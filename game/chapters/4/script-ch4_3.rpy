# Глава 4, часть 3 (сцены 236–245): дорога в Тристанию. Падение поклажи на
# Сайто в качающейся карете (тряска vibrate(2), BG +123 — интерьер кареты —
# id-заглушка), обнаружение «безбилетницы» Сиесты в мешке (CG 122 → 124 → 125),
# меню выбора объяснения (сцены 237 «сестра» / 238 «служанка Луизы» /
# 239 «честно») → сход 240 → сон Сайто: японская школа, дневной журнал и
# «наказание» Харуной (CG 137/138, меню 242/243/244) → сход 245, тряска и
# пробуждение в карете (белая вспышка).
# Источник: ps2_source/chapters/chapter_05_トリスタニアの危機.txt (SCENE 236–245).
# Точные аргументы: ps2_source/events_full/chapter_05_トリスタニアの危機.txt.
#
# Голоса: ch4.3_<spk>_<NNN> — новая группа части 3, нумерация с 001 по говорящему:
#   s ×43, l ×21, si ×16, ha ×24, d ×3 (всего 107 голосов).
# Без голоса: мысли Сайто ×8 (236 ×4+1, 240 ×1, 241 ×1, 245 ×3) + 2 null-блока
#   сцены 245 (……………… , теги ch4.3_null_a/b) + молчаливая реплика Харуной в 236.
# Реплика si 14735 (стон из мешка) — говорящий отображается как «？？？» в источнике:
#   заведён одноразовый персонаж unk_si = Character(_("???")) (цвет Сиесты,
#   ряд в tl/japanese + tl/russian по old "???");
#   пара имя↔id в манифесте остаётся ch4.3_si_001 (голос Сиесты).
# SE (se1 +36 play/stop) — не портируются (AGENTS §6).
# TNDL tndl(-30) в 237 — не переносится (система не реализована, AGENTS §6).
# CG 122/124/125 (EVENT_CG) и 137/138, а также BG +123 — без имён файлов в
#   image_id_map.csv → заглушки id(122)/id(124)/id(125)/id(137)/id(138)/id(123)
#   (незарегистрированные сущности — в отчёте части).
# Спрайты: 403 (s 2 happy) зарегистрирован попиксельно (block 401 pos 2:
#   MAE 0.0269 норм., следующий 0.0276). Остальные id — из карты (в т.ч.
#   438/440/442 = блок 434 «s 4», чередуются с блоком 401 «s 2» — по канону).
# Слои level=/x=/y=/dir= источника не копируются — show_sprites расставляет
#   сам; см. комментарии по месту.
# Сочувствие: 【好感度】 Луиза −10 (237, 239), Сиеста +10 (237), Харуна −10 (242) —
#   4 вызова update_sympathy.
# Конец части: jump ch4_4 (сцена 246 — следующая часть; E7-долг, как у 4_2).

