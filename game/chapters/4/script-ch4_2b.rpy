# Глава 4, часть 2b (даты карты-хаба 【移動】: сцены 1347–1366) — четыре даты,
# выбираемые из хаба сцены 225 (script-ch4_2.rpy): Сиеста (кухня), Кирхе
# (двор), Табита (коридор), Харуна (комната Луизы). Каждый лейбл вызывается
# из хаба через sprite_choice (renpy.call) и заканчивается `return`;
# ветки-сцены 연결ены `jump` внутри даты.
# Источник: ps2_source/chapters/chapter_05_トリスタニアの危機.txt
#   (SCENE 1347–1351, 1352–1356, 1357–1361, 1362–1366).
# Точные аргументы: ps2_source/events_full/chapter_05_トリスタニアの危機.txt.
# Голоса: ch4.2_<spk>_<NNN> — продолжение нумерации части 4_2 (sub-part группы
#   ch4.2: s 044…, si 011…, k 003…, t 006…, ha 010…, d 002…; 103 голоса).
# Без голоса: мысли Сайто ×9 (1347 ×4, 1357 ×3, 1361 ×1, 1362 ×1) + молчаливые
#   реплики Табиты ×2 (1361 «……。» ×2) — без voice.
# SE (se1 +44 в 1347, se0 +77 в 1351, se0 +72 в 1357, se0 +57/+56 в 1362,
#   se1 stop) — не портируются (AGENTS §6).
# CG 119 — зарегистрирован в image_id_map.csv как k_hug_3 (файл есть);
#   заглушка не нужна.
# Спрайты: +3 регистрации блока «ha 2» — 964 = ha 2 happy, 966 = ha 2 angry,
#   970 = ha 2 shy (попиксельная сверка SCENEDAT[964/966/970]).
# Слои level=/x=/y= источника (155/156/157, сдвиги) не копируются — layout
#   расставляет show_sprites; см. комментарии по месту.
# Стоимость: 【好感度】 Сиеста 20/-10/+10, Кирхе 20/-10/-10, Табита 30/+15/-15/-15,
#   Харуна 20/+10/-10 — 12 вызовов update_sympathy.
# Прочие ветки-сцены (1367–1382, второй хаб) — в следующих частях.


label date_siesta_ch4_2:
    # ==== SCENE 1347 (кухня) ====
    # [BG +32 (kitchen)][TRANS][BGM play=+7 → t6][SE se1 +44 — SE не портируется]
    $ fade_fx("kitchen", new_music="t6")

    th "Siesta seemed awfully down. I wonder if she's all right…"
    th "I mean, after everything she did for Haruna, being told to stay behind…"
    th "And — she really is crouched down there in the kitchen."

    # [lay2 +495 (si 1 sad)]
    $ show_sprites(("si 1 sad",))

    voice "ch4.2_si_011"
    si "Just me left behind… Just me left behind… Just me left behind…"

    # 【好感度】シエスタ 20
    $ update_sympathy(20, char_key="siesta")

    # [lay2 x=-96 — сдвиг][lay19 +946 (d 1 sad)]
    $ show_sprites(("si 1 sad", "d 1 sad"))

    voice "ch4.2_d_002"
    d "Partner, she looks like a pretty serious case."

    th "Hmm. What am I supposed to say to cheer her up?"

    # ==== 【選択肢】 (1347) → 1348/1349/1350, сходятся в 1351 ====
    menu:

        "Tell her it's a dangerous mission.{#ch4.2b_m1347a}":
            jump ch4_2b_siesta_1348

        "Tell her I'll bring back a souvenir.{#ch4.2b_m1347b}":
            jump ch4_2b_siesta_1349

        "Tell her it's absolutely out of the question.{#ch4.2b_m1347c}":
            jump ch4_2b_siesta_1350


