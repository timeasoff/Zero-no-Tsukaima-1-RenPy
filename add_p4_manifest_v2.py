import io, re

# Extract voices from PS2 source scenes 163-168
lines = io.open('ps2_source/chapters/chapter_04_女の戦い.txt', encoding='utf-8').read().splitlines()

# Voice ranges (from P4 source analysis)
# si: 14659-14688 (30 voices)
# ha: 2165-2188 (24 voices)  
# s: 11284-11310 (27 voices)
# l: 5938-5946, 5947-5948 (? voices)

voice_map = {}

# Manual mappings from PS2 source
si_idx = 14659
ha_idx = 2165
s_idx = 11284
l_idx = 5938

for raw in lines[885:1210]:  # scenes 163-168
    if 'SCENE' in raw:
        continue
    if '[voice' in raw and 'シエスタ' in raw:
        m = re.search(r'\[(\d+)\]', raw.replace('[voice ', '['))
        if m:
            vid = m.group(1)
            key = f'ch3.2_si_{str(si_idx).zfill(3)}'
            voice_map[vid] = key
            si_idx += 1
    elif '[voice' in raw and 'ハルナ' in raw:
        m = re.search(r'\[(\d+)\]', raw.replace('[voice ', '['))
        if m:
            vid = m.group(1)
            key = f'ch3.2_ha_{str(ha_idx).zfill(3)}'
            voice_map[vid] = key
            ha_idx += 1
    elif '[voice' in raw and 'サイト' in raw:
        m = re.search(r'\[(\d+)\]', raw.replace('[voice ', '['))
        if m:
            vid = m.group(1)
            key = f'ch3.2_s_{str(s_idx).zfill(3)}'
            voice_map[vid] = key
            s_idx += 1
    elif '[voice' in raw and 'ルイズ' in raw:
        m = re.search(r'\[(\d+)\]', raw.replace('[voice ', '['))
        if m:
            vid = m.group(1)
            key = f'ch3.2_l_{str(l_idx).zfill(3)}'
            voice_map[vid] = key
            l_idx += 1

print(f'Found {len(voice_map)} P4 voice mappings')

# Load manifest and update
vm_lines = io.open('references/voice_id_map.csv', encoding='utf-8').read().splitlines()
existing = set()
for ln in vm_lines:
    if ',' in ln and not ln.startswith('#'):
        existing.add(ln.split(',')[1].strip())

added = 0
for vid, key in voice_map.items():
    entry = f'{key},{vid}'
    if entry not in existing:
        vm_lines.append(entry)
        added += 1

print(f'Added {added} new entries')
io.open('references/voice_id_map.csv', 'w', encoding='utf-8').write('\n'.join(vm_lines) + '\n')