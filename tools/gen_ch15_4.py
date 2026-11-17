#!/usr/bin/env python3
"""Chapter 15 part 4 (scenes 654-659): finale, Weatherly's surrender."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
339: ("Come on, let's go! The castle's high ground is our goal!",
      "Ну же, идём! Нам нужна высота замка!"),
340: ("Let's go, Derflinger!", "Идём, Дерфлингер!"),
341: ("Right you are, partner.", "Верно, приятель."),
342: ("Leave that side to me, darling!", "Эту сторону доверь мне, дорогой!"),
343: ("I'll do my best.", "Постараюсь."),
344: ("Ah, enemies there.", "А, враги."),
345: ("(That the palace would become a battlefield...)", "(Что дворец станет полем боя…)"),
346: ("(I'm counting on you, everyone...)", "(Я на вас рассчитываю, все…)"),
347: ("E-Eek!", "О-Ой!"),
348: ("Don't freeze up and stop! If you don't want to die, run, Guiche!",
      "Не застывай! Если не хочешь умереть — беги, Гиш!"),
349: ("The summit should be close now...", "До вершины должно быть недалеко…"),
350: ("Darling, look out!", "Дорогой, осторожно!"),
351: ("Whoa!", "Ого!"),
352: ("...", "…"),
353: ("My, Saito. You look well...", "Ой, Сайто. Ты в порядке…"),
354: ("H-Haruna! Why are you doing this...", "Х-Харуна! Зачем ты это…"),
355: ("Don't call me Haruna! My name is Akina!", "Не называй меня Харуной! Моё имя — Акина!"),
356: ("My, who do we have here... It seems you've drawn the lead role "
      "in another grand performance.",
      "Ой, кто это… Похоже, вы снова достали главную роль для большого спектакля."),
357: ("Weatherly! How dare you do this to me...", "Уэзерби! Как ты смела так поступить со мной…"),
358: ("Oh, Kirche. Did the suggestion wear off?", "Ой, Кирке. Внушение уже прошло?"),
359: ("I undid it.", "Я сняла его."),
360: ("I see, Montmorency did. I thought I'd set it fairly deep... "
      "perhaps luck was on your side?",
      "Понятно, Монморанси. Я думала, что внушение было довольно глубоким… "
      "может, вам повезло?"),
361: ("Well? Did you get to return to a pure child's heart?",
      "Ну как? Удалось вернуться к чистому детскому сердцу?"),
362: ("None of your business.", "Не твоё дело."),
363: ("Thanks to some middle-aged woman showing us nothing but boring flames, "
      "I couldn't even sleep properly.",
      "Благодаря одной стареющей женщине, которая показывала только скучные пожары, "
      "я даже поспать как следует не смогла."),
364: ("Oh, and who might this 'middle-aged woman' be?", "Ой, а кто же эта «стареющая женщина»?"),
365: ("Weatherly-sama, of course.", "Конечно, Уэзерби-сама."),
366: ("How rude. Age doesn't matter to an actor.", "Как грубо. Для актрисы возраст не важен."),
367: ("The final act. It seems the cast wants it blood-soaked.",
      "Последний акт. Похоже, актёры хотят обагрить его кровью."),
368: ("Fine. Then let them spill as much blood as they like!",
      "Хорошо. Пусть прольют столько крови, сколько хотите!"),
369: ("Here I go! I won't let them interfere with Louise!",
      "Я начинаю! Не дам помешать Луизе!"),
370: ("This is the end, Weatherly! Akina!", "Конец, Уэзерби! Акина!"),
371: ("Damn!", "Чёрт!"),
372: ("Tch!", "Тьфу!"),
373: ("Now, feast your eyes on the magic of Void!", "Смотри же хорошенько на магию Пустоты!"),
374: ("Illusion!!", "Иллюзия!!"),
375: ("W-What! Out of the clouds...", "Ч-Что! Из облаков…"),
376: ("No way... an aerial fleet?", "Не может быть… воздушный флот?"),
377: ("What is this! Tristain—no, no country in Halkeginia has a fleet like that...!?",
      "Что это! Тристания — нет, ни одна страна в Халкегинии не имеет такого флота…!?"),
378: ("(So that's what Louise wanted. That fleet must be an illusion... "
      "something Void created...)",
      "(Так вот что хотела Луиза. Этот флот — иллюзия… то, что создала Пустота…)"),
379: ("Weatherly-sama, our fleet is retreating!", "Уэзерби-сама, наш флот отступает!"),
380: ("...And the troops around the castle too!", "…И войска у замка тоже!"),
381: ("We've lost... With the fleet gone, our numbers are meaningless.",
      "Мы проиграли… Без флота наши силы ничего не значат."),
382: ("Well done. Now, bring down the curtain on this farce!",
      "Браво. Теперь опустите занавес этого фарса!"),
383: ("(What does she mean?)", "(Что она имеет в виду?)"),
384: ("(She's telling you to cut her down, partner.)", "(Она говорит, чтобы ты её зарубил, приятель.)"),
385: ("...C-Cut her down?", "…З-Зарубить её?"),
386: ("Why hesitate? Or do you want me to throw myself from the tower "
      "like in that play?",
      "Чего ты колеблешься? Или хочешь, чтобы я бросилась с башни, как в том спектакле?"),
387: ("Tch... No. I can't let her die.", "Тьфу… Нет. Не могу я её убить."),
388: ("(There's no way I could cut down a girl!)", "(Я не смогу зарубить девушку!)"),
389: ("That's irresponsible, isn't it?", "Это безответственно, не правда ли?"),
390: ("What?", "Что?"),
391: ("You were going to leave Haruna like this? You're the one who made her "
      "into 'Akina', aren't you?",
      "Ты собиралась оставить Харуну такой? Это ты создала личность «Акина», верно?"),
392: ("No. I can't let her die.", "Нет. Я не дам ей умереть."),
393: ("Right. We still have use for Weatherly.", "Верно. У нас ещё есть дела до Уэзерби."),
394: ("We need her to lift Haruna's suggestion. And to answer for what she's done.",
      "Нам нужно, чтобы она сняла внушение с Харуны. И ответила за содеянное."),
395: ("I see. Very well, I surrender.", "Понятно. Ладно, я сдаюсь."),
396: ("Akina, that's fine with you too?", "Акина, ты тоже согласна?"),
397: ("I will obey Weatherly-sama...", "Я подчинюсь Уэзерби-саме…"),
398: ("Then I'll go fetch a soldier. We need them taken into custody.",
      "Тогда я позову солдата. Их нужно взять под стражу."),
399: ("Ah, please do.", "А, пожалуйста."),
400: ("Looks like the fighting in the city is mostly over.", "Похоже, бои в городе почти закончились."),
401: ("Good. Phew... I'm exhausted. At my limit...", "Хорошо. Фух… Я выбилась. Совсем…"),
402: ("Still, creating an illusion... There really is such magic.",
      "Всё-таки создать иллюзию… Бывает и такая магия."),
403: ("Mm... Even if they're enemies, it's better not to hurt anyone. "
      "That's why I chose that spell.",
      "Мм… Даже врагов лучше не ранить. Поэтому я выбрала это заклинание."),
404: ("Yeah. You're right.", "Да. Ты права."),
405: ("Anyway, get some rest. Good work, Louise.", "В любом случае, отдохни. Хорошо поработала, Луиза."),
406: ("Mm...", "Мм…"),
}
CHOICES = {
655: [("Cut her down?", "Зарубить её?"),
      ("That's irresponsible, isn't it?", "Это безответственно, не правда ли?"),
      ("I still need Weatherly", "У меня ещё есть дела до Уэзерби")],
}
SPK = {'ルイズ': 'l', 'サイト': 's', 'デルフリンガー': 'd', 'キュルケ': 'k',
       'タバサ': 't', 'アキナ': 'ak', 'ウェザリー': 'w', 'モンモランシー': 'm',
       'ギーシュ': 'g', 'null': 'th'}
START = {'s': 104, 'l': 83, 'd': 4, 'k': 42, 't': 5, 'ak': 22, 'w': 0, 'm': 15, 'g': 1, 'th': 0}


def main():
    data = json.load(open('reports/ch15/parse_619_659.json', encoding='utf-8'))
    script = ['# Глава 15, часть 4 (сцены 654–659): финал, иллюзия, капитуляция Уэзерби.',
              '# Источник: ps2_source/chapters/chapter_16_魔法の薬.txt (SCENE 654-659).',
              '', 'label ch15_4:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 659:
                break
            if x['no'] < 654:
                continue
            scene = x['no']
            script += ['label ch15_4_scene_%d:' % scene, '']
            continue
        if k == 'event':
            if scene:
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
            tag = 'ch15_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch15_4_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch15_4_scene_659')
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 654 <= scene <= 659:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch15_4_scene_%d' % x['target']
                                          if 654 <= x['target'] <= 659 else 'ch16'))
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 15 ====', '    jump ch16', '    return', '']
    files = {
        'game/chapters/15/script-ch15_4.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch15_4_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch15_4_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch15_4_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch15_4_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch15/voice_map_4.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
