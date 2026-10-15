# Глава 3, часть 7 (сцены 193–206): преддверие дуэли и покаяние Харуны.
# Вход — 4× jump ch3_7 из меню сцены 192 (часть 6): три ответа Сайто (ветки
# 193/194/195) сходятся в хаб 196; Луиза с Кирхе уходят драться, Сайто
# остаётся с Харуной и Табитой (197), где всплывает притворство Харуны —
# меню 197 ведёт в ветки 198/199/200 (→ хаб 201), далее 202 (двор, меню
# «как извиниться» → ветки 203/204/205) и финальный хаб 206, меню которого
# уходит в часть 8 (jump ch3_8; сцена 207 и бой — часть 8).
# Источник: ps2_source/chapters/chapter_04_女の戦い.txt (SCENE 193–206).
# Точные аргументы: ps2_source/events_full/chapter_04_女の戦い.txt (SCENE 193–206).
# Голоса: ch3.7_s_001…051, ch3.7_ha_001…028, ch3.7_l_001…013,
#         ch3.7_si_001…009, ch3.7_t_001…009, ch3.7_k_001…002 (112).
# Без голоса (только текст): t×2 (теги ch3.7_t_v01/v02), мысль сайта ×1.
# Голосованные многоточия: ha×1 + si×1 (теги …_vNN).
# Сцена 206 заканчивается battleInit/battleAdd/battleEnemy("敵キュルケ")/
# battle — система боя не реализована, вызовы не портируются (сводка в отчёте).

label ch3_7_193:
    # ==== SCENE 193 ==== (RESET: [BGM +27]/[BG +10]/[lay5 +429] = текущее состояние)
    # [lay5 +396]
    $ show_sprites("s 1 sad")

    voice "ch3.7_s_001"
    s "But they won't listen to a word I say."

    # [lay5 x=224 — сдвиг не копируется][lay2 +493]
    $ show_sprites(("s 1 sad", "si 1 angry"))

    voice "ch3.7_si_001"
    si "You won't know unless you try, will you?!"

    # [lay5 +429]
    $ show_sprites(("s 3 sad", "si 1 angry"))

    voice "ch3.7_s_002"
    s "A-all right…"

    # [lay5 +394]
    $ show_sprites(("s 1 angry", "si 1 angry"))

    voice "ch3.7_s_003"
    s "Louise, call off this duel! What if you get hurt?"

    # [lay2 hide][lay1 +306]
    $ show_sprites(("s 1 angry", "l 1 angry"))

    voice "ch3.7_l_001"
    l "Hurt? You — my own familiar — think I'd lose?"

    # [lay5 +396]
    $ show_sprites(("s 1 sad", "l 1 angry"))

    voice "ch3.7_s_004"
    s "N-no, that's not what I meant…"

    voice "ch3.7_l_002"
    l "Anyway — do you even know what caused all this?"

    # [lay5 +429]
    $ show_sprites(("s 3 sad", "l 1 angry"))

    voice "ch3.7_s_005"
    s "Umm… the size of your breasts?"

    # [lay1 +339]
    $ show_sprites(("s 3 sad", "l 3 angry"))

    voice "ch3.7_l_003"
    l "You idiot! Just stay out of it, Saito!"

    # [好感度] ルイズ -10 (TNDL tndl(-30) не портируется)
    $ update_sympathy(-10, char_key="louise")

    # [lay5 +396]
    $ show_sprites(("s 1 sad", "l 3 angry"))

    voice "ch3.7_s_006"
    s "Y-yes, ma'am…"

    # [lay1 hide][lay2 +495]
    $ show_sprites(("s 1 sad", "si 1 sad"))

    voice "ch3.7_si_002"
    si "Saito, you dummy…"

    # [好感度] シエスタ -10
    $ update_sympathy(-10, char_key="siesta")

    # [lay5 +429]
    $ show_sprites(("s 3 sad", "si 1 sad"))

    voice "ch3.7_s_007"
    s "Ee-eh!?"

    # [lay2 hide][lay5 hide] → сцена 196 перестраивает состав
    jump ch3_7_196

