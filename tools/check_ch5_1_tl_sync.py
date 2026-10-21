# -*- coding: utf-8 -*-
"""Сверка `old`-наборов tl/japanese и tl/russian: ищет записи, присутствующие
в одном файле, но отсутствующие в другом (осиротевшие после пересборки).

Опция --base HEAD — сверка с версией в git (проверка, что расхождения были
до текущей работы).

Запуск:  python tools/check_ch5_1_tl_sync.py [--base HEAD]
"""

import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD = re.compile(r'^    old "(.*)"$')


def olds(path, base=None):
    if base:
        txt = subprocess.check_output(["git", "show", "%s:%s" % (base, os.path.relpath(path, ROOT))])
        txt = txt.decode("utf-8")
    else:
        txt = io.open(path, encoding="utf-8").read()
    return [m.group(1) for m in (OLD.match(ln) for ln in txt.split("\n")) if m]


def main():
    base = None
    if "--base" in sys.argv:
        base = sys.argv[sys.argv.index("--base") + 1]
    for bucket in ("dialogs", "thoughs", "choises"):
        ja = olds(os.path.join(ROOT, "game", "tl", "japanese", bucket + ".rpy"), base)
        ru = olds(os.path.join(ROOT, "game", "tl", "russian", bucket + ".rpy"), base)
        only_ja = [x for x in ja if x not in set(ru)]
        only_ru = [x for x in ru if x not in set(ja)]
        print("%s: ja=%d ru=%d | только ja=%d, только ru=%d"
              % (bucket, len(ja), len(ru), len(only_ja), len(only_ru)))
        for x in only_ja[:20]:
            print("   только ja: %s" % x)
        for x in only_ru[:20]:
            print("   только ru: %s" % x)
    return 0


if __name__ == "__main__":
    sys.exit(main())
