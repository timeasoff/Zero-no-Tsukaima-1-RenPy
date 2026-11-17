# Глава 14, часть 4 (сцены 609–618): инфантильная регрессия, решение, тихий финал.
# Источник: ps2_source/chapters/chapter_15_私のお兄ちゃん.txt (SCENE 609-618).

label ch14_4:
    $ tndl(None)
    $ show_sprites()

label ch14_4_scene_609:

    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：（お兄ちゃんと連呼するキュルケを
    s "(We dragged Kirche, who kept calling me 'big brother', back to the inn…){#ch14_s_112}"

    # サイト：（戻ったんだけど……）
    s "(We got back, but…){#ch14_s_113}"

    # [SPRITE   lay5     hide]
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：催眠暗示による幼児退行だって？  [voice 12997]
    voice "ch14_s_114"
    s "Infantile regression from hypnotic suggestion, you say?{#ch14_s_114}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # モンモランシー：ええ、おそらくは。  [voice 4133]
    voice "ch14_m_010"
    m "Yes, most likely.{#ch14_m_010}"

    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # モンモランシー：魔法と、催眠術的な暗示の複合技ね。
    voice "ch14_m_011"
    m "It's a combined technique of magic and hypnotic suggestion. Honestly, it's impressive.{#ch14_m_011}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：じゃあ、ウェザリーの一味がキュルケに……。  [voice 12998]
    voice "ch14_s_115"
    s "So Weatherly's group did something to Kirche…{#ch14_s_115}"

    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # モンモランシー：ええ、おそらく。  [voice 4135]
    voice "ch14_m_012"
    m "Yes, probably.{#ch14_m_012}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：くそっ……。  [voice 12999]
    voice "ch14_s_116"
    s "Damn…{#ch14_s_116}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：でも、なんでキュルケを……。  [voice 7032]
    voice "ch14_l_029"
    l "But why Kirche…{#ch14_l_029}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：たぶん、警告。  [voice 15784]
    voice "ch14_t_006"
    t "Probably a warning.{#ch14_t_006}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……。
    l "…{#ch14_l_030}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch14_t_007}"

    # サイト：……。  [voice 13000]
    voice "ch14_s_117"
    s "…{#ch14_s_117}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：えへへ……。
    voice "ch14_k_085"
    k "Ehehe… Big brother, I love youuu…{#ch14_k_085}"

    # サイト：（あのキュルケをここまでにしてしまう。
    s "(Seeing Kirche like this… This is definitely a warning… What should I do…?){#ch14_s_118}"

    menu:
        "Give in{#ch14_4_c_609_1}":
            jump ch14_4_scene_610
        "Don't give in{#ch14_4_c_609_2}":
            jump ch14_4_scene_611
        "Kirche is cute…{#ch14_4_c_609_3}":
            jump ch14_4_scene_612

label ch14_4_scene_610:

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ルイズ、ここはもう手を……。  [voice 13001]
    voice "ch14_s_119"
    s "Louise, I think we should stop here…{#ch14_s_119}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：引こうなんていうんじゃないでしょうね？
    voice "ch14_l_031"
    l "You're not saying you'd give in to a threat, are you?{#ch14_l_031}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：うっ。
    voice "ch14_s_120"
    s "Ugh. N-No, I…{#ch14_s_120}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：サイト。
    voice "ch14_l_032"
    l "Saito. There are things you must never do.{#ch14_l_032}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：本人の意思に反して、
    voice "ch14_l_033"
    l "Using magic to control someone against their will. That, above all, must never be allowed.{#ch14_l_033}"

    # ルイズ：サイト、あなたが戦いたくないのなら
    voice "ch14_l_034"
    l "Saito, if you don't want to fight, that's fine.{#ch14_l_034}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：でも、わたしは戦う。
    voice "ch14_l_035"
    l "But I will fight. No matter what…{#ch14_l_035}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：わ、分かりました。
    voice "ch14_s_121"
    s "I-I understand. I'll fight too, mistress.{#ch14_s_121}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：そうよ、サイト！
    voice "ch14_l_036"
    l "That's right, Saito! You can't just stand by when a friend is treated like this!{#ch14_l_036}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：賛成。  [voice 15785]
    voice "ch14_t_008"
    t "Agreed.{#ch14_t_008}"

    # → next scene 613
    jump ch14_4_scene_613

