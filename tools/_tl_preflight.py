# -*- coding: utf-8 -*-
"""Pre-flight before gen_ch4_5_tl.py --apply.

1) no double quotes inside RU/EN strings (would break Ren'Py string literals)
2) no EN old from ch4_5 already present in tl files (duplicate old = silent loss)
3) JA new contain no line breaks
"""
import io
import re
import sys

sys.path.insert(0, 'tools')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from ch4_5_ru import RU_DIALOGS, RU_THOUGHTS, RU_CHOICES

SL = open('game/chapters/4/script-ch4_5.rpy', encoding='utf-8').read()

en_dialogs = [m.group(2) for m in re.finditer(r'^    (s|l|h|ha|si|d) "(.*)"$', SL, re.M)]
en_thoughts = [m.group(1) for m in re.finditer(r'^    th "(.*)"$', SL, re.M)]
en_choices = [m.group(1) for m in re.finditer(r'^        "(.*)":\s*(#.*)?$', SL, re.M)]

print('counts en: d=%d t=%d c=%d' % (len(en_dialogs), len(en_thoughts), len(en_choices)))

ru_all = RU_DIALOGS + RU_THOUGHTS + RU_CHOICES
bad = [s for s in ru_all + en_dialogs + en_thoughts + en_choices if '"' in s]
print('strings with double quote:', len(bad), bad[:3])

# JA extraction check for embedded newlines: reuse gen module
import importlib.util
spec = importlib.util.spec_from_file_location('gen', 'tools/gen_ch4_5_tl.py')
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)
import os
sys.stdout = io.TextIOWrapper(os.fdopen(1, 'wb', closefd=False),
                              encoding='utf-8', errors='replace')
src_d, src_t, src_c = gen.extract_source()
nl = [j for _, j in src_d + [(None, x) for x in src_t] + [(None, x) for x in src_c] if '\n' in j]
print('JA strings with newline:', len(nl))

# duplicate old check
targets = {
    'game/tl/russian/dialogs.rpy': en_dialogs,
    'game/tl/japanese/dialogs.rpy': en_dialogs,
    'game/tl/russian/thoughs.rpy': en_thoughts,
    'game/tl/japanese/thoughs.rpy': en_thoughts,
    'game/tl/russian/choises.rpy': en_choices,
    'game/tl/japanese/choises.rpy': en_choices,
}
for path, olds in targets.items():
    text = open(path, encoding='utf-8').read()
    hits = [o[:60] for o in olds if o in text]
    print('%s: overlapping olds = %d %s' % (path, len(hits), hits[:3]))

print('PREFLIGHT DONE')
