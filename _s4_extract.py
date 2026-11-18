# -*- coding: utf-8 -*-
import re, os, glob, json

ROOT = "/workspace/.tmp/opencode/review-ch2-5"
EN = os.path.join(ROOT, "game/chapters/2/script-ch2_4.rpy")

def strip_tag(s):
    # remove Ren'Py translator comments {#...}
    return re.sub(r"\{#[^}]*\}", "", s)

# 1) collect EN strings from part 2_4 (dialogue + th + menu choices)
en_strings = []
en_order = []
with open(EN, encoding="utf-8") as f:
    for ln, line in enumerate(f, 1):
        # dialogue lines:  s "..."  / th "..." / d "..." etc
        m = re.match(r'^\s+[a-z]{1,3}\s+"(.*)"\s*$', line)
        if m:
            en_strings.append(m.group(1))
            en_order.append((ln, "dlg", m.group(1)))
            continue
        # menu choices:  "text...":  (inside menu:)
        m = re.match(r'^\s+"(.*)":\s*$', line)
        if m:
            en_strings.append(m.group(1))
            en_order.append((ln, "menu", m.group(1)))

en_keys = {}
for s in en_strings:
    en_keys[strip_tag(s)] = True

# 2) parse all RU tl files (exclude common.rpy read-only)
files = sorted(glob.glob(os.path.join(ROOT, "game/tl/russian/*.rpy")))
results = []
matched_keys = {}
for fp in files:
    if fp.endswith("common.rpy"):
        continue
    cur_old = None
    cur_old_line = None
    with open(fp, encoding="utf-8") as f:
        lines = f.readlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        mo = re.match(r'^\s*old\s+"(.*)"\s*$', line.rstrip("\n"))
        if mo:
            # look ahead for new
            new = None
            new_line = None
            j = i + 1
            while j < len(lines) and j <= i + 4:
                mn = re.match(r'^\s*new\s+"(.*)"\s*$', lines[j].rstrip("\n"))
                if mn:
                    new = mn.group(1)
                    new_line = j + 1
                    break
                j += 1
            key = strip_tag(mo.group(1))
            if key in en_keys:
                results.append({
                    "file": os.path.basename(fp),
                    "old_line": i + 1,
                    "new_line": new_line,
                    "old": mo.group(1),
                    "new": new,
                })
                matched_keys[key] = True
            i = j + 1 if new is not None else i + 1
            continue
        i += 1

# unmatched EN strings
unmatched = [ (ln,kind,s) for (ln,kind,s) in en_order if strip_tag(s) not in matched_keys ]

out = []
out.append("=== MATCHED %d ===" % len(results))
for r in results:
    out.append("FILE %s  old_line=%s new_line=%s" % (r["file"], r["old_line"], r["new_line"]))
    out.append("  OLD: %s" % r["old"])
    out.append("  NEW: %s" % r["new"])
    out.append("")
out.append("=== UNMATCHED %d ===" % len(unmatched))
for (ln,kind,s) in unmatched:
    out.append("EN line %d [%s]: %s" % (ln, kind, s))

with open(os.path.join(ROOT, "_s4_out.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))

print("matched", len(results), "unmatched", len(unmatched))