label ch4_2b_siesta_1348:
    # ==== SCENE 1348 ==== (RESET: [lay19 +946][lay2 +495][BG +32][BGM +7] —
    # состояние на конец 1347; далее [lay19 hide] и [lay5 +396 (s 1 sad)])
    $ show_sprites(("si 1 sad", "s 1 sad"))

    voice "ch4.2_s_044"
    s "Siesta. This is a dangerous mission. There's no way I could take you along, right?"

    voice "ch4.2_si_012"
    si "…A… dangerous… mission."

    # [lay5 +390 (s 1)]
    $ show_sprites(("si 1 sad", "s 1"))

    voice "ch4.2_s_045"
    s "That's why Louise isn't taking you, Siesta. Can't you understand?"

    # [lay2 +493 (si 1 angry)]
    $ show_sprites(("si 1 angry", "s 1"))

    voice "ch4.2_si_013"
    si "No!"

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("si 1 angry", "s 3 sad"))

    voice "ch4.2_s_046"
    s "Whoa…"

    # [lay2 +528 (si 4 sad)]
    $ show_sprites(("si 4 sad", "s 3 sad"))

    voice "ch4.2_si_014"
    si "If it's a dangerous mission, that's all the more reason. Leaving you to face the danger all alone — I couldn't bear it!"

    # 【好感度】シエスタ -10
    $ update_sympathy(-10, char_key="siesta")

    # [lay5 +396 (s 1 sad)]
    $ show_sprites(("si 4 sad", "s 1 sad"))

    voice "ch4.2_s_047"
    s "Siesta…{#ch4.2b_s_047}"

    jump ch4_2b_siesta_1351


label ch4_2b_siesta_1349:
    # ==== SCENE 1349 ==== (RESET: [lay19 +946][lay2 +495][BG +32][BGM +7] —
    # состояние на конец 1347; далее [lay19 hide] и [lay5 +390 (s 1)])
    $ show_sprites(("si 1 sad", "s 1"))

    voice "ch4.2_s_048"
    s "Siesta. I'll bring you back a proper souvenir, so give it up this time."

    voice "ch4.2_si_015"
    si "A souvenir… I don't want one."

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("si 1 sad", "s 3 sad"))

    voice "ch4.2_s_049"
    s "Hmm. So a souvenir won't do it either…"

    # [lay2 +530 (si 4 shy)]
    $ show_sprites(("si 4 shy", "s 3 sad"))

    voice "ch4.2_si_016"
    si "Th-then… Saito-san, would you go on a date with me when you get back?"

    # 【好感度】シエスタ 10
    $ update_sympathy(10, char_key="siesta")

    # [lay5 +396 (s 1 sad)]
    $ show_sprites(("si 4 shy", "s 1 sad"))

    voice "ch4.2_s_050"
    s "A d-date? Wh-why?"

    jump ch4_2b_siesta_1351


label ch4_2b_siesta_1350:
    # ==== SCENE 1350 ==== (RESET: [lay19 +946][lay2 +495][BG +32][BGM +7] —
    # состояние на конец 1347; далее [lay19 hide] и [lay5 +390 (s 1)])
    $ show_sprites(("si 1 sad", "s 1"))

    voice "ch4.2_s_051"
    s "Siesta."

    # [lay2 +528 (si 4 sad)]
    $ show_sprites(("si 4 sad", "s 1"))

    voice "ch4.2_si_017"
    si "Ah… Saito-san…"

    # [lay5 +396 (s 1 sad)]
    $ show_sprites(("si 4 sad", "s 1 sad"))

    voice "ch4.2_s_052"
    s "No means no. You're grown up now, so don't go throwing tantrums."

    jump ch4_2b_siesta_1351


