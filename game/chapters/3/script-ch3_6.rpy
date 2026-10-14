# Глава 3, часть 6 (сцены 183–192): возвращение к хабу после поиска Луизы.
# Все четыре ветки карты сцены 178 (часть 5) входят в сюжетный хаб сцены 183:
# Кирхе с компанией, хамелеон-объятия (CG cg/k_hug → cg/k_hug_2), «настоящая
# цель визита» (ветки 188/189/190), стычка в 191 и финальный хаб сцены 192,
# меню которого уходит в часть 7 (ch3_7_193/194/195).
# Источник: ps2_source/chapters/chapter_04_女の戦い.txt (SCENE 183–192).
# Точные аргументы: ps2_source/events_full/chapter_04_女の戦い.txt (SCENE 183–192).
# Служебные сцены 158–162 (переходы карты сцены 157 → локации части 3) и
# 214–218 (переходы дат сцены 213 → сцены свиданий) не портируются: в меню
# ремастера переходы идут на метки напрямую (прецедент заглушек ч. 5).
# Голоса: ch3.6_s_001…032, ch3.6_k_001…027, ch3.6_l_001…019,
#         ch3.6_si_001…005, ch3.6_ha_001…009, ch3.6_t_001.
# Без голоса (только текст): t×1 (тег ch3.6_t_v01), мысли сайта ×3.
# Голосованные многоточия: l×2 + ha×3 + si×1 (теги …_vNN), l_010 (гроул)
# отрендерен вокализацией «Grrr…» по прецеденту ч. 2 («Uuuugh.»).

label ch3_6:
    # ==== SCENE 183 ====
    # [BG image=+10] louise_room, [BGM play=+21] → t20; SE +57/+56 дверь — не портируется
    $ fade_fx("louise_room", new_music="t20")
    # [lay5 +390]
    $ show_sprites("s 1")

    voice "ch3.6_s_001"
    s "Huh? Louise, you're back already."

    # [lay1 +306]
    $ show_sprites(("s 1", "l 1 angry"))

    voice "ch3.6_l_001"
    l "I'm back — is that a problem?"

    voice "ch3.6_s_002"
    s "N-no, that's not what I meant…! Huh? Siesta's here too… What about work?"

    # [lay1 hide][lay2 +489]
    $ show_sprites(("s 1", "si 1"))

    voice "ch3.6_si_001"
    si "I'm on a break from work right now."

    # [lay5 +429]
    $ show_sprites(("s 3 sad", "si 1"))

    voice "ch3.6_s_003"
    s "Kirche — and Tabitha, no less?"

    # [lay5 hide][lay2 hide][lay6 +678][lay0 +588] (Табита — LAYER lay0)
    $ show_sprites(("k 1 happy", "t 1"))

    voice "ch3.6_k_001"
    k "My, hello there, Darling. Sorry to impose."

    t "…{#ch3.6_t_v01}"

    # [lay6 hide][lay0 hide][lay5 +396]
    $ show_sprites("s 1 sad")

    voice "ch3.6_s_004"
    s "Hey, Haruna — nobody's done anything to you, have they?"

    # [lay5 x=224 — сдвиг не копируется][lay7 +973]
    $ show_sprites(("s 1 sad", "ha 3"))

    voice "ch3.6_ha_001"
    ha "N-no, nothing in particular."

    voice "ch3.6_s_005"
    s "Really? You don't have to worry about anyone else here, okay?"

    # [lay7 hide][lay1 +306]
    $ show_sprites(("s 1 sad", "l 1 angry"))

    voice "ch3.6_l_002"
    l "How rude! We haven't done anything!"

    # [lay5 +429]
    $ show_sprites(("s 3 sad", "l 1 angry"))

    voice "ch3.6_s_006"
    s "Good, then… By the way — what have you all got planned?"

    # [lay1 hide][lay6 +711]
    $ show_sprites(("s 3 sad", "k 4 happy"))

    voice "ch3.6_k_002"
    k "My, Darling — so it's ME you're curious about?"

    voice "ch3.6_s_007"
    s "Well, 'curious' isn't quite it…"

    menu:
        "Do you need Louise for something?{#ch3_m183a}":
            # ==== SCENE 184 ==== (RESET: состояние сцены 183 сохранено)
            # [lay5 +390]
            $ show_sprites(("s 1", "k 4 happy"))

            voice "ch3.6_s_008"
            s "Need Louise for something?"

            # [lay6 +676]
            $ show_sprites(("s 1", "k 1"))

            voice "ch3.6_k_003"
            k "Not really. I don't have any business with Louise."

            # [lay5 +396]
            $ show_sprites(("s 1 sad", "k 1"))

            voice "ch3.6_s_009"
            s "Then why?"

            # [lay6 +709]
            $ show_sprites(("s 1 sad", "k 4"))

            voice "ch3.6_k_004"
            k "Well, you see…"

            jump ch3_6_187

        "Or did you come to see Haruna?{#ch3_m183b}":
            # ==== SCENE 185 ==== (RESET: состояние сцены 183 сохранено)
            # [lay5 +390]
            $ show_sprites(("s 1", "k 4 happy"))

            voice "ch3.6_s_010"
            s "You came to see Haruna, then?"

            # [lay6 +676]
            $ show_sprites(("s 1", "k 1"))

            voice "ch3.6_k_005"
            k "Half-right, maybe. But no — my real purpose is…"

            jump ch3_6_187

        "Don't tell me you came to see me?{#ch3_m183c}":
            # ==== SCENE 186 ==== (RESET: состояние сцены 183 сохранено)
            # [lay5 +423]
            $ show_sprites(("s 3", "k 4 happy"))

            voice "ch3.6_s_011"
            s "You came to see me? Pfft, couldn't be."

            # [lay6 +684]
            $ show_sprites(("s 3", "k 1 shy"))

            voice "ch3.6_k_006"
            k "And what if I did?"

            # [好感度] キュルケ +10 (TNDL tndl(-30) не портируется)
            $ update_sympathy(10, char_key="kirche")

            # [lay5 +429]
            $ show_sprites(("s 3 sad", "k 1 shy"))

            voice "ch3.6_s_012"
            s "Wh-what would I do, even…"

            # [lay6 hide][lay1 +308]
            $ show_sprites(("s 3 sad", "l 1 sad"))

            voice "ch3.6_l_003"
            l "…{#ch3.6_l_v01}"

            # [lay1 hide][lay6 +709]
            $ show_sprites(("s 3 sad", "k 4"))

            voice "ch3.6_k_007"
            k "I see. My real purpose is…"

            jump ch3_6_187

