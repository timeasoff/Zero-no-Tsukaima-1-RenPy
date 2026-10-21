# -*- coding: utf-8 -*-
"""Правка примечаний новых строк sprite_id_map.csv (ch5 part1): запятые в поле
notes создавали лишние «поля» CSV — заменяются на «/».

Запуск:  python tools/fix_ch5_1_sprite_notes.py [--apply]
"""

import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, "references", "sprite_id_map.csv")
IDS = (504, 506, 654, 742, 1061, 1065, 1067)


def main():
    apply = "--apply" in sys.argv
    lines = io.open(CSV, encoding="utf-8").read().split("\n")
    out = []
    changed = 0
    for ln in lines:
        m = re.match(r"^(\d+),(.*)$", ln)
        if m and int(m.group(1)) in IDS:
            parts = ln.split(",")
            head = ",".join(parts[:6])
            notes = ",".join(parts[6:])
            new_notes = notes.replace(", ", " / ")
            if new_notes != notes:
                changed += 1
            ln = "%s,%s" % (head, new_notes)
        out.append(ln)
    print("изменено строк: %d" % changed)
    if apply and changed:
        io.open(CSV, "w", encoding="utf-8").write("\n".join(out))
        print("записано")


if __name__ == "__main__":
    main()
