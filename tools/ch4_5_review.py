# -*- coding: utf-8 -*-
"""Merged EN/JA/RU review sheet for self-review of ch4.5 translations."""
import io, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))
from ch4_5_ru import RU_DIALOGS, RU_THOUGHTS, RU_CHOICES

# reuse gen extraction
import importlib.util
spec = importlib.util.spec_from_file_location('gen', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gen_ch4_5_tl.py'))
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

src_d, src_t, src_c = gen.extract_source()
scr_d, scr_t, scr_c = gen.extract_script()

out = io.StringIO()
for n, ((key, ja), (skey, en), ru) in enumerate(zip(src_d, scr_d, RU_DIALOGS), 1):
    out.write('[D%03d] %s\n  EN: %s\n  JA: %s\n  RU: %s\n' % (n, key, en, ja, ru))
for n, ((ja), (en), ru) in enumerate(zip(src_t, scr_t, RU_THOUGHTS), 1):
    out.write('[T%03d]\n  EN: %s\n  JA: %s\n  RU: %s\n' % (n, en, ja, ru))
for n, ((ja), (en), ru) in enumerate(zip(src_c, scr_c, RU_CHOICES), 1):
    out.write('[C%03d]\n  EN: %s\n  JA: %s\n  RU: %s\n' % (n, en, ja, ru))

with open('tools/ch4_5_review.txt', 'w', encoding='utf-8') as f:
    f.write(out.getvalue())
print('wrote tools/ch4_5_review.txt')
