# Глава 11, часть 1 (сцены 467-471): «ハルナの決意» — начало, сцена пропажи, поиск.
# Источник: ps2_source/chapters/chapter_12_ハルナの決意.txt (SCENE 467-471).
# Точные аргументы: ps2_source/events_full/chapter_12_ハルナの決義.txt.
#
# Голоса: 32 (сцены 467-471). Нумерация ch11_<spk>_<NNN> — с 001 по говорящему.
#   si: 15120-15125 (6)
#   s: 13216-13227 (12)
#   l: 7160-7167 (8)
# Спрайты: id → имя по references/sprite_id_map.csv; PROVISIONAL для не подтверждённых.
# Фоны: id(2)=white, id(10)=louise_room/classroom, id(20)=corridor, id(26)=yard,
#   id(29)=council_room, id(32)=kitchen, id(85)=forest, id(88)=sky, id(1145)=overlay, id(1171)=overlay.
# CG: id(K) — заглушки, требуют решения человека.
# BGM: bgm play=+30→t29, +19→t18, +5→t4 — все есть.
# SE: se0 play=+57; se1 stop=1 — не переносятся (SE заглушка).
# Не переносятся: MOVIE(1) — movie(1); beginSkip/endSkip — пропускается;
#   waitSEStop/waitLoad/waitAction/waitTime — паузы/задержки.
#
# К обращению: по addresses.md — «мадемуазель/Ваше Высочество» для Анриетты,
#   «сан/кун» для сверстников, «сэнсэй» для учителей.

