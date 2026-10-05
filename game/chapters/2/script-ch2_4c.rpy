# Глава 2, часть 4c (сцены 1266–1280): выбор локации — 中庭 (Кирхе),
# 教室 (Табита) и ルイズの部屋 (Харуна).
# Источник: ps2_source/chapters/chapter_03_黒髪の来訪者.txt (scene 01266…01280)
# Точные аргументы: ps2_source/events_full/chapter_03_黒髪の来訪者.txt (SCENE 01266…01280)
# Вызываются из карты script-ch2_4.rpy (ch2_4_map) как цели sprite_choice.

label yard_ch2_4:
    # ==== SCENE 1266 ====
    $ fade_fx("yard_evening", new_music="t7", sprites=("d 1", "s 2"))

    voice "ch2.5_s_049"
    s "Because of the commotion earlier, there's hardly anyone around."

    voice "ch2.5_d_003"
    d "To any regular person, nobody's gonna stick their neck into something that troublesome on purpose."

    voice "ch2.5_s_050"
    s "Yeah, true."

    voice "ch2.5_d_004"
    d "Except that rare exception happens to be you, partner."

    $ show_sprites(("d 1", "s 4 angry"))
    voice "ch2.5_s_051"
    s "Shut up."

    $ show_sprites(("k 1", "s 4 angry"))
    voice "ch2.5_k_001"
    k "Oh my, if it isn't Darling. What are you doing in a place like this?"

    $ update_sympathy(20, char_key="kirche")

    $ show_sprites(("k 1", "s 2"))
    voice "ch2.5_s_052"
    s "Kirche? What are you doing here?"

    voice "ch2.5_k_002"
    k "What are YOU doing here, Darling?"

    voice "ch2.5_s_053"
    s "I was worried those guys might come back, so I was doing a bit of patrolling."

    $ show_sprites(("k 4 shy", "s 2"))
    voice "ch2.5_k_003"
    k "My, as expected of Darling. The brave side of you gives me a thrill too!"

    voice "ch2.5_s_054"
    s "But what about you, Kirche — why did you come back? They might still be here."

    $ show_sprites(("k 1 happy", "s 2"))
    voice "ch2.5_k_004"
    k "My, are you worried about me? I'm happy, Darling."

    $ show_sprites(("k 1 happy", "s 4 sad"))
    voice "ch2.5_s_055"
    s "Look..."

    menu:
        "I'd worry about anyone.{#ch2.5_m1266a}":
            # ==== SCENE 1267 ====
            $ show_sprites(("k 1 happy", "s 2"))
            voice "ch2.5_s_056"
            s "I'd worry about anyone."

            voice "ch2.5_k_005"
            k "Oh my, what a shame. I'd just hoped you'd worry about me alone..."

            voice "ch2.5_s_057"
            s "Like I could. At the very least, if it's people I know, anyone would worry."

            $ show_sprites(("k 4 shy", "s 2"))
            voice "ch2.5_k_006"
            k "Huh. Darling really is broad-minded."

            $ show_sprites(("k 4 shy", "s 4 sad"))
            voice "ch2.5_s_058"
            s "Is that so?{#ch2.5_s9513}"

            $ show_sprites(("k 1", "s 4 sad"))
            voice "ch2.5_k_007"
            k "That's right."

        "I'm worried because it's you, Kirche.{#ch2.5_m1266b}":
            # ==== SCENE 1268 ====
            $ show_sprites(("k 1 happy", "s 2"))
            voice "ch2.5_s_059"
            s "Because it's you, Kirche, I'm worried."

            voice "ch2.5_k_008"
            k "My, how honest of you."

            $ show_sprites(("k 1 happy", "s 2 angry"))
            voice "ch2.5_s_060"
            s "At least take me seriously. I know you're strong, Kirche, but your opponents are unknowns."

            $ show_sprites(("k 1 shy", "s 2 angry"))
            voice "ch2.5_k_009"
            k "I never let my guard down. A fight can happen anytime. ...But I'm happy about your honest feelings, Darling."

            $ update_sympathy(10, char_key="kirche")

            $ show_sprites(("k 1 shy", "s 4 sad"))
            voice "ch2.5_s_061"
            s "Hah."

            $ show_sprites(("k 1", "s 4 sad"))
            voice "ch2.5_k_010"
            k "There's no girl who wouldn't be happy to have a knight who cherishes her."

        "It's not like I'm worried about you.{#ch2.5_m1266c}":
            # ==== SCENE 1269 ====
            $ show_sprites(("k 1 happy", "s 4 happy"))
            voice "ch2.5_s_062"
            s "It's not like I'm worried about you."

            $ show_sprites(("k 4 angry", "s 4 happy"))
            voice "ch2.5_k_011"
            k "What's that supposed to mean?"

            $ update_sympathy(-10, char_key="kirche")

            voice "ch2.5_s_063"
            s "Well, you're pretty strong among the mages I've met, Kirche. Wouldn't worrying about you be rude?"

            voice "ch2.5_k_012"
            k "That assessment is fair enough, but putting it that way is rude."

            $ show_sprites(("k 4 angry", "s 4 sad"))
            voice "ch2.5_s_064"
            s "Gah. R-right. Sorry."

            $ show_sprites(("k 1", "s 4 sad"))
            voice "ch2.5_k_013"
            k "It's fine. Just be careful from now on."

            voice "ch2.5_s_065"
            s "Yes.{#ch2.5_s9520}"

    # ==== SCENE 1270 ====
    $ show_sprites(("k 1", "s 2"))
    voice "ch2.5_s_066"
    s "In the end, why are you here, Kirche?"

    voice "ch2.5_k_014"
    k "I was wondering whether any clues from those guys were left behind, even a little. I was looking around."

    voice "ch2.5_s_067"
    s "So, did you find anything, Kirche?"

    voice "ch2.5_k_015"
    k "About that explosion — I can say there are no traces of a bomb or magic having been used. That much, anyway."

    voice "ch2.5_k_016"
    k "Though Professor Colbert took the surrounding soil to his research room, so he's probably planning to examine that as well."

    voice "ch2.5_s_068"
    s "I see. If you find anything, let me know too."

    $ show_sprites(("k 1 happy", "s 2"))
    voice "ch2.5_k_017"
    k "Understood. Do your best on your patrol too, Darling."

    $ ch2_4_visited.add("yard")
    return

