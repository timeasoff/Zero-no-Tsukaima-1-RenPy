# Глава 3, часть 2 (сцены 147–157): утро в комнате Луизы — Сиеста уходит
# на работу; ветки расспроса Луизы; кухня — Луиза и Сиеста строит план
# разоблачения «болезни» Харуны; урок в классе; карта выбора локации
# (5 целей → part 3, см. script-ch3_3.rpy).
# Источник: ps2_source/chapters/chapter_04_女の戦い.txt (SCENE 0147–0157).
# Точные аргументы: ps2_source/events_full/chapter_04_女の戦い.txt (SCENE 0147–0157).
# Голоса: ch3.2_si_001…012, ch3.2_l_001…035, ch3.2_s_001…038, ch3.2_ha_001…005.
# Карта: hub-дизайн (зеркало ch2_4) — после каждой локации возврат на карту,
# «Leave» → ch3_2_leave → jump ch3_4. Ключи ch3_2_visited:
# hallway / siesta_hallway / classroom / courtyard / l_room.

default ch3_2_visited = set()

label ch3_2:
    # ==== SCENE 147 ====
    # [BG stage image=+10] louise_room, [TRANS crossfade], [BGM play=+31] → t30
    $ fade_fx("louise_room", new_music="t30")
    $ show_sprites("si 1")

    voice "ch3.2_si_001"
    si "Well then, Miss Valiere. Haruna-san, I have work to do, so I'll be going on ahead."

    $ show_sprites(("l 1 happy", "si 1"))

    voice "ch3.2_l_001"
    l "All right. Give it your all at work."

    voice "ch3.2_si_002"
    si "Then, if you'll excuse me."

    # [SE se0 play=+57] — дверь открывается
    play sound open_door
    $ show_sprites(("l 1 happy", "si 1", "s 1"))

    voice "ch3.2_s_001"
    s "Ah, Siesta — you're off to work?"

    voice "ch3.2_si_003"
    si "Ah, Saito-san. Pardon me."

    voice "ch3.2_s_002"
    s "Good luck at work!"

    $ show_sprites(("l 1 happy", "si 1 happy", "s 1"))

    voice "ch3.2_si_004"
    si "Yes, I will. Well then."

    # [SE se0 play=+56] — дверь закрывается, Сиеста уходит
    play sound close_door
    $ show_sprites(("l 1", "s 1"))

    voice "ch3.2_l_002"
    l "Saito, I'm sorry for making you go outside."

    voice "ch3.2_s_003"
    s "Louise, don't worry about it."

    $ show_sprites(("l 1", "s 3 shy"))

    voice "ch3.2_s_004"
    s "I'm actually kind of happy — I was thinking you might be starting to see me as a man."

    $ show_sprites(("l 3", "s 3 shy"))

    voice "ch3.2_l_003"
    l "I wasn't thinking anything of the sort. Propriety, that's all — propriety!"

    $ show_sprites(("l 3", "s 3 sad"))

    voice "ch3.2_s_005"
    s "Sure, sure. Is that so…"

    $ show_sprites(("l 3", "s 1"))

    voice "ch3.2_s_006"
    s "Come to think of it, Haruna — how are you feeling?"

    $ show_sprites(("l 3", "s 1", "ha 3"))

    voice "ch3.2_ha_001"
    ha "Yeah, I'm fine. Sorry for making you worry, Hiraga-kun."

    voice "ch3.2_s_007"
    s "Glad to hear it… Don't push yourself. There are no classes anyway, so take it easy."

    $ show_sprites(("l 3", "s 1", "ha 3 shy"))

    voice "ch3.2_ha_002"
    ha "Yeah… Thanks."

    $ show_sprites(("l 1", "s 1"))

    voice "ch3.2_l_004"
    l "Uuuugh."

    voice "ch3.2_s_008"
    s "What's wrong, Louise?"

    # ==== CHOISE (scene 147) ====
    # select: 148 / 149 / 150 → все ветки сходятся в ch3_151
    menu:
        "Are you feeling under the weather?{#ch3_m147a}":
            # ==== SCENE 148 ====
            $ show_sprites(("l 1", "s 1 sad"))

            voice "ch3.2_s_009"
            s "Are you feeling under the weather?"

            $ show_sprites(("l 1 angry", "s 1 sad"))

            voice "ch3.2_l_005"
            l "O-of course not! I was just humming a little."

            $ show_sprites(("l 1 angry", "s 1"))

            voice "ch3.2_s_010"
            s "You wouldn't just hum for no reason, right?"

            $ show_sprites(("l 1", "s 1"))

            voice "ch3.2_l_006"
            l "I'm fine, don't worry about it."

            voice "ch3.2_s_011"
            s "Well, all right… If you're feeling sick, say so right away, okay?"

            $ show_sprites(("l 1 shy", "s 1"))

            voice "ch3.2_l_007"
            l "I get it!"
            # [好感度] ルイズ +10
            $ update_sympathy(10, char_key="louise")

            jump ch3_151

        "Are you sleepy?{#ch3_m147b}":
            # ==== SCENE 149 ====
            $ show_sprites(("l 1", "s 1"))

            voice "ch3.2_s_012"
            s "Are you sleepy?"

            $ show_sprites(("l 1 angry", "s 1"))

            voice "ch3.2_l_008"
            l "How do you figure?"

            $ show_sprites(("l 1 angry", "s 3 sad"))

            voice "ch3.2_s_013"
            s "Nah. Just a feeling."

            $ show_sprites(("l 1", "s 3 sad"))

            voice "ch3.2_l_009"
            l "Don't go deciding how someone feels just on a whim."
            # [好感度] ルイズ -10
            $ update_sympathy(-10, char_key="louise")

            $ show_sprites(("l 1", "s 1"))

            voice "ch3.2_s_014"
            s "Yeah, yeah.{#ch3.2_s_014}"

            jump ch3_151

        "Are you hungry?{#ch3_m147c}":
            # ==== SCENE 150 ====
            $ show_sprites(("l 1", "s 1 sad"))

            voice "ch3.2_s_015"
            s "Are you hungry? It's still a while until lunch."

            $ show_sprites(("l 1 angry", "s 1 sad"))

            voice "ch3.2_l_010"
            l "It's not like I'm starving like you. Don't lump me in with you!"
            # [好感度] ルイズ -20
            $ update_sympathy(-20, char_key="louise")

            $ show_sprites(("l 1 angry", "s 1"))

            voice "ch3.2_s_016"
            s "I see, I see."

            jump ch3_151

