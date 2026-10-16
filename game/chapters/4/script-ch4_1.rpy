# Глава 4, часть 1 (сцены 219–224): титульная карточка, заседание Совета
# (Корбеар, Луиза, Харуна, Осман, Табита, Гиш, Монморанси) и выбор, как
# объяснить поцелуй. Титульная карточка: K=9. Вход — jump ch4 из ch3_8_213
# (E7 ч. 3 закрывается этим лейблом); выход — jump ch4_2.
# Источник: ps2_source/chapters/chapter_05_トリスタニアの危機.txt (SCENE 219–224).
# Точные аргументы: ps2_source/events_full/chapter_05_トリスタニアの危機.txt.
# Голоса: ch4_s_001…, ch4_l_001…, ch4_c_001…, ch4_o_001…, ch4_ha_001…,
#         ch4_t_001…, ch4_g_001…, ch4_m_001…, ch4_si_001…, ch4_k_001… (124).
# Без голоса: мысли сайта ×4 (219 ×3, 223 ×1) + null ×2 (223-мысль, 224-пауза)
#         + null Табиты (224).
# ITEM ×3 (パン/ハーブ/エリクサー) — не портируются (система не реализована).
# SE (se0 +56 в 224, se1 stop ×2) не портируются.
# Титульный монтаж (BG 2/1145/1131/1145/2) → overlay_screen (образ «overlay»).
# Спрайты: 13 кодов; +2 регистрации — 920 = o 1 happy, 926 = o 1 shy.

