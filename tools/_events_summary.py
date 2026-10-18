# -*- coding: utf-8 -*-
"""Summarize scene 256-260 events: source BGM/BG/CG vs script fx calls."""
import glob
import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

f = glob.glob('ps2_source/chapters/chapter_05_*.txt')[0]
L = open(f, encoding='utf-8', errors='replace').read().splitlines()
s256 = next(i for i, l in enumerate(L) if re.match(r'^-+\s*SCENE\s*0256', l.strip()))
s261 = next(i for i, l in enumerate(L) if re.match(r'^-+\s*SCENE\s*0261', l.strip()))

print('== SOURCE events (BGM/BG/EVENT_CG/TRANS) ==')
for i in range(s256, s261):
    ln = L[i]
    if re.search(r'\[(BGM|BG |EVENT_CG|VIBRATE)', ln):
        print('  %d %s' % (i + 1, ln.strip()))

print()
print('== SCRIPT fx/music lines ==')
SL = open('game/chapters/4/script-ch4_5.rpy', encoding='utf-8').read().splitlines()
for i, ln in enumerate(SL, 1):
    st = ln.strip()
    if (st.startswith('$ fade_fx') or st.startswith('stop music') or st.startswith('$ renpy.music')
            or st.startswith('play music') or st.startswith('call overlay_screen')
            or st.startswith('menu ') or st.startswith('jump ') or st.startswith('label ')):
        print('  %d %s' % (i, st))

print()
print('== SOURCE choices / sympathy ==')
for i in range(s256, s261):
    ln = L[i]
    if '【選択肢】' in ln or '【好感度】' in ln or ln.strip().startswith('→'):
        print('  %d %s' % (i + 1, ln.strip()))

print()
print('== SCRIPT sympathy ==')
for i, ln in enumerate(SL, 1):
    if 'update_sympathy' in ln:
        print('  %d %s' % (i, ln.strip()))
