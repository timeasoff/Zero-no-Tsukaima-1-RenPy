# Глава 18, часть 1 (сцены 696–705): «貴族の意地» — возвращение, Акина.
# Источник: ps2_source/chapters/chapter_19_貴族の意地.txt (SCENE 696-705).

label ch18:
    $ tndl(None)
    $ show_sprites()

label ch18_1_scene_696:

    # [TITLE title("貴族の意地")]
    # [BG       stage    image=+85, level=200]
    $ fade_fx("id(85)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+3]
    play music t2 fadein 1.0
    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # 味方Ａ：どうやら包囲網を抜けることができたようです。
    voice "ch18_soldier_008"
    soldier "We seem to have slipped through the encirclement. That's where our escort ends, Valliere-sama, Saito-sama.{#ch18_soldier_008}"

    # 味方Ａ：できれば学院までお送りしたいところですが、
    voice "ch18_soldier_009"
    soldier "We'd like to see you to the academy, but protecting the capital and Her Majesty comes first right now.{#ch18_soldier_009}"

    # [SPRITE   lay15    level=160]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：ええ、ご苦労さま。
    voice "ch18_l_061"
    l "Yes, thank you. Please convey my thanks to the Queen.{#ch18_l_061}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+390, level=156, dir=1A]
    # サイト：ここまでありがとうございます。
    voice "ch18_s_083"
    s "Thanks for everything. Get back safely.{#ch18_s_083}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay15    x=0, y=0]
    # 味方Ａ：はっ、それでは……。  [voice 4235]
    voice "ch18_soldier_010"
    soldier "Yes, then…{#ch18_soldier_010}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay15    hide]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1134, level=200]
    $ fade_fx("id(1134)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 2000)]
    # [EVENT_CG event    image=+148, level=80]
    $ dissolve_fx("id(148)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # サイト：あの兵士さん、帰り大丈夫かなぁ。  [voice 11771]
    voice "ch18_s_084"
    s "I wonder if that soldier will be all right going back…{#ch18_s_084}"

    # ルイズ：大丈夫よ。
    voice "ch18_l_062"
    l "He will. Surely.{#ch18_l_062}"

    # [EVENT_CG event    image=+149, level=80]
    $ dissolve_fx("id(149)")
    # サイト：きっとってなぁ……。
    voice "ch18_s_085"
    s "Surely, huh… The cannons will get more active as time passes, won't they?{#ch18_s_085}"

    # ルイズ：わたし達はわたし達の仕事をこなすことが
    voice "ch18_l_063"
    l "Our priority is to do our own jobs. Right?{#ch18_l_063}"

    # サイト：うっ。  [voice 11773]
    voice "ch18_s_086"
    s "Ugh.{#ch18_s_086}"

    # ルイズ：それより今は一刻も早く学院に戻って、
    voice "ch18_l_064"
    l "More importantly, let's get back to the academy as fast as we can and return to Tristain in the Zero Fighter.{#ch18_l_064}"

    # [EVENT_CG event    image=+148, level=80]
    $ dissolve_fx("id(148)")
    # サイト：……。  [voice 11774]
    voice "ch18_s_087"
    s "…{#ch18_s_087}"

    # ルイズ：サイト？  [voice 6326]
    voice "ch18_l_065"
    l "Saito?{#ch18_l_065}"

    # サイト：なぁルイズ、昨日の夜も言ったけど、
    voice "ch18_s_088"
    s "Louise, like I said last night… are you really okay with this?{#ch18_s_088}"

    # ルイズ：な、なにがよ？  [voice 6327]
    voice "ch18_l_066"
    l "W-What's 'okay'?!{#ch18_l_066}"

    # サイト：俺はできれば、戦場に行きたくない。
    voice "ch18_s_089"
    s "I'd rather not go to the battlefield. And I don't want you to go either.{#ch18_s_089}"

    # ルイズ：……。  [voice 6328]
    voice "ch18_l_067"
    l "…{#ch18_l_067}"

    # サイト：そりゃあ俺はおまえの使い魔だから、
    voice "ch18_s_090"
    s "Sure, I'm your familiar—if you order me, I'll go with you to the battlefield. But…{#ch18_s_090}"

    # サイト：（できれば、ルイズにはこれ以上危険な
    s "(I don't want Louise to be in danger again.){#ch18_s_091}"

    # サイト：（前はたまたま成功しただけなんだ。
    s "(That last time was just luck. It doesn't mean we'll succeed this time either.){#ch18_s_092}"

    # [EVENT_CG event    image=+150, level=80]
    $ dissolve_fx("id(150)")
    # ルイズ：もういい！  [voice 6329]
    voice "ch18_l_068"
    l "Enough!{#ch18_l_068}"

    # サイト：ルイズ……。  [voice 11778]
    voice "ch18_s_093"
    s "Louise…{#ch18_s_093}"

    # ルイズ：あんたがグダグダ言うなら、
    voice "ch18_l_069"
    l "If you keep waffling, I'll go alone.{#ch18_l_069}"

    # [EVENT_CG event    image=+151, level=80]
    $ dissolve_fx("id(151)")
    # サイト：いや、俺が戦いに行きたくねーって
    voice "ch18_s_094"
    s "That's not what I'm saying—that I don't want to fight. Don't you get it?{#ch18_s_094}"

    # ルイズ：道中うだうだ言っててもはじまらないわ。
    voice "ch18_l_070"
    l "Dawdling on the road won't help. Right now, too, Tristain and the Queen are in danger.{#ch18_l_070}"

    # ルイズ：あんたもわたしの使い魔なら、少しは……、
    voice "ch18_l_071"
    l "If you're my familiar, you should at least… Ah, what's that!?{#ch18_l_071}"

    # [SE       se0      play=+67]
    # [SE       se0      play=+66]
    # [EVENT_CG event    image=+148, level=80]
    $ dissolve_fx("id(148)")
    # サイト：この音は？
    voice "ch18_s_095"
    s "That sound? U-Up there!?{#ch18_s_095}"

    # [EVENT_CG event    image=+130, level=80]
    $ dissolve_fx("id(130)")
    # ルイズ：シルフィードだわ！
    voice "ch18_l_072"
    l "It's Sylphid! Tabitha's familiar!{#ch18_l_072}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+85, level=200]
    $ fade_fx("id(85)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [LAYER    lay0     image=+588, level=154, dir=1A]
    # タバサ：見つけた。  [voice 15585]
    voice "ch18_t_004"
    t "Found you.{#ch18_t_004}"

    # [LAYER    lay0     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=156, dir=1A]
    # サイト：やっぱりタバサか。
    voice "ch18_s_096"
    s "So it is Tabitha. Came to pick us up?{#ch18_s_096}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：ちょうどいいわ、すぐにわたし達を学院まで
    voice "ch18_l_073"
    l "Perfect. Take us to the academy at once. The capital is…{#ch18_l_073}"

    # タバサ：はやく乗って。
    voice "ch18_t_005"
    t "Hurry. Get on.{#ch18_t_005}"

    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：急いでって、どうして？
    voice "ch18_l_074"
    l "Hurry? Why? Something happen at the academy?{#ch18_l_074}"

    # [LAYER    lay0     image=+594, level=154, dir=1A]
    # タバサ：ハルナが暴れてる。  [voice 15587]
    voice "ch18_t_006"
    t "Haruna's gone wild.{#ch18_t_006}"

    menu:
        "Haruna? No way!{#ch18_1_c_696_1}":
            jump ch18_1_scene_697
        "Is it really Haruna?{#ch18_1_c_696_2}":
            jump ch18_1_scene_698
        "What happened to you, Haruna…?{#ch18_1_c_696_3}":
            jump ch18_1_scene_699

label ch18_1_scene_697:

    # [LAYER    lay0     image=+594, level=154, dir=1A]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+85, level=200]
    $ fade_fx("id(85)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+394, level=156, dir=1A]
    # サイト：な……春奈が？
    voice "ch18_s_097"
    s "Haruna? No way!{#ch18_s_097}"

    # サイト：あいつは魔法なんて使えないし、
    voice "ch18_s_098"
    s "She can't use magic, and she can't even handle a weapon properly!{#ch18_s_098}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：そうよ！
    voice "ch18_l_075"
    l "Right! She's just a commoner, no matter how you look at her.{#ch18_l_075}"

    # → next scene 700
    jump ch18_1_scene_700

label ch18_1_scene_698:

    # [LAYER    lay0     image=+594, level=154, dir=1A]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+85, level=200]
    $ fade_fx("id(85)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+394, level=156, dir=1A]
    # サイト：そ、それは本当に春奈なのか？
    voice "ch18_s_099"
    s "T-That really is Haruna? Are you sure you're not mistaken?{#ch18_s_099}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：そ、そうよ。
    voice "ch18_l_076"
    l "Y-Yes. A commoner throwing a tantrum couldn't beat Kirche, could she?{#ch18_l_076}"

    # → next scene 700
    jump ch18_1_scene_700

label ch18_1_scene_699:

    # [LAYER    lay0     image=+594, level=154, dir=1A]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+85, level=200]
    $ fade_fx("id(85)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+429, level=156, dir=2A]
    # サイト：急にどうしちゃったんだ、春奈……。  [voice 11785]
    voice "ch18_s_100"
    s "What's happened to you, Haruna…?{#ch18_s_100}"

    # サイト：でも、春奈がちょっと暴れたからって
    voice "ch18_s_101"
    s "Even if Haruna went wild, would the academy explode into chaos?{#ch18_s_101}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：そうよ！
    voice "ch18_l_077"
    l "Right! She was just a normal girl who couldn't use magic.{#ch18_l_077}"

    # → next scene 700
    jump ch18_1_scene_700

label ch18_1_scene_700:

    # [SPRITE   lay5     image=+394, level=156, dir=1A]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+85, level=200]
    $ fade_fx("id(85)")
    # [SPRITE   lay5     image=+396, level=156, dir=1A]
    # サイト：とにかく事情を説明してくれ。
    voice "ch18_s_102"
    s "Explain what's going on. Haruna has no reason to go wild.{#ch18_s_102}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+594, level=154, dir=1A]
    # タバサ：わたしも分からない。
    voice "ch18_t_007"
    t "I don't know either. Maybe Kirche doesn't.{#ch18_t_007}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：分かったわ。
    voice "ch18_l_078"
    l "I see. Let's hurry anyway.{#ch18_l_078}"

    # サイト：お、おう。  [voice 11788]
    voice "ch18_s_103"
    s "O-Okay.{#ch18_s_103}"

    # [SE       se0      play=+67]
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SE       se0      play=+66]
    # [EVENT_CG event    image=+130, level=80]
    $ dissolve_fx("id(130)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # サイト：（俺達はタバサのシルフィードに乗って、
    s "(We rode Tabitha's Sylphid to the academy. What on earth happened…?){#ch18_s_104}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # → next scene 701
    jump ch18_1_scene_701

label ch18_1_scene_701:

    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1147, level=200]
    $ fade_fx("id(1147)")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1138, level=200]
    $ fade_fx("id(1138)")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1147, level=200]
    $ fade_fx("id(1147)")
    # [TRANS trans("crossfade", 750)]
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # ルイズ：これは、どういうこと？  [voice 6340]
    voice "ch18_l_079"
    l "What is the meaning of this?{#ch18_l_079}"

    # [SPRITE   lay5     level=156]
    # [SPRITE   lay19    image=+944, level=149, dir=1A]
    # [SPRITE   lay1     level=155]
    # デルフリンガー：おい相棒、こりゃあ……。  [voice 1308]
    voice "ch18_d_007"
    d "Hey, partner, this is…{#ch18_d_007}"

    # [SPRITE   lay5     level=149]
    # [SPRITE   lay19    level=150]
    # [SPRITE   lay1     level=156]
    # サイト：まるで戦争があったみたいだな。
    voice "ch18_s_105"
    s "It's like a war zone. Are you sure Haruna is the cause…?{#ch18_s_105}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=155, dir=1A]
    # タバサ：急いで……。  [voice 15589]
    voice "ch18_t_008"
    t "Hurry…{#ch18_t_008}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay3     image=+856, level=152, dir=1A]
    # モンモランシー：サイト、ルイズっ！
    voice "ch18_m_005"
    m "Saito, Louise! Thank goodness, you finally came.{#ch18_m_005}"

    # [SPRITE   lay3     x=-96, y=0]
    # [SPRITE   lay5     image=+394, level=149, dir=1A]
    # サイト：モンモン！
    voice "ch18_s_106"
    s "Montmon! What's happening? Tell me the situation.{#ch18_s_106}"

    # [SPRITE   lay3     image=+858, level=152, dir=1A]
    # モンモランシー：状況もなにも……朝食を食べてたらいきなり
    voice "ch18_m_006"
    m "The situation, I… We were eating breakfast when screams and explosions came from the plaza. Guiche and I went to see…{#ch18_m_006}"

    # モンモランシー：ハルナが、爆弾をつかってあちこちを
    voice "ch18_m_007"
    m "Haruna was setting off bombs all over the place.{#ch18_m_007}"

    # モンモランシー：もちろん、ギーシュがゴーレムを召喚して、
    voice "ch18_m_008"
    m "Of course Guiche summoned a golem and attacked, but…{#ch18_m_008}"

    # [SPRITE   lay5     image=+427, level=149, dir=2A]
    # サイト：あっけなく返り討ち、ってわけか。  [voice 11791]
    voice "ch18_s_107"
    s "Routed in no time, I suppose.{#ch18_s_107}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=156, dir=1A]
    # ルイズ：でも、学院には先生達だっているでしょう？
    voice "ch18_l_080"
    l "But there are teachers at the academy, aren't there? One girl couldn't…{#ch18_l_080}"

    # [SPRITE   lay3     image=+856, level=152, dir=1A]
    # モンモランシー：それができないから困ってるんだってば！
    voice "ch18_m_009"
    m "That's just it—they can't! Come here, quickly.{#ch18_m_009}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay21    image=+1019, level=151, dir=1A]
    # [SPRITE   lay6     image=+682, level=154, dir=1A]
    # ハルナ：あはははっ！
    voice "ch18_ha_001"
    ha "Ahahaha! What's wrong, Kirche? Is that your great fire magic?{#ch18_ha_001}"

    # キュルケ：くっ、速度がおいつかない！  [voice 3299]
    voice "ch18_k_008"
    k "Tch! She's too fast!{#ch18_k_008}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     image=+394, level=149, dir=1A]
    # サイト：キュルケ！  [voice 11792]
    voice "ch18_s_108"
    s "Kirche!{#ch18_s_108}"

    # [SPRITE   lay6     image=+676, level=154, dir=1A]
    # キュルケ：ダーリン……。
    voice "ch18_k_009"
    k "Darling… You finally came.{#ch18_k_009}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay21    image=+1017, level=151, dir=1A]
    # ハルナ：はん、やっとお出ましか……。
    voice "ch18_ha_002"
    ha "Hn, so you've come at last… The legendary Gandálfr.{#ch18_ha_002}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     image=+339, level=156, dir=2A]
    # ルイズ：キュルケ！
    voice "ch18_l_081"
    l "Kirche! Why are you struggling against a mere commoner!?{#ch18_l_081}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay6     image=+713, level=154, dir=2A]
    # キュルケ：呪文よりも爆破のほうが早いのよ。
    voice "ch18_k_010"
    k "Explosions are faster than spells. I've never seen anything like it!{#ch18_k_010}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+396, level=149, dir=1A]
    # サイト：春奈……。
    voice "ch18_s_109"
    s "Haruna… Why are you doing this!{#ch18_s_109}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay21    image=+1021, level=151, dir=1A]
    # ハルナ：その名前で呼ぶな！  [voice 2384]
    voice "ch18_ha_003"
    ha "Don't call me by that name!{#ch18_ha_003}"

    # サイト：え？  [voice 11794]
    voice "ch18_s_110"
    s "Eh?{#ch18_s_110}"

    # [SPRITE   lay21    image=+1017, level=151, dir=1A]
    # アキナ：あたしはハルナなんて名前じゃない。
    voice "ch18_ak_001"
    ak "I'm not Haruna. My name is… Akina.{#ch18_ak_001}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+339, level=156, dir=2A]
    # ルイズ：アキナ？
    voice "ch18_l_082"
    l "Akina? But… you look exactly like Haruna in every way!{#ch18_l_082}"

    # [SPRITE   lay21    level=151]
    # [SPRITE   lay19    image=+944, level=149, dir=1A]
    # [SPRITE   lay1     level=156]
    # デルフリンガー：相棒、気をつけろ。
    voice "ch18_d_008"
    d "Partner, careful. It looks like magic is at work.{#ch18_d_008}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     image=+394, level=150, dir=1A]
    # サイト：なに！  [voice 11795]
    voice "ch18_s_111"
    s "What!{#ch18_s_111}"

    # [SPRITE   lay21    image=+1019, level=151, dir=1A]
    # アキナ：へぇ、さすがは伝説の剣だね。
    voice "ch18_ak_002"
    ak "Heh, as expected of the legendary sword. This body is indeed Haruna's. But the one inside, moving it, is different.{#ch18_ak_002}"

    # [SPRITE   lay5     image=+427, level=150, dir=2A]
    # サイト：まさか……二重人格？  [voice 11796]
    voice "ch18_s_112"
    s "You don't mean… a split personality?{#ch18_s_112}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     image=+308, level=156, dir=1A]
    # ルイズ：なによ、それ？  [voice 6344]
    voice "ch18_l_083"
    l "What's that?{#ch18_l_083}"

    # [SPRITE   lay5     image=+394, level=150, dir=1A]
    # サイト：簡単に言うと、１人の中に２人がいるってこと。  [voice 11797]
    voice "ch18_s_113"
    s "Simply put, there are two people in one body.{#ch18_s_113}"

    # [SPRITE   lay1     image=+306, level=156, dir=1A]
    # ルイズ：なんてことを！
    voice "ch18_l_084"
    l "How could you! You used forbidden magic to control someone's heart!{#ch18_l_084}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay21    image=+1019, level=151, dir=1A]
    # アキナ：さすがに理解が早いねぇ。  [voice 63]
    voice "ch18_ak_003"
    ak "You're quick to understand, aren't you.{#ch18_ak_003}"

    # サイト：春奈はどうなったんだ！？  [voice 11798]
    voice "ch18_s_114"
    s "What happened to Haruna!?{#ch18_s_114}"

    # [SPRITE   lay21    image=+1017, level=151, dir=1A]
    # アキナ：ハルナのことが心配かい？
    voice "ch18_ak_004"
    ak "Worried about Haruna? Don't be. Haruna is alive.{#ch18_ak_004}"

    # アキナ：あたしが眠ってる間は、ハルナは、
    voice "ch18_ak_005"
    ak "While I'm asleep, Haruna stays Haruna.{#ch18_ak_005}"

    # アキナ：逆にハルナが眠っている間は、
    voice "ch18_ak_006"
    ak "And while Haruna sleeps, I move this body. That's the arrangement.{#ch18_ak_006}"

    # [SPRITE   lay21    image=+1019, level=151, dir=1A]
    # アキナ：まったくこっけいな話だよね。  [voice 67]
    voice "ch18_ak_007"
    ak "Quite ridiculous, isn't it.{#ch18_ak_007}"

    # アキナ：ハルナは自分が眠っている間に
    voice "ch18_ak_008"
    ak "Haruna has no idea what terrible things she does while she's asleep…{#ch18_ak_008}"

    # [SPRITE   lay5     image=+396, level=150, dir=1A]
    # サイト：……。  [voice 11799]
    voice "ch18_s_115"
    s "…{#ch18_s_115}"

    # [SPRITE   lay21    image=+1017, level=151, dir=1A]
    # アキナ：ハルナは、もうずいぶん前に
    voice "ch18_ak_009"
    ak "Haruna came to Halkeginia quite some time ago.{#ch18_ak_009}"

    # アキナ：そして、ハルナを保護したあのお方は、
    voice "ch18_ak_010"
    ak "And the one who took her in asked about her circumstances, where she came from— and decided she could be useful.{#ch18_ak_010}"

    # アキナ：トリステインにいるっていう伝説の使い魔、
    voice "ch18_ak_011"
    ak "To investigate Saito, the legendary familiar of Tristain, and his mistress Louise. {#ch18_ak_011}"

    # [SPRITE   lay5     image=+394, level=150, dir=1A]
    # サイト：お、俺とルイズのことを？  [voice 11800]
    voice "ch18_s_116"
    s "O-Us!?{#ch18_s_116}"

    # [SPRITE   lay21    image=+1019, level=151, dir=1A]
    # アキナ：ああ、そうさ。
    voice "ch18_ak_012"
    ak "Yeah. I've been watching you all this time.{#ch18_ak_012}"

    # アキナ：情報は逐一あたしのご主人様に送らせて
    voice "ch18_ak_013"
    ak "I had every piece of information sent to my mistress.{#ch18_ak_013}"

    # [SPRITE   lay21    image=+1017, level=151, dir=1A]
    # アキナ：あたしのもうひとつの役目である、
    voice "ch18_ak_014"
    ak "On the side, while I was busy with my other job—sabotage…{#ch18_ak_014}"

    # アキナ：なんともチョロい任務だったけどな。  [voice 75]
    voice "ch18_ak_015"
    ak "It was a rather easy assignment, though.{#ch18_ak_015}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+713, level=154, dir=2A]
    # キュルケ：破壊活動、って……。
    voice "ch18_k_011"
    k "Sabotage… So the bombings everywhere were…{#ch18_k_011}"

    # [SPRITE   lay21    image=+1019, level=151, dir=1A]
    # アキナ：お察しのとおり。
    voice "ch18_ak_016"
    ak "Just as you guessed. My doing.{#ch18_ak_016}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+394, level=150, dir=1A]
    # サイト：お前の親玉は誰なんだ！  [voice 11801]
    voice "ch18_s_117"
    s "Who's your mastermind!?{#ch18_s_117}"

    # [SPRITE   lay21    image=+1017, level=151, dir=1A]
    # アキナ：さぁてねぇ……。
    voice "ch18_ak_017"
    ak "Well now… You'll find out soon enough, won't you?{#ch18_ak_017}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     image=+339, level=156, dir=2A]
    # ルイズ：サイト、あの娘を捕まえるわよ！  [voice 6346]
    voice "ch18_l_085"
    l "Saito, we'll capture her!{#ch18_l_085}"

    # [SPRITE   lay5     image=+427, level=150, dir=2A]
    # サイト：そ、そうは言っても、春奈を攻撃するのかよ！  [voice 11802]
    voice "ch18_s_118"
    s "B-But that means attacking Haruna!{#ch18_s_118}"

    # ルイズ：学院みんなの命がかかってるのよ。
    voice "ch18_l_086"
    l "Everyone's lives are at stake. Get a grip!{#ch18_l_086}"

    menu:
        "If it comes to this, I'll do it!{#ch18_1_c_701_1}":
            jump ch18_1_scene_702
        "Think{#ch18_1_c_701_2}":
            jump ch18_1_scene_703
        "Refuse!{#ch18_1_c_701_3}":
            jump ch18_1_scene_704

label ch18_1_scene_702:

    # [SPRITE   lay5     image=+427, level=150, dir=2A]
    # [SPRITE   lay1     image=+339, level=156, dir=2A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [SPRITE   lay5     image=+394, level=150, dir=1A]
    # サイト：こうなりゃやってやる！
    voice "ch18_s_119"
    s "If it comes to this, I'll do it! Let's go, Louise.{#ch18_s_119}"

    # [SPRITE   lay1     image=+306, level=156, dir=1A]
    # ルイズ：分かってるわよ！  [voice 6348]
    voice "ch18_l_087"
    l "I know!{#ch18_l_087}"

    # [SPRITE   lay5     level=150]
    # [SPRITE   lay1     level=156]
    # [SPRITE   lay19    image=+940, level=149, dir=1A]
    # デルフリンガー：２人とも待て！
    voice "ch18_d_009"
    d "Both of you, wait! I can't agree to charging in without knowing how she'll act.{#ch18_d_009}"

    # [SPRITE   lay5     image=+429, level=149, dir=2A]
    # [SPRITE   lay5     level=149]
    # [SPRITE   lay1     level=156]
    # [SPRITE   lay19    level=150]
    # サイト：くっ。
    voice "ch18_s_120"
    s "Tch. Then what should we do?{#ch18_s_120}"

    # → next scene 705
    jump ch18_1_scene_705

label ch18_1_scene_703:

    # [SPRITE   lay5     image=+427, level=150, dir=2A]
    # [SPRITE   lay1     image=+339, level=156, dir=2A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [SPRITE   lay5     image=+396, level=150, dir=1A]
    # サイト：ど、どうすればいいんだ！  [voice 11805]
    voice "ch18_s_121"
    s "W-What should we do!{#ch18_s_121}"

    # [SPRITE   lay1     image=+306, level=156, dir=1A]
    # ルイズ：なに突っ立ってんのよ！
    voice "ch18_l_088"
    l "Why are you standing there! Let's go!{#ch18_l_088}"

    # [SPRITE   lay5     level=150]
    # [SPRITE   lay1     level=156]
    # [SPRITE   lay19    image=+940, level=149, dir=1A]
    # デルフリンガー：２人とも待て！
    voice "ch18_d_010"
    d "Both of you, wait! I can't agree to charging in without knowing how she'll act.{#ch18_d_010}"

    # [SPRITE   lay5     level=151]
    # [SPRITE   lay1     level=149]
    # [SPRITE   lay19    level=150]
    # ルイズ：そんな……。
    voice "ch18_l_089"
    l "That's… Then what do we do?{#ch18_l_089}"

    # → next scene 705
    jump ch18_1_scene_705

label ch18_1_scene_704:

    # [SPRITE   lay5     image=+427, level=150, dir=2A]
    # [SPRITE   lay1     image=+339, level=156, dir=2A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [SPRITE   lay5     image=+394, level=150, dir=1A]
    # サイト：断る。
    voice "ch18_s_122"
    s "I refuse. She may be Akina now, but she's still Haruna.{#ch18_s_122}"

    # [SPRITE   lay5     image=+396, level=150, dir=1A]
    # サイト：それに、本物の春奈の人格は
    voice "ch18_s_123"
    s "And the real Haruna's personality isn't gone. She's just being controlled by Akina.{#ch18_s_123}"

    # [SPRITE   lay1     image=+308, level=156, dir=1A]
    # ルイズ：む～～っ！  [voice 6351]
    voice "ch18_l_090"
    l "Grr…{#ch18_l_090}"

    # → next scene 705
    jump ch18_1_scene_705

label ch18_1_scene_705:

    # [SPRITE   lay1     image=+306, level=156, dir=1A]
    # [SPRITE   lay19    image=+940, level=150, dir=1A]
    # [SPRITE   lay5     image=+429, level=149, dir=2A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [SPRITE   lay19    image=+944, level=149, dir=1A]
    # [SPRITE   lay1     level=156]
    # [SPRITE   lay19    level=149]
    # [SPRITE   lay5     level=150]
    # デルフリンガー：もう少し様子を見ろ。
    voice "ch18_d_011"
    d "Watch a little longer. She might leave an opening.{#ch18_d_011}"

    # [SPRITE   lay5     image=+427, level=149, dir=2A]
    # [SPRITE   lay1     level=156]
    # [SPRITE   lay19    level=150]
    # [SPRITE   lay5     level=149]
    # サイト：……くそっ！  [voice 11808]
    voice "ch18_s_124"
    s "…Damn!{#ch18_s_124}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    image=+1019, level=151, dir=1A]
    # アキナ：あんたらがなんで、この学院に舞い戻って
    voice "ch18_ak_018"
    ak "I know why you've come back to this academy. To use that Zero Fighter… right?{#ch18_ak_018}"

    # アキナ：そうはさせないわ。
    voice "ch18_ak_019"
    ak "I won't let you. Reconquista's victory is assured, but I can't leave loose ends.{#ch18_ak_019}"

    # [SPRITE   lay21    image=+1021, level=151, dir=1A]
    # アキナ：あんたらにもここを動かないでいてもらうよ。
    voice "ch18_ak_020"
    ak "I'll keep you from leaving this place. If you don't listen…{#ch18_ak_020}"

    # [SPRITE   lay21    hide]
    # [SE       se0      play=+63]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay21    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay19    vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay21    hide, reset]
    # [SPRITE   lay3     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay1     image=+308, level=156, dir=1A]
    # ルイズ：きゃっ！  [voice 6352]
    voice "ch18_l_091"
    l "Eek!{#ch18_l_091}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay21    image=+1019, level=151, dir=1A]
    # アキナ：学院中に爆弾を仕掛けさせてもらったの。
    voice "ch18_ak_021"
    ak "I've had bombs planted all over the academy. They can be detonated anytime on my signal.{#ch18_ak_021}"

    # アキナ：あんたがどこへも行かないように、
    voice "ch18_ak_022"
    ak "So you won't leave, I'll watch from the highest place.{#ch18_ak_022}"

    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay5     image=+394, level=149, dir=1A]
    # サイト：くっ……。  [voice 11809]
    voice "ch18_s_125"
    s "Tch…{#ch18_s_125}"

    # [SPRITE   lay21    image=+1017, level=151, dir=1A]
    # アキナ：ほら、サイト！
    voice "ch18_ak_023"
    ak "See, Saito! Stand aside! Do you want me to blow this place up right now?{#ch18_ak_023}"

    # [SPRITE   lay5     image=+396, level=149, dir=1A]
    # サイト：分かった……。  [voice 11810]
    voice "ch18_s_126"
    s "Fine…{#ch18_s_126}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+308, level=156, dir=1A]
    # [SPRITE   lay5     image=+396, level=149, dir=1A]
    # [SPRITE   lay1     level=156]
    # [SPRITE   lay19    image=+946, level=149, dir=1A]
    # [SPRITE   lay5     level=150]
    # デルフリンガー：困ったことになったな、相棒。
    voice "ch18_d_012"
    d "This is a fine mess, partner. Who'd have thought that girl was a spy.{#ch18_d_012}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     image=+394, level=150, dir=1A]
    # サイト：春奈はスパイなんかじゃない。
    voice "ch18_s_127"
    s "Haruna isn't a spy. It's Akina—it's magic controlling her!{#ch18_s_127}"

    # [SPRITE   lay1     image=+306, level=156, dir=1A]
    # ルイズ：なによなによなんなのよ！
    voice "ch18_l_092"
    l "What, what, what! We have no time to waste here, Louise and I—{#ch18_l_092}"

    # ルイズ：こんなとこで、無駄な時間をすごす
    voice "ch18_l_093"
    l "—no time to waste in a place like this!!{#ch18_l_093}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 706
    jump ch18_2

    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch18_2
    return

