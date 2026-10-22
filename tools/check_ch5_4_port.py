# -*- coding: utf-8 -*-
"""Сверка порта части ch5_4 с японским источником.

Проверяет:
  * порядок и состав голосов: источник (events_full) == сценарий == манифест;
  * наличие .ogg для каждой строки `voice`;
  * `update_sympathy` == события 【好感度】;
  * меню: число, пункты, цели вариантов == CHOICE/【選択肢】 источника;
  * структура extra-блоков: main -> call label -> ... -> return.

Запуск:  python tools/check_ch5_4_port.py
"""

import io
import os
import re
import sys
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'ps2_source', 'events_full', 'chapter_06_本当の想い.txt')
SCRIPT = os.path.join(ROOT, 'game', 'chapters', '5', 'script-ch5_4.rpy')
MANIFEST = os.path.join(ROOT, 'references', 'voice_id_map.csv')
OGG = os.path.join(ROOT, 'game', 'audio', 'voices')

# порядок сцен части (основная линия 315-319 + extra-блоки 1383-1407)
FLOW = [
    (315, [], None),
    (1383, [1384, 1385, 1386], 1387),
    (316, [], None),
    (1388, [1389, 1390, 1391], 1392),
    (317, [], None),
    (1393, [1394, 1395, 1396], 1397),
    (318, [], None),
    (1398, [1399, 1400, 1401], 1402),
    (319, [], None),
    (1403, [1404, 1405, 1406], 1407),
]

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
    return (toks[0] if toks else 'null',
            toks[1] if len(toks) > 1 else 'null',
            toks[2] if len(toks) > 2 else '',
            vid)


def parse_events():
    """-> {scene: {'talk': [(spk, text, vid)], 'like': [(key, n)], 'choice': [(target, ja)]}}"""
    out = {}
    cur = None
    for ln in io.open(SRC, encoding='utf-8'):
        ln = ln.rstrip('\n')
        ms = re.match(r'^## SCENE (\d+)', ln)
        if ms:
            cur = int(ms.group(1))
            continue
        if cur is None:
            continue
        b = out.setdefault(cur, {'talk': [], 'like': [], 'choice': []})
        m = re.match(r'^DIALOGUE\s+talk\((.*)\)\s*$', ln)
        if m:
            spk, disp, text, vid = parse_args(m.group(1))
            b['talk'].append((spk, text, vid))
            continue
        m = re.match(r'^LIKE\s+like\("([^"]+)",\s*(-?\d+)\)\s*$', ln)
        if m:
            b['like'].append((m.group(1), int(m.group(2))))
            continue
        m = re.match(r'^CHOICE\s+selectItem\("(.*?)",\s*\(0x01000000 \+(\d+)\)', ln)
        if m:
            b['choice'].append((int(m.group(2)), m.group(1)))
    return out


