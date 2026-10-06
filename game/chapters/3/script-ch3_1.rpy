# Глава 3, часть 1 (сцены 137–146): утро в комнате Луизы — спор о четвёртом,
# коридор — разговор с Гишем. Титульная карточка: K=8.

label ch3:
    call overlay_screen("overlay",  "Chapter Three: 'A Woman's Battle'", isUseBlur=False, text_mode="black") from _call_overlay_screen_8
    pause(2)


     # звук птиц

    # ==== SCENE 137 ====
    $ fade_fx("sky", new_music="t4")

    voice "ch3_ha_001"
    ha "Nn— mmm... Ahh, it's so bright."

    $ fade_fx("louise_room")

    $ show_sprites("ha 3")
    voice "ch3_ha_002"
    ha "Hah... Morning's come around again..."

    $ show_sprites("ha 3 sad")
    voice "ch3_ha_003"
    ha "The morning light's no different from Japan's, is it..."

    voice "ch3_ha_004"
    ha "I wonder when I'll ever get used to living in this world..."

    $ show_sprites("ha 3 shy")
    voice "ch3_ha_005"
    ha "But that's fine. Right now, Hiraga-kun is right beside me...!?"

    $ show_sprites("ha 3 angry")
    voice "ch3_ha_006"
    ha "Eh...?{#ch3_ha_006}"

    # BGM stop + CG «все в кровати» + новый трек
    $ show_sprites(None)
    $ dissolve_fx("id(114)", stop_music=True, new_music="t29", type="cg")

    voice "ch3_ha_007"
    ha "Why is Hiraga-kun sleeping between Louise-san and Siesta-san!? He was supposed to be on the floor, wasn't he!?"

    voice "ch3_ha_008"
    ha "Wake up, wake up! Hiraga-kun, wake up!"

    # тряска слоёв (vibrate=7), затем сброс состояний
    $ shake_fx(duration=0.8)

    $ fade_fx("louise_room")

    $ show_sprites("s 5 angry")
    voice "ch3_s_001"
    s "Wha— whoa—!? What's going on!?"

    $ show_sprites(("l 4 sad", "s 5 angry"))
    voice "ch3_l_001"
    l "Jeez, what is it? You're so noisy..."

    $ show_sprites(("l 4 sad", "si 6 sad"))
    voice "ch3_si_001"
    si "...Ah, good morning."

    $ show_sprites(None)
    $ show_sprites("ha 3 angry")
    voice "ch3_ha_009"
    ha "Ah— you two! Why are you sleeping next to Hiraga-kun!?"

    $ show_sprites(("l 4", "ha 3 angry"))
    voice "ch3_l_002"
    l "Why? It's obvious, isn't it? Saito is my familiar, so of course we'd sleep together."

    th "What is Louise even saying... She's the one who dragged me into bed by force yesterday..."

    th "What's more, both Louise and Siesta insisted on using my arm as a pillow..."

    th "As a result, my arm aches like crazy, but..."

    voice "ch3_ha_010"
    ha "Th-then why is Siesta-san here!?"

    $ show_sprites(("si 6 angry", "ha 3 angry"))
    voice "ch3_si_002"
    si "I had already decided to share a bed with Miss Valiere from the start, so I don't think there's any problem."

    $ show_sprites("ha 3 angry", side="right")
    voice "ch3_ha_011"
    ha "Even if the bed is big, with three people in it, Hiraga-kun's in the way too, right?"

    $ show_sprites(("ha 3 angry", "s 5"))
    voice "ch3_s_002"
    s "Huh? I'm..."

    # ==== CHOISE (scene 137) ====
    menu:
        "I didn't think it was a bother.{#ch3_m137a}":
            # ==== SCENE 138 ====
            voice "ch3_s_003"
            s "I didn't think it was a bother."

            $ show_sprites(("ha 3 angry", "s 6 happy"))
            voice "ch3_s_004"
            s "Even if it's the three of us, just being able to sleep on the bed makes me happy."

            $ show_sprites(None)
            $ show_sprites("si 6 sad")
            voice "ch3_si_003"
            si "Saito-san...{#ch3_si_003}"

            $ show_sprites(("l 4 sad", "si 6 sad"))
            voice "ch3_l_003"
            l "Saito...{#ch3_l_003}"

            $ show_sprites(None)
            $ show_sprites("ha 3 sad", side="left")
            voice "ch3_ha_012"
            ha "Hiraga-kun...{#ch3_ha_012}"

            th "Huh? Everyone's looking at me with pity, aren't they..."

            jump ch3_141

        "Now that you mention it, it might be cramped.{#ch3_m137b}":
            # ==== SCENE 139 ====
            # фон/музыка/спрайты уже в этом состоянии (ветка = no-op)
            voice "ch3_s_005"
            s "Now that you mention it, it might have been cramped."

            voice "ch3_ha_013"
            ha "It was a bother after all, wasn't it!"

            $ show_sprites(("ha 3 angry", "s 6 sad"))
            voice "ch3_s_006"
            s "But it's not my bed, so it's not for me to say whether it was cramped."

            $ show_sprites(("ha 3 angry", "s 6 happy"))
            voice "ch3_s_007"
            s "Well, I used to sleep on straw, so I can sleep anywhere now, I guess. Ahahaha..."

            $ show_sprites(("ha 3 sad", "s 6 happy"))
            voice "ch3_ha_014"
            ha "I-Is that so..."

            jump ch3_141

        "How about the four of us sleep together?{#ch3_m137c}":
            # ==== SCENE 140 ====
            # фон/музыка/спрайты уже в этом состоянии (ветка = no-op)
            $ show_sprites(("ha 3 angry", "s 6"))
            voice "ch3_s_008"
            s "How about we try sleeping with four of us?"

            $ show_sprites(("l 4", "s 6"))
            voice "ch3_l_004"
            l "Huh?{#ch3_l_004}"
            $ update_sympathy(-10, char_key="louise")

            $ show_sprites(("l 4", "si 6 sad"))
            voice "ch3_si_004"
            si "Miss Valiere! Saito-san, Saito-san!!"
            $ update_sympathy(-10, char_key="siesta")

            $ show_sprites(None)
            $ show_sprites("s 5 sad", side="right")
            voice "ch3_s_009"
            s "Hey, wait a second. There was still room on the bed with three of us, right?"

            $ show_sprites("s 6 sad", side="right")
            voice "ch3_s_010"
            s "I was thinking maybe we could take a crack at four..."

            $ show_sprites(("ha 3 angry", "s 6 sad"))
            voice "ch3_ha_015"
            ha "Hiraga-kun, you're the worst!"
            $ update_sympathy(-10, char_key="haruna")

            $ show_sprites(("ha 3 angry", "s 5 sad"))
            voice "ch3_s_011"
            s "Wh-what!? ...Eh?"

            jump ch3_141