label ch3_7_194:
    # ==== SCENE 194 ==== (RESET: [BGM +27]/[BG +10]/[lay5 +429] = текущее состояние)
    # [lay5 +390]
    $ show_sprites("s 1")

    voice "ch3.7_s_008"
    s "Girls shouldn't be dueling."

    # [lay5 x=224 — сдвиг не копируется][lay2 +491]
    $ show_sprites(("s 1", "si 1 happy"))

    voice "ch3.7_si_003"
    si "That's right! Duels are no good."

    # [好感度] シエスタ +10
    $ update_sympathy(10, char_key="siesta")

    # [lay5 +394]
    $ show_sprites(("s 1 angry", "si 1 happy"))

    voice "ch3.7_s_009"
    s "Louise, call off the duel! Nothing good can come of it, right?"

    # [lay2 hide][lay1 +306]
    $ show_sprites(("s 1 angry", "l 1 angry"))

    voice "ch3.7_l_004"
    l "Honestly, you… If we go back to the root of it all, everything…"

    # [好感度] ルイズ -10 (TNDL tndl(-30) не портируется)
    $ update_sympathy(-10, char_key="louise")

    # [lay1 +302]
    $ show_sprites(("s 1 angry", "l 1"))

    voice "ch3.7_l_005"
    l "…No. It's not just that."

    # [lay1 +339]
    $ show_sprites(("s 1 angry", "l 3 angry"))

    voice "ch3.7_l_006"
    l "Even before you came, Saito, I knew Kirche and I had to settle this once and for all. So be quiet."

    # [lay5 +429]
    $ show_sprites(("s 3 sad", "l 3 angry"))

    voice "ch3.7_s_010"
    s "…No good. So their feud ran that deep, huh."

    # [lay1 hide][lay5 hide] → сцена 196
    jump ch3_7_196

label ch3_7_195:
    # ==== SCENE 195 ==== (RESET: [BGM +27]/[BG +10]/[lay5 +429] = текущее состояние)
    # [lay5 +390]
    $ show_sprites("s 1")

    voice "ch3.7_s_011"
    s "Why not let them go until they're both satisfied?"

    # [lay5 x=224 — сдвиг не копируется][lay2 +528]
    $ show_sprites(("s 1", "si 4 sad"))

    voice "ch3.7_si_004"
    si "Saito-san, how can you…"

    # [好感度] シエスタ -10
    $ update_sympathy(-10, char_key="siesta")

    voice "ch3.7_s_012"
    s "If they don't go until they're satisfied, the bad blood never goes away, right?"

    # [lay2 +495]
    $ show_sprites(("s 1", "si 1 sad"))

    voice "ch3.7_si_005"
    si "But this is a duel between nobles. Someone could get seriously hurt…"

    # [lay5 +429]
    $ show_sprites(("s 3 sad", "si 1 sad"))

    voice "ch3.7_s_013"
    s "Hmm…"

    # [lay5 +390]
    $ show_sprites(("s 1", "si 1 sad"))

    voice "ch3.7_s_014"
    s "Hey, you two — maybe you should still call it off…"

    # [lay2 hide][lay1 +306]
    $ show_sprites(("s 1", "l 1 angry"))

    voice "ch3.7_l_007"
    l "Be quiet, Saito! We've already decided to fight!"

    # [lay5 +396]
    $ show_sprites(("s 1 sad", "l 1 angry"))

    voice "ch3.7_s_015"
    s "Well, that's that. No way I can stop them."

    # [lay1 hide][lay5 hide] → сцена 196
    jump ch3_7_196

label ch3_7_196:
    # ==== SCENE 196 ==== (RESET: [BGM +27]/[BG +10] = текущее состояние)
    # [lay1 +339][lay6 +676]
    $ show_sprites(("l 3 angry", "k 1"))

    voice "ch3.7_l_008"
    l "Say, Kirche — the peanut gallery's getting loud. Shall we take it outside?"

    voice "ch3.7_k_001"
    k "Sure. I'd feel bad tearing the room to shreds."

    # [lay1 +306]
    $ show_sprites(("l 1 angry", "k 1"))

    voice "ch3.7_l_009"
    l "Hmph! Say all you want while you still can!"

    # [SE se0 +57 дверь][lay1 hide][lay6 hide][SE se0 +56] — SE не портируется
    # [lay2 +493]
    $ show_sprites("si 1 angry")

    voice "ch3.7_si_006"
    si "Ah! Please wait, both of you—!"

    # [SE se0 +57][lay2 hide][SE se0 +56] — SE не портируется
    th "Siesta too…{#ch3.7_th_196}"

    # [SE se1 stop][BGM stop=1000] → fade сцены 197
    stop music fadeout 1.0

    jump ch3_7_197

