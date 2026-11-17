#!/usr/bin/env python3
"""Fix ch10_2: rename ch10_ha_XXX -> ch10_h_(XXX+64), update TL files, add manifest rows."""
import re, os

SCRIPT = 'game/chapters/10/script-ch10_2.rpy'
JA_TL = 'game/tl/japanese/ch10_2_dialogs.rpy'
RU_TL = 'game/tl/russian/ch10_2_dialogs.rpy'
MANIFEST = 'references/voice_id_map.csv'

# --- 1. Load script ---
with open(SCRIPT, encoding='utf-8') as f:
    script = f.read()

# Find all ch10_ha_NNN occurrences
ha_pattern = re.compile(r'ch10_ha_(\d{3})')
matches = ha_pattern.findall(script)
print(f"Found {len(matches)} ch10_ha_XXX occurrences")

# Rename: ch10_ha_NNN -> ch10_h_NNN+64  (since part1 ends at h_064)
def repl(m):
    old_num = int(m.group(1))
    new_num = old_num + 64
    return f'ch10_h_{new_num:03d}'

# Replace everywhere in script (voice names + tags + comments)
script = re.sub(r'ch10_ha_(\d{3})', repl, script)

with open(SCRIPT, 'w', encoding='utf-8') as f:
    f.write(script)

# Verify
remaining = re.findall(r'ch10_ha_', script)
print(f"Remaining ch10_ha_: {len(remaining)}")

# --- 2. Extract voice mappings from script ---
# Find: voice "ch10_XXX_NNN" followed by [voice N] comment
voice_statements = []
lines = script.split('\n')
for i, line in enumerate(lines):
    vm = re.match(r'^\s*voice "(ch10_[a-z_]+_\d+)"', line)
    if vm:
        vname = vm.group(1)
        # Look ahead for [voice N]
        vid = None
        for j in range(i+1, min(i+3, len(lines))):
            jm = re.search(r'\[voice (\d+)\]', lines[j])
            if jm:
                vid = jm.group(1)
                break
        voice_statements.append((vname, vid))
        print(f"  voice {vname} -> id {vid}")

# Separate voiced from null-voice
voiced = [(n, v) for n, v in voice_statements if v]
null_voice = [(n, v) for n, v in voice_statements if not v]
print(f"\nVoiced lines: {len(voiced)}, null voice: {len(null_voice)}")

# --- 3. Update TL files ---
def update_tl(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()
    def repl_all(m):
        old_num = int(m.group(1))
        new_num = old_num + 64
        return f'ch10_h_{new_num:03d}'
    content = re.sub(r'ch10_ha_(\d{3})', repl_all, content)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated TL: {path}")

update_tl(JA_TL)
update_tl(RU_TL)

# --- 4. Update manifest ---
# Read manifest
with open(MANIFEST, encoding='utf-8') as f:
    manifest_lines = f.readlines()

# Find last ch10 entry index
last_idx = -1
for i, line in enumerate(manifest_lines):
    if line.startswith('ch10_'):
        last_idx = i

print(f"\nLast ch10 manifest entry at line {last_idx}: {manifest_lines[last_idx].strip()}")

# Build manifest rows for voiced ch10_2 entries
new_rows = []
for vname, vid in voiced:
    new_rows.append(f'{vname},{vid},,\n')

print(f"\nAdding {len(new_rows)} manifest rows:")
for r in new_rows:
    print(f"  {r.strip()}")

# Check for duplicates with existing manifest
existing = set()
for line in manifest_lines:
    parts = line.strip().split(',')
    if parts:
        existing.add(parts[0])

dup = [r for r in new_rows if r.split(',')[0] in existing]
if dup:
    print(f"\nWARNING: {len(dup)} duplicates will be added!")
    for d in dup[:5]:
        print(f"  {d.strip()}")

# Insert after last ch10 entry
manifest_lines = manifest_lines[:last_idx+1] + new_rows + manifest_lines[last_idx+1:]

with open(MANIFEST, 'w', encoding='utf-8') as f:
    f.writelines(manifest_lines)

print(f"\nManifest updated with {len(new_rows)} new rows")
print("\nDone!")