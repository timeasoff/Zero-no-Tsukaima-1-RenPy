# -*- coding: utf-8 -*-
"""View source scenes 0257-0259 (1922-2011) and script branch labels."""
import glob
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

f = glob.glob('ps2_source/chapters/chapter_05_*.txt')[0]
L = open(f, encoding='utf-8', errors='replace').read().splitlines()
for i in range(1921, 2011):
    print('  %d %r' % (i + 1, L[i]))
