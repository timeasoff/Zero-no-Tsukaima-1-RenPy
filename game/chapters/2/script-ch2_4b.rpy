# Глава 2, часть 5 (сцены 1256–1265): выбор локации — 廊下 (Луиза) и 厨房 (Сиеста).
# Источник: ps2_source/chapters/chapter_03_黒髪の来訪者.txt (scene 01256…01265)
# Точные аргументы: ps2_source/events_full/chapter_03_黒髪の来訪者.txt (SCENE 01256…01265)
# Вызываются из карты script-ch2_4.rpy (ch2_4_map) как цели sprite_choice.

label hallway_ch2_4:
    # ==== SCENE 1256 ====
    $ fade_fx("hallway_evening", new_music="t5", sprites=("d 1", "s 2"))

    voice "ch2.5_s_001"
    s "Because of the commotion earlier, the whole academy feels restless."

    voice "ch2.5_d_001"
    d "Well, can't be helped. With a ruckus that flashy, you'd hear it even if you didn't see it."

    $ show_sprites(("l 1 angry", "s 2"))
    voice "ch2.5_l_001"
    l "Saito!"

    $ update_sympathy(20, char_key="louise")

    voice "ch2.5_s_002"
    s "Yeah?"

    voice "ch2.5_l_002"
    l "I wondered where you were wandering off to, and here you are."

    voice "ch2.5_l_003"
    l "Good grief, wandering off on your own away from your master — what are you thinking?"

    $ show_sprites(("l 1 angry", "s 4"))
    voice "ch2.5_s_003"
    s "Because I don't know when that bomb user might come back."

    voice "ch2.5_s_004"
    s "That's why I thought someone ought to keep a lookout."

    $ show_sprites(("l 3 sad", "s 4"))
    voice "ch2.5_l_004"
    l "I understand that, but... then at least consult me first. I'd worry about where you went, you know?"

    $ show_sprites(("l 3", "s 4 sad"))
    voice "ch2.5_s_005"
    s "Uh, that was thoughtless of me. Sorry."

    $ show_sprites(("l 3", "d 1 sad", "s 4 sad"))
    voice "ch2.5_l_005"
    l "If it were really the case, I'd blast those suspicious types away with my magic and catch them."

    voice "ch2.5_d_002"
    d "No, no, if you blast them away with magic, their lives would be in danger."

    $ show_sprites(("l 3", "s 2"))
    voice "ch2.5_s_006"
    s "First of all, your magic isn't something others can know about, right? You're not supposed to use it so casually."

    $ show_sprites(("l 1", "s 2"))
    voice "ch2.5_l_006"
    l "I know that without you telling me, Saito. That the 'Void' is something I must never tell anyone."

    $ show_sprites(("l 1 sad", "s 2"))
    voice "ch2.5_l_007"
    l "But everyone thinks I can't use magic well. To everyone, I'm 'Louise the Zero.'"

    $ show_sprites(("l 1 sad", "s 2 sad"))
    voice "ch2.5_s_007"
    s "Louise..."

    menu:
        "I know.{#ch2.5_m1256a}":
            # ==== SCENE 1257 ====
            $ show_sprites(("l 3 shy", "s 2"))
            voice "ch2.5_s_008"
            s "I know."

            voice "ch2.5_l_008"
            l "Wh-what, all of a sudden?"

            $ update_sympathy(10, char_key="louise")

            voice "ch2.5_s_009"
            s "Even if no one else in this world knows, I know. So don't make that face."

            $ show_sprites(("l 1 shy", "s 2"))
            voice "ch2.5_l_009"
            l "Sa... Saito?"

            $ show_sprites(("l 1 shy", "s 4"))
            voice "ch2.5_s_010"
            s "I said, don't make that teary-eyed face. It's not like you, Louise."

            $ show_sprites(("l 1 angry", "s 4"))
            voice "ch2.5_l_010"
            l "Wh-who's making a teary-eyed face! I'm not!"

        "Don't worry about that.{#ch2.5_m1256b}":
            # ==== SCENE 1258 ====
            $ show_sprites(("l 3 angry", "s 2 sad"))
            voice "ch2.5_s_011"
            s "Don't worry about that."

            voice "ch2.5_l_011"
            l "...You say that awfully casually."

            $ update_sympathy(-10, char_key="louise")

            $ show_sprites(("l 3 angry", "s 4 sad"))
            voice "ch2.5_s_012"
            s "It's not casual. Well, I can't understand a noble's pride and all that."

            $ show_sprites(("l 3 angry", "s 4"))
            voice "ch2.5_s_013"
            s "You yourself know that you're not 'Louise the Zero.' No matter what the others say, that's certain."

            $ show_sprites(("l 1", "s 4"))
            voice "ch2.5_l_012"
            l "Yeah... that's right. That's true."

        "Someday you'll be able to tell.{#ch2.5_m1256c}":
            # ==== SCENE 1259 ====
            $ show_sprites(("l 1", "s 2"))
            voice "ch2.5_s_014"
            s "Someday, the day will come when you can tell."

            voice "ch2.5_l_013"
            l "Eh...?"

            $ show_sprites(("l 1 sad", "s 2"))
            voice "ch2.5_s_015"
            s "Right now, you're the only 'Void' user in this country, so..."

            voice "ch2.5_s_016"
            s "If that were known, you might be taken advantage of for ill, so you have to keep it secret, right?"

            voice "ch2.5_l_014"
            l "Y-yes. Her Highness said that, but..."

            $ show_sprites(("l 1 sad", "s 4"))
            voice "ch2.5_s_017"
            s "So in other words, once the people who'd think to take advantage of you are gone, you can openly declare it, right?"

            voice "ch2.5_l_015"
            l "Y-yes. In theory that's how it works."

            $ show_sprites(("l 1", "s 4"))
            voice "ch2.5_s_018"
            s "Then what you should do is hone your magic and grow strong. If you can serve Her Highness, everything's OK."

            voice "ch2.5_l_016"
            l "...Hearing you talk, the world seems awfully simple."

            $ show_sprites(("l 1", "s 4 sad"))
            voice "ch2.5_s_019"
            s "What, that's a bad thing?"

            voice "ch2.5_l_017"
            l "If things went that easily, no one would have to struggle."

    # ==== SCENE 1260 ====
    voice "ch2.5_l_018"
    l "I feel like I've been smoothly talked around, but from now on, talk to me properly."

    voice "ch2.5_s_020"
    s "Yeah, got it."

    voice "ch2.5_l_019"
    l "Well then, I'll head back to my room. You do your best on your patrol."

    voice "ch2.5_s_021"
    s "Understood. I'll patrol thoroughly."

    $ ch2_4_visited.add("hallway")
    return

