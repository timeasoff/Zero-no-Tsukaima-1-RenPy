# Глава 24 (источник chapter_25): школьная форма, уход Харуны, клятва Сиэсты.
# Источник: ps2_source/chapters/chapter_25_制服の魅力.txt (SCENE 894-902).

label ch24:
    $ tndl(None)
    $ show_sprites()

label ch24_1_scene_894:

    # [TITLE title("制服の魅力")]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1165, level=200]
    $ fade_fx("id(1165)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：シエスタ！  [voice 7990]
    voice "ch24_s_001"
    s "Siesta!{#ch24_s_001}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あれ、サイトさんっ。
    voice "ch24_si_001"
    si "Oh, Saito-san. What's the matter? You look so happy today.{#ch24_si_001}"

    # サイト：ふふ～ん、そりゃあもちろん。  [voice 7991]
    voice "ch24_s_002"
    s "Heh heh~, of course I am.{#ch24_s_002}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：今日はシエスタにプレゼントを
    voice "ch24_s_003"
    s "Today I brought a present for Siesta!{#ch24_s_003}"

    # [SPRITE   lay2     image=+530, level=160, dir=2A]
    # シエスタ：えっ、わたしにですか？  [voice 14151]
    voice "ch24_si_002"
    si "Eh? For me?{#ch24_si_002}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：そうだよぉ～？
    voice "ch24_s_004"
    s "That's right~! Ta-daaa!! Look at this wrapping paper!!{#ch24_s_004}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：わあ、可愛い……。
    voice "ch24_si_003"
    si "Wow, it's cute… What's inside?{#ch24_si_003}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：それは、受け取ってからのお楽しみってやつ。
    voice "ch24_s_005"
    s "That's for you to find out once you open it. Here, open it, open it.{#ch24_s_005}"

    # [SPRITE   lay2     image=+530, level=160, dir=2A]
    # シエスタ：あ、ありがとうございます……。
    voice "ch24_si_004"
    si "Ah, thank you… I'm so happy…{#ch24_si_004}"

    # [SE       se0      play=+59]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：これは……水兵さんの……服？  [voice 14154]
    voice "ch24_si_005"
    si "This is… a sailor's… clothes?{#ch24_si_005}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：正解！  [voice 7995]
    voice "ch24_s_006"
    s "Correct!{#ch24_s_006}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：これはセーラー服といって、日本ではシエスタ
    voice "ch24_s_007"
    s "It's called a sailor uniform. In Japan, cute girls like Siesta wear it to study!{#ch24_s_007}"

    # シエスタ：お勉強……つまり、学生さんが
    voice "ch24_si_006"
    si "Studying… So it's a uniform students wear, right?{#ch24_si_006}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：そうさっ！
    voice "ch24_s_008"
    s "That's right! So I want Siesta to wear it, too!{#ch24_s_008}"

    # [SPRITE   lay2     image=+522, level=160, dir=2A]
    # シエスタ：いいんですか？  [voice 14156]
    voice "ch24_si_007"
    si "Is that really all right?{#ch24_si_007}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：いいのいいの。
    voice "ch24_s_009"
    s "Of course it is. More importantly, will you put it on right now?{#ch24_s_009}"

    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：ええっ！？
    voice "ch24_si_008"
    si "Eh!? Right now!?{#ch24_si_008}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：うん、期待してますシエスタさん。
    voice "ch24_s_010"
    s "Yep, I'm looking forward to it, Siesta-san. Put it on. Put it on, put it on.{#ch24_s_010}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：き、期待されちゃいましたね。
    voice "ch24_si_009"
    si "W-Well, you've made me curious. Wait a moment, I'll change right away…{#ch24_si_009}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     x=64, y=0]
    # サイト：（……やったぞっ！
    s "(…Yes! Soon I'll get to see Siesta in a sailor uniform!!){#ch24_s_011}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+283, level=80]
    $ dissolve_fx("id(283)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # シエスタ：サイトさんっ……お待たせしましたっ！！  [voice 14159]
    voice "ch24_si_010"
    si "Saito-san… Sorry to keep you waiting!!{#ch24_si_010}"

    # シエスタ：えへっ……。
    voice "ch24_si_011"
    si "Heh heh… How do I look? Does it suit me?{#ch24_si_011}"

    # サイト：おおおおおおおーーーーっ！  [voice 8000]
    voice "ch24_s_012"
    s "Ooooohooooo!!{#ch24_s_012}"

    # シエスタ：さ、サイトさんったら、声が大きいですよぉ。  [voice 14161]
    voice "ch24_si_012"
    si "My, Saito-san, your voice is so loud.{#ch24_si_012}"

    # サイト：ううっ……ぐすっ……。
    voice "ch24_s_013"
    s "Ugh… Sniff… I'm glad I'm alive!{#ch24_s_013}"

    # [EVENT_CG event    image=+284, level=80]
    $ dissolve_fx("id(284)")
    # シエスタ：……はい？
    voice "ch24_si_013"
    si "…Huh? Um, Saito-san, why are you crying?{#ch24_si_013}"

    # サイト：いやあ、シエスタの姿があまりにも眩しくてっ！
    voice "ch24_s_014"
    s "No, it's just—seeing you like this is so dazzling! Japan came rushing back to me.{#ch24_s_014}"

    # サイト：ああっ、ハルケギニアを照らす日の光が
    voice "ch24_s_015"
    s "Ah! I've never felt the light of Halkeginia shine this brightly before!!{#ch24_s_015}"

    # [EVENT_CG event    image=+283, level=80]
    $ dissolve_fx("id(283)")
    # シエスタ：大丈夫ですか、サイトさん？
    voice "ch24_si_014"
    si "Are you all right, Saito-san? I have a handkerchief here… Here.{#ch24_si_014}"

    # サイト：ありがとう、シエスタぁ。
    voice "ch24_s_016"
    s "Thank you, Siesta. That uniform really suits you!{#ch24_s_016}"

    # シエスタ：ほ、ほんとですか？
    voice "ch24_si_015"
    si "R-Really? It's the first time I've worn something so… revealing, and I'm a bit embarrassed…{#ch24_si_015}"

    # サイト：い、いやいや、それがまたいいんだよぉ……。  [voice 8005]
    voice "ch24_s_017"
    s "N-No, that's exactly what's good about it…{#ch24_s_017}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # ルイズ：どこ見てるのよっ！！
    voice "ch24_l_001"
    l "Just what are you looking at!? Idiot!!{#ch24_l_001}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay2     vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [SPRITE   lay1     hide, vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # サイト：ぎひゃぁあぁあぁ！！
    voice "ch24_s_018"
    s "Gyaaaaaah!! L-Louise… Why are you here!?{#ch24_s_018}"

    # ルイズ：シエスタになんて格好させてるのよっ！！
    voice "ch24_l_002"
    l "What are you making Siesta wear!? Honestly, have you no shame as a person!?{#ch24_l_002}"

    # サイト：ぐふっ……。
    voice "ch24_s_019"
    s "Guh… Flop.{#ch24_s_019}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+284, level=80]
    $ dissolve_fx("id(284)")
    # [TRANS trans("crossfade", 1000)]
    # シエスタ：サ、サイトさんっ！！
    voice "ch24_si_016"
    si "S-Saito-san!! Pull yourself together!!{#ch24_si_016}"

    # ルイズ：ほっときなさいよっ、こんなバカっ！！
    voice "ch24_l_003"
    l "Leave him be, he's an idiot!! Siesta, take that off at once, too!!{#ch24_l_003}"

    # シエスタ：ええっ、でもこれはサイトさんがせっかく
    voice "ch24_si_017"
    si "Eh, but this is the student uniform Saito-san gave me…{#ch24_si_017}"

    # ルイズ：当然、この服も没収！  [voice 4560]
    voice "ch24_l_004"
    l "Then that, too, is confiscated!{#ch24_l_004}"

    menu:
        "Let Louise wear it{#ch24_1_c_894_1}":
            jump ch24_1_scene_895
        "Stay silent{#ch24_1_c_894_2}":
            jump ch24_1_scene_896
        "I'll wear it myself!{#ch24_1_c_894_3}":
            jump ch24_1_scene_897

label ch24_1_scene_895:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+284, level=80]
    $ dissolve_fx("id(284)")
    # サイト：ううっ……シエスタがダメなら……。
    voice "ch24_s_020"
    s "Ugh… If Siesta's no good… Maybe Louise would wear it…{#ch24_s_020}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：なにか、言ったかしら？  [voice 4561]
    voice "ch24_l_005"
    l "Did you say something?{#ch24_l_005}"

    # サイト：ひぃぃっ！！  [voice 8009]
    voice "ch24_s_021"
    s "Eeeeeh!!{#ch24_s_021}"

    # ルイズ：やっぱり、今すぐ罪を償わせてあげる！！
    voice "ch24_l_006"
    l "Yes, now you must atone at once! Brace yourself!!{#ch24_l_006}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SE       se0      play=+61]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [SPRITE   lay2     vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # サイト：ぎゃあああああああっ……。  [voice 8010]
    voice "ch24_s_022"
    s "Gyaaaaah…{#ch24_s_022}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # → next scene 898
    jump ch24_1_scene_898

label ch24_1_scene_896:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+284, level=80]
    $ dissolve_fx("id(284)")
    # サイト：なんでもないでしゅ……。  [voice 8011]
    voice "ch24_s_023"
    s "It's nothing, really…{#ch24_s_023}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：ふんっ……。
    voice "ch24_l_007"
    l "Hmph… Well, come quickly. Or I'll tie you up with a collar and a belt.{#ch24_l_007}"

    # サイト：ふぁい……。
    voice "ch24_s_024"
    s "Yaah… Once I recover, I'll come at once.{#ch24_s_024}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # → next scene 898
    jump ch24_1_scene_898

