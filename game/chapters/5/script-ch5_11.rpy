# Chapter 5, part 11: Tabitha, Haruna and Henrietta dates; scene 343 dispatcher.
# Scene 343 routes into chapter content that has not yet been ported. Until then,
# unavailable destinations use the project's attention endpoint.

label ch5_11_date_tabitha:
    $ fade_fx("id(43)", new_music="t21")
    $ show_sprites(("s 1", "t 1"))
    voice "ch5.11_s_001"
    s "Oh, there you are.{#ch5_11_v8667}"
    voice "ch5.11_t_001"
    t "Would you like some tea?{#ch5_11_v15306}"
    voice "ch5.11_s_002"
    s "Y-yes, please.{#ch5_11_v8668}"
    voice "ch5.11_s_003"
    s "About the play… It must have been hard, right?{#ch5_11_v8669}"
    voice "ch5.11_t_002"
    t "It was hard.{#ch5_11_v15307}"
    voice "ch5.11_s_004"
    s "How so?{#ch5_11_v8670}"
    voice "ch5.11_t_003"
    t "Using my body and raising my voice so much… It was my first time.{#ch5_11_v15308}"
    $ show_sprites(("s 2", "t 5"))
    voice "ch5.11_s_005"
    s "…That does sound hard.{#ch5_11_v8671}"
    voice "ch5.11_t_004"
    t "But it was not bad.{#ch5_11_v15309}"
    voice "ch5.11_t_005"
    t "A good experience.{#ch5_11_v15310}"
    $ show_sprites(("s 1", "t 5"))
    voice "ch5.11_s_006"
    s "I see. I am glad you say that, Tabitha.{#ch5_11_v8672}"
    voice "ch5.11_s_007"
    s "But now it is finally… really over, huh.{#ch5_11_v8673}"
    voice "ch5.11_t_006"
    t "Everything passes, no matter when.{#ch5_11_v15311}"
    voice "ch5.11_s_008"
    s "Passes, huh…{#ch5_11_v8674}"
    voice "ch5.11_t_007"
    t "In happy times and painful times, what matters is knowing that moment.{#ch5_11_v15312}"
    $ show_sprites(("s 2", "t 5"))
    voice "ch5.11_s_009"
    s "Yeah. So today is the end of our special days.{#ch5_11_v8675}"
    voice "ch5.11_t_008"
    t "Yes.{#ch5_11_v15313}"
    voice "ch5.11_t_009"
    t "But, looking at it the other way, up to today we were in a special time.{#ch5_11_v15314}"
    voice "ch5.11_t_010"
    t "…Can I ask you something?{#ch5_11_v15315}"
    voice "ch5.11_s_010"
    s "Hm?{#ch5_11_v8676}"
    voice "ch5.11_t_011"
    t "About your confession in the play.{#ch5_11_v15316}"
    $ show_sprites(("s 2", "t 5"))
    voice "ch5.11_s_011"
    s "Well, that is…{#ch5_11_v8677}"
    voice "ch5.11_t_012"
    t "You dodged the question earlier.{#ch5_11_v15317}"
    $ show_sprites(("s 4", "t 5"))
    voice "ch5.11_s_012"
    s "Sorry.{#ch5_11_v8678}"
    voice "ch5.11_t_013"
    t "Everyone lives wearing some kind of mask.{#ch5_11_v15318}"
    voice "ch5.11_t_014"
    t "I thought that in a play, you put on a visible mask and create a fictional world onstage.{#ch5_11_v15319}"
    voice "ch5.11_t_015"
    t "That is what I thought.{#ch5_11_v15320}"
    $ show_sprites(("s 2", "t 5"))
    voice "ch5.11_s_013"
    s "Um… Tabitha?{#ch5_11_v8679}"
    voice "ch5.11_t_016"
    t "But I felt something during this play.{#ch5_11_v15321}"
    voice "ch5.11_t_017"
    t "Maybe something can flow back from those masks and that fiction.{#ch5_11_v15322}"
    voice "ch5.11_s_014"
    s "Hmm… Is that so?{#ch5_11_v8680}"
    voice "ch5.11_t_018"
    t "That is why I want to know.{#ch5_11_v15323}"
    voice "ch5.11_t_019"
    t "How much of it did you mean? Or was it all acting?{#ch5_11_v15324}"
    menu:
        "I do not know.{#ch5_11_c001}":
            jump ch5_11_date_tabitha_1120
        "I meant all of it!{#ch5_11_c002}":
            jump ch5_11_date_tabitha_1121
        "What about you, Tabitha?{#ch5_11_c003}":
            jump ch5_11_date_tabitha_1122

