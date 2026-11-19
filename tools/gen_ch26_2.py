#!/usr/bin/env python3
"""Chapter 26 part 2 (scenes 944-954): audience with Henrietta, empty theater."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
136: ("I am Louise Francoise, third daughter of the Duke of La Valliere.",
      "Я — Луиза Франсуаза, третья дочь герцога Ла Вальера."),
137: ("A-A Duke's family!?", "Г-Герцогская семья!?"),
138: ("I wish an audience with the princess—no, with Her Majesty the Queen. Please announce me.",
      "Я прошу аудиенции у принцессы — нет, у Её Величества Королевы. Прошу доложить обо мне."),
139: ("To Her Majesty!? U-Understood. I'll check at once—please wait here.",
      "Принцессе!? П-Понятно. Я сейчас проверю — подождите здесь."),
140: ("Thank you.", "Спасибо."),
141: ("Wow—being a duke's family is amazing. That soldier who was so strict folded in no time.",
      "Ого — быть герцогской семьёй здорово. Тот строгий солдат сразу сдался."),
142: ("You only realized that now? From now on, act with a little more awareness of your position.",
      "Ты только сейчас это понял? Впредь действуй, хоть немного помня о своём положении."),
143: ("Yeess.", "Да-а-а."),
144: ("Sorry to keep you waiting. You're to be shown to a room at once.",
     "Простите за ожидание. Вас должны немедленно проводить в комнату."),
145: ("Thank you very much.", "Большое спасибо."),
146: ("Then, this way...", "Тогда, сюда…"),
147: ("...... ... ...", "……… … …"),
148: ("Excuse us...", "Простите за вторжение…"),
149: ("My, Louise Francoise! You're safe!", "Ох, Луиза Франсуаза! Ты невредима!"),
150: ("Your Majesty, who are these people?", "Ваше Величество, кто эти люди?"),
151: ("My childhood friend and her good friends.", "Моя подруга детства и её добрые друзья."),
152: ("...", "…"),
153: ("(I knew it, but their reaction is lukewarm...)", "Я знал это, но их реакция прохладная…"),
154: ("(It can't be helped. Let's behave ourselves here.)", "Ничего не поделать. Будем здесь вести себя тихо."),
155: ("Sorry to interrupt. Please continue the report.", "Простите, что прервала. Продолжайте доклад."),
156: ("Yes!", "Да!"),
157: ("Then, I'll report on the situation gathered so far.", "Тогда я доложу о ситуации, собранной на данный момент."),
158: ("Today's explosions and the fighting in various places...",
     "Сегодняшние взрывы и бои в разных местах…"),
159: ("...are believed to be the work of the bomber and his accomplices.",
     "…предположительно,деяния бомбиста и его сообщников."),
160: ("It's late to notice this now, but the bomber doesn't seem to have been detonating "
      "bombs indiscriminately.", "Поздно замечать это, но бомбист, похоже, не взрывал всё подряд."),
161: ("Meaning what?", "То есть?"),
162: ("According to a captured soldier's testimony, craftsmen were invited from various countries "
      "to repair the sites of previous bombings—", "По показаниям захваченного солдата, для ремонта "
      "мест предыдущих взрывов приглашались мастера из разных стран —"),
163: ("Apparently, saboteurs were sent in among those craftsmen and secretly installed gun "
      "emplacements at the repair sites.", "Похоже, среди мастеров были посланы диверсанты, и на "
      "местах ремонта тайно установили орудийные позиции."),
164: ("We can say the castle is now in a critical situation, surrounded by enemy batteries.",
     "Можно сказать, что замок сейчас в критическом положении — окружён вражескими батареями."),
165: ("It seems a huge organization lurks behind the bomber, doesn't it?",
     "Похоже, за бомбистом стоит огромная организация, да?"),
166: ("Did you learn which unit the captured soldier belonged to?", "Удалось выяснить, к какому "
     "подразделению принадлежал захваченный солдат?"),
167: ("No. We haven't extracted that much testimony yet.", "Нет. Пока не удалось добиться таких показаний."),
168: ("I see...", "Понятно…"),
169: ("(A while later, the princess looked quite tired after ending the meeting.)",
     "Спустя некоторое время принцесса выглядела довольно уставшей после совещания."),
170: ("Sorry to keep you waiting.", "Простите, что заставила ждать."),
171: ("No, the fault is ours—to barge in at such a busy time.", "Нет, виноваты мы — ворвались в "
     "такое напряжённое время."),
172: ("It's fine, Louise.", "Всё хорошо, Луиза."),
173: ("So—what is it? Is it related to the bomber?", "Так — в чём дело? Это связано с бомбистом?"),
174: ("Well, that is...", "Ну, это…"),
175: ("Oh, what's wrong? It's us, isn't it? Don't hold back—tell me.",
     "Ох, что случилось? Мы же с тобой близкие, правда? Не стесняйся — говори."),
176: ("But, Princess...", "Но, принцесса…"),
177: ("Then I'll be blunt with Her Majesty myself...", "Тогда я сам скажу Её Величеству напрямую…"),
178: ("H-Hey, Saito! You be quiet!!", "Э-Эй, Сайто! Ты помалкивай!!"),
179: ("Well, the exchange was so roundabout, I just...", "Ну, разговор такой тянутый, я и…"),
180: ("If your 'just' offends the princess, we're the ones in trouble!",
     "Если твоё «и» оскорбит принцессу, пострадаем мы!"),
181: ("Heh heh heh... You're still an entertaining familiar, aren't you?",
     "Хи-хи-хи… Ты всё такой же забавный фамильяр, да?"),
182: ("I'm terribly sorry, Princess! It's only because my training of him was lacking...",
     "Прошу прощения, принцесса! Всё из-за того, что я плохо его воспитала…"),
183: ("To be frank—we'd like to be informed of the capital's current situation. That's why...",
     "Откровенно говоря — мы хотели бы узнать о текущей ситуации в столице. Поэтому…"),
184: ("I understand. Then, let me explain the state of the capital.", "Понятно. Тогда расскажу о положении в столице."),
185: ("At present, we're fighting enemy soldiers who've infiltrated several parts of the capital.",
     "Сейчас мы боремся с вражескими солдатами, проникшими в несколько районов столицы."),
186: ("As the report said, the whole series of incidents caused by the bomber seems to have been planned.",
     "Как и в докладе, вся серия инцидентов, вызванных бомбистом, похоже, была спланирована."),
187: ("I can't help regretting that we didn't notice it a little earlier...",
     "Я не могу не сожалеть, что не заметили это чуть раньше…"),
188: ("Princess...", "Принцесса…"),
189: ("...", "…"),
190: ("Cheer up, Princess.", "Не падайте духом, принцесса."),
191: ("If you're down, everyone around you gets gloomy, too.", "Если вы подавлены, все вокруг тоже мрачнеют."),
192: ("Heh, that's true. Thank you, familiar.", "Хи, верно. Спасибо, фамильяр."),
193: ("What's done is done. We should think about how to win the fighting happening now.",
     "Что сделано, то сделано. Нужно думать, как победить в текущем бою."),
194: ("Saito! What are you doing, giving the Princess your opinion so boldly!?",
     "Сайто! Что ты делаешь, так дерзко давая принцессе советы!?"),
195: ("Why are you angry? I'm just speaking sense...", "Почему ты злишься? Я же говорю дельное…"),
196: ("Thank you, familiar. Indeed, you're right. I nearly lost sight of what matters again.",
     "Спасибо, фамильяр. И верно. Я чуть снова не упустила главное."),
197: ("W-Well, if the Princess says it's fine, then it's fine...", "Н-Ну, если принцесса говорит, что хорошо, значит хорошо…"),
198: ("Do you know what will happen next, Princess?", "Знаете ли вы, что будет дальше, принцесса?"),
199: ("How dare you take that tone with the Princess! Of course she can't know!",
     "Как ты смеешь так разговаривать с принцессой! Конечно, она не может знать!"),
200: ("She can't know... You're right.", "Не может знать… Верно."),
201: ("Indeed, we still don't grasp their objective, do we?", "И верно, мы ещё не поняли их цель, да?"),
202: ("Look to what comes next rather than what's happening now. That's quite right.",
     "Смотреть не на то, что происходит сейчас, а на то, что будет дальше. Это верно."),
203: ("Thank you, familiar. I nearly repeated my mistake.", "Спасибо, фамильяр. Я чуть не повторила ошибку."),
204: ("W-Well, if the Princess says it's fine, then it's fine...", "Н-Ну, если принцесса говорит, что хорошо, значит хорошо…"),
205: ("Louise... In this situation, it'll be hard to ask about Haruna, too.",
     "Луиза… В такой ситуации и спросить о Харуне будет трудно."),
206: ("Y-You fool. Saying unnecessary things...", "Г-Глупец. Говорит лишнее…"),
207: ("Haruna... The girl you acted with in the play, was it? What happened to her?",
     "Харуна… Та девушка, с которой ты играла в спектакле, да? Что с ней?"),
208: ("Y-Yes, Princess. Actually, Haruna went missing around the time the fighting began...",
     "Д-Да, принцесса. Дело в том, что Харуна пропала примерно когда начался бой…"),
209: ("My, missing? That's serious.", "Ох, пропала? Это серьёзно."),
210: ("Yes, we tried searching, but... we couldn't find her. We thought if you had any information...",
     "Да, мы пытались искать, но… не нашли. Мы подумали, если у вас есть сведения…"),
211: ("I see...", "Понятно…"),
212: ("As you can see, information-gathering isn't functioning well now that fighting has broken out.",
     "Как видите, сбор информации работает плохо, с тех пор как начался бой."),
213: ("The moment I learn anything, I'll inform Louise.", "Как только я что-то узнаю, я сообщу Луизе."),
214: ("Thank you for your consideration.", "Спасибо за ваше внимание."),
215: ("Haruna... Where did you go...", "Харуна… Куда ты ушла…"),
216: ("...", "…"),
217: ("We learned the capital's situation, but not even Haruna's, it seems.",
     "Мы узнали о положении в столице, но даже о Харуне — нет, кажется."),
218: ("Even if we had info on Haruna, it wouldn't reach the princess's ears anyway.",
     "Даже если бы были сведения о Харуне, до принцессы они бы всё равно не дошли."),
219: ("Mm.", "Мм."),
220: ("More importantly, I wonder how Kirche is doing...", "Главное — интересно, как дела у Кирке…"),
221: ("Judging by the lack of news, I'm afraid there's no good news, either.",
     "Судя по тому, что нет вестей, боюсь, хороших новостей тоже нет."),
222: ("...", "…"),
223: ("Saito-san, it's all right. I'm sure Haruna-san is safe.", "Сайто-сан, всё хорошо. Я уверена, Харуна-сан в безопасности."),
224: ("Mm...", "Мм…"),
225: ("Darring!!", "Дорррогой!!"),
226: ("Kirche!", "Кирке!"),
227: ("I missed you, darling. Being apart from you, this body of mine was burning with longing!",
     "Я скучала, дорогой. Пока мы были в разлуке, это тело горело от тоски!"),
228: ("You can say that, but stop hugging Saito!", "Можешь говорить что хочешь, но перестань обнимать Сайто!"),
229: ("Oh, come on. It's not like he'll shrink from it.", "О, да ладно. Он от этого не уменьшится."),
230: ("Ugh.", "Ох."),
231: ("W-Well, fine. More importantly—did you find Haruna?", "Н-Ну, ладно. Главное — ты нашла Харуну?"),
232: ("Not at all. Nobody's seen her.", "Совсем нет. Никто её не видел."),
233: ("I see...", "Понятно…"),
234: ("Cheer up, darling. I can think of one place she might be.", "Не унывай, дорогой. Я могу думать об одном месте, где она может быть."),
235: ("W-Where?", "Г-Где?"),
236: ("The theater. There must be some clue there.", "Театр. Там наверняка есть зацепка."),
237: ("The theater? Why there?", "Театр? Почему именно там?"),
238: ("The theater...", "Театр…"),
239: ("Well, just come with me.", "Ну, просто иди за мной."),
240: ("A-Oh, wait!", "А-Ой, погоди!"),
241: ("...... ... ...", "……… … …"),
242: ("Nobody's here and there's nothing here! It's completely empty. We've been played...",
     "Никого нет и ничего нет! Совершенно пусто. Нас провели…"),
243: ("Played how? I'd like a proper explanation!", "Провели — это как? Я хочу нормального объяснения!"),
244: ("The thing is, Tabitha and I were investigating the bomber, and we found out that "
      "a suspicious person was coming and going at the theater.", "Дело в том, что мы с Табасой "
      "расследовали бомбиста и выяснили, что в театр входил и выходил подозрительный человек."),
245: ("Wait a moment. Why did you two keep such an important thing to yourselves until now?",
     "Погоди. Почему вы двое до сих пор скрывали такую важную вещь?"),
246: ("No evidence.", "Нет доказательств."),
247: ("Even without evidence... If you'd told us...", "Даже без доказательств… Если бы вы сказали нам…"),
248: ("You'd have confronted Weatherly, wouldn't you?", "Вы бы допросили Уэзерби, да?"),
249: ("...", "…"),
250: ("Surely you can't suspect someone without real proof, can you?",
     "Нельзя же подозревать человека без серьёзных доказательств, правда?"),
251: ("Of course, if it were this bold, we wouldn't have left it alone, either...",
     "Конечно, если бы это было так дерзко, мы бы тоже не оставили это без внимания…"),
252: ("Hmm...", "Хм…"),
253: ("Right. Kirche is right.", "Верно. Кирке права."),
254: ("It's precisely because we didn't know that there might be information to gain, "
     "isn't it? That's what Kirche decided, right?", "Именно потому, что мы не знали, могла "
     "появиться новая информация, да? Так решила Кирке, верно?"),
255: ("And if Weatherly were involved, she wouldn't have let us—who knew—go so easily, either.",
     "И если бы Уэзерби была замешана, она бы не отпустила нас, знающих, просто так."),
256: ("Right!? Darling understands perfectly!", "Верно!? Дорогой всё отлично понимает!"),
257: ("But, you could have at least told us...", "Но вы могли хотя бы сказать нам…"),
258: ("Darling, I know what you'll say—but she's a professional actress. She'd notice immediately.",
     "Дорогой, даже если ты и скажешь — она профессиональная актриса. Она сразу заметит."),
259: ("Then the whole investigation would be ruined, wouldn't it?", "Тогда всё расследование пошло бы насмарку, да?"),
260: ("Well, be that as it may—in the end, the other side was one step ahead, and it all fell apart.",
     "Ну, так или иначе — в конце концов, противник был на шаг впереди, и всё рухнуло."),
261: ("Saying it now won't change anything.", "Сейчас говорить об этом бесполезно."),
262: ("We didn't even notice that suspicious person, did we?", "Мы даже не заметили того подозрительного человека, да?"),
263: ("Well, yes, but...", "Ну, да, но…"),
264: ("In that sense, we're no different from you.", "В этом смысле мы ничем от вас не отличаемся."),
265: ("In the end, the other side was one step ahead and everything fell apart, too.",
     "В конце концов, противник был на шаг впереди, и у нас всё рухнуло."),
}
CHOICES = {
946: [("Cheer up", "Не падайте духом"),
      ("What's done is done", "Что сделано, то сделано"),
      ("What happens next?", "Что будет дальше?")],
951: [("Kirche is right", "Кирке права"),
      ("You could have told us", "Вы могли бы сказать нам"),
      ("It's too late now", "Сейчас уже поздно")],
}
SPK = {'ルイズ': 'l', '味方Ａ': 'soldier', 'サイト': 's', 'アンリエッタ': 'h',
       '将校': 'commander', 'タバサ': 't', 'シエスタ': 'si', 'キュルケ': 'k', 'null': 'th'}
START = {'l': 27, 'soldier': 7, 's': 58, 'h': 0, 'commander': 0,
         't': 18, 'si': 14, 'k': 10, 'th': 2}


def main():
    data = json.load(open('reports/ch26/parse_934_971.json', encoding='utf-8'))
    script = ['# Глава 26, часть 2 (сцены 944–954): аудиенция, пустой театр.',
              '# Источник: ps2_source/chapters/chapter_27_タバサの秘密.txt (SCENE 944-954).',
              '', 'label ch26_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 954: break
            if x['no'] < 944: continue
            scene = x['no']
            script += ['label ch26_2_scene_%d:' % scene, '']
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
                ctext = '%s{#ch26_2_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch26_2_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 944 <= scene <= 954: continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch26_2_scene_%d' % x['target'] if 944 <= x['target'] <= 954 else 'ch26_3'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 2 ====', '    jump ch26_3', '    return', '']
    files = {
        'game/chapters/26/script-ch26_2.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch26_2_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch26_2_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch26_2_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch26_2_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch26/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == "__main__":
    main()
