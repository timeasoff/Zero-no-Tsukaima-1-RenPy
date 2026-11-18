# Глава 11, часть 3 (сцены 478-499): «ハルナの決意» — продолжение.
# Источник: ps2_source/chapters/chapter_12_ハルナの決意.txt (SCENE 478-499).
# Точные аргументы: ps2_source/events_full/chapter_12_ハルナの決意.txt.
# EN-база в сценарии; JA/RU — в game/tl/{japanese,russian}/ch11_3_*.rpy.
# Голоса: нумерация ch11_<spk>_<NNN> продолжает части 1-2 (общая нумерация главы).

label ch11_3:
    $ tndl(None)
    $ show_sprites()

label ch11_3_scene_478:

    # [BG       stage    image=+10, level=200]
    $ fade_fx("louise_room")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # ルイズ：……行っちゃったわね。  [voice 7172]
    voice "ch11_l_014"
    l "She's gone, isn't she.{#ch11_l_014}"

    # サイト：ああ、行っちゃったな。  [voice 13251]
    voice "ch11_s_041"
    s "Yeah, she's gone.{#ch11_s_041}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：短い付き合いだったはずなのに……。
    voice "ch11_l_015"
    l "It was such a short time… / but it's lonely once she's gone.{#ch11_l_015}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：いまごろ、どのあたりでしょうね？
    voice "ch11_si_017"
    si "I wonder where she is by now? / She said she'd be based in Tristain for a while, didn't she?{#ch11_si_017}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：……。
    k "…{#ch11_k_007}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：あ～～なんか肩こっちゃった。
    voice "ch11_k_008"
    k "Ugh, my shoulders are all stiff. / It's all this sullen talk that doesn't suit me.{#ch11_k_008}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：むっ、なによ。
    voice "ch11_l_016"
    l "Hmph. What's with that attitude!{#ch11_l_016}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：というわけで、しばらくお休みをとるわね。  [voice 3820]
    voice "ch11_k_009"
    k "In that case, I'll be taking a break for a while.{#ch11_k_009}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：へ？  [voice 7175]
    voice "ch11_l_017"
    l "Huh?{#ch11_l_017}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ち、ちょっと正気！？
    voice "ch11_l_018"
    l "W-Wait, are you out of your mind!? Don't just say whatever you want!{#ch11_l_018}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：女王陛下のお手伝いや舞台やらで
    voice "ch11_k_010"
    k "I've been helping Her Majesty and doing shows, / and the fatigue has piled up…{#ch11_k_010}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：わたしも休む。  [voice 15799]
    voice "ch11_t_002"
    t "I'm resting too.{#ch11_t_002}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：え、ええっ！？  [voice 13252]
    voice "ch11_s_042"
    s "W-What!?{#ch11_s_042}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：ち、ちょっと待ちなさい！
    voice "ch11_l_019"
    l "W-Wait a moment! The bomb-thrower business isn't settled yet. I won't allow you to do as you please!{#ch11_l_019}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：……。  [voice 13253]
    voice "ch11_s_043"
    s "…{#ch11_s_043}"

    menu:
        "Something's off.{#ch11_3_c_478_1}":
            jump ch11_3_scene_479
        "…It's getting lonely.{#ch11_3_c_478_2}":
            jump ch11_3_scene_480
        "That's so irresponsible!{#ch11_3_c_478_3}":
            jump ch11_3_scene_481

label ch11_3_scene_479:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("louise_room")
    # サイト：（なにか変だな？）
    s "Something's wrong, isn't it?{#ch11_s_044}"

    # サイト：（２人とも、いい加減なことをする奴じゃ
    s "Neither of them is the type to act carelessly…{#ch11_s_045}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なあ、キュルケ……。  [voice 13254]
    voice "ch11_s_046"
    s "Say, Kirche…{#ch11_s_046}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：分かっているわよ。
    voice "ch11_k_011"
    k "I know, darling.{#ch11_k_011}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：大丈夫。
    voice "ch11_t_003"
    t "It's fine. Leave it to me.{#ch11_t_003}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：……へ？
    voice "ch11_s_047"
    s "…Huh? What do you mean?{#ch11_s_047}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：ご、ご主人様を無視して話を
    voice "ch11_l_020"
    l "D-Don't you ignore your master and talk among yourselves! You stupid dog!{#ch11_l_020}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # → next scene 482
    jump ch11_3_scene_482

