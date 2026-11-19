# Глава 11, часть 4 (сцены 500-509): «ハルナの決意» — продолжение.
# Источник: ps2_source/chapters/chapter_12_ハルナの決意.txt (SCENE 500-509).
# Точные аргументы: ps2_source/events_full/chapter_12_ハルナの決意.txt.
# EN-база в сценарии; JA/RU — в game/tl/{japanese,russian}/ch11_4_*.rpy.
# Голоса: нумерация ch11_<spk>_<NNN> продолжает части 1-2 (общая нумерация главы).

label ch11_4:
    $ tndl(None)
    $ show_sprites()

label ch11_4_scene_500:

    # [BG       stage    image=+59, level=200]
    $ fade_fx("town_square_evening")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [SE       se1      play=+37]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ふぅ、やっとトリスタニアについたな。  [voice 13289]
    voice "ch11_s_097"
    s "Whew, we finally made it to Tristain.{#ch11_s_097}"

    # ルイズ：もう、シャキッとしなさいよね。
    voice "ch11_l_036"
    l "Honestly, snap out of it. Snap!{#ch11_l_036}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：さっきから何怒ってるんだよ。
    voice "ch11_s_098"
    s "Why are you so angry all of a sudden? You've been pouting this whole time.{#ch11_s_098}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：怒ってなんかないわよ！  [voice 7195]
    voice "ch11_l_037"
    l "I'm not angry or anything!{#ch11_l_037}"

    # サイト：ほら、怒ってるじゃないか。  [voice 13291]
    voice "ch11_s_099"
    s "See? You're angry.{#ch11_s_099}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ふんっ！  [voice 7196]
    voice "ch11_l_038"
    l "Hmph!{#ch11_l_038}"

    # サイト：（はぁ……困ったなぁ）
    s "Sigh… What am I going to do?{#ch11_s_100}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：あ！
    voice "ch11_s_101"
    s "Ah! Isn't that Haruna and Weatherly-san? What luck, running into them here!{#ch11_s_101}"

    # サイト：おーい、春奈ー！  [voice 13293]
    voice "ch11_s_102"
    s "Hey! Haruna!{#ch11_s_102}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：……。
    ha "…{#ch11_ha_054}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：春奈？  [voice 13294]
    voice "ch11_s_103"
    s "Haruna?{#ch11_s_103}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay20    image=+1063, level=160, dir=1A]
    # ウェザリー：これはこれは、ミス・ヴァリエールにサイト！
    voice "ch11_w_029"
    w "Well, well. If it isn't Miss Valliere and Saito! What a coincidence, meeting you here.{#ch11_w_029}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：あら、ウェザリー。
    voice "ch11_l_039"
    l "Oh, Weatherly. Just the one we wanted.{#ch11_l_039}"

    # ルイズ：ハルナの忘れ物を届けに来たのよ。  [voice 7198]
    voice "ch11_l_040"
    l "We've come to return something Haruna forgot.{#ch11_l_040}"

    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：あら、それはご丁寧に。  [voice 16107]
    voice "ch11_w_030"
    w "My, how thoughtful of you.{#ch11_w_030}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：……。
    ha "…{#ch11_ha_055}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：この手帳なんだけど。  [voice 13295]
    voice "ch11_s_104"
    s "About this notebook…{#ch11_s_104}"

    # ハルナ：そう、ありがと。  [voice 2611]
    voice "ch11_ha_056"
    ha "Oh, right. Thank you.{#ch11_ha_056}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：（……？）
    s "…?{#ch11_s_105}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（なんだ、この違和感？）
    s "What's this strange feeling?{#ch11_s_106}"

    # サイト：なあ、ウェザリーさん……。
    voice "ch11_s_107"
    s "Say, Weatherly-san… Is something wrong with Haruna?{#ch11_s_107}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：さあ？  [voice 16108]
    voice "ch11_w_031"
    w "Well?{#ch11_w_031}"

    # [SPRITE   lay20    image=+1063, level=160, dir=1A]
    # ウェザリー：あんなに感動的なお別れのあとに
    voice "ch11_w_032"
    w "We met again right after such a moving farewell, so she must be embarrassed.{#ch11_w_032}"

    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：それよりも、いい機会だから少し話を聞かせて
    voice "ch11_w_033"
    w "More than that, since we have a good opportunity, won't you tell me a little about yourself? I'm actually stuck for ideas for my next play.{#ch11_w_033}"

    # ウェザリー：この前は公演の準備で、
    voice "ch11_w_034"
    w "Last time, with the preparations for the performance, we hardly had a chance to talk personally.{#ch11_w_034}"

    # ウェザリー：ハルナから聞いたけど、サイトは凄い剣士で、
    voice "ch11_w_035"
    w "I heard from Haruna that you're a great swordsman, and that you have some mysterious power, don't you?{#ch11_w_035}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：そんなことを話したの！
    voice "ch11_l_041"
    l "You told her such things! That's no good, Haruna!{#ch11_l_041}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：……。
    ha "…{#ch11_ha_057}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：そんなヒーローの生い立ちってどんななの？  [voice 16113]
    voice "ch11_w_036"
    w "So what's the childhood of such a hero like?{#ch11_w_036}"

    menu:
        "That was when I…{#ch11_4_c_500_1}":
            jump ch11_4_scene_501
        "Um, well…{#ch11_4_c_500_2}":
            jump ch11_4_scene_502
        "My adult charm…{#ch11_4_c_500_3}":
            jump ch11_4_scene_503

