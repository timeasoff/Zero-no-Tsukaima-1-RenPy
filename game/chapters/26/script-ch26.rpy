# Глава 26, часть 1 (сцены 934–943): спор из-за Харуны, поездка в Галлию.
# Источник: ps2_source/chapters/chapter_27_タバサの秘密.txt (SCENE 934-943).

label ch26:
    $ tndl(None)
    $ show_sprites()

label ch26_1_scene_934:

    # [TITLE title("タバサの秘密")]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1155, level=200]
    $ fade_fx("id(1155)")
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
    # [SE       se0      play=+69]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # サイト：……。  [voice 12514]
    voice "ch26_s_001"
    s "…{#ch26_s_001}"

    # シエスタ：サイトさん……起きてください！  [voice 15048]
    voice "ch26_si_001"
    si "Saito-san… Please wake up!{#ch26_si_001}"

    # サイト：……んっ、んぁ？  [voice 12515]
    voice "ch26_s_002"
    s "…Mm, nn?{#ch26_s_002}"

    # シエスタ：起きてくださいってば、サイトさん！  [voice 15049]
    voice "ch26_si_002"
    si "I said wake up, Saito-san!{#ch26_si_002}"

    # サイト：……もう食べられない。  [voice 12516]
    voice "ch26_s_003"
    s "…I can't eat any more.{#ch26_s_003}"

    # シエスタ：もう、寝ぼけないでください！
    voice "ch26_si_003"
    si "Honestly, don't sleep-talk! It's serious!{#ch26_si_003}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     x=304, y=416]
    # [SPRITE   lay1     x=304, y=416]
    # [SPRITE   lay6     x=304, y=416]
    # [SPRITE   lay2     image=+505, level=140, dir=1B]
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # サイト：んん？
    voice "ch26_s_004"
    s "Mm? Siesta, what's the matter?{#ch26_s_004}"

    # シエスタ：ミス・ヴァリエールがっ！
    voice "ch26_si_004"
    si "Miss Valliere! Miss Valliere and Miss Tabitha are having a fight…!{#ch26_si_004}"

    # サイト：ルイズがタバサと、どうして？  [voice 12518]
    voice "ch26_s_005"
    s "Louise and Tabitha? Why?{#ch26_s_005}"

    # シエスタ：なんでって、決まってるじゃないですか！？
    voice "ch26_si_005"
    si "Why? It's obvious! It's about Haruna-san!{#ch26_si_005}"

    # [SPRITE   lay2     image=+504, level=160, dir=1B]
    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # サイト：あーっ、そりゃ大変だっ！
    voice "ch26_s_006"
    s "Oh no, that's bad! I'll go check right away!{#ch26_s_006}"

    # シエスタ：はいっ！
    voice "ch26_si_006"
    si "Yes! Please do!{#ch26_si_006}"

    # [SPRITE   lay5     image=+449, level=160, dir=2C]
    # サイト：まさか、ルイズが……。
    voice "ch26_s_007"
    s "I can't believe Louise would… Wait, they'll find out we all peeked at the letter!{#ch26_s_007}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # ルイズ：……。  [voice 6823]
    voice "ch26_l_001"
    l "…{#ch26_l_001}"

    # タバサ：……。
    t "…{#ch26_t_001}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+677, level=140, dir=1A]
    # キュルケ：あ、ダーリン！  [voice 3497]
    voice "ch26_k_001"
    k "Ah, darling!{#ch26_k_001}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：どうなってんだよ、こりゃ？
    voice "ch26_s_008"
    s "What's going on here? Weren't we all supposed to pretend we didn't know about the letter?{#ch26_s_008}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：そんなこと言ったって……。  [voice 3498]
    voice "ch26_k_002"
    k "Well, I mean…{#ch26_k_002}"

    # キュルケ：いきなりルイズが乗り込んできて、
    voice "ch26_k_003"
    k "Louise barged in and started telling Tabitha not to take Haruna to Gallia.{#ch26_k_003}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：はぁー、なにやってんだよ。  [voice 12522]
    voice "ch26_s_009"
    s "Sigh… What is she doing…{#ch26_s_009}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：（でも、ルイズが春奈をかばうようなことを
    s "(But for Louise to say something that sounds like she's protecting Haruna…){#ch26_s_010}"

    # キュルケ：でもタバサは、連れて行くって
    voice "ch26_k_004"
    k "But Tabitha said she'd take her, didn't she? Well, for Tabitha it is a mission.{#ch26_k_004}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：で、それから、ルイズが一方的に
    voice "ch26_k_005"
    k "And now Louise is shouting one-sidedly, while Tabitha just stays silent.{#ch26_k_005}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：な、なるほどね……。  [voice 12523]
    voice "ch26_s_011"
    s "I-I see…{#ch26_s_011}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # ルイズ：もう一度言うわよ！
    voice "ch26_l_002"
    l "I'll say it again! I will never hand Haruna over!{#ch26_l_002}"

    # タバサ：……。
    t "…{#ch26_t_002}"

    # ルイズ：だいたい、任務だかなんだか知らないけれど、
    voice "ch26_l_003"
    l "Honestly, I don't know what about this 'mission'—but selling a commoner… a friend, is shameful for a noble!{#ch26_l_003}"

    # タバサ：……。
    t "…{#ch26_t_003}"

    # ルイズ：黙ってないで、なんとか言いなさいっ！  [voice 6826]
    voice "ch26_l_004"
    l "Don't just stand there—say something!{#ch26_l_004}"

    # タバサ：……。
    t "…{#ch26_t_004}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # キュルケ：とまあ、こんな感じ。  [voice 3502]
    voice "ch26_k_006"
    k "Well, that's about it.{#ch26_k_006}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：こりゃ大変だ……。  [voice 12524]
    voice "ch26_s_012"
    s "This is bad…{#ch26_s_012}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ちょっと、サイト！
    voice "ch26_l_005"
    l "Hey, Saito! You too—say something to this stubborn Tabitha!{#ch26_l_005}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：えーっ、俺がー？  [voice 12525]
    voice "ch26_s_013"
    s "Eh, me!?{#ch26_s_013}"

    # ルイズ：ハルナはあんたのクラスメイトなんでしょ！？
    voice "ch26_l_006"
    l "Haruna is your classmate, isn't she!? If you don't put your foot down now, Tabitha will take her away!{#ch26_l_006}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：つれていかれるって……。  [voice 12526]
    voice "ch26_s_014"
    s "Take her away, you say…{#ch26_s_014}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch26_t_005}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+684, level=160, dir=1A]
    # キュルケ：頑張ってね、ダーリン。  [voice 3503]
    voice "ch26_k_007"
    k "Do your best, darling.{#ch26_k_007}"

    # サイト：この状況をどう頑張れと……。  [voice 12527]
    voice "ch26_s_015"
    s "How am I supposed to do my best in this situation…{#ch26_s_015}"

    menu:
        "Ask Tabitha to explain{#ch26_1_c_934_1}":
            jump ch26_1_scene_935
        "Calm Louise down{#ch26_1_c_934_2}":
            jump ch26_1_scene_936
        "Settle both down{#ch26_1_c_934_3}":
            jump ch26_1_scene_937

