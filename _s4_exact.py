# -*- coding: utf-8 -*-
import re, os, glob

ROOT = "/workspace/.tmp/opencode/review-ch2-5"
EN = os.path.join(ROOT, "game/chapters/2/script-ch2_4.rpy")

with open(EN, encoding="utf-8") as f:
    lines = f.readlines()

en_order = []
for ln, line in enumerate(lines, 1):
    m = re.match(r'^\s+[a-z]{1,3}\s+"(.*)"\s*$', line)
    if m:
        en_order.append((ln, "dlg", m.group(1)))
        continue
    m = re.match(r'^\s+"(.*)":\s*$', line)
    if m:
        en_order.append((ln, "menu", m.group(1)))

# index all tl entries by exact old
files = sorted(glob.glob(os.path.join(ROOT, "game/tl/russian/*.rpy")))
index = {}
for fp in files:
    if fp.endswith("common.rpy"):
        continue
    with open(fp, encoding="utf-8") as f:
        tl = f.readlines()
    i = 0
    while i < len(tl):
        mo = re.match(r'^\s*old\s+"(.*)"\s*$', tl[i].rstrip("\n"))
        if mo:
            new = None; new_line = None
            j = i + 1
            while j < len(tl) and j <= i + 4:
                mn = re.match(r'^\s*new\s+"(.*)"\s*$', tl[j].rstrip("\n"))
                if mn:
                    new = mn.group(1); new_line = j + 1; break
                j += 1
            index.setdefault(mo.group(1), []).append((os.path.basename(fp), i+1, new_line, new))
            i = j+1 if new is not None else i+1
            continue
        i += 1

out = []
out.append("=== EXACT MATCH REPORT (part 2_4) ===")
seen = {}
for (ln, kind, s) in en_order:
    hits = index.get(s, [])
    seen[s] = True
    out.append("EN L%d [%s]: %s" % (ln, kind, s))
    if not hits:
        out.append("   *** NO EXACT MATCH ***")
    for (f, ol, nl, new) in hits:
        out.append("   -> %s old@%d new@%d NEW: %s" % (f, ol, nl, new))
    out.append("")
with open(os.path.join(ROOT, "_s4_exact_out.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("total EN strings:", len(en_order), "exact-matched:", sum(1 for (ln,k,s) in en_order if s in index))
