#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re
from pathlib import Path
pairs = json.loads(Path("/workspace/.tmp/opencode/review-ch2-5/_g_scope_ch2_4.json").read_text(encoding="utf-8"))
TAG = re.compile(r'\{#[^}]*\}')
tagged_en = [p for p in pairs if TAG.search(p["en"])]
tagged_ru_ok = [p for p in tagged_en if TAG.findall(p["en"]) == TAG.findall(p["ru"])]
print("pairs with {#...} in EN:", len(tagged_en))
print("of those, preserve tag in RU new:", len(tagged_ru_ok))
print("drop tag in RU new:", len(tagged_en) - len(tagged_ru_ok))
