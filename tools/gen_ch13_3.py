#!/usr/bin/env python3
"""Chapter 13 part 3 (scenes 568-577): Kirche's fire, Weatherly suspicion."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("(I found a few small leads, but nothing really important...)",
    "Я нашёл пару мелких зацепок, но ничего важного…"),
1: ("(This might not work out. Could I even do a handstand...?)",
    "Кажется, ничего не выйдет. Я же не умею стоять на голове…"),
2: ("Really, darling, don't make such a sour face.", "Ну же, дорогой, не хмурься так."),
3: ("Looking so helpless doesn't suit my darling.",
    "С таким беспомощным видом ты не похож на моего дорогого."),
4: ("E-Easy for you to say...", "Т-Так не говори…"),
5: ("Ugh!", "Ну!"),
6: ("In times like this, you puff out your chest and say you can do it—even if you have to lie.",
    "В такое время нужно расправить плечи и сказать, что справишься, — даже если придётся солгать."),
7: ("That's the magic that moves you forward. Even fake cheer is still cheer.",
    "Вот магия, что движет вперёд. Даже наигранная бодрость — всё равно бодрость."),
8: ("I guess so.", "Наверное."),
9: ("All right, I'll give it a shot!", "Давай, попробую!"),
10: ("That's my darling! I might just fall for you all over again.",
     "Вот теперь ты мой дорогой! Я снова влюблюсь в тебя."),
11: ("Please spare me.", "Пощадите меня."),
12: ("What about you, Kirche? Aren't you worried?", "А ты сама как, Кирке? Ты не волнуешься?"),
13: ("Not at all. Because my darling is with me.", "Ни капли. Ведь дорогой со мной."),
14: ("That has nothing to do with it.", "Это совсем ни к чему."),
15: ("Oh, but it does. If you keep thinking about something, it becomes real. "
     "If you don't, nothing happens.",
     "О, нет, имеет. Если постоянно думать о чём-то, оно сбывается. Не думаешь — ничего не получается."),
16: ("???", "???"),
17: ("It's the same for love and for a task. That's why I'm with my darling.",
     "И с любовью, и с делом одинаково. Поэтому я и с дорогим."),
18: ("I don't quite get it, but... as long as I don't give up, things will work out?",
     "Не совсем понимаю, но… пока я не сдаюсь, всё получится?"),
19: ("Well, something like that.", "Ну, примерно так."),
20: ("...", "…"),
21: ("But, Kirche. Why are you so serious about this case?",
     "Но, Кирке. Почему ты так серьёзно относишься к этому делу?"),
22: ("Serious?", "Серьёзно?"),
23: ("I mean... you're not acting like your usual self.", "Ну… ты не похожа на обычную Кирке."),
24: ("You see, I hate that bomb-thrower.", "Дело в том, что я ненавижу этого бомбиста."),
25: ("Huh?", "А?"),
26: ("They see fire only as a tool for destruction. I hate the way they do things.",
     "Они видят в огне только орудие разрушения. Мне ненавистен их подход."),
27: ("As a mage of the 'fire' attribute... by the name of Kirche with a slight fever...",
     "Как маг стихии «огня»… клянусь именем Кирке с лёгким жаром…"),
28: ("...I have to teach them the 'true way to use fire'.",
     "…я должна показать им «настоящее применение огня»."),
29: ("(...'The true way to use fire'?)", "…«Настоящее применение огня»?"),
30: ("Say, Kirche. What's this 'true way to use fire'?",
     "Слушай, Кирке. Что это — «настоящее применение огня»?"),
31: ("Mm. Hard to put into words. Once this is over, I'll tell you all about it.",
     "Мм. Словами не передать. Когда всё закончится, я расскажу тебе подробно."),
32: ("Now, darling, let's go.", "Ну же, дорогой, идём."),
33: ("Yeah, yeah.", "Да-да."),
34: ("Looks like we've made it to the theater.", "Кажется, мы дошли до театра."),
35: ("The theater, huh... It's quiet once the performances end.",
     "Театр… После спектаклей здесь тихо."),
36: ("...!!", "…!!"),
37: ("What's wrong, Kirche?", "Что случилось, Кирке?"),
38: ("Shh! Quiet, darling...", "Тсс! Тише, дорогой…"),
39: ("...", "…"),
40: ("Is that... Weatherly-san? Preparing for the next play, maybe?",
     "Это… Уэзерби-сан? Может, готовится к следующему спектаклю?"),
41: ("Just as I thought.", "Так и думала."),
42: ("Just as you thought? Did something happen to Weatherly-san?",
     "Так и думала? Что случилось с Уэзерби-сан?"),
43: ("Darling... What we were looking for tonight wasn't the bomb-thrower.",
     "Дорогой… Сегодня ночью мы искали не бомбиста."),
44: ("Huh? Then who were we looking for?", "А? Тогда кого мы искали?"),
45: ("I was looking for Weatherly.", "Я искала Уэзерби."),
46: ("Weatherly-san's whereabouts...?", "Уэзерби-сан… её местоположение?"),
47: ("Ah, she's heading into the back alley! Darling, let's follow!",
     "А, она свернула в переулок! Дорогой, за ней!"),
48: ("(I have no idea what's going on, but for now, follow Kirche...)",
     "Ничего не понимаю, но пока послушаюсь Кирке…"),
49: (None, None),
50: ("She's gone... But why Weatherly-san?", "Она ушла… Но почему Уэзерби-сан?"),
51: ("I'm not sure yet, but Weatherly's been acting very suspicious. Maybe... a spy.",
     "Я пока не уверена, но Уэзерби ведёт себя очень подозрительно. Может… она шпион."),
52: ("Huh!? What was that?", "А!? Что ты сказала?"),
53: ("That can't be! Weatherly-san a spy...!", "Не может быть! Уэзерби-сан — шпион…!"),
54: ("Can't believe it? Or don't want to?", "Не верится? Или не хочется верить?"),
55: ("Now that you mention it...", "Теперь, когда ты сказала…"),
56: ("Yes, why didn't I notice sooner.", "Да, почему я не заметила раньше."),
57: ("They were so close, I never thought to suspect them.",
     "Она была так близко, что я и не подумала заподозривать."),
58: ("A spy of what?", "Шпион — кого?"),
59: ("I'm not sure, but they may be deeply involved in the bomb-thrower case.",
     "Точно не знаю, но она может быть глубоко замешана в деле бомбиста."),
60: ("A bomb-thrower's spy?", "Шпион бомбиста?"),
61: ("Well, who knows?", "Ну, кто знает?"),
62: ("A traveling troupe with unclear origins... And they can't even find a lead for an important play.",
     "Бродячая труппа с неясным прошлым… И даже на важный спектакль не могут найти главную роль."),
63: ("Didn't Weatherly-san say there was no one suitable for the lead?",
     "Разве Уэзерби-сан не говорила, что нет подходящего исполнителя?"),
64: ("Right. So we went on stage. But what if that was a cover?",
     "Да. Поэтому мы и вышли на сцену. Но что, если это было прикрытие?"),
65: ("N-No way! They couldn't have predicted we'd come.",
     "Н-Не может быть! Они же не могли предвидеть, что мы придём."),
66: ("True. It's still just guesswork.", "Верно. Это пока только догадки."),
67: ("But I dug around and found one suspicious thing after another.",
     "Но я покопалась и нашла одно подозрительное дело за другим."),
68: ("I don't know how deep this rat goes, but Weatherly is definitely up to something...",
     "Не знаю, насколько глубока эта крыса, но Уэзерби точно что-то задумала…"),
69: ("Still, you noticed. We didn't at all.", "И всё же заметила ты. Мы — совсем нет."),
70: ("In this town... I can sense fire.", "В этом городе… я чувствую огонь."),
}
CHOICES = {
568: [("Easy for you to say...", "Так не говори…"),
      ("All right, I'll give it a shot!", "Давай, попробую!"),
      ("What about you, Kirche?", "А ты сама как, Кирке?")],
573: [("That can't be!", "Не может быть!"),
      ("Now that you mention it...", "Теперь, когда ты сказала…"),
      ("A spy of what?", "Шпион — кого?")],
}
SPK = {'サイト': 's', 'キュルケ': 'k', 'ウェザリー': 'w', 'null': 'th'}
START = {'s': 99, 'k': 88, 'w': 0, 'th': 2}


def main():
    data = json.load(open('reports/ch13/parse_564_577.json', encoding='utf-8'))
    script = ['# Глава 13, часть 3 (сцены 568–577): огонь Кирке, подозрение на Уэзерби.',
              '# Источник: ps2_source/chapters/chapter_14_炎の予感.txt (SCENE 568-577).',
              '', 'label ch13_3:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 577:
                break
            if x['no'] < 568:
                continue
            scene = x['no']
            script += ['label ch13_3_scene_%d:' % scene, '']
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
                ctext = '%s{#ch13_3_c_%d_%d}' % (en_norm(en), scene, i + 1)
                tgt = ('ch13_3_scene_%d' % o['target']
                       if 568 <= o['target'] <= 577 else 'ch14')
                script.append('        "%s":' % ctext)
                script.append('            jump %s' % tgt)
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            tgt = ('ch13_3_scene_%d' % x['target']
                   if 568 <= x['target'] <= 577 else 'ch14')
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % tgt)
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 13 ====', '    jump ch14', '    return', '']
    files = {
        'game/chapters/13/script-ch13_3.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch13_3_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch13_3_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch13_3_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch13_3_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch13/voice_map_3.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
