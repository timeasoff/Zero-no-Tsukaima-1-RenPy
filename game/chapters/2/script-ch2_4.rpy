# Глава 2, часть 4 (сцены 99–114): побег бомбиста, поиск по академии,
# возвращение в комнату, ужин и ссора Луизы с Харуной.
# Источник: ps2_source/chapters/chapter_03_黒髪の来訪者.txt (scene 0099…0114)
# Точные аргументы: ps2_source/events_full/chapter_03_黒髪の来訪者.txt (SCENE 0099…0114)

# Посещённые локации (【移動】, сцена 100): убираются из карты после визита.
default ch2_4_visited = set()

label ch2_4:
    # ==== SCENE 99 ====
    # Взрыв: бомбист скрывается; белая вспышка, CG 100 (появление) → CG 101 (небо)
    $ scene_fx(("blow", "flash"), None, duration=(0.7, 0.5), stop_music=True, new_music="t17")
    $ fade_fx("ak_appear", type="cg", duration=1.0, window_hide=False)
    $ fade_fx("ak_sky", type="cg", duration=1.0, window_hide=False)
    $ fade_fx("yard", new_music="t26", sprites="s 4 angry")

    voice "ch2.4_s_001"
    s "Damn it! The bomb user got away...!? Nowhere in sight."

    voice "ch2.4_d_001"
    d "Partner, it's not just the bomb user. Take a look around."

    voice "ch2.4_s_002"
    s "Huh... Aah! Those guys have vanished too!?"

    $ show_sprites(("k 1 angry", "l 3 angry"))
    voice "ch2.4_k_001"
    k "Whaaat? When did they...!"

    voice "ch2.4_l_001"
    l "They slipped away in that explosion? Then that bomb user really was their accomplice?"

    $ show_sprites(("k 1 sad", "l 3 angry"))
    voice "ch2.4_k_002"
    k "That's very likely. Someone curious enough to sneak into the academy — a chance encounter would be too convenient."

    $ show_sprites("c 1 sad")
    voice "ch2.4_c_001"
    c "But that explosion — what in the world...?"

    $ show_sprites(("c 1 sad", "s 2 sad"))
    voice "ch2.4_s_003"
    s "Professor? What is it?"

    $ show_sprites(("c 1", "s 2 sad"))
    voice "ch2.4_c_002"
    c "Ah, no, there's just something bothering me... More importantly, I'll report this to the academy. You all go back to the classroom."

    $ show_sprites(("l 1", "s 2 sad"))
    voice "ch2.4_l_002"
    l "Understood, Professor Colbert."

    $ show_sprites(("k 4 sad", "s 2 sad"))
    voice "ch2.4_k_003"
    k "I'm not satisfied at all. It's like I didn't get to burn enough..."

    $ show_sprites(("k 4 sad", "s 4"))
    voice "ch2.4_s_004"
    s "Incomplete combustion, you mean?"

    $ show_sprites(("k 4 happy", "s 4"))
    voice "ch2.4_k_004"
    k "Ah, yeah, that's it. As expected of you, darling — so perceptive."

    $ show_sprites(("l 3 angry", "s 4"))
    voice "ch2.4_l_003"
    l "...Why is that the only thing you ever notice?"

    $ show_sprites(("s 2", "l 3 angry"))
    voice "ch2.4_s_005"
    s "Hm? Did you say something?"

    $ show_sprites(("s 2", "l 1 angry"))
    voice "ch2.4_l_004"
    l "Nothing at all! Come on, let's head back already!"

    # ==== SCENE 100 ====
    $ fade_fx("yard_evening", new_music="t18")

    th "In the end, we didn't find a single clue about the intruders."
    th "The ease with which the academy was infiltrated seems to be an issue — the teachers have started a meeting."
    th "So we're left not knowing the details after all. I just can't feel at ease."
    th "More than that, I'm bothered by how persistently those guys were after Haruna... I doubt they've given up after today."

    $ fade_fx("hallway_evening", sprites=("l 3 sad", "s 1 sad"))
    voice "ch2.4_l_005"
    l "Saito? What's wrong, going all quiet like that?"

    th "And if that bomb user comes back again, it won't be a joke."

    $ show_sprites(("l 1", "s 1 sad"))
    voice "ch2.4_l_006"
    l "Saito, I said answer me. Is something on your mind?"

    $ show_sprites(("l 1", "s 1"))
    voice "ch2.4_s_006"
    s "Louise."

    voice "ch2.4_l_007"
    l "Wh-what?"

    voice "ch2.4_s_007"
    s "I'm going to take a quick look around the academy."

    $ show_sprites(("l 3 angry", "s 1"))
    voice "ch2.4_l_008"
    l "What!? Wait, a patrol, what?"

    $ fade_fx("hallway_down_evening", sprites="s 1")
    th "Now then. Even if I patrol, where should I start?"

    # Выбор локации (【移動】, сцена 100): карта-цикл. Контент локаций —
    # в script-ch2_4b.rpy (廊下/厨房) и script-ch2_4c.rpy (中庭/教室/ルイズの部屋),
    # сцены 1256–1280. После визита локация убирается из карты;
    # «Leave» → сцена 106 (ch2_4_room).
    jump ch2_4_map
    return

