# Глава 13, часть 2 (сцены 1469–1484): ночные маршруты Кирке и Сайто.
# Источник: ps2_source/chapters/chapter_14_炎の予感.txt (SCENE 1469-1484).

label ch13_2:
    $ tndl(None)
    $ show_sprites()

label ch13_2_scene_1469:

    # [BG       stage    image=+64, level=200]
    $ fade_fx("id(64)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：何か、情報を知ってる人いないかな。  [voice 10110]
    voice "ch13_s_051"
    s "Anybody know anything?{#ch13_s_051}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：そうね……。
    voice "ch13_k_042"
    k "Well… Let's ask that soldier over there.{#ch13_k_042}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：そんな簡単に教えてくれるかなぁ。
    voice "ch13_s_052"
    s "Would they tell us that easily? Hey, Kirche!{#ch13_s_052}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     x=64, y=0]
    # キュルケ：こんばんわ、兵隊さん。
    voice "ch13_k_043"
    k "Good evening, soldier. We're with the academy, staying here.{#ch13_k_043}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # [SPRITE   lay6     level=155]
    # 味方Ａ：はっ！
    voice "ch13_soldier_001"
    soldier "Yes! What can I do for you?{#ch13_soldier_001}"

    # [SPRITE   lay6     image=+715, level=155, dir=2A]
    # キュルケ：あたし、所用があって、外出しなければ
    voice "ch13_k_044"
    k "I have an errand and must go out, but I'm so scared…{#ch13_k_044}"

    # [SPRITE   lay6     image=+717, level=155, dir=2A]
    # キュルケ：さっきから、胸がどきどき高鳴っておりますの。
    voice "ch13_k_045"
    k "My heart's been pounding for a while now. Look, like this…{#ch13_k_045}"

    # [SPRITE   lay15    image=+1116, level=160, dir=1A]
    # 味方Ａ：むっ、胸が、でありますかっ！
    voice "ch13_soldier_002"
    soldier "Hm, your heart!? That must be frightening indeed!{#ch13_soldier_002}"

    # 味方Ａ：ですが、ご、ご安心ください。
    voice "ch13_soldier_003"
    soldier "But don't worry! Under Her Majesty's authority, we'll catch the evildoers!{#ch13_soldier_003}"

    # [SPRITE   lay6     image=+676, level=155, dir=1A]
    # キュルケ：うふ、頼もしい方。
    voice "ch13_k_046"
    k "My, how dependable. Have you learned anything about the bomb-thrower?{#ch13_k_046}"

    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # 味方Ａ：そ、それがですねっ！
    voice "ch13_soldier_004"
    soldier "W-Well, you see! Actually…!{#ch13_soldier_004}"

    # サイト：（あ～あ。
    s "(Oh boy. That soldier is getting all flustered by Kirche…){#ch13_s_053}"

    # サイト：（……お、俺もキュルケに迫られてる時って
    s "(…Hmm, is that the face I make when Kirche comes on to me…?){#ch13_s_054}"

    # [SPRITE   lay6     image=+678, level=155, dir=1A]
    # キュルケ：ありがとう、
    voice "ch13_k_047"
    k "Thanks, that was helpful.{#ch13_k_047}"

    # 味方Ａ：麗しき女性よ。
    voice "ch13_soldier_005"
    soldier "O beautiful lady! After this…{#ch13_soldier_005}"

    # [SPRITE   lay6     image=+709, level=155, dir=2A]
    # キュルケ：あら、だめよ。
    voice "ch13_k_048"
    k "Oh, no. I'm with darling today.{#ch13_k_048}"

    # [SPRITE   lay15    image=+1118, level=160, dir=1A]
    # 味方Ａ：……。  [voice 4217]
    voice "ch13_soldier_006"
    soldier "…{#ch13_soldier_006}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay6     image=+676, level=155, dir=1A]
    # キュルケ：ダーリン、情報は取れたわよ。  [voice 3033]
    voice "ch13_k_049"
    k "Darling, I got the information.{#ch13_k_049}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+407, level=156, dir=1B]
    # サイト：（お母さん、男性は悲しい生き物です）
    s "(Mom, men are sad creatures.){#ch13_s_055}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
label ch13_2_scene_1470:

    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：あんまり人がいないね。  [voice 10112]
    voice "ch13_s_056"
    s "There's hardly anyone here.{#ch13_s_056}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：人も集まりにくくなってるんでしょうけどね。
    voice "ch13_k_050"
    k "People are hesitant to come out too… Oh, good evening. Alone?{#ch13_k_050}"

    # サイト：（ん？
    s "(Hm? Was someone there?){#ch13_s_057}"

    # 猫：みゃあ。  [voice 955]
    voice "ch13_cat_001"
    cat "Meow.{#ch13_cat_001}"

    # サイト：（……へ？
    s "(…Eh? A cat?){#ch13_s_058}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：あら、そうなの、大変ね。
    voice "ch13_k_051"
    k "Oh, is that so, how terrible. By the way, kitty, do you know the bad bomb-thrower?{#ch13_k_051}"

    # 猫：ふみゃう……。  [voice 956]
    voice "ch13_cat_002"
    cat "Fumya…{#ch13_cat_002}"

    # サイト：（キュルケの奴……、
    s "(Kirche… is she talking to a cat?){#ch13_s_059}"

    menu:
        "Cute…{#ch13_2_c_1470_1}":
            jump ch13_2_scene_1471
        "I'll try talking too.{#ch13_2_c_1470_2}":
            jump ch13_2_scene_1472
        "Kirche broke.{#ch13_2_c_1470_3}":
            jump ch13_2_scene_1473

label ch13_2_scene_1471:

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # サイト：（か、かわいい。
    s "(C-Cute. So this is a fantasy world!){#ch13_s_060}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：……。  [voice 10113]
    voice "ch13_s_061"
    s "…{#ch13_s_061}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ん？
    voice "ch13_k_052"
    k "Hm? What's wrong, darling?{#ch13_k_052}"

    # [SPRITE   lay5     image=+434, level=160, dir=2B]
    # サイト：いや、なんというか……ほら……。
    voice "ch13_s_062"
    s "No, I just… Seeing you talk to a cat is kind of cute.{#ch13_s_062}"

    # キュルケ：え？
    voice "ch13_k_053"
    k "Eh? Really, darling. That's proper information gathering too, you know?{#ch13_k_053}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：え。
    voice "ch13_s_063"
    s "Huh? You understand cat language?{#ch13_s_063}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：うふふ。
    voice "ch13_k_054"
    k "Ufufu. Sort of.{#ch13_k_054}"

    # → next scene 1474
    jump ch13_2_scene_1474

label ch13_2_scene_1472:

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：（これがファンタジーの世界か！
    s "(So this is a fantasy world! I wonder if I can talk to cats too?){#ch13_s_064}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ダーリンどうしたの？
    voice "ch13_k_055"
    k "Darling, what's wrong? You're spacing out.{#ch13_k_055}"

    # [SPRITE   lay5     image=+434, level=160, dir=2B]
    # サイト：俺も話しかけられるのかなぁって。  [voice 10116]
    voice "ch13_s_065"
    s "I was wondering if I could talk to cats too.{#ch13_s_065}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：えっ？  [voice 3040]
    voice "ch13_k_056"
    k "Eh?{#ch13_k_056}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：おまえは何かアヤしい奴を見なかったか？  [voice 10117]
    voice "ch13_s_066"
    s "Did you see anything suspicious?{#ch13_s_066}"

    # 猫：ふにゃあ？  [voice 957]
    voice "ch13_cat_003"
    cat "Funyaa?{#ch13_cat_003}"

    # サイト：そうか……。
    voice "ch13_s_067"
    s "I see… Tell me if anything happens again.{#ch13_s_067}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ダーリン、猫の言葉が分かるの？  [voice 3041]
    voice "ch13_k_057"
    k "Darling, you understand cat language?{#ch13_k_057}"

    # [SPRITE   lay5     image=+434, level=160, dir=2B]
    # サイト：いや、全然。  [voice 10119]
    voice "ch13_s_068"
    s "No, not at all.{#ch13_s_068}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：あ、あら、そう。  [voice 3042]
    voice "ch13_k_058"
    k "O-Oh, I see.{#ch13_k_058}"

    # → next scene 1474
    jump ch13_2_scene_1474

label ch13_2_scene_1473:

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：キュ、キュルケが壊れた。  [voice 10120]
    voice "ch13_s_069"
    s "K-Kirche broke.{#ch13_s_069}"

    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：な、なによそれ！
    voice "ch13_k_059"
    k "W-What!? How rude!{#ch13_k_059}"

    # 猫：ふにゃ～～！！  [voice 958]
    voice "ch13_cat_004"
    cat "Funyaaa!!{#ch13_cat_004}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：あ～～、行っちゃった！
    voice "ch13_k_060"
    k "Aah, it ran away! Really, darling!{#ch13_k_060}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：い、いや、だって、ねぇ。
    voice "ch13_s_070"
    s "N-No, but, you see… you were talking to a cat.{#ch13_s_070}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：もしかしたら何か知ってるかも？
    voice "ch13_k_061"
    k "I thought it might know something…?{#ch13_k_061}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：へ？  [voice 10122]
    voice "ch13_s_071"
    s "Huh?{#ch13_s_071}"

    # [SPRITE   lay5     image=+434, level=160, dir=2B]
    # サイト：も、もしかして、ホントにキュルケは
    voice "ch13_s_072"
    s "M-Maybe Kirche really does understand cats…?{#ch13_s_072}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：なんとなくは分かるかも。  [voice 3046]
    voice "ch13_k_062"
    k "Maybe, just maybe I do.{#ch13_k_062}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：いっ？  [voice 10124]
    voice "ch13_s_073"
    s "Huh?{#ch13_s_073}"

    # → next scene 1474
    jump ch13_2_scene_1474

label ch13_2_scene_1474:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：まぁ、この辺の状況は、大体分かったし。
    voice "ch13_k_063"
    k "Well, I get the picture now. Shall we look around a bit more?{#ch13_k_063}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：本当ですか？  [voice 10125]
    voice "ch13_s_074"
    s "Really?{#ch13_s_074}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
label ch13_2_scene_1475:

    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あら、今日も時間通りね。  [voice 3048]
    voice "ch13_k_064"
    k "Oh, right on time today.{#ch13_k_064}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：キュルケ？  [voice 10126]
    voice "ch13_s_075"
    s "Kirche?{#ch13_s_075}"

    # 情報屋：……貴族のお嬢さま。
    voice "ch13_informant_001"
    informant "…A noble young lady. 'Lend me one light, please.'{#ch13_informant_001}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：うわっ！  [voice 10127]
    voice "ch13_s_076"
    s "Whoa!{#ch13_s_076}"

    # キュルケ：あら、『１つでいいの？』  [voice 3049]
    voice "ch13_k_065"
    k "Oh, 'just one'?{#ch13_k_065}"

    # 情報屋：『……火を２つもあわせれば、
    voice "ch13_informant_002"
    informant "'…Put two flames together and it becomes a blaze, you see.'{#ch13_informant_002}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：ダーリン、安心して。
    voice "ch13_k_066"
    k "Darling, relax. It's the informant.{#ch13_k_066}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：どこにいるか、分からないんですが……。  [voice 10128]
    voice "ch13_s_077"
    s "I can't see where they are…{#ch13_s_077}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：そりゃ、そうよ。
    voice "ch13_k_067"
    k "Of course not. They're not amateurs who'd reveal themselves here.{#ch13_k_067}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：そういうものなんですか？  [voice 10129]
    voice "ch13_s_078"
    s "Is that how it works?{#ch13_s_078}"

    # 情報屋：これ、報告書でさぁ。  [voice 2648]
    voice "ch13_informant_003"
    informant "Here's the report.{#ch13_informant_003}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：はいはい。
    voice "ch13_k_068"
    k "Yes, yes. Certainly. Good work.{#ch13_k_068}"

    # 情報屋：気をつけてくだせえ。
    voice "ch13_informant_004"
    informant "Be careful. Those young ladies are being targeted.{#ch13_informant_004}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：分かってるわ。
    voice "ch13_k_069"
    k "I know. Here's your payment…{#ch13_k_069}"

    # 情報屋：へっへぇ……。  [voice 2650]
    voice "ch13_informant_005"
    informant "Heh heh…{#ch13_informant_005}"

    # サイト：情報屋って……。  [voice 10130]
    voice "ch13_s_079"
    s "An informant, huh…{#ch13_s_079}"

    menu:
        "They're targeting you? Are you all right?{#ch13_2_c_1475_1}":
            jump ch13_2_scene_1476
        "Can you trust them?{#ch13_2_c_1475_2}":
            jump ch13_2_scene_1477
        "W-Where did you meet them?{#ch13_2_c_1475_3}":
            jump ch13_2_scene_1478

label ch13_2_scene_1476:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：狙われてるって、大丈夫なのか？  [voice 10131]
    voice "ch13_s_080"
    s "They're targeting you? Are you all right?{#ch13_s_080}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：あら、心配してくれてるの？  [voice 3054]
    voice "ch13_k_070"
    k "My, are you worried about me?{#ch13_k_070}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：うふふ、大丈夫。  [voice 3055]
    voice "ch13_k_071"
    k "Ufufu, it's fine.{#ch13_k_071}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：この微熱のキュルケとダーリンのコンビに
    voice "ch13_k_072"
    k "Nobody can beat the combo of Kirche with a slight fever and darling!{#ch13_k_072}"

    # → next scene 1479
    jump ch13_2_scene_1479

label ch13_2_scene_1477:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：信用できるのか？  [voice 10132]
    voice "ch13_s_081"
    s "Can you trust them?{#ch13_s_081}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：さあ、どうかしら？  [voice 3057]
    voice "ch13_k_073"
    k "Well, who knows?{#ch13_k_073}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：おいおい。  [voice 10133]
    voice "ch13_s_082"
    s "Hey now.{#ch13_s_082}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # → next scene 1479
    jump ch13_2_scene_1479

label ch13_2_scene_1478:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：ど、どこで知り合ったんだ？
    voice "ch13_s_083"
    s "W-Where did you meet someone like that…?{#ch13_s_083}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：うふふ……。
    voice "ch13_k_074"
    k "Ufufu… A girl needs her secrets.{#ch13_k_074}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：普通の女の子の秘密じゃねーだろ。  [voice 10135]
    voice "ch13_s_084"
    s "That's not an ordinary girl's secret, is it…?{#ch13_s_084}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # → next scene 1479
    jump ch13_2_scene_1479

label ch13_2_scene_1479:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # キュルケ：もう少し、調べて回りましょうか？  [voice 3059]
    voice "ch13_k_075"
    k "Shall we look around a bit more?{#ch13_k_075}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
label ch13_2_scene_1480:

    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SE       se1      play=+37]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：こんな時間なのに、結構、人がいるわね。  [voice 3060]
    voice "ch13_k_076"
    k "It's late, but there are quite a few people here.{#ch13_k_076}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：そりゃまあ、市場が開くのは朝一番だからな。  [voice 10136]
    voice "ch13_s_085"
    s "Well, the market opens at dawn.{#ch13_s_085}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：あら、この果物おいしい！  [voice 3061]
    voice "ch13_k_077"
    k "Oh, this fruit is delicious!{#ch13_k_077}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：いきなり果物食べてるし。  [voice 10137]
    voice "ch13_s_086"
    s "Eating fruit all of a sudden…{#ch13_s_086}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：調査をするんじゃなかったのかよ！  [voice 10138]
    voice "ch13_s_087"
    s "Weren't we supposed to be investigating!?{#ch13_s_087}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：あら、いいじゃない、
    voice "ch13_k_078"
    k "Oh, it's fine. It looked delicious. And I got information too.{#ch13_k_078}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：そ、そなの？  [voice 10139]
    voice "ch13_s_088"
    s "R-Really?{#ch13_s_088}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：市場の人は、意外と情報通なのよ。  [voice 3063]
    voice "ch13_k_079"
    k "Market people are surprisingly well-informed.{#ch13_k_079}"

    menu:
        "Accept it.{#ch13_2_c_1480_1}":
            jump ch13_2_scene_1481
        "Look suspicious.{#ch13_2_c_1480_2}":
            jump ch13_2_scene_1482
        "I'll have one too.{#ch13_2_c_1480_3}":
            jump ch13_2_scene_1483