label ch4_3:
    # ==== SCENE 236 ==== (RESET: [SE se1 +36][BG +88 (sky)][BGM +5 → t4])
    $ fade_fx("sky", new_music="t4")

    th "How long have I been jolted around in this carriage since leaving the academy?"

    th "The sky's still bright. We should arrive around evening."

    voice "ch4.3_l_001"
    l "…Hoo… hoo…"

    voice "ch4.3_ha_001"
    ha "…Mm… mmh…"

    th "And there they are, cuddled up together, sound asleep."

    th "Well, we've been stuck in this carriage since morning, after all. No wonder… Maybe I'll get some shut-eye too?"

    # [BGM stop=1000][wait][vibrate на слоях][VIBRATE vibrate(2)][wait 800]
    # [BG сброс/скрытие — тряска, затем затемнение]
    stop music fadeout 1.0
    $ shake_fx(duration=0.8)

    # [BG +123 (интерьер кареты, id-заглушка)][TRANS][BGM +30 → t29][lay5 +405
    # (s 2 angry) dir=1B]
    $ fade_fx("id(123)", new_music="t29", sprites=("s 2 angry",))

    voice "ch4.3_s_001"
    s "Ugh… What a wretched road this is!!"

    # [lay5 +438 (s 4 angry) dir=2B]
    $ show_sprites(("s 4 angry",))

    voice "ch4.3_s_002"
    s "And now the luggage that was piled up is toppling over… Wha…?"

    # [lay5 +440 (s 4 sad) dir=2B]
    $ show_sprites(("s 4 sad",))

    voice "ch4.3_s_003"
    s "Gwah… Ouch… This thing weighs a ton… What the heck is packed in here anyway?"

    # [lay5 x=224 — сдвиг][lay19 +940 (d 1) dir=1A]
    $ show_sprites(("d 1", "s 4 sad"))

    voice "ch4.3_d_001"
    d "What's the matter, partner? You were groaning up quite a storm there."

    # [lay5 +407 (s 2 sad) dir=1B]
    $ show_sprites(("d 1", "s 2 sad"))

    voice "ch4.3_s_004"
    s "The carriage lurched, and the luggage standing upright came crashing down on me."

    voice "ch4.3_si_001"
    unk_si "…Mmh…"

    # [lay5 +405 (s 2 angry) dir=1B]
    $ show_sprites(("d 1", "s 2 angry"))

    voice "ch4.3_s_005"
    s "Whoa-whoa! Th-the luggage talked!!"

    # [lay19 +942 (d 1 happy) dir=1A]
    $ show_sprites(("d 1 happy", "s 2 angry"))

    voice "ch4.3_d_002"
    d "The luggage talks? You starting to doze off for real, partner?"

    # [lay5 +438 (s 4 angry) dir=2B]
    $ show_sprites(("d 1 happy", "s 4 angry"))

    voice "ch4.3_s_006"
    s "Hey, of all things, I don't need to hear that from you… Or is this a world where absolutely everything talks?"

    # [lay2/lay5/lay19 hide][BG hide][EVENT_CG +122 (Луиза злится, id-заглушка)][TRANS]
    # — CG вместо тройки спрайтов (пасьянс "что за багаж" в мешке)
    $ fade_fx("id(122)", type="cg")

    voice "ch4.3_l_002"
    l "…Would you keep it down. I can't sleep a wink."

    voice "ch4.3_s_007"
    s "The luggage piled over there fell on top of me. Then the luggage talked. And somehow it was soft…"

    voice "ch4.3_l_003"
    l "Saito, what on earth are you talking about?"

    voice "ch4.3_s_008"
    s "A-anyway, let's open it up and check what's inside."

    # [lay5/lay1 hide][BG hide][EVENT_CG hide][wait][EVENT_CG +124][TRANS]
    $ fade_fx("id(124)", type="cg")

    voice "ch4.3_si_002"
    si "Ahaha, I came strolling along with you!"

    voice "ch4.3_l_004"
    l "……。{#ch4.3_sil001}"

    ha "……。{#ch4.3_sil002}"

    voice "ch4.3_s_009"
    s "……。{#ch4.3_sil003}"

    voice "ch4.3_d_003"
    d "……。{#ch4.3_sil004}"

    # [EVENT_CG imageType=1 +125][waitLoad] — прямая смена CG на том же слое
    $ dissolve_fx("id(125)", type="cg")

    voice "ch4.3_si_003"
    si "…Tee-hee."

    voice "ch4.3_ha_002"
    ha "W-why is Siesta, the one on house-guard duty, here of all places?"

    # [lay2/5/19/1/7 hide][EVENT_CG hide][wait][EVENT_CG +122][TRANS]
    $ fade_fx("id(122)", type="cg")

    voice "ch4.3_l_005"
    l "Tie the mouth of that luggage bag shut right now!"

    voice "ch4.3_si_004"
    si "Eh!?{#ch4.3_eh14738}"

    voice "ch4.3_s_010"
    s "Why would you!?"

    voice "ch4.3_l_006"
    l "We throw it out. If we're lucky, a troupe of entertainers will pick her up."

    # [lay2/lay5/lay1 hide][EVENT_CG hide][wait][msgon] — мысль на чёрном
    $ fade_fx()

    th "…Hold on, Louise!! You're really pulling the bag's mouth tight!!"

    # [lay5 hide][BG +123 (интерьер кареты)][TRANS][lay2 +526 (si 4 angry)][msgon]
    $ fade_fx("id(123)")

    $ show_sprites(("si 4 angry",))

    voice "ch4.3_si_005"
    si "I-I'm sorry, Miss Vallière!! Forgive me, please… Ugyaaaaah!?"

    # [lay2 x=-96 — сдвиг][lay5 +405 (s 2 angry) dir=1B]
    $ show_sprites(("si 4 angry", "s 2 angry"))

    voice "ch4.3_s_011"
    s "Hey, you can't be serious!? Calm down, Louise!!"

    # [lay2 +495 (si 1 sad) dir=1A]
    $ show_sprites(("si 1 sad", "s 2 angry"))

    voice "ch4.3_si_006"
    si "P-please, I'll be useful to everyone! I'll work as hard as I can, so p-please l-let me come along!!"

    # [lay2 hide][lay1 +306 (l 1 angry) dir=1A] — Сиеста скрыта; Сайто (s 2 angry) остаётся
    $ show_sprites(("l 1 angry", "s 2 angry"))

    voice "ch4.3_l_007"
    l "I told Siesta she was to stay behind! Unless… this was YOUR doing, Saito…!"

    # [lay5 +440 (s 4 sad) dir=2B]
    $ show_sprites(("l 1 angry", "s 4 sad"))

    voice "ch4.3_s_012"
    s "Wh-whoa, hold on. You really think I'd do something like that?"

    # [lay5 hide][lay2 +495 (si 1 sad) dir=1A x=224] — Луиза справа… нет: Луиза (l angry)
    # остаётся слева, Сиеста появляется справа
    $ show_sprites(("l 1 angry", "si 1 sad"))

    voice "ch4.3_si_007"
    si "I'm sorry, Miss Vallière. Saito-san is not at fault. It was entirely my own decision."

    # [lay1 +308 (l 1 sad) dir=1A]
    $ show_sprites(("l 1 sad", "si 1 sad"))

    voice "ch4.3_l_008"
    l "Siesta…{#ch4.3_t6080}"

    voice "ch4.3_si_008"
    si "I was worried about Haruna-san and Saito-san, and… somehow I ended up sneaking aboard like a stowaway."

    # [lay1 +302 (l 1) dir=1A]
    $ show_sprites(("l 1", "si 1 sad"))

    voice "ch4.3_l_009"
    l "It does bother me a little that I wasn't the one brought along… But Saito, what exactly do you intend to do?"

    # [lay2 hide][lay5 +440 (s 4 sad) dir=2B] — Луиза (l 1) слева, Сайто справа
    $ show_sprites(("l 1", "s 4 sad"))

    voice "ch4.3_s_013"
    s "What can I say to that… But we can't very well head back to the academy like this, can we?"

    # [lay1 +339 (l 3 angry) dir=2A]
    $ show_sprites(("l 3 angry", "s 4 sad"))

    voice "ch4.3_l_010"
    l "We go straight on to the royal palace! There's no reason THEY should take her along, is there?"

    # [lay5 hide][lay2 +495 (si 1 sad) dir=1A x=224] — Луиза (l 3 angry) слева,
    # Сиеста справа
    $ show_sprites(("l 3 angry", "si 1 sad"))

    voice "ch4.3_si_009"
    si "……。{#ch4.3_sil005}"

    # [lay1 +302 (l 1) dir=1A]
    $ show_sprites(("l 1", "si 1 sad"))

    voice "ch4.3_l_011"
    l "Saito. How exactly do you plan to explain Siesta?"

    # [lay2 hide][lay5 +407 (s 2 sad) dir=1B] — Луиза (l 1) слева, Сайто справа
    $ show_sprites(("l 1", "s 2 sad"))

    voice "ch4.3_s_014"
    s "As for Siesta, well…"

    # ==== 【選択肢】 (236) → 237/238/239, сходятся в 240 ====
    menu:

        "Say she's my little sister.{#ch4.3_m236a}":
            jump ch4_3_237

        "Say she's Louise's maid.{#ch4.3_m236b}":
            jump ch4_3_238

        "I think we should just tell the truth.{#ch4.3_m236c}":
            jump ch4_3_239


