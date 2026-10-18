# Глава 4, часть 5 (сцены 256–260): Прибытие во дворец, встреча с Анриеттой,
# объяснение ситуации с Харуной, меню подозрений (257/258/259), миссия.
# Источник: ps2_source/chapters/chapter_05_トリスタニアの危機.txt
#   (SCENE 256–260)
# Точные аргументы: ps2_source/events_full/chapter_05_トリスタニアの危機.txt.
#
# Голоса: ch4.5_<spk>_<NNN> — новая группа части 5, нумерация с 001 по
# говорящему, порядок порта (256 → меню 257/258/259 → 260):
#   s ×46 (001–022 main, 023–025 257, 026–029 258, 030–033 259, 034–046 260),
#   l ×24 (001–013 main, 014–015 258, 016–017 259, 018–024 260),
#   h (Анриетта) ×20 (001–010 main, 011–012 257, 013–016 258, 017–020 260),
#   ha ×8 (001–003 main, 004–006 256, 007–008 259),
#   si ×3 (001–002 main, 003 259), d ×2 (260).
# Не портируются: SE (se0 +61/+63/+65, se1 stop), точечные level=/dir=/sync,
#   msgon/msgoff, waitAction, vibrate (AGENTS §6).
# Симпатия (3 вызова update_sympathy): 257 louise +10, 258 henrietta −30,
#   259 henrietta +30 (257), louise −10 (258).
# Спрайты: h-пул 764/766/768/770/801 (h 1/h 1 happy/h 1 sad/h 1 angry/h 1 shy)
#   из карты; s-пул 401/403/405/407 (s 2/s 2 happy/s 2 angry/s 2 sad),
#   434/436/438/440 (s 4/s 4 happy/s 4 angry/s 4 sad),
#   302/304/306/308 (l 1/l 1 happy/l 1 angry/l 1 sad),
#   335/339/341 (l 3/l 3 angry/l 3 sad),
#   489/491 (si 1/si 1 happy), 940/946 (d 1/d 1 sad).
# Фоны: 62 (заглушка id(62)), 63 (заглушка id(63)), 36 (заглушка id(36)),
#   59 town_square_evening, 2 white, 1151/1142 (заглушки id(1151)/id(1142)),
#   102/206/207 (заглушки id(102)/id(206)/id(207)).
# BGM t{K-1}: +21→t20 (256), +10→t9 (256), +28→t27 (256/257/258/259/260),
#   +27→t26 (260); stop перед сходами/выходами.
# Меню подозрений: 257 «Луиза невиновна» / 258 «Луиза виновна» /
#   259 «Другая информация» → сход на 260.

