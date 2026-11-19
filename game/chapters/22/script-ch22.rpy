# Глава 22, часть 1 (сцены 806–816): утро, кулинарный бой начинается.
# Источник: ps2_source/chapters/chapter_23_料理の鉄人.txt (SCENE 806-816).

label ch22:
    $ tndl(None)
    $ show_sprites(None)

label ch22_1_scene_806:

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
    # シエスタ：サイトさん……。  [voice 14872]
    voice "ch22_si_001"
    si "Saito-san…{#ch22_si_001}"

    # サイト：んん。  [voice 12125]
    voice "ch22_s_001"
    s "Mm.{#ch22_s_001}"

    # シエスタ：サイトさんっ……サイトさん。  [voice 14873]
    voice "ch22_si_002"
    si "Saito-san… Saito-san.{#ch22_si_002}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+215, level=80]
    $ dissolve_fx("id(215)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [SE       se0      play=+69]
    # シエスタ：おはようございます、サイトさん。  [voice 14874]
    voice "ch22_si_003"
    si "Good morning, Saito-san.{#ch22_si_003}"

    # サイト：ふゎあああっ……おはよう、シエスタ。
    voice "ch22_s_002"
    s "Waaah… Morning, Siesta. And good night.{#ch22_s_002}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # シエスタ：ちょっと、サイトさんっ！！
    voice "ch22_si_004"
    si "Hey, Saito-san!! Get up!{#ch22_si_004}"

    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # シエスタ：ミス・ヴァリエールを起こす時間ですよ。  [voice 14876]
    voice "ch22_si_005"
    si "It's time to wake Miss Valliere.{#ch22_si_005}"

    # [EVENT_CG event    image=+216, level=80]
    $ dissolve_fx("id(216)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：ああ、そんな時間か……。
    voice "ch22_s_003"
    s "Ah, so it's that time… Thanks, Siesta.{#ch22_s_003}"

    # [EVENT_CG event    image=+215, level=80]
    $ dissolve_fx("id(215)")
    # シエスタ：いいえ、サイトさん。
    voice "ch22_si_006"
    si "Not at all, Saito-san. I'm glad I could be of help.{#ch22_si_006}"

    # サイト：（でも、こうやって誰かに起こしてもらうのって
    s "(But it's been a while since someone woke me up like this… Kind of nice.){#ch22_s_004}"

    # シエスタ：それじゃあサイトさん。
    voice "ch22_si_007"
    si "Well then, Saito-san. Next is Miss Valliere, isn't it?{#ch22_si_007}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # サイト：オーケー。  [voice 12128]
    voice "ch22_s_005"
    s "All right.{#ch22_s_005}"

    menu:
        "Wake her up as usual{#ch22_1_c_806_1}":
            jump ch22_1_scene_807
        "Leave it to Siesta{#ch22_1_c_806_2}":
            jump ch22_1_scene_808
        "Try a new method{#ch22_1_c_806_3}":
            jump ch22_1_scene_809

label ch22_1_scene_807:

    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # サイト：（いつものように布団を引っぺがしてやるか。
    s "(I'll just yank the blanket off like usual. Louise won't wake up otherwise.){#ch22_s_006}"

    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # サイト：とーりゃーっ！  [voice 12129]
    voice "ch22_s_007"
    s "Take this!{#ch22_s_007}"

    # [SE       se0      play=+67]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+330, level=160, dir=1C]
    # ルイズ：ふにゃっ！？  [voice 6603]
    voice "ch22_l_001"
    l "Nyah!?{#ch22_l_001}"

    # [SPRITE   lay5     image=+414, level=160, dir=1C]
    # サイト：おはようございます、ご主人様ぁ～。
    voice "ch22_s_008"
    s "Good morning, mistress! It's another lovely morning! Please open your eyes!{#ch22_s_008}"

    # ルイズ：あんたねぇ。
    voice "ch22_l_002"
    l "You… Could you at least think about how you wake someone up…{#ch22_l_002}"

    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # サイト：な……ちょっと待ったっ！！
    voice "ch22_s_009"
    s "Wha— Wait a second!! It's not like I did anything different from usual…{#ch22_s_009}"

    # → next scene 810
    jump ch22_1_scene_810

label ch22_1_scene_808:

    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+445, level=160, dir=2C]
    # サイト：シエスタ。
    voice "ch22_s_010"
    s "Siesta. I'll leave this to you.{#ch22_s_010}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：ええ？
    voice "ch22_si_008"
    si "Eh? Are you sure?{#ch22_si_008}"

    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # サイト：ああ。
    voice "ch22_s_011"
    s "Yeah. Your technique… let's see it! Waking Louise—that's the trial!{#ch22_s_011}"

    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：が、頑張りますっ！  [voice 14880]
    voice "ch22_si_009"
    si "I-I'll do my best!{#ch22_si_009}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：おはようございます、ミス・ヴァリエール。
    voice "ch22_si_010"
    si "Good morning, Miss Valliere. It's about time you woke up?{#ch22_si_010}"

    # [SPRITE   lay2     x=224, y=0]
    # [SPRITE   lay1     image=+330, level=160, dir=1C]
    # ルイズ：……ん、ふにゃあっ。
    voice "ch22_l_003"
    l "…Mm, nyah… Si…esta… Mornin…{#ch22_l_003}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+414, level=160, dir=1C]
    # サイト：見事だ、シエスタ！
    voice "ch22_s_012"
    s "Magnificent, Siesta! You managed to wake Louise, who's always low-blood-pressure and slow to rise!{#ch22_s_012}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：えへへ、ありがとうございます。  [voice 14882]
    voice "ch22_si_011"
    si "Ehehe, thank you.{#ch22_si_011}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+328, level=160, dir=1C]
    # ルイズ：ちょっと、サイト？
    voice "ch22_l_004"
    l "Hey, Saito? It's fine to praise her, but where's the water for washing my face?{#ch22_l_004}"

    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：し、しまったぁ！  [voice 12135]
    voice "ch22_s_013"
    s "O-Oh no!{#ch22_s_013}"

    # → next scene 810
    jump ch22_1_scene_810

label ch22_1_scene_809:

    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # サイト：今日は新しい方法を試してみよう。  [voice 12136]
    voice "ch22_s_014"
    s "Today I'll try a new method.{#ch22_s_014}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：サイトさん、それは……？  [voice 14883]
    voice "ch22_si_012"
    si "Saito-san, that is…?{#ch22_si_012}"

    # [SPRITE   lay5     image=+445, level=160, dir=2C]
    # サイト：ふふふっ、まあ見ててくれ。  [voice 12137]
    voice "ch22_s_015"
    s "Heh heh, just watch.{#ch22_s_015}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # サイト：ご主人様……ふぅっ。
    voice "ch22_s_016"
    s "Mistress… Phew. It's morning… Phew. Time to wake… Phew phew phew.{#ch22_s_016}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+328, level=160, dir=1C]
    # ルイズ：うひゃああああっ！
    voice "ch22_l_005"
    l "Kyaaa! What are you doing, blowing into my ear!?{#ch22_l_005}"

    # [SPRITE   lay5     image=+414, level=160, dir=1C]
    # サイト：おはよう、ルイズ。  [voice 12139]
    voice "ch22_s_017"
    s "Good morning, Louise.{#ch22_s_017}"

    # ルイズ：おはようルイズじゃないわよっ！
    voice "ch22_l_006"
    l "That's not 'good morning, Louise'! Why can't you wake me up normally!?{#ch22_l_006}"

    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：ま、待て、落ち着け。  [voice 12140]
    voice "ch22_s_018"
    s "W-Wait, calm down.{#ch22_s_018}"

    # → next scene 810
    jump ch22_1_scene_810

label ch22_1_scene_810:

    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # [SPRITE   lay1     image=+330, level=160, dir=1C]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+329, level=140, dir=1C]
    # ルイズ：朝からお仕置きよー！  [voice 6609]
    voice "ch22_l_007"
    l "Punishment first thing in the morning!?{#ch22_l_007}"

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
    # サイト：ぎゃああああすっ！  [voice 12141]
    voice "ch22_s_019"
    s "Gyaaaaaah!{#ch22_s_019}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 811
    jump ch22_1_scene_811

label ch22_1_scene_811:

    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # サイト：（そして、朝食の時間……）
    s "(And then, breakfast time…){#ch22_s_020}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：さぁ、これで全部です。  [voice 14884]
    voice "ch22_si_013"
    si "There, that's everything.{#ch22_si_013}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：すっげぇ～～。  [voice 12142]
    voice "ch22_s_021"
    s "Amazing~~.{#ch22_s_021}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：それじゃあ、いただきましょう。  [voice 6610]
    voice "ch22_l_008"
    l "Well then, let's eat.{#ch22_l_008}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：うふふっ。  [voice 2398]
    voice "ch22_ha_001"
    ha "Heh heh.{#ch22_ha_001}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：ゆっくり召し上がってくださいね。  [voice 14885]
    voice "ch22_si_014"
    si "Please enjoy it slowly.{#ch22_si_014}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：偉大なる始祖ブリミルと女王陛下よ。  [voice 6611]
    voice "ch22_l_009"
    l "O great Founder Brimir and Her Majesty the Queen.{#ch22_l_009}"

    # ルイズ：今朝もささやかな糧を我らに
    voice "ch22_l_010"
    l "We deeply thank You for granting us this modest meal this morning, too.{#ch22_l_010}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SE       se0      play=+57]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+712, level=140, dir=2A]
    # キュルケ：さぁ！！
    voice "ch22_k_001"
    k "All right!! The cooking contest!!{#ch22_k_001}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # ルイズ：んぐんぐっ……あら？
    voice "ch22_l_011"
    l "Gng gng… Hmm? This salad is actually pretty good, isn't it?{#ch22_l_011}"

    # シエスタ：あ、ありがとうございますっ。
    voice "ch22_si_015"
    si "A, thank you! There's plenty more, so please help yourself!{#ch22_si_015}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：わあっ、このロールパンもフカフカ！  [voice 2399]
    voice "ch22_ha_002"
    ha "Wow, these rolls are so fluffy!{#ch22_ha_002}"

    # シエスタ：それはですね。コック長のマルトーさんが
    voice "ch22_si_016"
    si "That's because head chef Marto got up early and carefully kneaded the dough before baking—it's a special recipe!{#ch22_si_016}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：ちょっとぉ、あたしの話聞いてるっ？  [voice 3407]
    voice "ch22_k_002"
    k "Hey, are you even listening to me?{#ch22_k_002}"

    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：今、食事中なの！  [voice 6614]
    voice "ch22_l_012"
    l "We're eating right now!{#ch22_l_012}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：あら、余裕ね。
    voice "ch22_k_003"
    k "Oh, how relaxed. I hope you're this relaxed during the match, too.{#ch22_k_003}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そんなの決まってるでしょ。  [voice 6615]
    voice "ch22_l_013"
    l "That goes without saying.{#ch22_l_013}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：決戦の場は食堂に用意したから、
    voice "ch22_k_004"
    k "I've set the battlefield in the dining hall. Once you finish breakfast, come on in. Understood?{#ch22_k_004}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：分かったわ。
    voice "ch22_l_014"
    l "I understand. I'll make you eat your words, absolutely!{#ch22_l_014}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：楽しみにしておくわ。
    voice "ch22_k_005"
    k "I'll look forward to it. See you then.{#ch22_k_005}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 812
    jump ch22_1_scene_812

label ch22_1_scene_812:

    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SE       se1      play=+39]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：なんだか、おおごとになってしまいましたね。  [voice 14888]
    voice "ch22_si_017"
    si "It's gotten kind of big, hasn't it.{#ch22_si_017}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：たかだか数人の料理対決に、ここまで人が
    voice "ch22_s_022"
    s "For a cooking contest between a few people, so many have gathered… This academy has a lot of idle students.{#ch22_s_022}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # オスマン：やあやあ、諸君、おはよう。
    voice "ch22_o_001"
    o "Yo yo, everyone, good morning. I hear our cute students have prepared a feast today?{#ch22_o_001}"

    # [SPRITE   lay10    x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：オールド・オスマンっ！？
    voice "ch22_l_015"
    l "Old Osmond!? And Mr. Colbert, too!?{#ch22_l_015}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # コルベール：今日は、天気にも恵まれていますな。
    voice "ch22_c_001"
    c "The weather's lovely today, isn't it. Show off your skills and make something wonderful.{#ch22_c_001}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：もしかして、わたし達を審査するのは……。  [voice 6618]
    voice "ch22_l_016"
    l "Could it be that you two are judging us…?{#ch22_l_016}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：そうよ、ルイズ。  [voice 3411]
    voice "ch22_k_006"
    k "That's right, Louise.{#ch22_k_006}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：キュルケっ！？  [voice 6619]
    voice "ch22_l_017"
    l "Kirche!?{#ch22_l_017}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：うふふっ、待ちくたびれたわ？
    voice "ch22_k_007"
    k "Heh heh, all tired of waiting? Today I'll give you the final push!{#ch22_k_007}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：あぁら、それはおあいにくさまっ。
    voice "ch22_l_018"
    l "Oh, that's too bad for you. I have a trump card, too!{#ch22_l_018}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あら、そう。
    voice "ch22_k_008"
    k "Oh, really? Well, I'm looking forward to it.{#ch22_k_008}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：ねぇ、タバサぁ。
    voice "ch22_k_009"
    k "Hey, Tabitha. What are you planning to make? Do you have confidence in winning?{#ch22_k_009}"

    # [SPRITE   lay6     x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：先手必勝。  [voice 15635]
    voice "ch22_t_001"
    t "First strike wins.{#ch22_t_001}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なんだそりゃ。  [voice 12144]
    voice "ch22_s_023"
    s "What's that supposed to mean?{#ch22_s_023}"

    # [SE       se1      stop=1]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：それじゃあ、ルールを説明するわ。  [voice 3415]
    voice "ch22_k_010"
    k "Well then, let me explain the rules.{#ch22_k_010}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：３人の審査員で判定を取ります。
    voice "ch22_k_011"
    k "Three judges will decide. Whoever gets the most points wins. Easy to understand, right?{#ch22_k_011}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：ズルなしの真剣勝負。
    voice "ch22_k_012"
    k "No cheating, a serious fight. Let's all do our best… Heh heh heh.{#ch22_k_012}"

    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：望むところよっ！  [voice 6621]
    voice "ch22_l_019"
    l "Gladly!{#ch22_l_019}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # ハルナ：私も、今日は頑張るんだからっ！  [voice 2400]
    voice "ch22_ha_003"
    ha "I'll do my best today, too!{#ch22_ha_003}"

    # シエスタ：よろしくお願いします、みなさん。  [voice 14889]
    voice "ch22_si_018"
    si "Please take care of us, everyone.{#ch22_si_018}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：勝負。  [voice 15636]
    voice "ch22_t_002"
    t "Fight.{#ch22_t_002}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：えー、それでは……コホン。
    voice "ch22_o_002"
    o "Ahem, then… Let the cooking begin.{#ch22_o_002}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：いよいよスタートだな。
    voice "ch22_s_024"
    s "Here we go. Will Siesta be all right?{#ch22_s_024}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：ええ、もちろんです。  [voice 14890]
    voice "ch22_si_019"
    si "Yes, of course.{#ch22_si_019}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：ひいおじいちゃん秘伝の料理を
    voice "ch22_si_020"
    si "I'll serve a secret family recipe from my great-great-grandfather, so look forward to it!{#ch22_si_020}"

    menu:
        "I want to eat it already{#ch22_1_c_812_1}":
            jump ch22_1_scene_813
        "Did I bring stomach medicine?{#ch22_1_c_812_2}":
            jump ch22_1_scene_814
        "Don't overdo it{#ch22_1_c_812_3}":
            jump ch22_1_scene_815

