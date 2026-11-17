# Глава 10, часть 1 (сцены 431-446): «Внезапный скаут» — начало, выбор, диалоги, переходы.
# Источник: ps2_source/chapters/chapter_11_突然のスカウト.txt (SCENE 431-446).
# Точные аргументы: ps2_source/events_full/chapter_11_突然のスカウト.txt.
#
# Голоса: 144 (сцены 431-446). Нумерация ch10_<spk>_<NNN> — с 001 по говорящему.
#   s: 13136-13169 (34)
#   h: 2456-2518 (63)
#   si: 15078-15108 (31)
#   l: 7142-7149 (8)
#   o: 4500-4505 (6)
#   c: 1201-1203 (3)
#   PS2 voice IDs: s=13136-13169; h=2456-2518; si=15078-15108; l=7142-7149; o=4500-4505; c=1201-1203
# Спрайты: id → имя по references/sprite_id_map.csv; PROVISIONAL для не подтверждённых.
# Фоны: id(2)=white, id(10)=classroom, id(20)=corridor, id(26)=yard, id(29)=council_room,
#   id(32)=kitchen, id(88)=sky, id(1145)=overlay, id(1170)=overlay.
# CG: id(K) — заглушки, требуют решения человека.
# BGM: bgm play=+5→t4, +19→t18, +29→t28, +32→t31 — все есть.
# SE: se0 play=+57; se1 stop=1 — не переносятся (SE заглушка).
# Не переносятся: MOVIE(1) — movie(1); beginSkip/endSkip — пропускается;
#   waitSEStop/waitLoad/waitAction/waitTime — паузы/задержки.
#
# К обращению: по addresses.md — «мадемуазель/Ваше Высочество» для Анриетты,
#   «сан/кун» для сверстников, «сэнсэй» для учителей.

