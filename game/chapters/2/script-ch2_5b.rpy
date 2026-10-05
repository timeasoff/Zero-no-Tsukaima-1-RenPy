# Глава 2, часть 5b (сцены 1281–1296): второй проход по карте —
# ルイズの部屋 (Харуна), キルケの部屋 (Кирхе), タバサの部屋 (Табита), 廊下 (коридор).
# Источник: ps2_source/chapters/chapter_03_黒髪の来訪者.txt (scene 1281…1296)
# Точные аргументы: ps2_source/events_full/chapter_03_黒髪の来訪者.txt (SCENE 1281…1296)
# Вызываются из карты script-ch2_5.rpy (ch2_5_map) как цели sprite_choice.

label l_room_ch2_5:
    # ==== SCENE 1281 ====
    $ fade_fx("ha_sick_3", new_music="t10", type="cg")
    play sound open_door

    voice "ch2.5_ha_019"
    ha "Ah...{#ch2.5_ha1868}"

    $ update_sympathy(20, char_key="haruna")

    $ dissolve_fx("ha_sick_2", type="cg")

    voice "ch2.5_ha_020"
    ha "You're back?"

    voice "ch2.5_s_114"
    s "Ah, no. Has Louise come back?"

    $ dissolve_fx("ha_sick_3", type="cg")

    voice "ch2.5_ha_021"
    ha "...Not yet."

    voice "ch2.5_s_115"
    s "I see...{#ch2.5_s9570}"

    th "How far did that girl go anyway?"

    voice "ch2.5_ha_022"
    ha "……。{#ch2.5_ha1871}"

    voice "ch2.5_s_116"
    s "Hey, Haruna..."

    voice "ch2.5_ha_023"
    ha "……。{#ch2.5_ha1872}"

    th "What's wrong? She's in a really foul mood."

    menu:
        "Did I say something wrong?{#ch2.5_m1281a}":
            # ==== SCENE 1282 ====
            voice "ch2.5_s_117"
            s "Did I say something wrong?"

            voice "ch2.5_ha_024"
            ha "...No, you didn't say anything."

            $ update_sympathy(-10, char_key="haruna")

            voice "ch2.5_s_118"
            s "R-right? Good, then."

            th "Then why on earth is she in a bad mood?"

            voice "ch2.5_ha_025"
            ha "……。{#ch2.5_ha1874}"

            th "Did I really say something wrong?"

        "Are you scared of being alone?{#ch2.5_m1281b}":
            # ==== SCENE 1283 ====
            voice "ch2.5_s_119"
            s "Are you scared of being alone?"

            voice "ch2.5_ha_026"
            ha "S-scared, you say... a little, I guess."

            voice "ch2.5_s_120"
            s "I see... That's only natural."

            voice "ch2.5_s_121"
            s "Those guys who are after Haruna could still be lurking nearby."

            voice "ch2.5_s_122"
            s "I got caught up with Louise and forgot. Sorry."

            voice "ch2.5_ha_027"
            ha "...I-it's fine. If it's Hiraga-kun worrying about Louise-san, I suppose it can't be helped."

            voice "ch2.5_s_123"
            s "I hope you understand..."

            voice "ch2.5_ha_028"
            ha "……。{#ch2.5_ha1877}"

            th "Hmm... Did I say something weird?"

        "Does something hurt?{#ch2.5_m1281c}":
            # ==== SCENE 1284 ====
            voice "ch2.5_s_124"
            s "Does something hurt?"

            voice "ch2.5_ha_029"
            ha "That's not really it... no."

            voice "ch2.5_s_125"
            s "Is that so? But don't push yourself — tell me when it hurts, okay?"

            voice "ch2.5_s_126"
            s "I'm not the type to notice that kind of thing."

            voice "ch2.5_ha_030"
            ha "...That's true."

            voice "ch2.5_s_127"
            s "Huh? What?{#ch2.5_s9582}"

            voice "ch2.5_ha_031"
            ha "N-nothing. But thanks for worrying about me. I'm fine for now."

            th "So she's not sick after all. Then why did her mood go sour all of a sudden?"

    # ==== SCENE 1285 ====
    voice "ch2.5_d_008"
    d "So what now, partner? Wanna go look somewhere else?"

    voice "ch2.5_s_128"
    s "...Nah. At this point, let's wait here for Louise and the others to come back."

    voice "ch2.5_d_009"
    d "Got it."

    voice "ch2.5_ha_032"
    ha "……。{#ch2.5_ha1881}"

    th "I sure hope Haruna's mood perks up before Louise gets back..."

    $ ch2_5_visited.add("l_room")
    return

