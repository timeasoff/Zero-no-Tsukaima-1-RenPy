# Глава 13, часть 3 (сцены 568–577): огонь Кирке, подозрение на Уэзерби.
# Источник: ps2_source/chapters/chapter_14_炎の予感.txt (SCENE 568-577).

label ch13_3:
    $ tndl(None)
    $ show_sprites()

    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # → next scene 1469
    jump ch14

    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # → next scene 1470
    jump ch14

    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # → next scene 1475
    jump ch14

    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+43, hide, level=10]
    $ fade_fx("id(43)")
    # → next scene 1480
    jump ch14

label ch13_3_scene_568:

    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：（小さな情報はいくつかあったけど、
    s "(I found a few small leads, but nothing really important…){#ch13_s_100}"

    # サイト：（こりゃ、ダメかもしれないな。
    s "(This might not work out. Could I even do a handstand…?){#ch13_s_101}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：もう、ダーリンったら、そんな渋い顔しない。  [voice 3656]
    voice "ch13_k_089"
    k "Really, darling, don't make such a sour face.{#ch13_k_089}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：そんな弱気な顔をするなんて、
    voice "ch13_k_090"
    k "Looking so timid doesn't suit my darling.{#ch13_k_090}"

    menu:
        "Easy for you to say…{#ch13_3_c_568_1}":
            jump ch13_3_scene_569
        "All right, I'll give it a shot!{#ch13_3_c_568_2}":
            jump ch13_3_scene_570
        "What about you, Kirche?{#ch13_3_c_568_3}":
            jump ch13_3_scene_571

label ch13_3_scene_569:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：そ、そんなこといわれても……。  [voice 12881]
    voice "ch13_s_102"
    s "E-Easy for you to say…{#ch13_s_102}"

    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：もうっ！  [voice 3658]
    voice "ch13_k_091"
    k "Ugh!{#ch13_k_091}"

    # キュルケ：こんなときはウソでもできるって胸を張るの。  [voice 3659]
    voice "ch13_k_092"
    k "In times like this, you puff out your chest and say you can do it—even if you have to lie.{#ch13_k_092}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：それが前に進むための魔法よ。
    voice "ch13_k_093"
    k "That's the magic that moves you forward. Even fake cheer is still cheer.{#ch13_k_093}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：そうだな。  [voice 12882]
    voice "ch13_s_103"
    s "I guess so.{#ch13_s_103}"

    # → next scene 572
    jump ch13_3_scene_572

label ch13_3_scene_570:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay5     image=+403, level=160, dir=1B]
    # サイト：よしっ、頑張ってみるか！  [voice 12883]
    voice "ch13_s_104"
    s "All right, I'll give it a shot!{#ch13_s_104}"

    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：それでこそ、あたしのダーリン！
    voice "ch13_k_094"
    k "That's my darling! I might just fall for you all over again.{#ch13_k_094}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：勘弁してください。  [voice 12884]
    voice "ch13_s_105"
    s "Please spare me.{#ch13_s_105}"

    # → next scene 572
    jump ch13_3_scene_572

label ch13_3_scene_571:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：キュルケはどうなんだよ。
    voice "ch13_s_106"
    s "What about you, Kirche? Aren't you worried?{#ch13_s_106}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：不安になんてならないわ。
    voice "ch13_k_095"
    k "Not at all. Because my darling is with me.{#ch13_k_095}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：いや、まったく関係ないだろ。  [voice 12886]
    voice "ch13_s_107"
    s "That has nothing to do with it.{#ch13_s_107}"

    # キュルケ：そうでもないわよ。
    voice "ch13_k_096"
    k "Oh, but it does. If you keep thinking about something, it becomes real. If you don't, nothing happens.{#ch13_k_096}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：？？？  [voice 12887]
    voice "ch13_s_108"
    s "???{#ch13_s_108}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：それは恋も課題も一緒よ。
    voice "ch13_k_097"
    k "It's the same for love and for a task. That's why I'm with my darling.{#ch13_k_097}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：良く分からないけど、俺が諦めなければ
    voice "ch13_s_109"
    s "I don't quite get it, but… as long as I don't give up, things will work out?{#ch13_s_109}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：まぁ、そういうことよ。  [voice 3665]
    voice "ch13_k_098"
    k "Well, something like that.{#ch13_k_098}"

    # → next scene 572
    jump ch13_3_scene_572