label ch26_1_scene_935:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay6     image=+684, level=160, dir=1A]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：タバサ。
    voice "ch26_s_016"
    s "Tabitha. Since we're here, won't you give us an explanation everyone can accept?{#ch26_s_016}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch26_t_006}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：頼まれたから春奈をつれてくって
    voice "ch26_s_017"
    s "Just saying you were asked to bring Haruna isn't enough, is it?{#ch26_s_017}"

    # サイト：俺達が春奈を心配してる気持ちも
    voice "ch26_s_018"
    s "Try to understand how worried we are about Haruna. And I'm worried about you, too, of course.{#ch26_s_018}"

    # タバサ：……。
    t "…{#ch26_t_007}"

    # → next scene 938
    jump ch26_1_scene_938

label ch26_1_scene_936:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay6     image=+684, level=160, dir=1A]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ルイズ、落ち着けよ。
    voice "ch26_s_019"
    s "Louise, calm down. There's a reason Tabitha's silent, isn't there?{#ch26_s_019}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：理由ってなによ？
    voice "ch26_l_007"
    l "A reason? How would you know that?{#ch26_l_007}"

    # サイト：そりゃ、だいたいの想像はつくさ。
    voice "ch26_s_020"
    s "Well, I can guess. It's probably a top-secret mission she can't tell anyone about.{#ch26_s_020}"

    # ルイズ：それでサイトは納得できるわけ？  [voice 6830]
    voice "ch26_l_008"
    l "And that's supposed to satisfy you?{#ch26_l_008}"

    # サイト：もちろん、できるはずない。
    voice "ch26_s_021"
    s "Of course not. And Tabitha must be agonizing over the mission, too.{#ch26_s_021}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そうだろ、タバサ？  [voice 12534]
    voice "ch26_s_022"
    s "Right, Tabitha?{#ch26_s_022}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch26_t_008}"

    # サイト：ルイズの気持ちもちゃんと
    voice "ch26_s_023"
    s "Please try to understand Louise's feelings, too.{#ch26_s_023}"

    # サイト：ルイズが口にしてる気持ちは、
    voice "ch26_s_024"
    s "The feelings Louise is expressing are the feelings of all of us…{#ch26_s_024}"

    # タバサ：……。
    t "…{#ch26_t_009}"

    # → next scene 938
    jump ch26_1_scene_938

