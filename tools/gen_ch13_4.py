#!/usr/bin/env python3
"""Chapter 13 part 4 (extra scenes 1184-1188): volleyball and the aftermath."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("Ah, what lovely weather...", "Ах, какая прекрасная погода…"),
1: ("Sigh, you're so carefree.", "Фух, какая ты беззаботная."),
2: ("W-What's that!?", "Ч-Что ты сказала!?"),
3: ("You don't know what Louise will do to us if we lose.",
    "Ты не знаешь, что Луиза сделает с нами, если мы проиграем."),
4: ("It's fine. Darling is with me.", "Всё хорошо. Дорогой со мной."),
5: ("Yeah, that's what I mean...", "Нет, я к тому и веду…"),
6: ("Hey, won't you teach me a game from your country to pass the time?",
    "Слушай, не научишь ли ты меня игре из своей страны, чтобы скоротать время?"),
7: ("Eh?", "А?"),
8: ("Come on, now's the time for that. We need to relax a little.",
    "Ну же, сейчас как раз подходящий момент. Нужно немного расслабиться."),
9: ("(You can't just spring that on me, you moody girl...)",
    "Ну вот вдруг такое говорить — переменчивая ты…"),
10: ("I suppose so. What should we do?", "Ладно. Что придумаем?"),
11: ("That's the spirit.", "Вот-вот, так-то лучше."),
12: ("Maybe a girl's game would be better...?", "Может, девичья игра была бы лучше…?"),
13: ("Mm, anything's fine.", "Мм, всё подойдёт."),
14: ("Well, the classic would be... volleyball, I guess...?",
     "Ну, из классики… наверное, волейбол…?"),
15: ("Volleyball?", "Волейбол?"),
16: ("Yeah, a ball game from my country.", "Да, игра с мячом из моей страны."),
17: ("Huh.", "Хм."),
18: (None, None),
19: ("That said, we're too few for volleyball. Let's practice setting.",
     "Впрочем, для волейбола нас мало. Давай потренируем пас."),
20: ("Setting?", "Пас?"),
21: ("Simply put, you pass the ball to the other person without holding it.",
     "Проще говоря, передаёшь мяч другому, не удерживая его в руках."),
22: ("Like this.", "Вот так."),
23: ("Huh. I think I get it.", "Хм, вроде поняла."),
24: ("Here we go! Up!", "Ну же! Вверх!"),
25: ("Pon!", "Пон!"),
26: ("Eek!", "Ой!"),
27: ("Pon!", "Пон!"),
28: ("Oh? Hiraga-kun, are you playing volleyball?", "Ах? Хирага-кун, вы играете в волейбол?"),
29: ("Ah, Haruna. Kirche asked me to teach her something to pass the time.",
     "А, Харуна. Кирке попросила научить её чем-нибудь скоротать время."),
30: ("Playing here of all places... I don't know you.",
     "Играть в таком месте… Я тебя не знаю."),
31: ("Louise-san was fuming, saying she'd make you eat pasta standing on your head if she wins.",
     "Луиза-сан была в ярости — сказала, если победит, заставит тебя есть пасту стоя на голове."),
32: ("Ugh, seriously?", "Ох, правда?"),
33: ("It's fine, it's fine. I've got it all figured out.",
     "Всё хорошо, всё хорошо. Я всё продумала."),
34: ("Really?", "Правда?"),
35: ("More importantly, Haruna. Will you practice setting with me?",
     "Главное — Харуна. Поработаешь со мной пас?"),
36: ("With darling, I just can't seem to do it.", "С дорогим у меня никак не получается."),
37: ("Well, excuse me.", "Ну, прошу прощения."),
38: ("Sure. I wanted to move my body a bit anyway.",
     "Конечно. Я и так хотела немного размяться."),
39: (None, None),
40: ("(Kirche's coordination is great... wait!)", "Вот она Кирке — координация отличная… стоп!"),
41: ("(W-What are those two things swaying at Kirche's chest...?)",
     "Ч-Что это за две вещи колышутся у Кирке на груди…?"),
42: ("Ahahaha. Quite interesting, isn't it?", "А-ха-ха. Довольно забавно, правда?"),
43: ("Pon!", "Пон!"),
44: ("There!", "Вот!"),
45: ("(...A swaying... demonic ball? The charm and the thrill of it...)",
     "…Колышется… демонический мяч? Очарование и волнение…"),
46: ("This world is full of danger!", "Чёрт, этот мир полон опасностей!"),
47: ("D-Don't look!", "Н-Не смотри!"),
48: ("Darling, look out!", "Дорогой, осторожно!"),
49: ("Guh!", "Гух!"),
50: ("Really, Hiraga-kun. What are you looking at with that red face?",
     "Ну же, Хирага-кун. Что ты смотришь с таким красным лицом?"),
51: ("D-Don't guess, Haruna-chan.", "Н-Не угадывай, Харуна-тян."),
52: ("I don't know Hiraga-kun anymore.", "Я не знаю никакого Хирага-куна."),
53: ("Eeeh. S-Sorry...", "Ох. П-Прости…"),
54: ("(Wow, I can't look away. Is this what charm is...?)",
     "Вау, я не могу отвести взгляд. Это и есть обаяние…?"),
55: ("Darling, look out!", "Дорогой, осторожно!"),
56: ("Guh!", "Гух!"),
57: ("What are you doing, getting between Haruna and me?",
     "Что ты делаешь, вставая между Харуной и мной?"),
58: ("W-Well, er...", "Н-Ну, э-э…"),
59: ("...Ufufu. Where were you looking?", "…Уф-фу. Куда ты смотрел?"),
60: ("S-Somewhere I can't say...", "Т-Туда, где нельзя сказать…"),
61: ("Hiraga-kun's pervert!", "Хирага-кун — извращенец!"),
62: ("Eeeh. S-Sorry...", "Ох. П-Прости…"),
63: ("...Hm? What's with this pressure!?", "…Хм? Что за давление!?"),
64: ("...", "…"),
65: ("Guh!", "Гух!"),
66: ("I don't know.", "Я не знаю."),
67: ("Ouch, I mean...", "Ой, я хотел сказать…"),
68: ("Kirche-san, shall we play somewhere else? Hiraga-kun keeps looking at strange places.",
     "Кирке-сан, давайте поиграем в другом месте? Хирага-кун всё время смотрит в странные места."),
69: ("Eep...", "Ай…"),
70: ("Eh. I don't mind being watched...", "Э-э. Я не против, чтобы на меня смотрели…"),
71: ("No, I mean...", "Нет, я хотел…"),
72: ("Hmph.", "Хмф."),
73: ("Ahahaha...", "А-ха-ха…"),
}
CHOICES = {
1184: [("Look away from Kirche", "Отвести взгляд от Кирке"),
       ("Not look away from Kirche", "Не отводить взгляд от Кирке"),
       ("...Is that killing intent?", "…Это убийственное намерение?")],
}
SPK = {'キュルケ': 'k', 'サイト': 's', 'ハルナ': 'ha', 'null': 'th'}
START = {'k': 124, 's': 132, 'ha': 2, 'th': 2}


def main():
    data = json.load(open('reports/ch13/parse_1184_1188.json', encoding='utf-8'))
    script = ['# Глава 13, часть 4 (сцены 1184–1188): волейбол, « demonic ball».',
              '# Источник: ps2_source/chapters/chapter_14_炎の予感.txt (SCENE 1184-1188).',
              '', 'label ch13_4:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 1188:
                break
            scene = x['no']
            script += ['label ch13_4_scene_%d:' % scene, '']
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
                ctext = '%s{#ch13_4_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch13_4_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump ch14')
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 4 ====', '    jump ch14', '    return', '']
    files = {
        'game/chapters/13/script-ch13_4.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch13_4_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch13_4_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch13_4_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch13_4_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch13/voice_map_4.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
