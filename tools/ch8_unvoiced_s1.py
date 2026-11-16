# -*- coding: utf-8 -*-
"""S1: find talk units (consecutive non-indented lines) WITHOUT [voice N] in chapter_09."""
import re, io, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(ROOT, "ps2_source", "chapters")
name = [f for f in os.listdir(src) if f.startswith("chapter_09_")][0]
path = os.path.join(src, name)

out = io.StringIO()
cur = None
buf = []
voiced = False
units = []

def flush():
    global buf, voiced
    if buf:
        units.append((cur, "VOICE" if voiced else "NOVOICE", " / ".join(buf)))
    buf, voiced = [], False

with open(path, encoding="utf-8") as f:
    for line in f:
        m = re.match(r"---- SCENE (\d+) ----", line)
        if m:
            flush()
            cur = int(m.group(1))
            continue
        s = line.rstrip("\n").rstrip()
        if not s:
            continue
        if s.startswith(" "):  # event line
            flush()
            continue
        buf.append(s)
        if "[voice " in s:
            voiced = True
            flush()

flush()

n_v = sum(1 for u in units if u[1] == "VOICE" and u[0] is not None)
n_nv = sum(1 for u in units if u[1] == "NOVOICE" and u[0] is not None)
out.write("voiced talk units=%d unvoiced talk units=%d\n\n" % (n_v, n_nv))
for u in units:
    if u[1] == "NOVOICE" and u[0] is not None:
        out.write("SCENE %d UNVOICED: %s\n" % (u[0], u[2]))

with open(os.path.join(ROOT, "reports", "_tmp_ch8_s1_unvoiced.txt"), "w", encoding="utf-8") as f:
    f.write(out.getvalue())
print("voiced=%d unvoiced=%d" % (n_v, n_nv))
