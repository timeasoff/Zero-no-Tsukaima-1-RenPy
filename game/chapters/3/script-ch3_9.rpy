# Глава 3, часть 9 (даты 1064–1083): свидания с Сиестой, Табитой, Кирхе и
# Харуной — финал главы 3. Вход — call из portrait_choice сцены 213 (часть 8):
# четыре линии date_*_ch3_9, в каждой меню на 3 ответа, ветки сходятся в
# финальную сцену линии (1068/1073/1078/1083), которая заканчивается return —
# управление возвращается в ch3_8_213 → fade чёрным → jump ch4 (сцена 219
# «дата с кем угодно» = глава 4; решение (5) в reports/log.md).
# Источник: ps2_source/chapters/chapter_04_女の戦い.txt (SCENE 1064–1083).
# Точные аргументы: ps2_source/events_full/chapter_04_女の戦い.txt (те же сцены).
# Голоса: ch3.9_s_001…065, ch3.9_si_001…016, ch3.9_t_001…009,
#         ch3.9_k_001…013, ch3.9_ha_001…011 (114).
# Без голоса (только текст): мысли сайта в 1064/1069 (теги ch3.9_th_1064/
# ch3.9_th_1069) + null-многоточие Табиты 1073 (тег ch3.9_t_v01).
# COFFEE в финалах 1068/1073/1078/1083 → pause(1.0) (сигнатура не реализована).
# SE (se0 +82/+57 в сцене 1074, se1 stop=1 на границах) не портируется.
# CG без имён (заглушки image_id_map): id(219)/id(220) — шарф Сиесты,
# id(236)/id(237) — Табита с Сильфидой, id(270) — нулевой истребитель.
# Ветки и финалы входят в RESET-состояние (BGM/CG/спрайты = текущие —
# комментарий сцены). Особый случай — сцена 1078: показ s 1 sad на входе
# реален для ветки 1076 (заканчивалась s 1) и no-op для 1075/1077.

label date_siesta_ch3_9:
    # ==== SCENE 1064 ====
    # [BG +26 (yard)][TRANS][BGM play=+7] → t6; [lay5 +390]
    $ fade_fx("yard", new_music="t6", sprites=("s 1",))

    voice "ch3.9_s_001"
    s "Ah, Siesta — so this is where you were."

    # [lay5 x=224 — сдвиг не копируется][lay2 +491 (si 1 happy)]
    $ show_sprites(("si 1 happy", "s 1"))

    voice "ch3.9_si_001"
    si "Saito! You showed up at just the right time!"

    # [好感度] シエスタ 20
    $ update_sympathy(20, char_key="siesta")

    voice "ch3.9_s_002"
    s "Did you need me for something?"

    # [lay2 +524 (si 4 happy)]
    $ show_sprites(("si 4 happy", "s 1"))

    voice "ch3.9_si_002"
    si "Yes! There's something I'd really like you to see, Saito!"

    # [lay5 +423 (s 3)]
    $ show_sprites(("si 4 happy", "s 3"))

    voice "ch3.9_s_003"
    s "Oh? What is it? Now I'm curious."

    # [lay2 hide][lay5 hide][BG hide][EVENT_CG +219][TRANS]
    # (fade покрывает удаление спрайтов и фона; CG без имени → заглушка id(219))
    $ fade_fx("id(219)", type="cg")

    voice "ch3.9_si_003"
    si "Please — take this scarf!"

    voice "ch3.9_s_004"
    s "For me? A hand-knitted scarf — are you sure? Heh… that really makes me happy."

    # [EVENT_CG +220] — кроссфейд CG
    $ dissolve_fx("id(220)", type="cg")

    voice "ch3.9_si_004"
    si "I'm glad you said that…"

    voice "ch3.9_s_005"
    s "Hm? You just gave me a scarf — so why are you still knitting?"

    # [EVENT_CG +219] — кроссфейд CG
    $ dissolve_fx("id(219)", type="cg")

    voice "ch3.9_si_005"
    si "The one on my needles now is my second one."

    voice "ch3.9_s_006"
    s "A second one!? Don't tell me — both of them are the same pattern?"

    voice "ch3.9_si_006"
    si "Yes…{#ch3.9_si_006}"

    # без голоса: мысль сайта (канон без [voice])
    th "Hmm… let's see…{#ch3.9_th_1064}"

    menu:

        "Is that a pair look?{#ch3_m1064a}":
            jump ch3_9_si_1065

        "Some skill, huh.{#ch3_m1064b}":
            jump ch3_9_si_1066

        "Wouldn't a different pattern be better?{#ch3_m1064c}":
            jump ch3_9_si_1067

