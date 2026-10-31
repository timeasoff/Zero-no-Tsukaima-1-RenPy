#!/usr/bin/env python3
"""Сборка references/routes.md: шапка (§0-§4, §5-шапка, §6/§7-заголовки, §8)
+ содержимое evidence-файлов трёх подзадач.

Запуск из корня проекта:
    python3 reports/tasks/T20261031-033403-0df1/assemble_routes.py

Токены-заглушки в references/routes.md заменяются на тело секций:
    PLACEHOLDER-S5 -> s2_ported_branches.md   (инвентарь порта, гл.0-6 + extra)
    PLACEHOLDER-S6 -> s3_source_branches.md   (источник, гл.07-17)
    PLACEHOLDER-S7 -> s5_source_branches.md   (источник, гл.18-29, 90/91)

Первая строка H1 каждого evidence-файла отбрасывается (заголовок уже есть в §N).
Идемпотентно: повторный прогон идентичен (токены исчезают -> повтор ничего не меняет,
кроме контрольного сообщения). Секции §8 собираются вручную ведущим агентом.
"""
import sys
from pathlib import Path

BASE = Path("reports/tasks/T20261031-033403-0df1")
OUT = Path("references/routes.md")

SECTIONS = [
    ("PLACEHOLDER-S5", BASE / "s2_ported_branches.md"),
    ("PLACEHOLDER-S6", BASE / "s3_source_branches.md"),
    ("PLACEHOLDER-S7", BASE / "s5_source_branches.md"),
]


def strip_h1(text: str) -> str:
    lines = text.splitlines(keepends=True)
    i = 0
    if lines and lines[0].startswith("# "):
        i = 1
        while i < len(lines) and lines[i].strip() == "":
            i += 1
    return "".join(lines[i:]).rstrip("\n") + "\n"


def main() -> int:
    text = OUT.read_text(encoding="utf-8")
    missing = []
    for token, path in SECTIONS:
        if token not in text:
            missing.append(token)
            continue
        body = strip_h1(path.read_text(encoding="utf-8"))
        text = text.replace(token, body, 1)
    if missing:
        print("SKIP (нет токена, возможно уже собрано): " + ", ".join(missing))
    OUT.write_text(text, encoding="utf-8")
    print(f"OK: {OUT} — {len(text.splitlines())} строк, {len(text)} байт")
    return 0


if __name__ == "__main__":
    sys.exit(main())
