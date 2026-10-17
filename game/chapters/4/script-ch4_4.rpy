# Глава 4, часть 4 (сцены 246–255 + даты 1367–1382): Тристания. Прилёт в
# королевскую столицу (каретка → титульная карточка «トリスタニア» — прецедент
# ch0/ch1 через overlay_screen; сцена 247: 58→1149→1140→1149→58), улица
# с шумом (SE se1 +37 loop — не портируется), меню поддержки Харуной
# (248 «мы с вами» / 249 «Луиза найдёт» / 250 «когда-нибудь устроится»),
# хаб-улица 【移動】 (сцена 251, moveInit +256 / 4 пункта «表通り»,
# 4-й без иконки) → даты: Харуна — магазин специй (1367–1371), Луиза —
# аптечка и зелье (1372–1376, Дерфлингер lay19 id 940/946), Сиеста —
# городская прогулка (1377–1381), пустая улица (1382). Leave-цель хаба —
# сцена 256 (следующая часть).
# Источник: ps2_source/chapters/chapter_05_トリスタニアの危機.txt
#   (SCENE 246–255, 1367–1382; сцены 252–255 — диспетчерские переходы,
#   не портируются как отдельные лейблы — их работу делает ch4_4_map,
#   по прецеденту хаба P2: сцены 226–230).
# Точные аргументы: ps2_source/events_full/chapter_05_トリスタニアの危機.txt.
#
# Голоса: ch4.4_<spk>_<NNN> — новая группа части 4, нумерация с 001 по
# говорящему, порядок порта (246–255 → даты A/B/C/D):
#   s ×46 (001–010 main, 011–026 A, 027–031 B, 032–045 C, 046 D),
#   l ×24 (001–009 main, 010–024 B), ha ×34 (001–012 main, 013–034 A),
#   si ×24 (001–006 main, 007–024 C), mer ×11 (A), d ×6 (B) — всего 145.
# Новые id спрайтов: d-пул 940/946 (d 1 / d 1 sad) — из карты; s 409 = s 2 shy
#   (блок 401 pos 8) — пиксель-сверка SCENEDAT[409] подтвердила (MAE 0.0268,
#   следующий s 2 happy 0.0273), строка добавлена в references/sprite_id_map.csv;
#   497/524 (si 1 shy / si 4 happy) — из карты.
# Спрайт даты B: сцены с lay19 (меч Дерфлингера) — только карта-состояния;
#   перевод уровней level=154/155/156 не копируется (AGENTS §6).
# Титульная карточка 1140 «トリスタニア (+ゼロの使い魔)» — заголовок EN
#   "Tristania" (словарный канон); подзаголовок серии не переносится;
#   background карточки = town_square (титульный фото/размытый вариант,
#   PROVISIONAL — см. image_id_map 1140/1149).
# Озвученная «мысль» Дерфлингера d 1244 — формально DIALOGUE с голосом,
#   портируется как обычная реплика (скобки сохранены) — по канону JA.
# 商人 (специй-торговец, даты A) — define merchant уже существует
#   (characters.rpy:27); в манифесте — код mer.
# Не портируются: SE (se1 +37/+56 stop), вывод символов lay1 x=144/y=416,
#   точечные level=/dir=/waitTime/sync/create (AGENTS §6).
# Сочувствие (8 вызовов update_sympathy): 248 haruna +10, 249 louise −10,
#   250 haruna −10, 1367 haruna +20, 1372 louise +20, 1377 siesta +20,
#   1378 siesta +10, 1379 siesta −10.
# Карта хаба вызываетет даты через renpy.call (sprite_choice) → ветки-даты
#   заканчиваются return; visited-ключи: store / apothecary / stroll /
#   street (добавляются в конце каждой даты). Leave → jump ch4_5 (E7-долг).

default ch4_4_visited = set()

label ch4_4:
    # ==== SCENE 246 ==== (RESET: [SE se1 stop×2][BGM +19 → t18][BG +123
    # (интерьер кареты, id-заглушка)][TRANS 1000][lay2 +491 (si 1 happy) 1A])
    $ fade_fx("id(123)", new_music="t18", sprites=("si 1 happy",))

    voice "ch4.4_si_001"
    si "H-Haruna? Look—look outside!"

    # [lay2 x=-96][lay7 +962 (ha 2) 1B]
    $ show_sprites(("si 1 happy", "ha 2"))

    voice "ch4.4_ha_001"
    ha "What is it, Miss Siesta?"

    # [lay7 +964 (ha 2 happy) 1B]
    $ show_sprites(("si 1 happy", "ha 2 happy"))

    voice "ch4.4_ha_002"
    ha "Whoa… What an incredible view. So this is the…"

    # [lay2 hide][lay1 +304 (l 1 happy) 1A]
    $ show_sprites(("l 1 happy",))

    voice "ch4.4_l_001"
    l "Right. The royal capital, Tristania."

    voice "ch4.4_l_002"
    l "…We're almost at the palace, aren't we."

    th "We had made it to Tristania, safe and sound."

    # [SE se1 stop=1 ×2 — SE не портируются][BGM stop=1000]
    # [lay1 hide][lay7 hide][lay5 hide][BG hide]
    stop music fadeout 1.0
    # → next scene 247

