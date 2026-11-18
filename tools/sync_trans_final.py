#!/usr/bin/env python3
"""Sync reports/extra/trans_{90,91}.json with the FINAL TL state.

After prompts 09/10/11 many EN/RU strings were edited directly in TL.
This script writes those final values back into the trans JSON so regeneration
reproduces the committed game files.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent


def tl_pairs(path):
    out, old = {}, None
    for line in (ROOT / path).read_text(encoding='utf-8').splitlines():
        m = re.match(r'^\s*old "(.*)"', line)
        if m:
            old = m.group(1)
            continue
        m = re.match(r'^\s*new "(.*)"', line)
        if m and old is not None:
            t = re.search(r'\{#([^}]+)\}', old)
            if t:
                out[t.group(1)] = (old.split('{#')[0], m.group(1))
            old = None
    return out


def voice_by_key(parse_path):
    d = json.load(open(ROOT / parse_path, encoding='utf-8'))
    out = {}
    for sc in d['scenes']:
        for i, it in enumerate(sc['items']):
            if it['kind'] == 'dlg' and it.get('voice') is not None:
                out['s%d_%d' % (sc['no'], i)] = 'd%d' % it['voice']
    return out


def main():
    for ch in (90, 91):
        ja = tl_pairs('game/tl/japanese/sp%d_dialogs.rpy' % ch)
        ru = tl_pairs('game/tl/russian/sp%d_dialogs.rpy' % ch)
        ja_c = tl_pairs('game/tl/japanese/sp%d_choises.rpy' % ch)
        ru_c = tl_pairs('game/tl/russian/sp%d_choises.rpy' % ch)
        vmap = voice_by_key('reports/extra/parse_%d.json' % ch)
        p = ROOT / ('reports/extra/trans_%d.json' % ch)
        d = json.load(open(p, encoding='utf-8'))
        n = 0
        for tag, (en, ja_val) in ja.items():
            m = re.match(r'sp%d_s(\d+)_(\d+)' % ch, tag)
            if not m:
                continue
            key = 's%d_%d' % (int(m.group(1)), int(m.group(2)))
            ru_val = ru.get(tag, (None, ja_val))[1]
            d[key] = [en, ru_val]
            n += 1
            if key in vmap:
                d[vmap[key]] = [en, ru_val]
                n += 1
        for tag, (en, ja_val) in ja_c.items():
            m = re.match(r'sp%d_c_(\d+)_(\d+)' % ch, tag)
            if not m:
                continue
            key = 'c%d_%d' % (int(m.group(1)), int(m.group(2)))
            d[key] = [en, ru_c.get(tag, (None, ja_val))[1]]
            n += 1
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('trans_%d: written %d keys' % (ch, n))


if __name__ == '__main__':
    main()
