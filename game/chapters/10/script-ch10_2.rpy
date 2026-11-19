# Глава 10, часть 2 (сцены 451-466): «Внезапный скаут» — переездСиесты, свидание, finais.
# Источник: ps2_source/chapters/chapter_11_突然のスカウト.txt (SCENE 451-466).
# Точные аргументы: ps2_source/events_full/chapter_11_突然のスカウト.txt.
#
# Голоса: 121 (сцены 451-466). Нумерация ch10_<spk>_<NNN> — с 001 по говорящему.
#   s: 13170-13215
#   h: 2519-2558  (Haruna, var ha)
#   si: 15109-15119
#   l: 7150-7159
#   o: 4506-4510
#   c: 1203
#   w: 16073-16080
#   k: 3813
#   m: 4157
#   t: (no voice, Tabitha ellipsis)
# PS2 voice IDs: s=13170..13215; h=2519..2558; si=15109..15119; l=7150..7159;
#   o=4506..4510; c=1203; w=16073..16080; k=3813; m=4157.
# Спрайты: id → имя по references/sprite_id_map.csv; PROVISIONAL для не подтверждённых.
# Фоны: id(12)=classroom2, id(11)=classroom, id(90)=nightsky, id(28)=courtyard,
#   id(23)=corridor, id(29)=council_room, id(26)=yard, id(19)=dorm, id(88)=sky.
# CG: id(273)=ha_moon — сцена с двумя лунами.
# BGM: bgm play=+19→t18, +17→t16, +20→t19, +32→t31 — все есть.
# SE: не переносятся (SE-заглушка, по решению проекта).
# Не переносятся: MOVIE, beginSkip/endSkip, waitSEStop/waitLoad/waitAction/waitTime.
# К обращению: по addresses.md — «мадемуазель/Ваше Высочество» для Анриетты,
#   «сан/кун» для сверстников, «сэнсэй» для учителей.

