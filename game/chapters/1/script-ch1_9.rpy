# комната луизы. ОБЩИЙ СБОР!
label ch1_9:
    $ fade_fx("louise_room", new_music="t18", sprites=("l 1"), duration=2)
    voice "ch1.9_l_001"
    l "Right then, everyone is assembled."

    $ show_sprites(("k 1", "t 1"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.9_k_001"
    k "Yes, everyone has gathered."

    t "..."

    $ show_sprites(("g 2 shy", "ha 1"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.9_g_001"
    g "Oh, lovely young lady. Would you be willing to become my personal maid?"

    $ show_sprites(("g 2 shy", "ha 1 sad"))
    voice "ch1.9_ha_001"
    ha "Eh, umm…"

    $ show_sprites(("g 2 shy", "m 4 angry"))
    voice "ch1.9_m_001"
    m "Guiche! You're drooling over every girl you see again!"

    $ show_sprites(("g 2 happy", "m 4 angry"))
    voice "ch1.9_g_002"
    g "Oh my, are you jealous? My dear Montmorency."

    voice "ch1.9_g_003"
    g "But don't worry. My heart will never forget you."

    $ show_sprites(("g 2 happy", "m 1 angry"))
    voice "ch1.9_m_002"
    m "All you do is say you won't forget me, but then you're immediately checking out other girls! How am I supposed not to worry after that?"

    $ show_sprites(("g 2 happy", "s 1 angry"))
    voice "ch1.9_s_001"
    s "Listen, did you even need to come? Take one look, and that's it—goodbye."

    $ show_sprites(("g 1 sad", "s 1 angry"))
    voice "ch1.9_g_004"
    g "What an impolite tone. I'm offering to lend you my strength, so you shouldn't speak to me like that."

    $ show_sprites(("g 1 sad", "l 1 sad"))
    voice "ch1.9_l_002"
    l "It can't be helped. Montmorency let it slip. Since it's come to this, I'll accept your help."

    $ show_sprites(("g 1 angry", "l 1 sad"))
    voice "ch1.9_g_005"
    g "Mmmmm… That's a rather humiliating way to put it, but… fine…"

    $ show_sprites(("g 1 angry", "k 1"))
    voice "ch1.9_k_002"
    k "Yes, yes. That's enough commotion."

    voice "ch1.9_k_003"
    k "First, we need to decide where she should stay… That's the biggest problem."

    $ show_sprites(("g 1 angry", "s 3 sad"))
    voice "ch1.9_s_002"
    s "Where she should stay… Can't it be here?"

    $ show_sprites(("g 2", "s 3 sad"))
    voice "ch1.9_g_006"
    g "Hiding a commoner in secret is a serious matter. In any case, it seems to me that this situation is beyond our capabilities."


    $ show_sprites(("l 1", "s 3 sad"))
    voice "ch1.9_l_003"
    l "Oh, it's fine. We'll have this girl leave right away."

    $ show_sprites(("l 1", "s 1 angry"))
    voice "ch1.9_s_003"
    s "What!? Wait, Louise!"

    $ show_sprites(("l 1 angry", "s 1 angry"))
    voice "ch1.9_l_004"
    l "What?"

    voice "ch1.9_s_004"
    s "You…"

    menu: 
        "Come on, can't something be done about that?":
            $ show_sprites(("l 1 angry", "s 3 sad"))
            voice "ch1.9_s_005"
            s "Come on, can't something be done about that?"

            voice "ch1.9_l_005"
            l "What do you mean by 'something'?"

            voice "ch1.9_l_006"
            l "Do you seriously think we're capable of hiding a commoner? That's just unrealistic."

            voice "ch1.9_s_006"
            s "B-but isn't that cruel?"

            $ update_sympathy(10, char_key="louise")
            $ tndl(30)

        "Don't say such awful things!":
            $ show_sprites(("l 1 angry", "s 1 angry"))
            voice "ch1.9_s_005-2"
            s "Don't say such awful things!"

            voice "ch1.9_l_005-2"
            l "What's awful about it? I'm just stating the obvious."

            $ update_sympathy(-10, char_key="louise")
            $ tndl(-30)

            $ show_sprites(("l 1 angry", "s 3 angry"))
            voice "ch1.9_s_006-2"
            s "You want to leave her all alone in this world! That's exactly what I mean when I say 'awful'!"

    $ show_sprites(("l 1", "s 3 angry"))
    voice "ch1.9_l_007"
    l "Actually, we brought this girl to the academy to look after her, since she had passed out on the road."

    $ show_sprites(("l 1", "s 3 sad"))
    voice "ch1.9_s_007"
    s "W-well, yeah. That's true, but…"

    voice "ch1.9_l_008"
    l "She seems to have recovered after resting for the night, so it is improper for an outsider to remain at the academy."

    voice "ch1.9_l_009"
    l "Am I saying something wrong?"

    voice "ch1.9_s_008"
    s "T-That's... Your logic isn't wrong, but... but that's just heartless!"

    $ show_sprites(("l 1 angry", "s 3 sad"))
    voice "ch1.9_l_010"
    l "Then how are we supposed to take care of her from now on?"

    voice "ch1.9_l_011"
    l "We're not talking about a dog or a cat here. It's obviously impossible to just keep her."

    $ show_sprites(("l 1 angry", "s 3 angry"))
    voice "ch1.9_s_009"
    s "What did you say...?!"

    $ show_sprites(("l 1 angry", "si 1 sad"))
    voice "ch1.9_si_001"
    si "U-Um, Saito-san, Miss Valliere, please calm down."

    $ show_sprites(("l 1 angry", "k 4"))
    voice "ch1.9_k_004"
    k "Hmph..."

    $ show_sprites(("l 1 angry", "k 4 happy"))
    voice "ch1.9_k_005"
    k "Hey, Louise? Could it be... you're jealous?"

    voice "ch1.9_l_012"
    l "Huh?{#a}"

    $ show_sprites(("l 1 angry", "k 1 happy"))
    voice "ch1.9_k_006"
    k "Are you trying to kick her out just because Saito is so devoted to her?"

    $ show_sprites(("l 3 angry", "k 1 happy"))
    voice "ch1.9_l_013"
    l "Wha...! I-I-I don't mean it like that!"

    $ show_sprites(("l 3 angry", "k 1"))
    voice "ch1.9_k_007"
    k "After all, sheltering her doesn't mean we can keep it up indefinitely, right?"

    voice "ch1.9_k_008"
    k "Still, that level of desperation is nothing short of jealousy!"

    $ show_sprites(("l 1 angry", "k 1"))
    voice "ch1.9_l_014"
    l "That can't be! Why would I be jealous of this Saito!"

    $ show_sprites(("l 1 angry", "k 1 happy"))
    voice "ch1.9_k_009"
    k "Then that's fine. Even if it's just for a while, why not shelter her?" 

    $ show_sprites(("l 1 sad", "k 1 happy"))
    voice "ch1.9_l_015"
    l "Ugh..."

    $ show_sprites(("l 1 sad", "s 1 sad"))
    voice "ch1.9_s_010"
    s "Louise, please. Just let her stay for a while."

    $ show_sprites(("l 3 angry", "s 1 sad"))
    voice "ch1.9_l_016"
    l "Fine! We just need to hide her for a while, right!"

    $ show_sprites(("l 3 angry", "k 4 happy"))
    voice "ch1.9_k_010"
    k "That settles it."

    $ show_sprites(("l 3 angry", "s 1"))
    voice "ch1.9_s_011"
    s "...Thanks, Louise."

    $ show_sprites(("ha 1 happy", "s 1"))
    voice "ch1.9_ha_002"
    ha "Thank you, Hiraga-kun." 

    $ show_sprites(("ha 1 happy", "s 3 shy"))
    voice "ch1.9_s_012"
    s "Huh? N-No, I didn't do anything..."

    $ show_sprites(("ha 1 happy", "s 3 happy"))
    voice "ch1.9_s_013"
    s "I mean, being thrown into this world all alone is tough, isn't it?"

    $ show_sprites(("g 1", "s 3 happy"))
    voice "ch1.9_g_007"
    g "But if she came from the same place as Saito, {i}'Japan'{/i}, doesn't she have a master who summoned her?"

    $ show_sprites(("g 1", "s 1 sad"))
    voice "ch1.9_s_014"
    s "Eh?{#e?}"

    voice "ch1.9_g_008"
    g "I'm just saying that, just like Louise, she might have a master who summoned her."

    $ show_sprites(("g 1", "s 1"))
    voice "ch1.9_s_015"
    s "Ah... I see. That possibility does exist, doesn't it." 

    $ show_sprites(("g 1", "l 1 angry"))
    voice "ch1.9_l_017"
    l "So you're saying the people who attacked us are actually the mages who summoned her, or their subordinates?"

    $ show_sprites(("g 2 angry", "l 1 angry"))
    voice "ch1.9_g_009"
    g "The people who attacked?"

    $ show_sprites(("g 2 angry", "s 3 happy"))
    voice "ch1.9_s_016"
    s "Well, it's nothing you need to worry about." 

    $ show_sprites(("k 1 angry", "s 3 happy"))
    voice "ch1.9_k_011"
    k "That could very well be. If so, she could possess a special ability just like Darling."

    $ show_sprites(("k 1 angry", "s 3 angry"))
    voice "ch1.9_s_017"
    s "A special ability... like mine?"

    th "My special ability as a familiar, the power to master any weapon... Could Haruna have that kind of ability too...?"

    $ show_sprites(("m 1 angry", "s 3 angry"))
    voice "ch1.9_m_003"
    m "Oh, I actually looked into that. There's no mark of a familiar contract anywhere on her." 

    $ show_sprites(("m 1 angry", "l 1"))
    voice "ch1.9_l_018"
    l "Ah, is that so?" 

    $ show_sprites(("m 1", "l 1"))
    voice "ch1.9_m_004"
    m "Yes. That is for sure."

    $ show_sprites(("m 1", "s 3 sad"))
    voice "ch1.9_s_018"
    s "Then that means..."  

    menu:
        "Isn't it possible that we overlooked something?":
            $ show_sprites(("m 1", "s 1"))
            voice "ch1.9_s_019"
            s "Is it possible Monmon overlooked it?" 

            $ show_sprites(("m 4 angry", "s 1"))
            voice "ch1.9_m_005"
            m "How rude. I looked properly, all over her body. But there was no crest anywhere."

            $ show_sprites(("m 4 angry", "g 1 shy"))
            voice "ch1.9_g_010"
            g "W-what, h-her whole body?"

            voice "ch1.9_g_011"
            g "Th-then, Montmorency, you looked at every single corner of this girl's body, didn't you?"

            voice "ch1.9_g_012"
            g "With your own eyes, leaving nothing unseen!"

            $ show_sprites(("m 1 sad", "g 1 shy"))
            voice "ch1.9_m_006"
            m "Uh, yes..."

            $ show_sprites(("m 1 sad", "g 2 shy"))
            voice "ch1.9_g_013"
            g "Aaaah. What an exquisite scenario! Ah, why wasn't I there too!"

            $ show_sprites(("m 4 angry", "g 2 shy"))
            voice "ch1.9_m_007"
            m "If you were there, I'd have thrown you out of the room!"  

            $ show_sprites(("m 4 angry", "s 3 shy"))
            th "Right, so while I was waiting out in the hall, Montmorency was up to that... Ah, I feel a nosebleed coming on."

            $ show_sprites(("l 2 angry", "s 3 shy"))
            voice "ch1.9_l_019"
            l "Saito? You just had a dirty thought, didn't you?"

            $ show_sprites(("l 2 angry", "s 3 sad"))
            voice "ch1.9_s_020"
            s "No, nothing of the sort!"

            $ show_sprites(("l 2 angry", "s 1"))
            voice "ch1.9_s_021"
            s "But that means she wasn't summoned as a familiar the way I was, right?"

            $ show_sprites(("l 1", "s 1"))
            voice "ch1.9_l_020"
            l "I can't say for sure, but that seems to be the case."

        "Was it by chance that she came to this world?":
            $ show_sprites(("m 1", "s 1"))
            voice "ch1.9_s_025"
            s "Does that mean she ended up in this world by coincidence? That instead of being summoned like me, she just happened to stumble in here?" 

            voice "ch1.9_m_008"
            m "I'm just saying that's a possibility. At the very least, she isn't a contracted familiar." 

            $ show_sprites(("k 1", "s 1 sad"))
            voice "ch1.9_k_014"
            k "For instance, maybe she was summoned but fled before the contract was finalized. That's a possibility too."

            voice "ch1.9_s_026"
            s "Hmmm..."

    voice "ch1.9_s_022"
    s "Well, but if we hear her full story, it might give a clue on how to return to Japan."

    $ show_sprites(("l 1", "s 3 happy"))
    voice "ch1.9_s_023"
    s "Anyway, I'll do whatever I can to help. So let's cheer up."

    $ show_sprites(("ha 1 shy", "s 3 happy"))
    voice "ch1.9_ha_003"
    ha "Yeah... Thank you, Hiraga-kun. Just having you here makes me feel so much more at ease."

    $ show_sprites(("ha 1 shy", "s 3 shy"))
    voice "ch1.9_s_024"
    s "R-really?"

    $ show_sprites(("l 1 angry"), anim_out="slide_right", mode="big")
    voice "ch1.9_l_021"
    l "..."

    $ show_sprites(("si 1 angry"), anim_out="slide_right", mode="big")
    voice "ch1.9_si_002"
    si "..."

    $ show_sprites(("k 4 happy"), anim_out="slide_right")
    voice "ch1.9_k_012"
    k "Oh my. It seems things are going to get quite interesting from here on out."

    $ show_sprites(("g 2", "k 4 happy"))
    voice "ch1.9_g_014"
    g "Eh? What is?"

    $ show_sprites(("g 2", "k 1"))
    voice "ch1.9_k_013"
    k "No, it's just my own business." 

    $ fade_fx("sky_night", new_music="t17", type="cg")
    voice "ch1.9_unk_001"
    unk "What's the situation with that girl?"

    voice "ch1.9_unds_001"
    unds "We found her collapsed on the road, but before we could make contact, a pair got to her first. We engaged in battle and were defeated." 

    voice "ch1.9_unk_002"
    unk "Two people?"

    voice "ch1.9_unds_002"
    unds "Yes, a young noble girl and a commoner with an intelligence sword."

    voice "ch1.9_unds_003"
    unds "It seems the girl was taken by those two and went to the Tristain Magical Academy."

    voice "ch1.9_unk_003"
    unk "Understood. Continue your surveillance as is. We will make our next move when the time is right."

    voice "ch1.9_unds_004"
    unds "Yes, sir."

    jump ch1_10
    return
        
    






