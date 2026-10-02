# встреча с Гишем
label ch1_8:
    $ fade_fx("hallway_down_night", new_music="t18", sprites=("g 1"))

    voice "ch1.8_g_001"
    g "Oh? I hear the four of you have been summoned by the Headmaster. What on earth happened?"

    $ show_sprites(("g 1"), mode="big")
    th "Guishe is Louise's classmate. He specializes in Earth system magic. He knows as 'Guishe the Bronze'."
    th "He's a womanizer and a show-off, but you just can't hate the guy."

    $ show_sprites(("l 1", "g 1"))
    voice "ch1.8_l_001"
    l "Listen... There was an unfortunate accident."

    $ show_sprites(("k 1", "g 1"))
    voice "ch1.8_k_001"
    k "Oh, right. Louise just accidentally destroyed a commoner's room with her magic."
    
    $ show_sprites(("k 1", "g 1 happy"))
    voice "ch1.8_g_002"
    g "Hahaha. Some things never change with Louise."

    $ show_sprites(("l 1 angry", "g 1 happy"))
    voice "ch1.8_l_002"
    l "Tch...!"
    
    th "Unable to retort, just stewing in rage. I need to make a run for it before things blow up."
    
    voice "ch1.8_g_003"
    g "By the way, where is that commoner? I, Guiche, would like to lay eyes on him just once."
    
    $ show_sprites(("l 1 angry", "m 1 sad"))
    voice "ch1.8_m_001"
    m "..."

    $ show_sprites(("l 3 happy", "m 1 sad"))
    voice "ch1.8_l_003"
    l "By the way, Montmorency... I have a question I'd like to ask you once more."
    
    voice "ch1.8_m_002"
    m "W-what is it?"
    
    $ show_sprites(("l 3", "m 1 sad"))
    voice "ch1.8_l_004"
    l "Why do you avoid eye contact, I wonder?"

    voice "ch1.8_m_003"
    m "No, not really. Just doing some neck exercises, that's all."

    $ show_sprites(("l 3 angry", "m 1 sad"))
    voice "ch1.8_l_005"
    l "Didn't I tell you to stay silent? Why are we being found out like this!"

    $ show_sprites(("l 3 angry", "m 1 happy"))
    voice "ch1.8_m_004"
    m "Ah, ahaha... Sorry, I couldn't help it."

    voice "ch1.8_l_006"
    l "Don't give me that 'slipped out' excuse. I said it was a secret! If this keeps up, our future looks bleak."

    $ show_sprites(("g 1 happy", "m 1 happy"))
    voice "ch1.8_g_004"
    g "Eh, why is it a secret? There's no way the beautiful Montmorency would keep things from me!"

    $ show_sprites(("g 1 happy", "m 1 sad"))
    voice "ch1.8_m_005"
    m "Sorry, Louise. I wish I hadn't said a word just now."

    $ show_sprites(("g 1 sad", "m 1 sad"))
    voice "ch1.8_g_005"
    g "Eh? Did I do something wrong to you!?"

    $ show_sprites(("l 1 sad", "m 1 sad"))
    voice "ch1.8_l_007"
    l "Montmorency. I feel for you."

    $ show_sprites(("s 3 sad", "m 1 sad"))
    voice "ch1.8_s_001"
    s "I agree completely."

    $ show_sprites(("g 1 angry", "m 1 sad"))
    voice "ch1.8_g_006"
    g "Whaaat!? Why is everyone ganging up on me like this!?"

    $ show_sprites(("g 1 angry", "m 1"))
    voice "ch1.8_m_006"
    m "Anyway, putting that aside. We should go see how she’s doing later. She’s due for a check-up soon."
    
    $ show_sprites(("l 1", "m 1"))
    voice "ch1.8_l_008"
    l "Agreed. Since I have a lecture, let’s agree to gather everyone once it finishes. Is that fine?"
    
    voice "ch1.8_m_007"
    m "It’s fine with me."
   
    $ show_sprites(("g 2 happy", "m 1"))
    voice "ch1.8_g_007"
    g "I’m fine with that as well."

    $ show_sprites(("k 1", "t 1"),  anim_in="slide_right", anim_out="slide_right")
    voice "ch1.8_k_002"
    k "Understood."
    t "..."

    $ show_sprites(("s 3"),  anim_in="slide_right", anim_out="slide_right")
    voice "ch1.8_s_002"
    s "It's okay by me as well... if you say so."

    th "Classes... They’re useless to me. It’s just lessons on this world’s magic and history, after all."
    th "Sorry to Louise, but I think I’ll take a short walk."

    $ fade_fx("hallway_night", new_music="t3")

    $ sprite_choice([
        {"char": "tabitha",      "text": "Library", "target": "library_ch1_8"},
        {"char": "kirche",      "text": "Kirche's Room", "target": "k_room_ch1_8"},
        {"char": "haruna",      "text": "Louise's Room", "target": "l_room_ch1_8"},
        {"text": "Hallway",       "target": "hallway_ch1_8"},
    ])

    jump ch1_9
    return

