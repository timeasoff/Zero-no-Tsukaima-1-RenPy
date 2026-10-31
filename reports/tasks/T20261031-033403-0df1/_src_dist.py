#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Распределение 【好感度】 по персонажам/значениям в chapter_02 (только в файл)."""
import re
from collections import Counter

SRC = "/workspace/ps2_source/chapters/chapter_02_ゼロのルイズ.txt"
OUT = "/workspace/reports/tasks/T20261031-033403-0df1/_src_like_dist.txt"

lines = open(SRC, encoding="utf-8").read().splitlines()
events = []
for i, line in enumerate(lines, 1):
    if "\u3010\u597d\u611f\u5ea6\u3011" in line:
        seg = line.split("\u3010\u597d\u611f\u5ea6\u3011")[1].strip()
        events.append((i, seg))

by_char = Counter()
by_val = Counter()
for _, seg in events:
    m = re.match(r"([^\s\d+\-]+)?\s*([+\-]\d+)?", seg)
    name = (m.group(1) or "?")
    val = (m.group(2) or "?")
    by_char[name] += 1
    by_val[(name, val)] += 1

out = []
out.append("TOTAL %d" % len(events))
out.append("-- by char --")
for k, v in by_char.most_common():
    out.append("%s\t%d" % (k, v))
out.append("-- by char+value --")
for (k, val), v in sorted(by_val.items()):
    out.append("%s %s\tx%d" % (k, val, v))
out.append("-- all events (line: seg) --")
for i, seg in events:
    out.append("%d\t%s" % (i, seg))

open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("events=%d chars=%d -> %s" % (len(events), len(by_char), OUT))
