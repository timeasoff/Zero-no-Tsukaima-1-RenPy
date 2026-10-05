# Глава 2, часть 8 (сцены 1047–1058): завершение ветки Табиты
# (1047–1048) и ветки свиданий с Кирке (1049–1053) и Харуной
# (1054–1058). Общего входного лейбла ch2_8 нет:
#   ch2_8_tabitha_1047/1048 — jump из script-ch2_7.rpy,
#   date_kirche_ch2_8 / date_haruna_ch2_8 — из portrait_choice
#   (script-ch2_6.rpy).
# Источник: ps2_source/chapters/chapter_03_黒髪の来訪者.txt
# Точные аргументы: ps2_source/events_full/chapter_03_黒髪の来訪者.txt

label ch2_8_tabitha_1047:
    # ==== SCENE 1047 ====
    $ fade_fx("cafe_entrance", sprites=("t 1 sad", "s 1"))
    voice "ch2.8_s_001"
    s "Come on, let's look around some other places too."
    voice "ch2.8_t_001"
    t "...I'm not interested in anything but the bookstore."
    $ update_sympathy(-15, char_key="tabitha")
    voice "ch2.8_s_002"
    s "I figured. But on a day like this, window shopping'll do - let's just stroll around."
    $ show_sprites(("t 1", "s 1"))
    voice "ch2.8_t_002"
    t "...Win-dow... what?"
    $ show_sprites(("t 1", "s 3 sad"))
    voice "ch2.8_s_003"
    s "Huh? Er..."
    $ show_sprites(("t 1", "s 3"))
    voice "ch2.8_s_004"
    s "It's a word from my country - it means wandering past the shops and looking in the windows, even if you're not buying."
    voice "ch2.8_t_003"
    t "...I don't mind."
    voice "ch2.8_s_005"
    s "Alright, let's go look around."
    jump ch2_8_tabitha_1048

label ch2_8_tabitha_1048:
    # ==== SCENE 1048 ====
    $ fade_fx("town_evening", sprites=("t 1", "s 1"))
    voice "ch2.8_s_006"
    s "So? Feeling better?"
    $ show_sprites(("t 1 happy", "s 1"))
    th "...{#ch2.8_th1048}"
    voice "ch2.8_s_007"
    s "I see. That's good."
    voice "ch2.8_s_008"
    s "So, what now? Want to look around a bit more?"
    $ show_sprites(("t 1", "s 1"))
    voice "ch2.8_t_004"
    t "...I'm going home now."
    voice "ch2.8_s_009"
    s "I see... Well, um."
    $ show_sprites(("t 1", "s 3"))
    voice "ch2.8_s_010"
    s "It's a shame about the book, but don't mope too much about it."
    $ show_sprites(("t 1 happy", "s 3"))
    voice "ch2.8_t_005"
    t "...I know. And... today was fun."
    $ show_sprites(("t 1 happy", "s 1"))
    voice "ch2.8_s_011"
    s "Hm? I'm glad to hear that. Shall we head back to the academy?"
    $ show_sprites(("t 1", "s 1"))
    voice "ch2.8_t_006"
    t "...Yeah."
    stop music fadeout 1.0
    $ pause(1.0)
    return

label date_kirche_ch2_8:
    # ==== SCENE 1049 ====
    $ fade_fx("hallway", new_music="t7", sprites=("s 1",), side="left")
    play sound knock_door
    voice "ch2.8_s_012"
    s "Kirche, you in?"
    call open_door("left", "room") from _call_open_door_10
    $ show_sprites(("k 2 angry",), side="right")
    voice "ch2.8_k_001"
    k "I am, yees. What do you want?"
    $ show_sprites(("s 3 sad", "k 2 angry"))
    voice "ch2.8_s_013"
    s "...You seem sort of in a bad mood. What's wrong?"
    voice "ch2.8_k_002"
    k "It's hoooot! Seriously, what is this heat? And there's not even a breeze..."
    voice "ch2.8_s_014"
    s "Kirche, you can't stand the heat? A lukewarm Kirche... what would that even be?"
    $ show_sprites(("s 3 sad", "k 2 sad"))
    voice "ch2.8_k_003"
    k "Not at all. Ugh, isn't there somewhere cool?"
    $ show_sprites(("s 1 sad", "k 2 sad"))
    voice "ch2.8_s_015"
    s "Hmm. Was there somewhere...?"
    $ show_sprites(("s 1 sad", "k 2 happy"))
    voice "ch2.8_k_004"
    k "...That's it, I've decided!!"
    voice "ch2.8_s_016"
    s "Huh? So there is somewhere?"
    voice "ch2.8_k_005"
    k "When it comes to cooling off, it's the lake. Darling, let's go to the lake!"
    $ update_sympathy(20, char_key="kirche")
    $ show_sprites(("s 3 happy", "k 2 happy"))
    voice "ch2.8_s_017"
    s "Huh, a lake? Is it that close?"
    voice "ch2.8_k_006"
    k "Exactly. Then it's decided - let's hurry up and go. Come on, come on, come on."
    $ show_sprites(("s 3 sad", "k 2 happy"))
    voice "ch2.8_s_018"
    s "Wait. What are we even going to do at the lake?"
    $ show_sprites(("s 3 sad", "k 2 shy"))
    voice "ch2.8_k_007"
    k "What do you mean? If you go to the lake, there's only one thing to do."
    voice "ch2.8_s_019"
    s "Such as...?"
    menu:
        "Fishing!{#ch2.8_m1049a}":
            jump ch2_8_kirche_1050
        "Let's swim!{#ch2.8_m1049b}":
            jump ch2_8_kirche_1051
        "An adventure in the shade!{#ch2.8_m1049c}":
            jump ch2_8_kirche_1052

