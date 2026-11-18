#!/usr/bin/env python3
"""Parse chapter_90/91 (tsundere/dere) into structured JSON.

Usage: python tools/gen_extra_data.py <chapter_90|chapter_91> <out.json>

Dialogue rule (per ps2-source skill §2.1): a line with a speaker prefix "X："
starts a dialogue; the following physical lines WITHOUT a speaker prefix are its
continuation, and the LAST one carries "[voice N]".  A new speaker prefix always
starts a new dialogue (even if the previous one had no [voice]).
"""
import json
import re
import sys

CHAPTERS = {
    'chapter_90': 'ps2_source/chapters/chapter_90_特別イベントA（トゥンデレ／デレ）.txt',
    'chapter_91': 'ps2_source/chapters/chapter_91_特別イベントB（トゥンデレ／デレ）.txt',
}


def parse_scene(no, body):
    items = []
    lines = [l.rstrip() for l in body.split('\n') if l.strip()]
    pending = None  # (speaker, [text parts])
    def flush():
        nonlocal pending
        if pending is not None:
            items.append({'kind': 'dlg', 'speaker': pending[0], 'ja': ''.join(pending[1]),
                          'voice': None, 'thought': False})
            pending = None
    for line in lines:
        stripped = line.strip()
        if pending is not None:
            # new speaker prefix, engine tag or control marker -> flush previous
            # as no-voice dialogue and reprocess the line normally
            if (re.match(r'^[^：\n]+：', stripped)
                    or stripped.startswith('[')
                    or stripped.startswith('【')
                    or stripped.startswith('→')):
                flush()
            else:
                mv = re.match(r'^(.*?)\s*\[voice (\d+)\]$', stripped)
                if mv:
                    items.append({'kind': 'dlg', 'speaker': pending[0],
                                  'ja': ''.join(pending[1]) + mv.group(1).strip(),
                                  'voice': int(mv.group(2)), 'thought': False})
                    pending = None
                else:
                    pending[1].append(stripped)
                continue
        if stripped.startswith('['):
            flush()
            items.append({'kind': 'event', 'src': stripped})
            continue
        mc = re.match(r'【選択肢】(.+?) → scene (\d+)', stripped)
        if mc:
            flush()
            items.append({'kind': 'choice', 'text': mc.group(1), 'target': int(mc.group(2))})
            continue
        mg = re.match(r'→ next scene (\d+)', stripped)
        if mg:
            flush()
            items.append({'kind': 'goto', 'target': int(mg.group(1))})
            continue
        md = re.match(r'【デート】(.+?) → scene (\d+)', stripped)
        if md:
            flush()
            items.append({'kind': 'date', 'speaker': md.group(1), 'target': int(md.group(2))})
            continue
        ml = re.match(r'【好感度】(.+?)\s+(-?\d+)', stripped)
        if ml:
            flush()
            items.append({'kind': 'like', 'speaker': ml.group(1), 'value': int(ml.group(2))})
            continue
        mv = re.match(r'^(.*?)\s*\[voice (\d+)\]$', stripped)
        if mv:
            prefix = mv.group(1).strip()
            if '：' in prefix:
                spk, ja = prefix.split('：', 1)
                items.append({'kind': 'dlg', 'speaker': spk, 'ja': ja, 'voice': int(mv.group(2)),
                              'thought': False})
            else:
                items.append({'kind': 'dlg', 'speaker': 'null', 'ja': prefix,
                              'voice': int(mv.group(2)), 'thought': True})
            continue
        msp = re.match(r'^([^：]+)：(.+)$', stripped)
        if msp:
            pending = (msp.group(1), [msp.group(2)])
            continue
        items.append({'kind': 'dlg', 'speaker': 'null', 'ja': stripped,
                      'voice': None, 'thought': True})
    flush()
    return {'no': no, 'items': items}


def main():
    key, out = sys.argv[1], sys.argv[2]
    text = open(CHAPTERS[key], encoding='utf-8').read()
    matches = re.finditer(r'^---- SCENE (\d+) ----(.*?)(?=^---- SCENE |\Z)', text, re.M | re.S)
    scenes = [parse_scene(int(m.group(1)), m.group(2)) for m in matches]
    with open(out, 'w', encoding='utf-8') as f:
        json.dump({'chapter': key, 'source': CHAPTERS[key], 'scenes': scenes}, f,
                  ensure_ascii=False, indent=1)
    voices = sum(1 for s in scenes for i in s['items'] if i['kind'] == 'dlg' and i['voice'] is not None)
    print('chapter', key, 'scenes', len(scenes), 'voices', voices, 'out', out)


if __name__ == '__main__':
    main()
