import glob
p = glob.glob('ps2_source/chapters/chapter_90_*.txt')[0]
t = open(p, encoding='utf-8').read().split('\n')
for a,b in [(2115,2152),(2375,2395),(3110,3165),(3260,3280),(2140,2150),(3060,3080)]:
    print('====',a,'-',b)
    for i in range(a-1,min(b,len(t))):
        print(i+1, t[i])
