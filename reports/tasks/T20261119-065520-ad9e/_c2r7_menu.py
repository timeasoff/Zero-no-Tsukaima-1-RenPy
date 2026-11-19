# -*- coding: utf-8 -*-
import re, os, json
ROOT = "/workspace/.tmp/opencode/review-ch2-5"
def read(p):
    with open(p, encoding="utf-8") as f: return f.read()
def parse_pairs(path):
    lines = read(path).splitlines(); out=[]; cur=None
    for i,ln in enumerate(lines,1):
        s=ln.strip()
        if s.startswith("old "): cur=s[4:].strip()
        elif s.startswith("new ") and cur is not None:
            out.append((cur[1:-1].replace('\\"','"') if len(cur)>1 and cur[0]=='"' and cur[-1]=='"' else cur,
                        s[4:][1:-1].replace('\\"','"') if len(s[4:])>1 and s[4:][0]=='"' and s[4:][-1]=='"' else s[4:], i))
            cur=None
    return out
def build(folder):
    m={}
    for fn in os.listdir(os.path.join(ROOT,"game/tl",folder)):
        if fn.endswith(".rpy"):
            for old,new,ln in parse_pairs(os.path.join(ROOT,"game/tl",folder,fn)):
                m[old]=(new,fn,ln)
    return m
ru=build("russian"); ja=build("japanese")
script=read(os.path.join(ROOT,"game/chapters/2/script-ch2_7.rpy"))
lines=script.splitlines()
for i,ln in enumerate(lines,1):
    m=re.match(r'^\s*"(.*?)\{#.*\}\s*:\s*$', ln)
    if m:
        en=m.group(1).replace('\\"','"')
        print(f"[L{i}] MENU")
        print("  EN:",en)
        print("  JA:",ja.get(en,("<<NONE>>",))[0])
        print("  RU:",ru.get(en,("<<NONE>>",))[0])
