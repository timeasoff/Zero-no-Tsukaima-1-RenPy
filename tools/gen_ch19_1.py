#!/usr/bin/env python3
"""Chapter 19 part 1 (scenes 739-749): operation morning, tunnels, freed friends."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("(The morning of the operation has finally arrived.)", "Наконец наступило утро дня операции."),
1: ("Well, let's go over the situation.", "Итак, подведём итоги обстановки."),
2: ("Our final objective: Miss Valliere uses Void magic to eliminate the enemy...",
    "Наша главная цель: мисс Вальер применяет магию Пустоты и уничтожает врагов…"),
3: ("Are we agreed so far?", "До сюда всё понятно?"),
4: ("Yes.", "Да."),
5: ("No mistakes.", "Ошибок нет."),
6: ("There should be many enemy soldiers inside the academy. And their commander "
    "Weatherly uses a special hypnosis magic.",
    "В академии должно быть много вражеских солдат. И их командующая Уэзерби "
    "применяет особую магию гипноза."),
7: ("There's a great risk that even the students and teachers here will become your enemies.",
    "Велика вероятность, что даже здешние ученики и преподаватели станут вашими врагами."),
8: ("Be careful of that.", "Будьте осторожны."),
9: ("Yes.", "Да."),
10: ("Now, Miss Valliere.", "Теперь, мисс Вальер."),
11: ("Yes.", "Да."),
12: ("This Void magic you'll use—what kind of magic is it, exactly?",
     "Эта магия Пустоты, которую вы примените, — что это за магия?"),
13: ("...", "…"),
14: ("I'm a teacher at the academy, after all. Even a hint of what magic you'll use "
     "could help me advise you.",
     "Я всё же преподаватель академии. Даже намёк на то, какую магию вы примените, "
     "помог бы мне дать совет."),
15: ("It's something aimed at the sky where the ship occupying the academy is.",
     "Это то, что направлено в небо, где находится корабль, захвативший академию."),
16: ("The range... the wider the better, I suppose.", "Радиус… чем шире, тем лучше, наверное."),
17: ("Hmm, a wide-area spell. And aimed at the sky, eh.", "Хм, магия широкого радиуса. И в небо, значит."),
18: ("Sorry, Mr. Colbert. I can't explain it in detail myself.",
     "Простите, Кольбер-сэн. Я и сама не могу объяснить подробно."),
19: ("No, no, I understand. I won't press you.", "Нет-нет, понял. Не буду настаивать."),
20: ("In that case, I'll have to give you advice that's rather unfavorable to you.",
     "В таком случае мне придётся дать вам совет, который вам невыгоден."),
21: ("W-What do you mean, professor?", "Ч-Что вы имеете в виду, сэнсэй?"),
22: ("If Miss Valliere casts a spell at the sky, the best place is the academy rooftop.",
     "Если мисс Вальер наложит заклинание на небо, лучшее место — крыша академии."),
23: ("But if we're to stop Weatherly and Akina's bombing... we should settle the fight "
     "in the headmaster's office where they're barricaded.",
     "Но если мы хотим помешать взрывам Уэзерби и Акины… бой следует решить "
     "в кабинете директора, где они заперлись."),
24: ("Before using Void, there's a risk the academy will be blown up. "
     "We need to draw their attention too.",
     "Пока мы не применили Пустоту, академию могут взорвать. "
     "Нужно тоже отвлечь их внимание."),
25: ("Ugh... True.", "Ох… Верно."),
26: ("Saito and I have to act separately no matter what, don't we.",
     "Мы с Сайто в любом случае должны действовать раздельно, да?"),
27: ("It's a cruel thing to say, but there's no other way to make the plan work.",
     "Жестко, но другого пути к успеху операции нет."),
28: ("Yes. There's no other way, so we'll do our best.", "Да. Другого выхода нет, сделаем всё возможное."),
29: ("If we can link up with Kirche and Tabitha, somehow...",
     "Если получится соединиться с Кирке и Табасой, как-нибудь…"),
30: ("Indeed. We can only pray Miss Zerbst and Miss Tabitha haven't fallen into enemy hands.",
     "Верно. Остаётся лишь молиться, чтобы мисс Церпст и мисс Табаса не попали в руки врага."),
31: ("If you two make a commotion, they'll surely try to join you.",
     "Если вы двое поднимете шум, они наверняка попытаются к вам присоединиться."),
32: ("Which should we do first...?", "Что же делать сперва…?"),
33: ("Saito-kun, I'm afraid the idea of doing one first doesn't really apply here.",
     "Сайто-кун, боюсь, здесь нельзя делать сначала одно, а потом другое."),
34: ("So Saito and I need to split up, is that it?", "Значит, нам с Сайто нужно разделиться, да?"),
35: ("Ah... It's a plan full of holes, but even so, we have no choice but to do it.",
     "Ах… План полный дыр, но даже так нам нечего делать, кроме как идти."),
36: ("It's fine. We have the blessing of the First Founder Brimir.",
     "Всё хорошо. У нас благословение Первого Основателя Бримира."),
37: ("Yes. I can't help but feel uneasy sending you two on such a plan.",
     "Да. Я не могу не беспокоиться, отправляя вас с таким планом."),
38: ("All I can do now is believe in you and leave it to you.",
     "Теперь я могу только верить в вас и довериться вам."),
39: ("Right, now that we've confirmed the plan—this map for you two.",
     "Итак, раз план согласован — вот карта для вас."),
40: ("There are two... One is a map of the academy, but this one...",
     "Их две… Одна — план академии, а эта…"),
41: ("It's the map of the underground passage you came through from the courtyard.",
     "Это карта подземного хода, по которому вы пришли со двора."),
42: ("The exit leading to the shortest route to the rooftop is here.",
     "Выход к самому короткому пути на крышу — здесь."),
43: ("So Saito and I split up here? Ah, but at this distance it's practically just around the corner.",
     "Значит, мы с Сайто здесь расстанемся? А, но на этом расстоянии это буквально рукой подать."),
44: ("The wind is at our backs. Oh, there's one more thing I should give you.",
     "Ветер в нашу пользу. Ах, ещё кое-что я должен вам передать."),
45: ("Ah, this is...", "А, это…"),
46: ("Yes, the earplugs I showed you yesterday. I gave you a rough explanation then, I think.",
     "Да, беруши, которые я вам показывал вчера. Тогда я вкратце объяснил, кажется."),
47: ("The most troublesome enemy is Weatherly's hypnosis magic.",
     "Самый неприятный враг — гипноз Уэзерби."),
48: ("But with these, you'll be fine.", "Но с ними всё будет хорошо."),
49: ("Even if you fight someone under hypnosis, putting these on should "
     "temporarily restore their senses.",
     "Даже если придётся сражаться с тем, кто под гипнозом, эти беруши "
     "временно вернут ему рассудок."),
50: ("Understood.", "Понятно."),
51: ("Now go. Once I've confirmed you're outside, I'll make a little commotion "
     "outside myself.",
     "Ну же, идём. Как только я убежусь, что вы снаружи, я сам устрою "
     "небольшой переполох."),
52: ("Ugh, why is this passage so dark and narrow! And it smells like mold!!",
     "Ох, почему этот ход такой тёмный и узкий! И ещё пахнет плесенью!!"),
53: ("What do you expect—it's a sewer. Instead of screaming, let's move.",
     "Чего ты хочешь — это канализация. Вместо того чтобы визжать, идём дальше."),
54: ("I'll take this grudge out on Weatherly and Akina a hundredfold!",
     "Я отомщу Уэзерби и Акине за это сторицей!"),
55: ("That's just it... Are we really okay with defeating those two?",
     "В том-то и дело… Мы и правда можем победить этих двоих?"),
56: ("Hah? What nonsense are you talking. They're invaders!",
     "А? Что за вздор. Они захватчики!"),
57: ("Weatherly may be, but...", "Уэзерби — может, но…"),
58: ("What? You're being awfully hesitant.", "Что? Ты говоришь очень нерешительно."),
59: ("At least Akina is just a personality implanted in Haruna's mind. "
     "Her body is Haruna's, isn't it?",
     "По крайней мере Акина — лишь личность, внедрённая в разум Харуны. "
     "А тело Харуно, верно?"),
60: ("Hurting Akina means hurting Haruna...", "Ранить Акину — значит ранить Харуну…"),
61: ("T-That's... Well, yes.", "Т-Это… Ну, да."),
62: ("Maybe they have circumstances that forced them into this...",
     "Может, у них есть обстоятельства, которые их вынудили…"),
63: ("Even so, they're trying to kill everyone in this academy, you know?",
     "Даже так, они же хотят убить всех в академии, правда?"),
64: ("Yeah...", "Да…"),
65: ("I wonder if Haruna will ever come back...", "Интересно, вернётся ли Харуна…"),
66: ("That's something to leave to the professor. In the end, maybe he can do something.",
     "Это слово за сэнсэем. В конце концов, может, он что-то сможет."),
67: ("Or maybe he can't.", "Или может не сможет."),
68: ("...", "…"),
69: ("I want to restore Haruna no matter what. Even if, once she's back, "
     "she's tormented by what she did as Akina...",
     "Я во что бы то ни стало хочу вернуть Харуну. Даже если, когда она вернётся, "
     "её будут мучить дела, совершённые ею как Акиной…"),
70: ("Even so, Haruna has to become Haruna again.", "И всё равно Харуна должна стать Харуной."),
71: ("...", "…"),
72: ("But if only Weatherly can fix Haruna...", "Но если только Уэзерби может исправить Харуну…"),
73: ("Let's think about that once it's all over. Now is not the time to hesitate.",
     "Об этом подумаем, когда всё кончится. Сейчас не время сомневаться."),
74: ("I know. I know it, but...", "Я знаю. Я знаю, но…"),
75: ("...", "…"),
76: ("Hey, you two. Mind if I join the conversation? Someone's coming.",
     "Эй, вы двое. Можно мне присоединиться? Кто-то идёт."),
77: ("Eh...?", "А…?"),
78: ("Two sets of footsteps.", "Два шага."),
79: ("Enemies?", "Враги?"),
80: ("What'll you do, partner? Go out and meet them?", "Что решим, приятель? Выйдем навстречу?"),
81: ("No, they could be allies. Let's see who it is first.",
     "Нет, могут быть союзники. Сначала посмотрим, кто это."),
82: ("They're coming, partner... That's it!", "Они идут, приятель… Это что такое!"),
83: ("Who's there!? Huh? It's Kirche and Tabitha.", "Кто там!? А? Это Кирке и Табаса."),
84: ("...", "…"),
85: ("...", "…"),
86: ("Don't come closer, partner! Something's off about them.",
     "Не подходи, приятель! Что-то с ними не так."),
87: ("N-No... It can't be!", "Н-Нет… Не может быть!"),
88: ("Damn. I can't hold back, then!", "Чёрт. Тогда я не смогу сдерживаться!"),
89: ("Phew. That's done.", "Фух. Готово."),
90: ("O-Oh? Why are you here, Louise? And where are we?",
     "О-Ой? Почему ты здесь, Луиза? И где мы?"),
91: ("The underground passage.", "Подземный ход."),
92: ("Well, well. You're back to your senses at last, eh?",
     "Ну-ну. Вы наконец пришли в себя, да?"),
93: ("Explain, darling. What's going on?", "Объясни, дорогой. Что происходит?"),
94: ("First, let me check. Kirche, what's the last thing you remember?",
     "Сначала проверю. Кирке, что ты помнишь последним?"),
95: ("Um. Well, after clearing most of the courtyard enemies, we stormed the "
     "headmaster's office where Weatherly and Akina were.",
     "Э-Э. Ну, после того как мы убрали большинство врагов во дворе, мы штурмовали "
     "кабинет директора, где были Уэзерби и Акина."),
96: ("There, I came face to face with Weatherly...",
     "Там я встретилась с Уэзерби лицом к лицу…"),
97: ("Routed.", "Отбиты."),
98: ("Indeed, I have no memory after that.", "Да, после этого я ничего не помню."),
99: ("More importantly, darling—why are you wearing earplugs?",
     "Главное, дорогой — почему у тебя беруши?"),
100: ("Well, that's the thing...", "Ну, в том-то и дело…"),
101: ("I thought so. Tabitha said as much—that there was such a countermeasure.",
     "Я так и думал. Табаса тоже говорила, что есть такое средство."),
102: ("By the way, you two do agree with our plan, don't you?",
     "Кстати, вы двое согласны с нашим планом, да?"),
103: ("No reason to refuse.", "Причин отказываться нет."),
104: ("Same here.", "И я тоже."),
105: ("Thanks.", "Спасибо."),
106: ("Honestly, I was worried about what we'd do if we couldn't find you two. "
      "I'm glad we have more allies.",
     "Честно, я не знал, что делать, если мы вас не найдём. Рад, что союзников стало больше."),
107: ("We really have no choice but to split into two groups.",
     "И правда придётся разделиться на две группы."),
108: ("Going from the rooftop to the headmaster's office takes too long.",
     "Переход с крыши в кабинет директора займёт слишком много времени."),
109: ("Darling, how will you divide the groups?", "Дорогой, как ты разделишь группы?"),
110: ("Why are you asking me?", "Почему ты меня спрашиваешь?"),
111: ("Oh? Can Louise decide?", "Ой? Луиза может решить?"),
112: ("What was that—!", "Что ты сказала—!"),
113: ("Come on, stop fighting.", "Ну же, прекратите ссориться."),
114: ("...", "…"),
115: ("Hm? What is it, Tabitha?", "Хм? Что случилось, Табаса?"),
116: ("Kirche and Louise.", "Кирке и Луиза."),
117: ("Me and Saito.", "Я и Сайто."),
118: ("With Louise? Well, if Tabitha says so, I suppose it can't be helped. "
      "She must have a reason...",
     "С Луизой? Ну, если Табаса так говорит, видно, ничего не поделать. "
     "Наверное, у неё есть причина…"),
119: ("Mm.", "Мм."),
120: ("So that's how it is. Louise, I'll go with you.",
     "Так вот как. Луиза, я пойду с тобой."),
121: ("Fine. If you insist, I'll go with Kirche.",
     "Ладно. Раз ты настаиваешь, пойду с Кирке."),
122: ("Tabitha, I'm counting on you.", "Табаса, на тебя надеюсь."),
123: ("Please.", "Пожалуйста."),
124: ("Yeah. With Tabitha, I feel better.", "Да. С Табасой мне спокойнее."),
125: ("Thank you.", "Спасибо."),
}
CHOICES = {
739: [("Saito and I split up?", "Мы с Сайто действуем раздельно?"),
      ("If we can link up with Kirche and Tabitha", "Если получится соединиться с Кирке и Табасой"),
      ("Which should we do first?", "Что делать сперва?")],
744: [("Weatherly may be, but...", "Уэзерби — может, но…"),
      ("Maybe they have circumstances", "Может, у них есть обстоятельства"),
      ("Will Haruna ever come back?", "Вернётся ли Харуна?")],
}
SPK = {'サイト': 's', 'コルベール': 'c', 'ルイズ': 'l', 'デルフリンガー': 'd',
       'キュルケ': 'k', 'タバサ': 't', 'null': 'th'}
START = {'s': 247, 'c': 74, 'l': 187, 'd': 25, 'k': 33, 't': 23, 'th': 0}


def main():
    data = json.load(open('reports/ch19/parse_739_768.json', encoding='utf-8'))
    script = ['# Глава 19, часть 1 (сцены 739–749): утро операции, подземный ход.',
              '# Источник: ps2_source/chapters/chapter_20_小悪魔と春風の協奏曲.txt (SCENE 739-749).',
              '', 'label ch19:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 749:
                break
            scene = x['no']
            script += ['label ch19_1_scene_%d:' % scene, '']
            continue
        if k == 'event':
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
            tag = 'ch19_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch19_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch19_1_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 739 <= scene <= 749:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch19_1_scene_%d' % x['target']
                                          if 739 <= x['target'] <= 749 else 'ch19_2'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch19_2', '    return', '']
    files = {
        'game/chapters/19/script-ch19_1.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch19_1_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch19_1_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch19_1_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch19_1_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch19/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
