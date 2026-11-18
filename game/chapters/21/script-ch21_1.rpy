# Глава 21, часть 1 (сцены 771–779): Сиэста становится горничной Луизы.
# Источник: ps2_source/chapters/chapter_22_サイトのメイド.txt (SCENE 771-779).

label ch21:
    $ tndl(None)
    $ show_sprites()

label ch21_1_scene_771:

    # [TITLE title("サイトのメイド")]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # サイト：（演劇が終わってから、かれこれ数日。
    s "(A few days have passed since the play ended. Suddenly, the bomber stopped showing up.){#ch21_s_001}"

    # サイト：（そのため、みんなそろって魔法学院に
    s "(So we all ended up returning to the magic academy, but…){#ch21_s_002}"

    # サイト：（結果らしい結果をだせなかったことと、
    s "(Since we got no real results and still don't know who the bomber is, everyone's on edge.){#ch21_s_003}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1162, level=200]
    $ fade_fx("id(1162)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：やっぱり、納得いかないわっ！
    voice "ch21_l_001"
    l "I still can't accept it! What was that bomber, suddenly vanishing like that!{#ch21_l_001}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：わたしが受けた屈辱は、
    voice "ch21_l_002"
    l "How am I supposed to deal with the humiliation I suffered!{#ch21_l_002}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：あきらめが悪いわね、ホントに。
    voice "ch21_k_001"
    k "You're a sore loser, really. What's the point of regretting something that's over?{#ch21_k_001}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：なんですってぇ！？  [voice 6542]
    voice "ch21_l_003"
    l "What was that!?{#ch21_l_003}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：もっと前向きに考えなさいよ。
    voice "ch21_k_002"
    k "Look on the bright side. You'll go bald, you know? {#ch21_k_002}"

    # [SPRITE   lay1     image=+372, level=160, dir=3A]
    # ルイズ：んなっ……キュルケっ！？  [voice 6543]
    voice "ch21_l_004"
    l "Wha—! Kirche!?{#ch21_l_004}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：お、落ち着け、ルイズっ！！
    voice "ch21_s_004"
    s "Hey, calm down, Louise!! Are you trying to blow up the room!?{#ch21_s_004}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：ダーリンも、こんな短気なルイズの使い魔
    voice "ch21_k_003"
    k "Darling, why don't you quit being that short-tempered Louise's familiar and become mine instead?{#ch21_k_003}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+373, level=140, dir=3A]
    # ルイズ：どさくさにまぎれて、
    voice "ch21_l_005"
    l "Don't you dare hug Saito in the confusion!{#ch21_l_005}"

    # [SPRITE   lay1     hide]
    # [SE       se0      play=+95]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [SPRITE   lay4     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     hide, reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # サイト：うわー！  [voice 12000]
    voice "ch21_s_005"
    s "Wah!{#ch21_s_005}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # サイト：（まったく、ルイズもキュルケも……。
    s "(Honestly, both Louise and Kirche… Fighting won't get us anywhere, will it?){#ch21_s_006}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：……。  [voice 14812]
    voice "ch21_si_001"
    si "…{#ch21_si_001}"

    # サイト：（シエスタ、どうしたんだろ……。
    s "(Siesta? What's wrong with her… She's been standing there frozen…){#ch21_s_007}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：シエスタ、どうしたの？  [voice 12001]
    voice "ch21_s_008"
    s "Siesta, what's wrong?{#ch21_s_008}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+526, level=160, dir=2A]
    # シエスタ：きゃっ！  [voice 14813]
    voice "ch21_si_002"
    si "Eep!{#ch21_si_002}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ああっ、ごめんっ！
    voice "ch21_s_009"
    s "Ah, sorry! I didn't mean to startle you.{#ch21_s_009}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：わ、わたしの方こそ、
    voice "ch21_si_003"
    si "N-No, I'm the one who got startled, sorry.{#ch21_si_003}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：どうしたのさ、さっきからボーッとして。  [voice 12003]
    voice "ch21_s_010"
    s "What's wrong? You've been spacing out this whole time.{#ch21_s_010}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あ、そ、そうでした。
    voice "ch21_si_004"
    si "A-Ah, that's right. I was just about to bring the cake and tea.{#ch21_si_004}"

    # シエスタ：では、失礼しますね、サイトさん。  [voice 14816]
    voice "ch21_si_005"
    si "Well then, excuse me, Saito-san.{#ch21_si_005}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：あ、うん。  [voice 12004]
    voice "ch21_s_011"
    s "A, okay.{#ch21_s_011}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（シエスタ、どうしたんだろう？
    s "(What's wrong with Siesta?… Did she take the tea to Guiche and Montmorency's table?){#ch21_s_012}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：お待たせして申し訳ありません。
    voice "ch21_si_006"
    si "Sorry to keep you waiting. I've brought your tea and cake.{#ch21_si_006}"

    # [SPRITE   lay2     x=224, y=0]
    # [SPRITE   lay4     image=+555, level=160, dir=1A]
    # ギーシュ：いやあ、ありがとう。
    voice "ch21_g_001"
    g "Ah, thanks. Pour the tea from her cup, would you?{#ch21_g_001}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：はい、かしこまりました。  [voice 14818]
    voice "ch21_si_007"
    si "Yes, certainly.{#ch21_si_007}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：……。  [voice 14819]
    voice "ch21_si_008"
    si "…{#ch21_si_008}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay3     vibrate=7]
    # [SPRITE   lay2     vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [SPRITE   lay4     vibrate=7]
    # [SPRITE   lay1     vibrate=7]
    # [SPRITE   lay6     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     reset]
    # [SPRITE   lay2     reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # モンモランシー：きゃああっ……ちょっと、お茶がっ！！  [voice 4098]
    voice "ch21_m_001"
    m "Kyaaa! Oh no, the tea!{#ch21_m_001}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay4     image=+559, level=160, dir=1A]
    # ギーシュ：あ～～っ！！
    voice "ch21_g_002"
    g "Ahh!! Montmorency! What are you doing, girl!?{#ch21_g_002}"

    # [SPRITE   lay2     image=+526, level=160, dir=2A]
    # シエスタ：え？
    voice "ch21_si_009"
    si "Eh? Ah!{#ch21_si_009}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：も、申し訳ございません！！  [voice 14821]
    voice "ch21_si_010"
    si "I-I'm terribly sorry!!{#ch21_si_010}"

    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # ギーシュ：おお、なんてことなんだ！
    voice "ch21_g_003"
    g "Oh no. Did you burn yourself, Montmorency?{#ch21_g_003}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # モンモランシー：もう、制服が台無しだわ。  [voice 4099]
    voice "ch21_m_002"
    m "Really, my uniform is ruined.{#ch21_m_002}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：申し訳ございませんっ！
    voice "ch21_si_011"
    si "I'm so sorry! I'll wipe it right away and bring you a new one!{#ch21_si_011}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # サイト：（ああ、見てられないっ！
    s "(Ah, I can't watch this! I'll go over!){#ch21_s_013}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：大丈夫か、シエスタ？
    voice "ch21_s_014"
    s "Are you all right, Siesta? Did you burn yourself?{#ch21_s_014}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # モンモランシー：ちょっと、お茶かけられたのはわたしよ！
    voice "ch21_m_003"
    m "Hey! I'm the one who got the tea on me! You've got the wrong person to worry about!{#ch21_m_003}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ああ、モンモン、すまなかった。
    voice "ch21_s_015"
    s "Ah, Montmorency, sorry. Siesta seems a bit tired.{#ch21_s_015}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # シエスタ：あっ……。
    voice "ch21_si_012"
    si "Ah… No, really, Saito-san, apologizing… It's my carelessness, so… I'm sorry!{#ch21_si_012}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay4     image=+570, level=160, dir=2A]
    # [SPRITE   lay3     image=+889, level=160, dir=2A]
    # ギーシュ：ふん、せっかくのティータイムが台無しだ。
    voice "ch21_g_004"
    g "Hmph, our tea time is ruined. I've completely lost the mood for it. Let's go, Montmorency.{#ch21_g_004}"

    # モンモランシー：ええ！  [voice 4101]
    voice "ch21_m_004"
    m "Right!{#ch21_m_004}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：ごめんなさい。
    voice "ch21_si_013"
    si "I'm sorry. My mistake caused trouble for Saito-san too…{#ch21_si_013}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：元気だせよ、シエスタ。
    voice "ch21_s_016"
    s "Cheer up, Siesta. What you failed at today, you can make up for tomorrow, right?{#ch21_s_016}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：はい……。  [voice 14825]
    voice "ch21_si_014"
    si "Yes…{#ch21_si_014}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：でも、わたし……。
    voice "ch21_si_015"
    si "But I… I've decided to take a few days off starting tomorrow.{#ch21_si_015}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ええっ！？
    voice "ch21_s_017"
    s "Eh!? Why?{#ch21_s_017}"

    # シエスタ：実は、魔法学院に帰ってきてから、
    voice "ch21_si_016"
    si "Actually, ever since I came back to the academy, I've been like this the whole time.{#ch21_si_016}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：落ち着くまで、メイドの仕事は
    voice "ch21_si_017"
    si "They told me to refrain from my maid duties until I calm down.{#ch21_si_017}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：なので、実家に戻りまして、
    voice "ch21_si_018"
    si "So I was thinking of going back to my family home to settle my mind a little.{#ch21_si_018}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そんなぁ……。
    voice "ch21_s_018"
    s "No way… Telling you to take time off is going too far.{#ch21_s_018}"

    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # シエスタ：わたしの未熟さが悪いんです……。  [voice 14830]
    voice "ch21_si_019"
    si "It's because I'm so inept…{#ch21_si_019}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：なぁ、シエスタ。
    voice "ch21_s_019"
    s "Listen, Siesta. If I can help, I'll do anything. So don't say you'll leave the academy.{#ch21_s_019}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：ありがとうございます……。  [voice 14831]
    voice "ch21_si_020"
    si "Thank you very much…{#ch21_si_020}"

    # シエスタ：……。  [voice 14832]
    voice "ch21_si_021"
    si "…{#ch21_si_021}"

    # サイト：？？？  [voice 12011]
    voice "ch21_s_020"
    s "???{#ch21_s_020}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あの……。
    voice "ch21_si_022"
    si "Um… Saito-san. May I ask you to help me?{#ch21_si_022}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ああ？
    voice "ch21_s_021"
    s "Huh? Sure, but…{#ch21_s_021}"

    # [SPRITE   lay2     image=+530, level=160, dir=2A]
    # シエスタ：あの……。
    voice "ch21_si_023"
    si "Um… Um… Um!{#ch21_si_023}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：あの？  [voice 12013]
    voice "ch21_s_022"
    s "Um?{#ch21_s_022}"

    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：わたしをサイトさんのメイドにしてください！！  [voice 14835]
    voice "ch21_si_024"
    si "Please make me your maid, Saito-san!{#ch21_si_024}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay3     vibrate=7]
    # [SPRITE   lay2     vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [SPRITE   lay4     vibrate=7]
    # [SPRITE   lay1     vibrate=7]
    # [SPRITE   lay6     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     hide, reset]
    # [SPRITE   lay2     reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # サイト：い？  [voice 12014]
    voice "ch21_s_023"
    s "Eh?{#ch21_s_023}"

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay2     image=+497, level=160, dir=1A]
    # シエスタ：サイトさんをご主人様として初心に返り、
    voice "ch21_si_025"
    si "I want to start over with you as my master and polish my skills as a servant again!{#ch21_si_025}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ぼ、ボクがご主人様ですかぁ！？
    voice "ch21_s_024"
    s "M-Me, a master!? T-That is…{#ch21_s_024}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ダメよ、そんなのっ！
    voice "ch21_l_006"
    l "No way! I won't allow it. Absolutely not!{#ch21_l_006}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ル、ルイズ。
    voice "ch21_s_025"
    s "L-Louise. Where were you listening from?{#ch21_s_025}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：はじめから全部よ。
    voice "ch21_l_007"
    l "From the very beginning. Siesta becoming Saito's maid is absolutely not allowed!{#ch21_l_007}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：で、ですよね。
    voice "ch21_s_026"
    s "R-Right. So then…{#ch21_s_026}"

    menu:
        "How about becoming Kirche's maid?{#ch21_1_c_771_1}":
            jump ch21_1_scene_772
        "How about becoming Tabitha's maid?{#ch21_1_c_771_2}":
            jump ch21_1_scene_773
        "How about becoming Guiche's maid?{#ch21_1_c_771_3}":
            jump ch21_1_scene_774