label ch5_11_date_tabitha_1120:
    $ show_sprites(("s 4", "t 5"))
    voice "ch5.11_s_015"
    s "I do not know. Honestly, I had not thought about it that deeply.{#ch5_11_v8681}"
    voice "ch5.11_t_020"
    t "I see.{#ch5_11_v15325}"
    voice "ch5.11_s_016"
    s "…Still, I cannot say where it began or ended.{#ch5_11_v8682}"
    voice "ch5.11_s_017"
    s "I do not think I held you because of some mask or because we were acting. Probably.{#ch5_11_v8683}"
    voice "ch5.11_t_021"
    t "You can leave out 'probably.'{#ch5_11_v15326}"
    jump ch5_11_date_tabitha_1123

label ch5_11_date_tabitha_1121:
    voice "ch5.11_s_018"
    s "Maybe I meant all of it.{#ch5_11_v8684}"
    voice "ch5.11_t_022"
    t "I will recommend a good hospital.{#ch5_11_v15327}"
    voice "ch5.11_s_019"
    s "H-hey, wait!{#ch5_11_v8685}"
    voice "ch5.11_t_023"
    t "If you cannot take off your mask, that is an illness. It is very frightening.{#ch5_11_v15328}"
    voice "ch5.11_s_020"
    s "Maybe I did feel something as the character…{#ch5_11_v8686}"
    voice "ch5.11_s_021"
    s "But I think it is true that those were my feelings then…{#ch5_11_v8687}"
    voice "ch5.11_t_024"
    t "Really?{#ch5_11_v15329}"
    voice "ch5.11_s_022"
    s "P-probably. But I mean how I felt then.{#ch5_11_v8688}"
    jump ch5_11_date_tabitha_1123

label ch5_11_date_tabitha_1122:
    voice "ch5.11_s_023"
    s "T-Tabitha, what about you?!{#ch5_11_v8689}"
    voice "ch5.11_t_025"
    t "Me?{#ch5_11_v15330}"
    voice "ch5.11_s_024"
    s "What did you think when you heard my confession then?!{#ch5_11_v8690}"
    voice "ch5.11_t_026"
    t "It is unfair to answer a question with a question. I cannot answer.{#ch5_11_v15331}"
    voice "ch5.11_s_025"
    s "Then do not ask me.{#ch5_11_v8691}"
    voice "ch5.11_t_027"
    t "Hm.{#ch5_11_v15332}"
    voice "ch5.11_s_026"
    s "All I can say is that it was not all acting. That is about it.{#ch5_11_v8692}"
    voice "ch5.11_t_028"
    t "I see. Maybe it was the same for me.{#ch5_11_v15333}"
    jump ch5_11_date_tabitha_1123

label ch5_11_date_tabitha_1123:
    voice "ch5.11_t_029"
    t "Still, I am glad I asked.{#ch5_11_v15334}"
    voice "ch5.11_s_027"
    s "I was sweating over here. Give me a little warning next time.{#ch5_11_v8693}"
    voice "ch5.11_t_030"
    t "All right.{#ch5_11_v15335}"
    jump ch5_11_scene_343

