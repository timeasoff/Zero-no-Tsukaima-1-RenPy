# Глава 22, часть 4 (сцены 838–848): судейство, Сиэста отказывается.
# Источник: ps2_source/chapters/chapter_23_料理の鉄人.txt (SCENE 838-848).

label ch22_4:
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
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [SPRITE   lay9     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay10    image=+922, level=160, dir=1A]
    # [SPRITE   lay10    x=224, y=0]
    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # [SPRITE   lay10    hide]
    # [SPRITE   lay9     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay2     x=224, y=0]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [SPRITE   lay9     x=224, y=0]
    # [SPRITE   lay7     image=+990, level=160, dir=2A]
    # [SPRITE   lay9     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay7     image=+990, level=160, dir=2A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # [SPRITE   lay7     image=+990, level=160, dir=2A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay7     image=+955, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # [SPRITE   lay7     image=+990, level=160, dir=2A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay7     image=+988, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
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
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # [SPRITE   lay9     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay10    hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
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
    # [SPRITE   lay2     x=224, y=0]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+990, level=160, dir=2A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
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
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # [SPRITE   lay9     hide]
    # [SPRITE   lay2     image=+494, level=140, dir=1A]
    # [SE       se0      play=+53]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # [SPRITE   lay4     image=+555, level=160, dir=1A]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay4     hide]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay7     image=+955, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay2     image=+524, level=160, dir=2A]
label ch22_4_scene_838:

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：ありがとう、シエスタ。
    voice "ch22_s_137"
    s "Thanks, Siesta. If I feel like eating it again, you'll treat us, right?{#ch22_s_137}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：ええっ、もちろん！
    voice "ch22_si_059"
    si "Eh? Of course! Just say the word anytime.{#ch22_si_059}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：分かった。  [voice 12234]
    voice "ch22_s_138"
    s "Got it.{#ch22_s_138}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：むうううううっ……。
    voice "ch22_l_056"
    l "Muuuu… Something just doesn't sit right with me.{#ch22_l_056}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # コルベール：うーむ、食べる人の立場に立った、
    voice "ch22_c_017"
    c "Hmm, a truly wonderful dish that puts itself in the eater's place, isn't it.{#ch22_c_017}"

    # サイト：（このカレーの感動は、きっと死ぬまで
    s "(I'll never forget the impression this curry made, I think… Not until I die.){#ch22_s_139}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # → next scene 839
    jump ch22_4_scene_839