def main():
    ev = parse_events()
    problems = []

    # ---------- 1) порядок сцен ----------
    order = []
    for sc, branches, rejoin in FLOW:
        order.append(sc)
        order.extend(branches)
        if rejoin:
            order.append(rejoin)

    # ---------- 2) голоса: источник ----------
    src_voices = []          # (scene, spk, vid)
    for sc in order:
        for spk, text, vid in ev[sc]['talk']:
            if vid is not None:
                src_voices.append((sc, spk, vid))

    # ---------- 3) голоса: сценарий ----------
    lines = io.open(SCRIPT, encoding='utf-8').read().split('\n')
    script_voices = []       # (name, voice_id)
    cur_scene = 0
    for ln in lines:
        ms = re.match(r'^\s*# ==== SCENE (\d+)', ln)
        if ms:
            cur_scene = int(ms.group(1))
        mv = re.match(r'^\s*voice "([^"]+)"', ln)
        if mv:
            script_voices.append((mv.group(1), cur_scene))

    if len(src_voices) != len(script_voices):
        problems.append('число голосов разошлось: источник %d, сценарий %d'
                        % (len(src_voices), len(script_voices)))

    # ---------- 4) манифест ----------
    man = {}
    for ln in io.open(MANIFEST, encoding='utf-8'):
        p = ln.rstrip('\n').split(',')
        if len(p) >= 2 and p[0].startswith('ch5.4_'):
            man[p[0]] = int(p[1])

    # ---------- 5) сверка порядка и id ----------
    order_ok = True
    for i, (name, sc) in enumerate(script_voices):
        if i >= len(src_voices):
            break
        s_sc, s_spk, s_vid = src_voices[i]
        if man.get(name) != s_vid:
            problems.append('id не совпал: %s (манифест %s, источник %d) в сцене %d'
                            % (name, man.get(name), s_vid, s_sc))
            order_ok = False
    # хвост: в источнике реплики без голоса (мысли) — их быть не должно в списке voice
    voiced_in_src = len(src_voices)
    print('голосов: источник=%d, сценарий=%d, манифест=%d' %
          (voiced_in_src, len(script_voices), len(man)))
    if len(man) != len(script_voices):
        problems.append('манифест (%d) != сценарий (%d)' % (len(man), len(script_voices)))

    # ---------- 6) .ogg ----------
    missing_ogg = []
    for name, sc in script_voices:
        p = os.path.join(OGG, name + '.ogg')
        if not os.path.exists(p):
            missing_ogg.append(name)
    if missing_ogg:
        problems.append('нет .ogg: %s' % ', '.join(missing_ogg[:5]))
    print('ogg: нет=%d' % len(missing_ogg))

    # ---------- 7) update_sympathy ----------
    src_like = []
    for sc in order:
        for key, n in ev[sc]['like']:
            src_like.append((sc, n))
    script_like = []
    for ln in lines:
        ms = re.match(r'^\s*\$ update_sympathy\((-?\d+), char_key="([^"]+)"\)', ln)
        if ms:
            script_like.append((int(ms.group(1)), ms.group(2)))
    print('好感度: источник=%d, сценарий=%d' % (len(src_like), len(script_like)))
    if len(src_like) != len(script_like):
        problems.append('число update_sympathy разошлось: %d / %d'
                        % (len(src_like), len(script_like)))
    else:
        for i, ((sc, n), (sn, sk)) in enumerate(zip(src_like, script_like)):
            if n != sn:
                problems.append('update_sympathy[%d]: источник %d (сцена %d) != сценарий %d'
                                % (i, n, sc, sn))

    # ---------- 8) меню ----------
    src_choices = []
    for sc in order:
        for target, ja in ev[sc]['choice']:
            src_choices.append((sc, target, ja))
    script_choices = []
    cur_scene = 0
    for ln in lines:
        ms = re.match(r'^\s*# ==== SCENE (\d+)', ln)
        if ms:
            cur_scene = int(ms.group(1))
        mc = re.match(r'^\s+"([^"]+)":\s*$', ln)
        if mc:
            script_choices.append((cur_scene, mc.group(1)))
    print('пунктов меню: источник=%d, сценарий=%d' % (len(src_choices), len(script_choices)))
    if len(src_choices) != len(script_choices):
        problems.append('число пунктов меню разошлось: %d / %d'
                        % (len(src_choices), len(script_choices)))

    # ---------- 9) структура: call/return/jump ----------
    labels = set(re.findall(r'^label (\w+):', io.open(SCRIPT, encoding='utf-8').read(), re.M))
    calls = re.findall(r'^\s*call (\w+) from (_call_\w+)', io.open(SCRIPT, encoding='utf-8').read(), re.M)
    for lbl, call_id in calls:
        if lbl not in labels:
            problems.append('call %s: нет метки' % lbl)
        if call_id != '_call_%s' % lbl:
            problems.append('call %s: неверный from (%s)' % (lbl, call_id))
    returns = len(re.findall(r'^\s*return\s*$', io.open(SCRIPT, encoding='utf-8').read(), re.M))
    print('метки: %d, call: %d, return: %d' % (len(labels), len(calls), returns))
    if returns != len(calls) + 1:
        problems.append('return (%d) != call+1 (%d)' % (returns, len(calls) + 1))
    if 'jump ch5_5' not in io.open(SCRIPT, encoding='utf-8').read():
        problems.append('нет выхода jump ch5_5')

    # ---------- 10) дубли меток/имён голосов ----------
    dup_names = [k for k, v in Counter(n for n, _ in script_voices).items() if v > 1]
    if dup_names:
        problems.append('дубли имён голосов: %s' % dup_names[:5])

    print()
    if problems:
        for p in problems:
            print('PROBLEM: ' + p)
        print('\nRESULT: ПРОБЛЕМЫ: %d' % len(problems))
        return 1
    print('RESULT: OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
