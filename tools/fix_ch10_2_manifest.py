#!/usr/bin/env python3
"""Extract voice IDs (from preceding [voice N] comment) and add manifest rows for ch10_2."""
import re

SCRIPT = 'game/chapters/10/script-ch10_2.rpy'
MANIFEST = 'references/voice_id_map.csv'

with open(SCRIPT, encoding='utf-8') as f:
    lines = f.read().split('\n')

voice_map = []  # (voice_name, voice_id)
for i, line in enumerate(lines):
    vm = re.match(r'^\s*voice "(ch10_[a-z_]+_\d+)"', line)
    if vm:
        vname = vm.group(1)
        vid = None
        # Preceding comment line usually holds [voice N]
        if i > 0:
            pm = re.search(r'\[voice (\d+)\]', lines[i-1])
            if pm:
                vid = pm.group(1)
        # Fallback: following # JA[N]: comment
        if not vid:
            for j in range(i+1, min(i+3, len(lines))):
                jm = re.search(r'# JA\[(\d+)\]', lines[j])
                if jm:
                    vid = jm.group(1)
                    break
        voice_map.append((vname, vid))

voiced = [(n, v) for n, v in voice_map if v]
nullv = [(n, v) for n, v in voice_map if not v]
print(f"Voice statements: {len(voice_map)}; voiced={len(voiced)}, null={len(nullv)}")
if nullv:
    print("Null-voice names:", [n for n, _ in nullv])

# Load manifest
with open(MANIFEST, encoding='utf-8') as f:
    mlines = f.readlines()

existing = set()
for line in mlines:
    p = line.strip().split(',')
    if p:
        existing.add(p[0])

# Determine last ch10 entry line index
last_idx = -1
for i, line in enumerate(mlines):
    if line.startswith('ch10_'):
        last_idx = i

new_rows = []
for vname, vid in voiced:
    if vname in existing:
        print(f"  SKIP existing: {vname}")
        continue
    new_rows.append(f'{vname},{vid},,\n')

print(f"New manifest rows: {len(new_rows)}")
for r in new_rows:
    print(f"  {r.strip()}")

if new_rows:
    mlines = mlines[:last_idx+1] + new_rows + mlines[last_idx+1:]
    with open(MANIFEST, 'w', encoding='utf-8') as f:
        f.writelines(mlines)
    print(f"Manifest updated.")

# Verify all script voices covered
missing = [n for n, v in voiced if n not in existing and f'{n},{v},,\n' not in new_rows]
print(f"Uncovered voiced: {missing}")