# Глава 2, часть 2 (сцены 76–89): урок Кольбера, визит к Харуне, возвращение в класс
# Источник: ps2_source/chapters/chapter_03_黒髪の来訪者.txt (scene 0076…0089)
# события: ps2_source/events_full/chapter_03_黒髪の来訪者.txt (## SCENE 0076…0089)

label ch2_2:
    # ==== SCENE 76 ====
    $ fade_fx("classroom", sprites="c 1")

    voice "ch2.2_c_001"
    c "Now then, let's begin today's lesson. Hmm, now where was it we left off last time?"

    # ==== SCENE 77 ====
    voice "ch2.2_c_002"
    c "Ah yes, it was the review of the general theory of the four attributes..."
    voice "ch2.2_c_003"
    c "Today, then, let me explain each attribute in a little more detail."
    voice "ch2.2_c_004"
    c "You all surely know your own attribute from experience, but it is important to grasp each attribute properly."

    $ show_sprites("s 1")
    voice "ch2.2_s_001"
    s "As expected, everyone's taking the lesson seriously. I don't see anyone fooling around."

    th "But for me, this class is boring. Hearing it won't make me able to use magic anyway."
    th "Come to think of it, how is Haruna doing?"
    th "I left her care to Siesta, but even Siesta can't check on her while she's at work..."
    th "Hmm..."

    # ==== CHOISE (scene 77) ====
    menu:
        "Going back to my room":
            # ==== SCENE 78 ====
            th "All right, now that that's decided, right away..."

            $ show_sprites(("l 1", "s 1"))
            voice "ch2.2_l_001"
            l "Hm? What's the matter?"

            $ show_sprites(("l 1", "s 3 happy"))
            voice "ch2.2_s_002"
            s "Uh, listen, sorry, but I'm gonna skip out on class for a bit."

            $ show_sprites(("l 1 angry", "s 3 happy"))
            voice "ch2.2_l_002"
            l "Wait, what are you saying? A familiar skipping his master's class—do you think that's allowed?"

            $ update_sympathy(-10, char_key="louise")

            voice "ch2.2_s_003"
            s "Why not? If you look around, there are familiars who don't attend anyway."

            $ show_sprites(("l 3 angry", "s 3 happy"))
            voice "ch2.2_l_003"
            l "That's for familiars who can't even enter the classroom. You're human, so stay put and keep quiet."

            $ show_sprites(("l 3 angry", "s 1"))
            voice "ch2.2_s_004"
            s "Okaaay."

            $ show_sprites("s 3 sad")
            th "Still, I am worried. Maybe I'll go check on Haruna..."

            jump hallway_ch2_2

        "Not going back to my room":
            # ==== SCENE 79 ====
            th "I've decided to leave it to Siesta, so I'll just quietly listen to class."

            $ update_sympathy(10, char_key="louise")

            voice "ch2.2_s_005"
            s "...#dots"

            $ show_sprites("c 1")
            voice "ch2.2_c_005"
            c "Yes—what people often do is let themselves be trapped by the image a word carries, and narrow the diversity of an attribute themselves..."

            $ show_sprites("s 1 sad")
            th "Nope, I still don't understand a thing. If I can't use magic, I just can't get interested."

            $ show_sprites("s 3 sad")
            th "I'm still worried. Maybe I'll go check on Haruna..."

            jump hallway_ch2_2

        "What should I do...":
            # ==== SCENE 80 ====
            th "I'm worried about Haruna, but I decided to leave it to Siesta, and skipping class would be wrong..."

            $ show_sprites("s 3 sad")
            voice "ch2.2_s_006"
            s "Hmm, hmm..."

            $ show_sprites(("l 1 sad", "s 3 sad"))
            voice "ch2.2_l_004"
            l "Hey, what's wrong? You've been groaning this whole time..."

            voice "ch2.2_s_007"
            s "Uh, listen, sorry, but I'm gonna skip out on class for a bit."

            $ show_sprites(("l 1 angry", "s 3 sad"))
            voice "ch2.2_l_005"
            l "Wait, what are you saying? A familiar skipping his master's class—do you think that's allowed?"

            voice "ch2.2_s_008"
            s "Why not? If you look around, there are familiars who don't attend anyway."

            $ show_sprites(("l 3 angry", "s 3 sad"))
            voice "ch2.2_l_006"
            l "That's for familiars who can't even enter the classroom. You're human, so stay put and keep quiet."

            $ show_sprites(("l 3 angry", "s 1"))
            voice "ch2.2_s_009"
            s "Okaaay."

            $ show_sprites("s 3 sad")
            th "Still, I am worried. Maybe I'll go check on Haruna..."

            jump hallway_ch2_2