label ch2_4_map:
    $ choices = []
    if "hallway" not in ch2_4_visited:
        $ choices.append({"char": "louise", "text": "Hallway{#ch2.4_hallway}", "target": "hallway_ch2_4"})
    if "kitchen" not in ch2_4_visited:
        $ choices.append({"char": "siesta", "text": "Kitchen", "target": "kitchen_ch2_4"})
    if "yard" not in ch2_4_visited:
        $ choices.append({"char": "kirche", "text": "Courtyard", "target": "yard_ch2_4"})
    if "classroom" not in ch2_4_visited:
        $ choices.append({"text": "Classroom", "target": "classroom_ch2_4"})
    if "l_room" not in ch2_4_visited:
        $ choices.append({"char": "haruna", "text": "Louise's Room{#ch2.4_lroom}", "target": "l_room_ch2_4"})
    $ choices.append({"text": "Leave", "target": "ch2_4_leave"})
    $ sprite_choice(choices)
    jump ch2_4_map
    return

label ch2_4_leave:
    jump ch2_4_room

label ch2_4_room:
    # ==== SCENE 106 ====
    $ fade_fx("sky_night")
    $ fade_fx("yard_night", new_music="t19")

    voice "ch2.4_s_008"
    s "Man, it's already this late. It's already deep into the night."

    voice "ch2.4_d_002"
    d "Partner, let's call it a day. Doesn't look like anyone's hiding in the academy."

    voice "ch2.4_s_009"
    s "Yeah. Well then, let's head back to the room."

    # дверь: Сайто возвращается в комнату (SE +57 → open_door, +56 → close_door)
    stop music fadeout 1.0
    call open_door("left", "louise_room_night") from _call_open_door_8
    play music t3 fadein 1.0
    $ show_sprites("s 1")

    voice "ch2.4_s_010"
    s "I'm home."

    $ show_sprites(("l 1", "s 1"))
    voice "ch2.4_l_009"
    l "So you're back."

    $ show_sprites(("si 1", "s 1"))
    voice "ch2.4_si_001"
    si "Good work, Saito-san. Weren't you in any danger?"

    $ show_sprites(("ha 3", "s 1"))
    voice "ch2.4_ha_001"
    ha "Welcome back. How was the patrol?"

    th "Ah... having girls welcome me home can make me feel this happy."

    $ show_sprites(("l 1 sad", "s 1"))
    voice "ch2.4_s_011"
    s "Yeah. I looked around the academy all afternoon, but there was nothing unusual anywhere."

    $ show_sprites(("l 1 sad", "s 1 sad"))
    voice "ch2.4_l_010"
    l "Hmm...{#ch2.4_l_010}"

    voice "ch2.4_s_012"
    s "And that's a reply completely devoid of interest."

    voice "ch2.4_l_011"
    l "Isn't it fine, everyone was safe. It's no more and no less than that."

    voice "ch2.4_s_013"
    s "Well, if you put it that way, you're right."

    $ show_sprites(("d 1", "l 1 sad", "s 1 sad"))
    voice "ch2.4_d_003"
    d "Hey now! I don't think it'd hurt to say a kind word of appreciation or at least one, I say."

    $ show_sprites(("l 1", "s 1 sad"))
    voice "ch2.4_l_012"
    l "Yes, yes. Good work."

    voice "ch2.4_s_014"
    s "......{#ch2.4_s_014}"

    voice "ch2.4_l_013"
    l "......{#ch2.4_l_013}"

    $ show_sprites(("si 1", "s 1 sad"))
    voice "ch2.4_si_002"
    si "U-um, Miss Vallière seems tired, so..."

    th "I-is that so?"

    menu:
        "Did something happen, Louise?{#ch2.4_m106a}":
            # ==== SCENE 107 ====
            $ show_sprites(("l 1", "s 1 sad"))
            voice "ch2.4_s_015"
            s "Did something happen, Louise?{#ch2.4_s_015}"

            $ show_sprites(("l 1", "s 1 sad"))
            voice "ch2.4_l_014"
            l "Huh? What's this all of a sudden?"

            voice "ch2.4_s_016"
            s "Well, you seemed kind of absent-minded. I wondered if something was bothering you."

            $ show_sprites(("l 3 angry", "s 1 sad"))
            voice "ch2.4_l_015"
            l "N-nothing in particular."

            voice "ch2.4_s_017"
            s "Is that so? Hmm... then I guess it's fine."

            $ show_sprites(("l 1", "s 1 sad"))
            voice "ch2.4_l_016"
            l "...Really, it's nothing. There's no need to worry."

            $ update_sympathy(10, char_key="louise")

            $ show_sprites(("l 1", "s 1"))
            voice "ch2.4_s_018"
            s "Hmm. If you say so, I suppose it's fine, but don't push yourself too hard."

            voice "ch2.4_l_017"
            l "I'm not. ...Honestly."

            jump ch2_4_dinner

        "Did something happen, Siesta?{#ch2.4_m106b}":
            # ==== SCENE 108 ====
            $ show_sprites(("si 1 sad", "s 1 sad"))
            voice "ch2.4_s_019"
            s "Did something happen, Siesta?{#ch2.4_s_019}"

            voice "ch2.4_si_003"
            si "Huh, me...?"

            voice "ch2.4_s_020"
            s "Well, you looked kind of scared to ask Louise anything, so..."

            $ update_sympathy(-10, char_key="siesta")

            $ show_sprites(("si 4 sad", "s 1 sad"))
            voice "ch2.4_si_004"
            si "......{#ch2.4_si_004}"

            jump ch2_4_dinner

        "How are you feeling, Haruna?{#ch2.4_m106c}":
            # ==== SCENE 109 ====
            $ show_sprites(("s 1", "si 1"))
            voice "ch2.4_s_021"
            s "How are you feeling, Haruna?{#ch2.4_s_021}"

            $ fade_fx("ha_sick_3", type="cg")
            voice "ch2.4_ha_002"
            ha "Ah, yeah. Compared to this morning, I think I'm much better."

            $ update_sympathy(10, char_key="haruna")

            voice "ch2.4_s_022"
            s "That's a relief."

            voice "ch2.4_l_018"
            l "...Hmph.{#ch2.4_l_018}"

            $ update_sympathy(-10, char_key="louise")

            voice "ch2.4_ha_003"
            ha "I still feel a little sluggish, though... But I think I'm mostly okay now."

            voice "ch2.4_s_023"
            s "You'd better not overdo it. Rest properly until you're fully recovered."

            $ dissolve_fx("ha_sick_2", type="cg")
            voice "ch2.4_ha_004"
            ha "Thank you, Hiraga-kun.{#ch2.4_ha_004}"

            $ fade_fx("louise_room_night", sprites=("s 1", "si 1 sad"))
            jump ch2_4_dinner

