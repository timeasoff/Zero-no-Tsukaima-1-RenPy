#!/usr/bin/env python3
"""Port all scenes of chapter_90/91 to a single extra file.

Translations are read from reports/extra/trans_<90|91>.json keyed by:
  "d<voice_id>"            -> [EN, RU]   (for voiced dialogue, unique per PS2 voice id)
  "s<scene>_<ord>"         -> [EN, RU]   (for dialogue with no voice)
  "c<scene>_<target>"      -> [EN, RU]   (for choice labels)

Usage: python tools/gen_extra_all.py <chapter_90|chapter_91> <prefix>
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

PARSE = {'chapter_90': 'reports/extra/parse_90.json', 'chapter_91': 'reports/extra/parse_91.json'}
# scenes already ported into separate sp_*.rpy files -> skip them and route jumps there
PORTED = {'chapter_91': {1700, 1725, 1726, 1727, 1728, 1729, 1730, 1731, 1732}, 'chapter_90': set()}
PORTED_PREFIX = {1700: 'sp_d1', 1725: 'sp_d1', 1726: 'sp_d1', 1727: 'sp_d1',
                 1728: 'sp_d1', 1729: 'sp_d1', 1730: 'sp_d1', 1731: 'sp_d1', 1732: 'sp_d1'}
TRANS = {'chapter_90': 'reports/extra/trans_90.json', 'chapter_91': 'reports/extra/trans_91.json'}
OUT = {'chapter_90': 'sp90', 'chapter_91': 'sp91'}
# voice ids without a source .wav: dialogue kept, `voice` line omitted
NO_AUDIO = re.compile(r'^\|\s*sp91_\S+\s*\|\s*(\d+)\s*\|', re.M)


def no_audio_ids():
    p = Path(__file__).parent.parent / 'reports/extra/no_audio_ch91.md'
    if not p.exists():
        return set()
    return set(int(x) for x in NO_AUDIO.findall(p.read_text(encoding='utf-8')))


def main():
    chapter = sys.argv[1]
    prefix = OUT[chapter]
    data = json.load(open(PARSE[chapter], encoding='utf-8'))
    trans = json.load(open(TRANS[chapter], encoding='utf-8'))
    lines = ['# Extra event chapter (%s), all scenes.' % chapter,
             '# Источник: ps2_source/chapters/%s.txt' % chapter, '']
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    missing = []
    no_audio = no_audio_ids()
    in_menu = False
    for si, s in enumerate(data['scenes']):
        if s['no'] in PORTED.get(chapter, set()):
            continue
        lines.append('label %s_scene_%d:' % (prefix, s['no']))
        lines.append('')
        for item_i, it in enumerate(s['items']):
            k = it['kind']
            if in_menu and k != 'choice':
                in_menu = False
                lines.append('')
            if k == 'event':
                event(it['src'], lines)
            elif k == 'dlg':
                key = ('d%d' % it['voice']) if it['voice'] is not None else 's%d_0' % s['no']
                key_new = 's%d_%d' % (s['no'], item_i)
                pair = trans.get(key_new) or trans.get(key)
                if pair is None:
                    missing.append(key + '/' + key_new)
                    lines.append('    # MISSING %s: %s' % (key, it['ja'][:50].replace('\n', ' ')))
                    continue
                en, ru = en_norm(pair[0]), pair[1]
                tag = '%s_%03d' % (prefix, si)  # tag per scene, not per dlg (tags unique anyway)
                tag = '%s_s%d_%03d' % (prefix, s['no'], item_i)
                full = '%s{#%s}' % (en, tag)
                lines.append('    # ' + it['ja'][:55].replace('\n', ' '))
                if it['voice'] is not None and it['voice'] not in no_audio:
                    lines.append('    voice "%s"' % tag)
                    manifest.append((tag, it['voice']))
                spk = 'th' if it['thought'] else {'サイト': 's', 'ルイズ': 'l', 'キュルケ': 'k',
                       'シエスタ': 'si', 'タバサ': 't', 'アンリエッタ': 'h', 'ハルナ': 'ha',
                       'コルベール': 'c', ' null': 'th'}.get(it['speaker'], 'th')
                lines.append('    %s "%s"' % (spk, full))
                ja_new = it['ja'] if it['thought'] else '%s：%s' % (it['speaker'], it['ja'])
                ja_d += ['    old "%s"' % full, '    new "%s"' % ja_new, '']
                ru_d += ['    old "%s"' % full, '    new "%s"' % ru, '']
                lines.append('')
            elif k == 'choice':
                if not in_menu:
                    lines.append('')
                    lines.append('    menu:')
                    in_menu = True
                key = 'c%d_%d' % (s['no'], it['target'])
                pair = trans.get(key)
                if pair is None:
                    missing.append(key)
                    lines.append('        # MISSING CHOICE ' + key)
                    continue
                en, ru = en_norm(pair[0]), pair[1]
                ctext = '%s{#%s_c_%d_%d}' % (en, prefix, s['no'], it['target'])
                lines.append('        "%s":' % ctext)
                lines.append('            jump %s_scene_%d' % (prefix, it['target']))
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % it['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            elif k == 'goto':
                if in_menu:
                    in_menu = False
                    lines.append('')
                t = it['target']
                lines.append('    # → next scene %d' % t)
                self_target = ('sp_d1' if t in PORTED_PREFIX else prefix)
                lines.append('    jump %s_scene_%d' % (self_target, t) if any(x['no'] == t for x in data['scenes']) else '    jump attention')
                lines.append('')
            elif k == 'like':
                if in_menu:
                    in_menu = False
                    lines.append('')
                lines.append('    # 【好感度】%s %d' % (it['speaker'], it['value']))
        if in_menu:
            in_menu = False
            lines.append('')
    lines.append('')
    lines.append('    return')
    files = {
        'game/chapters/extra/%s.rpy' % prefix: '\n'.join(lines) + '\n',
        'game/tl/japanese/%s_dialogs.rpy' % prefix: '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/%s_dialogs.rpy' % prefix: '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/%s_choises.rpy' % prefix: '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/%s_choises.rpy' % prefix: '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/extra/voice_map_%s.csv' % prefix, 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), 'missing', len(missing), missing[:15])


if __name__ == '__main__':
    main()
