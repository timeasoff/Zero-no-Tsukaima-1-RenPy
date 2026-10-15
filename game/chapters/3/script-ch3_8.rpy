# Глава 3, часть 8 (сцены 207–213 + дата Луизы 1059–1062): итоги дуэли,
# раскаяние Харуны и утреннее меню свиданий. Вход — jump ch3_8 из меню
# сцены 206 (часть 7). Меню сцены 207 ведёт в ветки 208/209/210, все сходятся
# в хаб 211 (прощение Харуны), далее 212 (кабинет Луизы) и 213 — утро и
# меню свиданий (5 девушек): линия Луизы (1059 с меню 1060/1061/1062) — в
# этой части, линии остальных (1064/1069/1074/1079) — в части 9.
# После возврата из даты — jump ch4 (сцена 219 «дата с кем угодно» = глава 4;
# помимо неё в меню сцены 213 PS2 был 6-й пункт 【デート進行】→ сцена 219 —
# по эталону ch1/ch2 в portrait_choice входят только 5 девушек).
# Заглушки переходных сцен 214–218 не портируются.
# Источник: ps2_source/chapters/chapter_04_女の戦い.txt (SCENE 207–213, 1059–1062).
# Точные аргументы: ps2_source/events_full/chapter_04_女の戦い.txt (те же сцены).
# Голоса: ch3.8_s_001…047, ch3.8_l_001…036, ch3.8_ha_001…010, ch3.8_k_001…004,
#         ch3.8_si_001…004, ch3.8_t_001…002 (103).
# Без голоса (только текст): мысли сайта ×3 в сцене 213 (теги ch3.8_thNN) +
# null-многоточие 1059 (тег ch3.8_null_1059).
# COFFEE в датах 1060/1061/1062 → pause(1.0) (сигнатура не реализована).
# SE (se0 play=+69 в сцене 213 и se1 stop=1 на границах сцен) не портируется.
# Сцена 207: [EVENT_CG +272] — CG без имени, заглушка id(272).

label ch3_8:
    # ==== SCENE 207 ==== (RESET: [BGM +25]/[BG +26] = текущее состояние)
    # [BG +26 (yard)][TRANS][BGM play=+25] → t24; [lay1 +308][lay6 +682]
    $ fade_fx("yard", new_music="t24", sprites=("l 1 sad", "k 1 sad"))

    voice "ch3.8_k_001"
    k "Hah, hah, hah… My, my — you've gotten pretty good, haven't you?"

    voice "ch3.8_l_001"
    l "Hah, hah, hah… You too, Kirche…"

    # [lay1 hide][lay6 hide][lay5 +390]
    $ show_sprites(("s 1",))

    voice "ch3.8_s_001"
    s "Well, y'know… I'm just glad the duel ended without anyone getting seriously hurt."

    # [lay5 hide][lay7 +955]
    $ show_sprites(("ha 1 angry",))

    voice "ch3.8_ha_001"
    ha "Louise!"

    # [lay7 x=224 — сдвиг не копируется][lay1 +306]
    $ show_sprites(("l 1 angry", "ha 1 angry"))

    voice "ch3.8_l_002"
    l "Haruna! What are you doing here?"

    # [lay7 hide][lay5 +429]
    $ show_sprites(("s 3 sad", "l 1 angry"))

    voice "ch3.8_s_002"
    s "She's been here the whole time, apparently."

    # [BGM stop=1000][lay1 hide][lay5 hide][BG hide][EVENT_CG +272][TRANS]
    # [BGM play=+17] → t16 (fade покрывает удаление спрайтов и фона; во время
    # CG спрайты не показываются — реплики 2228–2232/6007–6008/3231–3232/14720
    # звучат поверх CG; CG без имени → заглушка id(272))
    stop music fadeout 1.0
    $ fade_fx("id(272)", type="cg", new_music="t16")

    voice "ch3.8_ha_002"
    ha "Because I played sick, it all blew up into this huge mess! I'm so sorry, everyone!"

    voice "ch3.8_ha_003"
    ha "I faked being sick… just because I wanted Hiraga-kun's attention…"

    voice "ch3.8_ha_004"
    ha "I really am… I really am the worst — I just keep doing awful, selfish things…"

    voice "ch3.8_ha_005"
    ha "Guh… sniff… guh…"

    voice "ch3.8_l_003"
    l "W-well! Even if you fake-cry, I'm not falling for it!"

    voice "ch3.8_s_003"
    s "Hey now, 'fake crying' is a bit much… That's going too far, Louise."

    voice "ch3.8_l_004"
    l "Besides, Saito — you fall for anything way too easily!"

    voice "ch3.8_k_002"
    k "Maybe so. Looks like you were the only one, Darling, who didn't notice she was faking."

    # [lay6 hide] — не показан (защитный сброс PS2)
    voice "ch3.8_k_003"
    k "I adore that about you, Darling… but being too sweet to girls is, in its own way, a crime, you know?"

    voice "ch3.8_si_001"
    si "That's true. Saito-san is too kind…"

    voice "ch3.8_ha_006"
    ha "Guh, sniff… guh…"

    # [lay1/lay7/lay2/lay5/lay6 hide][BG hide][EVENT_CG hide][BG +26 (yard)][TRANS]
    $ fade_fx("yard")

    # [lay7 +990][lay5 +396]
    $ show_sprites(("s 1 sad", "ha 4 sad"))

    voice "ch3.8_s_004"
    s "Y'know, that's me all right. When I see a girl crying…"

    menu:

        "…I just want to protect her.{#ch3_m207a}":
            jump ch3_8_208

        "…I want to believe her unconditionally.{#ch3_m207b}":
            jump ch3_8_209

        "…it kind of sends a chill down my spine.{#ch3_m207c}":
            jump ch3_8_210

