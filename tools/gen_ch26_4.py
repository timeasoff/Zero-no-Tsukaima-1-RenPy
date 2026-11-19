#!/usr/bin/env python3
"""Chapter 26 part 4 (scenes 965-966): Akina's attack, Tabitha's backstory."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
368: ("So that was the real purpose of the mission...", "Так вот настоящая цель задания…"),
369: ("Eh? The mission...", "А? Задание…"),
370: ("Are you saying Gallia knew Haruna was the bomber?", "Ты хочешь сказать, что Галлия знала: Харуна — бомбист?"),
371: ("Tabitha, tell me. Just how much does Gallia know?", "Табаса, скажи. Что именно знает Галлия?"),
372: ("...", "…"),
373: ("Wait a moment. You really intend to capture Haruna and take her to Gallia?",
     "Погоди. Ты и правда намерена захватить Харуну и увезти в Галлию?"),
374: ("The personality is Akina now, but the body is Haruna's!",
     "Личность сейчас Акина, но тело — самоё Харуны!"),
375: ("...", "…"),
376: ("Hey, Tabitha!?", "Эй, Табаса!?"),
377: ("Hey now, infighting? You're still too soft...", "Ого, ссора между своими? Ты всё так же мягок…"),
378: ("Take this!!", "Получи!!"),
379: ("Saito...!!", "Сайто…!!"),
380: ("Wha—Tabitha!", "Ах — Табаса!"),
381: ("Ha ha ha ha ha! This is comedy! That Tabitha shielding Saito!",
     "Ха-ха-ха-ха! Это комедия! Табаса защищает Сайто!"),
382: ("Shut up, shut up! Be quiet!", "Замолчи, замолчи! Помалкивай!"),
383: ("Ooh, scary.", "Ой, страшно."),
384: ("Why did you shield me...", "Почему ты меня прикрыла…"),
385: ("...Are you all right?", "…Ты в порядке?"),
386: ("Ah, I'm fine. I'm all right.", "Ах, я в порядке. Всё хорошо."),
387: ("Thank goodness...", "Слава богу…"),
388: ("Hey, Tabitha? Wake up, wake up!", "Эй, Табаса? Проснись, проснись!"),
389: ("Ah ha ha, just as I thought. I knew you'd gallantly shield Saito that way.",
     "А-ха-ха, как я и думала. Я знала, что ты самоотверженно прикрыешь Сайто."),
390: ("And knowing that, you still threw the bomb at me?", "И, зная это, ты всё равно бросила в меня бомбу?"),
391: ("Oh yes, exactly. And sure enough—willing to risk your life to shield him. "
      "What a gallant girl.", "О да, именно. И точно — готова была пожертвовать собой ради него. "
      "Какая самоотверженная девушка."),
392: ("Then, I suppose it's time for me to say goodbye.", "Тогда, думаю, пора мне попрощаться."),
393: ("Hey—don't you run away!", "Эй — не смей убегать!"),
394: ("Then just chase me. Leaving that girl burning for your sake behind—right?~",
     "Тогда догоняй. Оставив ту девушку гореть ради тебя — да?~"),
395: ("Ugh, damn it!", "Ох, чёрт!"),
396: ("I told you, didn't I? That kindness of yours hurts everyone. Ah ha ha, see you~!",
     "Я же говорила? Что твоя доброта ранит всех. А-ха-ха, до встречи~!"),
397: ("Using Haruna's body like that... What a horrible thing to do!",
     "Использовать тело Харуны так… Какая ужасная вещь!"),
398: ("(After that, we were taken in by Louise and Kirche, who'd rushed to the scene.)",
     "После этого нас взяли под опеку Луиза и Кирке, которые поспешили на место."),
399: ("(It took a lot of medicine and magic to treat Tabitha's burns...)",
     "Для лечения ожогов Табасы потребовалось много лекарств и магии…"),
400: ("(But fortunately—if one can call it that—Montmorency and Guiche, having heard "
      "the commotion, came to our lodgings.)", "Но, к счастью — если можно так сказать — "
      "Монморанси и Гиш, услышав шум, пришли в нашу гостиницу."),
401: ("(I managed to calm the two down, who wanted to hear the story, and had Montmorency "
      "treat Tabitha's injuries right away.)", "Я кое-как успокоил двоих, которые хотели "
      "всё узнать, и попросил Монморанси срочно лечить Табасу."),
402: ("Phew... She should be all right now.", "Фух… Теперь она должна быть в порядке."),
403: ("Really? Is she really all right?", "Правда? Она и правда в порядке?"),
404: ("I healed all the burns. She's truly fine.", "Я вылечила все ожоги. Она и правда в порядке."),
405: ("What she needs now is rest. She should stay quiet for a few days.",
     "Ей нужно восстановить силы. Несколько дней она должна полежать тихо."),
406: ("And watch for fever. There's still a chance the burns could become inflamed.",
     "И следите за жаром. Ещё есть риск воспаления ожогов."),
407: ("Got it. I'll nurse her with all my care.", "Понял. Я буду ухаживать за ней изо всех сил."),
408: ("Then, I'll go rest, too.", "Тогда я тоже пойду отдыхать."),
409: ("Thanks, Montmorency.", "Спасибо, Монморанси."),
410: ("Good—that we're still in the capital.", "Хорошо, что мы всё ещё в столице."),
411: ("You're right.", "Верно."),
412: ("With all this war-like commotion, we couldn't leave the capital—it was a real problem.",
     "Из-за всей этой войны нельзя выйти из столицы — вот была проблема."),
413: ("Well, that's what you call luck, I suppose...", "Ну, это можно назвать удачей…"),
414: ("Yes, it is. Now, let me rest. I'm quite tired myself.", "Да. А теперь я пойду отдыхать. Я и сама сильно устала."),
415: ("...", "…"),
416: ("(Tabitha getting hurt—it's my fault, after all...)", "Табаса пострадала — в конце концов, это моя вина…"),
417: ("(If I hadn't followed her, maybe Tabitha would've beaten Haruna—no, Akina—on her own...)",
     "Если бы я не пошёл за ней, может, Табаса победила бы Харуну — нет, Акину — одна…"),
418: ("Haa... What am I...", "Хаа… Что же я…"),
419: ("What are you moping about?", "Что ты хмуришься?"),
420: ("N-Nothing!", "Н-Ничего!"),
421: ("Hmm. Is that so.", "Хм. Вот как."),
422: ("...", "…"),
423: ("...", "…"),
424: ("Well—about nursing Tabitha. I'll help you, too.", "Так — по поводу ухода за Табасой. Я тоже помогу."),
425: ("Eh? Why?", "А? Почему?"),
426: ("Why? It's obvious. A familiar's mess is the mistress's responsibility.",
     "Почему? Это очевидно. Ошибки фамильяра — ответственность госпожи."),
427: ("I see. Thanks.", "Понятно. Спасибо."),
428: ("What's that...? Talk back to me like usual. It throws me off...",
     "Это что ещё такое…? Возрази мне как обычно. Я сбилась с толку…"),
429: ("Tabitha ended up like this because of me...", "Табаса оказалась в таком состоянии из-за меня…"),
430: ("You being down won't make Tabitha heal any faster, you know?",
     "Твоя подавленность не ускорит выздоровление Табасы, правда?"),
431: ("Well, yes, but...", "Ну, да, но…"),
432: ("Honestly... I'll go change the water.", "Право… Я пойду сменить воду."),
433: ("Mm... Please.", "Мм… Пожалуйста."),
434: ("(Tabitha's hands are so small...)", "У Табасы такие маленькие руки…"),
435: ("(Holding her hand and watching her sleep—even I, nursing her, can relax a little...)",
     "Держа её руку и глядя на её сон — даже я, ухаживая за ней, могу немного расслабиться…"),
436: ("(Come to think of it...)", "Кстати…"),
437: ("(I remember—after my duel with Guiche, Louise nursed me...)",
     "Я помню — после моей дуэли с Гишем Луиза ухаживала за мной…"),
438: ("(Was Louise feeling the same way back then...?)", "Может, Луиза тогда чувствовала то же…?"),
439: ("Here, I've changed the water.", "Вот, я поменяла воду."),
440: ("...", "…"),
441: ("Wh-What? Staring at my face like that.", "Ч-Что? Ты смотришь на моё лицо."),
442: ("No, it's nothing.", "Нет, ничего."),
443: ("Mm...", "Мм…"),
444: ("Ah, Tabitha?", "Ах, Табаса?"),
445: ("...Mm, mmph.", "…Мм, м-м."),
446: ("Sounds like she's talking in her sleep. She seems a little restless, but is she all right?",
     "Похоже, она говорит во сне. Она немного беспокоится, но всё ли хорошо?"),
447: ("Who knows?", "Кто знает?"),
448: ("...Sama.", "…сама."),
449: ("Eh? What did she say?", "А? Что она сказала?"),
450: ("...Mother.", "…Мама."),
451: ("I thought I heard 'mother'...?", "Мне показалось, она сказала «мама»…?"),
452: ("Mother, don't drink that. Mother.", "Мама, не пей это. Мама."),
453: ("I'm coming in. How's Tabitha?", "Я вхожу. Как Табаса?"),
454: ("Thanks to Montmorency's healing magic, I think her condition is stable.",
     "Благодаря целебной магии Монморанси, думаю, её состояние стабильно."),
455: ("Oh, good...", "Ох, хорошо…"),
456: ("Say, Kirche. There's something I want to ask. Can I?", "Слушай, Кирке. Я хочу кое-что спросить. Можно?"),
457: ("About Tabitha? Sure.", "О Табасе? Конечно."),
458: ("Why does Tabitha keep taking missions from Gallia?", "Почему Табаса всё время берёт задания из Галлии?"),
459: ("Gallia knew about Haruna—it's suspicious. What exactly is Tabitha carrying?",
     "Галлия знала о Харуне — подозрительно. Что именно несёт Табаса?"),
460: ("That... I'll have to tell you about Tabitha's family.", "Это… придётся рассказать о семье Табасы."),
461: ("Got it? Just between us.", "Понял? Только между нами."),
462: ("Ah... Yeah.", "Ах… Да."),
463: ("Tabitha's family—they were actually of the royal line that rules Gallia.",
     "Семья Табасы — на самом деле из королевского рода, правящего Галлией."),
464: ("Were, meaning...? Don't tell me...?", "Были — это значит…? Неужто…?"),
465: ("Yes. Tabitha is a princess.", "Да. Табаса — принцесса."),
466: ("So that's it...", "Так вот как…"),
467: ("But she got caught up in a power struggle, and her father was assassinated.",
     "Но её втянули в борьбу за власть, и отец был убит."),
468: ("That's awful... They'd go that far against family?", "Ужасно… Они пошли на такое против родных?"),
469: ("Oh, that's normal. It happens in every country.", "О, это нормально. В любой стране бывает."),
470: ("Is that so?", "Правда?"),
471: ("And her mother, protecting Tabitha, drank poison as well.",
     "А её мать, защищая Табасу, тоже выпила яд."),
472: ("It affected her mind... She no longer seems to recognize Tabitha.",
     "Это повредило её разум… Она, кажется, больше не узнаёт Табасу."),
473: ("Her mother—poisoned? Ah, now I remember...", "Мать — отравили? Ах, теперь вспомнил…"),
474: ("The words Tabitha said in her sleep...", "Слова, которые Табаса сказала во сне…"),
475: ("What about her sleep-talking?", "Что насчёт её слов во сне?"),
476: ("She said—'Mother, don't drink that.'", "Она сказала: «Мама, не пей это»."),
477: ("I see...", "Понятно…"),
478: ("But that alone didn't stop Gallia's attacks.", "Но одного этого не хватило, чтобы остановить нападения Галлии."),
479: ("They kept dumping brutal missions on Tabitha, in the form of 'requests.' "
      "And all of them were life-threatening.", "Они продолжали сваливать на Табасу жестокие задания "
      "в форме «просьб». И все они были смертельно опасны."),
480: ("Tabitha...", "Табаса…"),
481: ("Even so, she carries them out without complaint to protect her mother.",
     "И всё же она выполняет их без жалоб, чтобы защитить мать."),
482: ("Keeping the enemy from laying a hand on her mother—that's Tabitha's reason to live.",
     "Не дать врагу тронуть её мать — вот смысл жизни Табасы."),
483: ("I see... That's how it was...", "Так вот как… Такие обстоятельства…"),
484: ("(Then I can't tell her to stop taking Haruna to Gallia...)",
     "Тогда я не могу просить её не увозить Харуну в Галлию…"),
}
SPK = {'タバサ': 't', 'サイト': 's', 'アキナ': 'ak', 'モンモランシー': 'm',
       'ルイズ': 'l', 'キュルケ': 'k', 'null': 'th'}
START = {'t': 46, 's': 138, 'ak': 16, 'm': 2, 'l': 64, 'k': 31, 'th': 4}


def main():
    data = json.load(open('reports/ch26/parse_934_971.json', encoding='utf-8'))
    script = ['# Глава 26, часть 4 (сцены 965–966): атака Акины, прошлое Табасы.',
              '# Источник: ps2_source/chapters/chapter_27_タバサの秘密.txt (SCENE 965-966).',
              '', 'label ch26_4:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            scene = x['no'] if 965 <= x['no'] <= 966 else None
            if scene is None:
                continue
            script += ['label ch26_4_scene_%d:' % scene, '']
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
        if k == 'goto':
            if scene is None or not 965 <= scene <= 966: continue
            t = x['target']
            if t in (965, 966):
                dest = 'ch26_4_scene_%d' % t
            elif t == 967:
                dest = 'ch26_4b'
            else:
                continue
            script.append('    # → next scene %d' % t)
            script.append('    jump %s' % dest)
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 4 ====', '    jump ch26_4b', '    return', '']
    files = {
        'game/chapters/26/script-ch26_4.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch26_4_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch26_4_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch26_4_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch26_4_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch26/voice_map_4.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
