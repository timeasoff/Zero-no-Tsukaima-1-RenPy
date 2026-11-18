# Глава 21, часть 2 (сцены 780–789): любовное смятение, кулинарный бой.
# Источник: ps2_source/chapters/chapter_22_サイトのメイド.txt (SCENE 780-789).

label ch21_2:
    $ tndl(None)
    $ show_sprites()

    # [TITLE title("サイトのメイド")]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
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
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay1     image=+372, level=160, dir=3A]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+373, level=140, dir=3A]
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
    # [SPRITE   lay5     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+526, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay2     x=224, y=0]
    # [SPRITE   lay4     image=+555, level=160, dir=1A]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
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
    # [SPRITE   lay3     hide]
    # [SPRITE   lay4     image=+559, level=160, dir=1A]
    # [SPRITE   lay2     image=+526, level=160, dir=2A]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # [SPRITE   lay4     hide]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay4     image=+570, level=160, dir=2A]
    # [SPRITE   lay3     image=+889, level=160, dir=2A]
    # [SPRITE   lay4     hide]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay2     image=+530, level=160, dir=2A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
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
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay2     image=+497, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
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
    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [LAYER    lay0     hide]
    # [SPRITE   lay4     image=+555, level=160, dir=1A]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # [SPRITE   lay4     hide]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay4     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [LAYER    lay0     hide]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # [SPRITE   lay3     image=+885, level=160, dir=2A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
label ch21_2_scene_780:

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     x=464, y=416]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：と、とにかく！
    voice "ch21_l_034"
    l "F-Forget about that! Never mind my laundry! It's about why Siesta was acting strange!{#ch21_l_034}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：なんかこう、気が付くとボーッとしてるん
    voice "ch21_s_056"
    s "Somehow, you just kind of zone out, don't you?{#ch21_s_056}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ひょっとして、俺達にも相談できないような
    voice "ch21_s_057"
    s "Could she be carrying some trouble she can't even confide in us about?{#ch21_s_057}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：だとしたらきっと、もうアレしかないわね。  [voice 3384]
    voice "ch21_k_007"
    k "If so, there's only one thing left, I'm sure.{#ch21_k_007}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：アレ？  [voice 12045]
    voice "ch21_s_058"
    s "One thing?{#ch21_s_058}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：恋よ。  [voice 3385]
    voice "ch21_k_008"
    k "Love.{#ch21_k_008}"

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：恋ーっ！？  [voice 12046]
    voice "ch21_s_059"
    s "Lo-ove!?{#ch21_s_059}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay4     image=+566, level=160, dir=2A]
    # ギーシュ：そうか、なるほどね。
    voice "ch21_g_007"
    g "Ah, of course. Love does blind people, after all…{#ch21_g_007}"

    # [SPRITE   lay4     level=152]
    # [SPRITE   lay6     image=+709, level=150, dir=2A]
    # キュルケ：そこの所どうなのよ、サイト？
    voice "ch21_k_009"
    k "So what about it, Saito? Spit it out.{#ch21_k_009}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay5     image=+394, level=157, dir=1A]
    # サイト：ちょっと待てよ。
    voice "ch21_s_060"
    s "Hold on. Why is my name coming up here!?{#ch21_s_060}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=156, dir=1A]
    # ルイズ：シエスタの恋って言ったらあんたが
    voice "ch21_l_035"
    l "If we're talking about Siesta's love, you're obviously the cause, right!{#ch21_l_035}"

    # [SPRITE   lay1     image=+339, level=156, dir=2A]
    # ルイズ：あんたが女の子に対して思わせぶりな
    voice "ch21_l_036"
    l "It's your fault for acting suggestively toward every girl you see!{#ch21_l_036}"

    # [SPRITE   lay1     image=+306, level=156, dir=1A]
    # ルイズ：そもそも、わたしの使い魔のくせに、
    voice "ch21_l_037"
    l "What's more, as my familiar, laying hands on other girls is unthinkable!!{#ch21_l_037}"

    # [SPRITE   lay5     image=+396, level=157, dir=1A]
    # サイト：落ち着けぇ！！
    voice "ch21_s_061"
    s "Calm down!! Whoa, what are you about to do, Louise!?{#ch21_s_061}"

    # ルイズ：その根性、たたき直してやるんだから！！  [voice 6577]
    voice "ch21_l_038"
    l "I'll beat that stubbornness right out of you!!{#ch21_l_038}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [SPRITE   lay4     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [SE       se0      play=+61]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [SPRITE   lay4     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # サイト：ぎゃああああああああああっ！！！  [voice 12049]
    voice "ch21_s_062"
    s "Gyaaaaaaaaaaaaaa!!{#ch21_s_062}"

    # [LAYER    lay0     image=+588, level=154, dir=1A]
    # タバサ：一時中断。  [voice 15629]
    voice "ch21_t_004"
    t "Temporary suspension.{#ch21_t_004}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # → next scene 781
    jump ch21_2_scene_781