label kirche_room_ch2_5:
    # ==== SCENE 1286 ====
    $ fade_fx("hallway_night", new_music="t7", sprites="s 1")
    play sound knock_door

    voice "ch2.5_s_129"
    s "Hey, Kirche, you there?"

    voice "ch2.5_k_018"
    k "Oh, Darling? One moment."

    voice "ch2.5_k_019"
    k "Come on in. I've unlocked the door."

    voice "ch2.5_s_130"
    s "Pardon the intrusion~!"

    play sound open_door

    $ fade_fx("bg kirche_room_night", sprites="k 3")

    play sound close_door

    voice "ch2.5_k_020"
    k "What's wrong, Darling?"

    $ update_sympathy(20, char_key="kirche")

    $ show_sprites(("s 1", "k 3"))

    voice "ch2.5_s_131"
    s "Say, Kirche. Has Louise come by here?"

    $ show_sprites(("s 1", "k 3 sad"))

    voice "ch2.5_k_021"
    k "Louise? No, she hasn't come to this room."

    $ show_sprites(("s 3 sad", "k 3 sad"))

    voice "ch2.5_s_132"
    s "I see... Where on earth did she go?"

    $ show_sprites(("s 3 sad", "k 3 happy"))

    voice "ch2.5_k_022"
    k "...Hey, Darling."

    voice "ch2.5_s_133"
    s "Hm?{#ch2.5_s9588}"

    voice "ch2.5_k_023"
    k "What on earth did you do to Louise this time?"

    voice "ch2.5_s_134"
    s "Huh? Umm..."

    menu:
        "I think I made her mad about Haruna.{#ch2.5_m1286a}":
            # ==== SCENE 1287 ====
            voice "ch2.5_s_135"
            s "I think I made her mad about Haruna."

            voice "ch2.5_s_136"
            s "But why does it bug her that I'm looking after Haruna...? Maybe it's because I'm a familiar."

            $ show_sprites(("s 3 sad", "k 3 sad"))

            voice "ch2.5_k_024"
            k "Sigh... You really don't get it, do you."

            $ show_sprites(("s 1 sad", "k 3 sad"))

            voice "ch2.5_s_137"
            s "I don't get it?"

            $ show_sprites(("s 1 sad", "k 3"))

            voice "ch2.5_k_025"
            k "It'd be tactless for me to say it myself. Why don't you ask the person herself what the reason is?"

            $ show_sprites(("s 3 angry", "k 3"))

            voice "ch2.5_s_138"
            s "Th-there's no way I can do that. If I did, I'd get punished."

            $ show_sprites(("s 3 angry", "k 3 sad"))

            voice "ch2.5_k_026"
            k "Sigh, oh dear. Well, this is Louise's own fault too, I suppose."

        "It's Louise's usual tantrum.{#ch2.5_m1286b}":
            # ==== SCENE 1288 ====
            $ show_sprites(("s 3 angry", "k 3 happy"))

            voice "ch2.5_s_139"
            s "It's Louise's usual tantrum."

            $ show_sprites(("s 3 angry", "k 3"))

            voice "ch2.5_k_027"
            k "I see... So that's what you think, Darling."

            voice "ch2.5_s_140"
            s "But Louise blows up out of nowhere all the time, right?"

            $ show_sprites(("s 3 angry", "k 3 sad"))

            voice "ch2.5_k_028"
            k "That may be how it looks from your side... Sigh, I guess you're both alike."

            $ show_sprites(("s 3 angry", "k 3"))

            voice "ch2.5_k_029"
            k "I'm keeping quiet because anything I say here won't help. But try to think about Louise a little too."

        "I don't really know either.{#ch2.5_m1286c}":
            # ==== SCENE 1289 ====
            voice "ch2.5_s_141"
            s "I don't really know either."

            $ show_sprites(("s 3 sad", "k 3 sad"))

            voice "ch2.5_k_030"
            k "Really?{#ch2.5_k2950}"

            $ update_sympathy(-10, char_key="kirche")

            voice "ch2.5_s_142"
            s "No, I really don't! Louise suddenly blew up and stormed off... I didn't even have time to hear her side."

            voice "ch2.5_s_143"
            s "She's also seemed oddly sullen since this morning. Maybe she wasn't feeling well?"

            $ show_sprites(("s 3 sad", "k 3"))

            voice "ch2.5_k_031"
            k "Hmm... Well, in your own way you're thinking about Louise. Even if you're a little off."

            $ show_sprites(("s 3", "k 3"))

            voice "ch2.5_s_144"
            s "Huh? I'm off?"

            voice "ch2.5_k_032"
            k "Hmm... Personally, I'd rather you stayed off the mark. It's a little complicated..."

    # ==== SCENE 1290 ====
    $ show_sprites(("s 3", "k 3 sad"))

    voice "ch2.5_s_145"
    s "Say... Kirche, you know why Louise got angry, don't you?"

    voice "ch2.5_k_033"
    k "Mm, more or less."

    $ show_sprites(("s 1", "k 3 sad"))

    voice "ch2.5_s_146"
    s "C-could you tell me?"

    voice "ch2.5_k_034"
    k "No way. Think about it yourself."

    voice "ch2.5_s_147"
    s "Yeah...{#ch2.5_s9602}"

    voice "ch2.5_k_035"
    k "Well, that girl will come back to her room eventually, won't she? Go back first and wait?"

    voice "ch2.5_k_036"
    k "Also, don't you think you two should talk a bit more?"

    voice "ch2.5_s_148"
    s "Yeah... I'll try that. Thanks, Kirche."

    $ show_sprites(("s 1", "k 3 happy"))

    voice "ch2.5_k_037"
    k "You're welcome.{#ch2.5_k2957}"

    play sound open_door

    $ fade_fx("hallway_night", sprites="s 1 sad")

    play sound close_door

    voice "ch2.5_s_149"
    s "Alright, maybe I'll head back to my room for a bit."

    $ ch2_5_visited.add("kirche_room")
    return