label ch3_8_208:
    # ==== SCENE 208 ==== (RESET: [lay7 +990][lay5 +396][BGM +17][BG +26]
    # = текущее состояние)
    # [lay5 +390]
    $ show_sprites(("s 1", "ha 4 sad"))

    voice "ch3.8_s_005"
    s "…I just want to protect her."

    # [lay7 hide][lay1 +308]
    $ show_sprites(("s 1", "l 1 sad"))

    voice "ch3.8_l_005"
    l "That's exactly what being fooled looks like! If you rush to defend every girl's tears, you'll wear yourself out!"

    # [lay5 +429]
    $ show_sprites(("s 3 sad", "l 1 sad"))

    voice "ch3.8_s_006"
    s "Well, yeah, I guess. …Just instinct, y'know."

    jump ch3_8_211

label ch3_8_209:
    # ==== SCENE 209 ==== (RESET: [lay5 +396][lay7 +990][BGM +17][BG +26]
    # = текущее состояние)
    # [lay5 +390]
    $ show_sprites(("s 1", "ha 4 sad"))

    voice "ch3.8_s_007"
    s "…I want to believe her unconditionally."

    # [lay7 hide][lay1 +308]
    $ show_sprites(("s 1", "l 1 sad"))

    voice "ch3.8_l_006"
    l "With that, you'll just get fooled again. Absolutely."

    # [好感度] ルイズ -10 (TNDL tndl(-30) не портируется)
    $ update_sympathy(-10, char_key="louise")

    # [lay5 +429]
    $ show_sprites(("s 3 sad", "l 1 sad"))

    voice "ch3.8_s_008"
    s "Nah, I think I can at least tell the obvious fake tears."

    voice "ch3.8_l_007"
    l "In your dreams."

    jump ch3_8_211

