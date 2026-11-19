#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Find JA `new` strings (and EN old) for a list of English anchor strings."""
import re
from pathlib import Path

root = Path(__file__).parent
targets = [
    "Is that so...? What a shame.",
    "...There's no guarantee the book I want will still be in stock by next time.",
    "That stall over there sells juice, so I'll go grab some.",
    "Even unbaked, it already smells pretty good.",
    "Er, well, it's such nice weather and your throat must be dry, right?",
    "Sure, thanks.",
    "Hey, Siesta. So you're here.",
    "...They'll get pretty heavy, though.",
]

RE_TL = re.compile(r'^\s*(old|new)\s+"(.*)"\s*$')

def collect(tl_dir_name):
    pairs = []
    tl_dir = root / "game" / "tl" / tl_dir_name
    for f in sorted(tl_dir.rglob("*.rpy")):
        if f.name == "common.rpy":
            continue
        pending = None
        for i, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            m = RE_TL.match(line)
            if not m:
                continue
            if m.group(1) == "old":
                pending = (m.group(2), str(f.relative_to(root)), i)
            elif m.group(1) == "new" and pending is not None:
                pairs.append((pending[0], m.group(2), pending[1], pending[2], i))
                pending = None
    return pairs

ja_pairs = collect("japanese")
en_raw = (root / "game" / "chapters" / "2" / "script-ch2_7.rpy").read_text(encoding="utf-8")

for t in targets:
    print("=" * 70)
    print("EN ANCHOR:", t)
    print("  in script-ch2_7.rpy:", t in en_raw)
    hits = [p for p in ja_pairs if p[0] == t]
    if not hits:
        print("  JA tl: (no exact match)")
    for p in hits:
        print(f"  JA [{p[2]}:{p[3]}]: {p[1]}")
