#!/usr/bin/env python3
"""Chapter 26 part 1 (scenes 934-943): Louise vs Tabitha over Haruna."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
    0: ('...', '…'),
    1: ('Saito-san... Please wake up!', 'Сайто-сан… Проснитесь!'),
    2: ('...Mm, nn?', '…Мм, нн?'),
    3: ('I said wake up, Saito-san!', 'Я сказала — проснитесь, Сайто-сан!'),
    4: ("...I can't eat any more.", '…Я больше не могу есть.'),
    5: ("Honestly, don't sleep-talk! It's serious!", 'Право, не говорите во сне! Это серьёзно!'),
    6: ("Mm? Siesta, what's the matter?", 'Мм? Сиэста, что случилось?'),
    7: ('Miss Valliere! Miss Valliere and Miss Tabitha are having a fight...!', 'Мисс Вальер! Мисс Вальер и мисс Табаса ссорятся…!'),
    8: ('Louise and Tabitha? Why?', 'Луиза и Табаса? Почему?'),
    9: ("Why? It's obvious! It's about Haruna-san!", 'Почему? Это же очевидно! Из-за Харуны-сан!'),
    10: ("Oh no, that's bad! I'll go check right away!", 'Ох, это плохо! Я сейчас пойду!'),
    11: ('Yes! Please do!', 'Да! Прошу вас!'),
    12: ("I can't believe Louise would... Wait, they'll find out we all peeked at the letter!", 'Не могу поверить, что Луиза… Погоди, они сейчас узнают, что мы все тайком читали письмо!'),
    13: ('...', '…'),
    14: ('...', '…'),
    15: ('Ah, darling!', 'Ах, дорогой!'),
    16: ("What's going on here? Weren't we all supposed to pretend we didn't know about the letter?", 'Что тут происходит? Мы же договорились притворяться, что не знаем о письме?'),
    17: ('Well, I mean...', 'Ну, я хочу сказать…'),
    18: ('Louise barged in and started telling Tabitha not to take Haruna to Gallia.', 'Луиза ворвалась и стала говорить Табасе, чтобы та не увозила Харуну в Галлию.'),
    19: ('Sigh... What is she doing...', 'Ох… Что она делает…'),
    20: ("(But for Louise to say something that sounds like she's protecting Haruna...)", 'Но чтобы Луиза сказала что-то вроде защиты Харуны…'),
    21: ("But Tabitha said she'd take her, didn't she? Well, for Tabitha it is a mission.", 'Но Табаса сказала, что увезёт, да? Ну, для Табасы это задание.'),
    22: ('And now Louise is shouting one-sidedly, while Tabitha just stays silent.', 'А сейчас Луиза кричит в одно сторону, а Табаса просто молчит.'),
    23: ('I-I see...', 'П-Понятно…'),
    24: ("I'll say it again! I will never hand Haruna over!", 'Повторяю! Я никогда не отдам Харуну!'),
    25: ('...', '…'),
    26: ("Honestly, I don't know what about this 'mission'—but selling a commoner... a friend, is shameful for a noble!", 'Право, я не знаю, что там за «задание» — но продать простолюдина… друга, — позор для дворянки!'),
    27: ('...', '…'),
    28: ("Don't just stand there—say something!", 'Не стой молча — скажи что-нибудь!'),
    29: ('...', '…'),
    30: ("Well, that's about it.", 'Ну, примерно так.'),
    31: ('This is bad...', 'Это плохо…'),
    32: ('Hey, Saito! You too—say something to this stubborn Tabitha!', 'Эй, Сайто! Ты тоже скажи что-нибудь этой упрямой Табасе!'),
    33: ('Eh, me!?', 'А, я!?'),
    34: ("Haruna is your classmate, isn't she!? If you don't put your foot down now, Tabitha will take her away!", 'Харуна же твоя одноклассница!? Если ты сейчас не вмешаешься, Табаса её увезёт!'),
    35: ('Take her away, you say...', 'Увезёт, говоришь…'),
    36: ('...', '…'),
    37: ('Do your best, darling.', 'Постарайся, дорогой.'),
    38: ('How am I supposed to do my best in this situation...', 'Как я должен здесь «постараться»…'),
    39: ("Tabitha. Since we're here, won't you give us an explanation everyone can accept?", 'Табаса. Раз мы уже здесь, не объяснишь ли ты так, чтобы все поняли?'),
    40: ('...', '…'),
    41: ("Just saying you were asked to bring Haruna isn't enough, is it?", 'Просто сказать, что тебя попросили доставить Харуну, недостаточно, да?'),
    42: ("Try to understand how worried we are about Haruna. And I'm worried about you, too, of course.", 'Попробуй понять, как мы волнуемся за Харуну. И, конечно, я волнуюсь и за тебя.'),
    43: ('...', '…'),
    44: ("Louise, calm down. There's a reason Tabitha's silent, isn't there?", 'Луиза, успокойся. У Табасы есть причина молчать, да?'),
    45: ('A reason? How would you know that?', 'Причина? Откуда тебе знать?'),
    46: ("Well, I can guess. It's probably a top-secret mission she can't tell anyone about.", 'Ну, могу предположить. Наверное, это сверхсекретное задание, о котором нельзя никому говорить.'),
    47: ("And that's supposed to satisfy you?", 'И это тебя должно устроить?'),
    48: ('Of course not. And Tabitha must be agonizing over the mission, too.', 'Конечно нет. И Табаса наверняка мучается из-за этого задания.'),
    49: ('Right, Tabitha?', 'Верно, Табаса?'),
    50: ('...', '…'),
    51: ("Please try to understand Louise's feelings, too.", 'Пожалуйста, пойми и чувства Луизы.'),
    52: ('The feelings Louise is expressing are the feelings of all of us...', 'То, что говорит Луиза, — чувства всех нас…'),
    53: ('...', '…'),
    54: ('Let me be clear—both of you are at fault!', 'Откровенно говоря — вы оба виноваты!'),
    55: ('Ehh!?', 'А!?'),
    56: ('...', '…'),
    57: ("Louise blames too much, and Tabitha doesn't say what she should. Both are at fault.", 'Луиза слишком обвиняет, а Табаса не говорит то, что должна. Обе виноваты.'),
    58: ('Hmph.', 'Хмф.'),
    59: ("But, Tabitha. Try to understand Louise's feelings, too.", 'Но, Табаса. Попробуй понять и чувства Луизы.'),
    60: ('The feelings Louise is expressing are the feelings of all of us...', 'То, что говорит Луиза, — чувства всех нас…'),
    61: ('...', '…'),
    62: ('Say, Tabitha. About Haruna being taken to Gallia—is there really no way around it?', 'Слушай, Табаса. Про доставку Харуны в Галлию — неужели нельзя ничего придумать?'),
    63: ("No. It's a mission.", 'Нет. Это задание.'),
    64: ('I see... This is bad...', 'Понятно… Это плохо…'),
    65: ('Hmm, what should we do...', 'Хм, что же нам делать…'),
    66: ('Saito-san!', 'Сайто-сан!'),
    67: ("Siesta, what's wrong?", 'Сиэста, что случилось?'),
    68: ("I-It's terrible! Haruna-san has disappeared!", 'Это, это ужасно! Харуна-сан исчезла!'),
    69: ('Eh, seriously?', 'А, правда?'),
    70: ('Yes, really.', 'Да, правда.'),
    71: ('...!?', '…!?'),
    72: ('Wh-Why!?', 'П-Почему!?'),
    73: ("Hey, that's not good!", 'Эй, это же ужасно!'),
    74: ('I took my eyes off Haruna-san for a moment...', 'Я на минуту упустила Харуну-сан из виду…'),
    75: ("I'll go look for her!", 'Я пойду её искать!'),
    76: ('We should search for Haruna, too.', 'Нам тоже стоит поискать Харуну.'),
    77: ("Right. Standing here arguing won't help.", 'Верно. Стоять здесь и спорить бесполезно.'),
    78: ('Well then...', 'Ну что ж…'),
    79: ('...!?', '…!?'),
    80: ("What's wrong?", 'Что случилось?'),
    81: ('S-Saito-san!?', 'С-Сайто-сан!?'),
    82: ('What!? Is it the bomber at a time like this!?', 'Что!? Это бомбист в такой момент!?'),
    83: ("What!? Again!? This time it's close.", 'Что!? Опять!? На этот раз рядом.'),
    84: ('Saito-san...', 'Сайто-сан…'),
    85: ("What's happening!?", 'Что происходит!?'),
    86: ('Hey, you! This place could be caught in fighting any moment!', 'Эй, вы! Этот дом может в любой момент оказаться в бою!'),
    87: ('Hurry—get out of the inn!', 'Быстрее — уходите из гостиницы!'),
    88: ("Hey, what's going on!?", 'Эй, что происходит!?'),
    89: ("We don't know who the enemy is, but we're under attack! Run before you're hurt!", 'Мы не знаем, кто враг, но нас атакуют! Бегите, пока не пострадали!'),
    90: ("I'm worried about Haruna, but first let's go to the castle and get information about the bomber!", 'Я волнуюсь за Харуну, но сначала пойдём в замок и узнаем о бомбисте!'),
    91: ('Right. Tabitha, is that all right with you?', 'Верно. Табаса, ты согласна?'),
    92: ('Mm.', 'Мм.'),
    93: ("All right, it's decided. Siesta, you're coming with us, too!", 'Ладно, решено. Сиэста, ты тоже идёшь с нами!'),
    94: ('Y-Yes!', 'Д-Да!'),
    95: ("What is this... It's just like a war...", 'Что это… словно война…'),
    96: ("Siesta. Don't leave our side.", 'Сиэста. Не отходи от нас.'),
    97: ('Yes, Miss Valliere!', 'Да, мисс Вальер!'),
    98: ('Stop.', 'Стой.'),
    99: ('Why suddenly?', 'Почему вдруг?'),
    100: ('Could it... no way...', 'Неужто… не может быть…'),
    101: ('Mm.', 'Мм.'),
    102: ("We're in a hurry! Let's go, Derf!", 'Мы спешим! Пойдём, Дерф!'),
    103: ('Oh, my turn, partner!', 'Ох, моя очередь, приятель!'),
    104: ("Yeah—let's smash them with everything we've got!", 'Да — разнесём их изо всех сил!'),
    105: ("Understood, partner. I thought I'd end up unable to speak at this rate.", 'Понял, приятель. Я уже думал, что так и останусь немым.'),
    106: ('Phew—we finally made it to the castle.', 'Фух — мы наконец добрались до замка.'),
    107: ("Good. It looks like the enemy hasn't reached the castle yet.", 'Хорошо. Похоже, враг ещё не дошёл до замка.'),
    108: ('I thought the bomber worked alone, but it seems I was wrong.', 'Я думала, бомбист действует в одиночку, но, кажется, ошиблась.'),
    109: ('Who they are—what organization—I have no idea at all.', 'Кто они и какая организация — не имею ни малейшего понятия.'),
    110: ("Who cares? Catch them and we'll know everything.", 'Да какая разница? Поймаем — и всё узнаем.'),
    111: ('Well, if only it were that easy...', 'Ну, если бы всё было так просто…'),
    112: ('...', '…'),
    113: ('Well then, into the castle...', 'Ну что ж, в замок…'),
    114: ('Hey, you there! You may not enter the castle without permission!', 'Эй, вы там! Без разрешения входить в замок нельзя!'),
    115: ("We've come to the castle on legitimate business.", 'Мы пришли в замок по законному делу.'),
    116: ('No. I cannot permit entry.', 'Нет. Я не могу разрешить вход.'),
    117: ("I'm under orders to let nobody in without permission.", 'Мне приказано никого не пускать без разрешения.'),
    118: ("You can't permit us—we're... Oh, there's no time to dawdle here!", 'Вы не можете нас пустить — мы… Ох, здесь некогда тянуть время!'),
    119: ("All right, here's what we'll do...", 'Ладно, сделаем вот что…'),
    120: ('Louise—can I take care of these guys?', 'Луиза — можно я разберусь с этими?'),
    121: ("Of course not! What are you saying! Honestly, you're an idiot!", 'Конечно нет! Что ты несёшь! Право, ты идиот!'),
    122: ('W-Well, I thought so...', 'Н-Ну, я так и думал…'),
    123: ('Saito, be quiet. Leave this to me.', 'Сайто, помалкивай. Предоставь это мне.'),
    124: ('Yes, yes.', 'Да-да.'),
    125: ("Louise, I'll leave it to you.", 'Луиза, предоставляю тебе.'),
    126: ('Wh-What? I thought you were going to do something!', 'Ч-Что? Я думала, ты что-то сделаешь!'),
    127: ("Well, I mean—I don't know what to do!", 'Ну, я… не знаю, что делать!'),
    128: ("Honestly, you're utterly useless!", 'Право, ты совершенный бесполезный!'),
    129: ('Yes, yes.', 'Да-да.'),
    130: ('Heh heh, come now, soldier—have something warm to eat with this.', 'Хи-хи, ну же, солдат — съешь что-нибудь горячее с этим.'),
    131: ("Saito! What are you doing!? You can't win them over like that!", 'Сайто! Что ты делаешь!? Так ты их не уговоришь!'),
    132: ('Eh, but...', 'А, но…'),
    133: ("You there. What's your purpose? Depending on your answer, I'll arrest you.", 'Вы там. Какова ваша цель? Смотря что вы скажете, я вас арестую.'),
    134: ("Oh, for heaven's sake—you've only made things more complicated! Saito, be quiet!", 'Ох, ради всего святого — ты только всё усложнил! Сайто, помалкивай!'),
    135: ('Yes, yes.', 'Да-да.'),
}
CHOICES = {
934: [("Ask Tabitha to explain", "Попросить Табасу объяснить"),
      ("Calm Louise down", "Успокоить Луизу"),
      ("Settle both down", "Примирить обеих")],
940: [("Use force!", "Применить силу!"),
      ("Leave it to Louise", "Поручить Луизе"),
      ("...That's a bribe, isn't it", "...Это же взятка, да?")],
}
SPK = {'サイト': 's', 'シエスタ': 'si', 'ルイズ': 'l', 'タバサ': 't',
       'キュルケ': 'k', '味方Ａ': 'soldier', 'null': 'th'}
START = {'s': 0, 'si': 0, 'l': 0, 't': 0, 'k': 0, 'soldier': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch26/parse_934_971.json', encoding='utf-8'))
    script = ['# Глава 26, часть 1 (сцены 934–943): спор из-за Харуны, поездка в Галлию.',
              '# Источник: ps2_source/chapters/chapter_27_タバサの秘密.txt (SCENE 934-943).',
              '', 'label ch26:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 943: break
            scene = x['no']
            script += ['label ch26_1_scene_%d:' % scene, '']
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
            tag = 'ch26_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch26_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch26_1_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 934 <= scene <= 943: continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch26_1_scene_%d' % x['target'] if 934 <= x['target'] <= 943 else 'ch26_2'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch26_2', '    return', '']
    files = {
        'game/chapters/26/script-ch26.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch26_1_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch26_1_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch26_1_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch26_1_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch26/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
