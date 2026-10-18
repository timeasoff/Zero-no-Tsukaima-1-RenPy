# -*- coding: utf-8 -*-
"""Audit non-portable calls (movie/coffee/item/battle/points) in scenes 256-260 and count fx."""
import glob
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

f = glob.glob('ps2_source/chapters/chapter_05_*.txt')[0]
L = open(f, encoding='utf-8', errors='replace').read().splitlines()

calls = {}
for i in range(1622, 2110):
    for m in re.finditer(r'(movie|coffee|item|battle\w*|points|waitAction|waitSEStop|waitLoad|sync|create|setZoom|setRotate|setAffineOrigin|swapLayers|screenShow|msgon|msgoff|beginSkip|endSkip)\s*\(', L[i]):
        calls.setdefault(m.group(1), []).append(i + 1)
print('non-portable calls in 256-260:', calls if calls else 'NONE')

SL = open('game/chapters/4/script-ch4_5.rpy', encoding='utf-8').read()
ids = re.findall(r'fade_fx\("id\((\d+)\)"', SL)
import collections
print('fade_fx id counts:', dict(collections.Counter(ids)))
print('shake_fx:', SL.count('shake_fx()'))
print('play music:', re.findall(r'play music (\w+)', SL))
print('update_sympathy:', len(re.findall(r'update_sympathy\(', SL)))
print('voice lines:', len(re.findall(r'^    voice "', SL, re.M)))
print('th lines:', len(re.findall(r'^    th "', SL, re.M)))
