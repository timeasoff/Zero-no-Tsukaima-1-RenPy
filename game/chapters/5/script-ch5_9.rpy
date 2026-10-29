# Chapter 5, part 9: Haruna scenes 1154-1158 and Henrietta scenes 1159-1163.
# Source: chapter_06_本当の想い.txt and events_full; scene 342 continues in S10.

label ch5_9:
    if zero_route == 5:
        jump ch5_9_r5_henrietta
    else:
        jump ch5_9_r6_haruna

label ch5_9_r6_haruna:
    # ==== SCENE 1154 ====
    $ fade_fx("id(54)")
    play music t4 fadein 1.0
    $ show_sprites(("w 1"))
    voice "ch5.9_w_001"
    w "Haruna!{#ch5_9_v15858}"
    voice "ch5.9_ha_001"
    ha "Huh?! Whaaaat?! M-me?!{#ch5_9_v1683}"
    voice "ch5.9_l_001"
    l "W-wait! How did you come to that?!{#ch5_9_v4765}"
    voice "ch5.9_w_002"
    w "Oh, I do not play favorites. I simply chose the best person for the role.{#ch5_9_v15859}"
    voice "ch5.9_ha_002"
    ha "I am the heroine… I am the heroine…{#ch5_9_v1684}"
    voice "ch5.9_k_001"
    k "…Are you really sure this is all right?{#ch5_9_v2834}"
    voice "ch5.9_t_001"
    t "I am a little worried.{#ch5_9_v15360}"
    voice "ch5.9_w_003"
    w "Then I will announce the rest of the casting. The old nobleman who raised him will be…{#ch5_9_v15860}"
    th "……… …… …{#ch5_9_s1154_8}"
    th "And then the curtain rose. The play proceeded without a hitch, and swept toward its climax.{#ch5_9_s1154_9}"
    voice "ch5.9_s_001"
    s "We can buy a little time here.{#ch5_9_v8835}"
    voice "ch5.9_ha_003"
    ha "I will persuade the enemy forces. If I return to the Empire, everything should be settled.{#ch5_9_v1685}"
    voice "ch5.9_s_002"
    s "But then I will lose you.{#ch5_9_v8836}"
    voice "ch5.9_ha_004"
    ha "But if we do nothing, the prince will lose both his kingdom and his life!{#ch5_9_v1686}"
    voice "ch5.9_s_003"
    s "What is a kingdom to me? What is death compared with that?{#ch5_9_v8837}"
    voice "ch5.9_s_004"
    s "Laugh at me. I fear living on after losing you more than I fear death or a ruined kingdom.{#ch5_9_v8838}"
    voice "ch5.9_ha_005"
    ha "Prince!{#ch5_9_v1687}"
    voice "ch5.9_s_005"
    s "Ah, my beloved. You cannot know how much I loved you.{#ch5_9_v8839}"
    voice "ch5.9_s_006"
    s "Love blinds everyone and drives them mad. The noblemen who whispered their love to you all met ruin trying to answer your riddles.{#ch5_9_v8840}"
    voice "ch5.9_s_007"
    s "But I can no longer laugh at their foolishness. I wagered this kingdom for you, and destroyed it myself!{#ch5_9_v8841}"
    voice "ch5.9_s_008"
    s "The castle is falling. Leave.{#ch5_9_v8842}"
    voice "ch5.9_s_009"
    s "The attacking soldiers will welcome you as their new queen with cries of joy!{#ch5_9_v8843}"
    voice "ch5.9_s_010"
    s "You will live and become queen.{#ch5_9_v8844}"
    voice "ch5.9_ha_006"
    ha "Ah, Prince!{#ch5_9_v1688}"
    voice "ch5.9_s_011"
    s "My beloved. But I have no regrets.{#ch5_9_v8845}"
    voice "ch5.9_s_012"
    s "My love for you was worth the price. If only… just once…{#ch5_9_v8846}"
    voice "ch5.9_s_013"
    s "I wanted to know what you truly felt.{#ch5_9_v8847}"
    voice "ch5.9_s_014"
    s "Ah, the enemy soldiers have reached the tower… There is no time left.{#ch5_9_v8848}"
    voice "ch5.9_ha_007"
    ha "Prince, do you remember the night you proposed to me?{#ch5_9_v1689}"
    voice "ch5.9_ha_008"
    ha "It was a beautiful night, like tonight. I will give you my answer now.{#ch5_9_v1690}"
    voice "ch5.9_s_015"
    s "Princess?{#ch5_9_v8849}"
    voice "ch5.9_ha_009"
    ha "Noelle will die here… as the prince’s wife.{#ch5_9_v1691}"
    voice "ch5.9_g_001"
    g "There she is! The princess!{#ch5_9_v1416}"
    voice "ch5.9_ha_010"
    ha "…{#ch5_9_v1692}"
    voice "ch5.9_s_016"
    s "Then let us go, Noelle. I will follow you wherever you go.{#ch5_9_v8850}"
    voice "ch5.9_t_002"
    t "And so the two of them threw themselves from the tower.{#ch5_9_v15361}"
    voice "ch5.9_t_003"
    t "They say white flowers eventually bloomed where the two of them fell, side by side…{#ch5_9_v15362}"
    th "……… …… …{#ch5_9_s1154_37}"
    voice "ch5.9_ha_011"
    ha "Th-that was incredible, Hiraga! Your performance was so passionate.{#ch5_9_v1693}"
    voice "ch5.9_s_017"
    s "W-well, maybe a little.{#ch5_9_v8851}"
    voice "ch5.9_w_004"
    w "Ladies and gentlemen, please give them one more grand round of applause!{#ch5_9_v15861}"
    voice "ch5.9_ha_012"
    ha "Hey, Hiraga. I almost thought that confession was real.{#ch5_9_v1694}"
    th "What am I supposed to say to that…{#ch5_9_s1154_42}"
    menu:
        "I really meant it.{#ch5_9_c1155}":
            jump ch5_9_r6_haruna_1155
        "It was only a play!{#ch5_9_c1156}":
            jump ch5_9_r6_haruna_1156
        "Laugh it off{#ch5_9_c1157}":
            jump ch5_9_r6_haruna_1157