label ch3_151:
    # ==== SCENE 151 ====
    # фон/музыка не меняются (bгm +31 → t30 уже играет); RESET нормализует
    $ show_sprites(("l 3", "s 1"))

    voice "ch3.2_l_011"
    l "Well then, I've got things to do, so I'm heading out first. Saito, come to the classroom after."

    $ show_sprites(("l 3", "s 3 sad"))

    voice "ch3.2_s_017"
    s "Huh? Why?{#ch3.2_s_017}"

    $ show_sprites(("l 1 angry", "s 3 sad"))

    voice "ch3.2_l_012"
    l "…A-anyway, you don't have to come, Saito!"

    $ show_sprites(("l 1 angry", "s 1 sad"))

    voice "ch3.2_s_018"
    s "That's not even a reason."

    $ show_sprites(("l 3 angry", "s 1 sad"))

    voice "ch3.2_l_013"
    l "And you, Haruna! You're a patient, so you'd better stay put and rest, okay!?"

    # Луиза уходит: [SPRITE lay1/lay5 hide] + [SE se0 play=+57]
    # (waitSEStop не портируется — нереализуемый вызов)
    play sound open_door
    $ show_sprites("ha 3 sad")

    voice "ch3.2_ha_003"
    ha "Y-yes…"

    $ show_sprites(("ha 3 sad", "s 1"))

    voice "ch3.2_s_019"
    s "Louise — she's worried about Haruna, in her own way, isn't she."

    voice "ch3.2_ha_004"
    ha "Do you think so…"

    $ show_sprites(("ha 3 sad", "s 3 sad"))

    voice "ch3.2_s_020"
    s "Hm? Did you say something just now?"

    $ show_sprites(("ha 3", "s 3 sad"))

    voice "ch3.2_ha_005"
    ha "Nope, nothing."

    $ show_sprites(("ha 3", "s 1"))

    voice "ch3.2_s_021"
    s "Still — what do you suppose Louise is up to?"

    jump ch3_152

