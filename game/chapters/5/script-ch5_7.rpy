# Глава 5, часть 7: сцена 341 + route branches 1134/1139.
# Generated from ps2_source/events_full/chapter_06_本当の想い.txt.

label ch5_7:
    $ fade_fx("id(53)")  # BG +53
    play music t27 fadein 1.0
    th "And at last, the day of the casting announcement had arrived.{#ch5.7_th_001}"
    $ show_sprites(())
    $ fade_fx("black")
    $ fade_fx("id(54)")  # BG +54
    $ show_sprites(("w 1 happy"))  # lay20 +1063
    voice "ch5.7_w_001"
    w "Everyone, good work. Now I'll announce the final casting. First, Prince Kane will be played by... Saito!{#ch5_7_v15991}"
    $ show_sprites(("w 1 happy", "g 2 sad"))  # lay4 +572
    voice "ch5.7_g_001"
    g "I-I wouldn't get a part anyway...{#ch5_7_v1517}"
    $ show_sprites(("g 2 sad"))
    $ show_sprites(("g 2 sad", "m 2 sad"))  # lay3 +869
    voice "ch5.7_m_001"
    m "W-well, well.{#ch5_7_v4086}"
    $ show_sprites(("m 2 sad"))
    $ show_sprites(())
    $ show_sprites(("w 1"))  # lay20 +1061
    $ show_sprites(("w 1", "s 1 happy"))  # lay5 +392
    voice "ch5.7_s_001"
    s "R-really? Is that all right?{#ch5_7_v11701}"
    voice "ch5.7_w_002"
    w "...You showed real talent. Have confidence in yourself.{#ch5_7_v15992}"
    voice "ch5.7_w_003"
    w "...I'll take the role of the enemy noble. A play needs a villain to hold together.{#ch5_7_v15993}"
    $ show_sprites(("w 1"))
    voice "ch5.7_w_004"
    w "Now, about the heroine, Princess Noelle...{#ch5_7_v15994}"
    $ show_sprites(())
    $ show_sprites(("l 6"))  # lay1 +314
    voice "ch5.7_l_001"
    l "…….{#ch5_7_v6257}"
    $ show_sprites(())
    $ show_sprites(("ha 2"))  # lay7 +963
    voice "ch5.7_ha_001"
    ha "…….{#ch5_7_v2377}"
    $ show_sprites(())
    $ show_sprites(("si 1"))  # lay2 +501
    voice "ch5.7_si_001"
    si "…….{#ch5_7_v14788}"
    $ show_sprites(())
    $ show_sprites(("k 1"))  # lay6 +688
    k "…….{#ch5.7_th_002}"
    $ show_sprites(())
    $ show_sprites(("t 1"))  # lay0 +633
    t "…….{#ch5.7_th_003}"
    $ show_sprites(())
    $ show_sprites(("m 2"))  # lay3 +864
    voice "ch5.7_m_002"
    m "…….{#ch5_7_v4087}"
    $ show_sprites(())
    $ show_sprites(("h 3"))  # lay8 +776
    voice "ch5.7_h_001"
    h "…….{#ch5_7_v578}"
    stop music fadeout 1.0
    $ show_sprites(())
    $ fade_fx("black")
    $ zero_route = compute_zero_route()
    if zero_route == 1:
        jump ch5_7_r1_louise
    elif zero_route == 2:
        jump ch5_8_r2_kirche
    elif zero_route == 3:
        jump ch5_8_r3_tabitha
    elif zero_route == 4:
        jump ch5_7_r4_siesta
    elif zero_route == 5:
        jump ch5_9_r5_henrietta
    else:
        jump ch5_9_r6_haruna

