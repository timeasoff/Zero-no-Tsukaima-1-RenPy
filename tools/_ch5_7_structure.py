# -*- coding: utf-8 -*-
"""Карта структуры хвоста главы 5: core 341-343 + extra 1104-1163, 1870-1875.

Для каждой сцены: входящие/исходящие переходы (→ next), выборы (【選択肢】),
меню дат (dateItem из events), счёт голосов.
"""
import io, os, re, sys
from collections import defaultdict

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(ROOT, 'ps2_source', 'chapters', 'chapter_06_本当の想い.txt')
EV = os.path.join(ROOT, 'ps2_source', 'events_full', 'chapter_06_本当の想い.txt')

# ---- разбор chapters: сцены, → next, 【選択肢】, голоса ----
scenes = {}          # num -> {'next': set, 'choices': [(label,target)], 'voices': n, 'move': [...]}
cur = None
for ln in io.open(CH, encoding='utf-8'):
    ln = ln.rstrip('\n')
    m = re.match(r'^---- SCENE (\d+) ----', ln)
    if m:
        cur = int(m.group(1))
        scenes[cur] = {'next': set(), 'choices': [], 'voices': 0, 'moves': []}
        continue
    if cur is None:
        continue
    m = re.search(r'→ next scene (\d+)', ln)
    if m:
        scenes[cur]['next'].add(int(m.group(1)))
    m = re.search(r'【選択肢】(.+?) → scene (\d+)', ln)
    if m:
        scenes[cur]['choices'].append((m.group(1).strip(), int(m.group(2))))
    m = re.search(r'【移動】(.+?) → scene \d+.*?\+(\d+)\)\)', ln)
    if m:
        scenes[cur]['moves'].append((m.group(1).strip(), int(m.group(2))))
    if '[voice' in ln:
        scenes[cur]['voices'] += 1

# ---- разбор events: dateItem (меню дат) ----
date_menus = defaultdict(list)   # scene -> [(girl, target)]
cur = None
for ln in io.open(EV, encoding='utf-8'):
    ln = ln.rstrip('\n')
    m = re.match(r'^## SCENE (\d+)', ln)
    if m:
        cur = int(m.group(1))
        continue
    m = re.match(r'^DATE\s+dateItem\("([^"]+)", \(0x01000000 \+(\d+)\)\)', ln)
    if m and cur:
        date_menus[cur].append((m.group(1), int(m.group(2))))

TAIL = list(range(1104, 1164)) + list(range(1870, 1876)) + [341, 342, 343]
print('=== ГОЛОСА по сценам хвоста ===')
tot = 0
for sc in sorted(TAIL):
    if sc in scenes:
        v = scenes[sc]['voices']
        tot += v
        print('  %4d: голосов=%3d  next=%s  choices=%s  moves=%s  dateMenu=%s' % (
            sc, v, sorted(scenes[sc]['next']) or '-', scenes[sc]['choices'] or '-',
            scenes[sc]['moves'] or '-', date_menus.get(sc) or '-'))
print('ИТОГО голосов в 1104-1163 + 1870-1875 + 341/342:', tot)

# ---- к каким сценам идут переходы из хвоста (вне хвоста) ----
print('\n=== Исходы хвоста наружу ===')
for sc in sorted(TAIL):
    if sc in scenes:
        out = {n for n in scenes[sc]['next'] if n not in TAIL}
        if out:
            print('  %4d -> %s' % (sc, sorted(out)))
