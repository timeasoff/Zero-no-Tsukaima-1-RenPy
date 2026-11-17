#!/usr/bin/env python3
"""Chapter 16 (scenes 660-669): bed confusion, Haruna's departure."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("Yoohoo~, darling.", "Ауу~, дорогой."),
1: ("O-Oh. Kirche!", "О-Ой. Кирке!"),
2: ("Ugh, Kirche!", "Ох, Кирке!"),
3: ("We don't see each other much lately... Are you dumping me?",
    "Мы теперь редко видимся… Ты что, бросил меня?"),
4: ("N-No, that's not it, but...", "Н-Нет, дело не в этом, но…"),
5: ("K-Kirche, get away from him! You stupid dog!", "К-Кирке, отойди от него! Глупый пёс!"),
6: ("...Eek! S-Sorry, mistress!", "…Кайн! П-Прости, госпожа!"),
7: ("Wait, Louise? What are you doing to darling?", "Эй, Луиза? Что ты делаешь с дорогим?"),
8: ("We were finally having a nice talk after so long...", "Мы наконец-то нормально поговорили после долгого перерыва…"),
9: ("S-Saito is my familiar! He can't talk to other girls!",
    "С-Сайто — мой фамильяр! Он не должен разговаривать с другими девушками!"),
10: ("My my... Darling, you've got quite a terrible mistress, haven't you...",
     "Ой-ой… Дорогой, у тебя ужасная госпожа, да…"),
11: ("Come on, let's go, stupid dog!", "Ну же, идём, глупый пёс!"),
12: ("Y-Yes, ma'am!", "Т-Так точно!"),
13: ("Ufufu. Isn't this fun.", "Уф-фу. Это забавно."),
14: ("Listen, Valliere. The bigger the obstacle, the more my flame of love burns...!",
     "Слушай, Вальер. Чем больше препятствие, тем сильнее горит пламя моей любви…!"),
15: (None, None),
16: ("(Ufufu. If it's come to this, I'll just have to use force.)",
     "Уф-фу. Раз дошло до этого, придётся действовать."),
17: ("(Love is war... Louise?)", "Любовь — это война… Луиза?"),
18: ("Darling is...? Ah, that outfit is bed, right?", "Дорогой…? А, этот наряд — для постели, да?"),
19: ("Mumble mumble...", "Ммм-ммм…"),
20: ("Ufu, darling, it's me, me. I've come.", "Уфу, дорогой, это я, я. Я пришла."),
21: ("Today I'm going to make you mine, darling.", "Сегодня я сделаю тебя своим, дорогой."),
22: ("Mm...", "Мм…"),
23: ("...Ufufu, what a cute voice. Ticklish, ticklish...",
     "…Уф-фу, какой милый голосочек. Щекотно, щекотно…"),
24: ("Mm... Ah...", "Мм… Ах…"),
25: ("Oh, you're more delicate than I thought, darling.",
     "Ой, ты более хрупкий, чем я думала, дорогой."),
26: ("And such beautiful skin... Your chest is so slender too.",
     "И какая красивая кожа… Грудь тоже такая худенькая."),
27: ("Ah... No...", "Ах… Нет…"),
28: ("Ufufu, I'm helping myself~~.", "Уф-фу, я забираю свовоо~~."),
29: ("...", "…"),
30: ("Ufufu.", "Уф-фу."),
31: ("Saito! Stop...!", "Сайто! Прекрати…!"),
32: ("...Huh? Huh? Kirche?", "…А? А? Кирке?"),
33: ("...O-Oh? Louise?", "…О-Ой? Луиза?"),
34: ("...What the hell are you two doing!?", "…Что вы двое, чёрт возьми, делаете!?"),
35: ("E-Eek!", "К-Кайн!"),
36: ("Why are you two hugging in bed!?", "Почему вы двое обнимаетесь в постели!?"),
37: ("(Since when is this place paradise?)", "(С каких пор здесь рай?)"),
38: ("H-Hugging...!? N-n-n-n-n-n-n-n-n-n...!", "О-Обнимаетесь…? Н-Н-Н-Н-Н…!"),
39: ("Geez, darling—want to join in?", "Ну же, дорогой — хочешь присоединиться?"),
40: ("What are you saying! Kirche!", "Что ты говоришь! Кирке!"),
41: ("I mean, what are you doing!?", "И вообще, что вы делаете!?"),
42: ("E-Er... A good night greeting?", "Э-Э… Ночное приветствие?"),
43: ("What's that supposed to mean!", "Что это значит!"),
44: ("I don't care what you call it! What were you doing to Saito while I was sleeping!?",
     "Неважно, как это называется! Что ты делала с Сайто, пока я спала!?"),
45: ("Oh, now that you mention it...", "А, кстати…"),
46: ("What do you mean 'oh now that you mention it'! Are you an idiot!",
     "Это ещё что за «кстати»! Ты что, идиотка!"),
47: ("(Sigh. It's started again...)", "(Фух. Опять началось…)"),
48: ("(G-God... Have I done something wrong?)", "(Б-Боже… Я что-то не то сделал?)"),
49: ("Saito, why are you escaping reality!", "Сайто, почему ты уходишь от реальности!"),
50: ("Say something! Tell her you're mine!", "Скажи что-нибудь! Скажи, что ты мой!"),
51: ("What! Darling is mine, right?", "Что! Дорогой — мой, верно?"),
52: ("(...H-Help me, God!)", "(…П-Помоги мне, боже!)"),
53: ("I'm tired. I'm going to sleep.", "Я устал. Иду спать."),
54: ("Wait, what's this! Sleeping so irresponsibly!", "Эй, что это! Спишь так безответственно!"),
55: ("D-Darling!", "Д-Дорогой!"),
56: ("Well, fine! Kirche, let's settle this today!", "Ладно! Кирке, сегодня мы это выясним!"),
57: ("Gladly! Come outside!", "С удовольствием! Выходи на улицу!"),
58: ("(Why do I always get the short straw...?)", "(Почему мне всегда достаётся самое плохое…?)"),
59: ("(Surrounded by such cute girls, and there's me, who can't do anything...)",
     "Столько милых девушек, а я — тот, кто ничего не может…"),
60: ("(Damn it!!)", "(Чёрт!!)"),
61: ("...What's wrong, darling? Crying all of a sudden.", "…Что случилось, дорогой? Вдруг заплакал."),
62: ("S-Saito?", "С-Сайто?"),
63: ("What's there to complain about, surrounded by such cute girls as us!",
     "Что тебе не нравится, когда тебя окружают такие милые девушки, как мы!"),
64: ("It's your fault for being indecisive, darling!", "Это твоя вина — ты нерешительный, дорогой!"),
65: ("...Ugh. Sorry.", "…Ох. Простите."),
66: ("...Really, you're...", "…Ну и ну,"),
67: ("...such an idiot.", "…глупый."),
68: ("Eh? What do you mean, 'becoming independent'?", "А? Что значит «стать самостоятельной»?"),
69: ("Well... I can't stay at this academy forever... I thought it was about time "
     "I stopped relying on Louise-san and the others.",
     "Ну… Я не могу вечно оставаться в этой академии… Я подумала, что пора "
     "перестать зависеть от Луизы-сан и остальных."),
70: ("If you say that, I've been living off Louise's kindness ever since she summoned me, "
     "one way or another.",
     "Если так, то я с тех пор, как Луиза меня вызвала, всё равно жил за счёт академии."),
71: ("Hiraga-kun is Louise-san's familiar, so of course. But I'm not...",
     "Хирага-кун — фамильяр Луизы-сан, это понятно. Но я нет…"),
72: ("That's true, but... We're probably the only two Japanese people in this world.",
     "Это верно, но… Мы, наверное, единственные японцы в этом мире."),
73: ("And we're not exactly strangers to each other... So if I worked at the academy, maybe...",
     "И мы не совсем чужие друг другу… Так что, если бы я работал в академии, может…"),
74: ("You see, Hiraga-kun... I've been scouted.", "Дело в том, Хирага-кун… Меня завербовали."),
75: ("S-Scouted for what?", "З-Завербовали — куда?"),
76: ("A troupe, a troupe.", "В труппу, в театральную труппу."),
77: ("A troupe? You mean that Weatherly's troupe?", "Труппа? Ты имеешь в виду труппу Уэзерби?"),
78: ("No. Someone from another troupe who saw that play liked me and scouted me.",
     "Нет. Кто-то из другой труппы, кто видел тот спектакль, понравился мне и завербовал."),
79: ("I thought this was a good chance, so I'm going to join them.",
     "Я подумала, что это хороший шанс, и хочу к ним присоединиться."),
80: ("But joining a troupe means performing in other towns, right?",
     "Но в труппе придётся ездить на гастроли в другие города, да?"),
81: ("Yes. We'll probably see less of each other, Hiraga-kun.",
     "Да. Мы с тобой, наверное, будем видеться реже, Хирага-кун."),
82: ("But I'm looking forward to it. I get to see so many towns in this world.",
     "Но я с радостью жду этого. Я смогу увидеть много городов в этом мире."),
83: ("Maybe I'll even find a clue to get back to Japan?",
     "Может, я даже найду подсказку, как вернуться в Японию?"),
84: ("I see. Yeah, that's right.", "Понятно. Да, верно."),
85: ("So, Hiraga-kun... Please cheer me on, if you don't mind.",
     "Так что, Хирага-кун… Пожалуйста, поддержи меня, если не против."),
86: ("Of course! And let's both do our best to find a way back to Japan!",
     "Конечно! И давай вместе искать способ вернуться в Японию!"),
87: ("Mm!", "Мм!"),
88: ("Hiiii! You two!", "Хиии! Вы двое!"),
89: ("Kirche!", "Кирке!"),
90: ("Kirche-san! About before—I'm sorry. Back then...",
     "Кирке-сан! Прошу прощения за то, что было тогда…"),
91: ("Ah, it's fine.", "А, ладно."),
92: ("If I kept harping on what's past, the name of Kirche with a slight fever would cry.",
     "Если я буду всё время твердить о прошлом, имя Кирке с лёгким жаром будет плакать."),
93: ("Y-Yes. Um...", "Д-Да. Э-Э…"),
94: ("...", "…"),
95: ("Ah, right!", "А, точно!"),
96: ("I wanted to give Haruna a parting gift. I've prepared a special spell for her.",
     "Я хотела сделать Харуне прощальный подарок. Я подготовила для неё особенное заклинание."),
97: ("Eh, such a thing...", "Ах, не надо…"),
98: ("...This is the true way to use 'fire' magic.", "…Вот как на самом деле используется магия «огня»."),
99: ("Fireworks.", "Фейерверк."),
100: ("Wow.", "Ого."),
101: ("...", "…"),
102: ("Kirche-san.", "Кирке-сан."),
103: ("Please take care of Hiraga-kun.", "Пожалуйста, присматривай за Хирага-куном."),
104: ("Huh?", "А?"),
105: ("...", "…"),
106: ("Eh? Ah... Yes...", "А? А… Да…"),
107: ("I don't quite get it, but... Okay.", "Я не совсем понимаю, но… ладно."),
108: ("Well, it's not like I'm entrusting him to you... Just don't let that Louise break him.",
     "Впрочем, я не чтобы ты за ним ухаживала… Просто не дай той Луизе его сломать."),
109: ("What are you talking about?", "О чём вы?"),
110: ("Ufufu, why don't you guess?", "Уф-фу, догадайся."),
111: ("Hiraga-kun! Be careful with girls.", "Хирага-кун! Осторожнее с девушками."),
112: ("Y-Yes!", "Д-Да!"),
113: (None, None),
114: ("Ah, she's gone, huh...", "Ах, она ушла…"),
115: ("Oh, darling. Are you lonely?", "Ой, дорогой. Тебе одиноко?"),
116: ("Well... She was like the only friend I had. And now my little sister's gone too...",
     "Ну… Она была как единственный друг. А теперь ещё и сестрёнка ушла…"),
117: ("Little sister?", "Сестрёнка?"),
118: ("No, nothing!", "Нет, ничего!"),
119: ("(Kirche doesn't seem to remember being a child...)", "(Кирке, кажется, не помнит, что была ребёнком…)"),
120: ("...", "…"),
121: ("(O-Of course it was good! Though that imbalance was something else...)",
     "К-Конечно, всё было хорошо! Хотя тот дисбаланс был чем-то…"),
122: ("...Haa.", "…Фух."),
123: ("Heh, heh.", "Хе-хе."),
124: ("(Happy and sad... Mixed feelings. And that imbalance was exquisite...)",
     "И радостно, и грустно… Смешанные чувства. И тот дисбаланс был прекрасен…"),
125: ("...Darling?", "…Дорогой?"),
126: ("...Maybe I liked it that way better?", "…Может, мне больше нравилось, когда она была такой?"),
127: ("Geez, darling!", "Ну же, дорогой!"),
128: ("What do you mean, 'that way'?", "Что значит «такой»?"),
129: ("Eh? Ah, no—Ahahaha...", "А? А, нет—А-ха-ха…"),
130: ("Really, darling, with me right here, what are you thinking about!",
     "Ну же, дорогой, я же рядом, а ты всё думаешь о чём-то!"),
131: ("Whoa! If you hug me like that, all sorts of things...!", "Ого! Если ты так обнимаешь, то всякое…!"),
132: ("Ufufu. Were you thinking something naughty?", "Уф-фу. Ты думал о чём-то неподобающем?"),
133: ("Eh?", "А?"),
134: ("No, you can't! Big brother?", "Нет, нельзя! Братишка?"),
135: ("...Eh?", "…А?"),
136: ("Eh!?", "А!?"),
137: ("Ufufu!", "Уф-фу!"),
}
CHOICES = {
660: [("Pray to heaven", "Помолиться небу"),
      ("I'm tired today. Think tomorrow", "Сегодня я устал. Подумаю завтра"),
      ("I'll cry", "Я расплачусь")],
665: [("Of course it was good, though!", "Конечно, всё было хорошо!"),
      ("Happy and sad at the same time...", "И радостно, и грустно…"),
      ("Maybe I liked it that way better...?", "Может, мне нравилось, когда она была такой…?")],
}
SPK = {'キュルケ': 'k', 'サイト': 's', 'ルイズ': 'l', 'ハルナ': 'ha', 'null': 'th'}
START = {k: 0 for k in SPK.values()}


def main():
    data = json.load(open('reports/ch16/parse_660_669.json', encoding='utf-8'))
    script = ['# Глава 16 (сцены 660–669): «微熱の使い手» — постельные неразберихи и отъезд Харуны.',
              '# Источник: ps2_source/chapters/chapter_17_微熱の使い手.txt (SCENE 660-669).',
              '', 'label ch16:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            scene = x['no']
            script += ['label ch16_1_scene_%d:' % scene, '']
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
            tag = 'ch16_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch16_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch16_1_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump ch16_1_scene_%d' % x['target'])
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 16 ====', '    jump ch17', '    return', '']
    files = {
        'game/chapters/16/script-ch16_1.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch16_1_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch16_1_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch16_1_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch16_1_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch16/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
