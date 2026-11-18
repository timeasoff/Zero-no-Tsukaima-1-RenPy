# Глава 25, часть 2 (сцены 918–932): свидание с Табасой, слежка, нападение магов.
# Источник: ps2_source/chapters/chapter_26_手紙の秘密.txt (SCENE 918-932).

label ch25_2:
    $ tndl(None)
    $ show_sprites()

label ch25_2_scene_918:

    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # null：………。
    th "… … …{#ch25_th_001}"

    # サイト：あれから、大人しく待ってるわけだけど……。
    voice "ch25_s_065"
    s "After that, I waited quietly—but quite a lot of time has passed by now…{#ch25_s_065}"

    # サイト：タバサのやつ、いくらなんでも遅すぎないか？  [voice 12447]
    voice "ch25_s_066"
    s "Tabitha's taking too long, even by her standards, isn't she?{#ch25_s_066}"

    # サイト：……はっ！？  [voice 12448]
    voice "ch25_s_067"
    s "…Hah!?{#ch25_s_067}"

    # サイト：これはひょっとして、置き去り？  [voice 12449]
    voice "ch25_s_068"
    s "Could this be… being stood up?{#ch25_s_068}"

    # サイト：いやぁ、まてまて。
    voice "ch25_s_069"
    s "No, wait, wait. I should think more positively about this.{#ch25_s_069}"

    # サイト：そう、ポジティブに……。
    voice "ch25_s_070"
    s "Right, positively… Hmm… A 'neglect play'?{#ch25_s_070}"

    # サイト：ありうるなぁ、放置プレイ……。  [voice 12452]
    voice "ch25_s_071"
    s "That's quite possible, a neglect play…{#ch25_s_071}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # タバサ：放置プレイってなに？  [voice 15661]
    voice "ch25_t_021"
    t "What's a neglect play?{#ch25_t_021}"

    # サイト：はうわっ！？
    voice "ch25_s_072"
    s "Whoa!? T-Tabitha-san!?{#ch25_s_072}"

    # タバサ：……。
    t "…{#ch25_t_022}"

    # [LAYER    lay0     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：い、いつからそこに？  [voice 12454]
    voice "ch25_s_073"
    s "S-Since when were you there?{#ch25_s_073}"

    # タバサ：いま来たところ。  [voice 15662]
    voice "ch25_t_023"
    t "I just got here.{#ch25_t_023}"

    # サイト：そ、そうでしたか。  [voice 12455]
    voice "ch25_s_074"
    s "O-Oh. I see.{#ch25_s_074}"

    # タバサ：放置プレイって？  [voice 15663]
    voice "ch25_t_024"
    t "The neglect play?{#ch25_t_024}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：えーっと……。  [voice 12456]
    voice "ch25_s_075"
    s "Umm…{#ch25_s_075}"

    menu:
        "Did you change clothes?{#ch25_2_c_918_1}":
            jump ch25_2_scene_919
        "You don't need to know!{#ch25_2_c_918_2}":
            jump ch25_2_scene_920
        "A 'neglect play' is…{#ch25_2_c_918_3}":
            jump ch25_2_scene_921

label ch25_2_scene_919:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：そんなことより、着替えてきたんだ？  [voice 12457]
    voice "ch25_s_076"
    s "More importantly—did you change clothes?{#ch25_s_076}"

    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：うん。  [voice 15664]
    voice "ch25_t_025"
    t "Mm.{#ch25_t_025}"

    # サイト：なんというか……。
    voice "ch25_s_077"
    s "I mean… I usually only see you in your uniform, so Tabitha in different clothes looks really fresh.{#ch25_s_077}"

    # タバサ：……。
    t "…{#ch25_t_026}"

    # → next scene 922
    jump ch25_2_scene_922