label ch11_3_scene_480:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("louise_room")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：春奈に続いて、キュルケとタバサまで
    voice "ch11_s_048"
    s "After Haruna, now Kirche and Tabitha are gone too?{#ch11_s_048}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：寂しくなるなあ。  [voice 13257]
    voice "ch11_s_049"
    s "It's gonna be lonely.{#ch11_s_049}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # シエスタ：そうですねぇ。  [voice 15136]
    voice "ch11_si_018"
    si "It is, isn't it.{#ch11_si_018}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そ、そういう問題じゃないでしょ！  [voice 7179]
    voice "ch11_l_021"
    l "T-That's not the point, is it!{#ch11_l_021}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：な、なにを考えてるのよ！
    voice "ch11_l_022"
    l "W-What are you thinking, you two?!{#ch11_l_022}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     hide]
    # → next scene 482
    jump ch11_3_scene_482

label ch11_3_scene_481:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("louise_room")
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：そ、そんな無責任な！  [voice 13258]
    voice "ch11_s_050"
    s "T-That's so irresponsible!{#ch11_s_050}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：そうよそうよ！  [voice 7181]
    voice "ch11_l_023"
    l "Exactly, exactly!{#ch11_l_023}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：後で分かる。  [voice 15801]
    voice "ch11_t_004"
    t "You'll understand later.{#ch11_t_004}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：分かるって、ど、どういう意味よ！  [voice 7182]
    voice "ch11_l_024"
    l "Understand? W-What do you mean by that!{#ch11_l_024}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：まあまあ、単純まっすぐなのが
    voice "ch11_k_012"
    k "Now, now, that's Louise for you—simple and straightforward…{#ch11_k_012}"

    # [SPRITE   lay1     hide]
    # → next scene 482
    jump ch11_3_scene_482

label ch11_3_scene_482:

    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("louise_room")
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：そういうわけだから。
    voice "ch11_k_013"
    k "That's why. See you, darling.{#ch11_k_013}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：なにがどうなってるんだよ。
    voice "ch11_s_051"
    s "What the heck is going on? I don't get it at all!{#ch11_s_051}"

    # ルイズ：い、いいわよ！
    voice "ch11_l_025"
    l "F-Fine! I don't care anymore!{#ch11_l_025}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 483
    jump ch11_3_scene_483