label classroom_ch2_4:
    # ==== SCENE 1271 ====
    $ fade_fx("classroom_evening", new_music="t8", sprites="s 2")

    voice "ch2.5_s_069"
    s "Looks like there's no particular damage here. ...Hey, Tabitha's here."

    $ show_sprites(("t 1", "s 4 sad"))
    t "……。{#ch2.5_t1271}"

    $ update_sympathy(30, char_key="tabitha")

    th "She's reading a book completely normally. Like that commotion earlier never even happened."

    voice "ch2.5_s_070"
    s "Hey, Tabitha. Was the classroom all right?"

    voice "ch2.5_t_001"
    t "...All right?"

    voice "ch2.5_s_071"
    s "The explosion just now. There was a huge noise outside, right?"

    voice "ch2.5_t_002"
    t "...Mm-hm."

    voice "ch2.5_s_072"
    s "Tabitha, were you okay?"

    voice "ch2.5_t_003"
    t "...Yes. Why?"

    voice "ch2.5_s_073"
    s "Why do you ask...?"

    voice "ch2.5_t_004"
    t "...Why do you ask that?"

    voice "ch2.5_s_074"
    s "Because..."

    menu:
        "I was worried about Tabitha.{#ch2.5_m1271a}":
            # ==== SCENE 1272 ====
            $ show_sprites(("t 1", "s 2"))
            voice "ch2.5_s_075"
            s "Because I was worried about Tabitha."

            voice "ch2.5_t_005"
            t "...I see.{#ch2.5_t15421}"

            $ update_sympathy(15, char_key="tabitha")

            $ show_sprites(("t 1", "s 4 sad"))
            voice "ch2.5_s_076"
            s "...Yeah.{#ch2.5_s9531}"

            th "Being ignored this skillfully is honestly kind of refreshing..."

            voice "ch2.5_t_006"
            t "...Why?"

            voice "ch2.5_s_077"
            s "Huh?{#ch2.5_s9532}"

            t "……。{#ch2.5_t1272a}"

            th "Um... I'm not imagining things, right?"

            $ show_sprites(("t 1", "s 2"))
            voice "ch2.5_s_078"
            s "You ask why... I guess because I was curious."

            voice "ch2.5_t_007"
            t "...I see.{#ch2.5_t15423}"

            voice "ch2.5_s_079"
            s "Yeah.{#ch2.5_s9534}"

            t "……。{#ch2.5_t1272b}"

            $ show_sprites(("t 1", "s 4 sad"))
            th "Um, um... I have no idea how I'm supposed to react!"

            th "Doesn't seem like she hates me, but..."

        "I was worried about everyone in the classroom.{#ch2.5_m1271b}":
            # ==== SCENE 1273 ====
            $ show_sprites(("t 1", "s 4"))
            voice "ch2.5_s_080"
            s "Because I was worried about everyone in the classroom."

            voice "ch2.5_t_008"
            t "...Everyone's fine."

            voice "ch2.5_s_081"
            s "Ah... right.{#ch2.5_s9536}"

            voice "ch2.5_s_082"
            s "……。{#ch2.5_s1273}"

            t "……。{#ch2.5_t1273}"

            $ show_sprites(("t 1", "s 4 sad"))
            th "Ugh, I can't keep the silence going."

        "No particular reason.{#ch2.5_m1271c}":
            # ==== SCENE 1274 ====
            $ show_sprites(("t 1", "s 4"))
            voice "ch2.5_s_083"
            s "No particular reason."

            voice "ch2.5_t_009"
            t "...I see.{#ch2.5_t15425}"

            $ update_sympathy(-15, char_key="tabitha")

            voice "ch2.5_s_084"
            s "U-um."

            t "……。{#ch2.5_t1274}"

            voice "ch2.5_s_085"
            s "……。{#ch2.5_s1274}"

            voice "ch2.5_t_010"
            t "...What?{#ch2.5_t15426}"

            $ show_sprites(("t 1", "s 4 sad"))
            voice "ch2.5_s_086"
            s "N-no, nothing in particular... nothing."

            th "Don't know why, but maybe she's in a bad mood. Or maybe I'm interrupting her reading."

            voice "ch2.5_s_087"
            s "Um, did I interrupt? Sorry about that."

    # ==== SCENE 1275 ====
    voice "ch2.5_t_011"
    t "...So, what are you doing?"

    $ show_sprites(("t 1", "s 4"))
    voice "ch2.5_s_088"
    s "Huh? Ah, um, I'm patrolling the academy."

    voice "ch2.5_t_012"
    t "...I see. Do your best."

    voice "ch2.5_s_089"
    s "R-right.{#ch2.5_s9544}"

    $ show_sprites("s 4")
    voice "ch2.5_s_090"
    s "Hmm. I don't quite get it, but I'm pretty sure this place is abnormal."

    $ show_sprites(("d 1", "s 4"))
    voice "ch2.5_d_005"
    d "Wouldn't it be more likely that that girl just hasn't noticed?"

    $ show_sprites(("d 1", "s 4 happy"))
    voice "ch2.5_s_091"
    s "...I believe in Tabitha."

    $ show_sprites(("d 1 sad", "s 4 happy"))
    voice "ch2.5_d_006"
    d "Your eyes are totally swimming, partner."

    $ show_sprites(("d 1 sad", "s 4 sad"))
    voice "ch2.5_s_092"
    s "……。{#ch2.5_s1275}"

    voice "ch2.5_d_007"
    d "……。{#ch2.5_d1275}"

    $ show_sprites(("d 1 sad", "s 2"))
    voice "ch2.5_s_093"
    s "Well then. Time to get moving."

    $ ch2_4_visited.add("classroom")
    return

