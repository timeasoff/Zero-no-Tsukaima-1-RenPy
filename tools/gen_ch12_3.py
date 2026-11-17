#!/usr/bin/env python3
"""Chapter 12 part 3 (scenes 535-543): Confrontation, illusion, the marriage joke."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("Akina!", "Акина!"),
1: ("W-What, Saito!?", "Ч-Что, Сайто!?"),
2: ("What's Weatherly to you!? She's only using you!", "При чём тут Уэзерби!? Она просто использует тебя!"),
3: ("Stop letting her use you like that. Is there anything good in staying there?",
    "Хватит позволять ей пользоваться тобой. Что хорошего в том, чтобы оставаться там?"),
4: ("Good? What do you know about Weatherly-sama?", "Хорошего? Что ты понимаешь в Уэзерби-саме?"),
5: ("Weatherly! How could you do this to Haruna...!", "Уэзерби! Как ты могла так поступить с Харуной…!"),
6: ("It was necessary for this girl to survive.", "Это было нужно, чтобы эта девочка выжила."),
7: ("What!?", "Что!?"),
8: ("Weatherly... Why! For the likes of Reconquista...!", "Уэзерби… Почему! Ради таких, как Реконкиста…!"),
9: ("I have my own circumstances. I won't make excuses.", "У меня свои обстоятельства. Я не буду оправдываться."),
10: ("I used Haruna and you by my own will and for my own reasons.",
     "Я использовала Харуну, тебя и остальных по своей воле и по своим причинам."),
11: ("If you want to stop us, then stop us with your own power!",
     "Если хотите остановить нас — останавливайте своей силой!"),
12: ("E-Eii...!", "Э-Эй!"),
13: ("Kyaaaa!", "А-а-а-а!"),
14: ("Heh...?", "Хм…?"),
15: ("A-Aaaa... what did I...? Was that Haruna's doing!?",
     "А-Аааа… что я наделала…? Это была Харуна!?"),
16: ("W-Weatherly!? Did she fall!?", "У-Уэзерби!? Она упала!?"),
17: ("(N-No way. Did she just fall?)", "Н-Не может быть. Она что, упала?"),
18: ("(F-From the top of a castle like this—even a Halkeginian wouldn't survive...)",
     "С такой высоты — даже житель Халкегинии не выживет…"),
19: ("W-What are you doing! Haruna! ...No, Akina!", "Ч-Что ты делаешь! Харуна! …Нет, Акина!"),
20: ("Eh? She's alive?", "А? Она жива?"),
21: ("She caught hold of a bay window just in time!", "Она вовремя ухватилась за выступ окна!"),
22: ("W-Weatherly-sama! Hold on tight!", "У-Уэзерби-сама! Держитесь крепче!"),
23: ("So that's how it is... That she can bring her consciousness to the surface... I can't believe it.",
     "Так вот как… Она смогла вывести сознание на поверхность… Не верю."),
24: ("Damn, the shock has ruined my spell... Just when I needed it...",
     "Чёрт, от потрясения заклинание не выходит… Именно сейчас…"),
25: ("I'll put a stronger spell on Haruna later. One that keeps her consciousness under forever...",
     "Я наложу на Харуну более сильное заклинание позже. Такое, чтобы её сознание больше не выходило…"),
26: ("Like hell you will!", "Не выйдет!"),
27: ("You two... brace yourselves!", "Вы двое… готовьтесь!"),
28: ("Ugh! It's over, is it. Damn, I was so close...", "Ох! Кажется, конец. Чёрт, я была так близко…"),
29: ("Be quiet and let yourself be bound!", "Не двигайся и дай себя связать!"),
30: ("...", "…"),
31: ("Hah. It seems the roles have reversed, haven't they?", "Ха. Кажется, роли поменялись местами, да?"),
32: ("Now Saito and the others are chasing, and I'm the one cornered...",
     "Теперь Сайто и остальные преследуют, а я загнанная…"),
33: ("Then I'll play my part as the script demands.", "Тогда я сыграю свою роль, как велит сценарий."),
34: ("Wait, Weatherly!", "Стой, Уэзерби!"),
35: ("Farewell.", "Прощай."),
36: ("Weatherly!", "Уэзерби!"),
37: ("(W-Wait. From this height, she won't survive...)", "П-Подожди. С такой высоты она не выживет…"),
38: ("Weatherly-sama...", "Уэзерби-сама…"),
39: ("...", "…"),
40: ("Saito, this is a battle too. I'll use the power of Void. Watch Akina, all right?",
     "Сайто, это тоже битва. Я применю силу Пустоты. Присмотри за Акиной, ладно?"),
41: ("Ah...", "Аа…"),
42: ("Illusion!!", "Иллюзия!!"),
43: ("W-What! An entire aerial fleet out of the clouds...!", "Ч-Что! Целый воздушный флот из облаков…!"),
44: ("You don't mean that's an illusion!?", "Неужели это иллюзия!?"),
45: ("That's right... An entirely false fleet...", "Да… Совсем не настоящий флот…"),
46: ("The enemy soldiers are fleeing the cannons one after another.",
     "Вражеские солдаты один за другим разбегаются от орудий."),
47: ("Thank goodness... This battle is over... at last.", "Слава богу… Битва окончена… наконец."),
48: ("Ah... Louise, get some rest. Void takes a lot of mental energy, doesn't it?",
     "Аа… Луиза, отдохни. Пустота отнимает много сил, правда?"),
49: ("Mm, I will. Phew... I'm a little... tired.", "Мм, да. Фух… Я немножко… устала."),
50: ("Good work... Louise.", "Хорошо поработала… Луиза."),
51: ("Phew, being inside a castle really makes my shoulders stiff.",
     "Фух, в замке прямо плечи затекают."),
52: ("Well now, I wonder how Haruna's doing? Maybe it's Akina right now.",
     "Ну что ж, как Харуна? Впрочем, может, сейчас это Акина."),
53: ("This is confusing.", "Запутанно как-то."),
54: ("(Officially, Haruna became a palace maid. While acting as Akina's garden keeper, she resumed her maid training...)",
     "Официально Харуна стала горничной дворца. Исполняя обязанности садовницы при Акине, она возобновила обучение горничной…"),
55: ("(Rumor has it she spends most of her time destroying palace plates and vases...)",
     "Говорят, она в основном занята тем, что бьёт дворцовые тарелки и вазы…"),
56: ("(Even the Princess, who laughed at first, has lately been clutching her head...)",
     "Даже принцесса, что сначала смеялась, в последнее время держится за голову…"),
57: ("(Ah, a ponytail... Which means...)", "А, хвостик… Значит…"),
58: ("(So right now it's Akina...)", "Сейчас это Акина…"),
59: ("Hey, Akina. Doing well?", "Эй, Акина. Как дела?"),
60: ("...", "…"),
61: ("H-Hey, Saito.", "Й-Йо, Сайто."),
62: ("You're still wearing that stupid face, aren't you.", "Ты всё ещё с этой глупой рожей, да?"),
63: ("W-What's wrong? You're awfully worked up.", "Ч-Что случилось? Ты как-то слишком взвинчена."),
64: ("(I mean... your way of talking is strange.)", "То есть… ты говоришь как-то странно."),
65: ("R-Really? I'm always like this.", "П-Правда? Я всегда такая."),
66: ("Huh? You stopped saying 'atashi'?", "Эй? Ты перестала говорить «атаси»?"),
67: ("W-What are you talking about! I'm still me!", "Ч-Что ты несёшь! Я всё та же!"),
68: ("D-Don't say boring things. I have something important to tell you today!",
     "Н-Не говори ерунды. У меня сегодня важный разговор!"),
69: ("Important?", "Важный?"),
70: ("T-That's right! Important!", "Т-Точно! Важный!"),
71: ("Ouch! If it's important, don't shove me down all of a sudden...",
     "Ой! Если важный, то не вали меня вдруг на пол…"),
72: ("(Akina's body is right against me... Damn. Why is my heart racing...)",
     "Акина прямо рядом… Чёрт. Почему сердце колотится…"),
73: ("Hurry up and propose to Haruna!", "Скажи Харуне, что хочешь жениться, прямо сейчас!"),
74: ("Ah, propose to...", "Аа, жениться…"),
75: ("...", "…"),
76: ("...", "…"),
77: ("...Kyukon?", "…Кюкон?"),
78: ("Um, Akina-san? What's a 'Kyukon'?", "Э-Э, Акина-сан? Что такое «Кюкон»?"),
79: ("W-What's that! It's obvious, isn't it!", "Ч-Что это! Неужели не ясно!"),
80: ("A proposal! A proposal!", "Предложение! Предложение!"),
81: ("In other words, I love you!", "Иными словами — ты любишь меня!"),
82: ("...", "…"),
83: ("...Huh?", "…А?"),
84: ("Um, I'm not following the conversation at all...", "Э-Э, я совсем не понимаю, о чём речь…"),
85: ("(No, it's not that I don't understand. Akina's still too out there...)",
     "Нет, дело не в этом. Акина по-прежнему слишком странная…"),
86: ("...Idiot! That's why Louise calls you a stupid dog.",
     "…Непроницательный! Поэтому Луиза и зовёт тебя глупым пёсом."),
87: ("All right, listen...", "Ладно, слушай…"),
88: ("H-Haruna likes Hiraga-kun... I mean, Saito. That's why she's waiting so faithfully.",
     "Х-Харуне нравится Хирага-кун… то есть Сайто. Поэтому она так верно ждёт."),
89: ("For you... for Saito to propose 'marriage'.", "Пока ты… Сайто не предложишь ей «женитьбу»."),
90: ("T-That's quite a joke.", "Т-Что за шутка такая."),
91: ("...And why marriage all of a sudden?", "…И почему вдруг женитьба?"),
92: ("W-We're high school students, you know.", "М-Мы же школьники, вообще-то."),
93: ("But there are lots of rivals... and Mama said you can't even hold hands unless you're married!",
     "Но соперниц много… и мама говорила, что без брака даже руку держать нельзя!"),
94: ("A-Anyway! This is Haruna's wish!", "В-В общем! Это желание Харуны!"),
95: ("I-It's not like people do that these days...", "Н-Ну сейчас так уже не делают…"),
96: ("Haruna said she was a lady before, you know. Maybe she's for real?",
     "Харуна раньше говорила, что она юная леди. Может, это правда?"),
97: ("(Something's been off since a while ago...)", "Что-то не так уже давно…"),
98: ("(Ah, now that I think of it... Akina or Haruna...)", "А, кстати… Акина или Харуна…"),
99: ("(Like when she broke a precious plate and pretended to switch personalities to cover it up...)",
     "Как та раз, когда разбила драгоценную тарелку и притворилась сменой личности, чтобы скрыть…"),
100: ("(Or when we split sweets and she switched so she'd get two shares...)",
      "Или когда делили сладости — она переключалась и брала две порции…"),
101: ("(I heard such funny stories from the maids...)", "Я слышал такие забавные истории от горничных…"),
102: ("N-No way...", "Н-Не может быть…"),
103: ("S-So that really was Haruna's wish?", "Т-Так это и правда желание Харуны?"),
104: ("Maybe it was Akina's...", "Может, это было Акины…"),
105: ("T-That's not true! Akina may want it too, but so do I!", "Н-Неправда! Акина тоже хочет, но и я!"),
106: ("...Huh?", "…А?"),
107: ("...Eh?", "…А?"),
108: ("...", "…"),
109: ("...T-That's mean! Disguising yourself as me and saying whatever you like!",
     "…П-Подло! Притворилась мной и говорила что вздумалось!"),
110: ("...Huh?", "…А?"),
111: ("T-No, just now it was Haruna pretending to be me.", "Н-Нет, сейчас это Харуна притворилась мной."),
112: ("Hold on, what's going on here!", "Постой, что здесь происходит!"),
113: ("This Akina is the real one, right!?", "Эта Акина — настоящая, да!?"),
114: ("Which one is which!?", "Кто из них кто!?"),
115: ("...Really Akina?", "…И правда Акина?"),
116: ("Don't tell me it's Haruna...?", "Неужели это Харуна…?"),
117: ("...", "…"),
118: ("...Ah, Akina! What are you doing saying such things!", "…Ах, Акина! Что ты такое говоришь!"),
119: ("...E-Er...?", "…Э-Э…?"),
120: ("S-Sorry, Hiraga-kun. Akina said something stupid!", "П-Прости, Хирага-кун. Акина наговорила глупостей!"),
121: ("A-Akina likes Hiraga-kun too. That's why she said that...",
     "А-Акина тоже любит Хирага-куна. Поэтому она так и сказала…"),
122: ("I-Is that so...", "Т-Так вот как…"),
123: ("Y-Yes. Ahahaha...", "Д-Да. А-ха-ха…"),
124: ("...Who are you really?", "…Кто ты на самом деле?"),
125: ("Ugh, er... au au... It's Touch.", "Ой, э-э… ау-ау… Это «Тач»."),
126: ("E-Er...", "Э-Э…"),
127: ("...Could it be a third personality, 'Fuyuna'?", "…Может, это третья личность — «Фуюна»?"),
128: ("That's it, that's it!", "Вот-вот, это оно!"),
129: ("C-Come on, enough alreadyyy!", "Н-Ну хватит уже-е!"),
130: ("Honestly, really!", "Ну и ну!"),
131: ("Hey, you two! Sitting next to us, talking about proposals and whatnot...",
     "Эй, вы двое! Сидите рядом и говорите про женитьбу всякое…"),
132: ("Let me tell you, I won't allow that—I'm the stupid dog's mistress!",
     "Знайте, я такого не позволю — я всё-таки госпожа глупого пса!"),
133: ("W-What!?", "Ч-Что!?"),
134: ("W-What!?", "Ч-Что!?"),
135: ("My my, it seems the battle of the sexes has only just begun.",
     "Ой-ой, кажется, женская битва только начинается."),
136: ("Spare me...", "Пощадите…"),
}
CHOICES = {
539: [("Is it really Akina's wish?", "Это и правда желание Акины?"),
      ("Is it really Haruna?", "Это и правда Харуна?"),
      ("Who is it really?", "Кто это на самом деле?")],
}
SPK = {'サイト': 's', 'アキナ': 'ak', 'ウェザリー': 'w', 'ハルナ': 'ha',
       'ルイズ': 'l', 'アンリエッタ': 'h', 'null': 'th'}
START = {'s': 64, 'ak': 48, 'w': 2, 'ha': 19, 'l': 67, 'h': 14, 'th': 2}


def main():
    data = json.load(open('reports/ch12/parse_535_548.json', encoding='utf-8'))
    script = ['# Глава 12, часть 3 (сцены 535–543): разоблачение, иллюзия, «женитьба».',
              '# Источник: ps2_source/chapters/chapter_13_もう一人のハルナ.txt (SCENE 535-543).',
              '', 'label ch12_3:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    no_audio = []
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 543:
                break
            scene = x['no']
            script += ['label ch12_3_scene_%d:' % scene, '']
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
            tag = 'ch12_%s_%03d' % (spk, counters[spk])
            full = '%s{#%s}' % (en, tag)
            script.append('    # ' + x['src'])
            if x['voice'] == 0:
                no_audio.append((tag, x['voice']))
                script.append('    # voice id 0 — нет аудио, строка voice пропущена')
            elif x['voice'] is not None:
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
                ctext = '%s{#ch12_3_c_%d_%d}' % (en_norm(en), scene, i + 1)
                tgt = ('ch12_3_scene_%d' % o['target']
                       if 535 <= o['target'] <= 543 else 'ch12_4')
                script.append('        "%s":' % ctext)
                script.append('            jump %s' % tgt)
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            tgt = ('ch12_3_scene_%d' % x['target']
                   if 535 <= x['target'] <= 543 else 'ch12_4')
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % tgt)
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 3 ====', '    jump ch12_4', '    return', '']
    files = {
        'game/chapters/12/script-ch12_3.rpy': '\n'.join(script) + '\n',
        'game/chapters/12/script-ch12_4.rpy':
            '# Глава 12, часть 4 (сцены 544–548): заглушка.\n\n'
            'label ch12_4:\n    $ tndl(None)\n    jump attention\n    return\n',
        'game/tl/japanese/ch12_3_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch12_3_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch12_3_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch12_3_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch12/voice_map_3.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), 'no_audio', no_audio, counters)


if __name__ == '__main__':
    main()
