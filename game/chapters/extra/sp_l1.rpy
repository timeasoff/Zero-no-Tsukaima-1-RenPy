# kormeshka_event
label sp_l1:
    call overlay_screen("overlay",  "A tsundere event occurred!", isUseBlur=False, text_mode="orange") from _call_sp_l1

    $ fade_fx("ready_to_blow_2", new_music="t3", type="cg")
    voice "sp_l1_l_001"
    l "Hey, um, Saito. Are you hungry?"

    voice "sp_l1_s_001"
    s "Huh? Wh-what do you want, out of the blue?"

    voice "sp_l1_l_002"
    l "You're hun-gry, aren't you?"
    voice "sp_l1_s_002"
    s "Ah... well... uh..."

    menu:
        "Looks like I'm actually getting hungry...":
            voice "sp_l1_s_003-2"
            s "Looks like I'm actually getting hungry..."

            th "Looks like it's best not to argue right now. If she gets mad, it'll just be a huge hassle."

            voice "sp_l1_l_008"
            l "Yes, exactly. There's no need to hold back just because you're a familiar."
        
        "Yep! Starving, totally starving!!":
            voice "sp_l1_s_003"
            s "Yep! Starving, totally starving!!"

            th "I don't really understand it, but... I guess I should stay on her good side for now."
            
            voice "sp_l1_s_004"
            s "Seriously, I'm absolutely starving!!"

            voice "sp_l1_l_003"
            l "Good. I'm glad."

            voice "sp_l1_s_005"
            s "Glad?"

            voice "sp_l1_l_004"
            l "Oh, no. Never mind."

        "Not hungry one bit.":
            voice "sp_l1_s_003-3"
            s "Not hungry one bit."

            th "No way am I giving in right now!"

            voice "sp_l1_s_008"
            s "Not in the slightest! Absolutely not! Not even a little bit!!"

            th "I will firmly stand by my own will..."

            voice "sp_l1_l_009"
            l "..."

            th "Though, she actually seems to be angry!!"

            voice "sp_l1_s_009"
            s "Oh, no... On second thought... my stomach might be empty..."

            voice "sp_l1_l_010"
            l "Really?"

            voice "sp_l1_s_010"
            s "Y-yeah. Really, really. Ah, I'm so hungry!!"

            voice "sp_l1_l_011"
            l "I'm glad."

            voice "sp_l1_s_011"
            s "Huh? Glad? What do you mean, 'glad'?"

    voice "sp_l1_l_005"
    l "Then let's go to the dining hall right now!"

    voice "sp_l1_s_006" 
    s "Huh?{#E?}"

    voice "sp_l1_l_006"
    l "Come on, hurry up! We're going!"

    voice "sp_l1_s_007"
    s "H-hey, hey now. What's with the sudden rush..."

    $ fade_fx("dining_hall")
    $ show_sprites(("l 1 happy", "s 3"), anim_in="slide_right")
    
    pause(0.5)
    voice "sp_l1_l_007"
    l "Here... eat."

    $ show_sprites(("l 1 happy", "s 3 sad"))
    voice "sp_l1_s_012"
    s "Huh? What's this?"

    voice "sp_l1_l_012"
    l "What do you mean, 'what'? It's a stew. Doesn't it look like one?"
    ## I dunno what the hell book this is, but I've double-checked this case five times and this is indeed what it's about.

    voice "sp_l1_s_013"
    s "Well, it doesn't look like it."

    voice "sp_l1_s_014"
    s "But how come?"

    th "It is stew, right...? Why me?"

    $ show_sprites(("l 1 angry", "s 3 sad"))
    voice "sp_l1_l_013"
    l "Ah... W-well, d-don't misunderstand me!"

    voice "sp_l1_l_014"
    l "It's not like I prepared this just to make you eat it!!"

    $ show_sprites(("l 1 sad", "s 3 sad"))
    voice "sp_l1_l_015"
    l "J-just, um..."

    voice "sp_l1_s_015"
    s "?"

    $ show_sprites(("l 3 shy", "s 3 sad"))
    voice "sp_l1_l_016"
    l "Y-yes, exactly! Because I just had extra!"

    voice "sp_l1_s_016"
    s "Ah... alright. I get it, I get it. No need to get so mad."

    $ show_sprites(("l 3 sad", "s 3 sad"))
    voice "sp_l1_l_017"
    l "I-I'm not angry or anything. So... well? Are you going to eat it?"

    $ show_sprites(("l 3 sad", "s 3"))
    voice "sp_l1_s_017"
    s "Ah, yeah. I'll have some. It looks delicious, after all."

    $ show_sprites(("l 3", "s 3"))
    voice "sp_l1_l_018"
    l "W-well then..."

    voice "sp_l1_s_018"
    s "Yeah. Here's the spoon."

    $ fade_fx("l_feed", type="cg")
    voice "sp_l1_l_019"
    l "Here, say 'ahh'."

    voice "sp_l1_s_019"
    s "...Huh?{#a?}"

    voice "sp_l1_l_020"
    l "I'm telling you, say 'ahh'."

    voice "sp_l1_s_020"
    s "..."

    menu:
        "Is this some kind of punishment game?":
            voice "sp_l1_s_032"
            s "Is this some kind of punishment game?"

            $ dissolve_fx("l_feed_3", type="cg")
            voice "sp_l1_l_031"
            l "W-what kind of nonsense is that!"

            voice "sp_l1_s_033"
            s "No, I mean like, you made some kind of bet with Kirche and lost."

            voice "sp_l1_l_032"
            l "I would do no such thing! Idiot! Just eat it already!!"

            voice "sp_l1_s_034"
            s "Hey, there's no need to get mad."

            voice "sp_l1_l_033"
            l "Come on! Say 'ahhh'!"

            voice "sp_l1_s_035"
            "Ah, ahh..."

        "Ahh...":
            voice "sp_l1_s_031"
            s "Ahh..."

            th "I have no idea what she's scheming, but... it's best not to cross her."

            voice "sp_l1_l_030"
            l "Oh, my, you're not being very honest with yourself today. I wish it were always like this."
        
        "Does this have poison in it or something?":
            voice "sp_l1_s_021"
            s "Does this have poison in it or something?"

            $ dissolve_fx("l_feed_3", type="cg")
            voice "sp_l1_l_021"
            l "W-what are you saying! I would never do such a thing!"

            voice "sp_l1_s_022"
            s "Ah, n-no, sorry. I was just joking."
            
            voice "sp_l1_l_022"
            l "Good grief, you're a total idiot. You have no idea how a woman's heart works..."

            voice "sp_l1_s_023"
            s "Huh? Woman's heart?"

            voice "sp_l1_l_023"
            l "Never mind! Just eat, I said!!"

            voice "sp_l1_s_024"
            s "A-alright, I understand."

    $ dissolve_fx("l_feed", type="cg")
    voice "sp_l1_s_025"
    s "{i}Chews{/i}..."

    voice "sp_l1_l_024"
    l "Is it good?"

    voice "sp_l1_s_026"
    s "Mhm! It's good!!"

    voice "sp_l1_l_025"
    l "Really!?"

    voice "sp_l1_s_027"
    s "Oh yeah, the cafeteria food here is really good, you know!"

    $ dissolve_fx("l_feed_2", type="cg")
    voice "sp_l1_l_026"
    l "..."

    voice "sp_l1_s_028"
    s "Seriously, having a proper meal is the only thing that brings me joy!!"

    voice "sp_l1_l_027"
    l "..."

    voice "sp_l1_s_029"
    s "Hold on... Eh? What's going on? Louise?"

    voice "sp_l1_l_028"
    l "..."

    voice "sp_l1_s_030"
    s "Hey, hey. Louise-san."

    $ dissolve_fx("l_feed_3", type="cg")
    pause(0.5)
    voice "sp_l1_l_029"
    l "...What?"

    voice "sp_l1_s_036"
    s "Eh?"

    voice "sp_l1_l_034"
    l "What, what is it?!"

    voice "sp_l1_s_037"
    s "No... what's wrong?"

    voice "sp_l1_l_035"
    l "Anyway... anyway, I'm just...!!"

    voice "sp_l1_s_038"
    s "N-no, I mean, what?"

    voice "sp_l1_l_036"
    l "Saito, you fool!!!"

    $ fade_fx("dining_hall", sprites=("s 3 sad"))
    pause(0.5)
    voice "sp_l1_s_039"
    s "Oh... She ran off."

    th "Why is she getting so mad anyway, she's such a weirdo..."

    $ show_sprites(None, anim_out="slide_right")

    return


