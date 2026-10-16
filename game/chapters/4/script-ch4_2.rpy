# Глава 4, часть 2 (сцены 225–235 + дата 1342–1346): утро в комнате Луизы
# (переполох вокруг Харуны, Сиесте велено остаться), карта-хаб 【移動】
# с датами (Луиза/Сиеста/Кирхе/Табита/Харуна), проводы у кареты и выбор,
# рядом с кем сесть. Вход — jump ch4_2 из script-ch4_1.rpy; выход — jump ch4_3.
# Источник: ps2_source/chapters/chapter_05_トリスタニアの危機.txt (SCENE 225–235,
# 1342–1346, дата Луизы).
# Точные аргументы: ps2_source/events_full/chapter_05_トリスタニアの危機.txt.
# Голоса: ch4.2_<spk>_001… (125).
# Без голоса: мысли Сайто ×8 (225 ×1, 231 ×2, 232 ×1, 234 ×1, 235 ×1,
#         1342 ×1, 1346 ×1) — th-строки без voice.
# SE (se0 +57 в 1342, se1 +44 в 1347 — вне части, se1 stop) — не портируются.
# CG 123/120/121 (сцена 231) — заглушки id(123)/id(120)/id(121).
# 【移動】 (сцена 225): 5 пунктов-дат → date_louise_ch4_2 / date_siesta_ch4_2 /
#   date_kirche_ch4_2 / date_tabitha_ch4_2 / date_haruna_ch4_2; leave-цель
#   moveInit = сцена 231. После визита локация убирается из карты (как ch2_4_map).
#   Портреты пунктов — из char_data (ha 1 вместо ha 2 источника; PROVISIONAL).
# Сцены 226–230 — служебные заглушки карты (next → 1342/1347/…); не портируются.
# Спрайты: +2 регистрации блока «ha 2» — 962 = ha 2, 968 = ha 2 sad.

default ch4_2_visited = set()