label ch22_1_scene_813:

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：秘伝の料理かぁ……早く食べてみたいなぁ。
    voice "ch22_s_025"
    s "A secret recipe… I can't wait to eat it. It's Siesta's home cooking, after all!{#ch22_s_025}"

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：頑張りますっ！
    voice "ch22_si_021"
    si "I'll do my best! More than anything, I want Saito-san to say it's delicious!{#ch22_si_021}"

    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # サイト：（ああっ、シエスタ、可愛い……）
    s "(Ah, Siesta, you're so cute…){#ch22_s_026}"

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
    # サイト：痛っぇ～～～～～っ！！
    voice "ch22_s_027"
    s "Ouch! Who threw that ladle at me!?{#ch22_s_027}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：あんたはわたしの使い魔なんだから、
    voice "ch22_l_020"
    l "You're my familiar, so pin your hopes on MY cooking! You're a useless familiar, truly!{#ch22_l_020}"

    # → next scene 816
    jump ch22_1_scene_816

label ch22_1_scene_814:

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：シエスタはいいとして……。
    voice "ch22_s_028"
    s "Siesta's fine, but… the others' cooking… Did I bring stomach medicine?{#ch22_s_028}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あ、はい。
    voice "ch22_si_022"
    si "Ah, yes. I have some stomach medicine from my grandmother in my room, so don't worry.{#ch22_si_022}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：もしかしたら、お世話になるかも……。
    voice "ch22_s_029"
    s "I might need it… No, I definitely will need it.{#ch22_s_029}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：でも、とっても苦いお薬ですよ？  [voice 14894]
    voice "ch22_si_023"
    si "But it's a very bitter medicine, you know?{#ch22_si_023}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：それはいやだなぁ。
    voice "ch22_s_030"
    s "Ugh. Is there nothing sweet?{#ch22_s_030}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：うーん、そういうのはありません。
    voice "ch22_si_024"
    si "Hmm, I don't think so. Please drink it bravely, okay?{#ch22_si_024}"

    # → next scene 816
    jump ch22_1_scene_816

