# -*- coding: utf-8 -*-
"""Verify script↔source mapping around BG+36 transitions: source 1786-1800, 1835-1852, 2090-2110."""
import glob
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

f = glob.glob('ps2_source/chapters/chapter_05_*.txt')[0]
L = open(f, encoding='utf-8', errors='replace').read().splitlines()
for a, b in ((1786, 1800), (1835, 1852), (2090, 2110)):
    print('== SOURCE %d-%d ==' % (a, b))
    for i in range(a - 1, b):
        print('  %d %r' % (i + 1, L[i]))
    print()