label ch3_7_197:
    # ==== SCENE 197 ==== (TRANS crossfade, [BGM +28] → t27)
    $ fade_fx("louise_room", new_music="t27")
    # [lay7 +979]
    $ show_sprites("ha 3 sad")

    voice "ch3.7_ha_001"
    ha "Um, Hiraga-kun… They said they'd duel — is that okay?"

    # [lay7 x=-96 — сдвиг не копируется][lay5 +429]
    $ show_sprites(("ha 3 sad", "s 3 sad"))

    voice "ch3.7_s_016"
    s "No, it's not okay. How am I supposed to stop them…"

    # [lay5 +396]
    $ show_sprites(("ha 3 sad", "s 1 sad"))

    voice "ch3.7_s_017"
    s "Still — I can't believe those two are actually going to duel for real…"

    voice "ch3.7_s_018"
    s "They said they never got along before I came here — maybe it's all just piled up over time."

    voice "ch3.7_ha_002"
    ha "I-see…{#ch3.7_ha_002}"

    # [lay7 hide][lay0 +588] (Табита — LAYER lay0)
    $ show_sprites("t 1")

    voice "ch3.7_t_001"
    t "…No.{#ch3.7_t_001}"

    # [lay5 +390]
    $ show_sprites(("t 1", "s 1"))

    voice "ch3.7_s_019"
    s "Huh?{#ch3.7_s_019}"

    # [lay0 +621]
    $ show_sprites(("t 4", "s 1"))

    voice "ch3.7_t_002"
    t "It's all your fault."

    # [lay5 +429]
    $ show_sprites(("t 4", "s 3 sad"))

    voice "ch3.7_s_020"
    s "Huh? Why me!?"

    # [lay0 +588]
    $ show_sprites(("t 1", "s 3 sad"))

    t "…{#ch3.7_t_v01}"

    # [lay5 +396]
    $ show_sprites(("t 1", "s 1 sad"))

    voice "ch3.7_s_021"
    s "Say something—!"

    voice "ch3.7_t_003"
    t "And then…"

    # [lay5 hide][lay7 +973]
    $ show_sprites(("t 1", "ha 3"))

    voice "ch3.7_ha_003"
    ha "M-me?{#ch3.7_ha_003}"

    # [lay0 +621]
    $ show_sprites(("t 4", "ha 3"))

    voice "ch3.7_t_004"
    t "You… too stubborn for your own good."

    # [lay7 +979]
    $ show_sprites(("t 4", "ha 3 sad"))

    voice "ch3.7_ha_004"
    ha "…{#ch3.7_ha_v01}"

    # [lay7 hide][lay5 +429]
    $ show_sprites("s 3 sad")

    voice "ch3.7_s_022"
    s "Hey now, Tabitha — what do you mean Haruna's too stubborn?"

    # [lay0 +588]
    $ show_sprites(("t 1", "s 3 sad"))

    t "…{#ch3.7_t_v02}"

    # [lay0 hide][lay7 +973]
    $ show_sprites(("s 3 sad", "ha 3"))

    voice "ch3.7_ha_005"
    ha "Um, Hiraga-kun… There's something I have to apologize for."

    # [lay5 +396]
    $ show_sprites(("s 1 sad", "ha 3"))

    voice "ch3.7_s_023"
    s "What's this all of a sudden…"

    # [lay7 +979]
    $ show_sprites(("s 1 sad", "ha 3 sad"))

    voice "ch3.7_ha_006"
    ha "You've been taking care of me all this time… but the truth is, I wasn't really sick."

    # [lay5 +429]
    $ show_sprites(("s 3 sad", "ha 3 sad"))

    voice "ch3.7_s_024"
    s "Huh? You mean you faked it? …Really?"

    voice "ch3.7_ha_007"
    ha "Yes, really… Well, I did feel awful the first day…"

    voice "ch3.7_ha_008"
    ha "But the day after that, I got better so fast it was surprising…"

    voice "ch3.7_ha_009"
    ha "But you were so kind to me, Hiraga-kun… I guess I just let myself enjoy it…"

    # [lay5 +390]
    $ show_sprites(("s 1", "ha 3 sad"))

    voice "ch3.7_s_025"
    s "I see…{#ch3.7_s_025}"

    voice "ch3.7_ha_010"
    ha "I'm sorry, Hiraga-kun."

    menu:
        "Sorry — that's a bit of a shock…{#ch3_m197a}":
            # ==== SCENE 198 ==== (RESET: [BGM +28]/[BG +10] = текущее состояние)
            # [lay5 +396]
            $ show_sprites(("s 1 sad", "ha 3 sad"))

            voice "ch3.7_s_026"
            s "Sorry — that's a bit of a shock…"

            # [lay7 +979] (тот же кадр)
            voice "ch3.7_ha_011"
            ha "Hiraga-kun, I'm sorry…"

            # [lay5 +390]
            $ show_sprites(("s 1", "ha 3 sad"))

            voice "ch3.7_s_027"
            s "No, I'm at fault too for not noticing."

            voice "ch3.7_ha_012"
            ha "I'm truly sorry."

            # [好感度] ハルナ -10 (TNDL tndl(30) не портируется)
            $ update_sympathy(-10, char_key="haruna")

            jump ch3_7_201

        "I'm just glad you weren't really sick{#ch3_m197b}":
            # ==== SCENE 199 ==== (RESET: текущее состояние сохранено)
            # [lay5 +390] (тот же кадр)
            voice "ch3.7_s_028"
            s "Still — I'm really glad you weren't sick."

            # [lay7 +979] (тот же кадр)
            voice "ch3.7_ha_013"
            ha "…You're not angry?"

            voice "ch3.7_s_029"
            s "Hmm, a little. But I'm happier that you weren't really sick."

            # [lay5 +392]
            $ show_sprites(("s 1 happy", "ha 3 sad"))

            voice "ch3.7_s_030"
            s "In the end, no matter what, healthy beats sick any day."

            # [lay7 +981]
            $ show_sprites(("s 1 happy", "ha 3 shy"))

            voice "ch3.7_ha_014"
            ha "Hiraga-kun…{#ch3.7_ha_014}"

            # [好感度] ハルナ +10 (TNDL tndl(-30) не портируется)
            $ update_sympathy(10, char_key="haruna")

            jump ch3_7_201

        "You don't have to worry about me{#ch3_m197c}":
            # ==== SCENE 200 ==== (RESET: текущее состояние сохранено)
            # [lay5 +423]
            $ show_sprites(("s 3", "ha 3 sad"))

            voice "ch3.7_s_031"
            s "You don't have to worry about me."

            voice "ch3.7_s_032"
            s "It wasn't only because you were sick that I nursed you and looked after you."

            # [lay5 +390]
            $ show_sprites(("s 1", "ha 3 sad"))

            voice "ch3.7_s_033"
            s "You're not a stranger to me. I'd have looked after you even if you weren't sick."

            # [lay7 +981]
            $ show_sprites(("s 1", "ha 3 shy"))

            voice "ch3.7_ha_015"
            ha "Hiraga-kun…{#ch3.7_ha_015}"

            jump ch3_7_201

