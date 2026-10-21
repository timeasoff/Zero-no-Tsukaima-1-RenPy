# -*- coding: utf-8 -*-
"""Вспомогательный дамп: JA (источник) + EN (tools/ch5_1_en.py) по репликам.

Использование: python tools/dump_ch5_1_ja.py .tmp/ja_dump_ch5_1.txt
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import gen_ch5_1_script as G
from ch5_1_en import EN_DIALOGS, EN_THOUGHTS, EN_CHOICES
from ch5_1_ru import RU_DIALOGS, RU_THOUGHTS, RU_CHOICES


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, '.tmp', 'ja_dump_ch5_1.txt')
    scenes = G.parse_events()
    order = []
    for sc, br, rj in G.FLOW:
        order.append(sc)
        if br:
            order.extend(br)
        if rj:
            order.append(rj)
    V = G.Voices()
    vmap = {}
    for sc in order:
        for i, e in enumerate(scenes.get(sc, [])):
            if e[0] == 'talk' and e[4] is not None:
                vmap[(sc, i)] = V.name(e[1])
    th = 0
    lines = []
    for sc in order:
        lines.append('==== SCENE %d ====' % sc)
        for i, e in enumerate(scenes.get(sc, [])):
            if e[0] == 'talk':
                if e[4] is None:
                    th += 1
                    tag = 'ch5_th_%03d' % th
                    lines.append('  [%s] %s' % (tag, e[3].replace('\\n', ' / ')))
                    lines.append('       EN: %s' % str(EN_THOUGHTS.get(tag)).replace('\\n', ' / '))
                    lines.append('       RU: %s' % str(RU_THOUGHTS.get(tag)).replace('\\n', ' / '))
                else:
                    vn = vmap[(sc, i)]
                    lines.append('  [%s|%s] %s' % (vn, e[1], e[3].replace('\\n', ' / ')))
                    lines.append('       EN: %s' % str(EN_DIALOGS.get(vn)).replace('\\n', ' / '))
                    lines.append('       RU: %s' % str(RU_DIALOGS.get(vn)).replace('\\n', ' / '))
            elif e[0] == 'choice':
                lines.append('  [choice->%d] %s' % (e[2], e[1]))
                lines.append('       EN: %s' % str(EN_CHOICES.get(str(e[2]))))
                lines.append('       RU: %s' % str(RU_CHOICES.get(str(e[2]))))
    with io.open(out_path, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lines) + '\n')
    print('written: %s (%d lines)' % (out_path, len(lines)))


if __name__ == '__main__':
    main()