label hallway_ch2_2:
    # ==== SCENE 81 ====
    $ show_sprites("s 3 happy", side="right")
    voice "ch2.2_s_010"
    s "Well then, that's how it is—I'll leave the rest to you."

    $ show_sprites(None)

    ## как будто тут логичнее оставить сцену, а не делать hallway_down. РЕШЕНИЕ ПОЛЬЗОВАТЕЛЯ
    ##$ fade_fx("hallway_down")

    voice "ch2.2_l_007"
    l "'Leave it to you' nothing! Ah, hey!"
    voice "ch2.2_c_006"
    c "Hm? Is something the matter, Miss Valiere?"
    voice "ch2.2_l_008"
    l "Ah, no, it's nothing. M-my stupid familiar just said something about the toilet, ohohoho."

    ## а тут черный экран
    stop music fadeout 1.0
    $ fade_fx("black")

    th "I've got a feeling I'm in for quite a scolding when I get back..."

    jump l_room_ch2_2


label l_room_ch2_2:
    # ==== SCENE 82 ====
    $ fade_fx("hallway", new_music="t10", sprites="s 1")

    voice "ch2.2_s_011"
    s "Haruna? It's me, Saito..."
    voice "ch2.2_ha_001"
    ha "Ah, Hiraga-kun!? W-wait a moment. I'll unlock the door now."

    # дверь: Харуна открывает — open_door (slide + звук + смена фона), затем показ Харуны
    call open_door("right", "bg louise_room") from _call_open_door_6
    $ show_sprites("ha 3 shy")

    voice "ch2.2_ha_002"
    ha "W-what is it? Weren't you in class?"

    $ show_sprites(("ha 3 shy", "s 3 sad"))
    voice "ch2.2_s_012"
    s "I came to see how you were... Are you okay? You're still flushed."
    voice "ch2.2_ha_003"
    ha "Ah, ah... yeah. I'm sorry. I still seem to be unwell."
    voice "ch2.2_s_013"
    s "That's not good, you need to rest properly. Though I'm the one who woke you. Sorry."
    voice "ch2.2_ha_004"
    ha "Ah, no. It's not like that."
    voice "ch2.2_s_014"
    s "Never mind, get back in bed. You need to rest quietly."
    voice "ch2.2_ha_005"
    ha "O-okay."

    $ show_sprites(None)
    $ dissolve_fx("ha_sick_5", stop_music=True, new_music="t16", type="cg")

    voice "ch2.2_s_015"
    s "Uh, let's see... the water's in the basin. A towel, a towel..."
    ha "...#dots"
    voice "ch2.2_s_016"
    s "Here, does cooling your forehead with the towel make it a bit better?"

    $ dissolve_fx("ha_sick_2", type="cg")
    voice "ch2.2_ha_006"
    ha "Yeah... thank you, Hiraga-kun."
    voice "ch2.2_s_017"
    s "It's nothing. It's about all I can do, though."

    $ dissolve_fx("ha_sick_3", type="cg")
    voice "ch2.2_ha_007"
    ha "Hey, Hiraga-kun..."
    voice "ch2.2_s_018"
    s "Huh?{#un}"
    voice "ch2.2_ha_008"
    ha "Is it true that you're a familiar, Hiraga-kun? The same as that dragon-like monster."
    voice "ch2.2_s_019"
    s "Hmm. Well, that's a long story, but for now I'm Louise's familiar."
    voice "ch2.2_s_020"
    s "Well, even if I'm a familiar, I do laundry, cleaning... I guess I'm kind of like a maid?"
    voice "ch2.2_ha_009"
    ha "Louise-san's... maid?"
    voice "ch2.2_s_021"
    s "N-no... S-sometimes I fight with a sword too. Really only occasionally... though."
    voice "ch2.2_ha_010"
    ha "Fighting..."
    voice "ch2.2_s_022"
    s "There have been some dangerous moments, though..."
    voice "ch2.2_s_023"
    s "Even so, in this world I know nothing about, she's been keeping me alive, so... I guess she really is my master."
    voice "ch2.2_ha_011"
    ha "Hey... Hiraga-kun."
    voice "ch2.2_s_024"
    s "Huh?{#un}"

    $ dissolve_fx("ha_sick_2", type="cg")
    voice "ch2.2_ha_012"
    ha "Can I tell you something weird?"
    voice "ch2.2_s_025"
    s "Something weird? Well, sure..."
    voice "ch2.2_ha_013"
    ha "You know, in this world you seem to be having a lot of fun surrounded by girls. It's a little... lonely."
    voice "ch2.2_s_026"
    s "What!?"
    voice "ch2.2_s_027"
    s "No, really, it's not that much fun at all. I mean it."

    $ dissolve_fx("ha_sick_3", type="cg")
    voice "ch2.2_ha_014"
    ha "Is that so?{#haru}"
    voice "ch2.2_ha_015"
    ha "You don't seem to mind Louise-san at all, and you looked pretty close with that Siesta-san too."
    voice "ch2.2_ha_016"
    ha "Somehow, I started feeling lonely, wondering if you'd end up becoming a person of this world."
    voice "ch2.2_s_028"
    s "N-no, that's not true. It just happened. Yeah, it just happened to look that way."
    voice "ch2.2_ha_017"
    ha "Hmm, is that so?"

    # дверь: Сиеста стучит, затем открывает (звук) — до показа её спрайта
    play sound knock_door
    pause(1.0)
    voice "ch2.2_si_001"
    si "Excuse me."

    play sound open_door

    $ fade_fx("louise_room", new_music="t29", sprites="si 1 angry")
    voice "ch2.2_si_002"
    si "Haruna-san, how are you feeling? W-wait, why on earth is Saito-san here!?"

    $ show_sprites("si 4 angry")
    voice "ch2.2_si_003"
    si "Ah, don't tell me you were sneaking in for a night visit while I and Miss Valiere were away!?"

    $ show_sprites(("si 4 angry", "s 3 sad"))
    voice "ch2.2_s_029"
    s "No, I'm not doing anything like that! Besides, it's not even night yet..."

    $ show_sprites(("si 4 sad", "s 3 sad"))
    voice "ch2.2_si_004"
    si "Right, that's right... This is a bad dream... or an illusion. Just a nightmare, that's it! It has to be!"
    voice "ch2.2_s_030"
    s "Well, you see..."

    # ==== CHOISE (scene 82) ====
    menu:
        "I was worried about Haruna":
            # ==== SCENE 83 ====
            voice "ch2.2_s_031"
            s "I was worried about Haruna, so... I just kind of drifted over here."

            $ show_sprites(("si 4", "s 3 sad"))
            voice "ch2.2_si_005"
            si "Hmm... is that so."

            $ update_sympathy(-10, char_key="siesta")
            $ update_sympathy(-10, char_key="louise")


            $ show_sprites("ha 3 shy")
            voice "ch2.2_ha_018"
            ha "...#dots"

            $ update_sympathy(10, char_key="haruna")

            $ show_sprites(("si 1 sad", "ha 3 shy"))
            voice "ch2.2_si_006"
            si "Skipping class, just the two of you..."
            voice "ch2.2_s_032"
            s "Uh, um, Siesta?"

            $ show_sprites(("si 1 sad", "ha 3"))
            voice "ch2.2_ha_019"
            ha "Um, Hiraga-kun came because he was worried about me. There's nothing wrong with..."

            $ show_sprites(("si 4 sad", "ha 3"))
            voice "ch2.2_si_007"
            si "Just the two of you... In a room where no one's watching, just the two of you..."

            $ show_sprites(("si 4 sad", "s 3 sad"))
            voice "ch2.2_s_033"
            s "Siesta? Listen, I really haven't done anything shameful, okay? I even have a witness."

            $ show_sprites(("si 1 sad", "s 3 sad"))
            voice "ch2.2_si_008"
            si "A witness? Who? Don't tell me it's Haruna-san..."

            $ show_sprites(("si 1 sad", "s 1"))
            voice "ch2.2_s_034"
            s "No, this one."

            jump derf_ch2_2

        "I came to pick up something I forgot":
            # ==== SCENE 84 ====
            $ show_sprites(("si 4 sad", "s 3 happy"))
            voice "ch2.2_s_035"
            s "I came to pick up something I forgot."

            $ show_sprites(("si 1 sad", "s 3 happy"))
            voice "ch2.2_si_009"
            si "Something you forgot? Did Miss Valiere forget something?"
            voice "ch2.2_s_036"
            s "Ah, no, I forgot it."
            voice "ch2.2_si_010"
            si "You did, Saito-san? What exactly?"

            $ show_sprites(("si 1 sad", "s 1"))
            voice "ch2.2_s_037"
            s "Uh... this one."

            jump derf_ch2_2


