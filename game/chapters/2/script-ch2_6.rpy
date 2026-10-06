# Глава 2, часть 6 (сцены 125–131 + свидание с Луизой 1034–1037):
# ночной разговор в комнате Луизы (CG155), выбор 126/127/128,
# возвращение Луизы и Сиесты, кабинет Османа (сцена 130), утро (131)
# и выбор свидания; первая ветка свидания — 1034–1037.
# Источник: ps2_source/chapters/chapter_03_黒髪の来訪者.txt
# Точные аргументы: ps2_source/events_full/chapter_03_黒髪の来訪者.txt
# Сцены 132–136 — редиректы движка (0 реплик), не портируются.
# Ветки свиданий остальных девушек — в script-ch2_7/8.rpy.

label ch2_6:
    # ==== SCENE 125 ====
    $ fade_fx("ha_sick_3", type="cg", new_music="t19")
    voice "ch2.6_s_001"
    s "Phew..."
    voice "ch2.6_ha_001"
    ha "Hiraga-kun... Louise isn't back yet, is she?"
    voice "ch2.6_s_002"
    s "...No."
    voice "ch2.6_ha_002"
    ha "Worried?"
    voice "ch2.6_s_003"
    s "...A little, yeah."
    th "Where did those two go? Louise I'd expect, but for Siesta to be gone too..."
    th "Should I go look for them again? Maybe I'll swing by outside this time..."
    stop music fadeout 1.0
    call open_door("left", "louise_room_night") from _call_open_door_9
    play music t28 fadein 1.0
    $ show_sprites(("l 1 happy", "si 1 happy"))
    voice "ch2.6_l_001"
    l "We just got back."
    voice "ch2.6_si_001"
    si "Sorry to keep you waiting, Saito-san. I'm back now."
    $ show_sprites(("s 1 angry",))
    voice "ch2.6_s_004"
    s "Louise! Siesta!"
    $ show_sprites(("l 1 sad", "s 1 angry"))
    voice "ch2.6_l_002"
    l "Goodness, look at that shocked face..."
    $ show_sprites(("l 1 sad", "s 1 sad"))
    voice "ch2.6_s_005"
    s "You... You were so late, you had me worried sick, you know?"
    voice "ch2.6_l_003"
    l "Worried...? Okay, so I was a little late getting back, but it's not even midnight yet."
    $ show_sprites(("l 1 sad", "s 1 angry"))
    voice "ch2.6_s_006"
    s "You've forgotten what happened this afternoon, haven't you? There's no guarantee those bastards won't come again!"
    $ show_sprites(("si 1 sad", "s 1 angry"))
    voice "ch2.6_si_002"
    si "Please don't be so angry, Saito-san. I'm partly to blame for the delay."
    $ show_sprites(("si 1 sad", "s 3 sad"))
    voice "ch2.6_s_007"
    s "Siesta?"
    voice "ch2.6_si_003"
    si "Miss Vallière and I were talking for a while."
    voice "ch2.6_s_008"
    s "Talking? About what, exactly..."
    $ show_sprites(("si 4", "s 3 sad"))
    voice "ch2.6_si_004"
    si "It's a ladies' conversation, so naturally it's a secret from you, Saito-san."
    $ show_sprites(("si 4", "s 1 shy"))
    voice "ch2.6_s_009"
    s "O-oh, is that so."
    th "An important talk between women...? That has a rather thrilling ring to it."
    $ show_sprites(("l 3 sad", "s 1 shy"))
    voice "ch2.6_l_004"
    l "I owe Haruna an apology."
    $ show_sprites(("l 3 sad", "s 3 sad"))
    voice "ch2.6_s_010"
    s "Louise?"
    $ fade_fx("ha_sick_3", type="cg")
    voice "ch2.6_l_005"
    l "Suddenly there were more people in the room, and I got all irritable because I couldn't settle down. I'm sorry."
    voice "ch2.6_ha_003"
    ha "Y-yes... n-no..."
    voice "ch2.6_l_006"
    l "Don't worry about what I said earlier. Make yourself at home tomorrow too."
    voice "ch2.6_ha_004"
    ha "Yes... Thank you very much."
    $ fade_fx("louise_room_night", sprites=("s 3 sad",))
    th "Louise suddenly started being nice out of nowhere... Which somehow creeps me out — no, downright scares me."
    voice "ch2.6_s_011"
    s "Hey, Siesta."
    $ show_sprites(("si 1", "s 3 sad"))
    voice "ch2.6_si_005"
    si "Yes?{#ch2.6_si_005}"
    voice "ch2.6_s_012"
    s "So..."
    menu:
        "Did something happen to Louise?{#ch2.6_m125a}":
            # ==== SCENE 126 ====
            voice "ch2.6_s_013"
            s "Did something happen to Louise?"
            $ show_sprites(("si 1 sad", "s 3 sad"))
            voice "ch2.6_si_006"
            si "Something like what?"
            $ show_sprites(("si 1 sad", "s 3 happy"))
            voice "ch2.6_s_014"
            s "Well... I hope I'm wrong, but her suddenly being so nice just feels off somehow."
            $ show_sprites(("si 1", "s 3 happy"))
            voice "ch2.6_si_007"
            si "Is that so? Nothing in particular."
            $ update_sympathy(10, char_key="siesta")
            $ show_sprites(("si 1", "s 3"))
            voice "ch2.6_s_015"
            s "I see. If you didn't notice anything, then maybe I imagined it."
            jump ch2_6_night
        "What were you talking about earlier?{#ch2.6_m125b}":
            # ==== SCENE 127 ====
            voice "ch2.6_s_016"
            s "What were you talking about earlier?"
            voice "ch2.6_si_008"
            si "I told you. It's a secret, so I can't say."
            $ show_sprites(("si 1", "s 3"))
            voice "ch2.6_s_017"
            s "Come on, do me a favor here."
            $ update_sympathy(-10, char_key="siesta")
            $ show_sprites(("si 1 angry", "s 3"))
            voice "ch2.6_si_009"
            si "Trying to force a girl to give up her secret is awfully rude, you know."
            $ show_sprites(("si 1 angry", "s 3 sad"))
            voice "ch2.6_s_018"
            s "Ugh. When you put it that way, I'm sunk."
            $ show_sprites(("si 1", "s 3 sad"))
            voice "ch2.6_si_010"
            si "So, I can't tell you any more than that."
            voice "ch2.6_s_019"
            s "Hmm... I guess there's nothing I can do."
            jump ch2_6_night
        "Could you take the dishes back?":
            # ==== SCENE 128 ====
            $ show_sprites(("si 1", "s 1"))
            voice "ch2.6_s_020"
            s "Could you take the dishes back to the dining hall?"
            voice "ch2.6_si_011"
            si "Ah, sure. Understood. I'll take them all to the kitchen later."
            voice "ch2.6_s_021"
            s "Sorry for making extra work for you."
            voice "ch2.6_si_012"
            si "It's no trouble at all. By the way, was dinner good?"
            $ show_sprites(("si 1", "s 3 happy"))
            voice "ch2.6_s_022"
            s "Yeah, it was great. Thanks, Siesta."
            $ show_sprites(("si 1 happy", "s 3 happy"))
            voice "ch2.6_si_013"
            si "Hehe, you're welcome."
            jump ch2_6_night