label ch25_2_scene_920:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：知る必要、ありませんっ！  [voice 12459]
    voice "ch25_s_078"
    s "You have no need to know!{#ch25_s_078}"

    # [LAYER    lay0     image=+605, level=160, dir=1B]
    # タバサ：知っちゃダメ？  [voice 15665]
    voice "ch25_t_027"
    t "I can't know?{#ch25_t_027}"

    # サイト：ダメ。  [voice 12460]
    voice "ch25_s_079"
    s "No.{#ch25_s_079}"

    # タバサ：ダメ？  [voice 15666]
    voice "ch25_t_028"
    t "No?{#ch25_t_028}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：あ、タ、タバサ、服着替えてきたんだ？  [voice 12461]
    voice "ch25_s_080"
    s "A-Ah, Tabitha, did you change clothes?{#ch25_s_080}"

    # [LAYER    lay0     image=+603, level=160, dir=1B]
    # タバサ：ごまかしてる。  [voice 15667]
    voice "ch25_t_029"
    t "You're dodging the question.{#ch25_t_029}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ううっ。  [voice 12462]
    voice "ch25_s_081"
    s "Ugh.{#ch25_s_081}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：ち、ちがう！
    voice "ch25_s_082"
    s "N-No! I was just amazed by Tabitha's usual clothes—I've never seen them before!{#ch25_s_082}"

    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # タバサ：感動？  [voice 15668]
    voice "ch25_t_030"
    t "Amazed?{#ch25_t_030}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：うん、感動。
    voice "ch25_s_083"
    s "Yeah, amazed. It looks really fresh and nice!{#ch25_s_083}"

    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：……。  [voice 15669]
    voice "ch25_t_031"
    t "…{#ch25_t_031}"

    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # タバサ：で、放置プレイって？  [voice 15670]
    voice "ch25_t_032"
    t "So, the neglect play?{#ch25_t_032}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ま、また今度にしてください。  [voice 12465]
    voice "ch25_s_084"
    s "Well, let's leave that for next time.{#ch25_s_084}"

    # → next scene 922
    jump ch25_2_scene_922

label ch25_2_scene_921:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：放置プレイというのは……。  [voice 12466]
    voice "ch25_s_085"
    s "A 'neglect play' is…{#ch25_s_085}"

    # サイト：俺の国に存在する屈折した愛情表現の
    voice "ch25_s_086"
    s "…one of the twisted ways of showing affection that exists in my country.{#ch25_s_086}"

    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：愛情表現……。  [voice 15671]
    voice "ch25_t_033"
    t "Affection…{#ch25_t_033}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：いや、絶対勘違いしてると思うけど、
    voice "ch25_s_087"
    s "No, I'm sure you're misunderstanding. Twisted affection is a very difficult thing!{#ch25_s_087}"

    # サイト：そもそも、する側とされる側との間に
    voice "ch25_s_088"
    s "For one thing, it only works if there's a relationship of trust between the one doing it and the one receiving it.{#ch25_s_088}"

    # タバサ：信頼関係。  [voice 15672]
    voice "ch25_t_034"
    t "Trust.{#ch25_t_034}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：憧れちゃダメ！
    voice "ch25_s_089"
    s "You mustn't admire it! Normal people hate it!{#ch25_s_089}"

    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # タバサ：うん。  [voice 15673]
    voice "ch25_t_035"
    t "Mm.{#ch25_t_035}"

    # → next scene 922
    jump ch25_2_scene_922

label ch25_2_scene_922:

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：で、タバサ。
    voice "ch25_s_090"
    s "So, Tabitha—what should I do?{#ch25_s_090}"

    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_036}"

    # サイト：どうしたの？
    voice "ch25_s_091"
    s "What's wrong? Don't hold back, tell me anything.{#ch25_s_091}"

    # タバサ：今日一日。  [voice 15674]
    voice "ch25_t_037"
    t "All day today.{#ch25_t_037}"

    # サイト：うんうん。  [voice 12473]
    voice "ch25_s_092"
    s "Mm-hm.{#ch25_s_092}"

    # タバサ：付き合ってほしい。  [voice 15675]
    voice "ch25_t_038"
    t "I want you to keep me company.{#ch25_t_038}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：うんうん……。
    voice "ch25_s_093"
    s "Mm-hm… Eh? Keep you company?{#ch25_s_093}"

    # [LAYER    lay0     image=+605, level=160, dir=1B]
    # タバサ：ダメ？  [voice 15676]
    voice "ch25_t_039"
    t "No?{#ch25_t_039}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：ダメじゃない！
    voice "ch25_s_094"
    s "Of course not! Of course not! I'd be delighted to accompany you!!{#ch25_s_094}"

    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_040}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：（なんか、手紙のことをごまかされてる
    s "(I feel like she's dodging the question about the letter… But whatever.){#ch25_s_095}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：で、タバサはどこに付き合ってほしいの？  [voice 12476]
    voice "ch25_s_096"
    s "So, where do you want me to accompany you, Tabitha?{#ch25_s_096}"

    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # タバサ：決めて。  [voice 15677]
    voice "ch25_t_041"
    t "You decide.{#ch25_t_041}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：えっ？
    voice "ch25_s_097"
    s "Eh? I can decide where we go?{#ch25_s_097}"

    # タバサ：うん。  [voice 15678]
    voice "ch25_t_042"
    t "Mm.{#ch25_t_042}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：えーと……。  [voice 12478]
    voice "ch25_s_098"
    s "Um…{#ch25_s_098}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # 【移動】劇場 → scene 599  ((0x01000000 +1513))
    th "[Move] Theater{#ch25_th_002}"

    # 【移動】表通り → scene 599  ((0x01000000 +1518))
    th "[Move] Main street{#ch25_th_003}"

    # 【移動】裏通り → scene 599  ((0x01000000 +1523))
    th "[Move] Back street{#ch25_th_004}"

    # 【移動】街道 → scene 599  ((0x01000000 +1528))
    th "[Move] Highway{#ch25_th_005}"