label library_ch1_8:
    $ fade_fx("library", new_music="t8")
    $ show_sprites(("s 1"))

    voice "ch1.8_s_003"
    s "Not a sound... Libraries are quiet no matter what world you're in."

    voice "ch1.8_s_004"
    s "Oh, what's that?"

    $ fade_fx("t_library_read", type="cg")
    voice "ch1.8_s_005"
    s "Yo, Tabitha."
    t "..."
    $ update_sympathy(20, char_key="tabitha")

    th "Huh, I wonder if she didn't hear me."

    voice "ch1.8_s_006"
    s "Hey, Tabitha!"

    $ dissolve_fx("t_library_read_2", type="cg")
    voice "ch1.8_t_001"
    t "...Silence."

    voice "ch1.8_s_007"
    s "Ah, sorry.{#var2}"

    $ dissolve_fx("t_library_read", type="cg")
    pause(0.5)
    play sound read
    t "..."
    th "She's gotten absorbed in her book again."

    voice "ch1.8_s_008"
    s "Tabitha? Tabitha-san, hellooo?"

    play sound read
    pause(0.5)
    t "..."
    th "Hmm. To be this unresponsive... I have to applaud her."
    th "Still, just what is in a book that can captivate someone so completely?"

    menu:
        "See what's in the book":
            th "I'm curious what's inside. Shall I sneak a look from behind her?"
            
            voice "ch1.8_s_009"
            s "Well now, what do we have here...?"

            voice "ch1.8_s_010"
            s "...?"

            voice "ch1.8_s_011"
            s "Can't read a word of this."
            th "Come to think of it, I can understand the language here, but I can't read the writing at all."
            
            $ dissolve_fx("t_library_read_2", type="cg")
            voice "ch1.8_t_002"
            t "...A general overview of the latest theories and discussions from various countries regarding the special effects that occur when superimposing the 'fire' system onto the 'wind' system."
            
            voice "ch1.8_s_012"
            s "Eh?{#e?}"

            voice "ch1.8_t_003"
            t "...That's why it's pointless for you to read it."

            voice "ch1.8_s_013"
            s "Ah... I see."
            th "On top of not being able to read it in the first place, if it's a thesis on magic, then yeah, it really is meaningless to me."
            
            voice "ch1.8_s_014"
            s "Sorry for disturbing you."

            voice "ch1.8_t_004"
            t "...No problem."

        "Snatch the book":
            th "Let's see what's written here... I suppose I'll just borrow it for a moment."
            
            voice "ch1.8_s_009-2"
            s "Well now, what do we have here...?"

            $ dissolve_fx("t_library_read_3", duration=2.0, type="cg")
            t "..."

            $ update_sympathy(-20, char_key="tabitha")
            $ update_sympathy(20, char_key="louise")

            voice "ch1.8_s_010-2"
            s "...?"

            voice "ch1.8_s_021"
            s "What the heck is this? I can't make out a single word of what's written here."

            th "Come to think of it, I can understand the language here, but I can't read the writing at all."
            
            $ dissolve_fx("t_library_read_4", type="cg")
            voice "ch1.8_t_002-2"
            t "...A general overview of the latest theories and discussions from various countries regarding the special effects that occur when superimposing the 'fire' system onto the 'wind' system."
            
            voice "ch1.8_s_012-2"
            s "Eh?"

            voice "ch1.8_t_003-2"
            t "...It's something you don't need to understand."

            voice "ch1.8_s_013-2"
            s "Ah... I see."
            th "On top of not being able to read it in the first place, if it's a thesis on magic, then yeah, it really is meaningless to me."
            
            voice "ch1.8_s_022"
            s "My bad for interrupting. Here's the book."

            $ dissolve_fx("t_library_read", type="cg")
            t "..."
            th "Can't read her expressionless face, but I wonder if she's actually angry."
            th "Now that I think about it, grabbing a book out of someone's hands without warning is pretty rude. Guess I really stepped in it."

        "Inquire about the book":
            th "Maybe I should ask Tabitha what's written in it?"
            
            voice "ch1.8_s_017"
            s "Hey, what's actually written in this thing?"

            voice "ch1.8_t_005"
            t "...It's something you don't need to know."
            
            $ update_sympathy(20, char_key="tabitha")
            $ update_sympathy(-20, char_key="louise")
            
            voice "ch1.8_s_018"
            s "...I mean, yeah, perhaps. But..."
            th "Come to think of it, I can't read the writing anyway."

            voice "ch1.8_s_019"
            s "Umm... could you at least give me an explanation?"
            
            t "..."

            voice "ch1.8_s_020"
            s "I guess that's a no?"

            $ dissolve_fx("t_library_read_2", type="cg")
            voice "ch1.8_t_002-3"
            t "...A general overview of the latest theories and discussions from various countries regarding the special effects that occur when superimposing the 'fire' system onto the 'wind' system."
            
            voice "ch1.8_s_012-3"
            s "Eh?"

            voice "ch1.8_t_003-3"
            t "...That's why it's pointless for you to read it."

            voice "ch1.8_s_013-3"
            s "Ah... I see."
            th "On top of not being able to read it in the first place, if it's a thesis on magic, then yeah, it really is meaningless to me."
            
            voice "ch1.8_s_014-3"
            s "Sorry for disturbing you."

            $ dissolve_fx("t_library_read", type="cg")
            voice "ch1.8_t_006"
            t "...Not really."
            th "Maybe I shouldn't have been so persistent... She doesn't seem all that angry, though."

    voice "ch1.8_s_015"
    s "Well then, I'll be going."

    t "..."
    th "Did she just nod a little?... So she confirmed it?"
    
    voice "ch1.8_s_016"
    s "Well, whatever."

    return

