#!/usr/bin/env python3
"""Ren'Py flow audit for port/ch22-to-end scope.

Checks label graph, reachability, cycles, part chain, menu structure,
overlay-K uniqueness, and entry/exit consistency.
"""
from __future__ import annotations
import argparse
import collections
import glob
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
GAME = ROOT / 'game'
CHAPTERS = GAME / 'chapters'
TARGET = [22, 23, 24, 25, 26, 27, 28]
LABEL_RE = re.compile(r'^\s*label\s+([A-Za-z_]\w*)', re.M)
JUMP_RE = re.compile(r'^\s*jump\s+([^\s#]+)', re.M)
CALL_RE = re.compile(r'^\s*call\s+([^\s(]+)', re.M)
MENU_RE = re.compile(r'^\s*menu\s*:', re.M)
OVERLAY_RE = re.compile(r'from\s+_call_overlay_screen_(\d+)')
RETURN_RE = re.compile(r'^\s*return\s*$', re.M)


def collect(files):
    labels, jumps, calls, menus, overlays, returns = {}, [], [], 0, [], 0
    for f in files:
        text = Path(f).read_text(encoding='utf-8')
        for i, line in enumerate(text.splitlines(), 1):
            m = LABEL_RE.match(line)
            if m:
                labels[m.group(1)] = (str(f), i)
            m = JUMP_RE.match(line)
            if m:
                jumps.append((m.group(1), str(f), i))
            m = CALL_RE.match(line)
            if m:
                calls.append((m.group(1), str(f), i))
            if MENU_RE.match(line):
                menus += 1
            m = OVERLAY_RE.search(line)
            if m:
                overlays.append((m.group(1), str(f), i))
            if RETURN_RE.match(line):
                returns += 1
    return {'labels': labels, 'jumps': jumps, 'calls': calls, 'menus': menus,
            'overlays': overlays, 'returns': returns}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--md')
    args = ap.parse_args()
    files = []
    for c in TARGET:
        files += sorted(glob.glob(str(CHAPTERS / str(c) / '*.rpy')))
    files += sorted(glob.glob(str(CHAPTERS / 'extra' / '*.rpy')))
    d = collect(files)
    lines = ['# Ren\'Py flow audit — port/ch22-to-end', '',
             'Files: %d, labels: %d, jumps: %d, calls: %d, menus: %d, returns: %d' % (
                 len(files), len(d['labels']), len(d['jumps']), len(d['calls']),
                 d['menus'], d['returns']), '']

    # broken targets
    all_labels = set(d['labels'])
    # include labels from entire game tree (calls may target screens/features)
    project_files = glob.glob(str(GAME / '**' / '*.rpy'), recursive=True)
    project_labels = set(collect(project_files)['labels'])
    broken = [(t, f, i) for t, f, i in d['jumps'] + d['calls']
              if t not in project_labels and not t.startswith('expression')]
    lines.append('## Broken jump/call targets: %d' % len(broken))
    for b in broken[:10]:
        lines.append('- %s @ %s:%d' % b)

    # reachability from entry labels of target chapters
    entries = ['ch22', 'ch23', 'ch24', 'ch25', 'ch26', 'ch27', 'ch28',
               'sp90_scene_1533', 'sp91_scene_1697', 'sp_d1']
    graph = collections.defaultdict(list)
    # fall-through edges: a label flows to the next label in the same file unless
    # its block ends with jump/return
    by_file = collections.defaultdict(list)
    for lab, (f, i) in d['labels'].items():
        by_file[f].append((i, lab))
    terminators = set()
    for t, f, i in d['jumps']:
        terminators.add((f, i))
    for f, labs in by_file.items():
        labs.sort()
        for k in range(len(labs) - 1):
            i, lab = labs[k]
            # if any jump/return line exists between this label and the next
            text_lines = Path(f).read_text(encoding='utf-8').splitlines()
            between = text_lines[i:labs[k + 1][0] - 1]
            ends = any(re.match(r'^\s*(jump|return)\b', ln) for ln in between)
            if not ends:
                graph[lab].append(labs[k + 1][1])
    # graph edges: every jump is an edge, except top-level jumps AFTER the first
    # top-level terminator in the same label block (dead code). Menu jumps are
    # indented deeper and are always real edges.
    seen_top_term = set()
    for t, f, i in d['jumps'] + d['calls']:
        src = None
        for lab, (lf, li) in d['labels'].items():
            if lf == f and li <= i and (src is None or li > d['labels'][src][1]):
                src = lab
        if src is None:
            continue
        line = Path(f).read_text(encoding='utf-8').splitlines()[i - 1]
        top = bool(re.match(r'^    (?:jump|call|return)\b', line))
        if top:
            if src in seen_top_term:
                continue
            seen_top_term.add(src)
        graph[src].append(t)
    seen, stack = set(), [e for e in entries if e in all_labels]
    while stack:
        n = stack.pop()
        if n in seen:
            continue
        seen.add(n)
        stack += [t for t in graph.get(n, []) if t in all_labels]
    unreachable = sorted(all_labels - seen)
    lines.append('')
    lines.append('## Unreachable labels in scope from chapter entry points: %d' % len(unreachable))
    lines.append(', '.join(unreachable[:25]) or '(none)')

    # cycles (simple DFS)
    color, cycles = {}, []
    def dfs(n, path):
        color[n] = 1
        for t in graph.get(n, []):
            if t not in all_labels:
                continue
            if color.get(t) == 1:
                cycles.append(path[path.index(t):] + [t])
            elif color.get(t, 0) == 0:
                dfs(t, path + [t])
        color[n] = 2
    for e in entries:
        if e in all_labels and color.get(e, 0) == 0:
            dfs(e, [e])
    lines.append('')
    lines.append('## Cycles reachable from entries: %d' % len(cycles))
    for c in cycles[:5]:
        lines.append('- ' + ' -> '.join(c))

    # overlay K uniqueness
    ks = collections.Counter(k for k, _, _ in d['overlays'])
    dups = [k for k, v in ks.items() if v > 1]
    lines.append('')
    lines.append('## Overlay K in scope: %s (duplicates: %s)' % (
        sorted(ks, key=int) or '(none)', dups or '(none)'))

    # part chain
    lines.append('')
    lines.append('## Mainline chain')
    for c in TARGET:
        fs = sorted(glob.glob(str(CHAPTERS / str(c) / '*.rpy')))
        ch = collect(fs)
        last = [t for t, _, _ in ch['jumps']]
        lines.append('- ch%d: files=%d labels=%d tail_jumps=%s' % (
            c, len(fs), len(ch['labels']), last[-3:]))

    out = '\n'.join(lines) + '\n'
    if args.md:
        Path(args.md).write_text(out, encoding='utf-8')
    print(out)


if __name__ == '__main__':
    main()
