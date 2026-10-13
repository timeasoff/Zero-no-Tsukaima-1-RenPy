# -*- coding: utf-8 -*-
"""Инвентаризация после git clean -fdx: что есть, чего не хватает.

Сверяет references/voice_id_map.csv с game/audio/voices/*.ogg,
а references/image_id_map.csv (filename) с game/images/**.
Вывод — в reports/recovery_inventory.md (UTF-8).
"""
import csv
import io
import os

OUT = "reports/recovery_inventory.md"
lines = []


def w(s=""):
    lines.append(s)


# --- голоса ---
voice_rows = []
with io.open("references/voice_id_map.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        voice_rows.append(row)

present = set()
vdir = "game/audio/voices"
if os.path.isdir(vdir):
    present = {fn for fn in os.listdir(vdir) if fn.endswith(".ogg")}

need = []
have = 0
no_pair = []
for r in voice_rows:
    name = (r.get("voice_name") or "").strip()
    if not name:
        continue
    fn = name + ".ogg"
    if fn in present:
        have += 1
    else:
        need.append(r)
        if not (r.get("voice_id") or "").strip():
            no_pair.append(name)

# по префиксам
from collections import Counter
pref = Counter()
for r in need:
    n = r["voice_name"]
    p = n.split("_")[0]
    pref[p] += 1

w("# Инвентаризация потерь (git clean -fdx)")
w()
w("## Голоса")
w()
w(f"- строк в манифесте (с именем): {len(voice_rows)}")
w(f"- есть .ogg: {have}")
w(f"- **НЕТ .ogg: {len(need)}** (из них без пары имя↔id: {len(no_pair)})")
w()
w("### Недостающие по префиксам")
w()
w("| префикс | нет |")
w("|---|---:|")
for p, c in sorted(pref.items(), key=lambda kv: -kv[1]):
    w(f"| `{p}` | {c} |")
w()

# --- картинки ---
w("## Картинки (image_id_map.csv)")
w()
img_rows = []
with io.open("references/image_id_map.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        img_rows.append(row)
named = [r for r in img_rows if (r.get("filename") or "").strip()]
img_missing = []
img_have = 0
for r in named:
    fn = r["filename"].strip()
    # ищем в game/images рекурсивно — однозвучные имена
    found = False
    for root, _dirs, files in os.walk("game/images"):
        if fn in files or (fn + ".webp") in files:
            found = True
            break
    if found:
        img_have += 1
    else:
        img_missing.append((r.get("image_id"), r.get("kind"), fn))
w(f"- строк в справочнике: {len(img_rows)}; с заполненным filename: {len(named)}")
w(f"- файл найден в game/images: {img_have}")
w(f"- **filename заполнен, файла НЕТ: {len(img_missing)}**")
if img_missing:
    w()
    w("| image_id | kind | filename |")
    w("|---|---|---|")
    for iid, kind, fn in img_missing[:40]:
        w(f"| {iid} | {kind} | `{fn}` |")
    if len(img_missing) > 40:
        w(f"| ... | | ещё {len(img_missing)-40} |")
w()

# --- gui / прочее ---
for d in ("game/gui", "game/audio/bgm", "game/audio/sfx", "game/video", "game/images"):
    c = 0
    if os.path.isdir(d):
        for _r, _dd, ff in os.walk(d):
            c += len(ff)
    else:
        c = -1
    w(f"- {d}: {c if c >= 0 else 'НЕТ ПАПКИ'}")
w()

io.open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("OK ->", OUT)
print("voices missing:", len(need), "images missing:", len(img_missing))