label ch22_1_scene_815:

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：頑張るのはいいけど、
    voice "ch22_s_031"
    s "Doing your best is fine, but don't overdo it, okay?{#ch22_s_031}"

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：大丈夫ですっ。
    voice "ch22_si_025"
    si "It's fine! For Saito-san's sake, I can… do anything.{#ch22_si_025}"

    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # サイト：いや、そう言われちゃうと
    voice "ch22_s_032"
    s "Well, when you put it that way, I get embarrassed.{#ch22_s_032}"

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
    # サイト：痛っぇ～～～～～っ！！
    voice "ch22_s_033"
    s "Ouch! Who threw that ladle at me!?{#ch22_s_033}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：あんたはわたしの使い魔なんだから、
    voice "ch22_l_021"
    l "You're my familiar, so don't flirt with other girls. You stupid dog!{#ch22_l_021}"

    # → next scene 816
    jump ch22_1_scene_816

label ch22_1_scene_816:

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
    # ギーシュ：みんなの料理の腕前はどんな感じ
    voice "ch22_g_001"
    g "I wonder how everyone's cooking is coming along…{#ch22_g_001}"

    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # モンモランシー：まあ、あまり期待しないほうがいいわね、
    voice "ch22_m_001"
    m "Well, you'd better not expect too much—especially from some people's cooking.{#ch22_m_001}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # オスマン：ほっ、ほっ、ほっ。
    voice "ch22_o_003"
    o "Heh, heh, heh. A noble cooking for herself—is this Saito-kun's influence, too?{#ch22_o_003}"

    # [SPRITE   lay10    x=224, y=0]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：ええ、良い影響だと思います。  [voice 1168]
    voice "ch22_c_002"
    c "Yes, I think it's a good influence.{#ch22_c_002}"

    # サイト：（これで料理がまともだったら、
    s "(If the food turns out decent after all, this will be a nice story… I wonder how it'll turn out…){#ch22_s_034}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay10    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # → next scene 817
    jump ch22_2

    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch22_2
    return

