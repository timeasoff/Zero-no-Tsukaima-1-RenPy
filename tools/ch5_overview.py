# -*- coding: utf-8 -*-
"""Обзор главы 5: сцены, границы строк, число голосов (для резки по §3)."""
import io, re, sys, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SRC = glob.glob('/workspace/ps2_source/chapters/chapter_06_*.txt')[0]
EVT = glob.glob('/workspace/ps2_source/events_full/chapter_06_*.txt')[0]

# --- главы: сцены из chapters-файла ---
lines = io.open(SRC, encoding='utf-8', errors='replace').read().splitlines()
scenes = []
for i, ln in enumerate(lines):
    m = re.match(r'^----\s*SCENE\s*(\d+)\s*----', ln.strip())
    if m:
        scenes.append((int(m.group(1)), i))
print('сцен в chapters-файле:', len(scenes), '| первая:', scenes[0][0], '| последняя:', scenes[-1][0])

# --- голоса по сценам из events_full ---
cur = None
voice = {}
extra = {}
for ln in io.open(EVT, encoding='utf-8', errors='replace'):
    m = re.match(r'^## SCENE (\d+)', ln)
    if m:
        cur = int(m.group(1))
        voice.setdefault(cur, 0)
        continue
    if cur is None:
        continue
    if re.match(r'^DIALOGUE\s+talk\(', ln) and re.search(r'\(0x0[46]000000 \+\d+\)', ln):
        voice[cur] += 1

# --- сцены «ядра» (269..343) и extra ---
CORE = [s for s, _ in scenes if s <= 343]
EX = [s for s, _ in scenes if s > 343]
print('ядро:', len(CORE), 'сцен (269..343); extra:', len(EX))
print()
print('--- ядро: сцены, строки, голоса ---')
tot = 0
for idx, (s, start) in enumerate(scenes):
    if s > 343:
        break
    end = scenes[idx + 1][1] if idx + 1 < len(scenes) else len(lines)
    v = voice.get(s, 0)
    tot += v
    print('  %4d  строки %5d–%5d  голосов %3d  (всего %4d)' % (s, start + 1, end, v, tot))
print()
print('--- extra: сцены и голоса (первые 30) ---')
for s in EX[:30]:
    print('  %4d  голосов %3d' % (s, voice.get(s, 0)))
print('extra всего сцен:', len(EX), '| голосов в extra:', sum(voice.get(s, 0) for s in EX))
print('голосов в ядре:', tot)
