#!/usr/bin/env python3
"""Merge out_<ch>_<batch>.json translation files into trans_<ch>.json."""
import glob
import json
import sys


def main():
    merged = {}
    collisions = []
    for p in sorted(glob.glob('reports/extra/trans/out_*.json')):
        try:
            data = json.load(open(p, encoding='utf-8'))
        except Exception as e:
            print('SKIP bad', p, e)
            continue
        for k, v in data.items():
            if k in merged and merged[k] != v:
                collisions.append((k, p))
            merged[k] = v
    for ch in ['90', '91']:
        out = 'reports/extra/trans_%s.json' % ch
        with open(out, 'w', encoding='utf-8') as f:
            json.dump(merged, f, ensure_ascii=False, indent=1)
        print('wrote', out, len(merged))
    if collisions:
        print('COLLISIONS', len(collisions), collisions[:5])


if __name__ == '__main__':
    main()
