# -*- coding: utf-8 -*-
"""View source scene 0260 head: lines 2012-2092."""
import glob
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

f = glob.glob('ps2_source/chapters/chapter_05_*.txt')[0]
L = open(f, encoding='utf-8', errors='replace').read().splitlines()
for i in range(2011, 2092):
    print('  %d %r' % (i + 1, L[i]))
