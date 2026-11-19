import io, json, re
base = "/workspace/.tmp/opencode/review-ch2-5/"
p = base + "reports/sma/ch2/2/structure/20261118-t-24e8ae.md"
t = io.open(p, encoding="utf-8").read()
m = re.search(r"```json\n(.*?)\n```", t, re.S)
data = json.loads(m.group(1))
print("JSON OK; keys:", sorted(data.keys()))
print("findings:", len(data["findings"]), "preserved_count:", data["preserved_count"],
      "checked_units:", data["checked_units"])
print("finding categories:", [f["category"] for f in data["findings"]])
# check no U+FFFD / mojibake
bad = [c for c in t if c == "\ufffd"]
print("U+FFFD count:", len(bad))
