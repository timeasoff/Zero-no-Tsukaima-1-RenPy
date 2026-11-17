# Глава 18, часть 3 (сцены 714–723): прорыв к Zero Fighter.
# Источник: ps2_source/chapters/chapter_19_貴族の意地.txt (SCENE 714-723).

label ch18_3:
    $ tndl(None)
    $ show_sprites()

label ch18_3_scene_714:

    # [LAYER    lay0     image=+588, level=154, dir=1A]
    # [SPRITE   lay6     image=+676, level=153, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：わ、分かった。
    voice "ch18_s_163"
    s "R-Right! I'll come back to help right away!{#ch18_s_163}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+339, level=155, dir=2A]
    # ルイズ：さあ、そうと決まったら急ぐわよ、サイト！  [voice 6374]
    voice "ch18_l_113"
    l "Now that it's settled, let's hurry, Saito!{#ch18_l_113}"

    # → next scene 717
    jump ch18_3_scene_717

label ch18_3_scene_715:

    # [LAYER    lay0     image=+588, level=154, dir=1A]
    # [SPRITE   lay6     image=+676, level=153, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+407, level=156, dir=1B]
    # サイト：キュルケ、タバサ……。
    voice "ch18_s_164"
    s "Kirche, Tabitha… But I…{#ch18_s_164}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：あーもう。
    voice "ch18_l_114"
    l "Ugh, enough! Go, Saito!!{#ch18_l_114}"

    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # サイト：ちょっと待てよ。
    voice "ch18_s_165"
    s "Wait a moment. Louise…!{#ch18_s_165}"

    # → next scene 717
    jump ch18_3_scene_717

label ch18_3_scene_716:

    # [LAYER    lay0     image=+588, level=154, dir=1A]
    # [SPRITE   lay6     image=+676, level=153, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：お、俺もここに残って戦う！  [voice 11844]
    voice "ch18_s_166"
    s "I'll stay here and fight too!{#ch18_s_166}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：な、なに言ってんのよサイト！
    voice "ch18_l_115"
    l "What are you saying, Saito! Do you understand what Kirche meant? Let's go!{#ch18_l_115}"

    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # サイト：ちょっと待てよ。
    voice "ch18_s_167"
    s "Wait a moment. Louise…!{#ch18_s_167}"

    # → next scene 717
    jump ch18_3_scene_717

label ch18_3_scene_717:

    # [SPRITE   lay1     image=+339, level=155, dir=2A]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [SPRITE   lay1     image=+339, level=155, dir=2A]
    # ルイズ：キュルケ！
    voice "ch18_l_116"
    l "Kirche! I'll definitely repay this debt!{#ch18_l_116}"

    # ルイズ：それまでレコン・キスタなんかに
    voice "ch18_l_117"
    l "Until then, don't let Reconquista beat you!{#ch18_l_117}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=154, dir=1A]
    # [SPRITE   lay6     image=+711, level=153, dir=2A]
    # キュルケ：縁起でもない……。
    voice "ch18_k_033"
    k "Don't say such things… The slight-fever and snow-gale combo is invincible. Right, Tabitha?{#ch18_k_033}"

    # [LAYER    lay0     image=+590, level=154, dir=1A]
    # タバサ：……。
    t "…{#ch18_t_023}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+339, level=155, dir=2A]
    # [SPRITE   lay5     image=+407, level=156, dir=1B]
    # ルイズ：そ、それじゃまかせたからね！
    voice "ch18_l_118"
    l "T-Then I'm counting on you! Let's go, Saito!!{#ch18_l_118}"

    # サイト：おい、ルイズ。
    voice "ch18_s_168"
    s "Hey, Louise. Are Kirche and Tabitha really going to be okay?{#ch18_s_168}"

    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：あの２人は敵へのおとり役を引き受けて
    voice "ch18_l_119"
    l "They volunteered as decoys for the enemy! And you still want to go back?{#ch18_l_119}"

    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # サイト：……。  [voice 11847]
    voice "ch18_s_169"
    s "…{#ch18_s_169}"

    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：行くわよ、サイト。
    voice "ch18_l_120"
    l "Let's go, Saito. If you feel sorry toward Kirche and the others…{#ch18_l_120}"

    # ルイズ：一刻も早く、あんたのゼロ戦で
    voice "ch18_l_121"
    l "Then reach Tristain in your Zero Fighter as fast as you can.{#ch18_l_121}"

    # サイト：あ、あぁ……。  [voice 11848]
    voice "ch18_s_170"
    s "O-Okay…{#ch18_s_170}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 718
    jump ch18_3_scene_718

