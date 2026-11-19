import re, os, json
ROOT = "/workspace/.tmp/opencode/review-ch2-5"

def parse_tl(path):
    d = {}
    old = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r'\s*old\s+"(.*)"\s*$', line.rstrip("\n"))
            if m:
                old = m.group(1); continue
            m = re.match(r'\s*new\s+"(.*)"\s*$', line.rstrip("\n"))
            if m and old is not None:
                d[old] = m.group(1); old = None
    return d

def parse_all(folder):
    d = {}
    base = os.path.join(ROOT, "game/tl", folder)
    for fn in os.listdir(base):
        if fn.endswith(".rpy"):
            d.update(parse_tl(os.path.join(base, fn)))
    return d

ja = parse_all("japanese"); ru = parse_all("russian")
choices = [
  "Couldn't sleep because of an all-nighter or something",
  "Couldn't sleep because that female guest was on her mind",
  "Couldn't sleep because she was keeping watch on me",
  "Shall we go catch him too?",
  "I'd like to eat breakfast",
]
with open(os.path.join(ROOT, ".audit_choices.txt"), "w", encoding="utf-8") as f:
    for c in choices:
        f.write(f"EN: {c}\n JA: {ja.get(c)}\n RU: {ru.get(c)}\n")
print("done")
