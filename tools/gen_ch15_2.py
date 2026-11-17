#!/usr/bin/env python3
"""Chapter 15 part 2 (scenes 633-642): war council, Void permission."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
120: ("Whew. But the problem is what we do now. Why reveal herself now?",
      "Фух. Но главное — что нам теперь делать. Почему она раскрылась именно сейчас?"),
121: ("Akina said 'the final act is about to begin'...", "Акина сказала «начинается последний акт»…"),
122: ("'Because there's no need to hide anymore.'", "«Потому что больше нет нужды скрываться»."),
123: ("Tabitha!", "Табаса!"),
124: ("The medicine ingredients you asked for.", "Ингредиенты для лекарства, которое вы просили."),
125: ("Ah, thank you, Tabitha. Now we can manage.", "Ах, спасибо, Табаса. Теперь мы справимся."),
126: ("'No need to hide anymore'... What does that mean, Tabitha?",
      "«Больше нет нужды скрываться»… Что это значит, Табаса?"),
127: ("Fires are breaking out all over the city now.", "Сейчас по всему городу вспыхивают пожары."),
128: ("W-What!? It wasn't just the market!?", "Ч-Что!? Это был не только рынок!?"),
129: ("The market fire was just the beginning. There's shelling of the palace too, it seems.",
      "Пожар на рынке — только начало. Кажется, дворец тоже обстреливают."),
130: ("Looks like today was the day they were to act.", "Похоже, сегодня был день, когда они должны были действовать."),
131: ("A-Anyway, let's get to the castle! I'm worried about the Princess! Hurry!",
      "К-Короче, идём в замок! Я беспокоюсь о принцессе! Быстрее!"),
132: ("Let us through! It's urgent!", "Пропустите! Это срочно!"),
133: ("Halt. This is the palace! Follow the proper procedures.", "Стой. Здесь дворец! Соблюдайте порядок."),
134: ("What business do academy students have here!?", "Какое дело здесь академистам!?"),
135: ("W-What did you say!?", "Ч-Что ты сказал!?"),
136: ("Louise, calm down!", "Луиза, успокойся!"),
137: ("Wah!", "Ай!"),
138: ("Eek!", "Ой!"),
139: ("Louise! Are you all right!", "Луиза! Ты в порядке!"),
140: ("(Shelling, you said?)", "Обстрел, говоришь?"),
141: ("(Damn, this is ridiculous. Why is shelling reaching the palace!?)",
      "Чёрт, это возмутительно. Почему снаряды долетают до дворца!?"),
142: ("Now do you understand how serious this is? I'm Louise Francoise, "
      "third daughter of Duke La Valliere.",
      "Теперь ты понял, насколько это важно? Я Луиза Франсуаза, третья дочь герцога Ла Вальер."),
143: ("I have an urgent report concerning the Queen's order. Please announce me.",
      "У меня срочный доклад по поводу приказа Её Величества. Доложите обо мне."),
144: ("B-But...", "Н-Но…"),
145: ("Announce me at once! You can see the fires too! We don't have time for this!",
      "Доложите немедленно! Вы же видите пожары! Нам некогда!"),
146: ("P-Please wait a moment!", "П-Подождите немного!"),
147: ("So, the situation is...", "Итак, обстановка…"),
148: ("Yes. Starting with the fire at the central market, buildings and bridges "
      "across the city have been bombed...",
      "Так. Начиная с пожара на центральном рынке, по всему городу взорваны здания и мосты…"),
149: ("Since then, continuous shelling of the palace from cannons hidden around "
      "the city has been confirmed.",
      "После этого зафиксирован продолжающийся обстрел дворца из орудий, спрятанных в разных местах города."),
150: ("Cannons inside the city? How on earth—!", "Орудия в городе? Как это вообще возможно!?"),
151: ("Reports from the soldiers who subdued the attackers say...",
      "Со слов солдат, которые смогли подавить нападавших…"),
152: ("Reconquista used the recent bombings to slip soldiers disguised as repair "
      "workers into the country.",
      "Реконкиста использовала недавние взрывы, чтобы отправить в страну солдат под видом ремонтников."),
153: ("They seem to have slipped into the damaged sites and installed numerous small cannons.",
      "Они проникли на места разрушений и установили множество малых орудий."),
154: ("What!?", "Что!?"),
155: ("Please look at this map. The sites of the bombings and the cannon positions match exactly.",
      "Посмотрите на эту карту. Места взрывов и позиции орудий совпадают полностью."),
156: ("T-This is...", "Ч-Это…"),
157: ("Yes. The bombings were carried out at the positions best suited for shelling the palace.",
      "Да. Взрывы были произведены в точках, лучше всего подходящих для обстрела дворца."),
158: ("Good heavens. So once again we were one step behind...",
      "Боже мой. Значит, и на этот раз мы оказались на шаг позади…"),
159: ("Reporting.", "Докладываю."),
160: ("Third daughter of the La Valliere family, Louise Francoise.",
     "Третья дочь дома Ла Вальер, Луиза Франсуаза."),
161: ("She requests an audience with Her Majesty regarding an urgent matter.",
     "Она просит аудиенции у Её Величества по срочному делу."),
162: ("Louise? Show her in at once.", "Луиза? Проведите её немедленно."),
163: ("Your Majesty, this Louise you mention...?", "Ваше Величество, эта Луиза, о которой вы…?"),
164: ("They're the ones I had investigating the bomb-thrower. They may have an important report.",
     "Это те, кому я поручила расследовать дело бомбиста. Возможно, у них важный доклад."),
165: ("But this is a war council.", "Но здесь идёт военный совет."),
166: ("Understood. Let's pause the council. You may step down.",
     "Понятно. Объявляю перерыв в совете. Можете идти."),
167: ("...Yes.", "…Так точно."),
168: ("Princess!", "Принцесса!"),
169: ("Louise. You came. And your familiars too.", "Луиза. Ты пришла. И твои фамильяры тоже."),
170: ("I'm sorry, Princess... We couldn't stop the bomb-throwers.",
     "Простите, принцесса… Мы не смогли остановить бомбистов."),
171: ("There's no use regretting the past. Your report, then.",
     "Не стоит сожалеть о прошлом. Переходите к докладу."),
172: ("Yes.", "Да."),
174: ("I see. So that Weatherly troupe after all...", "Понятно. Значит, всё-таки эта труппа Уэзерби…"),
175: ("You knew? Then your joining the performance was...?", "Вы знали? И ваше участие в спектакле было…?"),
176: ("I was indeed conducting a secret investigation. I hated keeping it from Louise.",
     "Я действительно вела тайное расследование. Мне было тяжело скрывать это от Луизы."),
177: ("You could have told me even one thing...", "Вы могли бы сказать хотя бы словом…"),
178: ("Everyone has their strengths. Louise isn't good at keeping secrets.",
     "У каждого свои способности. Луиза не умеет хранить тайны."),
179: ("...", "…"),
180: ("In any case, we must be wary of Miss Weatherly's abilities...",
     "Во всяком случае, мы должны остерегаться способностей мисс Уэзерби…"),
181: ("Not only poor Kirche and Haruna—there may be others in the army and nobility under hypnosis.",
     "Не только несчастные Кирке и Харуна — под гипнозом могут быть и в армии, и среди дворян."),
182: ("I was careless. I had no idea things had gone this far. If I'd noticed sooner...",
     "Я была невнимательна. Я не знала, что дела зашли так далеко. Если бы заметила раньше…"),
183: ("What do you mean?", "Что вы имеете в виду?"),
184: ("It seems the bomb-thrower incident was merely the enemy's first move.",
     "Похоже, дело бомбиста было лишь первым ходом врага."),
185: ("In Tristain, enemy soldiers who infiltrated during the incident have begun moving, "
      "and street fighting is breaking out.",
     "В Тристании вражеские солдаты, проникшие во время того дела, начали действовать, "
     "и вспыхивают уличные бои."),
186: ("T-That can't be!", "Э-Этого не может быть!"),
187: ("Then we'll go take out the cannons...", "Тогда мы пойдём громить орудия…"),
188: ("Wait. There are a great many cannons, heavily guarded.",
     "Подождите. Орудий много, и они хорошо охраняются."),
189: ("I know your strength well. But now, I want you to save it.",
     "Я хорошо знаю вашу силу. Но сейчас я хочу, чтобы вы её приберегли."),
190: ("But, Princess!", "Но, принцесса!"),
191: ("You are our country's trump card. You must not act recklessly.",
     "Вы — козырь нашей страны. Вам нельзя действовать опрометчиво."),
192: ("Anyway, we need to thin out the enemy troops! Let us join the street fighting!",
     "В любом случае, нужно уменьшить число врагов! Давайте пойдём на уличные бои!"),
193: ("I'm truly glad to hear that.", "Я искренне рада это слышать."),
194: ("But I can't allow it.", "Но я не могу это позволить."),
195: ("But, Princess!", "Но, принцесса!"),
196: ("You are our country's trump card. You must not act recklessly.",
     "Вы — козырь нашей страны. Вам нельзя действовать опрометчиво."),
197: ("If there's street fighting, civilians must be getting hurt, right?",
     "Если идут уличные бои, страдают горожане, да?"),
198: ("Good heavens...", "Боже мой…"),
199: ("Let's help guide the evacuation. It's the least we can do right now.",
     "Давайте поможем с эвакуацией. Сейчас это всё, что мы можем."),
200: ("Right. Let's hurry!", "Верно. Быстрее!"),
201: ("No. Wait here for now.", "Нет. Пока подождите."),
202: ("You are our country's trump card. You must not act recklessly.",
     "Вы — козырь нашей страны. Вам нельзя действовать опрометчиво."),
203: ("But!", "Но!"),
204: ("They wouldn't send only those infiltrated soldiers to attack Tristain.",
     "Они не стали бы атаковать Тристанию только теми солдатами, что проникли в город."),
205: ("Most likely...", "Скорее всего…"),
206: ("Reporting!", "Докладываю!"),
207: ("Enemy fleet spotted departing from the direction of Albion.",
     "Обнаружен выход вражеского флота со стороны Альбиона."),
208: ("Course is almost straight. It appears to be heading for Tristain.",
     "Курс почти прямой. Похоже, он направляется к Тристании."),
209: ("What!?", "Что!?"),
210: ("So it's come.", "Значит, это началось."),
211: ("A surprise attack on the capital after maximum chaos from sabotage...",
     "Внезапный удар по столице после максимального хаоса от диверсий…"),
212: ("N-No way...", "Н-Не может быть…"),
213: ("It's what I feared most...", "Это чего я больше всего боялась…"),
214: ("...", "…"),
215: ("Hey, Louise. You've gone quiet—what's wrong?", "Эй, Луиза. Ты затихла — что случилось?"),
216: ("Princess... no, Your Majesty.", "Принцесса… нет, Ваше Величество."),
217: ("Louise Francoise applies for permission to use Void magic in Tristain.",
     "Луиза Франсуаза просит разрешения применить магию Пустоты в Тристании."),
218: ("H-Hey, Louise!", "Э-Эй, Луиза!"),
219: ("You intend to use Void here in Tristain?", "Вы намерены применить Пустоту здесь, в Тристании?"),
220: ("That's insane. It's a fleet, a fleet! You saw the one that fell at Talb's plains!",
     "Это безумие. Флот, флот! Ты видела тот, что упал в поле Тарба!"),
221: ("If one crashes in a city like this, do you have any idea what'll happen!?",
     "Если он рухнет в таком городе, ты представляешь, что будет!?"),
222: ("Then just don't let it fall, silly!", "Тогда просто не дай ему упасть, глупыш!"),
223: ("You make it sound so easy!", "Ты говоришь так, будто это просто!"),
224: ("Quiet, stupid dog! I have a plan!", "Замолчи, глупый пёс! У меня есть план!"),
225: ("Princess. Please, grant permission...", "Принцесса. Прошу, разрешите…"),
226: ("...", "…"),
227: ("Very well. I approve.", "Хорошо. Я разрешаю."),
228: ("The capital... Tristain will really be all right?", "Столица… Тристания и правда будет в безопасности?"),
229: ("...It's fine. Even if it's Void, I won't use Explosion.",
     "…Всё хорошо. Даже если это Пустота, я не применю «Взрыв»."),
230: ("Wait, what do you mean!?", "Подожди, что ты имеешь в виду!?"),
231: ("Void isn't only Explosion, that's all.", "Пустота — не только «Взрыв», вот и всё."),
232: ("Hm? What do you mean?", "Хм? Что ты имеешь в виду?"),
233: ("Louise, I'm counting on you.", "Луиза, я на тебя рассчитываю."),
234: ("Yes. I won't fail you.", "Да. Я не подведу."),
235: ("Ugh.", "Фух."),
236: ("Still worrying? Let's go back to the inn!", "Всё ещё сомневаешься? Вернёмся в гостиницу!"),
237: ("Huh? Why the inn?", "А? Зачем в гостиницу?"),
238: ("To use Void, we need everyone's power.", "Чтобы применить Пустоту, нужна сила всех."),
239: ("Everyone's power?", "Сила всех?"),
240: ("Say, Louise. Are you really going to use Void?", "Слушай, Луиза. Ты и правда применишь Пустоту?"),
241: ("You're so persistent. If I say I will, I will. What else can we do?",
     "Какой ты настойчивый. Скажу — значит применю. Что нам ещё остаётся?"),
242: ("That's true, but...", "Это верно, но…"),
243: ("You keep worrying about what happens after. What matters is before you use it.",
     "Ты всё беспокоишься о том, что будет после. А главное — до того, как применить."),
244: ("Before?", "До?"),
245: ("You know the Void chant takes a long time, don't you?",
     "Ты же знаешь, заклинание Пустоты читается долго, да?"),
246: ("That's when Weatherly and Akina will come to interrupt.",
     "Именно тогда придут Уэзерби и Акина, чтобы помешать."),
247: ("Right. That's certainly possible.", "Верно. Это действительно может быть."),
248: ("Right now, only Tabitha and you can fight those two. That's... not enough, to put it mildly.",
     "Сейчас с ними могут сразиться только Табаса и ты. Этого… мягко говоря, мало."),
249: ("Not enough manpower.", "Недостаток сил."),
250: ("Exactly. If only Kirche were back to normal...", "Вот именно. Хоть бы Кирке вернулась в нормальное состояние…"),
}
CHOICES = {
636: [("We'll go destroy the cannons!", "Мы идём громить орудия!"),
      ("We'll join the street fighting!", "Мы пойдём на уличные бои!"),
      ("We'll help the citizens evacuate!", "Мы поможем эвакуировать горожан!")],
}
SPK = {'ルイズ': 'l', 'サイト': 's', 'タバサ': 't', 'モンモランシー': 'm',
       'デルフリンガー': 'd', 'アンリエッタ': 'h', '将校': 'commander',
       '兵士ＭＳ': 'soldier', '味方Ａ': 'soldier', 'null': 'th'}
START = {'s': 47, 'k': 19, 'l': 23, 'm': 6, 'ak': 22, 'd': 1, 'th': 0, 't': 0,
         'h': 0, 'commander': 0, 'soldier': 0}


def main():
    data = json.load(open('reports/ch15/parse_619_659.json', encoding='utf-8'))
    script = ['# Глава 15, часть 2 (сцены 633–642): военный совет, разрешение на Пустоту.',
              '# Источник: ps2_source/chapters/chapter_16_魔法の薬.txt (SCENE 633-642).',
              '', 'label ch15_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 642:
                break
            if x['no'] < 633:
                continue
            scene = x['no']
            script += ['label ch15_2_scene_%d:' % scene, '']
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
            continue
        if k == 'choice':
            if scene is None or scene not in CHOICES:
                continue
            script.append('    menu:')
            for i, o in enumerate(x['options']):
                en, ru = CHOICES[scene][i]
                ctext = '%s{#ch15_2_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch15_2_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 633 <= scene <= 642:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump ch15_2_scene_%d' % x['target'])
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 2 ====', '    jump ch15_3', '    return', '']
    files = {
        'game/chapters/15/script-ch15_2.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch15_2_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch15_2_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch15_2_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch15_2_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch15/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