label ch3_9_si_1065:
    # ==== SCENE 1065 ==== (RESET: [BGM +7]/[EVENT_CG +219] = текущее состояние)
    voice "ch3.9_s_007"
    s "Is that a pair look?{#ch3.9_s_007}"

    voice "ch3.9_si_007"
    si "What's a 'pair look'?"

    voice "ch3.9_s_008"
    s "When two people wear matching clothes — same design and all — and go around together."

    voice "ch3.9_si_008"
    si "Like how all the students wear the same uniform?"

    voice "ch3.9_s_009"
    s "No, no. Everyone wearing the same thing doesn't count as a pair look."

    voice "ch3.9_s_010"
    s "The point is that it's just the two of you."

    # [EVENT_CG +220] — кроссфейд CG
    $ dissolve_fx("id(220)", type="cg")

    voice "ch3.9_si_009"
    si "Just the two of us…"

    # [好感度] シエスタ 10
    $ update_sympathy(10, char_key="siesta")

    jump ch3_9_si_1068

label ch3_9_si_1066:
    # ==== SCENE 1066 ==== (RESET: [BGM +7]/[EVENT_CG +219] = текущее состояние)
    voice "ch3.9_s_011"
    s "That's some serious skill. Louise knits too, but hers never came out this good."

    voice "ch3.9_s_012"
    s "She gave me a really tiny sweater once."

    voice "ch3.9_si_010"
    si "I won't lose…"

    # [好感度] シエスタ -10
    $ update_sympathy(-10, char_key="siesta")

    voice "ch3.9_s_013"
    s "Hm? What's up, Siesta?"

    # [EVENT_CG +220] — кроссфейд CG
    $ dissolve_fx("id(220)", type="cg")

    voice "ch3.9_si_011"
    si "No, it's nothing. Nothing at all~"

    jump ch3_9_si_1068

label ch3_9_si_1067:
    # ==== SCENE 1067 ==== (RESET: [BGM +7]/[EVENT_CG +219] = текущее состояние)
    voice "ch3.9_s_014"
    s "H-how about a different pattern? It's just — kind of embarrassing…"

    voice "ch3.9_si_012"
    si "Why would it be embarrassing?"

    # [EVENT_CG +220] — кроссфейд CG
    $ dissolve_fx("id(220)", type="cg")

    voice "ch3.9_si_013"
    si "The same pattern would be — um, well — I know it's embarrassing, but… I like it."

    voice "ch3.9_s_015"
    s "If you like it, that's fine by me. I just wonder if I'm the right person for it…"

    voice "ch3.9_si_014"
    si "That's not true. …It's what I want."

    jump ch3_9_si_1068

label ch3_9_si_1068:
    # ==== SCENE 1068 ==== (RESET: [BGM +7]/[EVENT_CG +220] = текущее состояние
    # во всех трёх ветках)
    voice "ch3.9_s_016"
    s "Anyway — thanks for the scarf. Now I've got something to look forward to this winter."

    # [EVENT_CG +219] — кроссфейд CG
    $ dissolve_fx("id(219)", type="cg")

    voice "ch3.9_si_015"
    si "Really? Then I'll knit all sorts of things! Please accept them too!"

    voice "ch3.9_s_017"
    s "Okay — deal. I'll be looking forward to it."

    voice "ch3.9_si_016"
    si "Then I'll knit my heart out!"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay2/lay5 hide — не
    # показаны (всё действие на CG)][EVENT_CG hide][COFFEE → pause(1.0)]
    stop music fadeout 1.0
    pause(1.0)
    return

