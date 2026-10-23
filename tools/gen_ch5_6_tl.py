# -*- coding: utf-8 -*-
"""Запись old/new для части ch5.6 в game/tl/japanese и game/tl/russian.

old — EN-строка сценария (tools/ch5_6_en.py, через mapping6),
new — RU (tools/ch5_6_ru.py) / JA (из events-источника).

Глубинный-first порядок (CHAINS): сцены 335 -> 1408..1428.
Мысли: 4 core (335) + 17 extra = 21 (th_001..th_021).
Голоса: 127, по говорящему с 001.

Формат tl/{japanese,russian}/ch5_6_*.rpy — плоские бакеты (как в 0/1):
  translate <lang> strings: old "EN" / new "JA/RU", маркеры # ===== ch5.6.

Использование:
    python tools/gen_ch5_6_tl.py --apply
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'ps2_source', 'events_full',
                   'chapter_06_本当の想い.txt')

SCENES_335 = 335
CHAINS = [
    [1408, 1409, 1410, 1411, 1412],
    [1413, 1414, 1415, 1416, 1417],
    [1418, 1419, 1420, 1421, 1422],
    [1423, 1424, 1425, 1426, 1427],
    [1428],
]
ORDER = [s for ch in CHAINS for s in ch]

SPK = {'サイト': 's', 'ルイズ': 'l', 'ハルナ': 'ha', 'シエスタ': 'si',
       'キュルケ': 'k', 'タバサ': 't', 'ギーシュ': 'g',
       'モンモランシー': 'm', 'ウェザリー': 'w', 'アンリエッタ': 'h',
       'null': 'th'}

RE_TALK = re.compile(r'^DIALOGUE\s+talk\((.*)\)\s*$')
RE_CHOICE = re.compile(
    r'^CHOICE\s+selectItem\("((?:[^"\\]|\\.)*)",\s*'
    r'\(0x01000000 \+(\d+)\).*$')
RE_MAPDEST = re.compile(
    r'^MAPDEST\s+moveItem\("([^"]*)",\s*\(0x02000000 \+\d+\),\s*'
    r'\(0x01000000 \+(\d+)\)\)')
SPLIT_ARGS = re.compile(
    r'"((?:[^"\\]|\\.)*)"|(\bnull\b)|\(0x0[46]000000 \+(\d+)\)')


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
    scenes = {}
    cur = None
    included = set(ORDER) | {SCENES_335}
    for ln in io.open(SRC, encoding='utf-8'):
        ln = ln.rstrip('\n')
        m = re.match(r'^## SCENE (\d+)', ln)
        if m:
            cur = int(m.group(1))
            scenes.setdefault(cur, [])
            continue
        if cur not in included:
            continue
        ev = scenes[cur]
        m = RE_TALK.match(ln)
        if m:
            spk, disp, text, vid = parse_args(m.group(1))
            ev.append(('talk', spk, disp, text or '', vid))
            continue
        m = RE_CHOICE.match(ln)
        if m:
            ev.append(('choice', m.group(1), int(m.group(2))))
            continue
    return scenes


def load_mappings():
    sys.path.insert(0, ROOT)
    sys.path.insert(0, os.path.join(ROOT, '.tmp'))
    import mapping6
    from ch5_6_en import EN_DIALOGS, EN_THOUGHTS, EN_CHOICES
    from ch5_6_ru import RU_DIALOGS, RU_THOUGHTS, RU_CHOICES
    return (mapping6.VOICE_MAP, mapping6.THOUGHT_MAP, mapping6.CHOICE_MAP,
            mapping6.FRESH_IN_PIN, EN_DIALOGS, EN_THOUGHTS, EN_CHOICES,
            RU_DIALOGS, RU_THOUGHTS, RU_CHOICES)


def _resolve_dlg(vn, DIALOGS, VOICE_MAP, FRESH_IN_PIN, lang):
    """lang='en' -> EN, 'ru' -> RU."""
    rec = VOICE_MAP.get(vn, ('old', vn))
    if rec[0] == 'old':
        return DIALOGS.get(rec[1])
    if rec[0] == 'merge':
        parts = []
        for k in rec[1]:
            e = DIALOGS.get(k)
            if e:
                parts.append(e.replace('\n', ' '))
        return ' '.join(parts) if parts else None
    if rec[0] == 'fresh':
        return rec[1][1 if lang == 'ru' else 0]
    return DIALOGS.get(vn)


def resolve_th(tag, THOUGHTS, THOUGHT_MAP):
    rec = THOUGHT_MAP.get(tag, ('old', tag))
    if rec[0] == 'old':
        return THOUGHTS.get(rec[1])
    return THOUGHTS.get(tag)


def resolve_choice(target, CHOICES, CHOICE_MAP):
    rec = CHOICE_MAP.get(str(target), ('old', str(target)))
    if rec[0] == 'old':
        return CHOICES.get(rec[1])
    return CHOICES.get(str(target))


def write_bucket(items, lang, fn):
    lines = ['translate %s strings:' % lang,
             '# ===== ch5.6: %d strings =====' % len(items)]
    for old, new in items:
        esc_old = old.replace('\\', '\\\\').replace('"', '\\"')
        esc_new = new.replace('\\', '\\\\').replace('"', '\\"')
        lines.append('')
        lines.append('    old "%s"' % esc_old)
        lines.append('    new "%s"' % esc_new)
    lines.append('# ===== end ch5.6 =====')
    with io.open(fn, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print('  %-9s %-24s %d entries' % (lang, os.path.relpath(fn, ROOT),
                                       len(items)))


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    (VOICE_MAP, THOUGHT_MAP, CHOICE_MAP, FRESH_IN_PIN,
     EN_DIALOGS, EN_THOUGHTS, EN_CHOICES,
     RU_DIALOGS, RU_THOUGHTS, RU_CHOICES) = load_mappings()

    scenes = parse_events()
    missing = []

    # ---- voice_idx: voice_name -> (sc, i) в порядке CHAINS (depth-first)
    voice_idx = {}
    cnt = {}
    for sc in ORDER:
        for i, e in enumerate(scenes.get(sc, [])):
            if e[0] == 'talk' and e[4] is not None:
                key = SPK.get(e[1], 'x')
                cnt[key] = cnt.get(key, 0) + 1
                vn = 'ch5.6_%s_%03d' % (key, cnt[key])
                voice_idx[vn] = (sc, i)

    # ---- мысли: th_001..004 = core 335, th_005..021 = extra depth-first
    thought_map_pos = {}   # 'ch5.6_th_NNN' -> (sc, i)
    tn = 0
    for i, e in enumerate(scenes.get(SCENES_335, [])):
        if e[0] == 'talk' and e[4] is None:
            tn += 1
            thought_map_pos['ch5.6_th_%03d' % tn] = (SCENES_335, i)
    for sc in ORDER:
        for i, e in enumerate(scenes.get(sc, [])):
            if e[0] == 'talk' and e[4] is None:
                tn += 1
                thought_map_pos['ch5.6_th_%03d' % tn] = (sc, i)

    JAP = {'dialogs': [], 'thoughs': [], 'choises': []}
    RU = {'dialogs': [], 'thoughs': [], 'choises': []}

     # ---- диалоги (в порядке voice_idx = depth-first) ----
    for vn in sorted(voice_idx, key=lambda n: voice_idx[n]):
        sc, i = voice_idx[vn]
        text = scenes[sc][i][3]
        vid = scenes[sc][i][4]
        en = _resolve_dlg(vn, EN_DIALOGS, VOICE_MAP, FRESH_IN_PIN, 'en')
        ja = text.replace('\n', ' ')
        if not en:
            missing.append(('dialog', vn, text))
            continue
        old = en.replace('\n', ' ').strip() + '{#ch5_6_v%s}' % vid
        JAP['dialogs'].append((old, ja))
        ru = _resolve_dlg(vn, RU_DIALOGS, VOICE_MAP, FRESH_IN_PIN, 'ru')
        if ru:
            RU['dialogs'].append((old, ru.replace('\n', ' ').strip()))
        else:
            missing.append(('dialog_ru', vn, en))

    # ---- мысли (th_001..th_021) ----
    for tag in sorted(thought_map_pos, key=lambda t: int(t.split('_')[-1])):
        sc, i = thought_map_pos[tag]
        ja = scenes[sc][i][3].replace('\n', ' ')
        en = resolve_th(tag, EN_THOUGHTS, THOUGHT_MAP)
        if not en:
            missing.append(('thought', tag, ja))
            continue
        old = en.replace('\n', ' ').strip() + '{#%s}' % tag
        JAP['thoughs'].append((old, ja))
        ru = resolve_th(tag, RU_THOUGHTS, THOUGHT_MAP)
        if ru:
            RU['thoughs'].append((old, ru.replace('\n', ' ').strip()))
        else:
            missing.append(('thought_ru', tag, en))

    # ---- выборы (choices) ----
    # location choices из SCENE 335 MAPDEST
    loc_map = {}
    for ln in io.open(SRC, encoding='utf-8'):
        m = RE_MAPDEST.match(ln.rstrip('\n'))
        if m:
            loc_map[int(m.group(2))] = m.group(1)

    # 5 location choices (depth-first: 1408,1413,1418,1423,1428)
    for target in [1408, 1413, 1418, 1423, 1428]:
        ja = loc_map.get(target, '')
        en = resolve_choice(target, EN_CHOICES, CHOICE_MAP)
        if not en:
            missing.append(('choice_loc', str(target), ja))
            continue
        old = en.replace('\n', ' ').strip() + '{#ch5_6_c%s}' % target
        JAP['choises'].append((old, ja))
        ru = resolve_choice(target, RU_CHOICES, CHOICE_MAP)
        if ru:
            RU['choises'].append((old, ru.replace('\n', ' ').strip()))
        else:
            missing.append(('choice_loc_ru', str(target), en))

    # mini-menu choices: CHOICE selectItem events (depth-first по CHAINS)
    seen = set()
    for sc in ORDER:
        for e in scenes.get(sc, []):
            if e[0] == 'choice':
                tgt = e[2]
                if tgt in seen:
                    continue
                seen.add(tgt)
                ja = e[1]
                en = resolve_choice(tgt, EN_CHOICES, CHOICE_MAP)
                if not en:
                    missing.append(('choice_mini', str(tgt), ja))
                    continue
                old = en.replace('\n', ' ').strip() + '{#ch5_6_c%s}' % tgt
                JAP['choises'].append((old, ja))
                ru = resolve_choice(tgt, RU_CHOICES, CHOICE_MAP)
                if ru:
                    RU['choises'].append((old, ru.replace('\n', ' ').strip()))
                else:
                    missing.append(('choice_mini_ru', str(tgt), en))

    # ---- output ----
    print('JAP: dialogs=%d thoughs=%d choises=%d' %
          (len(JAP['dialogs']), len(JAP['thoughs']), len(JAP['choises'])))
    print('RU : dialogs=%d thoughs=%d choises=%d' %
          (len(RU['dialogs']), len(RU['thoughs']), len(RU['choises'])))

    if missing:
        print('\nMISSING: %d' % len(missing))
        for kind, key, val in missing[:40]:
            print('  %-12s %-14s %s' % (kind, key, val.replace('\\n', ' / ')[:50]))
    else:
        print('\nall translations present')

    if args.apply:
        base = os.path.join(ROOT, 'game', 'tl')
        write_bucket(JAP['dialogs'], 'japanese',
                     os.path.join(base, 'japanese', 'ch5_6_dialogs.rpy'))
        write_bucket(JAP['thoughs'], 'japanese',
                     os.path.join(base, 'japanese', 'ch5_6_thoughts.rpy'))
        write_bucket(JAP['choises'], 'japanese',
                     os.path.join(base, 'japanese', 'ch5_6_choises.rpy'))
        write_bucket(RU['dialogs'], 'russian',
                     os.path.join(base, 'russian', 'ch5_6_dialogs.rpy'))
        write_bucket(RU['thoughs'], 'russian',
                     os.path.join(base, 'russian', 'ch5_6_thoughts.rpy'))
        write_bucket(RU['choises'], 'russian',
                     os.path.join(base, 'russian', 'ch5_6_choises.rpy'))
        print('\nwritten: game/tl/{japanese,russian}/ch5_6_*.rpy')


if __name__ == '__main__':
    main()
