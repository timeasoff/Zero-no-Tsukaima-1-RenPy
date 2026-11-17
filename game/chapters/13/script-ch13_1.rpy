# Глава 13, часть 1 (сцены 549–563): «炎の予感» — спор, соревнование, ночной план.
# Источник: ps2_source/chapters/chapter_14_炎の予感.txt (SCENE 549-563).

label ch13:
    $ tndl(None)
    $ show_sprites()

label ch13_1_scene_549:

    # [TITLE title("炎の予感")]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # サイト：（演劇が終わってから、かれこれ数日。
    s "(Several days have passed since the play ended. Still no trace of the bomb-thrower…){#ch13_s_001}"

    # サイト：（調査は続けてるんだけど、
    s "(I keep investigating, but I can't get any solid leads. Louise is in a bad mood too…){#ch13_s_002}"

    # サイト：（しかし、いつまでこの状態が
    s "(How long is this going to last…?){#ch13_s_003}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1158, level=200]
    $ fade_fx("id(1158)")
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
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SE       se0      play=+57]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：お帰りなさいませ。
    voice "ch13_si_001"
    si "Welcome home, Miss Valliere. Saito-san.{#ch13_si_001}"

    # [SE       se0      play=+56]
    # [SPRITE   lay2     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：はぁ……、ダメね。
    voice "ch13_l_001"
    l "Sigh… No luck again today.{#ch13_l_001}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：お気を落とさないでください。
    voice "ch13_si_002"
    si "Don't be discouraged. I'll make some tea.{#ch13_si_002}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     hide]
    # [SE       se0      play=+57]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：今、戻ったわ。  [voice 3615]
    voice "ch13_k_001"
    k "I'm back.{#ch13_k_001}"

    # [SPRITE   lay6     x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：ただいま。  [voice 15773]
    voice "ch13_t_001"
    t "I'm home.{#ch13_t_001}"

    # [SE       se0      play=+56]
    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そっちはどう？  [voice 6968]
    voice "ch13_l_002"
    l "How did it go on your end?{#ch13_l_002}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：全然ダメね。
    voice "ch13_k_002"
    k "No luck at all. Judging by that face, same for you?{#ch13_k_002}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：ハァ。  [voice 6969]
    voice "ch13_l_003"
    l "Haa.{#ch13_l_003}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：もうっ、シケた顔しないでよ！
    voice "ch13_k_003"
    k "Ugh, don't make that gloomy face! With that look you'll never get fired up when it counts!{#ch13_k_003}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：キュルケが能天気すぎるのよ。  [voice 6970]
    voice "ch13_l_004"
    l "Kirche is too carefree.{#ch13_l_004}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+112, level=80]
    $ dissolve_fx("id(112)")
    # [TRANS trans("crossfade", 1000)]
    # キュルケ：むっ、なによ！  [voice 3618]
    voice "ch13_k_004"
    k "Hmph, what's that!?{#ch13_k_004}"

    # ルイズ：こうしてる間にも、爆弾使いの被害が
    voice "ch13_l_005"
    l "Even while we sit here, the bomb-thrower's damage may be spreading.{#ch13_l_005}"

    # キュルケ：だからってイライラしてても
    voice "ch13_k_005"
    k "Getting worked up won't help! At this rate you'll never catch them.{#ch13_k_005}"

    # [EVENT_CG event    image=+113, level=80]
    $ dissolve_fx("id(113)")
    # ルイズ：な、なんですって！  [voice 6972]
    voice "ch13_l_006"
    l "W-What did you say!?{#ch13_l_006}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：お、おいっ！
    voice "ch13_s_004"
    s "H-Hey! You two!{#ch13_s_004}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # ルイズ：なによ！  [voice 6973]
    voice "ch13_l_007"
    l "What!?{#ch13_l_007}"

    # キュルケ：なにかしら、ダーリン？  [voice 3620]
    voice "ch13_k_006"
    k "What is it, darling?{#ch13_k_006}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：な、なんでもないでしゅぅ……。  [voice 12844]
    voice "ch13_s_005"
    s "N-Nothing at all…{#ch13_s_005}"

    # サイト：（女って、こ、怖い……）
    s "(Women are… scary…){#ch13_s_006}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：で、でも。
    voice "ch13_s_007"
    s "B-But… fighting isn't good…{#ch13_s_007}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：そうね。
    voice "ch13_k_007"
    k "Right. Then let's do this.{#ch13_k_007}"

    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：へっ？  [voice 6974]
    voice "ch13_l_008"
    l "Huh?{#ch13_l_008}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：２組に分かれて、どちらが先に爆弾使いを
    voice "ch13_k_008"
    k "Split into two teams and see who catches the bomb-thrower first. How about a contest?{#ch13_k_008}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：おいおいキュルケ。  [voice 12846]
    voice "ch13_s_008"
    s "Hey now, Kirche.{#ch13_s_008}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：負けた方は勝った方の命令を聞くこと！
    voice "ch13_k_009"
    k "The loser obeys the winner's orders! How does that sound?{#ch13_k_009}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：姫さまからの依頼なのよ。
    voice "ch13_l_009"
    l "It's a request from the Princess. A contest is improper.{#ch13_l_009}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：いいじゃない。
    voice "ch13_k_010"
    k "Oh, come on. Don't they say team competitions improve overall efficiency?{#ch13_k_010}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：そういうこともあるかもしれないけど……。  [voice 6976]
    voice "ch13_l_010"
    l "That may be true, but…{#ch13_l_010}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：は～～い！
    voice "ch13_k_011"
    k "Haaaaay! Then it's decided! And darling, you're on my team.{#ch13_k_011}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ちょ、ちょっと待ちなさいよ！
    voice "ch13_l_011"
    l "W-Wait a moment! Why would he be on your team!?{#ch13_l_011}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：あら、ダーリンがいないと、
    voice "ch13_k_012"
    k "My, without darling, are you worried, Louise?{#ch13_k_012}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：そ、そんなことないもん！  [voice 6978]
    voice "ch13_l_012"
    l "T-That's not it at all!{#ch13_l_012}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：じゃあ、決定ね！  [voice 3627]
    voice "ch13_k_013"
    k "Then it's decided!{#ch13_k_013}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：あううう……。  [voice 6979]
    voice "ch13_l_013"
    l "Uuu…{#ch13_l_013}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：じ、じゃあそのかわり！
    voice "ch13_l_014"
    l "T-Then instead! I get to use everyone else!{#ch13_l_014}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ええ、いいわよ。  [voice 3628]
    voice "ch13_k_014"
    k "Sure, fine.{#ch13_k_014}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：わ、分かったわ！
    voice "ch13_l_015"
    l "F-Fine! If I win, you'll attend class standing on your head!{#ch13_l_015}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：そ、それでもいいの？
    voice "ch13_l_016"
    l "Y-You're fine with that? You can still back out now, you know.{#ch13_l_016}"

    # キュルケ：いーわよ。
    voice "ch13_k_015"
    k "Sure. In return, if I win…{#ch13_k_015}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：そうねぇ。
    voice "ch13_k_016"
    k "Let me see… How about you be my maid for a day?{#ch13_k_016}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：わ、分かったわよ。
    voice "ch13_l_017"
    l "F-Fine! Don't blame me if you regret it!{#ch13_l_017}"

    # サイト：（なんだか、俺の知らないところで、
    s "(Somehow, things are being decided without me…){#ch13_s_009}"

    menu:
        "Object.{#ch13_1_c_549_1}":
            jump ch13_1_scene_550
        "Accept it.{#ch13_1_c_549_2}":
            jump ch13_1_scene_551
        "Pout a little.{#ch13_1_c_549_3}":
            jump ch13_1_scene_552