label ch22_4_scene_839:

    # [BG       stage    image=+21, level=200]
    $ fade_fx("id(21)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：それでは最後に、ミス・タバサの料理です。  [voice 1184]
    voice "ch22_c_018"
    c "Well then, last is Miss Tabitha's dish.{#ch22_c_018}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # キュルケ：ねぇねぇタバサ。
    voice "ch22_k_038"
    k "Hey hey, Tabitha. Just what did you make?{#ch22_k_038}"

    # タバサ：２次発酵。  [voice 15640]
    voice "ch22_t_008"
    t "Second fermentation.{#ch22_t_008}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：ニジハッコウ？
    voice "ch22_l_057"
    l "Second fermentation? What's that? What kind of dish?{#ch22_l_057}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     image=+955, level=160, dir=1A]
    # ハルナ：ひょっとして……！  [voice 2419]
    voice "ch22_ha_022"
    ha "Could it be…!{#ch22_ha_022}"

    # [SE       se0      play=+67]
    # [SPRITE   lay7     hide]
    # [LAYER    lay0     x=64, y=0]
    # タバサ：これ。  [voice 15641]
    voice "ch22_t_009"
    t "This.{#ch22_t_009}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # オスマン：ほほう、パンじゃの！  [voice 4485]
    voice "ch22_o_013"
    o "My, my, it's bread!{#ch22_o_013}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：んー、焼きたてのいい香り！
    voice "ch22_k_039"
    k "Mm, the smell of fresh-baked bread! Let me have one right away!{#ch22_k_039}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：これはっ……。
    voice "ch22_s_140"
    s "This is… This bread is…!{#ch22_s_140}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：やっぱり！
    voice "ch22_ha_023"
    ha "I knew it! This is a copy bread, isn't it!!{#ch22_ha_023}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # ギーシュ：コッペパン？  [voice 1529]
    voice "ch22_g_003"
    g "Copy bread?{#ch22_g_003}"

    # [SPRITE   lay4     image=+555, level=160, dir=1A]
    # ギーシュ：この奇妙なパンのことを彼女が
    voice "ch22_g_004"
    g "If she knows this strange bread, then that must be it—this is bread from another world, right?{#ch22_g_004}"

    # [SPRITE   lay4     x=-96, y=0]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：ああっ、そうだよっ！！
    voice "ch22_s_141"
    s "Ah, that's right!! I never paid attention to the name, but I always ate it. Come to think of it, it's called a copy bread, this is!{#ch22_s_141}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：私達の世界では、ごく当たり前に手に入る
    voice "ch22_ha_024"
    ha "In our world, it's an everyday bread you can get anywhere.{#ch22_ha_024}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：すごいじゃない、タバサっ！
    voice "ch22_k_040"
    k "Amazing, aren't you, Tabitha! How did you find out about this bread?{#ch22_k_040}"

    # [SPRITE   lay6     x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SE       se0      play=+72]
    # タバサ：秘密。  [voice 15642]
    voice "ch22_t_010"
    t "Secret.{#ch22_t_010}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：細かいことは取りあえず置いておいてさ、
    voice "ch22_s_142"
    s "Let's leave the details for later and all eat already!{#ch22_s_142}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：ほら、シエスタも食べてごらんよっ！！  [voice 12238]
    voice "ch22_s_143"
    s "Look, Siesta, you eat some, too!!{#ch22_s_143}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あっ……はいっ！
    voice "ch22_si_060"
    si "Ah… Yes! Then I'll have one.{#ch22_si_060}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：ほうほう、全体的に焼けているにもかかわらず、
    voice "ch22_c_019"
    c "My, my. It's baked all over yet isn't crispy at all, is it?{#ch22_c_019}"

    # [SPRITE   lay9     x=224, y=0]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：なんだかそれにミルクの香りがするわ……。
    voice "ch22_l_058"
    l "And it smells of milk… And it's soft.{#ch22_l_058}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay4     image=+568, level=160, dir=2A]
    # ギーシュ：見た目とは裏腹になんともみずみずしくて
    voice "ch22_g_005"
    g "Contrary to its appearance, it's so juicy, with a faint sweetness spreading in the mouth… Ah, what a sinful bread!{#ch22_g_005}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：これが、サイトさんの世界で食べてるパン……。  [voice 14932]
    voice "ch22_si_061"
    si "This is the bread Saito-san eats in his world…{#ch22_si_061}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：はぐはぐっ。
    voice "ch22_s_144"
    s "Munch munch… Ah, yeah. It's so nostalgic I could cry.{#ch22_s_144}"

    menu:
        "It's tasty, right?{#ch22_4_c_839_1}":
            jump ch22_4_scene_840
        "I ate it as a kid{#ch22_4_c_839_2}":
            jump ch22_4_scene_841
        "I used to leave it{#ch22_4_c_839_3}":
            jump ch22_4_scene_842

label ch22_4_scene_840:

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+21, level=200]
    $ fade_fx("id(21)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：どうだシエスタ、うまいだろ？  [voice 12240]
    voice "ch22_s_145"
    s "How is it, Siesta? Tasty, right?{#ch22_s_145}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：あむあむっ。
    voice "ch22_si_062"
    si "Munch munch. It really is delicious!{#ch22_si_062}"

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：こうして噛んでるだけでとても甘くて、
    voice "ch22_si_063"
    si "Just chewing it like this is so sweet, I can't help smiling…{#ch22_si_063}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：ははっ、そりゃあいいや。  [voice 12241]
    voice "ch22_s_146"
    s "Ha ha, well, that's good.{#ch22_s_146}"

    # → next scene 843
    jump ch22_4_scene_843

label ch22_4_scene_841:

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+21, level=200]
    $ fade_fx("id(21)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ガキの頃からよく食べていたよ。  [voice 12242]
    voice "ch22_s_147"
    s "I've eaten it since I was a kid.{#ch22_s_147}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：こうして、そのまま食べてもおいしいし。
    voice "ch22_s_148"
    s "It's good just like this, and if you make a slit and put jam in it, it's delicious again.{#ch22_s_148}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：それはおいしそうですねっ！  [voice 14935]
    voice "ch22_si_064"
    si "That sounds delicious!{#ch22_si_064}"

    # → next scene 843
    jump ch22_4_scene_843

label ch22_4_scene_842:

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+21, level=200]
    $ fade_fx("id(21)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：昔は、給食にでてきてさ、
    voice "ch22_s_149"
    s "Back then it came with school lunches, and I often left it uneaten. Now I think about it, what a waste.{#ch22_s_149}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：キュウショク？  [voice 14936]
    voice "ch22_si_065"
    si "School lunch?{#ch22_si_065}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：えーと、学校で出る食事みたいなものなんだよ。  [voice 12245]
    voice "ch22_s_150"
    s "Um, it's like a meal they serve at school.{#ch22_s_150}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：こんなに美味しく感じるなんてなぁ……。
    voice "ch22_s_151"
    s "To think it tastes this good now… I suppose it's the taste of memories, after all…{#ch22_s_151}"

    # [SPRITE   lay2     image=+522, level=160, dir=2A]
    # シエスタ：サイトさん……。  [voice 14937]
    voice "ch22_si_066"
    si "Saito-san…{#ch22_si_066}"

    # → next scene 843
    jump ch22_4_scene_843

label ch22_4_scene_843:

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+21, level=200]
    $ fade_fx("id(21)")
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # オスマン：ふむ、これは実に後を引くパンじゃのう？
    voice "ch22_o_014"
    o "Hmm, this bread really leaves you wanting more. Could I have one more, Miss Tabitha?{#ch22_o_014}"

    # [SPRITE   lay10    x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：どうぞ。  [voice 15643]
    voice "ch22_t_011"
    t "Here.{#ch22_t_011}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    lay0     hide]
    # [SPRITE   lay10    hide]
    # [BG       stage    hide]
    # → next scene 844
    jump ch22_4_scene_844

