#!/usr/bin/env python3
"""Update EN dialogue text in sp90.rpy by translation tag (prompt 09 fixes)."""
import re
from pathlib import Path

from fix_semantic_findings import SP90

p = Path(__file__).parent.parent / 'game/chapters/extra/sp90.rpy'
lines = p.read_text(encoding='utf-8').split('\n')
out, changed = [], []
for line in lines:
    m = re.search(r'\{#([^}]+)\}', line)
    tag = m.group(1) if m else None
    if tag and tag in SP90 and re.match(r'^\s*[A-Za-z_]\w*\s+"', line):
        new_en = SP90[tag][0].split('{#')[0]
        head, sep, tail = line.partition('{#')
        q = head.find('"')
        if q >= 0:
            line = head[:q + 1] + new_en + sep + tail
            changed.append(tag)
    out.append(line)
p.write_text('\n'.join(out), encoding='utf-8')
print('changed', len(changed), changed)
