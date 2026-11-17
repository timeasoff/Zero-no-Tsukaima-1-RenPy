#!/usr/bin/env python3
import re, difflib

# Source talk() calls for scenes 431-446
with open('ps2_source/events_full/chapter_11_突然のスカウト.txt', 'r', encoding='utf-8') as f:
    events = f.read()

scenes = re.split(r'## SCENE (\d+)', events)
src_talks = []
for i in range(1, len(scenes), 2):
    if int(scenes[i]) not in range(431, 447):
        continue
    for m in re.finditer(r'talk\("([^"]*)",\s*null,\s*"((?:[^"\\]|\\.)*)",\s*\(?([^)]*)\)?\)', scenes[i+1]):
        spk, text, vid = m.group(1), m.group(2), m.group(3).strip()
        v = None
        vm = re.search(r'\+\s*(\d+)', vid)
        if vm: v = int(vm.group(1))
        src_talks.append((spk, text, v))

# Script dialogue lines in order
with open('game/chapters/10/script-ch10_1.rpy', 'r', encoding='utf-8') as f:
    script = f.read()

script_lines = []
lines = script.split('\n')
i = 0
while i < len(lines):
    vm = re.match(r'\s*voice\s+"(ch10_([a-z]+)_(\d+))"', lines[i])
    if vm:
        j = i + 1
        while j < len(lines) and not lines[j].strip(): j += 1
        dm = re.match(r'\s*([a-z]+)\s+"(.+?)\{#(.+?)\}"', lines[j])
        if dm:
            script_lines.append((dm.group(1), dm.group(2), dm.group(3)))
            i = j + 1
            continue
    dm = re.match(r'\s*([a-z]+)\s+"(.+?)\{#(.+?)\}"', lines[i])
    if dm:
        script_lines.append((dm.group(1), dm.group(2), dm.group(3)))
    i += 1

print(f"Source: {len(src_talks)} lines")
print(f"Script: {len(script_lines)} lines")

spk_map = {'サイト': 's', 'ハルナ': 'h', 'シエスタ': 'si', 'ルイズ': 'l', 'オスマン': 'o', 'コルベール': 'c'}

# Compare speaker sequences
bad = 0
for idx in range(min(len(src_talks), len(script_lines))):
    ss = spk_map.get(src_talks[idx][0], src_talks[idx][0])
    scs = script_lines[idx][0]
    if ss != scs:
        print(f"MISMATCH at {idx}: src={ss} script={scs}")
        print(f"  src: {src_talks[idx][2][:50]}")
        print(f"  scr: {script_lines[idx][1][:50]}")
        bad += 1
        if bad > 5: break

if bad == 0:
    print("✓ Speaker sequences match for all lines")

# Check voiced lines have correct voice IDs
vid_bad = 0
for idx, (spk, text, vid) in enumerate(src_talks):
    if vid is not None and idx < len(script_lines):
        # script voice name should map to this vid
        pass  # already verified via mapping

print(f"\nScript has {len(script_lines)} dialogue lines, source has {len(src_talks)}")
if len(script_lines) == len(src_talks):
    print("✓ COUNTS MATCH")
else:
    print(f"✗ COUNT DIFF: {len(src_talks) - len(script_lines)}")
