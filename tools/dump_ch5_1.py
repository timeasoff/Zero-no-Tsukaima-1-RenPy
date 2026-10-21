# -*- coding: utf-8 -*-
"""Дамп порядка реплик части ch5.1 (сцены 269-284) с ключами голосов.

Использование: python tools/dump_ch5_1.py > .tmp/ch5_1_lines.txt
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'ps2_source', 'events_full',
                   'chapter_06_本当の想い.txt')

SCENES = list(range(269, 285))
ORDER = [269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280,
         281, 282, 283, 284]

SPK = {'サイト': 's', 'ルイズ': 'l', 'ハルナ': 'ha', 'シエスタ': 'si',
       'デルフリンガー': 'd', 'キュルケ': 'k', 'タバサ': 't', 'ギーシュ': 'g',
       'モンモランシー': 'm', 'ウェザリー': 'w', 'null': 'th'}

RE_TALK = re.compile(r'^DIALOGUE\s+talk\((.*)\)\s*$')
RE_CHOICE = re.compile(r'^CHOICE\s+selectItem\("((?:[^"\\]|\\.)*)",\s*\(0x01000000 \+(\d+)\).*$')
RE_GOTO = re.compile(r'^GOTO\s+next\(\(0x01000000 \+(\d+)\).*$')
RE_LIKE = re.compile(r'^LIKE\s+like\("([^"]*)",\s*(-?\d+)\)\s*$')
SPLIT_ARGS = re.compile(r'"((?:[^"\\]|\\.)*)"|(\bnull\b)|\(0x0[46]000000 \+(\d+)\)')


def parse_args(args):
    toks = []
    vid = None
    for m in SPLIT_ARGS.finditer(args):
        if m.group(3):
            vid = int(m.group(3))
        elif m.group(2):
            toks.append('null')
        else:
            toks.append(m.group(1))
    spk = toks[0] if len(toks) > 0 else 'null'
    disp = toks[1] if len(toks) > 1 else 'null'
    text = toks[2] if len(toks) > 2 else ''
    return spk, disp, text, vid


def parse():
    scenes = {}
    cur = None
    for ln in io.open(SRC, encoding='utf-8'):
        ln = ln.rstrip('\n')
        m = re.match(r'^## SCENE (\d+)', ln)
        if m:
            cur = int(m.group(1))
            scenes.setdefault(cur, [])
            continue
        if cur not in SCENES:
            continue
        ev = scenes[cur]
        m = RE_TALK.match(ln)
        if m:
            spk, disp, text, vid = parse_args(m.group(1))
            ev.append(('talk', spk, disp, text, vid))
            continue
        m = RE_CHOICE.match(ln)
        if m:
            ev.append(('choice', m.group(1), int(m.group(2))))
            continue
        m = RE_GOTO.match(ln)
        if m:
            ev.append(('goto', int(m.group(1))))
            continue
        m = RE_LIKE.match(ln)
        if m:
            ev.append(('like', m.group(1), int(m.group(2))))
            continue
    return scenes


def main():
    scenes = parse()
    counts = {}
    th = 0
    for sc in ORDER:
        print('=== SCENE %d ===' % sc)
        for e in scenes.get(sc, []):
            if e[0] == 'talk':
                spk, disp, text, vid = e[1], e[2], e[3], e[4]
                if vid is None:
                    th += 1
                    print('  THOUGHT ch5_th_%03d  [%s] %s' % (th, spk, text))
                else:
                    key = SPK.get(spk, 'x')
                    counts[key] = counts.get(key, 0) + 1
                    name = 'ch5_%s_%03d' % (key, counts[key])
                    print('  %-16s vid=%-6d disp=%-6s [%s] %s'
                          % (name, vid, disp, spk, text))
            elif e[0] == 'choice':
                print('  CHOICE -> scene %d : %s' % (e[2], e[1]))
            elif e[0] == 'like':
                print('  LIKE %s %+d' % (e[1], e[2]))
            elif e[0] == 'goto':
                print('  GOTO -> scene %d' % e[1])
    print('\nvoices per speaker:', counts, 'total', sum(counts.values()))
    print('thoughts:', th)


if __name__ == '__main__':
    main()
