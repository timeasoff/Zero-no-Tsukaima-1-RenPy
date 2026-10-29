# -*- coding: utf-8 -*-
"""Generate chapter 5 part 7 translation buckets from the canonical event source."""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import gen_ch5_7_script as gen
from ch5_7_en import EN_DIALOGS, EN_THOUGHTS, EN_CHOICES
from ch5_7_ru import RU_DIALOGS, RU_THOUGHTS, RU_CHOICES


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def ru_text(s):
    return s.replace("...", "…")


def write(path, language, rows):
    lines = ["translate %s strings:" % language, "# ===== ch5.7 regenerated ====="]
    for old, new in rows:
        lines += ["", '    old "%s"' % esc(old), '    new "%s"' % esc(new)]
    lines.append("# ===== end ch5.7 =====")
    with io.open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def main():
    scenes = gen.parse()
    names, counts, thoughts = {}, {}, {}
    for sc in gen.ORDER:
        for i, e in enumerate(scenes.get(sc, [])):
            if e[0] == "talk" and e[4] is not None:
                key = gen.SPK.get(e[1], "x")
                counts[key] = counts.get(key, 0) + 1
                names[(sc, i)] = "ch5.7_%s_%03d" % (key, counts[key])
    tn = 0
    for sc in gen.ORDER:
        for i, e in enumerate(scenes.get(sc, [])):
            if e[0] == "talk" and e[4] is None:
                tn += 1; thoughts[(sc, i)] = "ch5.7_th_%03d" % tn

    dialogs_ja, dialogs_ru, thoughts_ja, thoughts_ru, choices_ja, choices_ru = [], [], [], [], [], []
    missing = []
    for sc in gen.ORDER:
        for i, e in enumerate(scenes.get(sc, [])):
            if e[0] == "talk":
                ja = e[3].replace("\\n", " ")
                if e[4] is None:
                    tag = thoughts[(sc, i)]; old = EN_THOUGHTS.get(tag); ru = RU_THOUGHTS.get(tag)
                    if not old or not ru: missing.append(tag); continue
                    tagged = old.replace("\n", " ") + "{#%s}" % tag
                    thoughts_ja.append((tagged, ja)); thoughts_ru.append((tagged, ru_text(ru.replace("\n", " "))))
                else:
                    tag = names[(sc, i)]; old = EN_DIALOGS.get(tag); ru = RU_DIALOGS.get(tag)
                    if not old or not ru: missing.append(tag); continue
                    tagged = old.replace("\n", " ") + "{#ch5_7_v%s}" % e[4]
                    dialogs_ja.append((tagged, ja)); dialogs_ru.append((tagged, ru_text(ru.replace("\n", " "))))
            elif e[0] == "choice":
                target, ja = str(e[2]), e[1]
                old, ru = EN_CHOICES.get(target), RU_CHOICES.get(target)
                if not old or not ru: missing.append("choice:%s" % target); continue
                tagged = old + "{#ch5_7_c%s}" % target
                choices_ja.append((tagged, ja)); choices_ru.append((tagged, ru))
    if missing:
        raise SystemExit("missing translations: " + ", ".join(missing))
    write(os.path.join(ROOT, "game/tl/japanese/ch5_7_dialogs.rpy"), "japanese", dialogs_ja)
    write(os.path.join(ROOT, "game/tl/russian/ch5_7_dialogs.rpy"), "russian", dialogs_ru)
    write(os.path.join(ROOT, "game/tl/japanese/ch5_7_thoughts.rpy"), "japanese", thoughts_ja)
    write(os.path.join(ROOT, "game/tl/russian/ch5_7_thoughts.rpy"), "russian", thoughts_ru)
    write(os.path.join(ROOT, "game/tl/japanese/ch5_7_choises.rpy"), "japanese", choices_ja)
    write(os.path.join(ROOT, "game/tl/russian/ch5_7_choises.rpy"), "russian", choices_ru)
    print("dialogs=%d thoughts=%d choices=%d" % (len(dialogs_ja), len(thoughts_ja), len(choices_ja)))


if __name__ == "__main__": main()
