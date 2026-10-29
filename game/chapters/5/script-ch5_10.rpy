# Chapter 5, part 10: epilogue scene 342, date menu 1870-1875,
# and the Louise, Siesta and Kirche date entries requested for this part.
# Scene 343 is not ported here. Local dates therefore forward to the
# future ch5_11 scene-343 dispatcher; 1872/1874/1875 remain external S11 routes.

label ch5_10:
    $ fade_fx("id(57)", new_music="t28")
    $ show_sprites(("w 1"))
    voice "ch5.10_w_001"
    w "It is a relief that it worked out.{#ch5_10_v15995}"
    $ show_sprites(("w 1", "s 1"))
    voice "ch5.10_s_001"
    s "That was completely reckless! Almost all the main actors were amateurs!{#ch5_10_v11702}"
    voice "ch5.10_w_002"
    w "Oh, do not say that. The audience would get bored if every performance were the same.{#ch5_10_v15996}"
    $ show_sprites(("h 1"))
    voice "ch5.10_h_001"
    h "So it is over… Looking back, those were happy days.{#ch5_10_v579}"
    voice "ch5.10_w_003"
    w "Here is the bag I promised you.{#ch5_10_v15997}"
    $ show_sprites(("ha 1"))
    voice "ch5.10_ha_001"
    ha "Oh, thank you very much!{#ch5_10_v2378}"
    voice "ch5.10_ha_002"
    ha "Hiraga, look! My purse was in this hidden pocket!{#ch5_10_v2379}"
    $ show_sprites(("w 1", "ha 1"))
    voice "ch5.10_w_004"
    w "I see. It certainly is Haruna's. I am sorry for all the things I said.{#ch5_10_v15998}"
    $ show_sprites(("ha 2"))
    voice "ch5.10_ha_003"
    ha "No, it is all right… It came back to me like this, after all.{#ch5_10_v2380}"
    $ show_sprites(("s 1"))
    voice "ch5.10_s_002"
    s "That is great, Haruna!{#ch5_10_v11703}"
    $ show_sprites(("l 1", "ha 1"))
    voice "ch5.10_l_001"
    l "Well, I suppose that is good.{#ch5_10_v6258}"
    voice "ch5.10_ha_004"
    ha "Y-yes! Thank you, everyone.{#ch5_10_v2381}"
    stop music fadeout 1.0
    $ show_sprites(())
    $ fade_fx("id(90)", new_music="t19")
    voice "ch5.10_s_003"
    s "…Phew. I still feel like I have not come down from the excitement.{#ch5_10_v11704}"
    th "Who should I go see tonight…?{#ch5_10_th_001}"
    stop music fadeout 1.0
    jump ch5_10_date_menu

label ch5_10_date_menu:
    if zero_route == 1:
        jump ch5_10_date_louise
    elif zero_route == 2:
        jump ch5_10_date_kirche
    elif zero_route == 3:
        jump ch5_11_date_tabitha
    elif zero_route == 4:
        jump ch5_10_date_siesta
    elif zero_route == 5:
        jump ch5_11_date_henrietta
    else:
        jump ch5_11_date_haruna

label ch5_10_date_louise:
    $ fade_fx("id(46)", new_music="t21")
    $ show_sprites(("l 1", "s 1"))
    voice "ch5.10_l_002"
    l "Oh, Saito. You came at just the right time…{#ch5_10_v4732}"
    voice "ch5.10_s_004"
    s "L-Louise, what is that dress…?{#ch5_10_v8631}"
    voice "ch5.10_l_003"
    l "Heehee. Since today's performance is the last one, they lent it to me.{#ch5_10_v4733}"
    voice "ch5.10_l_004"
    l "So, let us have dinner. They had the food prepared, too.{#ch5_10_v4734}"
    $ show_sprites(("l 1", "s 2"))
    voice "ch5.10_s_005"
    s "Yeah…{#ch5_10_v8632}"
    $ show_sprites(("l 2", "s 2"))
    voice "ch5.10_l_005"
    l "You are so tactless. Escort me properly, will you?{#ch5_10_v4735}"
    $ show_sprites(("l 2", "s 1"))
    voice "ch5.10_s_006"
    s "S-sorry.{#ch5_10_v8633}"
    $ show_sprites(("l 3", "s 1"))
    voice "ch5.10_l_006"
    l "I thought you might be a little cool in the play, so why are you like this in real life?{#ch5_10_v4736}"
    voice "ch5.10_s_007"
    s "I-I do not know what to say to that…{#ch5_10_v8634}"
    $ show_sprites(())
    $ dissolve_fx("id(204)", type="cg")
    voice "ch5.10_s_008"
    s "What an amazing meal. It must have cost a fortune, did it not?{#ch5_10_v8635}"
    voice "ch5.10_l_007"
    l "Really? But Weatherly paid me for appearing, so it was not that expensive.{#ch5_10_v4737}"
    voice "ch5.10_l_008"
    l "Saito?{#ch5_10_v4738}"
    voice "ch5.10_s_009"
    s "Hm?{#ch5_10_v8636}"
    voice "ch5.10_l_009"
    l "How do I look to you right now, Saito?{#ch5_10_v4739}"
    voice "ch5.10_s_010"
    s "H-how should I know what to say…{#ch5_10_v8637}"
    menu:
        "You look prettier than usual.{#ch5_10_c001}":
            jump ch5_11_date_louise_1105
        "You look the same as always.{#ch5_10_c002}":
            jump ch5_11_date_louise_1106
        "Does the dress fit you?{#ch5_10_c003}":
            jump ch5_11_date_louise_1107