label derf_ch2_2:
    # ==== SCENE 85 ====
    $ show_sprites(("si 1 sad", "d 1 angry", "s 1"))
    voice "ch2.2_d_001"
    d "Whoa whoa whoa, you're throwing this at me right away!?"

    voice "ch2.2_s_038"
    s "Hey, Derflinger. I just came back to the room and was talking with Haruna, right?"

    $ show_sprites(("si 1 sad", "d 1", "s 1"))
    voice "ch2.2_d_002"
    d "Relax, partner here really was just talking. He didn't do anything shady."

    $ show_sprites(("si 1", "d 1", "s 1"))
    voice "ch2.2_si_011"
    si "Is that so? I'm relieved..."
    voice "ch2.2_d_003"
    d "Really, really. You finally had the room to yourselves, and one of you was even in bed."

    $ show_sprites(("si 1", "d 1 happy", "s 1"))
    voice "ch2.2_d_004"
    d "You'd think he'd at least get in the mood... Honestly, you've got no guts, partner."

    $ show_sprites(("si 1", "s 3 angry"))
    voice "ch2.2_s_039"
    s "'No guts' was uncalled for. ...Anyway, that's how it is. You get it?"

    $ show_sprites(("si 1 happy", "s 3 angry"))
    voice "ch2.2_si_012"
    si "Yes. I'm sorry for doubting you."

    $ show_sprites(("si 1 happy", "s 1 shy"))
    voice "ch2.2_s_040"
    s "Ah, no no, as long as you understand."

    $ show_sprites(("si 1", "s 1 shy"))
    voice "ch2.2_si_013"
    si "But if you don't get back to class soon, Miss Valiere will be furious, you know?"

    $ show_sprites(("si 1", "s 1 sad"))
    voice "ch2.2_s_041"
    s "Ugh. Y-you're right."
    voice "ch2.2_si_014"
    si "I'll keep an eye on Haruna-san, so please go back to class, Saito-san."

    $ show_sprites(("si 1", "s 1"))
    voice "ch2.2_s_042"
    s "R-right. Well, I'd better get going."

    $ show_sprites(("ha 3", "s 1"))
    voice "ch2.2_ha_020"
    ha "Hiraga-kun, thank you."
    voice "ch2.2_s_043"
    s "It's nothing. Well then, take care of things, Siesta!"

    $ show_sprites(("si 1 happy", "s 1"))
    voice "ch2.2_si_015"
    si "Yes, Saito-san."

    # дверь: Сайто уходит от Харуны — open_door
    call open_door("left") from _call_open_door_7

    $ fade_fx("hallway", sprites="s 3 sad")
    th "I ended up taking quite a while. This might be more than just skipping a meal."

    jump back_class_ch2_2


