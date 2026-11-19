#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract RU old/new pairs whose `old` occurs in script-ch2_7.rpy (scope of part 2_7)."""
import re
from pathlib import Path

root = Path(__file__).parent
en_file = root / "game" / "chapters" / "2" / "script-ch2_7.rpy"

RE_TL = re.compile(r'^\s*(old|new)\s+"(.*)"\s*$')
RE_SPEAKER = re.compile(r'^\s*([A-Za-z_][\w.]*)\s+"(.*)"\s*$')
CODE = {"voice","scene","show","hide","jump","call","with","define","image",
        "transform","play","stop","queue","window","pause","python","return",
        "pass","if","elif","else","while","for","translate","camera","at",
        "using","style","$"}

def extract_texts(path):
    texts = set()
    for line in path.read_text(encoding="utf-8").split("\n"):
        m = RE_TL.match(line)
        if m:
            if m.group(1) is None:
                pass
            if m.group(1) == "new":
                pass
        # speech lines (bare / speaker) with parsed[0] None
        rs = RE_SPEAKER.match(line)
        if rs and rs.group(1) not in CODE:
            texts.add(rs.group(2))
        else:
            rb = re.match(r'^\s*"(.*)"\s*$', line)
            if rb:
                texts.add(rb.group(1))
    return texts

en_texts = extract_texts(en_file)

tl_dir = root / "game" / "tl" / "russian"
out = []
count = 0
for f in sorted(tl_dir.rglob("*.rpy")):
    if f.name == "common.rpy":
        continue
    content = f.read_text(encoding="utf-8")
    lines = content.split("\n")
    pending_old = None
    pending_old_line = None
    for i, line in enumerate(lines, 1):
        m = RE_TL.match(line)
        if not m:
            continue
        kw, body = m.group(1), m.group(2)
        if kw == "old":
            pending_old = body
            pending_old_line = i
            continue
        # kw == new
        if pending_old is not None and pending_old in en_texts:
            count += 1
            rel = str(f.relative_to(root))
            out.append(
                f"### [{count}] {rel}:{pending_old_line} (new@{i})\n"
                f"OLD: {pending_old}\n"
                f"NEW: {body}\n"
            )
        pending_old = None

with open(root / ".tmp_pairs_2_7.txt", "w", encoding="utf-8") as fh:
    fh.write(f"TOTAL_IN_SCOPE: {count}\n\n")
    fh.write("\n".join(out))

print("TOTAL_IN_SCOPE:", count)
