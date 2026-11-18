# Глава 11, часть 2 (сцены 472-477): «ハルナの決意» — поиск, встреча, прощание.
# Источник: ps2_source/chapters/chapter_12_ハルナの決意.txt (SCENE 472-477).
# Точные аргументы: ps2_source/events_full/chapter_12_ハルナの決意.txt.
#
# Голоса: 77. Нумерация ch11_<spk>_<NNN> — с 001 по говорящему (продолжение ch11_1).
#   si: 15132-15134 (3)  — ch11_si_013..015
#   s: 13228-13250 (23)  — ch11_s_017..039 (s_013..016 — безголосые мысли)
#   l: 7168-7171 (4)     — ch11_l_009..012
#   ha: 2559-2589 (31)   — ch11_ha_001..031
#   k: 3814-3818 (5)     — ch11_k_001..005
#   w: 16081-16086 (6)   — ch11_w_001..006
#   c: 1204 (1)          — ch11_c_001
#   g: 1538 (1)          — ch11_g_001
#   m: 4158 (1)          — ch11_m_001
#   o: 4511-4512 (2)     — ch11_o_001..002
# Фоны: id(32)=kitchen, id(23)=classroom, id(26)=yard, id(88)=sky, id(85)=forest, id(54)=theater_backstage, id(2)=white.
# CG: id(297-299) — заглушки id(K), требуют решения человека.
# BGM: bgm play=+28→t27, +17→t16, +19→t18, +23→t22, +31→t30, +22→t21.
# SE: se1 stop=1, se0 play=+94 — не переносятся (SE заглушка).
# Не переносятся: MOVIE, waitSEStop/waitLoad/waitAction, beginSkip/endSkip.
# 【選択肢】 в сцене 473 → menu + *_choice (3 варианта: 474/475/476 → 477).
# В Inner Thoughts (…без voice) — без voice-тега, только EN.

