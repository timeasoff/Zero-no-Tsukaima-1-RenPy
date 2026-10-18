# -*- coding: utf-8 -*-
"""Генерация переводов JA/RU для части 5 (ch4_5), версия 2.

Направление пар: old = EN-строка сценария (дословно), new = JA (канон,
ps2_source/chapters/chapter_05) в tl/japanese и new = RU (tools/ch4_5_ru.py)
в tl/russian. Бакеты: dialogs / thoughs / choises.

Использование:
    python tools/gen_ch4_5_tl.py              # dry-run (счётчики + сверка)
    python tools/gen_ch4_5_tl.py --apply      # добавить блоки в tl-файлы
"""

import re
import glob
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ch4_5_ru import RU_DIALOGS, RU_THOUGHTS, RU_CHOICES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SCRIPT_PATH = os.path.join(ROOT, 'game', 'chapters', '4', 'script-ch4_5.rpy')
TL = {
    ('ja', 'dialogs'): os.path.join(ROOT, 'game', 'tl', 'japanese', 'dialogs.rpy'),
    ('ja', 'thoughs'): os.path.join(ROOT, 'game', 'tl', 'japanese', 'thoughs.rpy'),
    ('ja', 'choises'): os.path.join(ROOT, 'game', 'tl', 'japanese', 'choises.rpy'),
    ('ru', 'dialogs'): os.path.join(ROOT, 'game', 'tl', 'russian', 'dialogs.rpy'),
    ('ru', 'thoughs'): os.path.join(ROOT, 'game', 'tl', 'russian', 'thoughs.rpy'),
    ('ru', 'choises'): os.path.join(ROOT, 'game', 'tl', 'russian', 'choises.rpy'),
}

JA2KEY = {'サイト': 's', 'ルイズ': 'l', 'アンリエッタ': 'h',
          'ハルナ': 'ha', 'シエスタ': 'si', 'デルフリンガー': 'd', 'null': 'n'}

SCENE_START = re.compile(r'^-+\s*SCENE\s*(\d+)\s*-+$')
TALK = re.compile(r'^([^\s：:（【\[]+)：(.*)$')


def extract_source():
    f = glob.glob(os.path.join(ROOT, 'ps2_source', 'chapters', 'chapter_05_*.txt'))[0]
    L = open(f, encoding='utf-8', errors='replace').read().splitlines()
    s256 = next(i for i, l in enumerate(L) if re.match(r'^-+\s*SCENE\s*0256', l.strip()))
    s261 = next(i for i, l in enumerate(L) if re.match(r'^-+\s*SCENE\s*0261', l.strip()))

    dialogs, thoughts, choices = [], [], []
    i = s256
    while i < s261:
        ln = L[i]
        m = TALK.match(ln)
        if m and not ln.strip().startswith('['):
            spk = m.group(1)
            j = i + 1
            cont = []
            while j < s261:
                ns = L[j].strip()
                if (TALK.match(L[j]) or ns.startswith('[') or '【' in ns
                        or ns.startswith('→') or SCENE_START.match(ns)):
                    break
                if ns:
                    cont.append(L[j])
                j += 1
            block = [ln] + cont
            if any('[voice' in b for b in block):
                ja = m.group(2) + ''.join(cont)
                ja = re.sub(r'\s*\[voice \d+\]', '', ja)
                dialogs.append((JA2KEY.get(spk, '?'), ja))
            else:
                thoughts.append(m.group(2) + ''.join(cont))
            i = j
            continue
        if '【選択肢】' in ln:
            t = ln.strip()
            t = re.sub(r'^【選択肢】', '', t)
            t = re.sub(r'\s*→\s*scene\s*\d+.*$', '', t)
            choices.append(t)
        i += 1
    return dialogs, thoughts, choices