label ch21_2_scene_781:

    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # モンモランシー：そういえば、演劇のお手伝いをしていた時から、
    voice "ch21_m_008"
    m "Now that I think about it, Siesta seemed a bit distracted even while we were helping with the play.{#ch21_m_008}"

    # [SPRITE   lay3     x=224, y=0]
    # [SPRITE   lay7     image=+984, level=160, dir=2A]
    # ハルナ：それで分かりました。
    voice "ch21_ha_003"
    ha "That explains it. Siesta was cast as Hiraga-kun's lover in the play, wasn't she?{#ch21_ha_003}"

    # ハルナ：つまり、シエスタさんは演劇を通じて、
    voice "ch21_ha_004"
    ha "So you're saying that through the play, Siesta confessed to Hiraga-kun—even if it was a role— and developed feelings for him?{#ch21_ha_004}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ちょっ……ちょっと待ってくれよ。
    voice "ch21_s_063"
    s "W-Wait a second. Is there any proof Siesta actually has feelings for me?{#ch21_s_063}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：それに、告白って言ってもあくまで
    voice "ch21_s_064"
    s "And even if she did 'confess,' that was just inside the play, right? Haruna, you're going too far.{#ch21_s_064}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：じー。  [voice 6578]
    voice "ch21_l_039"
    l "…{#ch21_l_039}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：え？  [voice 12052]
    voice "ch21_s_065"
    s "Eh?{#ch21_s_065}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：じー。  [voice 2389]
    voice "ch21_ha_005"
    ha "…{#ch21_ha_005}"

    # サイト：え？  [voice 12053]
    voice "ch21_s_066"
    s "Eh?{#ch21_s_066}"

    # [SPRITE   lay7     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：じー。  [voice 15630]
    voice "ch21_t_005"
    t "…{#ch21_t_005}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：え？  [voice 12054]
    voice "ch21_s_067"
    s "Eh?{#ch21_s_067}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：シエスタだって恋する権利はあるわ。
    voice "ch21_k_010"
    k "Siesta has the right to love someone, too. But she's got some nerve setting her sights on my darling!{#ch21_k_010}"

    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：誰があんたの恋人ですって？
    voice "ch21_l_040"
    l "Who said she's your lover? My familiar can do what she likes, but I absolutely refuse to hand her over to you, even if it kills me!{#ch21_l_040}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：あらぁ？
    voice "ch21_k_011"
    k "Oh? Could it be, Louise, that you're in love with your familiar?{#ch21_k_011}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：なっ！？
    voice "ch21_l_041"
    l "Wha—! What are you suddenly saying, Kirche! And with a commoner like Saito…!{#ch21_l_041}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：なら、別にあたしがもらってもいいじゃない。  [voice 3389]
    voice "ch21_k_012"
    k "Then I don't mind taking him myself.{#ch21_k_012}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：うー。  [voice 6581]
    voice "ch21_l_042"
    l "Ugh.{#ch21_l_042}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：ちょうどいいわ。
    voice "ch21_k_013"
    k "Perfect. Let's have a real contest over who's worthy of darling, shall we?{#ch21_k_013}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：望むところよ、キュルケ。
    voice "ch21_l_043"
    l "Gladly, Kirche. On the name of La Valliere, I will never give you Saito!{#ch21_l_043}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：おまえら、何を勝手に血走ってるんだよ？
    voice "ch21_s_068"
    s "You two, why are you getting so bloodshot over this? Hey—take a look at your faces in a mirror sometime.{#ch21_s_068}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：平賀くん、大丈夫。
    voice "ch21_ha_006"
    ha "It's all right, Hiraga-kun. Siesta can't use magic, either. I can try a little, too, can't I?{#ch21_ha_006}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：いや、春奈。
    voice "ch21_s_069"
    s "No, Haruna. Not you too.{#ch21_s_069}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # キュルケ：うふふっ、もちろんタバサも参加よね？  [voice 3391]
    voice "ch21_k_014"
    k "Heh heh, of course Tabitha's joining, too, right?{#ch21_k_014}"

    # タバサ：付き合う。  [voice 15631]
    voice "ch21_t_006"
    t "I'll join.{#ch21_t_006}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：だーかーらー、違うんだってばっ！
    voice "ch21_s_070"
    s "I keep telling you—it's not like that! Won't any of you listen to me!? Hey, are you even listening~!?{#ch21_s_070}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay4     image=+555, level=160, dir=1A]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # モンモランシー：はぁ……。
    voice "ch21_m_009"
    m "Haa… Well, do your best, then.{#ch21_m_009}"

    # [SPRITE   lay4     image=+563, level=160, dir=1A]
    # ギーシュ：まったくさ、モンモランシー。
    voice "ch21_g_008"
    g "Really, Montmorency. Let's talk about love ourselves, shall we?{#ch21_g_008}"

    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # モンモランシー：結構よ！  [voice 4107]
    voice "ch21_m_010"
    m "Not interested!{#ch21_m_010}"

    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # ギーシュ：そんな……。  [voice 1526]
    voice "ch21_g_009"
    g "You're kidding…{#ch21_g_009}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay4     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：それじゃあ、話がまとまったところで、
    voice "ch21_k_015"
    k "Well, now that that's settled, let's go declare war on Siesta, shall we? Desertion before the enemy is punishable by death!{#ch21_k_015}"

    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：望むところよ、絶対に後悔させてあげるから。  [voice 6583]
    voice "ch21_l_044"
    l "Gladly. I'll make you regret it, absolutely.{#ch21_l_044}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：その言葉、忘れないことね。
    voice "ch21_k_016"
    k "I won't forget those words. Heh heh, things are getting fun.{#ch21_k_016}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：うおおおおっ。
    voice "ch21_s_071"
    s "Whoaaa! Someone, listen to me~!!{#ch21_s_071}"

    menu:
        "What are you planning, Kirche?{#ch21_2_c_781_1}":
            jump ch21_2_scene_782
        "Calm down, Louise{#ch21_2_c_781_2}":
            jump ch21_2_scene_783
        "Help me, Tabitha{#ch21_2_c_781_3}":
            jump ch21_2_scene_784

