#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extractor for grammar/prose audit of part 2_4 (scoped exactly like check_typography)."""
import re, json
from pathlib import Path

ROOT = Path("/workspace/.tmp/opencode/review-ch2-5")

CODE_SPEAKERS = {
    "voice", "scene", "show", "hide", "jump", "call", "with", "define",
    "image", "transform", "play", "stop", "queue", "window", "pause",
    "python", "return", "pass", "if", "elif", "else", "while", "for",
    "translate", "camera", "at", "using", "style", "$",
}
RE_TL_LINE = re.compile(r'^\s*(?P<kw>old|new)\s+"(?P<body>.*)"\s*$')
RE_SPEAKER_LINE = re.compile(r'^\s*(?P<sp>[A-Za-z_][\w.]*)\s+"(?P<body>.*)"\s*$')
RE_BARE_LINE = re.compile(r'^\s*"(?P<body>.*)"\s*$')

def extract(line):
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None
    m = RE_TL_LINE.match(line)
    if m:
        return m.group("kw"), m.group("body")
    m = RE_SPEAKER_LINE.match(line)
    if m:
        sp = m.group("sp")
        if sp in CODE_SPEAKERS:
            return None
        return None, m.group("body")
    m = RE_BARE_LINE.match(line)
    if m:
        return None, m.group("body")
    return None

en_file = ROOT / "game/chapters/2/script-ch2_4.rpy"
en_lines = en_file.read_text(encoding="utf-8").split("\n")
en_set = set()
en_first_line = {}
for i, line in enumerate(en_lines, 1):
    p = extract(line)
    if p and p[0] is None and p[1]:
        en_set.add(p[1])
        if p[1] not in en_first_line:
            en_first_line[p[1]] = i

pairs = []
for f in sorted((ROOT / "game/tl/russian").rglob("*.rpy")):
    if f.name == "common.rpy":
        continue
    pending_old = None
    old_line = 0
    for i, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
        p = extract(line)
        if not p or p[0] is None:
            continue
        kw, body = p
        if kw == "old":
            pending_old, old_line = body, i
            continue
        if pending_old is not None and pending_old in en_set:
            pairs.append({
                "file": str(f.relative_to(ROOT)),
                "ru_line": i,
                "old_line": old_line,
                "script_line": en_first_line.get(pending_old),
                "en": pending_old,
                "ru": body,
            })
        pending_old = None

pairs.sort(key=lambda p: (p["script_line"] or 99999, p["file"], p["ru_line"]))
(ROOT / "_g_scope_ch2_4.json").write_text(json.dumps(pairs, ensure_ascii=False, indent=1), encoding="utf-8")
out = []
for p in pairs:
    out.append("### script L%s | %s:%d" % (p["script_line"], p["file"], p["ru_line"]))
    out.append("EN: " + p["en"])
    out.append("RU: " + p["ru"])
    out.append("")
(ROOT / "_g_pairs_ch2_4.txt").write_text("\n".join(out), encoding="utf-8")
print("PAIRS:", len(pairs))
