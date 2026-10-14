# Глава 3, часть 4 (сцены 163–168): Сиеста слишком рьяно ухаживает за
# больной Харуной — комната раскалена; Сайто застаёт их вдвоём, появляется
# Луиза, Сиеста падает в обморок.
# Источник: ps2_source/chapters/chapter_04_女の戦い.txt (SCENE 0163–0168).
# Голоса: ch3.4_si_001…030, ch3.4_ha_001…025, ch3.4_s_001…029, ch3.4_l_001…009.

label ch3_4:
    # ==== SCENE 163 ====
    # [BG stage image=+10] louise_room, [BGM play=+30] → t29
    $ fade_fx("louise_room", new_music="t29")
    $ show_sprites("ha 3")

    # [SE se0 play=+82] — не портируется (см. отчёт)
    voice "ch3.4_si_001"
    si "Haruna-san, pardon me~!"

    # спрайты скрываются, включается CG «Сиеста с грудой вещей»
    $ show_sprites(None)
    $ fade_fx("id(115)", type="cg")

    voice "ch3.4_ha_001"
    ha "Siesta-san… What's with all this luggage…?"

    voice "ch3.4_si_002"
    si "How are you feeling?"

    voice "ch3.4_ha_002"
    ha "Somehow, I'm managing…"

    voice "ch3.4_si_003"
    si "…But your complexion still doesn't look good. Could it be a cold?"

    voice "ch3.4_ha_003"
    ha "Maybe… something like that?"

    voice "ch3.4_si_004"
    si "...{#ch3.4_si_004}"

    voice "ch3.4_ha_004"
    ha "...{#ch3.4_ha_004}"

    voice "ch3.4_si_005"
    si "I've prepared all sorts of things for you, Haruna."

    voice "ch3.4_ha_005"
    ha "Eh…?"

    # [EVENT_CG image=+116]
    $ dissolve_fx("id(116)", type="cg")

    voice "ch3.4_si_006"
    si "First, let me tuck you into this thick quilt."

    # [VIBRATE vibrate(2)] + waitTime(800)
    $ shake_fx(duration=0.8)

    voice "ch3.4_ha_006"
    ha "Ah, if you do that…"

    # [EVENT_CG image=+115]
    $ dissolve_fx("id(115)", type="cg")

    voice "ch3.4_si_007"
    si "They say it's good to sweat out a cold. This is kindness."

    voice "ch3.4_ha_007"
    ha "R-right. Ju-just the right temperature, or so I thought."

    voice "ch3.4_si_008"
    si "I'm glad! I wanted to warm you up, so I made something really hot!"

    voice "ch3.4_ha_008"
    ha "Um, I don't really have an appetite right now…"

    $ dissolve_fx("id(116)", type="cg")

    voice "ch3.4_si_009"
    si "No good, Haruna. You have to eat precisely because you have a cold."

    $ dissolve_fx("id(115)", type="cg")

    voice "ch3.4_si_010"
    si "If you don't get proper nutrition, your cold will never get better, you know."

    voice "ch3.4_ha_009"
    ha "Could it be… you're dead set on making me eat?"

    voice "ch3.4_si_011"
    si "Dead set, you say… How harsh. I put my heart into preparing this dish because I wanted you to eat it."

    $ dissolve_fx("id(116)", type="cg")

    voice "ch3.4_si_012"
    si "If you were already well, you might not need to eat it… or so I was thinking…"

    voice "ch3.4_ha_010"
    ha "...{#ch3.4_ha_010}"

    $ dissolve_fx("id(115)", type="cg")

    voice "ch3.4_ha_011"
    th "She's trying to get me to admit I'm not really sick…"

    voice "ch3.4_ha_012"
    th "She doesn't like that Hiraga-kun is nursing me, I'm sure… but I'm not about to back down either…"

    voice "ch3.4_ha_013"
    ha "…I won't lose."

    voice "ch3.4_si_013"
    si "Pardon? Did you say something?"

    voice "ch3.4_ha_014"
    ha "N-nope, nothing~."

    voice "ch3.4_si_014"
    si "Now, it's all ready."

    voice "ch3.4_ha_015"
    ha "My, it looks really hot… Like it's bubbling away."

    voice "ch3.4_ha_016"
    ha "Even so, this might be too hot to eat…"

    voice "ch3.4_si_015"
    si "No, no. A sick person has to eat at least this much…"

    $ dissolve_fx("id(116)", type="cg")

    voice "ch3.4_si_016"
    si "Oh, right—I also prepared firewood, so I'll light the fireplace later."

    voice "ch3.4_ha_017"
    ha "Eh…!!"

    $ dissolve_fx("id(115)", type="cg")

    voice "ch3.4_si_017"
    si "Ufu, ufufufu…"

    voice "ch3.4_ha_018"
    ha "Fufu, fufufufu…"

    # [BGM stop=1000], спрайты/CG скрываются → next scene 164
    stop music fadeout 1.0

    # ==== SCENE 164 ====
    # [BG stage image=+14] hallway, [BGM play=+19] → t18
    $ fade_fx("hallway", new_music="t18")
    $ show_sprites("s 3 sad")

    voice "ch3.4_s_001"
    s "Louise, where the heck did she go off to…"

    # [SE se0 play=+57], затем смена фона: [BG image=+13] louise_room_night, [BGM play=+30]
    $ fade_fx("louise_room_night", new_music="t29")
    $ show_sprites("s 1 angry")

    voice "ch3.4_s_002"
    s "Wh-wha—!? W-what the—!?"

    voice "ch3.4_s_003"
    s "This room's heat is unnatural—!?"

    # Сиеста и Харуна улыбаются друг другу в раскалённой комнате
    $ show_sprites(("si 1 happy", "ha 3 happy"))

    voice "ch3.4_si_018"
    si "Ufufu, ufufufu…"

    voice "ch3.4_ha_019"
    ha "Fufufu, fufufufu…"

    $ show_sprites("s 1 angry")

    voice "ch3.4_s_004"
    s "W-what are you doing? Grinning at each other in this heat!"

    $ show_sprites("s 1 sad")

    voice "ch3.4_s_005"
    s "U-um…"

    # ==== CHOICE (scene 164) ====
    menu:
        "Are you okay, Haruna?{#ch3_m164a}":
            # ==== SCENE 165 ====
            $ show_sprites("s 1 sad")

            voice "ch3.4_s_006"
            s "Are you okay, Haruna?"

            $ show_sprites(("s 1 sad", "ha 3 sad"))

            voice "ch3.4_ha_020"
            ha "Ah, Hiraga-kun… I'm fine…"
            $ update_sympathy(10, char_key="haruna")

            $ show_sprites(("s 1 angry", "ha 3 sad"))

            voice "ch3.4_s_007"
            s "No, no, no—what are you saying? This doesn't look fine at all!"

            $ show_sprites(("s 1 sad", "ha 3 sad"))

            voice "ch3.4_s_008"
            s "You're drenched in sweat—how many quilts do you have on you?"

            $ show_sprites(("s 1 sad", "ha 3"))

            voice "ch3.4_ha_021"
            ha "Th-that's…"

            $ show_sprites(("s 1", "ha 3"))

            voice "ch3.4_s_009"
            s "That's?"

            $ show_sprites(("s 1 sad", "ha 3 sad"))

            voice "ch3.4_ha_022"
            ha "It's nothing…"

            $ show_sprites("s 1 sad")

            voice "ch3.4_s_010"
            s "That's the thing—'it's nothing' can't cover a situation like this, right?"

            jump ch3_4_168

        "Siesta, you okay?{#ch3_m164b}":
            # ==== SCENE 166 ====
            $ show_sprites("s 1 sad")

            voice "ch3.4_s_011"
            s "Siesta, you okay?"

            $ show_sprites(("s 1 sad", "si 4 shy"))

            voice "ch3.4_si_019"
            si "Ah, Saito-san… Ufufufu…"
            $ update_sympathy(10, char_key="siesta")

            $ show_sprites(("s 3 sad", "si 4 shy"))

            voice "ch3.4_s_012"
            s "No, I don't mean 'Saito-san'—"

            $ show_sprites(("s 3 sad", "si 1 happy"))

            voice "ch3.4_si_020"
            si "Yees. I'm fiiine."

            $ show_sprites(("s 1 sad", "si 1 happy"))

            voice "ch3.4_s_013"
            s "You don't look fine at all… More importantly, what are you two doing?"

            $ show_sprites(("s 1 sad", "si 1"))

            voice "ch3.4_si_021"
            si "W-well, you see… I was just warming up the room a little…"

            $ show_sprites(("s 1", "si 1"))

            voice "ch3.4_s_014"
            s "Warming it? Why?"

            voice "ch3.4_si_022"
            si "Well, how should I put it…"

            $ show_sprites(("s 1", "si 4 happy"))

            voice "ch3.4_s_015"
            s "How should you put it?"

            voice "ch3.4_si_023"
            si "Ufufufu…"

            $ show_sprites(("s 1 sad", "si 4 happy"))

            voice "ch3.4_s_016"
            s "No, I don't mean 'ufufu'—"

            jump ch3_4_168

        "...Louise!?{#ch3_m164c}":
            # ==== SCENE 167 ====
            $ show_sprites("s 1 sad")

            voice "ch3.4_s_017"
            s "...Louise!?"

            $ show_sprites(("si 1", "ha 3"))

            voice "ch3.4_si_024"
            si "If you mean Miss Vallière, she isn't here."

            voice "ch3.4_ha_023"
            ha "Yes, it's just the two of us…"

            $ show_sprites("s 3 sad")

            voice "ch3.4_s_018"
            s "I see… So what are you two up to? Making the room this hot and all."

            $ show_sprites(("si 1 sad", "ha 3 sad"))

            voice "ch3.4_si_025"
            si "...{#ch3.4_si_025}"

            voice "ch3.4_ha_024"
            ha "...{#ch3.4_ha_024}"

            $ show_sprites(("si 4 happy", "ha 3 sad"))

            voice "ch3.4_si_026"
            si "Ufufu, ufufufu…{#ch3.4_si_026}"

            $ show_sprites(("si 4 happy", "ha 3 happy"))

            voice "ch3.4_ha_025"
            ha "Fufufu, fufufufu…{#ch3.4_ha_025}"

            $ show_sprites("s 1 sad")

            voice "ch3.4_s_019"
            s "I have no idea what's going on…"

            jump ch3_4_168