label ch5_11_date_haruna:
    $ fade_fx("id(53)", new_music="t21")
    $ show_sprites(("ha 1"))
    voice "ch5.11_ha_001"
    ha "Sigh… It is over now…{#ch5_11_v1661}"
    $ show_sprites(("ha 1", "s 1"))
    voice "ch5.11_s_074"
    s "Haruna, there you are.{#ch5_11_v8709}"
    voice "ch5.11_ha_002"
    ha "…Oh, Hiraga-kun!{#ch5_11_v1662}"
    voice "ch5.11_s_075"
    s "What are you doing here?{#ch5_11_v8710}"
    voice "ch5.11_ha_003"
    ha "Nothing, I was just feeling a little sentimental.{#ch5_11_v1663}"
    voice "ch5.11_ha_004"
    ha "…The festival-like bustle of our days onstage has finally come to an end.{#ch5_11_v1664}"
    voice "ch5.11_s_076"
    s "…Yeah.{#ch5_11_v8711}"
    voice "ch5.11_ha_005"
    ha "I had never been surrounded by so many people, so I got nervous.{#ch5_11_v1665}"
    voice "ch5.11_ha_006"
    ha "…At first, I was desperately trying to imagine the audience as potatoes.{#ch5_11_v1666}"
    voice "ch5.11_s_077"
    s "Oh, I did that too.{#ch5_11_v8712}"
    $ show_sprites(("ha 2", "s 1"))
    voice "ch5.11_ha_007"
    ha "But it was fun.{#ch5_11_v1667}"
    voice "ch5.11_ha_008"
    ha "The atmosphere onstage is really strange.{#ch5_11_v1668}"
    voice "ch5.11_s_078"
    s "Yeah, it really is…{#ch5_11_v8713}"
    voice "ch5.11_s_079"
    s "But we really did manage to pull it off, huh?{#ch5_11_v8714}"
    voice "ch5.11_ha_009"
    ha "Heehee.{#ch5_11_v1669}"
    $ show_sprites(("ha 1", "s 1"))
    voice "ch5.11_s_080"
    s "Well, you had a strong reason: getting your bag back.{#ch5_11_v8715}"
    voice "ch5.11_ha_010"
    ha "Um, well, about that… You see… Actually…{#ch5_11_v1670}"
    voice "ch5.11_ha_011"
    ha "There was a photograph in my bag. I really did not want to lose it.{#ch5_11_v1671}"
    th "What kind of photo could it be?{#ch5_11_th_001}"
    menu:
        "A picture of a pet?{#ch5_11_c004}":
            jump ch5_11_date_haruna_1125
        "A picture of her boyfriend?{#ch5_11_c005}":
            jump ch5_11_date_haruna_1126
        "A picture of me?{#ch5_11_c006}":
            jump ch5_11_date_haruna_1127

label ch5_11_date_haruna_1125:
    voice "ch5.11_s_081"
    s "A picture of a pet?{#ch5_11_v8716}"
    voice "ch5.11_ha_012"
    ha "…No.{#ch5_11_v1672}"
    voice "ch5.11_ha_013"
    ha "I-it is a picture of you, Hiraga-kun…{#ch5_11_v1673}"
    jump ch5_11_date_haruna_1128

label ch5_11_date_haruna_1126:
    voice "ch5.11_s_082"
    s "A picture of your boyfriend, maybe?{#ch5_11_v8717}"
    th "…That would make me really jealous.{#ch5_11_th_002}"
    voice "ch5.11_ha_014"
    ha "…No. It is similar, but different.{#ch5_11_v1674}"
    voice "ch5.11_ha_015"
    ha "I-it is a picture of you, Hiraga-kun…{#ch5_11_v1675}"
    jump ch5_11_date_haruna_1128

label ch5_11_date_haruna_1127:
    voice "ch5.11_s_083"
    s "A picture of me?{#ch5_11_v8718}"
    th "…As if that could be it!{#ch5_11_th_003}"
    voice "ch5.11_ha_016"
    ha "…!!!{#ch5_11_v1676}"
    voice "ch5.11_ha_017"
    ha "H-how did you know?!{#ch5_11_v1677}"
    jump ch5_11_date_haruna_1128

label ch5_11_date_haruna_1128:
    voice "ch5.11_s_084"
    s "…Huh? Mine?{#ch5_11_v8719}"
    voice "ch5.11_ha_018"
    ha "Yes. Here.{#ch5_11_v1678}"
    $ show_sprites(())
    $ dissolve_fx("id(277)", type="cg")
    voice "ch5.11_s_085"
    s "Oh, it really is me.{#ch5_11_v8720}"
    voice "ch5.11_s_086"
    s "W-wait, what?!{#ch5_11_v8721}"
    voice "ch5.11_s_087"
    s "W-why do you have a picture of me in your bag?{#ch5_11_v8722}"
    voice "ch5.11_ha_019"
    ha "H-how should I know what to say to that?!{#ch5_11_v1679}"
    th "I-it is true… She kept a picture of me in her bag.{#ch5_11_th_004}"
    th "Whoa… It did not bother me before, but now that I have noticed it… I am getting embarrassed.{#ch5_11_th_005}"
    $ fade_fx("id(53)")
    $ show_sprites(("ha 1", "s 1"))
    voice "ch5.11_ha_020"
    ha "This is a secret just between Hiraga-kun and me, okay?{#ch5_11_v1680}"
    voice "ch5.11_s_088"
    s "Oh, sure. I understand.{#ch5_11_v8723}"
    voice "ch5.11_ha_021"
    ha "Hehehe…{#ch5_11_v1681}"
    jump ch5_11_scene_343

