# Глава 15, часть 3 (сцены 643–653): лекарство, возвращение Кирке.
# Источник: ps2_source/chapters/chapter_16_魔法の薬.txt (SCENE 643-653).

label ch15_3:
    $ tndl(None)
    $ show_sprites()

label ch15_3_scene_643:

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：それでもやるしかないか。  [voice 13087]
    voice "ch15_s_073"
    s "Even so, we have no choice but to do it, huh.{#ch15_s_073}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そうね。
    voice "ch15_l_065"
    l "Right. We don't have time to wait for Kirche to recover.{#ch15_l_065}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：そうなると、うまくいくかどうかは、
    voice "ch15_l_066"
    l "So it all comes down to you. Make sure you protect me, okay? {#ch15_l_066}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：へっ、任せておけよ。
    voice "ch15_s_074"
    s "Heh, leave it to me. I'm Louise's familiar. I'll guard you until the chanting is done.{#ch15_s_074}"

    # [SPRITE   lay5     level=154]
    # [SPRITE   lay1     level=153]
    # [SPRITE   lay19    image=+942, level=147, dir=1A]
    # デルフリンガー：その意気だぜ、相棒！  [voice 1364]
    voice "ch15_d_003"
    d "That's the spirit, partner!{#ch15_d_003}"

    # → next scene 646
    jump ch15_3_scene_646

label ch15_3_scene_644:

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：なあ、やっぱり虚無を使うべきじゃないん
    voice "ch15_s_075"
    s "Say… maybe we shouldn't use Void after all?{#ch15_s_075}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：危険すぎると思うんだけど。  [voice 13090]
    voice "ch15_s_076"
    s "It's too dangerous, I think.{#ch15_s_076}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：虚無の魔法はひとつではないって、
    voice "ch15_l_067"
    l "How many times do I have to tell you Void magic isn't just one thing?{#ch15_l_067}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：お願い今はわたしを信じて……。
    voice "ch15_l_068"
    l "Please, trust me for now… If you believe, it becomes strength.{#ch15_l_068}"

    # → next scene 646
    jump ch15_3_scene_646

label ch15_3_scene_645:

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：キュルケの代わりに、ギーシュ……ってだめ？  [voice 13091]
    voice "ch15_s_077"
    s "Can't Guiche take Kirche's place… no, right?{#ch15_s_077}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：あんた、本気で言ってる？  [voice 7117]
    voice "ch15_l_069"
    l "Are you serious?{#ch15_l_069}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：だよね、ですよね。
    voice "ch15_s_078"
    s "Yeah, I thought so. I knew it.{#ch15_s_078}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：とにかく、ルイズを俺は信じるよ。
    voice "ch15_s_079"
    s "Anyway, I trust you, Louise. I'll definitely protect you. So go ahead and unleash Void!{#ch15_s_079}"

    # → next scene 646
    jump ch15_3_scene_646

