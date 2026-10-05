# Глава 2, часть 3 (сцены 90–98): урок Кольбера, ссора Луизы и Кирхе,
# нападение бомбиста, бой, первое появление Акины.
# Источник: ps2_source/chapters/chapter_03_黒髪の来訪者.txt (scene 0090…0098)
# Точные аргументы: ps2_source/events_full/chapter_03_黒髪の来訪者.txt (SCENE 0090…0098)

label ch2_3:
    # ==== SCENE 90 ====
    $ fade_fx("classroom", sprites="c 1")

    voice "ch2.3_c_001"
    c "Now then, let's get back to our discussion."

    voice "ch2.3_c_002"
    c "The Fire element is thought to be the most aggressive of the four, but it isn't specialized for combat, nor is it especially strong."

    voice "ch2.3_c_003"
    c "It's true that among the four, Fire is the easiest to turn to attack — but between skilled wielders, there's no superiority among Fire, Water, Wind, and Earth."

    $ show_sprites(("c 1", "k 1"))
    voice "ch2.3_k_001"
    k "With all due respect, Professor Colbert. It's a fact that the Fire element is clearly superior to the other three."

    voice "ch2.3_c_004"
    c "Hmm, Miss Zerbst. I'm aware you take pride in your own element, but..."

    voice "ch2.3_c_005"
    c "Isn't that opinion a little extreme?"

    voice "ch2.3_k_002"
    k "My, but it's a fact. There are individual differences, so I won't say it's absolute..."

    voice "ch2.3_k_003"
    k "The element that can wield the most beautiful and most powerful magic is Fire."

    $ show_sprites(("c 1", "k 1 happy"))
    voice "ch2.3_k_004"
    k "Of course, that doesn't mean the other elements are ugly or weak. It's simply that Fire is the best."

    voice "ch2.3_k_005"
    k "But some people can't even get as far as having an element. Isn't that right, 'Louise the Zero'?"

    # Первый CG сцены — fade_fx (не dissolve): покрывающий переход сам убирает спрайты. В оригинале здесь fade
    $ fade_fx("l_k_fight", stop_music=True, new_music="t29", type="cg")
    voice "ch2.3_l_001"
    l "...It's been a while since I heard someone say something so stupid. I wonder who the fool could be?"

    voice "ch2.3_k_006"
    k "Oh? Magic, growth, and feminine charm — all of them zero. I wonder who that could be?"

    $ dissolve_fx("l_k_fight_2", type="cg")
    voice "ch2.3_l_002"
    l "Who's 'Zero'!? I gave back that disgraceful nickname long ago...!"

    th "That Louise — she's forgotten the Queen told her not to tell anyone about the 'Void'!"

    voice "ch2.3_s_001"
    s "Louise, shh, shh!"

    $ dissolve_fx("l_k_fight", type="cg")
    voice "ch2.3_l_003"
    l "Huh, what? ...Ah!"

    voice "ch2.3_k_007"
    k "What's wrong? You're making a strange face. Could you be preparing to run away?"

    voice "ch2.3_l_004"
    l "Fu... fu, fu, fu... This is just perfect. I've been irritated since yesterday."

    $ dissolve_fx("l_k_fight_2", type="cg")
    voice "ch2.3_l_005"
    l "Miss Zerbst. Today I'm going to settle this once and for all."

    voice "ch2.3_k_008"
    k "I wonder if you can. You, of all people, 'Zero'?"

    voice "ch2.3_l_006"
    l "You've said it twice now. I won't forgive you anymore..."

    voice "ch2.3_s_002"
    s "H-hey, wait a second..."

    menu:
        "Stop it, Louise":
            # ==== SCENE 91 ====
            $ dissolve_fx("l_k_fight_2", type="cg")
            voice "ch2.3_s_003"
            s "Stop it, Louise."

            voice "ch2.3_l_007"
            l "Why are you stopping me!?"

            voice "ch2.3_s_004"
            s "Because you're about to use magic, aren't you?"

            voice "ch2.3_l_008"
            l "Of course I am. It's a noble's duel — a duel."

            voice "ch2.3_s_005"
            s "That's exactly what's wrong. Your magic isn't something you can just use in front of people."

            $ dissolve_fx("l_k_fight", type="cg")
            voice "ch2.3_l_009"
            l "Ugh. That's true, but..."

            $ update_sympathy(10, char_key="louise")

            voice "ch2.3_s_006"
            s "Then isn't this the place to hold back?"

            voice "ch2.3_l_010"
            l "Ugh, ugh..."

            voice "ch2.3_k_009"
            k "What's this? After all that big talk, you're running away after all?"

            $ dissolve_fx("l_k_fight_2", type="cg")
            voice "ch2.3_l_011"
            l "What did you say!? I'm not running away!"

            th "Aah, Kirche had to go and say something unnecessary...!"
            jump ch2_3_battle

        "Stop it, Kirche":
            # ==== SCENE 92 ====
            $ dissolve_fx("l_k_fight_2", type="cg")
            voice "ch2.3_s_007"
            s "Stop it, Kirche."

            voice "ch2.3_k_010"
            k "Oh? I'm not the one who challenged anyone to a duel, darling."

            $ dissolve_fx("l_k_fight_3", type="cg")
            voice "ch2.3_k_011"
            k "The one who challenged is your master."

            voice "ch2.3_s_008"
            s "Please, could you stop provoking Louise?"

            voice "ch2.3_s_009"
            s "Besides, she seems to be in a bad mood today."

            voice "ch2.3_k_012"
            k "Mood?"

            $ dissolve_fx("l_k_fight", type="cg")
            voice "ch2.3_k_013"
            k "I don't really care about Louise's mood either way. But I don't mean to cause you trouble, darling."

            $ update_sympathy(10, char_key="kirche")

            voice "ch2.3_s_010"
            s "Well, thanks for that."

            $ dissolve_fx("l_k_fight_2", type="cg")
            voice "ch2.3_l_012"
            l "Don't go whispering unnecessary things into someone else's familiar. And what's this? After all that lofty talk, you're going to run?"

            $ dissolve_fx("l_k_fight_4", type="cg")
            voice "ch2.3_k_014"
            k "Who said anything about running?"

            th "Aah, they're getting more and more heated...!"
            jump ch2_3_battle

        "Please stop them, Professor":
            # ==== SCENE 93 ====
            $ fade_fx("classroom", sprites=("c 1 sad", "s 1 angry"))
            voice "ch2.3_s_011"
            s "Please stop them, Professor."

            $ show_sprites(("c 1 angry", "s 1 angry"))
            voice "ch2.3_c_006"
            c "Eh? Me?"

            voice "ch2.3_s_012"
            s "Who else is there? Please, stop those two."

            $ show_sprites("c 1 angry")
            voice "ch2.3_c_007"
            c "Private duels within the academy are strictly forbidden. Miss Valiere, Miss Zerbst! Stop this duel at once!"

            voice "ch2.3_c_008"
            c "I will not permit a duel in front of my eyes. For one, it disrupts the lesson."

            # Первый CG сцены — fade_fx (не dissolve): покрывающий переход сам убирает спрайты. В оригинале здесь fade
            $ fade_fx("l_k_fight_4", type="cg")
            voice "ch2.3_k_015"
            k "...I have no intention of disrupting the lesson."

            voice "ch2.3_l_013"
            l "Let's take this outside. Then we won't be a bother."

            voice "ch2.3_k_016"
            k "Fine. Let's settle this between just the two of us."

            voice "ch2.3_c_009"
            c "H-hey, wait! Miss Valiere, Miss Zerbst!"

            voice "ch2.3_s_013"
            s "It's no use...!?"
            jump ch2_3_battle

