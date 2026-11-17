#!/usr/bin/env python3
"""Chapter 14 part 4 (scenes 609-618): regression, decision, quiet ending."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
235: ("(We dragged Kirche, who kept calling me 'big brother', back to the inn...)",
      "Мы притащили Кирке, которая всё время звала меня «братишкой», обратно в гостиницу…"),
236: ("(We got back, but...)", "(Мы вернулись, но…)"),
237: ("Infantile regression from hypnotic suggestion, you say?", "Инфантильная регрессия от гипнотического внушения, говоришь?"),
238: ("Yes, most likely.", "Да, скорее всего."),
239: ("It's a combined technique of magic and hypnotic suggestion. Honestly, it's impressive.",
      "Это сложный приём — магия плюс гипнотическое внушение. честно говоря, впечатляет."),
240: ("So Weatherly's group did something to Kirche...", "Значит, группа Уэзерби что-то сделала с Кирке…"),
241: ("Yes, probably.", "Да, наверное."),
242: ("Damn...", "Чёрт…"),
243: ("But why Kirche...", "Но почему Кирке…"),
244: ("Probably a warning.", "Наверное, предупреждение."),
245: ("...", "…"),
246: ("...", "…"),
247: ("...", "…"),
248: ("Ehehe... Big brother, I love youuu...", "Хе-хе… Братишка, я тебя люблюуу…"),
249: ("(Seeing Kirche like this... This is definitely a warning... What should I do...?)",
      "(Видеть Кирке такой… Это точно предупреждение… Что мне делать…?)"),
250: ("Louise, I think we should stop here...", "Луиза, может, нам стоит остановиться…"),
251: ("You're not saying you'd give in to a threat, are you?", "Ты не хочешь сказать, что сдаёшься под угрозой?"),
252: ("Ugh. N-No, I...", "Ох. Я-Я не…"),
253: ("Saito. There are things you must never do.", "Сайто. Есть вещи, которых нельзя делать."),
254: ("Using magic to control someone against their will. That, above all, must never be allowed.",
      "Использовать магию, чтобы управлять человеком против его воли. Вот это нельзя позволять ни в коем случае."),
255: ("Saito, if you don't want to fight, that's fine.", "Сайто, если ты не хочешь сражаться — хорошо."),
256: ("But I will fight. No matter what...", "Но я буду сражаться. Что бы ни было…"),
257: ("I-I understand. I'll fight too, mistress.", "П-Понял. Я тоже буду сражаться, госпожа."),
258: ("That's right, Saito! You can't just stand by when a friend is treated like this!",
      "Вот так, Сайто! Неужели ты можешь спокойно смотреть, как так поступают с другом!"),
259: ("Agreed.", "Согласна."),
260: ("This is a threat, certainly. But giving in and backing off—I can't do that.",
      "Это угроза, без сомнения. Но сдаться и отступить — я не могу."),
261: ("Saito...", "Сайто…"),
262: ("People who do such terrible things... can't be allowed to run rampant.",
      "Таких, кто творит ужасные вещи… нельзя оставлять безнаказанными."),
263: ("Right. I can't forgive them either.", "Верно. Я тоже не могу их простить."),
264: ("Agreed.", "Согласна."),
265: ("(Still, Kirche calling me 'big brother' is kind of cute...)",
      "(И всё же Кирке, называющая меня «братишкой», — это мило…)"),
266: ("(Honestly, the usual Kirche is nice too, but this Kirche is...)",
      "(Честно, обычная Кирке хороша, но эта Кирке…)"),
267: ("Saito! What are you grinning at while looking at Kirche!?",
      "Сайто! Что ты ухмыляешься, глядя на Кирке!?"),
268: ("Eep! I-I'm not grinning at all!", "Ай! Я-Я совсем не ухмыляюсь!"),
269: ("Saito, do you really intend to fight?", "Сайто, ты и правда собираешься сражаться?"),
270: ("O-Of course, mistress!", "К-Конечно, госпожа!"),
271: ("Honestly, really!", "Ну же, хватит!"),
272: ("Kirche's antics are cute, but it's really throwing me off.",
      "Выкрутасы Кирке милые, но меня это здорово сбивает с толку."),
273: ("It's hard to imagine this from the usual Miss Zerbst—so shy and quiet.",
      "Трудно представить такое от обычной мисс Церпст — такой застенчивой и тихой."),
274: ("Ufufu, big brother.", "Уф-фу, братишка."),
275: ("Honestly, why does that stupid dog get to be 'big brother'!!",
      "Ну же, почему этот глупый пёс — вдруг «братишка»!!"),
276: ("Jealous?", "Ревнуешь?"),
277: ("I-I'm not jealous at all!", "Я-Я совсем не ревную!"),
278: ("It may take time, but I'll try to make a medicine.", "Может занять время, но я попробую сделать лекарство."),
279: ("Can you manage it! Montmon!", "У тебя получится! Монмон!"),
280: ("I can't promise anything, though.", "Я ничего не обещаю."),
281: ("Montmon... You really are amazing, you know.", "Монмон… Ты и правда потрясающая."),
282: ("What's that supposed to mean! Honestly!", "Что это значит! Ну же!"),
283: ("More importantly, what will you all do now? Not forgiving them is fine, but our enemy is a huge organization.",
      "Главное — что вы теперь сделаете? Не прощать — это хорошо, но противник — огромная организация."),
284: ("I hate to say it, but you should ask the Queen for help.", "Не хочу это говорить, но вам стоит просить помощи у Королевы."),
285: ("Let me think a little... What are they really planning?", "Дайте мне немного подумать… Что же они задумали?"),
286: ("...", "…"),
287: ("...", "…"),
288: ("(Kirche went quiet—so she was with Tabitha, huh...)", "(Кирке затихла — значит, она была у Табасы… да?)"),
289: ("Kirche, what are you doing with Tabitha?", "Кирке, что ты делаешь с Табасой?"),
290: ("Mm. Tabitha onee-chan is reading me a story.", "Мм. Табаса-онээ-тян читает мне сказку."),
291: ("Mm.", "Мм."),
292: ("Hey, read more stories!", "Ещё сказку!"),
293: ("And so, the prince was able to defeat the dragon.", "И так принц смог победить дракона."),
294: ("Yay! Yay!", "Ура! Ура!"),
295: ("(Tabitha is soothing Kirche—the one who's usually the big sister...)",
      "(Табаса утешает Кирке — ту, что обычно сама старшая…)"),
296: ("Tabitha's actually quite good with kids.", "Табаса и правда хорошо ладит с детьми."),
297: ("Is she?", "Правда?"),
298: ("...?", "…?"),
299: ("Thanks, Tabitha. You saved me.", "Спасибо, Табаса. Ты меня выручила."),
300: ("...?", "…?"),
301: ("Well, ever since Kirche turned like this, she's been glued to me. It's a relief.",
      "Дело в том, что с тех пор, как Кирке стала такой, она не отходит от меня. Это облегчение."),
302: ("...", "…"),
303: ("(What's this feeling in my chest...?)", "(Что это за чувство в груди…?)"),
304: ("(Reading a book with Tabitha like this...)", "(Читать вот так с Табасой…)"),
305: ("B-Big brother is lonely!", "Б-Братишке одиноко!"),
306: ("What's wrong, big brother?", "Что случилось, братишка?"),
307: ("...", "…"),
308: ("N-No, it's nothing...", "Н-Нет, ничего…"),
309: (None, None),
310: ("Hiraga-kun, you're glued to Kirche-san, aren't you?", "Хирага-кун, ты не отходишь от Кирке-сан, да?"),
311: ("Saito-san, do you actually like little girls?", "Сайто-сан, вам и правда нравятся маленькие девочки?"),
312: ("Hiraga-kun, in Japan you were never like this... But maybe you were just hiding it...",
      "Хирага-кун, в Японии ты таким не был… Но, может, ты просто скрывал…"),
313: ("N-Now, now...", "Н-Ну-ну…"),
314: ("Hiraga-kun, even in another world, crime is still wrong.", "Хирага-кун, даже в другом мире преступление остаётся преступлением."),
315: ("Hold on, you two. What do you think I am?", "Подождите вы двое. Что вы обо мне подумали?"),
316: ("...", "…"),
317: ("Big broooother! I'm sleepy...", "Братишшаа! Спать хочется…"),
318: ("H-Hey! Kirche, don't hug me.", "Э-Эй! Кирке, не обнимай меня."),
319: ("Big brother's lap is warmmm. Good niiight...", "У братишки тёплые коленки. Спокойной нооочи…"),
320: ("Ah! A lap pillow! What an attack!", "Ах! Под HEAD-подушку! Какая атака!"),
321: ("I-Is this all right! Miss Valliere!?", "М-Можно ли это! Мисс Вальер!?"),
322: ("I-I don't know!", "Я-Я не знаю!"),
323: ("...Big brother, I love you.", "…Братишка, я тебя люблю."),
324: ("...", "…"),
325: ("(Sigh... What am I supposed to do? At this rate, I won't last...)",
      "(Фух… Что мне делать? Так я долго не продержусь…)"),
}
CHOICES = {
609: [("Give in", "Сдаться"),
      ("Don't give in", "Не сдаваться"),
      ("Kirche is cute...", "Кирке милая…")],
614: [("Watch over them warmly", "Тепло наблюдать за ними"),
      ("Feel a little relieved", "Немного успокоиться"),
      ("Jealous of Tabitha", "Ревновать к Табасе")],
}
SPK = {'サイト': 's', 'モンモランシー': 'm', 'ルイズ': 'l', 'タバサ': 't',
       'キュルケ': 'k', 'シエスタ': 'si', 'ハルナ': 'ha', 'null': 'th'}
START = {'s': 111, 'm': 9, 'l': 28, 't': 5, 'k': 84, 'si': 5, 'ha': 3, 'th': 2}


def main():
    data = json.load(open('reports/ch14/parse_578_619.json', encoding='utf-8'))
    script = ['# Глава 14, часть 4 (сцены 609–618): инфантильная регрессия, решение, тихий финал.',
              '# Источник: ps2_source/chapters/chapter_15_私のお兄ちゃん.txt (SCENE 609-618).',
              '', 'label ch14_4:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 618:
                break
            if x['no'] < 609:
                continue
            scene = x['no']
            script += ['label ch14_4_scene_%d:' % scene, '']
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
            continue
        if k == 'choice':
            if scene is None or scene not in CHOICES:
                continue
            script.append('    menu:')
            for i, o in enumerate(x['options']):
                en, ru = CHOICES[scene][i]
                ctext = '%s{#ch14_4_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch14_4_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 609 <= scene <= 618:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump ch14_4_scene_%d' % x['target'])
            script.append('')
    # Точки входа из move-меню части 3 (extra 1489–1491), пока заглушки.
    script += ['label ch14_4_scene_1489:', '    jump attention', '    return', '',
               'label ch14_4_scene_1490:', '    jump attention', '    return', '',
               'label ch14_4_scene_1491:', '    jump attention', '    return', '']
    script += ['    # ==== КОНЕЦ ГЛАВЫ 14 ====', '    jump ch15', '    return', '']
    files = {
        'game/chapters/14/script-ch14_4.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch14_4_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch14_4_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch14_4_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch14_4_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch14/voice_map_4.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