label ch21_2_scene_782:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # サイト：いったい何をするつもりなんだよ、キュルケ？  [voice 12059]
    voice "ch21_s_072"
    s "Just what do you intend to do, Kirche?{#ch21_s_072}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ルイズのメイドとして働くようになってから、
    voice "ch21_s_073"
    s "Ever since she started working as Louise's maid, she's finally been doing better. Leave Siesta alone.{#ch21_s_073}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：そうねぇ……ダーリンが、
    voice "ch21_k_017"
    k "Hmm… I might consider it, if darling agrees to live with me from now on, forever?{#ch21_k_017}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そ、そんなぁ！！
    voice "ch21_s_074"
    s "T-That's…! If we did that…{#ch21_s_074}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：あら、安心なさい。
    voice "ch21_l_045"
    l "Oh, don't worry. I've reserved the empty lot behind the academy building as your eternal resting place.{#ch21_l_045}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # → next scene 785
    jump ch21_2_scene_785

label ch21_2_scene_783:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ちょっと落ち着いてくれよ、ルイズ。
    voice "ch21_s_075"
    s "Just calm down a little, Louise. Siesta is serving you and trying to start over, isn't she?{#ch21_s_075}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：シエスタのことなんていいのよ！  [voice 6585]
    voice "ch21_l_046"
    l "I don't care about Siesta!{#ch21_l_046}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：え。  [voice 12063]
    voice "ch21_s_076"
    s "Eh.{#ch21_s_076}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：ツェルプストー家からふっかけてきたのよ？
    voice "ch21_l_047"
    l "Zerbst picked a fight with us, didn't she? I have to answer with victory!{#ch21_l_047}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そんなぁ、別に気にすることはないじゃないか。  [voice 12064]
    voice "ch21_s_077"
    s "Come on, it's not like you have to take it that seriously…{#ch21_s_077}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # → next scene 785
    jump ch21_2_scene_785

