#!/usr/bin/env python3
"""Chapter 22 part 3 (scenes 824-837): tasting Haruna, Louise, Siesta's curry."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
231: ("Well then, now that everyone's recovered. Let's move on to the next tasting.",
      "Ну что ж, теперь, когда все пришли в себя. Переходим к следующему блюду."),
232: ("Yes, it's me.", "Да, это я."),
233: ("I tried making a salad with fresh vegetables.", "Я попробовала сделать салат из свежих овощей."),
234: ("My, my—a starter this time? Let's dig in... Hmm!?", "Ого, на этот раз закуска? Попробуем… Хм!?"),
235: ("Oh, is something the matter, Old Osmond?", "Ох, что-то не так, старик Осман?"),
236: ("Hmm, is it my imagination? The vegetables on the plate seem to be moving.",
      "Хм, может, мне показалось? Овощи на тарелке будто движутся."),
237: ("There's a rustling sound coming from the vegetables.", "От овощей доносится шорох."),
238: ("Whoa! The shredded burdock is moving every now and then!", "Ого! Нарезанный лопух иногда шевелится!"),
239: ("Oh, that's fluid burdock. It's an ornamental plant, so it's rarely used in cooking...",
      "О, это текучий лопух. Это декоративное растение, его редко используют в готовке…"),
240: ("Seeing it cooked like this is a little... no, quite eerie.",
      "Видеть его приготовленным вот так — немного… нет, довольно жутко."),
241: ("O-Ornamental plant? What is it, what is that...", "Д-Декоративное растение? Что это, что это…"),
242: ("This is truly a fantasy world.", "Это и правда мир фэнтези."),
243: ("Choosing fluid burdock as an ingredient is quite an original idea, Haruna-kun.",
      "Выбрать текучий лопух в качестве ингредиента — довольно оригинальная идея, Харуна-кун."),
244: ("No, it's... I'm not very familiar with the vegetables of this world...",
      "Нет, я… Я не очень знакома с овощами этого мира…"),
245: ("Indeed. Only a commoner would think of something like this.", "И верно. Только простолюдин додумался бы до такого."),
246: ("O-Okay. Let's try eating it, then.", "Л-Ладно. Тогда попробуем."),
247: ("Ah, make sure you put the special dressing on it?", "А, ты не забудь особенную заправку?"),
248: ("Ah, the dressing's ordinary, then.", "А, заправка обычная, значит."),
249: ("But blue onions, white peppers, wriggling burdock, and cabbage shreds hard as needles..."
      "...*gulp*.", "Но синие луковицы, белые перцы, извивающийся лопух и нарезанная капуста "
      "твёрже иголок… …*глоток*."),
250: ("I'm going to eat it!?", "Я сейчас съем это!?"),
251: ("Mmgh... Hanhahohewa!?", "Ммгх… Ха-ха-хо-хэ-ва!?"),
252: ("Ugh, what is this?", "Ох, что это?"),
253: ("Whoa... That's an amazing sound, isn't it...", "Ого… Звук просто потрясающий, да…"),
254: ("All right, why don't we eat it together, then, Haruna?", "Ладно, давай тогда есть вместе, Харуна?"),
255: ("Mm, of course.", "Мм, конечно."),
256: ("Phew. Ready, set! *gulp*!", "Фух. Раз, два! *глоток*!"),
257: ("Th-That's an incredible sound!", "Т-Этот звук просто невероятный!"),
258: ("That's mine cabbage.", "Это рудокопная капуста."),
259: ("Mng mng... Mnguuu~~!!", "Мнг-мнг… Мнгууу~~!!"),
260: ("Haruna, are you all right!?", "Харуна, ты в порядке!?"),
261: ("C-Can you even eat this?", "М-Можно ли это есть?"),
262: ("Ah, I dropped it!", "Ах, я уронил!"),
263: ("What a waste! ...Eh!?", "Какая жалость! …А!?"),
264: ("No way... The cucumber just dug into the ground.", "Не может быть… Огурец только что зарылся в землю."),
265: ("Yeah. There's a hole left behind.", "Ага. Ямка осталась."),
266: ("We didn't see that. We saw nothing.", "Мы этого не видели. Мы ничего не видели."),
267: ("R-Right! Now, try it! Salad of cucumbers that burrow into the ground!",
      "В-Верно! Ну, попробуй! Салат из огурцов, зарывающихся в землю!"),
268: ("Damn you, fantasy world!", "Чёртов фэнтези-мир!"),
269: ("It's highly nutritious and very healthy, isn't it. And the appearance is unusual, too.",
      "Очень питательное и полезное блюдо, правда? И на вид необычное."),
270: ("(Colbert-sen and Headmaster Osmond are eating it properly. Fearsome, this fantasy world.)",
      "Кольбер-сэн и директор Осман едят это как ни в чём не бывало. Страшный мир, этот фэнтези."),
271: ("Well then, shall we move on to the next tasting?", "Ну что ж, перейдём к следующему блюду?"),
272: ("Next is Miss Valliere's dish.", "Следующее — блюдо мисс Вальер."),
273: ("Oh, stew, is it?", "О, суп, значит?"),
274: ("I gathered the finest ingredients from everywhere. Poultry, potatoes, onions... "
      "I selected each with the utmost care.", "Я собрала отборные ингредиенты со всего света. "
      "Птица, картофель, лук… Я выбирала каждый с особой тщательностью."),
275: ("It looks pretty decent, doesn't it?", "На вид довольно прилично, да?"),
276: ("It's not just the look! Hurry up and eat it, why don't you?", "Дело не только в виде! "
      "Ну же, поскорее пробуй!"),
277: ("Let's see... *gulp*... Mng mng...", "Посмотрим… *глоток*… Мнг-мнг…"),
278: ("Oh! Th-This is!?", "О! Т-Это что!?"),
279: ("...Well? Saito?", "…Ну? Сайто?"),
280: ("Mmmh!! This is surprising!!", "Мммх!! Это неожиданно!!"),
281: ("Right, right? It's delicious, isn't it? That's what I can do!", "Верно, верно? Вкусно, да? "
      "Вот на что я способна!"),
282: ("The ingredients are cut evenly and it's cooked through. I'm impressed, Louise!",
      "Ингредиенты нарезаны ровно и хорошо проварены. Я в восторге, Луиза!"),
283: ("That goes without saying, you idiot!!", "Это само собой, дурак!!"),
284: ("But why is it so sweet?", "Но почему оно такое сладкое?"),
285: ("Eh... Sweet?", "А… Сладкое?"),
286: ("For Kirche this is her sworn enemy's cooking. Why don't you check it with your own tongue?",
      "Для Кирке это стряпня заклятого врага. Почему бы тебе не проверить своим языком?"),
287: ("True enough... Well then, I'll have some. *gulp*... Mm mm...", "И верно… Ну что ж, попробую. "
      "*Глоток*… Мм-мм…"),
288: ("Kirche, are you all right? You're not going to scream suddenly, are you?",
      "Кирке, ты в порядке? Ты не закричишь вдруг, да?"),
289: ("What's that supposed to mean!?", "Что это значит!?"),
290: ("Mm hmm... A very Valliere-like taste. How old are you this year? Making a stew like this... "
      "heh heh!", "Мм-хм… Очень вальерийский вкус. Сколько тебе лет? Готовить такой суп… хи-хи!"),
291: ("What was that!?", "Что ты сказала!?"),
292: ("This is the sweetest stew I've ever eaten.", "Такой приторно-сладкий суп я ещё никогда не ела."),
293: ("Eh... Sweet?", "А… Сладкое?"),
294: ("Before I eat, there's something I want to ask you.", "Перед тем как есть, я хочу кое-что спросить."),
295: ("What is it?", "Что?"),
296: ("Did you taste it properly?", "Ты как следует пробовала?"),
297: ("Hah!? Why should I have to taste my own cooking!?", "А!? Почему я должна пробовать свою стряпню!?"),
298: ("Tasting what I cook is your job as my familiar, isn't it?", "Пробовать то, что я готовлю, — "
      "твоя обязанность как фамильяра, да?"),
299: ("Because you were playing judge, I couldn't tell how it tasted!",
      "Пока ты играл судью, я не могла понять вкус!"),
300: ("Just as I thought.", "Так и думал."),
301: ("Well then, I'll have some too. Let's see... Huh?", "Ну что ж, я тоже попробую. Посмотрим… А?"),
302: ("W-What's wrong, Siesta?", "Ч-Что случилось, Сиэста?"),
303: ("Miss Valliere... Um, does this have honey in it? It's often used as a secret ingredient...",
      "Мисс Вальер… Э-Э, в нём есть мёд? Его часто добавляют как секретный ингредиент…"),
304: ("Yes... It was in the book. So that's why...", "Да… В книге было написано. Так что…"),
305: ("...How much did you put in?", "…Сколько ты положила?"),
306: ("...One whole jar.", "…Целую банку."),
307: ("Mmgh... Cough, cough...", "Ммгх… Кхм, кхм…"),
308: ("For a pot this size, one whole jar is far too much!", "Для кастрюли такого размера целая банка "
      "слишком много!"),
309: ("Honestly... You should taste it first.", "Честно… Сначала попробуй!"),
310: ("Shut up, honestly. Don't you men nag me! Eat what your mistress gives you without complaint!?",
      "Замолчи, правда. Не пилите меня, мужчины! Ешьте, что даёт госпожа, без жалоб!?"),
311: ("Heh heh. With this seasoning, I'd say a small child would enjoy it more than us.",
      "Хе-хе. С такой приправой её больше оценил бы ребёнок, чем мы."),
312: ("It is a bit sweet, certainly, but there's a certain warmth to this stew.",
      "Она и правда немного сладковата, но в этом супе есть особое тепло."),
313: ("(Well, judging by Louise's standards, that was better than expected. Still, she looks dissatisfied...)",
      "Ну, по меркам Луизы вышло лучше, чем можно было ждать. Но она всё равно недовольна…"),
314: ("Well then, Siesta's dish is next.", "Ну что ж, дальше блюдо Сиэсты."),
315: ("Judging by what's been served so far, none of you know anything at all!!",
      "Судя по тому, что вы здесь пробовали, вы ничего не понимаете!!"),
316: ("Oh!?", "О!?"),
317: ("When you cook, you must think about the person who'll eat it!",
      "Когда готовишь, нужно думать о том, кто будет это есть!"),
318: ("From the moment a cook enters the kitchen, they must never forget their love for the one "
      "eating their food!", "С того момента, как повар встаёт у плиты, он не должен забывать "
      "о любви к тому, кто будет есть его еду!"),
319: ("As expected of Siesta. Well said.", "Как и подобает Сиэсте. Хорошо сказано."),
320: ("Actually, Marto-san said that.", "На самом деле это сказал Марто-сан."),
321: ("Just repeating him, were you?", "Просто повторяешь его слова?"),
322: ("Now, everyone, please eat. This is a special stew passed down from my great-great-grandfather!",
      "Ну же, все, угощайтесь. Это особый суп, переданный мне прадедушкой!"),
323: ("Even though Louise made stew, you two serve the same thing... She must be pretty confident, "
      "that girl, don't you think?", "Хотя Луиза готовила суп, вы двое подаёте то же самое… "
      "Должно быть, она очень уверена в себе, да?"),
324: ("Well. Let's enjoy it thoroughly, Montmorency.", "Ну что ж. Насладимся сполна, Монморанси."),
325: ("Here, Saito-san. Please eat.", "Вот, Сайто-сан. Угощайтесь."),
326: ("Thanks, Siesta... Wait.", "Спасибо, Сиэста… Погоди."),
327: ("Aaaaah!! This dish is... No way!?", "А-а-а-а!! Это блюдо… Не может быть!?"),
328: ("This is! Could it be...", "Это! Неужто…"),
329: ("Both you and Haruna-san know this dish, don't you?", "И вы, и Харуна-сан знаете это блюдо, да?"),
330: ("This is curry!! It's a dish from the world we lived in!!", "Это карри!! Блюдо из мира, где мы жили!!"),
331: ("Hehe... Eat plenty, okay!", "Хи-хи… Ешь побольше, ладно!"),
332: ("Ah, I'm eating! *gulp*, *chew chew*...", "Ах, я ем! *Глоток*, *жую-жую*…"),
333: ("To think curry would show up here of all places...", "Кто бы мог подумать, что карри появится именно здесь…"),
334: ("A dish unique to our world showing up in a place like this—it's kind of amazing, isn't it?",
      "Блюдо, присущее нашему миру, появляется в таком месте — это просто поразительно, да?"),
335: ("Truly, isn't it. I'm a little grateful to my great-great-grandfather.",
      "И правда. Я немного благодарна прадедушке."),
336: ("Thanks to him, Saito-san was so happy...", "Благодаря ему Сайто-сан так обрадовался…"),
337: ("If I'd known such a wonderful dish was waiting, Louise's cooking wouldn't have stood a chance!!",
      "Если бы я знал, что ждёт такое радостное блюдо, стряпня Луизы не имела бы шансов!!"),
338: ("Oh, you certainly do talk. I suppose my stew was just sweet, childish stew, was it!?",
      "О, как же ты красноречив. Значит, мой суп был просто сладким детским супом, да!?"),
339: ("Honestly! I'm never cooking for Saito again!", "Честно! Больше я Сайто готовить не буду!"),
340: ("Hey, Siesta. Teach Louise how to make curry later, would you?",
      "Эй, Сиэста. Потом научи Луизу готовить карри, ладно?"),
341: ("Me!?", "Меня!?"),
342: ("Eh... Why would you ask that!?", "А… Почему ты просишь об этом!?"),
343: ("See, curry and stew are cooked the same way up to a point, right? "
      "So I thought maybe Louise could make it, too.", "Видишь, карри и суп готовятся одинаково до "
      "определённого этапа, да? Я и подумал, может, Луиза тоже сможет.",),
344: ("Besides, I want everyone to know the food of my country.", "И ещё я хочу, чтобы все узнали "
      "блюда моей страны."),
345: ("Yes! That's right.", "Да! Верно."),
}
CHOICES = {
824: [("Try the wriggling vegetables", "Попробовать шевелящиеся овощи"),
      ("Offer it to Haruna", "Предложить Харуне"),
      ("Pinch it timidly", "Боязливо ущипнуть")],
829: [("Eat Louise's stew", "Съесть суп Луизы"),
      ("Offer it to Kirche", "Предложить Кирке"),
      ("Did you taste it?", "Ты пробовала?")],
834: [("Curry is here!", "Карри здесь!"),
      ("Such a joyful dish!", "Такое радостное блюдо!"),
      ("Teach Louise, too", "Научи и Луизу")],
}
SPK = {'コルベール': 'c', 'ハルナ': 'ha', 'オスマン': 'o', 'ルイズ': 'l', 'サイト': 's',
       'シエスタ': 'si', 'キュルケ': 'k', 'モンモランシー': 'm', 'ギーシュ': 'g',
       'タバサ': 't', 'null': 'th'}
START = {'c': 9, 'ha': 8, 'o': 7, 'l': 34, 's': 94, 'si': 39, 'k': 31, 'm': 1, 'g': 1, 't': 7, 'th': 0}


def main():
    data = json.load(open('reports/ch22/parse_806_848.json', encoding='utf-8'))
    script = ['# Глава 22, часть 3 (сцены 824–837): дегустация, карри Сиэсты.',
              '# Источник: ps2_source/chapters/chapter_23_料理の鉄人.txt (SCENE 824-837).',
              '', 'label ch22_3:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 837:
                break
            if x['no'] < 824:
                continue
            scene = x['no']
            script += ['label ch22_3_scene_%d:' % scene, '']
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
                ctext = '%s{#ch22_3_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch22_3_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 824 <= scene <= 837:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch22_3_scene_%d' % x['target']
                                          if 824 <= x['target'] <= 837 else 'ch22_4'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 3 ====', '    jump ch22_4', '    return', '']
    files = {
        'game/chapters/22/script-ch22_3.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch22_3_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch22_3_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch22_3_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch22_3_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch22/voice_map_3.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
