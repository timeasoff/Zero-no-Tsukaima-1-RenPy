#!/usr/bin/env python3
"""Chapter 18 part 3 (scenes 714-723): infiltration, Zero Fighter Without fuel."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
299: ("R-Right! I'll come back to help right away!", "П-Понял! Я сразу вернусь с подкреплением!"),
300: ("Now that it's settled, let's hurry, Saito!", "Раз решили — идём быстрее, Сайто!"),
301: ("Kirche, Tabitha... But I...", "Кирке, Табаса… Но я…"),
302: ("Ugh, enough! Go, Saito!!", "Ну же, хватит! Идём, Сайто!!"),
303: ("Wait a moment. Louise...!", "Подожди. Луиза…!"),
304: ("I'll stay here and fight too!", "Я тоже останусь здесь и буду сражаться!"),
305: ("What are you saying, Saito! Do you understand what Kirche meant? Let's go!",
      "Что ты говоришь, Сайто! Ты понял, что имела в виду Кирке? Идём!"),
306: ("Wait a moment. Louise...!", "Подожди. Луиза…!"),
307: ("Kirche! I'll definitely repay this debt!", "Кирке! Я обязательно верну этот долг!"),
308: ("Until then, don't let Reconquista beat you!", "А до тех пор не дай Реконкисте победить себя!"),
309: ("Don't say such things... The slight-fever and snow-gale combo is invincible. "
      "Right, Tabitha?",
      "Не говори такого… Дуэт лёгкого жара и снежного вихря непобедим. Правда, Табаса?"),
310: ("...", "…"),
311: ("T-Then I'm counting on you! Let's go, Saito!!", "Т-Тогда я на вас рассчитываю! Идём, Сайто!!"),
312: ("Hey, Louise. Are Kirche and Tabitha really going to be okay?",
      "Эй, Луиза. Кирке и Табаса и правда будут в безопасности?"),
313: ("They volunteered as decoys for the enemy! And you still want to go back?",
      "Они сами вызвались приманкой для врага! И ты всё равно хочешь вернуться?"),
314: ("...", "…"),
315: ("Let's go, Saito. If you feel sorry toward Kirche and the others...",
      "Идём, Сайто. Если ты чувствуешь вину перед Кирке и остальными…"),
316: ("Then reach Tristain in your Zero Fighter as fast as you can.",
      "То как можно скорее доберись до Тристании на своём Zero Fighter."),
317: ("O-Okay...", "Д-Да…"),
318: ("Oh boy...", "Ох…"),
319: ("Even though we expected it... so many soldiers...", "Хоть мы и ожидали… столько солдат…"),
320: ("(What Louise and I saw when we reached the plaza with the Zero Fighter...)",
      "(Что мы с Луизой увидели, когда пришли на площадь к Zero Fighter…)"),
321: ("(The Zero Fighter surrounded by nearly ten Reconquista soldiers.)",
      "(Zero Fighter, окружённый почти десятью солдатами Реконкисты.)"),
322: ("What'll you do, partner?", "Что будешь делать, приятель?"),
323: ("Taking on this many is a bit of a chore, but if we dawdle, more may come.",
      "С этим количеством справиться непросто, но если тянуть, врагов может стать больше."),
324: ("Fine, let's clear them out fast!", "Ладно, быстро покончим с ними!"),
325: ("Exactly. Now, let's go...", "Верно. Ну же, идём…"),
326: ("No, wait, don't rush.", "Нет, подожди, не спеши."),
327: ("Nobody's rushing. If more enemies come, we'll be in real trouble.",
      "Никто не спешит. Если врагов станет больше, нам будет непросто."),
328: ("Let's take care of them quickly... okay?", "Быстро покончим с ними… ладно?"),
329: ("What do you think, Louise?", "Как думаешь, Луиза?"),
330: ("I agree with Derflinger. Since they haven't noticed us yet, we'll have fewer to fight.",
      "Я согласна с Дерфлингером. Пока они нас не заметили, врагов будет меньше."),
331: ("Right. Okay...", "Верно. Ладно…"),
332: ("Honestly, you stupid Saito!", "Ну же, глупый Сайто!"),
333: ("Who's there! Who is it!?", "Кто там! Кто это!?"),
334: ("Let's go! Derf!", "Идём! Дерф!"),
335: ("Well, here we go.", "Ну что ж, пошли."),
336: ("We managed, didn't we.", "Нам удалось, да?"),
337: ("Fighting while protecting the Zero Fighter... takes some care.",
      "Сражаться, защищая Zero Fighter… требует осторожности."),
338: ("So, will this thing fly?", "Так, эта штука полетит?"),
339: ("Wait a second. Let me see... No good. The instruments are fine, "
      "the flaps are fine, but...",
      "Подожди. Дай посмотреть… Нет. Приборы в порядке, закрылки тоже, но…"),
340: ("We're short on gasoline.", "Не хватает бензина."),
341: ("Gaso-what?", "Бен-чего?"),
342: ("Gasoline is like magic power for magic. Without it, the Zero Fighter won't fly.",
      "Бензин для Zero Fighter — что магическая сила для магии. Без него он не полетит."),
343: ("So it's useless, then?", "Значит, он бесполезен?"),
344: ("Colbert-sen might have a spare, but to get there we'd have to cut through "
      "the school building...",
      "У Кольбера-сэна может быть запас, но чтобы туда попасть, придётся пройти "
      "через здание академии…"),
345: ("And if Mr. Colbert isn't in the lab, we can't get in... Too risky.",
      "И если Кольбера нет в лаборатории, мы не попадём… Слишком рискованно."),
}
CHOICES = {
718: [("Fine, let's clear them out fast!", "Ладно, быстро покончим с ними!"),
      ("No, wait, don't rush", "Нет, подожди, не спеши"),
      ("What do you think, Louise?", "Как думаешь, Луиза?")],
723: [("Let's go to the lab", "Пойдём в лабораторию"),
      ("Maybe we should retreat for now", "Может, пока отступить"),
      ("Let's think", "Подумаем")],
}
SPK = {'サイト': 's', 'ルイズ': 'l', 'キュルケ': 'k', 'タバサ': 't',
       'デルフリンガー': 'd', '兵士ＭＳ': 'soldier', 'null': 'th'}
START = {'s': 162, 'l': 112, 'k': 32, 't': 22, 'd': 22, 'soldier': 10, 'th': 0}


def main():
    data = json.load(open('reports/ch18/parse_696_738.json', encoding='utf-8'))
    script = ['# Глава 18, часть 3 (сцены 714–723): прорыв к Zero Fighter.',
              '# Источник: ps2_source/chapters/chapter_19_貴族の意地.txt (SCENE 714-723).',
              '', 'label ch18_3:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 723:
                break
            if x['no'] < 714:
                continue
            scene = x['no']
            script += ['label ch18_3_scene_%d:' % scene, '']
            continue
        if k == 'event':
            if scene:
                event(x['src'], script)
            continue
        if k == 'dlg':
            idx = x['idx']
            if idx not in T:
                continue
            en, ru = T[idx]
            if en is None:
                script.append('    # ' + x['src'] + ' (no voice)')
                continue
            en = en_norm(en)
            spk = SPK.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch18_%s_%03d' % (spk, counters[spk])
            full = '%s{#%s}' % (en, tag)
            script.append('    # ' + x['src'])
            if x['voice'] is not None:
                script.append('    voice "%s"' % tag)
                manifest.append((tag, x['voice']))
            script.append('    %s "%s"' % (spk, full))
            ja_new = x['ja'] if x['thought'] else '%s：%s' % (x['speaker'], x['ja'])
            ja_d += ['    old "%s"' % full, '    new "%s"' % ja_new, '']
            ru_d += ['    old "%s"' % full, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'choice':
            if scene is None or scene not in CHOICES:
                continue
            script.append('    menu:')
            for i, o in enumerate(x['options']):
                en, ru = CHOICES[scene][i]
                ctext = '%s{#ch18_3_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump %s' % ('ch18_3_scene_%d' % o['target'] if 714 <= o['target'] <= 723 else 'ch18_4'))
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 714 <= scene <= 723:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch18_3_scene_%d' % x['target']
                                          if 714 <= x['target'] <= 723 else 'ch18_4'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 3 ====', '    jump ch18_4', '    return', '']
    files = {
        'game/chapters/18/script-ch18_3.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch18_3_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch18_3_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch18_3_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch18_3_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch18/voice_map_3.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
