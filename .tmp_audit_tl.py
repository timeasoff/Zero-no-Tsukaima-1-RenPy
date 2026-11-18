import re, io, glob, os
from collections import defaultdict
base = "/workspace/.tmp/opencode/review-ch2-5/"

script = io.open(base + "game/chapters/2/script-ch2_2.rpy", encoding="utf-8").read()
lines = script.split("\n")

# Extract translatable strings from script (mimic check_project candidates):
#  - "<ident> \"text\"" dialogues/thoughts
#  - bare "text" lines (narrative) and "text": menu items
# We'll collect the literal content.
strs = []
patterns = [
    re.compile(r'^\s*[a-zA-Z_][\w]*\s+"(.*)"\s*$'),   # speaker "..."
]
for ln in lines:
    s = ln.strip()
    if s.startswith('#'):
        continue
    m = re.match(r'^\s*([a-zA-Z_][\w]*)\s+"(.*)"\s*$', ln)
    if m and m.group(1) not in ('update_sympathy', 'voice'):
        strs.append(m.group(2))
    else:
        # bare string narrative: "...."
        m2 = re.match(r'^\s*"(.*)"\s*:?\s*$', ln)
        if m2:
            strs.append(m2.group(1))

def unescape(x):
    return x.replace('\\"','"')

strs = [unescape(x) for x in strs]

# Load TL old->list of (file,line) for each language
def load_tl(lang):
    idx = defaultdict(list)
    for f in glob.glob(base + f"game/tl/{lang}/*.rpy"):
        if f.endswith('common.rpy'):
            continue
        for i, ln in enumerate(io.open(f, encoding='utf-8').read().split("\n"), 1):
            m = re.match(r'\s*old\s+"(.*)"\s*$', ln)
            if m:
                idx[unescape(m.group(1))].append((os.path.relpath(f, base), i))
    return idx

ja = load_tl('japanese')
ru = load_tl('russian')

out = io.open(base + ".tmp_audit_tl_report.txt", "w", encoding="utf-8")
out.write(f"Total translatable strings extracted from script-ch2_2.rpy: {len(strs)}\n\n")
out.write("=== Strings missing old in JA or RU, or with duplicate old ===\n")
problems = 0
for s in strs:
    ja_locs = ja.get(s, [])
    ru_locs = ru.get(s, [])
    issues = []
    if not ja_locs: issues.append('NO_JA_OLD')
    if not ru_locs: issues.append('NO_RU_OLD')
    if len(ja_locs) > 1: issues.append(f'DUP_JA={ja_locs}')
    if len(ru_locs) > 1: issues.append(f'DUP_RU={ru_locs}')
    if issues:
        problems += 1
        out.write(f"[{', '.join(issues)}] \"{s}\"  JA={ja_locs} RU={ru_locs}\n")
out.write(f"\nTotal strings with problems: {problems}\n")
out.close()
print("done; strings=%d problems=%d" % (len(strs), problems))