label ch21_1_scene_772:

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：キュルケんとこのメイドになるってのはどう？  [voice 12018]
    voice "ch21_s_027"
    s "How about becoming Kirche's maid?{#ch21_s_027}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：冗談じゃないわっ！！
    voice "ch21_l_008"
    l "Don't be ridiculous!! That's out of the question!{#ch21_l_008}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：な、なんでさ。
    voice "ch21_s_028"
    s "W-Why? If our place won't do, then what else can we do?{#ch21_s_028}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：だからって、ツェルプストーに頼るような
    voice "ch21_l_009"
    l "That's no reason to go running to Zerbst!{#ch21_l_009}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そ、そういうことじゃないと思うけど……。  [voice 12020]
    voice "ch21_s_029"
    s "I don't think that's what this is about, but…{#ch21_s_029}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：とにかく、だめっ！  [voice 6549]
    voice "ch21_l_010"
    l "In any case, no!{#ch21_l_010}"

    # → next scene 775
    jump ch21_1_scene_775

label ch21_1_scene_773:

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：タバサんとこのメイドになるってのはどう？  [voice 12021]
    voice "ch21_s_030"
    s "How about becoming Tabitha's maid?{#ch21_s_030}"

    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：タバサなら、安心できるんじゃない？  [voice 6550]
    voice "ch21_l_011"
    l "Tabitha might be fine, don't you think?{#ch21_l_011}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：え、ええっと……。
    voice "ch21_si_026"
    si "E-Erm… But Miss Tabitha does everything for herself…{#ch21_si_026}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：わたしのいる意味がないと……思います。  [voice 14838]
    voice "ch21_si_027"
    si "I don't think there's any need for me…{#ch21_si_027}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そっか。
    voice "ch21_s_031"
    s "Yeah. Tabitha can manage most things with magic.{#ch21_s_031}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：悪かったわね！
    voice "ch21_l_012"
    l "Sorry about that! I can't do everything with magic!{#ch21_l_012}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そ、そんなこと言ってないだろ。  [voice 12023]
    voice "ch21_s_032"
    s "I didn't say that.{#ch21_s_032}"

    # → next scene 775
    jump ch21_1_scene_775

