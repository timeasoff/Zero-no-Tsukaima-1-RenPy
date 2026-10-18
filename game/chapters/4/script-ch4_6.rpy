# Глава 4, часть 6 (сцены 261–268): Финал основной линии
#
# Источник: ps2_source/chapters/chapter_05_トリスタニアの危機.txt (SCENE 261–268)
# Точные аргументы: ps2_source/events_full/chapter_05_トリスタニアの危機.txt.
#
# Голоса: ch4.6_<spk>_<NNN> — новая группа части 6, нумерация с 001 по говорящему, порядок порта (261 → 262 → 263 → 264 → 265 → 266 → 267 → 268):
#   s ×12 (001–012), l ×7 (001–007), h ×4 (001–004), ha ×3 (001–003), si ×2 (001–002), d ×5 (001–005), k ×5 (001–005), o ×6 (001–007), t ×5 (001–005), c ×4 (001–004), a ×3 (001–003)
#
# Не портируются: SE (se0/se1), точечные level=/dir=/sync, vibrate, waitAction, msgon/msgoff (AGENTS.md §6).
#   Битва с акиной: используется shake_fx() вместо vibrate.
#
# Вход: jump ch4_6 из ch4_5.rpy (конец part 5). Выход: jump ch4_7 (или jump attention при завершении главы).
#
# Примечание: сцены 1342-1382 (кома/движение) и дополнительные сцены (1084-1103) будут обработаны отдельно
#   в соответствии с алгоритмом разрезки главы на части (AGENTS.md §3).

