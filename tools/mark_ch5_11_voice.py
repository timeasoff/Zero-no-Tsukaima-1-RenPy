# -*- coding: utf-8 -*-
"""Register S11 voice names and mark their exact source rows as used."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "game/chapters/5/script-ch5_11.rpy"
MANIFEST = ROOT / "references/voice_id_map.csv"
TRANS = ROOT / "transcriptions_ja_ru.csv"

script = SCRIPT.read_text(encoding="utf-8")
pairs = []
for name, ident in re.findall(r'voice "([^"]+)"\n\s*[^\n]*\{#ch5_11_v(\d+)\}', script):
    pair = (name, int(ident))
    if pair not in pairs:
        pairs.append(pair)
if len(pairs) != 177:
    raise SystemExit(f"expected 177 unique S11 pairs, got {len(pairs)}")

existing = set()
for line in MANIFEST.read_text(encoding="utf-8").splitlines():
    if line.startswith("#") or not line.strip():
        continue
    name = line.split(",", 1)[0]
    existing.add(name)
dupes = [name for name, _ in pairs if name in existing]
if dupes:
    raise SystemExit("manifest entries already exist: " + ", ".join(dupes))

with MANIFEST.open("a", encoding="utf-8", newline="") as fh:
    for name, ident in pairs:
        fh.write(f"{name},{ident},,S11 USED\n")

lines = TRANS.read_text(encoding="utf-8-sig").splitlines()
ids = {ident for _, ident in pairs}
marked = set()
out = []
for line in lines:
    m = re.match(r"(VOICE_ID\.BIN_[0-9A-Fa-f]{8})\.wav,(.*)$", line)
    if m:
        ident = int(m.group(1).split("_")[-1], 16)
        if ident in ids and not line.startswith("#"):
            line = "# USED ch5.11 " + line
            marked.add(ident)
    out.append(line)
if marked != ids:
    raise SystemExit(f"transcription ids not marked: {sorted(ids - marked)}")
TRANS.write_text("\ufeff" + "\n".join(out) + "\n", encoding="utf-8")
print(f"manifest={len(pairs)} marked={len(marked)}")
