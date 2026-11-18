#!/usr/bin/env python3
"""Bring RU names in scope in line with dictionary.md canon.

Кирке -> Кирхе (indeclinable); Табас* -> Табит* with declension preserved.
Only game/tl/russian files of the target scope; JA and EN untouched.
"""
import glob
from pathlib import Path

ROOT = Path(__file__).parent.parent
REPS = [
 ('Табасой', 'Табитой'), ('Табасы', 'Табиты'), ('Табасе', 'Табите'),
 ('Табасу', 'Табиту'), ('Табаса', 'Табита'), ('Кирке', 'Кирхе'),
]

files = []
for c in range(22, 29):
    files += glob.glob(str(ROOT / 'game/tl/russian' / ('ch%d_*' % c)))
files += glob.glob(str(ROOT / 'game/tl/russian/sp9*'))

total = 0
for p in sorted(set(files)):
    s = Path(p).read_text(encoding='utf-8')
    n = 0
    for a, b in REPS:
        c = s.count(a)
        if c:
            s = s.replace(a, b)
            n += c
    if n:
        Path(p).write_text(s, encoding='utf-8')
        total += n
        print(Path(p).name, n)
print('total replacements', total)
