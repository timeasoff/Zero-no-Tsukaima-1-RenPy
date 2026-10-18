# -*- coding: utf-8 -*-
"""Patch: ASCII-safe final print in gen_ch4_5_voices.py (cp1251 console)."""
p = 'tools/gen_ch4_5_voices.py'
b = open(p, 'rb').read()
old = '✅ '.encode('utf-8')
new = ''.encode('utf-8')
assert b.count(old) == 1, b.count(old)
b = b.replace(old, new)
open(p, 'wb').write(b)
print('patched ok')
