# Глава 3, часть 3 (сцены 1297–1321): карта выбора локации — пять веток:
# коридор вниз к Луизе (1297–1301), коридор с Сиестой (1302–1306),
# класс с Кирхе (1307–1311), двор с Табитой (1312–1316),
# комната Луизы с Харуной (1317–1321). Каждая локация помечает ключ
# в ch3_2_visited и делает return → карта (ch3_2_map в script-ch3_2.rpy).
# Источник: ps2_source/chapters/chapter_04_女の戦い.txt (SCENE 1297–1321).
# Точные аргументы: ps2_source/events_full/chapter_04_女の戦い.txt (SCENE 1297–1321).
# Голоса: ch3.3_s_001…082, ch3.3_l_001…009, ch3.3_si_001…014,
#         ch3.3_k_001…016, ch3.3_t_001…003, ch3.3_ha_001…008.
# Без голоса (только текст): k×1, t×4, ha×7 (теги …_v01), мысли сайта ×4.

label hallway_ch3_3:
    # ==== SCENE 1297 ====
    # [BG stage image=+17] hallway_down, [BGM play=+6] → t5
    $ fade_fx("hallway_down", new_music="t5")
    $ show_sprites("s 1")

    voice "ch3.3_s_001"
    s "Even so, that Louise— she could've at least said something before leaving… Hm?"

    # [lay5 hide][lay1 +302] → l 1
    $ show_sprites("l 1")

    voice "ch3.3_s_002"
    s "Ah, there she is. Louise."

    # [lay1 +306]
    $ show_sprites("l 1 angry")

    voice "ch3.3_l_001"
    l "…Ah!?"

    # [好感度] ルイズ +20
    $ update_sympathy(20, char_key="louise")

    voice "ch3.3_s_003"
    s "Hey, Louiise!"

    # [lay1 hide]
    $ show_sprites("s 1")

    voice "ch3.3_s_004"
    s "Why're you running!? Geez — don't make me chase you…"

    # [BG stage image=+14] hallway: [lay5 hide][BG hide] → смена фона, затем [lay1 +306]
    $ fade_fx("hallway")
    $ show_sprites("l 1 angry")

    voice "ch3.3_l_002"
    l "Aaugh, honestly! Don't follow me on purpose!"

    # [lay1 x=-96][lay5 +394]
    $ show_sprites(("l 1 angry", "s 1 angry"))

    voice "ch3.3_s_005"
    s "If you run off the second you see me, naturally I'm going to get curious and chase you!"

    voice "ch3.3_l_003"
    l "I ran because I didn't want you to follow! You're my familiar, Saito — take a hint!!"

    # [lay5 +429]
    $ show_sprites(("l 1 angry", "s 3 sad"))

    voice "ch3.3_s_006"
    s "So that's why I— …Oh. Could it be…"

    # ==== CHOICE (scene 1297) ====
    # select: 1298 / 1299 / 1300 → все ветки сходятся в ch3_1301
    menu:
        "Did I do something?{#ch3_m1297a}":
            # ==== SCENE 1298 ====
            # RESET: фон/музыка/спрайты не меняются
            voice "ch3.3_s_007"
            s "Did I do something? I don't think I've done anything to make Louise mad…"

            voice "ch3.3_l_004"
            l "I don't care about that — I'm telling you not to follow me right now! Got it?"

            # [好感度] ルイズ -10; tndl(-30) — не портируется (система не реализована)
            $ update_sympathy(-10, char_key="louise")

            # [lay5 +396]
            $ show_sprites(("l 1 angry", "s 1 sad"))

            voice "ch3.3_s_008"
            s "I get it, I get it. Just don't be so mad…"

            # [lay1 +339]
            $ show_sprites(("l 3 angry", "s 1 sad"))

            voice "ch3.3_l_005"
            l "If you follow me… I'll really get mad at you, okay!!"

            jump ch3_1301

        "Am I in the way?{#ch3_m1297b}":
            # ==== SCENE 1299 ====
            # RESET: фон/музыка/спрайты не меняются
            voice "ch3.3_s_009"
            s "Am I in the way?"

            # [lay1 +308]
            $ show_sprites(("l 1 sad", "s 3 sad"))

            voice "ch3.3_l_006"
            l "I-I'm not saying you're in the way or anything…"

            # [lay5 +396]
            $ show_sprites(("l 1 sad", "s 1 sad"))

            voice "ch3.3_s_010"
            s "Okay, okay. So where are you headed?"

            # [lay1 +339]
            $ show_sprites(("l 3 angry", "s 1 sad"))

            voice "ch3.3_l_007"
            l "You're not getting it at all! I told you not to come, so don't follow me!"

            jump ch3_1301

        "Are you going to take a bath?{#ch3_m1297c}":
            # ==== SCENE 1300 ====
            # RESET: фон/музыка/спрайты не меняются
            # [lay5 +425]
            $ show_sprites(("l 1 angry", "s 3 happy"))

            voice "ch3.3_s_011"
            s "Are you going to take a bath?"

            # [lay1 +302]
            $ show_sprites(("l 1", "s 3 happy"))

            voice "ch3.3_l_008"
            l "Y-yes, I am… It's hot today, after all. …Wh-what's with that look?"

            # [lay5 +396]
            $ show_sprites(("l 1", "s 1 sad"))

            voice "ch3.3_s_012"
            s "Really?{#ch3.3_s_012}"

            # [lay1 +339]
            $ show_sprites(("l 3 angry", "s 1 sad"))

            voice "ch3.3_l_009"
            l "That doesn't matter! Just don't follow me for now! See you!"

            jump ch3_1301

