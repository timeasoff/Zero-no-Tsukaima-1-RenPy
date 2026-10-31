# S4 — сборка канон-таблицы симпатий: references/sympathy_canon.csv
# Источники: CSV подзадач S1 (chapter_02) и S3 (chapter_03..06).
# Запуск из корня проекта: python reports/tasks/T20261031-054249-c81b/s4_assemble.py
import csv, sys, io, collections

BASE = "reports/tasks/T20261031-054249-c81b"
SRC = [f"{BASE}/sympathy_canon_ch02.csv", f"{BASE}/sympathy_canon_ch03_06.csv"]
OUT = "references/sympathy_canon.csv"

FIELDS = ["chapter_source", "project_chapter", "scene", "char_ja", "char_key",
          "value", "branch_kind", "menu_owner_scene", "choice_text",
          "source_line", "events_full_line", "notes"]

rows = []
for p in SRC:
    with io.open(p, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            if list(r.keys()) != FIELDS:
                sys.exit(f"FATAL: неожиданные колонки в {p}: {list(r.keys())}")
            rows.append({k: (r[k] or "").strip() for k in FIELDS})

# нормализация chapter_source: "chapter_03" -> "chapter_03_黒髪の来訪者"
import re, glob
stems = {}
for p in glob.glob("ps2_source/chapters/*.txt"):
    m = re.match(r"ps2_source/chapters/(chapter_\d+)_", p)
    if m:
        stems[m.group(1)] = re.match(r"ps2_source/chapters/(.+)\.txt", p).group(1)
for r in rows:
    cs = r["chapter_source"]
    if cs != stems.get(cs):
        full = stems.get(cs)
        if full is None:
            # может, уже полное имя
            pref = re.match(r"(chapter_\d+)", cs)
            full = stems.get(pref.group(1)) if pref else None
        if full is None:
            sys.exit(f"FATAL: неизвестный chapter_source: {cs}")
        r["chapter_source"] = full

# контроль: количество строк = числу 【好感度】 в ps2_source/chapters
# chapter_00 — системный файл с синтаксической легендой ("【好感度】name add"
# в сцене-документации), реальных событий симпатии там нет — исключаем явно.
SKIP = {"chapter_00_システム（エンジン・メニュー）"}
canon_counts = collections.Counter()
for p in glob.glob("ps2_source/chapters/*.txt"):
    stem = re.match(r"ps2_source/chapters/(.+)\.txt", p).group(1)
    if stem in SKIP:
        continue
    n = sum(1 for line in io.open(p, encoding="utf-8")
            if re.match(r"\s*【好感度】", line))
    if n:
        canon_counts[stem] = n

csv_counts = collections.Counter(r["chapter_source"] for r in rows)
print("=== контроль количества строк (источник vs CSV) ===")
ok = True
for name, n in sorted(canon_counts.items()):
    val = csv_counts.get(name, 0)
    flag = "OK" if val == n else "MISMATCH"
    if flag != "OK":
        ok = False
    print(f"  {name}: источник {n} / CSV {val}  {flag}")
extra = set(csv_counts) - set(canon_counts)
if extra:
    ok = False
    print(f"  ЛИШНИЕ главы в CSV: {sorted(extra)}")
print(f"  ВСЕГО: источник {sum(canon_counts.values())} / CSV {len(rows)}")
if len(rows) != sum(canon_counts.values()):
    ok = False

if not ok:
    print("RESULT: CONTROL FAILED — не пишем выход")
    sys.exit(1)

with io.open(OUT, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL,
                       lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow(r)

# сводка для отчёта
per_ch = collections.defaultdict(lambda: collections.Counter())
summ = collections.defaultdict(lambda: [0, 0, 0])  # n, sum+, sum-
for r in rows:
    v = int(r["value"])
    key = (r["project_chapter"], r["char_key"])
    per_ch[r["project_chapter"]][r["char_key"]] += 1
    s = summ[key]
    s[0] += 1
    if v > 0:
        s[1] += v
    else:
        s[2] += v
print("=== сводка (проектная глава: персонаж n / Σ+ / Σ−) ===")
for ch in sorted(per_ch, key=lambda x: (len(x), x)):
    parts = []
    for c, n in sorted(per_ch[ch].items()):
        s = summ[(ch, c)]
        parts.append(f"{c} {n}({s[1]:+d}{s[2]:+d})")
    print(f"  гл.{ch}: " + ", ".join(parts))
print(f"\nWROTE: {OUT}  строк: {len(rows)}")
print("RESULT: OK" if ok else "RESULT: FAILED")
