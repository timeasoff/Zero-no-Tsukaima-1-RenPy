#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ищет числовые таблицы (главы/сцены) в движковых сценах 0,1,2 (CP932 → UTF-8)."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SC = os.path.join(ROOT, "ps2_source", "scripts")
OUT = os.path.join(HERE, "engine_tables.md")

pat = re.compile(r"\b(429|430|769|770|670|771|431)\b")
with open(OUT, "w", encoding="utf-8") as f:
    for i in (0, 1, 2, 3):
        p = os.path.join(SC, "SCENE_%04d.txt" % i)
        if not os.path.exists(p):
            continue
        text = open(p, "rb").read().decode("cp932", errors="replace")
        lines = text.replace("\r\n", "\n").split("\n")
        f.write("\n## SCENE_%04d lines=%d\n" % (i, len(lines)))
        for n, l in enumerate(lines, 1):
            if pat.search(l) or "syssave" in l or "chapter" in l.lower() \
                    or "sceneMain" in l or "zero_route" in l:
                f.write("  %d| %s\n" % (n, l.strip()[:200]))
print("-> " + OUT)
