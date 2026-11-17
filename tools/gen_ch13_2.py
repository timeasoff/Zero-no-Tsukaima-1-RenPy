#!/usr/bin/env python3
"""Chapter 13 part 2 (extra scenes 1469-1484): night investigation routes."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("Anybody know anything?", "Кто-нибудь знает что-нибудь?"),
1: ("Well... Let's ask that soldier over there.", "Ну… Спросим того солдата."),
2: ("Would they tell us that easily? Hey, Kirche!", "Неужели он так просто скажет? Эй, Кирке!"),
3: ("Good evening, soldier. We're with the academy, staying here.",
    "Добрый вечер, солдат. Мы из академии, остановились здесь."),
4: ("Yes! What can I do for you?", "Так точно! Что вам угодно?"),
5: ("I have an errand and must go out, but I'm so scared...",
    "Мне нужно выйти по делу, но я так боюсь…"),
6: ("My heart's been pounding for a while now. Look, like this...",
    "Сердце колотится уже давно. Смотрите, вот…"),
7: ("Hm, your heart!? That must be frightening indeed!", "Хм, сердце!? Должно быть, ужасно!"),
8: ("But don't worry! Under Her Majesty's authority, we'll catch the evildoers!",
    "Но не волнуйтесь! Под властью Её Величества мы поймаем злоумышленников!"),
9: ("My, how dependable. Have you learned anything about the bomb-thrower?",
    "Ой, какой надёжный. Вы узнали что-нибудь о бомбисте?"),
10: ("W-Well, you see! Actually...!", "Т-Так, видите ли! Дело в том…!"),
11: ("(Oh boy. That soldier is getting all flustered by Kirche...)",
     "Ох. Солдат совсем растерялся от Кирке…"),
12: ("(...Hmm, is that the face I make when Kirche comes on to me...?)",
     "…Хм, неужели у меня такое лицо, когда Кирке меня соблазняет…?"),
13: ("Thanks, that was helpful.", "Спасибо, было полезно."),
14: ("O beautiful lady! After this...", "О прекрасная леди! После этого…"),
15: ("Oh, no. I'm with darling today.", "О, нет. Сегодня я с дорогим."),
16: ("...", "…"),
17: ("Darling, I got the information.", "Дорогой, я получила информацию."),
18: ("(Mom, men are sad creatures.)", "Мама, мужчины — грустные существа."),
19: ("There's hardly anyone here.", "Здесь почти никого нет."),
20: ("People are hesitant to come out too... Oh, good evening. Alone?",
     "Люди, видимо, тоже боятся выходить… О, добрый вечер. Вы один?"),
21: ("(Hm? Was someone there?)", "Хм? Кто-то был?"),
22: ("Meow.", "Мяу."),
23: ("(...Eh? A cat?)", "…А? Кот?"),
24: ("Oh, is that so, how terrible. By the way, kitty, do you know the bad bomb-thrower?",
     "Ой, неужели, как ужасно. Кстати, котик, ты знаешь злого бомбиста?"),
25: ("Fumya...", "Фумяу…"),
26: ("(Kirche... is she talking to a cat?)", "Кирке… она разговаривает с котом?"),
27: ("(C-Cute. So this is a fantasy world!)", "М-Милый. Вот это мир фэнтези!"),
28: ("...", "…"),
29: ("Hm? What's wrong, darling?", "Хм? Что с тобой, дорогой?"),
30: ("No, I just... Seeing you talk to a cat is kind of cute.",
     "Нет, я просто… Это мило — разговаривать с котом."),
31: ("Eh? Really, darling. That's proper information gathering too, you know?",
     "Эй, ну давай, дорогой. Это тоже сбор информации, знаешь ли?"),
32: ("Huh? You understand cat language?", "А? Ты понимаешь кошачий язык?"),
33: ("Ufufu. Sort of.", "Уф-фу. Как-то так."),
34: ("(So this is a fantasy world! I wonder if I can talk to cats too?)",
     "Вот это мир фэнтези! Интересно, я тоже смогу поговорить с котом?"),
35: ("Darling, what's wrong? You're spacing out.", "Дорогой, что с тобой? Ты отвлёкся."),
36: ("I was wondering if I could talk to cats too.", "Я думал, смогу ли и я поговорить с котом."),
37: ("Eh?", "Э?"),
38: ("Did you see anything suspicious?", "Ты видел кого-то подозрительного?"),
39: ("Funyaa?", "Фуня?"),
40: ("I see... Tell me if anything happens again.", "Понятно… Если что-то снова случится, скажи."),
41: ("Darling, you understand cat language?", "Дорогой, ты понимаешь кошачий?"),
42: ("No, not at all.", "Нет, совсем нет."),
43: ("O-Oh, I see.", "О-Ой, понятно."),
44: ("K-Kirche broke.", "К-Кирке сломалась."),
45: ("W-What!? How rude!", "Ч-Что!? Как смело!"),
46: ("Funyaaa!!", "Фуняаа!!"),
47: ("Aah, it ran away! Really, darling!", "Аа, оно убежало! Ну же, дорогой!"),
48: ("N-No, but, you see... you were talking to a cat.", "Н-Нет, но понимаешь… ты разговаривала с котом."),
49: ("I thought it might know something...?", "Я подумала, может, он что-то знает…?"),
50: ("Huh?", "А?"),
51: ("M-Maybe Kirche really does understand cats...?", "М-Может, Кирке и правда понимает котов…?"),
52: ("Maybe, just maybe I do.", "Как-то понимаю, может быть."),
53: ("Huh?", "А?"),
54: ("Well, I get the picture now. Shall we look around a bit more?",
     "Ну, я поняла обстановку. Пойдём ещё немного поищем?"),
55: ("Really?", "Правда?"),
56: ("Oh, right on time today.", "Ой, сегодня вовремя."),
57: ("Kirche?", "Кирке?"),
58: ("...A noble young lady. 'Lend me one light, please.'",
     "…Юная благородная леди. «Одолжи мне один огонёк, пожалуйста»."),
59: ("Whoa!", "Ого!"),
60: ("Oh, 'just one'?", "Ой, «только один»?"),
61: ("'...Put two flames together and it becomes a blaze, you see.'",
     "«…Сложи два огонька вместе — и получится пожар, понимаете»."),
62: ("Darling, relax. It's the informant.", "Дорогой, не волнуйся. Это информатор."),
63: ("I can't see where they are...", "Я не вижу, где он…"),
64: ("Of course not. They're not amateurs who'd reveal themselves here.",
     "Конечно. Они не дилетанты, чтобы раскрываться здесь."),
65: ("Is that how it works?", "Так принято?"),
66: ("Here's the report.", "Вот отчёт."),
67: ("Yes, yes. Certainly. Good work.", "Да-да. Конечно. Хорошая работа."),
68: ("Be careful. Those young ladies are being targeted.",
     "Осторожнее. За этими барышнями охотятся."),
69: ("I know. Here's your payment...", "Знаю. Вот твоя плата…"),
70: ("Heh heh...", "Хи-хи…"),
71: ("An informant, huh...", "Информатор, значит…"),
72: ("They're targeting you? Are you all right?", "За вами охотятся? Вы в безопасности?"),
73: ("My, are you worried about me?", "Ой, ты беспокоишься обо мне?"),
74: ("Ufufu, it's fine.", "Уф-фу, всё хорошо."),
75: ("Nobody can beat the combo of Kirche with a slight fever and darling!",
     "Никто не одолеет связку «Кирке с лёгким жаром и дорогой»!"),
76: ("Can you trust them?", "Можно ли ему верить?"),
77: ("Well, who knows?", "Ну, кто знает?"),
78: ("Hey now.", "Эй, давай."),
79: ("W-Where did you meet someone like that...?", "Г-Где ты познакомилась с таким…?"),
80: ("Ufufu... A girl needs her secrets.", "Уф-фу… Девушке нужны свои секреты."),
81: ("That's not an ordinary girl's secret, is it...?", "Это не обычный девичий секрет, правда…?"),
82: ("Shall we look around a bit more?", "Пойдём ещё немного поищем?"),
83: ("It's late, but there are quite a few people here.", "Уже поздно, но здесь довольно много народу."),
84: ("Well, the market opens at dawn.", "Ну, рынок открывается на рассвете."),
85: ("Oh, this fruit is delicious!", "Ой, какой вкусный фрукт!"),
86: ("Eating fruit all of a sudden...", "Вдруг начала есть фрукты…"),
87: ("Weren't we supposed to be investigating!?", "Мы же должны расследовать!?"),
88: ("Oh, it's fine. It looked delicious. And I got information too.",
     "Ой, ладно. Он выглядел вкусным. И информацию я тоже получила."),
89: ("R-Really?", "П-Правда?"),
90: ("Market people are surprisingly well-informed.", "Люди на рынке удивительно осведомлены."),
91: ("I see...", "Понятно…"),
92: ("Did you get any information?", "Ты получила информацию?"),
93: ("E-Eh, of course.", "К-Конечно."),
94: ("Like how to tell delicious fruit... or how to catch a boy's eye...",
     "Например, как выбрать вкусный фрукт… или как привлечь внимание мальчика…"),
95: ("You know? Wrap vegetables in wet paper and they last longer.",
     "Знаешь? Если завернуть овощи во влажную бумагу, они дольше хранятся."),
96: ("I don't need that kind of information.", "Мне такая информация не нужна."),
97: ("Really? Well, I suppose market people are well-informed.",
     "Правда? Ну, ладно, что люди на рынке осведомлены."),
98: ("Would they really give you important info for one fruit?",
     "Неужели за один фрукт они дали важную информацию?"),
99: ("Mm. Well, information at that price.", "Мм. Ну, информация по такой цене."),
100: ("But it's fine. This fruit is delicious. Want to try some, darling?",
     "Но это хорошо. Фрукт вкусный. Хочешь попробовать, дорогой?"),
101: ("N-Now's not the time for that!", "Н-Сейчас не до этого!"),
102: ("Sigh, I'm getting hungry too. I'll take one.", "Фух, я тоже проголодался. Возьму один."),
103: ("Ufufu. Eating like this, just the two of us, feels like a date.",
     "Уф-фу. Есть так, вдвоём — как свидание."),
104: ("N-Now that you mention it... yeah.", "Т-Теперь, когда ты сказала… да."),
105: ("Eating in the night city like this...", "Есть в ночном городе вот так…"),
106: ("If it were a lavish meal, maybe.", "Если бы это был роскошный ужин — может."),
107: ("Oh, with darling, anything tastes like the best meal.",
     "Ой, с дорогим любая еда — лучшая в мире."),
108: ("I'm getting embarrassed...", "Мне становится неловко…"),
109: ("Really, darling, you're so cute!", "Ну же, дорогой, ты такой милый!"),
110: ("(Is it really all right...?)", "И правда всё хорошо…?"),
}
CHOICES = {
1470: [("Cute...", "Милый…"),
       ("I'll try talking too.", "Я тоже попробую поговорить."),
       ("Kirche broke.", "Кирке сломалась.")],
1475: [("They're targeting you? Are you all right?", "За вами охотятся? Вы в безопасности?"),
       ("Can you trust them?", "Можно ли ему верить?"),
       ("W-Where did you meet them?", "Г-Где вы с ним познакомились?")],
1480: [("Accept it.", "Согласиться."),
       ("Look suspicious.", "Посмотреть с подозрением."),
       ("I'll have one too.", "Я тоже возьму.")],
}
SPK = {'サイト': 's', 'キュルケ': 'k', '味方Ａ': 'soldier', '猫': 'cat',
       '情報屋': 'informant', 'null': 'th'}
START = {'s': 50, 'k': 41, 'soldier': 0, 'cat': 0, 'informant': 0, 'th': 2}


def main():
    data = json.load(open('reports/ch13/parse_1469_1484.json', encoding='utf-8'))
    script = ['# Глава 13, часть 2 (сцены 1469–1484): ночные маршруты Кирке и Сайто.',
              '# Источник: ps2_source/chapters/chapter_14_炎の予感.txt (SCENE 1469-1484).',
              '', 'label ch13_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            scene = x['no']
            script += ['label ch13_2_scene_%d:' % scene, '']
            continue
        if k == 'event':
            event(x['src'], script)
            continue
        if k == 'dlg':
            en, ru = T[x['idx']]
            if en is None:
                script.append('    # ' + x['src'] + ' (no voice)')
                continue
            en = en_norm(en)
            spk = SPK.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch13_%s_%03d' % (spk, counters[spk])
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
            script.append('    menu:')
            for i, o in enumerate(x['options']):
                en, ru = CHOICES[scene][i]
                ctext = '%s{#ch13_2_c_%d_%d}' % (en_norm(en), scene, i + 1)
                tgt = 'ch13_2_scene_%d' % o['target']
                script.append('        "%s":' % ctext)
                script.append('            jump %s' % tgt)
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump ch13_2_scene_%d' % x['target'])
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 2 ====', '    jump ch13_3', '    return', '']
    files = {
        'game/chapters/13/script-ch13_2.rpy': '\n'.join(script) + '\n',
        'game/chapters/13/script-ch13_3.rpy':
            '# Глава 13, часть 3 (сцены 568–577): заглушка.\n\n'
            'label ch13_3:\n    $ tndl(None)\n    jump ch14\n    return\n',
        'game/tl/japanese/ch13_2_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch13_2_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch13_2_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch13_2_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch13/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
