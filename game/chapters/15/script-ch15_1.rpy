# Глава 15, часть 1 (сцены 619–632): утро, разоблачение Акины.
# Источник: ps2_source/chapters/chapter_16_魔法の薬.txt (SCENE 619-632).

label ch15:
    $ tndl(None)
    $ show_sprites()

label ch15_1_scene_619:

    # [TITLE title("魔法の薬")]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1160, level=200]
    $ fade_fx("id(1160)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # サイト：ふが……。  [voice 13018]
    voice "ch15_s_001"
    s "Ugh…{#ch15_s_001}"

    # キュルケ：おにぃ～～ちゃん！  [voice 3763]
    voice "ch15_k_001"
    k "Onii~chan!{#ch15_k_001}"

    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [SPRITE   lay5     hide, vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay6     hide, vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+700, level=160, dir=1C]
    # キュルケ：おはよっ！  [voice 3764]
    voice "ch15_k_002"
    k "Good morning!{#ch15_k_002}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：おわっ、キュルケ！
    voice "ch15_s_002"
    s "Whoa, Kirche! G-Good morning.{#ch15_s_002}"

    # [SPRITE   lay6     image=+698, level=160, dir=1C]
    # キュルケ：おにいちゃん、よくねむれた？  [voice 3765]
    voice "ch15_k_003"
    k "Big brother, did you sleep well?{#ch15_k_003}"

    # [SPRITE   lay5     image=+451, level=160, dir=2C]
    # サイト：う～～ん？  [voice 13020]
    voice "ch15_s_003"
    s "Uuuun?{#ch15_s_003}"

    menu:
        "I slept well{#ch15_1_c_619_1}":
            jump ch15_1_scene_620
        "I feel like I had a weird dream{#ch15_1_c_619_2}":
            jump ch15_1_scene_621
        "Um, Kirche… could you move a little away?{#ch15_1_c_619_3}":
            jump ch15_1_scene_622

label ch15_1_scene_620:

    # [SPRITE   lay5     image=+451, level=160, dir=2C]
    # [SPRITE   lay6     image=+698, level=160, dir=1C]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # サイト：ああ、よく眠れたよ。
    voice "ch15_s_004"
    s "Yeah, I slept well. Slept like a log.{#ch15_s_004}"

    # [SPRITE   lay6     image=+700, level=160, dir=1C]
    # キュルケ：ホント！
    voice "ch15_k_004"
    k "Really! Kirche slept well too.{#ch15_k_004}"

    # キュルケ：おにいちゃんといっしょだったからだねっ！
    voice "ch15_k_005"
    k "It's because I was with big brother! Let's sleep together again tonight!{#ch15_k_005}"

    # [SPRITE   lay5     image=+451, level=160, dir=2C]
    # サイト：って、俺と一緒だったって？  [voice 13022]
    voice "ch15_s_005"
    s "Wait, you were with me?{#ch15_s_005}"

    # [SPRITE   lay6     image=+704, level=160, dir=1C]
    # キュルケ：うん。
    voice "ch15_k_006"
    k "Mm. At night I got scared, and when I went to big brother…{#ch15_k_006}"

    # [SPRITE   lay6     image=+698, level=160, dir=1C]
    # キュルケ：キュルケのこと、キュッてしてくれて……。
    voice "ch15_k_007"
    k "And you held me tight… Big brother was so warm…{#ch15_k_007}"

    # [SPRITE   lay5     image=+447, level=160, dir=2C]
    # サイト：あは、あはは……。  [voice 13023]
    voice "ch15_s_006"
    s "Ha, haha…{#ch15_s_006}"

    # → next scene 623
    jump ch15_1_scene_623

label ch15_1_scene_621:

    # [SPRITE   lay5     image=+451, level=160, dir=2C]
    # [SPRITE   lay6     image=+698, level=160, dir=1C]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：なんだか、変な夢を見た気がする……。  [voice 13024]
    voice "ch15_s_007"
    s "I feel like I had a strange dream…{#ch15_s_007}"

    # [SPRITE   lay6     image=+700, level=160, dir=1C]
    # キュルケ：ゆめ？
    voice "ch15_k_008"
    k "A dream? What kind? Was Kirche in it?{#ch15_k_008}"

    # [SPRITE   lay5     image=+451, level=160, dir=2C]
    # サイト：う～～ん、細かいところは全然覚えて
    voice "ch15_s_008"
    s "Uuu… I don't remember the details at all…{#ch15_s_008}"

    # [SPRITE   lay6     image=+704, level=160, dir=1C]
    # キュルケ：ぶぅ～～っ！
    voice "ch15_k_009"
    k "Buuu! Boring. Tonight, dream of Kirche!{#ch15_k_009}"

    # [SPRITE   lay5     image=+445, level=160, dir=2C]
    # サイト：ははは。
    voice "ch15_s_009"
    s "Hahaha. Sorry, sorry.{#ch15_s_009}"

    # → next scene 623
    jump ch15_1_scene_623

label ch15_1_scene_622:

    # [SPRITE   lay5     image=+451, level=160, dir=2C]
    # [SPRITE   lay6     image=+698, level=160, dir=1C]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：あ、あの、キュルケさん？  [voice 13027]
    voice "ch15_s_010"
    s "Um, Kirche-san?{#ch15_s_010}"

    # サイト：少しだけ体を離してもらえはしませんか？  [voice 13028]
    voice "ch15_s_011"
    s "Could you move just a little away from me?{#ch15_s_011}"

    # [SPRITE   lay6     image=+704, level=160, dir=1C]
    # キュルケ：え～～！
    voice "ch15_k_010"
    k "Ehh! Why?{#ch15_k_010}"

    # キュルケ：おにいちゃん、キュルケのこときらいに
    voice "ch15_k_011"
    k "Big brother, did you stop liking Kirche?{#ch15_k_011}"

    # [SPRITE   lay5     image=+451, level=160, dir=2C]
    # サイト：そ、そういうわけじゃないけど……。  [voice 13029]
    voice "ch15_s_012"
    s "T-That's not it, but…{#ch15_s_012}"

    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：お、俺、男の子ですから。  [voice 13030]
    voice "ch15_s_013"
    s "I'm, um, a boy.{#ch15_s_013}"

    # [SPRITE   lay6     image=+698, level=160, dir=1C]
    # キュルケ：？？？  [voice 3774]
    voice "ch15_k_012"
    k "???{#ch15_k_012}"

    # → next scene 623
    jump ch15_1_scene_623

label ch15_1_scene_623:

    # [SPRITE   lay5     image=+447, level=160, dir=2C]
    # [SPRITE   lay6     image=+698, level=160, dir=1C]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # サイト：そ、そうだ！
    voice "ch15_s_014"
    s "R-Right! More importantly!{#ch15_s_014}"

    # [SPRITE   lay5     image=+449, level=160, dir=2C]
    # サイト：こんなところルイズに見つかったら
    voice "ch15_s_015"
    s "Wouldn't it be terrible if Louise found us like this!?{#ch15_s_015}"

    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：もし、そんなことになったら……。  [voice 13033]
    voice "ch15_s_016"
    s "If that happened…{#ch15_s_016}"

    # ルイズ：どうなると思う？  [voice 7049]
    voice "ch15_l_001"
    l "What do you think would happen?{#ch15_l_001}"

    # [SPRITE   lay5     image=+451, level=160, dir=2C]
    # サイト：そ、そりゃもう！
    voice "ch15_s_017"
    s "W-Why, I'd be beaten to a pulp, torn to shreds, utterly wrecked…{#ch15_s_017}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：ご主人様、おはようございます。  [voice 13035]
    voice "ch15_s_018"
    s "Good morning, mistress.{#ch15_s_018}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：うるさいわね！
    voice "ch15_l_002"
    l "Shut up! It's no use making excuses now!{#ch15_l_002}"

    # サイト：きゃ、きゃいーん！  [voice 13036]
    voice "ch15_s_019"
    s "E-Eek!{#ch15_s_019}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+62]
    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay3     vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [SPRITE   lay1     vibrate=7]
    # [SPRITE   lay6     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [SE       se0      play=+61]
    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay3     vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [SPRITE   lay1     vibrate=7]
    # [SPRITE   lay6     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+704, level=160, dir=1C]
    # キュルケ：……。  [voice 3775]
    voice "ch15_k_013"
    k "…{#ch15_k_013}"

    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：おはよう。
    voice "ch15_l_003"
    l "Good morning, Kirche.{#ch15_l_003}"

    # キュルケ：……おはよ。  [voice 3776]
    voice "ch15_k_014"
    k "…Morning.{#ch15_k_014}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：相変わらず、わたしにはなつかないのね……。
    voice "ch15_l_004"
    l "You still don't warm up to me, do you… Are you all right? That stupid dog didn't do anything weird to you?{#ch15_l_004}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+451, level=160, dir=2C]
    # サイト：だ、だから、何もしてないって。  [voice 13037]
    voice "ch15_s_020"
    s "B-But I told you, I didn't do anything!{#ch15_s_020}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+704, level=160, dir=1C]
    # キュルケ：……おにいちゃんをいじめちゃヤダ。  [voice 3777]
    voice "ch15_k_015"
    k "…I don't want to hurt big brother…{#ch15_k_015}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：もう！
    voice "ch15_l_005"
    l "Really, are you actually Kirche?{#ch15_l_005}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # モンモランシー：……おつかれさま。  [voice 4141]
    voice "ch15_m_001"
    m "…It was a rough night.{#ch15_m_001}"

    # [SPRITE   lay3     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：まったく、なんで俺がこんな目に……。  [voice 13038]
    voice "ch15_s_021"
    s "Honestly, why does this keep happening to me…{#ch15_s_021}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なあ、モンモン。
    voice "ch15_s_022"
    s "Say, Montmon. How's the medicine for Kirche's suggestion coming along?{#ch15_s_022}"

    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # モンモランシー：まだよ。  [voice 4142]
    voice "ch15_m_002"
    m "Not yet.{#ch15_m_002}"

    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # モンモランシー：言ったでしょう？
    voice "ch15_m_003"
    m "I told you? It'll take some time.{#ch15_m_003}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：俺の命が持つ間に完成してほしい、です。  [voice 13040]
    voice "ch15_s_023"
    s "I'd like it finished before my life ends, please.{#ch15_s_023}"

    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # モンモランシー：頑張ってはみるけど、期待しないで。  [voice 4144]
    voice "ch15_m_004"
    m "I'll try, but don't get your hopes up.{#ch15_m_004}"

    # モンモランシー：いま、タバサに足りないお薬の材料を
    voice "ch15_m_005"
    m "Right now Tabitha is gathering the ingredients we're missing… but it depends on the result.{#ch15_m_005}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # モンモランシー：きゃあっ！  [voice 4146]
    voice "ch15_m_006"
    m "Eek!{#ch15_m_006}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：な、なんだ！  [voice 13041]
    voice "ch15_s_024"
    s "W-What was that!{#ch15_s_024}"

    # [SE       se0      play=+57]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：サイトっ！
    voice "ch15_l_006"
    l "Saito! That explosion just now!{#ch15_l_006}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：くそ。
    voice "ch15_s_025"
    s "Damn. Is it the bomb-thrower again?{#ch15_s_025}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+704, level=160, dir=1C]
    # キュルケ：お、おにいちゃん。
    voice "ch15_k_016"
    k "B-Big brother. What was that…?{#ch15_k_016}"

    # キュルケ：おおきなおとが……。
    voice "ch15_k_017"
    k "A loud sound… and shaking…{#ch15_k_017}"

    # キュルケ：こわい、こわいよ……。  [voice 3780]
    voice "ch15_k_018"
    k "Scary, so scary…{#ch15_k_018}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（キュルケ……）
    s "(Kirche…){#ch15_s_026}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：なに、ボ～ッとしてるのよ！
    voice "ch15_l_007"
    l "Why are you spacing out! Hurry to the scene!{#ch15_l_007}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：お、おうっ！  [voice 13043]
    voice "ch15_s_027"
    s "O-Okay!{#ch15_s_027}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 624
    jump ch15_1_scene_624

label ch15_1_scene_624:

    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1150, level=200]
    $ fade_fx("id(1150)")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1141, level=200]
    $ fade_fx("id(1141)")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1150, level=200]
    $ fade_fx("id(1150)")
    # [TRANS trans("crossfade", 750)]
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [SPRITE   lay21    image=+1028, level=160, dir=1B]
    # アキナ：燃えろ、燃えろ。
    voice "ch15_ak_001"
    ak "Burn, burn. Let it all burn!{#ch15_ak_001}"

    # [SPRITE   lay21    image=+1030, level=160, dir=1B]
    # アキナ：ははっ！
    voice "ch15_ak_002"
    ak "Haha! Ahahahaha!{#ch15_ak_002}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # ルイズ：街が……。  [voice 7056]
    voice "ch15_l_008"
    l "The city…{#ch15_l_008}"

    # サイト：な、何てことしやがる！  [voice 13044]
    voice "ch15_s_028"
    s "What the hell are they doing!{#ch15_s_028}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：サイト、あそこ！  [voice 7057]
    voice "ch15_l_009"
    l "Saito, over there!{#ch15_l_009}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：あははは、来たようね！  [voice 167]
    voice "ch15_ak_003"
    ak "Ahahaha, here they come!{#ch15_ak_003}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：春奈！？
    voice "ch15_s_029"
    s "Haruna!? It's dangerous there! Get over here!{#ch15_s_029}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：早くしなさい！
    voice "ch15_l_010"
    l "Hurry! It's dangerous!{#ch15_l_010}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：あははは……。
    voice "ch15_ak_004"
    ak "Ahahaha… Still the same naive fools!{#ch15_ak_004}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：は、春奈？  [voice 13046]
    voice "ch15_s_030"
    s "H-Haruna?{#ch15_s_030}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # デルフリンガー：気をつけろ、相棒！  [voice 1362]
    voice "ch15_d_001"
    d "Careful, partner!{#ch15_d_001}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：あたしをハルナって呼ぶな！  [voice 169]
    voice "ch15_ak_005"
    ak "Don't call me Haruna!{#ch15_ak_005}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：あたしの名は『アキナ』……。  [voice 170]
    voice "ch15_ak_006"
    ak "My name is 'Akina'…{#ch15_ak_006}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：ウェザリー様につくっていただいた、
    voice "ch15_ak_007"
    ak "The real me, made by Weatherly-sama!{#ch15_ak_007}"

    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：な、なんだと！  [voice 13047]
    voice "ch15_s_031"
    s "W-What did you say!?{#ch15_s_031}"

    menu:
        "You've been lying to us all along?{#ch15_1_c_624_1}":
            jump ch15_1_scene_625
        "It's a lie, you're a fake! I don't believe it!{#ch15_1_c_624_2}":
            jump ch15_1_scene_626
        "A sick joke, right?{#ch15_1_c_624_3}":
            jump ch15_1_scene_627

