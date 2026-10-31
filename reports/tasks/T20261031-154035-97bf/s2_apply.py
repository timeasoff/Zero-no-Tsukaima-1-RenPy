#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Применение плана вставок s1_insert_plan.csv (S2-S5, T20261031-154035-97bf).

--chapter N   глава (номер папки game/chapters/N)
--apply       запись файлов (без него — dry-run: печать операций)

Строки плана status=PLAN: вставка `$ tndl(...)` после anchor_line
(с валидацией содержимого якоря по anchor_type) + удаление
стale-комментария, парного к вставке (stale_line).

Операции применяются по файлу в ОБРАТНОМ порядке номеров строк
(удаление строки > вставки не сдвигает якорь).
При любом конфликте (якорь не совпал с ожидаемым содержимым,
дубль в одной точке, цель удаления не комментарий) — операция
не применяется, выводится проблема, команда завершается с кодом 1
и файл НЕ пишется.
"""
import argparse
import csv
import re
import sys
from pathlib import Path

TASK_DIR = Path(__file__).resolve().parent
ROOT = TASK_DIR.parents[2]
PLAN = TASK_DIR / "s1_insert_plan.csv"


def fmt_value(v):
    return "None" if v == "" else str(int(v))


def load_rows(chapter):
    rows = []
    with PLAN.open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["status"] == "PLAN" and r["chapter"] == chapter:
                rows.append(r)
    return rows


def anchor_ok(anchor_type, anchor):
    if anchor_type == "label":
        return bool(re.match(r"^label ch\d+:", anchor))
    if anchor_type.startswith("syn"):
        return bool(re.match(r"^\s*\$ ?update_sympathy\(", anchor))
    if anchor_type == "dialogue":
        return bool(re.match(r'^\s*[A-Za-z_][\w.]* "', anchor))
    if anchor_type == "stmt":
        return bool(anchor.strip() and not anchor.lstrip().startswith("#"))
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", required=True)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    ch = args.chapter

    rows = load_rows(ch)
    if not rows:
        print("ERROR: no PLAN rows for chapter", ch)
        return 1

    by_file = {}
    for r in rows:
        by_file.setdefault(r["insert_file"], {"ins": [], "del": []})
        by_file[r["insert_file"]]["ins"].append(r)
        if r["stale_file"]:
            by_file[r["insert_file"]]["del"].append(int(r["stale_line"]))

    problems = []
    total_ins = total_del = 0
    edited = []

    for fname in sorted(by_file):
        ops = by_file[fname]
        path = ROOT / "game" / "chapters" / ch / fname
        if not path.exists():
            problems.append("%s: file missing" % fname)
            continue
        lines = path.read_text(encoding="utf-8").splitlines()

        plan_ops = []           # (line_1based, "ins"/"del", payload)
        anchors_seen = set()
        for r in ops["ins"]:
            ln = int(r["insert_after"])
            if not 1 <= ln <= len(lines):
                problems.append("%s:%d anchor out of range" % (fname, ln))
                continue
            anchor = lines[ln - 1]
            at = r["anchor_type"]
            if not anchor_ok(at, anchor):
                problems.append("%s:%d anchor_type=%s unexpected: %r"
                                % (fname, ln, at, anchor[:80]))
                continue
            if ln in anchors_seen:
                problems.append("%s:%d duplicate insert anchor" % (fname, ln))
                continue
            anchors_seen.add(ln)
            if at == "label":
                indent = "    "
            elif r["indent"]:
                indent = r["indent"]
            else:
                indent = anchor[: len(anchor) - len(anchor.lstrip())]
            text = indent + "$ tndl(%s)" % fmt_value(r["value"])
            plan_ops.append((ln, "ins", text))
            total_ins += 1
            print("  INS  %s:%-5d after  [%s] %s"
                  % (fname, ln, at, text.strip()))

        seen_del = set()
        for dl in ops["del"]:
            if dl in seen_del:
                continue
            seen_del.add(dl)
            if not 1 <= dl <= len(lines):
                problems.append("%s:%d delete line out of range" % (fname, dl))
                continue
            content = lines[dl - 1]
            if "tndl(" not in content or not content.lstrip().startswith("#"):
                problems.append("%s:%d delete target is not a tndl-comment: %r"
                                % (fname, dl, content[:80]))
                continue
            plan_ops.append((dl, "del", None))
            total_del += 1
            print("  DEL  %s:%-5d %s" % (fname, dl, content.strip()[:70]))

        # обратный порядок: удалять/вставлять от больших номеров строк
        plan_ops.sort(key=lambda x: (-x[0], 0 if x[1] == "del" else 1))
        for ln, kind, payload in plan_ops:
            if kind == "del":
                del lines[ln - 1]
            else:
                lines.insert(ln, payload)
        if any(k == "ins" for _, k, _ in plan_ops) or any(
                k == "del" for _, k, _ in plan_ops):
            edited.append((path, lines))

    if problems:
        print("\nPROBLEMS (%d) — nothing written:" % len(problems))
        for p in problems:
            print("  !", p)
        return 1

    print("\nplanned: %d inserts, %d stale deletions, %d files"
          % (total_ins, total_del, len(edited)))
    if not args.apply:
        print("DRY-RUN — pass --apply to write")
        return 0

    for path, lines in edited:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("written:", path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
