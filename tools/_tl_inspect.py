# -*- coding: utf-8 -*-
"""Inspect structure of tl files: translate block headers and indentation."""
import io, sys, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

FILES = [
    'game/tl/russian/dialogs.rpy', 'game/tl/japanese/dialogs.rpy',
    'game/tl/russian/thoughs.rpy', 'game/tl/japanese/thoughs.rpy',
    'game/tl/russian/choises.rpy', 'game/tl/japanese/choises.rpy',
]
for p in FILES:
    L = open(p, encoding='utf-8').read().splitlines()
    heads = [(i + 1, l) for i, l in enumerate(L) if l.startswith('translate ')]
    print('== %s  lines=%d  blocks=%d' % (p, len(L), len(heads)))
    for i, l in heads[:3]:
        print('   first  %d: %s' % (i, l))
    for i, l in heads[-3:]:
        print('   last   %d: %s' % (i, l))
    # indentation stats of 'old' lines in last block
    if heads:
        start = heads[-1][0]
        olds = [(i + start, l) for i, l in enumerate(L[start:]) if l.strip().startswith('old ')]
        indents = sorted(set(len(l) - len(l.lstrip()) for _, l in olds))
        print('   last-block old count=%d indents=%s tail:' % (len(olds), indents))
        for l in L[-4:]:
            print('      |%s' % l)