label ch26_1_scene_937:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay6     image=+684, level=160, dir=1A]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：はっきり言うけど、どっちも悪いっ！  [voice 12537]
    voice "ch26_s_025"
    s "Let me be clear—both of you are at fault!{#ch26_s_025}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # ルイズ：ええーっ！？  [voice 6831]
    voice "ch26_l_009"
    l "Ehh!?{#ch26_l_009}"

    # タバサ：……。
    t "…{#ch26_t_010}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ルイズは一方的に責めすぎだし、
    voice "ch26_s_026"
    s "Louise blames too much, and Tabitha doesn't say what she should. Both are at fault.{#ch26_s_026}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：ぶー。  [voice 6832]
    voice "ch26_l_010"
    l "Hmph.{#ch26_l_010}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：でも、タバサ。
    voice "ch26_s_027"
    s "But, Tabitha. Try to understand Louise's feelings, too.{#ch26_s_027}"

    # サイト：ルイズが口にしてる気持ちは、
    voice "ch26_s_028"
    s "The feelings Louise is expressing are the feelings of all of us…{#ch26_s_028}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch26_t_011}"

    # → next scene 938
    jump ch26_1_scene_938

label ch26_1_scene_938:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なあ、タバサ。
    voice "ch26_s_029"
    s "Say, Tabitha. About Haruna being taken to Gallia—is there really no way around it?{#ch26_s_029}"

    # タバサ：それは無理。
    voice "ch26_t_012"
    t "No. It's a mission.{#ch26_t_012}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そっか……。
    voice "ch26_s_030"
    s "I see… This is bad…{#ch26_s_030}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # → next scene 939
    jump ch26_1_scene_939