label date_tabitha_ch3_9:
    # ==== SCENE 1069 ====
    # [BG +26 (yard)][TRANS][BGM play=+9] → t8; [lay5 +423]
    $ fade_fx("yard", new_music="t8", sprites=("s 3",))

    voice "ch3.9_s_018"
    s "I wonder if Tabitha's around…"

    # [lay5 hide][BG hide][EVENT_CG +236][TRANS]
    # (fade покрывает удаление спрайтов и фона; CG без имени → заглушка id(236))
    $ fade_fx("id(236)", type="cg")

    voice "ch3.9_s_019"
    s "Ah — there she is. With her familiar Sylphid."

    voice "ch3.9_s_020"
    s "Tabitha really does seem to enjoy taking care of Sylphid…"

    voice "ch3.9_s_021"
    s "So this is what they mean by the ideal bond between a familiar and its master…"

    # без голоса: мысль сайта (канон без [voice])
    th "As for my own master, Louise…{#ch3.9_th_1069}"

    # [EVENT_CG +237] — кроссфейд CG
    $ dissolve_fx("id(237)", type="cg")

    voice "ch3.9_t_001"
    t "…You were here?"

    # [好感度] タバサ 30
    $ update_sympathy(30, char_key="tabitha")

    voice "ch3.9_s_022"
    s "Ah, Tabitha!? Sorry, sorry — I was just watching for a while."

    voice "ch3.9_t_002"
    t "Bad taste."

    voice "ch3.9_s_023"
    s "You and Sylphid looked like you were having such a good time, I hesitated to call out."

    # [EVENT_CG +236] — кроссфейд CG
    $ dissolve_fx("id(236)", type="cg")

    voice "ch3.9_t_003"
    t "You could tell?"

    voice "ch3.9_s_024"
    s "Tell what — that you two were having fun?"

    voice "ch3.9_t_004"
    t "Yeah.{#ch3.9_t_004}"

    voice "ch3.9_s_025"
    s "Well, yeah…"

    menu:

        "I'm a familiar too, y'know!{#ch3_m1069a}":
            jump ch3_9_t_1070

        "I can't explain it — I just know.{#ch3_m1069b}":
            jump ch3_9_t_1071

        "It's written on your face.{#ch3_m1069c}":
            jump ch3_9_t_1072

label ch3_9_t_1070:
    # ==== SCENE 1070 ==== (RESET: [BGM +9]/[EVENT_CG +236] = текущее состояние)
    voice "ch3.9_s_026"
    s "I'm a familiar too — of course I can tell."

    # [EVENT_CG +237] — кроссфейд CG
    $ dissolve_fx("id(237)", type="cg")

    voice "ch3.9_t_005"
    t "Random guess."

    voice "ch3.9_s_027"
    s "Ah — you saw through me…"

    # [EVENT_CG +236] — кроссфейд CG
    $ dissolve_fx("id(236)", type="cg")

    voice "ch3.9_s_028"
    s "But anyone could see that you and Sylphid get along great."

    jump ch3_9_t_1073

label ch3_9_t_1071:
    # ==== SCENE 1071 ==== (RESET: [BGM +9]/[EVENT_CG +236] = текущее состояние)
    voice "ch3.9_s_029"
    s "I can't explain it — I just know.{#ch3.9_s_029}"

    # [EVENT_CG +237] — кроссфейд CG
    $ dissolve_fx("id(237)", type="cg")

    voice "ch3.9_t_006"
    t "Weak grounds."

    # [好感度] タバサ -15
    $ update_sympathy(-15, char_key="tabitha")

    voice "ch3.9_s_030"
    s "Being told that just leaves me stumped."

    # [EVENT_CG +236] — кроссфейд CG
    $ dissolve_fx("id(236)", type="cg")

    voice "ch3.9_s_031"
    s "Still, watching you and Sylphid — I could tell you were having fun."

    jump ch3_9_t_1073

label ch3_9_t_1072:
    # ==== SCENE 1072 ==== (RESET: [BGM +9]/[EVENT_CG +236] = текущее состояние)
    voice "ch3.9_s_032"
    s "It's written on your face.{#ch3.9_s_032}"

    # [EVENT_CG +237] — кроссфейд CG
    $ dissolve_fx("id(237)", type="cg")

    voice "ch3.9_t_007"
    t "…Liar."

    # [好感度] タバサ 15
    $ update_sympathy(15, char_key="tabitha")

    voice "ch3.9_s_033"
    s "As if I were lying!"

    # [EVENT_CG +236] — кроссфейд CG
    $ dissolve_fx("id(236)", type="cg")

    voice "ch3.9_s_034"
    s "I was thinking — Sylphid is someone you can really let your guard down around."

    jump ch3_9_t_1073