label ch4_2b_siesta_1351:
    # ==== SCENE 1351 (общее схождение) ====
    # [lay2 +528][lay5 +396][BGM +7][SE se1 +44] — состояние на конец ветки;
    # [lay2 +491 (si 1 happy)][SE se0 +77 — SE не портируется]
    $ show_sprites(("si 1 happy", "s 1 sad"))

    voice "ch4.2_si_018"
    si "Ahh!! You're right!"

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("si 1 happy", "s 3 sad"))

    voice "ch4.2_s_053"
    s "Siesta, what's the matter?"

    # [lay2 +524 (si 4 happy)]
    $ show_sprites(("si 4 happy", "s 3 sad"))

    voice "ch4.2_si_019"
    si "Honestly, what am I doing. I'm sorry, Saito-san. Thank you for worrying about me."

    # [lay2 +489 (si 1)]
    $ show_sprites(("si 1", "s 3 sad"))

    voice "ch4.2_si_020"
    si "I'm all right now, so please don't worry."

    # [lay5 +390 (s 1)]
    $ show_sprites(("si 1", "s 1"))

    voice "ch4.2_s_054"
    s "Well, if you say so…"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay2 hide][lay5 hide][BG hide]
    stop music fadeout 1.0
    $ ch4_2_visited.add("kitchen")
    # return (а не jump): карта вызвала лейбл через renpy.call (sprite_choice).
    return


label date_kirche_ch4_2:
    # ==== SCENE 1352 (двор) ====
    # [BG +26 (yard)][TRANS][BGM play=+8 → t7][lay6 +709 (k 4) dir=2A]
    $ fade_fx("yard", new_music="t7", sprites=("k 4",))

    voice "ch4.2_k_003"
    k "Darling, found you."

    # 【好感度】キュルケ 20
    $ update_sympathy(20, char_key="kirche")

    # [lay6 x=-96 — сдвиг][lay5 +390 (s 1)]
    $ show_sprites(("k 4", "s 1"))

    voice "ch4.2_s_055"
    s "Ah, Kirche."

    # [lay6 +676 (k 1)]
    $ show_sprites(("k 1", "s 1"))

    voice "ch4.2_k_004"
    k "I heard you're going off to Tristania?"

    # [lay5 +396 (s 1 sad)]
    $ show_sprites(("k 1", "s 1 sad"))

    voice "ch4.2_s_056"
    s "Ugh. That was supposed to be a secret, wasn't it? Where did you hear that?"

    voice "ch4.2_k_005"
    k "Mm, a secret."

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("k 1", "s 3 sad"))

    voice "ch4.2_s_057"
    s "Tch.{#ch4.2b_s_057}"

    # [lay6 +709 (k 4)]
    $ show_sprites(("k 4", "s 3 sad"))

    voice "ch4.2_k_006"
    k "But I never heard why. Just what are you going there for?"

    # [lay5 +390 (s 1)]
    $ show_sprites(("k 4", "s 1"))

    voice "ch4.2_s_058"
    s "Uh, well…"

    # ==== 【選択肢】 (1352) → 1353/1354/1355, сходятся в 1356 ====
    menu:

        "There are reasons I can't tell you.{#ch4.2b_m1352a}":
            jump ch4_2b_kirche_1353

        "I'm taking Haruna sightseeing.{#ch4.2b_m1352b}":
            jump ch4_2b_kirche_1354

        "The headmaster asked me to run an errand.{#ch4.2b_m1352c}":
            jump ch4_2b_kirche_1355


label ch4_2b_kirche_1353:
    # ==== SCENE 1353 ==== (RESET: [lay5 +390][lay6 +709][BG +26][BGM +8] =
    # текущее состояние; далее [lay5 +396 (s 1 sad)])
    $ show_sprites(("k 4", "s 1 sad"))

    voice "ch4.2_s_059"
    s "It's, uh, reasons I can't really tell you…"

    # [lay6 +715 (k 4 sad)]
    $ show_sprites(("k 4 sad", "s 1 sad"))

    voice "ch4.2_k_007"
    k "Whaat. How boring."

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("k 4 sad", "s 3 sad"))

    voice "ch4.2_s_060"
    s "Even if you call it boring… Well, it's a secret."

    jump ch4_2b_kirche_1356


