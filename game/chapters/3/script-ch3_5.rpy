# -*- coding: utf-8 -*-
# Глава 3, часть 5 (сцены 169–178 + ветки 1322–1341): Сайто допрашивает Луизу
# и Сиесту (три варианта), мирится с Харуной, Луиза уходит — Сайто обыскивает
#学院 (четыре ветки поиска: Луиза/Кирхэ/Табита/кухня).
# Источник: ps2_source/chapters/chapter_04_女の戦い.txt (SCENE 0169–0178, 1322–1341).
# Переходы сцен 179–182 (заглушки nextScene) не портируются — меню ведёт
# напрямую на метки веток.
# Голоса: ch3.5_s_001…082, ch3.5_l_001…026, ch3.5_si_001…017, ch3.5_ha_001…012,
#         ch3.5_k_001…010, ch3.5_t_001, ch3.5_c_001…010, ch3.5_m_001…011,
#         ch3.5_g_001…012.

# ==== ВЕТКА 1 (сцена 169): «It was Louise who started it…» ====
label ch3_5_169:
    # ==== SCENE 169 ====
    # [BG stage image=+10] louise_room, [BGM play=+19] → t18
    $ fade_fx("louise_room", new_music="t18")
    $ show_sprites(("s 1 angry", "l 1 sad"))

    voice "ch3.5_s_001"
    s "Louise started this, didn't she?"

    $ show_sprites(("s 1 angry", "l 1 angry"))

    voice "ch3.5_l_001"
    l "...{#ch3.5_l_001}"

    voice "ch3.5_s_002"
    s "Why the silence? So I'm right?"

    $ show_sprites(("s 1 angry", "l 1"))

    voice "ch3.5_l_002"
    l "...{#ch3.5_l_002}"

    $ update_sympathy(-10, char_key="louise")

    $ show_sprites(("s 1 angry", "si 1 sad"))

    voice "ch3.5_si_001"
    si "N-no, that's wrong, Saito-san! This was my idea, and—"

    voice "ch3.5_s_003"
    s "Sorry, Siesta, but could you keep quiet?"

    $ update_sympathy(-10, char_key="siesta")

    jump ch3_5_172

# ==== ВЕТКА 2 (сцена 170): «This isn't like the usual Siesta.» ====
label ch3_5_170:
    # ==== SCENE 170 ====
    $ fade_fx("louise_room", new_music="t18")
    $ show_sprites(("s 1 angry", "l 1 sad"))

    voice "ch3.5_s_004"
    s "This isn't like the usual Siesta."

    $ show_sprites(("s 1 angry", "si 1 sad"))

    voice "ch3.5_si_002"
    si "I'm sorry…"

    $ show_sprites(("s 1 sad", "si 1 sad"))

    voice "ch3.5_s_005"
    s "To think Siesta would do something like this… I'm disappointed."

    $ show_sprites(("s 1 sad", "si 4 angry"))

    voice "ch3.5_si_003"
    si "Gahn!?"

    $ update_sympathy(-10, char_key="siesta")

    $ show_sprites(("s 1 sad", "l 3 angry"))

    voice "ch3.5_l_003"
    l "Saito! That was way too much!"

    $ show_sprites(("s 1 angry", "l 3 angry"))

    voice "ch3.5_s_006"
    s "I don't think so."

    jump ch3_5_172

# ==== ВЕТКА 3 (сцена 171): «Do you dislike Haruna?» ====
label ch3_5_171:
    # ==== SCENE 171 ====
    $ fade_fx("louise_room", new_music="t18")
    $ show_sprites("s 3 sad")

    voice "ch3.5_s_007"
    s "Do you two dislike Haruna?"

    # [SPRITE lay5 hide] s уходит; показываются сиеста и луиза
    $ show_sprites(("si 1 sad", "l 1 sad"))

    voice "ch3.5_si_004"
    si "Not at all, we don't dislike her… It's just that…"

    voice "ch3.5_l_004"
    l "Because Saito keeps fussing over Haruna…"

    $ show_sprites("s 1 angry")

    voice "ch3.5_s_008"
    s "So you resort to pranks like this? That's going too far, you know."

    jump ch3_5_172

# ==== ОБЩАЯ ЛИНИЯ: сцены 172–178 ====
label ch3_5_172:
    # ==== SCENE 172 ====
    # [SPRITE lay5=394] s 1 angry — состояние спрайта сохраняется из ветки;
    # [BGM play=+19] → t18 (уже играет), [BG stage=+10] — фон не меняется
    voice "ch3.5_s_009"
    s "I'm being serious here, you know! I'm really angry!"

    $ show_sprites(("si 1 sad", "l 1 sad"))

    voice "ch3.5_si_005"
    si "…I'm sorry."

    voice "ch3.5_l_005"
    l "...{#ch3.5_l_005}"

    $ show_sprites(None)
    stop music fadeout 1.0

    jump ch3_5_173

