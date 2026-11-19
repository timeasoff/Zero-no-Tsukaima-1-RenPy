#!/usr/bin/env python3
"""Chapter 27 part 2 (scenes 985-993): splitting teams, Tabitha's charm, ambush."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
156: ("Anyway, I'm not convinced!", "В любом случае, я не убеждён!"),
157: ("Hey, Saito. It seems you and I have a difference of opinion about Void magic, don't we?",
     "Эй, Сайто. Кажется, у нас с тобой разные взгляды на Пустоту, да?"),
158: ("A difference of opinion? You're going to blow Tristain and the infiltrators away together, aren't you?",
     "Разные взгляды? Ты же хочешь взорвать Тристанию вместе с проникшими врагами, да?"),
159: ("Nooo—I said we'll use a different spell. Don't worry.", "Нeeeт — я же сказала, что применю другое заклинание. Не волнуйся."),
160: ("A different spell?", "Другое заклинание?"),
161: ("Y-Yes, a different spell.", "Д-Да, другое заклинание."),
162: ("(What kind of 'different spell' could that be...?)", "Какое ещё «другое заклинание»…?"),
163: ("Say—what are you actually planning?", "Слушай — что ты на самом деле задумала?"),
164: ("I've told you—you don't need to worry, Saito.", "Я же сказала — тебе не нужно волноваться, Сайто."),
165: ("Even if you say that—I'm worried! At this rate, the whole capital could be blown away!",
     "Даже если ты так говоришь — я волнуюсь! Так столицу может снести!"),
166: ("I'm not going to do that. How many times do I have to tell you!?",
     "Я не собираюсь этого делать. Сколько раз тебе повторять!?"),
167: ("If you keep nagging, I'll blow you away first!", "Если будешь приставать, я первой тебя взорву!"),
168: ("Hey!!", "Эй!!"),
169: ("See? Everyone's here. Enough—this discussion is over!", "Видишь? Все здесь. Хватит — разговор окончен!"),
170: ("Over, you say...", "Окончен, говоришь…"),
171: ("(True—we can't talk about Void magic in front of Kirche and the others...)",
     "Верно — при Кирке и остальных нельзя говорить о Пустоте…"),
172: ("Ah, darling!", "Ах, дорогой!"),
173: ("You went all the way to the Queen—what did you do!?", "Ты сходил к Королеве — что ты там делал!?"),
174: ("It wasn't me—Louise had business with the princess.", "Это не я — у Луизы было дело к принцессе."),
175: ("Hmm... Louise has quite the influence, doesn't she?", "Хм… У Луизы, оказывается, есть влияние, да?"),
176: ("What do you mean, 'quite'!? I'm...!!", "Что значит «оказывается»!? Я же…!!"),
177: ("Well, whatever. More importantly, let's divide up our roles.",
     "Ладно. Главное — давайте распределим роли."),
178: ("Divide up roles—what are you talking about?", "Распределить роли — о чём ты?"),
179: ("It's obvious. We decide who fights what.", "Очевидно. Решим, кто с кем сражается."),
180: ("Reconquista is closing in from outside Tristain, and Akina is rampaging inside.",
     "Реконкиста подступает извне, а Акина буйствует внутри."),
181: ("Huh? Shouldn't we all rush to take down Akina first?", "А? Не стоит ли всем вместе сначала одолеть Акину?"),
182: ("If we do that, my spell's preparation might not be ready in time. And how would we even find Akina?",
     "Если так, я могу не успеть подготовить заклинание. И как мы вообще найдём Акину?"),
183: ("Better to shift our thinking a little—deal with the air fleet while knocking down Akina when she interferes.",
     "Лучше немного изменить подход — заняться флотом, а Акину сбить, когда она помешает."),
184: ("When you put it that way... Even if Akina doesn't show, we can handle the fleet first and deal with her later.",
     "Когда ты так говоришь… Даже если Акина не появится, можно сначала справиться с флотом, а с ней позже."),
185: ("Then we'll split in two. One team for Akina, one for the air fleet.",
     "Тогда разделимся надвое. Одна группа против Акины, другая — против флота."),
186: ("Hey, Louise. Are we really okay splitting up?", "Эй, Луиза. Мы и правда можем разделиться?"),
187: ("The air fleet won't be handled even with everyone. And yet you want to split our forces...",
     "С флотом не справиться даже всем вместе. А ты хочешь разделить силы…"),
188: ("Well, leave that part to me. I have a trump card.", "Ну, это предоставь мне. У меня есть козырь."),
189: ("A trump card?", "Козырь?"),
190: ("If I told you, it wouldn't be a trump card, would it? So—I'll take the air fleet; Tabitha takes Akina...",
     "Если скажу, это уже не козырь, да? Так — я беру флот, Табаса берёт Акину…"),
191: ("Mm.", "Мм."),
192: ("What about Saito and Kirche?", "А что будете делать Сайто и Кирке?"),
193: ("Ehh!? I can't team up with darling!? What's the reason?", "А!? Я не могу работать с дорогим!? Почему?"),
194: ("There's no reason. It's my strategy.", "Причины нет. Это моя стратегия."),
195: ("I-I understand.", "П-Понятно."),
196: ("So, Saito—which do you want to team with, Louise or Tabitha?", "Так, Сайто — с кем хочешь работать, с Луизой или Табасой?"),
197: ("Which I want... Shouldn't it be decided by the enemy we're facing?", "С кем хочу… Разве это не определяется врагом, против которого идём?"),
198: ("...", "…"),
199: ("(Hmm... Louise says she'll use Void, which worries me...)", "Хм… Луиза говорит, что применит Пустоту — это волнует…"),
200: ("(Tabitha's burns have healed, but she's not at full strength, so I'm worried...)",
     "Ожоги Табасы зажили, но она не в полной форме — беспокоит…"),
201: ("(So, honestly, I'm far more worried about Tabitha...)", "Так что, честно говоря, я гораздо больше беспокоюсь о Табасе…"),
202: ("Hmm...", "Хм…"),
203: ("I think... Louise, after all.", "Я думаю… всё-таки Луизу."),
204: ("(She says she'll fight the air fleet, but Void's power worries me...)", "Она говорит, что против флота, но сила Пустоты беспокоит…"),
205: ("Hey, darling!", "Эй, дорогой!"),
206: ("Wh-What is it...?", "Ч-Что…?"),
207: ("Darling will team with Tabitha. I'll team with Louise.", "Дорогой работает с Табасой. Я — с Луизой."),
208: ("Eh, but if I team with Tabitha... It'll be like last time...", "А, но если я с Табасой… будет как в прошлый раз…"),
209: ("It'll be fine this time...", "В этот раз всё будет хорошо…"),
210: ("So—I'll be with Louise.", "Так — я с Луизой."),
211: ("I think... Tabitha, after all.", "Я думаю… всё-таки Табасу."),
212: ("...", "…"),
213: ("(Akina needs dealing with quickly, but the fleet won't arrive for a while yet...)",
     "С Акиной нужно быстро, но до флота ещё есть время…"),
214: ("(And after Akina's down, I need to be there when they decide Haruna's fate...)",
     "И после того, как Акина будет повержена, мне нужно присутствовать при решении судьбы Харуны…"),
215: ("(More than anything, I'm worried Tabitha will overdo it...)", "И больше всего — боюсь, что Табаса перестарается…"),
216: ("Good choice, darling.", "Хороший выбор, дорогой."),
217: ("Hmm? Why?", "Хм? Почему?"),
218: ("Because Tabitha is happy.", "Потому что Табаса рада."),
219: ("...", "…"),
220: ("So I don't matter, do I?", "Значит, я не важна, да?"),
221: ("N-No, that's not it! Well then—Kirche, take care of Louise, please.",
     "Н-Нет, это не так! Ну тогда — Кирке, присмотри за Луизой, пожалуйста."),
222: ("Leave it to me, darling. I'll keep a close eye on Louise.",
     "Оставь мне, дорогой. Я пристально присмотрю за Луизой."),
223: ("Sorry—let Kirche decide first.", "Прости — пусть Кирке решит первой."),
224: ("Ehh!? In a case like this, a boy needs to decide firmly, darling!",
     "А!? В такое время мальчик должен решить твёрдо, дорогой!"),
225: ("I know, but... I want to be with both of them, you see...", "Знаю, но… Я хочу быть с обеими, понимаешь…"),
226: ("Then darling should team with Tabitha.", "Тогда дорогой должен работать с Табасой."),
227: ("Eh, why?", "А, почему?"),
228: ("Even if she looks like that, Tabitha wants to team with darling.", "Несмотря на вид, Табаса хочет работать с дорогим."),
229: ("...", "…"),
230: ("Got it. Tabitha, please.", "Понял. Табаса, пожалуйста."),
231: ("...Mm.", "…Мм."),
232: ("Well then, darling, Tabitha—take care of Haruna.", "Ну что ж, дорогой, Табаса — позаботьтесь о Харуне."),
233: ("Ah, I understand. Louise, Kirche—please.", "Ах, понял. Луиза, Кирке — прошу вас."),
234: ("Honestly—you just need to trust your mistress, you silly familiar.",
     "Право — тебе лишь нужно доверять госпоже, глупый фамильяр."),
235: ("And if you do anything to Tabitha, you'll be punished later!", "И если ты что-то сделаешь Табасе — потом наказание!"),
236: ("I won't do anything.", "Я ничего не сделаю."),
237: ("Well then...", "Ну что ж…"),
238: ("If we make a scene on the roof, we can probably lure Akina out—but...",
     "Если устроить сцену на крыше, можно выманить Акину — но…"),
239: ("Is Tabitha's body really all right? Her burns are healed, but she's not at full strength, is she...",
     "Табаса и правда в порядке? Ожоги зажили, но она не в полной силе, да…"),
240: ("...", "…"),
241: ("You're still worried?", "Ты всё ещё волнуешься?"),
242: ("...Mm.", "…Мм."),
243: ("I don't want Tabitha to overdo it...", "Я не хочу, чтобы Табаса перестаралась…"),
244: ("...", "…"),
245: ("...Um.", "…Э-Э."),
246: ("Hmm? What's wrong?", "Хм? Что случилось?"),
247: ("A charm.", "Заклинание."),
248: ("A charm?", "Заклинание?"),
249: ("Mm. I want a charm.", "Мм. Я хочу заклинание."),
250: ("Um, I'll do what I can, but...?", "Э-Э, я сделаю что смогу, но…?"),
251: ("It has to be you.", "Это должен быть только ты."),
252: ("I see. Then what should I do?", "Понятно. Тогда что мне делать?"),
253: ("Close your eyes.", "Закрой глаза."),
254: ("Eh? That's all? Well then, I'll close them...", "А? Это всё? Ну что ж, закрываю…"),
255: ("...", "…"),
256: ("Are you sure?", "Ты уверена?"),
257: ("Mm.", "Мм."),
258: ("(What is she going to do...?)", "Что она собирается делать…?"),
259: ("(...Chu.)", "…Чмок."),
260: ("Eh? Ehh!? W-What did you just do!?", "А? А-а!? Ч-Что ты сейчас сделала!?"),
261: ("...", "…"),
262: ("U-Um... There was something incredibly soft...", "Э-Э… Было что-то невероятно мягкое…"),
263: ("...", "…"),
264: ("Th-This couldn't be... I-It's a k-k-k...", "Т-Это не может быть… Э-Это п-поце…"),
265: ("...D-Don't say it. It's embarrassing.", "…Н-Не говори. Неловко."),
266: ("Embarrassing, you say...", "Неловко, говоришь…"),
267: ("If it's all right... Could you do that charm again?", "Если можно… можешь повторить это заклинание?"),
268: ("N-No.", "Н-Нет."),
269: ("O-Oh... Ha ha ha...", "О-Ох… Ха-ха-ха…"),
270: ("Mm, I'm fine.", "Мм, я в порядке."),
271: ("Then that's fine... But don't overdo it, okay?", "Ну, тогда хорошо… Но не перестарайся, ладно?"),
272: ("We made it to the town—but will Akina really show up before us?", "Мы вышли в город — но Акина и правда появится перед нами?"),
273: ("She'll come.", "Она придёт."),
274: ("You sound sure.", "Ты уверена."),
275: ("I spread word that I'm targeting Haruna.", "Я распустила слух, что охочусь за Харуной."),
276: ("The one she'll go after is me.", "Она пойдёт за мной."),
277: ("A plan to become bait yourself...? Say—is a request always this painful?", "План — самой стать приманкой…? Слушай — задания всегда такие тяжёлые?"),
278: ("Painful. But now, just a little less painful.", "Тяжёлые. Но сейчас — чуть менее тяжёлые."),
279: ("Why?", "Почему?"),
280: ("Because Saito is here.", "Потому что Сайто здесь."),
281: ("...", "…"),
282: ("...She's here.", "…Она здесь."),
283: ("Eh?", "А?"),
284: ("Ah ha ha ha! Ha ha! A-ha-ha-ha!!", "А-ха-ха-ха! Ха-ха! А-ха-ха-ха!!"),
285: ("That voice—could it be?", "Этот голос — неужто?"),
286: ("Mm.", "Мм."),
287: ("Ah ha—found you!", "А-ха — нашла вас!"),
288: ("I mean—how did you know we were here?", "Я хотел спросить — откуда ты узнала, что мы здесь?"),
289: ("I've been watching your every move!", "Я следила за каждым вашим шагом!"),
290: ("Tabitha's after my life? That's a million years too early.", "Табаса охотится за моей жизнью? Это на миллион лет рано."),
291: ("Hey now—Haruna's still a teenager.", "Эй — Харуне же ещё нет двадцати."),
292: ("This time I'll defeat you.", "В этот раз я тебя одолею."),
293: ("Ehh—that sounds fun.", "Ох — это звучит забавно."),
294: ("Derf—draw!", "Дерф — обнажай клинок!"),
}
CHOICES = {
986: [("Leave it to Tabitha", "Поручить Табасе"),
      ("Worried about after", "Беспокоит будущее"),
      ("Worried about everyone", "Беспокоит всех")],
}
SPK = {'サイト': 's', 'ルイズ': 'l', 'キュルケ': 'k', 'タバサ': 't',
       'アキナ': 'ak', 'null': 'th'}
START = {'s': 61, 'l': 44, 'k': 21, 't': 10, 'ak': 2, 'th': 0}


def main():
    data = json.load(open('reports/ch27/parse_972_998.json', encoding='utf-8'))
    script = ['# Глава 27, часть 2 (сцены 985–993): распределение ролей, чары Табасы, засада.',
              '# Источник: ps2_source/chapters/chapter_28_ハルナの秘密.txt (SCENE 985-993).',
              '', 'label ch27_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 993: break
            if x['no'] < 985: continue
            scene = x['no']
            script += ['label ch27_2_scene_%d:' % scene, '']
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
            tag = 'ch27_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch27_2_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch27_2_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 985 <= scene <= 993: continue
            t = x['target']
            if scene == 990 and t == 992:
                script.append('    # checkKiss(): ветка 991/992 — zero_kiss не портирован; идём по ветке zero_kiss (991), как в гл.12')
                continue
            script.append('    # → next scene %d' % t)
            script.append('    jump %s' % ('ch27_2_scene_%d' % t if 985 <= t <= 993 else 'ch27_3'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 2 ====', '    jump ch27_3', '    return', '']
    files = {
        'game/chapters/27/script-ch27_2.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch27_2_dialogs.rpy': '\n'.join(['translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch27_2_dialogs.rpy': '\n'.join(['translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch27_2_choises.rpy': '\n'.join(['translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch27_2_choises.rpy': '\n'.join(['translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch27/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest: f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