label ch3_1301:
    # ==== SCENE 1301 ====
    # RESET: фон/музыка/спрайты не меняются (все ветки приходят в (l 3 angry, s 1 sad))
    # [lay1 hide]
    $ show_sprites("s 1 sad")

    voice "ch3.3_s_013"
    s "Well, shoot… Did I do something to Louise…"

    # [BGM stop=1000], спрайты/фон скрываются → карта
    stop music fadeout 1.0
    $ ch3_2_visited.add("hallway")
    return

label siesta_hallway_ch3_3:
    # ==== SCENE 1302 ====
    # [BG stage image=+14] hallway, [BGM play=+7] → t6
    $ fade_fx("hallway", new_music="t6")
    $ show_sprites("s 1")

    voice "ch3.3_s_014"
    s "Where on earth did Louise run off to…"

    voice "ch3.3_s_015"
    s "…Hm? Isn't that Siesta? Looks like she's hauling a huge load…"

    # [lay5 +392]
    $ show_sprites("s 1 happy")

    voice "ch3.3_s_016"
    s "Hey, Siestaaa!"

    # [lay5 hide][BG hide][EVENT_CG +217] → CG «Сиеста с ношей»
    $ show_sprites(None)
    $ fade_fx("id(217)", type="cg")

    voice "ch3.3_si_001"
    si "…!? S-Saito-san!!"

    # [好感度] シエスタ +20
    $ update_sympathy(20, char_key="siesta")

    voice "ch3.3_s_017"
    s "That load looks brutal to carry. Want a hand?"

    # [EVENT_CG +218]
    $ dissolve_fx("id(218)", type="cg")

    voice "ch3.3_si_002"
    si "Um, well, you see…"

    voice "ch3.3_s_018"
    s "What's wrong? You don't have to hold back."

    # [EVENT_CG +217]
    $ dissolve_fx("id(217)", type="cg")

    voice "ch3.3_si_003"
    si "No, I'm fine…"

    voice "ch3.3_s_019"
    s "Huh? Why? Oh — could it be…"

    # ==== CHOICE (scene 1302) ====
    # select: 1303 / 1304 / 1305 → все ветки сходятся в ch3_1306
    menu:
        "Luggage I'm not allowed to touch?{#ch3_m1302a}":
            # ==== SCENE 1303 ====
            # RESET: музыка/CG не меняются
            voice "ch3.3_s_020"
            s "Luggage I'm not allowed to touch?"

            voice "ch3.3_si_004"
            si "N-no, that's not it at all~"

            voice "ch3.3_s_021"
            s "Then I'll…"

            # [BGM stop=1000], пауза, [EVENT_CG +218] (crossfade), [BGM play=+30] → t29
            stop music fadeout 1.0
            $ dissolve_fx("id(218)", type="cg")
            play music t29

            voice "ch3.3_si_005"
            si "N-no! I said no — stooop!?"

            # [好感度] シエスタ -10
            $ update_sympathy(-10, char_key="siesta")

            voice "ch3.3_s_022"
            s "W-wait, Siesta… W-what's wrong?"

            voice "ch3.3_si_006"
            si "Please be quiet and trust me for now — I'd never do anything to hurt you, Saito-san."

            jump ch3_1306

        "Did I do something to offend you?{#ch3_m1302b}":
            # ==== SCENE 1304 ====
            # RESET: музыка/CG не меняются
            voice "ch3.3_s_023"
            s "Did I do something to offend you?"

            # [EVENT_CG +218]
            $ dissolve_fx("id(218)", type="cg")

            voice "ch3.3_si_007"
            si "N-no, I haven't! Not at all!"

            # [好感度] シエスタ +10
            $ update_sympathy(10, char_key="siesta")

            voice "ch3.3_s_024"
            s "Then I'll carry the luggage…"

            voice "ch3.3_si_008"
            si "T-that's exactly why you can't! It's work I was asked to do…"

            voice "ch3.3_si_009"
            si "If they found out I let Saito-san help, I'd get scolded."

            voice "ch3.3_s_025"
            s "I-see…"

            jump ch3_1306

        "Are you working out or something?{#ch3_m1302c}":
            # ==== SCENE 1305 ====
            # RESET: музыка/CG не меняются
            voice "ch3.3_s_026"
            s "Are you working out or something?"

            voice "ch3.3_si_010"
            si "Well, in a way… A maid's job comes down to stamina, so this is how I keep in shape, day after day…"

            voice "ch3.3_s_027"
            s "You're kidding."

            # [EVENT_CG +218]
            $ dissolve_fx("id(218)", type="cg")

            voice "ch3.3_si_011"
            si "Yes.{#ch3.3_si_011}"

            voice "ch3.3_s_028"
            s "I don't know what you're so shy about, but I'm going to help you."

            voice "ch3.3_si_012"
            si "Um, Saito-san — I really don't need any help…"

            jump ch3_1306

