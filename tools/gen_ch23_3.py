#!/usr/bin/env python3
"""Chapter 23 part 3 (scenes 879-893): Akina's trap, Void illusion, victory."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
234: ("Princess. Would you grant me permission to use Void magic?", "Принцесса. Позвольте мне применить магию Пустоты?"),
235: ("Eh, seriously!?", "А, правда!?"),
236: ("Void magic, in this capital?", "Пустоту — в этой столице?"),
237: ("Yes. I think it's the only way.", "Да. Я думаю, это единственный путь."),
238: ("Hey, wait a second, Louise!? If you use Void, the whole city will be blown away!",
      "Эй, погоди, Луиза!? Если ты применишь Пустоту, город снесёт!"),
239: ("I know that much myself! I've thought of another way, so just be quiet for a moment!!",
      "Я и сама это знаю! Я придумала другой способ, так что помалкивай немного!!"),
240: ("Princess, please! Let me use the magic!", "Принцесса, прошу! Разрешите мне магию!"),
241: ("All right, Louise. I leave it to you.", "Ладно, Луиза. Полагаюсь на тебя."),
242: ("Thank you, Princess.", "Спасибо, принцесса."),
243: ("Do your best, Louise. I believe in your magic. When the enemy attacks, I'll definitely protect you.",
      "Постарайся, Луиза. Я верю в твою магию. Когда враг нападёт, я обязательно тебя защищу."),
244: ("Mm... I'll do my best, too.", "Мм… Я тоже постараюсь."),
245: ("So, do you have a chance of winning?", "Так, есть ли у тебя шанс победить?"),
246: ("Hmm, let me see. I'd say about fifty-fifty.", "Хм, подумаем. Примерно пятьдесят на пятьдесят."),
247: ("What's that supposed to mean? Are you going to be okay?", "Что это значит? Ты справишься?"),
248: ("It's fine. Anything's better than zero, right?", "Всё хорошо. Всё лучше нуля, да?"),
249: ("I see. So it's a 'if we die, we die together' kind of thing, is it?",
      "Понятно. Значит, это в духе «если умрём, то вместе», да?"),
250: ("What's that supposed to mean?", "Что ты хочешь сказать?"),
251: ("You're going to blow everything up with Void magic, aren't you?",
      "Ты же всё взорвёшь магией Пустоты, да?"),
252: ("I told you I won't do that! Honestly, you're so slow! Trust your mistress a little more!",
      "Я же сказала, что не буду! Право, какой же ты тупой! Хоть немного доверяй госпоже!"),
253: ("Let's go, Saito!", "Идём, Сайто!"),
254: ("Right!", "Да!"),
255: ("Just a little more and we'll be on the roof!!", "Ещё немного — и мы выйдем на крышу!!"),
256: ("Why the roof!?", "Почему на крышу!?"),
257: ("For this spell, I need the spot with the best view, more than anything!",
      "Для этого заклинания мне нужен обзорный участок, прежде всего!"),
258: ("I need to secure a place to cast! Got it!", "Нужно обеспечить место для заклинания! Понял?"),
259: ("Understood.", "Понял."),
260: ("Watch out, partner!", "Осторожно, приятель!"),
261: ("Take this!!", "Получи!!"),
262: ("Louise, look out!!", "Луиза, берегись!!"),
263: ("Kyaaa!!", "Кья-а-а!!"),
264: ("Gwaaah!!", "Гуа-а-а!!"),
265: ("Ugh... That was close.", "Ох… Едва увернулся."),
266: ("That explosion just now... The bomber is here, isn't she!", "Этот взрыв сейчас… Бомбист здесь, да!"),
267: ("Just as Weatherly-sama said, we've been interrupted, haven't we.",
      "Как и говорила Уэзерби-сама, нам помешали."),
268: ("Ah... You...", "А… Ты…"),
269: ("S-Seriously?", "П-Правда?"),
270: ("Heh heh... Hello, Saito-kun. Should I call you Hiraga-kun instead?",
      "Хи-хи… Здравствуй, Сайто-кун. Может, лучше звать тебя Хирага-куном?"),
271: ("Haruna!? What are you doing here!?", "Харуна!? Что ты здесь делаешь!?"),
272: ("I should ask you that. Leaving me behind, why are you in a place like this?",
      "Я должна спросить тебя. Бросив меня, почему ты оказался в таком месте?"),
273: ("Mmm... So the bomber was Haruna!?", "Мм… Так бомбист — это Харуна!?"),
274: ("That's right, Louise. And my name isn't Haruna.", "Верно, Луиза. И меня зовут не Харуна."),
275: ("I have a name given to me by Weatherly-sama—Akina.", "У меня есть имя, данное мне Уэзерби-сама, — Акина."),
276: ("Akina? And Weatherly... That Weatherly?", "Акина? И Уэзерби… Та самая Уэзерби?"),
277: ("That's right...", "Да…"),
278: ("I'm a persona—the bomber—created by Weatherly-sama separately from Haruna's consciousness.",
      "Я — личность бомбиста, созданная Уэзерби-сама отдельно от сознания Харуны."),
279: ("Weatherly—the one from that theater troupe!?", "Уэзерби — из той театральной труппы!?"),
280: ("Speaking of her so casually is worthy of ten thousand deaths. Weatherly-sama is my boss.",
      "Называть её так запросто — достойно десяти тысяч смертей. Уэзерби-сама — мой босс."),
281: ("So... the woman who took care of me when I first came to this world was Weatherly!?",
      "Значит… женщина, которая позаботилась обо мне, когда я впервые попал в этот мир, была Уэзерби!?"),
282: ("Saito, don't make me say the same thing twice. It hurts.",
      "Сайто, не заставляй меня повторять одно и то же. Тебе достанется."),
283: ("So we were dancing neatly on a stage prepared for us by Weatherly, were we?",
      "Значит, нами ловко манипулировали на сцене, подготовленной Уэзерби, да?"),
284: ("Heh heh!! That's right. It was all a farce, all of it.", "Хи-хи!! Верно. Всё было фарсом, всё."),
285: ("Not one of us could escape from the hand of Weatherly-sama, who prepared the stage.",
      "Никто из нас не смог уйти из руки Уэзерби-сама, подготовившей сцену."),
286: ("You sound as if you knew this would happen from the start, don't you?",
      "Ты говоришь так, будто знала, что всё так и будет с самого начала, да?"),
287: ("Haruna probably thinks she was acting of her own will, but it was all my will. "
      "Not knowing must be pitiful.", "Харуна, наверное, думает, что действовала по своей воле, "
      "но всё было моей волей. Не знать — жалко, правда?"),
288: ("You all pitied poor Haruna and went along with her, didn't you? And look at you now.",
      "Вы все пожалели бедняжку Харуну и пошли у неё на поводу, да? Вот к чему это привело."),
289: ("It went so well that I had to strain not to laugh.", "Всё шло так гладко, что я едва сдерживала смех."),
290: ("Manipulating Haruna's heart like that...", "Играть сердцем Харуны…"),
291: ("But that's over, too. Weatherly-sama is calling for my curtain call.",
      "Но и это кончено. Уэзерби-сама зовёт меня на поклон."),
292: ("Ugh...", "Ох…"),
293: ("Oh? You're motivated? Can you hurt Haruna's body? Well, I won't hold back, either.",
      "О? Ты горишь? Сможешь ли ты повредить тело Харуны? Что ж, я тоже не буду сдерживаться."),
294: ("Yeah, I can. Without a moment's hesitation.", "Да, смогу. Без малейшего колебания."),
295: ("What?", "Что?"),
296: ("Because I'm Louise's familiar! I won't let anyone lay a finger on my mistress!",
      "Потому что я фамильяр Луизы! Я не дам никому тронуть мою госпожу!"),
297: ("Coward!", "Трус!"),
298: ("A-ha-ha-ha! Say whatever you like!", "А-ха-ха-ха! Говори что хочешь!"),
299: ("We have no choice but to fight, Saito!", "Нам нечего делать, кроме как сражаться, Сайто!"),
300: ("Looks like it... Damn it!", "Похоже на то… Чёрт!"),
301: ("As if I could fight her! Damn it!", "Как будто я смогу с ней сразиться! Чёрт!"),
302: ("A-ha-ha-ha! If you're going to be killed by the woman you loved, that's a fine end for you, isn't it!?",
      "А-ха-ха-ха! Если тебя убьёт любимая тобой женщина — что ж, достойный конец, да!?"),
303: ("Saito! That's not Haruna now! We have to save her!", "Сайто! Это уже не Харуна! Мы должны её спасти!"),
304: ("You're right. Damn it!", "Верно. Чёрт!"),
305: ("Let's go, Louise!", "Идём, Луиза!"),
306: ("Yes, I understand.", "Да, поняла."),
307: ("Mmguah...!!", "Ммгуа-а…!!"),
308: ("Haa... We did it...", "Аа… У нас получилось…"),
309: ("Guh... You okay, Louise?", "Гух… Ты в порядке, Луиза?"),
310: ("Mm... Somehow.", "Мм… Коек-как."),
311: ("(Both Louise and I had collapsed on the spot.)", "И Луиза, и я рухнули на месте."),
312: ("Nice work, partner.", "Неплохо сработано, приятель."),
313: ("Heh. Praising me here won't get you anything. More importantly, is Haruna all right...!?",
      "Хи. Хвалить меня тут бесполезно. Главное — Харуна в порядке…!?"),
314: ("(No serious external injuries, it seems...)", "Кажется, серьёзных внешних ран нет…"),
315: ("You okay, Haruna?", "Ты в порядке, Харуна?"),
316: ("...", "…"),
317: ("She seems fine. No danger to her life.", "Похоже, в порядке. Жизни ничего не угрожает."),
318: ("Ah, she seems fine.", "Ах, похоже, она в порядке."),
319: ("But tie her up with rope. If she's still Akina, she'd be dangerous.",
      "Но свяжи её верёвкой. Если она всё ещё Акина, это опасно."),
320: ("But...", "Но…"),
321: ("Please.", "Прошу."),
322: ("All right.", "Ладно."),
323: ("More importantly, Louise. Use Void magic, please!", "Главное, Луиза. Примени Пустоту, прошу!"),
324: ("Mm.", "Мм."),
325: ("I'll make it succeed, for sure. Watch closely!", "Я обязательно добьюсь успеха. Смотри хорошенько!"),
326: ("Ah... Show me.", "Ах… Покажи."),
327: ("Illusion!!", "Иллюзия!!"),
328: ("Saito! Look at the legendary spell I chanted!", "Сайто! Посмотри на легендарное заклинание, которое я произнесла!"),
329: ("...This is incredible.", "…Это невероятно."),
330: ("(A huge fleet, enough to fill the whole sky, covered Tristain above in darkness.)",
      "Огромный флот, способный заполнить всё небо, покрыл Тристанию темнотой."),
331: ("The spell Louise was about to use was an incredible one, wasn't it.",
      "Заклинание, которое Луиза собиралась применить, было невероятным, да."),
332: ("But this is a product of Void. An illusion born of Void... a dream spell.",
      "Но это порождение Пустоты. Иллюзия, рождённая Пустотой… заклинание сна."),
333: ("Ah... Amazing!! The enemy is running from the batteries!", "Ах... Потрясающе!! Враг разбегается от батарей!"),
334: ("Heh heh... My magic is quite something, too, isn't it?", "Хи-хи… Моя магия тоже неплоха, да?"),
335: ("Well done for now, Louise.", "Пока что отличная работа, Луиза."),
336: ("Mm... The fighting isn't over yet. But there's nothing more we can do now.",
      "Мм… Бой ещё не закончен. Но больше мы ничего не можем."),
337: ("You've worked hard too, Saito. I'm grateful to you today.", "И ты постарался, Сайто. Я благодарна тебе сегодня."),
338: ("Now I might be able to keep my promise.", "Теперь я, кажется, смогу сдержать обещание."),
339: ("Promise?", "Обещание?"),
340: ("I borrowed a charm from Siesta. Now I can return it to her.",
      "Я занял у Сиэсты оберег. Теперь я могу его вернуть."),
341: ("Huuuuh, a charm, was it...", "Хммм, оберег, значит…"),
342: ("They say wearing it lets you avoid any disaster.", "Говорят, если его носить, любая беда обходит стороной."),
343: ("I see... Maybe it really worked, then?", "Понятно… Может, он и правда подействовал?"),
344: ("Yeah, I'd say so. It was rough, but we won.", "Да, я бы сказал, что да. Было тяжело, но мы победили."),
345: ("...It makes me angry, somehow.", "…Отчего-то мне становится обидно."),
346: ("W-Why!?", "П-Почему!?"),
347: ("We got through today, but do you think there'll be another war?",
      "Сегодня нас вытащило, но думаешь, будет ещё война?"),
348: ("Probably.", "Наверное."),
349: ("For now we saved the capital. Isn't that enough? We'll think about the rest when the time comes.",
      "Пока мы спасли столицу. Разве этого мало? Остальном подумаем, когда придёт время."),
350: ("Mm... You're right.", "Мм… Верно."),
351: ("Well then, let's go. The princess is waiting.", "Ну что ж, идём. Принцесса ждёт."),
352: ("You're right.", "Верно."),
353: ("(Siesta, I kept my promise.)", "Сиэста, я сдержал обещание."),
}
CHOICES = {
879: [("Believe in Louise's power", "Верить в силу Луизы"),
      ("Is there a chance of winning?", "Есть ли шанс победить?"),
      ("If we die, we die together", "Если умрём, то вместе")],
884: [("Yes, I can do it", "Да, я смогу"),
      ("That's cowardly!", "Это трусость!"),
      ("There's no way I can!", "Я никак не смогу!")],
889: [("Good work, Louise", "Отличная работа, Луиза"),
      ("I can return the charm", "Я смогу вернуть оберег"),
      ("The fight will go on", "Наверное, бой ещё продолжится, да?")],
}
SPK = {'ルイズ': 'l', 'サイト': 's', 'アンリエッタ': 'h', 'デルフリンガー': 'd',
       'アキナ': 'ak', 'ハルナ': 'ha', 'null': 'th'}
START = {'l': 59, 's': 84, 'h': 29, 'd': 0, 'ak': 0, 'ha': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch23/parse_849_893.json', encoding='utf-8'))
    script = ['# Глава 23, часть 3 (сцены 879–893): ловушка Акины, иллюзия Пустоты, победа.',
              '# Источник: ps2_source/chapters/chapter_24_沈黙の応援.txt (SCENE 879-893).',
              '', 'label ch23_3:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] < 879: continue
            scene = x['no']
            script += ['label ch23_3_scene_%d:' % scene, '']
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
            tag = 'ch23_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch23_3_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch23_3_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 879 <= scene <= 893: continue
            t = x['target']
            script.append('    # → next scene %d' % t)
            script.append('    jump %s' % ('ch23_3_scene_%d' % t if 879 <= t <= 893 else 'ch24'))
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 23 ====', '    jump ch24', '    return', '']
    files = {
        'game/chapters/23/script-ch23_3.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch23_3_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch23_3_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch23_3_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch23_3_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch23/voice_map_3.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