label ch4_5:
    # ==== SCENE 256 ==== (RESET: [SE se1 stop][BGM +21 → t20][BG +62
    # (заглушка id(62))][TRANS 500][BG +1151 (заглушка id(1151))][TRANS 500]
    # [BG +1142 (заглушка id(1142))][TRANS 500][BG +1151][TRANS 750]
    # [BG +62][TRANS 2000][BG +63 (заглушка id(63))][TRANS 1000][BGM +21])
    # Монтаж 62→1151→1142→1151→62→63 свёрнут в финальный кадр 63
    #   (дворец; кадры монтажа — заглушки id(K), имена не заполнены).
    $ fade_fx("id(63)", new_music="t20")

    th "The appointed time had come, and we set foot in the palace where the princess awaited us."

    $ show_sprites(("s 2",))

    voice "ch4.5_s_001"
    s "I wonder if the princess is doing well. It's been a while since we last saw each other like this, Louise."

    th "Come to think of it, the last time was when the war ended…"

    th "In the end, we never got to test whether the way back to our world was real or not."

    th "Well, we'll find another way someday."

    $ show_sprites(("s 2", "l 1 angry"))

    voice "ch4.5_l_001"
    l "Hey, Saito, be quiet. And don't call her 'the princess' so casually!"

    $ show_sprites(("s 4", "l 3 angry"))

    voice "ch4.5_s_002"
    s "But isn't she already an acquaintance of ours?"

    $ show_sprites(("s 4", "l 1"))

    voice "ch4.5_l_002"
    l "You fool, that's extremely rude! The princess is now the queen who supports an entire nation!"

    $ show_sprites(("s 4", "l 1"))

    voice "ch4.5_l_003"
    l "You may be my familiar, but to others you're a commoner. You must be more respectful!"

    $ show_sprites(("s 4", "l 1 angry"))

    voice "ch4.5_l_004"
    l "Otherwise, you'll be charged with insulting the queen, and it will go badly for you!"

    $ show_sprites(("s 4", "l 1"))

    voice "ch4.5_s_003"
    s "Yeah, I know."

    stop music fadeout 1.0
    $ show_sprites()
    $ fade_fx("id(36)", new_music="t9")

    # [BG hide][BG +36 (заглушка id(36))][TRANS 1000][BGM +10 → t9][lay8 +766 (h 1 happy)]
    $ show_sprites(("h 1 happy",))

    voice "ch4.5_h_001"
    h "Ah, it's been so long! Louise Françoise."

    # [lay8 hide][EVENT_CG +206 (заглушка id(206))][TRANS 1000]
    $ show_sprites()
    $ fade_fx("id(206)", type="cg")

    voice "ch4.5_l_005"
    l "Your Majesty, I wish you good health."

    voice "ch4.5_h_002"
    h "Louise. You look as energetic as ever. Please, raise your head."

    voice "ch4.5_h_003"
    h "And here, let's not stand on ceremony. Can't you call me by my name as you did in the old days?"

    # [EVENT_CG 206 → 207 (заглушка id(207))]
    $ fade_fx("id(207)", type="cg")

    voice "ch4.5_l_006"
    l "Yes…."

    voice "ch4.5_h_004"
    h "And your familiar here? He hasn't changed either, has he?"

    # [lay8 hide][lay1 hide][BG hide][EVENT_CG hide][BG +36 (заглушка id(36))][TRANS 1000]
    # [lay8 +764 (h 1)][lay5 +401 (s 2)]
    $ fade_fx("id(36)")
    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_s_004"
    s "Ah… yes. It is an honor to meet you again."

    $ show_sprites(("s 2", "h 1 happy"))

    voice "ch4.5_h_005"
    h "And this woman here?"

    $ show_sprites(("s 2", "si 1"))

    voice "ch4.5_si_001"
    si "Yes, it is I. I am Siesta, a maid serving at the academy."

    $ show_sprites(("s 2", "l 1"))

    voice "ch4.5_l_007"
    l "Um, well… This time I have brought her as my servant to the castle."

    $ show_sprites(("s 2", "h 1 happy"))

    voice "ch4.5_h_006"
    h "They call you Siesta? It's a pleasure to meet you."

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_007"
    h "And this other girl here… I don't often see a face like hers around here."

    $ show_sprites(("s 2", "l 3 sad"))

    voice "ch4.5_l_008"
    l "Ah, um, this girl is…"

    $ show_sprites(("s 2", "ha 1"))

    voice "ch4.5_ha_001"
    ha "Um… It is my first time meeting you. I am Haruna Takanagi."

    $ show_sprites(("s 2", "h 1 happy"))

    voice "ch4.5_h_008"
    h "So you are Miss Takanagi Haruna. Are you perhaps the person from another world that the headmaster reported?"

    $ show_sprites(("s 2", "l 1"))

    voice "ch4.5_l_009"
    l "Regarding that, I will tell you everything now."

    voice "ch4.5_l_010"
    l "Princess. Please, calm down and lend me your ear."

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_009"
    h "Very well, Louise. I will listen to your confession with an open heart."

    $ show_sprites()
    # [BG hide] (пустой тайм-скип: 3 строки канона) [BG hide][BG +36 (заглушка id(36))][TRANS]
    $ fade_fx("black")
    th "………………{#ch4.5_null_a}"

    $ fade_fx("id(36)")
    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_010"
    h "I see. I understand the general situation."

    voice "ch4.5_h_011"
    h "As the headmaster says, Takanagi Haruna was not summoned as a familiar…"

    voice "ch4.5_h_012"
    h "And the reason for that is still unknown, you say."

    voice "ch4.5_l_011"
    l "Yes.{#ch4.5_d029}"

    $ show_sprites(("s 2", "h 1 happy"))

    voice "ch4.5_h_013"
    h "Very well. I will continue to entrust Takanagi Haruna's care to you, Louise Françoise."

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_014"
    h "However, given the circumstances, I must forbid you to make it public that she came from another world."

    $ show_sprites(("s 2", "h 1 angry"))

    voice "ch4.5_h_015"
    h "There is a risk she may be exploited by those who harbor dark conspiracies."

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_l_012"
    l "Your Highness, please allow me to express my deepest gratitude for your understanding."

    $ show_sprites(("s 2", "ha 1 happy"))

    voice "ch4.5_ha_002"
    ha "Thank you, Your Majesty."

    $ show_sprites(("s 2", "ha 1"))

    voice "ch4.5_h_016"
    h "Miss Haruna."

    voice "ch4.5_ha_003"
    ha "Yes.{#ch4.5_d036}"

    $ show_sprites(("s 2", "ha 1 happy"))

    voice "ch4.5_h_017"
    h "Life in another world right from the start. It may be difficult, but please do your best."

    $ show_sprites(("s 2", "ha 1"))

    voice "ch4.5_h_018"
    h "As with this familiar of yours, the day will surely come when you can return."

    $ show_sprites(("s 2", "ha 1 happy"))

    voice "ch4.5_ha_004"
    ha "Thank you very much.{#ch4.5_d039}"

    $ show_sprites(("s 2", "si 1 happy"))

    voice "ch4.5_si_002"
    si "I'm so relieved. Is everything settled now?"

    $ show_sprites(("s 2", "s 2"))

    voice "ch4.5_s_005"
    s "Yeah, I guess so.{#ch4.5_d041}"

    $ show_sprites()
    $ fade_fx("id(36)")

    # ==== SCENE 256 (продолжение) ==== (BG hide → BG +36 (заглушка id(36)), TRANS 1000;
    # BGM не меняется — t9 продолжается до stop в 1842)
    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_019"
    h "By the way, there is another reason I called you all here like this."

    $ show_sprites(("s 2", "l 1"))

    voice "ch4.5_l_013"
    l "Eh… What do you mean!?"

    $ show_sprites(("s 2", "l 1 sad"))

    voice "ch4.5_l_014"
    l "I thought it was because of Haruna!"

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_020"
    h "No. This is the first I have heard of Miss Haruna."

    $ show_sprites(("s 2", "h 1 angry"))

    voice "ch4.5_h_021"
    h "What I am about to tell you is, in a sense, a grave problem."

    $ show_sprites(("s 2",))

    voice "ch4.5_s_006"
    s "What is this grave problem?"

    $ show_sprites(("s 2", "l 1 angry"))

    voice "ch4.5_l_015"
    l "Saito! How many times must I tell you not to speak so familiarly!"

    voice "ch4.5_l_016"
    l "I am terribly sorry, Your Majesty. The fault is entirely mine as his master…"

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_022"
    h "Louise, it is fine. Let us speak."

    voice "ch4.5_h_023"
    h "Miss Haruna, Miss Siesta. I am sorry, but could you please excuse us for a moment?"

    $ show_sprites(("s 2", "ha 1"))

    voice "ch4.5_ha_005"
    ha "Yes, of course."

    $ show_sprites(("s 2", "si 1"))

    voice "ch4.5_si_003"
    si "Then, we will take our leave."

    $ show_sprites(("s 2",))
    th "Haruna seemed a bit anxious, but the two of them bowed deeply and left the audience chamber, escorted by the attendants."

    stop music fadeout 1.0
    $ show_sprites()
    $ fade_fx("id(36)", new_music="t27")

    # ==== SCENE 256 (завершение) ==== (BGM +28 → t27)
    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_024"
    h "Now then, to the main topic."

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_025"
    h "Recently, there have been rumors of a person called the 'Bomb User' operating in the shadows. Louise, and you, familiar—surely you have heard of them?"

    # [lay8 x=224 — точечный сдвиг не копируется][lay1 +302 (l 1) dir=1A]
    $ show_sprites(("s 2", "l 1"))

    voice "ch4.5_l_017"
    l "Yes — the other day the academy was attacked too, by someone who looked like the Bomb User."

    # [lay8 +770 (h 1 angry) dir=1A]
    $ show_sprites(("s 2", "h 1 angry"))

    voice "ch4.5_h_026"
    h "Is that so… Louise, did you see who that person was?"

    $ show_sprites(("s 2", "l 1 sad"))

    voice "ch4.5_l_018"
    l "Yes… But I could not see their face."

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_027"
    h "That is unfortunate. We, for our part, are trying to identify the suspect and have conducted an investigation."

    $ show_sprites(("s 2", "h 1 happy"))

    voice "ch4.5_h_028"
    h "As a result, we were able to narrow down the suspects from the characteristics of the perpetrator and the areas where the incidents occurred."

    $ show_sprites(("s 2", "s 2"))

    voice "ch4.5_s_007"
    s "Oh, that's quick. So we just need to find that culprit and bring them to you, right, Princess?"

    $ show_sprites(("s 2", "l 3 angry"))

    voice "ch4.5_l_019"
    l "Hey, don't just decide the story yourself!"

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_029"
    h "That's right. The gist of it is as the familiar says."

    $ show_sprites(("s 2", "h 1 angry"))

    voice "ch4.5_h_030"
    h "The characteristics of the culprit are that they are relatively small and agile, and that they wore a robe draped over their entire head."

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_031"
    h "So the intelligence agency believes the culprit is a small-statured boy."

    $ show_sprites(("s 2", "l 1"))

    voice "ch4.5_l_020"
    l "A boy… you say?"

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_032"
    h "This is just my own conjecture, but judging by the culprit's appearance, I also think they might be a woman."

    $ show_sprites(("s 2", "h 1 happy"))

    voice "ch4.5_h_033"
    h "And so, when we cross-referenced the culprit's appearance with women, one person came to mind."

    $ show_sprites(("s 2",))

    voice "ch4.5_s_008"
    s "Hmm-hmm."

    $ show_sprites(("s 2", "h 1 angry"))

    voice "ch4.5_h_034"
    h "There are two characteristics for identifying the culprit. One is 'explosions.' And if it is a woman, then 'the girl with no chest.'"

    $ show_sprites(("s 2", "l 1 shy"))

    voice "ch4.5_l_021"
    l "M-me!?{#ch4.5_d071}"

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.5_h_035"
    h "N-no. I haven't said anything about you yet…"

    $ show_sprites(("s 2", "s 2 happy"))

    voice "ch4.5_s_009"
    s "Ahahahaha!! That's definitely Louise and no one else!"

    $ show_sprites(("s 2", "l 3 angry"))

    voice "ch4.5_l_022"
    l "To dare call your own master the culprit… What an impertinent dog you are!"

    $ show_sprites(("s 2", "s 2 sad"))

    voice "ch4.5_s_010"
    s "N-no, Louise. Calm down. Let's think about this a bit more."

    # 【選択肢】×3 (сцена 256)
    menu ch4_5_256_choice:
        "The Bomb User isn't Louise.{#ch4.5_c256a}":
            jump ch4_5_257
        "The Bomb User is Louise.{#ch4.5_c256b}":
            jump ch4_5_258
        "Is there other information?{#ch4.5_c256c}":
            jump ch4_5_259


