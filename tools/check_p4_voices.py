# -*- coding: utf-8 -*-
# Сверка voice-ключей script-ch3_4.rpy с манифестом voice_id_map.csv.
import io
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

script = io.open('game/chapters/3/script-ch3_4.rpy', encoding='utf-8').read()
used = re.findall(r'voice "([^"]+)"', script)

manifest = set()
for ln in io.open('references/voice_id_map.csv', encoding='utf-8').read().splitlines():
    if not ln.strip() or ln.startswith('#') or ln.startswith('voice_name'):
        continue
    manifest.add(ln.split(',', 1)[0].strip())

used_set = set(used)
print('voice calls in script:', len(used), 'unique:', len(used_set))
dupes = sorted({k for k in used if used.count(k) > 1})
print('duplicated keys:', dupes if dupes else 'none')

missing = sorted(k for k in used_set if k not in manifest)
print('used but not in manifest:', missing if missing else 'none')

unused = sorted(k for k in manifest if k.startswith('ch3.4_') and k not in used_set)
print('manifest ch3.4_* unused:', unused if unused else 'none')