label ch11_2:

    # ==== SCENE 472 ====
    # [BG stage image=+32, level=200] [TRANS 1000]
    # [BGM bgm play=+28 → t27]
    $ fade_fx("kitchen")
    play music t27 fadein 1.0
    $ show_sprites()
    # [SPRITE lay5 image=+394, level=160, dir=1A]
    # サイト：（……駄目だ。 / どこにもいない）
    s "No good. / She's nowhere.{#ch11_s_013}"
    # JA(no voice): サイト：（……駄目だ。 / どこにもいない）
    # [SPRITE lay5 hide]
    # [BG stage hide]
    # [BG stage image=+23, level=200] [TRANS 1000]
    $ fade_fx("classroom")
    # [SPRITE lay5 image=+396, level=160, dir=1A]
    # サイト：（どこに行ったんだよ。 / まさかホントに……）
    s "Where did she go? / Don't tell me she really…{#ch11_s_014}"
    # JA(no voice): サイト：（どこに行ったんだよ。 / まさかホントに……）
    # [SPRITE lay5 hide]
    # [BG stage hide]
    # [BG stage image=+26, level=200] [TRANS 1000]
    $ fade_fx("yard")
    # [SPRITE lay5 image=+390, level=160, dir=1A]
    # サイト：（……そうだ、森！ / まだ、あそこには行っていなかった！）
    s "…That's right, the forest! / I haven't checked there yet!{#ch11_s_015}"
    # JA(no voice): サイト：（……そうだ、森！ / まだ、あそこには行っていなかった！）
    # [SPRITE lay5 hide]
    # [BG stage hide]
    # [BG stage image=+88, level=200] [TRANS 1000]
    $ fade_fx("sky")
    # null：………。 / ……。 / …。  (no voice)
    # [BGM bgm stop=1000]
    stop music fadeout 1.0
    # [BG stage hide]
    # [BG stage image=+85, level=200] [TRANS 1000]
    $ fade_fx("forest")
    # [SPRITE lay7 image=+957, level=160, dir=1A]
    # [BGM bgm play=+17 → t16]
    play music t16 fadein 1.0
    # サイト：（……いた、春奈だ！）
    s "…There she is, Haruna!{#ch11_s_016}"
    # JA[13228]: サイト：（……いた、春奈だ！） — PROVISIONAL (dup of 13228)
    # [SPRITE lay7 image=+955, level=160, dir=1A]
    # ハルナ：平賀くん！ / どうしてこんなところに！？ [voice 2559]
    voice "ch11_ha_001"
    ha "Hiragan-kun! / Why are you in a place like this!?{#ch11_ha_001}"
    # JA[2559]: ハルナ：平賀くん！ / どうしてこんなところに！？
    # [SPRITE lay7 x=-96, y=0]
    # [SPRITE lay5 image=+427, level=160, dir=2A]
    # サイト：どうしてこんなところにじゃないよ！ [voice 13228]
    voice "ch11_s_017"
    s "That's not 'why are you here'!{#ch11_s_017}"
    # JA[13228]: サイト：どうしてこんなところにじゃないよ！
    # サイト：春奈が急にいなくなったりするから、 / こっちは大騒ぎだぞ！ [voice 13229]
    voice "ch11_s_018"
    s "You suddenly disappear / and everyone's in an uproar!{#ch11_s_018}"
    # JA[13229]: サイト：春奈が急にいなくなったりするから、こっちは大騒ぎだぞ！
    # [SPRITE lay7 image=+957, level=160, dir=1A]
    # ハルナ：えっ……。 / あの、その……。 [voice 2560]
    voice "ch11_ha_002"
    ha "Eh… / Um, well…{#ch11_ha_002}"
    # JA[2560]: ハルナ：えっ……。 / あの、その……。
    # [SPRITE lay5 image=+394, level=160, dir=1A]
    # サイト：シエスタなんか、悩んでる春奈を見てたから、 / 縁起でもないこと考えだすし……。 [voice 13230]
    voice "ch11_s_019"
    s "Even Siesta, seeing you worried, / started thinking the worst…{#ch11_s_019}"
    # JA[13230]: サイト：シエスタなんか、悩んでる春奈を見てたから、縁起でもないこと考えだすし……。
    # サイト：ルイズ達も心配して探しまわってるんだぞ！ [voice 13231]
    voice "ch11_s_020"
    s "Louise and the others are worried sick looking for you!{#ch11_s_020}"
    # JA[13231]: サイト：ルイズ達も心配して探しまわってるんだぞ！
    # [SPRITE lay7 image=+957, level=160, dir=1A]
    # ハルナ：ご、ごめんなさい。 / 静かに考えたくて。 [voice 2561]
    voice "ch11_ha_003"
    ha "I-I'm sorry. / I just wanted to think in peace.{#ch11_ha_003}"
    # JA[2561]: ハルナ：ご、ごめんなさい。 / 静かに考えたくて。
    # [SPRITE lay5 image=+396, level=160, dir=1A]
    # サイト：やっぱり、ウェザリーさんからの誘いのこと？ [voice 13232]
    voice "ch11_s_021"
    s "As I thought, it's about Weatherly-san's offer?{#ch11_s_021}"
    # JA[13232]: サイト：やっぱり、ウェザリーさんからの誘いのこと？
    # ハルナ：うん。 [voice 2562]
    voice "ch11_ha_004"
    ha "Yeah.{#ch11_ha_004}"
    # JA[2562]: ハルナ：うん。
    # [SPRITE lay7 hide]
    # [SPRITE lay5 hide]
    # [BG stage hide]
    # [EVENT_CG event image=+298, level=80] [TRANS 1000]
    # CG placeholder
    $ dissolve_fx("id(298)")
    # ハルナ：ホントはね、最初から返事は決まってたの。 / 私がこの世界で生きてくためって考えればね。 [voice 2563]
    voice "ch11_ha_005"
    ha "Actually, my answer was decided from the start. / If I think about living in this world…{#ch11_ha_005}"
    # JA[2563]: ハルナ：ホントはね、最初から返事は決まってたの。 / 私がこの世界で生きてくためって考えればね。
    # サイト：そ、それって……。 [voice 13233]
    voice "ch11_s_022"
    s "Th-that means…{#ch11_s_022}"
    # JA[13233]: サイト：そ、それって……。
    # ハルナ：でも、そう答えるには、 / 勇気が……足りなかった。 [voice 2564]
    voice "ch11_ha_006"
    ha "But to give that answer… / I didn't have enough… courage.{#ch11_ha_006}"
    # JA[2564]: ハルナ：でも、そう答えるには、勇気が……足りなかった。
    # サイト：勇気？ [voice 13234]
    voice "ch11_s_023"
    s "Courage?{#ch11_s_023}"
    # JA[13234]: サイト：勇気？
    # ハルナ：この学院を離れる勇気。 [voice 2565]
    voice "ch11_ha_007"
    ha "The courage to leave this academy.{#ch11_ha_007}"
    # JA[2565]: ハルナ：この学院を離れる勇気。
    # ハルナ：ルイズさんがいて、シエスタさんがいて、 / みんながいて……。 [voice 2566]
    voice "ch11_ha_008"
    ha "Louise-san is here, Siesta-san is here, / everyone is here…{#ch11_ha_008}"
    # JA[2566]: ハルナ：ルイズさんがいて、シエスタさんがいて、みんながいて……。
    # ハルナ：急にこっちの世界に来て、 / 不安だったり、怖かったりもしたけど、 [voice 2567]
    voice "ch11_ha_009"
    ha "Suddenly coming to this world, / I was anxious, scared even, / but…{#ch11_ha_009}"
    # JA[2567]: ハルナ：急にこっちの世界に来て、不安だったり、怖かったりもしたけど、
    # ハルナ：この学院にいる時間は、 / そんなこと忘れられるくらい、楽しかったわ。 [voice 2568]
    voice "ch11_ha_010"
    ha "The time at this academy was / so fun I forgot all that.{#ch11_ha_010}"
    # JA[2568]: ハルナ：この学院にいる時間は、そんなことは忘れられるくらい、楽しかったわ。
    # ハルナ：それに、平賀くんがいつもいてくれたし。 [voice 2569]
    voice "ch11_ha_011"
    ha "Besides, Hiragan-kun was always there for me.{#ch11_ha_011}"
    # JA[2569]: ハルナ：それに、平賀くんがいつもいてくれたし。
    # サイト：なるほど、俺がいたからね。 / って俺？ [voice 13235]
    voice "ch11_s_024"
    s "I see, because I was here. / Wait, me?{#ch11_s_024}"
    # JA[13235]: サイト：なるほど、俺がいたからね。って俺？
    # [EVENT_CG event image=+299, level=80]
    $ dissolve_fx("id(299)")
    # ハルナ：……うん。 [voice 2570]
    voice "ch11_ha_012"
    ha "…Yeah.{#ch11_ha_012}"
    # JA[2570]: ハルナ：……うん。
    # サイト：え、えっと、それって……。 [voice 13236]
    voice "ch11_s_025"
    s "Uh, um, that means…{#ch11_s_025}"
    # JA[13236]: サイト：え、えっと、それって……。
    # [EVENT_CG event image=+297, level=80]
    $ dissolve_fx("id(297)")
    # ハルナ：でも、もういいの。 / もう、決めたから。 [voice 2571]
    voice "ch11_ha_013"
    ha "But it's okay now. / I've already decided.{#ch11_ha_013}"
    # JA[2571]: ハルナ：でも、もういいの。もう、決めたから。
    # ハルナ：わたし、ウェザリーさんの劇団に入る。 [voice 2572]
    voice "ch11_ha_014"
    ha "I'm joining Weatherly-san's troupe.{#ch11_ha_014}"
    # JA[2572]: ハルナ：わたし、ウェザリーさんの劇団に入る。
    # サイト：お、おい。 / 春奈！ [voice 13237]
    voice "ch11_s_026"
    s "H-hey. / Haruna!{#ch11_s_026}"
    # JA[13237]: サイト：お、おい。春奈！
    # ハルナ：そ、そんな顔しないでよ、平賀くん。 / 自分で決めたことなんだから、平気よ。 / ……たぶん。 [voice 2573]
    voice "ch11_ha_015"
    ha "D-don't make that face, Hiragan-kun. / I decided this myself, so I'm fine. / …Probably.{#ch11_ha_015}"
    # JA[2573]: ハルナ：そ、そんな顔しないでよ、平賀くん。自分で決めたことなんだから、平気よ。……たぶん。
    # サイト：……。 [voice 13238]
    voice "ch11_s_039"
    s "…{#ch11_s_039}"
    # JA[13238]: サイト：……。
    # [EVENT_CG event image=+299, level=80]
    $ dissolve_fx("id(299)")
    # ハルナ：それにね、ウェザリーさんの劇団は / 旅回りだけど、トリスタニアにはよく / 来るらしいし……。 [voice 2574]
    voice "ch11_ha_016"
    ha "they say they come to Tristain often, so… {#ch11_ha_016}"
    # JA[2574]: ハルナ：それにね、ウェザリーさんの劇団は旅回りだけど、トリスタニアにはよく来るらしいし……。
    # ハルナ：平賀くんや学院のみんなには、 / いつでも会えるから……大丈夫。 [voice 2575]
    voice "ch11_ha_017"
    ha "I can see Hiragan-kun and everyone / anytime… it's okay.{#ch11_ha_017}"
    # JA[2575]: ハルナ：平賀くんや学院のみんなには、いつでも会えるから……大丈夫。
    # サイト：ああ、そうだよな。 / いつでも会えるよ。 / 何があっても大歓迎さ。 [voice 13239]
    voice "ch11_s_027"
    s "Yeah, that's right. / You can visit anytime. / You're always welcome.{#ch11_s_027}"
    # JA[13239]: サイト：ああ、そうだよな。いつでも会えるよ。何があっても大歓迎さ。
    # ハルナ：うん。 [voice 2576]
    voice "ch11_ha_018"
    ha "Yeah.{#ch11_ha_018}"
    # JA[2576]: ハルナ：うん。
    # サイト：……。 [voice 13240]
    voice "ch11_s_028"
    s "…{#ch11_s_028}"
    # JA[13240]: サイト：……。
    # [EVENT_CG event image=+297, level=80]
    # ハルナ：……。 / ハルナ：いけない！ / みんな心配してくれてるんだよね。 / 戻らないと！ [voice 2577]
    voice "ch11_ha_019"
    ha "… / Wait! / Everyone's worried, right? / I have to go back!{#ch11_ha_019}"
    # JA[2577]: ハルナ：……。いけない！みんな心配してくれてるんだよね。戻らないと！
    # サイト：そ、そうだな。 / シエスタがカンカンだぞ！ [voice 13241]
    voice "ch11_s_029"
    s "Y-yeah. / Siesta's gonna be furious!{#ch11_s_029}"
    # JA[13241]: サイト：そ、そうだな。シエスタがカンカンだぞ！
    # [SE se1 stop=1] [BGM bgm stop=1000] [SPRITE hide] [EVENT_CG hide]
    # → next scene 473

    # ==== SCENE 473 ====
    # [BG stage image=+26, level=200] [TRANS 1000]
    $ fade_fx("yard")
    # [BGM bgm play=+19 → t18]
    play music t18 fadein 1.0
    # [SPRITE lay7 image=+951, level=160, dir=1A]
    # ハルナ：それでは皆さん、短い間でしたが / お世話になりました。 [voice 2578]
    voice "ch11_ha_020"
    ha "Well then, everyone, it was short, but / thank you for everything.{#ch11_ha_020}"
    # JA[2578]: ハルナ：それでは皆さん、短い間でしたがお世話になりました。
    # [SPRITE lay7 x=-96, y=0]
    # [SPRITE lay1 image=+304, level=160, dir=1A]
    # ルイズ：劇団でも頑張ってね、ハルナ。 [voice 7168]
    voice "ch11_l_009"
    l "Do your best at the troupe too, Haruna.{#ch11_l_009}"
    # JA[7168]: ルイズ：劇団でも頑張ってね、ハルナ。
    # ハルナ：ルイズさん、いろいろありがとうございました。 / 平賀くんのことよろしくお願いします。 [voice 2579]
    voice "ch11_ha_021"
    ha "Louise-san, thank you for everything. / Please take care of Hiragan-kun.{#ch11_ha_021}"
    # JA[2579]: ハルナ：ルイズさん、いろいろありがとうございました。平賀くんのことよろしくお願いします。
    # [SPRITE lay1 image=+337, level=160, dir=2A]
    # ルイズ：大丈夫よ。 [voice 7169]
    voice "ch11_l_010"
    l "It's fine.{#ch11_l_010}"
    # JA[7169]: ルイズ：大丈夫よ。
    # [SPRITE lay1 hide]
    # [SPRITE lay2 image=+495, level=160, dir=1A]
    # シエスタ：さ、さびしくなります。 / ハルナさん……。 [voice 15132]
    voice "ch11_si_013"
    si "It's gonna be… lonely. / Haruna-san…{#ch11_si_013}"
    # JA[15132]: シエスタ：さ、さびしくなります。ハルナさん……。
    # シエスタ：た、旅先では生水とか飲んじゃダメですよ。 / 変な人についていかないでね。 / それから……それから……。 [voice 15133]
    voice "ch11_si_014"
    si "D-don't drink untreated water on your travels. / Don't follow suspicious people. / And then… and then…{#ch11_si_014}"
    # JA[15133]: シエスタ：た、旅先では生水とか飲んじゃダメですよ。変な人についていかないでね。それから……それから……。
    # [SPRITE lay7 image=+953, level=160, dir=1A]
    # ハルナ：もう、シエスタさんったら。 / 私、そんなに子供じゃないですよ。 [voice 2580]
    voice "ch11_ha_022"
    ha "Geez, Siesta-san. / I'm not that much of a child.{#ch11_ha_022}"
    # JA[2580]: ハルナ：もう、シエスタさんったら。私、そんなに子供じゃないですよ。
    # [SPRITE lay2 image=+528, level=160, dir=2A]
    # シエスタ：そ、そうですよね……。 [voice 15134]
    voice "ch11_si_015"
    si "R-right, of course…{#ch11_si_015}"
    # JA[15134]: シエスタ：そ、そうですよね……。
    # [SPRITE lay2 hide] [SPRITE lay7 hide]
    # [LAYER lay0 image=+594, level=160, dir=1A] [SPRITE lay6 image=+715, level=160, dir=2A]
    # キュルケ：……。 / タバサ：……。 [no voice]
    # [LAYER lay0 hide] [SPRITE lay6 hide]
    # [SPRITE lay3 image=+852, level=160, dir=1A] [SPRITE lay4 image=+561, level=160, dir=1A]
    # モンモランシー：どうしたの？ / ２人とも難しい顔して。 [voice 4158]
    voice "ch11_m_001"
    m "What's wrong? / You both have such difficult faces.{#ch11_m_001}"
    # JA[4158]: モンモランシー：どうしたの？２人とも難しい顔して。
    # [SPRITE lay4 image=+572, level=160, dir=2A]
    # ギーシュ：あんなかわいい子がいなくなるのは残念だな / って、イタタ……。 / つねらないで、モンモランシー！ [voice 1538]
    voice "ch11_g_001"
    g "It's a shame such a cute girl is leaving / Ow… / Don't pinch me, Montmorency!{#ch11_g_001}"
    # JA[1538]: ギーシュ：あんなかわいい子がいなくなるのは残念だなって、イタタ…つねらないで、モンモランシー！
    # [SPRITE lay3 hide] [SPRITE lay4 hide]
    # [SPRITE lay20 image=+1063, level=160, dir=1A]
    # ウェザリー：あらあら、人気者なのね。 / ハルナ。 [voice 16081]
    voice "ch11_w_001"
    w "My my, you're popular. / Haruna.{#ch11_w_001}"
    # JA[16081]: ウェザリー：あらあら、人気者なのね。ハルナ。
    # [SPRITE lay20 x=224, y=0]
    # [SPRITE lay7 image=+951, level=160, dir=1A]
    # ハルナ：ウェザリーさん。 [voice 2581]
    voice "ch11_ha_023"
    ha "Weatherly-san.{#ch11_ha_023}"
    # JA[2581]: ハルナ：ウェザリーさん。
    # [SPRITE lay20 hide]
    # [SPRITE lay9 image=+929, level=160, dir=1A]
    # コルベール：ハルナ、体には気をつけるように。 / 旅暮らしでは、ふとしたことが大きな病気に / つながるものです。 [voice 1204]
    voice "ch11_c_001"
    c "Haruna, take care of your health. / In a traveling life, small things can lead to serious illness.{#ch11_c_001}"
    # JA[1204]: コルベール：ハルナ、体には気をつけるように。旅暮らしでは、ふとしたことが大きな病気につながるものです。
    # [SPRITE lay9 hide]
    # [SPRITE lay10 image=+920, level=160, dir=1A]
    # オスマン：学院には気軽に立ち寄られよ。 / 一座のきれいどころもつれての。 [voice 4511]
    voice "ch11_o_001"
    o "Feel free to drop by the academy. / Bring the troupe's beauties with you.{#ch11_o_001}"
    # JA[4511]: オスマン：学院には気軽に立ち寄られよ。一座のきれいどころもつれての。
    # [SPRITE lay7 hide]
    # [SPRITE lay20 image=+1063, level=160, dir=1A]
    # ウェザリー：け、検討しておきましょう。 [voice 16082]
    voice "ch11_w_002"
    w "W-we'll consider it.{#ch11_w_002}"
    # JA[16082]: ウェザリー：け、検討しておきましょう。
    # [SPRITE lay10 image=+926, level=160, dir=1A]
    # オスマン：くれぐれもきれいどころでの。 [voice 4512]
    voice "ch11_o_002"
    o "Make sure it's the beauties.{#ch11_o_002}"
    # JA[4512]: オスマン：くれぐれもきれいどころでの。
    # ウェザリー：……。 [voice 16083]
    voice "ch11_w_003"
    w "…{#ch11_w_003}"
    # JA[16083]: ウェザリー：…。
    # [SPRITE lay10 hide] [SPRITE lay20 hide]
    # [SPRITE lay7 image=+951, level=160, dir=1A] [SPRITE lay5 image=+390, level=160, dir=1A]
    # サイト：春奈……。 [voice 13242]
    voice "ch11_s_030"
    s "Haruna…{#ch11_s_030}"
    # JA[13242]: サイト：春奈…。
    # サイト：日本に戻る方法が見つかったら / すぐ連絡をとるから……。 [voice 13243]
    voice "ch11_s_031"
    s "If I find a way back to Japan / I'll contact you right away…{#ch11_s_031}"
    # JA[13243]: サイト：日本に戻る方法が見つかったらすぐ連絡をとるから…。
    # ハルナ：うん、私も。 / 旅の暮らしになると、いろんな土地に / 行くと思うし……ね。 [voice 2582]
    voice "ch11_ha_024"
    ha "Yeah, me too. / With a traveling life, I'll visit many places / so…{#ch11_ha_024}"
    # JA[2582]: ハルナ：うん、私も。旅の暮らしになると、いろんな土地に行くと思うし…ね。
    # [SPRITE lay5 hide]
    # [SPRITE lay6 image=+715, level=160, dir=2A]
    # キュルケ：……。 [voice 3814]
    voice "ch11_k_001"
    k "…{#ch11_k_001}"
    # JA[3814]: キュルケ：…。
    # キュルケ：ねえ、ハルナ……。 / ちょっとだけいい？ [voice 3815]
    voice "ch11_k_002"
    k "Hey, Haruna… / Just a moment?{#ch11_k_002}"
    # JA[3815]: キュルケ：ねえ、ハルナ…。ちょっとだけいい？
    # [BGM bgm stop=1000]
    stop music fadeout 1.0
    # [SPRITE lay7 hide] [SPRITE lay6 hide] [BG stage hide]
    # [BG stage image=+23, level=200] [TRANS 1000]
    $ fade_fx("classroom")
    # [SPRITE lay7 image=+955, level=160, dir=1A] [SPRITE lay6 image=+682, level=160, dir=1A]
    # [BGM bgm play=+28 → t27]
    play music t27 fadein 1.0
    # ハルナ：キュルケさん、そんなにひっぱらないで / ください。 [voice 2583]
    voice "ch11_ha_025"
    ha "Kirche-san, please don't pull me so hard.{#ch11_ha_025}"
    # JA[2583]: ハルナ：キュルケさん、そんなにひっぱらないでください。
    # キュルケ：ウェザリーに気を許してはだめよ。 [voice 3816]
    voice "ch11_k_003"
    k "Don't let your guard down with Weatherly.{#ch11_k_003}"
    # JA[3816]: キュルケ：ウェザリーに気を許してはだめよ。
    # [SPRITE lay7 image=+957, level=160, dir=1A]
    # ハルナ：えっ、それはどういう？ [voice 2584]
    voice "ch11_ha_026"
    ha "Eh, what do you mean?{#ch11_ha_026}"
    # JA[2584]: ハルナ：えっ、それはどういう？
    # [SPRITE lay6 image=+713, level=160, dir=2A]
    # キュルケ：しっ！ / 証拠はないの。 [voice 3817]
    voice "ch11_k_004"
    k "Shh! / There's no proof.{#ch11_k_004}"
    # JA[3817]: キュルケ：しっ！証拠はないの。
    # [SPRITE lay6 image=+711, level=160, dir=2A]
    # キュルケ：まあ、女の子の旅暮らしへの注意って / とこかしら。 / とにかくいいわね？ [voice 3818]
    voice "ch11_k_005"
    k "Well, consider it advice for a girl's traveling life. / Anyway, got it?{#ch11_k_005}"
    # JA[3818]: キュルケ：まあ、女の子の旅暮らしへの注意ってとこかしら。とにかくいいわね？
    # ハルナ：は、はい。 [voice 2585]
    voice "ch11_ha_027"
    ha "Y-yes.{#ch11_ha_027}"
    # JA[2585]: ハルナ：は、はい。
    # [BGM bgm stop=1000]
    stop music fadeout 1.0
    # [SPRITE lay7 hide] [SPRITE lay6 hide] [BG stage hide]
    # [BG stage image=+26, level=200] [TRANS 1000]
    $ fade_fx("yard")
    # [SPRITE lay7 image=+957, level=160, dir=1A] [SPRITE lay20 image=+1061, level=160, dir=1A]
    # [BGM bgm play=+19 → t18]
    play music t18 fadein 1.0
    # ウェザリー：じゃあ、そろそろ……。 [voice 16084]
    voice "ch11_w_004"
    w "Well then, it's about time…{#ch11_w_004}"
    # JA[16084]: ウェザリー：じゃあ、そろそろ…。
    # ハルナ：……。 (no voice)
    # サイト：（どうしたんだろう？ / 　春奈の顔色が悪いみたいだけど） (no voice)
    # 【選択肢】じゃあ、頑張ってな → scene 474
    # 【選択肢】手紙書くよ → scene 475
    # 【選択肢】大丈夫、また会えるさ → scene 476
    menu:
        "Then, do your best.":
            jump ch11_2_scene_474
        "I'll write letters.":
            jump ch11_2_scene_475
        "It's okay, we'll meet again.":
            jump ch11_2_scene_476

