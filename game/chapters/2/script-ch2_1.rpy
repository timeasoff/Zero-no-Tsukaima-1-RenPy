# Глава 2, часть 1 (сцены 68–75): утро, состояние Харуны, предупреждение о бомбисте

label ch2:
    call overlay_screen("overlay",  "Chapter Two: 'The Black-Haired Visitor'", isUseBlur=False, text_mode="black") from _call_overlay_screen_7
    pause(2)

    # ==== SCENE 68 ====
    $ fade_fx("id(88)", new_music="t4")

    voice "ch2_s_001"
    s "Mmm... Ahh— what a stretch."

    $ fade_fx("id(10)")

    $ show_sprites("s 1")
    voice "ch2_s_002"
    s "Morning, huh... It's been a while since I slept on straw. My whole body aches..."

    th "Can't be helped, I guess... Putting Siesta's bed into Louise's room made it two beds, and that's fine, but..."

    th "Counting Haruna, who isn't feeling well, to having a bed to herself..."

    th "The other bed must be for Louise and Siesta, right? Surely not all three of us getting into one bed..."

    th "Well, I did move back to the straw on my own, but... it feels kind of lonely..."

    $ show_sprites(None)
    $ show_sprites("si 1")
    voice "ch2_si_001"
    si "Ah— good morning, Saito-san."

    $ show_sprites(("si 1", "s 1"))
    voice "ch2_s_003"
    s "Good morning, Siesta. You're up early, as always."

    voice "ch2_si_002"
    si "I always have work in the mornings, so I'm up at this hour."

    voice "ch2_s_004"
    s "As usual, Siesta. I really admire you."

    $ show_sprites(("si 1 shy", "s 1"))
    voice "ch2_si_003"
    si "Ah, um, that's too kind... I'm still far from that..."

    $ show_sprites(("si 1", "s 1"))
    voice "ch2_s_005"
    s "Ah, right— is Louise still asleep? I'd better help with her morning routine while I can..."

    voice "ch2_si_004"
    si "Ah, Miss Valiere is..."

    $ show_sprites(None)
    $ show_sprites("l 1")
    voice "ch2_l_001"
    l "I'm already up."

    $ show_sprites(("l 1", "s 1"))
    voice "ch2_s_006"
    s "Wh— what!?"

    $ show_sprites(("l 1 angry", "s 1"))
    voice "ch2_l_002"
    l "Honestly, leaving your master behind and just snoring away— what do you think you're doing?"

    voice "ch2_s_007"
    s "Geez, why are you up early today of all days... It's usually your sleeping time!"

    voice "ch2_l_003"
    l "U-uh, be quiet. I actually get up this early."

    th "Is that really true..."

    $ show_sprites(("si 1", "s 1"))
    voice "ch2_si_005"
    si "Miss Valiere was up even before I got up."

    $ show_sprites(("si 1", "s 1"))
    th "Wh— what!? That's really early! What's going on?"

    # ==== CHOISE (scene 68) ====
    menu:
        "Couldn't sleep because of an all-nighter or something":
            # ==== SCENE 69 ====
            voice "ch2_s_008"
            s "You didn't stay up all night, did you?"

            $ show_sprites(("l 1", "s 1"))
            voice "ch2_l_004"
            l "N-no, that's not it at all. I slept just fine."

            $ show_sprites(("l 1", "s 1"))
            voice "ch2_s_009"
            s "If you fall asleep in class, it'd be shameful as a familiar, so get proper rest."

            $ show_sprites(("l 1 angry", "s 1"))
            voice "ch2_l_005"
            l "I told you I slept just fine! Besides, you're the one who's always asleep!"

            $ show_sprites(("si 1", "s 1"))
            voice "ch2_si_006"
            si "Eh? Saito-san, you sleep in class?"

            $ show_sprites(("si 1", "s 1"))
            voice "ch2_s_010"
            s "I-I mean, um... You see, I can't read the writing of this world, so I can't take part in class..."

            $ show_sprites(("l 1 angry", "s 1"))
            voice "ch2_l_006"
            l "Hmph, you just lack the will."

        "Couldn't sleep because that female guest was on her mind":
            # ==== SCENE 70 ====
            $ show_sprites(("si 1", "s 1"))
            voice "ch2_s_011"
            s "Couldn't sleep because that female guest was on your mind?"

            $ show_sprites(("si 1 sad", "s 1"))
            voice "ch2_si_007"
            si "Ah, was I in the way?"

            $ show_sprites(None)
            $ show_sprites("l 1")
            voice "ch2_l_007"
            l "U... no, that's not it. It's just that the room's population density was high, so I had a little trouble sleeping."

            $ update_sympathy(10, char_key="louise")

            $ show_sprites(("l 1", "si 1 sad"))
            voice "ch2_si_008"
            si "If that's the case, that's fine, though..."

            voice "ch2_si_009"
            si "If I was the reason you woke up early or something, I don't know how I should apologize..."

            $ show_sprites(None)
            $ show_sprites("s 1")
            voice "ch2_s_012"
            s "Ah, it's fine, Siesta. Louise isn't that sensitive."

            $ show_sprites(("l 1", "s 1"))
            voice "ch2_l_008"
            l "What do you mean by that!"

            $ show_sprites(("l 1 angry", "s 1"))
            voice "ch2_s_013"
            s "Ah, no, I mean it's that nothing ruffles her. Hey, Siesta!"

            $ show_sprites(("si 1", "s 1"))
            voice "ch2_si_010"
            si "Y-yes. Just as Saito-san says."

            $ show_sprites(("l 1", "s 1"))
            voice "ch2_l_009"
            l "Is that really true? Well, if that's the case, then it's fine."

        "Couldn't sleep because she was keeping watch on me":
            # ==== SCENE 71 ====
            $ show_sprites(("si 1", "s 1"))
            voice "ch2_s_014"
            s "You were keeping watch on me, or something?"

            $ show_sprites(("l 1", "s 1"))
            voice "ch2_l_010"
            l "Huh? Why?"

            $ show_sprites(("l 1", "s 1"))
            voice "ch2_s_015"
            s "I figured you were keeping watch out of worry for Siesta and Haruna."

            $ show_sprites(("l 1 angry", "s 1"))
            voice "ch2_l_011"
            l "Why would I have to monitor every move of my familiar! And besides— Saito, were you planning to do something?"

            $ update_sympathy(-10, char_key="louise")

            voice "ch2_s_016"
            s "No, it's nothing like that... I couldn't possibly do something so out of line. Yes, I swear on my fate."

            $ show_sprites(("l 1", "s 1"))
            voice "ch2_l_012"
            l "Really? Well, if that's the case, then it's fine."

            $ show_sprites(("l 1 angry", "s 1"))
            voice "ch2_l_013"
            l "If you were going to stir up trouble, you'll have to accept the punishment that comes with it."

    # ==== SCENE 72 ====
    $ show_sprites(("l 1", "s 1"))
    voice "ch2_s_017"
    s "Ah, right— what about Haruna?"

    $ show_sprites(("si 1", "s 1"))
    voice "ch2_si_011"
    si "She seems to still be sleeping."

    $ show_sprites(("l 1", "s 1"))
    voice "ch2_l_014"
    l "Hmph, looks like there's a bigger sleephead than me."

    $ show_sprites(("l 1", "s 1"))
    voice "ch2_s_018"
    s "No, that's not something to boast about at all, is it?"

    $ show_sprites(None)
    $ show_sprites("si 1 sad")
    voice "ch2_si_012"
    si "Ah, Haruna-san... ...Oh?"

    $ show_sprites(("si 1 sad", "s 1"))
    voice "ch2_s_019"
    s "...What's wrong, Siesta?"

    $ show_sprites(None)
    $ dissolve_fx("id(154)", stop_music=True, new_music="t27", type="cg")

    voice "ch2_si_013"
    si "Haruna-san, your face is pale. Besides, it looks like you have a fever too..."

    voice "ch2_ha_001"
    ha "...Hiraga-kun... Louise-san, Siesta-san... I'm sorry."

    voice "ch2_l_015"
    l "W-why are you apologizing! Pull yourself together!"

    voice "ch2_ha_002"
    ha "My body feels heavy, and I can't muster any strength..."

    voice "ch2_s_020"
    s "I get it, so stop talking. Sorry, Siesta— could you wake Montmorency up?"

    voice "ch2_si_014"
    si "Yes, understood."

    $ fade_fx("id(10)", sprites=("m 1", "s 1"))
    voice "ch2_m_001"
    m "Honestly, waking people up first thing in the morning— you really are a troublesome bunch. I did say I'd cooperate... though."

    voice "ch2_s_021"
    s "Sorry, Montmorency. So— how is Haruna doing!"

    voice "ch2_m_002"
    m "Hmm. She still hasn't adjusted to the change of environment, it seems, and that's why she has a fever."

    voice "ch2_m_003"
    m "She seemed to feel better yesterday, so I let my guard down. She'd better rest for a while."

    voice "ch2_ha_003"
    ha "I'm sorry for causing you trouble."

    voice "ch2_m_004"
    m "If you feel that way, then get better quickly."

    voice "ch2_ha_004"
    ha "Yes..."

    $ show_sprites(("m 1", "l 1"))
    voice "ch2_l_016"
    l "Besides, it's about time to head to class."

    voice "ch2_m_005"
    m "Oh my. I need to hurry back to my room and get ready."

    $ show_sprites(("m 1", "s 1"))
    voice "ch2_s_022"
    s "Since Louise got up early today, I thought we had plenty of time..."

    $ show_sprites(("l 1 angry", "s 1"))
    voice "ch2_l_017"
    l "Stop that! Let's get to class already."

    $ show_sprites(("l 1 angry", "s 1"))
    voice "ch2_s_023"
    s "Huh—? A, ow! I'm telling you, stop pulling! And you haven't changed yet, have you!"

    voice "ch2_l_018"
    l "A...!! I'll change right now, so get out of the room!"

    voice "ch2_s_024"
    s "Huh? I'm the one who's supposed to dress her?"

    $ show_sprites(None)
    $ show_sprites("si 1")
    voice "ch2_si_015"
    si "Saito-san..."

    $ show_sprites(None)
    $ dissolve_fx("id(155)", type="cg")

    voice "ch2_ha_005"
    ha "Hiraga-kun...{#hiraga}"

    $ fade_fx("id(10)", sprites="m 1")
    $ show_sprites("m 1 angry")
    voice "ch2_m_006"
    m "You're the lowest..."

    $ show_sprites(None)
    $ show_sprites("s 1")
    voice "ch2_s_025"
    s "Wha...? Wha...?"

    $ show_sprites(None)
    $ show_sprites(("l 1 angry", "si 1"))
    voice "ch2_l_019"
    l "Get out of the room quickly! Siesta will change for me."

    voice "ch2_si_016"
    si "Yes, understood. Saito-san, I'm sorry, but could you wait outside the room for a while?"

    voice "ch2_l_020"
    l "Stop dawdling and get out!"

    $ show_sprites(None)
    $ show_sprites("s 1")
    voice "ch2_s_026"
    s "Y-yes.{#h}"

    call open_door("right", "id(14)") from _call_open_door_5

    $ show_sprites("s 1", anim="slide_right")
    th "Honestly, minding other people's eyes... What's wrong with Louise today?"

    # ==== SCENE 73 ====
    $ fade_fx("id(23)", new_music="t31", sprites=("l 1", "s 1"))
    voice "ch2_s_027"
    s "In the end, we were late after all."

    voice "ch2_l_021"
    l "Hmph, we were late because Saito wouldn't get out of the room quickly, right?"

    $ show_sprites(("l 1", "s 1 angry"))
    voice "ch2_s_028"
    s "It's my fault, huh!"

    $ show_sprites("l 1")
    voice "ch2_c_001"
    c "Miss Valiere. What seems to be the problem this morning?"

    $ show_sprites("l 1")
    voice "ch2_l_022"
    l "E...eh!? Ah, no, um, nothing. Professor Colbert."

    voice "ch2_c_002"
    c "I see. Well, that's fine, but class is about to begin, so please refrain from private conversation."

    voice "ch2_l_023"
    l "Yes."

    $ show_sprites(None)
    voice "ch2_c_003"
    c "Ahem. Before we get into class, there's something I want to warn everyone about."

    voice "ch2_c_004"
    c "Recently, some of you must have heard about the bomber..."

    $ show_sprites("k 1")
    voice "ch2_k_001"
    k "Professor Colbert? Ah, you mean the one who's been carrying out bombing attacks around Tristania?"

    $ show_sprites(None)
    voice "ch2_c_005"
    c "That's right... It's about that bomber."

    voice "ch2_c_006"
    c "Over the past few months, several buildings in Tristania have been blown up with bombs. Their true identity remains unknown."

    voice "ch2_c_007"
    c "I don't think the damage will reach the academy, but I've been ordered to be extremely careful when heading into Tristania."

    voice "ch2_c_008"
    c "Do not, under any circumstances, try to capture him yourselves or do anything reckless. Understood?"

    $ show_sprites("s 1")
    voice "ch2_s_029"
    s "Wow, there are some dangerous people out there."

    $ show_sprites(("l 1", "s 1"))
    voice "ch2_l_024"
    l "Well, it's none of our business anyway."

    voice "ch2_s_030"
    s "Yeah, I guess so..."

    # ==== CHOISE (scene 73) ====
    menu:
        "Shall we go catch him too?":
            # ==== SCENE 74 ====
            voice "ch2_s_031"
            s "Shall we go catch him too?"

            $ show_sprites(("l 1 angry", "s 1"))
            voice "ch2_l_025"
            l "Hear people out, will you. Professor Colbert just said we shouldn't do anything reckless like that."

            $ update_sympathy(-10, char_key="louise")

            voice "ch2_s_032"
            s "I know that."

            $ show_sprites(("l 1", "s 1"))
            voice "ch2_l_026"
            l "Then don't say anything extra. Understood?"

            voice "ch2_s_033"
            s "Y-yes.{#h2}"

            jump ch2_2

        "I'd like to eat breakfast":
            # ==== SCENE 75 ====
            voice "ch2_s_034"
            s "Besides, I'd like to eat breakfast."

            voice "ch2_l_027"
            l "Huh?{#ssa}"

            voice "ch2_s_035"
            s "You see, between this and that, I never had time to eat breakfast after I woke up. I'm hungry, you know."

            $ show_sprites(("l 1 angry", "s 1"))
            voice "ch2_l_028"
            l "Hold out until lunch."

            voice "ch2_s_036"
            s "Geez, I didn't do anything wrong— am I going without food?"

            voice "ch2_s_037"
            s "If it's going to be like this, I should have asked Siesta to bring me something."

            $ show_sprites(("l 1", "s 1"))
            voice "ch2_l_029"
            l "Aaah, fine. Behave yourself, or I'll skip your lunch too!"

            voice "ch2_s_038"
            s "Y-yes.{#h3}"

            jump ch2_2

    return