label ch11_3_scene_483:

    # [BG       stage    image=+54, level=200]
    $ fade_fx("theater_backstage")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [BGM      bgm      play=+23]
    play music t22 fadein 1.0
    # ハルナ：劇場を出てからまだほとんどたってないのに。
    voice "ch11_ha_033"
    ha "It's barely been any time since we left the theater. / And yet it feels so nostalgic—am I imagining it?{#ch11_ha_033}"

    # ウェザリー：……。
    w "…{#ch11_w_008}"

    # ウェザリー：任務、ご苦労だったわね。  [voice 16087]
    voice "ch11_w_009"
    w "You did well on the mission.{#ch11_w_009}"

    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：え？
    voice "ch11_ha_034"
    ha "Eh? Mission? What do you mean?{#ch11_ha_034}"

    # [SPRITE   lay20    image=+1063, level=160, dir=1A]
    # ウェザリー：なるほど。
    voice "ch11_w_010"
    w "I see. So Akina hasn't awakened yet.{#ch11_w_010}"

    # ハルナ：アキナ？
    voice "ch11_ha_035"
    ha "Akina? I'm Haruna, though.{#ch11_ha_035}"

    # ハルナ：ウェザリー、さん？  [voice 2593]
    voice "ch11_ha_036"
    ha "Weatherly-san?{#ch11_ha_036}"

    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：秘術が成功したのは嬉しいけれど、
    voice "ch11_w_011"
    w "I'm glad the secret art succeeded, but when things go too well, it becomes inconvenient.{#ch11_w_011}"

    # ハルナ：秘術？
    voice "ch11_ha_037"
    ha "Secret art? What do you mean by…?{#ch11_ha_037}"

    # [SPRITE   lay20    image=+1063, level=160, dir=1A]
    # ウェザリー：いいわ、教えてあげる。
    voice "ch11_w_012"
    w "Fine, I'll tell you. That recent bomb-thrower incident… it was all your doing.{#ch11_w_012}"

    # [SPRITE   lay7     image=+988, level=160, dir=2A]
    # ハルナ：な、なんですか！
    voice "ch11_ha_038"
    ha "W-What are you saying! That's too sudden, even for a joke!{#ch11_ha_038}"

    # ウェザリー：ふふふ。
    voice "ch11_w_013"
    w "Fufufu. Well, whether you believe it or not is of no consequence.{#ch11_w_013}"

    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：大事なのは、我らの計画が、
    voice "ch11_w_014"
    w "What matters is that our plan has advanced to the third stage thanks to your work.{#ch11_w_014}"

    # ウェザリー：最後にハルナ、あなたの意識を永遠に
    voice "ch11_w_015"
    w "Finally, Haruna—if I put your consciousness to sleep forever, the second stage will be complete.{#ch11_w_015}"

    # ウェザリー：不確定要因は、早く見切りをつけるに
    voice "ch11_w_016"
    w "An uncertain factor is best cut loose sooner rather than later.{#ch11_w_016}"

    # ウェザリー：いままで、ご苦労様。
    voice "ch11_w_017"
    w "Thank you for everything. Rest well.{#ch11_w_017}"

    # ウェザリー：……。
    w "…{#ch11_w_018}"

    # [SE       se0      play=+94]
    # [SPRITE   lay7     image=+990, level=160, dir=2A]
    # ハルナ：（……な、なに……？
    voice "ch11_ha_039"
    ha "What… what's happening…? My consciousness… drifting away…{#ch11_ha_039}"

    # [SPRITE   lay7     image=+988, level=160, dir=2A]
    # ハルナ：いや、や、やめて！  [voice 2597]
    voice "ch11_ha_040"
    ha "N-No, stop!{#ch11_ha_040}"

    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # ウェザリー：な、何っ！？
    voice "ch11_w_019"
    w "What!? A mere commoner resisting my spell!?{#ch11_w_019}"

    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：ご、ごめんなさい！  [voice 2598]
    voice "ch11_ha_041"
    ha "I-I'm sorry!{#ch11_ha_041}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay20    x=64, y=0]
    # ウェザリー：待て！
    voice "ch11_w_020"
    w "Wait! Haruna!{#ch11_w_020}"

    # ウェザリー：しまった、あのスピード！
    voice "ch11_w_021"
    w "Damn, that speed! Between that and the earlier resistance, Akina's power must be awakening!{#ch11_w_021}"

    # ウェザリー：くっ、逃がさないわよ！  [voice 16099]
    voice "ch11_w_022"
    w "Tch, I won't let you get away!{#ch11_w_022}"

    # [SPRITE   lay20    hide]
    # [BG       stage    hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("sky")
    # [TRANS trans("crossfade", 1000)]
    # null：………。  (no voice — пропущено по образцу ch11_2)
    # [BG       stage    hide]
    # [BG       stage    image=+47, level=200]
    $ fade_fx("cafe_entrance")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：はぁ、はぁ、はぁ！  [voice 2599]
    voice "ch11_ha_042"
    ha "Haa, haa, haa!{#ch11_ha_042}"

    # ハルナ：（キュルケさんが言ってたのって
    voice "ch11_ha_043"
    ha "Is this what Kirche-san was talking about?{#ch11_ha_043}"

    # ハルナ：（助けて！
    voice "ch11_ha_044"
    ha "Help me! Hiragan-kun!{#ch11_ha_044}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay7     hide]
    # [BG       stage    hide]