label back_class_ch2_2:
    # ==== SCENE 86 ====
    $ fade_fx("classroom", new_music="t31")
    $ show_sprites("s 1")

    th "Looks like Professor Colbert's class is still going. Maybe I'll slip in quietly..."
    th "Quietly... quietly..."

    $ show_sprites("l 1 angry")
    voice "ch2.2_l_009"
    l "Well, look who's back so soon!"
    voice "ch2.2_s_044"
    s "...Ah, yeah."
    voice "ch2.2_l_010"
    l "And just what errand did you go out for?"

    $ show_sprites("l 3 angry")
    voice "ch2.2_l_011"
    l "Leaving your master behind and skipping class on your own—it must have been a terribly important errand, hmm?"
    voice "ch2.2_s_045"
    s "Ahaha, well, that's..."

    # ==== CHOISE (scene 86) ====
    menu:
        "I went to check on Haruna":
            # ==== SCENE 87 ====
            $ show_sprites(("l 3 angry", "s 3 happy"))
            voice "ch2.2_s_046"
            s "I went to see how Haruna was doing."

            $ show_sprites(("l 1 angry", "s 3 happy"))
            voice "ch2.2_l_012"
            l "...Excuse me?"

            $ update_sympathy(-10, char_key="louise")

            $ show_sprites(("l 1 angry", "s 1"))
            voice "ch2.2_s_047"
            s "It's rough being sick and stuck in bed all alone, isn't it?"
            voice "ch2.2_s_048"
            s "Well, I can't really nurse anyone, but I thought at least being there might put her at ease."
            voice "ch2.2_l_013"
            l "Hmm... You were that worried about her."

            $ show_sprites(("l 1 angry", "s 3"))
            voice "ch2.2_s_049"
            s "Anyway, just as we were talking, Siesta came to check on her too, so I figured it was fine and came back."

            $ show_sprites(("l 1 sad", "s 3"))
            voice "ch2.2_l_014"
            l "...#dots"
            voice "ch2.2_s_050"
            s "Huh, what's wrong, Louise? You suddenly went quiet."

            $ show_sprites(("l 3 angry", "s 3"))
            voice "ch2.2_l_015"
            l "You... you flirt!"

            $ hit_fx(sprites=("l 3 angry", "s 3 sad"))
            voice "ch2.2_s_051"
            s "Gwoooh! My head is splitting!"
            voice "ch2.2_l_016"
            l "You start flirting with any girl you see—have some decency! Decency!"
            voice "ch2.2_s_052"
            s "Ugh... My master, have mercy..."

            $ show_sprites(("l 3 angry", "c 1"))
            voice "ch2.2_c_007"
            c "Ah, Miss Valiere. Disciplining your familiar is all well and good, but class is in session. Quiet down."

            $ show_sprites(("l 1 sad", "c 1"))
            voice "ch2.2_l_017"
            l "Yes, I'm sorry..."

            jump ch2_3

        "I went to get Derflinger":
            # ==== SCENE 88 ====
            $ show_sprites(("l 3 angry", "s 1"))
            voice "ch2.2_s_053"
            s "I went to get Derflinger."

            $ show_sprites(("l 1", "s 1"))
            voice "ch2.2_l_018"
            l "Huh? Derflinger?"
            voice "ch2.2_s_054"
            s "Yeah, that's right. Here."

            $ show_sprites(("l 1", "d 1 happy", "s 1"))
            voice "ch2.2_d_005"
            d "Partner here just left me lying around, y'know. I was so lonely I was about to start singing to myself."

            $ show_sprites(("l 3 sad", "s 1"))
            voice "ch2.2_l_019"
            l "No, please don't. I don't want rumors that suspicious singing is coming from my room."

            $ show_sprites(("l 1", "s 1"))
            voice "ch2.2_l_020"
            l "But why? Derflinger has nothing to do with class."
            voice "ch2.2_s_055"
            s "You never know whether it's related or not, right?"
            voice "ch2.2_s_056"
            s "An enemy could show up out of nowhere. If that happens and I'm unarmed, I'd be useless, wouldn't I?"

            $ show_sprites(("l 3 shy", "s 1"))
            voice "ch2.2_l_021"
            l "H-heh. For you, that's a rather admirable attitude. I suppose I'll give you some credit."

            $ update_sympathy(10, char_key="louise")

            $ show_sprites(("l 3 shy", "s 3 happy"))
            voice "ch2.2_s_057"
            s "So with that, relax and focus on class."

            $ show_sprites(("l 3", "s 3 happy"))
            voice "ch2.2_l_022"
            l "Yeah, yeah. I'll focus properly even without being told!"

            $ show_sprites(("l 3", "c 1"))
            voice "ch2.2_c_008"
            c "Miss Valiere? Are you listening to me?"

            $ show_sprites(("l 1", "c 1"))
            voice "ch2.2_l_023"
            l "Ah, yes. I'm listening."
            voice "ch2.2_c_009"
            c "Hmm. Then it's fine."

            jump ch2_3

        "I went to the toilet":
            # ==== SCENE 89 ====
            $ show_sprites(("l 3 angry", "s 1"))
            voice "ch2.2_s_058"
            s "I was in the toilet."

            $ show_sprites(("l 3", "s 1"))
            voice "ch2.2_l_024"
            l "Huh? The toilet...? Oh, honestly! Then just say so, you idiot!"

            $ show_sprites(("l 3", "s 3 sad"))
            voice "ch2.2_s_059"
            s "Ehh. Is that the kind of thing you have to announce every single time?"
            voice "ch2.2_l_025"
            l "I'm saying that disappearing without a word is the problem!"
            voice "ch2.2_l_026"
            l "A-anyway, you've taken care of your business now, right?"
            voice "ch2.2_s_060"
            s "Yeah.{#un2}"

            $ show_sprites(("l 3 sad", "s 3 sad"))
            voice "ch2.2_l_027"
            l "Then behave yourself for the rest of class. Understood?"

            $ show_sprites(("l 3 sad", "c 1"))
            voice "ch2.2_c_010"
            c "Ah, Miss Valiere. Disciplining your familiar is all well and good, but class is in session. Quiet down."

            $ show_sprites(("l 1 sad", "c 1"))
            voice "ch2.2_l_028"
            l "Yes, I'm sorry..."

            jump ch2_3

    return