label ch3_8_210:
    # ==== SCENE 210 ==== (RESET: [lay5 +396][lay7 +990][BGM +17][BG +26]
    # = текущее состояние)
    # [lay5 +423]
    $ show_sprites(("s 3", "ha 4 sad"))

    voice "ch3.8_s_009"
    s "…It kind of sends a chill down my spine."

    # [lay7 hide][lay1 +308]
    $ show_sprites(("s 3", "l 1 sad"))

    voice "ch3.8_l_008"
    l "Um… are you saying that in all seriousness?"

    # [好感度] ルイズ -10 (TNDL tndl(-30) не портируется)
    $ update_sympathy(-10, char_key="louise")

    # [lay5 +427]
    $ show_sprites(("s 3 angry", "l 1 sad"))

    voice "ch3.8_s_010"
    s "Kidding! A total joke!! Don't go taking it seriously!"

    # [lay1 hide][lay0 +627]
    $ show_sprites(("s 3 angry", "t 4 sad"))

    voice "ch3.8_t_001"
    t "…Pervert."

    # [好感度] タバサ -15 (TNDL только для ルイズ: tndl(-30) не портируется; ルイズ -10 применён выше)
    $ update_sympathy(-15, char_key="tabitha")

    # [lay0 hide][lay1 +302]
    $ show_sprites(("s 3 angry", "l 1"))

    jump ch3_8_211

label ch3_8_211:
    # ==== SCENE 211 ==== (RESET: [lay1 +308][lay5 +429][BGM +17][BG +26]
    # = нормализация состояния прихода из веток → [lay1 +302])
    $ show_sprites(("s 3 sad", "l 1"))

    voice "ch3.8_l_009"
    l "It's because you're like that, Saito — I didn't catch on that Haruna was faking the whole time!"

    # [lay1 +306]
    $ show_sprites(("s 3 sad", "l 1 angry"))

    voice "ch3.8_l_010"
    l "Haruna tried to fool all of us — just so she could keep you all to herself!"

    voice "ch3.8_l_011"
    l "Why can't you understand something that obvious?!"

    # [lay1 x=-96 — сдвиг не копируется][lay5 +390]
    $ show_sprites(("s 1", "l 1 angry"))

    voice "ch3.8_s_011"
    s "I get that you're mad, Louise. But hear me out, okay?"

    # [lay1 +308]
    $ show_sprites(("s 1", "l 1 sad"))

    voice "ch3.8_l_012"
    l "W-what… Making that serious face all of a sudden!"

    voice "ch3.8_s_012"
    s "I came to this strange world from my own, too — so I know exactly how Haruna feels."

    voice "ch3.8_s_013"
    s "When I was summoned to this world, I was plenty scared myself."

    voice "ch3.8_s_014"
    s "Surrounded by scenery I'd never seen, with nobody anywhere who knew me."

    # [lay5 +429]
    $ show_sprites(("s 3 sad", "l 1 sad"))

    voice "ch3.8_s_015"
    s "You can all imagine just how scary that is, right?"

    voice "ch3.8_s_016"
    s "In that situation, if there's someone you know — it's only natural you'd want to lean on them, don't you think?"

    # [lay5 +396]
    $ show_sprites(("s 1 sad", "l 1 sad"))

    voice "ch3.8_s_017"
    s "Sure, I know what Haruna did wasn't something to praise."

    # [lay5 +390]
    $ show_sprites(("s 1", "l 1 sad"))

    voice "ch3.8_s_018"
    s "That's why she's apologizing. She's asking if you can find it in you to forgive her."

    voice "ch3.8_s_019"
    s "But I'm really grateful to you, Louise."

    # [lay1 +310]
    $ show_sprites(("s 1", "l 1 shy"))

    voice "ch3.8_l_013"
    l "R-really…?"

    # [lay5 +396]
    $ show_sprites(("s 1 sad", "l 1 shy"))

    voice "ch3.8_s_020"
    s "I mean, at first you maybe didn't treat me like a human… but still…"

    # [lay5 +390]
    $ show_sprites(("s 1", "l 1 shy"))

    voice "ch3.8_s_021"
    s "Because you acknowledged that I'm allowed to be here — that's why I have this life now. So… that's why…"

    # [lay1 +343]
    $ show_sprites(("s 1", "l 3 shy"))

    voice "ch3.8_l_014"
    l "F-fine! I get it already! I just have to forgive Haruna, right?"

    # [lay1 +302]
    $ show_sprites(("s 1", "l 1"))

    voice "ch3.8_l_015"
    l "And I sort of understand why she faked being sick…"

    # [lay1 hide][lay2 +491]
    $ show_sprites(("s 1", "si 1 happy"))

    voice "ch3.8_si_002"
    si "I forgive Haruna-san too, you know."

    # [lay2 hide][lay6 +676]
    $ show_sprites(("s 1", "k 1"))

    voice "ch3.8_k_004"
    k "If Darling puts it that way, I've got no reason to be upset."

    # [lay6 hide][lay0 +588]
    $ show_sprites(("s 1", "t 1"))

    voice "ch3.8_t_002"
    t "I was never mad to begin with."

    # [lay5 hide][lay0 hide][lay7 +957]
    $ show_sprites(("ha 1 sad",))

    voice "ch3.8_ha_007"
    ha "Everyone… I'm sorry for everything. And… thank you."

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay7 hide][BG hide]
    stop music fadeout 1.0

    jump ch3_8_212