label ch5_11_date_henrietta:
    $ fade_fx("id(54)", new_music="t21")
    $ show_sprites(("s 1"))
    voice "ch5.11_s_089"
    s "…Princess, may I come in?{#ch5_11_v8724}"
    voice "ch5.11_h_001"
    h "Is that you, my familiar? Please come in.{#ch5_11_v348}"
    voice "ch5.11_s_090"
    s "E-excuse me…{#ch5_11_v8725}"
    $ show_sprites(("h 3"))
    $ fade_fx("id(57)")
    voice "ch5.11_s_091"
    s "…Huh?{#ch5_11_v8726}"
    $ show_sprites(("h 3", "s 4"))
    th "…Come on. Why is the princess wearing the queen's formal dress in a room like this?!{#ch5_11_th_006}"
    voice "ch5.11_s_092"
    s "…Er, um… Princess?{#ch5_11_v8727}"
    voice "ch5.11_h_002"
    h "…The days of celebration are over.{#ch5_11_v349}"
    voice "ch5.11_s_093"
    s "…What?{#ch5_11_v8728}"
    voice "ch5.11_h_003"
    h "From now on, I must return to the castle.{#ch5_11_v350}"
    th "…That is right. Once the play is over, the princess has to return to the castle.{#ch5_11_th_007}"
    th "Maybe the time she spent onstage was what she treasured most.{#ch5_11_th_008}"
    voice "ch5.11_h_004"
    h "…You have truly helped me. I intend to thank everyone, but I also wanted to ask you something, my familiar.{#ch5_11_v351}"
    voice "ch5.11_s_094"
    s "What is it?{#ch5_11_v8729}"
    $ show_sprites(())
    $ dissolve_fx("id(257)", type="cg")
    voice "ch5.11_h_005"
    h "Honestly, how much of that confession in the play did you mean?{#ch5_11_v352}"
    voice "ch5.11_s_095"
    s "Princess, that is…{#ch5_11_v8730}"
    voice "ch5.11_h_006"
    h "…You cannot say you want me to forget it.{#ch5_11_v353}"
    menu:
        "I meant it.{#ch5_11_c007}":
            jump ch5_11_date_henrietta_1130
        "It was not just acting.{#ch5_11_c008}":
            jump ch5_11_date_henrietta_1131
        "I do not know.{#ch5_11_c009}":
            jump ch5_11_date_henrietta_1132

label ch5_11_date_henrietta_1130:
    voice "ch5.11_s_096"
    s "I meant it.{#ch5_11_v8731}"
    voice "ch5.11_h_007"
    h "…{#ch5_11_v354}"
    voice "ch5.11_s_097"
    s "…But if you ask how much, I cannot answer. You are asking where the lie begins.{#ch5_11_v8732}"
    voice "ch5.11_s_098"
    s "…I do not think I was lying. Probably.{#ch5_11_v8733}"
    voice "ch5.11_h_008"
    h "…I see.{#ch5_11_v355}"
    jump ch5_11_date_henrietta_1133

label ch5_11_date_henrietta_1131:
    voice "ch5.11_s_099"
    s "It was not just acting.{#ch5_11_v8734}"
    voice "ch5.11_h_009"
    h "…{#ch5_11_v356}"
    voice "ch5.11_s_100"
    s "At the time, I saw Princess Noelle and the actress playing her as one and the same.{#ch5_11_v8735}"
    voice "ch5.11_s_101"
    s "So my confession was both a line in the play and my own words.{#ch5_11_v8736}"
    voice "ch5.11_h_010"
    h "…I see.{#ch5_11_v357}"
    jump ch5_11_date_henrietta_1133

