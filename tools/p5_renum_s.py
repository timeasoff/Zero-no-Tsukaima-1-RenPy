# -*- coding: utf-8 -*-
"""Сдвигает ключи ch3.5_s_NNN (NNN >= 27) на +1 в script-ch3_5.rpy.

Причина: при первом перечислении канона пропущена реплика s 11337
(сцена 177, «ったく、ルイズのヤツ……。») — все последующие ключи Saito
должны сместиться на одну позицию.
"""
import io
import re
import sys

PATH = "game/chapters/3/script-ch3_5.rpy"


def main():
    text = io.open(PATH, encoding="utf-8").read()

    def repl(m):
        n = int(m.group(1))
        if n >= 27:
            return 'voice "ch3.5_s_%03d"' % (n + 1)
        return m.group(0)

    new = re.sub(r'voice "ch3\.5_s_(\d+)"', repl, text)
    n_changed = sum(1 for a, b in zip(text.splitlines(), new.splitlines())
                    if a != b)
    io.open(PATH, "w", encoding="utf-8", newline="\n").write(new)
    print("shifted lines: %d" % n_changed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
