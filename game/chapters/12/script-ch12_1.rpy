# Глава 12, часть 1 (сцены 510–524): «もう一人のハルナ» — война, дворец, Акина.
# Источник: ps2_source/chapters/chapter_13_もう一人のハルナ.txt (SCENE 510-524).
# Голоса: ch12_<spk>_<NNN>, сквозная нумерация части.

label ch12:
    $ tndl(None)
    call overlay_screen("overlay", "Chapter Twelve: 'Another Haruna'{#ch12_title}", isUseBlur=False, text_mode="black") from _call_overlay_screen_19
    pause(2)
    $ show_sprites()

label ch12_1_scene_510:

    # [TITLE title("もう一人のハルナ")]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1172, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：な、なんだ？
    voice "ch12_s_001"
    s "W-What? Louise, did you cast a spell!?{#ch12_s_001}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：違うわよ！
    voice "ch12_l_001"
    l "No! How rude! The explosion was outside!{#ch12_l_001}"

    # [SE       se0      play=+82]
    # [SE       se0      play=+82]
    # [SE       se0      play=+82]
    # [SE       se0      play=+82]
    # null：ドンドンドン！！！
    th "Bang, bang, bang!!!{#ch12_th_001}"

    # 宿の主人：お、お客さん！
    voice "ch12_innkeeper_001"
    innkeeper "C-Customers! It's war! The war has started!{#ch12_innkeeper_001}"

    # 宿の主人：爆発やらなにやらだけじゃねえ、
    voice "ch12_innkeeper_002"
    innkeeper "It's not just explosions—Reconquista soldiers are swarming through the streets!{#ch12_innkeeper_002}"

    # ルイズ：な、なんですって！
    voice "ch12_l_002"
    l "W-What!? Why would Reconquista soldiers be here!?{#ch12_l_002}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：と、とにかく、宿にいてもはじまらないわ。
    voice "ch12_l_003"
    l "A-Anyway, staying at the inn won't help. Let's go to the castle!{#ch12_l_003}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：お、おうっ！
    voice "ch12_s_002"
    s "O-Okay! Let's head for the castle!{#ch12_s_002}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：なんか、生返事よ。
    voice "ch12_l_004"
    l "You answered a bit too slowly. You're worried about Haruna, aren't you?{#ch12_l_004}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：な、何を言うんだよ！
    voice "ch12_s_003"
    s "W-What are you talking about! That's… never mind.{#ch12_s_003}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ふん、ウソおっしゃい！
    voice "ch12_l_005"
    l "Hmph, don't lie to me! You hesitated before answering.{#ch12_l_005}"

    # ルイズ：ご主人様にウソをつくと、おしおきよ！  [voice 7226]
    voice "ch12_l_006"
    l "Lie to your mistress and you'll be punished!{#ch12_l_006}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ご、ごめんなしゃい。  [voice 13312]
    voice "ch12_s_004"
    s "S-Sorry about that…{#ch12_s_004}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：いいわ。
    voice "ch12_l_007"
    l "Fine. You may go save Haruna. I'll allow it, specially.{#ch12_l_007}"

    # サイト：……。
    s "…{#ch12_s_005}"

    menu:
        "…All right. I owe you one.{#ch12_1_c_510_1}":
            jump ch12_1_scene_511
        "But what about Louise!?{#ch12_1_c_510_2}":
            jump ch12_1_scene_512
        "T-That's easy for you to say!{#ch12_1_c_510_3}":
            jump ch12_1_scene_513

label ch12_1_scene_511:

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：分かった。
    voice "ch12_s_006"
    s "I understand. I owe you one.{#ch12_s_006}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：バカ犬のクセに格好をつけるんじゃないわよ！  [voice 7228]
    voice "ch12_l_008"
    l "Don't act cool just because you're a stupid dog!{#ch12_l_008}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そんな身勝手な……。  [voice 13314]
    voice "ch12_s_007"
    s "That's so selfish…{#ch12_s_007}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：ほら、なにグズグズしてるの！
    voice "ch12_l_009"
    l "Come on, what are you dawdling for! Go already.{#ch12_l_009}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 515
    jump ch12_1_scene_515