label ch11_4_scene_501:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [SE       se1      play=+37]
    # [BG       stage    image=+59, level=200]
    $ fade_fx("town_square_evening")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：ええと。
    voice "ch11_s_108"
    s "Um. That was when I…{#ch11_s_108}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：サイト、黙りなさい！
    voice "ch11_l_042"
    l "Saito, be quiet! Don't you dare talk!{#ch11_l_042}"

    # → next scene 504
    jump ch11_4_scene_504

label ch11_4_scene_502:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [SE       se1      play=+37]
    # [BG       stage    image=+59, level=200]
    $ fade_fx("town_square_evening")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ええと。
    voice "ch11_s_109"
    s "Um. You see…{#ch11_s_109}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：サイト！  [voice 7201]
    voice "ch11_l_043"
    l "Saito!{#ch11_l_043}"

    # ルイズ：ごめんなさい。
    voice "ch11_l_044"
    l "I'm sorry. Weatherly, we're not allowed to talk about this.{#ch11_l_044}"

    # ルイズ：あなたがいま知ってることも
    voice "ch11_l_045"
    l "Please don't say aloud what you've just learned.{#ch11_l_045}"

    # → next scene 504
    jump ch11_4_scene_504

label ch11_4_scene_503:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [SE       se1      play=+37]
    # [BG       stage    image=+59, level=200]
    $ fade_fx("town_square_evening")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：（そ、そんなに迫られると、
    s "When she presses me like that, my adult charm…{#ch11_s_110}"

    # [SPRITE   lay5     image=+431, level=160, dir=2A]
    # サイト：（なんだか知っていることを
    s "I feel like I'm about to tell her everything I know…{#ch11_s_111}"

    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # サイト：（ビバ猫耳！
    s "Long live cat ears! Bravo!{#ch11_s_112}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：な、何を考えているのよ！
    voice "ch11_l_046"
    l "W-What are you thinking! Stupid dog!{#ch11_l_046}"

    # → next scene 504
    jump ch11_4_scene_504

