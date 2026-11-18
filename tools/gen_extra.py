#!/usr/bin/env python3
"""Generic generator for a group of extra (tsundere/dere) scenes.

Usage: python tools/gen_extra.py <chapter_90|chapter_91> <out_prefix> <scene_no...>

Reads reports/extra/parse_<90|91>.json, emits:
  game/chapters/extra/<out_prefix>.rpy
  game/tl/japanese/<out_prefix>_dialogs.rpy
  game/tl/russian/<out_prefix>_dialogs.rpy
  reports/extra/voice_map_<out_prefix>.csv
Translations are supplied via <out_prefix>_t.json next to this script:
  {"<idx>": ["EN", "RU"], ...}  keyed by a running dlg index within the group.
"""
import json
import os
import sys

sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

CHAPTER_FILE = {'chapter_90': 'reports/extra/parse_90.json', 'chapter_91': 'reports/extra/parse_91.json'}


def main():
    chapter, prefix = sys.argv[1], sys.argv[2]
    nums = [int(n) for n in sys.argv[3:]]
    data = json.load(open(CHAPTER_FILE[chapter], encoding='utf-8'))
    trans_path = 'tools/%s_t.json' % prefix
    trans = json.load(open(trans_path, encoding='utf-8')) if os.path.exists(trans_path) else {}
    scenes = [s for s in data['scenes'] if s['no'] in nums]
    lines = ['# Extra event (%s), scenes %s.' % (chapter, ','.join(map(str, nums))),
             '# Источник: ps2_source/chapters/%s.txt' % chapter, '',
             'label %s:' % prefix, '    $ tndl(None)', '    $ show_sprites()', '']
    ja_d, ru_d = [], []
    manifest = []
    idx = 0
    for s in scenes:
        lines.append('label %s_scene_%d:' % (prefix, s['no']))
        lines.append('')
        for it in s['items']:
            k = it['kind']
            if k == 'event':
                event(it['src'], lines)
            elif k == 'dlg':
                en, ru = trans.get(str(idx), (None, None))
                if en is None:
                    lines.append('    # NO TRANSLATION idx %d: %s' % (idx, it['ja'][:60]))
                    idx += 1
                    continue
                en = en_norm(en)
                tag = '%s_d_%03d' % (prefix, idx)
                full = '%s{#%s}' % (en, tag)
                lines.append('    # ' + it['ja'][:60].replace('\n', ' '))
                if it['voice'] is not None:
                    lines.append('    voice "%s"' % tag)
                    manifest.append((tag, it['voice']))
                spk = 'th' if it['thought'] else ('s' if it['speaker'] == 'サイト'
                      else 'l' if it['speaker'] == 'ルイズ' else 'k' if it['speaker'] == 'キュルケ'
                      else 'si' if it['speaker'] == 'シエスタ' else 't' if it['speaker'] == 'タバサ'
                      else 'h' if it['speaker'] == 'アンリエッタ' else 'th')
                lines.append('    %s "%s"' % (spk, full))
                ja_new = it['ja'] if it['thought'] else '%s：%s' % (it['speaker'], it['ja'])
                ja_d += ['    old "%s"' % full, '    new "%s"' % ja_new, '']
                ru_d += ['    old "%s"' % full, '    new "%s"' % ru, '']
                lines.append('')
                idx += 1
            elif k == 'choice':
                en, ru = trans.get('c%d_%d' % (s['no'], it['target']), (None, None))
                if en is None:
                    lines.append('    # CHOICE NO TRANSLATION: ' + it['text'])
                    continue
                ctext = '%s{#%s_c_%d_%d}' % (en_norm(en), prefix, s['no'], it['target'])
                lines.append('        "%s":' % ctext)
                lines.append('            jump %s_scene_%d' % (prefix, it['target']))
                ja_c = None
                ja_d += ['    old "%s"' % ctext, '    new "%s"' % it['text'], '']
                ru_d += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            elif k == 'goto':
                lines.append('    # → next scene %d' % it['target'])
                lines.append('    jump %s_scene_%d' % (prefix, it['target']))
                lines.append('')
            elif k == 'like':
                lines.append('    # 【好感度】%s %d (update_sympathy not in source)' % (it['speaker'], it['value']))
    lines.append('    return')
    files = {
        'game/chapters/extra/%s.rpy' % prefix: '\n'.join(lines) + '\n',
        'game/tl/japanese/%s_dialogs.rpy' % prefix: '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/%s_dialogs.rpy' % prefix: '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/extra/voice_map_%s.csv' % prefix, 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), 'dialogs', idx)


if __name__ == '__main__':
    main()