label ch4_5_257:
    # ==== SCENE 257 ==== (ветка «Луиза невиновна»)
    $ show_sprites(("s 2 sad", "l 3 angry"))

    voice "ch4.5_s_011"
    s "Louise is not the culprit."

    $ show_sprites(("s 2", "l 3 angry"))

    voice "ch4.5_s_012"
    s "When the Bomb User appeared at the academy, Louise was with me. Louise has an alibi."

    # 【好感度】ルイズ 10
    $ update_sympathy(10, char_key="louise")

    $ show_sprites(("h 1", "l 3 angry"))

    voice "ch4.5_h_036"
    h "I see. That is important testimony."

    # 【好感度】アンリエッタ 30
    $ update_sympathy(30, char_key="henrietta")
    # → next scene 260
    jump ch4_5_260


label ch4_5_258:
    # ==== SCENE 258 ==== (ветка «Луиза виновна»)
    $ show_sprites(("s 2 sad", "l 3 angry"))

    voice "ch4.5_s_013"
    s "The Bomb User is Louise. No mistake."

    $ show_sprites(("h 1 shy", "l 3 angry"))

    voice "ch4.5_h_037"
    h "What did you say!? Familiar, keep your jokes to yourself."

    # 【好感度】アンリエッタ -30
    $ update_sympathy(-30, char_key="henrietta")

    $ show_sprites(("s 4", "l 3 angry"))

    voice "ch4.5_s_014"
    s "Explosions and a chest. The only one who fits these conditions in all of Tristania is Louise."

    # [SE se0 play=+61][BG vibrate=14] — SE не портируется
    $ shake_fx()

    $ show_sprites(("s 2 sad",))

    voice "ch4.5_s_015"
    s "W-whoa… I've really done it now."

    $ show_sprites(("s 2 sad", "l 1 angry"))

    voice "ch4.5_l_023"
    l "Id-diot! Watch what you're saying! In front of Her Majesty!"

    # 【好感度】ルイズ -10
    $ update_sympathy(-10, char_key="louise")

    $ show_sprites(("h 1 angry", "l 1 angry"))

    voice "ch4.5_h_038"
    h "Louise, calm down. I believe in you."

    # → next scene 260
    jump ch4_5_260