label ch4_2b_kirche_1354:
    # ==== SCENE 1354 ==== (RESET: [lay5 +390][lay6 +709][BG +26][BGM +8] =
    # текущее состояние; вызов идемпотентен — для трассируемости сверки)
    $ show_sprites(("k 4", "s 1"))

    voice "ch4.2_s_061"
    s "Since Haruna went to all the trouble of coming to this world, I thought I'd show her around…"

    # [lay6 +715 (k 4 sad)]
    $ show_sprites(("k 4 sad", "s 1"))

    voice "ch4.2_k_008"
    k "Really?{#ch4.2b_k_008}"

    # 【好感度】キュルケ -10
    $ update_sympathy(-10, char_key="kirche")

    # [lay5 +423 (s 3)]
    $ show_sprites(("k 4 sad", "s 3"))

    voice "ch4.2_s_062"
    s "N-no, really. For real, seriously."

    jump ch4_2b_kirche_1356


label ch4_2b_kirche_1355:
    # ==== SCENE 1355 ==== (RESET: [lay5 +390][lay6 +709][BG +26][BGM +8] =
    # текущее состояние; далее [lay5 +425 (s 3 happy)])
    $ show_sprites(("k 4", "s 3 happy"))

    voice "ch4.2_s_063"
    s "The headmaster asked me to go shopping for him. Man, what a pain."

    # [lay6 +715 (k 4 sad)]
    $ show_sprites(("k 4 sad", "s 3 happy"))

    voice "ch4.2_k_009"
    k "Really?{#ch4.2b_k_009}"

    # 【好感度】キュルケ -10
    $ update_sympathy(-10, char_key="kirche")

    # [lay5 +423 (s 3)]
    $ show_sprites(("k 4 sad", "s 3"))

    voice "ch4.2_s_064"
    s "I-it's true. See, his eyesight's gotten worse lately, so he's getting new glasses or something."

    jump ch4_2b_kirche_1356


label ch4_2b_kirche_1356:
    # ==== SCENE 1356 (общее схождение) ====
    # [lay5 +429][lay6 +715][BG +26][BGM +8] — состояние на конец ветки;
    # [lay6 +676 (k 1)]
    $ show_sprites(("k 1", "s 3 sad"))

    voice "ch4.2_k_010"
    k "Hmm…{#ch4.2b_k_010}"

    voice "ch4.2_k_011"
    k "Well, you do look like you're in a pinch, so I'll let it go at that."

    # [lay6 +715 (k 4 sad)]
    $ show_sprites(("k 4 sad", "s 3 sad"))

    voice "ch4.2_k_012"
    k "But, but. When I think I won't see you for a while, darling, I get so lonely."

    # [lay5 hide][lay6 hide][BG hide][EVENT_CG +119 (k_hug_3)][TRANS]
    $ fade_fx("k_hug_3", type="cg")

    voice "ch4.2_k_013"
    k "Oh, I just have to give you a big squeeze."

    voice "ch4.2_s_065"
    s "Hey, Kirche! Cut it out, everyone's watching!"

    voice "ch4.2_k_014"
    k "Why? It's fine, isn't it? Savings for the time we won't see each other!"

    voice "ch4.2_k_015"
    k "Come on, come on."

    voice "ch4.2_s_066"
    s "H-have mercy on me…"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay5 hide][lay6 hide][BG hide][EVENT_CG hide]
    stop music fadeout 1.0
    $ ch4_2_visited.add("yard")
    return


label date_tabitha_ch4_2:
    # ==== SCENE 1357 (коридор) ====
    # [BG +14 (hallway)][TRANS][BGM play=+9 → t8][LAYER lay0 +588 (t 1)]
    $ fade_fx("hallway", new_music="t8", sprites=("t 1",))

    th "Huh, it's Tabitha."

    voice "ch4.2_t_006"
    t "I was looking for you."

    # 【好感度】タバサ 30
    $ update_sympathy(30, char_key="tabitha")

    # [LAYER lay0 x=-96 — сдвиг][lay5 +390 (s 1)]
    $ show_sprites(("t 1", "s 1"))

    voice "ch4.2_s_067"
    s "Looking for me? That's rare, coming from you… Did something happen?"

    # [LAYER lay0 +621 (t 4)]
    $ show_sprites(("t 4", "s 1"))

    voice "ch4.2_t_007"
    t "This."

    voice "ch4.2_s_068"
    s "This book… for me?"

    # [LAYER lay0 +588 (t 1)]
    $ show_sprites(("t 1", "s 1"))

    voice "ch4.2_t_008"
    t "I'll lend it to you."

    # [SE se0 +72 — SE не портируется]
    th "Flipping through the pages, I found pictures of a noble-looking man's life from morning to night."
    th "There's writing as well, but… what kind of book is this?"

    # ==== 【選択肢】 (1357) → 1358/1359/1360, сходятся в 1361 ====
    menu:

        "A book about noble life?{#ch4.2b_m1357a}":
            jump ch4_2b_tabitha_1358

        "A book about Tabitha's family?{#ch4.2b_m1357b}":
            jump ch4_2b_tabitha_1359

        "A book with some kind of story?{#ch4.2b_m1357c}":
            jump ch4_2b_tabitha_1360


