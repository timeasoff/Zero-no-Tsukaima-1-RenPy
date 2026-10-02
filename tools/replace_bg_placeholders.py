#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZnT1 remaster - replace background placeholders id(K) with real names
(skill: assets).

Как это работает
    В скриптах части фон/CG без сопоставления пишется заглушкой:

        $ fade_fx("id(1145)")
        $ dissolve_fx("id(148)", type="cg")

    Человек заполняет колонку filename в references/image_id_map.csv, после
    чего скрипт подставляет реальные имена во всех .rpy:

        $ fade_fx("bg_tristania_night")

Запуск (из корня проекта):
    python tools/replace_bg_placeholders.py            # dry-run: что найдено
    python tools/replace_bg_placeholders.py --apply    # внести замены

    --map  <csv>   другой файл справочника
    --out  <md>    куда писать подробный отчёт
                    (по умолчанию reports/bg_placeholders.md)

Правила
    * dry-run НИЧЕГО не меняет (по умолчанию);
    * заменяются только заглушки, чей id заполнен в справочнике;
    * незаполненные id остаются заглушками (это норма, пока идёт сверка);
    * заглушка внутри строки tl (game/tl/**) НЕ трогается: её old в
      translate-блоке пришлось бы синхронизировать вручную — такой случай
      попадает в отчёт как TO-FIX;
    * файлы пишутся в UTF-8 без изменения структуры (только токен id(K)).

Консольный вывод — только ASCII/кириллица (PowerShell здесь cp1251),
детали — в UTF-8 отчёте.
"""
import argparse
import csv
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME = os.path.join(ROOT, "game")
DEFAULT_MAP = os.path.join(ROOT, "references", "image_id_map.csv")
DEFAULT_OUT = os.path.join(ROOT, "reports", "bg_placeholders.md")

PLACEHOLDER_RE = re.compile(r"\bid\((\d+)\)")


def read_map(path):
    """-> {image_id: filename} только для заполненных строк."""
    filled = {}
    all_ids = set()
    if not os.path.isfile(path):
        return filled, all_ids
    with io.open(path, encoding="utf-8", errors="replace") as fh:
        reader = csv.DictReader(l for l in fh if not l.lstrip().startswith("#"))
        for row in reader:
            raw = (row.get("image_id") or "").strip()
            if not raw.isdigit():
                continue
            num = int(raw)
            all_ids.add(num)
            name = (row.get("filename") or "").strip()
            if name:
                filled[num] = name
    return filled, all_ids


def iter_rpy(base):
    for dirpath, _dirs, filenames in os.walk(base):
        for name in sorted(filenames):
            if name.endswith(".rpy"):
                yield os.path.join(dirpath, name)


def collect_hits(filled):
    """-> [(relpath, lineno, [ids])] по всем .rpy в game/."""
    hits = []
    for path in iter_rpy(GAME):
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        try:
            with io.open(path, encoding="utf-8", errors="replace") as fh:
                lines = fh.read().splitlines()
        except OSError:
            continue
        for i, line in enumerate(lines, 1):
            ids = [int(m) for m in PLACEHOLDER_RE.findall(line)]
            if ids:
                hits.append((rel, i, ids, line))
    return hits


def apply_replacements(filled, hits):
    """Заменяет id(K) -> имя в НЕ-tl файлах. -> (changed_files, replaced)."""
    by_file = {}
    for rel, _i, ids, _line in hits:
        if rel.startswith("game/tl/"):
            continue
        for num in ids:
            if num in filled:
                by_file.setdefault(rel, set()).add(num)

    changed_files, replaced = 0, 0
    for rel, nums in sorted(by_file.items()):
        path = os.path.join(ROOT, rel.replace("/", os.sep))
        with io.open(path, encoding="utf-8", errors="strict", newline="") as fh:
            text = fh.read()

        def _sub(match):
            num = int(match.group(1))
            return filled[num] if num in nums else match.group(0)

        new_text = PLACEHOLDER_RE.sub(_sub, text)
        if new_text == text:
            continue
        before = len(PLACEHOLDER_RE.findall(text))
        after = len(PLACEHOLDER_RE.findall(new_text))
        with io.open(path, "w", encoding="utf-8", errors="strict", newline="") as fh:
            fh.write(new_text)
        changed_files += 1
        replaced += (before - after)
    return changed_files, replaced


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="write replacements (default: dry-run)")
    ap.add_argument("--map", dest="map_path", default=DEFAULT_MAP)
    ap.add_argument("--out", dest="out_path", default=DEFAULT_OUT)
    args = ap.parse_args()

    filled, all_ids = read_map(args.map_path)
    if not all_ids:
        print("ERROR: map not found or empty: %s"
              % os.path.relpath(args.map_path, ROOT))
        print("       run: python tools/build_image_id_map.py")
        sys.exit(1)

    hits = collect_hits(filled)
    mapped_hits, unmapped_hits, tl_hits = [], [], []
    mapped_ph, unmapped_ph, tl_ph = 0, 0, 0
    for rel, i, ids, line in hits:
        if rel.startswith("game/tl/"):
            tl_hits.append((rel, i, ids, line))
            tl_ph += len(ids)
            continue
        if any(n in filled for n in ids):
            mapped_hits.append((rel, i, ids))
        else:
            unmapped_hits.append((rel, i, ids))
        for num in ids:
            if num in filled:
                mapped_ph += 1
            else:
                unmapped_ph += 1

    print("map: %d ids, %d filled with a name"
          % (len(all_ids), len(filled)))
    print("placeholders in scripts: files=%d mapped=%d unmapped=%d in_tl=%d"
          % (len({r for r, _i, _n in mapped_hits + unmapped_hits}),
             mapped_ph, unmapped_ph, tl_ph))

    replaced = 0
    changed_files = 0
    if args.apply and mapped_ph:
        changed_files, replaced = apply_replacements(filled, hits)
        print("applied: files changed=%d, placeholders replaced=%d"
              % (changed_files, replaced))
    elif mapped_ph:
        print("dry-run: run again with --apply to replace %d placeholder(s)"
              % mapped_ph)

    # UTF-8 отчёт с деталями
    os.makedirs(os.path.dirname(args.out_path), exist_ok=True)
    with io.open(args.out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write("# Заглушки id(K) — сверка с references/image_id_map.csv\n\n")
        fh.write("* справочник: `%s` (id: %d, заполнено имя: %d)\n"
                 % (os.path.relpath(args.map_path, ROOT), len(all_ids), len(filled)))
        fh.write("* режим: %s\n\n" % ("APPLY" if args.apply else "DRY-RUN"))
        fh.write("## Заменено в этом прогоне\n\n")
        if not args.apply:
            fh.write("_dry-run: ничего не изменено_\n\n")
        else:
            fh.write("* файлов изменено: %d\n* заглушек заменено: %d\n\n"
                     % (changed_files, replaced))
        fh.write("## Готово к замене (есть имя в справочнике)\n\n")
        if mapped_hits:
            fh.write("| файл | строка | id |\n|---|---|---|\n")
            for rel, i, ids in mapped_hits:
                fh.write("| %s | %d | %s |\n"
                         % (rel, i, ", ".join("id(%d)" % n for n in ids)))
        else:
            fh.write("_нет_\n")
        fh.write("\n## Остаются заглушками (filename пуст в справочнике)\n\n")
        if unmapped_hits:
            fh.write("| файл | строка | id |\n|---|---|---|\n")
            for rel, i, ids in unmapped_hits:
                fh.write("| %s | %d | %s |\n"
                         % (rel, i, ", ".join("id(%d)" % n for n in ids)))
        else:
            fh.write("_нет_\n")
        fh.write("\n## Заглушки внутри game/tl (old/new синхронизировать вручную)\n\n")
        if tl_hits:
            fh.write("| файл | строка | id |\n|---|---|---|\n")
            for rel, i, ids, _line in tl_hits:
                fh.write("| %s | %d | %s |\n"
                         % (rel, i, ", ".join("id(%d)" % n for n in ids)))
        else:
            fh.write("_нет_\n")
        fh.write("\n## Статусы id из справочника\n\n")
        fh.write("* заполнено имя: %d из %d\n" % (len(filled), len(all_ids)))
        open_ids = sorted(all_ids - set(filled))
        if open_ids:
            fh.write("* ждут сопоставления (%d): %s\n"
                     % (len(open_ids),
                        ", ".join(str(n) for n in open_ids)))
    print("report: %s" % os.path.relpath(args.out_path, ROOT))


if __name__ == "__main__":
    main()