label ch3_5_173:
    # ==== SCENE 173 ====
    # [BG stage=+10] louise_room, [TRANS crossfade 1000], [BGM play=+21] → t20
    $ dissolve_fx("louise_room", duration=1.0, new_music="t20")

    # [SE se0 play=+59/+55] — не портируется (см. отчёт)
    th "I had Siesta put the bedding away and opened the windows to air the room out. Finally, the temperature settled down."

    $ show_sprites("s 3 sad")

    voice "ch3.5_s_010"
    s "Haruna, are you okay? You're not feeling sick?"

    $ show_sprites(("s 3 sad", "ha 3"))

    voice "ch3.5_ha_001"
    ha "Yeah, I'm fine now…"

    $ show_sprites(("s 1", "ha 3"))

    voice "ch3.5_s_011"
    s "That's good…"

    $ show_sprites(("l 1 sad", "si 1 sad"))

    voice "ch3.5_l_006"
    l "As if we're the ones in the wrong…"

    voice "ch3.5_si_006"
    si "That's right. It seems Saito-san dislikes us…"

    $ show_sprites("s 1 sad")

    voice "ch3.5_s_012"
    s "No, I'm not saying you're bad or that I hate you. I'm saying you went too far."

    $ show_sprites(("l 3 sad", "si 1 sad"))

    voice "ch3.5_l_007"
    l "But… Hey, Siesta?"

    voice "ch3.5_si_007"
    si "Yes… Saito-san wouldn't understand."

    $ show_sprites("s 3 sad")

    voice "ch3.5_s_013"
    s "…Good grief."

    # [BG stage hide] + [BG stage=+10, crossfade 1000] — повторный показ фона
    $ dissolve_fx("louise_room", duration=1.0)
    $ show_sprites(("s 3 sad", "si 1 sad"))

    voice "ch3.5_si_008"
    si "Well then, Saito-san… I have work to do, so…"

    $ show_sprites(("s 1", "si 1 sad"))

    voice "ch3.5_s_014"
    s "I see. Hang in there, Siesta…"

    voice "ch3.5_si_009"
    si "Yes…"

    $ show_sprites("s 1 sad")

    voice "ch3.5_s_015"
    s "Did I make Siesta feel down…?"

    $ show_sprites(("s 1 sad", "l 1 sad"))

    voice "ch3.5_l_008"
    l "…No wonder she's down. Even I…"

    $ show_sprites(("s 1 angry", "l 1 sad"))

    voice "ch3.5_s_016"
    s "That doesn't make it okay, does it?"

    $ show_sprites(("s 1 angry", "l 3 sad"))

    voice "ch3.5_l_009"
    l "Hah… Never mind. I'm going out for a bit."

    $ show_sprites(("s 1", "l 3 sad"))

    voice "ch3.5_s_017"
    s "Should I come with you?"

    $ show_sprites(("s 1", "l 1 angry"))

    voice "ch3.5_l_010"
    l "You don't have to come, Saito. Just go look after cute little Haruna all you like."

    $ show_sprites(("s 1 sad", "l 1 angry"))

    voice "ch3.5_s_018"
    s "What's with that tone…"

    # ==== CHOICE (scene 173) → сцены 174/175/176 ====
    menu:
        "Is it wrong of me to look after Haruna?{#ch3_m173a}":
            jump ch3_5_174

        "You didn't need to worry about her.{#ch3_m173b}":
            jump ch3_5_175

        "I'm just saying something objective.{#ch3_m173c}":
            jump ch3_5_176

label ch3_5_174:
    # ==== SCENE 174 ====
    $ show_sprites(("s 3 sad", "l 1 angry"))

    voice "ch3.5_s_019"
    s "Is it really so bad, looking after Haruna?"

    $ show_sprites(("s 3 sad", "l 1 angry"))

    voice "ch3.5_l_011"
    l "Nobody said that!"

    $ update_sympathy(-10, char_key="louise")

    $ show_sprites(("s 1 sad", "l 1 angry"))

    voice "ch3.5_s_020"
    s "Then why did you do something like that?"

    voice "ch3.5_l_012"
    l "...{#ch3.5_l_012}"

    jump ch3_5_177

