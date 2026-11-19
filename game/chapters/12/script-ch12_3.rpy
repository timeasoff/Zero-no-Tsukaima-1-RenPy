# Глава 12, часть 3 (сцены 535–543): разоблачение, иллюзия, «женитьба».
# Источник: ps2_source/chapters/chapter_13_もう一人のハルナ.txt (SCENE 535-543).

label ch12_3:
    $ tndl(None)
    $ show_sprites()

label ch12_3_scene_535:

    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [EVENT_CG event    image=+139, level=80]
    $ dissolve_fx("id(139)")
    # サイト：アキナ！  [voice 13361]
    voice "ch12_s_065"
    s "Akina!{#ch12_s_065}"

    # アキナ：な、なんだよ、サイト！  [voice 245]
    voice "ch12_ak_049"
    ak "W-What, Saito!?{#ch12_ak_049}"

    # サイト：ウェザリーがなんだっていうんだ！
    voice "ch12_s_066"
    s "What's Weatherly to you!? She's only using you!{#ch12_s_066}"

    # サイト：そんなことに利用されるのはやめろよ。
    voice "ch12_s_067"
    s "Stop letting her use you like that. Is there anything good in staying there?{#ch12_s_067}"

    # アキナ：いいこと？
    voice "ch12_ak_050"
    ak "Good? What do you know about Weatherly-sama?{#ch12_ak_050}"

    # → next scene 537
    jump ch12_3_scene_537

label ch12_3_scene_536:

    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [EVENT_CG event    image=+139, level=80]
    $ dissolve_fx("id(139)")
    # サイト：ウェザリー！
    voice "ch12_s_068"
    s "Weatherly! How could you do this to Haruna…!{#ch12_s_068}"

    # ウェザリー：この子が生きるには必要だったのよ。  [voice 16122]
    voice "ch12_w_003"
    w "It was necessary for this girl to survive.{#ch12_w_003}"

    # サイト：なんだと！  [voice 13365]
    voice "ch12_s_069"
    s "What!?{#ch12_s_069}"

    # → next scene 537
    jump ch12_3_scene_537

label ch12_3_scene_537:

    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [EVENT_CG event    image=+139, level=80]
    $ dissolve_fx("id(139)")
    # サイト：ウェザリー……。
    voice "ch12_s_070"
    s "Weatherly… Why! For the likes of Reconquista…!{#ch12_s_070}"

    # ウェザリー：こちらにも事情があるの。
    voice "ch12_w_004"
    w "I have my own circumstances. I won't make excuses.{#ch12_w_004}"

    # ウェザリー：わたしはわたしの意思と事情で
    voice "ch12_w_005"
    w "I used Haruna and you by my own will and for my own reasons.{#ch12_w_005}"

    # ウェザリー：わたし達を止めたければ、
    voice "ch12_w_006"
    w "If you want to stop us, then stop us with your own power!{#ch12_w_006}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay21    hide]
    # [SPRITE   lay20    hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay21    image=+1044, level=140, dir=2A]
    # ハルナ：え、えい……！  [voice 2631]
    voice "ch12_ha_020"
    ha "E-Eii…!{#ch12_ha_020}"

    # [SE       se0      play=+62]
    # ウェザリー：きゃぁぁぁぁっ！  [voice 16126]
    voice "ch12_w_007"
    w "Kyaaaa!{#ch12_w_007}"

    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：へっ……？  [voice 13367]
    voice "ch12_s_071"
    s "Heh…?{#ch12_s_071}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：あ、ああああ……あたしは何を……。
    voice "ch12_ak_051"
    ak "A-Aaaa… what did I…? Was that Haruna's doing!?{#ch12_ak_051}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：ウェ、ウェザリーは！？
    voice "ch12_l_068"
    l "W-Weatherly!? Did she fall!?{#ch12_l_068}"

    # サイト：（……マ、マジ？
    s "(N-No way. Did she just fall?){#ch12_s_072}"

    # サイト：（こ、こんな城のてっぺんから落ちたら
    s "(F-From the top of a castle like this—even a Halkeginian wouldn't survive…){#ch12_s_073}"

    # ウェザリー：な、何をするの！
    voice "ch12_w_008"
    w "W-What are you doing! Haruna! …No, Akina!{#ch12_w_008}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：え？
    voice "ch12_s_074"
    s "Eh? She's alive?{#ch12_s_074}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：とっさに出窓に捕まったのよ！  [voice 7289]
    voice "ch12_l_069"
    l "She caught hold of a bay window just in time!{#ch12_l_069}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：ウ、ウェザリー様！
    voice "ch12_ak_052"
    ak "W-Weatherly-sama! Hold on tight!{#ch12_ak_052}"

    # [SPRITE   lay21    x=224, y=0]
    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # ウェザリー：そうか、そういうことか……。
    voice "ch12_w_009"
    w "So that's how it is… That she can bring her consciousness to the surface… I can't believe it.{#ch12_w_009}"

    # [SPRITE   lay20    image=+1067, level=160, dir=1A]
    # ウェザリー：くそ、今のショックで、
    voice "ch12_w_010"
    w "Damn, the shock has ruined my spell… Just when I needed it…{#ch12_w_010}"

    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：ハルナには、後でもっと強力な術を
    voice "ch12_w_011"
    w "I'll put a stronger spell on Haruna later. One that keeps her consciousness under forever…{#ch12_w_011}"

    # [SPRITE   lay21    hide]
    # [SE       se0      play=+65]
    # [SPRITE   lay20    level=152]
    # [SPRITE   lay5     image=+471, level=150, dir=3B]
    # サイト：させるか！  [voice 13369]
    voice "ch12_s_075"
    s "Like hell you will!{#ch12_s_075}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay20    hide]
    # [SPRITE   lay20    image=+1088, level=132, dir=2A]
    # ウェザリー：あなた達……覚悟しなさい！  [voice 16131]
    voice "ch12_w_012"
    w "You two… brace yourselves!{#ch12_w_012}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay20    hide]
    # [SPRITE   lay7     hide]
    # [BG       stage    hide]
    # → next scene 538
    jump ch12_3_scene_538