label ch5_10_date_siesta:
    $ fade_fx("id(46)", new_music="t21")
    $ show_sprites(("si 1", "s 1"))
    voice "ch5.10_si_001"
    si "Oh, Saito-san. You came at just the right time…{#ch5_10_v14263}"
    voice "ch5.10_s_011"
    s "Huh? Siesta, is something wrong?{#ch5_10_v8647}"
    voice "ch5.10_si_002"
    si "I received my pay for the play today, so I asked Haruna-san and tried to make food from your country.{#ch5_10_v14264}"
    $ show_sprites(("si 1", "s 2"))
    voice "ch5.10_s_012"
    s "What? Seriously…{#ch5_10_v8648}"
    $ show_sprites(("si 2", "s 2"))
    voice "ch5.10_si_003"
    si "There were many ingredients I could not find or did not understand… Will you try it?{#ch5_10_v14265}"
    voice "ch5.10_s_013"
    s "You bet!{#ch5_10_v8649}"
    $ show_sprites(())
    $ dissolve_fx("id(221)", type="cg")
    voice "ch5.10_s_014"
    s "Whoa, what is this!{#ch5_10_v8650}"
    voice "ch5.10_s_015"
    s "Grilled fish and… lightly pickled vegetables…{#ch5_10_v8651}"
    voice "ch5.10_si_004"
    si "I could not get something called miso, so I used osumashi instead…{#ch5_10_v14266}"
    voice "ch5.10_si_005"
    si "But I made something called udon as well, so please eat it.{#ch5_10_v14267}"
    voice "ch5.10_s_016"
    s "Whoa!{#ch5_10_v8652}"
    voice "ch5.10_si_006"
    si "Haruna-san lamented that, apart from the grilled fish, all she needed was dashi and soy sauce.{#ch5_10_v14268}"
    voice "ch5.10_s_017"
    s "This is plenty! Ah, udon… I have not had this in ages.{#ch5_10_v8653}"
    voice "ch5.10_si_007"
    si "And in your country, everyone eats with these two sticks, right?{#ch5_10_v14269}"
    voice "ch5.10_si_008"
    si "I heard your great-grandfather did that too.{#ch5_10_v14270}"
    voice "ch5.10_s_018"
    s "Wow, even chopsticks! Siesta, you really thought of everything! All right, let us eat!{#ch5_10_v8654}"
    $ show_sprites(())
    $ dissolve_fx("id(221)", type="cg")
    voice "ch5.10_si_009"
    si "But food from your country is strange, is it not?{#ch5_10_v14271}"
    voice "ch5.10_s_019"
    s "Hm? Is it?{#ch5_10_v8655}"
    voice "ch5.10_si_010"
    si "I cannot tell whether it is simple or elaborate… Haruna-san said you care about the original taste of the ingredients.{#ch5_10_v14272}"
    voice "ch5.10_s_020"
    s "…Huh.{#ch5_10_v8656}"
    voice "ch5.10_si_011"
    si "Come to think of it, there was a funny story in the village about your great-grandfather eating raw eggs…{#ch5_10_v14273}"
    voice "ch5.10_si_012"
    si "When I asked Haruna-san, she said that was normal in your country. I was surprised.{#ch5_10_v14274}"
    voice "ch5.10_s_021"
    s "Your great-grandfather must have had a hard time too, Siesta.{#ch5_10_v8657}"
    menu:
        "I want to go home…{#ch5_10_c004}":
            jump ch5_11_date_siesta_1110
        "I want to eat hamburgers…{#ch5_10_c005}":
            jump ch5_11_date_siesta_1111
        "Do you have any other food stories?{#ch5_10_c006}":
            jump ch5_11_date_siesta_1112

