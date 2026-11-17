#!/usr/bin/env python3
"""Generate chapter 12 part 1 (scenes 510-524) from parsed source.

Writes EN script, JA/RU TL, voice-map fragment. Counterpart of
tools/gen_ch11_p34_script.py with chapter-12 id mapping.
"""
import json
import re

T = {
    0: ("W-What? Louise, did you cast a spell!?", "Ч-Что? Луиза, ты сотворила заклинание!?"),
    1: ("No! How rude! The explosion was outside!", "Нет! Как грубо! Взрыв был снаружи!"),
    2: ("Bang, bang, bang!!!", "Бах-бах-бах!!!"),
    3: ("C-Customers! It's war! The war has started!",
        "Г-Господа постояльцы! Война! Война началась!"),
    4: ("It's not just explosions—Reconquista soldiers are swarming through the streets!",
        "Мало вам взрывов — по городу расплодились солдаты Реконкисты!"),
    5: ("W-What!? Why would Reconquista soldiers be here!?",
        "Ч-Что!? При чём тут солдаты Реконкисты!?"),
    6: ("A-Anyway, staying at the inn won't help. Let's go to the castle!",
        "К-Короче, сидеть в гостинице бесполезно. Идём в замок!"),
    7: ("O-Okay! Let's head for the castle!", "Л-Ладно! Идём к замку!"),
    8: ("You answered a bit too slowly. You're worried about Haruna, aren't you?",
        "Ты ответил как-то вяло… Ты беспокоишься о Харуне, да?"),
    9: ("W-What are you talking about! That's... never mind.",
        "Ч-Что ты говоришь! Это… неважно."),
    10: ("Hmph, don't lie to me! You hesitated before answering.",
         "Хм, не лги мне! Ты поколебался, прежде чем ответить."),
    11: ("Lie to your mistress and you'll be punished!",
          "Солжёшь госпоже — и будешь наказан!"),
    12: ("S-Sorry about that...", "П-Прошу прощения…"),
    13: ("Fine. You may go save Haruna. I'll allow it, specially.",
         "Ладно. Глупый пёс, иди спасать Харуну. Особо разрешаю."),
    14: ("...", "…"),
    15: ("I understand. I owe you one.", "Понял. Я в долгу."),
    16: ("Don't act cool just because you're a stupid dog!",
         "Не строй из себя героя, глупый пёс!"),
    17: ("That's so selfish...", "Это так эгоистично…"),
    18: ("Come on, what are you dawdling for! Go already.",
         "Ну же, чего тянешь! Иди."),
    19: ("But Louise...", "Но Луиза…"),
    20: ("Hmph, don't underestimate me! I, the third daughter of the La Vallière family...",
         "Хм, не смей недооценивать меня! Я, третья дочь дома Ла Вальер…"),
    21: ("There's no way I'd fall behind on the battlefield!",
         "Не думаешь ли ты, что я отстану на поле боя!"),
    22: ("All right. Be careful!", "Ладно. Осторожно!"),
    23: ("Don't tell me what to do! You be careful!", "Не учи меня! Сам осторожнее!"),
    24: ("T-That's not something you can just tell me!",
         "Т-Так просто мне такого не говори!"),
    25: ("Then I command you. A mistress's order is absolute!",
         "Тогда приказываю. Приказ госпожи — закон!"),
    26: ("Sir, yes sir! This stupid dog of yours is off to rescue Haruna, sir!",
         "Так точно, сэр! Ваш глупый пёс отправляется спасать Харуну, сэр!"),
    27: ("Good. Now get going!", "Хорошо. Тогда иди же!"),
    28: ("(I guess the theater's the first place to look...)",
         "Начнём с театра, наверное…"),
    29: ("(Please be safe!)", "Только бы она была жива!"),
    30: ("Haa, haa haa...", "Хаа, хаа-хаа…"),
    31: ("(Damn, I was so close to the theater...)",
         "Чёрт, совсем рядом был…"),
    32: ("...", "…"),
    33: ("Damn, so these are the Reconquista soldiers the innkeeper was talking about!",
         "Чёрт, это и есть солдаты Реконкисты, о которых говорил хозяин!"),
    34: ("Get out of my wayyy!", "Убирайтесь с дороги-и!"),
    35: ("Cough, cough—shells falling near the palace!?",
         "Кхм, кхм — снаряды у самого дворца!?"),
    36: ("This is ridiculous! Why is the shelling reaching all the way here!? "
         "They couldn't possibly reach from outside the capital!",
         "Возмутительно! Как снаряды долетают сюда!? Извне столицы они бы не достали!"),
    37: ("Halt. This is the palace!", "Стой. Здесь дворец!"),
    38: ("It's an emergency. I need to see the Queen immediately...",
         "Это чрезвычайная ситуация. Немедленно доложите Её Величеству…"),
    39: ("A mere academy student demanding an audience! Follow the proper procedure.",
         "Ученица академии требует аудиенции! Соблюдайте положенный порядок."),
    40: ("W-What!? Can't you see what's happening!?",
         "Ч-Что!? Неужели вы не понимаете, что происходит!?"),
    41: ("Precisely because of the situation, we are on high alert!",
         "Именно поэтому мы и усилили охрану!"),
    42: ("Our duty is not to be flexible, but to enforce the rules.",
         "Наша задача — не делать исключений, а следить за порядком."),
    43: ("Wah!", "Ай!"),
    44: ("Eek!", "Ой!"),
    45: ("If being an academy student bothers you, I'll give you my name!",
         "Если вам не нравится, что я из академии, я представлюсь!"),
    46: ("Third daughter of Duke La Vallière, Louise Francoise.",
         "Третья дочь герцога Ла Вальер, Луиза Франсуаза."),
    47: ("I've come on urgent business concerning the Queen's order. ...Well? Happy now?",
         "Я явилась со срочным докладом по поводу приказа Её Величества. …Ну что, довольны?"),
    48: ("Of the La Vallière family... I-I apologize.",
         "Из дома Ла Вальер… П-Прошу прощения."),
    49: ("About the Queen's order, well, however...",
         "Что до приказа Её Величества, но…"),
    50: ("Announce me at once! You do realize this is an emergency! "
         "Can't you see the shelling and the fires in the city!?",
         "Доложите немедленно! Вы же понимаете, что это чрезвычайная ситуация! "
         "Не видите обстрел и пожары в городе!?"),
    51: ("P-Please wait a moment!", "П-Подождите немного!"),
    52: ("Reporting.", "Докладываю."),
    53: ("Third daughter of Duke La Vallière, Louise Francoise.",
         "Третья дочь герцога Ла Вальер, Луиза Франсуаза."),
    54: ("She requests an audience with Her Majesty.",
         "Она просит аудиенции у Её Величества."),
    55: ("Louise? So you came to Tristain. Show her in at once.",
         "Луиза? Значит, ты приехала в Тристанию. Проведите её немедленно."),
    56: ("Your Majesty, an outsider cannot...", "Ваше Величество, постороннего нельзя…"),
    57: ("It's all right.", "Всё в порядке."),
    58: ("These are the people I had investigating the bomb-thrower. "
         "They may have an important report.",
         "Это люди, которых я просила расследовать дело бомбиста. "
         "Возможно, у них важный доклад."),
    59: ("Besides, in this situation they're worth a million allies.",
         "К тому же сейчас они стоят миллиона союзников."),
    60: ("Your Majesty?", "Ваше Величество?"),
    61: ("Your Highness... Ah!", "Ваше Высочество… Ах!"),
    62: ("Third daughter of the La Vallière family, Louise Francoise, at your service.",
         "Третья дочь дома Ла Вальер, Луиза Франсуаза, явилась."),
    63: ("You came, Louise... Oh, where is your familiar?",
         "Ты пришла, Луиза… Ах, где же твой фамильяр?"),
    64: ("Ah, yes. Saito went into the city to save Haruna.",
         "А, да. Сайто ушёл в город спасать Харуну."),
    65: ("Haruna?", "Харуна?"),
    66: ("Yes.", "Да."),
    67: ("This is a formal war council. Please refrain from idle chatter.",
         "Здесь идёт официальный военный совет. Прошу воздержаться от праздных разговоров."),
    68: ("Oops. I'm sorry.", "Ой. Простите."),
    69: ("Understood. Then continue the report...", "Понятно. Продолжайте доклад…"),
    70: ("Yes, ma'am.", "Так точно."),
    71: ("At present, starting with the fire at the central market, buildings and bridges "
         "have been bombed all over the city...",
         "Сейчас, начиная с пожара на центральном рынке, по всему городу "
         "взорваны здания и мосты…"),
    72: ("Since then, continuous shelling of the palace has been confirmed from cannon "
         "sites hidden around the city.",
         "После этого зафиксирован продолжающийся обстрел дворца из орудий, "
         "которые, по всей видимости, скрыты в разных концах города."),
    73: ("Cannons inside the city? How could they...!",
         "Орудия в городе? Как это возможно!?"),
    74: ("We questioned a captured soldier. They used the recent bombings to...",
         "Мы допросили пленного солдата. Они использовали недавние взрывы, чтобы…"),
    75: ("Reconquista sent soldiers into the country disguised as repair workers.",
         "Реконкиста засылала солдат в страну под видом рабочих-ремонтников."),
    76: ("At the same time, they slipped in among the repair crews and installed "
         "many small cannons.",
         "Одновременно они проникли на места работ и установили множество малых орудий."),
    77: ("What!?", "Что!?"),
    78: ("Only those on the council may speak.", "Говорить имеют право только участники совета."),
    79: ("...", "…"),
    80: ("The records on the bombings and a map of the city.",
         "Материалы по взрывам и карту города."),
    81: ("Yes!", "Есть!"),
    82: ("...", "…"),
    83: ("T-This is...!", "Ч-Это что…!"),
    84: ("Yes. The bombings were set at the positions best suited to shelling the palace.",
         "Да. Взрывы были произведены в точках, лучше всего подходящих для обстрела дворца."),
    85: ("Remarkable. The bomb-thrower wasn't striking blindly—every incident was calculated.",
         "Искусно. Бомбист действовал не наугад — каждое событие было рассчитано."),
    86: ("Refrain from such remarks.", "Воздержитесь от таких слов."),
    87: ("Praising an enemy who uses such cowardly means is unbecoming.",
         "Восхвалять врага, прибегающего к таким подлым средствам, не подобает."),
    88: ("My apologies. Your Majesty.", "Прошу прощения. Ваше Величество."),
    89: ("We were careless. I had no idea things had gone this far.",
         "Мы оплошали. Я не знала, что дела зашли так далеко."),
    90: ("So the bomb-thrower's attacks were merely the enemy's first move, weren't they?",
         "Значит, дела бомбиста были лишь первым ходом врага, так?"),
    91: ("In the city, the infiltrated enemy soldiers have begun to move and large-scale "
         "street fighting is breaking out.",
         "В городе активировались проникшие вражеские солдаты — начинаются "
         "масштабные уличные бои."),
    92: ("...", "…"),
    93: ("Haa haa haa... It took longer than I thought.",
         "Хаа-хаа-хаа… Пришлось задержаться."),
    94: ("(There she is! Haruna!)", "Вот она! Харуна!"),
    95: ("I wanted to see you...", "Я так хотела тебя увидеть…"),
    96: ("...Eh!?", "…Э-э!?"),
    97: ("Ufufu...", "Уф-фу-фу…"),
    98: ("W-Wh-wh-wh-wh...", "Ч-Ч-ч-ч-ч…"),
    99: ("(The one touching my lips right now—could it be...)",
         "То, что сейчас касается моих губ… неужели…"),
    100: ("Hey, Saito...", "Слушай, Сайто…"),
    101: ("(...!)", "…!"),
    102: ("(...No! This isn't Haruna!)", "…Нет! Это не Харуна!"),
    103: ("Ufufu. Oh, Saito, what's wrong?", "Уф-фу. Ой, Сайто, что с тобой?"),
    104: ("You don't have to be shy, you know?", "Ты можешь не стесняться."),
    105: ("Who are you?", "Кто ты?"),
    106: ("My, you figured it out?", "Ого, догадался?"),
    107: ("Ufufu. You figured it out, didn't you?", "Уф-фу. Догадался, да?"),
    108: ("I wonder... am I really so different from Haruna?",
          "Интересно… я и вправду так не похожа на Харуну?"),
    109: ("...Huh?", "…А?"),
    110: ("I am Akina...", "Я — Акина…"),
    111: ("A new personality made for me by Weatherly-sama. Fufu, fufufufu...",
          "Новая личность, которую создала для меня Уэзерби-сама. Фу-фу, фуфуфуфу…"),
    112: ("And I'm the one you all called the 'bomb-thrower' and hunted everywhere!",
          "И я та самая, кого вы все называли «бомбистом» и искали повсюду!"),
    113: ("Ahahahahahahaha!", "А-ха-ха-ха-ха-ха!"),
    114: ("J-Joke... I can't laugh at this, Haruna.", "Ш-Шутишь? Мне не до смеха, Харуна."),
    115: ("A joke? Ahahaha... Are you an idiot?", "Шутка? А-ха-ха… Ты что, тупой?"),
    116: ("How about looking reality in the eye? Saito...",
          "Может, посмотришь правде в глаза? Сайто…"),
    117: ("T-Tell me you're lying, Haruna!", "С-Скажи, что это неправда, Харуна!"),
    118: ("If I said it was a lie, would this reality change? Then I'd say it a hundred times. "
          "I am Akina.",
          "Если я скажу, что это ложь, разве эта реальность изменится? "
          "Тогда я повторю хоть сто раз. Я — Акина."),
    119: ("I don't believe it. That the bomb-thrower was Haruna!",
          "Я не верю. Что бомбистом была Харуна!"),
    120: ("Then simply don't believe it.", "Тогда просто не верь."),
    121: ("The bomb-thrower is Akina; Haruna is a pure girl who knows nothing. Ugh, it makes me sick.",
          "Бомбист — это Акина, а Харуна — чистая девушка, которая ничего не знает. Фу, тошно."),
    122: ("Stop! Don't say it like that!", "Хватит! Не говори так!"),
    123: ("Shut up. I was made that way!", "Заткнись. Я была создана такой!"),
}