label ch4_4_247:
    # ==== SCENE 247 ==== (ритуал прибытия: [BGM +31 → t30][BG +58 (town_square)]
    # [TRANS 500][BG +1149 (титульный размытый)][500][BG +1140 — титульная
    # карточка «トリスタニア» + подзаголовок «ゼロの使い魔»][750][BG +1149]
    # [TRANS][BG +58][TRANS 2000][BG 58 repeat][BG hide] → [BG +38 (town)]
    # [TRANS 1000][SE se1 +37 loop — SE не портируется])
    # → карточка-титул по прецеденту ch0/ch1 (монтаж сворачивается в
    # overlay_screen; подзаголовок серии в текст карты не переносится)
    play music t30 fadein 1.0
    $ fade_fx("town_square")

    call overlay_screen("town_square", "Tristania") from _call_overlay_screen_10

    $ fade_fx("town", sprites=("si 1 happy",))

    voice "ch4.4_si_002"
    si "As far as the eye can see, it's nothing but buildings and people."

    # [lay2 x=-96][lay7 +964 (ha 2 happy) 1B]
    $ show_sprites(("si 1 happy", "ha 2 happy"))

    voice "ch4.4_ha_003"
    ha "It's like we've strayed into a movie's world. For a city so fantastically built to actually exist… it's all just like a dream."

    # [lay7 hide][lay5 +403 (s 2 happy) 1B]
    $ show_sprites(("si 1 happy", "s 2 happy"))

    voice "ch4.4_s_001"
    s "Well, when I first saw it, I figured I'd wandered into some theme park too."

    # [lay2 +489 (si 1) 1A]
    $ show_sprites(("si 1", "s 2 happy"))

    voice "ch4.4_si_003"
    si "A theme park?"

    # [lay5 +434 (s 4) 2B]
    $ show_sprites(("si 1", "s 4"))

    voice "ch4.4_s_002"
    s "Hmm. Like… a park that recreates the look of another world, I guess."

    voice "ch4.4_si_004"
    si "Ohh. Your world sounds like a rather strange place."

    # [lay5 hide][lay2 hide][lay7 +962 (ha 2) 1B]
    $ show_sprites(("ha 2",))

    voice "ch4.4_ha_004"
    ha "…But."

    # [lay7 x=224][lay1 +302 (l 1) 1A]
    $ show_sprites(("l 1", "ha 2"))

    voice "ch4.4_l_003"
    l "But what?"

    # [lay7 +968 (ha 2 sad) 1B]
    $ show_sprites(("l 1", "ha 2 sad"))

    voice "ch4.4_ha_005"
    ha "I really did end up in another world, didn't I… Me."

    menu ch4_4_247_choice:
        # 【選択肢】×3 (сцена 247)
        "We're right here with you.{#ch4.4_c247a}":
            # → scene 248
            jump ch4_4_248
        "Louise will track down the way back.{#ch4.4_c247b}":
            # → scene 249
            jump ch4_4_249
        "Someday, somehow, it'll all work out.{#ch4.4_c247c}":
            # → scene 250
            jump ch4_4_250

label ch4_4_248:
    # ==== SCENE 248 ==== (начало ветки = конец 247: [lay1 +302][lay7 +968]
    # [BGM +31 re-assert][SE se1 +37][BG +38][lay1 hide][lay5 +401 (s 2) 1B])
    $ show_sprites(("s 2", "ha 2 sad"))

    voice "ch4.4_s_003"
    s "It's all right, Haruna. We're right here with you, aren't we?"

    # [lay5 hide][lay1 +302 (l 1) 1A]
    $ show_sprites(("l 1", "ha 2 sad"))

    voice "ch4.4_l_004"
    l "Honestly, pull yourself together. It's embarrassing, isn't it?"

    # [lay1 hide][lay2 +491 (si 1 happy) 1A]
    $ show_sprites(("si 1 happy", "ha 2 sad"))

    voice "ch4.4_si_005"
    si "Cheer up, Miss Haruna!"

    # [lay7 +962 (ha 2) 1B]
    $ show_sprites(("si 1 happy", "ha 2"))

    voice "ch4.4_ha_006"
    ha "Yes… Thank you."

    # 【好感度】ハルナ 10
    $ update_sympathy(10, char_key="haruna")
    # → next scene 251
    jump ch4_4_251

label ch4_4_249:
    # ==== SCENE 249 ==== (начало ветки = конец 247: [lay1 +302][lay7 +968])
    $ show_sprites(("l 1", "ha 2 sad"))

    voice "ch4.4_s_004"
    s "Don't worry. As for how we get back to my world—Louise will track down a way for us."

    # [lay5 hide][lay1 +302 (l 1) 1A]
    $ show_sprites(("l 1", "ha 2 sad"))

    voice "ch4.4_l_005"
    l "M-me?{#ch4.4_x6098}"

    # [lay7 +968 (ha 2 sad) 1B]
    $ show_sprites(("l 1", "ha 2 sad"))

    voice "ch4.4_ha_007"
    ha "You won't look for it?"

    # [lay1 +308 (l 1 sad) 1A]
    $ show_sprites(("l 1 sad", "ha 2 sad"))

    voice "ch4.4_l_006"
    l "Mm…{#ch4.4_x6099}"

    # [lay1 +339 (l 3 angry) 2A]
    $ show_sprites(("l 3 angry", "ha 2 sad"))

    voice "ch4.4_l_007"
    l "I-I will look for you. With the power of the House of Vallière, we're bound to find it somehow."

    # [lay1 hide][lay5 +403 (s 2 happy) 1B]
    $ show_sprites(("s 2 happy", "ha 2 sad"))

    voice "ch4.4_s_005"
    s "Good for you, Haruna."

    # [lay7 +962 (ha 2) 1B]
    $ show_sprites(("s 2 happy", "ha 2"))

    voice "ch4.4_ha_008"
    ha "Yes.{#ch4.4_x2299}"

    # [lay5 hide][lay1 +302 (l 1) 1A]
    $ show_sprites(("l 1", "ha 2"))

    voice "ch4.4_l_008"
    l "Ugh.{#ch4.4_x6101}"

    # 【好感度】ルイズ -10
    $ update_sympathy(-10, char_key="louise")
    # → next scene 251
    jump ch4_4_251