label ch4_3_237:
    # ==== SCENE 237 ==== (RESET: [lay1 +302 (l 1)][lay5 +407 (s 2 sad)][BGM +30 —
    # уже t29][SE se1 +36 — SE не портируется][BG +123 (интерьер кареты)];
    # далее [lay5 +442 (s 4 shy) dir=2B] перед репликой)
    $ show_sprites(("l 1", "s 4 shy"))

    voice "ch4.3_s_015"
    s "So, I'm to explain her as my sister?"

    # [lay1 +306 (l 1 angry) dir=1A]
    $ show_sprites(("l 1 angry", "s 4 shy"))

    voice "ch4.3_l_012"
    l "…Hah!?"

    # 【好感度】ルイズ -10; tndl(-30) — не портируется
    $ update_sympathy(-10, char_key="louise")

    # [lay1 hide][lay2 +497 (si 1 shy) dir=1A]
    $ show_sprites(("si 1 shy", "s 4 shy"))

    voice "ch4.3_si_010"
    si "Eh!?{#ch4.3_eh14744}"

    # [lay5 +403 (s 2 happy) dir=1B]
    $ show_sprites(("si 1 shy", "s 2 happy"))

    voice "ch4.3_s_016"
    s "Look, Siesta has black hair and black eyes, right? I figure calling her my little sister would pass just fine."

    voice "ch4.3_si_011"
    si "U-um… Should I call you 'big bro'? Or maybe 'esteemed elder brother'?"

    # [lay2 +530 (si 4 shy) dir=2A]
    $ show_sprites(("si 4 shy", "s 2 happy"))

    voice "ch4.3_si_012"
    si "Aah, which should I go with!? Now I'm all torn…"

    # 【好感度】シエスタ 10
    $ update_sympathy(10, char_key="siesta")

    # [lay2 hide][lay1 +306 (l 1 angry) dir=1A]
    $ show_sprites(("l 1 angry", "s 2 happy"))

    voice "ch4.3_l_013"
    l "You needn't agonize over that! Have you got any other ideas?"

    # [lay5 +401 (s 2) dir=1B]
    $ show_sprites(("l 1 angry", "s 2"))

    voice "ch4.3_s_017"
    s "Well then — how about telling her she's Louise's maid?"

    # [lay1 +302 (l 1) dir=1A]
    $ show_sprites(("l 1", "s 2"))

    voice "ch4.3_l_014"
    l "Well… I suppose that's a reasonable option. It'll do, won't it?"

    # [lay1/lay5 hide][BG hide → BG +88 (sky)][TRANS] → 240
    $ fade_fx("sky")

    jump ch4_3_240


