# -*- coding: utf-8 -*-
"""Добавляет в references/sprite_id_map.csv строки для спрайтов главы 5, часть 1.

Имена выведены по блок-правилу проекта (references/sprite_id_map.csv, шапка):
  база B = id - ((id - 5) mod 11); позы 0/1 = база, 2/3 = happy, 4/5 = angry,
  6/7 = sad, 8/9 = shy.
Сверка SCENEDAT (пиксельная) в этой среде невозможна — все новые строки помечены
PROVISIONAL, как принято для ch4_6.

Запуск:  python tools/add_ch5_1_sprite_rows.py [--apply]
"""

import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVENTS = os.path.join(ROOT, "ps2_source", "events_full", "chapter_06_本当の想い.txt")
CSV = os.path.join(ROOT, "references", "sprite_id_map.csv")
SCENES = range(269, 285)

# id -> (имя, слой по умолчанию, примечание)
NEW = {
    504: ("si 2 angry", "lay2", "ch5 part1 (сцена 274); block 500 pos 4 — PROVISIONAL: сверка SCENEDAT не выполнена (si-блоки: 489=si 1 / 500=si 2 / 511=si 3 / 522=si 4 / 533=si 5 / 544=si 6)"),
    506: ("si 2 sad", "lay2", "ch5 part1 (сцена 274); block 500 pos 6 — PROVISIONAL: сверка SCENEDAT не выполнена"),
    654: ("t 7", "lay0", "ch5 part1 (сцена 275); block 654 pos 0 — PROVISIONAL: сверка SCENEDAT не выполнена (t-блоки: 588=t 1 / 599=t 2 / 610=t 3 / 621=t 4 / 632=t 5 / 643=t 6)"),
    742: ("k 7", "lay6", "ch5 part1 (сцена 279); block 742 pos 0 — PROVISIONAL: сверка SCENEDAT не выполнена (k-блоки: 676=k 1 / 687=k 2 / 698=k 3 / 709=k 4 / 720=k 5 / 731=k 6; 744=k 7 happy / 746=k 7 angry уже в справочнике)"),
    1061: ("w 1", "lay20", "ch5 part1 (сцена 280); block 1061 pos 0 — PROVISIONAL: сверка SCENEDAT не выполнена (первый w-блок)"),
    1065: ("w 1 angry", "lay20", "ch5 part1 (сцена 280); block 1061 pos 4 — PROVISIONAL: сверка SCENEDAT не выполнена"),
    1067: ("w 1 sad", "lay20", "ch5 part1 (сцена 280); block 1061 pos 6 — PROVISIONAL: сверка SCENEDAT не выполнена"),
}

TALK = re.compile(r"talk\((?:\"[^\"]*\"|null), (?:\"[^\"]*\"|null), \".*?\", (?:0x04000000 \+(\d+)|null)\)")


def collect():
    """Считает uses / first_scene / first_line / layers для каждого id."""
    lines = io.open(EVENTS, encoding="utf-8").read().split("\n")
    scenes = {}  # scene -> (start, end)
    cur = None
    for i, ln in enumerate(lines):
        m = re.match(r"^## SCENE (\d+)", ln)
        if m:
            cur = int(m.group(1))
            scenes[cur] = [i, len(lines)]
        elif cur is not None:
            scenes[cur][1] = i

    stats = {}
    for sc in SCENES:
        if sc not in scenes:
            continue
        a, b = scenes[sc]
        for i in range(a + 1, b):
            ln = lines[i]
            im = re.search(r"image = \(0x02000000 \+(\d+)\)", ln)
            lay = re.search(r'set\("(lay\d+)"', ln)
            if not (im and lay) or "hide" in ln:
                continue
            sid = int(im.group(1))
            st = stats.setdefault(sid, {"uses": 0, "scene": sc, "line": "", "layers": set()})
            st["uses"] += 1
            st["layers"].add(lay.group(1))
            if sc < st["scene"] or (sc == st["scene"] and not st["line"]):
                # первый talk после появления спрайта в этой сцене
                tid = ""
                for j in range(i + 1, b):
                    m = TALK.search(lines[j])
                    if m:
                        tid = m.group(1) or ""
                        break
                st["scene"] = sc
                st["line"] = tid
    return stats


def main():
    stats = collect()
    rows = []
    for sid in sorted(NEW):
        name, layer, note = NEW[sid]
        st = stats.get(sid, {"uses": 0, "scene": "", "line": "", "layers": set([layer])})
        layers = ";".join(sorted(st["layers"])) or layer
        rows.append("%d,%s,%d,%s,%s,%s,%s" % (sid, name, st["uses"], st["scene"], st["line"], layers, note))

    existing = io.open(CSV, encoding="utf-8").read()
    todo = [r for r in rows if not re.search(r"^%d," % int(r.split(",")[0]), existing, re.M)]
    print("новых строк: %d" % len(todo))
    for r in todo:
        print("  " + r)
    if "--apply" in sys.argv and todo:
        with io.open(CSV, "a", encoding="utf-8", newline="") as f:
            if not existing.endswith("\n"):
                f.write("\n")
            for r in todo:
                f.write(r + "\n")
        print("записано в %s" % CSV)


if __name__ == "__main__":
    main()