label ch2_3_battle:
    # ==== SCENE 94 ====
    $ dissolve_fx("l_k_fight_2", type="cg")

    voice "ch2.3_c_010"
    c "No, no, you two! Private duels are forbidden by the school rules."

    voice "ch2.3_l_014"
    l "In that case, let's say Professor Colbert knew nothing about it."

    voice "ch2.3_k_017"
    k "That's right. Two students were simply absent from class, so don't worry about it."

    voice "ch2.3_l_015"
    l "Let's go.{#ch2.3_L214}"

    voice "ch2.3_k_018"
    k "No need to tell me."

    $ fade_fx("classroom", sprites=("c 1 sad", "s 1 angry"))
    voice "ch2.3_s_014"
    s "Oh, man, can't be helped. Sorry, Professor. I'll go and try to stop them."

    voice "ch2.3_c_011"
    c "A-ah. Do your best."

    th "Good grief, is this part of a familiar's job too? ...No, definitely not."

    $ fade_fx("yard", sprites=("l 2 angry", "k 7 happy"))
    voice "ch2.3_k_019"
    k "Hmph, you're awfully eager for a fight this morning, aren't you?"

    voice "ch2.3_l_016"
    l "Sorry, but I don't think I can go easy on you today. Or rather, I don't intend to. Prepare yourself."

    voice "ch2.3_k_020"
    k "Fufufu. Your big mouth is almost refreshing when it goes that far."

    $ show_sprites(("l 2 angry", "s 1 angry"))
    voice "ch2.3_s_015"
    s "Hey, Louise, Kirche! That's enough, both of you!"

    $ show_sprites(("l 3 angry", "s 1 angry"))
    voice "ch2.3_l_017"
    l "You be quiet. As if that weren't enough, I've been in a bad mood since this morning."

    $ show_sprites(("l 3 angry", "k 4 happy"))
    voice "ch2.3_k_021"
    k "Oh my. Is it about Haruna? Why so jealous, I wonder?"

    $ show_sprites(("l 1 angry", "k 4 happy"))
    voice "ch2.3_l_018"
    l "What did you say!?"

    th "Aaah, what am I supposed to do...!"

    # Взрыв (SE +63)
    $ scene_fx(("blow", "flash"), None, duration=(0.7, 0.5), stop_music=True, new_music="t27")

    $ show_sprites("s 1 angry")
    voice "ch2.3_s_016"
    s "W-what was that!?"

    $ show_sprites("mage")
    voice "ch2.3_mage_001"
    mage "Hmph, I'd heard this was a magic academy, but the protection is nothing impressive."

    $ show_sprites(("l 3 angry", "k 4 angry"))
    voice "ch2.3_l_019"
    l "Wha— the mage from back then... Did they follow us all the way here?"

    voice "ch2.3_k_022"
    k "What? They infiltrated the academy?"

    $ show_sprites("mage")
    voice "ch2.3_mage_002"
    mage "Hand over that girl quietly. Otherwise, you'll get hurt."

    voice "ch2.3_s_017"
    s "Heh, wasn't it you who ran away with a lesson last time?"

    voice "ch2.3_mage_003"
    mage "Very well. If you won't hand her over, I'll just use force to get an answer."

    $ show_sprites(("l 2 angry", "k 7 angry"))
    voice "ch2.3_l_020"
    l "Kirche. Wait here for a moment. It seems I have to deal with these guys."

    voice "ch2.3_k_023"
    k "Oh, then I'll help. I absolutely hate this sort of boorish crowd."

    voice "ch2.3_l_021"
    l "Hmph. Suit yourself."

    play sound take_sword
    $ show_sprites("s 7")
    voice "ch2.3_d_001"
    d "Heh heh, now this is turning into something fun, eh? Well, we oughta thank the guy just for stopping the girls' squabble!"

    $ show_sprites("s 7 angry")
    voice "ch2.3_s_018"
    s "Couldn't agree more. I'm so happy I could cry."

    $ show_sprites("mage")
    voice "ch2.3_mage_004"
    mage "This time it won't go like last time. Minions, attack!"

    # ==== BATTLE (PS2 scene 94) ====
    # PS2: battleInit(26) / battleAdd("サイト","ルイズ","キュルケ") /
    #      battleEnemy("左","魔道士",1108) / battleEnemy("右","魔道士",1108) / battle().
    # Ремастер: API battle() есть (game/scripts/battle/*), но шаблоны бойцов в
    # game/characters.rpy закомментированы (char_data без блока "battle"), а
    # init_battle не определён → бой не подключён. Как в главе 1
    # (script-ch1_1.rpy: "call forest_battle" закомментирован) — бой не портируется.
    # $ battle(["saito", "louise", "kirche"], ["mage", "mage"])
    $ fade_fx("black", stop_music=True)
    pause(1.5)

    jump ch2_3_after