label ch12_3_scene_538:

    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # ウェザリー：ぐぅっ！
    voice "ch12_w_013"
    w "Ugh! It's over, is it. Damn, I was so close…{#ch12_w_013}"

    # [SPRITE   lay20    x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：おとなしく縛につきなさい！  [voice 7290]
    voice "ch12_l_070"
    l "Be quiet and let yourself be bound!{#ch12_l_070}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：……。  [voice 16133]
    voice "ch12_w_014"
    w "…{#ch12_w_014}"

    # [SPRITE   lay20    image=+1063, level=160, dir=1A]
    # ウェザリー：ふっ。
    voice "ch12_w_015"
    w "Hah. It seems the roles have reversed, haven't they?{#ch12_w_015}"

    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：今度はサイト達が追う側で、
    voice "ch12_w_016"
    w "Now Saito and the others are chasing, and I'm the one cornered…{#ch12_w_016}"

    # ウェザリー：なれば、わたしは台本どおりに
    voice "ch12_w_017"
    w "Then I'll play my part as the script demands.{#ch12_w_017}"

    # [SPRITE   lay20    x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：まて、ウェザリー！  [voice 13370]
    voice "ch12_s_076"
    s "Wait, Weatherly!{#ch12_s_076}"

    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # ウェザリー：さらばだ。  [voice 16137]
    voice "ch12_w_018"
    w "Farewell.{#ch12_w_018}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ウェザリー！  [voice 7291]
    voice "ch12_l_071"
    l "Weatherly!{#ch12_l_071}"

    # サイト：（ま、待てよ。
    s "(W-Wait. From this height, she won't survive…){#ch12_s_077}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：ウェザリー様……。  [voice 249]
    voice "ch12_ak_053"
    ak "Weatherly-sama…{#ch12_ak_053}"

    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：……。  [voice 13371]
    voice "ch12_s_078"
    s "…{#ch12_s_078}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+140, level=80]
    $ dissolve_fx("id(140)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：サイト、これも戦いなの。
    voice "ch12_l_072"
    l "Saito, this is a battle too. I'll use the power of Void. Watch Akina, all right?{#ch12_l_072}"

    # サイト：ああ……。  [voice 13372]
    voice "ch12_s_079"
    s "Ah…{#ch12_s_079}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # ルイズ：イリュージョン！！  [voice 7293]
    voice "ch12_l_073"
    l "Illusion!!{#ch12_l_073}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+141, level=80]
    $ dissolve_fx("id(141)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # サイト：な、なんだ！
    voice "ch12_s_080"
    s "W-What! An entire aerial fleet out of the clouds…!{#ch12_s_080}"

    # サイト：まさか、あれが幻だっていうのか？  [voice 13374]
    voice "ch12_s_081"
    s "You don't mean that's an illusion!?{#ch12_s_081}"

    # ルイズ：そうよ……。
    voice "ch12_l_074"
    l "That's right… An entirely false fleet…{#ch12_l_074}"

    # サイト：敵の兵士が砲台から次々と逃げ出しているぞ。  [voice 13375]
    voice "ch12_s_082"
    s "The enemy soldiers are fleeing the cannons one after another.{#ch12_s_082}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：良かった……。
    voice "ch12_l_075"
    l "Thank goodness… This battle is over… at last.{#ch12_l_075}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：ああ……。
    voice "ch12_s_083"
    s "Ah… Louise, get some rest. Void takes a lot of mental energy, doesn't it?{#ch12_s_083}"

    # ルイズ：うん、そうする。
    voice "ch12_l_076"
    l "Mm, I will. Phew… I'm a little… tired.{#ch12_l_076}"

    # サイト：お疲れ……ルイズ。  [voice 13377]
    voice "ch12_s_084"
    s "Good work… Louise.{#ch12_s_084}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=4000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 544
    jump ch12_4

label ch12_3_scene_539:

    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1173, level=200]
    $ fade_fx("id(1173)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [SE       se1      play=+37]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：はあ、どうもお城の中っていうのは
    voice "ch12_s_085"
    s "Phew, being inside a castle really makes my shoulders stiff.{#ch12_s_085}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：さてと、春奈は元気かな？
    voice "ch12_s_086"
    s "Well now, I wonder how Haruna's doing? Maybe it's Akina right now.{#ch12_s_086}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ややこしいな。  [voice 8093]
    voice "ch12_s_087"
    s "This is confusing.{#ch12_s_087}"

    # サイト：（正式には王宮の侍女となった春奈は、
    s "(Officially, Haruna became a palace maid. While acting as Akina's garden keeper, she resumed her maid training…){#ch12_s_088}"

    # サイト：（もっぱら王宮の皿や壺の破壊活動に
    s "(Rumor has it she spends most of her time destroying palace plates and vases…){#ch12_s_089}"

    # サイト：（最初は笑っていたお姫さまも、
    s "(Even the Princess, who laughed at first, is said to be clutching her head lately…){#ch12_s_090}"

    # [SPRITE   lay5     hide]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # サイト：（あ、ポニーテール……。
    s "(Ah, a ponytail… Which means…){#ch12_s_091}"

    # サイト：（今はアキナか……）
    s "(So right now it's Akina…){#ch12_s_092}"

    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：やあ、アキナ。
    voice "ch12_s_093"
    s "Hey, Akina. Doing well?{#ch12_s_093}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：……。
    ak "…{#ch12_ak_054}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：よ、よお、サイト。  [voice 0]
    # voice id 0 — нет аудио, строка voice пропущена
    ak "H-Hey, Saito.{#ch12_ak_055}"

    # アキナ：あいかわらずバカ面を下げているわね。  [voice 1]
    voice "ch12_ak_056"
    ak "You're still wearing that stupid face, aren't you.{#ch12_ak_056}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ど、どうかしたのか？
    voice "ch12_s_094"
    s "W-What's wrong? You're awfully worked up.{#ch12_s_094}"

    # サイト：（と、いうか……、なんかしゃべり方が変だ）
    s "(I mean… your way of talking is strange.){#ch12_s_095}"

    # アキナ：そ、そうだっけ？
    voice "ch12_ak_057"
    ak "R-Really? I'm always like this.{#ch12_ak_057}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：あれ？
    voice "ch12_s_096"
    s "Huh? You stopped saying 'atashi'?{#ch12_s_096}"

    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：な、なに言ってるんだよ！
    voice "ch12_ak_058"
    ak "W-What are you talking about! I'm still me!{#ch12_ak_058}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：つ、つまんないこと言ってないでさ。
    voice "ch12_ak_059"
    ak "D-Don't say boring things. I have something important to tell you today!{#ch12_ak_059}"

    # サイト：大切な話？  [voice 8097]
    voice "ch12_s_097"
    s "Important?{#ch12_s_097}"

    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：そ、そうだよ！
    voice "ch12_ak_060"
    ak "T-That's right! Important!{#ch12_ak_060}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+126, level=80]
    $ dissolve_fx("id(126)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+16]
    play music t15 fadein 1.0
    # サイト：いてっ！
    voice "ch12_s_098"
    s "Ouch! If it's important, don't shove me down all of a sudden…{#ch12_s_098}"

    # サイト：（アキナの体が間近に……。
    s "(Akina's body is right against me… Damn. Why is my heart racing…){#ch12_s_099}"

    # アキナ：はやくハルナに求婚してやれ！  [voice 6]
    voice "ch12_ak_061"
    ak "Hurry up and propose to Haruna!{#ch12_ak_061}"

    # サイト：ああ、求婚を……。  [voice 8099]
    voice "ch12_s_100"
    s "Ah, propose to…{#ch12_s_100}"

    # サイト：……。  [voice 8100]
    voice "ch12_s_101"
    s "…{#ch12_s_101}"

    # サイト：……。
    voice "ch12_s_102"
    s "…{#ch12_s_102}"

    # サイト：……キュウコン？  [voice 8102]
    voice "ch12_s_103"
    s "…Kyukon?{#ch12_s_103}"

    # サイト：……あの、アキナさん？
    voice "ch12_s_104"
    s "Um, Akina-san? What's a 'Kyukon'?{#ch12_s_104}"

    # [EVENT_CG event    image=+128, level=80]
    $ dissolve_fx("id(128)")
    # アキナ：な、なによ！
    voice "ch12_ak_062"
    ak "W-What's that! It's obvious, isn't it!{#ch12_ak_062}"

    # アキナ：プロポーズよ、プロポーズ！  [voice 8]
    voice "ch12_ak_063"
    ak "A proposal! A proposal!{#ch12_ak_063}"

    # [EVENT_CG event    image=+127, level=80]
    $ dissolve_fx("id(127)")
    # アキナ：つまり、あなたがわたしにアイラブユーよ。  [voice 9]
    voice "ch12_ak_064"
    ak "In other words, you're saying 'I love you' to me!{#ch12_ak_064}"

    # サイト：……。  [voice 8104]
    voice "ch12_s_105"
    s "…{#ch12_s_105}"

    # サイト：……は？  [voice 8105]
    voice "ch12_s_106"
    s "…Huh?{#ch12_s_106}"

    # サイト：ええと、話が良く見えないのですけど？  [voice 8106]
    voice "ch12_s_107"
    s "Um, I'm not following the conversation at all…{#ch12_s_107}"

    # サイト：（いや、見えないわけじゃないけど。
    s "(No, it's not that I don't understand. Akina's still too out there…){#ch12_s_108}"

    # [EVENT_CG event    image=+128, level=80]
    $ dissolve_fx("id(128)")
    # アキナ：……鈍感！
    voice "ch12_ak_065"
    ak "…Idiot! That's why Louise calls you a stupid dog.{#ch12_ak_065}"

    # [EVENT_CG event    image=+126, level=80]
    $ dissolve_fx("id(126)")
    # アキナ：いい、あのね……。  [voice 11]
    voice "ch12_ak_066"
    ak "All right, listen…{#ch12_ak_066}"

    # アキナ：ハ、ハルナは平賀くん……じゃなかった
    voice "ch12_ak_067"
    ak "H-Haruna likes Hiraga-kun… I mean, Saito. That's why she's waiting so faithfully.{#ch12_ak_067}"

    # [EVENT_CG event    image=+127, level=80]
    $ dissolve_fx("id(127)")
    # アキナ：あなたが……サイトが……、
    voice "ch12_ak_068"
    ak "For you… for Saito to propose 'marriage'.{#ch12_ak_068}"

    # サイト：そ、それはどういうご冗談で。  [voice 8107]
    voice "ch12_s_109"
    s "T-That's quite a joke.{#ch12_s_109}"

    # サイト：……っていうか、なんでいきなり結婚？  [voice 8108]
    voice "ch12_s_110"
    s "…And why marriage all of a sudden?{#ch12_s_110}"

    # サイト：ボ、ボクタチは高校生なワケで。  [voice 8109]
    voice "ch12_s_111"
    s "W-We're high school students, you know.{#ch12_s_111}"

    # [EVENT_CG event    image=+126, level=80]
    $ dissolve_fx("id(126)")
    # アキナ：だって、ライバルが多いし……、
    voice "ch12_ak_069"
    ak "But there are lots of rivals… and Mama said you can't even hold hands unless you're married!{#ch12_ak_069}"

    # [EVENT_CG event    image=+128, level=80]
    $ dissolve_fx("id(128)")
    # アキナ：と、とにかく！
    voice "ch12_ak_070"
    ak "A-Anyway! This is Haruna's wish!{#ch12_ak_070}"

    # サイト：い、いまどきそんなのって……。  [voice 8110]
    voice "ch12_s_112"
    s "I-It's not like people do that these days…{#ch12_s_112}"

    # サイト：春奈って前に、自分のことお嬢さんだって
    voice "ch12_s_113"
    s "Haruna said she was a lady before, you know. Maybe she's for real?{#ch12_s_113}"

    # サイト：（なんか、さっきから変だぞ？）
    s "(Something's been off since a while ago…){#ch12_s_114}"

    # サイト：（あれ、そういえば……。
    s "(Ah, now that I think of it… Akina or Haruna…){#ch12_s_115}"

    # サイト：（大切なお皿を割ったときに
    s "(Like when she broke a precious plate and pretended to switch personalities to cover it up…){#ch12_s_116}"

    # サイト：（お茶菓子を分けたりするとき、
    s "(Or when we split sweets and she switched so she'd get two shares…){#ch12_s_117}"

    # サイト：（そんな笑い話を侍女の人から聞いたけど）
    s "(I heard such funny stories from the maids…){#ch12_s_118}"

    # サイト：ま、まさか……。  [voice 8112]
    voice "ch12_s_119"
    s "N-No way…{#ch12_s_119}"

    menu:
        "Is it really Akina's wish?{#ch12_3_c_539_1}":
            jump ch12_3_scene_540
        "Is it really Haruna?{#ch12_3_c_539_2}":
            jump ch12_3_scene_541
        "Who is it really?{#ch12_3_c_539_3}":
            jump ch12_3_scene_542

label ch12_3_scene_540:

    # [BGM      bgm      play=+16]
    play music t15 fadein 1.0
    # [EVENT_CG event    image=+128, level=80]
    $ dissolve_fx("id(128)")
    # サイト：そ、それって、ホントに春奈の望みなの？  [voice 8113]
    voice "ch12_s_120"
    s "S-So that really was Haruna's wish?{#ch12_s_120}"

    # サイト：もしかしたら、アキナの……。  [voice 8114]
    voice "ch12_s_121"
    s "Maybe it was Akina's…{#ch12_s_121}"

    # [EVENT_CG event    image=+127, level=80]
    $ dissolve_fx("id(127)")
    # アキナ：ち、違うわよ！
    voice "ch12_ak_071"
    ak "T-That's not true! Akina may want it too, but so do I!{#ch12_ak_071}"

    # サイト：……へ？  [voice 8115]
    voice "ch12_s_122"
    s "…Huh?{#ch12_s_122}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：……あ？  [voice 1581]
    voice "ch12_ha_021"
    ha "…Eh?{#ch12_ha_021}"

    # ハルナ：……。  [voice 1582]
    voice "ch12_ha_022"
    ha "…{#ch12_ha_022}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：……ひ、ひどぉぉぉい！
    voice "ch12_ak_072"
    ak "…T-That's mean! Disguising yourself as me and saying whatever you like!{#ch12_ak_072}"

    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：……は？  [voice 8116]
    voice "ch12_s_123"
    s "…Huh?{#ch12_s_123}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：ち、違うんだ。
    voice "ch12_ak_073"
    ak "T-No, just now it was Haruna pretending to be me.{#ch12_ak_073}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ちょっと待て、何がどうなってるんだよ！  [voice 8117]
    voice "ch12_s_124"
    s "Hold on, what's going on here!{#ch12_s_124}"

    # サイト：今度のアキナは本物なんだろうな！  [voice 8118]
    voice "ch12_s_125"
    s "This Akina is the real one, right!?{#ch12_s_125}"

    # サイト：どっちがどっちなんだよ！  [voice 8119]
    voice "ch12_s_126"
    s "Which one is which!?{#ch12_s_126}"

    # → next scene 543
    jump ch12_3_scene_543

label ch12_3_scene_541:

    # [BGM      bgm      play=+16]
    play music t15 fadein 1.0
    # [EVENT_CG event    image=+128, level=80]
    $ dissolve_fx("id(128)")
    # サイト：……ホントにアキナ？  [voice 8120]
    voice "ch12_s_127"
    s "…Really Akina?{#ch12_s_127}"

    # サイト：まさか、春奈なんじゃ？  [voice 8121]
    voice "ch12_s_128"
    s "Don't tell me it's Haruna…?{#ch12_s_128}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：……。  [voice 1583]
    voice "ch12_ha_023"
    ha "…{#ch12_ha_023}"

    # [SPRITE   lay7     image=+955, level=160, dir=1A]
    # ハルナ：……はっ、アキナったら！
    voice "ch12_ha_024"
    ha "…Ah, Akina! What are you doing saying such things!{#ch12_ha_024}"

    # [SPRITE   lay7     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：……え、ええっと？  [voice 8122]
    voice "ch12_s_129"
    s "…E-Er…?{#ch12_s_129}"

    # [SPRITE   lay7     image=+986, level=160, dir=2A]
    # ハルナ：ご、ごめんなさい、平賀くん。
    voice "ch12_ha_025"
    ha "S-Sorry, Hiraga-kun. Akina said something stupid!{#ch12_ha_025}"

    # [SPRITE   lay7     image=+992, level=160, dir=2A]
    # ハルナ：ア、アキナも平賀くんのことが好きなの。
    voice "ch12_ha_026"
    ha "A-Akina likes Hiraga-kun too. That's why she said that…{#ch12_ha_026}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そ、そうなのか……。  [voice 8123]
    voice "ch12_s_130"
    s "I-Is that so…{#ch12_s_130}"

    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：そ、そうなの。
    voice "ch12_ha_027"
    ha "Y-Yes. Ahahaha…{#ch12_ha_027}"

    # → next scene 543
    jump ch12_3_scene_543

label ch12_3_scene_542:

    # [BGM      bgm      play=+16]
    play music t15 fadein 1.0
    # [EVENT_CG event    image=+128, level=80]
    $ dissolve_fx("id(128)")
    # サイト：……ホントは誰なの？  [voice 8124]
    voice "ch12_s_131"
    s "…Who are you really?{#ch12_s_131}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：うっ、ええと……あうあう。
    voice "ch12_ha_028"
    ha "Ugh, er… au au… It's Touch.{#ch12_ha_028}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：え、ええと……。  [voice 19]
    voice "ch12_ak_074"
    ak "E-Er…{#ch12_ak_074}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：……じ、実は３人目の「冬奈」だったりして？  [voice 20]
    voice "ch12_ak_075"
    ak "…Could it be a third personality, 'Fuyuna'?{#ch12_ak_075}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay7     image=+986, level=160, dir=2A]
    # ハルナ：そうそう、それよ！  [voice 1589]
    voice "ch12_ha_029"
    ha "That's it, that's it!{#ch12_ha_029}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：い、いいかげんにしろーーっ！  [voice 8125]
    voice "ch12_s_132"
    s "C-Come on, enough alreadyyy!{#ch12_s_132}"

    # → next scene 543
    jump ch12_3_scene_543

label ch12_3_scene_543:

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [BGM      bgm      play=+16]
    play music t15 fadein 1.0
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [SPRITE   lay21    hide]
    # [SPRITE   lay7     x=304, y=416]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：まったく、もう！  [voice 8126]
    voice "ch12_s_133"
    s "Honestly, really!{#ch12_s_133}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：ちょっとあなた達！
    voice "ch12_l_077"
    l "Hey, you two! Sitting next to us, talking about proposals and whatnot…{#ch12_l_077}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：言っておくけど、そういうのはバカ犬の
    voice "ch12_l_078"
    l "Let me tell you, I won't allow that—I'm the stupid dog's mistress!{#ch12_l_078}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     image=+956, level=140, dir=1A]
    # ハルナ：な、なによ～～！  [voice 1590]
    voice "ch12_ha_030"
    ha "W-What!?{#ch12_ha_030}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay21    image=+1022, level=140, dir=1A]
    # アキナ：な、なによ～～！  [voice 21]
    voice "ch12_ak_076"
    ak "W-What!?{#ch12_ak_076}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay8     image=+777, level=160, dir=1B]
    # アンリエッタ：あらあら、女の戦いははじまったばかり
    voice "ch12_h_015"
    h "My my, it seems the fight between the women has only just begun.{#ch12_h_015}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+430, level=140, dir=2A]
    # サイト：勘弁してくださいよ～～。  [voice 8127]
    voice "ch12_s_134"
    s "Spare me…{#ch12_s_134}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ЧАСТИ 3 ====
    jump ch12_4
    return

