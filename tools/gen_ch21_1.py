#!/usr/bin/env python3
"""Chapter 21 part 1 (scenes 771-779): Siesta becomes Louise's maid."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("(A few days have passed since the play ended. Suddenly, the bomber stopped showing up.)",
    "Прошло несколько дней с тех пор, как закончился спектакль. И вдруг бомбист перестал появляться."),
1: ("(So we all ended up returning to the magic academy, but...)",
    "Так что мы все вернулись в академию магии, но…"),
2: ("(Since we got no real results and still don't know who the bomber is, everyone's on edge.)",
    "Из-за того, что мы не добились результатов и так и не выяснили, кто такой бомбист, все сильно нервничают."),
3: ("I still can't accept it! What was that bomber, suddenly vanishing like that!",
    "Я всё равно не могу смириться! Что это за бомбист — вдруг взял и исчез!"),
4: ("How am I supposed to deal with the humiliation I suffered!", "Как мне быть с позором, который я пережила!"),
5: ("You're a sore loser, really. What's the point of regretting something that's over?",
    "Ты и правда не умеешь проигрывать. Зачем жалеть о том, что уже прошло?"),
6: ("What was that!?", "Что ты сказала!?"),
7: ("Look on the bright side. You'll go bald from worrying.",
    "Смотри на вещи позитивнее. От такого напряжения ты лысеешь."),
8: ("Wha—! Kirche!?", "Ах! Кирке!?"),
9: ("Hey, calm down, Louise!! Are you trying to blow up the room!?",
    "Эй, успокойся, Луиза!! Ты что, хочешь взорвать комнату!?"),
10: ("Darling, why don't you quit being that short-tempered Louise's familiar and become mine instead?",
    "Дорогой, а почему бы тебе не бросить быть фамильяром такой вспыльчивой Луизы и не стать моим?"),
11: ("Don't you dare hug Saito in the confusion!", "Не смей обнимать Сайто в этой суматохе!"),
12: ("Wah!", "Ой!"),
13: ("(Honestly, both Louise and Kirche... Fighting won't get us anywhere, will it?)",
    "Честно, и Луиза, и Кирке… Ссора ни к чему не приведёт, правда?"),
14: ("...", "…"),
15: ("(Siesta? What's wrong with her... She's been standing there frozen...)",
    "Сиэста? Что с ней… Она всё время стоит как замерзшая…"),
16: ("Siesta, what's wrong?", "Сиэста, что случилось?"),
17: ("Eep!", "Ай!"),
18: ("Ah, sorry! I didn't mean to startle you.", "Ах, прости! Я не хотел тебя напугать."),
19: ("N-No, I'm the one who got startled, sorry.", "Н-Нет, это я испугалась, простите."),
20: ("What's wrong? You've been spacing out this whole time.", "Что случилось? Ты всё время отключаешься."),
21: ("A-Ah, that's right. I was just about to bring the cake and tea.",
    "А-А, точно. Я как раз несла торт и чай."),
22: ("Well then, excuse me, Saito-san.", "Тогда извините, Сайто-сан."),
23: ("A, okay.", "А, ладно."),
24: ("(What's wrong with Siesta?... Did she take the tea to Guiche and Montmorency's table?)",
    "Что с Сиэстой… Она отнесла чай к столу Гиша и Монморанси?"),
25: ("Sorry to keep you waiting. I've brought your tea and cake.",
    "Простите за ожидание. Я принесла чай и торт."),
26: ("Ah, thanks. Pour the tea from her cup, would you?", "Ах, спасибо. Налей чай из её чашки."),
27: ("Yes, certainly.", "Да, конечно."),
28: ("...", "…"),
29: ("Kyaaa! Oh no, the tea!", "Кья-а! Ой, чай!"),
30: ("Ahh!! Montmorency! What are you doing, girl!?", "Ах!! Монморанси! Что ты делаешь, девочка!?"),
31: ("Eh? Ah!", "А? Ах!"),
32: ("I-I'm terribly sorry!!", "П-Простите, мне очень жаль!!"),
33: ("Oh no. Did you burn yourself, Montmorency?", "Ох. Ты не обожглася, Монморанси?"),
34: ("Really, my uniform is ruined.", "Ну всё, форма испорчена."),
35: ("I'm so sorry! I'll wipe it right away and bring you a new one!",
    "Мне очень жаль! Я сейчас же вытру и принесу новую!"),
36: ("(Ah, I can't watch this! I'll go over!)", "Ах, я не могу смотреть! Пойду-ка я!"),
37: ("Are you all right, Siesta? Did you burn yourself?", "Ты в порядке, Сиэста? Не обожглась?"),
38: ("Hey! I'm the one who got the tea on me! You've got the wrong person to worry about!",
    "Эй! Это меня облили чаем! Ты не туда смотришь!"),
39: ("Ah, Montmorency, sorry. Siesta seems a bit tired.", "Ах, Монморанси, прости. Сиэста, похоже, немного устала."),
40: ("Ah... No, really, Saito-san, apologizing... It's my carelessness, so... I'm sorry!",
    "Ах… Нет, правда, Сайто-сан, извиняйте… Это моя невнимательность, так что… простите!"),
41: ("Hmph, our tea time is ruined. I've lost all my appetite. Let's go, Montmorency.",
    "Хмф, наш чай испорчен. Аппетит пропал. Идём, Монморанси."),
42: ("Right!", "Да!"),
43: ("I'm sorry. My mistake caused trouble for Saito-san too...",
    "Простите. Из-за моей ошибки и Сайто-сан досталось…"),
44: ("Cheer up, Siesta. What you failed at today, you can make up for tomorrow, right?",
    "Не падай духом, Сиэста. Что сегодня не получилось, то наверстаешь завтра, да?"),
45: ("Yes...", "Да…"),
46: ("But I... I've decided to take a few days off starting tomorrow.",
    "Но я… я решила на несколько дней взять отпуск начиная с завтрашнего дня."),
47: ("Eh!? Why?", "А!? Почему?"),
48: ("Actually, ever since I came back to the academy, I've been like this the whole time.",
    "Дело в том, что с тех пор, как я вернулась в академию, я всё это время была такой."),
49: ("They told me to refrain from my maid duties until I calm down.",
    "Мне сказали пока не исполнять обязанности горничной, пока я не успокоюсь."),
50: ("So I was thinking of going back to my family home to settle my mind a little.",
    "И я подумывала вернуться домой, чтобы немного успокоиться."),
51: ("No way... Telling you to take time off is going too far.", "Не может быть… Просить тебя взять отпуск — слишком."),
52: ("It's because I'm so inept...", "Это из-за моей неопытности…"),
53: ("Listen, Siesta. If I can help, I'll do anything. So don't say you'll leave the academy.",
    "Слушай, Сиэста. Если я могу помочь, я сделаю что угодно. Так что не говори, что уйдёшь из академии."),
54: ("Thank you very much...", "Спасибо вам большое…"),
55: ("...", "…"),
56: ("???", "???"),
57: ("Um... Saito-san. May I ask you to help me?", "Э-Э… Сайто-сан. Можно вас попросить о помощи?"),
58: ("Huh? Sure, but...", "А? Конечно, но…"),
59: ("Um... Um... Um!", "Э… Э… Э!"),
60: ("Um?", "Э?"),
61: ("Please make me your maid, Saito-san!", "Позвольте мне стать вашей горничной, Сайто-сан!"),
62: ("Eh?", "А?"),
63: ("I want to start over with you as my master and polish my skills as a servant again!",
    "Я хочу начать сначала, считая вас своим господином, и заново отточить мастерство прислуги!"),
64: ("M-Me, a master!? T-That is...", "Я-Я господин!? Т-Это…"),
65: ("No way! I won't allow it. Absolutely not!", "Ни в коем случае! Я не позволю. Ни за что!"),
66: ("L-Louise. Where were you listening from?", "Л-Луиза. Откуда ты всё это слышала?"),
67: ("From the very beginning. Siesta becoming Saito's maid is absolutely not allowed!",
    "С самого начала. Чтобы Сиэста стала горничной Сайто — ни в коем случае!"),
68: ("R-Right. So then...", "В-Верно. Тогда…"),
69: ("How about becoming Kirche's maid?", "Как насчёт того, чтобы стать горничной Кирке?"),
70: ("Don't be ridiculous!! That's out of the question!", "Не смешно!! Об этом не может быть и речи!"),
71: ("W-Why? If our place won't do, then what else can we do?", "П-Почему? Если у нас не выходит, что же ещё делать?"),
72: ("That's no reason to go running to Zerbst!", "Это не повод бежать к Церпст!"),
73: ("I don't think that's what this is about, but...", "Я не думаю, что дело в этом, но…"),
74: ("In any case, no!", "В любом случае, нет!"),
75: ("How about becoming Tabitha's maid?", "Как насчёт того, чтобы стать горничной Табасы?"),
76: ("Tabitha might be fine, don't you think?", "Табаса — нормально, правда?"),
77: ("E-Erm... But Miss Tabitha does everything for herself...",
    "Э-Э… Но мисс Табаса всё делает сама…"),
78: ("I don't think there's any need for me...", "Я думаю, во мне нет нужды…"),
79: ("Yeah. Tabitha can manage most things with magic.", "Да. Табаса большую часть делает магией."),
80: ("Sorry about that! I can't do everything with magic!", "Извини! Я не могу всё делать магией!"),
81: ("I didn't say that.", "Я такого не говорил."),
82: ("How about becoming Guiche's maid?", "Как насчёт того, чтобы стать горничной Гиша?"),
83: ("Eh...", "А…"),
84: ("Hey. Are you serious about that!?", "Эй. Ты это серьёзно!?"),
85: ("I-I am, but...", "Я-Я серьёзно, но…"),
86: ("Are you an idiot!? Think about Siesta a little more!", "Ты дурак!? Подумай хоть немного о Сиэсте!"),
87: ("Well, Guiche would be...", "Ну, Гиш это…"),
88: ("Sigh... I really do have to go back to my family home, don't I...", "Ох… Мне и правда придётся вернуться домой, да…"),
89: ("Louise...", "Луиза…"),
90: ("Ugh, fine! I get it! You can stay in my room!", "Ох, ладно! Поняла! Можешь остаться в моей комнате!"),
91: ("Wah, thank you so much! I'll work as hard as I can!", "Ох, спасибо вам огромное! Я буду стараться изо всех сил!"),
92: ("Instead, you'll be serving me, not taking care of Saito. That's fine with you, right?",
    "Вместо этого ты будешь прислуживать мне, а не заботиться о Сайто. Тебе подходит?"),
93: ("Yes, Miss Valliere. Please take care of me from now on.",
    "Да, мисс Вальер. Прошу заботиться обо мне и дальше."),
94: ("Well, that settles it for now, I guess?", "Ну, на этот раз вопрос решён, да?"),
95: ("Saito-san, thank you very much. From now on I'll do my best to become a true maid.",
    "Сайто-сан, спасибо вам большое. Сейчас я сделаю всё, чтобы стать настоящей горничной."),
96: ("(And so, Siesta began serving Louise.)", "Так Сиэста начала прислуживать Луизе."),
97: ("(A few more days passed quickly after Siesta became Louise's maid.)",
    "После того как Сиэста стала горничной Луизы, прошло ещё несколько дней."),
98: ("Hum hum hum hum~", "Хм-хм-хм-хм~"),
99: ("(Siesta seems to be in a great mood ever since she became Louise's maid...)",
    "Сиэста, похоже, в отличном настроении с тех пор, как стала горничной Луизы…"),
100: ("Saito-san, Haruna-san. I'm going to wipe the floor now, so please get up on the bed.",
     "Сайто-сан, Харуна-сан. Сейчас я буду мыть пол, так что поднимитесь, пожалуйста, на кровать."),
101: ("Mm, okay.", "Мм, ладно."),
102: ("All right. Want me to help, too?", "Ладно. Может, мне помочь?"),
103: ("No, not at all! This is my job as a maid. Saito-san, please just relax.",
     "Нет, что вы! Это моя работа как горничной. Сайто-сан, просто отдыхайте."),
104: ("Then, Siesta, we'll leave the rest to you. We're going out for a bit.",
     "Тогда, Сиэста, остальное поручаем тебе. Мы на время выйдем."),
105: ("Louise, are you going somewhere?", "Луиза, ты куда-то идёшь?"),
106: ("Could you come with me for a bit, Saito and Haruna?", "Не могли бы вы со мной на время, Сайто и Харуна?"),
107: ("Me too?", "И я?"),
108: ("Ah... Yes, certainly. Have a good outing, everyone!", "Ах… Да, конечно. Хорошо погуляйте, все!"),
109: ("Good morning, Tabitha. Sorry to intrude.", "Доброе утро, Табаса. Прости за вторжение."),
110: ("Good morning.", "Доброе утро."),
111: ("Yo, so Saito's joining us too?", "Йо, Сайто тоже с нами?"),
112: ("Really, you gathered everyone after all?", " Правда, ты собрала всех?"),
113: ("What is this, everyone's here! What's going on!?", "Что это, мы все здесь! Что происходит!?"),
114: ("Then let's start the emergency meeting. Topic: Siesta!", "Тогда начнём срочное совещание. Тема: Сиэста!"),
115: ("Did something happen to Siesta?", "С Сиэстой что-то случилось?"),
116: ("I don't know if you noticed, but Siesta hasn't been herself since she came back from the trip.",
     "Не знаю, заметил ли ты, но Сиэста была не в себе с тех пор, как вернулась из поездки."),
117: ("The academy giving her leave is good proof. She must have been quite unwell.",
     "То, что академия дала ей отпуск, — хорошее тому доказательство. Она была совсем не в порядке."),
118: ("I wasn't the only one she spilled tea on, it seems. No wonder she got scolded.",
     "Похоже, чаем она облила не только нас. Неудивительно, что её отругали."),
119: ("She seems fine now, though.", "Но сейчас она вроде в порядке."),
120: ("Oh, so the emergency meeting's over? What a letdown.", "О, так срочное совещание закончилось? Как скучно."),
121: ("We don't know the cause.", "Причина неизвестна."),
122: ("Right. We still don't know why Siesta was acting strange.", "Верно. Мы так и не выяснили, почему Сиэста вела себя странно."),
123: ("Well, but thanks to Siesta, Louise doesn't have to do her own laundry anymore— "
      "isn't that good for a noble?", "Ну, но благодаря Сиэсте Луизе больше не надо стирать самой — "
      "разве это не хорошо для дворянки?"),
124: ("W-Well, yes, that's true.", "Н-Ну, да, это правда."),
125: ("(No, you never did your own laundry before either...)", "Нет, ты и раньше не стирала…"),
126: ("We can manage anything with magic... But you... You wash by hand, don't you?",
     "Мы можем всё сделать магией… Но ты… ты стираешь руками, да?"),
127: ("Sh-Shut up, flood Montmorency! You're good with water magic, so you're fine, but I'm not!",
     "З-Замолчи, наводнение Монморанси! Ты хороша в магии воды, тебе можно, а я нет!"),
128: ("Oh, I'm good with fire, but I still do laundry with magic, you know?",
     "О, я хороша с огнём, но всё равно стираю магией, знаешь?"),
129: ("...Me too.", "…Я тоже."),
130: ("Ugh...", "Ох…"),
131: ("Wait a second... That means...", "Погоди… значит…"),
132: ("Before I came, Saito did the laundry... So before I came to this world, Louise did it herself?",
     "Пока меня не было, Сайто стирал… Значит, до того, как я попал в этот мир, Луиза стирала сама?"),
133: ("You carried water in a bucket and washed in your room, didn't you? I know you wandered the halls at night.",
     "Ты носила воду в ведре и стирала в комнате, да? Я знаю, что ты бродила по коридорам по ночам."),
134: ("U-Ugh, shut up! Just leave me alone!", "О-Ох, замолчи! Отстань от меня!"),
135: ("Could it be that Louise actually likes doing laundry?", "Может, Луиза и правда любит стирать?"),
136: ("W-Why?", "П-Почему?"),
137: ("Well, when I first got here, I did the laundry, but lately you've been doing it yourself, haven't you?",
     "Ну, когда я только появился, стирал я, но в последнее время ты стираешь сама, да?"),
138: ("T-That's...", "Т-Это…"),
139: ("So I thought maybe you liked it.", "Я и подумал, что тебе, может, нравится."),
140: ("That's ridiculous! Are you an idiot!?", "Это нелепо! Ты что, идиот!?"),
141: ("...Why are you so angry?", "…Почему ты так злишься?"),
142: ("Once Siesta goes back to her old job, I'll do the laundry again. Don't worry.",
     "Когда Сиэста вернётся к своей работе, я снова буду стирать. Не волнуйся."),
143: ("N-No, that's fine!", "Н-Нет, это не нужно!"),
144: ("You used to let me wash them without a second thought.",
      "А раньше ты спокойно позволяла мне стирать."),
145: ("Because you might be looking at my laundry and grinning!",
      "Потому что ты мог смотреть на мою одежду и ухмыляться!"),
146: ("Eh! You saw!?", "А! Ты видела!?"),
147: ("It became the talk of the whole academy—that my familiar was grinning while "
      "doing the laundry. Ugh, the worst!", "Это стало темой разговоров всей академии — "
      "что мой фамильяр ухмылялся, стирая бельё. Фу, ужас!"),
}
CHOICES = {
771: [("How about becoming Kirche's maid?", "Как насчёт стать горничной Кирке?"),
      ("How about becoming Tabitha's maid?", "Как насчёт стать горничной Табасы?"),
      ("How about becoming Guiche's maid?", "Как насчёт стать горничной Гиша?")],
776: [("Did you do it yourself before I came?", "До того, как я пришёл, ты стирала сама?"),
      ("Does Louise actually like laundry?", "Луиза и правда любит стирать?"),
      ("I don't mind doing it again", "Я не против снова стирать")],
}
SPK = {'サイト': 's', 'ルイズ': 'l', 'キュルケ': 'k', 'シエスタ': 'si', 'ギーシュ': 'g',
       'モンモランシー': 'm', 'ハルナ': 'ha', 'タバサ': 't', 'null': 'th'}
START = {'s': 0, 'l': 0, 'k': 0, 'si': 0, 'g': 0, 'm': 0, 'ha': 0, 't': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch21/parse_771_805.json', encoding='utf-8'))
    script = ['# Глава 21, часть 1 (сцены 771–779): Сиэста становится горничной Луизы.',
              '# Источник: ps2_source/chapters/chapter_22_サイトのメイド.txt (SCENE 771-779).',
              '', 'label ch21:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 779:
                break
            scene = x['no']
            script += ['label ch21_1_scene_%d:' % scene, '']
            continue
        if k == 'event':
            event(x['src'], script)
            continue
        if k == 'dlg':
            idx = x['idx']
            if idx not in T:
                continue
            en, ru = T[idx]
            en = en_norm(en)
            spk = SPK.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch21_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch21_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch21_1_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 771 <= scene <= 779:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch21_1_scene_%d' % x['target']
                                          if 771 <= x['target'] <= 779 else 'ch21_2'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch21_2', '    return', '']
    files = {
        'game/chapters/21/script-ch21_1.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch21_1_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch21_1_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch21_1_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch21_1_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch21/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