label ch2_8_kirche_1050:
    # ==== SCENE 1050 ====
    $ fade_fx("room", sprites=("s 3 sad", "k 2 shy"))
    $ show_sprites(("s 1 happy", "k 2 shy"))
    voice "ch2.8_s_020"
    s "Fishing!"
    $ show_sprites(("s 1 happy", "k 2 angry"))
    voice "ch2.8_k_008"
    k "How do you get that?!"
    $ update_sympathy(-10, char_key="kirche")
    $ show_sprites(("s 1 sad", "k 2 angry"))
    voice "ch2.8_s_021"
    s "Huh, I was wrong?"
    voice "ch2.8_k_009"
    k "Sit there zoning out in the sun on a gorgeous day, waiting for a fish to bite? In your dreams."
    $ show_sprites(("s 3 happy", "k 2 angry"))
    voice "ch2.8_s_022"
    s "Oh, right. That would be hot."
    $ show_sprites(("s 3 happy", "k 2"))
    voice "ch2.8_k_010"
    k "Besides, neither of us has any fishing gear anyway."
    $ show_sprites(("s 1", "k 2"))
    voice "ch2.8_s_023"
    s "Ha, now that you mention it, you're right!"
    $ show_sprites(("s 1", "k 2 happy"))
    voice "ch2.8_k_011"
    k "If we're going to the lake, there's only one thing to do. Obviously we're swimming."
    voice "ch2.8_s_024"
    s "Oh, now that sounds fun."
    voice "ch2.8_k_012"
    k "Oh, just to check - you can swim, can't you, Darling?"
    voice "ch2.8_s_025"
    s "I can swim about as well as the next person."
    voice "ch2.8_k_013"
    k "Good. It'd be no fun if you were stuck all alone on the shore."
    jump ch2_8_kirche_1053

label ch2_8_kirche_1051:
    # ==== SCENE 1051 ====
    $ fade_fx("room", sprites=("s 3 sad", "k 2 shy"))
    $ show_sprites(("s 3 happy", "k 2 shy"))
    voice "ch2.8_s_026"
    s "Let's swim!"
    $ show_sprites(("s 3 happy", "k 2 happy"))
    voice "ch2.8_k_014"
    k "Straight to the point, as ever."
    $ update_sympathy(10, char_key="kirche")
    $ show_sprites(("s 1 happy", "k 2 happy"))
    voice "ch2.8_s_027"
    s "Yep. When it's hot, nothing beats a swim in the sea or the pool."
    jump ch2_8_kirche_1053

label ch2_8_kirche_1052:
    # ==== SCENE 1052 ====
    $ fade_fx("room", sprites=("s 3 sad", "k 2 shy"))
    $ show_sprites(("s 3 shy", "k 2 shy"))
    voice "ch2.8_s_028"
    s "An adventure in the shade!"
    voice "ch2.8_k_015"
    k "Oh? That has its own appeal, actually."
    $ show_sprites(("s 1 shy", "k 2 shy"))
    voice "ch2.8_s_029"
    s "Wait, really?"
    th "How much of that was serious...? Or am I just being toyed with?"
    $ show_sprites(("s 1 shy", "k 2 happy"))
    voice "ch2.8_k_016"
    k "But since we're going all the way to the lake, we have to swim first!"
    $ show_sprites(("s 1 sad", "k 2 happy"))
    th "...Yeah, fair enough."
    jump ch2_8_kirche_1053

