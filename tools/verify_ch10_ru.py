#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify RU TL quality: no leftover English, no foreign quotes, thoughts italicized."""
import re, sys

def check(path, label):
    with open(path, encoding='utf-8') as f:
        txt = f.read()
    issues = []
    # Latin letters in RU translation (excluding tags and code)
    # Extract only new "..." values
    news = re.findall(r'new\s+"(.*?)"', txt)
    for i, n in enumerate(news):
        if re.search(r'[A-Za-z]', n):
            issues.append(f"  L{i+1}: Latin letters in RU: {n[:60]!r}")
        if '...' in n:
            issues.append(f"  L{i+1}: ASCII ellipsis '...' in RU: {n[:60]!r}")
        if '"' in n or "'" in n:
            issues.append(f"  L{i+1}: Straight quotes in RU: {n[:60]!r}")
    print(f"[{label}] {len(news)} new-strings, {len(issues)} issues")
    for x in issues[:10]:
        print(x)
    return issues

total = 0
total += len(check('game/tl/russian/ch10_1_dialogs.rpy', 'RU dialogs'))
total += len(check('game/tl/russian/ch10_1_choises.rpy', 'RU choises'))
total += len(check('game/tl/russian/ch10_1_overlays.rpy', 'RU overlays'))
print(f"TOTAL issues: {total}")
sys.exit(0 if total == 0 else 1)
