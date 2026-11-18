#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
from pathlib import Path
p = Path("/workspace/.tmp/opencode/review-ch2-5/reports/sma/ch2/4/grammar/20261118-g-2c3ae8.md")
t = p.read_text(encoding="utf-8")  # strict UTF-8
assert "\ufffd" not in t, "U+FFFD present"
blocks = re.findall(r"```json\s*(.*?)\s*```", t, re.S)
assert len(blocks) == 1, "expected one json block, got %d" % len(blocks)
d = json.loads(blocks[0])
print("run_id:", d["run_id"], "part:", d["part"])
print("checked_units:", d["checked_units"], "findings:", len(d["findings"]))
from collections import Counter
print("dispositions:", dict(Counter(f["disposition"] for f in d["findings"])))
print("preserved_count field:", d["preserved_count"])
# ensure no stray latin/cyrillic mix artifacts
for f in d["findings"]:
    for k in ("current", "reason", "suggestion"):
        assert "ouch" not in f[k] and " нominative" not in f[k] and "agram" not in f[k]
print("VALID: UTF-8 ok, JSON parses, no artifacts")