label ch3_8_212:
    # ==== SCENE 212 ====
    # [BG +88 (sky)][TRANS][BGM play=+5] → t4
    $ fade_fx("sky", new_music="t4", type="cg")

    voice "ch3.8_ha_008"
    ha "Hiraga-kun. Hiraga-kun!"

    # [lay7 hide — не показан][BG hide][BG +10 (louise_room)][TRANS]
    # [lay5 +390][lay7 +953]
    $ fade_fx("louise_room", sprites=("s 1", "ha 1 happy"))

    voice "ch3.8_s_022"
    s "What's up?"

    # [lay7 +951]
    $ show_sprites(("s 1", "ha 1"))

    voice "ch3.8_ha_009"
    ha "Louise asked me to organize this shelf, but I'm stumped — I can't figure it out."

    # [lay5 +392]
    $ show_sprites(("s 1 happy", "ha 1"))

    voice "ch3.8_s_023"
    s "Let me see… If it's something I can do, just say the word."

    # [lay7 +953]
    $ show_sprites(("s 1 happy", "ha 1 happy"))

    voice "ch3.8_ha_010"
    ha "Thank you! Well then…"

    # [lay5 hide][lay7 hide][lay1 +306]
    $ show_sprites(("l 1 angry",))

    voice "ch3.8_l_016"
    l "Honestly, that Saito! In the end it's all about Haruna! If he wanted to know how the shelf works, he could've asked me!"

    voice "ch3.8_l_017"
    l "A dog! He's a dog! Wags his tail at anyone and everyone — he's definitely a dog!"

    # [lay1 x=-96 — сдвиг не копируется][lay2 +530]
    $ show_sprites(("l 1 angry", "si 4 shy"))

    voice "ch3.8_si_003"
    si "That's so true… Maybe I should get sick too…"

    # [lay1 +335]
    $ show_sprites(("l 3", "si 4 shy"))

    voice "ch3.8_l_018"
    l "Hm? Siesta? Did you just say something?!"

    # [lay2 +493]
    $ show_sprites(("l 3", "si 1 angry"))

    voice "ch3.8_si_004"
    si "N-no! It was nothing, Miss Vallière!"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay2/lay1 hide][BG hide]
    stop music fadeout 1.0

    jump ch3_8_213

label ch3_8_213:
    # ==== SCENE 213 ====
    # [BG +88 (sky)][TRANS][BGM play=+19] → t18; [SE se0 play=+69] — SE не портируется
    $ fade_fx("sky", new_music="t18", type="cg")

    th "Ahhh… Mm, what a nice morning.{#ch3.8_th01}"

    # [lay5 hide — не показан][BG +14 (hallway)][TRANS][lay5 +390]
    $ fade_fx("hallway", sprites=("s 1",))

    th "…Looks like everyone's already finished their morning routine and gone off somewhere.{#ch3.8_th02}"

    th "Well then… what should I do now?{#ch3.8_th03}"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay5 hide][BG hide]
    stop music fadeout 1.0

    $ portrait_choice([
        {"char": "louise",   "text": "Go on a date with Louise",  "target": "date_louise_ch3_8"},
        {"char": "siesta",   "text": "Go on a date with Siesta",  "target": "date_siesta_ch3_9"},
        {"char": "tabitha",  "text": "Go on a date with Tabitha", "target": "date_tabitha_ch3_9"},
        {"char": "kirche",   "text": "Go on a date with Kirche",  "target": "date_kirche_ch3_9"},
        {"char": "haruna",   "text": "Go on a date with Haruna",  "target": "date_haruna_ch3_9"},
    ])

    $ fade_fx("black")
    stop music fadeout 1.0
    jump ch4