label ch14_4_scene_611:

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：確かにこれは脅しだ。
    voice "ch14_s_122"
    s "This is a threat, certainly. But giving in and backing off—I can't do that.{#ch14_s_122}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：サイト……。  [voice 7039]
    voice "ch14_l_037"
    l "Saito…{#ch14_l_037}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：こんなひどいことをする奴らを……。
    voice "ch14_s_123"
    s "People who do such terrible things… can't be allowed to run rampant.{#ch14_s_123}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そうね。
    voice "ch14_l_038"
    l "Right. I can't forgive them either.{#ch14_l_038}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：賛成。  [voice 15786]
    voice "ch14_t_009"
    t "Agreed.{#ch14_t_009}"

    # → next scene 613
    jump ch14_4_scene_613

label ch14_4_scene_612:

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+431, level=160, dir=2A]
    # サイト：（しかし、『おにいちゃん』って慕ってくれる
    s "(Still, Kirche calling me 'big brother' is kind of cute…){#ch14_s_124}"

    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # サイト：（ホント、いつものキュルケもいいけど、
    s "(Honestly, the usual Kirche is nice too, but this Kirche is…){#ch14_s_125}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：サイト！
    voice "ch14_l_039"
    l "Saito! What are you grinning at while looking at Kirche!?{#ch14_l_039}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：はうっ！
    voice "ch14_s_126"
    s "Eep! I-I'm not grinning at all!{#ch14_s_126}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：サイト、本当にやる気あるんでしょうね？  [voice 7042]
    voice "ch14_l_040"
    l "Saito, do you really intend to fight?{#ch14_l_040}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：も、もちろんであります。
    voice "ch14_s_127"
    s "O-Of course, mistress!{#ch14_s_127}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：まったく、もう！  [voice 7043]
    voice "ch14_l_041"
    l "Honestly, really!{#ch14_l_041}"

    # → next scene 613
    jump ch14_4_scene_613

label ch14_4_scene_613:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay5     x=464, y=416]
    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：キュルケのしぐさはかわいいけど、
    voice "ch14_l_042"
    l "Kirche's antics are cute, but it's really throwing me off.{#ch14_l_042}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：普段のミス・ツェルプストーからは、
    voice "ch14_si_006"
    si "It's hard to imagine this from the usual Miss Zerbst—so shy and quiet.{#ch14_si_006}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：うふふ、おにいちゃん。  [voice 3754]
    voice "ch14_k_086"
    k "Ufufu, big brother.{#ch14_k_086}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：まったく、それにしても、
    voice "ch14_l_043"
    l "Honestly, why does that stupid dog get to be 'big brother'!!{#ch14_l_043}"

    # [SPRITE   lay1     x=-96, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：うらやましい？  [voice 15787]
    voice "ch14_t_010"
    t "Jealous?{#ch14_t_010}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：う、うらやましくなんかないわよ！  [voice 7046]
    voice "ch14_l_044"
    l "I-I'm not jealous at all!{#ch14_l_044}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # モンモランシー：時間がかかるかもしれないけど、
    voice "ch14_m_013"
    m "It may take time, but I'll try to make a medicine.{#ch14_m_013}"

    # [SPRITE   lay3     x=-96, y=0]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：なんとかなるのか！
    voice "ch14_s_128"
    s "Can you manage it! Montmon!{#ch14_s_128}"

    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # モンモランシー：保証はできないけどね。  [voice 4137]
    voice "ch14_m_014"
    m "I can't promise anything, though.{#ch14_m_014}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：モンモン……。
    voice "ch14_s_129"
    s "Montmon… You really are amazing, you know.{#ch14_s_129}"

    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # モンモランシー：どういう意味よ！
    voice "ch14_m_015"
    m "What's that supposed to mean! Honestly!{#ch14_m_015}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # モンモランシー：それより、あなた達はこれからどうするの？
    voice "ch14_m_016"
    m "More importantly, what will you all do now? Not forgiving them is fine, but our enemy is a huge organization.{#ch14_m_016}"

    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # モンモランシー：悔しいけど、これ以上は女王様に助けて
    voice "ch14_m_017"
    m "I hate to say it, but you should ask the Queen for help.{#ch14_m_017}"

    # [SPRITE   lay3     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：少し考えさせて……。
    voice "ch14_l_045"
    l "Let me think a little… What are they really planning?{#ch14_l_045}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay3     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 614
    jump ch14_4_scene_614

