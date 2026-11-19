#!/usr/bin/env python3
"""Chapter 25 part 2 (scenes 918-932): Tabitha's date, the tail, mages attack."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
135: ("...... ... ...", "……… … …"),
136: ("After that, I waited quietly—but quite a lot of time has passed by now...",
     "После этого я тихо ждал — но прошло уже довольно много времени…"),
137: ("Tabitha's taking too long, even by her standards, isn't she?", "Табаса слишком долго, даже по её меркам, да?"),
138: ("...Hah!?", "…Ах!?"),
139: ("Could this be... being stood up?", "Неужто… меня бросили?"),
140: ("No, wait, wait. I should think more positively about this.", "Нет, погоди. Надо думать позитивнее."),
141: ("Right, positively... Hmm... A 'neglect play'?", "Так, позитивнее… Хм… «Игра в пренебрежение»?"),
142: ("That's quite possible, a neglect play...", "Вполне возможно, «игра в пренебрежение»…"),
143: ("What's a neglect play?", "Что такое «игра в пренебрежение»?"),
144: ("Whoa!? T-Tabitha-san!?", "Ой!? Т-Табаса-сан!?"),
145: ("...", "…"),
146: ("S-Since when were you there?", "С-С каких пор ты там?"),
147: ("I just got here.", "Я только пришла."),
148: ("O-Oh. I see.", "О-Ох. Понятно."),
149: ("The neglect play?", "«Игра в пренебрежение»?"),
150: ("Umm...", "Э-Э…"),
151: ("More importantly—did you change clothes?", "Главное — ты переоделась?"),
152: ("Mm.", "Мм."),
153: ("I mean... I usually only see you in your uniform, so Tabitha in different clothes "
      "looks really fresh.", "Я хочу сказать… я обычно вижу тебя только в форме, поэтому "
      "Табаса в другой одежде выглядит так свежо."),
154: ("...", "…"),
155: ("You have no need to know!", "Тебе не нужно знать!"),
156: ("I can't know?", "Я не могу знать?"),
157: ("No.", "Нет."),
158: ("No?", "Нет?"),
159: ("A-Ah, Tabitha, did you change clothes?", "А-Ах, Табаса, ты переоделась?"),
160: ("You're dodging the question.", "Ты уходишь от ответа."),
161: ("Ugh.", "Ох."),
162: ("N-No! I was just amazed by Tabitha's usual clothes—I've never seen them before!",
     "Н-Нет! Я просто поражён был твоей повседневной одеждой — я её никогда не видел!"),
163: ("Amazed?", "Поражён?"),
164: ("Yeah, amazed. It looks really fresh and nice!", "Да, поражён. Выглядит очень свежо и хорошо!"),
165: ("...", "…"),
166: ("So, the neglect play?", "Так, «игра в пренебрежение»?"),
167: ("Well, let's leave that for next time.", "Ну, давай оставим это на следующий раз."),
168: ("A 'neglect play' is...", "«Игра в пренебрежение» — это…"),
169: ("...one of the twisted ways of showing affection that exists in my country.",
     "…один из извращённых способов выражения любви, который есть в моей стране."),
170: ("Affection...", "Любовь…"),
171: ("No, I'm sure you're misunderstanding. Twisted affection is a very difficult thing!",
     "Нет, думаю, ты не так поняла, но извращённая любовь — очень сложная вещь!"),
172: ("For one thing, it only works if there's a relationship of trust between the one "
      "doing it and the one receiving it.", "Во-первых, она работает только если между тем, "
      "кто её проявляет, и тем, кто её получает, есть доверие."),
173: ("Trust.", "Доверие."),
174: ("You mustn't admire it! Normal people hate it!", "Ты не должна ей восхищаться! Обычные люди её ненавидят!"),
175: ("Mm.", "Мм."),
176: ("So, Tabitha—what should I do?", "Так, Табаса — что мне делать?"),
177: ("...", "…"),
178: ("What's wrong? Don't hold back, tell me anything.", "Что случилось? Не стесняйся, говори что угодно."),
179: ("All day today.", "Весь сегодняшний день."),
180: ("Mm-hm.", "Мм-хм."),
181: ("I want you to keep me company.", "Я хочу, чтобы ты побыл со мной."),
182: ("Mm-hm... Eh? Keep you company?", "Мм-хм… А? Побыть с тобой?"),
183: ("No?", "Нет?"),
184: ("Of course not! Of course not! I'd be delighted to accompany you!!",
     "Конечно нет! Конечно нет! Я с радостью составлю тебе компанию!!"),
185: ("...", "…"),
186: ("(I feel like she's dodging the question about the letter... But whatever.)",
     "Кажется, она уходит от ответа о письме… Но ладно."),
187: ("So, where do you want me to accompany you, Tabitha?", "Так, куда ты хочешь, чтобы я тебя сопровождал, Табаса?"),
188: ("You decide.", "Решай сам."),
189: ("Eh? I can decide where we go?", "А? Я сам решаю, куда идти?"),
190: ("Mm.", "Мм."),
191: ("Um...", "Э-Э…"),
192: ("[Move] Theater", "[Переход] Театр"),
193: ("[Move] Main street", "[Переход] Главная улица"),
194: ("[Move] Back street", "[Переход] Задняя улица"),
195: ("[Move] Highway", "[Переход] Большая дорога"),
196: ("Heh heh. You both seem to be enjoying yourselves, darling and Tabitha.",
     "Хи-хи. Вы оба вроде весело проводите время, дорогой и Табаса."),
197: ("Hey, Kirche. Why do we all have to tail those two?", "Эй, Кирке. Почему мы все должны следить за этими двумя?"),
198: ("Why? Because I'm worried about darling, obviously. And of course, I'm worried about Tabitha, too.",
     "Почему? Потому что я волнуюсь за дорогого, понятно. И, конечно, я волнуюсь и за Табасу."),
199: ("You're worried too, aren't you, Louise? Otherwise you wouldn't have come along, would you?",
     "Ты тоже волнуешься, Луиза? Иначе бы ты не пошла, да?"),
200: ("I'm not saying I'm worried! I'm saying tailing people is bad taste!",
     "Я не говорю, что волнуюсь! Я говорю, что слежка — дурной тон!"),
201: ("Besides, tailing people isn't something a noble would do...", "И к тому же слежка — не то, чем занимаются дворяне…"),
202: ("So, Louise-san is going home?", "Значит, Луиза-сан идёт домой?"),
203: ("I'm in favor of tailing them.", "Я за слежку."),
204: ("Saito is my familiar. To leave your mistress behind and—oh!", "Сайто — мой фамильяр. Оставить госпожу и — ну же!!"),
205: ("H-Hey, Louise! If you shout like that, they'll spot us!", "Э-Эй, Луиза! Если ты так закричишь, они нас заметят!"),
206: ("Grrrr!!", "Гр-р-р!!"),
207: ("Aah! Saito-san is holding Miss Tabitha's hand!?", "Ах! Сайто-сан держит руку мисс Табасы!?"),
208: ("Eh? Eh!?", "А? А!?"),
209: ("Hiraga-kun. You seem to be getting pretty close to Tabitha-san...",
     "Хирага-кун. Кажется, ты довольно близко общаешься с Табасой-сан…"),
210: ("Kirche!", "Кирке!"),
211: ("Louise, why are you holding a staff?", "Луиза, зачем ты держишь посох?"),
212: ("Looks like the tailing is over, too.", "Похоже, слежка тоже закончилась."),
213: ("Say, Tabitha. Where are we going next?", "Слушай, Табаса. Куда мы идём дальше?"),
214: ("...!", "…!"),
215: ("Hmm? What's wrong, Tabitha? Your face suddenly got scary...", "Хм? Что случилось, Табаса? У тебя вдруг лицо стало страшным…"),
216: ("Get away from me.", "Отойди от меня."),
217: ("Get away—what do you mean?", "Отойди — что это значит?"),
218: ("Get away!", "Отойди!"),
219: ("...", "…"),
220: ("What are you people? Don't tell me...", "Что вы за люди? Неужто…"),
221: ("They're after Haruna, aren't they?", "Они охотятся за Харуной, да?"),
222: ("They're after Tabitha, aren't they?", "Они охотятся за Табасой, да?"),
223: ("They're jealous of us two, aren't they? Us, the best couple of the day!",
     "Они завидуют нам двоим, да? Нам, самопровозглашённой лучшей паре дня!"),
224: ("No.", "Нет."),
225: ("Eh? What do you mean, no? And how would you know, Tabitha?", "А? Что значит «нет»? И откуда ты знаешь, Табаса?"),
226: ("...", "…"),
227: ("At this rate, we won't be able to leave this place. So, might as well...",
     "Так мы отсюда не уйдём. Так что, ладно…"),
228: ("Saitooo!!", "Сайтооо!!"),
229: ("L-Louise? Why are you here?", "Л-Луиза? Откуда ты здесь?"),
230: ("Never mind that!", "Неважно!"),
231: ("Darring! I'll help you fight, too!", "Доррогой! Я тоже помогу тебе сразиться!"),
232: ("Kirche's here, too!?", "И Кирке здесь!?"),
233: ("...", "…"),
234: ("Phew. We drove them off somehow... but just what were they?", "Фух. Как-то мы их отогнали… но кто они такие?"),
235: ("...", "…"),
236: ("Say, Tabitha. You wouldn't happen to know who they were...", "Слушай, Табаса. Ты, случайно, не знаешь, кто они…"),
237: ("Are you all right, Hiraga-kun?", "Ты в порядке, Хирага-кун?"),
238: ("Are you injured, Saito-san?", "Вы не ранены, Сайто-сан?"),
239: ("Whoa, Haruna and Siesta!? Which means...", "Ого, Харуна и Сиэста!? Тогда…"),
240: ("Saito... You certainly had a good time, leaving your mistress behind.", "Сайто… Похоже, ты здорово развлёкся, бросив госпожу, да?"),
241: ("E-Eep!?", "Э-Ой!?"),
242: ("This calls for punishment...", "Это уже требует наказания…"),
243: ("They followed us.", "Они шли за нами."),
244: ("Eh?", "А?"),
245: ("...", "…"),
246: ("Ah, no, I didn't mean it that way... Right, Haruna?", "Ах, нет, я не это имела в виду… Верно, Харуна?"),
247: ("Y-Yes. We were just shopping.", "Д-Да. Мы просто делали покупки."),
248: ("And then we happened to spot Tabitha-san and Hiraga-kun... Right, Siesta-san?",
     "А потом мы случайно заметили Табасу-сан и Хирага-куна… Верно, Сиэста-сан?"),
249: ("Y-Yes. It was a coincidence.", "Д-Да. Это было совпадение."),
250: ("A coincidence—and a tail.", "Совпадение — и слежка."),
251: ("Ah ha, ha ha...", "А-ха-ха-ха…"),
}
CHOICES = {
918: [("Did you change clothes?", "Ты переоделась?"),
      ("You don't need to know!", "Тебе не нужно знать!"),
      ("A 'neglect play' is...", "«Игра в пренебрежение» — это…")],
927: [("They're after Haruna", "Они охотятся за Харуной"),
      ("They're after Tabitha", "Они охотятся за Табасой"),
      ("Jealous of us?", "Завидуют нам?")],
}
SPK = {'サイト': 's', 'タバサ': 't', 'キュルケ': 'k', 'ルイズ': 'l',
       'ハルナ': 'ha', 'シエスタ': 'si', '魔導士': 'mage', 'null': 'th'}
START = {'s': 64, 't': 20, 'k': 19, 'l': 27, 'ha': 2, 'si': 3, 'mage': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch25/parse_903_933.json', encoding='utf-8'))
    script = ['# Глава 25, часть 2 (сцены 918–932): свидание с Табасой, слежка, нападение магов.',
              '# Источник: ps2_source/chapters/chapter_26_手紙の秘密.txt (SCENE 918-932).',
              '', 'label ch25_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 932: break
            if x['no'] < 918:
                scene = None
                continue
            scene = x['no']
            script += ['label ch25_2_scene_%d:' % scene, '']
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
                ctext = '%s{#ch25_2_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch25_2_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 918 <= scene <= 932: continue
            t = x['target']
            script.append('    # → next scene %d' % t)
            if 918 <= t <= 932:
                script.append('    jump ch25_2_scene_%d' % t)
            elif 1513 <= t <= 1532:
                script.append('    # date event → ch25_4')
                script.append('    jump ch25_4')
            else:
                script.append('    jump ch25_3')
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 2 ====', '    jump ch25_3', '    return', '']
    files = {
        'game/chapters/25/script-ch25_2.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch25_2_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch25_2_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch25_2_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch25_2_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch25/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