label ch13_1_scene_550:

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：おいおい、俺の意見は聞かないのかよ。  [voice 12847]
    voice "ch13_s_010"
    s "Hey, aren't you going to hear my opinion?{#ch13_s_010}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：サイト……。
    voice "ch13_l_018"
    l "Saito… You be quiet for now.{#ch13_l_018}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ふぁい。  [voice 12848]
    voice "ch13_s_011"
    s "Y-yes, ma'am.{#ch13_s_011}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # → next scene 553
    jump ch13_1_scene_553

label ch13_1_scene_551:

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：なるほど、確かにキュルケの作戦は
    voice "ch13_s_012"
    s "I see. Kirche's plan might actually be good.{#ch13_s_012}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay7     image=+968, level=160, dir=1B]
    # ハルナ：平賀くん……。
    voice "ch13_ha_001"
    ha "Hiraga-kun… Do you really think so?{#ch13_ha_001}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：いや、まぁ……。
    voice "ch13_s_013"
    s "Well, kind of… Ahahahaha!{#ch13_s_013}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # → next scene 553
    jump ch13_1_scene_553

label ch13_1_scene_552:

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ふん……。
    voice "ch13_s_014"
    s "Hmph… Even as a familiar, nobody cares about me…{#ch13_s_014}"

    # サイト：（いじいじいじいじ）
    s "(Sulk, sulk…){#ch13_s_015}"

    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：（なでなで）  [voice 15774]
    voice "ch13_t_002"
    t "(Pat, pat.){#ch13_t_002}"

    # サイト：（じーん）
    s "(Touched…){#ch13_s_016}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # → next scene 553
    jump ch13_1_scene_553

