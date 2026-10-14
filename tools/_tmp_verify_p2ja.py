# -*- coding: utf-8 -*-
# Сверка JA gen_p2_tl.py с каноном v2: исправленный сбор канона
# (граница реплики — строка с [voice N]), посимвольный дифф, автофикс gen из канона.
import io, re, sys, ast

SRC = "ps2_source/chapters/chapter_04_女の戦い.txt"
GEN = "tools/gen_p2_tl.py"

src = io.open(SRC, encoding="utf-8").read().splitlines()

canon = {}
for idx, ln in enumerate(src):
    m = re.search(r"\[voice (\d+)\]\s*$", ln.rstrip())
    if not m:
        continue
    vid = int(m.group(1))
    body = ln[:m.start()].rstrip()
    parts = [body.split("：", 1)[-1] if "：" in body else body]
    j = idx - 1
    while j >= 0:
        t = src[j]
        # границы: пусто / декорация / заголовок сцены / реплика с чужим voice / новый говорящий
        if not t or t.startswith(" ") or t.startswith("-") or "[voice" in t or "：" in t:
            if "：" in t and "[voice" not in t:
                parts.insert(0, t.split("：", 1)[1])
            break
        parts.insert(0, t)
        j -= 1
    canon[vid] = "".join(parts)

gen_text = io.open(GEN, encoding="utf-8").read()
gen_lines = gen_text.splitlines()
voices = dict(re.findall(r'\("(ch3\.2_[a-z]+_\d+)",\s*(\d+)\)', gen_text))

# парс ROWS
rows = []
i = 0
while i < len(gen_lines):
    ln = gen_lines[i]
    if ln.strip().startswith('("dialogs"') or ln.strip().startswith('("thoughs"') or ln.strip().startswith('("choises"'):
        start = i
        block = [ln]
        while not block[-1].rstrip().endswith("),"):
            i += 1
            block.append(gen_lines[i])
        rows.append((start, i, "\n".join(block)))
    i += 1

row_data = {}   # old -> (start, end, bucket, ja, ru)
for start, end, blk in rows:
    tup = ast.literal_eval(blk.strip().rstrip(","))
    row_data[tup[1]] = (start, end, tup[0], tup[2], tup[3])

script = io.open("game/chapters/3/script-ch3_2.rpy", encoding="utf-8").read()
pairs = re.findall(r'voice "ch3\.2_([a-z]+)_(\d+)"\s*\n\s*[a-z]+ "((?:[^"\\]|\\.)*)"', script)

def show_diff(a, b, tag, key):
    print("MISMATCH", key, tag)
    n = max(len(a), len(b))
    diffs = []
    for k in range(n):
        ca = a[k] if k < len(a) else None
        cb = b[k] if k < len(b) else None
        if ca != cb:
            diffs.append("pos%d: got %s canon %s" % (
                k, "U+%04X" % ord(ca) if ca else "<none>",
                "U+%04X" % ord(cb) if cb else "<none>"))
    for d in diffs[:6]:
        print("   ", d)

AUTO = "--fix" in sys.argv
errors = 0
fixed = 0
for spk, num, old in pairs:
    key = "ch3.2_%s_%s" % (spk, num)
    vid = int(voices.get(key, 0))
    if vid == 0 or vid not in canon:
        print("MISSING", key, vid)
        errors += 1
        continue
    if old not in row_data:
        print("NO_ROW", key, old[:50])
        errors += 1
        continue
    start, end, bucket, ja, ru = row_data[old]
    c = canon[vid]
    if ja != c:
        errors += 1
        show_diff(ja, c, "vid %d" % vid, key)
        if AUTO:
            # заменить JA-строку в gen строке end (третий элемент кортежа)
            # пересобрать весь блок
            blk = gen_lines[start:end + 1]
            # найдём JA-строку: первая после старта, содержащая только строку с '"',
            # индекс: 0=old, 1=ja, 2=ru (однострочные) либо многострочные
            # проще: заменить содержимое кавычек в строке, чей индекс=старт+1,
            # если строка на старте заканчивается на '",'
            if gen_lines[start].rstrip().endswith('",'):
                ja_line_idx = start + 1
            else:
                ja_line_idx = start + 1  # multi-line: old, ja, ru каждый своей строкой
            indent = re.match(r"\s*", gen_lines[ja_line_idx]).group(0)
            gen_lines[ja_line_idx] = indent + '"%s",' % c
            fixed += 1

if AUTO and fixed:
    io.open(GEN, "w", encoding="utf-8").write("\n".join(gen_lines) + "\n")
    print("AUTO-FIXED rows:", fixed)

# меню/мысли: показать строки источника для выборов
for probe in ("確かに気になるな", "確実に気になる", "まあ、大丈夫だろ", "ちょっとは心配かな"):
    hit = [n for n, t in enumerate(src, 1) if probe in t]
    print("probe", repr(probe), "->", hit if hit else "NOT FOUND")

print("RESULT:", "OK" if errors == 0 else "ERRORS=%d" % errors)
