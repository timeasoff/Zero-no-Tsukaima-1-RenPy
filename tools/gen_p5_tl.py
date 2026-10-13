# -*- coding: utf-8 -*-
"""Генератор TL-блоков для главы 3, части 5 (сцены 169-178 + ветки 1322-1341).

EN old берётся из script-ch3_5.rpy (порядок следования), JA new — из канона
chapter_04 (склейка многострочных реплик, мысли в （ ） — как в источнике),
RU new — таблица RU по EN old. Порядок EN/JA сверен инструментами
p5_check_voices.py / p5_check_sprites.py (193 реплики + 19 пунктов меню).

Запуск: python tools/gen_p5_tl.py
"""
import io
import re
import sys

sys.path.insert(0, "tools")
import p5_check_sprites as pcs  # noqa: E402  (парсер канона)

SCRIPT = "game/chapters/3/script-ch3_5.rpy"

# RU-переводы, ключ = точная EN-строка скрипта (все 212 строк уникальны).
RU = {
    # ==== SCENE 169 ====
    "Louise started this, didn't she?":
        "Это же Луиза затеяла, да?",
    "...{#ch3.5_l_001}": "...",
    "Why the silence? So I'm right?":
        "Почему молчишь? Значит, я прав?",
    "...{#ch3.5_l_002}": "...",
    "N-no, that's wrong, Saito-san! This was my idea, and—":
        "Н-нет, это не так, Сайто-сан! Это я всё затеяла, и—",
    "Sorry, Siesta, but could you keep quiet?":
        "Прости, Сиеста, но можешь помолчать?",
    "This isn't like the usual Siesta.":
        "Это не похоже на обычную Сиесту.",
    "I'm sorry…":
        "Простите…",
    "To think Siesta would do something like this… I'm disappointed.":
        "Никогда бы не подумал, что Сиеста на такое способна… Разочарован.",
    "Gahn!?":
        "Га-н!?",
    "Saito! That was way too much!":
        "Сайто! Это было уже через чур!",
    "I don't think so.":
        "Не думаю.",

    # ==== SCENE 170 ====
    "Do you two dislike Haruna?":
        "Вы двое что, недолюбливаете Харуну?",
    "Not at all, we don't dislike her… It's just that…":
        "Совсем нет, мы её не недолюбливаем… Просто…",
    "Because Saito keeps fussing over Haruna…":
        "Потому что Сайто всё время хлопочет только о Харуне…",
    "So you resort to pranks like this? That's going too far, you know.":
        "И ради этого вы устроили такую проделку? Это перебор, знаете ли.",

    # ==== SCENE 171 ====
    "I'm being serious here, you know! I'm really angry!":
        "Я серьёзно, понимаешь! Я правда зол!",
    "…I'm sorry.":
        "…Простите.",
    "...{#ch3.5_l_005}": "...",

    # ==== SCENE 172 ====
    "I had Siesta put the bedding away and opened the windows to air the room out. Finally, the temperature settled down.":
        "Я попросил Сиесту убрать постель, открыл окна, чтобы проветрить комнату. Наконец температура улеглась.",
    "Haruna, are you okay? You're not feeling sick?":
        "Харуна, ты в порядке? Тебе не дурит?",
    "Yeah, I'm fine now…":
        "Да, уже всё в порядке…",
    "That's good…":
        "Это хорошо…",

    # ==== SCENE 173 ====
    "As if we're the ones in the wrong…":
        "Да мы ж не виноваты…",
    "That's right. It seems Saito-san dislikes us…":
        "Верно. Кажется, Сайто-сан нас не жалует…",
    "No, I'm not saying you're bad or that I hate you. I'm saying you went too far.":
        "Нет, я не говорю, что вы плохие или что вы мне неприятны. Я говорю, что вы зашли слишком далеко.",
    "But… Hey, Siesta?":
        "Но… Эй, Сиеста?",
    "Yes… Saito-san wouldn't understand.":
        "Да… Сайто-сан не поймёт.",
    "…Good grief.":
        "…Ну и ну.",
    "Well then, Saito-san… I have work to do, so…":
        "Тогда, Сайто-сан… У меня есть работа, так что…",
    "I see. Hang in there, Siesta…":
        "Понятно. Держись, Сиеста…",
    "Yes…":
        "Да…",
    "Did I make Siesta feel down…?":
        "Я не загрузил Сиесту…?",
    "…No wonder she's down. Even I…":
        "…Неудивительно, что она расстроена. Даже я…",
    "That doesn't make it okay, does it?":
        "Но это всё равно не оправдание, верно?",
    "Hah… Never mind. I'm going out for a bit.":
        "Фу… Ладно. Я ненадолго выйду.",
    "Should I come with you?":
        "Пойти с тобой?",
    "You don't have to come, Saito. Just go look after cute little Haruna all you like.":
        "Тебе не обязательно идти, Сайто. Только иди ухаживай за милой Харуной сколько душе угодно.",
    "What's with that tone…":
        "Что за тон…",
    "Is it wrong of me to look after Haruna?{#ch3_m173a}":
        "Разве плохо ухаживать за Харуной?",
    "You didn't need to worry about her.{#ch3_m173b}":
        "Я просто волновался за тебя…",
    "I'm just saying something objective.{#ch3_m173c}":
        "Я просто говорю объективно.",

    # ==== SCENE 174 ====
    "Is it really so bad, looking after Haruna?":
        "Разве ухаживать за Харуной такое плохое дело?",
    "Nobody said that!":
        "Никто такого не говорил!",
    "Then why did you do something like that?":
        "Тогда зачем вы это сделали?",
    "...{#ch3.5_l_012}": "...",

    # ==== SCENE 175 ====
    "I was worried about you…":
        "Я волновался за тебя…",
    "W-worried about me?! Is that true?":
        "В-волновался за меня?! Правда?",
    "Well… it's…":
        "Ну… это…",
    "Enough!! I'd rather not hear empty words like that!":
        "Хватит!! Такие слова слышать не хочу!",
    "No, listen, I mean it—":
        "Нет, послушай, я правда—",

    # ==== SCENE 176 ====
    "I'm just stating objective facts.":
        "Я просто констатирую объективные факты.",
    "Is that so…? And you think you're being objective, Saito?":
        "Так ли…? И тебе правда кажется, что ты объективен, Сайто?",
    "Yeah, that's what I think.":
        "Да, я так и считаю.",
    "...{#ch3.5_ha_176}": "...",
    "An-y-way! I'm going out by myself, so you stay here, Saito.":
        "В-во-об-ще-то! Я одна выхожу, а ты оставайся здесь, Сайто.",
    "Fine. Suit yourself.":
        "Ладно. Делай, что хочешь.",
    "Oh, I intend to.":
        "О, я и собиралась.",
    "Jeez, that Louise… Why's she so mad…? I don't get it anymore.":
        "Чёрт, эта Луиза… Что её так бесит… Я уже ничего не понимаю.",

    # ==== SCENE 178 ====
    "Honestly… That Saito gets me so mad!":
        "Да уж… Этот Сайто просто с ума сводит!",
    "…Kirche! It's me, Louise!!":
        "…Кирхе, это я, Луиза!!",
    "Hold on, Louise. Is there really no better way to knock?":
        "Погоди, Луиза. Разве нельзя стучать получше?",
    "I get that you're upset, but taking it out on things isn't the answer.":
        "Понимаю, что ты злишься, но срывать злость на вещах — не выход.",
    "Shut up! I'm coming in!!":
        "Заткнись! Я войду!!",
    "Miss Vallière. How did things go with Saito-san and the others?":
        "Мадемуазель Вальер, как поживают Сайто-сан и остальные?",
    "Ah, hopeless, hopeless. That idiot doesn't suspect for a second that Haruna is faking.":
        "Ах, безнадёжно, безнадёжно. Этот идиот хоть капельки не подозревает, что Харуна притворяется.",
    "I see… So everything we did was pointless, then…":
        "Понятно… Выходит, всё, что мы сделали, было зря…",
    "Not just pointless—it backfired spectacularly.":
        "Не просто зря — оно дало самый настоящий обратный эффект.",
    "See, Tabitha? Just like I said—it failed.":
        "Видишь, Табита? Я же говорила — провалилось.",
    "...{#ch3.5_t_178}": "...",
    "Besides, you two are way too soft. That Haruna girl has her eyes on darling too, right?":
        "Вообще-то вы слишком мягкие. Эта Харуна тоже на Дорогого глаз положила, верно?",
    "Probably.":
        "Наверное.",
    "Even in her shoes, I wouldn't have thrown in the towel.":
        "Даже на её месте я бы не сдалась.",
    "Because even if pushing through the heat made her sick, knowing darling would nurse her back to health is reason enough to keep going…":
        "Потому что даже если жара перетомила бы её, перспектива, что Дорогой будет за ней ухаживать, — достаточная причина продержаться…",
    "In the fairy tale my great-grandfather told me, it did work, though…":
        "В сказке, которую рассказывал мой прадедушка, это, правда, сработало…",
    "What kind of story was it?":
        "Что за история?",
    "Yes, Miss Zerbst. It's the tale of the North Wind and the Sun, competing to strip a traveler of his coat.":
        "Да, мадемуазель Цербст. Это сказка о Северном ветре и Солнце, которые спорили, кто снимет с путника плащ.",
    "In the story, the North Wind tries to blow the coat away, but fails…":
        "В истории Северный ветер пытается сдуть плащ, но не может…",
    "while the Sun, by bathing him in warm sunlight, makes him take it off himself.":
        "а Солнце, заливая путника тёплым светом, побуждает его снять плащ самому.",
    "I see. So it's better to talk someone into taking their clothes off than to tear them off by force.":
        "Понятно. Значит, лучше уговорить человека раздеться, чем рвать одежду силой.",
    "But I didn't think Haruna-san would be this patient…":
        "Но я не думала, что Харуна-сан такая терпеливая…",
    "The schemer drowns in their own scheme.":
        "Хитрый и на хитрости спотыкается.",
    "I'm telling you, Siesta. I thought that same plan would expose Haruna's fake illness too.":
        "Я же говорю, Сиеста. Я думала, тот же план раскроет притворство Харуны.",
    "Then I have no choice. This time, I'll go save darling myself!":
        "Тогда уж ничего не поделаешь. На этот раз я сама пойду спасать Дорогого!",
    "…Wait, what are you planning to do?":
        "…Погоди, что ты замыслила?",
    "Leave it to me. I'll make Haruna herself admit she was faking!":
        "Доверься мне. Я заставлю саму Харуну признать, что она притворялась!",
    "Um, Miss Vallière… Are you sure it's all right to leave everything to Miss Zerbst?":
        "Эм, мадемуазель Вальер… Вы уверены, что всё можно доверить мадемуазель Цербст?",
    "To be honest, I'm worried too…":
        "Честно говоря, я тоже волнуюсь…",
    "I don't think Louise would give up this easily. I should probably go tail her for a bit.":
        "Не верю, что Луиза так легко сдастся. Наверное, надо немного последить за ней.",
    "I wonder where Louise went…?":
        "Куда же подевалась Луиза…?",
    "Louise's room{#ch3_m178a}":
        "Комната Луизы",
    "Kirche's room{#ch3_m178b}":
        "Комната Кирхе",
    "Tabitha's room{#ch3_m178c}":
        "Комната Табиты",
    "The kitchen{#ch3_m178d}":
        "Кухня",

    # ==== SCENE 1322 ====
    "Ah, Hiraga-kun…":
        "А, Хирага-кун…",
    "I came looking for Louise and the others… Looks like they're not here.":
        "Я искал Луизу и остальных… Кажется, их здесь нет.",
    "Yeah. They haven't been here since before.":
        "Да. С тех пор их здесь не было.",
    "I see… Sorry about earlier. Pulling something so awful on a sick person…":
        "Понятно… Прости за раньше. Столь ужасное издевательство над больным…",
    "Yeah, that's already forgotten. It wasn't your fault, Hiraga-kun.":
        "Да, это уже забыто. В том не было твоей вины, Хирага-кун.",
    "Still… why would Louise and Siesta do something like that?":
        "Хотя… зачем Луиза и Сиеста такое затеяли?",
    "Hiraga-kun, do you really not know?":
        "Хирага-кун, ты правда не понимаешь?",
    "Huh? Know what?":
        "А? Чего?",
    "The reason Louise and the others did something like that together…":
        "Причину, по которой Луиза и другие сделали это вместе…",
    "The reason…?":
        "Причина…?",
    "Was it because Haruna took over your room?{#ch3_m1322a}":
        "Может, потому что Харуна заняла твою комнату?",
    "Actually, maybe it was Louise and Siesta's way of nursing her?{#ch3_m1322b}":
        "А если это способ лечения по-ихнему?",
    "Hmm, I have no idea.{#ch3_m1322c}":
        "Хм, не знаю.",

    # ==== SCENE 1323 ====
    "Was it because Haruna took over your room?":
        "Может, потому что Харуна заняла мою комнату?",
    "But if that's the case, I don't get why Siesta would tag along.":
        "Но если так, я не понимаю, зачем в это ввязалась Сиеста.",
    "If anything, Louise would want to kick Siesta out along with Haruna.":
        "Если уж на то пошло, Луиза скорее хотела бы выгнать Сиесту вместе с Харуной.",
    "Hey, Hiraga-kun. Are you serious right now?":
        "Слушай, Хирага-кун, ты сейчас серьёзно?",
    "Pretty much, yeah.":
        "Ну, примерно да.",

    # ==== SCENE 1324 ====
    "Actually, maybe it was Louise and Siesta's way of nursing her?":
        "А если это способ лечения по-ихнему?",
    "Like some kind of treatment—fighting fire with fire, heat with heat?":
        "Какое-то лечение — огнь огнём побеждают, жарой по жаре?",
    "If that's the case, I did something awful to Louise and the others…":
        "Если так, я ужасно прогадал Луизе и остальным…",
    "You're really kind, Hiraga-kun.":
        "Ты действительно добрый, Хирага-кун.",
    "Huh? Why?":
        "А? Почему?",

    # ==== SCENE 1325 ====
    "Hmm, I have no idea.":
        "Хм, не знаю.",
    "No matter how hard I try, I just can't imagine why Louise and the others would do that to Haruna.":
        "Как ни пытаюсь, не могу представить, зачем Луиза и другие так поступили бы с Харуной.",
    "Dense…":
        "Тупица…",
    "Eh?":
        "А?",
    "Never mind.":
        "Ничего.",
    "Tch.":
        "Цк.",

    # ==== SCENE 1326 ====
    "Haruna, can you guess why?":
        "Харуна, а ты можешь догадаться, почему?",
    "Ah, um… I'm sorry. I still don't know…":
        "А, ну… Простите. Всё равно не знаю…",
    "You don't? Yeah, I figured…":
        "Не знаешь? Я так и думал…",
    "Well, I should be heading out. Take it easy, okay?":
        "Ладно, мне пора. Отдыхай, хорошо?",
    "…Hiraga-kun, you idiot.":
        "…Хирага-кун, идиот.",

    # ==== SCENE 1327 ====
    "Louise isn't here… I was hoping she'd be back in her room. I wonder where she went…?{#ch3.5_th_1327}":
        "Луизы здесь нет… Надеялся, она вернулась в свою комнату. Куда же она подевалась…?",
    "My, Saito. Standing about in the hallway—is something the matter?":
        "А, Сайто. Что ты тут делаешь в коридоре с таким серьёзным лицом — что-то случилось?",
    "I was looking for Louise, but she's nowhere to be found…":
        "Я искал Луизу, но нигде не могу её найти…",
    "I see. That's a shame.":
        "Понятно. Жаль.",
    "Ah, that's right, Saito. Do drop by my research lab next time, won't you?":
        "А, точно, Сайто. Заходи-ка в следующий раз в мою лабораторию, хорошо?",
    "Yes, I'd love to.{#ch3_m1327a}":
        "Да, с удовольствием.",
    "Once things calm down, sure.{#ch3_m1327b}":
        "Как всё утихнет — обязательно.",
    "I'll make time to visit.{#ch3_m1327c}":
        "Я найду время и зайду.",
    "Yes, I'd love to.":
        "Да, с удовольствием.",
    "Very well. Come by whenever it suits you, Saito.":
        "Что ж, заходи, когда тебе удобно, Сайто.",
    "Once things calm down, sure.":
        "Как всё утихнет — обязательно.",
    "Once things calm down, you say… Are you busy with something lately?":
        "Как всё утихнет, говоришь… Ты в последнее время чем-то занят?",
    "Yes, a few things here and there… But I'll be sure to come.":
        "Да, тут да там… Но я обязательно зайду.",
    "I see. Then do come once things have settled down.":
        "Понятно. Тогда заходи, когда всё улеглось.",
    "I'll make time to visit.":
        "Я найду время и зайду.",
    "Make time, you say… Is there something keeping you busy?":
        "Найдёшь время, говоришь… Что тебя так занимает?",
    "Ah, well, a little…":
        "Ну, немного…",
    "Hesitating isn't like you, Saito. What exactly is going on?":
        "Ты ведь не из пугливых, Сайто. Что, собственно, происходит?",
    "Actually, Professor…I'm having a falling-out with some people.":
        "По правде говоря, профессор… у меня разлад с некоторыми людьми.",
    "I see. You've had it rough too, then.":
        "Понятно. Выходит, и тебе достаётся.",

    # ==== SCENE 1331 ====
    "Well then, I'll be looking forward to it, Saito.":
        "Ну что ж, я буду рассчитывать на тебя, Сайто.",
    "Yes, Professor.":
        "Да, профессор.",

    # ==== SCENE 1332 ====
    "Louise isn't here… I was hoping she'd be back in her room. I wonder where she went…?{#ch3.5_th_1332}":
        "Луизы здесь нет… Надеялся, она вернулась в свою комнату. Куда же она подевалась…?",
    "You… What are you doing there? Don't tell me you're planning to rob the place?":
        "Ты… Что ты тут делаешь? Неужели собрался грабить?",
    "Me, a burglar? No, no! I'm just looking for Louise.":
        "Я — вор? Да нет-нет! Я просто ищу Луизу.",
    "Oh, is that so? I haven't seen Louise. I wonder if she's really in?":
        "Ах, вот как? Луизу я не видела. Она точно там?",
    "I see. Thanks.":
        "Понятно. Спасибо.",
    "By the way, you… What do you want with Louise?":
        "Кстати, ты… Что тебе нужно от Луизы?",
    "What do I want…":
        "Что мне нужно…",
    "It's not like I need her for anything.{#ch3_m1332a}":
        "Да в общем-то и не нужно.",
    "I wanted to ask her about Haruna.{#ch3_m1332b}":
        "Я хотел спросить её о Харуне.",
    "Sorry. I can't tell you, Monmon.{#ch3_m1332c}":
        "Прости. Не могу тебе сказать, Монмон.",

    # ==== SCENE 1333 ====
    "It's not like I need Louise for anything.":
        "Да в общем-то мне Луиза и не нужна.",
    "I was just wondering where she might be, so I'm looking around.":
        "Я просто думал, где она может быть, и осматриваюсь.",
    "Oh, is that so.":
        "Ах, вот как.",

    # ==== SCENE 1334 ====
    "I wanted to consult her about something regarding Haruna.":
        "Я хотел посоветоваться с ней насчёт Харуны.",
    "Oh, is that so. Not to pry, but…":
        "Ах, вот как. Не то чтобы я хотелось влезать, но…",
    "You have it rough too, don't you? You're living with a maid, Louise, and Haruna now, right?":
        "Тоже непросто, да? Ты теперь живёшь с горничной, Луизой и Харуной, верно?",
    "Haha, hah…":
        "Ха-ха-ха, ха…",
    "If she knew about what just happened, she'd be shocked.":
        "Е бы она знала, что только что случилась, она бы удивилась.",

    # ==== SCENE 1335 ====
    "Sorry. I can't tell you, Monmon.":
        "Прости. Не могу тебе сказать, Монмон.",
    "Who are you calling Monmon?! I'm Montmorency!":
        "Кто тут Монмон?! Я Монморанси!",
    "Come on, what does a little thing like that matter?":
        "Да брось, какие мелочи.",
    "It matters plenty! And state your purpose properly.":
        "Ещё как имеют! И назови толком свою цель.",
    "You're a handful, Monmon.":
        "Ух ты, какой характер, Монмон.",
    "I said stop calling me Monmon! What if the whole academy hears—how will you take responsibility?":
        "Я сказала — не называй меня Монмон! Если это услышит вся академия — как ты за это ответишь?",
    "Responsibility… Ah, never mind.":
        "Ответить… Ах, ладно.",

    # ==== SCENE 1335/1336 ====
    "I was just wondering where Louise might be, so I'm looking around.":
        "Я просто думал, где может быть Луиза, и осматриваюсь.",
    "Oh, is that so? Then say so in the first place.":
        "Ах, вот как? Тогда говори сразу.",
    "Well, I've got to go look for Louise, so I'll be off…":
        "Ладно, мне пора искать Луизу, так что я пойду…",
    "Sorry I couldn't be of help.":
        "Прости, что не смогла помочь.",

    # ==== SCENE 1337 ====
    "Louise isn't here… I was hoping she'd be back in her room. I wonder where she went…?{#ch3.5_th_1337}":
        "Луизы здесь нет… Надеялся, она вернулась в свою комнату. Куда же она подевалась…?",
    "Hello, Saito. What's with that grave expression?":
        "Здравствуй, Сайто. Что за похмурое выражение лица?",
    "Do I really look that grim?":
        "Я правда так мрачно выгляжу?",
    "Mm… What's wrong? If it helps, I can lend an ear.":
        "Мм… Что случилось? Если поможет, могу выслушать.",
    "No, I was just wondering if you'd seen Louise anywhere.":
        "Да нет, просто думал, не видел ли ты Луизу.",
    "Louise? Not while I've been here, no…":
        "Луизу? Не с тех пор, как я здесь, нет…",
    "By the way, is something the matter with Louise?":
        "Кстати, что-нибудь случилось с Луизой?",
    "Actually…":
        "По правде говоря…",
    "I wanted to consult you about Haruna.{#ch3_m1337a}":
        "Я хотел посоветоваться с тобой о Харуне.",
    "No, never mind.{#ch3_m1337b}":
        "Да нет, неважно.",
    "Yeah, I just need her for something.{#ch3_m1337c}":
        "Да, мне просто кое-что от неё нужно.",

    # ==== SCENE 1338 ====
    "It's about Haruna—I wanted some advice…":
        "Это насчёт Харуны — хотел спросить совета…",
    "Advice? What on earth happened?":
        "Совета? Что, собственно, произошло?",
    "N-no, nothing happened. It's not a big deal.":
        "Н-нет, ничего не произошло. Да это ерунда.",
    "Is that so? All right, then.":
        "Ах, вот как? Что ж, хорошо.",
    "Something tells me asking Guiche for advice would only make things more complicated—and that feeling's probably right.{#ch3.5_th_1338}":
        "Что-то подсказывает: совета просить у Гиша — только всё запутать ещё больше. И это, наверное, верно.",

    # ==== SCENE 1339 ====
    "No, never mind.":
        "Да нет, неважно.",
    "You're a cold one, you know that? Don't be like that—tell me too, won't you?":
        "Ты ведь холодный тип, знаешь ли? Не будь таким — расскажи и мне, да?",
    "My bad, my bad. It's nothing all that serious. I'll tell you about it some other time.":
        "Моя вина, моя вина. Да это не так уж серьёзно. Расскажу как-нибудь в другой раз.",
    "Is that so? All right, then.{#ch3.5_g_008}":
        "Ах, вот как? Что ж, хорошо.",
    "Something tells me asking Guiche for advice would only make things more complicated—and that feeling's probably right.{#ch3.5_th_1339}":
        "Что-то подсказывает: совета просить у Гиша — только всё запутать ещё больше. И это, наверное, верно.",

    # ==== SCENE 1340 ====
    "Yeah, I just need her for something.":
        "Да, мне просто кое-что от неё нужно.",
    "I see. Doesn't sound like a crisis that needs my intervention.":
        "Понятно. Не похоже на кризис, требующий моего вмешательства.",
    "Something like that.":
        "Примерно так.",
    "It'd be a hassle, so I won't bother explaining the situation to Guiche.":
        "Слишком уж хлопотно, так что не буду объяснять Гишу ситуацию.",

    # ==== SCENE 1341 ====
    "By the way, Guiche—what are you even doing here?":
        "Кстати, Гиш — ты тут вообще что делаешь?",
    "Me? By visiting the kitchen—a place one rarely gets to see—I've been studying society.":
        "Я? Навещая кухню — место, куда редко попадают, — я изучаю общество.",
    "I… see. Oh, you've got sauce around your mouth.":
        "Я… понимаю. А, у тебя соус вокруг рта.",
    "W-wha—nonsense!? …Wait, there's nothing there!?":
        "Ч-что— ерунда!? …Погоди, там ничего нет!?",
    "Just kidding. Field trips to the kitchen are fine, but go easy on the nibbling.":
        "Шучу. Экскурсии на кухню — это хорошо, только не налягай на угощения.",
    "What are you talking about! I-I never nibble on anything!":
        "О чём ты говоришь! Я-я никогда не налягаю на угощения!",
    "Sure, sure. If you say so.":
        "Конечно, конечно. Раз уж так говоришь.",
    "Well, see you.":
        "Ну, пока.",
}


