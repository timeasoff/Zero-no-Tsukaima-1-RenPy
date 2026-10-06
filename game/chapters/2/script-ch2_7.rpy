# Глава 2, часть 7 (сцены 1038–1046): ветки свиданий с Луизой,
# Сиестой и Табитой. Общего входного лейбла ch2_7 нет — файл
# открывается только через portrait_choice (script-ch2_6.rpy) или
# прямой jump; ветки 1045/1046 уходят в часть 8 (сцена 1048).
# Источник: ps2_source/chapters/chapter_03_黒髪の来訪者.txt
# Точные аргументы: ps2_source/events_full/chapter_03_黒髪の来訪者.txt

label date_louise_ch2_7:
    # ==== SCENE 1038 ====
    $ fade_fx("id(208)", type="cg")
    voice "ch2.7_l_001"
    l "Anyway! I'm going to drink. Just watch me!"
    voice "ch2.7_l_002"
    l "You'll see! I'll grow so big that Kirche and Siesta won't even reach my feet!"
    th "Whew... Louise has it rough too, in her own way. I really do admire that grit of hers."
    voice "ch2.7_s_001"
    s "Sure, but don't drink too much and upset your stomach, okay?"
    voice "ch2.7_l_003"
    l "No! Once I've made up my mind, the only way is forward!"
    voice "ch2.7_l_004"
    l "Even if I collapse, it'll be face-first! That's how the House of Vallière lives!"
    th "She's turned it into a whole life creed... come on."
    stop music fadeout 1.0
    $ pause(1.0)
    return

label date_siesta_ch2_7:
    # ==== SCENE 1039 ====
    $ fade_fx("dining_hall", new_music="t6", sprites=("si 1",))
    $ update_sympathy(20, char_key="siesta")
    voice "ch2.7_si_001"
    si "Ah, good morning, Saito-san."
    $ show_sprites(("si 1", "s 1"))
    voice "ch2.7_s_002"
    s "Hey, Siesta. So you're here."
    voice "ch2.7_s_003"
    s "Busy with work today?"
    voice "ch2.7_si_002"
    si "No. I have the day off, so I thought I'd try my hand at baking sweets."
    $ show_sprites(("si 1", "s 3"))
    voice "ch2.7_s_004"
    s "Heh, that sounds like you. So, what are you making?"
    voice "ch2.7_si_003"
    si "I was thinking of making cookies today."
    $ show_sprites(("si 1", "s 3 happy"))
    voice "ch2.7_s_005"
    s "Cookies, huh. Yeah, yeah - fresh out of the oven they smell great and taste even better."
    $ show_sprites(("si 1 happy", "s 3 happy"))
    voice "ch2.7_si_004"
    si "Oh, that's right. Saito-san, why don't you make cookies with me?"
    $ show_sprites(("si 1 happy", "s 1"))
    voice "ch2.7_s_006"
    s "Huh? Me too?"
    voice "ch2.7_si_005"
    si "Yes. It's sure to be fun."
    voice "ch2.7_s_007"
    s "Well, I guess..."
    menu:
        "Nah, I'll pass.{#ch2.7_m1039a}":
            jump ch2_7_siesta_refuse
        "Sounds like fun - let's do it.{#ch2.7_m1039b}":
            jump ch2_7_siesta_join
        "I'll be in charge of tasting.{#ch2.7_m1039c}":
            jump ch2_7_siesta_taste

label ch2_7_siesta_refuse:
    # ==== SCENE 1040 ====
    $ fade_fx("dining_hall", sprites=("si 1 happy", "s 3"))
    voice "ch2.7_s_008"
    s "Nah, I'll pass."
    $ show_sprites(("si 1 sad", "s 3"))
    voice "ch2.7_si_006"
    si "Is that... no good?"
    $ update_sympathy(-10, char_key="siesta")
    $ show_sprites(("si 1 sad", "s 3 sad"))
    voice "ch2.7_s_009"
    s "I appreciate the offer, but I'd only get in your way, Siesta."
    $ show_sprites(("si 4 shy", "s 3 sad"))
    voice "ch2.7_si_007"
    si "Ah, um, it's not as if I could make anything that special - and Saito-san, you can do things too, you know."
    $ show_sprites(("si 4 shy", "s 3 happy"))
    voice "ch2.7_s_010"
    s "Hmm... you've got a point. Alright, let's give it a try."
    $ show_sprites(("si 1 shy", "s 3 happy"))
    voice "ch2.7_si_008"
    si "That's right. Let's do it together."
    jump ch2_7_siesta_kitchen

