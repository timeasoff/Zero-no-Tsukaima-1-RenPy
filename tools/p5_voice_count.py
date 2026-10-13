# -*- coding: utf-8 -*-
# Счётчик [voice N] по сценам chapter_04 для определения границы P5.
import io
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

text = io.open('ps2_source/chapters/chapter_04_女の戦い.txt', encoding='utf-8').read()
lines = text.splitlines()

scenes = []  # (scene_no, voice_count)
cur = None
count = 0
for ln in lines:
    m = re.match(r'---- SCENE (\d+) ----', ln)
    if m:
        if cur is not None:
            scenes.append((cur, count))
        cur = int(m.group(1))
        count = 0
    else:
        count += len(re.findall(r'\[voice (\d+)\]', ln))
if cur is not None:
    scenes.append((cur, count))

d = dict(scenes)

# P5 candidates: 169..178 then move branches
core = list(range(169, 179))
total = 0
for s in core:
    total += d.get(s, 0)
    print('scene %d: %d (cum %d)' % (s, d.get(s, 0), total))

print('--- after 178: move branches ---')
for start, end, name in ((1322, 1326, 'louise'), (1327, 1331, 'kirche'),
                         (1332, 1336, 'tabitha'), (1337, 1341, 'kitchen')):
    t = 0
    for s in range(start, end + 1):
        t += d.get(s, 0)
    print('%s: scenes %d-%d voices=%d -> total %d' % (name, start, end, t, total + t))

print('--- next scenes 179-186 ---')
t2 = 0
for s in range(179, 187):
    t2 += d.get(s, 0)
    print('scene %d: %d (cum %d)' % (s, d.get(s, 0), t2))
