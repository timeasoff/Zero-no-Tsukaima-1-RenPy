# Глава 14, часть 3 (сцены 599–608): возвращение, спасение Кирке, «братишка».
# Источник: ps2_source/chapters/chapter_15_私のお兄ちゃん.txt (SCENE 599-608).

label ch14_3:
    $ tndl(None)
    $ show_sprites()

    # → next scene 582
    jump ch14_4

    # → next scene 582
    jump ch14_4

    # → next scene 582
    jump ch14_4

    # → next scene 583
    jump ch14_4

    # → next scene 587
    jump ch14_4

    # → next scene 587
    jump ch14_4

    # → next scene 587
    jump ch14_4

    # → next scene 588
    jump ch14_4

    # → next scene 1485
    jump ch14_4

    # → next scene 1486
    jump ch14_4

    # → next scene 1487
    jump ch14_4

    # → next scene 1488
    jump ch14_4

    # → next scene 594
    jump ch14_4

    # → next scene 598
    jump ch14_4

    # → next scene 598
    jump ch14_4

    # → next scene 598
    jump ch14_4

    # → next scene 599
    jump ch14_3_scene_599

label ch14_3_scene_599:

    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # サイト：（追っ手を振り切った俺は、
    s "(I shook off the pursuers and somehow made it back to the inn…){#ch14_s_076}"

    # サイト：おい、ルイズ！
    voice "ch14_s_077"
    s "Hey, Louise! Open up! Louise!!{#ch14_s_077}"

    # [SPRITE   lay5     hide]
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+324, level=160, dir=1C]
    # ルイズ：誰？
    voice "ch14_l_006"
    l "Who is it? Saito?{#ch14_l_006}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：や、やぁ……。  [voice 12964]
    voice "ch14_s_078"
    s "Y-Yeah…{#ch14_s_078}"

    # [SPRITE   lay1     image=+330, level=160, dir=1C]
    # ルイズ：サ、サイト！？
    voice "ch14_l_007"
    l "Sa-Saito!? W-What happened to you! You're all battered!{#ch14_l_007}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+548, level=160, dir=2C]
    # シエスタ：きゃあっ！
    voice "ch14_si_001"
    si "Eek! Saito-san, hold on!{#ch14_si_001}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay3     image=+880, level=160, dir=1C]
    # モンモランシー：ええっ！？
    voice "ch14_m_001"
    m "Eh!? A-Are you all right!?{#ch14_m_001}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：俺は大丈夫……。
    voice "ch14_s_079"
    s "I'm fine… Hurry, we have to get to Kirche…!{#ch14_s_079}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay1     image=+324, level=160, dir=1C]
    # ルイズ：キュルケの元？
    voice "ch14_l_008"
    l "To Kirche? What happened, Saito!{#ch14_l_008}"

    # サイト：巡回の途中で、ウェザリーの罠に
    voice "ch14_s_080"
    s "We walked into Weatherly's trap during the patrol.{#ch14_s_080}"

    # [SPRITE   lay1     image=+328, level=160, dir=1C]
    # ルイズ：ちょっと、ウェザリーの罠……って
    voice "ch14_l_009"
    l "Wait, Weatherly's trap—what do you mean!?{#ch14_l_009}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：俺達が追っていた爆弾使いの裏には
    voice "ch14_s_081"
    s "Weatherly was behind the bomb-thrower we were chasing.{#ch14_s_081}"

    # ルイズ：な、なんですって！？  [voice 7013]
    voice "ch14_l_010"
    l "W-What!?{#ch14_l_010}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：キュルケはそれに気づいたらしく、
    voice "ch14_s_082"
    s "Kirche must have noticed too. We were following her, but… we were spotted and led into a trap…{#ch14_s_082}"

    # [SPRITE   lay1     image=+324, level=160, dir=1C]
    # ルイズ：……。  [voice 7014]
    voice "ch14_l_011"
    l "…{#ch14_l_011}"

    # [SPRITE   lay1     image=+328, level=160, dir=1C]
    # ルイズ：なんで、そんな重要なこと、
    voice "ch14_l_012"
    l "Why didn't you tell us something so important? We could have done something!{#ch14_l_012}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：それは後で説明する！
    voice "ch14_s_083"
    s "I'll explain later! We need to get to Kirche now… Ugh…{#ch14_s_083}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay3     image=+878, level=160, dir=1C]
    # モンモランシー：暴れないで！
    voice "ch14_m_002"
    m "Don't struggle! It'll make the Healing harder.{#ch14_m_002}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：頼む、ルイズ。
    voice "ch14_s_084"
    s "Please, Louise. Save Kirche!{#ch14_s_084}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay1     image=+324, level=160, dir=1C]
    # ルイズ：もう……。
    voice "ch14_l_013"
    l "Honestly… I'd do it without being asked! Everyone, let's go!{#ch14_l_013}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+610, level=160, dir=1C]
    # タバサ：うん。  [voice 15779]
    voice "ch14_t_001"
    t "Mm.{#ch14_t_001}"

    # [SPRITE   lay1     image=+330, level=160, dir=1C]
    # ルイズ：まったくキュルケったら、
    voice "ch14_l_014"
    l "Really, Kirche, what were you thinking…!{#ch14_l_014}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：（急がないと……。
    s "(Hurry… Kirche…){#ch14_s_085}"

    # 【移動】 → extra 1489/1490/1491
    menu:
        "Corridor{#ch14_3_c_599_1}":
            jump ch14_4_scene_1489
        "The main street{#ch14_3_c_599_2}":
            jump ch14_4_scene_1490
        "The back alley{#ch14_3_c_599_3}":
            jump ch14_4_scene_1491

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
label ch14_3_scene_600:

    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
