import re, io
base = "/workspace/.tmp/opencode/review-ch2-5/"
scope = io.open(base + ".tmp_audit_scope.txt", encoding="utf-8").read()
chap_part = scope.split("########## EVENTS_FULL")[0]

# count [voice N] in chapters part
voices = re.findall(r'\[voice (\d+)\]', chap_part)
print("JA [voice N] tags in scenes 76-89:", len(voices))

# count dialogue units: lines starting with a speaker + fullwidth colon, OR thought continuations
# Simpler: count lines ending with [voice N] plus lines that are thoughts (（…）) with null voice
# In chapters part, each DIALOGUE = a physical line with '：' at start OR a '（' thought.
units = []
for ln in chap_part.split("\n"):
    s = ln.strip()
    if not s: continue
    if re.match(r'^[^\s].*：', s) or s.startswith('（') or s.startswith('　'):
        # continuation lines without speaker but starting with ideographic space are part of previous
        if s.startswith('　'):
            continue
        units.append(s)
    elif '[voice' in s and not s.startswith('　'):
        # continuation line carrying [voice N] - belongs to prev, skip
        pass
print("approx JA top-level dialogue/thought starts:", len(units))

# events_full DIALOGUE count
ev_part = scope.split("########## EVENTS_FULL")[1]
d = len(re.findall(r'^DIALOGUE\s+talk\(', ev_part, re.M))
print("events_full DIALOGUE count:", d)

# script dialogue lines (dialog or th)
script = io.open(base + "game/chapters/2/script-ch2_2.rpy", encoding="utf-8").read()
sd = len(re.findall(r'^\s+(?:s|l|c|ha|si|d|th)\s+"', script, re.M))
print("script dialogue/thought lines:", sd)
menu_items = len(re.findall(r'^\s{8,}"[^"]+":', script, re.M))
print("script menu items:", menu_items)
