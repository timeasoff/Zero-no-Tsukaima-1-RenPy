#!/usr/bin/env python3
"""Chapter 23 part 1 (scenes 849-867): Zero Fighter destroyed, Siesta's charm."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("...", "…"),
1: ("Saito!", "Сайто!"),
2: ("Saito... Wake up already!", "Сайто… Вставай же!"),
3: ("...!?", "…!?"),
4: ("(Oops!! Siesta isn't here anymore—and I overslept!)",
     "Ой!! Сиэсты здесь больше нет, а я проспал!"),
5: ("There's no time for dawdling!!", "Некогда тянуть время!!"),
6: ("(Which means... right now, Louise is waking me up...!?)",
     "Иными словами… сейчас Луиза будит меня…!?"),
7: ("(A grand punishment awaits!? Bad!)", "Грандиозное наказание не за горами!? Плохо!"),
8: ("S-Sorry, Louise! I apologize for oversleeping, so please, just this once, let it go!!",
     "П-Прости, Луиза! Прошу прощения, что проспал, но, пожалуйста, только на этот раз прости!"),
9: ("If you have time to punish me, you should be at class right now...",
     "Если у тебя есть время меня наказывать, то лучше бы ты сейчас была на уроке…"),
10: ("Punishment later! This is no time for that!!", "Наказание потом! Сейчас не до этого!!"),
11: ("...Eh?", "…А?"),
12: ("Ugh, good morning, Louise. I feel a bit sluggish today. Ah ha ha... Cough, cough... Ugh.",
     "Ох, доброе утро, Луиза. Я сегодня какой-то вялый. А-ха-ха… Кхм, кхм… Ох."),
13: ("Eh!? Wait a second. Do you have a fever?", "А!? Погоди. У тебя жар?"),
14: ("Hmm... No fever. What terrible timing... What should we do...",
     "Хм… Похоже, жары нет, но… Какой же неудобный момент… Что же делать…"),
15: ("Pull yourself together, honestly...", "Возьми себя в руки, право слово…"),
16: ("H-Hiraga Saito is out.", "Х-Хирага Сайто отсутствует."),
17: ("What nonsense are you spouting! This is serious!", "Что за глупости ты несёшь! Это серьёзно!"),
18: ("The princess's castle has been attacked by the bomber!", "На замок принцессы напал бомбист!"),
19: ("Seriously!?", "Правда!?"),
20: ("We're leaving right now.", "Мы выходим немедленно."),
21: ("All right—if every second counts, let's take the Zero Fighter and fly there in a flash!",
     "Ладно — если дорога каждая секунда, прыгнем на Zero Fighter и мигом долетим!"),
22: ("That's the problem!", "В том-то и дело!"),
23: ("Why not!?", "Почему не получится!?"),
24: ("The bomber's attack got the Zero Fighter too... It looks like it was destroyed this morning.",
     "От атаки бомбиста пострадал и Zero Fighter… Кажется, его разрушили утром."),
25: ("...Damn it!!", "…Чёрт!!"),
26: ("Hey!! Where are you going!? Wait!!", "Эй!! Куда ты!? Постой!!"),
27: ("No way... The right wing is blown off... There's no way this can fly...",
     "Не может быть… Правое крыло оторвано… На этом и не полетишь…"),
28: ("Saito-san!", "Сайто-сан!"),
29: ("My great-grandfather's keepsake... To think a single bomb could tear metal wings this strong...",
     "Память моего прадедушки… И всего одна бомба разорвала такие прочные металлические крылья…"),
30: ("Ah, indeed. That's more destructive than I thought.",
     "Ах, верно. Разрушительная сила больше, чем я думал."),
31: ("We have to hurry. Tristain's castle and the princess are in danger.",
     "Нужно спешить. Замок Тристании и принцесса в опасности."),
32: ("Eh... Saito-san!? Surely you're not going to the castle!?",
     "А… Сайто-сан!? Вы же не собираетесь в замок!?"),
33: ("Yeah. Louise has been called, too—I have to go with her...",
     "Да. Луизу тоже вызвали — мне нужно идти с ней…"),
34: ("No, Saito-san!! You must not go to Tristain's castle!!",
     "Нет, Сайто-сан!! Не ходите в замок Тристании!!"),
35: ("I can't do that, Siesta. I'm Louise's familiar.", "Я не могу, Сиэста. Я фамильяр Луизы."),
36: ("Louise wants to save the princess. So I have to go with her and protect my mistress.",
     "Луиза хочет спасти принцессу. Значит, я должен пойти с ней и защитить госпожу."),
37: ("But... they're too strong. This is reckless!!", "Но… они слишком сильные. Это безрассудно!!"),
38: ("Even if you are Miss Valliere's familiar...", "Даже если вы фамильяр мисс Вальер…"),
39: ("Fighting people who use such terrible bombs is far too reckless!!",
     "Сражаться с людьми, которые применяют такие ужасные бомбы, — слишком безрассудно!!"),
40: ("If you get caught up in that blast, Saito-san, you too...",
     "Если вы попадёте под взрыв, Сайто-сан, и вы тоже…"),
41: ("No! I hate it! The thought of losing you... Just thinking about it...",
     "Нет! Я не хочу! Мысль о том, что вы исчезнете… От одной мысли…"),
42: ("So... please don't go!", "Так что… пожалуйста, не уходите!"),
43: ("Siesta...", "Сиэста…"),
44: ("The castle has proper soldiers, and lots of fine nobles, too...",
     "В замке есть настоящие солдаты, и много достойных дворян…"),
45: ("So why must you—who are neither noble nor anything—fight? The world is full of strange things.",
     "Так почему вы, который не дворянин и никто иной, должны сражаться? Мир полон странных вещей."),
46: ("Saito-san, please... Don't go...", "Сайто-сан, прошу вас… Не уходите…"),
47: ("Thank you, Siesta. Worrying about me this much... I'm really happy.",
     "Спасибо, Сиэста. Так волноваться за меня… Я и правда счастлив."),
48: ("Then...", "Тогда…"),
49: ("Don't worry. I won't do anything reckless.", "Не волнуйся. Я не буду делать глупостей."),
50: ("Eh...?", "А…?"),
51: ("I'm the familiar who protects Louise. I'll never throw my life away fighting for rank "
      "or honor.", "Я фамильяр, который защищает Луизу. Я никогда не буду разменивать жизнь "
      "ради титула или чести."),
52: ("I'll bring Louise back here, safe and sound. So pray for us and wait here, Siesta.",
     "Я приведу Луизу обратно, целёхонькую. Так что молись за нас и жди здесь, Сиэста."),
53: ("Sorry, Siesta. I'm... going to fight the bomber. To protect the people I care about.",
     "Прости, Сиэста. Я… иду сражаться с бомбистом. Чтобы защитить тех, кто мне дорог."),
54: ("No...", "Нет…"),
55: ("I'm not doing it out of duty. I've decided to protect them of my own free will. So...",
     "Я делаю это не по долгу. Я сам решил защищать их. Так что…"),
56: ("I'm scared of fighting, too.", "Я тоже боюсь сражаться."),
57: ("Then!", "Тогда!"),
58: ("But, see—I can't run away here. If I run away here...",
     "Но, понимаешь — я не могу здесь убежать. Если я сейчас сбегу…"),
59: ("...I'll spend the rest of my life running. That's... No, that's why. That's why I'm going.",
     "…я всю жизнь буду только убегать. Это… Нет, поэтому. Поэтому я иду."),
60: ("I understand... Then at least, please take this charm with you...",
     "Я поняла… Тогда возьмите хоть этот оберег с собой…"),
61: ("A charm?", "Оберег?"),
62: ("Yes... This one.", "Да… Вот этот."),
63: ("This charm is... Could it be...", "Этот оберег… Неужто…"),
64: ("Yes, it's my great-grandfather's keepsake. They say if you wear it, danger will avoid you.",
     "Да, это память моего прадедушки. Говорят, если его носить, опасность будет обходить стороной."),
65: ("So please, at least wear this charm with my prayers in it...",
     "Так что прошу вас, наденьте хоть этот оберег с моими молитвами…"),
66: ("Yeah, thanks. When the fight's over, I'll come straight back to return it.",
     "Да, спасибо. Когда всё кончится, я сразу приду его вернуть."),
67: ("Yes! You promised, didn't you?", "Да! Вы обещали, да?"),
68: ("Thanks, Siesta. With this, not even a bomb can hit me.",
     "Спасибо, Сиэста. С этим даже бомба в меня не попадёт."),
69: ("Even if it does, I'll pretend it didn't.", "А если попадёт — сделаю вид, что не попала."),
70: ("Honestly, Saito-san... Please don't do anything reckless...?",
     "Ох, Сайто-сан… Только не делайте глупостей, ладно…?"),
71: ("Yeah, I know.", "Да, знаю."),
72: ("Wearing this charm makes me feel stronger. I'll do my best.",
     "С этим оберегом я чувствую себя сильнее. Я постараюсь."),
73: ("Saito-san...", "Сайто-сан…"),
74: ("And also...", "И ещё…"),
75: ("What is it, Siesta?", "Что там, Сиэста?"),
76: ("Just one more thing... Um, could you... let me do a little charm? A special one.",
     "Ещё одно… Э-Э, можно вам… позволить мне маленькое заклинание? Особенное."),
77: ("A special one, huh? Sure, go ahead. What should I do?",
     "Особенное, значит? Конечно, делай. Что мне делать?"),
78: ("T-Then... Could you close your eyes for just a moment?",
     "Т-Тогда… Можете на мгновение закрыть глаза?"),
79: ("Close my eyes? Why?", "Закрыть глаза? Зачем?"),
80: ("W-Why... Well, um... It's embarrassing, that's...", "П-Почему… Ну, э-э… Это неловко, вот…"),
81: ("Embarrassed? I don't really get it, but...", "Неловко? Не понимаю, но…"),
82: ("Is this okay?", "Так хорошо?"),
83: ("Y-Yes.", "Д-Да."),
84: ("In... out... Okay, I'm ready. H-Here I go!", "Вдох… выдох… Ладно, я готова. Н-Ну же!"),
85: ("...Hah!?", "…Ах!?"),
86: ("Mm...", "Мм…"),
87: ("...!!", "…!!"),
88: ("...", "…"),
89: ("U-Um, I'm sorry... Doing something like this suddenly...",
     "Э-Э, простите… Так вдруг и такое…"),
90: ("B-But, that was a charm... a charm, you see...", "Н-Но это было заклинание… заклинание, понимаете…"),
91: ("Ah... Aah.", "Ах… А-а-а."),
92: ("That voice is Sylphid!?", "Этот голос — Сильфид!?"),
93: ("That's Miss Tabitha's...", "Это мисс Табасы…"),
94: ("There you are! We're taking Tabitha's Sylphid to the castle!",
     "Вот вы где! Мы летим в замок на Сильфиде Табасы!"),
95: ("Get on.", "Садись."),
96: ("Hah, hah, wait for us!!", "Ах, ах, подождите нас!!"),
97: ("Louise—are Kirche and Montmorency coming, too?", "Луиза — Кирке и Монморанси тоже идут?"),
98: ("No, they're not.", "Нет."),
99: ("This morning I was so distracted by the castle incident that I didn't notice—Haruna "
      "wasn't in her room, was she?", "Утром я так отвлеклась из-за беспокойства в замке, что не "
      "заметила — Харуны не было в комнате, да?"),
100: ("Eh, seriously?", "А, правда?"),
101: ("Y-Yes, seriously. Haruna vanished this morning.", "Д-Да, правда. Харуна исчезла утром."),
102: ("We've been looking, but there's no trace of her anywhere.",
     "Мы искали, но нигде нет и следа."),
103: ("A bomber came to the academy, too, so I worried something might have happened...",
     "В академию тоже пришёл бомбист, и я испугалась, что что-то случилось…"),
104: ("I asked Kirche and Montmorency to search for her.", "Я попросила Кирке и Монморанси её найти."),
105: ("Honestly, where could she have gone? Even magic can't find her...",
     "Право, куда она делась? Даже магия не находит…"),
106: ("Anyway, this is an emergency. Let's hurry to Tristain.",
     "В любом случае, это чрезвычайная ситуация. Спешим в Тристанию."),
107: ("Kirche, Montmorency—can I leave Haruna to you?", "Кирке, Монморанси — могу я вам поручить Харуну?"),
108: ("You think I'd refuse darling's request? We're in too deep to back out now. Right, Montmorency?",
     "Ты думаешь, я откажу дорогому? Мы уже слишком далеко зашли, чтобы отступать. Верно, Монморанси?"),
109: ("I suppose we must. I'll extend the range of my magic a little further.",
     "Видно, придётся. Я немного расширю радиус магии."),
110: ("Thanks. That helps.", "Спасибо. Выручаете."),
111: ("Saito-san.", "Сайто-сан."),
112: ("Siesta... It's fine. We'll definitely come back. Definitely!",
     "Сиэста… Всё хорошо. Мы обязательно вернёмся. Обязательно!"),
113: ("Yes!", "Да!"),
114: ("All right, let's go! Louise! Tabitha!", "Ладно, пошли! Луиза! Табаса!"),
115: ("Sylphid.", "Сильфид."),
116: ("Tristain. Hurry.", "Тристания. Быстрее."),
117: ("(Sylphid, carrying us, flapped her wings wider.)", "Сильфид, неся нас, взмахнула крыльями шире."),
118: ("Saito-san!!", "Сайто-сан!!"),
119: ("I'll be waiting for you! I'll definitely be waiting!", "Я буду ждать вас! Обязательно буду ждать!"),
120: ("We're here.", "Прибыли."),
121: ("Look! There's smoke! The capital is in chaos, too...",
     "Смотрите! Дым! В столице тоже беспорядок…"),
122: ("That bomber really went wild. The whole city's in confusion.",
     "Похоже, этот бомбист здорово разбушевался, да… Весь город в смятении."),
123: ("People are running away.", "Люди разбегаются."),
124: ("Right. It's less like they're afraid of the bomber, and more like they're fleeing "
      "from something...", "Верно. Скорее они не боятся бомбиста, а спасаются от чего-то…"),
125: ("What do you mean, something!", "Что значит — от чего-то!"),
126: ("An earthquake... or a war?", "Землетрясение… или война?"),
127: ("Let's go to the castle! I'm worried about the princess!", "Идём в замок! Я волнуюсь за принцессу!"),
}
CHOICES = {
849: [("Sorry, Louise", "Прости, Луиза"),
      ("I feel a bit sluggish", "Я сегодня вялый"),
      ("Hiraga Saito is out", "Хирага Сайто отсутствует")],
854: [("I'll definitely come back", "Я обязательно вернусь"),
      ("Fight to protect what matters", "Сражаться ради важного"),
      ("I can't run away", "Я не могу убежать")],
859: [("I'll return it first thing", "Я сразу верну его"),
      ("With this, I'm fine", "С этим я в порядке"),
      ("I feel stronger", "Я чувствую себя сильнее")],
}
SPK = {'サイト': 's', 'ルイズ': 'l', 'シエスタ': 'si', 'タバサ': 't',
       'モンモランシー': 'm', 'キュルケ': 'k', 'null': 'th'}
START = {'s': 0, 'l': 0, 'si': 0, 't': 0, 'm': 0, 'k': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch23/parse_849_893.json', encoding='utf-8'))
    script = ['# Глава 23, часть 1 (сцены 849–867): Zero Fighter разрушен, оберег Сиэсты.',
              '# Источник: ps2_source/chapters/chapter_24_沈黙の応援.txt (SCENE 849-867).',
              '', 'label ch23:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 867: break
            scene = x['no']
            script += ['label ch23_1_scene_%d:' % scene, '']
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
            tag = 'ch23_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch23_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch23_1_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 849 <= scene <= 867: continue
            if scene == 863 and x['target'] == 865:
                script.append('    # checkKiss(): ветка 864/865 — zero_kiss не портирован; идём по ветке zero_kiss (864), как в гл.12')
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch23_1_scene_%d' % x['target'] if 849 <= x['target'] <= 867 else 'ch23_2'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch23_2', '    return', '']
    files = {
        'game/chapters/23/script-ch23.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch23_1_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch23_1_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch23_1_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch23_1_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch23/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
