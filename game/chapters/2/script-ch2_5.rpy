# Глава 2, часть 5 (сцены 115–120 + карта перемещения round 2):
# ужин в комнате Луизы (CG155/157), выбор 116/117, совет в комнате Сиесты
# (сцена 119, CG109), прощание с Харуной (120) → ch2_5_map → локации 1281–1296.
# Источник: ps2_source/chapters/chapter_03_黒髪の来訪者.txt (scene 0115…0120)
# Точные аргументы: ps2_source/events_full/chapter_03_黒髪の来訪者.txt (SCENE 0115…0120)
# Сцены 121–124 — редиректы движка (0 реплик), не портируются.
# Локации round 2 (1281–1296) — в script-ch2_5b.rpy.

default ch2_5_visited = set()

label ch2_5:
    # ==== SCENE 115 ====
    $ fade_fx("louise_room_night", new_music="t19", sprites="s 1 sad")

    voice "ch2.5_s_176"
    s "Louise... What happened, anyway?"

    $ show_sprites(("si 4 sad", "s 1 sad"))
    voice "ch2.5_si_025"
    si "……。{#ch2.5_si14594}"

    $ fade_fx("ha_sick_3", type="cg")
    ha "……。{#ch2.5_ha115}"

    $ fade_fx("louise_room_night", sprites=("si 4 sad", "s 3 sad"))
    voice "ch2.5_s_177"
    s "U-um... Did I do something wrong?"

    $ show_sprites(("si 1", "s 3 sad"))
    voice "ch2.5_si_026"
    si "I'll be going now."

    $ show_sprites(("si 1", "s 1 sad"))
    voice "ch2.5_s_178"
    s "Go...?"

    voice "ch2.5_si_027"
    si "To look for Miss Vallière... I think it would be better if I spoke with her rather than Saito-san."

    voice "ch2.5_si_028"
    si "I'll find her and bring her back. You wait here, Saito-san."

    $ show_sprites(("s 1 sad",))
    voice "ch2.5_s_179"
    s "Ah, Siesta..."

    play sound open_door
    play sound close_door
    $ show_sprites(("s 3 sad",))
    voice "ch2.5_s_180"
    s "Well then, maybe I should go look for Louise too... Siesta told me to stay, but somehow I feel like this is my fault too..."

    $ fade_fx("ha_sick_3", type="cg")
    voice "ch2.5_ha_033"
    ha "Wait!"

    voice "ch2.5_s_181"
    s "Haruna?"

    voice "ch2.5_ha_034"
    ha "Don't go, Hiraga-kun. Don't leave me all alone..."

    voice "ch2.5_s_182"
    s "Haruna...{#ch2.5_s11175}"

    menu:
        "Chase after Siesta{#ch2.5_m115a}":
            jump ch2_5_chase
        "Stay by Haruna's side{#ch2.5_m115b}":
            jump ch2_5_stay

label ch2_5_chase:
    # ==== SCENE 116 ====
    voice "ch2.5_ha_035"
    ha "You're going to leave me behind...? All alone again..."

    $ update_sympathy(-10, char_key="haruna")

    voice "ch2.5_s_183"
    s "Haruna...{#ch2.5_s11176}"

    th "I'm worried about Louise. That idiot definitely misunderstood something, got in a huff, and blew up."

    th "But... I can't leave Haruna all alone right now... can I?"

    jump ch2_5_dinner

label ch2_5_stay:
    # ==== SCENE 117 ====
    voice "ch2.5_ha_036"
    ha "Hiraga-kun, you're not going, right? You won't disappear on me again?"

    voice "ch2.5_s_184"
    s "I told you, I won't disappear. Don't worry, just calm down."

    $ fade_fx("ha_sick_2", type="cg", new_music="t21")

    voice "ch2.5_ha_037"
    ha "Thank goodness..."

    $ update_sympathy(10, char_key="haruna")

    th "Ever since I came to this world, I haven't had a single acquaintance, or anyone willing to help me."

    th "So having me around — someone she already knows — must really matter that much."

    $ fade_fx("ha_sick_3", type="cg", new_music="t19")

    jump ch2_5_dinner

