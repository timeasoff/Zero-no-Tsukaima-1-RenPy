# Chapter 5, part 8: route 2 (Kirche), scenes 1144-1148, and route 3 (Tabitha), 1149-1153.
# Source: ps2_source/chapters/chapter_06_本当の想い.txt and events_full.

label ch5_8_r2_kirche:
    # ==== SCENE 1144 ====
    $ fade_fx("id(54)")
    play music t4 fadein 1.0
    $ show_sprites(("w 1"))
    voice "ch5.8_w_001"
    w "Mademoiselle Kirche!{#ch5_8_v15850}"
    $ show_sprites(("k 2"))
    voice "ch5.8_k_001"
    k "Well, naturally!{#ch5_8_v2818}"
    $ show_sprites(("l 6"))
    voice "ch5.8_l_001"
    l "W-wait! Why does it have to be her? Of all people, Kirche?!{#ch5_8_v4762}"
    $ show_sprites(("w 1"))
    voice "ch5.8_w_002"
    w "Her performance was especially good when she deftly turned down the young nobles' proposals. I knew she had the talent for it.{#ch5_8_v15851}"
    $ show_sprites(("k 3"))
    voice "ch5.8_k_002"
    k "Heehee… Well, it was talent!{#ch5_8_v2819}"
    voice "ch5.8_l_003"
    l "I can't accept this!{#ch5_8_v4763}"
    $ show_sprites(("h 3"))
    voice "ch5.8_h_001"
    h "What is decided cannot be helped. Let us do our best in the roles we were given.{#ch5_8_v367}"
    $ show_sprites(("w 1"))
    voice "ch5.8_w_003"
    w "Then I will announce the rest of the casting. The old nobleman who raised him will be…{#ch5_8_v15852}"
    jump ch5_8_kirche_play

label ch5_8_kirche_play:
    # ==== SCENE 1144 continuation ====
    $ fade_fx("id(90)")
    th "……… …… …{#ch5.8_th_001}"
    th "And then the curtain rose. The play proceeded without a hitch, and swept toward its climax.{#ch5.8_th_002}"
    $ fade_fx("id(145)", type="cg")
    play music t22 fadein 1.0
    voice "ch5.8_s_001"
    s "We can buy a little time here.{#ch5_8_v8788}"
    voice "ch5.8_k_003"
    k "I will persuade the enemy forces. If I return to the Empire, everything should be settled.{#ch5_8_v2820}"
    voice "ch5.8_s_002"
    s "But then I will lose you.{#ch5_8_v8789}"
    voice "ch5.8_k_004"
    k "But if we do nothing, the prince will lose both his kingdom and his life!{#ch5_8_v2821}"
    voice "ch5.8_s_003"
    s "What is a kingdom to me? What is death compared with that?{#ch5_8_v8790}"
    voice "ch5.8_s_004"
    s "Laugh at me. I fear living on after losing you more than I fear death or a ruined kingdom.{#ch5_8_v8791}"
    voice "ch5.8_k_005"
    k "Prince!{#ch5_8_v2822}"
    voice "ch5.8_s_005"
    s "Ah, my beloved. You cannot know how much I loved you.{#ch5_8_v8792}"
    voice "ch5.8_s_006"
    s "Love blinds everyone and drives them mad. The noblemen who whispered their love to you all met ruin trying to answer your riddles.{#ch5_8_v8793}"
    voice "ch5.8_s_007"
    s "But I can no longer laugh at their foolishness. I wagered this kingdom for you, and destroyed it myself!{#ch5_8_v8794}"
    voice "ch5.8_s_008"
    s "The castle is falling. Leave.{#ch5_8_v8795}"
    voice "ch5.8_s_009"
    s "The attacking soldiers will welcome you as their new queen with cries of joy!{#ch5_8_v8796}"
    voice "ch5.8_s_010"
    s "You will live and become queen.{#ch5_8_v8797}"
    voice "ch5.8_k_006"
    k "Ah, Prince!{#ch5_8_v2823}"
    voice "ch5.8_s_011"
    s "My beloved. But I have no regrets.{#ch5_8_v8798}"
    voice "ch5.8_s_012"
    s "My love for you was worth the price. If only… just once…{#ch5_8_v8799}"
    voice "ch5.8_s_013"
    s "I wanted to know what you truly felt.{#ch5_8_v8800}"
    voice "ch5.8_s_014"
    s "The enemy soldiers have reached the tower… There is no time left.{#ch5_8_v8801}"
    voice "ch5.8_k_007"
    k "Prince, do you remember the night you proposed to me?{#ch5_8_v2824}"
    voice "ch5.8_k_008"
    k "It was a beautiful night, like tonight. I will give you my answer now.{#ch5_8_v2825}"
    voice "ch5.8_s_015"
    s "Princess?{#ch5_8_v8802}"
    voice "ch5.8_k_009"
    k "Noelle will die here… as the prince's wife.{#ch5_8_v2826}"
    voice "ch5.8_g_001"
    g "There she is! The princess!{#ch5_8_v1414}"
    voice "ch5.8_k_010"
    k "…….{#ch5_8_v2827}"
    voice "ch5.8_s_016"
    s "Then let us go, Noelle. I will follow you wherever you go.{#ch5_8_v8803}"
    $ flash_fx("white")
    $ fade_fx("id(53)")
    voice "ch5.8_t_001"
    t "And so the two of them threw themselves from the tower…{#ch5_8_v15341}"
    voice "ch5.8_t_002"
    t "They say white flowers eventually bloomed where the two of them fell, side by side…{#ch5_8_v15342}"
    $ fade_fx("id(54)")
    play music t18 fadein 1.0
    $ show_sprites(("k 4"))
    voice "ch5.8_k_011"
    k "That was quite a passionate performance, wasn't it?{#ch5_8_v2828}"
    voice "ch5.8_s_017"
    s "W-was it? I was just carried away.{#ch5_8_v8804}"
    voice "ch5.8_w_004"
    w "Ladies and gentlemen, please give them one more grand round of applause!{#ch5_8_v15853}"
    voice "ch5.8_k_012"
    k "Hey, darling. I almost thought that confession was real.{#ch5_8_v2829}"
    th "What am I supposed to say to that…{#ch5.8_th_003}"
    menu:
        "Maybe I really meant it…{#ch5_8_c1145}":
            voice "ch5.8_s_018"
            s "Maybe I was actually serious…{#ch5_8_v8805}"
            voice "ch5.8_k_013"
            k "Oh? Really!{#ch5_8_v2830}"
            voice "ch5.8_s_019"
            s "N-no! Just kidding. I didn't mean anything!{#ch5_8_v8806}"
        "It was only a play!{#ch5_8_c1146}":
            voice "ch5.8_s_020"
            s "I-it was only a play!{#ch5_8_v8807}"
            voice "ch5.8_k_014"
            k "I see. Of course it was～～.{#ch5_8_v2831}"
            voice "ch5.8_k_015"
            k "Though perhaps truth can come from a lie.{#ch5_8_v2832}"
        "Laugh it off{#ch5_8_c1147}":
            voice "ch5.8_s_021"
            s "A-ahaha…{#ch5_8_v8808}"
            voice "ch5.8_k_016"
            k "…Oh, you're laughing it off? What a shame.{#ch5_8_v2833}"
            voice "ch5.8_s_022"
            s "P-please, give me a break.{#ch5_8_v8809}"
    jump ch5_8_r2_end