label ch4_2:
    # ==== SCENE 225 ====
    # [BG +10 (louise_room)][TRANS][BGM play=+19 → t18][lay1 +308 (l 1 sad)]
    $ fade_fx("louise_room", new_music="t18", sprites=("l 1 sad",))

    voice "ch4.2_l_001"
    l "I feel strangely heavy-hearted. To be summoned so suddenly. Whatever could it be about?"

    # [lay1 x=-96 — сдвиг][lay5 +390 (s 1)]
    $ show_sprites(("l 1 sad", "s 1"))

    voice "ch4.2_s_001"
    s "If even the Headmaster doesn't know, then maybe it's some private matter she wants to discuss with you?"

    # [lay1 +302 (l 1)]
    $ show_sprites(("l 1", "s 1"))

    voice "ch4.2_l_002"
    l "That can't be. Her Highness wouldn't go out of her way to summon me over something personal."

    # [lay5 hide][lay1 hide][lay2 +489 (si 1)]
    $ show_sprites(("si 1",))

    voice "ch4.2_si_001"
    si "Um… Everyone, what exactly was that discussion about?"

    # [lay2 hide][lay1 +302 (l 1)][lay5 +390 (s 1)]
    $ show_sprites(("l 1", "s 1"))

    voice "ch4.2_s_002"
    s "Ah, Louise — is it all right if I tell Siesta what we talked about earlier?"

    voice "ch4.2_l_003"
    l "It's fine, isn't it? She'll find out soon enough anyway."

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("l 1", "s 3 sad"))

    voice "ch4.2_s_003"
    s "You see, Her Highness summoned me and Louise. And it turns out we're going to Tristania."

    # [lay5 hide][lay2 +493 (si 1 angry)] — lay1 (l 1) остаётся на экране
    $ show_sprites(("l 1", "si 1 angry"))

    voice "ch4.2_si_002"
    si "Wh-what, to Her Majesty the Queen!?"

    # [lay1 +335 (l 3)]
    $ show_sprites(("l 3", "si 1 angry"))

    voice "ch4.2_l_004"
    l "H-hey, you're too loud. Listen, this is a secret just between us."

    # [lay2 +489 (si 1)]
    $ show_sprites(("l 3", "si 1"))

    voice "ch4.2_si_003"
    si "Yes, understood.{#ch4.2_si_003}"

    # [lay1 hide][lay5 +390 (s 1)]
    $ show_sprites(("si 1", "s 1"))

    voice "ch4.2_s_004"
    s "And on top of that, the Headmaster asked me to introduce Haruna to Her Highness, so Haruna's coming along too."

    # [lay2 +495 (si 1 sad)]
    $ show_sprites(("si 1 sad", "s 1"))

    voice "ch4.2_si_004"
    si "Is that so…"

    # [lay5 hide][lay2 hide][lay7 +957 (ha 1 sad)]
    $ show_sprites(("ha 1 sad",))

    voice "ch4.2_ha_001"
    ha "Um… Louise-san."

    # [lay7 x=224 — сдвиг][lay1 +302 (l 1)]
    $ show_sprites(("ha 1 sad", "l 1"))

    voice "ch4.2_l_005"
    l "What is it, Haruna?{#ch4.2_l_005}"

    # [lay7 +951 (ha 1)]
    $ show_sprites(("ha 1", "l 1"))

    voice "ch4.2_ha_002"
    ha "Louise-san, are you acquainted with Her Majesty the Queen?"

    # [lay1 +304 (l 1 happy)]
    $ show_sprites(("ha 1", "l 1 happy"))

    voice "ch4.2_l_006"
    l "Yes. When I was little, I served as Her Highness's playmate."

    # [lay7 hide][lay5 +390 (s 1)]
    $ show_sprites(("l 1 happy", "s 1"))

    voice "ch4.2_s_005"
    s "So if you put it another way, you and Her Highness are childhood friends?"

    # [lay1 +302 (l 1)]
    $ show_sprites(("l 1", "s 1"))

    voice "ch4.2_l_007"
    l "Well, I suppose that's how it amounts to. But don't go speaking of this too carelessly, all right?"

    voice "ch4.2_l_008"
    l "Her Highness is now the Queen who supports a whole nation."

    # [lay1 +335 (l 3)]
    $ show_sprites(("l 3", "s 1"))

    voice "ch4.2_l_009"
    l "A mere noble or commoner is not permitted to address her so lightly."

    # [lay1 +308 (l 1 sad)]
    $ show_sprites(("l 1 sad", "s 1"))

    voice "ch4.2_l_010"
    l "Still, the real problem is why we were summoned."

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("l 1 sad", "s 3 sad"))

    voice "ch4.2_s_006"
    s "You think it's about Haruna after all?"

    # [lay5 hide][lay7 +957 (ha 1 sad)]
    $ show_sprites(("l 1 sad", "ha 1 sad"))

    voice "ch4.2_ha_003"
    ha "Wh-what, about me…?"

    voice "ch4.2_l_011"
    l "Hmm, I still don't know. Still, it seems the Headmaster's arrangements will settle things peaceably…"

    voice "ch4.2_ha_004"
    ha "…"

    # [lay1 hide][lay5 +392 (s 1 happy)]
    $ show_sprites(("s 1 happy", "ha 1 sad"))

    voice "ch4.2_s_007"
    s "It'll be fine, Haruna. If it comes to it, I'll protect you."

    # [lay5 level=157][lay19 +942 (d 1 happy)][lay7 level=154]
    $ show_sprites(("s 1 happy", "ha 1 sad", "d 1 happy"))

    voice "ch4.2_d_001"
    d "Oho, as expected of my partner. Aren't you the cool one."

    # [lay19 hide][lay7 hide][lay5 hide][lay1 +339 (l 3 angry)]
    $ show_sprites(("l 3 angry",))

    voice "ch4.2_l_012"
    l "W-wait a moment. You mustn't go causing trouble at the royal palace."

    # [lay1 x=-96 — сдвиг][lay5 +390 (s 1)]
    $ show_sprites(("l 3 angry", "s 1"))

    voice "ch4.2_s_008"
    s "It'll be fine, I said. It was just an example."

    # [lay1 +302 (l 1)]
    $ show_sprites(("l 1", "s 1"))

    voice "ch4.2_l_013"
    l "Good grief…"

    # [lay5 hide][lay2 +489 (si 1)]
    $ show_sprites(("l 1", "si 1"))

    voice "ch4.2_si_005"
    si "Um… Miss Vallière."

    voice "ch4.2_l_014"
    l "Siesta, what is it?"

    # [lay2 +495 (si 1 sad)]
    $ show_sprites(("l 1", "si 1 sad"))

    voice "ch4.2_si_006"
    si "What's to become of me?"

    # [lay1 +335 (l 3)]
    $ show_sprites(("l 3", "si 1 sad"))

    voice "ch4.2_l_015"
    l "Ah, about that. I'll ask you to stay behind and mind this room, Siesta."

    # [lay2 +493 (si 1 angry)]
    $ show_sprites(("l 3", "si 1 angry"))

    voice "ch4.2_si_007"
    si "What!? Am I not allowed to come along too?"

    # [lay1 +302 (l 1)]
    $ show_sprites(("l 1", "si 1 angry"))

    voice "ch4.2_l_016"
    l "You may not. The ones summoned by Her Majesty are me and Saito. Haruna is going for the Headmaster's business."

    voice "ch4.2_l_017"
    l "You have no business there, do you, Siesta? We can't bloat the party for no reason."

    # [lay2 +528 (si 4 sad)]
    $ show_sprites(("l 1", "si 4 sad"))

    voice "ch4.2_si_008"
    si "That's…{#ch4.2_si_008}"

    # [lay2 hide][lay5 +429 (s 3 sad)]
    $ show_sprites(("l 1", "s 3 sad"))

    voice "ch4.2_s_009"
    s "Can't we bring at least Siesta? You know, to look after us…"

    voice "ch4.2_l_018"
    l "No.{#ch4.2_l_018}"

    # [lay1 hide][lay2 +495 (si 1 sad)]
    $ show_sprites(("si 1 sad", "s 3 sad"))

    voice "ch4.2_si_009"
    si "Saito-san, thank you. But it's just as Miss Vallière says. I'll stay behind, then."

    # [lay5 +396 (s 1 sad)]
    $ show_sprites(("si 1 sad", "s 1 sad"))

    voice "ch4.2_s_010"
    s "Siesta…"

    # [lay2 +489 (si 1)]
    $ show_sprites(("si 1", "s 1 sad"))

    voice "ch4.2_si_010"
    si "Well then, I have my work to attend to as well. If you'll excuse me."

    # [SE se0 +56 — SE не портируется][lay2 hide][lay5 hide][lay1 +335 (l 3)]
    $ show_sprites(("l 3",))

    voice "ch4.2_l_019"
    l "Then let's break up for now, shall we? Assemble before the carriage."

    # [lay1 x=-96 — сдвиг][lay5 +390 (s 1)]
    $ show_sprites(("l 3", "s 1"))

    voice "ch4.2_s_011"
    s "Understood.{#ch4.2_s_011}"

    # [lay5 hide][lay7 +951 (ha 1)]
    $ show_sprites(("l 3", "ha 1"))

    voice "ch4.2_ha_005"
    ha "Yes.{#ch4.2_ha_005}"

    # [lay1 hide][lay7 hide][BG hide][BG +14 (hallway)][TRANS][lay5 +390 (s 1)]
    $ fade_fx("hallway", sprites=("s 1",))

    th "Now then, what should I do…{#ch4.2_th_225}"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay5 hide][BG hide]
    stop music fadeout 1.0

    # 【移動】-хаб — карта дат (сцена 225): leave-цель moveInit = сцена 231.
    jump ch4_2_map


