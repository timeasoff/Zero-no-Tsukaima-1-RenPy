#!/usr/bin/env python3
"""Chapter 15 part 3 (scenes 643-653): the medicine, Kirche returns."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
251: ("Even so, we have no choice but to do it, huh.", "Всё равно, похоже, придётся."),
252: ("Right. We don't have time to wait for Kirche to recover.",
      "Да. У нас нет времени ждать, пока Кирке поправится."),
253: ("So it all comes down to you. You'd better protect her properly.",
      "Значит, всё зависит от тебя. Ты должен её уберечь."),
254: ("Heh, leave it to me. I'm Louise's familiar. I'll guard you until the chanting is done.",
      "Хе, доверься мне. Я фамильяр Луизы. Я буду охранять тебя, пока не закончится заклинание."),
255: ("That's the spirit, partner!", "Вот дух, приятель!"),
256: ("Say... maybe we shouldn't use Void after all?", "Слушай… может, нам всё-таки не стоит применять Пустоту?"),
257: ("It's too dangerous, I think.", "Кажется, это слишком опасно."),
258: ("How many times do I have to tell you Void magic isn't just one thing?",
      "Сколько раз тебе повторять, что магия Пустоты — не одна?"),
259: ("Please, trust me for now... If you believe, it becomes strength.",
      "Прошу, пока доверься мне… Если веришь, это становится силой."),
260: ("Can't Guiche take Kirche's place... no, right?", "Может, Гиш заменит Кирке… нет, да?"),
261: ("Are you serious?", "Ты серьёзно?"),
262: ("Yeah, I thought so. I knew it.", "Да, я так и знал."),
263: ("Anyway, I trust you, Louise. I'll definitely protect you. So go ahead and unleash Void!",
      "В любом случае, я доверяю тебе, Луиза. Я обязательно тебя защищу. Так что спокойно применяй Пустоту!"),
264: ("But, partner—even if you've decided to believe...", "Но, приятель, даже если ты решил верить…"),
265: ("Buying time until Louise's Void chant finishes is going to be tough, huh.",
      "Держать оборону, пока Луиза читает Пустоту, будет непросто, да."),
266: ("If Louise is out of it, the main force will be just me and Tabitha.",
      "Если Луиза выбывает, основные силы — это я и Табаса."),
267: ("If only Kirche could make it in time...", "Хоть бы Кирке успела…"),
268: ("What's wrong, big brother? Is Kirche being a burden?", "Что случилось, братишка? Кирке мешает?"),
269: ("N-Nothing! Don't be scared.", "Н-Ничего! Не пугайся."),
270: ("My, what's with these long faces?", "Ой, почему у всех такие хмурые лица?"),
271: ("Ah, Montmon! How much longer for Kirche's medicine?",
      "А, Монмон! Сколько ещё ждать лекарство для Кирке?"),
272: ("It's done... more or less.", "Готово… в целом."),
273: ("Heh? Really?", "А? Правда?"),
274: ("What, you doubt me? After rushing me so hard.",
      "Что, сомневаешься? После того как так подгоняла."),
275: ("I don't doubt you, I don't! All right!!", "Не сомневаюсь, не сомневаюсь! Ура!!"),
276: ("I also prepared medicine and a spell against Weatherly's suggestion. We'll use it later.",
      "Я также подготовила лекарство и заклинание против внушения Уэзерби. Применим позже."),
277: ("All right, Kirche... here, take this medicine...", "Ладно, Кирке… вот, выпей лекарство…"),
278: ("U-Um. Do I really have to drink it?", "Э-Э. Правда надо пить?"),
279: ("You see, big brother... Kirche doesn't like medicine...",
      "Понимаешь, братишка… Кирке не любит лекарства…"),
280: ("Bitter medicine... no.", "Горькое лекарство… не хочу."),
281: ("Come on, Kirche. Don't be difficult...", "Ну же, Кирке. Не капризничай…"),
282: ("It's not bitter, not bitter!", "Оно не горькое, не горькое!"),
283: ("Really, big brother?", "Правда, братишка?"),
284: ("It has akagusa fruit in it, so it'll be pretty bitter. That stuff is too bitter to eat raw.",
      "Там есть плод акагуса, так что будет довольно горьким. Он такой горький, что сырым его не едят."),
285: ("Then abso-lutely no!", "Тогда ни-ко-гда не буду!"),
286: ("Montmon! Don't interfere!", "Монмон! Не мешай!"),
287: ("Bitter medicine... no.", "Горькое лекарство… не хочу."),
288: ("What'll it take to get you to drink it?", "Как тебя уговорить выпить?"),
289: ("Right. Here, Kirche—", "Придумал. Слушай, Кирке—"),
290: ("If you drink this, I'll hold you afterwards!", "Если выпьешь, я потом поношу тебя на руках!"),
291: ("Really?", "Правда?"),
292: ("No! Absolutely not!", "Нет! Ни в коем случае!"),
293: ("Hey now, Louise!", "Эй, Луиза!"),
294: ("Ah... I spoke too soon.", "А… я слишком поспешила."),
295: ("You won't hold me? Then I absolutely won't drink it!", "Не понесешь? Тогда я точно не буду пить!"),
296: ("If it comes to this!", "Раз так —!"),
297: ("I'll take responsibility.", "Я беру ответственность на себя."),
298: ("Responsibility... what are you planning?", "Ответственность… что ты задумал?"),
299: ("Damn, what a handful!", "Чёрт, ну и хлопотная!"),
300: ("W-Wait, Saito! What are you doing drinking it—!?", "П-Подожди, Сайто! Что ты делаешь, это же пить…!?"),
301: ("A-Aaaaaah!", "А-Ааааа!"),
302: ("...", "…"),
303: ("...", "…"),
304: ("B-Big brother...", "Б-Братишка…"),
305: ("W-What are you doing, stupid dog!", "Ч-Что ты делаешь, глупый пёс!"),
306: ("D-Don't get the wrong idea! I just fed it to her mouth-to-mouth!",
      "Н-Не подумай ничего такого! Я просто скормил ей с губ на губы!"),
307: ("My mouth tastes bitter...!", "У меня во рту горько…!"),
308: ("Hic! Huh?", "Ик! А?"),
309: ("Honestly! What a handful!", "Ну же! Ну и хлопотная!"),
310: ("Here! Drink it, Kirche!", "Ну же! Пей, Кирке!"),
311: ("Drink it already—!", "Пей же —!"),
312: ("Noooo! ...Gulp.", "Нееет! …Глоток."),
313: ("T-Touche, Louise! That's too rough!", "Т-Ты чего, Луиза! Это слишком грубо!"),
314: ("...", "…"),
315: ("L-Louise onee-chan... that was mean.", "Л-Луиза-онээ-тян… это было плохо."),
316: ("M-My mouth is bitter...!", "У меня во рту горько…!"),
317: ("...Hic! Huh?", "…Ик! А?"),
318: ("W-What was that!?", "Ч-Что это было!?"),
319: ("It's starting to work.", "Оно начинает действовать."),
320: ("Huh huh huh huh huh?", "А? А? А?"),
321: ("Darling...? Louise...? What was I doing?", "Дорогой…? Луиза…? Что я делала?"),
322: ("Thank goodness! Kirche's back! Now we can win!", "Слава богу! Кирке вернулась! Теперь мы победим!"),
323: ("What's going on? What's this explosion? What happened?",
      "Что происходит? Что это за взрыв? Что случилось?"),
324: ("Explanations later! Montmon, the anti-suggestion thing, please!",
      "Объяснения потом! Монмон, средство против внушения, давай!"),
325: ("Right, here I go.", "Да, я начала."),
327: ("Ugh, my head is still spinning.", "Ох, у меня ещё крутится голова."),
328: ("You okay, Kirche...?", "Ты в порядке, Кирке…?"),
329: ("Yes, darling. Just a little dizzy...", "Да, дорогой. Немного головокружение…"),
330: ("You're too close! Both of you, step back!", "Вы слишком близко! Оба отойдите!"),
331: ("I'm still recovering. Be a little gentler with me.", "Я же ещё болею. Пощадите меня немного."),
332: ("Urgent message for Louise Francoise! Reconquista warships have entered "
      "Tristain's defense zone!",
      "Срочное сообщение для Луизы Франсуазы! Военные корабли Реконкисты вошли в зону обороны Тристании!"),
333: ("Reports also say part of the enemy force is descending, aiming to seize the palace.",
      "Также есть сообщения, что часть вражеских сил высаживается, намереваясь захватить дворец."),
334: ("What!?", "Что!?"),
335: ("So it's finally here, huh.", "Значит, это наконец началось."),
336: ("Damn, we wrote them off as mere actors... It was all a play... Weatherly.",
      "Чёрт, мы принимали их за просто актёров… Всё было спектаклем… Уэзерби."),
337: ("Hypnosis... actors... a play... Right.", "Гипноз… актёры… спектакль… Верно."),
338: ("Fine. I'll make that Weatherly regret this.", "Ладно. Я покажу этой Уэзерби, как надо."),
}
CHOICES = {
646: [("Don't be a brat...", "Не капризничай…"),
      ("...What should I do", "…Что мне делать"),
      ("If it comes to this!", "Раз так —!")],
}
SPK = {'サイト': 's', 'ルイズ': 'l', 'デルフリンガー': 'd', 'キュルケ': 'k',
       'モンモランシー': 'm', '味方Ａ': 'soldier', 'ギーシュ': 'g', 'null': 'th'}
START = {'s': 72, 'l': 64, 'd': 2, 'k': 19, 'm': 7, 'soldier': 8, 'g': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch15/parse_619_659.json', encoding='utf-8'))
    script = ['# Глава 15, часть 3 (сцены 643–653): лекарство, возвращение Кирке.',
              '# Источник: ps2_source/chapters/chapter_16_魔法の薬.txt (SCENE 643-653).',
              '', 'label ch15_3:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 653:
                break
            if x['no'] < 643:
                continue
            scene = x['no']
            script += ['label ch15_3_scene_%d:' % scene, '']
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
            if idx == 279:
                script.append('    menu:')
                for i, (en_m, ru_m) in enumerate(CHOICES[646]):
                    ctext = '%s{#ch15_3_c_646_%d}' % (en_norm(en_m), i + 1)
                    script.append('        "%s":' % ctext)
                    script.append('            jump ch15_3_scene_%d' % (648 + i))
                    ja_c += ['    old "%s"' % ctext,
                             '    new "%s"' % ('ワガママをいわないで……', '……ど、どうしよう', 'こうなったら！')[i], '']
                    ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru_m, '']
                script.append('')
            continue
        if k == 'choice':
            continue
        if k == 'goto':
            if scene is None or not 643 <= scene <= 653:
                continue
            if x['target'] == 652:
                script.append('    # → next scene 652 (альтернативная ветка — пропущена)')
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch15_3_scene_%d' % x['target']
                                          if 643 <= x['target'] <= 653 else 'ch15_4'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 3 ====', '    jump ch15_4', '    return', '']
    files = {
        'game/chapters/15/script-ch15_3.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch15_3_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch15_3_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch15_3_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch15_3_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch15/voice_map_3.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
