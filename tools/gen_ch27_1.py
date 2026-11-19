#!/usr/bin/env python3
"""Chapter 27 part 1 (scenes 972-984): Reconquista fleet, Void permission debate."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("A-ha-ha-ha-ha! Burn, break, crumble away!", "А-ха-ха-ха-ха! Гори, ломайся, рушься!"),
1: ("Ahh ha ha ha ha!", "А-а-а-ха-ха-ха!"),
2: ("Good morning... Are you awake?", "Доброе утро… Ты проснулась?"),
3: ("...", "…"),
4: ("Good morning, Miss Zerbst, Miss Tabitha, Miss Montmorency.",
     "Доброе утро, мисс Церпст, мисс Табаса, мисс Монморанси."),
5: ("Oh, you're up early today, aren't you?", "Ох, ты сегодня рано встала, да?"),
6: ("Well, I can't sleep with this tension continuing...", "Ну, я не могу спать при таком напряжении…"),
7: ("And the street fighting seems to be continuing, too...", "И уличные бои, кажется, продолжаются…"),
8: ("I wonder if the flames of war will reach here, too...", "Интересно, дойдёт ли сюда пламя войны…"),
9: ("Haa...", "Хаа…"),
10: ("Why the sigh, darling?", "Почему вздыхаешь, дорогой?"),
11: ("It's complicated—the bomber turned out to be Haruna.", "Это сложно — бомбистом оказалась Харуна."),
12: ("No. The bomber is the separate personality Akina, planted by Weatherly. Haruna has nothing to do with it.",
     "Нет. Бомбист — это отдельная личность Акина, вселённая Уэзерби. Харуна тут ни при чём."),
13: ("But it's Haruna who'll be captured. Personality doesn't matter.",
     "Но захватят Харуну. Личность тут не важна."),
14: ("So you're saying we shouldn't catch her? That would make her happy?",
     "То есть ты говоришь, что не надо её ловить? И это сделает её счастливее?"),
15: ("I'm not saying that. At this rate, the Tristain kingdom will be taken by storm.",
     "Я не это говорю. Так Тристания будет взята штурмом."),
16: ("There has to be a mastermind. Weatherly alone couldn't do something this audacious.",
     "Должен быть заказчик. Одна Уэзерби не смогла бы на такое."),
17: ("If only we could at least find that mastermind...", "Хоть бы найти этого заказчика…"),
18: ("...", "…"),
19: ("It's terrible, you guys.", "Это ужасно, вы все."),
20: ("What's wrong, Guiche?", "Что случилось, Гиш?"),
21: ("The Reconquista air fleet seems to be heading for Tristain.",
     "Воздушный флот Реконкисты, кажется, идёт к Тристании."),
22: ("The Reconquista air fleet!?", "Воздушный флот Реконкисты!?"),
23: ("W-Wait. In the last war, their fleet took serious damage.", "П-Погоди. В прошлой войне их флот сильно пострадал."),
24: ("I don't know. It's not certain information, but there's also a report that a fleet in the Tristain army defected.",
     "Не знаю. Данные неточные, но есть слух, что флот из армии Тристании перешёл на их сторону."),
25: ("Coming at this timing means...", "Появиться в такой момент значит…"),
26: ("Support for Tristain, maybe?", "Может, они идут на помощь Тристании?"),
27: ("Like, regretting the last war and helping us this time... or something?",
     "Типа, раскаиваются за прошлую войну и теперь помогут… или что-то в этом роде?"),
28: ("...That's naive. Reconquista would never do such a thing.", "…Это наивно. Реконкиста никогда бы такого не сделала."),
29: ("So they intend to attack amid Tristain's chaos.", "Значит, они хотят напасть в хаосе Тристании."),
30: ("Hmm, that's probably it, I suppose.", "Хм, наверное, так и есть."),
31: ("We can't rule out the theory that Reconquista is the mastermind, either.",
     "Нельзя исключить и версию, что заказчик — Реконкиста."),
32: ("When they attacked before, they lost spectacularly and made fools of themselves in front of neighboring countries. "
     "I'm sure they haven't forgotten that grudge.", "Когда они нападали раньше, они позорно проиграли перед "
     "соседними странами. Наверное, они не забыли ту обиду."),
33: ("...", "…"),
34: ("...", "…"),
35: ("What's wrong? You two went quiet all of a sudden.", "Что случилось? Вы двое вдруг замолчали."),
36: ("Eh? What do you mean? It's nothing, nothing...", "А? О чём вы? Просто совпадение, совпадение…"),
37: ("N-No, it's nothing...", "Н-Нет, ничего…"),
38: ("(There's no way I can tell them we were the ones who drove them off...)",
     "Я не могу им сказать, что это мы их отогнали…"),
39: ("Could the mastermind be Reconquista?", "Может, заказчик — Реконкиста?"),
40: ("But at this point, can we really prove that the street-fighting enemy is connected to Reconquista?",
     "Но сейчас мы же не можем доказать, что враг в городе связан с Реконкистой, правда?"),
41: ("Even if they were, they wouldn't admit it now, would they?", "Даже если бы были, сейчас бы не признали, да?"),
42: ("But one thing is clear...", "Но одно ясно…"),
43: ("Clear what?", "Что именно?"),
44: ("Reconquista hasn't forgotten the grudge from when they tried to attack Tristain and failed.",
     "Реконкиста не забыла обиду за попытку напасть на Тристанию и провал."),
45: ("Haa...", "Хаа…"),
46: ("(Somehow, it feels like Louise and I are the ones responsible...)",
     "Как-то получается, что виноваты мы с Луизой…"),
47: ("I mean—once the air fleet arrives, it's a full-scale war.", "Я хочу сказать — с приходом флота начнётся настоящая война."),
48: ("Right. If only we could stop the street fighting... We'd have a bit more of an advantage, but...",
     "Верно. Если бы остановить уличные бои… Мы бы получили небольшое преимущество, но…"),
49: ("In that sense, the timing is too good.", "В этом смысле момент слишком удачный."),
50: ("I'm going...", "Я иду…"),
51: ("What's wrong, Tabitha?", "Что случилось, Табаса?"),
52: ("I'll fight again.", "Я снова сражусь."),
53: ("Fight again—you don't mean...?", "Снова сражусь — ты не хочешь сказать…?"),
54: ("With Akina.", "С Акиной."),
55: ("Are you serious? Your wounds may have healed, but you're not fully recovered yet, are you?",
     "Ты серьёзно? Раны зажили, но ты ещё не полностью восстановилась, да?"),
56: ("But... Someone has to stop Akina.", "Но… Кто-то должен остановить Акину."),
57: ("True—unless we stop Akina, winning this war will be difficult. But still...",
     "Верно — пока мы не остановим Акину, выиграть эту войну будет трудно. Но всё же…"),
58: ("All right. I'll help Tabitha, too!", "Ладно. Я тоже помогу Табасе!"),
59: ("Kirche!", "Кирке!"),
60: ("Of course, so will I. We can't let Tabitha fight alone.", "Конечно, и я. Нельзя позволять Табасе сражаться одной."),
61: ("Even you!?", "Даже ты!?"),
62: ("What's that, Saito? Don't tell me you think that, because the bomber is using Haruna's body, "
      "she can't be fought!?", "Что это, Сайто? Неужто ты думаешь, что раз бомбист использует тело Харуны, "
      "с ней нельзя сражаться!?"),
63: ("...", "…"),
64: ("I think it's better to leave it to Tabitha.", "Я думаю, лучше поручить это Табасе."),
65: ("Meaning... You're saying we'd be a burden to Tabitha?", "То есть… Ты хочешь сказать, что мы обуза для Табасы?"),
66: ("That's not it, but... Tabitha got burned because I was there with her, in a way...",
     "Не совсем, но… Табаса обожглась отчасти потому, что я был рядом…"),
67: ("...", "…"),
68: ("When you put it that way, I can't help thinking about it...", "Когда ты так говоришь, я не могу не задуматься…"),
69: ("Oh, I'll be fine. I could never be a burden.", "О, я буду в порядке. Я никогда не стану обузой."),
70: ("As expected of Kirche. Quite the confidence...", "Как и подобает Кирке. Уверенности не занимать…"),
71: ("Nn fu fu, don't praise me so much, darling.", "Н-фу-фу, не хвали меня так, дорогой."),
72: ("T-Then I'll be fine, too!", "Т-Тогда и я буду в порядке!"),
73: ("Ha ha ha...", "Ха-ха-ха…"),
74: ("(Why compete over that...?)", "Зачем соревноваться в этом…?"),
75: ("I'm worried about what happens after Akina is defeated.", "Я волнуюсь о том, что будет после победы над Акиной."),
76: ("That Tabitha might hand Haruna over to Gallia.", "Что Табаса может передать Харуну Галлии."),
77: ("Haven't you talked it over with Tabitha?", "Разве ты не поговорил об этом с Табасой?"),
78: ("I have. I don't want to hand Haruna over—but considering Tabitha's position...",
     "Говорил. Я не хочу отдавать Харуну — но, учитывая положение Табасы…"),
79: ("It's a difficult problem...", "Это сложный вопрос…"),
80: ("I'm worried about everyone.", "Я волнуюсь за всех."),
81: ("If it were Louise, I'd understand—but I'm not so immature that darling needs to worry about me.",
     "Если бы это была Луиза — понимаю. Но я не настолько незрелая, чтобы дорогой волновался за меня."),
82: ("...", "…"),
83: ("Oh, you're not angry?", "О, ты не сердишься?"),
84: ("Not getting angry at slander that isn't true—that's what makes a true lady.",
     "Не сердиться на несправедливую клевету — вот что делает настоящую леди."),
85: ("Louise... Why are you so full of confidence?", "Луиза… Почему ты так полна уверенности?"),
86: ("Anyway—Kirche and I won't be a burden to Tabitha!", "В любом случае — я и Кирке не станем обузой для Табасы!"),
87: ("Akina isn't Haruna. That's exactly why Tabitha got badly burned shielding me...",
     "Акина — не Харуна. Именно поэтому Табаса сильно обожглась, прикрыв меня…"),
88: ("Then, if something happens to you, I suppose I'll just let you die and watch.",
     "Тогда, если с тобой что-то случится, я просто брошу тебя и не помогу."),
89: ("I believe in striking first. I won't give them a chance to do anything cowardly.",
     "Я верю в упреждающий удар. Я не дам врагу шанса на подлость."),
90: ("Ha ha ha... Then, we're fine.", "Ха-ха-ха… Тогда всё хорошо."),
91: ("...", "…"),
92: ("So, you're going after all?", "Так, ты и правда идёшь?"),
93: ("I'm going.", "Иду."),
94: ("All right. I'm going, too.", "Ладно. Я тоже иду."),
95: ("But—about Akina. No, about Haruna. Please at least hold off on handing her over to Gallia.",
     "Но — про Акину. Нет, про Харуну. Прошу хотя бы повременить с передачей её Галлии."),
96: ("I'll think about it.", "Подумаю."),
97: ("Thank you, Tabitha.", "Спасибо, Табаса."),
98: ("...", "…"),
99: ("Well then, let's go, Saito.", "Ну что ж, идём, Сайто."),
100: ("Go where?", "Куда идём?"),
101: ("Obviously—to the castle. We need the princess's permission.", "Очевидно — в замок. Нужно разрешение принцессы."),
102: ("So, Louise. What are you going to the princess for?", "Так, Луиза. Зачем ты идёшь к принцессе?"),
103: ("I'm uneasy about that confident look on my mistress's face...", "Мне тревожен этот уверенный вид моей госпожи…"),
104: ("Oh—I'm going to ask permission to use Void magic.", "Ох — я иду просить разрешения применить Пустоту."),
105: ("Void magic!? You intend to destroy the capital!?", "Пустота!? Ты собралась разрушить столицу!?"),
106: ("Hah? What are you talking about?", "А? Что ты несёшь?"),
107: ("What do you mean, what—you'll use Void on the air fleet, like last time, right?",
     "Что значит что — ты пустишь Пустоту в воздушный флот, как в прошлый раз, да?"),
108: ("Hmm... It's not exactly that.", "Хм… Не совсем так."),
109: ("It's not?", "Не так?"),
110: ("Well... A different method.", "Ну… Другой способ."),
111: ("Ah!? We're at the princess's room already. You'd better mind your manners!",
     "А!? Мы уже у комнаты принцессы. Ты должен вести себя прилично!"),
112: ("A-Ah...", "А-Ах…"),
113: ("Don't answer absentmindedly.", "Не отвечай рассеянно."),
114: ("(Even so—if I used Void magic here, the damage would be incredible...)",
     "Даже так — если бы я здесь применил Пустоту, ущерб был бы невероятным…"),
115: ("Princess, I'm sorry to drop in so often. Today I've come with a request.",
     "Принцесса, простите за частые визиты. Сегодня я пришла с просьбой."),
116: ("It's fine, Louise Francoise. Don't be so formal.", "Всё хорошо, Луиза Франсуаза. Не будь такой церемонной."),
117: ("In a situation like this, sticking to etiquette only makes the damage grow.",
     "В такой ситуации соблюдение этикета лишь увеличивает ущерб."),
118: ("Actually... I'd like permission to use Void magic in the capital.",
     "Дело в том… Я хочу просить разрешения применить Пустоту в столице."),
119: ("So, that's... Could you reconsider, mistress?", "Так, это… Может, передумаешь, госпожа?"),
120: ("No.", "Нет."),
121: ("Void magic, you say...", "Пустота, говоришь…"),
122: ("Yes, Princess.", "Да, принцесса."),
123: ("...", "…"),
124: ("Princess, tell me it's no. Using Void on the capital is madness...",
     "Принцесса, скажите, что нельзя. Применять Пустоту против столицы — безумие…"),
125: ("I see...", "Понятно…"),
126: ("Louise! You can't do something like that!!", "Луиза! Ты не можешь такое делать!!"),
127: ("Saito! You be quiet!!", "Сайто! Ты помалкивай!!"),
128: ("Even if you say that—!!", "Даже если ты так говоришь —!!"),
129: ("Well... Darling familiar, are you against using Void magic?", "Ну… Фамильяр, ты против применения Пустоты?"),
130: ("T-That is...", "Т-Это…"),
131: ("I'm against it! Absolutely against it!!", "Я против! Абсолютно против!!"),
132: ("Wh-Why would you say that! You—!!", "П-Почему ты такое говоришь! Ты —!!"),
133: ("Of course it's obvious! Do you have any idea how powerful your Void magic is!?",
     "Это само собой! Ты хоть понимаешь, насколько сильна твоя Пустота!?"),
134: ("I aimed at a single battleship, but it burned the whole fleet!!",
     "Ты целилась в один боевой корабль, а сгорел весь флот!!"),
135: ("I know... I was the one who cast it, after all...", "Я знаю… Я же сама её применила…"),
136: ("You don't understand at all! If you use magic that powerful here, the whole capital could vanish!!",
     "Ты ничего не понимаешь! Если применить здесь такую магию, столица может исчезнуть!!"),
137: ("Now, now. Louise has her own reasons. Why not trust her?",
     "Ну-ну. У Луизы есть свои причины. Почему бы ей не доверять?"),
138: ("Well, if the princess says so... But still...", "Ну, если принцесса так говорит… Но всё же…"),
139: ("If the princess gives permission, then I suppose...", "Если принцесса разрешит, то, думаю…"),
140: ("But you're really against it, aren't you? You're making that face.",
     "Но ты и правда против, да? У тебя такой вид."),
141: ("Of course I am! Are you taking that magic lightly?", "Конечно! Ты что, недооцениваешь эту магию?"),
142: ("I'm not taking it lightly.", "Я не недооцениваю."),
143: ("Is that so?", "Правда?"),
144: ("Now, now, familiar. Louise has her own reasons for asking.", "Ну-ну, фамильяр. У Луизы свои причины для просьбы."),
145: ("And Louise is more thoughtful than you think.", "И Луиза более рассудительна, чем ты думаешь."),
146: ("I don't know how many times she's saved me because of that...", "Я не знаю, сколько раз она спасала меня благодаря этому…"),
147: ("I'm telling you—the problem is WHERE it's used!", "Я говорю — проблема в ТОМ, ГДЕ её применят!"),
148: ("What's the problem?", "Что за проблема?"),
149: ("Are you serious? Using it in the capital is problematic any way you look at it!",
     "Ты серьёзно? Применять её в столице — проблема при любом раскладе!"),
150: ("Do you intend to erase the Tristain capital?", "Ты собралась стереть столицу Тристании?"),
151: ("What are you talking about, Saito? I have no intention of erasing the princess's capital!",
     "Что ты несёшь, Сайто? Я и не думала стирать столицу принцессы!"),
152: ("Then you clearly don't understand Void magic's power at all.", "Тогда ты явно не понимаешь силу Пустоты."),
153: ("What was that!?", "Что ты сказал!?"),
154: ("Now, now. Louise has her own reasons. Why not trust her?", "Ну-ну. У Луизы есть свои причины. Почему бы ей не доверять?"),
155: ("Well, if the princess says so... But still...", "Ну, если принцесса так говорит… Но всё же…"),
}
CHOICES = {
972: [("Support for Tristain?", "Помощь Тристании?"),
      ("Taking advantage of chaos?", "Использование хаоса?"),
      ("Is Reconquista the mastermind?", "Заказчик — Реконкиста?")],
976: [("Better to leave it to Tabitha", "Лучше поручить Табасе"),
      ("Worried about after the fight", "Беспокоит то, что будет после"),
      ("Worried about everyone", "Беспокоит всех")],
981: [("I'm against it!", "Я категорически против!"),
      ("If the princess allows...", "Если принцесса разрешит…"),
      ("The place is the problem", "Проблема в месте")],
}
SPK = {'アキナ': 'ak', 'キュルケ': 'k', 'タバサ': 't', 'シエスタ': 'si',
       'ルイズ': 'l', 'モンモランシー': 'm', 'サイト': 's', 'ギーシュ': 'g',
       'アンリエッタ': 'h', 'null': 'th'}
START = {'ak': 0, 'k': 0, 't': 0, 'si': 0, 'l': 0, 'm': 0, 's': 0, 'g': 0, 'h': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch27/parse_972_998.json', encoding='utf-8'))
    script = ['# Глава 27, часть 1 (сцены 972–984): флот Реконкисты, спор о Пустоте.',
              '# Источник: ps2_source/chapters/chapter_28_ハルナの秘密.txt (SCENE 972-984).',
              '', 'label ch27:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 984: break
            scene = x['no']
            script += ['label ch27_1_scene_%d:' % scene, '']
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
            tag = 'ch27_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch27_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch27_1_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 972 <= scene <= 984: continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch27_1_scene_%d' % x['target'] if 972 <= x['target'] <= 984 else 'ch27_2'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch27_2', '    return', '']
    files = {
        'game/chapters/27/script-ch27.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch27_1_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch27_1_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch27_1_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch27_1_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch27/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
