import re, os, json

ROOT = "/workspace/.tmp/opencode/review-ch2-5"

def parse_tl(path):
    d = {}
    old = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r'\s*old\s+"(.*)"\s*$', line.rstrip("\n"))
            if m:
                old = m.group(1)
                continue
            m = re.match(r'\s*new\s+"(.*)"\s*$', line.rstrip("\n"))
            if m and old is not None:
                d[old] = m.group(1)
                old = None
    return d

def parse_all(folder):
    d = {}
    base = os.path.join(ROOT, "game/tl", folder)
    for fn in os.listdir(base):
        if fn.endswith(".rpy"):
            d.update(parse_tl(os.path.join(base, fn)))
    return d

ja = parse_all("japanese")
ru = parse_all("russian")

# parse script
script = os.path.join(ROOT, "game/chapters/2/script-ch2_1.rpy")
rows = []
with open(script, encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        m = re.match(r'\s*(s|si|l|th|c|k|ha|m)\s+"(.*)"\s*$', line.rstrip("\n"))
        if m:
            spk = m.group(1)
            en = m.group(2)
            rows.append((i, spk, en, ja.get(en), ru.get(en)))

with open(os.path.join(ROOT, ".audit_rows.json"), "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)

# print as tab-separated to a file (utf-8), since console may mangle
with open(os.path.join(ROOT, ".audit_rows.txt"), "w", encoding="utf-8") as f:
    for (i, spk, en, j, r) in rows:
        f.write(f"L{i} [{spk}] EN: {en}\n")
        f.write(f"      JA: {j}\n")
        f.write(f"      RU: {r}\n")
print("rows:", len(rows))
print("missing JA:", sum(1 for x in rows if x[3] is None))
print("missing RU:", sum(1 for x in rows if x[4] is None))