label ch4_2b_tabitha_1358:
    # ==== SCENE 1358 ==== (RESET: [lay5 +390][lay0 +588][BG +14][BGM +9] =
    # состояние на конец 1357; далее [lay5 +423 (s 3)])
    $ show_sprites(("t 1", "s 3"))

    voice "ch4.2_s_069"
    s "Could this be a book about noble life?"

    # [LAYER lay0 +590 (t 1 happy)]
    $ show_sprites(("t 1 happy", "s 3"))

    voice "ch4.2_t_009"
    t "I thought it might be useful…"

    # 【好感度】タバサ 15
    $ update_sympathy(15, char_key="tabitha")

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("t 1 happy", "s 3 sad"))

    voice "ch4.2_s_070"
    s "Hmm, if only I could read the writing…"

    # [lay19 +946 (d 1 sad)][lay5 level=157][lay0 level=156] — level не копируется
    $ show_sprites(("d 1 sad", "t 1 happy", "s 3 sad"))

    jump ch4_2b_tabitha_1361


label ch4_2b_tabitha_1359:
    # ==== SCENE 1359 ==== (RESET: [lay5 +390][lay0 +588][BG +14][BGM +9] =
    # состояние на конец 1357; далее [lay5 +423 (s 3)])
    $ show_sprites(("t 1", "s 3"))

    voice "ch4.2_s_071"
    s "Could this be a book about the customs of Tabitha's family?"

    # [LAYER lay0 +594 (t 1 sad)]
    $ show_sprites(("t 1 sad", "s 3"))

    voice "ch4.2_t_010"
    t "Not at all."

    # 【好感度】タバサ -15
    $ update_sympathy(-15, char_key="tabitha")

    # [lay19 +940 (d 1)][lay5 level=157][lay0 level=156] — level не копируется
    $ show_sprites(("t 1 sad", "s 3", "d 1"))

    voice "ch4.2_d_003"
    d "Hey, partner. This is a book showing the manners of noble life."

    # [lay5 +429 (s 3 sad)][level 160/156/155 — не копируется]
    $ show_sprites(("t 1 sad", "s 3 sad", "d 1"))

    voice "ch4.2_s_072"
    s "Huh, noble manners? But I can't read the writing, so I've got no idea what's what.{#ch4.2b_s_072}"

    # [lay19 +946 (d 1 sad)][lay5 level=157][lay0 level=156] — level не копируется
    $ show_sprites(("d 1 sad", "t 1 sad", "s 3 sad"))

    jump ch4_2b_tabitha_1361


label ch4_2b_tabitha_1360:
    # ==== SCENE 1360 ==== (RESET: [lay5 +390][lay0 +588][BG +14][BGM +9] =
    # состояние на конец 1357; далее [lay5 +423 (s 3)])
    $ show_sprites(("t 1", "s 3"))

    voice "ch4.2_s_073"
    s "Could this be some kind of storybook?"

    voice "ch4.2_t_011"
    t "No.{#ch4.2b_t_011}"

    # 【好感度】タバサ -15
    $ update_sympathy(-15, char_key="tabitha")

    # [lay19 +940 (d 1)][lay5 level=157][lay0 level=156] — level не копируется
    $ show_sprites(("t 1", "s 3", "d 1"))

    voice "ch4.2_d_004"
    d "Hey, partner. This is a book showing the manners of noble life.{#ch4.2b_d_004}"

    # [lay5 +429 (s 3 sad)][level 160/156/155 — не копируется]
    $ show_sprites(("t 1", "s 3 sad", "d 1"))

    voice "ch4.2_s_074"
    s "Huh, noble manners? But I can't read the writing, so I've got no idea what's what.{#ch4.2b_s_074}"

    # [lay19 +946 (d 1 sad)][lay5 level=157][lay0 level=156] — level не копируется
    $ show_sprites(("d 1 sad", "t 1", "s 3 sad"))

    jump ch4_2b_tabitha_1361


