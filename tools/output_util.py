#!/usr/bin/env python3
"""Безопасный вывод в консоль для инструментов проверки ZnT1.

Консоль PowerShell здесь cp1251: японский/символы вне cp1251 не должны ронять
проверку. Ошибки кодировки заменяются на '?', кириллица cp1251 выводится как есть.

Полные результаты всегда пишутся в отчёты UTF-8 (reports/*.md), консоль — только
сводка.
"""
from __future__ import annotations

import sys


def ensure_safe_output() -> None:
    """Разрешить заменяющий режим для stdout/stderr (не ронять печать на cp1251)."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        try:
            reconfigure(errors="replace")
        except (ValueError, OSError, AttributeError):
            pass


def safe_print(text: str = "") -> None:
    """Печать без UnicodeEncodeError."""
    try:
        print(text)
    except UnicodeEncodeError:
        enc = getattr(sys.stdout, "encoding", None) or "ascii"
        print(text.encode(enc, errors="replace").decode(enc, errors="replace"))


def print_items(items, limit: int = 20, header: str = "") -> None:
    """Печать списка находок с ограничением длины (полный список — в отчёте)."""
    if header:
        safe_print(header)
    for item in items[:limit]:
        safe_print(f"  {item}")
    if len(items) > limit:
        safe_print(f"  ... и ещё {len(items) - limit} — см. отчёт")


def normalize_severity(result) -> None:
    """Согласовать severity с коллекцией: errors → ERROR, warnings → WARNING."""
    for item in getattr(result, "errors", []):
        item.severity = "ERROR"
    for item in getattr(result, "warnings", []):
        item.severity = "WARNING"
