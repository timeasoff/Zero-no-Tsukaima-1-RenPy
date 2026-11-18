#!/usr/bin/env python3
"""Chapter 25 part 4 (extra 1513-1532): four dates with Tabitha."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
384: ("Hmm, the theater, huh.", "Хм, театр, значит."),
385: ("What?", "Что?"),
386: ("I was saying how different the impression is before the play starts and after it ends.",
     "Я говорил, насколько разное впечатление до начала спектакля и после его конца."),
387: ("Standing in front of the theater like this, I get a little... well, nostalgic.",
     "Стоя вот так перед театром, я немного… ну, ностальгирую."),
388: ("...?", "…?"),
389: ("Umm, you see...", "Э-Э, видишь ли…"),
390: ("It was a nice break, I was saying.", "Это был хороший отдых, говорил я."),
391: ("Sure, the practice and helping out were hard, but I felt a real sense of fulfillment afterwards.",
     "Конечно, репетиции и помощь были тяжёлыми, но потом я почувствовал настоящее удовлетворение."),
392: ("Mm.", "Мм."),
393: ("We had a rare experience, I was saying.", "Мы получили редкий опыт, говорил я."),
394: ("Nobles and royals hardly ever take part in a play, do they?", "Дворяне и королевские особы почти никогда не участвуют в спектаклях, да?"),
395: ("Mm.", "Мм."),
396: ("Then it's sure to become a memory for life, I think.", "Тогда это наверняка станет воспоминанием на всю жизнь, думаю я."),
397: ("...", "…"),
398: ("We found Haruna's bag, too.", "И сумку Харуны мы нашли."),
399: ("What's more, by helping with the play, we not only got the bag back—we even got paid.",
     "Больше того, помогая со спектаклем, мы не только вернули сумку — нам даже заплатили."),
400: ("...", "…"),
401: ("Hmm? What's wrong? Did something bother you?", "Хм? Что случилось? Тебя что-то задело?"),
402: ("No...", "Нет…"),
403: ("But there was the mission to find the bomber.", "Но ведь было задание — найти бомбиста."),
404: ("Oops. That's something we promised not to bring up.", "Ой. Об этом мы обещали не вспоминать."),
405: ("Promised?", "Обещали?"),
406: ("Promised.", "Обещали."),
407: ("Mm...", "Мм…"),
408: ("So, Tabitha—do you have any memories that'll turn out nice, too?", "Так, Табаса — а у тебя есть воспоминания, которые станут хорошими?"),
409: ("...", "…"),
410: ("Eh? Ehh!? Why are you so red in the face!?", "А? А-а!? Почему у тебя такое красное лицо!?"),
411: ("I-It's nothing.", "Н-Ничего."),
412: ("R-Really? Still, I enjoyed it—having you as the heroine.",
     "П-Серьёзно? Впрочем, мне было весело — с тобой в роли героини."),
413: ("...", "…"),
414: ("Why are you turning red?", "Почему ты краснеешь?"),
415: ("Wow—the market's got a whole different energy. It's overflowing with rare things.",
     "Ого — рынок живёт совсем другой жизнью. Он полон редких вещей."),
416: ("Ah, a little bird. How cute!", "Ах, птичка. Какая милая!"),
417: ("Cute?", "Милая?"),
418: ("Huh? It's not cute?", "А? Она не милая?"),
419: ("It's for eating.", "Это на еду."),
420: ("Eh, really? Even though it's so cute...", "А, правда? Такая милая, а её едят…"),
421: ("It's a famous ingredient.", "Это известный ингредиент."),
422: ("I see.", "Понятно."),
423: ("Mm. Delicious...", "Мм. Вкусно…"),
424: ("It's delicious, huh...", "Вкусно, значит…"),
425: ("But it makes me feel a little sorry for it.", "Но мне жаль её."),
426: ("Maybe.", "Может."),
427: ("Right?", "Верно?"),
428: ("I can't eat that dish anymore. I'd think of it.", "Я больше не смогу есть это блюдо. Буду вспоминать."),
429: ("(It's that delicious!? )", "Настолько вкусно, что расстроилась!?"),
430: ("Truly a cross-cultural experience.", "Это и есть настоящий культурный обмен."),
431: ("Cross-cultural?", "Опыт другой культуры?"),
432: ("Yeah. But once you taste it, you might stop thinking it's cute at all.",
     "Да. Но стоит попробовать — и ты можешь перестать считать её милой."),
433: ("I'd like to try it once. If you say it's good, Tabitha, it must be.",
     "Хочу попробовать однажды. Если ты говоришь, что вкусно, Табаса, наверное, так и есть."),
434: ("...", "…"),
435: ("Ah, but maybe it's a luxury ingredient? Then it wouldn't be so easy to get.",
     "Ах, но может, это деликатес? Тогда так просто его не попробуешь."),
436: ("It's fine. It's home cooking.", "Всё хорошо. Это домашняя еда."),
437: ("I see. Then maybe someday I can eat it.", "Понятно. Тогда, может, когда-нибудь я её попробую."),
438: ("So, what kind of dish is it, exactly?", "Так, какое именно блюдо это?"),
439: ("It'll take a while.", "Будет долго, ладно?"),
440: ("Please keep it short, if possible.", "По возможности, покороче, пожалуйста."),
441: ("You skewer bite-sized pieces of meat and roast them while brushing on sauce.",
     "Ты нанизываешь кусочки мяса на шампур и жаришь их, смазывая соусом."),
442: ("Hey, that's yakitori...", "Эй, да это же якитори…"),
443: ("???", "???"),
444: ("They call it a back street, but it doesn't feel very back-alleyish, does it?",
     "Называют её задней улицей, но она не слишком похожа на переулок, да?"),
445: ("There are plenty of people and shops. Just...", "Людей и магазинов достаточно. Просто…"),
446: ("Just?", "Просто — что?"),
447: ("I'm a bit thirsty. I was thinking I'd like a drink. There are no convenience stores here, though.",
     "Я немного жажду. Хочется выпить. Но здесь нет круглосуточных магазинов."),
448: ("Convenience store?", "Круглосуточный магазин?"),
449: ("Ah, no—I mean one of those shops back home that's open 24 hours...",
     "Ах, нет — я про такой магазин у меня дома, который открыт 24 часа…"),
450: ("???", "???"),
451: ("Man, I'm thirsty.", "Ох, как же я жажду."),
452: ("...", "…"),
453: ("What's wrong?", "Что случилось?"),
454: ("Alcohol.", "Алкоголь."),
455: ("No, I mean—there is a bar right in front of us, though...",
     "Нет, я хотел сказать — прямо перед нами есть бар, но…"),
456: ("I'm underage back home...", "У меня дома я ещё несовершеннолетний…"),
457: ("Underage?", "Несовершеннолетний?"),
458: ("Well, where I come from, you're not allowed to drink until you're an adult.",
     "Ну, у меня дома не разрешают пить, пока не станешь взрослым."),
459: ("Not allowed to drink?", "Не разрешают пить?"),
460: ("If you do, you get scolded something fierce.", "Если выпьешь — тебя здорово отругают."),
461: ("Strange.", "Странно."),
462: ("Could it be you're drinking from morning?", "Неужто ты пьёшь с утра?"),
463: ("...", "…"),
464: ("Um... I'd prefer a drink without alcohol...", "Э-Э… Я бы лучше выпил что-то без алкоголя…"),
465: ("...", "…"),
466: ("I'd rather have a normal drink than alcohol.", "Я бы лучше выпил обычное питьё, чем алкоголь."),
467: ("Normal?", "Обычное?"),
468: ("Um, not alcohol—if possible, something without alcohol in it.",
     "Э-Э, не алкоголь — если можно, что-нибудь без спирта."),
469: ("Why?", "Почему?"),
470: ("Because... Well, drinking in the daytime is a bit... No, of course it's no good at night, either.",
     "Потому что… Ну, пить днём как-то… Нет, конечно, и ночью тоже нельзя."),
471: ("...?", "…?"),
472: ("Besides, I'd hate to get drunk and cause you trouble, Tabitha.",
     "И ещё — не хочется напиться и доставить тебе хлопот, Табаса."),
473: ("I'm sorry.", "Простите."),
474: ("Ah, no—you don't need to apologize. If we look hard enough, there'll be a drink somewhere...",
     "Ах, нет — вам не нужно извиняться. Если поискать, найдётся какое-нибудь питьё…"),
475: ("Ah, look! I'll buy a drink at that shop!", "Ах, смотрите! Куплю питьё в том магазине!"),
476: ("Ah... That's seasoning...", "Ах… Это приправа…"),
477: ("Whoa! Why do they sell it in such huge quantities!", "Ого! Почему её продают такими огромными количествами!"),
478: ("Sorry.", "Простите."),
479: ("No, it's fine. Look, let's search somewhere else.", "Нет, всё хорошо. Смотрите, поищем в другом месте."),
480: ("Mm.", "Мм."),
481: ("Walking like this, the two of us looking around—it's nice, but...",
     "Идти вот так вдвоём и смотреть по сторонам — хорошо, но…"),
482: ("...", "…"),
483: ("(Who would have thought Tabitha's casual clothes had this much destructive power...)",
     "Кто бы мог подумать, что повседневная одежда Табасы настолько сокрушительна…"),
484: ("What's wrong?", "Что случилось?"),
485: ("No, it's just...!? I was thinking these casual clothes suit you really well.",
     "Нет, я просто…!? Я так, подумал, что эта повседневная одежда тебе идёт."),
486: ("...", "…"),
487: ("Um... Outside the academy, do you always dress like this?", "Э-Э… Вне академии ты всегда так одеваешься?"),
488: ("...", "…"),
489: ("Eh? That's not it?", "А? Это не так?"),
490: ("Kirche picked this out.", "Это выбрала Кирке."),
491: ("I see...", "Понятно…"),
492: ("As expected of Kirche. It really suits you, Tabitha.", "Как и подобает Кирке. Тебе очень идёт, Табаса."),
493: ("...", "…"),
494: ("If only the amount of skin shown were more like Kirche's...", "Хоть бы открытости было столько же, сколько у Кирке…"),
495: ("...", "…"),
496: ("...I'm sorry. I got carried away.", "…Простите. Я зарвался."),
497: ("Next time, I want to see clothes Tabitha picked herself.", "В следующий раз хочу увидеть одежду, которую Табаса выбрала сама."),
498: ("Someday.", "Когда-нибудь."),
499: ("Kirche worries too much, doesn't she.", "Кирке тоже слишком волнуется, да?"),
500: ("...?", "…?"),
501: ("Tabitha, I think you'd look good in anything—Kirche doesn't need to look after you.",
     "Табаса, я думаю, тебе идёт всё — Кирке не нужно за тобой присматривать."),
502: ("That's not true.", "Это не так."),
503: ("Isn't it? I don't think so, though.", "Серьёзно? Я вот не думаю."),
504: ("Seriously?", "Серьёзно?"),
505: ("Yeah. Seriously.", "Да. Серьёзно."),
506: ("...", "…"),
507: ("But... I don't look at it much.", "Но… Я не смотрю на неё часто."),
508: ("Eh, why not?", "А, почему?"),
509: ("It's embarrassing, after all.", "Ведь неловко."),
510: ("O-Of course it is. Ha ha, ha ha...", "К-Конечно. Ха-ха, ха-ха…"),
}
CHOICES = {
1513: [("It was a good break", "Это был хороший отдых"),
       ("A rare experience", "Редкий опыт"),
       ("We found Haruna's bag", "Мы нашли сумку Харуны")],
1518: [("I feel sorry for it", "Мне жаль её"),
       ("A cross-cultural experience", "Опыт другой культуры"),
       ("I'd like to try it", "Хочу попробовать")],
1523: [("I'm underage", "Я несовершеннолетний"),
       ("Drinking in the morning?", "Пьёшь с утра?"),
       ("I'd rather have a normal drink", "Я лучше обычное питьё")],
1528: [("As expected of Kirche", "Как и подобает Кирке"),
       ("Clothes Tabitha picked", "Одежда, выбранная Табасой"),
       ("Kirche worries too much", "Кирке слишком волнуется")],
}
SPK = {'サイト': 's', 'タバサ': 't', 'null': 'th'}
START = {'s': 163, 't': 77, 'th': 6}


def main():
    data = json.load(open('reports/ch25/parse_903_933.json', encoding='utf-8'))
    script = ['# Глава 25, часть 4 (extra 1513–1532): свидания с Табасой.',
              '# Источник: ps2_source/chapters/chapter_26_手紙の秘密.txt (extra 1513-1532).',
              '', 'label ch25_4:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if not 1513 <= x['no'] <= 1532:
                scene = None
                continue
            scene = x['no']
            script += ['label ch25_4_scene_%d:' % scene, '']
            continue
        if k == 'event':
            if scene: event(x['src'], script)
            continue
        if k == 'dlg':
            idx = x['idx']
            if idx not in T: continue
            en, ru = T[idx]
            en = en_norm(en)
            spk = SPK.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch25_%s_%03d' % (spk, counters[spk])
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
            if scene is None or scene not in CHOICES: continue
            script.append('    menu:')
            for i, o in enumerate(x['options']):
                en, ru = CHOICES[scene][i]
                ctext = '%s{#ch25_4_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch25_4_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 1513 <= scene <= 1532: continue
            script.append('    # → next scene %d' % x['target'])
            if 1513 <= x['target'] <= 1532:
                script.append('    jump ch25_4_scene_%d' % x['target'])
            else:
                script.append('    jump ch26')
            script.append('')
    script += ['    # move(): возврат в сцену 927 (moveInit в 922)', '    # ==== КОНЕЦ ЧАСТИ 4 ====', '    jump ch25_2_scene_927', '    return', '']
    files = {
        'game/chapters/25/script-ch25_4.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch25_4_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch25_4_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch25_4_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch25_4_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch25/voice_map_4.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