label ch4_4_250:
    # ==== SCENE 250 ==== (начало ветки = конец 247: [lay1 +302][lay7 +968])
    $ show_sprites(("s 2", "ha 2 sad"))

    voice "ch4.4_s_006"
    s "It'll be fine, Haruna. Someday it's bound to work out."

    # [lay7 +968 (ha 2 sad) 1B]
    $ show_sprites(("s 2", "ha 2 sad"))

    voice "ch4.4_ha_009"
    ha "And if it doesn't work out?"

    # [lay5 +403 (s 2 happy) 1B]
    $ show_sprites(("s 2 happy", "ha 2 sad"))

    voice "ch4.4_s_007"
    s "It will work out. You were lucky enough to meet me, right? You're bound to find a way home too."

    # [lay7 +962 (ha 2) 1B]
    $ show_sprites(("s 2 happy", "ha 2"))

    voice "ch4.4_ha_010"
    ha "Yes… I guess so…"

    # 【好感度】ハルナ -10
    $ update_sympathy(-10, char_key="haruna")
    # → next scene 251
    jump ch4_4_251

label ch4_4_251:
    # ==== SCENE 251 ==== (сход веток; RESET: [lay2 +491][lay7 +962][BGM +31
    # re-assert][SE se1 +37][BG +38][lay2 hide][lay1 x=144 y=416 — без x/y
    # копирования][lay5 +401 (s 2) 1B])
    # BGM +31 / SE se1 +37 — re-assert, не дублируются (продолжают звучать).
    $ show_sprites(("s 2",))

    voice "ch4.4_s_008"
    s "Well, either way. Until we can get back to our own world, we'll have to live in this one."

    voice "ch4.4_s_009"
    s "Don't be so pessimistic. First things first—you should get used to this world."

    # [lay7 +968 (ha 2 sad) 1B]
    $ show_sprites(("s 2", "ha 2 sad"))

    voice "ch4.4_ha_011"
    ha "Yes…{#ch4.4_x2302}"

    # [lay7 968 — re-assert]
    voice "ch4.4_s_010"
    s "Cheer up, Haruna."

    # [lay5 hide][lay2 +491 (si 1 happy) 1A]
    $ show_sprites(("si 1 happy", "ha 2 sad"))

    voice "ch4.4_si_006"
    si "We won't leave Miss Haruna all alone! So please, have no worries!"

    # [lay2 hide][lay1 +335 (l 3) 2A]
    $ show_sprites(("l 3", "ha 2 sad"))

    voice "ch4.4_l_009"
    l "Really now—since you went to all the trouble of coming into town, at least go take a look at all sorts of places… It would be a waste, you know?"

    # [lay7 +964 (ha 2 happy) 1B]
    $ show_sprites(("l 3", "ha 2 happy"))

    voice "ch4.4_ha_012"
    ha "Yes… Thank you, everyone."

    # [SE se1 stop=1 — SE не портируется][lay1 hide][lay7 hide]
    $ show_sprites()

    th "With the audience with the princess still a while away…"

    th "We had decided to wander the streets of Tristania a bit."

    # [lay5 +401 (s 2) 1B]
    $ show_sprites(("s 2",))

    th "Now then—what should I do?"

    # [SE se1 stop; BGM stop=1000][lay5 hide][BG hide]
    stop music fadeout 1.0
    # 【移動】表通り ×4 → сцены 1367 / 1372 / 1377 / 1382
    # → карта-хаб (moveInit +256 → leave-цель 256)
    jump ch4_4_map


label ch4_4_map:
    # ==== Карта-хаб 【移動】 (сцена 251) ====
    # Цели (events_full, SCENE 251 MOVEINIT/MAPDEST): все «表通り» (Main Street)
    #   1367 — иконка 962 (ha 2), 1372 — 302 (l 1), 1377 — 489 (si 1),
    #   1382 — 0 (без иконки, пустая улица). Leave-цель moveInit = 256;
    #   музыка карты moveInit bgm=+4 → t3 (не портируется, смотри отчёт).
    # Даты заканчиваются return (лейблы вызываются через renpy.call),
    #   как в ch4_2_map / составах ch4_2b.
    $ choices = []
    if "store" not in ch4_4_visited:
        $ choices.append({"char": "haruna", "text": "Main Street{#ch4.4_m1367}", "target": "date_haruna_ch4_4"})
    if "apothecary" not in ch4_4_visited:
        $ choices.append({"char": "louise", "text": "Main Street{#ch4.4_m1372}", "target": "date_louise_ch4_4"})
    if "stroll" not in ch4_4_visited:
        $ choices.append({"char": "siesta", "text": "Main Street{#ch4.4_m1377}", "target": "date_siesta_ch4_4"})
    if "street" not in ch4_4_visited:
        $ choices.append({"text": "Main Street{#ch4.4_m1382}", "target": "date_street_ch4_4"})
    $ choices.append({"text": "Leave{#ch4.4_leave}", "target": "ch4_4_leave"})
    $ sprite_choice(choices)
    jump ch4_4_map
    return


label ch4_4_leave:
    # Leave хаба → leave-цель moveInit(+256): сцена 256 — следующая часть
    jump ch4_5


