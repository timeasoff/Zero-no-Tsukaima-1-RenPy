# -*- coding: utf-8 -*-
"""S1 analysis: count [voice]/talk per scene in chapter_09 (project ch8), part-split window."""
import re, io, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(ROOT, "ps2_source", "chapters")
name = [f for f in os.listdir(src) if f.startswith("chapter_09_")][0]
path = os.path.join(src, name)

out = io.StringIO()
cur = None
stats = {}
order = []
with open(path, encoding="utf-8") as f:
    for line in f:
        m = re.match(r"---- SCENE (\d+) ----", line)
        if m:
            cur = int(m.group(1))
            stats[cur] = {"voice": 0, "talk": 0, "lines": 0}
            order.append(cur)
            continue
        if cur is None:
            continue
        stats[cur]["lines"] += 1
        if "[voice " in line:
            stats[cur]["voice"] += 1
        if re.match(r"[^ ].*：|null：", line) and "：" in line:
            stats[cur]["talk"] += 1

total_v = sum(v["voice"] for v in stats.values())
total_t = sum(v["talk"] for v in stats.values())
out.write("chapter_09 scene stats\n")
out.write("scene: voices\n")
cum = 0
for sc in order:
    cum += stats[sc]["voice"]
    out.write("%d: v=%d cum=%d\n" % (sc, stats[sc]["voice"], cum))
out.write("TOTAL voices=%d talk-lines=%d\n" % (total_v, total_t))

lines = len(statss) if False else len(stats)
out.write("scenes=%d\n" % lines)
# print choices
with open(path, encoding="utf-8") as f:
    for line in f:
        if line.strip().startswith("【") or line.strip().startswith("→"):
            out.write(line.strip() + "\n")

res = out.getvalue()
with open(os.path.join(ROOT, "reports", "_tmp_ch8_s1_stats.txt"), "w", encoding="utf-8") as f:
    f.write(res)
print("OK", total_v, total_t)
