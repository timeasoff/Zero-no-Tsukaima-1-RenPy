#!/usr/bin/env python3
"""Voice-workflow audit for the port/ch22-to-end scope.

Checks (strictly by ID, never by text):
  1. ordered match: source [voice N] sequence vs port voice-name sequence resolved
     through references/voice_id_map.csv (per part)
  2. wav_source track presence for every used id
  3. transcriptions_ja_ru.csv row status (present / commented / removed)
  4. duplicate voice names in .rpy, duplicate ids in manifest
  5. speakers used in .rpy vs define in game/characters.rpy
  6. missing-audio count (documented cases)

Usage: python tools/voice_audit.py [--md reports/voice_audit.md]
"""
from __future__ import annotations
import argparse
import collections
import glob
import os
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
MANIFEST = ROOT / 'references' / 'voice_id_map.csv'
CSV = ROOT / 'transcriptions_ja_ru.csv'
WAV = ROOT / 'wav_files' if (ROOT / 'wav_files').is_dir() else ROOT / 'wav_source'
CHARS = ROOT / 'game' / 'characters.rpy'
SRC = ROOT / 'ps2_source' / 'chapters'

VOICE_RE = re.compile(r'^\s*voice\s+"([^"]+)"', re.M)
JA_VOICE_RE = re.compile(r'\[voice\s+(\d+)\]')
SCENE_RE = re.compile(r'^----\s*SCENE\s+(\d+)\s*----', re.M)
MAN_RE = re.compile(r'^([^,\s#]+)\s*,\s*(\d+)')

# (name, source chapter, port files glob, scene filter)
UNITS = [
    ('ch22_5', 'chapter_23_料理の鉄人.txt', 'game/chapters/22/script-ch22_5.rpy', lambda n: 1209 <= n <= 1213),
    ('ch23', 'chapter_24_沈黙の応援.txt', 'game/chapters/23/*.rpy', lambda n: 849 <= n <= 893),
    ('ch24', 'chapter_25_制服の魅力.txt', 'game/chapters/24/*.rpy', lambda n: 894 <= n <= 902),
    ('ch25', 'chapter_26_手紙の秘密.txt', 'game/chapters/25/*.rpy', lambda n: True),
    ('ch26', 'chapter_27_タバサの秘密.txt', 'game/chapters/26/*.rpy', lambda n: True),
    ('ch27', 'chapter_28_ハルナの秘密.txt', 'game/chapters/27/*.rpy', lambda n: True),
    ('ch28', 'chapter_29_夜の秘密.txt', 'game/chapters/28/*.rpy', lambda n: True),
    ('sp90', 'chapter_90_特別イベントA（トゥンデレ／デレ）.txt', 'game/chapters/extra/sp90.rpy', lambda n: True),
    ('sp91+sp_d1', 'chapter_91_特別イベントB（トゥンデレ／デレ）.txt',
     'game/chapters/extra/sp91.rpy,game/chapters/extra/sp_d1.rpy', lambda n: True),
]


def load_manifest():
    m = {}
    for raw in open(MANIFEST, encoding='utf-8-sig'):
        x = MAN_RE.match(raw.strip())
        if x:
            m[x.group(1)] = int(x.group(2))
    return m


def load_csv():
    active, commented = set(), set()
    import csv as _csv
    with open(CSV, encoding='utf-8-sig', newline='') as fh:
        for row in _csv.reader(fh):
            if len(row) < 4:
                continue
            fn = (row[0] or '').strip()
            m = re.match(r'^(#+\s*)?VOICE_ID\.BIN_([0-9A-F]{8})\.(wav|WAV|STV)$', fn, re.I)
            if not m:
                continue
            h = m.group(2)
            status = (row[3] or '').strip()
            marked = bool(m.group(1)) or bool(re.search(
                r'\bch\d[\w.]*_\w+_\d+|#?\s*USED\s+ch\d', status, re.I))
            (commented if marked else active).add(h)
    return active, commented


def load_defines():
    txt = open(CHARS, encoding='utf-8').read()
    return set(re.findall(r'^define\s+([A-Za-z_]\w*)\s*=\s*Character', txt, re.M))


def source_ids(path, keep):
    text = open(SRC / path, encoding='utf-8').read()
    out, cur = [], None
    for line in text.splitlines():
        ms = SCENE_RE.match(line)
        if ms:
            cur = int(ms.group(1))
        mv = JA_VOICE_RE.search(line)
        if mv and cur is not None and keep(cur):
            out.append(int(mv.group(1)))
    return out