label ch3_9_t_1073:
    # ==== SCENE 1073 ==== (RESET: [BGM +9]/[EVENT_CG +236] = текущее состояние
    # во всех трёх ветках)
    # [EVENT_CG +237] — кроссфейд CG
    $ dissolve_fx("id(237)", type="cg")

    voice "ch3.9_t_008"
    t "Still… peeking is wrong."

    voice "ch3.9_s_035"
    s "Sorry, sorry. I won't get in the way — can I just watch you two a bit longer?"

    # [EVENT_CG +236] — кроссфейд CG
    $ dissolve_fx("id(236)", type="cg")

    # без голоса: null-многоточие Табиты (канон без [voice])
    t "…{#ch3.9_t_v01}"

    voice "ch3.9_s_036"
    s "So — no good? Seeing Tabitha have fun puts me in a good mood too, y'know."

    # [EVENT_CG +237] — кроссфейд CG
    $ dissolve_fx("id(237)", type="cg")

    voice "ch3.9_t_009"
    t "…Alright."

    voice "ch3.9_s_037"
    s "Got it. Thanks."

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay5 hide — не
    # показан][LAYER lay0 hide — защитный сброс PS2 (Табита только в CG)]
    # [EVENT_CG hide][COFFEE → pause(1.0)]
    stop music fadeout 1.0
    pause(1.0)
    return

label date_kirche_ch3_9:
    # ==== SCENE 1074 ====
    # [BG +14 (hallway)][TRANS][BGM play=+8] → t7; [lay5 +390][SE se0 play=+82
    # — SE не портируется]
    $ fade_fx("hallway", new_music="t7", sprites=("s 1",))

    voice "ch3.9_s_038"
    s "Kirche — are you in?"

    # [SE se0 play=+57 — SE не портируется][lay5 hide][BG hide][BG +91 (room)]
    # [TRANS][lay6 +720 (k 5)]
    $ fade_fx("room", sprites=("k 5",))

    voice "ch3.9_k_001"
    k "Ah, Darling! You've come along at just the right moment."

    # [好感度] キュルケ 20
    $ update_sympathy(20, char_key="kirche")

    # [lay6 x=-96 — сдвиг не копируется][lay5 +390]
    $ show_sprites(("s 1", "k 5"))

    voice "ch3.9_s_039"
    s "Oh — you're not in uniform. Kirche out of uniform — it's a whole new look."

    # [lay6 +722 (k 5 happy)]
    $ show_sprites(("s 1", "k 5 happy"))

    voice "ch3.9_k_002"
    k "My, aren't you sweet. Complimenting a girl's clothes is step one of getting along with girls."

    # [lay6 +720 (k 5)]
    $ show_sprites(("s 1", "k 5"))

    voice "ch3.9_k_003"
    k "So — can you guess why I'm dressed like this?"

    # [lay5 +390 — повтор (s 1 уже показан)]

    voice "ch3.9_s_040"
    s "Why? Well, it's obviously…"

    menu:

        "Because you're an exhibitionist?{#ch3_m1074a}":
            jump ch3_9_k_1075

        "To let off steam?{#ch3_m1074b}":
            jump ch3_9_k_1076

        "Some wish to become someone else?{#ch3_m1074c}":
            jump ch3_9_k_1077

label ch3_9_k_1075:
    # ==== SCENE 1075 ==== (RESET: [lay5 +390][lay6 +720][BGM +8]/[BG +91
    # (room)] = текущее состояние)
    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("s 3 sad", "k 5"))

    voice "ch3.9_s_041"
    s "Because you're an exhibitionist?{#ch3.9_s_041}"

    # [lay6 +720 — повтор (k 5 уже показан)]
    voice "ch3.9_k_004"
    k "Exhibitionist — how rude. But, but — if my Darling wants it, I'll bare it all anytime."

    # [好感度] キュルケ -10
    $ update_sympathy(-10, char_key="kirche")

    # [lay5 +396 (s 1 sad)]
    $ show_sprites(("s 1 sad", "k 5"))

    voice "ch3.9_s_042"
    s "N-no, I'm good."

    # [lay6 +726 (k 5 sad)]
    $ show_sprites(("s 1 sad", "k 5 sad"))

    voice "ch3.9_k_005"
    k "Mm-oh, you're no fun~"

    # [lay6 +720 (k 5)]
    $ show_sprites(("s 1 sad", "k 5"))

    voice "ch3.9_k_006"
    k "The real answer: stress relief. Uniforms are stuffy, aren't they? The stress just piles up, you knoow…"

    jump ch3_9_k_1078

