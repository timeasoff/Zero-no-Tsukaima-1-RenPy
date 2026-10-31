#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сэмпл сцен-веток/финалов 90/91: первые 5 реплик + EVENT_CG/BGM сцены."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RAW = os.path.join(HERE, "raw_branches.json")
OUT = os.path.join(HERE, "route_samples.md")

RE_SCENE = re.compile(r"^---- SCENE (\d+) ----")


def sample(path, scenes):
    res = {}
    cur = None
    n = 0
    meta = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            m = RE_SCENE.match(line)
            if m:
                cur = int(m.group(1))
                n = 0
                if cur in scenes:
                    res.setdefault(cur, [])
                    meta.setdefault(cur, [])
                continue
            if cur in scenes:
                if n < 5 and not line.startswith("  ["):
                    txt = re.sub(r"\s*\[voice \d+\]$", "", line)
                    if txt.strip():
                        res[cur].append(txt.replace("\n", " / "))
                        n += 1
                if "[EVENT_CG" in line or "[BGM" in line:
                    meta[cur].append(line.strip())
    return res, meta


def main():
    raw = json.load(open(RAW, encoding="utf-8"))
    plan = {"90": [1553, 1557, 1560, 1561, 1569, 1585, 1625, 1692],
            "91": [1717, 1721, 1724, 1725, 1733, 1765, 1800, 1856]}
    with open(OUT, "w", encoding="utf-8") as f:
        for ch in ("90", "91"):
            d = raw[ch]
            path = os.path.join(ROOT, "ps2_source", "chapters", d["file"])
            r, meta = sample(path, set(plan[ch]))
            f.write("\n## Chapter %s\n" % ch)
            for s in plan[ch]:
                f.write("\n### SCENE %d\n" % s)
                for t in r.get(s, []):
                    f.write("- %s\n" % t[:150])
                for mm in meta.get(s, [])[:4]:
                    f.write("  * %s\n" % mm)
    print("-> %s" % OUT)


if __name__ == "__main__":
    main()
