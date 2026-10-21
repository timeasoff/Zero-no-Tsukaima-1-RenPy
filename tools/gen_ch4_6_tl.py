# -*- coding: utf-8 -*-
"""Генерация переводов JA/RU для части 6 (ch4_6).

old = строка сценария (дословно, как в game/chapters/4/script-ch4_6.rpy),
new = JA (канон, ps2_source/events_full) в tl/japanese и new = RU
(tools/ch4_6_ru.py) в tl/russian. Бакеты: dialogs / thoughs / choises.

Использование:
    python tools/gen_ch4_6_tl.py            # dry-run: счётчики, сверка, коллизии
    python tools/gen_ch4_6_tl.py --apply    # добавить блоки в tl-файлы
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ch4_6_ru import RU_DIALOGS, RU_THOUGHTS, RU_CHOICES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, 'game', 'chapters', '4', 'script-ch4_6.rpy')
LANG_DECL = {'ja': 'japanese', 'ru': 'russian'}

TL = {
    ('ja', 'dialogs'): os.path.join(ROOT, 'game', 'tl', 'japanese', 'dialogs.rpy'),
    ('ja', 'thoughs'): os.path.join(ROOT, 'game', 'tl', 'japanese', 'thoughs.rpy'),
    ('ja', 'choises'): os.path.join(ROOT, 'game', 'tl', 'japanese', 'choises.rpy'),
    ('ru', 'dialogs'): os.path.join(ROOT, 'game', 'tl', 'russian', 'dialogs.rpy'),
    ('ru', 'thoughs'): os.path.join(ROOT, 'game', 'tl', 'russian', 'thoughs.rpy'),
    ('ru', 'choises'): os.path.join(ROOT, 'game', 'tl', 'russian', 'choises.rpy'),
}

# ---------------------------------------------------------------- разбор скрипта
RE_VOICE = re.compile(r'^\s*voice\s+"(ch4\.6_\w+)"\s*$')
RE_TALK = re.compile(r'^\s*(\w+)\s+"(.*)"\s*$')
RE_TH = re.compile(r'^\s*th\s+"(.*)"\s*$')
RE_MENU = re.compile(r'^\s{8}"(.*)":\s*$')
RE_SCENE = re.compile(r'^(\s*)# ==== SCENE (\d+)')


def parse_script():
    """-> (dialogs, thoughts, choices): списки (key, en, ja-место)"""
    dialogs, thoughts, choices = [], [], []
    lines = io.open(SCRIPT, encoding='utf-8').read().splitlines()
    cur = 0
    head = 0
    branch = None
    i = 0
    while i < len(lines):
        ln = lines[i]
        ms = RE_SCENE.match(ln)
        if ms:
            cur = int(ms.group(2))
            if len(ms.group(1)) <= 4:
                head = cur
                branch = None
            else:
                branch = cur
        m = RE_VOICE.match(ln)
        if m:
            key = m.group(1)
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            m2 = RE_TALK.match(lines[j]) if j < len(lines) else None
            if m2:
                dialogs.append((branch or cur, key, m2.group(2)))
                i = j
        else:
            m = RE_TH.match(ln)
            if m:
                txt = m.group(1)
                tag = ''
                mt = re.search(r'\{#(ch4\.6_th_\d+)\}$', txt)
                if mt:
                    tag = mt.group(1)
                    txt = txt[:mt.start()]
                thoughts.append((branch or cur, tag, txt))
            else:
                m = RE_MENU.match(ln)
                if m:
                    choices.append((head, '', m.group(1)))
        i += 1
    return dialogs, thoughts, choices


# ---------------------------------------------------------------- разбор events
RE_SET = re.compile(r'^SET\s+set\("(\w+)",\s*\{(.*)\}\)\s*$')
RE_TALK_E = re.compile(r'^DIALOGUE\s+talk\((.*)\)\s*$')
RE_CHOICE = re.compile(r'^CHOICE\s+selectItem\("((?:[^"\\]|\\.)*)",\s*\(0x01000000 \+(\d+)\).*$')
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


def parse_events():
    """-> {scene: {'d': [...], 't': [...], 'c': [(target, ja)]}}"""
    ja = {}
    cur = 0
    files = [os.path.join(ROOT, '.tmp', 'events_261_268.txt'),
             os.path.join(ROOT, '.tmp', 'events_1085_1103.txt')]
    for fn in files:
        for ln in io.open(fn, encoding='utf-8'):
            ln = ln.rstrip('\n')
            ms = re.match(r'^## SCENE (\d+)', ln)
            if ms:
                cur = int(ms.group(1))
                ja.setdefault(cur, {'d': [], 't': [], 'c': []})
                continue
            m = RE_TALK_E.match(ln)
            if m:
                spk, disp, text, vid = parse_args(m.group(1))
                bucket = ja.setdefault(cur, {'d': [], 't': [], 'c': []})
                bucket['t' if vid is None else 'd'].append(text)
                continue
            m = RE_CHOICE.match(ln)
            if m:
                ja.setdefault(cur, {'d': [], 't': [], 'c': []})['c'].append((m.group(2), m.group(1)))
    return ja


def ja_flat(t):
    """JA-текст в одну строку: перевод строк → «　» (конвенция ch4_5)."""
    return t.replace('\\n　', '　').replace('\\n', '　')


def existing_olds(path):
    out = set()
    for ln in io.open(path, encoding='utf-8'):
        m = re.match(r'^\s*old\s+"(.*)"\s*$', ln)
        if m:
            out.add(m.group(1))
    return out


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--replace', action='store_true',
                    help='сначала убрать ранее добавленные блоки части 6')
    args = ap.parse_args()

    dialogs, thoughts, choices = parse_script()
    ja = parse_events()

    n_ja_d = sum(len(v['d']) for v in ja.values())
    n_ja_t = sum(len(v['t']) for v in ja.values())
    n_ja_c = sum(len(v['c']) for v in ja.values())

    print('script: dialogs=%d thoughts=%d choices=%d' % (len(dialogs), len(thoughts), len(choices)))
    print('events: dialogs=%d thoughts=%d choices=%d' % (n_ja_d, n_ja_t, n_ja_c))

    problems = []
    if len(dialogs) != n_ja_d:
        problems.append('число реплик скрипта и источника разошлось (%d / %d)' % (len(dialogs), n_ja_d))
    if len(thoughts) != n_ja_t:
        problems.append('число мыслей разошлось (%d / %d)' % (len(thoughts), n_ja_t))
    if len(choices) != n_ja_c:
        problems.append('число пунктов меню разошлось (%d / %d)' % (len(choices), n_ja_c))
    for p in problems:
        print('PROBLEM:', p)

    # JA по сценам, с курсором
    cursor = {sc: {'d': 0, 't': 0, 'c': 0} for sc in ja}

    def take(scene, kind):
        c = cursor.setdefault(scene, {'d': 0, 't': 0, 'c': 0})
        lst = ja.get(scene, {'d': [], 't': [], 'c': []})[kind]
        i = c[kind]
        c[kind] += 1
        if i >= len(lst):
            problems.append('в сцене %s закончились записи (%s)' % (scene, kind))
            return None
        return lst[i]

    # сборка блоков
    blocks = {k: [] for k in TL}

    def add(bucket, en, ja, ru):
        blocks[('ja', bucket)].append((en, ja))
        blocks[('ru', bucket)].append((en, ru))

    for scene, key, en in dialogs:
        ru = RU_DIALOGS.get(key)
        if ru is None:
            problems.append('нет RU для %s' % key)
            continue
        jad = take(scene, 'd')
        if jad is None:
            continue
        add('dialogs', en, ja_flat(jad), ru)

    for scene, tag, en in thoughts:
        ru = RU_THOUGHTS.get(tag)
        if ru is None:
            problems.append('нет RU для %s' % tag)
            continue
        old = '%s{#%s}' % (en, tag) if tag else en
        jat = take(scene, 't')
        if jat is None:
            continue
        add('thoughs', old, ja_flat(jat), ru)

    for scene, dummy, en in choices:
        got = take(scene, 'c')
        if got is None:
            continue
        target, ja_c = got
        ru = RU_CHOICES.get(target)
        if ru is None:
            problems.append('нет RU для опции (сцена %s)' % scene)
            continue
        add('choises', en, ja_flat(ja_c), ru)

    if args.replace:
        # снять блоки, добавленные ранее (по old из текущего скрипта и по тегу ch4.6)
        olds_all = set()
        for _sc, _k, en in dialogs:
            olds_all.add(en)
        for _sc, tag, en in thoughts:
            olds_all.add('%s{#%s}' % (en, tag) if tag else en)
        for _sc, _d, en in choices:
            olds_all.add(en)
        # опции портретного меню дат задаются вручную (не в строках скрипта)
        olds_all.add('Go on a date with Henrietta')
        # варианты без тега (строки могли быть с тегом в прошлом прогоне)
        for o in list(olds_all):
            olds_all.add(re.sub(r'\{#ch4\.6_[a-z]\d+\}$', '', o))
        for (lang, bucket), path in TL.items():
            if not os.path.exists(path):
                continue
            txt = io.open(path, encoding='utf-8').read()
            decl = LANG_DECL[lang]
            parts = txt.split('translate %s strings:\n' % decl)
            head, rest = parts[0], parts[1:]
            kept, removed = [], 0
            for b in rest:
                m = re.search(r'^\s*old\s+"(.*)"\s*$', b, re.M)
                if m and (m.group(1) in olds_all or re.search(r'\{#ch4\.6_[a-z]', m.group(1))):
                    removed += 1
                    continue
                kept.append(b)
            out = head + ''.join('translate %s strings:\n' % decl + b for b in kept)
            io.open(path, 'w', encoding='utf-8').write(out)
            print('removed from %s: %d' % (os.path.relpath(path, ROOT), removed))

    # опция портретного меню дат (в сценарии — список portrait_choice,
    # не обычный menu:): добавляется вручную, в оба языка
    add('choises', 'Go on a date with Henrietta',
        'アンリエッタとデートをします', 'Пойти на свидание с Анриеттой')

    # проверка коллизий old с уже существующими в tl
    for (lang, bucket), path in TL.items():
        if not os.path.exists(path):
            continue
        have = existing_olds(path)
        seen = set()
        for en, _ja in blocks[(lang, bucket)]:
            if en in have:
                problems.append('дубль old в tl/%s: %s' % (lang, en[:60]))
            if en in seen:
                problems.append('дубль old внутри части (tl/%s): %s' % (lang, en[:60]))
            seen.add(en)

    if problems:
        print('\nПРОБЛЕМЫ: %d' % len(problems))
        for p in problems[:40]:
            print('  -', p)
    else:
        print('\nколлизий нет')

    if args.apply and not problems:
        for (lang, bucket), path in TL.items():
            with io.open(path, 'a', encoding='utf-8') as fh:
                for en, new in blocks[(lang, bucket)]:
                    fh.write('translate %s strings:\n' % LANG_DECL[lang])
                    fh.write('    old "%s"\n' % en.replace('"', '\\"'))
                    fh.write('    new "%s"\n\n' % new.replace('"', '\\"'))
            print('written: %s (+%d)' % (os.path.relpath(path, ROOT), len(blocks[(lang, bucket)])))
    elif args.apply:
        print('\nНЕ ЗАПИСАНО: есть проблемы')


if __name__ == '__main__':
    main()