label ch14_3_scene_601:

    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
label ch14_3_scene_602:

    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
label ch14_3_scene_603:

    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
label ch14_3_scene_604:

    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：くそっ、キュルケ、
    voice "ch14_s_086"
    s "Damn it, Kirche, where did you go!?{#ch14_s_086}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay7     image=+966, level=160, dir=1B]
    # ハルナ：平賀くーんっ！
    voice "ch14_ha_001"
    ha "Hiraga-kuuun! It's Kirche-san!{#ch14_ha_001}"

    # サイト：見つかったのかっ！？
    voice "ch14_s_087"
    s "You found her!? Is she all right!?{#ch14_s_087}"

    # [SPRITE   lay7     image=+968, level=160, dir=1B]
    # ハルナ：道に倒れていたの。
    voice "ch14_ha_002"
    ha "She was lying in the road. Badly hurt, but it looks like her life isn't in danger…{#ch14_ha_002}"

    # サイト：くそっ！
    voice "ch14_s_088"
    s "Damn! I should have been with her!{#ch14_s_088}"

    # [SPRITE   lay7     image=+966, level=160, dir=1B]
    # ハルナ：あ、平賀くん、待って！  [voice 2450]
    voice "ch14_ha_003"
    ha "Ah, Hiraga-kun, wait!{#ch14_ha_003}"

    # [SPRITE   lay3     x=304, y=416]
    # [SPRITE   lay1     x=304, y=416]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     x=304, y=416]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     x=304, y=416]
    # [LAYER    lay0     x=304, y=416]
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+251, level=80]
    $ dissolve_fx("id(251)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：キュルケ！
    voice "ch14_s_089"
    s "Kirche! Are you all right!{#ch14_s_089}"

    # ルイズ：安心して。
    voice "ch14_l_015"
    l "Relax. She's breathing. No broken bones, it seems.{#ch14_l_015}"

    # モンモランシー：いま治癒をしてるから、静かにして。  [voice 4126]
    voice "ch14_m_003"
    m "I'm healing her now, so be quiet.{#ch14_m_003}"

    # サイト：良かった。  [voice 12975]
    voice "ch14_s_090"
    s "Thank goodness.{#ch14_s_090}"

    # モンモランシー：ふう。
    voice "ch14_m_004"
    m "Whew. I've restored her somewhat with magic, so she can move now.{#ch14_m_004}"

    # モンモランシー：あとは宿につれていって、安静にしないと……。  [voice 4128]
    voice "ch14_m_005"
    m "After that, we need to take her to the inn and keep her still…{#ch14_m_005}"

    # キュルケ：んっ……。  [voice 3742]
    voice "ch14_k_071"
    k "Mm…{#ch14_k_071}"

    # サイト：キュルケ！
    voice "ch14_s_091"
    s "Kirche! You're awake?{#ch14_s_091}"

    # モンモランシー：だめよ！
    voice "ch14_m_006"
    m "No! Don't shake her…!{#ch14_m_006}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：……。
    k "…{#ch14_k_072}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：……キュルケ？  [voice 12977]
    voice "ch14_s_092"
    s "…Kirche?{#ch14_s_092}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：……？  [voice 3743]
    voice "ch14_k_073"
    k "…?{#ch14_k_073}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……？  [voice 15780]
    voice "ch14_t_002"
    t "…?{#ch14_t_002}"

    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：……？  [voice 3744]
    voice "ch14_k_074"
    k "…?{#ch14_k_074}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：……な、なんだよ。
    voice "ch14_s_093"
    s "…What's going on? Hey, Kirche, what's wrong with you?{#ch14_s_093}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：……。
    k "…{#ch14_k_075}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：ギーシュと春奈が倒れてるキュルケを
    voice "ch14_s_094"
    s "Guiche and Haruna found Kirche lying down, and Montmorency treated her.{#ch14_s_094}"

    # [SPRITE   lay5     image=+403, level=160, dir=1B]
    # サイト：さぁ、後は宿に戻って安静にしてようぜ。  [voice 12980]
    voice "ch14_s_095"
    s "Come on, let's get back to the inn and rest.{#ch14_s_095}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：……。
    k "…{#ch14_k_076}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：おい、キュルケ、大丈夫か？
    voice "ch14_s_096"
    s "Hey, Kirche, are you all right? Do you know me?{#ch14_s_096}"

    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：おにいちゃん。  [voice 3745]
    voice "ch14_k_077"
    k "Big brother.{#ch14_k_077}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：へっ？  [voice 12982]
    voice "ch14_s_097"
    s "Huh?{#ch14_s_097}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+252, level=80]
    $ dissolve_fx("id(252)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # キュルケ：おにいちゃ～～ん！  [voice 3746]
    voice "ch14_k_078"
    k "Big broooother!{#ch14_k_078}"

    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # サイト：う、うわぁっ！
    voice "ch14_s_098"
    s "W-Whoa! Don't hug me all of a sudden!{#ch14_s_098}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：お？  [voice 7019]
    voice "ch14_l_016"
    l "Oh?{#ch14_l_016}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：にい？  [voice 15070]
    voice "ch14_si_002"
    si "Bro-?{#ch14_si_002}"

    # [SPRITE   lay2     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：ちゃん。  [voice 15781]
    voice "ch14_t_003"
    t "-ther.{#ch14_t_003}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+307, level=140, dir=1A]
    # ルイズ：な、なによそれはぁぁっ？  [voice 7020]
    voice "ch14_l_017"
    l "W-What was that!?{#ch14_l_017}"

    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+252, level=80]
    $ dissolve_fx("id(252)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：ほら、キュルケ。
    voice "ch14_l_018"
    l "Come on, Kirche. Stop with the bad joke!{#ch14_l_018}"

    # [EVENT_CG event    image=+253, level=80]
    $ dissolve_fx("id(253)")
    # キュルケ：うる……。  [voice 3747]
    voice "ch14_k_079"
    k "Shut u…{#ch14_k_079}"

    # ルイズ：な、何よ。
    voice "ch14_l_019"
    l "What? Even if you cry, I won't forgive you.{#ch14_l_019}"

    # ルイズ：第一、わたしに黙ってウェザリーを
    voice "ch14_l_020"
    l "Besides, chasing Weatherly without telling me is how you ended up like this…{#ch14_l_020}"

    # キュルケ：おにいちゃん。
    voice "ch14_k_080"
    k "Big brother. This one is scary…{#ch14_k_080}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：お、おい、キュルケ。
    voice "ch14_s_099"
    s "H-Hey, Kirche. Don't cling to my back.{#ch14_s_099}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：サイト！
    voice "ch14_l_021"
    l "Saito! Since when are you Kirche's big brother!?{#ch14_l_021}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：お、俺は知らん！
    voice "ch14_s_100"
    s "I-I don't know! I don't know anything!{#ch14_s_100}"

    # ルイズ：じゃあそのバカ犬に抱きついてる
    voice "ch14_l_022"
    l "Then what's this Kirche clinging to you!?{#ch14_l_022}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：説明してくださいますよね？  [voice 15071]
    voice "ch14_si_003"
    si "You'll explain, won't you?{#ch14_si_003}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：せ、説明って……。  [voice 12986]
    voice "ch14_s_101"
    s "E-Explain what…{#ch14_s_101}"

    menu:
        "Kirche apparently is my sister{#ch14_3_c_604_1}":
            jump ch14_3_scene_605
        "It must be a mistake{#ch14_3_c_604_2}":
            jump ch14_3_scene_606
        "Did everyone mishear?{#ch14_3_c_604_3}":
            jump ch14_3_scene_607

label ch14_3_scene_605:

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：キ、キュルケは俺の妹だったらしい……。  [voice 12987]
    voice "ch14_s_102"
    s "K-Kirche is apparently my sister…{#ch14_s_102}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：おにいちゃんうれしい。  [voice 3749]
    voice "ch14_k_081"
    k "Big brother, I'm happy.{#ch14_k_081}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：そんなわけあるはずないでしょ！  [voice 7026]
    voice "ch14_l_023"
    l "That can't be true!{#ch14_l_023}"

    # → next scene 608
    jump ch14_3_scene_608

label ch14_3_scene_606:

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：な、なにかの間違いだ！
    voice "ch14_s_103"
    s "I-It's a mistake! Kirche my sister, really—it can't be!{#ch14_s_103}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：そんなことは分かってるわよ！  [voice 7027]
    voice "ch14_l_024"
    l "We know that!{#ch14_l_024}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：それでは、女の子にお兄ちゃんと
    voice "ch14_si_004"
    si "Then it's a game where you make a girl call you 'big brother'?{#ch14_si_004}"

    # [SPRITE   lay2     image=+497, level=160, dir=1A]
    # シエスタ：だったら、わたしに言ってくれれば
    voice "ch14_si_005"
    si "If so, you could have told me. I'd call you 'big brother' anytime…{#ch14_si_005}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：ま、待て！
    voice "ch14_s_104"
    s "W-Wait! I have no 'little sister' attribute!{#ch14_s_104}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：今キュルケに、グッと来てるのは
    voice "ch14_s_105"
    s "This feeling Kirche is giving me must be my imagination!{#ch14_s_105}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # → next scene 608
    jump ch14_3_scene_608

label ch14_3_scene_607:

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：みんなの聞き間違いだよ。  [voice 12991]
    voice "ch14_s_106"
    s "You all misheard.{#ch14_s_106}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+252, level=80]
    $ dissolve_fx("id(252)")
    # [TRANS trans("crossfade", 1000)]
    # キュルケ：おにいちゃん。
    voice "ch14_k_082"
    k "Big brother. Big brother.{#ch14_k_082}"

    # サイト：は、はうっ。
    voice "ch14_s_107"
    s "U-Ugh. Kirche, when you call me that with such innocent eyes…{#ch14_s_107}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # ルイズ：うふふ……。
    voice "ch14_l_025"
    l "Ufufu… Saito, you seem to hear it just fine.{#ch14_l_025}"

    # サイト：はうう。
    voice "ch14_s_108"
    s "Ugh. So it wasn't a hallucination!{#ch14_s_108}"

    # → next scene 608
    jump ch14_3_scene_608

label ch14_3_scene_608:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：ま、待てルイズ。
    voice "ch14_s_109"
    s "Wait, Louise. I don't understand any of this either.{#ch14_s_109}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：あくまでごまかす気なのね……。  [voice 7029]
    voice "ch14_l_026"
    l "You're just trying to dodge the question…{#ch14_l_026}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ひ、ひぃっっっ！  [voice 12995]
    voice "ch14_s_110"
    s "E-Eek!{#ch14_s_110}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # モンモランシー：いいかげんにしなさい！
    voice "ch14_m_007"
    m "Stop it, you two!{#ch14_m_007}"

    # [SPRITE   lay3     image=+889, level=160, dir=2A]
    # モンモランシー：よく分からないけど、
    voice "ch14_m_008"
    m "I don't understand either, but Kirche is frightened, isn't she!?{#ch14_m_008}"

    # [SPRITE   lay3     x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：そうそう。  [voice 15782]
    voice "ch14_t_004"
    t "That's right.{#ch14_t_004}"

    # [SPRITE   lay3     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：……。  [voice 3751]
    voice "ch14_k_083"
    k "…{#ch14_k_083}"

    # [SPRITE   lay6     x=224, y=0]
    # [LAYER    lay0     image=+590, level=160, dir=1A]
    # タバサ：よしよし。  [voice 15783]
    voice "ch14_t_005"
    t "There, there.{#ch14_t_005}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：な、なによ。
    voice "ch14_l_027"
    l "W-What is this? It's like I'm the bad one…{#ch14_l_027}"

    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+253, level=80]
    $ dissolve_fx("id(253)")
    # [TRANS trans("crossfade", 1000)]
    # キュルケ：お、おにいちゃんをいじめないで……。  [voice 3752]
    voice "ch14_k_084"
    k "O-Onii-chan. Don't be mean to him…{#ch14_k_084}"

    # ルイズ：……うっ。  [voice 7031]
    voice "ch14_l_028"
    l "…Ugh.{#ch14_l_028}"

    # サイト：……な、なあ、モンモン。
    voice "ch14_s_111"
    s "…Say, Montmon. What's wrong with Kirche?{#ch14_s_111}"

    # モンモランシー：い、いま調べるからちょっと待って！  [voice 4132]
    voice "ch14_m_009"
    m "I-I'm checking now, wait a moment!{#ch14_m_009}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay3     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # → next scene 609
    jump ch14_4

    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     hide]
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [LAYER    lay0     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # → next scene 613
    jump ch14_4

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # → next scene 613
    jump ch14_4

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+431, level=160, dir=2A]
    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # → next scene 613
    jump ch14_4

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay5     x=464, y=416]
    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay1     x=-96, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # [SPRITE   lay1     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # [SPRITE   lay3     x=-96, y=0]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # [SPRITE   lay3     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay3     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 614
    jump ch14_4

    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [LAYER    lay0     image=+590, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [LAYER    lay0     image=+590, level=160, dir=1A]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [LAYER    lay0     image=+590, level=160, dir=1A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # → next scene 618
    jump ch14_4

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [LAYER    lay0     image=+590, level=160, dir=1A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # → next scene 618
    jump ch14_4

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [LAYER    lay0     image=+590, level=160, dir=1A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # → next scene 618
    jump ch14_4

    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [BG       stage    hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay7     image=+962, level=160, dir=1B]
    # [SPRITE   lay7     x=224, y=0]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay7     image=+968, level=160, dir=1B]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay7     image=+962, level=160, dir=1B]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay7     image=+968, level=160, dir=1B]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [EVENT_CG event    image=+254, level=80]
    $ dissolve_fx("id(254)")
    # [TRANS trans("crossfade", 1000)]
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
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+14]
    play music t13 fadein 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+252, level=80]
    $ dissolve_fx("id(252)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [EVENT_CG event    image=+253, level=80]
    $ dissolve_fx("id(253)")
    # [BGM      bgm      play=+14]
    play music t13 fadein 1.0
    # [EVENT_CG event    image=+253, level=80]
    $ dissolve_fx("id(253)")
    # [EVENT_CG event    image=+252, level=80]
    $ dissolve_fx("id(252)")
    # → next scene 1193
    jump ch14_4

    # [BGM      bgm      play=+14]
    play music t13 fadein 1.0
    # [EVENT_CG event    image=+253, level=80]
    $ dissolve_fx("id(253)")
    # [EVENT_CG event    image=+252, level=80]
    $ dissolve_fx("id(252)")
    # → next scene 1193
    jump ch14_4

    # [BGM      bgm      play=+14]
    play music t13 fadein 1.0
    # [EVENT_CG event    image=+253, level=80]
    $ dissolve_fx("id(253)")
    # [EVENT_CG event    image=+252, level=80]
    $ dissolve_fx("id(252)")
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # → next scene 1193
    jump ch14_4

    # [BGM      bgm      play=+14]
    play music t13 fadein 1.0
    # [EVENT_CG event    image=+252, level=80]
    $ dissolve_fx("id(252)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    hide]
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [COFFEE]
    $ pause(1.0)
    # → next scene 619
    jump ch14_4

    # [BG       stage    image=+64, level=200]
    $ fade_fx("id(64)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SE       se1      play=+37]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [SE       se1      stop=1]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+64, level=200]
    $ fade_fx("id(64)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [LAYER    lay0     x=224, y=0]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # [SPRITE   lay3     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [LAYER    lay0     hide]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay3     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay4     hide]
    # [SPRITE   lay7     image=+966, level=160, dir=1B]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay7     image=+968, level=160, dir=1B]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay4     image=+559, level=160, dir=1A]
    # [SPRITE   lay4     hide]
    # [SPRITE   lay7     image=+962, level=160, dir=1B]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [SPRITE   lay7     image=+966, level=160, dir=1B]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ЧАСТИ 3 ====
    jump ch14_4
    return

