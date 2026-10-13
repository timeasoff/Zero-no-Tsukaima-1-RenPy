import io
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

want = {302, 304, 306, 308, 337, 341, 390, 394, 396,
        429, 489, 491, 493, 495, 524, 528, 530, 973, 975, 979}

path = 'references/sprite_id_map.csv'
lines = io.open(path, encoding='utf-8').read().splitlines()
print(lines[0])
for ln in lines[1:]:
    if not ln.strip() or ln.startswith('#'):
        continue
    parts = ln.split(',')
    try:
        iid = int(parts[0])
    except ValueError:
        continue
    if iid in want:
        print(ln)