CHOICES = {
    510: [("...All right. I owe you one.", "…Ладно. Я в долгу."),
          ("But what about Louise!?", "А Луиза?!"),
          ("T-That's easy for you to say!", "Т-Так не говори!")],
    521: [("Cut the joke!", "Хватит шутить!"),
          ("Tell me you're lying, Haruna!", "Скажи, что это ложь, Харуна!"),
          ("I don't believe it!", "Я не верю!")],
}

SPK = {'サイト': 's', 'ルイズ': 'l', 'null': 'th', '宿の主人': 'innkeeper',
       '敵兵士ＥＳ': 'es', '味方Ａ': 'soldier', 'アンリエッタ': 'h',
       '将校': 'commander', 'ハルナ': 'ha', 'アキナ': 'ak'}
BGN = {2: 'white', 38: 'town', 58: 'town_square', 1145: 'overlay', 1172: 'overlay'}
START = {k: 0 for k in SPK.values()}


def bg(i):
    return BGN.get(i, 'id(%d)' % i)


def en_norm(s):
    """PROMTS.md п.5: EN-многоточие — символ '…'."""
    return re.sub(r'\.{3,}', '…', s)


def event(src, out):
    out.append('    # ' + src)
    m = re.search(r'\[BG +stage +image=\+(\d+)', src)
    if m:
        out.append('    $ fade_fx("%s")' % bg(int(m.group(1))))
        return
    m = re.search(r'\[EVENT_CG +event +image=\+(\d+)', src)
    if m:
        out.append('    $ dissolve_fx("id(%d)")' % int(m.group(1)))
        return
    m = re.search(r'\[BGM +bgm +play=\+(\d+)', src)
    if m:
        out.append('    play music t%d fadein 1.0' % (int(m.group(1)) - 1))
        return
    if '[BGM' in src and 'stop=' in src:
        out.append('    stop music fadeout 1.0')
        return
    if '[LAYER' in src and 'white' in src and 'hide' not in src:
        out.append('    $ flash_fx("white")')
        return
    if '[VIBRATE' in src:
        out.append('    $ shake_fx(duration=0.8)')
        return
    if '[COFFEE]' in src:
        out.append('    $ pause(1.0)')


