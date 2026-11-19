# -*- coding: utf-8 -*-
"""Independent C-audit extractor for part 2_7. Builds EN->RU and EN->JA maps
from tl/ buckets, and lists the EN dialogue lines of script-ch2_7.rpy in order."""
import re, os, json

ROOT = "/workspace/.tmp/opencode/review-ch2-5"

def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

def parse_pairs(path):
    """Return list of (old, new, lineno) from a translate strings block."""
    txt = read(path)
    lines = txt.splitlines()
    out = []
    cur_old = None
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if s.startswith("old "):
            cur_old = s[4:].strip()
        elif s.startswith("new "):
            newv = s[4:].strip()
            if cur_old is not None:
                out.append((cur_old, newv, i))
                cur_old = None
    return out

def unquote(s):
    # EN strings in rpy are quoted with double quotes; tl old/new likewise.
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        return s[1:-1].replace('\\"', '"')
    return s

# Build maps from all tl files (flat buckets)
def build_map(folder):
    m = {}
    dup = []
    for fn in os.listdir(os.path.join(ROOT, "game/tl", folder)):
        if not fn.endswith(".rpy"):
            continue
        path = os.path.join(ROOT, "game/tl", folder, fn)
        for old, new, ln in parse_pairs(path):
            o = unquote(old)
            n = unquote(new)
            if o in m:
                dup.append((o, fn, ln, m[o][0], m[o][1]))
            m[o] = (n, fn, ln)
    return m, dup

ru_map, ru_dup = build_map("russian")
ja_map, ja_dup = build_map("japanese")

# Extract dialogue lines from script
script = read(os.path.join(ROOT, "game/chapters/2/script-ch2_7.rpy"))
slines = script.splitlines()
records = []
voice_re = re.compile(r'voice\s+"([^"]+)"')
dlg_re = re.compile(r'^\s*(l|s|si|t|th)\s+"(.*)"\s*$')
pending_voice = None
for i, ln in enumerate(slines, 1):
    vm = voice_re.search(ln)
    if vm:
        pending_voice = vm.group(1)
        continue
    dm = dlg_re.match(ln)
    if dm:
        who, raw = dm.group(1), dm.group(2)
        en = raw.replace('\\"', '"')
        records.append({
            "line": i, "who": who, "voice": pending_voice, "en": en,
            "ru": ru_map.get(en), "ja": ja_map.get(en),
        })
        pending_voice = None
        continue
    # menu choices
    cm = re.match(r'^\s*"(.+?)\{.*\}\s*:\s*$', ln)
    if cm:
        en = cm.group(1).replace('\\"', '"')
        records.append({
            "line": i, "who": "menu", "voice": pending_voice, "en": en,
            "ru": ru_map.get(en), "ja": ja_map.get(en),
        })
        pending_voice = None

with open(os.path.join(ROOT, "_c2r7_pairs.json"), "w", encoding="utf-8") as f:
    json.dump({"records": records, "ru_dup": ru_dup, "ja_dup": ja_dup},
              f, ensure_ascii=False, indent=1)

# Human-readable
with open(os.path.join(ROOT, "_c2r7_pairs.txt"), "w", encoding="utf-8") as f:
    for r in records:
        f.write(f"[L{r['line']}] {r['who']} {r['voice']}\n")
        f.write(f"  EN: {r['en']}\n")
        f.write(f"  JA: {r['ja'][0] if r['ja'] else '<<NO JA PAIR>>'}\n")
        f.write(f"  RU: {r['ru'][0] if r['ru'] else '<<NO RU PAIR>>'}\n")
        f.write("\n")

print("records:", len(records))
print("no JA pair:", sum(1 for r in records if not r["ja"]))
print("no RU pair:", sum(1 for r in records if not r["ru"]))
print("ru_dup:", len(ru_dup), "ja_dup:", len(ja_dup))
