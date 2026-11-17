#!/usr/bin/env python3
"""Phase 2 summaries for ch15 parts 2-4."""
import json
RUN='20261118-014000'
D={
2:[('ch15_l_051','глупыш','добавка, убрана'),('ch15_l_059','しつこい','надоедливый'),
   ('ch15_soldier_002','生徒風情','академишки'),('ch15_h_029','来ましたか','Вот оно и пришло'),
   ('ch15_commander_003','模様だと','как сообщают'),('ch15_s_040','奴ら','эти')],
3:[('ch15_s_080','時間を稼ぐ','выиграть время'),('ch15_k_034','ひどい','ужасно'),
   ('ch15_k_042','病み上がり/いたわって','на поправке/нежнее'),
   ('ch15_l_066','守ってね','мягкая просьба'),('ch15_m_010','подгоняла','подгонял (род)'),
   ('ch15_m_015','いくわよ','пошла')],
4:[('ch15_s_107','おわっ','Ой!'),('ch15_w_001','最高の舞台','великолепный спектакль'),
   ('ch15_k_047','年増達','эти старух'),('ch15_ak_026','でしょう？','Правда?'),
   ('ch15_w_006','うるさい','Надоело'),('ch15_l_091','限界','на пределе'),
   ('ch15_d_005/d_006','相棒','убрано'),('ch15_s_112','虚無の…','Луиза создала силой Пустоты')]}
for p,rows in D.items():
    obj={'analysis_id':f'{RUN}-ch15-p{p}','part':f'ch15_{p}','phase':2,
         'findings':[{'tag':r[0],'ja':r[1],'status':'CONFIRMED_ERROR','action':'FIXED','reason':r[2]} for r in rows]}
    t=['# Analyzer — Фаза 2, ch15 часть %d'%p,'',
       '- analysis_id: `%s`'%obj['analysis_id'],
       '- Итог: %d CONFIRMED_ERROR → FIXED.'%len(rows),'',
       '| Тег | JA | Статус |','|---|---|---|']
    for r in rows:t.append('| %s | %s | FIXED |'%(r[0],r[1]))
    t+=['','## JSON','','```json',json.dumps(obj,ensure_ascii=False,indent=2),'```','']
    f=f'reports/sma/ch15/{p}/analysis/{RUN}-ch15-p{p}.md'
    open(f,'w',encoding='utf-8').write('\n'.join(t))
    print('wrote',f,len(rows))
