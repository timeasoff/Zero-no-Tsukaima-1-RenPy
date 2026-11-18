# Глава 19, часть 3 (сцены 764–768): прошлое Уэзерби, развязка, финал.
# Источник: ps2_source/chapters/chapter_20_小悪魔と春風の協奏曲.txt (SCENE 764-768).

label ch19_3:
    $ tndl(None)
    $ show_sprites()

label ch19_3_scene_764:

    # [SPRITE   lay5     image=+471, level=160, dir=3B]
    # [LAYER    lay0     image=+658, level=160, dir=3A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+29, level=200]
    $ fade_fx("id(29)")
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # ウェザリー：驚いたな。
    voice "ch19_w_005"
    w "I'm surprised. That you made it this far…{#ch19_w_005}"

    # [SPRITE   lay20    x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：驚いたってことなら、俺のほうが驚いたよ。
    voice "ch19_s_317"
    s "If you're surprised, I'm more surprised. That you were the enemy, Weatherly.{#ch19_s_317}"

    # ウェザリー：まぁ、ここまでは上手く行ってたんだけどね。
    voice "ch19_w_006"
    w "Well, things were going well up to here. Everything was going according to script…{#ch19_w_006}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch19_t_045}"

    # [SPRITE   lay20    image=+1067, level=160, dir=1A]
    # ウェザリー：タバサ……。
    voice "ch19_w_007"
    w "Tabitha… The spell seems to have worn off. Was it too shallow, I wonder?{#ch19_w_007}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ウェザリー、ここで投降してくれないか。
    voice "ch19_s_318"
    s "Weatherly, won't you surrender here? I don't want to hurt you—or Haruna.{#ch19_s_318}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：こいつ、ウェザリー様を愚弄するか！  [voice 95]
    voice "ch19_ak_005"
    ak "This one dares to mock Weatherly-sama!{#ch19_ak_005}"

    # [SPRITE   lay20    image=+1063, level=160, dir=1A]
    # ウェザリー：なるほどね。
    voice "ch19_w_008"
    w "I see. That fleet seems to be the work of Louise and Saito. We underestimated your strength.{#ch19_w_008}"

    # アキナ：ウェザリー様。
    voice "ch19_ak_006"
    ak "Weatherly-sama, we still have hostages and bombs. We could even detonate them…{#ch19_ak_006}"

    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：やめなさいアキナ、ここでは我々や友軍も
    voice "ch19_w_009"
    w "Stop it, Akina. We'd be caught in the explosion too, along with our allies.{#ch19_w_009}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：ウェザリー様……。  [voice 97]
    voice "ch19_ak_007"
    ak "Weatherly-sama…{#ch19_ak_007}"

    # ウェザリー：わたしが魔法を使えばいいだけの話よ。
    voice "ch19_w_010"
    w "I'll just use my magic. Take this!{#ch19_w_010}"

    # [SE       se0      play=+94]
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # ウェザリー：なっ！
    voice "ch19_w_011"
    w "What! Why isn't it working?{#ch19_w_011}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     image=+434, level=160, dir=2B]
    # サイト：その魔法はすでに対応ずみだよ。
    voice "ch19_s_319"
    s "We've already countered that magic. Look—these.{#ch19_s_319}"

    # ウェザリー：な、な、なっ……み、耳栓だとっ！？
    voice "ch19_w_012"
    w "W-What… Earplugs!? No, no way…!{#ch19_w_012}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：ウェザリー。
    voice "ch19_s_320"
    s "Weatherly. Your magic controls people through sound they can't hear, doesn't it?{#ch19_s_320}"

    # サイト：でも、この耳栓には魔法を打ち消す
    voice "ch19_s_321"
    s "But these earplugs have a wind spell that cancels it. In other words, we can resist it.{#ch19_s_321}"

    # ウェザリー：う、嘘だ……嘘だ！
    voice "ch19_w_013"
    w "Ugh, lies… Lies! This magic is special—only my family can use it.{#ch19_w_013}"

    # ウェザリー：仕組みなぞ、そうそう知られてるはずがない！！  [voice 16036]
    voice "ch19_w_014"
    w "There's no way its mechanism could be known so easily!!{#ch19_w_014}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：ああ、それを解読したのはわしじゃよ。  [voice 4458]
    voice "ch19_o_001"
    o "Ah, it was I who deciphered it.{#ch19_o_001}"

    # [SPRITE   lay20    image=+1067, level=160, dir=1A]
    # ウェザリー：い、いや……。
    voice "ch19_w_015"
    w "N-No… But you were confined in the headmaster's office the whole time…{#ch19_w_015}"

    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # オスマン：わしのモートソグニルを
    voice "ch19_o_002"
    o "You shouldn't underestimate my Mortosgnir.{#ch19_o_002}"

    # オスマン：こやつが本調子なら学院どころか、
    voice "ch19_o_003"
    o "At full strength, he could round-trip to the capital in a day—not just the academy.{#ch19_o_003}"

    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：ちょうどいいことに、
    voice "ch19_o_004"
    o "Conveniently, this academy has people studying all sorts of magic.{#ch19_o_004}"

    # オスマン：彼につなぎをつけたら、
    voice "ch19_o_005"
    o "I put him in touch with one, and he worked out a countermeasure in one go.{#ch19_o_005}"

    # オスマン：まぁ、おまえさんの失敗は、
    voice "ch19_o_006"
    o "Well, your mistake was letting me hear that incantation.{#ch19_o_006}"

    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # オスマン：いやいや、まだまだ若い、若いのぅ。
    voice "ch19_o_007"
    o "No, no, you're still young—still young. Ho ho ho ho.{#ch19_o_007}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay20    image=+1067, level=160, dir=1A]
    # ウェザリー：ここまでか、ここまでなのか？
    voice "ch19_w_016"
    w "Is this the end? Is this the end? No—I can't just slink away like this. My… my…{#ch19_w_016}"

    # [SPRITE   lay20    image=+1087, level=160, dir=2A]
    # ウェザリー：アキナ、わたしのそばから離れないで！
    voice "ch19_w_017"
    w "Akina, don't leave my side! If it comes to it, I'll take down Old Osmond and Gandalfr!{#ch19_w_017}"

    # ウェザリー：ゆくぞ、ガンダールヴ！
    voice "ch19_w_018"
    w "Here I come, Gandalfr! Receive the fangs and claws of my resentment and rage!{#ch19_w_018}"

    # [SPRITE   lay20    x=-160, y=0]
    # [SPRITE   lay21    image=+1043, level=160, dir=2A]
    # アキナ：どこまでもあなたにお供します、ウェザリー様！  [voice 98]
    voice "ch19_ak_008"
    ak "I'll follow you anywhere, Weatherly-sama!{#ch19_ak_008}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay21    hide]
    # [LAYER    lay0     image=+654, level=160, dir=3A]
    # [SPRITE   lay5     image=+471, level=160, dir=3B]
    # サイト：やっぱり戦うしかないのか。  [voice 11984]
    voice "ch19_s_322"
    s "So we have to fight after all, huh.{#ch19_s_322}"

    # タバサ：くる。  [voice 15621]
    voice "ch19_t_046"
    t "They're coming.{#ch19_t_046}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # → next scene 765
    jump ch19_3_scene_765

