#!/usr/bin/env python3
"""Coverage audit: PS2 source (chapters + events_full) vs Ren'Py port.

Checks beyond omission_precheck (which only compares voiced IDs):
  A. voice-id multiset: source [voice N] vs port voices resolved via manifest
  B. scene coverage: every source SCENE N has a corresponding port label
  C. non-voiced dialogue: each source JA voiceless line present in tl/japanese new
  D. choices / next-scene / like / set / selectItem / dateItem / moveItem counts
  E. event (BG/CG/SPRITE/BGM/SE/VIBRATE/LAYER/TRANS/COFFEE) counts
  F. TL structural completeness: EN strings vs old/new in both TL dirs, no empty new,
     no duplicate old, correct language header

Usage:
  python tools/audit_coverage.py <chapter> <source_file> <port_glob> [--md OUT]
  (chapter like 22, 23, ... or extra; port_glob relative to repo root)
"""
from __future__ import annotations
import argparse
import collections
import glob
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
MANIFEST = ROOT / 'references' / 'voice_id_map.csv'
TL_J = ROOT / 'game' / 'tl' / 'japanese'
TL_R = ROOT / 'game' / 'tl' / 'russian'
SRC_CH = ROOT / 'ps2_source' / 'chapters'
SRC_EV = ROOT / 'ps2_source' / 'events_full'

SCENE_RE = re.compile(r'^----\s*SCENE\s+(\d+)\s*----', re.M)
VOICE_RE = re.compile(r'\[voice\s+(\d+)\]')
CHOICE_RE = re.compile(r'【選択肢】')
NEXT_RE = re.compile(r'→\s*next\s*scene\s+(\d+)')
LIKE_RE = re.compile(r'【好感度】')
SELECT_RE = re.compile(r'【選択】|selectItem|dateItem|moveItem|set\(|【移動】|【デート】')
SPEAKER_RE = re.compile(r'^([^：\[\]]{1,24})：')
EVENT_TYPES = ['BG', 'EVENT_CG', 'SPRITE', 'BGM', 'SE', 'VIBRATE', 'LAYER', 'TRANS', 'COFFEE']

EN_VOICE_RE = re.compile(r'^\s*voice\s+"([^"]+)"')
EN_LABEL_RE = re.compile(r'^label\s+(\S+)\s*:', re.M)
EN_MENU_RE = re.compile(r'^\s*menu\s*:', re.M)
EN_CHOICE_RE = re.compile(r'^\s{8}"(?:[^"\\]|\\.)*":', re.M)
EN_JUMP_RE = re.compile(r'^\s*jump\s+(\S+)')
EN_SAY_RE = re.compile(r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s+"((?:[^"\\]|\\.)*)"')
EN_STR_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')
SAY_KW = {'if','elif','else','while','for','return','jump','call','label','menu','python',
          'init','define','default','scene','show','hide','with','play','stop','pause','voice',
          'queue','window','nvl','$'}
TL_OLD_RE = re.compile(r'^\s*old\s+"((?:[^"\\]|\\.)*)"')
TL_NEW_RE = re.compile(r'^\s*new\s+"((?:[^"\\]|\\.)*)"')
MAN_RE = re.compile(r'^([^,\s#]+)\s*,\s*(\d+)')


def load_manifest():
    m = {}
    for raw in open(MANIFEST, encoding='utf-8-sig'):
        x = MAN_RE.match(raw.strip())
        if x:
            m[x.group(1)] = int(x.group(2))
    return m