label ch12_1_scene_512:

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：でも、ルイズは……。  [voice 13315]
    voice "ch12_s_008"
    s "But Louise…{#ch12_s_008}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：むっ、バカにしないでよね！
    voice "ch12_l_010"
    l "Hmph, don't underestimate me! I, the third daughter of the La Vallière family…{#ch12_l_010}"

    # ルイズ：そうやすやすと戦場で遅れをとるハズ
    voice "ch12_l_011"
    l "There's no way I'd fall behind on the battlefield!{#ch12_l_011}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：分かった。
    voice "ch12_s_009"
    s "All right. Be careful!{#ch12_s_009}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：大きなお世話よ！
    voice "ch12_l_012"
    l "Don't tell me what to do! You be careful!{#ch12_l_012}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 515
    jump ch12_1_scene_515

label ch12_1_scene_513:

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そ、そんなこといわれても！  [voice 13317]
    voice "ch12_s_010"
    s "T-That's not something you can just tell me!{#ch12_s_010}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：じゃあ、命令。
    voice "ch12_l_013"
    l "Then I command you. A mistress's order is absolute!{#ch12_l_013}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：サー・イエッサー！
    voice "ch12_s_011"
    s "Sir, yes sir! This stupid dog of yours is off to rescue Haruna, sir!{#ch12_s_011}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：よろしい、とっとと行きなさい！  [voice 7234]
    voice "ch12_l_014"
    l "Good. Now get going!{#ch12_l_014}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 515
    jump ch12_1_scene_515

label ch12_1_scene_514:

    # [SPRITE   lay1     image=+335, level=156, dir=2A]
    # [SPRITE   lay5     image=+429, level=157, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 515
    jump ch12_1_scene_515

label ch12_1_scene_515:

    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：（とりあえず探すなら劇場からか……）
    s "(I guess the theater's the first place to look…){#ch12_s_012}"

    # サイト：（無事でいてくれよ！）
    s "(Please be safe!){#ch12_s_013}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：はぁ、はぁはぁ……。  [voice 13319]
    voice "ch12_s_014"
    s "Haa, haa haa…{#ch12_s_014}"

    # サイト：（ちくしょう、あと少しで劇場なのに……）
    s "(Damn, I was so close to the theater…){#ch12_s_015}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay14    image=+1111, level=160, dir=1A]
    # [SPRITE   lay22    image=+1111, level=160, dir=1A]
    # 敵兵士ＥＳ：……！  [voice 1407]
    voice "ch12_es_001"
    es "…{#ch12_es_001}"

    # [SPRITE   lay14    hide]
    # [SPRITE   lay22    hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：くそっ、宿の親父が言ってた
    voice "ch12_s_016"
    s "Damn, so these are the Reconquista soldiers the innkeeper was talking about!{#ch12_s_016}"

    # [SE       se0      play=+65]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay5     image=+472, level=140, dir=3B]
    # サイト：てめえらそこをどけぇぇぇっ！  [voice 13321]
    voice "ch12_s_017"
    s "Get out of my wayyy!{#ch12_s_017}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 516
    jump ch12_1_scene_516

