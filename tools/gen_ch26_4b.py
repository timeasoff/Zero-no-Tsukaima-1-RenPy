#!/usr/bin/env python3
"""Chapter 26 part 4b (scenes 967-971): Tabitha wakes up - RECOVERED OMISSION.

These 5 core scenes (54 voices) were absent from the original port; part 4 jumped
straight from scene 966 to the extra date scenes (ch26_5). This part restores them
between part 4 and part 5.
"""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = json.load(open('reports/ch26/new/trans_967_971.json', encoding='utf-8'))
CHOICES = {
    967: [
        ("Let's stay quiet just like this.", "Помолчим и останемся так."),
        ("Could this be……?", "Неужели это……?"),
        ("I have to properly continue the conversation……", "Нужно продолжить разговор как следует……"),
    ],
}
SPK = {'サイト': 's', 'タバサ': 't', 'キュルケ': 'k', 'null': 'th'}
START = {'s': 0, 't': 0, 'k': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch26/parse_934_971.json', encoding='utf-8'))
    script = ['# Глава 26, часть 4b (сцены 967–971): пробуждение Табасы — восстановленный пропуск.',
              '# Источник: ps2_source/chapters/chapter_27_タバサの秘密.txt (SCENE 967-971).',
              '', 'label ch26_4b:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            scene = x['no'] if 967 <= x['no'] <= 971 else None
            if scene is None:
                continue
            script += ['label ch26_4b_scene_%d:' % scene, '']
            continue
        if scene is None or not 967 <= scene <= 971:
            continue
        if k == 'event':
            event(x['src'], script)
            continue
        if k == 'dlg':
            pair = T.get('d%d' % x['idx'])
            if pair is None:
                script.append('    # MISSING d%d: %s' % (x['idx'], x['ja'][:40]))
                continue
            en, ru = en_norm(pair[0]), pair[1]
            spk = SPK.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch26_4b_%s_%03d' % (spk, counters[spk])
            full = '%s{#%s}' % (en, tag)
            script.append('    # ' + x['src'])
            if x['voice'] is not None:
                script.append('    voice "%s"' % tag)
                manifest.append((tag, x['voice']))
            script.append('    %s "%s"' % (spk, full))
            ja_new = x['ja'] if x['thought'] else '%s：%s' % (x['speaker'], x['ja'])
            ja_d += ['    old "%s"' % full, '    new "%s"' % ja_new, '']
            ru_d += ['    old "%s"' % full, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'choice':
            if scene != 967:
                continue
            script.append('    menu:')
            for i, o in enumerate(x['options']):
                en, ru = CHOICES[scene][i]
                ctext = '%s{#ch26_4b_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch26_4b_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump ch26_4b_scene_%d' % x['target'])
            script.append('')
            continue
        if k == 'date':
            script.append('    # 【デート】%s → scene %d' % (x.get('text', ''), x['target']))
            if x.get('kind2') == 'date':
                script.append('    jump ch26_5')
            else:
                script.append('    # 【デート進行】 → scene %d (выход в следующую главу)' % x['target'])
                script.append('    jump ch27')
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 4b ====', '    jump ch26_5', '    return', '']
    files = {
        'game/chapters/26/script-ch26_4b.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch26_4b_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch26_4b_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch26_4b_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch26_4b_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch26/voice_map_4b.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
