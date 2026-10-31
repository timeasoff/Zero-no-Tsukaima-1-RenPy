# Лес

label forest_battle:
    call screen battle_menu
    
    if _return == "start_battle":
        # Initialize battle state
        $ init_battle(["mage", "mage"])
        
        # Show battle screen and get result
        call screen battle_screen
        
        if _return == "victory":
            return 
        elif _return == "defeat":
            "Game Over..."
            
    elif _return == "cancel":
        "test"
        # action Rollback()
    return

# forest
label ch1:
    $ tndl(None)
    call overlay_screen("overlay",  "Chapter One: \"Louise of Zero\"", isUseBlur=False, text_mode="black") from _call_overlay_screen_4
    pause(2)
    $ dissolve_fx("forest", new_music="t18")
    
    call overlay_screen("forest",  "The Road (Highway)") from _call_overlay_screen_5
    pause(1)
    $ dissolve_fx("l_s_forest", type="cg")

    l "....."
    voice "ch1_s_001"
    s "…Hey, Louise-san, can you hear me?"

    voice "ch1_l_001"
    l "What?"

    voice "ch1_s_002"
    s "I was wondering…"

    $ dissolve_fx("l_s_forest_l_speak", type="cg")

    voice "ch1_l_002"
    l "…go ahead and say it."

    voice "ch1_s_003"
    s "If I recall correctly, this morning you said, {i}'It's been forever since I've gone out shopping in town on a day off!'{/i}"

    voice "ch1_s_004"
    s "…or something along those lines, didn't you say? I seem to recall it sounded like you were having quite a bit of fun."

    $ dissolve_fx("l_s_forest", type="cg")

    voice "ch1_l_003"
    l "I wonder if something like that really happened..."

    $ dissolve_fx("l_s_forest_s_speak", type="cg")

    voice "ch1_s_005"
    s "No, no, no, of course I'm curious! You seemed to be having so much fun back then—why on earth are you in such a bad mood now?"

    voice "ch1_l_004"
    l "Well, of course YOU had a great time. You were going all lovey-dovey with every girl in sight..."

    voice "ch1_l_005"
    l "Really, nothing could be more unseemly!"

    $ dissolve_fx("l_s_forest", type="cg")

    voice "ch1_s_006"
    s "I wasn't being all lovey-dovey or anything! Wait… could it be you're jealous?"

    $ dissolve_fx("l_s_forest_l_speak", type="cg")

    voice "ch1_l_006"
    l "Th-th-that's ridiculous, of course not!"

    voice "ch1_l_007"
    l "If my stupid familiar goes around causing trouble everywhere, it'll reflect badly on me—your master! It's not like I'm jealous or anything, okay!"

    $ dissolve_fx("l_s_forest_s_speak", type="cg")
    
    voice "ch1_s_007"
    s "Is that so, huh?"

    voice "ch1_l_008"
    l "That's exactly right!"

    $ fade_fx("forest")

    $ show_sprites("s 1", mode="big")

    th "My name is Hiraga Saito. I was supposed to be just an ordinary high school student... or so I thought."
    $ show_sprites("l 1", mode="big")
    th "But now, I'm with this willful master — Louise Françoise Le Blanc de La Vallière..."
    th "Long story short: thanks to Louise's summoning spell, I — who got called here as a familiar — am now living in her room."
    $ fade_fx("sky", type="cg")

    th "In another world, \"Halkeginia\", where mages rule the land as nobility... It was a world entirely unlike Japan."
    th "What's more, the country we live in—Tristain—suddenly came under invasion from \"Reconquista\"."
    th "Using the Zero fighter found in Siesta's hometown and the power of Louise's \"Void\" magic, we somehow managed to repel Reconquista's massive fleet."
    th "Having suffered devastating losses, Reconquista won't be launching another invasion anytime soon."
    th "Well, I guess this is what they call a fleeting moment of peace…"
    th "But when will I ever be able to return to Japan..."
    th "Well, I guess it'll all work out somehow… It's always been like that up to now, anyway…"
    th "Then again, my lower back really aches… I still haven't gotten used to riding a horse…"

    $ fade_fx("l_s_forest", type="cg")

    voice "ch1_s_008"
    s "Still, she went on a bit of a weird clothes-shopping spree this time. And it takes forever to pick anything out... Honestly, I was just killing time the whole way through..."

    $ fade_fx("l_s_forest_l_speak", type="cg")

    voice "ch1_l_009"
    l "W-well, it's not like it's a bad thing! What's so wrong with me dressing up!?"

    th "Louise actually looks really nice..."

    # ==== CHOISE 1 ====
    $ choise_result = None
    menu:
        "I thoughts it's good!":
            $ choise_result = "good"
        "I don't care.":
            $ choise_result = "neutral"
        "It's terrible!":
            $ choise_result = "bad"

    if choise_result == "good":

        voice "ch1_s_009"
        s "I thoughts it's great! You've got good looks to begin with. So paying more attention to your appearance is totally fine."

        $ dissolve_fx("l_s_forest", type="cg")

        voice "ch1_l_010"
        l "I-is that so...?"

        $ update_sympathy(10)
        $ tndl(30)

        voice "ch1_s_010"
        s "But why do girls take so long just picking out clothes? I just don't get it at all..."
    elif choise_result == "neutral": 

        ## симпатия луизы не меняется

        voice "ch1_s_011"
        s "Either one's fine. It's got nothing to do with me, anyway."

        voice "ch1_s_012"
        s "Just one thing though: don't go dumping any extra hassle on me, alright?"
    elif choise_result == "bad":

        $ dissolve_fx("l_s_forest_s_speak", type="cg")
        voice "ch1_s_013"
        s "Of course it's no good, right? Do you really want to dress up so badly that you'd go to the trouble of putting me through all this, huh?"

        $ update_sympathy(-10)
        $ tndl(-30)
    else:
        "ERR"

    #$ show_sympathy_hud()

    ## louise shows tsun-tsun side in any case :)

    $ dissolve_fx("l_s_forest_l_speak", type="cg")

    voice "ch1_l_011"
    l "Ugh, what is it, what is it?! You've done nothing but complain this whole time! Hello? You're my familiar, aren't you? So stop whining and get to work!"

    voice "ch1_l_012"
    l "For one thing, I go out of my way to try on clothes at the shop, and you can't even bother to look properly—or tell me what you think!"

    voice "ch1_s_014"
    s "Hm? What was that?"

    voice "ch1_l_013"
    l "It's nothing, really! I've been making sure you eat properly these days, so the least you can do is obediently listen to your master!"

    voice "ch1_s_015"
    s "Yeah yeah, sure thing~"
    $ dissolve_fx("l_s_forest", type="cg")
    th "Jeez... She's got such a cute look going for her. If only her personality had even a tiny bit of that same charm, I wouldn't have a single complaint..."
    $ dissolve_fx("l_s_forest_l_speak", type="cg")

    voice "ch1_l_014"
    l "Did you say something!?"

    voice "ch1_s_016"
    s "N-no, nothing at all!"

    $ fade_fx("forest")

    $ show_sprites("d 1 happy")
    pause(0.2)
    voice "ch1_d_001"
    d "Hah hah haa! Still getting bossed around by her, huh, partner?"

    $ show_sprites(("l 3 angry", "d 1"))
    voice "ch1_l_015"
    l "I do NOT boss him around!"

    $ show_sprites(("l 3 angry", "d 1", "s 3 angry"))
    voice "ch1_s_017"
    s "I'm NOT being bossed around, okay?!"

    $ show_sprites("d 1", mode="big", anim="slide")

    th "This is Derflinger. As you can see, a talking sword. Well, he's my partner, I guess."
    th "It's good that he told me I'm the legendary familiar 'Gandálfr', but he just won't give me any details."
    th "Partner says he's simply forgotten everything, but... I wonder if he'll remember anything at all..."

    $ show_sprites("d 1 happy")
    voice "ch1_d_002"
    d "Well, well, you two are getting along nicely, huh? I was starting to sweat, wondering when my turn would ever come!"

    $ show_sprites("d 1")
    voice "ch1_d_003"
    d "See, a mage and their familiar—they're one-of-a-kind partners, that's the thing. So you two getting along? That's a good thing, y'know!"

    voice "ch1_d_004"
    d "Besides, when a noble young lady goes out of her way to dress up for her partner's sake — that's quite the gesture, y'know!"

    $ show_sprites("d 1 shy")
    voice "ch1_d_005"

    # !!!
    if choise_result == "good":
        d "See? That’s it. A real man knows to offer a gentle word when it counts—that’s what being a man’s all about, huh?"
    else:
        d "C'mon, partner — a real man at least offers a gentle word when it counts, yeah?"

    $ show_sprites(("l 3 angry", "d 1 shy"))
    voice "ch1_l_016"
    l "If you run your mouth one more time, I'll melt you down into scrap iron and bury you in the academy's backyard — got it?!"

    $ show_sprites(("l 3 angry", "d 1 sad"))
    voice "ch1_d_006"
    d "Whoa, scary! Partner, I'll just take a little nap for now — so when my cue comes, give me a holler, yeah?"

    $ show_sprites(("l 3 angry", "s 1 sad"))

    voice "ch1_s_018"
    s "Sheesh..."

    $ show_sprites("l 3", mode="big")
    th "My master, Louise... she's stubborn, fiercely proud, and quick to anger..."
    th "Well, regarding the fact that she... ahem, has no chest... since she seriously stresses over it, I'd better keep quiet..."
    th "But sometimes she's unexpectedly gentle... and honestly, she looks pretty cute at times."
    th "Anyway, I just can't leave her be... Must be the classic curse of a guy who's lost his heart."

    # ==== SUBCHAPTER 2 ====
    $ fade_fx("l_s_forest_l_s_speak", new_music="t27", type="cg")
    
    th "Hm...? Someone's collapsed."

    voice "ch1_l_017"
    l "Hey, Saito? What's wrong?"

    voice "ch1_s_019"
    s "Over there... Isn't someone lying at the foot of that tree?"

    $ dissolve_fx("l_s_forest_s_speak", type="cg")

    voice "ch1_l_018"
    l "What? Where?"

    voice "ch1_s_020"
    s "Hey, over there... nah, better to see for myself. My bad, Louise! I'm going first!"

    $ dissolve_fx("l_forest", type="cg")

    voice "ch1_l_019"
    l "Ah—wait, Saito! Ugh, what is wrong with you?!"

    $ fade_fx("ha_forest", type="cg")

    voice "ch1_s_021"
    s "Just as I thought... There really is someone collapsed... I wonder if she is okay... wait—huh, hey!?"

    voice "ch1_l_020"
    l "Seriously, Saito! What are you doing leaving your master behind?! …Wait, there really is someone collapsed…"

    voice "ch1_l_021"
    l "This girl… she's wearing such unfamiliar clothes. Just what country could she be from, I wonder?"

    th "That blazer she's wearing... now that I look closer, isn't that the uniform from the school I used to go to?"
    th "Why is this girl wearing these clothes? Could it be... she's from Japan too, just like me...?"
    th "No, no... this girl... It’s like I’ve met her somewhere before..."
    th "Where, exactly? Back at my school in Japan?"
    th "I remember now. No doubt about it. She’s \"Haruna Takana\", our class representative...?"
    th "No, wait... Get a grip, me. What the hell is Takana-san doing in this world?"

    voice "ch1_l_022"
    l "Hey, Saito. What's with you staring at this girl so intently?"

    voice "ch1_s_022"
    s "Ah, uh—my bad, my bad. First things first, I should help her out..."

    voice "ch1_s_023"
    s "First, check pulse and heartbeat..., loosen her clothes to keep the airway clear..."

    $ hit_fx()
    pause(0.5)

    voice "ch1_l_023"
    l "Saito, what do you think you're doing?! Trying to take off a girl's clothes?!"

    voice "ch1_s_024"
    s "Huh!? I-It's a misunderstanding! I was just trying to take care of this girl!"

    voice "ch1_l_024"
    l "It doesn't look that way at all! I'll examine her myself, so you just go away!"

    voice "ch1_s_025"
    s "...Yeah, yeah."

    voice "ch1_l_025"
    l "It looks like she's just unconscious. No head trauma... Saito, hurry and head to the academy!"

    voice "ch1_s_026"
    s "Eh?"

    voice "ch1_l_026"
    l "No time for 'Eh?' — we can't exactly drag an unconscious person along, can we?"

    voice "ch1_l_027"
    l "I meant we should call for reinforcements! Surely you don't need me to spell out every last detail before you get it, right?"

    voice "ch1_s_027"
    s "Ah, yeah... You're right."

    th "There's a lot I want to ask... but first things first — her condition."

    # ==== SUBCHAPTER 3 ====

    $ fade_fx("forest",new_music="t17")

    $ show_sprites("mage")
    voice "ch1_mage_001"
    mage "So there you are."

    $ show_sprites(("mage", "s 1 angry"))

    voice "ch1_s_028"
    s "Gah?!"

    $ show_sprites(("mage", "l 1 angry"))

    voice "ch1_l_028"
    l "What?! Who are you people?!"

    voice "ch1_mage_002"
    mage "Hand over that girl."

    $ show_sprites(("mage", "s 1 angry"))
    voice "ch1_s_029"
    s "Who are you people? Do you know this girl?"

    voice "ch1_mage_003"
    mage "You have no need to know. Leave quietly, and we'll spare your lives."

    voice "ch1_s_030"
    s "What did you just say?!{#ver1}"

    # ==== CHOISE 2 ====
    $ choise_result = None
    $ louise = "l 1 angry"
    menu:
        "Let me think for a moment.":
            $ choise_result = "neutral"
        "Like hell I'd do that!":
            $ choise_result = "good"
        "Alright... I'll hand her over.":
            $ choise_result = "bad" 

    if choise_result == "good":
        voice "ch1_s_036"
        s "Like hell I can do that! You just pop out of nowhere, dressed all suspiciously — did you really think I'd just hand her over without a second thought?!"
        
        $ louise = "l 1 sad"
        $ show_sprites((louise, "s 1 angry"))
        voice "ch1_l_031"
        l "Saito..."
        pause(1)

        $ update_sympathy(10)
        $ tndl(30)
    elif choise_result == "neutral": 
        $ show_sprites(("mage", "s 1 sad"))

        voice "ch1_s_031"
        s "W-wait... let me think for a moment."

        $ louise = "l 1 angry"
        $ show_sprites((louise, "s 1 sad"))
        
        voice "ch1_l_029"
        l "What are you even thinking about?! This is obviously a 'no way' situation, got it?!"

        $ show_sprites((louise, "s 3 sad"))

        voice "ch1_s_032"
        s "Ah, yeah... You're right.{#var_2}"

    elif choise_result == "bad":
        voice "ch1_s_037"
        $ show_sprites(("mage", "s 1 sad"))

        s "Understood. You can have this girl."
        
        $ show_sprites(("l 3 angry", "s 1 sad"))

        voice "ch1_l_032"
        l "Wait, Saito! You can't possibly mean you're going to entrust this girl to these suspicious strangers we know nothing about?!"
        
        $ update_sympathy(-10)
        $ tndl(-30)

        $ show_sprites(("l 3 angry", "s 3 sad"))

        voice "ch1_s_038"
        s "Huh? Ah, no... Um, well, you see... I was just testing them, okay?!"

        $ louise = "l 1"
        $ show_sprites(("l 1", "s 3 sad"))
        voice "ch1_l_033"
        l "Is that so...?"
    
    $ show_sprites((louise, "s 1 angry"))    

    voice "ch1_s_033"
    s "Hey, you guys! Listen up good."

    voice "ch1_s_034"
    s "I'm not handing this girl over to you. Leave — now!"

    $ show_sprites((louise, "d 1 happy", "s 1 angry"), center_front=True)    
    voice "ch1_d_007"
    d "Heh heh heh... That's what I like to see, partner! Thought my edge'd never see action again."

    $ show_sprites(("mage", "d 1", "s 1 angry"))    
    voice "ch1_mage_004"
    mage "Hmph... How foolish. A mere commoner dares to stand in our way? Very well — then you shall receive a fitting recompense."

    play sound take_sword
    $ show_sprites(("mage", "s 7 angry"))    
    voice "ch1_s_035"
    s "Louise! I'm counting on you!"

    $ show_sprites(("l 2 angry", "s 7 angry")) 
    voice "ch1_l_030"
    l "I know! Getting dragged into something like this... Saito, you're going to pay for this later!"

    th "Like hell I'd give this important clue to getting back to Japan to these sketchy characters!"

    voice "ch1_d_008"
    d "Seems like the other side's fixin' to act, partner."  

    # call screen battle_menu

    # ==== BATTLE ==== 
    $ fade_fx("black")
    call overlay_screen(None, "") from _call_overlay_screen_battle_0
    
    #call forest_battle from _call_forest_battle

    # ==== SUBCHAPTER 4 ====
    $ fade_fx("forest", new_music="t24", sprites=("mage", "s 1 angry"))

    voice "ch1_mage_005"
    mage "To think I'd struggle against such a little girl and a commoner... Retreat!"

    voice "ch1_s_039"
    s "Hey, wait! Don't you run away!"

    $ flash_fx(sprites=("s 1 angry"), side="right")

    voice "ch1_s_063"
    s "Ah!?"

    $ show_sprites(("d 1 angry", "s 1 angry")) 
    voice "ch1_d_009"
    d "Hey now. They've escaped."

    $ show_sprites(("l 3 angry", "d 1 angry", "s 1 angry")) 

    voice "ch1_l_034"
    l "As if I'd let them get away! We're pursuing them, Saito!"

    $ show_sprites(("l 3 angry", "d 1", "s 1 angry"), center_front=True) 
    voice "ch1_d_010"
    d "Hey, hold on, cool it."

    $ show_sprites(("l 3 angry", "d 1", "s 1 angry")) 
    voice "ch1_l_035"
    l "Hey, are you really planning to just leave them alone?"

    $ show_sprites(("l 3 angry", "d 1 happy", "s 1 angry"), center_front=True) 
    voice "ch1_d_011"
    d "If we go charging after them without thinking and they've got reinforcements waiting, we could end up on the receiving end. Let's call it good that we scared them off and leave it at that."

    # Луиза на первый план
    $ show_sprites(("l 1 sad", "d 1 happy", "s 1 angry"))
    voice "ch1_l_036"
    l "...Well, I suppose you might be right. But still, something about this just doesn't sit right with me."

    #$ fade_clear("cg ha_forest")
    $ fade_fx("ha_forest", type="cg")

    voice "ch1_s_040"
    s "There, there. But more importantly, I think what we really need here is artificial respiration..."

    voice "ch1_l_037"
    l "You're so persistent!"

    $ hit_fx(type="cg")
    voice "ch1_s_041"
    s "Ooow! My head hurts like hell, like it's about to burst!"

    voice "ch1_l_038"
    l "If you try that again, I really will break (your head). Anyway, Saito, what do we do now?"

    $ fade_fx("forest", sprites=("l 1 sad", "s 1 angry"))

    voice "ch1_s_042"
    s "Huh? What do you mean, {i}'what do we do?'{/i}... About what, exactly?"

    voice "ch1_s_043"
    l "If those guys were targeting her for a reason, then she's not just an ordinary girl, right? It's not certain that we can handle this on our own."

    $ show_sprites(("l 3 sad", "s 1 angry"))
    voice "ch1_l_039"
    l "There's also the option of heading back to town once and asking them to put this girl under protection, right?"

    $ show_sprites(("l 3 sad", "d 1", "s 1 angry"))
    voice "ch1_d_012"
    d "Well, that's the common-sense judgment, I suppose."

    $ show_sprites(("l 3 sad", "s 1 angry"))
    voice "ch1_s_044"
    s "N-no, we can't! We can't just abandon this girl halfway!"

    voice "ch1_l_040"
    l "...Why do you care so much about her, anyway?"

    pause(0.2)
    $ show_sprites(("l 3 sad", "s 3 sad"))
    pause(0.2)
    voice "ch1_s_045"
    s "W-well, that's... Once we've gotten involved, it's only right to see things through to the end and take care of her, isn't it?"

    th "Besides, who knows... maybe this could give me a clue on how to get back to Japan."

    $ show_sprites(("l 3 angry", "s 3 sad"))
    voice "ch1_l_041"
    l "Something's fishy here! Saito, spill it — what have you done to her?!"

    $ show_sprites(("l 3 angry", "s 3 angry"))
    voice "ch1_s_046"
    s "N-no, hold on! What are you even saying I did to this girl we just found a moment ago?!"

    $ show_sprites(("l 1 angry", "s 3 angry"))
    voice "ch1_l_042"
    l "You've known her for five minutes and you're already acting like this! She's got a big chest — which is exactly what you like — AND black hair just like Siesta's! Coincidence? I think not!"    
    
    voice "ch1_s_047"
    s "Uh! If you put it that way... I suppose you're right."

    $ show_sprites(("l 3 angry", "s 3 angry"))
    voice "ch1_l_043"
    l "Alright, spill it! What exactly have you done to her, huh?!"

    # ==== CHOISE 3 ==== 
    $ choise_result = None
    menu:
        "I don't recall.":
            $ choise_result = "bad"
        "I didn't do anything!":
            $ choise_result = "good"

    if choise_result == "bad":
        $ show_sprites(("l 3 angry", "s 3 happy"))
        voice "ch1_s_048"
        s "I have absolutely no recollection of that. No, truly. Seriously!"
        $ show_sprites(("l 1 angry", "s 3 happy"))
        voice "ch1_l_044"
        l "...It's exactly that way of speaking that makes me unable to trust you. You don't even intend to answer seriously, do you? Is that how it is?"
        $ update_sympathy(-10)
        $ tndl(-30)

        $ show_sprites(("l 1 angry", "s 3"))
        voice "ch1_s_049"
        s "No, wait, really! I'm telling you, I'm not lying! Please calm down, Louise-san."

        voice "ch1_l_045"
        l "No arguments!"
        $ hit_fx(sprites=("l 1 angry", "s 3 angry"))
        voice "ch1_s_050"
        s "Nooooooo!"

        voice "ch1_l_046"
        l "Haa... haa... haa..."
        $ show_sprites(("l 1 angry", "d 1 happy", "s 3 angry"))
        voice "ch1_d_013"
        d "...Haa. Hey, you still alive there, partner?"

        $ show_sprites(("l 1 angry", "d 1", "s 1 sad"))
        voice "ch1_s_051"
        s "...I'm dead."

        $ show_sprites(("l 1", "s 1 sad"))
        voice "ch1_l_047"
        l "Oh well, it's fine. I was planning to do that anyway, so let's just take her to the academy for now."

        voice "ch1_s_052"
        s "...Please."

        $ show_sprites(("l 3 angry", "s 1 sad"))
        voice "ch1_l_048"
        l "It's not like I'm doing this for you, you know. If you so much as lay a finger on this girl, I won't hold back next time — got it?"

        $ show_sprites(("l 3 angry", "s 3 sad"))
        pause(0.2)
        voice "ch1_s_053"
        s "I'm telling you, it's a misunderstanding!"

    if choise_result == "good":
        $ show_sprites(("l 3 angry", "s 3 angry"))
        voice "ch1_s_056"
        s "I didn't do anything! This girl — I swear, I just met her for the first time!"

        $ show_sprites(("l 3 sad", "s 3 angry"))
        voice "ch1_l_053"
        l "...Really? Then why are you so eager about it, hmm?"

        $ show_sprites(("l 3 sad", "s 1"))
        voice "ch1_s_057"
        s "This girl... she really reminds me of a classmate from my hometown."
        voice "ch1_s_058"
        s "So basically... if this isn't just some crazy person's prank, then..."

        $ show_sprites(("l 3 sad", "s 1 sad"))
        voice "ch1_s_059"
        s "There's a chance she holds a key to my world... that's what I'm thinking."

        pause(0.2)
        $ show_sprites(("l 1 sad", "s 1 sad"))
        voice "ch1_l_054"
        l "Ah..."

        ## тут 3 раза подряд если повысили то уже максимум должен быть
        $ update_sympathy(10)
        $ tndl(30)
        $ show_sprites(("l 1 sad", "s 1 angry"))
        voice "ch1_s_060"
        s "I want any clue I can get to return to my original world. ...Ah, but of course, it's also true that I really do want to help her. That part's completely genuine."

        voice "ch1_l_055"
        l "..."

        $ show_sprites(("l 1 sad", "s 1"))
        voice "ch1_s_061"
        s "It's the honest-to-god truth."

        $ show_sprites(("l 1 angry", "s 1"))
        voice "ch1_l_056"
        l "Ugh, fine, I get it! I was planning to do that anyway, so let's just take her to the Academy for now."

        voice "ch1_s_062"
        s "I'm sorry to ask, but... please."


    $ show_sprites(("l 1", "s 1"))
    voice "ch1_l_049"
    l "Those people from earlier might attack again, so I'm putting this girl on my horse. I'll move the luggage attached here over to your side, alright?"
    
    if choise_result == "good":
        voice "ch1_s_064"
        s "Yeah."
    if choise_result == "bad":
        voice "ch1_s_054"
        s "...Alright..."

    voice "ch1_l_050"
    l "But, I know the circumstances are... well, complicated. Still, just letting a commoner into the academy on our own — if the teachers find out, that could be real trouble, probably."

    voice "ch1_l_051"
    l "She does need treatment, but... I wonder what we should do about it."

    voice "ch1_s_055"
    s "About that... let's think it over once we get back."

    voice "ch1_l_052"
    l "Honestly... why am I the one stuck doing this...?"

    $ fade_fx("yard_night_blurred", stop_music=True)

    jump ch1_2

    return