label ch4_3_238:
    # ==== SCENE 238 ==== (RESET: [lay1 +302 (l 1)][lay5 +407 (s 2 sad)][BGM +30 —
    # уже t29][SE se1 +36 — SE не портируется][BG +123];
    # далее [lay5 +401 (s 2) dir=1B] перед репликой)
    $ show_sprites(("l 1", "s 2"))

    voice "ch4.3_s_018"
    s "How about the idea that she's Louise's maid?"

    # [lay1 +302 (l 1) dir=1A — переутверждение]
    $ show_sprites(("l 1", "s 2"))

    voice "ch4.3_l_015"
    l "Well, I suppose that's a reasonable option. It'll do, won't it?{#ch4.3_d6087}"

    # [lay5 hide][lay2 +491 (si 1 happy) dir=1A x=224] — Луиза (l 1) слева,
    # Сиеста справа
    $ show_sprites(("l 1", "si 1 happy"))

    voice "ch4.3_si_013"
    si "Yes! In Saito-san's place, I'll take care of everything around you."

    # [lay1 +335 (l 3) dir=2A]
    $ show_sprites(("l 3", "si 1 happy"))

    voice "ch4.3_l_016"
    l "Something about that phrasing bothers me… But fine, whatever."

    # [lay1/lay2 hide][BG hide → BG +88 (sky)][TRANS] → 240
    $ fade_fx("sky")

    jump ch4_3_240


