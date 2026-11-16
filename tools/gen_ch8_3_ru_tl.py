#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генерация русского перевода для ch8_3 на основе EN-скрипта и JA-оригинала.
Перевод делается с учёта контекста, стиля ch8_1/ch8_2 и словаря терминов.
"""

# Словарь EN -> RU для ch8_3 (148 диалогов + 7 мыслей)
# Переводы адаптированы под стиль проекта, обращения по addresses.md
TRANSLATIONS = [
    # ch8_s_082
    ("Alright, this is youth!", "Ну вот, так это и есть — юность!"),
    # ch8_si_010
    ("That's Saito, that's Saito…!", "Это Сайто, это Сайто…!"),
    # ch8_l_051
    ("It's fine. I'll fix it.", "Ничего страшного. Я это исправлю."),
    # ch8_s_083
    ("Eh, ah, oh, o-oh… It's just a joke…", "Э, а, о, о-о… Это же просто шутка…"),
    # ch8_s_084
    ("Ugh, ugh, grumble…?", "Трясётся, трясётся…?"),
    # ch8_l_052
    ("I managed to fix it somehow.", "Как-то получилось починить."),
    # ch8_l_053
    ("Your Highness!", "Ваше Высочество!"),
    # ch8_h_059
    ("Yes!", "Да!"),
    # ch8_l_054
    ("I disagree. But if you've decided, then I'll follow.", "Я не согласна. Но если Вы так решили, то последую за Вами."),
    # ch8_h_060
    ("Thank you, Louise.", "Спасибо, Луиза."),
    # ch8_s_085
    ("So you're going to join up with the army?", "Значит, вы собираетесь присоединиться к армии?"),
    # ch8_h_061
    ("No. I'm returning to the palace.", "Нет. Я возвращаюсь в дворец."),
    # ch8_h_062
    ("So I'd like to accompany you on the way there, if you don't mind.", "Поэтому я бы хотела сопроводить вас по дороге, если не против."),
    # ch8_s_086
    ("But the palace is under attack right now. You don't have to force your way back…", "Но дворец сейчас под атакой. Вам не нужно насильно пробиваться обратно…"),
    # ch8_h_063
    ("It's enough that I'm safe inside the palace, so the Tristain can be reassured that I'm alive.", "Достаточно того, что я в безопасности внутри дворца, чтобы Тристейн узнал: я жива."),
    # ch8_h_064
    ("Besides, I have something on my mind.", "К тому же, у меня есть одна мысль."),
    # ch8_h_065
    ("I, as a queen, have different things I can do as a mage.", "Я, как королева, могу сделать что-то иное, как волшебница."),
    # ch8_s_087
    ("And what is that?", "А что именно?"),
    # ch8_h_066
    ("That's something I'll tell you about when the time comes. For now, just think of it as a backup plan.", "Об этом я расскажу, когда придет время. Пока считайте это запасным планом."),
    # ch8_l_055
    ("Understood. I'll do my best to protect the Princess.", "Поняла. Я сделаю всё возможное, чтобы защитить Принцессу."),
    # ch8_h_067
    ("Thank you, Louise.", "Спасибо, Луиза."),
    # ch8_g_003
    ("Hey? Something seems to be happening outside. What's going on?", "О? Кажется, снаружи что-то происходит. Что случилось?"),
    # ch8_k_011
    ("No way!?", "Неужели!?"),
    # ch8_e_001
    ("I found them.", "Нашёл их."),
    # ch8_si_011
    ("Kyaaa!", "Кяаа!"),
    # ch8_k_012
    ("They're the Reconquista assassins, aren't they.", "Это убийцы Реконкисты, верно?"),
    # ch8_s_088
    ("Damn it! So this is where it comes down to?", "Чёрт! Так вот где всё решается?"),
    # ch8_l_056
    ("Siesta! Get back! It's dangerous!", "сьеста! Отойди! Опасно!"),
    # ch8_si_012
    ("Yes!", "Ха-ай!"),
    # ch8_k_013
    ("First, let's turn and fight back!", "Сначала дадим им сдачи!"),
    # ch8_t_003
    ("All detained. Can't let you retreat.", "Все задержаны. Отступать не позволю."),
    # ch8_s_089
    ("Alright, let's do this!", "Ладно, давайте сделаем это!"),
    # ch8_s_090
    ("Everyone, are you all right!?", "Все, вы в порядке!?"),
    # ch8_l_057
    ("The Princess and Siesta, everyone is safe.", "Принцесса и Сьеста, все в безопасности."),
    # ch8_k_014
    ("We drove them all off.", "Всех их отогнали."),
    # ch8_l_058
    ("This is getting out of hand. We have to hurry!", "Дело принимает плохой оборот. Нам нужно поторопиться!"),
    # ch8_s_091
    ("Siesta, wait here. The academy is safer, but there's no time.", "Сьеста, подожди здесь. Академия безопаснее, но времени нет."),
    # ch8_si_013
    ("Yes! Please give me your support, Saito-san…!", "Ха-ай! Пожалуйста, поддержите меня, Сайто-сан…!"),
    # ch8_s_092
    ("Yeah…", "Аа…"),
    # ch8_l_059
    ("Then let's split up. I'll go with Site and Kirche to the palace.", "Тогда разделимся. Я пойду с Сайто и Кюрке к дворцу."),
    # ch8_k_015
    ("Tabitha, Montmorency, and Guiche — attack the cannons. Be careful.", "Табаса, Монморанси, Гюш — атакуйте пушки. Осторожнее."),
    # ch8_t_004
    ("Understood.", "Понял."),
    # ch8_h_068
    ("Understood. I'll make sure I'm not an obstacle. Do your best.", "Поняла. Стараюсь не мешать. Удачи."),
    # ch8_l_061
    ("Then, the plan begins.", "Тогда план начинается."),
    # ch8_a_001
    ("Your Majesty! Are you safe!?", "Ваше Величество! Вы в безопасности!?"),
    # ch8_a_002
    ("Your Majesty has returned! Now, we have won!", "Ваше Величество вернулись! Теперь мы победили!"),
    # ch8_s_093
    ("Wow. Just seeing the Princess is changing the mood of the city.", "Вау. Только вид Принцессы меняет настроение в городе."),
    # ch8_d_001
    ("Being a king means little to me. Having this person around means I can believe in them.", "Быть королём — ерунда. Главное — чтобы рядом был кто-то, в кого можно верить."),
    # ch8_o_001
    ("Yes, sir. Small-scale combat has been occurring at the eastern cannon since morning.", "Гав. С утра у восточной батареи идут мелкие сражения."),
    # ch8_o_002
    ("That would explain why the castle bombardment has stopped, for now.", "Поэтому, вероятно, обстрел замка пока прекратился."),
    # ch8_k_016
    ("Tabitha and the others are doing their best, aren't they.", "Табаса и остальные стараются, да?"),
    # ch8_o_003
    ("However, the Reconquista fleet is… approaching.", "Однако флот Реконкисты… приближается."),
    # ch8_h_070
    ("I understand. That's why I've prepared the backup plan.", "Понимаю. Именно поэтому я приготовила запасной план."),
    # ch8_o_004
    ("The backup plan…?", "Запасной план…?"),
    # ch8_h_071
    ("I'll explain the details after this battle is over.", "Подробности объясню после окончания битвы."),
    # ch8_h_072
    ("I'll relay this to all units deployed in the city. Keep surrounding them and wait. If chaos occurs in the enemy camp, then launch an all-out assault.", "Передам это всем подразделениям в городе. Продолжайте окружение и ждите. Если во вражеском лагере начнётся хаос — наносите решающий удар."),
    # ch8_o_005
    ("Understood!", "Понял!"),
    # ch8_s_095
    ("Alright, let's head to the roof! From there, you can use your magic to take them all down!", "Хорошо, на крышу! Оттуда ты сможешь魔法で一気に片付けられるぞ!"),
    # ch8_l_062
    ("Yes, please rely on me. I'll show you my true power!", "Да, рассчитывайте на меня. Покажу свою истинную силу!"),
    # ch8_l_063
    ("Hey! Believe in your master more!", "Эй! Верьте в своего хозяина сильнее!"),
    # ch8_s_096
    ("Here we come!", "Прибыли!"),
    # ch8_l_064
    ("Whew, whew, whew… It's a high place. Climbing all those stairs was tiring.", "Ха-а, ха-а, ха-а… Высота. Подъём по лестнице утомил."),
    # ch8_s_097
    ("But look at this! From here, we can see all the cannons!", "Но смотри! Отсюда видно все орудия!"),
    # ch8_l_065
    ("All right, watch this! I'll smack the Reconquista forces with the righteous hammer of justice!", "Хорошо, смотрите! Свергну я на Реконкисту молот правосудия!"),
    # ch8_w_001
    ("You won't get away with this.", "Так не выйдет."),
    # ch8_s_098
    ("What!?", "Что!?"),
    # ch8_w_002
    ("Surprised? You really came this far, didn't you. I underestimated you.", "Удивлён? Ты действительно добрался до сюда. Я недооценил тебя."),
    # ch8_ak_001
    ("I'm not in the mood for fighting anymore. Just stay here.", "Уже не в духе драться. Просто оставайся здесь."),
    # ch8_s_099
    ("Weatherby, and Akina too!", "Везерли, и Акина тоже!"),
    # ch8_d_002
    ("Maybe you thought we'd come here. You were wrong.", "Думали, мы придём сюда? Ошиблись."),
    # ch8_w_003
    ("It's thanks to the information gathered by Haruna. Though she collected it unconsciously.", "Благодаря информации, собранной Харуной. Хоть она и делала это бессознательно."),
    # ch8_s_100
    ("What!?", "Что!?"),
    # ch8_w_004
    ("Do you even understand why Haruna was being targeted regularly?", "Ты вообще понимаешь, почему Харуну регулярно атаковывали?"),
    # ch8_w_005
    ("That's when Akina was passing information about you and Louise to me.", "В то время Акина передавала мне сведения о тебе и Луизе."),
    # ch8_w_006
    ("Though Akina herself doesn't remember doing any of it.", "Хоть сама Акина и не помнит, что это сделала."),
    # ch8_s_101
    ("Damn you, Weatherby! Restore Haruna!", "Чёрт тебя, Везерли! Верни Харуну!"),
    # ch8_w_007
    ("Unfortunately, that's not something I can agree to. I have my own goals. Until I achieve them, I will use you.", "К сожалению, я не могу согласиться. У меня свои цели. Пока не достигну их — буду пользоваться вами."),
    # ch8_s_102
    ("Haruna…", "Харуна…"),
    # ch8_w_008
    ("You intended to attack the cannons from the palace rooftop with a long-range spell. But since we're already occupying it, it's meaningless.", "Ты планировал атаковать орудия с крыши дворца дальним заклинанием. Но раз мы уже заняли позицию — это бессмысленно."),
    # ch8_w_009
    ("I'll just finish this here on the rooftop. It's fortunate that the Princess is here.", "Просто закончу это здесь, на крыше. К счастью, Принцесса тоже здесь."),
    # ch8_l_066
    ("Fine then. If you won't stop, then we'll defeat you.", "Хорошо. Если не остановитесь — победим вас мы."),
    # ch8_ak_002
    ("Oh, can you? Can I use my bomb on your magic? Do it if you can win.", "О, сможете? А если я применить свою бомбу против вашей магии? Попробуйте, если сможете выиграть."),
    # ch8_h_073
    ("That's enough.", "Достаточно."),
    # ch8_ak_003
    ("Ah…!", "А…!"),
    # ch8_w_010
    ("What!?", "Что!?"),
    # ch8_s_103
    ("Haruna!?", "Харуна!?"),
    # ch8_h_074
    ("Secure that child! Quickly!", "Захватите этого ребёнка! Быстро!"),
    # ch8_s_104
    ("Huh? Ah, yes!", "Э? А, да!"),
    # ch8_w_011
    ("…!", "…!"),
    # ch8_s_105
    ("Haruna! Or is it Akina? Anyway, is everyone safe?", "Харуна! Или это уже Акина? Во всяком случае, все в порядке?"),
    # ch8_ha_001
    ("Un… unnn…", "Ун… унн…"),
    # ch8_k_017
    ("Looks like we're all safe, then.", "Кажется, все в безопасности."),
    # ch8_h_076
    ("As long as I am here, it's absolutely impossible.", "Пока я здесь — это абсолютно невозможно."),
    # ch8_w_012
    ("Why… how are you able to dispel it?", "Почему… как ты смог это рассеять?"),
    # ch8_w_013
    ("This is a secret art passed down in my family! It shouldn't be breakable by someone like you!", "Это секретная техника моей семьи! Её не должен был преодолеть кто-то вроде тебя!"),
    # ch8_h_077
    ("That it can be broken, I knew. I knew you were communicating through a sound that humans cannot hear.", "То, что её можно взломать, я знала. Знала, что вы общаетесь звуком, недоступным человеческому уху."),
    # ch8_h_078
    ("I was just making you unable to hear that sound by using magic.", "Я просто магией сделала так, что вы его не слышите."),
    # ch8_w_014
    ("No, that's a lie…! This magic is a special art that only my family can use!", "Нет, это ложь…! Эта магия — исключительное мастерство только моей семьи!"),
    # ch8_w_015
    ("How could you possibly know how to counter it?!", "Откуда вы могли знать, как её противостоять?!"),
    # ch8_w_016
    ("Why… how did you know?! Did you raid your own village…?", "Почему… как ты узнал?! Неужели ты нагрянул на свою деревню…?"),
    # ch8_h_079
    ("Miss Weatherby, your loss of nobility was not because of your origins.", "Мисс Везерли, вас лишили дворянства не из-за вашего происхождения."),
    # ch8_w_017
    ("What…?", "Что…?"),
    # ch8_h_080
    ("You used a forbidden magic that manipulates the heart, which was deemed inhuman.", "Вы использовали запрещённую магию, манипулирующую сердцем, которая считалась нечеловечной."),
    # ch8_h_081
    ("You were persecuted in your noble years because of your origins. I understand and sympathize.", "В ваши дворянские годы вас преследовали из-за происхождения. Я понимаю и сочувствую."),
    # ch8_h_082
    ("But you broke the taboo and attempted to toy with the hearts of others.", "Но вы нарушили табу и попытались играть с чужими сердцами."),
    # ch8_h_083
    ("That is a crime for which there is no excuse, and so you have lost your noble status.", "Это преступление, за которое нет оправдания. Поэтому вы потеряли дворянское звание."),
    # ch8_w_018
    ("How… I can't believe the secret art of my family would be turned against me…", "Как… Не могу поверить, что семейная тайна обратилась против меня…"),
    # ch8_h_084
    ("The existence of the forbidden heart-manipulating magic is a threat. That's why research was conducted by some of the royal family and military.", "Существование запрещённой магии управления сердцем — угроза. Поэтому и члены королевской семьи, и военные вели исследования, как её взломать."),
    # ch8_h_085
    ("What I learned to protect my people was that. Your magic no longer works.", "То, чему я научилась ради защиты народа — это и есть. Твоя магия больше не работает."),
    # ch8_w_019
    ("Heh heh heh… Now that my family's secret is sealed, the only option is to overpower with force.", "Хе-хе-хе… Раз семейный секрет запечатан, остаётся только сила."),
    # ch8_w_020
    ("Then at least let me face you head-on and take down the queen!", "Тогда пусть хоть в открытую схватку убью королеву!"),
    # ch8_w_021
    ("Come then! I have nothing left but my pride and my anger! Take this!!", "Иди же! Остались только гордость и гнев! Прими это!!"),
    # ch8_s_106
    ("I guess we really have to fight then.", "Видимо, действительно придётся драться."),
    # ch8_s_107
    ("No more games, Derflinger! This is it!", "Больше никаких игр, Дерфлингер! Это конец!"),
    # ch8_d_003
    ("All right, partner!", "Хорошо, партнёр!"),
    # ch8_w_022
    ("Kuahh!", "Куаа!"),
    # ch8_s_108
    ("That's enough, Weatherby. You're defeated.", "Всё, Везерли. Ты проиграл."),
    # ch8_w_023
    ("Heh heh heh…", "Хе-хе-хе…"),
    # ch8_w_024
    ("Did you really think I'd be defeated by a queen I underestimated?", "Неужели ты думал, что проиграешь подручной, которой пренебрегал?"),
    # ch8_s_116
    ("Weatherby…", "Везерли…"),
    # ch8_w_025
    ("Then at this point, no mercy for the defeated! This is the finishing blow!", "Тогда на этом этапе — не жалеть побеждённых! Это решающий удар!"),
    # ch8_s_117
    ("What should the Princess do?", "Что должна сделать Принцесса?"),
    # ch8_h_086
    ("Miss Weatherby. You will pay for your sins.", "Мисс Везерли. Вы ответите за свои грехи."),
    # ch8_w_026
    ("I know. Do what you will.", "Знаю. Делай что хочешь."),
    # ch8_h_087
    ("Understood. I'll inform you of the punishment later.", "Поняла. Наказание сообщу позже."),
    # ch8_h_088
    ("Next is your turn, Louise. Show me your power.", "Следующая — ты, Луиза. Покажи свою силу."),
    # ch8_l_067
    ("Yes. I entrust this to you.", "Да. Доверяю это тебе."),
    # ch8_l_068
    ("Come forth, here I am… Here I am.", "Явься, вот я… Вот я."),
    # ch8_l_069
    ("Illusion!!", "Иллюзия!!"),
    # ch8_h_089
    ("Oh…!", "О…!"),
    # ch8_s_109
    ("Eh…!?", "Э…!?"),
    # ch8_s_110
    ("Was that… the Tristain aerial fleet!?", "Это… тристейнский воздушный флот!?"),
    # ch8_l_070
    ("No, it's not… Idiot.", "Нет, не это… Идиот."),
    # ch8_h_090
    ("Oh, Louise… This is Illusion. It's magic that creates tangible illusions…", "О, Луиза… Это Иллюзия. Магия, создающая осязаемые иллюзии…"),
    # ch8_s_111
    ("So that fleet was an illusion?", "Значит, тот флот был иллюзией?"),
    # ch8_l_071
    ("So it was… Then? / So, what about my magic?", "Так это так… И что? / А как же моя магия?"),
    # ch8_s_112
    ("Yeah, that's more than enough! The Reconquista fleet has started retreating, and the ground cannons are getting noisy.", "Ага, этого более чем достаточно! Флот Реконкисты начал отступление, а наземные батареи зашумели."),
    # ch8_h_091
    ("The troops who saw the enemy's confusion have launched their assault. With this, the battle is decided.", "Подразделения, заметившие замешательство врага, перешли в наступление. С этим битва решена."),
    # ch8_l_072
    ("Yes… That's good…", "Да… Хорошо…"),
    # ch8_s_113
    ("Whoa. What's wrong with Louise? She just collapsed?", "Ух. Чего с Луизой? Она просто рухнула?"),
    # ch8_s_114
    ("Louise, you're exhausted. Rest now; the rest is on us.", "Луиза, ты измотана. Отдохни, за остальное ответим мы."),
    # ch8_l_073
    ("…Yeah. I'm a bit tired…", "…Ага. Чуть-чуть устала…"),
    # ch8_h_092
    ("Louise… and my familiars, thank you. Thanks to you, this country was saved.", "Луиза… и мои фамильяры, спасибо. Благодаря вам эта страна спасена."),
    # ch8_h_093
    ("And I… also… will do my best.", "И я… тоже… сделаю всё возможное."),
    # ch8_s_115
    ("What?", "Что?"),
    # ch8_h_094
    ("Oh, no. Well, it seems we'll have a lot of work ahead of us now.", "О, нет. Ну, похоже, впереди у нас горы работы."),
    # ch8_h_095
    ("Casualty care, rebuilding damaged buildings… There are so many things to do, more than I can think of now.", "Уход за ранеными, восстановление зданий… Столько дел, что даже не придумаешь всё сразу."),
    # ch8_h_096
    ("But… I will not run away. I am… the queen of this country.", "Но… Я не сбегу. Я… королева этой страны."),
]

# Thoughts translations (7 entries)
THOUGHTS_TRANSLATIONS = [
    ("（ど、どうしよう。\n　女の子が泣いちゃったら、\n　一体どうすればいいんだ？）",
     "(Ч-что делать.\n  Если девочка заплакала,\n  что мне вообще делать?)"),
    ("（お姫さま、どうしたんだ？\n　あんなに顔を真っ赤にして……）",
     "(Принцесса, что с ней?\n  Лицо такое красное…)"),
    ("（今、詰め寄られたかと思ったら、\n　暖かくて柔らかい感触が……。\n　お姫さまの唇が……っ！？）",
     "(Думала, сейчас прижмёт к стене,\n  а вдруг — тёплое и мягкое касание…\n  Губы Принцессы…!?)"),
    ("（虚無のことは誰にも言えないからな……）",
     "(О Пустоте никому не скажешь…)"),
    ("（ウェザリーは、まだ虚無の力について\n　あまりよく分かっていないみたいだ。\n　まだ、隙はある……）",
     "(Везерли, кажется, до сих пор\n  не до конца понимает силу Пустоты.\n  Ещё есть шанс…)"),
    ("（村？\n　ウェザリーの生まれた村が、\n　この技を伝えていたのか？）",
     "(Деревня?\n  В родной деревне Везерли\n  передавали эту технику?)"),
    ("（そっか、虚無の魔法は、\n　精神力をめちゃくちゃ消費するんだっけ……）",
     "(Такс, магия Пустоты,\n  жестоко расходует ментальные силы…)"),
]


def write_russian_tl():
    # Write dialogs
    with open('game/tl/russian/ch8_3_dialogs.rpy', 'w', encoding='utf-8') as f:
        f.write(f'# ===== ch8.3: {len(TRANSLATIONS)} strings (dialogues) =====\n')
        f.write('translate russian strings:\n\n')
        for en_text, ru_text in TRANSLATIONS:
            f.write(f'    old "{en_text}"\n')
            f.write(f'    new "{ru_text}"\n\n')
    print(f"Written {len(TRANSLATIONS)} dialogue entries to ch8_3_dialogs.rpy")

    # Write thoughts
    with open('game/tl/russian/ch8_3_thoughs.rpy', 'w', encoding='utf-8') as f:
        f.write(f'# ===== ch8.3: {len(THOUGHTS_TRANSLATIONS)} strings (thoughts) =====\n')
        f.write('translate russian strings:\n\n')
        for ja_text, ru_text in THOUGHTS_TRANSLATIONS:
            # Use JA as old key since thoughts don't have voice markers
            f.write(f'    old "{ja_text}"\n')
            f.write(f'    new "{ru_text}"\n\n')
    print(f"Written {len(THOUGHTS_TRANSLATIONS)} thought entries to ch8_3_thoughs.rpy")


if __name__ == '__main__':
    write_russian_tl()