label ch3_7_201:
    # ==== SCENE 201 ==== (RESET: [BGM +28]/[BG +10]/[lay7 +979]/[lay5 +390] = текущее состояние)
    # [lay5 +396]
    $ show_sprites(("s 1 sad", "ha 3 sad"))

    voice "ch3.7_s_034"
    s "So then — could it be… Siesta made the room hot, and Kirche goaded Haruna, because…?"

    # [lay7 +979] (тот же кадр)
    voice "ch3.7_ha_016"
    ha "Probably to make me confess that I was faking it. But I was stubborn too…"

    # [lay5 +429]
    $ show_sprites(("s 3 sad", "ha 3 sad"))

    voice "ch3.7_s_035"
    s "I see… Then, like Tabitha said, it's my fault for not noticing the fake."

    # [lay7 +973]
    $ show_sprites(("s 3 sad", "ha 3"))

    voice "ch3.7_ha_017"
    ha "No, Hiraga-kun, it's not your fault. The one at fault is me — abusing your kindness while I faked being sick…"

    # [lay5 +390]
    $ show_sprites(("s 1", "ha 3"))

    voice "ch3.7_s_036"
    s "Hey, Tabitha — am I really the only one who didn't catch on to Haruna's act?"

    # [lay7 hide][lay0 +588]
    $ show_sprites(("s 1", "t 1"))

    voice "ch3.7_t_005"
    t "…Just you."

    # [lay5 +396]
    $ show_sprites(("s 1 sad", "t 1"))

    voice "ch3.7_s_037"
    s "So that's how it is…"

    # [lay0 +621]
    $ show_sprites(("s 1 sad", "t 4"))

    voice "ch3.7_t_006"
    t "Hurry."

    # [lay5 +394]
    $ show_sprites(("s 1 angry", "t 4"))

    voice "ch3.7_s_038"
    s "Hurry, as in… Oh, right! I have to go stop Louise's duel right now!!"

    # [SE se1 stop][BGM stop=1000] → fade сцены 202
    stop music fadeout 1.0

    jump ch3_7_202

