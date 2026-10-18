# -*- coding: utf-8 -*-
"""View source lines 1660-1690 and script lines 78-120 for comparison."""
import glob
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

f = glob.glob('ps2_source/chapters/chapter_05_*.txt')[0]
L = open(f, encoding='utf-8', errors='replace').read().splitlines()
print('== SOURCE 1660-1690 ==')
for i in range(1659, 1690):
    print('  %d %r' % (i + 1, L[i]))

SL = open('game/chapters/4/script-ch4_5.rpy', encoding='utf-8').read().splitlines()
print('== SCRIPT 78-122 ==')
for i in range(77, 122):
    print('  %d %s' % (i + 1, SL[i]))