label date_haruna_ch4_4:
    # ==== DATES: A — дата с Харуной, магазин специй (сцены 1367–1371) ====
    # [BG +38 (town)][TRANS 1000][BGM +11 → t10][lay7 +962 (ha 2) 1B]
    $ fade_fx("town", new_music="t10", sprites=("ha 2",))

    th "Whoops, there's Haruna. She's staring at the shop's goods, completely engrossed."

    voice "ch4.4_ha_013"
    ha "There's so much of everything…"

    # 【好感度】ハルナ 20
    $ update_sympathy(20, char_key="haruna")

    voice "ch4.4_mer_001"
    merchant "Welcome, young lady! Looking for anything in particular?"

    # [lay7 +968 (ha 2 sad) 1B]
    $ show_sprites(("ha 2 sad",))

    voice "ch4.4_ha_014"
    ha "Ah, u-um… Well… I was wondering what that red fruit there might be."

    voice "ch4.4_mer_002"
    merchant "Missie, that there is no fruit. It's a spice!"

    # [lay7 +966 (ha 2 angry) 1B]
    $ show_sprites(("ha 2 angry",))

    voice "ch4.4_ha_015"
    ha "Wha—this isn't a fruit?"

    voice "ch4.4_mer_003"
    merchant "Don't be saying foolish things now. Eat even a bite of it, and you'll be blowing smoke from both ears so hot it is!"

    # [lay7 +962 (ha 2) 1B]
    $ show_sprites(("ha 2",))

    voice "ch4.4_ha_016"
    ha "Oh… so it's not, then…"

    # [lay7 x=-96][lay5 +401 (s 2) 1B] — Харуна слева, Сайто справа
    $ show_sprites(("ha 2", "s 2"))

    voice "ch4.4_s_011"
    s "Haruna. What were you looking at?"

    # [lay7 +964 (ha 2 happy) 1B]
    $ show_sprites(("ha 2 happy", "s 2"))

    voice "ch4.4_ha_017"
    ha "Ah, Hiraga-kun! Look. There's so much food here I've never seen before."

    voice "ch4.4_s_012"
    s "Hm."

    voice "ch4.4_mer_004"
    merchant "Not knowing this spice, eh—then maybe the two of you have come from somewhere far off?"

    # [lay7 +968 (ha 2 sad) 1B]
    $ show_sprites(("ha 2 sad", "s 2"))

    voice "ch4.4_ha_018"
    ha "A-ah, well…"

    # [lay5 +434 (s 4) 2B]
    $ show_sprites(("ha 2 sad", "s 4"))

    voice "ch4.4_s_013"
    s "Well, we're from a little way east, that's all."

    voice "ch4.4_mer_005"
    merchant "Oh, is that so. Quite a long road you've come, then. Here, ask me anything you like."

    # [lay7 +962 (ha 2) 1B]
    $ show_sprites(("ha 2", "s 4"))

    voice "ch4.4_ha_019"
    ha "Hiraga-kun, there's all sorts of interesting things here."

    # [lay5 +401 (s 2) 1B]
    $ show_sprites(("ha 2", "s 2"))

    voice "ch4.4_s_014"
    s "You mean the vegetables?"

    voice "ch4.4_ha_020"
    ha "Yes. Just imagining what all of these foods could taste like is fun enough."

    # [lay5 +436 (s 4 happy) 2B]
    $ show_sprites(("ha 2", "s 4 happy"))

    voice "ch4.4_s_015"
    s "Well then—want to try eating something?"

    # [lay7 +968 (ha 2 sad) 1B]
    $ show_sprites(("ha 2 sad", "s 4 happy"))

    voice "ch4.4_ha_021"
    ha "Eh, we can? But… I don't have any money."

    # [lay5 +401 (s 2) 1B]
    $ show_sprites(("ha 2 sad", "s 2"))

    voice "ch4.4_s_016"
    s "I actually have a little on me. Sir, which of these would you recommend as a fruit?"

    # [lay7 +962 (ha 2) 1B]
    $ show_sprites(("ha 2", "s 2"))

    voice "ch4.4_mer_006"
    merchant "Well now… among these three, is it…"

    th "With that, the old man pulled out three of the fruits. Which one to pick?"

    menu ch4_4_1367_choice:
        # 【選択肢】×3 (сцена 1367)
        "The red fruit that looks like a tomato.{#ch4.4_c1367a}":
            # → scene 1368
            jump ch4_4_haruna_1368
        "The green fruit that looks like a cucumber.{#ch4.4_c1367b}":
            # → scene 1369
            jump ch4_4_haruna_1369
        "The yellow fruit that looks like a lemon.{#ch4.4_c1367c}":
            # → scene 1370
            jump ch4_4_haruna_1370

label ch4_4_haruna_1368:
    # ==== SCENE 1368 ==== (ветка «красный плод»; [lay5+lay7 — как в 1367]
    # [BGM +11 re-assert][BG +38])
    $ show_sprites(("ha 2", "s 2"))

    voice "ch4.4_s_017"
    s "Sir, I'll take this red fruit."

    voice "ch4.4_mer_007"
    merchant "There you go."

    # [lay7 +962 (ha 2) — re-assert]
    voice "ch4.4_ha_022"
    ha "Thank you, Hiraga-kun. Well then, let's try it."

    th "What would it taste like, I wonder…"

    # [lay7 +964 (ha 2 happy) 1B]
    $ show_sprites(("ha 2 happy", "s 2"))

    voice "ch4.4_ha_023"
    ha "Huh, this is sour."

    # [lay5 +434 (s 4) 2B]
    $ show_sprites(("ha 2 happy", "s 4"))

    voice "ch4.4_s_018"
    s "Whoa, it is. It's nothing at all like I imagined."

    # [lay7 +962 (ha 2) 1B]
    $ show_sprites(("ha 2", "s 4"))

    voice "ch4.4_ha_024"
    ha "Yes, it's strange, isn't it…"

    # → next scene 1371
    jump ch4_4_haruna_1371