label ch4_3_239:
    # ==== SCENE 239 ==== (RESET: [lay1 +302 (l 1)][lay5 +407 (s 2 sad)][BGM +30 —
    # уже t29][SE se1 +36 — SE не портируется][BG +123];
    # далее [lay5 +440 (s 4 sad) dir=2B] перед репликой)
    $ show_sprites(("l 1", "s 4 sad"))

    voice "ch4.3_s_019"
    s "Just say it straight. She's the princess — she'll surely understand."

    # [lay1 +308 (l 1 sad) dir=1A]
    $ show_sprites(("l 1 sad", "s 4 sad"))

    voice "ch4.3_l_017"
    l "…I know full well that's our only option… And lying gets us nowhere, after all."

    # 【好感度】ルイズ -10
    $ update_sympathy(-10, char_key="louise")

    # [lay5 +401 (s 2) dir=1B]
    $ show_sprites(("l 1 sad", "s 2"))

    voice "ch4.3_s_020"
    s "Right then… Good for you, Siesta."

    # [lay1 +302 (l 1) dir=1A]
    $ show_sprites(("l 1", "s 2"))

    voice "ch4.3_l_018"
    l "But no."

    # [lay5 hide][lay2 +493 (si 1 angry) dir=1A]
    $ show_sprites(("l 1", "si 1 angry"))

    voice "ch4.3_si_014"
    si "Eh!?{#ch4.3_eh14748}"

    # [lay1 +335 (l 3) dir=2A]
    $ show_sprites(("l 3", "si 1 angry"))

    voice "ch4.3_l_019"
    l "We'll simply have her go down as my maid. Otherwise all sorts of problems will come up…"

    # [lay2 +489 (si 1) dir=1A]
    $ show_sprites(("l 3", "si 1"))

    voice "ch4.3_si_015"
    si "Yes, understood!"

    # [lay1/lay2 hide][BG hide → BG +88 (sky)][TRANS] → 240
    $ fade_fx("sky")

    jump ch4_3_240


label ch4_3_240:
    # ==== SCENE 240 ==== (RESET: [BGM +30 — уже t29][SE se1 +36][BG +88 (sky)] —
    # возможность переутверждена веткой) — мысль Сайто, затем остановки.
    th "Well, and that's how it went… In the end, the three of us — Louise, Haruna, and Siesta — set off for the royal palace."

    # [SE se1 stop ×2 — SE не портируются][BGM stop=1000][lay5 hide][BG hide]
    stop music fadeout 1.0

    jump ch4_3_241