label ch4_2_map:
    # ==== Карта-хаб 【移動】 (сцена 225) ====
    # Цели: 1342 (Луиза), 1347 (Сиеста), 1352 (Кирхе), 1357 (Табита),
    # 1362 (Харуна). После визита локация убирается из карты (как ch2_4_map);
    # «Leave» → ch4_2_leave → сцена 231.
    # ВНИМАНИЕ: реализована только дата Луизы (1342–1346). Остальные четыре
    # цели (date_siesta/kirche/tabitha/haruna_ch4_2) — форвард-ссылки на
    # непортированные сцены 1347–1382 (долг E7-класса; вне охвата
    # check_project.py, который сканирует только `jump`).
    $ choices = []
    if "louise_room" not in ch4_2_visited:
        $ choices.append({"char": "louise", "text": "Louise's Room{#ch4.2_lroom}", "target": "date_louise_ch4_2"})
    if "kitchen" not in ch4_2_visited:
        $ choices.append({"char": "siesta", "text": "Kitchen{#ch4.2_kitchen}", "target": "date_siesta_ch4_2"})
    if "yard" not in ch4_2_visited:
        $ choices.append({"char": "kirche", "text": "Courtyard{#ch4.2_yard}", "target": "date_kirche_ch4_2"})
    if "hallway" not in ch4_2_visited:
        $ choices.append({"char": "tabitha", "text": "Hallway{#ch4.2_hallway}", "target": "date_tabitha_ch4_2"})
    if "h_room" not in ch4_2_visited:
        $ choices.append({"char": "haruna", "text": "Louise's Room{#ch4.2_hroom}", "target": "date_haruna_ch4_2"})
    $ choices.append({"text": "Leave{#ch4.2_leave}", "target": "ch4_2_leave"})
    $ sprite_choice(choices)
    jump ch4_2_map
    return