label ch14_4_scene_614:

    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [LAYER    lay0     image=+590, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch14_t_011}"

    # キュルケ：……。
    k "…{#ch14_k_087}"

    # サイト：（キュルケのやつ、静かになったと思ったら、
    s "(Kirche went quiet—so she was with Tabitha, huh…){#ch14_s_130}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：キュルケ、タバサと何をしてるんだい？  [voice 13010]
    voice "ch14_s_131"
    s "Kirche, what are you doing with Tabitha?{#ch14_s_131}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：うん、タバサおねえちゃんに、
    voice "ch14_k_088"
    k "Mm. Tabitha onee-chan is reading me a story.{#ch14_k_088}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：うん。  [voice 15788]
    voice "ch14_t_012"
    t "Mm.{#ch14_t_012}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：ねぇ、もっとごほんをよんで！  [voice 3756]
    voice "ch14_k_089"
    k "Hey, read more stories!{#ch14_k_089}"

    # [LAYER    lay0     image=+590, level=160, dir=1A]
    # タバサ：こうして、王子様はドラゴンを倒すことが
    voice "ch14_t_013"
    t "And so, the prince was able to defeat the dragon.{#ch14_t_013}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：わーい、やったー。  [voice 3757]
    voice "ch14_k_090"
    k "Yay! Yay!{#ch14_k_090}"

    # サイト：（普段はお姉さんの役割だったキュルケを
    s "(Tabitha is soothing Kirche—the one who's usually the big sister…){#ch14_s_132}"

    menu:
        "Watch over them warmly{#ch14_4_c_614_1}":
            jump ch14_4_scene_615
        "Feel a little relieved{#ch14_4_c_614_2}":
            jump ch14_4_scene_616
        "Jealous of Tabitha{#ch14_4_c_614_3}":
            jump ch14_4_scene_617