label ch13_2_scene_1481:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SE       se1      play=+37]
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：なるほど……。  [voice 10140]
    voice "ch13_s_089"
    s "I see…{#ch13_s_089}"

    # [SPRITE   lay5     image=+434, level=160, dir=2B]
    # サイト：なにか情報が手に入ったのか？  [voice 10141]
    voice "ch13_s_090"
    s "Did you get any information?{#ch13_s_090}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：え、ええ、もちろん。  [voice 3064]
    voice "ch13_k_080"
    k "E-Eh, of course.{#ch13_k_080}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：美味しい果物の見分け方とか……、
    voice "ch13_k_081"
    k "Like how to tell delicious fruit… or how to catch a boy's eye…{#ch13_k_081}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：知ってる？
    voice "ch13_k_082"
    k "You know? Wrap vegetables in wet paper and they last longer.{#ch13_k_082}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：そんな情報は要らないって。  [voice 10142]
    voice "ch13_s_091"
    s "I don't need that kind of information.{#ch13_s_091}"

    # → next scene 1484
    jump ch13_2_scene_1484

label ch13_2_scene_1482:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SE       se1      play=+37]
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：本当かぁ？
    voice "ch13_s_092"
    s "Really? Well, I suppose market people are well-informed.{#ch13_s_092}"

    # サイト：果物ひとつでそんな重要な情報を
    voice "ch13_s_093"
    s "Would they really give you important info for one fruit?{#ch13_s_093}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：うーん。
    voice "ch13_k_083"
    k "Mm. Well, information at that price.{#ch13_k_083}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：でも、いいじゃない。
    voice "ch13_k_084"
    k "But it's fine. This fruit is delicious. Want to try some, darling?{#ch13_k_084}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：い、今はそれどころじゃないだろ！  [voice 10145]
    voice "ch13_s_094"
    s "N-Now's not the time for that!{#ch13_s_094}"

    # → next scene 1484
    jump ch13_2_scene_1484

