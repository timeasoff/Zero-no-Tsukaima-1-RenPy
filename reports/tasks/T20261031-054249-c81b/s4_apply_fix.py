# -*- coding: utf-8 -*-
"""Порция правки кода главы 1 по канону (задача T20261031-054249-c81b).

Операции (все по данным S1-карты и канона chapter_02):
  1) 54 matched: значение update_sympathy -> value_canon (8 совпадают, без правки);
  2) 19 EXTRA:   13 удалить («другая ±20 / Луиза ∓20» — в каноне нет),
                 6 заменить на $ tndl(±30) — в оригинале на этих местах
                 standalone tndl(±30) (порт превратил их в like Луизы);
  3) 25 paired:  вставить $ tndl(N) сразу после matched-строки
                 (в events_full за like сразу следует tndl).
JA-текст и tl/ не затрагиваются. Запуск: python ... [--apply].
"""
import csv
import io
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
ROOT = os.path.normpath(ROOT)

MAP_CSV = os.path.join(ROOT, 'reports', 'tasks', 'T20261031-054249-c81b',
                       'sympathy_port_ch1_map.csv')
CANON_CSV = os.path.join(ROOT, 'references', 'sympathy_canon.csv')
EVT = os.path.join(ROOT, 'ps2_source', 'events_full', 'chapter_02_ゼロのルイズ.txt')
CH1_DIR = os.path.join(ROOT, 'game', 'chapters', '1')

APPLY = '--apply' in sys.argv

# --- 6 standalone tndl: EXTRA-строка Луизы стоит там, где в JA tndl(±30) ---
# ключ: file:line EXTRA-строки -> значение tndl (знак сверен со SCENE events_full)
STANDALONE = {
    'script-ch1_2.rpy:112': -30,   # events_full:835  после talk 10850 (ch1.2_s_007)
    'script-ch1_3.rpy:385': -30,   # events_full:3976 после talk 3967  (ch1.3_m_008)
    'script-ch1_3.rpy:427': 30,    # events_full:3939 после talk 3963  (ch1.3_m_014)
    'script-ch1_6.rpy:437': 30,    # events_full:1742 после talk 10933 (ch1.6_s_023)
    'script-ch1_6.rpy:470': -30,   # events_full:1837 после talk 5664  (ch1.6_l_026)
    'script-ch1_8.rpy:611': 30,    # events_full:4413 после talk 4915  (ch1.8_l_012)
}


def load_canon_tndl():
    """сцена -> (events_full_line for like, tndl value or None)."""
    lines = io.open(EVT, encoding='utf-8').read().split('\n')
    rows = list(csv.DictReader(io.open(CANON_CSV, encoding='utf-8')))
    out = {}
    for r in rows:
        if r['chapter_source'] != 'chapter_02_ゼロのルイズ':
            continue
        scene = int(r['scene'])
        fl = int(r['events_full_line'])
        # events_full_line — 1-based номер строки like; tndl стоит на следующей
        # строке = индекс fl в 0-based массиве
        nxt = lines[fl] if fl < len(lines) else ''
        m = re.match(r'TNDL\s+tndl\((-?\d+)\)', nxt)
        out[(scene, r['char_key'])] = (fl, int(m.group(1)) if m else None)
    return out