label ch15_1_scene_625:

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：最初から、お、俺達を騙していたのか？  [voice 13048]
    voice "ch15_s_032"
    s "You were lying to us from the start, weren't you?{#ch15_s_032}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：さあ、どうかしらね。
    voice "ch15_ak_008"
    ak "Well, who knows. 'That girl' doesn't know anything…{#ch15_ak_008}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：でも、あたしはすべてを知って操っていたわ。
    voice "ch15_ak_009"
    ak "But I knew everything and pulled the strings. Yes, everything…{#ch15_ak_009}"

    # → next scene 628
    jump ch15_1_scene_628

label ch15_1_scene_626:

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：嘘だ、ニセモノだ！
    voice "ch15_s_033"
    s "It's a lie, you're a fake! I won't believe it!{#ch15_s_033}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：あら、嬉しい。
    voice "ch15_ak_010"
    ak "Oh, how sweet. She'll be happy when she hears that.{#ch15_ak_010}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：そして絶望するわ。
    voice "ch15_ak_011"
    ak "And then she'll despair. When she learns what she did without knowing. Ahah, wonderful!{#ch15_ak_011}"

    # → next scene 628
    jump ch15_1_scene_628

label ch15_1_scene_627:

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：な、なんだよそれ？
    voice "ch15_s_034"
    s "What's that? I can't laugh at that. Come on, it's a sick joke, right?{#ch15_s_034}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：あら、どうして？
    voice "ch15_ak_012"
    ak "Oh, why? You have to accept reality.{#ch15_ak_012}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ちくしょう！
    voice "ch15_s_035"
    s "Damn! You mean it was all set up from the beginning?{#ch15_s_035}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：そうよ、最初から。  [voice 177]
    voice "ch15_ak_013"
    ak "That's right. From the very start.{#ch15_ak_013}"

    # → next scene 628
    jump ch15_1_scene_628