label ch13_1_scene_553:

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # ルイズ：行くわよ、みんな！  [voice 6985]
    voice "ch13_l_019"
    l "Let's go, everyone!{#ch13_l_019}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay7     image=+962, level=160, dir=1B]
    # ハルナ：ルイズさん、ど、どこにですか？  [voice 2447]
    voice "ch13_ha_002"
    ha "Louise-san, w-where are we going?{#ch13_ha_002}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：知らないわよ、そんなの！
    voice "ch13_l_020"
    l "How should I know! Hurry up!{#ch13_l_020}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # ギーシュ：おいおい、ルイズ。
    voice "ch13_g_001"
    g "Hey, Louise. Don't drag us into this.{#ch13_g_001}"

    # ルイズ：つべこべ言わずについてきなさい。
    voice "ch13_l_021"
    l "No complaining. All we have to do is win. Win!{#ch13_l_021}"

    # [SPRITE   lay4     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch13_t_003}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：ほら、タバサも来る！  [voice 6988]
    voice "ch13_l_022"
    l "Come on, Tabitha too!{#ch13_l_022}"

    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # タバサ：さよなら。  [voice 15775]
    voice "ch13_t_004"
    t "Goodbye.{#ch13_t_004}"

    # [SE       se0      play=+57]
    # [SPRITE   lay1     hide]
    # [LAYER    lay0     hide]
    # [SE       se0      play=+56]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：……。  [voice 12852]
    voice "ch13_s_017"
    s "…{#ch13_s_017}"

    # サイト：はぁ。
    voice "ch13_s_018"
    s "Sigh. Say, Kirche.{#ch13_s_018}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なんで俺と一緒に行動するんだ？  [voice 12854]
    voice "ch13_s_019"
    s "Why are you teaming up with me?{#ch13_s_019}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：まぁ、ケンカをするのも飽きたし、
    voice "ch13_k_017"
    k "Well, I got tired of arguing, and figured it's time to get serious. That's all.{#ch13_k_017}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：本当かよ……。  [voice 12855]
    voice "ch13_s_020"
    s "Really…?{#ch13_s_020}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 554
    jump ch13_1_scene_554

label ch13_1_scene_554:

    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（部屋は俺とキュルケだけになってしまった）
    s "(Just Kirche and me in the room now.){#ch13_s_021}"

    # サイト：（キュルケは本を読んでるし……。
    s "(Kirche is reading a book… At this rate we'll lose, won't we?){#ch13_s_022}"

    menu:
        "Let's go out right away!{#ch13_1_c_554_1}":
            jump ch13_1_scene_555
        "Rest like this?{#ch13_1_c_554_2}":
            jump ch13_1_scene_556
        "Hold a strategy meeting!{#ch13_1_c_554_3}":
            jump ch13_1_scene_557

