#!/usr/bin/env python3
"""Regenerate ch10_2 TL files from the current (fixed) script."""
import re, json

SCRIPT = 'game/chapters/10/script-ch10_2.rpy'
JA_TL = 'game/tl/japanese/ch10_2_dialogs.rpy'
RU_TL = 'game/tl/russian/ch10_2_dialogs.rpy'

with open(SCRIPT, encoding='utf-8') as f:
    lines = f.read().split('\n')

entries_ja = []  # (old_str, tag_inner, ja_new)
entries_ru = []  # (old_str, tag_inner, ru_new)

i = 0
while i < len(lines):
    m = re.match(r'^\s+(s|ha|si|l|o|c|w|k|m|t)\s+"([^"]*)"\s*$', lines[i])
    if m:
        full_text = m.group(2)  # content inside quotes, e.g. "...... Yes. {#ch10_s_075}"
        # full_text should contain a tag {#...}
        tm = re.match(r'^(.*)\{(#ch10_[a-z_]+_\d+)\}$', full_text)
        if tm:
            en_text = tm.group(1)  # text before tag, e.g. "...... Yes. "
            tag_inner = tm.group(2)  # #ch10_s_075
            old_str = full_text  # full string with tag
            tag = f'{{{tag_inner}}}'

            ja = None
            for j in range(i+1, min(i+4, len(lines))):
                jm = re.match(r'^\s+# JA\[(\d+)\]: (.*)$', lines[j])
                if jm:
                    ja = jm.group(2).strip()
                    break
            if not ja:
                ja = f"[NO JA] {tag_inner}"
            entries_ja.append((old_str, tag_inner, ja))

            ru_key = None
            tm2 = re.match(r'^#ch10_h_(\d+)$', tag_inner)
            if tm2:
                ru_key = f'ch10_ha_{int(tm2.group(1)) - 64:03d}'
            else:
                ru_key = tag_inner[1:]
            ru_map = json.load(open('/tmp/ch10_2_ru.json', encoding='utf-8'))
            ru_new = ru_map.get(ru_key) or ru_map.get(tag_inner) or f"[NO RU] {tag_inner}"
            entries_ru.append((old_str, tag_inner, ru_new))
        i += 1
        continue
    i += 1

print(f"Found {len(entries_ja)} dialogue entries")

# Write JA TL
with open(JA_TL, 'w', encoding='utf-8') as f:
    f.write('# translate japanese strings:\n')
    f.write('# (ch10_2: scenes 451-466, 136 dialogue lines)\n')
    seen = set()
    for old_str, tag_inner, ja in entries_ja:
        if old_str in seen:
            continue
        seen.add(old_str)
        f.write(f'    old "{old_str}"\n')
        f.write(f'    new "{ja}"\n')

# Write RU TL
with open(RU_TL, 'w', encoding='utf-8') as f:
    f.write('# translate russian strings:\n')
    f.write('# (ch10_2: scenes 451-466, 136 dialogue lines)\n')
    seen = set()
    for old_str, tag_inner, ru in entries_ru:
        if old_str in seen:
            continue
        seen.add(old_str)
        f.write(f'    old "{old_str}"\n')
        f.write(f'    new "{ru}"\n')

print(f"Wrote JA + RU TL with {len(seen)} entries each")