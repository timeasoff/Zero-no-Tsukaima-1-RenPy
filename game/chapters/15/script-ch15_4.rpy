# Глава 15, часть 4 (сцены 654–659): финал, иллюзия, капитуляция Уэзерби.
# Источник: ps2_source/chapters/chapter_16_魔法の薬.txt (SCENE 654-659).

label ch15_4:
    $ tndl(None)
    $ show_sprites()

label ch15_4_scene_654:

    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+24]
    play music t23 fadein 1.0
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：さあ、行きましょう！
    voice "ch15_l_084"
    l "Come on, let's go! The castle's high ground is our goal!{#ch15_l_084}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：行くぜデルフリンガー！  [voice 13119]
    voice "ch15_s_105"
    s "Let's go, Derflinger!{#ch15_s_105}"

    # [SPRITE   lay19    image=+942, level=146, dir=1A]
    # [SPRITE   lay5     level=154]
    # [SPRITE   lay1     level=153]
    # デルフリンガー：おうよ、相棒。  [voice 1366]
    voice "ch15_d_005"
    d "Right you are, partner.{#ch15_d_005}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay6     image=+680, level=151, dir=1A]
    # [LAYER    lay0     image=+588, level=152, dir=1A]
    # キュルケ：そっちは任せたわよ、ダーリン！  [voice 3805]
    voice "ch15_k_043"
    k "Leave that side to me, darling!{#ch15_k_043}"

    # タバサ：頑張る。  [voice 15797]
    voice "ch15_t_006"
    t "I'll do my best.{#ch15_t_006}"

    # [LAYER    lay0     image=+621, level=152, dir=2A]
    # タバサ：あ、そこ敵が。  [voice 15798]
    voice "ch15_t_007"
    t "Ah, enemies there.{#ch15_t_007}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+302, level=153, dir=1A]
    # ルイズ：（まさか王宮が戦場になるなんて……）  [voice 7133]
    voice "ch15_l_085"
    l "(That the palace would become a battlefield…){#ch15_l_085}"

    # [SPRITE   lay1     image=+335, level=153, dir=2A]
    # ルイズ：（……頼んだわよ、みんな）  [voice 7134]
    voice "ch15_l_086"
    l "(I'm counting on you, everyone…){#ch15_l_086}"

    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay4     image=+561, level=149, dir=1A]
    # ギーシュ：ひ、ひいぃーーっ！  [voice 1537]
    voice "ch15_g_002"
    g "E-Eek!{#ch15_g_002}"

    # [SPRITE   lay4     x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=154, dir=1B]
    # サイト：腰を抜かして立ち止まるんじゃない！
    voice "ch15_s_106"
    s "Don't freeze up and stop! If you don't want to die, run, Guiche!{#ch15_s_106}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay1     image=+302, level=153, dir=1A]
    # ルイズ：頂上はもうすぐのはずだけど……。  [voice 7135]
    voice "ch15_l_087"
    l "The summit should be close now…{#ch15_l_087}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+713, level=151, dir=2A]
    # キュルケ：ダーリン、危ないっ！  [voice 3806]
    voice "ch15_k_044"
    k "Darling, look out!{#ch15_k_044}"

    # [SPRITE   lay5     image=+438, level=154, dir=2B]
    # サイト：おわっ！  [voice 13121]
    voice "ch15_s_107"
    s "Whoa!{#ch15_s_107}"

    # [SE       se0      play=+63]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay3     vibrate=21]
    # [SPRITE   lay20    vibrate=21]
    # [LAYER    lay0     vibrate=21]
    # [SPRITE   lay21    vibrate=21]
    # [SPRITE   lay4     vibrate=21]
    # [SPRITE   lay19    vibrate=21]
    # [SPRITE   lay6     vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     hide, reset]
    # [SPRITE   lay20    hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay21    hide, reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay6     reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay1     hide, reset]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+139, level=80]
    $ dissolve_fx("id(139)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # アキナ：……。
    ak "…{#ch15_ak_023}"

    # アキナ：あら、サイト。
    voice "ch15_ak_024"
    ak "My, Saito. You look well…{#ch15_ak_024}"

    # サイト：は、春奈！
    voice "ch15_s_108"
    s "H-Haruna! Why are you doing this…{#ch15_s_108}"

    # アキナ：あたしをハルナって呼ぶな！
    voice "ch15_ak_025"
    ak "Don't call me Haruna! My name is Akina!{#ch15_ak_025}"

    # ウェザリー：あら、誰かと思えば……。
    voice "ch15_w_001"
    w "My, who do we have here… It seems you've drawn the lead role in another grand performance.{#ch15_w_001}"

    # キュルケ：ウェザリー！
    voice "ch15_k_045"
    k "Weatherly! How dare you do this to me…{#ch15_k_045}"

    # ウェザリー：あら、キュルケ。
    voice "ch15_w_002"
    w "Oh, Kirche. Did the suggestion wear off?{#ch15_w_002}"

    # モンモランシー：わたしが解いたのよ。  [voice 4156]
    voice "ch15_m_016"
    m "I undid it.{#ch15_m_016}"

    # ウェザリー：そう、モンモランシーがね。
    voice "ch15_w_003"
    w "I see, Montmorency did. I thought I'd set it fairly deep… perhaps luck was on your side?{#ch15_w_003}"

    # ウェザリー：どうだった？
    voice "ch15_w_004"
    w "Well? Did you get to return to a pure child's heart?{#ch15_w_004}"

    # キュルケ：大きなお世話よ。  [voice 3808]
    voice "ch15_k_046"
    k "None of your business.{#ch15_k_046}"

    # キュルケ：どこかの年増達がつまらない炎ばかり
    voice "ch15_k_047"
    k "Thanks to some middle-aged woman showing us nothing but boring flames, I couldn't even sleep properly.{#ch15_k_047}"

    # ウェザリー：あら、年増って誰のことかしら？  [voice 16061]
    voice "ch15_w_005"
    w "Oh, and who might this 'middle-aged woman' be?{#ch15_w_005}"

    # アキナ：ウェザリー様のことでしょう？  [voice 189]
    voice "ch15_ak_026"
    ak "Weatherly-sama, of course.{#ch15_ak_026}"

    # ウェザリー：うるさいわね。
    voice "ch15_w_006"
    w "How rude. Age doesn't matter to an actor.{#ch15_w_006}"

    # ウェザリー：最後の一幕。
    voice "ch15_w_007"
    w "The final act. It seems the cast wants it blood-soaked.{#ch15_w_007}"

    # ウェザリー：いいわ、せいぜい、盛大に血を流させてあげる！  [voice 16064]
    voice "ch15_w_008"
    w "Fine. Then let them spill as much blood as they like!{#ch15_w_008}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay20    hide]
    # [SPRITE   lay21    hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+65]
    # [SPRITE   lay5     image=+472, level=134, dir=3B]
    # サイト：いくぜ！
    voice "ch15_s_109"
    s "Here I go! I won't let them interfere with Louise!{#ch15_s_109}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 655
    jump ch15_4_scene_655

label ch15_4_scene_655:

    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：これまでだ、ウェザリー！
    voice "ch15_s_110"
    s "This is the end, Weatherly! Akina!{#ch15_s_110}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # アキナ：ちくしょう！  [voice 190]
    voice "ch15_ak_027"
    ak "Damn!{#ch15_ak_027}"

    # ウェザリー：くっ！  [voice 16065]
    voice "ch15_w_009"
    w "Tch!{#ch15_w_009}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay21    hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+140, level=80]
    $ dissolve_fx("id(140)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：さあ、虚無の魔法を、
    voice "ch15_l_088"
    l "Now, feast your eyes on the magic of Void!{#ch15_l_088}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # ルイズ：イリュージョン！！  [voice 7137]
    voice "ch15_l_089"
    l "Illusion!!{#ch15_l_089}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+141, level=80]
    $ dissolve_fx("id(141)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # サイト：な、なんだ！
    voice "ch15_s_111"
    s "W-What! Out of the clouds…{#ch15_s_111}"

    # キュルケ：そんな……空中艦隊なんて？  [voice 3810]
    voice "ch15_k_048"
    k "No way… an aerial fleet?{#ch15_k_048}"

    # ウェザリー：どういうことだ！
    voice "ch15_w_010"
    w "What is this! Tristain—no, no country in Halkeginia has a fleet like that…!?{#ch15_w_010}"

    # サイト：（そうか、これがルイズのやりたかった魔法か。
    s "(So that's what Louise wanted. That fleet must be an illusion… something Void created…){#ch15_s_112}"

    # アキナ：ウェザリーさま、
    voice "ch15_ak_028"
    ak "Weatherly-sama, our fleet is retreating!{#ch15_ak_028}"

    # アキナ：……城の周りの兵達も！  [voice 192]
    voice "ch15_ak_029"
    ak "…And the troops around the castle too!{#ch15_ak_029}"

    # ウェザリー：負け……か。
    voice "ch15_w_011"
    w "We've lost… With the fleet gone, our numbers are meaningless.{#ch15_w_011}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay20    image=+1067, level=160, dir=1A]
    # ウェザリー：見事だった。
    voice "ch15_w_012"
    w "Well done. Now, bring down the curtain on this farce!{#ch15_w_012}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：（どういうことだ？）
    s "(What does she mean?){#ch15_s_113}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # デルフリンガー：（……自分を斬れっていってるんだよ）  [voice 1367]
    voice "ch15_d_006"
    d "(She's telling you to cut her down, partner.){#ch15_d_006}"

    menu:
        "Cut her down?{#ch15_4_c_655_1}":
            jump ch15_4_scene_659
        "That's irresponsible, isn't it?{#ch15_4_c_655_2}":
            jump ch15_4_scene_659
        "I still need Weatherly{#ch15_4_c_655_3}":
            jump ch15_4_scene_659

label ch15_4_scene_656:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：……き、斬れって？  [voice 13126]
    voice "ch15_s_114"
    s "…C-Cut her down?{#ch15_s_114}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # ウェザリー：何を迷ってる？
    voice "ch15_w_013"
    w "Why hesitate? Or do you want me to throw myself from the tower like in that play?{#ch15_w_013}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：くっ……。
    voice "ch15_s_115"
    s "Tch… No. I can't let her die.{#ch15_s_115}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：（お、女の子を斬れるわけねえだろう！）
    s "(There's no way I could cut down a girl!){#ch15_s_116}"

    # → next scene 659
    jump ch15_4_scene_659

label ch15_4_scene_657:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：それは無責任なんじゃないか？  [voice 13128]
    voice "ch15_s_117"
    s "That's irresponsible, isn't it?{#ch15_s_117}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # ウェザリー：何？  [voice 16070]
    voice "ch15_w_014"
    w "What?{#ch15_w_014}"

    # サイト：春奈をこのまま放っておくつもりか？
    voice "ch15_s_118"
    s "You were going to leave Haruna like this? You're the one who made her into 'Akina', aren't you?{#ch15_s_118}"

    # → next scene 659
    jump ch15_4_scene_659

label ch15_4_scene_658:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ダメだ。
    voice "ch15_s_119"
    s "No. I can't let her die.{#ch15_s_119}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：そうね。
    voice "ch15_k_049"
    k "Right. We still have use for Weatherly.{#ch15_k_049}"

    # → next scene 659
    jump ch15_4_scene_659

label ch15_4_scene_659:

    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay20    hide]
    # [SPRITE   lay6     x=304, y=416]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ハルナの暗示を解いてもらわないといけないし。
    voice "ch15_l_090"
    l "We need her to lift Haruna's suggestion. And to answer for what she's done.{#ch15_l_090}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay20    image=+1067, level=160, dir=1A]
    # ウェザリー：なるほど。
    voice "ch15_w_015"
    w "I see. Very well, I surrender.{#ch15_w_015}"

    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：アキナも、それでいいね？  [voice 16072]
    voice "ch15_w_016"
    w "Akina, that's fine with you too?{#ch15_w_016}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：あたしは、ウェザリー様に従います……。  [voice 193]
    voice "ch15_ak_030"
    ak "I will obey Weatherly-sama…{#ch15_ak_030}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay21    hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：それじゃあ、あたし、兵士を呼んでくるわ。
    voice "ch15_k_050"
    k "Then I'll go fetch a soldier. We need them taken into custody.{#ch15_k_050}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：ああ、頼むよ。  [voice 13131]
    voice "ch15_s_120"
    s "Ah, please do.{#ch15_s_120}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     x=64, y=0]
    # サイト：市街の戦いもほとんど終わったみたいだな。  [voice 13132]
    voice "ch15_s_121"
    s "Looks like the fighting in the city is mostly over.{#ch15_s_121}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：良かった。
    voice "ch15_l_091"
    l "Good. Phew… I'm exhausted. At my limit…{#ch15_l_091}"

    # [SPRITE   lay5     image=+434, level=160, dir=2B]
    # サイト：しかし、幻を作り出すなんてな。
    voice "ch15_s_122"
    s "Still, creating an illusion… There really is such magic.{#ch15_s_122}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：ん……。
    voice "ch15_l_092"
    l "Mm… Even if they're enemies, it's better not to hurt anyone. That's why I chose that spell.{#ch15_l_092}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：うん。
    voice "ch15_s_123"
    s "Yeah. You're right.{#ch15_s_123}"

    # [SPRITE   lay5     image=+403, level=160, dir=1B]
    # サイト：とにかく、今は休みな。
    voice "ch15_s_124"
    s "Anyway, get some rest. Good work, Louise.{#ch15_s_124}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：うん……。  [voice 7141]
    voice "ch15_l_093"
    l "Mm…{#ch15_l_093}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=4000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 665
    jump ch16

    # ==== КОНЕЦ ГЛАВЫ 15 ====
    jump ch16
    return

