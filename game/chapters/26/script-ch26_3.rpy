# Глава 26, часть 3 (сцены 955–964): Акина на крыше.
# Источник: ps2_source/chapters/chapter_27_タバサの秘密.txt (SCENE 955-964).

label ch26_3:
    $ tndl(None)
    $ show_sprites()

label ch26_3_scene_955:

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+54, level=200]
    $ fade_fx("id(54)")
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：はぁ……。
    voice "ch26_s_088"
    s "Sigh… Where on earth did Haruna go…{#ch26_s_088}"

    # サイト：もし、ガリア王国へ連れて行かれるのが
    voice "ch26_s_089"
    s "Even if she fled because she was afraid of being taken to Gallia, disappearing without telling me anything…{#ch26_s_089}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：ごめんなさい。  [voice 15695]
    voice "ch26_t_023"
    t "I'm sorry.{#ch26_t_023}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：タバサが謝る必要なんてないよ。  [voice 12600]
    voice "ch26_s_090"
    s "You don't need to apologize, Tabitha.{#ch26_s_090}"

    # タバサ：でも……。  [voice 15696]
    voice "ch26_t_024"
    t "But…{#ch26_t_024}"

    # サイト：いいって……。
    voice "ch26_s_091"
    s "It's fine… It's not your fault.{#ch26_s_091}"

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch26_t_025}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：きっと、無事でいるに決まって……。  [voice 12602]
    voice "ch26_s_092"
    s "I'm sure she's safe…{#ch26_s_092}"

    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     reset]
    # [LAYER    lay0     reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ばっ、爆発！？  [voice 12603]
    voice "ch26_s_093"
    s "Ba—an explosion!?{#ch26_s_093}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay2     image=+506, level=160, dir=1B]
    # シエスタ：キャーッ！？  [voice 15063]
    voice "ch26_si_016"
    si "Kyaa!?{#ch26_si_016}"

    # [SPRITE   lay2     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch26_t_026}"

    # サイト：大丈夫か、タバサ？
    voice "ch26_s_094"
    s "Are you all right, Tabitha? Are you hurt?{#ch26_s_094}"

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：うん、大丈夫。  [voice 15697]
    voice "ch26_t_027"
    t "Mm, I'm fine.{#ch26_t_027}"

    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     reset]
    # [LAYER    lay0     reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：ねぇ、この劇場……。
    voice "ch26_l_062"
    l "Hey—this theater… It's shaking, isn't it?{#ch26_l_062}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：ヤバそうね。
    voice "ch26_k_029"
    k "Looks bad. Everyone, get outside!{#ch26_k_029}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 956
    jump ch26_3_scene_956

