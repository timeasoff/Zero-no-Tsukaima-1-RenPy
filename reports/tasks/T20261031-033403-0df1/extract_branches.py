#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Извлечение развилок PS2-источника для глав 18..29 и 90/91.

Только чтение ps2_source/. Выход: JSON (raw) + markdown-фрагменты в raw.json,
финальный отчёт собирается вручную из raw.json.

Поля на каждую главу:
  scenes            — число сцен в файле
  choices           — [(owner, [(text, target)])]
  moves             — [(owner, [(name, target_real, target_raw, note)])]
  dates             — [(owner, [(name, target)])]
  dateprog          — [(owner, target)]
  nexts             — [(owner, target)]
  likes             — [(owner, name, value)]          (events_full LIKE)
  tndls             — [(owner, value)]                (events_full TNDL)
  routes            — [(owner, kind)]                 checkRoute/checkKiss
  other_if          — [(owner, text)]                 if(...) != if(isJump())
  cond_gotos        — [(owner, target, cond)]         next(...) с флагом != true
  header            — строка главы (core/extra scenes)
"""
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CHAPTERS = os.path.join(ROOT, "ps2_source", "chapters")
EVENTS = os.path.join(ROOT, "ps2_source", "events_full")
OUT = os.path.join(HERE, "raw_branches.json")

CHS = list(range(18, 30)) + [90, 91]

RE_SCENE = re.compile(r"^---- SCENE (\d+) ----")
RE_CHOICE = re.compile(r"^\s*【選択肢】(.+?)\s*→\s*scene\s+(\d+)")
RE_MOVE = re.compile(
    r"^\s*【移動】(.+?)\s*→\s*scene\s+(\d+)\s*(?:\(\(0x01000000\s*\+(\d+)\)\))?")
RE_DATE = re.compile(r"^\s*【デート】(.+?)\s*→\s*scene\s+(\d+)")
RE_DATEPROG = re.compile(r"^\s*【デート進行】\s*→\s*scene\s+(\d+)")
RE_NEXT = re.compile(r"^\s*→\s*next\s+scene\s+(\d+)")
RE_LIKE_CH = re.compile(r"^\s*【好感度】(.+?)\s+([+-]?\d+)")
RE_HDR = re.compile(r"^(core scenes|extra scenes)\s*:\s*(.+)$")


def find(pattern, folder):
    hits = glob.glob(os.path.join(folder, "chapter_%02d_*.txt" % pattern))
    if len(hits) != 1:
        raise SystemExit("chapter %s: %d files in %s" % (pattern, len(hits), folder))
    return hits[0]


def parse_chapter(path):
    d = {"header": [], "scenes": 0, "scene_list": [], "choices": [], "moves": [],
         "dates": [], "dateprog": [], "nexts": [], "likes_ch": []}
    owner = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            m = RE_HDR.match(line)
            if m:
                d["header"].append(m.group(0))
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
                d["moves"].append([owner, m.group(1).strip(), int(m.group(2)),
                                   real, "no-double-paren" if real is None else ""])
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


RE_E_SCENE = re.compile(r"^## SCENE (\d+)")


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


RE_SCENE_CODE = re.compile(r"\(0x01000000\s*\+(\d+)\)")


def parse_events(path):
    d = {"tndls": [], "likes": [], "routes": [], "other_if": [],
         "cond_gotos": [], "gotos": 0, "choices": [], "moves": [],
         "dates": [], "datecalls": [], "scenes": 0}
    owner = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            m = RE_E_SCENE.match(line)
            if m:
                owner = int(m.group(1))
                d["scenes"] += 1
                continue
            if owner is None:
                continue
            if line.startswith("TNDL "):
                mm = re.search(r"tndl\((.*)\)\s*$", line)
                d["tndls"].append([owner, mm.group(1) if mm else "?"])
            elif line.startswith("LIKE "):
                mm = re.search(r"like\((.*)\)\s*$", line)
                d["likes"].append([owner, mm.group(1) if mm else "?"])
            elif line.startswith("checkRoute "):
                d["routes"].append([owner, "checkRoute"])
            elif line.startswith("checkKiss "):
                d["routes"].append([owner, "checkKiss"])
            elif line.startswith("if "):
                txt = line[3:].strip()
                if txt != "if(isJump())":
                    d["other_if"].append([owner, txt])
            elif line.startswith("GOTO "):
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
            elif line.startswith("CHOICE "):
                mm = re.search(r"selectItem\((.*)\)\s*$", line)
                if mm:
                    a = split_args(mm.group(1))
                    tgt = RE_SCENE_CODE.search(a[1]) if len(a) > 1 else None
                    d["choices"].append([owner, a[0], int(tgt.group(1)) if tgt else None,
                                         a[2] if len(a) > 2 else ""])
            elif line.startswith("MAPDEST "):
                mm = re.search(r"moveItem\((.*)\)\s*$", line)
                if mm:
                    a = split_args(mm.group(1))
                    t2 = RE_SCENE_CODE.search(a[1]) if len(a) > 1 else None
                    t3 = RE_SCENE_CODE.search(a[2]) if len(a) > 2 else None
                    d["moves"].append([owner, a[0],
                                       int(t2.group(1)) if t2 else None,
                                       int(t3.group(1)) if t3 else None])
            elif line.startswith("DATE "):
                if "dateItem(" in line:
                    mm = re.search(r"dateItem\((.*)\)\s*$", line)
                    if mm:
                        a = split_args(mm.group(1))
                        t = RE_SCENE_CODE.search(a[1]) if len(a) > 1 else None
                        d["dates"].append([owner, a[0], int(t.group(1)) if t else None])
                else:
                    mm = re.search(r"date\((.*)\)\s*$", line)
                    if mm:
                        d["datecalls"].append([owner, mm.group(1)])
    return d


def main():
    res = {}
    for ch in CHS:
        cf = find(ch, CHAPTERS)
        ef = find(ch, EVENTS)
        cd = parse_chapter(cf)
        ed = parse_events(ef)
        cd.update({"file": os.path.basename(cf), "events_file": os.path.basename(ef)})
        cd["ev"] = ed
        res[ch] = cd
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)

    # краткая сводка в stdout (без японского текста)
    print("chapter | scenes | choice-menus | choices | moves | dates | dateprog "
          "| next | like(ch) | tndl | like(ev) | route | otherIf | condGoto")
    for ch in CHS:
        d = res[ch]
        e = d["ev"]
        menus = len({x[0] for x in d["choices"]})
        print("%d | %d | %d | %d | %d | %d | %d | %d | %d | %d | %d | %d | %d | %d"
              % (ch, d["scenes"], menus, len(d["choices"]), len(d["moves"]),
                 len(d["dates"]), len(d["dateprog"]), len(d["nexts"]),
                 len(d["likes_ch"]), len(e["tndls"]), len(e["likes"]),
                 len(e["routes"]), len(e["other_if"]), len(e["cond_gotos"])))
    print("-> %s" % OUT)


if __name__ == "__main__":
    main()