label ch3_141:
    # ==== SCENE 141 ====
    # линии 200–205: мимолётный спрайт Харуны поглощён очисткой состояния
    $ show_sprites(None)
    $ show_sprites("l 4")

    voice "ch3_l_005"
    l "See? That's what I said, didn't I? When I say it's fine, it's fine."

    $ show_sprites(("l 4", "si 6"))
    voice "ch3_si_005"
    si "That's right, Haruna-san. We're freeloading in Miss Valiere's room."

    voice "ch3_si_006"
    si "We shouldn't make too many demands, you know?"

    $ show_sprites(None)
    $ show_sprites("s 6 sad", side="right")
    voice "ch3_s_012"
    s "Is that really being so demanding?"

    $ show_sprites(("si 6 angry", "s 6 sad"))
    voice "ch3_si_007"
    si "It certainly is a demand!"

    $ show_sprites(None)
    $ show_sprites("l 4", side="left")
    voice "ch3_l_006"
    l "Never mind that— Haruna!"

    $ show_sprites(("l 4", "ha 3"))
    voice "ch3_ha_016"
    ha "Y-yes.{#ch3_ha_016}"

    voice "ch3_l_007"
    l "You're sick, aren't you?"

    voice "ch3_ha_017"
    ha "Yes, I am, but..."

    voice "ch3_l_008"
    l "Then you have to get proper rest, don't you?"

    $ show_sprites(("ha 3", "si 6"))
    voice "ch3_si_008"
    si "That's right, Haruna-san. If you don't rest properly, even an illness that would heal on its own won't get better."

    $ show_sprites(("ha 3 sad", "si 6"))
    voice "ch3_ha_018"
    ha "Nn... R-right... I'll be good and stay put."

    $ show_sprites("si 6", side="right")
    $ show_sprites(("l 4 happy", "si 6"))
    voice "ch3_l_009"
    l "Now then, don't hold back— sleep, sleeeep."

    $ show_sprites(("l 4 happy", "si 6 happy"))
    voice "ch3_si_009"
    si "That's right. If you don't lie down, it'll be bad for your health—"

    th "...Why is it that, even though they're both smiling, I feel something scary?"

    $ show_sprites(("l 4 happy", "d 1 sad", "si 6 happy"))
    voice "ch3_d_001"
    d "Good grief, women are terrifying, aren't they..."

    $ show_sprites(("l 4", "d 1 sad", "si 6 happy"))
    voice "ch3_l_010"
    l "What was that?"

    voice "ch3_d_002"
    d "N-no, no... It's nothing at all..."

    $ show_sprites(None)

    # ==== SCENE 142 ====
    play sound close_door
    $ fade_fx("hallway", new_music="t18")

    $ show_sprites("s 1", side="right")
    th "Ever since Siesta and Haruna started coming to Louise's room, waiting outside while they change has become part of my routine."

    $ show_sprites("s 3 sad", side="right")
    th "What exactly was my position, when I used to help Louise dress..."

    voice "ch3_g_001"
    g "Hi. What are you doing in a place like this?"

    $ show_sprites("s 1 sad", side="right")
    voice "ch3_s_013"
    s "Hm? ...Oh, it's you, Guiche."

    $ show_sprites(("g 1", "s 1 sad"))
    voice "ch3_g_002"
    g "'What do you mean, what' — that's rather rude of you."

    $ show_sprites(("g 1 happy", "s 1 sad"))
    voice "ch3_g_003"
    g "...Never mind. A noble does not lose his temper so easily. Be grateful for my magnanimity."

    $ show_sprites(("g 1 happy", "s 1"))
    voice "ch3_s_014"
    s "Yeah, yeah, thanks, thanks... More to the point, what are you doing here, Guiche? This is the girls' dorm, isn't it?"

    $ show_sprites(("g 2", "s 1"))
    voice "ch3_g_004"
    g "Montmorency asked me to come. Ah, it's tough being a popular guy."

    th "Whatever— he was probably summoned because Monmon found out he was fooling around, or something."

    $ show_sprites(("g 1", "s 1"))
    voice "ch3_g_005"
    g "Did you say something?"

    $ show_sprites(("g 1", "s 3"))
    voice "ch3_s_015"
    s "Nah, nah, nothing at all."

    voice "ch3_g_006"
    g "By the way, why were you kicked out of the room? Did you make Louise angry again, perhaps?"

    $ show_sprites(("g 1", "s 1"))
    voice "ch3_s_016"
    s "I didn't make her mad or anything. They're changing inside, so they just made me wait outside."

    $ show_sprites(("g 2", "s 1"))
    voice "ch3_g_007"
    g "I see, that's a tough break..."

    $ show_sprites(("g 2", "s 1 sad"))
    voice "ch3_s_017"
    s "Yeah, well."

    $ show_sprites(("g 2", "d 1 happy", "s 1 sad"))
    voice "ch3_d_003"
    d "You say all that, but deep down don't you want to go inside, partner?"

    $ show_sprites(("g 2", "s 1 sad"))
    $ show_sprites(("g 2", "s 1 angry"))
    voice "ch3_s_018"
    s "D-don't be ridiculous. There's no way I'd do something that scary."

    $ show_sprites(("g 1", "s 1 angry"))
    voice "ch3_g_008"
    g "Why would it be scary? I hear you used to help Louise dress, didn't you?"

    $ show_sprites(("g 1", "s 1"))
    voice "ch3_s_019"
    s "That and this are two different stories."

    $ show_sprites(("g 1", "d 1", "s 1"))
    voice "ch3_d_004"
    d "Still, I truly admire your patience, partner."

    $ show_sprites(("g 1", "s 1"))
    $ show_sprites(("g 1 shy", "s 1"))
    voice "ch3_g_009"
    g "By the way, Saito, who's your type?"

    $ show_sprites(("g 1 shy", "s 1 angry"))
    voice "ch3_s_020"
    s "Where did that come from?"

    $ show_sprites(("g 2", "s 1 angry"))
    voice "ch3_g_010"
    g "Just personal curiosity. I wanted to know how it feels, living with three girls."

    $ show_sprites(("g 2", "s 1 sad"))
    th "You've always got a few girls hanging around, haven't you?"

    $ show_sprites(("g 1", "s 1 sad"))
    voice "ch3_g_011"
    g "Hm? Did you say something?{#ch3_g_011}"

    $ show_sprites(("g 1", "s 1"))
    voice "ch3_s_021"
    s "N-Nah. Besides, there's no way I'd say something that embarrassing."

    $ show_sprites(("g 1 happy", "s 1"))
    voice "ch3_g_012"
    g "We're such good friends, aren't we? Won't you tell me in secret?"

    $ show_sprites(("g 1 happy", "s 3 sad"))
    voice "ch3_s_022"
    s "W-well..."

    # ==== CHOISE (scene 142) ====
    menu:
        "Probably Louise.{#ch3_m142a}":
            # ==== SCENE 143 ====
            $ show_sprites(("g 1 happy", "s 1"))
            voice "ch3_s_023"
            s "It's Louise after all. Then again, that's only because Louise is my master. I don't have any weird feelings for her."

            $ show_sprites(("g 1", "s 1"))
            voice "ch3_g_013"
            g "I see. So you're putting your master first, as a familiar."

            $ show_sprites(("g 1 happy", "s 1"))
            voice "ch3_g_014"
            g "Well, quite. I can't imagine a commoner like you could ever do anything with a noble like Louise."

            $ show_sprites(("g 1 happy", "s 1 sad"))
            voice "ch3_s_024"
            s "Uh-huh. I'm ever so sorry."

            jump ch3_146

        "Maybe Siesta?{#ch3_m142b}":
            # ==== SCENE 144 ====
            $ show_sprites(("g 1 happy", "s 1"))
            voice "ch3_s_025"
            s "I guess Siesta's on my mind... Then again, that's all it is— we're nothing like that."

            voice "ch3_g_015"
            g "I see, the maid girl. She seems honest and dependable— she'd suit you well, don't you think?"

            $ show_sprites(("g 1 happy", "s 3 sad"))
            voice "ch3_s_026"
            s "Come to think of it, don't you have any maids or something in your room? You're a noble, aren't you?"

            $ show_sprites(("g 1", "s 3 sad"))
            voice "ch3_g_016"
            g "I'm not exactly rich enough to bring a retainer along, you see. I didn't bring one to the academy."

            $ show_sprites(("g 1", "s 1"))
            voice "ch3_s_027"
            s "I see...{#ch3_s_027}"

            jump ch3_146

        "Maybe Haruna?{#ch3_m142c}":
            # ==== SCENE 145 ====
            $ show_sprites(("g 1 happy", "s 1"))
            voice "ch3_s_028"
            s "Haruna, maybe? We were classmates, so it'd be a lie to say she's not on my mind."

            voice "ch3_s_029"
            s "Then again, that's all it is— we're nothing like that."

            $ show_sprites(("g 1", "s 1"))
            voice "ch3_g_017"
            g "Haruna? Ah, that girl. She's got a mysterious air about her."

            $ show_sprites(("g 1", "s 3 sad"))
            voice "ch3_s_030"
            s "R-really?{#ch3_s_030}"

            voice "ch3_g_018"
            g "Yeah. Girls like her tend to hide a lot about themselves, so you need to be careful, Saito."

            $ show_sprites(("g 1", "s 1"))
            voice "ch3_s_031"
            s "Alright, I'll keep that in mind."

            jump ch3_146

label ch3_146:
    # ==== SCENE 146 ====
    $ show_sprites(("g 1 happy", "s 1 sad"))

    voice "ch3_l_011"
    l "Saito~ I'm done changing, so come on in."

    $ show_sprites(("g 1", "s 1 sad"))
    voice "ch3_g_019"
    g "Oh, your master is calling you, Saito."

    $ show_sprites(("g 1", "s 1"))
    voice "ch3_s_032"
    s "Yeah, yeah. Then I'd better head back to the room."

    $ show_sprites(("g 1", "s 1 angry"))
    voice "ch3_s_033"
    s "By the way— don't go telling anyone about what just happened."

    $ show_sprites(("g 2", "s 1 angry"))
    voice "ch3_g_020"
    g "I know, I know. I'm a tight-lipped fellow, after all."

    $ show_sprites(("g 2", "s 1 sad"))
    th "Monmon said the very same thing, and then blabbed everything..."

    $ show_sprites(("g 2", "s 1"))
    voice "ch3_s_034"
    s "Alright, I'm counting on you. See ya."

    $ show_sprites(None)

    jump attention
