#!/usr/bin/env python3
"""Confirmed literary fixes for sp90 (prompt 10)."""
from pathlib import Path

ROOT = Path(__file__).parent.parent
RU = ROOT / 'game/tl/russian/sp90_dialogs.rpy'
EN = ROOT / 'game/chapters/extra/sp90.rpy'
JA = ROOT / 'game/tl/japanese/sp90_dialogs.rpy'

s = RU.read_text(encoding='utf-8')
reps = [
 ('Я сбиву только яблоки', 'Я собью только яблоки'),
 ('Мистер Кольбер!', 'Профессор Кольбер!'),
 ('Хозяйка', 'Госпожа'), ('хозяйка', 'госпожа'),
 ('new "Ч-Чёрт побери~~!!→ next scene 1664"', 'new "Ч-Чёрт побери~~!!"'),
 ('old "(D-Damn iiit~~!!)→ next scene 1664{#', 'old "(D-Damn iiit~~!!){#'),
 ('………。……。…。', '……… … …'),
]
for a, b in reps:
    c = s.count(a)
    print('RU', repr(a[:45]), 'x', c)
    s = s.replace(a, b)
RU.write_text(s, encoding='utf-8')

# EN .rpy and JA TL old: remove the leaked directive
for p in (EN, JA):
    t = p.read_text(encoding='utf-8')
    c = t.count('(D-Damn iiit~~!!)→ next scene 1664')
    if c:
        p.write_text(t.replace('(D-Damn iiit~~!!)→ next scene 1664', '(D-Damn iiit~~!!)'), encoding='utf-8')
        print(p.name, 'directive removed x', c)
