#!/usr/bin/env python3
"""Chapter 21 part 2 (scenes 780-789): love confusion, cooking contest decided."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
148: ("F-Forget about that! Never mind my laundry! It's about why Siesta was acting strange!",
      "Т-Так, неважно! Забудьте про мою стирку! Дело в том, почему Сиэста вела себя странно!"),
149: ("Somehow, you just kind of zone out, don't you?", "Как будто просто отключаешься, да?"),
150: ("Could she be carrying some trouble she can't even confide in us about?",
      "Может, у неё есть какая-то беда, о которой она не может нам даже рассказать?"),
151: ("If so, there's only one thing left, I'm sure.", "Если так, то остаётся только одно."),
152: ("One thing?", "Одно — что?"),
153: ("Love.", "Любовь."),
154: ("Lo-ove!?", "Л-Любовь!?"),
155: ("Ah, of course. Love does blind people, after all...", "А, конечно. Любовь и правда ослепляет…"),
156: ("So what about it, Saito? Spit it out.", "Так что скажешь, Сайто? Говори прямо."),
157: ("Hold on. Why is my name coming up here!?", "Погоди. Почему тут вообще моё имя!?"),
158: ("If we're talking about Siesta's love, you're obviously the cause, right!",
     "Если речь о любви Сиэсты, то причина, понятно, ты!"),
159: ("It's your fault for acting suggestively toward every girl you see!",
     "Это твоя вина — ты со всеми девушками ведёшь себя двусмысленно!"),
160: ("What's more, as my familiar, you shouldn't be laying hands on other girls!!",
     "Более того, будучи моим фамильяром, не смей приставать к другим девушкам!!"),
161: ("Calm down!! Whoa, what are you about to do, Louise!?", "Успокойся!! Ой, что ты хочешь сделать, Луиза!?"),
162: ("I'll beat that attitude right out of you!!", "Я выбью из тебя это желание!!"),
163: ("Gyaaaaaaaaaaaaaa!!", "Гя-а-а-а-а-а-а-а!!"),
164: ("Temporary suspension.", "Временное прекращение."),
165: ("Now that I think about it, Siesta seemed a bit distracted even while we were helping with the play.",
     "Теперь, когда я вспоминаю, Сиэста и во время спектакля была немного рассеянной."),
166: ("That explains it. Siesta was cast as Hiraga-kun's lover in the play, wasn't she?",
     "Вот оно. Сиэста же была в роли возлюбленной Хирага-куна в спектакле, верно?"),
167: ("So you're saying that through the play, Siesta confessed to Hiraga-kun—even if it was a role— "
      "and developed feelings for him?", "То есть вы хотите сказать, что через спектакль Сиэста "
      "призналась Хирага-куну — пусть и в роли — и влюбилась в него?"),
168: ("W-Wait a second. Is there any proof Siesta actually has feelings for me?",
     "П-Подождите минуту. Есть ли хоть какое-то доказательство, что Сиэста меня любит?"),
169: ("And even if she did 'confess,' that was just inside the play, right? Haruna, you're going too far.",
     "И даже если она «призналась», это было внутри спектакля, да? Харуна, ты слишком далеко заходишь."),
170: ("...", "…"),
171: ("Eh?", "А?"),
172: ("...", "…"),
173: ("Eh?", "А?"),
174: ("...", "…"),
175: ("Eh?", "А?"),
176: ("Siesta has the right to love someone, too. But she's got some nerve setting her sights on my darling!",
     "Сиэста тоже имеет право любить. Но хватать моего дорогого — храбрости ей не занимать!"),
177: ("Who said she's your lover? My familiar can do what she likes, but I absolutely refuse to hand her over to you!",
     "Кто сказал, что она твоя возлюбленная? Мой фамильяр вправе делать что хочет, но отдать её тебе — никогда!"),
178: ("Oh? Could it be, Louise, that you're in love with your familiar?",
     "О? Неужто, Луиза, ты влюблена в своего фамильяра?"),
179: ("Wha—! What are you suddenly saying, Kirche! And with a commoner like Saito...!",
     "Ах! Что ты вдруг несёшь, Кирке! И с каким-то простолюдином, как Сайто…!"),
180: ("Then I don't mind taking him myself.", "Тогда я не против забрать его себе."),
181: ("Ugh.", "Ох."),
182: ("Perfect. Let's have a real contest over who's worthy of darling, shall we?",
     "Отлично. Давайте по-настоящему выясним, кто достоин дорогого, да?"),
183: ("Gladly, Kirche. On the name of La Valliere, I will never give you Saito!",
     "С удовольствием, Кирке. Именем Ла Вальер я никогда не отдам тебе Сайто!"),
184: ("You two, why are you getting so bloodshot over this? Hey—take a look at your faces in a mirror sometime.",
     "Вы двое, почему вы так разошлись? Эй — посмотрите как-нибудь на свои лица в зеркало."),
185: ("It's all right, Hiraga-kun. Siesta can't use magic, either. I can try a little, too, can't I?",
     "Всё хорошо, Хирага-кун. Сиэста же не умеет колдовать. И я могу немного постараться, правда?"),
186: ("No, Haruna. Not you too.", "Нет, Харуна. Не ты ли."),
187: ("Heh heh, of course Tabitha's joining, too, right?", "Хи-хи, Табаса, конечно, тоже участвует, да?"),
188: ("I'll join.", "Присоединюсь."),
189: ("I keep telling you—it's not like that! Won't any of you listen to me!? Hey, are you even listening~!?",
     "Я же говорю — всё не так! Неужели никто меня не послушает!? Эй, вы вообще слушаете~!?"),
190: ("Haa... Well, do your best, then.", "Хаа… Ну, тогда постарайтесь."),
191: ("Really, Montmorency. Let's talk about love ourselves, shall we?",
     "Правда, Монморанси. Давай и мы поговорим о любви, да?"),
192: ("Not interested!", "Не интересно!"),
193: ("You're kidding...", "Не может быть…"),
194: ("Well, now that that's settled, let's go declare war on Siesta, shall we? "
     "Desertion before the enemy is punishable by death!",
     "Ну, раз вопрос решён, идём объявить Сиэсте войну, да? "
     "Дезертирство перед врагом карается смертью!"),
195: ("Gladly. I'll make you regret it, absolutely.", "С удовольствием. Я заставлю тебя пожалеть, честно."),
196: ("I won't forget those words. Heh heh, things are getting fun.",
     "Я не забуду эти слова. Хи-хи, становится весело."),
197: ("Whoaaa! Someone, listen to me~!!", "О-о-о! Кто-нибудь, послушайте меня~!!"),
198: ("Just what do you intend to do, Kirche?", "Что ты собираешься делать, Кирке?"),
199: ("Ever since she started working as Louise's maid, she's finally been doing better. "
      "Leave Siesta alone.", "С тех пор как она стала горничной Луизы, дела у неё наконец пошли хорошо. "
      "Оставь Сиэсту в покое."),
200: ("Hmm... I might consider it, if darling agrees to live with me from now on, forever?",
     "Хм… Я бы подумала, если бы дорогой согласился жить со мной всегда, вечно?"),
201: ("T-That's...! If we did that...", "Т-Это…! Если так сделать…"),
202: ("Oh, don't worry. I've reserved the empty lot behind the academy building "
      "as your eternal resting place.", "О, не волнуйся. Я зарезервировала пустырь за зданием академии "
      "для твоего вечного упокоения."),
203: ("Just calm down a little, Louise. Siesta is serving you and trying to start over, isn't she?",
     "Успокойся хоть немного, Луиза. Сиэста же прислуживает тебе и пытается начать сначала, да?"),
204: ("I don't care about Siesta!", "Мне нет дела до Сиэсты!"),
205: ("Eh.", "А."),
206: ("Zerbst picked a fight with us, didn't she? I have to answer with victory!",
     "Церпст бросила нам вызов, да? Я должна ответить победой!"),
207: ("Come on, it's not like you have to take it that seriously...", "Ну, не обязательно принимать это так близко…"),
208: ("Please, Tabitha! Help me talk some sense into them!", "Прошу тебя, Табаса! Помоги мне их уговорить!"),
209: ("Coward.", "Трус."),
210: ("Oof... That's cold...", "Ой… Это больно…"),
211: ("(Looks like this is going to get really ugly over Siesta for a while.)",
     "Похоже, из-за Сиэсты здесь надолго начнётся настоящий раздор."),
212: ("Siesta. I'm back.", "Сиэста. Я вернулась."),
213: ("Ah, welcome back.", "Ах, с возвращением."),
214: ("Eh...? Are you all here, too? What happened?", "А…? Вы все тоже здесь? Что случилось?"),
215: ("We have business with you.", "У нас к тебе дело."),
216: ("Yes? What business would that be?", "Да? Какое дело?"),
217: ("Heh heh, Siesta? Bet Saito against us and fight us fair and square!",
     "Хи-хи, Сиэста? Поставь Сайто на кон и сражайся с нами честно!"),
218: ("Y-Yes!? Um, what do you mean by that?", "Д-Да!? Э-Э, что это значит?"),
219: ("Have I done something rude...? I-I'm just a village girl... I can't fight all of you...",
     "Я что-то не так сделала…? Я-Я всего лишь деревенская девушка… Я не могу сразиться со всеми вами…"),
220: ("It's fine, Siesta. It's a fight between girls, after all.",
     "Всё хорошо, Сиэста. Это же девичье состязание."),
221: ("A fight between girls...", "Девичье состязание…"),
222: ("For some reason, everyone here wants to bet me and compete with Siesta...",
     "Почему-то все здесь захотели поставить меня на кон и посоревноваться с Сиэстой…"),
223: ("I tried to stop them, but...", "Я пытался их остановить, но…"),
224: ("I-I see...", "Т-Так вот как…"),
225: ("All right. If it's over Saito-san, I'll accept that fight.",
     "Ладно. Если ставка — Сайто-сан, я приму это состязание."),
226: ("If I win this, I can openly be with Saito-san, right!",
     "Если я выиграю, я смогу открыто быть с Сайто-саном, да!"),
227: ("Why would it mean that!?", "Почему это должно что-то значить!?"),
228: ("So, what's the contest going to be? The important part.", "Так, а в чём будет состязание? Главное."),
229: ("No, would you all stop taking this so seriously!", "Нет, неужели вы не можете не принимать это так серьёзно!"),
230: ("Hmm, let me think... Something Siesta could do even without magic...",
     "Хм, подумаем… Что-то, что Сиэста может делать даже без магии…"),
231: ("All I can do is maid work. Cooking and such...", "Я умею только работу горничной. Готовить и тому подобное…"),
232: ("Oh, that's perfect, isn't it?", "О, это же идеально, правда?"),
233: ("Eh?", "А?"),
234: ("It's decided! The contest is a cooking battle of our proudest dishes!",
     "Решено! Состязание — кулинарный бой лучших блюд!"),
235: ("What was that!?", "Что ты сказала!?"),
236: ("Then I might be able to manage something, too.", "Тогда и я, возможно, смогу что-то сделать."),
237: ("A cooking battle... Kirche, are you serious!?", "Кулинарный бой… Кирке, ты серьёзно!?"),
238: ("Of course... I never go back on my word.", "Конечно… Я не отступаю от своих слов."),
239: ("Not bad.", "Неплохо."),
240: ("A cooking battle, huh...", "Кулинарный бой, значит…"),
241: ("Say, Louise. Does a stomach medicine exist in this world?",
     "Слушай, Луиза. Существует ли в этом мире лекарство для желудка?"),
242: ("Icho-yaku? What's that?", "Итё-яку? Что это?"),
243: ("Ah, it's medicine you take when your stomach's off from eating something strange or too much.",
     "А, это лекарство, которое пьют, когда желудок расстроился от странной еды или переедания."),
244: ("Something strange? Are you saying the food I cook is strange!?",
     "Странной? Ты хочешь сказать, что моя стряпня странная!?"),
245: ("N-No, I didn't mean it that way!", "Н-Нет, я не это имел в виду!"),
246: ("If it's a cooking battle, Siesta's specialty, huh!", "Если кулинарный бой, то это стихия Сиэсты, да!"),
247: ("Yes! I help cook everyone's meals every day, so I'm a little confident!",
     "Да! Я каждый день помогаю готовить еду для всех, так что немного уверенности у меня есть!"),
248: ("Heh heh, that's what makes it worth it. I'll show you what I can do, so be ready!",
     "Хи-хи, вот это и интересно. Я покажу тебе, на что способна, так что будь готова!"),
249: ("I-I won't let you win for free, either!", "Я-Я тоже не дам тебе победить просто так!"),
250: ("And what does that mean?", "А это что значит?"),
251: ("Hehe... Maybe I'll look for a dish that'll surprise Hiraga-kun, too?",
     "Хи-хи… Может, и я найду блюдо, которое удивит Хирага-куна?"),
252: ("I'm getting so motivated! Please look forward to it, Saito-san!!",
     "У меня появилось столько рвения! Ждите с нетерпением, Сайто-сан!!"),
253: ("Ah, do your best, Siesta!!", "Ах, постарайся, Сиэста!!"),
254: ("Hehe... Yes!", "Хи-хи… Да!"),
255: ("Overruled! I choose the swimsuit contest! I'm sure everyone agrees with me!",
     "Отклонено! Я выбираю конкурс купальников! Уверен, все со мной согласны!"),
256: ("...", "…"),
257: ("Hey, why did swimsuits come into this?", "Эй, почему тут вообще купальники?"),
258: ("The worst.", "Ужасно."),
259: ("Sorry, I got carried away. Forgive me.", "Простите, я зарвался. Прошу прощения."),
260: ("If you want to see that badly, come to my room later.",
     "Если тебе так хочется смотреть, заходи ко мне в комнату позже."),
261: ("I'll show you all sorts of things. Not just swimsuits, either.",
     "Я покажу тебе всякое. Не только купальники."),
262: ("All sorts! What do you mean, all sorts!?", "Всякое! Что значит «всякое»!?"),
263: ("Saito... Which would you prefer, the whip or the collar?",
     "Сайто… что ты предпочтёшь — кнут или ошейник?"),
264: ("No, thank you. I'll pass.", "Нет, спасибо. Я воздержусь."),
}
CHOICES = {
781: [("What are you planning, Kirche?", "Что ты задумала, Кирке?"),
      ("Calm down, Louise", "Успокойся, Луиза"),
      ("Help me, Tabitha", "Помоги мне, Табаса")],
786: [("Does stomach medicine exist here?", "Существует ли здесь лекарство для желудка?"),
      ("It's Siesta's specialty", "Это стихия Сиэсты"),
      ("I'd rather judge swimsuits", "Я бы лучше судил купальники")],
}
SPK = {'サイト': 's', 'ルイズ': 'l', 'キュルケ': 'k', 'シエスタ': 'si', 'ギーシュ': 'g',
       'モンモランシー': 'm', 'ハルナ': 'ha', 'タバサ': 't', 'null': 'th'}
START = {'s': 55, 'l': 33, 'k': 6, 'si': 36, 'g': 6, 'm': 7, 'ha': 2, 't': 3, 'th': 0}


def main():
    data = json.load(open('reports/ch21/parse_771_805.json', encoding='utf-8'))
    script = ['# Глава 21, часть 2 (сцены 780–789): любовное смятение, кулинарный бой.',
              '# Источник: ps2_source/chapters/chapter_22_サイトのメイド.txt (SCENE 780-789).',
              '', 'label ch21_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 789:
                break
            if x['no'] < 780:
                continue
            scene = x['no']
            script += ['label ch21_2_scene_%d:' % scene, '']
            continue
        if k == 'event':
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
                ctext = '%s{#ch21_2_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch21_2_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 780 <= scene <= 789:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch21_2_scene_%d' % x['target']
                                          if 780 <= x['target'] <= 789 else 'ch21_3'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 2 ====', '    jump ch21_3', '    return', '']
    files = {
        'game/chapters/21/script-ch21_2.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch21_2_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch21_2_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch21_2_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch21_2_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch21/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
