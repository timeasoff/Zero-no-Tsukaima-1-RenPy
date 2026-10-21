# -*- coding: utf-8 -*-
"""Временный конвертер голосов wav -> ogg через soundfile (ffmpeg в этой
среде недоступен). Использует логику tools/media/audio_converter.py:
имя wav по voice_id из wav_files/, результат — game/audio/voices/<voice_name>.ogg.

Запуск:  python tools/_tmp_convert_voices.py ch4.6
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import soundfile as sf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WAV_DIR = os.path.join(ROOT, 'wav_files')
OUT_DIR = os.path.join(ROOT, 'game', 'audio', 'voices')
MANIFEST = os.path.join(ROOT, 'references', 'voice_id_map.csv')
WAV_ID_RE = re.compile(r'_([0-9A-Fa-f]{8})\.wav$')

prefix = sys.argv[1] if len(sys.argv) > 1 else 'ch4.6'

index = {}
for name in sorted(os.listdir(WAV_DIR)):
    m = WAV_ID_RE.search(name)
    if m:
        index.setdefault(int(m.group(1), 16), name)

rows = []
for ln in io.open(MANIFEST, encoding='utf-8'):
    p = ln.rstrip('\n').split(',')
    if len(p) < 2 or not p[0].startswith(prefix):
        continue
    rows.append((p[0], int(p[1])))

print('строк манифеста:', len(rows))
done = skipped = 0
for name, vid in rows:
    out = os.path.join(OUT_DIR, name + '.ogg')
    if os.path.exists(out) and os.path.getsize(out) > 0:
        skipped += 1
        continue
    wav = index.get(vid)
    if not wav:
        print('НЕТ WAV для', name, vid)
        continue
    data, sr = sf.read(os.path.join(WAV_DIR, wav), dtype='float32', always_2d=True)
    sf.write(out, data, sr, format='OGG', subtype='VORBIS')
    done += 1
print('сконвертировано:', done, 'уже было:', skipped)
