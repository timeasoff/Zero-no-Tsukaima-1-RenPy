# -*- coding: utf-8 -*-
"""Извлечение JA-реплик части 7 (сцена 341 + ветки 1134/1139) в порядке порта.

Выводит: сцена | spk | voice_id | текст (JA) — по каждому talk() с голосом,
плюс мысли (voice=None) и выборы (【選択肢】). Порядок = порядок порта.
"""
import io, os, re, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EV = os.path.join(ROOT, 'ps2_source', 'events_full', 'chapter_06_本当の想い.txt')

# Часть 7: сцена 341, ветка 1134 (1134-1138), ветка 1139 (1139-1143)
PART7 = [341, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143]

RE_SET = re.compile(r'^SET\s+set\("(\w+)",\s*\{(.*)\}\)\s*$')
RE_TALK = re.compile(r'^DIALOGUE\s+talk\((.*)\)\s*$')
RE_CHOICE = re.compile(r'^CHOICE\s+selectItem\("((?:[^"\\]|\\.)*)",\s*\(0x01000000 \+(\d+)\)')
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
    text = toks[2] if len(toks) > 2 else ''
    return spk, text, vid


cur = None
for ln in io.open(EV, encoding='utf-8'):
    ln = ln.rstrip('\n')
    m = re.match(r'^## SCENE (\d+)', ln)
    if m:
        cur = int(m.group(1))
        continue
    if cur not in PART7:
        continue
    m = RE_TALK.match(ln)
    if m:
        spk, text, vid = parse_args(m.group(1))
        tag = ('v%d' % vid) if vid is not None else '(thought)'
        print('[%d] %-10s %-10s %s' % (cur, spk, tag, text.replace('\\n', ' / ')))
    m = RE_CHOICE.match(ln)
    if m:
        print('[%d] %-10s %-10s 【選択肢】 %s -> %s' % (
            cur, 'CHOICE', '', m.group(1).replace('\\n', ' / '), m.group(2)))