def main():
    data = json.load(open('reports/ch12/parse_510_524.json', encoding='utf-8'))
    script = [
        '# Глава 12, часть 1 (сцены 510–524): «もう一人のハルナ» — война, дворец, Акина.',
        '# Источник: ps2_source/chapters/chapter_13_もう一人のハルナ.txt (SCENE 510-524).',
        '# Голоса: ch12_<spk>_<NNN>, сквозная нумерация части.',
        '',
        'label ch12:',
        '    $ tndl(None)',
        '    call overlay_screen("overlay", "Chapter Twelve: \'Another Haruna\'{#ch12_title}", '
        'isUseBlur=False, text_mode="black") from _call_overlay_screen_19',
        '    pause(2)',
        '    $ show_sprites()',
        '',
    ]
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            scene = x['no']
            script += ['label ch12_1_scene_%d:' % scene, '']
            continue
        if k == 'event':
            event(x['src'], script)
            continue
        if k == 'dlg':
            en, ru = T[x['idx']]
            en = en_norm(en)
            spk = SPK.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch12_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch12_1_c_%d_%d}' % (en_norm(en), scene, i + 1)
                tgt = ('ch12_1_scene_%d' % o['target']
                       if 510 <= o['target'] <= 524 else 'ch12_2')
                script.append('        "%s":' % ctext)
                script.append('            jump %s' % tgt)
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene == 518 and x['target'] == 520:
                script.append('    # checkKiss(): ветка 519/520. Флаг поцелуя не портирован — '
                              'идём по ветке без поцелуя (520).')
                continue
            tgt = ('ch12_1_scene_%d' % x['target']
                   if 510 <= x['target'] <= 524 else 'ch12_2')
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % tgt)
            script.append('')
            continue
        if k == 'date':
            script.append('    # 【デート】 — не портируется')
            continue

    script += ['    # ==== КОНЕЦ ЧАСТИ 1 ====', '    jump ch12_2', '    return', '']

    files = {
        'game/chapters/12/script-ch12_1.rpy': '\n'.join(script) + '\n',
        'game/chapters/12/script-ch12_2.rpy':
            '# Глава 12, часть 2 (сцены 525+): заглушка.\n\n'
            'label ch12_2:\n    jump attention\n    return\n',
        'game/tl/japanese/ch12_1_dialogs.rpy':
            '\n'.join(['# translate japanese strings:',
                       '# (ch12_1: scenes 510-524)', ''] + ja_d) + '\n',
        'game/tl/russian/ch12_1_dialogs.rpy':
            '\n'.join(['# translate russian strings:',
                       '# (ch12_1: scenes 510-524)', ''] + ru_d) + '\n',
        'game/tl/japanese/ch12_1_choises.rpy':
            '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch12_1_choises.rpy':
            '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
        'game/tl/japanese/ch12_1_overlays.rpy':
            '# ch12.1: overlay title\ntranslate japanese strings:\n\n'
            '    old "Chapter Twelve: \'Another Haruna\'{#ch12_title}"\n'
            '    new "第十二章「もう一人のハルナ」"\n',
        'game/tl/russian/ch12_1_overlays.rpy':
            '# ch12.1: overlay title\ntranslate russian strings:\n\n'
            '    old "Chapter Twelve: \'Another Haruna\'{#ch12_title}"\n'
            '    new "Глава двенадцатая. «Другая Харуна»"\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch12/voice_map_1.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), 'counters', counters)


if __name__ == '__main__':
    main()