label ch11_4_scene_504:

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [SE       se1      play=+37]
    # [BG       stage    image=+59, level=200]
    $ fade_fx("town_square_evening")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay20    image=+1063, level=160, dir=1A]
    # ウェザリー：固いこと言わなくても、いいじゃない？  [voice 16114]
    voice "ch11_w_037"
    w "You don't have to be so formal, you know?{#ch11_w_037}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ち、ちょっとまって！  [voice 7205]
    voice "ch11_l_047"
    l "W-Wait a moment!{#ch11_l_047}"

    # ウェザリー：もちろん、若き天才魔法使いの
    voice "ch11_w_038"
    w "Of course, I'm also interested in the young genius mage, Miss Valliere.{#ch11_w_038}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：あら、それほどでも。
    voice "ch11_l_048"
    l "Oh, I'm not that… I mean, no!{#ch11_l_048}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：と、とにかく！
    voice "ch11_l_049"
    l "A-Anyway! We're tired from traveling, so let's talk another day!{#ch11_l_049}"

    # ルイズ：ほら、宿にいくわよ！
    voice "ch11_l_050"
    l "Come on, we're going to the inn! Stupid dog!{#ch11_l_050}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：急にどうしたんだよ！
    voice "ch11_s_113"
    s "What's gotten into you all of a sudden! Louise!{#ch11_s_113}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：じ、じゃあな……春奈！
    voice "ch11_s_114"
    s "W-Well then… Haruna! See you later!{#ch11_s_114}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：……。
    ha "…{#ch11_ha_058}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # アキナ：あいかわらず馬鹿な奴ら。  [voice 194]
    voice "ch11_ak_002"
    ak "The same stupid fools as ever.{#ch11_ak_002}"

    # [SPRITE   lay20    image=+1063, level=160, dir=1A]
    # ウェザリー：ふふ、勘付かれたかな？  [voice 16116]
    voice "ch11_w_039"
    w "Fufu, did she notice?{#ch11_w_039}"

    # ウェザリー：まあ、全て手遅れだけどね。
    voice "ch11_w_040"
    w "Well, it's too late for all of that now. For those young ladies, at least.{#ch11_w_040}"

    # アキナ：最後に欲張りすぎね。
    voice "ch11_ak_003"
    ak "Don't get greedy at the very end. The final act is about to begin…{#ch11_ak_003}"

    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：アキナはどうなの？
    voice "ch11_w_041"
    w "What about you, Akina? That boy, Saito.{#ch11_w_041}"

    # [SPRITE   lay21    image=+1025, level=160, dir=1A]
    # アキナ：……っ！
    voice "ch11_ak_004"
    ak "…! I don't care about someone so indecisive. Haruna has terrible taste.{#ch11_ak_004}"

    # ウェザリー：いいじゃない。
    voice "ch11_w_042"
    w "What does it matter? Haruna is gone now, anyway.{#ch11_w_042}"

    # アキナ：……。
    ak "…{#ch11_ak_005}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay20    hide]
    # [SPRITE   lay21    hide]
    # [BG       stage    hide]
    # → next scene 505
    jump ch11_4_scene_505

label ch11_4_scene_505:

    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：さっきはどうしたんだよ？
    voice "ch11_s_115"
    s "What was that about? Acting so strange all of a sudden… It's weird.{#ch11_s_115}"

    # ルイズ：あんた、何も気がつかなかったの？  [voice 7209]
    voice "ch11_l_051"
    l "You didn't notice anything?{#ch11_l_051}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：何がさ？  [voice 13302]
    voice "ch11_s_116"
    s "Notice what?{#ch11_s_116}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：あのウェザリーの態度……。
    voice "ch11_l_052"
    l "That Weatherly's attitude… I never noticed before, but now that I think about it, a lot of it is suspicious.{#ch11_l_052}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：どこが？
    voice "ch11_s_117"
    s "Like what? I thought it was an ordinary conversation.{#ch11_s_117}"

    # ルイズ：いきなり街中で会ったのがまず不自然よ。
    voice "ch11_l_053"
    l "First, running into her in the street like that was unnatural. It was as if she knew we were coming.{#ch11_l_053}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：それに、いきなりわたし達を
    voice "ch11_l_054"
    l "And then, prying into our business out of nowhere… It's strange.{#ch11_l_054}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そういえば、春奈もなんか変だったな。
    voice "ch11_s_118"
    s "Now that I think about it, Haruna was acting strange too. The way she looked at me was like I was a stranger…{#ch11_s_118}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：離れてみて、あんたが危険なけだもの
    voice "ch11_l_055"
    l "Maybe now that she's away, she realized what a dangerous beast you are!{#ch11_l_055}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ひ、ひどいっ！  [voice 13305]
    voice "ch11_s_119"
    s "T-That's mean!{#ch11_s_119}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：それは冗談としても。
    voice "ch11_l_056"
    l "Even setting that aside as a joke… something might happen.{#ch11_l_056}"

    menu:
        "What do you mean?{#ch11_4_c_505_1}":
            jump ch11_4_scene_506
        "Aren't you overthinking it?{#ch11_4_c_505_2}":
            jump ch11_4_scene_507
        "What do you want me to do?{#ch11_4_c_505_3}":
            jump ch11_4_scene_508

