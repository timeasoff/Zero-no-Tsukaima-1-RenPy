#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Декодирует несколько SCENE_*.txt (CP932) и печатает хвост/шапку в UTF-8 файл."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SC = os.path.join(ROOT, "ps2_source", "scripts")
OUT = os.path.join(HERE, "scene_tails.md")

ids = [428, 429, 430, 768, 769, 770, 771]
with open(OUT, "w", encoding="utf-8") as f:
    for i in ids:
        p = os.path.join(SC, "SCENE_%04d.txt" % i)
        if not os.path.exists(p):
            f.write("\n## SCENE_%04d: MISSING\n" % i)
            continue
        data = open(p, "rb").read()
        text = data.decode("cp932", errors="replace")
        lines = [l for l in text.replace("\r\n", "\n").split("\n")]
        f.write("\n## SCENE_%04d  bytes=%d lines=%d\n" % (i, len(data), len(lines)))
        f.write("HEAD:\n")
        for l in lines[:6]:
            f.write("  | %s\n" % l[:160])
        f.write("TAIL:\n")
        for l in lines[-8:]:
            f.write("  | %s\n" % l[:160])
        f.write("next()/goto refs: %s\n" %
                [l.strip()[:120] for l in lines if "next(" in l][:6])
print("-> " + OUT)
