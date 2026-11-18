#!/usr/bin/env python3
"""Chapter 28 part 1 (scenes 999-1007): Tabitha's secret cake."""
import json, sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("Hey, darling! What's the meaning of this!?", "Эй, дорогой! Что это значит!?"),
1: ("What do you mean, what's the meaning?", "Что значит «что значит»?"),
2: ("Going out on secret dates with Tabitha night after night—behind my back!",
     "Ноч за ночью тайно встречаться с Табасой — за моей спиной!"),
3: ("Um... I'm afraid I don't follow?", "Э-Э… Я не понимаю, о чём вы?"),
4: ("What was that!? You went behind my back and did something with Tabitha...",
     "Что это было!? Ты сделал что-то с Табасой за моей спиной…"),
5: ("I let you sleep in my bed every night—why would you sneak out to do that...",
     "Я же каждую ночь разрешаю тебе спать в моей кровати — зачем ты выскальзывал…"),
6: ("No—if we were sleeping in the same bed, you'd normally notice me sneaking out, wouldn't you?",
     "Нет — если бы мы спали в одной кровати, ты бы обычно заметила, что я ушёл, да?"),
7: ("I'm a deep sleeper! Not noticing is only natural!", "Я сплю очень крепко! Не заметить — естественно!"),
8: ("You're that determined to make me the villain?", "Ты так стремишься сделать меня злодеем?"),
9: ("Villain? Hah! You're a dog, aren't you?", "Злодей? Ха! Ты же пёс, да?"),
10: ("...Even as I tell the truth, Louise keeps calling me a dog...", "…Даже говоря правду, Луиза называет меня псом…"),
11: ("Say, darling. You're really not meeting Tabitha at night?", "Слушай, дорогой. Ты и правда не встречаешься с Табасой по ночам?"),
12: ("I'm not! Absolutely not!!", "Нет! Ни в коем случае!!"),
13: ("Hmm... My intuition was wrong, after all.", "Хм… Моя интуиция ошиблась."),
14: ("Hey—what was that just now?", "Эй — что ты сейчас сказал?"),
15: ("I said my intuition was wrong.", "Я сказал, что интуиция ошиблась."),
16: ("Not that part. The part after.", "Не это. То, что после."),
17: ("Oh—that my intuition? ", "Ах — что моя интуиция?"),
18: ("That's it. You blamed me on intuition alone?", "Вот. Ты обвинил меня лишь по интуиции?"),
19: ("Well... In the end, yes.", "Ну… В конце концов, да."),
20: ("So why did this story about Saito and Tabitha dating at night start?",
     "Так откуда взялась эта история о том, что Сайто и Табаса встречаются по ночам?"),
21: ("Actually... There's a rumor that Tabitha's been up to something at night lately.",
     "Дело в том… Ходит слух, что Табаса в последнее время что-то делает по ночам."),
22: ("And I figured—any rumor about Tabitha probably involves darling, right?",
     "Я и подумала — может, любой слух о Табасе как-то связан с дорогим, да?"),
23: ("Look here...", "Слушай…"),
24: ("If you want to know what Tabitha's doing so badly, why not just ask her directly?",
     "Если тебе так хочется узнать, что делает Табаса, почему бы не спросить её напрямую?"),
25: ("That's the thing—I tried asking casually, but she wouldn't tell me...",
     "В том-то и дело — я попробовала спросить косвенно, но она не сказала…"),
26: ("All right, all right. I'll go ask her now, then.", "Ладно-ладно. Тогда я сейчас пойду и спрошу."),
27: ("Honestly... I wonder what everyone's so worried about.", "Право… Интересно, чего все так волнуются."),
28: ("Um—this is Saito...", "Э-Э — это Сайто…"),
29: ("Come in.", "Входи."),
30: ("...What is it?", "…Что тебе?"),
31: ("Well, actually—have you been keeping anything from everyone lately?",
     "Ну, дело в том — ты последнее время что-то скрываешь от всех?"),
