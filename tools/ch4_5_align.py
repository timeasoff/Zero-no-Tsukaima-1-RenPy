# -*- coding: utf-8 -*-
"""Write alignment dump: source utterances vs script voice lines (file output, UTF-8)."""
import re, glob

src = glob.glob('ps2_source/chapters/chapter_05_*.txt')[0]
lines = open(src, encoding='utf-8', errors='replace').read().splitlines()

scene_re = re.compile(r'^-+\s*SCENE\s*(\d+)\s*-+$')
voice_re = re.compile(r'\[voice\s+(\d+)\]')
spk_re = re.compile(r'^([^\s：:（【]+)[：:]')

JA2KEY = {'サイト': 's', 'ルイズ': 'l', 'アンリエッタ': 'h',
          'ハルナ': 'ha', 'シエスタ': 'si', 'デルフリンガー': 'd'}

cur = None
last_spk = None
pending = []  # utterance buffer: speaker + text lines until voice marker found
out = []
utter_id = 0
for ln in lines:
    m = scene_re.match(ln.strip())
    if m:
        cur = int(m.group(1))
        last_spk = None
        continue
    if cur is None or not (256 <= cur <= 260):
        continue
    sm = spk_re.match(ln)
    if sm and not ln.strip().startswith('['):
        last_spk = sm.group(1)
        pending = [(last_spk, ln.split('：', 1)[-1].split(':', 1)[-1])]
    elif pending and not ln.strip().startswith('['):
        pending.append((last_spk, ln))
    vm = voice_re.search(ln)
    if vm:
        vid = int(vm.group(1))
        key = JA2KEY.get(last_spk, '?')
        text = ' '.join(t for _, t in pending)
        text = re.sub(r'\s*\[voice \d+\]', '', text)
        utter_id += 1
        out.append((utter_id, cur, key, vid, text))
        pending = []

# script side
spath = 'game/chapters/4/script-ch4_5.rpy'
slines = open(spath, encoding='utf-8').read().splitlines()
SPEAKERS = {'s', 'l', 'h', 'ha', 'si', 'd'}
sout = []
sid = 0
for idx, ln in enumerate(slines, 1):
    st = ln.strip()
    mm = re.match(r'^([a-z]+)\s+"(.*)"$', st)
    if mm and mm.group(1) in SPEAKERS:
        v = None
        for back in range(1, 4):
            if idx - back - 1 < 0:
                break
            vm = re.search(r'voice "ch4\.5_([a-z]+_\d+)"', slines[idx - back - 1])
            if vm:
                v = vm.group(1)
                break
        sid += 1
        sout.append((sid, idx, mm.group(1), v, mm.group(2)))

with open('tools/ch4_5_align.txt', 'w', encoding='utf-8') as f:
    f.write('=== SOURCE (%d utterances) ===\n' % len(out))
    for u in out:
        f.write('%3d scene=%d %-3s vid=%-6d %s\n' % u)
    f.write('\n=== SCRIPT (%d lines) ===\n' % len(sout))
    for s in sout:
        f.write('%3d line=%-4d %-3s %-12s %s\n' % s)

print('source=%d script=%d -> tools/ch4_5_align.txt' % (len(out), len(sout)))
