import io

entries = []
for ln in io.open('references/voice_id_map.csv', encoding='utf-8').read().splitlines():
    if ln.startswith('#') or not ln.strip() or ',' not in ln:
        continue
    k, v = ln.split(',', 1)
    k, v = k.strip(), v.strip()
    if k.startswith('ch3.2_'):
        entries.append((int(v), k))

entries.sort()
print('total ch3.2 entries:', len(entries))
for vid, k in entries:
    print(vid, k)