label ch5_7_r1_louise:
    $ fade_fx("id(54)")  # BG +54
    play music t4 fadein 1.0
    $ show_sprites(("w 1"))  # lay20 +1061
    voice "ch5.7_w_005"
    w "I choose Miss Vallière.{#ch5_7_v15842}"
    $ show_sprites(())
    $ show_sprites(("ha 2"))  # lay7 +962
    voice "ch5.7_ha_002"
    ha "Congratulations, Miss Louise.{#ch5_7_v1682}"
    $ show_sprites(())
    $ show_sprites(("l 6"))  # lay1 +313
    voice "ch5.7_l_002"
    l "Of course!{#ch5_7_v4747}"
    $ show_sprites(())
    $ show_sprites(("k 2 sad"))  # lay6 +693
    voice "ch5.7_k_001"
    k "Aww, I was hoping to win the heroine's part and make Louise stamp her feet.{#ch5_7_v2817}"
    $ show_sprites(())
    $ show_sprites(("h 3"))  # lay8 +775
    voice "ch5.7_h_002"
    h "Well, what is decided cannot be helped. Let us do our best in the roles we were given.{#ch5_7_v365}"
    $ show_sprites(())
    $ show_sprites(("t 5"))  # lay0 +632
    voice "ch5.7_t_001"
    t "Naturally.{#ch5_7_v15336}"
    $ show_sprites(())
    $ show_sprites(("w 1"))  # lay20 +1061
    voice "ch5.7_w_006"
    w "Then I will announce the rest of the casting. The old nobleman who raised him will be...{#ch5_7_v15843}"
    stop music fadeout 1.0
    $ show_sprites(())
    $ fade_fx("black")
    $ show_sprites(())
    $ show_sprites(())
    $ show_sprites(())
    $ show_sprites(())
    $ show_sprites(())
    $ show_sprites(())
    $ fade_fx("sky_night")  # BG +90
    th "……… …… …{#ch5.7_th_004}"
    th "And then the curtain rose. The play proceeded without a hitch, and swept toward its climax.{#ch5.7_th_005}"
    $ show_sprites(())
    $ fade_fx("black")
    $ fade_fx("id(142)", type="cg")
    play music t22 fadein 1.0
    voice "ch5.7_s_002"
    s "We can buy a little time here.{#ch5_7_v8743}"
    voice "ch5.7_l_003"
    l "I will negotiate with the enemy. If I return to the Empire, everything will be settled.{#ch5_7_v4748}"
    voice "ch5.7_s_003"
    s "But then I will lose you.{#ch5_7_v8744}"
    voice "ch5.7_l_004"
    l "But if we do nothing, the prince will lose both his kingdom and his life!{#ch5_7_v4749}"
    voice "ch5.7_s_004"
    s "What is a kingdom to me? What is death compared with that?{#ch5_7_v8745}"
    voice "ch5.7_s_005"
    s "Laugh at me. I fear living on after losing you more than I fear death or a ruined kingdom.{#ch5_7_v8746}"
    voice "ch5.7_l_005"
    l "Prince!{#ch5_7_v4750}"
    voice "ch5.7_s_006"
    s "Ah, my beloved. You cannot know how much I loved you.{#ch5_7_v8747}"
    voice "ch5.7_s_007"
    s "Love blinds everyone and drives them mad. The noblemen who whispered their love to you all met ruin trying to answer your riddles.{#ch5_7_v8748}"
    voice "ch5.7_s_008"
    s "But I can no longer laugh at their foolishness. I wagered this kingdom for you, and destroyed it myself!{#ch5_7_v8749}"
    voice "ch5.7_s_009"
    s "The castle is falling. Leave.{#ch5_7_v8750}"
    voice "ch5.7_s_010"
    s "The attacking soldiers will welcome you as their new queen with cries of joy!{#ch5_7_v8751}"
    voice "ch5.7_s_011"
    s "You will live and become queen.{#ch5_7_v8752}"
    voice "ch5.7_l_006"
    l "Ah, Prince!{#ch5_7_v4751}"
    voice "ch5.7_s_012"
    s "My beloved. But I have no regrets.{#ch5_7_v8753}"
    voice "ch5.7_s_013"
    s "My love for you was worth the price. If only... just once...{#ch5_7_v8754}"
    voice "ch5.7_s_014"
    s "I wanted to know what you truly felt.{#ch5_7_v8755}"
    voice "ch5.7_s_015"
    s "The enemy soldiers have reached the tower... There is no time left.{#ch5_7_v8756}"
    voice "ch5.7_l_007"
    l "Prince, do you remember the night you proposed to me?{#ch5_7_v4752}"
    voice "ch5.7_l_008"
    l "It was a beautiful night, like tonight. I will give you my answer now.{#ch5_7_v4753}"
    voice "ch5.7_s_016"
    s "Princess?{#ch5_7_v8757}"
    voice "ch5.7_l_009"
    l "Noelle will die here... as the prince's wife.{#ch5_7_v4754}"
    voice "ch5.7_g_002"
    g "There she is! The princess!{#ch5_7_v1412}"
    voice "ch5.7_l_010"
    l "…….{#ch5_7_v4755}"
    voice "ch5.7_s_017"
    s "Then let us go, Noelle. I will follow you wherever you go.{#ch5_7_v8758}"
    $ flash_fx("white")
    $ show_sprites(())
    $ show_sprites(())
    $ show_sprites(())
    $ fade_fx("id(53)")  # BG +53
    $ fade_fx("black")
    $ flash_fx("white")
    voice "ch5.7_t_002"
    t "And so the two of them threw themselves from the tower...{#ch5_7_v15337}"
    voice "ch5.7_t_003"
    t "They say white flowers eventually bloomed where the two of them fell, side by side...{#ch5_7_v15338}"
    stop music fadeout 1.0
    $ show_sprites(())
    $ show_sprites(())
    $ show_sprites(())
    $ show_sprites(())
    $ fade_fx("black")
    th "……… …… …{#ch5.7_th_006}"
    $ fade_fx("id(54)")  # BG +54
    play music t18 fadein 1.0
    $ show_sprites(("l 6"))  # lay1 +359
    voice "ch5.7_l_011"
    l "That was quite a passionate performance.{#ch5_7_v4756}"
    voice "ch5.7_s_018"
    s "...Well, just a little.{#ch5_7_v8759}"
    voice "ch5.7_w_007"
    w "Ladies and gentlemen, please give them one more grand round of applause!{#ch5_7_v15844}"
    $ show_sprites(("l 6"))  # lay1 +365
    voice "ch5.7_l_012"
    l "Saito, tell me... Was that confession real?{#ch5_7_v4757}"
    th "What am I supposed to say to that...{#ch5.7_th_007}"
    menu:
        "I meant it...{#ch5_7_c1135}":
            $ show_sprites(("l 6"))  # lay1 +365
            play music t18 fadein 1.0
            $ fade_fx("id(54)")  # BG +54
            voice "ch5.7_s_019"
            s "I was pretty serious about it...{#ch5_7_v8760}"
            $ show_sprites(())
            $ show_sprites(("l 6"))  # lay1 +366
            voice "ch5.7_l_013"
            l "Huh?{#ch5_7_v4758}"
            voice "ch5.7_s_020"
            s "N-no, it was nothing!{#ch5_7_v8761}"
            jump ch5_7_r1_rejoin
        "It was only a play!{#ch5_7_c1136}":
            $ show_sprites(("l 6"))  # lay1 +365
            play music t18 fadein 1.0
            $ fade_fx("id(54)")  # BG +54
            voice "ch5.7_s_021"
            s "I-it was only acting!{#ch5_7_v8762}"
            $ show_sprites(("l 6"))  # lay1 +363
            voice "ch5.7_l_014"
            l "R-right. ...Of course I knew that.{#ch5_7_v4759}"
            jump ch5_7_r1_rejoin
        "Change the subject{#ch5_7_c1137}":
            $ show_sprites(("l 6"))  # lay1 +365
            play music t18 fadein 1.0
            $ fade_fx("id(54)")  # BG +54
            voice "ch5.7_s_022"
            s "Ahahaha...{#ch5_7_v8763}"
            $ show_sprites(("l 6"))  # lay1 +361
            voice "ch5.7_l_015"
            l "Are you trying to laugh your way out of it?{#ch5_7_v4760}"
            voice "ch5.7_s_023"
            s "Please, spare me.{#ch5_7_v8764}"
            jump ch5_7_r1_rejoin