label ch3_5_175:
    # ==== SCENE 175 ====
    $ show_sprites(("s 3 sad", "l 1 angry"))

    voice "ch3.5_s_021"
    s "I was worried about you…"

    $ show_sprites(("s 3 sad", "l 3 shy"))

    voice "ch3.5_l_013"
    l "W-worried about me?! Is that true?"

    $ update_sympathy(10, char_key="louise")

    $ show_sprites(("s 1 sad", "l 3 shy"))

    voice "ch3.5_s_022"
    s "Well… it's…"

    $ show_sprites(("s 1 sad", "l 1 angry"))

    voice "ch3.5_l_014"
    l "Enough!! I'd rather not hear empty words like that!"

    voice "ch3.5_s_023"
    s "No, listen, I mean it—"

    jump ch3_5_177

label ch3_5_176:
    # ==== SCENE 176 ====
    $ show_sprites(("s 1 angry", "l 1 angry"))

    voice "ch3.5_s_024"
    s "I'm just stating objective facts."

    $ show_sprites(("s 1 angry", "l 1"))

    voice "ch3.5_l_015"
    l "Is that so…? And you think you're being objective, Saito?"

    $ show_sprites(("s 1", "l 1"))

    voice "ch3.5_s_025"
    s "Yeah, that's what I think."

    $ show_sprites("ha 3 sad")
    ha "...{#ch3.5_ha_176}"

    jump ch3_5_177

label ch3_5_177:
    # ==== SCENE 177 ====
    # [SPRITE lay1=306, lay5=396], [BGM play=+21] → t20 (уже играет)
    $ show_sprites(("l 1 angry", "s 1 sad"))

    voice "ch3.5_l_016"
    l "An-y-way! I'm going out by myself, so you stay here, Saito."

    $ show_sprites(("l 1 angry", "s 1 angry"))

    voice "ch3.5_s_026"
    s "Fine. Suit yourself."

    $ show_sprites(("l 3 angry", "s 1 angry"))

    voice "ch3.5_l_017"
    l "Oh, I intend to."

    # [SE se0 +57/+58] дверь, [VIBRATE vibrate(1)] → shake_fx; луиза уходит,
    # спрайт сайто меняется на s 3 sad (один в кадре)
    $ shake_fx(duration=1.0)
    $ show_sprites("s 3 sad")

    voice "ch3.5_s_027"
    s "Jeez, that Louise… Why's she so mad…? I don't get it anymore."

    stop music fadeout 1.0
    $ show_sprites(None)

    jump ch3_5_178

