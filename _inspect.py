#!/usr/bin/env python3
import re, unicodedata
from pathlib import Path
root = Path(__file__).parent
d = root / "game/tl/russian"

def codepoints(s):
    # only show quote-like chars
    out=[]
    for ch in s:
        if ch in '«»„“”"\'':
            out.append(f"U+{ord(ch):04X}({unicodedata.name(ch,'?')})")
    return out

# Check the actual quote chars in the in-scope new strings for quotes
targets = [9, 59, 74, 104, 106, 110, 113]
for i, idx in enumerate(targets):
    pass

# Print codepoints for every RU new in scope that contains any quote char
import json
res = json.loads((root / "_scope_result.json").read_text(encoding="utf-8"))
for r in res["ru"]:
    q = codepoints(r["new"])
    if q:
        print(f"[line {r['new_line']}] {r['file']}: {q}")
        print("   ", r["new"])
print("="*50)
# Count usage of „ in all ru tl
cnt=0
files=[]
for f in sorted(d.rglob("*.rpy")):
    if f.name=="common.rpy": continue
    t=f.read_text(encoding="utf-8")
    n=t.count("„")
    if n:
        cnt+=n
        files.append((f.name,n))
print("Total '„' in ru tl:", cnt)
print("Files with '„':", files[:30], "... total", len(files))
# Харуна occurrences and following char
print("="*50)
haru=[]
for f in sorted(d.rglob("*.rpy")):
    t=f.read_text(encoding="utf-8")
    for m in re.finditer(r"Харун[а-яё]*", t):
        haru.append((f.name, m.group(0)))
from collections import Counter
print("Харун* forms:", Counter(x[1] for x in haru))