label k_room_ch1_8:
    $ fade_fx("hallway_down_night", new_music="t7")
    $ show_sprites('s 1', anim="slide_right") 

    play sound knock_door
    pause(1)
    
    voice "ch1.8_s_023"
    s "Kirche, are you there?"

    voice "ch1.8_k_003"
    k "Oh, Darling? The door isn't locked. Feel free to come in."

    voice "ch1.8_s_024"
    s "Well then, excuse me!"

    call open_door("right", "bg kirche_room_night") from _call_open_door_3

    $ show_sprites(("k 3 happy", "s 1"), anim="slide_right")

    voice "ch1.8_k_004"
    k "Come in! What a surprise. To what do I owe the pleasure?"
    
    $ update_sympathy(20, char_key="kirche")

    voice "ch1.8_s_025"
    s "Well, I don't really have any business here, but... uh..."
    voice "ch1.8_s_026"

    $ show_sprites(("k 3 happy", "s 1 angry"))
    s "Wha—wha-what!?"

    $ show_sprites(("k 3 angry", "s 1 angry"))
    voice "ch1.8_k_005"
    k "Eh? What's going on!?"

    voice "ch1.8_s_027"
    s "What's with that outfit-!?"

    $ show_sprites(("k 3", "s 1 angry"))
    voice "ch1.8_k_006"
    k "Huh? Is something wrong with this outfit?"

    voice "ch1.8_s_028"
    s "Don't give me that 'is something wrong' crap—!"
    
    menu:
        "Act like a gentleman and close my eyes.":
            th "R-right, in situations like this, it's only polite to close your eyes like a gentleman. As a true gentleman!"

            $ fade_fx("black")
            voice "ch1.8_k_007"
            k "Oh my, what's wrong, Darling? Closing your eyes all of a sudden like that."

            voice "ch1.8_s_029"
            s "Anyway, hurry up and get dressed. I've got my eyes closed. If you want, I can even step outside."
            
            voice "ch1.8_k_008"
            k "Oh, you really don't need to worry about that. I'm staying like this as long as I'm in my room anyway."
            
            voice "ch1.8_s_030"
            s "Well, I agree you're free to dress however you want in your own room, but... I'm still a guy, after all."
            
            voice "ch1.8_k_009"
            k "Ah... don't tell me you're turned on?"
            
            voice "ch1.8_s_031"
            s "If I'm honest, I'm scared of what happens next, so I'll deliberately keep my mouth shut!"
            
            voice "ch1.8_k_010"
            k "What happens next'... Oh! You mean you're scared of Louise finding out!"
            
            voice "ch1.8_s_032"
            s "...I didn't say anything, you know?"
            
            voice "ch1.8_k_011"
            k "Well, fine then. Anyway, how long are you going to keep your eyes closed?"
            
            voice "ch1.8_s_033"
            s "How long? Well, until you get dressed, obviously..."
            
            voice "ch1.8_k_012"
            k "Hup!"
            
            play music t29 fadein 1.0
            
            th "Wha—!? What are these two soft, warm, and absolutely blissful sensations pressing against my chest—!?"
            
            voice "ch1.8_k_013"
            k "Hehe... Do you still intend not to open your eyes, even now?"
            
            voice "ch1.8_s_034"
            s "Ugh—!? No good, I can't hold back anymore!"

            $ fade_fx("bg kirche_room_night", sprites=("k 3", "s 1 sad"))

        "Take this opportunity to get a good look.":
            th "Th-this is my chance? I should take this moment to enjoy the view... No, wait, observe!"
            th "...stares intently."

            $ show_sprites(("k 3 happy", "s 1 angry"))

            voice "ch1.8_k_015"
            k "...My, my?"

            $ update_sympathy(-20, char_key="louise")
            $ update_sympathy(20, char_key="kirche")

            th "Seeing it up close again, how should I put it... it's amazing... Like 'boom, squeeze, boom!' or something."
            
            voice "ch1.8_k_016"
            k "Fufu, what do you think? Are you getting turned on?"

            $ show_sprites(("k 3 happy", "s 1 shy"))
            
            voice "ch1.8_s_037"
            s "Yeah, a lot..."
            
            voice "ch1.8_k_017"
            k "Oh my, aren't you honest."

            $ show_sprites(("k 3 shy", "s 1 shy"))

            voice "ch1.8_k_018"
            k "In that case, want to get a closer look?"

            pause(1)
            play music t29 fadein 1.0 
            $ show_sprites(("k 3 shy", "s 1 angry"))
            
            voice "ch1.8_s_038"
            s "E-e-even closer... What?"

            $ show_sprites(("k 3 happy", "s 1 angry"))

            voice "ch1.8_k_019"
            k "Oh, I'm just teasing, Darling. Let's just focus on building up the tension between us today, shall we?"
            
            $ show_sprites(("k 3 happy", "s 1"))
            voice "ch1.8_s_039"
            s "Uh... yeah..."

        "Scold her.":
            play music t29 fadein 1.0

            voice "ch1.8_s_040"
            s "You mustn't go out in public dressed so sloppily! Besides, it's unseemly for a girl your age to act like that!"
            
            $ show_sprites(("k 3 angry", "s 1 angry")) 
            voice "ch1.8_k_020"
            k "What's the big deal? It's perfectly fine, isn't it?"

            $ update_sympathy(20, char_key="louise")
            $ update_sympathy(-20, char_key="kirche")
            
            voice "ch1.8_s_041"
            s "It's not okay! You should just wear your uniform like a normal person!"
            
            voice "ch1.8_k_021"
            k "No way! It's just too hot, that's all!"
            
            $ show_sprites(("k 3 angry", "s 1 sad")) 
            voice "ch1.8_s_042"
            s "Is that really how it works?"
            
            voice "ch1.8_k_022"
            k "That's just how it is!"
            
            voice "ch1.8_s_043"
            s "Well, I guess there's no helping it then..."

    voice "ch1.8_s_044"
    s "W-well, in any case... I'll be heading back now."

    $ show_sprites(("k 3 shy", "s 1 sad"))
    
    voice "ch1.8_k_014"
    k "Oh, Darling, you're so adorable when you're this innocent <3. Do come back again."

    call open_door("left") from _call_open_door_4

    $ fade_fx("hallway_down_night")
    $ show_sprites(("s 1 angry"), anim="slide_left") 
    
    th "Haa... haa... haa... Phew, that was a dangerous situation."
    
    th "My reason was about to be swept away by youthful passions that had exceeded all limits..."
    
    voice "ch1.8_s_045"
    $ show_sprites(("s 1 sad")) 
    s "...Better go back and behave myself."

    return

