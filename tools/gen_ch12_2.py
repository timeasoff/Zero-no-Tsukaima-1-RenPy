#!/usr/bin/env python3
"""Chapter 12 part 2 (scenes 525-534). Uses event mapping from gen_ch12_1."""
import json
import sys

sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
    0: ("Like some happy fairy tale, clicking your heels three times won't take you back to your world.",
        "Как в счастливой сказке — щёлкни каблуками три раза, и ты не сможешь вернуться в прежний мир."),
    1: ("No one will ever really save us. That's our reality!",
        "Никто по-настоящему не спасёт нас. Вот наша реальность!"),
    2: ("Damn it, what's going to happen to Haruna!?", "Чёрт, что будет с Харуной!?"),
    3: ("Who cares? She'll just disappear, that's all.", "А какая разница? Она просто исчезнет — и всё."),
    4: ("W-What did you say!?", "Ч-Что ты сказала!?"),
    5: ("Eek! W-Why are you pointing a sword at me, Hiraga-kun!?",
        "Ой! Ч-Почему ты направляешь на меня меч, Хирага-кун!?"),
    6: ("Haruna...", "Харуна…"),
    7: ("Ahahaha... idiot!", "А-ха-ха… дурак!"),
    8: ("T-That's dirty!", "Это подло!"),
    9: ("Hey, partner. That girl's movements are no joke—watch out.",
        "Эй, приятель. Движения этой девчонки не шутка — остерегайся."),
    10: ("Don't tell me that!", "Не говори мне такого!"),
    11: ("Don't look at me like that...", "Не смотри на меня так…"),
    12: ("Just kidding, ahaha...", "Пошутила, а-ха-ха…"),
    13: ("...! What's this presence!?", "…! Что за присутствие!?"),
    14: ("Eeeeeek!", "А-а-а-а!"),
    15: ("W-What the hell!?", "Ч-Что за чёрт!?"),
    16: ("Rushing out to meet Saito without a thought for your own danger, and you two are...?",
         "Бросилась встречать Сайто, забыв об опасности, а вы двое…"),
    17: ("W-What are you two playing at!?", "Ч-Что вы двое тут вытворяете!?"),
    18: ("L-Louise!", "Л-Луиза!"),
    19: ("Wait, Louise! You've got it wrong!", "Подожди, Луиза! Ты не так поняла!"),
    20: ("Ow ow ow... What's your problem, Louise! Trying to kill me!?",
         "Ай-ай-ай… Ты что, Луиза! Хочешь убить меня!?"),
    21: ("...? Haruna? What's with that way of speaking?", "…? Харуна? Что за манера говорить?"),
    22: ("So your goody-two-shoes act was a lie, and this is the real you?",
         "Так твоё прилежание было только маской, а это настоящая ты?"),
    23: ("Shut up, shut up!", "Заткнись, заткнись!"),
    24: ("Don't call me Haruna! I'm Akina!", "Не смей называть меня Харуной! Я — Акина!"),
    25: ("What's going on here?", "Что это значит?"),
    26: ("Looks like Weatherly's controlling her. She says she's the bomb-thrower.",
         "Похоже, Уэзерби её подчинила. Она говорит, что она и есть бомбист."),
    27: ("What!? So Weatherly's the mastermind!?", "Что!? Тогда Уэзерби — закулисный организатор!?"),
    28: ("T-Then what was that play all about? Hmph, making fools of us.",
         "Т-Так что же это была за пьеса? Хм, нас выставили за дураков."),
    29: ("Don't say Weatherly-sama's name without honorifics. And don't ignore me!",
         "Не смей называть Уэзерби-саму без уважения. И не игнорируй меня!"),
    30: ("Whoa!", "Ого!"),
    31: ("You said Akina, right? What do you want?", "Ты сказала — Акина, верно? Какова твоя цель?"),
    32: ("I told you, didn't I? Sabotage in Tristain. As the bomb-thrower.",
         "Я же сказала — диверсии в Тристании. В роли бомбиста."),
    33: ("I was supposed to infiltrate the academy to gather information about its secrets, though...",
         "Я должна была проникнуть в академию, чтобы собрать сведения о её секретах, но…"),
    34: ("The academy's secrets?", "Секреты академии?"),
    35: ("You, Louise. The power of Void you carry.", "Ты, Луиза. Сила Пустоты, что в тебе."),
    36: ("W-What!?", "Ч-Что!?"),
    37: ("Meeting Saito made Haruna's consciousness stronger and threw off my plans, but...",
         "Встреча с Сайто усилила сознание Харуны и спутала мои планы, но…"),
    38: ("This power belongs to the Princess... to the Queen.",
         "Эта сила принадлежит принцессе… Её Величеству."),
    39: ("For lowly wretches like you to touch it so casually—outrageous!",
         "Чтоб такие жалкие твари, как вы, так запросто к ней прикасались — возмутительно!"),
    40: ("Hmph, how interesting. However polite you act, in the end it's power that decides.",
         "Хм, забавно. Как бы ты ни важничала, в конце концов решает сила."),
    41: ("Now, come out!", "А ну, выходи!"),
    42: ("...!", "…!"),
    43: ("D-Damn it!", "Ч-Чёрт!"),
    44: ("H-How dare you...!", "Как ты смеешь…!"),
    45: ("Fufufu, now do you understand?", "Фу-фу-фу, теперь поняла?"),
    46: ("H-Help me, Hiraga-kun.", "П-Помоги мне, Хирага-кун."),
    47: ("Another trick to make me think she's Haruna, is it?",
         "Опять хочешь заставить меня поверить, что она Харуна?"),
    48: ("Stop it, don't come out! I am me!", "Прекрати, не выходи! Я — это я!"),
    49: ("H-Hiraga-kun...", "Х-Хирага-кун…"),
    50: ("Damn it! Stop it, Haruna!", "Чёрт! Прекрати, Харуна!"),
    51: ("H-Hey. Could it really be Haruna...?", "Э-Эй. Неужели это и правда Харуна…?"),
    52: ("Shut up. I am Akina!", "Заткнись. Я — Акина!"),
    53: ("Eek! W-Wait!", "Ой! П-Подождите!"),
    54: ("No! Haruna!", "Нет! Харуна!"),
    55: (None, None),
    56: ("Damn, I let Akina get away. What a blunder.", "Чёрт, я упустил Акину. Вот оплошность."),
    57: ("What was that? Haruna and Akina...?", "Что это было? Харуна и Акина…?"),
    58: ("Hypnosis. They've implanted a false second personality into her to control and manipulate her.",
         "Гипноз. Ей внедрили ложную вторую личность, чтобы подчинить и направлять её."),
    59: ("And one more thing. The girl's physical abilities are boosted by another suggestion or spell.",
         "И ещё кое-что. Физические возможности девчонки усилены другим внушением или заклинанием."),
    60: ("Unbelievable... Haruna...", "Невероятно… Харуна…"),
    61: ("Right! How's the battle going!?", "Да! Как дела на поле боя!?"),
    62: ("Still going. It's actually getting more intense, if anything.",
         "Ещё идёт. Скорее, становится только ожесточённее."),
    63: ("Apparently Reconquista used the repair work after the bombings to slip in soldiers and plant cannons...",
         "Похоже, Реконкиста использовала восстановительные работы после взрывов, "
         "чтобы проникнуть солдатами и установить орудия…"),
    64: ("—and prepare this attack on Tristain.", "—и подготовить это нападение на Тристанию."),
    65: ("They mean to use the confusion to strike Tristain with the remaining aerial fleet, I'd wager.",
         "Они хотят в этой сумятице ударить по Тристании оставшимся воздушным флотом."),
    66: ("I hear the fleet has already been spotted heading this way.",
         "Говорят, флот уже замечен — он идёт сюда."),
    67: ("Then we have to get to the reinforcements fast!", "Тогда надо быстрее к подкреплению!"),
    68: ("...Yes. About that.", "…Да. Насчёт этого."),
    69: ("I got permission from the Princess to use Void magic here in Tristain.",
         "Я получила у принцессы разрешение применить здесь, в Тристании, магию Пустоты."),
    70: ("I'll drive the fleet back with Void.", "Я отгоню флот силой Пустоты."),
    71: ("T-That's fine, but if you use that magic here, the whole capital will be blown away!",
         "Э-Это хорошо, но если ты применишь здесь ту магию, всю столицу снесёт!"),
    72: ("It's all right. I won't use Explosion.", "Всё хорошо. Я не буду применять «Взрыв»."),
    73: ("What do you mean!?", "Что ты имеешь в виду!?"),
    74: ("The Void lineage isn't only Explosion.", "Род Пустоты — не только «Взрыв»."),
    75: ("(True enough. Now that Void is barely known, we can catch the enemy off guard...)",
         "И правда. Сейчас, когда о Пустоте почти никто не знает, мы, небось, сможем застать врага врасплох…"),
    76: ("All right, Louise... I mean, mistress, it's in your hands!",
         "Ладно, Луиза… то есть, госпожа, я полагаюсь на тебя!"),
    77: ("Good. That's my familiar.", "Хорошо. Вот теперь ты мой фамильяр."),
    78: ("(But... it is Louise, isn't it...?)", "Но… это же Луиза, правда…?"),
    79: ("What's that worried look for! You're still my familiar, aren't you!? "
         "Perhaps you need a punishment right now…",
         "Что за обеспокоенный вид! Ты всё равно мой фамильяр! "
         "Может, тебе прямо сейчас нужно наказание…"),
    80: ("U-Understood, mistress!", "П-Понял, госпожа!"),
    81: ("Good!", "Хорошо!"),
    82: ("All right! Come what may!", "Ладно! Будь что будет!"),
    83: ("Somehow, you don't look convinced, but I think you understood.",
         "Какого-то ты не выглядишь убеждённым, но, кажется, понял."),
    84: ("So where are you casting the spell? I didn't bring the Zero Fighter.",
         "Так где ты наложишь заклинание? Я не принёс «Зеро-файтер»."),
    85: ("I've decided.", "Я уже решила."),
    86: ("The very top of the palace!", "Самая вершина дворца!"),
    87: ("Haa haa haa haa haa...", "Хаа-хаа-хаа-хаа-хаа…"),
    88: ("Damn, damn... that Haruna is getting in my way!", "Чёрт, чёрт… эта Харуна всё мешает!"),
    89: ("(What good will this do? Stop this foolishness...)", "К чему всё это? Прекрати эту глупость…"),
    90: ("Shut up, shut up!", "Заткнись, заткнись!"),
    91: ("I'll beat them and take Saito for myself!", "Я их одолею и заберу Сайто себе!"),
    92: ("(It's no use. Even if you do, Hiraga-kun won't change...)",
         "Бесполезно. Даже если так, чувства Хирага-куна не изменятся…"),
    93: ("Then I'll just have Weatherly-sama tinker with your head.",
         "Тогда попрошу Уэзерби-саму поработать с твоей головой."),
    94: ("And I'll have a Saito who only looks at us.", "И получится Сайто, который смотрит только на нас."),
    95: ("All right. I suppose I can let you show your face once in a while.",
         "Ладно. Я позволю тебе иногда показываться."),
    96: ("(What good would that do...)", "И что это даст…"),
    97: ("Or would you rather watch another woman beside Saito forever?",
         "Или ты предпочтёшь вечно видеть другую женщину рядом с Сайто?"),
    98: ("Someone who isn't me... is there, you know.", "Там есть кто-то, кто не я… понимаешь?"),
    99: ("(I-It can't be helped. If that's fate...)", "Н-Ничего не поделаешь. Если такова судьба…"),
    100: ("Hypocrite! Liar! Shut up, shut up!", "Лицемерка! Лгунья! Заткнись, заткнись!"),
    101: ("I won't have it—no other woman. If it were me... I could have Saito.",
          "Я не потерплю другой женщины. Если бы это была я… я бы заполучила Сайто."),
    102: ("He'd hold me in his arms. Only me. Only me.",
          "Он держал бы меня в объятиях. Только меня. Только меня."),
    103: ("Lend me your power, Haruna.", "Дай мне свою силу, Харуна."),
    104: ("Let's beat that Louise and make Saito ours alone.",
          "Победим эту Луизу и сделаем Сайто только нашим."),
    105: ("(Stop, stop, stop!)", "Хватит, хватит, хватит!"),
    106: ("(No! I don't want this! I don't want it at all!)", "Нет! Я этого не хочу! Совсем не хочу!"),
    107: ("Well said. I'm another you. I couldn't lie to myself.",
          "Ну, сказала! Я — ещё одна ты. Не смогу я себя обмануть."),
    108: ("(No, no... it isn't like that!)", "Нет, нет… это не так!"),
    109: ("For this spell, we need the spot with the best view in the whole castle!",
          "Для этого заклинания нам нужно место с лучшим обзором во всём замке!"),
    110: ("And, as last time, Void magic takes time to chant.",
          "И, как в прошлый раз, заклинание Пустоты требует времени для произнесения."),
    111: ("Secure both. Understood?", "Обеспечь и то, и другое. Понял?"),
    112: ("I got it! Leave it to me!", "Понял! Положись на меня!"),
    113: ("(Still, the castle grounds have turned into a battlefield too. This is rough...)",
          "Но даже внутри замка теперь поле боя. Непросто…"),
    114: ("So this is the rooftop, huh.", "Так, это крыша, значит."),
    115: ("Careful, partner!", "Осторожно, приятель!"),
    116: ("...You all right!? Saito!", "…Ты в порядке!? Сайто!"),
    117: ("I-I'm fine, somehow!", "Я-Я, вроде, нормально!"),
    118: ("(No mercy at all, huh!)", "Никакой пощады, однако!"),
    119: ("...", "…"),
    120: ("My, what a coincidence... Or should I say, the cast has assembled?",
          "Ой, какое совпадение… Или сказать — собрался весь актёрский состав?"),
    121: ("I don't know what you plan to do here... but meeting me was your misfortune.",
          "Не знаю, что вы тут задумали… но встреча со мной — ваша беда."),
    122: ("Haruna!", "Харуна!"),
    123: ("I told you not to call me that!", "Я же сказала — не называй меня так!"),
    124: ("Shut up. Haruna is Haruna!", "Заткнись. Харуна — это Харуна!"),
    125: ("I'll think of something, just wait for me! Haruna!",
          "Я обязательно что-нибудь придумаю, только подожди меня! Харуна!"),
}
CHOICES = {
    527: [("Believe Louise.", "Поверить Луизе."),
          ("It's Louise, isn't it?", "Это же Луиза, так?"),
          ("Come what may!", "Будь что будет!")],
    533: [("Haruna!", "Харуна!"), ("Akina!", "Акина!"), ("Weatherly!", "Уэзерби!")],
}
SPK = {'アキナ': 'ak', 'サイト': 's', 'ハルナ': 'ha', 'デルフリンガー': 'd',
       'ルイズ': 'l', '魔導士': 'mage', 'null': 'th', 'ウェザリー': 'w'}
