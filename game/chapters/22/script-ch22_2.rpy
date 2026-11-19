# Глава 22, часть 2 (сцены 817–823): осмотр готовки, напиток Кирке.
# Источник: ps2_source/chapters/chapter_23_料理の鉄人.txt (SCENE 817-823).

label ch22_2:
    $ tndl(None)
    $ show_sprites(None)

    # [TITLE title("料理の鉄人")]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1163, level=200]
    $ fade_fx("id(1163)")
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
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+215, level=80]
    $ dissolve_fx("id(215)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [SE       se0      play=+69]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [EVENT_CG event    image=+216, level=80]
    $ dissolve_fx("id(216)")
    # [TRANS trans("crossfade", 1000)]
    # [EVENT_CG event    image=+215, level=80]
    $ dissolve_fx("id(215)")
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # [SE       se0      play=+67]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+330, level=160, dir=1C]
    # [SPRITE   lay5     image=+414, level=160, dir=1C]
    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+445, level=160, dir=2C]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay2     x=224, y=0]
    # [SPRITE   lay1     image=+330, level=160, dir=1C]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+414, level=160, dir=1C]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+328, level=160, dir=1C]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+445, level=160, dir=2C]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+328, level=160, dir=1C]
    # [SPRITE   lay5     image=+414, level=160, dir=1C]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # [SPRITE   lay1     image=+330, level=160, dir=1C]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+329, level=140, dir=1C]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay1     hide, reset]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SE       se0      play=+57]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+712, level=140, dir=2A]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SE       se1      play=+39]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # [SPRITE   lay10    x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay10    hide]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay9     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [SPRITE   lay6     x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SE       se1      stop=1]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [LAYER    lay0     hide]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # [SPRITE   lay10    hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     x=64, y=0]
    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay10    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay9     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [SPRITE   lay4     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay10    hide, reset]
    # [SPRITE   lay3     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay9     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     x=64, y=0]
    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [SPRITE   lay4     vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [SPRITE   lay10    vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay9     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay10    hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay9     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     x=144, y=416]
    # [SPRITE   lay4     image=+555, level=160, dir=1A]
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # [SPRITE   lay4     hide]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # [SPRITE   lay10    x=224, y=0]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay10    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
label ch22_2_scene_817:

    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：調理が始まってしばらく経ったけど、
    voice "ch22_s_035"
    s "A while has passed since cooking began, but everyone's serious. Let me go take a look.{#ch22_s_035}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+32, level=200]
    $ fade_fx("id(32)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：まずはキュルケか。
    voice "ch22_s_036"
    s "Kirche first. Gah! What's that!?{#ch22_s_036}"

    # サイト：（キュルケは、黒光りした生き物から
    s "(Kirche is squeezing the meat out of some glossy black creature, extracting a purple, thick liquid.){#ch22_s_037}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（見た目すごいけど……あれ食えるのか？
    s "(It looks awful… Can you even eat that? Wait—am I the one eating it?){#ch22_s_038}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ふんふんふん……。  [voice 3418]
    voice "ch22_k_013"
    k "Hum hum hum…{#ch22_k_013}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：きゅ、キュルケさん？  [voice 12156]
    voice "ch22_s_039"
    s "K-Kirche-san?{#ch22_s_039}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：あら、ダーリン。
    voice "ch22_k_014"
    k "Oh, darling. Couldn't wait? Heh, just a little longer.{#ch22_k_014}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：今、一生忘れられないような
    voice "ch22_k_015"
    k "I'll feed you something delicious you'll never forget.{#ch22_k_015}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：い、いや、それは楽しみにしてるんだけどさ、
    voice "ch22_s_040"
    s "N-No, I'm looking forward to it, but… that purple liquid… what is it?{#ch22_s_040}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：それは秘密よ。
    voice "ch22_k_016"
    k "It's a secret. More secrets make things more fun, don't they? Both cooking and… men and women, right?{#ch22_k_016}"

    # サイト：（おいおい、がぜん不安になってきたぞ……）
    s "(Whoa, I'm getting worried now…){#ch22_s_041}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+32, level=200]
    $ fade_fx("id(32)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：（次は、ルイズだ）
    s "(Next is Louise.){#ch22_s_042}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：おりゃー！
    voice "ch22_l_022"
    l "Hi-yah! Ta-yah! Toooh!{#ch22_l_022}"

    # [SE       se0      play=+85]
    # [SE       se0      play=+88]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay10    vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay9     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay10    hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay9     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay1     reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：おわあああっ！  [voice 12158]
    voice "ch22_s_043"
    s "Whoa!{#ch22_s_043}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：あら？
    voice "ch22_l_023"
    l "Huh? I seems I sent the knife flying somewhere.{#ch22_l_023}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そ、その包丁なら、ボクの首筋をかすめて、
    voice "ch22_s_044"
    s "T-That knife grazed my neck and is stuck in the pillar over there…!{#ch22_s_044}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：あら、サイト。
    voice "ch22_l_024"
    l "Oh, Saito. What's wrong?{#ch22_l_024}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：どーしたのじゃねーよ！
    voice "ch22_s_045"
    s "What do you mean 'what's wrong'!? Swinging a knife around is dangerous! I nearly got stabbed!{#ch22_s_045}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：う、うるさいわね。
    voice "ch22_l_025"
    l "S-Shut up. As long as the ingredients are cut properly, it's fine. See?{#ch22_l_025}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：あ、ほんとだ。
    voice "ch22_s_046"
    s "Ah, you're right. The julienne's nice.{#ch22_s_046}"

    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：うふふー。
    voice "ch22_l_026"
    l "Heh heh~. Right?{#ch22_l_026}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：さ、分かったら、あっち行って！
    voice "ch22_l_027"
    l "Now that you've seen, go away! You're in the way! I-I get nervous when people watch!{#ch22_l_027}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：へいへい。  [voice 12162]
    voice "ch22_s_047"
    s "Yes, yes.{#ch22_s_047}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+223, level=80]
    $ dissolve_fx("id(223)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：（次は、シエスタだ）
    s "(Next is Siesta.){#ch22_s_048}"

    # [SE       se0      play=+81]
    # シエスタ：………。
    si "…{#ch22_si_026}"

    # サイト：（シエスタ……。
    s "(Siesta… She looks so serious…){#ch22_s_049}"

    # サイト：あ、これうまそ。
    voice "ch22_s_050"
    s "Ah, that looks good. Just a tiny bite.{#ch22_s_050}"

    # [SE       se0      play=+71]
    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay10    vibrate=7]
    # [SPRITE   lay2     hide, vibrate=7]
    # [SPRITE   lay5     hide, vibrate=7]
    # [SPRITE   lay9     vibrate=7]
    # [LAYER    lay0     vibrate=7]
    # [SPRITE   lay1     vibrate=7]
    # [SPRITE   lay7     vibrate=7]
    # [SPRITE   lay6     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay10    hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay9     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # シエスタ：だめです！  [voice 14898]
    voice "ch22_si_027"
    si "No!{#ch22_si_027}"

    # サイト：いてっ。  [voice 12164]
    voice "ch22_s_051"
    s "Ouch.{#ch22_s_051}"

    # シエスタ：つまみぐいなんてお行儀悪いですよ。  [voice 14899]
    voice "ch22_si_028"
    si "Sneaking bites is bad manners, you know.{#ch22_si_028}"

    # サイト：たはは……。
    voice "ch22_s_052"
    s "Ha ha… It just looked so tasty, I couldn't help it.{#ch22_s_052}"

    # シエスタ：もうすぐ出来上がりますから、
    voice "ch22_si_029"
    si "It'll be ready soon, so please wait over there. …Wait.{#ch22_si_029}"

    # サイト：ん？
    voice "ch22_s_053"
    s "Hmm? What's wrong? Your face is bright red.{#ch22_s_053}"

    # シエスタ：い、いえ、あ、あのこんなこと言ってると、
    voice "ch22_si_030"
    si "N-No, I… Um, when I say things like this, it's just like… Um, that…{#ch22_si_030}"

    # サイト：まるで？  [voice 12167]
    voice "ch22_s_054"
    s "Like what?{#ch22_s_054}"

    # シエスタ：し、新婚さんみたいだなって！
    voice "ch22_si_031"
    si "L-Like a newlywed couple! I'm the wife and Saito-san is… the husband… or something!{#ch22_si_031}"

    # サイト：な、なんですとっ！？  [voice 12168]
    voice "ch22_s_055"
    s "W-What was that!?{#ch22_s_055}"

    # シエスタ：い、言っちゃった……。
    voice "ch22_si_032"
    si "I-I said it… S-Sorry. I said something strange…{#ch22_si_032}"

    # サイト：いいいい、いいいや、
    voice "ch22_s_056"
    s "I-It's fine! It's fine! I-It's really fine!{#ch22_s_056}"

    # シエスタ：……。  [voice 14904]
    voice "ch22_si_033"
    si "…{#ch22_si_033}"

    # サイト：……。  [voice 12170]
    voice "ch22_s_057"
    s "…{#ch22_s_057}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+32, level=200]
    $ fade_fx("id(32)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SE       se0      play=+88]
    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay10    vibrate=7]
    # [SPRITE   lay2     vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [SPRITE   lay9     vibrate=7]
    # [LAYER    lay0     vibrate=7]
    # [SPRITE   lay1     vibrate=7]
    # [SPRITE   lay7     vibrate=7]
    # [SPRITE   lay6     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay10    hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay9     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # サイト：はうっ！？  [voice 12171]
    voice "ch22_s_058"
    s "Whoa!{#ch22_s_058}"

    # サイト：……。  [voice 12172]
    voice "ch22_s_059"
    s "…{#ch22_s_059}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+526, level=160, dir=2A]
    # シエスタ：きゃあっ！
    voice "ch22_si_034"
    si "Kyaa! Why did the knife fly at me!? Saito-san, are you all right!?{#ch22_si_034}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なんとか……。
    voice "ch22_s_060"
    s "Somehow… It only grazed my neck, it seems… This knife is…{#ch22_s_060}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：あーら、また包丁飛ばしちゃったわ。  [voice 6630]
    voice "ch22_l_028"
    l "Oh my, I sent the knife flying again.{#ch22_l_028}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：やっぱりお前か！
    voice "ch22_s_061"
    s "So it was you! You did it on purpose, didn't you!{#ch22_s_061}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：そんなわけないでしょう？
    voice "ch22_l_029"
    l "Surely not? My hand just slipped.{#ch22_l_029}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そ、そうか。  [voice 12175]
    voice "ch22_s_062"
    s "I-Is that so.{#ch22_s_062}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：……惜しかったわ。  [voice 6632]
    voice "ch22_l_030"
    l "…What a shame.{#ch22_l_030}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：な、なんか言ったか！？  [voice 12176]
    voice "ch22_s_063"
    s "D-Did you say something!?{#ch22_s_063}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：別にー。
    voice "ch22_l_031"
    l "Nothing. Ah, I'm busy, busy.{#ch22_l_031}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：じゃ、じゃあ、俺行くね。
    voice "ch22_s_064"
    s "W-Well, I'll be going, then. I feel my life is in danger.{#ch22_s_064}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：は、はい、そうですね。
    voice "ch22_si_035"
    si "Y-Yes, that's right. Saito-san, please look forward to it.{#ch22_si_035}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ああ、もちろんさ！  [voice 12178]
    voice "ch22_s_065"
    s "Ah, of course!{#ch22_s_065}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+32, level=200]
    $ fade_fx("id(32)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：（……あれ？
    s "(…Huh? What's Haruna doing? It looks like she's cutting a cucumber monster…){#ch22_s_066}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：なんで切っても切っても、
    voice "ch22_ha_004"
    ha "Why does it keep growing back no matter how much I cut it? How am I supposed to slice this?{#ch22_ha_004}"

    # サイト：（……それ、本当に野菜なのか？
    s "(…Is that really a vegetable? Or something that shouldn't exist in this world…){#ch22_s_067}"

    # [SE       se0      play=+64]
    # [SPRITE   lay7     image=+955, level=160, dir=1A]
    # ハルナ：ひゃあっ！！
    voice "ch22_ha_005"
    ha "Eeeh!! Ugh… How am I supposed to cut an exploding tomato… mmph.{#ch22_ha_005}"

    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：こんにゃくみたいなゴボウ……、
    voice "ch22_ha_006"
    ha "Burdock like konjac… cabbage like plastic… How do they eat these in this world…?{#ch22_ha_006}"

    # サイト：（やっぱり、見慣れない食材に苦戦してるな）
    s "(She's struggling with unfamiliar ingredients, after all.){#ch22_s_068}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+32, level=200]
    $ fade_fx("id(32)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：（そして、タバサは……っと）
    s "(And Tabitha…){#ch22_s_069}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SE       se0      play=+72]
    # タバサ：……。
    t "…{#ch22_t_003}"

    # サイト：……。  [voice 12179]
    voice "ch22_s_070"
    s "…{#ch22_s_070}"

    # [SE       se0      play=+72]
    # タバサ：……。
    t "…{#ch22_t_004}"

    # サイト：（ずっと本を読んでるみたいだけど……、
    s "(She seems to be reading the whole time… Is she really all right?){#ch22_s_071}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+32, level=200]
    $ fade_fx("id(32)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # コルベール：みなさん、なかなか見事な手際ですねぇ？  [voice 1169]
    voice "ch22_c_003"
    c "Everyone, your technique is quite impressive, isn't it?{#ch22_c_003}"

    # オスマン：ふむふむ、花嫁修業も上々といった
    voice "ch22_o_004"
    o "Hmm hmm. Bridal training is going well, too, I see.{#ch22_o_004}"

    # サイト：（後は、料理の完成をゆっくりと
    s "(All that's left is to wait patiently for the food to be done… Gaku gaku buru buru…){#ch22_s_072}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay10    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # → next scene 818
    jump ch22_2_scene_818

label ch22_2_scene_818:

    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # コルベール：それでは、まもなく終了時間となります。  [voice 1170]
    voice "ch22_c_004"
    c "Well then, it'll be time to finish soon.{#ch22_c_004}"

    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+32, level=200]
    $ fade_fx("id(32)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay9     x=304, y=416]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SE       se0      play=+72]
    # タバサ：ん。  [voice 15637]
    voice "ch22_t_005"
    t "Mm.{#ch22_t_005}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あら、ルイズ。
    voice "ch22_k_017"
    k "Oh, Louise. Your cooking turned out more decent than I expected.{#ch22_k_017}"

    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ふん、これぐらいのことなんて。
    voice "ch22_l_032"
    l "Hmph, this much is nothing. It's easier than washing my face in the morning.{#ch22_l_032}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：見た目は良くても、味のほうはどうかしらね？  [voice 3423]
    voice "ch22_k_018"
    k "It may look good, but how does it taste, I wonder?{#ch22_k_018}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+984, level=160, dir=2A]
    # ハルナ：はあっ……。
    voice "ch22_ha_007"
    ha "Haaah… It seems I managed to make something presentable.{#ch22_ha_007}"

    # [SPRITE   lay7     x=224, y=0]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：みなさん、どうにか時間内に作り上げる事が
    voice "ch22_si_036"
    si "Everyone, it looks like we managed to finish in time, didn't we?{#ch22_si_036}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ああっ、やっぱりシエスタからは、
    voice "ch22_s_073"
    s "Ah, as expected—I can feel Siesta's composure as a servant. Well, naturally.{#ch22_s_073}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：ふむっ。
    voice "ch22_o_005"
    o "Hmm. Then let's start eating right away, shall we?{#ch22_o_005}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：採点するうえでの公平を期するために、
    voice "ch22_c_005"
    c "To ensure fair judging, let's have the cooks draw lots for the tasting order.{#ch22_c_005}"

    # コルベール：それではどうぞ。  [voice 1172]
    voice "ch22_c_006"
    c "All right, then. Please.{#ch22_c_006}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ふふっ、あたしが１番よ。  [voice 3424]
    voice "ch22_k_019"
    k "Heh heh, I'm number one.{#ch22_k_019}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：わ、私が２番。  [voice 2405]
    voice "ch22_ha_008"
    ha "I-I'm number two.{#ch22_ha_008}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：３番よ。  [voice 6635]
    voice "ch22_l_033"
    l "Number three.{#ch22_l_033}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：わたし、４番です。  [voice 14908]
    voice "ch22_si_037"
    si "I'm number four.{#ch22_si_037}"

    # [SPRITE   lay2     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：５。  [voice 15638]
    voice "ch22_t_006"
    t "Five.{#ch22_t_006}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：（綺麗に片付いた調理台の上を見ると……）
    s "(Looking at the tidy counters…){#ch22_s_074}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（あれ、キュルケの台には
    s "(Huh? On Kirche's counter there's only an empty glass. Did she fail?){#ch22_s_075}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：（春奈の台には、大きなボウルが置いてある。
    s "(On Haruna's counter there's a big bowl. The lid's closed, so I can't see inside.){#ch22_s_076}"

    # サイト：（ルイズとシエスタは……煮込みモノか。
    s "(Louise and Siesta… something stewed. Big pots with ladles stuck in them.){#ch22_s_077}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（タバサは……。
    s "(Tabitha… a cloth over a big plate. What's under it is a complete mystery.){#ch22_s_078}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：それでは、ミス・ツェルプストーの料理から
    voice "ch22_c_007"
    c "Well then, let's start with Miss Zerbst's dish.{#ch22_c_007}"

    # [SPRITE   lay9     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：分かりましたわ、ミスタ・コルベール。  [voice 3425]
    voice "ch22_k_020"
    k "Understood, Mr. Colbert.{#ch22_k_020}"

    # サイト：（さて、いよいよか……）
    s "(Well, here we go…){#ch22_s_079}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # → next scene 819
    jump ch22_2_scene_819

label ch22_2_scene_819:

    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ではみなさん、グラスをご用意ください。
    voice "ch22_k_021"
    k "Everyone, please take a glass. I've prepared a special drink, ordered for this very day!{#ch22_k_021}"

    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # オスマン：ほほう、ドリンクとは。  [voice 4479]
    voice "ch22_o_006"
    o "My, my. A drink, is it?{#ch22_o_006}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # コルベール：これは、食前酒がわりにちょうど良いですねぇ。  [voice 1174]
    voice "ch22_c_008"
    c "This is perfect as an aperitif, isn't it.{#ch22_c_008}"

    # サイト：（うわぁ、見るからにヤバそうな粘り気）
    s "(Whoa, it looks dangerously viscous…){#ch22_s_080}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay9     hide]
    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：このドリンクは、ダーリンのために
    voice "ch22_k_022"
    k "I made this drink for darling… So drink plenty, okay?{#ch22_k_022}"

    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ちょっとキュルケ？
    voice "ch22_l_034"
    l "Hey, Kirche. Just what is this? This horrible-colored liquid…{#ch22_l_034}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：さぁ、遠慮しないで。
    voice "ch22_k_023"
    k "Come now, don't hold back. Help yourself.{#ch22_k_023}"

    menu:
        "Have Siesta try it{#ch22_2_c_819_1}":
            jump ch22_2_scene_820
        "How about tasting it myself?{#ch22_2_c_819_2}":
            jump ch22_2_scene_821
        "I'll drink it!{#ch22_2_c_819_3}":
            jump ch22_2_scene_822

label ch22_2_scene_820:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：シエスタも飲んでみなよ？
    voice "ch22_s_081"
    s "Why don't you try it too, Siesta? Here's a glass.{#ch22_s_081}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：ええっ、あの……えーと……。
    voice "ch22_si_038"
    si "Eh? Um… Well… Just a little! …Gulp.{#ch22_si_038}"

    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # シエスタ：うううっ。
    voice "ch22_si_039"
    si "Ugh. That's enough.{#ch22_si_039}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：え、まじ？  [voice 12182]
    voice "ch22_s_082"
    s "Eh, seriously?{#ch22_s_082}"

    # → next scene 823
    jump ch22_2_scene_823

label ch22_2_scene_821:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：ま、まずは自分で味見ってどうかな？  [voice 12183]
    voice "ch22_s_083"
    s "W-Well, how about tasting it myself first?{#ch22_s_083}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：え？  [voice 3429]
    voice "ch22_k_024"
    k "Eh?{#ch22_k_024}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：味見した？  [voice 12184]
    voice "ch22_s_084"
    s "Did you taste it?{#ch22_s_084}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：わ、分かったわよっ！！
    voice "ch22_k_025"
    k "I-Understood!! …Gulp.{#ch22_k_025}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+1, level=200]
    $ fade_fx("id(1)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：……うっ。  [voice 3431]
    voice "ch22_k_026"
    k "…Ugh.{#ch22_k_026}"

    # [SPRITE   lay6     hide]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：お、おいおい、
    voice "ch22_s_085"
    s "H-Hey, Kirche, you're crouching over—are you all right?{#ch22_s_085}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：自滅。  [voice 15639]
    voice "ch22_t_007"
    t "Self-destruction.{#ch22_t_007}"

    # → next scene 823
    jump ch22_2_scene_823

label ch22_2_scene_822:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # サイト：（くそっ……俺も男だっ！！）
    s "(Damn… I'm a man too!!){#ch22_s_086}"

    # → next scene 823
    jump ch22_2_scene_823

label ch22_2_scene_823:

    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay6     x=464, y=416]
    # [SPRITE   lay1     x=144, y=416]
    # [LAYER    lay0     x=304, y=416]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：いただきまっす！！
    voice "ch22_s_087"
    s "Itadakimasu!! Mom, Dad, I'm sorry! Gulping it down!{#ch22_s_087}"

    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay10    vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay9     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay10    hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay9     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+1, level=200]
    $ fade_fx("id(1)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：……。  [voice 12187]
    voice "ch22_s_088"
    s "…{#ch22_s_088}"

    # サイト：（……死ねる）
    s "(…I can die now){#ch22_s_089}"

    # [SPRITE   lay5     hide]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：どおかしら、ダーリン。
    voice "ch22_k_027"
    k "How is it, darling? Feeling energized?{#ch22_k_027}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：無理。  [voice 12188]
    voice "ch22_s_090"
    s "Impossible.{#ch22_s_090}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：って、こんなの飲めるはずねーだろ！  [voice 12189]
    voice "ch22_s_091"
    s "Wait—there's no way anyone could drink this!{#ch22_s_091}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # [SPRITE   lay10    image=+924, level=160, dir=1A]
    # コルベール：うむ……。
    voice "ch22_c_009"
    c "Hmm… This taste…{#ch22_c_009}"

    # オスマン：……。
    o "…{#ch22_o_007}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay10    hide]
    # [SPRITE   lay6     image=+713, level=160, dir=2A]
    # キュルケ：なぁによぉ、その反応はっ！
    voice "ch22_k_028"
    k "What's with that reaction! Oh, I'm so disappointed…{#ch22_k_028}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ところでこれ、いったい何が原料なんだ？  [voice 12190]
    voice "ch22_s_092"
    s "By the way, what's it made from?{#ch22_s_092}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ああ、これ？
    voice "ch22_k_029"
    k "Oh, this? It's the fresh blood of a rare animal—a 'sea lizard.'{#ch22_k_029}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：１匹からほんのわずかしか取れない、
    voice "ch22_k_030"
    k "You can only get a tiny amount from one, so it's incredibly precious…{#ch22_k_030}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ま、まじですか？  [voice 12191]
    voice "ch22_s_093"
    s "R-Really?{#ch22_s_093}"

    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：もお、サイトったら、だらしがないのねぇ。
    voice "ch22_k_031"
    k "Oh, Saito, you're so sloppy. If you drink this, you'll be full of energy… Especially for a man…{#ch22_k_031}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：りょ、料理じゃねーじゃないか。  [voice 12192]
    voice "ch22_s_094"
    s "Th-That's not cooking at all.{#ch22_s_094}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 824
    jump ch22_3

    # ==== КОНЕЦ ЧАСТИ 2 ====
    jump ch22_3
    return