def port_voices(globs, manifest):
    """Voice names ordered by source scene number, interleaving multiple files."""
    entries, speakers, dup = [], set(), []
    files = []
    for g in globs.split(','):
        files += [Path(p) for p in glob.glob(str(ROOT / g.strip()))]
    for p in files:
        text = open(p, encoding='utf-8').read()
        scene = None
        for line in text.splitlines():
            ml = re.match(r'^label\s+\S*scene_(\d+):', line)
            if ml:
                scene = int(ml.group(1))
            mv = VOICE_RE.match(line)
            if mv and scene is not None:
                entries.append((scene, mv.group(1)))
            ms = re.match(r'^\s*([A-Za-z_]\w*)\s+"(?:[^"\\]|\\.)*"', line)
            if ms and ms.group(1) not in ('voice', 'jump', 'call', 'label', 'menu',
                                          'if', 'elif', 'else', 'return', 'play',
                                          'stop', 'pause', 'scene', 'show', 'hide',
                                          'window', 'with', 'python', 'init', 'define',
                                          'default', 'th'):
                speakers.add(ms.group(1))
        c = collections.Counter(VOICE_RE.findall(text))
        dup += [k for k, v in c.items() if v > 1]
    entries.sort(key=lambda x: x[0])  # stable: preserves line order within a scene
    return [n for _, n in entries], speakers, dup


def wav_files():
    out = set()
    for n in os.listdir(WAV):
        m = re.search(r'VOICE_ID\.BIN_([0-9A-F]{8})\.wav', n)
        if m:
            out.add(m.group(1))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--md')
    args = ap.parse_args()
    man = load_manifest()
    csv_active, csv_commented = load_csv()
    defines = load_defines()
    wavs = wav_files()
    lines = ['# Voice-workflow audit — port/ch22-to-end', '',
             'Правило: ID только из `[voice N]`, не по тексту.', '',
             '| unit | src voices | port voices | ordered match | no-wav | CSV active | CSV commented | CSV missing | dups | speakers undefined |',
             '|---|---:|---:|---|---:|---:|---:|---:|---:|---|']
    total = collections.Counter()
    all_used = set()
    for name, src, globs, keep in UNITS:
        sids = source_ids(src, keep)
        vnames, speakers, dups = port_voices(globs, man)
        pids = [man.get(v) for v in vnames]
        unknown = [v for v in vnames if v not in man]
        known = [i for i in pids if i is not None]
        filtered_src = [i for i in sids if i in set(known)]
        ordered = (filtered_src == known)
        no_wav = [i for i in pids if i is not None and '%08X' % i not in wavs]
        active = [i for i in pids if i is not None and '%08X' % i in csv_active]
        commented = [i for i in pids if i is not None and '%08X' % i in csv_commented]
        missing_csv = [i for i in pids if i is not None and '%08X' % i not in csv_active and '%08X' % i not in csv_commented]
        undef = sorted(speakers - defines)
        all_used.update(i for i in pids if i is not None)
        total['src'] += len(sids); total['port'] += len(vnames)
        total['no_wav'] += len(no_wav); total['csv_active'] += len(active)
        total['csv_commented'] += len(commented); total['csv_missing'] += len(missing_csv)
        total['unknown_name'] += len(unknown); total['dup_name'] += len(dups)
        total['undef'] += len(undef)
        lines.append('| %s | %d | %d | %s | %d | %d | %d | %d | %d | %s |' % (
            name, len(sids), len(pids), 'OK' if ordered else 'FAIL(%d)' % sum(a != b for a, b in zip(sids, pids)),
            len(no_wav), len(active), len(commented), len(missing_csv), len(dups),
            ','.join(undef) if undef else '—'))
        if not ordered:
            diff = [(n, a, b) for n, a, b in zip(vnames, sids, pids) if a != b][:5]
            lines.append('  - order diff sample: %s' % diff)
        if unknown:
            lines.append('  - voice names without manifest: %s' % unknown[:5])
    lines.append('')
    lines.append('| TOTAL | %d | %d | — | %d | %d | %d | %d | %d | %d |' % (
        total['src'], total['port'], total['no_wav'], total['csv_active'],
        total['csv_commented'], total['csv_missing'], total['dup_name'], total['undef']))
    out = '\n'.join(lines) + '\n'
    if args.md:
        open(args.md, 'w', encoding='utf-8').write(out)
    print(out)


if __name__ == '__main__':
    main()
