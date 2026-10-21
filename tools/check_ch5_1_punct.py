# -*- coding: utf-8 -*-
"""Поиск «чистых» реплик (только знаки препинания / звуки) в дампе JA+EN+RU."""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import gen_ch5_1_script as G
from ch5_1_en import EN_DIALOGS, EN_THOUGHTS, EN_CHOICES
from ch5_1_ru import RU_DIALOGS, RU_THOUGHTS, RU_CHOICES

PUNCT = set(u'…。、！？!?…（）() \u3000ー～-–—「」『』"\'')


def main():
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
    for sc in order:
        for i, e in enumerate(scenes.get(sc, [])):
            if e[0] != 'talk':
                continue
            if e[4] is None:
                th += 1
                key = 'ch5_th_%03d' % th
                en = EN_THOUGHTS.get(key, '')
                ru = RU_THOUGHTS.get(key, '')
            else:
                key = vmap[(sc, i)]
                en = EN_DIALOGS.get(key, '')
                ru = RU_DIALOGS.get(key, '')
            ja = e[3]
            stripped = ''.join(c for c in ja if c not in PUNCT)
            # «чистая» реплика: кроме знаков/слов-звуков ничего
            if len(stripped) <= 3:
                print('%-14s JA=%-24s EN=%-28s RU=%s'
                      % (key, ja.replace('\\n', ' / '), en.replace('\\n', ' / '),
                         ru.replace('\\n', ' / ')))


if __name__ == '__main__':
    main()