label ch4_5_259:
    # ==== SCENE 259 ==== (ветка «Другая информация»)
    $ show_sprites(("s 2 sad", "l 3 angry"))

    voice "ch4.5_s_016"
    s "Isn't there any other information? With just this, we can't tell if it's Louise or someone else."

    $ show_sprites(("s 2 sad", "l 1"))

    voice "ch4.5_l_024"
    l "It's not me!"

    $ show_sprites(("s 4 sad", "l 1"))

    voice "ch4.5_s_017"
    s "I know that.{#ch4.5_d087}"

    $ show_sprites(("s 4 sad", "h 1"))

    voice "ch4.5_h_039"
    h "That's exactly right. It is as the familiar says."

    # → next scene 260
    jump ch4_5_260


label ch4_5_260:
    # ==== SCENE 260 ==== (сход веток; BGM +28 → t27)
    $ show_sprites(("s 2 happy", "h 1"))

    voice "ch4.5_h_040"
    h "Louise, and you, familiar. I would like to ask the two of you to investigate and capture the Bomb User."

    $ show_sprites(("s 2 happy", "l 1 sad"))

    voice "ch4.5_l_025"
    l "There is no need to ask such a thing!"

    $ show_sprites(("s 2 happy", "l 1"))

    voice "ch4.5_l_026"
    l "As the third daughter of the House of La Vallière, Louise Françoise will bring the Bomb User before Your Majesty, in the name of the nobility."

    $ show_sprites(("s 2 happy", "h 1 angry"))

    voice "ch4.5_h_041"
    h "If this were truly the case, I would not wish to entrust such a dangerous task to my friend Louise…"

    $ show_sprites(("s 2 happy", "l 1 happy"))

    voice "ch4.5_l_027"
    l "What a thing to say. We will surely meet Your Highness's expectations."

    $ show_sprites(("s 2 happy",))

    voice "ch4.5_s_018"
    s "Princess, just you wait for our good news."

    $ show_sprites(("s 2 happy", "h 1 happy"))

    voice "ch4.5_h_042"
    h "My, how reassuring. I believe in the efforts of Louise and her familiar."

    # [BGM stop=1000][SE se0 play=+63][BG vibrate=14] — SE не портируется
    stop music fadeout 1.0
    $ shake_fx()

    # [BGM +27 → t26][lay8 +768 (h 1 sad)]
    play music t26 fadein 1.0
    $ show_sprites(("s 2 angry", "h 1 sad"))

    voice "ch4.5_h_043"
    h "Nn…!!"

    $ show_sprites(("s 2 angry", "l 1"))

    voice "ch4.5_l_028"
    l "Kyaah!!"

    $ show_sprites(("s 2 angry",))

    voice "ch4.5_s_019"
    s "What!?{#ch4.5_d098}"

    th "Suddenly, a loud explosion was heard."

    voice "ch4.5_s_020"
    s "Speaking of the devil… Is that it!"

    $ show_sprites(("s 2 angry", "l 3 angry"))

    voice "ch4.5_l_029"
    l "Heh, this is perfect. Let's go, Saito! Your Highness, please flee to a safe place!!"

    $ show_sprites(("s 2 angry", "h 1 sad"))

    voice "ch4.5_h_044"
    h "Louise!!{#ch4.5_d101}"

    $ show_sprites(("s 2 angry", "l 1"))

    voice "ch4.5_l_030"
    l "……!?"

    $ show_sprites(("s 2 angry", "h 1 angry"))

    voice "ch4.5_h_045"
    h "Louise. Promise me you won't do anything reckless."

    $ show_sprites(("s 2 angry", "l 3"))

    voice "ch4.5_l_031"
    l "Of course. Now, quickly, to the back!!"

    $ show_sprites(("s 2 angry", "s 4 angry"))

    voice "ch4.5_s_021"
    s "Derflinger, from here on it's our turn."

    # [SE se0 play=+65] — SE не портируется
    $ show_sprites(("s 4 angry", "d 1"))

    voice "ch4.5_d_001"
    d "You called, partner! Don't let your guard down, yeah?"

    $ show_sprites(("s 4 angry",))

    voice "ch4.5_s_022"
    s "Louise, this way!"

    $ show_sprites(("s 4 angry", "l 1 angry"))

    voice "ch4.5_l_032"
    l "H-hey! Wait a minute!"

    $ show_sprites(("s 4 angry", "l 3 angry"))

    voice "ch4.5_l_033"
    l "Gh… Just you wait, Bomb User. I will definitely catch you!!"

    # [SE se1 stop][BGM stop=1000] — SE не портируется
    stop music fadeout 1.0
    $ show_sprites()
    # → next scene 261
    jump ch4_6