label ch11_3_scene_484:

    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+88, level=200]
    $ fade_fx("sky")
    # [TRANS trans("crossfade", 1000)]
    # ハルナ：はぁはぁはぁ……。  [voice 2602]
    voice "ch11_ha_045"
    ha "Haa haa haa…{#ch11_ha_045}"

    # ハルナ：はぁはぁはぁ……。  [voice 2603]
    voice "ch11_ha_046"
    ha "Haa haa haa…{#ch11_ha_046}"

    # ハルナ：（動いて！
    voice "ch11_ha_047"
    ha "Move! …My body!{#ch11_ha_047}"

    # ハルナ：（動いて！
    voice "ch11_ha_048"
    ha "Move! …My legs!{#ch11_ha_048}"

    # ハルナ：（動きなさい！
    voice "ch11_ha_049"
    ha "Come on, move! …Please, move!{#ch11_ha_049}"

    # [SPRITE   lay7     hide]
    # [BG       stage    hide]
    # null：………。  (no voice — пропущено по образцу ch11_2)
    # [BG       stage    image=+47, level=200]
    $ fade_fx("cafe_entrance")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：はぁはぁ……。
    voice "ch11_ha_050"
    ha "Haa haa… If I've come this far…{#ch11_ha_050}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [SPRITE   lay7     hide]
    # [SPRITE   lay11    image=+1105, level=160, dir=1A]
    # [SPRITE   lay12    image=+1105, level=160, dir=1A]
    # [SPRITE   lay12    level=155]
    # [SPRITE   lay20    image=+1061, level=154, dir=1A]
    # [SPRITE   lay11    level=156]
    # ウェザリー：逃げ切れると思ったの？  [voice 16100]
    voice "ch11_w_023"
    w "Did you think you could get away?{#ch11_w_023}"

    # 魔導士：……。
    mage "…{#ch11_mage_002}"

    # 魔導士：……。
    mage "…{#ch11_mage_003}"

    # [SPRITE   lay11    hide]
    # [SPRITE   lay12    hide]
    # [SPRITE   lay20    hide]
    # [SPRITE   lay7     image=+955, level=157, dir=1A]
    # ハルナ：ウェザリーさん！  [voice 2608]
    voice "ch11_ha_051"
    ha "Weatherly-san!{#ch11_ha_051}"

    # [SPRITE   lay7     x=-96, y=0]
    # [SPRITE   lay20    image=+1061, level=154, dir=1A]
    # ウェザリー：手間をかけさせるものではない。  [voice 16101]
    voice "ch11_w_024"
    w "I shouldn't have to go to this much trouble.{#ch11_w_024}"

    # [SPRITE   lay7     image=+957, level=157, dir=1A]
    # ハルナ：い、いやですっ！
    voice "ch11_ha_052"
    ha "N-No! Please stop!{#ch11_ha_052}"

    # ウェザリー：さあ、眠りなさい。
    voice "ch11_w_025"
    w "Now, sleep. Rest your exhausted body.{#ch11_w_025}"

    # ウェザリー：大丈夫、目覚めた時には、
    voice "ch11_w_026"
    w "It's fine. When you wake, you'll be someone else. You'll even forget you were Haruna.{#ch11_w_026}"

    # [SPRITE   lay7     image=+955, level=157, dir=1A]
    # ハルナ：いっ、いやぁあぁぁーーーっ！  [voice 2610]
    voice "ch11_ha_053"
    ha "N-Nooooooo!{#ch11_ha_053}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # null：………。  (no voice — пропущено по образцу ch11_2)
    # [SPRITE   lay12    hide]
    # [SPRITE   lay20    image=+1061, level=154, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay11    hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # ウェザリー：しかし、よく頑張ったものね。
    voice "ch11_w_027"
    w "Still, you did well—to run this far through the pursuit.{#ch11_w_027}"

    # [SPRITE   lay20    image=+1067, level=154, dir=1A]
    # ウェザリー：（もしかして、彼女にも伝説の力があるの？）  [voice 16105]
    voice "ch11_w_028"
    w "Could she have the legendary power too?{#ch11_w_028}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay20    hide]
    # [BG       stage    hide]
    # → next scene 485
    jump ch11_3_scene_485

label ch11_3_scene_485:

    # [BG       stage    image=+88, level=200]
    $ fade_fx("sky")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # サイト：（春奈に続いて、キュルケとタバサが
    s "A few days since Haruna, then Kirche and Tabitha, disappeared from the academy…{#ch11_s_052}"

    # サイト：（なんというか、やっぱり……寂しいよな）
    s "I don't know how to say it, but… it's lonely.{#ch11_s_053}"

    # サイト：（ルイズもいつもに比べて元気がないみたいだ）
    s "Louise seems less energetic than usual, too.{#ch11_s_054}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+17, level=200]
    $ fade_fx("hallway_down")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あ、サイトさん！
    voice "ch11_si_019"
    si "Ah, Saito-san! Just the person I wanted!{#ch11_si_019}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：あれ？
    voice "ch11_s_055"
    s "Huh? Siesta, what's wrong?{#ch11_s_055}"

    # シエスタ：ハルナさんの忘れ物なんです。  [voice 15138]
    voice "ch11_si_020"
    si "It's something Haruna-san forgot.{#ch11_si_020}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：手帳？  [voice 13261]
    voice "ch11_s_056"
    s "A notebook?{#ch11_s_056}"

    menu:
        "Let's check inside.{#ch11_3_c_485_1}":
            jump ch11_3_scene_486
        "Should we return it?{#ch11_3_c_485_2}":
            jump ch11_3_scene_487
        "We don't need it, do we?{#ch11_3_c_485_3}":
            jump ch11_3_scene_488