def parse_source(path, scene_filter=None):
    text = open(path, encoding='utf-8').read()
    if scene_filter:
        # keep only the requested scene blocks
        blocks = re.split(r'(?=^----\s*SCENE\s+\d+\s*----)', text, flags=re.M)
        keep = [blocks[0]]  # header (extra scenes: line etc.)
        for b in blocks[1:]:
            ms = re.match(r'----\s*SCENE\s+(\d+)\s*----', b)
            if ms and int(ms.group(1)) in scene_filter:
                keep.append(b)
        text = ''.join(keep)
    scenes = [int(x) for x in SCENE_RE.findall(text)]
    voices = [int(x) for x in VOICE_RE.findall(text)]
    # voices per scene
    by_scene = collections.defaultdict(list)
    cur = None
    for line in text.splitlines():
        ms = re.match(r'^----\s*SCENE\s+(\d+)\s*----', line)
        if ms:
            cur = int(ms.group(1))
        mv = VOICE_RE.search(line)
        if mv and cur is not None:
            by_scene[cur].append(int(mv.group(1)))
    # voiceless dialogue lines (speaker：... without [voice]) and continuation
    voiceless = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith('[') or s.startswith('【') or s.startswith('→'):
            continue
        if VOICE_RE.search(s):
            continue
        if SPEAKER_RE.match(s):
            voiceless.append(s)
    events = collections.Counter()
    for et in EVENT_TYPES:
        events[et] = len(re.findall(r'\[\s*' + et + r'\b', text))
    return {
        'scenes': scenes, 'voices': voices, 'by_scene': by_scene,
        'voiceless': voiceless, 'choices': len(CHOICE_RE.findall(text)),
        'next': len(NEXT_RE.findall(text)), 'like': len(LIKE_RE.findall(text)),
        'control': len(SELECT_RE.findall(text)), 'events': events,
    }


def parse_port(paths, manifest):
    voices, labels, choices, jumps = [], [], 0, []
    say_strings = []
    event_comments = collections.Counter()
    for p in paths:
        text = open(p, encoding='utf-8').read()
        lines = text.splitlines()
        labels += EN_LABEL_RE.findall(text)
        choices += len(EN_CHOICE_RE.findall(text))
        for line in lines:
            mv = EN_VOICE_RE.match(line)
            if mv:
                name = mv.group(1)
                voices.append({'name': name, 'id': manifest.get(name)})
            mj = EN_JUMP_RE.match(line)
            if mj:
                jumps.append(mj.group(1))
            ms = EN_SAY_RE.match(line)
            if ms and ms.group(1) not in SAY_KW:
                say_strings.append(ms.group(2))
            if re.match(r'^\s*#\s*\[', line):
                for et in EVENT_TYPES:
                    if re.match(r'^\s*#\s*\[\s*' + et + r'\b', line):
                        event_comments[et] += 1
    return {'voices': voices, 'labels': labels, 'choices': choices, 'jumps': jumps,
            'say_strings': say_strings, 'events': event_comments}


