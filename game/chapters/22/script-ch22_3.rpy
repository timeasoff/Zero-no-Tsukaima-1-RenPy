# Глава 22, часть 3 (сцены 824–837): дегустация, карри Сиэсты.
# Источник: ps2_source/chapters/chapter_23_料理の鉄人.txt (SCENE 824-837).

label ch22_3:
    $ tndl(None)
    $ show_sprites()

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
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+32, level=200]
    $ fade_fx("id(32)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+32, level=200]
    $ fade_fx("id(32)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
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
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+223, level=80]
    $ dissolve_fx("id(223)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+81]
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
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+526, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+32, level=200]
    $ fade_fx("id(32)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # [SE       se0      play=+64]
    # [SPRITE   lay7     image=+955, level=160, dir=1A]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+32, level=200]
    $ fade_fx("id(32)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SE       se0      play=+72]
    # [SE       se0      play=+72]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+32, level=200]
    $ fade_fx("id(32)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay10    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+32, level=200]
    $ fade_fx("id(32)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay9     x=304, y=416]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SE       se0      play=+72]
    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+984, level=160, dir=2A]
    # [SPRITE   lay7     x=224, y=0]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # [SPRITE   lay10    hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [SPRITE   lay9     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [SPRITE   lay9     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [SPRITE   lay10    hide]
    # [SPRITE   lay9     hide]
    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+1, level=200]
    $ fade_fx("id(1)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # [SPRITE   lay6     hide]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
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
    # [SPRITE   lay5     hide]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # [SPRITE   lay10    image=+924, level=160, dir=1A]
    # [SPRITE   lay9     hide]
    # [SPRITE   lay10    hide]
    # [SPRITE   lay6     image=+713, level=160, dir=2A]
    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
label ch22_3_scene_824:

    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # コルベール：では、みなさんが回復したところで。
    voice "ch22_c_010"
    c "Well then, now that everyone's recovered. Let's move on to the next tasting.{#ch22_c_010}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：はい、私です。  [voice 2406]
    voice "ch22_ha_009"
    ha "Yes, it's me.{#ch22_ha_009}"

    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：新鮮な野菜を使ったサラダを作ってみました。  [voice 2407]
    voice "ch22_ha_010"
    ha "I tried making a salad with fresh vegetables.{#ch22_ha_010}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay10    image=+922, level=160, dir=1A]
    # オスマン：ほほぅ、今度は前菜じゃな？
    voice "ch22_o_008"
    o "My, my—a starter this time? Let's dig in… Hmm!?{#ch22_o_008}"

    # [SPRITE   lay10    x=224, y=0]
    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # コルベール：おや、どうかされましたか？
    voice "ch22_c_011"
    c "Oh, is something the matter, Old Osmond?{#ch22_c_011}"

    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：はて、わしの目の錯覚かのぅ？
    voice "ch22_o_009"
    o "Hmm, is it my imagination? The vegetables on the plate seem to be moving.{#ch22_o_009}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay9     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：なんか、野菜からガサゴソ音がするわ。  [voice 6637]
    voice "ch22_l_035"
    l "There's a rustling sound coming from the vegetables.{#ch22_l_035}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：うおおっ、ゴボウの千切りが、
    voice "ch22_s_095"
    s "Whoa! The shredded burdock is moving every now and then!{#ch22_s_095}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あら、それ流体ゴボウですね。
    voice "ch22_si_040"
    si "Oh, that's fluid burdock. It's an ornamental plant, so it's rarely used in cooking…{#ch22_si_040}"

    # [SPRITE   lay2     x=224, y=0]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：こうして料理されてるのを見ると、
    voice "ch22_k_032"
    k "Seeing it cooked like this is a little… no, quite eerie.{#ch22_k_032}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：か、かんさい……植物なんですか？
    voice "ch22_ha_011"
    ha "O-Ornamental plant? What is it, what is that…{#ch22_ha_011}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：まさにファンタジー世界だな。  [voice 12194]
    voice "ch22_s_096"
    s "This is truly a fantasy world.{#ch22_s_096}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：流体ゴボウを食材に選ぶとは、
    voice "ch22_c_012"
    c "Choosing fluid burdock as an ingredient is quite an original idea, Haruna-kun.{#ch22_c_012}"

    # [SPRITE   lay9     x=224, y=0]
    # [SPRITE   lay7     image=+990, level=160, dir=2A]
    # ハルナ：いえ、その……。
    voice "ch22_ha_012"
    ha "No, it's… I'm not very familiar with the vegetables of this world…{#ch22_ha_012}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：確かに、平民にしか思いつかないわね、これは。  [voice 3438]
    voice "ch22_k_033"
    k "Indeed. Only a commoner would think of something like this.{#ch22_k_033}"

    menu:
        "Try the wriggling vegetables{#ch22_3_c_824_1}":
            jump ch22_3_scene_825
        "Offer it to Haruna{#ch22_3_c_824_2}":
            jump ch22_3_scene_826
        "Pinch it timidly{#ch22_3_c_824_3}":
            jump ch22_3_scene_827

label ch22_3_scene_825:

    # [SPRITE   lay7     image=+990, level=160, dir=2A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：よ、よし。
    voice "ch22_s_097"
    s "O-Okay. Let's try eating it, then.{#ch22_s_097}"

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：あっ、ちゃんと特製のドレッシングをかけてね？  [voice 2410]
    voice "ch22_ha_013"
    ha "Ah, make sure you put the special dressing on it?{#ch22_ha_013}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：あ、ドレッシングは普通なのね。  [voice 12196]
    voice "ch22_s_098"
    s "Ah, the dressing's ordinary, then.{#ch22_s_098}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：しっかし、青いタマネギとか、白いピーマンとか
    voice "ch22_s_099"
    s "But blue onions, white peppers, wriggling burdock, and cabbage shreds hard as needles…*gulp*.{#ch22_s_099}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：食うぞっ！？  [voice 12198]
    voice "ch22_s_100"
    s "I'm going to eat it!?{#ch22_s_100}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：んぐっ……はんはほへわぉ！？  [voice 12199]
    voice "ch22_s_101"
    s "Mmgh… Hanhahohewa!?{#ch22_s_101}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：うぐ、なんだこれわ？  [voice 12200]
    voice "ch22_s_102"
    s "Ugh, what is this?{#ch22_s_102}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：うわあぁ……。
    voice "ch22_si_041"
    si "Whoa… That's an amazing sound, isn't it…{#ch22_si_041}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # → next scene 828
    jump ch22_3_scene_828

label ch22_3_scene_826:

    # [SPRITE   lay7     image=+990, level=160, dir=2A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：よし、どうせなら春奈も一緒に食おうぜ？  [voice 12201]
    voice "ch22_s_103"
    s "All right, why don't we eat it together, then, Haruna?{#ch22_s_103}"

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：うん、もちろんいいよ。  [voice 2411]
    voice "ch22_ha_014"
    ha "Mm, of course.{#ch22_ha_014}"

    # [SPRITE   lay7     image=+955, level=160, dir=1A]
    # ハルナ：ふぅ。
    voice "ch22_ha_015"
    ha "Phew. Ready, set! *gulp*!{#ch22_ha_015}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：す、凄い音がしてるわよ？  [voice 3439]
    voice "ch22_k_034"
    k "Th-That's an incredible sound!{#ch22_k_034}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：それは、鉱山キャベツです。  [voice 14913]
    voice "ch22_si_042"
    si "That's mine cabbage.{#ch22_si_042}"

    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：んぐんぐ……んぐぅ～～！！  [voice 2413]
    voice "ch22_ha_016"
    ha "Mng mng… Mnguuu~~!!{#ch22_ha_016}"

    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：ハルナさん、大丈夫ですかっ！？  [voice 14914]
    voice "ch22_si_043"
    si "Haruna, are you all right!?{#ch22_si_043}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # → next scene 828
    jump ch22_3_scene_828

label ch22_3_scene_827:

    # [SPRITE   lay7     image=+990, level=160, dir=2A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：こ、これ、食えるのか？  [voice 12202]
    voice "ch22_s_104"
    s "C-Can you even eat this?{#ch22_s_104}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：あ、落としちゃった！  [voice 12203]
    voice "ch22_s_105"
    s "Ah, I dropped it!{#ch22_s_105}"

    # [SPRITE   lay7     image=+988, level=160, dir=2A]
    # ハルナ：もったいないわね！
    voice "ch22_ha_017"
    ha "What a waste! …Eh!?{#ch22_ha_017}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：まじか……。
    voice "ch22_s_106"
    s "No way… The cucumber just dug into the ground.{#ch22_s_106}"

    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：うん。
    voice "ch22_ha_018"
    ha "Yeah. There's a hole left behind.{#ch22_ha_018}"

    # サイト：見なかった。
    voice "ch22_s_107"
    s "We didn't see that. We saw nothing.{#ch22_s_107}"

    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：そ、そうね！
    voice "ch22_ha_019"
    ha "R-Right! Now, try it! Salad of cucumbers that burrow into the ground!{#ch22_ha_019}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：くそっ、ファンタジー世界め！  [voice 12206]
    voice "ch22_s_108"
    s "Damn you, fantasy world!{#ch22_s_108}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # → next scene 828
    jump ch22_3_scene_828

label ch22_3_scene_828:

    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # コルベール：栄養価も高く、とてもヘルシーな逸品ですね。
    voice "ch22_c_013"
    c "It's highly nutritious and very healthy, isn't it. And the appearance is unusual, too.{#ch22_c_013}"

    # サイト：（コルベール先生と、オスマン学院長は
    s "(Colbert-sen and Headmaster Osmond are eating it properly. Fearsome, this fantasy world.){#ch22_s_109}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay10    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # → next scene 829
    jump ch22_3_scene_829

label ch22_3_scene_829:

    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # オスマン：では、そろそろ次の品評といきますかな？  [voice 4482]
    voice "ch22_o_010"
    o "Well then, shall we move on to the next tasting?{#ch22_o_010}"

    # コルベール：次は、ミス・ヴァリエールの料理ですね。  [voice 1180]
    voice "ch22_c_014"
    c "Next is Miss Valliere's dish.{#ch22_c_014}"

    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # オスマン：ほう、シチューかね。  [voice 4483]
    voice "ch22_o_011"
    o "Oh, stew, is it?{#ch22_o_011}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：各地から極上の素材を集めましたわ。
    voice "ch22_l_036"
    l "I gathered the finest ingredients from everywhere. Poultry, potatoes, onions… I selected each with the utmost care.{#ch22_l_036}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：見た目は結構まともじゃないか？  [voice 12207]
    voice "ch22_s_110"
    s "It looks pretty decent, doesn't it?{#ch22_s_110}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：見た目だけじゃないわよっ！！
    voice "ch22_l_037"
    l "It's not just the look! Hurry up and eat it, why don't you?{#ch22_l_037}"

    menu:
        "Eat Louise's stew{#ch22_3_c_829_1}":
            jump ch22_3_scene_830
        "Offer it to Kirche{#ch22_3_c_829_2}":
            jump ch22_3_scene_831
        "Did you taste it?{#ch22_3_c_829_3}":
            jump ch22_3_scene_832

label ch22_3_scene_830:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：どれどれ……はぐっ……んぐんぐっ……。  [voice 12208]
    voice "ch22_s_111"
    s "Let's see… *gulp*… Mng mng…{#ch22_s_111}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：おおっ、こ、これは！？  [voice 12209]
    voice "ch22_s_112"
    s "Oh! Th-This is!?{#ch22_s_112}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……どう？
    voice "ch22_l_038"
    l "…Well? Saito?{#ch22_l_038}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：んん～っ！！
    voice "ch22_s_113"
    s "Mmmh!! This is surprising!!{#ch22_s_113}"

    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：でしょでしょ？
    voice "ch22_l_039"
    l "Right, right? It's delicious, isn't it? That's what I can do!{#ch22_l_039}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：具が均等に刻んであって、
    voice "ch22_s_114"
    s "The ingredients are cut evenly and it's cooked through. I'm impressed, Louise!{#ch22_s_114}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：そんなの当たり前でしょうが、バカっ！！  [voice 6642]
    voice "ch22_l_040"
    l "That goes without saying, you idiot!!{#ch22_l_040}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：でも、何でこんなに甘いんだ？  [voice 12212]
    voice "ch22_s_115"
    s "But why is it so sweet?{#ch22_s_115}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：えっ……甘い？  [voice 6643]
    voice "ch22_l_041"
    l "Eh… Sweet?{#ch22_l_041}"

    # → next scene 833
    jump ch22_3_scene_833

label ch22_3_scene_831:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：キュルケにとっては、宿敵の料理じゃないか。
    voice "ch22_s_116"
    s "For Kirche this is her sworn enemy's cooking. Why don't you check it with your own tongue?{#ch22_s_116}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：それもそうね……。
    voice "ch22_k_035"
    k "True enough… Well then, I'll have some. *gulp*… Mm mm…{#ch22_k_035}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：キュルケ、大丈夫か？
    voice "ch22_s_117"
    s "Kirche, are you all right? You're not going to scream suddenly, are you?{#ch22_s_117}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：どーいう意味よ、それ！？  [voice 6644]
    voice "ch22_l_042"
    l "What's that supposed to mean!?{#ch22_l_042}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：んふっ……実にヴァリエールらしい味だわ。
    voice "ch22_k_036"
    k "Mm hmm… A very Valliere-like taste. How old are you this year? Making a stew like this… heh heh!{#ch22_k_036}"

    # ルイズ：なによそれっ？  [voice 6645]
    voice "ch22_l_043"
    l "What was that!?{#ch22_l_043}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ここまで甘ったるいシチューは、
    voice "ch22_k_037"
    k "This is the sweetest stew I've ever eaten.{#ch22_k_037}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：えっ……甘い？  [voice 6646]
    voice "ch22_l_044"
    l "Eh… Sweet?{#ch22_l_044}"

    # → next scene 833
    jump ch22_3_scene_833

label ch22_3_scene_832:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：食う前にひとつ、聞いておきたいことがある。  [voice 12215]
    voice "ch22_s_118"
    s "Before I eat, there's something I want to ask you.{#ch22_s_118}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：何よ。  [voice 6647]
    voice "ch22_l_045"
    l "What is it?{#ch22_l_045}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：お前、ちゃんと味見したか？  [voice 12216]
    voice "ch22_s_119"
    s "Did you taste it properly?{#ch22_s_119}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：はあっ！？
    voice "ch22_l_046"
    l "Hah!? Why should I have to taste my own cooking!?{#ch22_l_046}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：わたしが作る料理の味見は、
    voice "ch22_l_047"
    l "Tasting what I cook is your job as my familiar, isn't it?{#ch22_l_047}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：サイトが審査員なんてやってるから、
    voice "ch22_l_048"
    l "Because you were playing judge, I couldn't tell how it tasted!{#ch22_l_048}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：やっぱり。  [voice 12217]
    voice "ch22_s_120"
    s "Just as I thought.{#ch22_s_120}"

    # → next scene 833
    jump ch22_3_scene_833

label ch22_3_scene_833:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     x=304, y=416]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：じゃ、わたしもいただきますね。
    voice "ch22_si_044"
    si "Well then, I'll have some too. Let's see… Huh?{#ch22_si_044}"

    # [SPRITE   lay2     x=224, y=0]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：ど、どうしたの、シエスタ？  [voice 6651]
    voice "ch22_l_049"
    l "W-What's wrong, Siesta?{#ch22_l_049}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：ミス・ヴァリエール……、
    voice "ch22_si_045"
    si "Miss Valliere… Um, does this have honey in it? It's often used as a secret ingredient…{#ch22_si_045}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：ええ……。
    voice "ch22_l_050"
    l "Yes… It was in the book. So that's why…{#ch22_l_050}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：……どれくらい入れたんだ？  [voice 12218]
    voice "ch22_s_121"
    s "…How much did you put in?{#ch22_s_121}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：……ひとビン。  [voice 6653]
    voice "ch22_l_051"
    l "…One whole jar.{#ch22_l_051}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+990, level=160, dir=2A]
    # ハルナ：んぐっ……けほっ、けほっ……。  [voice 2417]
    voice "ch22_ha_020"
    ha "Mmgh… Cough, cough…{#ch22_ha_020}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：この大きさの鍋で、ビン１本は多すぎますっ！  [voice 14917]
    voice "ch22_si_046"
    si "For a pot this size, one whole jar is far too much!{#ch22_si_046}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：まったく……まずは味見しろ。  [voice 12219]
    voice "ch22_s_122"
    s "Honestly… You should taste it first.{#ch22_s_122}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：うるっさいわねぇ、ホントに。
    voice "ch22_l_052"
    l "Shut up, honestly. Don't you men nag me! Eat what your mistress gives you without complaint!?{#ch22_l_052}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # オスマン：ほほっ、この味付けじゃと、
    voice "ch22_o_012"
    o "Heh heh. With this seasoning, I'd say a small child would enjoy it more than us.{#ch22_o_012}"

    # コルベール：確かに少々甘口ですが、
    voice "ch22_c_015"
    c "It is a bit sweet, certainly, but there's a certain warmth to this stew.{#ch22_c_015}"

    # サイト：（まぁ、ルイズのイメージからすれば、
    s "(Well, judging by Louise's standards, that was better than expected. Still, she looks dissatisfied…){#ch22_s_123}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay10    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # → next scene 834
    jump ch22_3_scene_834

label ch22_3_scene_834:

    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # コルベール：それでは、シエスタの料理ですね。  [voice 1182]
    voice "ch22_c_016"
    c "Well then, Siesta's dish is next.{#ch22_c_016}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay2     image=+494, level=140, dir=1A]
    # [SE       se0      play=+53]
    # シエスタ：これまで発表された料理を食べた限りでは、
    voice "ch22_si_047"
    si "Judging by what's been served so far, none of you know anything at all!!{#ch22_si_047}"

    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：おおっ！？  [voice 12220]
    voice "ch22_s_124"
    s "Oh!?{#ch22_s_124}"

    # シエスタ：お料理を作るときは、食べてくれる人の事を
    voice "ch22_si_048"
    si "When you cook, you must think about the person who'll eat it!{#ch22_si_048}"

    # シエスタ：料理人は調理場に立った時から、
    voice "ch22_si_049"
    si "From the moment a cook enters the kitchen, they must never forget their love for the one eating their food!{#ch22_si_049}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：さすがシエスタ。
    voice "ch22_s_125"
    s "As expected of Siesta. Well said.{#ch22_s_125}"

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：って、マルトーさんがおっしゃってました。  [voice 14921]
    voice "ch22_si_050"
    si "Actually, Marto-san said that.{#ch22_si_050}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：受け売りかいっ。  [voice 12222]
    voice "ch22_s_126"
    s "Just repeating him, were you?{#ch22_s_126}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：さあ、みなさん召し上がってください。
    voice "ch22_si_051"
    si "Now, everyone, please eat. This is a special stew passed down from my great-great-grandfather!{#ch22_si_051}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # [SPRITE   lay4     image=+555, level=160, dir=1A]
    # モンモランシー：ルイズがシチューを作ったっていうのに、
    voice "ch22_m_002"
    m "Even though Louise made stew, you two serve the same thing… She must be pretty confident, that girl, don't you think?{#ch22_m_002}"

    # ギーシュ：まぁ。
    voice "ch22_g_002"
    g "Well. Let's enjoy it thoroughly, Montmorency.{#ch22_g_002}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay4     hide]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：はい、どうぞ、サイトさん。
    voice "ch22_si_052"
    si "Here, Saito-san. Please eat.{#ch22_si_052}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ありがとうシエスタ……って。  [voice 12223]
    voice "ch22_s_127"
    s "Thanks, Siesta… Wait.{#ch22_s_127}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ああーーーっ！！
    voice "ch22_s_128"
    s "Aaaaah!! This dish is… No way!?{#ch22_s_128}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay7     image=+955, level=160, dir=1A]
    # ハルナ：これって！
    voice "ch22_ha_021"
    ha "This is! Could it be…{#ch22_ha_021}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：サイトさんもハルナさんもこの料理を
    voice "ch22_si_053"
    si "Both you and Haruna-san know this dish, don't you?{#ch22_si_053}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：これは、カレーだよっ！！
    voice "ch22_s_129"
    s "This is curry!! It's a dish from the world we lived in!!{#ch22_s_129}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：くすっ……。
    voice "ch22_si_054"
    si "Hehe… Eat plenty, okay!{#ch22_si_054}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：ああっ、いただきます！
    voice "ch22_s_130"
    s "Ah, I'm eating! *gulp*, *chew chew*…{#ch22_s_130}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：まさか、カレーが出てくるなんてなぁ……。  [voice 12227]
    voice "ch22_s_131"
    s "To think curry would show up here of all places…{#ch22_s_131}"

    menu:
        "Curry is here!{#ch22_3_c_834_1}":
            jump ch22_3_scene_835
        "Such a joyful dish!{#ch22_3_c_834_2}":
            jump ch22_3_scene_836
        "Teach Louise, too{#ch22_3_c_834_3}":
            jump ch22_3_scene_837

label ch22_3_scene_835:

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：こんな所で俺達の世界特有の料理が
    voice "ch22_s_132"
    s "A dish unique to our world showing up in a place like this—it's kind of amazing, isn't it?{#ch22_s_132}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：ホントに、そうですね。
    voice "ch22_si_055"
    si "Truly, isn't it. I'm a little grateful to my great-great-grandfather.{#ch22_si_055}"

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：おかげで、サイトさんが、
    voice "ch22_si_056"
    si "Thanks to him, Saito-san was so happy…{#ch22_si_056}"

    # → next scene 838
    jump ch22_4

label ch22_3_scene_836:

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：こんなにうれしい料理が待っていたのなら、
    voice "ch22_s_133"
    s "If I'd known such a wonderful dish was waiting, Louise's cooking wouldn't have stood a chance!!{#ch22_s_133}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：あら、随分と言ってくれるじゃないの？
    voice "ch22_l_053"
    l "Oh, you certainly do talk. I suppose my stew was just sweet, childish stew, was it!?{#ch22_l_053}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：もう、サイトになんか絶対に
    voice "ch22_l_054"
    l "Honestly! I'm never cooking for Saito again!{#ch22_l_054}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # → next scene 838
    jump ch22_4

label ch22_3_scene_837:

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：なあ、シエスタ。
    voice "ch22_s_134"
    s "Hey, Siesta. Teach Louise how to make curry later, would you?{#ch22_s_134}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：わ、わたしにっ！？  [voice 6657]
    voice "ch22_l_055"
    l "Me!?{#ch22_l_055}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：え……。
    voice "ch22_si_057"
    si "Eh… Why would you ask that!?{#ch22_si_057}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ほら、カレーとシチューって途中まで
    voice "ch22_s_135"
    s "See, curry and stew are cooked the same way up to a point, right? So I thought maybe Louise could make it, too.{#ch22_s_135}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：それに、俺の国の料理、みんなに
    voice "ch22_s_136"
    s "Besides, I want everyone to know the food of my country.{#ch22_s_136}"

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：はい！
    voice "ch22_si_058"
    si "Yes! That's right.{#ch22_si_058}"

    # → next scene 838
    jump ch22_4

    # ==== КОНЕЦ ЧАСТИ 3 ====
    jump ch22_4
    return