label ch4_2_leave:
    jump ch4_2_231


label date_louise_ch4_2:
    # ==== SCENES 1342–1346 (дата с Луизой, «ルイズの部屋») ====
    # [BG +10 (louise_room)][TRANS][BGM play=+6 → t5][SE se0 +57 — SE не портируется]
    # [waitSEStop — не портируется][lay5 +396 (s 1 sad)]
    $ fade_fx("louise_room", new_music="t5", sprites=("s 1 sad",))

    voice "ch4.2_s_012"
    s "Hey, what are you making such a mess for? The floor's covered in clothes."

    # [lay5 x=224 — сдвиг][lay1 +306 (l 1 angry)]
    $ show_sprites(("l 1 angry", "s 1 sad"))

    voice "ch4.2_l_020"
    l "Hey, Saito! If you've got time to stand there spacing out, then help me!"

    # 【好感度】ルイズ 20
    $ update_sympathy(20, char_key="louise")

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("l 1 angry", "s 3 sad"))

    voice "ch4.2_s_013"
    s "Louise, what have you been doing all this time? My packing was finished long ago."

    # [lay1 +302 (l 1)]
    $ show_sprites(("l 1", "s 3 sad"))

    voice "ch4.2_l_021"
    l "A girl needs all sorts of preparations before going out."

    # [lay1 +308 (l 1 sad)]
    $ show_sprites(("l 1 sad", "s 3 sad"))

    voice "ch4.2_l_022"
    l "Besides, I've been leaving everything to you lately, so I don't even know what's where…"

    th "Honestly, this is what I get for letting her dump everything on me."

    # ==== 【選択肢】 (1342) → 1343/1344/1345, сходятся в 1346 ====
    menu:

        "Give her a hand.{#ch4.2_m1342a}":
            jump ch4_2_l_1343

        "I don't want to help.{#ch4.2_m1342b}":
            jump ch4_2_l_1344

        "Offer to help, on one condition.{#ch4.2_m1342c}":
            jump ch4_2_l_1345


label ch4_2_l_1343:
    # ==== SCENE 1343 ==== (RESET: [lay5 +429][lay1 +308][BG +10][BGM +6] =
    # текущее состояние)
    # [lay5 +390 (s 1)]
    $ show_sprites(("l 1 sad", "s 1"))

    voice "ch4.2_s_014"
    s "All right, I'll help you."

    # [lay1 +304 (l 1 happy)]
    $ show_sprites(("l 1 happy", "s 1"))

    voice "ch4.2_l_023"
    l "Really?{#ch4.2_l_023}"

    # 【好感度】ルイズ 20
    $ update_sympathy(20, char_key="louise")

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("l 1 happy", "s 3 sad"))

    voice "ch4.2_s_015"
    s "At this rate, it'll never get finished."

    # [lay1 +335 (l 3)]
    $ show_sprites(("l 3", "s 3 sad"))

    voice "ch4.2_l_024"
    l "Since I'm in such a good mood, just help me quietly!"

    # 【好感度】ルイズ -10
    $ update_sympathy(-10, char_key="louise")

    jump ch4_2_l_1346


label ch4_2_l_1344:
    # ==== SCENE 1344 ==== (RESET: [lay5 +429][lay1 +308] — состояние на конец
    # 1342; в линейном проходе ветки не сбрасываются, поэтому выставляем явно)
    $ show_sprites(("l 1 sad", "s 3 sad"))

    voice "ch4.2_s_016"
    s "Wha—. So I'm the one helping, huh."

    # [lay1 +335 (l 3)]
    $ show_sprites(("l 3", "s 3 sad"))

    voice "ch4.2_l_025"
    l "It's your master's order. No complaints."

    jump ch4_2_l_1346