label kitchen_ch2_4:
    # ==== SCENE 1261 ====
    $ fade_fx("kitchen_evening", new_music="t6", sprites="s 2")

    voice "ch2.5_s_022"
    s "Looks like there's nothing particularly wrong here..."

    $ show_sprites(("si 1", "s 2"))
    voice "ch2.5_si_001"
    si "Ah, Saito-san!"

    $ update_sympathy(20, char_key="siesta")

    voice "ch2.5_s_023"
    s "Ah, hey, Siesta."

    voice "ch2.5_si_002"
    si "Thank goodness, Saito-san, you're safe."

    $ show_sprites(("si 1", "s 4 sad"))
    voice "ch2.5_s_024"
    s "Huh? Safe?"

    $ show_sprites(("si 1 sad", "s 4 sad"))
    voice "ch2.5_si_003"
    si "Earlier, there was a loud explosion outside, wasn't there?"

    voice "ch2.5_si_004"
    si "Then the academy teachers said, 'Commoners are not to go outside'..."

    voice "ch2.5_si_005"
    si "So I had no idea what happened outside."

    voice "ch2.5_si_006"
    si "I was so worried, thinking what if something happened to you, Saito-san..."

    $ show_sprites(("si 4 sad", "s 4 sad"))
    voice "ch2.5_s_025"
    s "I'm fine, as you can see. Right now I'm patrolling to check if there's any danger."

    $ show_sprites(("si 1 shy", "s 4 sad"))
    voice "ch2.5_si_007"
    si "Is that so. Saito-san, you really are dependable."

    voice "ch2.5_s_026"
    s "I-is that so? Ahaha..."

    $ show_sprites(("si 1", "s 4 sad"))
    voice "ch2.5_si_008"
    si "But what on earth happened?"

    voice "ch2.5_s_027"
    s "Ah, that's..."

    menu:
        "A suspicious person infiltrated.{#ch2.5_m1261a}":
            # ==== SCENE 1262 ====
            $ show_sprites(("si 1 sad", "s 2 angry"))
            voice "ch2.5_s_028"
            s "A suspicious person infiltrated."

            voice "ch2.5_si_009"
            si "A suspicious person?"

            $ show_sprites(("si 1 sad", "s 2"))
            voice "ch2.5_s_029"
            s "Yeah. The guy who tried to take Haruna yesterday, and his accomplice who uses bombs."

            $ show_sprites(("si 4 angry", "s 2"))
            voice "ch2.5_si_010"
            si "Those people infiltrated the academy grounds!?"

            voice "ch2.5_s_030"
            s "Ah, yeah. Me and Louise and the others beat them, but they got away."

            voice "ch2.5_s_031"
            s "So I'm patrolling to see if they've come back again."

            $ show_sprites(("si 1 shy", "s 2"))
            voice "ch2.5_si_011"
            si "Is that so. As expected of you, Saito-san."

            voice "ch2.5_s_032"
            s "No, it's nothing that big. I can only do this much."

            $ show_sprites(("si 4 shy", "s 2"))
            voice "ch2.5_si_012"
            si "No, that IS a big deal. And yet you don't boast about it... You're so humble, Saito-san."

            $ show_sprites(("si 4 shy", "s 4 happy"))
            voice "ch2.5_s_033"
            s "Ah, no, hahaha..."

            th "If I get praised so openly, I'll get embarrassed."

        "That Louise did it again.{#ch2.5_m1261b}":
            # ==== SCENE 1263 ====
            $ show_sprites(("si 4 happy", "s 4 happy"))
            voice "ch2.5_s_034"
            s "That Louise did it again."

            voice "ch2.5_si_013"
            si "Oh my, Miss Vallière?"

            voice "ch2.5_s_035"
            s "That's right, she once again let her magic run wild. She blew a huge hole in the courtyard."

            $ show_sprites(("si 1 happy", "s 4 happy"))
            voice "ch2.5_si_014"
            si "Oh my."

            voice "ch2.5_s_036"
            s "So right now, they're in the middle of restoring the courtyard outside."

            voice "ch2.5_s_037"
            s "I think they're telling people not to go outside because it's dangerous underfoot there."

            $ show_sprites(("si 1 happy", "s 4 sad"))
            voice "ch2.5_si_015"
            si "That's a lie, isn't it?"

            voice "ch2.5_s_038"
            s "Wh-what? Why would you think that?"

            $ show_sprites(("si 1", "s 4 sad"))
            voice "ch2.5_si_016"
            si "Because if that earlier explosion was Miss Vallière's doing, there'd be no need for you to patrol, Saito-san."

            voice "ch2.5_si_017"
            si "You told that lie on purpose to keep me from worrying, didn't you, Saito-san?"

            $ show_sprites(("si 1", "s 4"))
            voice "ch2.5_s_039"
            s "Hmm, you've seen right through me. Sorry, Siesta. You're right, that was all a lie."

            $ show_sprites(("si 4 happy", "s 4"))
            voice "ch2.5_si_018"
            si "Ufufu... Saito-san, you're so kind."

            $ update_sympathy(10, char_key="siesta")

            voice "ch2.5_s_040"
            s "Ah, no. It's nothing big."

        "I don't know either.{#ch2.5_m1261c}":
            # ==== SCENE 1264 ====
            $ show_sprites(("si 1 sad", "s 2 sad"))
            voice "ch2.5_s_041"
            s "I don't know either."

            voice "ch2.5_si_019"
            si "Is that so?{#ch2.5_si019}"

            $ update_sympathy(-10, char_key="siesta")

            voice "ch2.5_s_042"
            s "I know a huge explosion happened outside, but unfortunately I didn't see what actually happened..."

            voice "ch2.5_si_020"
            si "Is that so. I wonder what on earth happened."

            voice "ch2.5_s_043"
            s "I don't know, but if it wasn't an accident and someone suspicious snuck in, it'd be a problem."

            voice "ch2.5_s_044"
            s "So I'm patrolling like this."

            voice "ch2.5_si_021"
            si "Is that so. It must be hard for you too, Saito-san."

            $ show_sprites(("si 1 sad", "s 4 sad"))
            voice "ch2.5_s_045"
            s "No, I can only do this much."

            $ show_sprites(("si 1", "s 4 sad"))
            voice "ch2.5_si_022"
            si "It's fine. People are here to do what they can. That's what I think."

            $ show_sprites(("si 1", "s 4"))
            voice "ch2.5_s_046"
            s "Yeah, you're right. As expected of Siesta. You say good things."

            $ show_sprites(("si 4 shy", "s 4"))
            voice "ch2.5_si_023"
            si "Oh, stop it. It's nothing that big."

    # ==== SCENE 1265 ====
    $ show_sprites(("si 1", "s 2"))
    voice "ch2.5_s_047"
    s "Well then, if you see anyone unfamiliar or acting suspiciously, could you let me or the academy teachers know?"

    voice "ch2.5_si_024"
    si "Yes, understood. You take care too, Saito-san."

    voice "ch2.5_s_048"
    s "Thank you."

    $ ch2_4_visited.add("kitchen")
    return