label ch4_2b_tabitha_1361:
    # ==== SCENE 1361 (общее схождение) ====
    # [lay19 +946 (d 1 sad)][lay5 +429 (s 3 sad)][lay0 +590 (t 1 happy)][BGM +9][BG +14]
    $ show_sprites(("d 1 sad", "t 1 happy", "s 3 sad"))

    voice "ch4.2_d_005"
    d "How pathetic. Partner, you'd better learn to read one of these days."

    # [lay19 +940 (d 1)][lay5 +396 (s 1 sad)]
    $ show_sprites(("d 1", "t 1 happy", "s 1 sad"))

    voice "ch4.2_s_075"
    s "Can't help it, right? It's not like I'm staying in this world forever."

    # [LAYER lay0 +588 (t 1)]
    $ show_sprites(("d 1", "t 1", "s 1 sad"))

    t "……。{#ch4.2b_t_001}"

    # [lay19 level=155][lay5 level=157][lay0 level=156] — level не копируется
    voice "ch4.2_d_006"
    d "If it's writing, I can read it. I'll read it to you later."

    # [lay5 +423 (s 3)]
    $ show_sprites(("d 1", "t 1", "s 3"))

    voice "ch4.2_s_076"
    s "S-seriously?"

    # [lay5 +390 (s 1)]
    $ show_sprites(("d 1", "t 1", "s 1"))

    voice "ch4.2_s_077"
    s "Well, hearing 'manners' makes me nervous, but I suppose it's better to know."

    # [lay19 level=155][lay5 level=157][lay0 level=156] — level не копируется
    voice "ch4.2_d_007"
    d "That's right. She picked out a book with plenty of pictures for you. Be grateful to the girl there."

    # [lay19 hide][lay5 +423 (s 3)]
    $ show_sprites(("t 1", "s 3"))

    voice "ch4.2_s_078"
    s "Huh, for me…? She went out of her way?"

    # [LAYER lay0 +596 (t 1 shy)]
    $ show_sprites(("t 1 shy", "s 3"))

    t "……。{#ch4.2b_t_002}"

    # [lay5 +392 (s 1 happy)]
    $ show_sprites(("t 1 shy", "s 1 happy"))

    voice "ch4.2_s_079"
    s "Thanks, Tabitha. I owe you one."

    # [LAYER lay0 +590 (t 1 happy)]
    $ show_sprites(("t 1 happy", "s 1 happy"))

    voice "ch4.2_t_012"
    t "Yeah…"

    # [lay5 +396 (s 1 sad)]
    $ show_sprites(("t 1 happy", "s 1 sad"))

    th "Hmm, but when did I ever tell Tabitha that I'd be meeting a noble?"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay5 hide][lay0 hide][BG hide]
    stop music fadeout 1.0
    $ ch4_2_visited.add("hallway")
    return