label ch4_2_l_1345:
    # ==== SCENE 1345 ==== (RESET: [lay5 +429][lay1 +308] = текущее состояние)
    # [lay5 +390 (s 1)]
    $ show_sprites(("l 1 sad", "s 1"))

    voice "ch4.2_s_017"
    s "I don't mind helping, but… I do have one condition."

    # [lay1 +302 (l 1)]
    $ show_sprites(("l 1", "s 1"))

    voice "ch4.2_l_026"
    l "A condition? Go on, try saying it, just in case."

    # [lay5 +425 (s 3 happy)]
    $ show_sprites(("l 1", "s 3 happy"))

    voice "ch4.2_s_018"
    s "I'd like tonight's dinner to have one extra dish… something like that. Is that a no?"

    # [lay1 +335 (l 3)]
    $ show_sprites(("l 3", "s 3 happy"))

    voice "ch4.2_l_027"
    l "Rejected. Keep talking nonsense and I'll cut you off from dinner entirely!"

    # 【好感度】ルイズ -10
    $ update_sympathy(-10, char_key="louise")

    jump ch4_2_l_1346


label ch4_2_l_1346:
    # ==== SCENE 1346 ==== (RESET: [lay5 +429][lay1 +335] = текущее состояние)
    # [lay5 +390 (s 1)]
    $ show_sprites(("l 3", "s 1"))

    voice "ch4.2_s_019"
    s "Yeah, yeah, understood. So, what's left?"

    # [lay1 +310 (l 1 shy)]
    $ show_sprites(("l 1 shy", "s 1"))

    voice "ch4.2_l_028"
    l "A change of clothes…"

    voice "ch4.2_s_020"
    s "I see. Since you never tidy up normally, you can't find where anything is."

    # [lay1 +308 (l 1 sad)]
    $ show_sprites(("l 1 sad", "s 1"))

    voice "ch4.2_l_029"
    l "Ugh."

    # [lay5 +423 (s 3)]
    $ show_sprites(("l 1 sad", "s 3"))

    voice "ch4.2_s_021"
    s "Er, how many days' worth do you need?"

    # [lay1 +343 (l 3 shy)]
    $ show_sprites(("l 3 shy", "s 3"))

    voice "ch4.2_l_030"
    l "…Th-that is. Two or three days' worth at most should be… enough… I think…"

    # [lay5 +390 (s 1)]
    $ show_sprites(("l 3 shy", "s 1"))

    voice "ch4.2_s_022"
    s "Yeah, yeah, about three days. Do you need clothes other than the school uniform too?"

    # [lay1 +310 (l 1 shy)]
    $ show_sprites(("l 1 shy", "s 1"))

    voice "ch4.2_l_031"
    l "M-maybe I do…"

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("l 1 shy", "s 3 sad"))

    voice "ch4.2_s_023"
    s "Do you have a fever? Your face is bright red, you know?"

    # [lay1 +306 (l 1 angry)]
    $ show_sprites(("l 1 angry", "s 3 sad"))

    voice "ch4.2_l_032"
    l "Oh, be quiet! J-just hurry up and pack it already."

    # [lay1 +310 (l 1 shy)][lay5 +396 (s 1 sad)]
    $ show_sprites(("l 1 shy", "s 1 sad"))

    voice "ch4.2_s_024"
    s "I'll pack it properly even without being told."

    # [lay5 +390 (s 1)]
    $ show_sprites(("l 1 shy", "s 1"))

    voice "ch4.2_s_025"
    s "Still, though it's odd for a guy to say it, I've gotten rather good at folding clothes lately."

    voice "ch4.2_s_026"
    s "Look, Louise. This folding, and this neatening."

    # [lay5 +423 (s 3)]
    $ show_sprites(("l 1 shy", "s 3"))

    voice "ch4.2_s_027"
    s "Even if I said a girl did this, it'd pass."

    # [lay5 +392 (s 1 happy)]
    $ show_sprites(("l 1 shy", "s 1 happy"))

    voice "ch4.2_s_028"
    s "And this whiteness of the fabric. You could call it a masterstroke of hand-washing."

    # [lay1 +343 (l 3 shy)]
    $ show_sprites(("l 3 shy", "s 1 happy"))

    voice "ch4.2_l_033"
    l "Enough already! A-ah, ahh, I'll do the rest myself! Get out of this room right now, at once!"

    # [lay5 +396 (s 1 sad)]
    $ show_sprites(("l 3 shy", "s 1 sad"))

    voice "ch4.2_s_029"
    s "What's the matter, Louise? Did I do something to offend you?"

    # [lay1 +310 (l 1 shy)]
    $ show_sprites(("l 1 shy", "s 1 sad"))

    voice "ch4.2_l_034"
    l "N-nothing. I'm telling you, I'll do it myself after all."

    th "What on earth's gotten into her?"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay1 hide][lay5 hide][BG hide]
    stop music fadeout 1.0
    $ ch4_2_visited.add("louise_room")
    # return (а не jump): карта вызвала лейбл через renpy.call (sprite_choice),
    # после return хаб продолжит с "jump ch4_2_map" — как в ch2_4b.
    return