label l_room_ch1_8:
    $ fade_fx("louise_room_night", new_music="t10", sprites=("ha 3 shy"))
    voice "ch1.8_ha_001"
    ha "Ah..."

    $ update_sympathy(20, char_key="haruna")   

    $ show_sprites(("ha 3 shy", "s 1"), anim="slide_right") 
    
    voice "ch1.8_s_046"
    s "H-hey there."

    voice "ch1.8_s_047"
    s "Is it really alright for you to stay awake? If you're feeling weary, I believe you should lie down."

    $ show_sprites(("ha 3", "s 1")) 
    voice "ch1.8_ha_002"
    ha "No, I'm fine. It's nothing serious, doesn't seem to be any real problem."

    voice "ch1.8_s_048"
    s "R-right."

    voice "ch1.8_ha_003"
    ha "Yeah.{#um}"

    $ show_sprites(("ha 3", "s 1 shy"))
    voice "ch1.8_s_049"
    s "..."

    $ show_sprites(("ha 3 shy", "s 1 shy")) 
    ha "..."

    $ show_sprites(("ha 3 shy", "s 3 sad")) 

    th "Ugh, this is so awkward... Or rather, I can't stand these gaps in the conversation!"
    th "Even though there's so much I want to ask, I just don't know where to start..."

    voice "ch1.8_ha_004"
    ha "U-um..."

    $ show_sprites(("ha 3 shy", "s 3 shy")) 
    voice "ch1.8_s_050"
    s "Ah, um..."

    $ show_sprites(("ha 3 sad", "s 3 shy")) 
    voice "ch1.8_ha_005"
    ha "Ah, sorry.{#ver2}"

    $ show_sprites(("ha 3 sad", "s 3 sad")) 
    voice "ch1.8_s_051"
    s "Ah, no, p-please go ahead."

    $ show_sprites(("ha 3 shy", "s 3 sad")) 
    voice "ch1.8_ha_006"
    ha "Um, no, Hiraga-kun should go first."

    $ show_sprites(("ha 3 shy", "s 3 shy")) 
    voice "ch1.8_s_052"
    s "No, not at all... You can go first."

    th "Waaah! Super awkward!"
    
    voice "ch1.8_ha_007"
    ha "Ah... um, well... It's really nothing, so..."

    voice "ch1.8_s_053"
    s "Nah, same here... yeah." 

    ha "..."

    voice "ch1.8_s_054"
    s "..."

    voice "ch1.8_s_055"
    s "Hey, um... There's something I want to ask you."
    
    play music t29 fadein 1.0
    $ show_sprites(("l 1 angry", "s 3 shy")) 

    voice "ch1.8_l_009"
    l "What is it? What do you want to ask?"

    $ show_sprites(("l 1 angry", "s 3 angry")) 
    voice "ch1.8_s_056"
    s "Huh, whoa!?"

    $ show_sprites(("l 1 angry", "s 1 angry")) 
    voice "ch1.8_s_057"
    s "Louise, where did you come from!? I thought you said you were going to class?"

    $ show_sprites(("l 1 happy", "s 1 angry")) 
    voice "ch1.8_l_010"
    l "Somebody somewhere was acting awfully suspicious, so I got worried and came back to check on the room. Good thing I came back!"


    $ show_sprites(("l 3 angry", "s 1 angry")) 
    voice "ch1.8_l_011"
    l "I wonder what exactly you were trying to do while your Master was in class?"

    $ show_sprites(("l 3 angry", "s 3 sad")) 
    voice "ch1.8_s_058"
    s "Uh, um...{#eto}"

    menu:
        "I thought I might clean the room a bit...":
            voice "ch1.8_s_059"
            s "Nah, I just realized I haven't done any room cleaning or anything at all today."

            $ show_sprites(("l 3 angry", "s 1 happy")) 
            voice "ch1.8_s_060"
            s "I figured I might as well do it while my Master is busy with her studies, you know."

            $ show_sprites(("l 3 happy", "s 1 happy")) 
            voice "ch1.8_l_012"
            l "Oh, really?{#ver2}"

            $ update_sympathy(20, char_key="louise")  
            voice "ch1.8_s_061"
            s "Yeah, yeah.{#dada}"

            voice "ch1.8_l_013"
            l "That's rather commendable attitude for a familiar, I must say."

            voice "ch1.8_s_062"
            s "Heh-heh, maybe."

            voice "ch1.8_l_014"
            l "Still, it's not like it's something you should do without my knowing..."

            $ show_sprites(("l 3 happy", "s 3 happy")) 
            voice "ch1.8_s_063"
            s "No, look. A good familiar is someone who takes care of things before being asked, isn't he?"

            $ show_sprites(("l 3", "s 3 happy")) 
            voice "ch1.8_l_015"
            l "Hmmm. Well, I'll accept that explanation for today."

            $ show_sprites(("ha 3 sad", "s 3 happy")) 
            voice "ch1.8_ha_008"
            ha "Hiraga-kun... Totally whipped..."

            $ show_sprites(("ha 3 sad", "s 1 sad")) 
            voice "ch1.8_s_066"
            s "Wh-what!? Ah, no, that's not true... I'd like to think so."

        "Nothing special.":
            voice "ch1.8_s_067"
            s "Um... nothing."

            voice "ch1.8_l_018"
            l "Huh?{#a}"

            $ show_sprites(("ha 3 angry", "s 3 sad")) 
            voice "ch1.8_ha_009"
            ha "Eh?{#e?}"

            $ show_sprites(("ha 3 angry", "s 1"))
            voice "ch1.8_s_068"
            s "No, really. I just felt like it, so I came here. There's no particular reason, that's just how it is."

            $ show_sprites(("ha 3 sad", "s 1"))
            voice "ch1.8_ha_010"
            ha "Hiraga-kun..."

            $ update_sympathy(-20, char_key="haruna")  

            $ show_sprites(("l 3 angry", "s 1"))
            voice "ch1.8_l_019"
            l "What's that supposed to mean. Think of a better reason, would you!"

            $ show_sprites(("l 3 angry", "s 3 sad"))
            voice "ch1.8_s_069"
            s "Even if you tell me to think of one..."

            $ show_sprites(("l 1 sad", "s 3 sad"))
            voice "ch1.8_l_020"
            l "Haa... Getting really mad over something like this... it's ridiculous."

            $ show_sprites(("l 1 sad", "ha 3 sad"))
            voice "ch1.8_ha_011"
            ha "That's right. Louise-san is absolutely correct."

            voice "ch1.8_l_021"
            l "Don't you think?"

            voice "ch1.8_ha_012"
            ha "Yes."

            $ show_sprites(("l 1 sad", "s 1 sad"))
            th "Huh, why are you two agreeing all of a sudden?!"
        
        "There's something I want to ask Haruna right away...":
            $ show_sprites(("l 3 angry", "s 1")) 
            voice "ch1.8_s_070"
            s "I had something I needed to ask Haruna right away. I couldn't just wait until class ended."

            $ show_sprites(("ha 3 shy", "s 1")) 
            voice "ch1.8_ha_013"
            ha "Hiraga-kun..."

            $ update_sympathy(20, char_key="haruna")  
            $ update_sympathy(-20, char_key="louise")  

            $ show_sprites(("l 1 angry", "s 1")) 
            voice "ch1.8_l_022"
            l "Hmmm. So what exactly do you want to ask? Go ahead and ask it right now, with me watching."

            $ show_sprites(("l 1 angry", "s 1 sad")) 
            voice "ch1.8_s_071"
            s "N-no, the thing is... Nothing's coming to me. So, you see, I'm stuck."

            $ show_sprites(("l 3 angry", "s 1 sad")) 
            voice "ch1.8_l_023"
            l "So, you were trying to ask something you didn't want me to find out about, weren't you?"

            voice "ch1.8_s_072"
            s "E-eh, what!? W-wait a minute..."

            $ show_sprites(("l 2 angry", "s 1 sad")) 
            voice "ch1.8_l_024"
            l "Words are useless!!"

            stop music fadeout 4.0
            $ scene_fx("blow flash", sound="blow_2", duration=(0.5, 4), sprites=("l 1", "s 1 sad"))
            pause(1)

    stop music fadeout 1.0
    $ show_sprites(("l 1", "s 1 sad")) 
    play music t18 fadein 1.0

    voice "ch1.8_l_016"
    l "Well, fine. We can't get back to class now anyway, so let's wait here for the others."

    $ show_sprites(("l 1", "s 1 angry"))
    voice "ch1.8_s_064"
    s "Huh?{#eee}" 

    $ show_sprites(("l 1 angry", "s 1 angry"))
    voice "ch1.8_l_017"
    l "Any complaints?"

    $ show_sprites(("l 1 angry", "s 1 sad"))
    voice "ch1.8_s_065"
    s "...n-none."

    return


label hallway_ch1_8:
    $ fade_fx("hallway_down_night", new_music="t18")
    
    $ show_sprites(("s 1"))
    voice "ch1.8_s_073"
    s "..."
    th "Looks like I don't know anyone here."
    voice "ch1.8_s_074"
    s "..."
    th "Then again, I don't really have any business here. I suppose I should just head back."    

    return