def canon_items():
    """[(kind, spk, ja)] из канона в порядке источника (часть 5)."""
    smap = pcs.load_sprite_map()
    flow = pcs.canon_flow(smap)
    out = []
    for kind, spk, _state, payload in flow:
        if kind == "menu":
            line = payload  # 【選択肢】text → scene N  /  【移動】text → scene N ...
            m = re.match(r"【[^】]+】(.*?)\s*→\s*scene", line)
            ja = m.group(1).strip() if m else line
            out.append(("menu", None, ja))
        else:
            out.append(("item", spk, "".join(payload["parts"])))
    return out


def script_items():
    """[(kind, old)] из script-ch3_5.rpy в порядке следования."""
    lines = io.open(SCRIPT, encoding="utf-8").read().splitlines()
    out = []
    for ln in lines:
        m = re.match(r'\s*(s|l|si|ha|k|t|c|m|g|th) "(.*)"$', ln)
        if m:
            out.append(("th" if m.group(1) == "th" else "item", m.group(2)))
            continue
        m = re.match(r'\s*"(.*)":$', ln)
        if m:
            out.append(("menu", m.group(1)))
    return out


def main():
    cj = canon_items()
    sg = script_items()
    if len(cj) != len(sg):
        print("COUNT mismatch: canon=%d script=%d" % (len(cj), len(sg)))
        return 1
    rows = []
    for i, ((ck, _cspk, ja), (sk, old)) in enumerate(zip(cj, sg)):
        if (ck == "menu") != (sk == "menu"):
            print("KIND mismatch at #%d: canon=%s script=%s" % (i, ck, sk))
            return 1
        bucket = "choises" if sk == "menu" else ("thoughs" if sk == "th" else "dialogs")
        rows.append((bucket, old, ja))

    # RU-покрытие
    missing = [old for _, old, _ in rows if old not in RU]
    extra = [k for k in RU if k not in {old for _, old, _ in rows}]
    if missing:
        print("RU missing: %d" % len(missing))
        for m in missing[:20]:
            print("  " + m[:70])
        return 1
    if extra:
        print("RU extra keys: %d" % len(extra))
        for m in extra[:20]:
            print("  " + m[:70])
        return 1

    # уникальность old
    seen = {}
    for _, old, _ in rows:
        seen[old] = seen.get(old, 0) + 1
    dups = [k for k, v in seen.items() if v > 1]
    if dups:
        print("DUPLICATE old: %d" % len(dups))
        for d in dups[:20]:
            print("  " + d[:70])
        return 1

    bucket_files = {"dialogs": "dialogs.rpy", "thoughs": "thoughs.rpy",
                    "choises": "choises.rpy"}
    by_bucket = {"dialogs": [], "thoughs": [], "choises": []}
    for bucket, old, ja in rows:
        by_bucket[bucket].append((old, ja, RU[old]))

    total = 0
    for bucket, pairs in by_bucket.items():
        fname = bucket_files[bucket]
        block_ja = "".join('\n    old "%s"\n    new "%s"\n' % (o, j)
                           for o, j, r in pairs)
        block_ru = "".join('\n    old "%s"\n    new "%s"\n' % (o, r)
                           for o, j, r in pairs)
        for lang, block in (("japanese", block_ja), ("russian", block_ru)):
            path = "game/tl/%s/%s" % (lang, fname)
            text = io.open(path, encoding="utf-8").read()
            if text and not text.endswith("\n"):
                text += "\n"
            text += block
            io.open(path, "w", encoding="utf-8").write(text)
        total += len(pairs)
        print("  %s: %d pairs" % (bucket, len(pairs)))

    print("P5 TL pairs written:", total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
