#!/usr/bin/env python3
"""Chapter 15 part 1 (scenes 619-632): morning, Akina's revelation."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("Ugh...", "Фух…"),
1: ("Onii~chan!", "Братишшаа!"),
2: ("Good morning!", "Доброе утро!"),
3: ("Whoa, Kirche! G-Good morning.", "Ого, Кирке! Д-Доброе утро."),
4: ("Big brother, did you sleep well?", "Братишка, ты хорошо выспался?"),
5: ("Uuuun?", "Ууу?"),
6: ("Yeah, I slept well. Slept like a log.", "Да, выспался. Спал крепко."),
7: ("Really! Kirche slept well too.", "Правда! Кирке тоже хорошо выспалась."),
8: ("It's because I was with big brother! Let's sleep together again tonight!",
    "Это потому что я была с братишкой! Давай сегодня снова спать вместе!"),
9: ("Wait, you were with me?", "Это что, я был с тобой?"),
10: ("Mm. At night I got scared, and when I went to big brother...",
     "Мм. Ночью мне стало страшно, и я пошла к братишке…"),
11: ("And you held me tight... Big brother was so warm...",
     "И ты меня крепко обнял… Братишка был такой тёплый…"),
12: ("Ha, haha...", "Ха, ха-ха…"),
13: ("I feel like I had a strange dream...", "Кажется, я видел странный сон…"),
14: ("A dream? What kind? Was Kirche in it?", "Сон? Какой? Кирке там была?"),
15: ("Uuu... I don't remember the details at all...", "Ууу… Я совсем не помню подробностей…"),
16: ("Buuu! Boring. Tonight, dream of Kirche!", "Бууу! Скучно. Сегодня снись Кирке!"),
17: ("Hahaha. Sorry, sorry.", "Ха-ха-ха. Прости, прости."),
18: ("Um, Kirche-san?", "Э-Э, Кирке-сан?"),
19: ("Could you move just a little away from me?", "Можешь отодвинуться от меня хотя бы немного?"),
20: ("Ehh! Why?", "Эээ! Почему?"),
21: ("Big brother, did you stop liking Kirche?", "Братишка, ты больше не любишь Кирке?"),
22: ("T-That's not it, but...", "Я-Я не это, но…"),
23: ("I'm, um, a boy.", "Я, э-э, мальчик."),
24: ("???", "???"),
25: ("R-Right! More importantly!", "Т-Точно! Главное!"),
26: ("Wouldn't it be terrible if Louise found us like this!?", "Что будет, если Луиза увидит нас таких!?"),
27: ("If that happened...", "Если бы это случилось…"),
28: ("What do you think would happen?", "Как ты думаешь, что было бы?"),
29: ("W-Why, I'd be beaten to a pulp, torn to shreds, utterly wrecked...",
     "Н-Ну, меня бы поколотили, порвали на куски, разнесли в пух и прах…"),
30: ("Good morning, mistress.", "Доброе утро, госпожа."),
31: ("Shut up! It's no use making excuses now!", "Замолчи! Оправдываться сейчас бесполезно!"),
32: ("E-Eek!", "К-Кайн!"),
35: ("...", "…"),
36: ("Good morning, Kirche.", "Доброе утро, Кирке."),
37: ("...Morning.", "…Утро."),
38: ("You still don't warm up to me, do you... Are you all right? "
     "That stupid dog didn't do anything weird to you?",
     "Ты всё ещё не тянешься ко мне… Ты в порядке? Этот глупый пёс не сделал ничего странного?"),
39: ("B-But I told you, I didn't do anything!", "Н-Но я же говорю, я ничего не делал!"),
40: ("...I don't want to hurt big brother...", "…Я не хочу обижать братишку…"),
41: ("Really, are you actually Kirche?", "Ну же, ты и правда Кирке?"),
42: ("...It was a rough night.", "…Тяжёлая была ночь."),
43: ("Honestly, why does this keep happening to me...", "Ну же, почему это всё время со мной…"),
44: ("Say, Montmon. How's the medicine for Kirche's suggestion coming along?",
     "Слушай, Монмон. Как дела с лекарством от гипнотического внушения Кирке?"),
45: ("Not yet.", "Пока нет."),
46: ("I told you? It'll take some time.", "Я же говорила — займёт немного времени."),
47: ("I'd like it finished before my life ends, please.", "Хотелось бы, чтобы оно было готово, пока я жив."),
48: ("I'll try, but don't get your hopes up.", "Постараюсь, но не надейся слишком."),
49: ("Right now Tabitha is gathering the ingredients we're missing... but it depends on the result.",
     "Сейчас Табаса собирает недостающие ингредиенты… но всё зависит от результата."),
50: ("Eek!", "Ай!"),
51: ("W-What was that!", "Ч-Что это было!"),
52: ("Saito! That explosion just now!", "Сайто! Этот взрыв сейчас!"),
53: ("Damn. Is it the bomb-thrower again?", "Чёрт. Опять бомбист?"),
54: ("B-Big brother. What was that...?", "Б-Братишка. Что это было…?"),
55: ("A loud sound... and shaking...", "Громкий звук… и тряска…"),
56: ("Scary, so scary...", "Страшно, так страшно…"),
57: ("(Kirche...)", "Кирке…"),
58: ("Why are you spacing out! Hurry to the scene!", "Что ты застыл! Быстрее к месту взрыва!"),
59: ("O-Okay!", "Т-Так точно!"),
60: ("Burn, burn. Let it all burn!", "Гори, гори. Пусть всё горит!"),
61: ("Haha! Ahahahaha!", "Ха-ха! А-ха-ха-ха!"),
62: ("The city...", "Город…"),
63: ("What the hell are they doing!", "Что они, чёрт возьми, творят!"),
64: ("Saito, over there!", "Сайто, вон там!"),
65: ("Ahahaha, here they come!", "А-ха-ха, они идут!"),
66: ("Haruna!? It's dangerous there! Get over here!", "Харуна!? Там опасно! Иди сюда!"),
67: ("Hurry! It's dangerous!", "Быстрее! Опасно!"),
68: ("Ahahaha... Still the same naive fools!", "А-ха-ха… Всё такие же наивные дураки!"),
69: ("H-Haruna?", "Х-Харуна?"),
70: ("Careful, partner!", "Осторожно, приятель!"),
71: ("Don't call me Haruna!", "Не называй меня Харуной!"),
72: ("My name is 'Akina'...", "Моё имя — «Акина»…"),
73: ("The real me, made by Weatherly-sama!", "Настоящая я, созданная Уэзерби-самой!"),
74: ("W-What did you say!?", "Ч-Что ты сказала!?"),
75: ("You were lying to us from the start, weren't you?", "Ты с самого начала нам лгала, да?"),
76: ("Well, who knows. 'That girl' doesn't know anything...",
     "Ну, кто знает. «Та девочка» ничего не знает…"),
77: ("But I knew everything and pulled the strings. Yes, everything...",
     "Но я всё знала и тянула за ниточки. Да, всё…"),
78: ("It's a lie, you're a fake! I won't believe it!", "Это ложь, ты подделка! Я не поверю!"),
79: ("Oh, how sweet. She'll be happy when she hears that.", "Ой, как мило. Она обрадуется, когда услышит."),
80: ("And then she'll despair. When she learns what she did without knowing. Ahah, wonderful!",
     "А потом придёт отчаяние. Когда она узнает, что делала, сама не зная. А-ха, прекрасно!"),
81: ("What's that? I can't laugh at that. Come on, it's a sick joke, right?",
     "Что это? Мне не до смеха. Ну же, это больная шутка, да?"),
82: ("Oh, why? You have to accept reality.", "Ой, почему? Приходится принять реальность."),
83: ("Damn! You mean it was all set up from the beginning?",
     "Чёрт! Ты хочешь сказать, что всё было подстроено с самого начала?"),
84: ("That's right. From the very start.", "Верно. С самого начала."),
85: ("W-What's going on here!?", "Ч-Что здесь происходит!?"),
86: ("Hm. Too complicated for Louise, was it?", "Хм. Слишком сложно для Луизы, да?"),
87: ("So that's what the hypnosis on Kirche could do too, huh.",
     "Вот на что ещё годится гипноз, наложенный на Кирке."),
88: ("Oh, correct. Not so dumb after all, Saito.", "Ой, верно. Ты не такой уж тупой, Сайто."),
89: ("Don't toy with us! We were puppets from the start, weren't we!",
     "Не издевайся! Мы были марионетками с самого начала, да?"),
90: ("Kirche's deduction that I was connected to Weatherly wasn't bad, but she was just short.",
     "Догадка Кирке, что я связана с Уэзерби, была неплохой, но чуть-чуть не дотянула."),
91: ("The truth is, I was passing your information to Weatherly-sama...",
     "На самом деле я передавала ваши сведения Уэзерби-саме…"),
92: ("And then—boom. Ahahaha...", "А потом — бах. А-ха-ха…"),
93: ("Why tell us this now...", "Почему ты рассказываешь это сейчас…"),
94: ("The play is over.", "Спектакль окончен."),
95: ("The final act is about to begin. So, my regards.",
     "Сейчас начнётся последний акт. Поэтому — приветствие."),
96: ("See? Manners matter, don't they?", "Видишь? Хорошие манеры важны, правда?"),
97: ("Ahahaha, bye bye~~!", "А-ха-ха, пока-пока~~!"),
98: ("No... Haruna was the bomb-thrower...", "Неужели… Харуна была бомбистом…"),
99: ("No! Like Kirche, Haruna is just being controlled.", "Нет! Как и Кирке, Харуной просто управляют."),
100: ("Even so...", "Даже если так…"),
101: ("I'll stop Haruna myself.", "Я сам остановлю Харуну."),
102: ("...", "…"),
103: ("Fine, I understand, Saito. Do as you like.", "Ладно, я поняла, Сайто. Делай как хочешь."),
104: ("Eh, really? For real?", "А? Правда? Серьёзно?"),
105: ("According to 'Akina', Haruna herself doesn't know what she's done, right?",
     "По словам «Акины», сама Харуна не знает, что делала, верно?"),
106: ("So when she learns the truth and falls apart, you'll be there to catch her. "
     "That's an order from your mistress.",
     "Так что, когда она узнает правду и рухнет, ты её подхватишь. Это приказ госпожи."),
107: ("The one at fault is Weatherly.", "Виновата Уэзерби."),
108: ("A traveling troupe's leader, my foot—what a fraud she turned out to be.",
     "«Главарь бродячей труппы», как же — какая же она шарлатанка."),
109: ("Kirche said before she was attacked.", "Кирке сказала перед тем, как её атаковали."),
110: ("That behind Weatherly there might be someone much bigger.",
     "Что за Уэзерби может стоять кто-то покрупнее."),
111: ("In the end, Kirche was closest to the truth.", "В итоге Кирке ближе всех подошла к правде."),
112: ("What's wrong, big brother?", "Что случилось, братишка?"),
113: ("It's nothing, Kirche. I was just praising you—you're smart.",
     "Ничего, Кирке. Я просто хвалил тебя — ты умная."),
114: ("Yes. Though it's bitter.", "Да. Хоть и горько."),
115: ("So that's why she wanted to use us so much during the performance.",
     "Так вот почему она так хотела использовать нас во время спектакля."),
116: ("Yes, that's why she bossed us around so much.", "Да, поэтому она так командовала нами."),
117: ("Hm... Should I let that muscle ache grudge go?", "Хм… Стоит ли мне простить ту боль в мышцах?"),
118: ("Wait a second, Louise! You're angry about the wrong thing!",
     "Подожди, Луиза! Ты злишься не на то!"),
119: ("I don't care! I'm furious right now!", "Мне всё равно! Я сейчас очень зла!"),
}
CHOICES = {
619: [("I slept well", "Выспался хорошо"),
      ("I feel like I had a weird dream", "Кажется, я видел странный сон"),
      ("Um, Kirche... could you move a little away?", "Э-Э, Кирке… можно отодвинуться немного?")],
624: [("You've been lying to us all along?", "Ты всё это время нам лгала?"),
      ("It's a lie, you're a fake! I don't believe it!", "Это ложь, ты подделка! Я не верю!"),
      ("A sick joke, right?", "Это больная шутка, да?")],
629: [("I'll stop Haruna myself", "Я сам остановлю Харуну"),
      ("Weatherly...", "Уэзерби…"),
      ("So that's why the performance...", "Так поэтому на представлении…")],
}
SPK = {'サイト': 's', 'キュルケ': 'k', 'ルイズ': 'l', 'モンモランシー': 'm',
       'アキナ': 'ak', 'デルフリンガー': 'd', 'null': 'th'}
START = {k: 0 for k in SPK.values()}


def main():
    data = json.load(open('reports/ch15/parse_619_659.json', encoding='utf-8'))
    script = ['# Глава 15, часть 1 (сцены 619–632): утро, разоблачение Акины.',
              '# Источник: ps2_source/chapters/chapter_16_魔法の薬.txt (SCENE 619-632).',
              '', 'label ch15:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 632:
                break
            scene = x['no']
            script += ['label ch15_1_scene_%d:' % scene, '']
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
            tag = 'ch15_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch15_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                tgt = ('ch15_1_scene_%d' % o['target']
                       if 619 <= o['target'] <= 632 else 'ch15_2')
                script.append('        "%s":' % ctext)
                script.append('            jump %s' % tgt)
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 619 <= scene <= 632:
                continue
            tgt = ('ch15_1_scene_%d' % x['target']
                   if 619 <= x['target'] <= 632 else 'ch15_2')
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % tgt)
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch15_2', '    return', '']
    files = {
        'game/chapters/15/script-ch15_1.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch15_1_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch15_1_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch15_1_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch15_1_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch15/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
