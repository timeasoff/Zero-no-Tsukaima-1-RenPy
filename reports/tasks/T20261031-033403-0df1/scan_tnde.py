#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Поиск tnEventId / dlEventId / getTunDeleScene / date() в ps2_source/scripts (CP932).

Только чтение. Вывод — UTF-8 файл рядом со скриптом, японский в консоль не печатается.
"""
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
SCRIPTS = os.path.join(ROOT, "ps2_source", "scripts")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tnde_scan_out.txt")

TOKENS = [b"tnEventId", b"dlEventId", b"getTunDeleScene", b"TunDele", b"date("]

hits = []
for name in sorted(os.listdir(SCRIPTS)):
    if not name.endswith(".txt"):
        continue
    path = os.path.join(SCRIPTS, name)
    with open(path, "rb") as f:
        data = f.read()
    for tok in TOKENS:
        for m in re.finditer(re.escape(tok), data):
            s = max(0, m.start() - 300)
            e = min(len(data), m.end() + 300)
            chunk = data[s:e]
            try:
                text = chunk.decode("cp932", errors="replace")
            except Exception:
                text = repr(chunk)
            hits.append((name, m.start(), tok.decode(), text.replace("\r\n", "\n")))

with open(OUT, "w", encoding="utf-8") as f:
    f.write("hits: %d\n" % len(hits))
    for name, off, tok, text in hits:
        f.write("\n===== %s offset=%d token=%s\n" % (name, off, tok))
        f.write(text)
        f.write("\n")

sys.stdout.write("hits=%d -> %s\n" % (len(hits), OUT))