label ch3_4_168:
    # ==== SCENE 168 ====
    $ show_sprites("s 3 sad")

    voice "ch3.4_s_020"
    s "What on earth is going on?"

    $ show_sprites("l 1 happy")

    voice "ch3.4_l_001"
    l "Wow, it really did get hot~. Ah, Saito…"

    $ show_sprites(("l 1 angry", "s 1 angry"))

    voice "ch3.4_s_021"
    s "Hey, Louise. I just made a 'this is bad' face at you, didn't I?"

    $ show_sprites(("l 3 happy", "s 1 angry"))

    voice "ch3.4_l_002"
    l "Eh? What do you mean?"

    $ show_sprites(("l 3 happy", "s 1"))

    voice "ch3.4_s_022"
    s "You don't seem that surprised by how hot this room is."

    $ show_sprites(("l 1 angry", "s 1"))

    voice "ch3.4_l_003"
    l "Th-that's just your imagination!"

    $ show_sprites(("l 1 angry", "s 1 sad"))

    voice "ch3.4_s_023"
    s "Besides, it's your own room in this state—you should be at least a little surprised…"

    $ show_sprites(("l 1", "s 1 sad"))

    voice "ch3.4_l_004"
    l "…Waaah, Siesta, are you okay-? How did this happen-!"

    $ show_sprites(("l 1", "s 3 sad"))

    th "She's laying it on thick…"

    $ show_sprites(("l 1", "si 4 sad"))

    voice "ch3.4_si_027"
    si "M-Miss Vallière… I'm done for."

    $ show_sprites(("l 1 sad", "si 4 sad"))

    voice "ch3.4_l_005"
    l "W-wait, Siesta!?"

    voice "ch3.4_si_028"
    si "I'll entrust the rest to your ha…n… ……hau!?"

    $ show_sprites("l 1 sad")
    $ shake_fx(duration=0.8)

    $ show_sprites(("l 1 sad", "s 1 angry"))

    voice "ch3.4_s_024"
    s "Waaah—Siesta!?"

    $ show_sprites(("l 1 angry", "s 1 angry"))

    voice "ch3.4_l_006"
    l "Hey, pull yourself together, Siesta! Siestaa!?"

    # [BGM stop=1000], затемнение
    stop music fadeout 1.0
    $ show_sprites(None)
    $ fade_fx("black")

    th "………………"

    # [BG image=+10] louise_room, [BGM play=+19] → t18 — Сиеста приходит в себя
    $ fade_fx("louise_room", new_music="t18")
    $ show_sprites("si 1 sad")

    voice "ch3.4_si_029"
    si "S-sorry. I actually passed out…"

    $ show_sprites(("si 1 sad", "l 1 happy"))

    voice "ch3.4_l_007"
    l "Ah, you're okay. Thank goodness…"

    $ show_sprites(("l 1 happy", "s 1 angry"))

    voice "ch3.4_s_025"
    s "Louise…"

    $ show_sprites(("l 1 angry", "s 1 angry"))

    voice "ch3.4_l_008"
    l "Wh-what…"

    voice "ch3.4_s_026"
    s "And you, Siesta…"

    $ show_sprites(("s 1 angry", "si 1 angry"))

    voice "ch3.4_si_030"
    si "Y-yes!"

    voice "ch3.4_s_027"
    s "What exactly did you two do?"

    $ show_sprites(("s 1 angry", "l 3 sad"))

    voice "ch3.4_l_009"
    l "I didn't do anything…"

    voice "ch3.4_s_028"
    s "You did plenty! Heating up the room like idiots with Siesta—what were you thinking!"

    $ show_sprites(("s 1 angry", "l 1 sad"))

    voice "ch3.4_s_029"
    s "Haruna's sick! Even if she weren't, doing this to someone would break their body, you know?!"

    th "But who started this mess?"

    # ==== CHOICE (scene 168) → сцены 169–171 (часть 5) ====
    menu:
        "It was Louise who started it, right?{#ch3_m168a}":
            jump ch3_5_169

        "This isn't like the usual Siesta.{#ch3_m168b}":
            jump ch3_5_170

        "Do you dislike Haruna?{#ch3_m168c}":
            jump ch3_5_171
