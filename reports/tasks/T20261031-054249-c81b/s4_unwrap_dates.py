# -*- coding: utf-8 -*-
"""Снятие 5 конструкций `if louise_sympathy == 100: call sp_l1 / else:` из
script-ch1_10.rpy (условие переехало в ch1_10 до portrait_choice — по SCENE_0003
date():2555/2564). Тело else дедентится на 4 пробела. Стоп-условие: первая
непустая строка с отступом <= 4 (уровень тела label)."""
import io
import re

path = 'game/chapters/1/script-ch1_10.rpy'
lines = io.open(path, encoding='utf-8').read().split('\n')
out = []
i = 0
removed = 0
while i < len(lines):
    l = lines[i]
    if (re.match(r'^    if louise_sympathy == 100:\s*$', l)
            and i + 2 < len(lines)
            and re.match(r'^        call sp_l1 from _call_sp_l1_\d+\s*$', lines[i + 1])
            and re.match(r'^    else:\s*$', lines[i + 2])):
        j = i + 3
        body = []
        while j < len(lines):
            s = lines[j]
            if s.strip() and (len(s) - len(s.lstrip())) <= 4:
                break
            body.append(s)
            j += 1
        assert body and body[0].strip(), 'пустое тело else в строке %d' % (i + 1)
        for b in body:
            if b.strip():
                assert b.startswith('    '), 'строка тела без отступа 4: %r' % b
                out.append(b[4:])
            else:
                out.append(b)
        removed += 1
        i = j
        continue
    out.append(l)
    i += 1

assert removed == 5, 'удалено конструкций: %d (ожидалось 5)' % removed
text = '\n'.join(out)
assert 'louise_sympathy == 100' not in text, 'остались условия == 100'
assert 'call sp_l1' not in text, 'call sp_l1 остался внутри date_*'
io.open(path, 'w', encoding='utf-8', newline='\n').write(text)
print('OK: снято 5 if/else, условий == 100 не осталось')