label ch18_3_scene_718:

    # [EVENT_CG event    image=+159, level=80]
    $ dissolve_fx("id(159)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # サイト：あちゃあ……。  [voice 11849]
    voice "ch18_s_171"
    s "Oh boy…{#ch18_s_171}"

    # ルイズ：予想できていたこととはいえ、
    voice "ch18_l_122"
    l "Even though we expected it… so many soldiers…{#ch18_l_122}"

    # サイト：（ゼロ戦のある広場にたどりついた俺とルイズが
    s "(What Louise and I saw when we reached the plaza with the Zero Fighter…){#ch18_s_172}"

    # サイト：（１０人近いレコン・キスタ兵に囲まれた
    s "(The Zero Fighter surrounded by nearly ten Reconquista soldiers.){#ch18_s_173}"

    # デルフリンガー：どうする相棒？  [voice 1324]
    voice "ch18_d_023"
    d "What'll you do, partner?{#ch18_d_023}"

    # デルフリンガー：これだけ倒すのはちょいと骨だが、
    voice "ch18_d_024"
    d "Taking on this many is a bit of a chore, but if we dawdle, more may come.{#ch18_d_024}"

    menu:
        "Fine, let's clear them out fast!{#ch18_3_c_718_1}":
            jump ch18_3_scene_719
        "No, wait, don't rush{#ch18_3_c_718_2}":
            jump ch18_3_scene_720
        "What do you think, Louise?{#ch18_3_c_718_3}":
            jump ch18_3_scene_721

label ch18_3_scene_719:

    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [EVENT_CG event    image=+159, level=80]
    $ dissolve_fx("id(159)")
    # サイト：よし、さっさと片付けるぞ！  [voice 11850]
    voice "ch18_s_174"
    s "Fine, let's clear them out fast!{#ch18_s_174}"

    # ルイズ：そのとおりね。
    voice "ch18_l_123"
    l "Exactly. Now, let's go…{#ch18_l_123}"

    # → next scene 722
    jump ch18_3_scene_722

label ch18_3_scene_720:

    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [EVENT_CG event    image=+159, level=80]
    $ dissolve_fx("id(159)")
    # サイト：いやまて、焦るな。  [voice 11851]
    voice "ch18_s_175"
    s "No, wait, don't rush.{#ch18_s_175}"

    # ルイズ：別に誰も焦ってなんかいないでしょ。
    voice "ch18_l_124"
    l "Nobody's rushing. If more enemies come, we'll be in real trouble.{#ch18_l_124}"

    # ルイズ：さっさと片付けるわよ……いい？  [voice 6386]
    voice "ch18_l_125"
    l "Let's take care of them quickly… okay?{#ch18_l_125}"

    # → next scene 722
    jump ch18_3_scene_722

label ch18_3_scene_721:

    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [EVENT_CG event    image=+159, level=80]
    $ dissolve_fx("id(159)")
    # サイト：ルイズはどう思う？  [voice 11852]
    voice "ch18_s_176"
    s "What do you think, Louise?{#ch18_s_176}"

    # ルイズ：わたしもデルフリンガーと同意見ね。
    voice "ch18_l_126"
    l "I agree with Derflinger. Since they haven't noticed us yet, we'll have fewer to fight.{#ch18_l_126}"

    # → next scene 722
    jump ch18_3_scene_722

label ch18_3_scene_722:

    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [EVENT_CG event    image=+159, level=80]
    $ dissolve_fx("id(159)")
    # サイト：そうだな。
    voice "ch18_s_177"
    s "Right. Okay…{#ch18_s_177}"

    # [SE       se0      play=+75]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # ルイズ：もう、バカサイト！  [voice 6388]
    voice "ch18_l_127"
    l "Honestly, you stupid Saito!{#ch18_l_127}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay14    image=+1111, level=160, dir=1A]
    # 兵士ＭＳ：誰だ、そこにいるのは誰だ！  [voice 4236]
    voice "ch18_soldier_011"
    soldier "Who's there! Who is it!?{#ch18_soldier_011}"

    # [SPRITE   lay14    hide]
    # [SE       se0      play=+65]
    # [SPRITE   lay5     image=+471, level=160, dir=3B]
    # サイト：行くぞ！
    voice "ch18_s_178"
    s "Let's go! Derf!{#ch18_s_178}"

    # デルフリンガー：やれやれ、行くとしますか。  [voice 1326]
    voice "ch18_d_025"
    d "Well, here we go.{#ch18_d_025}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay19    hide]
    # [BG       stage    hide]
    # → next scene 723
    jump ch18_3_scene_723

label ch18_3_scene_723:

    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # ルイズ：なんとかなった、わね。  [voice 6389]
    voice "ch18_l_128"
    l "We managed, didn't we.{#ch18_l_128}"

    # サイト：ゼロ戦を守りながら戦うってのは、
    voice "ch18_s_179"
    s "Fighting while protecting the Zero Fighter… takes some care.{#ch18_s_179}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：で、肝心のこれは飛ばせそうなの？  [voice 6390]
    voice "ch18_l_129"
    l "So, will this thing fly?{#ch18_l_129}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：ちょっと待てよ。
    voice "ch18_s_180"
    s "Wait a second. Let me see… No good. The instruments are fine, the flaps are fine, but…{#ch18_s_180}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：動かすために必要なガソリンが足りない。  [voice 11857]
    voice "ch18_s_181"
    s "We're short on gasoline.{#ch18_s_181}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：がそりん？  [voice 6391]
    voice "ch18_l_130"
    l "Gaso-what?{#ch18_l_130}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：あー、ガソリンっていうのは魔法で言うところの
    voice "ch18_s_182"
    s "Gasoline is like magic power for magic. Without it, the Zero Fighter won't fly.{#ch18_s_182}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：つまり、これは役に立たないってことなのね？  [voice 6392]
    voice "ch18_l_131"
    l "So it's useless, then?{#ch18_l_131}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：コルベール先生のところに行けば、予備の
    voice "ch18_s_183"
    s "Colbert-sen might have a spare, but to get there we'd have to cut through the school building…{#ch18_s_183}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：それ以前に、ミスタ・コルベールが研究室に
    voice "ch18_l_132"
    l "And if Mr. Colbert isn't in the lab, we can't get in… Too risky.{#ch18_l_132}"

    menu:
        "Let's go to the lab{#ch18_3_c_723_1}":
            jump ch18_4
        "Maybe we should retreat for now{#ch18_3_c_723_2}":
            jump ch18_4
        "Let's think{#ch18_3_c_723_3}":
            jump ch18_4

    # ==== КОНЕЦ ЧАСТИ 3 ====
    jump ch18_4
    return

