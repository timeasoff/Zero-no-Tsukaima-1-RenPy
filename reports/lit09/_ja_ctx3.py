import glob
p = glob.glob('ps2_source/chapters/chapter_90_*.txt')[0]
t = open(p, encoding='utf-8').read().split('\n')
for k in ['それで十分', '大事なのは', '男の子', 'かわいい', '妙に', '変な格好', '似合う', '下着を', '普通', '服装', '趣味', '落ち着']:
    hits = [(i+1,l) for i,l in enumerate(t) if k in l]
    print('###', k, len(hits))
    for ln,l in hits[:10]:
        print(ln, l[:120])
# the 'only woof is enough' line: find  wonders
for a,b in [(1290,1322),(3000,3020),(3115,3130),(3440,3460)]:
    print('====',a,b)
    for i in range(a-1,min(b,len(t))):
        print(i+1,t[i])
