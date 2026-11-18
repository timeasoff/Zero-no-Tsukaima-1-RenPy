# Глава 26, часть 2 (сцены 944–954): аудиенция, пустой театр.
# Источник: ps2_source/chapters/chapter_27_タバサの秘密.txt (SCENE 944-954).

label ch26_2:
    $ tndl(None)
    $ show_sprites()

label ch26_2_scene_944:

    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+303, level=135, dir=1A]
    # ルイズ：わたしはラ・ヴァリエール公爵家の三女、
    voice "ch26_l_028"
    l "I am Louise Francoise, third daughter of the Duke of La Valliere.{#ch26_l_028}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # [SPRITE   lay1     level=151]
    # 味方Ａ：な、公爵家？  [voice 4253]
    voice "ch26_soldier_008"
    soldier "A-A Duke's family!?{#ch26_soldier_008}"

    # ルイズ：姫さま……。
    voice "ch26_l_029"
    l "I wish an audience with the princess—no, with Her Majesty the Queen. Please announce me.{#ch26_l_029}"

    # 味方Ａ：女王陛下に……？
    voice "ch26_soldier_009"
    soldier "To Her Majesty!? U-Understood. I'll check at once—please wait here.{#ch26_soldier_009}"

    # ルイズ：ありがとうございます。  [voice 6852]
    voice "ch26_l_030"
    l "Thank you.{#ch26_l_030}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay5     image=+434, level=156, dir=2B]
    # サイト：はー、公爵家ってすごいんだな。
    voice "ch26_s_059"
    s "Wow—being a duke's family is amazing. That soldier who was so strict folded in no time.{#ch26_s_059}"

    # ルイズ：今頃分かったの？
    voice "ch26_l_031"
    l "You only realized that now? From now on, act with a little more awareness of your position.{#ch26_l_031}"

    # サイト：へーい。  [voice 12572]
    voice "ch26_s_060"
    s "Yeess.{#ch26_s_060}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 945
    jump ch26_2_scene_945