label ch3_5_178:
    # ==== SCENE 178 ====
    # [BG stage=+14] hallway, [TRANS crossfade 1000], [BGM play=+19] → t18
    $ dissolve_fx("hallway", duration=1.0, new_music="t18")
    $ show_sprites("l 1 angry")

    voice "ch3.5_l_018"
    l "Honestly… That Saito gets me so mad!"

    voice "ch3.5_l_019"
    l "…Kirche! It's me, Louise!!"

    # Кирхэ говорит изнутри комнаты — спрайта ещё нет
    voice "ch3.5_k_001"
    k "Hold on, Louise. Is there really no better way to knock?"

    voice "ch3.5_k_002"
    k "I get that you're upset, but taking it out on things isn't the answer."

    voice "ch3.5_l_020"
    l "Shut up! I'm coming in!!"

    # [SE se0 +57] дверь; [BG stage hide] → [BG stage=+91] room, crossfade
    $ dissolve_fx("room", duration=1.0)
    $ show_sprites(("si 1", "l 1"))

    voice "ch3.5_si_010"
    si "Miss Vallière. How did things go with Saito-san and the others?"

    voice "ch3.5_l_021"
    l "Ah, hopeless, hopeless. That idiot doesn't suspect for a second that Haruna is faking."

    $ show_sprites(("si 1 sad", "l 1"))

    voice "ch3.5_si_011"
    si "I see… So everything we did was pointless, then…"

    $ show_sprites(("si 1 sad", "l 1 sad"))

    voice "ch3.5_l_022"
    l "Not just pointless—it backfired spectacularly."

    $ show_sprites(("k 1 happy", "t 1"))

    voice "ch3.5_k_003"
    k "See, Tabitha? Just like I said—it failed."

    t "...{#ch3.5_t_178}"

    $ show_sprites(("k 1", "t 1"))

    voice "ch3.5_k_004"
    k "Besides, you two are way too soft. That Haruna girl has her eyes on darling too, right?"

    $ show_sprites(("k 1", "l 1"))

    voice "ch3.5_l_023"
    l "Probably."

    voice "ch3.5_k_005"
    k "Even in her shoes, I wouldn't have thrown in the towel."

    $ show_sprites(("k 1 shy", "l 1"))

    voice "ch3.5_k_006"
    k "Because even if pushing through the heat made her sick, knowing darling would nurse her back to health is reason enough to keep going…"

    $ show_sprites(("k 1 shy", "si 1"))

    voice "ch3.5_si_012"
    si "In the fairy tale my great-grandfather told me, it did work, though…"

    $ show_sprites(("k 4", "si 1"))

    voice "ch3.5_k_007"
    k "What kind of story was it?"

    voice "ch3.5_si_013"
    si "Yes, Miss Zerbst. It's the tale of the North Wind and the Sun, competing to strip a traveler of his coat."

    voice "ch3.5_si_014"
    si "In the story, the North Wind tries to blow the coat away, but fails…"

    $ show_sprites(("k 4", "si 1 happy"))

    voice "ch3.5_si_015"
    si "while the Sun, by bathing him in warm sunlight, makes him take it off himself."

    $ show_sprites(("k 1", "si 1 happy"))

    voice "ch3.5_k_008"
    k "I see. So it's better to talk someone into taking their clothes off than to tear them off by force."

    $ show_sprites(("k 1", "si 1 sad"))

    voice "ch3.5_si_016"
    si "But I didn't think Haruna-san would be this patient…"

    $ show_sprites(("si 1 sad", "t 1"))

    voice "ch3.5_t_001"
    t "The schemer drowns in their own scheme."

    $ show_sprites(("si 1 sad", "l 1"))

    voice "ch3.5_l_024"
    l "I'm telling you, Siesta. I thought that same plan would expose Haruna's fake illness too."

    $ show_sprites("k 1 sad")

    voice "ch3.5_k_009"
    k "Then I have no choice. This time, I'll go save darling myself!"

    $ show_sprites(("k 1 sad", "l 1"))

    voice "ch3.5_l_025"
    l "…Wait, what are you planning to do?"

    $ show_sprites(("k 4 happy", "l 1"))

    voice "ch3.5_k_010"
    k "Leave it to me. I'll make Haruna herself admit she was faking!"

    $ show_sprites(("si 1 sad", "l 1"))

    voice "ch3.5_si_017"
    si "Um, Miss Vallière… Are you sure it's all right to leave everything to Miss Zerbst?"

    $ show_sprites(("si 1 sad", "l 1 sad"))

    voice "ch3.5_l_026"
    l "To be honest, I'm worried too…"

    # [BG stage hide] → [BG stage=+14] hallway, crossfade
    $ dissolve_fx("hallway", duration=1.0)
    $ show_sprites("s 1")

    th "I don't think Louise would give up this easily. I should probably go tail her for a bit."
    th "I wonder where Louise went…?"

    stop music fadeout 1.0
    $ show_sprites(None)

    # ==== CHOICE (scene 178)【移動】→ ветки поиска ====
    # сцены 179–182 — переходные заглушки, не портируются
    menu:
        "Louise's room{#ch3_m178a}":
            jump ch3_5_1322

        "Kirche's room{#ch3_m178b}":
            jump ch3_5_1327

        "Tabitha's room{#ch3_m178c}":
            jump ch3_5_1332

        "The kitchen{#ch3_m178d}":
            jump ch3_5_1337

# ==== ВЕТКА ПОИСКА 1: комната Луизы (сцены 1322–1326) ====
label ch3_5_1322:
    # ==== SCENE 1322 ====
    # [BG stage=+10] louise_room, crossfade, [BGM play=+11] → t10
    $ dissolve_fx("louise_room", duration=1.0, new_music="t10")
    $ show_sprites("ha 3 happy")

    voice "ch3.5_ha_002"
    ha "Ah, Hiraga-kun…"

    $ update_sympathy(20, char_key="haruna")

    $ show_sprites(("ha 3 shy", "s 1"))

    voice "ch3.5_s_028"
    s "I came looking for Louise and the others… Looks like they're not here."

    $ show_sprites(("ha 3", "s 1"))

    voice "ch3.5_ha_003"
    ha "Yeah. They haven't been here since before."

    $ show_sprites(("ha 3", "s 3 sad"))

    voice "ch3.5_s_029"
    s "I see… Sorry about earlier. Pulling something so awful on a sick person…"

    voice "ch3.5_ha_004"
    ha "Yeah, that's already forgotten. It wasn't your fault, Hiraga-kun."

    $ show_sprites(("ha 3", "s 1 sad"))

    voice "ch3.5_s_030"
    s "Still… why would Louise and Siesta do something like that?"

    $ show_sprites(("ha 3 sad", "s 1 sad"))

    voice "ch3.5_ha_005"
    ha "Hiraga-kun, do you really not know?"

    $ show_sprites(("ha 3 sad", "s 1"))

    voice "ch3.5_s_031"
    s "Huh? Know what?"

    $ show_sprites(("ha 3", "s 1"))

    voice "ch3.5_ha_006"
    ha "The reason Louise and the others did something like that together…"

    voice "ch3.5_s_032"
    s "The reason…?"

    # ==== CHOICE (scene 1322) → сцены 1323/1324/1325 ====
    menu:
        "Was it because Haruna took over your room?{#ch3_m1322a}":
            jump ch3_5_1323

        "Actually, maybe it was Louise and Siesta's way of nursing her?{#ch3_m1322b}":
            jump ch3_5_1324

        "Hmm, I have no idea.{#ch3_m1322c}":
            jump ch3_5_1325

