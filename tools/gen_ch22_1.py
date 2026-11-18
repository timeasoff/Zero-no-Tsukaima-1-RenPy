#!/usr/bin/env python3
"""Chapter 22 part 1 (scenes 806-816): morning wake-up, cooking contest begins."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("Saito-san...", "Сайто-сан…"),
1: ("Mm.", "Мм."),
2: ("Saito-san... Saito-san.", "Сайто-сан… Сайто-сан."),
3: ("Good morning, Saito-san.", "Доброе утро, Сайто-сан."),
4: ("Waaah... Morning, Siesta. And good night.", "Вааах… Утро, Сиэста. И спокойной ночи."),
5: ("Hey, Saito-san!! Get up!", "Эй, Сайто-сан!! Вставайте!"),
6: ("It's time to wake Miss Valliere.", "Пора будить мисс Вальер."),
7: ("Ah, so it's that time... Thanks, Siesta.", "А, так вот же время… Спасибо, Сиэста."),
8: ("Not at all, Saito-san. I'm glad I could be of help.",
    "Не за что, Сайто-сан. Я рада, что могла помочь."),
9: ("(But it's been a while since someone woke me up like this... Kind of nice.)",
    "Но давно уже никто меня не будил так… И даже приятно."),
10: ("Well then, Saito-san. Next is Miss Valliere, isn't it?",
     "Ну что ж, Сайто-сан. Дальше мисс Вальер, да?"),
11: ("All right.", "Ладно."),
12: ("(I'll just yank the blanket off like usual. Louise won't wake up otherwise.)",
     "Сдерну одеяло, как обычно. Луиза иначе не просыпается."),
13: ("Take this!", "А-а-а!"),
14: ("Nyah!?", "Ня!?"),
15: ("Good morning, mistress! It's another lovely morning! Please open your eyes!",
     "Доброе утро, госпожа! Ещё одно прекрасное утро! Прошу открыть глаза!"),
16: ("You... Could you at least think about how you wake someone up...",
     "Ты… Мог бы хоть подумать, как будишь человека…"),
17: ("Wha— Wait a second!! It's not like I did anything different from usual...",
     "Что— Погоди!! Я же ничего не сделал необычного…"),
18: ("Siesta. I'll leave this to you.", "Сиэста. Предоставляю это тебе."),
19: ("Eh? Are you sure?", "А? Вы уверены?"),
20: ("Yeah. Your technique... let's see it! Waking Louise—that's the trial!",
     "Ага. Твоё мастерство… покажи его! Разбудить Луизу — вот испытание!"),
21: ("I-I'll do my best!", "Я-Я постараюсь!"),
22: ("Good morning, Miss Valliere. It's about time you woke up?",
     "Доброе утро, мисс Вальер. Пора просыпаться?"),
23: ("...Mm, nyah... Si...esta... Mornin...", "…Мм, ня… Си…эста… Утра…"),
24: ("Magnificent, Siesta! You managed to wake Louise, who's always low-blood-pressure and slow to rise!",
     "Великолепно, Сиэста! Тебе удалось разбудить Луизу, которая вечно вялая по утрам!"),
25: ("Ehehe, thank you.", "Хи-хи, спасибо."),
26: ("Hey, Saito? It's fine to praise her, but where's the water for washing my face?",
     "Эй, Сайто? Хвалить можно, но где вода для умывания?"),
27: ("O-Oh no!", "О-Ой!"),
28: ("Today I'll try a new method.", "Сегодня я попробую новый метод."),
29: ("Saito-san, that is...?", "Сайто-сан, это…?"),
30: ("Heh heh, just watch.", "Хи-хи, просто смотри."),
31: ("Mistress... Phew. It's morning... Phew. Time to wake... Phew phew phew.",
     "Госпожа… Фух. Утро… Фух. Пора просыпаться… Фу-фу-фу."),
32: ("Kyaaa! What are you doing, blowing into my ear!?", "Кья-а! Что ты делаешь, дуешь мне в ухо!?"),
33: ("Good morning, Louise.", "Доброе утро, Луиза."),
34: ("That's not 'good morning, Louise'! Why can't you wake me up normally!?",
     "Это не «доброе утро, Луиза»! Почему ты не можешь будить нормально!?"),
35: ("W-Wait, calm down.", "П-Погоди, успокойся."),
36: ("Punishment first thing in the morning!?", "Наказание с самого утра!?"),
37: ("Gyaaaaaah!", "Гя-а-а-а!"),
38: ("(And then, breakfast time...)", "А затем — время завтрака…"),
39: ("There, that's everything.", "Вот, это всё."),
40: ("Amazing~~.", "Потрясающе~~."),
41: ("Well then, let's eat.", "Ну что ж, приступим."),
42: ("Heh heh.", "Хи-хи."),
43: ("Please enjoy it slowly.", "Приятного аппетита."),
44: ("O great Founder Brimir and Her Majesty the Queen.",
     "Великий Основатель Бримир и Её Величество Королева."),
45: ("We deeply thank You for granting us this modest meal this morning, too.",
     "Мы глубоко благодарим Вас за то, что и сегодня утром даровали нам эту скромную трапезу."),
46: ("All right!! The cooking contest!!", "Ну всё!! Кулинарный бой!!"),
47: ("Gng gng... Hmm? This salad is actually pretty good, isn't it?",
     "Мгм-мгм… Хм? Этот салат и правда неплох, да?"),
48: ("A, thank you! There's plenty more, so please help yourself!",
     "А, спасибо! Ещё много, так что угощайтесь без стеснения!"),
49: ("Wow, these rolls are so fluffy!", "Ох, эти булочки такие пышные!"),
50: ("That's because head chef Marto got up early and carefully kneaded the dough "
      "before baking—it's a special recipe!", "Это потому, что шеф-повар Марто встал рано, "
      "тщательно вымесил тесто и испёк его — особый рецепт!"),
51: ("Hey, are you even listening to me?", "Эй, ты меня слушаешь?"),
52: ("We're eating right now!", "Мы же едим!"),
53: ("Oh, how relaxed. I hope you're this relaxed during the match, too.",
     "О, какая невозмутимость. Хоть бы ты была такой же невозмутимой в бою."),
54: ("That goes without saying.", "Это само собой."),
55: ("I've set the battlefield in the dining hall. Once you finish breakfast, come on in. "
      "Understood?", "Я подготовила поле боя в столовой. Как закончите завтрак, приходите. "
      "Понятно?"),
56: ("I understand. I'll make you eat your words, absolutely!",
     "Понятно. Я заставлю тебя взять свои слова обратно, честно!"),
57: ("I'll look forward to it. See you then.", "Буду ждать. До встречи."),
58: ("It's gotten kind of big, hasn't it.", "Всё это как-то разрослось, да."),
59: ("For a cooking contest between a few people, so many have gathered... "
      "This academy has a lot of idle students.", "Ради кулинарного боя между несколькими "
      "людьми собралось столько народу… В этой академии полно праздных учеников."),
60: ("Yo yo, everyone, good morning. I hear our cute students have prepared a feast today?",
     "Йо-йо, всем привет. Слышал, наши милые ученики сегодня подготовили пиршество?"),
61: ("Old Osmond!? And Mr. Colbert, too!?", "Старик Осман!? И Кольбер-сэн тоже!?"),
62: ("The weather's lovely today, isn't it. Show off your skills and make something wonderful.",
     "Сегодня прекрасная погода, правда? Покажите своё мастерство и приготовьте что-то чудесное."),
63: ("Could it be that you two are judging us...?", "Неужто вы двое будете нас судить…?"),
64: ("That's right, Louise.", "Верно, Луиза."),
65: ("Kirche!?", "Кирке!?"),
66: ("Heh heh, all tired of waiting? Today I'll give you the final push!",
     "Хи-хи, устала ждать? Сегодня я добью тебя!"),
67: ("Oh, that's too bad for you. I have a trump card, too!",
     "О, жаль. У меня тоже есть козырь в рукаве!"),
68: ("Oh, really? Well, I'm looking forward to it.", "О, правда? Ну, я с нетерпением жду."),
69: ("Hey, Tabitha. What are you planning to make? Do you have confidence in winning?",
     "Эй, Табаса. Что ты собираешься готовить? Ты уверена в победе?"),
70: ("First strike wins.", "Первый удар решает."),
71: ("What's that supposed to mean?", "Что это значит?"),
72: ("Well then, let me explain the rules.", "Ну что ж, объясню правила."),
73: ("Three judges will decide. Whoever gets the most points wins. Easy to understand, right?",
     "Решат трое судей. Победит набравший больше всего очков. Просто, да?"),
74: ("No cheating, a serious fight. Let's all do our best... Heh heh heh.",
     "Без читов, честный бой. Давайте все постараемся… Хи-хи-хи."),
75: ("Gladly!", "С удовольствием!"),
76: ("I'll do my best today, too!", "И я сегодня постараюсь!"),
77: ("Please take care of us, everyone.", "Прошу о нас заботиться, все."),
78: ("Fight.", "Бой."),
79: ("Ahem, then... Let the cooking begin.", "Кхм, тогда… Начинаем готовить."),
80: ("Here we go. Will Siesta be all right?", "Ну, поехали. Сиэста справится?"),
81: ("Yes, of course.", "Да, конечно."),
82: ("I'll serve a secret family recipe from my great-great-grandfather, so look forward to it!",
     "Я приготвлю секретный рецепт моего прапрадедушки, так что ждите с нетерпением!"),
83: ("A secret recipe... I can't wait to eat it. It's Siesta's home cooking, after all!",
     "Секретный рецепт… Не могу дождаться, когда попробую. Всё-таки это стряпня Сиэсты!"),
84: ("I'll do my best! More than anything, I want Saito-san to say it's delicious!",
     "Я постараюсь! Больше всего я хочу, чтобы Сайто-сан сказал, что вкусно!"),
85: ("(Ah, Siesta, you're so cute...)", "Ах, Сиэста, ты такая милая…"),
86: ("Ouch! Who threw that ladle at me!?", "Ай! Кто швырнул в меня половник!?"),
87: ("You're my familiar, so pin your hopes on MY cooking! You're a useless familiar, truly!",
     "Ты мой фамильяр, так что возлагай надежды на МОЮ стряпню! Ты и правда никудышный фамильяр!"),
88: ("Siesta's fine, but... the others' cooking... Did I bring stomach medicine?",
     "Сиэста — ладно, но… стряпня остальных… Я взял лекарство для желудка?"),
89: ("Ah, yes. I have some stomach medicine from my grandmother in my room, so don't worry.",
     "А, да. В моей комнате есть лекарство для желудка от бабушки, так что не волнуйтесь."),
90: ("I might need it... No, I definitely will need it.",
     "Возможно, оно понадобится… Нет, оно точно понадобится."),
91: ("But it's a very bitter medicine, you know?", "Но это очень горькое лекарство, знаете?"),
92: ("Ugh. Is there nothing sweet?", "Ох. Нет ничего сладкого?"),
93: ("Hmm, I don't think so. Please drink it bravely, okay?",
     "Хм, вроде нет. Выпейте его храбро, ладно?"),
94: ("Doing your best is fine, but don't overdo it, okay?",
     "Стараться — хорошо, но не перестарайся, ладно?"),
95: ("It's fine! For Saito-san's sake, I can... do anything.",
     "Всё хорошо! Ради Сайто-сан я… могу что угодно."),
96: ("Well, when you put it that way, I get embarrassed.", "Ну, когда ты так говоришь, мне неловко."),
97: ("Ouch! Who threw that ladle at me!?", "Ай! Кто швырнул в меня половник!?"),
98: ("You're my familiar, so don't flirt with other girls. You stupid dog!",
     "Ты мой фамильяр, так что не флиртуй с другими девушками. Тупая собака!"),
99: ("I wonder how everyone's cooking is coming along...", "Интересно, как у всех дела с готовкой…"),
100: ("Well, you'd better not expect too much—especially from some people's cooking.",
      "Ну, лучше не ждать слишком многого — особенно от стряпни некоторых."),
101: ("Heh, heh, heh. A noble cooking for herself—is this Saito-kun's influence, too?",
      "Хи-хи-хи. Дворянка готовит сама — это тоже влияние Сайто-куна?"),
102: ("Yes, I think it's a good influence.", "Да, я думаю, это хорошее влияние."),
103: ("(If the food turns out decent after all, this will be a nice story... "
      "I wonder how it'll turn out...)", "Если еда и правда выйдет приличной, это будет "
      "хорошая история… Интересно, чем всё кончится…"),
}
CHOICES = {
806: [("Wake her up as usual", "Разбудить как обычно"),
      ("Leave it to Siesta", "Поручить Сиэсте"),
      ("Try a new method", "Попробовать новый метод")],
812: [("I want to eat it already", "Хочу скорее попробовать"),
      ("Did I bring stomach medicine?", "Я взял лекарство для желудка?"),
      ("Don't overdo it", "Не перестарайся")],
}
SPK = {'シエスタ': 'si', 'サイト': 's', 'ルイズ': 'l', 'ハルナ': 'ha', 'キュルケ': 'k',
       'オスマン': 'o', 'コルベール': 'c', 'タバサ': 't', 'ギーシュ': 'g',
       'モンモランシー': 'm', 'null': 'th'}
START = {'si': 0, 's': 0, 'l': 0, 'ha': 0, 'k': 0, 'o': 0, 'c': 0, 't': 0,
         'g': 0, 'm': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch22/parse_806_848.json', encoding='utf-8'))
    script = ['# Глава 22, часть 1 (сцены 806–816): утро, кулинарный бой начинается.',
              '# Источник: ps2_source/chapters/chapter_23_料理の鉄人.txt (SCENE 806-816).',
              '', 'label ch22:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 816:
                break
            scene = x['no']
            script += ['label ch22_1_scene_%d:' % scene, '']
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
                ctext = '%s{#ch22_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch22_1_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 806 <= scene <= 816:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch22_1_scene_%d' % x['target']
                                          if 806 <= x['target'] <= 816 else 'ch22_2'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch22_2', '    return', '']
    files = {
        'game/chapters/22/script-ch22.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch22_1_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch22_1_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch22_1_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch22_1_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch22/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