label ch3_6_187:
    # ==== SCENE 187 ==== RESET веток 184/185/186 упразднён: переход сразу
    # [BGM stop], спрайты/фон скрываются, [EVENT_CG +118], [BGM play=+30] → t29
    # (fade покрывает удаление спрайтов; первый CG серии — через fade)
    $ fade_fx("cg/k_hug", type="cg", new_music="t29")
    # [VIBRATE vibrate(1)] → shake_fx
    $ shake_fx(duration=1.0)

    voice "ch3.6_k_008"
    k "I came 'cause I wanted to see you, Darling!!"

    voice "ch3.6_ha_002"
    ha "Eh!?{#ch3.6_ha_002}"

    voice "ch3.6_s_013"
    s "W-wah!? Don't just tackle me out of nowhere!"

    # [EVENT_CG +117] imageType=1 — кроссфейд CG
    $ dissolve_fx("cg/k_hug_2", type="cg")

    voice "ch3.6_l_004"
    l "H-hey! Let go — Saito—!!"

    voice "ch3.6_s_014"
    s "M-me!? You saw it happen right in front of you!!"

    voice "ch3.6_l_005"
    l "…R-right. Kirche! Just what do you think you're doing!?"

    voice "ch3.6_k_009"
    k "No 'what do I think' about it — I planned to do this from the very start."

    voice "ch3.6_l_006"
    l "…Wha—!?"

    voice "ch3.6_k_010"
    k "Say, Haruna — how about you?"

    voice "ch3.6_ha_003"
    ha "M-me?"

    voice "ch3.6_k_011"
    k "Don't you want to try doing something like this to Darling?"

    voice "ch3.6_ha_004"
    ha "I-I don't particularly…"

    voice "ch3.6_k_012"
    k "Of course not. You couldn't — you might pass your illness on."

    voice "ch3.6_ha_005"
    ha "…{#ch3.6_ha_v01}"

    voice "ch3.6_k_013"
    k "Feeling the one you love skin to skin — it's wonderful… So, Saito — how about you?"

    # [VIBRATE vibrate(1)] → shake_fx
    $ shake_fx(duration=1.0)

    voice "ch3.6_s_015"
    s "Mmrph— fghh… C-can't… breathe…"

    voice "ch3.6_k_014"
    k "Darling… why stay in a place like this? Why not come to my room?"

    voice "ch3.6_s_016"
    s "No, I couldn't…"

    voice "ch3.6_ha_006"
    ha "…{#ch3.6_ha_v02}"

    voice "ch3.6_k_015"
    k "It's bad for Haruna. With this many people around, a curable illness stops getting better."

    voice "ch3.6_k_016"
    k "So while Haruna's sick, the least you could do is spend time with me in my room…"

    voice "ch3.6_s_017"
    s "But I'm still Louise's familiar, y'know…"

    voice "ch3.6_k_017"
    k "Serve Louise properly during the day — that's all she needs, isn't it?"

    voice "ch3.6_l_007"
    l "…{#ch3.6_l_v02}"

    voice "ch3.6_s_018"
    s "She's not answering, so…"

    voice "ch3.6_k_018"
    k "Louise saying nothing means she's fine with it — I'm sure of it."

    voice "ch3.6_s_019"
    s "Ha, ahaha… What am I supposed to do…?"

    voice "ch3.6_k_019"
    k "Darling — could it be you're the type who hates being treated like this? Answer me clearly. Here. Now."

    voice "ch3.6_s_020"
    s "Umm…"

    menu:
        "I'd never think that!{#ch3_m187a}":
            # ==== SCENE 188 ==== (RESET: [BGM +30]/[EVENT_CG +117] = текущее состояние)
            voice "ch3.6_s_021"
            s "Hate it… I'd never think that!"

            voice "ch3.6_l_008"
            l "Saaaaito…"

            # [好感度] ルイズ -10 (TNDL tndl(-30) не портируется)
            $ update_sympathy(-10, char_key="louise")

            voice "ch3.6_s_022"
            s "N-no, Louise — I answered objectively on behalf of men everywhere. It's not my personal opinion."

            voice "ch3.6_l_009"
            l "I see. So Saito can stop being a boy, then. Got it."

            voice "ch3.6_s_023"
            s "N-no, wait. Hol' on."

            jump ch3_6_191

        "It's not about breasts or not…{#ch3_m187b}":
            # ==== SCENE 189 ==== (RESET: текущее состояние сохранено)
            voice "ch3.6_s_024"
            s "It's not about breasts — rather, it's other things, y'know, umm, that is…"

            voice "ch3.6_k_020"
            k "Honestly, Darling. You can be more honest — I'd teach you plenty."

            # [好感度] キュルケ +10
            $ update_sympathy(10, char_key="kirche")

            voice "ch3.6_s_025"
            s "I-I see…{#ch3.6_s_025}"

            voice "ch3.6_l_010"
            l "Grrr…"

            # [好感度] ルイズ -10 (TNDL tndl(-30) не портируется)
            $ update_sympathy(-10, char_key="louise")

            voice "ch3.6_si_002"
            si "…{#ch3.6_si_v01}"

            # [好感度] シエスタ -10
            $ update_sympathy(-10, char_key="siesta")

            voice "ch3.6_ha_007"
            ha "…{#ch3.6_ha_v03}"

            # [好感度] ハルナ -10
            $ update_sympathy(-10, char_key="haruna")

            voice "ch3.6_s_026"
            s "…Hah!? Everyone's glaring at me…"

            voice "ch3.6_t_001"
            t "…Unclean."

            jump ch3_6_191

        "I don't judge people by their breasts.{#ch3_m187c}":
            # ==== SCENE 190 ==== (RESET: текущее состояние сохранено)
            voice "ch3.6_s_027"
            s "I don't judge people by their breasts, y'know."

            voice "ch3.6_l_011"
            l "Saito…"

            voice "ch3.6_ha_008"
            ha "Hiraga-kun…"

            th "W-what's with those pitying looks…{#ch3.6_th_190a}"

            voice "ch3.6_k_021"
            k "…I'm happy. You're the first to ever say that to me, Darling."

            # [好感度] キュルケ +10
            $ update_sympathy(10, char_key="kirche")

            voice "ch3.6_k_022"
            k "Every guy who hits on me goes for the breasts first, anyway."

            voice "ch3.6_s_028"
            s "Well, about that…"

            th "It's not like I'm hitting on her…{#ch3.6_th_190b}"

            jump ch3_6_191

