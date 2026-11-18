#!/usr/bin/env python3
"""Chapter 19 part 2 (scenes 750-763): kiss, illusion fleet, Weatherly."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
126: ("So, everyone knows the plan, right?", "Итак, все помнят план?"),
127: ("First, Louise and Kirche head for the rooftop... Right?",
      "Сначала Луиза и Кирке идут на крышу… Верно?"),
128: ("Right. You and Tabitha make your way to the headmaster's office, making " 
      "sure you're noticed.", "Верно. С Табасой идёшь к кабинету директора и "
      "стараешься привлечь к себе внимание."),
129: ("To draw Weatherly's attention our way, yeah?", "Чтобы отвлечь Уэзерби на нас, да?"),
130: ("And I'll use that spell. It should throw the enemies in the academy into confusion.",
      "А я применю то заклинание. Оно должно внести замешательство во врагов в академии."),
131: ("You'll use the confusion to restrain Weatherly and Akina.",
      "А ты воспользуешься замешательством и задержишь Уэзерби и Акину."),
132: ("Hey, what is that spell?", "Эй, а что это за заклинание?"),
133: ("It's a secret.", "Это секрет."),
134: ("What kind of secret?", "Что за секрет?"),
135: ("Obviously. To deceive the enemy, you first deceive your allies. Anyone could be listening.",
      "Само собой. Чтобы обмануть врага, сперва обмани союзников. Мало ли кто слушает."),
136: ("We won't fail either—but you two can't afford to fail.",
      "Мы не ошибёмся, но и вы двое не имеете права на ошибку."),
137: ("We have to save both the academy and Haruna.",
      "Нам нужно спасти и академию, и Харуну."),
138: ("Heavy responsibility.", "Большая ответственность."),
139: ("All right, let's go.", "Ладно, пошли."),
140: ("Mm.", "Мм."),
141: ("U-Um... Wait, Saito.", "Э-Э… Подожди, Сайто."),
142: ("What is it? Anything left undecided? Something you don't understand?",
      "Что? Осталось что-то неоговорённое? Что-то непонятное?"),
143: ("T-That is... Are you all right?", "Т-То есть… Ты в порядке?"),
144: ("Huh?", "А?"),
145: ("W-We only have to reach the rooftop...", "Н-Нам всего-то нужно дойти до крыши…"),
146: ("If the spell works, we can just hide somewhere afterwards.",
      "Если заклинание сработает, потом можно спрятаться где-нибудь."),
147: ("But you and Tabitha have to fight Reconquista's soldiers and Weatherly, don't you?",
      "А вам с Табасой придётся сражаться с солдатами Реконкисты и Уэзерби, да?"),
148: ("I mean, Tabitha's there, and there's Derflinger too... But still...",
      "Ну, Табаса рядом, и Дерфлингер есть… Но всё равно…"),
149: ("Don't worry. Leave it to me.", "Не волнуйся. Положись на меня."),
150: ("Don't act cool and get yourself hurt. You're always missing the important point...",
      "Не рисуйся, а то пострадаешь. Ты всегда упускаешь главное…"),
151: ("I really am worried.", "Я правда волнуюсь."),
152: ("What's that? Don't you trust me? That hurts a little.",
      "Что это? Ты мне не доверяешь? Мне немного обидно."),
153: ("N-No, that's not it... I do trust you, I just...", "Н-Нет, не то… Я же не то чтобы не доверяю… просто…"),
154: ("Oh, Louise. Are you worried about darling?", "О, Луиза. Неужто ты волнуешься за дорогого?"),
155: ("W-What... It's only natural to worry about your own familiar.",
      "Ч-Что… Волноваться за своего фамильяра — ничего дурного, правда?"),
156: ("What are you talking about, Louise? I'm more worried about you.",
      "Что ты говоришь, Луиза? Я больше волнуюсь за тебя."),
157: ("Wh-What are you saying to your mistress, you familiar!",
      "Т-Ты это что говоришь госпоже, фамильяр!"),
158: ("Oh, Louise. Are you a little happy that darling is worrying about you?",
      "О, Луиза. Ты немного рада, что дорогой волнуется за тебя?"),
159: ("Agitation.", "Волнение."),
160: ("N-No I'm not! Just because the master showed a little concern for his familiar "
      "doesn't mean I'm pleased!", "Н-Нет! Просто госпожа немного позаботилась о "
      "фамильяре — и это не значит, что я довольна!"),
161: ("It'll be fine. I'm sure we'll manage somehow.", "Всё будет хорошо. Я уверен, мы как-нибудь справимся."),
162: ("Why are you so casual about it? You're always like this...",
      "Почему ты так легко ко всему относишься? Ты всегда такой…"),
163: ("After all, I'm the legendary familiar Gandalfr, right?",
      "В конце концов, я же легендарный фамильяр Гандальф, да?"),
164: ("The weapon that suits me best, and it absorbs enemy magic too. "
      "I won't go down that easily.",
      "Оружие, которое мне больше всего подходит, к тому же оно поглощает магию врага. "
      "Меня так просто не одолеть."),
165: ("Hey now, that's nice to hear. I'll be fired up today, you bet.",
      "Эй, приятно слышать. Сегодня я постараюсь на славу."),
166: ("Today—come on, be fired up every day...", "Сегодня — давай хоть каждый день старался…"),
167: ("What is it? You think you can do everything on your own?",
      "Что? Думаешь, ты один можешь всё?"),
168: ("L-Louise?", "Л-Луиза?"),
169: ("You're a familiar, yet you always ignore me and run off on your own, "
      "and then you get into danger...", "Ты фамильяр, но вечно игнорируешь меня и "
      "бежишь один, а потом попадаешь в опасность…"),
170: ("Honestly, you're such an idiot!", "Правда, ты полный дурак!"),
171: ("You, you...!", "Ты, ты…!"),
172: ("W-Wah!?", "О-Ой!?"),
173: ("Oh my.", "Ох."),
174: ("...", "…"),
175: ("(E-Er... Something soft just touched my lips...)",
      "Э-Э… Кажется, что-то мягкое коснулось моих губ…"),
176: ("Mm...", "Мм…"),
177: ("(Could this be it? Am I being kissed by Louise?)",
      "Неужто это то самое? Луиза меня поцеловала?"),
178: ("E-Eh? You... You kissed me...!?", "А-А? Ты… Ты меня поцеловала…!?"),
179: ("T-That was... This was...! D-Don't get the wrong idea!",
      "Т-То было… Это было…! К-Ка-ка-ка-ка… Н-Не подумай чего!"),
180: ("You really never listen to your mistress...", "Ты и правда никогда не слушаешь госпожу…"),
181: ("You always ignore my feelings!", "Ты вечно игнорируешь мои чувства!"),
182: ("I just renewed the contract so that you'd listen to me properly! "
      "That's it—a contract, a contract!!", "Я просто обновила договор, чтобы ты "
      "слушался! Вот и всё — договор, договор!!"),
183: ("Contract.", "Договор."),
184: ("Contract, is it... Hmm.", "Договор… Хм."),
185: ("Not a summoning contract. It's a contract that you'll come back properly!",
      "Не договор призыва. Это договор, что ты вернёшься как положено!"),
186: ("Well, let's leave it at that. Right, darling?", "Ну, пусть будет так. Да, дорогой?"),
187: ("...", "…"),
188: ("(No good. My heart started pounding now of all times. A kiss, huh...)",
      "Плохо. Сердце заколотилось именно сейчас. Поцелуй, однако…"),
189: ("Saito, your face is bright red.", "Сайто, у тебя лицо прямо красное."),
190: ("Ooh, you're young, partner. But the rest comes after the operation.",
      "О-о, ты молод, приятель. Но продолжение — после операции."),
191: ("A-Ah. I know.", "А-А. Знаю."),
192: ("L-Let's go, Kirche.", "И-Идём, Кирке."),
193: ("Yes, yes. See you later, darling, Tabitha.", "Да-да. До встречи, дорогой, Табаса."),
194: ("You're a naughty familiar who doesn't listen to your mistress!",
      "Ты дерзкий непослушный фамильяр, который не слушает госпожу!"),
195: ("So once the academy is back to normal and the capital is saved, "
      "I'm going to re-educate you, absolutely!", "Так что когда академия вернётся "
      "в норму и столица будет спасена, я тебя непременно перевоспитаю!"),
196: ("So until then, don't get yourself hurt!", "Так что до тех пор не пострадай!"),
197: ("Got it? If you break even one of my orders, it's punishment!",
      "Понял? Нарушишь хоть одно моё указание — будет наказание!"),
198: ("O-Oh... Got it.", "О-О… Понял."),
199: ("As long as you understand. Don't ever forget those words. Let's go, Kirche.",
      "Лишь бы ты понял. Никогда не забывай эти слова. Идём, Кирке."),
200: ("Yes, yes. Well... thanks for the meal.", "Да-да. Ну… спасибо за угощение."),
201: ("Saito, let's go too.", "Сайто, и нам пора."),
202: ("O-Okay.", "У-Угу."),
203: ("See you, Tabitha.", "До встречи, Табаса."),
204: ("(Gulp)", "Глоток"),
205: ("This way.", "Сюда."),
206: ("O-Okay.", "О-Ок."),
207: ("(I wonder if Louise is all right...)", "Интересно, Луиза в порядке…"),
208: ("Hey, Louise?", "Эй, Луиза?"),
209: ("W-What now?", "Ч-Что ещё?"),
210: ("That thing earlier... were you serious?", "То, что было раньше… ты серьёзно?"),
211: ("Eh... What thing?", "А… Что именно?"),
212: ("Don't play dumb. You kissed Saito, didn't you?",
      "Не притворяйся. Ты поцеловала Сайто, правда?"),
213: ("Ugh.", "Ох."),
214: ("I can't believe a noble—and the daughter of a Valliere, no less—doing that "
      "to a commoner...", "Не верю, что дворянка — к тому же дочь Вальера — "
      "поцеловала простолюдина…"),
215: ("I hate to say it, but were you serious about it?",
      "Не хочу этого говорить, но ты и правда серьёзно?"),
216: ("T-That's none of your business!", "Т-Это тебя не касается!"),
217: ("It does concern me. Saito is my darling, after all.",
      "Касается. Сайто же мой дорогой."),
218: ("D-Don't decide that on your own!", "Н-Не решай это за меня!"),
219: ("Mm, but if you're serious, I'll have to rethink my position too... "
      "So, are you serious?", "Хм, но если ты серьёзно, придётся и мне кое-что "
      "пересмотреть… Так ты серьёзно?"),
220: ("Oh, shut up, shut up!", "Ах, отстань, отстань!"),
221: ("Oh, I heard you perfectly. You declared you'd re-educate darling.",
      "О, я всё отлично слышала. Ты заявила, что перевоспитаешь дорогого."),
222: ("Poor darling, stuck with a mistress like Louise.",
      "Бедный дорогой — с такой свирепой госпожой, как Луиза."),
223: ("You know what Louise is like. She'll throw darling out of her room, "
      "skip his meals, and mistreat him.", "Ты знаешь Луизу. Выгонит дорогого из "
      "комнаты, лишит еды, будет обижать его."),
224: ("Ah, poor darling...", "Ах, бедный дорогой…"),
225: ("What... Saito is my familiar; I can do whatever I want with him!",
      "Что… Сайто мой фамильяр, я могу с ним делать что хочу!"),
226: ("Well, fine.", "Ну, ладно."),
227: ("The more you mistreat darling, the more likely he'll become only mine.",
      "Чем больше ты будешь дурно обращаться с дорогим, тем выше шанс, "
      "что он станет только моим."),
228: ("W-What!? You're a noble, flirting with a commoner—aren't you ashamed?",
      "Т-Ты что!? Дворянка, увиваешься за простолюдином — тебе не стыдно?"),
229: ("Love knows no rank. If anything, I'd even take a noble title for darling.",
      "Любовь не знает сословий. Более того, я даже готова получить дворянский "
      "титул ради дорогого."),
230: ("T-That's no good! Saito is only my familiar; you can't take him!",
      "Т-Это нельзя! Сайто только мой фамильяр, ты не можешь его забрать!"),
231: ("...", "…"),
232: ("Oh dear. You made such a fuss that the enemy gathered.",
      "Ой-ой. Ты шумела так, что враг собрался."),
233: ("What are you talking about! It's because Kirche said something strange!",
      "О чём ты! Это Кирке сказала что-то странное!"),
234: ("Enough! Everyone, finish them off!", "Хватит! Всех уничтожить!"),
235: ("Ooh, scary, scary.", "Ой, страшно, страшно."),
236: ("We managed to beat them, didn't we.", "Нам удалось их одолеть, да."),
237: ("We're short on time. Could you show us that spell of yours already?",
      "Времени мало. Не можешь ли ты уже показать своё заклинание?"),
238: ("I know.", "Знаю."),
239: ("Louise, still not ready?", "Луиза, ещё не готова?"),
240: ("I've just finished the incantation. Come forth, that which is not here... "
      "Be as though you were here.", "Я только что завершила заклинание. "
      "Появись, того, чего здесь нет… Будь так, будто ты здесь."),
241: ("Illusion!!", "Иллюзия!!"),
242: ("Wha... Such a thing!", "Что… Как это!"),
243: ("Looks like it worked.", "Похоже, получилось."),
244: ("Eh...!?", "А…!?"),
245: ("(At that moment, I doubted my own eyes. Dozens of aerial ships bearing "
      "Tristain's crest appeared in the sky in an instant.)",
      "В тот миг я не поверил своим глазам. В небе мгновенно появились десятки "
      "воздушных кораблей с гербом Тристании."),
246: ("(Louise's Void magic had succeeded perfectly.)", "Магия Пустоты Луизы "
      "сработала превосходно."),
247: ("So that's what she meant by the spell she'd use...", "Так вот что она "
      "имела в виду, говоря о заклинании…"),
248: ("As expected of Louise. She really is my mistress!", "Как и подобает Луизе. "
      "Она и правда моя госпожа!"),
249: ("We need to hurry too.", "И нам нужно поспешить."),
250: ("Right. The headmaster's office is right in front of us. Shall we go in one rush?",
      "Да. Кабинет директора уже прямо перед нами. Пойдём сразу, одним рывком?"),
251: ("Wh-What is that huge fleet! Where did so many...",
      "Ч-Что это за огромный флот! Откуда столько…"),
252: ("That's not in the data.", "Такого в данных нет."),
253: ("Weatherly-sama, the soldiers are panicking! They're leaving their posts "
      "and running around!", "Уэзерби-сама, солдаты паникуют! Покидают посты "
      "и мечутся!"),
254: ("Panicking here plays right into the enemy's hands. Tell them to "
      "restore formation at once.", "Паниковать здесь — на руку врагу. "
      "Прикажите немедленно восстановить строй."),
255: ("Yes!", "Да!"),
256: ("Who could have done this... Don't tell me Tristain has been retaken?",
      "Кто мог это сделать… Неужто Тристанию отвоевали?"),
257: ("Y-You people...!", "В-Вы это…!"),
258: ("S-Saito...!?", "С-Сайто…!?"),
259: ("Weatherly. And Akina. We've come to demand you return our academy and Haruna.",
      "Уэзерби. И Акина. Мы пришли потребовать вернуть нам академию и Харуну."),
}
CHOICES = {
751: [("Leave it to me.", "Положись на меня."),
      ("Don't you trust me?", "Ты мне не доверяешь?"),
      ("I'm more worried about you, Louise.", "Я больше волнуюсь за тебя, Луиза.")],
}
SPK = {'サイト': 's', 'ルイズ': 'l', 'キュルケ': 'k', 'タバサ': 't',
       'デルフリンガー': 'd', 'ウェザリー': 'w', 'アキナ': 'ak', '魔導士': 'mage', 'null': 'th'}
START = {'s': 285, 'l': 213, 'k': 48, 't': 33, 'd': 31, 'w': 0, 'ak': 0, 'mage': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch19/parse_739_768.json', encoding='utf-8'))
    script = ['# Глава 19, часть 2 (сцены 750–763): поцелуй, иллюзорный флот, Уэзерби.',
              '# Источник: ps2_source/chapters/chapter_20_小悪魔と春風の協奏曲.txt (SCENE 750-763).',
              '', 'label ch19_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 763:
                break
            if x['no'] < 750:
                continue
            scene = x['no']
            script += ['label ch19_2_scene_%d:' % scene, '']
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
                ctext = '%s{#ch19_2_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch19_2_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 750 <= scene <= 763:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch19_2_scene_%d' % x['target']
                                          if 750 <= x['target'] <= 763 else 'ch19_3'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 2 ====', '    jump ch19_3', '    return', '']
    files = {
        'game/chapters/19/script-ch19_2.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch19_2_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch19_2_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch19_2_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch19_2_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch19/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