label ch4_2_231:
    # ==== SCENE 231 ====
    # [BG +26 (yard)][TRANS][BGM play=+32 → t31][lay9 +929 (c 1)]
    $ fade_fx("yard", new_music="t31", sprites=("c 1",))

    voice "ch4.2_c_001"
    c "Then, Miss Vallière. Do be careful on the road."

    # [lay9 x=224 — сдвиг][lay1 +304 (l 1 happy)]
    $ show_sprites(("l 1 happy", "c 1"))

    voice "ch4.2_l_035"
    l "Yes. Thank you, Professor Colbert."

    # [lay9 hide][lay10 +918 (o 1)]
    $ show_sprites(("l 1 happy", "o 1"))

    voice "ch4.2_o_001"
    o "Mind yourselves on the road. If anything happens, send word at once."

    # [lay1 +302 (l 1)]
    $ show_sprites(("l 1", "o 1"))

    voice "ch4.2_l_036"
    l "Understood. I'm grateful you've prepared such a fine carriage for us."

    voice "ch4.2_o_002"
    o "Hmm, no thanks needed."

    # [lay10 +920 (o 1 happy)]
    $ show_sprites(("l 1", "o 1 happy"))

    voice "ch4.2_o_003"
    o "Come, Her Majesty must be waiting for you with bated breath. Off you go, and do be careful."

    voice "ch4.2_l_037"
    l "Yes, then we'll be on our way."

    # [lay10 hide][lay1 hide][lay9 +929 (c 1)]
    $ show_sprites(("c 1",))

    voice "ch4.2_c_002"
    c "Saito-kun, I'm counting on you to look after the two of them."

    # [lay9 x=-96 — сдвиг][lay5 +401 (s 2) dir=1B]
    $ show_sprites(("c 1", "s 2"))

    voice "ch4.2_s_030"
    s "Yes, I'll do my best."

    voice "ch4.2_c_003"
    c "Haruna-kun, once you're there, follow the instructions of Miss Vallière and Saito-kun."

    # [lay5 hide][lay7 +962 (ha 2) dir=1B]
    $ show_sprites(("c 1", "ha 2"))

    voice "ch4.2_ha_006"
    ha "Yes, I understand."

    # [lay9 hide][lay7 hide][lay1 +335 (l 3) dir=2A]
    $ show_sprites(("l 3",))

    voice "ch4.2_l_038"
    l "Now then, let's get into the carriage."

    # [lay1 hide][BG hide][EVENT_CG +123][TRANS]
    $ fade_fx("id(123)", type="cg")

    th "So, about that carriage — it's got two-person seats facing each other…"

    # [EVENT_CG +120] — кроссфейд CG
    $ dissolve_fx("id(120)", type="cg")

    th "Louise and Haruna are sitting across from each other. Now then, whose side should I sit on…"

    # [EVENT_CG +121] — кроссфейд CG
    $ dissolve_fx("id(121)", type="cg")

    voice "ch4.2_l_039"
    l "What are you standing around for? Hurry up and sit next to me!"

    voice "ch4.2_ha_007"
    ha "Hiraga-kun, you can sit next to me too, you know? I feel bad, the way Louise-san ends up cramped."

    # [lay5 hide][lay1 hide][lay7 hide][BG hide][EVENT_CG hide][BG +26][TRANS][lay5 +440 (s 4 sad) dir=2B]
    $ fade_fx("yard", sprites=("s 4 sad",))

    voice "ch4.2_s_031"
    s "Ah, what should I do…"

    menu:

        "Sit next to Louise.{#ch4.2_m231a}":
            jump ch4_2_232

        "Sit next to Haruna.{#ch4.2_m231b}":
            jump ch4_2_233

        "Waver over which seat.{#ch4.2_m231c}":
            jump ch4_2_234


