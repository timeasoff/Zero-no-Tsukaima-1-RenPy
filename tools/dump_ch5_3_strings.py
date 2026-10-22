# -*- coding: utf-8 -*-
"""Полный список строк части 3 главы 5: имя реплики -> JA (для заполнения
EN/RU-модулей). Использование: python tools/dump_ch5_3_strings.py"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gen_ch5_3_script as G


def main():
    scenes = G.parse_events()
    V = G.Voices()
    order = []
    seen = set()
    for sc, branches, rejoin in G.FLOW:
        for x in ([sc] + list(branches) + ([rejoin] if rejoin else [])):
            if x not in seen:
                seen.add(x)
                order.append(x)
    th = 0
    for sc in order:
        for e in scenes.get(sc, []):
            if e[0] == 'talk':
                if e[4] is None:
                    th += 1
                    print('TH %-16s | %s' % ('ch5_3_th_%03d' % th,
                                            e[3].replace('\\n', ' \\n ')))
                else:
                    vn = V.name(e[1])
                    print('DL %-16s | %-8s | %s' % (vn, e[1],
                                                   e[3].replace('\\n', ' \\n ')))
            elif e[0] == 'choice':
                print('CH %-16s | %s' % (str(e[2]), e[1]))
    print('\nитого: голосов %d, мыслей %d' % (sum(V.counts.values()), th))


if __name__ == '__main__':
    main()