label ch13_3_scene_572:

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：……。  [voice 12889]
    voice "ch13_s_110"
    s "…{#ch13_s_110}"

    # サイト：でも、キュルケ。
    voice "ch13_s_111"
    s "But, Kirche. Why are you so serious about this case?{#ch13_s_111}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：真剣？  [voice 3666]
    voice "ch13_k_099"
    k "Serious?{#ch13_k_099}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：なんつーか、その……。
    voice "ch13_s_112"
    s "I mean… you're not acting like your usual self.{#ch13_s_112}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：あたしね、あの爆弾使いが嫌いなの……。  [voice 3667]
    voice "ch13_k_100"
    k "You see, I hate that bomb-thrower.{#ch13_k_100}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：へっ？  [voice 12892]
    voice "ch13_s_113"
    s "Huh?{#ch13_s_113}"

    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：火というものを、単純な破壊の道具としか
    voice "ch13_k_101"
    k "They see fire only as a tool for destruction. I hate the way they do things.{#ch13_k_101}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：『火』の属性の魔法使いとして……。
    voice "ch13_k_102"
    k "As a mage of the 'fire' attribute… by the name of Kirche with a slight fever…{#ch13_k_102}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：『本当の火の使い方』というものを
    voice "ch13_k_103"
    k "…I have to teach them the 'true way to use fire'.{#ch13_k_103}"

    # サイト：（……『本当の火の使い方』？）
    s "(…'The true way to use fire'?){#ch13_s_114}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：なあ、キュルケ。
    voice "ch13_s_115"
    s "Say, Kirche. What's this 'true way to use fire'?{#ch13_s_115}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：うーん。
    voice "ch13_k_104"
    k "Mm. Hard to put into words. Once this is over, I'll tell you all about it.{#ch13_k_104}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：さぁ、ダーリン行くわよ。  [voice 3672]
    voice "ch13_k_105"
    k "Now, darling, let's go.{#ch13_k_105}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：へいへい。  [voice 12894]
    voice "ch13_s_116"
    s "Yeah, yeah.{#ch13_s_116}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 573
    jump ch13_3_scene_573

