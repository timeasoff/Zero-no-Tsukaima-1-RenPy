# -*- coding: utf-8 -*-
# Сверка JA из tools/gen_p3_tl.py с каноном:
#  - озвученные реплики — ps2_source/chapters (граница — строка с [voice N]);
#  - безголосые реплики и мысли — ps2_source/events_full (talk(..., null, ...));
#  - пункты выбора — ps2_source/events_full (selectItem).
# --fix: переписать JA-строки gen_p3_tl.py из канона.
import io, re, sys, ast, importlib.util

SRC = "ps2_source/chapters/chapter_04_女の戦い.txt"
EVT = "ps2_source/events_full/chapter_04_女の戦い.txt"
GEN = "tools/gen_p3_tl.py"
SCR = "game/chapters/3/script-ch3_3.rpy"

# ---- канон: озвученные реплики ----
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
        if not t or t.startswith(" ") or t.startswith("-") or "[voice" in t or "：" in t:
            if "：" in t and "[voice" not in t:
                parts.insert(0, t.split("：", 1)[1])
            break
        parts.insert(0, t)
        j -= 1
    canon[vid] = "".join(parts)

# ---- events: безголосые реплики/мыслi + выборы (сцены 1297..1321) ----
evt = io.open(EVT, encoding="utf-8").read().splitlines()
canon_novoice, canon_choices = [], []
scene = 0
for ln in evt:
    ms = re.match(r"## SCENE (\d+)", ln)
    if ms:
        scene = int(ms.group(1))
        continue
    if not (1297 <= scene <= 1321):
        continue
    md = re.match(r'DIALOGUE\s+talk\("[^"]*",\s*null,\s*"((?:[^"\\]|\\.)*)",\s*null\)', ln)
    if md:
        canon_novoice.append(md.group(1).replace("\\n", ""))
    mc = re.match(r'CHOICE\s+selectItem\("([^"]*)"', ln)
    if mc:
        canon_choices.append(mc.group(1))

# ---- gen: загрузка модуля + текст для --fix ----
gen_text = io.open(GEN, encoding="utf-8").read()
gen_lines = gen_text.splitlines()
spec = importlib.util.spec_from_file_location("gen_p3_tl", GEN)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
rows = mod.ROWS
voices = dict(mod.VOICES)
row_by_old = {old: (bucket, ja, ru) for bucket, old, ja, ru in rows}

def fix_ja(old, new_ja):
    for i, ln in enumerate(gen_lines):
        if ln.rstrip().endswith('"%s",' % old):
            jline = gen_lines[i + 1]
            indent = re.match(r"\s*", jline).group(0)
            gen_lines[i + 1] = indent + '"%s",' % new_ja
            return True
    return False

def show_diff(a, b, tag, key):
    print("MISMATCH", key, tag)
    n = max(len(a), len(b))
    for k in range(n):
        ca = a[k] if k < len(a) else None
        cb = b[k] if k < len(b) else None
        if ca != cb:
            print("    pos%d: got %s canon %s" % (
                k, "U+%04X" % ord(ca) if ca else "<none>",
                "U+%04X" % ord(cb) if cb else "<none>"))

AUTO = "--fix" in sys.argv
errors = 0
fixed = 0

# 1) озвученные
script = io.open(SCR, encoding="utf-8").read()
pairs = re.findall(
    r'voice "ch3\.3_([a-z]+)_(\d+)"\s*\n\s*(?:s|l|si|k|t|ha|th) "((?:[^"\\]|\\.)*)"',
    script)
for spk, num, old in pairs:
    key = "ch3.3_%s_%s" % (spk, num)
    vid = int(voices.get(key, 0))
    if vid == 0 or vid not in canon:
        print("MISSING", key, vid)
        errors += 1
        continue
    if old not in row_by_old:
        print("NO_ROW", key, old[:60])
        errors += 1
        continue
    ja = row_by_old[old][1]
    c = canon[vid]
    if ja != c:
        errors += 1
        show_diff(ja, c, "vid %d" % vid, key)
        if AUTO and fix_ja(old, c):
            fixed += 1
print("voiced lines checked:", len(pairs))

# 2) безголосые + мысли (в порядке следования строк скрипта)
novoice_rows = [r for r in rows
                if r[0] == "thoughs" or re.search(r"\{#ch3\.3_[kt]h?_v\d+\}", r[1])
                or re.search(r"\{#ch3\.3_ha_v\d+\}", r[1])]
print("novoice rows:", len(novoice_rows), "canon novoice:", len(canon_novoice))
if len(novoice_rows) != len(canon_novoice):
    print("ERROR: novoice count mismatch")
    errors += 1
else:
    for (bucket, old, ja, ru), c in zip(novoice_rows, canon_novoice):
        if ja != c:
            errors += 1
            show_diff(ja, c, "novoice", old)
            if AUTO and fix_ja(old, c):
                fixed += 1

# 3) пункты выбора
choise_rows = [r for r in rows if r[0] == "choises"]
print("choise rows:", len(choise_rows), "canon choices:", len(canon_choices))
if len(choise_rows) != len(canon_choices):
    print("ERROR: choise count mismatch")
    errors += 1
else:
    for (bucket, old, ja, ru), c in zip(choise_rows, canon_choices):
        if ja != c:
            errors += 1
            show_diff(ja, c, "choice", old)
            if AUTO and fix_ja(old, c):
                fixed += 1

if AUTO and fixed:
    io.open(GEN, "w", encoding="utf-8").write("\n".join(gen_lines) + "\n")
    print("AUTO-FIXED rows:", fixed)

print("RESULT:", "OK" if errors == 0 else "ERRORS=%d" % errors)