label ch21_1_scene_774:

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ギーシュんとこのメイドになるってのはどう？  [voice 12024]
    voice "ch21_s_033"
    s "How about becoming Guiche's maid?{#ch21_s_033}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：えっ……。  [voice 14839]
    voice "ch21_si_028"
    si "Eh…{#ch21_si_028}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ちょっと、あんた。
    voice "ch21_l_013"
    l "Hey. Are you serious about that!?{#ch21_l_013}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ほ、本気だけど。  [voice 12025]
    voice "ch21_s_034"
    s "I-I am, but…{#ch21_s_034}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：あんたバカじゃないの！？
    voice "ch21_l_014"
    l "Are you an idiot!? Think about Siesta a little more!{#ch21_l_014}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：確かに、あのギーシュじゃな……。  [voice 12026]
    voice "ch21_s_035"
    s "Well, Guiche would be…{#ch21_s_035}"

    # → next scene 775
    jump ch21_1_scene_775

label ch21_1_scene_775:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # シエスタ：はぁ、やはりわたし、実家に帰らなければ
    voice "ch21_si_029"
    si "Sigh… I really do have to go back to my family home, don't I…{#ch21_si_029}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ルイズ……。  [voice 12027]
    voice "ch21_s_036"
    s "Louise…{#ch21_s_036}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：あーもう！
    voice "ch21_l_015"
    l "Ugh, fine! I get it! You can stay in my room!{#ch21_l_015}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：わあっ、ありがとうございますっ！
    voice "ch21_si_030"
    si "Wah, thank you so much! I'll work as hard as I can!{#ch21_si_030}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：その代わり、サイトの世話じゃなくて、
    voice "ch21_l_016"
    l "Instead, you'll be serving me, not taking care of Saito. That's fine with you, right?{#ch21_l_016}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：はいっ、ミス・ヴァリエール。
    voice "ch21_si_031"
    si "Yes, Miss Valliere. Please take care of me from now on.{#ch21_si_031}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：これでひとまずは、一件落着かな？  [voice 12028]
    voice "ch21_s_037"
    s "Well, that settles it for now, I guess?{#ch21_s_037}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：サイトさん、どうもありがとうございます。
    voice "ch21_si_032"
    si "Saito-san, thank you very much. From now on I'll do my best to become a true maid.{#ch21_si_032}"

    # サイト：（こうしてシエスタは、ルイズの給仕を
    s "(And so, Siesta began serving Louise.){#ch21_s_038}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 776
    jump ch21_1_scene_776

