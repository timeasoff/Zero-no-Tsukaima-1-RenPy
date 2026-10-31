# hallway night
label ch1_3:
    $ fade_fx("sky_night", new_music="t19", type="cg")
    th "Phew... what a crazy day..."
    $ fade_fx("hallway_night")

    $ show_sprites(("s 3 sad"))
    th "Maybe I should go somewhere before going to bed?"

    $ sprite_choice([
        {"char": "siesta",      "text": "Siesta's Room", "target": "si_room_ch1_3"},
        {"char": "louise",      "text": "Louise's Room", "target": "l_room_ch1_3"},
        {"char": "montmorency", "text": "Hallway",       "target": "hallway_ch1_3"},
    ])

    jump ch1_4
    return


label si_room_ch1_3:
    $ fade_fx("hallway_night", new_music="t6", sprites=("s 1"))
    
    play sound knock_door
    pause(1)
    voice "ch1.3_si_001"
    si "Yes?"

    voice "ch1.3_s_019"
    s "Ah, Siesta? It's me... mind if I come in?"

    voice "ch1.3_si_002"
    si "Ah, Saito-san? Please, come in."

    call open_door("right", "si_room_night") from _call_open_door_1

    $ show_sprites(("s 1", "si 1"), anim="slide_right")
    voice "ch1.3_si_003"
    si "What's the matter, Saito? Did you happen to forget something, perhaps?"

    voice "ch1.3_s_020"
    s "No, not really... I just felt like dropping by, I guess."

    $ show_sprites(("s 3", "si 1"))
    voice "ch1.3_s_021"
    s "I just wanted to drop by one last time before bed, that's all. Hope I'm not bothering you?"

    $ show_sprites(("s 3", "si 1 shy"))
    voice "ch1.3_si_004"
    si "Oh, no, not at all! I could never think of you as a bother. I... well, actually, you are more than welcome."

    $ update_sympathy(20, char_key="siesta")
    
    voice "ch1.3_s_022"
    s "R-really? But I'm sorry about that... dropping a sick person on you so suddenly and all."

    $ show_sprites(("s 3", "si 1"))
    voice "ch1.3_si_005"
    si "No, please don't worry about that. We help each other out in times of need. Besides, I'm worried too, since she still hasn't woken up."

    voice "ch1.3_si_006"
    si "I'll nurse her whenever I have a free moment from my chores. So please, Saito-san, just go to sleep and don't worry about a thing."

    $ show_sprites(("s 1", "si 1"))
    voice "ch1.3_s_023"
    s "Got it. Thank you, Siesta."

    voice "ch1.3_si_007"
    si "Oh, geez. I've told you time and time again, but please don't worry about it at all, okay?"

    voice "ch1.3_s_024"
    s "Yeah. But I just really felt like I had to thank you, you know?"

    $ show_sprites(("s 1", "si 1 happy"))
    voice "ch1.3_si_008"
    si "...Hehe."

    $ show_sprites(("s 1", "si 1"))
    voice "ch1.3_si_009"
    si "But... This person's hair and skin color. They're the same as Saito-san's and mine, aren't they?"
    
    voice "ch1.3_s_025"
    s "Yeah..."

    voice "ch1.3_si_010"
    si "This is just my imagination... but is this person from the same country as Saito-san and my great-grandfather?"

    voice "ch1.3_s_026"
    s "That is..."

    menu:
        "You might be right.":
            voice "ch1.3_s_027"
            s "Probably, that might be the case. But you won't know the details unless you ask the person themselves."

            voice "ch1.3_si_011"
            si "Is that so... Someone from the same country as Saito-san... Then, Saito-san must be curious too, right?"

            $ update_sympathy(10, char_key="siesta")
            $ tndl(-30)

            $ show_sprites(("s 3 sad", "si 1"))
            voice "ch1.3_s_028"
            s "Eh? W-well, yeah."

            voice "ch1.3_s_029"
            s "But right now, I have no idea what's going on at all."

            voice "ch1.3_si_012"
            si "I suppose so."
        #neutral
        "I doubt it's just a coincidence.":
            $ show_sprites(("s 3 sad", "si 1"))
            voice "ch1.3_s_035"
            s "I don't think it's a coincidence. I doubt there are many people in the same circumstances as me."

            voice "ch1.3_si_018"
            si "I suppose so."
        "I don't really know.{#var2}":
            voice "ch1.3_s_036"
            s "I wonder... I don't really understand it myself either."

            $ show_sprites(("s 1", "si 1 sad"))
            voice "ch1.3_si_019"
            si "Is that so?"

            $ update_sympathy(-10, char_key="siesta")
            $ tndl(30)

            $ show_sprites(("s 3 sad", "si 1 sad"))
            voice "ch1.3_s_037"
            s "Just like Siesta, there's also the possibility that their grandfather or father was from the same country as me. But you won't know unless you ask."

            $ show_sprites(("s 3 sad", "si 1"))
            voice "ch1.3_si_020"
            si "Ah, you're right."


    voice "ch1.3_si_013"
    si "This hair color and skin color. And also, the clothes from Saito-san's hometown..."

    $ show_sprites(("s 3 sad", "si 1 sad"))
    voice "ch1.3_si_014"
    si "...That's a bit too much of a coincidence to just be a coincidence, don't you think?"

    $ show_sprites(("s 1", "si 1 sad"))
    voice "ch1.3_s_030"
    s "Yeah. Maybe. But I don't want to get my hopes up just to be let down."

    voice "ch1.3_si_015"
    si "I thought so... You still want to keep hoping, don't you?"

    voice "ch1.3_s_031"
    s "W-well, I guess. It could be the lead I need to get back to my own world."

    voice "ch1.3_si_016"
    si "Your original world... is that so?"

    
    $ show_sprites(("s 3 sad", "si 1 sad"))
    voice "ch1.3_s_032"
    s "Ah, oh no. Is it already this late?"

    $ show_sprites(("s 3", "si 1 sad"))
    voice "ch1.3_s_033"
    s "Sorry for showing up so late. Anyway, see you tomorrow."

    $ show_sprites(("s 3", "si 1"))
    voice "ch1.3_si_017"
    si "Ah, right. Good night, Saito-san."

    voice "ch1.3_s_034"
    s "Ah, good night, Siesta."

    call open_door("left", stop_music=True) from _call_open_door_2

    return
