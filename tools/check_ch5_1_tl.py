# -*- coding: utf-8 -*-
"""Проверка покрытия tl для части ch5_1.

Сверяет строки сценария `game/chapters/5/script-ch5_1.rpy` с парами old/new
в `game/tl/{japanese,russian}/{dialogs,thoughs,choises}.rpy`:
  * каждая строка сценария (реплика / мысль / пункт меню) есть в tl как `old`;
  * у каждой такой `old` есть `new` (в т.ч. многострочный);
  * дубликатов `old` в файле нет.

Запуск:  python tools/check_ch5_1_tl.py
"""

import io
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "game", "chapters", "5", "script-ch5_1.rpy")

OLD = re.compile(r'^    old "(.*)"$')
NEW = re.compile(r'^    new +"(.*)"$')
HEAD = re.compile(r"^translate .* strings:")

# тип строки сценария -> бакет tl
BUCKET = {"dialog": "dialogs", "th": "thoughs", "choice": "choises"}


def script_strings():
    out = {"dialogs": [], "thoughs": [], "choises": []}
    for ln in io.open(SCRIPT, encoding="utf-8").read().split("\n"):
        m = re.match(r'^\s*(\w+) "(.*)"$', ln)
        if not m:
            continue
        who, text = m.group(1), m.group(2)
        if who in ("s", "l", "ha", "si", "w", "k", "d", "t", "g", "m", "unk_w", "unk_k"):
            out["dialogs"].append(text)
        elif who == "th":
            out["thoughs"].append(text)
        elif who == "menu":
            continue
    return out


def menu_strings():
    out = []
    for ln in io.open(SCRIPT, encoding="utf-8").read().split("\n"):
        m = re.match(r'^\s+"([^"]+)":$', ln)
        if m:
            out.append(m.group(1))
    return out


def read_records(path):
    lines = io.open(path, encoding="utf-8").read().split("\n")
    records = []
    cur_old, cur_new = None, None
    for ln in lines:
        if HEAD.match(ln):
            if cur_old is not None:
                records.append((cur_old, cur_new))
            cur_old, cur_new = None, None
            continue
        m = OLD.match(ln)
        if m:
            if cur_old is not None:
                records.append((cur_old, cur_new))
            cur_old, cur_new = m.group(1), None
            continue
        m = NEW.match(ln)
        if m and cur_old is not None and cur_new is None:
            cur_new = m.group(1)
    if cur_old is not None:
        records.append((cur_old, cur_new))
    return records


def main():
    want = script_strings()
    want["choises"] = menu_strings()
    ok = True
    for lang in ("japanese", "russian"):
        for bucket in ("dialogs", "thoughs", "choises"):
            path = os.path.join(ROOT, "game", "tl", lang, bucket + ".rpy")
            records = read_records(path)
            olds = [o for o, _ in records]
            dups = [k for k, v in Counter(olds).items() if v > 1]
            have = set(olds)
            missing = [s for s in want[bucket] if s not in have]
            broken = [o for o, w in records if w is None and o in set(want[bucket])]
            print("%s/%s: строк сценария=%d, в tl=%d, дублей old=%d, нет old=%d, без new=%d"
                  % (lang, bucket, len(want[bucket]), len(records), len(dups), len(missing), len(broken)))
            if dups:
                ok = False
                for d in dups[:5]:
                    print("   ДУБЛЬ old: %s" % d)
            if missing:
                ok = False
                for m in missing[:5]:
                    print("   НЕТ old: %s" % m)
            if broken:
                ok = False
                for b in broken[:5]:
                    print("   НЕТ new: %s" % b)
    print("RESULT:", "OK" if ok else "ПРОБЛЕМЫ")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
