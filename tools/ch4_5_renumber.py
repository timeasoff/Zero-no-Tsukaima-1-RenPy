# -*- coding: utf-8 -*-
"""Renumber ch4.5 voice names sequentially per speaker in script-ch4_5.rpy.

Idempotent: numbering is derived purely from order of appearance, so re-running
changes nothing. Prints an ASCII report (old -> new) to stdout.
"""
import re, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

PATH = 'game/chapters/4/script-ch4_5.rpy'
text = open(PATH, encoding='utf-8').read()
lines = text.splitlines(keepends=True)

counters = {}
changes = []
out = []
pat = re.compile(r'(voice "ch4\.5_)([a-z]+)_\d+"')
for ln in lines:
    def repl(m):
        spk = m.group(2)
        counters[spk] = counters.get(spk, 0) + 1
        new = '%s%s_%03d"' % (m.group(1), spk, counters[spk])
        old = m.group(0)
        if old != new:
            changes.append((old.strip(), new.strip()))
        return new
    out.append(pat.sub(repl, ln))

open(PATH, 'w', encoding='utf-8', newline='').write(''.join(out))

total = sum(counters.values())
print('total voices: %d' % total)
for k in sorted(counters):
    print('  %-3s %d' % (k, counters[k]))
print('renumbered: %d' % len(changes))
for o, n in changes[:60]:
    print('  %s -> %s' % (o, n))