label ch2_6_night:
    # ==== SCENE 129 ====
    $ show_sprites(("l 3 happy",))
    th "Still, rather than being in a good mood, she just seems... gracious."
    th "If she's going to get along with Haruna, I couldn't ask for more, but..."
    th "I just hope nothing else strange happens."
    stop music fadeout 1.0
    jump ch2_6_cabinet
label ch2_6_cabinet:
    # ==== SCENE 130 ====
    $ fade_fx("osman_cabinet_night", new_music="t31")
    voice "ch2.6_o_001"
    o "So, how did it go? Was there anything at the blast site?"
    $ show_sprites(("c 1", "o 1"))
    voice "ch2.6_c_001"
    c "Yes. Examining the blast site, we recovered what appears to be residue from the bomb."
    voice "ch2.6_o_002"
    o "Hmm."
    voice "ch2.6_c_002"
    c "A full analysis will take time, but a preliminary examination has already turned up a few things."
    $ show_sprites(("c 1", "o 1 sad"))
    voice "ch2.6_o_003"
    o "Such as?"
    voice "ch2.6_c_003"
    c "That the bomb was made differently from anything in ordinary circulation."
    voice "ch2.6_c_004"
    c "The destructive power, the blast radius — everything is different. I'd say it's unmistakably military."
    voice "ch2.6_o_004"
    o "...Hmm. Are you certain?"
    $ show_sprites(("c 1 angry", "o 1 sad"))
    voice "ch2.6_c_005"
    c "Yes, I'm certain."
    $ show_sprites(("c 1 angry", "o 1 angry"))
    voice "ch2.6_o_005"
    o "You mean to say... that a country — or an army — is behind this incident?"
    $ show_sprites(("c 1 sad", "o 1 angry"))
    voice "ch2.6_c_006"
    c "No, I can't say that for certain yet..."
    $ show_sprites(("c 1", "o 1 angry"))
    voice "ch2.6_c_007"
    c "But if we deduce the bomb's structure and compare it with the bomb technology of every country, including our own..."
    $ show_sprites(("c 1", "o 1"))
    voice "ch2.6_o_006"
    o "Then we can narrow down which country the culprit is from — or which organization they belong to."
    voice "ch2.6_c_008"
    c "Yes. It will take some time, but..."
    voice "ch2.6_o_007"
    o "Understood. I'm counting on you."
    voice "ch2.6_o_008"
    o "If we had the time, I'd have you dig into this at leisure — but that isn't possible."
    $ show_sprites(("c 1 sad", "o 1"))
    voice "ch2.6_c_009"
    c "But... what in the world is going on?"
    voice "ch2.6_c_010"
    c "Between that war with the Reconquista army the other day, everything has become so unsettled."
    $ show_sprites(("c 1 sad", "o 1 angry"))
    voice "ch2.6_o_009"
    o "That lies beyond what we should be speculating about. First we must devote all our effort to the students' safety."
    $ show_sprites(("c 1 angry", "o 1 angry"))
    voice "ch2.6_c_011"
    c "R-right. I'll get on with the investigation at once."
    $ show_sprites(("o 1",))
    voice "ch2.6_o_010"
    o "I only hope this doesn't blow up any further... For now, all we can do is pray."
    stop music fadeout 1.0
    jump ch2_6_morning
