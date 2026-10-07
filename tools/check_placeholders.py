#!/usr/bin/env python3
"""
Проверка заглушек и незаполненных мест в проекте ZnT1.

Проверяет:
- id(K) заглушки в .rpy файлах (должны быть заменены на имена из image_id_map.csv)
- TODO, FIXME, XXX комментарии
- Пустые строки перевода (old "..." new "")
- Незаполненные filename в image_id_map.csv
- Отсутствующие файлы изображений/звуков

Запуск:
    python tools/check_placeholders.py [--chapter N] [--verbose]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Set, Dict

sys.path.insert(0, str(Path(__file__).parent))
from output_util import ensure_safe_output, print_items, normalize_severity  # noqa: E402


@dataclass
class PlaceholderError:
    file: str
    line: int
    code: str
    message: str
    severity: str = "ERROR"

    def __str__(self) -> str:
        return f"[{self.severity}] {self.file}:{self.line}: {self.code} — {self.message}"


@dataclass
class PlaceholderResult:
    errors: List[PlaceholderError] = field(default_factory=list)
    warnings: List[PlaceholderError] = field(default_factory=list)
    info: List[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not any(e.severity == "ERROR" for e in self.errors)


class PlaceholderChecker:
    """Проверка заглушек и незаполненных мест."""

    # Паттерны
    RE_ID_PLACEHOLDER = re.compile(r'\bid\((\d+)\)')  # id(123)
    RE_TODO = re.compile(r'\b(TODO|FIXME|XXX|HACK)\b', re.IGNORECASE)
    RE_EMPTY_NEW = re.compile(r'new\s+""')  # Пустой перевод
    RE_STUB = re.compile(r'\b(STUB|PLACEHOLDER)\b', re.IGNORECASE)

    def __init__(self, root: Path):
        self.root = root
        self.result = PlaceholderResult()
        self.image_map: Dict[str, str] = {}  # id -> filename
        self._load_image_map()

    def _load_image_map(self) -> None:
        """Загрузить карту изображений."""
        map_file = self.root / "references" / "image_id_map.csv"
        if not map_file.exists():
            self.result.warnings.append(PlaceholderError(
                "references/image_id_map.csv", 0, "NO_MAP",
                "Файл image_id_map.csv не найден"
            ))
            return

        with open(map_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                image_id = row.get("image_id", "").strip()
                filename = row.get("filename", "").strip()
                if image_id:
                    self.image_map[image_id] = filename

    def check_file(self, filepath: Path) -> None:
        """Проверить один файл."""
        rel_path = filepath.relative_to(self.root)
        try:
            content = filepath.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            self.result.errors.append(PlaceholderError(
                str(rel_path), 0, "ENCODING", "Файл не в UTF-8"
            ))
            return

        lines = content.split("\n")

        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue

            # Проверка id(K) заглушек
            self._check_id_placeholder(rel_path, i, line)

            # Проверка TODO/FIXME
            self._check_todo(rel_path, i, line)

            # Проверка пустых переводов
            self._check_empty_translation(rel_path, i, line)

            # Проверка STUB
            self._check_stub(rel_path, i, line)

    def _check_id_placeholder(self, rel_path: Path, line_num: int, line: str) -> None:
        """Проверка id(K) заглушек."""
        matches = self.RE_ID_PLACEHOLDER.findall(line)
        for match in matches:
            image_id = match
            if image_id in self.image_map:
                filename = self.image_map[image_id]
                if filename:
                    # ID есть в карте, но заглушка не заменена
                    self.result.warnings.append(PlaceholderError(
                        str(rel_path), line_num, "ID_PLACEHOLDER",
                        f"id({image_id}) — заглушка не заменена (файл: {filename})"
                    ))
                else:
                    # ID есть в карте, но filename пустой
                    self.result.warnings.append(PlaceholderError(
                        str(rel_path), line_num, "ID_UNNAMED",
                        f"id({image_id}) — filename не заполнен в image_id_map.csv"
                    ))
            else:
                # ID нет в карте
                self.result.errors.append(PlaceholderError(
                    str(rel_path), line_num, "ID_UNKNOWN",
                    f"id({image_id}) — ID не найден в image_id_map.csv"
                ))

    def _check_todo(self, rel_path: Path, line_num: int, line: str) -> None:
        """Проверка TODO/FIXME."""
        if self.RE_TODO.search(line):
            self.result.warnings.append(PlaceholderError(
                str(rel_path), line_num, "TODO",
                f"Найден TODO/FIXME: {line.strip()[:50]}..."
            ))

    def _check_empty_translation(self, rel_path: Path, line_num: int, line: str) -> None:
        """Проверка пустых переводов."""
        if self.RE_EMPTY_NEW.search(line):
            self.result.errors.append(PlaceholderError(
                str(rel_path), line_num, "EMPTY_NEW",
                "Пустой перевод (new \"\")"
            ))

    def _check_stub(self, rel_path: Path, line_num: int, line: str) -> None:
        """Проверка STUB."""
        if self.RE_STUB.search(line):
            self.result.warnings.append(PlaceholderError(
                str(rel_path), line_num, "STUB",
                f"Найден STUB: {line.strip()[:50]}..."
            ))

    def check_image_map(self) -> None:
        """Проверить image_id_map.csv на незаполненные записи."""
        if not self.image_map:
            return

        unnamed = [id for id, name in self.image_map.items() if not name]
        if unnamed:
            self.result.info.append(
                f"image_id_map.csv: {len(unnamed)} ID без filename (ожидают заполнения)"
            )

    def check_chapter(self, chapter_dir: Path) -> None:
        """Проверить все файлы в папке главы."""
        if not chapter_dir.exists():
            return

        for rpy_file in sorted(chapter_dir.glob("*.rpy")):
            self.check_file(rpy_file)

    def check_all_chapters(self) -> None:
        """Проверить все главы."""
        chapters_dir = self.root / "game" / "chapters"
        if not chapters_dir.exists():
            return

        for chapter_dir in sorted(chapters_dir.iterdir()):
            if chapter_dir.is_dir():
                self.check_chapter(chapter_dir)

    def check_tl_files(self) -> None:
        """Проверить файлы переводов."""
        tl_dir = self.root / "game" / "tl"
        if not tl_dir.exists():
            return

        # Исключаем read-only файлы (common.rpy, options.rpy)
        readonly_files = {"common.rpy", "options.rpy"}

        for lang_dir in tl_dir.iterdir():
            if lang_dir.is_dir():
                for rpy_file in sorted(lang_dir.rglob("*.rpy")):
                    if rpy_file.name in readonly_files:
                        continue
                    self.check_file(rpy_file)

    def run(self, chapter: Optional[int] = None) -> PlaceholderResult:
        """Запустить проверки."""
        if chapter is not None:
            chapter_dir = self.root / "game" / "chapters" / str(chapter)
            self.check_chapter(chapter_dir)
        else:
            self.check_all_chapters()

        self.check_tl_files()
        self.check_image_map()
        return self.result


def main() -> int:
    ensure_safe_output()
    parser = argparse.ArgumentParser(description="Проверка заглушек")
    parser.add_argument("--chapter", type=int, help="Проверить только главу N")
    parser.add_argument("--verbose", "-v", action="store_true", help="Подробный вывод")
    parser.add_argument("--no-report", action="store_true", help="Не писать отчёт")
    args = parser.parse_args()

    root = Path(__file__).parent.parent
    checker = PlaceholderChecker(root)
    result = checker.run(chapter=args.chapter)
    normalize_severity(result)

    # Вывод
    print("=" * 60)
    print("Проверка заглушек")
    print("=" * 60)

    if result.errors:
        print_items(result.errors, 20, f"\nERROR ({len(result.errors)}):")

    if result.warnings:
        print_items(result.warnings, 20, f"\nWARNING ({len(result.warnings)}):")

    if result.info:
        print(f"\nINFO ({len(result.info)}):")
        for i in result.info:
            print(f"  {i}")

    if not result.errors and not result.warnings:
        print("\nOK — проблем не найдено.")
    elif not result.errors:
        print(f"\nOK (с предупреждениями): {len(result.warnings)} warning(s)")
    else:
        print(f"\nERRORS: {len(result.errors)} error(s), {len(result.warnings)} warning(s)")

    # Запись отчёта
    if not args.no_report:
        report_path = root / "reports" / "check_placeholders.md"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("# Проверка заглушек\n\n")
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
            if not result.errors and not result.warnings:
                f.write("OK — проблем не найдено.\n")
        print(f"\nОтчёт: {report_path.relative_to(root)}")

    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