label ch24_1_scene_897:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+284, level=80]
    $ dissolve_fx("id(284)")
    # サイト：俺が着る！  [voice 8013]
    voice "ch24_s_025"
    s "I'll wear it myself!{#ch24_s_025}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：は？
    voice "ch24_l_008"
    l "Huh? What are you talking about? Or have you finally awakened something?{#ch24_l_008}"

    # サイト：何にだ！  [voice 8014]
    voice "ch24_s_026"
    s "Awakened what!?{#ch24_s_026}"

    # ルイズ：まあ、いいわ。
    voice "ch24_l_009"
    l "Fine. Anyway, I'm confiscating this. See you.{#ch24_l_009}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # → next scene 898
    jump ch24_1_scene_898

label ch24_1_scene_898:

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # シエスタ：サイトさん……。
    voice "ch24_si_018"
    si "Saito-san… Please pull yourself together.{#ch24_si_018}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：あは……ははっ。
    voice "ch24_s_027"
    s "Ah ha… Ha ha. I'm fine, this much…{#ch24_s_027}"

    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # シエスタ：せっかくのプレゼントでしたのに、残念です。  [voice 14168]
    voice "ch24_si_019"
    si "It was such a nice present, though. What a shame.{#ch24_si_019}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：でも、今度はわたしがセーラー服作りに
    voice "ch24_si_020"
    si "But next time I'll try making a sailor uniform myself. So look forward to it!{#ch24_si_020}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：そ、それは本当ですかっ！！  [voice 8016]
    voice "ch24_s_028"
    s "R-Really!?{#ch24_s_028}"

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：はいっ、サイトさんのために頑張っちゃいます！
    voice "ch24_si_021"
    si "Yes! I'll do my best for Saito-san! Let's go on a date in matching outfits!{#ch24_si_021}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：……え？  [voice 8017]
    voice "ch24_s_029"
    s "…Eh?{#ch24_s_029}"

    # サイト：（シエスタ自作のセーラー服に期待を膨らませ
    s "(Even as I looked forward to Siesta's handmade sailor uniform, I felt a little uneasy.){#ch24_s_030}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