# Сквозная нумерация главы: продолжить после части 1.
START = {'ak': 10, 's': 30, 'ha': 8, 'l': 32, 'd': 0, 'mage': 0, 'th': 1, 'w': 0}


def main():
    data = json.load(open('reports/ch12/parse_525_544.json', encoding='utf-8'))
    script = ['# Глава 12, часть 2 (сцены 525–534): Акина против Харуны, Пустота, крыша.',
              '# Источник: ps2_source/chapters/chapter_13_もう一人のハルナ.txt (SCENE 525-534).',
              '', 'label ch12_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 534:
                break
            scene = x['no']
            script += ['label ch12_2_scene_%d:' % scene, '']
            continue
        if k == 'event':
            event(x['src'], script)
            continue
        if k == 'dlg':
            en, ru = T[x['idx']]
            if en is None:
                script.append('    # ' + x['src'] + '  (no voice — пропущено по образцу ch11_2)')
                continue
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
                ctext = '%s{#ch12_2_c_%d_%d}' % (en_norm(en), scene, i + 1)
                tgt = ('ch12_2_scene_%d' % o['target']
                       if 525 <= o['target'] <= 534 else 'ch12_3')
                script.append('        "%s":' % ctext)
                script.append('            jump %s' % tgt)
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if 510 <= x['target'] <= 534:
                tgt = 'ch12_2_scene_%d' % x['target']
            else:
                tgt = 'ch12_3'
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % tgt)
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 2 ====', '    jump ch12_3', '    return', '']
    files = {
        'game/chapters/12/script-ch12_2.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch12_2_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch12_2_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch12_2_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch12_2_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch12/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
