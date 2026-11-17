#!/usr/bin/env python3
"""Chapter 12 part 4 (scenes 544-548): finale, Louise keeps her familiar."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
0: ("(Once the enemy loses morale and discipline, their units crumble surprisingly easily...)",
    "Потерявшие боевой дух и порядок вражеские части рассыпаются удивительно легко…"),
1: ("(The units that tried to escape were suppressed one after another and surrendered.)",
    "Пытавшиеся прорваться отряды подавляли один за другим, и они сдавались."),
2: ("(Thus the conspiracy played out in Tristain lowered its curtain at last, leaving deep scars...)",
    "Так интрига, разыгравшаяся в Тристании, наконец опустила занавес, оставив глубокие шрамы…"),
3: ("(And we regained a temporary peace...)", "А мы на время вернули себе мирную жизнь…"),
4: ("(The hypnosis on Haruna would take long to undo, so for now the two personalities go on living side by side...)",
    "Снять гипноз с Харуны обещали не скоро, и пока что две личности живут вместе…"),
5: (None, None),
6: ("Me? At the palace?", "Меня — во дворец?"),
7: ("Yes, that's right.", "Да, всё верно."),
8: ("More precisely, we need the Akina inside you.", "Точнее — нам нужна Акина, что внутри тебя."),
9: ("What do you want with me?", "И что ты хочешь от меня?"),
10: ("Whoa, Akina! Don't just pop out like that.", "Ого, Акина! Не появляйся так внезапно."),
11: ("You know the situation in this country, don't you?", "Вы знаете, каково положение в этой стране, не так ли?"),
12: ("So I'd like to ask for your help. Even if that power wasn't something you sought.",
     "Поэтому я хочу просить о вашей помощи. Пусть даже эта сила досталась вам не по желанию."),
13: ("B-But, Your Highness...", "Н-Но, Ваше Высочество…"),
14: ("This Akina is... well, she was Weatherly's tool. Is that really all right with you?",
     "Эта Акина… ну, она была орудием Уэзерби. Вас это действительно устраивает?"),
15: ("Miss Weatherly, you say. She was never found after that, I hear. Whether she's alive or dead is unknown.",
     "Мисс Уэзерби, говорите? После того её так и не нашли, кажется. Жива она или мертва — неизвестно."),
16: ("Weatherly-sama...", "Уэзерби-сама…"),
17: ("She told me that she, a noblewoman, had suddenly been stripped of her rank by the Kingdom of Tristain.",
     "Она говорила, что её, дворянку, внезапно лишили титула Тристанинское королевство."),
18: ("Weatherly-sama, whose extraordinary magical talent was recognized by Reconquista...",
     "Уэзерби-саму, чь выдающийся талант к магии заметила Реконкиста…"),
19: ("...promised that in return for this operation's success, her noble rank would be restored.",
     "…пообещала, что в награду за успех операции ей вернут дворянский титул."),
20: ("Miss Weatherly didn't understand. That spell of hers, the one that beguiles the hearts of others, "
     "is forbidden in this country...",
     "Мисс Уэзерби не знала. Её заклинание, что смущает сердца других, в этой стране запрещено…"),
21: ("...and that very taboo was why her rank was taken from her.",
     "…и именно за это её и лишили титула."),
22: ("...", "…"),
23: ("Understood, Your Majesty. If I'll do, I'll take the job.",
     "Поняла, Ваше Величество. Если я подойду — согласна."),
24: ("I thought that maybe I could restore at least a little of Weatherly-sama's honor.",
     "Я подумала, что, может, смогу вернуть хоть немного чести Уэзерби-самы."),
25: ("...Is that so.", "…Вот как."),
26: ("Oh, but if you're to work at the castle, you'll have to fix that way of speaking of yours.",
     "О, но если вы будете служить в замке, придётся исправить вашу манеру говорить."),
27: ("Ahahaha... As for manners, I suppose I can leave that to Haruna.",
     "А-ха-ха… С этикетом, думаю, справится Харуна."),
28: ("I see.", "Понятно."),
29: ("(Hm, wait a second. Haruna was...)", "Хм, подожди-ка. Харуна же…"),
30: ("(She's fine with manners, but she can't do housework at all, can she...)",
     "С этикетом всё хорошо, но домашним хозяйством она совсем не умеет заниматься…"),
31: ("But Haruna couldn't do any housework at all, could she?", "Но Харуна же совсем не умела работать по дому, правда?"),
32: ("Ah, now that you mention it.", "А, точно."),
33: ("There's no need to worry. She can always study at the palace.", "Не стоит беспокоиться. Она может учиться во дворце."),
34: ("I'll tell the maids to overlook a few small inconveniences...",
     "Я скажу горничным не обращать внимания на мелкие неудобства…"),
35: ("(I hope it's all right... I just hope the Princess won't regret this...)",
     "Надеюсь, всё хорошо… Только бы принцесса не пожалела об этом…"),
36: ("(Ah, let it be... Overthinking it means I lose, right?)",
     "Да ладно… Слишком много думать — значит проиграть, да?"),
37: ("(Still, even with hypnosis, how did Haruna suddenly become a first-class terrorist?)",
     "И всё же, даже под гипнозом — как Харуна вдруг стала первоклассной террористкой?"),
38: ("(Maybe, for all I know, she was into guns and weapons or something?)",
     "Может, она, глядишь, увлекалась оружием или ещё чем?"),
39: ("Saito, that face means you're thinking something rude.",
     "Сайто, у тебя лицо такое, будто ты думаешь о чём-то грубом."),
40: ("(Ugh, how did she know? Akina's too sharp.)", "Ой, откуда она знает? Акина слишком проницательна."),
41: ("(I don't know anything... even though Haruna really can't do housework...)",
     "Я ничего не знаю… хотя Харуна и правда не умеет работать по дому…"),
42: ("B-By the way, what's going to happen to Haruna and Akina from now on?",
     "К-Кстати, что будет с Харуной и Акиной дальше?"),
43: ("The court healer says there are few cases like this, so she can't say for certain...",
     "Придворный целитель говорит, что случаев таких мало, поэтому пока ничего не скажешь…"),
44: ("But she should recover little by little, given time.", "Но со временем она должна восстановиться понемногу."),
45: ("I see.", "Понятно."),
46: (None, None),
47: ("Well then, see you, Saito.", "Ну что ж, пока, Сайто."),
48: ("I'm sorry for all the trouble I caused...", "Прости за все неприятности, которые я причинила…"),
49: ("D-Don't worry about it!", "Н-Не беспокойся!"),
50: ("But it'll get lonely. Even though it's one person, it feels like losing two.",
     "Но станет одиноко. Хотя она одна — кажется, будто лишился двух."),
51: ("You can meet her whenever you want. It's not far from the academy to Tristain.",
     "Ты можешь встретиться с ней когда захочешь. От академии до Тристании недалеко."),
52: ("T-That's right, isn't it.", "Т-Точно, да?"),
53: ("Then, it's about time...", "Тогда, пожалуй, пора…"),
54: ("Oh, right. Haruna.", "Ах, да. Харуна."),
55: ("...What is it?", "…Что?"),
56: ("This stupid dog is my familiar for life, you know!", "Этот глупый пёс — мой фамильяр на всю жизнь, понятно!"),
57: ("W-What are you saying all of a sudden.", "Ч-Что это ты вдруг сказала."),
58: ("This much I have to make clear.", "Это я должна прояснить."),
59: ("But this has nothing to do with romance!", "Но это же совсем не про любовь!"),
60: ("Eh?", "А?"),
61: ("My, my.", "Ой-ой."),
62: ("Sigh... Give me a break already...", "Ох… Ну дайте мне уже покой…"),
}
CHOICES = {
544: [("Mention it, just in case?", "Стоит упомянуть, на всякий случай?"),
      ("Ah, never mind...", "Да ладно…"),
      ("I don't know anything...", "Я ничего не знаю…")],
}
SPK = {'サイト': 's', 'ルイズ': 'l', 'アンリエッタ': 'h', 'アキナ': 'ak',
       'ハルナ': 'ha', 'null': 'th'}
START = {'s': 134, 'l': 78, 'h': 15, 'ak': 76, 'ha': 30, 'th': 2}


def main():
    data = json.load(open('reports/ch12/parse_544_548.json', encoding='utf-8'))
    script = ['# Глава 12, часть 4 (сцены 544–548): финал, Луиза и её фамильяр.',
              '# Источник: ps2_source/chapters/chapter_13_もう一人のハルナ.txt (SCENE 544-548).',
              '', 'label ch12_4:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            scene = x['no']
            script += ['label ch12_4_scene_%d:' % scene, '']
            continue
        if k == 'event':
            event(x['src'], script)
            continue
        if k == 'dlg':
            en, ru = T[x['idx']]
            if en is None:
                script.append('    # ' + x['src'] + ' (no voice — пропущено по образцу ch11_2)')
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
                ctext = '%s{#ch12_4_c_%d_%d}' % (en_norm(en), scene, i + 1)
                tgt = 'ch12_4_scene_%d' % o['target']
                script.append('        "%s":' % ctext)
                script.append('            jump %s' % tgt)
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump ch12_4_scene_%d' % x['target'])
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 12 ====', '    jump ch13', '    return', '']
    files = {
        'game/chapters/12/script-ch12_4.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch12_4_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch12_4_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch12_4_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch12_4_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch12/voice_map_4.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
