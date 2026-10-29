# -*- coding: utf-8 -*-
"""Mark the voice transcription rows consumed by chapter 5 part 7."""
import csv
import io
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
script = (ROOT / "game/chapters/5/script-ch5_7.rpy").read_text(encoding="utf-8")
manifest = {}
for name in re.findall(r'voice "(ch5\.7_[^"]+)"', script):
    for row in csv.reader((ROOT / "references/voice_id_map.csv").read_text(encoding="utf-8").splitlines()):
        if row and row[0] == name:
            manifest[int(row[1])] = name
            break

path = ROOT / "transcriptions_ja_ru.csv"
raw = path.read_text(encoding="utf-8-sig").splitlines()
out = []
changed = 0
for line in raw:
    match = re.match(r"(VOICE_ID\.BIN_[0-9A-Fa-f]{8})\.wav,(.*)$", line)
    if match:
        voice_id = int(match.group(1).split("_")[-1], 16)
        if voice_id in manifest and not line.startswith("#"):
            line = "# USED ch5.7 " + line
            changed += 1
    out.append(line)
path.write_text("\ufeff" + "\n".join(out) + "\n", encoding="utf-8")
print("marked", changed, "of", len(manifest))
