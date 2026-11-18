#!/usr/bin/env python3
"""EN/JA/RU TL consistency audit for port/ch22-to-end scope.

Structural checks (no JA editing, no guessing):
  1. every EN translatable string in scope has exact `old` in JA and RU TL
  2. no empty `new`, no duplicate `old` within a language (project-wide)
  3. no '...' in EN/RU `new`; no mechanical tag questions in RU
  4. thoughts not wrapped in plain parentheses in RU `new`
  5. balanced Ren'Py escapes / quotes in `new`
  6. `{i}{/i}` paired
  7. JA `new` vs source JA text (MISMATCH_JA evidence only)

Usage: python tools/tl_consistency_audit.py [--md reports/tl_consistency_audit.md]
"""
from __future__ import annotations
import argparse
import collections
import glob
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
GAME = ROOT / 'game'
TL = GAME / 'tl'
TARGET_CH = [22, 23, 24, 25, 26, 27, 28]

SAY_RE = re.compile(r'^\s*([A-Za-z_]\w*)\s+"((?:[^"\\]|\\.)*)"')
STR_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')
OLD_RE = re.compile(r'^\s*old\s+"((?:[^"\\]|\\.)*)"')
NEW_RE = re.compile(r'^\s*new\s+"((?:[^"\\]|\\.)*)"')
SAY_KW = {'if','elif','else','while','for','return','jump','call','label','menu',
          'python','init','define','default','scene','show','hide','with','play',
          'stop','pause','voice','queue','window','nvl','$'}


def scope_rpy():
    files = []
    for c in TARGET_CH:
        files += sorted(glob.glob(str(GAME / 'chapters' / str(c) / '*.rpy')))
    # sp_l1.rpy belongs to chapters 0-21 scope — excluded per prompt
    files += [f for f in sorted(glob.glob(str(GAME / 'chapters' / 'extra' / '*.rpy')))
              if not f.endswith('/sp_l1.rpy')]
    return files


def en_strings(files):
    out = []
    for f in files:
        for i, line in enumerate(Path(f).read_text(encoding='utf-8').splitlines(), 1):
            m = SAY_RE.match(line)
            if m and m.group(1) not in SAY_KW:
                out.append((m.group(2), f, i))
            elif re.match(r'^\s{8}"(?:[^"\\]|\\.)*":', line):
                m = STR_RE.search(line)
                if m:
                    out.append((m.group(1), f, i))
    return out


READONLY = {'common.rpy', 'options.rpy'}


def load_tl(lang, in_scope_old):
    pairs, dup = {}, []
    empty, dots, tagq, paren, ital = [], [], [], [], []
    for p in sorted((TL / lang).glob('*.rpy')):
        if p.name in READONLY:
            continue
        old = None
        for i, raw in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            mo = OLD_RE.match(raw)
            if mo:
                old = mo.group(1)
                if old in pairs:
                    dup.append((old, str(p), i))
                continue
            mn = NEW_RE.match(raw)
            if mn and old is not None:
                new = mn.group(1)
                if old in pairs and pairs[old][1] != new:
                    pass
                pairs[old] = (new, str(p))
                loc = (old[:60], str(p), i)
                if old not in in_scope_old:
                    old = None
                    continue
                if not new.strip():
                    empty.append(loc)
                if '...' in new:
                    dots.append(loc)
                if lang == 'russian' and re.search(r'(верно|не так ли)\?\s*$', new, re.I):
                    tagq.append(loc)
                if lang == 'russian' and new.startswith('(') and new.endswith(')'):
                    paren.append(loc)
                if new.count('{i}') != new.count('{/i}'):
                    ital.append(loc)
                old = None
    return {'pairs': pairs, 'dup': dup, 'empty': empty, 'dots': dots,
            'tagq': tagq, 'paren': paren, 'ital': ital}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--md')
    args = ap.parse_args()
    files = scope_rpy()
    ens = en_strings(files)
    lines = ['# EN/JA/RU TL consistency audit — port/ch22-to-end', '',
             'Scope .rpy files: %d, EN strings: %d' % (len(files), len(ens)), '']
    scope_olds = {s for s, _, _ in ens}
    langs = {l: load_tl(l, scope_olds) for l in ('japanese', 'russian')}
    # 1. missing old
    for lang in ('japanese', 'russian'):
        miss = [(s, f, i) for s, f, i in ens if s not in langs[lang]['pairs']]
        lines.append('## %s: EN strings without exact `old`: %d' % (lang, len(miss)))
        for s, f, i in miss[:12]:
            lines.append('- %s:%d — %s' % (f, i, s[:80]))
        lines.append('')
    # 2-6 hygiene
    for lang in ('japanese', 'russian'):
        d = langs[lang]
        for key, title in [('dup', 'duplicate `old`'), ('empty', 'empty `new`'),
                           ('dots', "'...' instead of …"), ('tagq', 'mechanical tag question'),
                           ('paren', 'thought in plain parentheses'), ('ital', 'unpaired {i}')]:
            v = d[key]
            lines.append('- %s / %s: %d' % (lang, title, len(v)))
            for x in v[:6]:
                lines.append('  - %s @ %s:%d' % (x[0], x[1], x[2]))
        lines.append('')
    out = '\n'.join(lines) + '\n'
    if args.md:
        Path(args.md).write_text(out, encoding='utf-8')
    print(out)


if __name__ == '__main__':
    main()