label ch26_1_scene_939:

    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：うーん、どうしたもんかなぁ……。  [voice 12543]
    voice "ch26_s_031"
    s "Hmm, what should we do…{#ch26_s_031}"

    # [SE       se0      play=+82]
    # シエスタ：サイトさんっ！  [voice 15054]
    voice "ch26_si_007"
    si "Saito-san!{#ch26_si_007}"

    # [SE       se0      play=+57]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+504, level=160, dir=1B]
    # サイト：シエスタどうしたんだ？  [voice 12544]
    voice "ch26_s_032"
    s "Siesta, what's wrong?{#ch26_s_032}"

    # シエスタ：たっ、たたた、大変なんですっ！
    voice "ch26_si_008"
    si "I-It's terrible! Haruna-san has disappeared!{#ch26_si_008}"

    # サイト：え、まじ？  [voice 12545]
    voice "ch26_s_033"
    s "Eh, seriously?{#ch26_s_033}"

    # シエスタ：はい、本当です。  [voice 15056]
    voice "ch26_si_009"
    si "Yes, really.{#ch26_si_009}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：……！？  [voice 15687]
    voice "ch26_t_013"
    t "…!?{#ch26_t_013}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：なっ、なんでーっ！？  [voice 6833]
    voice "ch26_l_011"
    l "Wh-Why!?{#ch26_l_011}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：ちょっと、大変じゃないのっ！？  [voice 3504]
    voice "ch26_k_008"
    k "Hey, that's not good!{#ch26_k_008}"

    # [SPRITE   lay2     image=+506, level=160, dir=1B]
    # シエスタ：わたしがハルナさんから、目を離した隙に……。  [voice 15057]
    voice "ch26_si_010"
    si "I took my eyes off Haruna-san for a moment…{#ch26_si_010}"

    # キュルケ：あたし、探しに行ってくるわ！  [voice 3505]
    voice "ch26_k_009"
    k "I'll go look for her!{#ch26_k_009}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：俺達も春奈のこと探しに出た方が
    voice "ch26_s_034"
    s "We should search for Haruna, too.{#ch26_s_034}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そうね。
    voice "ch26_l_012"
    l "Right. Standing here arguing won't help.{#ch26_l_012}"

    # サイト：それじゃあ……。  [voice 12547]
    voice "ch26_s_035"
    s "Well then…{#ch26_s_035}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SE       se0      play=+64]
    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay15    vibrate=7]
    # [SPRITE   lay19    vibrate=7]
    # [SPRITE   lay1     vibrate=7]
    # [SPRITE   lay2     vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [SPRITE   lay6     vibrate=7]
    # [LAYER    lay0     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay15    hide, reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay1     reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay6     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：……！？  [voice 15688]
    voice "ch26_t_014"
    t "…!?{#ch26_t_014}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：どうしたの？  [voice 6835]
    voice "ch26_l_013"
    l "What's wrong?{#ch26_l_013}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+506, level=160, dir=1B]
    # シエスタ：サ、サイトさん！？  [voice 15058]
    voice "ch26_si_011"
    si "S-Saito-san!?{#ch26_si_011}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：なっ、なんだ！？
    voice "ch26_s_036"
    s "What!? Is it the bomber at a time like this!?{#ch26_s_036}"

    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay15    vibrate=14]
    # [SPRITE   lay19    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay15    hide, reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay2     reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay6     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：なっ、また！？
    voice "ch26_s_037"
    s "What!? Again!? This time it's close.{#ch26_s_037}"

    # シエスタ：サイトさん……。  [voice 15059]
    voice "ch26_si_012"
    si "Saito-san…{#ch26_si_012}"

    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay15    vibrate=14]
    # [SPRITE   lay19    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay15    hide, reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay2     reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay6     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SE       se0      play=+57]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # [SPRITE   lay15    hide]
    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：な、なにごとなの！？  [voice 6836]
    voice "ch26_l_014"
    l "What's happening!?{#ch26_l_014}"

    # 味方Ａ：おいっ、お前達！
    voice "ch26_soldier_001"
    soldier "Hey, you! This place could be caught in fighting any moment!{#ch26_soldier_001}"

    # 味方Ａ：急いで宿の外へ避難するんだ！！  [voice 4247]
    voice "ch26_soldier_002"
    soldier "Hurry—get out of the inn!{#ch26_soldier_002}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：なあ、いったい何が起こってんだよ！？  [voice 12550]
    voice "ch26_s_038"
    s "Hey, what's going on!?{#ch26_s_038}"

    # 味方Ａ：敵の正体は分からんが、
    voice "ch26_soldier_003"
    soldier "We don't know who the enemy is, but we're under attack! Run before you're hurt!{#ch26_soldier_003}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ハルナの身が心配だけど、
    voice "ch26_l_015"
    l "I'm worried about Haruna, but first let's go to the castle and get information about the bomber!{#ch26_l_015}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そうだな。
    voice "ch26_s_039"
    s "Right. Tabitha, is that all right with you?{#ch26_s_039}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：うん。  [voice 15689]
    voice "ch26_t_015"
    t "Mm.{#ch26_t_015}"

    # サイト：よし、決まりだ。
    voice "ch26_s_040"
    s "All right, it's decided. Siesta, you're coming with us, too!{#ch26_s_040}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay2     image=+500, level=160, dir=1B]
    # シエスタ：は、はいっ！  [voice 15060]
    voice "ch26_si_013"
    si "Y-Yes!{#ch26_si_013}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
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
    # [SE       se0      play=+63]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay15    vibrate=14]
    # [SPRITE   lay19    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay15    hide, reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：なんだこりゃ……。
    voice "ch26_s_041"
    s "What is this… It's just like a war…{#ch26_s_041}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay2     image=+504, level=160, dir=1B]
    # ルイズ：シエスタ。
    voice "ch26_l_016"
    l "Siesta. Don't leave our side.{#ch26_l_016}"

    # シエスタ：はいっ、ミス・ヴァリエール！  [voice 15061]
    voice "ch26_si_014"
    si "Yes, Miss Valliere!{#ch26_si_014}"

    # [SE       se0      play=+63]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [SPRITE   lay15    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay19    vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay2     reset]
    # [SPRITE   lay5     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay15    hide, reset]
    # [SPRITE   lay1     reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：止まって。  [voice 15690]
    voice "ch26_t_016"
    t "Stop.{#ch26_t_016}"

    # [LAYER    lay0     x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：急にどうしたんだよ？  [voice 12554]
    voice "ch26_s_042"
    s "Why suddenly?{#ch26_s_042}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：ひょっとして、まさか……？  [voice 6839]
    voice "ch26_l_017"
    l "Could it… no way…{#ch26_l_017}"

    # タバサ：うん。  [voice 15691]
    voice "ch26_t_017"
    t "Mm.{#ch26_t_017}"

    # [SE       se0      play=+65]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+471, level=160, dir=3B]
    # サイト：こっちは急いでるってのに！
    voice "ch26_s_043"
    s "We're in a hurry! Let's go, Derf!{#ch26_s_043}"

    # デルフリンガー：おっ、出番か相棒！  [voice 1353]
    voice "ch26_th_001"
    th "Oh, my turn, partner!{#ch26_th_001}"

    # サイト：ああ、思いっきりぶっとばしてやろうぜ！！  [voice 12556]
    voice "ch26_s_044"
    s "Yeah—let's smash them with everything we've got!{#ch26_s_044}"

    # デルフリンガー：了解したぜ、相棒。
    voice "ch26_th_002"
    th "Understood, partner. I thought I'd end up unable to speak at this rate.{#ch26_th_002}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay19    hide]
    # [BG       stage    hide]
    # → next scene 940
    jump ch26_1_scene_940

