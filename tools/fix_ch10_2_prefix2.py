#!/usr/bin/env python3
# Simple fix for ch10_2: rename ch10_ha_XXX -> ch10_h_(XXX+64) for both voice names and tags
import re, json, os

# --- 1. Load script ---
with open('game/chapters/10/script-ch10_2.rpy', encoding='utf-8') as f:
    script = f.read()

# Find all occurrences of ch10_ha_ followed by 3 digits
ha_pattern = re.compile(r'ch10_ha_(\d{3})')

# Build mapping: replace with ch10_h_(int+64)
matches = ha_pattern.findall(script)
print(f"Found {len(matches)} ch10_ha_XXX occurrences in script")

# Create mapping dict
mapping = {}
for old_num_str in matches:
    old_num = int(old_num_str)
    new_num = old_num + 64
    mapping[old_num] = new_num
    # Print first/last few
    if old_num <= 5 or old_num >= len(matches)-2:
        print(f"  ch10_ha_{old_num:03d} -> ch10_h_{new_num:03d}")

# Replace in script - all occurrences of ch10_ha_ in voice and tags
# For voice statements
script = re.sub(r'voice "ch10_ha_(\d{3})"', lambda m: f'voice "ch10_h_{int(m.group(1))+64:03d}"', script)

# For tags in dialogue: {#ch10_ha_XXX}
script = re.sub(r'\{#(ch10_ha_)(\d{3})\}', lambda m: f'{{#ch10_h_{int(m.group(2))+64:03d}}}', script)

# Write script
script_path = 'game/chapters/10/script-ch10_2.rpy'
with open(script_path, 'w', encoding='utf-8') as f:
    f.write(script)
print(f"Updated {script_path}")

# --- 2. Verify ---
remaining = ha_pattern.findall(script)
print(f"Remaining ch10_ha_ after replacement: {len(remaining)}")

# --- 3. Update TL files ---

def update_tl_file(tl_path):
    if not os.path.exists(tl_path):
        print(f"TL file {tl_path} does not exist, skipping")
        return
    with open(tl_path, encoding='utf-8') as f:
        content = f.read()
    # Replace all ch10_ha_XXX -> ch10_h_XXX+64
    def repl_all(m):
        old_num = int(m.group(1))
        new_num = old_num + 64
        return f'ch10_h_{new_num:03d}'
    new_content = re.sub(r'ch10_ha_(\d{3})', repl_all, content)
    with open(tl_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated TL file: {tl_path}")

update_tl_file('game/tl/japanese/ch10_2_dialogs.rpy')
update_tl_file('game/tl/russian/ch10_2_dialogs.rpy')

# --- 4. Update manifest ---
# Find last ch10 entry in manifest
with open('references/voice_id_map.csv', encoding='utf-8') as f:
    manifest_lines = f.readlines()

last_idx = None
for i, line in enumerate(manifest_lines):
    if line.startswith('ch10_') or i == len(manifest_lines) - 1:
        last_idx = i

# If last line doesn't start with ch10_, go back
while last_idx and not manifest_lines[last_idx].startswith('ch10_'):
    last_idx -= 1

if last_idx is None:
    print("No ch10 entries in manifest")
else:
    print(f"Last ch10 manifest entry at line {last_idx}: {manifest_lines[last_idx].strip()}")
    # Add new rows after it
    # Get voice data from script
    # Script already updated; voice IDs from original source: 2519..2558 for ha, 13170..13215 for s, etc.
    # Build new rows: ch10_h_065,2519 through ch10_h_104,2558 (40 rows for ha)
    # Plus others from ch10_2
    new_rows = []
    # Saito: s_063 -> 13170, ... s_118 -> 13215
    for i in range(63, 119):
        vname = f'ch10_s_{i:03d}'
        vid = 13170 + (i - 63)
        new_rows.append(f'{vname},{vid},,\n')
    # Haruna: h_065 -> 2519 through h_104 -> 2558
    for i in range(65, 105):
        vname = f'ch10_h_{i:03d}'
        vid = 2519 + (i - 65)
        new_rows.append(f'{vname},{vid},,\n')
    # Siesta: si_032 -> 15109, ... si_042 -> 15119
    for i in range(32, 43):
        vname = f'ch10_si_{i:03d}'
        vid = 15109 + (i - 32)
        new_rows.append(f'{vname},{vid},,\n')
    # Louise: l_009 -> 7150, ... l_018 -> 7159
    for i in range(9, 19):
        vname = f'ch10_l_{i:03d}'
        vid = 7150 + (i - 9)
        new_rows.append(f'{vname},{vid},,\n')
    # Osmond: o_007 -> 4506, ... o_011 -> 4510
    for i in range(7, 12):
        vname = f'ch10_o_{i:03d}'
        vid = 4506 + (i - 7)
        new_rows.append(f'{vname},{vid},,\n')
    # Colbert: c_004 -> 1203
    new_rows.append('ch10_c_004,1203,,')
    # Wesley: w_001 -> 16073 through w_008 -> 16080
    for i in range(1, 9):
        vname = f'ch10_w_{i:03d}'
        vid = 16073 + (i - 1)
        new_rows.append(f'{vname},{vid},,\n')
    # Kirche: k_001 -> 3813
    new_rows.append('ch10_k_001,3813,,')
    # Tabitha: t_001 - null voice, no voice ID needed
    # Montmorency: m_005 -> 4157
    new_rows.append('ch10_m_005,4157,,')
    
    # Insert new rows after last ch10 entry
    manifest_lines = manifest_lines[:last_idx+1] + new_rows + manifest_lines[last_idx+1:]
    
    with open('references/voice_id_map.csv', 'w', encoding='utf-8') as f:
        f.writelines(manifest_lines)
    
    print(f"\nUpdated manifest with {len(new_rows)} new rows")
    for r in new_rows:
        print(f"  {r.strip()}")
    
print("\nFix completed!")