label ch13_1_scene_555:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：キュルケ！
    voice "ch13_s_023"
    s "Kirche! Let's get going too!{#ch13_s_023}"

    # [SPRITE   lay5     hide]
    # [EVENT_CG event    image=+249, level=80]
    $ dissolve_fx("id(249)")
    # [TRANS trans("crossfade", 1000)]
    # キュルケ：ふぁ……。
    voice "ch13_k_018"
    k "Haa… I'm tired…{#ch13_k_018}"

    # サイト：え？  [voice 12857]
    voice "ch13_s_024"
    s "Eh?{#ch13_s_024}"

    # キュルケ：あたしは少し昼寝をするけど、
    voice "ch13_k_019"
    k "I'm going to take a nap. What about you, darling?{#ch13_k_019}"

    # サイト：ちょっとまて！
    voice "ch13_s_025"
    s "Wait! What about the contest!?{#ch13_s_025}"

    # → next scene 558
    jump ch13_1_scene_558

label ch13_1_scene_556:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：あせっても仕方がないし、
    voice "ch13_s_026"
    s "Panicking won't help. Let's rest like this.{#ch13_s_026}"

    # [SPRITE   lay5     hide]
    # [EVENT_CG event    image=+249, level=80]
    $ dissolve_fx("id(249)")
    # [TRANS trans("crossfade", 1000)]
    # キュルケ：あら、考えが一致したわね、ダーリン。  [voice 3634]
    voice "ch13_k_020"
    k "My, we think alike, darling.{#ch13_k_020}"

    # キュルケ：あたしは少し昼寝をするけど……、  [voice 3635]
    voice "ch13_k_021"
    k "I'll take a little nap…{#ch13_k_021}"

    # サイト：おいおい。
    voice "ch13_s_027"
    s "Hey… I didn't mean to relax that much…{#ch13_s_027}"

    # → next scene 558
    jump ch13_1_scene_558

label ch13_1_scene_557:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：作戦会議でもしようぜ。
    voice "ch13_s_028"
    s "Let's hold a strategy meeting. Wandering around blindly is inefficient.{#ch13_s_028}"

    # [SPRITE   lay5     hide]
    # [EVENT_CG event    image=+249, level=80]
    $ dissolve_fx("id(249)")
    # [TRANS trans("crossfade", 1000)]
    # キュルケ：あら、ダーリン。
    voice "ch13_k_022"
    k "My, darling. I do have a plan.{#ch13_k_022}"

    # サイト：え？
    voice "ch13_s_029"
    s "Eh? Really?{#ch13_s_029}"

    # キュルケ：まあ、詳しくはあとで説明するわ。
    voice "ch13_k_023"
    k "Well, I'll explain later. For now, I'm taking a little nap.{#ch13_k_023}"

    # サイト：お、おい。
    voice "ch13_s_030"
    s "H-Hey! What do you mean, nap!?{#ch13_s_030}"

    # → next scene 558
    jump ch13_1_scene_558

label ch13_1_scene_558:

    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [EVENT_CG event    image=+249, level=80]
    $ dissolve_fx("id(249)")
    # キュルケ：大丈夫、ダーリン。
    voice "ch13_k_024"
    k "It's fine, darling. I have a proper plan. Right?{#ch13_k_024}"

    # サイト：か、考えって？  [voice 12864]
    voice "ch13_s_031"
    s "W-What plan?{#ch13_s_031}"

    # キュルケ：ないしょ。  [voice 3639]
    voice "ch13_k_025"
    k "Secret.{#ch13_k_025}"

    # サイト：そりゃないだろ？
    voice "ch13_s_032"
    s "You can't do that! If we lose, it's handstands for both of us!{#ch13_s_032}"

    # キュルケ：もう、あせらないの。
    voice "ch13_k_026"
    k "Goodness, don't panic. I've heard the bomb-thrower often appears at night.{#ch13_k_026}"

    # サイト：でも、俺達が会ったのは昼間だけだぜ。  [voice 12866]
    voice "ch13_s_033"
    s "But the ones we saw were in broad daylight.{#ch13_s_033}"

    # [SPRITE   lay6     hide]
    # キュルケ：まぁ、そこが疑問といえば、疑問なんだけど、
    voice "ch13_k_027"
    k "Well, that's the puzzling part, but all the sightings in town were at night.{#ch13_k_027}"

    # キュルケ：だったら、同じ歩き回るにしても、
    voice "ch13_k_028"
    k "So even if we're walking around, wouldn't narrowing the search to night increase our chances?{#ch13_k_028}"

    # サイト：なるほど。
    voice "ch13_s_034"
    s "I see. Now that you mention it…{#ch13_s_034}"

    # キュルケ：作戦、分かってくれた？  [voice 3643]
    voice "ch13_k_029"
    k "You got the plan?{#ch13_k_029}"

    # サイト：分かったよ。
    voice "ch13_s_035"
    s "Got it. I'll nap too, to prepare for the night.{#ch13_s_035}"

    # キュルケ：と・こ・ろで？
    voice "ch13_k_030"
    k "By the way? Darling, why don't we sleep together?{#ch13_k_030}"

    # サイト：え、遠慮しておきます。  [voice 12869]
    voice "ch13_s_036"
    s "Eh, I'll pass.{#ch13_s_036}"

    # キュルケ：あら、残念。  [voice 3645]
    voice "ch13_k_031"
    k "Oh, what a pity.{#ch13_k_031}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # → next scene 559
    jump ch13_1_scene_559

