import re, io, csv
base = "/workspace/.tmp/opencode/review-ch2-5/"
# source voice ids across scenes 76-89 (chapters part)
scope = io.open(base + ".tmp_audit_scope.txt", encoding="utf-8").read()
chap_part = scope.split("########## EVENTS_FULL")[0]
src_ids = [int(x) for x in re.findall(r'\[voice (\d+)\]', chap_part)]

# script voice -> id via map
with io.open(base + "references/voice_id_map.csv", encoding="utf-8") as f:
    r = csv.reader(f); next(r)
    vmap = {row[0].strip(): int(row[1]) for row in r if len(row) >= 2 and row[1].strip().isdigit()}
script = io.open(base + "game/chapters/2/script-ch2_2.rpy", encoding="utf-8").read()
sv = re.findall(r'voice "([^"]+)"', script)
script_ids = [vmap[v] for v in sv]

print("src count:", len(src_ids), "script count:", len(script_ids))
mism = [(i+1, a, b) for i,(a,b) in enumerate(zip(src_ids, script_ids)) if a != b]
print("mismatches (position, src_id, script_id):", len(mism))
for m in mism[:40]:
    print("  ", m)
