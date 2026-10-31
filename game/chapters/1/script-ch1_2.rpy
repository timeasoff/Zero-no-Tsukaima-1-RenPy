# siesta's room night
label ch1_2:
    call overlay_screen("yard_night",  "Tristain Academy of Magic") from _call_overlay_screen_6
    pause(2)
    $ fade_fx("ha_sick", new_music="t28", type="cg")

    th "In the end, Siesta kindly let us keep the girl we'd brought back hidden in her room."
    th "Since calling a doctor was out of the question, we decided to have Montmorency examine her."

    $ fade_fx("si_room_night", sprites=("m 1", "s 1"))
    pause(0.2)

    voice "ch1.2_s_001"
    s "Hey, how'd it go? Is she hurt anywhere? Any signs of illness? Nothing... serious, right?"

    voice "ch1.2_m_001"
    m "Saito, calm down. I gave her a quick check-up, and there's nothing particularly wrong. I think she's just exhausted from built-up fatigue."

    voice "ch1.2_m_002"
    m "Wouldn't it be fine to just let her sleep like this?"

    voice "ch1.2_s_002"
    s "I see... That's a relief. Thanks, Monmon."

    $ show_sprites(("m 1 angry", "s 1"))
    voice "ch1.2_m_003"
    m "My name is Montmorency! I've told you not to make up weird nicknames for me!"

    $ show_sprites(("m 1"), mode="big")

    th "Montmorency is Louise's classmate. She specializes in water magic. Her nickname is \"Montmorency the Fragrance.\""
    th "I call her Monmon, but she doesn't seem too fond of the nickname"

    $ show_sprites(("m 1", "s 1 sad"))

    voice "ch1.2_s_003"
    s "Ah, yeah. But seriously, thanks."

    voice "ch1.2_m_004"
    m "You're welcome. It's not like I'm under any obligation to do this, but I simply can't abandon someone who's sick."

    $ show_sprites(("l 1", "s 1 sad"))
    voice "ch1.2_l_001"
    l "Anyway, Siesta. I apologize for dragging a sick person into the room without warning."

    $ show_sprites(("l 1", "si 1"))

    voice "ch1.2_si_01"
    si "Oh, it's quite alright. Please don't worry about it, Miss Vallière. After all, it's for the sake of helping someone in need."

    $ show_sprites(("si 1"), mode="big")
    
    th "Siesta is a maid working at this academy. She feels a sense of kinship with me since we're both commoners."
    th "She's kind, great at cooking... I wish my master would take a page out of her book."

    $ show_sprites(("l 1", "si 1"))
    $ show_sprites(("l 1", "si 4 shy"))

    voice "ch1.2_si_02"
    si "Besides... it's what Saito asked for."

    $ show_sprites(("l 1 angry", "si 4 shy"))
    voice "ch1.2_l_002"
    l "...I see."

    $ show_sprites(("l 1 angry", "m 1 sad"))
    voice "ch1.2_m_005"
    m "But this girl... I don't recognize her from the academy. Just where on earth did you pick up this commoner?"

    $ show_sprites(("l 1", "m 1 sad"))
    voice "ch1.2_l_003"
    l "Eh?"
    
    $ show_sprites(("l 1", "m 1 angry"))
    voice "ch1.2_m_006"
    m "Don't just 'eh' at me. I'll have you know I remember the faces of almost all the commoners working at the academy."
    voice "ch1.2_m_007"
    m "Listen... Saito. Where exactly did you bring this girl from?"

    $ show_sprites(("l 1", "s 1 sad"))
    voice "ch1.2_s_004"
    s "Uh, um..."

    $ result = None
    menu:
        "Blame it on Louise":
            $ show_sprites(("l 1", "s 3 happy"))
            voice "ch1.2_s_005"
            s "Um... Louise, what was our story again?"

            $ show_sprites(("l 3", "s 3 happy"))
            voice "ch1.2_l_004"
            l "Um, th-that's right! I met her today when I went out to town. Apparently, she's a commoner from my hometown!"

            $ update_sympathy(10)
            $ tndl(30)

            voice "ch1.2_l_005"
            l "She said her purse was stolen on the way and she had nowhere to go, so I thought I'd take her in for a while."

            $ show_sprites(("m 4 sad", "s 3 happy"))

            voice "ch1.2_m_008"
            m "Hmm... Well, she certainly does look terribly exhausted. If that's the case, I suppose it can't be helped."

            th "Nice one, Louise!"
            
        "Try to cover it up yourself":
            $ show_sprites(("l 1", "s 3 sad"))
            voice "ch1.2_s_007"
            s "Um, um, y-yeah, that's right! I ran into her in town, and she looked like she was going through a lot, so I just brought her along!"

            $ tndl(-30)

            $ show_sprites(("m 1 sad", "s 3 sad"))
            voice "ch1.2_m_014"
            m "Is that so? But bringing a commoner along so suddenly like that is quite improper, you know."

            $ show_sprites(("m 1 sad", "s 3 happy"))
            voice "ch1.2_s_011"
            s "Hahaha. I'm such a naughty boy, huh..."

            $ show_sprites(("m 4 sad", "s 3 happy"))
            voice "ch1.2_m_015"
            m "...Well, I'll do you the favor of just leaving it at that."
            

        "Blame it on Siesta":
            $ show_sprites(("l 1", "s 3 sad"))
            voice "ch1.2_s_006"
            s "Um... Siesta, what was our story again?"

            $ show_sprites(("si 1 angry", "s 3 sad"))
            voice "ch1.2_si_03"
            si "Um, y-yes, that's right! She's a distant relative from my home village."

            $ update_sympathy(10, char_key="siesta")
            $ show_sprites(("si 1", "s 3 sad"))
            voice "ch1.2_si_04"
            si "She ran away from home, so I figured I'd let her stay for a few days."


            $ show_sprites(("m 4 angry", "s 3 sad"))
            voice "ch1.2_m_016"
            m "Hmm... Well, I suppose you're right. You two do have the exact same eye color and everything. If she really is a relative, then I suppose it can't be helped."

            $ show_sprites(("m 4 angry", "s 3 happy"))

            th "Thank you, Siesta!"
            
    voice "ch1.2_m_009"
    m "For now, just let her get some rest. I doubt her condition will change anytime soon, but let me know if anything happens."

    $ show_sprites(("m 4 sad", "s 1"))

    voice "ch1.2_s_008"
    s "Yeah. I owe you one, Monmon."

    $ show_sprites(("m 1 angry", "s 1"))
    voice "ch1.2_m_010"
    m "I told you, it's Montmorency!"

    $ show_sprites(("m 1", "s 1"))
    voice "ch1.2_s_009"
    s "So... I have a favor to ask."

    voice "ch1.2_m_011"
    m "What is it?"

    $ show_sprites(("m 1", "s 3 sad"))
    voice "ch1.2_s_010"
    s "Actually, I'd like to keep her presence here a secret from the others at the academy."

    $ show_sprites(("m 1 angry", "s 3 sad"))
    voice "ch1.2_m_012"
    m "A secret? Why should I have to promise you anything?!"

    $ show_sprites(("m 1 angry", "l 3 sad"))
    voice "ch1.2_l_006"
    l "Montmorency, I'm asking you too... could you please keep this a secret?"

    $ show_sprites(("m 1", "l 3 sad"))

    voice "ch1.2_m_013"
    m "...Well, fine. I'll keep your secret. Now then, I'm heading back to my room."

    $ show_sprites(("si 1", "l 3 sad"))
    voice "ch1.2_si_05"
    si "That's a relief. Saito-san, Miss Variere."

    $ show_sprites(("si 1", "s 3"))
    voice "ch1.2_s_012"
    s "Well, at least her life isn't in danger, right? That's a relief."

    th "But could she really be Takanagi-san? If that's the case... how did she end up in this world..."
    th "Well, once she wakes up, I'll be able to figure everything out..."

    $ show_sprites(("l 1 sad", "s 3"))
    voice "ch1.2_l_007"
    l "Now we just have to hope she wakes up... I wonder what we should do?"

    $ show_sprites(("si 1", "s 3"))
    voice "ch1.2_si_06"
    si "I'll stay here and look after her. You two should get some rest now."

    voice "ch1.2_s_013"
    s "Is that so? Sorry about that, Siesta. I'm causing you a lot of trouble."

    $ show_sprites(("l 1 sad", "s 3"))
    voice "ch1.2_l_008"
    l "Really, I know I'm causing you extra trouble because of Saito, but I'm counting on you."

    $ show_sprites(("si 4 shy", "s 3"))
    voice "ch1.2_si_07"
    si "It's really no trouble at all. I'm just glad I can be of help to Saito-san."

    $ show_sprites(("si 4 shy", "s 3 shy"))
    voice "ch1.2_s_014"
    s "Huh? Ah, th-thanks..."

    $ show_sprites(("l 1 angry", "s 3 shy"))
    voice "ch1.2_l_009"
    l "Come on, Saito! Siesta went out of her way to be nice about it, so we're heading back to the room!"

    ## тряска и персонажи исчезают
    $ hit_fx(sound=None)
    $ show_sprites(None, anim="slide_right") 

    voice "ch1.2_s_015"
    s "Hey, wait! Don't pull me so hard! Ow, ow, ow! I said it hurts!"

    jump ch1_3
    return
        


