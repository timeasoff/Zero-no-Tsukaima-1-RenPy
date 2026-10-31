#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Состав говорящих во ВСЕЙ сцене (не только начало) для входных сцен 90/91."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RAW = os.path.join(HERE, "raw_branches.json")
OUT = os.path.join(HERE, "entry_speakers.md")

RE_SCENE = re.compile(r"^---- SCENE (\d+) ----")


def census(path, owners):
    res = {}
    cur = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            m = RE_SCENE.match(line)
            if m:
                cur = int(m.group(1))
                if cur in owners:
                    res.setdefault(cur, {})
                continue
            if cur in res:
                m2 = re.match(r"^([^  \[（【].*?)：", line)
                if m2:
                    spk = m2.group(1)
                    res[cur][spk] = res[cur].get(spk, 0) + 1
    return res


def main():
    raw = json.load(open(RAW, encoding="utf-8"))
    with open(OUT, "w", encoding="utf-8") as f:
        for ch, lo, hi in (("90", 1535, 1552), ("91", 1699, 1716)):
            d = raw[ch]
            path = os.path.join(ROOT, "ps2_source", "chapters", d["file"])
            owners = {i for i in range(lo, hi + 1)}
            c = census(path, owners)
            f.write("\n## Chapter %s entry scenes — speakers\n" % ch)
            for o in sorted(c):
                items = sorted(c[o].items(), key=lambda kv: -kv[1])
                f.write("- %d: %s\n" % (o, ", ".join("%s(%d)" % kv for kv in items)))
    print("-> %s" % OUT)


if __name__ == "__main__":
    main()