label ch4:
    call overlay_screen("overlay", "Chapter Four: 'Crisis in Tristania'", isUseBlur=False, text_mode="black") from _call_overlay_screen_9
    pause(2)

    # ==== SCENE 219 ====
    # [TITLE title("トリスタニアの危機")][BG 2/1145/1131/1145/2 — титульный
    # монтаж → overlay_screen выше][ITEM パン/ハーブ/エリクサー — не портируются]
    # [BGM play=+5] → t4; [BG +88 (sky)]
    $ fade_fx("sky", new_music="t4")

    th "…Because of the Louise-and-Kirche commotion, Haruna's secret got out to the academy…{#ch4_th_219a}"
    th "…And now we have to explain the situation to the Headmaster…{#ch4_th_219b}"
    th "…All I can do is pray Haruna doesn't get expelled…{#ch4_th_219c}"

    # [BGM stop=1000][lay5 hide][BG hide][BG +29 (osman_cabinet)][BGM play=+32] → t31
    stop music fadeout 1.0
    $ fade_fx("osman_cabinet", new_music="t31")

    # [lay9 +929 (c 1)]
    $ show_sprites(("c 1",))

    voice "ch4_c_001"
    c "I didn't gather you all here this early for nothing."

    voice "ch4_c_002"
    c "I'd like Miss Vallière to explain about the woman she was letting stay at the academy without permission."

    # [lay9 x=224 — сдвиг][lay1 +302 (l 1)]
    $ show_sprites(("l 1", "c 1"))

    voice "ch4_l_001"
    l "Before I explain, allow me to speak. This woman — Haruna — has done the academy no harm."

    voice "ch4_l_002"
    l "The one who caused the harm is me. If punishment is to be given, give it to me alone."

    voice "ch4_l_003"
    l "Not that I'm offering a trade, but I hope Haruna will be treated leniently."

    # [lay9 hide][lay1 hide][lay5 +396 (s 1 sad)][lay7 +957 (ha 1 sad)]
    $ show_sprites(("ha 1 sad", "s 1 sad"))

    voice "ch4_s_001"
    s "Louise…{#ch4_s_001}"

    voice "ch4_ha_001"
    ha "Louise…{#ch4_ha_001}"

    # [lay5 hide][lay7 hide][lay9 +929 (c 1)]
    $ show_sprites(("c 1",))

    voice "ch4_c_003"
    c "Miss Vallière. I understand how you feel.{#ch4_c_003}"

    voice "ch4_c_004"
    c "But the academy has rules. Academy life is about observing those rules…"

    # [lay9 x=224 — сдвиг][lay10 +918 (o 1)]
    $ show_sprites(("c 1", "o 1"))

    voice "ch4_o_001"
    o "Mister Colbert, that will be quite enough."

    voice "ch4_o_002"
    o "Neither Miss Vallière nor the rest of you broke the rules on purpose."

    voice "ch4_o_003"
    o "There were reasons. Surely that's so."

    # [lay9 +935 (c 1 sad)]
    $ show_sprites(("c 1 sad", "o 1"))

    voice "ch4_c_005"
    c "No, but Headmaster…"

    # [lay10 +920 (o 1 happy)]
    $ show_sprites(("c 1 sad", "o 1 happy"))

    voice "ch4_o_004"
    o "Er, the young lady over there. Might I ask your name once more?"

    # [lay9 hide][lay7 +951 (ha 1)]
    $ show_sprites(("o 1 happy", "ha 1"))

    voice "ch4_ha_002"
    ha "Yes… Nice to meet you. I am Takanagi Haruna."

    # [lay10 +918 (o 1)]
    $ show_sprites(("o 1", "ha 1"))

    voice "ch4_o_005"
    o "Takanagi Haruna… Shall I call you Miss Haruna?"

    # [lay7 +957 (ha 1 sad)]
    $ show_sprites(("o 1", "ha 1 sad"))

    voice "ch4_ha_003"
    ha "No, um… Haruna is fine for me. 'Miss Haruna' — well… I'm not of that station…"

    voice "ch4_o_006"
    o "…I see. Then I shall call you as such… Ahem."

    voice "ch4_o_007"
    o "As Miss Vallière said, Haruna came from another world… is that the story?"

    # [lay7 +951 (ha 1)]
    $ show_sprites(("o 1", "ha 1"))

    voice "ch4_ha_004"
    ha "Yes… The world I lived in is a different world from this one."

    voice "ch4_o_008"
    o "My… How very interesting."

    # [lay7 hide][lay5 +390 (s 1)]
    $ show_sprites(("o 1", "s 1"))

    voice "ch4_s_002"
    s "Haruna was my classmate. She served as class president at the school I attended."

    voice "ch4_o_009"
    o "A classmate, you say?"

    voice "ch4_s_003"
    s "Yes. So I knew her, or rather, we were acquaintances…"

    voice "ch4_s_004"
    s "And so I asked Louise, and she let me stay here."

    # [lay10 hide][lay9 +933 (c 1 angry)]
    $ show_sprites(("s 1", "c 1 angry"))

    voice "ch4_c_006"
    c "What — from the same world as you, Saito?"

    # [lay9 +929 (c 1)]
    $ show_sprites(("s 1", "c 1"))

    voice "ch4_c_007"
    c "Then it's possible that Haruna, too, is a familiar summoned to this world."

    # [lay5 hide][lay7 +957 (ha 1 sad)]
    $ show_sprites(("c 1", "ha 1 sad"))

    voice "ch4_ha_005"
    ha "A familiar!?"

    # [lay9 +935 (c 1 sad)]
    $ show_sprites(("c 1 sad", "ha 1 sad"))

    voice "ch4_c_008"
    c "Well, there was no precedent for you either, Saito, so I can't say for certain…"

    # [lay9 +929 (c 1)]
    $ show_sprites(("c 1", "ha 1 sad"))

    voice "ch4_c_009"
    c "We don't know whether the trigger for people and things from other worlds arriving is a natural phenomenon or something artificial."

    voice "ch4_c_010"
    c "For the record, your arrival was certainly due to Miss Vallière's summoning magic."

    # [lay9 hide][lay10 +918 (o 1)]
    $ show_sprites(("ha 1 sad", "o 1"))

    voice "ch4_o_010"
    o "Then, Haruna. Can you explain how you came to this world?"

    # [lay7 +951 (ha 1)]
    $ show_sprites(("ha 1", "o 1"))

    voice "ch4_ha_006"
    ha "No — I was walking home from school when everything went bright, and then I was here. So I don't know the details."

    # [lay7 +957 (ha 1 sad)]
    $ show_sprites(("ha 1 sad", "o 1"))

    voice "ch4_ha_007"
    ha "After that, strangers grabbed me, I ran away…"

    # [lay7 +951 (ha 1)]
    $ show_sprites(("ha 1", "o 1"))

    voice "ch4_ha_008"
    ha "Just when I had no idea what would happen, Hiraga-kun, Louise, and Siesta saved me."

    voice "ch4_o_011"
    o "My… How very mysterious. Just what could have guided you both to this world?"

    # [lay7 hide][lay9 +929 (c 1)]
    $ show_sprites(("o 1", "c 1"))

    voice "ch4_c_011"
    c "The crest — how shall we confirm the Contract Servant? …Osmond."

    # [lay10 hide][lay9 hide][lay7 +957 (ha 1 sad)]
    $ show_sprites(("ha 1 sad",))

    voice "ch4_ha_009"
    ha "…Hm? Con-tract Ser-vant? What's that, Hiraga-kun?"

    # [lay7 x=-96 — сдвиг][lay5 +429 (s 3 sad)]
    $ show_sprites(("ha 1 sad", "s 3 sad"))

    voice "ch4_s_005"
    s "Er… Well, that's…"

    # [lay5 hide][lay0 +588 (t 1)]
    $ show_sprites(("ha 1 sad", "t 1"))

    voice "ch4_t_001"
    t "Contract means covenant. Servant means familiar."

    # [lay0 hide][lay9 +929 (c 1)]
    $ show_sprites(("ha 1 sad", "c 1"))

    voice "ch4_c_012"
    c "Exactly. A Contract Servant is the covenant by which a mage acknowledges a familiar."

    # [lay9 +935 (c 1 sad)]
    $ show_sprites(("ha 1 sad", "c 1 sad"))

    voice "ch4_c_013"
    c "It's not that I doubt you…"

    # [lay9 +929 (c 1)]
    $ show_sprites(("ha 1 sad", "c 1"))

    voice "ch4_c_014"
    c "But if Haruna has formed a contract, a crest should have appeared somewhere on her."

    voice "ch4_c_015"
    c "I would like to verify that. Will you cooperate?"

    # [lay7 +957 (ha 1 sad) — повтор]

    voice "ch4_ha_010"
    ha "A crest?"

    # [lay9 hide][lay5 +390 (s 1)]
    $ show_sprites(("ha 1 sad", "s 1"))

    voice "ch4_s_006"
    s "Haruna. I think she means the crest on my left hand here."

    # [lay7 +951 (ha 1)]
    $ show_sprites(("ha 1", "s 1"))

    voice "ch4_ha_011"
    ha "Oh, it's true… I hadn't noticed."

    # [lay5 hide][lay9 +929 (c 1)]
    $ show_sprites(("ha 1", "c 1"))

    voice "ch4_c_016"
    c "The crest is the proof of the familiar's contract."

    voice "ch4_c_017"
    c "The one engraved on the back of your left hand, Saito, is proof of the contract exchanged with Miss Vallière."

    # [lay7 hide][lay9 hide][lay4 +555 (g 1)]
    $ show_sprites(("g 1",))

    voice "ch4_g_001"
    g "You swear yourself to the Pentagon that governs the five powers. Bestow blessing upon this one, and make them my familiar. …Or so it goes."

    # [lay4 +566 (g 2)]
    $ show_sprites(("g 2",))

    voice "ch4_g_002"
    g "And then you bestow the oath's kiss upon the familiar…"

    # [lay4 x=224 — сдвиг][lay7 +955 (ha 1 angry)]
    $ show_sprites(("g 2", "ha 1 angry"))

    voice "ch4_ha_012"
    ha "A-a kiss!?"

    # [lay7 hide][lay1 +306 (l 1 angry)]
    $ show_sprites(("g 2", "l 1 angry"))

    voice "ch4_l_004"
    l "Gh… Quiet, Guiche!! You had to go and remember that tedious bit!!"

    # [lay4 hide][lay5 +394 (s 1 angry)]
    $ show_sprites(("l 1 angry", "s 1 angry"))

    voice "ch4_s_007"
    s "What do you mean, 'that tedious bit'!!"

    voice "ch4_l_005"
    l "It's nothing at all!!"

    # [lay1 hide][lay7 +955 (ha 1 angry)]
    $ show_sprites(("s 1 angry", "ha 1 angry"))

    voice "ch4_ha_013"
    ha "Wh-what, I've never kissed anyone!! And besides… then Hiraga-kun is… wh-what!?"

    # [lay5 +429 (s 3 sad)]
    $ show_sprites(("ha 1 angry", "s 3 sad"))

    voice "ch4_s_008"
    s "Ah, no, that's, well…"

    menu:

        "It was an accident.{#ch4_m219a}":
            jump ch4_1_220

        "Louise was the one who…{#ch4_m219b}":
            jump ch4_1_221

        "Actually, it was me…{#ch4_m219c}":
            jump ch4_1_222