label ch3_1306:
    # ==== SCENE 1306 ====
    # [BGM play=+30] → t29 (ветка a: уже играет — канонический перезапуск;
    # ветки b/c: смена t6 → t29), [EVENT_CG +218] уже показан во всех ветках
    play music t29 fadein 1.0

    voice "ch3.3_si_013"
    si "A-anyway! A load this size is nothing for me alone!"

    voice "ch3.3_s_029"
    s "If Siesta insists that much, I won't do anything…"

    voice "ch3.3_si_014"
    si "Well then, I'll be going, Saito-san."

    voice "ch3.3_s_030"
    s "Ah, right…"

    # [EVENT_CG hide][BG stage image=+14] hallway → смена CG на фон
    $ fade_fx("hallway")
    $ show_sprites("s 1 sad")

    voice "ch3.3_s_031"
    s "Whatever she says, she's still wobbling… I hope she's really okay…"

    # [BGM stop=1000], спрайты/фон скрываются → карта
    stop music fadeout 1.0
    $ ch3_2_visited.add("siesta_hallway")
    return

label classroom_ch3_3:
    # ==== SCENE 1307 ====
    # [BG stage image=+23] classroom, [BGM play=+8] → t7
    $ fade_fx("classroom", new_music="t7")
    $ show_sprites("s 1")

    voice "ch3.3_s_032"
    s "Now then, what should I do…{#ch3.3_s_032}"

    # [lay5 x=224][lay6 +676] → k 1
    $ show_sprites(("k 1", "s 1"))

    voice "ch3.3_k_001"
    k "My, Darling. All alone right now?"

    # [好感度] キュルケ +20
    $ update_sympathy(20, char_key="kirche")

    voice "ch3.3_s_033"
    s "Ah, Kirche… Louise up and vanished the moment class ended…"

    # [lay6 +678]
    $ show_sprites(("k 1 happy", "s 1"))

    voice "ch3.3_k_002"
    k "I see, I see. …So that means my Darling's free right now, doesn't it?"

    # [lay5 +423]
    $ show_sprites(("k 1 happy", "s 3"))

    voice "ch3.3_s_034"
    s "Well, I guess so."

    # [lay6 +709]
    $ show_sprites(("k 4", "s 3"))

    voice "ch3.3_k_003"
    k "Then here's a perfect chance — come with me… Mm?"

    # [lay5 +390]
    $ show_sprites(("k 4", "s 1"))

    voice "ch3.3_s_035"
    s "What's wrong, Kirche? Staring at my face out of nowhere…"

    # [lay6 +676]
    $ show_sprites(("k 1", "s 1"))

    voice "ch3.3_k_004"
    k "Wait. Would you let me read your fortune, Darling?"

    # [lay5 +429]
    $ show_sprites(("k 1", "s 3 sad"))

    voice "ch3.3_s_036"
    s "Ah, sure… I don't mind…"

    k "…{#ch3.3_k_v01}"

    # [lay6 +682]
    $ show_sprites(("k 1 sad", "s 3 sad"))

    voice "ch3.3_k_005"
    k "…I see it. …Listen, Saito — you've got the sign of woman-trouble."

    # [lay5 +396]
    $ show_sprites(("k 1 sad", "s 1 sad"))

    voice "ch3.3_s_037"
    s "A sign of woman-trouble? That can't happen to me… …Or can it…"

    # [lay6 +715]
    $ show_sprites(("k 4 sad", "s 1 sad"))

    voice "ch3.3_k_006"
    k "Hmm… maybe it's even worse than usual?"

    # [lay5 +394]
    $ show_sprites(("k 4 sad", "s 1 angry"))

    voice "ch3.3_s_038"
    s "Huh, seriously? Worse than usual — what's that mean?"

    # [lay6 +676]
    $ show_sprites(("k 1", "s 1 angry"))

    voice "ch3.3_k_007"
    k "I don't know the details either. But shouldn't you be careful around the girls here?"

    voice "ch3.3_k_008"
    k "There must be one girl who's the cause. Any idea who, Darling?"

    # [lay5 +429]
    $ show_sprites(("k 1", "s 3 sad"))

    voice "ch3.3_s_039"
    s "Someone I suspect, huh… Let me think…"

    # ==== CHOICE (scene 1307) ====
    # select: 1308 / 1309 / 1310 → все ветки сходятся в ch3_1311
    menu:
        "Louise, one way or another?{#ch3_m1307a}":
            # ==== SCENE 1308 ====
            # RESET: фон/музыка/спрайты не меняются
            # [lay5 +390]
            $ show_sprites(("k 1", "s 1"))

            voice "ch3.3_s_040"
            s "Louise, one way or another?"

            # [lay6 +711]
            $ show_sprites(("k 4 happy", "s 1"))

            voice "ch3.3_k_009"
            k "My, so Darling thought so too."

            # [好感度] キュルケ +10; tndl(-30) — не портируется (система не реализована)
            $ update_sympathy(10, char_key="kirche")

            # [lay5 +396]
            $ show_sprites(("k 4 happy", "s 1 sad"))

            voice "ch3.3_s_041"
            s "Well, I'm always getting punished as the 'stupid dog' and all…"

            # [lay5 +429]
            $ show_sprites(("k 4 happy", "s 3 sad"))

            voice "ch3.3_s_042"
            s "I wonder what punishment would be worse than that…"

            # [lay5 +396]
            $ show_sprites(("k 4 happy", "s 1 sad"))

            voice "ch3.3_s_043"
            s "Brrr… I'm starting to get scared."

            jump ch3_1311

        "Siesta directly?{#ch3_m1307b}":
            # ==== SCENE 1309 ====
            # RESET: фон/музыка/спрайты не меняются
            # [lay5 +390]
            $ show_sprites(("k 1", "s 1"))

            voice "ch3.3_s_044"
            s "Siesta directly?"

            # [lay6 +715]
            $ show_sprites(("k 4 sad", "s 1"))

            voice "ch3.3_k_010"
            k "My, how unexpected… What about the maid?"

            # [lay5 +423]
            $ show_sprites(("k 4 sad", "s 3"))

            voice "ch3.3_s_045"
            s "No, it's not like I think Siesta's done anything wrong or anything."

            # [lay5 +396]
            $ show_sprites(("k 4 sad", "s 1 sad"))

            voice "ch3.3_s_046"
            s "It's just — when Louise and Siesta are in the same room, I don't know, I get all uneasy."

            # [lay6 +676]
            $ show_sprites(("k 1", "s 1 sad"))

            voice "ch3.3_k_011"
            k "Of course you'd be uneasy. In all sorts of ways…"

            # [lay5 +390]
            $ show_sprites(("k 1", "s 1"))

            voice "ch3.3_s_047"
            s "Hm? Did you say something?{#ch3.3_s_047}"

            # [lay6 +711]
            $ show_sprites(("k 4 happy", "s 1"))

            voice "ch3.3_k_012"
            k "Mm-mm, nothing at all."

            jump ch3_1311

        "Kirche, by any chance?{#ch3_m1307c}":
            # ==== SCENE 1310 ====
            # RESET: фон/музыка/спрайты не меняются
            # [lay5 +390]
            $ show_sprites(("k 1", "s 1"))

            voice "ch3.3_s_048"
            s "Kirche, by any chance?"

            # [lay6 +680]
            $ show_sprites(("k 1 angry", "s 1"))

            voice "ch3.3_k_013"
            k "Why would I be the cause? Darling or not, I'll get mad, you know?"

            # [好感度] キュルケ -10; tndl(+30) — не портируется (система не реализована)
            $ update_sympathy(-10, char_key="kirche")

            # [lay5 +423]
            $ show_sprites(("k 1 angry", "s 3"))

            voice "ch3.3_s_049"
            s "Just kidding, just kidding."

            # [lay6 +717]
            $ show_sprites(("k 4 shy", "s 3"))

            voice "ch3.3_k_014"
            k "Say things like that and you'll bring on woman-trouble that's no joke."

            # [lay5 +396]
            $ show_sprites(("k 4 shy", "s 1 sad"))

            voice "ch3.3_s_050"
            s "No, that would be bad… Maybe."

            jump ch3_1311

