#!/usr/bin/env python3
"""Sync reports/extra/trans_*.json and reports/ch2x parse-derived translations
after semantic fixes so regeneration reproduces the corrected text."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, 'tools')
from fix_semantic_findings import SP90, SP91_RU, CH27_RU

ROOT = Path(__file__).parent.parent


def ja_by_tag(path):
    out, old = {}, None
    for l in open(path, encoding='utf-8'):
        m = re.match(r'^\s*old "(.*)"', l.rstrip('\n'))
        if m:
            old = m.group(1)
            continue
        m = re.match(r'^\s*new "(.*)"', l.rstrip('\n'))
        if m and old is not None:
            t = re.search(r'\{#([^}]+)\}', old)
            if t:
                out[t.group(1)] = m.group(1)
            old = None
    return out


def find_keys(parse_path, ja):
    d = json.load(open(parse_path, encoding='utf-8'))
    scenes = d.get('scenes', []) if isinstance(d, dict) else []
    if not scenes:
        # flat list
        items, cur = [], None
        for x in d:
            if x.get('kind') == 'scene':
                cur = x['no']
            elif x.get('kind') == 'dlg':
                items.append((cur, x))
        scenes = [{'no': cur, 'items': items}] if False else scenes
    keys = []
    for sc in scenes:
        for i, it in enumerate(sc.get('items', [])):
            if it.get('kind') == 'dlg' and it.get('ja') == ja:
                keys.append('s%d_%d' % (sc['no'], i))
                if it.get('voice') is not None:
                    keys.append('d%d' % it['voice'])
    return keys


def main():
    # extra trans_90
    ja = ja_by_tag(ROOT / 'game/tl/japanese/sp90_dialogs.rpy')
    p = ROOT / 'reports/extra/trans_90.json'
    d = json.load(open(p, encoding='utf-8'))
    n = 0
    for tag, (en, ru) in SP90.items():
        j = ja.get(tag)
        if not j:
            print('no JA for', tag)
            continue
        for k in find_keys(ROOT / 'reports/extra/parse_90.json', j):
            if k in d:
                d[k] = [en.split('{#')[0], ru]
                n += 1
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('trans_90 updated keys', n)
    # extra trans_91
    ja = ja_by_tag(ROOT / 'game/tl/japanese/sp91_dialogs.rpy')
    p = ROOT / 'reports/extra/trans_91.json'
    d = json.load(open(p, encoding='utf-8'))
    n = 0
    for tag, ru in SP91_RU.items():
        j = ja.get(tag)
        if not j:
            print('no JA for', tag)
            continue
        # keep existing EN, replace RU
        for k in find_keys(ROOT / 'reports/extra/parse_91.json', j):
            if k in d:
                d[k] = [d[k][0], ru]
                n += 1
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('trans_91 updated keys', n)


if __name__ == '__main__':
    main()
