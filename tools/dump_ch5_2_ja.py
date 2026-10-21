# -*- coding: utf-8 -*-
"""Вспомогательный дамп для части 2 главы 5: ключ, говорящий, JA, контекст.

Использование: python tools/dump_ch5_2_ja.py .tmp/ja_dump_ch5_2.txt
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import gen_ch5_2_script as G


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        ROOT, '.tmp', 'ja_dump_ch5_2.txt')
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
    prev = ''
    for sc in order:
        lines.append('==== SCENE %d ====' % sc)
        for i, e in enumerate(scenes.get(sc, [])):
            if e[0] == 'talk':
                if e[4] is None:
                    th += 1
                    key = 'ch5_2_th_%03d' % th
                    lines.append('[%s] (мысль %s)' % (key, e[1]))
                    lines.append('   JA: %s' % e[3].replace('\\n', ' / '))
                    lines.append('   контекст: ...%s' % prev[-60:])
                else:
                    key = vmap[(sc, i)]
                    lines.append('[%s] %s' % (key, e[1]))
                    lines.append('   JA: %s' % e[3].replace('\\n', ' / '))
                    lines.append('   контекст: ...%s' % prev[-60:])
                prev = e[3].replace('\\n', ' / ')
            elif e[0] == 'choice':
                lines.append('[меню -> %d] %s' % (e[2], e[1]))
            elif e[0] == 'like':
                lines.append('[好感度] %s %+d' % (e[1], e[2]))
            elif e[0] in ('bg', 'cg'):
                lines.append('[%s] +%d' % ('BG' if e[0] == 'bg' else 'CG', e[1]))
            elif e[0] == 'bgm_play':
                lines.append('[BGM] t%d' % (e[1] - 1))
            elif e[0] == 'bgm_stop':
                lines.append('[BGM stop]')
    d = os.path.dirname(out_path)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    with io.open(out_path, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lines) + '\n')
    print('written: %s (%d lines)' % (out_path, len(lines)))


if __name__ == '__main__':
    main()