label ch19_3_scene_765:

    # [BG       stage    image=+29, level=200]
    $ fade_fx("id(29)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # ウェザリー：さあ……殺しなさい。
    voice "ch19_w_019"
    w "Come now, kill me. I'm a member of Reconquista now. I won't live in disgrace.{#ch19_w_019}"

    # アキナ：だめですウェザリー様！
    voice "ch19_ak_009"
    ak "No, Weatherly-sama! What about the village's restoration? Your honor?{#ch19_ak_009}"

    # [SPRITE   lay21    hide]
    # [LAYER    lay0     image=+627, level=160, dir=2A]
    # タバサ：故郷？
    voice "ch19_t_047"
    t "Homeland? Honor?{#ch19_t_047}"

    # ウェザリー：やめなさい、アキナ。  [voice 16042]
    voice "ch19_w_020"
    w "Stop it, Akina.{#ch19_w_020}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：いやだ！
    voice "ch19_ak_010"
    ak "No! I may be a fleeting life, but you created me, Weatherly-sama.{#ch19_ak_010}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：だからウェザリー様の命が助かるなら
    voice "ch19_ak_011"
    ak "So if it saves your life, I'd do anything…{#ch19_ak_011}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：事情がありそうじゃな。
    voice "ch19_o_008"
    o "There seems to be more to this. Well, won't you tell us? I won't do you any harm.{#ch19_o_008}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：ウェザリー様は、別にレコン・キスタの
    voice "ch19_ak_012"
    ak "Weatherly-sama never cared about Reconquista's ideals or reforming the world.{#ch19_ak_012}"

    # アキナ：ただ、故郷の村で、村の人達と静かに
    voice "ch19_ak_013"
    ak "She just wanted to live quietly in her home village with its people. That alone made her happy.{#ch19_ak_013}"

    # アキナ：それを……。  [voice 104]
    voice "ch19_ak_014"
    ak "And that…{#ch19_ak_014}"

    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：ある時、トリステインによって、
    voice "ch19_ak_015"
    ak "One day, Tristain stripped her of her noble status and took the village away.{#ch19_ak_015}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：落ち込んでいたウェザリー様に
    voice "ch19_ak_016"
    ak "Reconquista promised to restore her status and her village to the depressed Weatherly. So she had no choice but to…{#ch19_ak_016}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay20    image=+1067, level=160, dir=1A]
    # ウェザリー：……。  [voice 16043]
    voice "ch19_w_021"
    w "…{#ch19_w_021}"

    # オスマン：しかたなく、トリステインに復讐したと。
    voice "ch19_o_009"
    o "So you took revenge on Tristain because you had no choice, is that it?{#ch19_o_009}"

    # ウェザリー：わたしの父は貴族、母は獣人。
    voice "ch19_w_022"
    w "My father was a noble, my mother a beast-person. Father lost his noble status for marrying her, and we were driven from our manor and lands.{#ch19_w_022}"

    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # ウェザリー：トリステインのこの行為をわたしは、
    voice "ch19_w_023"
    w "I can never forget what Tristain did.{#ch19_w_023}"

    # [SPRITE   lay10    hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：本当に？  [voice 15623]
    voice "ch19_t_048"
    t "Really?{#ch19_t_048}"

    # ウェザリー：本当にとは何だ？  [voice 16046]
    voice "ch19_w_024"
    w "What do you mean, 'really'?{#ch19_w_024}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：おぬしの考え違いだろうと、言っているのじゃ。  [voice 4467]
    voice "ch19_o_010"
    o "I'm saying you're mistaken.{#ch19_o_010}"

    # [SPRITE   lay10    image=+924, level=160, dir=1A]
    # オスマン：確かに、獣人は忌むべきものとされており、
    voice "ch19_o_011"
    o "It's true that beast-people are reviled and suffer unjust discrimination. That much is fact.{#ch19_o_011}"

    # オスマン：しかしのう……。
    voice "ch19_o_012"
    o "But… the reason you lost your noble status was almost certainly your magic.{#ch19_o_012}"

    # [SPRITE   lay10    hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：禁忌。  [voice 15624]
    voice "ch19_t_049"
    t "Forbidden magic.{#ch19_t_049}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay10    image=+924, level=160, dir=1A]
    # オスマン：そう……。
    voice "ch19_o_013"
    o "Yes… Touching forbidden magic is a grave sin in itself.{#ch19_o_013}"

    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：たぶん、じゃが。
    voice "ch19_o_014"
    o "Probably, though. Your parents didn't tell you the truth because they wanted you to forget the forbidden magic.{#ch19_o_014}"

    # [SPRITE   lay20    image=+1067, level=160, dir=1A]
    # ウェザリー：なるほど、わたしが覚えたその魔法。
    voice "ch19_w_025"
    w "I see. The magic I learned—it is indeed forbidden magic that controls the heart.{#ch19_w_025}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：ウェザリー様……。  [voice 107]
    voice "ch19_ak_017"
    ak "Weatherly-sama…{#ch19_ak_017}"

    # ウェザリー：今更命乞いなどしようとは思わない。
    voice "ch19_w_026"
    w "I don't intend to beg for my life now. But, Saito, there are times when a person must fight for honor.{#ch19_w_026}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：俺はこの世界の人間じゃないから、
    voice "ch19_s_323"
    s "I'm not from this world, so I don't know about honor. I just protected everyone.{#ch19_s_323}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：……。
    ak "…{#ch19_ak_018}"

    # サイト：春奈を返してもらうぞ。  [voice 11986]
    voice "ch19_s_324"
    s "Give Haruna back.{#ch19_s_324}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：ああ、分かった。
    voice "ch19_w_027"
    w "Ah, I understand. I'll do what I can.{#ch19_w_027}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay20    hide]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：どうやら、兵隊も軍艦も引き上げたようじゃ。
    voice "ch19_o_015"
    o "Looks like the soldiers and ships have withdrawn. Well, the academy's crisis is over.{#ch19_o_015}"

    # [SPRITE   lay10    x=-96, y=0]
    # [SPRITE   lay19    image=+942, level=160, dir=1A]
    # デルフリンガー：いろいろあったが……これにて一件落着って
    voice "ch19_d_034"
    d "A lot happened, but that's the end of this affair, isn't it, partner?{#ch19_d_034}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [SPRITE   lay10    hide]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：サ、サイト……。  [voice 6527]
    voice "ch19_l_266"
    l "S-Saito…{#ch19_l_266}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+442, level=160, dir=2B]
    # サイト：よ、よぉ……、ルイズ。  [voice 11987]
    voice "ch19_s_325"
    s "Y-Yeah… Louise.{#ch19_s_325}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ダーリン、タバサ。
    voice "ch19_k_078"
    k "Darling, Tabitha, I'm glad you're unhurt. Well, I believed in you, though.{#ch19_k_078}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：みなさん、無事でしたか。
    voice "ch19_c_106"
    c "Everyone safe? Then everything worked out. Good.{#ch19_c_106}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：サイトさん！
    voice "ch19_si_001"
    si "Saito-san! You're safe! Thank goodness!{#ch19_si_001}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+403, level=160, dir=1B]
    # サイト：シ、シエスタ！
    voice "ch19_s_326"
    s "S-Siesta! I'm glad you're safe too.{#ch19_s_326}"

    # [SPRITE   lay2     image=+526, level=160, dir=2A]
    # シエスタ：聞いてくださいよ、サイトさん。
    voice "ch19_si_002"
    si "Listen, Saito-san. When I came to, I was tied up with rope inside Miss Valliere's chest of drawers.{#ch19_si_002}"

    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # シエスタ：わたし、怖くて、怖くて……。
    voice "ch19_si_003"
    si "I was so scared, so scared… But somehow the rope loosened, and I could run to you.{#ch19_si_003}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：もっと、ちゃんと縛っておけば
    voice "ch19_l_267"
    l "I should have tied you more securely…{#ch19_l_267}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：ル、ルイズ……。
    voice "ch19_s_327"
    s "L-Louise… By the way, what's happening in Tristania?{#ch19_s_327}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：それについては、さっき王都から知らせが
    voice "ch19_k_079"
    k "We just got word from the capital about that.{#ch19_k_079}"

    # キュルケ：トリスタニアに向かっていたレコン・キスタの
    voice "ch19_k_080"
    k "The Reconquista fleet heading for Tristania panicked at the sudden appearance of a mysterious huge fleet and withdrew.{#ch19_k_080}"

    # キュルケ：あと、市街戦の状況についても同じ。
    voice "ch19_k_081"
    k "Same for the street fighting. The sudden fleet threw the enemy units occupying the battery posts into disarray, and…{#ch19_k_081}"

    # キュルケ：多少の犠牲は出したけど、
    voice "ch19_k_082"
    k "…there were some casualties, but we retook most of the batteries.{#ch19_k_082}"

    # [SPRITE   lay5     image=+403, level=160, dir=1B]
    # サイト：なんとかなったんだな、ルイズ。  [voice 11990]
    voice "ch19_s_328"
    s "It worked out after all, Louise.{#ch19_s_328}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：うん……。  [voice 6529]
    voice "ch19_l_268"
    l "Mm…{#ch19_l_268}"

    # → next scene 766
    jump ch19_3_scene_766

    # → next scene 767
    jump ch19_3_scene_767

label ch19_3_scene_766:

    # [SPRITE   lay5     image=+403, level=160, dir=1B]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+29, level=200]
    $ fade_fx("id(29)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：なんか変ですね２人とも。
    voice "ch19_si_004"
    si "Something's odd about you two. I sense a strange atmosphere.{#ch19_si_004}"

    # [SPRITE   lay5     image=+436, level=160, dir=2B]
    # サイト：そ、そんなことはないって！
    voice "ch19_s_329"
    s "N-No, there's nothing! Right, everyone?{#ch19_s_329}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：さぁねぇ、どうかしら～。  [voice 3376]
    voice "ch19_k_083"
    k "Well now, who can say~.{#ch19_k_083}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # タバサ：……。
    t "…{#ch19_t_050}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：まさか、ミス・ヴァリエール……。
    voice "ch19_si_005"
    si "Don't tell me—Miss Valliere, you kissed Saito-san!?{#ch19_si_005}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：な、なに言ってるのよ？
    voice "ch19_l_269"
    l "W-What are you talking about? That's impossible.{#ch19_l_269}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+409, level=160, dir=1B]
    # サイト：そ、そうだよ。
    voice "ch19_s_330"
    s "R-Right. I'd never kiss Louise. Ha ha, ha ha ha…{#ch19_s_330}"

    # シエスタ：いいえ、わたしの女のカンが、
    voice "ch19_si_006"
    si "No. My woman's intuition tells me Saito-san kissed Miss Valliere.{#ch19_si_006}"

    # [SPRITE   lay5     image=+442, level=160, dir=2B]
    # サイト：そ、そんなこと……。  [voice 11993]
    voice "ch19_s_331"
    s "T-That's…{#ch19_s_331}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：あるはずないでしょ？  [voice 6531]
    voice "ch19_l_270"
    l "It's impossible, right?{#ch19_l_270}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+494, level=140, dir=1A]
    # シエスタ：なら、お二人とも……。
    voice "ch19_si_007"
    si "Then both of you—look straight into my eyes!{#ch19_si_007}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+408, level=140, dir=1B]
    # サイト：……。  [voice 11994]
    voice "ch19_s_332"
    s "…{#ch19_s_332}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+309, level=140, dir=1A]
    # ルイズ：……。  [voice 6532]
    voice "ch19_l_271"
    l "…{#ch19_l_271}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+496, level=140, dir=1A]
    # シエスタ：目……そらしましたね？  [voice 14804]
    voice "ch19_si_008"
    si "You looked away, didn't you?{#ch19_si_008}"

    # [SPRITE   lay2     image=+494, level=140, dir=1A]
    # シエスタ：ミス・ヴァリエール！
    voice "ch19_si_009"
    si "Miss Valliere! We formed an alliance, didn't we? No going off on your own!{#ch19_si_009}"

    # [SPRITE   lay2     image=+527, level=140, dir=2A]
    # シエスタ：裏切ったんですね！
    voice "ch19_si_010"
    si "You betrayed me! That's awful!{#ch19_si_010}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……。  [voice 6533]
    voice "ch19_l_272"
    l "…{#ch19_l_272}"

    # [SPRITE   lay1     hide]
    # → next scene 768
    jump ch19_3_scene_768

label ch19_3_scene_767:

    # [SPRITE   lay5     image=+403, level=160, dir=1B]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+29, level=200]
    $ fade_fx("id(29)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+497, level=160, dir=1A]
    # シエスタ：サイトさん！
    voice "ch19_si_011"
    si "Saito-san! Thank you for worrying about me.{#ch19_si_011}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：ちょ、ちょっとシエスタ。  [voice 11995]
    voice "ch19_s_333"
    s "J-Just a moment, Siesta.{#ch19_s_333}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：ちょっと、シエスタ！
    voice "ch19_l_273"
    l "Just a moment, Siesta! Why are you clinging to Saito?{#ch19_l_273}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：わ、わたしは心配してくれた
    voice "ch19_si_012"
    si "I-I'm just expressing my gratitude to Saito-san for worrying about me.{#ch19_si_012}"

    # ルイズ：感謝の意を表すると、なんで寄り添うのよ。  [voice 6535]
    voice "ch19_l_274"
    l "Expressing gratitude means clinging to him?{#ch19_l_274}"

    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：なら、言わせていただきますけど、
    voice "ch19_si_013"
    si "Then let me say this: Miss Valliere is too hard on Saito-san.{#ch19_si_013}"

    # シエスタ：こんな大仕事をしたんです。
    voice "ch19_si_014"
    si "He did such a big job. You could praise him, couldn't you?{#ch19_si_014}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：……。  [voice 6536]
    voice "ch19_l_275"
    l "…{#ch19_l_275}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     hide]
    # → next scene 768
    jump ch19_3_scene_768

label ch19_3_scene_768:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+29, level=200]
    $ fade_fx("id(29)")
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あら、タバサ。
    voice "ch19_k_084"
    k "Oh, Tabitha. Let's clear out.{#ch19_k_084}"

    # タバサ：うん。  [voice 15625]
    voice "ch19_t_051"
    t "Mm.{#ch19_t_051}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # オスマン：ミスタ・コルベール。
    voice "ch19_o_016"
    o "Mr. Colbert. Let's take the prisoners and go outside as well.{#ch19_o_016}"

    # コルベール：はい。  [voice 1166]
    voice "ch19_c_107"
    c "Yes.{#ch19_c_107}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay9     hide]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：ちょ、ちょっと。  [voice 11996]
    voice "ch19_s_334"
    s "J-Just a moment.{#ch19_s_334}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：もう、許さない。
    voice "ch19_l_276"
    l "I won't forgive you. It's all this stupid dog's fault!{#ch19_l_276}"

    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：ちょ、ちょっと待てよ。
    voice "ch19_s_335"
    s "W-Wait! Siesta, run away quickly. If you stay here any longer, your life will be in danger!{#ch19_s_335}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+530, level=160, dir=2A]
    # シエスタ：いいんです。
    voice "ch19_si_015"
    si "It's fine. I don't know what will happen if I'm with Saito-san, but it's what I wish for!{#ch19_si_015}"

    # [SPRITE   lay1     image=+372, level=160, dir=3A]
    # ルイズ：分かったわ。
    voice "ch19_l_277"
    l "I see. You've got nerve.{#ch19_l_277}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay10    vibrate=21]
    # [SPRITE   lay21    vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [SPRITE   lay19    vibrate=21]
    # [SPRITE   lay20    vibrate=21]
    # [SPRITE   lay2     vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [SPRITE   lay9     vibrate=21]
    # [SPRITE   lay6     vibrate=21]
    # [LAYER    lay0     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay10    hide, reset]
    # [SPRITE   lay21    hide, reset]
    # [SPRITE   lay1     reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay20    hide, reset]
    # [SPRITE   lay2     reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay9     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay10    hide]
    # [SPRITE   lay21    x=464, y=416]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay19    x=464, y=416]
    # [SPRITE   lay20    x=464, y=416]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # ルイズ：サイトのバカー！  [voice 6539]
    voice "ch19_l_278"
    l "Saito, you idiot!{#ch19_l_278}"

    # [SE       se0      play=+62]
    # [SE       se0      play=+61]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay10    vibrate=14]
    # [SPRITE   lay21    vibrate=14]
    # [SPRITE   lay1     hide, vibrate=14]
    # [SPRITE   lay19    vibrate=14]
    # [SPRITE   lay20    vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay9     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay10    hide, reset]
    # [SPRITE   lay21    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay20    hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay9     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [LAYER    lay0     hide, reset]
    # サイト：ぎゃー！！！  [voice 11998]
    voice "ch19_s_336"
    s "Gyaaah!!!{#ch19_s_336}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=4000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 770
    jump ch20

    # ==== КОНЕЦ ГЛАВЫ 19 ====
    jump ch20
    return