label ch2_8_kirche_1053:
    # ==== SCENE 1053 ====
    $ fade_fx("room", sprites=("s 3 sad", "k 2 happy"))
    voice "ch2.8_s_030"
    s "Okay, so we're going to the lake to swim. But what about supplies and all..."
    voice "ch2.8_k_017"
    k "We don't need any of that. We're going as we are! Come on, let's go!"
    $ show_sprites(("s 3 angry", "k 2 happy"))
    voice "ch2.8_s_031"
    s "Whaaat!?"
    $ fade_fx("forest", sprites=("s 3 sad", "k 2"))
    voice "ch2.8_k_018"
    k "Come on, just a little further."
    voice "ch2.8_s_032"
    s "Sorry, I need a break. I'm worn out from walking."
    $ show_sprites(("s 3 sad", "k 2 sad"))
    voice "ch2.8_k_019"
    k "Honestly, Darling, you're such a laggard. I'm going on ahead."
    $ show_sprites(("s 3 sad",), side="left")
    voice "ch2.8_s_033"
    s "Wow, she really left me. She must have wanted to swim that badly."
    $ fade_fx("id(247)", type="cg", new_music="t13")
    voice "ch2.8_k_020"
    k "Here I go-o!!"
    voice "ch2.8_k_021"
    k "Come on, Darling! Hurry up and get here!"
    voice "ch2.8_s_034"
    s "I-I can't just come when you tell me to! Kirche, you're not wearing anything, are you!?"
    voice "ch2.8_k_022"
    k "Of course not. You don't swim in your clothes."
    voice "ch2.8_s_035"
    s "Y-yes, ma'am, that's true, but..."
    voice "ch2.8_k_023"
    k "Darling..."
    voice "ch2.8_s_036"
    s "Waaah! Stop coming at me like that!"
    voice "ch2.8_k_024"
    k "Huh? What's wrong? You just dropped to your knees all of a sudden."
    voice "ch2.8_s_037"
    s "Well, you see, a phenomenon particular to men has occurred."
    voice "ch2.8_k_025"
    k "Oh, that? Fufu, Darling, you're so innocent. Adorable!"
    voice "ch2.8_s_038"
    s "A-a-adorable... I see."
    voice "ch2.8_k_026"
    k "You're all red. I could just eat you up!"
    voice "ch2.8_s_039"
    s "Please don't eat me..."
    stop music fadeout 1.0
    $ pause(1.0)
    return

label date_haruna_ch2_8:
    # ==== SCENE 1054 ====
    $ fade_fx("louise_room", new_music="t10", sprites=("ha 1",), side="right")
    voice "ch2.8_ha_001"
    ha "Ah... Hiraga-kun."
    $ update_sympathy(20, char_key="haruna")
    $ show_sprites(("s 1", "ha 1"))
    voice "ch2.8_s_040"
    s "Hey, Haruna... You were reading something, weren't you? What was it?"
    $ show_sprites(("s 1", "ha 1 sad"))
    voice "ch2.8_ha_002"
    ha "Um..."
    $ show_sprites(("s 3", "ha 1 sad"))
    voice "ch2.8_s_041"
    s "Ah, wait - let me guess?"
    voice "ch2.8_ha_003"
    ha "H-huh...?"
    voice "ch2.8_s_042"
    s "So, my guess is..."
    menu:
        "A diary, of course.{#ch2.8_m1054a}":
            jump ch2_8_haruna_1055
        "A student handbook.{#ch2.8_m1054b}":
            jump ch2_8_haruna_1056
        "A letter from someone.{#ch2.8_m1054c}":
            jump ch2_8_haruna_1057

label ch2_8_haruna_1055:
    # ==== SCENE 1055 ====
    $ fade_fx("louise_room", sprites=("s 3", "ha 1 sad"))
    voice "ch2.8_s_043"
    s "A diary, of course."
    $ show_sprites(("s 3", "ha 1 shy"))
    voice "ch2.8_ha_004"
    ha "Nope, not that."
    $ show_sprites(("s 3", "ha 1 sad"))
    voice "ch2.8_ha_005"
    ha "I did have a bag with me, but I lost it when we escaped."
    $ show_sprites(("s 1 sad", "ha 1 sad"))
    voice "ch2.8_s_044"
    s "I-I see..."
    voice "ch2.8_ha_006"
    ha "I still have a few things with me, but this is my treasure now."
    voice "ch2.8_s_045"
    s "Is that a student handbook?"
    voice "ch2.8_ha_007"
    ha "Mm-hm."
    jump ch2_8_haruna_1058