label ch21_2_scene_784:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：お願いだ、タバサっ！
    voice "ch21_s_078"
    s "Please, Tabitha! Help me talk some sense into them!{#ch21_s_078}"

    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # タバサ：意気地無し。  [voice 15632]
    voice "ch21_t_007"
    t "Coward.{#ch21_t_007}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ううっ、そんなぁ……。  [voice 12066]
    voice "ch21_s_079"
    s "Oof… That's cold…{#ch21_s_079}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # → next scene 785
    jump ch21_2_scene_785

label ch21_2_scene_785:

    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：（こいつはきっとしばらくの間、
    s "(Looks like this is going to get really ugly over Siesta for a while.){#ch21_s_080}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 786
    jump ch21_2_scene_786

label ch21_2_scene_786:

    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：シエスタっ。
    voice "ch21_l_048"
    l "Siesta. I'm back.{#ch21_l_048}"

    # [SE       se0      play=+57]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：あっ、おかえりなさい。  [voice 14848]
    voice "ch21_si_037"
    si "Ah, welcome back.{#ch21_si_037}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あれ……。
    voice "ch21_si_038"
    si "Eh…? Are you all here, too? What happened?{#ch21_si_038}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あなたに用があるの。  [voice 3395]
    voice "ch21_k_018"
    k "We have business with you.{#ch21_k_018}"

    # シエスタ：はい、何のご用でしょうか？  [voice 14850]
    voice "ch21_si_039"
    si "Yes? What business would that be?{#ch21_si_039}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：ふふっ、シエスタ？
    voice "ch21_k_019"
    k "Heh heh, Siesta? Bet Saito against us and fight us fair and square!{#ch21_k_019}"

    # [SPRITE   lay2     image=+526, level=160, dir=2A]
    # シエスタ：はいっ！？
    voice "ch21_si_040"
    si "Y-Yes!? Um, what do you mean by that?{#ch21_si_040}"

    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # シエスタ：わたくし、何か失礼なことでも……？
    voice "ch21_si_041"
    si "Have I done something rude…? I-I'm just a village girl… I can't fight all of you…{#ch21_si_041}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：大丈夫ですよ、シエスタさん。
    voice "ch21_ha_007"
    ha "It's fine, Siesta. It's a fight between girls, after all.{#ch21_ha_007}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：女の子の戦い……。  [voice 14853]
    voice "ch21_si_042"
    si "A fight between girls…{#ch21_si_042}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：どういうわけか、ここにいるみんなが、
    voice "ch21_s_081"
    s "For some reason, everyone here wants to bet me and compete with Siesta…{#ch21_s_081}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：俺は止めたんだけど……。  [voice 12068]
    voice "ch21_s_082"
    s "I tried to stop them, but…{#ch21_s_082}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：そ、そうなんですか……。  [voice 14854]
    voice "ch21_si_043"
    si "I-I see…{#ch21_si_043}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # シエスタ：分かりました。
    voice "ch21_si_044"
    si "All right. If it's over Saito-san, I'll accept that fight.{#ch21_si_044}"

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：これに勝てば、堂々とサイトさんと
    voice "ch21_si_045"
    si "If I win this, I can openly flirt with Saito-san, right!{#ch21_si_045}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：どうして、そうなるのさ！  [voice 12069]
    voice "ch21_s_083"
    s "Why would it mean that!?{#ch21_s_083}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：それで、肝心の勝負の内容は、何にするの？  [voice 6588]
    voice "ch21_l_049"
    l "So, what's the contest going to be? The important part.{#ch21_l_049}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：いや、おまえら淡々と事を進めるなよ。  [voice 12070]
    voice "ch21_s_084"
    s "No, would you all stop calmly steamrolling ahead with this!{#ch21_s_084}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：うーんと、そうねぇ。
    voice "ch21_k_020"
    k "Hmm, let me think… Something Siesta could do even without magic…{#ch21_k_020}"

    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：わたしにできることなんて、
    voice "ch21_si_046"
    si "All I can do is maid work. Cooking and such…{#ch21_si_046}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：あら、それいいじゃない？  [voice 3398]
    voice "ch21_k_021"
    k "Oh, that's perfect, isn't it?{#ch21_k_021}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：え？  [voice 14858]
    voice "ch21_si_047"
    si "Eh?{#ch21_si_047}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：決めたわ、勝負は自慢の料理対決よっ！  [voice 3399]
    voice "ch21_k_022"
    k "It's decided! The contest is a cooking battle of our proudest dishes!{#ch21_k_022}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay7     image=+986, level=160, dir=2A]
    # ルイズ：なんですってぇ？  [voice 6589]
    voice "ch21_l_050"
    l "What was that!?{#ch21_l_050}"

    # ハルナ：それなら私でも何とかできそうです。  [voice 2392]
    voice "ch21_ha_008"
    ha "Then I might be able to manage something, too.{#ch21_ha_008}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # サイト：料理対決って……キュルケ、本気かよっ！  [voice 12071]
    voice "ch21_s_085"
    s "A cooking battle… Kirche, are you serious!?{#ch21_s_085}"

    # キュルケ：もちろん……あたしに二言はないから。  [voice 3400]
    voice "ch21_k_023"
    k "Of course… I never go back on my word.{#ch21_k_023}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：悪くない。  [voice 15633]
    voice "ch21_t_008"
    t "Not bad.{#ch21_t_008}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：料理対決ねえ……。  [voice 12072]
    voice "ch21_s_086"
    s "A cooking battle, huh…{#ch21_s_086}"

    menu:
        "Does stomach medicine exist here?{#ch21_2_c_786_1}":
            jump ch21_2_scene_787
        "It's Siesta's specialty{#ch21_2_c_786_2}":
            jump ch21_2_scene_788
        "I'd rather judge swimsuits{#ch21_2_c_786_3}":
            jump ch21_2_scene_789

