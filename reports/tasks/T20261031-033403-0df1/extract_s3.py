#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S3: извлечение развилок PS2-источника для глав 07..17.

Только чтение ps2_source/. Выход: raw_s3.json + ASCII-сводка в stdout.
Основано на extract_branches.py (S5, главы 18..29), но не изменяет его.

Дополнительно к S5-версии:
  * сверка chapters <-> events_full (счётчики и цели);
  * проверка существования целевых сцен во всём ps2_source/chapters/;
  * like_ch (【好感度】) и like (events LIKE) — оба входа;
  * нестандартные if (все строки "if", кроме if(isJump()));
  * условные GOTO next(..., cond != true).
"""
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CHAPTERS = os.path.join(ROOT, "ps2_source", "chapters")
EVENTS = os.path.join(ROOT, "ps2_source", "events_full")
OUT = os.path.join(HERE, "raw_s3.json")

CHS = list(range(7, 18))

RE_SCENE = re.compile(r"^---- SCENE (\d+) ----")
RE_CHOICE = re.compile(r"^\s*【選択肢】(.+?)\s*→\s*scene\s+(\d+)")
RE_MOVE = re.compile(
    r"^\s*【移動】(.+?)\s*→\s*scene\s+(\d+)\s*(?:\(\(0x01000000\s*\+(\d+)\)\))?")
RE_DATE = re.compile(r"^\s*【デート】(.+?)\s*→\s*scene\s+(\d+)")
RE_DATEPROG = re.compile(r"^\s*【デート進行】\s*→\s*scene\s+(\d+)")
RE_NEXT = re.compile(r"^\s*→\s*next\s+scene\s+(\d+)")
RE_LIKE_CH = re.compile(r"^\s*【好感度】(.+?)\s+([+-]?\d+)")
RE_HDR = re.compile(r"^(core scenes|extra scenes)\s*:\s*(.+)$")
RE_E_SCENE = re.compile(r"^## SCENE (\d+)")
RE_SCENE_CODE = re.compile(r"\(0x01000000\s*\+(\d+)\)")


def find(ch, folder):
    hits = glob.glob(os.path.join(folder, "chapter_%02d_*.txt" % ch))
    if len(hits) != 1:
        raise SystemExit("chapter %d: %d files in %s" % (ch, len(hits), folder))
    return hits[0]


def parse_chapter(path):
    d = {"header": [], "scenes": 0, "scene_list": [], "choices": [], "moves": [],
         "dates": [], "dateprog": [], "nexts": [], "likes_ch": []}
    owner = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\r\n")
            m = RE_HDR.match(line)
            if m:
                d["header"].append(m.group(0).strip())
                continue
            m = RE_SCENE.match(line)
            if m:
                owner = int(m.group(1))
                d["scenes"] += 1
                d["scene_list"].append(owner)
                continue
            if owner is None:
                continue
            m = RE_CHOICE.match(line)
            if m:
                d["choices"].append([owner, m.group(1).strip(), int(m.group(2))])
                continue
            m = RE_MOVE.match(line)
            if m:
                real = int(m.group(3)) if m.group(3) else None
                d["moves"].append([owner, m.group(1).strip(), int(m.group(2)), real])
                continue
            m = RE_DATE.match(line)
            if m:
                d["dates"].append([owner, m.group(1).strip(), int(m.group(2))])
                continue
            m = RE_DATEPROG.match(line)
            if m:
                d["dateprog"].append([owner, int(m.group(1))])
                continue
            m = RE_NEXT.match(line)
            if m:
                d["nexts"].append([owner, int(m.group(1))])
                continue
            m = RE_LIKE_CH.match(line)
            if m:
                d["likes_ch"].append([owner, m.group(1).strip(), int(m.group(2))])
                continue
    return d


def split_args(s):
    """Разбор аргументов по запятым на глубине 0 (учёт (){}[] и кавычек)."""
    out, depth, cur, inq = [], 0, "", None
    i = 0
    while i < len(s):
        c = s[i]
        if inq:
            if c == "\\":
                cur += c + (s[i + 1] if i + 1 < len(s) else "")
                i += 2
                continue
            if c == inq:
                inq = None
            cur += c
        else:
            if c in "\"'":
                inq = c
                cur += c
            elif c in "({[":
                depth += 1
                cur += c
            elif c in ")}]":
                depth -= 1
                cur += c
            elif c == "," and depth == 0:
                out.append(cur.strip())
                cur = ""
            else:
                cur += c
        i += 1
    if cur.strip():
        out.append(cur.strip())
    return out


def parse_events(path):
    d = {"tndls": [], "likes": [], "routes": [], "other_if": [],
         "cond_gotos": [], "gotos": 0, "choices": [], "moves": [],
         "dates": [], "datecalls": [], "scenes": 0}
    owner = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\r\n")
            m = RE_E_SCENE.match(line)
            if m:
                owner = int(m.group(1))
                d["scenes"] += 1
                continue
            if owner is None:
                continue
            if line.startswith("TNDL"):
                mm = re.search(r"tndl\((.*)\)\s*$", line)
                d["tndls"].append([owner, mm.group(1) if mm else "?"])
            elif line.startswith("LIKE"):
                mm = re.search(r"like\((.*)\)\s*$", line)
                d["likes"].append([owner, mm.group(1) if mm else "?"])
            elif line.startswith("checkRoute"):
                d["routes"].append([owner, "checkRoute"])
            elif line.startswith("checkKiss"):
                d["routes"].append([owner, "checkKiss"])
            elif line.startswith("if"):
                txt = line.strip()
                if "isJump" not in txt:
                    d["other_if"].append([owner, txt])
            elif line.startswith("GOTO"):
                d["gotos"] += 1
                mm = re.search(r"next\((.*)\)\s*$", line)
                if not mm:
                    continue
                args = split_args(mm.group(1))
                if len(args) == 2:
                    tgt = RE_SCENE_CODE.search(args[0])
                    cond = args[1].strip()
                    if tgt and cond != "true":
                        d["cond_gotos"].append([owner, int(tgt.group(1)), cond])
            elif line.startswith("CHOICE"):
                mm = re.search(r"selectItem\((.*)\)\s*$", line)
                if mm:
                    a = split_args(mm.group(1))
                    tgt = RE_SCENE_CODE.search(a[1]) if len(a) > 1 else None
                    d["choices"].append([owner, a[0],
                                         int(tgt.group(1)) if tgt else None,
                                         a[2] if len(a) > 2 else "",
                                         a[3] if len(a) > 3 else ""])
            elif line.startswith("MAPDEST"):
                mm = re.search(r"moveItem\((.*)\)\s*$", line)
                if mm:
                    a = split_args(mm.group(1))
                    t2 = RE_SCENE_CODE.search(a[1]) if len(a) > 1 else None
                    t3 = RE_SCENE_CODE.search(a[2]) if len(a) > 2 else None
                    d["moves"].append([owner, a[0],
                                       int(t2.group(1)) if t2 else None,
                                       int(t3.group(1)) if t3 else None])
            elif line.startswith("DATE"):
                if "dateItem(" in line:
                    mm = re.search(r"dateItem\((.*)\)\s*$", line)
                    if mm:
                        a = split_args(mm.group(1))
                        t = RE_SCENE_CODE.search(a[1]) if len(a) > 1 else None
                        d["dates"].append([owner, a[0],
                                           int(t.group(1)) if t else None])
                else:
                    mm = re.search(r"date\((.*)\)\s*$", line)
                    if mm:
                        a = split_args(mm.group(1))
                        t = RE_SCENE_CODE.search(a[0]) if a else None
                        d["datecalls"].append([owner, int(t.group(1)) if t else None,
                                               a[1:] if len(a) > 1 else []])
    return d


def all_scene_set():
    """Все сцены всех глав ps2_source/chapters/ — для проверки целей."""
    s = set()
    for p in glob.glob(os.path.join(CHAPTERS, "chapter_*.txt")):
        with open(p, encoding="utf-8") as f:
            for line in f:
                m = RE_SCENE.match(line)
                if m:
                    s.add(int(m.group(1)))
    return s


def main():
    global_scenes = all_scene_set()
    res = {}
    problems = []
    for ch in CHS:
        cf, ef = find(ch, CHAPTERS), find(ch, EVENTS)
        cd = parse_chapter(cf)
        ed = parse_events(ef)
        cd.update({"file": os.path.basename(cf),
                   "events_file": os.path.basename(ef)})
        cd["ev"] = ed

        # сверка chapters <-> events_full
        cross = {"scenes": [cd["scenes"], ed["scenes"]],
                 "choices": [len(cd["choices"]), len(ed["choices"])],
                 "moves": [len(cd["moves"]), len(ed["moves"])],
                 "dates": [len(cd["dates"]), len(ed["dates"])]}
        mism = [k for k, v in cross.items() if v[0] != v[1]]
        cd["cross_mismatch"] = mism

        # цели: существуют ли сцены
        targets = []
        targets += [(o, g) for o, _, g in cd["choices"]]
        targets += [(o, g) for o, _, _, g in cd["moves"]]
        targets += [(o, g) for o, _, g in cd["dates"]]
        targets += [(o, g) for o, g in cd["dateprog"]]
        targets += [(o, g) for o, g in cd["nexts"]]
        cd["bad_targets"] = [[o, g] for o, g in targets if g not in global_scenes]

        # цели, ведущие в другие главы (владелец вне диапазона главы)
        own = set(cd["scene_list"])
        cd["foreign_targets"] = sorted({g for _, g in targets
                                        if g not in own and g in global_scenes})

        res[ch] = cd
        if mism:
            problems.append("ch%02d cross mismatch: %s" % (ch, mism))
        if cd["bad_targets"]:
            problems.append("ch%02d bad targets: %s" % (ch, cd["bad_targets"]))

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)

    print("chapter scenes(ch/ev) choiceMenus choices moves dates dateprog next "
          "like(ch) tndl like(ev) route otherIf condGoto badTargets")
    for ch in CHS:
        d = res[ch]
        e = d["ev"]
        menus = len({x[0] for x in d["choices"]})
        print("%d %d/%d %d %d %d %d %d %d %d %d %d %d %d %d %d"
              % (ch, d["scenes"], e["scenes"], menus, len(d["choices"]),
                 len(d["moves"]), len(d["dates"]), len(d["dateprog"]),
                 len(d["nexts"]), len(d["likes_ch"]), len(e["tndls"]),
                 len(e["likes"]), len(e["routes"]), len(e["other_if"]),
                 len(e["cond_gotos"]), len(d["bad_targets"])))
    print("global scenes known: %d" % len(global_scenes))
    print("problems: %s" % ("; ".join(problems) if problems else "none"))
    print("-> %s" % OUT)


if __name__ == "__main__":
    main()
