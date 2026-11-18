#!/usr/bin/env python3
"""Chapter 22 part 4 (scenes 838-848): judging, Siesta declines to be Saito's maid."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
346: ("Thanks, Siesta. If I feel like eating it again, you'll treat us, right?",
      "Спасибо, Сиэста. Если вдруг захочется ещё — ты нас угостишь, да?"),
347: ("Eh? Of course! Just say the word anytime.", "А? Конечно! Скажи только слово в любой момент."),
348: ("Got it.", "Понял."),
349: ("Muuuu... Something just doesn't sit right with me.", "Мууу… Что-то мне не даёт покоя."),
350: ("Hmm, a truly wonderful dish that puts itself in the eater's place, isn't it.",
      "Хм, поистине прекрасное блюдо, словно вставшее на место того, кто его ест, да?"),
351: ("(I'll never forget the impression this curry made, I think... Not until I die.)",
      "Впечатление от этого карри я не забуду никогда… Пока не умру."),
352: ("Well then, last is Miss Tabitha's dish.", "Ну что ж, последнее — блюдо мисс Табасы."),
353: ("Hey hey, Tabitha. Just what did you make?", "Эй, Табаса. Что ты всё-таки сделала?"),
354: ("Second fermentation.", "Вторая ферментация."),
355: ("Second fermentation? What's that? What kind of dish?", "Вторая ферментация? Что это? Какое блюдо?"),
356: ("Could it be...!", "Неужто…!"),
357: ("This.", "Это."),
358: ("My, my, it's bread!", "Ого, это же хлеб!"),
359: ("Mm, the smell of fresh-baked bread! Let me have one right away!",
      "Мм, запах свежей выпечки! Сейчас же возьму один!"),
360: ("This is... This bread is...!", "Это… Этот хлеб…!"),
361: ("I knew it! This is a copy bread, isn't it!!", "Так и есть! Это же булочка, да!!"),
362: ("Copy bread?", "Булочка?"),
363: ("If she knows this strange bread, then that must be it—this is bread from another world, right?",
      "Если она знает этот странный хлеб, значит, это оно — этот хлеб из другого мира, да?"),
364: ("Ah, that's right!! I never paid attention to the name, but I always ate it. "
      "Come to think of it, it's called a copy bread, this is!", "Ах, верно!! Я никогда не обращал "
      "внимания на название, но всё время его ел. Если вспомнить, её зовут булочка, это!"),
365: ("In our world, it's an everyday bread you can get anywhere.", "В нашем мире это обычный хлеб, "
      "который можно достать где угодно."),
366: ("Amazing, aren't you, Tabitha! How did you find out about this bread?",
      "Невероятно, Табаса! Как ты узнала об этом хлебе?"),
367: ("Secret.", "Секрет."),
368: ("Let's leave the details for later and all eat already!", "Оставим подробности на потом и уже начнём есть!"),
369: ("Look, Siesta, you eat some, too!!", "Смотри, Сиэста, ты тоже поешь!!"),
370: ("Ah... Yes! Then I'll have one.", "Ах… Да! Тогда возьму одну."),
371: ("My, my. It's baked all over yet isn't crispy at all, is it?",
      "Ого. Оно пропеклось со всех сторон, но совсем не хрустит, да?"),
372: ("And it smells of milk... And it's soft.", "И пахнет молоком… И мягкое."),
373: ("Contrary to its appearance, it's so juicy, with a faint sweetness spreading in the mouth... "
      "Ah, what a sinful bread!", "Вопреки внешнему виду оно такое сочное, и лёгкая сладость "
      "растекается во рту… Ах, какой греховный хлеб!"),
374: ("This is the bread Saito-san eats in his world...", "Это хлеб, который Сайто-сан ест в своём мире…"),
375: ("Munch munch... Ah, yeah. It's so nostalgic I could cry.", "Жую-жую… Ах, да. Так ностальгично, "
      "что хочется плакать."),
376: ("How is it, Siesta? Tasty, right?", "Как оно, Сиэста? Вкусно, да?"),
377: ("Munch munch. It really is delicious!", "Мм-мм. Оно и правда вкусное!"),
378: ("Just chewing it like this is so sweet, I can't help smiling...",
      "От одного жевания становится так сладко, что невольно улыбаешься…"),
379: ("Ha ha, well, that's good.", "Ха-ха, ну, это хорошо."),
380: ("I've eaten it since I was a kid.", "Я ел его с детства."),
381: ("It's good just like this, and if you make a slit and put jam in it, it's delicious again.",
      "Оно хорошо и просто так, а если сделать надрез и положить туда варенье — снова вкусно."),
382: ("That sounds delicious!", "Звучит вкусно!"),
383: ("Back then it came with school lunches, and I often left it uneaten. "
      "Now I think about it, what a waste.", "Раньше его давали в школьных обедах, и я часто "
      "оставлял его нетронутым. Сейчас думаю — какая же это была расточительность."),
384: ("School lunch?", "Школьный обед?"),
385: ("Um, it's like a meal they serve at school.", "Э-Э, это как еда, которую дают в школе."),
386: ("To think it tastes this good now... I suppose it's the taste of memories, after all...",
      "Кто бы подумал, что сейчас оно так вкусно… Наверное, это всё же вкус воспоминаний…"),
387: ("Saito-san...", "Сайто-сан…"),
388: ("Hmm, this bread really leaves you wanting more. Could I have one more, Miss Tabitha?",
      "Хм, этот хлеб и правда оставляет желать ещё. Можно ещё один, мисс Табаса?"),
389: ("Here.", "Вот."),
390: ("The winner is... What shall we do, Old Osmond?", "Победитель… Что решим, старик Осман?"),
391: ("Hmm, yes...", "Хм, да…"),
392: ("Today was a good opportunity to learn the importance of 'sincerity' through home cooking.",
      "Сегодня был хороший случай узнать важность «искренности» через домашнюю стряпню."),
393: ("Whatever the purpose, it was wonderful that you all cooked wholeheartedly for Saito-kun, "
      "our guest of honor.", "Какой бы ни была цель, то, что вы все готовили от души для Сайто-куна, "
      "нашего почётного гостя, — прекрасно."),
394: ("The five young people who competed today are all winners—no, I wouldn't be overstating it.",
      "Все пятеро молодых людей, что сегодня соперничали, — победители. Впрочем, я бы не преувеличил."),
395: ("Begging your pardon, Old Osmond. Such an ambiguous result doesn't satisfy me. "
      "I think it's important to make things clear-cut.", "Простите, старик Осман. Такой неопределённый "
      "результат меня не устраивает. Я думаю, важно всё выяснить до конца."),
396: ("Hmm.", "Хм."),
397: ("Then how about this: let the judges vote for the dish they found delicious, "
      "and decide the winner by that?", "Тогда как насчёт этого: пусть судьи проголосуют за блюдо, "
      "которое им понравилось, и определим победителя по итогам?"),
398: ("Yes. Deciding a winner is fine.", "Да. Определить победителя можно."),
399: ("The count is complete. I'll announce the results.", "Подсчёт завершён. Объявляю результаты."),
400: ("The winner is...", "Победитель…"),
401: ("...", "…"),
402: ("(W-Who won...?)", "К-Кто победил…?"),
403: ("The winner is!", "Победитель —!"),
404: ("Mr. Colbert! Begging your pardon, but that pause is far too long!",
      "Мистер Кольбер! Простите, но пауза слишком долгая!"),
405: ("Oh, my apologies. Then, I'll announce it.", "О, прошу прощения. Тогда объявляю."),
406: ("The winner is Siesta, who made the curry stew!!", "Победитель — Сиэста, приготовившая карри!!"),
407: ("...", "…"),
408: ("Yay, Siesta. Congratulations!!", "Ура, Сиэста. Поздравляю!!"),
409: ("A-Ah... Yes!", "А-А… Да!"),
410: ("Saito-san...", "Сайто-сан…"),
411: ("What's wrong, Siesta? You won—you should be happier.", "Что случилось, Сиэста? Ты же победила — "
      "радовалась бы больше."),
412: ("Um!", "Э-Э!"),
413: ("Hmm? What is it?", "Хм? Что такое?"),
414: ("Saito-san... Which dish did you think was the most delicious...?",
      "Сайто-сан… Какое блюдо вы посчитали самым вкусным…?"),
415: ("Eh?", "А?"),
416: ("Of course, the curry was the best. Siesta's curry.", "Конечно, карри было лучшим. Карри Сиэсты."),
417: ("Is that so?", "Правда?"),
418: ("...? What's wrong?", "…? Что случилось?"),
419: ("Uggh... I'm torn between it and the curry... but I'd go with the copy bread here.",
      "Ох… Я в сомнениях между ним и карри… но здесь я выберу булочку."),
420: ("...I thought so, didn't I.", "…Так и знала."),
421: ("Siesta? What's wrong?", "Сиэста? Что с тобой?"),
422: ("No no, I was nervous at first, but everyone's cooking was great.",
      "Нет-нет, сначала я волновался, но у всех были отличные блюда."),
423: ("(Kirche's was questionable as cooking, but... I can't say that out loud.)",
      "Кирке — сомнительно, можно ли это назвать готовкой, но… вслух такого не скажешь."),
424: ("...", "…"),
425: ("Siesta, what's wrong? Why that face?", "Сиэста, что случилось? Почему у тебя такое лицо?"),
426: ("Saito-san.", "Сайто-сан."),
427: ("Yes!?", "Да!?"),
428: ("I'm sorry!! I can't be your servant, Saito-san!!", "Простите!! Я не могу быть вашей прислугой, "
      "Сайто-сан!!"),
429: ("Eh?", "А?"),
430: ("(Ah, right, I remember. She said if she won the cooking contest, she'd become my maid.)",
      "Ах, точно, вспомнил. Она говорила, что если победит в кулинарном бою, станет моей горничной."),
431: ("Siesta, why? You tried so hard in the contest.", "Сиэста, почему? Ты так старалась в состязании."),
432: ("I'm truly sorry. But I...", "Мне правда жаль. Но я…"),
433: ("I realized it when I saw you eating the copy bread Miss Tabitha made.",
      "Я поняла это, когда увидела, как вы едите булочку, которую сделала мисс Табаса."),
434: ("Realized what?", "Поняла что?"),
435: ("I tried my hardest for you, Saito-san, I really did.", "Я старалась изо всех сил ради вас, "
      "Сайто-сан, правда старалась."),
436: ("But if I understood you more deeply, I'd surely have prepared a dish even more familiar "
      "than the copy bread!", "Но если бы я понимала вас глубже, я бы наверняка приготовила блюдо "
      "ещё более родное, чем булочка!"),
437: ("True, I won the cooking contest. But that alone wasn't enough...", "Да, я выиграла кулинарный бой. "
      "Но этого одного было недостаточно…"),
438: ("That's not true, Siesta!! Your curry was just as delicious!", "Это не так, Сиэста!! "
      "Твоё карри было таким же вкусным!"),
439: ("'Just as' isn't good enough!", "«Так же» — недостаточно!"),
440: ("Ooh!?", "О-о!?"),
441: ("I think I understand Siesta's feelings... a little.", "Я, кажется, понимаю чувства Сиэсты… немного."),
442: ("In this world—no, even in your world, I'm the one who knows Saito-san best!",
      "В этом мире — нет, даже в вашем мире, я та, кто знает Сайто-сан лучше всех!"),
443: ("I realized I need to train until I can say that confidently.", "Я поняла, что должна тренироваться, "
      "пока не смогу сказать это уверенно."),
444: ("So I've decided to go back to being the academy's maid! To understand people's feelings better...",
      "Поэтому я решила вернуться к работе горничной академии! Чтобы лучше понимать чувства людей…"),
445: ("Siesta...", "Сиэста…"),
446: ("Besides, I can't keep causing Miss Valliere trouble any longer.", "И ещё я не могу и дальше "
      "доставлять неприятности мисс Вальер."),
447: ("I understand. Do as you like.", "Я поняла. Поступай как хочешь."),
448: ("Whatever the reason, if Siesta wants it, I can't stop her.", "Какова бы ни была причина, если "
      "Сиэста хочет так, я не могу её остановить."),
449: ("...Yes. It was a short time, but thank you for everything.", "…Да. Это было недолго, но спасибо за всё."),
450: ("(S-So, that wraps this up, I guess...)", "Т-Так, на этом история закончена, наверное…"),
451: ("Case closed.", "Дело закрыто."),
}
CHOICES = {
839: [("It's tasty, right?", "Вкусно, да?"),
      ("I ate it as a kid", "Я ел его в детстве"),
      ("I used to leave it", "Я его оставлял")],
844: [("Of course, curry", "Конечно, карри"),
      ("The copy bread", "Булочка"),
      ("Everything was tasty", "Всё было вкусно")],
}
SPK = {'サイト': 's', 'シエスタ': 'si', 'ルイズ': 'l', 'コルベール': 'c', 'キュルケ': 'k',
       'タバサ': 't', 'ハルナ': 'ha', 'オスマン': 'o', 'ギーシュ': 'g', 'null': 'th'}
START = {'s': 136, 'si': 58, 'l': 55, 'c': 16, 'k': 37, 't': 7,
         'ha': 21, 'o': 12, 'g': 2, 'th': 0}


def main():
    data = json.load(open('reports/ch22/parse_806_848.json', encoding='utf-8'))
    script = ['# Глава 22, часть 4 (сцены 838–848): судейство, Сиэста отказывается.',
              '# Источник: ps2_source/chapters/chapter_23_料理の鉄人.txt (SCENE 838-848).',
              '', 'label ch22_4:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 848:
                break
            if x['no'] < 838:
                continue
            scene = x['no']
            script += ['label ch22_4_scene_%d:' % scene, '']
            continue
        if k == 'event':
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
                ctext = '%s{#ch22_4_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch22_4_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 838 <= scene <= 848:
                continue
            script.append('    # → next scene %d' % x['target'])
            if 838 <= x['target'] <= 848:
                script.append('    jump ch22_4_scene_%d' % x['target'])
            elif x['target'] in (1209, 1210, 1211, 1212, 1213):
                script.append('    # date event → ch22_5')
                script.append('    jump ch22_5')
            else:
                script.append('    jump ch23')
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 4 ====', '    jump ch22_5', '    return', '']
    files = {
        'game/chapters/22/script-ch22_4.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch22_4_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch22_4_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch22_4_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch22_4_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch22/voice_map_4.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