label ch21_2_scene_787:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：なあ、ルイズ。
    voice "ch21_s_087"
    s "Say, Louise. Does a stomach medicine exist in this world?{#ch21_s_087}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：イチョウヤク？
    voice "ch21_l_051"
    l "Icho-yaku? What's that?{#ch21_l_051}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：ああ、変なモノ食ったり、食べ過ぎたりして
    voice "ch21_s_088"
    s "Ah, it's medicine you take when your stomach's off from eating something strange or too much.{#ch21_s_088}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：変なモノ？
    voice "ch21_l_052"
    l "Something strange? Are you saying the food I cook is strange!?{#ch21_l_052}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：い、いや、そういう意味じゃなくてっ！  [voice 12075]
    voice "ch21_s_089"
    s "N-No, I didn't mean it that way!{#ch21_s_089}"

    # → next scene 790
    jump ch21_3

label ch21_2_scene_788:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：料理対決なら、シエスタの得意分野だな！  [voice 12076]
    voice "ch21_s_090"
    s "If it's a cooking battle, Siesta's specialty, huh!{#ch21_s_090}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：はいっ！
    voice "ch21_si_048"
    si "Yes! I help cook everyone's meals every day, so I'm a little confident!{#ch21_si_048}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：ふふっ、それでこそ張り合いがあるってものよ。
    voice "ch21_k_024"
    k "Heh heh, that's what makes it worth it. I'll show you what I can do, so be ready!{#ch21_k_024}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：わ、わたしだってタダじゃ済ませないんだから！  [voice 6592]
    voice "ch21_l_053"
    l "I-I won't let you win for free, either!{#ch21_l_053}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：それって、どういう意味ですか？  [voice 12077]
    voice "ch21_s_091"
    s "And what does that mean?{#ch21_s_091}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：くすっ……。
    voice "ch21_ha_009"
    ha "Hehe… Maybe I'll look for a dish that'll surprise Hiraga-kun, too?{#ch21_ha_009}"

    # [SPRITE   lay7     x=224, y=0]
    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：なんだか、とってもやる気が出てきましたっ！
    voice "ch21_si_049"
    si "I'm getting so motivated! Please look forward to it, Saito-san!!{#ch21_si_049}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：ああ、頑張れよシエスタっ！！  [voice 12078]
    voice "ch21_s_092"
    s "Ah, do your best, Siesta!!{#ch21_s_092}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：くすっ……はいっ！  [voice 14861]
    voice "ch21_si_050"
    si "Hehe… Yes!{#ch21_si_050}"

    # → next scene 790
    jump ch21_3

