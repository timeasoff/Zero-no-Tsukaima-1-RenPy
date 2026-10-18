# -*- coding: utf-8 -*-
"""One-shot: fix manifest row format in gen_ch4_5_voices.py (byte-safe)."""
p = 'tools/gen_ch4_5_voices.py'
b = open(p, 'rb').read()

old = b'        manifest_lines.append(f"{script_name},{canon_id},{script_spk}")'
new = b'        manifest_lines.append(f"{script_name},{canon_id}")'
assert b.count(old) == 1, ('old', b.count(old))
b = b.replace(old, new)

old2 = '# Формат: voice_name,voice_id,speaker_code'.encode('utf-8')
new2 = '# Формат колонок манифеста: voice_name,voice_id (wav_file/notes не заполняются)'.encode('utf-8')
assert b.count(old2) == 1, ('old2', b.count(old2))
b = b.replace(old2, new2)

open(p, 'wb').write(b)
print('patched ok')
