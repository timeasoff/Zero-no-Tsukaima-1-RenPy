import re
from pathlib import Path

root = Path("/workspace/.tmp/opencode/review-ch2-5")
en_file = root / "game/chapters/4/script-ch4_1.rpy"
en_text = en_file.read_text(encoding="utf-8")
en_strings = set()

pat_dlg = re.compile(r'^\s*(?:c|l|s|ha|o|t|g|k|m|si|th)\s+"(.*)"\s*$')
pat_choice = re.compile(r'^\s*"(.*)"\s*:\s*$')
for line in en_text.split("\n"):
    m = pat_dlg.match(line)
    if m:
        en_strings.add(m.group(1))
    m = pat_choice.match(line)
    if m:
        en_strings.add(m.group(1))

ru_dir = root / "game/tl/russian"
out = []
for f in sorted(ru_dir.glob("*.rpy")):
    if f.name == "common.rpy":
        continue
    content = f.read_text(encoding="utf-8")
    pending_old = None
    pending_line = None
    for i, line in enumerate(content.split("\n"), 1):
        m = re.match(r'^\s*old\s+"(.*)"\s*$', line)
        if m:
            pending_old = m.group(1)
            pending_line = i
            continue
        m = re.match(r'^\s*new\s+"(.*)"\s*$', line)
        if m:
            if pending_old is not None and pending_old in en_strings:
                out.append((f.name, pending_line, i, pending_old, m.group(1)))
            pending_old = None

print("EN strings collected:", len(en_strings))
print("RU new in scope:", len(out))
for fname, ol, nl, old, new in out:
    print(f"\n[{fname} old@{ol} new@{nl}]")
    print("EN:", old)
    print("RU:", new)