label ch11_2_scene_474:
    # ==== SCENE 474 ====
    # [SPRITE lay20 image=+1061, level=160, dir=1A]
    # [SPRITE lay7 image=+957, level=160, dir=1A]
    # [BGM bgm play=+19 → t18]
    play music t18 fadein 1.0
    # [BG stage image=+26, level=200]
    $ fade_fx("yard")
    # [SPRITE lay20 hide]
    # [SPRITE lay5 image=+390, level=160, dir=1A]
    # サイト：じゃあ、頑張ってな。 [voice 13244]
    voice "ch11_s_032"
    s "Then, do your best.{#ch11_s_032}"
    # JA[13244]: サイト：じゃあ、頑張ってな。
    # [SPRITE lay7 image=+953, level=160, dir=1A]
    # ハルナ：うん……。 / 約束する。 / じゃあね、バイバイ。 [voice 2586]
    voice "ch11_ha_028"
    ha "Yeah… / I promise. / Well then, bye-bye.{#ch11_ha_028}"
    # JA[2586]: ハルナ：うん…。約束する。じゃあね、バイバイ。
    # [SPRITE lay7 hide] [SPRITE lay5 hide]
    # → next scene 477
    jump ch11_2_scene_477

label ch11_2_scene_475:
    # ==== SCENE 475 ====
    # [SPRITE lay20 image=+1061, level=160, dir=1A]
    # [SPRITE lay7 image=+957, level=160, dir=1A]
    # [BGM bgm play=+19 → t18]
    play music t18 fadein 1.0
    # [BG stage image=+26, level=200]
    $ fade_fx("yard")
    # [SPRITE lay20 hide]
    # [SPRITE lay5 image=+390, level=160, dir=1A]
    # サイト：手紙、書くよ。 [voice 13245]
    voice "ch11_s_033"
    s "I'll write letters.{#ch11_s_033}"
    # JA[13245]: サイト：手紙、書くよ。
    # [SPRITE lay7 image=+951, level=160, dir=1A]
    # ハルナ：うん、私も。 [voice 2587]
    voice "ch11_ha_029"
    ha "Yeah, me too.{#ch11_ha_029}"
    # JA[2587]: ハルナ：うん、私も。
    # [SPRITE lay5 image=+429, level=160, dir=2A]
    # サイト：あ、でも、こっちの文字分かんないんだった。 / 郵便の人にあて先とか分かるかな？ [voice 13246]
    voice "ch11_s_034"
    s "Ah, but I don't know the writing here. / Will the postman understand the address?{#ch11_s_034}"
    # JA[13246]: サイト：あ、でも、こっちの文字分かんないんだった。郵便の人にあて先とか分かるかな？
    # [SPRITE lay7 hide]
    # [SPRITE lay1 image=+341, level=160, dir=2A]
    # ルイズ：それくらいは、わたしが書いてあげるわよ。 [voice 7170]
    voice "ch11_l_011"
    l "That much, I'll write for you.{#ch11_l_011}"
    # JA[7170]: ルイズ：それくらいは、わたしが書いてあげるわよ。
    # [SPRITE lay5 image=+423, level=160, dir=2A]
    # サイト：ルイズ……。 / ありがとう。 [voice 13247]
    voice "ch11_s_035"
    s "Louise… / Thanks.{#ch11_s_035}"
    # JA[13247]: サイト：ルイズ…。ありがとう。
    # [SPRITE lay5 hide]
    # → next scene 477
    jump ch11_2_scene_477

