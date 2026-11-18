#!/usr/bin/env python3
"""Chapter 22 part 2 (scenes 817-823): cooking inspection, Kirche's drink."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
104: ("A while has passed since cooking began, but everyone's serious. Let me go take a look.",
      "Прошло немало времени с начала готовки, но все серьёзно. Схожу посмотрю."),
105: ("Kirche first. Gah! What's that!?", "Сначала Кирке. Ах! Что это!?"),
106: ("(Kirche is squeezing the meat out of some glossy black creature, extracting a purple, "
      "thick liquid.)", "Кирке выжимает мясо из какой-то блестящей чёрной твари и "
      "добывает пурпурную густую жидкость."),
107: ("(It looks awful... Can you even eat that? Wait—am I the one eating it?)",
      "На вид жутко… Это вообще съедобно? Погоди — это мне придётся это есть?"),
108: ("Hum hum hum...", "Хм-хм-хм…"),
109: ("K-Kirche-san?", "К-Кирке-сан?"),
110: ("Oh, darling. Couldn't wait? Heh, just a little longer.",
      "О, дорогой. Не смог дождаться? Хи, ещё немного."),
111: ("I'll feed you something delicious you'll never forget.",
      "Я накормлю тебя чем-то таким вкусным, что ты никогда не забудешь."),
112: ("N-No, I'm looking forward to it, but... that purple liquid... what is it?",
      "Н-Нет, я жду с нетерпением, но… эта пурпурная жидкость… что это?"),
113: ("It's a secret. More secrets make things more fun, don't they? "
      "Both cooking and... men and women, right?", "Это секрет. Чем больше секретов, тем веселее, "
      "правда? И готовка, и… мужчины с женщинами, да?"),
114: ("(Whoa, I'm getting worried now...)", "Ого, я начинаю волноваться…"),
115: ("(Next is Louise.)", "Дальше Луиза."),
116: ("Hi-yah! Ta-yah! Toooh!", "Хия! Тая! Т-о-о-о!"),
117: ("Whoa!", "Ой!"),
118: ("Huh? I seems I sent the knife flying somewhere.", "А? Кажется, я уронила нож."),
119: ("T-That knife grazed my neck and is stuck in the pillar over there...!",
      "Т-Тот нож задел мою шею и воткнулся в колонну напротив…!"),
120: ("Oh, Saito. What's wrong?", "О, Сайто. Что случилось?"),
121: ("What do you mean 'what's wrong'!? Swinging a knife around is dangerous! "
      "I nearly got stabbed!", "Это что значит «что случилось»!? Размахивать ножом опасно! "
      "Я чуть не пострадал!"),
122: ("S-Shut up. As long as the ingredients are cut properly, it's fine. See?",
      "З-Замолчи. Лишь бы ингредиенты были нарезаны как надо. Смотри?"),
123: ("Ah, you're right. The julienne's nice.", "А, верно. Нарезка тонкая, красиво."),
124: ("Heh heh~. Right?", "Хи-хи~. Да?"),
125: ("Now that you've seen, go away! You're in the way! I-I get nervous when people watch!",
      "Раз увидел, уходи! Ты мешаешь! Я-Я волнуюсь, когда на меня смотрят!"),
126: ("Yes, yes.", "Да-да."),
127: ("(Next is Siesta.)", "Дальше Сиэста."),
128: ("......", "……"),
129: ("(Siesta... She looks so serious...)", "Сиэста… У неё такое серьёзное лицо…"),
130: ("Ah, that looks good. Just a tiny bite.", "А, это выглядит вкусно. Совсем чуть-чуть."),
131: ("No!", "Нельзя!"),
132: ("Ouch.", "Ой."),
133: ("Sneaking bites is bad manners, you know.", "Красться к еде — дурной тон, знаете."),
134: ("Ha ha... It just looked so tasty, I couldn't help it.", "Ха-ха… Выглядело так вкусно, я не удержался."),
135: ("It'll be ready soon, so please wait over there. ...Wait.", "Скоро всё будет готово, так что подождите там. …Погоди."),
136: ("Hmm? What's wrong? Your face is bright red.", "Хм? Что случилось? У тебя лицо всё красное."),
137: ("N-No, I... Um, when I say things like this, it's just like... Um, that...",
      "Н-Нет, я… Э-Э, когда я так говорю, это прямо как… Э-Э, как будто…"),
138: ("Like what?", "Как будто — что?"),
139: ("L-Like a newlywed couple! I'm the wife and Saito-san is... the husband... or something!",
      "Будто молодожёны! Я — жена, а Сайто-сан —… муж… или что-то в этом роде!"),
140: ("W-What was that!?", "Ч-Что ты сказала!?"),
141: ("I-I said it... S-Sorry. I said something strange...",
      "Я-Я сказала… П-Простите. Я сказала глупость…"),
142: ("I-It's fine! It's fine! I-It's really fine!", "Н-Нормально! Всё нормально! Я-Я не против!"),
143: ("...", "…"),
144: ("...", "…"),
145: ("Whoa!", "Ой!"),
146: ("...", "…"),
147: ("Kyaa! Why did the knife fly at me!? Saito-san, are you all right!?",
      "Кья! Почему нож полетел в меня!? Сайто-сан, вы в порядке!?"),
148: ("Somehow... It only grazed my neck, it seems... This knife is...",
      "Как-то… Кажется, только задела шею… Этот нож…"),
149: ("Oh my, I sent the knife flying again.", "Ох, я опять упустила нож."),
150: ("So it was you! You did it on purpose, didn't you!", "Так это ты! Ты специально, да!"),
151: ("Surely not? My hand just slipped.", "Конечно нет? Рука просто сорвалась."),
152: ("I-Is that so.", "Т-Так ли."),
153: ("...What a shame.", "…Жаль."),
154: ("D-Did you say something!?", "Т-Ты что-то сказала!?"),
155: ("Nothing. Ah, I'm busy, busy.", "Ничего. Ах, я занята, занята."),
156: ("W-Well, I'll be going, then. I feel my life is in danger.",
      "Н-Ну, я пойду. Я чувствую угрозу жизни."),
157: ("Y-Yes, that's right. Saito-san, please look forward to it.",
      "Д-Да, верно. Сайто-сан, ждите с нетерпением."),
158: ("Ah, of course!", "Ах, конечно!"),
159: ("(...Huh? What's Haruna doing? It looks like she's cutting a cucumber monster...)",
      "…А? Что делает Харуна? Кажется, она режет огуречного монстра…"),
160: ("Why does it keep growing back no matter how much I cut it? How am I supposed to slice this?",
      "Почему оно снова становится целым, сколько ни режь? Как это нарезать?"),
161: ("(...Is that really a vegetable? Or something that shouldn't exist in this world...)",
      "…Это и правда овощ? Или что-то, чего не должно быть в этом мире…"),
162: ("Eeeh!! Ugh... How am I supposed to cut an exploding tomato... mmph.",
      "И-ик!! Ох… Как резать взрывающийся помидор… м-м-м."),
163: ("Burdock like konjac... cabbage like plastic... How do they eat these in this world...?",
      "Лопух как коньяк… капуста как пластик… Как это едят в этом мире…?"),
164: ("(She's struggling with unfamiliar ingredients, after all.)",
      "Она и правда мучается с незнакомыми ингредиентами."),
165: ("(And Tabitha...)", "А Табаса…"),
166: ("...", "…"),
167: ("...", "…"),
168: ("...", "…"),
169: ("(She seems to be reading the whole time... Is she really all right?)",
      "Похоже, она всё время читает… Она точно в порядке?"),
170: ("Everyone, your technique is quite impressive, isn't it?",
      "Все вы работаете довольно искусно, правда?"),
171: ("Hmm hmm. Bridal training is going well, too, I see.", "Хм-хм. Вижу, и подготовка к свадьбе идёт хорошо."),
172: ("(All that's left is to wait patiently for the food to be done... Gaku gaku buru buru...)",
      "Осталось только спокойно дождаться готовки… Дрожь-дрожь…"),
173: ("Well then, it'll be time to finish soon.", "Ну что ж, скоро время выйдет."),
174: ("Mm.", "Мм."),
175: ("Oh, Louise. Your cooking turned out more decent than I expected.",
      "О, Луиза. Твоя стряпня вышла приличнее, чем я ожидала."),
176: ("Hmph, this much is nothing. It's easier than washing my face in the morning.",
      "Хмф, это пустяки. Легче, чем умываться по утрам."),
177: ("It may look good, but how does it taste, I wonder?", "На вид хорошо, но как на вкус, интересно?"),
178: ("Haaah... It seems I managed to make something presentable.", "Ааах… Кажется, у меня что-то вышло."),
179: ("Everyone, it looks like we managed to finish in time, didn't we?",
      "Все, похоже, мы успели закончить вовремя, да?"),
180: ("Ah, as expected—I can feel Siesta's composure as a servant. Well, naturally.",
      "Ах, как и ожидалось — в Сиэсте чувствуется выдержка прислуги. Ну, само собой."),
181: ("Hmm. Then let's start eating right away, shall we?", "Хм. Тогда начнём пробовать прямо сейчас, да?"),
182: ("To ensure fair judging, let's have the cooks draw lots for the tasting order.",
      "Чтобы судить честно, пусть повара вытянут жребий с порядком дегустации."),
183: ("All right, then. Please.", "Ну что ж. Пожалуйста."),
184: ("Heh heh, I'm number one.", "Хи-хи, я первая."),
185: ("I-I'm number two.", "Я-Я вторая."),
186: ("Number three.", "Третья."),
187: ("I'm number four.", "Я четвёртая."),
188: ("Five.", "Пять."),
189: ("(Looking at the tidy counters...)", "Глядя на аккуратные столы…"),
190: ("(Huh? On Kirche's counter there's only an empty glass. Did she fail?)",
      "А? На столе Кирке только пустой бокал. Она провалилась?"),
191: ("(On Haruna's counter there's a big bowl. The lid's closed, so I can't see inside.)",
      "На столе Харуны большая миска. Крышка закрыта, так что содержимого не видно."),
192: ("(Louise and Siesta... something stewed. Big pots with ladles stuck in them.)",
      "У Луизы и Сиэсты… что-то тушёное. Большие кастрюли с воткнутыми половниками."),
193: ("(Tabitha... a cloth over a big plate. What's under it is a complete mystery.)",
      "У Табасы… ткань на большом блюде. Что там — совершенная загадка."),
194: ("Well then, let's start with Miss Zerbst's dish.", "Ну что ж, начнём с блюда мисс Церпст."),
195: ("Understood, Mr. Colbert.", "Понятно, Кольбер-сэн."),
196: ("(Well, here we go...)", "Ну, поехали…"),
197: ("Everyone, please take a glass. I've prepared a special drink, ordered for this very day!",
      "Все, возьмите бокалы. Я приготовила особое питьё, заказанное специально для этого дня!"),
198: ("My, my. A drink, is it?", "Ого. Питьё, значит?"),
199: ("This is perfect as an aperitif, isn't it.", "Это как раз подойдёт в качестве аперитива, да?"),
200: ("(Whoa, it looks dangerously viscous...)", "Ого, опасно густая на вид…"),
201: ("I made this drink for darling... So drink plenty, okay?", "Я сделала это питьё для дорогого… "
      "Так выпей побольше, ладно?"),
202: ("Hey, Kirche. Just what is this? This horrible-colored liquid...",
      "Эй, Кирке. Что это вообще? Эта жидкость ужасного цвета…"),
203: ("Come now, don't hold back. Help yourself.", "Ну же, не стесняйтесь. Угощайтесь."),
204: ("Why don't you try it too, Siesta? Here's a glass.", "Попробуй и ты, Сиэста. Вот бокал."),
205: ("Eh? Um... Well... Just a little! ...Gulp.", "А? Э-Э… Ну… Совсем чуть-чуть! …Глоток."),
206: ("Ugh. That's enough.", "Ох. Больше не могу."),
207: ("Eh, seriously?", "А, правда?"),
208: ("W-Well, how about tasting it myself first?", "Н-Ну, что если я сперва попробую сам?"),
209: ("Eh?", "А?"),
210: ("Did you taste it?", "Ты пробовала?"),
211: ("I-Understood!! ...Gulp.", "П-Понятно!! …Глоток."),
212: ("...Ugh.", "…Ох."),
213: ("H-Hey, Kirche, you're crouching over—are you all right?", "Э-Эй, Кирке, ты скорчилась — ты в порядке?"),
214: ("Self-destruction.", "Самоуничтожение."),
215: ("(Damn... I'm a man too!!)", "Чёрт… Я тоже мужчина!!"),
216: ("Itadakimasu!! Mom, Dad, I'm sorry! Gulping it down!", "Приятного аппетита!! Мама, папа, простите! Глоток, глоток!"),
217: ("...", "…"),
218: ("(...I can die now)", "…Я могу умереть."),
219: ("How is it, darling? Feeling energized?", "Как оно, дорогой? Чувствуешь прилив сил?"),
220: ("Impossible.", "Невозможно."),
221: ("Wait—there's no way anyone could drink this!", "Погоди — это же нельзя пить!"),
222: ("Hmm... This taste...", "Хм… Этот вкус…"),
223: ("...", "…"),
224: ("What's with that reaction! Oh, I'm so disappointed...", "Что за реакция! Ох, я так разочарована…"),
225: ("By the way, what's it made from?", "Кстати, из чего это сделано?"),
226: ("Oh, this? It's the fresh blood of a rare animal—a 'sea lizard.'",
      "А, это? Это свежая кровь редкого зверя — «морской ящерицы»."),
227: ("You can only get a tiny amount from one, so it's incredibly precious...",
      "От одной особи берут совсем немного, так что это очень ценно…"),
228: ("R-Really?", "П-Правда?"),
229: ("Oh, Saito, you're so sloppy. If you drink this, you'll be full of energy... "
      "Especially for a man...", "Ох, Сайто, какой же ты неаккуратный. Выпей это — и будешь полон сил… "
      "Особенно мужчина…"),
230: ("Th-That's not cooking at all.", "Э-Это же не еда, а что-то другое."),
}
CHOICES = {
819: [("Have Siesta try it", "Пусть попробует Сиэста"),
      ("How about tasting it myself?", "Что если попробовать самому?"),
      ("I'll drink it!", "Я выпью!")],
}
SPK = {'サイト': 's', 'キュルケ': 'k', 'ルイズ': 'l', 'シエスタ': 'si', 'ハルナ': 'ha',
       'タバサ': 't', 'コルベール': 'c', 'オスマン': 'o', 'null': 'th'}
START = {'s': 34, 'k': 12, 'l': 21, 'si': 25, 'ha': 3, 't': 2, 'c': 2, 'o': 3, 'th': 0}


def main():
    data = json.load(open('reports/ch22/parse_806_848.json', encoding='utf-8'))
    script = ['# Глава 22, часть 2 (сцены 817–823): осмотр готовки, напиток Кирке.',
              '# Источник: ps2_source/chapters/chapter_23_料理の鉄人.txt (SCENE 817-823).',
              '', 'label ch22_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 823:
                break
            if x['no'] < 817:
                continue
            scene = x['no']
            script += ['label ch22_2_scene_%d:' % scene, '']
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
            tag = 'ch22_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch22_2_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch22_2_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 817 <= scene <= 823:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch22_2_scene_%d' % x['target']
                                          if 817 <= x['target'] <= 823 else 'ch22_3'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 2 ====', '    jump ch22_3', '    return', '']
    files = {
        'game/chapters/22/script-ch22_2.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch22_2_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch22_2_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch22_2_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch22_2_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch22/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