label l_room_ch1_3:
    $ fade_fx("louise_room_night", new_music="t5")

    $ show_sprites(("s 1"))
    voice "ch1.3_s_038"
    s "Phew, good grief."

    $ show_sprites(("l 1 angry", "s 1"))
    $ update_sympathy(20)

    voice "ch1.3_l_001"
    l "No 'good grief' for you. You'll rest when you finish your work!"
    
    $ show_sprites(("l 1 angry", "s 3 angry"))
    voice "ch1.3_s_039"
    s "What!? That's not fair, wifey!?"

    voice "ch1.3_l_002"
    l "Who are you calling wifey!"

    voice "ch1.3_l_003"
    l "Did you do the laundry? Did you clean your room? Did you put away the things you bought?"

    $ show_sprites(("l 1 angry", "s 1 angry"))
    voice "ch1.3_s_040"
    s "Ah, geez, don't dump it all on me at once! I can't possibly finish that many chores in one go."

    $ show_sprites(("l 3 angry", "s 1 angry"))
    voice "ch1.3_l_004"
    l "Then stop talking and get to work! No rest until you're done!"

    $ show_sprites(("l 3 angry", "s 3 sad"))
    voice "ch1.3_s_041"
    s "Huh?{#eee}"

    voice "ch1.3_l_005" 
    l "Do you have any complaints!?"

    $ show_sprites(("l 3 angry", "s 1 sad"))
    voice "ch1.3_s_042"
    s "...Alright, alright."

    $ show_sprites(("l 1 sad", "s 1 sad"))
    voice "ch1.3_l_006"
    l "..."

    voice "ch1.3_s_043"
    s "...Louise? What's wrong?"

    voice "ch1.3_l_007"
    l "Um... um, you know? I was just wondering if I could ask you something."

    $ show_sprites(("l 1 sad", "s 1"))
    voice "ch1.3_s_044"
    s "What is it?"

    voice "ch1.3_l_008"
    l "Saito... Do you... want to go back home? To your world?"

    $ show_sprites(("l 1 sad", "s 3 sad"))
    s "Huh...?"

    menu:
        "Yeah, I want to go back.":
            $ show_sprites(("l 1 sad", "s 3"))
            voice "ch1.3_s_045"
            s "Ah, I really want to go home. I don't know when that'll be, but I'm definitely going back. That's my main goal right now, after all."

            voice "ch1.3_l_009"
            l " ...Yes. That's right, isn't it... As I thought."

            $ show_sprites(("l 1 sad", "s 1"))
            voice "ch1.3_s_046"
            s "What's wrong with that?"

            voice "ch1.3_l_010"
            l "It's nothing!"

        "I've already forgotten about my world.":
            $ show_sprites(("l 1 sad", "s 1"))
            voice "ch1.3_s_049"
            s "I've already forgotten about my original world. This place is my home now."

            $ show_sprites(("l 3", "s 1"))
            voice "ch1.3_l_013"
            l "...Liar."

            $update_sympathy(-10)
            $ tndl(-30)
            $ show_sprites(("l 3", "s 3 angry"))
            voice "ch1.3_s_050"
            s "What's with that? I thought you were gonna ask me a question, but instead you're calling me a liar."

            voice "ch1.3_l_014"
            l "Saying you don't want to go back to your original world is obviously a lie."
            $ show_sprites(("l 3", "s 3 sad"))
            voice "ch1.3_s_051"
            s "...That is, well..."

            voice "ch1.3_l_015"
            l "You shouldn't tell such transparent lies. You realize how disrespectful that is, right?"

            $ show_sprites(("l 3", "s 1 sad"))
            voice "ch1.3_s_052"
            s "...Sorry."

            $ show_sprites(("l 1", "s 1 sad"))
            voice "ch1.3_l_016"
            l "Just forget it."

        "I don't really know.":
            voice "ch1.3_s_053"
            s "«I don't really know right now. I mean, of course I want to go back, but..."

            voice "ch1.3_l_017"
            l "But?"

            $ show_sprites(("l 1 sad", "s 3 happy"))
            voice "ch1.3_s_054"
            s "Looks like I've already finished everything I was supposed to do in this world."

            $ show_sprites(("l 1 sad", "s 1"))
            voice "ch1.3_s_055"
            s "Honestly, I don't know if it's right to just abandon everything here and go back."

            $ show_sprites(("l 1", "s 1"))
            voice "ch1.3_l_018"
            l "Hmm.."

            $update_sympathy(10)
            $ tndl(30)

            
    $ show_sprites(("l 3", "s 1"))
    voice "ch1.3_l_011"
    l "Right then. You still have business to attend to, so hurry up and get to it!"

    $ show_sprites(("l 3", "s 1 angry"))
    voice "ch1.3_s_047"
    s "Wh-what the hell! Then don't talk to me!"

    $ show_sprites(("l 3 angry", "s 1 angry"))
    voice "ch1.3_l_012"
    l "Shut up, shut up! Hurry up and do your work!"

    $ show_sprites(("l 3 angry", "s 3"))
    voice "ch1.3_s_048"
    s "Yeah, yeah."

    $ show_sprites(None, anim="slide_right") 

    return
