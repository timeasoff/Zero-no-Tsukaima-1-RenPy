import json, re, unicodedata
from pathlib import Path

p = Path("/workspace/.tmp/opencode/review-ch2-5/reports/sma/ch4/1/grammar/20261118-g-1b52d8.md")
t = p.read_text(encoding="utf-8")
assert "\ufffd" not in t, "U+FFFD found"
# detect CJK / non-target stray scripts
stray = sorted({c for c in t if unicodedata.name(c, "").startswith(("CJK", "HIRAGANA", "KATAKANA")) })
print("stray CJK/kana chars:", stray)
print("replacement char:", "\ufffd" in t)
blocks = re.findall(r"```json\n(.*?)\n```", t, re.S)
print("json blocks:", len(blocks))
data = json.loads(blocks[0])
print("keys:", sorted(data.keys()))
print("findings:", len(data["findings"]))
print("dispositions:", [f["disposition"] for f in data["findings"]])
print("lines:", [f["line"] for f in data["findings"]])
print("precheck:", data["precheck"], "checked_units:", data["checked_units"])
for f in data["findings"]:
    assert f["current"] and f["ja_anchor"] and f["reason"] and f["suggestion"]
    assert f["issue_type"] in {"GRAMMAR","SYNTAX","REGISTER","TYPOGRAPHY","TAG"}
    assert f["severity"] in {"ERROR","WARNING","CANDIDATE"}
    assert f["confidence"] in {"HIGH","MEDIUM","LOW"}
    assert f["disposition"] in {"PROPOSED","PRESERVED","LOW_RISK_FIX"}
print("VALIDATION OK")
