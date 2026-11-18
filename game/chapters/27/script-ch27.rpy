# Глава 27, часть 1 (сцены 972–984): флот Реконкисты, спор о Пустоте.
# Источник: ps2_source/chapters/chapter_28_ハルナの秘密.txt (SCENE 972-984).

label ch27:
    $ tndl(None)
    $ show_sprites()

label ch27_1_scene_972:

    # [TITLE title("ハルナの秘密")]
    # [EVENT_CG event    image=+98, level=80]
    $ dissolve_fx("id(98)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # アキナ：アハハハハハハハッ！
    voice "ch27_ak_001"
    ak "A-ha-ha-ha-ha! Burn, break, crumble away!{#ch27_ak_001}"

    # [SE       se0      play=+63]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [SPRITE   lay21    hide, vibrate=14]
    # [SPRITE   lay4     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay3     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay21    hide, reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # アキナ：アーッハハハハハハーッ！！  [voice 154]
    voice "ch27_ak_002"
    ak "Ahh ha ha ha ha!{#ch27_ak_002}"

    # [SE       se0      play=+63]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [SPRITE   lay21    vibrate=14]
    # [SPRITE   lay4     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay3     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay21    hide, reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay21    hide]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [EVENT_CG event    hide]
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1156, level=200]
    $ fade_fx("id(1156)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SE       se0      play=+82]
    # [SE       se0      play=+57]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：おはよう……。
    voice "ch27_k_001"
    k "Good morning… Are you awake?{#ch27_k_001}"

    # [SPRITE   lay6     x=-96, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch27_t_001}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay2     image=+502, level=160, dir=1B]
    # シエスタ：おはようございます。
    voice "ch27_si_001"
    si "Good morning, Miss Zerbst, Miss Tabitha, Miss Montmorency.{#ch27_si_001}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：あら、今朝は早いじゃない？  [voice 6900]
    voice "ch27_l_001"
    l "Oh, you're up early today, aren't you?{#ch27_l_001}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：だって、寝てられないわよ。
    voice "ch27_k_002"
    k "Well, I can't sleep with this tension continuing…{#ch27_k_002}"

    # キュルケ：それに、市街戦も続いてるみたいだし……。  [voice 3571]
    voice "ch27_k_003"
    k "And the street fighting seems to be continuing, too…{#ch27_k_003}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # モンモランシー：ここにも戦火が届くのかしらね……。  [voice 4122]
    voice "ch27_m_001"
    m "I wonder if the flames of war will reach here, too…{#ch27_m_001}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：はぁ……。  [voice 12714]
    voice "ch27_s_001"
    s "Haa…{#ch27_s_001}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：なにため息ついてるのよ、ダーリン？  [voice 3572]
    voice "ch27_k_004"
    k "Why the sigh, darling?{#ch27_k_004}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：爆弾使いの正体がハルナだったから、
    voice "ch27_l_002"
    l "It's complicated—the bomber turned out to be Haruna.{#ch27_l_002}"

    # サイト：いや、爆弾使いなのは、ウェザリーが植えつけた
    voice "ch27_s_002"
    s "No. The bomber is the separate personality Akina, planted by Weatherly. Haruna has nothing to do with it.{#ch27_s_002}"

    # ルイズ：でも、つかまるのはハルナなのよ。
    voice "ch27_l_003"
    l "But it's Haruna who'll be captured. Personality doesn't matter.{#ch27_l_003}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：じゃあ、捕まえないほうが幸せって言うのかよ！  [voice 12716]
    voice "ch27_s_003"
    s "So you're saying we shouldn't catch her? That would make her happy?{#ch27_s_003}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：そんなこと言ってない。
    voice "ch27_l_004"
    l "I'm not saying that. At this rate, the Tristain kingdom will be taken by storm.{#ch27_l_004}"

    # ルイズ：絶対、黒幕が絡んでるはずよ。
    voice "ch27_l_005"
    l "There has to be a mastermind. Weatherly alone couldn't do something this audacious.{#ch27_l_005}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：せめて、その黒幕が分かれば……。  [voice 6905]
    voice "ch27_l_006"
    l "If only we could at least find that mastermind…{#ch27_l_006}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch27_t_002}"

    # [SE       se0      play=+57]
    # [SPRITE   lay1     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay4     image=+559, level=160, dir=1A]
    # ギーシュ：大変だよ、きみ達。  [voice 1532]
    voice "ch27_g_001"
    g "It's terrible, you guys.{#ch27_g_001}"

    # [SPRITE   lay4     x=-96, y=0]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # モンモランシー：どうしたのよ、ギーシュ。  [voice 4123]
    voice "ch27_m_002"
    m "What's wrong, Guiche?{#ch27_m_002}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # ギーシュ：レコン・キスタの空中艦隊が、
    voice "ch27_g_002"
    g "The Reconquista air fleet seems to be heading for Tristain.{#ch27_g_002}"

    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [SPRITE   lay3     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：レコン・キスタの空中艦隊！？  [voice 12717]
    voice "ch27_s_004"
    s "The Reconquista air fleet!?{#ch27_s_004}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ま、まってよ。
    voice "ch27_l_007"
    l "W-Wait. In the last war, their fleet took serious damage.{#ch27_l_007}"

    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # ギーシュ：分からない。
    voice "ch27_g_003"
    g "I don't know. It's not certain information, but there's also a report that a fleet in the Tristain army defected.{#ch27_g_003}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：このタイミングで来るってことは……。  [voice 12718]
    voice "ch27_s_005"
    s "Coming at this timing means…{#ch27_s_005}"

    menu:
        "Support for Tristain?{#ch27_1_c_972_1}":
            jump ch27_1_scene_973
        "Taking advantage of chaos?{#ch27_1_c_972_2}":
            jump ch27_1_scene_974
        "Is Reconquista the mastermind?{#ch27_1_c_972_3}":
            jump ch27_1_scene_975

label ch27_1_scene_973:

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：トリステインを助けるためってことはないか？  [voice 12719]
    voice "ch27_s_006"
    s "Support for Tristain, maybe?{#ch27_s_006}"

    # サイト：ほら、前に戦争した一件を反省して、
    voice "ch27_s_007"
    s "Like, regretting the last war and helping us this time… or something?{#ch27_s_007}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：……甘いわね。
    voice "ch27_l_008"
    l "…That's naive. Reconquista would never do such a thing.{#ch27_l_008}"

    # → next scene 976
    jump ch27_1_scene_976

label ch27_1_scene_974:

    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：トリステインの混乱に乗じて攻める気か。  [voice 12721]
    voice "ch27_s_008"
    s "So they intend to attack amid Tristain's chaos.{#ch27_s_008}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：んー、そんなところね、きっと。  [voice 3573]
    voice "ch27_k_005"
    k "Hmm, that's probably it, I suppose.{#ch27_k_005}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：実はレコン・キスタが黒幕でした、
    voice "ch27_l_009"
    l "We can't rule out the theory that Reconquista is the mastermind, either.{#ch27_l_009}"

    # キュルケ：前に攻めてきたときは、派手に負けて
    voice "ch27_k_006"
    k "When they attacked before, they lost spectacularly and made fools of themselves in front of neighboring countries. I'm sure they haven't forgotten that grudge.{#ch27_k_006}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：……。  [voice 12722]
    voice "ch27_s_009"
    s "…{#ch27_s_009}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……。  [voice 6909]
    voice "ch27_l_010"
    l "…{#ch27_l_010}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+506, level=160, dir=1B]
    # シエスタ：どうしたんですか？
    voice "ch27_si_002"
    si "What's wrong? You two went quiet all of a sudden.{#ch27_si_002}"

    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：えっ、なんのことかしら？
    voice "ch27_l_011"
    l "Eh? What do you mean? It's nothing, nothing…{#ch27_l_011}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：い、いやなんでも……。  [voice 12723]
    voice "ch27_s_010"
    s "N-No, it's nothing…{#ch27_s_010}"

    # サイト：（まさか、俺達が撃退したなんてこと、
    s "(There's no way I can tell them we were the ones who drove them off…){#ch27_s_011}"

    # → next scene 976
    jump ch27_1_scene_976

label ch27_1_scene_975:

    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：実は黒幕がレコン・キスタだった？  [voice 12724]
    voice "ch27_s_012"
    s "Could the mastermind be Reconquista?{#ch27_s_012}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：でも、市街戦を行っている敵とレコン・キスタと
    voice "ch27_k_007"
    k "But at this point, can we really prove that the street-fighting enemy is connected to Reconquista?{#ch27_k_007}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：仮に結びついていたとしても、
    voice "ch27_l_012"
    l "Even if they were, they wouldn't admit it now, would they?{#ch27_l_012}"

    # キュルケ：ただ、はっきりしてることは……。  [voice 3576]
    voice "ch27_k_008"
    k "But one thing is clear…{#ch27_k_008}"

    # サイト：はっきりしてることは？  [voice 12725]
    voice "ch27_s_013"
    s "Clear what?{#ch27_s_013}"

    # キュルケ：レコン・キスタが以前、トリステインを
    voice "ch27_k_009"
    k "Reconquista hasn't forgotten the grudge from when they tried to attack Tristain and failed.{#ch27_k_009}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：はぁ……。  [voice 12726]
    voice "ch27_s_014"
    s "Haa…{#ch27_s_014}"

    # サイト：（なんだかんだで、俺とルイズに責任がある
    s "(Somehow, it feels like Louise and I are the ones responsible…){#ch27_s_015}"

    # → next scene 976
    jump ch27_1_scene_976

label ch27_1_scene_976:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：っていうかさ。
    voice "ch27_k_010"
    k "I mean—once the air fleet arrives, it's a full-scale war.{#ch27_k_010}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そうね。
    voice "ch27_l_013"
    l "Right. If only we could stop the street fighting… We'd have a bit more of an advantage, but…{#ch27_l_013}"

    # ルイズ：そういう意味ではタイミングが良すぎるわ。  [voice 6913]
    voice "ch27_l_014"
    l "In that sense, the timing is too good.{#ch27_l_014}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：出る……。  [voice 15735]
    voice "ch27_t_003"
    t "I'm going…{#ch27_t_003}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：どうしたの、タバサ？  [voice 3579]
    voice "ch27_k_011"
    k "What's wrong, Tabitha?{#ch27_k_011}"

    # タバサ：もう一度勝負する。  [voice 15736]
    voice "ch27_t_004"
    t "I'll fight again.{#ch27_t_004}"

    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：勝負するって、まさか……？  [voice 3580]
    voice "ch27_k_012"
    k "Fight again—you don't mean…?{#ch27_k_012}"

    # タバサ：アキナと。  [voice 15737]
    voice "ch27_t_005"
    t "With Akina.{#ch27_t_005}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：本気か？
    voice "ch27_s_016"
    s "Are you serious? Your wounds may have healed, but you're not fully recovered yet, are you?{#ch27_s_016}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：でも……。
    voice "ch27_t_006"
    t "But… Someone has to stop Akina.{#ch27_t_006}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：確かに、アキナを止めなければ、
    voice "ch27_s_017"
    s "True—unless we stop Akina, winning this war will be difficult. But still…{#ch27_s_017}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：分かった。
    voice "ch27_k_013"
    k "All right. I'll help Tabitha, too!{#ch27_k_013}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：キュルケ！  [voice 12729]
    voice "ch27_s_018"
    s "Kirche!{#ch27_s_018}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：もちろんわたしもね。
    voice "ch27_l_015"
    l "Of course, so will I. We can't let Tabitha fight alone.{#ch27_l_015}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：お前までもか！  [voice 12730]
    voice "ch27_s_019"
    s "Even you!?{#ch27_s_019}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：なによ、サイト。
    voice "ch27_l_016"
    l "What's that, Saito? Don't tell me you think that, because the bomber is using Haruna's body, she can't be fought!?{#ch27_l_016}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：……。  [voice 12731]
    voice "ch27_s_020"
    s "…{#ch27_s_020}"

    menu:
        "Better to leave it to Tabitha{#ch27_1_c_976_1}":
            jump ch27_1_scene_977
        "Worried about after the fight{#ch27_1_c_976_2}":
            jump ch27_1_scene_978
        "Worried about everyone{#ch27_1_c_976_3}":
            jump ch27_1_scene_979

label ch27_1_scene_977:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：タバサに任せた方がいいって。  [voice 12732]
    voice "ch27_s_021"
    s "I think it's better to leave it to Tabitha.{#ch27_s_021}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：それって……。
    voice "ch27_l_017"
    l "Meaning… You're saying we'd be a burden to Tabitha?{#ch27_l_017}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そういうわけじゃないけど……。
    voice "ch27_s_022"
    s "That's not it, but… Tabitha got burned because I was there with her, in a way…{#ch27_s_022}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……。  [voice 6917]
    voice "ch27_l_018"
    l "…{#ch27_l_018}"

    # ルイズ：それを言われると少し考えちゃうけど……。  [voice 6918]
    voice "ch27_l_019"
    l "When you put it that way, I can't help thinking about it…{#ch27_l_019}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あら、あたしなら平気よ。
    voice "ch27_k_014"
    k "Oh, I'll be fine. I could never be a burden.{#ch27_k_014}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：さすが、キュルケ。
    voice "ch27_s_023"
    s "As expected of Kirche. Quite the confidence…{#ch27_s_023}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：ンフフ、そんなに誉めないでよ、ダーリン。  [voice 3583]
    voice "ch27_k_015"
    k "Nn fu fu, don't praise me so much, darling.{#ch27_k_015}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：じゃ、じゃあ、わたしも平気っ！  [voice 6919]
    voice "ch27_l_020"
    l "T-Then I'll be fine, too!{#ch27_l_020}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：ハハハ……。  [voice 12735]
    voice "ch27_s_024"
    s "Ha ha ha…{#ch27_s_024}"

    # サイト：（なんでそこで張り合うのかなぁ……）
    s "(Why compete over that…?){#ch27_s_025}"

    # [SPRITE   lay1     hide]
    # → next scene 980
    jump ch27_1_scene_980

label ch27_1_scene_978:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：アキナに勝ったあとのことが心配なんだ。  [voice 12736]
    voice "ch27_s_026"
    s "I'm worried about what happens after Akina is defeated.{#ch27_s_026}"

    # サイト：タバサが春奈を、
    voice "ch27_s_027"
    s "That Tabitha might hand Haruna over to Gallia.{#ch27_s_027}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：そのことは、タバサと話し合ってるん
    voice "ch27_k_016"
    k "Haven't you talked it over with Tabitha?{#ch27_k_016}"

    # サイト：うん。
    voice "ch27_s_028"
    s "I have. I don't want to hand Haruna over—but considering Tabitha's position…{#ch27_s_028}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：難しい問題ね……。  [voice 3585]
    voice "ch27_k_017"
    k "It's a difficult problem…{#ch27_k_017}"

    # [SPRITE   lay6     hide]
    # → next scene 980
    jump ch27_1_scene_980

label ch27_1_scene_979:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：みんなのことが心配なんだ。  [voice 12739]
    voice "ch27_s_029"
    s "I'm worried about everyone.{#ch27_s_029}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ルイズのことならいざ知らず、
    voice "ch27_k_018"
    k "If it were Louise, I'd understand—but I'm not so immature that darling needs to worry about me.{#ch27_k_018}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……。  [voice 6920]
    voice "ch27_l_021"
    l "…{#ch27_l_021}"

    # キュルケ：あら、怒らないのね？  [voice 3587]
    voice "ch27_k_019"
    k "Oh, you're not angry?{#ch27_k_019}"

    # ルイズ：事実と違うことで中傷されても、
    voice "ch27_l_022"
    l "Not getting angry at slander that isn't true—that's what makes a true lady.{#ch27_l_022}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：ルイズ……。
    voice "ch27_k_020"
    k "Louise… Why are you so full of confidence?{#ch27_k_020}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：とにかく、わたしもキュルケも
    voice "ch27_l_023"
    l "Anyway—Kirche and I won't be a burden to Tabitha!{#ch27_l_023}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：アキナは春奈と違うんだ。
    voice "ch27_s_030"
    s "Akina isn't Haruna. That's exactly why Tabitha got badly burned shielding me…{#ch27_s_030}"

    # ルイズ：じゃあ、あんたに何かあったときは、
    voice "ch27_l_024"
    l "Then, if something happens to you, I suppose I'll just let you die and watch.{#ch27_l_024}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あたしは先手必勝よ。
    voice "ch27_k_021"
    k "I believe in striking first. I won't give them a chance to do anything cowardly.{#ch27_k_021}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：ハハハ……。
    voice "ch27_s_031"
    s "Ha ha ha… Then, we're fine.{#ch27_s_031}"

    # [SPRITE   lay6     hide]
    # → next scene 980
    jump ch27_1_scene_980

label ch27_1_scene_980:

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch27_t_007}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：やっぱり、行くのか。  [voice 12742]
    voice "ch27_s_032"
    s "So, you're going after all?{#ch27_s_032}"

    # タバサ：行く。  [voice 15739]
    voice "ch27_t_008"
    t "I'm going.{#ch27_t_008}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：分かった。
    voice "ch27_s_033"
    s "All right. I'm going, too.{#ch27_s_033}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：その代わり、アキナを……。
    voice "ch27_s_034"
    s "But—about Akina. No, about Haruna. Please at least hold off on handing her over to Gallia.{#ch27_s_034}"

    # タバサ：考えておく。  [voice 15740]
    voice "ch27_t_009"
    t "I'll think about it.{#ch27_t_009}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：ありがとう、タバサ。  [voice 12745]
    voice "ch27_s_035"
    s "Thank you, Tabitha.{#ch27_s_035}"

    # [LAYER    lay0     image=+596, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch27_t_010}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：それじゃ、行くわよサイト。  [voice 6924]
    voice "ch27_l_025"
    l "Well then, let's go, Saito.{#ch27_l_025}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：行くってどこにだよ？  [voice 12746]
    voice "ch27_s_036"
    s "Go where?{#ch27_s_036}"

    # ルイズ：決まってるじゃない、お城よ。
    voice "ch27_l_026"
    l "Obviously—to the castle. We need the princess's permission.{#ch27_l_026}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 981
    jump ch27_1_scene_981

label ch27_1_scene_981:

    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：で、ルイズ……。
    voice "ch27_s_037"
    s "So, Louise. What are you going to the princess for?{#ch27_s_037}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ご主人様の自信満々な表情に不安を
    voice "ch27_s_038"
    s "I'm uneasy about that confident look on my mistress's face…{#ch27_s_038}"

    # ルイズ：あら、虚無の魔法を使う許可をもらいに
    voice "ch27_l_027"
    l "Oh—I'm going to ask permission to use Void magic.{#ch27_l_027}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：虚無の魔法！？
    voice "ch27_s_039"
    s "Void magic!? You intend to destroy the capital!?{#ch27_s_039}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：は？
    voice "ch27_l_028"
    l "Hah? What are you talking about?{#ch27_l_028}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：何って……。
    voice "ch27_s_040"
    s "What do you mean, what—you'll use Void on the air fleet, like last time, right?{#ch27_s_040}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：んー……。
    voice "ch27_l_029"
    l "Hmm… It's not exactly that.{#ch27_l_029}"

    # サイト：違うのか？  [voice 12751]
    voice "ch27_s_041"
    s "It's not?{#ch27_s_041}"

    # ルイズ：まぁ、違う方法。  [voice 6929]
    voice "ch27_l_030"
    l "Well… A different method.{#ch27_l_030}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：あっ！？
    voice "ch27_l_031"
    l "Ah!? We're at the princess's room already. You'd better mind your manners!{#ch27_l_031}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：あ、ああ……。  [voice 12752]
    voice "ch27_s_042"
    s "A-Ah…{#ch27_s_042}"

    # ルイズ：生返事しない。  [voice 6931]
    voice "ch27_l_032"
    l "Don't answer absentmindedly.{#ch27_l_032}"

    # サイト：（そうは言っても、ここで虚無の魔法を
    s "(Even so—if I used Void magic here, the damage would be incredible…){#ch27_s_043}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+206, level=80]
    $ dissolve_fx("id(206)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：姫さま、たびたびの急な訪問、
    voice "ch27_l_033"
    l "Princess, I'm sorry to drop in so often. Today I've come with a request.{#ch27_l_033}"

    # アンリエッタ：いいのよ、ルイズ・フランソワーズ。
    voice "ch27_h_001"
    h "It's fine, Louise Francoise. Don't be so formal.{#ch27_h_001}"

    # アンリエッタ：この様な状況。
    voice "ch27_h_002"
    h "In a situation like this, sticking to etiquette only makes the damage grow.{#ch27_h_002}"

    # [EVENT_CG event    image=+207, level=80]
    $ dissolve_fx("id(207)")
    # ルイズ：実は……。
    voice "ch27_l_034"
    l "Actually… I'd like permission to use Void magic in the capital.{#ch27_l_034}"

    # サイト：だから、それは……。
    voice "ch27_s_044"
    s "So, that's… Could you reconsider, mistress?{#ch27_s_044}"

    # ルイズ：無理ね。  [voice 6934]
    voice "ch27_l_035"
    l "No.{#ch27_l_035}"

    # アンリエッタ：虚無の魔法、ですか……。  [voice 675]
    voice "ch27_h_003"
    h "Void magic, you say…{#ch27_h_003}"

    # ルイズ：はい、姫さま。  [voice 6935]
    voice "ch27_l_036"
    l "Yes, Princess.{#ch27_l_036}"

    # アンリエッタ：……。  [voice 676]
    voice "ch27_h_004"
    h "…{#ch27_h_004}"

    # サイト：（お姫さま、ダメだって言ってくれ。
    s "Princess, tell me it's no. Using Void on the capital is madness…{#ch27_s_045}"

    # アンリエッタ：そうですね……。  [voice 677]
    voice "ch27_h_005"
    h "I see…{#ch27_h_005}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ルイズ！
    voice "ch27_s_046"
    s "Louise! You can't do something like that!!{#ch27_s_046}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：サイトっ、あんたは黙ってなさいっ！  [voice 6936]
    voice "ch27_l_037"
    l "Saito! You be quiet!!{#ch27_l_037}"

    # サイト：そんなこと言ったってだなっ！！  [voice 12755]
    voice "ch27_s_047"
    s "Even if you say that—!!{#ch27_s_047}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+803, level=160, dir=2A]
    # アンリエッタ：まあ……。
    voice "ch27_h_006"
    h "Well… Darling familiar, are you against using Void magic?{#ch27_h_006}"

    # [SPRITE   lay8     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そ、それは……。  [voice 12756]
    voice "ch27_s_048"
    s "T-That is…{#ch27_s_048}"

    menu:
        "I'm against it!{#ch27_1_c_981_1}":
            jump ch27_1_scene_982
        "If the princess allows…{#ch27_1_c_981_2}":
            jump ch27_1_scene_983
        "The place is the problem{#ch27_1_c_981_3}":
            jump ch27_1_scene_984

label ch27_1_scene_982:

    # [SPRITE   lay8     image=+803, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：反対ですよ、絶対反対っ！！  [voice 12757]
    voice "ch27_s_049"
    s "I'm against it! Absolutely against it!!{#ch27_s_049}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：なっ、なんでそういうことを言うのよ！
    voice "ch27_l_038"
    l "Wh-Why would you say that! You—!!{#ch27_l_038}"

    # サイト：そんなの当たり前だろっ！！
    voice "ch27_s_050"
    s "Of course it's obvious! Do you have any idea how powerful your Void magic is!?{#ch27_s_050}"

    # サイト：目的の戦艦１隻落とすつもりで放ったのに、
    voice "ch27_s_051"
    s "I aimed at a single battleship, but it burned the whole fleet!!{#ch27_s_051}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：分かってるわよ……。
    voice "ch27_l_039"
    l "I know… I was the one who cast it, after all…{#ch27_l_039}"

    # サイト：全然、分かってないっ！
    voice "ch27_s_052"
    s "You don't understand at all! If you use magic that powerful here, the whole capital could vanish!!{#ch27_s_052}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     image=+797, level=160, dir=2A]
    # アンリエッタ：まあまあ、ルイズにはルイズの考えが
    voice "ch27_h_007"
    h "Now, now. Louise has her own reasons. Why not trust her?{#ch27_h_007}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：まあ、お姫さまがそう言うのなら……。
    voice "ch27_s_053"
    s "Well, if the princess says so… But still…{#ch27_s_053}"

    # → next scene 985
    jump ch27_2

label ch27_1_scene_983:

    # [SPRITE   lay8     image=+803, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：お姫さまが許可を出すのなら、まあ……。  [voice 12762]
    voice "ch27_s_054"
    s "If the princess gives permission, then I suppose…{#ch27_s_054}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：でも、本当は文句ありますって感じの
    voice "ch27_l_040"
    l "But you're really against it, aren't you? You're making that face.{#ch27_l_040}"

    # サイト：そりゃ、あるに決まってんだろ？
    voice "ch27_s_055"
    s "Of course I am! Are you taking that magic lightly?{#ch27_s_055}"

    # ルイズ：軽くなんて見てないわよ。  [voice 6940]
    voice "ch27_l_041"
    l "I'm not taking it lightly.{#ch27_l_041}"

    # サイト：どうだかねー。  [voice 12764]
    voice "ch27_s_056"
    s "Is that so?{#ch27_s_056}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     image=+797, level=160, dir=2A]
    # アンリエッタ：まあまあ、使い魔さん。
    voice "ch27_h_008"
    h "Now, now, familiar. Louise has her own reasons for asking.{#ch27_h_008}"

    # アンリエッタ：それに、ルイズはあなたが思っている以上に
    voice "ch27_h_009"
    h "And Louise is more thoughtful than you think.{#ch27_h_009}"

    # アンリエッタ：そのことで、わたくしが何度救われたことか
    voice "ch27_h_010"
    h "I don't know how many times she's saved me because of that…{#ch27_h_010}"

    # → next scene 985
    jump ch27_2

label ch27_1_scene_984:

    # [SPRITE   lay8     image=+803, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：使う場所が問題だって言ってるんです！  [voice 12765]
    voice "ch27_s_057"
    s "I'm telling you—the problem is WHERE it's used!{#ch27_s_057}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：どこが問題だって言うのよ？  [voice 6941]
    voice "ch27_l_042"
    l "What's the problem?{#ch27_l_042}"

    # サイト：本気で言ってんのか？
    voice "ch27_s_058"
    s "Are you serious? Using it in the capital is problematic any way you look at it!{#ch27_s_058}"

    # サイト：お前、トリスタニアの都を消し去る
    voice "ch27_s_059"
    s "Do you intend to erase the Tristain capital?{#ch27_s_059}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：サイトこそ、なに言ってんのよ？
    voice "ch27_l_043"
    l "What are you talking about, Saito? I have no intention of erasing the princess's capital!{#ch27_l_043}"

    # サイト：だとしたら、虚無の魔法の威力を
    voice "ch27_s_060"
    s "Then you clearly don't understand Void magic's power at all.{#ch27_s_060}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：なんですってぇ～っ！？  [voice 6943]
    voice "ch27_l_044"
    l "What was that!?{#ch27_l_044}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     image=+797, level=160, dir=2A]
    # アンリエッタ：まあまあ、ルイズにはルイズの考えが
    voice "ch27_h_011"
    h "Now, now. Louise has her own reasons. Why not trust her?{#ch27_h_011}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：まあ、お姫さまがそう言うのなら……。
    voice "ch27_s_061"
    s "Well, if the princess says so… But still…{#ch27_s_061}"

    # → next scene 985
    jump ch27_2

    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch27_2
    return