label ch15_1_scene_628:

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：ど、どういうことよ！  [voice 7059]
    voice "ch15_l_011"
    l "W-What's going on here!?{#ch15_l_011}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：ふーん、ルイズにはちょっと難しいお話だった
    voice "ch15_ak_014"
    ak "Hm. Too complicated for Louise, was it?{#ch15_ak_014}"

    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：キュルケにかけられた催眠術には、
    voice "ch15_s_036"
    s "So that's what the hypnosis on Kirche could do too, huh.{#ch15_s_036}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：あら、ご名答。
    voice "ch15_ak_015"
    ak "Oh, correct. Not so dumb after all, Saito.{#ch15_ak_015}"

    # サイト：ふざけるな！
    voice "ch15_s_037"
    s "Don't toy with us! We were puppets from the start, weren't we!{#ch15_s_037}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：ウェザリー様があたしとつながっていたと
    voice "ch15_ak_016"
    ak "Kirche's deduction that I was connected to Weatherly wasn't bad, but she was just short.{#ch15_ak_016}"

    # アキナ：ホントはあたしがおまえ達の情報を
    voice "ch15_ak_017"
    ak "The truth is, I was passing your information to Weatherly-sama…{#ch15_ak_017}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：ドカン、ってやってたの。
    voice "ch15_ak_018"
    ak "And then—boom. Ahahaha…{#ch15_ak_018}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：な、なんで今頃になって……。  [voice 13054]
    voice "ch15_s_038"
    s "Why tell us this now…{#ch15_s_038}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：お芝居はもうおしまい。  [voice 183]
    voice "ch15_ak_019"
    ak "The play is over.{#ch15_ak_019}"

    # アキナ：最後の幕が開いちゃうのよね。
    voice "ch15_ak_020"
    ak "The final act is about to begin. So, my regards.{#ch15_ak_020}"

    # アキナ：ほら、礼儀は大切でしょ？  [voice 185]
    voice "ch15_ak_021"
    ak "See? Manners matter, don't they?{#ch15_ak_021}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：あははは、じゃあね～～！  [voice 186]
    voice "ch15_ak_022"
    ak "Ahahaha, bye bye~~!{#ch15_ak_022}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 629
    jump ch15_1_scene_629

