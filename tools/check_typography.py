#!/usr/bin/env python3
"""
Проверка типографики для проекта ZnT1.

Области проверки зависят от --lang:
- ru:  только строки `new "..."` в game/tl/russian/** (кроме read-only common.rpy);
        при --chapter — только пары, чей `old` встречается в тексте этой главы.
- en:  только текстовые строки в game/chapters/<N>/** (EN-база в сценарии).
- ja:  только строки `new "..."` в game/tl/japanese/**; JA дословен из источника,
        поэтому троеточие источника '......' — INFO, не ошибка.

Проверки (EN/RU):
- ELLIPSIS:   '...' тремя точками вместо символа '…' (PROMTS.md п.5)
- QUOTES (ru): прямые кавычки " вместо «ёлочек»
- BRACKET_THOUGHT: реплика, целиком обёрнутая в скобки (в EN/RU мысль — курсив _…_)
- DOUBLE_SPACE / SPACE_BEFORE_PUNCT: предупреждения

Запуск:
    python tools/check_typography.py [--chapter N] [--lang ru|en|ja] [--verbose]
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set

sys.path.insert(0, str(Path(__file__).parent))
from output_util import ensure_safe_output, safe_print, print_items, normalize_severity  # noqa: E402

# Read-only файлы tl (AGENTS.md, раздел «Инфраструктура») — из проверок исключены.
READONLY_TL_FILES = {"common.rpy"}

# Язык -> имя каталога game/tl/<dir>
TL_DIRS = {"ru": "russian", "ja": "japanese", "en": "english"}

# Ключевые слова Ren'Py: строка после них — код, не реплика.
CODE_SPEAKERS = {
    "voice", "scene", "show", "hide", "jump", "call", "with", "define",
    "image", "transform", "play", "stop", "queue", "window", "pause",
    "python", "return", "pass", "if", "elif", "else", "while", "for",
    "translate", "camera", "at", "using", "style", "$",
}

RE_TL_LINE = re.compile(r'^\s*(?P<kw>old|new)\s+"(?P<body>.*)"\s*$')
RE_SPEAKER_LINE = re.compile(r'^\s*(?P<sp>[A-Za-z_][\w.]*)\s+"(?P<body>.*)"\s*$')
RE_BARE_LINE = re.compile(r'^\s*"(?P<body>.*)"\s*$')

RE_ELLIPSIS_THREE_DOTS = re.compile(r'\.\.\.')
RE_SPACE_BEFORE_PUNCT = re.compile(r'\s[.,;:!?]')
RE_DOUBLE_SPACE = re.compile(r'  +')
RE_SPACE_AFTER_OPEN_QUOTE = re.compile(r'«\s')
RE_SPACE_BEFORE_CLOSE_QUOTE = re.compile(r'\s»')


@dataclass
class TypoError:
    file: str
    line: int
    code: str
    message: str
    severity: str = "ERROR"

    def __str__(self) -> str:
        return f"[{self.severity}] {self.file}:{self.line}: {self.code} — {self.message}"


@dataclass
class TypoResult:
    errors: List[TypoError] = field(default_factory=list)
    warnings: List[TypoError] = field(default_factory=list)
    info: List[str] = field(default_factory=list)
    stats: Dict[str, int] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not any(e.severity == "ERROR" for e in self.errors)


class TypographyChecker:
    """Проверка типографики текста."""

    def __init__(self, root: Path):
        self.root = root
        self.result = TypoResult()

    # ------------------------------------------------------------------
    # Разбор строк
    # ------------------------------------------------------------------

    @staticmethod
    def _extract(line: str) -> Optional[tuple]:
        """Вернуть (kw, body): kw in {'old','new',None} или None, если строка — код."""
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            return None

        m = RE_TL_LINE.match(line)
        if m:
            return m.group("kw"), m.group("body")

        m = RE_SPEAKER_LINE.match(line)
        if m:
            sp = m.group("sp")
            if sp in CODE_SPEAKERS:
                return None
            return None, m.group("body")

        m = RE_BARE_LINE.match(line)
        if m:
            return None, m.group("body")

        return None

    # ------------------------------------------------------------------
    # Проверки текста
    # ------------------------------------------------------------------

    def _check_body(self, rel: str, line_num: int, body: str, lang: str,
                    kind: str) -> None:
        """kind: 'dialogue' (реплика) или 'new' (перевод)."""
        # Троеточие
        if RE_ELLIPSIS_THREE_DOTS.search(body):
            self.result.errors.append(TypoError(
                rel, line_num, "ELLIPSIS",
                "Многоточие '...' тремя точками вместо символа '…'"
            ))

        # Кавычки (только RU)
        if lang == "ru" and '"' in body:
            self.result.errors.append(TypoError(
                rel, line_num, "QUOTES",
                "Прямые кавычки в русском тексте — нужны «ёлочки»"
            ))

        # Реплика/мысль, целиком обёрнутая в скобки (в EN/RU — курсив _…_)
        s = body.strip()
        if len(s) > 3 and s.startswith("(") and s.endswith(")") and not s.startswith("id("):
            self.result.errors.append(TypoError(
                rel, line_num, "BRACKET_THOUGHT",
                f"Текст целиком в скобках: {s[:50]} — для мыслей использовать _…_"
            ))

        # Двойной пробел (не в начале — начало это уже отступ/разметка)
        if RE_DOUBLE_SPACE.search(body):
            self.result.warnings.append(TypoError(
                rel, line_num, "DOUBLE_SPACE", "Двойной пробел в тексте"
            ))

        # Пробел перед знаком препинания
        if RE_SPACE_BEFORE_PUNCT.search(body):
            self.result.warnings.append(TypoError(
                rel, line_num, "SPACE_BEFORE_PUNCT",
                f"Пробел перед знаком препинания: {body[:50]}"
            ))

        # Пробел у «ёлочек»
        if lang == "ru":
            if RE_SPACE_AFTER_OPEN_QUOTE.search(body):
                self.result.warnings.append(TypoError(
                    rel, line_num, "QUOTE_SPACE", "Пробел после «"
                ))
            if RE_SPACE_BEFORE_CLOSE_QUOTE.search(body):
                self.result.warnings.append(TypoError(
                    rel, line_num, "QUOTE_SPACE", "Пробел перед »"
                ))

    # ------------------------------------------------------------------
    # Сбор EN-текстов главы (для скоупинга RU по главе)
    # ------------------------------------------------------------------

    def _chapter_en_texts(self, chapter: int) -> Set[str]:
        texts: Set[str] = set()
        chapter_dir = self.root / "game" / "chapters" / str(chapter)
        if not chapter_dir.exists():
            return texts
        for rpy in sorted(chapter_dir.glob("*.rpy")):
            try:
                content = rpy.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for line in content.split("\n"):
                parsed = self._extract(line)
                if parsed and parsed[0] is None and parsed[1]:
                    texts.add(parsed[1])
        return texts

    # ------------------------------------------------------------------
    # Файлы
    # ------------------------------------------------------------------

    def _tl_files(self, lang: str) -> List[Path]:
        tl_dir = self.root / "game" / "tl" / TL_DIRS.get(lang, lang)
        if not tl_dir.exists():
            return []
        return [f for f in sorted(tl_dir.rglob("*.rpy"))
                if f.name not in READONLY_TL_FILES]

    def _chapter_files(self, chapter: Optional[int]) -> List[Path]:
        chapters_dir = self.root / "game" / "chapters"
        if not chapters_dir.exists():
            return []
        if chapter is not None:
            dirs = [chapters_dir / str(chapter)]
        else:
            dirs = [d for d in sorted(chapters_dir.iterdir()) if d.is_dir()]
        files: List[Path] = []
        for d in dirs:
            if d.exists():
                files.extend(sorted(d.glob("*.rpy")))
        return files

    # ------------------------------------------------------------------
    # Режимы
    # ------------------------------------------------------------------

    def check_russian(self, chapter: Optional[int]) -> None:
        """RU: строки new в game/tl/russian (скоуп по главе через old)."""
        en_texts = self._chapter_en_texts(chapter) if chapter is not None else None
        checked = 0
        scoped_out = 0
        pending_old: Optional[str] = None

        for f in self._tl_files("ru"):
            rel = str(f.relative_to(self.root))
            try:
                content = f.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                self.result.errors.append(TypoError(rel, 0, "ENCODING", "Файл не в UTF-8"))
                continue
            for i, line in enumerate(content.split("\n"), 1):
                parsed = self._extract(line)
                if not parsed or parsed[0] is None:
                    continue
                kw, body = parsed
                if kw == "old":
                    pending_old = body
                    continue
                # kw == 'new'
                if en_texts is not None:
                    if pending_old is None or pending_old not in en_texts:
                        scoped_out += 1
                        pending_old = None
                        continue
                pending_old = None
                checked += 1
                self._check_body(rel, i, body, "ru", "new")

        self.result.stats["ru_strings_checked"] = checked
        self.result.stats["ru_strings_out_of_scope"] = scoped_out
        if chapter is not None:
            self.result.info.append(
                f"RU: проверено {checked} строк new, вне главы {chapter}: {scoped_out}"
            )

    def check_english(self, chapter: Optional[int]) -> None:
        """EN: текстовые строки в game/chapters/**."""
        checked = 0
        for f in self._chapter_files(chapter):
            rel = str(f.relative_to(self.root))
            try:
                content = f.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                self.result.errors.append(TypoError(rel, 0, "ENCODING", "Файл не в UTF-8"))
                continue
            for i, line in enumerate(content.split("\n"), 1):
                parsed = self._extract(line)
                if not parsed or parsed[0] is not None:
                    continue  # old/new не бывает в сценарии; код пропущен
                if not parsed[1]:
                    continue
                checked += 1
                self._check_body(rel, i, parsed[1], "en", "dialogue")

        self.result.stats["en_strings_checked"] = checked

    def check_japanese(self, chapter: Optional[int]) -> None:
        """JA: строки new в game/tl/japanese — дословный источник, только INFO."""
        dots = 0
        checked = 0
        for f in self._tl_files("ja"):
            rel = str(f.relative_to(self.root))
            try:
                content = f.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                self.result.errors.append(TypoError(rel, 0, "ENCODING", "Файл не в UTF-8"))
                continue
            for line in content.split("\n"):
                parsed = self._extract(line)
                if not parsed or parsed[0] != "new":
                    continue
                checked += 1
                if RE_ELLIPSIS_THREE_DOTS.search(parsed[1]):
                    dots += 1

        self.result.stats["ja_strings_checked"] = checked
        self.result.stats["ja_strings_with_dots"] = dots
        self.result.info.append(
            f"JA: {checked} строк new; '......' источника сохранено дословно: {dots} "
            "(INFO — замена на '…' только по решению редактора)"
        )

    # ------------------------------------------------------------------

    def run(self, chapter: Optional[int] = None, lang: str = "ru") -> TypoResult:
        if lang == "ru":
            self.check_russian(chapter)
        elif lang == "en":
            self.check_english(chapter)
        else:
            self.check_japanese(chapter)
        return self.result


def main() -> int:
    ensure_safe_output()
    parser = argparse.ArgumentParser(description="Проверка типографики")
    parser.add_argument("--chapter", type=int, help="Проверить только главу N")
    parser.add_argument("--lang", choices=["ru", "en", "ja"], default="ru",
                        help="Язык проверки (по умолчанию ru)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Подробный вывод")
    parser.add_argument("--no-report", action="store_true", help="Не писать отчёт")
    args = parser.parse_args()

    root = Path(__file__).parent.parent
    checker = TypographyChecker(root)
    result = checker.run(chapter=args.chapter, lang=args.lang)
    normalize_severity(result)

    safe_print("=" * 60)
    scope = f", chapter={args.chapter}" if args.chapter else ""
    safe_print(f"Проверка типографики (lang={args.lang}{scope})")
    safe_print("=" * 60)

    if result.errors:
        print_items(result.errors, limit=20, header=f"\nERROR ({len(result.errors)}):")

    if result.warnings and (args.verbose or not result.errors or args.no_report):
        print_items(result.warnings, limit=20, header=f"\nWARNING ({len(result.warnings)}):")
    elif result.warnings:
        safe_print(f"\nWARNING ({len(result.warnings)}) — см. отчёт")

    if result.info:
        safe_print(f"\nINFO:")
        for i in result.info:
            safe_print(f"  {i}")

    if result.stats:
        safe_print("\nSTATS:")
        for key, value in sorted(result.stats.items()):
            safe_print(f"  {key}: {value}")

    if not result.errors and not result.warnings:
        safe_print("\nOK — проблем не найдено.")
    elif not result.errors:
        safe_print(f"\nOK (с предупреждениями): {len(result.warnings)} warning(s)")
    else:
        safe_print(f"\nERRORS: {len(result.errors)} error(s), {len(result.warnings)} warning(s)")

    if not args.no_report:
        suffix = f"_ch{args.chapter}" if args.chapter else ""
        report_path = root / "reports" / f"check_typography_{args.lang}{suffix}.md"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(f"# Проверка типографики ({args.lang})\n\n")
            f.write(f"Дата: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            if args.chapter:
                f.write(f"Область: глава {args.chapter}\n\n")
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
                f.write("## INFO\n\n")
                for i in result.info:
                    f.write(f"- {i}\n")
                f.write("\n")
            if result.stats:
                f.write("## STATS\n\n")
                for key, value in sorted(result.stats.items()):
                    f.write(f"- {key}: {value}\n")
                f.write("\n")
            if not result.errors and not result.warnings:
                f.write("OK — проблем не найдено.\n")
        safe_print(f"\nОтчёт: {report_path.relative_to(root)}")

    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
