# -*- coding: utf-8 -*-
"""Сверка: реплики в script-ch4_6.rpy ↔ реестр голосов (.tmp/part6_voices.txt)."""
import io, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

SCRIPT = 'game/chapters/4/script-ch4_6.rpy'
ROSTER = '.tmp/part6_voices.txt'

SPK2KEY = {'s': 's', 'l': 'l', 'h': 'h', 'si': 'si', 'ha': 'ha', 'd': 'd', 'ak': 'ak'}

# --- реестр: имя голоса -> (scene, ps2_id, spk) ---
roster = []
for ln in io.open(ROSTER, encoding='utf-8'):
    if ln.startswith('#'):
        continue
    p = ln.rstrip('\n').split('\t')
    if len(p) < 5:
        continue
    roster.append((int(p[0]), p[1], int(p[3]), p[4]))

# --- скрипт: последовательность (voice_name, speaker, text) ---
lines = io.open(SCRIPT, encoding='utf-8').read().splitlines()
script = []
i = 0
while i < len(lines):
    ln = lines[i]
    m = re.match(r'\s*voice\s+"([^"]+)"\s*$', ln)
    if m:
        vn = m.group(1)
        spk, text = None, None
        j = i + 1
        while j < len(lines) and lines[j].strip() == '':
            j += 1
        if j < len(lines):
            m2 = re.match(r'\s*(\w+)\s+"(.*)"\s*$', lines[j])
            if m2:
                spk, text = m2.group(1), m2.group(2)
        script.append((vn, spk, text))
        i = j
    i += 1

print('roster voices:', len(roster))
print('script voices:', len(script))

# 1) имена голосов по порядку
bad = 0
for k, (sc, spk, vid, vn) in enumerate(roster):
    if k >= len(script):
        print('MISSING in script:', vn, '(scene %d, id %d)' % (sc, vid))
        bad += 1
        continue
    svn, sspk, stext = script[k]
    if svn != vn:
        print('MISMATCH #%d: roster %s (scene %d id %d) vs script %s' % (k, vn, sc, vid, svn))
        bad += 1
        if bad > 25:
            print('...more'); break
if len(script) > len(roster):
    for k in range(len(roster), len(script)):
        print('EXTRA in script:', script[k][0])

# 2) диалоги без голоса (th / без voice)
print('\n--- строки реплик без voice ---')
i = 0
n = 0
while i < len(lines):
    ln = lines[i]
    m = re.match(r'\s*(th|[a-z_]+)\s+"(.*)"\s*$', ln)
    if m and not re.match(r'\s*voice', ln):
        prev = lines[i-1].strip() if i else ''
        if not prev.startswith('voice'):
            n += 1
            if n <= 40:
                print('%5d %s' % (i + 1, ln.strip()[:100]))
    i += 1
print('total no-voice lines:', n)