label ch25_2_scene_923:

    # [BG       stage    image=+58, hide, level=10]
    $ fade_fx("town_square")
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+58, hide, level=10]
    $ fade_fx("town_square")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+58, hide, level=10]
    $ fade_fx("town_square")
    # → next scene 1513
    # date event → ch25_4
    jump ch25_4

label ch25_2_scene_924:

    # [BG       stage    image=+58, hide, level=10]
    $ fade_fx("town_square")
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+58, hide, level=10]
    $ fade_fx("town_square")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+58, hide, level=10]
    $ fade_fx("town_square")
    # → next scene 1518
    # date event → ch25_4
    jump ch25_4

label ch25_2_scene_925:

    # [BG       stage    image=+58, hide, level=10]
    $ fade_fx("town_square")
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+58, hide, level=10]
    $ fade_fx("town_square")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+58, hide, level=10]
    $ fade_fx("town_square")
    # → next scene 1523
    # date event → ch25_4
    jump ch25_4

label ch25_2_scene_926:

    # [BG       stage    image=+58, hide, level=10]
    $ fade_fx("town_square")
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+58, hide, level=10]
    $ fade_fx("town_square")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+58, hide, level=10]
    $ fade_fx("town_square")
    # → next scene 1528
    # date event → ch25_4
    jump ch25_4

label ch25_2_scene_927:

    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [SE       se1      play=+37]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：むふふ。
    voice "ch25_k_020"
    k "Heh heh. You both seem to be enjoying yourselves, darling and Tabitha.{#ch25_k_020}"

    # ルイズ：ちょっと、キュルケ？
    voice "ch25_l_028"
    l "Hey, Kirche. Why do we all have to tail those two?{#ch25_l_028}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：なんでって、決まってるじゃない。
    voice "ch25_k_021"
    k "Why? Because I'm worried about darling, obviously. And of course, I'm worried about Tabitha, too.{#ch25_k_021}"

    # キュルケ：ルイズも、心配なんでしょ？
    voice "ch25_k_022"
    k "You're worried too, aren't you, Louise? Otherwise you wouldn't have come along, would you?{#ch25_k_022}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：わたしは心配してるとか、そーゆーことを
    voice "ch25_l_029"
    l "I'm not saying I'm worried! I'm saying tailing people is bad taste!{#ch25_l_029}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：だいたい、尾行だなんて、
    voice "ch25_l_030"
    l "Besides, tailing people isn't something a noble would do…{#ch25_l_030}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+964, level=160, dir=1B]
    # ハルナ：では、ルイズさんは帰ります？  [voice 2431]
    voice "ch25_ha_003"
    ha "So, Louise-san is going home?{#ch25_ha_003}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     image=+502, level=160, dir=1B]
    # シエスタ：わたしは尾行に賛成です。  [voice 15037]
    voice "ch25_si_004"
    si "I'm in favor of tailing them.{#ch25_si_004}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：サイトはわたしの使い魔なの。
    voice "ch25_l_031"
    l "Saito is my familiar. To leave your mistress behind and—oh!{#ch25_l_031}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：ちょ、ちょっとルイズ！
    voice "ch25_k_023"
    k "H-Hey, Louise! If you shout like that, they'll spot us!{#ch25_k_023}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：ふがふがふがが！！  [voice 6798]
    voice "ch25_l_032"
    l "Grrrr!!{#ch25_l_032}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay2     image=+504, level=160, dir=1B]
    # シエスタ：あーっ！
    voice "ch25_si_005"
    si "Aah! Saito-san is holding Miss Tabitha's hand!?{#ch25_si_005}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：えっ？
    voice "ch25_l_033"
    l "Eh? Eh!?{#ch25_l_033}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay7     image=+968, level=160, dir=1B]
    # ハルナ：平賀くん。
    voice "ch25_ha_004"
    ha "Hiraga-kun. You seem to be getting pretty close to Tabitha-san…{#ch25_ha_004}"

    # [SPRITE   lay1     image=+372, level=160, dir=3A]
    # ルイズ：キュルケ！  [voice 6800]
    voice "ch25_l_034"
    l "Kirche!{#ch25_l_034}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：ルイズ、どうしたの、杖なんて持って。  [voice 3472]
    voice "ch25_k_024"
    k "Louise, why are you holding a staff?{#ch25_k_024}"

    # ルイズ：どうやら、尾行も終わりみたいよ。  [voice 6801]
    voice "ch25_l_035"
    l "Looks like the tailing is over, too.{#ch25_l_035}"

    # [SE       se1      stop=1]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [TRANS trans("crossfade", 1000)]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：なあ、タバサ。
    voice "ch25_s_099"
    s "Say, Tabitha. Where are we going next?{#ch25_s_099}"

    # [LAYER    lay0     image=+669, level=160, dir=3B]
    # タバサ：……！  [voice 15679]
    voice "ch25_t_043"
    t "…!{#ch25_t_043}"

    # [SPRITE   lay5     image=+429, level=150, dir=2A]
    # [SPRITE   lay5     level=150]
    # [LAYER    lay0     level=154]
    # サイト：ん？
    voice "ch25_s_100"
    s "Hmm? What's wrong, Tabitha? Your face suddenly got scary…{#ch25_s_100}"

    # [SPRITE   lay5     level=151]
    # [LAYER    lay0     level=150]
    # タバサ：わたしから離れて。  [voice 15680]
    voice "ch25_t_044"
    t "Get away from me.{#ch25_t_044}"

    # [SPRITE   lay5     level=150]
    # [LAYER    lay0     level=151]
    # サイト：離れてって……。
    voice "ch25_s_101"
    s "Get away—what do you mean?{#ch25_s_101}"

    # [SPRITE   lay5     level=151]
    # [LAYER    lay0     level=150]
    # タバサ：離れてっ！  [voice 15681]
    voice "ch25_t_045"
    t "Get away!{#ch25_t_045}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay11    image=+1105, level=152, dir=1A]
    # [SPRITE   lay12    image=+1105, level=160, dir=1A]
    # 魔導士：……。
    mage "…{#ch25_mage_001}"

    # サイト：なんだよ、あんた達？
    voice "ch25_s_102"
    s "What are you people? Don't tell me…{#ch25_s_102}"

    menu:
        "They're after Haruna{#ch25_2_c_927_1}":
            jump ch25_2_scene_928
        "They're after Tabitha{#ch25_2_c_927_2}":
            jump ch25_2_scene_929
        "Jealous of us?{#ch25_2_c_927_3}":
            jump ch25_2_scene_930