label ch11_2_scene_476:
    # ==== SCENE 476 ====
    # [SPRITE lay20 image=+1061, level=160, dir=1A]
    # [SPRITE lay7 image=+957, level=160, dir=1A]
    # [BGM bgm play=+19 → t18]
    play music t18 fadein 1.0
    # [BG stage image=+26, level=200]
    $ fade_fx("yard")
    # [SPRITE lay20 hide]
    # [SPRITE lay5 image=+390, level=160, dir=1A]
    # サイト：大丈夫！ / また会えるさ。 [voice 13248]
    voice "ch11_s_036"
    s "It's okay! / We'll meet again.{#ch11_s_036}"
    # JA[13248]: サイト：大丈夫！また会えるさ。
    # [SPRITE lay7 image=+951, level=160, dir=1A]
    # ハルナ：そうね、そうだよね！ [voice 2588]
    voice "ch11_ha_030"
    ha "Right, that's true!{#ch11_ha_030}"
    # JA[2588]: ハルナ：そうね、そうだよね！
    # ハルナ：ピンチの時は助けてね。 / 平賀くん。 [voice 2589]
    voice "ch11_ha_031"
    ha "Help me if I'm in a pinch. / Hiragan-kun.{#ch11_ha_031}"
    # JA[2589]: ハルナ：ピンチの時は助けてね。平賀くん。
    # サイト：もちろんだって！ [voice 13249]
    voice "ch11_s_037"
    s "Of course!{#ch11_s_037}"
    # JA[13249]: サイト：もちろんだって！
    # [SPRITE lay7 hide] [SPRITE lay5 hide]
    # → next scene 477
    jump ch11_2_scene_477

