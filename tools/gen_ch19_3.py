#!/usr/bin/env python3
"""Chapter 19 part 3 (scenes 764-768): Weatherly's past, aftermath, ending."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
260: ("I'm surprised. That you made it this far...", "Удивлена. Что вы дошли так далеко…"),
261: ("If you're surprised, I'm more surprised. That you were the enemy, Weatherly.",
      "Если ты удивлена, то я ещё больше. Что ты оказалась врагом, Уэзерби."),
262: ("Well, things were going well up to here. Everything was going according to script...",
      "Ну, до сюда всё шло хорошо. Всё шло по сценарию…"),
263: ("...", "…"),
264: ("Tabitha... The spell seems to have worn off. Was it too shallow, I wonder?",
      "Табаса… Похоже, заклинание спало. Интересно, оно было слишком слабым?"),
265: ("Weatherly, won't you surrender here? I don't want to hurt you—or Haruna.",
      "Уэзерби, не сдашься ли ты здесь? Я не хочу обижать тебя — и Харуну."),
266: ("This one dares to mock Weatherly-sama!", "Как он смеёт насмехаться над Уэзерби-сама!"),
267: ("I see. That fleet seems to be the work of Louise and Saito. We underestimated your strength.",
      "Понятно. Этот флот — дело рук Луизы и Сайто. Мы недооценили вашу силу."),
268: ("Weatherly-sama, we still have hostages and bombs. We could even detonate them...",
      "Уэзерби-сама, у нас ещё есть заложники и бомбы. Мы можем даже взорвать их…"),
269: ("Stop it, Akina. We'd be caught in the explosion too, along with our allies.",
      "Прекрати, Акина. Мы сами пострадаем от взрыва — и союзники тоже."),
270: ("Weatherly-sama...", "Уэзерби-сама…"),
271: ("I'll just use my magic. Just watch.", "Я просто применю свою магию. Смотри."),
272: ("What! Why isn't it working?", "Что! Почему не срабатывает?"),
273: ("We've already countered that magic. Look—these.", "Ответ на неё уже найден. Смотри — эти."),
274: ("W-What... Earplugs!? No, no way...!", "Ч-Что… Беруши!? Не, не может быть…!"),
275: ("Weatherly. Your magic controls people through sound they can't hear, doesn't it?",
      "Уэзерби. Твоя магия управляет людьми звуком, который они не слышат, верно?"),
276: ("But these earplugs have a wind spell that cancels it. In other words, we can resist it.",
      "Но на этих берушах есть заклинание ветра, которое её нейтрализует. "
      "Иными словами, мы можем противостоять ей."),
277: ("Ugh, lies... Lies! This magic is special—only my family can use it.",
      "Ох, ложь… Ложь! Эта магия особенная — её может применять только мой род."),
278: ("There's no way its mechanism could be known so easily!!",
      "Не может быть, что её устройство так легко раскрыли!!"),
279: ("Ah, it was I who deciphered it.", "Ах, это я её расшифровал."),
280: ("N-No... But you were confined in the headmaster's office the whole time...",
      "Н-Нет… Но ты всё это время был заперт в кабинете директора…"),
281: ("You shouldn't underestimate my Mortosgnir.", "Не стоит недооценивать моего Мортогнира."),
282: ("At full strength, he could round-trip to the capital in a day—not just the academy.",
      "В полной форме он за день сходит туда и обратно не только до академии, "
      "но и до столицы."),
283: ("Conveniently, this academy has people studying all sorts of magic.",
      "Кстати, в этой академии есть люди, изучающие самые разные заклинания."),
284: ("I put him in touch with one, and he worked out a countermeasure in one go.",
      "Я связал его с одним из них — и тот разработал средство с первого раза."),
285: ("Well, your mistake was letting me hear that incantation.",
      "Ну, твоя ошибка в том, что ты дала мне услышать это заклинание."),
286: ("No, no, you're still young—still young. Ho ho ho ho.", "Нет-нет, ты ещё молод — молод. Хо-хо-хо-хо."),
287: ("Is this the end? Is this the end? No—I can't just slink away like this. My... my...",
      "Конец? Конец? Нет — я не могу просто так уйти. Моя… моя…"),
288: ("Akina, don't leave my side! If it comes to it, I'll take down Old Osmond and Gandalfr!",
      "Акина, не отходи от меня! Если придётся, я убью старика Османа и Гандальфа!"),
289: ("Here I come, Gandalfr! Receive the fangs and claws of my resentment and rage!",
      "Иду, Гандальф! Прими клыки и когти моей обиды и гнева!"),
290: ("I'll follow you anywhere, Weatherly-sama!", "Я последую за тобой куда угодно, Уэзерби-сама!"),
291: ("So we have to fight after all, huh.", "Значит, всё-таки придётся драться, да."),
292: ("They're coming.", "Они идут."),
293: ("Come now, kill me. I'm a member of Reconquista now. I won't live in disgrace.",
      "Ну же, убивай. Теперь я член Реконкисты. Я не хочу жить в позоре."),
294: ("No, Weatherly-sama! What about the village's restoration? Your honor?",
      "Нет, Уэзерби-сама! А восстановление деревни? А ваша честь?"),
295: ("Homeland? Honor?", "Родина? Честь?"),
296: ("Stop it, Akina.", "Прекрати, Акина."),
297: ("No! I may be a fleeting life, but you created me, Weatherly-sama.",
      "Нет! Я могу быть мимолётной жизнью, но ты меня создала, Уэзерби-сама."),
298: ("So if it saves your life, I'd do anything...", "Так что если это спасёт твою жизнь, я сделаю что угодно…"),
299: ("There seems to be more to this. Well, won't you tell us? I won't do you any harm.",
      "Похоже, тут есть свои обстоятельства. Ну, не расскажете ли? Я не причиню вам вреда."),
300: ("Weatherly-sama never cared about Reconquista's ideals or reforming the world.",
      "Уэзерби-сама никогда не заботилась об идеалах Реконкисты или переменах в мире."),
301: ("She just wanted to live quietly in her home village with its people. That alone made her happy.",
      "Она просто хотела тихо жить в родной деревне с её людьми. Этого ей было достаточно для счастья."),
302: ("And that was taken away...", "И это у неё отняли…"),
303: ("One day, Tristain stripped her of her noble status and took the village away.",
      "Однажды Тристания лишила её дворянского титула и отобрала деревню."),
304: ("Reconquista promised to restore her status and her village to the depressed Weatherly. "
      "So she had no choice but to...", "Реконкиста пообещала опечаленной Уэзерби вернуть титул "
      "и деревню. Поэтому ей пришлось…"),
305: ("...", "…"),
306: ("So you took revenge on Tristain because you had no choice, is that it?",
      "Так ты отомстила Тристании, потому что не было выбора, да?"),
307: ("My father was a noble, my mother a beast-person. Father lost his noble status "
      "for marrying her, and we were driven from our manor and lands.",
      "Отец был дворянином, мать — зверочеловеком. Отец лишился дворянства из-за "
      "брака с ней, и нас изгнали из поместья и земель."),
308: ("I can never forgive Tristain for that.", "Я никогда не смогу простить Тристании это."),
309: ("Really?", "Правда?"),
310: ("What do you mean, 'really'?", "Что значит «правда»?"),
311: ("I'm saying you're mistaken.", "Я говорю, что ты заблуждаешься."),
312: ("It's true that beast-people are reviled and suffer unjust discrimination. "
      "That much is fact.", "Верно, что зверолюдей порицают и они терпят "
      "несправедливую дискриминацию. Это правда."),
313: ("But... the reason you lost your noble status was almost certainly your magic.",
      "Но… причиной утраты твоего дворянского титула почти наверняка стала твоя магия."),
314: ("Forbidden magic.", "Запретная магия."),
315: ("Yes... Touching forbidden magic is a grave sin in itself.",
      "Да… Само прикосновение к запретной магии — уже тяжкий грех."),
316: ("Probably, though. Your parents didn't tell you the truth because they wanted "
      "you to forget the forbidden magic.", "Наверное. Твои родители не сказали тебе правду, "
      "потому что хотели, чтобы ты забыла запретную магию."),
317: ("I see. The magic I learned—it is indeed forbidden magic that controls the heart.",
      "Понятно. Магия, которую я выучила, — и правда запретная магия, "
      "управляющая сердцами."),
318: ("Weatherly-sama...", "Уэзерби-сама…"),
319: ("I don't intend to beg for my life now. But, Saito, there are times when a person "
      "must fight for honor.", "Я не собираюсь сейчас просить пощады. Но, Сайто, "
      "бывают времена, когда человек должен сражаться за честь."),
320: ("I'm not from this world, so I don't know about honor. I just protected everyone.",
      "Я не из этого мира, поэтому не понимаю чести. Я просто защищал всех."),
321: ("...", "…"),
322: ("Give Haruna back.", "Верни Харуну."),
323: ("Ah, I understand. I'll do what I can.", "Ах, понятно. Я сделаю что смогу."),
324: ("Looks like the soldiers and ships have withdrawn. Well, the academy's crisis is over.",
      "Похоже, солдаты и корабли отступили. Ну, кризис в академии миновал."),
325: ("A lot happened, but that's the end of this affair, isn't it, partner?",
      "Многое случилось, но на этом дело закрыто, приятель?"),
326: ("S-Saito...", "С-Сайто…"),
327: ("Y-Yeah... Louise.", "Д-Да… Луиза."),
328: ("Darling, Tabitha, I'm glad you're unhurt. Well, I believed in you, though.",
      "Дорогой, Табаса, рада, что вы не пострадали. Ну, я в вас верила."),
329: ("Everyone safe? Then everything worked out. Good.", "Все целы? Тогда всё "
      "получилось. Хорошо."),
330: ("Saito-san! You're safe! Thank goodness!", "Сайто-сан! Вы живы! Слава богу!"),
331: ("S-Siesta! I'm glad you're safe too.", "С-Сиэста! Я рад, что и ты в порядке."),
332: ("Listen, Saito-san. When I came to, I was tied up with rope inside Miss Valliere's "
      "closet.", "Слушайте, Сайто-сан. Когда я пришла в себя, я была связана верёвкой "
      "в шкафу мисс Вальер."),
333: ("I was so scared, so scared... But somehow the rope loosened, and I could run to you.",
      "Я так боялась, так боялась… Но верёвка как-то ослабла, и я смогла прибежать к вам."),
334: ("I should have tied you more securely...", "Надо было связать тебя покрепче…"),
335: ("L-Louise... By the way, what's happening in Tristania?", "Л-Луиза… Кстати, "
      "что происходит в Тристании?"),
336: ("We just got word from the capital about that.", "Нам только что пришло известие "
      "из столицы об этом."),
337: ("The Reconquista fleet heading for Tristania panicked at the sudden appearance "
      "of a mysterious huge fleet and withdrew.", "Флот Реконкисты, шедший к Тристании, "
      "запаниковал при внезапном появлении таинственного огромного флота и отступил."),
338: ("Same for the street fighting. The sudden fleet threw the enemy units occupying "
      "the battery posts into disarray, and...", "То же и с уличными боями. "
      "Появление флота нарушило строй вражеских отрядов у батарей, и…"),
339: ("...there were some casualties, but we retook most of the batteries.",
      "…были потери, но мы отвоевали большинство батарей."),
340: ("It worked out after all, Louise.", "Всё получилось, Луиза."),
341: ("Mm...", "Мм…"),
342: ("Something's odd about you two. I sense a strange atmosphere.",
      "Что-то странное в вас двоих. Я чувствую некое напряжение."),
343: ("N-No, there's nothing! Right, everyone?", "Н-Нет, ничего нет! Верно, все?"),
344: ("Well now, who can say~.", "Ну, кто знает~."),
345: ("...", "…"),
346: ("Don't tell me—Miss Valliere, you kissed Saito-san!?", "Неужто… мисс Вальер, "
      "вы поцеловали Сайто-сана!?"),
347: ("W-What are you talking about? That's impossible.", "Ч-Что ты говоришь? "
      "Такого не может быть."),
348: ("R-Right. I'd never kiss Louise. Ha ha, ha ha ha...", "В-Верно. Я бы никогда "
      "не поцеловал Луизу. Ха-ха, ха-ха-ха…"),
349: ("No. My woman's intuition tells me Saito-san kissed Miss Valliere.",
      "Нет. Моя женская интуиция говорит, что Сайто-сан поцеловал мисс Вальер."),
350: ("T-That's...", "Т-Это…"),
351: ("It's impossible, right?", "Этого не может быть, да?"),
352: ("Then both of you—look straight into my eyes!", "Тогда вы двое — "
      "посмотрите мне прямо в глаза!"),
353: ("...", "…"),
354: ("...", "…"),
355: ("You looked away, didn't you?", "Вы отвели взгляд, да?"),
356: ("Miss Valliere! We formed an alliance, didn't we? No going behind each other's backs!",
      "Мисс Вальер! Мы же заключили союз? Никаких тайных сделок!"),
357: ("You betrayed me! That's awful!", "Вы предали меня! Это ужасно!"),
358: ("...", "…"),
359: ("Saito-san! Thank you for worrying about me.", "Сайто-сан! Спасибо, что волновались за меня."),
360: ("J-Just a moment, Siesta.", "П-Подожди, Сиэста."),
361: ("Just a moment, Siesta! Why are you clinging to Saito?", "Подожди, Сиэста! "
      "Почему ты прижимаешься к Сайто?"),
362: ("I-I'm just expressing my gratitude to Saito-san for worrying about me.",
      "Я-Я просто выражаю благодарность Сайто-сану за то, что он волновался."),
363: ("Expressing gratitude means clinging to him?", "Выражать благодарность — "
      "значит прижиматься?"),
364: ("Then let me say this: Miss Valliere is too hard on Saito-san.",
      "Тогда позвольте сказать: мисс Вальер слишком строга к Сайто-сану."),
365: ("He did such a big job. You could praise him, couldn't you?", "Он проделал "
      "такую большую работу. Могли бы и похвалить его!"),
366: ("...", "…"),
367: ("Oh, Tabitha. Let's clear out.", "О, Табаса. Уйдём отсюда."),
368: ("Mm.", "Мм."),
369: ("Mr. Colbert. Let's take the prisoners and go outside as well.",
      "Кольбер-сэн. Давайте возьмём пленников и тоже выйдем наружу."),
370: ("Yes.", "Да."),
371: ("J-Just a moment.", "П-Подождите."),
372: ("I won't forgive you. It's all this stupid dog's fault!", "Я не прощу. "
      "Всё из-за этой тупой собаки!"),
373: ("W-Wait! Siesta, run away quickly. If you stay here any longer, your life will be in danger!",
      "П-Подожди! Сиэста, беги скорее. Если останешься здесь дольше, тебе угрожает опасность!"),
374: ("It's fine. I don't know what will happen if I'm with Saito-san, but it's what I wish for!",
      "Всё хорошо. Я не знаю, что случится, если я буду с Сайто-саном, но этого я и желаю!"),
375: ("I see. You've got nerve.", "Понятно. У тебя смелости не занимать."),
376: ("Saito, you idiot!", "Сайто, дурья башка!"),
377: ("Gyaaah!!!", "Гя-а-а-а!!!"),
}
CHOICES = {}
SPK = {'ウェザリー': 'w', 'サイト': 's', 'タバサ': 't', 'アキナ': 'ak', 'オスマン': 'o',
       'デルフリンガー': 'd', 'ルイズ': 'l', 'キュルケ': 'k', 'コルベール': 'c',
       'シエスタ': 'si', 'null': 'th'}
START = {'w': 4, 's': 316, 't': 44, 'ak': 4, 'o': 0, 'd': 33, 'l': 265,
         'k': 77, 'c': 105, 'si': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch19/parse_739_768.json', encoding='utf-8'))
    script = ['# Глава 19, часть 3 (сцены 764–768): прошлое Уэзерби, развязка, финал.',
              '# Источник: ps2_source/chapters/chapter_20_小悪魔と春風の協奏曲.txt (SCENE 764-768).',
              '', 'label ch19_3:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] < 764:
                continue
            scene = x['no']
            script += ['label ch19_3_scene_%d:' % scene, '']
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
            tag = 'ch19_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch19_3_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch19_3_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 764 <= scene <= 768:
                continue
            script.append('    # → next scene %d' % x['target'])
            if x['target'] > 768:
                script.append('    jump ch20')
            else:
                script.append('    jump ch19_3_scene_%d' % x['target'])
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 19 ====', '    jump ch20', '    return', '']
    files = {
        'game/chapters/19/script-ch19_3.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch19_3_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch19_3_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch19_3_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch19_3_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch19/voice_map_3.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