label ch2_3_after:
    # ==== SCENE 95 ====
    $ fade_fx("yard", new_music="t24", sprites=("l 2 angry", "k 7 happy"))

    voice "ch2.3_l_022"
    l "What's the matter, giving up already!?"

    voice "ch2.3_k_024"
    k "Fufun, it was more fun than I expected, but... this is the end."

    $ show_sprites("s 7 happy")
    voice "ch2.3_s_019"
    s "Heh, no matter how many times we do this, I'm not gonna lose."

    $ show_sprites("mage")
    voice "ch2.3_mage_005"
    mage "Ugh. To mere children..."

    $ show_sprites(("l 3 angry", "k 4 happy"))
    voice "ch2.3_l_023"
    l "Hmph, 'children'? There's a limit to how much you can underestimate a magic academy student."

    voice "ch2.3_k_025"
    k "That's right. Some students may look like children, but basically we're adults."

    $ show_sprites(("l 1 angry", "k 4 happy"))
    voice "ch2.3_l_024"
    l "Wh-who looks like a child!?"

    voice "ch2.3_k_026"
    k "Oh? I didn't mean you, Louise."

    voice "ch2.3_l_025"
    l "Ugh... I'll deal with that matter later."

    $ show_sprites(("l 3 angry", "k 4 happy"))
    voice "ch2.3_l_026"
    l "Now then, where shall we start? At the very least, you'll tell me your identity and why you're after that girl, right now."

    $ show_sprites(("l 3 angry", "s 2 angry"))
    voice "ch2.3_s_020"
    s "Yeah, yeah. Why don't you tell us why you're after Haruna?"

    $ show_sprites("mage")
    voice "ch2.3_mage_006"
    mage "Ugh...{#ch2.3_L365}"

    # Взрыв (SE +63)
    $ scene_fx(("blow", "flash"), None, duration=(0.7, 0.5), stop_music=True, new_music="t27")

    $ show_sprites("l 3 angry")
    voice "ch2.3_l_027"
    l "Wha— what!? What just happened!?"

    $ show_sprites(("l 3 angry", "d 1 angry"))
    voice "ch2.3_d_002"
    d "Hey, partner. ...Looks like we've got a new guest."

    $ show_sprites(("l 3 angry", "k 4 angry", "d 1 angry"))
    voice "ch2.3_l_028"
    l "Huh?{#ch2.3_L380}"

    voice "ch2.3_k_027"
    k "What?{#ch2.3_L383}"

    $ flash_fx("ak_appear", type="cg", stop_music=True, new_music="t17")
    unk "……。{#ch2.3_L386}"

    voice "ch2.3_s_021"
    s "Looks like that explosion just now was this one's doing."

    $ fade_fx("yard", sprites="k 1 angry")
    voice "ch2.3_k_028"
    k "I doubt she's one of Louise's kind, so I'd say she's a Fire user."

    voice "ch2.3_k_029"
    k "If she came to save her comrade, she's a little late."

    $ show_sprites("c 1 angry")
    voice "ch2.3_c_012"
    c "Look out! Get away, Miss Zerbst!"

    voice "ch2.3_k_030"
    k "Huh?{#ch2.3_L403}"

    voice "ch2.3_s_022"
    s "Professor?"

    # Взрыв (SE +63)
    $ show_sprites(None)
    $ scene_fx(("blow", "flash"), None, duration=(0.7, 0.5))

    voice "ch2.3_k_031"
    k "Kyaa!"

    voice "ch2.3_s_023"
    s "Whoa!"

    $ show_sprites(("l 3 sad", "k 4 angry"))
    voice "ch2.3_l_029"
    l "Wh-what!? There's a hole in the ground..."

    $ show_sprites("c 1 sad")
    voice "ch2.3_c_013"
    c "This is the power of a bomb... It must be the rumored bomb user."

    $ show_sprites(("c 1 sad", "s 2 angry"))
    voice "ch2.3_s_024"
    s "So it's the one the Professor mentioned this morning!"

    # Взрыв (SE +63)
    $ show_sprites(None)
    $ scene_fx(("blow", "flash"), None, duration=(0.7, 0.5))

    $ show_sprites(("l 1 sad", "s 2 sad"))
    voice "ch2.3_l_030"
    l "Kyaaaaa!"

    voice "ch2.3_s_025"
    s "Ugh! Is everyone all right!?"

    menu:
        "Louise, are you all right!?{#ch2.3_L442}":
            # ==== SCENE 96 ====
            $ show_sprites(("l 1 sad", "s 2 angry"))
            voice "ch2.3_s_026"
            s "Louise, are you all right!?{#ch2.3_L446}"

            $ show_sprites(("l 1 shy", "s 2 angry"))
            voice "ch2.3_l_031"
            l "Th-there's no need for you to worry about me. I'm fine, I'm not hurt."

            $ update_sympathy(10, char_key="louise")

            $ show_sprites(("l 1 shy", "s 4"))
            voice "ch2.3_s_027"
            s "I-I see, then that's good."

            voice "ch2.3_l_032"
            l "So you were worried about me."

            voice "ch2.3_s_028"
            s "Well, of course. You're my master."

            voice "ch2.3_l_033"
            l "……。{#ch2.3_L465}"

            $ show_sprites(None)
            jump ch2_4

        "Kirche, are you all right!?{#ch2.3_L470}":
            # ==== SCENE 97 ====
            $ show_sprites(("l 1 sad", "s 2 sad"))
            voice "ch2.3_s_029"
            s "Kirche, are you all right!?{#ch2.3_L474}"

            $ show_sprites(("k 4 shy", "s 2 sad"))
            voice "ch2.3_k_032"
            k "Aahn, darling was worried about me — I'm so moved!"

            $ update_sympathy(10, char_key="kirche")

            $ show_sprites(("k 4 shy", "s 4 shy"))
            voice "ch2.3_s_030"
            s "H-hey, don't cling to me."

            $ show_sprites(("l 3 angry", "s 4 shy", "k 4 shy"))
            voice "ch2.3_l_034"
            l "What are you doing, clinging to him in all this confusion!? There are still enemies!"

            $ show_sprites(("k 1", "s 4 shy"))
            voice "ch2.3_k_033"
            k "Yes, yes."

            $ show_sprites(None)
            jump ch2_4

        "Professor, are you all right!?{#ch2.3_L497}":
            # ==== SCENE 98 ====
            $ show_sprites(("l 1 sad", "s 2 sad"))
            voice "ch2.3_s_031"
            s "Professor, are you all right!?{#ch2.3_L501}"

            $ show_sprites(("c 1", "s 2 sad"))
            voice "ch2.3_c_014"
            c "Yes, I'm fine, but..."

            voice "ch2.3_l_035"
            l "Saito?"

            voice "ch2.3_s_032"
            s "Huh?{#ch2.3_L511}"

            $ update_sympathy(-10, char_key="louise")

            $ show_sprites(("l 3 angry", "s 2 sad"))
            voice "ch2.3_l_036"
            l "So I don't matter to you?"

            voice "ch2.3_s_033"
            s "Nah, it's not like that, but you should respect your elders, right?"

            $ show_sprites(("l 1 angry", "s 2 sad"))
            voice "ch2.3_l_037"
            l "...It seems you'll need a proper scolding later."

            $ show_sprites(("l 1 angry", "s 4 sad"))
            voice "ch2.3_s_034"
            s "Huh, why?"

            $ show_sprites(None)
            jump ch2_4