label ch24_1_scene_899:

    # [MOVIE movie(1)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：えっ、自立するってどういうことだよ？  [voice 9216]
    voice "ch24_s_031"
    s "Eh? What do you mean, becoming independent?{#ch24_s_031}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：うん、いつまでもこの学院で……。
    voice "ch24_ha_001"
    ha "Yeah. I can't stay at this academy forever… It'd be wrong to keep relying on Louise and the others.{#ch24_ha_001}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そんなこといったら、俺なんかルイズに
    voice "ch24_s_032"
    s "If you say that, then I've been taken care of by this academy ever since Louise summoned me.{#ch24_s_032}"

    # ハルナ：平賀くんはルイズさんの使い魔じゃない。
    voice "ch24_ha_002"
    ha "Hiraga-kun is Louise-san's familiar. Of course you're taken care of. But I'm not one, so…{#ch24_ha_002}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そりゃそうなんだけどさ……。
    voice "ch24_s_033"
    s "I know, but… We're probably the only two Japanese people in this world.{#ch24_s_033}"

    # サイト：それに、お互いのことを知らない
    voice "ch24_s_034"
    s "And we're not exactly strangers to each other… So if we worked at the academy, maybe…{#ch24_s_034}"

    # [SPRITE   lay7     image=+959, level=160, dir=1A]
    # ハルナ：あのね、平賀くん……。
    voice "ch24_ha_003"
    ha "The thing is, Hiraga-kun… I've been scouted.{#ch24_ha_003}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ス、スカウトって、なんの？  [voice 9220]
    voice "ch24_s_035"
    s "S-Scouted for what?{#ch24_s_035}"

    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：劇団よ、劇団。  [voice 1783]
    voice "ch24_ha_004"
    ha "A theater troupe, a theater troupe.{#ch24_ha_004}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：劇団って、あのウェザリーの劇団は
    voice "ch24_s_036"
    s "A theater troupe? I thought Weatherly's troupe was gone?{#ch24_s_036}"

    # ハルナ：違うの。
    voice "ch24_ha_005"
    ha "No. Someone from another troupe who saw that play liked me and scouted me.{#ch24_ha_005}"

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：この際、いい機会だから、その劇団のお世話に
    voice "ch24_ha_006"
    ha "Now's a good chance, so I've decided to join that troupe.{#ch24_ha_006}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：でもさ、劇団の世話になるってことは、
    voice "ch24_s_037"
    s "But if you join a troupe, you'll have to go on tours to other towns, won't you?{#ch24_s_037}"

    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：うん、そうだね。
    voice "ch24_ha_007"
    ha "Yeah. I probably won't get to see Hiraga-kun very often anymore.{#ch24_ha_007}"

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：でもね、私は楽しみにしてるんだ。
    voice "ch24_ha_008"
    ha "But I'm looking forward to it. I get to see all sorts of towns in this world.{#ch24_ha_008}"

    # ハルナ：ひょっとすると、日本へ戻るためのきっかけ
    voice "ch24_ha_009"
    ha "Maybe I'll even find a clue to get back to Japan.{#ch24_ha_009}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そっか、そうだよな。  [voice 9223]
    voice "ch24_s_038"
    s "I see. Yeah, that's right.{#ch24_s_038}"

    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：だから平賀くん……。
    voice "ch24_ha_010"
    ha "So, Hiraga-kun… If you don't mind, cheer me on, okay?{#ch24_ha_010}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：ああ、もちろんだとも！
    voice "ch24_s_039"
    s "Of course I will! And let's both do our best to find a way back to Japan!{#ch24_s_039}"

    # ハルナ：うん！  [voice 1790]
    voice "ch24_ha_011"
    ha "Mm!{#ch24_ha_011}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：（ウェザリーは逃げ惑う兵隊達の中に
    s "(I hear Weatherly was caught while trying to blend in with the panicked soldiers.){#ch24_s_040}"

    # サイト：（ウェザリーの背後には
    s "(Behind Weatherly, apparently, was Reconquista. A military meeting was held at once.){#ch24_s_041}"

    # サイト：（春奈を操っていた催眠魔法は、
    s "(The hypnosis magic controlling Haruna was undone by Weatherly.){#ch24_s_042}"

    # サイト：（これで、一連の爆弾使いにまつわる
    s "(With that, the whole bomber affair has come to an end.){#ch24_s_043}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # ルイズ：さぁ、わたし達も帰りましょう。  [voice 4841]
    voice "ch24_l_010"
    l "Well then, let's head home, too.{#ch24_l_010}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：でも、ウェザリーのこととか、
    voice "ch24_l_011"
    l "But we ended up staying so long because of Weatherly and Haruna, didn't we?{#ch24_l_011}"

    # サイト：そうだな。
    voice "ch24_s_044"
    s "Yeah. But everyone's waiting for us to get back.{#ch24_s_044}"

    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：そうだったわね。
    voice "ch24_l_012"
    l "Right, I suppose so. I wonder how everyone is doing right about now?{#ch24_l_012}"

    # シエスタ：サイトさ～～～～～～んっ！！  [voice 14359]
    voice "ch24_si_022"
    si "Saiiiito-saaaaan!!{#ch24_si_022}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # サイト：ええっ！？
    voice "ch24_s_045"
    s "Eh!? Th-That voice is…!{#ch24_s_045}"

    # ルイズ：ウソぉ、何であの子がこんな所にっ！？  [voice 4844]
    voice "ch24_l_013"
    l "No way, why is she here!?{#ch24_l_013}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    image=+282, level=80]
    $ dissolve_fx("id(282)")
    # [TRANS trans("crossfade", 1000)]
    # シエスタ：サイトさんっ！！
    voice "ch24_si_023"
    si "Saito-san!! I… found you!!{#ch24_si_023}"

    # サイト：うわ、ど、どうしたのシエスタ。  [voice 9227]
    voice "ch24_s_046"
    s "Whoa, what's wrong, Siesta?{#ch24_s_046}"

    # シエスタ：わたし、なかなかサイトさん達が
    voice "ch24_si_024"
    si "You two weren't coming back for so long, I got worried and came to check on you!!{#ch24_si_024}"

    # サイト：俺なら、ほらこのとおり。
    voice "ch24_s_047"
    s "Well, as you can see—I'm completely fine.{#ch24_s_047}"

    # シエスタ：良かったぁ！  [voice 14362]
    voice "ch24_si_025"
    si "Thank goodness!{#ch24_si_025}"

    # サイト：ああ、そうだシエスタっ。
    voice "ch24_s_048"
    s "Ah, that's right, Siesta. I'll return the charm I borrowed, just as I promised.{#ch24_s_048}"

    # サイト：爆弾使いと戦ったときも、
    voice "ch24_s_049"
    s "When I fought the bomber, thanks to it I got through without injury.{#ch24_s_049}"

    # シエスタ：ホントですかぁ？
    voice "ch24_si_026"
    si "Really? Thank goodness. Great-grandfather must have protected you, Saito-san.{#ch24_si_026}"

    # サイト：ああ、きっとそうに違いないさ。  [voice 9231]
    voice "ch24_s_050"
    s "Ah, I'm sure he did.{#ch24_s_050}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：お守りかぁ～。
    voice "ch24_l_014"
    l "A charm, huh… Nice, isn't it… a charm.{#ch24_l_014}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：なんだよぉ、別にいいだろう？
    voice "ch24_s_051"
    s "What's that? It's fine, isn't it? Besides, Louise is my charm, right?{#ch24_s_051}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：そ、そうよっ！！
    voice "ch24_l_015"
    l "T-That's right!! My charm is only Saito!{#ch24_l_015}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：それだったら、サイトさんのお守りには、
    voice "ch24_si_027"
    si "Then I'll become Saito-san's charm!{#ch24_si_027}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ええ！？  [voice 9233]
    voice "ch24_s_052"
    s "Eh!?{#ch24_s_052}"

    # → next scene 900
    jump ch24_1_scene_900

    # → next scene 901
    jump ch24_1_scene_901