label ch22_4_scene_844:

    # [BG       stage    image=+21, level=200]
    $ fade_fx("id(21)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # コルベール：優勝者は……。
    voice "ch22_c_020"
    c "The winner is… What shall we do, Old Osmond?{#ch22_c_020}"

    # オスマン：そうじゃな……。  [voice 4487]
    voice "ch22_o_015"
    o "Hmm, yes…{#ch22_o_015}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay10    x=64, y=0]
    # オスマン：今日は手料理を通じて、
    voice "ch22_o_016"
    o "Today was a good opportunity to learn the importance of 'sincerity' through home cooking.{#ch22_o_016}"

    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # オスマン：目的はどうあれ、今回の主賓であるサイトくん
    voice "ch22_o_017"
    o "Whatever the purpose, it was wonderful that you all cooked wholeheartedly for Saito-kun, our guest of honor.{#ch22_o_017}"

    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：このたび腕を競い合った５人の若人は、
    voice "ch22_o_018"
    o "The five young people who competed today are all winners—no, I wouldn't be overstating it.{#ch22_o_018}"

    # [SPRITE   lay10    x=224, y=0]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：失礼ながら、オールド・オスマン。
    voice "ch22_k_041"
    k "Begging your pardon, Old Osmond. Such an ambiguous result doesn't satisfy me. I think it's important to make things clear-cut.{#ch22_k_041}"

    # オスマン：ふうむ。  [voice 4491]
    voice "ch22_o_019"
    o "Hmm.{#ch22_o_019}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：では、審査員で、美味しかった料理に
    voice "ch22_c_021"
    c "Then how about this: let the judges vote for the dish they found delicious, and decide the winner by that?{#ch22_c_021}"

    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # オスマン：そうじゃな。
    voice "ch22_o_020"
    o "Yes. Deciding a winner is fine.{#ch22_o_020}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay10    hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+89, level=200]
    $ fade_fx("id(89)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # コルベール：集計が終わりました。
    voice "ch22_c_022"
    c "The count is complete. I'll announce the results.{#ch22_c_022}"

    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+21, level=200]
    $ fade_fx("id(21)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：優勝者は……。  [voice 1189]
    voice "ch22_c_023"
    c "The winner is…{#ch22_c_023}"

    # コルベール：……。
    c "…{#ch22_c_024}"

    # サイト：（だ、誰に決まったんだ……？）
    s "(W-Who won…?){#ch22_s_152}"

    # [SPRITE   lay9     image=+933, level=160, dir=1A]
    # コルベール：優勝者はっ！  [voice 1190]
    voice "ch22_c_025"
    c "The winner is!{#ch22_c_025}"

    # [SPRITE   lay9     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ミスタ・コルベール！
    voice "ch22_l_059"
    l "Mr. Colbert! Begging your pardon, but that pause is far too long!{#ch22_l_059}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # コルベール：おや、これは失礼。
    voice "ch22_c_026"
    c "Oh, my apologies. Then, I'll announce it.{#ch22_c_026}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：優勝は、カレーシチューを作った、
    voice "ch22_c_027"
    c "The winner is Siesta, who made the curry stew!!{#ch22_c_027}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay9     hide]
    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # シエスタ：……。  [voice 14938]
    voice "ch22_si_067"
    si "…{#ch22_si_067}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：やったね、シエスタ。
    voice "ch22_s_153"
    s "Yay, Siesta. Congratulations!!{#ch22_s_153}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あ、はい……！  [voice 14939]
    voice "ch22_si_068"
    si "A-Ah… Yes!{#ch22_si_068}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：サイトさん……。  [voice 14940]
    voice "ch22_si_069"
    si "Saito-san…{#ch22_si_069}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：どうしたの、シエスタ。
    voice "ch22_s_154"
    s "What's wrong, Siesta? You won—you should be happier.{#ch22_s_154}"

    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：あのっ！  [voice 14941]
    voice "ch22_si_070"
    si "Um!{#ch22_si_070}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：ん？
    voice "ch22_s_155"
    s "Hmm? What is it?{#ch22_s_155}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：サイトさんは……。
    voice "ch22_si_071"
    si "Saito-san… Which dish did you think was the most delicious…?{#ch22_si_071}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：え？  [voice 12250]
    voice "ch22_s_156"
    s "Eh?{#ch22_s_156}"

    menu:
        "Of course, curry{#ch22_4_c_844_1}":
            jump ch22_4_scene_845
        "The copy bread{#ch22_4_c_844_2}":
            jump ch22_4_scene_846
        "Everything was tasty{#ch22_4_c_844_3}":
            jump ch22_4_scene_847

label ch22_4_scene_845:

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [BG       stage    image=+21, level=200]
    $ fade_fx("id(21)")
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：もちろん、カレーが一番美味かったよ。
    voice "ch22_s_157"
    s "Of course, the curry was the best. Siesta's curry.{#ch22_s_157}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：そうですか？  [voice 14943]
    voice "ch22_si_072"
    si "Is that so?{#ch22_si_072}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：……？
    voice "ch22_s_158"
    s "…? What's wrong?{#ch22_s_158}"

    # → next scene 848
    jump ch22_4_scene_848

label ch22_4_scene_846:

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [BG       stage    image=+21, level=200]
    $ fade_fx("id(21)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：ううーん、
    voice "ch22_s_159"
    s "Uggh… I'm torn between it and the curry… but I'd go with the copy bread here.{#ch22_s_159}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：……やっぱり、そうですか。  [voice 14944]
    voice "ch22_si_073"
    si "…I thought so, didn't I.{#ch22_si_073}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：シエスタ？
    voice "ch22_s_160"
    s "Siesta? What's wrong?{#ch22_s_160}"

    # → next scene 848
    jump ch22_4_scene_848

label ch22_4_scene_847:

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [BG       stage    image=+21, level=200]
    $ fade_fx("id(21)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：いやいや、はじめはびくびくしていたけど、
    voice "ch22_s_161"
    s "No no, I was nervous at first, but everyone's cooking was great.{#ch22_s_161}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：（キュルケのは料理なのか微妙だけど……。
    s "(Kirche's was questionable as cooking, but… I can't say that out loud.){#ch22_s_162}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：……。  [voice 14945]
    voice "ch22_si_074"
    si "…{#ch22_si_074}"

    # → next scene 848
    jump ch22_4_scene_848

label ch22_4_scene_848:

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [BG       stage    image=+21, level=200]
    $ fade_fx("id(21)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：シエスタ、どうしたの？
    voice "ch22_s_163"
    s "Siesta, what's wrong? Why that face?{#ch22_s_163}"

    # シエスタ：サイトさん。  [voice 14946]
    voice "ch22_si_075"
    si "Saito-san.{#ch22_si_075}"

    # サイト：はいっ！？  [voice 12257]
    voice "ch22_s_164"
    s "Yes!?{#ch22_s_164}"

    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：ゴメンなさいっ！！
    voice "ch22_si_076"
    si "I'm sorry!! I can't be your servant, Saito-san!!{#ch22_si_076}"

    # サイト：え？  [voice 12258]
    voice "ch22_s_165"
    s "Eh?{#ch22_s_165}"

    # サイト：（そういや、思い出した。
    s "(Ah, right, I remember. She said if she won the cooking contest, she'd become my maid.){#ch22_s_166}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：シエスタさん、どうしてなの？
    voice "ch22_ha_025"
    ha "Siesta, why? You tried so hard in the contest.{#ch22_ha_025}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # シエスタ：ホントにごめんなさい。
    voice "ch22_si_077"
    si "I'm truly sorry. But I…{#ch22_si_077}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：ミス・タバサが作った、コッペパンを
    voice "ch22_si_078"
    si "I realized it when I saw you eating the copy bread Miss Tabitha made.{#ch22_si_078}"

    # [SPRITE   lay2     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：気付いたって、何に？  [voice 6662]
    voice "ch22_l_060"
    l "Realized what?{#ch22_l_060}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：わたし、サイトさんのために、
    voice "ch22_si_079"
    si "I tried my hardest for you, Saito-san, I really did.{#ch22_si_079}"

    # シエスタ：でも、サイトさんの事をもっと深く理解して
    voice "ch22_si_080"
    si "But if I understood you more deeply, I'd surely have prepared a dish even more familiar than the copy bread!{#ch22_si_080}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：確かに、料理大会では優勝しました。
    voice "ch22_si_081"
    si "True, I won the cooking contest. But that alone wasn't enough…{#ch22_si_081}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：そんなことないよ、シエスタっ！！
    voice "ch22_s_167"
    s "That's not true, Siesta!! Your curry was just as delicious!{#ch22_s_167}"

    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：同じくらいじゃ、だめなんですっ！  [voice 14953]
    voice "ch22_si_082"
    si "'Just as' isn't good enough!{#ch22_si_082}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：おお！？  [voice 12260]
    voice "ch22_s_168"
    s "Ooh!?{#ch22_s_168}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：なんだかシエスタさんの気持ち……。
    voice "ch22_ha_026"
    ha "I think I understand Siesta's feelings… a little.{#ch22_ha_026}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     x=64, y=0]
    # シエスタ：この世界……いえ、サイトさんの世界にいても、
    voice "ch22_si_083"
    si "In this world—no, even in your world, I'm the one who knows Saito-san best!{#ch22_si_083}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：そう思えるようになるまで、
    voice "ch22_si_084"
    si "I realized I need to train until I can say that confidently.{#ch22_si_084}"

    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # シエスタ：ですから、わたし。
    voice "ch22_si_085"
    si "So I've decided to go back to being the academy's maid! To understand people's feelings better…{#ch22_si_085}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：シエスタ……。  [voice 12261]
    voice "ch22_s_169"
    s "Siesta…{#ch22_s_169}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：それに、これ以上、ミス・ヴァリエールに
    voice "ch22_si_086"
    si "Besides, I can't keep causing Miss Valliere trouble any longer.{#ch22_si_086}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：分かったわ。
    voice "ch22_l_061"
    l "I understand. Do as you like.{#ch22_l_061}"

    # ルイズ：理由はどうあれ、シエスタがそうしたいと
    voice "ch22_l_062"
    l "Whatever the reason, if Siesta wants it, I can't stop her.{#ch22_l_062}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：……はい。
    voice "ch22_si_087"
    si "…Yes. It was a short time, but thank you for everything.{#ch22_si_087}"

    # サイト：（こ、これで一件落着なのかなぁ）
    s "(S-So, that wraps this up, I guess…){#ch22_s_170}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：一件落着。  [voice 15644]
    voice "ch22_t_012"
    t "Case closed.{#ch22_t_012}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ЧАСТИ 4 ====
    jump ch22_5
    return