label ch4_1_220:
    # ==== SCENE 220 ==== (RESET: [lay5 +429][lay7 +955][BGM +32]/[BG +29
    # (osman_cabinet)] = текущее состояние)
    # [lay5 +396 (s 1 sad)]
    $ show_sprites(("ha 1 angry", "s 1 sad"))

    voice "ch4_s_009"
    s "Th-that was an accident. It was necessary for the familiar ritual."

    # [lay7 hide][lay1 +343 (l 3 shy)]
    $ show_sprites(("s 1 sad", "l 3 shy"))

    voice "ch4_l_006"
    l "Th-that's right. I only kissed you because the ritual required it. There was nothing else to it."

    # [好感度] ルイズ 10
    $ update_sympathy(10, char_key="louise")

    jump ch4_1_223

label ch4_1_221:
    # ==== SCENE 221 ==== (RESET: [lay5 +429][lay7 +955][BGM +32]/[BG +29
    # (osman_cabinet)] = текущее состояние)
    # [lay5 +396 (s 1 sad)]
    $ show_sprites(("ha 1 angry", "s 1 sad"))

    voice "ch4_s_010"
    s "Louise was the one who asked for it, you see…"

    # [lay7 hide][lay1 +306 (l 1 angry)]
    $ show_sprites(("s 1 sad", "l 1 angry"))

    voice "ch4_l_007"
    l "Y-you idiot. It was obviously for the ritual, wasn't it? There was nothing else to it."

    # [lay1 +343 (l 3 shy)]
    $ show_sprites(("s 1 sad", "l 3 shy"))

    voice "ch4_l_008"
    l "Where else would you find someone demanding a kiss from a commoner who appeared out of nowhere?"

    jump ch4_1_223

