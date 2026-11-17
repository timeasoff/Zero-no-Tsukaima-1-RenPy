#!/usr/bin/env python3
"""Chapter 18 part 4 (scenes 724-738): Louise breaks down, Colbert's plan."""
import json
import sys
sys.path.insert(0, 'tools')
from gen_ch12_1 import event, en_norm

T = {
346: ("Right, let's try to reach the professor's lab somehow. We have nowhere else to go.",
      "Ладно, попробуем добраться до лаборатории сэнсэя. Другого выхода нет."),
347: ("Wait, Saito! That's far too dangerous.", "Подожди, Сайто! Это слишком опасно."),
348: ("Then... what should we do?", "Тогда… что нам делать?"),
349: ("I guess we have to retreat for now.", "Наверное, придётся пока отступить."),
350: ("Retreat... to where?", "Отступить… куда?"),
351: ("Um... Damn, I can't think of anywhere. We're boxed in, huh.",
      "Э-Э… Чёрт, ничего не приходит в голову. Мы в ловушке, да?"),
352: ("Damn it... What do we do?", "Чёрт… Что нам делать?"),
353: ("We can't just stay here. Is there anywhere still safe?",
      "Здесь оставаться нельзя. Есть ли место, где ещё безопасно?"),
354: ("In this situation, I wouldn't count on that either...",
      "В такой ситуации и на это нельзя рассчитывать…"),
355: ("To fly the Zero Fighter, we need an open space in the first place.",
      "Чтобы поднять Zero Fighter, нужно открытое пространство."),
356: ("With this many soldiers around, even with gasoline, we can't just take off.",
      "Столько солдат вокруг — даже с бензином не просто взлететь."),
357: ("No! I have to save everyone...", "Нет! Я должна спасти всех…"),
358: ("Hah? What are you talking about?", "А? Что ты говоришь?"),
359: ("I have to protect the Queen, the headmaster, everyone at the academy—all of them.",
      "Я должна защитить Королеву, директора, всех в академии — всех."),
360: ("Because I'm the wielder of Void. The legendary mage. That's why I won the last war.",
      "Потому что я — носитель Пустоты. Легендарный маг. Поэтому я победила в прошлой войне."),
361: ("This time too... Yes—even if it costs me my life.",
      "И на этот раз… Да — даже если это будет стоить мне жизни."),
362: ("You stupid idiot!", "Глупая!"),
363: ("Why did you hit me...? You familiar, you cur—hitting your mistress!",
      "Зачем ты меня ударил…? Фамильяр, пёс — бить свою госпожу!"),
364: ("Yeah, I hit you. Look, Louise. There's one thing I just can't accept.",
      "Да, ударил. Слушай, Луиза. Есть одна вещь, которую я никак не могу принять."),
365: ("Why are you nobles so ready to throw your lives away?",
      "Почему вы, дворяне, так легко готовы расстаться с жизнью?"),
366: ("It's not because I'm a noble. Unless I use Void, the crisis facing Tristain can't be stopped.",
      "Дело не в том, что я дворянка. Без Пустоты кризис, грозящий Тристании, не остановить."),
367: ("Then isn't it natural to do what I can?", "Тогда разве не естественно делать то, что я могу?"),
368: ("Louise... But right now, you're clearly pushing yourself too hard.",
      "Луиза… Но сейчас ты явно перегибаешь."),
369: ("...!", "…!"),
370: ("Sure, you're a Void mage. Even I can see that power is incredible.",
      "Конечно, ты маг Пустоты. Даже я вижу, что эта сила невероятна."),
371: ("But, Louise... you're just a girl.", "Но Луиза… ты просто девушка."),
372: ("Right now you're pretending to be strong, aren't you? You're scared, aren't you? "
      "I can't stand seeing you like that.",
      "Сейчас ты храбришься, да? Ты боишься, правда? Я не могу смотреть на такую Луизу."),
373: ("Try to value yourself more. Like you always do with me—it's fine to be a selfish Louise.",
      "Попробуй ценить себя больше. Как ты всегда со мной — можно быть эгоистичной Луизой."),
374: ("Saito...", "Сайто…"),
375: ("So, look...", "Ну, понимаешь…"),
376: ("What would you know about me... what would you know...",
      "Что ты понимаешь во мне… что ты понимаешь…"),
377: ("Louise?", "Луиза?"),
378: ("You never listen to your mistress, you fawn over girls, you're useless and yet "
      "you eat like there's no tomorrow...",
      "Ты не слушаешь госпожу, увиваешься за девушками, ни на что не годишься, "
      "но при этом ешь как безумный…"),
379: ("I don't want to hear that from you—you know nothing of the burden of being born "
      "a noble, or of staying one...",
      "Не хочу это слышать от тебя — ты не знаешь ни тяжести родиться дворянкой, "
      "ни того, каково оставаться ею…"),
380: ("I don't want to hear it...!", "Не хочу слушать…!"),
381: ("...", "…"),
382: ("I'm scared of using Void magic too, you know...", "Я и сама боюсь применять Пустоту, знаешь ли…"),
383: ("They call it legendary magic, but I have no idea what it even is.",
      "Называют легендарной магией, а я даже не понимаю, что это."),
384: ("Maybe using it will kill me.", "Может, она убьёт меня."),
385: ("I want to live a happier life too. But this is the magic I finally got.",
      "Я и сама хочу жить радостнее. Но это магия, которую я наконец получила."),
386: ("The Zero Louise, the Zero Louise they mocked me as...",
      "Меня дразнили «Нулиза», «Нулиза»…"),
387: ("This is the first thing I've ever had that isn't zero... sniff, ugh...",
      "Это первая вещь в моей жизни, которая не нуль… всхлип, ох…"),
388: ("Loui...", "Луи…"),
389: ("Idiot... Don't look at me, don't talk to me...!", "Дурак… Не смотри на меня, не говори со мной…!"),
390: ("As my familiar, you shouldn't see your mistress crying...!",
      "Фамильяр не должен видеть, как его госпожа плачет…!"),
391: ("Louise...", "Луиза…"),
392: ("W-What is it... Are you pitying me?", "Ч-Что… Ты меня жалеешь?"),
393: ("That's not it... no.", "Нет… не то."),
394: ("It's just... I couldn't leave you alone, that's all.", "Просто… я не смог оставить тебя, вот и всё."),
395: ("...", "…"),
396: ("Eek!?", "Ай!?"),
397: ("Who's there!", "Кто там!"),
398: ("Now, now, surely you can put that sword away, Saito-kun.", "Ну-ну, убери меч, Сайто-кун."),
399: ("That voice... Mr. Colbert?", "Этот голос… Кольбер-сэн?"),
400: ("Indeed. And I apologize for interrupting.", "Так и есть. И прошу прощения, что помешал."),
401: ("But as you know, things are critical inside and outside the academy. "
      "I hope you'll forgive the breach of etiquette.",
      "Но, как вы знаете, сейчас и внутри, и снаружи академии чрезвычайная ситуация. "
      "Надеюсь, вы простите мне нарушение этикета."),
402: ("N-Not at all... I-I'm fine!", "Н-Нет… Я-Я в порядке!"),
403: ("By the way, professor, you're safe—that's good.", "Кстати, сэнсэй, вы живы — хорошо."),
404: ("Old Osmond asked me to find you. I'm glad we met up safely.",
      "Старик Осман просил меня найти вас. Рад, что мы благополучно встретились."),
405: ("From the headmaster?", "От директора?"),
406: ("Yes. Though it seems our last hope—this Zero Fighter—is in a sorry state.",
      "Да. Хотя наша последняя надежда — этот Zero Fighter — похоже, в плохом состоянии."),
407: ("Eh, we're short on gasoline... Don't you have a spare, professor?",
      "А, не хватает бензина… Нет ли запасного, сэнсэй?"),
408: ("Sorry. With all the recent turmoil, I neglected the refining. "
      "This is a lifelong shame for me.",
      "Простите. Из-за всей этой кутерьмы я запустил перегонку. Это позор на всю жизнь."),
409: ("I see...", "Понятно…"),
410: ("Still, now that the Zero Fighter is unusable, staying here is dangerous.",
      "И всё же, раз Zero Fighter не годится, оставаться здесь опасно."),
411: ("In fact, most of the academy is now under Reconquista's control.",
      "Более того, почти вся академия теперь под контролем Реконкисты."),
412: ("For now, let's put an invisibility spell on the Zero Fighter. "
      "We can't let it be destroyed.",
      "Пока наложим на Zero Fighter заклинание невидимости. Нельзя, чтобы его разрушили."),
413: ("Now, first we need to hide. And I know just the place for it.",
      "Теперь главное — укрыться. И я знаю идеальное место."),
414: ("Is there such a place left in the academy? From what you say, we can neither "
      "flee nor hide...",
      "Неужели в академии осталось такое место? Судя по вашим словам, мы не можем "
      "ни бежать, ни спрятаться…"),
415: ("R-Right, Mr. Colbert. Isn't staying inside the academy more dangerous?",
      "В-Верно, Кольбер-сэн. Не опаснее ли оставаться в академии?"),
416: ("Come now, Saito-kun has been there several times, haven't you? "
      "It's my lab.",
      "Ну же, Сайто-кун там бывал не раз, правда? Это моя лаборатория."),
417: ("Could it be Louise's room?", "Неужели комната Луизы?"),
418: ("That can't be. Why would my room be a perfect hiding place?",
      "Не может быть. Почему моя комната — идеальное укрытие?"),
419: ("Well, it's, you know, outsmarting the enemy, or...", "Ну, это, понимаешь, обхитрить врага, или…"),
420: ("Come now, Saito-kun has been there several times, haven't you? It's my lab.",
      "Ну же, Сайто-кун там бывал не раз, правда? Это моя лаборатория."),
421: ("Surely not the professor's lab?", "Неужели лаборатория сэнсэя?"),
422: ("The lab?", "Лаборатория?"),
423: ("Exactly. Correct, Saito-kun.", "Именно. Правильно, Сайто-кун."),
424: ("Eh, but the professor's lab is pretty deep inside the school building... "
      "We'll be spotted, won't we?",
      "А, но лаборатория сэнсэя глубоко в здании… Нас заметят, правда?"),
425: ("True, the official route would be dangerous. Yes, the official route is dangerous.",
      "Верно, официальный путь опасен. Да, официальный путь опасен."),
426: ("Mr. Colbert... surely not.", "Кольбер-сэн… неужели."),
427: ("Allow me to guide you, Miss Valliere and Saito-kun. This is... "
      "the shortcut to my lab.",
      "Позвольте провести вас, мисс Вальер и Сайто-кун. Это… "
      "короткий путь к моей лаборатории."),
428: ("E-Eh!?", "А-А!?"),
429: ("This is, could it be...", "Это, неужели…"),
430: ("A secret tunnel!?", "Тайный ход!?"),
431: ("This is exactly why I'm called the ever-appearing Colbert, you two.",
      "Вот почему меня называют «появляющийся ниоткуда Кольбер»."),
432: ("Now, onward! To my beloved lab!", "Ну же, вперёд! К моей родной лаборатории!"),
433: ("Heh. This is a bit of an adventure, isn't it? Right, Louise?", "Хе. Это как приключение, да? Луиза?"),
434: ("Don't ask me.", "Не спрашивай меня."),
435: ("Come in, it's a bit of a mess.", "Входите, тут немного беспорядок."),
436: ("Pardon the intrusion...", "Простите за вторжение…"),
437: ("Excuse us.", "Извините."),
438: ("Right, without further ado. The academy is currently under Reconquista's control.",
      "Так, без лишних слов. Академия сейчас под контролем Реконкисты."),
439: ("The only exception is this place, more or less.", "Единственное исключение — это место, более-менее."),
440: ("This lab is quite far from the academy, and from the outside it looks like "
      "just a stone shack.",
      "Эта лаборатория далеко от академии, а снаружи выглядит как простая каменная хижина."),
441: ("And I probably understand the situation better than anyone here. Because...",
      "И я, наверное, понимаю обстановку лучше всех здесь. Потому что…"),
442: ("Eek, a m-mouse!?", "Ай, м-мышь!?"),
443: ("Oh, don't crush it. This is no ordinary mouse.", "Ой, не раздави её. Это не обычная мышь."),
444: ("Believe it or not, it's Old Osmond's familiar.", "Поверите или нет — это фамильяр старика Османа."),
445: ("This? It just looks like a small white mouse...", "Это? Она просто маленькая белая мышка…"),
446: ("Don't judge by appearances, Miss Valliere. That goes for your familiar too.",
      "Не судите по внешности, мисс Вальер. Это касается и вашего фамильяра."),
447: ("E-Eh... Well, yes.", "А-А… Ну, да."),
448: ("I was given a task before Old Osmond entered negotiations with Akina.",
      "Мне дали задание до того, как Осман начал переговоры с Акиной."),
449: ("I was entrusted with this familiar—Mortosgnir.",
      "Мне вручили этого фамильяра — Мортогнира."),
450: ("Through him, I've been in contact with Old Osmond, confined in the headmaster's office.",
      "Через него я связываюсь со стариком Османом, запертым в кабинете директора."),
451: ("H-Haa... Is that so.", "Х-Ха… Вот как."),
452: ("(How does one even communicate with a mouse...?)", "(Как вообще общаться с мышью…?)"),
453: ("Now, here's the important part. Weatherly's target is the Void mage and her familiar...",
      "Теперь главное. Цель Уэзерби — маг Пустоты и её фамильяр…"),
454: ("In other words, information on Miss Valliere and Saito-kun, and probably capturing you both.",
      "Иными словами, сведения о мисс Вальер и Сайто-куне и, вероятно, ваше задержание."),
455: ("Plus, seizing the magic items the academy has collected and learning how to use them.",
      "Плюс захват магических предметов, собранных академией, и сведений об их действии."),
456: ("Old Osmond has steadfastly refused all of Weatherly's demands.",
      "Старик Осман твёрдо отклоняет все требования Уэзерби."),
457: ("In response, Weatherly threatens to wipe out everyone inside the academy, "
      "teachers and students alike.",
      "В ответ Уэзерби угрожает уничтожить всех в академии — и преподавателей, и учеников."),
458: ("Naturally, the means would be Akina's bombs and a barrage from the aerial ships.",
      "Естественно, это бомбы Акины и залп с воздушных кораблей."),
459: ("I hear the capital, Tristain, is in terrible shape too—street fighting, "
      "the approaching Reconquista fleet.",
      "Слышал, что и столица Тристания в тяжёлом положении — уличные бои, "
      "приближение флота Реконкисты."),
460: ("We can't expect reinforcements. The same goes for the surrounding nobles.",
      "На подкрепление рассчитывать не приходится. То же и с окрестными дворянами."),
461: ("So I'd like to take charge of this incident myself.",
      "Поэтому я хочу сам взять руководство этим делом."),
462: ("H-Haa...", "Х-Ха…"),
463: ("The operation has several goals. First, eliminate the enemy forces inside the academy.",
      "У операции несколько целей. Во-первых, уничтожение вражеских сил внутри академии."),
464: ("Then, neutralizing and restraining Weatherly—the operation's commander—and Akina.",
      "Далее — обезвреживание и задержание Уэзерби, командующей операцией, и Акины."),
465: ("Disarming the bombs planted around the academy is also pending, but probably "
      "only Akina can handle them.",
      "Обезвреживание бомб по всей академии тоже в повестке, но, вероятно, "
      "справиться с ними может только Акина."),
466: ("If we restrain her, the bomb threat disappears.",
      "Если мы её задержим, угроза бомб исчезнет."),
467: ("Finally... here's the problem—the aerial ship lounging above the academy.",
      "И напоследок… вот проблема — воздушный корабль, расположившийся над академией."),
468: ("This one is difficult. Left alone, it could link up with Reconquista's main fleet.",
      "С ним сложно. Оставленный без присмотра, он может соединиться с главным флотом Реконкисты."),
469: ("If only I could get the Zero Fighter running... One ship, I think I could manage.",
      "Хоть бы завести Zero Fighter… С одним кораблём я бы, кажется, справился."),
470: ("Mm...", "Мм…"),
471: ("Wishing for what we don't have is pointless. We'll have to improvise...",
      "Желать того, чего нет, бесполезно. Придётся действовать по обстоятельствам…"),
472: ("I'll do it.", "Я сделаю это."),
473: ("Hm? Miss Valliere, you just said...", "Хм? Мисс Вальер, вы только что сказали…"),
474: ("I'll take that battleship.", "Я возьму на себя тот боевой корабль."),
475: ("Louise, surely you don't mean...", "Луиза, неужели ты…"),
476: ("Yes. I'll use Void magic. Fortunately, they don't seem to know exactly "
      "what my Void magic does.",
      "Да. Я применю Пустоту. К счастью, они, похоже, не знают точно, "
      "что делает моя магия."),
477: ("If nobody knows its full nature, it should surprise them—and be quite effective.",
      "Если никто не знает её сути, это застанет врага врасплох и даст немалый эффект."),
478: ("What do you think, Mr. Colbert?", "Как считаете, Кольбер-сэн?"),
479: ("Hmm... Yes, it's worth trying. But how good are our chances?",
      "Хм… Да, стоит попробовать. Но каковы наши шансы?"),
480: ("No, Louise's power is... I mean, we might turn the whole academy to ash with it.",
      "Нет, сила Луизы — я хочу сказать, мы можем превратить всю академию в пепел."),
481: ("W-What was that!?", "Ч-Что это было!?"),
482: ("I mean, back then too...", "Ну, и в тот раз тоже…"),
483: ("Louise... what do you intend to use? Surely not that thing from the other day...?",
      "Луиза… что ты собираешься применить? Неужели ту штуку на днях…?"),
484: ("E-Er, I don't understand it myself.", "Э-Э, я и сам не понимаю."),
485: ("It's fine! I'll take that battleship down perfectly!", "Всё хорошо! Я точно свергну тот корабль!"),
486: ("Surely not that thing from the other day...?", "Неужели ту штуку на днях…?"),
487: ("You don't think I'd use Explosion, do you?", "Неужели ты думаешь, что я примену «Взрыв»?"),
488: ("Eh... Isn't it?", "А… разве нет?"),
489: ("Even I can imagine what would happen if I used Explosion in the academy.",
      "Даже я могу представить, что случится, применю я «Взрыв» в академии."),
490: ("Eh, so that means...", "А, то есть…"),
491: ("I'll use a new spell. The right magic for a situation like this.",
      "Я применю новое заклинание. Магию, подходящую для такого случая."),
492: ("If it works, we can retake the academy without a single casualty.",
      "Если получится, мы отберём академию без единой жертвы."),
493: ("I can trust you, right?", "Я могу тебе верить, да?"),
494: ("I'm your mistress. Who else would you trust?", "Я твоя госпожа. Кому же ещё тебе верить?"),
495: ("Got it. Let's bet on my mistress, then.", "Понял. Тогда поставим на госпожу."),
496: ("Looks like mistress and familiar have come to an agreement. Then I'll help too.",
      "Похоже, госпожа и фамильяр пришли к согласию. Тогда и я помогу."),
497: ("Help?", "Помочь?"),
498: ("About Weatherly.", "С Уэзерби."),
499: ("Weatherly?", "С Уэзерби?"),
500: ("Do you remember the strange sound in the headmaster's office?",
      "Помните странный звук в кабинете директора?"),
501: ("The truth is, Weatherly seems to be a user of mind-controlling magic. "
      "She controls hearts through sound.",
      "Дело в том, что Уэзерби, похоже, владеет магией управления разумом. "
      "Она управляет сердцами через звук."),
502: ("Like hypnosis?", "Как гипноз?"),
503: ("It's magic I've never seen before. Probably unique to Weatherly.",
      "Это магия, которой я никогда не видел. Вероятно, её собственная."),
504: ("And Akina-kun? She must be controlling Haruna-kun in a similar way.",
      "И Акина-кун? Она наверняка управляет Харуной похожим способом."),
505: ("Isn't there a way to counter it?", "Неужели нет способа противостоять этому?"),
506: ("Look at this.", "Посмотрите на это."),
507: ("(As he said that, Professor Colbert took out some small wooden object.)",
      "Сказав это, Кольбер-сэн вытащил какой-то небольшой деревянный предмет."),
508: ("Um... What's this? It looks like earplugs.", "Э-Э… Что это? Похоже на беруши."),
509: ("As you see, earplugs. Though enchanted with a special wind spell.",
      "Как видите, беруши. Только с особым заклинанием ветра."),
510: ("With these in, Weatherly's magic will be nullified when she tries it.",
      "С ними — когда Уэзерби применит свою магию, она будет нейтрализована."),
511: ("Amazing. Made in no time...", "Удивительно. Сделать так быстро…"),
512: ("Ah, no—it's mostly thanks to Old Osmond's help. Quite the headmaster, isn't he?",
      "А, нет — это в основном заслуга старика Османа. Настоящий директор, да?"),
513: ("Can this bring Haruna back?", "Это вернёт Харуну?"),
514: ("Sadly, that will be difficult.", "К сожалению, это будет трудно."),
515: ("Even if we stop the control, removing the personality created in her mind "
      "won't be easy.",
      "Даже если мы прервём управление, убрать созданную в её разуме личность "
      "будет непросто."),
516: ("I see...", "Понятно…"),
517: ("I managed to prepare about ten of these. Use them when calling on Miss Zerbst "
      "or Miss Tabitha for help.",
      "Мне удалось сделать около десяти штук. Используйте их, когда будете "
      "звать на помощь мисс Церпст или мисс Табасу."),
518: ("According to Mortosgnir, those two haven't been captured yet.",
      "По словам Мортогнира, те двое пока не взяты в плен."),
519: ("Mr. Colbert, thank you for your efforts.", "Кольбер-сэн, спасибо за ваши старания."),
520: ("Good. Now that we have a countermeasure, let's hold a real strategy meeting.",
      "Хорошо. Теперь, когда есть средство защиты, проведём настоящий военный совет."),
521: ("(In the end, our plan to retake the academy was set for just after dawn.)",
      "В итоге план отвоевать академию назначили на сразу после рассвета."),
522: ("(The enemy soldiers would be slower then, and Louise wanted to reach the "
      "capital as soon as possible.)",
      "Тогда вражеские солдаты должны быть медленнее, и Луиза хотела как можно "
      "скорее добраться до столицы."),
523: ("(So we decided to turn in early to prepare for tomorrow—but...)",
      "Мы решили лечь пораньше, чтобы подготовиться к завтрашнему дню, но…"),
524: ("(No good. I slept lightly for the first two or three hours, then couldn't "
      "sleep anymore.)",
      "Не вышло. Я легко поспал первые два-три часа, а потом уже не мог уснуть."),
525: ("(I feel like something like this happened not too long ago...)",
      "Кажется, подобное уже случалось совсем недавно…"),
526: ("(I really only ever act the same way, don't I...)", "Я и правда всегда действую одинаково, да…"),
}
CHOICES = {
728: [("Is there such a place in the academy?", "Неужели в академии есть такое место?"),
      ("Louise's room?", "Комната Луизы?"),
      ("The professor's lab?", "Лаборатория сэнсэя?")],
733: [("No, that's a bit much...", "Нет, это слишком…"),
      ("What is Louise going to use?", "Что Луиза собирается применить?"),
      ("Oh, even I don't get it", "О, я и сам не понимаю")],
}
SPK = {'サイト': 's', 'ルイズ': 'l', 'コルベール': 'c', '兵士ＭＳ': 'soldier',
       'デルフリンガー': 'd', 'null': 'th'}
