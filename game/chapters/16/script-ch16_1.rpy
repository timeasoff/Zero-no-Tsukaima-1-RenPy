# Глава 16 (сцены 660–669): «微熱の使い手» — постельные неразберихи и отъезд Харуны.
# Источник: ps2_source/chapters/chapter_17_微熱の使い手.txt (SCENE 660-669).

label ch16:
    $ tndl(None)
    $ show_sprites()

label ch16_1_scene_660:

    # [TITLE title("微熱の使い手")]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1161, level=200]
    $ fade_fx("id(1161)")
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
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：やっほ～～、ダーリン。  [voice 2665]
    voice "ch16_k_001"
    k "Yoohoo~, darling.{#ch16_k_001}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：お、おう。
    voice "ch16_s_001"
    s "O-Oh. Kirche!{#ch16_s_001}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：うっ、キュルケ！  [voice 4575]
    voice "ch16_l_001"
    l "Ugh, Kirche!{#ch16_l_001}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：最近、なかなか逢えないけど……、
    voice "ch16_k_002"
    k "We don't see each other much lately… Are you dumping me?{#ch16_k_002}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そ、そんなことはないんだけど……。  [voice 8083]
    voice "ch16_s_002"
    s "N-No, that's not it, but…{#ch16_s_002}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：キュ、キュルケから離れなさい！
    voice "ch16_l_002"
    l "K-Kirche, get away from him! You stupid dog!{#ch16_l_002}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：……ひいっ！
    voice "ch16_s_003"
    s "…Eek! S-Sorry, mistress!{#ch16_s_003}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：ちょっとルイズ？
    voice "ch16_k_003"
    k "Wait, Louise? What are you doing to darling?{#ch16_k_003}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：せっかく、久しぶりにダーリンと
    voice "ch16_k_004"
    k "We were finally having a nice talk after so long…{#ch16_k_004}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：サ、サイトはわたしの使い魔なんだから。
    voice "ch16_l_003"
    l "S-Saito is my familiar! He can't talk to other girls!{#ch16_l_003}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：あらあら……。
    voice "ch16_k_005"
    k "My my… Darling, you've got quite a terrible mistress, haven't you…{#ch16_k_005}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：ほら、行くわよ、バカ犬！  [voice 4578]
    voice "ch16_l_004"
    l "Come on, let's go, stupid dog!{#ch16_l_004}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：は、はいー！  [voice 8085]
    voice "ch16_s_004"
    s "Y-Yes, ma'am!{#ch16_s_004}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：うふふ。
    voice "ch16_k_006"
    k "Ufufu. Isn't this fun.{#ch16_k_006}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：いいこと、ヴァリエール。
    voice "ch16_k_007"
    k "Listen, Valliere. The bigger the obstacle, the more my flame of love burns…!{#ch16_k_007}"

    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # null：………。 (no voice)
    # [BG       stage    hide]
    # [BG       stage    image=+16, level=200]
    $ fade_fx("id(16)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+698, level=160, dir=1C]
    # キュルケ：（うふふ。
    voice "ch16_k_008"
    k "(Ufufu. If it's come to this, I'll just have to use force.){#ch16_k_008}"

    # キュルケ：（恋は戦争なのよ……ルイズ？）  [voice 2673]
    voice "ch16_k_009"
    k "(Love is war… Louise?){#ch16_k_009}"

    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+12, level=200]
    $ fade_fx("id(12)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+57]
    # [SPRITE   lay6     image=+700, level=160, dir=1C]
    # キュルケ：ダーリンは……？
    voice "ch16_k_010"
    k "Darling is…? Ah, that outfit is bed, right?{#ch16_k_010}"

    # ルイズ：むにゃむにゃ……。  [voice 4579]
    voice "ch16_l_005"
    l "Mumble mumble…{#ch16_l_005}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+291, level=80]
    $ dissolve_fx("id(291)")
    # [TRANS trans("crossfade", 1000)]
    # キュルケ：うふ、ダーリン、あたしよ、あたし。
    voice "ch16_k_011"
    k "Ufu, darling, it's me, me. I've come.{#ch16_k_011}"

    # キュルケ：今日こそ、ダーリンをあたしのものに
    voice "ch16_k_012"
    k "Today I'm going to make you mine, darling.{#ch16_k_012}"

    # [SE       se0      play=+59]
    # ルイズ：ん……。  [voice 4580]
    voice "ch16_l_006"
    l "Mm…{#ch16_l_006}"

    # キュルケ：……うふふ、かわいい声しちゃって。
    voice "ch16_k_013"
    k "…Ufufu, what a cute voice. Ticklish, ticklish…{#ch16_k_013}"

    # ルイズ：んっ……あっ……。  [voice 4581]
    voice "ch16_l_007"
    l "Mm… Ah…{#ch16_l_007}"

    # キュルケ：あら、意外とダーリンって線が細いのね。  [voice 2678]
    voice "ch16_k_014"
    k "Oh, you're more delicate than I thought, darling.{#ch16_k_014}"

    # キュルケ：それに、きれいな肌……。
    voice "ch16_k_015"
    k "And such beautiful skin… Your chest is so slender too.{#ch16_k_015}"

    # ルイズ：あんっ……いやっ……。  [voice 4582]
    voice "ch16_l_008"
    l "Ah… No…{#ch16_l_008}"

    # [EVENT_CG event    image=+292, level=80]
    $ dissolve_fx("id(292)")
    # キュルケ：うふふ、いただきま～～す。  [voice 2680]
    voice "ch16_k_016"
    k "Ufufu, I'm helping myself~~.{#ch16_k_016}"

    # サイト：……。  [voice 8086]
    voice "ch16_s_005"
    s "…{#ch16_s_005}"

    # キュルケ：うふふ。  [voice 2681]
    voice "ch16_k_017"
    k "Ufufu.{#ch16_k_017}"

    # ルイズ：サイト！
    voice "ch16_l_009"
    l "Saito! Stop…!{#ch16_l_009}"

    # ルイズ：……へ？
    voice "ch16_l_010"
    l "…Huh? Huh? Kirche?{#ch16_l_010}"

    # [EVENT_CG event    image=+291, level=80]
    $ dissolve_fx("id(291)")
    # キュルケ：……あ、あら？
    voice "ch16_k_018"
    k "…O-Oh? Louise?{#ch16_k_018}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # サイト：……な、何をやってるんだよ！
    voice "ch16_s_006"
    s "…What the hell are you two doing!?{#ch16_s_006}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+12, level=200]
    $ fade_fx("id(12)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay1     image=+329, level=140, dir=1C]
    # ルイズ：き、きゃ～～っ！  [voice 4585]
    voice "ch16_l_011"
    l "E-Eek!{#ch16_l_011}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：なんで、ふ、２人がベッドで抱き合ってんの！？  [voice 8088]
    voice "ch16_s_007"
    s "Why are you two hugging in bed!?{#ch16_s_007}"

    # サイト：（なんというか、
    s "(Since when is this place paradise?){#ch16_s_008}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+332, level=160, dir=1C]
    # [SPRITE   lay6     image=+706, level=160, dir=1C]
    # ルイズ：だ、抱き合って……！？
    voice "ch16_l_012"
    l "H-Hugging…!? N-n-n-n-n-n-n-n-n-n…!{#ch16_l_012}"

    # キュルケ：もうっ、ダーリンも混ざってみる？  [voice 2683]
    voice "ch16_k_019"
    k "Geez, darling—want to join in?{#ch16_k_019}"

    # [SPRITE   lay1     image=+328, level=160, dir=1C]
    # ルイズ：な、何を言ってるのよ！
    voice "ch16_l_013"
    l "What are you saying! Kirche!{#ch16_l_013}"

    # [SPRITE   lay1     image=+324, level=160, dir=1C]
    # ルイズ：っていうか、よく考えたら何してるのよ！  [voice 4588]
    voice "ch16_l_014"
    l "I mean, what are you doing!?{#ch16_l_014}"

    # [SPRITE   lay6     image=+700, level=160, dir=1C]
    # キュルケ：え、え～と、夜のごあいさつ？  [voice 2684]
    voice "ch16_k_020"
    k "E-Er… A good night greeting?{#ch16_k_020}"

    # [SPRITE   lay1     image=+328, level=160, dir=1C]
    # ルイズ：な、なによそれは！  [voice 4589]
    voice "ch16_l_015"
    l "What's that supposed to mean!{#ch16_l_015}"

    # ルイズ：夜のごあいさつだかなんだか
    voice "ch16_l_016"
    l "I don't care what you call it! What were you doing to Saito while I was sleeping!?{#ch16_l_016}"

    # [SPRITE   lay6     image=+704, level=160, dir=1C]
    # キュルケ：あ、そういえば……。  [voice 2685]
    voice "ch16_k_021"
    k "Oh, now that you mention it…{#ch16_k_021}"

    # [SPRITE   lay1     image=+324, level=160, dir=1C]
    # ルイズ：なにが『あ、そういえば……』よ。
    voice "ch16_l_017"
    l "What do you mean 'oh now that you mention it'! Are you an idiot!{#ch16_l_017}"

    # サイト：（はぁ。
    s "(Sigh. It's started again…){#ch16_s_009}"

    menu:
        "Pray to heaven{#ch16_1_c_660_1}":
            jump ch16_1_scene_661
        "I'm tired today. Think tomorrow{#ch16_1_c_660_2}":
            jump ch16_1_scene_662
        "I'll cry{#ch16_1_c_660_3}":
            jump ch16_1_scene_663

label ch16_1_scene_661:

    # [SPRITE   lay1     image=+324, level=160, dir=1C]
    # [SPRITE   lay6     image=+704, level=160, dir=1C]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+12, level=200]
    $ fade_fx("id(12)")
    # サイト：（か、神さま……。
    s "(G-God… Have I done something wrong?){#ch16_s_010}"

    # [SPRITE   lay1     image=+328, level=160, dir=1C]
    # ルイズ：サイト、なに現実逃避してるの！  [voice 4592]
    voice "ch16_l_018"
    l "Saito, why are you escaping reality!{#ch16_l_018}"

    # ルイズ：何か言ってやりなさい！
    voice "ch16_l_019"
    l "Say something! Tell her you're mine!{#ch16_l_019}"

    # [SPRITE   lay6     image=+702, level=160, dir=1C]
    # キュルケ：なによ！
    voice "ch16_k_022"
    k "What! Darling is mine, right?{#ch16_k_022}"

    # サイト：（……た、助けて。
    s "(…H-Help me, God!){#ch16_s_011}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 664
    jump ch16_1_scene_664

label ch16_1_scene_662:

    # [SPRITE   lay1     image=+324, level=160, dir=1C]
    # [SPRITE   lay6     image=+704, level=160, dir=1C]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+12, level=200]
    $ fade_fx("id(12)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：疲れた。
    voice "ch16_s_012"
    s "I'm tired. I'm going to sleep.{#ch16_s_012}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+328, level=160, dir=1C]
    # [SPRITE   lay6     image=+704, level=160, dir=1C]
    # ルイズ：ちょっと、なによ！
    voice "ch16_l_020"
    l "Wait, what's this! Sleeping so irresponsibly!{#ch16_l_020}"

    # キュルケ：だ、ダーリン！  [voice 2687]
    voice "ch16_k_023"
    k "D-Darling!{#ch16_k_023}"

    # ルイズ：ま、まあいいわ！
    voice "ch16_l_021"
    l "Well, fine! Kirche, let's settle this today!{#ch16_l_021}"

    # [SPRITE   lay6     image=+702, level=160, dir=1C]
    # キュルケ：望むところよ！
    voice "ch16_k_024"
    k "Gladly! Come outside!{#ch16_k_024}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 664
    jump ch16_1_scene_664

label ch16_1_scene_663:

    # [SPRITE   lay1     image=+324, level=160, dir=1C]
    # [SPRITE   lay6     image=+704, level=160, dir=1C]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+12, level=200]
    $ fade_fx("id(12)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：（なんか、俺って貧乏くじばかり……）
    s "(Why do I always get the short straw…?){#ch16_s_013}"

    # サイト：（かわいい女の子ばかりなのに、
    s "(Surrounded by such cute girls, and there's me, who can't do anything…){#ch16_s_014}"

    # サイト：（チクショーーっ！）
    s "(Damn it!!){#ch16_s_015}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+324, level=160, dir=1C]
    # [SPRITE   lay6     image=+704, level=160, dir=1C]
    # キュルケ：……どうしたのよ、ダーリン。
    voice "ch16_k_025"
    k "…What's wrong, darling? Crying all of a sudden.{#ch16_k_025}"

    # [SPRITE   lay1     image=+330, level=160, dir=1C]
    # ルイズ：サ、サイト？  [voice 4596]
    voice "ch16_l_022"
    l "S-Saito?{#ch16_l_022}"

    # [SPRITE   lay1     image=+328, level=160, dir=1C]
    # ルイズ：なによ、こんなにかわいい
    voice "ch16_l_023"
    l "What's there to complain about, surrounded by such cute girls as us!{#ch16_l_023}"

    # [SPRITE   lay6     image=+702, level=160, dir=1C]
    # キュルケ：ダーリンが優柔不断なのが悪いんでしょ！  [voice 2690]
    voice "ch16_k_026"
    k "It's your fault for being indecisive, darling!{#ch16_k_026}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：……うっ。
    voice "ch16_s_016"
    s "…Ugh. Sorry.{#ch16_s_016}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+704, level=160, dir=1C]
    # [SPRITE   lay1     image=+330, level=160, dir=1C]
    # キュルケ：……ホントにもう、  [voice 2691]
    voice "ch16_k_027"
    k "…Really, you're…{#ch16_k_027}"

    # ルイズ：バカなんだから。  [voice 4598]
    voice "ch16_l_024"
    l "…such an idiot.{#ch16_l_024}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 664
    jump ch16_1_scene_664

label ch16_1_scene_664:

label ch16_1_scene_665:

    # [MOVIE movie(1)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+89, level=200]
    $ fade_fx("id(89)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：えっ、自立するってどういうことだよ？  [voice 9272]
    voice "ch16_s_017"
    s "Eh? What do you mean, 'becoming independent'?{#ch16_s_017}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+59, level=200]
    $ fade_fx("id(59)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：うん、いつまでもこの学院で……。
    voice "ch16_ha_001"
    ha "Well… I can't stay at this academy forever… I thought it was about time I stopped relying on Louise-san and the others.{#ch16_ha_001}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そんなこといったら、俺なんかルイズに
    voice "ch16_s_018"
    s "If you say that, I've been living off Louise's kindness ever since she summoned me, one way or another.{#ch16_s_018}"

    # ハルナ：平賀くんはルイズさんの使い魔じゃない。
    voice "ch16_ha_002"
    ha "Hiraga-kun is Louise-san's familiar, so of course. But I'm not…{#ch16_ha_002}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そりゃそうなんだけどさ……。
    voice "ch16_s_019"
    s "That's true, but… We're probably the only two Japanese people in this world.{#ch16_s_019}"

    # サイト：それに、お互いのことを知らない
    voice "ch16_s_020"
    s "And we're not exactly strangers to each other… So if I worked at the academy, maybe…{#ch16_s_020}"

    # [SPRITE   lay7     image=+959, level=160, dir=1A]
    # ハルナ：あのね、平賀くん……。
    voice "ch16_ha_003"
    ha "You see, Hiraga-kun… I've been scouted.{#ch16_ha_003}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ス、スカウトって、なんの？  [voice 9276]
    voice "ch16_s_021"
    s "S-Scouted for what?{#ch16_s_021}"

    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：劇団よ、劇団。  [voice 1805]
    voice "ch16_ha_004"
    ha "A troupe, a troupe.{#ch16_ha_004}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：劇団って、あのウェザリーの劇団のこと？  [voice 9277]
    voice "ch16_s_022"
    s "A troupe? You mean that Weatherly's troupe?{#ch16_s_022}"

    # ハルナ：違うの。
    voice "ch16_ha_005"
    ha "No. Someone from another troupe who saw that play liked me and scouted me.{#ch16_ha_005}"

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：この際、いい機会だから、その劇団のお世話に
    voice "ch16_ha_006"
    ha "I thought this was a good chance, so I'm going to join them.{#ch16_ha_006}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：でもさ、劇団の世話になるってことは、
    voice "ch16_s_023"
    s "But joining a troupe means performing in other towns, right?{#ch16_s_023}"

    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：うん、そうだね。
    voice "ch16_ha_007"
    ha "Yes. We'll probably see less of each other, Hiraga-kun.{#ch16_ha_007}"

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：でもね、私は楽しみにしてるんだ。
    voice "ch16_ha_008"
    ha "But I'm looking forward to it. I get to see so many towns in this world.{#ch16_ha_008}"

    # ハルナ：ひょっとすると、日本へ戻るためのきっかけ
    voice "ch16_ha_009"
    ha "Maybe I'll even find a clue to get back to Japan?{#ch16_ha_009}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そっか、そうだよな。  [voice 9279]
    voice "ch16_s_024"
    s "I see. Yeah, that's right.{#ch16_s_024}"

    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：だから平賀くん……。
    voice "ch16_ha_010"
    ha "So, Hiraga-kun… Please cheer me on, if you don't mind.{#ch16_ha_010}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：ああ、もちろんだとも！
    voice "ch16_s_025"
    s "Of course! And let's both do our best to find a way back to Japan!{#ch16_s_025}"

    # ハルナ：うん！  [voice 1812]
    voice "ch16_ha_011"
    ha "Mm!{#ch16_ha_011}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：ハァイ！
    voice "ch16_k_028"
    k "Hiiii! You two!{#ch16_k_028}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：キュルケ！  [voice 9281]
    voice "ch16_s_026"
    s "Kirche!{#ch16_s_026}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：キュルケさん！
    voice "ch16_ha_012"
    ha "Kirche-san! About before—I'm sorry. Back then…{#ch16_ha_012}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あ～～、別にいいわよ。  [voice 2882]
    voice "ch16_k_029"
    k "Ah, it's fine.{#ch16_k_029}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：終わったことをいつまでも言ってたんじゃ、
    voice "ch16_k_030"
    k "If I kept harping on what's past, the name of Kirche with a slight fever would cry.{#ch16_k_030}"

    # ハルナ：は、はい。
    voice "ch16_ha_013"
    ha "Y-Yes. Um…{#ch16_ha_013}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：……。
    k "…{#ch16_k_031}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：あ、そうそう！  [voice 2884]
    voice "ch16_k_032"
    k "Ah, right!{#ch16_k_032}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：ハルナのために、餞別を送ろうと思ってね。
    voice "ch16_k_033"
    k "I wanted to give Haruna a parting gift. I've prepared a special spell for her.{#ch16_k_033}"

    # [SPRITE   lay7     image=+984, level=160, dir=2A]
    # ハルナ：え、そんな……。  [voice 1815]
    voice "ch16_ha_014"
    ha "Eh, such a thing…{#ch16_ha_014}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：……これが本当の、『火の魔法』の使い方よ。  [voice 2886]
    voice "ch16_k_034"
    k "…This is the true way to use 'fire' magic.{#ch16_k_034}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+290, level=80]
    $ dissolve_fx("id(290)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+63]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # ハルナ：花火だ。  [voice 1816]
    voice "ch16_ha_015"
    ha "Fireworks.{#ch16_ha_015}"

    # サイト：すげえ。  [voice 9282]
    voice "ch16_s_027"
    s "Wow.{#ch16_s_027}"

    # ハルナ：……。
    ha "…{#ch16_ha_016}"

    # ハルナ：キュルケさん。  [voice 1817]
    voice "ch16_ha_017"
    ha "Kirche-san.{#ch16_ha_017}"

    # ハルナ：平賀くんのことをよろしくお願いします。  [voice 1818]
    voice "ch16_ha_018"
    ha "Please take care of Hiraga-kun.{#ch16_ha_018}"

    # キュルケ：へ？  [voice 2887]
    voice "ch16_k_035"
    k "Huh?{#ch16_k_035}"

    # ハルナ：……。  [voice 1819]
    voice "ch16_ha_019"
    ha "…{#ch16_ha_019}"

    # キュルケ：え？
    voice "ch16_k_036"
    k "Eh? Ah… Yes…{#ch16_k_036}"

    # キュルケ：なんか、よく分かんないけど……。
    voice "ch16_k_037"
    k "I don't quite get it, but… Okay.{#ch16_k_037}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay7     image=+986, level=160, dir=2A]
    # ハルナ：まあ、預けるだけですけどね。
    voice "ch16_ha_020"
    ha "Well, it's not like I'm entrusting him to you… Just don't let that Louise break him.{#ch16_ha_020}"

    # [SPRITE   lay7     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なんの話をしてるんだ？  [voice 9283]
    voice "ch16_s_028"
    s "What are you talking about?{#ch16_s_028}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：うふふ、さあ？  [voice 2890]
    voice "ch16_k_038"
    k "Ufufu, why don't you guess?{#ch16_k_038}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：平賀くん！
    voice "ch16_ha_021"
    ha "Hiraga-kun! Be careful with girls.{#ch16_ha_021}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：は、はいっ！  [voice 9284]
    voice "ch16_s_029"
    s "Y-Yes!{#ch16_s_029}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # null：………。 (no voice)
    # [BG       stage    hide]
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # サイト：ああ、行っちゃったか……。  [voice 9285]
    voice "ch16_s_030"
    s "Ah, she's gone, huh…{#ch16_s_030}"

    # キュルケ：あら、ダーリン。
    voice "ch16_k_039"
    k "Oh, darling. Are you lonely?{#ch16_k_039}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そりゃ、まあ……。
    voice "ch16_s_031"
    s "Well… She was like the only friend I had. And now my little sister's gone too…{#ch16_s_031}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：いもうと？  [voice 2892]
    voice "ch16_k_040"
    k "Little sister?{#ch16_k_040}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：いやいや、なんでも！  [voice 9287]
    voice "ch16_s_032"
    s "No, nothing!{#ch16_s_032}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（……キュルケは子供になってたときの記憶は
    s "(Kirche doesn't seem to remember being a child…){#ch16_s_033}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：……。
    k "…{#ch16_k_041}"

    menu:
        "Of course it was good, though!{#ch16_1_c_665_1}":
            jump ch16_1_scene_666
        "Happy and sad at the same time…{#ch16_1_c_665_2}":
            jump ch16_1_scene_667
        "Maybe I liked it that way better…?{#ch16_1_c_665_3}":
            jump ch16_1_scene_668

label ch16_1_scene_666:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（も、もちろん良かったんだけどね！
    s "(O-Of course it was good! Though that imbalance was something else…){#ch16_s_034}"

    # サイト：……ハァ。  [voice 9288]
    voice "ch16_s_035"
    s "…Haa.{#ch16_s_035}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：くすっ、くす。  [voice 2893]
    voice "ch16_k_042"
    k "Heh, heh.{#ch16_k_042}"

    # → next scene 669
    jump ch16_1_scene_669

label ch16_1_scene_667:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # サイト：（うれしいような寂しいような……。
    s "(Happy and sad… Mixed feelings. And that imbalance was exquisite…){#ch16_s_036}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：……ダーリン？  [voice 2894]
    voice "ch16_k_043"
    k "…Darling?{#ch16_k_043}"

    # → next scene 669
    jump ch16_1_scene_669

label ch16_1_scene_668:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：……あっちのほうが良かったかも？  [voice 9289]
    voice "ch16_s_037"
    s "…Maybe I liked it that way better?{#ch16_s_037}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：もうっ、ダーリンったら！  [voice 2895]
    voice "ch16_k_044"
    k "Geez, darling!{#ch16_k_044}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：……あっちってなによ？  [voice 2896]
    voice "ch16_k_045"
    k "What do you mean, 'that way'?{#ch16_k_045}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：え？
    voice "ch16_s_038"
    s "Eh? Ah, no—Ahahaha…{#ch16_s_038}"

    # → next scene 669
    jump ch16_1_scene_669

label ch16_1_scene_669:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：もう、ダーリンったら、
    voice "ch16_k_046"
    k "Really, darling, with me right here, what are you thinking about!{#ch16_k_046}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+119, level=80]
    $ dissolve_fx("id(119)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [SPRITE   lay7     vibrate=7]
    # [SPRITE   lay6     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # サイト：うわっ！
    voice "ch16_s_039"
    s "Whoa! If you hug me like that, all sorts of things…!{#ch16_s_039}"

    # キュルケ：うふふ、もしかして、
    voice "ch16_k_047"
    k "Ufufu. Were you thinking something naughty?{#ch16_k_047}"

    # サイト：え？  [voice 9292]
    voice "ch16_s_040"
    s "Eh?{#ch16_s_040}"

    # キュルケ：もう、だめよ？
    voice "ch16_k_048"
    k "No, you can't! Big brother?{#ch16_k_048}"

    # サイト：……え？  [voice 9293]
    voice "ch16_s_041"
    s "…Eh?{#ch16_s_041}"

    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay5     hide, vibrate=7]
    # [SPRITE   lay7     vibrate=7]
    # [SPRITE   lay6     hide, vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # サイト：ええ！？  [voice 9294]
    voice "ch16_s_042"
    s "Eh!?{#ch16_s_042}"

    # キュルケ：うふふ！  [voice 2900]
    voice "ch16_k_049"
    k "Ufufu!{#ch16_k_049}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # ==== КОНЕЦ ГЛАВЫ 16 ====
    jump ch17
    return