label ch2_7_siesta_join:
    # ==== SCENE 1041 ====
    $ fade_fx("dining_hall", sprites=("si 1 happy", "s 3 happy"))
    voice "ch2.7_s_011"
    s "Sounds like fun - let's do it."
    $ show_sprites(("si 1 shy", "s 3 happy"))
    voice "ch2.7_si_009"
    si "Really?!"
    $ update_sympathy(10, char_key="siesta")
    voice "ch2.7_s_012"
    s "Well, I don't know a thing about cooking, so I might just be dead weight."
    voice "ch2.7_si_010"
    si "Not at all. Let's do our best together, okay?"
    $ show_sprites(("si 1 shy", "s 1 happy"))
    voice "ch2.7_s_013"
    s "Yeah.{#ch2.7_s_013}"
    jump ch2_7_siesta_kitchen

label ch2_7_siesta_taste:
    # ==== SCENE 1042 ====
    $ fade_fx("dining_hall", sprites=("si 1 happy", "s 3 sad"))
    voice "ch2.7_s_014"
    s "Er... I'll be in charge of tasting, then."
    $ show_sprites(("si 1 sad", "s 3 sad"))
    voice "ch2.7_si_011"
    si "Is that so...? What a shame."
    $ show_sprites(("si 4 sad", "s 3 sad"))
    voice "ch2.7_si_012"
    si "And here I thought Saito-san and I could make cookies together..."
    $ show_sprites(("si 4 sad", "s 3 happy"))
    voice "ch2.7_s_015"
    s "N-no, I mean, I'm terrible at cooking and all..."
    voice "ch2.7_si_013"
    si "Tug, tug..."
    $ show_sprites(("si 4 sad", "s 3 sad"))
    voice "ch2.7_s_016"
    s "...{#ch2.7_s_016}"
    voice "ch2.7_si_014"
    si "Tug, tug...{#ch2.7_si_014}"
    $ show_sprites(("si 4 sad", "s 1"))
    voice "ch2.7_s_017"
    s "Alright. I'll help out too."
    $ show_sprites(("si 4 shy", "s 1"))
    voice "ch2.7_si_015"
    si "Really? Then let's do it together!"
    $ show_sprites(("si 4 shy", "s 1 sad"))
    th "Dammit - did Siesta just set me up?"
    jump ch2_7_siesta_kitchen

label ch2_7_siesta_kitchen:
    # ==== SCENE 1043 ====
    $ fade_fx("kitchen", sprites=("si 1 happy", "s 1"))
    voice "ch2.7_si_016"
    si "Then please knead this butter until it's soft and paste-like. I'll get the flour ready in the meantime."
    voice "ch2.7_s_018"
    s "Mm, got it."
    $ show_sprites(("s 1",))
    voice "ch2.7_s_019"
    s "...Mmf. This is harder than it looks."
    $ show_sprites(("si 1 happy", "s 1"))
    voice "ch2.7_si_017"
    si "Is it done?"
    $ show_sprites(("si 1 happy", "s 3 happy"))
    voice "ch2.7_s_020"
    s "Ah, yeah. Sort of."
    voice "ch2.7_si_018"
    si "Next, add the sugar and egg yolk, and stir well again."
    voice "ch2.7_si_019"
    si "Sugar in first - and once it's mixed well, then the yolk."
    $ show_sprites(("si 1 happy", "s 3"))
    voice "ch2.7_s_021"
    s "Roger!"
    $ show_sprites(("s 1",))
    th "Even unbaked, it already smells pretty good."
    $ show_sprites(("si 1 happy", "s 1"))
    voice "ch2.7_si_020"
    si "How is it?"
    voice "ch2.7_s_022"
    s "I think I stirred it."
    voice "ch2.7_si_021"
    si "Let's see, let's see."
    voice "ch2.7_si_022"
    si "...Yep, this should be fine."
    voice "ch2.7_si_023"
    si "Then I'll fold in the flour and mix."
    voice "ch2.7_s_023"
    s "Sure, thanks."
    voice "ch2.7_si_024"
    si "Alright."
    th "Mm-mm-mm. How quick and deft she is."
    voice "ch2.7_si_025"
    si "Now I'll lay out the dough... and put it in the oven..."
    voice "ch2.7_si_026"
    si "Now we just wait for it to bake right."
    $ show_sprites(("si 1 happy", "s 1 happy"))
    voice "ch2.7_s_024"
    s "I can't wait for them to be done."
    voice "ch2.7_si_027"
    si "Yes.{#ch2.7_si_027}"
    $ show_sprites(("si 1",))
    voice "ch2.7_si_028"
    si "I wonder if they're about ready."
    voice "ch2.7_si_029"
    si "Let's see... Yep! Looking good."
    $ show_sprites(("si 1", "s 1 happy"))
    voice "ch2.7_s_025"
    s "Let me see... Huh... smells great."
    voice "ch2.7_si_030"
    si "Saito-san, go ahead and have a taste."
    voice "ch2.7_s_026"
    s "Then I won't hold back."
    $ show_sprites(("si 1", "s 3 happy"))
    voice "ch2.7_s_027"
    s "Mm! This is delicious! As expected of Siesta - they're great."
    $ show_sprites(("si 4 shy", "s 3 happy"))
    voice "ch2.7_si_031"
    si "Thank you... I'm sure it's because you were here, Saito-san."
    $ show_sprites(("si 4 shy", "s 3 shy"))
    voice "ch2.7_s_028"
    s "Nah, in the end I didn't actually do anything useful. But these cookies really are good."
    voice "ch2.7_si_032"
    si "Fufu, eat as much as you like."
    voice "ch2.7_s_029"
    s "It'd be a waste for me to eat them all. Let's share, Siesta."
    voice "ch2.7_si_033"
    si "Ah, yes!"
    stop music fadeout 1.0
    $ pause(1.0)
    return