label ch5_9_r6_haruna_1155:
    # ==== SCENE 1155 ====
    $ fade_fx("id(54)")
    play music t18 fadein 1.0
    voice "ch5.9_s_018"
    s "I really meant it…{#ch5_9_v8852}"
    voice "ch5.9_ha_013"
    ha "Huh?{#ch5_9_v1695}"
    voice "ch5.9_s_019"
    s "N-no, it is nothing!{#ch5_9_v8853}"
    jump ch5_9_r6_haruna_1158
label ch5_9_r6_haruna_1156:
    # ==== SCENE 1156 ====
    $ fade_fx("id(54)")
    play music t18 fadein 1.0
    voice "ch5.9_s_020"
    s "I-it was only a play! Of course!{#ch5_9_v8854}"
    voice "ch5.9_ha_014"
    ha "Y-yes, of course.{#ch5_9_v1696}"
    jump ch5_9_r6_haruna_1158
label ch5_9_r6_haruna_1157:
    # ==== SCENE 1157 ====
    $ fade_fx("id(54)")
    play music t18 fadein 1.0
    voice "ch5.9_s_021"
    s "A-ahaha…{#ch5_9_v8855}"
    voice "ch5.9_ha_015"
    ha "Hm. So you are laughing it off.{#ch5_9_v1697}"
    voice "ch5.9_s_022"
    s "Sorry. I got a little carried away.{#ch5_9_v8856}"
    voice "ch5.9_ha_016"
    ha "I-I am not angry or anything.{#ch5_9_v1698}"
    jump ch5_9_r6_haruna_1158
label ch5_9_r6_haruna_1158:
    # ==== SCENE 1158 ====
    stop music fadeout 1.0
    $ show_sprites(())
    jump ch5_10