label ch3_5_1323:
    # ==== SCENE 1323 ====
    $ show_sprites(("s 3", "ha 3"))

    voice "ch3.5_s_033"
    s "Was it because Haruna took over your room?"

    $ show_sprites(("s 1 sad", "ha 3"))

    voice "ch3.5_s_034"
    s "But if that's the case, I don't get why Siesta would tag along."

    voice "ch3.5_s_035"
    s "If anything, Louise would want to kick Siesta out along with Haruna."

    $ show_sprites(("s 1 sad", "ha 3 sad"))

    voice "ch3.5_ha_007"
    ha "Hey, Hiraga-kun. Are you serious right now?"

    $ update_sympathy(-10, char_key="haruna")

    $ show_sprites(("s 1", "ha 3 sad"))

    voice "ch3.5_s_036"
    s "Pretty much, yeah."

    jump ch3_5_1326

label ch3_5_1324:
    # ==== SCENE 1324 ====
    $ show_sprites(("s 3 sad", "ha 3"))

    voice "ch3.5_s_037"
    s "Actually, maybe it was Louise and Siesta's way of nursing her?"

    $ show_sprites(("s 1", "ha 3"))

    voice "ch3.5_s_038"
    s "Like some kind of treatment—fighting fire with fire, heat with heat?"

    $ show_sprites(("s 1 sad", "ha 3"))

    voice "ch3.5_s_039"
    s "If that's the case, I did something awful to Louise and the others…"

    $ show_sprites(("s 1 sad", "ha 3 sad"))

    voice "ch3.5_ha_008"
    ha "You're really kind, Hiraga-kun."

    $ show_sprites(("s 1", "ha 3 sad"))

    voice "ch3.5_s_040"
    s "Huh? Why?{#ch3.5_s_040}"

    jump ch3_5_1326

label ch3_5_1325:
    # ==== SCENE 1325 ====
    $ show_sprites(("s 3 sad", "ha 3"))

    voice "ch3.5_s_041"
    s "Hmm, I have no idea."

    $ show_sprites(("s 1 sad", "ha 3"))

    voice "ch3.5_s_042"
    s "No matter how hard I try, I just can't imagine why Louise and the others would do that to Haruna."

    $ show_sprites(("s 1 sad", "ha 3 sad"))

    voice "ch3.5_ha_009"
    ha "Dense…"

    $ show_sprites(("s 1", "ha 3 sad"))

    voice "ch3.5_s_043"
    s "Eh?{#ch3.5_s_043}"

    $ show_sprites(("s 1", "ha 3"))

    voice "ch3.5_ha_010"
    ha "Never mind."

    $ show_sprites(("s 1 sad", "ha 3"))

    voice "ch3.5_s_044"
    s "Tch."

    jump ch3_5_1326

label ch3_5_1326:
    # ==== SCENE 1326 ====
    $ show_sprites(("s 1", "ha 3 sad"))

    voice "ch3.5_s_045"
    s "Haruna, can you guess why?"

    voice "ch3.5_ha_011"
    ha "Ah, um… I'm sorry. I still don't know…"

    $ show_sprites(("s 1 sad", "ha 3 sad"))

    voice "ch3.5_s_046"
    s "You don't? Yeah, I figured…"

    $ show_sprites(("s 1", "ha 3"))

    voice "ch3.5_s_047"
    s "Well, I should be heading out. Take it easy, okay?"

    $ show_sprites("ha 3 sad")

    voice "ch3.5_ha_012"
    ha "…Hiraga-kun, you idiot."

    # [SE se1 stop], [BGM stop=1000], спрайты и фон скрываются
    stop music fadeout 1.0
    $ show_sprites(None)

    jump ch3_6