label ch11_3_scene_486:

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("hallway_down")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：とりあえず、中を確認してみよう。  [voice 13262]
    voice "ch11_s_057"
    s "First, let's take a look inside.{#ch11_s_057}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あ、はい。  [voice 15139]
    voice "ch11_si_021"
    si "Ah, yes.{#ch11_si_021}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：……でも、いいんですか？
    voice "ch11_si_022"
    si "…But is it all right? It's a girl's personal things.{#ch11_si_022}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：き、貴重品かどうか確かめるんだよ！  [voice 13263]
    voice "ch11_s_058"
    s "W-We're just checking if it's something valuable!{#ch11_s_058}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：このノート、何が書いてあるんでしょう？
    voice "ch11_si_023"
    si "I wonder what's written in this notebook? I can't read a bit of it.{#ch11_si_023}"

    # サイト：俺達の国の文字だからな。
    voice "ch11_s_059"
    s "It's the writing of our country. Well, it's also the country of Siesta's great-grandfather. See, it looks like the letters on that grave, doesn't it?{#ch11_s_059}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あ、そういわれてみれば……。  [voice 15142]
    voice "ch11_si_024"
    si "Ah, now that you mention it…{#ch11_si_024}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（春奈らしい几帳面な字だなあ）
    s "It's just like Haruna—neat and careful handwriting.{#ch11_s_060}"

    # サイト：あれ？
    voice "ch11_s_061"
    s "Huh? What's this?{#ch11_s_061}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：え？
    voice "ch11_s_062"
    s "Eh? Wh-What?{#ch11_s_062}"

    # → next scene 489
    jump ch11_3_scene_489

label ch11_3_scene_487:

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("hallway_down")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：やっぱり届けたほうがいいのかな？  [voice 13267]
    voice "ch11_s_063"
    s "Maybe I really should return it after all?{#ch11_s_063}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：そうですねぇ。
    voice "ch11_si_025"
    si "I suppose so. If it's something precious, that is.{#ch11_si_025}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：あれ？
    voice "ch11_s_064"
    s "Huh? What's this?{#ch11_s_064}"

    # サイト：（……写真？）
    s "…A photo?{#ch11_s_065}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：……え？
    voice "ch11_s_066"
    s "…Eh? Wh-What?{#ch11_s_066}"

    # → next scene 489
    jump ch11_3_scene_489

label ch11_3_scene_488:

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("hallway_down")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：別にいらないんじゃないかな？  [voice 13270]
    voice "ch11_s_067"
    s "It's not like she needs it, does she?{#ch11_s_067}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：そ、そうなんでしょうか？  [voice 15144]
    voice "ch11_si_026"
    si "R-Really?{#ch11_si_026}"

    # サイト：どうなんだろう？  [voice 13271]
    voice "ch11_s_068"
    s "Who knows?{#ch11_s_068}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：あれ？
    voice "ch11_s_069"
    s "Huh? What's this? Is it sticking out?{#ch11_s_069}"

    # サイト：（……写真？）
    s "…A photo?{#ch11_s_070}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：……って、え？
    voice "ch11_s_071"
    s "…Wait, eh? Wh-What?{#ch11_s_071}"

    # → next scene 489
    jump ch11_3_scene_489