label ch11:
    $ tndl(None)
    # Титульный монтаж → overlay_screen (образ «overlay»).
    call overlay_screen("overlay", "Chapter Eleven: 'Haruna's Decision'{#ch11_title}", isUseBlur=False, text_mode="black") from _call_overlay_screen_18
    pause(2)


    # ==== SCENE 467 ====
    # [TITLE title("ハルナの決意")] — входит в титульный монтаж overlay_screen
    # [BG stage image=+88] [TRANS trans("crossfade", 500)]
    # [BGM bgm play=+5 → t4]
    $ show_sprites()
    play music t4 fadein 1.0
    # シエスタ：サイトさん、ミス・ヴァリエール。
    # おはようございます！  [voice 15120]
    voice "ch11_si_001"
    si "Good morning, Site-san, Miss Varière!{#ch11_si_001}"
    # JA[15120]: シエスタ：サイトさん、ミス・ヴァリエール。
    #   おはようございます！
    # サイト：ううっ、なんだ？
    # まだ起きる時間じゃないのに。  [voice 13216]
    voice "ch11_s_001"
    s "Ugh, what? It's not even morning yet.{#ch11_s_001}"
    # JA[13216]: サイト：ううっ、なんだ？
    #   まだ起きる時間じゃないのに。
    # ルイズ：なによぉ？
    # いったい。
    # サイト……早く出てよ……。  [voice 7160]
    voice "ch11_l_001"
    l "What is it, really? Site…… get out already……{#ch11_l_001}"
    # JA[7160]: ルイズ：なによぉ？ / いったい。
    #   サイト……早く出てよ……。
    # サイト：へいへい……。  [voice 13217]
    voice "ch11_s_002"
    s "Yeah, yeah…….{#ch11_s_002}"
    # JA[13217]: サイト：へいへい……。
    #  [SE se0 play=+57] — не переносится
    #  [SPRITE lay2 hide]
    #  [SPRITE lay5 hide]
    #  [SPRITE lay1 hide]
    #  [BG stage hide]
    #  [BG stage image=+10, level=200]
    #  [TRANS trans("crossfade", 1000)]
    #  [SPRITE lay5 image=+418, level=160, dir=1C]
    # サイト：ふぁい……。
    # こんな朝っぱらから誰？  [voice 13218]
    voice "ch11_s_003"
    s "Fwaa…… who's here this early?{#ch11_s_003}"
    # JA[13218]: サイト：ふぁい……。 / こんな朝っぱらから誰？
    #  [SE se0 play=+56]
    #  [SPRITE lay5 x=224, y=0]
    #  [SPRITE lay2 image=+495, level=160, dir=1A]
    # シエスタ：朝早くから申し訳ありませんっ！  [voice 15121]
    voice "ch11_si_002"
    si "Sorry for the early morning!{#ch11_si_002}"
    # JA[15121]: シエスタ：朝早くから申し訳ありませんっ！
    #  [SPRITE lay5 image=+451, level=160, dir=2C]
    # サイト：あれぇ？
    # シエスタ、どうしたの？  [voice 13219]
    voice "ch11_s_004"
    s "Huh? Siesta, what's wrong?{#ch11_s_004}"
    # JA[13219]: サイト：あれぇ？ / シエスタ、どうしたの？
    # シエスタ：ハルナさんはこちらに来ておられませんか！  [voice 15122]
    voice "ch11_si_003"
    si "Has Haruna-san come here?{#ch11_si_003}"
    # JA[15122]: シエスタ：ハルナさんはこちらに来ておられませんか！
    #  [SPRITE lay5 image=+418, level=160, dir=1C]
    # サイト：えっ、いや来てないけど？  [voice 13220]
    voice "ch11_s_005"
    s "What? No, she hasn't.{#ch11_s_005}"
    # JA[13220]: サイト：えっ、いや来てないけど？
    #  [BG stage hide]
    #  [BG stage image=+2] [TRANS trans("crossfade", 500)]
    #  [BG stage image=+1145] [TRANS trans("crossfade", 1000)]
    #  [BG stage image=+1170] [TRANS trans("crossfade", 1000)]
    #  [BG stage image=+1145] [TRANS trans("crossfade", 1000)]
    #  [BG stage image=+2] [TRANS trans("crossfade", 2000)]
    #  [BG stage image=+88, level=200]
    #  [TRANS trans("crossfade", 1000)]
    #  [BGM bgm play=+19 → t18]
    play music t18 fadein 1.0
    $ fade_fx("classroom")
    #  [SPRITE lay7 image=+951 → h 2]
    $ show_sprites(("h 2"))
    # ルイズ：どうしたのよ、シエスタ。
    # そんな大声出して。  [voice 7161]
    voice "ch11_l_002"
    l "What's wrong, Siesta? Shouting that loud.{#ch11_l_002}"
    # JA[7161]: ルイズ：どうしたのよ、シエスタ。そんな大声出して。
    #  [SPRITE lay7 image=+951 → h 2]
    $ show_sprites(("h 2"))
    # シエスタ：すみません。
    # ミス・ヴァリエール。  [voice 15123]
    voice "ch11_si_004"
    si "Sorry. / Miss Varière.{#ch11_si_004}"
    # JA[15123]: シエスタ：すみません。ミス・ヴァリエール。
    # シエスタ：ハルナさんが……、
    # ハルナさんがいなくなったんです！  [voice 15124]
    voice "ch11_si_005"
    si "Haruna-san…… / Haruna-san is gone missing!{#ch11_si_005}"
    # JA[15124]: シエスタ：ハルナさんが……、ハルナさんがいなくなったんです！
    #  [SPRITE lay1 hide]
    #  [SPRITE lay5 image=+451, level=160, dir=2C]
    # サイト：へ？  [voice 13221]
    voice "ch11_s_006"
    s "Huh?{#ch11_s_006}"
    # JA[13221]: サイト：へ？
    #  [SPRITE lay5 hide]
    #  [SPRITE lay1 image=+328, level=160, dir=1C]
    # ルイズ：ハルナが？
    # ど、どういうこと？  [voice 7162]
    voice "ch11_l_003"
    l "Haruna? / What do you mean?{#ch11_l_003}"
    # JA[7162]: ルイズ：ハルナが？ど、どういうこと？
    # シエスタ：朝起きたら、部屋にハルナさんがいなくて……。
    # 厨房や広間も探してみたんですけど……。
    # どこにもいなくって……。  [voice 15125]
    voice "ch11_si_006"
    si "When I woke up, / Haruna-san wasn't in her room…… / I looked in the kitchen and the hall too…… / but she's nowhere……{#ch11_si_006}"
    # JA[15125]: シエスタ：朝起きたら、部屋にハルナさんがいなくて……。 / 厨房や広間も探してみたんですけど……。 / どこにもいなくって……。
    #  【選択肢】そんなに慌てなくても → scene 468
    #  【選択肢】すぐに探そう → scene 469
    #  【選択肢】少し待ってみよう → scene 470

    # ==== SCENE 468 ====
    # サイト：別に少しいないぐらいで
    # そんなに慌てなくても……。  [voice 13222]
    voice "ch11_s_007"
    s "But if she hasn't been / gone long, / there's no need to panic……{#ch11_s_007}"
    # JA[13222]: サイト：別に少しいないぐらいで / そんなに慌てなくても……。
    # シエスタ：なに言ってるんですか！
    # ハルナさん、昨日からずいぶん
    # 悩んでたんですよ！  [voice 15126]
    voice "ch11_si_007"
    si "What are you saying! / Haruna-san / has been worried / since yesterday!{#ch11_si_007}"
    # JA[15126]: シエスタ：なに言ってるんですか！ / ハルナさん、昨日からずいぶん / 悩んでたんですよ！
    # シエスタ：もし……。
    # 早まったことなんてしてたら……！
    # ああ、どうしよう！  [voice 15127]
    voice "ch11_si_008"
    si "What if…… / What if she did something rash……! / Oh, what should we do!{#ch11_si_008}"
    # JA[15127]: シエスタ：もし……。 / 早めたことなんてしてたら……！ / ああ、どうしよう！
    # サイト：わ、分かった！
    # とにかく探しにいこう！  [voice 13223]
    voice "ch11_s_008"
    s "O-okay! / Anyway, let's go look!{#ch11_s_008}"
    # JA[13223]: サイト：わ、分かった！ / とにかく探しにいこう！
    #  → next scene 471

    # ==== SCENE 469 ====
    # サイト：な、なんだって！
    # わ、分かった！
    # すぐ探しにいこう！  [voice 13224]
    voice "ch11_s_009"
    s "Wh-what! / O-okay! / Let's go look right away!{#ch11_s_009}"
    # JA[13224]: サイト：な、なんだって！ / わ、分かった！ / すぐ探しにいこう！
    # ルイズ：な、なによ。
    # そんなに慌てなくても。  [voice 7163]
    voice "ch11_l_004"
    l "Wh-what? / No need to panic so much.{#ch11_l_004}"
    # JA[7163]: ルイズ：な、なによ。 / そんなに慌てなくても。
    # シエスタ：ミス・ヴァリエール……。  [voice 15128]
    voice "ch11_si_009"
    si "Miss Varière……{#ch11_si_009}"
    # JA[15128]: シエスタ：ミス・ヴァリエール……。
    # ルイズ：わ、分かったわよ！  [voice 7164]
    voice "ch11_l_005"
    l "O-okay, okay!{#ch11_l_005}"
    # JA[7164]: ルイズ：わ、分かったわよ！
    # ルイズ：わたしも探しに行くから、
    # 少し待って！  [voice 7165]
    voice "ch11_l_006"
    l "I'm going to look too, / so wait a little!{#ch11_l_006}"
    # JA[7165]: ルイズ：わたしも探しに行くから、 / 少し待って！
    #  → next scene 471

    # ==== SCENE 470 ====
    # サイト：と、とりあえず、少し待ってみたら……。  [voice 13225]
    voice "ch11_s_010"
    s "F-for now, let's wait and see……{#ch11_s_010}"
    # JA[13225]: サイト：と、とりあえず、少し待ってみたら……。
    # シエスタ：で、ですけど！  [voice 15129]
    voice "ch11_si_010"
    si "But!{#ch11_si_010}"
    # JA[15129]: シエスタ：で、ですけど！
    # シエスタ：その待ってる間になにかあったら……。  [voice 15130]
    voice "ch11_si_011"
    si "If something happens / while we wait……{#ch11_si_011}"
    # JA[15130]: シエスタ：その待ってる間になにかあったら……。
    # ルイズ：……。  [voice 7166]
    voice "ch11_l_007"
    l "…{#ch11_l_007}"
    # JA[7166]: ルイズ：……。
    # シエスタ：わ、わたし、もう一度探しに行きます！  [voice 15131]
    voice "ch11_si_012"
    si "I'll go look again!{#ch11_si_012}"
    # JA[15131]: シエスタ：わ、わたし、もう一度探しに行きます！
    # ルイズ：わたしも探しに行くわ！  [voice 7167]
    voice "ch11_l_008"
    l "I'm going to look too!{#ch11_l_008}"
    # JA[7167]: ルイズ：わたしも探しに行くわ！
    # サイト：わ、分かったって！
    # 俺も探しにいくから。  [voice 13226]
    voice "ch11_s_011"
    s "O-okay, okay! / I'll go look too.{#ch11_s_011}"
    # JA[13226]: サイト：わ、分かったって！ / 俺も探しにいくから。

    # ==== SCENE 471 ====
    # サイト：（やっぱり春奈は悩んでたんだ）
    # サイト：（春奈を見つけて、俺は何て言えばいいんだろう？）
    # サイト：……。  [voice 13227]
    voice "ch11_s_012"
    s "(As I thought, Haruna was worrying.) / (When I find Haruna, / what should I say?) / ……{#ch11_s_012}"
    # JA[13227]: サイト：（やっぱり春奈は悩んでたんだ） / （春奈を見つけて、俺は何て言えばいいんだろう？） / ……。
    #  → jump ch11_2 (scene 472 — поиск, ハルナ発見)

    # ==== КОНЕЦ ГЛАВЫ 11, ЧАСТИ 1 ====
    # Дальше — SCENE 472 (ハルナ発見), voice: 2559-2577.

    # → jump ch11_2
    jump ch11_2
    return
