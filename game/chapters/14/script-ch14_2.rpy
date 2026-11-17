# Глава 14, часть 2 (сцены 1485–1488): поиски Уэзерби по маршрутам.
# Источник: ps2_source/chapters/chapter_15_私のお兄ちゃん.txt (SCENE 1485-1488).

label ch14_2:
    $ tndl(None)
    $ show_sprites()

label ch14_2_scene_1485:

    # [BG       stage    image=+64, level=200]
    $ fade_fx("id(64)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：……。  [voice 10150]
    voice "ch14_s_061"
    s "…{#ch14_s_061}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：う～ん、
    voice "ch14_k_051"
    k "Mm, Weatherly isn't here either.{#ch14_k_051}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：まあ、俺達の推理がホントなら、
    voice "ch14_s_062"
    s "Well, if our deduction is right, she shouldn't be here anyway.{#ch14_s_062}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：そうかしら？
    voice "ch14_k_052"
    k "You think so? The castle must be part of the final objective. She might be keeping watch.{#ch14_k_052}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：どんなことを企んでるのか、分からないしね。  [voice 3075]
    voice "ch14_k_053"
    k "We don't know what she's planning.{#ch14_k_053}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：そ、そうだよな……。  [voice 10152]
    voice "ch14_s_063"
    s "Y-Yes, I guess…{#ch14_s_063}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
label ch14_2_scene_1486:

    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SE       se1      play=+37]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ここには、ウェザリーはいないみたい……。  [voice 3076]
    voice "ch14_k_054"
    k "Weatherly isn't here either…{#ch14_k_054}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：ああ、そうだな。  [voice 10153]
    voice "ch14_s_064"
    s "Yeah, I suppose.{#ch14_s_064}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：見てみてダーリン。
    voice "ch14_k_055"
    k "Look, darling. This place is full of couples.{#ch14_k_055}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：げっ。
    voice "ch14_s_065"
    s "Ugh. It is a good atmosphere, though.{#ch14_s_065}"

    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：ダーリン。
    voice "ch14_k_056"
    k "Darling, shall we declare our love here too?{#ch14_k_056}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：キュルケ、今はそういう場合じゃないだろ？  [voice 10155]
    voice "ch14_s_066"
    s "Kirche, this isn't the time for that.{#ch14_s_066}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あら、そう？
    voice "ch14_k_057"
    k "Oh, is that so? Too bad. Let's do it another time.{#ch14_k_057}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：ほっ……。  [voice 10156]
    voice "ch14_s_067"
    s "Phew…{#ch14_s_067}"

    # [SE       se1      stop=1]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
label ch14_2_scene_1487:

    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ここには、いないみたいね。  [voice 3080]
    voice "ch14_k_058"
    k "She's not here either.{#ch14_k_058}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：しかし、トリスタニアはホントにそこら中が
    voice "ch14_s_068"
    s "Tristain really is under construction everywhere.{#ch14_s_068}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：爆弾使いが破壊しまくってるからね。
    voice "ch14_k_059"
    k "Because the bomb-thrower keeps destroying things. The locals have it rough.{#ch14_k_059}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：それに、職人やら何やらで外国から人も
    voice "ch14_k_060"
    k "And there are more foreigners—craftsmen and such.{#ch14_k_060}"

    # キュルケ：当然、人の出入りが盛んになってるから
    voice "ch14_k_061"
    k "Naturally, with people coming and going, public order gets worse, they say.{#ch14_k_061}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：なるほど。
    voice "ch14_s_069"
    s "I see. Even thinking about it, we need to settle this soon.{#ch14_s_069}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：そうね……。  [voice 3084]
    voice "ch14_k_062"
    k "Yeah…{#ch14_k_062}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
label ch14_2_scene_1488:

    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：ここに、ウェザリーさんはいないか……。  [voice 10159]
    voice "ch14_s_070"
    s "Weatherly isn't here, is she…{#ch14_s_070}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：みたいね。  [voice 3085]
    voice "ch14_k_063"
    k "Looks like it.{#ch14_k_063}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：そういえば今日はキュルケの使い魔……。
    voice "ch14_s_071"
    s "By the way, today it's Kirche's familiar… er…{#ch14_s_071}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：フレイムのこと？  [voice 3086]
    voice "ch14_k_064"
    k "Flame?{#ch14_k_064}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：そう、それ。
    voice "ch14_s_072"
    s "Right, that. Where did Flame go?{#ch14_s_072}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あの子は学院にお留守番よ。
    voice "ch14_k_065"
    k "She's minding the academy. She'd stand out too much in the capital.{#ch14_k_065}"

    # キュルケ：まあ、何かあったらすぐに連れてくるけどね。  [voice 3088]
    voice "ch14_k_066"
    k "Well, if anything happens, I'll bring her right away.{#ch14_k_066}"

    # サイト：そっか……。  [voice 10162]
    voice "ch14_s_073"
    s "I see…{#ch14_s_073}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：そうね。
    voice "ch14_k_067"
    k "Yeah. She might be a little angry, actually.{#ch14_k_067}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：……えっ？  [voice 10163]
    voice "ch14_s_074"
    s "…Eh?{#ch14_s_074}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あたしを独り占めしてるって、
    voice "ch14_k_068"
    k "She might be mad that you're keeping me all to yourself.{#ch14_k_068}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：ぱくっ……ってされないように
    voice "ch14_k_069"
    k "Watch out she doesn't take a bite out of you.{#ch14_k_069}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ぱくっ？
    voice "ch14_s_075"
    s "Bite? W-What is that supposed to mean!?{#ch14_s_075}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ダーリン、次の場所にいってみましょう。
    voice "ch14_k_070"
    k "Come on, darling. Let's try the next place. Next!{#ch14_k_070}"

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
    # ==== КОНЕЦ ЧАСТИ 2 ====
    jump ch14_3
    return

