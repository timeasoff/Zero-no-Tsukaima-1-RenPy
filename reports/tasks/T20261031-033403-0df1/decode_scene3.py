#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Полная расшифровка SCENE_0003.txt (CP932) в UTF-8 файл для чтения."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
src = os.path.join(ROOT, "ps2_source", "scripts", "SCENE_0003.txt")
dst = os.path.join(HERE, "SCENE_0003_decoded.txt")

with open(src, "rb") as f:
    data = f.read()
text = data.decode("cp932", errors="replace")
with open(dst, "w", encoding="utf-8") as f:
    f.write(text)
print("lines=%d -> %s" % (text.count("\n") + 1, dst))
