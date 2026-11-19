# script-ch8_3.rpy — Глава 8, часть 3: сцены 424–428
# Порт из ps2_source/chapters/chapter_09_決意のお姫さま.txt
# Граница части: 424–428, след. часть: ch8_4 (или конец главы)

label ch8_3:
    # ==== SCENE 424 ====
    # Примечание: сцена 424 — ветка «全力で青春する» (выбор c009) из меню ch8_2;
    #          после выбора сюда переходит управление, затем → next scene 425.

    # [SPRITE   lay8     image=+775, level=160, dir=1B]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [BGM      bgm      play=+28 → t28]
    play music t28 fadein 1.0
    # [BG       stage    image=+43, level=200 → id(43)]
    $ fade_fx("id(43)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay8     hide] [SPRITE   lay5     hide] [BG stage hide]
    $ show_sprites()
    $ fade_fx(None)
    # [SPRITE   lay5     image=+426, level=140, dir=2A]
    $ show_sprites(("s 3",))
    # [SPRITE   lay8     image=+794, level=160, dir=1C → h 2 shy]
    $ show_sprites(("s 3", "h 2 shy"))
    # サイト：よーし、これが青春なんだな！
    # [voice 13641]
    voice "ch8_s_082"
    s "Alright, this is youth! {#ch8_s_082}"
    # JA[13641]: よーし、これが青春なんだな！
    # サイト：俺についてこい！
    # [voice 13641] — продолжение той же реплики.
    # [SPRITE   lay5     hide]
    $ show_sprites()
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # [BGM      bgm      play=+28 → t28]
    $ show_sprites(("s 3", "l 1", "s 2"))
    play music t28 fadein 1.0
    # シエスタ：サイトさんが、サイトさんが……。  [voice 15176]
    voice "ch8_si_010"
    si "That's Saito, that's Saito…! {#ch8_si_010}"
    # JA[15176]: シエスタ：サイトさんが、サイトさんが……。
    # ルイズ：大丈夫、わたしが直してあげるわ。
    # [voice 7457]
    voice "ch8_l_051"
    l "It's fine. I'll fix it. {#ch8_l_051}"
    # JA[7457]: 大丈夫、わたしが直してあげるわ。
    # サイト、ちょっと来なさい。  [voice 7457]
    # サイト：え、あ、お、おい……。
    # 冗談だってば……。  [voice 13642]
    voice "ch8_s_083"
    s "Eh, ah, oh, o-oh… It's just a joke… {#ch8_s_083}"
    # JA[13642]: サイト：え、あ、お、おい……。 / 冗談だってば……。
    # [SPRITE   lay1     hide] [SPRITE   lay5     hide] [BG stage hide]
    # [EVENT_CG event    hide]
    $ show_sprites()
    $ fade_fx(None)
    # [BG       stage    image=+90, level=200]
    # [TRANS trans("crossfade", 1000)]
    # null：………。
    # ……。
    # …。
    # [SE       se0      play=+62]
    # [SPRITE   lay1     hide] [SPRITE   lay5     hide] [SPRITE   lay3 vibrate=14]
    # ...  [VIBRATE vibrate(2)]
    # [BG       stage    reset]
    # ... reset commands
    # [SE       se0      play=+61]
    # ... reset commands
    # [BG       stage    image=+43, level=200]
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：なんとか直してきたわ。  [voice 7458]
    voice "ch8_l_052"
    l "I managed to fix it somehow. {#ch8_l_052}"
    # JA[7458]: ルイズ：なんとか直してきたわ。
    # サイト：がたがたぶるぶる……。  [voice 13643]
    voice "ch8_s_084"
    s "Ugh, ugh, grumble…? {#ch8_s_084}"
    # JA[13643]: サイト：がたがたぶるぶる……。
    # ルイズ：姫さま！  [voice 7459]
    voice "ch8_l_053"
    l "Your Highness! {#ch8_l_053}"
    # JA[7459]: ルイズ：姫さま！
    # アンリエッタ：はい！  [voice 910]
    voice "ch8_h_059"
    h "Yes! {#ch8_h_059}"
    # JA[910]: アンリエッタ：はい！
    # ルイズ：わたしは反対です。
    # でも、姫さまが自ら決めたのなら、
    # 従いましょう。  [voice 7460]
    voice "ch8_l_054"
    l "I disagree. But if you've decided, then I'll follow. {#ch8_l_054}"
    # JA[7460]: ルイズ：わたしは反対です。 / でも、姫さまが自ら決めたのなら、 / 従いましょう。
    # アンリエッタ：ルイズ、ありがとうございます。  [voice 911]
    voice "ch8_h_060"
    h "Thank you, Louise. {#ch8_h_060}"
    # JA[911]: アンリエッタ：ルイズ、ありがとうございます。
    # → next scene 425

label ch8_3_425:
    # ==== SCENE 425 ====
    # [SPRITE   lay8     image=+775, level=160, dir=1B]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+28 → t28]
    play music t28 fadein 1.0
    # [BG       stage    image=+43, level=200 → id(43)]
    $ fade_fx("id(43)")
    # サイト：軍の人達に合流するつもりですか？  [voice 13644]
    voice "ch8_s_085"
    s "So you're going to join up with the army? {#ch8_s_085}"
    # JA[13644]: サイト：軍の人達に合流するつもりですか？
    # [SPRITE   lay8     image=+775, level=160, dir=1B]
    # アンリエッタ：いいえ。
    # わたくしは、王宮へ戻るつもりです。  [voice 912]
    voice "ch8_h_061"
    h "No. I'm returning to the palace. {#ch8_h_061}"
    # JA[912]: アンリエッタ：いいえ。 / わたくしは、王宮へ戻るつもりです。
    # アンリエッタ：ですから、そこまでの道中を皆さんと
    # ご一緒したいのです。  [voice 913]
    voice "ch8_h_062"
    h "So I'd like to accompany you on the way there, if you don't mind. {#ch8_h_062}"
    # JA[913]: アンリエッタ：ですから、そこまでの道中を皆さんと / ご一緒したいのです。
    # サイト：でも、今攻められてる最中の王宮に、
    # 無理して戻らなくても……。  [voice 13645]
    voice "ch8_s_086"
    s "But the palace is under attack right now. You don't have to force your way back… {#ch8_s_086}"
    # JA[13645]: サイト：でも、今攻められてる最中の王宮に、 / 無理して戻らなくても……。
    # アンリエッタ：わたくしが王宮内に無事でいることで、
    # トリステインが健在であることを
    # 示せるだけでよいのです。  [voice 914]
    voice "ch8_h_063"
    h "It's enough that I'm safe inside the palace — that shows Tristain is still standing. {#ch8_h_063}"
    # JA[914]: アンリエッタ：わたくしが王宮内に無事でいることで、 / トリステインが健在であることを / 示せるだけでよいのです。
    # アンリエッタ：それに、わたくしにもひとつ、
    # 考えていることがあるのですよ。  [voice 915]
    voice "ch8_h_064"
    h "Besides, I have something on my mind. {#ch8_h_064}"
    # JA[915]: アンリエッタ：それに、わたくしにもひとつ、 / 考えていることがあるのですよ。
    # アンリエッタ：女王としてのわたくしとは別に、
    # 魔術師としてのわたくしにできることが、
    # ひとつある……と考えているのです。  [voice 916]
    voice "ch8_h_065"
    h "Apart from me as queen, there's just one thing I can do as a mage. {#ch8_h_065}"
    # JA[916]: アンリエッタ：女王としてのわたくしとは別に、 / 魔術師としてのわたくしにできることが、 / ひとつある……と考えているのです。
    # サイト：それは、いったい何ですか？  [voice 13646]
    voice "ch8_s_087"
    s "And what is that? {#ch8_s_087}"
    # JA[13646]: サイト：それは、いったい何ですか？
    # アンリエッタ：それは、その時がきたらお話しします。
    # そうですね、奥の手と思ってください。  [voice 917]
    voice "ch8_h_066"
    h "That's something I'll tell you about when the time comes. For now, just think of it as a backup plan. {#ch8_h_066}"
    # JA[917]: アンリエッタ：それは、その時がきたらお話しします。 / そうですね、奥の手と思ってください。
    # ルイズ：分かりました。
    # 精一杯、姫さまをお守りさせていただきます。  [voice 7461]
    voice "ch8_l_055"
    l "Understood. I'll do my best to protect the Princess. {#ch8_l_055}"
    # JA[7461]: ルイズ：分かりました。 / 精一杯、姫さまをお守りさせていただきます。
    # アンリエッタ：ありがとう、ルイズ。  [voice 918]
    voice "ch8_h_067"
    h "Thank you, Louise. {#ch8_h_067}"
    # JA[918]: アンリエッタ：ありがとう、ルイズ。
    # ギーシュ：おや？ / なんだか外が、急に騒がしくなったぞ。 / 何かあったのか。  [voice 1564]
    voice "ch8_g_003"
    g "Hey? Something seems to be happening outside. What's going on? {#ch8_g_003}"
    # JA[1564]: ギーシュ：おや？ / なんだか外が、急に騒がしくなったぞ。 / 何かあったのか。
    # キュルケ：まさか！？  [voice 3868]
    voice "ch8_k_011"
    k "No way!? {#ch8_k_011}"
    # JA[3868]: キュルケ：まさか！？
    # 敵ＥＡ：見つけたぞ。  [voice 1386]
    voice "ch8_e_001"
    enemy "I found them. {#ch8_e_001}"
    # JA[1386]: 敵ＥＡ：見つけたぞ。
    # シエスタ：きゃああっ！  [voice 15177]
    voice "ch8_si_011"
    si "Kyaaa! {#ch8_si_011}"
    # JA[15177]: シエスタ：きゃああっ！
    # キュルケ：レコン・キスタの刺客なのね。  [voice 3869]
    voice "ch8_k_012"
    k "They're the Reconquista assassins, aren't they. {#ch8_k_012}"
    # JA[3869]: キュルケ：レコン・キスタの刺客なのね。
    # サイト：くそっ！ / まさかここで戦うハメになるとは！  [voice 13647]
    voice "ch8_s_088"
    s "Damn it! So this is where it comes down to? {#ch8_s_088}"
    # JA[13647]: サイト：くそっ！ / まさかここで戦うハメになるとは！
    # ルイズ：シエスタ！ / 危険だわ、下がって！  [voice 7462]
    voice "ch8_l_056"
    l "Siesta! Get back! It's dangerous! {#ch8_l_056}"
    # JA[7462]: ルイズ：シエスタ！ / 危険だわ、下がって！
    # シエスタ：は、はいっ！  [voice 15178]
    voice "ch8_si_012"
    si "Yes! {#ch8_si_012}"
    # JA[15178]: シエスタ：は、はいっ！
    # キュルケ：まずは、こいつらを返り討ちにしないとねっ！  [voice 3870]
    voice "ch8_k_013"
    k "First, let's turn and fight back! {#ch8_k_013}"
    # JA[3870]: キュルケ：まずは、こいつらを返り討ちにしないとねっ！
    # タバサ：全員拘束。 / 帰しちゃ駄目。  [voice 15813]
    voice "ch8_t_003"
    t "All detained. Can't let you retreat. {#ch8_t_003}"
    # JA[15813]: タバサ：全員拘束。 / 帰しちゃ駄目。
    # サイト：さあっ、いくぜえっ！  [voice 13648]
    voice "ch8_s_089"
    s "Alright, let's do this! {#ch8_s_089}"
    # JA[13648]: サイト：さあっ、いくぜえっ！
    # → next scene 426

    # ==== SCENE 426 ====
    # [BG       stage    image=+43, level=200 → id(43)]
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25 → t25]
    play music t25 fadein 1.0
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    $ show_sprites(("s 3",))
    # サイト：みんな、無事か！  [voice 13649]
    voice "ch8_s_090"
    s "Everyone, are you all right!? {#ch8_s_090}"
    # JA[13649]: サイト：みんな、無事か！
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # ルイズ：姫さまも、シエスタも、みんな無事。  [voice 7463]
    voice "ch8_l_057"
    l "The Princess and Siesta, everyone is safe. {#ch8_l_057}"
    # JA[7463]: ルイズ：姫さまも、シエスタも、みんな無事。
    # [SPRITE   lay5     hide]
    $ show_sprites()
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：敵は全員、撃退したわね。  [voice 3871]
    voice "ch8_k_014"
    k "We drove them all off. {#ch8_k_014}"
    # JA[3871]: キュルケ：敵は全員、撃退したわね。
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：こうなった以上、のんびりしてられないわ。 / 急がなくちゃ！  [voice 7464]
    voice "ch8_l_058"
    l "This is getting out of hand. We have to hurry! {#ch8_l_058}"
    # JA[7464]: ルイズ：こうなった以上、のんびりしてられないわ。 / 急がなくちゃ！
    # [SPRITE   lay6     hide]
    $ show_sprites()
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：シエスタは、ここで待っててくれ。 / 本当は学院のほうが安全だけど、 / そんな時間もない。  [voice 13650]
    voice "ch8_s_091"
    s "Siesta, wait here. The academy is safer, but there's no time. {#ch8_s_091}"
    # JA[13650]: サイト：シエスタは、ここで待っててくれ。 / 本当は学院のほうが安全だけど、 / そんな時間もない。
    # シエスタ：は、はいっ。 / サイトさん、ご武運を……。  [voice 15179]
    voice "ch8_si_013"
    si "Yes! Good luck in battle, Saito-san…! {#ch8_si_013}"
    # JA[15179]: シエスタ：は、はいっ。 / サイトさん、ご武運を……。
    # サイト：ああ……。  [voice 13651]
    voice "ch8_s_092"
    s "Yeah… {#ch8_s_092}"
    # JA[13651]: サイト：ああ……。
    # ルイズ：では、二手に分かれましょう。 / わたしにサイト、姫さまとキュルケは、 / このまま王宮をめざすことにするわ。  [voice 7465]
    voice "ch8_l_059"
    l "Then let's split up. I'll go with the Princess, Saito, and Kirche to the palace. {#ch8_l_059}"
    # JA[7465]: ルイズ：では、二手に分かれましょう。 / わたしにサイト、姫さまとキュルケは、 / このまま王宮をめざすことにするわ。
    # キュルケ：タバサ、モンモランシー、ギーシュは、 / 砲台への攻撃をお願い。 / 気をつけてね。  [voice 3872]
    voice "ch8_k_015"
    k "Tabitha, Montmorency, and Guiche — attack the cannons. Be careful. {#ch8_k_015}"
    # JA[3872]: キュルケ：タバサ、モンモランシー、ギーシュは、 / 砲台への攻撃をお願い。 / 気をつけてね。
    # タバサ：了解。  [voice 15814]
    voice "ch8_t_004"
    t "Understood. {#ch8_t_004}"
    # JA[15814]: タバサ：了解。
    # ルイズ：わたしにサイト、姫さまとキュルケは、 / このまま王宮をめざすことにするわ。  [voice 7466]
    voice "ch8_l_060"
    l "So I'll have Site, the Princess, and Kirche head to the palace. {#ch8_l_60}"
    # JA[7466]: ルイズ：わたしにサイト、姫さまとキュルケは、 / このまま王宮をめざすことにするわ。
    # アンリエッタ：分かりました。 / 足手まといにならないよう、 / 頑張ります。  [voice 919]
    voice "ch8_h_068"
    h "Understood. I'll make sure I'm not an obstacle. Do your best. {#ch8_h_068}"
    # JA[919]: アンリエッタ：分かりました。 / 足手まといにならないよう、 / 頑張ります。
    # ルイズ：では、作戦開始ね。  [voice 7467]
    voice "ch8_l_061"
    l "Then, the plan begins. {#ch8_l_061}"
    # JA[7467]: ルイズ：では、作戦開始ね。
    # → next scene 427

    # ==== SCENE 427 ====
    # [BG       stage    image=+43, level=200 → id(43)]
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25 → t25]
    play music t25 fadein 1.0
    # [SPRITE   lay15    image=+1114, level=160, dir=1A]  # 味方Ａ (ally A)
    # [SPRITE   lay17    image=+1114, level=160, dir=1A]  # 味方Ａ
    # 味方Ａ：陥下！ご無事で！  [voice 4278]
    voice "ch8_a_001"
    man_a "Your Majesty! Are you safe!? {#ch8_a_001}"
    # JA[4278]: 味方Ａ：陥下！ご無事で！
    # 味方Ａ：陥下が戻られた！ / これで、我々の勝利だ！  [voice 4279]
    voice "ch8_a_002"
    man_a "Your Majesty has returned! Now, we have won! {#ch8_a_002}"
    # JA[4279]: 味方Ａ：陥下が戻られた！ / これで、我々の勝利だ！
    # [SPRITE   lay15    hide] [SPRITE   lay17    hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]  # サイト
    # サイト：すごいな。 / お姫さまの姿を見ただけで、 / 城の連中の雰囲気が変わっていくよ。  [voice 13652]
    voice "ch8_s_093"
    s "Wow. Just seeing the Princess is changing the mood of the city. {#ch8_s_093}"
    # JA[13652]: サイト：すごいな。 / お姫さまの姿を見ただけで、 / 城の連中の雰囲気が変わっていくよ。
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay19    image=+940, level=160, dir=1A]  # デルフリンガー
    # デルフリンガー：王様ってなあそんなもんだよ。 / この人がいれば大丈夫って思させられるのも / 仕事ってもんだ。  [voice 1372]
    voice "ch8_d_001"
    d "That's what being a king is like. Making people think that with her around everything will be all right — that's part of the job. {#ch8_d_001}"
    # JA[1372]: デルフリンガー：王様ってなあそんなもんだよ。 / この人がいれば大丈夫って思させられるのも / 仕事ってもんだ。
    # [SPRITE   lay5     hide] [SPRITE   lay19    hide]
    # [SPRITE   lay8     image=+779, level=160, dir=1B]  # アンリエッタ
    # アンリエッタ：状況はどうなっていますか。  [voice 920]
    voice "ch8_h_069"
    h "How is the situation? {#ch8_h_069}"
    # JA[920]: アンリエッタ：状況はどうなっていますか。
    # [SPRITE   lay8     x=224, y=0]
    # [SPRITE   lay18    image=+1121, level=160, dir=1A]  # 将校
    # 将校：はっ / 朝から、東側の砲台で小規模な戦闘が発生しております。  [voice 4354]
    voice "ch8_o_001"
    commander "Yes, sir. Small-scale combat has been occurring at the eastern cannon since morning. {#ch8_o_001}"
    # JA[4354]: 将校：はっ / 朝から、東側の砲台で小規模な戦闘が発生しております。
    # 将校：そのためか、城への砲撃は / 今のところ停止しております。  [voice 4355]
    voice "ch8_o_002"
    commander "That would explain why the castle bombardment has stopped, for now. {#ch8_o_002}"
    # JA[4355]: 将校：そのためか、城への砲撃は / 今のところ停止しております。
    # [SPRITE   lay8     hide] [SPRITE   lay18    hide]
    # [SPRITE   lay6     image=+676, level=154, dir=1A]  # キュルケ
    # キュルケ：タバサ達が、頑張ってくれてるのね。  [voice 3873]
    voice "ch8_k_016"
    k "Tabitha and the others are doing their best, aren't they. {#ch8_k_016}"
    # JA[3873]: キュルケ：タバサ達が、頑張ってくれてるのね。
    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：ああ。 / そうだな。  [voice 13653]
    voice "ch8_s_094"
    s "Yeah, I see. {#ch8_s_94}"
    # JA[13653]: サイト：ああ。 / そうだな。
    # [SPRITE   lay6     hide] [SPRITE   lay5     hide]
    # [SPRITE   lay18    image=+1125, level=160, dir=1A]  # 将校
    # 将校：ですが、レコン・キスタからの大艦隊が……。  [voice 4356]
    voice "ch8_o_003"
    commander "However, the Reconquista fleet is… approaching. {#ch8_o_003}"
    # JA[4356]: 将校：ですが、レコン・キスタからの大艦隊が……。
    # [SPRITE   lay18    x=-96, y=0]
    # [SPRITE   lay8     image=+775, level=151, dir=1B]  # アンリエッタ
    # アンリエッタ：分かっています。 / ですから、奥の手を用意してきました。  [voice 921]
    voice "ch8_h_070"
    h "I understand. That's why I've prepared the backup plan. {#ch8_h_070}"
    # JA[921]: アンリエッタ：分かっています。 / ですから、奥の手を用意してきました。
    # [SPRITE   lay18    image=+1121, level=160, dir=1A]
    # 将校：奥の手……ですか？  [voice 4357]
    voice "ch8_o_004"
    commander "The backup plan…? {#ch8_o_004}"
    # JA[4357]: 将校：奥の手……ですか？
    # アンリエッタ：詳しいことはこの戦いが終わったら / 説明します。  [voice 922]
    voice "ch8_h_071"
    h "I'll explain the details after this battle is over. {#ch8_h_071}"
    # JA[922]: アンリエッタ：詳しいことはこの戦いが終わったら / 説明します。
    # アンリエッタ：市街に展開している各部隊に伝達。 / 現状このまま包囲して待機、敵陣に混乱が / 生じたら一気に突入してください。  [voice 923]
    voice "ch8_h_072"
    h "I'll relay this to all units deployed in the city. Keep surrounding them and wait. If chaos occurs in the enemy camp, then launch an all-out assault. {#ch8_h_072}"
    # JA[923]: アンリエッタ：市街に展開している各部隊に伝達。 / 現状このまま包囲して待機、敵陣に混乱が / 生じたら一気に突入してください。
    # [SPRITE   lay18    hide] [SPRITE   lay8     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]  # キュルケ
    # 将校：はっ、了解いたしました！  [voice 4358]
    voice "ch8_o_005"
    commander "Understood! {#ch8_o_005}"
    # JA[4358]: 将校：はっ、了解いたしました！
    # [SPRITE   lay8     hide] [SPRITE   lay18    hide]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]  # サイト
    # サイト：よしっ、このまま屋上に出るぞ！ / そこからなら、お前の魔法で一気に / ケリをつけられるんだな？  [voice 13654]
    voice "ch8_s_095"
    s "Alright, let's head to the roof! From there, with your magic you can finish them all off in one go, right? {#ch8_s_095}"
    # JA[13654]: サイト：よしっ、このまま屋上に出るぞ！ / そこからなら、お前の魔法で一気に / ケリをつけられるんだな？
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+335, level=155, dir=2A]  # ルイズ
    # ルイズ：ええ、まかせて！ / わたしの真の実力を見せてあげるわ！  [voice 7468]
    voice "ch8_l_062"
    l "Yes, please rely on me. I'll show you my true power! {#ch8_l_062}"
    # JA[7468]: ルイズ：ええ、まかせて！ / わたしの真の実力を見せてあげるわ！
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：こら！ / もっと、ご主人様を信じなさい。  [voice 7469]
    voice "ch8_l_063"
    l "Hey! Believe in your master more! {#ch8_l_063}"
    # JA[7469]: ルイズ：こら！ / もっと、ご主人様を信じなさい。
    # [SPRITE   lay5     hide] [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [SPRITE   lay5     image=+403, level=156, dir=1B]
    # サイト：とっ、到着～！  [voice 13656]
    voice "ch8_s_096"
    s "Here we come! {#ch8_s_096}"
    # JA[13656]: サイト：とっ、到着～！
    # ルイズ：はあ、はあ、はあ……っ。 / 分かってたことだけど、高いところね。 / 階段を昇るのに疲れたわ。  [voice 7470]
    voice "ch8_l_064"
    l "Whew, whew, whew… It's a high place. Climbing all those stairs was tiring. {#ch8_l_064}"
    # JA[7470]: ルイズ：はあ、はあ、はあ……っ。 / 分かってたことだけど、高いところね。 / 階段を昇るのに疲れたわ。
    # [SPRITE   lay5     image=+403, level=156, dir=1B]
    # サイト：だけど、見ろよ。 / ここからなら、砲台全部が視界に入る！  [voice 13657]
    voice "ch8_s_097"
    s "But look at this! From here, we can see all the cannons! {#ch8_s_097}"
    # JA[13657]: サイト：だけど、見ろよ。 / ここからなら、砲台全部が視界に入る！
    # ルイズ：よーし、見てなさい！ / レコン・キスタの連中に、正義の鉄槌を / 下してあげるわ！  [voice 7471]
    voice "ch8_l_065"
    l "All right, watch this! I'll smack the Reconquista forces with the righteous hammer of justice! {#ch8_l_065}"
    # JA[7471]: ルイズ：よーし、見てなさい！ / レコン・キスタの連中に、正義の鉄槌を / 下してあげるわ！
    # [BGM      bgm      stop=1000]
    # [EVENT_CG event    image=+139, level=80]
    # [BGM      bgm      play=+18]
    play music t18 fadein 1.0
    # ウェザリー：そうはいかない。  [voice 16166]
    voice "ch8_w_001"
    w "You won't get away with this. {#ch8_w_001}"
    # JA[16166]: ウェザリー：そうはいかない。
    # サイト：っ！？  [voice 13658]
    voice "ch8_s_098"
    s "What!? {#ch8_s_098}"
    # JA[13658]: サイト：っ！？
    # ウェザリー：驚いたな。 / まさかここまで来るとは……。 / きみ達を正直見くびっていたよ。  [voice 16167]
    voice "ch8_w_002"
    w "Well, I'm surprised. You really came this far, didn't you. I underestimated you. {#ch8_w_002}"
    # JA[16167]: ウェザリー：驚いたな。 / まさかここまで来るとは……。 / きみ達を正直見くびっていたよ。
    # アキナ：もう……。 / 戦うのも面倒なんだから、 / ここに来ないでよね。  [voice 258]
    voice "ch8_ak_001"
    ak "I'm not in the mood for fighting anymore. Just stay here. {#ch8_ak_001}"
    # JA[258]: アキナ：もう……。 / 戦うのも面倒なんだから、 / ここに来ないでよね。
    # サイト：ウェザリー、それにアキナ！  [voice 13659]
    voice "ch8_s_099"
    s "Weatherby, and Akina too! {#ch8_s_099}"
    # JA[13659]: サイト：ウェザリー、それにアキナ！
    # デルフリンガー：たぶん、俺達がここに来ると思って、 / 先回りしたんだろうよ。  [voice 1373]
    voice "ch8_d_002"
    d "Maybe they figured we'd come here and got here ahead of us. {#ch8_d_002}"
    # JA[1373]: デルフリンガー：たぶん、俺達がここに来ると思って、 / 先回りしたんだろうよ。
    # ウェザリー：ハルナが集めてくれた情報のおかげだよ。 / 最も、ハルナは無意識に情報を / 集めていただけだけどね。  [voice 16168]
    voice "ch8_w_003"
    w "It's thanks to the information gathered by Haruna. Though she collected it unconsciously. {#ch8_w_003}"
    # JA[16168]: ウェザリー：ハルナが集めてくれた情報のおかげだよ。 / 最も、ハルナは無意識に情報を / 集めていただけだけどね。
    # サイト：なにっ！？  [voice 13660]
    voice "ch8_s_100"
    s "What!? {#ch8_s_100}"
    # JA[13660]: サイト：なにっ！？
    # ウェザリー：なぜ定期的にハルナが襲われたのか、 / 本当の意味を分かってないだろ？  [voice 16169]
    voice "ch8_w_004"
    w "Do you even understand why Haruna was being targeted regularly? {#ch8_w_004}"
    # JA[16169]: ウェザリー：なぜ定期的にハルナが襲われたのか、 / 本当の意味を分かってないだろ？
    # ウェザリー：そのとき、アキナがサイトやルイズの / 情報をわたしまで、伝えていたのさ。  [voice 16170]
    voice "ch8_w_005"
    w "That's when Akina was passing information about you and Louise to me. {#ch8_w_005}"
    # JA[16170]: ウェザリー：そのとき、アキナがサイトやルイズの / 情報をわたしまで、伝えていたのさ。
    # ウェザリー：もっとも、アキナがやったことは / ハルナは一切覚えていないんだけどね。  [voice 16171]
    voice "ch8_w_006"
    w "Though Haruna doesn't remember any of what Akina did. {#ch8_w_006}"
    # JA[16171]: ウェザリー：もっとも、アキナがやったことは / ハルナは一切覚えていないんだけどね。
    # サイト：くそっ、ウェザリー！ / 春奈を元に戻せ！  [voice 13661]
    voice "ch8_s_101"
    s "Damn you, Weatherby! Restore Haruna! {#ch8_s_101}"
    # JA[13661]: サイト：くそっ、ウェザリー！ / 春奈を元に戻せ！
    # ウェザリー：残念だが、それはできない相談だ。 / わたしには目的があるんだ。 / それを達成するまでは利用させてもらうよ。  [voice 16172]
    voice "ch8_w_007"
    w "Unfortunately, that's not something I can agree to. I have my own goals. Until I achieve them, I will use you. {#ch8_w_007}"
    # JA[16172]: ウェザリー：残念だが、それはできない相談だ。 / わたしには目的があるんだ。 / それを達成するまでは利用させてもらうよ。
    # サイト：春奈……。  [voice 13662]
    voice "ch8_s_102"
    s "Haruna… {#ch8_s_102}"
    # JA[13662]: サイト：春奈……。
    # ウェザリー：王宮の屋上から、長距離攻撃呪文で / 砲台を攻撃するつもりだったんだろうが、 / こちらが先に占拠してしまえば無意味だよ。  [voice 16173]
    voice "ch8_w_008"
    w "You intended to attack the cannons from the palace rooftop with a long-range spell. But since we're already occupying it, it's meaningless. {#ch8_w_008}"
    # JA[16173]: ウェザリー：王宮の屋上から、長距離攻撃呪文で / 砲台を攻撃するつもりだったんだろうが、 / こちらが先に占拠してしまえば無意味だよ。
    # ウェザリー：このまま屋上で始末してあげるよ。 / ちょうどお姫様もいるようだしね。  [voice 16174]
    voice "ch8_w_009"
    w "I'll just finish this here on the rooftop. It's fortunate that the Princess is here. {#ch8_w_009}"
    # JA[16174]: ウェザリー：このまま屋上で始末してあげるよ。 / ちょうどお姫様もいるようだしね。
    # ルイズ：おあいにくさま。 / だったらわたし達が、 / あなた達を倒してみせるわ。  [voice 7472]
    voice "ch8_l_066"
    l "Fine then. If you won't stop, then we'll defeat you. {#ch8_l_066}"
    # JA[7472]: ルイズ：おあいにくさま。 / だったらわたし達が、 / あなた達を倒してみせるわ。
    # アキナ：へえ、できるのかい？ / あたしの爆弾に、ウェザリー様の魔法。 / 勝てるもんならやってみな。  [voice 259]
    voice "ch8_ak_002"
    ak "My bomb, and Weatherby-sama's magic — try to beat that if you can. {#ch8_ak_002}"
    # JA[259]: アキナ：へえ、できるのかい？ / あたしの爆弾に、ウェザリー様の魔法。 / 勝てるもんならやってみな。
    # アンリエッタ：そこまでです！  [voice 924]
    voice "ch8_h_073"
    h "That's enough. {#ch8_h_073}"
    # JA[924]: アンリエッタ：そこまでです！
    # アキナ：あ……っ。  [voice 260]
    voice "ch8_ak_003"
    ak "Ah…! {#ch8_ak_003}"
    # JA[260]: アキナ：あ……っ。
    # ウェザリー：なにっ！？  [voice 16175]
    voice "ch8_w_010"
    w "What!? {#ch8_w_010}"
    # JA[16175]: ウェザリー：なにっ！？
    # サイト：春奈！？  [voice 13663]
    voice "ch8_s_103"
    s "Haruna!? {#ch8_s_103}"
    # JA[13663]: サイト：春奈！？
    # アンリエッタ：その子を確保してください、早く！  [voice 925]
    voice "ch8_h_074"
    h "Secure that child! Quickly! {#ch8_h_074}"
    # JA[925]: アンリエッタ：その子を確保してください、早く！
    # サイト：え？ / あ、はいっ！  [voice 13664]
    voice "ch8_s_104"
    s "Huh? Ah, yes! {#ch8_s_104}"
    # JA[13664]: サイト：え？ / あ、はいっ！
    # ウェザリー：……っ！  [voice 16176]
    voice "ch8_w_011"
    w "…! {#ch8_w_011}"
    # JA[16176]: ウェザリー：……っ！
    # サイト：春奈！ / あ、いや、まだアキナか？ / とにかく、無事か？  [voice 13665]
    voice "ch8_s_105"
    s "Haruna! Or is it Akina? Anyway, is everyone safe? {#ch8_s_105}"
    # JA[13665]: サイト：春奈！ / あ、いや、まだアキナか？ / とにかく、無事か？
    # ハルナ：う……ううん……。  [voice 2639]
    voice "ch8_ha_001"
    ha "Un… unnn… {#ch8_ha_001}"
    # JA[2639]: ハルナ：う……ううん……。
    # キュルケ：どうやら無事のようね。  [voice 3874]
    voice "ch8_k_017"
    k "Looks like we're all safe, then. {#ch8_k_017}"
    # JA[3874]: キュルケ：どうやら無事のようね。
    # アンリエッタ：あなたの魔法 / 「ブレインウォッシュ・ハウリング」は、 / ここでは通用しません。  [voice 926]
    voice "ch8_h_075"
    h "Your magic, ‘Brainwash Howling’, doesn't work here. {#ch8_h_075}"
    # JA[926]: アンリエッタ：あなたの魔法 / 「ブレインウォッシュ・ハウリング」は、 / ここでは通用しません。
    # アンリエッタ：わたくしがいる限り、絶対に。  [voice 927]
    voice "ch8_h_076"
    h "As long as I am here, it's absolutely impossible. {#ch8_h_076}"
    # JA[927]: アンリエッタ：わたくしがいる限り、絶対に。
    # ウェザリー：なぜ……。 / どうしてお前が、この技を解除できる？  [voice 16177]
    voice "ch8_w_012"
    w "Why… how are you able to dispel it? {#ch8_w_012}"
    # JA[16177]: ウェザリー：なぜ……。 / どうしてお前が、この技を解除できる？
    # ウェザリー：これは、わたしが一族から学んだ秘術のはず！ / お前ごときに破れるはずがない！  [voice 16178]
    voice "ch8_w_013"
    w "This is a secret art passed down in my family! It shouldn't be breakable by someone like you! {#ch8_w_013}"
    # JA[16178]: ウェザリー：これは、わたしが一族から学んだ秘術のはず！ / お前ごときに破れるはずがない！
    # アンリエッタ：それが、破れるのですよ。 / あなたが人には聞くことのできない音で、 / 指示を出しているのは分かっています。  [voice 928]
    voice "ch8_h_077"
    h "That it can be broken, I knew. I knew you were communicating through a sound that humans cannot hear. {#ch8_h_077}"
    # JA[928]: アンリエッタ：それが、破れるのですよ。 / あなたが人には聞くことのできない音で、 / 指示を出しているのは分かっています。
    # アンリエッタ：わたくしが魔法を使って、 / その音を聞こえなくさせているだけです。  [voice 929]
    voice "ch8_h_078"
    h "I simply used magic to make that sound inaudible. {#ch8_h_078}"
    # JA[929]: アンリエッタ：わたくしが魔法を使って、 / その音を聞こえなくさせているだけです。
    # ウェザリー：う、嘘だ……嘘だ！ / この魔法はわたしの一族にしか使えない / 特別なもの！  [voice 16179]
    voice "ch8_w_014"
    w "No, that's a lie…! This magic is a special art that only my family can use! {#ch8_w_014}"
    # JA[16179]: ウェザリー：う、嘘だ……嘘だ！ / この魔法はわたしの一族にしか使えない / 特別なもの！
    # ウェザリー：対処法をそうそう知られてるはずがない！！  [voice 16180]
    voice "ch8_w_015"
    w "How could you possibly know how to counter it?! {#ch8_w_015}"
    # JA[16180]: ウェザリー：対処法をそうそう知られてるはずがない！！
    # ウェザリー：お前、なぜ……どうやって知った！？ / まさか、村を……一族を襲って / むりやり聞き出したのか！？  [voice 16181]
    voice "ch8_w_016"
    w "Why… how did you know?! Did you raid your own village…? {#ch8_w_016}"
    # JA[16181]: ウェザリー：お前、なぜ……どうやって知った！？ / まさか、村を……一族を襲って / むりやり聞き出したのか！？
    # サイト：（村？ / 　ウェザリーの生まれた村が、 / 　この技を伝えていたのか？）
    # → no voice; internal thought.
    # アンリエッタ：ミス・ウェザリー、 / あなたが貴族の身分を剥奪されたのは、 / あなたの出自とは関係ありません。  [voice 931]
    voice "ch8_h_079"
    h "Miss Weatherby, your loss of nobility was not because of your origins. {#ch8_h_079}"
    # JA[931]: アンリエッタ：ミス・ウェザリー、 / あなたが貴族の身分を剥奪されたのは、 / あなたの出自とは関係ありません。
    # ウェザリー：なに……？  [voice 16182]
    voice "ch8_w_017"
    w "What…? {#ch8_w_017}"
    # JA[16182]: ウェザリー：なに……？
    # アンリエッタ：魔法によって人の心を操る……。 / 非人道的であるがゆえに禁忌とされた / 技を使用したためです。  [voice 932]
    voice "ch8_h_080"
    h "You used a forbidden magic that manipulates the heart, which was deemed inhuman. {#ch8_h_080}"
    # JA[932]: アンリエッタ：魔法によって人の心を操る……。 / 非人道的であるがゆえに禁忌とされた / 技を使用したためです。
    # アンリエッタ：あなたが貴族であった時分、出自によって / 迫害を受けたことは事実でしょうし、 / それについては同情をします。  [voice 933]
    voice "ch8_h_081"
    h "You were persecuted in your noble years because of your origins. I understand and sympathize. {#ch8_h_081}"
    # JA[933]: アンリエッタ：あなたが貴族であった時分、出自によって / 迫害を受けたことは事実でしょうし、 / それについては同情をします。
    # アンリエッタ：しかし、あなたは禁忌を破り、 / 人の心をもてあそぼうとしたのです。  [voice 934]
    voice "ch8_h_082"
    h "But you broke the taboo and attempted to toy with the hearts of others. {#ch8_h_082}"
    # JA[934]: アンリエッタ：しかし、あなたは禁忌を破り、 / 人の心をもてあそぼうとしたのです。
    # アンリエッタ：それは、いかなる理由があろうと / 許されない罪です。 / だから、あなたは貴族の資格を失ったのです。  [voice 935]
    voice "ch8_h_083"
    h "That is a crime for which there is no excuse, and so you have lost your noble status. {#ch8_h_083}"
    # JA[935]: アンリエッタ：それは、いかなる理由があろうと / 許されない罪です。 / だから、あなたは貴族の資格を失ったのです。
    # ウェザリー：そんな……わたしが会得した一族の技が、 / 仇になったっていうの……。  [voice 16183]
    voice "ch8_w_018"
    w "How… I can't believe the secret art of my family would be turned against me… {#ch8_w_018}"
    # JA[16183]: ウェザリー：そんな……わたしが会得した一族の技が、 / 仇になったっていうの……。
    # アンリエッタ：人心を操る禁忌の技の存在は、 / 脅威です。 / それゆえ、王家の者や軍の一部では、 / この技を破るための研究もおこなわれていました。  [voice 936]
    voice "ch8_h_084"
    h "The existence of the forbidden heart-manipulating magic is a threat. That's why research was conducted by some of the royal family and military. {#ch8_h_084}"
    # JA[936]: アンリエッタ：人心を操る禁忌の技の存在は、 / 脅威です。 / それゆえ、王家の者や軍の一部では、 / この技を破るための研究もおこなわれていました。
    # アンリエッタ：わたくしが民を守るため学んだのは、そのひとつ。 / あなたの技は、もはや効きません。  [voice 937]
    voice "ch8_h_085"
    h "What I learned to protect my people was that. Your magic no longer works. {#ch8_h_085}"
    # JA[937]: アンリエッタ：わたくしが民を守るため学んだのは、そのひとつ。 / あなたの技は、もはや効きません。
    # ウェザリー：く、くくくっ。 / 一族の秘術を封じられた今は、 / 力攻めあるのみか。  [voice 16184]
    voice "ch8_w_019"
    w "Heh heh heh… Now that my family's secret is sealed, the only option is to overpower with force. {#ch8_w_019}"
    # JA[16184]: ウェザリー：く、くくくっ。 / 一族の秘術を封じられた今は、 / 力攻めあるのみか。
    # ウェザリー：ならばせめて、相討ちになってでも、 / 女王を討ち取ってくれる！  [voice 16185]
    voice "ch8_w_020"
    w "Then at least let me take the queen down with me, even if we both die! {#ch8_w_020}"
    # JA[16185]: ウェザリー：ならばせめて、相討ちになってでも、 / 女王を討ち取ってくれる！
    # ウェザリー：ゆくぞ！ / 我が無念と怒りの牙と爪、 / その身に受けてみるがいい！！  [voice 16186]
    voice "ch8_w_021"
    w "Come then! All I have left are the fangs and claws of my resentment and rage! Take this!! {#ch8_w_021}"
    # JA[16186]: ウェザリー：ゆくぞ！ / 我が無念と怒りの牙と爪、 / その身に受けてみるがいい！!
    # サイト：やっぱり戦うしかないのか。  [voice 13666]
    voice "ch8_s_106"
    s "I guess we really have to fight then. {#ch8_s_106}"
    # JA[13666]: サイト：やっぱり戦うしかないのか。
    # サイト：くっ、これで最後にするぞ、デルフ！  [voice 13667]
    voice "ch8_s_107"
    s "No more games, Derflinger! This is it! {#ch8_s_107}"
    # JA[13667]: サイト：くっ、これで最後にするぞ、デルフ！
    # デルフリンガー：あいよ、相棒っ！  [voice 1374]
    voice "ch8_d_003"
    d "All right, partner! {#ch8_d_003}"
    # JA[1374]: デルフリンガー：あいよ、相棒っ！
    # → next scene 428

    # ==== SCENE 428 ====
    # [BG       stage    image=+71, level=200 → id(71)]
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25 → t25]
    play music t25 fadein 1.0
    # [SPRITE   lay20    image=+1065, level=160, dir=1A]  # ウェザリー
    # ウェザリー：くはっ！  [voice 16187]
    voice "ch8_w_022"
    w "Kuahh! {#ch8_w_022}"
    # JA[16187]: ウェザリー：くはっ！
    # [SPRITE   lay20    hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]  # サイト
    # サイト：ここまでだ、ウェザリー。 / お前の負けだ。  [voice 13668]
    voice "ch8_s_108"
    s "That's enough, Weatherby. You're defeated. {#ch8_s_108}"
    # JA[13668]: サイト：ここまでだ、ウェザリー。 / お前の負けだ。
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay20    image=+1063, level=160, dir=1A]
    # ウェザリー：……ふ、ふふふっ。  [voice 16188]
    voice "ch8_w_023"
    w "Heh heh heh… {#ch8_w_023}"
    # JA[16188]: ウェザリー：……ふ、ふふふっ。
    # ウェザリー：まさか、未熟と侮っていた女王に負けるとは、 / 思ってもみなかった。  [voice 16189]
    voice "ch8_w_024"
    w "I never imagined I'd be defeated by a queen I looked down on as inexperienced!{#ch8_w_024}"
    # JA[16189]: ウェザリー：まさか、未熟と侮っていた女王に負けるとは、 / 思ってもみなかった。
    # サイト：ウェザリー……。  [voice 13669]
    voice "ch8_s_116"
    s "Weatherby… {#ch8_s_116}"
    # JA[13669]: サイト：ウェザラー。
    # ウェザラー：さあ、敗者に情けは無用。 / 生き恥をさらこうとは思わないわ。 / ひ Thought it to the finishing blow.  [voice 16190]
    voice "ch8_w_025"
    w "Then at this point, no mercy for the defeated! I won't live in shame — finish me off with one blow! {#ch8_w_025}"
    # JA[16190]: ウェザラー：さあ、敗者に情けは無用。 / 生き恥をさらこうとは思わないわ。 / ひ Thought it to the finishing blow.
    # サイト：お姫さま、どうします？  [voice 13670]
    voice "ch8_s_117"
    s "What should the Princess do? {#ch8_s_117}"
    # JA[13670]: サイト：お姫さま、どうします？
    # アンリエッタ：ミス・ウェザリー。 / あなたには、自分の罪を償ってもらいます。  [voice 938]
    voice "ch8_h_086"
    h "Miss Weatherby. You will pay for your sins. {#ch8_h_086}"
    # JA[938]: アンリエッタ：ミス・ウェザラー。 / あなたには、自分の罪を償ってもらいます。
    # ウェザラー：それはもう覚悟してるわ。 / 好きにしなさい。  [voice 16191]
    voice "ch8_w_026"
    w "I know. Do what you will. {#ch8_w_026}"
    # JA[16191]: ウェザラー：それはもう覚悟してるわ。 / 好きにしなさい。
    # アンリエッタ：分かりました。 / 処分は後ほどお伝えします。  [voice 939]
    voice "ch8_h_087"
    h "Understood. I'll inform you of the punishment later. {#ch8_h_087}"
    # JA[939]: アンリエッタ：分かりました。 / 処分は後ほどお伝えします。
    # アンリエッタ：次はルイズ、あなたの番ですね。 / 力を見せてください。  [voice 940]
    voice "ch8_h_088"
    h "Next is your turn, Louise. Show me your power. {#ch8_h_088}"
    # JA[940]: アンリエッタ：次はルイズ、あなたの番ですね。 / 力を見せてください。
    # ルイズ：はい。 / お任せください。  [voice 7473]
    voice "ch8_l_067"
    l "Yes. Leave it to me. {#ch8_l_067}"
    # JA[7473]: ルイズ：はい。 / お任せください。
    # ルイズ：出でよ、ここになきもの……ここにあるように。  [voice 7474]
    voice "ch8_l_068"
    l "Come forth, you who are not here… be as though you were here. {#ch8_l_068}"
    # JA[7474]: ルイズ：出でよ、ここになきもの……ここにあるように。
    # ルイズ：イリュージョン！！  [voice 7475]
    voice "ch8_l_069"
    l "Illusion!! {#ch8_l_069}"
    # JA[7475]: ルイズ：イリュージョン！！
    # アンリエッタ：ああ……！  [voice 941]
    voice "ch8_h_089"
    h "Oh…! {#ch8_h_089}"
    # JA[941]: アンリエッタ：ああ……！
    # サイト：え……！？  [voice 13671]
    voice "ch8_s_109"
    s "Eh…!? {#ch8_s_109}"
    # JA[13671]: サイト：え……！？
    # サイト：あれは……トリステインの空中艦隊！？  [voice 13672]
    voice "ch8_s_110"
    s "Was that… the Tristain aerial fleet!? {#ch8_s_110}"
    # JA[13672]: サイト：あれは……トリステインの空中艦隊！？
    # ルイズ：違うわよ……ばか……。  [voice 7476]
    voice "ch8_l_070"
    l "No, it's not… Idiot. {#ch8_l_070}"
    # JA[7476]: ルイズ：違うわよ……ばか……。
    # アンリエッタ：ああ、ルイズ……。 / これは、イリュージョンなのね。 / 実体なき幻を出現させる魔法……。  [voice 942]
    voice "ch8_h_090"
    h "Oh, Louise… This is Illusion. It's magic that manifests incorporeal illusions… {#ch8_h_090}"
    # JA[942]: アンリエッタ：ああ、ルイズ……。 / これは、イリュージョンなのね。 / 実体なき幻を出現させる魔法……。
    # サイト：ってことは、あの艦隊は幻？  [voice 13673]
    voice "ch8_s_111"
    s "So that fleet was an illusion? {#ch8_s_111}"
    # JA[13673]: サイト：ってことは、あの艦隊は幻？
    # ルイズ：そういうこと……。 / どう？ / わたしの魔法は？  [voice 7477]
    voice "ch8_l_071"
    l "So it was… Then? / So, what about my magic? {#ch8_l_071}"
    # JA[7477]: ルイズ：そういうこと……。 / どう？ / わたしの魔法は？
    # サイト：ああ、十分すぎるほどさ！ / レコン・キスタの艦隊は退却し始めてるし、 / 地上の砲台も、騒がしいことになってるぜ。  [voice 13674]
    voice "ch8_s_112"
    s "Yeah, that's more than enough! The Reconquista fleet has started retreating, and the ground cannons are getting noisy. {#ch8_s_112}"
    # JA[13674]: サイト：ああ、十分すぎるほどさ！ / レコン・キスタの艦隊は退却し始めてるし、 / 地上の砲台も、騒がしいことになってるぜ。
    # アンリエッタ：敵の動揺を見た各部隊が、 / 突入を開始したようですね。 / これで、勝敗は決しました。  [voice 943]
    voice "ch8_h_091"
    h "The troops who saw the enemy's confusion have launched their assault. With this, the battle is decided. {#ch8_h_091}"
    # JA[943]: アンリエッタ：敵の動揺を見た各部隊が、 / 突入を開始したようですね。 / これで、勝敗は決しました。
    # ルイズ：そう……良かった……。  [voice 7478]
    voice "ch8_l_072"
    l "Yes… That's good… {#ch8_l_072}"
    # JA[7478]: ルイズ：そう……良かった……。
    # サイト：うわっ。 / ルイズ、突然倒れてどうしたんだよ。  [voice 13675]
    voice "ch8_s_113"
    s "Whoa. What's wrong with Louise? She just collapsed? {#ch8_s_113}"
    # JA[13675]: サイト：うわっ。 / ルイズ、突然倒れてどうしたんだよ。
    # サイト：（そっか、虚無の魔法は、 / 　精神力をめちゃくちゃ消費するんだっけ……）
    # → no voice; internal thought.
    # サイト：ルイズ、お疲れ様。 / 後のことは任せて、少し休めよ。  [voice 13676]
    voice "ch8_s_114"
    s "Louise, you're exhausted. Rest now; the rest is on us. {#ch8_s_114}"
    # JA[13676]: サイト：ルイズ、お疲れ様。 / 後のことは任せて、少し休めよ。
    # ルイズ：……うん。 / ちょっぴり疲れちゃった……。  [voice 7479]
    voice "ch8_l_073"
    l "…Yeah. I'm a bit tired… {#ch8_l_073}"
    # JA[7479]: ルイズ：……うん。 / ちょっぴり疲れちゃった……。
    # アンリエッタ：ルイズ……そして使い魔さん、ありがとう。 / あなたがたのおかげで、この国は救われました。  [voice 944]
    voice "ch8_h_092"
    h "Louise… and my familiars, thank you. Thanks to you, this country was saved. {#ch8_h_092}"
    # JA[944]: アンリエッタ：ルイズ……そして使い魔さん、ありがとう。 / あなたがたのおかげで、この国は救われました。
    # アンリエッタ：そしてわたくしも……。  [voice 945]
    voice "ch8_h_093"
    h "And I… also… {#ch8_h_093}"
    # JA[945]: アンリエッタ：そしてわたくしも……。
    # サイト：え？  [voice 13677]
    voice "ch8_s_115"
    s "What? {#ch8_s_115}"
    # JA[13677]: サイト：え？
    # アンリエッタ：い、いえ。 / さあ、これから激務になりそうですね。  [voice 946]
    voice "ch8_h_094"
    h "Oh, no. Well, it seems we'll have a lot of work ahead of us now. {#ch8_h_094}"
    # JA[946]: アンリエッタ：い、いえ。 / さあ、これから激務になりそうですね。
    # アンリエッタ：怪我人の収容、壊れた建物の再建……。 / 今すぐ思いつかないほど、やるべき事はたくさん / あります。  [voice 947]
    voice "ch8_h_095"
    h "Casualty care, rebuilding damaged buildings… There are so many things to do, more than I can think of now. {#ch8_h_095}"
    # JA[947]: アンリエッタ：怪我人の収容、壊れた建物の再建……。 / 今すぐ思いつかないほど、やるべき事はたくさん / あります。
    # アンリエッタ：でも……。 / わたくしはもう逃げようなんて思いません。 / わたくしは……この国の女王なのですから。  [voice 948]
    voice "ch8_h_096"
    h "But… I will not run away. I am… the queen of this country. {#ch8_h_096}"
    # JA[948]: アンリエッタ：でも……。 / わたくしはもう逃げようなんて思いません。 / わたくしは……この国の女王なのですから。
    # → next scene 430 (chapter end → jump attention)
    jump attention
