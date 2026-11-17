#!/usr/bin/env python3
"""Chapter 14 part 1 (scenes 578-598): Investigating Weatherly, ambush."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("So, how's the team-up with Kirche going?", "Так, как у тебя дела с командой Кирке?"),
1: ("Well, so-so, I guess.", "Ну, более-менее."),
2: ("Hm. Is that so.", "Хм. Вот как."),
3: ("H-How about you?", "А-А у тебя как?"),
4: ("I won't tell you. You're my enemy, Saito, aren't you?", "Не скажу. Ты же мой враг, Сайто?"),
5: ("I-Is that so.", "Т-Так вот как."),
6: ("(Why are you so angry...!)?", "Почему ты так злишься…!?"),
7: ("A-Anyway, we need to prepare for the night search...",
    "К-Короче, нам ещё готовиться к ночным поискам…"),
8: ("Really, you stupid dog.", "Ну же, глупый пёс."),
9: (None, None),
10: ("Yaaawn... Morning, Kirche.", "Фуаа… Доброе утро, Кирке."),
11: ("(Though it's night, actually...)", "Хотя на самом деле ещё ночь…"),
12: ("Fua... Morning, darling.", "Фуа… Доброе утро, дорогой."),
13: ("What's wrong, Kirche? You look sleepy.", "Что случилось, Кирке? Ты выглядишь сонной."),
14: ("I was reading documents about Weatherly.", "Я читала документы об Уэзерби."),
15: ("About Weatherly?", "Об Уэзерби?"),
16: ("I got them from a certain source... But...", "Их мне достали из одного источника… Но…"),
17: ("Maybe she's not just a rat.", "Может, она не просто крыса."),
18: ("Too much money for a mere traveling actress. And she meets with nobles often—"
     "and only ones with shady reputations.",
     "Слишком много средств для простой бродячей актрисы. И она часто встречается "
     "с дворянами — и только с теми, у кого дурная репутация."),
19: ("Not just a rat, you say?", "Не просто крыса, говоришь?"),
20: ("Maybe she's a bigger rat than the bomb-thrower.", "Может, она крыса покрупнее, чем бомбист."),
21: ("J-Just because she visits nobles with bad reputations...",
     "П-Просто потому, что она ходит к дворянам с плохой репутацией…"),
22: ("That doesn't mean she's doing something bad, does it?",
     "Это не значит, что она делает что-то плохое, правда?"),
23: ("I know you want to believe, but we should be wary of Weatherly. She's black as pitch.",
     "Я понимаю, тебе хочется верить, но Уэзерби нужно остерегаться. Она чёрным-черна."),
24: ("I know, but...", "Я знаю, но…"),
25: ("...Isn't it wrong to suspect her?", "…Нехорошо её подозревать, нет?"),
26: ("If investigating clears the suspicion, what's wrong with that? Or are you afraid of the truth?",
     "Если расследование снимет подозрения — что плохого? Или ты боишься правды?"),
27: ("T-That's not it, but...", "Я-Я не это имел в виду, но…"),
28: ("(The bomb-thrower incident. A traveling actress who might be a spy...)",
     "Дело бомбиста. Бродячая актриса, возможно шпион…"),
29: ("(What's about to happen in Tristain...?)", "Что же готовится в Тристании…?"),
30: ("Reconquista lost many of its prized aerial fleet in the last battle, right?",
     "Реконкиста потеряла много своих лучших воздушных кораблей в прошлом бою, верно?"),
31: ("Yeah, but?", "Да, но?"),
32: ("(Of course, the ones who sank them were me and Louise... but it's a secret.)",
     "Конечно, их потопили мы с Луизой… но это секрет."),
33: ("So Reconquista, now at a disadvantage, changed the form of the war, I think.",
     "Так что Реконкиста, оказавшись в невыгодном положении, изменила форму войны, я думаю."),
34: ("Changed the form of the war?", "Изменила форму войны?"),
35: ("They're shaking Tristain from within—sowing confusion with bombings, bribing nobles...",
     "Они расшатывают Тристанию изнутри — сеют хаос взрывами, подкупают дворян…"),
36: ("...", "…"),
37: ("I see. Indeed, with firecrackers going off under your feet, you can't chant a proper spell.",
     "Понятно. И правда, когда под ногами трещат петарды, нормальное заклинание не произнести."),
38: ("So that's it.", "Вот в чём дело."),
39: ("I think Her Majesty is wary of that too. I wonder how much she's figured out.",
     "Думаю, Её Величество тоже это беспокоит. Интересно, насколько она разобралась?"),
40: ("The Princess?", "Принцесса?"),
41: ("The Queen didn't join a troupe for fun, you know.",
     "Королева же не ради забавы присоединилась к труппе."),
42: ("So Weatherly is an agent sent by Reconquista?", "Значит, Уэзерби — агент, посланный Реконкистой?"),
43: ("Judging by the situation, that's how it looks.", "Судя по обстоятельствам, так и есть."),
44: ("Hey, isn't this all too convenient? This isn't a play.",
     "Эй, не слишком ли всё удобно сходится? Это не спектакль."),
45: ("True, it's too convenient. Especially that we were written into it. "
     "There's one more thing we're missing.",
     "Верно, слишком удобно. Особенно то, что нас вписали в это. Ещё что-то мы упускаем."),
46: ("Missing what?", "Упускаем что?"),
47: ("The Princess was just playing around, right? I wanted to spend time with Louise for once.",
     "Принцесса просто развлекалась, да? Я хотел немного побыть с Луизой."),
48: ("That joke isn't funny.", "Эта шутка не смешная."),
49: ("I-I see...", "Я-Я понял…"),
50: ("But if you know this much, why not talk to Louise?",
     "Но если ты столько знаешь, почему не поговоришь с Луизой?"),
51: ("There isn't enough evidence yet.", "Пока недостаточно доказательств."),
52: ("B-But!", "Н-Но!"),
53: ("It's Louise, isn't it? Tell her carelessly and she'll charge in and make a scene.",
     "Это же Луиза, правда? Скажешь ей неосторожно — и она бросится в бой и поднимет шум."),
54: ("Ugh... True...", "Ох… Верно…"),
55: ("Ufufu... Besides, the contest is still going, you know!",
     "Уф-фу… К тому же соревнование ещё продолжается!"),
56: ("...Eh? You're not putting the contest with Louise ahead of this, are you?",
     "…А? Неужто ты ставишь соревнование с Луизой выше этого?"),
57: ("Come on, darling! To the night streets again!", "Ну же, дорогой! Опять в ночный город!"),
58: ("W-Wait a second!", "П-Подожди!"),
59: ("Ohohoho!", "О-хо-хо!"),
60: ("W-What are you doing? Pressing against me... It's embarrassing!",
     "Ч-Что ты делаешь? Прижимаешься… Это неловко!"),
61: ("My, my, darling. Don't be shy.", "Ой, дорогой. Не стесняйся."),
62: ("It's a disguise, a disguise. If we don't act like lovers, they'll get suspicious, right?",
     "Это маскировка, маскировка. Если не будем изображать влюблённых, нас заподозрят, правда?"),
63: ("I-I see?", "Т-Так?"),
64: ("Ufufu, but being like this with just the two of us feels like a date.",
     "Уф-фу, но быть вот так вдвоём — как свидание."),
65: ("Ufufu, a date with darling. A date with darling.",
     "Уф-фу, свидание с дорогим. Свидание с дорогим."),
66: ("(Whoa, Kirche's body is against my arm... Why am I surrounded by girls ever since "
     "I came to this world...?)",
     "Ого, Кирке прижалась к моей руке… Почему с тех пор, как я попал в этот мир, "
     "меня всё время осаждают девушки…"),
67: ("(Is this my popular phase...?)", "Это что, моя пора популярности…?"),
68: ("That's ridiculous! You stupid dog!!", "Не может быть! Глупый пёс!!"),
69: ("...!", "…!"),
70: ("What's wrong, darling?", "Что случилось, дорогой?"),
71: ("No, it's just... a chill.", "Нет, просто… озноб."),
72: ("Oh, then... shall I warm you up?", "О, тогда… согреть тебя?"),
73: ("Eh! That's a bit... dangerous!", "Э! Это как-то… опасно!"),
74: ("Ufufu... A red-faced darling is cute too! I don't want to let go!",
     "Уф-фу… Покрасневший дорогой тоже милый! Не хочу отпускать!"),
75: ("Please. Let go of me.", "Прошу. Отпусти меня."),
76: ("Come on, darling. Let's find Weatherly!", "Ну же, дорогой. Идём искать Уэзерби!"),
77: ("Please. Listen to people.", "Прошу. Послушай меня."),
82: ("...", "…"),
83: ("There! It's Weatherly-san!", "Вот! Уэзерби-сан!"),
84: ("Darling, quiet. Let's watch for a bit.", "Дорогой, тише. Посмотрим немного."),
85: ("...", "…"),
86: ("What's she doing? Ah, she's moving.", "Что она делает? А, она идёт."),
87: ("Let's follow!", "Идём за ней!"),
88: (None, None),
89: ("Kirche. Are you walking rather slowly today?", "Кирке. Ты сегодня идёшь очень медленно, нет?"),
90: ("Ah, partner. It's almost like she's deliberately leading us on...",
     "Ах, приятель. Будто она намеренно нас ведёт…"),
91: ("Eh?", "А?"),
92: ("What!?", "Что!?"),
93: ("...", "…"),
94: ("Damn, we're surrounded?", "Чёрт, нас окружили?"),
95: ("So they knew from the start.", "Значит, они знали с самого начала."),
96: ("Come out, Weatherly! You're here, aren't you?!", "Выходи, Уэзерби! Ты здесь, да?!"),
97: ("...", "…"),
98: ("My my. What does the leading pair want with this troupe leader?",
     "Ой-ой. Что нужно главным героям от этого главаря труппы?"),
99: ("Weatherly-san!", "Уэзерби-сан!"),
100: ("And what are you plotting, Weatherly, with such suspicious mages in tow?",
     "А что ты задумала, Уэзерби, с такими подозрительными магами?"),
101: ("Why, nothing at all.", "Ну же, ничего."),
102: ("Though even if I were plotting something...", "Впрочем, даже если бы я что-то задумала…"),
103: ("...you'd never learn what it is.", "…вы никогда не узнаете, что именно."),
104: ("Because you two will be disposed of right here.", "Потому что вас двоих здесь и уберут."),
105: ("All right! Next is you, Weatherly!", "Отлично! Теперь твоя очередь, Уэзерби!"),
106: ("Unfortunately, I'm not short on extras.", "К сожалению, у меня нет недостатка в статистах."),
107: ("...", "…"),
108: ("Darling! New ones!", "Дорогой! Новые!"),
109: ("...", "…"),
110: ("Damn, so many of them. It's endless!", "Чёрт, их столько. Конца нет!"),
111: ("True. We have to call Louise and the others.", "Верно. Нужно позвать Луизу и остальных."),
112: ("I know, but how!?", "Я знаю, но как!?"),
113: ("I'll evaporate the river water to make fog. In the confusion, let's split in two.",
     "Я испарю воду из реки и сделаю туман. В суматохе разделимся."),
114: ("I'll draw the enemy and run. Meanwhile, get Louise and the others.",
     "Я отвлеку врагов и убегу. А ты за это время позови Луизу и остальных."),
115: ("You can do that!?", "Ты такое можешь!?"),
116: ("I don't say what I can't do. I'm Kirche with a slight fever, after all.",
     "Я не говорю о том, чего не могу. Я же Кирке с лёгким жаром."),
117: ("Got it. Then I'll go get Louise...", "Понял. Тогда я пойду к Луизе…"),
118: ("Be careful, darling. Once you link up with Louise and the others, counterattack at once.",
     "Осторожно, дорогой. Как только соединишься с Луизой и остальными — сразу контратакуйте."),
119: ("Of course. You be careful too, Kirche!", "Конечно. И ты осторожнее, Кирке!"),
120: ("Kirche, drawing them all on alone? That's too dangerous.",
     "Кирке, одной отвлечь всех? Это слишком опасно."),
121: ("Ufufu, who do you think I am?", "Уф-фу, ты кто, по-твоему, я?"),
122: ("...", "…"),
123: ("Darling, please. Just listen to me for now.", "Дорогой, прошу. Пока просто послушайся меня."),
124: ("It's fine. Once you join Louise and the others, counterattack right away.",
     "Всё хорошо. Как только соединишься с Луизой и остальными — сразу контратакуйте."),
125: ("Got it. You be careful too, Kirche.", "Понял. И ты осторожнее, Кирке."),
126: ("With a slight fever, you can't evaporate water.", "С лёгким жаром воду не испарить."),
127: ("Really, darling. Don't fuss over details. I don't say what I can't do.",
     "Ну же, дорогой. Не цепляйся к мелочам. Я не говорю о том, чего не могу."),
128: ("Darling, please. Just listen to me for now.", "Дорогой, прошу. Пока просто послушайся меня."),
129: ("It's fine. Once you join Louise and the others, counterattack right away.",
     "Всё хорошо. Как только соединишься с Луизой и остальными — сразу контратакуйте."),
130: ("Got it. You be careful too, Kirche.", "Понял. И ты осторожнее, Кирке."),
131: ("It's fine, darling. It'll work.", "Всё хорошо, дорогой. Всё получится."),
132: ("I'll show you what the true magic of 'fire' is—Kirche with a slight fever!",
     "Я покажу тебе, что такое настоящая магия «огня», — Кирке с лёгким жаром!"),
133: ("Tch! What is this! This steam!", "Тьфу! Что это! Этот пар!"),
134: ("Fool! Calm down!", "Глупец! Успокойся!"),
135: ("Darling, now!!", "Дорогой, сейчас!!"),
136: ("Got it!", "Понял!"),
}
CHOICES = {
578: [("Not just a rat, you say?", "Не просто крыса?"),
      ("It's not like she's doing anything wrong...", "Она же ничего плохого не делает…"),
      ("Isn't it wrong to suspect her?", "Нехорошо её подозревать?")],
583: [("Weatherly is an agent, then?", "Значит, Уэзерби — агент?"),
      ("Too much of a coincidence, isn't it?", "Слишком всё сходится, не правда ли?"),
      ("The Princess was just playing, right?", "Принцесса просто играла, да?")],
594: [("Got it", "Понял"),
      ("Let's run together", "Убежим вместе"),
      ("You can't evaporate with a slight fever", "С лёгким жаром ты не испаришь")],
}
MOVES = [("In front of the castle", "Перед замком", "城前"),
         ("The main street", "Главная улица", "表通り"),
         ("The back alley", "Задний переулок", "裏通り"),
         ("The street", "Улица", "街道")]
SPK = {'ルイズ': 'l', 'サイト': 's', 'キュルケ': 'k', 'null': 'th',
       'デルフリンガー': 'd', 'ウェザリー': 'w', '魔導士': 'mage'}
START = {k: 0 for k in SPK.values()}


def main():
    data = json.load(open('reports/ch14/parse_578_619.json', encoding='utf-8'))
    script = ['# Глава 14, часть 1 (сцены 578–598): «私のお兄ちゃん» — слежка за Уэзерби, засада.',
              '# Источник: ps2_source/chapters/chapter_15_私のお兄ちゃん.txt (SCENE 578-598).',
              '', 'label ch14:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 598:
                break
            scene = x['no']
            script += ['label ch14_1_scene_%d:' % scene, '']
            continue
        if k == 'event':
            event(x['src'], script)
            continue
        if k == 'dlg':
            idx = x['idx']
            if 78 <= idx <= 81:
                continue
            if 589 <= (scene or 0) <= 592:
                continue
            en, ru = T[idx]
            if en is None:
                script.append('    # ' + x['src'] + ' (no voice)')
                continue
            en = en_norm(en)
            spk = SPK.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch14_%s_%03d' % (spk, counters[spk])
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
            if idx == 77:
                script.append('    # 【移動】 → extra 1485/1486/1487/1488')
                script.append('    menu:')
                for i, (en_m, ru_m, ja_m) in enumerate(MOVES):
                    ctext = '%s{#ch14_1_c_588_%d}' % (en_norm(en_m), i + 1)
                    script.append('        "%s":' % ctext)
                    script.append('            jump ch14_2_scene_%d' %
                                  (1485, 1486, 1487, 1488)[i])
                    ja_c += ['    old "%s"' % ctext, '    new "%s"' % ja_m, '']
                    ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru_m, '']
                script.append('')
            continue
        if k == 'choice':
            script.append('    menu:')
            for i, o in enumerate(x['options']):
                en, ru = CHOICES[scene][i]
                ctext = '%s{#ch14_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                tgt = ('ch14_1_scene_%d' % o['target']
                       if 578 <= o['target'] <= 598 else 'ch14_2')
                script.append('        "%s":' % ctext)
                script.append('            jump %s' % tgt)
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene and 589 <= scene <= 592:
                continue
            tgt = ('ch14_1_scene_%d' % x['target']
                   if 578 <= x['target'] <= 598 else 'ch14_2')
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % tgt)
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch14_2', '    return', '']
    files = {
        'game/chapters/14/script-ch14_1.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch14_1_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch14_1_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch14_1_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch14_1_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch14/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
