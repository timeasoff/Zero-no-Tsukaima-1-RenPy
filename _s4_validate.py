# -*- coding: utf-8 -*-
import json, re, os
p = "/workspace/.tmp/opencode/review-ch2-5/reports/sma/ch2/4/humanizer/20261118-h-44f9f5.md"
with open(p, "rb") as f:
    raw = f.read()
text = raw.decode("utf-8", errors="strict")
assert "\ufffd" not in text, "U+FFFD present"
m = re.search(r"```json\n(.*?)\n```", text, re.S)
assert m, "no json block"
data = json.loads(m.group(1))
print("JSON OK; findings=", len(data["findings"]),
      "checked=", data["checked_units"],
      "preserved=", data["preserved_count"],
      "mismatch=", len(data["mismatch_ja"]))
# verify all findings required keys & disposition values
req = {"line","source_en","ja_anchor","current","problem","reason","suggestion","ja_unchanged","severity","confidence","disposition"}
for i, f in enumerate(data["findings"]):
    assert set(f) == req, (i, set(f) ^ req)
    assert f["disposition"] in {"PRESERVED","PROPOSED","LOW_RISK_FIX"}, f
    assert f["severity"] in {"ERROR","WARNING","CANDIDATE"}, f
    assert f["confidence"] in {"HIGH","MEDIUM","LOW"}, f
    assert f["ja_anchor"].strip(), i
print("SCHEMA OK")