label date_louise_ch3_8:
    # ==== SCENE 1059 ====
    # [BG +10 (louise_room)][TRANS][BGM play=+6] → t5; [lay1 +302][lay5 +390]
    $ fade_fx("louise_room", new_music="t5", sprites=("l 1", "s 1"))

    voice "ch3.8_s_024"
    s "Oh, Louise — you're here. …Weren't you going out somewhere?"

    # [lay1 +308]
    $ show_sprites(("l 1 sad", "s 1"))

    voice "ch3.8_l_019"
    l "Saito, where have you been? I've been all feverish and miserable…"

    # [好感度] ルイズ 20
    $ update_sympathy(20, char_key="louise")

    # [lay5 +396]
    $ show_sprites(("l 1 sad", "s 1 sad"))

    voice "ch3.8_s_025"
    s "Whoa, that's some fever. Did you catch a cold?"

    voice "ch3.8_l_020"
    l "Maybe a cold…"

    voice "ch3.8_s_026"
    s "Why didn't you say something?"

    # [lay1 +341]
    $ show_sprites(("l 3 sad", "s 1 sad"))

    voice "ch3.8_l_021"
    l "Because… I did something awful to Haruna, didn't I? I couldn't exactly go around saying I had a fever."

    # [lay5 +394]
    $ show_sprites(("l 3 sad", "s 1 angry"))

    voice "ch3.8_s_027"
    s "Idiot! Stop being so stubborn. Now be a good girl and just lie down."

    # [lay1 +308]
    $ show_sprites(("l 1 sad", "s 1 angry"))

    voice "ch3.8_l_022"
    l "You're such an idiot, Saito… You can't go ordering your master around…"

    # [lay5 +390]
    $ show_sprites(("l 1 sad", "s 1"))

    voice "ch3.8_s_028"
    s "This isn't an order — it's a favor. Get into bed, already!"

    voice "ch3.8_l_023"
    l "…Okay."

    # [lay5 hide][lay1 hide][BG hide][BG +88 (sky)][TRANS] — время идёт
    $ fade_fx("sky", type="cg")

    th "………………{#ch3.8_null_1059}"

    # [BGM stop=1000][BG hide][EVENT_CG +199 (l_sick_3)][TRANS][BGM play=+12] → t11
    stop music fadeout 1.0
    $ fade_fx("l_sick_3", type="cg", new_music="t11")

    voice "ch3.8_s_029"
    s "How's that, Louise?"

    voice "ch3.8_l_024"
    l "Mm. The towel's nice and cold — feels good."

    voice "ch3.8_s_030"
    s "Is that so? …Good."

    voice "ch3.8_s_031"
    s "Anything else you need?"

    # [EVENT_CG +198 (l_sick_2)] imageType=1 — кроссфейд CG
    $ dissolve_fx("l_sick_2", type="cg")

    voice "ch3.8_l_025"
    l "Hmm…{#ch3.8_l_025}"

    voice "ch3.8_s_032"
    s "Hm?"

    voice "ch3.8_l_026"
    l "I kind of want you to do something for me, Saito…"

    voice "ch3.8_s_033"
    s "Something, huh…"

    menu:

        "Peel an apple for her.{#ch3_m1059a}":
            jump ch3_8_l_1060

        "Wipe her down.{#ch3_m1059b}":
            jump ch3_8_l_1061

        "Tell her a story.{#ch3_m1059c}":
            jump ch3_8_l_1062