label ch3_1311:
    # ==== SCENE 1311 ====
    # RESET: (lay5 +396)[lay6 +711] — расхождение веток, показываем явно
    $ show_sprites(("k 4 happy", "s 1 sad"))

    # [lay6 +709]
    $ show_sprites(("k 4", "s 1 sad"))

    voice "ch3.3_k_015"
    k "An-y-way! Whoever the cause is, you'd better watch out for woman-trouble, okay?"

    voice "ch3.3_s_051"
    s "Is that really so?"

    # [lay6 +676]
    $ show_sprites(("k 1", "s 1 sad"))

    voice "ch3.3_k_016"
    k "I can tell even without a proper reading — this could be pretty bad."

    # [lay5 +429]
    $ show_sprites(("k 1", "s 3 sad"))

    voice "ch3.3_s_052"
    s "Yeah, I'll be careful…"

    th "But how am I supposed to be careful…"

    # [BGM stop=1000], спрайты/фон скрываются → карта
    stop music fadeout 1.0
    $ ch3_2_visited.add("classroom")
    return

label courtyard_ch3_3:
    # ==== SCENE 1312 ====
    # [BG stage image=+26] yard, [BGM play=+9] → t8
    $ fade_fx("yard", new_music="t8")

    voice "ch3.3_s_053"
    s "I stepped out into the courtyard, but… No sign of Louise."

    voice "ch3.3_s_054"
    s "…Hm? Is that Tabitha over there?"

    # [LAYER lay0 +588] → t 1
    $ show_sprites("t 1")

    t "…{#ch3.3_t_v01}"

    # [好感度] タバサ +30
    $ update_sympathy(30, char_key="tabitha")

    # [lay0 x=-96][lay5 +392]
    $ show_sprites(("t 1", "s 1 happy"))

    voice "ch3.3_s_055"
    s "H-hi…"

    t "…{#ch3.3_t_v02}"

    # [lay5 +396]
    $ show_sprites(("t 1", "s 1 sad"))

    th "No reaction, huh… — right, no time to chicken out."

    # [lay5 +390]
    $ show_sprites(("t 1", "s 1"))

    voice "ch3.3_s_056"
    s "If you know, I'd like to hear it… Have you seen Louise around here?"

    # [lay0 +621]
    $ show_sprites(("t 4", "s 1"))

    t "…{#ch3.3_t_v03}"

    # [lay5 +429]
    $ show_sprites(("t 4", "s 3 sad"))

    voice "ch3.3_s_057"
    s "Um, Tabitha-san? Could it be…"

    # ==== CHOICE (scene 1312) ====
    # select: 1313 / 1314 / 1315 → все ветки сходятся в ch3_1316
    menu:
        "Do you hate me?{#ch3_m1312a}":
            # ==== SCENE 1313 ====
            # RESET: фон/музыка/спрайты не меняются
            voice "ch3.3_s_058"
            s "Do you hate me?"

            # [lay0 +588]
            $ show_sprites(("t 1", "s 3 sad"))

            t "…{#ch3.3_t_v04}"

            # [好感度] タバサ +15; tndl(-30) — не портируется (система не реализована)
            $ update_sympathy(15, char_key="tabitha")

            jump ch3_1316

        "Have you really not seen Louise?{#ch3_m1312b}":
            # ==== SCENE 1314 ====
            # RESET: фон/музыка/спрайты не меняются
            # [lay5 +396]
            $ show_sprites(("t 4", "s 1 sad"))

            voice "ch3.3_s_059"
            s "Have you really not seen Louise?"

            # [lay0 +592]
            $ show_sprites(("t 1 angry", "s 1 sad"))

            voice "ch3.3_t_001"
            t "…Nope."

            # [好感度] タバサ -15; tndl(+30) — не портируется (система не реализована)
            $ update_sympathy(-15, char_key="tabitha")

            # [lay5 +429]
            $ show_sprites(("t 1 angry", "s 3 sad"))

            voice "ch3.3_s_060"
            s "I-I see…"

            jump ch3_1316

        "Are you busy reading?{#ch3_m1312c}":
            # ==== SCENE 1315 ====
            # RESET: фон/музыка/спрайты не меняются
            # [lay5 +396]
            $ show_sprites(("t 4", "s 1 sad"))

            voice "ch3.3_s_061"
            s "Are you busy reading?"

            voice "ch3.3_t_002"
            t "…Very."

            # [lay5 +429]
            $ show_sprites(("t 4", "s 3 sad"))

            voice "ch3.3_s_062"
            s "I see. My apologies, then."

            jump ch3_1316

