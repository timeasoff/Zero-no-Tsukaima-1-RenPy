#!/usr/bin/env python3
"""Chapter 18 part 2 (scenes 706-713): siege of the academy."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
127: ("(Akina barricaded herself in the headmaster's office.)", "Акина заперлась в кабинете директора."),
128: ("(The headmaster, grasping the situation, proposed negotiating with her.)", "Директор, поняв обстановку, предложил вести переговоры."),
129: ("So the thief has barricaded herself in the headmaster's office, eh? "
      "We can't storm it carelessly. Let me try talking her down first.",
      "Так, значит, вор заперся в кабинете директора? Нельзя штурмовать опрометчиво. "
      "Сначала я попробую уговорить её."),
130: ("That's dangerous! If anything happened to Old Osmond...", "Это опасно! Если со старым Османом что-то случится…"),
131: ("Your concern warms me, but I am the headmaster. Leave the talking to me.",
      "Твоя забота греет, но я — директор. Доверь переговоры мне."),
132: ("But what if Old Osmond is taken hostage!", "Но если старика Османа возьмут в заложники!"),
133: ("In that case, all the teachers can attack, or do whatever—right?",
      "В таком случае все преподаватели могут атаковать или что-нибудь ещё — верно?"),
134: ("Many against few. However many bombs she has, she can't win.",
      "Много против немногих. Сколько бы бомб у неё ни было, она не победит."),
135: ("...", "…"),
136: ("No other options, then it's settled.", "Других предложений нет — значит, решено."),
137: ("Ahem. Akina, I'd like to have a word. May I come in?",
      "Кхм. Акина, я хотел бы поговорить. Можно мне войти?"),
138: ("Fine. But if you try anything strange—boom!", "Ладно. Но если что-то не то — бах!"),
139: ("We can hardly do anything from here. I'll open the lock myself, if you don't mind?",
      "Отсюда мы вряд ли что-то можем. Я сам откручу замок, если не против?"),
140: ("Well, I'm off. The rest is up to you.", "Ну, я пошёл. Остальное на вас."),
141: ("Old Osmond...!", "Старик Осман…!"),
142: ("(Meanwhile, we were gathered in a classroom by the headmaster's arrangement.)",
      "Тем временем нас по указанию директора собрали в классе."),
143: ("What are they talking about? I wonder.", "О чём они говорят? Интересно."),
144: ("Leave it to me.", "Доверь мне."),
145: ("I used magic. Now we can hear what's inside.", "Я использовала магию. Теперь мы слышим разговор внутри."),
146: ("Ah, Tabitha, you're so reliable! Let's see...", "Ах, Табаса, ты такая надёжная! Посмотрим…"),
147: ("You know the situation, Akina-kun.", "Ты понимаешь обстановку, Акина-кун."),
148: ("You're a professional, so you understand. We have teachers here, and students "
      "with the title of Chevalier.",
      "Ты профессионал, поэтому понимаешь. Здесь есть преподаватели и ученики "
      "с титулом шевалье."),
149: ("Consider all of them turning against you. Even you couldn't get out unharmed... could you?",
      "Представь, что все они станут против тебя. Даже ты не выйдешь невредимой… верно?"),
150: ("Well, about that...", "Ну, это ещё вопрос…"),
151: ("You could surrender and use your abilities for Tristain.", "Ты можешь сдаться и применить способности на благо Тристании."),
152: ("If you surrender, I'll put in a word with Her Majesty. I won't let them mistreat you.",
      "Если сдашься, я замолвлю словечко перед Её Величеством. Я не дам тебя обидеть."),
153: ("Yeah, that's one path, maybe. At least Haruna would listen to you obediently.",
      "Да, может, это и один из путей. По крайней мере Харуна послушалась бы тебя."),
154: ("But see—I've already done my job. You've guessed, haven't you? "
      "I didn't come here alone.",
      "Но дело в том, что я уже выполнила задачу. Ты догадываешься, да? "
      "Я пришла не одна."),
155: ("...", "…"),
156: ("W-What!?", "Ч-Что!?"),
157: ("That sound... this is...", "Этот звук… это…"),
158: ("Partner. Everything may have come too late.", "Приятель. Возможно, всё пришло слишком поздно."),
159: ("It's terrible, everyone! Look out the window!!", "Беда, все! Посмотрите в окно!!"),
160: ("...", "…"),
161: ("That emblem on the hull... Reconquista? Why would Reconquista warships...",
      "Этот герб на борту… Реконкиста? Почему корабли Реконкисты…"),
162: ("Looks like they've arrived. The main force. Now the tables have turned.",
      "Похоже, они пришли. Основные силы. Теперь положение переменилось."),
163: ("Grr...", "Грр…"),
164: ("Akina, well done. You've grown quite skilled at diversion, it seems.",
      "Акина, отлично поработала. Кажется, ты стала довольно искусной в отвлекающих маневрах."),
165: ("That voice... Weatherly-san?", "Этот голос… Уэзерби-сан?"),
166: ("No way...", "Не может быть…"),
167: ("...", "…"),
168: ("So you're the commander of this operation. Quite a plan.",
      "Так вы и есть руководитель этой операции. Довольно искусный план."),
169: ("I'm flattered.", "Польщена."),
170: ("Now, as you can see outside, this academy is already under Reconquista's control.",
      "Как вы видите в окно, эта академия уже под контролем Реконкисты."),
171: ("Soldiers are already stationed throughout. Every cannon is aimed at the academy.",
      "Солдаты уже расставлены по всей академии. Все орудия наведены на неё."),
172: ("Please don't think we're bluffing. We're quite serious.",
      "Прошу не думать, что мы блефуем. Мы совершенно серьёзны."),
173: ("Such a large-scale operation means you have some goal.",
      "Такая масштабная операция значит, что у вас есть цель."),
174: ("Just what is it you want?", "Именно чего вы хотите?"),
175: ("You make it easy to talk. Good.", "Вы упрощаете разговор. Хорошо."),
176: ("First, information about the legendary familiar of this academy and its wielder. "
      "Naturally, we'll take the two themselves as test subjects.",
      "Во-первых, сведения о легендарном фамильяре этой академии и его хозяйке. "
      "Естественно, мы заберём их самих в качестве подопытных."),
177: ("Isn't that Akina-kun already getting you information?",
      "Разве Акина-кун уже не добывает вам сведения?"),
178: ("Only the common ones. Classified information was difficult even for Akina to obtain.",
      "Лишь обычные. Секретные даже Акине было трудно достать."),
179: ("I-I'm sorry, Weatherly-sama. I couldn't be of more use...",
      "П-Простите, Уэзерби-сама. Я не смогла быть полезной…"),
180: ("Don't blame yourself. You did well in such a short time.",
      "Не вини себя. За такой короткий срок ты хорошо постаралась."),
181: ("Ah, and Old Osmond.", "Ах, и старик Осман."),
182: ("We'd like you to hand over the magic items stored in this academy...",
      "Мы хотели бы, чтобы вы передали магические предметы, хранящиеся в академии…"),
183: ("...and provide information on how to use them. Rumor has it there are many interesting things.",
      "…и предоставили сведения об их применении. Говорят, там немало интересного."),
184: ("Quite the list of demands. Did you think I'd simply say yes?",
      "Довольно много требований. Ты думал, я просто соглашусь?"),
185: ("We hold hostages... The lives of every student—surely that's a small price?",
      "У нас заложники… Жизни всех учеников — невеликая цена, правда?"),
186: ("What do we do? Rush the headmaster's office?", "Что делаем? Врываемся в кабинет директора?"),
187: ("Hey now, partner. You're as straight ahead as ever.", "Эй, приятель. Ты всё так же прямолинеен."),
188: ("There are bombs and soldiers all over the academy, right? How will you slip through?",
      "В академии повсюду бомбы и солдаты, верно? Как ты проскользнёшь?"),
189: ("That's true, but...", "Это верно, но…"),
190: ("If you refuse to talk... we'll have to take suitable measures.",
      "Если вы отказываетесь говорить… нам придётся принять соответствующие меры."),
191: ("Pardon me...!", "Простите…!"),
192: ("W-What was that...?", "Ч-Что это было…?"),
193: ("A strange sound...", "Странный звук…"),
194: ("Stopping the magic.", "Останавливаю магию."),
195: ("W-What is it, Tabitha?", "Ч-Что случилось, Табаса?"),
196: ("This magic...", "Эта магия…"),
197: ("I see. Interesting magic. The forbidden art that controls the heart... "
      "But it doesn't seem to work on me.",
      "Понятно. Интересная магия. Запретное искусство, управляющее сердцем… "
      "Но на меня, кажется, не действует."),
198: ("Tch, even old and worn, that power is the real thing, is it? "
      "Then we use the original method.",
      "Тьфу, даже в старости эта сила настоящая, да? Тогда применим исходный способ."),
199: ("Old Osmond. From now on, you'll be under our supervision.",
      "Старик Осман. Отныне вы будете под нашим присмотром."),
200: ("Keeping silent is also fine. But if you persist in your stubbornness...",
      "Молчать — тоже хорошо. Но если вы будете упорствовать…"),
201: ("This academy and everyone in it will be consumed by the flames of our "
      "Reconquista's judgment.",
      "Эта академия и все в ней будут пожраны пламенем правосудия нашей Реконкисты."),
202: ("...", "…"),
203: ("Very well. Akina, go ahead.", "Хорошо. Акина, начинай."),
204: ("Yes.", "Да."),
205: ("A-Another explosion...!?", "О-Опять взрыв…!?"),
206: ("Damn...", "Чёрт…"),
207: ("I do hope that old head considers how little time you have left.",
      "Надеюсь, эта старая голова хорошенько подумает, сколько у вас осталось времени."),
208: ("Indeed. Let me think right up to the very last moment.",
      "Именно. Подумаю до самого последнего момента."),
209: ("Buying time is fine, but hoping for reinforcements is pointless.",
      "Тянуть время — хорошо, но надеяться на подкрепление бесполезно."),
210: ("You've heard, I'm sure—Tristain is a battlefield too. No one can come to your aid.",
      "Вы, конечно, слышали — Тристания тоже поле боя. Никто не сможет вам помочь."),
211: ("...", "…"),
212: ("Then take all the time you need.", "Тогда думайте сколько угодно."),
213: ("Haruna, and now Weatherly too—both servants of Reconquista...",
      "Харуна, а теперь и Уэзерби — обе слуги Реконкисты…"),
214: ("Well, I suspected as much and was investigating—but it seems we were always a step behind.",
      "Ну, я подозревала и расследовала — но, кажется, мы всё время опаздывали."),
215: ("Total defeat.", "Полное поражение."),
216: ("W-Wait, since when was Weatherly suspicious...?",
      "П-Подожди, с того пор Уэзерби стала подозрительной…?"),
217: ("Since the Queen came. Remember when I sulked and skipped practice?",
      "С тех пор как приехала Королева. Помнишь, я дулась и не ходила на тренировки?"),
218: ("Ah!", "А!"),
219: ("I was investigating everything around Weatherly. The Queen's visit wasn't idle either.",
      "Я расследовала всё вокруг Уэзерби. И визит Королевы был не просто так."),
220: ("Why didn't you tell me something so important...", "Почему ты не сказала мне о таком важном…"),
221: ("Because you get single-minded, don't you? You're no good for strategy. "
      "And you even played the lead on stage, didn't you?",
      "Потому что ты упрямая, да? Для стратегии не годишься. "
      "И даже сыграла главную роль на сцене, верно?"),
222: ("Ugh... That may be true, but... But...", "Ох… Может, и так, но… Но…"),
223: ("(Right now, we're having a strategy meeting in Louise's room with Kirche and the others.)",
      "Сейчас мы с Кирке и остальными проводим совещание в комнате Луизы."),
224: ("(The academy teachers are hiding everywhere to stop the Reconquista troops.)",
      "Преподаватели академии прячутся повсюду, чтобы не допустить солдат Реконкисты."),
225: ("(They've mobilized even the triangle and the line mages—a real all-academy defense.)",
      "Они мобилизовали даже магов треугольника и линии — настоящая оборона всей академии."),
226: ("(But even so, the enemy has mages too—professionals of combat. It doesn't feel reassuring.)",
      "Но и у врага есть маги — причём профессионалы боя. Это не успокаивает."),
227: ("So what will you do, Louise? It seems their target is you two.",
      "И что ты сделаешь, Луиза? Похоже, их цель — вы двое."),
228: ("How you act now holds the key to everything, one might say.",
      "От твоих действий сейчас зависит всё, можно сказать."),
229: ("That's obvious. Use the Zero Fighter to save Tristain. Then the academy will be saved too.",
      "Это очевидно. Использовать Zero Fighter и спасти Тристанию. Тогда и академия будет спасена."),
230: ("Wait a second. Isn't that backwards? Shouldn't we save the academy first?",
      "Подожди. Разве не наоборот? Сначала надо спасти академию."),
231: ("I'm not wrong. If we save the academy but Tristain falls, it's all for nothing.",
      "Я не ошиблась. Если академия уцелеет, а Тристания падёт, всё напрасно."),
232: ("...So that's the mistress's decision. I refuse!", "…Такова воля госпожи? Я отказываюсь!"),
233: ("What!?", "Что!?"),
234: ("My, my.", "Ой-ой."),
235: ("...", "…"),
236: ("Sure, nobles have their priorities—but I can't abandon this academy. Isn't that right!",
      "Конечно, у дворян свои приоритеты — но я не могу бросить академию. Разве не так!"),
237: ("I never said abandon it.", "Я не говорила — бросить."),
238: ("Sure, I'm your familiar—but I don't want to listen to someone as cold as you right now.",
      "Конечно, я твой фамильяр — но не хочу слушать такую холодную, как ты сейчас."),
239: ("Y-You! When I'm quiet, you say whatever you like...!",
      "Т-Ты! когда я молчу, ты говоришь что хочешь…!"),
240: ("I'm not exactly easy about it either!", "Мне самой нелегко, знаешь ли!"),
241: ("Oh dear, you two are still on such good terms.", "Ой, вы двое всё так же ладите."),
242: ("Waste of time.", "Потеря времени."),
243: ("Wait, Louise. Someone's coming.", "Подожди, Луиза. Кто-то идёт."),
244: ("Enemy?", "Враг?"),
245: ("Saito...-san? Is Saito-san here?", "Сайто-сан? Вы здесь, Сайто-сан?"),
246: ("That voice—Siesta? But all commoners were told to evacuate to the cafeteria.",
      "Этот голос — Сиеста? Но всем жителям велели эвакуироваться в столовую."),
247: ("But I was worried about you, Saito-san, so I came here.",
      "Но я волновалась за вас, Сайто-сан, и пришла сюда."),
248: ("All right, I'll open up now.", "Ладно, сейчас открою."),
249: ("Hey, partner, wait a...", "Эй, приятель, подожди…"),
250: ("Siesta, you're safe... Waah!?", "Сиеста, ты жива… Вау!?"),
251: ("Die, Saito-san!", "Умри, Сайто-сан!"),
252: ("H-Hey, Siesta. Why are you holding a knife...?", "Э-Эй, Сиеста. Зачем у тебя нож…?"),
253: ("Die, Saito-san... It's your fault...", "Умри, Сайто-сан… Это твоя вина…"),
254: ("Everyone's in danger and you're fooling around with Miss Valliere...",
      "Все в опасности, а вы забавляетесь с мисс Вальер…"),
255: ("Just die... If you won't value me, you can die with me...",
      "Умри… Если ты не ценишь меня, умри вместе со мной…"),
256: ("S-Siesta! What on earth are you...", "С-Сиеста! Что ты…"),
257: ("Die-die-die-die-die... Ufufufufufufufufu...", "Умри-умри-умри-умри… Уф-фу-фу-фу-фу-фу…"),
258: ("Hey partner, put up a fight! We'll be killed at this rate!",
      "Эй, приятель, защитись! Так нас убьют!"),
259: ("B-But attacking Siesta...", "Н-Но нападать на Сиесту…"),
260: ("You can't be serious! Now's not the time!", "Ты что, серьёзно! Сейчас не время!"),
261: ("I'm not saying kill her, you idiot!", "Я не говорю убить её, дурак!"),
262: ("B-But... Waaah!", "Н-Но… Вауу!"),
263: ("Derf, can't you do anything!?", "Дерф, неужели ты ничего не можешь!?"),
264: ("Do something!? It's your fault for opening the door defenseless!",
      "Сделать!? Это твоя вина, что ты открыл дверь беззащитным!"),
265: ("B-But... Waaah!", "Н-Но… Вауу!"),
266: ("Somebody help!", "Кто-нибудь, помогите!"),
267: ("Why are you whimpering! Somebody, er...", "Что за жалкий голос! Кто-нибудь, э-э…"),
268: ("Wah!? Siesta, stop—!", "Ай!? Сиеста, прекрати—!"),
269: ("Hah.", "Ха."),
270: ("Ah? Ugh.", "А? Ох."),
271: ("Tabitha? What did you...?", "Табаса? Что ты…?"),
272: ("No problem. Just knocked her out.", "Всё в порядке. Просто оглушила."),
273: ("Still, why would she try to kill darling? I can't say she has no reason, though...",
      "И всё же, почему она хотела убить дорогого? Не сказать, что причин нет…"),
274: ("Wait. Something's wrong, isn't it? Siesta trying to kill someone...",
      "Подожди. Что-то не так, правда? Сиеста пытается убить…"),
275: ("Hypnosis magic.", "Магия гипноза."),
276: ("Eh?", "А?"),
277: ("The forbidden art that controls the heart.", "Запретное искусство, управляющее сердцем."),
278: ("Could anyone even use that? It's forbidden, isn't it?",
      "Неужто кто-то может её применять? Ведь это запрещено, правда?"),
279: ("I don't know. What Reconquista uses and how they fight...",
      "Понятия не имею. Что использует Реконкиста и как воюет…"),
280: ("Anyway, what do we do with Siesta? We can't just leave her.",
      "В любом случае, что нам делать с Сиестой? Не оставлять же её просто так."),
281: ("Fine. Tie her up and put her in the wardrobe.", "Ладно. Свяжем её и запрём в шкаф."),
282: ("Hey now.", "Эй, давай не так."),
283: ("It's fine. Once everything's over, I'll figure something out.",
      "Всё хорошо. Когда всё закончится, я что-нибудь придумаю."),
284: ("More importantly, it's getting noisy outside. We should move soon.",
      "Главное — снаружи становится шумно. Нам пора перемещаться."),
285: ("Reconquista soldiers, huh...", "Солдаты Реконкисты, значит…"),
286: ("Haa, haa...", "Хаа, хаа…"),
287: ("We made it this far, it seems.", "Кажется, мы добрались сюда."),
288: ("You really can tell they're trained soldiers. No wasted movement.",
      "И правда видно, что это обученные солдаты. Ни одного лишнего движения."),
289: ("If they've gotten this far, things are serious. Saito, there's no time left.",
      "Раз они зашли так далеко — дела плохи. Сайто, времени больше нет."),
290: ("Right, partner. I know what you want to say to the noble girl—but...",
      "Верно, приятель. Я знаю, что ты хочешь сказать этой дворянке — но…"),
291: ("This isn't the time to argue.", "Сейчас не время спорить."),
292: ("We need the Zero Fighter's power now.", "Сейчас нужна сила Zero Fighter."),
293: ("Got it.", "Понял."),
294: ("The remaining soldiers will come eventually. We'll handle them.",
      "Остальные солдаты тоже подойдут. Мы с ними справимся."),
295: ("But Kirche and the others alone...", "Но Кирке и остальные одни…"),
296: ("Tabitha and I can hold out quite a while. Playing for time is boring, though...",
      "Мы с Табасой продержимся довольно долго. Только роль отвлекающей приманки скучна…"),
297: ("But if the academy stays occupied, we're stuck anyway. You two move.",
      "Но если академия останется захваченной, мы всё равно в тупике. Вы двое действуйте."),
298: ("Now go. And bring reinforcements quickly to help us, my darling.",
      "Ну же, идём. И быстро приведи подкрепление, чтобы помочь нам, дорогой."),
}
CHOICES = {
708: [("But attacking Siesta...", "Но нападать на Сиесту…"),
      ("Derf, can't you do anything!?", "Дерф, неужели ты ничего не можешь!?"),
      ("Somebody help!", "Кто-нибудь, помогите!")],
}
SPK = {'サイト': 's', 'ルイズ': 'l', 'オスマン': 'o', 'コルベール': 'c',
       'アキナ': 'ak', 'キュルケ': 'k', 'デルフリンガー': 'd',
       'モンモランシー': 'm', 'タバサ': 't', 'ウェザリー': 'w',
       'シエスタ': 'si', 'null': 'th'}
START = {'s': 127, 'l': 93, 'o': 0, 'c': 9, 'ak': 23, 'k': 11,
         'd': 12, 'm': 9, 't': 8, 'w': 0, 'si': 0, 'th': 0}


def main():
    data = json.load(open('reports/ch18/parse_696_738.json', encoding='utf-8'))
    script = ['# Глава 18, часть 2 (сцены 706–713): осада академии.',
              '# Источник: ps2_source/chapters/chapter_19_貴族の意地.txt (SCENE 706-713).',
              '', 'label ch18_2:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 713:
                break
            if x['no'] < 706:
                continue
            scene = x['no']
            script += ['label ch18_2_scene_%d:' % scene, '']
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
            tag = 'ch18_%s_%03d' % (spk, counters[spk])
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
                ctext = '%s{#ch18_2_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch18_2_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 706 <= scene <= 713:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch18_2_scene_%d' % x['target']
                                          if 706 <= x['target'] <= 713 else 'ch18_3'))
            script.append('')
    script += ['    # ==== КОНЕЦ ЧАСТИ 2 ====', '    jump ch18_3', '    return', '']
    files = {
        'game/chapters/18/script-ch18_2.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch18_2_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch18_2_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch18_2_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch18_2_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch18/voice_map_2.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
