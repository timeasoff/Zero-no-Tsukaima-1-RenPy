# Сиеста спалила Сайто и Луизу
label ch1_5:
    $ fade_fx("sky", new_music="t4", type="cg")
    voice "ch1.5_s_001"
    s "Hmm... {i}yawns{/i}. It's already morning, huh... I wonder what time it is?"

    voice "ch1.5_s_002"
    s "I'd better get everything ready for washing up before Louise wakes up... {i}yawns{/i}."

    voice "ch1.5_s_003"
    s "Ah... But this bed, which I haven't slept in for a long time, is so comfortable... I can't get up..."

    
    $ fade_fx("louise_room")
    pause(0.2)
    play sound knock_door
    pause(1)

    voice "ch1.5_s_004"
    s "Huh...?{#ha}" 

    voice "ch1.5_si_001"
    si "Good morning, Saito-san. Good morning, Miss Vallière."

    voice "ch1.5_s_005"
    s "Eh, Siesta?"

    th "Wait, I'm still sleeping in the same bed as Louise!!"

    voice "ch1.5_si_002"
    si "I'm sorry to bother you so early in the morning, but actually, about last night..."

    $ fade_fx("si_wakeup", new_music="t29", type="cg")
    pause(2)
    voice "ch1.5_si_003"
    si "..."

    voice "ch1.5_s_006"
    s "Ah... G-good morning... Siesta..."

    voice "ch1.5_si_004"
    si "You two... in the same bed..."

    voice "ch1.5_s_007"
    s "Ah, no, wait!"

    voice "ch1.5_s_008"
    s "I don't know what kind of misunderstanding you've got, but there's no romance, no {i}'moe'{/i} moments, or anything like that you're imagining."

    voice "ch1.5_s_009"
    s "It's hard to sleep on the straw that is technically my proper bed, right?"

    voice "ch1.5_s_010"
    s "Then my master told me to get into the corner of the bed, so I just did what I was told..."

    voice "ch1.5_s_011"
    s "See, if I don't obey, I'll get punished, you know."

    voice "ch1.5_s_012"
    s "So I was like, 'this is annoying,' but I still got into the same bed anyway. Just thinking to myself, {i}'man, this is a pain...'{/i} or whatever."

    pause(1)
    $ dissolve_fx("si_wakeup_2", type="cg")

    voice "ch1.5_si_005"
    si "...Is that so?"

    th "S-scary... It's terrifying how she's still smiling..."

    voice "ch1.5_si_006"
    si "I get all that. But then, what about that hand tightly gripping your clothes, Saito-san?"

    voice "ch1.5_s_013"
    s "Eh!?{#e}"
    
    th "W-w-why the hell is Louise sleeping while clinging to me!?"

    voice "ch1.5_s_014"
    s "Th-th-this!"

    # громче
    voice "ch1.5_si_007"
    si "Yes?"

    voice "ch1.5_s_015"
    s "Well, the thing is..."

    $ result = None
    menu:
        "Louise is just half-asleep!":
            voice "ch1.5_s_016"
            s "That Louise is just half-asleep..."

            voice "ch1.5_s_017"
            s "If this keeps up, I might be stuck in bed for the rest of my life, hehe... Or so I could say... How does that sound?"

            voice "ch1.5_si_008"
            si "That must be a dreadful situation."

            voice "ch1.5_si_009"
            si "How on earth did he manage to catch the attention of Miss Vallière... I'm quite curious."

            voice "ch1.5_s_018"
            s "S-Siesta..."

            voice "ch1.5_l_001"
            l "Mmm..."

            voice "ch1.5_s_019"
            s "Ah, looks like Louise is waking up."

            voice "ch1.5_l_002"
            l "Mmm... {i}yaaaawn{/i}... Huh, Saito...?"
        
        "We need a witness's testimony here!":
            $ result = 'TESTIMONY!!!'

            voice "ch1.5_s_021"
            s "At this juncture, it is my intention to prove my innocence through the testimony of a third party!"

            voice "ch1.5_si_012"
            si "A third party...? But currently, there is no one else in this room besides Saito-san, myself, and Miss Vallière."

            voice "ch1.5_s_022"
            s "I have my partner with me! Hey, Derf!"

            voice "ch1.5_d_001"
            d "What's up, partner? What do you need from me this early in the morning?"

            voice "ch1.5_d_002"
            d "Hold on, what's going on here? Sneaking around with a village girl in a noble's bedroom? You're as reckless as ever, partner."

            voice "ch1.5_si_013"
            si "W-What!? No, I'm not mentally ready for something like that!"

            $ update_sympathy(10, char_key="siesta")
            $ tndl(-30)

            voice "ch1.5_s_023"
            s "That's not it! Don't say things that will be completely misunderstood!"

            voice "ch1.5_d_003"
            d "Tch, what a drag. Anyway, what do you really need?"

            voice "ch1.5_s_024"
            s "You've been keeping an eye on everything in this room the whole time, haven't you?"

            voice "ch1.5_d_004"
            d "Yeah, I suppose."

            voice "ch1.5_s_025"
            s "Sorry to ask, but could you vouch for my innocence to Siesta?"

            voice "ch1.5_d_005"
            d "Eh?{#e?}"

            voice "ch1.5_s_026"
            s "I'm begging you. My honor is on the line."

            voice "ch1.5_d_006"
            d "My, my. You're as stubbornly by-the-book as always, partner. Oh well, whatever."

            voice "ch1.5_d_007"
            d "The noble girl gave my partner permission to use the bed."

            voice "ch1.5_d_008"
            d "She told him he could share the bed as long as he stuck to the corner. And I ain't making this up."

            voice "ch1.5_si_014"
            si "...Is that really true?"

            voice "ch1.5_s_037"
            s "Yes, yes! It's the truth, so please, try to believe me!"

            voice "ch1.5_d_009"
            d "Well, naturally. Though what dirty thoughts my partner had when he got into that bed is none of my business."

            voice "ch1.5_s_027"
            s "Like I said! Stop adding unnecessary commentary!"

            voice "ch1.5_l_001-2"
            l "Mmm..."

            voice "ch1.5_s_028"
            s "Huh? Louise, did you wake up?"

            voice "ch1.5_l_005"
            l "{i}Yawns{/i}... Ugh, you're so noisy first thing in the morning, Saito. Now I've ended up waking up because of you..."

        "I'll wake up Louise and let her explain it herself.":
            $ result = "WAKE UP!"

            voice "ch1.5_s_029"
            s "Uh, um. In a situation like this, rather than me saying it, it's probably better to let Louise herself explain it, yeah."

            voice "ch1.5_s_030"
            s "Hey, Louise, Louise! I'm begging you, wake up and explain this situation! Or rather, prove my innocence!"

            voice "ch1.5_l_006"
            l "Mmm... mm..."

            voice "ch1.5_s_031"
            s "Louise! Come on, wake up!"

            voice "ch1.5_l_007"
            l "Mmm..."

            voice "ch1.5_si_016"
            si "!!!!!"

            $ update_sympathy(-10, char_key="siesta")
            $ tndl(30)

            voice "ch1.5_s_032"
            s "Lu-, Louise!? Wait a minute, there's a limit to sleep-hugging! Don't cling to me, don't squeeze me!"

            voice "ch1.5_si_017"
            si "Sa... Saito-san..."

            voice "ch1.5_s_033"
            s "!!!!! Wait, Siesta, I swear it's a misunderstanding!"

            voice "ch1.5_si_018"
            si "To think that you and Miss Vallière had become that close... I had no idea at all."

            th "What am I supposed to do now!?"

            voice "ch1.5_l_002-2"
            l "Mmm... {i}Yawns{/i}... Huh, Saito...?"

    $ fade_fx("louise_room")
    pause(1)

    if result == "WAKE UP!":
        $ show_sprites(("l 4 angry", "s 5 sad"))
        voice "ch1.5_l_008"
        l "...Wait, huh!? Why are you clinging to me!?"

        voice "ch1.5_s_034"
        s "Wha-!? N-No, that's wro...!"

        $ scene_fx("hit flash", sound="punch", duration=(0.3, 2), sprites=("si 1 sad", "s 5 sad"))
        pause(1)

        voice "ch1.5_s_035"
        s "A-Anyway, at least my name has been cleared, right?"

        voice "ch1.5_si_019"
        si "Y-Yes... I sincerely apologize for having doubted you."

        $ show_sprites(("l 4 angry", "s 5 sad"))
        voice "ch1.5_l_009"
        l "Geez, that's fine now, whatever! More importantly, why is Siesta in my room!?"
    else:
        $ show_sprites(("l 4 angry", "s 5"))
        pause(0.5)

        if result == 'TESTIMONY!!!':
            voice "ch1.5_l_003-2"
        else:
            voice "ch1.5_l_003"
        l "Wait... wha-!? Why is Siesta in my room!?"

    th "Come to think of it, I wonder why Siesta came at this time?"

    $ show_sprites(("l 4 angry", "si 1"))
    voice "ch1.5_si_010"
    si "Right. I came regarding that girl."

    $ show_sprites(("s 5 angry", "si 1"))
    voice "ch1.5_s_038"
    s "Eh?{#e?}"

    voice "ch1.5_si_011"
    si "That girl woke up just now. So, I thought I should come and inform Saito-san and Miss Vallière..."

    $ show_sprites(("s 5 happy", "si 1"))
    voice "ch1.5_s_036"
    s "Really!? Got it, I'll go right away!"

    $ show_sprites(("l 4 angry", "si 1"))
    voice "ch1.5_l_010"
    l "Eh, ah, wait a sec, Saito!? Wait until I get changed!!"

    $ show_sprites(("l 4 angry", "si 1 angry"))
    voice "ch1.5_si_020"
    si "Ah, Saito-san. Please wait!"

    $ show_sprites(None, anim="slide_right") 

    jump ch1_6
    return