label ch26_2_scene_945:

    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay15    image=+1114, level=159, dir=1A]
    # [SPRITE   lay1     level=154]
    # 味方Ａ：お待たせしました。
    voice "ch26_soldier_010"
    soldier "Sorry to keep you waiting. You're to be shown to a room at once.{#ch26_soldier_010}"

    # ルイズ：どうもありがとう。  [voice 6854]
    voice "ch26_l_032"
    l "Thank you very much.{#ch26_l_032}"

    # 味方Ａ：では、こちらに……。  [voice 4256]
    voice "ch26_soldier_011"
    soldier "Then, this way…{#ch26_soldier_011}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [TRANS trans("crossfade", 1000)]
    # null：………。
    th "… … …{#ch26_th_003}"

    # [BG       stage    hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=154, dir=1A]
    # ルイズ：失礼いたします……。  [voice 6855]
    voice "ch26_l_033"
    l "Excuse us…{#ch26_l_033}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay8     image=+766, level=153, dir=1A]
    # アンリエッタ：まあ、ルイズ・フランソワーズ！
    voice "ch26_h_001"
    h "My, Louise Francoise! You're safe!{#ch26_h_001}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     level=152]
    # [SPRITE   lay18    image=+1121, level=159, dir=1A]
    # 将校：陛下、その者達は？  [voice 4314]
    voice "ch26_commander_001"
    commander "Your Majesty, who are these people?{#ch26_commander_001}"

    # [SPRITE   lay8     image=+764, level=152, dir=1A]
    # アンリエッタ：わたくしの幼馴染と、そのよき友人達ですわ。  [voice 647]
    voice "ch26_h_002"
    h "My childhood friend and her good friends.{#ch26_h_002}"

    # 将校：……。  [voice 4315]
    voice "ch26_commander_002"
    commander "…{#ch26_commander_002}"

    # [SPRITE   lay18    hide]
    # [SPRITE   lay8     hide]
    # [SPRITE   lay1     image=+302, level=153, dir=1A]
    # [SPRITE   lay5     image=+396, level=154, dir=1A]
    # サイト：（分かってはいたけど、反応が微妙だな）
    s "(I knew it, but their reaction is lukewarm…){#ch26_s_061}"

    # ルイズ：（仕方ないわ。
    voice "ch26_l_034"
    l "(It can't be helped. Let's behave ourselves here.){#ch26_l_034}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+135, level=80]
    $ dissolve_fx("id(135)")
    # [TRANS trans("crossfade", 1000)]
    # アンリエッタ：中座して失礼しました。
    voice "ch26_h_003"
    h "Sorry to interrupt. Please continue the report.{#ch26_h_003}"

    # 将校：はっ！  [voice 4316]
    voice "ch26_commander_003"
    commander "Yes!{#ch26_commander_003}"

    # 将校：それでは、現在まで集まっている状況について、
    voice "ch26_commander_004"
    commander "Then, I'll report on the situation gathered so far.{#ch26_commander_004}"

    # 将校：本日起きた爆破事件及び、
    voice "ch26_commander_005"
    commander "Today's explosions and the fighting in various places…{#ch26_commander_005}"

    # 将校：例の爆弾使いとその仲間が引き起こしたものと
    voice "ch26_commander_006"
    commander "…are believed to be the work of the bomber and his accomplices.{#ch26_commander_006}"

    # 将校：ここに至って気づくのも遅いのですが、
    voice "ch26_commander_007"
    commander "It's late to notice this now, but the bomber doesn't seem to have been detonating bombs indiscriminately.{#ch26_commander_007}"

    # アンリエッタ：と、言いますと？  [voice 649]
    voice "ch26_h_004"
    h "Meaning what?{#ch26_h_004}"

    # 将校：捕らえた敵兵の証言によりますと、
    voice "ch26_commander_008"
    commander "According to a captured soldier's testimony, craftsmen were invited from various countries to repair the sites of previous bombings—{#ch26_commander_008}"

    # 将校：どうやら、工作兵を職人に混ぜて送り込んでいた
    voice "ch26_commander_009"
    commander "Apparently, saboteurs were sent in among those craftsmen and secretly installed gun emplacements at the repair sites.{#ch26_commander_009}"

    # 将校：今、城の周囲は敵の砲台によって囲まれた、
    voice "ch26_commander_010"
    commander "We can say the castle is now in a critical situation, surrounded by enemy batteries.{#ch26_commander_010}"

    # アンリエッタ：どうやら爆弾使いの背後には巨大な組織が
    voice "ch26_h_005"
    h "It seems a huge organization lurks behind the bomber, doesn't it?{#ch26_h_005}"

    # アンリエッタ：捕まえた兵はどこに所属しているのか、
    voice "ch26_h_006"
    h "Did you learn which unit the captured soldier belonged to?{#ch26_h_006}"

    # 将校：いえ、まだそこまで証言を引き出しては
    voice "ch26_commander_011"
    commander "No. We haven't extracted that much testimony yet.{#ch26_commander_011}"

    # アンリエッタ：そうですか……。  [voice 652]
    voice "ch26_h_007"
    h "I see…{#ch26_h_007}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay8     hide]
    # [SPRITE   lay18    hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # → next scene 946
    jump ch26_2_scene_946