label ch3_9_k_1076:
    # ==== SCENE 1076 ==== (RESET: [lay5 +390][lay6 +720][BGM +8]/[BG +91
    # (room)] = текущее состояние)
    # [lay5 +392 (s 1 happy)]
    $ show_sprites(("s 1 happy", "k 5"))

    voice "ch3.9_s_043"
    s "To let off steam?{#ch3.9_s_043}"

    # [lay6 +722 (k 5 happy)]
    $ show_sprites(("s 1 happy", "k 5 happy"))

    voice "ch3.9_k_007"
    k "That's exactly it, Darling! The academy uniform is so tight — this body of mine just doesn't fit…"

    # [好感度] キュルケ 10
    $ update_sympathy(10, char_key="kirche")

    # [lay5 +390 (s 1)]
    $ show_sprites(("s 1", "k 5 happy"))

    voice "ch3.9_s_044"
    s "…Yeah, that does look tight."

    # [lay6 +720 (k 5)]
    $ show_sprites(("s 1", "k 5"))

    voice "ch3.9_k_008"
    k "And I have to wear it all the time — so the stress just builds and builds, you knoow…"

    jump ch3_9_k_1078

label ch3_9_k_1077:
    # ==== SCENE 1077 ==== (RESET: [lay5 +390][lay6 +720][BGM +8]/[BG +91
    # (room)] = текущее состояние)
    # [lay5 +423 (s 3)]
    $ show_sprites(("s 3", "k 5"))

    voice "ch3.9_s_045"
    s "Some wish to become someone else?{#ch3.9_s_045}"

    # [lay6 +726 (k 5 sad)]
    $ show_sprites(("s 3", "k 5 sad"))

    voice "ch3.9_k_009"
    k "Hmm~ Not wrong — but not right either?"

    # [lay5 +396 (s 1 sad)]
    $ show_sprites(("s 1 sad", "k 5 sad"))

    voice "ch3.9_s_046"
    s "Hmm… I give up."

    # [lay6 +720 (k 5)]
    $ show_sprites(("s 1 sad", "k 5"))

    voice "ch3.9_k_010"
    k "The real answer: stress relief. Uniforms are stuffy, aren't they? The stress just piles up, you knoow…{#ch3.9_k_010}"

    jump ch3_9_k_1078