START = {'s': 183, 'l': 132, 'c': 13, 'soldier': 11, 'd': 25, 'th': 0}


def main():
    data = json.load(open('reports/ch18/parse_696_738.json', encoding='utf-8'))
    script = ['# Глава 18, часть 4 (сцены 724–738): кризис, лаборатория Кольбера, новый план.',
              '# Источник: ps2_source/chapters/chapter_19_貴族の意地.txt (SCENE 724-738).',
              '', 'label ch18_4:', '    $ tndl(None)', '    $ show_sprites()', '']
    counters = dict(START)
    ja_d, ru_d, ja_c, ru_c = [], [], [], []
    manifest = []
    scene = None
    for x in data:
        k = x['kind']
        if k == 'scene':
            if x['no'] > 738:
                break
            if x['no'] < 724:
                continue
            scene = x['no']
            script += ['label ch18_4_scene_%d:' % scene, '']
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
                ctext = '%s{#ch18_4_c_%d_%d}' % (en_norm(en), scene, i + 1)
                script.append('        "%s":' % ctext)
                script.append('            jump ch18_4_scene_%d' % o['target'])
                ja_c += ['    old "%s"' % ctext, '    new "%s"' % o['text'], '']
                ru_c += ['    old "%s"' % ctext, '    new "%s"' % ru, '']
            script.append('')
            continue
        if k == 'goto':
            if scene is None or not 724 <= scene <= 738:
                continue
            script.append('    # → next scene %d' % x['target'])
            script.append('    jump %s' % ('ch18_4_scene_%d' % x['target']
                                          if 724 <= x['target'] <= 738 else 'ch19'))
            script.append('')
    script += ['    # ==== КОНЕЦ ГЛАВЫ 18 ====', '    jump attention', '    return', '']
    files = {
        'game/chapters/18/script-ch18_4.rpy': '\n'.join(script) + '\n',
        'game/tl/japanese/ch18_4_dialogs.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_d) + '\n',
        'game/tl/russian/ch18_4_dialogs.rpy': '\n'.join(['# translate russian strings:', ''] + ru_d) + '\n',
        'game/tl/japanese/ch18_4_choises.rpy': '\n'.join(['# translate japanese strings:', ''] + ja_c) + '\n',
        'game/tl/russian/ch18_4_choises.rpy': '\n'.join(['# translate russian strings:', ''] + ru_c) + '\n',
    }
    for p, body in files.items():
        open(p, 'w', encoding='utf-8').write(body)
        print('wrote', p, len(body))
    with open('reports/ch18/voice_map_4.csv', 'w', encoding='utf-8') as f:
        f.write('voice_name,voice_id\n')
        for v, i in manifest:
            f.write('%s,%d\n' % (v, i))
    print('voices', len(manifest), counters)


if __name__ == '__main__':
    main()