label date_tabitha_ch2_7:
    # ==== SCENE 1044 ====
    $ fade_fx("hallway", new_music="t8", sprites=("t 1", "s 3 happy"))
    voice "ch2.7_s_030"
    s "Hey, Tabitha - it's nice out today. Want to go somewhere for once?"
    $ update_sympathy(30, char_key="tabitha")
    voice "ch2.7_t_001"
    t "...Already on my schedule."
    $ show_sprites(("t 1", "s 3 angry"))
    voice "ch2.7_s_031"
    s "...Whaat?! Tabitha is going outside!?"
    $ show_sprites(("t 1 angry", "s 3 angry"))
    th "...{#ch2.7_th1044a}"
    $ show_sprites(("t 1 angry", "s 3 sad"))
    voice "ch2.7_s_032"
    s "Ah, no - I'm not saying it's weird to go out. It's just, I came to invite you and you beat me to it..."
    $ show_sprites(("t 1 angry", "s 3"))
    voice "ch2.7_s_033"
    s "Ah, whatever. So, where are you headed? I can come along, if you want."
    $ show_sprites(("t 1", "s 3"))
    voice "ch2.7_t_002"
    t "...To town, to buy books."
    $ show_sprites(("t 1", "s 1"))
    voice "ch2.7_s_034"
    s "Oh... sorry, that makes perfect sense."
    voice "ch2.7_t_003"
    t "...So I can't come along today."
    $ show_sprites(("t 1", "s 3 happy"))
    voice "ch2.7_s_035"
    s "Hahaha. Come on, in that case I'll at least carry your bags."
    voice "ch2.7_t_004"
    t "...You don't mind?"
    voice "ch2.7_s_036"
    s "Of course, it's nothing."
    voice "ch2.7_t_005"
    t "...They'll get pretty heavy, though."
    $ show_sprites(("t 1", "s 3 sad"))
    voice "ch2.7_s_037"
    s "Er... how heavy?"
    voice "ch2.7_t_006"
    t "...Usually I only buy what fits in my bag."
    $ show_sprites(("t 1", "s 3 happy"))
    voice "ch2.7_s_038"
    s "Oh, I can handle that much. Don't worry, leeeave it to me."
    voice "ch2.7_t_007"
    t "...Alright. Please."
    voice "ch2.7_s_039"
    s "Roger, roger."
    $ fade_fx("town", sprites=("t 1", "s 1"))
    voice "ch2.7_s_040"
    s "Phew, as lively as ever. So, which way is the bookstore?"
    voice "ch2.7_t_008"
    t "...This way."
    voice "ch2.7_s_041"
    s "Okay. Let's go."
    $ fade_fx("cafe_entrance", sprites=("t 1", "s 1"))
    voice "ch2.7_t_009"
    t "...Just around this corner."
    voice "ch2.7_s_042"
    s "Let's see."
    voice "ch2.7_s_043"
    s "This one here - the shop with the sign out front?"
    voice "ch2.7_t_010"
    t "...Sign?"
    $ show_sprites(("t 1", "s 1 sad"))
    voice "ch2.7_s_044"
    s "Something's written on it. I can't read it, though."
    th "...{#ch2.7_th1044b}"
    $ show_sprites(("t 1", "s 1"))
    voice "ch2.7_s_045"
    s "What does it say?"
    $ show_sprites(("t 1 sad", "s 1"))
    voice "ch2.7_t_011"
    t "...'Closed today.'"
    $ show_sprites(("t 1 sad", "s 1 sad"))
    voice "ch2.7_s_046"
    s "...Huh?{#ch2.7_s_046}"
    voice "ch2.7_t_012"
    t "...The shop is closed."
    voice "ch2.7_s_047"
    s "Great. Talk about bad luck."
    th "...{#ch2.7_th1044c}"
    th "Wow, Tabitha is so disappointed it's obvious just to look at. She must have been looking forward to it a lot."
    menu:
        "Such days happen.{#ch2.7_m1044a}":
            jump ch2_7_tabitha_1045
        "I'll buy you something.{#ch2.7_m1044b}":
            jump ch2_7_tabitha_1046
        "Let's see more than just the bookstore.{#ch2.7_m1044c}":
            jump ch2_8_tabitha_1047