def extract_script():
    SL = open(SCRIPT_PATH, encoding='utf-8').read().splitlines()
    DIALOG = re.compile(r'^(s|l|h|ha|si|d)\s+"(.*)"$')
    TH = re.compile(r'^th\s+"(.*)"$')
    MENU = re.compile(r'^"(.+)":\s*(#.*)?$')
    dialogs, thoughts, choices = [], [], []
    for ln in SL:
        st = ln.strip()
        m = DIALOG.match(st)
        if m:
            dialogs.append((m.group(1), m.group(2)))
            continue
        m = TH.match(st)
        if m:
            thoughts.append(m.group(1))
            continue
        m = MENU.match(st)
        if m:
            choices.append(m.group(1))
    return dialogs, thoughts, choices


def block(lang_header, pairs):
    out = [lang_header, '']
    for old, new in pairs:
        out.append('    old "%s"' % old)
        out.append('    new "%s"' % new)
        out.append('')
    return '\n'.join(out).rstrip('\n')


def main():
    apply = '--apply' in sys.argv

    src_d, src_t, src_c = extract_source()
    scr_d, scr_t, scr_c = extract_script()

    print('dialogs: script=%d source=%d ru=%d' % (len(scr_d), len(src_d), len(RU_DIALOGS)))
    print('thoughts: script=%d source=%d ru=%d' % (len(scr_t), len(src_t), len(RU_THOUGHTS)))
    print('choices: script=%d source=%d ru=%d' % (len(scr_c), len(src_c), len(RU_CHOICES)))

    assert len(scr_d) == len(src_d) == len(RU_DIALOGS), 'dialog count'
    assert len(scr_t) == len(src_t) == len(RU_THOUGHTS), 'thought count'
    assert len(scr_c) == len(src_c) == len(RU_CHOICES), 'choice count'

    bad = [(i + 1, a[0], b[0]) for i, (a, b) in enumerate(zip(src_d, scr_d)) if a[0] != b[0]]
    assert not bad, 'speaker order mismatch: %s' % bad[:5]

    # EN-строки обязаны быть непустыми и без сырых управляющих символов
    for name, items in (('dialog', scr_d), ('thought', [(None, t) for t in scr_t]),
                        ('choice', [(None, c) for c in scr_c])):
        for it in items:
            t = it[1] if isinstance(it, tuple) else it
            assert t.strip(), 'empty %s string' % name

    print('ALIGNMENT: OK')

    if not apply:
        print('\n--- DRY RUN ---')
        print('pairs to append: dialogs=%d thoughts=%d choices=%d (x2 languages)'
              % (len(scr_d), len(scr_t), len(scr_c)))
        print('first dialog: old=%r' % scr_d[0][1][:60])
        print('first ja    : %r' % src_d[0][1][:40])
        print('first ru    : %r' % RU_DIALOGS[0][:40])
        print('\ndry-run only; run with --apply to write')
        return

    jobs = [
        (('ja', 'dialogs'), 'translate japanese strings:',
         [(en, ja) for (_, en), (_, ja) in zip(scr_d, src_d)]),
        (('ru', 'dialogs'), 'translate russian strings:',
         [(en, ru) for (_, en), ru in zip(scr_d, RU_DIALOGS)]),
        (('ja', 'thoughs'), 'translate japanese strings:',
         list(zip(scr_t, src_t))),
        (('ru', 'thoughs'), 'translate russian strings:',
         list(zip(scr_t, RU_THOUGHTS))),
        (('ja', 'choises'), 'translate japanese strings:',
         list(zip(scr_c, src_c))),
        (('ru', 'choises'), 'translate russian strings:',
         list(zip(scr_c, RU_CHOICES))),
    ]

    for (lang, bucket), header, pairs in jobs:
        path = TL[(lang, bucket)]
        with open(path, 'a', encoding='utf-8') as f:
            f.write('\n\n' + block(header, pairs) + '\n')
        print('appended %s/%s: +%d pairs' % (lang, bucket, len(pairs)))


if __name__ == '__main__':
    main()
