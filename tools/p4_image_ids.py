import io
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

want = {10, 13, 14, 115, 116, 302, 304, 306, 308, 337, 341, 390, 394, 396,
        429, 489, 491, 493, 495, 524, 528, 530, 973, 975, 979}

for ln in io.open('references/image_id_map.csv', encoding='utf-8').read().splitlines()[1:]:
    if not ln.strip() or ln.startswith('#'):
        continue
    parts = ln.split(',')
    try:
        iid = int(parts[0])
    except ValueError:
        continue
    if iid in want:
        print(ln)