label ch5_8_r2_end:
    # ==== SCENE 1148 ====
    jump ch5_9

label ch5_8_r3_tabitha:
    # ==== SCENE 1149 ====
    $ fade_fx("id(54)")
    play music t4 fadein 1.0
    $ show_sprites(("w 1"))
    voice "ch5.8_w_005"
    w "Mademoiselle Tabitha!{#ch5_8_v15854}"
    $ show_sprites(("l 6"))
    voice "ch5.8_l_002"
    l "Eeeeeh?!{#ch5_8_v4764}"
    $ show_sprites(("t 5"))
    t "…….{#ch5.8_th_004}"
    $ show_sprites(("w 1"))
    voice "ch5.8_w_006"
    w "Her dignity, or perhaps her mysterious air, is perfect. It may be a bit of a gamble, though.{#ch5_8_v15855}"
    $ show_sprites(("k 2"))
    voice "ch5.8_k_017"
    k "…Are you really sure this is all right?{#ch5_8_v2834}"
    voice "ch5.8_t_003"
    t "It is all right.{#ch5_8_v15343}"
    th "Really?!{#ch5.8_th_005}"
    $ show_sprites(("h 3"))
    voice "ch5.8_h_002"
    h "What is decided cannot be helped. Let us do our best in the roles we were given.{#ch5_8_v368}"
    $ show_sprites(("w 1"))
    voice "ch5.8_w_007"
    w "Then I will announce the rest of the casting. The old nobleman who raised him will be…{#ch5_8_v15856}"
    jump ch5_8_tabitha_play

