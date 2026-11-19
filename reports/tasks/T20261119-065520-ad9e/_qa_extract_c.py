# -*- coding: utf-8 -*-
import re, os, json

ROOT = os.path.dirname(os.path.abspath(__file__))

def parse_pairs(path):
    """Return dict old -> new for `translate ... strings:` blocks."""
    res = {}
    if not os.path.exists(path):
        return res
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()
    old = None
    for ln in lines:
        m = re.match(r'\s*old\s+"(.*)"\s*$', ln.rstrip('\n'))
        if m:
            old = m.group(1)
            continue
        m = re.match(r'\s*new\s+"(.*)"\s*$', ln.rstrip('\n'))
        if m and old is not None:
            res.setdefault(old, []).append(m.group(1))
            old = None
    return res

ru = {}
ja = {}
for lang, store in [('russian', ru), ('japanese', ja)]:
    d = os.path.join(ROOT, 'game', 'tl', lang)
    for fn in ['dialogs.rpy', 'thoughs.rpy', 'choises.rpy', 'characters.rpy', 'overlays.rpy']:
        p = os.path.join(d, fn)
        for k, v in parse_pairs(p).items():
            store.setdefault(k, []).append((fn, v))

# Extract EN strings from ch2_5.rpy in order with line numbers
script = os.path.join(ROOT, 'game', 'chapters', '2', 'script-ch2_5.rpy')
with open(script, encoding='utf-8') as f:
    slines = f.readlines()

out = []
for i, ln in enumerate(slines, 1):
    s = ln.strip()
    # match  s "..." / si "..." / th "..." / l "..." / ha "..." / k "..." / t "..." / menu choice "..."
    m = re.match(r'^([a-z]+)\s+"(.*)"\s*$', s)
    if not m:
        continue
    speaker, text = m.group(1), m.group(2)
    if speaker == 'voice':
        continue
    # strip trailing {#...} marker
    text_clean = re.sub(r'\{\#ch2\.5_[^\}]*\}', '', text)
    ru_entries = ru.get(text, []) or ru.get(text_clean, [])
    ja_entries = ja.get(text, []) or ja.get(text_clean, [])
    out.append({
        'script_line': i,
        'speaker': speaker,
        'en': text,
        'ru': ru_entries,
        'ja': ja_entries,
    })

with open(os.path.join(ROOT, '_qa_c_pairs.json'), 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

print('utterances:', len(out))
print('missing RU:', sum(1 for o in out if not o['ru']))
print('missing JA:', sum(1 for o in out if not o['ja']))
