#!/usr/bin/env python3
"""Generate ch11 parts 3/4 script + TL + voice-map fragment from parsed source.

Usage: python tools/gen_ch11_p34_script.py
Inputs: reports/ch11/parse_478_499.json, parse_500_1178.json, tools/ch11_p34_trans.py
Outputs: game/chapters/11/script-ch11_{3,4}.rpy,
         game/tl/{japanese,russian}/ch11_{3,4}_{dialogs,choises}.rpy,
         reports/ch11/voice_map_3_4.csv
"""
import json
import os
import re
import sys

sys.path.insert(0, 'tools')
from ch11_p34_trans import P3, P4, C3, C4

BG_NAMED = {10: 'louise_room', 17: 'hallway_down', 26: 'yard',
            47: 'cafe_entrance', 59: 'town_square_evening', 88: 'sky',
            2: 'white', 32: 'kitchen', 23: 'classroom', 85: 'forest',
            54: 'theater_backstage'}

SPK = {'サイト': 's', 'ルイズ': 'l', 'キュルケ': 'k', 'タバサ': 't',
       'シエスタ': 'si', 'ハルナ': 'ha', 'ウェザリー': 'w',
       'アキナ': 'ak', '魔導士': 'mage', 'null': 'th'}

# Per-speaker tag counters carried over from part 2 (last used).
START = {'s': 40, 'ha': 32, 'l': 13, 'si': 16, 'k': 6,
         't': 1, 'w': 7, 'ak': 1, 'mage': 1, 'th': 1}


def en_norm(s):
    """PROMTS.md п.5: многоточие в EN — символ '…', не три точки."""
    return re.sub(r'\.{3,}', '…', s) if s else s


def bg_name(i):
    return BG_NAMED.get(i, 'id(%d)' % i)


def event_line(src, out):
    """Translate one bracketed source event into a comment + optional call."""
    out.append('    # ' + src)
    m = re.search(r'\[BG +stage +image=\+(\d+)', src)
    if m:
        out.append('    $ fade_fx("%s")' % bg_name(int(m.group(1))))
        return
    m = re.search(r'\[EVENT_CG +event +image=\+(\d+)', src)
    if m:
        out.append('    $ dissolve_fx("id(%d)")' % int(m.group(1)))
        return
    m = re.search(r'\[BGM +bgm +play=\+(\d+)', src)
    if m:
        out.append('    play music t%d fadein 1.0' % (int(m.group(1)) - 1))
        return
    if '[BGM' in src and 'stop=' in src:
        out.append('    stop music fadeout 1.0')
        return
    if '[LAYER' in src and 'white' in src and 'hide' not in src:
        out.append('    $ flash_fx("white")')
        return
    if '[COFFEE]' in src:
        out.append('    $ pause(1.0)')


def label_for(target, part):
    if part == 3:
        if target == 500:
            return 'ch11_4'
        if 478 <= target <= 499:
            return 'ch11_3_scene_%d' % target
    else:
        if 500 <= target <= 509:
            return 'ch11_4_scene_%d' % target
    return None