label ch26_3_scene_956:

    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [SE       se0      play=+63]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay21    vibrate=14]
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
    # [SPRITE   lay21    hide, reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay6     image=+713, level=160, dir=2A]
    # キュルケ：もう、どこからの攻撃なのっ！？  [voice 3526]
    voice "ch26_k_030"
    k "Where's the attack coming from!?{#ch26_k_030}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay2     image=+504, level=160, dir=1B]
    # シエスタ：ああ！
    voice "ch26_si_017"
    si "Ah! On the roof! There's someone there!{#ch26_si_017}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：……！？  [voice 15698]
    voice "ch26_t_028"
    t "…!?{#ch26_t_028}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：どうした？  [voice 12605]
    voice "ch26_s_095"
    s "What's wrong?{#ch26_s_095}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+98, level=80]
    $ dissolve_fx("id(98)")
    # [SPRITE   lay21    x=304, y=416]
    # [SPRITE   lay19    x=304, y=416]
    # [SPRITE   lay1     x=304, y=416]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # アキナ：……。
    ak "…{#ch26_ak_001}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [EVENT_CG event    hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # サイト：まさか……あれは、春奈？
    voice "ch26_s_096"
    s "No way… That's Haruna? Why is she up there?{#ch26_s_096}"

    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+654, level=160, dir=3A]
    # タバサ：シルフィード。  [voice 15699]
    voice "ch26_t_029"
    t "Sylphid.{#ch26_t_029}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：えっ、タバサ！？
    voice "ch26_s_097"
    s "Eh, Tabitha!? You're not really going!?{#ch26_s_097}"

    # タバサ：……。
    t "…{#ch26_t_030}"

    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：待てよ、俺も行くっ！  [voice 12608]
    voice "ch26_s_098"
    s "Wait, I'm going, too!{#ch26_s_098}"

    # [SE       se0      play=+67]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：サイト！！  [voice 6885]
    voice "ch26_l_063"
    l "Saito!!{#ch26_l_063}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：大丈夫みたい。
    voice "ch26_k_031"
    k "Looks like he's fine. Darling's holding onto Sylphid safely.{#ch26_k_031}"

    # ルイズ：もう、いつもいつもいつも勝手に
    voice "ch26_l_064"
    l "Honestly—always acting on your own!{#ch26_l_064}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：あら、サイトまで来たんだ？  [voice 129]
    voice "ch26_ak_002"
    ak "Oh, so even Saito came?{#ch26_ak_002}"

    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：お前……。
    voice "ch26_s_099"
    s "You… Are you really Haruna?{#ch26_s_099}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：アッハハッ。
    voice "ch26_ak_003"
    ak "Ah ha ha. Who can say?{#ch26_ak_003}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：ねぇ、タバサ……。
    voice "ch26_ak_004"
    ak "Say, Tabitha… You're going to capture me and take me away, aren't you?{#ch26_ak_004}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+654, level=160, dir=3A]
    # タバサ：うん。
    voice "ch26_t_031"
    t "Mm. Be still.{#ch26_t_031}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：はははははっ。  [voice 132]
    voice "ch26_ak_005"
    ak "Ha ha ha ha!{#ch26_ak_005}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：あたしを捕まえられたら、
    voice "ch26_ak_006"
    ak "If you can catch me, I don't mind being taken away. Am I being too generous?{#ch26_ak_006}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：おい、春奈。
    voice "ch26_s_100"
    s "Hey, Haruna. What are you saying? If it's my fault, I'll apologize.{#ch26_s_100}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：サイトは相変わらず人がいいね。
    voice "ch26_ak_007"
    ak "Saito, you're still too kind. That's why everyone gets hurt.{#ch26_ak_007}"

    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：なっ！  [voice 12611]
    voice "ch26_s_101"
    s "Hah!{#ch26_s_101}"

    # [SPRITE   lay21    hide]
    # [LAYER    lay0     image=+654, level=160, dir=3A]
    # タバサ：……。
    t "…{#ch26_t_032}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：おい、タバサ。
    voice "ch26_s_102"
    s "Hey, Tabitha… Are you going to fight?{#ch26_s_102}"

    # タバサ：うん。  [voice 15701]
    voice "ch26_t_033"
    t "Mm.{#ch26_t_033}"

    # サイト：相手は春奈なんだぞ。  [voice 12613]
    voice "ch26_s_103"
    s "The opponent is Haruna, you know.{#ch26_s_103}"

    # タバサ：これはわたしの任務だから。  [voice 15702]
    voice "ch26_t_034"
    t "This is my mission.{#ch26_t_034}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：だからって……。  [voice 12614]
    voice "ch26_s_104"
    s "Even so…{#ch26_s_104}"

    menu:
        "I can't just stare{#ch26_3_c_956_1}":
            jump ch26_3_scene_957
        "Leaving Haruna like this?{#ch26_3_c_956_2}":
            jump ch26_3_scene_958
        "Letting you fight alone?{#ch26_3_c_956_3}":
            jump ch26_3_scene_959

label ch26_3_scene_957:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [LAYER    lay0     image=+654, level=160, dir=3A]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ボーっと見てるわけにはいかないだろ。  [voice 12615]
    voice "ch26_s_105"
    s "I can't just stand here and stare, can I?{#ch26_s_105}"

    # [LAYER    lay0     image=+660, level=160, dir=3A]
    # タバサ：でも……。  [voice 15703]
    voice "ch26_t_035"
    t "But…{#ch26_t_035}"

    # サイト：春奈を気絶させればいいんだろ？
    voice "ch26_s_106"
    s "We just need to knock Haruna out, right? I don't want either of you hurt.{#ch26_s_106}"

    # → next scene 960
    jump ch26_3_scene_960

label ch26_3_scene_958:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [LAYER    lay0     image=+654, level=160, dir=3A]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：こんな春奈を放っておけるかよ。  [voice 12617]
    voice "ch26_s_107"
    s "I can't leave Haruna like this.{#ch26_s_107}"

    # [LAYER    lay0     image=+660, level=160, dir=3A]
    # タバサ：でも……。  [voice 15704]
    voice "ch26_t_036"
    t "But…{#ch26_t_036}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：ああ、分かってる。
    voice "ch26_s_108"
    s "Ah, I know. I can feel this much killing intent…{#ch26_s_108}"

    # サイト：今、目の前にいるのは、
    voice "ch26_s_109"
    s "The one in front of me now isn't the Haruna we know.{#ch26_s_109}"

    # [LAYER    lay0     image=+654, level=160, dir=3A]
    # タバサ：うん。  [voice 15705]
    voice "ch26_t_037"
    t "Mm.{#ch26_t_037}"

    # → next scene 960
    jump ch26_3_scene_960