label ch15_3_scene_646:

    # [SPRITE   lay5     image=+405, level=154, dir=1B]
    # [SPRITE   lay1     image=+335, level=153, dir=2A]
    # [SPRITE   lay19    image=+942, level=147, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay19    hide]
    # [BG       stage    hide]
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay19    image=+940, level=147, dir=1A]
    # [SPRITE   lay5     image=+401, level=154, dir=1B]
    # デルフリンガー：しかし、相棒。
    voice "ch15_d_004"
    d "But, partner—even if you've decided to believe…{#ch15_d_004}"

    # [SPRITE   lay5     image=+440, level=154, dir=2B]
    # サイト：ルイズの虚無の魔法の詠唱が終わるまで
    voice "ch15_s_080"
    s "Buying time until Louise's Void chant finishes is going to be tough, huh.{#ch15_s_080}"

    # [SPRITE   lay5     image=+401, level=154, dir=1B]
    # サイト：ルイズが抜けるってことは、
    voice "ch15_s_081"
    s "If Louise is out of it, the main force will be just me and Tabitha.{#ch15_s_081}"

    # [SPRITE   lay5     image=+407, level=154, dir=1B]
    # サイト：せめて、キュルケが間に合ってくれてれば……。  [voice 13096]
    voice "ch15_s_082"
    s "If only Kirche could make it in time…{#ch15_s_082}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # キュルケ：どうかしたの、おにいちゃん？
    voice "ch15_k_020"
    k "What's wrong, big brother? Is Kirche being a burden?{#ch15_k_020}"

    # [SPRITE   lay5     image=+434, level=154, dir=2B]
    # サイト：な、なんでもないぞ、怖がらなくていいから。  [voice 13097]
    voice "ch15_s_083"
    s "N-Nothing! Don't be scared.{#ch15_s_083}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay3     image=+852, level=149, dir=1A]
    # モンモランシー：あら、どうしたのよ。
    voice "ch15_m_008"
    m "My, what's with these long faces?{#ch15_m_008}"

    # [SPRITE   lay3     x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=154, dir=1B]
    # サイト：あ、モンモン！
    voice "ch15_s_084"
    s "Ah, Montmon! How much longer for Kirche's medicine?{#ch15_s_084}"

    # [SPRITE   lay3     image=+885, level=149, dir=2A]
    # モンモランシー：完成したわよ……一応ね。  [voice 4149]
    voice "ch15_m_009"
    m "It's done… more or less.{#ch15_m_009}"

    # [SPRITE   lay5     image=+440, level=154, dir=2B]
    # サイト：へっ？
    voice "ch15_s_085"
    s "Heh? Really?{#ch15_s_085}"

    # [SPRITE   lay3     image=+856, level=149, dir=1A]
    # モンモランシー：なによ、疑うの？
    voice "ch15_m_010"
    m "What, you doubt me? After rushing me so hard.{#ch15_m_010}"

    # [SPRITE   lay5     image=+403, level=154, dir=1B]
    # サイト：疑わない、疑わないって！
    voice "ch15_s_086"
    s "I don't doubt you, I don't! All right!!{#ch15_s_086}"

    # [SPRITE   lay3     image=+852, level=149, dir=1A]
    # モンモランシー：それとウェザリーの暗示に対抗するための
    voice "ch15_m_011"
    m "I also prepared medicine and a spell against Weatherly's suggestion. We'll use it later.{#ch15_m_011}"

    # [SPRITE   lay5     image=+434, level=154, dir=2B]
    # サイト：よしっ、キュルケ……。
    voice "ch15_s_087"
    s "All right, Kirche… here, take this medicine…{#ch15_s_087}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay6     image=+715, level=151, dir=2A]
    # キュルケ：え、ええと。
    voice "ch15_k_021"
    k "U-Um. Do I really have to drink it?{#ch15_k_021}"

    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # キュルケ：あ、あのね、おにいちゃん……。
    voice "ch15_k_022"
    k "You see, big brother… Kirche doesn't like medicine…{#ch15_k_022}"

    menu:
        "Don't be a brat…{#ch15_3_c_646_1}":
            jump ch15_3_scene_648
        "…What should I do{#ch15_3_c_646_2}":
            jump ch15_3_scene_649
        "If it comes to this!{#ch15_3_c_646_3}":
            jump ch15_3_scene_650

    # → next scene 647
    jump ch15_3_scene_647

    # → next scene 652 (альтернативная ветка — пропущена)
label ch15_3_scene_647:

    # [SPRITE   lay5     image=+434, level=154, dir=2B]
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
label ch15_3_scene_648:

    # [SPRITE   lay5     image=+434, level=154, dir=2B]
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # キュルケ：にがいおくすり……いや。  [voice 3785]
    voice "ch15_k_023"
    k "Bitter medicine… no.{#ch15_k_023}"

    # [SPRITE   lay5     image=+440, level=154, dir=2B]
    # サイト：なあ、キュルケ。
    voice "ch15_s_088"
    s "Come on, Kirche. Don't be difficult…{#ch15_s_088}"

    # [SPRITE   lay5     image=+403, level=154, dir=1B]
    # サイト：苦くない苦くないって！  [voice 13103]
    voice "ch15_s_089"
    s "It's not bitter, not bitter!{#ch15_s_089}"

    # [SPRITE   lay6     image=+711, level=151, dir=2A]
    # キュルケ：ホント、おにいちゃん？  [voice 3786]
    voice "ch15_k_024"
    k "Really, big brother?{#ch15_k_024}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay3     image=+858, level=149, dir=1A]
    # モンモランシー：アカグサの実が入ってるから、
    voice "ch15_m_012"
    m "It has akagusa fruit in it, so it'll be pretty bitter. That stuff is too bitter to eat raw.{#ch15_m_012}"

    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # キュルケ：じゃ、ぜーったいいや！  [voice 3787]
    voice "ch15_k_025"
    k "Then abso-lutely no!{#ch15_k_025}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay5     image=+405, level=154, dir=1B]
    # サイト：モンモン！
    voice "ch15_s_090"
    s "Montmon! Don't interfere!{#ch15_s_090}"

    # → next scene 651
    jump ch15_3_scene_651

