#!/usr/bin/env python3
"""Chapter 21 part 3 (scenes 790-805 + 1204-1208): cooking prep, date with Siesta."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
265: ("Well, I'll handle the arrangements for the contest. Look forward to it.",
      "Что ж, я позабочусь о подготовке состязания. Ждите с нетерпением."),
266: ("I know.", "Знаю."),
267: ("Then, Siesta—let's see what you're capable of, shall we?",
      "Тогда, Сиэста — покажи, какова твоя повседневная работа, да?"),
268: ("Understood, Miss Zerbst. Please go easy on me.",
      "Поняла, мисс Церпст. Прошу быть снисходительной."),
269: ("All right, I'll do my best!!", "Отлично, я постараюсь!!"),
270: ("Good grief. I got dragged into something terrible, didn't I...",
      "Ох, ну вот… Я втянулся в жуткую историю, да…"),
271: ("Heh heh! Things are getting interesting, aren't they, partner?",
      "Хи-хи! Дела становятся всё интереснее, приятель?"),
272: ("What's that supposed to mean, Derf? Don't act like it's someone else's problem.",
      "Что это значит, Дерф? Не притворяйся, что это не твоё дело."),
273: ("What's wrong? Let's just watch the show. Still, being popular is a pain, huh.",
      "Что? Давай просто посмотрим. И всё же быть популярным — тяжёлая ноша, да?"),
274: ("It's not my fault, is it?", "Это не моя вина, правда?"),
275: ("Is that so? I'd say your wishy-washy attitude is the cause, though...",
      "Так ли? Я бы сказал, причина — твоя неопределённость…"),
276: ("I can't help it. I'm not from this world. I do want to go back someday...",
      "Ничего не поделать. Я не из этого мира. И когда-нибудь хочу вернуться…"),
277: ("All right, all right. I won't say any more. I just need things to be fun.",
      "Ладно-ладно. Больше не скажу. Мне лишь бы было весело."),
278: ("...", "…"),
279: ("By the way, partner. Who do you think will win?",
      "Кстати, приятель. Кто, по-твоему, победит?"),
280: ("Hmm...", "Хм…"),
281: ("Siesta's the favorite, isn't she? She's used to cooking, being a maid and all.",
      "Сиэста — фаворит, да? Она же привыкла готовить, будучи горничной."),
282: ("Yeah, that's the obvious pick. Not much fun in it, though.",
      "Да, логичный выбор. Только мало веселья."),
283: ("Hey, quit talking about 'fun.' I'm the one who has to eat it, you know. "
      "I'd be in trouble if they made something 'interesting.'",
      "Эй, хватит про «веселье». Я же тот, кто будет это есть. "
      "Будет плохо, если они приготовят что-то «интересное»."),
284: ("Actually, Louise might be a dark horse.", "Вообще-то, Луиза может стать тёмной лошадкой."),
285: ("Hey, partner, are you serious?", "Эй, приятель, ты серьёзно?"),
286: ("She does amazing things when push comes to shove. You never know.",
      "Она способна на удивительное, когда прижмёт. Кто знает?"),
287: ("I see. Well, that'd be the best outcome for you, partner.",
      "Понятно. Ну, для тебя это был бы лучший исход, приятель."),
288: ("Why's that?", "Почему?"),
289: ("If a noble girl cooks something good, fine—but if not... "
      "What do you think she'll come up with?", "Если дворянка приготовит что-то хорошее — ладно, "
      "а если нет… Что, по-твоему, она придумает?"),
290: ("R-Right... Louise, please...", "Т-Точно… Луиза, прошу тебя…"),
291: ("Me.", "Я."),
292: ("Huh? You don't cook, partner.", "А? Ты же не готовишь, приятель."),
293: ("Think about it. I'm the one eating what they make, right? "
      "Siesta's reassuring, sure, but...", "Подумай. Я же буду есть то, что они сделают, да? "
      "Сиэста надёжна, это хорошо, но…"),
294: ("Hang in there, partner.", "Держись, приятель."),
295: ("I'm getting a little worried. Maybe I should go check on them...",
      "Я начинаю немного волноваться. Может, сходить посмотреть…"),
296: ("[Move] Tabitha's room", "[Переход] Комната Табасы"),
297: ("[Move] Courtyard", "[Переход] Двор"),
298: ("[Move] Louise's room", "[Переход] Комната Луизы"),
299: ("[Move] Courtyard", "[Переход] Двор"),
300: ("Ah, I'm exhausted. I think I'll sleep great on a straw bed tonight, too.",
      "Ах, я устал. Кажется, сегодня я отлично высплюсь и на соломенной подстилке."),
301: ("Saito-san, you've worked hard.", "Сайто-сан, вы постарались."),
302: ("Ah, Siesta, you too. Cleaning and laundry from morning, and on top of that "
      "preparing for the cooking contest...", "Ах, Сиэста, это ты постаралась. Уборка и стирка с утра, "
      "да ещё и подготовка к кулинарному бою…"),
303: ("Really, are you all right?", "Правда, ты в порядке?"),
304: ("Yes. Thank you for worrying about me, Saito-san.", "Да. Спасибо, что волнуетесь за меня, Сайто-сан."),
305: ("Honestly... What are those two thinking?", "Честно… Что они задумали?"),
306: ("But it's a little fun, isn't it? Perhaps they're worried because I was down?",
      "Но это немного весело, правда? Может, они беспокоились, потому что я была подавлена?"),
307: ("You're strong, Siesta.", "Ты сильная, Сиэста."),
308: ("Heh heh, I'm not the only one. Girls are much stronger than Saito-san thinks, you know?",
      "Хи-хи, я не одна. Девочки куда сильнее, чем Сайто-сан думает, знаете?"),
309: ("Hmm, I don't really get it.", "Хм, я не совсем понимаю."),
310: ("Heh heh, really, Saito-san.", "Хи-хи, ну же, Сайто-сан."),
311: ("Ha ha ha!", "Ха-ха-ха!"),
312: ("Um... Saito-san.", "Э-Э… Сайто-сан."),
313: ("Hmm?", "Хм?"),
314: ("Um... Could I... sit next to you?", "Э-Э… Можно мне… сесть рядом?"),
315: ("Eh? A-Ah... Sure.", "А? А-А…"),
316: ("Eep... Heh heh, straw is soft, isn't it?", "Ой… Хи-хи, солома мягкая, правда?"),
317: ("(H-Hey... Cuddling up to me is cheating!!)", "Э-Э… Прижиматься — это нечестно!!"),
318: ("I'm back... Wait, hey! What are you two doing, all cuddled up together!?",
      "Я вернулась… Тут, погоди! Что вы двое делаете, прилипли друг к другу!?"),
319: ("Whoa, Louise!!", "Ой, Луиза!!"),
320: ("...Ah! W-Welcome back, Miss Valliere. Haruna-san...",
      "…Ах! Д-Добро пожаловать, мисс Вальер. Харуна-сан…"),
321: ("Just what were you doing! Tell me!", "Что вы только что делали! Говорите!"),
322: ("Siesta, that was awful. Sneaking up on Hiraga-kun like that...",
      "Сиэста, это ужасно. Подкрадываться к Хирага-куну…"),
323: ("N-Nothing! We were just talking!", "Н-Ничего! Мы просто разговаривали!"),
324: ("Talking about what!", "О чём разговаривали!"),
325: ("L-Look, the cooking contest is coming up, right? So we were talking about all sorts—",
      "С-Смотри, же кулинарный бой приближается, да? Мы просто говорили о разном—"),
326: ("Heh heh... You really think that excuse will work?", "Хи-хи… Ты правда думаешь, это сработает?"),
327: ("I-It's true!", "П-Правда!"),
328: ("L-Look, we were talking about how strong girls are! Like Louise and...",
      "С-Смотри, мы говорили о том, какие девочки сильные! Например, Луиза и…"),
329: ("Me, strong? That's rude to a lady!", "Я сильная? Это грубо по отношению к леди!"),
330: ("N-No, I didn't mean it that way!", "Н-Нет, я не это имел в виду!"),
331: ("L-Look, I was saying how surprisingly soft it is!", "С-Смотри, я говорил, какой неожиданно мягкий!"),
332: ("Wh-Wh-What's soft! Did you touch it! You did, didn't you!",
      "Ч-Ч-Что мягкое! Ты трогал! Ты трогал, да!"),
333: ("Nobody said anything like that! I said the straw was soft...",
      "Никто такого не говорил! Я сказал, что солома мягкая…"),
334: ("No questions asked!", "Никаких вопросов!"),
335: ("Louise, punish him!", "Луиза, накажи его!"),
336: ("Geeh!? Wait, wait, Louise!! Not the whip, not the whi—!!",
      "Ги-и!? Погоди, погоди, Луиза!! Не кнут, не кнууу—!!"),
337: ("Hiiih! Help meee~!!", "Хи-и! Помогите~!!"),
338: ("Guh... Giiih... Ugh.", "Гух… Ги-и… Ох."),
339: ("...Ugh, where am I?", "…Ох, где я?"),
340: ("Yo, partner. Finally awake? I thought you'd never wake up.",
      "Йо, приятель. Наконец проснулся? Я уже думал, ты никогда не проснёшься."),
341: ("Hey, Derf. That was the worst way to wake up.", "Йо, Дерф. Худшее пробуждение."),
342: ("So this is a hallway... I guess they dragged me out of the room. My body hurts...",
      "Так, это коридор… Видно, меня вытащили из комнаты. Тело болит…"),
343: ("Well, it couldn't be helped.", "Ну, ничего не поделать."),
344: ("Haaah. What awful luck I have.", "Ааах. Какая же невезучесть."),
345: ("At this rate, Siesta, Haruna, and even Louise are all asleep by now...",
      "Судя по всему, Сиэста, Харуна и даже Луиза уже спят…"),
346: ("Yeah. I got dragged into it as your partner and got kicked out, too.",
      "Да. Я попался как твой напарник, и меня тоже выгнали."),
347: ("Sorry.", "Прости."),
348: ("It's fine, partner.", "Ничего, приятель."),
349: ("Well, I guess I'll go for a walk to clear my head...",
      "Ну, пойду прогуляюсь, проветрюсь…"),
350: ("Even at night, it's deserted and a little eerie, isn't it?",
      "Даже ночью здесь безлюдно и немного жутко, да?"),
351: ("What's wrong, scared of the dark? Don't be silly, you're no child.",
      "Что, боишься темноты? Не смеши, ты не ребёнок."),
352: ("...Allow me to dissuade the enemy. If I return to the Empire, everything will be settled.",
      "…Позвольте мне отговорить врага. Если я вернусь в Империю, всё уладится."),
353: ("...Huh? That voice just now... Siesta?", "…А? Этот голос сейчас… Сиэста?"),
354: ("Aye, that's the village girl's voice, all right. And I've heard those lines before, too.",
      "Да, это голос деревенской девушки, сомнений нет. И эти слова я уже слышал."),
355: ("...But if we go on like this, the prince will lose both his kingdom and his life!",
      "…Но если мы продолжим, принц потеряет и королевство, и жизнь!"),
356: ("Prince, do you remember the night I received your proposal?",
      "Принц, помните ли вы ту ночь, когда я получила ваше предложение?"),
357: ("It was a beautiful twin-moon night, just like tonight. Let me give you my answer now.",
      "Это была прекрасная ночь с двумя лунами, как и сегодня. Позвольте мне сейчас дать ответ."),
358: ("...Siesta.", "…Сиэста."),
359: ("Eep!?", "Ай!?"),
360: ("...Saito-san.", "…Сайто-сан."),
361: ("That was the line from the play we did on stage, wasn't it?",
      "Это была реплика из спектакля, который мы играли, да?"),
362: ("Ah, Saito-san figured it out right away, didn't you. You saw something embarrassing, didn't you~?",
      "Ах, Сайто-сан сразу догадался, да? Вы увидели нечто неловкое~?"),
363: ("It was my first time acting on a stage like that... I was worried I'd mess up.",
      "Я впервые играл на такой сцене… Всё боялся ошибиться."),
364: ("Isn't it! Especially the fear before the curtain rises—",
      "Да! Особенно страх перед поднятием занавеса —"),
365: ("I felt the same. I kept thinking my voice would crack and ruin the mood.",
      "Я чувствовал то же. Всё думал, что голос сорвётся и испортит атмосферу."),
366: ("And I'm not exactly prince material. But Siesta's princess suited you perfectly?",
      "И я совсем не подходил на роль принца. Но Сиэста идеально подошла к роли принцессы, да?"),
367: ("Really? ...Thank you. Ehehe.", "Правда?.. Спасибо. Хи-хи."),
368: ("Ah ha ha... Still, the reception was better than I expected. Thank goodness.",
      "Ах-ха-ха… Всё же отзывы были лучше, чем я ожидал. Слава богу."),
369: ("If I'd said it was terrible, Haruna's bag wouldn't have been returned, either.",
      "Если бы я сказал, что всё было ужасно, сумка Харуны тоже бы не вернулась."),
370: ("Right. It was the fruit of everyone's efforts—something we built together.",
      "Да. Это был плод общих усилий — то, что мы создали все вместе."),
371: ("Yeah. I think it was a really precious experience.", "Да. Я думаю, это был очень ценный опыт."),
372: ("Yes. It became a wonderful memory for me, too.", "Да. И для меня это стало прекрасным воспоминанием."),
373: ("But...", "Но…"),
374: ("Hmm? What's wrong?", "Хм? Что случилось?"),
375: ("The prince and princess... Why did they choose death?", "Принц и принцесса… Почему они выбрали смерть?"),
376: ("Eh?", "А?"),
377: ("I keep thinking there must have been another way...", "Я всё думаю, должен был быть другой выход…"),
378: ("And when I think about it, I feel so very heavy-hearted.",
      "И когда я об этом думаю, на сердце становится так тяжело."),
379: ("What do you think, Saito-san?", "А как считаете вы, Сайто-сан?"),
380: ("Hmm... Let me see. If I were...", "Хм… Подумаем. Если бы я был…"),
381: ("I'd send the princess back to her own country, I suppose...",
      "Я бы отправил принцессу обратно в её страну, наверное…"),
382: ("...Yes. That's right...", "…Да. Верно…"),
383: ("After all, forcing her to abandon the place she was born and raised would be cruel...",
      "В конце концов, заставлять её бросить место, где она родилась и выросла, жестоко…"),
384: ("Saito-san...", "Сайто-сан…"),
385: ("I'd take the princess and run away somewhere... where neither country could find us.",
      "Я бы взял принцессу и убежал куда-нибудь… туда, где нас не найдёт ни одно из королевств."),
386: ("How wonderful. Living together in some small village, just the two of us.",
      "Как прекрасно. Жить вдвоём в какой-нибудь маленькой деревне."),
387: ("Yeah, that's right.", "Да, верно."),
388: ("And we'd tend a small field together, and before long a child would be born... "
      "Saito-san, how many children would you like?", "И вместе обрабатывать маленькое поле, "
      "а со временем родится ребёнок… Сайто-сан, сколько детей вы хотите?"),
389: ("E-Eh!?", "А-А!?"),
390: ("N-No, I'm sorry... I got carried away imagining it...", "Н-Нет, простите… Я невольно представила…"),
391: ("Ha ha ha!", "Ха-ха-ха!"),
392: ("I'd destroy both countries and become king myself.",
      "Я бы уничтожил оба королевства и сам стал королём."),
393: ("Hehe. How heroic.", "Хи-хи. Как героично."),
394: ("I'm kidding. I could never do something like that.",
      "Я шучу. Я бы никогда не смог такого сделать."),
395: ("You could, Saito-san. You can do anything, Saito-san.",
      "Сможете, Сайто-сан. Вы удивительный человек, который может всё, Сайто-сан."),
396: ("R-Really...?", "П-Правда…?"),
397: ("Yes.", "Да."),
398: ("Ha ha, you say it so confidently.", "Ха-ха, ты говоришь так уверенно."),
399: ("If you were the prince, Saito-san—", "Если бы вы были принцем, Сайто-сан—"),
400: ("Stay as kind as you are now, and just grow even stronger, okay? "
      "I'll be cheering you on from the shadows, too.", "Останьтесь таким же добрым, каким вы сейчас, "
      "и просто становитесь всё сильнее, ладно? Я тоже буду поддерживать вас из тени."),
401: ("Yeah. I'll try my best.", "Да. Я постараюсь."),
402: ("If it comes to it, I'll protect everyone with this. Right, Derf—I'm counting on you, partner!",
      "Если дойдёт до дела, я защищу всех вот этим. Верно, Дерф — я на тебя рассчитываю, приятель!"),
403: ("Hah... Don't expect one village girl to be handled by your one arm. Figure it out yourself.",
      "Ха… Ну же, справишься как-нибудь и одной рукой, я тебе говорю! Сам разберись."),
404: ("D-Don't say that! Please, Derflinger-saaan!", "Н-Не говори так! Прошу тебя, Дерфлингер-сааан!"),
405: ("Oh, Saito-san, really! Hehe hehe hehe...", "Ох, Сайто-сан, ну же! Хи-хи-хи-хи…"),
406: ("Ha ha, I can't keep a cool act, can't I...", "Ха-ха, не получается держать важный вид…"),
407: ("Well then, Saito-san. Should we head back soon?", "Ну что ж, Сайто-сан. Не пора ли нам возвращаться?"),
408: ("Ah, we talked until quite late, didn't we. Let's go, then.",
      "Ах, мы заговорились до позднего часа. Что ж, пойдём."),
409: ("Yes, prince.", "Да, принц."),
}
CHOICES = {
791: [("Siesta, the favorite", "Сиэста — фаворит"),
      ("Louise, the dark horse", "Луиза — тёмная лошадка"),
      ("Me", "Я")],
800: [("About the cooking contest", "О кулинарном бое"),
      ("About Louise's strength", "О силе Луизы"),
      ("About how soft the straw is", "О мягкости соломы")],
1204: [("Send the princess home", "Отправить принцессу домой"),
       ("Run away together", "Убежать вместе"),
       ("Destroy both countries", "Уничтожить оба королевства")],
}
SPK = {'サイト': 's', 'キュルケ': 'k', 'ルイズ': 'l', 'シエスタ': 'si', 'ハルナ': 'ha',
       'デルフリンガー': 'd', 'null': 'th'}
START = {'s': 96, 'k': 26, 'l': 55, 'si': 50, 'ha': 10, 'd': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch21/parse_771_805.json', encoding='utf-8'))
    script = ['# Глава 21, часть 3 (сцены 790–805 + 1204–1208): подготовка, свидание с Сиэстой.',
              '# Источник: ps2_source/chapters/chapter_22_サイトのメイド.txt.',
              '', 'label ch21_3:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            n = x['no']
            if not ((790 <= n <= 805) or (1204 <= n <= 1208)):
                continue
            scene = n
            script += ['label ch21_3_scene_%d:' % scene, '']
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
            en = en_norm(en)
            spk = SPK.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch21_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch21_3_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch21_3_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None:
                continue
            if not ((790 <= scene <= 805) or (1204 <= scene <= 1208)):
                continue
            t = x['target']
            script.append('    # → next scene %d' % t)
            if 790 <= t <= 805 or 1204 <= t <= 1208:
                script.append('    jump ch21_3_scene_%d' % t)
            elif 1493 <= t <= 1512:
                script.append('    # date event → ch21_4 (extra)')
                script.append('    jump ch21_4')
            else:
                script.append('    jump ch22')
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 3 ====', '    jump ch21_4', '    return', '']
    files = {
        'game/chapters/21/script-ch21_3.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch21_3_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch21_3_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch21_3_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch21_3_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch21/voice_map_3.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