label ch4_1_222:
    # ==== SCENE 222 ==== (RESET: [lay5 +429][lay7 +955][BGM +32]/[BG +29
    # (osman_cabinet)] = текущее состояние)
    # [lay5 +398 (s 1 shy)]
    $ show_sprites(("ha 1 angry", "s 1 shy"))

    voice "ch4_s_011"
    s "A-actually, it was me…"

    # [lay7 +955 (ha 1 angry) — повтор]
    voice "ch4_ha_014"
    ha "Eh!"

    # [好感度] ハルナ -10
    $ update_sympathy(-10, char_key="haruna")

    # [lay7 hide][lay1 +343 (l 3 shy)]
    $ show_sprites(("s 1 shy", "l 3 shy"))

    voice "ch4_l_009"
    l "Y-you idiot, what are you saying. It was obviously for the ritual, wasn't it? There was nothing else to it."

    # [好感度] ルイズ -10
    $ update_sympathy(-10, char_key="louise")

    jump ch4_1_223

label ch4_1_223:
    # ==== SCENE 223 ==== (RESET: [lay5 +396][lay1 +343][BGM +32]/[BG +29
    # (osman_cabinet)] = текущее состояние во всех трёх ветках)
    # [lay5 hide][lay7 +957 (ha 1 sad)]
    $ show_sprites(("l 3 shy", "ha 1 sad"))

    voice "ch4_ha_015"
    ha "I-is that so…"

    # [lay1 hide][lay9 +929 (c 1)]
    $ show_sprites(("ha 1 sad", "c 1"))

    voice "ch4_c_018"
    c "It is. It was an act performed in a sacred ritual. Please calm yourself, Haruna."

    voice "ch4_ha_016"
    ha "I'm sorry."

    # [lay7 hide][lay10 +918 (o 1)]
    $ show_sprites(("c 1", "o 1"))

    voice "ch4_o_012"
    o "Now then, Mister Colbert."

    voice "ch4_o_013"
    o "I think we must check whether or not a crest is engraved upon Haruna?"

    # [lay9 +935 (c 1 sad)]
    $ show_sprites(("c 1 sad", "o 1"))

    voice "ch4_c_019"
    c "…Indeed, that's true."

    # без голоса: мысль сайта
    th "Wh-what did you say!! You mean to examine Haruna's body from head to toe!?{#ch4_th_223}"

    # [lay9 +929 (c 1)]
    $ show_sprites(("c 1", "o 1"))

    voice "ch4_c_020"
    c "Whether she came from another world as a familiar, or simply wandered into this one by chance."

    voice "ch4_c_021"
    c "The difference is significant — and it's the most important matter."

    # [lay9 hide][lay7 +951 (ha 1)]
    $ show_sprites(("o 1", "ha 1"))

    voice "ch4_ha_017"
    ha "Confirming the crest…?"

    # [lay10 +926 (o 1 shy)]
    $ show_sprites(("ha 1", "o 1 shy"))

    voice "ch4_o_014"
    o "If the crest hasn't been confirmed yet, I could examine her myself…"

    # [lay7 hide][lay9 +933 (c 1 angry)]
    $ show_sprites(("o 1 shy", "c 1 angry"))

    voice "ch4_c_022"
    c "Ahem."

    # [lay10 +920 (o 1 happy)]
    $ show_sprites(("c 1 angry", "o 1 happy"))

    voice "ch4_o_015"
    o "No, no, that was a joke. We'll leave it to one of the female teachers."

    # [lay9 hide][lay3 +852 (m 1)]
    $ show_sprites(("o 1 happy", "m 1"))

    voice "ch4_m_001"
    m "Um, Osmond. When I was looking after Takanagi Haruna…"

    # [lay3 +891 (m 4 sad)]
    $ show_sprites(("o 1 happy", "m 4 sad"))

    voice "ch4_m_002"
    m "I examined her body, but I didn't find any such crest."

    # [lay10 hide][lay9 +929 (c 1)]
    $ show_sprites(("m 4 sad", "c 1"))

    voice "ch4_c_023"
    c "I see, Miss Montmorency. There's no mistake in what you say?"

    # [lay3 +852 (m 1)]
    $ show_sprites(("c 1", "m 1"))

    voice "ch4_m_003"
    m "…No. There is no mistake, Mister Colbert."

    # [lay9 hide][lay3 hide][lay10 +918 (o 1)]
    $ show_sprites(("o 1",))

    voice "ch4_o_016"
    o "Hmm, is that so."

    voice "ch4_o_017"
    o "…Hmm. Very well. I shall take Miss Montmorency's word."

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay10 hide][lay5 hide
    # — не показан][BG hide]
    stop music fadeout 1.0

    jump ch4_1_224

label ch4_1_224:
    # ==== SCENE 224 ====
    # (после 223 — чёрный экран: BG скрыт, спрайтов нет, музыки нет)
    # [null：………。……。…。 — без голоса]
    th "………………{#ch4_null_224}"

    # [BG hide][BG +29 (osman_cabinet)][TRANS][BGM play=+32] → t31
    $ fade_fx("osman_cabinet", new_music="t31")

    # [lay9 +929 (c 1)]
    $ show_sprites(("c 1",))

    voice "ch4_c_024"
    c "Then this meeting is adjourned. From now on, each of you will be mindful and act in a way that brings no shame upon the name of nobility."

    voice "ch4_c_025"
    c "Especially you, Miss Vallière. And you, Miss Zerbst. Both of you be especially careful."

    # [lay9 x=224 — сдвиг][lay1 +302 (l 1)]
    $ show_sprites(("l 1", "c 1"))

    voice "ch4_l_010"
    l "Yes.{#ch4_l_010}"

    # [lay9 hide][lay6 +676 (k 1)]
    $ show_sprites(("l 1", "k 1"))

    voice "ch4_k_001"
    k "Understood.{#ch4_k_001}"

    # [lay1 hide][lay6 hide][lay9 +929 (c 1)]
    $ show_sprites(("c 1",))

    voice "ch4_c_026"
    c "Furthermore, we will deliberate on Haruna's custody within the academy. Refrain from any rash actions."

    # [lay9 x=224 — сдвиг][lay7 +957 (ha 1 sad)]
    $ show_sprites(("c 1", "ha 1 sad"))

    voice "ch4_ha_018"
    ha "Yes… I'm sorry."

    # [lay9 hide][lay10 +920 (o 1 happy)]
    $ show_sprites(("ha 1 sad", "o 1 happy"))

    voice "ch4_o_018"
    o "Ho ho ho, there's no need to be so afraid. I won't treat you badly. You may rest easy."

    # [lay7 +951 (ha 1)]
    $ show_sprites(("ha 1", "o 1 happy"))

    voice "ch4_ha_019"
    ha "Thank you, Headmaster."

    # [lay10 hide][lay7 hide][lay9 +929 (c 1)]
    $ show_sprites(("c 1",))

    voice "ch4_c_027"
    c "Until we contact you, Haruna will remain in Miss Vallière's care."

    # [lay9 x=224 — сдвиг][lay1 +302 (l 1)]
    $ show_sprites(("l 1", "c 1"))

    voice "ch4_l_011"
    l "Understood.{#ch4_l_011}"

    # [lay9 hide][lay1 hide][lay5 +390 (s 1)][lay7 +951 (ha 1)]
    $ show_sprites(("ha 1", "s 1"))

    voice "ch4_s_012"
    s "It'll be fine, Haruna. We're with you."

    # [lay7 +953 (ha 1 happy)]
    $ show_sprites(("ha 1 happy", "s 1"))

    voice "ch4_ha_020"
    ha "Mm, thank you. Hiraga-kun."

    # [lay5 hide][lay7 hide][lay1 +306 (l 1 angry)]
    $ show_sprites(("l 1 angry",))

    voice "ch4_l_012"
    l "Wh-what about my thanks!?"

    # [lay1 x=-96 — сдвиг][lay7 +951 (ha 1)]
    $ show_sprites(("l 1 angry", "ha 1"))

    voice "ch4_ha_021"
    ha "Um, Louise — nice to meet you too, formally."

    # [lay1 +310 (l 1 shy)]
    $ show_sprites(("ha 1", "l 1 shy"))

    voice "ch4_l_013"
    l "N-nice to meet you, Haruna."

    # [lay7 hide][lay1 hide][lay6 +676 (k 1)][lay0 +588 (t 1)]
    $ show_sprites(("k 1", "t 1"))

    voice "ch4_k_002"
    k "Well, I suppose that's a relief, isn't it?"

    # без голоса: null Табиты
    t "…{#ch4_t_v01}"

    # [lay6 hide][lay0 hide][lay10 +918 (o 1)]
    $ show_sprites(("o 1",))

    voice "ch4_o_019"
    o "This meeting is adjourned… or I'd like to say as much, but…"

    voice "ch4_o_020"
    o "Miss Vallière, Saito, Haruna. Could the three of you stay behind?"

    # [lay10 x=224 — сдвиг][lay1 +302 (l 1)]
    $ show_sprites(("o 1", "l 1"))

    voice "ch4_l_014"
    l "The three of us…?"

    voice "ch4_o_021"
    o "If you would."

    # [lay1 hide][lay10 hide][lay6 +676 (k 1)]
    $ show_sprites(("k 1",))

    voice "ch4_k_003"
    k "Well then, I'll be off."

    # [lay6 hide][lay2 +489 (si 1)]
    $ show_sprites(("si 1",))

    voice "ch4_si_001"
    si "Excuse me.{#ch4_si_001}"

    # [lay2 hide][lay0 +588 (t 1)]
    $ show_sprites(("t 1",))

    voice "ch4_t_002"
    t "See you."

    # [lay0 hide][lay10 +918 (o 1)]
    $ show_sprites(("o 1",))

    voice "ch4_o_022"
    o "Mister Colbert. Would you close the door?"

    # [lay10 x=224 — сдвиг][lay9 +929 (c 1)]
    $ show_sprites(("c 1", "o 1"))

    voice "ch4_c_028"
    c "Y-yes.{#ch4_c_028}"

    # [lay9 hide][lay10 x=64 — сдвиг][SE se0 play=+56 — SE не портируется]
    $ show_sprites(("o 1",))

    voice "ch4_o_023"
    o "The truth is, you see."

    voice "ch4_o_024"
    o "Her Majesty the Queen has commanded that Miss Vallière and her familiar be sent to the royal palace."

    # [lay10 x=224 — сдвиг][lay1 +302 (l 1)]
    $ show_sprites(("o 1", "l 1"))

    voice "ch4_l_015"
    l "Her Majesty — me and Saito?"

    # [lay1 hide][lay5 +390 (s 1)]
    $ show_sprites(("o 1", "s 1"))

    voice "ch4_s_013"
    s "The princess?"

    # [lay5 hide][lay7 +951 (ha 1)]
    $ show_sprites(("o 1", "ha 1"))

    voice "ch4_ha_022"
    ha "The Queen?"

    # [lay7 hide][lay1 +308 (l 1 sad)]
    $ show_sprites(("o 1", "l 1 sad"))

    voice "ch4_l_016"
    l "Could it be… has word of Haruna reached the palace?"

    voice "ch4_o_025"
    o "Who can say — I don't know the details either."

    voice "ch4_o_026"
    o "But I thought it a good opportunity to report that people from another world have arrived, so I reported it to Her Majesty earlier."

    voice "ch4_o_027"
    o "While I'm at it — forgive the imposition — might I ask you to present Haruna to Her Majesty as well?"

    # [lay1 +302 (l 1)]
    $ show_sprites(("o 1", "l 1"))

    voice "ch4_l_017"
    l "Understood.{#ch4_l_017}"

    # [lay10 +920 (o 1 happy)]
    $ show_sprites(("l 1", "o 1 happy"))

    voice "ch4_o_028"
    o "Good."

    # [lay10 +918 (o 1)]
    $ show_sprites(("l 1", "o 1"))

    voice "ch4_o_029"
    o "The sooner you depart, the better. I've already had a carriage waiting before the academy. Set out as soon as your preparations are ready."

    voice "ch4_l_018"
    l "Yes, understood.{#ch4_l_018}"

    # [lay10 hide][lay9 +929 (c 1)]
    $ show_sprites(("l 1", "c 1"))

    voice "ch4_c_029"
    c "Then, Miss Vallière. See that you don't disgrace yourself before Her Majesty."

    voice "ch4_l_019"
    l "Yes, Mister Colbert. I understand."

    voice "ch4_l_020"
    l "Then I'll return to my room to pack for the journey. Excuse me."

    # [SE se1 stop=1 — SE не портируется][BGM stop=1000][lay9 hide][lay1 hide]
    # [BG hide]
    stop music fadeout 1.0

    jump ch4_2
