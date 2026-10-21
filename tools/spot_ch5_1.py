# -*- coding: utf-8 -*-
"""Выборочная сверка части ch5.1: JA (источник) ↔ EN (скрипт) ↔ RU (tl)
для строк, заданных номерами строк скрипта.

Использование: python tools/spot_ch5_1.py 87 166 198 274 321 463 569 706 865 903 981
"""

import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "game", "chapters", "5", "script-ch5_1.rpy")
SRC = os.path.join(ROOT, "ps2_source", "events_full", "chapter_06_本当の想い.txt")


def main():
    nums = [int(x) for x in sys.argv[1:]] or [87, 166, 198, 274, 321, 463, 569, 706, 865, 903, 981]
    lines = io.open(SCRIPT, encoding="utf-8").read().split("\n")
    # JA по id реплики
    ja = {}
    cur = 0
    for ln in io.open(SRC, encoding="utf-8"):
        m = re.match(r"^## SCENE (\d+)", ln)
        if m:
            cur = int(m.group(1))
        m2 = re.search(r'talk\("(?:[^"\\]|\\.)*", (?:null|"(?:[^"\\]|\\.)*"), "(.*)", \(0x04000000 \+(\d+)\)\)', ln)
        if m2 and 269 <= cur <= 284:
            ja[m2.group(2)] = m2.group(1).replace("\\n", "　")
    for n in nums:
        i = n - 1
        # строка с репликой — последняя подходящая до n
        en = None
        en_idx = None
        for k in range(i, max(-1, i - 6), -1):
            m = re.match(r'^\s*\w+ "(.*)"$', lines[k])
            if m:
                en, en_idx = m.group(1), k
                break
        j = "?"
        vid = None
        for ln in lines[en_idx:en_idx + 5] if en_idx is not None else []:
            m = re.search(r"# JA\[(\d+)\]:\s*(.*)$", ln)
            if m:
                vid, j = m.group(1), m.group(2)
                break
        print("стр.%d  id=%s\n   EN: %s\n   JA: %s\n" % (n, vid, en, j))


if __name__ == "__main__":
    main()