# ==== ВЕТКА ПОИСКА 2: коридор / Кольбер (сцены 1327–1331) ====
label ch3_5_1327:
    # ==== SCENE 1327 ====
    # [BG stage=+14] hallway, crossfade, [BGM play=+19] → t18
    $ dissolve_fx("hallway", duration=1.0, new_music="t18")

    th "Louise isn't here… I was hoping she'd be back in her room. I wonder where she went…?{#ch3.5_th_1327}"

    # [BGM stop=1000] + [BGM play=+32] → t31
    stop music fadeout 1.0
    play music t31 fadein 1.0

    $ show_sprites("c 1")

    voice "ch3.5_c_001"
    c "My, Saito. Standing about in the hallway—is something the matter?"

    $ show_sprites(("c 1", "s 3 sad"))

    voice "ch3.5_s_048"
    s "I was looking for Louise, but she's nowhere to be found…"

    $ show_sprites(("c 1 sad", "s 3 sad"))

    voice "ch3.5_c_002"
    c "I see. That's a shame."

    $ show_sprites(("c 1 happy", "s 3 sad"))

    voice "ch3.5_c_003"
    c "Ah, that's right, Saito. Do drop by my research lab next time, won't you?"

    # ==== CHOICE (scene 1327) → сцены 1328/1329/1330 ====
    menu:
        "Yes, I'd love to.{#ch3_m1327a}":
            jump ch3_5_1328

        "Once things calm down, sure.{#ch3_m1327b}":
            jump ch3_5_1329

        "I'll make time to visit.{#ch3_m1327c}":
            jump ch3_5_1330

label ch3_5_1328:
    # ==== SCENE 1328 ====
    $ show_sprites(("c 1 happy", "s 1"))

    voice "ch3.5_s_049"
    s "Yes, I'd love to."

    $ show_sprites(("c 1", "s 1"))

    voice "ch3.5_c_004"
    c "Very well. Come by whenever it suits you, Saito."

    jump ch3_5_1331

label ch3_5_1329:
    # ==== SCENE 1329 ====
    $ show_sprites(("c 1 happy", "s 1"))

    voice "ch3.5_s_050"
    s "Once things calm down, sure."

    $ show_sprites(("c 1", "s 1"))

    voice "ch3.5_c_005"
    c "Once things calm down, you say… Are you busy with something lately?"

    $ show_sprites(("c 1", "s 1 sad"))

    voice "ch3.5_s_051"
    s "Yes, a few things here and there… But I'll be sure to come."

    voice "ch3.5_c_006"
    c "I see. Then do come once things have settled down."

    jump ch3_5_1331

label ch3_5_1330:
    # ==== SCENE 1330 ====
    $ show_sprites(("c 1 happy", "s 1"))

    voice "ch3.5_s_052"
    s "I'll make time to visit."

    $ show_sprites(("c 1", "s 1"))

    voice "ch3.5_c_007"
    c "Make time, you say… Is there something keeping you busy?"

    $ show_sprites(("c 1", "s 3 sad"))

    voice "ch3.5_s_053"
    s "Ah, well, a little…"

    voice "ch3.5_c_008"
    c "Hesitating isn't like you, Saito. What exactly is going on?"

    $ show_sprites(("c 1", "s 1 sad"))

    voice "ch3.5_s_054"
    s "Actually, Professor…I'm having a falling-out with some people."

    voice "ch3.5_c_009"
    c "I see. You've had it rough too, then."

    jump ch3_5_1331

label ch3_5_1331:
    # ==== SCENE 1331 ====
    $ show_sprites(("c 1 happy", "s 1"))

    voice "ch3.5_c_010"
    c "Well then, I'll be looking forward to it, Saito."

    $ show_sprites(("c 1 happy", "s 1"))

    voice "ch3.5_s_055"
    s "Yes, Professor."

    stop music fadeout 1.0
    $ show_sprites(None)

    jump ch3_6

# ==== ВЕТКА ПОИСКА 3: комната Табиты / Монморанси (сцены 1332–1336) ====
label ch3_5_1332:
    # ==== SCENE 1332 ====
    # [BG stage=+14] hallway, crossfade, [BGM play=+19] → t18
    $ dissolve_fx("hallway", duration=1.0, new_music="t18")

    th "Louise isn't here… I was hoping she'd be back in her room. I wonder where she went…?{#ch3.5_th_1332}"

    $ show_sprites("m 1 sad")

    voice "ch3.5_m_001"
    m "You… What are you doing there? Don't tell me you're planning to rob the place?"

    $ show_sprites(("m 1 sad", "s 1"))

    voice "ch3.5_s_056"
    s "Me, a burglar? No, no! I'm just looking for Louise."

    $ show_sprites(("m 1", "s 1"))

    voice "ch3.5_m_002"
    m "Oh, is that so? I haven't seen Louise. I wonder if she's really in?"

    voice "ch3.5_s_057"
    s "I see. Thanks."

    $ show_sprites(("m 4", "s 1"))

    voice "ch3.5_m_003"
    m "By the way, you… What do you want with Louise?"

    $ show_sprites(("m 4", "s 3 sad"))

    voice "ch3.5_s_058"
    s "What do I want…"

    # ==== CHOICE (scene 1332) → сцены 1333/1334/1335 ====
    menu:
        "It's not like I need her for anything.{#ch3_m1332a}":
            jump ch3_5_1333

        "I wanted to ask her about Haruna.{#ch3_m1332b}":
            jump ch3_5_1334

        "Sorry. I can't tell you, Monmon.{#ch3_m1332c}":
            jump ch3_5_1335

