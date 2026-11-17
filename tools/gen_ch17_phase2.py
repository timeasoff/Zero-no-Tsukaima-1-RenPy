#!/usr/bin/env python3
"""Phase 2 summaries for ch17 parts 1-2."""
import json
RUN='20261118-020000'
D={
1:[('ch17_soldier_007','現在の位置から/二日と少々','по текущему положению/чуть больше двух дней'),
   ('ch17_soldier_001','女王陛下 vocative','Ваше Величество (не Её)'),
   ('ch17_s_025','なんだか…印象','кажется, стал'),('ch17_l_002','どさくさにまぎれて','пользуясь суматохой'),
   ('ch17_t_003','敵前逃亡','дезертирство перед врагом'),('ch17_l_014','ご機嫌麗しゅう','моё почтение'),
   ('ch17_s_034','いやだね','Не хочу'),('ch17_h_015','おそらく','Возможно')],
2:[]}
for p,rows in D.items():
    if not rows: continue
    obj={'analysis_id':f'{RUN}-ch17-p{p}','part':f'ch17_{p}','phase':2,
         'findings':[{'tag':r[0],'ja':r[1],'status':'CONFIRMED_ERROR','action':'FIXED','reason':r[2]} for r in rows]}
    t=['# Analyzer — Фаза 2, ch17 часть %d'%p,'',
       '- analysis_id: `%s`'%obj['analysis_id'],
       '- Итог: %d CONFIRMED_ERROR → FIXED.'%len(rows),'',
       '| Тег | JA | Статус |','|---|---|---|']
    for r in rows:t.append('| %s | %s | FIXED |'%(r[0],r[1]))
    t+=['','## JSON','','```json',json.dumps(obj,ensure_ascii=False,indent=2),'```','']
    f=f'reports/sma/ch17/{p}/analysis/{RUN}-ch17-p{p}.md'
    open(f,'w',encoding='utf-8').write('\n'.join(t))
    print('wrote',f,len(rows))