label ch26_2_scene_946:

    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # サイト：（それからしばらくして、
    s "(A while later, the princess looked quite tired after ending the meeting.){#ch26_s_062}"

    # [SPRITE   lay8     image=+766, level=160, dir=1A]
    # アンリエッタ：お待たせしてごめんなさいね。  [voice 653]
    voice "ch26_h_008"
    h "Sorry to keep you waiting.{#ch26_h_008}"

    # [SPRITE   lay8     x=224, y=0]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：こちらこそ、このような急ぎの時に押しかけ、
    voice "ch26_l_035"
    l "No, the fault is ours—to barge in at such a busy time.{#ch26_l_035}"

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：いいのです、ルイズ。  [voice 654]
    voice "ch26_h_009"
    h "It's fine, Louise.{#ch26_h_009}"

    # アンリエッタ：それで、どうしたの？
    voice "ch26_h_010"
    h "So—what is it? Is it related to the bomber?{#ch26_h_010}"

    # ルイズ：それが、その……。  [voice 6858]
    voice "ch26_l_036"
    l "Well, that is…{#ch26_l_036}"

    # [SPRITE   lay8     image=+766, level=160, dir=1A]
    # アンリエッタ：あら、どうしたの？
    voice "ch26_h_011"
    h "Oh, what's wrong? It's us, isn't it? Don't hold back—tell me.{#ch26_h_011}"

    # ルイズ：ですが、姫さま……。  [voice 6859]
    voice "ch26_l_037"
    l "But, Princess…{#ch26_l_037}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：それでは、この俺がお姫さまに単刀直入に……。  [voice 12573]
    voice "ch26_s_063"
    s "Then I'll be blunt with the princess myself…{#ch26_s_063}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：こっ、こらサイトっ！
    voice "ch26_l_038"
    l "H-Hey, Saito! You be quiet!!{#ch26_l_038}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：だって、あんまりまどろっこしい
    voice "ch26_s_064"
    s "Well, the exchange was so roundabout, I just…{#ch26_s_064}"

    # ルイズ：あんたのつい、ってやつで姫さまに無礼を
    voice "ch26_l_039"
    l "If your 'tsui' offends the princess, we're the ones in trouble!{#ch26_l_039}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     image=+766, level=160, dir=1A]
    # アンリエッタ：フフフッ……。
    voice "ch26_h_012"
    h "Heh heh heh… You're still an entertaining familiar, aren't you?{#ch26_h_012}"

    # [SPRITE   lay8     x=224, y=0]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：もっ、申し訳ございません姫さまっ！
    voice "ch26_l_040"
    l "I'm terribly sorry, Princess! It's only because my training of him was lacking…{#ch26_l_040}"

    # ルイズ：率直に申し上げます。
    voice "ch26_l_041"
    l "To be frank—we'd like to be informed of the capital's current situation. That's why…{#ch26_l_041}"

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：分かりました。
    voice "ch26_h_013"
    h "I understand. Then, let me explain the state of the capital.{#ch26_h_013}"

    # アンリエッタ：現在、都の数箇所で潜入していた敵兵と
    voice "ch26_h_014"
    h "At present, we're fighting enemy soldiers who've infiltrated several parts of the capital.{#ch26_h_014}"

    # アンリエッタ：先ほどの報告どおり、これまで起こっていた
    voice "ch26_h_015"
    h "As the report said, the whole series of incidents caused by the bomber seems to have been planned.{#ch26_h_015}"

    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # アンリエッタ：わたくし達が、それにもう少し早く
    voice "ch26_h_016"
    h "I can't help regretting that we didn't notice it a little earlier…{#ch26_h_016}"

    # ルイズ：姫さま……。  [voice 6864]
    voice "ch26_l_042"
    l "Princess…{#ch26_l_042}"

    # サイト：……。  [voice 12575]
    voice "ch26_s_065"
    s "…{#ch26_s_065}"

    menu:
        "Cheer up{#ch26_2_c_946_1}":
            jump ch26_2_scene_947
        "What's done is done{#ch26_2_c_946_2}":
            jump ch26_2_scene_948
        "What happens next?{#ch26_2_c_946_3}":
            jump ch26_2_scene_949

label ch26_2_scene_947:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：元気出してくださいよ、お姫さま。  [voice 12576]
    voice "ch26_s_066"
    s "Cheer up, Princess.{#ch26_s_066}"

    # サイト：お姫さまが沈んでいたら、
    voice "ch26_s_067"
    s "If you're down, everyone around you gets gloomy, too.{#ch26_s_067}"

    # [SPRITE   lay8     image=+766, level=160, dir=1A]
    # アンリエッタ：フフッ、そうですね。
    voice "ch26_h_017"
    h "Heh, that's true. Thank you, familiar.{#ch26_h_017}"

    # → next scene 950
    jump ch26_2_scene_950

label ch26_2_scene_948:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：なってしまったものはしょうがないですよ。
    voice "ch26_s_068"
    s "What's done is done. We should think about how to win the fighting happening now.{#ch26_s_068}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：サイト！
    voice "ch26_l_043"
    l "Saito! What are you doing, giving the Princess your opinion so boldly!?{#ch26_l_043}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なんで怒るんだよ！
    voice "ch26_s_069"
    s "Why are you angry? I'm just speaking sense…{#ch26_s_069}"

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：ありがとう、使い魔さん。
    voice "ch26_h_018"
    h "Thank you, familiar. Indeed, you're right. I nearly lost sight of what matters again.{#ch26_h_018}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：ひ、姫さまがそれで良いというなら
    voice "ch26_l_044"
    l "W-Well, if the Princess says it's fine, then it's fine…{#ch26_l_044}"

    # [SPRITE   lay1     hide]
    # → next scene 950
    jump ch26_2_scene_950