label ch4_2_232:
    # ==== SCENE 232 ==== (RESET: [BG +26][BGM +32] = текущее состояние)
    # [lay5 +434 (s 4)]
    $ show_sprites(("s 4",))

    voice "ch4.2_s_032"
    s "Well then, I guess I'll go with sitting next to Louise?"

    # [lay5 x=224 — сдвиг][lay1 +343 (l 3 shy) dir=2A]
    $ show_sprites(("l 3 shy", "s 4"))

    voice "ch4.2_l_040"
    l "Th-that's right!? Th-that's… that's perfectly fine, isn't it."

    # 【好感度】ルイズ 10
    $ update_sympathy(10, char_key="louise")

    # [lay1 hide][lay7 +968 (ha 2 sad) dir=1B]
    $ show_sprites(("s 4", "ha 2 sad"))

    voice "ch4.2_ha_008"
    ha "Mm…"

    # 【好感度】ハルナ -10
    $ update_sympathy(-10, char_key="haruna")

    # [lay5 +407 (s 2 sad) dir=1B]
    $ show_sprites(("s 2 sad", "ha 2 sad"))

    th "Ahh… Haruna, why do you look away so wistfully…"

    # [lay7 hide][lay5 hide]
    $ show_sprites(None)
    jump ch4_2_235


label ch4_2_233:
    # ==== SCENE 233 ==== (RESET: [BG +26][BGM +32] = текущее состояние)
    # [lay5 +401 (s 2) dir=1B]
    $ show_sprites(("s 2",))

    voice "ch4.2_s_033"
    s "All right, I'll sit next to Haruna."

    # 【好感度】ハルナ 10
    $ update_sympathy(10, char_key="haruna")

    # [lay5 x=224 — сдвиг][lay1 +306 (l 1 angry) dir=1A]
    $ show_sprites(("l 1 angry", "s 2"))

    voice "ch4.2_l_041"
    l "Wh-what! It's fine… it's fine! Do whatever you like, Saito, that's all there is to it!"

    # 【好感度】ルイズ -10
    $ update_sympathy(-10, char_key="louise")

    # [lay5 +440 (s 4 sad) dir=2B]
    $ show_sprites(("l 1 angry", "s 4 sad"))

    voice "ch4.2_s_034"
    s "Huh? What are you getting angry for?"

    voice "ch4.2_l_042"
    l "It's none of your business, Saito."

    # [lay1 hide][lay5 hide]
    $ show_sprites(None)
    jump ch4_2_235


label ch4_2_234:
    # ==== SCENE 234 ==== (RESET: [BG +26][BGM +32] = текущее состояние)
    # [lay5 +407 (s 2 sad) dir=1B]
    $ show_sprites(("s 2 sad",))

    th "Whose side should I sit on… Somehow it looks like I'll ruffle feathers whichever I pick."

    # [lay5 x=224 — сдвиг][lay1 +339 (l 3 angry) dir=2A]
    $ show_sprites(("l 3 angry", "s 2 sad"))

    voice "ch4.2_l_043"
    l "Oh, just make up your mind already! Or would you rather be loaded up with the rest of the luggage?"

    # 【好感度】ルイズ -10
    $ update_sympathy(-10, char_key="louise")

    voice "ch4.2_s_035"
    s "Please, anything but that."

    # [lay1 hide][lay5 hide]
    $ show_sprites(None)
    jump ch4_2_235


