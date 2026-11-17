#!/usr/bin/env python3
"""Phase 2 decision reports for ch12 parts 3 and 4."""
import json

RUN = '20261117-233000'
DATA = {
 3: [
  ('372','ch12_s_087','ややこしい','CONFIRMED_ERROR','FIXED','Сбивчиво→Запутанно','речь описана как несвязная, JA — о запутанной ситуации'),
  ('527','ch12_ak_065','鈍感','CONFIRMED_ERROR','FIXED','Тупой→Непроницательный','речь о нечувствительности к чувствам, не об интеллекте'),
  ('824','ch12_h_015','女の戦い','CONFIRMED_ERROR','FIXED','битва полов→женская битва','участники: женщины, а не полы'),
  ('409','ch12_ak_055','よ、よお','CONFIRMED_ERROR','FIXED','Здравствуй→Й-Йо','грубоватый регистр приветствия Акины'),
  ('247','ch12_ak_064','あなたがわたしにアイラブユー','CONFIRMED_ERROR','FIXED','я тебя люблю→ты любишь меня','падежная рамка が/に: субъект — Сайто'),
  ('34','ch12_w_005','サイト達','CONFIRMED_ERROR','FIXED','добавлено «и остальных»','達 — множественный оттенок'),
  ('166','ch12_s_088','王宮の侍女','CONFIRMED_ERROR','FIXED','фрейлина→горничная','дальше по тексту та же роль — горничная'),
  ('292','ch12_s_113','お嬢さん','CONFIRMED_ERROR','FIXED','из знатного рода→юная леди','お嬢さん не говорит о происхождении'),
  ('394','ch12_s_133','まったく、もう！','CONFIRMED_ERROR','FIXED','Ну всё, хватит→Ну и ну','возглас раздражения, не команда'),
 ],
 4: [
  ('61','ch12_h_021','あなたにも使っていた','CONFIRMED_ERROR','FIXED','добавлено «которым ты и сама пользовалась»','утраченный модификатор причастности Акины'),
  ('115','ch12_s_147','銃 / マニア','CONFIRMED_ERROR','FIXED','увлекалась оружием→фанатка огнестрельного оружия','утрачены 銃 и степень マニア'),
  ('16','ch12_s_139','とされ','CONFIRMED_ERROR','FIXED','обещали→как говорят','источник сведений — сообщение, не обещание'),
  ('55','ch12_ak_080','認められた','CONFIRMED_ERROR','FIXED','заметила→признала; талант→силу','признание достоинства, не внимание'),
  ('55','ch12_ak_080','чь→чей','CONFIRMED_ERROR','FIXED','чь→чей','согласование с «силу» (RGC-3)'),
  ('23','ch12_s_137','大きな傷跡','CONFIRMED_ERROR','FIXED','глубокие→большие','признак размера, а не глубины'),
  ('88','ch12_l_080','手先','CONFIRMED_ERROR','FIXED','орудие→пешка','личная подчинённость, а не инструмент'),
  ('354','ch12_l_084','だからね','CONFIRMED_ERROR','FIXED','понятно!→так и знай!','самоутверждение с соучаствующим тегом, не требование'),
  ('158','ch12_s_142','はずでは……','CONFIRMED_ERROR','FIXED','добавлено «кажется»','инференциальное сомнение, не констатация'),
 ],
}
AUD = {
 3: ('a/20261117-231257-e21b.md','c/20261117-231258-65d5.md','analysis/20261117-231258-a1ad.phase1.md'),
 4: ('a/20261117-231257-3860.md','c/20261117-231258-9175.md','analysis/20261117-231258-0a66.phase1.md'),
}

for part, rows in DATA.items():
    a,c,f1 = AUD[part]
    obj = {
      'analysis_id': '%s-ch12-p%d' % (RUN, part),
      'part': 'ch12_%d' % part, 'phase': 2,
      'inputs': {'a_runs':['reports/sma/ch12/%d/%s'%(part,a)],
                 'c_runs':['reports/sma/ch12/%d/%s'%(part,c)],
                 'phase1':'reports/sma/ch12/%d/%s'%(part,f1),
                 'precheck':'reports/sma/ch12/%d/precheck/'%part},
      'findings':[{'line':r[0],'tag':r[1],'ja':r[2],'status':r[3],'action':r[4],
                   'before_after':r[5],'reason':r[6]} for r in rows],
    }
    fixed=sum(1 for r in rows if r[4]=='FIXED')
    text=['# Analyzer — Фаза 2, ch12 часть %d'%part,'',
          '- analysis_id: `%s`'%obj['analysis_id'],
          '- Вход: A `%s`; C `%s`; Фаза 1 `%s`.'%(a,c,f1),
          '- Итог: %d CONFIRMED_ERROR → FIXED.'%fixed,'',
          '| Строка | Тег | JA | Статус | Disposition |',
          '|---|---|---|---|---|']
    for r in rows:
        text.append('| %s | %s | %s | %s | %s |'%(r[0],r[1],r[2],r[3],r[4]))
    text+=['','## Детали','']
    for r in rows:
        text.append('- **%s / %s**: %s. %s'%(r[0],r[1],r[5],r[6]))
    text+=['','## JSON','','```json',json.dumps(obj,ensure_ascii=False,indent=2),'```','']
    p='reports/sma/ch12/%d/analysis/%s-ch12-p%d.md'%(part,RUN,part)
    open(p,'w',encoding='utf-8').write('\n'.join(text))
    print('wrote',p,'findings',len(rows))
