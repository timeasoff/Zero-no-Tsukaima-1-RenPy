# -*- coding: utf-8 -*-
"""Dump script dialogue lines (speaker/text/voice) for alignment check."""
import re, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

path = 'game/chapters/4/script-ch4_5.rpy'
lines = open(path, encoding='utf-8').read().splitlines()

SPEAKERS = {'s', 'l', 'h', 'ha', 'si', 'd'}
i = 0
n_voiced = 0
n_unvoiced = 0
for idx, ln in enumerate(lines, 1):
    st = ln.strip()
    m = re.match(r'^([a-z]+)\s+"(.*)"$', st)
    if m and m.group(1) in SPEAKERS:
        # look back up to 3 lines for a voice call
        v = None
        for back in range(1, 4):
            if idx - back - 1 < 0:
                break
            vm = re.search(r'voice "ch4\.5_([a-z]+_\d+)"', lines[idx - back - 1])
            if vm:
                v = vm.group(1)
                break
        text = m.group(2)[:70]
        if v:
            n_voiced += 1
            mark = 'V ' + v
        else:
            n_unvoiced += 1
            mark = 'NO-VOICE'
        print('%4d [%s] %-55s %s' % (idx, m.group(1), text, mark))
print('voiced=%d unvoiced=%d' % (n_voiced, n_unvoiced))