label ch4_2_235:
    # ==== SCENE 235 ==== (RESET: [BG +26][BGM +32] = текущее состояние;
    # спрайты скрыты во всех трёх ветках)
    # [LAYER lay0 +588 (t 1) dir=1A]
    $ show_sprites(("t 1",))

    voice "ch4.2_t_001"
    t "A bloodbath."

    # [lay0 x=224 — сдвиг][lay6 +676 (k 1) dir=1A]
    $ show_sprites(("t 1", "k 1"))

    voice "ch4.2_k_001"
    k "Aww. Darling, sneaking off on us like that — how cold of you."

    # [lay0 hide][lay6 hide][lay5 +401 (s 2) dir=1B]
    $ show_sprites(("s 2",))

    voice "ch4.2_s_036"
    s "Kirche, Tabitha."

    # [lay5 x=224 — сдвиг][lay4 +566 (g 2) dir=2A]
    $ show_sprites(("s 2", "g 2"))

    voice "ch4.2_g_001"
    g "Hey there, don't go forgetting about us, either."

    voice "ch4.2_s_037"
    s "Guiche, Montmon."

    # [lay4 hide][lay3 +856 (m 1 angry) dir=1A]
    $ show_sprites(("m 1 angry", "s 2"))

    voice "ch4.2_m_001"
    m "For the last time, it's not Montmon. You're doing that on purpose, aren't you?"

    # [lay5 +434 (s 4) dir=2B]
    $ show_sprites(("m 1 angry", "s 4"))

    voice "ch4.2_s_038"
    s "N-no, sorry. But why are you all here?"

    # [lay3 hide][lay4 +555 (g 1) dir=1A]
    $ show_sprites(("g 1", "s 4"))

    voice "ch4.2_g_002"
    g "We came to see you off. I thought we'd watch over your departure."

    # [lay5 +401 (s 2) dir=1B]
    $ show_sprites(("g 1", "s 2"))

    voice "ch4.2_s_039"
    s "I see. Thanks.{#ch4.2_s_039}"

    # [lay4 hide][lay5 level=156][LAYER lay0 +588 (t 1) dir=1A]
    $ show_sprites(("t 1", "s 2"))

    voice "ch4.2_t_002"
    t "Tug, tug."

    # [lay0 x=-96 — сдвиг][lay5 +434 (s 4) dir=2B]
    $ show_sprites(("t 1", "s 4"))

    voice "ch4.2_s_040"
    s "Hm? What is it, Tabitha?"

    # [LAYER lay0 +621 (t 4) dir=2A]
    $ show_sprites(("t 4", "s 4"))

    voice "ch4.2_t_003"
    t "You, over here."

    # [lay5 +401 (s 2) dir=1B]
    $ show_sprites(("t 4", "s 2"))

    voice "ch4.2_s_041"
    s "？？？？{#ch4.2_s_041}"

    # [LAYER lay0 +588 (t 1) dir=1A]
    $ show_sprites(("t 1", "s 2"))

    voice "ch4.2_t_004"
    t "You and you, over here."

    # [lay5 +440 (s 4 sad) dir=2B]
    $ show_sprites(("t 1", "s 4 sad"))

    voice "ch4.2_s_042"
    s "？？？？{#ch4.2_s_042}"

    # [lay5 hide][lay6 +676 (k 1) dir=1A level=154]
    $ show_sprites(("t 1", "k 1"))

    voice "ch4.2_k_002"
    k "Tabitha's saying that Louise and Haruna should sit together, and you on the opposite side, darling."

    voice "ch4.2_t_005"
    t "That way, the two of them are even."

    # [lay6 hide][lay0 hide][lay5 +401 (s 2) dir=1B]
    $ show_sprites(("s 2",))

    voice "ch4.2_s_043"
    s "Ah, I see. Thanks, Tabitha. What, it was simple after all."

    # [lay5 hide][lay1 +308 (l 1 sad) dir=1A][lay7 +968 (ha 2 sad) dir=1B]
    $ show_sprites(("l 1 sad", "ha 2 sad"))

    voice "ch4.2_l_044"
    l "……{#ch4.2_l_044}"

    voice "ch4.2_ha_009"
    ha "……{#ch4.2_ha_009}"

    # [lay7 hide][lay1 +302 (l 1)]
    $ show_sprites(("l 1",))

    voice "ch4.2_l_045"
    l "Then, everyone, we'll be off."

    # [lay1 hide][lay10 +920 (o 1 happy) dir=1A level=149]
    $ show_sprites(("o 1 happy",))

    voice "ch4.2_o_004"
    o "Do your best out there."

    th "And so, at last, we set out from the Academy of Magic."

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay10 hide][lay5 hide][BG hide]
    stop music fadeout 1.0

    jump ch4_3
