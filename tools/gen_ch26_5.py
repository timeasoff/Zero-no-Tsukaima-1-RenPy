#!/usr/bin/env python3
"""Chapter 26 part 5 (extra 1219-1223): pinky promise with Tabitha."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
554: ("Ah, there's Tabitha. She seems well enough to go outside. Good.",
     "Ах, вон Табаса. Похоже, она уже поправилась настолько, что может выйти. Хорошо."),
555: ("But what's wrong? She keeps looking down... Now I'm curious...",
     "Но что случилось? Она всё время смотрит вниз… Теперь мне стало интересно…"),
556: ("Hey there, Tabitha~.", "Эй, Табаса~."),
557: ("...", "…"),
558: ("What's wrong? Going for a walk? You shouldn't overdo it yet, should you?",
     "Что случилось? Гуляешь? Ты же ещё не должна напрягаться, да?"),
559: ("Mm.", "Мм."),
560: ("You keep looking down like that?", "Ты всё время вот так смотришь вниз?"),
561: ("Thinking.", "Думаю."),
562: ("Eh, thinking? Could it be...", "А, думаешь? Неужто…"),
563: ("About me, perhaps?", "Обо мне, например?"),
564: ("A little close.", "Отчасти."),
565: ("What do you mean, 'a little'? So what exactly...?", "Что значит «отчасти»? Тогда про что именно…?"),
566: ("Why I shielded you.", "Почему я тебя прикрыла."),
567: ("About how I shielded you?", "О том, что ты меня прикрыла?"),
568: ("Mm.", "Мм."),
569: ("Um... You mean you wish you hadn't?", "Э-Э… Ты хочешь сказать, что жалеешь?"),
570: ("No. I thought I should.", "Нет. Я подумала, что должна была."),
571: ("Ha ha, ha ha...", "Ха-ха, ха-ха…"),
572: ("(A complicated feeling...)", "Сложное чувство…"),
573: ("But...", "Но…"),
574: ("About Haruna, perhaps?", "О Харуне, например?"),
575: ("Partly right. But not quite.", "Отчасти верно. Но не совсем."),
576: ("What, not quite?", "Что, не совсем?"),
577: ("Then what were you thinking about?", "Тогда о чём ты думала?"),
578: ("Why I shielded you then.", "Почему я тогда тебя прикрыла."),
579: ("Looking back... I could have handled it with magic.", "Оглядываясь назад… я могла справиться магией."),
580: ("T-That's true, maybe...", "П-Правда, может быть…"),
581: ("Failure.", "Прова́л."),
582: ("Hmm—so you mean your body moved before you could think, basically?",
     "Хм — то есть, проще говоря, тело сработало раньше, чем ты успела подумать?"),
583: ("Looks like it. I wonder why that happened.", "Похоже. Интересно, почему так получилось."),
584: ("Ha ha ha... Well then, if something like that happens again, you can just let me get hit, okay?",
     "Ха-ха-ха… Тогда, если такое случится снова, ты можешь просто бросить меня на произвол судьбы, ладно?"),
585: ("No. I'm sure I won't be able to ignore it...", "Нет. Я наверняка не смогу это игнорировать…"),
586: ("It's fine. I'm used to getting hurt.", "Всё хорошо. Я привык получать травмы."),
587: ("...", "…"),
588: ("Ah—you don't believe me, do you? I'm tougher than Tabitha thinks!",
     "Ах — ты мне не веришь, да? Я выносливее, чем думает Табаса!"),
589: ("(I do get punished by Louise all the time, after all...)", "Меня же всё время наказывает Луиза…"),
590: ("So—if that happens again, just fight without worrying about me, all right?",
     "Так что — если такое случится снова, сражайся, не беспокоясь обо мне, ладно?"),
591: ("...", "…"),
592: ("Don't make that face. I was more upset that you got burned than that I was safe.",
     "Не делай такое лицо. Я больше расстраивался из-за твоего ожога, чем радовался, что сам уцелел."),
593: ("...Mm.", "…Мм."),
594: ("So please... Don't do anything reckless again, okay?", "Так что, пожалуйста… Больше не делай глупостей, ладно?"),
595: ("...", "…"),
596: ("Oh—so you're not sure you can protect me, are you?", "Ох — значит, ты не уверена, что сможешь меня защитить, да?"),
597: ("...", "…"),
598: ("Then, how about a pinky promise?", "Тогда давай поклянёмся на мизинцах?"),
599: ("Pinky promise?", "Клятва на мизинцах?"),
600: ("Where I come from, when two people make a private promise, they do it like this...",
     "У меня дома, когда двое заключают личный договор, делают вот так…"),
601: ("Ah...", "Ах…"),
602: ("Hooking little fingers together...", "Переплетя мизинцы…"),
603: ("...", "…"),
604: ("...and sealing the promise to the rhyme.", "…и скрепляя договор считалкой."),
605: ("Meaning... a contract?", "То есть… договор?"),
606: ("Hmm, something like that. Well then, here we go...", "Хм, что-то вроде того. Ну что ж, начнём…"),
607: ("Yubi-piki, genman. If you lie—too bad! And I'll cut your finger off!",
     "Юби-пики, гэнман. солжёшь — плохо будет! И я отрежу тебе палец!"),
608: ("...", "…"),
609: ("So, that means we promised, right?", "Ну, раз поклялись — полагаюсь на тебя, ладно?"),
610: ("...Mm. I'll try not to be reckless.", "…Мм. Постараюсь не делать глупостей."),
611: ("Ha ha ha... 'Try' won't do, you know...", "Ха-ха-ха… «Постараюсь» — этого мало…"),
}
CHOICES = {
1219: [("About me?", "Обо мне?"),
       ("About shielding you?", "О том, что ты меня прикрыла?"),
       ("About Haruna?", "О Харуне?")],
}
SPK = {'サイト': 's', 'タバサ': 't', 'null': 'th'}
START = {'s': 197, 't': 57, 'th': 4}


def main():
    data = json.load(open('reports/ch26/parse_934_971.json', encoding='utf-8'))
    script = ['# Глава 26, часть 5 (extra 1219–1223): клятва на мизинцах с Табасой.',
              '# Источник: ps2_source/chapters/chapter_27_タバサの秘密.txt (extra 1219-1223).',
              '', 'label ch26_5:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if not 1219 <= x['no'] <= 1223: continue
            scene = x['no']
            script += ['label ch26_5_scene_%d:' % scene, '']
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
                ctext = '%s{#ch26_5_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch26_5_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 1219 <= scene <= 1223: continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump ch27' if not (1219 <= x['target'] <= 1223) else '    jump ch26_5_scene_%d' % x['target'])
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 26 ====', '    jump ch27', '    return', '']
    files = {
        'game/chapters/26/script-ch26_5.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch26_5_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch26_5_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch26_5_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch26_5_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch26/voice_map_5.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == "__main__":
    main()