label ch4_4_haruna_1369:
    # ==== SCENE 1369 ==== (ветка «зелёный плод»)
    $ show_sprites(("ha 2", "s 2"))

    voice "ch4.4_s_019"
    s "Sir, I'll take this green fruit."

    voice "ch4.4_mer_008"
    merchant "There you go.{#ch4.4_x3949}"

    # [lay7 +962 (ha 2) — re-assert]
    voice "ch4.4_ha_025"
    ha "Thank you, Hiraga-kun. Well then, let's try it.{#ch4.4_x1929}"

    th "What would it taste like, I wonder…{#ch4.4_m2}"

    # [lay7 +964 (ha 2 happy) 1B]
    $ show_sprites(("ha 2 happy", "s 2"))

    voice "ch4.4_ha_026"
    ha "Huh, this is sweet."

    # [lay5 +434 (s 4) 2B]
    $ show_sprites(("ha 2 happy", "s 4"))

    voice "ch4.4_s_020"
    s "Whoa, it is. It's nothing at all like I imagined.{#ch4.4_x9846}"

    # [lay7 +962 (ha 2) 1B]
    $ show_sprites(("ha 2", "s 4"))

    voice "ch4.4_ha_027"
    ha "Yes, it's strange, isn't it…{#ch4.4_x1931}"

    # → next scene 1371
    jump ch4_4_haruna_1371

label ch4_4_haruna_1370:
    # ==== SCENE 1370 ==== (ветка «жёлтый плод»)
    $ show_sprites(("ha 2", "s 2"))

    voice "ch4.4_s_021"
    s "Sir, I'll take this yellow fruit."

    voice "ch4.4_mer_009"
    merchant "There you go.{#ch4.4_x3950}"

    # [lay7 +962 (ha 2) — re-assert]
    voice "ch4.4_ha_028"
    ha "Thank you, Hiraga-kun. Well then, let's try it.{#ch4.4_x1932}"

    th "What would it taste like, I wonder…{#ch4.4_m3}"

    # [lay7 +964 (ha 2 happy) 1B]
    $ show_sprites(("ha 2 happy", "s 2"))

    voice "ch4.4_ha_029"
    ha "Huh, the inside is all jelly-like."

    # [lay5 +434 (s 4) 2B]
    $ show_sprites(("ha 2 happy", "s 4"))

    voice "ch4.4_s_022"
    s "Whoa, it is. It's nothing at all like I imagined.{#ch4.4_x9848}"

    # [lay7 +962 (ha 2) 1B]
    $ show_sprites(("ha 2", "s 4"))

    voice "ch4.4_ha_030"
    ha "Yes, it's strange, isn't it…{#ch4.4_x1934}"

    # → next scene 1371
    jump ch4_4_haruna_1371

label ch4_4_haruna_1371:
    # ==== SCENE 1371 ==== (общее схождение даты A; [lay5 +434 (s 4) 2B]
    # [lay7 +962 (ha 2) 1B][BGM +11 re-assert][BG +38][lay7 +964 (ha 2 happy)])
    $ show_sprites(("ha 2 happy", "s 4"))

    voice "ch4.4_ha_031"
    ha "But, but all the same, this may be tasty in its own way."

    # [lay5 +401 (s 2) 1B]
    $ show_sprites(("ha 2 happy", "s 2"))

    voice "ch4.4_s_023"
    s "You think so?"

    # [lay7 +962 (ha 2) 1B]
    $ show_sprites(("ha 2", "s 2"))

    voice "ch4.4_ha_032"
    ha "Yes.{#ch4.4_x1936}"

    # [lay5 +403 (s 2 happy) 1B]
    $ show_sprites(("ha 2", "s 2 happy"))

    voice "ch4.4_s_024"
    s "Good to hear, then."

    # [lay7 +964 (ha 2 happy) 1B]
    $ show_sprites(("ha 2 happy", "s 2 happy"))

    voice "ch4.4_ha_033"
    ha "Thank you, Hiraga-kun!"

    voice "ch4.4_mer_010"
    merchant "But say, the two of you do seem close. Are you husband and wife?"

    # [lay5 +442 (s 4 shy) 2B]
    $ show_sprites(("ha 2 happy", "s 4 shy"))

    voice "ch4.4_s_025"
    s "Wh-what!? N-no, nothing of the sort, not at all!"

    # [lay7 +970 (ha 2 shy) 1B]
    $ show_sprites(("ha 2 shy", "s 4 shy"))

    voice "ch4.4_ha_034"
    ha "Honestly, you old man, seriously!"

    voice "ch4.4_mer_011"
    merchant "Hah hah hah… the young ones have it good, truly they do!"

    # [lay5 +436 (s 4 happy) 2B]
    $ show_sprites(("ha 2 shy", "s 4 happy"))

    voice "ch4.4_s_026"
    s "Hah hah hah hah…"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay5 hide][lay7 hide][BG hide]
    stop music fadeout 1.0
    $ ch4_4_visited.add("store")
    # return (а не jump): карта вызвала лейбл через renpy.call (sprite_choice).
    return


label date_louise_ch4_4:
    # ==== DATES: B — дата с Луизой, аптека-витрина (сцены 1372–1376) ====
    # [BG +38 (town)][TRANS 1000][BGM +6 → t5] — спрайтов при входе нет
    $ fade_fx("town", new_music="t5")

    th "Louise was there—no wait, it looked like she was seriously peering into some shop's window."

    # [lay1 +302 (l 1) 1A]
    $ show_sprites(("l 1",))

    voice "ch4.4_l_010"
    l "Staaare."

    # 【好感度】ルイズ 20
    $ update_sympathy(20, char_key="louise")

    th "What was she so seriously looking at? I'd sneak a peek and find out, that's what."

    voice "ch4.4_l_011"
    l "Staaare.{#ch4.4_l4972}"

    th "The shop itself… was an ordinary one. In the window, bottles filled with liquid were on display."

    th "Hm. What would that liquid be, I wonder…"

    th "Judging from the size of those bottles, it wasn't a spice or a seasoning, but without a doubt… a medicine. It had to be."

    menu ch4_4_1372_choice:
        # 【選択肢】×3 (сцена 1372)
        "A love potion?{#ch4.4_c1372a}":
            # → scene 1373
            jump ch4_4_louise_1373
        "A cold medicine?{#ch4.4_c1372b}":
            # → scene 1374
            jump ch4_4_louise_1374
        "A cough medicine?{#ch4.4_c1372c}":
            # → scene 1375
            jump ch4_4_louise_1375