label ch2_7_tabitha_1045:
    # ==== SCENE 1045 ====
    $ fade_fx("cafe_entrance", sprites=("t 1 sad", "s 3"))
    voice "ch2.7_s_048"
    s "Days like this happen."
    th "...{#ch2.7_th1045a}"
    voice "ch2.7_s_049"
    s "Come on, it's not like today's the only day you can buy books. You can just come again next time."
    voice "ch2.7_t_013"
    t "...There's no guarantee the book I want will still be in stock by next time."
    $ show_sprites(("t 1 sad", "s 3 sad"))
    voice "ch2.7_s_050"
    s "Oof. Fair point, but..."
    voice "ch2.7_s_051"
    s "...{#ch2.7_s_051}"
    th "...{#ch2.7_th1045}"
    $ show_sprites(("t 1 sad", "s 1"))
    voice "ch2.7_s_052"
    s "Ah, tell you what - next time I'll sneak out on your errand. Tell me the title and I'll buy it for you."
    $ show_sprites(("t 1", "s 1"))
    voice "ch2.7_t_014"
    t "...Are you sure?"
    voice "ch2.7_s_053"
    s "Ah, yeah. I'll manage somehow."
    $ show_sprites(("t 1 happy", "s 1"))
    voice "ch2.7_t_015"
    t "...Thanks."
    jump ch2_8_tabitha_1048

label ch2_7_tabitha_1046:
    # ==== SCENE 1046 ====
    $ fade_fx("cafe_entrance", sprites=("t 1 sad", "s 3 happy"))
    voice "ch2.7_s_054"
    s "I'll buy you something."
    $ show_sprites(("t 1", "s 3 happy"))
    voice "ch2.7_t_016"
    t "...Huh?{#ch2.7_t_016}"
    voice "ch2.7_s_055"
    s "Er, well, it's such nice weather and your throat must be dry, right?"
    voice "ch2.7_s_056"
    s "That stall over there sells juice, so I'll go grab some."
    $ show_sprites(("t 1 sad",))
    voice "ch2.7_t_017"
    t "Ah...{#ch2.7_t_017}"
    $ fade_fx("town", sprites=("t 1", "s 3"))
    voice "ch2.7_s_057"
    s "Here, sorry to keep you waiting. This one's yours, Tabitha."
    th "...{#ch2.7_th1046a}"
    $ show_sprites(("t 1", "s 3 sad"))
    voice "ch2.7_s_058"
    s "Oh - come to think of it, what juice is this? I couldn't read the menu so I just grabbed something, hope it's fine."
    voice "ch2.7_t_018"
    t "...That's wild grape juice."
    $ show_sprites(("t 1", "s 3"))
    voice "ch2.7_s_059"
    s "Wild grapes, huh. Oh, and what's yours?"
    voice "ch2.7_t_019"
    t "...This one is mountain cranberry juice."
    voice "ch2.7_s_060"
    s "Huh... I have no idea what mountain cranberries are, but... oh well, dig in!"
    $ show_sprites(("t 1", "s 3 happy"))
    voice "ch2.7_s_061"
    s "Pfft - sour, but good."
    stop music fadeout 1.0
    play music t14 fadein 1.0
    $ show_sprites(("t 1 happy", "s 3 happy"))
    th "...{#ch2.7_th1046b}"
    $ update_sympathy(15, char_key="tabitha")
    $ show_sprites(("t 1 happy", "s 1"))
    voice "ch2.7_s_062"
    s "Hmm? What's wrong?"
    $ show_sprites(("t 1 shy", "s 1"))
    voice "ch2.7_t_020"
    t "...Nothing."
    # Сц. 1048 в источнике начинается с play=+9 (t8); после смены на t14
    # в ветке 1046 возвращаем t8 (на ветках 1045/1047 t8 уже звучит).
    stop music fadeout 1.0
    play music t8 fadein 1.0
    jump ch2_8_tabitha_1048

