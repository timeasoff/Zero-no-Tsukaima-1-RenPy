# -*- coding: utf-8 -*-
"""List every source talk line in scenes 256-260 WITHOUT a [voice N] marker
(i.e. silent/null narration lines) — must all be represented in the script."""
import re, glob, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

f = glob.glob('ps2_source/chapters/chapter_05_*.txt')[0]
L = open(f, encoding='utf-8', errors='replace').read().splitlines()

scene_re = re.compile(r'^-+\s*SCENE\s*(\d+)\s*-+$')
talk_re = re.compile(r'^([^\s：:（【\[]+)：(.*)$')

cur = None
start = {}
for i, ln in enumerate(L):
    m = scene_re.match(ln.strip())
    if m:
        cur = int(m.group(1))

# range: scene 256 header .. scene 261 header
s256 = next(i for i, l in enumerate(L) if re.match(r'^-+\s*SCENE\s*0256', l.strip()))
s261 = next(i for i, l in enumerate(L) if re.match(r'^-+\s*SCENE\s*0261', l.strip()))

silent = []
for i in range(s256, s261):
    ln = L[i]
    m = talk_re.match(ln)
    if m and not ln.strip().startswith('['):
        # gather continuation lines until next talk/event line
        j = i + 1
        cont = []
        while j < s261:
            nxt = L[j]
            if talk_re.match(nxt) or nxt.strip().startswith('['):
                break
            if nxt.strip():
                cont.append(nxt)
            j += 1
        block = [ln] + cont
        if any('[voice' in b for b in block):
            continue  # voiced dialog: marker sits on a later physical line
        silent.append((i + 1, m.group(1), m.group(2), cont))

print('scene range lines %d..%d' % (s256 + 1, s261))
print('silent talk blocks: %d' % len(silent))
for line_no, spk, first, cont in silent:
    print('  %d %s：%s' % (line_no, spk, first))
    for c in cont:
        print('        + %s' % c)