label ch26_1_scene_940:

    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [SPRITE   lay5     image=+434, level=160, dir=2B]
    # サイト：ふーっ、ようやく城に着いたぜ。  [voice 12557]
    voice "ch26_s_045"
    s "Phew—we finally made it to the castle.{#ch26_s_045}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：良かった、まだお城までは敵が
    voice "ch26_l_018"
    l "Good. It looks like the enemy hasn't reached the castle yet.{#ch26_l_018}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：爆弾使いって単独犯だと思っていたけど、
    voice "ch26_k_010"
    k "I thought the bomber worked alone, but it seems I was wrong.{#ch26_k_010}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：一体何者なのか、どんな組織かもさっぱりだよ。  [voice 12558]
    voice "ch26_s_046"
    s "Who they are—what organization—I have no idea at all.{#ch26_s_046}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：別にいいじゃない。
    voice "ch26_l_019"
    l "Who cares? Catch them and we'll know everything.{#ch26_l_019}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：まぁ、そう簡単にいけばいいんだけどな……。  [voice 12559]
    voice "ch26_s_047"
    s "Well, if only it were that easy…{#ch26_s_047}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch26_t_018}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：それじゃあ、城の中へ……。  [voice 12560]
    voice "ch26_s_048"
    s "Well then, into the castle…{#ch26_s_048}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay15    image=+1116, level=160, dir=1A]
    # 味方Ａ：おい、そこのっ！
    voice "ch26_soldier_004"
    soldier "Hey, you there! You may not enter the castle without permission!{#ch26_soldier_004}"

    # [SPRITE   lay15    level=160]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：わたし達は、ちゃんとした用があってお城へ
    voice "ch26_l_020"
    l "We've come to the castle on legitimate business.{#ch26_l_020}"

    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # 味方Ａ：ならん。
    voice "ch26_soldier_005"
    soldier "No. I cannot permit entry.{#ch26_soldier_005}"

    # 味方Ａ：許可無き人間は、誰も入れるなと命令が出てる。  [voice 4251]
    voice "ch26_soldier_006"
    soldier "I'm under orders to let nobody in without permission.{#ch26_soldier_006}"

    # ルイズ：許可できないって、わたし達は……。
    voice "ch26_l_021"
    l "You can't permit us—we're… Oh, there's no time to dawdle here!{#ch26_l_021}"

    # サイト：よし、ここはひとつ……。  [voice 12561]
    voice "ch26_s_049"
    s "All right, here's what we'll do…{#ch26_s_049}"

    menu:
        "Use force!{#ch26_1_c_940_1}":
            jump ch26_1_scene_941
        "Leave it to Louise{#ch26_1_c_940_2}":
            jump ch26_1_scene_942
        "…That's a bribe, isn't it{#ch26_1_c_940_3}":
            jump ch26_1_scene_943

