#!/usr/bin/env python3
"""
Проверка озвучки по transcriptions_ja_ru.csv для проекта ZnT1.

Проверяет:
- Использование голосов из transcriptions_ja_ru.csv в скриптах
- Наличие пар voice_name <-> voice_id в voice_id_map.csv
- Статусы транскрипций (использовано/не использовано)
- Отсутствующие транскрипции для используемых голосов

Запуск:
    python tools/check_voice_transcriptions.py [--chapter N] [--verbose]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Dict, Set, Tuple

sys.path.insert(0, str(Path(__file__).parent))
from output_util import ensure_safe_output, print_items, normalize_severity  # noqa: E402


@dataclass
class VoiceError:
    file: str
    code: str
    message: str
    severity: str = "ERROR"

    def __str__(self) -> str:
        return f"[{self.severity}] {self.file}: {self.code} — {self.message}"


@dataclass
class VoiceResult:
    errors: List[VoiceError] = field(default_factory=list)
    warnings: List[VoiceError] = field(default_factory=list)
    info: List[str] = field(default_factory=list)
    stats: Dict[str, int] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not any(e.severity == "ERROR" for e in self.errors)


class VoiceTranscriptionChecker:
    """Проверка озвучки по транскрипциям."""

    RE_VOICE_REF = re.compile(r'voice\s+"([^"]+)"')
    # Строка CSV: [## ]VOICE_ID.BIN_<hex8>.wav
    RE_VOICE_ROW = re.compile(r"^(#+\s*)?VOICE_ID\.BIN_([0-9A-Fa-f]{8})\.(wav|WAV|STV)$")
    # Отметка использованного в status: имя голоса ch2.6_s_003 [.wav]
    RE_STATUS_MARK = re.compile(r"\bch\d[\w.]*_\w+_\d+")

    def __init__(self, root: Path):
        self.root = root
        self.result = VoiceResult()
        self.transcriptions: Dict[str, Dict[str, str]] = {}  # активная очередь
        self.consumed_ids: Set[str] = set()  # строки, помеченные использованными
        self.voice_map: Dict[str, str] = {}  # voice_name -> voice_id
        self.used_voices: Dict[str, Set[str]] = {}  # voice_id -> set of files
        self._load_transcriptions()
        self._load_voice_map()

    def _load_transcriptions(self) -> None:
        """Загрузить транскрипции.

        Формат: filename,original,translation,status (UTF-8 с BOM).
        Ключ — десятичный voice_id, вычисленный из имени
        VOICE_ID.BIN_<hex8>.wav. Строки-секции и закомментированные пропускаются.
        Использованные голоса УДАЛЯЮТСЯ из CSV (очередь непортированного).
        """
        trans_file = self.root / "transcriptions_ja_ru.csv"
        if not trans_file.exists():
            self.result.warnings.append(VoiceError(
                "transcriptions_ja_ru.csv", "NO_FILE",
                "Файл transcriptions_ja_ru.csv не найден"
            ))
            return

        with open(trans_file, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            skipped = 0  # секции-закладки и не-голосовые строки
            for row in reader:
                fn = (row.get("filename") or "").strip()
                status = row.get("status") or ""
                m = self.RE_VOICE_ROW.match(fn)
                if not m:
                    skipped += 1
                    continue
                voice_id = str(int(m.group(2), 16))
                if m.group(1) or self.RE_STATUS_MARK.search(status):
                    self.consumed_ids.add(voice_id)   # помечено использованным
                else:
                    self.transcriptions[voice_id] = row  # активная строка очереди

        self.result.stats["transcriptions_queue_rows"] = len(self.transcriptions)
        self.result.stats["transcriptions_consumed_rows"] = len(self.consumed_ids)
        if skipped:
            self.result.stats["transcriptions_skipped_rows"] = skipped

    def _load_voice_map(self) -> None:
        """Загрузить карту голосов (пропускает строки-комментарии CSV)."""
        map_file = self.root / "references" / "voice_id_map.csv"
        if not map_file.exists():
            self.result.warnings.append(VoiceError(
                "references/voice_id_map.csv", "NO_MAP",
                "Файл voice_id_map.csv не найден"
            ))
            return

        with open(map_file, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                voice_name = (row.get("voice_name") or "").strip()
                voice_id = (row.get("voice_id") or "").strip()
                if voice_name and voice_id and not voice_name.startswith("#"):
                    self.voice_map[voice_name] = voice_id

        self.result.stats["manifest_pairs"] = len(self.voice_map)

    def check_chapter(self, chapter_dir: Path) -> None:
        """Проверить голоса в главе."""
        if not chapter_dir.exists():
            return

        for rpy_file in sorted(chapter_dir.glob("*.rpy")):
            rel_path = rpy_file.relative_to(self.root)
            try:
                content = rpy_file.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue

            for match in self.RE_VOICE_REF.finditer(content):
                voice_file = match.group(1)
                self._check_voice_usage(rel_path, voice_file)

    def _check_voice_usage(self, rel_path: Path, voice_file: str) -> None:
        """Проверить использование голоса."""
        # Ищем voice_id по имени файла
        voice_id = self.voice_map.get(voice_file)
        if not voice_id:
            self.result.warnings.append(VoiceError(
                str(rel_path), "VOICE_NOT_IN_MAP",
                f"Голос {voice_file} не найден в voice_id_map.csv"
            ))
            return

        # Регистрируем использование
        if voice_id not in self.used_voices:
            self.used_voices[voice_id] = set()
        self.used_voices[voice_id].add(str(rel_path))

        # Использованный голос: строка должна быть удалена/помечена в CSV
        # (transcriptions_ja_ru.csv — очередь непортированного)
        if voice_id in self.transcriptions:
            self.result.warnings.append(VoiceError(
                str(rel_path), "TRANSCRIPT_ROW_STILL_IN_QUEUE",
                f"Голос {voice_file} (id={voice_id}) использован, но его строка "
                f"всё ещё в transcriptions_ja_ru.csv — удалить/пометить"
            ))

    def check_all_chapters(self) -> None:
        """Проверить все главы."""
        chapters_dir = self.root / "game" / "chapters"
        if not chapters_dir.exists():
            return

        for chapter_dir in sorted(chapters_dir.iterdir()):
            if chapter_dir.is_dir():
                self.check_chapter(chapter_dir)

    def compute_stats(self) -> None:
        """Вычислить статистику.

        transcriptions_ja_ru.csv — очередь непортированного: использованный голос
        удаляется из неё. Поэтому «взято из CSV» = id отсутствует в очереди.
        """
        queue_ids = set(self.transcriptions.keys())
        used_ids = set(self.used_voices.keys())
        manifest_ids = {str(v) for v in self.voice_map.values()}

        consumed_by_scan = used_ids - queue_ids          # сканируемая выборка, строка помечена/удалена
        still_in_queue = used_ids & queue_ids            # использован, но строка не обработана
        manifest_consumed = manifest_ids - queue_ids     # весь манифест: строка помечена/удалена
        manifest_in_queue = manifest_ids & queue_ids

        self.result.stats["voices_used_in_scripts"] = len(used_ids)
        self.result.stats["voices_used_row_consumed"] = len(consumed_by_scan)
        self.result.stats["voices_used_row_still_in_queue"] = len(still_in_queue)
        self.result.stats["manifest_ids_row_consumed"] = len(manifest_consumed)
        self.result.stats["manifest_ids_row_in_queue"] = len(manifest_in_queue)

        if still_in_queue:
            first = sorted(still_in_queue)[:10]
            self.result.warnings.append(VoiceError(
                "transcriptions_ja_ru.csv", "ROWS_NOT_CONSUMED",
                f"{len(still_in_queue)} использованных голосов всё ещё в очереди "
                f"(первые 10: {', '.join(first)})"
            ))

        if manifest_in_queue:
            self.result.info.append(
                f"{len(manifest_in_queue)} id из манифеста есть в очереди CSV "
                "(строка не удалена/не помечена)"
            )

    def run(self, chapter: Optional[int] = None) -> VoiceResult:
        """Запустить проверки."""
        if chapter is not None:
            chapter_dir = self.root / "game" / "chapters" / str(chapter)
            self.check_chapter(chapter_dir)
        else:
            self.check_all_chapters()

        self.compute_stats()
        return self.result


def main() -> int:
    ensure_safe_output()
    parser = argparse.ArgumentParser(description="Проверка озвучки по транскрипциям")
    parser.add_argument("--chapter", type=int, help="Проверить только главу N")
    parser.add_argument("--verbose", "-v", action="store_true", help="Подробный вывод")
    parser.add_argument("--no-report", action="store_true", help="Не писать отчёт")
    args = parser.parse_args()

    root = Path(__file__).parent.parent
    checker = VoiceTranscriptionChecker(root)
    result = checker.run(chapter=args.chapter)
    normalize_severity(result)

    # Вывод
    print("=" * 60)
    print("Проверка озвучки по transcriptions_ja_ru.csv")
    print("=" * 60)

    if result.errors:
        print_items(result.errors, 20, f"\nERROR ({len(result.errors)}):")

    if result.warnings:
        print_items(result.warnings, 20, f"\nWARNING ({len(result.warnings)}):")

    if result.info:
        print(f"\nINFO ({len(result.info)}):")
        for i in result.info:
            print(f"  {i}")

    # Статистика
    if result.stats:
        print(f"\nСтатистика:")
        for key, value in sorted(result.stats.items()):
            print(f"  {key}: {value}")

    if not result.errors and not result.warnings:
        print("\nOK — проблем не найдено.")
    elif not result.errors:
        print(f"\nOK (с предупреждениями): {len(result.warnings)} warning(s)")
    else:
        print(f"\nERRORS: {len(result.errors)} error(s), {len(result.warnings)} warning(s)")

    # Запись отчёта
    if not args.no_report:
        report_path = root / "reports" / "check_voice_transcriptions.md"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("# Проверка озвучки по transcriptions_ja_ru.csv\n\n")
            f.write(f"Дата: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            if result.errors:
                f.write(f"## ERROR ({len(result.errors)})\n\n")
                for e in result.errors:
                    f.write(f"- {e}\n")
                f.write("\n")
            if result.warnings:
                f.write(f"## WARNING ({len(result.warnings)})\n\n")
                for w in result.warnings:
                    f.write(f"- {w}\n")
                f.write("\n")
            if result.info:
                f.write(f"## INFO ({len(result.info)})\n\n")
                for i in result.info:
                    f.write(f"- {i}\n")
                f.write("\n")
            if result.stats:
                f.write("## Статистика\n\n")
                for key, value in sorted(result.stats.items()):
                    f.write(f"- {key}: {value}\n")
                f.write("\n")
            if not result.errors and not result.warnings:
                f.write("OK — проблем не найдено.\n")
        print(f"\nОтчёт: {report_path.relative_to(root)}")

    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
