#!/usr/bin/env python3
import json
from pathlib import Path
root = Path(__file__).parent
res = json.loads((root / "_scope_result.json").read_text(encoding="utf-8"))
# indexes (1-based in readable) of interest
want = {7, 9, 46, 59, 74, 106, 110, 113}
for i, r in enumerate(res["ru"], 1):
    if i in want:
        print(f"IDX {i} ENline={r['old_line']} RUline={r['new_line']}")
        print("  old:", r["old"])
        print("  new:", r["new"])
        print("  ja :", " | ".join(r["ja"]))
