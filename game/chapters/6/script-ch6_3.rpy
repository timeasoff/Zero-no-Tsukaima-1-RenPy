# Chapter 6, part 3: Henrietta night-city date, source scenes 1164-1168.
# Source: ps2_source/chapters/chapter_07_家出のお姫さま.txt (src L1165-1360),
# exact arguments in ps2_source/events_full/chapter_07 (L1105-1106 date gate,
# L1108-1286 scenes 1164-1168).
# The date is entered unconditionally from the end of ch6_2 (source scene 374:
# 【デート】アンリエッタ -> 1164); the postdate target +375 is core scene 375 of
# chapter_08 (chapter 7), which is not ported yet, so the part tail is
# `jump attention` (PROVISIONAL endpoint, re-hooked to ch7 when it is ported).
# Conventions of chapter 6: no show_sprites (ch6_1/ch6_2), backgrounds/CG as
# id(K) placeholders, system SE not ported, BGM by id (t9 = +10, t15 = +16).

label ch6_3:
    # Source date gate (events_full chapter_07 L1105-1106):
    #   dateItem("アンリエッタ", +1164); date(+375, false, +4).
    # Дére/тундére-событие вместо даты — как date() (гейт-эталон
    # script-ch5_10.rpy): zero_tundele >= 211 → tndl_pick() (chapter_91, дére);
    # слот 0 дére = кормёжка (sp_l1), K=11; остальные дére-слоты 1..5 и весь
    # тундére-блок (chapter_90, <40) не портированы → fallthrough в дату.
    if zero_tundele >= 211:
        $ zero_tndl_no = tndl_pick(zero_dele_event)
        if zero_tndl_no == 0:
            $ zero_dele_event[0] += 1
            $ zero_tundele_count += 1
            call sp_l1 from _call_sp_l1_11
            $ fade_fx("black")
            stop music fadeout 1.0
            # Postdate +375 = chapter_08 core scene 375 = начало главы 7
            # (script-ch7_1.rpy, label ch7): хук установлен при портировании
            # части 3 главы 7 (script-ch7_3.rpy).
            jump ch7

    jump ch6_3_s1164

label ch6_3_s1164:
    # Source scene 1164 (src L1165-1261): gate of the inn, night stroll to town,
    # the ring stall, 3-choice menu to scenes 1165-1167.
    # [BG stage image=+43][TRANS][BGM play=+10][SE se0 play=+55 skipped][SPRITE lay8 +810 skipped]
    $ fade_fx("id(43)", new_music="t9")
    voice "ch6.3_h_001"
    h "Oh, good… You were still up."
    # [SPRITE lay5 +412]
    voice "ch6.3_s_001"
    s "Princess? What's going on?"
    voice "ch6.3_h_002"
    h "In fact, I came because I wanted to ask my familiar for something."
    voice "ch6.3_s_002"
    s "Something? If there's anything I can do, name it."
    voice "ch6.3_h_003"
    h "Oh, that's wonderful. You see, I would like to see the town at night. So I came to ask if you would show me around."
    # [SPRITE lay5 +418]
    voice "ch6.3_s_003"
    s "Wh-what!? I just got scolded by Louise about the daytime thing! I nearly died!"
    voice "ch6.3_h_004"
    h "I have been out a few times during the day, but I have never once seen the town after sunset."
    # [SPRITE lay5 +451]
    voice "ch6.3_s_004"
    s "Could it be… slipping out of the inn into the town… or something?"
    voice "ch6.3_h_005"
    h "Yes. Let's go."
    # [SPRITE lay8 +810]
    voice "ch6.3_h_006"
    h "Look, I changed into proper clothes, after all. I am completely ready."
    # [SPRITE lay5 +416]
    voice "ch6.3_s_005"
    s "I am not ready! Mostly in spirit!"
    voice "ch6.3_h_007"
    h "Is that a no?{#ch6_3_d001}"
    # [SPRITE lay5 +418]
    th "Ugh! Being stared at by the princess with such a look… the guilt really gets to me!"
    th "No, but… I don't want to be scolded by Louise again either…"
    # [voice 394]
    voice "ch6.3_h_008"
    h "…{#ch6_3_d002}"
    # [SPRITE lay5 +412]
    voice "ch6.3_s_006"
    s "All right. But we'll keep it quiet, so Louise doesn't find out."
    # [SPRITE lay8 +810]
    voice "ch6.3_h_009"
    h "Of course! Naturally!"
    # [SPRITE lay5 +418]
    th "Ahhh… I'm really weak against girls pressing me. I know I'm going to destroy myself because of this someday."
    # [SPRITE hide][BG stage hide][WAIT waitAction skipped]
    # [BG stage image=+40][TRANS][SE se1 play=+37 skipped][SPRITE lay8 +810]
    $ fade_fx("id(40)")
    voice "ch6.3_h_010"
    h "My…!{#ch6_3_d003}"
    # [SPRITE lay5 +390]
    voice "ch6.3_s_007"
    s "Is something the matter?"
    voice "ch6.3_h_011"
    h "The night town looks so different. It appears completely unlike the daytime. It's as if it were an entirely different town…"
    # [SPRITE lay5 +423]
    voice "ch6.3_s_008"
    s "Well, it certainly is around here."
    voice "ch6.3_merchant_001"
    merchant "Come in, come in. Oh, you there with the beautiful young lady - what about a little something for your companion?"
    # [SPRITE lay8 +810]
    voice "ch6.3_h_012"
    h "My, how pretty! So many colorful rings!"
    # [SPRITE lay5 +396]
    voice "ch6.3_s_009"
    s "Um… Princess, is it that unusual to you?"
    voice "ch6.3_h_013"
    h "It's not that it's unusual, but isn't it beautiful? Oh, this is…"
    voice "ch6.3_merchant_002"
    merchant "Miss, which one caught your eye?"
    # [SPRITE lay8 +808]
    voice "ch6.3_h_014"
    h "Let me see… this top one, with the delicate craftsmanship, is…"
    # [SPRITE lay5 +390]
    voice "ch6.3_s_010"
    s "Princess…{#ch6_3_d004}"
    # 【選択肢】src L1259-1261 → scenes 1165-1167
    menu:
        "I'll buy it for you":
            jump ch6_3_s1165
        "You must have better ones":
            jump ch6_3_s1166
        "Wouldn't you like to see other shops too?":
            jump ch6_3_s1167