label ch13_2_scene_1483:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SE       se1      play=+37]
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：はあ、なんだか俺もお腹がすいてきたな。
    voice "ch13_s_095"
    s "Sigh, I'm getting hungry too. I'll take one.{#ch13_s_095}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：うふふ。
    voice "ch13_k_085"
    k "Ufufu. Eating like this, just the two of us, feels like a date.{#ch13_k_085}"

    # [SPRITE   lay5     image=+434, level=160, dir=2B]
    # サイト：そ、そういえば……そうだな。  [voice 10147]
    voice "ch13_s_096"
    s "N-Now that you mention it… yeah.{#ch13_s_096}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：夜の街で、こうして食事して……。  [voice 3070]
    voice "ch13_k_086"
    k "Eating in the night city like this…{#ch13_k_086}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：これが豪華な食事だったら、
    voice "ch13_s_097"
    s "If it were a lavish meal, maybe.{#ch13_s_097}"

    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：あら、ダーリンと一緒だったら、
    voice "ch13_k_087"
    k "Oh, with darling, anything tastes like the best meal.{#ch13_k_087}"

    # [SPRITE   lay5     image=+442, level=160, dir=2B]
    # サイト：なんか、照れちまうな。  [voice 10149]
    voice "ch13_s_098"
    s "I'm getting embarrassed…{#ch13_s_098}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：もう、ダーリンかわいいんだから！  [voice 3072]
    voice "ch13_k_088"
    k "Really, darling, you're so cute!{#ch13_k_088}"

    # → next scene 1484
    jump ch13_2_scene_1484

label ch13_2_scene_1484:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SE       se1      play=+37]
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # サイト：（本当に大丈夫かな……？）
    s "(Is it really all right…?){#ch13_s_099}"

    # [SE       se1      stop=1]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ЧАСТИ 2 ====
    jump ch13_3
    return

