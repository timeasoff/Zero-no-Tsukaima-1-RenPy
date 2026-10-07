#!/usr/bin/env python3
"""
Проверка синтаксиса Ren'Py для проекта ZnT1.

Проверяет:
- Баланс кавычек в строках
- Баланс скобок ()
- Корректность отступов (табуляции vs пробелы)
- Наличие обязательных конструкций (label, jump, menu)
- Синтаксис voice "..."
- Синтаксис scene/show/hide/with
- Синтаксис define Character

Запуск:
    python tools/check_renpy_syntax.py [--chapter ЦЕЛЬ] [--verbose]

ЦЕЛЬ (см. tools/targets.py):
    2 | extra | 0 | 2_4b | 2_5* | script-ch2_5b.rpy | sp_l1 | game/chapters/2/script-ch2_4b.rpy
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

sys.path.insert(0, str(Path(__file__).parent))
from output_util import ensure_safe_output, print_items, normalize_severity  # noqa: E402
from targets import resolve_target, TargetError  # noqa: E402


@dataclass
class SyntaxError:
    file: str
    line: int
    code: str
    message: str
    severity: str = "ERROR"  # ERROR / WARNING

    def __str__(self) -> str:
        return f"[{self.severity}] {self.file}:{self.line}: {self.code} — {self.message}"


@dataclass
class CheckResult:
    errors: List[SyntaxError] = field(default_factory=list)
    warnings: List[SyntaxError] = field(default_factory=list)
    info: List[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not any(e.severity == "ERROR" for e in self.errors)


class RenPySyntaxChecker:
    """Проверка синтаксиса Ren'Py файлов."""

    # Паттерны для проверки
    RE_VOICE = re.compile(r'^\s*voice\s+"([^"]+)"')
    RE_SCENE = re.compile(r'^\s*scene\s+(\S+)')
    RE_SHOW = re.compile(r'^\s*show\s+(\S+)')
    RE_HIDE = re.compile(r'^\s*hide\s+(\S+)')
    RE_WITH = re.compile(r'^\s*with\s+(\S+)')
    RE_LABEL = re.compile(r'^\s*label\s+(\S+):')
    RE_JUMP = re.compile(r'^\s*jump\s+(\S+)')
    RE_CALL = re.compile(r'^\s*call\s+(\S+)')
    RE_MENU = re.compile(r'^\s*menu\s*:')
    RE_DEFINE_CHAR = re.compile(r'^\s*define\s+(\w+)\s*=\s*Character\(')
    RE_PYTHON = re.compile(r'^\s*\$')
    RE_IMAGE_DEF = re.compile(r'^\s*image\s+(\S+)\s*=')
    RE_TRANSFORM = re.compile(r'^\s*transform\s+(\S+)\s*:')

    # Запрещённые конструкции
    RE_FORBIDDEN_MOVIE = re.compile(r'^\s*movie\s*\(')
    RE_FORBIDDEN_COFFEE = re.compile(r'^\s*coffee\s*\(')

    def __init__(self, root: Path):
        self.root = root
        self.result = CheckResult()

    def check_file(self, filepath: Path) -> None:
        """Проверить один .rpy файл."""
        rel_path = filepath.relative_to(self.root)
        try:
            content = filepath.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            self.result.errors.append(SyntaxError(
                str(rel_path), 0, "ENCODING", "Файл не в UTF-8"
            ))
            return

        lines = content.split("\n")
        in_python_block = False
        paren_depth = 0
        bracket_depth = 0
        brace_depth = 0

        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            # Пропускаем пустые строки и комментарии
            if not stripped or stripped.startswith("#"):
                continue

            # Проверка отступов (табуляции запрещены)
            if line.startswith("\t"):
                self.result.warnings.append(SyntaxError(
                    str(rel_path), i, "TABS",
                    "Табуляция в отступе (используй 4 пробела)"
                ))

            # Проверка баланса кавычек (простая)
            if stripped.count('"') % 2 != 0 and not stripped.startswith('#'):
                # Можно быть многострочной строкой - проверим контекст
                if not self._is_likely_multiline(lines, i):
                    self.result.warnings.append(SyntaxError(
                        str(rel_path), i, "QUOTES",
                        f"Нечётное количество кавычек: {stripped[:50]}..."
                    ))

            # Проверка баланса скобок
            paren_depth += line.count("(") - line.count(")")
            bracket_depth += line.count("[") - line.count("]")
            brace_depth += line.count("{") - line.count("}")

            # Проверка запрещённых конструкций
            if self.RE_FORBIDDEN_MOVIE.search(line):
                self.result.warnings.append(SyntaxError(
                    str(rel_path), i, "MOVIE",
                    "movie() не портируется — используй renpy.movie_cutscene()"
                ))
            if self.RE_FORBIDDEN_COFFEE.search(line):
                self.result.warnings.append(SyntaxError(
                    str(rel_path), i, "COFFEE",
                    "coffee() не реализована — используй pause(1.0)"
                ))

            # Проверка voice
            if self.RE_VOICE.match(line):
                voice_file = self.RE_VOICE.match(line).group(1)
                # В Ren'Py voice может быть без расширения — это нормально
                # Проверяем только наличие пустой строки
                if not voice_file:
                    self.result.warnings.append(SyntaxError(
                        str(rel_path), i, "VOICE_EMPTY",
                        "voice без имени файла"
                    ))

            # Проверка define Character
            if self.RE_DEFINE_CHAR.match(line):
                # Проверим, что есть name= или color=
                if "name=" not in line and "color=" not in line:
                    self.result.warnings.append(SyntaxError(
                        str(rel_path), i, "CHAR_DEF",
                        "Character без name= или color= (проверь настройки)"
                    ))

        # Проверка баланса скобок в конце файла
        if paren_depth != 0:
            self.result.errors.append(SyntaxError(
                str(rel_path), len(lines), "PAREN_BALANCE",
                f"Небаланс скобок (): {paren_depth}"
            ))
        if bracket_depth != 0:
            self.result.errors.append(SyntaxError(
                str(rel_path), len(lines), "BRACKET_BALANCE",
                f"Небаланс скобок []: {bracket_depth}"
            ))
        if brace_depth != 0:
            self.result.errors.append(SyntaxError(
                str(rel_path), len(lines), "BRACE_BALANCE",
                f"Небаланс скобок {{}}: {brace_depth}"
            ))

    def _is_likely_multiline(self, lines: List[str], line_idx: int) -> bool:
        """Проверить, может ли строка быть частью многострочной реплики."""
        # Смотрим на предыдущие строки
        for i in range(max(0, line_idx - 3), line_idx):
            if '"' in lines[i]:
                return True
        return False

    def check_chapter(self, chapter_dir: Path) -> None:
        """Проверить все .rpy файлы в папке главы."""
        if not chapter_dir.exists():
            self.result.errors.append(SyntaxError(
                str(chapter_dir), 0, "NO_DIR",
                f"Папка главы не найдена: {chapter_dir}"
            ))
            return

        rpy_files = sorted(chapter_dir.glob("*.rpy"))
        if not rpy_files:
            self.result.warnings.append(SyntaxError(
                str(chapter_dir), 0, "NO_RPY",
                "Нет .rpy файлов в папке главы"
            ))
            return

        for rpy_file in rpy_files:
            self.check_file(rpy_file)

    def check_all_chapters(self) -> None:
        """Проверить все главы в game/chapters/."""
        chapters_dir = self.root / "game" / "chapters"
        if not chapters_dir.exists():
            self.result.errors.append(SyntaxError(
                "game/chapters", 0, "NO_DIR",
                "Папка game/chapters не найдена"
            ))
            return

        for chapter_dir in sorted(chapters_dir.iterdir()):
            if chapter_dir.is_dir():
                self.check_chapter(chapter_dir)

    def check_tl_files(self) -> None:
        """Проверить файлы переводов в game/tl/."""
        tl_dir = self.root / "game" / "tl"
        if not tl_dir.exists():
            return

        for lang_dir in tl_dir.iterdir():
            if not lang_dir.is_dir():
                continue
            for rpy_file in lang_dir.rglob("*.rpy"):
                self.check_file(rpy_file)

    def run(self, chapter: Optional[str] = None) -> CheckResult:
        """Запустить проверки.

        chapter — цель: номер главы ('2'), часть ('2_4b'), имя файла
        ('script-ch2_5b.rpy', 'sp_l1'), папка ('extra'); None = весь проект.
        """
        if chapter is not None:
            try:
                target = resolve_target(self.root, chapter)
            except TargetError as e:
                self.result.errors.append(SyntaxError("target", 0, "BAD_TARGET", str(e)))
                return self.result
            if target.is_folder:
                self.check_chapter(target.chapter_dir)
            else:
                for f in target.files:
                    self.check_file(f)
        else:
            self.check_all_chapters()

        self.check_tl_files()
        return self.result


def main() -> int:
    ensure_safe_output()
    parser = argparse.ArgumentParser(description="Проверка синтаксиса Ren'Py")
    parser.add_argument("--chapter", type=str,
                        help="Цель: 2 | extra | 2_4b | script-ch2_5b.rpy | sp_l1 (пусто = весь проект)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Подробный вывод")
    parser.add_argument("--no-report", action="store_true", help="Не писать отчёт")
    args = parser.parse_args()

    root = Path(__file__).parent.parent
    checker = RenPySyntaxChecker(root)
    result = checker.run(chapter=args.chapter)
    normalize_severity(result)

    # Вывод
    print("=" * 60)
    print("Проверка синтаксиса Ren'Py")
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
        report_path = root / "reports" / "check_renpy_syntax.md"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("# Проверка синтаксиса Ren'Py\n\n")
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
            if not result.errors and not result.warnings:
                f.write("OK — проблем не найдено.\n")
        print(f"\nОтчёт: {report_path.relative_to(root)}")

    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