label ch5_10_date_kirche:
    $ fade_fx("id(54)", new_music="t21")
    $ show_sprites(("k 1"))
    voice "ch5.10_k_001"
    k "Ah, my beloved. How deeply I loved you.{#ch5_10_v2795}"
    voice "ch5.10_k_002"
    k "Love blinds everyone and drives them mad. The noblemen who whispered love to you all met ruin trying to answer your riddles.{#ch5_10_v2796}"
    voice "ch5.10_k_003"
    k "But I will no longer laugh at their foolishness. I wagered this kingdom for you, and destroyed it myself!{#ch5_10_v2797}"
    $ show_sprites(("k 2"))
    voice "ch5.10_k_004"
    k "Men are such fools.{#ch5_10_v2798}"
    $ show_sprites(("k 1", "s 1"))
    voice "ch5.10_s_022"
    s "Kirche. I wondered where you were…{#ch5_10_v8694}"
    $ show_sprites(("k 1", "s 1"))
    voice "ch5.10_k_005"
    k "…Oh, darling?{#ch5_10_v2799}"
    voice "ch5.10_s_023"
    s "What is wrong?{#ch5_10_v8695}"
    voice "ch5.10_k_006"
    k "Nothing. I just became a little sentimental.{#ch5_10_v2800}"
    voice "ch5.10_k_007"
    k "The days onstage, with all that festival excitement, are finally over.{#ch5_10_v2801}"
    voice "ch5.10_s_024"
    s "Yeah.{#ch5_10_v8696}"
    $ show_sprites(("k 3", "s 1"))
    voice "ch5.10_k_008"
    k "I had never been surrounded by so many people, so I got nervous.{#ch5_10_v2802}"
    $ show_sprites(("k 3", "s 2"))
    voice "ch5.10_s_025"
    s "Really?{#ch5_10_v8697}"
    voice "ch5.10_k_009"
    k "Yes. Besides, the atmosphere onstage is quite unique, is it not?{#ch5_10_v2803}"
    $ show_sprites(("k 3", "s 1"))
    voice "ch5.10_s_026"
    s "Yeah, it certainly is…{#ch5_10_v8698}"
    voice "ch5.10_k_010"
    k "Hey, darling. Shall we perform the climax again?{#ch5_10_v2804}"
    voice "ch5.10_k_011"
    k "On a stage with only the two of us…{#ch5_10_v2805}"
    $ show_sprites(("k 1", "s 2"))
    voice "ch5.10_s_027"
    s "Sure, why not.{#ch5_10_v8699}"
    $ show_sprites(("k 1", "s 3"))
    $ fade_fx("id(54)")
    voice "ch5.10_s_028"
    s "My beloved. But I shall not regret it.{#ch5_10_v8700}"
    voice "ch5.10_s_029"
    s "My love for you was worth that price. If only… just once…{#ch5_10_v8701}"
    $ show_sprites(("k 1", "s 1"))
    voice "ch5.10_s_030"
    s "I wanted to know what you truly felt.{#ch5_10_v8702}"
    $ show_sprites(("k 3", "s 1"))
    voice "ch5.10_k_012"
    k "Hey? Do you really want to know? Do you want to know how I feel?{#ch5_10_v2806}"
    voice "ch5.10_s_031"
    s "W-wait a minute. That is not Kirche's next line, is it?{#ch5_10_v8703}"
    $ show_sprites(("k 2", "s 1"))
    voice "ch5.10_k_013"
    k "Do not dodge the question. Answer yes or no.{#ch5_10_v2807}"
    menu:
        "Resist.{#ch5_10_c007}":
            jump ch5_11_date_kirche_1115
        "Yes.{#ch5_10_c008}":
            jump ch5_11_date_kirche_1116
        "No.{#ch5_10_c009}":
            jump ch5_11_date_kirche_1117