label ch4_4_louise_1373:
    # ==== SCENE 1373 ==== (ветка «любовное зелье»; [lay1 +302][BGM +6
    # re-assert][BG +38]) — мысли, без спрайт-событий
    th "A love potion? No, no—hold on. Who on earth would I even use it on?"

    th "Eh—could it be, me? That couldn't possibly be. Get a grip of yourself, me."

    # → next scene 1376
    jump ch4_4_louise_1376

label ch4_4_louise_1374:
    # ==== SCENE 1374 ==== (ветка «лекарство от простуды»)
    th "A cold medicine? Had Louise been ill right now?"

    th "Could it be she's sick, but with an important duty weighing on her, she's been keeping silent?"

    th "Whoa, that's bad news. Hang in there, Louise!"

    # → next scene 1376
    jump ch4_4_louise_1376

label ch4_4_louise_1375:
    # ==== SCENE 1375 ==== (ветка «лекарство для горла»)
    th "A cough medicine? Had her throat been hurting that badly?"

    th "Every day she does nothing but scold me, after all. Maybe her throat does hurt, then."

    th "When I think of it like that, some guilt starts gnawing at me…"

    # → next scene 1376
    jump ch4_4_louise_1376

label ch4_4_louise_1376:
    # ==== SCENE 1376 ==== (общее схождение даты B; [lay1 +302][BGM +6
    # re-assert][BG +38][lay1 +302 re-assert])
    $ show_sprites(("l 1",))

    voice "ch4.4_l_012"
    l "…Saito."

    th "Louise…{#ch4.4_m1376a}"

    # [lay1 hide → +307 (l 1 angry) level140 1A]
    $ show_sprites(("l 1 angry",))

    voice "ch4.4_l_013"
    l "Saito!{#ch4.4_x4974}"

    # [lay1 hide → +306 (l 1 angry) level160 1A][lay5 +394 (s 1 angry) 1A]
    $ show_sprites(("l 1 angry", "s 1 angry"))

    voice "ch4.4_s_027"
    s "Y-yeeesss!! Wh-what is it, yelling out of nowhere. You startled me, you know!"

    # [lay1 +302 (l 1) 1A]
    $ show_sprites(("l 1", "s 1 angry"))

    voice "ch4.4_l_014"
    l "The one surprised here is me. Why were you muttering to yourself behind my back?"

    # [lay1 +335 (l 3) 2A]
    $ show_sprites(("l 3", "s 1 angry"))

    voice "ch4.4_l_015"
    l "Saito, do you have some kind of habit like that, too?"

    # [lay5 +390 (s 1) 1A]
    $ show_sprites(("l 3", "s 1"))

    voice "ch4.4_s_028"
    s "N-no, it's just… you were staring so intently at that medicine there, so I was wondering what kind of medicine it was."

    # [lay1 +310 (l 1 shy) 1A]
    $ show_sprites(("l 1 shy", "s 1"))

    voice "ch4.4_l_016"
    l "A-a medicine? Wh-what does it matter what it is!"

    # [lay5 +423 (s 3) 2A]
    $ show_sprites(("l 1 shy", "s 3"))

    voice "ch4.4_s_029"
    s "Oh, but I can't help being curious about what you might be wanting."

    # [lay1 +302 (l 1) 1A]
    $ show_sprites(("l 1", "s 3"))

    voice "ch4.4_l_017"
    l "I'm not wanting. Not in the least, I don't need it."

    # [lay5 level=156][lay19 +946 (d 1 sad) level154 1A][lay1 level=155]
    $ show_sprites(("l 1", "d 1 sad", "s 3"))

    voice "ch4.4_d_001"
    d "…Somehow, that just feels like the end of the world, doesn't it."

    # [lay5 level=156][lay19 level=155][lay1 +308 (l 1 sad) level154 1A]
    $ show_sprites(("l 1 sad", "d 1 sad", "s 3"))

    voice "ch4.4_l_018"
    l "Huh?{#ch4.4_x4979}"

    # [lay5 level=156][lay19 level=154][lay1 level=155]
    $ show_sprites(("l 1 sad", "d 1 sad", "s 3"))

    voice "ch4.4_d_002"
    d "Well, I could just read the writing on that bottle… Hah… Doing all that would be a complete waste."

    # [lay19 hide][lay1 +310 (l 1 shy) level155 1A]
    $ show_sprites(("l 1 shy", "s 3"))

    voice "ch4.4_l_019"
    l "What—!"

    # [lay5 +390 (s 1) level156 1A]
    $ show_sprites(("l 1 shy", "s 1"))

    voice "ch4.4_s_030"
    s "Hey, Derflinger. Do you know what kind of medicine it is?"

    # [lay1 +302 (l 1) level155 1A]
    $ show_sprites(("l 1", "s 1"))

    voice "ch4.4_l_020"
    l "Derflinger…"

    # [lay5 level=156][lay19 +940 (d 1) level154 1A][lay1 level=155]
    $ show_sprites(("l 1", "d 1", "s 1"))

    voice "ch4.4_d_003"
    d "Huh?{#ch4.4_x1242}"

    # [lay1 +339 (l 3 angry) level154 2A][lay5 level=156][lay19 level=155]
    # [lay1 level=154]
    $ show_sprites(("l 3 angry", "d 1", "s 1"))

    voice "ch4.4_l_021"
    l "What sort of punishment would you prefer? To rust into a lump of iron? Or perhaps the bottom of the sea would suit you?"

    # [lay5 level=156][lay19 +946 (d 1 sad) level154 1A][lay1 level=155]
    $ show_sprites(("l 3 angry", "d 1 sad", "s 1"))

    voice "ch4.4_d_004"
    d "A-ah, me, I didn't see anything at all, and I don't know a thing, I swear. My mistake there, partner."

    # [lay19 hide][lay1 +302 (l 1) level155 1A]
    $ show_sprites(("l 1", "s 1"))

    voice "ch4.4_l_022"
    l "Yes—now that's right."

    # [lay5 +429 (s 3 sad) level156 2A]
    $ show_sprites(("l 1", "s 3 sad"))

    voice "ch4.4_s_031"
    s "Truly, what a strange lot you all are. Knowing about it, not knowing about it… In the end, what medicine is it even?"

    # [lay1 +310 (l 1 shy) level155 1A]
    $ show_sprites(("l 1 shy", "s 3 sad"))

    voice "ch4.4_l_023"
    l "It's fine for you not to know, Saito!"

    # [lay5 level=156][lay19 +940 (d 1) level154 1A][lay1 level=155]
    $ show_sprites(("l 1 shy", "d 1", "s 3 sad"))

    voice "ch4.4_d_005"
    d "No chance I could tell my partner it's a potion for making your chest bigger, you see."

    # [lay5 level=156][lay19 level=155][lay1 +306 (l 1 angry) level154 1A]
    $ show_sprites(("l 1 angry", "d 1", "s 3 sad"))

    voice "ch4.4_l_024"
    l "Did you just say something!?"

    # [lay5 level=156][lay19 +946 (d 1 sad) level154 1A][lay1 level=155]
    $ show_sprites(("l 1 angry", "d 1 sad", "s 3 sad"))

    voice "ch4.4_d_006"
    d "Oh no, no—it was nothing at all."

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000]
    # [lay5 hide][lay19 hide][lay1 hide][BG hide]
    stop music fadeout 1.0
    $ ch4_4_visited.add("apothecary")
    # return (а не jump): карта вызвала лейбл через renpy.call (sprite_choice).
    return