label ch26_3_scene_959:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [LAYER    lay0     image=+654, level=160, dir=3A]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：お前だけが戦うのを見過ごせるかよ。  [voice 12620]
    voice "ch26_s_110"
    s "I can't stand by and watch you fight alone.{#ch26_s_110}"

    # [LAYER    lay0     image=+660, level=160, dir=3A]
    # タバサ：でも……。  [voice 15706]
    voice "ch26_t_038"
    t "But…{#ch26_t_038}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：いいんだ、手伝うよ。
    voice "ch26_s_111"
    s "It's fine. I'll help you. I'll fight carefully so I don't get in your way.{#ch26_s_111}"

    # [LAYER    lay0     image=+656, level=160, dir=3A]
    # タバサ：うん……。  [voice 15707]
    voice "ch26_t_039"
    t "Mm…{#ch26_t_039}"

    # → next scene 960
    jump ch26_3_scene_960

label ch26_3_scene_960:

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [LAYER    lay0     image=+660, level=160, dir=3A]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # サイト：（それにしても……。
    s "(That aside… What on earth happened to Haruna?){#ch26_s_112}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：なあ、タバサ。
    voice "ch26_s_113"
    s "Say, Tabitha. I don't know why the Haruna in front of us became like this.{#ch26_s_113}"

    # サイト：タバサに引き渡せるかどうか、
    voice "ch26_s_114"
    s "I can't promise I'll hand her over to you. Is that all right?{#ch26_s_114}"

    # [LAYER    lay0     image=+654, level=160, dir=3A]
    # タバサ：うん。  [voice 15708]
    voice "ch26_t_040"
    t "Mm.{#ch26_t_040}"

    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：よし、それじゃあ……。
    voice "ch26_s_115"
    s "All right, then… Derf, draw!{#ch26_s_115}"

    # [SE       se0      play=+65]
    # [SPRITE   lay5     image=+467, level=148, dir=3B]
    # [SPRITE   lay5     level=148]
    # [LAYER    lay0     level=152]
    # デルフリンガー：いいぜ、相棒……。
    voice "ch26_d_001"
    d "Sure, partner… This is getting strange again, isn't it?{#ch26_d_001}"

    # サイト：春奈のことだろ？
    voice "ch26_s_116"
    s "It's about Haruna, right? Ah, don't worry. I'll hold back.{#ch26_s_116}"

    # デルフリンガー：手加減？
    voice "ch26_d_002"
    d "Hold back? What are you talking about? With that attitude, you'll lose, partner.{#ch26_d_002}"

    # [SPRITE   lay5     image=+473, level=148, dir=3B]
    # サイト：どういうことだよ？  [voice 12626]
    voice "ch26_s_117"
    s "What do you mean?{#ch26_s_117}"

    # デルフリンガー：すぐに分かるさ。
    voice "ch26_d_003"
    d "You'll see soon. My intuition is buzzing. If you want to survive, fight for real.{#ch26_d_003}"

    # サイト：くそ……。  [voice 12627]
    voice "ch26_s_118"
    s "Damn…{#ch26_s_118}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    image=+1019, level=149, dir=1A]
    # アキナ：どれ、相談は終わったかい？
    voice "ch26_ak_008"
    ak "Well, has the chat finished? Then, I'm coming!{#ch26_ak_008}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay21    hide]
    # [SPRITE   lay19    hide]
    # [BG       stage    hide]
    # → next scene 961
    jump ch26_3_scene_961