label ch2_5_dinner:
    # ==== SCENE 118 ====
    voice "ch2.5_s_185"
    s "Got it. I'm not going anywhere. Anyway, let's hurry up and finish dinner."

    voice "ch2.5_ha_038"
    ha "O-oh. Right..."

    th "I'll leave Louise to Siesta for now. She'll probably be fine."

    voice "ch2.5_ha_039"
    ha "Hiraga-kun, what's wrong?"

    voice "ch2.5_s_186"
    s "Hm? No, it's nothing."

    jump ch2_5_council

label ch2_5_council:
    # ==== SCENE 119 ====
    $ fade_fx("si_room_night", new_music="t27", sprites=("l 1 sad",))

    voice "ch2.5_l_020"
    l "...What am I even thinking? I don't even know myself."

    voice "ch2.5_l_021"
    l "Saito didn't do anything wrong in the first place... and I still went and said that. I'm really the worst..."

    $ show_sprites(("l 1 angry",))
    voice "ch2.5_l_022"
    l "Even so, the way that girl Haruna talked rubbed me the wrong way."

    voice "ch2.5_l_023"
    l "Being from the same world as Saito means she's a commoner."

    voice "ch2.5_l_024"
    l "I couldn't forgive a commoner speaking to me like that... but still..."

    $ show_sprites(("l 1 sad",))
    voice "ch2.5_l_025"
    l "That's no reason to go and make such a fool of myself, though... How am I even supposed to face them when I get back..."

    play sound open_door

    voice "ch2.5_l_026"
    l "……？{#ch2.5_l5865}"

    $ show_sprites(("l 1 sad", "si 1"))
    play sound close_door

    voice "ch2.5_si_029"
    si "Miss Vallière. So you were here. I've been looking everywhere for you."

    $ show_sprites(("l 3 angry", "si 1"))
    voice "ch2.5_l_027"
    l "Siesta... W-what do you want, commoner?"

    voice "ch2.5_si_030"
    si "I had Saito-san wait in his room. It's only me and Miss Vallière here — no one else will hear us."

    $ show_sprites(("l 3", "si 1"))
    voice "ch2.5_l_028"
    l "Huh...?{#ch2.5_l5867}"

    voice "ch2.5_si_031"
    si "Miss Vallière. I understand how you feel."

    $ show_sprites(("l 3 sad", "si 1"))
    voice "ch2.5_l_029"
    l "W-what are you talking about?"

    $ show_sprites(("l 3 sad", "si 1 sad"))
    voice "ch2.5_si_032"
    si "Right now, since Haruna showed up, Saito-san thinks about nothing but her..."

    $ show_sprites(("l 3 sad", "si 1 angry"))
    voice "ch2.5_si_033"
    si "No, even that's putting it too strongly — but right now he's putting Haruna first of all."

    $ show_sprites(("l 3 sad", "si 1 sad"))
    voice "ch2.5_si_034"
    si "Of course, I know that's just Saito-san's kindness at heart."

    $ show_sprites(("l 1 sad", "si 1 sad"))
    voice "ch2.5_l_030"
    l "……。{#ch2.5_l5869}"

    $ show_sprites(("l 1 sad", "si 1"))
    voice "ch2.5_si_035"
    si "However you look at it, I'm certain Haruna has feelings for Saito-san."

    voice "ch2.5_si_036"
    si "If this goes on, Haruna will take Saito-san away from us. No — if it were only that, it would still be fine, but..."

    $ show_sprites(("l 1 sad", "si 1 sad"))
    voice "ch2.5_si_037"
    si "At worst, he might leave the academy with Haruna to look for a way back to the original world."

    $ show_sprites(("l 1 sad", "si 1"))
    voice "ch2.5_si_038"
    si "Miss Vallière, let me be blunt. Shall we join forces — just for now?"

    $ show_sprites(("l 1", "si 1"))
    voice "ch2.5_l_031"
    l "I understand what you're saying. But I think it's absurd for a commoner to be giving me orders."

    $ show_sprites(("l 1", "si 1 sad"))
    voice "ch2.5_si_039"
    si "Miss Vallière. I don't intend to meddle with your creed, but things aren't that forgiving right now."

    $ show_sprites(("l 1 sad", "si 1 sad"))
    voice "ch2.5_l_032"
    l "……。{#ch2.5_l5871}"

    voice "ch2.5_si_040"
    si "Haruna is from the same world as Saito-san."

    voice "ch2.5_l_033"
    l "Th-that's true, but..."

    voice "ch2.5_si_041"
    si "Saito-san won't say it, but I'm sure he's homesick even now."

    voice "ch2.5_si_042"
    si "And for Saito-san like that, Haruna is his hometown."

    voice "ch2.5_si_043"
    si "I'm sure he must have special feelings for Haruna."

    $ show_sprites(("l 1 sad", "si 1 angry"))
    voice "ch2.5_si_044"
    si "And what's worse, Haruna senses her hometown in Saito-san too. And she's trying to use it."

    $ show_sprites(("l 3 angry", "si 1 angry"))
    voice "ch2.5_l_034"
    l "U-use!?"

    $ show_sprites(("l 3 angry", "si 1"))
    voice "ch2.5_si_045"
    si "For example, Haruna's illness. It had probably already healed by nighttime."

    $ show_sprites(("l 3", "si 1"))
    voice "ch2.5_l_035"
    l "Really?{#ch2.5_l5874}"

    voice "ch2.5_si_046"
    si "Yes, really. I'll grant she really was in bad shape that morning."

    voice "ch2.5_si_047"
    si "But I've been watching her, and an illness so severe she can't leave bed — no matter how you look at it, that's a lie."

    $ show_sprites(("l 3 angry", "si 1"))
    voice "ch2.5_l_036"
    l "...So then what? You're saying that girl is using a fake illness to exploit Saito's kindness?"

    voice "ch2.5_si_048"
    si "Exactly. Honest, kind, and easy to fool — Saito-san hasn't noticed it."

    $ show_sprites(("l 3 sad", "si 1"))
    voice "ch2.5_l_037"
    l "That's a rather barbed way to put it..."

    voice "ch2.5_si_049"
    si "Haruna has been using the fake illness to monopolize Saito-san even more."

    voice "ch2.5_si_050"
    si "I believe she saw the relationship between us and Saito-san, and decided to make her move."

    voice "ch2.5_si_051"
    si "If we leave this alone, it's exactly what Haruna wants."

    $ show_sprites(("l 3 happy", "si 1"))
    voice "ch2.5_l_038"
    l "F-fufu... To think she expected such behavior to be allowed in my room..."

    $ show_sprites(("l 3 angry", "si 1"))
    voice "ch2.5_l_039"
    l "She's really got some nerve, hasn't she."

    $ fade_fx("id(109)", type="cg", new_music="t24")

    voice "ch2.5_l_040"
    l "Fine. Let's call a truce — only until I've put that wicked girl in her place."

    voice "ch2.5_si_052"
    si "Then the alliance is formed."

    voice "ch2.5_k_038"
    k "You're always doing something amusing, aren't you?"

    $ fade_fx("si_room_night", new_music="t29", sprites=("l 3 angry", "k 1 happy"))
    voice "ch2.5_l_041"
    l "Kirche! Why are you here!?"

    voice "ch2.5_k_039"
    k "Oh, I'm not the only one."

    $ show_sprites(("l 3 angry", "t 1"))
    voice "ch2.5_t_026"
    t "...I just happened to drop by."

    $ show_sprites(("l 1 angry", "t 1"))
    voice "ch2.5_l_042"
    l "T-Tabitha!"

    $ show_sprites(("l 1 angry", "k 1 happy"))
    voice "ch2.5_k_040"
    k "Honestly, I just happened to pass by. And with Darling involved, I ended up listening to the whole thing."

    voice "ch2.5_l_043"
    l "O-oh no, you don't mean..."

    $ show_sprites(("l 1 angry", "k 1"))
    voice "ch2.5_k_041"
    k "Don't misunderstand me. I'm saying I'll help."

    $ show_sprites(("si 1 sad", "k 1"))
    voice "ch2.5_si_053"
    si "Miss Zerbst?"

    voice "ch2.5_k_042"
    k "I won't get in your way. And of course, I'll keep it quiet from Darling and Haruna."

    $ show_sprites(("si 1 sad", "k 1 happy"))
    voice "ch2.5_k_043"
    k "In return, though, I get to observe. How about it?"

    $ show_sprites(("l 1", "k 1 happy"))
    voice "ch2.5_l_044"
    l "I have my serious doubts about how much protection I'd get. Understood."

    voice "ch2.5_k_044"
    k "Then do your best for me too. Good night."

    $ show_sprites(("l 1", "t 1"))
    voice "ch2.5_t_027"
    t "...Good night."

    $ fade_fx("id(109)", type="cg")

    voice "ch2.5_l_045"
    l "For now, let's put off the strategy meeting. I won't let Haruna keep putting on airs."

    voice "ch2.5_si_054"
    si "Yes, Miss Vallière! For Saito-san's sake too!"

    voice "ch2.5_l_046"
    l "S-Saito has nothing to do with it! He never gives a thought to his master! About that stupid familiar..."

    voice "ch2.5_si_055"
    si "R-right..."

    jump ch2_5_after