label ch15_3_scene_649:

    # [SPRITE   lay5     image=+434, level=154, dir=2B]
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # キュルケ：にがいおくすり……いや。  [voice 3788]
    voice "ch15_k_026"
    k "Bitter medicine… no.{#ch15_k_026}"

    # [SPRITE   lay5     image=+440, level=154, dir=2B]
    # サイト：ど、どうしたら
    voice "ch15_s_091"
    s "What'll it take to get you to drink it?{#ch15_s_091}"

    # [SPRITE   lay5     image=+403, level=154, dir=1B]
    # サイト：そうだ。
    voice "ch15_s_092"
    s "Right. Here, Kirche—{#ch15_s_092}"

    # サイト：このお薬飲んだら、後で抱っこしてあげるぞー。  [voice 13107]
    voice "ch15_s_093"
    s "If you drink this, I'll hold you afterwards!{#ch15_s_093}"

    # [SPRITE   lay6     image=+711, level=151, dir=2A]
    # キュルケ：ほんと？  [voice 3789]
    voice "ch15_k_027"
    k "Really?{#ch15_k_027}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=153, dir=1A]
    # ルイズ：だめっ！
    voice "ch15_l_070"
    l "No! Absolutely not!{#ch15_l_070}"

    # [SPRITE   lay5     image=+407, level=154, dir=1B]
    # サイト：おいおい、ルイズ！  [voice 13108]
    voice "ch15_s_094"
    s "Hey now, Louise!{#ch15_s_094}"

    # [SPRITE   lay1     image=+343, level=153, dir=2A]
    # ルイズ：あ……つい……。  [voice 7119]
    voice "ch15_l_071"
    l "Ah… I spoke too soon.{#ch15_l_071}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # キュルケ：だっこしてくれないの？
    voice "ch15_k_028"
    k "You won't hold me? Then I absolutely won't drink it!{#ch15_k_028}"

    # → next scene 651
    jump ch15_3_scene_651

label ch15_3_scene_650:

    # [SPRITE   lay5     image=+434, level=154, dir=2B]
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+405, level=154, dir=1B]
    # サイト：こうなったら！  [voice 13109]
    voice "ch15_s_095"
    s "If it comes to this!{#ch15_s_095}"

    # サイト：責任は俺が取る。  [voice 13110]
    voice "ch15_s_096"
    s "I'll take responsibility.{#ch15_s_096}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+308, level=153, dir=1A]
    # ルイズ：責任って……どうするつもり？  [voice 7120]
    voice "ch15_l_072"
    l "Responsibility… what are you planning?{#ch15_l_072}"

    # → next scene 651
    jump ch15_3_scene_651