32: ("...", "…"),
33: ("(Ah—she's silent, but I can tell she's hiding something...)", "Ах — она молчит, но я чувствую, что что-то скрывает…"),
34: ("Then—will you tell just me? What you do at night, Tabitha?", "Тогда — расскажешь только мне? Что ты делаешь по ночам, Табаса?"),
35: ("...", "…"),
36: ("No good?", "Не получится?"),
37: ("No.", "Нет."),
38: ("Ehh—why not?", "А — почему?"),
39: ("No means no.", "Нет — значит нет."),
40: ("O-Okay... At least a hint, then...", "Л-Ладно… Тогда хотя бы намёк…"),
41: ("I won't tell.", "Не скажу."),
42: ("...Say, Tabitha...", "…Слушай, Табаса…"),
43: ("You don't want to tell me that badly?", "Ты настолько не хочешь мне говорить?"),
44: ("Mm. To you especially.", "Мм. Только тебе — абсолютно."),
45: ("'To me especially'... And 'absolutely', too...", "«Особенно мне»… И при этом «абсолютно»…"),
46: ("Are you doing something you can't tell anyone?", "Ты делаешь что-то, о чём нельзя никому говорить?"),
47: ("No, I'm not.", "Нет."),
48: ("Then...", "Тогда…"),
49: ("But I can't tell you now.", "Но сейчас я не могу сказать тебе."),
50: ("Eh? What do you mean?", "А? Что ты хочешь сказать?"),
51: ("Could it be—you hate me?", "Неужто — ты меня ненавидишь?"),
52: ("...", "…"),
53: ("(She won't answer... And she looks so troubled...)", "Она не отвечает… И у неё такой обеспокоенный вид…"),
54: ("Um—sorry for asking something strange.", "Э-Э — прости, что спросил странное."),
55: ("...", "…"),
56: ("(Still troubled...)", "Всё ещё обеспокоена…"),
57: ("...", "…"),
58: ("...", "…"),
59: ("Um... I'm going home now.", "Э-Э… Я пойду домой."),
60: ("Ah...", "Ах…"),
61: ("What was that?", "Что это было?"),
62: ("...", "…"),
63: ("Well then—", "Ну что ж —"),
64: ("How did it go, darling?", "Как всё прошло, дорогой?"),
65: ("...", "…"),
66: ("Hey, Saito! Say something!", "Эй, Сайто! Скажи что-нибудь!"),
67: ("...Sorry. I couldn't do it.", "…Прости. У меня не получилось."),
68: ("Meaning... She didn't tell you either, did she?", "Значит… Она и тебе не сказала, да?"),
69: ("Far from it... Ugh... Can I just go to sleep now?", "Более того… Ох… Можно мне уже лечь спать?"),
70: ("You're starting to feel sorry for him, so you can go ahead and sleep first.", "Мне его стало жалко, так что иди спать первым."),
71: ("Then, excuse me...", "Тогда, прошу прощения…"),
72: ("Hey! Saito! Why are you trying to sleep on straw on the floor! Get into bed properly...",
     "Эй! Сайто! Почему ты собираешься спать на соломе на полу! Ложись в кровать как надо…"),
73: ("It's fine for me... Sleeping on the floor suits a bad dog like me...",
     "Мне хорошо… Спать на полу — как раз для такого плохого пса, как я…"),
74: ("Oh my—darling's become completely self-deprecating.", "Ох — дорогой совсем ушёл в самоуничижение."),
75: ("Sniff... Sniffle... Hiccup... S-snore...", "Хлюп… Хлюп… Ик… С-сплю…"),
76: ("...He's already asleep.", "…Он уже уснул."),
77: ("Tabitha really drove darling into a corner, didn't she...", "Табаса и правда загнала дорогого в угол…"),
78: ("Ugh—I fell asleep too fast and woke up before it was even morning.", "Ох — я слишком быстро уснул и проснулся ещё до утра."),
79: ("Huh? The kitchen light's still on. It's not time for prep yet...", "А? Свет на кухне ещё горит. Ещё не время готовить…"),
80: ("Ah.", "Ах."),
81: ("That voice—Tabitha?", "Этот голос — Табаса?"),
82: ("...", "…"),
83: ("What's wrong?", "Что случилось?"),
84: ("I was making a cake. For you.", "Я пекла торт. Для тебя."),
85: ("Eh? A cake?", "А? Торт?"),
86: ("Mm.", "Мм."),
87: ("...Tabitha made it?", "…Табаса сделала его?"),
88: ("Homemade.", "Сделала сама."),
89: ("Tabitha—you had a hobby of cake-making?", "Табаса — у тебя было хобби печь торты?"),
90: ("No, I didn't. But...", "Нет. Но…"),
91: ("'Didn't'—meaning, perhaps...", "«Не было» — значит, может быть…"),
92: ("Did you take up cake-making as a hobby?", "Ты начала печь торты как хобби?"),
93: ("...Mm.", "…Мм."),
94: ("But why suddenly?", "Но почему вдруг?"),
95: ("...", "…"),
96: ("You still won't tell me, will you?", "Ты всё равно не скажешь мне, да?"),
97: ("...Because I wanted you to eat it.", "…Потому что я хотела, чтобы ты его съел."),
98: ("Eh? Really?", "А? Правда?"),
99: ("Mm, really. But it's full of failures.", "Мм, правда. Но полно ошибок."),
100: ("You made it for me?", "Ты сделала это для меня?"),
101: ("...Mm.", "…Мм."),
102: ("...Eh? Really?", "…А? Правда?"),
103: ("Really. But it's full of failures.", "Правда. Но полно ошибок."),
104: ("Is it part of a human experiment?", "Это часть эксперимента над людьми?"),
105: ("No.", "Нет."),
106: ("Then—a surprise prank?", "Тогда — сюрприз-розыгрыш?"),
107: ("A what?", "Что?"),
108: ("Ha ha, you don't get it, do you? It means tricking and scaring someone.",
     "Ха-ха, ты не поняла, да? Это значит обмануть и напугать."),
