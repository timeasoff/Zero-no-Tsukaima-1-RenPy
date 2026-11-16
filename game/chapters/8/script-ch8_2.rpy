# script-ch8_2.rpy — Глава 8, часть 2: сцены 417–423
# Порт из ps2_source/chapters/chapter_09_決意のお姫さま.txt
# Граница части: 417–423, след. часть: ch8_3 (сцены 424–427)

label ch8_2:
    # ==== SCENE 417 ====
    # [SPRITE lay8 image=+787 level=140 dir=1C → id(787)]
    $ show_sprites(("id(787)"))
    # [BGM bgm play=+16 → t16]
    play music t16 fadein 1.0
    # [BG stage image=+42 level=200 → id(42)]
    $ fade_fx("id(42)")
    # [BGM bgm stop=1000]
    stop music fadeout 1.0
    # [SE se0 play=+59]
    $ se_fx("se59")
    # [SPRITE lay8 hide] [SPRITE lay5 hide] [BG stage hide]
    $ show_sprites()
    $ fade_fx(None)
    # [EVENT_CG event image=+267 level=80]
    $ dissolve_fx("id(267)", type="cg")
    # [TRANS trans("crossfade", 1000)]
    # [BGM bgm play=+22 → t22]
    play music t22 fadein 1.0
    # アンリエッタ：ちゅっ。  [voice 892]
    voice "ch8_h_041"
    h "Mwah. {#ch8_h_041}"
    # JA[892]: ちゅっ。
    # サイト：えっ？  [voice 13617]
    voice "ch8_s_058"
    s "Eh? {#ch8_s_058}"
    # JA[13617]: えっ？
    # アンリエッタ：うふふ、隙あり、ですよサイトさん。そんな風では騎士失格です。  [voice 893]
    voice "ch8_h_042"
    h "Hehe, you have an opening, Saito-san. That's not knight-like. {#ch8_h_042}"
    # JA[893]: うふふ、隙あり、ですよサイトさん。そんな風では騎士失格です。
    # サイト：（今、詰め寄られたかと思ったら、暖かくて柔らかい感触が……。お姫さまの唇が……っ！？）
    # [no voice — thought]
    s (Now, just when I thought she was pressing in on me, a warm soft sensation… Her lips…!?)
    # JA: （今、詰め寄られたかと思ったら、暖かくて柔らかい感触が……。お姫さまの唇が……っ！？）
    # [SPRITE lay8 hide] [SPRITE lay5 hide] [BG stage hide] [EVENT_CG event hide]
    $ show_sprites()
    $ fade_fx(None)
    # [BG stage image=+42 level=200 → id(42)]
    $ fade_fx("id(42)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE lay5 image=+427 level=160 dir=2A → s 3]
    $ show_sprites(("s 3",))
    # [SPRITE lay8 image=+794 level=160 dir=1C → h 2 shy]
    $ show_sprites(("s 3", "h 2 shy"))
    # サイト：え……ええっ、えええー！？  [voice 13618]
    voice "ch8_s_059"
    s "Eh… Eh, eeh!? {#ch8_s_059}"
    # JA[13618]: え……ええっ、えええー！？
    # アンリエッタ：……。  [voice 894]
    voice "ch8_h_043"
    h "… {#ch8_h_043}"
    # JA[894]: ……。
    # → next scene 419

    # ==== SCENE 418 ==== (transition, no dialogue)
    # [SPRITE lay8 image=+787 level=140 dir=1C → id(787)]
    $ show_sprites(("id(787)"))
    # [BGM bgm play=+16 → t16]
    play music t16 fadein 1.0
    # [BG stage image=+42 level=200 → id(42)]
    $ fade_fx("id(42)")
    # [SPRITE lay8 hide]
    $ show_sprites()
    # [SPRITE lay8 image=+786 level=160 dir=1C → h 2]
    $ show_sprites(("h 2",))
    # [SPRITE lay5 image=+427 level=160 dir=2A → s 3]
    $ show_sprites(("s 3", "h 2"))
    # [SPRITE lay8 image=+786 level=160 dir=1C → h 2]
    $ show_sprites(("s 3", "h 2"))
    # → next scene 419

    # ==== SCENE 419 ====
    # [SPRITE lay8 image=+794 level=160 dir=1C → h 2 shy]
    $ show_sprites(("s 3", "h 2 shy"))
    # [SPRITE lay5 image=+427 level=160 dir=2A → s 3]
    # [BGM bgm play=+22 → t22]
    play music t22 fadein 1.0
    # [BG stage image=+42 level=200 → id(42)]
    $ fade_fx("id(42)")
    # ルイズ：サ～イ～ト～！！  [voice 7421]
    voice "ch8_l_015"
    l "Saaai～to～!! {#ch8_l_015}"
    # JA[7421]: サ～イ～ト～！！
    # [SPRITE lay8 hide]
    $ show_sprites(("s 3",))
    # [SPRITE lay5 image=+394 level=160 dir=1A → s 1]
    $ show_sprites(("s 1",))
    # サイト：なんだよ、今それどころじゃないよ。  [voice 13619]
    voice "ch8_s_060"
    s "What? Now's not the time for that. {#ch8_s_060}"
    # JA[13619]: なんだよ、今それどころじゃないよ。
    # [SPRITE lay5 image=+429 level=160 dir=2A → s 3 sad]
    $ show_sprites(("s 3 sad",))
    # サイト：……え？今の声は、あれ？  [voice 13620]
    voice "ch8_s_061"
    s "…Eh? That voice just now…? {#ch8_s_061}"
    # JA[13620]: ……え？今の声は、あれ？
    # [BGM bgm stop=1000]
    stop music fadeout 1.0
    # [SPRITE lay5 image=+396 level=160 dir=1A → s 1 sad]
    $ show_sprites(("s 1 sad",))
    # サイト：はッ！？背後にものすごい殺気が！  [voice 13621]
    voice "ch8_s_062"
    s "Hah!? There's a killing intent behind me! {#ch8_s_062}"
    # JA[13621]: はッ！？背後にものすごい殺気が！
    # [SPRITE lay1 hide] [SPRITE lay5 hide] [BG stage hide]
    $ show_sprites()
    $ fade_fx(None)
    # [EVENT_CG event image=+213 level=80]
    $ dissolve_fx("id(213)", type="cg")
    # [TRANS trans("crossfade", 1000)]
    # [BGM bgm play=+30 → t30]
    play music t30 fadein 1.0
    # ルイズ：あんたってバカは、いくら言ってきかせても見境なしにふらふらと……！  [voice 7422]
    voice "ch8_l_016"
    l "You idiot, no matter how much I tell you, you keep wandering without limit…! {#ch8_l_016}"
    # JA[7422]: あんたってバカは、いくら言ってきかせても見境なしにふらふらと……！
    # サイト：る、ルイズっ！？ま、待て！ちちがうんだ、これは！  [voice 13622]
    voice "ch8_s_063"
    s "L-Louise!? W-Wait! That's not it, this is! {#ch8_s_063}"
    # JA[13622]: る、ルイズっ！？ま、待て！ちちがうんだ、これは！
    # ルイズ：この……バカ使い魔ぁーっ！！  [voice 7423]
    voice "ch8_l_017"
    l "You… stupid familiar～!! {#ch8_l_017}"
    # JA[7423]: この……バカ使い魔ぁーっ！！
    # [SE se0 play=+95]
    $ se_fx("se95")
    # [BG stage vibrate=14]
    # [EVENT_CG event vibrate=14]
    # [SPRITE lay1 hide, vibrate=14]
    # [SPRITE lay8 vibrate=14]
    # [SPRITE lay5 hide, vibrate=14]
    # [VIBRATE vibrate(2)]
    # [BG stage hide, reset]
    # [EVENT_CG event reset]
    # [SPRITE lay1 hide, reset]
    # [SPRITE lay8 hide, reset]
    # [SPRITE lay5 hide, reset]
    $ show_sprites()
    $ fade_fx(None)
    # [LAYER white image=+2 level=0]
    $ flash_fx("white")
    # [BGM bgm stop=1000]
    stop music fadeout 1.0
    # [SPRITE lay1 hide] [SPRITE lay5 hide] [BG stage hide] [EVENT_CG event hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER white hide]
    # → next scene 420

    # ==== SCENE 420 ====
    # [BG stage image=+43 level=200 → id(43)]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM bgm play=+20 → t20]
    play music t20 fadein 1.0
    # [SPRITE lay1 image=+306 level=160 dir=1A → l 1]
    $ show_sprites(("l 1",))
    # ルイズ：どう、少しは反省した？  [voice 7424]
    voice "ch8_l_018"
    l "Well, have you reflected a little? {#ch8_l_018}"
    # JA[7424]: どう、少しは反省した？
    # [SPRITE lay1 x=-96 y=0]
    # [SPRITE lay5 image=+396 level=160 dir=1A → s 1 sad]
    $ show_sprites(("s 1 sad", "l 1"))
    # サイト：しました、反省しました……。  [voice 13623]
    voice "ch8_s_064"
    s "I did, I reflected… {#ch8_s_064}"
    # JA[13623]: しました、反省しました……。
    # [SPRITE lay1 image=+339 level=160 dir=2A → l 1 angry]
    $ show_sprites(("s 1 sad", "l 1 angry"))
    # ルイズ：まったく、油断も隙もないんだから……。  [voice 7425]
    voice "ch8_l_019"
    l "Honestly, you're so careless and thoughtless… {#ch8_l_019}"
    # JA[7425]: まったく、油断も隙もないんだから……。
    # [SPRITE lay5 hide]
    $ show_sprites(("l 1 angry",))
    # [SPRITE lay8 image=+786 level=160 dir=1C → h 2]
    $ show_sprites(("l 1 angry", "h 2"))
    # アンリエッタ：それで、どうしたのですかルイズ？  [voice 895]
    voice "ch8_h_044"
    h "So, what is it, Louise? {#ch8_h_044}"
    # JA[895]: それで、どうしたのですかルイズ？
    # [SPRITE lay1 image=+302 level=160 dir=1A → l 1]
    $ show_sprites(("l 1", "h 2"))
    # ルイズ：ああ、そうです。実は、姫さまにご許可をいただきたいと思いまして、参りました。  [voice 7426]
    voice "ch8_l_020"
    l "Yes. Actually, I came to ask for Her Majesty's permission. {#ch8_l_020}"
    # JA[7426]: ああ、そうです。実は、姫さまにご許可をいただきたいと思いまして、参りました。
    # アンリエッタ：許可？どのようなことでしょう？  [voice 896]
    voice "ch8_h_045"
    h "Permission? What for? {#ch8_h_045}"
    # JA[896]: 許可？どのようなことでしょう？
    # [SPRITE lay1 image=+335 level=160 dir=2A → l 1 angry]
    $ show_sprites(("l 1 angry", "h 2"))
    # ルイズ：現在、レコン・キスタの艦隊が、こちらに向かっています。  [voice 7427]
    voice "ch8_l_021"
    l "Currently, the Reconquista fleet is heading this way. {#ch8_l_021}"
    # JA[7427]: 現在、レコン・キスタの艦隊が、こちらに向かっています。
    # [SPRITE lay8 image=+792 level=160 dir=1C → h 2 sad]
    $ show_sprites(("l 1 angry", "h 2 sad"))
    # アンリエッタ：レコン・キスタですか……。  [voice 897]
    voice "ch8_h_046"
    h "Reconquista… {#ch8_h_046}"
    # JA[897]: レコン・キスタですか……。
    # [SPRITE lay1 image=+302 level=160 dir=1A → l 1]
    $ show_sprites(("l 1", "h 2 sad"))
    # ルイズ：……姫さま。まだ、希望はあります。  [voice 7428]
    voice "ch8_l_022"
    l "…Princess. There is still hope. {#ch8_l_022}"
    # JA[7428]: ……姫さま。まだ、希望はあります。
    # [SPRITE lay8 image=+786 level=160 dir=1C → h 2]
    $ show_sprites(("l 1", "h 2"))
    # アンリエッタ：希望……ですか？  [voice 898]
    voice "ch8_h_047"
    h "Hope…? {#ch8_h_047}"
    # JA[898]: 希望……ですか？
    # [SPRITE lay8 hide]
    $ show_sprites(("l 1",))
    # [SPRITE lay5 image=+396 level=160 dir=1A → s 1 sad]
    $ show_sprites(("s 1 sad", "l 1"))
    # サイト：待て、ルイズ。お前、何をやる気だ？  [voice 13624]
    voice "ch8_s_065"
    s "Wait, Louise. What are you planning to do? {#ch8_s_065}"
    # JA[13624]: 待て、ルイズ。お前、何をやる気だ？
    # [SPRITE lay1 image=+335 level=160 dir=2A → l 1 angry]
    $ show_sprites(("s 1 sad", "l 1 angry"))
    # ルイズ：決まってるじゃない。レコン・キスタの連中を追っ払うのよ。  [voice 7429]
    voice "ch8_l_023"
    l "It's decided. We'll drive out the Reconquista forces. {#ch8_l_023}"
    # JA[7429]: 決まってるじゃない。レコン・キスタの連中を追っ払うのよ。
    # [SPRITE lay5 image=+394 level=160 dir=1A → s 1]
    $ show_sprites(("s 1", "l 1 angry"))
    # サイト：追っ払うって、どうやって！まさか、お前……！  [voice 13625]
    voice "ch8_s_066"
    s "Drive them out? How!? You don't mean…! {#ch8_s_066}"
    # JA[13625]: 追っ払うって、どうやって！まさか、お前……！
    # ルイズ：そうよ。ここまで来たら迷ってなんていられないもの。  [voice 7430]
    voice "ch8_l_024"
    l "Yes. At this point, I can't afford to hesitate. {#ch8_l_024}"
    # JA[7430]: そうよ。ここまで来たら迷ってなんていられないもの。
    # [SPRITE lay1 image=+302 level=160 dir=1A → l 1]
    $ show_sprites(("s 1", "l 1"))
    # ルイズ：そのために、ぜひ、姫さまのご許可をいただきたいのです。  [voice 7431]
    voice "ch8_l_025"
    l "For that, I want Her Majesty's permission. {#ch8_l_025}"
    # JA[7431]: そのために、ぜひ、姫さまのご許可をいただきたいのです。
    # [SPRITE lay5 hide]
    $ show_sprites(("l 1",))
    # [SPRITE lay8 image=+786 level=160 dir=1C → h 2]
    $ show_sprites(("l 1", "h 2"))
    # アンリエッタ：虚無の魔法の使用許可ですね。  [voice 899]
    voice "ch8_h_048"
    h "Permission to use Void Magic. {#ch8_h_048}"
    # JA[899]: 虚無の魔法の使用許可ですね。
    # ルイズ：はい。虚無の魔法をトリスタニアで使用する許可です。  [voice 7432]
    voice "ch8_l_026"
    l "Yes. Permission to use Void Magic in Tristain. {#ch8_l_026}"
    # JA[7432]: はい。虚無の魔法をトリスタニアで使用する許可です。
    # [SPRITE lay8 hide]
    $ show_sprites(("l 1",))
    # [SPRITE lay5 image=+394 level=160 dir=1A → s 1]
    $ show_sprites(("s 1", "l 1"))
    # サイト：ちょっと待て！お前、なに考えてるんだ！  [voice 13626]
    voice "ch8_s_067"
    s "Wait! What are you thinking?! {#ch8_s_067}"
    # JA[13626]: ちょっと待て！お前、なに考えてるんだ！
    # ルイズ：なによ、大声出して。これでも一生懸命考えたんだから。  [voice 7433]
    voice "ch8_l_027"
    l "What? You're shouting. I thought about this hard, you know. {#ch8_l_027}"
    # JA[7433]: なによ、大声出して。これでも一生懸命考えたんだから。
    # [SPRITE lay1 image=+335 level=160 dir=2A → l 1 angry]
    $ show_sprites(("s 1", "l 1 angry"))
    # ルイズ：砲台よりもまずは艦隊。虚無の魔法だったら、敵の意表を突けるはずよ。  [voice 7434]
    voice "ch8_l_028"
    l "The fleet first, before the fortresses. With Void Magic, we should be able to surprise the enemy. {#ch8_l_028}"
    # JA[7434]: 砲台よりもまずは艦隊。虚無の魔法だったら、敵の意表を突けるはずよ。
    # ルイズ：艦隊が負けたことを知れば、砲台にいる兵の士気も下がるわ。そこを軍に動いてもらうのよ。  [voice 7435]
    voice "ch8_l_029"
    l "If they learn the fleet lost, the soldiers' morale at the fortresses will drop. I'll have the army move there. {#ch8_l_029}"
    # JA[7435]: 艦隊が負けたことを知れば、砲台にいる兵の士気も下がるわ。そこを軍に動いてもらうのよ。
    # [SPRITE lay5 image=+396 level=160 dir=1A → s 1 sad]
    $ show_sprites(("s 1 sad", "l 1 angry"))
    # サイト：でもなぁ。この案はやっぱり反対だ。  [voice 13627]
    voice "ch8_s_068"
    s "But still. I'm against this plan. {#ch8_s_068}"
    # JA[13627]: でもなぁ。この案はやっぱり反対だ。
    # [SPRITE lay1 image=+306 level=160 dir=1A → l 1]
    $ show_sprites(("s 1 sad", "l 1"))
    # ルイズ：なんでよ！  [voice 7436]
    voice "ch8_l_030"
    l "Why! {#ch8_l_030}"
    # JA[7436]: なんでよ！
    # [SPRITE lay5 image=+394 level=160 dir=1A → s 1]
    $ show_sprites(("s 1", "l 1"))
    # サイト：そりゃ、お前が虚無の魔法を使えば、敵はなんとかできるかもしれないけど、だけど、この都はどうなる！？  [voice 13628]
    voice "ch8_s_069"
    s "If you use Void Magic, maybe we can handle the enemy, but what about this city!? {#ch8_s_069}"
    # JA[13628]: そりゃ、お前が虚無の魔法を使えば、敵はなんとかできるかもしれないけど、だけど、この都はどうなる！？
    # [SPRITE lay1 image=+302 level=160 dir=1A → l 1]
    $ show_sprites(("s 1", "l 1"))
    # ルイズ：どうもさっきから話が合わないような気がするんだけど。  [voice 7437]
    voice "ch8_l_031"
    l "I feel like we've been talking past each other. {#ch8_l_031}"
    # JA[7437]: どうもさっきから話が合わないような気がするんだけど。
    # [SPRITE lay1 image=+335 level=160 dir=2A → l 1 angry]
    $ show_sprites(("s 1", "l 1 angry"))
    # ルイズ：まさかわたしがエクスプロージョンで艦隊を吹っ飛ばすとか思ってんじゃないでしょうね？  [voice 7438]
    voice "ch8_l_032"
    l "You don't think I'm going to blow up the fleet with Explosion, do you? {#ch8_l_032}"
    # JA[7438]: まさかわたしがエクスプロージョンで艦隊を吹っ飛ばすとか思ってんじゃないでしょうね？
    # [SPRITE lay5 image=+429 level=160 dir=2A → s 3 sad]
    $ show_sprites(("s 3 sad", "l 1 angry"))
    # サイト：え……違うの？  [voice 13629]
    voice "ch8_s_070"
    s "Eh… no? {#ch8_s_070}"
    # JA[13629]: え……違うの？
    # [SPRITE lay1 image=+306 level=160 dir=1A → l 1]
    $ show_sprites(("s 3 sad", "l 1"))
    # ルイズ：違うわよっ！  [voice 7439]
    voice "ch8_l_033"
    l "No! {#ch8_l_033}"
    # JA[7439]: 違うわよっ！
    # [SPRITE lay1 image=+302 level=160 dir=1A → l 1]
    # ルイズ：いくらわたしでも、こんな人がいっぱいの場所であんなの使ったらどうなるかくらい、想像できるわよ。  [voice 7440]
    voice "ch8_l_034"
    l "Even I can imagine what would happen if I used that in a place full of people. {#ch8_l_034}"
    # JA[7440]: いくらわたしでも、こんな人がいっぱいの場所であんなの使ったらどうなるかくらい、想像できるわよ。
    # [SPRITE lay5 image=+390 level=160 dir=1A → s 1]
    $ show_sprites(("s 1", "l 1"))
    # サイト：……え？ということは……。  [voice 13630]
    voice "ch8_s_071"
    s "…Eh? Then that means… {#ch8_s_071}"
    # JA[13630]: ……え？ということは……。
    # [SPRITE lay1 image=+337 level=160 dir=2A → l 1 happy]
    $ show_sprites(("s 1", "l 1 happy"))
    # ルイズ：そうよ。新しい魔法を見つけたの。今回みたいな状況にぴったりなのをね。  [voice 7441]
    voice "ch8_l_035"
    l "Yes. I found a new magic. One perfect for situations like this. {#ch8_l_035}"
    # JA[7441]: そうよ。新しい魔法を見つけたの。今回みたいな状況にぴったりなのをね。
    # ルイズ：そいつを試してみようと思うの。  [voice 7442]
    voice "ch8_l_036"
    l "I want to try it. {#ch8_l_036}"
    # JA[7442]: そいつを試してみようと思うの。
    # [SPRITE lay5 image=+396 level=160 dir=1A → s 1 sad]
    $ show_sprites(("s 1 sad", "l 1 happy"))
    # サイト：それはそれで、ぶっつけ本番ってことだよな。  [voice 13631]
    voice "ch8_s_072"
    s "So that means it's a live test. {#ch8_s_072}"
    # JA[13631]: それはそれで、ぶっつけ本番ってことだよな。
    # [SPRITE lay1 image=+302 level=160 dir=1A → l 1]
    $ show_sprites(("s 1 sad", "l 1"))
    # ルイズ：つべこべ言わない！それしかないんだから。  [voice 7443]
    voice "ch8_l_037"
    l "No objections! There's no other way. {#ch8_l_037}"
    # JA[7443]: つべこべ言わない！それしかないんだから。
    # [SPRITE lay5 hide]
    $ show_sprites(("l 1",))
    # [SPRITE lay8 image=+786 level=160 dir=1C → h 2]
    $ show_sprites(("l 1", "h 2"))
    # アンリエッタ：ルイズ。それを使うことで、市民に被害を出すことなく襲撃者を制圧できるのですね。  [voice 900]
    voice "ch8_h_049"
    h "Louise. Using that, we can suppress the attackers without harming citizens. {#ch8_h_049}"
    # JA[900]: ルイズ。それを使うことで、市民に被害を出すことなく襲撃者を制圧できるのですね。
    # ルイズ：はい、わたしとサイトと、みんなの力があれば、敵を制圧することができるはずです。いえ、やってみせます。  [voice 7444]
    voice "ch8_l_038"
    l "Yes, with me, Saito, and everyone's power, we should be able to suppress the enemy. I'll show you. {#ch8_l_038}"
    # JA[7444]: はい、わたしとサイトと、みんなの力があれば、敵を制圧することができるはずです。いえ、やってみせます。
    # ルイズ：姫さまには、お城に戻って軍への指示をお願いします。  [voice 7445]
    voice "ch8_l_039"
    l "Princess, please return to the castle and give orders to the army. {#ch8_l_039}"
    # JA[7445]: 姫さまには、お城に戻って軍への指示をお願いします。
    # アンリエッタ：分かりました。ルイズ、トリスタニアでの虚無の魔法の使用を許可します。  [voice 901]
    voice "ch8_h_050"
    h "Understood. Louise, I grant permission to use Void Magic in Tristain. {#ch8_h_050}"
    # JA[901]: 分かりました。ルイズ、トリスタニアでの虚無の魔法の使用を許可します。
    # [SPRITE lay1 image=+304 level=160 dir=1A → l 1]
    $ show_sprites(("l 1", "h 2"))
    # ルイズ：はいっ！  [voice 7446]
    voice "ch8_l_040"
    l "Yes! {#ch8_l_040}"
    # JA[7446]: はいっ！
    # [SE se1 stop=1]
    $ se_fx("se1_stop")
    # [BGM bgm stop=1000]
    stop music fadeout 1.0
    # [SPRITE lay8 hide] [SPRITE lay1 hide] [BG stage hide]
    $ show_sprites()
    $ fade_fx(None)
    # → next scene 421

    # ==== SCENE 421 ====
    # [BG stage image=+43 level=200 → id(43)]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM bgm play=+28 → t28]
    play music t28 fadein 1.0
    # [SPRITE lay1 image=+302 level=160 dir=1A → l 1]
    $ show_sprites(("l 1",))
    # ルイズ：そんなわけで、改めて皆に手伝ってほしいの。力を貸して、お願い。  [voice 7447]
    voice "ch8_l_041"
    l "For that reason, I ask everyone for help. Please lend me your power. {#ch8_l_041}"
    # JA[7447]: そんなわけで、改めて皆に手伝ってほしいの。力を貸して、お願い。
    # [SPRITE lay1 x=-96 y=0]
    # [SPRITE lay4 image=+557 level=160 dir=1A → g 1]
    $ show_sprites(("l 1", "g 1"))
    # ギーシュ：女王陛下の命令とあらば、たとえ火の中水の中！もちろん参加させてもらうよ。  [voice 1562]
    voice "ch8_g_001"
    g "If Her Majesty commands it, through fire and water! Of course I'll join. {#ch8_g_001}"
    # JA[1562]: 女王陛下の命令とあらば、たとえ火の中水の中！もちろん参加させてもらうよ。
    # [SPRITE lay1 hide]
    $ show_sprites(("g 1",))
    # [SPRITE lay3 image=+852 level=160 dir=1A → m 1]
    $ show_sprites(("g 1", "m 1"))
    # モンモランシー：もう、しょうがないんだから。わたしももちろん手伝うわよ。  [voice 4174]
    voice "ch8_m_003"
    m "Honestly, there's no helping you. Of course I'll help too. {#ch8_m_003}"
    # JA[4174]: もう、しょうがないんだから。わたしももちろん手伝うわよ。
    # [SPRITE lay3 hide]
    $ show_sprites(("g 1",))
    # [SPRITE lay6 image=+676 level=160 dir=1A → k 1]
    $ show_sprites(("g 1", "k 1"))
    # キュルケ：打つ手があるのなら、それをしない理由なんてないわね。やられっぱなしは、あたしの主義に反するのよ。  [voice 3863]
    voice "ch8_k_006"
    k "If there's a way to fight, there's no reason not to. Being on the receiving end goes against my principles. {#ch8_k_006}"
    # JA[3863]: 打つ手があるのなら、それをしない理由なんてないわね。やられっぱなしは、あたしの主義に反するのよ。
    # [SPRITE lay4 hide]
    $ show_sprites(("k 1",))
    # [LAYER lay0 image=+588 level=160 dir=1A → t 1]
    $ show_sprites(("k 1", "t 1"))
    # タバサ：右に同じ。  [voice 15811]
    voice "ch8_t_001"
    t "Right side same. {#ch8_t_001}"
    # JA[15811]: 右に同じ。
    # [SPRITE lay6 hide] [LAYER lay0 hide]
    $ show_sprites()
    # [SPRITE lay1 image=+304 level=160 dir=1A → l 1]
    $ show_sprites(("l 1",))
    # ルイズ：ありがとう。  [voice 7448]
    voice "ch8_l_042"
    l "Thank you. {#ch8_l_042}"
    # JA[7448]: ありがとう。
    # [SPRITE lay1 hide]
    $ show_sprites()
    # [SPRITE lay2 image=+528 level=160 dir=2A → si 2]
    $ show_sprites(("si 2",))
    # シエスタ：皆さん、やっぱり戦いに行っちゃうんですね。  [voice 15174]
    voice "ch8_si_008"
    si "Everyone, you're really going to fight. {#ch8_si_008}"
    # JA[15174]: 皆さん、やっぱり戦いに行っちゃうんですね。
    # [SPRITE lay2 x=-96 y=0]
    # [SPRITE lay5 image=+396 level=160 dir=1A → s 1 sad]
    $ show_sprites(("si 2", "s 1 sad"))
    # サイト：シエスタ……。  [voice 13632]
    voice "ch8_s_073"
    s "Siesta… {#ch8_s_073}"
    # JA[13632]: シエスタ……。
    # [SPRITE lay5 image=+390 level=160 dir=1A → s 1]
    $ show_sprites(("si 2", "s 1"))
    # サイト：大丈夫だって。無事に帰ってくる。きみは宿屋に残って、待っててくれ。  [voice 13633]
    voice "ch8_s_074"
    s "It'll be fine. I'll come back safely. You stay at the inn and wait. {#ch8_s_074}"
    # JA[13633]: 大丈夫だって。無事に帰ってくる。きみは宿屋に残って、待っててくれ。
    # [SPRITE lay2 image=+489 level=160 dir=1A → si 1]
    $ show_sprites(("si 1", "s 1"))
    # シエスタ：分かりました。必ず……戻ってきてくださいね……。  [voice 15175]
    voice "ch8_si_009"
    si "Understood. Please… come back safely… {#ch8_si_009}"
    # JA[15175]: 分かりました。必ず……戻ってきてくださいね……。
    # [SPRITE lay5 image=+423 level=160 dir=2A → s 3]
    $ show_sprites(("si 1", "s 3"))
    # サイト：ああ、大丈夫さ。  [voice 13634]
    voice "ch8_s_075"
    s "Yeah, I'll be fine. {#ch8_s_075}"
    # JA[13634]: ああ、大丈夫さ。
    # [SPRITE lay2 hide]
    $ show_sprites(("s 3",))
    # [SPRITE lay5 hide]
    $ show_sprites()
    # [SPRITE lay1 image=+302 level=160 dir=1A → l 1]
    $ show_sprites(("l 1",))
    # ルイズ：それじゃあ、作戦を説明するわ。わたしとサイトが城の高台に移動するの。皆には……。  [voice 7449]
    voice "ch8_l_043"
    l "Then I'll explain the operation. Saito and I will move to the castle hill. Everyone… {#ch8_l_043}"
    # JA[7449]: それじゃあ、作戦を説明するわ。わたしとサイトが城の高台に移動するの。皆には……。
    # [SPRITE lay1 x=-96 y=0]
    # [SPRITE lay6 image=+676 level=160 dir=1A → k 1]
    $ show_sprites(("l 1", "k 1"))
    # キュルケ：あんた達が城にたどりつけるよう、敵をひきつけろってわけね？  [voice 3864]
    voice "ch8_k_007"
    k "So you want us to lure the enemy so you can reach the castle? {#ch8_k_007}"
    # JA[3864]: あんた達が城にたどりつけるよう、敵をひきつけろってわけね？
    # [SPRITE lay1 image=+335 level=160 dir=2A → l 1 angry]
    $ show_sprites(("l 1 angry", "k 1"))
    # ルイズ：ええ。できるだけ城から敵を離してほしいの。  [voice 7450]
    voice "ch8_l_044"
    l "Yes. I want you to keep the enemy away from the castle as much as possible. {#ch8_l_044}"
    # JA[7450]: ええ。できるだけ城から敵を離してほしいの。
    # [SPRITE lay6 hide]
    $ show_sprites(("l 1 angry",))
    # [SPRITE lay4 image=+555 level=160 dir=1A → g 1]
    $ show_sprites(("l 1 angry", "g 1"))
    # ギーシュ：高台に昇るのはいいけど、そこで何をしようってんだい？  [voice 1563]
    voice "ch8_g_002"
    g "Going to the hill is fine, but what will you do there? {#ch8_g_002}"
    # JA[1563]: 高台に昇るのはいいけど、そこで何をしようってんだい？
    # [SPRITE lay1 image=+343 level=160 dir=2A → l 1 angry]
    $ show_sprites(("l 1 angry", "g 1"))
    # ルイズ：そ、それはその……。いろいろあるのよっ！詳しいことは言えないけど……。  [voice 7451]
    voice "ch8_l_045"
    l "T-That's… there are various reasons! I can't say details, but… {#ch8_l_045}"
    # JA[7451]: そ、それはその……。いろいろあるのよっ！詳しいことは言えないけど……。
    # サイト：（虚無のことは誰にも言えないからな……）
    # [no voice — thought]
    s (I can't tell anyone about Void Magic…)
    # JA: （虚無のことは誰にも言えないからな……）
    # [SPRITE lay1 hide] [SPRITE lay4 hide]
    $ show_sprites()
    # [SPRITE lay6 image=+676 level=160 dir=1A → k 1]
    $ show_sprites(("k 1",))
    # キュルケ：まあいいわ。  [voice 3865]
    voice "ch8_k_008"
    k "Well, I don't mind. {#ch8_k_008}"
    # JA[3865]: まあいいわ。
    # [SPRITE lay6 image=+678 level=160 dir=1A → k 1]
    $ show_sprites(("k 1",))
    # キュルケ：何をするのか分からないけど、それしか手がないっていうのなら、あたし達にできることをするだけよ。  [voice 3866]
    voice "ch8_k_009"
    k "I don't know what you'll do, but if that's the only option, we'll do what we can. {#ch8_k_009}"
    # JA[3866]: 何をするのか分からないけど、それしか手がないっていうのなら、あたし達にできることをするだけよ。
    # [SPRITE lay6 image=+709 level=160 dir=2A → k 1]
    $ show_sprites(("k 1",))
    # キュルケ：もっとも、ヴァリエールにいいところを持ってかれるとこが面白くないけどね。  [voice 3867]
    voice "ch8_k_010"
    k "Although, it's not fun that Variel will take the good parts. {#ch8_k_010}"
    # JA[3867]: もっとも、ヴァリエールにいいところを持ってかれるとこが面白くないけどね。
    # [SPRITE lay6 x=224 y=0]
    # [LAYER lay0 image=+592 level=160 dir=1A → t 1]
    $ show_sprites(("k 1", "t 1"))
    # タバサ：正念場。  [voice 15812]
    voice "ch8_t_002"
    t "The critical moment. {#ch8_t_002}"
    # JA[15812]: 正念場。
    # [SPRITE lay6 hide] [LAYER lay0 hide]
    $ show_sprites()
    # [SPRITE lay5 image=+390 level=160 dir=1A → s 1]
    $ show_sprites(("s 1",))
    # サイト：よし。そうと決まったら、明朝が勝負だな……。  [voice 13635]
    voice "ch8_s_076"
    s "Good. If that's decided, tomorrow is the battle… {#ch8_s_076}"
    # JA[13635]: よし。そうと決まったら、明朝が勝負だな……。
    # [SPRITE lay5 hide]
    $ show_sprites()
    # [SPRITE lay8 image=+775 level=160 dir=1B → h 2]
    $ show_sprites(("h 2",))
    # アンリエッタ：皆様、集まっていますか。  [voice 902]
    voice "ch8_h_051"
    h "Everyone, are you gathered? {#ch8_h_051}"
    # JA[902]: 皆様、集まっていますか。
    # [SPRITE lay8 x=224 y=0]
    # [SPRITE lay5 image=+394 level=160 dir=1A → s 1]
    $ show_sprites(("h 2", "s 1"))
    # サイト：お姫さま！？  [voice 13636]
    voice "ch8_s_077"
    s "Princess!? {#ch8_s_077}"
    # JA[13636]: お姫さま！？
    # [SPRITE lay5 hide]
    $ show_sprites(("h 2",))
    # [SPRITE lay1 image=+302 level=160 dir=1A → l 1]
    $ show_sprites(("h 2", "l 1"))
    # ルイズ：姫さま！お体はもうよろしいのですか？  [voice 7452]
    voice "ch8_l_046"
    l "Princess! Are you well? {#ch8_l_046}"
    # JA[7452]: 姫さま！お体はもうよろしいのですか？
    # [SPRITE lay8 image=+777 level=160 dir=1B → h 2]
    $ show_sprites(("h 2", "l 1"))
    # アンリエッタ：ええ、もう大丈夫。  [voice 903]
    voice "ch8_h_052"
    h "Yes, I'm fine now. {#ch8_h_052}"
    # JA[903]: ええ、もう大丈夫。
    # [SPRITE lay8 image=+775 level=160 dir=1B → h 2]
    $ show_sprites(("h 2", "l 1"))
    # アンリエッタ：ルイズ、城に向かうのですね。  [voice 904]
    voice "ch8_h_053"
    h "Louise, you're heading to the castle. {#ch8_h_053}"
    # JA[904]: ルイズ、城に向かうのですね。
    # ルイズ：はい。姫さまは今しばらくここでお待ちください。このトリスタニアに平和を取り戻してきます。  [voice 7453]
    voice "ch8_l_047"
    l "Yes. Princess, please wait here a while. I will restore peace to this Tristain. {#ch8_l_047}"
    # JA[7453]: はい。姫さまは今しばらくここでお待ちください。このトリスタニアに平和を取り戻してきます。
    # アンリエッタ：心強いですね、ルイズ。でも、あなた達だけに戦わせるわけにはまいりません。  [voice 905]
    voice "ch8_h_054"
    h "That's reassuring, Louise. But I can't have only you fight. {#ch8_h_054}"
    # JA[905]: 心強いですね、ルイズ。でも、あなた達だけに戦わせるわけにはまいりません。
    # アンリエッタ：わたくしも戦います。  [voice 906]
    voice "ch8_h_055"
    h "I will fight too. {#ch8_h_055}"
    # JA[906]: わたくしも戦います。
    # [SPRITE lay1 image=+308 level=160 dir=1A → l 1]
    $ show_sprites(("h 2", "l 1"))
    # ルイズ：あ、あの、姫さま！？いくらなんでもそれは無茶です！  [voice 7454]
    voice "ch8_l_048"
    l "W-W-W-Well, Princess!? That's too reckless! {#ch8_l_048}"
    # JA[7454]: あ、あの、姫さま！？いくらなんでもそれは無茶です！
    # [SPRITE lay1 hide]
    $ show_sprites(("h 2",))
    # [SPRITE lay5 image=+394 level=160 dir=1A → s 1]
    $ show_sprites(("h 2", "s 1"))
    # サイト：そうですよ！俺達が言うのもなんですけど、危険な戦いになるのは確実なんですよ！？  [voice 13637]
    voice "ch8_s_078"
    s "That's right! Even we hesitate to say it, but it'll definitely be a dangerous battle!? {#ch8_s_078}"
    # JA[13637]: そうですよ！俺達が言うのもなんですけど、危険な戦いになるのは確実なんですよ！？
    # アンリエッタ：皆さんの言うことは、よく分かります。でも、わたくし１人がただ、不安に震えているわけにはまいりません。  [voice 907]
    voice "ch8_h_056"
    h "I understand what you're saying. But I can't just tremble with anxiety alone. {#ch8_h_056}"
    # JA[907]: 皆さんの言うことは、よく分かります。でも、わたくし１人がただ、不安に震えているわけにはまいりません。

    # ---- 【選択肢】 ----
    menu:
        "Stop with all force.{#ch8_c007}":
            # JA: 全力で止める
            # [SPRITE lay8 image=+775 level=160 dir=1B → h 2]
            $ show_sprites(("h 2", "s 1"))
            # [SPRITE lay5 image=+394 level=160 dir=1A → s 1]
            # [BGM bgm play=+28 → t28]
            play music t28 fadein 1.0
            # [BG stage image=+43 level=200 → id(43)]
            $ fade_fx("id(43)")
            # [SPRITE lay5 image=+394 level=160 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2"))
            # サイト：駄目ですよ、お姫さま。俺は許可できません。  [voice 13638]
            voice "ch8_s_079"
            s "No way, Princess. I can't grant permission. {#ch8_s_079}"
            # JA[13638]: 駄目ですよ、お姫さま。俺は許可できません。
            # [SPRITE lay8 image=+775 level=160 dir=1B → h 2]
            $ show_sprites(("s 1", "h 2"))
            # アンリエッタ：わたくしは女王なのです。先頭に立って戦わなければ、誰がついてくるのですか？  [voice 908]
            voice "ch8_h_057"
            h "I am the Queen. If I don't lead the front lines, who will follow? {#ch8_h_057}"
            # JA[908]: わたくしは女王なのです。先頭に立って戦わなければ、誰がついてくるのですか？
            # [SPRITE lay5 image=+396 level=160 dir=1A → s 1 sad]
            $ show_sprites(("s 1 sad", "h 2"))
            # サイト：……。  [voice 13639]
            voice "ch8_s_080"
            s "… {#ch8_s_080}"
            # JA[13639]: ……。
            # [SPRITE lay5 image=+390 level=160 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2"))
            # → next scene 425
            # Часть 2 заканчивается: сцена 425 — в script-ch8_3.rpy.
            jump ch8_3

        "Affirm with all force.{#ch8_c008}":
            # JA: 全力で肯定する
            # [SPRITE lay8 image=+775 level=160 dir=1B → h 2]
            $ show_sprites(("h 2", "s 1"))
            # [SPRITE lay5 image=+394 level=160 dir=1A → s 1]
            # [BGM bgm play=+28 → t28]
            play music t28 fadein 1.0
            # [BG stage image=+43 level=200 → id(43)]
            $ fade_fx("id(43)")
            # [SPRITE lay5 image=+390 level=160 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2"))
            # サイト：分かりました。俺も手伝います。  [voice 13640]
            voice "ch8_s_081"
            s "Understood. I'll help too. {#ch8_s_081}"
            # JA[13640]: 分かりました。俺も手伝います。
            # [SPRITE lay5 hide]
            $ show_sprites(("h 2",))
            # [SPRITE lay1 image=+306 level=160 dir=1A → l 1]
            $ show_sprites(("h 2", "l 1"))
            # ルイズ：サイト！あんた何言ってるのか、分かってるの？  [voice 7455]
            voice "ch8_l_049"
            l "Saito! Do you understand what you're saying? {#ch8_l_049}"
            # JA[7455]: サイト！あんた何言ってるのか、分かってるの？
            # [SPRITE lay8 image=+775 level=160 dir=1B → h 2]
            $ show_sprites(("h 2", "l 1"))
            # アンリエッタ：ルイズ、わたしくは女王なのです。先頭に立って戦わなければ、誰がついてくるのですか？  [voice 909]
            voice "ch8_h_058"
            h "Louise, I am the Queen. If I don't lead the front lines, who will follow? {#ch8_h_058}"
            # JA[909]: ルイズ、わたしくは女王なのです。先頭に立って戦わなければ、誰がついてくるのですか？
            # [SPRITE lay1 image=+308 level=160 dir=1A → l 1]
            $ show_sprites(("h 2", "l 1"))
            # ルイズ：……。  [voice 7456]
            voice "ch8_l_050"
            l "… {#ch8_l_050}"
            # JA[7456]: ……。
            # [SPRITE lay1 hide]
            $ show_sprites(("h 2",))
            # [SPRITE lay5 image=+390 level=160 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2"))
            # → next scene 425
            # Часть 2 заканчивается: сцена 425 — в script-ch8_3.rpy.
            jump ch8_3

        "Go all-out youthful.{#ch8_c009}":
            # JA: 全力で青春する
            # 场景 424 — «全力で青春する» ветка содержится в script-ch8_3.rpy.
            # Часть 2 заканчивается: сцена 424 — в script-ch8_3.rpy.
            jump ch8_3