label ch3_1316:
    # ==== SCENE 1316 ====
    # RESET: (lay5 +429)[lay0 +588] — расхождение веток, показываем явно
    $ show_sprites(("t 1", "s 3 sad"))

    # [lay5 +390]
    $ show_sprites(("t 1", "s 1"))

    voice "ch3.3_s_063"
    s "Well then, I'd better not interrupt your reading — I'll be going."

    voice "ch3.3_t_003"
    t "…Louise isn't here."

    # [lay0 hide][lay5 +423]
    $ show_sprites("s 3")

    voice "ch3.3_s_064"
    s "R-right? Thanks for telling me."

    # [lay5 +396]
    $ show_sprites("s 1 sad")

    th "Tabitha seems kind of upset — did I say something to tick her off?"

    # [BGM stop=1000], спрайты/фон скрываются → карта
    stop music fadeout 1.0
    $ ch3_2_visited.add("courtyard")
    return

label l_room_ch3_3:
    # ==== SCENE 1317 ====
    # [BG stage image=+10] louise_room, [BGM play=+11] → t10
    $ fade_fx("louise_room", new_music="t10")
    $ show_sprites("s 1 sad")

    voice "ch3.3_s_065"
    s "Back here again… She's not back, after all."

    # [lay5 x=224][lay7 +975] → ha 3 happy
    $ show_sprites(("ha 3 happy", "s 1 sad"))

    voice "ch3.3_ha_001"
    ha "Ah, Hiraga-kun!"

    # [好感度] ハルナ +20
    $ update_sympathy(20, char_key="haruna")

    # [lay5 +390]
    $ show_sprites(("ha 3 happy", "s 1"))

    voice "ch3.3_s_066"
    s "Sorry, Haruna. Seems I woke you while you were sleeping."

    # [lay7 +973]
    $ show_sprites(("ha 3", "s 1"))

    voice "ch3.3_ha_002"
    ha "No, it's fine. I was thinking I might be okay without sleeping soon anyway."

    # [lay5 +396]
    $ show_sprites(("ha 3", "s 1 sad"))

    voice "ch3.3_s_067"
    s "No way. You have to sleep properly until you're better."

    # [lay7 +979]
    $ show_sprites(("ha 3 sad", "s 1 sad"))

    voice "ch3.3_ha_003"
    ha "But…{#ch3.3_ha_003}"

    # [lay5 +390]
    $ show_sprites(("ha 3 sad", "s 1"))

    voice "ch3.3_s_068"
    s "In this world, you can't just go to the hospital, take some medicine, and call it done."

    voice "ch3.3_ha_004"
    ha "R-right…{#ch3.3_ha_004}"

    # [lay5 +429]
    $ show_sprites(("ha 3 sad", "s 3 sad"))

    voice "ch3.3_s_069"
    s "I once got seriously hurt in a duel."

    # [lay7 +973]
    $ show_sprites(("ha 3", "s 3 sad"))

    voice "ch3.3_ha_005"
    ha "Eh — Hiraga-kun is the type to fight duels… I'm a little… surprised…"

    # [lay5 +390]
    $ show_sprites(("ha 3", "s 1"))

    voice "ch3.3_s_070"
    s "Well, I'll keep my opponent's name a secret for their honor — but I won the duel, though I took a real beating."

    voice "ch3.3_s_071"
    s "Back then I had Louise buy me a secret potion for a healing spell — I caused her a ton of trouble."

    # [lay7 +979][lay5 +429]
    $ show_sprites(("ha 3 sad", "s 3 sad"))

    voice "ch3.3_s_072"
    s "And that secret potion turned out to be incredibly expensive…"

    ha "…{#ch3.3_ha_v01}"

    # [lay5 +390]
    $ show_sprites(("ha 3 sad", "s 1"))

    voice "ch3.3_s_073"
    s "Hm? What's wrong, Haruna?"

    voice "ch3.3_ha_006"
    ha "…No, it's nothing. It's nothing, but…"

    # [lay5 +429]
    $ show_sprites(("ha 3 sad", "s 3 sad"))

    voice "ch3.3_s_074"
    s "Could it be… Is there something you want to say to me?"

    voice "ch3.3_ha_007"
    ha "…No.{#ch3.3_ha_007}"

    th "She looks like she wants to say something — what should I do…"

    # [lay5 +396]
    $ show_sprites(("ha 3 sad", "s 1 sad"))

    voice "ch3.3_s_075"
    s "Hey, Haruna…"

    # ==== CHOICE (scene 1317) ====
    # select: 1318 / 1319 / 1320 → все ветки сходятся в ch3_1321
    menu:
        "Don't hold back with me.{#ch3_m1317a}":
            # ==== SCENE 1318 ====
            # RESET: фон/музыка/спрайты не меняются; [lay5 +390]
            $ show_sprites(("ha 3 sad", "s 1"))

            voice "ch3.3_s_076"
            s "Don't hold back with me."

            # [lay7 +981] → ha 3 shy
            $ show_sprites(("ha 3 shy", "s 1"))

            ha "…{#ch3.3_ha_v02}"

            # [好感度] ハルナ +10; tndl(-30) — не портируется (система не реализована)
            $ update_sympathy(10, char_key="haruna")

            voice "ch3.3_s_077"
            s "You and I are from the same world, you know."

            # [lay7 +973]
            $ show_sprites(("ha 3", "s 1"))

            ha "…{#ch3.3_ha_v03}"

            jump ch3_1321

        "You need to rest up now, okay?{#ch3_m1317b}":
            # ==== SCENE 1319 ====
            # RESET: фон/музыка/спрайты не меняются; [lay5 +390]
            $ show_sprites(("ha 3 sad", "s 1"))

            voice "ch3.3_s_078"
            s "You need to rest up now, okay?"

            ha "…{#ch3.3_ha_v04}"

            voice "ch3.3_s_079"
            s "This is a world where even curing one illness is a struggle. Your body's your greatest asset here."

            ha "…{#ch3.3_ha_v05}"

            jump ch3_1321

        "If you've got something to say, say it.{#ch3_m1317c}":
            # ==== SCENE 1320 ====
            # RESET: фон/музыка/спрайты не меняются; [lay5 +390]
            $ show_sprites(("ha 3 sad", "s 1"))

            voice "ch3.3_s_080"
            s "If you've got something to say, say it."

            ha "…{#ch3.3_ha_v06}"

            # [好感度] ハルナ -10; tndl(+30) — не портируется (система не реализована)
            $ update_sympathy(-10, char_key="haruna")

            # [lay5 +396]
            $ show_sprites(("ha 3 sad", "s 1 sad"))

            voice "ch3.3_s_081"
            s "Keeping things you want to say all to yourself is stressful — bad for your health, you know?"

            ha "…{#ch3.3_ha_v07}"

            jump ch3_1321

label ch3_1321:
    # ==== SCENE 1321 ====
    # RESET: (lay7 +973)[lay5 +390] — расхождение веток, показываем явно
    $ show_sprites(("ha 3", "s 1"))

    # [lay7 +979]
    $ show_sprites(("ha 3 sad", "s 1"))

    voice "ch3.3_ha_008"
    ha "I'm going to sleep…"

    voice "ch3.3_s_082"
    s "…Ah, right? See you later, then."

    # [BGM stop=1000], спрайты/фон скрываются → карта
    stop music fadeout 1.0
    $ ch3_2_visited.add("l_room")
    return
