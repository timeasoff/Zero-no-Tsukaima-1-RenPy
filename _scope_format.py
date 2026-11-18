#!/usr/bin/env python3
import json
from pathlib import Path
root = Path(__file__).parent
d = json.loads((root / "_scope_result.json").read_text(encoding="utf-8"))
lines = []
for n, r in enumerate(d["ru"], 1):
    ja = " | ".join(r["ja"]) if r["ja"] else "(NO JA TL MATCH)"
    lines.append(f"[{n}] {r['file']}:{r['new_line']} (EN line {r['old_line']})")
    lines.append(f"  EN : {r['old']}")
    lines.append(f"  JA : {ja}")
    lines.append(f"  RU : {r['new']}")
    lines.append("")
(root / "_scope_readable.txt").write_text("\n".join(lines), encoding="utf-8")
print("wrote", len(d["ru"]), "entries")