label date_siesta_ch4_4:
    # ==== DATES: C — дата с Сиестой, городская прогулка (сцены 1377–1381) ====
    # [BG +38 (town)][TRANS 1000][BGM +7 → t6][lay2 +491 (si 1 happy) 1A]
    $ fade_fx("town", new_music="t6", sprites=("si 1 happy",))

    voice "ch4.4_si_007"
    si "Ah… Saito-san!!"

    # 【好感度】シエスタ 20
    $ update_sympathy(20, char_key="siesta")

    # [lay2 x=-96][lay5 +401 (s 2) 1B] — Сиеста слева, Сайто справа
    $ show_sprites(("si 1 happy", "s 2"))

    voice "ch4.4_s_032"
    s "Oh—Siesta. You found me that easily, huh."

    # [lay2 +489 (si 1) 1A]
    $ show_sprites(("si 1", "s 2"))

    voice "ch4.4_si_008"
    si "It's simple, really. Your clothes, Saito-san, stand out terribly."

    # [lay5 +434 (s 4) 2B]
    $ show_sprites(("si 1", "s 4"))

    voice "ch4.4_s_033"
    s "Ah… true enough. There really isn't anyone else who would dress quite like this."

    # [lay2 +497 (si 1 shy) 1A]
    $ show_sprites(("si 1 shy", "s 4"))

    voice "ch4.4_si_009"
    si "That's right! No matter where I am, I'm confident I could find you straight away."

    # [lay5 +409 (s 2 shy) 1B]
    $ show_sprites(("si 1 shy", "s 2 shy"))

    voice "ch4.4_s_034"
    s "I-is that so?{#ch4.4_x9860}"

    # [lay2 +489 (si 1) 1A]
    $ show_sprites(("si 1", "s 2 shy"))

    voice "ch4.4_si_010"
    si "Saito-san. Actually, this isn't my first time in Tristania, you know."

    # [lay5 +401 (s 2) 1B]
    $ show_sprites(("si 1", "s 2"))

    voice "ch4.4_s_035"
    s "Eh, really?"

    # (lay9491 — re-assert)
    voice "ch4.4_si_011"
    si "Yes—my uncle actually runs a tavern here in Tristania, so I've visited here several times before."

    voice "ch4.4_s_036"
    s "Hm.{#ch4.4_s9862}"

    # [lay2 +495 (si 1 sad) 1A]
    $ show_sprites(("si 1 sad", "s 2"))

    voice "ch4.4_si_012"
    si "If the chance had come, I would have liked to go there, but it seems we won't have the time this visit."

    # [lay5 +440 (s 4 sad) 2B]
    $ show_sprites(("si 1 sad", "s 4 sad"))

    voice "ch4.4_s_037"
    s "Sorry about that. Dragging you here while things are quite hectic."

    # [lay2 +489 (si 1) 1A]
    $ show_sprites(("si 1", "s 4 sad"))

    voice "ch4.4_si_013"
    si "Not at all. I tagged along of my own accord, after all. That doesn't trouble me one bit."

    # [lay2 +491 (si 1 happy) 1A]
    $ show_sprites(("si 1 happy", "s 4 sad"))

    voice "ch4.4_si_014"
    si "More to the point, Saito-san—what do you make of this city, Tristania?"

    menu ch4_4_1377_choice:
        # 【選択肢】×3 (сцена 1377)
        "It's a big city.{#ch4.4_c1377a}":
            # → scene 1378
            jump ch4_4_siesta_1378
        "It's smaller than I expected.{#ch4.4_c1377b}":
            # → scene 1379
            jump ch4_4_siesta_1379
        "What do you think, Siesta?{#ch4.4_c1377c}":
            # → scene 1380
            jump ch4_4_siesta_1380

