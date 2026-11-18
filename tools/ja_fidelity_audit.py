#!/usr/bin/env python3
"""JA `new` fidelity audit: compare tl/japanese `new` strings to PS2 source JA.

Evidence only. Never edits JA.  MISMATCH_JA candidates are flagged for the
classification/disposition cycle.
"""
from __future__ import annotations
import argparse
import glob
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
TLJ = ROOT / 'game' / 'tl' / 'japanese'
OLD_RE = re.compile(r'^\s*old\s+"((?:[^"\\]|\\.)*)"')
NEW_RE = re.compile(r'^\s*new\s+"((?:[^"\\]|\\.)*)"')

PARSE = []
for c in range(22, 29):
    PARSE += glob.glob(str(ROOT / 'reports' / ('ch%d' % c) / 'parse_*.json'))
PARSE += [str(ROOT / 'reports' / 'extra' / ('parse_%d.json' % n)) for n in (90, 91)]


def norm(s):
    s = s.replace('\\n', '').replace('\n', '').replace(' ', '').replace('　', '')
    return s.strip('。')


def source_ja():
    out = set()
    for p in PARSE:
        if not Path(p).exists():
            continue
        d = json.load(open(p, encoding='utf-8'))
        if isinstance(d, dict):
            scenes = d.get('scenes', [])
        else:
            scenes = [{'items': d}]
        for sc in scenes:
            for it in sc.get('items', []):
                if it.get('kind') == 'dlg' and it.get('ja'):
                    out.add(norm(it['ja']))
                elif it.get('kind') == 'choice':
                    if it.get('text'):
                        out.add(norm(it['text']))
                    for o in it.get('options', []):
                        if o.get('text'):
                            out.add(norm(o['text']))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--md')
    args = ap.parse_args()
    src = source_ja()
    patterns = []
    for c in range(22, 29):
        patterns += glob.glob(str(TLJ / ('ch%d_*' % c)))
    patterns += glob.glob(str(TLJ / 'sp9*'))
    lines = ['# JA new fidelity audit', '', 'source JA lines: %d' % len(src), '']
    miss = []
    total = 0
    for p in sorted(set(patterns)):
        old = None
        for i, raw in enumerate(Path(p).read_text(encoding='utf-8').splitlines(), 1):
            mo = OLD_RE.match(raw)
            if mo:
                old = mo.group(1)
                continue
            mn = NEW_RE.match(raw)
            if mn and old is not None:
                ja = mn.group(1)
                total += 1
                core = re.sub(r'^[^：]{1,10}：', '', ja)
                if norm(core) and norm(core) not in src and norm(ja) not in src:
                    miss.append((core[:70], Path(p).name, i))
                old = None
    lines.append('JA new strings checked: %d, not found verbatim in source: %d' % (total, len(miss)))
    for m in miss[:25]:
        lines.append('- %s @ %s:%d' % m)
    out = '\n'.join(lines) + '\n'
    if args.md:
        Path(args.md).write_text(out, encoding='utf-8')
    print(out)


if __name__ == '__main__':
    main()
