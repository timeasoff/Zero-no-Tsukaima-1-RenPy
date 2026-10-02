# Осман вызывает в кабинет
label ch1_7:
    $ fade_fx("yard", new_music="t31", type="cg")
    voice "ch1.7_o_001"
    o "So? What exactly happened here?"

    $ fade_fx("osman_cabinet", sprites=("o 1"))
    voice "ch1.7_o_002"
    o "Granted, it is only a detached building, but having one room completely wrecked is a serious matter indeed."

    $ show_sprites(("l 1 sad", "s 1 sad"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_s_001"
    s "..."

    voice "ch1.7_l_001"
    l "..."

    $ show_sprites(("si 1 sad", "s 1 sad"))
    voice "ch1.7_si_001"
    si "..."

    $ show_sprites(("si 1 sad", "k 1 sad"))
    k "..."

    $ show_sprites(("t 1", "k 1 sad"))
    t "..."

    $ show_sprites(("t 1", "m 1 sad"))
    voice "ch1.7_m_001"
    m "..."

    $ show_sprites(("o 1 angry"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_o_003"
    o "I won't understand a thing if you just stay silent, you know."

    th "Even if you say that..."
    th "If I tell the truth, I’ll give Haruna away, so I can't really say anything..."

    voice "ch1.7_o_004"
    o "Judging by the state of the room... Yes, indeed... What exactly happened, Miss Vallière?"

    $ show_sprites(("l 1 sad", "s 1 sad"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_l_002"
    l "Yes! Um, well..."

    th "Hmm, as expected of the Headmaster."
    th "You've figured out at a glance that the magic that destroyed Siesta's room was Louise's, and you're trying to get an explanation or a confession from her!"

    voice "ch1.7_l_003"
    l "During a magic experiment, the magic accidentally went out of control and caused an explosion."

    $ show_sprites(("l 1 sad", "s 1 angry"))
    voice "ch1.7_s_002"
    s "Huh?{#e}"

    $ show_sprites(("l 1 angry", "s 1 angry"))
    voice "ch1.7_l_004"
    l "Saito!? Is something wrong?"

    $ show_sprites(("l 1 angry", "s 1 sad"))
    voice "ch1.7_s_003"
    s "No, it's nothing."

    th "Well, that's true. She can't really say, 'I let magic get out of control out of some inexplicable jealousy.'"

    $ show_sprites(("o 1"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_o_005"
    o "Hmm... an experiment, huh? And you all participated in it too?"

    $ show_sprites(("m 1"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_m_002"
    m "Y-yes."

    $ show_sprites(("k 1", "t 1"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_k_001"
    k "Oh, I was just an observer."

    voice "ch1.7_t_001"
    t "The same."

    $ show_sprites(("si 1 sad"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_si_002"
    si "Well, I..."

    $ show_sprites(("o 1"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_o_006"
    o "Ah... As for the fact that you provided this room, there is no need to trouble yourself with forced explanations."

    th "For some reason, I get the sense that the Headmaster knows it all and is feigning ignorance... Conveniently enough, though."

    voice "ch1.7_o_007"
    o "I am indeed quite curious as to what kind of experiment you were conducting..."

    voice "ch1.7_o_008"
    o "However, if it had been the main building, that would be one thing, but wrecking a commoner's private room is hardly commendable."

    $ show_sprites(("l 1 sad"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_l_005"
    l "I-I'm sorry."

    $ show_sprites(("o 1"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_o_009"
    o "Well, think nothing of it. If it was indeed a magical experiment, then it is, after all, a student's proper duty."

    voice "ch1.7_o_010"
    o "The academy will cover the costs of repairing the room. Make sure to be more careful from now on."

    $ show_sprites(("l 1 happy", "si 1 sad"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_l_006"
    l "Y-yes! Thank you so much!"

    th "What a relief..."

    voice "ch1.7_si_003"
    si "Um... Headmaster. What am I supposed to do while the repairs are underway?"

    $ show_sprites(("o 1 sad"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_o_011"
    o "Hmm? Indeed... I hadn't thought that far ahead."

    th "In that case..."

    menu:
        "Can't something be done, Headmaster?":
            $ show_sprites(("o 1 sad", "s 1 angry"))
            voice "ch1.7_s_004"
            s "Isn't there a way to resolve this, Headmaster?"

            voice "ch1.7_o_012"
            o "Hmm. Let's see..."

            $ show_sprites(("o 1", "s 1 angry"))
            voice "ch1.7_o_013"
            o "May I make that decision?"

            $ show_sprites(("o 1", "si 1"))
            voice "ch1.7_si_004"
            si "Oh, yes. Please do."

            voice "ch1.7_o_014"
            o "Miss Vallière. You're to look after her in your room until the repairs are done."

            $ show_sprites(("o 1", "si 1 shy"))
            voice "ch1.7_si_005-2"
            si "Huh?{#he?}"

            $ show_sprites(("o 1", "l 1 angry"))
            voice "ch1.7_l_007"
            l "H-hold on, Old Osmond! That's going too far, I mean...!"

            voice "ch1.7_o_015"
            o "Hmm? Is there a problem with that?"

            $ show_sprites(("o 1", "l 1 sad"))
            voice "ch1.7_l_008"
            l "Uh, um..."

            voice "ch1.7_o_016"
            o "Now, now, just consider it extra lessons while the repairs are underway."

            voice "ch1.7_l_009"
            l "...Understood."

        "What about Kirche's room?":
            $ show_sprites(("si 1 sad", "s 1"), anim_in="slide_right", anim_out="slide_right")
            voice "ch1.7_s_006"
            s "What about using Kirche's room?"

            $ update_sympathy(-20, char_key="siesta")
            $ show_sprites(("si 1 sad", "k 1 angry"), anim_out="slide_right")
            voice "ch1.7_k_002"
            k "Huh, my room?"

            $ show_sprites(("si 1 sad", "k 4 sad"))
            voice "ch1.7_k_003"
            k "Hmm, it's not a bad idea, but isn't it a bit too intense for her?"

            $ show_sprites(("si 1 shy", "k 4 sad"))
            voice "ch1.7_si_005-3"
            si "Eh? Eh? Eeh?!"
            
            $ show_sprites(("t 1", "k 4 sad"))
            voice "ch1.7_t_002"
            t "...Kirche."

            $ show_sprites(("t 1", "k 1"))
            voice "ch1.7_k_004"
            k "Huh? What's wrong, Tabitha?"

            $ show_sprites(("t 4", "k 1"))
            t "..."

            voice "ch1.7_k_005"
            k "Oh, right. I'm sorry. My room is definitely not a good idea."

            $ show_sprites(("s 3 sad", "k 1"))
            voice "ch1.7_s_007"
            s "Eh, is that so?"

            voice "ch1.7_k_006"
            k "I suppose this girl would find Louise's room much more to her liking than mine, right?"

            $ show_sprites(("si 1 shy", "l 1 angry"), anim_in="slide_right", anim_out="slide_right")
            voice "ch1.7_si_005-4"
            si "Huh?{#he?}"

            voice "ch1.7_l_011"
            "Hey Kirche! What are you talking about?!"

            $ show_sprites(("si 1 shy", "s 3 angry"))
            voice "ch1.7_s_008"
            s "Y-y-yes, that's right, Kirche! I am also in Louise's room, you know!?"

            voice "ch1.7_si_007"
            si "Ah, I don't mind that at all; rather, it is exactly what I desire! But is that really alright?"

            $ show_sprites(("k 4", "s 3 angry"))
            voice "ch1.7_k_007"
            k "It's fine, it's fine. After all, it was Louise who destroyed your room. She really ought to take responsibility."

            $ show_sprites(("k 4", "l 3 angry"))
            voice "ch1.7_l_012"
            l "That's a completely different matter!"

            $ show_sprites(("k 4 happy", "l 3 angry"))
            voice "ch1.7_k_008"
            k "Hehehe, how naive of you, Louise. Do you honestly believe I would stop merely because it's something you'd dislike?"

            $ show_sprites(("s 1", "l 3 angry"))
            voice "ch1.7_s_009"
            s "Well, that's a fair point."

            $ show_sprites(("s 1", "l 1 angry"))
            voice "ch1.7_l_013"
            l "That might be a fair point, but that's exactly why I refuse!"

            $ show_sprites(("o 1", "l 1 angry"))
            voice "ch1.7_o_017"
            o "That's enough, Miss Vallière."

            voice "ch1.7_o_018"
            o "She has nowhere to go and is in quite a predicament. You are to look after her until the repairs are completed."

            $ show_sprites(("o 1", "l 1 sad"))
            voice "ch1.7_l_014"
            l "But...!"

            voice "ch1.7_o_016-2"
            o "Now, now, just consider it extra lessons while the repairs are underway."

            $ show_sprites(("k 4 happy", "si 1"), anim_in="slide_right", anim_out="slide_right")
            voice "ch1.7_k_009"
            k "So with that said, do your best."

            voice "ch1.7_si_008"
            si "Yes! I will do my best!"

            $ show_sprites(("s 3 sad"), anim_in="slide_right", anim_out="slide_right")
            th "What are you talking about...?"

        "You can come to my room.":
            $ show_sprites(("si 1 sad", "s 1"), anim_in="slide_right", anim_out="slide_right")
            voice "ch1.7_s_010"
            s "In that case, you can stay in my room."

            $ show_sprites(("si 1 shy", "s 1"))
            voice "ch1.7_si_005"
            si "Huh?{#he?}"

            $ update_sympathy(20, char_key="siesta")
            $ update_sympathy(-20, char_key="louise")

            $ show_sprites(("si 1 shy", "l 3 angry"))
            voice "ch1.7_l_016"
            l "Hey Saito! What are you talking about?!"


            $ show_sprites(("si 1 sad", "l 3 angry"))
            voice "ch1.7_si_009"
            si "But, but is that really okay?"

            $ show_sprites(("si 1 sad", "s 1 happy"))
            voice "ch1.7_s_011"
            s "Come on, it's fine. After all, my master is the one who wrecked Siesta's room, right?"

            $ show_sprites(("l 3 angry", "s 1 happy"))
            voice "ch1.7_l_017"
            l "That's a completely different issue! And for the record, it's my room, not yours!"

            voice "ch1.7_s_012"
            s "Well, you could say that."

            $ show_sprites(("l 1 angry", "s 1 happy"))
            voice "ch1.7_l_018"
            l "What's with this calm response! I'm the owner of this room! You're just the familiar!"

            voice "ch1.7_l_019"
            l "My familiar shouldn't bring other people into the room without my permission!"

            $ show_sprites(("l 1 angry", "o 1"))
            voice "ch1.7_o_017-2"
            o "That's enough, Miss Vallière."

            voice "ch1.7_o_018-2"
            o "She has nowhere to go and is in quite a predicament. You are to look after her until the repairs are completed."

            $ show_sprites(("l 1 sad", "o 1"))
            voice "ch1.7_l_014-2"
            l "But...!"

            voice "ch1.7_o_016-3"
            o "Now, now, just consider it extra lessons while the repairs are underway."

            l "...Understood."
            voice "ch1.7_l_015"

    $ show_sprites(("si 1 happy"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_si_006"
    si "Ah, um! Forgive my impertinence, but I’m counting on you both. Mr. Saito! Miss Vallière!"

    $ show_sprites(("l 1 sad", "s 1 happy"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.7_s_005"
    s "Ah, aah... likewise..."

    voice "ch1.7_l_010"
    l "..."

    th "I just hope nothing goes wrong..."

    jump ch1_8
    return