label ch25_2_scene_928:

    # [SPRITE   lay12    image=+1105, level=160, dir=1A]
    # [SPRITE   lay11    image=+1105, level=152, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # サイト：春奈を狙った連中だな。  [voice 12483]
    voice "ch25_s_103"
    s "They're after Haruna, aren't they?{#ch25_s_103}"

    # → next scene 931
    jump ch25_2_scene_931

label ch25_2_scene_929:

    # [SPRITE   lay12    image=+1105, level=160, dir=1A]
    # [SPRITE   lay11    image=+1105, level=152, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # サイト：タバサを狙ってるのか？  [voice 12484]
    voice "ch25_s_104"
    s "They're after Tabitha, aren't they?{#ch25_s_104}"

    # → next scene 931
    jump ch25_2_scene_931

label ch25_2_scene_930:

    # [SPRITE   lay12    image=+1105, level=160, dir=1A]
    # [SPRITE   lay11    image=+1105, level=152, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # サイト：俺達２人に嫉妬してるな？
    voice "ch25_s_105"
    s "They're jealous of us two, aren't they? Us, the best couple of the day!{#ch25_s_105}"

    # → next scene 931
    jump ch25_2_scene_931

label ch25_2_scene_931:

    # [SPRITE   lay12    image=+1105, level=160, dir=1A]
    # [SPRITE   lay11    image=+1105, level=152, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [SPRITE   lay11    hide]
    # [SPRITE   lay12    hide]
    # [LAYER    lay0     image=+669, level=150, dir=3B]
    # タバサ：違う。  [voice 15682]
    voice "ch25_t_046"
    t "No.{#ch25_t_046}"

    # [LAYER    lay0     x=-160, y=0]
    # [SPRITE   lay5     image=+429, level=148, dir=2A]
    # [LAYER    lay0     level=151]
    # サイト：えっ、何違うの？
    voice "ch25_s_106"
    s "Eh? What do you mean, no? And how would you know, Tabitha?{#ch25_s_106}"

    # [SPRITE   lay5     level=149]
    # [LAYER    lay0     level=148]
    # [LAYER    lay0     image=+671, level=148, dir=3B]
    # タバサ：……。
    t "…{#ch25_t_047}"

    # [SE       se0      play=+65]
    # [SPRITE   lay5     image=+460, level=148, dir=3A]
    # [SPRITE   lay5     level=148]
    # [LAYER    lay0     level=149]
    # サイト：このままだと、ここを立ち去れそうもない
    voice "ch25_s_107"
    s "At this rate, we won't be able to leave this place. So, might as well…{#ch25_s_107}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+372, level=156, dir=3A]
    # ルイズ：サイトーッ！  [voice 6802]
    voice "ch25_l_036"
    l "Saitooo!!{#ch25_l_036}"

    # [SPRITE   lay5     image=+462, level=148, dir=3A]
    # サイト：ル、ルイズ？
    voice "ch25_s_108"
    s "L-Louise? Why are you here?{#ch25_s_108}"

    # ルイズ：なんだっていいでしょっ！  [voice 6803]
    voice "ch25_l_037"
    l "Never mind that!{#ch25_l_037}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+746, level=154, dir=3A]
    # キュルケ：ダーリーンッ！
    voice "ch25_k_025"
    k "Darring! I'll help you fight, too!{#ch25_k_025}"

    # サイト：キュルケまでいるのか！？  [voice 12489]
    voice "ch25_s_109"
    s "Kirche's here, too!?{#ch25_s_109}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+665, level=149, dir=3B]
    # タバサ：……。
    t "…{#ch25_t_048}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 932
    jump ch25_2_scene_932