label ch10:
    $ tndl(None)
    # Титульный монтаж → overlay_screen (образ «overlay»).
    call overlay_screen("overlay", "Chapter Ten: 'The Sudden Scout'{#ch10_title}", isUseBlur=False, text_mode="black") from _call_overlay_screen_15
    pause(2)


    # ==== SCENE 431 ====
    # [TITLE title("突然のスカウト")] — входит в титульный монтаж overlay_screen
    # [BG stage image=+88] [TRANS trans("crossfade", 1000)]
    # [BGM bgm play=+5 → t4]
    $ show_sprites()
    play music t4 fadein 1.0
    # サイト：（演劇が終わってから、かれこれ数日。 / いきなり、爆弾使いが現れなく / なってしまった）
    s "(A few days since the play ended. / The bomb user suddenly vanished…){#ch10_s_001}"
    # JA[null]: サイト：（演劇が終わってから、かれこれ数日。 / いきなり、爆弾使いが現れなく / なってしまった）
    # サイト：（そのため、みんなそろって魔法学院に / 戻ることになったわけなんだけど……）
    s "(So everyone returned to the magic academy…){#ch10_s_002}"
    # JA[null]: サイト：（そのため、みんなそろって魔法学院に / 戻ることになったわけなんだけど……）
    # サイト：（結果らしい結果をだせなかったことと、 / 爆弾使いの正体が分からないことから、 / みんなやたらと気が立ってしまっている）
    s "(No results, no clue who the bomb user is — / everyone is on edge.){#ch10_s_003}"
    # JA[null]: サイト：（結果らしい結果をだせなかったことと、 / 爆弾使いの正体が分からないことから、 / みんなやたらと気が立ってしまっている）
    # [BGM bgm stop=1000] → fadeout
    stop music fadeout 1.0
    # [SPRITE lay5 hide]
    # [BG stage image=+2] [TRANS trans("crossfade", 500)]
    # [BG stage image=+1145] [TRANS trans("crossfade", 1000)]
    # [BG stage image=+1170] [TRANS trans("crossfade", 1000)]
    # [BG stage image=+1145] [TRANS trans("crossfade", 1000)]
    # [BG stage image=+2] [TRANS trans("crossfade", 2000)]
    # [BG stage image=+10] [TRANS trans("crossfade", 1000)]
    # [BGM bgm play=+19 → t18]
    play music t18 fadein 1.0
    $ fade_fx("classroom")
    # [SPRITE lay7 image=+951 → h 2]
    $ show_sprites(("h 2"))
    # ハルナ：教科書……ノート……カラーペン色々…… / ……プリ帳……タオル……制汗スプレー…… / お化粧ポーチ……文庫本……。  [voice 2456]
    voice "ch10_h_001"
    h "Textbooks… notebooks… colored pens… / …sketchbook… towel… deodorant spray… / makeup pouch… paperback… {#ch10_h_001}"
    # JA[2456]: ハルナ：教科書……ノート……カラーペン色々…… / ……プリ帳……タオル……制汗スプレー…… / お化粧ポーチ……文庫本……。
    # [SPRITE lay7 image=+953 → h 2 happy]
    $ show_sprites(("h 2 happy"))
    # ハルナ：あ、アメ玉発見っ！  [voice 2457]
    voice "ch10_h_002"
    h "Ah, found some candy! {#ch10_h_002}"
    # JA[2457]: ハルナ：あ、アメ玉発見っ！
    # ハルナ：うん、甘～い！ / 久しぶり～～。  [voice 2458]
    voice "ch10_h_003"
    h "Mmm, sweet~! / Long time no see~. {#ch10_h_003}"
    # JA[2458]: ハルナ：うん、甘～い！ / 久しぶり～～。
    # [SPRITE lay7 image=+951 → h 2]
    $ show_sprites(("h 2"))
    # ハルナ：良かった。  [voice 2459]
    voice "ch10_h_004"
    h "Good. {#ch10_h_004}"
    # JA[2459]: ハルナ：良かった。
    # ハルナ：ウェザリーさん、ちゃんと鞄の中身は / 保管してくれてたんだ。  [voice 2460]
    voice "ch10_h_005"
    h "Wesley-san kept my bag contents / safe for me. {#ch10_h_005}"
    # JA[2460]: ハルナ：ウェザリーさん、ちゃんと鞄の中身は / 保管してくれてたんだ。
    # [SPRITE lay7 image=+953 → h 2 happy]
    $ show_sprites(("h 2 happy"))
    # ハルナ：あ、ケータイ！  [voice 2461]
    voice "ch10_h_006"
    h "Ah, my phone! {#ch10_h_006}"
    # JA[2461]: ハルナ：あ、ケータイ！
    # [SPRITE lay7 image=+951 → h 2]
    $ show_sprites(("h 2"))
    # ハルナ：……。  [voice 2462]
    voice "ch10_h_007"
    h "…{#ch10_h_007}"
    # JA[2462]: ハルナ：……。
    # [SPRITE lay7 image=+957 → h 2 sad]
    $ show_sprites(("h 2 sad"))
    # ハルナ：やっぱり電池が切れてる。  [voice 2463]
    voice "ch10_h_008"
    h "The battery is dead, as expected. {#ch10_h_008}"
    # JA[2463]: ハルナ：やっぱり電池が切れてる。
    # ハルナ：……。  [voice 2464]
    voice "ch10_h_009"
    h "…{#ch10_h_009}"
    # JA[2464]: ハルナ：……。
    # [SPRITE lay7 image=+951 → h 2]
    $ show_sprites(("h 2"))
    # ハルナ：なに期待してたんだろ。 / バカみたい。  [voice 2465]
    voice "ch10_h_010"
    h "What was I expecting? / I'm such an idiot. {#ch10_h_010}"
    # JA[2465]: ハルナ：なに期待してたんだろ。 / バカみたい。
    # [SE se0 play=+57] — не переносится
    # [SPRITE lay7 x=-96, y=0]
    # [SPRITE lay5 image=+390 → s 1]
    $ show_sprites(("s 1", "h 2"))
    # サイト：あれ？ / なにしてるの、春奈？  [voice 13136]
    voice "ch10_s_004"
    s "Hm? / What are you doing, Haruna? {#ch10_s_004}"
    # JA[13136]: サイト：あれ？ / なにしてるの、春奈？
    # [SPRITE lay7 image=+953 → h 2 happy]
    $ show_sprites(("s 1", "h 2 happy"))
    # ハルナ：あっ、平賀くん！  [voice 2466]
    voice "ch10_h_011"
    h "Ah, Hiraga-kun! {#ch10_h_011}"
    # JA[2466]: ハルナ：あっ、平賀くん！
    # [SPRITE lay7 image=+951 → h 2]
    $ show_sprites(("s 1", "h 2"))
    # ハルナ：ウェザリーさんから返してもらった、 / バッグの中身をチェックしてたの。  [voice 2467]
    voice "ch10_h_012"
    h "Wesley-san returned it, so I was / checking what's inside the bag. {#ch10_h_012}"
    # JA[2467]: ハルナ：ウェザリーさんから返してもらった、 / バッグの中身をチェックしてたの。
    # サイト：無くなってるものとかは？  [voice 13137]
    voice "ch10_s_005"
    s "Anything missing? {#ch10_s_005}"
    # JA[13137]: サイト：無くなってるものとかは？
    # ハルナ：ううん、特には。  [voice 2468]
    voice "ch10_h_013"
    h "No, nothing special. {#ch10_h_013}"
    # JA[2468]: ハルナ：ううん、特には。
    # 【選択肢】あ、ケータイ？ → scene 432
    # 【選択肢】手帳？ → scene 433
    # 【選択肢】教科書か…… → scene 434
    menu:
        "Ah, your phone? {#ch10_choice_001}":
            jump ch10_432
        "Your notebook? {#ch10_choice_002}":
            jump ch10_433
        "Your textbook… {#ch10_choice_003}":
            jump ch10_434


    # ==== SCENE 432 ====
    # [SPRITE lay5 image=+390 → s 1] [SPRITE lay7 image=+951 → h 2]
    # [BGM bgm play=+19 → t18]
    # [BG stage image=+10] [SPRITE lay5 image=+392 → s 1]
    label ch10_432:
        $ show_sprites(("s 1", "h 2"))
        play music t18 fadein 1.0
        # サイト：うわ、それ、ケータイじゃん！ / なっつかし……。  [voice 13138]
        voice "ch10_s_006"
        s "Whoa, that's a phone! / Nostalgic… {#ch10_s_006}"
        # JA[13138]: サイト：うわ、それ、ケータイじゃん！ / なっつかし……。
        # [SPRITE lay7 image=+957 → h 2 sad]
        $ show_sprites(("s 1", "h 2 sad"))
        # ハルナ：でも、電池切れ。 / 充電器なんか持ち歩かないもの……。 / それにどうせ電池があっても圏外だし。  [voice 2469]
        voice "ch10_h_014"
        h "But the battery's dead. / I don't carry a charger around… / Besides, even with battery, there's no signal. {#ch10_h_014}"
        # JA[2469]: ハルナ：でも、電池切れ。 / 充電器なんか持ち歩かないもの……。 / それにどうせ電池があっても圏外だし。
        # [SPRITE lay5 image=+423 → s 1 sad]
        $ show_sprites(("s 1 sad", "h 2 sad"))
        # サイト：まあ、充電器があってもだめだけどね。 / こっちは電気そのものが無いし。  [voice 13139]
        voice "ch10_s_007"
        s "Well, even with a charger it wouldn't work. / There's no electricity here either. {#ch10_s_007}"
        # JA[13139]: サイト：まあ、充電器があってもだめだけどね。 / こっちは電気そのものが無いし。
        # [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("s 1 sad", "h 2"))
        # ハルナ：そうね。 / でも充電できれば、 / せめてカメラくらいは使えたのに。  [voice 2470]
        voice "ch10_h_015"
        h "I know. / But if I could charge it, / at least I could use the camera. {#ch10_h_015}"
        # JA[2470]: ハルナ：そうね。 / でも充電できれば、 / せめてカメラくらいは使えたのに。
        # [SPRITE lay5 image=+390 → s 1]
        $ show_sprites(("s 1", "h 2"))
        # サイト：写真かぁ。 / 最近撮ってないなぁ。 / まぁ、この世界にはカメラはないからね。  [voice 13140]
        voice "ch10_s_008"
        s "Photos, huh. / Haven't taken any lately. / Well, there are no cameras in this world. {#ch10_s_008}"
        # JA[13140]: サイト：写真かぁ。 / 最近撮ってないなぁ。 / まぁ、この世界にはカメラはないからね。
        # → next scene 435
        jump ch10_435


    # ==== SCENE 433 ====
    # [SPRITE lay5 image=+390 → s 1] [SPRITE lay7 image=+951 → h 2]
    # [BGM bgm play=+19 → t18]
    # [BG stage image=+10] [SPRITE lay5 image=+392 → s 1]
    label ch10_433:
        $ show_sprites(("s 1", "h 2"))
        play music t18 fadein 1.0
        # サイト：あ、その手帳は？  [voice 13141]
        voice "ch10_s_009"
        s "Ah, what about that notebook? {#ch10_s_009}"
        # JA[13141]: サイト：あ、その手帳は？
        # [SPRITE lay7 image=+951 → h 2]
        # ハルナ：う、うん。 / これは、私の大切な手帳。  [voice 2471]
        voice "ch10_h_016"
        h "Y-yeah. / This is my precious notebook. {#ch10_h_016}"
        # JA[2471]: ハルナ：う、うん。 / これは、私の大切な手帳。
        # [SPRITE lay5 image=+423 → s 1 sad]
        $ show_sprites(("s 1 sad", "h 2"))
        # サイト：ふーん、そうなんだ。  [voice 13142]
        voice "ch10_s_010"
        s "Hmm, I see. {#ch10_s_010}"
        # JA[13142]: サイト：ふーん、そうなんだ。
        # → next scene 435
        jump ch10_435


    # ==== SCENE 434 ====
    # [SPRITE lay5 image=+390 → s 1] [SPRITE lay7 image=+951 → h 2]
    # [BGM bgm play=+19 → t18]
    # [BG stage image=+10] [SPRITE lay5 image=+396 → s 1]
    label ch10_434:
        $ show_sprites(("s 1", "h 2"))
        play music t18 fadein 1.0
        # サイト：うっ、教科書か……。  [voice 13143]
        voice "ch10_s_011"
        s "Ah, the textbook… {#ch10_s_011}"
        # JA[13143]: サイト：うっ、教科書か……。
        # [SPRITE lay7 image=+953 → h 2 happy]
        $ show_sprites(("s 1", "h 2 happy"))
        # ハルナ：ええ、そうよ。 / これでこっちの世界でも、勉強ができるわね。  [voice 2472]
        voice "ch10_h_017"
        h "Yes, that's right. / With this, I can study in this world too. {#ch10_h_017}"
        # JA[2472]: ハルナ：ええ、そうよ。 / これでこっちの世界でも、勉強ができるわね。
        # [SPRITE lay5 image=+429 → s 1 sad]
        $ show_sprites(("s 1 sad", "h 2 happy"))
        # サイト：ほんっと、優等生だよなあ。  [voice 13144]
        voice "ch10_s_012"
        s "You really are a model student. {#ch10_s_012}"
        # JA[13144]: サイト：ほんっと、優等生だよなあ。
        # → next scene 435
        jump ch10_435


    # ==== SCENE 435 ====
    # [SPRITE lay5 image=+390 → s 1] [SPRITE lay7 image=+951 → h 2]
    # [BGM bgm play=+19 → t18]
    # [BG stage image=+10]
    # [SPRITE lay5 hide] [SPRITE lay7 hide] [BG stage hide]
    # null：………。 / ……。 / …。
    label ch10_435:
        $ show_sprites(("s 1", "h 2"))
        play music t18 fadein 1.0
        $ show_sprites()
        # [BG stage image=+10] [TRANS trans("crossfade", 1000)]
        # [SPRITE lay7 image=+953 → h 2 happy] [SPRITE lay5 image=+390 → s 1]
        $ fade_fx("classroom")
        $ show_sprites(("s 1", "h 2 happy"))
        # ハルナ：鞄、見つかって良かった。 / ホントに。  [voice 2473]
        voice "ch10_h_018"
        h "I'm glad you found the bag. / Really. {#ch10_h_018}"
        # JA[2473]: ハルナ：鞄、見つかって良かった。 / ホントに。
        # [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("s 1", "h 2"))
        # ハルナ：……。  [null]
        h "…{#ch10_h_019}"
        # JA[null]: ハルナ：……。
        # ハルナ：ねぇ、平賀くん。  [voice 2474]
        voice "ch10_h_020"
        h "Hey, Hiraga-kun. {#ch10_h_020}"
        # JA[2474]: ハルナ：ねぇ、平賀くん。
        # サイト：ん？  [voice 13145]
        voice "ch10_s_013"
        s "Hm? {#ch10_s_013}"
        # JA[13145]: サイト：ん？
        # [SPRITE lay7 image=+957 → h 2 sad]
        $ show_sprites(("s 1", "h 2 sad"))
        # ハルナ：これから私、どうしたらいいのかな？  [voice 2475]
        voice "ch10_h_021"
        h "What should I do from now on? {#ch10_h_021}"
        # JA[2475]: ハルナ：これから私、どうしたらいいのかな？
        # [SPRITE lay5 image=+429 → s 1 sad]
        $ show_sprites(("s 1 sad", "h 2 sad"))
        # サイト：え、どうかしたの？  [voice 13146]
        voice "ch10_s_014"
        s "Huh, is something wrong? {#ch10_s_014}"
        # JA[13146]: サイト：え、どうかしたの？
        # [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("s 1 sad", "h 2"))
        # ハルナ：私ね。 / 平賀くんみたいに凄い力もないし、 / 魔法も使えない。  [voice 2476]
        voice "ch10_h_022"
        h "Me? / I don't have any special power like you, / and I can't use magic. {#ch10_h_022}"
        # JA[2476]: ハルナ：私ね。 / 平賀くんみたいに凄い力もないし、 / 魔法も使えない。
        # ハルナ：何か得意なことがあるわけでもない。  [voice 2477]
        voice "ch10_h_023"
        h "And I'm not good at anything special. {#ch10_h_023}"
        # JA[2477]: ハルナ：何か得意なことがあるわけでもない。
        # [SPRITE lay7 image=+957 → h 2 sad]
        $ show_sprites(("s 1 sad", "h 2 sad"))
        # ハルナ：これまでは流れで何とかなったけど、 / これからはそうもいかないだろうって / 思ったら急に不安になってきて……。  [voice 2478]
        voice "ch10_h_024"
        h "So far things worked out somehow, / but I suddenly got anxious thinking / that won't be the case from now on… {#ch10_h_024}"
        # JA[2478]: ハルナ：これまでは流れで何とかなったけど、 / これからはそうもいかないだろうって / 思ったら急に不安になってきて……。
        # サイト：（春奈は頭がいいから、 / 考えすぎてるのかなぁ……）
        s "(Haruna is smart, so / maybe she's overthinking it…){#ch10_s_015}"
        # JA[null]: サイト：（春奈は頭がいいから、 / 考えすぎてるのかなぁ……）
        # [SPRITE lay5 image=+390 → s 1]
        $ show_sprites(("s 1", "h 2 sad"))
        # サイト：まあ、何もできないって不安になるなら、 / 何かできるようになればいいんじゃない？  [voice 13147]
        voice "ch10_s_016"
        s "Well, if you're anxious about not being able to do anything, / why not learn to do something? {#ch10_s_016}"
        # JA[13147]: サイト：まあ、何もできないって不安になるなら、 / 何かできるようになればいいんじゃない？
        # [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("s 1", "h 2"))
        # ハルナ：え？  [voice 2479]
        voice "ch10_h_025"
        h "Hm? {#ch10_h_025}"
        # JA[2479]: ハルナ：え？
        # [SPRITE lay5 image=+423 → s 1 sad]
        $ show_sprites(("s 1 sad", "h 2"))
        # サイト：とりあえず、シエスタのところで / メイドの仕事を覚えてみるとか、どうかな？  [voice 13148]
        voice "ch10_s_017"
        s "How about learning to be a maid / at Siesta's place, for starters? {#ch10_s_017}"
        # JA[13148]: サイト：とりあえず、シエスタのところで / メイドの仕事を覚えてみるとか、どうかな？
        # [SE se1 stop=1] — не переносится
        # [BGM bgm stop=1000] → fadeout
        stop music fadeout 1.0
        # [SPRITE lay7 hide] [SPRITE lay5 hide] [BG stage hide]
        $ show_sprites()
        # → next scene 436
        jump ch10_436


    # ==== SCENE 436 ====
    # [BG stage image=+10] [TRANS trans("crossfade", 1000)]
    # [BGM bgm play=+19 → t18]
    # [SPRITE lay5 image=+390 → s 1] [SPRITE lay1 image=+302 → l 1]
    label ch10_436:
        $ fade_fx("classroom")
        play music t18 fadein 1.0
        $ show_sprites(("s 1", "l 1"))
        # サイト：というわけでさ。 / シエスタのとこで、春奈にメイドの修行 / してもらおうかと思うんだけど、どうかな？  [voice 13149]
        voice "ch10_s_018"
        s "So, I was thinking of having Haruna / train as a maid at Siesta's place. What do you think? {#ch10_s_018}"
        # JA[13149]: サイト：というわけでさ。 / シエスタのとこで、春奈にメイドの修行 / してもらおうかと思うんだけど、どうかな？
        # ルイズ：なるほどね。 / そういうことなら、シエスタに話す前に……、  [voice 7142]
        voice "ch10_l_001"
        l "I see. / In that case, before talking to Siesta… {#ch10_l_001}"
        # JA[7142]: ルイズ：なるほどね。 / そういうことなら、シエスタに話す前に……、
        # [SPRITE lay1 image=+335 → l 1 sad]
        $ show_sprites(("s 1", "l 1 sad"))
        # ルイズ：オールド・オスマンや、ミスタ・コルベールに、 / 相談してみたらどうかしら？  [voice 7143]
        voice "ch10_l_002"
        l "Why not consult Old Osmond / or Mr. Colbert? {#ch10_l_002}"
        # JA[7143]: ルイズ：オールド・オスマンや、ミスタ・コルベールに、 / 相談してみたらどうかしら？
        # [SPRITE lay1 image=+302 → l 1]
        $ show_sprites(("s 1", "l 1"))
        # ルイズ：シエスタは学院のメイドなんだし、 / 許可はもらっておいたほうがいいわ。  [voice 7144]
        voice "ch10_l_003"
        l "Siesta is a maid at the academy, / so we should get permission first. {#ch10_l_003}"
        # JA[7144]: ルイズ：シエスタは学院のメイドなんだし、 / 許可はもらっておいたほうがいいわ。
        # [SPRITE lay5 image=+392 → s 1]
        $ show_sprites(("s 1", "l 1"))
        # サイト：んじゃ、すぐ行こう！ / 善は急げってね！  [voice 13150]
        voice "ch10_s_019"
        s "Then let's go now! / Strike while the iron's hot! {#ch10_s_019}"
        # JA[13150]: サイト：んじゃ、すぐ行こう！ / 善は急げってね！
        # [SPRITE lay1 hide] [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("s 1", "h 2"))
        # ハルナ：う、うん。  [voice 2480]
        voice "ch10_h_026"
        h "Y-yeah. {#ch10_h_026}"
        # JA[2480]: ハルナ：う、うん。
        # [BGM bgm stop=1000] → fadeout
        stop music fadeout 1.0
        # [SPRITE lay5 hide] [SPRITE lay7 hide] [BG stage hide]
        $ show_sprites()
        # [BG stage image=+29] [TRANS trans("crossfade", 1000)]
        # [BGM bgm play=+32 → t31]
        # [SPRITE lay10 image=+918 → o 1]
        play music t31 fadein 1.0
        $ fade_fx("council_room")
        $ show_sprites(("o 1"))
        # オスマン：ふむふむ。 / 自活のために仕事を覚えたいと……。  [voice 4500]
        voice "ch10_o_001"
        o "Mmm-hmm. / You want to learn a job to support yourself… {#ch10_o_001}"
        # JA[4500]: オスマン：ふむふむ。 / 自活のために仕事を覚えたいと……。
        # [SPRITE lay10 x=224, y=0]
        # [SPRITE lay7 image=+955 → h 2 happy]
        $ show_sprites(("o 1", "h 2 happy"))
        # ハルナ：は、はいっ！  [voice 2481]
        voice "ch10_h_027"
        h "Y-yes! {#ch10_h_027}"
        # JA[2481]: ハルナ：は、はいっ！
        # [SPRITE lay7 hide] [SPRITE lay1 image=+302 → l 1]
        $ show_sprites(("o 1", "l 1"))
        # ルイズ：オールド・オスマン。 / わたしからもお願いします。 / どうかご一考いただけませんか？  [voice 7145]
        voice "ch10_l_004"
        l "Old Osmond. / From me as well, please. / Could you give it some thought? {#ch10_l_004}"
        # JA[7145]: ルイズ：オールド・オスマン。 / わたしからもお願いします。 / どうかご一考いただけませんか？
        # [SPRITE lay1 hide] [SPRITE lay9 image=+931 → c 1]
        $ show_sprites(("o 1", "c 1"))
        # コルベール：素晴らしい！ / 実に立派な心がけではありませんか！  [voice 1201]
        voice "ch10_c_001"
        c "Wonderful! / Isn't that a truly admirable attitude! {#ch10_c_001}"
        # JA[1201]: コルベール：素晴らしい！ / 実に立派な心がけではありませんか！
        # [SPRITE lay9 image=+929 → c 1 sad]
        $ show_sprites(("o 1", "c 1 sad"))
        # コルベール：まずは、ミス・ヴァリエールやサイトくんの / 言う通り、メイドの見習いから始めるのが / よいかもしれませんね。  [voice 1202]
        voice "ch10_c_002"
        c "First, as Miss Vallière and Saito-kun say, / it might be best to start as a maid apprentice. {#ch10_c_002}"
        # JA[1202]: コルベール：まずは、ミス・ヴァリエールやサイトくんの / 言う通り、メイドの見習いから始めるのが / よいかもしれませんね。
        # オスマン：そうじゃな。 / コルベール君。 / 手続きは、君に任せる。  [voice 4501]
        voice "ch10_o_002"
        o "Indeed. / Colbert. / I'll leave the procedures to you. {#ch10_o_002}"
        # JA[4501]: オスマン：そうじゃな。 / コルベール君。 / 手続きは、君に任せる。
        # [SPRITE lay9 hide] [SPRITE lay7 image=+953 → h 2 happy]
        $ show_sprites(("o 1", "h 2 happy"))
        # ハルナ：ありがとうございますっ！ / コルベール先生！ / 学院長！  [voice 2482]
        voice "ch10_h_028"
        h "Thank you very much! / Mr. Colbert! / Headmaster! {#ch10_h_028}"
        # JA[2482]: ハルナ：ありがとうございますっ！ / コルベール先生！ / 学院長！
        # [SPRITE lay10 image=+920 → o 1 happy]
        $ show_sprites(("o 1 happy", "h 2 happy"))
        # オスマン：ほっほっほ……。  [voice 4502]
        voice "ch10_o_003"
        o "Hohoho… {#ch10_o_003}"
        # JA[4502]: オスマン：ほっほっほ……。
        # [SPRITE lay10 image=+924 → o 1]
        $ show_sprites(("o 1", "h 2 happy"))
        # オスマン：しかし、惜しいのう。  [voice 4503]
        voice "ch10_o_004"
        o "However, what a shame. {#ch10_o_004}"
        # JA[4503]: オスマン：しかし、惜しいのう。
        # [SPRITE lay7 hide] [SPRITE lay5 image=+390 → s 1]
        $ show_sprites(("o 1", "s 1"))
        # サイト：どうかしたんですか？ / 学院長？  [voice 13151]
        voice "ch10_s_020"
        s "Is something wrong, / Headmaster? {#ch10_s_020}"
        # JA[13151]: サイト：どうかしたんですか？ / 学院長？
        # [SPRITE lay10 image=+926 → o 1 sad]
        $ show_sprites(("o 1 sad", "s 1"))
        # オスマン：メイド服を用意できたらと思ったんじゃが。  [voice 4504]
        voice "ch10_o_005"
        o "I thought I could prepare a maid outfit. {#ch10_o_005}"
        # JA[4504]: オスマン：メイド服を用意できたらと思ったんじゃが。
        # [SPRITE lay10 image=+924 → o 1]
        $ show_sprites(("o 1", "s 1"))
        # オスマン：最近メイド服が不足気味でのう。 / ハルナくんのメイド姿は当分見られないの / じゃよ。  [voice 4505]
        voice "ch10_o_006"
        o "Maid outfits have been in short supply lately. / You won't see Haruna-kun in a maid outfit / for a while. {#ch10_o_006}"
        # JA[4505]: オスマン：最近メイド服が不足気味でのう。 / ハルナくんのメイド姿は当分見られないの / じゃよ。
        # [SPRITE lay5 hide] [SPRITE lay1 image=+308 → l 1 sad]
        $ show_sprites(("o 1", "l 1 sad"))
        # ルイズ：……。  [voice 7146]
        voice "ch10_l_005"
        l "…{#ch10_l_005}"
        # JA[7146]: ルイズ：……。
        # コルベール：……。
        c "…{#ch10_c_003}"
        # JA[null]: コルベール：……。
        # [SPRITE lay10 hide] [SPRITE lay9 image=+935 → c 1]
        $ show_sprites(("c 1", "l 1 sad"))
        # コルベール：……。
        # [SPRITE lay1 hide] [SPRITE lay7 image=+957 → h 2 sad]
        $ show_sprites(("c 1", "h 2 sad"))
        # ハルナ：あは、あははは。  [voice 2483]
        voice "ch10_h_029"
        h "Ah, ahaha. {#ch10_h_029}"
        # JA[2483]: ハルナ：あは、あははは。
        # [SPRITE lay7 hide] [SPRITE lay9 hide] [SPRITE lay5 image=+396 → s 1]
        $ show_sprites(("s 1"))
        # サイト：（……学院長、相変わらず飛ばしてるなあ）
        s "(…The Headmaster is still skipping ahead as always){#ch10_s_021}"
        # JA[null]: サイト：（……学院長、相変わらず飛ばしてるなあ）
        # サイト：（春奈にメイド服か……）
        s "(A maid outfit for Haruna…){#ch10_s_022}"
        # JA[null]: サイト：（春奈にメイド服か……）
        # 【選択肢】俺はがっかりだ → scene 437
        # 【選択肢】がっかりなんてしてないぞ → scene 438
        # 【選択肢】……オスマン先生、男だぜ → scene 439
        menu:
            "I'm disappointed {#ch10_choice_004}":
                jump ch10_437
            "I'm not disappointed {#ch10_choice_005}":
                jump ch10_438
            "…Mr. Osmond, you're a man {#ch10_choice_006}":
                jump ch10_439


    # ==== SCENE 437 ====
    # [SPRITE lay5 image=+390 → s 1]
    # [BGM bgm play=+32 → t31]
    # [BG stage image=+29] [SPRITE lay5 image=+394 → s 1 angry]
    label ch10_437:
        $ show_sprites(("s 1"))
        play music t31 fadein 1.0
        $ fade_fx("council_room")
        $ show_sprites(("s 1 angry"))
        # サイト：（……ちくしょう、学院長！ / なんで肝心な時に不足してるんだよ！ / 普通は余分に用意しておくだろう！）
        s "(…Damn it, Headmaster! / Why is it lacking at the crucial moment! / Normally you'd prepare extra!){#ch10_s_023}"
        # JA[null]: サイト：（……ちくしょう、学院長！ / なんで肝心な時に不足してるんだよ！ / 普通は余分に用意しておくだろう！）
        # [SPRITE lay5 image=+396 → s 1 sad]
        $ show_sprites(("s 1 sad"))
        # サイト：（なんで、肝心なときにファンタジー要素が / 薄いんだよ）
        s "(Why is the fantasy element / so thin at the crucial moment){#ch10_s_024}"
        # JA[null]: サイト：（なんで、肝心なときにファンタジー要素が / 薄いんだよ）
        # [SE se1 stop=1] — не переносится
        # [BGM bgm stop=1000] → fadeout
        stop music fadeout 1.0
        # [SPRITE lay5 hide] [BG stage hide]
        $ show_sprites()
        # → next scene 441
        jump ch10_441


    # ==== SCENE 438 ====
    # [SPRITE lay5 image=+390 → s 1]
    # [BGM bgm play=+32 → t31]
    # [BG stage image=+29] [SPRITE lay5 image=+396 → s 1]
    label ch10_438:
        $ show_sprites(("s 1"))
        play music t31 fadein 1.0
        $ fade_fx("council_room")
        $ show_sprites(("s 1"))
        # サイト：……。
        s "…{#ch10_s_025}"
        # JA[null]: サイト：……。
        # [SPRITE lay5 x=224, y=0] [SPRITE lay7 image=+957 → h 2 sad]
        $ show_sprites(("s 1", "h 2 sad"))
        # ハルナ：平賀くん？ / どうしたの？ / 残念そうな顔をして。  [voice 2484]
        voice "ch10_h_030"
        h "Hiraga-kun? / What's wrong? / You look disappointed. {#ch10_h_030}"
        # JA[2484]: ハルナ：平賀くん？ / どうしたの？ / 残念そうな顔をして。
        # [SPRITE lay5 image=+394 → s 1 angry]
        $ show_sprites(("s 1 angry", "h 2 sad"))
        # サイト：べ、別に俺はがっかりなんかしてないぞ。 / ホ、ホントだぞ！  [voice 13152]
        voice "ch10_s_026"
        s "I-I'm not disappointed. / I-I really mean it! {#ch10_s_026}"
        # JA[13152]: サイト：べ、別に俺はがっかりなんかしてないぞ。 / ホ、ホントだぞ！
        # [SPRITE lay7 hide] [SPRITE lay1 image=+302 → l 1]
        $ show_sprites(("s 1 angry", "l 1"))
        # ルイズ：ふーん。  [voice 7147]
        voice "ch10_l_006"
        l "Hmph. {#ch10_l_006}"
        # JA[7147]: ルイズ：ふーん。
        # [SE se1 stop=1] — не переносится
        # [BGM bgm stop=1000] → fadeout
        stop music fadeout 1.0
        # [SPRITE lay5 hide] [SPRITE lay1 hide] [BG stage hide]
        $ show_sprites()
        # → next scene 441
        jump ch10_441


    # ==== SCENE 439 ====
    # [SPRITE lay5 image=+390 → s 1]
    # [BGM bgm play=+32 → t31]
    # [BG stage image=+29] [SPRITE lay5 image=+394 → s 1 angry]
    label ch10_439:
        $ show_sprites(("s 1"))
        play music t31 fadein 1.0
        $ fade_fx("council_room")
        $ show_sprites(("s 1 angry"))
        # サイト：（このじいさん……男だぜ……。 / メイド服への愛。 / こいつは本物だ！）
        s "(This old man… he's a man, alright… / Love for maid outfits. / He's the real deal!){#ch10_s_027}"
        # JA[null]: サイト：（このじいさん……男だぜ……。 / メイド服への愛。 / こいつは本物だ！）
        # [SPRITE lay5 x=224, y=0] [SPRITE lay1 image=+308 → l 1 sad]
        $ show_sprites(("s 1 angry", "l 1 sad"))
        # ルイズ：なぜかしら？ / オールド・オスマンから、サイトと同じ / 雰囲気を感じるわ。  [voice 7148]
        voice "ch10_l_007"
        l "Why do you say that? / I sense the same aura from you / as from Old Osmond. {#ch10_l_007}"
        # JA[7148]: ルイズ：なぜかしら？ / オールド・オスマンから、サイトと同じ / 雰囲気を感じるわ。
        # [SPRITE lay5 hide] [SPRITE lay7 image=+957 → h 2 sad]
        $ show_sprites(("s 1 angry", "h 2 sad"))
        # ハルナ：男の人ってみんなこうなのかしら。  [voice 2485]
        voice "ch10_h_031"
        h "Are all men like this? {#ch10_h_031}"
        # JA[2485]: ハルナ：男の人ってみんなこうなのかしら。
        # [SPRITE lay1 image=+302 → l 1]
        $ show_sprites(("s 1 angry", "h 2 sad", "l 1"))
        # ルイズ：この２人だけよ。 / 間違いなく。  [voice 7149]
        voice "ch10_l_008"
        l "Just those two. / Without a doubt. {#ch10_l_008}"
        # JA[7149]: ルイズ：この２人だけよ。 / 間違いなく。
        # [SE se1 stop=1] — не переносится
        # [BGM bgm stop=1000] → fadeout
        stop music fadeout 1.0
        # [SPRITE lay7 hide] [SPRITE lay1 hide] [BG stage hide]
        $ show_sprites()
        # → next scene 441
        jump ch10_441


    # ==== SCENE 440 ====
    # [SPRITE lay5 image=+396 → s 1]
    # [BGM bgm play=+32 → t31]
    # [BG stage image=+29]
    # [SE se1 stop=1] [BGM bgm stop=1000] [SPRITE lay5 hide] [BG stage hide]
    # → next scene 441
    label ch10_440:
        $ show_sprites(("s 1"))
        play music t31 fadein 1.0
        $ fade_fx("council_room")
        stop music fadeout 1.0
        $ show_sprites()
        # → next scene 441
        jump ch10_441


    # ==== SCENE 441 ====
    # [BG stage image=+20] [TRANS trans("crossfade", 1000)]
    # [BGM bgm play=+19 → t18]
    # [SPRITE lay7 image=+953 → h 2 happy]
    label ch10_441:
        $ fade_fx("corridor")
        play music t18 fadein 1.0
        $ show_sprites(("h 2 happy"))
        # ハルナ：さて、と！ / 準備完了！  [voice 2486]
        voice "ch10_h_032"
        h "Alright then! / Ready! {#ch10_h_032}"
        # JA[2486]: ハルナ：さて、と！ / 準備完了！
        # [SPRITE lay7 x=-96, y=0]
        # [SPRITE lay5 image=+396 → s 1]
        $ show_sprites(("s 1", "h 2 happy"))
        # サイト：結局、いつもの制服なんだ。 / 学院長……恨むぜ……。  [voice 13153]
        voice "ch10_s_028"
        s "In the end, it's the usual uniform. / Headmaster… I'll hold a grudge… {#ch10_s_028}"
        # JA[13153]: サイト：結局、いつもの制服なんだ。 / 学院長……恨むぜ……。
        # [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("s 1", "h 2"))
        # ハルナ：あら、平賀くん……。 / もしかして、残念だった？  [voice 2487]
        voice "ch10_h_033"
        h "Oh, Hiraga-kun… / Were you disappointed, maybe? {#ch10_h_033}"
        # JA[2487]: ハルナ：あら、平賀くん……。 / もしかして、残念だった？
        # [SPRITE lay5 image=+425 → s 1 sad]
        $ show_sprites(("s 1 sad", "h 2"))
        # サイト：ハハハ。 / 一体、なんのことやら。  [voice 13154]
        voice "ch10_s_029"
        s "Hahaha. / What could you mean? {#ch10_s_029}"
        # JA[13154]: サイト：ハハハ。 / 一体、なんのことやら。
        # [SPRITE lay7 hide] [SPRITE lay5 hide]
        # [SPRITE lay2 image=+489 → si 1]
        $ show_sprites(("si 1"))
        # シエスタ：ハルナさん、準備はできましたか？  [voice 15078]
        voice "ch10_si_001"
        si "Haruna-san, are you ready? {#ch10_si_001}"
        # JA[15078]: シエスタ：ハルナさん、準備はできましたか？
        # [SPRITE lay2 x=224, y=0]
        # [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("si 1", "h 2"))
        # ハルナ：ええ、大丈夫です。  [voice 2488]
        voice "ch10_h_034"
        h "Yes, I'm fine. {#ch10_h_034}"
        # JA[2488]: ハルナ：ええ、大丈夫です。
        # [SPRITE lay7 hide] [SPRITE lay5 image=+429 → s 1 sad]
        $ show_sprites(("si 1", "s 1 sad"))
        # サイト：悪いな、シエスタ。 / 自分の仕事もあるのに。  [voice 13155]
        voice "ch10_s_030"
        s "Sorry, Siesta. / Even though you have your own work. {#ch10_s_030}"
        # JA[13155]: サイト：悪いな、シエスタ。 / 自分の仕事もあるのに。
        # シエスタ：いえ、全然構わないですよ。 / それに……、  [voice 15079]
        voice "ch10_si_002"
        si "No, it's not a problem at all. / Besides… {#ch10_si_002}"
        # JA[15079]: シエスタ：いえ、全然構わないですよ。 / それに……、
        # [SPRITE lay2 image=+491 → si 1 happy]
        $ show_sprites(("si 1 happy", "s 1 sad"))
        # シエスタ：ハルナさんからメイドの勉強をしたいって / 聞いて、わたしも嬉しかったんです。 / だから一緒に頑張りましょ、ハルナさん！  [voice 15080]
        voice "ch10_si_003"
        si "I was happy to hear that you want to / learn to be a maid from me. / So let's do our best together, Haruna-san! {#ch10_si_003}"
        # JA[15080]: シエスタ：ハルナさんからメイドの勉強をしたいって / 聞いて、わたしも嬉しかったんです。 / だから一緒に頑張りましょ、ハルナさん！
        # [SPRITE lay5 hide] [SPRITE lay7 image=+953 → h 2 happy]
        $ show_sprites(("si 1 happy", "h 2 happy"))
        # ハルナ：ええ！ / よろしくお願いしますね、シエスタさん。  [voice 2489]
        voice "ch10_h_035"
        h "Yes! / I'm counting on you, Siesta-san. {#ch10_h_035}"
        # JA[2489]: ハルナ：ええ！ / よろしくお願いしますね、シエスタさん。
        # シエスタ：びしびし行きますからね！ / うふふ。  [voice 15081]
        voice "ch10_si_004"
        si "I'll do my best! / Ufufu. {#ch10_si_004}"
        # JA[15081]: シエスタ：びしびし行きますからね！ / うふふ。
        # [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("si 1 happy", "h 2"))
        # ハルナ：望むとこです。  [voice 2490]
        voice "ch10_h_036"
        h "That's what I'm hoping for. {#ch10_h_036}"
        # JA[2490]: ハルナ：望むとこです。
        # サイト：（……美しい。 / 女同士の友情成立の瞬間ってやつか……）
        s "(…Beautiful. / Is this the moment a friendship between women is formed?){#ch10_s_031}"
        # JA[null]: サイト：（……美しい。 / 女同士の友情成立の瞬間ってやつか……）
        # [SPRITE lay2 image=+489 → si 1]
        $ show_sprites(("si 1", "h 2"))
        # シエスタ：それじゃ、厨房の手伝いから始めましょうか。  [voice 15082]
        voice "ch10_si_005"
        si "Then let's start with helping in the kitchen. {#ch10_si_005}"
        # JA[15082]: シエスタ：それじゃ、厨房の手伝いから始めましょうか。
        # ハルナ：はーい。  [voice 2491]
        voice "ch10_h_037"
        h "Yes! {#ch10_h_037}"
        # JA[2491]: ハルナ：はーい。
        # [SPRITE lay7 hide] [SPRITE lay2 hide] [SPRITE lay5 hide] [BG stage hide]
        $ show_sprites()
        # [BG stage image=+32] [TRANS trans("crossfade", 1000)]
        # [SPRITE lay2 image=+489 → si 1] [SPRITE lay7 image=+951 → h 2]
        $ fade_fx("kitchen")
        $ show_sprites(("si 1", "h 2"))
        # シエスタ：まずは簡単なところから……。 / そうですね、イモの皮剥きから / やってみてください。  [voice 15083]
        voice "ch10_si_006"
        si "Let's start with something easy… / How about peeling potatoes first? {#ch10_si_006}"
        # JA[15083]: シエスタ：まずは簡単なところから……。 / そうですね、イモの皮剥きから / やってみてください。
        # シエスタ：皮が残ったままだったりすると、 / 貴族の方から苦情が来ることがありますから、 / 気をつけてくださいね。  [voice 15084]
        voice "ch10_si_007"
        si "If the skin is left on, / the nobles might complain, / so please be careful. {#ch10_si_007}"
        # JA[15084]: シエスタ：皮が残ったままだったりすると、 / 貴族の方から苦情が来ることがありますから、 / 気をつけてくださいね。
        # [SPRITE lay7 image=+953 → h 2 happy]
        $ show_sprites(("si 1", "h 2 happy"))
        # ハルナ：分かりました。 / 任せてください！  [voice 2492]
        voice "ch10_h_038"
        h "Understood. / Leave it to me! {#ch10_h_038}"
        # JA[2492]: ハルナ：分かりました。 / 任せてください！
        # シエスタ：わたし、向こうで自分の仕事をしてますから、 / 少しの間、お願いしますね。 / 何かあったら、呼んでください。  [voice 15085]
        voice "ch10_si_008"
        si "I have my own work over there, / so please handle this for a while. / If anything happens, call me. {#ch10_si_008}"
        # JA[15085]: シエスタ：わたし、向こうで自分の仕事をしてますから、 / 少しの間、お願いしますね。 / 何かあったら、呼んでください。
        # [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("si 1", "h 2"))
        # ハルナ：はーい。  [voice 2493]
        voice "ch10_h_039"
        h "Yes! {#ch10_h_039}"
        # JA[2493]: ハルナ：はーい。
        # [SPRITE lay2 hide] [SPRITE lay5 image=+390 → s 1]
        $ show_sprites(("s 1"))
        # サイト：俺もちょっとルイズの服の洗濯をしてくるよ。 / また、終わる頃に来るから。 / 頑張れよ、春奈。  [voice 13156]
        voice "ch10_s_032"
        s "I'll go wash Louise's clothes too. / I'll come back when I'm done. / Do your best, Haruna. {#ch10_s_032}"
        # JA[13156]: サイト：俺もちょっとルイズの服の洗濯をしてくるよ。 / また、終わる頃に来るから。 / 頑張れよ、春奈。
        # [SPRITE lay7 image=+953 → h 2 happy]
        $ show_sprites(("s 1", "h 2 happy"))
        # ハルナ：平賀くん、いろいろありがとね。  [voice 2494]
        voice "ch10_h_040"
        h "Thanks for everything, Hiraga-kun. {#ch10_h_040}"
        # JA[2494]: ハルナ：平賀くん、いろいろありがとね。
        # [SPRITE lay5 image=+423 → s 1 sad]
        $ show_sprites(("s 1 sad", "h 2 happy"))
        # サイト：なーに、いいって。 / じゃ、後で。  [voice 13157]
        voice "ch10_s_033"
        s "What? No problem. / See you later. {#ch10_s_033}"
        # JA[13157]: サイト：なーに、いいって。 / じゃ、後で。
        # [SPRITE lay7 hide] [SPRITE lay5 hide] [BG stage hide]
        $ show_sprites()
        # [BG stage image=+88] [TRANS trans("crossfade", 1000)]
        # null：………。 / ……。 / …。
        $ fade_fx("sky")
        # サイト：（ふぅ、やっと干し終わった……。 / 春奈の方もそろそろ終わってるかな？ / ちょっと、行ってみるか）
        s "(Phew, finally done hanging the laundry… / I wonder if Haruna's done too? / Let me go check.){#ch10_s_034}"
        # JA[null]: サイト：（ふぅ、やっと干し終わった……。 / 春奈の方もそろそろ終わってるかな？ / ちょっと、行ってみるか）
        # [SPRITE lay5 hide] [BG stage hide]
        $ show_sprites()
        # [BG stage image=+32] [TRANS trans("crossfade", 1000)]
        # [SPRITE lay2 image=+489 → si 1] [SPRITE lay7 image=+951 → h 2]
        $ fade_fx("kitchen")
        $ show_sprites(("si 1", "h 2"))
        # サイト：（ん、シエスタも戻ってきたとこみたいだな）
        s "(Hm, looks like Siesta is back too.){#ch10_s_035}"
        # JA[null]: サイト：（ん、シエスタも戻ってきたとこみたいだな）
        # シエスタ：ハルナさん、どうですか？  [voice 15086]
        voice "ch10_si_009"
        si "How's it going, Haruna-san? {#ch10_si_009}"
        # JA[15086]: シエスタ：ハルナさん、どうですか？
        # ハルナ：ふふふ。 / 私、皮剥きの天才かもしれません。  [voice 2495]
        voice "ch10_h_041"
        h "Fufufu. / I might be a genius at peeling. {#ch10_h_041}"
        # JA[2495]: ハルナ：ふふふ。 / 私、皮剥きの天才かもしれません。
        # サイト：（応用利かない天才だよな、それ。 / でも、うまくことできたみたいだ。 / 心配することもなかったかな？）
        s "(A genius that can't be applied, that one. / But it seems to have gone well. / Nothing to worry about?){#ch10_s_036}"
        # JA[null]: サイト：（応用利かない天才だよな、それ。 / でも、うまくことできたみたいだ。 / 心配することもなかったかな？）
        # [SPRITE lay2 image=+491 → si 1 happy]
        $ show_sprites(("si 1 happy", "h 2"))
        # シエスタ：まあ。 / そんなに上手にできたんですか？ / メイドさんの才能あり、かもですよ？  [voice 15087]
        voice "ch10_si_010"
        si "Well. / Did you do it that well? / You might have talent as a maid? {#ch10_si_010}"
        # JA[15087]: シエスタ：まあ。 / そんなに上手にできたんですか？ / メイドさんの才能あり、かもですよ？
        # [SPRITE lay7 image=+953 → h 2 happy]
        $ show_sprites(("si 1 happy", "h 2 happy"))
        # ハルナ：えへへ、じゃーん。 / ほら、見て見て！ / こんなにキレイに剥けたんですよ！  [voice 2496]
        voice "ch10_h_042"
        h "Ehehe, look! / Look, look! / I peeled it this beautifully! {#ch10_h_042}"
        # JA[2496]: ハルナ：えへへ、じゃーん。 / ほら、見て見て！ / こんなにキレイに剥けたんですよ！
        # シエスタ：どれどれ……。 / うん、合格ですっ！  [voice 15088]
        voice "ch10_si_011"
        si "Let me see… / Yup, you pass! {#ch10_si_011}"
        # JA[15088]: シエスタ：どれどれ……。 / うん、合格ですっ！
        # ハルナ：やったぁ！  [voice 2497]
        voice "ch10_h_043"
        h "Yay! {#ch10_h_043}"
        # JA[2497]: ハルナ：やったぁ！
        # サイト：（そうかそうか。 / 春奈もちゃんとできるんだなぁ）
        s "(I see, I see. / Haruna can do it properly after all.){#ch10_s_037}"
        # JA[null]: サイト：（そうかそうか。 / 春奈もちゃんとできるんだなぁ）
        # [SPRITE lay2 image=+493 → si 1]
        $ show_sprites(("si 1", "h 2 happy"))
        # シエスタ：これなら心配ありませんね……って、あら？  [voice 15089]
        voice "ch10_si_012"
        si "No need to worry about that… wait, oh? {#ch10_si_012}"
        # JA[15089]: シエスタ：これなら心配ありませんね……って、あら？
        # [SPRITE lay2 image=+495 → si 1 sad]
        $ show_sprites(("si 1 sad", "h 2 happy"))
        # シエスタ：ええと……。 / カゴが空っぽですけど、 / もしかして、これ……ひとつだけ？  [voice 15090]
        voice "ch10_si_013"
        si "Um… / The basket is empty, but / could it be… just one? {#ch10_si_013}"
        # JA[15090]: シエスタ：ええと……。 / カゴが空っぽですけど、 / もしかして、これ……ひとつだけ？
        # サイト：（え？）
        s "(Huh?){#ch10_s_038}"
        # JA[null]: サイト：（え？）
        # [SPRITE lay7 image=+957 → h 2 sad]
        $ show_sprites(("si 1 sad", "h 2 sad"))
        # ハルナ：え、ええ。 / 意外と、皮がキレイにとれなくて……。  [voice 2498]
        voice "ch10_h_044"
        h "E-eh. / Surprisingly, the skin doesn't come off cleanly… {#ch10_h_044}"
        # JA[2498]: ハルナ：え、ええ。 / 意外と、皮がキレイにとれなくて……。
        # サイト：（……始めてから、３０分くらい経ったよな？ / それで１個だけって……）
        s "(…It's been about 30 minutes since we started, right? / And only one potato…){#ch10_s_039}"
        # JA[null]: サイト：（……始めてから、３０分くらい経ったよな？ / それで１個だけって……）
        # [SPRITE lay2 image=+489 → si 1]
        $ show_sprites(("si 1", "h 2 sad"))
        # シエスタ：と、とってもキレイに剥けてて、 / それはすごいと思います。  [voice 15091]
        voice "ch10_si_014"
        si "It's, it's peeled very beautifully, / I think that's amazing. {#ch10_si_014}"
        # JA[15091]: シエスタ：と、とってもキレイに剥けてて、 / それはすごいと思います。
        # [SPRITE lay2 image=+495 → si 1 sad]
        $ show_sprites(("si 1 sad", "h 2 sad"))
        # シエスタ：でも、お料理はたくさん作りますから、 / 速さと量も大事なんですよ。  [voice 15092]
        voice "ch10_si_015"
        si "But we cook a lot, / so speed and quantity matter too. {#ch10_si_015}"
        # JA[15092]: シエスタ：でも、お料理はたくさん作りますから、 / 速さと量も大事なんですよ。
        # [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("si 1 sad", "h 2"))
        # ハルナ：そ、そうですよね……。 / キレイに剥きつつ、速さと量ですね！ / 分かりました、今度は頑張ります。  [voice 2499]
        voice "ch10_h_045"
        h "Y-yes… / Beautiful peeling, plus speed and quantity! / Got it, I'll do better next time. {#ch10_h_045}"
        # JA[2499]: ハルナ：そ、そうですよね……。 / キレイに剥きつつ、速さと量ですね！ / 分かりました、今度は頑張ります。
        # [SPRITE lay2 image=+493 → si 1]
        $ show_sprites(("si 1", "h 2"))
        # シエスタ：きゃあっ！ / ハルナさん、そのナイフの使い方、危ないです！ / やめてください。  [voice 15093]
        voice "ch10_si_016"
        si "Kyaa! / Haruna-san, that knife handling is dangerous! / Please stop. {#ch10_si_016}"
        # JA[15093]: シエスタ：きゃあっ！ / ハルナさん、そのナイフの使い方、危ないです！ / やめてください。
        # ハルナ：え、そうなんですか？  [voice 2500]
        voice "ch10_h_046"
        h "Eh, is that so? {#ch10_h_046}"
        # JA[2500]: ハルナ：え、そうなんですか？
        # [SPRITE lay2 image=+495 → si 1 sad]
        $ show_sprites(("si 1 sad", "h 2"))
        # シエスタ：も、もしかして、ハルナさん、 / ナイフを使ったことないんですか？  [voice 15094]
        voice "ch10_si_017"
        si "C-could it be, Haruna-san, / you've never used a knife before? {#ch10_si_017}"
        # JA[15094]: シエスタ：も、もしかして、ハルナさん、 / ナイフを使ったことないんですか？
        # [SPRITE lay7 image=+957 → h 2 sad]
        $ show_sprites(("si 1 sad", "h 2 sad"))
        # ハルナ：え、ええ……。 / ちょっと……慣れてない、です。  [voice 2501]
        voice "ch10_h_047"
        h "E-eh… / A little… I'm not used to it. {#ch10_h_047}"
        # JA[2501]: ハルナ：え、ええ……。 / ちょっと……慣れてない、です。
        # シエスタ：そ、そうですか……。  [voice 15095]
        voice "ch10_si_018"
        si "I-I see… {#ch10_si_018}"
        # JA[15095]: シエスタ：そ、そうですか……。
        # サイト：（シエスタ……すまん）
        s "(Siesta… sorry){#ch10_s_040}"
        # JA[null]: サイト：（シエスタ……すまん）
        # [SPRITE lay2 image=+489 → si 1]
        $ show_sprites(("si 1", "h 2 sad"))
        # シエスタ：ち、ちょっと厨房は早かったかもしれませんね。 / べ、別のお仕事はなかったかしら。  [voice 15096]
        voice "ch10_si_019"
        si "M-maybe the kitchen work was too soon. / I-is there any other work? {#ch10_si_019}"
        # JA[15096]: シエスタ：ち、ちょっと厨房は早かったかもしれませんね。 / べ、別のお仕事はなかったかしら。
        # [SPRITE lay7 hide] [SPRITE lay2 hide] [SPRITE lay5 hide] [BG stage hide]
        $ show_sprites()
        # [BG stage image=+20] [TRANS trans("crossfade", 1000)]
        # [SPRITE lay2 image=+489 → si 1] [SPRITE lay7 image=+951 → h 2]
        $ fade_fx("corridor")
        $ show_sprites(("si 1", "h 2"))
        # シエスタ：それでは、広間の掃除をお願いしますね。  [voice 15097]
        voice "ch10_si_020"
        si "Then, please clean the great hall. {#ch10_si_020}"
        # JA[15097]: シエスタ：それでは、広間の掃除をお願いしますね。
        # [SPRITE lay7 image=+955 → h 2 happy]
        $ show_sprites(("si 1", "h 2 happy"))
        # ハルナ：頑張りますっ！  [voice 2502]
        voice "ch10_h_048"
        h "I'll do my best! {#ch10_h_048}"
        # JA[2502]: ハルナ：頑張りますっ！
        # シエスタ：ここは、見てのとおり、 / 壊れやすい彫像とかを飾って……。  [voice 15098]
        voice "ch10_si_021"
        si "As you can see, / there are fragile statues and such… {#ch10_si_021}"
        # JA[15098]: シエスタ：ここは、見てのとおり、 / 壊れやすい彫像とかを飾って……。
        # ハルナ：では、いきます！ / それーーーっ！  [voice 2503]
        voice "ch10_h_049"
        h "Then, here I go! / Heeeere I go! {#ch10_h_049}"
        # JA[2503]: ハルナ：では、いきます！ / それーーーっ！
        # [SPRITE lay7 hide] [SPRITE lay2 image=+526 → si 1 sad]
        $ show_sprites(("si 1 sad"))
        # シエスタ：ち、ちょっと待ってください！ / まだ説明が！  [voice 15099]
        voice "ch10_si_022"
        si "W-wait! / I haven't finished explaining! {#ch10_si_022}"
        # JA[15099]: シエスタ：ち、ちょっと待ってください！ / まだ説明が！
        # サイト：（シエスタ……。 / すまん、ほんとにすまん）
        s "(Siesta… / Sorry, really sorry){#ch10_s_041}"
        # JA[null]: サイト：（シエスタ……。 / すまん、ほんとにすまん）
        # [SPRITE lay2 hide] [SPRITE lay5 hide] [BG stage hide]
        $ show_sprites()
        # [BG stage image=+26] [TRANS trans("crossfade", 1000)]
        # [SPRITE lay2 image=+495 → si 1] [SPRITE lay7 image=+951 → h 2]
        $ fade_fx("yard")
        $ show_sprites(("si 1", "h 2"))
        # シエスタ：は、ハルナさん……次はお洗濯を……。  [voice 15100]
        voice "ch10_si_023"
        si "H-Haruna-san… next is laundry… {#ch10_si_023}"
        # JA[15100]: シエスタ：は、ハルナさん……次はお洗濯を……。
        # ハルナ：……あれ？ / シエスタさん？ / 洗濯機がないんですけど？  [voice 2504]
        voice "ch10_h_050"
        h "…Hm? / Siesta-san? / There's no washing machine? {#ch10_h_050}"
        # JA[2504]: ハルナ：……あれ？ / シエスタさん？ / 洗濯機がないんですけど？
        # [SPRITE lay2 image=+489 → si 1]
        $ show_sprites(("si 1", "h 2"))
        # シエスタ：センタクキ？ / 何ですか、それ？  [voice 15101]
        voice "ch10_si_024"
        si "Washing machine? / What's that? {#ch10_si_024}"
        # JA[15101]: シエスタ：センタクキ？ / 何ですか、それ？
        # [SPRITE lay7 image=+957 → h 2 sad]
        $ show_sprites(("si 1", "h 2 sad"))
        # ハルナ：あ、そっか……。 / こっちの世界には……。  [voice 2505]
        voice "ch10_h_051"
        h "Ah, right… / In this world… {#ch10_h_051}"
        # JA[2505]: ハルナ：あ、そっか……。 / こっちの世界には……。
        # シエスタ：えーと、センタクキっていうのは無いので、 / この洗濯板や洗濯棒を使ってください。  [voice 15102]
        voice "ch10_si_025"
        si "Um, there are no washing machines here, / so please use this washboard and laundry stick. {#ch10_si_025}"
        # JA[15102]: シエスタ：えーと、センタクキっていうのは無いので、 / この洗濯板や洗濯棒を使ってください。
        # [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("si 1", "h 2"))
        # ハルナ：洗濯板？ / 洗濯棒？ / これどうやって使うのかしら……？  [voice 2506]
        voice "ch10_h_052"
        h "Washboard? / Laundry stick? / How do you use these…? {#ch10_h_052}"
        # JA[2506]: ハルナ：洗濯板？ / 洗濯棒？ / これどうやって使うのかしら……？
        # サイト：（洗濯か……）
        s "(Laundry, huh…){#ch10_s_042}"
        # JA[null]: サイト：（洗濯か……）
        # 【選択肢】手伝おう → scene 442
        # 【選択肢】もう少し様子を見てみよう → scene 443
        # 【選択肢】おいおい、大丈夫か？ → scene 444
        menu:
            "I'll help {#ch10_choice_007}":
                jump ch10_442
            "Let's watch a bit longer {#ch10_choice_008}":
                jump ch10_443
            "Hey, are you okay? {#ch10_choice_009}":
                jump ch10_444


    # ==== SCENE 442 ====
    # [SPRITE lay7 image=+951 → h 2] [SPRITE lay2 image=+489 → si 1]
    # [BGM bgm play=+19 → t18]
    # [BG stage image=+26]
    # [SPRITE lay2 hide] [SPRITE lay5 image=+390 → s 1]
    label ch10_442:
        $ show_sprites(("h 2", "si 1"))
        play music t18 fadein 1.0
        $ fade_fx("yard")
        $ show_sprites(("si 1", "s 1"))
        # サイト：どれ、洗濯だったら得意中の得意だから、 / 俺にまかせなよ。  [voice 13158]
        voice "ch10_s_043"
        s "Leave it to me, / laundry is my specialty. {#ch10_s_043}"
        # JA[13158]: サイト：どれ、洗濯だったら得意中の得意だから、 / 俺にまかせなよ。
        # [SPRITE lay7 image=+957 → h 2 sad]
        $ show_sprites(("si 1", "s 1", "h 2 sad"))
        # ハルナ：平賀くん……。 / お願い……。  [voice 2507]
        voice "ch10_h_053"
        h "Hiraga-kun… / Please… {#ch10_h_053}"
        # JA[2507]: ハルナ：平賀くん……。 / お願い……。
        # [SPRITE lay5 image=+392 → s 1 sad]
        $ show_sprites(("si 1", "s 1 sad", "h 2 sad"))
        # サイト：とりあえず、この洗濯を終わらせよう！  [voice 13159]
        voice "ch10_s_044"
        s "For now, let's finish this laundry! {#ch10_s_044}"
        # JA[13159]: サイト：とりあえず、この洗濯を終わらせよう！
        # [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("si 1", "s 1 sad", "h 2"))
        # ハルナ：うん。  [voice 2508]
        voice "ch10_h_054"
        h "Mm. {#ch10_h_054}"
        # JA[2508]: ハルナ：うん。
        # → next scene 445
        jump ch10_445


    # ==== SCENE 443 ====
    # [SPRITE lay7 image=+951 → h 2] [SPRITE lay2 image=+489 → si 1]
    # [BGM bgm play=+19 → t18]
    # [BG stage image=+26]
    # [SPRITE lay7 image=+951 → h 2]
    label ch10_443:
        $ show_sprites(("h 2", "si 1"))
        play music t18 fadein 1.0
        $ fade_fx("yard")
        $ show_sprites(("h 2"))
        # ハルナ：え、えっと、こうすればいいんですか？ / ごりごりっと。  [voice 2509]
        voice "ch10_h_055"
        h "E-um, do I do it like this? / Scrub scrub. {#ch10_h_055}"
        # JA[2509]: ハルナ：え、えっと、こうすればいいんですか？ / ごりごりっと。
        # [SPRITE lay2 image=+495 → si 1 sad]
        $ show_sprites(("si 1 sad", "h 2"))
        # シエスタ：洗濯板の上で洗濯棒を転がされても。  [voice 15103]
        voice "ch10_si_026"
        si "Even if you roll the laundry stick on the washboard. {#ch10_si_026}"
        # JA[15103]: シエスタ：洗濯板の上で洗濯棒を転がされても。
        # [SPRITE lay7 image=+957 → h 2 sad]
        $ show_sprites(("si 1 sad", "h 2 sad"))
        # ハルナ：あ、やっぱり、違うのね……。 / どうしよ……。  [voice 2510]
        voice "ch10_h_056"
        h "Ah, as expected, that's wrong… / What do I do… {#ch10_h_056}"
        # JA[2510]: ハルナ：あ、やっぱり、違うのね……。 / どうしよ……。
        # サイト：（仕方ないな、俺の出番か）
        s "(I guess it's my turn.){#ch10_s_045}"
        # JA[null]: サイト：（仕方ないな、俺の出番か）
        # [SPRITE lay2 hide] [SPRITE lay5 image=+390 → s 1]
        $ show_sprites(("s 1"))
        # サイト：そこのお嬢さん。 / 洗濯のことなら、俺に聞きな。  [voice 13160]
        voice "ch10_s_046"
        s "Young lady over there. / For laundry, ask me. {#ch10_s_046}"
        # JA[13160]: サイト：そこのお嬢さん。 / 洗濯のことなら、俺に聞きな。
        # [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("s 1", "h 2"))
        # ハルナ：ひ、平賀くん。  [voice 2511]
        voice "ch10_h_057"
        h "H-Hiraga-kun. {#ch10_h_057}"
        # JA[2511]: ハルナ：ひ、平賀くん。
        # → next scene 445
        jump ch10_445


    # ==== SCENE 444 ====
    # [SPRITE lay7 image=+951 → h 2] [SPRITE lay2 image=+489 → si 1]
    # [BGM bgm play=+19 → t18]
    # [BG stage image=+26]
    # [SPRITE lay2 hide] [SPRITE lay5 image=+396 → s 1]
    label ch10_444:
        $ show_sprites(("h 2", "si 1"))
        play music t18 fadein 1.0
        $ fade_fx("yard")
        $ show_sprites(("s 1"))
        # サイト：おいおい、大丈夫か？  [voice 13161]
        voice "ch10_s_047"
        s "Hey hey, are you okay? {#ch10_s_047}"
        # JA[13161]: サイト：おいおい、大丈夫か？
        # [SPRITE lay7 image=+955 → h 2 sad]
        $ show_sprites(("s 1", "h 2 sad"))
        # ハルナ：ひ、平賀くん！ / 見てたの？  [voice 2512]
        voice "ch10_h_058"
        h "H-Hiraga-kun! / Were you watching? {#ch10_h_058}"
        # JA[2512]: ハルナ：ひ、平賀くん！ / 見てたの？
        # [SPRITE lay5 image=+429 → s 1 sad]
        $ show_sprites(("s 1 sad", "h 2 sad"))
        # サイト：え、ええと。 / と、とりあえず洗濯を手伝うよ。  [voice 13162]
        voice "ch10_s_048"
        s "E-um. / I-I'll help with the laundry. {#ch10_s_048}"
        # JA[13162]: サイト：え、ええと。 / と、とりあえず洗濯を手伝うよ。
        # → next scene 445
        jump ch10_445


    # ==== SCENE 445 ====
    # [SPRITE lay5 image=+392 → s 1] [SPRITE lay7 image=+951 → h 2]
    # [BGM bgm play=+19 → t18]
    # [BG stage image=+26]
    # [SPRITE lay5 image=+390 → s 1]
    label ch10_445:
        $ show_sprites(("s 1", "h 2"))
        play music t18 fadein 1.0
        $ fade_fx("yard")
        $ show_sprites(("s 1"))
        # サイト：ほら、こうやってさ、 / 洗濯板の上でごしごしと洗って。  [voice 13163]
        voice "ch10_s_049"
        s "Here, like this, / scrub it on the washboard. {#ch10_s_049}"
        # JA[13163]: サイト：ほら、こうやってさ、 / 洗濯板の上でごしごしと洗って。
        # [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("s 1", "h 2"))
        # ハルナ：う、うん。  [voice 2513]
        voice "ch10_h_059"
        h "U-um. {#ch10_h_059}"
        # JA[2513]: ハルナ：う、うん。
        # [SPRITE lay5 image=+392 → s 1 sad]
        $ show_sprites(("s 1 sad", "h 2"))
        # サイト：しつこい汚れの時とかは、 / この洗濯棒でぽかぽかと叩くのさ。  [voice 13164]
        voice "ch10_s_050"
        s "For stubborn stains, / tap them with this laundry stick. {#ch10_s_050}"
        # JA[13164]: サイト：しつこい汚れの時とかは、 / この洗濯棒でぽかぽかと叩くのさ。
        # [SPRITE lay7 image=+957 → h 2 sad]
        $ show_sprites(("s 1 sad", "h 2 sad"))
        # ハルナ：そ、そうだったんだ。 / ごめんね、私、全然分かんなくて……。  [voice 2514]
        voice "ch10_h_060"
        h "S-so that's how it's done. / Sorry, I didn't understand at all… {#ch10_h_060}"
        # JA[2514]: ハルナ：そ、そうだったんだ。 / ごめんね、私、全然分かんなくて……。
        # [SPRITE lay5 image=+429 → s 1 sad]
        $ show_sprites(("s 1 sad", "h 2 sad"))
        # サイト：い、いや、謝ることじゃないよ。  [voice 13165]
        voice "ch10_s_051"
        s "N-no, you don't need to apologize. {#ch10_s_051}"
        # JA[13165]: サイト：い、いや、謝ることじゃないよ。
        # サイト：（しかし……）
        s "(But…){#ch10_s_052}"
        # JA[null]: サイト：（しかし……）
        # サイト：（まあ、洗濯は仕方ないとしても、 / 春奈がまさか、こんなに生活力がないとは）
        s "(Well, laundry is one thing, / but I never thought Haruna had so little survival skill.){#ch10_s_053}"
        # JA[null]: サイト：（まあ、洗濯は仕方ないとしても、 / 春奈がまさか、こんなに生活力がないとは）
        # [SPRITE lay5 image=+396 → s 1]
        $ show_sprites(("s 1", "h 2 sad"))
        # サイト：（なんでもできる優等生タイプだと思ってたのに / ここまで手際が悪いか、ふつー！）
        s "(I thought she was a capable model student, / but she's this clumsy. Typical!){#ch10_s_054}"
        # JA[null]: サイト：（なんでもできる優等生タイプだと思ってたのに / ここまで手際が悪いか、ふつー！）
        # ハルナ：あうう、平賀くん。 / そんな目で見ないで～～。  [voice 2515]
        voice "ch10_h_061"
        h "Auuugh, Hiraga-kun. / Don't look at me like that~~. {#ch10_h_061}"
        # JA[2515]: ハルナ：あうう、平賀くん。 / そんな目で見ないで～～。
        # [SPRITE lay5 hide] [SPRITE lay2 image=+495 → si 1]
        $ show_sprites(("si 1", "h 2 sad"))
        # シエスタ：ちょ、ちょっぴり、前途多難かもしれませんね。  [voice 15104]
        voice "ch10_si_027"
        si "It, it might be a rocky road ahead. {#ch10_si_027}"
        # JA[15104]: シエスタ：ちょ、ちょっぴり、前途多難かもしれませんね。
        # ハルナ：ごめんなさい。  [voice 2516]
        voice "ch10_h_062"
        h "I'm sorry. {#ch10_h_062}"
        # JA[2516]: ハルナ：ごめんなさい。
        # [SPRITE lay2 image=+489 → si 1]
        $ show_sprites(("si 1", "h 2 sad"))
        # シエスタ：でも、すぐ逃げ出しちゃう子も多いのに、 / ハルナさんは立派です。  [voice 15105]
        voice "ch10_si_028"
        si "But many girls run away right away, / so Haruna-san is doing great. {#ch10_si_028}"
        # JA[15105]: シエスタ：でも、すぐ逃げ出しちゃう子も多いのに、 / ハルナさんは立派です。
        # [SPRITE lay7 hide] [SPRITE lay5 image=+429 → s 1 sad]
        $ show_sprites(("si 1", "s 1 sad"))
        # サイト：そなの？  [voice 13166]
        voice "ch10_s_055"
        s "Is that so? {#ch10_s_055}"
        # JA[13166]: サイト：そなの？
        # シエスタ：ええ。 / こう見えて、結構メイドって大変なんですよ？  [voice 15106]
        voice "ch10_si_029"
        si "Yes. / Believe it or not, being a maid is quite hard. {#ch10_si_029}"
        # JA[15106]: シエスタ：ええ。 / こう見えて、結構メイドって大変なんですよ？
        # [SPRITE lay5 image=+390 → s 1]
        $ show_sprites(("si 1", "s 1"))
        # サイト：うむ。 / それはよく分かる。 / ルイズの世話だけでぼろぼろだしな、俺。  [voice 13167]
        voice "ch10_s_056"
        s "Mmm. / I know that well. / Taking care of Louise alone wears me out. {#ch10_s_056}"
        # JA[13167]: サイト：うむ。 / それはよく分かる。 / ルイズの世話だけでぼろぼろだしな、俺。
        # [SPRITE lay2 image=+495 → si 1]
        $ show_sprites(("si 1", "s 1"))
        # シエスタ：ミス・ヴァリエールは、また違う大変かも……。  [voice 15107]
        voice "ch10_si_030"
        si "Miss Vallière might be a different kind of hard… {#ch10_si_030}"
        # JA[15107]: シエスタ：ミス・ヴァリエールは、また違う大変かも……。
        # [SPRITE lay5 image=+429 → s 1 sad]
        $ show_sprites(("si 1", "s 1 sad"))
        # サイト：え？ / そ、そう？  [voice 13168]
        voice "ch10_s_057"
        s "Huh? / R-really? {#ch10_s_057}"
        # JA[13168]: サイト：え？ / そ、そう？
        # [SPRITE lay5 hide] [SPRITE lay7 image=+951 → h 2]
        $ show_sprites(("si 1", "h 2"))
        # ハルナ：失敗は悔しいですけど、 / こうやって働くのはなんだか楽しくて。 / こういうの初めてだから……。  [voice 2517]
        voice "ch10_h_063"
        h "Failing is frustrating, / but working like this is somehow fun. / It's my first time doing this… {#ch10_h_063}"
        # JA[2517]: ハルナ：失敗は悔しいですけど、 / こうやって働くのはなんだか楽しくて。 / こういうの初めてだから……。
        # [SPRITE lay2 image=+491 → si 1 happy]
        $ show_sprites(("si 1 happy", "h 2"))
        # シエスタ：楽しいのが一番大事ですよ。 / じゃあ、お仕事続けましょうか。 / まだまだ、たくさんありますから。  [voice 15108]
        voice "ch10_si_031"
        si "Enjoying it is most important. / Now then, let's continue working. / There's still a lot to do. {#ch10_si_031}"
        # JA[15108]: シエスタ：楽しいのが一番大事ですよ。 / じゃあ、お仕事続けましょうか。 / まだまだ、たくさんありますから。
        # [SPRITE lay7 image=+953 → h 2 happy]
        $ show_sprites(("si 1 happy", "h 2 happy"))
        # ハルナ：はい！  [voice 2518]
        voice "ch10_h_064"
        h "Yes! {#ch10_h_064}"
        # JA[2518]: ハルナ：はい！
        # [SPRITE lay2 hide] [SPRITE lay5 image=+390 → s 1]
        $ show_sprites(("s 1"))
        # サイト：頑張れよ、春奈。  [voice 13169]
        voice "ch10_s_058"
        s "Do your best, Haruna. {#ch10_s_058}"
        # JA[13169]: サイト：頑張れよ、春奈。
        # [SE se1 stop=1] — не переносится
        # [BGM bgm stop=1000] → fadeout
        stop music fadeout 1.0
        # [SPRITE lay5 hide] [SPRITE lay7 hide] [BG stage hide]
        $ show_sprites()
        # → next scene 446
        jump ch10_446


    # ==== SCENE 446 ====
    # [BG stage image=+14] [TRANS trans("crossfade", 1000)]
    # [BGM bgm play=+29 → t28]
    # [SPRITE lay5 image=+396 → s 1]
    label ch10_446:
        $ fade_fx("library")
        play music t28 fadein 1.0
        $ show_sprites(("s 1"))
        # サイト：（……う～ん。 / やる気があるのはいいんだけど）
        s "(…Hmmm. / It's good that she's motivated, but…){#ch10_s_059}"
        # JA[null]: サイト：（……う～ん。 / やる気があるのはいいんだけど）
        # サイト：（春奈、ホントに大丈夫なのか？）
        s "(Haruna, is she really going to be okay?){#ch10_s_060}"
        # JA[null]: サイト：（春奈、ホントに大丈夫なのか？）
        # サイト：……。
        s "…{#ch10_s_061}"
        # JA[null]: サイト：……。
        # [SPRITE lay5 image=+390 → s 1]
        $ show_sprites(("s 1"))
        # サイト：（心配になってきた。 / ちょっと様子を見てこよう！）
        s "(I'm getting worried. / Let me go check on her!){#ch10_s_062}"
        # JA[null]: サイト：（心配になってきた。 / ちょっと様子を見てこよう！）
        # [SE se1 stop=1] — не переносится
        # [BGM bgm stop=1000] → fadeout
        stop music fadeout 1.0
        # [SPRITE lay5 hide] [BG stage hide]
        $ show_sprites()
        # 【移動】図書館 → scene 588  ((0x01000000 +1449))
        # 【移動】学院長室 → scene 918  ((0x01000000 +1454))
        # 【移動】厨房 → scene 489  ((0x01000000 +1459))
        # 【移動】廊下 → scene 676  ((0x01000000 +1464))
        # → jump attention (конец части 1)
        jump attention
        return