label ch2_6_morning:
    # ==== SCENE 131 ====
    $ fade_fx("sky", new_music="t4", type="cg")
    th "Ugh, good grief... It's morning already?"
    th "I feel like all I've done lately is get tired..."
    th "Well then... what should I do now? Maybe I'll invite someone and go somewhere."
    stop music fadeout 1.0

    $ portrait_choice([
        {"char": "louise",   "text": "Go on a date with Louise",  "target": "date_louise_ch2_6"},
        {"char": "siesta",   "text": "Go on a date with Siesta",  "target": "date_siesta_ch2_7"},
        {"char": "tabitha",  "text": "Go on a date with Tabitha", "target": "date_tabitha_ch2_7"},
        {"char": "kirche",   "text": "Go on a date with Kirche",  "target": "date_kirche_ch2_8"},
        {"char": "haruna",   "text": "Go on a date with Haruna",  "target": "date_haruna_ch2_8"},
    ])

    $ fade_fx("black")
    stop music fadeout 1.0
    jump ch3

label date_louise_ch2_6:
    # ==== SCENE 1034 ====
    $ fade_fx("yard", new_music="t5", sprites=("s 3",))
    voice "ch2.6_s_023"
    s "Hey, Louisee— wait, why are you getting ready to go out?"
    $ show_sprites(("l 6 happy", "s 3"))
    $ update_sympathy(20, char_key="louise")
    voice "ch2.6_l_007"
    l "Oh, Saito. Perfect timing. I'm heading to the ranch!"
    $ show_sprites(("l 6 happy", "s 3 sad"))
    voice "ch2.6_s_024"
    s "Huh? Why the ranch?"
    $ show_sprites(("l 6 angry", "s 3 sad"))
    voice "ch2.6_l_008"
    l "Stop yapping and let's go!"
    $ show_sprites(("l 6 angry", "s 3 angry"))
    voice "ch2.6_s_025"
    s "Wait, where did this sudden turn come from!?"
    $ fade_fx("forest", sprites=("l 6 happy", "s 1"))
    voice "ch2.6_l_009"
    l "Look — the blue sky, the white clouds, this fresh morning air! It lifts your spirits!"
    voice "ch2.6_s_026"
    s "Yeah, you're right. It does feel great."
    $ show_sprites(("s 1 sad",))
    voice "ch2.6_s_027"
    s "Hang on... huh? Where did she go?"
    $ fade_fx("id(208)", type="cg")
    voice "ch2.6_l_010"
    l "Sorry to keep you waiting!"
    voice "ch2.6_s_028"
    s "Where were you? And what's that in your hand?"
    voice "ch2.6_l_011"
    l "Goodness, haven't you seen it before? It's milk."
    voice "ch2.6_s_029"
    s "No, I mean, sure, I can tell by looking — I know what it is."
    voice "ch2.6_l_012"
    l "Fufufu. I've just gotten it straight from the ranch — fresh from the cow!"
    voice "ch2.6_s_030"
    s "Sounds delicious... Wait, do you even like milk that much?"
    voice "ch2.6_l_013"
    l "This is a challenge."
    voice "ch2.6_s_031"
    s "A challenge? Milady, what exactly do you intend to do?"
    voice "ch2.6_l_014"
    l "Nothing to you, Saito. If anything, it's putting wisdom into practice — proof of knowledge!"
    voice "ch2.6_s_032"
    s "Sorry, I have no idea what you're talking about."
    voice "ch2.6_l_015"
    l "They say drinking milk makes you grow, don't they?"
    voice "ch2.6_s_033"
    s "Makes you what?"
    voice "ch2.6_l_016"
    l "...All sorts of things!"
    voice "ch2.6_l_017"
    l "True, for a noble like me to drink a cow's milk straight — it's rather unbecoming, I'll admit."
    voice "ch2.6_l_018"
    l "But if I don't drink milk now, I'll never grow! That's how it works, I'm sure of it!"
    voice "ch2.6_l_019"
    l "In that case! Betting on an old saying is also a path worth taking."
    voice "ch2.6_l_020"
    l "Fufufufufufufu... Once I drink this, I'll leave Kirche in the dust..."
    voice "ch2.6_s_034"
    s "Sigh. Fine, whatever..."
    menu:
        "Bigger where, exactly?{#ch2.6_m1034a}":
            # ==== SCENE 1035 ====
            $ fade_fx("forest", sprites=("l 6 happy", "s 1 angry"))
            voice "ch2.6_s_035"
            s "Bigger where, exactly?"
            stop music fadeout 1.0
            play music t29 fadein 1.0
            $ show_sprites(("l 6 shy", "s 1 angry"))
            voice "ch2.6_l_021"
            l "W-where...?"
            voice "ch2.6_l_022"
            l "Th-that doesn't matter!"
            $ show_sprites(("l 6 shy", "s 3 happy"))
            voice "ch2.6_s_036"
            s "Hmm? Aha, I get it."
            $ show_sprites(("l 6 shy", "s 1 happy"))
            voice "ch2.6_s_037"
            s "You want your chest to get bigger, don't you? Well, one glass of milk won't make it happen overnight, you know~"
            $ show_sprites(("l 6 angry", "s 1 happy"))
            voice "ch2.6_l_023"
            l "Shut up! It's none of your business!!"
            $ update_sympathy(-10, char_key="louise")
            # Удар (SE +62, vibrate(2), +61) + белая вспышка — спрайты меняются под ней
            $ scene_fx("hit flash", sound="punch", duration=(0.3, 2), sprites=("l 6 angry", "s 3 sad"))
            voice "ch2.6_s_038"
            s "Guh! Ouch! I'm done for—!!"
            voice "ch2.6_l_024"
            l "Hah, hah, hah..."
            jump date_louise_ch2_7
        "You don't have to push yourself.{#ch2.6_m1034b}":
            # ==== SCENE 1036 ====
            $ fade_fx("forest", sprites=("l 6 happy", "s 3 happy"))
            voice "ch2.6_s_039"
            s "You don't have to push yourself, you know."
            stop music fadeout 1.0
            play music t29 fadein 1.0
            $ show_sprites(("l 6 angry", "s 3 happy"))
            voice "ch2.6_l_025"
            l "Hah? What do you mean, push myself!"
            $ show_sprites(("l 6 angry", "s 1"))
            voice "ch2.6_s_040"
            s "Calm down. Listen carefully to what I'm saying."
            voice "ch2.6_s_041"
            s "Even if you don't force yourself to grow, you can just wait and let it happen naturally."
            voice "ch2.6_s_042"
            s "I'm not saying trying is bad — but you're fine just the way you are without overreaching."
            $ show_sprites(("l 6 shy", "s 1"))
            voice "ch2.6_l_026"
            l "Eh... um, um, Saito?"
            $ update_sympathy(10, char_key="louise")
            $ show_sprites(("l 6 shy", "s 3"))
            voice "ch2.6_s_043"
            s "If you strain yourself and hurt your body, that defeats the whole point, doesn't it? Just take it easy."
            voice "ch2.6_l_027"
            l "Ah... yeah. I wasn't planning to force myself..."
            voice "ch2.6_l_028"
            l "I mean, um, well... I just wanted to try it, that's all."
            voice "ch2.6_l_029"
            l "And besides, you... I mean, men — they say they like them bigger, don't they?"
            voice "ch2.6_s_044"
            s "Do they? I think that varies from person to person."
            voice "ch2.6_l_030"
            l "Eh? But I'm pretty sure you said you like them bigger..."
            $ show_sprites(("l 6 shy", "s 1 angry"))
            voice "ch2.6_s_045"
            s "Huh? I said that?"
            $ show_sprites(("l 6 angry", "s 1 angry"))
            voice "ch2.6_l_031"
            l "N-nothing! Don't ask weird questions!"
            jump date_louise_ch2_7
        "Give me some too.{#ch2.6_m1034c}":
            # ==== SCENE 1037 ====
            $ fade_fx("forest", sprites=("l 6 happy", "s 1 angry"))
            voice "ch2.6_s_046"
            s "Give me some too."
            stop music fadeout 1.0
            play music t29 fadein 1.0
            $ show_sprites(("l 6 angry", "s 1 angry"))
            voice "ch2.6_l_032"
            l "Huh?{#ch2.6_l_032}"
            $ show_sprites(("l 6 angry", "s 1 sad"))
            voice "ch2.6_s_047"
            s "No, I'm saying — pour me some of the milk too."
            $ show_sprites(("l 6 sad", "s 1 sad"))
            voice "ch2.6_l_033"
            l "Wh-why?"
            $ show_sprites(("l 6 sad", "s 3 happy"))
            voice "ch2.6_s_048"
            s "Well, it just looks fresh and tasty... Is there some other reason?"
            $ show_sprites(("l 6 angry", "s 3 happy"))
            voice "ch2.6_l_034"
            l "No."
            $ show_sprites(("l 6 angry", "s 3 angry"))
            voice "ch2.6_s_049"
            s "Why not!?"
            voice "ch2.6_l_035"
            l "There's none to spare for you. I had to ask the ranchers for this specially, you know."
            $ show_sprites(("l 6 angry", "s 3 sad"))
            voice "ch2.6_s_050"
            s "Tch... I guess that's how it is."
            jump date_louise_ch2_7