label ch21_1_scene_776:

    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # サイト：（シエスタがルイズのメイドになってから、
    s "(A few more days passed quickly after Siesta became Louise's maid.){#ch21_s_039}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：ふんふふんふーん♪  [voice 14844]
    voice "ch21_si_033"
    si "Hum hum hum hum~{#ch21_si_033}"

    # サイト：（シエスタのやつ、ルイズのメイドに
    s "(Siesta seems to be in a great mood ever since she became Louise's maid…){#ch21_s_040}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：サイトさん、ハルナさん。
    voice "ch21_si_034"
    si "Saito-san, Haruna-san. I'm going to wipe the floor now, so please get up on the bed.{#ch21_si_034}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：うん、分かったわ。  [voice 2385]
    voice "ch21_ha_001"
    ha "Mm, okay.{#ch21_ha_001}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：オーケー。
    voice "ch21_s_041"
    s "All right. Want me to help, too?{#ch21_s_041}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：いえ、とんでもない！
    voice "ch21_si_035"
    si "No, not at all! This is my job as a maid. Saito-san, please just relax.{#ch21_si_035}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：なら、シエスタ。
    voice "ch21_l_017"
    l "Then, Siesta, we'll leave the rest to you. We're going out for a bit.{#ch21_l_017}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ルイズ、どこか出かけるのか？  [voice 12030]
    voice "ch21_s_042"
    s "Louise, are you going somewhere?{#ch21_s_042}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：サイトとハルナも、
    voice "ch21_l_018"
    l "Could you come with me for a bit, Saito and Haruna?{#ch21_l_018}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：私も？  [voice 2386]
    voice "ch21_ha_002"
    ha "Me too?{#ch21_ha_002}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あっ……はい、かしこまりました。
    voice "ch21_si_036"
    si "Ah… Yes, certainly. Have a good outing, everyone!{#ch21_si_036}"

    # [SPRITE   lay2     hide]
    # [BG       stage    hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+57]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：おはよう、タバサ。
    voice "ch21_l_019"
    l "Good morning, Tabitha. Sorry to intrude.{#ch21_l_019}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：おはよう。  [voice 15626]
    voice "ch21_t_001"
    t "Good morning.{#ch21_t_001}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay4     image=+555, level=160, dir=1A]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # ギーシュ：やあ、サイトも同席するのか。  [voice 1522]
    voice "ch21_g_005"
    g "Yo, so Saito's joining us too?{#ch21_g_005}"

    # モンモランシー：もう、結局全員集めたわけ？  [voice 4102]
    voice "ch21_m_005"
    m "Really, you gathered everyone after all?{#ch21_m_005}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なんだよおい、キュルケもいるし、
    voice "ch21_s_043"
    s "What is this, everyone's here! What's going on!?{#ch21_s_043}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：それじゃあ早速、緊急会議を始めるわ。
    voice "ch21_l_020"
    l "Then let's start the emergency meeting. Topic: Siesta!{#ch21_l_020}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：シエスタがどうかしたのか？  [voice 12032]
    voice "ch21_s_044"
    s "Did something happen to Siesta?{#ch21_s_044}"

    # ルイズ：サイトが気づいていたかどうかは、
    voice "ch21_l_021"
    l "I don't know if you noticed, but Siesta hasn't been herself since she came back from the trip.{#ch21_l_021}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：問題視した学院がシエスタに
    voice "ch21_l_022"
    l "The academy giving her leave is good proof. She must have been quite unwell.{#ch21_l_022}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # ギーシュ：紅茶をかけられたのも、
    voice "ch21_g_006"
    g "I wasn't the only one she spilled tea on, it seems. No wonder she got scolded.{#ch21_g_006}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：今はもう平気そうじゃないか。  [voice 12033]
    voice "ch21_s_045"
    s "She seems fine now, though.{#ch21_s_045}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay4     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # キュルケ：あら、それじゃあ緊急会議はもうおしまい？
    voice "ch21_k_004"
    k "Oh, so the emergency meeting's over? What a letdown.{#ch21_k_004}"

    # タバサ：原因が分からない。  [voice 15627]
    voice "ch21_t_002"
    t "We don't know the cause.{#ch21_t_002}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：そうね。
    voice "ch21_l_023"
    l "Right. We still don't know why Siesta was acting strange.{#ch21_l_023}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # モンモランシー：まあ、でも、シエスタのお陰で、
    voice "ch21_m_006"
    m "Well, but thanks to Siesta, Louise doesn't have to do her own laundry anymore— isn't that good for a noble?{#ch21_m_006}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：ま、まあ、確かにそうね。  [voice 6563]
    voice "ch21_l_024"
    l "W-Well, yes, that's true.{#ch21_l_024}"

    # サイト：（いや、前もお前洗濯してないだろ）
    s "(No, you never did your own laundry before either…){#ch21_s_046}"

    # [SPRITE   lay3     image=+885, level=160, dir=2A]
    # モンモランシー：わたし達は魔法でなんとかしてしまうけど……。
    voice "ch21_m_007"
    m "We can manage anything with magic… But you… You wash by hand, don't you?{#ch21_m_007}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：う、うるさいわよ、洪水のモンモランシー！
    voice "ch21_l_025"
    l "Sh-Shut up, flood Montmorency! You're good with water magic, so you're fine, but I'm not!{#ch21_l_025}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あら、わたしは火が得意だけど、
    voice "ch21_k_005"
    k "Oh, I'm good with fire, but I still do laundry with magic, you know?{#ch21_k_005}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……わたしも。  [voice 15628]
    voice "ch21_t_003"
    t "…Me too.{#ch21_t_003}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：う……。  [voice 6565]
    voice "ch21_l_026"
    l "Ugh…{#ch21_l_026}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：待てよ？
    voice "ch21_s_047"
    s "Wait a second… That means…{#ch21_s_047}"

    menu:
        "Did you do it yourself before I came?{#ch21_1_c_776_1}":
            jump ch21_1_scene_777
        "Does Louise actually like laundry?{#ch21_1_c_776_2}":
            jump ch21_1_scene_778
        "I don't mind doing it again{#ch21_1_c_776_3}":
            jump ch21_1_scene_779

