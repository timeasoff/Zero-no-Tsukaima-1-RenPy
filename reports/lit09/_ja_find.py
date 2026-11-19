import glob, re
p = glob.glob('ps2_source/chapters/chapter_90_*.txt')[0]
t = open(p, encoding='utf-8').read().split('\n')
keys = ['ミスタ', '血しぶき', '血', 'デルフリンガー', 'かわいい子', '力ん', '調子', '妻', '女房', 'おかみ', 'ご主人様', '最高', 'すごい']
for k in keys:
    print('###', k)
    hits = [(i+1,l) for i,l in enumerate(t) if k in l]
    for ln,l in hits[:18]:
        print(ln, l[:130])
    print('count', len(hits))
