#!/usr/bin/env python3
"""Chapter 23 part 2 (scenes 868-878): at the castle, Henrietta's briefing."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
128: ("Hey, showing up at the castle so suddenly—is that all right?",
      "Эй, являться в замок так внезапно — это нормально?",),
129: ("Every second counts. I can't worry about details.", "Счёт идёт на секунды. Некогда разбираться в мелочах."),
130: ("Tabitha, thank you for bringing us this far.", "Табаса, спасибо, что довела нас сюда."),
131: ("I'm worried about the academy and Haruna. I want you to go back and help Kirche and the others.",
      "Я волнуюсь за академию и Харуну. Вернись и помоги Кирке и остальным."),
132: ("Understood.", "Понятно."),
133: ("Let's hurry, Saito!!", "Поторопимся, Сайто!!"),
134: ("(Tug tug)", "Потянул."),
135: ("Hmm?", "Хм?"),
136: ("I'll do my best.", "Постараюсь."),
137: ("Yeah, you do that.", "Да, постарайся."),
138: ("Halt! You there, charging into the palace...!", "Стой! Вы там, врываетесь во дворец…!"),
139: ("You look like students of the magic academy, but you're suspicious!",
      "Вы похожи на учеников академии магии, но вы подозрительны!"),
140: ("W-What was that!? Suspicious!? That's outrageous!!", "Ч-Что вы сказали!? Подозрительны!? Это возмутительно!!"),
141: ("O-Oh, calm down, Louise!", "О-Ой, успокойся, Луиза!"),
142: ("No! I can't stay silent! This concerns the honor of the Valliere family!",
      "Нет! Я не могу молчать! Это касается чести дома Вальер!"),
143: ("I am Louise Francoise Le Blanc de La Valliere, third daughter of the Duke of La Valliere.",
      "Я — Луиза Франсуаза Ле Блан де Ла Вальер, третья дочь герцога Ла Вальера."),
144: ("And I'm Hiraga Saito.", "А я — Хирага Сайто."),
145: ("He may look like this, but he's my familiar.", "Может, он и такой, но он мой фамильяр."),
146: ("O-Oh... My apologies! Please forgive my rudeness!", "О-Ох… Прошу прощения! Простите мою дерзость!"),
147: ("But why has a member of a ducal house come to the castle at a time like this?",
      "Но почему представитель герцогского дома прибыл в замок в такое время?"),
148: ("Honestly, why are you asking so many questions? We're in a hurry!",
      "Право, зачем вы задаёте столько вопросов? Мы же спешим!"),
149: ("Louise, calm down, I said.", "Луиза, успокойся, говорю же."),
150: ("I'll do the talking.", "Я поведу переговоры."),
151: ("Ah, wait, Saito!?", "Ах, погоди, Сайто!?"),
152: ("You there—are you the captain? Look, we want to see the princess. Could you announce us?",
      "Ты там — ты капитан? Слушай, мы хотим видеть принцессу. Можешь доложить о нас?"),
153: ("To Her Majesty? No, no! She's busy right now!", "Её Величеству? Нет-нет! Сейчас она занята!"),
154: ("Oh, that's enough! Saito, be quiet!", "Ох, хватит! Сайто, помалкивай!"),
155: ("Louise, I'll leave it to you.", "Луиза, предоставляю тебе."),
156: ("I understand.", "Понятно."),
157: ("Princess... No, I wish an audience with Her Majesty the Queen. Please announce me.",
      "Принцесса… Нет, я прошу аудиенции у Её Величества Королевы. Прошу доложить обо мне."),
158: ("Her Majesty is currently occupied with emergency deliberations. I'm sorry, but I cannot announce you.",
      "Её Величество сейчас занята экстренными совещаниями. Прошу прощения, но я не могу доложить."),
159: ("It's about that emergency that I want to see her! Never mind, just announce me!",
      "Я и хочу видеть её по поводу этого чрезвычайного положения! Неважно, просто доложи!"),
160: ("Princess~! Princess~! Come out~!", "Принцесса~! Принцесса~! Выйдите~!"),
161: ("Hey, Saito!?", "Эй, Сайто!?"),
162: ("Nu nu nu! Suspicious fellow!", "Ну-ну-ну! Подозрительный тип!"),
163: ("Honestly, you—just be quiet!", "Право, ты — просто помалкивай!"),
164: ("Honestly... I have a direct warrant from Her Majesty!", "Право… У меня есть личный указ от Её Величества!"),
165: ("This is... indeed the royal crest...", "Это… и правда королевский герб…"),
166: ("Now that you understand, announce me at once. We have no time!",
      "Раз понял, доложи немедленно. У нас нет времени!"),
167: ("Understood. Please wait here.", "Понятно. Подождите здесь."),
168: ("Say, Louise. Wouldn't it have been better to show that from the start?",
      "Слушай, Луиза. Не лучше ли было показать это сразу?"),
169: ("It's not something you flash around casually. It was supposed to be a top-secret mission.",
      "Это не то, что можно просто так показывать. Это была сверхсекретная миссия."),
170: ("Well, I suppose so.", "Ну, наверное."),
171: ("Princess! Are you safe!?", "Принцесса! Вы живы!?"),
172: ("Louise, Louise Francoise, is that you! We've been waiting for you.",
      "Луиза, Луиза Франсуаза, это вы! Мы вас ждали."),
173: ("(The people around the big table must be military and officials of high rank. "
      "The way they look at me and Louise is stern.)", "Люди вокруг большого стола — видно, военные "
      "и важные чиновники. Они смотрят на меня и Луизу сурово."),
174: ("Princess... I'm glad you're safe.", "Принцесса… Я рада, что вы в безопасности."),
175: ("To come here at such a dangerous time... Why are you always like this, Louise?",
      "Прийти сюда в такое опасное время… Почему ты всегда такая, Луиза?"),
176: ("Because I was worried about you, of course!", "Потому что я волновалась за вас, конечно!"),
177: ("Thank you, Louise. I'm grateful for your friendship.", "Спасибо, Луиза. Я благодарна за твою дружбу."),
178: ("Henrietta-sama...", "Анриетта-сама…"),
179: ("That aside, why is the castle in such an uproar? That soldier earlier was unusually tense, too.",
      "Но почему в замке такой переполох? И тот солдат прямо излучал злость."),
180: ("Yes. For precautions against the bomber, the security seems excessive to me, though...?",
      "Да. Мне кажется, меры против бомбиста слишком строгие…?"),
181: ("That's right, Louise. This whole disturbance isn't about the bomber.",
      "Верно, Луиза. Вся эта тревога не из-за бомбиста."),
182: ("Not about, you say?", "Не из-за — это как?"),
183: ("What do you mean?", "Что вы хотите сказать?"),
184: ("...", "…"),
185: ("The 'bomber' we've been treating as our enemy appears to have been merely a pawn.",
      "Тот «бомбист», которого мы считали врагом, похоже, был лишь пешкой."),
186: ("The bomber a pawn? You mean there's a mastermind?", "Бомбист — пешка? То есть есть заказчик?"),
187: ("Yes. It's because we failed to see that that this country is in its current predicament.",
      "Да. Из-за того, что мы не разглядели этого, страна оказалась в нынешнем положении."),
188: ("First, the explosions that have happened so far—we thought the bomber was detonating "
      "them without a plan.", "Во-первых, предыдущие взрывы — мы думали, что бомбист производил "
      "их без плана."),
189: ("But that wasn't so. Look at this map.", "Но это было не так. Посмотрите на эту карту."),
190: ("This is a map of Tristain and its surroundings. These marks are where the explosions occurred?",
      "Это карта Тристании и окрестностей. Эти отметки — места взрывов?"),
191: ("Yes. Looking at this, do you notice anything?", "Да. Смотрите на неё — что вы замечаете?"),
192: ("It looks like they're arranged in a circle around the castle...", "Похоже, они образуют круг вокруг замка…"),
193: ("No. They don't just look like they're surrounding it. They are surrounding it.",
      "Нет. Дело не в том, что «похоже». Они и правда окружают."),
194: ("Right now, the castle is completely encircled by the enemy's cannons.",
      "Сейчас замок со всех сторон окружён вражескими пушками."),
195: ("Cannons? Princess, what on earth do you mean?", "Пушки? Принцесса, что это значит?"),
196: ("Because the bombings kept recurring, there was a shortage of craftsmen for repairs, "
      "so workers were brought in from abroad.", "Из-за повторяющихся взрывов не хватало мастеров "
      "для ремонта, поэтому рабочих привезли из других стран."),
197: ("The enemy infiltrated agents among those craftsmen and installed gun emplacements "
      "at the repair sites.", "Враг проник туда агентами среди мастеров и установил орудия "
      "на местах ремонта."),
198: ("What!? So right now, this castle is...", "Что!? Значит, сейчас этот замок…"),
199: ("Yes. It's surrounded by enemy strongholds.", "Да. Он окружён вражескими опорными пунктами."),
200: ("They're not very active yet, but if they all move at once, the castle could even fall.",
      "Пока они не действуют активно, но если все разом начнут — замок может даже пасть."),
201: ("That's terrible... If only we'd caught the bomber before it came to this...",
      "Это ужасно… Если бы мы поймали бомбиста раньше, чем дошло до этого…"),
202: ("No, Louise.", "Нет, Луиза."),
203: ("Back then, the fact that you didn't pursue too far and avoid disaster was blessing enough.",
      "Тогда уже хорошо, что вы зашли слишком далеко, но беды не случилось."),
204: ("Princess...", "Принцесса…"),
205: ("In any case, we're attacking each battery separately now, but the situation isn't going well.",
      "Во всяком случае, сейчас мы атакуем каждую батарею по отдельности, но дела идут плохо."),
206: ("We also have to spare soldiers for evacuating the citizens... In short, we're on the defensive.",
      "Приходится выделять солдат и для эвакуации горожан… Словом, мы в отстающих."),
207: ("That's the situation for now.", "Вот такое положение дел.."),
208: ("Louise, and you, familiar. Please wait a little. I'll wrap up the deliberations now.",
      "Луиза, и ты, фамильяр. Подождите немного. Сейчас я завершу совещание."),
209: ("Understood.", "Понятно."),
210: ("(After that, the meeting dragged on. By any reckoning, the situation wasn't good. "
      "It was bound to take a long time.)", "После этого совещание затянулось. Как ни считай, "
      "ситуация была нехорошая. И оно наверняка займёт много времени."),
211: ("Understood. Then everyone, proceed as decided in the meeting.",
      "Понятно. Тогда все, действуйте по решению совещания."),
212: ("Keep casualties to a minimum. Now, dismissed.", "Потери — минимальные. На этом свободны."),
213: ("Looks like the meeting finally ended.", "Кажется, совещание наконец закончилось."),
214: ("Sorry to keep you waiting.", "Простите, что заставила ждать."),
215: ("Not at all. Rather, you look tired, Princess...", "Ничего. Скорее, вы устали, принцесса…"),
216: ("Falling for the bomber's trick, I let the enemy into the capital. It's my lack of ability...",
      "Попавшись на уловку бомбиста, я впустила врага в столицу. Это моя неспособность…"),
217: ("Princess... We're responsible, too.", "Принцесса… Мы тоже несём ответственность."),
218: ("No. You did well. I'm grateful.", "Нет. Вы хорошо постарались. Я благодарна."),
219: ("...", "…"),
220: ("The princess isn't at fault. The fault lies with the bomber and whoever's pulling his strings.",
      "Принцесса не виновата. Виноваты бомбист и тот, кто им управляет."),
221: ("Right. We'll defeat them with our own hands, somehow.", "Верно. Мы победим их своими руками, что бы ни было."),
222: ("Louise, got any good ideas? We can't go on like this, can we?",
      "Луиза, есть хорошая идея? Так дальше нельзя, да?"),
223: ("Hmm...", "Хм…"),
224: ("What are the soldiers doing? Sitting around looking important here won't help.",
      "Что делают солдаты? Сидеть тут с важным видом — толку нет."),
225: ("Saito!", "Сайто!"),
226: ("The military—down to the lowliest soldier—has done well. But given how sudden this was...",
      "Военные — вплоть до рядовых — постарались. Но учитывая, как всё внезапно началось…"),
227: ("O-Oh. I see.", "О-Ох. Понятно."),
228: ("What do you know, putting on airs!", "Что ты понимаешь, важничай — не встревай не в своё дело!"),
229: ("Got any good idea, then?", "Тогда есть хорошая идея?"),
230: ("It's not that I don't... But yes. Maybe this is the only way.",
      "Не то чтобы нет… Но да. Может, это единственный путь."),
231: ("Oh! You've thought of a plan?", "О! Придумала план?"),
232: ("Princess. There's something I must ask your forgiveness for.", "Принцесса. Я должна просить у вас прощения."),
233: ("Of me? What is it?", "У меня? Что это?"),
}
CHOICES = {
868: [("I'll do the talking", "Я поведу переговоры"),
      ("Leave it to Louise", "Поручить Луизе"),
      ("Princess~!", "Принцесса~!")],
874: [("The princess isn't to blame", "Принцесса не виновата"),
      ("Any good ideas, Louise?", "Есть идея, Луиза?"),
      ("What's the army doing?", "Что делает армия?")],
}
SPK = {'サイト': 's', 'ルイズ': 'l', 'タバサ': 't', '味方Ａ': 'soldier',
       'モンモランシー': 'm', 'キュルケ': 'k', 'アンリエッタ': 'h', 'null': 'th'}
START = {'s': 57, 'l': 21, 't': 5, 'soldier': 0, 'm': 4, 'k': 2, 'h': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch23/parse_849_893.json', encoding='utf-8'))
    script = ['# Глава 23, часть 2 (сцены 868–878): в замке, briefing Генриетты.',
              '# Источник: ps2_source/chapters/chapter_24_沈黙の応援.txt (SCENE 868-878).',
              '', 'label ch23_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 878: break
            if x['no'] < 868: continue
            scene = x['no']
            script += ['label ch23_2_scene_%d:' % scene, '']
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
                ctext = '%s{#ch23_2_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch23_2_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 868 <= scene <= 878: continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch23_2_scene_%d' % x['target'] if 868 <= x['target'] <= 878 else 'ch23_3'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 2 ====', '    jump ch23_3', '    return', '']
    files = {
        'game/chapters/23/script-ch23_2.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch23_2_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch23_2_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch23_2_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch23_2_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch23/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