label ch5_7_r1_rejoin:
    $ show_sprites(("l 6"))  # lay1 +366
    play music t18 fadein 1.0
    $ fade_fx("id(54)")  # BG +54
    stop music fadeout 1.0
    $ show_sprites(("l 6"))
    $ show_sprites(("l 6"))
    $ show_sprites(())
    $ fade_fx("black")
    stop music fadeout 1.0
    $ fade_fx("black")
    jump ch5_10
label ch5_7_r4_siesta:
    $ fade_fx("id(54)")  # BG +54
    play music t4 fadein 1.0
    $ show_sprites(("w 1"))  # lay20 +1061
    voice "ch5.7_w_008"
    w "Siesta!{#ch5_7_v15845}"
    $ show_sprites(())
    $ show_sprites(("si 2"))  # lay2 +500
    voice "ch5.7_si_002"
    si "Huh? Me?{#ch5_7_v14284}"
    $ show_sprites(("si 2", "l 6 angry"))  # lay1 +317
    voice "ch5.7_l_016"
    l "W-wait! Why her?{#ch5_7_v4761}"
    $ show_sprites(("si 2"))
    $ show_sprites(("si 2", "w 1"))  # lay20 +1061
    voice "ch5.7_w_009"
    w "Your strong performance made a good impression. You practiced harder than anyone else.{#ch5_7_v15846}"
    $ show_sprites(("si 2 sad", "w 1"))  # lay2 +506
    voice "ch5.7_si_003"
    si "Is it really all right for someone like me to play the heroine?{#ch5_7_v14285}"
    voice "ch5.7_w_010"
    w "Have confidence in yourself. Otherwise, there would be no point in my choosing you.{#ch5_7_v15847}"
    $ show_sprites(("si 2", "w 1"))  # lay2 +500
    voice "ch5.7_si_004"
    si "Th-thank you very much.{#ch5_7_v14286}"
    $ show_sprites(("w 1"))
    $ show_sprites(("w 1", "h 3"))  # lay8 +775
    voice "ch5.7_h_003"
    h "Well, what is decided cannot be helped. Let us do our best in the roles we were given.{#ch5_7_v366}"
    voice "ch5.7_w_011"
    w "Then I will announce the rest of the casting. The old nobleman who raised him will be...{#ch5_7_v15848}"
    stop music fadeout 1.0
    $ show_sprites(("h 3"))
    $ show_sprites(())
    $ fade_fx("black")
    $ show_sprites(())
    $ show_sprites(())
    $ show_sprites(())
    $ show_sprites(())
    $ fade_fx("sky_night")  # BG +90
    th "……… …… …{#ch5.7_th_008}"
    th "And then the curtain rose. The play proceeded without a hitch, and swept toward its climax.{#ch5.7_th_009}"
    $ show_sprites(())
    $ fade_fx("black")
    $ fade_fx("id(143)", type="cg")
    play music t22 fadein 1.0
    voice "ch5.7_s_024"
    s "We can buy a little time here.{#ch5_7_v8765}"
    voice "ch5.7_si_005"
    si "I will negotiate with the enemy. If I return to the Empire, everything will be settled.{#ch5_7_v14287}"
    voice "ch5.7_s_025"
    s "But then I will lose you.{#ch5_7_v8766}"
    voice "ch5.7_si_006"
    si "But if we do nothing, the prince will lose both his kingdom and his life!{#ch5_7_v14288}"
    voice "ch5.7_s_026"
    s "What is a kingdom to me? What is death compared with that?{#ch5_7_v8767}"
    voice "ch5.7_s_027"
    s "Laugh at me. I fear living on after losing you more than I fear death or a ruined kingdom.{#ch5_7_v8768}"
    voice "ch5.7_si_007"
    si "Prince!{#ch5_7_v14289}"
    voice "ch5.7_s_028"
    s "Ah, my beloved. You cannot know how much I loved you.{#ch5_7_v8769}"
    voice "ch5.7_s_029"
    s "Love blinds everyone and drives them mad. The noblemen who whispered their love to you all met ruin trying to answer your riddles.{#ch5_7_v8770}"
    voice "ch5.7_s_030"
    s "But I can no longer laugh at their foolishness. I wagered this kingdom for you, and destroyed it myself!{#ch5_7_v8771}"
    voice "ch5.7_s_031"
    s "The castle is falling. Leave.{#ch5_7_v8772}"
    voice "ch5.7_s_032"
    s "The attacking soldiers will welcome you as their new queen with cries of joy!{#ch5_7_v8773}"
    voice "ch5.7_s_033"
    s "You will live and become queen.{#ch5_7_v8774}"
    voice "ch5.7_si_008"
    si "Ah, Prince!{#ch5_7_v14290}"
    voice "ch5.7_s_034"
    s "My beloved. But I have no regrets.{#ch5_7_v8775}"
    voice "ch5.7_s_035"
    s "My love for you was worth the price. If only... just once...{#ch5_7_v8776}"
    voice "ch5.7_s_036"
    s "I wanted to know what you truly felt.{#ch5_7_v8777}"
    voice "ch5.7_s_037"
    s "The enemy soldiers have reached the tower... There is no time left.{#ch5_7_v8778}"
    voice "ch5.7_si_009"
    si "P-Prince, do you remember the night you proposed to me?{#ch5_7_v14291}"
    voice "ch5.7_si_010"
    si "I will give you my answer now.{#ch5_7_v14292}"
    voice "ch5.7_s_038"
    s "Princess?{#ch5_7_v8779}"
    voice "ch5.7_si_011"
    si "Noelle will die here... as the prince's wife.{#ch5_7_v14293}"
    voice "ch5.7_g_003"
    g "There she is! The princess!{#ch5_7_v1413}"
    voice "ch5.7_si_012"
    si "…….{#ch5_7_v14294}"
    voice "ch5.7_s_039"
    s "Then let us go, Noelle. I will follow you wherever you go.{#ch5_7_v8780}"
    $ flash_fx("white")
    $ show_sprites(())
    $ show_sprites(())
    $ show_sprites(())
    $ fade_fx("id(53)")  # BG +53
    $ fade_fx("black")
    $ flash_fx("white")
    voice "ch5.7_t_004"
    t "And so the two of them threw themselves from the tower.{#ch5_7_v15339}"
    voice "ch5.7_t_005"
    t "They say white flowers eventually bloomed where the two of them fell, side by side.{#ch5_7_v15340}"
    stop music fadeout 1.0
    $ show_sprites(())
    $ show_sprites(())
    $ show_sprites(())
    $ show_sprites(())
    $ fade_fx("black")
    th "……… …… …{#ch5.7_th_010}"
    $ fade_fx("id(54)")  # BG +54
    play music t18 fadein 1.0
    $ show_sprites(("si 1"))  # lay2 +511
    voice "ch5.7_s_040"
    s "You looked like a real princess. It was as if you were a different Siesta.{#ch5_7_v8781}"
    $ show_sprites(("si 1"))  # lay2 +513
    voice "ch5.7_si_013"
    si "R-really? Hearing that from you makes me happy.{#ch5_7_v14295}"
    voice "ch5.7_w_012"
    w "Ladies and gentlemen, please give them one more grand round of applause!{#ch5_7_v15849}"
    $ show_sprites(("si 1"))  # lay2 +519
    voice "ch5.7_si_014"
    si "Saito-san, tell me... Was that proposal real?{#ch5_7_v14296}"
    th "What am I supposed to say to that...{#ch5.7_th_011}"
    menu:
        "Maybe I was serious?{#ch5_7_c1140}":
            $ show_sprites(("si 1"))  # lay2 +519
            play music t18 fadein 1.0
            $ fade_fx("id(54)")  # BG +54
            voice "ch5.7_s_041"
            s "Maybe I was serious?{#ch5_7_v8782}"
            $ show_sprites(())
            $ show_sprites(("si 1"))  # lay2 +520
            voice "ch5.7_si_015"
            si "Really? If that is what you want, Saito-san, then anytime...{#ch5_7_v14297}"
            voice "ch5.7_s_042"
            s "S-stop! Stop!{#ch5_7_v8783}"
            jump ch5_7_r4_rejoin
        "It was only acting!{#ch5_7_c1141}":
            $ show_sprites(("si 1"))  # lay2 +519
            play music t18 fadein 1.0
            $ fade_fx("id(54)")  # BG +54
            voice "ch5.7_s_043"
            s "It was only acting!{#ch5_7_v8784}"
            $ show_sprites(("si 1"))  # lay2 +517
            voice "ch5.7_si_016"
            si "I-I thought so. Someone like me...{#ch5_7_v14298}"
            voice "ch5.7_si_017"
            si "Ahaha, taking the play seriously... I really am just a country girl, aren't I?{#ch5_7_v14299}"
            voice "ch5.7_s_044"
            s "N-no, that is not what I meant!{#ch5_7_v8785}"
            jump ch5_7_r4_rejoin
        "Laugh it off{#ch5_7_c1142}":
            $ show_sprites(("si 1"))  # lay2 +519
            play music t18 fadein 1.0
            $ fade_fx("id(54)")  # BG +54
            voice "ch5.7_s_045"
            s "A-ahaha...{#ch5_7_v8786}"
            $ show_sprites(("si 1"))  # lay2 +516
            voice "ch5.7_si_018"
            si "Please do not laugh it off. I am serious, you know?{#ch5_7_v14300}"
            voice "ch5.7_s_046"
            s "Please, spare me.{#ch5_7_v8787}"
            jump ch5_7_r4_rejoin
label ch5_7_r4_rejoin:
    $ show_sprites(("si 1"))  # lay2 +520
    play music t18 fadein 1.0
    $ fade_fx("id(54)")  # BG +54
    stop music fadeout 1.0
    $ show_sprites(("si 1"))
    $ show_sprites(())
    $ show_sprites(())
    $ fade_fx("black")
    stop music fadeout 1.0
    $ fade_fx("black")
    jump ch5_10
