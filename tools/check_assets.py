#!/usr/bin/env python3
"""
Проверка ассетов для проекта ZnT1.

Проверяет:
- Наличие файлов изображений (BG, CG, спрайты) по image_id_map.csv
- Наличие файлов звуков (BGM, SE)
- Наличие файлов голосов (.ogg)
- Использование transcriptions_ja_ru.csv
- Статистику по использованию ассетов

Запуск:
    python tools/check_assets.py [--chapter N] [--verbose]
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
class AssetError:
    file: str
    code: str
    message: str
    severity: str = "ERROR"

    def __str__(self) -> str:
        return f"[{self.severity}] {self.file}: {self.code} — {self.message}"


@dataclass
class AssetResult:
    errors: List[AssetError] = field(default_factory=list)
    warnings: List[AssetError] = field(default_factory=list)
    info: List[str] = field(default_factory=list)
    stats: Dict[str, int] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not any(e.severity == "ERROR" for e in self.errors)


class AssetChecker:
    """Проверка ассетов."""

    # Паттерны
    RE_VOICE_REF = re.compile(r'voice\s+"([^"]+)"')
    RE_BGM_REF = re.compile(r'play\s+music\s+"([^"]+)"')
    RE_SE_REF = re.compile(r'play\s+sound\s+"([^"]+)"')
    RE_IMAGE_REF = re.compile(r'scene\s+(\S+)|show\s+(\S+)|hide\s+(\S+)')
    # Строка CSV: [## ]VOICE_ID.BIN_<hex8>.wav; отметка использования — в status
    RE_VOICE_ROW = re.compile(r"^(#+\s*)?VOICE_ID\.BIN_([0-9A-Fa-f]{8})\.(wav|WAV|STV)$")
    RE_STATUS_MARK = re.compile(r"\bch\d[\w.]*_\w+_\d+")

    def __init__(self, root: Path):
        self.root = root
        self.result = AssetResult()
        self.image_map: Dict[str, Dict[str, str]] = {}
        self.voice_map: Dict[str, str] = {}  # voice_name -> voice_id
        self.transcriptions: Dict[str, Dict[str, str]] = {}  # активная очередь
        self.consumed_ids: Set[str] = set()  # строки, помеченные использованными
        self.used_voice_ids: Set[str] = set()  # голоса в проверенной выборке
        self._load_image_map()
        self._load_voice_map()
        self._load_transcriptions()

    def _load_image_map(self) -> None:
        """Загрузить карту изображений."""
        map_file = self.root / "references" / "image_id_map.csv"
        if not map_file.exists():
            self.result.warnings.append(AssetError(
                "references/image_id_map.csv", "NO_MAP",
                "Файл image_id_map.csv не найден"
            ))
            return

        with open(map_file, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                image_id = (row.get("image_id") or "").strip()
                if image_id:
                    self.image_map[image_id] = row

    def _load_voice_map(self) -> None:
        """Загрузить карту голосов (пропускает строки-комментарии CSV)."""
        map_file = self.root / "references" / "voice_id_map.csv"
        if not map_file.exists():
            return

        with open(map_file, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                voice_name = (row.get("voice_name") or "").strip()
                voice_id = (row.get("voice_id") or "").strip()
                if voice_name and voice_id and not voice_name.startswith("#"):
                    self.voice_map[voice_name] = voice_id

    def _load_transcriptions(self) -> None:
        """Загрузить transcriptions_ja_ru.csv.

        Ключ — десятичный voice_id из имени VOICE_ID.BIN_<hex8>.wav.
        Строки с префиксом '## ' или с именем голоса в status считаются
        ПОМеченными использованными (consumed), остальные — активная очередь.
        """
        trans_file = self.root / "transcriptions_ja_ru.csv"
        if not trans_file.exists():
            return

        with open(trans_file, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                fn = (row.get("filename") or "").strip()
                status = row.get("status") or ""
                m = self.RE_VOICE_ROW.match(fn)
                if not m:
                    continue
                voice_id = str(int(m.group(2), 16))
                if m.group(1) or self.RE_STATUS_MARK.search(status):
                    self.consumed_ids.add(voice_id)
                else:
                    self.transcriptions[voice_id] = row

    def check_chapter(self, chapter_dir: Path) -> None:
        """Проверить ассеты в главе."""
        if not chapter_dir.exists():
            return

        chapter_voices: Set[str] = set()
        chapter_images: Set[str] = set()

        for rpy_file in sorted(chapter_dir.glob("*.rpy")):
            rel_path = rpy_file.relative_to(self.root)
            try:
                content = rpy_file.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue

            # Проверка голосов
            for match in self.RE_VOICE_REF.finditer(content):
                voice_file = match.group(1)
                chapter_voices.add(voice_file)
                self._check_voice_file(rel_path, voice_file)

            # Проверка изображений
            for match in self.RE_IMAGE_REF.finditer(content):
                image_name = match.group(1) or match.group(2) or match.group(3)
                if image_name and not image_name.startswith("id("):
                    chapter_images.add(image_name)

        # Обновляем статистику
        self.result.stats[f"chapter_{chapter_dir.name}_voices"] = len(chapter_voices)
        self.result.stats[f"chapter_{chapter_dir.name}_images"] = len(chapter_images)

    def _check_voice_file(self, rel_path: Path, voice_file: str) -> None:
        """Проверить существование голосового файла (.ogg в game/audio/voices/)."""
        # Голос в проверенной выборке (для статистики против очереди CSV)
        vid = self.voice_map.get(voice_file)
        if vid:
            self.used_voice_ids.add(vid)

        voices_dir = self.root / "game" / "audio" / "voices"
        # Имя в voice "..." без расширения; на диске — .ogg (см. voice-workflow)
        if (voices_dir / f"{voice_file}.ogg").exists() or (voices_dir / voice_file).exists():
            return
        self.result.errors.append(AssetError(
            str(rel_path), "VOICE_MISSING",
            f"Голосовой файл не найден: {voice_file}.ogg"
        ))

    def check_voice_transcriptions(self) -> None:
        """Статистика голосов против transcriptions_ja_ru.csv (очередь непортированного).

        Использованный голос удаляется из CSV, поэтому «взят из CSV» = id
        отсутствует в очереди. Детальная построчная проверка —
        tools/check_voice_transcriptions.py.
        """
        if not self.transcriptions:
            self.result.info.append("transcriptions_ja_ru.csv не найден или пуст")
            return

        queue = set(self.transcriptions.keys())
        used = self.used_voice_ids
        consumed = used - queue
        still = used & queue

        self.result.stats["voices_used_in_scope"] = len(used)
        self.result.stats["voices_used_row_consumed"] = len(consumed)
        self.result.stats["voices_used_row_still_in_queue"] = len(still)
        self.result.stats["transcriptions_queue_rows"] = len(queue)
        self.result.stats["transcriptions_consumed_rows"] = len(self.consumed_ids)

        if still:
            self.result.warnings.append(AssetError(
                "transcriptions_ja_ru.csv", "ROWS_NOT_CONSUMED",
                f"{len(still)} использованных голосов не помечены в очереди CSV "
                f"(первые 10: {', '.join(sorted(still)[:10])})"
            ))

        self.result.info.append(
            f"В очереди transcriptions_ja_ru.csv: {len(queue)} строк "
            f"(помечено использованными: {len(self.consumed_ids)}); "
            f"из проверенной выборки помечено: {len(consumed)}"
        )

    def check_image_map(self) -> None:
        """Проверить карту изображений."""
        if not self.image_map:
            return

        total = len(self.image_map)
        named = sum(1 for row in self.image_map.values()
                    if (row.get("filename") or "").strip())
        unnamed = total - named

        self.result.stats["images_total"] = total
        self.result.stats["images_named"] = named
        self.result.stats["images_unnamed"] = unnamed

        if unnamed > 0:
            self.result.info.append(
                f"image_id_map.csv: {unnamed}/{total} ID без filename (ожидают заполнения)"
            )

    def check_all_chapters(self) -> None:
        """Проверить все главы."""
        chapters_dir = self.root / "game" / "chapters"
        if not chapters_dir.exists():
            return

        for chapter_dir in sorted(chapters_dir.iterdir()):
            if chapter_dir.is_dir():
                self.check_chapter(chapter_dir)

    def run(self, chapter: Optional[int] = None) -> AssetResult:
        """Запустить проверки."""
        if chapter is not None:
            chapter_dir = self.root / "game" / "chapters" / str(chapter)
            self.check_chapter(chapter_dir)
        else:
            self.check_all_chapters()

        self.check_voice_transcriptions()
        self.check_image_map()
        return self.result


def main() -> int:
    ensure_safe_output()
    parser = argparse.ArgumentParser(description="Проверка ассетов")
    parser.add_argument("--chapter", type=int, help="Проверить только главу N")
    parser.add_argument("--verbose", "-v", action="store_true", help="Подробный вывод")
    parser.add_argument("--no-report", action="store_true", help="Не писать отчёт")
    args = parser.parse_args()

    root = Path(__file__).parent.parent
    checker = AssetChecker(root)
    result = checker.run(chapter=args.chapter)
    normalize_severity(result)

    # Вывод
    print("=" * 60)
    print("Проверка ассетов")
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
        report_path = root / "reports" / "check_assets.md"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("# Проверка ассетов\n\n")
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