label ch24_1_scene_900:

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：サイトさんの無事を願うためなら……。
    voice "ch24_si_028"
    si "If it's for praying for your safety… I'll kiss you again, like before!!{#ch24_si_028}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+307, level=140, dir=1A]
    # ルイズ：キ……キスぅ！？  [voice 4847]
    voice "ch24_l_016"
    l "K-Kiss!?{#ch24_l_016}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：うわあ、シエスタったらっ！！  [voice 9234]
    voice "ch24_s_053"
    s "Whoa, Siesta!!{#ch24_s_053}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+497, level=160, dir=1A]
    # シエスタ：わあっ、わたしったら一体なんてコトをっ！
    voice "ch24_si_029"
    si "Oh, what have I done! To think I said I'd kissed… I'm so embarrassed!{#ch24_si_029}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+373, level=140, dir=3A]
    # ルイズ：こ、この子ったら……わたしが目を離した隙に
    voice "ch24_l_017"
    l "Th-This girl… What did she do while I wasn't looking!?{#ch24_l_017}"

    # [SPRITE   lay1     image=+372, level=160, dir=3A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：ひええっ……。
    voice "ch24_s_054"
    s "Eeeh… That was, um… Whoaaa!!{#ch24_s_054}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+373, level=140, dir=3A]
    # ルイズ：問答無用よぉ！！
    voice "ch24_l_018"
    l "No excuses! I'll beat that shameless, rotten attitude right out of you!{#ch24_l_018}"

    # [SPRITE   lay1     hide]
    # [SE       se0      play=+95]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：こ、殺されるぅ！！  [voice 9236]
    voice "ch24_s_055"
    s "I'm going to be killed!!{#ch24_s_055}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # ルイズ：こらあっ、お待ちなさいっ！！
    voice "ch24_l_019"
    l "Hey! Stop right there! Don't you dare run away! Accept your fate!{#ch24_l_019}"

    # サイト：俺は、なにも悪いコトなんて
    voice "ch24_s_056"
    s "I didn't do anything wrong!{#ch24_s_056}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：ゴチャゴチャうるさいわよぉ！！
    voice "ch24_l_020"
    l "Shut up! As punishment for talking back—no meals for three days!{#ch24_l_020}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：そ、そんなぁ！！
    voice "ch24_s_057"
    s "T-That's too much!!{#ch24_s_057}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+307, level=140, dir=1A]
    # ルイズ：ダメっ！！
    voice "ch24_l_021"
    l "No! Absolutely! No exceptions!!{#ch24_l_021}"

    # [SPRITE   lay1     hide]
    # [SE       se0      play=+61]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [SPRITE   lay7     vibrate=21]
    # [SPRITE   lay2     vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：ぎゃああああっ！！  [voice 9239]
    voice "ch24_s_058"
    s "Gyaaaaah!!{#ch24_s_058}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # → next scene 902
    jump ch24_1_scene_902

