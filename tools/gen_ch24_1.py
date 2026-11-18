#!/usr/bin/env python3
"""Chapter 24 part 1 (scenes 894-902): sailor uniform, Haruna leaves, Siesta's promise."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("Siesta!", "Сиэста!"),
1: ("Oh, Saito-san. What's the matter? You look so happy today.",
    "Ох, Сайто-сан. Что случилось? Вы сегодня такой радостный."),
2: ("Heh heh~, of course I am.", "Хи-хи~, конечно."),
3: ("Today I brought a present for Siesta!", "Сегодня я принёс Сиэсте подарок!"),
4: ("Eh? For me?", "А? Мне?"),
5: ("That's right~! Ta-daaa!! Look at this wrapping paper!!",
    "Верно~! Та-да-а-а!! Смотрите на эту упаковку!!"),
6: ("Wow, it's cute... What's inside?", "Ох, какая милая… Что внутри?"),
7: ("That's for you to find out once you open it. Here, open it, open it.",
    "Это сюрприз, узнаешь, когда откроешь. Давай, открывай, открывай."),
8: ("Ah, thank you... I'm so happy...", "Ах, спасибо… Я так рада…"),
9: ("This is... a sailor's... clothes?", "Это… форма моряка…?"),
10: ("Correct!", "Верно!"),
11: ("It's called a sailor uniform. In Japan, cute girls like Siesta wear it to study!",
     "Это называется «салеру фуку» — школьная форма. В Японии такие милые девушки, "
     "как Сиэста, носят её, когда учатся!"),
12: ("Studying... So it's a uniform students wear, right?", "Учёба… Значит, это форма учениц, да?"),
13: ("That's right! So I want Siesta to wear it, too!", "Верно! Поэтому я хочу, чтобы и Сиэста её надела!"),
14: ("Is that really all right?", "Это и правда можно?"),
15: ("Of course it is. More importantly, will you put it on right now?",
     "Конечно можно. Главное — надень её прямо сейчас, ладно?"),
16: ("Eh!? Right now!?", "А!? Прямо сейчас!?"),
17: ("Yep, I'm looking forward to it, Siesta-san. Put it on. Put it on, put it on.",
     "Ага, я жду с нетерпением, Сиэста-сан. Надевай. Надевай, надевай, надевай."),
18: ("W-Well, you've made me curious. Wait a moment, I'll change right away...",
     "Н-Ну, вы так ждёте этого. Подождите немного, я сразу переоденусь…"),
19: ("(...Yes! Soon I'll get to see Siesta in a sailor uniform!!)",
     "…Да! Скоро я увижу Сиэсту в школьной форме!!"),
20: ("Saito-san... Sorry to keep you waiting!!", "Сайто-сан… Простите за ожидание!!"),
21: ("Heh heh... How do I look? Does it suit me?", "Хи-хи… Как я выгляжу? Идёт мне?"),
22: ("Ooooohooooo!!", "О-о-о-о-о!!"),
23: ("My, Saito-san, your voice is so loud.", "Ой, Сайто-сан, вы так громко."),
24: ("Ugh... Sniff... I'm glad I'm alive!", "Ох… Хлюп… Я рад, что живу!"),
25: ("...Huh? Um, Saito-san, why are you crying?", "…А? Э-Э, Сайто-сан, почему вы плачете?"),
26: ("No, it's just—seeing you like this is so dazzling! Japan came rushing back to me.",
     "Нет, дело в том — вы так ослепительны! Я вдруг вспомнил Японию."),
27: ("Ah! I've never felt the light of Halkeginia shine this brightly before!!",
     "Ах! Никогда ещё свет Халкегии не казался мне таким ярким!!"),
28: ("Are you all right, Saito-san? I have a handkerchief here... Here.",
     "Вы в порядке, Сайто-сан? У меня есть платок… Вот."),
29: ("Thank you, Siesta. That uniform really suits you!", "Спасибо, Сиэста. Эта форма и правда тебе идёт!"),
30: ("R-Really? It's the first time I've worn something so... revealing, and I'm a bit embarrassed...",
     "П-Правда? Я впервые в такой… открытой одежде, и мне немного неловко…"),
31: ("N-No, that's exactly what's good about it...", "Н-Нет, в этом как раз и прелесть…"),
32: ("Just what are you looking at!? Idiot!!", "Что ты смотришь!? Дурак!!"),
33: ("Gyaaaaaah!! L-Louise... Why are you here!?", "Гя-а-а-а!! Л-Луиза… Откуда ты здесь!?"),
34: ("What are you making Siesta wear!? Honestly, have you no shame as a person!?",
     "Что ты заставляешь Сиэсту носить!? Право, у тебя нет стыда как у человека!?"),
35: ("Guh... Flop.", "Гух… Бата."),
36: ("S-Saito-san!! Pull yourself together!!", "С-Сайто-сан!! Придите в себя!!"),
37: ("Leave him be, he's an idiot!! Siesta, take that off at once, too!!",
     "Оставь его, он дурак!! Сиэста, ты тоже сейчас же это сними!!"),
38: ("Eh, but this is the student uniform Saito-san gave me...", "Ах, но это же школьная форма, "
     "которую подарил Сайто-сан…"),
39: ("Then that, too, is confiscated!", "Тогда её тоже конфискуют!"),
40: ("Ugh... If Siesta's no good... Maybe Louise would wear it...",
     "Ох… Если Сиэста не годится… Может, Луиза наденет…"),
41: ("Did you say something?", "Ты что-то сказала?"),
42: ("Eeeeeh!!", "И-и-и!!"),
43: ("Yes, now you must atone at once! Brace yourself!!", "Да, сейчас же искупи вину! Приготовься!!"),
44: ("Gyaaaaah...", "Гя-а-а-а…"),
45: ("It's nothing, really...", "Ничего, правда…"),
46: ("Hmph... Well, come quickly. Or I'll tie you up with a collar and a belt.",
     "Хмф… Ну, иди скорее. А то свяжу тебя ошейником и ремнём."),
47: ("Yaah... Once I recover, I'll come at once.", "Ой… Как только приду в себя, сразу приду."),
48: ("I'll wear it myself!", "Я сам её надену!"),
49: ("Huh? What are you talking about? Or have you finally awakened something?",
     "А? Что ты несёшь? Или ты наконец что-то в себе пробудил?"),
50: ("Awakened what!?", "Пробудил что!?"),
51: ("Fine. Anyway, I'm confiscating this. See you.", "Ладно. В любом случае я это изыму. До встречи."),
52: ("Saito-san... Please pull yourself together.", "Сайто-сан… Придите в себя, пожалуйста."),
53: ("Ah ha... Ha ha. I'm fine, this much...", "А-ха… Ха-ха. Я в порядке, это пустяки…"),
54: ("It was such a nice present, though. What a shame.", "Такой хороший подарок — и вот. Жаль."),
55: ("But next time I'll try making a sailor uniform myself. So look forward to it!",
     "Но в следующий раз я попробую сшить школьную форму сама. Так что ждите с нетерпением!"),
56: ("R-Really!?", "П-Правда!?"),
57: ("Yes! I'll do my best for Saito-san! Let's go on a date in matching outfits!",
     "Да! Я постараюсь ради Сайто-сан! Давайте пойдём на свидание в одинаковой одежде!"),
58: ("...Eh?", "…А?"),
59: ("(Even as I looked forward to Siesta's handmade sailor uniform, I felt a little uneasy.)",
     "Хотя я с нетерпением ждал сшитую Сиэстой форму, мне было немного не по себе."),
60: ("Eh? What do you mean, becoming independent?", "А? Что значит — стать самостоятельной?"),
61: ("Yeah. I can't stay at this academy forever... It'd be wrong to keep relying on Louise and the others.",
     "Да. Вечно оставаться в этой академии… Я и сама не знаю, правильно ли всё время полагаться на Луизу и остальных."),
62: ("If you say that, then I've been taken care of by this academy ever since Louise summoned me.",
     "Если так, то меня опекает эта академия с тех пор, как Луиза меня призвала."),
63: ("Hiraga-kun is Louise-san's familiar. Of course you're taken care of. But I'm not one, so...",
     "Хирага-кун — фамильяр Луизы-сан. Вам и положено. А я нет, поэтому…"),
64: ("I know, but... We're probably the only two Japanese people in this world.",
     "Я знаю, но… Мы, наверное, единственные японцы в этом мире."),
65: ("And we're not exactly strangers to each other... So if we worked at the academy, maybe...",
     "И мы не совсем чужие друг другу… Так что если бы мы работали в академии, может…"),
66: ("The thing is, Hiraga-kun... I've been scouted.", "Дело в том, Хирага-кун… Меня завербовали."),
67: ("S-Scouted for what?", "З-Завербовали — куда?"),
68: ("A theater troupe, a theater troupe.", "В театральную труппу, в труппу."),
69: ("A theater troupe? I thought Weatherly's troupe was gone?", "Труппу? Я думал, труппы Уэзерби больше нет?"),
70: ("No. Someone from another troupe who saw that play liked me and scouted me.",
     "Нет. Кто-то из другой труппы, кто смотрел тот спектакль, меня и завербовал."),
71: ("Now's a good chance, so I've decided to join that troupe.",
     "Сейчас как раз удобный случай, и я решила присоединиться к этой труппе."),
72: ("But if you join a troupe, you'll have to go on tours to other towns, won't you?",
     "Но если ты в труппе, тебе придётся ездить с гастролями в другие города, да?"),
73: ("Yeah. I probably won't get to see Hiraga-kun very often anymore.",
     "Ага. Наверное, мы с Хирага-куном будем видеться реже."),
74: ("But I'm looking forward to it. I get to see all sorts of towns in this world.",
     "Но я с нетерпением жду. Я смогу объездить разные города этого мира."),
75: ("Maybe I'll even find a clue to get back to Japan.", "Может, я даже найду ключ к дороге в Японию."),
76: ("I see. Yeah, that's right.", "Понятно. Да, верно."),
77: ("So, Hiraga-kun... If you don't mind, cheer me on, okay?",
     "Так что, Хирага-кун… Если не против, поддержи меня, ладно?"),
78: ("Of course I will! And let's both do our best to find a way back to Japan!",
     "Конечно! И давай вместе постараемся найти способ вернуться в Японию!"),
79: ("Mm!", "Мм!"),
80: ("(I hear Weatherly was caught while trying to blend in with the panicked soldiers.)",
     "Говорят, Уэзерби поймали, когда она пыталась затеряться среди паникующих солдат."),
81: ("(Behind Weatherly, apparently, was Reconquista. A military meeting was held at once.)",
     "За Уэзерби, кажется, стояла Реконкиста. Сразу же провели военное совещание."),
82: ("(The hypnosis magic controlling Haruna was undone by Weatherly.)",
     "Магию гипноза, которой управляли Харуной, сняла Уэзерби."),
83: ("(With that, the whole bomber affair has come to an end.)", "На этом вся история с бомбистом закончилась."),
84: ("Well then, let's head home, too.", "Ну что ж, и нам пора домой."),
85: ("But we ended up staying so long because of Weatherly and Haruna, didn't we?",
     "Но из-за Уэзерби и Харуны мы задержались так надолго, да?"),
86: ("Yeah. But everyone's waiting for us to get back.", "Да. Но все ждут нашего возвращения."),
87: ("Right, I suppose so. I wonder how everyone is doing right about now?",
     "Верно. Интересно, как у всех дела прямо сейчас?"),
88: ("Saiiiito-saaaaan!!", "Сайтоооо-саааан!!"),
89: ("Eh!? Th-That voice is...!", "А!? Э-Этот голос…!"),
90: ("No way, why is she here!?", "Не может быть, почему она здесь!?"),
91: ("Saito-san!! I... found you!!", "Сайто-сан!! Я… нашла вас!!"),
92: ("Whoa, what's wrong, Siesta?", "Ой, что случилось, Сиэста?"),
93: ("You two weren't coming back for so long, I got worried and came to check on you!!",
     "Вы всё не возвращались, и я волновалась и пришла посмотреть, что с вами!!"),
94: ("Well, as you can see—I'm completely fine.", "Ну, как видишь — я в полном порядке."),
95: ("Thank goodness!", "Слава богу!"),
96: ("Ah, that's right, Siesta. I'll return the charm I borrowed, just as I promised.",
     "Ах, да, Сиэста. Я верну одолженный оберег, как и обещал."),
97: ("When I fought the bomber, thanks to it I got through without injury.",
     "Когда я сражался с бомбистом, благодаря ему я обошёлся без ран."),
98: ("Really? Thank goodness. Great-grandfather must have protected you, Saito-san.",
     "Правда? Слава богу. Значит, прадедушка защитил вас, Сайто-сан."),
99: ("Ah, I'm sure he did.", "Ах, я уверен, что так и было."),
100: ("A charm, huh... Nice, isn't it... a charm.", "Оберег, значит… Хорошо же… оберег."),
101: ("What's that? It's fine, isn't it? Besides, Louise is my charm, right?",
      "Что это? Нормально же, правда? И к тому же я — оберег Луизы, да?"),
102: ("T-That's right!! My charm is only Saito!", "В-Верно!! Мой оберег — только Сайто!"),
103: ("Then I'll become Saito-san's charm!", "Тогда я стану оберегом Сайто-сан!"),
104: ("Eh!?", "А!?"),
105: ("If it's for praying for your safety... I'll kiss you again, like before!!",
      "Если ради того, чтобы молиться за вашу безопасность… я снова вас поцелую, как раньше!!"),
106: ("K-Kiss!?", "П-Поцелую!?"),
107: ("Whoa, Siesta!!", "Ой, Сиэста!!"),
108: ("Oh, what have I done! To think I said I'd kissed... I'm so embarrassed!",
      "Ох, что я сделала! И сказать, что поцеловала… Мне так неловко!"),
109: ("Th-This girl... What did she do while I wasn't looking!?",
      "Э-Эта девушка… Что она сделала, пока я не смотрела!?"),
110: ("Eeeh... That was, um... Whoaaa!!", "Э-Э… Это было, э-э… О-о-о!!"),
111: ("No excuses! I'll beat that shameless, rotten attitude right out of you!",
      "Никаких оправданий! Я выбью из тебя этот беспринципный, прогнивший нрав!"),
112: ("I'm going to be killed!!", "Меня убьют!!"),
113: ("Hey! Stop right there! Don't you dare run away! Accept your fate!",
      "Эй! Стой! Не смей убегать! Смирись!"),
114: ("I didn't do anything wrong!", "Я же ничего плохого не сделал!"),
115: ("Shut up! As punishment for talking back—no meals for three days!",
      "Замолчи! В наказание за дерзость — три дня без еды!"),
116: ("T-That's too much!!", "Т-Это слишком!!"),
117: ("No! Absolutely! No exceptions!!", "Нет! Ни в коем случае! Без исключений!!"),
118: ("Gyaaaaah!!", "Гя-а-а-а!!"),
119: ("Honestly, you two—separate yourselves already!", "Право, вы двое — отойдите друг от друга!"),
120: ("No. I've decided. From now on, I'll be Saito-san's charm!",
      "Нет. Я решила. Сейчас я стану оберегом Сайто-сан!"),
121: ("So, Saito-san, please stay with me forever!", "Так что, Сайто-сан, оставайтесь со мной всегда!"),
122: ("Enough! I've decided! Saito is forbidden from getting cozy with Siesta!",
      "Хватит! Я решила! Сайто запрещено обниматься с Сиэстой!"),
123: ("Hah!? That's tyranny!", "А!? Это тирания!"),
124: ("Shut up! As punishment for talking back—no meals for a week!",
      "Замолчи! В наказание за дерзость — неделя без еды!"),
125: ("That's too much!!", "Это слишком!!"),
126: ("Then, Saito-san, won't you live in my room with me?", "Тогда, Сайто-сан, не пожелаете ли вы жить в моей комнате?"),
127: ("What was that!? Saito—what did you do with her while I wasn't looking!?",
      "Что вы сказали!? Сайто — что ты делал с ней, пока я не смотрела!?"),
128: ("Eeeh... That was, um... Whoaaa!!", "Э-Э… Это было, э-э… О-о-о!!"),
129: ("No excuses! I'll beat that shameless, rotten attitude right out of you!",
      "Никаких оправданий! Я выбью из тебя этот беспринципный, прогнивший нрав!"),
130: ("I'm going to be killed!!", "Меня убьют!!"),
131: ("O great Founder Brimir. Grant a moment's peace to poor Saito.",
      "Великий Основатель Бримир. Даруй минутный покой бедняге Сайто."),
132: ("(On a summer afternoon in Buldone, my screams, Louise's shouts and Siesta's prayers "
      "echoed up to the sky.)", "Во второй половине дня в Будоне мои крики, крики Луизы и молитвы "
      "Сиэсты звенели до неба."),
}
CHOICES = {
894: [("Let Louise wear it", "Пусть наденет Луиза"),
      ("Stay silent", "Промолчать (мужской кризис)"),
      ("I'll wear it myself!", "Я сам её надену!")],
899: [("Returns the charm", "Вернёт оберег"),
      ("Siesta's oath", "Клятва Сиэсты"),
      ("The fight continues", "Бой продолжится")],
}
SPK = {'サイト': 's', 'シエスタ': 'si', 'ルイズ': 'l', 'ハルナ': 'ha', 'null': 'th'}
START = {'s': 0, 'si': 0, 'l': 0, 'ha': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch24/parse_894_902.json', encoding='utf-8'))
    script = ['# Глава 24 (источник chapter_25): школьная форма, уход Харуны, клятва Сиэсты.',
              '# Источник: ps2_source/chapters/chapter_25_制服の魅力.txt (SCENE 894-902).',
              '', 'label ch24:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            scene = x['no']
            script += ['label ch24_1_scene_%d:' % scene, '']
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
            tag = 'ch24_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch24_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch24_1_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 894 <= scene <= 902: continue
            script.append('    # → next scene %d' % x['target'])
            if 894 <= x['target'] <= 902:
                script.append('    jump ch24_1_scene_%d' % x['target'])
            else:
                script.append('    jump ch25')
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 24 ====', '    jump ch25', '    return', '']
    files = {
        'game/chapters/24/script-ch24.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch24_1_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch24_1_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch24_1_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch24_1_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch24/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