label ch15_1_scene_629:

    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：まさか、ハルナが爆弾使いだったなんて。  [voice 7060]
    voice "ch15_l_012"
    l "No… Haruna was the bomb-thrower…{#ch15_l_012}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：違う！
    voice "ch15_s_039"
    s "No! Like Kirche, Haruna is just being controlled.{#ch15_s_039}"

    # ルイズ：それはそうだけど……。  [voice 7061]
    voice "ch15_l_013"
    l "Even so…{#ch15_l_013}"

    menu:
        "I'll stop Haruna myself{#ch15_1_c_629_1}":
            jump ch15_1_scene_630
        "Weatherly…{#ch15_1_c_629_2}":
            jump ch15_1_scene_631
        "So that's why the performance…{#ch15_1_c_629_3}":
            jump ch15_1_scene_632

label ch15_1_scene_630:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：春奈は俺が止めてみせる。  [voice 13056]
    voice "ch15_s_040"
    s "I'll stop Haruna myself.{#ch15_s_040}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：……。  [voice 7062]
    voice "ch15_l_014"
    l "…{#ch15_l_014}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：もう、分かったわサイト。
    voice "ch15_l_015"
    l "Fine, I understand, Saito. Do as you like.{#ch15_l_015}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：え、いいの？
    voice "ch15_s_041"
    s "Eh, really? For real?{#ch15_s_041}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：『アキナ』の話だと、
    voice "ch15_l_016"
    l "According to 'Akina', Haruna herself doesn't know what she's done, right?{#ch15_l_016}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：真実を知って、ハルナが落ち込んでも、
    voice "ch15_l_017"
    l "So when she learns the truth and falls apart, you'll be there to catch her. That's an order from your mistress.{#ch15_l_017}"

    # → next scene 633
    jump ch15_2