label ch11_2_scene_477:
    # ==== SCENE 477 ====
    # [BGM bgm play=+19 → t18]
    play music t18 fadein 1.0
    # [BG stage image=+26, level=200]
    $ fade_fx("yard")
    # [SPRITE lay1 image=+306, level=160, dir=1A]
    # ルイズ：まったく、なにを雰囲気だしてるのかしら。 [voice 7171]
    voice "ch11_l_012"
    l "Honestly, what's with the atmosphere?{#ch11_l_012}"
    # JA[7171]: ルイズ：まったく、なにを雰囲気だしてるのかしら。
    # [SPRITE lay1 hide]
    # [SPRITE lay20 image=+1063, level=160, dir=1A]
    # ウェザリー：では、次の舞台でのハルナの活躍を楽しみに / しておいてください。 [voice 16085]
    voice "ch11_w_005"
    w "Well then, please look forward to Haruna's performance on the next stage.{#ch11_w_005}"
    # JA[16085]: ウェザリー：では、次の舞台でのハルナの活躍を楽しみにしておいてください。
    # [SPRITE lay20 hide]
    # [SPRITE lay6 image=+715, level=160, dir=2A]
    # キュルケ：……。 [no voice]
    # [SPRITE lay6 hide]
    # [SPRITE lay20 image=+1063, level=160, dir=1A]
    # ウェザリー：それでは、さらばです！ / 魔法学院の皆様。 [voice 16086]
    voice "ch11_w_006"
    w "Then, farewell! / Everyone of the Magic Academy.{#ch11_w_006}"
    # JA[16086]: ウェザリー：それでは、さらばです！魔法学院の皆様。
    # [SPRITE lay20 hide]
    # [SPRITE lay5 image=+429, level=160, dir=2A]
    # サイト：春奈……。 [voice 13250]
    voice "ch11_s_038"
    s "Haruna…{#ch11_s_038}"
    # JA[13250]: サイト：春奈…。
    # [SE se1 stop=1] [BGM bgm stop=1000] [SPRITE lay5 hide] [BG stage hide]
    # → next scene 478
    jump ch11_3

    # ==== КОНЕЦ ГЛАВЫ 11, ЧАСТИ 2 ====
    # Дальше — SCENE 478+ (scene 478: aftermath, scene 479/480/481: choices, etc.)