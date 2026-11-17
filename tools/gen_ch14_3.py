#!/usr/bin/env python3
"""Chapter 14 part 3 (scenes 599-608): return, rescue, 'onii-chan'."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
137: ("(I shook off the pursuers and somehow made it back to the inn...)",
      "Я оторвался от преследователей и кое-как добрался до гостиницы…"),
138: ("Hey, Louise! Open up! Louise!!", "Эй, Луиза! Открой! Луиза!!"),
139: ("Who is it? Saito?", "Кто это? Сайто?"),
140: ("Y-Yeah...", "Д-Да…"),
141: ("Sa-Saito!? W-What happened to you! You're all battered!",
      "С-Сайто!? Ч-Что с тобой! Ты весь в синяках!"),
142: ("Eek! Saito-san, hold on!", "Ой! Сайто-сан, держитесь!"),
143: ("Eh!? A-Are you all right!?", "А!? Т-Ты в порядке!?"),
144: ("I'm fine... Hurry, we have to get to Kirche...!", "Я в порядке… Скорее, надо идти к Кирке…!"),
145: ("To Kirche? What happened, Saito!", "К Кирке? Что случилось, Сайто!"),
146: ("We walked into Weatherly's trap during the patrol.", "Мы попали в ловушку Уэзерби во время патруля."),
147: ("Wait, Weatherly's trap—what do you mean!?", "Подожди, ловушка Уэзерби — что это значит!?"),
148: ("Weatherly was behind the bomb-thrower we were chasing.",
      "За бомбистом, за которым мы охотились, стояла Уэзерби."),
149: ("W-What!?", "Ч-Что!?"),
150: ("Kirche must have noticed too. We were following her, but... we were spotted and led into a trap...",
      "Кирке, видимо, тоже догадалась. Мы шли за ней, но… нас заметили и заманили в ловушку…"),
151: ("...", "…"),
152: ("Why didn't you tell us something so important? We could have done something!",
      "Почему ты не рассказал нам о таком важном? Мы бы что-то сделали!"),
153: ("I'll explain later! We need to get to Kirche now... Ugh...",
      "Я объясню позже! Сейчас надо к Кирке… Ох…"),
154: ("Don't struggle! It'll make the Healing harder.", "Не дергайся! Исцеление подействует хуже."),
155: ("Please, Louise. Save Kirche!", "Прошу, Луиза. Спаси Кирке!"),
156: ("Honestly... I'd do it without being asked! Everyone, let's go!",
      "Ну же… Я и так бы сделала! Всем идём!"),
157: ("Mm.", "Мм."),
158: ("Really, Kirche, what were you thinking...!", "Ну же, Кирке, что ты задумала…!"),
159: ("(Hurry... Kirche...)", "Скорее… Кирке…"),
163: ("Damn it, Kirche, where did you go!?", "Чёрт, Кирке, куда ты делась!?"),
164: ("Hiraga-kuuun! It's Kirche-san!", "Хирага-кууун! Кирке-сан!"),
165: ("You found her!? Is she all right!?", "Вы нашли её!? Она в порядке!?"),
166: ("She was lying in the road. Badly hurt, but it looks like her life isn't in danger...",
      "Она лежала на дороге. Сильно поранена, но жизни, кажется, ничего не угрожает…"),
167: ("Damn! I should have been with her!", "Чёрт! Надо было мне быть с ней!"),
168: ("Ah, Hiraga-kun, wait!", "Ах, Хирага-кун, подожди!"),
169: ("Kirche! Are you all right!", "Кирке! Ты в порядке!"),
170: ("Relax. She's breathing. No broken bones, it seems.", "Успокойся. Она дышит. Кажется, кости целы."),
171: ("I'm healing her now, so be quiet.", "Я сейчас лечу её, поэтому помолчи."),
172: ("Thank goodness.", "Слава богу."),
173: ("Whew. I've restored her somewhat with magic, so she can move now.",
      "Фух. Я отчасти восстановил её магией, теперь она может двигаться."),
174: ("After that, we need to take her to the inn and keep her still...",
      "После этого нужно отнести её в гостиницу и обеспечить покой…"),
175: ("Mm...", "Мм…"),
176: ("Kirche! You're awake?", "Кирке! Ты проснулась?"),
177: ("No! Don't shake her...!", "Нельзя! Не тряси её…!"),
178: ("...", "…"),
179: ("...Kirche?", "…Кирке?"),
180: ("...?", "…?"),
181: ("...?", "…?"),
182: ("...?", "…?"),
183: ("...What's going on? Hey, Kirche, what's wrong with you?",
      "…Что это? Эй, Кирке, что с тобой?"),
184: ("...", "…"),
185: ("Guiche and Haruna found Kirche lying down, and Montmorency treated her.",
      "Гиш и Харуна нашли Кирке лежащей, а Монморанси её вылечила."),
186: ("Come on, let's get back to the inn and rest.", "Ну же, вернёмся в гостиницу и отдохнём."),
187: ("...", "…"),
188: ("Hey, Kirche, are you all right? Do you know me?", "Эй, Кирке, ты в порядке? Ты меня узнаёшь?"),
189: ("Big brother.", "Братишка."),
190: ("Huh?", "А?"),
191: ("Big broooother!", "Братишшаа!"),
192: ("W-Whoa! Don't hug me all of a sudden!", "О-Ого! Не обнимай меня вдруг!"),
193: ("Oh?", "О?"),
194: ("Bro-?", "Бра-?"),
195: ("-ther.", "-тишка."),
196: ("W-What was that!?", "Ч-Что это было!?"),
197: ("Come on, Kirche. Stop with the bad joke!", "Ну же, Кирке. Хватит плохих шуток!"),
198: ("Shut u...", "Заткни…"),
199: ("What? Even if you cry, I won't forgive you.", "Что? Даже если будешь плакать, я не прощу."),
200: ("Besides, chasing Weatherly without telling me is how you ended up like this...",
      "И вообще, если бы не тайком гналась за Уэзерби, не оказалась бы в таком виде…"),
201: ("Big brother. This one is scary...", "Братишка. Эта страшная…"),
202: ("H-Hey, Kirche. Don't cling to my back.", "Э-Эй, Кирке. Не висни у меня на спине."),
203: ("Saito! Since when are you Kirche's big brother!?", "Сайто! С каких пор ты брат Кирке!?"),
204: ("I-I don't know! I don't know anything!", "Я-Я не знаю! Ничего не знаю!"),
205: ("Then what's this Kirche clinging to you!?", "Тогда что это — Кирке, которая к тебе прилипла!?"),
206: ("You'll explain, won't you?", "Вы нам объясните, правда?"),
207: ("E-Explain what...", "О-Объяснить что…"),
208: ("K-Kirche is apparently my sister...", "К-Кирке, оказывается, моя сестра…"),
209: ("Big brother, I'm happy.", "Братишка, я рада."),
210: ("That can't be true!", "Так не может быть!"),
211: ("I-It's a mistake! Kirche my sister, really—it can't be!",
      "Т-Это недоразумение! Кирке моя сестра — не может быть!"),
212: ("We know that!", "Мы и так знаем!"),
213: ("Then it's a game where you make a girl call you 'big brother'?",
      "Значит, это игра, в которой ты заставляешь девушку называть себя «братишкой»?"),
214: ("If so, you could have told me. I'd call you 'big brother' anytime...",
      "Если так, ты мог бы сказать мне. Я бы назвала тебя «братишкой» когда угодно…"),
215: ("W-Wait! I have no 'little sister' attribute!", "П-Подожди! У меня нет атрибута младшей сестры!"),
216: ("This feeling Kirche is giving me must be my imagination!",
      "Это чувство, которое Кирке у меня вызывает, — только воображение!"),
217: ("You all misheard.", "Вы все ослышались."),
218: ("Big brother. Big brother.", "Братишка. Братишка."),
219: ("U-Ugh. Kirche, when you call me that with such innocent eyes...",
      "О-Ох. Кирке, когда ты называешь меня так с такими невинными глазами…"),
220: ("Ufufu... Saito, you seem to hear it just fine.", "Уф-фу… Сайто, ты, кажется, отлично слышишь."),
221: ("Ugh. So it wasn't a hallucination!", "Ох. Так это не галлюцинация!"),
222: ("Wait, Louise. I don't understand any of this either.", "Подожди, Луиза. Я сам ничего не понимаю."),
223: ("You're just trying to dodge the question...", "Ты просто хочешь уйти от ответа…"),
224: ("E-Eek!", "Ч-Чёрт!"),
225: ("Stop it, you two!", "Прекратите, вы двое!"),
226: ("I don't understand either, but Kirche is frightened, isn't she!?",
      "Я тоже ничего не понимаю, но Кирке же напугана!"),
227: ("That's right.", "Верно."),
228: ("...", "…"),
229: ("There, there.", "Ну-ну, всё хорошо."),
230: ("W-What is this? It's like I'm the bad one...", "Ч-Что это? Получается, я плохая…"),
231: ("O-Onii-chan. Don't be mean to me...", "Б-Братишка. Не обижай меня…"),
232: ("...Ugh.", "…Ох."),
233: ("...Say, Montmon. What's wrong with Kirche?", "…Слушай, Монмон. Что с Кирке?"),
234: ("I-I'm checking now, wait a moment!", "Я-Я сейчас проверю, подожди!"),
}
CHOICES = {
604: [("Kirche apparently is my sister", "Кирке, оказывается, моя сестра"),
      ("It must be a mistake", "Это должно быть недоразумение"),
      ("Did everyone mishear?", "Все ослышались?")],
}
MOVES = [("Corridor", "Коридор", "廊下"),
         ("The main street", "Главная улица", "表通り"),
         ("The back alley", "Задний переулок", "裏通り")]
SPK = {'サイト': 's', 'ルイズ': 'l', 'シエスタ': 'si', 'モンモランシー': 'm',
       'タバサ': 't', 'ハルナ': 'ha', 'キュルケ': 'k', 'null': 'th'}
START = {'s': 75, 'k': 70, 'l': 5, 'si': 0, 'm': 0, 't': 0, 'ha': 0, 'th': 2}


def main():
    data = json.load(open('reports/ch14/parse_578_619.json', encoding='utf-8'))
    script = ['# Глава 14, часть 3 (сцены 599–608): возвращение, спасение Кирке, «братишка».',
              '# Источник: ps2_source/chapters/chapter_15_私のお兄ちゃん.txt (SCENE 599-608).',
              '', 'label ch14_3:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if not 599 <= x['no'] <= 608:
                continue
            scene = x['no']
            script += ['label ch14_3_scene_%d:' % scene, '']
            continue
        if k == 'event':
            if scene:
                event(x['src'], script)
            continue
        if k == 'dlg':
            idx = x['idx']
            if 160 <= idx <= 162:
                continue
            if scene in (600, 601, 602, 603):
                continue
            if idx not in T:
                continue
            en, ru = T[idx]
            if en is None:
                script.append('    # ' + x['src'] + ' (no voice)')
                continue
            en = en_norm(en)
            spk = SPK.get(x['speaker'], 'th')
            counters[spk] += 1
            tag = 'ch14_%s_%03d' % (spk, counters[spk])
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
            if idx == 159:
                script.append('    # 【移動】 → extra 1489/1490/1491')
                script.append('    menu:')
                for i, (en_m, ru_m, ja_m) in enumerate(MOVES):
                    ctext = '%s{#ch14_3_c_599_%d}' % (en_norm(en_m), i + 1)
                    script.append('        "%s":' % ctext)
                    script.append('            jump ch14_4_scene_%d' % (1489 + i))
                    ja_c += ['    old "%s"' % ctext, '    new "%s"' % ja_m, '']
                    ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru_m, '']
                script.append('')
            continue
        if k == 'choice':
            if scene is None or scene not in CHOICES:
                continue
            script.append('    menu:')
            for i, o in enumerate(x['options']):
                en, ru = CHOICES[scene][i]
                ctext = '%s{#ch14_3_c_%d_%d}' % (en_norm(en), scene, i + 1)
                tgt = ('ch14_3_scene_%d' % o['target']
                       if 599 <= o['target'] <= 608 else 'ch14_4')
                script.append('        "%s":' % ctext)
                script.append('            jump %s' % tgt)
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene in (600, 601, 602, 603):
                continue
            tgt = ('ch14_3_scene_%d' % x['target']
                   if 599 <= x['target'] <= 608 else 'ch14_4')
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % tgt)
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 3 ====', '    jump ch14_4', '    return', '']
    files = {
        'game/chapters/14/script-ch14_3.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch14_3_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch14_3_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch14_3_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch14_3_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch14/voice_map_3.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