label ch4_4_siesta_1378:
    # ==== SCENE 1378 ==== (ветка «большой город»; [lay2 +491][lay5 +440]
    # [BGM +7 re-assert][BG +38][lay5 +401 (s 2) 1B])
    $ show_sprites(("si 1 happy", "s 2"))

    voice "ch4.4_s_038"
    s "Honestly, I just think: what a big city."

    # [lay2 +489 (si 1) 1A]
    $ show_sprites(("si 1", "s 2"))

    voice "ch4.4_si_015"
    si "Isn't it just? The first time I came to Tristania, I got completely lost."

    voice "ch4.4_si_016"
    si "These days I can walk around without losing my way to some extent, but until then it was quite an ordeal."

    # [lay5 +440 (s 4 sad) 2B]
    $ show_sprites(("si 1", "s 4 sad"))

    voice "ch4.4_s_039"
    s "Whoa—if even you could get lost in it, Siesta, I'd better not stray too far, huh."

    # [lay2 +524 (si 4 happy) 2A]
    $ show_sprites(("si 4 happy", "s 4 sad"))

    voice "ch4.4_si_017"
    si "No need to worry. If it's you, Saito-san, I will find you at any time."

    # 【好感度】シエスタ 10
    $ update_sympathy(10, char_key="siesta")
    # → next scene 1381
    jump ch4_4_siesta_1381

label ch4_4_siesta_1379:
    # ==== SCENE 1379 ==== (ветка «меньше, чем я думал»)
    $ show_sprites(("si 1 happy", "s 2"))

    voice "ch4.4_s_040"
    s "It's smaller than I expected."

    # [lay2 +495 (si 1 sad) 1A]
    $ show_sprites(("si 1 sad", "s 2"))

    voice "ch4.4_si_018"
    si "Is it? I was told it's about the third or fourth largest city in Halkeginia."

    # [lay5 +440 (s 4 sad) 2B]
    $ show_sprites(("si 1 sad", "s 4 sad"))

    voice "ch4.4_s_041"
    s "Ah, no—I meant that in my world's cities, the scale is far more overwhelming."

    # [lay2 +489 (si 1) 1A]
    $ show_sprites(("si 1", "s 4 sad"))

    voice "ch4.4_si_019"
    si "Is that so… I can't even imagine a city any bigger than Tristania."

    # 【好感度】シエスタ -10
    $ update_sympathy(-10, char_key="siesta")
    # → next scene 1381
    jump ch4_4_siesta_1381

label ch4_4_siesta_1380:
    # ==== SCENE 1380 ==== (ветка «Сиеста, как ты думаешь?»)
    $ show_sprites(("si 1 happy", "s 2"))

    voice "ch4.4_s_042"
    s "Rather—what do you think of it, Siesta?"

    # [lay2 +489 (si 1) 1A]
    $ show_sprites(("si 1", "s 2"))

    voice "ch4.4_si_020"
    si "Me… you mean? Well, let me see…"

    # [lay2 +524 (si 4 happy) 2A]
    $ show_sprites(("si 4 happy", "s 2"))

    voice "ch4.4_si_021"
    si "It's lively, it's bustling, and—I love it. Somehow it makes me feel like having fun myself, in a way."

    # [lay5 +403 (s 2 happy) 2B]
    $ show_sprites(("si 4 happy", "s 2 happy"))

    voice "ch4.4_s_043"
    s "Yeah, right you are."

    # → next scene 1381
    jump ch4_4_siesta_1381

label ch4_4_siesta_1381:
    # ==== SCENE 1381 ==== (общее схождение даты C; [lay2 +524 (si 4 happy)]
    # [lay5 +440 (s 4 sad)][BGM +7 re-assert][BG +38][lay2 +491 (si 1 happy)])
    $ show_sprites(("si 1 happy", "s 4 sad"))

    voice "ch4.4_si_022"
    si "Oh, that's right—there's a place around here selling delicious fruit, you know."

    # [lay2 +489 (si 1) 1A]
    $ show_sprites(("si 1", "s 4 sad"))

    voice "ch4.4_si_023"
    si "Would you like to go together, Saito-san?"

    # [lay5 +436 (s 4 happy) 2B]
    $ show_sprites(("si 1", "s 4 happy"))

    voice "ch4.4_s_044"
    s "Ah, that sounds nice."

    # [lay2 +491 (si 1 happy) 1A]
    $ show_sprites(("si 1 happy", "s 4 happy"))

    voice "ch4.4_si_024"
    si "Then let's head there together."

    # [lay5 +401 (s 2) 1B]
    $ show_sprites(("si 1 happy", "s 2"))

    voice "ch4.4_s_045"
    s "Yes.{#ch4.4_x9871}"

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000]
    # [lay2 hide][lay5 hide][BG hide]
    stop music fadeout 1.0
    $ ch4_4_visited.add("stroll")
    # return (а не jump): карта вызвала лейбл через renpy.call (sprite_choice).
    return


label date_street_ch4_4:
    # ==== DATES: D — пустая улица (сцена 1382; 4-й пункт карты, иконка 0) ====
    # [BG +38 (town)][TRANS 1000][BGM +31 → t30][lay5 +401 (s 2) 1B]
    $ fade_fx("town", new_music="t30", sprites=("s 2",))

    th "Looks like there's no one around here."

    voice "ch4.4_s_046"
    s "……{#ch4.4_x9872}"

    th "Well, we're not going to be doing anything in particular here either, so for now—let's move along."

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay5 hide][BG hide]
    stop music fadeout 1.0
    $ ch4_4_visited.add("street")
    # return (а не jump): карта вызвала лейбл через renpy.call (sprite_choice).
    return