label ch4_3_241:
    # ==== SCENE 241 ==== (RESET: [BG +89 (sky_evening)][TRANS][BGM +4 → t3])
    $ fade_fx("sky_evening", new_music="t3")

    voice "ch4.3_s_021"
    s "……。{#ch4.3_sil006}"

    voice "ch4.3_ha_003"
    ha "…Hiraga-kun."

    voice "ch4.3_s_022"
    s "Mmmh…?"

    voice "ch4.3_ha_004"
    ha "Hiraga-kun, I said…"

    voice "ch4.3_s_023"
    s "Oh, sorry… We've arrived in Tristania, haven't we?"

    # [lay5/lay7 hide][BG hide][wait][EVENT_CG +137 — класс в Японии (id-заглушка)][TRANS]
    $ fade_fx("id(137)", type="cg")

    voice "ch4.3_ha_005"
    ha "Honestly… What are you dozing off for? School let out ages ago."

    voice "ch4.3_s_024"
    s "…!?"

    voice "ch4.3_s_025"
    s "Huh…? Wait, isn't this a school?"

    th "Looking around, I can pick out quite a few familiar classmates."

    voice "ch4.3_ha_006"
    ha "School let out, and you're STILL sleeping, Hiraga-kun. You slept through every class today, didn't you?"

    voice "ch4.3_s_026"
    s "Huh, I slept that much? Now I'm in trouble."

    voice "ch4.3_ha_007"
    ha "And besides — today it's YOUR day on hall duty, Hiraga-kun. You'd better get that class journal written."

    voice "ch4.3_s_027"
    s "Oh? Is that a fact?"

    # [EVENT_CG imageType=1 +138 — классный журнал (id-заглушка)][waitLoad]
    $ dissolve_fx("id(138)", type="cg")

    voice "ch4.3_ha_008"
    ha "'Is that a fact,' really…? Today WE were the duty reps, both of us! I did practically all the work, mind you."

    voice "ch4.3_s_028"
    s "Oh… that's right, sorry. It's just that something feels a bit off with me."

    # [EVENT_CG +137 — обратно (id-заглушка)][waitLoad]
    $ dissolve_fx("id(137)", type="cg")

    voice "ch4.3_ha_009"
    ha "Good grief… I'll keep an eye on you right here."

    voice "ch4.3_ha_010"
    ha "But the class journal you WILL write properly, understand?"

    voice "ch4.3_s_029"
    s "Ugh.{#ch4.3_t11510}"

    voice "ch4.3_ha_011"
    ha "Come on now, no gawking. Hurry up and write, Hiraga-kun! We do want to head home together, don't we?"

    # ==== 【選択肢】 (241) → 242/243/244, сходятся в 245 ====
    menu:

        "Ask her to handle the class journal too.{#ch4.3_m241a}":
            jump ch4_3_242

        "Say you feel unwell and go to the infirmary.{#ch4.3_m241b}":
            jump ch4_3_243

        "What day of the week was it again?{#ch4.3_m241c}":
            jump ch4_3_244


label ch4_3_242:
    # ==== SCENE 242 ==== (RESET: [BGM +4 — уже t3][EVENT_CG +137 — id(137),
    # переутверждение после Dissolve 137 на/menu])
    voice "ch4.3_s_030"
    s "Come on, with all that energy — handle the class journal for me too!"

    # [EVENT_CG imageType=1 +138 (id-заглушка)][waitLoad]
    $ dissolve_fx("id(138)", type="cg")

    voice "ch4.3_ha_012"
    ha "Oh no you don't! That's just plain unfair — I'M the one doing everything!?"

    # 【好感度】ハルナ -10
    $ update_sympathy(-10, char_key="haruna")

    # [EVENT_CG +137 (id-заглушка)][waitLoad] → 245
    $ dissolve_fx("id(137)", type="cg")

    jump ch4_3_245


label ch4_3_243:
    # ==== SCENE 243 ==== (RESET: [BGM +4 — уже t3][EVENT_CG +137 — id(137)])
    voice "ch4.3_s_031"
    s "The thing is, I'm not feeling so well… Mind if I go to the infirmary?"

    voice "ch4.3_ha_013"
    ha "Hmm — but your sleep-talk sounded pretty jolly. You were even dreaming of being surrounded by girls."

    voice "ch4.3_s_032"
    s "Wh—, seriously!?"

    voice "ch4.3_ha_014"
    ha "Yeah, so… That request is rejected."

    jump ch4_3_245


label ch4_3_244:
    # ==== SCENE 244 ==== (RESET: [BGM +4 — уже t3][EVENT_CG +137 — id(137)])
    voice "ch4.3_s_033"
    s "What day was today again? Could it be Friday?"

    voice "ch4.3_ha_015"
    ha "Monday, obviously. Really, are you all right, Hiraga-kun?"

    jump ch4_3_245


