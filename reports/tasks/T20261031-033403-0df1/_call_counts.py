#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Счётчики вызовов like()/tndl()/date()/checkRoute()/checkKiss() по events_full.

Только в файл-отчёт (ASCII-сводка в консоль), японский в консоль не печатается.
"""
import glob
import os
import re
from collections import Counter

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_call_counts.txt")

pats = {
    "like": re.compile(r"\blike\("),
    "tndl": re.compile(r"\btndl\("),
    "date": re.compile(r"\bdate\("),
    "checkRoute": re.compile(r"\bcheckRoute\("),
    "checkKiss": re.compile(r"\bcheckKiss\("),
}

rows = []
totals = Counter()
for f in sorted(glob.glob("/workspace/ps2_source/events_full/*.txt")):
    name = os.path.basename(f)
    counts = Counter()
    for line in open(f, encoding="utf-8"):
        for key, p in pats.items():
            if p.search(line):
                counts[key] += 1
    if any(counts.values()):
        rows.append((name, dict(counts)))
        for k, v in counts.items():
            totals[k] += v

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("CALL COUNTS in ps2_source/events_full/*.txt\n")
    fh.write("TOTALS: %s\n\n" % dict(totals))
    for name, counts in rows:
        fh.write("%s\t%s\n" % (name, counts))

print("totals: %s" % dict(totals))
print("files with hits: %d -> %s" % (len(rows), OUT))
