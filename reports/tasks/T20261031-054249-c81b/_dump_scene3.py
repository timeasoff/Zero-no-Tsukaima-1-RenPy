# -*- coding: utf-8 -*-
"""Dump decoded lines of ps2_source/scripts/SCENE_0003.txt (cp932 + NUL)."""
import sys

PATH = "ps2_source/scripts/SCENE_0003.txt"

def load():
    with open(PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("cp932", errors="replace")
    # normalize NULs (often between chars in these dumps)
    text = text.replace("\x00", "")
    return text.splitlines()

def main():
    lines = load()
    if len(sys.argv) >= 3:
        a, b = int(sys.argv[1]), int(sys.argv[2])
    else:
        a, b = 1, len(lines)
    for i in range(a - 1, min(b, len(lines))):
        sys.stdout.write("%d: %s\n" % (i + 1, lines[i]))

if __name__ == "__main__":
    main()
