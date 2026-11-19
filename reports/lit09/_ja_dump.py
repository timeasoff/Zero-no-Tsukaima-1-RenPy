import glob
p = glob.glob('ps2_source/chapters/chapter_90_*.txt')[0]
t = open(p, encoding='utf-8').read().split('\n')
ranges = [(275,292),(655,670),(1345,1360),(1528,1542),(1590,1620),(1760,1800),(2650,2665),(3475,3495),(3545,3570),(3595,3620)]
for a,b in ranges:
    print('==== lines',a,'-',b)
    for i in range(a-1,min(b,len(t))):
        print(i+1, t[i])
