#!/usr/bin/env python3
"""Third round of confirmed literary fixes (prompt 10), sp91."""
from pathlib import Path

p = Path(__file__).parent.parent / 'game/tl/russian/sp91_dialogs.rpy'
s = p.read_text(encoding='utf-8')
REPS = [
 ('Н-нет, я… Луиз…?', 'Н-нет, я… Луиза…?'),
 ('Луиз весь день была рядом', 'Луиза весь день была рядом'),
 ('С-слушай. Луиз.', 'С-слушай. Луиза.'),
 ('Это просто оговорка!', 'Это просто фигура речи!'),
 ('……Я могу больше не сдержаться.', '……Может, я больше не сдержусь.'),
 ('в дворянских семьях', 'в аристократических семьях'),
 ('Но я не дворянин — я простолюдин.', 'Но я не аристократ — я простолюдин.'),
 ('…Разве это не странно?', '…Разве это не противоречие?'),
]
for a, b in REPS:
    c = s.count(a)
    print(repr(a[:45]), '->', repr(b[:45]), 'x', c)
    s = s.replace(a, b)
p.write_text(s, encoding='utf-8')
