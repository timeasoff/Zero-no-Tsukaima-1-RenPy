#!/usr/bin/env python3
"""Chapter 13 part 1 (scenes 549-563): the contest, the night plan."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("(Several days have passed since the play ended. Still no trace of the bomb-thrower...)",
    "Прошло уже несколько дней с тех пор, как закончился спектакль. Следов бомбиста так и не нашли…"),
1: ("(I keep investigating, but I can't get any solid leads. Louise is in a bad mood too...)",
    "Я продолжаю расследовать, но никаких зацепок. Луиза тоже в плохом настроении…"),
2: ("(How long is this going to last...?)", "Сколько это ещё продолжится…"),
3: ("Welcome home, Miss Valliere. Saito-san.", "С возвращением, мисс Вальер. Сайто-сан."),
4: ("Sigh... No luck again today.", "Фух… Опять безрезультатно."),
5: ("Don't be discouraged. I'll make some tea.", "Не расстраивайтесь. Я заварю чаю."),
6: ("I'm back.", "Я вернулась."),
7: ("I'm home.", "Я дома."),
8: ("How did it go on your end?", "У вас как дела?"),
9: ("No luck at all. Judging by that face, same for you?", "Совсем нет. Судя по этому лицу, у вас тоже?"),
10: ("Haa.", "Хаа."),
11: ("Ugh, don't make that gloomy face! With that look you'll never get fired up when it counts!",
     "Ну же, не хмурься! С таким видом ты вспыхнуть не сможешь, когда припрёт!"),
12: ("Kirche is too carefree.", "Кирке слишком беззаботна."),
13: ("Hmph, what's that!?", "Хм, что ты сказала!?"),
14: ("Even while we sit here, the bomb-thrower's damage may be spreading.",
     "Пока мы здесь сидим, урон от бомбиста может расти."),
15: ("Getting worked up won't help! At this rate you'll never catch them.",
     "Злиться бесполезно! Так вы никогда их не поймаете."),
16: ("W-What did you say!?", "Ч-Что ты сказала!?"),
17: ("H-Hey! You two!", "Э-Эй! Вы двое!"),
18: ("What!?", "Что!?"),
19: ("What is it, darling?", "Что, дорогой?"),
20: ("N-Nothing at all...", "Н-Ничего такого…"),
21: ("(Women are... scary...)", "Женщины… страшные…"),
22: ("B-But... fighting isn't good...", "Н-Но… ссориться нехорошо…"),
23: ("Right. Then let's do this.", "Верно. Тогда давайте так."),
24: ("Huh?", "А?"),
25: ("Split into two teams and see who catches the bomb-thrower first. How about a contest?",
     "Разделимся на две группы и посмотрим, кто первым поймает бомбиста. Устроим соревнование?"),
26: ("Hey now, Kirche.", "Эй, Кирке."),
27: ("The loser obeys the winner's orders! How does that sound?",
     "Проигравший выполняет приказы победителя! Как насчёт?"),
28: ("It's a request from the Princess. A contest is improper.",
     "Это просьба принцессы. Соревноваться неуместно."),
29: ("Oh, come on. Don't they say team competitions improve overall efficiency?",
     "Ну же. Говорят же, что командное соревнование повышает общую эффективность?"),
30: ("That may be true, but...", "Может, и так, но…"),
31: ("Haaaaay! Then it's decided! And darling, you're on my team.",
     "Ха-а-ай! Тогда решено! И дорогой, ты в моей команде."),
32: ("W-Wait a moment! Why would he be on your team!?",
     "П-Подождите! Почему он в вашей команде!?"),
33: ("My, without darling, are you worried, Louise?", "Ой, без дорогого ты тревожишься, Луиза?"),
34: ("T-That's not it at all!", "В-Вовсе нет!"),
35: ("Then it's decided!", "Тогда решено!"),
36: ("Uuu...", "Ууу…"),
37: ("T-Then instead! I get to use everyone else!", "Т-Тогда взамен! Все остальные в моей команде!"),
38: ("Sure, fine.", "Конечно, ладно."),
39: ("F-Fine! If I win, you'll attend class standing on your head!",
     "Л-Ладно! Если я побежу, ты будешь посещать занятия стоя на голове!"),
40: ("Y-You're fine with that? You can still back out now, you know.",
     "Т-Ты согласна? Ты ещё можешь отказаться, пока не поздно."),
41: ("Sure. In return, if I win...", "Конечно. А если я победю…"),
42: ("Let me see... How about you be my maid for a day?",
     "Хм… Как насчёт — быть моей горничной день?"),
43: ("F-Fine! Don't blame me if you regret it!", "Л-Ладно! Не жалуйся, если пожалеешь!"),
44: ("(Somehow, things are being decided without me...)", "Как-то так выходит, что всё решают без меня…"),
45: ("Hey, aren't you going to hear my opinion?", "Эй, вы не собираетесь выслушать моё мнение?"),
46: ("Saito... You be quiet for now.", "Сайто… Помолчи."),
47: ("Y-yes, ma'am.", "Так точно."),
48: ("I see. Kirche's plan might actually be good.", "Понятно. План Кирке и вправду может быть неплохим."),
49: ("Hiraga-kun... Do you really think so?", "Хирага-кун… Ты правда так думаешь?"),
50: ("Well, kind of... Ahahahaha!", "Ну, примерно… А-ха-ха-ха!"),
51: ("Hmph... Even as a familiar, nobody cares about me...",
     "Хм… Даже будучи фамильяром, обо мне никто не заботится…"),
52: ("(Sulk, sulk...)", "Обида-обида…"),
53: ("(Pat, pat.)", "Поглаживает."),
54: ("(Touched...)", "Растрогался…"),
55: ("Let's go, everyone!", "Идём, всем!"),
56: ("Louise-san, w-where are we going?", "Луиза-сан, к-куда мы идём?"),
57: ("How should I know! Hurry up!", "Откуда я знаю! Быстрее!"),
58: ("Hey, Louise. Don't drag us into this.", "Эй, Луиза. Не втягивай нас в это."),
59: ("No complaining. All we have to do is win. Win!", "Без возражений. Нам надо только победить. Победить!"),
60: ("...", "…"),
61: ("Come on, Tabitha too!", "Ну же, Табаса тоже идёт!"),
62: ("Goodbye.", "До свидания."),
63: ("...", "…"),
64: ("Sigh. Say, Kirche.", "Фух. Слушай, Кирке."),
65: ("Why are you teaming up with me?", "Почему ты идёшь со мной?"),
66: ("Well, I got tired of arguing, and figured it's time to get serious. That's all.",
     "Ну, я устала спорить и решила, пора взяться за дело серьёзно. Вот и всё."),
67: ("Really...?", "Правда…?"),
68: ("(Just Kirche and me in the room now.)", "В комнате остались только я и Кирке."),
69: ("(Kirche is reading a book... At this rate we'll lose, won't we?)",
     "Кирке читает книгу… Так мы проиграем, да?"),
70: ("Kirche! Let's get going too!", "Кирке! Идём и мы!"),
71: ("Haa... I'm tired...", "Фух… Я устала…"),
72: ("Eh?", "А?"),
73: ("I'm going to take a nap. What about you, darling?", "Я немного посплю. А ты что сделаешь, дорогой?"),
74: ("Wait! What about the contest!?", "Подожди! А соревнование!?"),
75: ("Panicking won't help. Let's rest like this.", "Паниковать бесполезно. Давай отдохнём."),
76: ("My, we think alike, darling.", "Ой, мы думаем одинаково, дорогой."),
77: ("I'll take a little nap...", "Я немного посплю…"),
78: ("Hey... I didn't mean to relax that much...", "Эй… Я не собирался расслабляться настолько…"),
79: ("Let's hold a strategy meeting. Wandering around blindly is inefficient.",
     "Давай проведём совещание. Ходить наугад — неэффективно."),
80: ("My, darling. I do have a plan.", "Ой, дорогой. У меня есть план."),
81: ("Eh? Really?", "А? Правда?"),
82: ("Well, I'll explain later. For now, I'm taking a little nap.", "Ну, объясню позже. Пока я немного посплю."),
83: ("H-Hey! What do you mean, nap!?", "Э-Эй! Что значит «посплю»!?"),
84: ("It's fine, darling. I have a proper plan. Right?", "Всё хорошо, дорогой. У меня есть план. Да?"),
85: ("W-What plan?", "Ч-Что за план?"),
86: ("Secret.", "Секрет."),
87: ("You can't do that! If we lose, it's handstands for both of us!",
     "Так не честно! Если проиграем, оба будем стоять на голове!"),
88: ("Goodness, don't panic. I've heard the bomb-thrower often appears at night.",
     "Ну же, не паникуй. Я слышала, бомбист чаще появляется ночью."),
89: ("But the ones we saw were in broad daylight.", "Но мы видели его днём."),
90: ("Well, that's the puzzling part, but all the sightings in town were at night.",
     "Вот это и странно, но в городе его видели только ночью."),
91: ("So even if we're walking around, wouldn't narrowing the search to night increase our chances?",
     "Так что если уж ходить, то поиски ночью повышают шансы заметить его, не правда ли?"),
92: ("I see. Now that you mention it...", "Понятно. Теперь, когда ты сказала… и правда."),
93: ("You got the plan?", "Понял план?"),
94: ("Got it. I'll nap too, to prepare for the night.", "Понял. Я тоже посплю, чтобы подготовиться к ночи."),
95: ("By the way? Darling, why don't we sleep together?", "Кстати? Дорогой, почему бы нам не поспать вместе?"),
96: ("Eh, I'll pass.", "Э, я воздержусь."),
97: ("Oh, what a pity.", "Ой, жаль."),
98: ("...Si! ...Saito!", "…Са-Сайто!"),
99: ("...Hmm?", "…Мм?"),
100: ("Saito! Why are you sleeping!?", "Сайто! Что ты спишь!?"),
101: ("Was I asleep?", "Я спал?"),
102: ("You were. Fast asleep.", "Да. Спал крепко."),
103: ("Oops.", "Ой."),
104: ("(It's pretty dark outside. I must have slept quite a while...)",
     "На улице уже темно. Я, кажется, проспал довольно долго…"),
105: ("I'm back.", "Я вернулась."),
106: ("Welcome back, Tabitha. How did it go?", "С возвращением, Табаса. Как дела?"),
107: ("Waste of time.", "Потеря времени."),
108: ("(I see. Louise and the others didn't find anything today either...)",
     "Ясно. Похоже, Луиза и остальные сегодня ничего не нашли…"),
109: ("Y-You've all worked hard...", "В-Вы все постарались…"),
110: ("Thanks. But...", "Спасибо. Но…"),
111: ("I don't want to hear that from someone who slept the whole time.",
     "Не хочу этого слышать от того, кто проспал всё это время."),
112: ("Woe is me...", "Ох, горе мне…"),
113: ("D-Don't lose heart... There's still time!", "Н-Не падайте духом… Ещё будет возможность!"),
114: ("What, Saito. Don't act superior.", "Что, Сайто. Не важничай."),
115: ("Just watch. I'll win this contest and make you stand on your head for a day!",
     "Смотри. Я выиграю это соревнование и заставлю тебя день простоять на голове!"),
116: ("W-What!?", "Ч-Что!?"),
117: ("Out all day with nothing to show for it—that's no good!",
     "Целый день снаружи и ничего не найти — это плохо!"),
118: ("What! You slept the whole time, Saito! Do you even intend to compete!?",
     "Что! Ты всё время спал, Сайто! Ты вообще собираешься соревноваться!?"),
119: ("I-I do... Kirche is...", "Я-Я собираюсь… Кирке…"),
120: ("Now, now, no shouting. Darling, it's about time we went out.",
     "Ну-ну, не кричи. Дорогой, пора идти."),
121: ("G-Going out at this hour, where could you possibly go!?",
     "В-В такое время — куда вы собрались!?"),
122: ("Under this beautiful starry sky, a man and a woman go out. "
     "Doesn't that pretty much tell you what they'll do?",
     "Под этим прекрасным звёздным небом мужчина и женщина выходят. "
     "Догадаться, чем они займутся, не трудно, правда?"),
123: ("H-How shameless!", "Фу, нечисто!"),
124: ("W-Wait, Louise! Don't worry—what you're imagining will never happen!",
     "П-Подожди, Луиза! Не волнуйся — того, что ты представила, абсолютно не будет!"),
125: ("I don't believe you!", "Я тебе не верю!"),
126: ("Goodness, you're such a fool. It's an investigation, an investigation!",
     "Ну же, какая ты глупая. Это расследование, расследование!"),
127: ("We're focusing on the night patrol. They say the bomb-thrower appears more often at night, right?",
     "Мы сосредоточимся на ночных поисках. Говорят, бомбист чаще появляется ночью, да?"),
128: ("Hmf. I don't believe it.", "Хмф. Не верю."),
129: ("Well, fine. The rest of you rest up and get ready for tomorrow.",
     "Ладно. Остальные отдыхайте и готовьтесь к завтрашнему дню."),
130: ("Understood.", "Понятно."),
131: ("W-Wait! I'm coming too!", "П-Подождите! Я тоже иду!"),
132: ("No. Louise, you're overdoing it.", "Нет. Луиза, ты слишком стараешься."),
133: ("At this rate you'll be useless when it matters. Good children go to bed on time.",
     "Так ты станешь бесполезной, когда припрёт. Хорошие дети ложатся спать вовремя."),
134: ("Ugh. Fine.", "Уу. Ладно."),
135: ("Well then, the adult hour begins. Hee, let's go, darling.",
     "Ну что ж, начинается взрослый час. Хе, идём, дорогой."),
136: ("Y-Yes, ma'am.", "Т-Так точно."),
137: ("Saito, you idiot! Dog! I won't forgive you!", "Сайто, дурак! Пёс! Я тебе не прощу!"),
138: ("(I... can't hear her. Can't hear her...)", "Я… не слышу. Не слышу…"),
139: ("Now, darling. Where shall we go?", "Ну же, дорогой. Куда нам направиться?"),
}
CHOICES = {
549: [("Object.", "Возразить."), ("Accept it.", "Согласиться."), ("Pout a little.", "Подуться.")],
554: [("Let's go out right away!", "Пойдём сейчас же!"), ("Rest like this?", "Отдохнём так?"),
      ("Hold a strategy meeting!", "Проведём совещание!")],
559: [("Comfort everyone.", "Утешить всех."), ("Encourage everyone.", "Подбодрить всех."),
      ("Scold everyone.", "Отругать всех.")],
}
MOVES = [("In front of the castle", "Перед замком", "城前"),
         ("The street", "Улица", "街道"),
         ("The back alley", "Задний переулок", "裏通り"),
         ("The main street", "Главная улица", "表通り")]
SPK = {'サイト': 's', 'ルイズ': 'l', 'シエスタ': 'si', 'キュルケ': 'k', 'タバサ': 't',
       'ギーシュ': 'g', 'ハルナ': 'ha', 'null': 'th'}
START = {k: 0 for k in SPK.values()}


def main():
    data = json.load(open('reports/ch13/parse_549_569.json', encoding='utf-8'))
    script = ['# Глава 13, часть 1 (сцены 549–563): «炎の予感» — спор, соревнование, ночной план.',
              '# Источник: ps2_source/chapters/chapter_14_炎の予感.txt (SCENE 549-563).',
              '', 'label ch13:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 563:
                break
            scene = x['no']
            script += ['label ch13_1_scene_%d:' % scene, '']
            continue
        if k == 'event':
            event(x['src'], script)
            continue
        if k == 'dlg':
            idx = x['idx']
            if 140 <= idx <= 143:
                continue  # move options handled as menu at end of scene
            en, ru = T[idx]
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
            if idx == 139:
                script.append('    # 【移動】城前/街道/裏通り/表通り → 1469/1470/1475/1480 '
                              '(extra-сцены не портированы)')
                script.append('    menu:')
                for i, (en_m, ru_m, ja_m) in enumerate(MOVES):
                    ctext = '%s{#ch13_1_c_563_%d}' % (en_norm(en_m), i + 1)
                    script.append('        "%s":' % ctext)
                    script.append('            jump ch13_2')
                    ja_c += ['    old "%s"' % ctext, '    new "%s"' % ja_m, '']
                    ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru_m, '']
                script.append('')
            continue
        if k == 'choice':
            script.append('    menu:')
            for i, o in enumerate(x['options']):
                en, ru = CHOICES[scene][i]
                ctext = '%s{#ch13_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                tgt = ('ch13_1_scene_%d' % o['target']
                       if 549 <= o['target'] <= 563 else 'ch13_2')
                script.append('        "%s":' % ctext)
                script.append('            jump %s' % tgt)
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            tgt = ('ch13_1_scene_%d' % x['target']
                   if 549 <= x['target'] <= 563 else 'ch13_2')
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % tgt)
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch13_2', '    return', '']
    files = {
        'game/chapters/13/script-ch13_1.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch13_1_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch13_1_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch13_1_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch13_1_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch13/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
