# -*- coding: utf-8 -*-
"""Дамп всех переводимых строк script-ch3_5.rpy (EN) в порядке следования."""
import io
import re
import sys

PATH = "game/chapters/3/script-ch3_5.rpy"


def main():
    text = io.open(PATH, encoding="utf-8").read().splitlines()
    out = []
    in_menu = False
    for i, ln in enumerate(text, 1):
        m = re.match(r'\s*(s|l|si|ha|k|t|c|m|g|th) "(.*)"$', ln)
        if m:
            out.append("%5d [%s] %s" % (i, m.group(1), m.group(2)))
            continue
        m = re.match(r'\s*"(.*)":$', ln)
        if m:
            out.append("%5d [menu] %s" % (i, m.group(1)))
    io.open("tools/p5_strings_dump.txt", "w", encoding="utf-8",
            newline="\n").write("\n".join(out))
    print("strings: %d -> tools/p5_strings_dump.txt" % len(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