label ch6_3_s1165:
    # Source scene 1165 (src L1263-1278): "I'll buy it for you" branch.
    # [BGM play=+10][SE se1 play=+37 skipped][BG stage image=+40]
    $ fade_fx("id(40)", new_music="t9")
    voice "ch6.3_s_011"
    s "I'll buy it for you."
    voice "ch6.3_h_015"
    h "Are you sure?{#ch6_3_d005}"
    voice "ch6.3_s_012"
    s "Well, for something like this, I can manage with my pocket money."
    voice "ch6.3_h_016"
    h "No, that's not what I mean…"
    # → next scene 1168
    jump ch6_3_s1168

label ch6_3_s1166:
    # Source scene 1166 (src L1280-1299): "You must have better ones" branch.
    # [BGM play=+10][SE se1 play=+37 skipped][BG stage image=+40]
    $ fade_fx("id(40)", new_music="t9")
    voice "ch6.3_s_013"
    s "You must have better ones at home?"
    voice "ch6.3_h_017"
    h "Well, that is true, but…"
    voice "ch6.3_h_018"
    h "But those are things that have been in our house for a long time, or gifts given to it. They are not things that belong to me personally."
    voice "ch6.3_s_014"
    s "Princess…{#ch6_3_d006}"
    voice "ch6.3_h_019"
    h "The ring itself may be cheap, but choosing it for myself is what makes it enjoyable. That is a value that cannot be put a price on."
    # → next scene 1168
    jump ch6_3_s1168

label ch6_3_s1167:
    # Source scene 1167 (src L1301-1318): "See other shops" branch.
    # [BGM play=+10][SE se1 play=+37 skipped][BG stage image=+40]
    $ fade_fx("id(40)", new_music="t9")
    voice "ch6.3_s_015"
    s "Wouldn't you like to see other shops too?{#ch6_3_d007}"
    voice "ch6.3_h_020"
    h "Hm? Oh, yes, of course."
    th "Even while saying that, her eyes won't leave the rings on display. It's in places like these that the princess is still just a girl."
    voice "ch6.3_s_016"
    s "All right then."
    # → next scene 1168
    jump ch6_3_s1168

label ch6_3_s1168:
    # Source scene 1168 (src L1320-1360): buying the ring, CG, tail of the date.
    # [BGM play=+10][SE se1 play=+37 skipped][BG stage image=+40]
    $ fade_fx("id(40)", new_music="t9")
    voice "ch6.3_s_017"
    s "Dad, give me this ring. Is this enough?"
    voice "ch6.3_h_021"
    h "Familiar!?"
    voice "ch6.3_merchant_003"
    merchant "Right away, thank you for your patronage!"
    voice "ch6.3_s_018"
    s "Here you are, Princess."
    # [BGM stop=1000][SPRITE hide][BG hide][WAIT waitAction skipped]
    stop music fadeout 1.0
    # [BGM play=+16 → t15][EVENT_CG event image=+263][TRANS crossfade]
    $ dissolve_fx("id(263)", type="cg")
    voice "ch6.3_h_022"
    h "Ah… thank you…"
    # [EVENT_CG event image=+262][WAIT waitLoad skipped]
    $ dissolve_fx("id(262)", type="cg")
    voice "ch6.3_h_023"
    h "Heh, how does it look?"
    voice "ch6.3_s_019"
    s "Yeah, it's really pretty for something from a street stall."
    # [EVENT_CG event image=+263]
    $ dissolve_fx("id(263)", type="cg")
    voice "ch6.3_h_024"
    h "Heh heh. Looking at it like this, it almost looks like an engagement ring."
    voice "ch6.3_s_020"
    s "Hm?{#ch6_3_d008}"
    voice "ch6.3_h_025"
    h "Nothing at all. Heh heh."
    # [SE stop][BGM stop=1000][SPRITE/BG hide][EVENT_CG hide][WAIT waitTime skipped]
    stop music fadeout 1.0
    # [COFFEE → $ pause(1.0), AGENTS.md §6; not ported literally]
    $ pause(1.0)
    # 【デート進行】→ next scene 375 = chapter_08 core (chapter 7): хук на
    # script-ch7_1.rpy (label ch7), установлен при портировании части 3 главы 7.
    jump ch7
