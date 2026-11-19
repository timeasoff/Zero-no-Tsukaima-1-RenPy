#!/usr/bin/env python3
"""Asset audit for port/ch22-to-end: BGM t{K-1}, image ids, SE, FX, movie."""
import argparse
import collections
import csv
import glob
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
SRC = ROOT / 'ps2_source' / 'chapters'
RPY = [str(ROOT / 'game/chapters/22/script-ch22_5.rpy')]
for c in range(23, 29):
    RPY += sorted(glob.glob(str(ROOT / 'game/chapters' / str(c) / '*.rpy')))
RPY += sorted(glob.glob(str(ROOT / 'game/chapters/extra/sp9*.rpy')))
RPY += [str(ROOT / 'game/chapters/extra/sp_d1.rpy')]

BGM_PLAY = re.compile(r'\[BGM\s+bgm\s+play=\+(\d+)')
BGM_STOP = re.compile(r'\[BGM\s+bgm\s+stop=')
IMG = re.compile(r'\[(?:BG\s+stage|EVENT_CG\s+event)\s+image=\+(\d+)')
SE = re.compile(r'\[SE\s+se\d+\s+play=\+(\d+)')
MOVIE = re.compile(r'\[MOVIE\s+movie\((\d+)\)\]')

PORT_BGM = re.compile(r'play music t(\d+)')
PORT_BGM_ARG = re.compile(r'new_music="t(\d+)"')
PORT_IMG_ID = re.compile(r'(?:fade|dissolve|flash)_fx\("id\((\d+)\)"')
PORT_IMG_NAMED = re.compile(r'(?:fade|dissolve|flash)_fx\("([^"()]+)"')
PORT_SE = re.compile(r'play sound (\w+)')
PORT_FX = re.compile(r'\$\s*(\w+_fx)\(')


def source_files():
    # ch22 scope = part 5 only (extra 1209-1213); other chapters whole
    out = []
    for c in range(23, 30):
        out += glob.glob(str(SRC / ('chapter_%d_*.txt' % c)))
    out += glob.glob(str(SRC / 'chapter_90_*.txt'))
    out += glob.glob(str(SRC / 'chapter_91_*.txt'))
    return sorted(set(out))


def scoped_source_blob():
    """Drop scenes outside the target scope (ch22 only part 5)."""
    chunks = []
    for p in source_files():
        text = Path(p).read_text(encoding='utf-8')
        if 'chapter_23_' in p:
            parts = re.split(r'(?=^---- SCENE \d+ ----)', text, flags=re.M)
            text = parts[0] + ''.join(b for b in parts[1:]
                                      if re.match(r'---- SCENE (1209|1210|1211|1212|1213) ----', b))
        chunks.append(text)
    return '\n'.join(chunks)


def load_map():
    rows = {}
    with open(ROOT / 'references/image_id_map.csv', encoding='utf-8') as f:
        lines = [l for l in f if not l.startswith('#')]
    for r in csv.DictReader(lines):
        if r.get('image_id', '').isdigit():
            rows[int(r['image_id'])] = r
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--md')
    args = ap.parse_args()
    src_blob = scoped_source_blob()
    port_blob = '\n'.join(Path(p).read_text(encoding='utf-8') for p in RPY)
    imap = load_map()

    s_bgm = collections.Counter(int(x) - 1 for x in BGM_PLAY.findall(src_blob))
    p_bgm = collections.Counter(int(x) for x in PORT_BGM.findall(port_blob) + PORT_BGM_ARG.findall(port_blob))
    miss_bgm = s_bgm - p_bgm
    extra_bgm = p_bgm - s_bgm

    s_img = set(int(x) for x in IMG.findall(src_blob))
    p_id = set(int(x) for x in PORT_IMG_ID.findall(port_blob))
    unmapped = sorted(s_img - set(imap))
    not_in_port = sorted(s_img - p_id)
    named_in_map = sum(1 for k in p_id if imap.get(k, {}).get('filename'))

    s_se = collections.Counter(BGM_STOP.findall(src_blob))
    movies = MOVIE.findall(src_blob)
    port_se = collections.Counter(PORT_SE.findall(port_blob))
    fx = collections.Counter(PORT_FX.findall(port_blob))

    lines = ['# Asset audit — port/ch22-to-end', '',
             'Source files: %d, port files: %d' % (len(source_files()), len(RPY)), '',
             '## BGM (formula t{K-1})',
             '- source play ids: %d unique; expected tracks: %s' % (len(s_bgm), sorted(s_bgm)),
             '- port tracks: %d unique' % len(p_bgm),
             '- missing tracks: %s' % (sorted(miss_bgm.elements())[:20] or 'none'),
             '- extra tracks (not from source): %s' % (sorted(extra_bgm.elements())[:20] or 'none'), '',
             '## Images',
             '- source image ids: %d; map rows: %d; ids missing from map: %s' % (len(s_img), len(imap), unmapped[:20]),
             '- source ids not seen as id(K) placeholder in port: %d (may be named directly) %s' % (len(not_in_port), not_in_port[:20]),
             '- placeholders in port: %d distinct; of them with filled filename: %d (W6 risk)' % (len(p_id), named_in_map),
             '',
             '## SE / movie / FX',
             '- source BGM-stop events: %d; port stop music: %d' % (sum(s_se.values()), port_blob.count('stop music')),
             '- source MOVIE calls: %d; port play sound: %s' % (len(movies), dict(port_se)),
             '- fx calls: %s' % dict(fx),
             '']
    out = '\n'.join(lines) + '\n'
    if args.md:
        Path(args.md).write_text(out, encoding='utf-8')
    print(out)


if __name__ == '__main__':
    main()