label ch5_9_r5_henrietta:
    # ==== SCENE 1159 ====
    $ fade_fx("id(54)")
    play music t4 fadein 1.0
    $ show_sprites(("w 1"))
    voice "ch5.9_w_005"
    w "I will ask Miss Henrietta to take the role.{#ch5_9_v15862}"
    voice "ch5.9_h_001"
    h "…What? Me?{#ch5_9_v369}"
    voice "ch5.9_l_002"
    l "What, whaaaat?!{#ch5_9_v4766}"
    th "A reigning queen playing a princess? No matter how you look at it, that cannot be right.{#ch5_9_s1159_55}"
    voice "ch5.9_w_006"
    w "…Was that really so surprising? Given her ability, she was the obvious choice.{#ch5_9_v15863}"
    voice "ch5.9_k_002"
    k "Oh, no. Louise was simply silly enough to think she would get the part.{#ch5_9_v2836}"
    voice "ch5.9_l_003"
    l "Y-yes. I jumped to conclusions…{#ch5_9_v4767}"
    voice "ch5.9_l_004"
    l "Just you wait.{#ch5_9_v4768}"
    voice "ch5.9_k_003"
    k "That is my line.{#ch5_9_v2837}"
    voice "ch5.9_t_004"
    t "No fighting.{#ch5_9_v15363}"
    voice "ch5.9_h_002"
    h "What is decided cannot be helped. Let us do our best in the roles we were given.{#ch5_9_v370}"
    voice "ch5.9_w_007"
    w "Then I will announce the rest of the casting. The old nobleman who raised him will be…{#ch5_9_v15864}"
    th "……… …… …{#ch5_9_s1159_64}"
    th "And then the curtain rose. The play proceeded without a hitch, and swept toward its climax.{#ch5_9_s1159_65}"
    voice "ch5.9_s_023"
    s "We can buy a little time here.{#ch5_9_v8857}"
    voice "ch5.9_h_003"
    h "…I will persuade the enemy forces. If I return to the Empire, everything should be settled.{#ch5_9_v371}"
    voice "ch5.9_s_024"
    s "But then I will lose you.{#ch5_9_v8858}"
    voice "ch5.9_h_004"
    h "…But if we do nothing, the prince will lose both his kingdom and his life!{#ch5_9_v372}"
    voice "ch5.9_s_025"
    s "What is a kingdom to me? What is death compared with that?{#ch5_9_v8859}"
    voice "ch5.9_s_026"
    s "…Laugh at me. I fear living on after losing you more than I fear death or a ruined kingdom.{#ch5_9_v8860}"
    voice "ch5.9_h_005"
    h "…Prince!{#ch5_9_v373}"
    th "…Perhaps this play is too cruel for a princess.{#ch5_9_s1159_73}"
    voice "ch5.9_s_027"
    s "…Ah, my beloved. You cannot know how much I loved you.{#ch5_9_v8861}"
    voice "ch5.9_s_028"
    s "…Love blinds everyone and drives them mad. The noblemen who whispered their love to you all met ruin trying to answer your riddles.{#ch5_9_v8862}"
    voice "ch5.9_s_029"
    s "But I can no longer laugh at their foolishness. …I wagered this kingdom for you, and destroyed it myself!{#ch5_9_v8863}"
    voice "ch5.9_s_030"
    s "…The castle is falling. Leave.{#ch5_9_v8864}"
    voice "ch5.9_s_031"
    s "The attacking soldiers will welcome you as their new queen with cries of joy!{#ch5_9_v8865}"
    voice "ch5.9_s_032"
    s "You will live and become queen.{#ch5_9_v8866}"
    voice "ch5.9_h_006"
    h "…Prince!{#ch5_9_v374}"
    voice "ch5.9_s_033"
    s "…My beloved. But I have no regrets.{#ch5_9_v8867}"
    voice "ch5.9_s_034"
    s "My love for you was worth the price. If only… just once…{#ch5_9_v8868}"
    voice "ch5.9_s_035"
    s "I wanted to know what you truly felt.{#ch5_9_v8869}"
    voice "ch5.9_s_036"
    s "Ah, the enemy soldiers have reached the tower… There is no time left.{#ch5_9_v8870}"
    voice "ch5.9_h_007"
    h "…Prince, do you remember the night you proposed to me?{#ch5_9_v375}"
    voice "ch5.9_h_008"
    h "It was a beautiful night, like tonight. …I will give you my answer now.{#ch5_9_v376}"
    voice "ch5.9_s_037"
    s "…Princess?{#ch5_9_v8871}"
    voice "ch5.9_h_009"
    h "Noelle will die here… as the prince’s wife.{#ch5_9_v377}"
    voice "ch5.9_g_002"
    g "…There she is! The princess!{#ch5_9_v1417}"
    voice "ch5.9_h_010"
    h "…{#ch5_9_v378}"
    voice "ch5.9_s_038"
    s "Then let us go, Noelle. I will follow you wherever you go.{#ch5_9_v8872}"
    voice "ch5.9_t_005"
    t "And so the two of them threw themselves from the tower.{#ch5_9_v15364}"
    voice "ch5.9_t_006"
    t "They say white flowers eventually bloomed where the two of them fell, side by side…{#ch5_9_v15365}"
    th "……… …… …{#ch5_9_s1159_94}"
    voice "ch5.9_h_011"
    h "…{#ch5_9_v379}"
    voice "ch5.9_s_039"
    s "…Princess.{#ch5_9_v8873}"
    voice "ch5.9_h_012"
    h "I feel rather strange. Even though it was only a play…{#ch5_9_v380}"
    voice "ch5.9_s_040"
    s "…{#ch5_9_v8874}"
    voice "ch5.9_w_008"
    w "Ladies and gentlemen, please give them one more grand round of applause!{#ch5_9_v15865}"
    voice "ch5.9_h_013"
    h "Hey, familiar. You were thinking about something else, were you not?{#ch5_9_v381}"
    voice "ch5.9_s_041"
    s "Huh?{#ch5_9_v8875}"
    voice "ch5.9_h_014"
    h "That was quite a passionate confession.{#ch5_9_v382}"
    th "What am I supposed to say to that…{#ch5_9_s1159_103}"
    menu:
        "I really meant it.{#ch5_9_c1160}":
            jump ch5_9_r5_henrietta_1160
        "I am sorry.{#ch5_9_c1161}":
            jump ch5_9_r5_henrietta_1161
        "Laugh it off{#ch5_9_c1162}":
            jump ch5_9_r5_henrietta_1162