label ch3_8_l_1060:
    # ==== SCENE 1060 ==== (RESET: [BGM +12]/[EVENT_CG +198] = текущее состояние)
    voice "ch3.8_s_034"
    s "I'll peel the apple for you."

    voice "ch3.8_l_027"
    l "An apple?"

    voice "ch3.8_s_035"
    s "Yeah — an apple. They're great for a cold, y'know."

    voice "ch3.8_s_036"
    s "I'll peel it, so hang on."

    voice "ch3.8_l_028"
    l "…Okay.{#ch3.8_l_028}"

    # [lay1/lay5 hide — не показаны][EVENT_CG hide][wait 1000][EVENT_CG +200 (l_sick_4)][TRANS]
    $ dissolve_fx("l_sick_4", type="cg")

    voice "ch3.8_l_029"
    l "How clumsy."

    voice "ch3.8_s_037"
    s "Don't say that. That kitchen knife was huge, okay?"

    # [EVENT_CG +199 (l_sick_3)] imageType=1 — кроссфейд CG
    $ dissolve_fx("l_sick_3", type="cg")

    voice "ch3.8_l_030"
    l "But… it's tasty."

    # [好感度] ルイズ 10
    $ update_sympathy(10, char_key="louise")

    voice "ch3.8_s_038"
    s "Yeah?{#ch3.8_s_038}"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay1/lay5 hide — не показаны]
    # [EVENT_CG hide][COFFEE → pause(1.0)]
    stop music fadeout 1.0
    pause(1.0)
    return

label ch3_8_l_1061:
    # ==== SCENE 1061 ==== (RESET: [BGM +12]/[EVENT_CG +198] = текущее состояние)
    voice "ch3.8_s_039"
    s "Want me to wipe you down? You're all sweaty."

    # [EVENT_CG +200 (l_sick_4)] — кроссфейд CG
    $ dissolve_fx("l_sick_4", type="cg")

    voice "ch3.8_l_031"
    l "No.{#ch3.8_l_031}"

    # [好感度] ルイズ -10 (TNDL в этой сцене нет — только LIKE)
    $ update_sympathy(-10, char_key="louise")

    voice "ch3.8_s_040"
    s "Yeah… fair enough. Sorry."

    # [EVENT_CG +198 (l_sick_2)] — кроссфейд CG
    $ dissolve_fx("l_sick_2", type="cg")

    voice "ch3.8_l_032"
    l "But… if I'm still asleep tomorrow, I could let you wipe me down."

    voice "ch3.8_s_041"
    s "R-really? You mean it?"

    # [EVENT_CG +200 (l_sick_4)] — кроссфейд CG
    $ dissolve_fx("l_sick_4", type="cg")

    voice "ch3.8_l_033"
    l "Idiot! Don't get the wrong idea! It's just my face — you're only wiping my face!"

    voice "ch3.8_s_042"
    s "I-see…{#ch3.8_s_042}"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay1/lay5 hide — не показаны]
    # [EVENT_CG hide][COFFEE → pause(1.0)]
    stop music fadeout 1.0
    pause(1.0)
    return

label ch3_8_l_1062:
    # ==== SCENE 1062 ==== (RESET: [BGM +12]/[EVENT_CG +198] = текущее состояние)
    voice "ch3.8_s_043"
    s "Now then — how about I tell you a story? …Except I can't read a single one of these…"

    voice "ch3.8_l_034"
    l "Then tell me one you know, Saito."

    voice "ch3.8_s_044"
    s "Is that so? Then… how about…"

    # [lay1/lay5 hide — не показаны][EVENT_CG hide][EVENT_CG +199 (l_sick_3)][TRANS]
    $ dissolve_fx("l_sick_3", type="cg")

    voice "ch3.8_l_035"
    l "…Mm… So sleepy…"

    voice "ch3.8_s_045"
    s "O-oh? Then you'd better get some sleep."

    voice "ch3.8_l_036"
    l "Zzz… zzz…"

    voice "ch3.8_s_046"
    s "Looks like she finally fell asleep. I just hope she gets better by tomorrow…"

    voice "ch3.8_s_047"
    s "Well then — today, I'll just have to keep watch over my princess."

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay1/lay5 hide — не показаны]
    # [EVENT_CG hide][COFFEE → pause(1.0)]
    stop music fadeout 1.0
    pause(1.0)
    return