label ch3_152:
    # ==== SCENE 152 ====
    # [SE se1 stop] / [BGM stop=1000] / [BG stage hide] сведены в переход;
    # [BG stage image=+32] kitchen, [BGM play=+30] → t29
    $ fade_fx("kitchen", new_music="t29")
    $ show_sprites(("l 1 angry", "si 1"))

    voice "ch3.2_l_014"
    l "Grr, this is no fun! For all that he's my familiar, all he does is fuss over Haruna!!"

    voice "ch3.2_l_015"
    l "Siesta, you think so too, right?"

    $ show_sprites(("l 1 angry", "si 1 sad"))

    voice "ch3.2_si_005"
    si "Y-yes… It's not fair of Haruna-san to fake an illness and have Saito-san fuss over her."

    $ show_sprites(("l 1 angry", "si 4 shy"))

    voice "ch3.2_si_006"
    si "But maybe I'm a little happy about it. Thanks to that I got to sleep next to Saito-san… …Hehe."

    $ show_sprites(("l 1", "si 4 shy"))

    voice "ch3.2_l_016"
    l "Eh? Did you say something?"

    $ show_sprites(("l 1", "si 1"))

    voice "ch3.2_si_007"
    si "No, nothing…"

    $ show_sprites(("l 1 angry", "si 1"))

    voice "ch3.2_l_017"
    l "Unforgivable~! Saito didn't have to get taken in by Haruna's little feigned illness like that!!"

    voice "ch3.2_si_008"
    si "Miss Valiere. I believe we should make Haruna-san confess that she's faking."

    $ show_sprites(("l 1", "si 1"))

    voice "ch3.2_l_018"
    l "But wouldn't it be faster if we just told Saito ourselves?"

    $ show_sprites(("l 1", "si 1 sad"))

    voice "ch3.2_si_009"
    si "Do you think so? In the end, it's someone else's illness. There's no way others could tell."

    $ show_sprites(("l 3 happy", "si 1 sad"))

    voice "ch3.2_l_019"
    l "Then we'll just use magic. There's bound to be a perfect spell."

    $ show_sprites(("l 3 happy", "si 4 happy"))

    voice "ch3.2_si_010"
    si "Um, Miss Valiere — if it's all right, I have a good idea…"

    $ show_sprites(("l 1 happy", "si 4 happy"))

    voice "ch3.2_l_020"
    l "Eh? What is it, what is it!?"

    $ show_sprites(("l 1 happy", "si 1"))

    voice "ch3.2_si_011"
    si "What if we…….……how does that sound?"

    $ show_sprites(("l 3 happy", "si 1"))

    voice "ch3.2_l_021"
    l "…I like that! All right, let's do it!"

    voice "ch3.2_si_012"
    si "Then I'll get things ready later…"

    $ show_sprites(("l 1 happy", "si 1"))

    voice "ch3.2_l_022"
    l "Nfufufufu… Just you watch, Haruna! I'll expose your fake illness completely, I swear it~!!"

    jump ch3_153

label ch3_153:
    # ==== SCENE 153 ====
    # [SE se1 stop] / [BGM stop=1000] / [BG stage hide] сведены в переход;
    # [BG stage image=+23] classroom, [BGM play=+32] → t31
    $ fade_fx("classroom", new_music="t31")

    th "As always, I have no idea what the lesson's about."

    th "Nobles who sit through lessons like this every day really have it tough. Well, I mostly sleep through it myself, but…"

    th "But Louise seems to be enjoying today's lesson an awful lot. Did something fun happen or what?"

    $ show_sprites("l 1")

    voice "ch3.2_l_023"
    l "…Hm? What's with the gawking? Is there something on my face?"

    $ show_sprites(("l 1", "s 1"))

    voice "ch3.2_s_022"
    s "No, it's just — you seem to be enjoying the lesson more than usual today. Did something fun happen?"

    $ show_sprites(("l 1 angry", "s 1"))

    voice "ch3.2_l_024"
    l "Ghk. N-nothing at all!"

    $ show_sprites(("l 1 angry", "s 3 sad"))

    voice "ch3.2_s_023"
    s "Really? You're really not hiding anything from me?"

    $ show_sprites(("l 1", "s 3 sad"))

    voice "ch3.2_l_025"
    l "I-I'm not hiding anything."

    $ show_sprites(("l 1", "s 1"))

    voice "ch3.2_l_026"
    l "Besides, Saito — you're the one who's dying to know how Haruna is, aren't you!?"

    voice "ch3.2_s_024"
    s "What's with you, Louise? Bringing up Haruna out of nowhere…"

    # ==== CHOISE (scene 153) ====
    # select: 154 / 155 / 156 → все ветки сходятся в ch3_157
    menu:
        "Well, she's probably fine, right?{#ch3_m153a}":
            # ==== SCENE 154 ====
            $ show_sprites(("l 1", "s 3 sad"))

            voice "ch3.2_s_025"
            s "I mean… she's probably fine."

            $ show_sprites(("l 1 happy", "s 3 sad"))

            voice "ch3.2_l_027"
            l "Eh, Saito — do you really mean that?"
            # [好感度] ルイズ +10
            $ update_sympathy(10, char_key="louise")

            $ show_sprites(("l 1 happy", "s 1"))

            voice "ch3.2_s_026"
            s "What's there to be serious about? She's sleeping in your room, so there's no problem, right?"

            voice "ch3.2_s_027"
            s "Besides, Siesta said she'd look after her whenever she has free time…"

            $ show_sprites(("l 1 sad", "s 1"))

            voice "ch3.2_l_028"
            l "W-well, when you put it that way… Maybe she'll be fine."

            jump ch3_157

        "I'm a little worried, I guess.{#ch3_m153b}":
            # ==== SCENE 155 ====
            $ show_sprites(("l 1", "s 3 sad"))

            voice "ch3.2_s_028"
            s "Well, yeah, I'm a little worried. She's laid up sick, after all."

            $ show_sprites(("l 1 angry", "s 3 sad"))

            voice "ch3.2_l_029"
            l "Muuu…"

            $ show_sprites(("l 1 angry", "s 1"))

            voice "ch3.2_s_029"
            s "But it doesn't seem like a life-threatening illness, and I figure she'll get better with rest — so I'm not that worried."

            $ show_sprites(("l 1", "s 1"))

            voice "ch3.2_l_030"
            l "Eh, is that so?"

            voice "ch3.2_s_030"
            s "Yeah — no matter how much I worry, it's not going to make her recover any faster."

            $ show_sprites(("l 1", "s 1 sad"))

            voice "ch3.2_s_031"
            s "Still, I'd like her to get better soon, if she can."

            $ show_sprites(("l 1 angry", "s 1 sad"))

            voice "ch3.2_l_031"
            l "…{#ch3.2_l_031}"

            $ show_sprites(("l 1 angry", "s 1"))

            voice "ch3.2_s_032"
            s "Hm? What's wrong, glaring at me like that?"

            $ show_sprites(("l 1", "s 1"))

            voice "ch3.2_l_032"
            l "I'm not glaring or anything…"
            # [好感度] ルイズ -10
            $ update_sympathy(-10, char_key="louise")

            jump ch3_157

        "Yeah, it does bug me.{#ch3_m153c}":
            # ==== SCENE 156 ====
            $ show_sprites(("l 1", "s 1"))

            voice "ch3.2_s_033"
            s "Yeah… you're right, it does bug me."

            $ show_sprites(("l 1 angry", "s 1"))

            voice "ch3.2_l_033"
            l "Mmm…"

            $ show_sprites(("l 1 angry", "s 3"))

            voice "ch3.2_s_034"
            s "To Haruna, I'm the only person she knows in this world — I've got to look after her."

            $ show_sprites(("l 1 angry", "s 1"))

            voice "ch3.2_s_035"
            s "But I know I'm being a nuisance to you and Siesta, and I'm sorry about that."

            $ show_sprites(("l 1 shy", "s 1"))

            voice "ch3.2_l_034"
            l "U-um… That part's fine, I don't really mind…"

            jump ch3_157

