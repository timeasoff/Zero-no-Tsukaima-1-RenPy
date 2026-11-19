#!/usr/bin/env python3
"""Chapter 25 part 1 (scenes 903-917): a letter arrives for Tabitha."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("(Several days have passed since the play ended. We still have no clue about the bomber.)",
    "Прошло несколько дней с тех пор, как закончился спектакль. У нас всё ещё нет ни следа бомбиста."),
1: ("(I keep investigating, but I can't get any solid information. Louise is getting irritable, too...)",
    "Я продолжаю расследовать, но не могу добиться никаких существенных данных. Луиза тоже становится раздражительной…"),
2: ("(I was right to send Guiche and Montmorency home.)", "Я правильно поступил, отослав Гиша и Монморанси домой."),
3: ("(But how long will this go on...?)", "Но как долго это будет продолжаться…?"),
4: ("Hey, Louise. We've been in Tristain for days now—is this really okay?",
    "Слушай, Луиза. Мы уже много дней в Тристании — это нормально?"),
5: ("What do you expect? We can't find any solid clue about the bomber.",
    "Что я должна делать? Мы не можем найти ни одной зацепки о бомбисте."),
6: ("No, I mean—if there's no clue, we should at least search more seriously...",
    "Нет, я хочу сказать — если нет зацепки, надо хотя бы искать серьёзнее…"),
7: ("Then go look for one.", "Тогда иди ищи."),
8: ("Where?", "Где?"),
9: ("How should I know?", "Откуда мне знать?"),
10: ("Well, I suppose...", "Ну, в принципе…"),
11: ("What is it? Go find that clue already.", "Что? Иди же ищи ту зацепку."),
12: ("Ugh...", "Ох…"),
13: ("In that case, I'll help Saito-san search for clues, too...",
    "В таком случае я тоже помогу Сайто-сан искать зацепки…"),
14: ("Eh, really!? You really are kind, Siesta.", "А, правда!? Ты и правда добрая, Сиэста."),
15: ("Then I'll come, too.", "Тогда и я пойду."),
16: ("Even Haruna... How lucky I am to have such kind classmates.",
    "Даже Харуна… Как же мне повезло с такими добрыми одноклассницами."),
17: ("If darling is going, I'll follow him anywhere.", "Если дорогой идёт, я пойду за ним куда угодно."),
18: ("Emergency evacuation.", "Экстренная эвакуация."),
19: ("Hey, what's the big idea!? Leaving me out like that!", "Эй, что за дела!? Меня одну оставляете!"),
20: ("Louise-san overworks Hiraga-kun!", "Луиза-сан слишком перегружает Хирага-куна!"),
21: ("That's right. Could you treat him a little more kindly...?", "Верно. Могли бы вы обращаться с ним немного мягче…?"),
22: ("Because a familiar is a familiar! Nothing more, nothing less!",
     "Потому что фамильяр — это фамильяр! Не больше и не меньше!"),
23: ("(Whatever you say, they're all just frustrated about having no clues...)",
     "Что бы ни говорили, они все просто раздражены из-за отсутствия зацепок…"),
24: ("Hmm? What's this? A letter slipped under the door...", "Хм? Что это? Письмо под дверью…"),
25: ("Eh, a letter? From whom?", "А, письмо? От кого?"),
26: ("Beats me... I can't read this script. It's probably not addressed to you, Louise?",
     "Понятия не имею… Я не могу прочесть эти иероглифы. Наверное, оно не тебе, Луиза?"),
27: ("Show it here. Honestly, learn to read at least writing, would you?",
     "Дай сюда. Право, научись хоть читать, что ли."),
28: ("Yes, yes, mistress.", "Да-да, госпожа."),
29: ("This isn't addressed to me. It's to Tabitha.", "Оно не мне. Оно Табасе."),
30: ("...", "…"),
31: ("Even so, having a letter delivered to our lodgings while we're away from home... "
     "It must be urgent.", "И всё же — письмо доставлено в нашу гостиницу, хотя мы вдали от дома… "
     "Должно быть, срочно."),
32: ("...", "…"),
33: ("...", "…"),
34: ("...Huh? What's wrong, Tabitha? You look gloomy.", "…А? Что случилось, Табаса? У тебя мрачный вид."),
35: ("...", "…"),
36: ("Hey, Tabitha. That letter—could it be...", "Эй, Табаса. Это письмо — неужто…"),
37: ("...Mm.", "…Мм."),
38: ("Hmm? Something happened?", "Хм? Что-то случилось?"),
39: ("Actually... Tabitha is highly skilled—skilled enough to hold the title of Chevalier.",
     "Дело в том… Табаса очень искусна — настолько, что имеет звание шевалье."),
40: ("(The title of Chevalier... What kind of title is that?)", "Звание шевалье… Что это за звание?"),
41: ("I thought Tabitha was a mage, but she's a knight? So 'Chevalier' is a knight's title, right?",
     "Я думал, Табаса маг, а она рыцарь? Значит, «шевалье» — рыцарское звание, да?"),
42: ("Saito...", "Сайто…"),
43: ("Darling...", "Дорогой…"),
44: ("Eh, eh!? Why are you both looking at me like that!?", "А, а!? С чего вы оба так остолбенели!?"),
45: ("A 'Chevalier' is a title granted to those who've achieved great deeds.",
     "«Шевалье» — звание, которое дают за выдающиеся заслуги."),
46: ("I see.", "Понятно."),
47: ("Actually... She was a cook, perhaps?", "Вообще-то… Может, она была поваром?"),
48: ("...What are you talking about, you?", "…О чём ты это, ты?"),
49: ("Eh? Am I wrong? Isn't 'Chevalier' a cook's title?", "А? Я неправ? Разве «шевалье» — звание повара?"),
50: ("Not remotely!", "Совсем нет!"),
51: ("A 'Chevalier' is a title granted to those who've achieved great deeds.",
     "«Шевалье» — звание, которое дают за выдающиеся заслуги."),
52: ("Ha ha, so that's it...", "Ха-ха, вот как…"),
53: ("Could it be a mage's title, then?", "Тогда, может, это звание мага?"),
54: ("Hmm. It's not exactly right, but not completely wrong, either.",
     "Хм. Не совсем верно, но и не совсем неверно."),
55: ("A 'Chevalier' is a title granted to those who've achieved great deeds.",
     "«Шевалье» — звание, которое дают за выдающиеся заслуги."),
56: ("Huh.", "Ого."),
57: ("Which means... Tabitha did something to earn such a title?", "Значит… Табаса совершила что-то, "
     "достойное такого звания?"),
58: ("That's right. Tabitha is amazing!", "Верно. Табаса удивительная!"),
59: ("Wow, impressive.", "Ого, впечатляет."),
60: ("...", "…"),
61: ("So—is Tabitha's Chevalier title connected to this letter somehow?",
     "Так… звание Табасы и это письмо как-то связаны?"),
62: ("Actually, Tabitha gets requests for missions from a certain country from time to time...",
     "Дело в том, что к Табасе каждый раз обращаются с заданиями из одной страны…"),
63: ("But?", "Но?"),
64: ("...", "…"),
65: ("...", "…"),
66: ("The missions are extremely difficult. They're the kind only Tabitha could pull off.",
     "Задания очень сложные. Такие, что справиться с ними может только Табаса."),
67: ("Wait—is this mission difficult, too?", "Погоди — и это задание сложное?"),
68: ("...", "…"),
69: ("Say, Tabitha. If you don't mind, could you tell me what's in that letter, too?",
     "Слушай, Табаса. Если не против, можешь рассказать мне, что в этом письме?"),
70: ("Maybe I could be of some help.", "Может, я смогу чем-нибудь помочь."),
71: ("...", "…"),
72: ("Ah, Tabitha...", "Ах, Табаса…"),
73: ("She left...", "Она ушла…"),
74: ("Maybe asking about that letter was a mistake, wasn't it?", "Может, спрашивать об этом письме было ошибкой?"),
75: ("Of course it was. It's a mission. She didn't want us to know.",
     "Конечно. Это же задание. Она не хотела, чтобы мы знали."),
76: ("...Hey, Kirche. Why do you get so gloomy over Tabitha?", "…Эй, Кирке. Почему ты так мрачнеешь из-за Табасы?"),
77: ("I-I'm not gloomy at all...", "Я-Я совсем не мрачная…"),
78: ("Looks like there's a complicated story there. Doesn't it interest you, Saito?",
     "Похоже, там сложная история. Тебе это не интересно, Сайто?"),
79: ("Well, I suppose I am a little curious...", "Ну, мне тоже немного интересно…"),
80: ("Right? Saito's curious, too, isn't he?", "Верно? Сайто тоже интересно, да?"),
81: ("But, people have their own circumstances...", "Но у людей бывают свои обстоятельства…"),
82: ("What are you talking about? Tabitha is our classmate and friend! "
     "Of course you'd worry about her!", "О чём ты? Табаса наша одноклассница и подруга! "
     "Конечно, ты волнуешься за неё!"),
83: ("No, I mean... I don't really care.", "Нет, я хотел сказать… Мне всё равно."),
84: ("You don't care... You're so cold.", "Тебе всё равно… Какой же ты холодный."),
85: ("Darling.", "Дорогой."),
86: ("Hmm?", "Хм?"),
87: ("Can I ask you a favor?", "Можно тебя попросить об одолжении?"),
88: ("If it's not something impossible...", "Если только это не что-то невозможное…"),
89: ("I want you to ask Tabitha about that letter. I'm just... worried.",
     "Я хочу, чтобы ты спросил Табасу об этом письме. Я просто… волнуюсь."),
90: ("Me?", "Я?"),
91: ("Why Saito?", "Почему Сайто?"),
92: ("Hmm. Women's intuition, maybe?", "Хм. Может, женская интуиция?"),
93: ("Darling, you've gotten close to Tabitha lately, haven't you?",
     "Дорогой, ты в последнее время сблизился с Табасой, да?"),
94: ("Eep.", "Ой."),
95: ("She may be quiet and you may think I can't tell, but I can see it perfectly well.",
     "Она молчаливая, и ты, наверное, думаешь, что я не замечу — но я всё прекрасно вижу."),
96: ("Wh-What was that!? You like small ones, don't you!", "Ч-Что ты сказала!? Тебе нравятся маленькие, да!"),
97: ("I-Is that true, Saito-san?", "П-Правда ли это, Сайто-сан?"),
98: ("N-No, it's a misunderstanding!", "Н-Нет, это недоразумение!"),
99: ("Well, we can question you about that later. For now, Tabitha is the priority.",
     "Ну, потом допросим тебя по этому поводу. Сейчас важнее Табаса."),
100: ("I-Understood. There's one thing I can't accept, but you're right—Saito is the right person for this.",
      "П-Понятно. Есть одна вещь, с которой я не согласна, но ты права — Сайто здесь подходит лучше всех."),
101: ("Saito, go check on Tabitha. Understand? That's an order. Don't come back empty-handed.",
      "Сайто, сходи проверь Табасу. Понял? Это приказ. Не возвращайся без результатов."),
102: ("Yes, yes...", "Да-да…"),
103: ("Tabitha... Where did she go?", "Табаса… Куда она пошла?"),
104: ("...Oh, I found her easily.", "…А, я легко её нашёл."),
105: ("...", "…"),
106: ("Well, there's no point overthinking it. For now, let me call out to her.",
     "Ну, нет смысла слишком думать. Пока что окликну её."),
107: ("Hey there, Tabitha~.", "Эй, Табаса~."),
108: ("I'll leave her alone for a while. She must have her own way of sorting out her feelings...",
     "Оставлю её пока в покое. У неё наверняка свой способ разобраться с чувствами…"),
109: ("...No, this won't do. If I go back like this, Louise will beat me to death.",
     "…Нет, так не пойдёт. Если я вернусь вот так, Луиза меня изобьёт до смерти."),
110: ("Hey there, Tabitha~.", "Эй, Табаса~."),
111: ("What was in that letter? Something that made Tabitha run out of the room?",
     "Что было в том письме? Что-то, из-за чего Табаса выбежала из комнаты?"),
112: ("Something painful? Something sad? Something difficult?", "Болезненное? Грустное? Сложное?"),
113: ("...", "…"),
114: ("...", "…"),
115: ("Well, thinking won't give me an answer. Let me just ask her directly.",
     "Ну, размышления не дадут ответа. Спрошу её напрямую."),
116: ("Hey there, Tabitha~.", "Эй, Табаса~."),
117: ("What?", "Что?"),
118: ("Um, Tabitha-san.", "Э-Э, Табаса-сан."),
119: ("...", "…"),
120: ("Um, I was hoping you could tell me about that letter...", "Э-Э, я надеялся, что ты расскажешь мне об этом письме…"),
121: ("...", "…"),
122: ("Ah ha ha ha ha...", "А-ха-ха-ха-ха…"),
123: ("...", "…"),
124: ("Um, even just one word would be fine—please just react somehow...",
     "Э-Э, хоть одним словом — просто отреагируй как-нибудь…"),
125: ("...", "…"),
126: ("N-No?", "Н-Нет?"),
127: ("All right. I'll talk.", "Ладно. Я расскажу."),
128: ("Great... So first...", "Отлично… Так, сперва…"),
129: ("I need time.", "Мне нужно время."),
130: ("Fine, but why?", "Хорошо, но почему?"),
131: ("Time.", "Время."),
132: ("O-Okay...", "Л-Ладно…"),
133: ("Then.", "Тогда."),
134: ("Wait—and she walked off somewhere!!", "Погоди — и она куда-то ушла!!"),
}
CHOICES = {
903: [("A knight's title?", "Рыцарское звание?"),
      ("A chef's title?", "Звание повара?"),
      ("A mage's title?", "Звание мага?")],
908: [("I am a little curious", "Мне тоже немного интересно"),
      ("Everyone has their reasons", "У всех свои причины"),
      ("Not really", "Мне всё равно")],
913: [("Call out to her", "Окликнуть её"),
      ("Leave her alone", "Оставить в покое"),
      ("What was that letter?", "Что это было за письмо?")],
}
SPK = {'サイト': 's', 'ルイズ': 'l', 'シエスタ': 'si', 'ハルナ': 'ha',
       'キュルケ': 'k', 'タバサ': 't', 'null': 'th'}
START = {'s': 0, 'l': 0, 'si': 0, 'ha': 0, 'k': 0, 't': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch25/parse_903_933.json', encoding='utf-8'))
    script = ['# Глава 25, часть 1 (сцены 903–917): письмо для Табасы.',
              '# Источник: ps2_source/chapters/chapter_26_手紙の秘密.txt (SCENE 903-917).',
              '', 'label ch25:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 917: break
            scene = x['no']
            script += ['label ch25_1_scene_%d:' % scene, '']
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
            tag = 'ch25_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch25_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch25_1_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 903 <= scene <= 917: continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch25_1_scene_%d' % x['target'] if 903 <= x['target'] <= 917 else 'ch25_2'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch25_2', '    return', '']
    files = {
        'game/chapters/25/script-ch25.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch25_1_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch25_1_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch25_1_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch25_1_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch25/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