label tabitha_room_ch2_5:
    # ==== SCENE 1291 ====
    $ fade_fx("hallway_night", new_music="t8", sprites="s 1")
    play sound knock_door

    voice "ch2.5_s_150"
    s "Hey, Tabitha, you there?"

    voice "ch2.5_s_151"
    s "……。{#ch2.5_s9606}"

    voice "ch2.5_s_152"
    s "Maybe she's out."

    voice "ch2.5_t_013"
    t "...Unlocked."

    voice "ch2.5_s_153"
    s "Sorry, coming in."

    play sound open_door

    $ fade_fx("bg tabitha_room_night", sprites="t 3")

    play sound close_door

    t "……。{#ch2.5_t1291}"

    $ update_sympathy(30, char_key="tabitha")

    $ show_sprites(("s 3", "t 3"))

    voice "ch2.5_s_154"
    s "Good, you're here. Say, has Louise come this way?"

    voice "ch2.5_t_014"
    t "...No.{#ch2.5_t15430}"

    $ show_sprites(("s 3 sad", "t 3"))

    voice "ch2.5_s_155"
    s "I... see.{#ch2.5_s9610}"

    th "Ugh, with that same expressionless face, I can't tell if she's lying or telling the truth..."

    voice "ch2.5_t_015"
    t "...What?{#ch2.5_t15431}"

    $ show_sprites(("s 1 sad", "t 3"))

    voice "ch2.5_s_156"
    s "Ah, no...{#ch2.5_s9611}"

    menu:
        "What were you doing?{#ch2.5_m1291a}":
            # ==== SCENE 1292 ====
            $ show_sprites(("s 1", "t 3"))

            voice "ch2.5_s_157"
            s "What were you doing?"

            voice "ch2.5_t_016"
            t "...Watching the stars."

            voice "ch2.5_s_158"
            s "Stars?"

            voice "ch2.5_t_017"
            t "...Yep.{#ch2.5_t15433}"

            voice "ch2.5_t_018"
            t "...That star is the Hunter of the North. Remember it, and you won't lose your way."

            $ show_sprites(("s 3 sad", "t 3"))

            voice "ch2.5_s_159"
            s "Umm, where is it roughly?"

            voice "ch2.5_t_019"
            t "...That one.{#ch2.5_t15435}"

            th "The night sky here looks nothing like the one in Japan. Well, obviously."

            t "……。{#ch2.5_t1292a}"

            voice "ch2.5_s_160"
            s "...Whoa."

            $ show_sprites(("s 1", "t 3"))

            voice "ch2.5_s_161"
            s "The stars are pretty, but I've got to go look for Louise."

            voice "ch2.5_s_162"
            s "Thanks for showing me the stars."

            $ show_sprites(("s 1", "t 3 happy"))

            t "……。{#ch2.5_t1292b}"

            $ update_sympathy(15, char_key="tabitha")

        "Why did you unlock the door?{#ch2.5_m1291b}":
            # ==== SCENE 1293 ====
            $ show_sprites(("s 1", "t 3"))

            voice "ch2.5_s_163"
            s "Why did you unlock the door?"

            voice "ch2.5_t_020"
            t "...Because you were looking for Louise."

            $ show_sprites(("s 3", "t 3"))

            voice "ch2.5_s_164"
            s "Huh? Ah, no, I was looking for her, sure. But that's it?"

            voice "ch2.5_t_021"
            t "...Right. But that's what matters."

            $ show_sprites(("s 3 sad", "t 3"))

            voice "ch2.5_s_165"
            s "Huh? Sorry, I seriously don't get it."

            $ show_sprites(("s 3 sad", "t 3 sad"))

            voice "ch2.5_t_022"
            t "...If you don't get it, fine."

            $ show_sprites(("s 3 happy", "t 3 sad"))

            voice "ch2.5_s_166"
            s "Umm, yeah, got it. I don't really get it, but got it."

            $ show_sprites(("s 1", "t 3 sad"))

            voice "ch2.5_s_167"
            s "Well, I should get going."

        "Do you really not know where Louise is?{#ch2.5_m1291c}":
            # ==== SCENE 1294 ====
            $ show_sprites(("s 1", "t 3"))

            voice "ch2.5_s_168"
            s "Do you really not know where Louise is?"

            voice "ch2.5_t_023"
            t "...I don't.{#ch2.5_t15439}"

            $ update_sympathy(-15, char_key="tabitha")

            $ show_sprites(("s 3", "t 3"))

            voice "ch2.5_s_169"
            s "I see. Sorry for barging in on you."

            t "……。{#ch2.5_t1294}"

            $ show_sprites(("s 1", "t 3"))

            voice "ch2.5_s_170"
            s "Um, looks like I'm in the way, so I'll get going."

    # ==== SCENE 1295 ====
    $ show_sprites(("s 1", "t 3"))

    voice "ch2.5_t_024"
    t "...Remain alert."

    $ show_sprites(("s 3 sad", "t 3"))

    voice "ch2.5_s_171"
    s "Huh? Not 'be careful'?"

    voice "ch2.5_t_025"
    t "...Well then.{#ch2.5_t15441}"

    play sound open_door

    $ fade_fx("hallway_night", sprites="s 3 sad")

    play sound close_door

    voice "ch2.5_s_172"
    s "Hmm? What was that about?"

    voice "ch2.5_s_173"
    s "No time to worry about that. I'll head back to Louise's room for now."

    $ ch2_5_visited.add("tabitha_room")
    return

label corridor_ch2_5:
    # ==== SCENE 1296 ====
    $ fade_fx("hallway_down_night", new_music="t31", sprites=("d 1", "s 3 sad"))

    voice "ch2.5_s_174"
    s "Still, there's nobody around, huh."

    voice "ch2.5_d_010"
    d "After what happened today, nobody's gonna be wandering around outside their room."

    voice "ch2.5_d_011"
    d "Partner, maybe we should head back to the room first. We might have crossed paths — those two could already be back."

    $ show_sprites(("d 1", "s 1"))

    voice "ch2.5_s_175"
    s "Alright, let's head back. Louise and Siesta can't be wandering around forever... I think."

    $ ch2_5_visited.add("corridor")
    return