label ch15_3_scene_651:

    # [SPRITE   lay5     image=+405, level=154, dir=1B]
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     x=144, y=416]
    # [SPRITE   lay5     image=+405, level=154, dir=1B]
    # サイト：くそっ、もう世話の焼ける！  [voice 13111]
    voice "ch15_s_097"
    s "Damn, what a handful!{#ch15_s_097}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=153, dir=1A]
    # ルイズ：ち、ちょっとサイト！
    voice "ch15_l_073"
    l "W-Wait, Saito! What are you doing drinking it—!?{#ch15_l_073}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+255, level=80]
    $ dissolve_fx("id(255)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+14]
    play music t13 fadein 1.0
    # ルイズ：あ、ああああああっ！  [voice 7122]
    voice "ch15_l_074"
    l "A-Aaaaaah!{#ch15_l_074}"

    # サイト：……。  [voice 13112]
    voice "ch15_s_098"
    s "…{#ch15_s_098}"

    # キュルケ：……。  [voice 3791]
    voice "ch15_k_029"
    k "…{#ch15_k_029}"

    # キュルケ：お、おにいちゃん……。  [voice 3792]
    voice "ch15_k_030"
    k "B-Big brother…{#ch15_k_030}"

    # ルイズ：ななな、何してるのよバカ犬！  [voice 7123]
    voice "ch15_l_075"
    l "W-What are you doing, stupid dog!{#ch15_l_075}"

    # サイト：ご、誤解するな！
    voice "ch15_s_099"
    s "D-Don't get the wrong idea! I just fed it to her mouth-to-mouth!{#ch15_s_099}"

    # キュルケ：おくちがにがいよぉ……！  [voice 3793]
    voice "ch15_k_031"
    k "My mouth tastes bitter…!{#ch15_k_031}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay6     image=+676, level=151, dir=1A]
    # キュルケ：ひくっ！
    voice "ch15_k_032"
    k "Hic! Huh?{#ch15_k_032}"

    # → next scene 653
    jump ch15_3_scene_653

label ch15_3_scene_652:

    # [SPRITE   lay5     image=+434, level=154, dir=2B]
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+302, level=153, dir=1A]
    # ルイズ：もうっ！
    voice "ch15_l_076"
    l "Honestly! What a handful!{#ch15_l_076}"

    # [SPRITE   lay1     image=+306, level=153, dir=1A]
    # ルイズ：ほらっ！
    voice "ch15_l_077"
    l "Here! Drink it, Kirche!{#ch15_l_077}"

    # ルイズ：飲むのよーーッ！  [voice 7126]
    voice "ch15_l_078"
    l "Drink it already—!{#ch15_l_078}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # キュルケ：やだーーーっ！
    voice "ch15_k_033"
    k "Noooo! …Gulp.{#ch15_k_033}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay3     image=+856, level=149, dir=1A]
    # モンモランシー：ち、ちょっとルイズっ！
    voice "ch15_m_013"
    m "H-Hey, Louise! That's too much!{#ch15_m_013}"

    # [SPRITE   lay1     image=+302, level=153, dir=1A]
    # ルイズ：……。  [voice 7127]
    voice "ch15_l_079"
    l "…{#ch15_l_079}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # キュルケ：ル、ルイズおねぇちゃん……ひどい。  [voice 3796]
    voice "ch15_k_034"
    k "L-Louise onee-chan… that was mean.{#ch15_k_034}"

    # キュルケ：お、おくちが、にがいよぉーーっ！  [voice 3797]
    voice "ch15_k_035"
    k "M-My mouth is bitter…!{#ch15_k_035}"

    # [SPRITE   lay6     image=+676, level=151, dir=1A]
    # キュルケ：……ひくっ！
    voice "ch15_k_036"
    k "…Hic! Huh?{#ch15_k_036}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=154, dir=1B]
    # サイト：な、なんだよっ！  [voice 13114]
    voice "ch15_s_100"
    s "W-What was that!?{#ch15_s_100}"

    # → next scene 653
    jump ch15_3_scene_653