label ch26_2_scene_949:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：お姫さまは、これからどうなるのか
    voice "ch26_s_070"
    s "Do you know what will happen next, Princess?{#ch26_s_070}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：姫さまに向かって、
    voice "ch26_l_045"
    l "How dare you take that tone with the Princess! Of course she can't know!{#ch26_l_045}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # アンリエッタ：分かるはずがない……。
    voice "ch26_h_019"
    h "She can't know… You're right.{#ch26_h_019}"

    # アンリエッタ：確かに、まだ相手の目的も把握できて
    voice "ch26_h_020"
    h "Indeed, we still don't grasp their objective, do we?{#ch26_h_020}"

    # アンリエッタ：今起こるよりも、次に目を向ける。
    voice "ch26_h_021"
    h "Look to what comes next rather than what's happening now. That's quite right.{#ch26_h_021}"

    # アンリエッタ：ありがとう、使い魔さん。
    voice "ch26_h_022"
    h "Thank you, familiar. I nearly repeated my mistake.{#ch26_h_022}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：ひ、姫さまがそれで良いというなら
    voice "ch26_l_046"
    l "W-Well, if the Princess says it's fine, then it's fine…{#ch26_l_046}"

    # [SPRITE   lay1     hide]
    # → next scene 950
    jump ch26_2_scene_950

label ch26_2_scene_950:

    # [SPRITE   lay8     image=+766, level=160, dir=1A]
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay1     x=144, y=416]
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ルイズ……。
    voice "ch26_s_071"
    s "Louise… In this situation, it'll be hard to ask about Haruna, too.{#ch26_s_071}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ば、ばか。
    voice "ch26_l_047"
    l "Y-You fool. Saying unnecessary things…{#ch26_l_047}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：ハルナ……。
    voice "ch26_h_023"
    h "Haruna… The girl you acted with in the play, was it? What happened to her?{#ch26_h_023}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：は、はい、姫さま。
    voice "ch26_l_048"
    l "Y-Yes, Princess. Actually, Haruna went missing around the time the fighting began…{#ch26_l_048}"

    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # アンリエッタ：まぁ、行方不明ですか……。
    voice "ch26_h_024"
    h "My, missing? That's serious.{#ch26_h_024}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：ええ、探そうとしていたのですが……。
    voice "ch26_l_049"
    l "Yes, we tried searching, but… we couldn't find her. We thought if you had any information…{#ch26_l_049}"

    # アンリエッタ：そうでしたか……。  [voice 670]
    voice "ch26_h_025"
    h "I see…{#ch26_h_025}"

    # アンリエッタ：こちらのほうは、見てのとおり戦闘が
    voice "ch26_h_026"
    h "As you can see, information-gathering isn't functioning well now that fighting has broken out.{#ch26_h_026}"

    # アンリエッタ：分かり次第、ルイズにお知らせしますね。  [voice 672]
    voice "ch26_h_027"
    h "The moment I learn anything, I'll inform Louise.{#ch26_h_027}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ご配慮、ありがとうございます。  [voice 6872]
    voice "ch26_l_050"
    l "Thank you for your consideration.{#ch26_l_050}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：春奈……。
    voice "ch26_s_072"
    s "Haruna… Where did you go…{#ch26_s_072}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch26_t_019}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # → next scene 951
    jump ch26_2_scene_951