label ch13_3_scene_573:

    # [BG       stage    image=+52, level=200]
    $ fade_fx("id(52)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：劇場の前まで来てしまったみたいね。  [voice 3673]
    voice "ch13_k_106"
    k "Looks like we've made it to the theater.{#ch13_k_106}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：劇場か……。
    voice "ch13_s_117"
    s "The theater, huh… It's quiet once the performances end.{#ch13_s_117}"

    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：……！！  [voice 3674]
    voice "ch13_k_107"
    k "…!!{#ch13_k_107}"

    # サイト：どうしたんだ？
    voice "ch13_s_118"
    s "What's wrong, Kirche?{#ch13_s_118}"

    # [SPRITE   lay6     image=+713, level=160, dir=2A]
    # キュルケ：シィッ！
    voice "ch13_k_108"
    k "Shh! Quiet, darling…{#ch13_k_108}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：……。
    w "…{#ch13_w_001}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：あれは……ウェザリーさん？
    voice "ch13_s_119"
    s "Is that… Weatherly-san? Preparing for the next play, maybe?{#ch13_s_119}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：やっぱりね。  [voice 3676]
    voice "ch13_k_109"
    k "Just as I thought.{#ch13_k_109}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：やっぱりって。
    voice "ch13_s_120"
    s "Just as you thought? Did something happen to Weatherly-san?{#ch13_s_120}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：ダーリン……。
    voice "ch13_k_110"
    k "Darling… What we were looking for tonight wasn't the bomb-thrower.{#ch13_k_110}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：え、なんだって？
    voice "ch13_s_121"
    s "Huh? Then who were we looking for?{#ch13_s_121}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あたしが探していたのは、ウェザリーの行方。  [voice 3678]
    voice "ch13_k_111"
    k "I was looking for Weatherly.{#ch13_k_111}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：ウェザリーさんの行方……？  [voice 12900]
    voice "ch13_s_122"
    s "Weatherly-san's whereabouts…?{#ch13_s_122}"

    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：あ、裏路地に行くわ！
    voice "ch13_k_112"
    k "Ah, she's heading into the back alley! Darling, let's follow!{#ch13_k_112}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：（何が、なんだかさっぱりだが、
    s "(I have no idea what's going on, but for now, follow Kirche…){#ch13_s_123}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # null：………。 (no voice)
    # [BG       stage    hide]
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：いない……。
    voice "ch13_s_124"
    s "She's gone… But why Weatherly-san?{#ch13_s_124}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：まだ確信は無いんだけど、
    voice "ch13_k_113"
    k "I'm not sure yet, but Weatherly's been acting very suspicious. Maybe… a spy.{#ch13_k_113}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ええっ、なんだって？  [voice 12902]
    voice "ch13_s_125"
    s "Huh!? What was that?{#ch13_s_125}"

    menu:
        "That can't be!{#ch13_3_c_573_1}":
            jump ch13_3_scene_574
        "Now that you mention it…{#ch13_3_c_573_2}":
            jump ch13_3_scene_575
        "A spy of what?{#ch13_3_c_573_3}":
            jump ch13_3_scene_576

label ch13_3_scene_574:

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：そんなはずはないって！
    voice "ch13_s_126"
    s "That can't be! Weatherly-san a spy…!{#ch13_s_126}"

    # キュルケ：信じられない？
    voice "ch13_k_114"
    k "Can't believe it? Or don't want to?{#ch13_k_114}"

    # → next scene 577
    jump ch13_3_scene_577

label ch13_3_scene_575:

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：言われてみれば。  [voice 12904]
    voice "ch13_s_127"
    s "Now that you mention it…{#ch13_s_127}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：ええ、どうして最初から気づかなかった
    voice "ch13_k_115"
    k "Yes, why didn't I notice sooner.{#ch13_k_115}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あまりにも近くにいたから、
    voice "ch13_k_116"
    k "They were so close, I never thought to suspect them.{#ch13_k_116}"

    # → next scene 577
    jump ch13_3_scene_577

label ch13_3_scene_576:

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：スパイって何の？  [voice 12905]
    voice "ch13_s_128"
    s "A spy of what?{#ch13_s_128}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：確信はないけど、爆弾使いの件に
    voice "ch13_k_117"
    k "I'm not sure, but they may be deeply involved in the bomb-thrower case.{#ch13_k_117}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：爆弾使いのスパイ？  [voice 12906]
    voice "ch13_s_129"
    s "A bomb-thrower's spy?{#ch13_s_129}"

    # キュルケ：さぁ、それはどうかしら？  [voice 3685]
    voice "ch13_k_118"
    k "Well, who knows?{#ch13_k_118}"

    # → next scene 577
    jump ch13_3_scene_577

label ch13_3_scene_577:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：身元の不確かな旅回りの一座……。
    voice "ch13_k_119"
    k "A traveling troupe with unclear origins… And they can't even find a lead for an important play.{#ch13_k_119}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：主役がいないのは、それに合う人が
    voice "ch13_s_130"
    s "Didn't Weatherly-san say there was no one suitable for the lead?{#ch13_s_130}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：そうね。
    voice "ch13_k_120"
    k "Right. So we went on stage. But what if that was a cover?{#ch13_k_120}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：ま、まさか？
    voice "ch13_s_131"
    s "N-No way! They couldn't have predicted we'd come.{#ch13_s_131}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：確かにそう。
    voice "ch13_k_121"
    k "True. It's still just guesswork.{#ch13_k_121}"

    # キュルケ：でも、他にも調べてみたら胡散臭い話が
    voice "ch13_k_122"
    k "But I dug around and found one suspicious thing after another.{#ch13_k_122}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：どれほどのネズミかは分からないけど、
    voice "ch13_k_123"
    k "I don't know how deep this rat goes, but Weatherly is definitely up to something…{#ch13_k_123}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：しかし、良く気がついたな。
    voice "ch13_s_132"
    s "Still, you noticed. We didn't at all.{#ch13_s_132}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：この街にはね……。
    voice "ch13_k_124"
    k "In this town… I can sense fire.{#ch13_k_124}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ЯДРА ГЛАВЫ 13 ====
    jump ch13_4
    return

