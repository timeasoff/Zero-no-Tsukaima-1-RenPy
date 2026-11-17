#!/usr/bin/env python3
"""Fix TL files: proper old/new format."""
import json, re

# Load pairs
pairs = json.load(open('/tmp/ch10_2_pairs.json', encoding='utf-8'))

# Generate correct TL entries
ja_entries = []
ru_entries = []

for p in pairs:
    # EN text is p['en']
    old_ja = p['ja']
    old_ru = ru_map[p['tag']]  # RU translation
    
    # Build entries
    ja_entries.append((p['en'], old_ja))  # old = EN text, new = JA text
    ru_entries.append((p['en'], old_ru))  # old = EN text, new = RU text

# Write JA TL
with open('game/tl/japanese/ch10_2_dialogs.rpy', 'w', encoding='utf-8') as f:
    f.write('# translate japanese strings:\n')
    f.write('# (ch10_2: scenes 451-466, 136 dialogue lines)\n')
    for old, new in ja_entries:
        f.write(f'    old "{old}": "{new}"\n')

# Write RU TL
with open('game/tl/russian/ch10_2_dialogs.rpy', 'w', encoding='utf-8') as f:
    f.write('# translate russian strings:\n')
    f.write('# (ch10_2: scenes 451-466, 136 dialogue lines)\n')
    for old, new in ru_entries:
        f.write(f'    old "{old}": "{new}"\n')

print("Fixed TL files with proper format.")