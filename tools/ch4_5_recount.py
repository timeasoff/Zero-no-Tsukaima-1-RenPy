# -*- coding: utf-8 -*-
"""Recount #2: source per-speaker vs script per-speaker for scenes 256-260."""
import re, io, sys, glob, importlib.util
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

JA2KEY = {
    'サイト': 's', 'ルイズ': 'l', 'アンリエッタ': 'h',
    'ハルナ': 'ha', 'シエスタ': 'si',
}

src = glob.glob('ps2_source/chapters/chapter_05_*.txt')[0]
lines = open(src, encoding='utf-8', errors='replace').read().splitlines()

scene_re = re.compile(r'^-+\s*SCENE\s*(\d+)\s*-+$')
voice_re = re.compile(r'\[voice\s+(\d+)\]')
spk_re = re.compile(r'^([^\s：:（【]+)[：:]')

cur = None
last_spk = None
src_voices = []  # (scene, voice_id, speaker_key, speaker_ja)
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
    vm = voice_re.search(ln)
    if vm:
        src_voices.append((cur, int(vm.group(1)), JA2KEY.get(last_spk, '?'), last_spk))

print('SOURCE total: %d' % len(src_voices))
print('  per key:', dict(Counter(v[2] for v in src_voices)))
unknown = [v for v in src_voices if v[2] == '?']
if unknown:
    print('  UNKNOWN speaker lines:', unknown)
# duplicates of voice id
idc = Counter(v[1] for v in src_voices)
print('  dup voice ids:', [k for k, c in idc.items() if c > 1] or 'none')

# script
script = open('game/chapters/4/script-ch4_5.rpy', encoding='utf-8').read()
sv = re.findall(r'voice "ch4\.5_([a-z]+)_(\d+)"', script)
print('SCRIPT total: %d (unique %d)' % (len(sv), len(set(sv))))
print('  per key:', dict(Counter(sp for sp, n in sv)))
dup = [k for k, c in Counter(sv).items() if c > 1]
print('  dups:', dup or 'none')

# canon
spec = importlib.util.spec_from_file_location('gen', 'tools/gen_ch4_5_voices.py')
gen = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(gen)
except SystemExit:
    pass
canon = getattr(gen, 'CANON_VOICES', [])
print('CANON total: %d' % len(canon))
if canon and isinstance(canon[0], tuple) and len(canon[0]) == 3:
    # (voice_id, speaker_key, ja_text)
    print('  per key:', dict(Counter(t[1] for t in canon)))
    canon_ids = [t[0] for t in canon]
    print('  ids equal to source order:', canon_ids == [v[1] for v in src_voices])

# per-speaker delta source vs script
sc = Counter(v[2] for v in src_voices)
pc = Counter(sp for sp, n in sv)
print('DELTA (source - script):')
for k in sorted(set(sc) | set(pc)):
    print('  %-3s source=%d script=%d diff=%+d' % (k, sc.get(k, 0), pc.get(k, 0), sc.get(k, 0) - pc.get(k, 0)))

# source voice id -> speaker, aligned with canon, to locate missing ones
print('SOURCE per-scene:', dict(Counter(v[0] for v in src_voices)))