label l_room_ch2_4:
    # ==== SCENE 1276 ====
    $ fade_fx("ha_sick_3", new_music="t10", type="cg")
    play sound open_door

    voice "ch2.5_ha_001"
    ha "Kyaa!?"

    voice "ch2.5_s_094"
    s "Whoa!?{#ch2.5_s9549}"

    voice "ch2.5_ha_002"
    ha "Ah, Hiraga-kun."

    $ update_sympathy(20, char_key="haruna")

    voice "ch2.5_s_095"
    s "Sorry. I startled you."

    voice "ch2.5_ha_003"
    ha "Ah, no. The door suddenly opened, so I was just a little startled. But what's wrong?"

    voice "ch2.5_s_096"
    s "Yeah, there was a big noise just now, right?"

    voice "ch2.5_ha_004"
    ha "Yes. There was a big noise, like fireworks."

    voice "ch2.5_s_097"
    s "Actually, there was an explosion out in the courtyard."

    voice "ch2.5_ha_005"
    ha "An explosion!?"

    voice "ch2.5_s_098"
    s "Yeah. ...Those guys who came after you yesterday — they snuck into the academy."

    voice "ch2.5_ha_006"
    ha "I-see... so that's what it was."

    voice "ch2.5_s_099"
    s "We managed to drive them off, but... they might come back, so I was patrolling the academy."

    voice "ch2.5_ha_007"
    ha "Ah... yes, I understand. Hiraga-kun, is there anything I should be careful about...?"

    voice "ch2.5_s_100"
    s "Let's see..."

    menu:
        "At least I'm glad you're safe, Haruna.{#ch2.5_m1276a}":
            # ==== SCENE 1277 ====
            voice "ch2.5_s_101"
            s "At any rate, I'm just glad you're safe, Haruna."

            $ dissolve_fx("ha_sick_2", type="cg")
            voice "ch2.5_ha_008"
            ha "Eh?{#ch2.5_h1857}"

            $ update_sympathy(10, char_key="haruna")

            voice "ch2.5_s_102"
            s "Those guys were after you, weren't they? I thought it'd be terrible if you were found."

            voice "ch2.5_ha_009"
            ha "Hiraga-kun... you were worried about me."

            voice "ch2.5_s_103"
            s "Of course I was. That goes without saying, right?"

            voice "ch2.5_ha_010"
            ha "...Thank you."

            $ dissolve_fx("ha_sick_3", type="cg")

        "Make sure nobody else finds you.{#ch2.5_m1276b}":
            # ==== SCENE 1278 ====
            voice "ch2.5_s_104"
            s "Make sure nobody else finds you."

            voice "ch2.5_ha_011"
            ha "Yes, I'll be careful. Siesta-san warned me too that I mustn't be seen by the academy's people."

            voice "ch2.5_s_105"
            s "That's good, but... everyone here uses magic, so you can't judge by appearances."

            $ dissolve_fx("ha_sick_2", type="cg")
            voice "ch2.5_ha_012"
            ha "Yes... I'll be careful."

            $ dissolve_fx("ha_sick_3", type="cg")

        "Just stay put, okay?{#ch2.5_m1276c}":
            # ==== SCENE 1279 ====
            voice "ch2.5_s_106"
            s "Just stay put, okay?"

            voice "ch2.5_ha_013"
            ha "Eh, yes. I intend to stay in this room just as I was told."

            voice "ch2.5_s_107"
            s "Good, then you'll be fine."

            voice "ch2.5_s_108"
            s "It's just... the girls around me tend to be the charge-ahead type, so... I've started to worry."

            voice "ch2.5_ha_014"
            ha "Hiraga-kun... do you date that many girls?"

            $ update_sympathy(-10, char_key="haruna")

            voice "ch2.5_s_109"
            s "N-no... I'm not dating anyone. Louise mostly just treats me as her familiar anyway."

            voice "ch2.5_ha_015"
            ha "But... you seem to be on good terms with all sorts of girls..."

            voice "ch2.5_s_110"
            s "I-is that so...? Hahahaha."

            voice "ch2.5_ha_016"
            ha "Hm..."

    # ==== SCENE 1280 ====
    voice "ch2.5_s_111"
    s "Anyway, don't leave this room. If a stranger calls out, don't answer."

    voice "ch2.5_ha_017"
    ha "Yes, understood.{#ch2.5_h1866}"

    voice "ch2.5_s_112"
    s "Well, I'm off to patrol the rest."

    voice "ch2.5_ha_018"
    ha "You be careful too, Hiraga-kun."

    voice "ch2.5_s_113"
    s "Yeah.{#ch2.5_s9568}"

    play sound open_door

    $ ch2_4_visited.add("l_room")
    return