label ch14_4_scene_615:

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [LAYER    lay0     image=+590, level=160, dir=1A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：タバサって実は面倒見がいいんだな。  [voice 13011]
    voice "ch14_s_133"
    s "Tabitha's actually quite good with kids.{#ch14_s_133}"

    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：そう？  [voice 15790]
    voice "ch14_t_014"
    t "Is she?{#ch14_t_014}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：……？  [voice 3758]
    voice "ch14_k_091"
    k "…?{#ch14_k_091}"

    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # → next scene 618
    jump ch14_4_scene_618

label ch14_4_scene_616:

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [LAYER    lay0     image=+590, level=160, dir=1A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ありがと、タバサ。
    voice "ch14_s_134"
    s "Thanks, Tabitha. You saved me.{#ch14_s_134}"

    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……？  [voice 15791]
    voice "ch14_t_015"
    t "…?{#ch14_t_015}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：いや、キュルケがこうなってから、
    voice "ch14_s_135"
    s "Well, ever since Kirche turned like this, she's been glued to me. It's a relief.{#ch14_s_135}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch14_t_016}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # → next scene 618
    jump ch14_4_scene_618

label ch14_4_scene_617:

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [LAYER    lay0     image=+590, level=160, dir=1A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（な、なんだろう、この胸のもやもやは……）
    s "(What's this feeling in my chest…?){#ch14_s_136}"

    # サイト：（そんな風にタバサと一緒に
    s "(Reading a book with Tabitha like this…){#ch14_s_137}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：お、お兄ちゃんはさびしいぞー！  [voice 13014]
    voice "ch14_s_138"
    s "B-Big brother is lonely!{#ch14_s_138}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：どうしたの？
    voice "ch14_k_092"
    k "What's wrong, big brother?{#ch14_k_092}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch14_t_017}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：い、いやなんでも……。  [voice 13015]
    voice "ch14_s_139"
    s "N-No, it's nothing…{#ch14_s_139}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # → next scene 618
    jump ch14_4_scene_618

label ch14_4_scene_618:

    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # null：………。 (no voice)
    # [BG       stage    hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay7     image=+962, level=160, dir=1B]
    # ハルナ：平賀くん、キュルケさんにつきっきりですね。  [voice 2451]
    voice "ch14_ha_004"
    ha "Hiraga-kun, you're glued to Kirche-san, aren't you?{#ch14_ha_004}"

    # [SPRITE   lay7     x=224, y=0]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：サイトさん、本当は小さい娘が
    voice "ch14_si_007"
    si "Saito-san, do you actually like little girls?{#ch14_si_007}"

    # [SPRITE   lay7     image=+968, level=160, dir=1B]
    # ハルナ：平賀くん、日本ではそんなこと
    voice "ch14_ha_005"
    ha "Hiraga-kun, in Japan you were never like this… But maybe you were just hiding it…{#ch14_ha_005}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：ま、まあまあ……。  [voice 15076]
    voice "ch14_si_008"
    si "N-Now, now…{#ch14_si_008}"

    # [SPRITE   lay7     image=+962, level=160, dir=1B]
    # ハルナ：平賀くん、たとえ異世界でも犯罪は
    voice "ch14_ha_006"
    ha "Hiraga-kun, even in another world, crime is still wrong.{#ch14_ha_006}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ちょっと待て、おまえら。
    voice "ch14_s_140"
    s "Hold on, you two. What do you think I am?{#ch14_s_140}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay7     image=+968, level=160, dir=1B]
    # ハルナ：……。  [voice 2454]
    voice "ch14_ha_007"
    ha "…{#ch14_ha_007}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：おにいちゃ～～ん！
    voice "ch14_k_093"
    k "Big broooother! I'm sleepy…{#ch14_k_093}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：お、おいっ！
    voice "ch14_s_141"
    s "H-Hey! Kirche, don't hug me.{#ch14_s_141}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [EVENT_CG event    image=+254, level=80]
    $ dissolve_fx("id(254)")
    # [TRANS trans("crossfade", 1000)]
    # キュルケ：おにいちゃんのおひざ、あったかーい。
    voice "ch14_k_094"
    k "Big brother's lap is warmmm. Good niiight…{#ch14_k_094}"

    # ハルナ：ああっ、ひざまくらですか！
    voice "ch14_ha_008"
    ha "Ah! A lap pillow! What an attack!{#ch14_ha_008}"

    # シエスタ：い、いいんですか！
    voice "ch14_si_009"
    si "I-Is this all right! Miss Valliere!?{#ch14_si_009}"

    # ルイズ：し、知らないもん！  [voice 7048]
    voice "ch14_l_046"
    l "I-I don't know!{#ch14_l_046}"

    # キュルケ：……おにいちゃん、だいすき。  [voice 3762]
    voice "ch14_k_095"
    k "…Big brother, I love you.{#ch14_k_095}"

    # タバサ：……。
    t "…{#ch14_t_018}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：（はぁ……。
    s "(Sigh… What am I supposed to do? At this rate, I won't last…){#ch14_s_142}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
label ch14_4_scene_1489:
    jump attention
    return

label ch14_4_scene_1490:
    jump attention
    return

label ch14_4_scene_1491:
    jump attention
    return

    # ==== КОНЕЦ ГЛАВЫ 14 ====
    jump ch15
    return