label date_haruna_ch4_2:
    # ==== SCENE 1362 (комната Луизы) ====
    # [SE se0 +57 — SE не портируется][BG +10 (louise_room)][TRANS]
    # [BGM play=+11 → t10][lay7 +964 (ha 2 happy) dir=1B]
    $ fade_fx("louise_room", new_music="t10", sprites=("ha 2 happy",))

    voice "ch4.2_ha_010"
    ha "Ah, Hiraga-kun?"

    # 【好感度】ハルナ 20
    $ update_sympathy(20, char_key="haruna")

    # [SE se0 +56 — SE не портируется][lay7 x=-96 — сдвиг][lay5 +429 (s 3 sad)]
    $ show_sprites(("ha 2 happy", "s 3 sad"))

    voice "ch4.2_s_080"
    s "Um, who are you?"

    voice "ch4.2_ha_011"
    ha "Hiraga-kun, you're such a flatterer. It's me, me. Haruna."

    # [lay5 +390 (s 1)]
    $ show_sprites(("ha 2 happy", "s 1"))

    voice "ch4.2_s_081"
    s "Oh, it's Haruna? I didn't recognize you for a second. What's with the outfit?"

    # [lay7 +962 (ha 2)]
    $ show_sprites(("ha 2", "s 1"))

    voice "ch4.2_ha_012"
    ha "Louise-san said it'd be boring to always wear the same clothes, so she lent me this."

    # [lay5 +423 (s 3)]
    $ show_sprites(("ha 2", "s 3"))

    voice "ch4.2_s_082"
    s "Huh, that Louise, of all people…"

    # [lay7 +970 (ha 2 shy)]
    $ show_sprites(("ha 2 shy", "s 3"))

    voice "ch4.2_ha_013"
    ha "Hiraga-kun, how do I look? It's been so long since I wore anything but my uniform, I'm embarrassed."

    # [lay5 +390 (s 1)][lay7 +962 (ha 2)]
    $ show_sprites(("ha 2", "s 1"))

    th "Let's see…"

    # ==== 【選択肢】 (1362) → 1363/1364/1365, сходятся в 1366 ====
    menu:

        "It really suits you.{#ch4.2b_m1362a}":
            jump ch4_2b_haruna_1363

        "I'd like some new clothes too.{#ch4.2b_m1362b}":
            jump ch4_2b_haruna_1364

        "Clothes make the man, as they say.{#ch4.2b_m1362c}":
            jump ch4_2b_haruna_1365


label ch4_2b_haruna_1363:
    # ==== SCENE 1363 ==== (RESET: [lay7 +962][lay5 +390][BG +10][BGM +11] =
    # состояние на конец 1362; далее [lay5 +431 (s 3 shy)])
    $ show_sprites(("ha 2", "s 3 shy"))

    voice "ch4.2_s_083"
    s "It suits you pretty well, doesn't it?"

    # [lay7 +970 (ha 2 shy)]
    $ show_sprites(("ha 2 shy", "s 3 shy"))

    voice "ch4.2_ha_014"
    ha "Y-you think so?"

    # 【好感度】ハルナ 10
    $ update_sympathy(10, char_key="haruna")

    # [lay7 +962 (ha 2)]
    $ show_sprites(("ha 2", "s 3 shy"))

    voice "ch4.2_ha_015"
    ha "Like I said before, I've been in my uniform all this time, right?"

    # [lay7 +964 (ha 2 happy)]
    $ show_sprites(("ha 2 happy", "s 3 shy"))

    voice "ch4.2_ha_016"
    ha "Wearing something different puts me in a happy mood. Clothes really do matter."

    jump ch4_2b_haruna_1366


label ch4_2b_haruna_1364:
    # ==== SCENE 1364 ==== (RESET: [lay7 +962][lay5 +390][BG +10][BGM +11] =
    # состояние на конец 1362; далее [lay5 +429 (s 3 sad)])
    $ show_sprites(("ha 2", "s 3 sad"))

    voice "ch4.2_s_084"
    s "I'd like some new clothes too. I've been wearing pretty much this since I came to this world."

    # [lay7 +968 (ha 2 sad)]
    $ show_sprites(("ha 2 sad", "s 3 sad"))

    voice "ch4.2_ha_017"
    ha "If I had money, I'd buy you some…"

    # [lay5 +390 (s 1)]
    $ show_sprites(("ha 2 sad", "s 1"))

    voice "ch4.2_s_085"
    s "No, the thought alone makes me happy. Really, I wish Louise had even a bit of that in her…"

    # [lay7 +962 (ha 2)]
    $ show_sprites(("ha 2", "s 1"))

    voice "ch4.2_ha_018"
    ha "My, Louise-san isn't as awful a person as you think she is."

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("ha 2", "s 3 sad"))

    voice "ch4.2_s_086"
    s "Really?{#ch4.2b_s_086}"

    jump ch4_2b_haruna_1366