label ch5_11_date_henrietta_1132:
    voice "ch5.11_s_102"
    s "I do not know.{#ch5_11_v8737}"
    voice "ch5.11_s_103"
    s "The princess and I were caught up in the whirl of the play then.{#ch5_11_v8738}"
    voice "ch5.11_h_011"
    h "…{#ch5_11_v358}"
    voice "ch5.11_s_104"
    s "But even now that I am calm, I can still make that vow.{#ch5_11_v8739}"
    voice "ch5.11_s_105"
    s "Ah… Of course, if the princess permits it.{#ch5_11_v8740}"
    voice "ch5.11_h_012"
    h "I shall think about granting permission.{#ch5_11_v359}"
    jump ch5_11_date_henrietta_1133

label ch5_11_date_henrietta_1133:
    voice "ch5.11_h_013"
    h "I have received an answer I can be satisfied with. Now I can return to the castle without regret.{#ch5_11_v360}"
    voice "ch5.11_s_106"
    s "Will I see you again?{#ch5_11_v8741}"
    voice "ch5.11_h_014"
    h "Yes, next time as your queen…{#ch5_11_v361}"
    voice "ch5.11_s_107"
    s "Understood.{#ch5_11_v8742}"
    $ show_sprites(())
    th "……… …… …{#ch5_11_th_009}"
    $ fade_fx("id(90)")
    voice "ch5.11_h_015"
    h "I am returning to the castle, to the stage of politics, diplomacy, and war…{#ch5_11_v362}"
    voice "ch5.11_h_016"
    h "Unlike the stage, all the blood shed there will be real…{#ch5_11_v363}"
    voice "ch5.11_h_017"
    h "Founder, I pray you grant me good fortune…{#ch5_11_v364}"
    jump ch5_11_scene_343

label ch5_11_scene_343:
    if zero_route == 1:
        jump attention
    elif zero_route == 2:
        jump attention
    elif zero_route == 3:
        jump attention
    elif zero_route == 4:
        jump attention
    elif zero_route == 5:
        jump attention
    else:
        jump attention

label ch5_11_date_louise_1105:
    $ fade_fx("id(204)", new_music="t21")
    voice "ch5.11_s_029"
    s "Y-you look prettier than usual.{#ch5_11_v8638}"
    voice "ch5.11_l_001"
    l "Really?{#ch5_11_v4740}"
    voice "ch5.11_s_030"
    s "What would be the point of lying?{#ch5_11_v8639}"
    jump ch5_11_date_louise_1108

label ch5_11_date_louise_1106:
    $ fade_fx("id(204)", new_music="t21")
    voice "ch5.11_s_031"
    s "You look the same as always.{#ch5_11_v8640}"
    voice "ch5.11_l_002"
    l "Really?{#ch5_11_v4741}"
    voice "ch5.11_s_032"
    s "Of course. Just the same old Louise.{#ch5_11_v8641}"
    jump ch5_11_date_louise_1108

label ch5_11_date_louise_1107:
    $ fade_fx("id(204)", new_music="t21")
    voice "ch5.11_s_033"
    s "Does that dress fit you?{#ch5_11_v8642}"
    voice "ch5.11_l_003"
    l "What kind of question is that?{#ch5_11_v4742}"
    voice "ch5.11_s_034"
    s "N-no, I was just wondering about the dress.{#ch5_11_v8643}"
    voice "ch5.11_l_004"
    l "Only the dress?{#ch5_11_v4743}"
    voice "ch5.11_s_035"
    s "Only the dress.{#ch5_11_v8644}"
    jump ch5_11_date_louise_1108

label ch5_11_date_louise_1108:
    $ dissolve_fx("id(204)", type="cg")
    voice "ch5.11_l_005"
    l "Hmm. Then why will you not look at me?{#ch5_11_v4744}"
    voice "ch5.11_s_036"
    s "Because I am embarrassed, obviously.{#ch5_11_v8645}"
    voice "ch5.11_l_006"
    l "Oh, you are embarrassed? How strange… The great Saito, embarrassed.{#ch5_11_v4745}"
    voice "ch5.11_s_037"
    s "I-idiot. Let us eat before the food gets cold.{#ch5_11_v8646}"
    voice "ch5.11_l_007"
    l "Hehe. All right.{#ch5_11_v4746}"
    jump ch5_11_scene_343