label ch4_3_245:
    # ==== SCENE 245 ==== (RESET: [BGM +4 — уже t3][EVENT_CG +137 — id(137)];
    # затем [lay7/lay5 hide][EVENT_CG hide][wait][BG +89 (sky_evening)][TRANS])
    $ fade_fx("sky_evening")

    th "………………{#ch4.3_null_a}"

    # [BG hide][wait][EVENT_CG +137 (id-заглушка)][TRANS]
    $ fade_fx("id(137)", type="cg")

    voice "ch4.3_s_034"
    s "There, that'll do, right?"

    voice "ch4.3_ha_016"
    ha "Let's see… Hmm, I suppose that'll pass? Though your journal is one big block of lies."

    voice "ch4.3_s_035"
    s "Well, I slept through the whole day, after all."

    voice "ch4.3_ha_017"
    ha "Be more careful tomorrow, OK? You've been getting warnings from the teacher lately."

    voice "ch4.3_s_036"
    s "Yes, ma'am."

    voice "ch4.3_ha_018"
    ha "And a Hiraga-kun like that gets PUNISHED!"

    # [BGM stop=1000][wait 1000][BGM +27 → t26]
    stop music fadeout 1.0
    pause(1.0)
    play music t26 fadein 1.0

    voice "ch4.3_s_037"
    s "P-punished!? …Wait, with what?"

    voice "ch4.3_ha_019"
    ha "Well, you LOVE punishments, right? Punishments."

    voice "ch4.3_ha_020"
    ha "Louise-san told me: Hiraga-kun just loves getting punished."

    voice "ch4.3_s_038"
    s "Louise-san? Who's that?"

    voice "ch4.3_ha_021"
    ha "Eh, who was that again?"

    voice "ch4.3_s_039"
    s "W-wait, what's that ball of light!?"

    voice "ch4.3_ha_022"
    ha "Hmm… magic?"

    voice "ch4.3_s_040"
    s "M-magic? Wait, Haruna!! Cut it out!!!"

    # [EVENT_CG imageType=1 +138 (id-заглушка)][waitLoad]
    $ dissolve_fx("id(138)", type="cg")

    voice "ch4.3_ha_023"
    ha "No protests accepted!"

    voice "ch4.3_s_041"
    s "Uwaaaaaah."

    # [lay5 hide][vibrate на слоях][VIBRATE vibrate(2)][wait 800][слои сбрасываются,
    # BG скрыт; BGM stop] — тряска до остановки музыки (порядок источника)
    $ shake_fx(duration=0.8)

    stop music fadeout 1.0

    # [LAYER white +2][wait][lay1 +302 (l 1)][BG +123 (интерьер кареты)]
    # [EVENT_CG hide][TRANS crossfade 0][LAYER hide][BGM +4 → t3] —
    # пробуждение: белая вспышка закрывает смену сцены
    $ flash_fx("id(123)", sprites=("l 1",))

    play music t3 fadein 1.0

    voice "ch4.3_l_020"
    l "Saito? What's wrong? You were asleep one moment, and now you suddenly cry out."

    # [lay1 x=-96 — сдвиг][lay5 +407 (s 2 sad) dir=1B]
    $ show_sprites(("l 1", "s 2 sad"))

    voice "ch4.3_s_042"
    s "Where am I?"

    voice "ch4.3_l_021"
    l "We're still on the highway. What's the matter?"

    # [lay1 hide][lay2 +495 (si 1 sad) dir=1A]
    $ show_sprites(("si 1 sad", "s 2 sad"))

    voice "ch4.3_si_016"
    si "Saito-san, you're sweating buckets! What sort of nightmare was it?"

    # [lay5 +440 (s 4 sad) dir=2B]
    $ show_sprites(("si 1 sad", "s 4 sad"))

    voice "ch4.3_s_043"
    s "N-no, it was nothing…"

    # [lay5 +407 (s 2 sad) dir=1B]
    $ show_sprites(("si 1 sad", "s 2 sad"))

    th "Why did I even dream something like that? And Haruna doing magic? Impossible…"

    th "Probably that simply got mixed up in my head with Louise's usual punishments."

    # [lay2 hide][lay7 +962 (ha 2) x=-96] — Харуна слева, Сайто справа
    $ show_sprites(("ha 2", "s 2 sad"))

    voice "ch4.3_ha_024"
    ha "…?"

    th "I'll just sleep it off again…"

    # [lay7/lay5 hide][BG hide][msgon]
    $ fade_fx()

    th "………………{#ch4.3_null_b}"

    # [SE se1 stop ×2 — SE не портируются][BGM stop=1000][BG stage hide]
    stop music fadeout 1.0

    jump ch4_4
