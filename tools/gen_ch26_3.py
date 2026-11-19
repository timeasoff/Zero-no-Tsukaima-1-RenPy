#!/usr/bin/env python3
"""Chapter 26 part 3 (scenes 955-964): Akina reveals herself on the roof."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
266: ("Sigh... Where on earth did Haruna go...", "Ох… Куда же делась Харуна…"),
267: ("Even if she fled because she was afraid of being taken to Gallia, disappearing without "
      "telling me anything...", "Даже если она сбежала, испугавшись поездки в Галлию, исчезнуть, "
      "ничего мне не сказав…"),
268: ("I'm sorry.", "Простите."),
269: ("You don't need to apologize, Tabitha.", "Тебе не за что извиняться, Табаса."),
270: ("But...", "Но…"),
271: ("It's fine... It's not your fault.", "Всё хорошо… Это не твоя вина."),
272: ("...", "…"),
273: ("I'm sure she's safe...", "Я уверен, она в безопасности…"),
274: ("Ba—an explosion!?", "Ба — взрыв!?"),
275: ("Kyaa!?", "Кья-а!?"),
276: ("...", "…"),
277: ("Are you all right, Tabitha? Are you hurt?", "Ты в порядке, Табаса? Не ранена?"),
278: ("Mm, I'm fine.", "Мм, я в порядке."),
279: ("Hey—this theater... It's shaking, isn't it?", "Эй — этот театр… Он трясётся, да?"),
280: ("Looks bad. Everyone, get outside!", "Похоже, плохо. Все, наружу!"),
281: ("Where's the attack coming from!?", "Откуда ведут атаку!?"),
282: ("Ah! On the roof! There's someone there!", "Ах! На крыше! Там кто-то есть!"),
283: ("...!?", "…!?"),
284: ("What's wrong?", "Что случилось?"),
285: ("...", "…"),
286: ("No way... That's Haruna? Why is she up there?", "Не может быть… Это Харуна? Что она там делает?"),
287: ("Sylphid.", "Сильфид."),
288: ("Eh, Tabitha!? You're not really going!?", "А, Табаса!? Ты и правда летишь!?"),
289: ("...", "…"),
290: ("Wait, I'm going, too!", "Погоди, я тоже лечу!"),
291: ("Saito!!", "Сайто!!"),
292: ("Looks like he's fine. Darling's holding onto Sylphid safely.", "Похоже, всё хорошо. "
     "Дорогой безопасно держится за Сильфид."),
293: ("Honestly—always acting on your own!", "Право — вечно действуешь самовольно!"),
294: ("Oh, so even Saito came?", "О, значит, даже Сайто пришёл?"),
295: ("You... Are you really Haruna?", "Ты… Ты и правда Харуна?"),
296: ("Ah ha ha. Who can say?", "А-ха-ха. Кто знает?"),
297: ("Say, Tabitha... You're going to capture me and take me away, aren't you?",
     "Слушай, Табаса… Ты же собираешься меня захватить и увезти, да?"),
298: ("Mm. Be still.", "Мм. Не двигайся."),
299: ("Ha ha ha ha!", "Ха-ха-ха-ха!"),
300: ("If you can catch me, I don't mind being taken away. Am I being too generous?",
     "Если ты меня поймаешь, я не против, чтобы меня увезли. Я слишком добра?"),
301: ("Hey, Haruna. What are you saying? If it's my fault, I'll apologize.",
     "Эй, Харуна. Что ты говоришь? Если я виноват, я извинюсь."),
302: ("Saito, you're still too kind. That's why everyone gets hurt.",
     "Сайто, ты всё такой добрый. Из-за этого все и страдают."),
303: ("Hah!", "Ах!"),
304: ("...", "…"),
305: ("Hey, Tabitha... Are you going to fight?", "Эй, Табаса… Ты собираешься сражаться?"),
306: ("Mm.", "Мм."),
307: ("The opponent is Haruna, you know.", "Ведь противник — Харуна, знаешь."),
308: ("This is my mission.", "Это моё задание."),
309: ("Even so...", "Даже так…"),
310: ("I can't just stand here and stare, can I?", "Я не могу просто стоять и смотреть, да?"),
311: ("But...", "Но…"),
312: ("We just need to knock Haruna out, right? I don't want either of you hurt.",
     "Нужно просто вырубить Харуну, да? Я не хочу, чтобы кто-то из вас пострадал."),
313: ("I can't leave Haruna like this.", "Я не могу оставить Харуну так."),
314: ("But...", "Но…"),
315: ("Ah, I know. I can feel this much killing intent...", "Ах, я понимаю. Я чувствую столько злобы…"),
316: ("The one in front of me now isn't the Haruna we know.", "Тот, кто сейчас передо мной, — не "
     "та Харуна, которую мы знаем."),
317: ("Mm.", "Мм."),
318: ("I can't stand by and watch you fight alone.", "Я не могу смотреть, как ты сражаешься одна."),
319: ("But...", "Но…"),
320: ("It's fine. I'll help you. I'll fight carefully so I don't get in your way.",
     "Всё хорошо. Я помогу. Буду сражаться осторожно, чтобы не мешать тебе."),
321: ("Mm...", "Мм…"),
322: ("(That aside... What on earth happened to Haruna?)", "Это всё, конечно… Что же случилось с Харуной?"),
323: ("Say, Tabitha. I don't know why the Haruna in front of us became like this.",
     "Слушай, Табаса. Я не понимаю, почему Харуна перед нами стала такой."),
324: ("I can't promise I'll hand her over to you. Is that all right?",
     "Я не могу обещать, что отдам её тебе. Это нормально?"),
325: ("Mm.", "Мм."),
326: ("All right, then... Derf, draw!", "Ладно, тогда… Дерф, ную!"),
327: ("Sure, partner... This is getting strange again, isn't it?", "Конечно, приятель… Опять "
     "странная история, да?"),
328: ("It's about Haruna, right? Ah, don't worry. I'll hold back.",
     "Из-за Харуны, да? Ах, не волнуйся. Я буду осторожен."),
329: ("Hold back? What are you talking about? With that attitude, you'll lose, partner.",
     "Осторожен? О чём ты? С таким настроем ты проиграешь, приятель."),
330: ("What do you mean?", "Что ты хочешь сказать?"),
331: ("You'll see soon. My intuition is buzzing. If you want to survive, fight for real.",
     "Скоро увидишь. Моя интуиция будит. Если хочешь выжить, сражайся по-настоящему."),
332: ("Damn...", "Чёрт…"),
333: ("Well, has the chat finished? Then, I'm coming!", "Ну, болтовня закончилась? Тогда я иду!"),
334: ("We won... did we?", "Мы победили… да?"),
335: ("We won...", "Мы победили…"),
336: ("But why... Why would Haruna...", "Но почему… Почему Харуна…"),
337: ("Wrong...", "Не то…"),
338: ("...!?", "…!?"),
339: ("Wrong—what's wrong?", "Не то — что не то?"),
340: ("I'm... not Haruna...", "Я… не Харуна…"),
341: ("Not Haruna...? You look exactly like Haruna to me!", "Не Харуна…? Для тебя ты выглядишь "
     "точно как Харуна!"),
342: ("Ah ha, ah ha ha... Then let me tell you.", "А-ха, а-ха-ха… Тогда я тебе скажу."),
343: ("I am Haruna and not Haruna.", "Я — Харуна и не Харуна."),
344: ("What are you saying, Haruna?", "Что ты говоришь, Харуна?"),
345: ("My name is Akina. I'm a separate personality created by Weatherly-sama...",
     "Меня зовут Акина. Я отдельная личность, созданная Уэзерби-сама…"),
346: ("Weatherly? A separate personality? Where did Haruna go?", "Уэзерби? Отдельная личность? "
     "Куда делась Харуна?"),
347: ("She's asleep inside me. While I'm awake, Haruna is always sleeping.",
     "Она спит во мне. Пока я просыпаюсь, Харуна всегда спит."),
348: ("Don't lie!", "Не лги!"),
349: ("It's not a lie. You've noticed by now, haven't you? The bomber's identity.",
     "Это не ложь. Ты уже догадался, да? Кто такой бомбист."),
350: ("It's me.", "Это я."),
351: ("The bomber? No way...", "Бомбист? Не может быть…"),
352: ("Weatherly, you say...", "Уэзерби, говоришь…"),
353: ("From the theater.", "Из театра."),
354: ("Right—that Weatherly who put on the play, isn't it?", "Верно — та Уэзерби, которая "
     "устраивала спектакль, да?"),
355: ("Ah, now that I think of it—Haruna said she'd met Weatherly somewhere...",
     "Ах, теперь вспомнил — Харуна говорила, что где-то встречалась с Уэзерби…"),
356: ("Was that because her memory was confused?", "Может, её память была спутана?"),
357: ("A separate personality, you say...", "Отдельная личность, говоришь…"),
358: ("Is it really that easy to implant another personality?", "Неужели так легко вселить другую личность?"),
359: ("This 'Akina' doesn't resemble Haruna's personality at all, does she?",
     "Эта «Акина» совсем не похожа на характер Харуны, да?"),
360: ("Human emotions aren't that simple.", "Чувства человека не так просты."),
361: ("I know, but—Haruna would never enjoy hurting people.", "Я знаю, но — Харуна никогда бы "
     "не радовалась, причиняя боль людям."),
362: ("With advanced magic, perhaps...", "С помощью сложной магии, может быть…"),
363: ("Magic...", "Магия…"),
364: ("The bomber's identity, you say...", "Кто такой бомбист, говоришь…"),
365: ("Haruna isn't the type to be happy about becoming a bomber...", "Харуна не тот человек, "
     "который радовался бы, став бомбистом…"),
366: ("A separate personality. That isn't Haruna.", "Отдельная личность. Это не Харуна."),
367: ("Damn... What a terrible thing to do...", "Чёрт… Какая ужасная вещь…"),
}
CHOICES = {
956: [("I can't just stare", "Я не могу просто смотреть"),
      ("Leaving Haruna like this?", "Оставить Харуну так?"),
      ("Letting you fight alone?", "Позволить тебе сражаться одной?")],
961: [("Weatherly...", "Уэзерби…"),
      ("Separate personality...", "Отдельная личность…"),
      ("The bomber's identity...", "Кто такой бомбист…")],
}
SPK = {'サイト': 's', 'タバサ': 't', 'シエスタ': 'si', 'ルイズ': 'l',
       'キュルケ': 'k', 'アキナ': 'ak', 'デルフリンガー': 'd', 'null': 'th'}
START = {'s': 87, 't': 22, 'si': 15, 'l': 61, 'k': 28, 'ak': 0, 'd': 0, 'th': 4}


def main():
    data = json.load(open('reports/ch26/parse_934_971.json', encoding='utf-8'))
    script = ['# Глава 26, часть 3 (сцены 955–964): Акина на крыше.',
              '# Источник: ps2_source/chapters/chapter_27_タバサの秘密.txt (SCENE 955-964).',
              '', 'label ch26_3:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 964: break
            if x['no'] < 955: continue
            scene = x['no']
            script += ['label ch26_3_scene_%d:' % scene, '']
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
                ctext = '%s{#ch26_3_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch26_3_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 955 <= scene <= 964: continue
            t = x['target']
            script.append('    # → next scene %d' % t)
            script.append('    jump %s' % ('ch26_3_scene_%d' % t if 955 <= t <= 964 else 'ch26_4'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 3 ====', '    jump ch26_4', '    return', '']
    files = {
        'game/chapters/26/script-ch26_3.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch26_3_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch26_3_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch26_3_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch26_3_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch26/voice_map_3.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == "__main__":
    main()