label ch13_1_scene_559:

    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # ルイズ：……ト！
    voice "ch13_l_023"
    l "…Si! …Saito!{#ch13_l_023}"

    # サイト：……ん？  [voice 12870]
    voice "ch13_s_037"
    s "…Hmm?{#ch13_s_037}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：サイト！
    voice "ch13_l_024"
    l "Saito! Why are you sleeping!?{#ch13_l_024}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ね、寝てた？  [voice 12871]
    voice "ch13_s_038"
    s "Was I asleep?{#ch13_s_038}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：寝てたわよ。
    voice "ch13_l_025"
    l "You were. Fast asleep.{#ch13_l_025}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：い、いけね。  [voice 12872]
    voice "ch13_s_039"
    s "Oops.{#ch13_s_039}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：（外はずいぶん暗いな。
    s "(It's pretty dark outside. I must have slept quite a while…){#ch13_s_040}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：ただいま。  [voice 15776]
    voice "ch13_t_005"
    t "I'm back.{#ch13_t_005}"

    # [LAYER    lay0     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：おかえり、タバサ。
    voice "ch13_k_032"
    k "Welcome back, Tabitha. How did it go?{#ch13_k_032}"

    # タバサ：時間の無駄。  [voice 15777]
    voice "ch13_t_006"
    t "Waste of time.{#ch13_t_006}"

    # サイト：（そっかー。
    s "(I see. Louise and the others didn't find anything today either…){#ch13_s_041}"

    menu:
        "Comfort everyone.{#ch13_1_c_559_1}":
            jump ch13_1_scene_560
        "Encourage everyone.{#ch13_1_c_559_2}":
            jump ch13_1_scene_561
        "Scold everyone.{#ch13_1_c_559_3}":
            jump ch13_1_scene_562

label ch13_1_scene_560:

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：お、おつかれさま……。
    voice "ch13_s_042"
    s "Y-You've all worked hard…{#ch13_s_042}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ありがと。
    voice "ch13_l_026"
    l "Thanks. But…{#ch13_l_026}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：とことんまで寝てたサイトに
    voice "ch13_l_027"
    l "I don't want to hear that from someone who slept the whole time.{#ch13_l_027}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：とほほ……。  [voice 12874]
    voice "ch13_s_043"
    s "Woe is me…{#ch13_s_043}"

    # → next scene 563
    jump ch13_1_scene_563

label ch13_1_scene_561:

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：き、気を落とさずに……。
    voice "ch13_s_044"
    s "D-Don't lose heart… There's still time!{#ch13_s_044}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：なによ、サイト。
    voice "ch13_l_028"
    l "What, Saito. Don't act superior.{#ch13_l_028}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：見てなさい。
    voice "ch13_l_029"
    l "Just watch. I'll win this contest and make you stand on your head for a day!{#ch13_l_029}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：な、なんですと！  [voice 12876]
    voice "ch13_s_045"
    s "W-What!?{#ch13_s_045}"

    # → next scene 563
    jump ch13_1_scene_563