label ch2_5_after:
    # ==== SCENE 120 ====
    $ fade_fx("ha_sick_3", type="cg", new_music="t10")

    voice "ch2.5_ha_040"
    ha "Thank you for the meal."

    voice "ch2.5_s_187"
    s "I'll take the dishes. Haruna, you rest now."

    voice "ch2.5_ha_041"
    ha "O-okay. Thank you, Hiraga-kun."

    voice "ch2.5_s_188"
    s "Nah, it's nothing."

    th "Still, those two are taking their sweet time coming back..."

    th "I wonder if Siesta can't find Louise?"

    th "Or maybe it's Louise — she's stubborn in the oddest ways... She might not be able to make herself come back."

    voice "ch2.5_ha_042"
    ha "Hiraga-kun, what's wrong? You're spacing out."

    voice "ch2.5_s_189"
    s "...Guess there's no helping it."

    voice "ch2.5_ha_043"
    ha "Hiraga-kun?"

    voice "ch2.5_s_190"
    s "Sorry. I'm just stepping out for a bit."

    voice "ch2.5_ha_044"
    ha "Where are you going?"

    voice "ch2.5_s_191"
    s "To look for Louise."

    voice "ch2.5_ha_045"
    ha "Even if you don't go yourself, Hiraga-kun — Louise-san will be right back, won't she? It looked like Siesta went to meet her."

    voice "ch2.5_s_192"
    s "No, she won't. My master is one stubborn customer."

    voice "ch2.5_s_193"
    s "If I don't go meet her myself, she can't bring herself to come back straight. What a troublesome girl."

    voice "ch2.5_s_194"
    s "I'll be right back, so don't worry. Now get some rest."

    play sound open_door
    play sound close_door

    voice "ch2.5_ha_046"
    ha "...Sigh. Why is Hiraga-kun so kind to everyone, anyway?"

    $ fade_fx("hallway_night", new_music="t19", sprites="s 1")

    th "Well then. I said all that, but where did Louise run off to?"

    jump ch2_5_map

label ch2_5_map:
    # Выбор локации round 2 (【移動】 после сцены 120): цель Leave по moveInit —
    # сцена 125 (jump ch2_6). Контент локаций (сцены 1281–1296) —
    # в script-ch2_5b.rpy; после визита локация убирается из карты.
    $ choices = []
    if "l_room" not in ch2_5_visited:
        $ choices.append({"char": "haruna", "text": "Louise's Room{#ch2.5_lroom}", "target": "l_room_ch2_5"})
    if "kirche_room" not in ch2_5_visited:
        $ choices.append({"char": "kirche", "text": "Kirche's Room{#ch2.5_kroom}", "target": "kirche_room_ch2_5"})
    if "tabitha_room" not in ch2_5_visited:
        $ choices.append({"char": "tabitha", "text": "Tabitha's Room", "target": "tabitha_room_ch2_5"})
    if "corridor" not in ch2_5_visited:
        $ choices.append({"text": "Hallway{#ch2.5_hallway}", "target": "corridor_ch2_5"})
    $ choices.append({"text": "Leave{#ch2.5_leave}", "target": "ch2_5_leave"})
    $ sprite_choice(choices)
    jump ch2_5_map
    return

label ch2_5_leave:
    jump ch2_6
