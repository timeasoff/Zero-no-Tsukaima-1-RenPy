#!/usr/bin/env python3
"""Apply confirmed literary-review fixes (prompt 10). Local, minimal edits."""
from pathlib import Path

ROOT = Path(__file__).parent.parent

EDITS = {
 'game/tl/russian/ch23_3_dialogs.rpy': [
   ('Коек-как', 'Кое-как'),
   ('Остальном подумаем', 'Об остальном подумаем'),
 ],
 'game/tl/russian/ch26_2_dialogs.rpy': [
   ('предположительно,деяния', 'предположительно, деяния'),
   ('Принцессе!?', 'Её Величеству!?'),
   ('Кирке', 'Кирхе'),
 ],
 'game/tl/russian/ch26_2_choises.rpy': [
   ('Кирке', 'Кирхе'),
 ],
 'game/tl/russian/ch27_2_dialogs.rpy': [
   ('Нeeeт', 'Нееет'),
 ],
}

for rel, reps in EDITS.items():
    p = ROOT / rel
    if not p.exists():
        print('MISSING', rel)
        continue
    s = p.read_text(encoding='utf-8')
    n = 0
    for a, b in reps:
        c = s.count(a)
        if c:
            s = s.replace(a, b)
            n += c
            print(rel.split('/')[-1], repr(a), '->', repr(b), 'x', c)
    p.write_text(s, encoding='utf-8')
    print(' total', n)
