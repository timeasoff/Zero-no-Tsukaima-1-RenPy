# -*- coding: utf-8 -*-
"""Глава 4 (P1+P2): правка форм обращения по addresses.md.

- ミスタ・コルベール → EN "Professor Colbert" / RU «профессор Кольбер»
  (addresses.md: «месье/мистер Кольбер» — неправильно; исключение для Кольбера).
- ミス・モンモランシー → RU «мадемуазель Монморанси».
- ミス・ハルナ → RU «мадемуазель Харуна» (в реплике Харуны — цитата формы).
- RU «госпожа/госпожи Вальер» (ч. 4_2) → «мадемуазель Вальер».

Запуск: python tools/fix_ch4_addresses.py [--apply]
"""
import io
import sys

BASE = r'D:/gameMake/ZnT-1/ZnT1'
S1 = BASE + '/game/chapters/4/script-ch4_1.rpy'
S2 = BASE + '/game/chapters/4/script-ch4_2.rpy'
JA = BASE + '/game/tl/japanese/dialogs.rpy'
RU = BASE + '/game/tl/russian/dialogs.rpy'

# line-number targeted replacements in the RU tl (1-based)
RU_LINES = {
    10360: [('«Мисс Харуна»', '«Мадемуазель Харуна»')],
    10549: [('мисс Монморанси', 'мадемуазель Монморанси')],
    10558: [('мисс Монморанси', 'мадемуазель Монморанси')],
    10777: [('Госпожа Вальер', 'Мадемуазель Вальер')],
    10807: [('госпожа Вальер', 'мадемуазель Вальер')],
    10924: [('госпожа Вальер', 'мадемуазель Вальер')],
    10951: [('госпожи Вальер', 'мадемуазель Вальер')],
}


def fix_mister(path, expect):
    text = io.open(path, encoding='utf-8').read()
    n = text.count('Mister Colbert')
    if n != expect:
        raise SystemExit('%s: Mister Colbert = %d (ожидалось %d)'
                         % (path, n, expect))
    return text.replace('Mister Colbert', 'Professor Colbert'), n


def fix_ru_new(text, expect):
    n = text.count('мистер Кольбер') + text.count('Мистер Кольбер')
    if n != expect:
        raise SystemExit('ru: мистер Кольбер = %d (ожидалось %d)' % (n, expect))
    return (text.replace('Мистер Кольбер', 'Профессор Кольбер')
                .replace('мистер Кольбер', 'профессор Кольбер')), n


def main():
    apply = '--apply' in sys.argv
    s1, n1 = fix_mister(S1, 5)
    s2, n2 = fix_mister(S2, 1)
    ja, n3 = fix_mister(JA, 6)
    ru, n4 = fix_mister(RU, 6)
    ru, n5 = fix_ru_new(ru, 6)

    lines = ru.split('\n')
    for ln, pairs in sorted(RU_LINES.items()):
        src = lines[ln - 1]
        for a, b in pairs:
            if src.count(a) != 1:
                raise SystemExit('ru line %d: %r x%d' % (ln, a, src.count(a)))
            src = src.replace(a, b)
        lines[ln - 1] = src
    ru = '\n'.join(lines)

    print('EN Mister Colbert -> Professor Colbert: %d (ch4_1) %d (ch4_2)'
          % (n1, n2))
    print('ja old: %d   ru old: %d   ru new «профессор Кольбер»: %d'
          % (n3, n4, n5))
    print('ru точечных правок форм обращения: %d' % len(RU_LINES))
    if not apply:
        print('dry-run OK. Use --apply to write.')
        return 0
    io.open(S1, 'w', encoding='utf-8', newline='').write(s1)
    io.open(S2, 'w', encoding='utf-8', newline='').write(s2)
    io.open(JA, 'w', encoding='utf-8', newline='').write(ja)
    io.open(RU, 'w', encoding='utf-8', newline='').write(ru)
    print('written')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
