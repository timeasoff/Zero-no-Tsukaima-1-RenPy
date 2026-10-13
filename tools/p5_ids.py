# -*- coding: utf-8 -*-
# Позы спрайтов и фоны для P5 (сцены 169-178, 1322-1341).
import io
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

want = {91, 32, 343, 588, 676, 678, 682, 684, 709, 711,
        852, 856, 858, 885, 889, 929, 931, 935, 555, 559, 566}

for path in ('references/sprite_id_map.csv', 'references/image_id_map.csv'):
    print('==', path)
    for ln in io.open(path, encoding='utf-8').read().splitlines()[1:]:
        if not ln.strip() or ln.startswith('#'):
            continue
        parts = ln.split(',')
        try:
            iid = int(parts[0])
        except ValueError:
            continue
        if iid in want:
            print(ln)
