#!/usr/bin/env python3
"""Chapter 21 part 4 (extra scenes 1493-1512): cooking recon, four mini-dates."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
410: ("(I wonder what Tabitha's planning to cook...)", "Интересно, что Табаса собирается готовить…"),
411: ("Who is it?", "Кто там?"),
412: ("It's me, Tabitha. Mind if I come in?", "Это я, Табаса. Можно войти?"),
413: ("Come in.", "Входи."),
414: ("Sorry to intrude.", "Прости за вторжение."),
415: ("If you're here to scout, don't bother.", "Если ты за разведкой — не стоит."),
416: ("Ah, I'm found out?", "Ах, я раскрыт?"),
417: ("That book you're reading—is it by any chance about cooking?",
      "Та книга, которую ты читаешь, — не о готовке ли она?"),
418: ("Secret.", "Секрет."),
419: ("You won't tell me?", "Ты не скажешь?"),
420: ("No.", "Нет."),
421: ("(As expected of Tabitha. Her defenses are impenetrable. Now, what to do?)",
      "Как и подобает Табасе. Оборона непроницаема. Ну, что же делать?"),
422: ("(All right, time to change tactics. I'll tease her.)",
      "Ладно, пора сменить тактику. Подразню её."),
423: ("I don't want to see it at all~.", "Я совсем не хочу её видеть~."),
424: ("...", "…"),
425: ("I don't want to see it, really.", "Правда не хочу."),
426: ("...", "…"),
427: ("So, show me.", "Так что покажи."),
428: ("No.", "Нет."),
429: ("Sniff sniff...", "Хлюп-хлюп…"),
430: ("(If that's how it is, I'll go with force. I'll make her show me!)",
      "Раз так, пойду напролом. Заставлю её показать!"),
431: ("Hiyah!", "Хия!"),
432: ("Whoops.", "Ой."),
433: ("You little—!!", "Ах ты!.."),
434: ("Whoops.", "Ой."),
435: ("Sniff sniff...", "Хлюп-хлюп…"),
436: ("Hmph, I suppose I'm just not good enough...", "Хмф, я и правда ни на что не годен…"),
437: ("Sulk, sulk, sulk...", "Обида-обида-обида…"),
438: ("...", "…"),
439: ("Sulk, sulk, sulk...", "Обида-обида-обида…"),
440: ("...", "…"),
441: ("So, show me.", "Так что покажи."),
442: ("No.", "Нет."),
443: ("Sniff sniff...", "Хлюп-хлюп…"),
444: ("Levitation.", "Левитация."),
445: ("Whoa!? I'm floating!", "О-о!? Я взлетел!"),
446: ("Please.", "Прошу."),
447: ("I'm being dragged into the hallway—!", "Меня вытаскивают в коридор—!"),
448: ("(What on earth could be so secret that she'd go this far?)",
      "Что же это такое, что требует таких мер?"),
449: ("Oh, it's Kirche. What are you doing?", "О, это Кирке. Что ты делаешь?"),
450: ("A~h, it's Saito. Heh heh, curious?", "А-а, это Сайто. Хи-хи, интересно?"),
451: ("Well, a little. What were you looking at so intently?",
      "Ну, немного. Что ты так пристально рассматривала?"),
452: ("No, Saito, seriously—stop peeking!", "Нет, Сайто, правда — не подглядывай!"),
453: ("What's this, just grass. Why is the shelf full of grass?",
      "Что это, просто трава. Почему полка заставлена травой?"),
454: ("It's not just grass. These are medicinal herbs Mr. Colbert is growing.",
      "Это не просто трава. Это лекарственные травы, которые выращивает Кольбер-сэн."),
455: ("Huh~. So what are you going to do with them?", "Ага~. И что ты с ними собираешься делать?"),
456: ("It's a secret.", "Секрет."),
457: ("Haah. I see.", "Аа. Понятно."),
458: ("...Hey, darling? If I come first in the cooking contest, will you go on a date with me?",
      "…Эй, дорогой? Если я займу первое место в кулинарном бою, ты пойдёшь со мной на свидание?"),
459: ("A date!?", "На свидание!?"),
460: ("If you promise, I might tell you.", "Если пообещаешь, может, я и скажу."),
461: ("Y-Yes, gladly.", "Д-Да, с удовольствием."),
462: ("Really!? Heh heh! I'm so happy!", "Правда!? Хи-хи! Я так рада!"),
463: ("Guh! Kirche, it's fine to hug me, but I can't—can't breathe!",
      "Гух! Кирке, обнимать меня можно, но я не—не могу дышать!"),
464: ("Oh, sorry.", "О, прости."),
465: ("Heh heh, but now that it's decided, I'll do my best!", "Хи-хи, а раз решили, я постараюсь!"),
466: ("T-That's a little...", "Т-Это немного…"),
467: ("Is it no good?", "Тебе не нравится?"),
468: ("W-Well, Louise could be watching from anywhere, you know!",
      "Н-Ну, Луиза может смотреть откуда угодно!"),
469: ("It's fine. If I come first, even Louise won't have anything to say. So—a date.",
      "Всё хорошо. Если я буду первой, даже Луиза не сможет возразить. Так что — свидание."),
470: ("Come on, come on, come on!", "Ну же, ну же, ну же!"),
471: ("O-Okay, I understand.", "Л-Ладно, понял."),
472: ("Heh heh! I'm so happy!", "Хи-хи! Я так рада!"),
473: ("That aside, Kirche—what dish are you planning to make?",
      "Это всё, конечно, но, Кирке, какое блюдо ты собираешься готовить?"),
474: ("Oh? Trying to change the subject, are we?", "О? Пытаешься сменить тему?"),
475: ("Ouch.", "Ой."),
476: ("Fine. I'll forgive you.", "Ладно. Прощаю."),
477: ("So, what dish?", "Так, какое блюдо?"),
478: ("It's a secret.", "Секрет."),
479: ("I see.", "Понятно."),
480: ("Well then, look forward to it on the day. I'll make something special for darling!",
      "Ну что ж, жди с нетерпением в тот день. Я приготовлю что-то особенное для дорогого!"),
481: ("A-Ah. Well then.", "А-А. Ну что ж."),
482: ("(Growing anticipation and anxiety... Will I be all right...)",
      "Растущее ожидание и тревога… Всё ли будет хорошо…"),
483: ("(Wait—I never found out about the herbs!)", "Погоди — я же так и не узнал про травы!"),
484: ("Muu.", "Му."),
485: ("(Whoa... Louise is in a bad mood.)", "Ого… Луиза не в духе."),
486: ("Saito!! I'll hear your request. Right now, name the dish you want!",
      "Сайто!! Я выслушаю твою просьбу. Немедленно назови блюдо, которое хочешь!"),
487: ("Even if you ask what my favorite food is...", "Даже если спросишь, какая моя любимая еда…"),
488: ("Come on, don't dawdle. We'll run out of time for practice, won't we?",
      "Ну же, не тяни. Время на тренировку кончится, да?"),
489: ("(Easy for you to say... A Japanese dish wouldn't make sense to you...)",
      "Легко сказать… Японское блюдо тебе и не понять…"),
490: ("S-Stew, I guess... Mom used to make it a lot.", "С-Суп… наверное. Мама часто его готовила."),
491: ("Stew, huh... Hmm...", "Суп, значит… Хм…"),
492: ("T-That reaction...", "Т-Такая реакция…"),
493: ("Could it be you're really confident in it!? Like, 'I'm particular about the cream!' or something!?",
      "Неужто ты очень уверена в нём!? Вроде «я особенно требовательна к сливкам!» или того хуже!?"),
494: ("N-Not that much! B-But, well, yes, it is one of my, um, specialties!",
      "Н-Не настолько! Н-Но, ну, да, это одно из моих, э-э, фирменных блюд!"),
495: ("(That's a lie...)", "Она лжёт…"),
496: ("You've never made stew before?", "Ты никогда не готовила суп?"),
497: ("O-Of course I have! I'm practically a chef! You'd be surprised, and I don't care!",
      "К-Конечно готовила! Я чуть не шеф-повар! Удивишься — и мне всё равно!"),
498: ("(That's definitely a lie...)", "Точно лжёт…"),
499: ("You don't know what stew is?", "Ты не знаешь, что такое суп?"),
500: ("I know! How rude!", "Знаю! Какая дерзость!"),
501: ("If we're talking stew, I'm the one. If you mention me, you mention stew—that's how well I know it!",
      "Когда речь о супе, это я. Скажи «я» — и сразу «суп», так я его знаю!"),
502: ("(That's impossible...)", "Это невозможно…"),
503: ("A question for my mistress.", "Вопрос к госпоже."),
504: ("What is it? I'll allow you to ask, just this once.", "Что? Разрешаю тебе спросить, только на этот раз."),
505: ("Before we talk about stew—have you ever cooked anything?",
      "Прежде чем говорить о супе — ты когда-нибудь готовила?"),
506: ("...", "…"),
507: ("...", "…"),
508: ("I-It's easy. You just follow the book—put the cut ingredients and seasonings in a pot, right?",
      "Э-Это легко. Просто следуй книге — положи нарезанные ингредиенты и специи в кастрюлю, да?"),
509: ("(Hang in there, me. I can do it if I try. I will definitely survive this.)",
      "Держись, я. Если постараюсь, у меня получится. Я обязательно выживу."),
510: ("What! Simply being able to eat the food my familiar makes should be thanks enough!",
      "Что! Одного того, что ты можешь есть еду, приготовленную госпожой, должно быть достаточно!"),
511: ("Whoa, she left the room... What's going to become of me...",
      "Ого, она вышла из комнаты… Что со мной будет…"),
512: ("(Huh, Haruna and Montmorency? An unusual pair.)",
      "А, Харуна и Монморанси? Необычная пара."),
513: ("Oh, it's Saito. Louise isn't here, you know.", "О, это Сайто. Луизы здесь нет."),
514: ("Just a walk, a walk. By the way, what were you two talking about?",
      "Просто гуляю, гуляю. Кстати, о чём вы двое говорили?"),
515: ("They were asking my advice about the cooking contest. I was thinking of trying a local dish "
      "from this world.", "Она просила совета насчёт кулинарного боя. Я подумываю приготовить "
      "какое-нибудь блюдо этого мира."),
516: ("Local cuisine, huh...", "Местная кухня, значит…"),
517: ("Charcoal-grilled frog, perhaps...?", "Может, лягушка на углях…?"),
518: ("We don't eat such things!", "Мы такое не едим!"),
519: ("R-Right I thought so.", "Т-Точно, я так и думал."),
520: ("Salamander tongue... perhaps?", "Язык саламандры… может?"),
521: ("Salamander—that's Kirche's familiar, isn't it? Hiraga-kun, stop joking.",
      "Саламандра — это же фамильяр Кирке, да? Хирага-кун, не шути."),
522: ("Ha ha, sorry, sorry. Of course nobody would eat that.", "Ха-ха, прости, прости. Конечно, это никто не ест."),
523: ("Oh, but they do.", "О, но её едят."),
524: ("Eh?", "А?"),
525: ("It's prized among gourmets. Since only a small amount can be harvested, "
      "it's traded at a high price.", "Это ценят гурманы. Поскольку добывают немного, "
      "продаётся оно по высокой цене."),
526: ("I see... Kirche will look at Flame differently from now on.",
      "Понятно… Теперь Кирке будет смотреть на Флейм по-другому."),
527: ("Hiraga-kun, don't! It's cruel.", "Хирага-кун, не надо! Это жестоко."),
528: ("I-I know, I know.", "Я-Я знаю, знаю."),
529: ("I've never heard of it. There's no such thing, is there?",
      "Я не слышал. Такого же не бывает, да?"),
530: ("Oh, it exists. How rude.", "О, существует. Какая дерзость."),
531: ("For example, what kind?", "Например, какое?"),
532: ("Hmm... It might be a dish unique to our lands, it's so rare.",
      "Хм… Настолько редкое, что, кажется, это блюдо есть только в наших краях."),
533: ("Oh, this sounds promising!", "О, это звучит многообещающе!"),
534: ("You melt cheese in a pot and eat it by dipping skewers of bread into it. "
      "Rare, isn't it?", "Ты плавишь сыр в кастрюле и макаешь в него хлеб на шампурах. "
      "Редкое блюдо, правда?"),
535: ("Fondue?", "Фондю?"),
536: ("So it existed in this world, too...", "Значит, и в этом мире оно было…"),
537: ("But in my house, all the servants handle everything. Even if you call it commoners' "
      "local food, it means nothing to me.", "Но у дома всеми делами занимаются слуги. "
      "Даже если ты называешь это простонародной едой, мне это ничего не говорит."),
538: ("That's no good.", "Это не годится."),
539: ("What! How rude! If you say that, I'll teach Haruna an amazing dish instead!",
      "Что! Как дерзко! Раз ты так говоришь, я лучше научу Харуну дивному блюду!"),
540: ("W-What was that?", "Ч-Что это было?"),
541: ("Heh heh, well then, Haruna, let's go.", "Хи-хи, что ж, Харуна, идём."),
542: ("Well then, Hiraga-kun. Please look forward to my cooking, too!",
      "Ну что ж, Хирага-кун. Жди с нетерпением и моей стряпни!"),
543: ("Ah, I'm looking forward to it.", "Ах, жду с нетерпением."),
544: ("(Haruna... What are they going to teach you...)", "Харуна… Что тебе туда вбивают…"),
}
CHOICES = {
1493: [("Tease her", "Подразнить её"), ("Peek", "Подсмотреть"), ("Sulk", "Обидеться")],
1498: [("Gladly!", "С удовольствием!"), ("That's a little...", "Это немного…"),
       ("That aside...", "Это всё, конечно…")],
1503: [("Very confident?", "Очень уверена?"), ("Never made it?", "Никогда не готовила?"),
       ("Don't know stew?", "Не знаешь суп?")],
1508: [("Charcoal-grilled frog?", "Лягушка на углях?"),
       ("Salamander tongue?", "Язык саламандры?"), ("Never heard of it", "Не слышал")],
}
SPK = {'サイト': 's', 'タバサ': 't', 'キュルケ': 'k', 'ルイズ': 'l',
       'モンモランシー': 'm', 'ハルナ': 'ha', 'null': 'th'}
START = {'s': 167, 't': 51, 'k': 28, 'l': 63, 'm': 10, 'ha': 13, 'th': 4}


def main():
    data = json.load(open('reports/ch21/parse_771_805.json', encoding='utf-8'))
    script = ['# Глава 21, часть 4 (extra 1493–1512): разведка перед боем, мини-свидания.',
              '# Источник: ps2_source/chapters/chapter_22_サイトのメイド.txt (extra scenes).',
              '', 'label ch21_4:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if not 1493 <= x['no'] <= 1512:
                continue
            scene = x['no']
            script += ['label ch21_4_scene_%d:' % scene, '']
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
            tag = 'ch21_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch21_4_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch21_4_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 1493 <= scene <= 1512:
                continue
            script.append('    # → next scene %d' % x['target'])
            if 1493 <= x['target'] <= 1512:
                script.append('    jump ch21_4_scene_%d' % x['target'])
            else:
                script.append('    jump ch22')
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 21 ====', '    jump ch22', '    return', '']
    files = {
        'game/chapters/21/script-ch21_4.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch21_4_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch21_4_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch21_4_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch21_4_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch21/voice_map_4.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