label ch5_8_tabitha_play:
    # ==== SCENE 1149 continuation ====
    $ fade_fx("id(90)")
    th "……… …… …{#ch5.8_th_006}"
    th "And then the curtain rose. The play proceeded without a hitch, and swept toward its climax.{#ch5.8_th_007}"
    $ fade_fx("id(144)", type="cg")
    play music t22 fadein 1.0
    voice "ch5.8_s_023"
    s "We can buy a little time here.{#ch5_8_v8810}"
    voice "ch5.8_t_004"
    t "I will persuade the enemy forces. If I return to the Empire, everything should be settled.{#ch5_8_v15344}"
    voice "ch5.8_s_024"
    s "But then I will lose you.{#ch5_8_v8811}"
    voice "ch5.8_t_005"
    t "But if we do nothing, the prince will lose both his kingdom and his life.{#ch5_8_v15345}"
    voice "ch5.8_s_025"
    s "What is a kingdom to me? What is death compared with that?{#ch5_8_v8812}"
    voice "ch5.8_s_026"
    s "Laugh at me. I fear living on after losing you more than I fear death or a ruined kingdom.{#ch5_8_v8813}"
    voice "ch5.8_t_006"
    t "Prince.{#ch5_8_v15346}"
    voice "ch5.8_s_027"
    s "Ah, my beloved. You cannot know how much I loved you.{#ch5_8_v8814}"
    voice "ch5.8_s_028"
    s "Love blinds everyone and drives them mad. The noblemen who whispered their love to you all met ruin trying to answer your riddles.{#ch5_8_v8815}"
    voice "ch5.8_s_029"
    s "But I can no longer laugh at their foolishness. I wagered this kingdom for you, and destroyed it myself!{#ch5_8_v8816}"
    voice "ch5.8_s_030"
    s "The castle is falling. Leave.{#ch5_8_v8817}"
    voice "ch5.8_s_031"
    s "The attacking soldiers will welcome you as their new queen with cries of joy!{#ch5_8_v8818}"
    voice "ch5.8_s_032"
    s "You will live and become queen.{#ch5_8_v8819}"
    t "…….{#ch5_8_th_008}"
    voice "ch5.8_s_033"
    s "My beloved. But I have no regrets.{#ch5_8_v8820}"
    voice "ch5.8_s_034"
    s "My love for you was worth the price. If only… just once…{#ch5_8_v8821}"
    voice "ch5.8_s_035"
    s "I wanted to know what you truly felt.{#ch5_8_v8822}"
    voice "ch5.8_s_036"
    s "The enemy soldiers have reached the tower… There is no time left.{#ch5_8_v8823}"
    voice "ch5.8_t_008"
    t "Prince, do you remember the night you proposed to me?{#ch5_8_v15347}"
    voice "ch5.8_t_009"
    t "It was a beautiful night, like tonight. I will give you my answer now.{#ch5_8_v15348}"
    voice "ch5.8_s_037"
    s "Princess?{#ch5_8_v8824}"
    voice "ch5.8_t_010"
    t "Noelle will die here… as the prince's wife. I wish to die here.{#ch5_8_v15349}"
    voice "ch5.8_g_002"
    g "There she is! The princess!{#ch5_8_v1415}"
    voice "ch5.8_t_011"
    t "Come.{#ch5_8_v15350}"
    voice "ch5.8_s_038"
    s "Then let us go, Noelle. I will follow you wherever you go.{#ch5_8_v8825}"
    $ flash_fx("white")
    $ fade_fx("id(53)")
    voice "ch5.8_t_012"
    t "And so the two of them threw themselves from the tower.{#ch5_8_v15351}"
    voice "ch5.8_t_013"
    t "They say white flowers eventually bloomed where the two of them fell, side by side…{#ch5_8_v15352}"
    $ fade_fx("id(54)")
    play music t18 fadein 1.0
    $ show_sprites(("t 6"))
    voice "ch5.8_s_039"
    s "She really looked like a princess. She seemed like a different person from the usual Tabitha.{#ch5_8_v8826}"
    t "…….{#ch5_8_th_009}"
    voice "ch5.8_w_008"
    w "Ladies and gentlemen, please give them one more grand round of applause!{#ch5_8_v15857}"
    voice "ch5.8_t_015"
    t "So confessions really happen.{#ch5_8_v15353}"
    voice "ch5.8_s_040"
    s "W-what?{#ch5_8_v8827}"
    voice "ch5.8_t_016"
    t "I've never seen one before.{#ch5_8_v15354}"
    th "What am I supposed to say to that…{#ch5.8_th_010}"
    menu:
        "Maybe I really meant it{#ch5_8_c1150}":
            voice "ch5.8_s_041"
            s "Maybe I really meant it?{#ch5_8_v8828}"
            voice "ch5.8_t_017"
            t "Yes.{#ch5_8_v15355}"
            voice "ch5.8_s_042"
            s "When you just go along with it like that, it makes me sad.{#ch5_8_v8829}"
            voice "ch5.8_t_018"
            t "…Were you joking?{#ch5_8_v15356}"
            voice "ch5.8_s_043"
            s "Huh? Huh?!{#ch5_8_v8830}"
        "It was only a play!{#ch5_8_c1151}":
            voice "ch5.8_s_044"
            s "I-it was only a play!{#ch5_8_v8831}"
            voice "ch5.8_t_019"
            t "Yes. A play?{#ch5_8_v15357}"
            voice "ch5.8_s_045"
            s "Ugh. Th-that… No, I mean…{#ch5_8_v8832}"
        "Laugh it off{#ch5_8_c1152}":
            s "…….{#ch5_8_th_011}"
            voice "ch5.8_s_047"
            s "A-ahaha…{#ch5_8_v8833}"
            voice "ch5.8_t_020"
            t "I dislike evasiveness.{#ch5_8_v15358}"
            voice "ch5.8_s_048"
            s "No, I mean, well…{#ch5_8_v8834}"
            voice "ch5.8_t_021"
            t "A lie.{#ch5_8_v15359}"
    jump ch5_8_r3_end

label ch5_8_r3_end:
    # ==== SCENE 1153 ====
    jump ch5_9