label ch5_11_date_siesta_1110:
    $ dissolve_fx("id(221)", type="cg")
    voice "ch5.11_s_039"
    s "I want to go home.{#ch5_11_v8658}"
    voice "ch5.11_si_006"
    si "Home?{#ch5_11_v14275}"
    voice "ch5.11_s_040"
    s "Yeah. Eating this food made me think of it.{#ch5_11_v8659}"
    voice "ch5.11_si_007"
    si "I am sorry.{#ch5_11_v14276}"
    voice "ch5.11_s_041"
    s "You do not have to apologize, Siesta.{#ch5_11_v8660}"
    jump ch5_11_date_siesta_1113

label ch5_11_date_siesta_1111:
    $ dissolve_fx("id(221)", type="cg")
    voice "ch5.11_s_042"
    s "I could really go for a hamburger.{#ch5_11_v8661}"
    voice "ch5.11_si_008"
    si "A hamburger…?{#ch5_11_v14277}"
    voice "ch5.11_s_043"
    s "Yeah. Breadcrumbs, salt, ground meat, onions… You knead it all together and grill it.{#ch5_11_v8662}"
    voice "ch5.11_si_009"
    si "That sounds doable. Shall I make one next time?{#ch5_11_v14278}"
    voice "ch5.11_s_044"
    s "Really?{#ch5_11_v8663}"
    voice "ch5.11_si_010"
    si "Yes. Look forward to it.{#ch5_11_v14279}"
    jump ch5_11_date_siesta_1113

label ch5_11_date_siesta_1112:
    $ dissolve_fx("id(221)", type="cg")
    voice "ch5.11_s_045"
    s "Anything else about food?{#ch5_11_v8664}"
    voice "ch5.11_si_011"
    si "Let me see… I have heard that you eat black paper and raw fish.{#ch5_11_v14280}"
    voice "ch5.11_si_012"
    si "I was told your eating habits are strange, in any case.{#ch5_11_v14281}"
    voice "ch5.11_s_046"
    s "If you came to my country, you would be shocked.{#ch5_11_v8665}"
    voice "ch5.11_si_013"
    si "I would like to visit your country, Saito.{#ch5_11_v14282}"
    jump ch5_11_date_siesta_1113

label ch5_11_date_siesta_1113:
    voice "ch5.11_s_047"
    s "Thank you for the meal. It was delicious.{#ch5_11_v8666}"
    voice "ch5.11_si_014"
    si "Hehe… You are welcome.{#ch5_11_v14283}"
    jump ch5_11_scene_343

label ch5_11_date_kirche_1115:
    $ fade_fx("id(54)", new_music="t21")
    voice "ch5.11_s_049"
    s "Stop! Stop, Kirche!{#ch5_11_v8704}"
    voice "ch5.11_k_007"
    k "…What is it, darling?{#ch5_11_v2808}"
    voice "ch5.11_s_050"
    s "Um… That sort of thing…{#ch5_11_v8705}"
    voice "ch5.11_k_008"
    k "Honestly… That is just like you, darling.{#ch5_11_v2809}"
    voice "ch5.11_k_015"
    k "Hm, fine. I will forgive you today.{#ch5_11_v2810}"
    jump ch5_11_date_kirche_1118

label ch5_11_date_kirche_1116:
    $ fade_fx("id(54)", new_music="t21")
    voice "ch5.11_s_051"
    s "Y-yes.{#ch5_11_v8706}"
    voice "ch5.11_k_009"
    k "Really?{#ch5_11_v2811}"
    voice "ch5.11_s_052"
    s "Really…{#ch5_11_v8707}"
    voice "ch5.11_k_010"
    k "All right. I will forgive you today.{#ch5_11_v2812}"
    jump ch5_11_date_kirche_1118

label ch5_11_date_kirche_1117:
    $ fade_fx("id(54)", new_music="t21")
    voice "ch5.11_s_053"
    s "No.{#ch5_11_v8708}"
    voice "ch5.11_k_011"
    k "…Darling.{#ch5_11_v2813}"
    th "I should not have refused here, should I?{#ch5_11_th_007}"
    voice "ch5.11_k_012"
    k "All right. I will forgive you today.{#ch5_11_v2814}"
    jump ch5_11_date_kirche_1118

label ch5_11_date_kirche_1118:
    voice "ch5.11_k_013"
    k "Still, I envy a love that burns both body and soul.{#ch5_11_v2815}"
    voice "ch5.11_k_014"
    k "Do you not feel the same, darling?{#ch5_11_v2816}"
    jump ch5_11_scene_343