label ch12_1_scene_516:

    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay15    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay15    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ゲホゲホ、王宮近くまで砲撃ですって！  [voice 7235]
    voice "ch12_l_015"
    l "Cough, cough—shells falling near the palace!?{#ch12_l_015}"

    # ルイズ：冗談じゃないわよ。
    voice "ch12_l_016"
    l "This is ridiculous! Why is the shelling reaching all the way here!? They couldn't possibly reach from outside the capital!{#ch12_l_016}"

    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay15    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay15    hide, reset]
    # [SPRITE   lay1     reset]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay15    image=+1116, level=160, dir=1A]
    # 味方Ａ：止まれ。
    voice "ch12_soldier_001"
    soldier "Halt. This is the palace!{#ch12_soldier_001}"

    # [SPRITE   lay15    x=160, y=0]
    # [SPRITE   lay15    level=157]
    # [SPRITE   lay1     image=+302, level=156, dir=1A]
    # ルイズ：緊急事態よ。
    voice "ch12_l_017"
    l "It's an emergency. I need to see the Queen immediately…{#ch12_l_017}"

    # [SPRITE   lay15    image=+1116, level=157, dir=1A]
    # 味方Ａ：魔法学院の生徒風情が直接謁見を求めるなどと！
    voice "ch12_soldier_002"
    soldier "A mere academy student demanding an audience! Follow the proper procedure.{#ch12_soldier_002}"

    # [SPRITE   lay1     image=+306, level=156, dir=1A]
    # ルイズ：な、なんですって！
    voice "ch12_l_018"
    l "W-What!? Can't you see what's happening!?{#ch12_l_018}"

    # 味方Ａ：この状況であるからこそ、
    voice "ch12_soldier_003"
    soldier "Precisely because of the situation, we are on high alert!{#ch12_soldier_003}"

    # [SPRITE   lay15    image=+1114, level=157, dir=1A]
    # 味方Ａ：我々の任務は融通を利かせることではなく、
    voice "ch12_soldier_004"
    soldier "Our duty is not to be flexible, but to enforce the rules.{#ch12_soldier_004}"

    # [SE       se0      play=+64]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay15    vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay15    reset]
    # [SPRITE   lay1     reset]
    # [SPRITE   lay15    image=+1116, level=157, dir=1A]
    # 味方Ａ：うわぁっ！  [voice 4271]
    voice "ch12_soldier_005"
    soldier "Wah!{#ch12_soldier_005}"

    # ルイズ：きゃあ！  [voice 7239]
    voice "ch12_l_019"
    l "Eek!{#ch12_l_019}"

    # [SPRITE   lay1     image=+339, level=156, dir=2A]
    # ルイズ：魔法学院の生徒というのが不満なんだったら、
    voice "ch12_l_020"
    l "If being an academy student bothers you, I'll give you my name!{#ch12_l_020}"

    # [SPRITE   lay1     image=+302, level=156, dir=1A]
    # ルイズ：ラ・ヴァリエール公爵が三女、
    voice "ch12_l_021"
    l "Third daughter of Duke La Vallière, Louise Francoise.{#ch12_l_021}"

    # ルイズ：女王陛下ご下命の件につき、
    voice "ch12_l_022"
    l "I've come on urgent business concerning the Queen's order. …Well? Happy now?{#ch12_l_022}"

    # [SPRITE   lay15    image=+1118, level=157, dir=1A]
    # 味方Ａ：ラ・ヴァリエール家の……。
    voice "ch12_soldier_006"
    soldier "Of the La Vallière family… I-I apologize.{#ch12_soldier_006}"

    # 味方Ａ：女王陛下ご下命の件とは、し、しかし……。  [voice 4273]
    voice "ch12_soldier_007"
    soldier "About the Queen's order, well, however…{#ch12_soldier_007}"

    # [SPRITE   lay1     image=+306, level=156, dir=1A]
    # ルイズ：早く取り次ぎなさい！
    voice "ch12_l_023"
    l "Announce me at once! You do realize this is an emergency! Can't you see the shelling and the fires in the city!?{#ch12_l_023}"

    # [SPRITE   lay15    image=+1114, level=157, dir=1A]
    # 味方Ａ：し、しばらくお待ちください！  [voice 4274]
    voice "ch12_soldier_008"
    soldier "P-Please wait a moment!{#ch12_soldier_008}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 517
    jump ch12_1_scene_517