label ch3_5_1333:
    # ==== SCENE 1333 ====
    $ show_sprites(("m 4", "s 1"))

    voice "ch3.5_s_059"
    s "It's not like I need Louise for anything."

    voice "ch3.5_s_060"
    s "I was just wondering where she might be, so I'm looking around."

    $ show_sprites(("m 1", "s 1"))

    voice "ch3.5_m_004"
    m "Oh, is that so."

    jump ch3_5_1336

label ch3_5_1334:
    # ==== SCENE 1334 ====
    $ show_sprites(("m 4", "s 1"))

    voice "ch3.5_s_061"
    s "I wanted to consult her about something regarding Haruna."

    $ show_sprites(("m 1", "s 1"))

    voice "ch3.5_m_005"
    m "Oh, is that so. Not to pry, but…"

    $ show_sprites(("m 1 sad", "s 1"))

    voice "ch3.5_m_006"
    m "You have it rough too, don't you? You're living with a maid, Louise, and Haruna now, right?"

    $ show_sprites(("m 1 sad", "s 3 happy"))

    voice "ch3.5_s_062"
    s "Haha, hah…"

    $ show_sprites(("m 1 sad", "s 1 sad"))

    th "If she knew about what just happened, she'd be shocked."

    jump ch3_5_1336

label ch3_5_1335:
    # ==== SCENE 1335 ====
    $ show_sprites(("m 4", "s 1"))

    voice "ch3.5_s_063"
    s "Sorry. I can't tell you, Monmon."

    $ show_sprites(("m 1 angry", "s 1"))

    voice "ch3.5_m_007"
    m "Who are you calling Monmon?! I'm Montmorency!"

    $ show_sprites(("m 1 angry", "s 3 sad"))

    voice "ch3.5_s_064"
    s "Come on, what does a little thing like that matter?"

    voice "ch3.5_m_008"
    m "It matters plenty! And state your purpose properly."

    $ show_sprites(("m 1 angry", "s 1 sad"))

    voice "ch3.5_s_065"
    s "You're a handful, Monmon."

    $ show_sprites(("m 4 angry", "s 1 sad"))

    voice "ch3.5_m_009"
    m "I said stop calling me Monmon! What if the whole academy hears—how will you take responsibility?"

    voice "ch3.5_s_066"
    s "Responsibility… Ah, never mind."

    $ show_sprites(("m 4 angry", "s 1"))

    voice "ch3.5_s_067"
    s "I was just wondering where Louise might be, so I'm looking around."

    $ show_sprites(("m 1", "s 1"))

    voice "ch3.5_m_010"
    m "Oh, is that so? Then say so in the first place."

    jump ch3_5_1336

label ch3_5_1336:
    # ==== SCENE 1336 ====
    $ show_sprites(("s 1", "m 1"))

    voice "ch3.5_s_068"
    s "Well, I've got to go look for Louise, so I'll be off…"

    $ show_sprites(("s 1", "m 4"))

    voice "ch3.5_m_011"
    m "Sorry I couldn't be of help."

    stop music fadeout 1.0
    $ show_sprites(None)

    jump ch3_6

# ==== ВЕТКА ПОИСКА 4: кухня / Гиш (сцены 1337–1341) ====
label ch3_5_1337:
    # ==== SCENE 1337 ====
    # [BG stage=+32] kitchen, crossfade, [BGM play=+19] → t18
    # [SE se1 play=+44] — не портируется (см. отчёт)
    $ dissolve_fx("kitchen", duration=1.0, new_music="t18")

    th "Louise isn't here… I was hoping she'd be back in her room. I wonder where she went…?{#ch3.5_th_1337}"

    $ show_sprites("g 1")

    voice "ch3.5_g_001"
    g "Hello, Saito. What's with that grave expression?"

    $ show_sprites(("g 1", "s 1 sad"))

    voice "ch3.5_s_069"
    s "Do I really look that grim?"

    $ show_sprites(("g 2", "s 1 sad"))

    voice "ch3.5_g_002"
    g "Mm… What's wrong? If it helps, I can lend an ear."

    $ show_sprites(("g 2", "s 1"))

    voice "ch3.5_s_070"
    s "No, I was just wondering if you'd seen Louise anywhere."

    $ show_sprites(("g 1", "s 1"))

    voice "ch3.5_g_003"
    g "Louise? Not while I've been here, no…"

    voice "ch3.5_g_004"
    g "By the way, is something the matter with Louise?"

    voice "ch3.5_s_071"
    s "Actually…"

    # ==== CHOICE (scene 1337) → сцены 1338/1339/1340 ====
    menu:
        "I wanted to consult you about Haruna.{#ch3_m1337a}":
            jump ch3_5_1338

        "No, never mind.{#ch3_m1337b}":
            jump ch3_5_1339

        "Yeah, I just need her for something.{#ch3_m1337c}":
            jump ch3_5_1340

