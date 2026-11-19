#!/usr/bin/env python3
# Extract EN dialogue strings of part 5_5 and matching old/new pairs in RU/JA tl.
import re, json
from pathlib import Path

root = Path(__file__).parent
RE_TL_LINE = re.compile(r'^\s*(?P<kw>old|new)\s+"(?P<body>.*)"\s*$')
RE_SPEAKER_LINE = re.compile(r'^\s*(?P<sp>[A-Za-z_][\w.]*)\s+"(?P<body>.*)"\s*$')
RE_BARE_LINE = re.compile(r'^\s*"(?P<body>.*)"\s*$')
CODE_SPEAKERS = {
    "voice","scene","show","hide","jump","call","with","define","image",
    "transform","play","stop","queue","window","pause","python","return",
    "pass","if","elif","else","while","for","translate","camera","at",
    "using","style","$",
}

def extract(line):
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None
    m = RE_TL_LINE.match(line)
    if m:
        return m.group("kw"), m.group("body")
    m = RE_SPEAKER_LINE.match(line)
    if m:
        if m.group("sp") in CODE_SPEAKERS:
            return None
        return None, m.group("body")
    m = RE_BARE_LINE.match(line)
    if m:
        return None, m.group("body")
    return None

# 1. EN strings in script-ch5_5.rpy with line numbers
en_file = root / "game/chapters/5/script-ch5_5.rpy"
en_lines = []
en_set = set()
for i, line in enumerate(en_file.read_text(encoding="utf-8").split("\n"), 1):
    p = extract(line)
    if p and p[0] is None and p[1]:
        en_lines.append((i, p[1]))
        en_set.add(p[1])

# 2. tl pairs
def pairs_for(langdir):
    d = root / "game/tl" / langdir
    out = []
    pending = None
    for f in sorted(d.rglob("*.rpy")):
        if f.name == "common.rpy":
            continue
        pending = None
        for i, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            p = extract(line)
            if not p or p[0] is None:
                continue
            kw, body = p
            if kw == "old":
                pending = (body, i, f.name)
                continue
            # new
            if pending and pending[0] in en_set:
                out.append({"old": pending[0], "old_line": pending[1],
                            "file": pending[2], "new_line": i, "new": body})
            pending = None
    return out

ru = pairs_for("russian")
ja = pairs_for("japanese")

ja_by_old = {}
for j in ja:
    ja_by_old.setdefault(j["old"], []).append(j["new"])

for r in ru:
    r["ja"] = ja_by_old.get(r["old"], [])

result = {"en_count": len(en_lines), "en_lines": en_lines,
          "ru_count": len(ru), "ru": ru}
out = root / "_scope_result.json"
out.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
print("EN lines:", len(en_lines), "RU pairs in scope:", len(ru))
