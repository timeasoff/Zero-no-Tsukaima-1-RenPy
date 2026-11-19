import glob
p = glob.glob('ps2_source/chapters/chapter_90_*.txt')[0]
t = open(p, encoding='utf-8').read().split('\n')
for k in ['コルベール', 'スプラッター', 'スプラ', 'ワン', '哀れな', '情けない', '小心者', '妙な', 'その格好']:
    hits = [(i+1,l) for i,l in enumerate(t) if k in l]
    print('###', k, len(hits))
    for ln,l in hits[:20]:
        print(ln, l[:130])
print('=== ctx around 2180-2230 (scene 1618) ===')
for i in range(2175, min(2235, len(t))):
    print(i+1, t[i])