def main():
    map_rows = list(csv.DictReader(io.open(MAP_CSV, encoding='utf-8')))
    canon = load_canon_tndl()

    # собираем операции: {file: [(line, kind, payload)]}
    ops = {}
    def add(f, line, kind, payload, note=''):
        ops.setdefault(f, []).append((line, kind, payload, note))

    stats = {'value': 0, 'value_same': 0, 'del': 19 - len(STANDALONE),
             'repl_tndl': 0, 'ins_tndl': 0}

    for r in map_rows:
        fl_key = r['file:line']
        fname, lno = fl_key.rsplit(':', 1)
        lno = int(lno)
        if not r['value_canon']:
            if fl_key in STANDALONE:
                add(fname, lno, 'repl_tndl', STANDALONE[fl_key], 'standalone tndl')
                stats['repl_tndl'] += 1
            else:
                add(fname, lno, 'del', None, 'EXTRA louise')
                stats['del'] -= 0  # recount later
            continue
        new = int(r['value_canon'])
        old = int(r['value'])
        if new != old:
            add(fname, lno, 'value', (old, new), 'canon %s %s' % (r['matched_scene'], r['char_key']))
            stats['value'] += 1
        else:
            stats['value_same'] += 1
        # paired tndl?
        key = (int(r['matched_scene']), r['char_key'])
        if key in canon:
            fl, tv = canon[key]
            if tv is not None:
                add(fname, lno, 'ins_tndl', tv, 'paired after scene %s' % r['matched_scene'])
                stats['ins_tndl'] += 1

    stats['del'] = sum(1 for f in ops for o in ops[f] if o[1] == 'del')
    print('ops:', {k: sum(1 for f in ops for o in ops[f] if o[1] == k)
                   for k in ('value', 'del', 'repl_tndl', 'ins_tndl')})

    problems = []
    for fname in sorted(ops):
        path = os.path.join(CH1_DIR, fname)
        if not os.path.exists(path):
            problems.append('нет файла %s' % path)
            continue
        lines = io.open(path, encoding='utf-8').read().split('\n')
        for lno, kind, payload, note in sorted(ops[fname], key=lambda o: -o[0]):
            if lno - 1 >= len(lines):
                problems.append('%s:%d вне файла' % (fname, lno))
                continue
            line = lines[lno - 1]
            if kind == 'value':
                old, new = payload
                expect = re.match(r'\s*\$\s*update_sympathy\((-?\d+)', line)
                if not expect or int(expect.group(1)) != old:
                    problems.append('%s:%d ожидал update_sympathy(%d), есть %r' %
                                    (fname, lno, old, line.strip()))
            elif kind in ('del', 'repl_tndl'):
                if 'update_sympathy' not in line:
                    problems.append('%s:%d ожидал update_sympathy для удаления, есть %r' %
                                    (fname, lno, line.strip()))
            elif kind == 'ins_tndl':
                if 'update_sympathy' not in line:
                    problems.append('%s:%d вставка после update_sympathy, есть %r' %
                                    (fname, lno, line.strip()))

    # контекст 6 standalone — сверка, что перед EXTRA стоит нужный voice
    anchor_expect = {
        'script-ch1_2.rpy:112': 'ch1.2_s_007',
        'script-ch1_3.rpy:385': 'ch1.3_m_008',
        'script-ch1_3.rpy:427': 'ch1.3_m_014',
        'script-ch1_6.rpy:437': 'ch1.6_s_023',
        'script-ch1_6.rpy:470': 'ch1.6_l_026',
        'script-ch1_8.rpy:611': 'ch1.8_l_012',
    }
    for key, voice in anchor_expect.items():
        fname, lno = key.rsplit(':', 1)
        lno = int(lno)
        lines = io.open(os.path.join(CH1_DIR, fname), encoding='utf-8').read().split('\n')
        window = '\n'.join(lines[max(0, lno - 8):lno])
        if 'voice "%s"' % voice not in window:
            problems.append('%s: anchor voice %s не найден в 8 строках выше' % (key, voice))

    if problems:
        print('ПРОБЛЕМЫ (%d):' % len(problems))
        for p in problems:
            print('  -', p)
        if APPLY:
            print('APPLY отменён из-за проблем')
            return 1
        return 1

    print('самопроверка: OK')
    if not APPLY:
        print('dry-run: правок не делал')
        return 0

    for fname in sorted(ops):
        path = os.path.join(CH1_DIR, fname)
        lines = io.open(path, encoding='utf-8').read().split('\n')
        for lno, kind, payload, note in sorted(ops[fname], key=lambda o: -o[0]):
            i = lno - 1
            if kind == 'value':
                old, new = payload
                lines[i] = re.sub(r'(\$\s*update_sympathy\()(-?\d+)',
                                  lambda m: m.group(1) + str(new), lines[i], count=1)
            elif kind == 'del':
                del lines[i]
            elif kind == 'repl_tndl':
                indent = re.match(r'\s*', lines[i]).group(0)
                lines[i] = '%s$ tndl(%d)' % (indent, payload)
            elif kind == 'ins_tndl':
                indent = re.match(r'\s*', lines[i]).group(0)
                lines.insert(i + 1, '%s$ tndl(%d)' % (indent, payload))
        io.open(path, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
        print('записан', fname, '(%d ops)' % len(ops[fname]))
    return 0


def fl_key_of(fname, lno):
    return '%s:%d' % (fname, lno)


sys.exit(main())