109: ("Then... maybe.", "Тогда… может быть."),
110: ("Eh—it's a prank?", "А — это розыгрыш?"),
111: ("Mm. I wanted to surprise you.", "Мм. Я хотела тебя удивить."),
112: ("...", "…"),
113: ("Is this still being made?", "Это ещё готовится?"),
114: ("A failure. It isn't perfect yet.", "Неудачный вариант. Ещё не совершенный."),
115: ("May I eat it?", "Можно мне его съесть?"),
116: ("...", "…"),
117: ("Then I'll eat it. Here—open up.", "Тогда я съем. Ну — открой рот."),
118: ("Is it good?", "Вкусно?"),
119: ("Mm, it's really good! You really only just learned to make cakes?", "Мм, очень вкусно! Ты и правда только начала учиться печь?"),
120: ("Mm.", "Мм."),
121: ("I can't believe it.", "Не могу поверить."),
122: ("It must be... because the teacher was good.", "Должно быть… потому что учитель был хороший."),
123: ("Teacher?", "Учитель?"),
124: ("Siesta.", "Сиэста."),
125: ("I see... But why didn't you tell me when I asked?", "Понятно… Но почему не сказала, когда я спросил?"),
126: ("Because...", "Потому что…"),
127: ("Because why?", "Потому что — что?"),
128: ("Because I wanted to see your face light up.", "Потому что я хотела увидеть твоё радостное лицо."),
129: ("(This cake Tabitha made... Word of its taste will spread from the academy kitchen "
      "to the town...)", "Этот торт, что испекла Табаса… Слух о его вкусе распространится из академической "
      "кухни по городу…"),
130: ("(...and spark a cake craze across the country. But that's another story.)",
     "…и станет началом общенациональной тортовой лихорадки. Но это уже другая история."),
}
CHOICES = {
999: [("You don't want to tell me?", "Ты не хочешь мне говорить?"),
      ("Something you can't tell anyone?", "Что-то, о чём нельзя никому?"),
      ("Do you hate me?", "Ты меня ненавидишь?")],
1003: [("A baking hobby?", "Хобби — печь торты?"),
       ("You made it for me?", "Ты сделала для меня?"),
       ("A human experiment?", "Эксперимент над людьми?")],
}
SPK = {'キュルケ': 'k', 'サイト': 's', 'ルイズ': 'l', 'タバサ': 't', 'null': 'th'}
START = {'k': 0, 's': 0, 'l': 0, 't': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch28/parse_999_1008.json', encoding='utf-8'))
    script = ['# Глава 28, часть 1 (сцены 999–1007): секретный торт Табасы.',
              '# Источник: ps2_source/chapters/chapter_29_夜の秘密.txt (SCENE 999-1007).',
              '', 'label ch28:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 1007: break
            scene = x['no']
            script += ['label ch28_1_scene_%d:' % scene, '']
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
            tag = 'ch28_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch28_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch28_1_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 999 <= scene <= 1007: continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch28_1_scene_%d' % x['target'] if 999 <= x['target'] <= 1007 else 'ch28_2'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch28_2', '    return', '']
    files = {
        'game/chapters/28/script-ch28.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch28_1_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch28_1_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch28_1_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch28_1_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch28/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