label ch3_157:
    # ==== SCENE 157 ====
    # фон/музыка не меняются (bгm +32 → t31 уже играет)
    $ show_sprites(("l 1 sad", "s 1 sad"))

    voice "ch3.2_s_036"
    s "Hm? What's wrong? Did I say something that bothered you?"

    $ show_sprites(("l 1 sad", "s 1 sad"))

    voice "ch3.2_l_035"
    l "Nope, you didn't say anything."

    # Конец урока: [msgoff] + [BG stage hide] + повторный [TRANS crossfade]
    # того же фона (сцена 23) — пауза во времени
    $ show_sprites(None)
    $ fade_fx("classroom")

    $ show_sprites("s 1")

    voice "ch3.2_s_037"
    s "Oh, class is over. Now then, Louise— hm?"

    $ show_sprites("s 3 sad")

    voice "ch3.2_s_038"
    s "Huh? Where did Louise go? She up and ditched me without saying a word…"

    th "Now then, what should I do…"

    # [BGM stop=1000] перед картой (moveInit)
    stop music fadeout 1.0
    jump ch3_2_map

label ch3_2_map:
    # ==== SCENE 157 → 【移動】====
    # 5 целей PS2 (moveItem): 廊下→1297, 廊下→1302, 教室→1307, 中庭→1312,
    # ルイズの部屋→1317; плюс «Leave» (шаблон ch2_4) → ch3_2_leave → ch3_4.
    $ choices = []
    if "hallway" not in ch3_2_visited:
        $ choices.append({"char": "louise", "text": "Hallway{#ch3.2.hallway}", "target": "hallway_ch3_3"})
    if "siesta_hallway" not in ch3_2_visited:
        $ choices.append({"char": "siesta", "text": "Hallway{#ch3.2.siesta}", "target": "siesta_hallway_ch3_3"})
    if "classroom" not in ch3_2_visited:
        $ choices.append({"char": "kirche", "text": "Classroom", "target": "classroom_ch3_3"})
    if "courtyard" not in ch3_2_visited:
        $ choices.append({"char": "tabitha", "text": "Courtyard", "target": "courtyard_ch3_3"})
    if "l_room" not in ch3_2_visited:
        $ choices.append({"char": "haruna", "text": "Louise's Room{#ch3.2.lroom}", "target": "l_room_ch3_3"})
    $ choices.append({"text": "Leave", "target": "ch3_2_leave"})
    $ sprite_choice(choices)
    jump ch3_2_map
    return

label ch3_2_leave:
    jump ch3_4
