#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check scoped pairs for Ren'Py {#...} tag preservation mismatches."""
import re, json
from pathlib import Path
ROOT = Path("/workspace/.tmp/opencode/review-ch2-5")
pairs = json.loads((ROOT / "_g_scope_ch2_4.json").read_text(encoding="utf-8"))
TAG = re.compile(r'\{#[^}]*\}')
for p in pairs:
    en_tags = TAG.findall(p["en"])
    ru_tags = TAG.findall(p["ru"])
    if en_tags != ru_tags:
        print("script L%s | %s:%d" % (p["script_line"], p["file"], p["ru_line"]))
        print("  EN tags:", en_tags, " RU tags:", ru_tags)
        print("  EN:", p["en"])
        print("  RU:", p["ru"])
print("---done---")