label ch21_2_scene_789:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：却下だ！
    voice "ch21_s_093"
    s "Overruled! I choose the swimsuit contest! I'm sure everyone agrees with me!{#ch21_s_093}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：……。  [voice 6593]
    voice "ch21_l_054"
    l "…{#ch21_l_054}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     image=+955, level=160, dir=1A]
    # ハルナ：ちょっと、なんで水着が出てくるわけ？  [voice 2394]
    voice "ch21_ha_010"
    ha "Hey, why did swimsuits come into this?{#ch21_ha_010}"

    # [SPRITE   lay7     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：最低。  [voice 15634]
    voice "ch21_t_009"
    t "The worst.{#ch21_t_009}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：すいません、ボクが調子こいてました。
    voice "ch21_s_094"
    s "Sorry, I got carried away. Forgive me.{#ch21_s_094}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：そんなに見たいなら、
    voice "ch21_k_025"
    k "If you want to see that badly, come to my room later.{#ch21_k_025}"

    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：いろいろ見せてあげるわ。
    voice "ch21_k_026"
    k "I'll show you all sorts of things. Not just swimsuits, either.{#ch21_k_026}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：いろいろですか！
    voice "ch21_s_095"
    s "All sorts! What do you mean, all sorts!?{#ch21_s_095}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：サイト……。
    voice "ch21_l_055"
    l "Saito… Which would you prefer, the whip or the collar?{#ch21_l_055}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：いえ、ごめんなさい。
    voice "ch21_s_096"
    s "No, thank you. I'll pass.{#ch21_s_096}"

    # → next scene 790
    jump ch21_3

    # ==== КОНЕЦ ЧАСТИ 2 ====
    jump ch21_3
    return