label ch5_9_r5_henrietta_1160:
    # ==== SCENE 1160 ====
    $ fade_fx("id(54)")
    play music t18 fadein 1.0
    voice "ch5.9_s_042"
    s "…Because I really meant it.{#ch5_9_v8876}"
    voice "ch5.9_h_015"
    h "Huh?{#ch5_9_v383}"
    voice "ch5.9_s_043"
    s "N-no, it is nothing! Forget it.{#ch5_9_v8877}"
    jump ch5_9_r5_henrietta_1163
label ch5_9_r5_henrietta_1161:
    # ==== SCENE 1161 ====
    $ fade_fx("id(54)")
    play music t18 fadein 1.0
    voice "ch5.9_s_044"
    s "I am sorry… I got carried away by myself.{#ch5_9_v8878}"
    voice "ch5.9_h_016"
    h "…No, you were not alone, you know?{#ch5_9_v384}"
    voice "ch5.9_s_045"
    s "Huh? What do you mean…?{#ch5_9_v8879}"
    jump ch5_9_r5_henrietta_1163
label ch5_9_r5_henrietta_1162:
    # ==== SCENE 1162 ====
    $ fade_fx("id(54)")
    play music t18 fadein 1.0
    voice "ch5.9_s_046"
    s "A-ahaha…{#ch5_9_v8880}"
    voice "ch5.9_h_017"
    h "Heehee.{#ch5_9_v385}"
    voice "ch5.9_h_018"
    h "Louise is looking at you with a terrifying expression, familiar.{#ch5_9_v386}"
    voice "ch5.9_s_047"
    s "…Huh? Eek, nooo!{#ch5_9_v8881}"
    jump ch5_9_r5_henrietta_1163
label ch5_9_r5_henrietta_1163:
    # ==== SCENE 1163 ====
    stop music fadeout 1.0
    $ show_sprites(())
    jump ch5_10
