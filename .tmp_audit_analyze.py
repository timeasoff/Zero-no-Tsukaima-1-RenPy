import re, io, glob, os
base = "/workspace/.tmp/opencode/review-ch2-5/"

script = io.open(base + "game/chapters/2/script-ch2_2.rpy", encoding="utf-8").read()
slines = script.split("\n")

out = io.open(base + ".tmp_audit_report.txt", "w", encoding="utf-8")

# 1. voice numbering per speaker
out.write("=== VOICE IDS by prefix (script-ch2_2) ===\n")
voices = re.findall(r'voice "([^"]+)"', script)
from collections import defaultdict
d = defaultdict(list)
for v in voices:
    m = re.match(r'ch2\.2_([a-z]+)_(\d+)', v)
    if m:
        d[m.group(1)].append(int(m.group(2)))
    else:
        d['??'].append(v)
for k in sorted(d):
    nums = sorted(d[k])
    gaps = [n for n in range(1, max(nums)+1) if n not in nums] if nums and isinstance(nums[0], int) else []
    out.write(f"{k}: count={len(nums)} min={min(nums)} max={max(nums)} gaps={gaps} raw={nums}\n")
out.write(f"total voice lines: {len(voices)}\n")

# 2. odd markers
out.write("\n=== ODD MARKERS in script-ch2_2 ===\n")
for i, ln in enumerate(slines, 1):
    if re.search(r'#dots|#un|#haru|#h\d|\{#', ln):
        out.write(f"{i}: {ln.strip()}\n")

# 3. odd markers elsewhere in project (chapters only)
out.write("\n=== ODD MARKERS across all chapters (count by token) ===\n")
tok = defaultdict(int)
examples = {}
for f in glob.glob(base + "game/chapters/**/*.rpy", recursive=True):
    for ln in io.open(f, encoding="utf-8").read().split("\n"):
        for m in re.findall(r'\{#[^}]+\}|#[a-z]+\d*', ln):
            tok[m] += 1
            examples.setdefault(m, (os.path.relpath(f, base), ln.strip()))
for k in sorted(tok):
    out.write(f"{k}: {tok[k]}  e.g. {examples[k][0]}: {examples[k][1][:70]}\n")

out.close()
print("done")