label ch3_6_191:
    # ==== SCENE 191 ==== (RESET: [BGM +30]/[EVENT_CG +117] = текущее состояние)
    voice "ch3.6_k_023"
    k "Never mind. In that case, I'll just love you even MORE, Darling."

    # [VIBRATE vibrate(1)] → shake_fx
    $ shake_fx(duration=1.0)

    voice "ch3.6_s_029"
    s "Fghh, fghh… I-it… hurts… can't breathe…"

    voice "ch3.6_ha_009"
    ha "U-um…{#ch3.6_ha_009}"

    voice "ch3.6_l_012"
    l "Kirche, that's enough! I keep quiet and you two just flirt away!"

    voice "ch3.6_k_024"
    k "My~? Could someone be jealous?"

    voice "ch3.6_l_013"
    l "Wh-who's jealous of WHAT…!"

    voice "ch3.6_k_025"
    k "Darling likes big breasts. Yours obviously don't qualify. That's what you're jealous about, isn't it?"

    voice "ch3.6_l_014"
    l "Wha—!?"

    # [SE se1 stop], [BGM stop=1000], спрайты/CG скрываются — fade сцены 192
    stop music fadeout 1.0

    jump ch3_6_192

label ch3_6_192:
    # ==== SCENE 192 ====
    # [BG image=+10] louise_room, [BGM play=+27] → t26
    $ fade_fx("louise_room", new_music="t26")

    th "Somehow, before I knew it, this got way out of hand…{#ch3.6_th_192}"

    # [lay1 +307 lv=1] (close-up lv=1 — уровень не копируется)
    $ show_sprites("l 1 angry")

    voice "ch3.6_l_015"
    l "Saaaito… Just how long do you plan to keep this up~?"

    voice "ch3.6_s_030"
    s "Eeek!? Her anger's pointed at MEE!!"

    voice "ch3.6_s_031"
    s "S-sorry, Kirche. Let go already!"

    # [lay1 hide][lay6 +717]
    $ show_sprites("k 4 shy")

    voice "ch3.6_k_026"
    k "Mms… I wanted to feel Darling a little longer…"

    # [lay6 x=224 — сдвиг не копируется][lay1 +306]
    $ show_sprites(("k 4 shy", "l 1 angry"))

    voice "ch3.6_l_016"
    l "You said it was part of your plan, so I held back and held back — but that's it!"

    # [lay1 +339]
    $ show_sprites(("k 4 shy", "l 3 angry"))

    voice "ch3.6_l_017"
    l "That duel from before — we let it slide, but looks like it's time to settle it!"

    # [lay6 +676]
    $ show_sprites(("k 1", "l 3 angry"))

    voice "ch3.6_k_027"
    k "My? A duel — anytime you like. Shall we settle it right now?"

    # [lay1 +306]
    $ show_sprites(("k 1", "l 1 angry"))

    voice "ch3.6_l_018"
    l "Bring it on!"

    # [lay6 hide][lay2 +493][lay1 +302]
    $ show_sprites(("si 1 angry", "l 1"))

    voice "ch3.6_si_003"
    si "Both of you, stop! Duels between nobles aren't permitted!"

    # [lay1 +306]
    $ show_sprites(("si 1 angry", "l 1 angry"))

    voice "ch3.6_l_019"
    l "This isn't a fight as nobles — it's a fight as girls, for our pride!"

    voice "ch3.6_si_004"
    si "That's absurd! Miss Vallière!!"

    # [lay2 +495]
    $ show_sprites(("si 1 sad", "l 1 angry"))

    voice "ch3.6_si_005"
    si "Saito-san — you too, please tell them both to call off the duel."

    # [lay1 hide][lay2 hide][lay5 +429]
    $ show_sprites("s 3 sad")

    voice "ch3.6_s_032"
    s "Right…"

    menu:
        "They won't listen to me anyway.{#ch3_m192a}":
            jump ch3_7_193

        "Girls shouldn't be dueling.{#ch3_m192b}":
            jump ch3_7_194

        "Why not let them go until both are satisfied?{#ch3_m192c}":
            jump ch3_7_195
