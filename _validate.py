#!/usr/bin/env python3
import json, re
from pathlib import Path
p = Path("reports/sma/ch5/5/grammar/20261118-g-b8cf20.md")
t = p.read_text(encoding="utf-8")
blocks = re.findall(r"```json\s*(.*?)\s*```", t, re.S)
assert len(blocks) == 1, f"json blocks: {len(blocks)}"
d = json.loads(blocks[0])
print("OK json. findings:", len(d["findings"]),
      "checked_units:", d["checked_units"],
      "preserved_count:", d["preserved_count"])
print("severities:", [f["severity"] for f in d["findings"]])
print("U+FFFD present:", "\ufffd" in t)