label ch11_3_scene_489:

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("hallway_down")
    # [BGM      bgm      stop=500]
    stop music fadeout 1.0
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+277, level=80]
    $ dissolve_fx("id(277)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # サイト：（……俺の写真！？
    s "…My photo!? In a place like this…{#ch11_s_072}"

    # シエスタ：どうしたんです？
    voice "ch11_si_027"
    si "What's wrong? Your face is bright red.{#ch11_si_027}"

    # シエスタ：わっ、なんです！？
    voice "ch11_si_028"
    si "Wow, what's this!? It's a very detailed drawing.{#ch11_si_028}"

    # シエスタ：しかも、サイトさんが描いてあるなんて。  [voice 15147]
    voice "ch11_si_029"
    si "And what's more, it's Saito-san who's drawn here.{#ch11_si_029}"

    # サイト：あはは。
    voice "ch11_s_073"
    s "Haha. So it is.{#ch11_s_073}"

    # シエスタ：こんな緻密な絵をどうやって
    voice "ch11_si_030"
    si "I wonder how she drew such a detailed picture?{#ch11_si_030}"

    # サイト：さ、さあ……。
    voice "ch11_s_074"
    s "W-Well… I'm no expert on art.{#ch11_s_074}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+17, level=200]
    $ fade_fx("hallway_down")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # シエスタ：殿方のこんな絵を持ち歩いている
    voice "ch11_si_031"
    si "What must a girl feel, carrying around a picture of a boy like this…{#ch11_si_031}"

    # シエスタ：どんなものなのでしょうね？
    voice "ch11_si_032"
    si "I wonder what it's like? Saito-san would know, wouldn't you?{#ch11_si_032}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：な、なんというか。
    voice "ch11_s_075"
    s "W-Well, how should I put it. That is…{#ch11_s_075}"

    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # シエスタ：……はぁ、わたしも手に入るなら
    voice "ch11_si_033"
    si "…If I could get one, I'd carry it around too…{#ch11_si_033}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 490
    jump ch11_3_scene_490

label ch11_3_scene_490:

    # [BG       stage    image=+26, level=200]
    $ fade_fx("yard")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：（あ～～驚いた）
    s "Wow, I'm surprised.{#ch11_s_076}"

    # サイト：（……春奈、手帳に俺の写真を入れてたなんて）
    s "…Haruna had my photo in her notebook.{#ch11_s_077}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：……。  [voice 13277]
    voice "ch11_s_078"
    s "…{#ch11_s_078}"

    # サイト：俺のどこがそんなにいいんだよ。  [voice 13278]
    voice "ch11_s_079"
    s "What's so good about me?{#ch11_s_079}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（そうだよ……。
    s "That's right… If Haruna has the photo, it must have been taken in Japan.{#ch11_s_080}"

    # サイト：（俺、春奈に何かしたのか？
    s "Did I do something for Haruna? Something that would make her keep my photo like this?{#ch11_s_081}"

    # サイト：なんでなんだよ。
    voice "ch11_s_082"
    s "Why? Haruna…{#ch11_s_082}"

    menu:
        "I have to return the notebook to Haruna.{#ch11_3_c_490_1}":
            jump ch11_3_scene_491
        "I want to see Haruna.{#ch11_3_c_490_2}":
            jump ch11_3_scene_492
        "I want to ask Haruna.{#ch11_3_c_490_3}":
            jump ch11_3_scene_493

label ch11_3_scene_491:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("yard")
    # サイト：（……この手帳を届けないと）
    s "…I have to return this notebook.{#ch11_s_083}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 495
    jump ch11_3_scene_495

label ch11_3_scene_492:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("yard")
    # サイト：（春奈に逢いたい。
    s "I want to see Haruna. No matter what.{#ch11_s_084}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 495
    jump ch11_3_scene_495

label ch11_3_scene_493:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("yard")
    # サイト：（……なぜ、俺なんだ？）
    s "…Why me?{#ch11_s_085}"

    # サイト：（誤解とかだと情けないけど……、
    s "I'd be embarrassed if it were a misunderstanding, but… I want to be sure.{#ch11_s_086}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 495
    jump ch11_3_scene_495

label ch11_3_scene_494:

    # [SPRITE   lay5     image=+396, level=157, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("yard")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 495
    jump ch11_3_scene_495

label ch11_3_scene_495:

    # [BG       stage    image=+10, level=200]
    $ fade_fx("louise_room")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # ルイズ：忘れ物を届けたいって、どういうことよ？  [voice 7184]
    voice "ch11_l_026"
    l "What do you mean, you want to return something she forgot?{#ch11_l_026}"

    # サイト：いや、だから……。
    voice "ch11_s_087"
    s "Well, you see… I want to go to Tristain to return this notebook Haruna forgot.{#ch11_s_087}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：だから、なんでそうなるのかを聞いてるのよ。  [voice 7185]
    voice "ch11_l_027"
    l "That's not what I asked. I'm asking why it has to be you.{#ch11_l_027}"

    # ルイズ：そんなの他の人に頼めばいいじゃない？  [voice 7186]
    voice "ch11_l_028"
    l "Can't you just ask someone else?{#ch11_l_028}"

    # サイト：そ、そう言われても……。  [voice 13281]
    voice "ch11_s_088"
    s "I know, but…{#ch11_s_088}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：（あんな写真が挿んであるのを
    s "I can't let anyone see a photo like that in there!{#ch11_s_089}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：と、とにかく！
    voice "ch11_s_090"
    s "A-Anyway! I want to give it to Haruna myself, in person!{#ch11_s_090}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：ふ～～ん、ずいぶんとこだわるのね。
    voice "ch11_l_029"
    l "Hm~ You're awfully insistent. Something's suspicious.{#ch11_l_029}"

    # [SPRITE   lay1     image=+337, level=160, dir=2A]
    # ルイズ：いいわ、わたしもトリスタニアに行ってあげる。  [voice 7188]
    voice "ch11_l_030"
    l "Fine. I'll come with you to Tristain.{#ch11_l_030}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：な、なんでそうなるんだよ！  [voice 13283]
    voice "ch11_s_091"
    s "H-How did it come to this?!{#ch11_s_091}"

    menu:
        "Refuse firmly.{#ch11_3_c_495_1}":
            jump ch11_3_scene_496
        "Play it off.{#ch11_3_c_495_2}":
            jump ch11_3_scene_497
        "Accept it.{#ch11_3_c_495_3}":
            jump ch11_3_scene_498

label ch11_3_scene_496:

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # [SPRITE   lay1     image=+337, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("louise_room")
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：断固、断る！
    voice "ch11_s_092"
    s "I firmly refuse! I'm going alone!{#ch11_s_092}"

    # [SPRITE   lay1     image=+372, level=160, dir=3A]
    # ルイズ：あなたに拒否権なんて
    voice "ch11_l_031"
    l "You don't have the right to refuse!{#ch11_l_031}"

    # ルイズ：黙って言うことを聞きなさい。
    voice "ch11_l_032"
    l "Be quiet and do as I say. Stupid dog!{#ch11_l_032}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：き、きゃいん！  [voice 13285]
    voice "ch11_s_093"
    s "K-Kyah!{#ch11_s_093}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 500
    jump ch11_4

label ch11_3_scene_497:

    # [SPRITE   lay1     image=+337, level=160, dir=2A]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("louise_room")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そ、そんな……。  [voice 13286]
    voice "ch11_s_094"
    s "T-That's…{#ch11_s_094}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ご主人様にわざわざ出向いていただかなくとも！  [voice 13287]
    voice "ch11_s_095"
    s "You don't need to go out of your way, master!{#ch11_s_095}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：あら、遠慮なんて不要よ。
    voice "ch11_l_033"
    l "Oh, there's no need to hold back. It's not like Haruna and I are close.{#ch11_l_033}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：黙って言うことを聞きなさい。
    voice "ch11_l_034"
    l "Be quiet and do as I say. Stupid dog!{#ch11_l_034}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 500
    jump ch11_4

label ch11_3_scene_498:

    # [SPRITE   lay1     image=+337, level=160, dir=2A]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("louise_room")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：わ、分かりました。  [voice 13288]
    voice "ch11_s_096"
    s "I-I understand.{#ch11_s_096}"

    # [SPRITE   lay1     image=+337, level=160, dir=2A]
    # ルイズ：分かればよろしいっ！  [voice 7193]
    voice "ch11_l_035"
    l "Good, now you understand!{#ch11_l_035}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 500
    jump ch11_4

label ch11_3_scene_499:

    # [SPRITE   lay5     image=+396, level=157, dir=1A]
    # [SPRITE   lay1     image=+372, level=156, dir=3A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("louise_room")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 500
    jump ch11_4

    # ==== КОНЕЦ ГЛАВЫ 11, ЧАСТИ 3 ====
    jump attention
    return

