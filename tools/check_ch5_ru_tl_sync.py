# -*- coding: utf-8 -*-
"""Сверка модулей RU (tools/ch5_N_ru.py) с tl/russian: каждая строка модуля
должна встречаться в tl как `new` (в склеенном виде), и наоборот.

Нужен, чтобы правки в модуле не «терялись» при пересборке tl и чтобы
ручная правка tl не расходилась с модулем-источником.

Запуск: python tools/check_ch5_ru_tl_sync.py
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PARTS = {
    'ch5_1': ('ch5_1_ru', 'dialogs', 'thoughs', 'choises'),
    'ch5_2': ('ch5_2_ru', 'dialogs', 'thoughs', 'choises'),
    'ch5_3': ('ch5_3_ru', 'dialogs', 'thoughs', 'choises'),
    'ch5_4': ('ch5_4_ru', 'dialogs', 'thoughs', 'choises'),
}

# Реплики в （…） (мысль с голосом) лежат в бакете thoughs, хотя в модуле
# хранятся среди диалогов (references/ps2_to_renpy.csv, п. 2).
EXTRA_BUCKET = {
    'ch5_4': {'ch5.4_d_001': 'thoughs', 'ch5.4_d_002': 'thoughs'},
}

RE_OLD = re.compile(r'^\s*old\s+"(.*)"\s*$')
RE_NEW = re.compile(r'^\s*new\s+"(.*)"\s*$')


def flat(s):
    return s.replace('\n', ' ')


def tl_pairs(path):
    """-> {old: new} из файла tl."""
    pairs = {}
    cur_old = None
    for ln in io.open(path, encoding='utf-8'):
        m = RE_OLD.match(ln)
        if m:
            cur_old = m.group(1)
            continue
        m = RE_NEW.match(ln)
        if m and cur_old is not None:
            pairs[cur_old] = m.group(1)
            cur_old = None
    return pairs


def main():
    problems = 0
    for part, (mod_name, *buckets) in sorted(PARTS.items()):
        mod = __import__(mod_name)
        for bucket, attr in zip(buckets, ('RU_DIALOGS', 'RU_THOUGHTS', 'RU_CHOICES')):
            data = getattr(mod, attr)
            path = os.path.join(ROOT, 'game', 'tl', 'russian', bucket + '.rpy')
            pairs = tl_pairs(path)
            tl_new = set(pairs.values())
            extra = EXTRA_BUCKET.get(part, {})
            for key, text in data.items():
                val = flat(text)
                where = extra.get(key)
                if where and where != bucket:
                    # строка лежит в другом бакете tl — проверяем там
                    opath = os.path.join(ROOT, 'game', 'tl', 'russian', where + '.rpy')
                    if val in set(tl_pairs(opath).values()):
                        continue
                if val not in tl_new:
                    print('РАСХОЖДЕНИЕ %s/%s: в tl нет строки модуля' % (part, key))
                    print('   модуль: %s' % val[:100])
                    problems += 1
            print('%s/%s: строк модуля=%d, уникальных new в tl=%d'
                  % (part, bucket, len(data), len(tl_new)))
    print('\nRESULT: %s' % ('OK' if problems == 0 else 'РАСХОЖДЕНИЙ: %d' % problems))
    return 0 if problems == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