label ch26_1_scene_941:

    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [SPRITE   lay15    hide]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：ルイズ、こいつら、やっちゃっていい？  [voice 12562]
    voice "ch26_s_050"
    s "Louise—can I take care of these guys?{#ch26_s_050}"

    # ルイズ：いいわけないでしょ！
    voice "ch26_l_022"
    l "Of course not! What are you saying! Honestly, you're an idiot!{#ch26_l_022}"

    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # サイト：で、ですよね。  [voice 12563]
    voice "ch26_s_051"
    s "W-Well, I thought so…{#ch26_s_051}"

    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：サイトは黙ってて。
    voice "ch26_l_023"
    l "Saito, be quiet. Leave this to me.{#ch26_l_023}"

    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：はーい。  [voice 12564]
    voice "ch26_s_052"
    s "Yes, yes.{#ch26_s_052}"

    # → next scene 944
    jump ch26_2

label ch26_1_scene_942:

    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [SPRITE   lay15    hide]
    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：ルイズ、任せた！  [voice 12565]
    voice "ch26_s_053"
    s "Louise, I'll leave it to you.{#ch26_s_053}"

    # [SPRITE   lay1     image=+308, level=155, dir=1A]
    # ルイズ：な、なによ。
    voice "ch26_l_024"
    l "Wh-What? I thought you were going to do something!{#ch26_l_024}"

    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # サイト：いや、だって、どうしていいのか分かんねーし。  [voice 12566]
    voice "ch26_s_054"
    s "Well, I mean—I don't know what to do!{#ch26_s_054}"

    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：もう。
    voice "ch26_l_025"
    l "Honestly, you're utterly useless!{#ch26_l_025}"

    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：はーい。  [voice 12567]
    voice "ch26_s_055"
    s "Yes, yes.{#ch26_s_055}"

    # → next scene 944
    jump ch26_2

label ch26_1_scene_943:

    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [SPRITE   lay15    hide]
    # [SPRITE   lay5     image=+403, level=156, dir=1B]
    # サイト：へへへ、まあまあ兵士さん、
    voice "ch26_s_056"
    s "Heh heh, come now, soldier—have something warm to eat with this.{#ch26_s_056}"

    # ルイズ：サイトっ！
    voice "ch26_l_026"
    l "Saito! What are you doing!? You can't win them over like that!{#ch26_l_026}"

    # [SPRITE   lay5     image=+436, level=156, dir=2B]
    # サイト：えー、だってさぁ。  [voice 12569]
    voice "ch26_s_057"
    s "Eh, but…{#ch26_s_057}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay15    image=+1117, level=140, dir=1A]
    # 味方Ａ：貴様達。
    voice "ch26_soldier_007"
    soldier "You there. What's your purpose? Depending on your answer, I'll arrest you.{#ch26_soldier_007}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # ルイズ：あーもう、話がややこしくなっただけじゃない！
    voice "ch26_l_027"
    l "Oh, for heaven's sake—you've only made things more complicated! Saito, be quiet!{#ch26_l_027}"

    # サイト：はーい。  [voice 12570]
    voice "ch26_s_058"
    s "Yes, yes.{#ch26_s_058}"

    # → next scene 944
    jump ch26_2

    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch26_2
    return