label ch3_5_1338:
    # ==== SCENE 1338 ====
    $ show_sprites(("s 1", "g 1"))

    voice "ch3.5_s_072"
    s "It's about Haruna—I wanted some advice…"

    $ show_sprites(("s 1", "g 1 sad"))

    voice "ch3.5_g_005"
    g "Advice? What on earth happened?"

    $ show_sprites(("s 3 sad", "g 1 sad"))

    voice "ch3.5_s_073"
    s "N-no, nothing happened. It's not a big deal."

    $ show_sprites(("s 3 sad", "g 1"))

    voice "ch3.5_g_006"
    g "Is that so? All right, then."

    $ show_sprites(("s 1 sad", "g 1"))

    th "Something tells me asking Guiche for advice would only make things more complicated—and that feeling's probably right.{#ch3.5_th_1338}"

    jump ch3_5_1341

label ch3_5_1339:
    # ==== SCENE 1339 ====
    $ show_sprites(("s 3", "g 1"))

    voice "ch3.5_s_074"
    s "No, never mind."

    $ show_sprites(("s 3", "g 1 sad"))

    voice "ch3.5_g_007"
    g "You're a cold one, you know that? Don't be like that—tell me too, won't you?"

    $ show_sprites(("s 3 sad", "g 1 sad"))

    voice "ch3.5_s_075"
    s "My bad, my bad. It's nothing all that serious. I'll tell you about it some other time."

    $ show_sprites(("s 3 sad", "g 1"))

    voice "ch3.5_g_008"
    g "Is that so? All right, then.{#ch3.5_g_008}"

    $ show_sprites(("s 1 sad", "g 1"))

    th "Something tells me asking Guiche for advice would only make things more complicated—and that feeling's probably right.{#ch3.5_th_1339}"

    jump ch3_5_1341

label ch3_5_1340:
    # ==== SCENE 1340 ====
    $ show_sprites(("s 3", "g 1"))

    voice "ch3.5_s_076"
    s "Yeah, I just need her for something."

    $ show_sprites(("s 3", "g 1"))

    voice "ch3.5_g_009"
    g "I see. Doesn't sound like a crisis that needs my intervention."

    $ show_sprites(("s 1", "g 1"))

    voice "ch3.5_s_077"
    s "Something like that."

    $ show_sprites(("s 1 sad", "g 1"))

    th "It'd be a hassle, so I won't bother explaining the situation to Guiche."

    jump ch3_5_1341

label ch3_5_1341:
    # ==== SCENE 1341 ====
    # [BGM play=+19] → t18 (уже играет)
    $ show_sprites(("s 1", "g 1"))

    voice "ch3.5_s_078"
    s "By the way, Guiche—what are you even doing here?"

    $ show_sprites(("s 1", "g 2"))

    voice "ch3.5_g_010"
    g "Me? By visiting the kitchen—a place one rarely gets to see—I've been studying society."

    voice "ch3.5_s_079"
    s "I… see. Oh, you've got sauce around your mouth."

    $ show_sprites(("s 1", "g 1 angry"))

    voice "ch3.5_g_011"
    g "W-wha—nonsense!? …Wait, there's nothing there!?"

    $ show_sprites(("s 3 happy", "g 1 angry"))

    voice "ch3.5_s_080"
    s "Just kidding. Field trips to the kitchen are fine, but go easy on the nibbling."

    voice "ch3.5_g_012"
    g "What are you talking about! I-I never nibble on anything!"

    $ show_sprites(("s 3", "g 1 angry"))

    voice "ch3.5_s_081"
    s "Sure, sure. If you say so."

    $ show_sprites(("s 1", "g 1"))

    voice "ch3.5_s_082"
    s "Well, see you."

    stop music fadeout 1.0
    $ show_sprites(None)

    jump ch3_6