label ch13_1_scene_562:

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：昼からずっと出かけて収穫なしなんて、
    voice "ch13_s_046"
    s "Out all day with nothing to show for it—that's no good!{#ch13_s_046}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：なによ！
    voice "ch13_l_030"
    l "What! You slept the whole time, Saito! Do you even intend to compete!?{#ch13_l_030}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：あ、あるよ……。
    voice "ch13_s_047"
    s "I-I do… Kirche is…{#ch13_s_047}"

    # → next scene 563
    jump ch13_1_scene_563

label ch13_1_scene_563:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ほーら、騒がないの。
    voice "ch13_k_033"
    k "Now, now, no shouting. Darling, it's about time we went out.{#ch13_k_033}"

    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：こ、こんな時間から、
    voice "ch13_l_031"
    l "G-Going out at this hour, where could you possibly go!?{#ch13_l_031}"

    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：この美しい星空の下で、男と女が出かける。
    voice "ch13_k_034"
    k "Under this beautiful starry sky, a man and a woman go out. Doesn't that pretty much tell you what they'll do?{#ch13_k_034}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：ふ、不潔！  [voice 6998]
    voice "ch13_l_032"
    l "H-How shameless!{#ch13_l_032}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ま、まてっ、ルイズ！
    voice "ch13_s_048"
    s "W-Wait, Louise! Don't worry—what you're imagining will never happen!{#ch13_s_048}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：信用できないわ！  [voice 6999]
    voice "ch13_l_033"
    l "I don't believe you!{#ch13_l_033}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：もう、馬鹿ね。
    voice "ch13_k_035"
    k "Goodness, you're such a fool. It's an investigation, an investigation!{#ch13_k_035}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：あたし達は夜の捜査に絞ってみたの。
    voice "ch13_k_036"
    k "We're focusing on the night patrol. They say the bomb-thrower appears more often at night, right?{#ch13_k_036}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ふ、ふん。
    voice "ch13_l_034"
    l "Hmf. I don't believe it.{#ch13_l_034}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：まぁ、いいわ。
    voice "ch13_k_037"
    k "Well, fine. The rest of you rest up and get ready for tomorrow.{#ch13_k_037}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：分かった。  [voice 15778]
    voice "ch13_t_007"
    t "Understood.{#ch13_t_007}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ちょ、ちょっと！
    voice "ch13_l_035"
    l "W-Wait! I'm coming too!{#ch13_l_035}"

    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：ダメよ。
    voice "ch13_k_038"
    k "No. Louise, you're overdoing it.{#ch13_k_038}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：そんなんじゃ、いざってときに使い物に
    voice "ch13_k_039"
    k "At this rate you'll be useless when it matters. Good children go to bed on time.{#ch13_k_039}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：う～。
    voice "ch13_l_036"
    l "Ugh. Fine.{#ch13_l_036}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：さーて、大人の時間はこれから。
    voice "ch13_k_040"
    k "Well then, the adult hour begins. Hee, let's go, darling.{#ch13_k_040}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：は、はい～。  [voice 12880]
    voice "ch13_s_049"
    s "Y-Yes, ma'am.{#ch13_s_049}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：サイトの馬鹿っ！
    voice "ch13_l_037"
    l "Saito, you idiot! Dog! I won't forgive you!{#ch13_l_037}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（……き、聞こえない。
    s "(I… can't hear her. Can't hear her…){#ch13_s_050}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：さあ、ダーリン。
    voice "ch13_k_041"
    k "Now, darling. Where shall we go?{#ch13_k_041}"

    # 【移動】城前/街道/裏通り/表通り → 1469/1470/1475/1480 (extra-сцены не портированы)
    menu:
        "In front of the castle{#ch13_1_c_563_1}":
            jump ch13_2_scene_1469
        "The street{#ch13_1_c_563_2}":
            jump ch13_2_scene_1470
        "The back alley{#ch13_1_c_563_3}":
            jump ch13_2_scene_1475
        "The main street{#ch13_1_c_563_4}":
            jump ch13_2_scene_1480

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch13_2
    return

