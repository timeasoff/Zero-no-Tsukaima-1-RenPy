# -*- coding: utf-8 -*-
# Ищет nextScene/next в сырых сценах веток 1326/1331/1336/1341 и 183.
import io
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

for sid in (1326, 1331, 1336, 1341, 183, 182):
    path = 'ps2_source/scripts/SCENE_%04d.txt' % sid
    try:
        raw = io.open(path, encoding='cp932', errors='replace').read()
    except IOError:
        print(sid, 'FILE MISSING')
        continue
    hits = []
    for i, l in enumerate(raw.splitlines()):
        low = l.lower()
        if 'scene' in low or 'next' in low:
            hits.append((i + 1, l.strip()))
    print('=== scene', sid, '===')
    for i, l in hits[:12]:
        print(' ', i, ''.join(ch if ord(ch) < 128 else '?' for ch in l))
    if not hits:
        print('  (no next/scene refs)')