label ch26_2_scene_951:

    # [BG       stage    image=+42, level=200]
    $ fade_fx("id(42)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # ルイズ：都の状況は分かったものの、
    voice "ch26_l_051"
    l "We learned the capital's situation, but not even Haruna's, it seems.{#ch26_l_051}"

    # サイト：仮に春奈の情報があったとしても、
    voice "ch26_s_073"
    s "Even if we had info on Haruna, it wouldn't reach the princess's ears anyway.{#ch26_s_073}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：うん。  [voice 15692]
    voice "ch26_t_020"
    t "Mm.{#ch26_t_020}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：それより、キュルケのほうは
    voice "ch26_s_074"
    s "More importantly, I wonder how Kirche is doing…{#ch26_s_074}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：特に連絡がないところを見ると、
    voice "ch26_l_052"
    l "Judging by the lack of news, I'm afraid there's no good news, either.{#ch26_l_052}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：……。  [voice 12585]
    voice "ch26_s_075"
    s "…{#ch26_s_075}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+500, level=160, dir=1B]
    # シエスタ：サイトさん、大丈夫ですよ。
    voice "ch26_si_015"
    si "Saito-san, it's all right. I'm sure Haruna-san is safe.{#ch26_si_015}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：うん……。  [voice 12586]
    voice "ch26_s_076"
    s "Mm…{#ch26_s_076}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+119, level=80]
    $ dissolve_fx("id(119)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [LAYER    lay0     hide, reset]
    # キュルケ：ダーリーンッ！  [voice 3507]
    voice "ch26_k_011"
    k "Darring!!{#ch26_k_011}"

    # サイト：キュルケ！  [voice 12587]
    voice "ch26_s_077"
    s "Kirche!{#ch26_s_077}"

    # キュルケ：会いたかったわ、ダーリン。
    voice "ch26_k_012"
    k "I missed you, darling. Being apart from you, this body of mine was burning with longing!{#ch26_k_012}"

    # ルイズ：そういいながら、サイトに抱きつくのは
    voice "ch26_l_053"
    l "You can say that, but stop hugging Saito!{#ch26_l_053}"

    # キュルケ：あーら、いいじゃないの。
    voice "ch26_k_013"
    k "Oh, come on. It's not like he'll shrink from it.{#ch26_k_013}"

    # ルイズ：うー。  [voice 6876]
    voice "ch26_l_054"
    l "Ugh.{#ch26_l_054}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+42, level=200]
    $ fade_fx("id(42)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ま、まあまあ。
    voice "ch26_s_078"
    s "W-Well, fine. More importantly—did you find Haruna?{#ch26_s_078}"

    # キュルケ：全然駄目。
    voice "ch26_k_014"
    k "Not at all. Nobody's seen her.{#ch26_k_014}"

    # サイト：そうか……。  [voice 12589]
    voice "ch26_s_079"
    s "I see…{#ch26_s_079}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：元気出して、ダーリン。
    voice "ch26_k_015"
    k "Cheer up, darling. I can think of one place she might be.{#ch26_k_015}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ど、どこよ？  [voice 6877]
    voice "ch26_l_055"
    l "W-Where?{#ch26_l_055}"

    # キュルケ：劇場よ。
    voice "ch26_k_016"
    k "The theater. There must be some clue there.{#ch26_k_016}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：劇場？
    voice "ch26_l_056"
    l "The theater? Why there?{#ch26_l_056}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：劇場……。  [voice 15693]
    voice "ch26_t_021"
    t "The theater…{#ch26_t_021}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：まぁ、いいから。
    voice "ch26_k_017"
    k "Well, just come with me.{#ch26_k_017}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：あ、お、おーい。  [voice 12590]
    voice "ch26_s_080"
    s "A-Oh, wait!{#ch26_s_080}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+51, level=200]
    $ fade_fx("id(51)")
    # [TRANS trans("crossfade", 1000)]
    # null：………。
    th "… … …{#ch26_th_004}"

    # [BG       stage    hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+54, level=200]
    $ fade_fx("id(54)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay6     image=+713, level=160, dir=2A]
    # キュルケ：誰もいないし、何もないっ！
    voice "ch26_k_018"
    k "Nobody's here and there's nothing here! It's completely empty. We've been played…{#ch26_k_018}"

    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：何がやられたの？
    voice "ch26_l_057"
    l "Played how? I'd like a proper explanation!{#ch26_l_057}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：実はね、あたしとタバサで爆弾使い
    voice "ch26_k_019"
    k "The thing is, Tabitha and I were investigating the bomber, and we found out that a suspicious person was coming and going at the theater.{#ch26_k_019}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：ちょっと待ってよ。
    voice "ch26_l_058"
    l "Wait a moment. Why did you two keep such an important thing to yourselves until now?{#ch26_l_058}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：証拠がない。  [voice 15694]
    voice "ch26_t_022"
    t "No evidence.{#ch26_t_022}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：いくら証拠がないからって……。
    voice "ch26_l_059"
    l "Even without evidence… If you'd told us…{#ch26_l_059}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：話してくれれば、ウェザリーを問い詰めたのに
    voice "ch26_k_020"
    k "You'd have confronted Weatherly, wouldn't you?{#ch26_k_020}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……。  [voice 6882]
    voice "ch26_l_060"
    l "…{#ch26_l_060}"

    # キュルケ：いくらなんでも大した確証もないのに、
    voice "ch26_k_021"
    k "Surely you can't suspect someone without real proof, can you?{#ch26_k_021}"

    # キュルケ：もちろん、ここまで大胆な話だったら、
    voice "ch26_k_022"
    k "Of course, if it were this bold, we wouldn't have left it alone, either…{#ch26_k_022}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：うーん……。  [voice 12591]
    voice "ch26_s_081"
    s "Hmm…{#ch26_s_081}"

    menu:
        "Kirche is right{#ch26_2_c_951_1}":
            jump ch26_2_scene_952
        "You could have told us{#ch26_2_c_951_2}":
            jump ch26_2_scene_953
        "It's too late now{#ch26_2_c_951_3}":
            jump ch26_2_scene_954

label ch26_2_scene_952:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+54, level=200]
    $ fade_fx("id(54)")
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：そうだよな。
    voice "ch26_s_082"
    s "Right. Kirche is right.{#ch26_s_082}"

    # サイト：俺達が知らなかったからこそ、
    voice "ch26_s_083"
    s "It's precisely because we didn't know that there might be information to gain, isn't it? That's what Kirche decided, right?{#ch26_s_083}"

    # サイト：それに、もしウェザリーが関係していたと
    voice "ch26_s_084"
    s "And if Weatherly were involved, she wouldn't have let us—who knew—go so easily, either.{#ch26_s_084}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：でっしょー？
    voice "ch26_k_023"
    k "Right!? Darling understands perfectly!{#ch26_k_023}"

    # → next scene 955
    jump ch26_3

label ch26_2_scene_953:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+54, level=200]
    $ fade_fx("id(54)")
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：でも、話をしてくれるくらいは……。  [voice 12595]
    voice "ch26_s_085"
    s "But, you could have at least told us…{#ch26_s_085}"

    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：ダーリン。
    voice "ch26_k_024"
    k "Darling, I know what you'll say—but she's a professional actress. She'd notice immediately.{#ch26_k_024}"

    # キュルケ：そうなったら、調査がみんなパーに
    voice "ch26_k_025"
    k "Then the whole investigation would be ruined, wouldn't it?{#ch26_k_025}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：まぁ、そうは言っても。
    voice "ch26_k_026"
    k "Well, be that as it may—in the end, the other side was one step ahead, and it all fell apart.{#ch26_k_026}"

    # → next scene 955
    jump ch26_3

label ch26_2_scene_954:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+54, level=200]
    $ fade_fx("id(54)")
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：それを今言っても始まらないって。  [voice 12596]
    voice "ch26_s_086"
    s "Saying it now won't change anything.{#ch26_s_086}"

    # サイト：俺達なんて、その怪しい人物のことすら
    voice "ch26_s_087"
    s "We didn't even notice that suspicious person, did we?{#ch26_s_087}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そりゃまあそうなんだけどね……。  [voice 6883]
    voice "ch26_l_061"
    l "Well, yes, but…{#ch26_l_061}"

    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：そういう意味では、
    voice "ch26_k_027"
    k "In that sense, we're no different from you.{#ch26_k_027}"

    # キュルケ：結局、相手のほうが一歩上手で、
    voice "ch26_k_028"
    k "In the end, the other side was one step ahead and everything fell apart, too.{#ch26_k_028}"

    # [SPRITE   lay1     hide]
    # → next scene 955
    jump ch26_3

    # ==== КОНЕЦ ЧАСТИ 2 ====
    jump ch26_3
    return

