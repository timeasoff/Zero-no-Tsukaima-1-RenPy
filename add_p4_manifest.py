import io, re

# Extract voice data from P4 source
ja_txt = io.open('scratch_p4_data.txt', encoding='utf-8').read().splitlines()

# Load current manifest
entries = []
for ln in io.open('references/voice_id_map.csv', encoding='utf-8').read().splitlines():
    if ln.startswith('#') or not ln.strip():
        entries.append(ln)
    elif ',' in ln:
        entries.append(ln)

# Count existing ch3.2 keys
ch32_count = {}
for ln in entries:
    if ',' in ln and not ln.startswith('#'):
        k = ln.split(',')[0].strip()
        if k.startswith('ch3.2_'):
            sp = k[:7]  # ch3.2_si, ch3.2_ha, ch3.2_s, ch3.2_l
            if sp not in ch32_count:
                ch32_count[sp] = 0
            ch32_count[sp] += 1

print('Existing ch3.2 counts:', ch32_count)

# Find next available numbers based on scratch data
next_si = 14659  # from P4 data
next_ha = 2165
next_s = 11284
next_l = 5940

# Generate mappings from scratch_p4_data
added = 0
for raw in ja_txt:
    if raw.startswith('total='): continue
    parts = raw.split('|')
    if len(parts) < 4: continue
    
    key_vid = parts[0]
    if not key_vid.startswith('ch3.2_'): continue
    
    # Check if already in manifest
    vid = parts[1]
    found = False
    for ln in entries:
        if ln.startswith(f'{key_vid},'):
            found = True
            break
    
    if not found:
        entries.append(f'{key_vid},{vid}')
        added += 1

print(f'Added {added} entries')

# Write back
io.open('references/voice_id_map.csv', 'w', encoding='utf-8').write('\n'.join(entries) + '\n')
print('Updated voice_id_map.csv')