label ch15_1_scene_631:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：悪いのはウェザリーなんだ。  [voice 13058]
    voice "ch15_s_042"
    s "The one at fault is Weatherly.{#ch15_s_042}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：旅の一座の座長……なんて言って、
    voice "ch15_l_018"
    l "A traveling troupe's leader, my foot—what a fraud she turned out to be.{#ch15_l_018}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：キュルケが襲われる前に言ってた。  [voice 13059]
    voice "ch15_s_043"
    s "Kirche said before she was attacked.{#ch15_s_043}"

    # サイト：ウェザリーの背後にいるのは
    voice "ch15_s_044"
    s "That behind Weatherly there might be someone much bigger.{#ch15_s_044}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：結果的には、キュルケが一番真実に
    voice "ch15_l_019"
    l "In the end, Kirche was closest to the truth.{#ch15_l_019}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：どうしたのおにいちゃん？  [voice 3781]
    voice "ch15_k_019"
    k "What's wrong, big brother?{#ch15_k_019}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：なんでもないって、キュルケ。
    voice "ch15_s_045"
    s "It's nothing, Kirche. I was just praising you—you're smart.{#ch15_s_045}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：そうね。
    voice "ch15_l_020"
    l "Yes. Though it's bitter.{#ch15_l_020}"

    # → next scene 633
    jump ch15_2

label ch15_1_scene_632:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：だから公演のとき、あんなに俺達を
    voice "ch15_s_046"
    s "So that's why she wanted to use us so much during the performance.{#ch15_s_046}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そう、だから、あんなに偉そうに
    voice "ch15_l_021"
    l "Yes, that's why she bossed us around so much.{#ch15_l_021}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：あ、あの筋肉痛のウラミ、
    voice "ch15_l_022"
    l "Hm… Should I let that muscle ache grudge go?{#ch15_l_022}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ちょっとまて、ルイズ！
    voice "ch15_s_047"
    s "Wait a second, Louise! You're angry about the wrong thing!{#ch15_s_047}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：いいの！
    voice "ch15_l_023"
    l "I don't care! I'm furious right now!{#ch15_l_023}"

    # → next scene 633
    jump ch15_2

    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch15_2
    return

