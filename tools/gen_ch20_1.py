#!/usr/bin/env python3
"""Chapter 20 part 1 (scenes 769-770): punishment, Haruna leaves, daily life."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
    0: ('Ah, perfect! Good, great, perfect, Siesta!', 'Ах, идеально! Хорошо, отлично, великолепно, Сиэста!'),
    1: ("I-Is that so... But this is a strange outfit, isn't it?", 'П-Правда… Но это странный наряд, да?'),
    2: ("Don't say that! This was the most popular uniform in the world I came from!", 'Не говори так! Это была самая популярная форма в мире, откуда я пришел!'),
    3: ("And its name is 'Blazer'!!", 'И называется она «блейзер»!!'),
    4: ('B-Blazer, is it... A-Ah ha ha...', 'Б-Блейзер… А-А-ха-ха…'),
    5: ('Man, this short checkered skirt, the neat navy jacket, and on top of that, these navy socks!!', 'Ох, эта короткая клетчатая юбка, аккуратный тёмно-синий жакет и, венец всего, эти тёмно-синие носки!!'),
    6: ('Haaah, looking at you like this makes me think of back home...', 'Ах, глядя на тебя так, я вспоминаю свой прежний мир…'),
    7: ('Haa...', 'Хаа…'),
    8: ('But Siesta, it really suits you.', 'Но Сиэста, тебе и правда идёт.'),
    9: ("It's similar to your usual maid uniform, but the shorter skirt really emphasizes how cute you are.", 'Он похож на твою обычную форму горничной, но короткая юбка ещё больше подчёркивает, какая ты милая.'),
    10: ("R-Really? Saito-san... I'm happy. Ehehe.", 'П-Правда? Сайто-сан… Я рада. Хи-хи.'),
    11: ("(Whoa, blushing in a blazer... That's way too moe.)", 'Ух, покраснела в блейзере… Это слишком моэ.'),
    12: ('SAAIITOOO!', 'САААЙТООО!'),
    13: ('Eep! Mistress!', 'Ой! Госпожа!'),
    14: ("While I looked away for just a moment, you dress the maid up in strange clothes and grin like an idiot. You've got some nerve, Saito.", 'Стоило мне отвернуться на миг, как ты нарядил горничную в странную одежду и ухмыляешься. Храбрости тебе не занимать, Сайто.'),
    15: ('S-Saito-san! I have some work to do, so excuse me!', 'С-Сайто-сан! Мне пора работать, извините!'),
    16: ('Ah, Siesta! Where are you going in that blazer!', 'Ах, Сиэста! Куда ты в блейзере!'),
    17: ("I won't let you escape, Saito!", 'Я не дам тебе убежать, Сайто!'),
    18: ('F-Forgive me...', 'П-Прости…'),
    19: ("I won't!", 'Не прощу!'),
    20: ('N-No way...', 'Н-Не может быть…'),
    21: ("You really are a familiar who ogles maids and Zerbst's daughter and so on...", 'Ты и правда фамильяр, который пялится на горничных и дочь Церпст… не так ли?'),
    22: ("Even a dog, if you keep it three days, learns loyalty to its master. You're not even a dog.", 'Даже пёс, если держать его три дня, учится верности господину. А ты даже не пёс.'),
    23: ("Looks like I'll have to train you thoroughly this time.", 'Похоже, на этот раз придётся воспитать тебя как следует.'),
    24: ('E-Eep! Mistress is scary! Your beautiful face is ruined!', 'Х-Хи-и!? Госпожа страшная! Ваше прекрасное лицо испорчено!'),
    25: ("Silence! It's all Saito's fault to begin with.", 'Молчи! Во всём виноват Сайто.'),
    26: ("If that's how it is, I'll punish you thoroughly! I'll make you remember your place.", 'Раз так, я накажу тебя как следует! Я напомню тебе твоё место.'),
    27: ('H-Hiiiii!', 'Х-Хи-и-и!'),
    28: ("W-Well. How about you wash mistress's back in the bath?", 'Т-Так. Как насчёт того, чтобы ты помыл госпоже спину в ванной?'),
    29: ('Heh?', 'А?'),
    30: ("H-How about it? It's humiliating, isn't it? It's punishment, isn't it?", 'Н-Ну как? Унизительно, да? Это наказание, да?'),
    31: ("U-Um, maybe I'd actually like it a little.", 'Э-Э, может, мне даже немного понравится.'),
    32: ('W-What was that! Treat it as punishment! Be afraid!', 'Ч-Что ты сказал! Считай это наказанием! Бойся!'),
    33: ("Y-Yes, it's punishment. I'm trembling, trembling, trembling.", 'Д-Да, наказание. Я дрожу, дрожу, дрожу.'),
    34: ("W-Well, if you understand, let's go to the bath together. I'll get ready, so wait there.", 'Т-Так, раз понял, пойдём в ванную вместе. Я подготовлюсь, а ты подожди здесь.'),
    35: ('Y-Yes.', 'Д-Да.'),
    36: ("(But... In the bath with Louise... And washing Louise's back...)", 'Но… В ванной с Луизой… И мыть Луизе спину…'),
    37: ('(......)', '……'),
    38: ('(No, no, this is punishment, punishment...)', 'Нет-нет, это наказание, наказание…'),
    39: ('(Punishment, punishment, punishment.)', 'Наказание, наказание, наказание.'),
    40: ('Hey, what are you muttering about? Hurry up and punish me.', 'Эй, что ты бормочешь? Быстрее наказывай.'),
    41: ('Yeees.', 'Д-дааа.'),
    42: ('Um, mistress. What is that swimsuit?', 'Э-Э, госпожа. Что это за купальник?'),
    43: ('And no matter how I look at it, it looks like a school swimsuit...', 'И как я ни смотрю, это похоже на школьный купальник…'),
    44: ('This swimsuit is a parting gift from Haruna.', 'Этот купальник — прощальный подарок от Харуны.'),
    45: ('A parting gift!?', 'Прощальный подарок!?'),
    46: ("She said to use it if you didn't listen to me.", 'Она сказала использовать его, если ты не будешь меня слушаться.'),
    47: ("Haruna... What did you think of me? I mean, I'm really happy, but...", 'Харуна… Что ты обо мне подумала? Я и правда рад, но…'),
    48: ('But I think going into the bath in a swimsuit is a mistake.', 'Но я думаю, входить в ванну в купальнике — ошибка.'),
    49: ("What are you talking about? I can't get in the bath with you without a swimsuit, can I?", 'О чём ты? Я же не могу войти в ванну с тобой без купальника, правда?'),
    50: ('Well, yes, I suppose.', 'Ну, да, наверное.'),
    51: ('Here.', 'Вот.'),
    52: ('Eh? Here, with this towel, what are you going to...', 'А? Вот, этим полотенцем, что ты собираешься…'),
    53: ("Oh, how slow you are!", 'Ох, какая же ты медленная!'),
    54: ("I'm telling you to wash my back. Ah, but before that...", 'Я говорю, помой мне спину. Ах, но перед этим…'),
    55: ("There's another towel, right? Don't forget to blindfold yourself tightly with it.", 'Там ещё одно полотенце, верно? Не забудь как следует завязать им глаза.'),
    56: ("When I wash my back, I'll show a little of it. If you even loosen the blindfold a bit... I'll kill you.", 'Когда я буду мыть спину, я её немного покажу. Если хоть чуть ослабишь повязку… я тебя убью.'),
    57: ('O-Okay...', 'Л-Ладно…'),
    58: ('Here, this should do, right?', 'Вот, так нормально, да?'),
    59: ("Mm, let's see... Hmm, seems you followed my order properly.", 'Мм, посмотрим… Хм, кажется, ты послушался как надо.'),
    60: ('All right. Ready. Hurry up and wash my back!', 'Ладно. Готово. Быстрей мой мне спину!'),
    61: ('Yehehe...', 'И-хи-хи…'),
    62: ("(Ah, I've touched it before, but Louise's back is so smooth...)", 'Ах, я уже трогал её раньше, но спина Луизы такая гладкая…'),
    63: ("(If only I weren't blindfolded... No, what am I thinking, me...)", 'Хоть бы я не был с завязанными глазами… Нет, что я думаю?'),
    64: ("How's it going, mistress? Does your back feel good?", 'Как дела, госпожа? Спине хорошо?'),
    65: ('Yeah, a little harder is fine.', 'Да, можно немного сильнее.'),
    66: ('Ouii...', 'Оуи…'),
    67: ('Ah, there, there... Mm, right there. More, focus on that spot.', 'Ах, тут, тут… Мм, именно тут. Ещё, сконцентрируйся на этом месте.'),
    68: ('Oooi.', 'Оу-уи.'),
    69: ("Hmm hmm hmm. Hey, Saito. What's going through your mind right now?", 'Хм-хм-хм. Эй, Сайто. О чём ты сейчас думаешь?'),
    70: ("Eh? I'm thinking about nothing in particular... Just a little lightheaded.", 'А? Я ни о чём особенно… Просто немного закружилась голова.'),
    71: ("(Bad. The steam is building up, the temperature is rising. It's like a sauna.)", 'Плохо. Пара слишком много, температура растёт. Как в сауне.'),
    72: ('Hmph, no need for sore-loser talk. Alone with me in the bath, washing my back and all...', 'Хмп, не нужно оправдываться. Наедине со мной в ванной, да ещё и моешь мне спину…'),
    73: ("Not being able to see a thing is painful, isn't it? Frustrating, isn't it? Honestly, it's torture.", 'Ничего не видеть — мука, да? Досадно, да? По чести, это пытка.'),
    74: ("Well, that's the real purpose of this punishment, though.", 'Ну, в этом и заключается истинная цель этого наказания.'),
    75: ("If you've learned your lesson, you won't neglect me again.", 'Если ты усвоишь урок, больше не будешь пренебрегать мной.'),
    76: ('(My head is spinning. Why is Louise fine with this?)', 'У меня голова идёт кругом. Почему Луизе нормально?'),
    77: ('Hey, Saito, are you listening to me? Your hands have been stopped for a while now!', 'Эй, Сайто, ты меня слушаешь? Руки у тебя давно замерли!'),
    78: ('A... S-Sorry.', 'А… П-Прости.'),
    79: ("Honestly, praise you a little and you get cocky right away. That's Saito for you.", 'Правда, похвалишь тебя чуть — и ты сразу зазнаёшься. Такой уже Сайто.'),
    80: ('……... …. ..', '……… … …'),
    81: ("Aah, that feels good. Saito, you're good at washing bodies.", 'Аах, это приятно. Сайто, ты хорошо моешь тела.'),
    82: ("Mm, even so... Haa... It doesn't get big, does it.", 'Мм, и всё же… Хаа… Оно не становится большим, правда.'),
    83: ('W-What is?', 'Ч-Что — что?'),
    84: ("A-Any... No, anything's fine. Your hands stopped!", 'А-Что угодно… Нет, всё равно. Руки замерли!'),
    85: ('Y-Yes!', 'Д-Да!'),
    86: ("Hey, Saito, you've been acting strange for a while now. Did you get heatstroke or something?", 'Эй, Сайто, ты давно ведёшь себя странно. Тебе не плохо от жара?'),
    87: ('N-No... Nothing like that...', 'Н-Нет… Ничего такого…'),
    88: ('If only more parts of you would get bigger... Saito, your hands stopped again?', 'Хоть бы другие части тела стали больше… Сайто, руки опять замерли?'),
    89: ("(I'm at my limit. Mommy. I tried my best.)", 'Я на пределе. Мамочка. Я старался.'),
    90: ('Bata...', 'Бата…'),
    91: ('Kyaa! Saito? What happened to you, you collapsed!', 'Кья! Сайто? Что с тобой, ты упал!'),
    92: ('Hey... Saito! Are you okay?', 'Эй… Сайто! Ты в порядке?'),
    93: ('Open your eyes! Saito, Saito, Saitooooooo!!!!', 'Открой глаза! Сайто, Сайто, САЙТОООООО!!!!!!'),
    94: ('Eh? What do you mean, becoming independent?', 'А? Что значит — стать самостоятельной?'),
    95: ("Yeah. I can't stay at this academy forever... It'd be wrong to keep relying on Louise and the others.", 'Да. Вечно оставаться в этой академии… Я и сама не знаю, правильно ли всё время полагаться на Луизу и остальных.'),
    96: ("If you say that, then I've been taken care of by this academy ever since Louise summoned me.", 'Если так, то меня опекает эта академия с тех пор, как Луиза меня призвала.'),
    97: ("Hiraga-kun is Louise's familiar. Of course you're taken care of. But I'm not one, so...", 'Хирага-кун — фамильяр Луизы. Тебе и положено. А я нет, поэтому…'),
    98: ("I know, but... We're probably the only two Japanese people in this world.", 'Я знаю, но… Мы, наверное, единственные японцы в этом мире.'),
    99: ("And we're not exactly strangers to each other... So if we worked at the academy, maybe...", 'И мы не совсем чужие друг другу… Так что если бы мы работали в академии, может…'),
    100: ("The thing is, Hiraga-kun... I've been scouted.", 'Дело в том, Хирага-кун… Меня завербовали.'),
    101: ('S-Scouted for what?', 'З-Завербовали — куда?'),
    102: ('A theater troupe, a theater troupe.', 'В театральную труппу, в труппу.'),
    103: ("A theater troupe? You mean Weatherly's troupe?", 'Труппу? Ты имеешь в виду труппу Уэзерби?'),
    104: ('No. Someone from another troupe who saw that play liked me and scouted me.', 'Нет. Кто-то из другой труппы, кто смотрел тот спектакль, меня и завербовал.'),
    105: ("Now's a good chance, so I was thinking of going along with that troupe.", 'Сейчас как раз удобный случай, и я думаю присоединиться к этой труппе.'),
    106: ("But if you join a troupe, you'll have to go on tours to other towns, won't you?", 'Но если ты в труппе, тебе придётся ездить с гастролями в другие города, да?'),
    107: ("Yeah. I probably won't get to see Hiraga-kun very often anymore.", 'Да. Наверное, мы с Хирага-куном будем видеться реже.'),
    108: ("But I'm looking forward to it. I get to see all sorts of towns in this world.", 'Но я с нетерпением жду этого. Я смогу объездить разные города этого мира.'),
    109: ("Maybe I'll even find a clue to get back to Japan.", 'Может, я даже найду ключ к тому, чтобы вернуться в Японию.'),
    110: ("I see. Yeah, that's right.", 'Понятно. Да, верно.'),
    111: ("So, Hiraga-kun... If you don't mind, cheer me on, okay?", 'Так что, Хирага-кун… Если не против, поддержи меня, ладно?'),
    112: ("Of course I will! And let's both do our best to find a way back to Japan!", 'Конечно! И давай вместе постараемся найти способ вернуться в Японию!'),
    113: ('Mm!', 'Мм!'),
    114: ("(With Weatherly's help, Haruna was completely back to her old self.)", 'При помощи Уэзерби Харуна полностью вернулась к прежней себе.'),
    115: ("(She hardly remembers being Akina at all. I wonder if that's Weatherly's magic too...)", 'Она почти не помнит, что была Акиной. Интересно, это тоже магия Уэзерби…'),
    116: ('(Weatherly was charged with siding with Reconquista, but...)', 'Уэзерби предъявили обвинение в сотрудничестве с Реконкистой, но…'),
    117: ("(For providing information on Reconquista, and through the princess's consideration, she seems to have avoided punishment with just a few months of house arrest.)", 'За информацию о Реконкисте и по милости принцессы она, кажется, отделалась лишь несколькими месяцами домашнего ареста.'),
    118: ('(And so, after Haruna left the academy, life at the academy resumed pretty much as before... But...)', 'И после того как Харуна ушла из академии, жизнь в академии пошла почти как раньше… Но…'),
    119: ('By the way, Louise.', 'Кстати, Луиза.'),
    120: ('What is it, Saito?', 'Что такое, Сайто?'),
    121: ('Why are you taking out chains and ropes, mistress?', 'Почему ты достаёшь цепи и верёвки, госпожа?'),
    122: ('Listen. You are my familiar.', 'Слушай. Ты мой фамильяр.'),
    123: ('Haa...', 'Хаа…'),
    124: ('As a familiar, the orders of the mistress who summoned you are absolute. So far, so good?', 'Как фамильяр, ты обязан беспрекословно выполнять приказы призвавшей тебя госпожи. Пока понятно?'),
    125: ('Well...', 'Ну…'),
    126: ('And yet you wander away from me during class, and ogle every girl you see.', 'И при этом ты отлыниваешь от меня на уроках и пялишься на каждую девушку.'),
    127: ('And on top of that, you flirt with Siesta and Kirche behind my back! You have far too little awareness as a familiar!', 'А напоследок ещё и флиртуешь с Сиэстой и Кирке у меня за спиной! У тебя куда меньше сознания фамильяра, чем надо!'),
    128: ("So, I've decided to re-educate you thoroughly.", 'Так что я решила перевоспитать тебя как следует.'),
    129: ('Gulp.', 'Глоток.'),
    130: ('First, the chains. And restraints. What else do I need...', 'Сначала цепи. И наручники. Что ещё понадобится…'),
    131: ("And let me tell you, I only accept 'yes', 'understood', or 'roger' as a reply.", 'И предупреждаю: в ответ я принимаю только «да», «понял» или «есть».'),
    132: ('A... No...', 'А… Нет…'),
    133: ('Guh, it hurts!', 'Гух, больно!'),
    134: ("I told you I only accept 'yes', 'understood', or 'roger'. The re-education has already begun!", 'Я же сказала, что принимаю только «да», «понял» или «есть». Перевоспитание уже началось!'),
    135: ('Sigh...', 'Эх…'),
    136: ('Say, Louise.', 'Слушай, Луиза.'),
    137: ('What is it?', 'Что ещё?'),
    138: ("I'm probably the worst familiar there is. I know that.", 'Я, наверное, худший фамильяр из всех. Я это знаю.'),
    139: ('Oh? So you understand.', 'О? Так ты понимаешь.'),
    140: ("But as a man, I've decided I'll absolutely protect Louise.", 'Но как мужчина я решил, что обязательно защищу Луизу.'),
    141: ('...!', '…!'),
    142: ("I'll wash your clothes, clean your room. I don't mind moderate food either. But could you spare me the ropes and chains?", 'Я буду стирать твою одежду, убирать комнату. С едой я тоже не против скромной. Но верёвки и цепи — мог бы ты их убрать?'),
    143: ('...', '…'),
    144: ('Saito...', 'Сайто…'),
    145: ('Hm?', 'Хм?'),
    146: ('You stupid dog!', 'Тупая собака!'),
    147: ('Guh!', 'Гух!'),
    148: ('Come on, stop dawdling! Change your clothes—help me quickly!', 'Ну же, не тяни! Переодевайся — помоги мне скорее!'),
    149: ("What? You just said I didn't need to help you change...", 'Что? Ты же говорила, что мне не нужно помогать тебе переодеваться…'),
    150: ('Shut up!', 'Замолчи!'),
    151: ("You're my familiar, so you do as I say. I've decided it, so that's how it is!!", 'Ты мой фамильяр, поэтому делаешь, что я говорю. Я решила — значит, так и будет!!'),
    152: ("That's right. You're always my familiar.", 'Верно. Ты всегда мой фамильяр.'),
    153: ("No matter what anyone else says, you're only mine...", 'Что бы ни говорили другие, ты только мой…'),
    154: ('Hm? Did you say something, Louise?', 'Хм? Ты что-то сказала, Луиза?'),
    155: ("I said nothing! Now that you've changed, let's go to class at once. Follow me!", 'Я ничего не сказала! Раз переоделся, идём немедленно в класс. Следуй за мной!'),
    156: ('Yes, yes, milady.', 'Да-да, миледи.'),
    157: ("It's 'yes' when addressing your mistress!", 'Госпоже говорят «да»!'),
    158: ('Yeees.', 'Д-дааа.'),
    159: ('(...And so, our daily life continued like this.)', 'И вот так наша с Луизой жизнь продолжалась.'),
    160: ("(Small incidents happen, but the hard fact that I'm Louise's familiar doesn't change at all.)", 'Случаются мелкие происшествия, но незыблемый факт, что я фамильяр Луизы, совершенно не меняется.'),
    161: ("(After all, today too I am Louise's familiar.)", 'В конце концов, сегодня я снова фамильяр Луизы.'),
}


def main():
    data = json.load(open('reports/ch20/parse_769_770.json', encoding='utf-8'))
    script = ['# Глава 20 (источник chapter_21): наказание, уход Харуны, повседневность.',
              '# Источник: ps2_source/chapters/chapter_21_小悪魔のおしおき.txt (SCENE 769-770).',
              '', 'label ch20:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = {'s': 0, 'si': 0, 'l': 0, 'ha': 0, 'th': 0}
    ja_d, ru_d = [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            scene = x['no']
            script += ['label ch20_scene_%d:' % scene, '']
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
            spk = {'サイト': 's', 'シエスタ': 'si', 'ルイズ': 'l', 'ハルナ': 'ha', 'null': 'th'}.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch20_%s_%03d' % (spk, counters[spk])
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
        if k == 'goto':
            script.append('    # → next scene %d' % x['target'])
            if x['target'] <= 770:
                script.append('    jump ch20_scene_%d' % x['target'])
            else:
                script.append('    jump attention')
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 20 ====', '    jump attention', '    return', '']
    files = {
        'game/chapters/20/script-ch20.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch20_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch20_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch20/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