label ch2_4_dinner:
    # ==== SCENE 110 ====
    $ show_sprites(("si 1 sad", "s 1"))
    voice "ch2.4_s_024"
    s "Oh, right. Siesta, is there anything to eat?"

    voice "ch2.4_si_005"
    si "Huh? Don't tell me you haven't had dinner yet?"

    voice "ch2.4_s_025"
    s "Yeah. I was patrolling and missed my chance to eat. I'd appreciate it if there's anything."

    $ show_sprites(("si 1", "s 1"))
    voice "ch2.4_si_006"
    si "If you'd told me, I would have prepared something. Let me bring it now."

    $ show_sprites(("si 1", "s 3"))
    voice "ch2.4_s_026"
    s "I feel kind of bad about this."

    $ show_sprites(("si 1 happy", "s 3"))
    voice "ch2.4_si_007"
    si "This much is nothing. Well then, I'll go to the kitchen and get your meal."

    $ show_sprites("s 1")
    voice "ch2.4_s_027"
    s "By the way, Haruna, have you had dinner?"

    $ fade_fx("ha_sick_3", type="cg")
    voice "ch2.4_ha_005"
    ha "Yeah... I didn't have an appetite, so not yet. But if you're with me, Hiraga-kun, I might be able to eat."

    $ fade_fx("louise_room_night", sprites=("l 3 angry", "s 1"))
    voice "ch2.4_l_019"
    l "Kuh!? What is that?"

    $ show_sprites(("l 1 angry", "s 1"))
    voice "ch2.4_l_020"
    l "You're spoiling her quite a lot. She can eat a meal by herself, can't she?"

    $ show_sprites(("l 1 angry", "s 3 sad"))
    voice "ch2.4_s_028"
    s "Louise, calm down. Eating alone when you're laid up in bed makes you feel incredibly lonely, doesn't it?"

    voice "ch2.4_s_029"
    s "Not just the body, the heart needs to get better too. Besides, I'm hungry as well, so we might as well — eating together isn't strange at all, is it?"

    voice "ch2.4_l_021"
    l "It is strange."

    $ show_sprites(("l 1 angry", "s 1 angry"))
    voice "ch2.4_s_030"
    s "How is it!?"

    voice "ch2.4_l_022"
    l "You've never shown such attentive behavior up until now, have you?"

    voice "ch2.4_l_023"
    l "And yet you're being kind to that girl. You'd think that's odd, wouldn't you?"

    $ show_sprites(("l 1 angry", "s 1 sad"))
    voice "ch2.4_s_031"
    s "Well, even if you say that... Haruna is from the same world as me, and she's sick. What's wrong with being kind to her?"

    $ show_sprites(("l 3 sad", "s 1 sad"))
    voice "ch2.4_l_024"
    l "That's..."

    play sound open_door
    $ show_sprites(("si 1", "s 1 happy"))
    voice "ch2.4_si_008"
    si "I brought your dinner. The soup is a little lukewarm, though..."

    $ show_sprites(("l 1", "s 1 happy"))
    voice "ch2.4_s_032"
    s "Ah, Siesta, thank you."

    $ show_sprites(("l 1", "s 1 happy"))
    voice "ch2.4_l_025"
    l "...Hmph.{#ch2.4_l_025}"

    $ fade_fx("ha_sick_3", type="cg")
    voice "ch2.4_ha_006"
    ha "Sorry, Siesta-san."

    voice "ch2.4_si_009"
    si "No, no. I'm used to preparing meals for you, Saito-san."

    voice "ch2.4_ha_007"
    ha "Oh my, is that so?"

    voice "ch2.4_si_010"
    si "Yes, that's right."

    th "...It should be a warm atmosphere, but somehow the air feels strangely heavy."

    voice "ch2.4_ha_008"
    ha "Well then, thank you for the meal."

    voice "ch2.4_s_033"
    s "Yeah, don't push yourself."

    voice "ch2.4_ha_009"
    ha "No, this much is fine."

    voice "ch2.4_s_034"
    s "Still, though... Then, shall I feed you? Here, say ahh."

    $ dissolve_fx("ha_sick_2", type="cg", stop_music=True)
    voice "ch2.4_ha_010"
    ha "Eh..."

    voice "ch2.4_si_011"
    si "...!?"

    $ fade_fx("louise_room_night", new_music="t29", sprites="l 3 angry")
    voice "ch2.4_l_026"
    l "W-wait a minute!? Saito! What do you think you're doing!?"

    $ show_sprites(("l 3 angry", "s 3 sad"))
    voice "ch2.4_s_035"
    s "What do you mean — dinner."

    voice "ch2.4_l_027"
    l "That's not what I mean! What's with that 'ahh'!?"

    voice "ch2.4_s_036"
    s "Huh? Is something weird?"

    $ show_sprites(("l 3 angry", "s 3 sad"))
    voice "ch2.4_l_028"
    l "I'm telling you, it's weird!"

    $ fade_fx("ha_sick_2", type="cg")
    voice "ch2.4_ha_011"
    ha "Hiraga-kun, you're so kind..."

    $ fade_fx("louise_room_night", sprites=("l 3 angry", "s 1 sad"))
    voice "ch2.4_l_029"
    l "What's with that clingy, spoiling attitude!? You've never once shown me anything like that!"

    $ show_sprites(("l 3 angry", "s 1 sad"))
    voice "ch2.4_s_037"
    s "But you're always perfectly fine, aren't you?"

    $ show_sprites(("si 4 sad", "s 1 sad"))
    voice "ch2.4_si_012"
    si "Um, I don't think that's really the issue..."

    $ show_sprites("s 1 sad")
    voice "ch2.4_s_038"
    s "Um, Louise?"

    menu:
        "Do you want dinner too?{#ch2.4_m110a}":
            # ==== SCENE 111 ====
            $ show_sprites(("l 3 angry", "s 1"))
            voice "ch2.4_s_039"
            s "Do you want dinner too?{#ch2.4_s_039}"

            voice "ch2.4_l_030"
            l "Hah!? Why would it come to that!?"

            $ show_sprites(("l 3 angry", "s 3 sad"))
            voice "ch2.4_s_040"
            s "Well, you've been irritated this whole time. I thought you'd already had dinner, but maybe you're hungry and that's making you quick to anger."

            voice "ch2.4_l_031"
            l "I finished dinner long ago!"

            voice "ch2.4_s_041"
            s "Is that so? But if you're this irritated, then... are you on a diet or something?"

            $ show_sprites(("l 1 sad", "s 3 sad"))
            voice "ch2.4_l_032"
            l "Hah? A diet?"

            voice "ch2.4_s_042"
            s "You should stop."

            voice "ch2.4_s_043"
            s "Skipping meals by force will only ruin your health and have a bad effect on your mental stability — nothing good comes of it."

            $ show_sprites(("l 1 angry", "s 3 sad"))
            voice "ch2.4_l_033"
            l "Wrooong! I'm not doing that!"

            $ show_sprites(("l 1 angry", "s 3"))
            voice "ch2.4_s_044"
            s "Then that's fine. Besides, you're plenty attractive as you are, so if you did something unnecessary and rebounded, that'd be a disaster."

            $ show_sprites(("l 1 sad", "s 3"))
            voice "ch2.4_l_034"
            l "Um... I'm telling you, what are we even talking about?"

            jump ch2_4_after

        "Do you want me to say 'ahh' for you too?{#ch2.4_m110b}":
            # ==== SCENE 112 ====
            $ show_sprites(("l 1 shy", "s 3 happy"))
            voice "ch2.4_s_045"
            s "Do you want me to say 'ahh' for you too?{#ch2.4_s_045}"

            voice "ch2.4_l_035"
            l "Hah!? Wh-wh-why would it come to that!?"

            $ update_sympathy(10, char_key="louise")

            $ show_sprites(("l 1 shy", "s 1"))
            voice "ch2.4_s_046"
            s "Ah, so that's not it. You just seemed fixated on that."

            $ show_sprites(("l 3 shy", "s 1"))
            voice "ch2.4_l_036"
            l "That and this are different things! Why would I have to have you feed me?!"

            $ show_sprites(("l 1", "s 1"))
            voice "ch2.4_s_047"
            s "Yeah, you're right. I think so too."

            voice "ch2.4_l_037"
            l "...As long as you understand."

            jump ch2_4_after

        "Do you want to be laid up in bed too?{#ch2.4_m110c}":
            # ==== SCENE 113 ====
            $ show_sprites(("l 1 angry", "s 3 sad"))
            voice "ch2.4_s_048"
            s "Do you want to be laid up in bed too?{#ch2.4_s_048}"

            voice "ch2.4_l_038"
            l "Hah!? Why would it come to that!?{#ch2.4_l_038}"

            $ update_sympathy(-10, char_key="louise")

            voice "ch2.4_s_049"
            s "Well, you've been irritated this whole time. I thought maybe you wanted to stay in bed too, that's all."

            $ show_sprites(("l 1 sad", "s 3 sad"))
            voice "ch2.4_l_039"
            l "...It's true that talking with you gives me a headache. But I'm not going to fake being sick just to stay in bed."

            $ fade_fx("ha_sick_3", type="cg")
            voice "ch2.4_ha_012"
            ha "...Oh, is that so?"

            $ fade_fx("louise_room_night", sprites=("l 1 sad", "s 1"))
            voice "ch2.4_l_040"
            l "That's right. Me, of all people."

            jump ch2_4_after