label ch10_2:
    $ tndl(None)
    # Титульный монтаж (ч.2 продолжает часть 1, новый тайтл не нужен — используется общий overlay с части 1)
    pause(0.5)

    # ==== SCENE 451 ====
    # [BG stage image=+12] [TRANS trans("crossfade", 1000)]
    # [BGM bgm play=+19 → t18]
    # [SPRITE lay2 image=+491 → si 1]
    # [SPRITE lay1 image=+302 → l 1]
    label ch10_451:
        $ show_sprites(("si 1", "l 1"))
        play music t18 fadein 1.0
        $ fade_fx("classroom2")
        # シエスタ：ミス・ヴァリエール。 / 短い間でしたがお世話になりました。  [voice 15109]
        voice "ch10_si_032"
        si "Miss Varière. / I was in your care for a short time. {#ch10_si_032}"
        # JA[15109]: シエスタ：ミス・ヴァリエール。 / 短い間でしたがお世話になりました。
        # シエスタ：わたしの部屋の修理が終わったようですので、 / 今日からはそちらで。  [voice 15110]
        voice "ch10_si_033"
        si "My room repairs seem finished. / From today I'll be staying there. {#ch10_si_033}"
        # JA[15110]: シエスタ：わたしの部屋の修理が終わったようですので、 / 今日からはそちらで。
        # 【選択肢】……忘れてた → scene 452
        # 【選択肢】引越しの手伝いをするよ → scene 453
        # 【選択肢】部屋が新しくなって良かったかも？ → scene 454
        menu:
            "……I forgot it. {#ch10_choice_010}":
                jump ch10_452
            "I'll help with the move. {#ch10_choice_011}":
                jump ch10_453
            "The new room is nice, isn't it? {#ch10_choice_012}":
                jump ch10_454

    # ==== SCENE 452 ====
    # [SPRITE lay2 image=+495 → si 2]
    # [SPRITE lay1 image=+302 → l 1]
    # [BGM bgm play=+19 → t18]
    # [BG stage image=+12]
    label ch10_452:
        $ show_sprites(("si 2", "l 1"))
        play music t18 fadein 1.0
        $ show_sprites(("si 2"))
        $ show_sprites(("l 1"))
        # サイト：そういえば、シエスタの部屋って。  [voice 13170]
        voice "ch10_s_063"
        s "Say, Siesta's room... {#ch10_s_063}"
        # JA[13170]: サイト：そういえば、シエスタの部屋って。
        # [SPRITE lay2 image=+495 → si 2]
        # シエスタ：はい。 / この前、ミス・ヴァリエールが魔法を使って / メチャクチャにしてしまって……。  [voice 15111]
        voice "ch10_si_034"
        si "Yes. / Before, Miss Varière used magic / and completely wrecked it... {#ch10_si_034}"
        # JA[15111]: シエスタ：はい。 / この前、ミス・ヴァリエールが魔法を使って / メチャクチャにしてしまって……。
        # [SPRITE lay2 image=+493 → si 1]
        # シエスタ：って、サイトさん忘れてたんですか？  [voice 15112]
        voice "ch10_si_035"
        si "Um, did Saito-san forget? {#ch10_si_035}"
        # JA[15112]: シエスタ：って、サイトさん忘れてたんですか？
        # [SPRITE lay5 image=+429 → s 1]
        # サイト：ご、ごめん。  [voice 13171]
        voice "ch10_s_064"
        s "I-I'm sorry. {#ch10_s_064}"
        # JA[13171]: サイト：ご、ごめん。
        # [SPRITE lay7 image=+957 → h 2 sad]
        # ハルナ：平賀くん……ひどい。  [voice 2519]
        voice "ch10_h_065"
        ha "Hiraga-kun... that's awful. {#ch10_h_065}"
        # JA[2519]: ハルナ：平賀くん……ひどい。
        # [SPRITE lay1 image=+302 → l 1]
        # ルイズ：必要なものがあれば言ってね、シエスタ。 / わたしにも少し責任があるから、 / 何かあれば買い足してあげるわ。  [voice 7150]
        voice "ch10_l_009"
        l "Let me know if you need anything, Siesta. / I'm partly responsible too, / so I'll buy replacements if anything's missing. {#ch10_l_009}"
        # JA[7150]: ルイズ：必要なものがあれば言ってね、シエスタ。 / わたしにも少し責任があるから、 / 何かあれば買い足してあげるわ。
        # → next scene 455
        jump ch10_455

    # ==== SCENE 453 ====
    # [SPRITE lay2 image=+524 → si 3]
    # [SPRITE lay1 image=+302 → l 1]
    # [BGM bgm play=+19 → t18]
    # [BG stage image=+12]
    label ch10_453:
        $ show_sprites(("si 3", "l 1"))
        play music t18 fadein 1.0
        $ show_sprites(("si 3"))
        # サイト：そっか……。 / じゃあ、引越しの手伝いをするよ。  [voice 13172]
        voice "ch10_s_065"
        s "I see. / Then I'll help with the move. {#ch10_s_065}"
        # JA[13172]: サイト：そっか……。 / じゃあ、引越しの手伝いをするよ。
        # [SPRITE lay2 image=+423 → si 1]
        # シエスタ：えっ、いいんですか？  [voice 15113]
        voice "ch10_si_036"
        si "Eh? / Is that OK? {#ch10_si_036}"
        # JA[15113]: シエスタ：えっ、いいんですか？
        # [SPRITE lay5 image=+390 → s 1]
        # サイト：うん、何でも言ってよ。  [voice 13173]
        voice "ch10_s_066"
        s "Yeah, anything you want. {#ch10_s_066}"
        # JA[13173]: サイト：うん、何でも言ってよ。
        # [SPRITE lay7 image=+951 → h 2]
        # ハルナ：わ、私も手伝います。  [voice 2520]
        voice "ch10_h_066"
        ha "W-Well, I'll help too. {#ch10_h_066}"
        # JA[2520]: ハルナ：わ、私も手伝います。
        # → next scene 455
        jump ch10_455

    # ==== SCENE 454 ====
    # [SPRITE lay2 image=+489 → si 2]
    # [SPRITE lay1 image=+306 → l 3]
    # [BGM bgm play=+19 → t18]
    # [BG stage image=+12]
    label ch10_454:
        $ show_sprites(("si 2", "l 3"))
        play music t18 fadein 1.0
        $ show_sprites(("si 2"))
        $ show_sprites(("l 3"))
        # サイト：そっか……。 / 部屋が新しくなって良かったよな。  [voice 13174]
        voice "ch10_s_067"
        s "I see. / The new room is nice, isn't it? {#ch10_s_067}"
        # JA[13174]: サイト：そっか……。 / 部屋が新しくなって良かったよな。
        # [SPRITE lay2 image=+495 → si 2]
        # シエスタ：……うっ。 / そういうものでもないですよ。 / 前の部屋には愛着も思い出もありましたし。  [voice 15114]
        voice "ch10_si_037"
        si "Ugh. / Not necessarily the case. / I have attachments and memories of the old room. {#ch10_si_037}"
        # JA[15114]: シエスタ：……うっ。 / そういうものでもないですよ。 / 前の部屋には愛着も思い出もありましたし。
        # [SPRITE lay5 image=+429 → s 1]
        # サイト：ご、ごめん。  [voice 13175]
        voice "ch10_s_068"
        s "I-I'm sorry. {#ch10_s_068}"
        # JA[13175]: サイト：ご、ごめん。
        # [SPRITE lay1 image=+306 → l 3]
        # ルイズ：な、なによ。 / そこで謝ると、わたしが悪役みたいじゃない！  [voice 7151]
        voice "ch10_l_010"
        l "W-What? / If you apologize there, I look like the villain! {#ch10_l_010}"
        # JA[7151]: ルイズ：な、なによ。 / そこで謝ると、わたしが悪役みたいじゃない！
        # [SPRITE lay5 image=+396 → s 1]
        # サイト：まあ、この場合……悪いのは……。  [voice 13176]
        voice "ch10_s_069"
        s "Well, in this case... who's at fault... {#ch10_s_069}"
        # JA[13176]: サイト：まあ、この場合……悪いのは……。
        # [SPRITE lay1 image=+335 → l 2]
        # ルイズ：なにかしら？ / サイト？  [voice 7152]
        voice "ch10_l_011"
        l "What is it? / Saito? {#ch10_l_011}"
        # JA[7152]: ルイズ：なにかしら？ / サイト？
        # [SPRITE lay5 image=+429 → s 1]
        # サイト：な、なんでもないです。  [voice 13177]
        voice "ch10_s_070"
        s "N-Nothing. / Nothing at all. {#ch10_s_070}"
        # JA[13177]: サイト：な、なんでもないです。
        # → next scene 455
        jump ch10_455

    # ==== SCENE 455 ====
    # [SPRITE lay1 image=+302 → l 1]
    # [BGM bgm play=+19 → t18]
    # [BG stage image=+12]
    label ch10_455:
        $ show_sprites(("l 1"))
        play music t18 fadein 1.0
        $ show_sprites(("si 1", "h 2"))
        # シエスタ：……あっ！ / そ、それでですね！ / もしよろしかったら、  [voice 15115]
        voice "ch10_si_038"
        si "Oh! / Um! / If it's OK... {#ch10_si_038}"
        # JA[15115]: シエスタ：……あっ！ / そ、それでですね！ / もしよろしかったら、
        # [SPRITE lay2 image=+524 → si 3]
        # シエスタ：ハルナさんも一緒にわたしの部屋に来たら / どうかなって思ったんです。  [voice 15116]
        voice "ch10_si_039"
        si "I thought it might be nice if Miss Haruna came to my room too. {#ch10_si_039}"
        # JA[15116]: シエスタ：ハルナさんも一緒にわたしの部屋に来たら / どうかなって思ったんです。
        # [SPRITE lay7 image=+957 → h 2 sad]
        # ハルナ：えっ！ / わ、私もですか？  [voice 2521]
        voice "ch10_h_067"
        ha "Eh? / M-Me too? {#ch10_h_067}"
        # JA[2521]: ハルナ：えっ！ / わ、私もですか？
        # サイト：シ、シエスタ！ / 大丈夫なのか？  [voice 13178]
        voice "ch10_s_071"
        s "Siesta! / Are you OK? {#ch10_s_071}"
        # JA[13178]: サイト：シ、シエスタ！ / 大丈夫なのか？
        # [SPRITE lay2 image=+489 → si 2]
        # シエスタ：やはりメイドの仕事をするとなると、 / 生活サイクルが変わりますし。  [voice 15117]
        voice "ch10_si_040"
        si "As expected, doing maid work / changes your lifestyle cycle. {#ch10_si_040}"
        # JA[15117]: シエスタ：やはりメイドの仕事をするとなると、 / 生活サイクルが変わりますし。
        # [SPRITE lay2 image=+489 → si 2]
        # シエスタ：一緒に暮らした方が、たくさんのことを / 教えてあげられると思うんです。  [voice 15118]
        voice "ch10_si_041"
        si "I think living together would allow me to teach you many things. {#ch10_si_041}"
        # JA[15118]: シエスタ：一緒に暮らした方が、たくさんのことを / 教えてあげられると思うんです。
        # [SPRITE lay5 image=+429 → s 1]
        # サイト：そ、それはそうだけど。  [voice 13179]
        voice "ch10_s_072"
        s "It's true, but... {#ch10_s_072}"
        # JA[13179]: サイト：そ、それはそうだけど。
        # ルイズ：それもそうね。  [voice 7153]
        voice "ch10_l_012"
        l "That's also true. {#ch10_l_012}"
        # JA[7153]: ルイズ：それもそうね。
        # [SPRITE lay5 image=+396 → s 1]
        # ルイズ：これ以上、わたしの部屋が２人の居候に / 占拠されるのも正直困るし……。 / どう、ハルナ？  [voice 7154]
        voice "ch10_l_013"
        l "Honestly, it's troubling if my room is occupied by two boarders / any longer... / What do you think, Haruna? {#ch10_l_013}"
        # JA[7154]: ルイズ：これ以上、わたしの部屋が２人の居候に / 占拠されるのも正直困るし……。 / どう、ハルナ？
        # ハルナ：はい、分かりました。  [voice 2522]
        voice "ch10_h_068"
        ha "Yes, understood. {#ch10_h_068}"
        # JA[2522]: ハルナ：はい、分かりました。
        # サイト：……。  [voice 13180]
        voice "ch10_s_073"
        s "...... {#ch10_s_073}"
        # JA[13180]: サイト：……。
        # ルイズ：あら、どうしたの？ / 納得できてない顔ね。  [voice 7155]
        voice "ch10_l_014"
        l "Oh, what's wrong? / You look unconvinced. {#ch10_l_014}"
        # JA[7155]: ルイズ：あら、どうしたの？ / 納得できてない顔ね。
        # サイト：……。  [voice 13181]
        voice "ch10_s_074"
        s "...... {#ch10_s_074}"
        # JA[13181]: サイト：……。
        # ルイズ：心配かもしれないけど、 / ハルナのことはシエスタに任せなさい。 / それが１番いいのよ、たぶん。  [voice 7156]
        voice "ch10_l_015"
        l "It might be worrisome, / but leave Haruna to Siesta. / That's probably the best option. {#ch10_l_015}"
        # JA[7156]: ルイズ：心配かもしれないけど、 / ハルナのことはシエスタに任せなさい。 / それが１番いいのよ、たぶん。
        # サイト：……うん。  [voice 13182]
        voice "ch10_s_075"
        s "...... Yes. {#ch10_s_075}"
        # JA[13182]: サイト：……うん。
        # → next scene 456
        jump ch10_456

    # ==== SCENE 456 ====
    # [BGM bgm play+20 → t19]
    # [BG stage image=+90]
    # [SPRITE lay5 hide] [BG stage hide]
    # [BG stage image=+28]
    label ch10_456:
        $ fade_fx("nightsky")
        play music t19 fadein 1.0
        $ fade_fx("courtyard")
        $ show_sprites(("s 1"))
        # サイト：……。  [voice 13183]
        voice "ch10_s_076"
        s "...... {#ch10_s_076}"
        # JA[13183]: サイト：……。
        # サイト：（シエスタの部屋に２人が移って……）
        s "(The two of them moved into Siesta's room…) {#ch10_s_077}"
        # JA[null]: サイト：（シエスタの部屋に２人が移って……）
        # サイト：（なんかルイズと２人きりだと、 / 部屋が広く感じるっつーか……）
        s "(With just Louise and me, the room feels spacious…) {#ch10_s_078}"
        # JA[null]: サイト：（なんかルイズと２人きりだと、 / 部屋が広く感じるっつーか……）
        # サイト：（……なんとなく、抜け出してきちゃったけど）
        s "(...I kind of slipped out but){#ch10_s_079}"
        # JA[null]: サイト：（……なんとなく、抜け出してきちゃったけど）
        # サイト：……。  [voice 13184]
        voice "ch10_s_080"
        s "...... {#ch10_s_080}"
        # JA[13184]: サイト：……。
        # サイト：まあ、いいか。 / きれいな月夜だし。  [voice 13185]
        voice "ch10_s_081"
        s "Well, fine. / It's a beautiful moonlit night. {#ch10_s_081}"
        # JA[13185]: サイト：まあ、いいか。 / きれいな月夜だし。
        # ハルナ：あれ、平賀くん！  [voice 2523]
        voice "ch10_h_069"
        ha "Ah, Hiraga-kun! {#ch10_h_069}"
        # JA[2523]: ハルナ：あれ、平賀くん！
        # サイト：あれ？ / 春奈？  [voice 13186]
        voice "ch10_s_082"
        s "Huh? / Haruna? {#ch10_s_082}"
        # JA[13186]: サイト：あれ？ / 春奈？
        # ハルナ：どうしたの？ / こんなところで……。  [voice 2524]
        voice "ch10_h_070"
        ha "What's wrong? / In a place like this... {#ch10_h_070}"
        # JA[2524]: ハルナ：どうしたの？ / こんなところで……。
        # サイト：眠れなかったんで、ちょっと月を見てた。  [voice 13187]
        voice "ch10_s_083"
        s "I couldn't sleep, so I was looking at the moon. {#ch10_s_083}"
        # JA[13187]: サイト：眠れなかったんで、ちょっと月を見てた。
        # ハルナ：あ！ / じゃあ私と同じね。  [voice 2525]
        voice "ch10_h_071"
        ha "Ah! / Then you're the same as me. {#ch10_h_071}"
        # JA[2525]: ハルナ：あ！ / じゃあ私と同じね。
        # [EVENT_CG event image=+273]
        $ dissolve_fx("ha_moon", type="cg")
        play music t16 fadein 1.0
        # ハルナ：きれいな月だね。 / 夜空に月が２つ。 / 不思議な光景よね……ホント。  [voice 2527]
        voice "ch10_h_072"
        ha "A beautiful moon. / Two moons in the night sky. / Mysterious scene, isn't it... really. {#ch10_h_072}"
        # JA[2527]: ハルナ：きれいな月だね。 / 夜空に月が２つ。 / 不思議な光景よね……ホント。
        # サイト：まったくだよな。  [voice 13189]
        voice "ch10_s_084"
        s "Exactly right. {#ch10_s_084}"
        # JA[13189]: サイト：まったくだよな。
        # ハルナ：はあ。  [voice 2528]
        voice "ch10_h_073"
        ha "Haa. {#ch10_h_073}"
        # JA[2528]: ハルナ：はあ。
        # サイト：どうしたのだよ、ため息なんてついて。  [voice 13190]
        voice "ch10_s_085"
        s "What's wrong, sighing like that. {#ch10_s_085}"
        # JA[13190]: サイト：どうしたのだよ、ため息なんてついて。
        # ハルナ：だって、こんなに自分が何もできないなんて、 / 思ってもみなかったから。  [voice 2529]
        voice "ch10_h_074"
        ha "Because I never thought / I'd be unable to do anything like this. {#ch10_h_074}"
        # JA[2529]: ハルナ：だって、こんなに自分が何もできないなんて、 / 思ってもみなかったから。
        # サイト：……。  [voice 13191]
        voice "ch10_s_086"
        s "...... {#ch10_s_086}"
        # JA[13191]: サイト：……。
        # 【選択肢】最初は誰だってそんなもの → scene 457
        # 【選択肢】確かにひどかった → scene 458
        # 【選択肢】頑張ってはいたよね → scene 459
        menu:
            "At first everyone feels like that. {#ch10_choice_013}":
                jump ch10_457
            "It was indeed terribly bad. {#ch10_choice_014}":
                jump ch10_458
            "You tried your best, didn't you? {#ch10_choice_015}":
                jump ch10_459

    # ==== SCENE 457 ====
    # [BGM bgm play+17 → t16]
    # [EVENT_CG event image=+273]
    label ch10_457:
        $ dissolve_fx("ha_moon", type="cg")
        play music t16 fadein 1.0
        $ show_sprites(("s 1", "h 2"))
        # サイト：最初は誰だってそんなものだよ。  [voice 13192]
        voice "ch10_s_087"
        s "At first everyone feels like that. {#ch10_s_087}"
        # JA[13192]: サイト：最初は誰だってそんなものだよ。
        # ハルナ：そうなのかな？  [voice 2530]
        voice "ch10_h_075"
        ha "I wonder? {#ch10_h_075}"
        # JA[2530]: ハルナ：そうなのかな？
        # サイト：最近の女の子ってあんな感じじゃないの。  [voice 13193]
        voice "ch10_s_088"
        s "These days girls are like that, aren't they? {#ch10_s_088}"
        # JA[13193]: サイト：最近の女の子ってあんな感じじゃないの。
        # ハルナ：どの女の子かによるわよ。 / 男の子もそうでしょう？  [voice 2531]
        voice "ch10_h_076"
        ha "It depends on which girl. / Boys too, right? {#ch10_h_076}"
        # JA[2531]: ハルナ：どの女の子かによるわよ。 / 男の子もそうでしょう？
        # → next scene 460
        jump ch10_460

    # ==== SCENE 458 ====
    # [BGM bgm play+17 → t16]
    # [EVENT_CG event image=+273]
    label ch10_458:
        $ dissolve_fx("ha_moon", type="cg")
        play music t16 fadein 1.0
        $ show_sprites(("s 1", "h 2"))
        # サイト：確かにひどかったよな。  [voice 13194]
        voice "ch10_s_089"
        s "It was indeed terribly bad. {#ch10_s_089}"
        # JA[13194]: サイト：確かにひどかったよな。
        # ハルナ：うっ……。 / やっぱり平賀くんもそう思う？  [voice 2532]
        voice "ch10_h_077"
        ha "Ugh... / Hiraga-kun thinks so too? {#ch10_h_077}"
        # JA[2532]: ハルナ：うっ……。 / やっぱり平賀くんもそう思う？
        # サイト：あ、いや……。  [voice 13195]
        voice "ch10_s_090"
        s "Ah, no... {#ch10_s_090}"
        # JA[13195]: サイト：あ、いや……。
        # → next scene 460
        jump ch10_460

    # ==== SCENE 459 ====
    # [BGM bgm play+17 → t16]
    # [EVENT_CG event image=+273]
    label ch10_459:
        $ dissolve_fx("ha_moon", type="cg")
        play music t16 fadein 1.0
        $ show_sprites(("s 1", "h 2"))
        # サイト：頑張っていたとは思うよ。  [voice 13196]
        voice "ch10_s_091"
        s "I think you tried your best, though. {#ch10_s_091}"
        # JA[13196]: サイト：頑張っていたとは思うよ。
        # ハルナ：でも、頑張っているだけじゃダメ / なんだよね。  [voice 2533]
        voice "ch10_h_078"
        ha "But just trying isn't enough / right. {#ch10_h_078}"
        # JA[2533]: ハルナ：でも、頑張っているだけじゃダメ / なんだよね。
        # サイト：ま、まあ、そうなんだけど。  [voice 13197]
        voice "ch10_s_092"
        s "Well, yes, but... {#ch10_s_092}"
        # JA[13197]: サイト：ま、まあ、そうなんだけど。
        # → next scene 460
        jump ch10_460

    # ==== SCENE 460 ====
    # [BGM bgm play+17 → t16]
    # [EVENT_CG event image=+273]
    label ch10_460:
        $ dissolve_fx("ha_moon", type="cg")
        play music t16 fadein 1.0
        $ show_sprites(("h 2", "s 1"))
        # ハルナ：はあ、やっぱりお嬢様育ちだったのかな？ / 私。  [voice 2534]
        voice "ch10_h_079"
        ha "Haa, really, was she raised as an ojou-sama from the beginning? / Me. {#ch10_h_079}"
        # JA[2534]: ハルナ：はあ、やっぱりお嬢様育ちだったのかな？ / 私。
        # サイト：……。  [voice 13198]
        voice "ch10_s_093"
        s "...... {#ch10_s_093}"
        # JA[13198]: サイト：……。
        # ハルナ：私の家ってね、ちょっとだけお金持ちだったの。  [voice 2535]
        voice "ch10_h_080"
        ha "My house was just a little rich. {#ch10_h_080}"
        # JA[2535]: ハルナ：私の家ってね、ちょっとだけお金持ちだったの。
        # ハルナ：ちょこっとだけセレブ……みたいな感じ。  [voice 2536]
        voice "ch10_h_081"
        ha "Just a little like a celebrity... feel. {#ch10_h_081}"
        # JA[2536]: ハルナ：ちょこっとだけセレブ……みたいな感じ。
        # サイト：へえ、そうなんだ。  [voice 13199]
        voice "ch10_s_094"
        s "Oh, I see. {#ch10_s_094}"
        # JA[13199]: サイト：へえ、そうなんだ。
        # ハルナ：でも、パパもママも忙しくて、 / 家事は通いのハウスキーパーまかせでね……。  [voice 2537]
        voice "ch10_h_082"
        ha "But Mom and Dad are busy, / and housework is entrusted to a visiting housekeeper... {#ch10_h_082}"
        # JA[2537]: ハルナ：でも、パパもママも忙しくて、 / 家事は通いのハウスキーパーまかせでね……。
        # ハルナ：おかげで家事をおぼえる機会もなくて、 / ホントに何もできなくなっちゃって。  [voice 2538]
        voice "ch10_h_083"
        ha "Thanks to that, I had no opportunity to learn housework, / and I really can't do anything now. {#ch10_h_083}"
        # JA[2538]: ハルナ：おかげで家事をおぼえる機会もなくて、 / ホントに何もできなくなっちゃって。
        # サイト：ああ、それで……。  [voice 13200]
        voice "ch10_s_095"
        s "Ah, therefore... {#ch10_s_095}"
        # JA[13200]: サイト：ああ、それで……。
        # ハルナ：一応、料理くらい勉強しようと思ってたんだよ？ / まさかこんな形で勉強することになるなんて、 / 全然思ってなかったけど。  [voice 2539]
        voice "ch10_h_084"
        ha "I was going to study cooking a bit, though? / Never thought I'd learn it like this, / not at all. {#ch10_h_084}"
        # JA[2539]: ハルナ：一応、料理くらい勉強しようと思ってたんだよ？ / まさかこんな形で勉強することになるなんて、 / 全然思ってなかったけど。
        # サイト：ま、それは確かに。  [voice 13201]
        voice "ch10_s_096"
        s "Well, that's true. {#ch10_s_096}"
        # JA[13201]: サイト：ま、それは確かに。
        # ハルナ：そんなわけでね。 / 私、家ではずっとひとりぼっちだったの。  [voice 2540]
        voice "ch10_h_085"
        ha "Therefore... / I was always alone at home. {#ch10_h_085}"
        # JA[2540]: ハルナ：そんなわけでね。 / 私、家ではずっとひとりぼっちだったの。
        # ハルナ：だから、今みたいにみんなでわいわいするのって / すごく新鮮だったんだよ。  [voice 2541]
        voice "ch10_h_086"
        ha "So, everyone talking happily is very fresh. {#ch10_h_086}"
        # JA[2541]: ハルナ：だから、今みたいにみんなでわいわいするのって / すごく新鮮だったんだよ。
        # ハルナ：疲れるときもあるけどね。  [voice 2542]
        voice "ch10_h_087"
        ha "Sometimes tiring, but... {#ch10_h_087}"
        # JA[2542]: ハルナ：疲れるときもあるけどね。
        # サイト：俺も時々……。 / いや、しょっちゅうかな？  [voice 13202]
        voice "ch10_s_097"
        s "I sometimes too... / No, quite often? {#ch10_s_097}"
        # JA[13202]: サイト：俺も時々……。 / いや、しょっちゅうかな？
        # ハルナ：ふふっ。 / そういえば、お芝居楽しかったね。  [voice 2543]
        voice "ch10_h_088"
        ha "Fufu. / Come to think of it, the play was fun. {#ch10_h_088}"
        # JA[2543]: ハルナ：ふふっ。 / そういえば、お芝居楽しかったね。
        # ハルナ：平賀くんがいて……みんながいて……。 / ウェザリーさんもいて。  [voice 2544]
        voice "ch10_h_089"
        ha "Hiraga-kun was there... Everyone was there. / Ms. Wesley was there too. {#ch10_h_089}"
        # JA[2544]: ハルナ：平賀くんがいて……みんながいて……。 / ウェザリーさんもいて。
        # サイト：そっか……。  [voice 13203]
        voice "ch10_s_098"
        s "I see... {#ch10_s_098}"
        # JA[13203]: サイト：そっか……。
        # ハルナ：うん。  [voice 2545]
        voice "ch10_h_090"
        ha "Yes. {#ch10_h_090}"
        # JA[2545]: ハルナ：うん。
        # ハルナ：あ、ごめんね、私ひとりでしゃべっちゃって。 / 明日も早いから、私もう行くね！  [voice 2546]
        voice "ch10_h_091"
        ha "Ah, sorry, I talked alone. / Tomorrow's early so I'm going now! {#ch10_h_091}"
        # JA[2546]: ハルナ：あ、ごめんね、私ひとりでしゃべっちゃって。 / 明日も早いから、私もう行くね！
        # サイト：あ、ああ。  [voice 13204]
        voice "ch10_s_099"
        s "Ah, OK. {#ch10_s_099}"
        # JA[13204]: サイト：あ、ああ。
        # ハルナ：今度は平賀くんの話も聞かせてね！  [voice 2547]
        voice "ch10_h_092"
        ha "Next time tell me about Hiraga-kun too! {#ch10_h_092}"
        # JA[2547]: ハルナ：今度は平賀くんの話も聞かせてね！
        # サイト：え？ / あ……うん。  [voice 13205]
        voice "ch10_s_100"
        s "Eh? / Ah... yes. {#ch10_s_100}"
        # JA[13205]: サイト：え？ / あ……うん。
        # ハルナ：約束だからね～～。  [voice 2548]
        voice "ch10_h_093"
        ha "Because it's a promise, ne~. {#ch10_h_093}"
        # JA[2548]: ハルナ：約束だからね～～。
        # サイト：……。  [voice 13206]
        voice "ch10_s_101"
        s "...... {#ch10_s_101}"
        # JA[13206]: サイト：……。
        # サイト：（どうして女の子の話って / あんなにとりとめがないのかな？ / 女の子っていうのはよく分からん）
        s "(Why are girls' talks / so rambling like that? / I don't understand girls at all.){#ch10_s_102}"
        # JA[null]: サイト：（どうして女の子の話って / あんなにとりとめがないのかな？ / 女の子っていうのはよく分からん）
        # → next scene 461
        jump ch10_461

    # ==== SCENE 461 ====
    # [BGM bgm play+19 → t18]
    # [BG stage image=+88]
    # [SPRITE lay5 image=+429 → s 1]
    # [SPRITE lay1 image=+302 → l 1]
    # [BG stage image=+23]
    # [SPRITE lay5 image=+390 → s 1]
    # [SPRITE lay1 image=+302 → l 1]
    # [SPRITE lay10 image=+918 → o 1]
    # [SPRITE lay20 image=+1061 → w 1]
    label ch10_461:
        $ fade_fx("sky")
        play music t18 fadein 1.0
        $ fade_fx("corridor")
        $ fade_fx("council_room")
        $ show_sprites(("o 1", "w 1"))
        # サイト：（そして翌日。 / いつものように授業を受けていた休み時間。 / ルイズがひとつの知らせを持ってきた）
        s "(The next day. / During lunch break as usual attending classes. / Louise brought one notice.){#ch10_s_103}"
        # JA[null]: サイト：（そして翌日。 / いつものように授業を受けていた休み時間。 / ルイズがひとつの知らせを持ってきた）
        # サイト：ウェザリーさんが学院に来たって？ / いったい何をしに？  [voice 13207]
        voice "ch10_s_104"
        s "Did Ms. Wesley come to the academy? / What for? {#ch10_s_104}"
        # JA[13207]: サイト：ウェザリーさんが学院に来たって？ / いったい何をしに？
        # ルイズ：さあ、分からないわ。 / 今、オールド・オスマンと、 / 話をしてるみたいだけど……。  [voice 7157]
        voice "ch10_l_016"
        l "I don't know. / Right now Old Osmond seems to be talking... {#ch10_l_016}"
        # JA[7157]: ルイズ：さあ、分からないわ。 / 今、オールド・オスマンと、 / 話をしてるみたいだけど……。
        # サイト：あの演劇の時、なにかあったのかな。 / 行ってみるか。  [voice 13208]
        voice "ch10_s_105"
        s "Was there something at the play? / Let's check. {#ch10_s_105}"
        # JA[13208]: サイト：あの演劇の時、なにかあったのかな。 / 行ってみるか。
        # ルイズ：うん。  [voice 7158]
        voice "ch10_l_017"
        l "Yes. {#ch10_l_017}"
        # JA[7158]: ルイズ：うん。
        # オスマン：ほう、学院の生徒達があなたの劇団で……。  [voice 4506]
        voice "ch10_o_007"
        o "Ho, academy students in your theater troupe... {#ch10_o_007}"
        # JA[4506]: オスマン：ほう、学院の生徒達があなたの劇団で……。
        # ウェザリー：はい。 / 準備不足のなかでも素晴らしい / 舞台を見せてくれました。  [voice 16073]
        voice "ch10_w_001"
        w "Yes. / Wonderful performance even unprepared. {#ch10_w_001}"
        # JA[16073]: ウェザリー：はい。 / 準備不足のなかでも素晴らしい / 舞台を見せてくれました。
        # オスマン：ふむ、もっと早く教えていただいていれば、 / 我々も見学に行けましたのに。  [voice 4507]
        voice "ch10_o_008"
        o "Hmm, if I had known sooner, / we could have gone to see it. {#ch10_o_008}"
        # JA[4507]: オスマン：ふむ、もっと早く教えていただいていれば、 / 我々も見学に行けましたのに。
        # ウェザリー：あら、貴族の子弟を芝居の舞台などに / 立たせたことで、お叱りがあるかと / 覚悟を決めておりましたのに。  [voice 16074]
        voice "ch10_w_002"
        w "Oh, nobles performing on stage / I was prepared for scolding. {#ch10_w_002}"
        # JA[16074]: ウェザリー：あら、貴族の子弟を芝居の舞台などに / 立たせたことで、お叱りがあるかと / 覚悟を決めておりましたのに。
        # オスマン：さあ、どうですかの……。 / それで、どのようなお話ですかな？  [voice 4508]
        voice "ch10_o_009"
        o "Well, how is it? / And what kind of story is it? {#ch10_o_009}"
        # JA[4508]: オスマン：さあ、どうですかの……。 / それで、どのようなお話ですかな？
        # ウェザリー：いえいえ、その先日の公演で / ヒロインを演じたミス・ハルナが、 / こちらにいるとのお話を聞きまして。  [voice 16075]
        voice "ch10_w_003"
        w "Well, I heard that Miss Haruna, who played the heroine in that performance, is here. {#ch10_w_003}"
        # JA[16075]: ウェザリー：いえいえ、その先日の公演で / ヒロインを演じたミス・ハルナが、 / こちらにいるとのお話を聞きまして。
        # ウェザリー：聞けば、生徒ではないとか……。  [voice 16076]
        voice "ch10_w_004"
        w "I heard she's not a student... {#ch10_w_004}"
        # JA[16076]: ウェザリー：聞けば、生徒ではないとか……。
        # ウェザリー：そこで、もしよろしければ / 当劇団にスカウトさせていただけないかと / 思いまして、伺った次第です。  [voice 16077]
        voice "ch10_w_005"
        w "Therefore, if you would be so kind — I came to ask whether you might allow us to scout her for our troupe. {#ch10_w_005}"
        # JA[16077]: ウェザリー：そこで、もしよろしければ / 当劇団にスカウトさせていただけないかと / 思いまして、伺った次第です。
        # オスマン：スカウト……じゃと？  [voice 4509]
        voice "ch10_o_010"
        o "Scout...? {#ch10_o_010}"
        # JA[4509]: オスマン：スカウト……じゃと？
        # ウェザリー：はい。 / ミス・ハルナは身寄りもないとのこと。 / 悪い話ではないと思いますが？  [voice 16078]
        voice "ch10_w_006"
        w "Yes. / Miss Hannah has no relatives / I don't think it's bad. {#ch10_w_006}"
        # JA[16078]: ウェザリー：はい。 / ミス・ハルナは身寄りもないとのこと。 / 悪い話ではないと思いますが？
        # コルベール：……ふうむ。 / ともかく、本人の意思を確かめてみましょう。  [voice 1203]
        voice "ch10_c_004"
        c "Hmm. / In any case let's confirm main person's intention. {#ch10_c_004}"
        # JA[1203]: コルベール：……ふうむ。 / ともかく、本人の意思を確かめてみましょう。
        # （………。 / ……。 / …。）
        s "(......... / ...... / ...){#ch10_s_119}"
        # JA[null]: （………。 / ……。 / …。）
        # オスマン：……というわけなのじゃが？ / えー、どうかの、ハルナくん。  [voice 4510]
        voice "ch10_o_011"
        o "It's that way... / Well then, Haruna-kun. {#ch10_o_011}"
        # JA[4510]: オスマン：……というわけなのじゃが？ / えー、どうかの、ハルナくん。
        # ウェザリー：どうかしら、ハルナ？ / 悪くない話だと思うけど……。  [voice 16079]
        voice "ch10_w_007"
        w "How about it, Hannah? / Not a bad story I think... {#ch10_w_007}"
        # JA[16079]: ウェザリー：どうかしら、ハルナ？ / 悪くない話だと思うけど……。
        # ハルナ：……。  [voice 2549]
        voice "ch10_h_094"
        ha "...... {#ch10_h_094}"
        # JA[2549]: ハルナ：……。
        # ハルナ：とてもありがたいお話だと思います。  [voice 2550]
        voice "ch10_h_095"
        ha "Very grateful story I think. {#ch10_h_095}"
        # JA[2550]: ハルナ：とてもありがたいお話だと思います。
        # ハルナ：で、でも……その……。  [voice 2551]
        voice "ch10_h_096"
        ha "But... that... / ... {#ch10_h_096}"
        # JA[2551]: ハルナ：で、でも……その……。
        # ハルナ：数日だけ……。 / 数日だけ考えさせてくださいませんか？  [voice 2552]
        voice "ch10_h_097"
        ha "A few days... / Please give me a few days. {#ch10_h_097}"
        # JA[2552]: ハルナ：数日だけ……。 / 数日だけ考えさせてくださいませんか？
        # ウェザリー：……。  [voice 16080]
        voice "ch10_w_008"
        w "...... {#ch10_w_008}"
        # JA[16080]: ウェザリー：……。
        # → next scene 462
        jump ch10_462

    # ==== SCENE 462 ====
    # [BGM bgm play+19 → t18]
    # [BG stage image=+11]
    # [SPRITE lay5 image=+394 → s 1]
    label ch10_462:
        $ fade_fx("classroom")
        play music t18 fadein 1.0
        $ show_sprites(("s 1"))
        # サイト：劇団へのスカウト！？  [voice 13209]
        voice "ch10_s_106"
        s "Troupe scout!? {#ch10_s_106}"
        # JA[13209]: サイト：劇団へのスカウト！！
        # ハルナ：うん。  [voice 2553]
        voice "ch10_h_098"
        ha "Yes. {#ch10_h_098}"
        # JA[2553]: ハルナ：うん。
        # ルイズ：それで、どうしてウェザリーの誘いに / すぐ返事をしなかったの？  [voice 7159]
        voice "ch10_l_018"
        l "So why didn't you reply immediately to Wesley's invitation? {#ch10_l_018}"
        # JA[7159]: ルイズ：それで、どうしてウェザリーの誘いに / すぐ返事をしなかったの？
        # モンモランシー：そうよ、いいお話じゃない。  [voice 4157]
        voice "ch10_m_005"
        m "Right, it's a good offer, isn't it. {#ch10_m_005}"
        # JA[4157]: モンモランシー：そうよ、いいお話じゃない。
        # ハルナ：そ、それは、その……。  [voice 2554]
        voice "ch10_h_099"
        ha "It's... that... {#ch10_h_099}"
        # JA[2554]: ハルナ：そ、それは、その……。
        # シエスタ：慣れないメイドのお仕事より、 / 望まれるお仕事の方が……。  [voice 15119]
        voice "ch10_si_042"
        si "Rather than unfamiliar maid work, / desired work is better... {#ch10_si_042}"
        # JA[15119]: シエスタ：慣れないメイドのお仕事より、 / 望まれるお仕事の方が……。
        # サイト：……。  [voice 13210]
        voice "ch10_s_107"
        s "...... {#ch10_s_107}"
        # JA[13210]: サイト：……。
        # 【選択肢】いい話だと思う → scene 463
        # 【選択肢】どうなんだろう？ → scene 464
        # 【選択肢】俺は反対……なのか？ → scene 465
        menu:
            "I also think it's a good offer. {#ch10_choice_016}":
                jump ch10_463
            "I wonder? {#ch10_choice_017}":
                jump ch10_464
            "Do I oppose it? {#ch10_choice_018}":
                jump ch10_465

    # ==== SCENE 463 ====
    # [BGM bgm play+19 → t18]
    # [BG stage image=+11]
    label ch10_463:
        $ fade_fx("classroom")
        play music t18 fadein 1.0
        $ show_sprites(("s 1", "h 2"))
        # サイト：俺もいい話だと思うけど。  [voice 13211]
        voice "ch10_s_108"
        s "I also think it's a good offer. {#ch10_s_108}"
        # JA[13211]: サイト：俺もいい話だと思うけど。
        # ハルナ：……。  [voice null]
        ha "...... {#ch10_h_100}"
        # JA[null]: ハルナ：……。
        # サイト：（な、なんだっていうんだ、春奈。 / 必死そうな目で俺を見て……）
        s "(What is this, Haruna. / Looking at me with desperate eyes...){#ch10_s_109}"
        # JA[null]: サイト：（な、なんだっていうんだ、春奈。 / 必死そうな目で俺を見て……）
        # → next scene 466
        jump ch10_466

    # ==== SCENE 464 ====
    # [BGM bgm play+19 → t18]
    # [BG stage image=+11]
    label ch10_464:
        $ fade_fx("classroom")
        play music t18 fadein 1.0
        $ show_sprites(("s 1", "h 2"))
        # サイト：（どうなんだろう？ / それでなくても慣れない世界なのに、 / 旅をしてまわるなんて……）
        s "(I wonder? / Even though unfamiliar world, / traveling around...){#ch10_s_110}"
        # JA[null]: サイト：（どうなんだろう？ / それでなくても慣れない世界なのに、 / 旅をしてまわるなんて……）
        # ハルナ：……。  [voice null]
        ha "...... {#ch10_h_101}"
        # JA[null]: ハルナ：……。
        # サイト：（な、なんだよ、春奈。 / 何かを期待するような目で俺を見て……）
        s "(What is it, Haruna. / Looking at me expecting something...){#ch10_s_111}"
        # JA[null]: サイト：（な、なんだよ、春奈。 / 何かを期待するような目で俺を見て……）
        # → next scene 466
        jump ch10_466

    # ==== SCENE 465 ====
    # [BGM bgm play+19 → t18]
    # [BG stage image=+11]
    label ch10_465:
        $ fade_fx("classroom")
        play music t18 fadein 1.0
        $ show_sprites(("s 1", "h 2"))
        # サイト：（もし、春奈が劇団に入るとして。 / 俺はそれでいいって言い切れるのか？）
        s "(If Haruna joins troupe. / Can I say it's OK?){#ch10_s_112}"
        # JA[null]: サイト：（もし、春奈が劇団に入るとして。 / 俺はそれでいいって言い切れるのか？）
        # サイト：（もし劇団に入れば、春奈は学院から / 居なくなるんだぞ。 / それでいいのか？）
        s "(If joins troupe, Haruna disappears from academy. / Is that OK?){#ch10_s_113}"
        # JA[null]: サイト：（もし劇団に入れば、春奈は学院から / 居なくなるんだぞ。 / それでいいのか？）
        # サイト：な、なあ、春奈……。  [voice 13212]
        voice "ch10_s_114"
        s "Well then, Haruna... {#ch10_s_114}"
        # JA[13212]: サイト：な、なあ、春奈……。
        # ハルナ：な、なに、平賀くん！  [voice 2555]
        voice "ch10_h_102"
        ha "W-What, Hiraga-kun! {#ch10_h_102}"
        # JA[2555]: ハルナ：な、なに、平賀くん！
        # サイト：……。  [voice 13213]
        voice "ch10_s_115"
        s "...... {#ch10_s_115}"
        # JA[13213]: サイト：……。
        # サイト：あ……うん……。 / ごめん、なんでもない。  [voice 13214]
        voice "ch10_s_116"
        s "Ah... yes... / Sorry, nothing. {#ch10_s_116}"
        # JA[13214]: サイト：あ……うん……。 / ごめん、なんでもない。
        # ハルナ：そ、そう……。  [voice 2556]
        voice "ch10_h_103"
        ha "Yes... that... {#ch10_h_103}"
        # JA[2556]: ハルナ：そ、そう……。
        # サイト：（ちくしょう！ / 俺が何を言えるっていうんだよ。 / ……くそっ！）
        s "(Damn it! / What can I say... / ...damn it!){#ch10_s_117}"
        # JA[null]: サイト：（ちくしょう！ / 俺が何を言えるっていうんだよ。 / ……くそっ！）
        # → next scene 466
        jump ch10_466

    # ==== SCENE 466 ====
    # [BGM bgm play+19 → t18]
    # [BG stage image=+11]
    label ch10_466:
        $ fade_fx("classroom")
        play music t18 fadein 1.0
        $ show_sprites(("k 1", "t 1"))
        # キュルケ：ウェザリーがハルナをスカウトに……ねぇ？ / どういうことかしら、タバサ。  [voice 3813]
        voice "ch10_k_001"
        k "Wesley scouted Hannah... hmm? / What is it, Tabitha? {#ch10_k_001}"
        # JA[3813]: キュルケ：ウェザリーがハルナをスカウトに……ねぇ？ / どういうことかしら、タバサ。
        # タバサ：……。  [voice null]
        t "...... {#ch10_t_001}"
        # JA[null]: タバサ：……。
        # ハルナ：もう少しだけ考えます。 / 皆さん、ありがとうございました。  [voice 2557]
        voice "ch10_h_104"
        ha "I'll think a bit more. / Everyone, thank you. {#ch10_h_104}"
        # JA[2557]: ハルナ：もう少しだけ考えます。 / 皆さん、ありがとうございました。
        # サイト：そうだな……。 / 急な話だし、もうちょっと / 考えてみたほうがいいよ。  [voice 13215]
        voice "ch10_s_118"
        s "Yeah... / Sudden talk so a bit more / think it'd be good. {#ch10_s_118}"
        # JA[13215]: サイト：そうだな……。 / 急な話だし、もうちょっと / 考えてみたほうがいいよ。
        # ハルナ：うん。 / そうするね。  [voice 2558]
        voice "ch10_h_105"
        ha "Yes. / I will do so. {#ch10_h_105}"
        # JA[2558]: ハルナ：うん。 / そうするね。
        # 【デート】ハルナ → scene 1174
        # 【デート進行】 → scene 467
        # → jump attention (конец части 2 / главы 10)
        jump attention
        return
