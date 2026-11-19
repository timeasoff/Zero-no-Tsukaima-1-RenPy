# -*- coding: utf-8 -*-
import os, re, glob

ROOT = "/workspace/.tmp/opencode/review-ch2-5"
SCRIPT = os.path.join(ROOT, "game/chapters/2/script-ch2_4c.rpy")

def unescape(s):
    # Ren'Py string: \" -> ", \\ -> \
    return s.replace('\\"', '"').replace('\\\\', '\\')

def parse_tl(folder):
    pairs = {}  # old -> (new, filepath, lineno)
    for path in sorted(glob.glob(os.path.join(ROOT, folder, "*.rpy"))):
        base = os.path.basename(path)
        if base in ("common.rpy",):
            continue
        try:
            lines = open(path, encoding="utf-8").read().split("\n")
        except Exception:
            continue
        cur_old = None
        cur_line = 0
        for i, ln in enumerate(lines, 1):
            m = re.match(r'^\s*old\s+"(.*)"\s*$', ln)
            if m:
                cur_old = unescape(m.group(1))
                cur_line = i
                continue
            m = re.match(r'^\s*new\s+"(.*)"\s*$', ln)
            if m and cur_old is not None:
                new = unescape(m.group(1))
                if cur_old not in pairs:
                    pairs[cur_old] = (new, base, cur_line)
                cur_old = None
    return pairs

ja = parse_tl("game/tl/japanese")
ru = parse_tl("game/tl/russian")

def strip_anchor(s):
    return re.sub(r'\{#[^}]*\}', '', s).strip()

script_lines = open(SCRIPT, encoding="utf-8").read().split("\n")
out = []
for i, ln in enumerate(script_lines, 1):
    m = re.match(r'^\s*(s|d|k|t|ha|th)\s+"(.*)"\s*$', ln)
    speaker = None
    en = None
    if m:
        speaker, en = m.group(1), m.group(2)
    else:
        m2 = re.match(r'^\s*"(.*)"\s*:\s*$', ln)
        if m2:
            speaker = "MENU"
            en = m2.group(1)
    if en is None:
        continue
    variants = [en, strip_anchor(en)]
    ja_hit = None
    ru_hit = None
    for v in variants:
        if v in ja:
            ja_hit = ja[v]
            break
    for v in variants:
        if v in ru:
            ru_hit = ru[v]
            break
    out.append((i, speaker, en, ja_hit, ru_hit))

with open(os.path.join(ROOT, "_audit_aligned.txt"), "w", encoding="utf-8") as f:
    f.write("LINES=%d\n" % len(out))
    for (i, spk, en, ja_hit, ru_hit) in out:
        f.write("=" * 70 + "\n")
        f.write("L%d [%s] EN: %s\n" % (i, spk, en))
        f.write("  JA: %s\n" % (ja_hit[0] if ja_hit else "<<NO JA PAIR>>"))
        f.write("  RU: %s\n" % (ru_hit[0] if ru_hit else "<<NO RU PAIR>>"))
print("done", len(out))