def load_tl(folder):
    pairs = {}
    dups = collections.Counter()
    empty_new = []
    header_ok = True
    for p in sorted(folder.glob('*.rpy')):
        head = open(p, encoding='utf-8').read(200)
        if ('translate ' + folder.name + ' strings:') not in head:
            header_ok = False
        old = None
        for raw in open(p, encoding='utf-8'):
            s = raw.rstrip('\r\n')
            mo = TL_OLD_RE.match(s)
            if mo:
                old = mo.group(1)
                if old.strip():
                    dups[old] += 1
                continue
            mn = TL_NEW_RE.match(s)
            if mn and old is not None:
                if old.strip():
                    pairs[old] = mn.group(1)
                    if not mn.group(1).strip():
                        empty_new.append(old)
                old = None
    return {'pairs': pairs, 'dups': [k for k,v in dups.items() if v > 1],
            'empty_new': empty_new, 'header_ok': header_ok}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('chapter')
    ap.add_argument('source')
    ap.add_argument('port_glob')
    ap.add_argument('--md')
    ap.add_argument('--scenes', help='scene filter, e.g. 1209-1213 or 806,807')
    args = ap.parse_args()

    sf = None
    if args.scenes:
        sf = set()
        for part in args.scenes.split(','):
            if '-' in part:
                a, b = part.split('-', 1)
                sf.update(range(int(a), int(b) + 1))
            else:
                sf.add(int(part))
    src = parse_source(ROOT / args.source, sf)
    manifest = load_manifest()
    paths = []
    for g in args.port_glob.split(','):
        paths += [Path(p) for p in sorted(glob.glob(str(ROOT / g.strip())))]
    paths = sorted(set(paths))
    port = parse_port(paths, manifest)
    tlj = load_tl(TL_J)
    tlr = load_tl(TL_R)

    findings = []
    # A. voice ids
    src_ids = collections.Counter(src['voices'])
    port_ids = collections.Counter(v['id'] for v in port['voices'] if v['id'] is not None)
    unresolved = [v['name'] for v in port['voices'] if v['id'] is None]
    miss_v = src_ids - port_ids
    extra_v = port_ids - src_ids
    findings.append(('A voice-id', 'PASS' if not miss_v and not extra_v else 'FAIL',
                     f"src={sum(src_ids.values())} port={sum(port_ids.values())} missing={list(miss_v.elements())[:8]} extra={list(extra_v.elements())[:8]} unresolved={unresolved[:8]}"))
    # B. scenes
    scene_labels = set()
    for l in port['labels']:
        for n in re.findall(r'(\d+)', l):
            scene_labels.add(int(n))
    miss_s = set(src['scenes']) - scene_labels
    findings.append(('B scene coverage', 'PASS' if not miss_s else 'FAIL',
                     f"src={len(src['scenes'])} labels_with_scene={len(scene_labels)} missing={sorted(miss_s)[:12]}"))
    # C. voiceless dialogue in JA TL
    ja_news = [v for v in tlj['pairs'].values() if v]
    ja_blob = '\n'.join(ja_news)
    miss_vl = []
    for line in src['voiceless']:
        # strip speaker prefix and compare core
        core = SPEAKER_RE.sub('', line).strip(' 。…')
        if len(core) < 2:
            continue
        if core not in ja_blob:
            miss_vl.append(line[:60])
    findings.append(('C voiceless JA', 'REVIEW' if miss_vl else 'PASS',
                     f"src_voiceless={len(src['voiceless'])} not_found_in_ja_tl={len(miss_vl)} sample={miss_vl[:6]}"))
    # D. control counts
    findings.append(('D choices', 'PASS' if src['choices'] == port['choices'] else 'FAIL',
                     f"src={src['choices']} port={port['choices']}"))
    findings.append(('D next/like/control', 'INFO',
                     f"src next={src['next']} like={src['like']} control={src['control']}; port jumps={len(port['jumps'])}"))
    # E. events
    ev_diff = {k: (src['events'][k], port['events'][k]) for k in EVENT_TYPES if src['events'][k] != port['events'][k]}
    findings.append(('E events', 'INFO', f"src={dict(src['events'])} port_comments={dict(port['events'])} diff={ev_diff}"))
    # F. TL structural
    missing_ja = [s for s in port['say_strings'] if s not in tlj['pairs']]
    missing_ru = [s for s in port['say_strings'] if s not in tlr['pairs']]
    findings.append(('F TL pairs', 'PASS' if not missing_ja and not missing_ru else 'FAIL',
                     f"EN_strings={len(port['say_strings'])} no_JA={len(missing_ja)} no_RU={len(missing_ru)} sample_JA={missing_ja[:4]} sample_RU={missing_ru[:4]}"))
    findings.append(('F TL hygiene', 'PASS' if not tlj['dups'] and not tlr['dups'] and not tlj['empty_new'] and not tlr['empty_new'] and tlj['header_ok'] and tlr['header_ok'] else 'FAIL',
                     f"dup_JA={len(tlj['dups'])} dup_RU={len(tlr['dups'])} empty_JA={len(tlj['empty_new'])} empty_RU={len(tlr['empty_new'])} header_ok=({tlj['header_ok']},{tlr['header_ok']})"))

    lines = [f'# Coverage audit: {args.chapter}', '', f'Source: `{args.source}`',
             f'Port: `{args.port_glob}` ({len(paths)} files)', '',
             '| check | status | detail |', '|---|---|---|']
    for name, status, detail in findings:
        lines.append(f'| {name} | {status} | {detail} |')
    out = '\n'.join(lines) + '\n'
    if args.md:
        open(args.md, 'w', encoding='utf-8').write(out)
    print(out)


if __name__ == '__main__':
    main()
