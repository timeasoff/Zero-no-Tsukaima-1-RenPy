import re, sys

paths = [
    'game/tl/russian/sp90_dialogs.rpy',
    'game/tl/russian/sp90_choises.rpy',
]
pairs = []
for p in paths:
    lines = open(p, encoding='utf-8').read().split('\n')
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith('old "'):
            old = lines[i].strip()[5:-1]
            new = lines[i+1].strip()[5:-1]
            pairs.append((p, i+1, old, new))
            i += 2
        else:
            i += 1

print('TOTAL PAIRS', len(pairs))

# 1. Latin letters inside new
print('\n=== LATIN IN NEW ===')
for p, ln, old, new in pairs:
    lat = re.findall(r'[A-Za-z]', new)
    if lat:
        print(p, ln, repr(new), '->', set(lat))

# 2. glued punctuation: punctuation followed immediately by a capital Cyrillic letter
print('\n=== GLUED PUNCT (?!… followed by letter) ===')
for p, ln, old, new in pairs:
    for m in re.finditer(r'([!?….;:,])\s*([А-ЯЁ])', new):
        # report only when no space (or only …) between
        seg = m.group(0)
        if re.match(r'^[!?….;:,][А-ЯЁ]', seg) or re.match(r'^[!?;:,]\.\.\.[А-ЯЁ]', seg) or re.match(r'^[!?;:,]…[А-ЯЁ]', seg):
            print(p, ln, repr(new), '|', repr(seg))

# 3. Japanese full stop in new
print('\n=== JA PUNCT ===')
for p, ln, old, new in pairs:
    if '。' in new or '、' in new:
        print(p, ln, repr(new))

# 4. two dots
print('\n=== TWO DOTS ===')
for p, ln, old, new in pairs:
    if re.search(r'[а-яёА-ЯЁ!?]\.\.[^.]', new) or re.search(r'\.\.$', new):
        print(p, ln, repr(new))

# 5. EN thought markers -> RU italic check
en_path = 'game/chapters/extra/sp90.rpy'
en_lines = open(en_path, encoding='utf-8').read().split('\n')
en_map = {}
for l in en_lines:
    m = re.match(r'\s*[a-z]+ "(.*)\{#(sp90_[a-z0-9_]+)\}"', l)
    if m:
        en_map[m.group(2)] = m.group(1)
print('\n=== THOUGHTS (EN parens) vs RU italics ===')
for p, ln, old, new in pairs:
    m = re.search(r'\{#(sp90_[a-z0-9_]+)\}', old)
    if not m: continue
    eid = m.group(1)
    e = en_map.get(eid, '')
    if e.startswith('(') or '(' in e:
        ital = '_' in new
        print(('ITAL ' if ital else 'NOITAL'), p, ln, eid, '|EN:', e[:90], '|RU:', new[:90])