label ch2_4_after:
    # ==== SCENE 114 ====
    $ show_sprites(("l 1 sad", "s 3"))
    voice "ch2.4_s_050"
    s "There's no weird meaning behind it, okay? Haruna is sick, so looking after her is only normal, right?"

    $ show_sprites(("l 1 angry", "s 3"))
    voice "ch2.4_l_041"
    l "So if she's sick, you'll do anything for her?"

    $ show_sprites(("l 1 angry", "s 3 sad"))
    voice "ch2.4_s_051"
    s "I'm not going that far. Why are you getting angry about me looking after a sick person?"

    $ show_sprites(("l 3 sad", "s 3 sad"))
    voice "ch2.4_l_042"
    l "...B-because!"

    $ fade_fx("ha_sick_3", type="cg")
    voice "ch2.4_ha_013"
    ha "Please, that's enough."

    voice "ch2.4_l_043"
    l "!!{#ch2.4_l_043}"

    voice "ch2.4_s_052"
    s "Haruna..."

    voice "ch2.4_ha_014"
    ha "Hiraga-kun is not Miss Louise's tool. You of all people should know that, shouldn't you?"

    $ fade_fx("louise_room_night", sprites=("l 3 angry",))
    voice "ch2.4_l_044"
    l "I... I have no reason to be told that by you!"

    voice "ch2.4_l_045"
    l "And what's more! Sick, sick, sick — is being sick really so great? I don't care about Saito anymore!"

    voice "ch2.4_s_053"
    s "Ah, hey, Louise!"

    $ show_sprites(("l 1 angry",))
    voice "ch2.4_l_046"
    l "Stupid dog! Stupid familiar! Stupid Saito!"

    $ show_sprites(("l 1 angry",))
    voice "ch2.4_l_047"
    l "Honestly, I don't care anymore!"

    # Луиза убегает: дверь (SE +57 → open_door, +58 → close_door) + тряска
    play sound open_door
    $ show_sprites(None)
    play sound close_door
    $ shake_fx(duration=0.4)

    $ fade_fx("black", stop_music=True)
    jump ch2_5
