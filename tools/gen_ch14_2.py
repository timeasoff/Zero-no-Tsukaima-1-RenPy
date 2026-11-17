#!/usr/bin/env python3
"""Chapter 14 part 2 (extra scenes 1485-1488): searching for Weatherly."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
379: ("...", "…"),
380: ("Mm, Weatherly isn't here either.", "Мм, Уэзерби здесь нет."),
381: ("Well, if our deduction is right, she shouldn't be here anyway.",
      "Ну, если наша догадка верна, её здесь и не должно быть."),
382: ("You think so? The castle must be part of the final objective. She might be keeping watch.",
      "Думаешь? Замок наверняка входит в конечную цель. Она может наблюдать."),
383: ("We don't know what she's planning.", "Мы не знаем, что она задумала."),
384: ("Y-Yes, I guess...", "Д-Да, наверное…"),
385: ("Weatherly isn't here either...", "Уэзерби здесь тоже нет…"),
386: ("Yeah, I suppose.", "Да, похоже."),
387: ("Look, darling. This place is full of couples.", "Смотри, дорогой. Здесь полно пар."),
388: ("Ugh. It is a good atmosphere, though.", "Ох. Хотя атмосфера здесь и правда хорошая."),
389: ("Darling, shall we declare our love here too?",
      "Дорогой, почему бы нам не объясниться в любви здесь?"),
390: ("Kirche, this isn't the time for that.", "Кирке, сейчас не до этого."),
391: ("Oh, is that so? Too bad. Let's do it another time.",
      "О, правда? Жаль. Тогда в другой раз."),
392: ("Phew...", "Фух…"),
393: ("She's not here either.", "Здесь её тоже нет."),
394: ("Tristain really is under construction everywhere.", "В Тристании и правда всюду стройка."),
395: ("Because the bomb-thrower keeps destroying things. The locals have it rough.",
      "Из-за того, что бомбист всё разрушает. Местным достаётся."),
396: ("And there are more foreigners—craftsmen and such.",
      "И иностранцев стало больше — ремесленников и прочих."),
397: ("Naturally, with people coming and going, public order gets worse, they say.",
      "Естественно, при наплыве людей порядок ухудшается, говорят."),
398: ("I see. Even thinking about it, we need to settle this soon.",
      "Понятно. Даже судя по этому, нужно скорее покончить с этим."),
399: ("Yeah...", "Да…"),
400: ("Weatherly isn't here, is she...", "Уэзерби здесь нет, да…?"),
401: ("Looks like it.", "Похоже."),
402: ("By the way, today it's Kirche's familiar... er...",
      "Кстати, сегодня фамильяр Кирке… э-э…"),
403: ("Flame?", "Флейм?"),
404: ("Right, that. Where did Flame go?", "Да, он. Куда девался Флейм?"),
405: ("She's minding the academy. She'd stand out too much in the capital.",
      "Она осталась в академии. В столице она бы слишком выделялась."),
406: ("Well, if anything happens, I'll bring her right away.",
      "Впрочем, если что-то случится, я сразу её приведу."),
407: ("I see...", "Понятно…"),
408: ("Yeah. She might be a little angry, actually.", "Да. Она, кажется, немного сердится."),
409: ("...Eh?", "…А?"),
410: ("She might be mad that you're keeping me all to yourself.",
      "Она может сердиться, что ты забираешь меня себе целиком."),
411: ("Watch out she doesn't take a bite out of you.", "Осторожно, как бы она тебя не укусила."),
412: ("Bite? W-What is that supposed to mean!?", "Укусила? Ч-Что это значит!?"),
413: ("Come on, darling. Let's try the next place. Next!",
      "Ну же, дорогой. Пойдём в следующее место. Давай!"),
}
SPK = {'サイト': 's', 'キュルケ': 'k', 'null': 'th'}
START = {'s': 60, 'k': 50, 'th': 2}


def main():
    data = json.load(open('reports/ch14/parse_578_619.json', encoding='utf-8'))
    script = ['# Глава 14, часть 2 (сцены 1485–1488): поиски Уэзерби по маршрутам.',
              '# Источник: ps2_source/chapters/chapter_15_私のお兄ちゃん.txt (SCENE 1485-1488).',
              '', 'label ch14_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d = [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if not 1485 <= x['no'] <= 1488:
                continue
            scene = x['no']
            script += ['label ch14_2_scene_%d:' % scene, '']
            continue
        if k == 'event':
            if scene:
                event(x['src'], script)
            continue
        if k == 'dlg':
            if not scene or x['idx'] not in T:
                continue
            en, ru = T[x['idx']]
            if en is None:
                continue
            en = en_norm(en)
            spk = SPK.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch14_%s_%03d' % (spk, counters[spk])
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
    script += ['    # ==== КОНЕЦ ЧАСТИ 2 ====', '    jump ch14_3', '    return', '']
    files = {
        'game/chapters/14/script-ch14_2.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch14_2_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch14_2_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch14/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