label ch2_8_haruna_1056:
    # ==== SCENE 1056 ====
    $ fade_fx("louise_room", sprites=("s 3", "ha 1 sad"))
    voice "ch2.8_s_046"
    s "A student handbook, of course."
    $ show_sprites(("s 3", "ha 4 happy"))
    voice "ch2.8_ha_008"
    ha "Bingo. I'd tucked it into my uniform pocket, so it barely made it."
    $ update_sympathy(10, char_key="haruna")
    $ show_sprites(("s 3", "ha 1 sad"))
    voice "ch2.8_ha_009"
    ha "I did have a bag with me, but I lost it when we escaped.{#ch2.8_ha_009}"
    $ show_sprites(("s 1 sad", "ha 1 sad"))
    voice "ch2.8_s_047"
    s "I-I see...{#ch2.8_s_047}"
    jump ch2_8_haruna_1058

label ch2_8_haruna_1057:
    # ==== SCENE 1057 ====
    $ fade_fx("louise_room", sprites=("s 3", "ha 1 sad"))
    voice "ch2.8_s_048"
    s "A letter from someone, of course?"
    $ show_sprites(("s 3", "ha 4 shy"))
    voice "ch2.8_ha_010"
    ha "W-wha!? N-no, it's nothing like that!"
    voice "ch2.8_s_049"
    s "Oh, I was sure it was a love letter from somebody."
    $ show_sprites(("s 3", "ha 4 angry"))
    voice "ch2.8_ha_011"
    ha "I told you, no! This - this right here. See, you recognize it?"
    $ show_sprites(("s 3 sad", "ha 4 angry"))
    voice "ch2.8_s_050"
    s "The student handbook? You were reading that? Even after coming here, you're still the model student."
    $ show_sprites(("s 3 sad", "ha 1"))
    voice "ch2.8_ha_012"
    ha "It's not really like that, though."
    voice "ch2.8_ha_013"
    ha "I did have a bag with me, but I lost it when we escaped.{#ch2.8_ha_013}"
    $ show_sprites(("s 3 sad", "ha 1 sad"))
    voice "ch2.8_ha_014"
    ha "This is the only thing I have left... I think."
    voice "ch2.8_s_051"
    s "Haruna..."
    jump ch2_8_haruna_1058

label ch2_8_haruna_1058:
    # ==== SCENE 1058 ====
    $ fade_fx("louise_room", sprites=("s 1 sad", "ha 1 sad"))
    voice "ch2.8_ha_015"
    ha "Words work just fine in this world, but I can't read a single character."
    voice "ch2.8_s_052"
    s "Same as me..."
    voice "ch2.8_ha_016"
    ha "I never used to read the handbook. But if I don't read it now, I'm afraid I'll forget Japanese before long... it scares me."
    voice "ch2.8_s_053"
    s "I see... Come to think of it, I never really read the handbook properly either."
    $ fade_fx("id(269)", type="cg", new_music="t16")
    voice "ch2.8_s_054"
    s "Let's see, there was something funny in here... Um... 'Do not dress too showily'?"
    voice "ch2.8_ha_017"
    ha "Hee hee. 'Do not take detours on the way to or from school'!"
    voice "ch2.8_s_055"
    s "'Diligent study and a regular lifestyle' - there's a line like that in here."
    voice "ch2.8_ha_018"
    ha "The school song and the cheering song are in here too."
    voice "ch2.8_s_056"
    s "Ugh, I can't sing either of them at all."
    voice "ch2.8_ha_019"
    ha "Fufu."
    voice "ch2.8_s_057"
    s "Come to think of it, wasn't the button on the far right of the school vending machine always sold out?"
    voice "ch2.8_ha_020"
    ha "It was! It was!"
    voice "ch2.8_s_058"
    s "Wonder why the vendor never fixed it."
    voice "ch2.8_ha_021"
    ha "Actually, that button? If you press it, you can buy juice just fine. Did you know?"
    voice "ch2.8_s_059"
    s "Gah! Who knew there was a hidden trick like that!"
    voice "ch2.8_ha_022"
    ha "Really! Hee hee, ahaha!"
    voice "ch2.8_s_060"
    s "Haha, ahaha!"
    th "She laughed... I guess talking about memories of Japan is what makes Haruna happiest."
    stop music fadeout 1.0
    $ pause(1.0)
    return

