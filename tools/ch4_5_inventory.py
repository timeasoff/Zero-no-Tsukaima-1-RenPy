# -*- coding: utf-8 -*-
"""Inventory every translatable string in script-ch4_5.rpy."""
import re, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

PATH = 'game/chapters/4/script-ch4_5.rpy'
lines = open(PATH, encoding='utf-8').read().splitlines()

DIALOG = re.compile(r'^(s|l|h|ha|si|d|n)\s+"(.*)"$')
TH = re.compile(r'^th\s+"(.*)"$')
MENU = re.compile(r'^"(.+)":\s*(#.*)?$')
OVERLAY = re.compile(r'call overlay_screen\(')

buckets = {'dialog': [], 'thought': [], 'choice': [], 'overlay': [], 'other': []}
for i, ln in enumerate(lines, 1):
    st = ln.strip()
    m = DIALOG.match(st)
    if m:
        buckets['dialog'].append((i, m.group(1), m.group(2)))
        continue
    m = TH.match(st)
    if m:
        buckets['thought'].append((i, '', m.group(1)))
        continue
    m = MENU.match(st)
    if m:
        buckets['choice'].append((i, '', m.group(1)))
        continue
    if OVERLAY.search(st):
        buckets['overlay'].append((i, '', st))
        continue
    # any other line with a quoted string that isn't code-ish
    if re.match(r'^[a-z_]+ "', st) and not st.startswith('voice '):
        buckets['other'].append((i, '', st))

for k in buckets:
    print('%s: %d' % (k, len(buckets[k])))
for i, spk, t in buckets['choice']:
    print('  choice %d: %s' % (i, t[:80]))
for i, _, t in buckets['overlay']:
    print('  overlay %d: %s' % (i, t[:120]))
for i, _, t in buckets['other']:
    print('  other %d: %s' % (i, t[:120]))
for i, _, t in buckets['thought']:
    print('  thought %d: %s' % (i, t[:80]))
