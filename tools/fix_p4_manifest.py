# -*- coding: utf-8 -*-
# Исправление манифеста voice_id_map.csv для главы 3, части 4.
# Удаляет все битые записи ch3.2_* и добавляет 93 канонические по ps2_source:
#   si 14659-14688 -> ch3.2_si_001..030
#   ha 2164-2188   -> ch3.2_ha_001..025
#   s  11282-11310 -> ch3.2_s_001..029
#   l  5938-5946   -> ch3.2_l_001..009
import io

path = 'references/voice_id_map.csv'
lines = io.open(path, encoding='utf-8').read().splitlines()

kept = [l for l in lines if not l.split(',', 1)[0].strip().startswith('ch3.2_')]
removed = len(lines) - len(kept)

rows = []
def add(speaker, lo, hi):
    n = 0
    for vid in range(lo, hi + 1):
        n += 1
        rows.append('ch3.2_%s_%03d,%d' % (speaker, n, vid))

add('si', 14659, 14688)
add('ha', 2164, 2188)
add('s', 11282, 11310)
add('l', 5938, 5946)

text = '\n'.join(kept).rstrip('\n') + '\n' + '\n'.join(rows) + '\n'
io.open(path, 'w', encoding='utf-8', newline='').write(text)

print('removed broken:', removed)
print('added canonical:', len(rows))
print('total lines now:', len(kept) + len(rows))
