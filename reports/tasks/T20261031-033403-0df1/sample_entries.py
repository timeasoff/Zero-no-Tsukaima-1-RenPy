#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сэмпл входных сцен глав 90/91: говорящие + первые 3 реплики (в UTF-8 файл)."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RAW = os.path.join(HERE, "raw_branches.json")
OUT = os.path.join(HERE, "entry_samples.md")

RE_SCENE = re.compile(r"^---- SCENE (\d+) ----")
RE_TALK = re.compile(r"^([^  \[（].*?)：(.*)$")


def sample(path, owners, maxlines=4):
    res = {}
    cur = None
    buf = []
    count = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            m = RE_SCENE.match(line)
            if m:
                if cur is not None:
                    res[cur] = buf
                cur = int(m.group(1))
                buf = []
                count = 0
                continue
            if cur in owners and count < maxlines:
                m2 = RE_TALK.match(line)
                if m2 and not line.startswith("  ["):
                    spk = m2.group(1)
                    txt = m2.group(2).strip()
                    txt = re.sub(r"\s*\[voice \d+\]$", "", txt)
                    txt = txt.replace("\n", " / ")
                    buf.append((spk, txt))
                    count += 1
    if cur is not None:
        res[cur] = buf
    return res


def main():
    raw = json.load(open(RAW, encoding="utf-8"))
    with open(OUT, "w", encoding="utf-8") as f:
        for ch in ("90", "91"):
            d = raw[ch]
            owners = sorted({o for o, _, _ in d["choices"] if o < (1535 if ch == "90" else 1699) + 18})
            path = os.path.join(ROOT, "ps2_source", "chapters", d["file"])
            s = sample(path, set(owners))
            f.write("\n## Chapter %s — entry scenes (%d)\n" % (ch, len(owners)))
            for o in owners:
                f.write("\n### SCENE %d\n" % o)
                for spk, txt in s.get(o, []):
                    f.write("- %s: %s\n" % (spk, txt[:120]))
    print("-> %s" % OUT)


if __name__ == "__main__":
    main()
