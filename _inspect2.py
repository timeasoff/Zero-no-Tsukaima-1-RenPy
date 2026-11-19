#!/usr/bin/env python3
import re
from pathlib import Path
root = Path(__file__).parent
d = root / "game/tl/russian"
# occurrences of 'у Харуна' (undeclined after у) vs 'у Харуны'
for f in sorted(d.rglob("*.rpy")):
    t=f.read_text(encoding="utf-8")
    for m in re.finditer(r"[Уу] Харуна\b", t):
        s=max(0,m.start()-30); e=min(len(t),m.end()+40)
        print("UND 'у Харуна':", f.name, repr(t[s:e]))
print("--- count y Харуна / y Харуны ---")
tot_u_haruna=0; tot_u_haruny=0
for f in sorted(d.rglob("*.rpy")):
    t=f.read_text(encoding="utf-8")
    tot_u_haruna+=len(re.findall(r"[Уу] Харуна\b", t))
    tot_u_haruny+=len(re.findall(r"[Уу] Харуны\b", t))
print("у Харуна:", tot_u_haruna, " у Харуны:", tot_u_haruny)