label ch26_3_scene_961:

    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：勝った……か。  [voice 12628]
    voice "ch26_s_119"
    s "We won… did we?{#ch26_s_119}"

    # タバサ：勝った……。  [voice 15709]
    voice "ch26_t_041"
    t "We won…{#ch26_t_041}"

    # サイト：でも、なんで……。
    voice "ch26_s_120"
    s "But why… Why would Haruna…{#ch26_s_120}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：違う……。  [voice 136]
    voice "ch26_ak_009"
    ak "Wrong…{#ch26_ak_009}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：……！？  [voice 15710]
    voice "ch26_t_042"
    t "…!?{#ch26_t_042}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：違うって、何がだよ？  [voice 12630]
    voice "ch26_s_121"
    s "Wrong—what's wrong?{#ch26_s_121}"

    # アキナ：あたしは……。
    voice "ch26_ak_010"
    ak "I'm… not Haruna…{#ch26_ak_010}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # サイト：春奈じゃないって……。
    voice "ch26_s_122"
    s "Not Haruna…? You look exactly like Haruna to me!{#ch26_s_122}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：アハッ、アハハ……。
    voice "ch26_ak_011"
    ak "Ah ha, ah ha ha… Then let me tell you.{#ch26_ak_011}"

    # アキナ：あたしはハルナであってハルナじゃない。  [voice 139]
    voice "ch26_ak_012"
    ak "I am Haruna and not Haruna.{#ch26_ak_012}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：な、なに言ってんだよ、春奈？  [voice 12632]
    voice "ch26_s_123"
    s "What are you saying, Haruna?{#ch26_s_123}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：あたしの名はアキナ。
    voice "ch26_ak_013"
    ak "My name is Akina. I'm a separate personality created by Weatherly-sama…{#ch26_ak_013}"

    # サイト：ウェザリー？
    voice "ch26_s_124"
    s "Weatherly? A separate personality? Where did Haruna go?{#ch26_s_124}"

    # アキナ：あたしの中で眠ってるよ。
    voice "ch26_ak_014"
    ak "She's asleep inside me. While I'm awake, Haruna is always sleeping.{#ch26_ak_014}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：う、嘘を言うな。  [voice 12634]
    voice "ch26_s_125"
    s "Don't lie!{#ch26_s_125}"

    # アキナ：嘘じゃないさ。
    voice "ch26_ak_015"
    ak "It's not a lie. You've noticed by now, haven't you? The bomber's identity.{#ch26_ak_015}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：それはあたしさ。  [voice 143]
    voice "ch26_ak_016"
    ak "It's me.{#ch26_ak_016}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：爆弾使い？
    voice "ch26_s_126"
    s "The bomber? No way…{#ch26_s_126}"

    menu:
        "Weatherly…{#ch26_3_c_961_1}":
            jump ch26_3_scene_962
        "Separate personality…{#ch26_3_c_961_2}":
            jump ch26_3_scene_963
        "The bomber's identity…{#ch26_3_c_961_3}":
            jump ch26_3_scene_964

label ch26_3_scene_962:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：ウェザリーって……。  [voice 12636]
    voice "ch26_s_127"
    s "Weatherly, you say…{#ch26_s_127}"

    # [SPRITE   lay21    hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：劇場の。  [voice 15711]
    voice "ch26_t_043"
    t "From the theater.{#ch26_t_043}"

    # サイト：そう、劇を主催していた
    voice "ch26_s_128"
    s "Right—that Weatherly who put on the play, isn't it?{#ch26_s_128}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：あっ、そういえば春奈が……。
    voice "ch26_s_129"
    s "Ah, now that I think of it—Haruna said she'd met Weatherly somewhere…{#ch26_s_129}"

    # サイト：あれは記憶が混乱していたからなのか？  [voice 12639]
    voice "ch26_s_130"
    s "Was that because her memory was confused?{#ch26_s_130}"

    # → next scene 965
    jump ch26_4

label ch26_3_scene_963:

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：別人格って……。  [voice 12640]
    voice "ch26_s_131"
    s "A separate personality, you say…{#ch26_s_131}"

    # サイト：そんな、別の人格を植えつけるような真似、
    voice "ch26_s_132"
    s "Is it really that easy to implant another personality?{#ch26_s_132}"

    # サイト：あのアキナって奴、どう見たって
    voice "ch26_s_133"
    s "This 'Akina' doesn't resemble Haruna's personality at all, does she?{#ch26_s_133}"

    # [SPRITE   lay21    hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：人の感情はそんな簡単なものではない。  [voice 15712]
    voice "ch26_t_044"
    t "Human emotions aren't that simple.{#ch26_t_044}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：そりゃそうだけど……。
    voice "ch26_s_134"
    s "I know, but—Haruna would never enjoy hurting people.{#ch26_s_134}"

    # タバサ：高度な魔法を使えば、あるいは……。  [voice 15713]
    voice "ch26_t_045"
    t "With advanced magic, perhaps…{#ch26_t_045}"

    # サイト：魔法……。  [voice 12644]
    voice "ch26_s_135"
    s "Magic…{#ch26_s_135}"

    # → next scene 965
    jump ch26_4

label ch26_3_scene_964:

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：爆弾使いの正体って……。  [voice 12645]
    voice "ch26_s_136"
    s "The bomber's identity, you say…{#ch26_s_136}"

    # サイト：春奈は爆弾使いになって喜ぶような
    voice "ch26_s_137"
    s "Haruna isn't the type to be happy about becoming a bomber…{#ch26_s_137}"

    # [SPRITE   lay21    hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：別人格。
    voice "ch26_t_046"
    t "A separate personality. That isn't Haruna.{#ch26_t_046}"

    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：くそ……。
    voice "ch26_s_138"
    s "Damn… What a terrible thing to do…{#ch26_s_138}"

    # → next scene 965
    jump ch26_4

    # ==== КОНЕЦ ЧАСТИ 3 ====
    jump ch26_4
    return