label ch3_9_k_1078:
    # ==== SCENE 1078 ==== (RESET: [lay5 +396][lay6 +720][BGM +8]/[BG +91
    # (room)] = текущее состояние в ветках 1075/1077; ветка 1076 заканчивается
    # s 1 — показ s 1 sad на входе делает вход идентичным. [lay6 +720] повтор
    # в каноне — no-op)
    $ show_sprites(("s 1 sad", "k 5"))

    voice "ch3.9_k_011"
    k "So now and then I dress up in something else like this… Does Louise never do that?"

    # [lay5 +390 (s 1)]
    $ show_sprites(("s 1", "k 5"))

    voice "ch3.9_s_047"
    s "Louise? She's got plenty of clothes in her room."

    # [lay5 +396 (s 1 sad)]
    $ show_sprites(("s 1 sad", "k 5"))

    voice "ch3.9_s_048"
    s "At the academy, though, I mostly only see her in uniform or her nightgown."

    # [lay6 +726 (k 5 sad)]
    $ show_sprites(("s 1 sad", "k 5 sad"))

    voice "ch3.9_k_012"
    k "Sigh… I see. You have it tough too, Saito."

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("s 3 sad", "k 5 sad"))

    voice "ch3.9_s_049"
    s "R-really?{#ch3.9_s_049}"

    # [lay6 +722 (k 5 happy)]
    $ show_sprites(("s 3 sad", "k 5 happy"))

    voice "ch3.9_k_013"
    k "When you get tired of Louise, come to me right away — I'm waiting anytime!"

    # [lay5 +425 (s 3 happy)]
    $ show_sprites(("s 3 happy", "k 5 happy"))

    voice "ch3.9_s_050"
    s "Hah-hah-hah-hah…"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay5/lay6 hide][BG
    # hide][COFFEE → pause(1.0)]
    stop music fadeout 1.0
    pause(1.0)
    return

label date_haruna_ch3_9:
    # ==== SCENE 1079 ====
    # [BG +10 (louise_room)][TRANS][BGM play=+11] → t10; [lay5 +390]
    $ fade_fx("louise_room", new_music="t10", sprites=("s 1",))

    voice "ch3.9_s_051"
    s "Hey, Haruna — want to step out into the courtyard for a bit?"

    # [lay5 x=224 — сдвиг не копируется][lay7 +951 (ha 1)]
    $ show_sprites(("s 1", "ha 1"))

    voice "ch3.9_ha_001"
    ha "Sure, okay."

    voice "ch3.9_s_052"
    s "There's something I've been wanting to show you, Haruna."

    # [lay7 +953 (ha 1 happy)]
    $ show_sprites(("s 1", "ha 1 happy"))

    voice "ch3.9_ha_002"
    ha "Ooh, what is it? Now I'm excited~"

    # [好感度] ハルナ 20
    $ update_sympathy(20, char_key="haruna")

    # [BGM stop=1000][lay7 hide][lay5 hide][BG hide][EVENT_CG +270][TRANS]
    # [BGM play=+17] → t16 (fade покрывает удаление спрайтов и фона; CG без
    # имени → заглушка id(270))
    stop music fadeout 1.0
    $ fade_fx("id(270)", type="cg", new_music="t16")

    voice "ch3.9_s_053"
    s "This is what I wanted to show you, Haruna."

    voice "ch3.9_ha_003"
    ha "Is this… an airplane? It looks like a zero fighter… It's not the real thing, is it?"

    voice "ch3.9_s_054"
    s "It's real. This zero fighter came to this world from Japan."

    voice "ch3.9_ha_004"
    ha "It's real!? From Japan — all the way here?"

    voice "ch3.9_s_055"
    s "Yeah. It belongs to Siesta's great-grandfather — apparently he flew this zero fighter into this world."

    voice "ch3.9_ha_005"
    ha "So we're not the only ones who've come to this world…"

    voice "ch3.9_ha_006"
    ha "But I've never heard a story about anyone getting back…?"

    voice "ch3.9_s_056"
    s "That's…"

    menu:

        "That can't be helped.{#ch3_m1079a}":
            jump ch3_9_ha_1080

        "Maybe we just don't know.{#ch3_m1079b}":
            jump ch3_9_ha_1081

        "We'll be the first to return.{#ch3_m1079c}":
            jump ch3_9_ha_1082

label ch3_9_ha_1080:
    # ==== SCENE 1080 ==== (RESET: [BGM +17]/[EVENT_CG +270] = текущее состояние)
    voice "ch3.9_s_057"
    s "That can't be helped.{#ch3.9_s_057}"

    voice "ch3.9_ha_007"
    ha "Huh? Why not?"

    voice "ch3.9_s_058"
    s "If you return to your original world, you might lose any way to report success to this one — right? Put that way, it can't be helped."

    voice "ch3.9_ha_008"
    ha "Isn't that a bit too optimistic?"

    # [好感度] ハルナ -10
    $ update_sympathy(-10, char_key="haruna")

    voice "ch3.9_s_059"
    s "Still — beats just giving up, doesn't it?"

    jump ch3_9_ha_1083

label ch3_9_ha_1081:
    # ==== SCENE 1081 ==== (RESET: [BGM +17]/[EVENT_CG +270] = текущее состояние)
    voice "ch3.9_s_060"
    s "Maybe we just haven't heard about it yet?"

    voice "ch3.9_ha_009"
    ha "But we might not be able to get back."

    voice "ch3.9_s_061"
    s "That's why — if the chance comes, I want to see everything I can."

    jump ch3_9_ha_1083

label ch3_9_ha_1082:
    # ==== SCENE 1082 ==== (RESET: [BGM +17]/[EVENT_CG +270] = текущее состояние)
    voice "ch3.9_s_062"
    s "We just have to become the first ones to go back."

    voice "ch3.9_ha_010"
    ha "Yeah. That would be wonderful if we could… but could we?"

    # [好感度] ハルナ 10
    $ update_sympathy(10, char_key="haruna")

    voice "ch3.9_s_063"
    s "All sorts of things from our world seem to have drifted into this one."

    voice "ch3.9_s_064"
    s "Maybe someday we'll find something that helps us get home."

    jump ch3_9_ha_1083

label ch3_9_ha_1083:
    # ==== SCENE 1083 ==== (RESET: [BGM +17]/[EVENT_CG +270] = текущее состояние)
    voice "ch3.9_ha_011"
    ha "You're right. The chance of getting home isn't zero — so there's no need to give up yet…"

    voice "ch3.9_s_065"
    s "…Yeah. That's right.{#ch3.9_s_065}"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay7/lay5 hide — не
    # показаны (действие на CG)][EVENT_CG hide][COFFEE → pause(1.0)]
    stop music fadeout 1.0
    pause(1.0)
    return