label ch3_7_202:
    # ==== SCENE 202 ==== (TRANS crossfade, [BG +14] hallway, [BGM +26] → t25)
    $ fade_fx("hallway", new_music="t25")
    # [lay7 +957]
    $ show_sprites("ha 1 sad")

    voice "ch3.7_ha_018"
    ha "Say, it's fine to go stop Louise and the others — but do you know where they're fighting?"

    # [lay7 x=224 — сдвиг не копируется][lay0 +588]
    $ show_sprites(("ha 1 sad", "t 1"))

    voice "ch3.7_t_007"
    t "Probably the courtyard."

    # [lay7 hide][lay5 +429]
    $ show_sprites(("s 3 sad", "t 1"))

    voice "ch3.7_s_039"
    s "Probably… Now, how do we stop them?"

    # [lay0 +621]
    $ show_sprites(("s 3 sad", "t 4"))

    voice "ch3.7_t_008"
    t "It's fine. I'll stop the magic. You explain."

    # [lay5 +390]
    $ show_sprites(("s 1", "t 4"))

    voice "ch3.7_s_040"
    s "Got it.{#ch3.7_s_040}"

    # [lay0 hide][lay7 +951]
    $ show_sprites(("s 1", "ha 1"))

    voice "ch3.7_ha_019"
    ha "Um, Hiraga-kun."

    voice "ch3.7_s_041"
    s "What is it, Haruna?"

    # [lay7 +957]
    $ show_sprites(("s 1", "ha 1 sad"))

    voice "ch3.7_ha_020"
    ha "In the end, I caused trouble for Louise and Siesta… How should I apologize, do you think…"

    menu:
        "Why not just apologize honestly?{#ch3_m202a}":
            # ==== SCENE 203 ==== (RESET: [BGM +26]/[BG +14] = текущее состояние)
            # [lay5 +423]
            $ show_sprites(("s 3", "ha 1 sad"))

            voice "ch3.7_s_042"
            s "Why not just apologize honestly? You didn't mean any real harm, Haruna — I'm sure they'll understand."

            # [lay7 +951]
            $ show_sprites(("s 3", "ha 1"))

            voice "ch3.7_ha_021"
            ha "D-do you think so…"

            # [好感度] ハルナ +10
            $ update_sympathy(10, char_key="haruna")

            jump ch3_7_206

        "You don't have to apologize{#ch3_m202b}":
            # ==== SCENE 204 ==== (RESET: текущее состояние сохранено)
            # [lay5 +390]
            $ show_sprites(("s 1", "ha 1 sad"))

            voice "ch3.7_s_043"
            s "You don't have to apologize."

            # [lay7 +951]
            $ show_sprites(("s 1", "ha 1"))

            voice "ch3.7_ha_022"
            ha "Huh?{#ch3.7_ha_022}"

            # [lay5 +423]
            $ show_sprites(("s 3", "ha 1"))

            voice "ch3.7_s_044"
            s "It's not like you did anything that bad, right? Maybe you don't need to apologize."

            # [lay7 +957]
            $ show_sprites(("s 3", "ha 1 sad"))

            voice "ch3.7_ha_023"
            ha "No… I have to. I'll apologize honestly."

            # [好感度] ハルナ -10
            $ update_sympathy(-10, char_key="haruna")

            jump ch3_7_206

        "How about treating them to sweets sometime?{#ch3_m202c}":
            # ==== SCENE 205 ==== (RESET: текущее состояние сохранено)
            # [lay5 +392]
            $ show_sprites(("s 1 happy", "ha 1 sad"))

            voice "ch3.7_s_045"
            s "How about treating them to sweets sometime?"

            # [lay7 +957] (тот же кадр)
            voice "ch3.7_ha_024"
            ha "But… I don't have any money in this world…"

            # [lay5 +429]
            $ show_sprites(("s 3 sad", "ha 1 sad"))

            voice "ch3.7_s_046"
            s "Oh, right…"

            # [lay7 +951]
            $ show_sprites(("s 3 sad", "ha 1"))

            voice "ch3.7_ha_025"
            ha "Besides, I don't think that would make up for it. I'll apologize honestly."

            jump ch3_7_206