label ch4_6:
    # ==== SCENE 261 ====
    # [BG +59, level=200][TRANS 1000][BGM +18 → t18][lay5 +405 (s 2 sad)]
    $ fade_fx("id(59)", new_music="t18")
    $ show_sprites(("s 2 sad",))

    voice "ch4.6_s_001"
    s "Ugh... where's that damn Louise..."

    voice "ch4.6_s_002"
    s "That idiot over there..."

    th "I wonder where that idiot went..."

    # [BG hide][BG +59][TRANS 1000][BGM +18 → t18][lay5 +405 (s 2 sad)]
    $ fade_fx("id(59)")

    # ==== SCENE 262 ==== (битва с акиной)
    # [BG +59, level=200][TRANS 1000][BGM +18][lay21 +1028 (k 1)]
    $ show_sprites(("k 1",))

    voice "ch4.6_k_001"
    k "......くっ！！！！..."

    $ show_sprites(("k 1 sad",))

    voice "ch4.6_k_002"
    k "こんな相手に……。"

    $ show_sprites(("s 2",))

    voice "ch4.6_s_003"
    s "W-what?!"

    th "Saito...?"

    $ show_sprites(("s 2", "l 3 angry"))

    voice "ch4.6_l_001"
    l "There's got to be some way to beat this guy!"

    voice "ch4.6_l_002"
    l "In any case, let's start the battle."

    $ show_sprites(("s 4 angry",))

    voice "ch4.6_s_004"
    s "Louise, that's enough!"

    $ show_sprites(("s 2", "l 3 angry"))

    voice "ch4.6_s_005"
    s "Calm down and listen!"

    # [BG hide][EVENT_CG hide][BG +59][TRANS 1000][BGM +18][lay21 +1028]
    stop music fadeout 1.0
    $ shake_fx()
    $ show_sprites(("s 2 angry",))

    th "Suddenly, I remembered..."

    $ show_sprites(("h 1",))

    voice "ch4.6_h_001"
    h "What's wrong, Saito?"

    voice "ch4.6_h_002"
    h "It's been a while since we last saw each other like this, Louise."

    voice "ch4.6_h_003"
    h "The last time was when the war ended..."

    th "We never got to test whether the way back to our world was real or not."

    th "Well, we'll find another way sometime."

    $ show_sprites(("s 2", "l 1"))

    voice "ch4.6_l_003"
    l "Hey, don't just decide the story yourself!"

    $ show_sprites(("s 2", "l 1 angry"))

    voice "ch4.6_l_004"
    l "You're incredibly rude! The princess is now the queen who supports an entire nation!"

    voice "ch4.6_l_005"
    l "You may be my familiar, but to others you're a commoner. You must be more respectful!"

    voice "ch4.6_l_006"
    l "Otherwise, you'll be charged with insulting the queen, and it will go badly for you!"

    $ show_sprites(("s 2",))

    voice "ch4.6_s_006"
    s "I know.{#ch4.6_d136}"

    stop music fadeout 1.0
    $ show_sprites()
    $ fade_fx("black")

    th "………………{#ch4.6_null_a}"

    $ fade_fx("id(59)", new_music="t27")
    $ show_sprites(("s 2", "h 1"))

    voice "ch4.6_h_004"
    h "By the way, there is another reason I called you all here like this."

    $ show_sprites(("s 2", "l 1"))

    voice "ch4.6_l_007"
    l "Eh... What do you mean!?"

    $ show_sprites(("s 2", "l 1 sad"))

    voice "ch4.6_l_008"
    l "I thought it was because of Haruna!"

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.6_h_005"
    h "No. This is the first I have heard of Miss Haruna."

    $ show_sprites(("s 2", "h 1 angry"))

    voice "ch4.6_h_006"
    h "What I am about to tell you is, in a sense, a grave problem."

    $ show_sprites(("s 2",))

    voice "ch4.6_s_007"
    s "What is this grave problem?"

    $ show_sprites(("s 2", "l 1 angry"))

    voice "ch4.6_l_009"
    l "Saito! How many times must I tell you not to speak so familiarly!"

    voice "ch4.6_l_010"
    l "I am terribly sorry, Your Majesty. The fault is entirely mine as his master..."

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.6_h_007"
    h "Louise, it is fine. Let us speak."

    voice "ch4.6_h_008"
    h "Miss Haruna, Miss Siesta. I am sorry, but could you please excuse us for a moment?"

    $ show_sprites(("s 2", "ha 1"))

    voice "ch4.6_ha_001"
    ha "Yes, of course."

    $ show_sprites(("s 2", "si 1"))

    voice "ch4.6_si_001"
    si "Then, we will take our leave."

    $ show_sprites(("s 2",))
    th "Haruna seemed a bit anxious, but the two of them bowed deeply and left the audience chamber, escorted by the attendants."

    stop music fadeout 1.0
    $ show_sprites()
    $ fade_fx("id(36)", new_music="t27")

    # ==== SCENE 263 ====
    $ show_sprites(("s 2", "h 1"))

    voice "ch4.6_h_009"
    h "Now then, to the main topic."

    voice "ch4.6_h_010"
    h "Recently, there have been rumors of a person called the 'Bomb User' operating in the shadows. Louise, and you, familiar—surely you have heard of them?"

    $ show_sprites(("s 2", "l 1"))

    voice "ch4.6_l_011"
    l "Yes — the other day the academy was attacked too, by someone who looked like the Bomb User."

    $ show_sprites(("s 2", "h 1 angry"))

    voice "ch4.6_h_011"
    h "Is that so... Louise, did you see who that person was?"

    $ show_sprites(("s 2", "l 1 sad"))

    voice "ch4.6_l_012"
    l "Yes... But I could not see their face."

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.6_h_012"
    h "That is unfortunate. We, for our part, are trying to identify the suspect and have conducted an investigation."

    $ show_sprites(("s 2", "h 1 happy"))

    voice "ch4.6_h_013"
    h "As a result, we were able to narrow down the suspects from the characteristics of the perpetrator and the areas where the incidents occurred."

    $ show_sprites(("s 2", "s 2"))

    voice "ch4.6_s_008"
    s "Oh, that's quick. So we just need to find that culprit and bring them to you, right, Princess?"

    $ show_sprites(("s 2", "l 3 angry"))

    voice "ch4.6_l_013"
    l "Hey, don't just decide the story yourself!"

    $ show_sprites(("s 2", "h 1"))

    voice "ch4.6_h_014"
    h "That