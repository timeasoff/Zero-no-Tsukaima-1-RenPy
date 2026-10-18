# -*- coding: utf-8 -*-
"""List ch4.5 EN dialogues that need {#ch4.5_*} tags:
- already present as `old` in tl files, or
- duplicated inside ch4_5 itself.
"""
import io
import re
import sys
import collections

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SL = open('game/chapters/4/script-ch4_5.rpy', encoding='utf-8').read()
lines = SL.splitlines()

entries = []  # (line_no, speaker, text)
for i, ln in enumerate(lines, 1):
    m = re.match(r'^    (s|l|h|ha|si|d) "(.*)"$', ln)
    if m:
        entries.append((i, m.group(1), m.group(2)))

own = collections.Counter(t for _, _, t in entries)

ru = open('game/tl/russian/dialogs.rpy', encoding='utf-8').read()
ja = open('game/tl/japanese/dialogs.rpy', encoding='utf-8').read()

need = []
for n, (i, spk, t) in enumerate(entries, 1):
    reasons = []
    if own[t] > 1:
        reasons.append('own_x%d' % own[t])
    if t in ru or t in ja:
        reasons.append('in_tl')
    if reasons:
        need.append((n, i, spk, t, ','.join(reasons)))

print('need tag: %d' % len(need))
for n, i, spk, t, r in need:
    print('  D%03d line=%d [%s] %s  (%s)' % (n, i, spk, t[:80], r))

# thoughts / choices too
th = [m.group(1) for m in re.finditer(r'^    th "(.*)"$', SL, re.M)]
ru_t = open('game/tl/russian/thoughs.rpy', encoding='utf-8').read()
ja_t = open('game/tl/japanese/thoughs.rpy', encoding='utf-8').read()
print('thoughts colliding: %d' % sum(1 for t in th if t in ru_t or t in ja_t))
