# Харуна пробудилась
label ch1_6:
    $ fade_fx("si_room", new_music="t18", sprites=("ha 1 sad", "s 1"))

    voice "ch1.6_s_001"
    s "H-hey, where did you come from? What's your name?"

    voice "ch1.6_ha_001"
    unk_ha "Huh?!"

    voice "ch1.6_s_002"
    s "Are you from the same world as me? Are you Japanese too? Could you possibly be one of my classmates?"

    voice "ch1.6_ha_002"
    unk_ha "Ah, um, wait a moment..."
    
    voice "ch1.6_k_001"
    unk_k "Honestly, Darling. Bombarding a woman with questions all at once is a total no-no."

    $ show_sprites(("ha 1 sad", "s 1 sad"))
    voice "ch1.6_s_003"
    s "Eh?{#e?}"

    $ show_sprites(("k 1 happy", "s 1 sad"))
    voice "ch1.6_k_002"
    k "Be gentler. A man must elegantly lead a woman, you know."

    $ show_sprites(("k 1 happy", "s 3 sad"))
    voice "ch1.6_s_004"
    s "I-is that so? I'll be careful."

    $ show_sprites(("k 1 happy", "s 3 angry"))
    voice "ch1.6_s_005"
    s "Hold on a second! Hey, Kirche. What are you doing here?"

    voice "ch1.6_k_003"
    k "Oh, please, I'm not the only one, you know. See?"

    voice "ch1.6_s_006"
    s "Eh?"

    $ show_sprites(("t 1", "m 1"),  anim_in="slide_right", anim_out="slide_right")
    t "..."

    voice "ch1.6_m_001"
    m "Umm... Ah, right, right. Looks like she's doing well now."

    $ show_sprites(("l 3 angry", "s 3 sad"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.6_l_001"
    l "Why have so many people gathered here since this morning!"

    $ show_sprites(("k 1", "t 1"),  anim_in="slide_right", anim_out="slide_right")

    th "Kirche and Tabitha are Louise's classmates, having arrived as exchange students from Germania and Gallia, respectively."

    $ show_sprites(("k 1"), mode="big", anim_in="slide_right", anim_out="slide_right")
    th "Kirche excels in the fire element of magic. She is known as 'Kirche the Ardent'."
    th "She and Louise are simply on bad terms because of some ongoing friction over family lineage or place of origin."
    $ show_sprites(("t 1"), mode="big", anim_in="slide_left", anim_out="slide_left")
    th "Tabitha excels in the wind element of magic. She is known as 'Tabitha the Snowstorm'."
    th "Always taciturn and devoid of expression. What goes on in her mind is a mystery. Yet, she and Kirche are surprisingly close..."
    
    $ show_sprites(("k 1", "t 1"))
    th "Kirche being curious is one thing, but it's rare for Tabitha, who is always quietly reading a book, to actually show up."
    th "I wonder why they came here..."

    menu:
        "Ask Tabitha":
            $ show_sprites(("s 3 sad", "t 1"))
            voice "ch1.6_s_007-2"
            s "Hey, Tabitha. Why are you here?"

            voice "ch1.6_t_001"
            t "...I asked Montmorency, and Kirche brought me here."

            $ update_sympathy(15, char_key="tabitha")
            $ tndl(-30)

            voice "ch1.6_s_010"
            s "Thank you for the clear answer."

            voice "ch1.6_t_002"
            t "...But I do have an interest."

            voice "ch1.6_s_011"
            s "Oh, really?"

        "Ask Siesta":
            $ show_sprites(("si 1 sad", "s 3 sad"), anim_out="slide_right", anim_in="slide_right")
            voice "ch1.6_s_007-3"
            s "Hey, Siesta. Why are there so many people here?"
            
            voice "ch1.6_si_001"
            si "I-I don't know either."

            $ update_sympathy(10, char_key="siesta")
            $ tndl(-30)
            
            voice "ch1.6_s_012"
            s "Huh? Weren't you there when we came to call for you?"
            
            voice "ch1.6_si_002"
            si "Yes. I did let Miss Montmorency know, but as for everyone else, absolutely nothing..."
            
            $ show_sprites(("si 1 sad", "l 1 angry"))
            voice "ch1.6_l_006"
            l "So that leaves only one possible answer, doesn't it? Say, Montmorency?"
            
            $ show_sprites(("m 4 happy", "l 1 angry"))
            voice "ch1.6_m_002"
            m "...Hohoho."
            
            $ show_sprites(("k 1", "l 1 angry"))
            voice "ch1.6_k_004"
            k "Now, now. I don't know the circumstances, but it seems like it's turning into something fun, doesn't it?"
            
            voice "ch1.6_l_007-2"
            l "There's nothing fun about it, really."

            $ show_sprites(("t 1", "l 1 angry"))
            voice "ch1.6_t_002-2"
            t "...But I do have an interest."

            $ show_sprites(("t 1", "s 3 sad"))
            voice "ch1.6_s_011-2"
            s "Oh, really?"
            
        "Ask Louise":
            $ show_sprites(("l 3 angry", "s 3 sad"), anim_out="slide_right", anim_in="slide_right")
            voice "ch1.6_s_007-4"
            s "Hey, Louise. Why are there so many people here?"

            voice "ch1.6_l_002"
            l "As if I'd know, considering I came here with you!"

            voice "ch1.6_s_008"
            s "Yeah, that's a perfectly valid point, but I thought that perhaps only Louise could share this feeling of having nowhere to turn."

            voice "ch1.6_l_003"
            l "Well, I suppose that's true. But I know what the cause is."

            $ update_sympathy(10, char_key="louise")
            $ tndl(30)

            voice "ch1.6_s_009"
            s "Eh?{#e?}"

            $ show_sprites(("l 3", "s 3 sad"))
            voice "ch1.6_l_004"
            l  "Tell me, Siesta. It wasn't this bustling before you came to fetch us, was it?"

            $ show_sprites(("l 3", "si 1 sad"))
            voice "ch1.6_si_002-2"
            si "Yes. I did let Miss Montmorency know, but as for everyone else, absolutely nothing..."

            $ show_sprites(("l 3 angry", "si 1 sad"))
            voice "ch1.6_l_006-2"
            l "So that leaves only one possible answer, doesn't it? Say, Montmorency?"

            $ show_sprites(("l 3 angry", "m 4 happy"))
            voice "ch1.6_m_002-2"
            m "...Hohoho."

            $ show_sprites(("k 1", "t 1"), anim_out="slide_right", anim_in="slide_right")
            voice "ch1.6_k_005"
            k "Well, why not. Depending on what we're dealing with, we can give a hand too."

            t "..."

        "Ask Kirche":
            $ show_sprites(("k 1", "s 3 sad"))

            voice "ch1.6_s_007"
            s "Hey, Kirche. Why are you here?"

            voice "ch1.6_k_006"
            k "Oh, there's no particular reason, really."

            $ update_sympathy(10, char_key="kirche")
            $ tndl(-30)

            voice "ch1.6_k_007"
            k "I heard you and Louise were doing something amusing, so I just dropped by to see for myself."

            voice "ch1.6_s_013"
            s "Heard it...? From whom?"

            $ show_sprites(("k 1", "l 3 angry"))
            voice "ch1.6_l_006-3"
            l "It goes without saying, doesn’t it? Say, Montmorency?"
            
            $ show_sprites(("k 1", "m 4 happy", "l 3 angry"), center_front=True)
            voice "ch1.6_m_002-3"
            m "...Ohohoho."

            $ show_sprites(("k 1", "l 3 angry"))
            voice "ch1.6_k_004-2"
            k "Now, now. I don't know the circumstances, but it seems like it's turning into something fun, doesn't it?"
            
            voice "ch1.6_l_007"
            l "There's nothing fun about it, really."

            $ show_sprites(("l 1"))

    $ show_sprites(("l 1"), anim_out="slide_right")
    voice "ch1.6_l_005"
    l "Well, fine. It's like talking to a brick wall. I don't think any of you are leaving."
    
    voice "ch1.6_l_008"
    l "More importantly, the problem is who this girl is."

    $ show_sprites(("l 1", "ha 1 sad"))
    voice "ch1.6_ha_003"
    unk_ha "Umm…? Excuse me, what on earth am I doing here…?"
    
    th "She looks bewildered, unable to make sense of what's going on. Not surprising, though."
    
    $ show_sprites(("l 1", "s 1"))
    voice "ch1.6_s_014"
    s "Well, let's see... To explain, Louise and I found you collapsed on the outskirts of town yesterday and brought you here."
    
    voice "ch1.6_l_009"
    l "Incidentally, Siesta is the one who laid you in bed, and Montmorency examined you."
    
    $ show_sprites(("l 1", "ha 1 happy"))
    voice "ch1.6_ha_004"
    unk_ha "Oh, s-so that's how it was? My apologies, and thank you so much."
    
    $ show_sprites(("si 1", "ha 1 happy"))
    voice "ch1.6_si_003"
    si "Ah, no, I didn't really do anything..."
    
    $ show_sprites(("m 1", "ha 1 happy"))
    voice "ch1.6_m_003"
    m "Since you seemed exhausted, I simply instructed you to stay in bed and rest. That’s all I did."
    
    $ show_sprites(("l 1", "ha 1 happy"))
    voice "ch1.6_l_010"
    l "Now, I’d like to ask you something. Where do you come from? What’s your name?"
    
    $ show_sprites(("l 1", "ha 1"))
    voice "ch1.6_ha_005"
    unk_ha "Y-yes. I am Haruna... Haruna Takanaqi."
    
    $ show_sprites(("s 1 happy", "ha 1"))
    voice "ch1.6_s_015"
    s "Just as I thought, Takanaqi-san..."
    
    voice "ch1.6_ha_006"
    ha "You know about me? Saito... could you possibly be Hiraga Saito-kun?"
    
    voice "ch1.6_s_016"
    s "Ah, that's right, I'm Saito Hiraga. It’s been a while, Takanaqi-san."
    
    $ show_sprites(("s 1 happy", "ha 1 happy"))
    voice "ch1.6_ha_007"
    ha "I'm so happy... To think we'd meet in a place like this!!"
    
    $ show_sprites(("l 1 angry", "ha 1 happy"))
    voice "ch1.6_l_011"
    l "I knew it! So you already know Saito!"
    
    voice "ch1.6_ha_008"
    ha "Yes. I shared a class with Saito-kun and acted as our class president."
    
    voice "ch1.6_l_012"
    l "Well, never mind. So, how did you get here?"
    
    $ show_sprites(("l 1 angry", "ha 1"))
    voice "ch1.6_ha_009"
    ha "How... well, even if you ask me how... Out of nowhere, on a perfectly normal day, a round, mirror-like thing just appeared right before my eyes..."
    
    voice "ch1.6_ha_010"
    ha "The moment I touched it, it seems I ended up in this world."
    
    th "A round mirror... The same as what happened to me."
    
    voice "ch1.6_ha_011"
    ha "I had no idea where I was and was completely at a loss, when a woman who just happened to pass by stopped to help me..."
    
    voice "ch1.6_l_013"
    l "But...?"
    
    voice "ch1.6_ha_012"
    ha "They put me in a locked room and shut me inside, just like that..."
    
    $ show_sprites(("l 1 sad", "ha 1"))
    voice "ch1.6_l_014"
    l "Oh? That sounds like a rather grim tale, don't you think?"
    
    $ show_sprites(("k 1 sad", "ha 1"))
    voice "ch1.6_k_008"
    k "By all logic, that woman should be the mage who summoned the girl, but I can't say for certain."
    
    voice "ch1.6_ha_013"
    ha "Since I was kept confined all that while, I seized an opportunity to slip away. However..."
    
    $ show_sprites(("l 1", "ha 1"))
    voice "ch1.6_l_015"
    l "With no acquaintances and nowhere to head to, you were simply wandering aimlessly... I guess you probably would've passed out eventually."
    
    voice "ch1.6_ha_014"
    ha "Y-yes."
    
    $ show_sprites(("l 1", "si 1"))
    voice "ch1.6_si_004"
    si "And it was you two who rescued her at that point. What incredible luck she had, honestly."
    
    #! перекрывает морду сиесты. надо в рамки впихать cg изображения
    $ fade_fx("ha_hug", new_music="t29", type="cg")
    pause(0.2)
    $ shake_fx("ha_hug", type="cg")
    pause(0.2)

    voice "ch1.6_ha_015"
    ha "Ugh... Hiraga-kun!"
    
    voice "ch1.6_s_017"
    s "Whoa!?"
    
    $ dissolve_fx("ha_hug_2", duration=1, type="cg")
    voice "ch1.6_si_005"
    si "Wah!?"
    
    $ dissolve_fx("ha_hug_3", duration=1, type="cg")
    #! скорее всего реплика другая от уровня симпатии 
    #! использовать ch1.6_l_016_2
    voice "ch1.6_l_016"
    l "W-what is the meaning of this?! Why are you suddenly clinging to my familiar like that?! Get away from him!"
    
    voice "ch1.6_ha_016"
    ha "A familiar? What exactly is a 'familiar'? Hiraga-kun is a perfectly normal human being!"
    
    voice "ch1.6_ha_017"
    ha "To call him a familiar like that... Who do you think you are?!"
    
    $ fade_fx("si_room", new_music="t27", sprites=("l 1 angry", "ha 1 angry"))
    voice "ch1.6_l_017"
    l "Urgh!"

    $ show_sprites(("k 1 sad", "ha 1 angry"))
    voice "ch1.6_k_009"
    k "Well, normally, one wouldn't think that a human is being used as a familiar."
    
    $ show_sprites(("l 3 angry", "ha 1 angry"))
    voice "ch1.6_l_018"
    l "Bystanders, stay quiet!"
    
    $ show_sprites(("l 3", "ha 1 angry"))
    voice "ch1.6_l_019"
    l "Um, this is an extremely unusual situation, but... I called Saito forth with the magic used to summon familiars, and we established a contract."
    
    voice "ch1.6_l_020"
    l "So, even though Saito is human, he’s still my familiar. See? He has the familiar’s rune on his left hand."
    
    $ show_sprites(("l 3", "ha 1"))
    voice "ch1.6_ha_018"
    ha "...That much I understand."
    
    $ show_sprites(("l 3", "ha 1 angry"))
    voice "ch1.6_ha_019"
    ha "I understand that, but... You have no right to interfere with me hugging Hiraga-kun!"
    
    $ show_sprites(("l 3 angry", "ha 1 angry"))
    voice "ch1.6_l_021"
    l "What did you just say?!{#ver2}"
    
    voice "ch1.6_ha_020"
    ha "Hiraga-kun is the only acquaintance I have met since coming to this world. What's wrong with being happy about our reunion!?"
    
    $ show_sprites(("l 3 sad", "ha 1 angry"))
    voice "ch1.6_l_022"
    l "I-It's not exactly wrong, but there's a problem with the way you're expressing it..."
    
    voice "ch1.6_ha_021"
    ha "What’s so wrong with a hug?! It’s truly strange to get so upset merely because someone embraced your familiar!"
    
    $ show_sprites(("l 3 sad", "ha 1 happy"))
    voice "ch1.6_ha_022"
    ha "Also, feel free to call me Haruna, Hiraga-kun."

    $ show_sprites(("s 3 happy", "ha 1 happy"))
    voice "ch1.6_s_018"
    s "Ah, yeah... Haruna, huh..."

    $ show_sprites(("l 1 angry", "ha 1 happy"))
    voice "ch1.6_l_023"
    l "Wha—?!"

    $ show_sprites(("k 1 happy", "ha 1 happy"))
    voice "ch1.6_k_010"
    k "Well, that’s a fair point. Besides, it doesn't matter who hugs Darling, there's nothing wrong with that!"

    $ fade_fx("k_hug", new_music="t29", type="cg")
    pause(0.2)
    $ shake_fx("k_hug", type="cg")
    pause(0.2)

    voice "ch1.6_s_019"
    s "Huh?!{#var2}"

    voice "ch1.6_k_011"
    k "See? Just like this."
    
    voice "ch1.6_l_024"
    l "W-w-what the—?!"

    voice "ch1.6_si_006"
    si "I-I won't lose either!"
    
    #! сцена не помещается нужно сделать виньетку и уменьшить размер через bg_border
    $ dissolve_fx("butterbrot", duration=1, type="cg")
    pause(0.2)
    $ shake_fx("butterbrot", type="cg")
    pause(0.2)

    voice "ch1.6_s_020"
    s "Ohaa!?"

    th "Wh-what is going on here!? I'm surrounded by something soft and warm... This is, this situation is......!"
    
    voice "ch1.6_t_003"
    t "...Hell on earth."

    voice "ch1.6_s_021"
    s "Aah! Tabitha, when did you get into the corner of the room!?"

    voice "ch1.6_l_025"
    l "...Saito. Please, step away from those women immediately."

    voice "ch1.6_s_022"
    s "She says to get away..."
    
    menu:
        "Yeah.{#v2}":
            voice "ch1.6_s_023"
            s "Yes, right away."
            $ tndl(30)

            voice "ch1.6_ha_023"
            ha "No! And here I was, so happy to finally meet Hiraga-kun again...!"

            $ shake_fx("butterbrot", sound=None, type="cg")
            $ update_sympathy(-10, char_key="haruna")

            voice "ch1.6_si_007"
            si "If we back off now, we lose!"

            $ shake_fx("butterbrot", sound=None, type="cg")
            $ update_sympathy(-10, char_key="siesta")

            voice "ch1.6_k_012"
            k "Ohoho! If you can pull away, then go ahead and try! Look, look!"

            $ shake_fx("butterbrot", sound=None, type="cg")
            $ update_sympathy(-10, char_key="kirche")

            voice "ch1.6_s_024"
            s "Whoa! It feels like I'm surrounded by marshmallows, and they just won't let go of my face and body!"

            $ fade_fx("ready_to_blow", type="cg")
            voice "ch1.6_l_027"
            l "Fufufu, fufufu... I see. So you’ve decided to simply shamelessly embrace this, have you, Saito?"

        "Nope.":
            voice "ch1.6_s_025"
            s "No, that is impossible, Master."
            
            voice "ch1.6_l_026"
            l "What did you just say?!{#ver3}"
            $ tndl(-30)

            voice "ch1.6_s_026"
            s "No, look closely! I can't move a muscle, even if I wanted to get away!"

            voice "ch1.6_ha_024"
            ha "Hiraga-kun...~"
            $ update_sympathy(10, char_key="haruna")

            voice "ch1.6_si_008"
            si "Saito-san!"
            $ update_sympathy(10, char_key="siesta")

            voice "ch1.6_k_013"
            k "Vallière. You’ve lost. There isn't even a gap left to hug him now."
            $ update_sympathy(10, char_key="kirche")

            $ fade_fx("ready_to_blow", type="cg")
            voice "ch1.6_l_027-2"
            l "Fufufu, fufufu... Ah, I see. So Saito has absolutely no intention of pulling away?"

            voice "ch1.6_s_027"
            s "No, it's not that I don't want to pull away, it's that they won't let me go, do you understand!?"

    voice "ch1.6_l_028"
    l "Fine!!! Then I'll force you away from them!!"
    
    voice "ch1.6_s_028"
    s  "W-wait a minute! If you use magic in a place like this...!"

    voice "ch1.6_l_029"
    l "Words are useless!!"
    $ flash_fx("white", duration=1)
    pause(0.5)
    # Взрыв
    play sound blow_2
    pause(1)

    voice "ch1.6_s_029"
    s "Gwaaah!!"

    $ flash_fx("sky", type="cg")
    hide white

    voice "ch1.6_t_004"
    t "The damage is extensive..."

    jump ch1_7
    return