label ch12_1_scene_517:

    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay15    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay8     vibrate=14]
    # [SPRITE   lay18    vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay15    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay8     hide, reset]
    # [SPRITE   lay18    hide, reset]
    # [SPRITE   lay15    image=+1116, level=157, dir=1A]
    # 味方Ａ：報告します。  [voice 4275]
    voice "ch12_soldier_009"
    soldier "Reporting.{#ch12_soldier_009}"

    # [SPRITE   lay15    image=+1114, level=157, dir=1A]
    # 味方Ａ：ラ・ヴェリエール公爵家三女、
    voice "ch12_soldier_010"
    soldier "Third daughter of Duke La Vallière, Louise Francoise.{#ch12_soldier_010}"

    # 味方Ａ：女王陛下へのお取り次ぎを
    voice "ch12_soldier_011"
    soldier "She requests an audience with Her Majesty.{#ch12_soldier_011}"

    # [SPRITE   lay15    level=160]
    # [SPRITE   lay8     image=+766, level=155, dir=1A]
    # アンリエッタ：ルイズが？
    voice "ch12_h_001"
    h "Louise? So you came to Tristain. Show her in at once.{#ch12_h_001}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay8     level=154]
    # [SPRITE   lay18    image=+1121, level=160, dir=1A]
    # 将校：陛下、部外者を入れては……。  [voice 4339]
    voice "ch12_commander_001"
    commander "Your Majesty, an outsider cannot…{#ch12_commander_001}"

    # [SPRITE   lay8     image=+764, level=154, dir=1A]
    # アンリエッタ：かまいません。  [voice 720]
    voice "ch12_h_002"
    h "It's all right.{#ch12_h_002}"

    # アンリエッタ：わたくしが、爆弾使いについて調べさせていた
    voice "ch12_h_003"
    h "These are the people I had investigating the bomb-thrower. They may have an important report.{#ch12_h_003}"

    # [SPRITE   lay8     image=+766, level=154, dir=1A]
    # アンリエッタ：それに、この状況下では百万の味方にも
    voice "ch12_h_004"
    h "Besides, in this situation they're worth a million allies.{#ch12_h_004}"

    # [SPRITE   lay18    image=+1125, level=160, dir=1A]
    # 将校：陛下？  [voice 4340]
    voice "ch12_commander_002"
    commander "Your Majesty?{#ch12_commander_002}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay18    hide]
    # [BG       stage    hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+304, level=155, dir=1A]
    # ルイズ：姫さま……あっ！  [voice 7244]
    voice "ch12_l_024"
    l "Your Highness… Ah!{#ch12_l_024}"

    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：ラ・ヴァリエール家三女
    voice "ch12_l_025"
    l "Third daughter of the La Vallière family, Louise Francoise, at your service.{#ch12_l_025}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay8     image=+764, level=154, dir=1A]
    # アンリエッタ：よく来てくれました、ルイズ……。
    voice "ch12_h_005"
    h "You came, Louise… Oh, where is your familiar?{#ch12_h_005}"

    # ルイズ：あ、はい。
    voice "ch12_l_026"
    l "Ah, yes. Saito went into the city to save Haruna.{#ch12_l_026}"

    # アンリエッタ：ハルナですか？  [voice 724]
    voice "ch12_h_006"
    h "Haruna?{#ch12_h_006}"

    # ルイズ：はい。  [voice 7247]
    voice "ch12_l_027"
    l "Yes.{#ch12_l_027}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay18    image=+1123, level=160, dir=1A]
    # 将校：この場は正式の軍議の場です。
    voice "ch12_commander_003"
    commander "This is a formal war council. Please refrain from idle chatter.{#ch12_commander_003}"

    # [SPRITE   lay1     image=+308, level=155, dir=1A]
    # ルイズ：うっ。
    voice "ch12_l_028"
    l "Oops. I'm sorry.{#ch12_l_028}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay18    hide]
    # [SPRITE   lay8     image=+770, level=154, dir=1A]
    # アンリエッタ：分かりました。
    voice "ch12_h_007"
    h "Understood. Then continue the report…{#ch12_h_007}"

    # [SPRITE   lay8     x=224, y=0]
    # [SPRITE   lay18    image=+1121, level=160, dir=1A]
    # 将校：はっ。  [voice 4342]
    voice "ch12_commander_004"
    commander "Yes, ma'am.{#ch12_commander_004}"

    # 将校：現在、中央市場の炎上を皮切りに、
    voice "ch12_commander_005"
    commander "At present, starting with the fire at the central market, buildings and bridges have been bombed all over the city…{#ch12_commander_005}"

    # 将校：その後も、市内各地に隠匿されていたと思われる
    voice "ch12_commander_006"
    commander "Since then, continuous shelling of the palace has been confirmed from cannon sites hidden around the city.{#ch12_commander_006}"

    # [SPRITE   lay8     image=+768, level=154, dir=1A]
    # アンリエッタ：市内に砲台とはどういうことです？
    voice "ch12_h_008"
    h "Cannons inside the city? How could they…!{#ch12_h_008}"

    # 将校：降伏した敵兵を尋問したところ、
    voice "ch12_commander_007"
    commander "We questioned a captured soldier. They used the recent bombings to…{#ch12_commander_007}"

    # 将校：レコン・キスタが修復作業の職人に
    voice "ch12_commander_008"
    commander "Reconquista sent soldiers into the country disguised as repair workers.{#ch12_commander_008}"

    # [SPRITE   lay18    image=+1125, level=160, dir=1A]
    # 将校：それに併せ、現場の修復に紛れ込み
    voice "ch12_commander_009"
    commander "At the same time, they slipped in among the repair crews and installed many small cannons.{#ch12_commander_009}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：なんですって！  [voice 7249]
    voice "ch12_l_029"
    l "What!?{#ch12_l_029}"

    # [SPRITE   lay18    image=+1123, level=160, dir=1A]
    # 将校：軍議に加わるもの以外の発言は控えられよ。  [voice 4348]
    voice "ch12_commander_010"
    commander "Only those on the council may speak.{#ch12_commander_010}"

    # [SPRITE   lay1     image=+308, level=155, dir=1A]
    # ルイズ：……。  [voice 7250]
    voice "ch12_l_030"
    l "…{#ch12_l_030}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     image=+768, level=154, dir=1A]
    # アンリエッタ：爆破事件の資料と市街の地図を。  [voice 727]
    voice "ch12_h_009"
    h "The records on the bombings and a map of the city.{#ch12_h_009}"

    # [SPRITE   lay18    image=+1121, level=160, dir=1A]
    # 将校：はっ！  [voice 4349]
    voice "ch12_commander_011"
    commander "Yes!{#ch12_commander_011}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay18    hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+259, level=80]
    $ dissolve_fx("id(259)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：……。  [voice 7251]
    voice "ch12_l_031"
    l "…{#ch12_l_031}"

    # アンリエッタ：こ、これは……。  [voice 728]
    voice "ch12_h_010"
    h "T-This is…!{#ch12_h_010}"

    # 将校：はい。
    voice "ch12_commander_012"
    commander "Yes. The bombings were set at the positions best suited to shelling the palace.{#ch12_commander_012}"

    # 将校：見事なものです。
    voice "ch12_commander_013"
    commander "Remarkable. The bomb-thrower wasn't striking blindly—every incident was calculated.{#ch12_commander_013}"

    # アンリエッタ：発言を慎みなさい。  [voice 729]
    voice "ch12_h_011"
    h "Refrain from such remarks.{#ch12_h_011}"

    # アンリエッタ：このような卑怯な手段をとる敵への賞賛は
    voice "ch12_h_012"
    h "Praising an enemy who uses such cowardly means is unbecoming.{#ch12_h_012}"

    # 将校：失礼しました。
    voice "ch12_commander_014"
    commander "My apologies. Your Majesty.{#ch12_commander_014}"

    # アンリエッタ：不覚でした。
    voice "ch12_h_013"
    h "We were careless. I had no idea things had gone this far.{#ch12_h_013}"

    # アンリエッタ：爆弾使いの事件は、敵の単なる第一手に
    voice "ch12_h_014"
    h "So the bomb-thrower's attacks were merely the enemy's first move, weren't they?{#ch12_h_014}"

    # 将校：トリスタニア市街では潜入していた敵兵が
    voice "ch12_commander_015"
    commander "In the city, the infiltrated enemy soldiers have begun to move and large-scale street fighting is breaking out.{#ch12_commander_015}"

    # ルイズ：……。  [voice 7252]
    voice "ch12_l_032"
    l "…{#ch12_l_032}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay8     hide]
    # [SPRITE   lay18    hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # → next scene 518
    jump ch12_1_scene_518

label ch12_1_scene_518:

    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：はぁはぁはぁ。
    voice "ch12_s_018"
    s "Haa haa haa… It took longer than I thought.{#ch12_s_018}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：（……いた！
    s "(There she is! Haruna!){#ch12_s_019}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：会いたかった……。  [voice 2612]
    voice "ch12_ha_001"
    ha "I wanted to see you…{#ch12_ha_001}"

    # [SPRITE   lay7     x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：……えっ！  [voice 13323]
    voice "ch12_s_020"
    s "…Eh!?{#ch12_s_020}"

    # → next scene 519
    jump ch12_1_scene_519

    # checkKiss(): ветка 519/520. Флаг поцелуя не портирован — идём по ветке без поцелуя (520).
label ch12_1_scene_519:

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+276, level=80]
    $ dissolve_fx("id(276)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+17]
    play music t16 fadein 1.0
    # ハルナ：うふふっ……。  [voice 2613]
    voice "ch12_ha_002"
    ha "Ufufu…{#ch12_ha_002}"

    # サイト：な、ななななな……。  [voice 13324]
    voice "ch12_s_021"
    s "W-Wh-wh-wh-wh…{#ch12_s_021}"

    # サイト：（い、いま俺の唇に触れているのは、
    s "(The one touching my lips right now—could it be…){#ch12_s_022}"

    # ハルナ：ねぇ、サイト……。  [voice 2614]
    voice "ch12_ha_003"
    ha "Hey, Saito…{#ch12_ha_003}"

    # サイト：（……！）
    s "(…!){#ch12_s_023}"

    # サイト：（……違う！
    s "(…No! This isn't Haruna!){#ch12_s_024}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：うふふ。
    voice "ch12_ha_004"
    ha "Ufufu. Oh, Saito, what's wrong?{#ch12_ha_004}"

    # [SPRITE   lay7     image=+955, level=160, dir=1A]
    # ハルナ：恥ずかしがらなくてもいいじゃない？  [voice 2616]
    voice "ch12_ha_005"
    ha "You don't have to be shy, you know?{#ch12_ha_005}"

    # [SPRITE   lay7     x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：お前、誰だ？  [voice 13325]
    voice "ch12_s_025"
    s "Who are you?{#ch12_s_025}"

    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：あら、よく分かったわね？  [voice 2617]
    voice "ch12_ha_006"
    ha "My, you figured it out?{#ch12_ha_006}"

    # → next scene 521
    jump ch12_1_scene_521

label ch12_1_scene_520:

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：うふふ。
    voice "ch12_ha_007"
    ha "Ufufu. You figured it out, didn't you?{#ch12_ha_007}"

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：やっぱり
    voice "ch12_ha_008"
    ha "I wonder… am I really so different from Haruna?{#ch12_ha_008}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：……へ？  [voice 13326]
    voice "ch12_s_026"
    s "…Huh?{#ch12_s_026}"

    # → next scene 521
    jump ch12_1_scene_521

label ch12_1_scene_521:

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # アキナ：あたしはアキナ……。  [voice 198]
    voice "ch12_ak_001"
    ak "I am Akina…{#ch12_ak_001}"

    # アキナ：ウェザリー様に作っていただいた、
    voice "ch12_ak_002"
    ak "A new personality made for me by Weatherly-sama. Fufu, fufufufu…{#ch12_ak_002}"

    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：そして、おまえ達が『爆弾使い』って呼んで
    voice "ch12_ak_003"
    ak "And I'm the one you all called the 'bomb-thrower' and hunted everywhere!{#ch12_ak_003}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：あはははははははははは！  [voice 201]
    voice "ch12_ak_004"
    ak "Ahahahahahahaha!{#ch12_ak_004}"

    menu:
        "Cut the joke!{#ch12_1_c_521_1}":
            jump ch12_1_scene_522
        "Tell me you're lying, Haruna!{#ch12_1_c_521_2}":
            jump ch12_1_scene_523
        "I don't believe it!{#ch12_1_c_521_3}":
            jump ch12_1_scene_524

label ch12_1_scene_522:

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：じょ、冗談はよせよ。
    voice "ch12_s_027"
    s "J-Joke… I can't laugh at this, Haruna.{#ch12_s_027}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：冗談？
    voice "ch12_ak_005"
    ak "A joke? Ahahaha… Are you an idiot?{#ch12_ak_005}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：現実をしっかり見たら？
    voice "ch12_ak_006"
    ak "How about looking reality in the eye? Saito…{#ch12_ak_006}"

    # → next scene 525
    jump ch12_2

label ch12_1_scene_523:

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：う、嘘だといってくれよ、春奈！  [voice 13328]
    voice "ch12_s_028"
    s "T-Tell me you're lying, Haruna!{#ch12_s_028}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：嘘だといったらこの現実は変わるの？
    voice "ch12_ak_007"
    ak "If I said it was a lie, would this reality change? Then I'd say it a hundred times. I am Akina.{#ch12_ak_007}"

    # → next scene 525
    jump ch12_2

label ch12_1_scene_524:

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：俺は信じない。
    voice "ch12_s_029"
    s "I don't believe it. That the bomb-thrower was Haruna!{#ch12_s_029}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：じゃあ、信じなければいいじゃない。  [voice 205]
    voice "ch12_ak_008"
    ak "Then simply don't believe it.{#ch12_ak_008}"

    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：爆弾使いはアキナで、ハルナは何も知らない
    voice "ch12_ak_009"
    ak "The bomb-thrower is Akina; Haruna is a pure girl who knows nothing. Ugh, it makes me sick.{#ch12_ak_009}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：やめろ、そんな風にいうのは！  [voice 13330]
    voice "ch12_s_030"
    s "Stop! Don't say it like that!{#ch12_s_030}"

    # アキナ：うるさい。
    voice "ch12_ak_010"
    ak "Shut up. I was made that way!{#ch12_ak_010}"

    # → next scene 525
    jump ch12_2

    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch12_2
    return