label ch21_1_scene_777:

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：シエスタが来る前は俺が洗濯してたわけで……。
    voice "ch21_s_048"
    s "Before Siesta came, I did the laundry… So before I came to this world, you did it yourself?{#ch21_s_048}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：桶に水を汲んできて、部屋で洗ってたのよね？
    voice "ch21_k_006"
    k "You carried water in a bucket and washed in your room, didn't you? I know you wandered the halls at night.{#ch21_k_006}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：うっ、うるさいわねっ！
    voice "ch21_l_027"
    l "U-Ugh, shut up! Just leave me alone!{#ch21_l_027}"

    # → next scene 780
    jump ch21_2

label ch21_1_scene_778:

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：もしかして、ルイズって意外と洗濯好き？  [voice 12036]
    voice "ch21_s_049"
    s "Could it be that Louise actually likes doing laundry?{#ch21_s_049}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ど、どうして？  [voice 6567]
    voice "ch21_l_028"
    l "W-Why?{#ch21_l_028}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：だってほら、俺が来たばっかりの時は
    voice "ch21_s_050"
    s "Well, when I first got here, I did the laundry, but lately you've been doing it yourself, haven't you?{#ch21_s_050}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：そっ、それは……。  [voice 6568]
    voice "ch21_l_029"
    l "T-That's…{#ch21_l_029}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：だから、洗濯好きなのかなーって思ってさ。  [voice 12038]
    voice "ch21_s_051"
    s "So I thought maybe you liked it.{#ch21_s_051}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：そんなわけないでしょっ！
    voice "ch21_l_030"
    l "That's ridiculous! Are you an idiot!?{#ch21_l_030}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：……なんでそんなに怒るんだよ。  [voice 12039]
    voice "ch21_s_052"
    s "…Why are you so angry?{#ch21_s_052}"

    # → next scene 780
    jump ch21_2

label ch21_1_scene_779:

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：シエスタが元の仕事に戻ったら、
    voice "ch21_s_053"
    s "Once Siesta goes back to her old job, I'll do the laundry again. Don't worry.{#ch21_s_053}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：い、いいの、それは！  [voice 6570]
    voice "ch21_l_031"
    l "N-No, that's fine!{#ch21_l_031}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：前は普通に洗わせてたくせに。  [voice 12041]
    voice "ch21_s_054"
    s "You used to let me wash them without a second thought.{#ch21_s_054}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：あ、あんたがわたしの洗濯物見て、
    voice "ch21_l_032"
    l "Because you might be looking at my laundry and grinning!{#ch21_l_032}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ええっ！
    voice "ch21_s_055"
    s "Eh! You saw!?{#ch21_s_055}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：学院中の噂になってたのよ。
    voice "ch21_l_033"
    l "It became the talk of the whole academy—that my familiar was grinning while doing the laundry. Ugh, the worst!{#ch21_l_033}"

    # → next scene 780
    jump ch21_2

    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch21_2
    return

