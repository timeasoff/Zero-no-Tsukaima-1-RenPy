#!/usr/bin/env python3
# Fix ch10_2: rename ch10_ha_* -> ch10_h_065..104, update TL, manifest
import re, json, shutil

# --- 1. Load script ---
with open('game/chapters/10/script-ch10_2.rpy', encoding='utf-8') as f:
    script = f.read()

# Map old tags -> new tags for Haruna (only for voiced lines)
# Voice IDs 2519..2558 (40 voiced lines)
# ch10_1 ends at ch10_h_064=2518, so next is ch10_h_065=2519
# Need to track which ha_ tags have voice statements

# First pass: find all voice statements for Haruna
voice_map = {}  # old_tag -> new_tag
# We'll scan the script for: voice "ch10_ha_NNN" followed by ha "...{#ch10_ha_NNN}"
voice_pattern = re.compile(r'voice "(ch10_ha_\d+)"')
tag_pattern = re.compile(r'\{#(ch10_ha_\d+)\}')

# Find all ha_ tags in script (both voice statements and dialogue tags)
ha_tags_in_voice = []
ha_tags_in_dialogue = []

for m in voice_pattern.finditer(script):
    ha_tags_in_voice.append(m.group(1))

for m in tag_pattern.finditer(script):
    ha_tags_in_dialogue.append(m.group(1))

print(f"Ha tags in voice statements: {len(ha_tags_in_voice)}")
print(f"Ha tags in dialogue: {len(ha_tags_in_dialogue)}")
print(f"Voice tags: {ha_tags_in_voice[:5]}...")
print(f"Dialogue tags: {ha_tags_in_dialogue[:5]}...")

# The voice statements and dialogue tags should correspond 1:1 for voiced lines
# But some dialogue tags have no voice (null voice lines)
# We'll assign sequential numbers 065.. to voice statements

# Build mapping: old_ha_tag -> new_h_tag
# For each voiced line (voice statement), assign next number
counter = 65
mapping = {}
for old in ha_tags_in_voice:
    new = f"ch10_h_{counter:03d}"
    mapping[old] = new
    counter += 1

# For dialogue tags that DON'T have voice (null voice), also assign sequential
# But they should share the same counter? Actually they're interspersed.
# Better: assign based on dialogue order for ALL ha tags, matching voice statements where present

print(f"Assigned {len(mapping)} voice mappings")
for old, new in mapping.items():
    print(f"  {old} -> {new}")

# Now we need to replace in script:
# 1. voice "ch10_ha_NNN" -> voice "ch10_h_MMM"
# 2. {#ch10_ha_NNN} -> {#ch10_h_MMM} in dialogue lines

def replace_ha(match):
    old = match.group(1)
    return match.group(0).replace(old, mapping.get(old, old))

# For voice statements
def repl_voice(m):
    old = m.group(1)
    new = mapping.get(old, old)
    return f'voice "{new}"'

script_new = re.sub(r'voice "(ch10_ha_\d+)"', repl_voice, script)

# For tags in dialogue and thoughts
def repl_tag(m):
    old = m.group(1)
    new = mapping.get(old, old)
    return f'{{#{new}}}'

script_new = re.sub(r'\{#(ch10_ha_\d+)\}', repl_tag, script_new)

# Also need to update ha_ in comments? No, comments are just comments.

# Verify no ch10_ha_ remains
remaining = re.findall(r'ch10_ha_\d+', script_new)
print(f"Remaining ch10_ha_ in script: {len(remaining)}")
if remaining:
    for r in remaining[:10]:
        print(f"  {r}")

# --- 2. Write updated script ---
shutil.copy2('game/chapters/10/script-ch10_2.rpy', 'game/chapters/10/script-ch10_2.rpy.bak')
with open('game/chapters/10/script-ch10_2.rpy', 'w', encoding='utf-8') as f:
    f.write(script_new)
print("Updated script-ch10_2.rpy")

