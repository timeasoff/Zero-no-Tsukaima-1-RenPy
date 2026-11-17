#!/usr/bin/env python3
"""Chapter 17 part 1 (scenes 670-683): tensions, Queen's council."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("(A few days since the play ended. No leads on the bomb-thrower, only time passing...)",
    "Прошло несколько дней после спектакля. Ни зацепок о бомбисте, только время идёт…"),
1: ("(We all went back to the academy once, but...)", "(Мы все вернулись в академию, но…)"),
2: ("(No real results, and we still don't know who the bomb-thrower is—everyone's on edge...)",
    "(Никаких результатов, и мы так и не знаем, кто бомбист, — все на взводе…)"),
3: ("Say that again, Kirche?", "Повтори ещё раз, Кирке?"),
4: ("Oh, is the young lady of Valliere hard of hearing as well as empty-headed? "
    "Well, darling, what do you think?",
    "Ой, неужели юная леди Вальер не только пустоголова, но и туха ушами? "
    "Ну, дорогой, что думаешь?"),
5: ("Well... I mean...", "Ну… Я хотел сказать…"),
6: ("Stop clinging to Saito in the confusion!", "Хватит прижиматься к Сайто в такой момент!"),
7: ("(So that's how things stand. Oh well.)", "(Вот как всё обернулось. Ну что ж.)"),
8: ("Louise, cut it out. I understand you're irritated, but calm down, okay?",
    "Луиза, хватит. Я понимаю, ты раздражена, но успокойся, ладно?"),
9: ("Saito! What kind of language is that to use with your mistress?",
    "Сайто! Как ты разговариваешь со своей госпожой?"),
10: ("I think we need to re-educate you on your place as a familiar!?",
     "Похоже, мне придётся ещё раз объяснить тебе твоё место фамильяра!?"),
11: ("Hey, don't take it out on me!", "Эй, не вымещай на мне!"),
12: ("Kirche, that's a bit much...", "Кирке, это слишком…"),
13: ("You stay out of it, darling! This is between me and Louise.",
     "Ты не лезь, дорогой! Это разговор между мной и Луизой."),
14: ("O-My apologies...", "О-Прошу прощения…"),
15: ("Tabitha, stop them, please.", "Табаса, останови их, пожалуйста."),
16: ("Stress relief.", "Снятие стресса."),
17: ("Well, maybe... but don't you think there's a better way?",
     "Ну, может… Но не думаешь ли ты, что есть способ получше?"),
18: ("...", "…"),
19: ("Saito!", "Сайто!"),
20: ("Y-Yes!", "Д-Да!"),
21: ("What are you spacing out for? Cleaning and laundry! And you haven't made the bed yet, have you?",
     "Что ты застыл? Уборка и стирка! И постель ещё не застелена, да?"),
22: ("Oh, darling is going out with me. Overworking is bad for the body.",
     "Ой, дорогой собирается идти со мной. Переработка вредна для тела."),
23: ("Who gave you permission!", "Кто тебе это разрешил!"),
24: ("Why, me, of course.", "Ну, я, конечно."),
25: ("You're not Saito's mistress, are you!", "Ты же не госпожа Сайто!"),
26: ("Oh, but he's my darling, so it's much the same thing.",
     "Ой, но он мой дорогой — это почти одно и то же."),
27: ("It's nothing like it! It makes no sense!", "Совсем не одно и то же! Бессмыслица!"),
28: ("Ufufu. Well, there are things you just don't understand, my dear. "
     "The complicated relationship between a man and a woman.",
     "Уф-фу. Ну, есть вещи, которых ты просто не поймёшь. "
     "Сложные отношения между мужчиной и женщиной."),
29: ("What was that!?", "Что ты сказала!?"),
30: ("(If I stay, I'll definitely get dragged into their fight...)",
     "(Если я останусь, меня точно втянут в их драку…)"),
31: ("Ah, I remember—Colbert-sen called me about the Zero Fighter. See you!",
     "А, я вспомнил — меня звал Кольбер-сэн по поводу Zero Fighter. Пока!"),
32: ("W-Wait, Saito?", "П-Подожди, Сайто?"),
33: ("Darling?", "Дорогой?"),
34: ("Desertion under fire.", "Дезертирство."),
35: ("(Phew... I wasn't actually called by Colbert-sen...)",
     "(Фух… На самом деле Кольбер-сэн меня не звал…)"),
36: ("(I'll ask him to hide me until things cool down...)",
     "(Попрошу его укрыть меня, пока всё не уляжется…)"),
37: ("Oh, Saito-kun. What's wrong?", "Ой, Сайто-кун. Что случилось?"),
38: ("Um... Sorry, could you hide me for a bit?", "Э-Э… Простите, можно у вас немного скрыться?"),
39: ("Hm? What happened?", "Хм? Что случилось?"),
41: ("Hahahaha! Of course—even Saito-kun is powerless before women, eh?",
     "Ха-ха-ха! Конечно — даже Сайто-кун бессилен перед женщинами, да?"),
42: ("This is no laughing matter. I'm trembling, wondering when I'll be punished.",
     "Это не смешно. Я дрожу, не зная, когда меня накажут."),
43: ("No, excuse me. I was just thinking Saito-kun is human too.",
     "Нет, прости. Я просто подумал, что Сайто-кун тоже человек."),
44: ("...", "…"),
45: ("No, don't be angry. The fact you brought me this truth has changed my view of life.",
     "Нет, не сердись. То, что ты открыл мне эту правду, изменило мой взгляд на жизнь."),
46: ("View of life?", "Взгляд на жизнь?"),
47: ("Yes. Magic isn't something to attack others with, nor to create hierarchy.",
     "Да. Магия — не то, чем нападают на других, и не то, что создаёт иерархию."),
48: ("Magic is only true magic when it helps those who can't use it. That's what I believe.",
     "Магия — настоящая магия только тогда, когда служит тем, кто не может ею пользоваться. Я так думаю."),
49: ("Haa...", "Фух…"),
50: ("No, I'm sorry... I got carried away.", "Нет, прости… Я увлёкся."),
51: ("Not at all...", "Нет…"),
52: ("(Come to think of it, I've known Colbert-sen since I found the Zero Fighter...)",
     "(Если подумать, я знаю Кольбера-сэна с тех пор, как нашёл Zero Fighter…)"),
53: ("(At first he seemed interested in me as Louise's teacher...)",
     "(Сначала он, кажется, интересовался мной как преподаватель Луизы…)"),
54: ("(Ever since we shared the goal of flying the Zero Fighter, he's become my teacher too...)",
     "(С тех пор как у нас появилась общая цель — летать на Zero Fighter, он стал и моим наставником…)"),
55: ("Saito. I thought you'd be here.", "Сайто. Я так и думала, что ты здесь."),
56: ("Montmon! How did you know I was here?", "Монмон! Как ты узнала, что я здесь?"),
57: ("I saw you enter Mr. Colbert's room just now.", "Я видела, как ты входил в комнату Кольбера."),
58: ("I was just told by old Osmond to call you and Louise.",
     "Меня просто попросил старик Осман позвать тебя и Луизу."),
59: ("The headmaster? What for?", "Директор? Зачем?"),
60: ("Beats me. I wasn't told the details.", "Понятия не имею. Мне не сказали подробностей."),
61: ("All right, let's go. Thanks, Colbert-sen.", "Ладно, идём. Спасибо, Кольбер-сэн."),
62: ("No, no. Come anytime.", "Нет-нет. Приходи когда хочешь."),
63: ("The Princess wants to see us?", "Принцесса хочет видеть нас?"),
64: ("Aye, seems urgent. Sorry, but could you head to the palace at once? "
     "She said she'll explain in person.",
     "Да, похоже, срочно. Простите, но не могли бы вы немедленно отправиться во дворец? "
     "Она сказала, что объяснит лично."),
65: ("Understood. We'll go at once.", "Понятно. Мы сразу идём."),
66: ("I've got a bad feeling about this...", "Какое-то плохое предчувствие…"),
67: ("Her Majesty—Louise Francoise, third daughter of the La Valliere family, "
     "and her familiar have arrived.",
     "Её Величество — Луиза Франсуаза, третья дочь дома Ла Вальер, и её фамильяр прибыли."),
68: ("Your Majesty... Fair morning to you.", "Ваше Величество… Доброе утро."),
69: ("Ah, you finally came! Come in, Louise. You too, familiar.",
     "Ах, вы наконец! Входи, Луиза. И ты, фамильяр."),
70: ("B-But...", "Н-Но…"),
71: ("...", "…"),
72: ("There are a lot of soldiers here. Were you in the middle of a meeting?",
     "Здесь много военных. У вас было совещание?"),
73: ("Yes. That's why I called you.", "Да. Поэтому я вас и позвала."),
74: ("What do you mean, Your Majesty?", "Что вы имеете в виду, Ваше Величество?"),
75: ("Your Majesty, shall we resume the meeting soon?", "Ваше Величество, не пора ли возобновить совещание?"),
76: ("Whatever your reasoning, waiting for such children has cost us considerable time.",
     "Как бы вы ни объясняли, ожидание этих детей отняло у нас много времени."),
77: ("...", "…"),
78: ("Rude.", "Грубо."),
79: ("True. This is urgent. A map of the capital, here.", "Верно. Дело срочное. Карту столицы сюда."),
80: ("Yes.", "Так точно."),
81: ("Thank you. About the bombings occurring around the capital lately...",
     "Спасибо. О взрывах, которые в последнее время происходят по всему городу…"),
82: ("I investigated them myself and arrived at a certain hypothesis.",
     "Я провела расследование сама и пришла к определённой гипотезе."),
83: ("I wanted to explain it to everyone and have you judge it.",
     "Я хотела объяснить её вам всем и услышать ваше суждение."),
84: ("You summoned us for something like this!?", "Вы позвали нас из-за такого!?"),
85: ("Rather than that, what do you intend to do about the enemy right before your eyes!?",
     "Вместо этого — что вы намерены делать с врагом у самых глаз!?"),
86: ("Hey, mister. Shut up for a bit and listen to the Princess. "
     "She thought hard about this, you know.",
     "Эй, дядя. Помолчи немного и послушай принцессу. Она сколько думала над этим, знаешь ли."),
87: ("M-Mister!? You—insolence!", "Д-Дядя!? Ты… дерзость!"),
88: ("S-Saito! Apologize at once!", "С-Сайто! Немедленно извинись!"),
89: ("No way.", "Ни за что."),
90: ("You...", "Ты…"),
91: ("Everyone, this is a meeting. Put away your swords!", "Все мы на совещании. Уберите мечи!"),
92: ("Grr...", "Грр…"),
93: ("I'm sorry, Your Majesty. My familiar's insult is my insult. Punish me.",
     "Простите, Ваше Величество. Оскорбление фамильяра — оскорбление хозяйки. Накажите меня."),
94: ("No, it's fine. My chairing of the meeting was at fault. Just a little more time, please.",
     "Нет, всё хорошо. Это я плохо вела совещание. Прошу ещё немного времени."),
95: ("...", "…"),
96: ("Then let's continue.", "Тогда продолжим."),
97: ("Look at the map. These are the sites of the bombings so far. First here, then here...",
     "Смотрите на карту. Это места всех взрывов. Сначала здесь, потом здесь…"),
98: ("Eh, this is...?", "А, это…?"),
99: ("They're arranged in a circle around the castle.", "Они расположены по кругу вокруг замка."),
100: ("Yes. This can't be coincidence.", "Да. Это не может быть совпадением."),
101: ("If it's not coincidence, then what...?", "Если не совпадение, то что же…?"),
102: ("Repairing the bomb sites requires more craftsmen than this country has. "
      "So many from abroad were brought in.",
      "Для восстановления мест взрывов не хватает своих ремесленников. "
      "Поэтому пригласили многих из-за границы."),
103: ("If those craftsmen were honest, fine... But considering the bombings...",
      "Если бы эти ремесленники были честными — хорошо. Но, учитывая взрывы…"),
104: ("So you mean...?", "То есть…?"),
105: ("The culprit is a bomb-loving craftsman!? Or did they hire a fireworks maker by mistake!?",
      "Преступник — ремесленник, любящий бомбы!? Или наниматели перепутали строителя с фейерверкером!?"),
106: ("I so regret summoning you right now.", "Сейчас я ужасно жалею, что вызвала тебя."),
107: ("What, Louise. You look depressed... Maybe I'm wrong?",
      "Что, Луиза. Ты выглядишь уныло… Может, я неправ?"),
108: ("The craftsmen were called after the incidents, right? Then why bomb first! "
      "That bomb-loving craftsman!",
      "Ремесленников позвали после случаев, верно? Так зачем сначала взрывать! Этот любитель бомб!"),
109: ("R-Right.", "Д-Да."),
110: ("You mean an agent may have infiltrated disguised as a craftsman?",
      "То есть агент мог проникнуть под видом ремесленника?"),
111: ("If so, the bomb sites by now...", "Если так, то места взрывов сейчас…"),
112: ("Yes, exactly.", "Да, именно."),
113: ("A craftsman who wanted to sightsee in the capital caused the bombings!? "
      "What a roundabout way...!",
      "Ремесленник, который хотел посмотреть столицу, устроил взрывы!? Какой окольный путь…!"),
114: ("Idiot! Why would he!", "Дурак! Зачем ему!"),
115: ("Eh, am I wrong?", "А, я неправ?"),
116: ("Completely wrong!", "Совсем неправ!"),
117: ("Most likely, taking this chance, an agent has infiltrated disguised as a craftsman...",
      "Скорее всего, воспользовавшись случаем, агент проник под видом ремесленника…"),
118: ("Nonsense! Impossible!", "Ерунда! Невозможно!"),
119: ("Why can you say that so certainly? Analyzing all the evidence and the culprit's "
      "movements, there's no other explanation.",
      "Почему вы так уверены? Если проанализировать все доказательства и действия преступника, "
      "другого объяснения нет."),
120: ("Then we must act quickly!", "Тогда нужно действовать быстро!"),
121: ("Yes. Investigate the craftsmen at once. It may already be too late...",
      "Да. Немедленно проверьте ремесленников. Возможно, уже слишком поздно…"),
122: ("Eek!", "Ай!"),
123: ("W-What was that!?", "Ч-Что это было!?"),
124: ("Has the bomber come for the castle?", "Бомбист пришёл за замком?"),
125: ("Wait. This attack is—Report the situation!", "Подождите. Эта атака… Доложите обстановку!"),
126: ("Yes! Shelling toward the palace confirmed from points all over the city!",
      "Так точно! Обстрел дворца из разных точек города подтверждён!"),
127: ("Cannons inside the city? How is that possible?", "Орудия в городе? Как это возможно?"),
128: ("Reports say the cannons are installed at the sites of the recent bombings' repairs!",
      "По сообщениям, орудия установлены на местах восстановления после недавних взрывов!"),
129: ("There are cannons too! To let the enemy into this city... What has happened...!",
      "Даже орудия! Позволить врагу войти в этот город… Что же случилось…!"),
130: ("Your Majesty, one more... report.", "Ваше Величество, ещё один… доклад."),
131: ("And that is?", "И что же?"),
132: ("Scouts report Reconquista's aerial fleet has begun moving toward Tristain.",
      "Разведка сообщает, что воздушный флот Реконкисты начал двигаться к Тристании."),
133: ("What!? Have they already forgotten their defeat the other day!",
      "Что!? Неужели они забыли поражение на днях!"),
134: ("At current speed, the fleet will enter Tristain's airspace in a little under two days.",
      "При текущей скорости флот войдёт в воздушное пространство Тристании чуть меньше чем через два дня."),
135: ("All available units—recover the cannons immediately! "
      "Mages, don't lose sight of the fleet!",
      "Все доступные части — немедленно отбить орудия! Магам не терять флот из виду!"),
136: ("Yes!", "Так точно!"),
137: ("Also, evacuate residents near the cannons at once! "
      "Not a single drop of our people's blood may be spilled in Tristain!",
      "Также немедленно эвакуируйте жителей рядом с орудиями! "
      "Ни капли крови населения не должно пролиться в Тристании!"),
138: ("Yes!", "Так точно!"),
139: ("(The officers are leaving one by one. Should we go too...?)",
      "(Офицеры один за другим выходят. Нам тоже идти…?)"),
140: ("...", "…"),
}
CHOICES = {
670: [("Louise, cut it out", "Луиза, хватит"),
      ("Kirche, that's a bit much...", "Кирке, ты слишком…"),
      ("Tabitha, stop them", "Табаса, останови их")],
675: [("A bomb-loving craftsman!?", "Ремесленник-любитель бомб!?"),
      ("An agent disguised as a craftsman!?", "Агент под видом ремесленника!?"),
      ("A sightseeing craftsman!?", "Ремесленник-турист!?")],
680: [("Princess, what we can do is...", "Принцесса, что мы можем сделать…"),
      ("I just follow Louise", "Я просто следую за Луизой"),
      ("The academy's in danger! We have to go back!", "Академии угрожает опасность! Надо вернуться!")],
}
SPK = {'サイト': 's', 'ルイズ': 'l', 'キュルケ': 'k', 'タバサ': 't',
       'コルベール': 'c', 'モンモランシー': 'm', 'オスマン': 'o',
       '味方Ａ': 'soldier', '将校': 'commander', 'アンリエッタ': 'h', 'null': 'th'}
START = {k: 0 for k in SPK.values()}


def main():
    data = json.load(open('reports/ch17/parse_670_695.json', encoding='utf-8'))
    script = ['# Глава 17, часть 1 (сцены 670–683): «女王の決断» — напряжение, совет.',
              '# Источник: ps2_source/chapters/chapter_18_女王の決断.txt (SCENE 670-683).',
              '', 'label ch17:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 683:
                break
            scene = x['no']
            script += ['label ch17_1_scene_%d:' % scene, '']
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
            tag = 'ch17_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch17_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch17_1_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 670 <= scene <= 683:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch17_1_scene_%d' % x['target']
                                          if 670 <= x['target'] <= 683 else 'ch17_2'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch17_2', '    return', '']
    files = {
        'game/chapters/17/script-ch17_1.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch17_1_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch17_1_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch17_1_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch17_1_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch17/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
