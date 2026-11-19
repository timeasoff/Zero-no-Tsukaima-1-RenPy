import re, io, os
base = "/workspace/.tmp/opencode/review-ch2-5/"
script = io.open(base + "game/chapters/2/script-ch2_2.rpy", encoding="utf-8").read()
voices = re.findall(r'voice "([^"]+)"', script)

# voice_id_map.csv
import csv
rows = {}
mpath = base + "references/voice_id_map.csv"
with io.open(mpath, encoding="utf-8") as f:
    r = csv.reader(f)
    header = next(r)
    for row in r:
        if not row: continue
        rows[row[0].strip()] = row

missing = [v for v in voices if v not in rows]
print("voice_id_map header:", header)
print("script voices:", len(voices), "missing in map:", len(missing))
for v in missing[:30]:
    print("  MISSING:", v)

# sample mapped rows
for v in voices[:3]:
    print("  sample", v, "->", rows.get(v))
