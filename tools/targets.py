#!/usr/bin/env python3
"""
Разрешение цели проверки (target) для скриптов pipeline (ZnT1).

Цель задаёт, какие файлы главы проверяются. Принимаются формы:

    2                          — вся глава (папка game/chapters/2/)
    extra                      — вся папка non-цифровой главы (game/chapters/extra/)
    0                          — пролог (script-ch0.rpy)
    2_4b                       — часть 4b главы 2 (script-ch2_4b.rpy)
    2_4                        — часть 4 главы 2 (script-ch2_4.rpy)
    2_5*                       — все части с префиксом 5 (script-ch2_5.rpy, script-ch2_5b.rpy, ...)
    script-ch2_5b.rpy          — полное имя файла (ищется по всем папкам game/chapters/)
    script-ch2_5b              — то же без расширения
    sp_l1.rpy / sp_l1          — файл в папке extra
    game/chapters/2/script-ch2_4b.rpy — путь от корня проекта (слеши /)

Правила:
- Число целиком = папка главы; существующая папка по имени = вся папка.
- N_M… = часть главы N: ищется ТОЧНЫЙ файл script-chN_M.rpy (буквенный суффикс
  части указывается явно: 2_5b — это script-ch2_5b.rpy, а не script-ch2_5.rpy).
  Суффикс "*" — префиксное соответствие (все части с данным началом).
- Всё остальное — имя файла: ищется по всем папкам game/chapters/*/*.rpy
  (с расширением или без; допустим также путь от корня проекта).
- Ошибки — ASCII (консоль cp1251): только для печати, в отчётах всё в UTF-8.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


class TargetError(Exception):
    """Ошибка разрешения цели (сообщение — ASCII)."""


@dataclass
class ResolvedTarget:
    """Результат разрешения цели.

    key         — канонический ключ для состояния pipeline и имён отчётов
                  (круглые скобки: НЕ передаётся дочерним скриптам как --chapter,
                  для них передаётся исходный raw — он всегда разрешим повторно).
    label       — отображаемое имя.
    files       — отсортированный список .rpy файлов цели.
    chapter_dir — папка главы, которой принадлежат файлы.
    is_folder   — True, если цель = вся папка главы (важно для предупреждений
                  NO_RPY/NO_DIR в check_renpy_syntax).
    """
    key: str
    label: str
    files: List[Path] = field(default_factory=list)
    chapter_dir: Path = None  # type: ignore[assignment]
    is_folder: bool = False


def _chapter_dirs(chapters_dir: Path) -> List[Path]:
    return sorted(d for d in chapters_dir.iterdir() if d.is_dir())


def _natural_key(name: str):
    """Натуральная сортировка имён: ch1_2 перед ch1_10, ch2_4 перед ch2_4b."""
    return [(1, int(t)) if t.isdigit() else (0, t)
            for t in re.split(r"(\d+)", name)]


def _all_rpy(in_dir: Path) -> List[Path]:
    return sorted(in_dir.glob("*.rpy"), key=lambda p: _natural_key(p.name))


def _parts_list(chapter_dir: Path) -> str:
    """Список файлов главы для сообщения об ошибке (ASCII)."""
    names = [p.name for p in _all_rpy(chapter_dir)]
    if not names:
        return "no files"
    shown = ", ".join(names[:15])
    if len(names) > 15:
        shown += f", ... ({len(names)} total)"
    return shown


def _single_file_target(f: Path) -> ResolvedTarget:
    """Цель из одного файла: key выводится из имени (N_M…), папка — parent.

    Если в папке главы ровно один .rpy (например script-ch0.rpy), цель
    эквивалентна всей главе — key = имя папки, is_folder = True.
    """
    d = f.parent
    base = f.stem
    prefix = f"script-ch{d.name}_"
    if base.startswith(prefix):
        base = base[len(prefix):]
    else:
        prefix2 = "script-"
        base = base[len(prefix2):] if base.startswith(prefix2) else base
    key = f"{d.name}_{base}"
    if len(_all_rpy(d)) == 1:
        key = d.name
        return ResolvedTarget(key=key, label=key, files=[f], chapter_dir=d, is_folder=True)
    return ResolvedTarget(key=key, label=key, files=[f], chapter_dir=d, is_folder=False)


def _folder_target(d: Path) -> ResolvedTarget:
    return ResolvedTarget(
        key=d.name, label=d.name,
        files=_all_rpy(d), chapter_dir=d, is_folder=True,
    )


def _part_target(ch: str, part: str, d: Path) -> ResolvedTarget:
    """Часть главы: точное имя script-ch<ch>_<part>.rpy или префикс со '*'."""
    if not re.fullmatch(r"[A-Za-z0-9*]+", part):
        raise TargetError(
            f"Invalid part spec: '{part}' (use letters/digits, '*' suffix allowed)"
        )
    if part.endswith("*"):
        prefix = part[:-1]
        files = sorted(d.glob(f"script-ch{ch}_{prefix}*.rpy"))
        if not files:
            raise TargetError(
                f"No files matching script-ch{ch}_{prefix}* in chapter {ch} "
                f"(available: {_parts_list(d)})"
            )
        return ResolvedTarget(
            key=f"{ch}_{part}", label=f"{ch}_{part}",
            files=files, chapter_dir=d, is_folder=False,
        )
    f = d / f"script-ch{ch}_{part}.rpy"
    if not f.exists() and ch == "0" and part == "0":
        f = d / "script-ch0.rpy"
    if not f.exists():
        raise TargetError(
            f"Part {ch}_{part} not found in chapter {ch} "
            f"(available: {_parts_list(d)})"
        )
    return ResolvedTarget(
        key=f"{ch}_{part}", label=f"{ch}_{part}",
        files=[f], chapter_dir=d, is_folder=False,
    )


def _path_candidates(raw: str, root: Path) -> List[Path]:
    """Прямые пути от корня проекта (нормализация слешей)."""
    norm = raw.replace("\\", "/")
    while norm.startswith("./"):
        norm = norm[2:]
    cands: List[Path] = []
    if norm.startswith("game/chapters/") or norm.startswith("game/"):
        cands.append(root / norm)
    elif norm.startswith("chapters/"):
        cands.append(root / "game" / norm)
    else:
        cands.append(root / norm)
        cands.append(root / "game" / norm)
    return [c for c in cands if c.is_file()]


def _find_by_name(name: str, chapters_dir: Path) -> List[Path]:
    hits = []
    for d in _chapter_dirs(chapters_dir):
        f = d / name
        if f.is_file():
            hits.append(f)
    return hits


def resolve_target(root: Path, raw: str) -> ResolvedTarget:
    """Разрешить цель в список файлов. При неоднозначности/отсутствии — TargetError."""
    raw = (raw or "").strip().strip('"').strip("'")
    if not raw:
        raise TargetError(
            "Empty target. Use: 2 | 2_4b | script-ch2_5b.rpy | extra | sp_l1"
        )
    chapters_dir = root / "game" / "chapters"
    if not chapters_dir.exists():
        raise TargetError("Folder not found: game/chapters/")

    # 1. Целая глава по номеру (число целиком)
    if re.fullmatch(r"\d+", raw):
        d = chapters_dir / raw
        if not d.is_dir():
            raise TargetError(f"Chapter folder not found: game/chapters/{raw}/")
        return _folder_target(d)

    # 2. Существующая папка по имени (extra и т.п.)
    d = chapters_dir / raw
    if d.is_dir():
        return _folder_target(d)

    # 3. Путь к файлу (содержит слеш или расширение .rpy)
    if "/" in raw or "\\" in raw or raw.lower().endswith(".rpy"):
        hits = _path_candidates(raw, root)
        if len(hits) == 1:
            return _single_file_target(hits[0])
        if len(hits) > 1:
            raise TargetError(f"Ambiguous path {raw}: {hits}")

    # 4. Часть главы N_M… (после пути, чтобы путь не перехватывался)
    m = re.fullmatch(r"(\d+)_(.+)", raw)
    if m:
        ch, part = m.group(1), m.group(2)
        d = chapters_dir / ch
        if not d.is_dir():
            raise TargetError(f"Chapter folder not found: game/chapters/{ch}/")
        return _part_target(ch, part, d)

    # 5. Имя файла (с .rpy или без) — поиск по всем папкам глав
    name = raw if raw.lower().endswith(".rpy") else raw + ".rpy"
    hits = _find_by_name(name, chapters_dir)
    if len(hits) == 1:
        return _single_file_target(hits[0])
    if len(hits) > 1:
        raise TargetError(f"Ambiguous file {name} in game/chapters/: {hits}")

    # Подсказка: перечислить непустые главы с файлами (ASCII)
    hints = []
    for d in _chapter_dirs(chapters_dir):
        files = [p.name for p in _all_rpy(d)]
        if files:
            hints.append(f"{d.name}: {', '.join(files[:6])}")
    hint_str = "; ".join(hints[:12]) or "no .rpy files at all"
    raise TargetError(f"File '{name}' not found in game/chapters/. Existing: {hint_str}")


def main() -> int:
    """CLI-проверка резолвера: python tools/targets.py <target> [target...]."""
    from output_util import ensure_safe_output, safe_print  # noqa: E402
    ensure_safe_output()
    root = Path(__file__).parent.parent
    args = sys.argv[1:] or ["2", "2_4b", "script-ch2_5b.rpy", "extra", "sp_l1"]
    for a in args:
        try:
            t = resolve_target(root, a)
        except TargetError as e:
            safe_print(f"ERROR: {a} -> {e}")
            continue
        files = ", ".join(f.name for f in t.files) or "(no files)"
        safe_print(
            f"{a} -> key={t.key} folder={t.is_folder} "
            f"files[{len(t.files)}]: {files}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())