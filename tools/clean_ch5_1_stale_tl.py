# -*- coding: utf-8 -*-
"""Одноразовая чистка осиротевших записей tl после правки EN в части 5.1.

Причина: пересборка `gen_ch5_1_tl.py --replace` вырезала блок по совпадению
`old`; после правки EN (добавлено «too!», «…at all?», «Fine, I'll say it!»)
прежние `old` перестали совпадать, и по 2 записи на язык остались в файлах
как мусор (в скрипте таких строк уже нет).

Запуск:  python tools/clean_ch5_1_stale_tl.py [--apply]
"""

import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STALE = {
    os.path.join(ROOT, "game", "tl", "japanese", "dialogs.rpy"): [
        ('    old "Louise and Siesta are both all over Hiraga-kun first thing in the morning!"\n',
         '    new "ルイズさんや、シエスタさんも、　朝から平賀くんにベタベタしちゃって！"\n'),
        ('    old "…Wow, you really hadn\'t thought of anything at all."\n',
         '    new "……はぁ、ホントになにも考えて　なかったのかよ。"\n'),
    ],
    os.path.join(ROOT, "game", "tl", "russian", "dialogs.rpy"): [
        ('    old "Louise and Siesta are both all over Hiraga-kun first thing in the morning!"\n',
         '    new "Луиза и Сиеста с самого утра прилипают к Хирага-куну!"\n'),
        ('    old "…Wow, you really hadn\'t thought of anything at all."\n',
         '    new "…Ха-а, ты и правда ни о чём не подумала."\n'),
    ],
}


def main():
    apply = "--apply" in sys.argv
    for path, pairs in STALE.items():
        txt = io.open(path, encoding="utf-8").read()
        for old, new in pairs:
            block = "translate %s strings:\n%s%s\n" % (
                "japanese" if "japanese" in path else "russian", old, new)
            if block in txt:
                txt = txt.replace(block, "", 1)
                print("removed stale: %s :: %s" % (os.path.relpath(path, ROOT), old.strip()[:60]))
            else:
                print("NOT FOUND: %s :: %s" % (os.path.relpath(path, ROOT), old.strip()[:60]))
        if apply:
            io.open(path, "w", encoding="utf-8").write(txt)


if __name__ == "__main__":
    main()