label ch25_2_scene_932:

    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ふーっ。
    voice "ch25_s_110"
    s "Phew. We drove them off somehow… but just what were they?{#ch25_s_110}"

    # [LAYER    lay0     image=+605, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_049}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：なあ、タバサ。
    voice "ch25_s_111"
    s "Say, Tabitha. You wouldn't happen to know who they were…{#ch25_s_111}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+969, level=140, dir=1B]
    # ハルナ：大丈夫だった？
    voice "ch25_ha_005"
    ha "Are you all right, Hiraga-kun?{#ch25_ha_005}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay7     image=+968, level=160, dir=1B]
    # [SPRITE   lay2     image=+506, level=160, dir=1B]
    # シエスタ：お怪我はありませんでしたか？
    voice "ch25_si_006"
    si "Are you injured, Saito-san?{#ch25_si_006}"

    # サイト：うわっ、春奈にシエスタ！？
    voice "ch25_s_112"
    s "Whoa, Haruna and Siesta!? Which means…{#ch25_s_112}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+307, level=140, dir=1A]
    # ルイズ：サイト……。
    voice "ch25_l_038"
    l "Saito… You certainly had a good time, leaving your mistress behind.{#ch25_l_038}"

    # サイト：ひっ、ひぃ～っ！？  [voice 12493]
    voice "ch25_s_113"
    s "E-Eep!?{#ch25_s_113}"

    # ルイズ：これはもう、お仕置きを……。  [voice 6805]
    voice "ch25_l_039"
    l "This calls for punishment…{#ch25_l_039}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # タバサ：後をつけた。  [voice 15683]
    voice "ch25_t_050"
    t "They followed us.{#ch25_t_050}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：えっ？  [voice 6806]
    voice "ch25_l_040"
    l "Eh?{#ch25_l_040}"

    # タバサ：……。
    t "…{#ch25_t_051}"

    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：あっ、別にそーゆーわけじゃなくて……。
    voice "ch25_l_041"
    l "Ah, no, I didn't mean it that way… Right, Haruna?{#ch25_l_041}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     image=+964, level=160, dir=1B]
    # ハルナ：そ、そうです。
    voice "ch25_ha_006"
    ha "Y-Yes. We were just shopping.{#ch25_ha_006}"

    # ハルナ：で、たまたまタバサさんと平賀くんを
    voice "ch25_ha_007"
    ha "And then we happened to spot Tabitha-san and Hiraga-kun… Right, Siesta-san?{#ch25_ha_007}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     image=+502, level=160, dir=1B]
    # シエスタ：は、はい。
    voice "ch25_si_007"
    si "Y-Yes. It was a coincidence.{#ch25_si_007}"

    # [LAYER    lay0     image=+603, level=160, dir=1B]
    # タバサ：たまたま、尾行。  [voice 15684]
    voice "ch25_t_052"
    t "A coincidence—and a tail.{#ch25_t_052}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：あはは、はは……。  [voice 6808]
    voice "ch25_l_042"
    l "Ah ha, ha ha…{#ch25_l_042}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # → next scene 933
    jump ch25_3

    # ==== КОНЕЦ ЧАСТИ 2 ====
    jump ch25_3
    return