def generate(part, parse_file, trans, choices, counters, start_scene, end_scene):
    data = json.load(open(parse_file, encoding='utf-8'))
    script = []
    tl_ja_d, tl_ru_d = [], []
    tl_ja_c, tl_ru_c = [], []
    manifest = []
    cur_scene = None
    date_jumped = None

    script += [
        '# Глава 11, часть %d (сцены %d-%d): «ハルナの決意» — продолжение.' % (
            part, start_scene, end_scene),
        '# Источник: ps2_source/chapters/chapter_12_ハルナの決意.txt '
        '(SCENE %d-%d).' % (start_scene, end_scene),
        '# Точные аргументы: ps2_source/events_full/chapter_12_ハルナの決意.txt.',
        '# EN-база в сценарии; JA/RU — в game/tl/{japanese,russian}/ch11_%d_*.rpy.' % part,
        '# Голоса: нумерация ch11_<spk>_<NNN> продолжает части 1-2 (общая нумерация главы).',
        '',
        'label ch11_%d:' % part,
        '    $ tndl(None)',
        '    $ show_sprites()',
        '',
    ]

    for x in data:
        k = x['kind']
        if k == 'scene':
            cur_scene = x['no']
            date_jumped = None
            script += ['label ch11_%d_scene_%d:' % (part, cur_scene), '']
            continue
        if k == 'event':
            event_line(x['src'], script)
            continue
        if k == 'dlg':
            idx = x['idx']
            en, ru = trans[idx]
            en = en_norm(en)
            spk = SPK.get(x['speaker'], 'th')
            if en is None:
                script.append('    # ' + x['src'] + '  (no voice — пропущено по образцу ch11_2)')
                continue
            counters[spk] += 1
            tag = 'ch11_%s_%03d' % (spk, counters[spk])
            full = '%s{#%s}' % (en, tag)
            script.append('    # ' + x['src'])
            ja_new = ('%s：%s' % (x['speaker'], x['ja'])
                      if not x['thought'] else x['ja'])
            if x['voice'] is not None:
                vname = tag
                script.append('    voice "%s"' % vname)
                manifest.append((vname, x['voice']))
            script.append('    %s "%s"' % (spk, full))
            tl_ja_d += ['    old "%s"' % full, '    new "%s"' % ja_new, '']
            tl_ru_d += ['    old "%s"' % full, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'choice':
            opts = choices[cur_scene]
            script.append('    menu:')
            for i, o in enumerate(x['options']):
                en, ru = opts[i]
                ctext = '%s{#ch11_%d_c_%d_%d}' % (en_norm(en), part, cur_scene, i + 1)
                tgt = label_for(o['target'], part)
                script.append('        "%s":' % ctext)
                script.append('            jump %s' % (tgt or 'attention'))
                tl_ja_c += ['    old "%s"' % ctext,
                            '    new "%s"' % o['text'], '']
                tl_ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            tgt = label_for(x['target'], part)
            if tgt:
                script.append('    # → next scene %d' % x['target'])
                script.append('    jump %s' % tgt)
            else:
                script.append('    # → next scene %d (вне части)' % x['target'])
            script.append('')
            continue
        if k == 'date':
            script.append('    # 【デート%s】%s → scene %s — не портируется '
                          '(date-гейт, контент в game/chapters/extra/)' % (
                              x['kind2'], x['text'], x['target']))
            if date_jumped != cur_scene and label_for(x['target'], part) is None:
                script.append('    # → jump attention (конец портированного контента)')
                script.append('    jump attention')
                date_jumped = cur_scene
            continue

    script += ['    # ==== КОНЕЦ ГЛАВЫ 11, ЧАСТИ %d ====' % part,
               '    jump attention', '    return', '']

    lang = lambda rows, name, hdr: '\n'.join(
        ['# translate %s strings:' % name,
         '# (ch11_%d: scenes %d-%d)' % (part, start_scene, end_scene), ''] + rows) + '\n'
    files = {
        'game/chapters/11/script-ch11_%d.rpy' % part: '\n'.join(script) + '\n',
        'game/tl/japanese/ch11_%d_dialogs.rpy' % part: lang(tl_ja_d, 'japanese', ''),
        'game/tl/japanese/ch11_%d_choises.rpy' % part: lang(tl_ja_c, 'japanese', ''),
        'game/tl/russian/ch11_%d_dialogs.rpy' % part: lang(tl_ru_d, 'russian', ''),
        'game/tl/russian/ch11_%d_choises.rpy' % part: lang(tl_ru_c, 'russian', ''),
    }
    for path, body in files.items():
        with open(path, 'w', encoding='utf-8') as f:
            f.write(body)
        print('wrote', path, len(body), 'bytes')
    return manifest


def main():
    counters = dict(START)
    m3 = generate(3, 'reports/ch11/parse_478_499.json', P3, C3,
                  counters, 478, 499)
    m4 = generate(4, 'reports/ch11/parse_500_1178.json', P4, C4,
                  counters, 500, 509)
    with open('reports/ch11/voice_map_3_4.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in m3 + m4:
            f.write('%s,%d\n' % (v, i))
    print('manifest rows', len(m3) + len(m4), '(p3', len(m3), 'p4', len(m4), ')')
    print('final counters', counters)


if __name__ == '__main__':
    main()