label hallway_ch1_3:
    $ fade_fx("hallway_down_night", new_music="t28")
    $ show_sprites(("m 1"))
    voice "ch1.3_m_001"
    m "Oh? What are you doing in a place like this?"

    $ show_sprites(("m 1", "s 1"))
    voice "ch1.3_s_001"
    s "Huh? Mont... morency."

    $ show_sprites(("m 1 angry", "s 1"))
    voice "ch1.3_m_002"
    m "That awkward pause just now is bugging me a little, but... whatever. What are you doing here at this hour? You're going to have Louise kicking up a fuss again."

    voice "ch1.3_s_002"
    s "Hmm, well, I just thought I'd take a stroll around here, that's all."

    $ show_sprites(("m 1", "s 1"))    
    voice "ch1.3_m_003"
    m "Hmm.."

    $ show_sprites(("m 1", "s 1 happy"))
    voice "ch1.3_s_003"
    s "Anyway, thanks a lot for earlier."

    voice "ch1.3_m_004"
    m "It's no big deal. You don't need to be so grateful, you know."

    voice "ch1.3_m_005"
    m "Commoner or noble, I'd never abandon someone who's sick."

    $ show_sprites(("m 1", "s 1"))
    voice "ch1.3_s_004"
    s "Yeah, well, that's true, but..."

    $ show_sprites(("m 1 happy", "s 1"))
    voice "ch1.3_m_006"
    m "Oh my?"

    $ show_sprites(("m 1 happy", "s 3 sad"))
    voice "ch1.3_s_005"
    s "W-what is it...? What's with that oddly amused look in your eyes?"

    voice "ch1.3_m_007"
    m "Saito. You... don't tell me you've fallen for that girl?"

    $ show_sprites(("m 1 happy", "s 3 shy"))
    voice "ch1.3_s_006"
    s "Eh!?"

    menu:
        "How did you know!?{#var1}":
            voice "ch1.3_s_008"
            s "How did you know!?{#var1}"

            $ show_sprites(("m 1 shy", "s 3 shy"))
            voice "ch1.3_m_008"
            m "Oh my? So it really was true? I was just trying to fish for a reaction..."
            $ tndl(-30)

            $ show_sprites(("m 1 shy", "s 3"))
            voice "ch1.3_s_009"
            s "No, no, it's just a joke. We just met today, so there's no way that's true, right?"

            $ show_sprites(("m 4", "s 3"))
            voice "ch1.3_m_009"
            m "My, my, my. I wonder if that's really true?"

            $ show_sprites(("m 4", "s 1 angry"))
            voice "ch1.3_s_010"
            s "Yeah, it's got absolutely nothing to do with it."

        "Why do you think that?":
            $ show_sprites(("m 1 shy", "s 3 sad"))
            voice "ch1.3_s_016"
            s "Why would you think that? I just happened to save that girl who collapsed on the road, that's all, right?"  

            $ show_sprites(("m 1 sad", "s 3 sad"))  
            voice "ch1.3_m_016"
            m "I wonder if it was really just a coincidence? Or did you actually arrange it all beforehand and stage a little play to get her into the academy... or something?"

            voice "ch1.3_s_017"
            s "Why would I go through all that trouble? Besides, Louise would be totally against it, right?"

            $ show_sprites(("m 4 sad", "s 3 sad"))
            voice "ch1.3_m_017"
            m "Hmmm?"

            $ show_sprites(("m 4 sad", "s 1 angry"))
            voice "ch1.3_s_018"
            s "Just believe me!"

        "Th-there's no way that's true, right?":
            voice "ch1.3_s_007"
            s "T-there's no way that's true, right?"

            $ show_sprites(("m 1 sad", "s 3 shy"))
            voice "ch1.3_m_014"
            m "Oh my? Am I wrong? My instincts are usually pretty good, though... Or maybe you have a crush on Louise?"

            $ tndl(30)
            $ show_sprites(("m 1 sad", "s 3 sad"))
            voice "ch1.3_s_014"
            s "N-no, I'm telling you, that's not it! And it's not like that with Louise either, I swear!"

            $ show_sprites(("m 4", "s 3 sad"))
            voice "ch1.3_m_015"
            m "Oh my? Then... that maid?"

            $ show_sprites(("m 4", "s 1 angry"))
            voice "ch1.3_s_015"
            s "Thaaat's wroong tooo!"

    $ show_sprites(("m 4 happy", "s 1 angry"))
    voice "ch1.3_m_010"
    m "Hmph. Well, I think I'll let it slide for today."

    $ show_sprites(("m 4 happy", "s 3 sad"))
    voice "ch1.3_s_011"
    s "It's the 'for today...' part that's oddly terrifying, though."

    $ show_sprites(("m 1", "s 3 sad"))
    voice "ch1.3_m_011"
    m "Don't sweat the small stuff. I know it's hard to believe, but I can keep a secret, you know?"

    voice "ch1.3_m_012"
    m "I'll keep quiet about that girl, too. You can rest assured of that."

    $ show_sprites(("m 1", "s 1 sad"))
    voice "ch1.3_s_012"
    s "I'm trusting you here! Please, don't let me down!"

    voice "ch1.3_m_013"
    m "Alright, alright. Well then, I'm heading back to my room. Good night, sleep well."

    $ show_sprites(("s 3 sad"))
    voice "ch1.3_s_013"
    s "Phew, what a relief. But... I wonder if it's really going to be okay..."
                
    return