#!/usr/bin/env python3
"""Chapter 25 part 3 (scene 933 + extra 1214-1218): the letter's secret, stargazing."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
252: ("Saito. You certainly had your fun today, didn't you?", "Сайто. Похоже, ты сегодня хорошо провёл время, да?"),
253: ("Why are you sulking? Right, Siesta?", "Почему ты дуешься? Верно, Сиэста?"),
254: ("I don't know...", "Не знаю…"),
255: ("Eh? Even you, Siesta?", "А? Даже ты, Сиэста?"),
256: ("Hiraga-kun today was the worst...", "Хирага-кун сегодня был просто ужасен…"),
257: ("So why are you sulking too, Haruna?", "Так почему и ты дуешься, Харуна?"),
258: ("It's fine. I'm not in a bad mood, darling.", "Всё хорошо. Я не в дурном настроении, дорогой."),
259: ("Kirche!", "Кирке!"),
260: ("Well, when you watch the man you like being popular, it makes you proud—or makes you burn with jealousy.",
     "Дело в том, когда видишь, что любимый тобой мужчина пользуется успехом, то гордеешься, то, наоборот, ревнуешь."),
261: ("Hmm? Am I really that popular, according to you?", "Хм? Неужто я и правда такой популярный, по-твоему?"),
262: ("...!?", "…!?"),
263: ("You see...", "Видишь ли…"),
264: ("...Hiraga-kun.", "…Хирага-кун."),
265: ("...N-No. More importantly, let's eat, eat...", "…Н-Нет. Главное — есть, есть…"),
266: ("Come to think of it, Tabitha's been quiet for a while, too...", "Кстати, Табаса тоже уже давно молчит…"),
267: ("...", "…"),
268: ("Ah, Tabitha-san has fallen asleep...", "Ах, Табаса-сан уснула…"),
269: ("Heh heh, falling asleep during a meal... She must have been quite nervous today, too.",
     "Хи-хи, уснуть во время еды… Похоже, сегодня она волновалась, да?"),
270: ("...Mm.", "…Мм."),
271: ("Heh. Miss Zerbst is like Miss Tabitha's older sister, isn't she?",
     "Хи. Мисс Церпст словно старшая сестра мисс Табасы, да?"),
272: ("Well, we've known each other a long time.", "Ну, мы давно знакомы."),
273: ("Still, sleeping here will give her a cold. I'll take her to the inn once.",
     "Но если она тут уснёт, простудится. Отведу её обратно в гостиницу."),
274: ("Ah, please do.", "Ах, пожалуйста."),
275: ("Come on, Tabitha. Let's go back to the inn. Wake up.", "Ну же, Табаса. Идём в гостиницу. Проснись."),
276: ("...", "…"),
277: ("See you then.", "До встречи."),
278: ("...... ... ...", "……… … …"),
279: ("Oh? It looks like Tabitha-san dropped something.", "Ох? Кажется, Табаса-сан что-то уронила."),
280: ("That letter, I bet.", "Спорим, это то письмо."),
281: ("Phew, Tabitha must be exhausted. She's sleeping soundly. Wait—what's with all of you?",
     "Фух, похоже, Табаса здорово устала. Спит крепко. Погоди — что вы все?"),
282: ("T-This is Tabitha's letter... right?", "Т-Это письмо Табасы… да?"),
283: ("Oh, she dropped it? What a careless girl.", "О, она его уронила? Какая же она рассеянная."),
284: ("W-What should we do? Maybe we should return it right away...", "Ч-Что нам делать? В конце концов, лучше сразу вернуть…"),
285: ("Shall we take a look?", "Посмотрим?"),
286: ("Eh!?", "А!?"),
287: ("Tabitha never asks anyone for help, does she? So we have to help her, right?",
     "Табаса никогда ни к кому не обращается за помощью, да? Значит, мы должны ей помочь, верно?"),
288: ("So you want to look at the letter without telling her?", "То есть ты хочешь посмотреть письмо, не говоря ей?"),
289: ("Oh, not interested? Then I'll take a peek by myself.", "О, не хочешь? Тогда я одна посмотрю."),
290: ("Fine. We'll all apologize later for reading it without permission. Let's look.",
     "Ладно. Потом все вместе извинимся, что прочли без спроса. Давайте посмотрим."),
291: ("As expected of darling. So understanding. Then I'll read it on everyone's behalf.",
     "Как и подобает дорогому. Такой понятливый. Тогда я прочту от лица всех."),
292: ("Hmm hmm...", "Хм-хм…"),
293: ("...", "…"),
294: ("What's wrong, Kirche?", "Что случилось, Кирке?"),
295: ("I figured it was something to do with a mission, and therefore serious... but...",
     "Я думала, это связано с заданием и потому довольно серьёзное… но…"),
296: ("A mission? You thought?", "Задание? Ты думала?"),
297: ("This is going to be troublesome.", "Похоже, это будет хлопотно, да?"),
298: ("So, what is it!?", "Так что это!?"),
299: ("Do you know Tabitha's from the Kingdom of Gallia?", "Ты знаешь, что Табаса из королевства Галлия?"),
300: ("I know that much, but...", "Это я знаю, но…"),
301: ("Well, I'll skip the details. Tabitha gets missions from Gallia from time to time.",
     "Ну, пропущу подробности. Табасе время от времени дают задания из Галлии."),
302: ("This one is from Gallia, too—'capture a certain person and bring them to Gallia'—",
     "Это тоже из Галлии — «захватить определённое лицо и доставить его в Галлию» —"),
303: ("...that seems to be the mission.", "…похоже, это и есть задание."),
304: ("Well, it certainly doesn't sound like an easy one.", "Ну, судя по этому, задание не из лёгких."),
305: ("That depends on who they want captured, doesn't it?", "Это зависит от того, кого надо захватить, да?"),
306: ("There are people who are easy to catch, you know. If you prepared a girl with a big chest, "
      "a dog would come wagging its tail right away.", "Есть и такие, кого легко поймать, знаешь. "
      "Стоит подготовить девушку с большой грудью — и пёс сразу прибежит, виляя хвостом."),
307: ("M-Mistress... I sense something hurtful in that...", "Г-Госпожа… Мне кажется, тут есть нечто колючее…"),
308: ("Really? Maybe you're imagining it?", "Правда? Может, тебе показалось?"),
309: ("Sniff...", "Хлюп…"),
310: ("So, who is the person to be captured?", "Так, кого именно надо захватить?"),
311: ("Haruna. It's you.", "Харуна. Это ты."),
312: ("Eh?", "А?"),
313: ("No way?", "Не может быть?"),
314: ("That's...", "Это…"),
315: ("Seriously?", "Правда?"),
316: ("...", "…"),
317: ("Say, Haruna. Did you do something that Tabitha would need to bring you in for?",
     "Слушай, Харуна. Ты сделала что-то, из-за чего Табаса должна тебя доставить?"),
318: ("I... don't know. Why would I...", "Я… не знаю. Почему я…"),
319: ("But I understand how confused Tabitha must feel. To be told something like that suddenly...",
     "Но я понимаю, как растерялась Табаса. Так внезапно сказать…"),
320: ("(Walking through town together today was—an escape from reality, I suppose...)",
     "Прогулка по городу сегодня была — бегством от реальности, наверное…"),
321: ("Yes... It's not something we could ask others about, is it...?", "Да… Об этом нельзя было спросить у других, да…?"),
322: ("What will become of me...", "Что со мной будет…"),
323: ("...", "…"),
324: ("Hmm. For now...", "Хм. Пока что…"),
325: ("For now what?", "Пока — что?"),
326: ("I didn't read the letter, and none of you heard anything. Right?",
     "Я не читала письмо, и вы ничего не слышали. Верно?"),
327: ("R-Right. We didn't read it, and we didn't hear anything. That's how it is, right?",
     "В-Верно. Мы не читали и не слышали. Так и есть, да?"),
328: ("Haruna must be worried, too. Don't worry too much, okay?", "Харуна, наверное, тоже волнуется. "
     "Не переживай слишком, ладно?"),
329: ("But...", "Но…"),
330: ("It'll be fine. No matter that it's a mission—Tabitha would never capture Haruna, would she?",
     "Всё будет хорошо. Даже если это задание — Табаса же никогда не схватит Харуну, да?"),
331: ("M-Mm...", "М-Мм…"),
332: ("...", "…"),
333: ("(Even as I said it... What on earth is going on? Why would Gallia want Haruna...?)",
     "Хотя я это сказал… Что же происходит? Зачем Галлии Харуна…?"),
334: ("(Tabitha must be worrying a lot, too... I want to help somehow...)",
     "Табаса, наверное, тоже очень переживает… Хочу чем-нибудь помочь…"),
335: ("Good grief. We've gotten ourselves into something complicated...", "Боже мой. Мы ввязались в сложную историю…"),
336: ("That's... Tabitha, is it?", "Это… Табаса?"),
337: ("...", "…"),
338: ("Tabitha, are you awake? You fell asleep during the meal, so I got a scare.",
     "Табаса, ты проснулась? Ты уснула за едой, и я испугался."),
339: ("...", "…"),
340: ("They say you were tired. Sorry I couldn't notice sooner...", "Говорят, ты устала. Прости, что не заметил раньше…"),
341: ("...", "…"),
342: ("So, what were you doing? Watching the night sky, perhaps?", "Так, что ты делала? Может, смотрела на ночное небо?"),
343: ("Mm.", "Мм."),
344: ("I've been curious for a while... Does this world have constellations, too?",
     "Мне уже давно интересно… Есть ли и в этом мире созвездия?"),
345: ("Constellations?", "Созвездия?"),
346: ("Constellations are—you connect bright stars with lines and make them into people, animals, objects and so on.",
     "Созвездия — это когда яркие звёзды соединяют линиями и видят в них людей, животных, предметы."),
347: ("Connect with lines... Shapes...", "Соединить линиями… Фигуры…"),
348: ("No good. It doesn't make a shape.", "Не выходит. Не получается фигура."),
349: ("It's not about real shapes. You draw two lines and go 'a puppy!'—or a diamond and go 'a crow!'—that sort of thing.",
     "Дело не в настоящих фигурах. Проведёшь две линии и скажешь «щенок!» или ромб и скажешь "
     "«ворона!» — что-то в этом роде."),
350: ("...Weird. What are constellations for?", "…Странно. Зачем нужны созвездия?"),
351: ("What for... Well, let me see...", "Зачем… Ну, подумаем…"),
352: ("Maybe they used them as landmarks while traveling.", "Может, они служили ориентирами в путешествиях."),
353: ("Landmarks?", "Ориентиры?"),
354: ("Yes, landmarks. Constellations are visible or not depending on where you are.",
     "Да, ориентиры. Созвездия видно или не видно в зависимости от места."),
355: ("So if a particular constellation was visible or not, they could use it to work out where they were.",
     "Так что по тому, видно конкретное созвездие или нет, можно было определить своё местоположение."),
356: ("Interesting.", "Интересно."),
357: ("They're used for fortune-telling.", "Их используют для гадания."),
358: ("Fortune-telling?", "Гадание?"),
359: ("I don't really get how it works, but the stars move—so they tell fortunes from their movements, I think.",
     "Я не совсем понимаю, как это работает, но звёзды движутся — и, кажется, гадают по их движению."),
360: ("What do they tell with stars?", "Что гадают по звёздам?"),
361: ("All sorts of things. Love, work—anything about life, really.", "Всякое. Любовь, работа — да что угодно в жизни."),
362: ("Too much reliance.", "Слишком большая опора."),
363: ("Ha ha, maybe so.", "Ха-ха, может, и так."),
364: ("To tell the time, and such.", "Чтобы узнать время и тому подобное."),
365: ("The time?", "Время?"),
366: ("You can more or less tell from the position of a particular constellation. The season, too, probably.",
     "Примерно можно определить по положению определённого созвездия. И время года, наверное."),
367: ("The season?", "Время года?"),
368: ("I don't know about here, but where I come from, the visible constellations change with the season.",
     "Не знаю, как здесь, а у меня дома видимые созвездия меняются в зависимости от времени года."),
369: ("Strange.", "Странно."),
370: ("That aside...", "Впрочем…"),
371: ("Mm.", "Мм."),
372: ("Just looking up at a night sky I don't recognize at all tells me this isn't my world...",
     "Уже одного взгляда на совершенно незнакомое ночное небо достаточно, чтобы понять: это не мой мир…"),
373: ("Though two moons would give it away at a glance, too.", "Хотя две луны выдают это с первого взгляда."),
374: ("Are you lonely?", "Тебе одиноко?"),
375: ("Eh? N-No, I... That's not it...", "А? Н-Нет, я… Дело не в этом…"),
376: ("I see.", "Понятно."),
377: ("Ha ha, ha ha ha...", "Ха-ха, ха-ха-ха…"),
378: ("(Maybe she was trying to comfort me just now?)", "Может, она сейчас пыталась меня утешить?"),
379: ("Next time...", "В следующий раз…"),
380: ("U-Uh?", "А-А?"),
381: ("Tell me more stories.", "Расскажи мне."),
382: ("Ah, sure. If you want my stories, I can tell you as many as you like.",
     "Ах, конечно. Если тебе нужны мои истории, я могу рассказать сколько угодно."),
383: ("Mm.", "Мм."),
}
CHOICES = {
1214: [("As landmarks for travel", "Как ориентиры в пути"),
       ("For fortune-telling", "Для гадания"),
       ("To tell the time", "Чтобы узнать время")],
}
SPK = {'ルイズ': 'l', 'サイト': 's', 'シエスタ': 'si', 'ハルナ': 'ha',
       'キュルケ': 'k', 'タバサ': 't', 'null': 'th'}
START = {'l': 42, 's': 113, 'si': 7, 'ha': 7, 'k': 25, 't': 52, 'th': 5}


def main():
    data = json.load(open('reports/ch25/parse_903_933.json', encoding='utf-8'))
    script = ['# Глава 25, часть 3 (933 + extra 1214–1218): секрет письма, звёзды.',
              '# Источник: ps2_source/chapters/chapter_26_手紙の秘密.txt (SCENE 933, 1214-1218).',
              '', 'label ch25_3:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            n = x['no']
            active = (n == 933) or (1214 <= n <= 1218)
            if not active:
                scene = None
                continue
            scene = n
            script += ['label ch25_3_scene_%d:' % scene, '']
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
            tag = 'ch25_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch25_3_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch25_3_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None: continue
            active = (scene == 933) or (1214 <= scene <= 1218)
            if not active: continue
            t = x['target']
            script.append('    # → next scene %d' % t)
            if (t == 933) or (1214 <= t <= 1218):
                script.append('    jump ch25_3_scene_%d' % t)
            elif 1513 <= t <= 1532:
                script.append('    jump ch25_4')
            else:
                script.append('    jump ch26')
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 3 ====', '    jump ch25_4', '    return', '']
    files = {
        'game/chapters/25/script-ch25_3.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch25_3_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch25_3_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch25_3_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch25_3_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch25/voice_map_3.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
