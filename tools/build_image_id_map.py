#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZnT1 remaster - build/refresh references/image_id_map.csv (skill: assets).

Что делает
    Сканирует ps2_source/chapters/*.txt и собирает ВСЕ id картинок:
        [BG       stage    image=+K, ...]   -> kind=bg
        [EVENT_CG event    image=+K, ...]   -> kind=cg
        [SPRITE   layN     image=+K, ...]   -> kind=chara   (только с --include-chara)

    Для каждого id: сколько раз встречается (uses), в каких главах источника
    (chapters, номера глав источника через `;`), первая находка (source).

    Файл пересоздаётся с сохранением ручных правок пользователя:
    колонки filename и notes (а также строки, не найденные в источнике)
    не трогаются — именно там человек фиксирует своё сопоставление.

Запуск (из корня проекта):
    python tools/build_image_id_map.py                 # bg + cg
    python tools/build_image_id_map.py --include-chara # + спрайты
    python tools/build_image_id_map.py --dry-run       # только статистика

Формат references/image_id_map.csv (UTF-8, строки `#` — комментарии):
    image_id,kind,filename,source,notes,uses,chapters
    28,bg,forest,chapter_02 [BG stage image=+28],,12,02;03;05

Консольный вывод — только ASCII/кириллица (PowerShell здесь cp1251).
"""
import argparse
import csv
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT, "ps2_source", "chapters")
MAP_PATH = os.path.join(ROOT, "references", "image_id_map.csv")

FIELDNAMES = ["image_id", "kind", "filename", "source", "notes", "uses", "chapters"]

LINE_RE = re.compile(r"^\s*\[(BG|EVENT_CG|SPRITE)\s+(\S+)[^\]]*?image=\+(\d+)")
CHNUM_RE = re.compile(r"chapter_(\d+)")

KIND_ORDER = {"bg": 0, "cg": 1, "chara": 2}


def scan_source():
    """-> {(image_id:int): {"kinds": set, "uses": int, "chapters": set, "source": str}}"""
    agg = {}
    if not os.path.isdir(SRC_DIR):
        print("ERROR: source folder not found: %s" % os.path.relpath(SRC_DIR, ROOT))
        sys.exit(1)
    for name in sorted(os.listdir(SRC_DIR)):
        if not name.endswith(".txt"):
            continue
        m = CHNUM_RE.match(name)
        if not m:
            continue
        ch_num = m.group(1)
        path = os.path.join(SRC_DIR, name)
        with io.open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                hit = LINE_RE.match(line)
                if not hit:
                    continue
                tag, _layer, num = hit.group(1), hit.group(2), int(hit.group(3))
                kind = {"BG": "bg", "EVENT_CG": "cg", "SPRITE": "chara"}[tag]
                rec = agg.setdefault(num, {
                    "kinds": set(), "uses": 0, "chapters": set(), "source": "",
                })
                rec["kinds"].add(kind)
                rec["uses"] += 1
                rec["chapters"].add(ch_num)
                if not rec["source"]:
                    rec["source"] = "%s [%s %s image=+%d]" % (
                        ch_num, tag, hit.group(2), num)
    return agg


def read_existing():
    """-> {(image_id:int): row(dict)} из существующего справочника (без # строк)."""
    rows = {}
    if not os.path.isfile(MAP_PATH):
        return rows
    with io.open(MAP_PATH, encoding="utf-8", errors="replace") as fh:
        reader = csv.DictReader(l for l in fh if not l.lstrip().startswith("#"))
        for row in reader:
            try:
                rows[int(row.get("image_id", ""))] = row
            except (TypeError, ValueError):
                continue
    return rows


def build(include_chara, dry_run):
    agg = scan_source()
    existing = read_existing()

    ids = sorted(agg)
    missing = sorted(set(existing) - set(ids))

    out_rows = []
    stats = {"bg": 0, "cg": 0, "chara": 0, "filled": 0, "kept": 0}
    for num in ids:
        rec = agg[num]
        kinds = set(rec["kinds"])
        if not include_chara:
            kinds -= {"chara"}
            if not kinds:
                # id виден только как спрайт: в этот проход не попадает,
                # но уже созданную строку пользователя сохраняем как есть
                if num in existing:
                    out_rows.append({k: (existing[num].get(k) or "")
                                     for k in FIELDNAMES})
                    stats["kept"] += 1
                continue
        kind = "|".join(sorted(kinds, key=lambda k: KIND_ORDER.get(k, 9)))
        old = existing.get(num, {})
        filename = (old.get("filename") or "").strip()
        notes = (old.get("notes") or "").strip()
        row = {
            "image_id": str(num),
            "kind": kind,
            "filename": filename,
            "source": rec["source"],
            "notes": notes,
            "uses": str(rec["uses"]),
            "chapters": ";".join(sorted(rec["chapters"])),
        }
        out_rows.append(row)
        for k in kinds:
            stats[k] = stats.get(k, 0) + 1
        if filename:
            stats["filled"] += 1

    # строки, созданные вручную и не найденные в текущем скане, сохраняем как есть
    for num in missing:
        old = dict(existing[num])
        out_rows.append({k: (old.get(k) or "") for k in FIELDNAMES})
        stats["kept"] += 1

    out_rows.sort(key=lambda r: (
        min(KIND_ORDER.get(k, 9) for k in (r["kind"] or "").split("|")),
        int(r["image_id"]) if (r["image_id"] or "").isdigit() else 10 ** 9))

    print("scanned ids: total=%d bg=%d cg=%d chara=%d (include_chara=%s)"
          % (len(ids), stats.get("bg", 0), stats.get("cg", 0),
             stats.get("chara", 0), include_chara))
    print("rows to write: %d | filename filled: %d | kept (not in source): %d"
          % (len(out_rows), stats["filled"], stats["kept"]))
    if dry_run:
        print("dry-run: %s NOT written" % os.path.relpath(MAP_PATH, ROOT))
        return

    os.makedirs(os.path.dirname(MAP_PATH), exist_ok=True)
    header = [
        "# references/image_id_map.csv - id картинок PS2 -> имя в ремастере",
        "# Колонки: image_id,kind,filename,source,notes,uses,chapters",
        "#   image_id - K из image=+K в ps2_source/chapters/*.txt",
        "#   kind     - bg | cg | chara (составные виды через |)",
        "#   filename - ИМЯ В ПРОЕКТЕ: голое базовое имя без пути и расширения;",
        "#              заполняется по доказательной сверке с PS2/эталоном (fade_fx(\"forest\"),",
        "#              dissolve_fx(\"l_s_forest\", type=\"cg\")); пусто = ассета в проекте нет,",
        "#              в скриптах используется заглушка id(IMAGE_ID))",
        "#   source   - первая находка в источнике (генерируется)",
        "#   notes    - доказательство сопоставления / PROVISIONAL (при сверке)",
        "#   uses     - сколько раз встречается в источнике (генерируется)",
        "#   chapters - главы источника через ; (генерируется)",
        "# Пересоздаётся: python tools/build_image_id_map.py [--include-chara]",
        "# Ручные колонки filename/notes и нетронутые строки сохраняются.",
        "# Заглушки в скриптах заменяются: python tools/replace_bg_placeholders.py --apply",
    ]
    tmp = MAP_PATH + ".tmp"
    with io.open(tmp, "w", encoding="utf-8", newline="") as fh:
        for line in header:
            fh.write(line + "\n")
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        for row in out_rows:
            writer.writerow(row)
    os.replace(tmp, MAP_PATH)
    print("written: %s" % os.path.relpath(MAP_PATH, ROOT))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--include-chara", action="store_true",
                    help="also emit sprite (SPRITE layN) ids")
    ap.add_argument("--dry-run", action="store_true",
                    help="scan and print stats only")
    args = ap.parse_args()
    build(args.include_chara, args.dry_run)


if __name__ == "__main__":
    main()