label ch4_2b_haruna_1365:
    # ==== SCENE 1365 ==== (RESET: [lay7 +962][lay5 +390][BG +10][BGM +11] =
    # состояние на конец 1362; далее [lay5 +423 (s 3)])
    $ show_sprites(("ha 2", "s 3"))

    voice "ch4.2_s_087"
    s "Clothes make the man — they said it well…"

    # [lay7 +966 (ha 2 angry)]
    $ show_sprites(("ha 2 angry", "s 3"))

    voice "ch4.2_ha_019"
    ha "Hiraga-kun, that's so mean."

    # 【好感度】ハルナ -10
    $ update_sympathy(-10, char_key="haruna")

    # [lay5 +425 (s 3 happy)]
    $ show_sprites(("ha 2 angry", "s 3 happy"))

    voice "ch4.2_s_088"
    s "No, I'm joking, joking. I think it suits you quite well."

    # [lay7 +970 (ha 2 shy)]
    $ show_sprites(("ha 2 shy", "s 3 happy"))

    voice "ch4.2_ha_020"
    ha "Y-you think so? Thanks, Hiraga-kun."

    # [lay5 +398 (s 1 shy)]
    $ show_sprites(("ha 2 shy", "s 1 shy"))

    voice "ch4.2_s_089"
    s "N-no, it's nothing."

    jump ch4_2b_haruna_1366


label ch4_2b_haruna_1366:
    # ==== SCENE 1366 (общее схождение) ====
    # [lay7 +964 (ha 2 happy)][lay5 +431 (s 3 shy)][BG +10][BGM +11][lay5 +390 (s 1)]
    $ show_sprites(("ha 2 happy", "s 1"))

    voice "ch4.2_s_090"
    s "By the way, no offense, but wasn't Louise's outfit a bit small?"

    # [lay7 +968 (ha 2 sad)]
    $ show_sprites(("ha 2 sad", "s 1"))

    voice "ch4.2_ha_021"
    ha "Eek."

    # [lay5 +423 (s 3)]
    $ show_sprites(("ha 2 sad", "s 3"))

    voice "ch4.2_s_091"
    s "I mean, Louise is petite, right? I was wondering if it'd fit you."

    # [lay7 +962 (ha 2)]
    $ show_sprites(("ha 2", "s 3"))

    voice "ch4.2_ha_022"
    ha "Actually, I was thinking it's a bit tight."

    # [lay5 +390 (s 1)]
    $ show_sprites(("ha 2", "s 1"))

    voice "ch4.2_s_092"
    s "Ah, so it is?"

    # [lay7 +964 (ha 2 happy)]
    $ show_sprites(("ha 2 happy", "s 1"))

    voice "ch4.2_ha_023"
    ha "Hahahaha.{#ch4.2b_ha_023}"

    # [lay5 +425 (s 3 happy)]
    $ show_sprites(("ha 2 happy", "s 3 happy"))

    voice "ch4.2_s_093"
    s "Hahahaha.{#ch4.2b_s_093}"

    # [lay7 +970 (ha 2 shy)]
    $ show_sprites(("ha 2 shy", "s 3 happy"))

    voice "ch4.2_ha_024"
    ha "Hiraga-kun, you pervert."

    # [lay7 +962 (ha 2)]
    $ show_sprites(("ha 2", "s 3 happy"))

    voice "ch4.2_ha_025"
    ha "If you keep asking girls things like that, I'll have to punish you — Louise-san would, anyway."

    # [lay5 +423 (s 3)]
    $ show_sprites(("ha 2", "s 3"))

    voice "ch4.2_s_094"
    s "N-no, spare me that…"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay7 hide][lay5 hide][BG hide]
    stop music fadeout 1.0
    $ ch4_2_visited.add("h_room")
    return