label ch15_3_scene_653:

    # [SPRITE   lay5     image=+405, level=154, dir=1B]
    # [SPRITE   lay6     image=+676, level=151, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay3     image=+852, level=149, dir=1A]
    # モンモランシー：効きはじめたわ。  [voice 4154]
    voice "ch15_m_014"
    m "It's starting to work.{#ch15_m_014}"

    # [SPRITE   lay3     x=224, y=0]
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # キュルケ：あれあれあれあれあれ？  [voice 3799]
    voice "ch15_k_037"
    k "Huh huh huh huh huh?{#ch15_k_037}"

    # キュルケ：ダーリン……？
    voice "ch15_k_038"
    k "Darling…? Louise…? What was I doing?{#ch15_k_038}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay5     image=+403, level=154, dir=1B]
    # サイト：良かった！
    voice "ch15_s_101"
    s "Thank goodness! Kirche's back! Now we can win!{#ch15_s_101}"

    # [SPRITE   lay6     image=+715, level=151, dir=2A]
    # キュルケ：一体なんのこと？
    voice "ch15_k_039"
    k "What's going on? What's this explosion? What happened?{#ch15_k_039}"

    # [SPRITE   lay5     image=+405, level=154, dir=1B]
    # サイト：説明は後！
    voice "ch15_s_102"
    s "Explanations later! Montmon, the anti-suggestion thing, please!{#ch15_s_102}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay3     image=+856, level=149, dir=1A]
    # モンモランシー：じゃ、いくわよ。  [voice 4155]
    voice "ch15_m_015"
    m "Right, here I go.{#ch15_m_015}"

    # [SE       se0      play=+94]
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay16    x=304, y=416]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay5     image=+407, level=154, dir=1B]
    # [LAYER    lay0     x=464, y=416]
    # [SPRITE   lay15    x=304, y=416]
    # [SPRITE   lay4     x=304, y=416]
    # [SPRITE   lay1     x=144, y=416]
    # [SPRITE   lay19    x=144, y=416]
    # [SPRITE   lay6     image=+682, level=151, dir=1A]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # キュルケ：ううっ、まだ頭がボーッとするわ。  [voice 3802]
    voice "ch15_k_040"
    k "Ugh, my head is still spinning.{#ch15_k_040}"

    # サイト：大丈夫か、キュルケ……。  [voice 13117]
    voice "ch15_s_103"
    s "You okay, Kirche…?{#ch15_s_103}"

    # キュルケ：ええ、ダーリン。
    voice "ch15_k_041"
    k "Yes, darling. Just a little dizzy…{#ch15_k_041}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=153, dir=1A]
    # ルイズ：くっつきすぎよ！
    voice "ch15_l_080"
    l "You're too close! Both of you, step back!{#ch15_l_080}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay6     image=+715, level=151, dir=2A]
    # キュルケ：もう、病み上がりなのよ。
    voice "ch15_k_042"
    k "I'm still recovering. Be a little gentler with me.{#ch15_k_042}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SE       se0      play=+57]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay15    image=+1116, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # 味方Ａ：ルイズ・フランソワーズ殿に緊急連絡！
    voice "ch15_soldier_009"
    soldier "Urgent message for Louise Francoise! Reconquista warships have entered Tristain's defense zone!{#ch15_soldier_009}"

    # 味方Ａ：一部、敵部隊は王宮制圧を狙い降下作戦を
    voice "ch15_soldier_010"
    soldier "Reports also say part of the enemy force is descending, aiming to seize the palace.{#ch15_soldier_010}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay1     image=+306, level=153, dir=1A]
    # [SPRITE   lay5     image=+405, level=154, dir=1B]
    # ルイズ：なんですって！  [voice 7129]
    voice "ch15_l_081"
    l "What!?{#ch15_l_081}"

    # サイト：いよいよ来たってことか。  [voice 13118]
    voice "ch15_s_104"
    s "So it's finally here, huh.{#ch15_s_104}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay4     image=+559, level=150, dir=1A]
    # ギーシュ：くそぅ、役者風情と馬鹿にしてたら……。
    voice "ch15_g_001"
    g "Damn, we wrote them off as mere actors… It was all a play… Weatherly.{#ch15_g_001}"

    # [SPRITE   lay1     image=+302, level=153, dir=1A]
    # ルイズ：催眠術……役者……芝居……。
    voice "ch15_l_082"
    l "Hypnosis… actors… a play… Right.{#ch15_l_082}"

    # [SPRITE   lay1     image=+335, level=153, dir=2A]
    # ルイズ：いいわ、あのウェザリーには
    voice "ch15_l_083"
    l "Fine. I'll make that Weatherly regret this.{#ch15_l_083}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay4     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 654
    jump ch15_4

    # ==== КОНЕЦ ЧАСТИ 3 ====
    jump ch15_4
    return

