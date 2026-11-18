#!/usr/bin/env python3
"""Second round of confirmed literary fixes (prompt 10)."""
from pathlib import Path

ROOT = Path(__file__).parent.parent
EDITS = {
 'game/tl/russian/ch25_2_dialogs.rpy': [
   ('Л-Луиза? Откуда ты здесь?', 'Л-Луиза? Почему ты здесь?'),
 ],
 'game/tl/russian/ch25_4_dialogs.rpy': [
   ('Это и есть настоящий культурный обмен.', 'Это и есть настоящий опыт другой культуры.'),
   ('А, правда? Такая милая, а её едят…', 'А, правда? Такая милая…'),
 ],
 'game/tl/russian/ch25_1_dialogs.rpy': [
   ('не могу добиться никаких существенных данных', 'не могу получить никаких существенных сведений'),
 ],
 'game/tl/russian/sp91_dialogs.rpy': [
   ('дыхание Луиз прямо рядом', 'дыхание Луизы прямо рядом'),
   ('Тепло и вес Луиз у меня на спине', 'Тепло и вес Луизы у меня на спине'),
   ('Мыться вместе с Луиз…', 'Мыться вместе с Луизой…'),
 ],
}
for rel, reps in EDITS.items():
    p = ROOT / rel
    if not p.exists():
        print('MISSING', rel)
        continue
    s = p.read_text(encoding='utf-8')
    for a, b in reps:
        c = s.count(a)
        if c:
            s = s.replace(a, b)
            print(rel.split('/')[-1], repr(a[:40]), '->', repr(b[:40]), 'x', c)
        else:
            print('NOT FOUND', rel, repr(a[:40]))
    p.write_text(s, encoding='utf-8')
