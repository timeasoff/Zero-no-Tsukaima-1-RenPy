import re
paths = ['game/tl/russian/sp90_dialogs.rpy', 'game/tl/russian/sp90_choises.rpy']
pairs = []
for p in paths:
    lines = open(p, encoding='utf-8').read().split('\n')
    for i, l in enumerate(lines):
        if l.strip().startswith('new "'):
            new = l.strip()[5:-1]
            old = lines[i-1].strip()[5:-1]
            pairs.append((p, i+1, old, new))

print('=== SENTENCE PUNCT GLUED TO NEXT WORD ===')
for p, ln, old, new in pairs:
    # a full stop / ! / ? immediately followed by ellipsis then a capital, or directly a capital
    for m in re.finditer(r'[.!?](?:…+|\.\.)?[А-ЯЁ]', new):
        print(p, ln, repr(new), '|', repr(m.group(0)))
    if '…………' in new:
        print(p, ln, 'EIGHT DOTS', repr(new))

print('\n=== JA / LATIN ARTIFACTS SUMMARY ===')
for p, ln, old, new in pairs:
    if re.search(r'[a-zA-Z]', new) or '。' in new or re.search(r'\.\.[^.]', new):
        print(p, ln, repr(new))