label ch11_4_scene_506:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なにかが起きる……。
    voice "ch11_s_120"
    s "Something might happen… What do you mean?{#ch11_s_120}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：そんなの分かんないわよ！  [voice 7215]
    voice "ch11_l_057"
    l "How would I know!{#ch11_l_057}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：とりあえず、もう一度明日から調べましょう。  [voice 7216]
    voice "ch11_l_058"
    l "For now, let's investigate again starting tomorrow.{#ch11_l_058}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # 【デートdate】ハルナ → scene 1179 — не портируется (date-гейт, контент в game/chapters/extra/)
    # → next scene 510 (глава 12) — date-ветка 1179 не портирована
    jump ch12
    # 【デートproceed】 → scene 510 — не портируется (date-гейт, контент в game/chapters/extra/)
label ch11_4_scene_507:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：考えすぎなんじゃない？  [voice 13307]
    voice "ch11_s_121"
    s "Aren't you overthinking it?{#ch11_s_121}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：言われてみればそうなんだけど。  [voice 7217]
    voice "ch11_l_059"
    l "When you put it that way, maybe.{#ch11_l_059}"

    # ルイズ：やっぱり、疲れてるのかしら。
    voice "ch11_l_060"
    l "Maybe I'm just tired. I…{#ch11_l_060}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # 【デートdate】ハルナ → scene 1179 — не портируется (date-гейт, контент в game/chapters/extra/)
    # → next scene 510 (глава 12) — date-ветка 1179 не портирована
    jump ch12
    # 【デートproceed】 → scene 510 — не портируется (date-гейт, контент в game/chapters/extra/)
label ch11_4_scene_508:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：それで、どうしろっていうんだよ！  [voice 13308]
    voice "ch11_s_122"
    s "So what do you want me to do?!{#ch11_s_122}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：そんなの分かんないわよ！  [voice 7219]
    voice "ch11_l_061"
    l "How would I know!{#ch11_l_061}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：とりあえず、明日からもう一度地道に
    voice "ch11_l_062"
    l "For now, let's carefully investigate again starting tomorrow.{#ch11_l_062}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # 【デートdate】ハルナ → scene 1179 — не портируется (date-гейт, контент в game/chapters/extra/)
    # → next scene 510 (глава 12) — date-ветка 1179 не портирована
    jump ch12
    # 【デートproceed】 → scene 510 — не портируется (date-гейт, контент в game/chapters/extra/)
label ch11_4_scene_509:

    # [SPRITE   lay1     image=+302, level=156, dir=1A]
    # [SPRITE   lay5     image=+429, level=157, dir=2A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # 【デートdate】ハルナ → scene 1179 — не портируется (date-гейт, контент в game/chapters/extra/)
    # → next scene 510 (глава 12) — date-ветка 1179 не портирована
    jump ch12
    # 【デートproceed】 → scene 510 — не портируется (date-гейт, контент в game/chapters/extra/)
    # ==== КОНЕЦ ГЛАВЫ 11, ЧАСТИ 4 ====
    jump ch12
    return