# --- 3. Update TL files ---
def update_tl_file(tl_path, mapping):
    with open(tl_path, encoding='utf-8') as f:
        content = f.read()
    
    def repl(m):
        old_tag = m.group(1)
        new_tag = mapping.get(old_tag, old_tag)
        # The old string has {#old_tag}, replace with {#new_tag}
        return m.group(0).replace(f'{{#{old_tag}}}', f'{{#{new_tag}}}')
    
    # Replace in old strings (the part before the colon)
    # Pattern: old "text {#tag}": "new"
    new_content = re.sub(r'old "([^"]*\{#ch10_ha_\d+\}[^"]*)"', lambda m: m.group(0).replace(m.group(1), m.group(1).replace(m.group(1)[m.group(1).find('{#'):m.group(1).find('}')+1], f'{{#{mapping.get(m.group(1)[m.group(1).find('{#')+2:m.group(1).find('}')]]}')}'), content)
    
    # Simpler: just replace all {#ch10_ha_NNN} in the file
    def repl_all(m):
        old = m.group(1)
        new = mapping.get(old, old)
        return f'{{#{new}}}'
    
    new_content = re.sub(r'\{#(ch10_ha_\d+)\}', repl_all, content)
    
    with open(tl_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {tl_path}")

update_tl_file('game/tl/japanese/ch10_2_dialogs.rpy', mapping)
update_tl_file('game/tl/russian/ch10_2_dialogs.rpy', mapping)

# --- 4. Update manifest ---
# Read manifest
with open('references/voice_id_map.csv', encoding='utf-8') as f:
    manifest_lines = f.readlines()

# Find where to insert ch10_2 rows (after last ch10 row)
insert_idx = None
for i, line in enumerate(manifest_lines):
    if line.startswith('ch10_') and not manifest_lines[i+1].startswith('ch10_'):
        insert_idx = i + 1
        break

print(f"Insert manifest rows at line {insert_idx}")

# Build new rows for ch10_2
# Voice ID sequence from script comments: we need to extract them
# Let's parse the script for voice IDs from JA comments

# From the original script (before fix), JA comments had [voice N]
# Let's extract mapping from backup
with open('game/chapters/10/script-ch10_2.rpy.bak', encoding='utf-8') as f:
    orig_script = f.read()

# Find all voice statements and their following [voice ID]
voice_id_map = {}  # old_ha_tag -> voice_id
lines = orig_script.split('\n')
for i, line in enumerate(lines):
    vm = re.match(r'^\s*voice "(ch10_ha_\d+)"', line)
    if vm:
        old_tag = vm.group(1)
        # Look for [voice ID] in next few lines
        for j in range(i+1, min(i+3, len(lines))):
            jm = re.search(r'\[voice (\d+)\]', lines[j])
            if jm:
                voice_id_map[old_tag] = jm.group(1)
                break

print(f"Found {len(voice_id_map)} voice IDs:")
for old, vid in voice_id_map.items():
    print(f"  {old} -> {vid}")

# Build manifest rows for voiced lines only
new_rows = []
for old_tag in ha_tags_in_voice:
    new_tag = mapping[old_tag]
    vid = voice_id_map.get(old_tag)
    if vid:
        new_rows.append(f"{new_tag},{vid},,\n")

print(f"Adding {len(new_rows)} manifest rows for Haruna:")
for r in new_rows:
    print(f"  {r.strip()}")

# Also need to add other speakers from ch10_2: s, si, l, o, c, w, k, m
# Let's extract all voice statements and IDs from the original script
all_voice_ids = {}
for i, line in enumerate(lines):
    vm = re.match(r'^\s*voice "(ch10_[a-z_]+_\d+)"', line)
    if vm:
        vname = vm.group(1)
        for j in range(i+1, min(i+3, len(lines))):
            jm = re.search(r'\[voice (\d+)\]', lines[j])
            if jm:
                all_voice_ids[vname] = jm.group(1)
                break

print(f"\nAll voice statements with IDs ({len(all_voice_ids)}):")
for vname, vid in sorted(all_voice_ids.items()):
    print(f"  {vname} -> {vid}")

# Now add ALL ch10_2 rows (not just Haruna) that aren't already in manifest
# Check existing manifest
existing = set()
for line in manifest_lines:
    if line.startswith('ch10_'):
        parts = line.strip().split(',')
        if parts:
            existing.add(parts[0])

print(f"\nExisting ch10 manifest entries: {len(existing)}")
# Check which ch10_2 voice names are missing
for vname in sorted(all_voice_ids.keys()):
    if vname not in existing and vname not in mapping.values():
        vid = all_voice_ids[vname]
        new_rows.append(f"{vname},{vid},,\n")
        print(f"  Adding missing: {vname},{vid}")

# Insert new rows into manifest
if new_rows:
    manifest_lines = manifest_lines[:insert_idx] + new_rows + manifest_lines[insert_idx:]
    with open('references/voice_id_map.csv', 'w', encoding='utf-8') as f:
        f.writelines(manifest_lines)
    print(f"\nUpdated manifest with {len(new_rows)} new rows")
else:
    print("No new manifest rows needed")

print("\nDone! Now run checks.")