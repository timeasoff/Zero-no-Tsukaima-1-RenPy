#!/usr/bin/env python3
"""Chapter 18 part 1 (scenes 696-705): return to academy, Akina's rampage."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("We seem to have slipped through the encirclement. That's where our escort ends, "
    "Valliere-sama, Saito-sama.",
    "Кажется, мы прорвались через кольцо. Здесь наша охрана заканчивается, "
    "мадемуазель Вальер, Сайто-сама."),
1: ("We'd like to see you to the academy, but protecting the capital and Her Majesty "
    "comes first right now.",
    "Мы бы хотели проводить вас до академии, но сейчас важнее всего защищать "
    "столицу и Её Величество."),
2: ("Yes, thank you. Please convey my thanks to the Queen.",
    "Да, спасибо. Передайте мою благодарность Королеве."),
3: ("Thanks for everything. Get back safely.", "Спасибо за всё. Возвращайтесь осторожно."),
4: ("Yes, then...", "Так точно, тогда…"),
5: ("I wonder if that soldier will be all right going back...",
    "Интересно, тот солдат доберётся обратно…"),
6: ("He will. Surely.", "Доберётся. Наверное."),
7: ("Surely, huh... The cannons will get more active as time passes, won't they?",
    "Наверное, да… Со временем орудия будут стрелять чаще, да?"),
8: ("Our priority is to do our own jobs. Right?", "Наш приоритет — делать своё дело. Верно?"),
9: ("Ugh.", "Ох."),
10: ("More importantly, let's get back to the academy as fast as we can and return "
     "to Tristain in the Zero Fighter.",
     "Главное — как можно скорее вернуться в академию и на Zero Fighter "
     "вернуться в Тристанию."),
11: ("...", "…"),
12: ("Saito?", "Сайто?"),
13: ("Louise, like I said last night... are you really okay with this?",
     "Луиза, как я и говорил вчера… Ты правда согласна на это?"),
14: ("W-What's 'okay'?!", "Ч-Что «согласна»?!"),
15: ("I'd rather not go to the battlefield. And I don't want you to go either.",
     "Я бы не хотел идти на поле боя. И тебе я тоже не хочу."),
16: ("...", "…"),
17: ("Sure, I'm your familiar—if you order me, I'll go with you to the battlefield. But...",
     "Конечно, я твой фамильяр — если прикажешь, пойду с тобой на поле боя. Но…"),
18: ("(I don't want Louise to be in danger again.)", "(Я не хочу, чтобы Луиза опять оказалась в опасности.)"),
19: ("(That last time was just luck. It doesn't mean we'll succeed this time either.)",
     "(В прошлый раз просто повезло. Это не значит, что и сейчас получится.)"),
20: ("Enough!", "Хватит!"),
21: ("Louise...", "Луиза…"),
22: ("If you keep waffling, I'll go alone.", "Если ты будешь тянуть, я пойду одна."),
23: ("That's not what I'm saying—that I don't want to fight. Don't you get it?",
     "Я не о том, что не хочу сражаться. Неужели не понимаешь?"),
24: ("Dawdling on the road won't help. Right now, too, Tristain and the Queen are in danger.",
     "Болтовня в дороге ни к чему. Сейчас Тристании и Королеве грозит опасность."),
25: ("If you're my familiar, you should at least... Ah, what's that!?",
     "Раз ты мой фамильяр, ты бы хоть… Ах, что это!?"),
26: ("That sound? U-Up there!?", "Этот звук? В-Вверху!?"),
27: ("It's Sylphid! Tabitha's familiar!", "Это Сильфида! Фамильяр Табасы!"),
28: ("Found you.", "Нашла."),
29: ("So it is Tabitha. Came to pick us up?", "Так и есть Табаса. Пришла за нами?"),
30: ("Perfect. Take us to the academy at once. The capital is...",
     "Как раз. Отведи нас в академию немедленно. Столица…"),
31: ("Hurry. Get on.", "Быстро. Садитесь."),
32: ("Hurry? Why? Something happen at the academy?", "Быстро? Почему? Что случилось в академии?"),
33: ("Haruna's gone wild.", "Харуна буйствует."),
34: ("Haruna? No way!", "Харуна? Не может быть!"),
35: ("She can't use magic, and she can't even handle a weapon properly!",
     "Она же не умеет колдовать и даже с оружием обращается плохо!"),
36: ("Right! She's just a commoner, no matter how you look at her.",
     "Да! Как ни смотри, она просто жительница."),
37: ("T-That really is Haruna? Are you sure you're not mistaken?",
     "Т-Это правда Харуна? Ты не ошиблась?"),
38: ("Y-Yes. A commoner throwing a tantrum couldn't beat Kirche, could she?",
     "Д-Да. Простой жительнице с её выходками не победить Кирке, правда?"),
39: ("What's happened to you, Haruna...?", "Что с тобой, Харуна…?"),
40: ("Even if Haruna went wild, would the academy explode into chaos?",
     "Даже если Харуна буйствует — неужели академия подняла бы переполох?"),
41: ("Right! She was just a normal girl who couldn't use magic.",
     "Да! Она была обычной девушкой, которая не умела колдовать."),
42: ("Explain what's going on. Haruna has no reason to go wild.",
     "Объясни, что происходит. У Харуны нет причины буйствовать."),
43: ("I don't know either. Maybe Kirche doesn't.", "Я тоже не знаю. Может, Кирке."),
44: ("I see. Let's hurry anyway.", "Понятно. В любом случае, идём быстрее."),
45: ("O-Okay.", "Т-Так точно."),
46: ("(We rode Tabitha's Sylphid to the academy. What on earth happened...?)",
     "(Мы полетели на Сильфиде Табасы в академию. Что же случилось…?)"),
47: ("What is the meaning of this?", "Что это значит?"),
48: ("Hey, partner, this is...", "Эй, приятель, это…"),
49: ("It's like a war zone. Are you sure Haruna is the cause...?",
     "Будто здесь прошла война. Ты уверен, что причина — Харуна…?"),
50: ("Hurry...", "Быстрее…"),
51: ("Saito, Louise! Thank goodness, you finally came.", "Сайто, Луиза! Слава богу, вы наконец."),
52: ("Montmon! What's happening? Tell me the situation.", "Монмон! Что происходит? Расскажи обстановку."),
53: ("The situation, I... We were eating breakfast when screams and explosions came "
     "from the plaza. Guiche and I went to see...",
     "Обстановка… Мы завтракали, когда с площади донеслись крики и взрывы. "
     "Мы с Гишем пошли посмотреть…"),
54: ("Haruna was setting off bombs all over the place.", "Харуна взрывала всё вокруг."),
55: ("Of course Guiche summoned a golem and attacked, but...",
     "Конечно, Гиш вызвал голема и атаковал, но…"),
56: ("Routed in no time, I suppose.", "И его разбили в мгновение ока, да?"),
57: ("But there are teachers at the academy, aren't there? One girl couldn't...",
     "Но в академии же есть преподаватели? Одна девушка не смогла бы…"),
58: ("That's just it—they can't! Come here, quickly.", "В том и дело, что не могут! Идите сюда, быстро."),
59: ("Ahahaha! What's wrong, Kirche? Is that your great fire magic?",
     "А-ха-ха! Что случилось, Кирке? Это твоя великая магия огня?"),
60: ("Tch! She's too fast!", "Тьфу! Она слишком быстрая!"),
61: ("Kirche!", "Кирке!"),
62: ("Darling... You finally came.", "Дорогой… Ты наконец пришёл."),
63: ("Hn, so you've come at last... The legendary Gandálfr.",
     "Хм, вот вы и пришли… Легендарный Гандальв."),
64: ("Kirche! Why are you struggling against a mere commoner!?",
     "Кирке! Почему ты не справляешься с простой жительницей!?"),
65: ("Explosions are faster than spells. I've never seen anything like it!",
     "Взрывы быстрее заклинаний. Я такого никогда не видела!"),
66: ("Haruna... Why are you doing this!", "Харуна… Зачем ты это делаешь!"),
67: ("Don't call me by that name!", "Не называй меня этим именем!"),
68: ("Eh?", "А?"),
69: ("I'm not Haruna. My name is... Akina.", "Я не Харуна. Меня зовут… Акина."),
70: ("Akina? But... you look exactly like Haruna in every way!",
     "Акина? Но… ты же во всём похожа на Харуну!"),
71: ("Partner, careful. It looks like magic is at work.", "Приятель, осторожно. Похоже, здесь действует магия."),
72: ("What!", "Что!"),
73: ("Heh, as expected of the legendary sword. This body is indeed Haruna's. "
     "But the one inside, moving it, is different.",
     "Хе, как и подобает легендарному мечу. Это тело и правда Харуны. "
     "Но тот, кто внутри и им управляет, — другой."),
74: ("You don't mean... a split personality?", "Неужели… раздвоение личности?"),
75: ("What's that?", "Что это?"),
76: ("Simply put, there are two people in one body.", "Проще говоря, в одном теле двое."),
77: ("How could you! You used forbidden magic to control someone's heart!",
     "Как ты могла! Ты использовала запретную магию, чтобы управлять чужим сердцем!"),
78: ("You're quick to understand, aren't you.", "Быстро соображаешь, однако."),
79: ("What happened to Haruna!?", "Что случилось с Харуной!?"),
80: ("Worried about Haruna? Don't be. Haruna is alive.", "Волнуешься за Харуну? Не надо. Харуна жива."),
81: ("While I'm asleep, Haruna stays Haruna.", "Пока я сплю, Харуна остаётся Харуной."),
82: ("And while Haruna sleeps, I move this body. That's the arrangement.",
     "А пока спит Харуна, этим телом двигаюсь я. Таков порядок."),
83: ("Quite ridiculous, isn't it.", "Довольно смешно, правда?"),
84: ("Haruna has no idea what terrible things she does while she's asleep...",
     "Харуна даже не знает, что страшного она делает, пока спит…"),
85: ("...", "…"),
86: ("Haruna came to Halkeginia quite some time ago.", "Харуна прибыла в Халкегинию давно."),
87: ("And the one who took her in asked about her circumstances, where she came from— "
     "and decided she could be useful.",
     "А тот, кто её приютил, расспросил о её делах, о том, откуда она, — "
     "и решил, что она может пригодиться."),
88: ("To investigate Saito and his mistress Louise, the legendary familiar of Tristain.",
     "Чтобы разузнать о Сайто и его госпоже Луизе — легендарном фамильяре Тристании."),
89: ("O-Us!?", "О-Нас!?"),
90: ("Yeah. I've been watching you all this time.", "Да. Я всё это время наблюдала за вами."),
91: ("I had every piece of information sent to my mistress.",
     "Я отправляла моей госпоже каждую весть."),
92: ("On the side, while I was busy with my other job—sabotage...",
     "Между делом, пока я занималась своей другой работой — диверсиями…"),
93: ("It was a rather easy assignment, though.", "Впрочем, задание было нетрудным."),
94: ("Sabotage... So the bombings everywhere were...", "Диверсии… Значит, взрывы повсюду это…"),
95: ("Just as you guessed. My doing.", "Как ты и догадался. Моя работа."),
96: ("Who's your mastermind!?", "Кто твой хозяин!?"),
97: ("Well now... You'll find out soon enough, won't you?", "Ну что ж… Скоро узнаешь, правда?"),
98: ("Saito, we'll capture her!", "Сайто, мы её схватим!"),
99: ("B-But that means attacking Haruna!", "Н-Но это значит напасть на Харуну!"),
100: ("Everyone's lives are at stake. Get a grip!", "На кону жизни всех. Возьми себя в руки!"),
101: ("If it comes to this, I'll do it! Let's go, Louise.", "Раз так, я сделаю это! Идём, Луиза."),
102: ("I know!", "Я знаю!"),
103: ("Both of you, wait! I can't agree to charging in without knowing how she'll act.",
     "Вы двое, подождите! Я не могу одобрить лобовую атаку, не зная, как она действует."),
104: ("Tch. Then what should we do?", "Тьфу. Тогда что нам делать?"),
105: ("W-What should we do!", "Ч-Что нам делать!"),
106: ("Why are you standing there! Let's go!", "Что ты стоишь! Идём!"),
107: ("Both of you, wait! I can't agree to charging in without knowing how she'll act.",
     "Вы двое, подождите! Я не могу одобрить лобовую атаку, не зная, как она действует."),
108: ("That's... Then what do we do?", "Это… Тогда что нам делать?"),
109: ("I refuse. She may be Akina now, but she's still Haruna.",
     "Я отказываюсь. Сейчас она может быть Акиной, но она всё равно Харуна."),
110: ("And the real Haruna's personality isn't gone. She's just being controlled by Akina.",
     "И настоящая личность Харуны не исчезла. Ей просто управляет Акина."),
111: ("Grr...", "Грр…"),
112: ("Watch a little longer. She might leave an opening.", "Понаблюдайте ещё. Возможно, она оставит лазейку."),
113: ("...Damn!", "…Чёрт!"),
114: ("I know why you've come back to this academy. To use that Zero Fighter... right?",
     "Я знаю, зачем вы вернулись в академию. Чтобы завести тот Zero Fighter… верно?"),
115: ("I won't let you. Reconquista's victory is assured, but I can't leave loose ends.",
     "Я не позволю. Победа Реконкисты несомненна, но нельзя оставлять неопределённость."),
116: ("I'll keep you from leaving this place. If you don't listen...",
     "Я не дам вам уйти отсюда. Если не послушаетесь…"),
117: ("Eek!", "Ай!"),
118: ("I've had bombs planted all over the academy. They can be detonated anytime "
     "on my signal.",
     "Я везде в академии заложила бомбы. Они могут взорваться в любой момент "
     "по моему сигналу."),
119: ("So you won't leave, I'll watch from the highest place.", "Чтобы вы никуда не ушли, я буду наблюдать с самой высокой точки."),
120: ("Tch...", "Тьфу…"),
121: ("See, Saito! Stand aside! Do you want me to blow this place up right now?",
     "Ну же, Сайто! Дорогу! Хочешь, я взорву всё прямо сейчас?"),
122: ("Fine...", "Ладно…"),
123: ("This is a fine mess, partner. Who'd have thought that girl was a spy.",
     "Вот дела, приятель. Кто бы подумал, что та девушка — шпион."),
124: ("Haruna isn't a spy. It's Akina—it's magic controlling her!",
     "Харуна не шпион. Это Акина — ею управляет магия!"),
125: ("What, what, what! We have no time to waste here, Louise and I—",
     "Что, что, что! У нас нет времени здесь тратить, у меня с Луизой—"),
126: ("—no time to waste in a place like this!!", "—нет времени торчать в таком месте!!"),
}
CHOICES = {
696: [("Haruna? No way!", "Харуна? Не может быть!"),
      ("Is it really Haruna?", "Это правда Харуна?"),
      ("What happened to you, Haruna...?", "Что с тобой, Харуна…?")],
701: [("If it comes to this, I'll do it!", "Раз так, я сделаю это!"),
      ("Think", "Подумать"),
      ("Refuse!", "Отказаться!")],
}
SPK = {'味方Ａ': 'soldier', 'ルイズ': 'l', 'サイト': 's', 'タバサ': 't',
       'デルフリンガー': 'd', 'モンモランシー': 'm', 'ハルナ': 'ha',
       'キュルケ': 'k', 'アキナ': 'ak', 'null': 'th'}
START = {k: 0 for k in SPK.values()}
# continue numbering from ch17
START.update({'s': 82, 'l': 60, 't': 3, 'd': 6, 'm': 4, 'k': 7, 'ak': 0, 'soldier': 7, 'th': 0})


def main():
    data = json.load(open('reports/ch18/parse_696_738.json', encoding='utf-8'))
    script = ['# Глава 18, часть 1 (сцены 696–705): «貴族の意地» — возвращение, Акина.',
              '# Источник: ps2_source/chapters/chapter_19_貴族の意地.txt (SCENE 696-705).',
              '', 'label ch18:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 705:
                break
            scene = x['no']
            script += ['label ch18_1_scene_%d:' % scene, '']
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
            tag = 'ch18_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch18_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch18_1_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 696 <= scene <= 705:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch18_1_scene_%d' % x['target']
                                          if 696 <= x['target'] <= 705 else 'ch18_2'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch18_2', '    return', '']
    files = {
        'game/chapters/18/script-ch18_1.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch18_1_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch18_1_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch18_1_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch18_1_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch18/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