label ch3_7_206:
    # ==== SCENE 206 ==== (RESET: [lay7 +951]/[lay5 +423]/[BGM +26]/[BG +14] — старт веток 203/204/205)
    # [lay5 +390]
    $ show_sprites(("s 1", "ha 1"))

    voice "ch3.7_s_047"
    s "Well, you never know until you try."

    # [lay7 +951] (тот же кадр)
    voice "ch3.7_ha_026"
    ha "…Yeah."

    # [BGM stop=1000]; смена локации: [BG +14 → +26 yard], TRANS crossfade, [BGM +28] → t27
    stop music fadeout 1.0
    $ fade_fx("yard", new_music="t27")

    # [lay2 +493]
    $ show_sprites("si 1 angry")

    voice "ch3.7_si_007"
    si "Saito-san, you're late. Oh? Haruna — is that you? Is it okay for you to be here?"

    # [lay2 x=-96 — сдвиг не копируется][lay7 +957]
    $ show_sprites(("si 1 angry", "ha 1 sad"))

    voice "ch3.7_ha_027"
    ha "I'm sorry, Siesta. I was faking my illness. That's why I want to apologize to Louise too…"

    # [lay2 +495]
    $ show_sprites(("si 1 sad", "ha 1 sad"))

    voice "ch3.7_si_008"
    si "…{#ch3.7_si_v01}"

    # [lay7 hide][lay5 +390]
    $ show_sprites(("si 1 sad", "s 1"))

    voice "ch3.7_s_048"
    s "Siesta. I'm sorry too. So — can you forgive her?"

    # [lay2 +489]
    $ show_sprites(("si 1", "s 1"))

    voice "ch3.7_si_009"
    si "No, I should be the one apologizing for being mean."

    # [lay5 hide][lay7 +957]
    $ show_sprites(("si 1", "ha 1 sad"))

    voice "ch3.7_ha_028"
    ha "Siesta…{#ch3.7_ha_028}"

    # [lay2 hide][lay7 hide][lay1 +306]
    $ show_sprites("l 1 angry")

    voice "ch3.7_l_010"
    l "…Oh, Saito!? You're late! What have you been doing!!"

    # [lay1 x=-96 — сдвиг не копируется][lay5 +394]
    $ show_sprites(("l 1 angry", "s 1 angry"))

    voice "ch3.7_s_049"
    s "What do you mean, wh—… I came to stop Kirche and your duel… And Haruna wanted to apologize…"

    # [lay1 +339]
    $ show_sprites(("l 3 angry", "s 1 angry"))

    voice "ch3.7_l_011"
    l "Haruna can wait. Right now, I have to fight Kirche!"

    # [lay5 +396]
    $ show_sprites(("l 3 angry", "s 1 sad"))

    voice "ch3.7_s_050"
    s "That's insane."

    # [lay1 hide][lay5 hide][lay0 +588]
    $ show_sprites("t 1")

    voice "ch3.7_t_009"
    t "Too late."

    # [lay0 hide][lay1 +339][lay5 +396]
    $ show_sprites(("l 3 angry", "s 1 sad"))

    voice "ch3.7_l_012"
    l "Besides — if I, your master, am dueling, then my familiar Saito has to join in. That's an order!"

    # [lay5 +394]
    $ show_sprites(("l 3 angry", "s 1 angry"))

    voice "ch3.7_s_051"
    s "You've gotta be kidding!"

    # [lay1 +306]
    $ show_sprites(("l 1 angry", "s 1 angry"))

    voice "ch3.7_l_013"
    l "…That's fine by you, Kirche?"

    # [lay5 hide][lay6 +709]
    $ show_sprites(("l 1 angry", "k 4"))

    voice "ch3.7_k_002"
    k "Sure~ I'll even give you a handicap. Come at me with everything you've got!"

    # [SE se1 stop][BGM stop=1000]; battleInit((BG +26))/battleAdd(サイト)/battleAdd(ルイズ)/
    # battleEnemy("中", "敵キュルケ", image +746)/battle() — система боя не реализована,
    # вызовы не портируются (сводка в отчёте части); сцена 207 — часть 8.
    stop music fadeout 1.0

    jump ch3_8
