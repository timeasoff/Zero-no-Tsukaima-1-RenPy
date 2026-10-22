# -*- coding: utf-8 -*-
"""Пометка использованных строк transcriptions_ja_ru.csv для части 4 главы 5.

Правило — идти по id, а не по тексту: строки, чей voice_id (из манифеста
части 4 главы 5) совпал с filename в CSV, получают в status пометку с именем
.ogg. Пометки частей 1–3 (префиксы ch5_, ch5.2_, ch5.3_) не затрагиваются.

Запуск: python tools/mark_ch5_4_transcriptions.py
"""
import csv
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, 'transcriptions_ja_ru.csv')
MANIFEST = os.path.join(ROOT, 'references', 'voice_id_map.csv')
WAV_ID_RE = re.compile(r'_([0-9A-Fa-f]{8})\.wav$')
PREFIX = 'ch5.4_'

# voice_id -> имя ogg для части 4 главы 5
ogg = {}
for ln in io.open(MANIFEST, encoding='utf-8'):
    p = ln.rstrip('\n').split(',')
    if len(p) >= 2 and p[0].startswith(PREFIX):
        ogg[int(p[1])] = p[0] + '.ogg'

rows = []
with io.open(CSV_PATH, encoding='utf-8', newline='') as fh:
    r = csv.reader(fh)
    header = next(r)
    for row in r:
        rows.append(row)

marked = 0
for row in rows:
    if not row:
        continue
    fn = row[0]
    m = WAV_ID_RE.search(fn)
    if not m:
        continue
    vid = int(m.group(1), 16)
    if vid not in ogg:
        continue
    status = row[3] if len(row) > 3 else ''
    if ogg[vid] in status:
        continue
    while len(row) < 4:
        row.append('')
    row[3] = (status + '   ' + ogg[vid]).strip() if status else ogg[vid]
    marked += 1

with io.open(CSV_PATH, 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh, lineterminator='\n')
    w.writerow(header)
    for row in rows:
        w.writerow(row)

print('помечено строк:', marked, 'из', len(ogg), 'голосов части 4 главы 5')
