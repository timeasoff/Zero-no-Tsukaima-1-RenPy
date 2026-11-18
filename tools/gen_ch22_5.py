#!/usr/bin/env python3
"""Chapter 22 part 5 (extra scenes 1209-1213): tea with Siesta in the kitchen."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
452: ("Partner, you're looking pretty lonely there, aren't you?",
      "Приятель, у тебя довольно одинокий вид, да?"),
453: ("Ah, you can tell?", "Ах, ты видишь?"),
454: ("You always wear your heart on your face, partner.",
      "Ты всегда всё выражаешь лицом, приятель."),
455: ("I was just thinking—it's a little lonely. Starting tomorrow, when I go back to my room, "
      "Siesta's smile won't be there anymore...",
      "Я просто подумал — немного одиноко. С завтрашнего дня, когда я буду возвращаться в комнату, "
      "улыбки Сиэсты там уже не будет…"),
456: ("Whose smile?", "Чья улыбка?"),
457: ("Whoaah!", "Ой-ой-ой!"),
458: ("Good evening, Saito-san. What's wrong? Out so late...",
      "Добрый вечер, Сайто-сан. Что случилось? Так поздно…"),
459: ("N-No, I just thought I'd get some air. And you, Siesta?", "Н-Нет, я… просто подумал, может, выйти подышать воздухом. А ты, Сиэста?"),
460: ("I just went to greet Marto-san. Starting tomorrow, I get to work in the dining hall!",
      "Я как раз ходила поприветствовать Марто-сана. С завтрашнего дня я буду работать в столовой!"),
461: ("That's all thanks to you, Saito-san, too.", "И это всё благодаря вам, Сайто-сан."),
462: ("No, being told it's thanks to me makes me itch a bit... Still, I'm glad it worked out.",
      "Нет, когда мне говорят, что это благодаря мне, мне становится неловко… Но я рад, что всё получилось."),
463: ("Yes. From tomorrow I'll always be in the dining hall, so please come see me.",
      "Да. С завтрашнего дня я всегда буду в столовой, так что приходите меня навестить."),
464: ("Yeah, I got it. At noon, I'll definitely come to see you.",
      "Да, понял. В полдень я обязательно приду."),
465: ("Yes, I'll be waiting.", "Да, я буду ждать."),
466: ("By the way, Siesta, are you heading home already?", "Кстати, Сиэста, ты уже домой?"),
467: ("No. I have to prepare for tomorrow, so I'm going to clean the kitchen.",
      "Нет. Мне нужно подготовиться к завтрашнему дню, поэтому я буду убирать кухню."),
468: ("Hmm?", "Хм?"),
469: ("Um... If it's all right, would you like some tea in the kitchen?",
      "Э-Э… Если можно, не выпить ли вам чаю на кухне?"),
470: ("(W-What should I do?)", "Ч-Что мне делать?"),
471: ("Yeah, I'll go.", "Да, пойду."),
472: ("Is that so! Thank you very much.", "Правда! Спасибо вам большое."),
473: ("No, I won't.", "Нет, не пойду."),
474: ("Are you busy, Saito-san?", "Вы заняты, Сайто-сан?"),
475: ("No, that's not it, but...", "Нет, дело не в этом, но…"),
476: ("Then!", "Тогда!"),
477: ("O-Okay, I get it. Don't make that sad face. I'll go.",
      "Л-Ладно, понял. Не делай такое грустное лицо. Я пойду."),
478: ("Is that so! Thank you very much.", "Правда! Спасибо вам большое."),
479: ("Umm, what should I do...?", "Хм, что же мне делать…?"),
480: ("Are you busy, Saito-san?", "Вы заняты, Сайто-сан?"),
481: ("No, that's not it, but...", "Нет, дело не в этом, но…"),
482: ("Then!", "Тогда!"),
483: ("O-Okay, I get it. Don't make that sad face. I'll go.",
      "Л-Ладно, понял. Не делай такое грустное лицо. Я пойду."),
484: ("Is that so! Thank you very much.", "Правда! Спасибо вам большое."),
485: ("...... ... ...", "……… … …"),
486: ("Yes, here you are. It's hot, so please drink carefully, okay?",
      "Да, вот. Он горячий, так что пейте осторожно, ладно?"),
487: ("Thanks. Huh? Aren't you drinking, Siesta?", "Спасибо. А? Ты не пьёшь, Сиэста?"),
488: ("I still have cleaning left to do...", "Мне ещё нужно убирать…"),
489: ("Then I'll help you. Won't that be faster?", "Тогда я помогу. Так не быстрее ли?"),
490: ("No, Saito-san, please relax. All that's left is wiping down the shelf in the back.",
      "Нет, Сайто-сан, просто отдыхайте. Осталось только протереть полку в глубине."),
491: ("But if you do that, I can't relax either. Please, Siesta, have some tea with me, won't you?",
      "Но если ты будешь работать, я тоже не смогу отдохнуть. Прошу тебя, Сиэста, выпей со мной чаю, ладно?"),
492: ("...Mm. If Saito-san insists, I'll be indulgent and have some tea.",
      "…Хм. Раз Сайто-сан так просит, я позволю себе чаю."),
493: ("Ah, of course. I'll clean properly once I'm done.", "Ах, конечно. Когда закончу, я как следует уберу."),
494: ("You're so domestic, Siesta, aren't you?", "Ты такая домашняя, Сиэста, правда?"),
495: ("Is that so?", "Правда?"),
496: ("Well—cooking, laundry, cleaning, right? And you even look after a noble.",
      "Ну — готовка, стирка, уборка, да? И к тому же ты ещё заботишься о дворянке."),
497: ("I think anyone my age could do that much, couldn't they?",
      "Я думаю, любой человек моего возраста смог бы столько, правда?"),
498: ("I grew up looking after younger kids in the neighborhood, you see.",
      "Я выросла, присматривая за младшими детьми в соседних домах."),
499: ("When my father was away working, my mother protected our home and fields with my grandparents.",
      "Когда отец уезжал на заработки, мать вместе с дедушкой и бабушкой берегла дом и поле."),
500: ("She spun thread and wove cloth for clothes, too.", "Она ещё пряла нити и ткала ткань для одежды."),
501: ("Besides, I might just like being a busybody, you know?", "И ещё, кажется, я люблю вмешиваться в дела других, да?"),
502: ("Huh.", "Хм."),
503: ("In my world, nobody worked that hard... I'm impressed, really.",
      "В моём мире никто не работал так много… Я и правда восхищён."),
504: ("Thank you, Saito-san. But I...", "Спасибо вам, Сайто-сан. Но я…"),
505: ("Hmm?", "Хм?"),
506: ("I want to be a busybody only for you, Saito-san, someday.",
      "Я хочу когда-нибудь опекать только вас, Сайто-сан."),
507: ("Eh? T-That is...", "А? Т-Это…"),
508: ("Heh heh! Well then, I'll start cleaning the kitchen. Saito-san, please relax.",
      "Хи-хи! Что ж, я начну убирать кухню. Сайто-сан, отдыхайте."),
509: ("A... Okay...", "А… Ладно…"),
510: ("Honestly, you have it rough, partner.", "Честно, тебе непросто, приятель."),
511: ("Yeah, truly...", "Да, и правда…"),
}
CHOICES = {
1209: [("Yeah, I'll go", "Да, пойду"),
       ("No, I won't", "Нет, не пойду"),
       ("Hmm, not sure", "Хм, не знаю")],
}
SPK = {'デルフリンガー': 'd', 'サイト': 's', 'シエスタ': 'si', 'null': 'th'}
START = {'d': 0, 's': 170, 'si': 87, 'th': 0}


def main():
    data = json.load(open('reports/ch22/parse_806_848.json', encoding='utf-8'))
    script = ['# Глава 22, часть 5 (extra 1209–1213): чай с Сиэстой на кухне.',
              '# Источник: ps2_source/chapters/chapter_23_料理の鉄人.txt (extra SCENE 1209-1213).',
              '', 'label ch22_5:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if not 1209 <= x['no'] <= 1213:
                continue
            scene = x['no']
            script += ['label ch22_5_scene_%d:' % scene, '']
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
            en = en_norm(en)
            spk = SPK.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch22_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch22_5_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch22_5_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 1209 <= scene <= 1213:
                continue
            script.append('    # → next scene %d' % x['target'])
            if 1209 <= x['target'] <= 1213:
                script.append('    jump ch22_5_scene_%d' % x['target'])
            else:
                script.append('    jump ch23')
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 22 ====', '    jump ch23', '    return', '']
    files = {
        'game/chapters/22/script-ch22_5.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch22_5_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch22_5_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch22_5_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch22_5_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch22/voice_map_5.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
