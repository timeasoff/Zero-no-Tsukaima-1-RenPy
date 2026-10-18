# -*- coding: utf-8 -*-
"""Build ch4_5 translation reference: EN (from script) vs JA (canon, raw join).

Output: tools/ch4_5_tl_ref.txt (UTF-8)
  [D001] s
    EN: ...
    JA: ...
  ...
Also asserts speaker/order alignment between script and source.
"""
import re, glob, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

JA2KEY = {'サイト': 's', 'ルイズ': 'l', 'アンリエッタ': 'h',
          'ハルナ': 'ha', 'シエスタ': 'si', 'デルフリンガー': 'd', 'null': 'n'}

# ---------- source ----------
f = glob.glob('ps2_source/chapters/chapter_05_*.txt')[0]
L = open(f, encoding='utf-8', errors='replace').read().splitlines()
s256 = next(i for i, l in enumerate(L) if re.match(r'^-+\s*SCENE\s*0256', l.strip()))
s261 = next(i for i, l in enumerate(L) if re.match(r'^-+\s*SCENE\s*0261', l.strip()))

talk_re = re.compile(r'^([^\s：:（【\[]+)：(.*)$')

def raw_join(first, cont_lines):
    return first + ''.join(cont_lines)

src_dialogs = []   # (key, ja)
src_thoughts = []  # ja (with （）)
src_choices = []   # ja

i = s256
while i < s261:
    ln = L[i]
    m = talk_re.match(ln)
    if m and not ln.strip().startswith('['):
        spk = m.group(1)
        j = i + 1
        cont = []
        while j < s261:
            nxt = L[j]
            ns = nxt.strip()
            if (talk_re.match(nxt) or ns.startswith('[') or '【' in nxt
                    or ns.startswith('→') or re.match(r'^-+\s*SCENE', ns)):
                break
            if nxt.strip():
                cont.append(nxt)
            j += 1
        block = [ln] + cont
        if any('[voice' in b for b in block):
            ja = raw_join(m.group(2), [c for c in cont])
            ja = re.sub(r'\s*\[voice \d+\]', '', ja)
            src_dialogs.append((JA2KEY.get(spk, '?'), ja))
        elif spk == 'null':
            src_thoughts.append(raw_join(m.group(2), cont))  # placeholder position marker
        else:
            # thought （…）
            txt = raw_join(m.group(2), cont)
            src_thoughts.append(txt)
        i = j
        continue
    if '【選択肢】' in ln:
        t = ln.strip()
        t = re.sub(r'^【選択肢】', '', t)
        t = re.sub(r'\s*→\s*scene\s*\d+.*$', '', t)
        src_choices.append(t)
    i += 1

# ---------- script ----------
spath = 'game/chapters/4/script-ch4_5.rpy'
SL = open(spath, encoding='utf-8').read().splitlines()
DIALOG = re.compile(r'^(s|l|h|ha|si|d)\s+"(.*)"$')
TH = re.compile(r'^th\s+"(.*)"$')
MENU = re.compile(r'^"(.+)":\s*(#.*)?$')

scr_dialogs, scr_thoughts, scr_choices = [], [], []
for ln in SL:
    st = ln.strip()
    m = DIALOG.match(st)
    if m:
        scr_dialogs.append((m.group(1), m.group(2)))
        continue
    m = TH.match(st)
    if m:
        scr_thoughts.append(m.group(1))
        continue
    m = MENU.match(st)
    if m:
        scr_choices.append(m.group(1))

print('dialogs: source=%d script=%d' % (len(src_dialogs), len(scr_dialogs)))
print('thoughts: source=%d script=%d' % (len(src_thoughts), len(scr_thoughts)))
print('choices: source=%d script=%d' % (len(src_choices), len(scr_choices)))

assert len(src_dialogs) == len(scr_dialogs), 'dialog count'
bad = [(i + 1, a[0], b[0]) for i, (a, b) in enumerate(zip(src_dialogs, scr_dialogs)) if a[0] != b[0]]
assert not bad, 'speaker order mismatch: %s' % bad[:5]
assert len(src_thoughts) == len(scr_thoughts), 'thought count'
assert len(src_choices) == len(scr_choices), 'choice count'
print('ORDER/SPEAKER ALIGNMENT: OK')

with open('tools/ch4_5_tl_ref.txt', 'w', encoding='utf-8') as out:
    for n, ((key, ja), (skey, en)) in enumerate(zip(src_dialogs, scr_dialogs), 1):
        out.write('[D%03d] %s\n  EN: %s\n  JA: %s\n' % (n, key, en, ja))
    for n, (ja, en) in enumerate(zip(src_thoughts, scr_thoughts), 1):
        out.write('[T%03d]\n  EN: %s\n  JA: %s\n' % (n, en, ja))
    for n, (ja, en) in enumerate(zip(src_choices, scr_choices), 1):
        out.write('[C%03d]\n  EN: %s\n  JA: %s\n' % (n, en, ja))

print('wrote tools/ch4_5_tl_ref.txt')