label ch24_1_scene_901:

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：もぉ、あんた達ちょっと離れなさいってばっ！  [voice 4853]
    voice "ch24_l_022"
    l "Honestly, you two—separate yourselves already!{#ch24_l_022}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：いいえ、わたしもう決めましたっ。
    voice "ch24_si_030"
    si "No. I've decided. From now on, I'll be Saito-san's charm!{#ch24_si_030}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：だからサイトさん、ずっと一緒に
    voice "ch24_si_031"
    si "So, Saito-san, please stay with me forever!{#ch24_si_031}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：もういい、決めたわっ！！
    voice "ch24_l_023"
    l "Enough! I've decided! Saito is forbidden from getting cozy with Siesta!{#ch24_l_023}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：はあっ？
    voice "ch24_s_059"
    s "Hah!? That's tyranny!{#ch24_s_059}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：うるさいわねぇ！！
    voice "ch24_l_024"
    l "Shut up! As punishment for talking back—no meals for a week!{#ch24_l_024}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：そんなぁっ！！  [voice 9241]
    voice "ch24_s_060"
    s "That's too much!!{#ch24_s_060}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+497, level=160, dir=1A]
    # シエスタ：それならサイトさん、わたしの部屋で
    voice "ch24_si_032"
    si "Then, Saito-san, won't you live in my room with me?{#ch24_si_032}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：なんですってぇ！？
    voice "ch24_l_025"
    l "What was that!? Saito—what did you do with her while I wasn't looking!?{#ch24_l_025}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：ひええっ……。
    voice "ch24_s_061"
    s "Eeeh… That was, um… Whoaaa!!{#ch24_s_061}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+373, level=140, dir=3A]
    # ルイズ：問答無用よぉ！！
    voice "ch24_l_026"
    l "No excuses! I'll beat that shameless, rotten attitude right out of you!{#ch24_l_026}"

    # [SPRITE   lay1     hide]
    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：こ、殺されるぅ！！  [voice 9243]
    voice "ch24_s_062"
    s "I'm going to be killed!!{#ch24_s_062}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # → next scene 902
    jump ch24_1_scene_902

label ch24_1_scene_902:

    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # シエスタ：ああ、始祖ブリミルよ。
    voice "ch24_si_033"
    si "O great Founder Brimir. Grant a moment's peace to poor Saito.{#ch24_si_033}"

    # サイト：（ブルドンネ街の昼下がりに、
    s "(On a summer afternoon in Buldone, my screams, Louise's shouts and Siesta's prayers echoed up to the sky.){#ch24_s_063}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ГЛАВЫ 24 ====
    jump ch25
    return

