# Extra event chapter (chapter_91), all scenes.
# Источник: ps2_source/chapters/chapter_91.txt

label sp91_scene_1697:

label sp91_scene_1698:

label sp91_scene_1699:

    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ね、ねえ、サイト。おなか、空いてない？
    l "Hey, hey, Saito… aren't you hungry?{#sp91_s1699_003}"

    # えっ？な、なんだよ、いきなり。
    s "Huh? W-what's that for, all of a sudden?{#sp91_s1699_004}"

    # す・い・て・る・わ・よ・ね？
    l "You're hu-u-n-g-r-y, aren't you?{#sp91_s1699_005}"

    # あ……ええっと……。
    s "Ah… um…{#sp91_s1699_006}"

        "Yeah! I'm hungry, I'm hungry!!{#sp91_c_1699_1717}":
            jump sp91_scene_1717
        "Somehow, I'm starting to feel hungry.{#sp91_c_1699_1718}":
            jump sp91_scene_1718
        "Definitely not hungry.{#sp91_c_1699_1719}":
            jump sp91_scene_1719
label sp91_scene_1701:

    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ね、ねえ、サイト。アンタ、おなか空いてない？
    voice "sp91_s1701_003"
    l "Hey, hey, Saito. You're not hungry, are you?{#sp91_s1701_003}"

    # え？うーん、そうだなあ。
    voice "sp91_s1701_004"
    s "Huh? Yeah, now that you mention it.{#sp91_s1701_004}"

        "Well, maybe I am hungry.{#sp91_c_1701_1733}":
            jump sp91_scene_1733
        "Actually, I'm starving!!{#sp91_c_1701_1734}":
            jump sp91_scene_1734
        "Well then, that's settled.{#sp91_c_1701_1735}":
            jump sp91_scene_1735
label sp91_scene_1702:

    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ねえ、サイト。……本当に分からないの？
    voice "sp91_s1702_003"
    l "Hey, Saito… You really don't get it?{#sp91_s1702_003}"

    # ひゃ、ひゃぁっ！？
    voice "sp91_s1702_004"
    s "Hya, hyaaa!?{#sp91_s1702_004}"

    # （み、耳元にルイズの息がぁっ！）
    s "(M-my ear — Luise's breath is right there!){#sp91_s1702_005}"

    # （耳に息を吹きかけるなんて……、ど、どこでそんなテクニックを？）
    s "(Blowing into my ear like that… W-where did she learn such a technique?){#sp91_s1702_006}"

    # それとも、分からないふりをしてるの？
    voice "sp91_s1702_007"
    l "Or are you just pretending not to understand?{#sp91_s1702_007}"

    # え、あ、あのルイズ……さん？
    voice "sp91_s1702_008"
    s "Eh? A-ah, Luise… -san?{#sp91_s1702_008}"

    # 女の子の気持ちを……よ？
    voice "sp91_s1702_009"
    l "A girl's feelings… you know?{#sp91_s1702_009}"

        "W-what do you mean?{#sp91_c_1702_1741}":
            jump sp91_scene_1741
        "…I-I don't understand.{#sp91_c_1702_1742}":
            jump sp91_scene_1742
        "O-oh, the wolf-san inside me is…!{#sp91_c_1702_1743}":
            jump sp91_scene_1743
label sp91_scene_1703:

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ……ねえ、サイト？わたしと一緒にいるのはそんなにいや？
    voice "sp91_s1703_004"
    l "…Hey, Saito? Is being with me really that unpleasant?{#sp91_s1703_004}"

    # ……っ。
    voice "sp91_s1703_005"
    l "…!{#sp91_s1703_005}"

    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # ひ、ひぅっ！
    voice "sp91_s1703_007"
    s "H-hyuu!{#sp91_s1703_007}"

    # い、いきなり耳元に息をふきかけるんじゃねえっ！
    voice "sp91_s1703_008"
    s "D-don't go blowing into my ear out of nowhere like that!{#sp91_s1703_008}"

    # ……き、気持ち良かった？
    voice "sp91_s1703_009"
    l "…F-felt good, did it?{#sp91_s1703_009}"

        "It… might have felt good.{#sp91_c_1703_1749}":
            jump sp91_scene_1749
        "Where did you learn to do that!?{#sp91_c_1703_1750}":
            jump sp91_scene_1750
        "H-heh, stay calm! Stay calm!{#sp91_c_1703_1751}":
            jump sp91_scene_1751
label sp91_scene_1704:

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ……サ、サイトの馬鹿っ！どうしていつもそうなの？
    voice "sp91_s1704_004"
    l "…S-Saito, you idiot! Why are you always like that?{#sp91_s1704_004}"

    # い、いや、あのルイズ……？
    voice "sp91_s1704_005"
    s "N-no, I… Luise…?{#sp91_s1704_005}"

    # わ、わたしのこと……嫌い？
    voice "sp91_s1704_006"
    l "D-do you… hate me?{#sp91_s1704_006}"

    # い、いやそんな。嫌いってわけじゃ。
    voice "sp91_s1704_007"
    s "N-no, not at all. I don't hate you.{#sp91_s1704_007}"

    # だったら何故いつも意地悪するの？
    voice "sp91_s1704_008"
    l "Then why are you always so mean?{#sp91_s1704_008}"

    # い、いや別に意地悪なんて……。
    voice "sp91_s1704_009"
    s "N-no, I'm not trying to be mean or anything…{#sp91_s1704_009}"

    # （ルイズの体温と重みが背中に……）【選択肢】た、助けて！ → scene 1757【選択肢】俺の心の狼さんが…
    s "(Luise's warmth and weight against my back…) H-help me! → scene 1757 The wolf-san inside me is… → scene 1758 S-soft… → scene 1759{#sp91_s1704_010}"

label sp91_scene_1705:

    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ほんとに、もうっ！
    voice "sp91_s1705_003"
    l "Honestly, really now!{#sp91_s1705_003}"

    # 今日はどこにも行かないで、わたしと一緒にいなさいっ！
    voice "sp91_s1705_004"
    l "Don't go anywhere today — stay with me!{#sp91_s1705_004}"

    # ……は、はぁい。
    voice "sp91_s1705_005"
    s "…Y-yes!{#sp91_s1705_005}"

    # な、なによ。その態度！
    voice "sp91_s1705_006"
    l "W-what's with that attitude!?{#sp91_s1705_006}"

    # わ、わたしと一緒じゃ不満なの？
    voice "sp91_s1705_007"
    l "A-are you unhappy being with me?{#sp91_s1705_007}"

    # ……い、いえとんでもない！ご一緒できて光栄でありますっ！
    voice "sp91_s1705_008"
    s "…N-no, certainly not! It's an honor to be with you!{#sp91_s1705_008}"

    # もうっ！だったら最初からそう言いなさい！
    voice "sp91_s1705_009"
    l "Honestly! Then say so from the start!{#sp91_s1705_009}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # ………。……。…。
    th "………{#sp91_s1705_015}"

    # はぁ～～～～っ！
    voice "sp91_s1705_016"
    s "Haaaaah!{#sp91_s1705_016}"

    # ……スゥスゥ。
    voice "sp91_s1705_017"
    l "…Suu suu.{#sp91_s1705_017}"

    # （本人はとっとと寝ちゃうし……。俺は緊張しちゃってるっていうのに……）【選択肢】寝顔はホントかわいいよな → 
    s "(She just goes right to sleep… and here I am all tense…) Her sleeping face really is cute, isn't it → scene 1765 Wicked thoughts are… → scene 1766 …Oh, maybe I should sleep too → scene 1767{#sp91_s1705_018}"

label sp91_scene_1706:

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ……外出禁止よ！
    voice "sp91_s1706_004"
    l "…You're not allowed out!{#sp91_s1706_004}"

    # 今日はどこにも行かず、わたしと一緒にいなさいっ！
    voice "sp91_s1706_005"
    l "Don't go anywhere today — stay with me!{#sp91_s1706_005}"

    # そ、そんな横暴な……。
    voice "sp91_s1706_006"
    s "T-that's awfully high-handed…{#sp91_s1706_006}"

    # なにか不満でも？
    voice "sp91_s1706_007"
    l "Something bothering you?{#sp91_s1706_007}"

    # ……い、いいえ。お付き合いしますです。
    voice "sp91_s1706_008"
    s "…N-no. I'll be happy to keep you company.{#sp91_s1706_008}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # ………。……。…。[EVENT_CG event    image=+185, level=80][TRANS
    th "…{#sp91_s1706_012}"

    # （……はぁ。結局、ルイズは一日べったりだったし）
    s "(Hah. In the end, Luise stuck to me all day.){#sp91_s1706_013}"

    # ……ねぇ、サイト……起きてる？
    voice "sp91_s1706_014"
    l "…Hey, Saito… are you awake?{#sp91_s1706_014}"

    # お、起きてるけど？
    voice "sp91_s1706_015"
    s "H-huh? I'm awake, though.{#sp91_s1706_015}"

    # ……あの、腕枕……してくれる？
    voice "sp91_s1706_016"
    l "…Um, would you let me rest my head on your arm?{#sp91_s1706_016}"

    # え？ええと。
    voice "sp91_s1706_017"
    s "Huh? Um…{#sp91_s1706_017}"

        "I-it's fine, I guess?{#sp91_c_1706_1773}":
            jump sp91_scene_1773
        "W-wait a sec!{#sp91_c_1706_1774}":
            jump sp91_scene_1774
        "Refuse!{#sp91_c_1706_1775}":
            jump sp91_scene_1775
label sp91_scene_1707:

    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ……サイトはわたしの使い魔よね？
    voice "sp91_s1707_003"
    l "…You're my familiar, Saito, right?{#sp91_s1707_003}"

    # だったら、これは命令よ！今日は一日わたしと一緒にいなさい！……め、命令なんだからね！
    voice "sp91_s1707_004"
    l "Then this is an order! Stay with me all day today! …B-because it's an order, okay?!{#sp91_s1707_004}"

    # そ、そりゃいいけど。
    voice "sp91_s1707_005"
    s "T-that's fine and all, but…{#sp91_s1707_005}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # ………。……。…。[EVENT_CG event    image=+185, level=80][TRANS
    th "…{#sp91_s1707_009}"

    # な、なあ。ルイズ。
    voice "sp91_s1707_010"
    s "H-hey. Luise.{#sp91_s1707_010}"

    # ……な、なによ。
    voice "sp91_s1707_011"
    l "…W-what is it?{#sp91_s1707_011}"

    # ちょっと、くっつきすぎじゃありませんか？
    voice "sp91_s1707_012"
    s "Aren't we a little too close right now?{#sp91_s1707_012}"

    # い、いいじゃない。
    voice "sp91_s1707_013"
    l "I-it's fine, I don't mind.{#sp91_s1707_013}"

    # （今日は一日中べたべたしてた気がするのにまだ足りないっていうのかよ……）
    s "(Feels like she's been glued to me all day, and it's still not enough…){#sp91_s1707_014}"

    # （で、でもそれにしても……）
    s "(A-and even so…){#sp91_s1707_015}"

    # （……女の子の体って、暖かくてやわらかいなぁ。……それにいい匂いが……）
    s "(A girl's body is so warm and soft… And she smells so good, too…){#sp91_s1707_016}"

    # ……って、何考えてんだよ俺！
    voice "sp91_s1707_017"
    s "…Hey, what am I even thinking?!{#sp91_s1707_017}"

    # もうっ、どうしたのよ？
    voice "sp91_s1707_018"
    l "Honestly, what's wrong with you?{#sp91_s1707_018}"

    # ええと、いやその……。
    voice "sp91_s1707_019"
    s "Um, no, I mean…{#sp91_s1707_019}"

        "Honestly…{#sp91_c_1707_1781}":
            jump sp91_scene_1781
        "Try teasing her?{#sp91_c_1707_1782}":
            jump sp91_scene_1782
        "Laugh it off.{#sp91_c_1707_1783}":
            jump sp91_scene_1783
label sp91_scene_1708:

    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ……ねえ、サイト。あなた、お風呂が好きだったわよね。
    voice "sp91_s1708_003"
    l "…Hey, Saito. You used to like baths, didn't you?{#sp91_s1708_003}"

    # へっ？ええ、まあ……。
    voice "sp91_s1708_004"
    s "Huh? Yeah, well…{#sp91_s1708_004}"

    # といっても、俺の故郷じゃ普通っていうか、人並み程度ですけど……。
    voice "sp91_s1708_005"
    s "I mean, back home it's pretty common — average, really…{#sp91_s1708_005}"

    # ……そう。いいわ。
    voice "sp91_s1708_006"
    l "…I see. Fine.{#sp91_s1708_006}"

    # じゃあ、わたしが背中を洗ってあげる。
    voice "sp91_s1708_007"
    l "Then I'll wash your back.{#sp91_s1708_007}"

    # ……へ？
    voice "sp91_s1708_008"
    s "…Huh?{#sp91_s1708_008}"

    # な、なによ！わたしが洗ってあげるっていうんじゃ不満なの！？
    voice "sp91_s1708_009"
    l "W-what!? You're not happy that I'm the one washing you!?{#sp91_s1708_009}"

        "T-that's going a bit far, don't you think…?{#sp91_c_1708_1789}":
            jump sp91_scene_1789
        "It makes me happy, but…{#sp91_c_1708_1790}":
            jump sp91_scene_1790
        "Then, please do.{#sp91_c_1708_1791}":
            jump sp91_scene_1791
label sp91_scene_1709:

    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # 今日も、サイトのことお風呂で洗ってあげる。早く付いて来なさい。
    voice "sp91_s1709_003"
    l "Today too, I'm going to wash you in the bath. Hurry up and follow me.{#sp91_s1709_003}"

    # ……へっ？……え、ええっ！？
    voice "sp91_s1709_004"
    s "…Huh? …E-eh!?{#sp91_s1709_004}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # ………。……。…。[EVENT_CG event    image=+187, level=80][TRANS
    th "…{#sp91_s1709_008}"

    # さぁ、洗ってあげるわよ。早く背中向けなさい！
    voice "sp91_s1709_009"
    l "Come on, I'll wash you. Turn your back to me, quickly!{#sp91_s1709_009}"

    # （ルイズと一緒にお風呂なんて……）【選択肢】落ち着かない → scene 1797【選択肢】不気味で怖い！ →
    s "(Bathing with Luise, huh…) Can't calm down → scene 1797 It's creepy and scary! → scene 1798 I could dance with excitement! → scene 1799{#sp91_s1709_010}"

label sp91_scene_1710:

    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ……サ、サイトの馬鹿っ！イジワル！他の女の子がそんなにいいの！！
    voice "sp91_s1710_003"
    l "…S-Saito, you idiot! So mean! Are other girls really that good!?{#sp91_s1710_003}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     hide, vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [EVENT_CG event    hide]
    # [TRANS trans("crossfade", 1000)]
    # ぐはぁぁぁっ！
    voice "sp91_s1710_017"
    s "Guhaaaah!{#sp91_s1710_017}"

    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # い、いや、勘違いだと思うし、俺、そんなにフラフラしてないし。ご主人様一直線ですよ？
    voice "sp91_s1710_020"
    s "N-no, I think that's a misunderstanding. I'm not flirting around that much. I only have eyes for my master, okay?{#sp91_s1710_020}"

    # なら、他の女の子を見たりしない？
    voice "sp91_s1710_021"
    l "Then you won't look at other girls?{#sp91_s1710_021}"

    # え、ええと。
    voice "sp91_s1710_022"
    s "Eh, um…{#sp91_s1710_022}"

        "O-of course!{#sp91_c_1710_1805}":
            jump sp91_scene_1805
        "I'll handle it constructively.{#sp91_c_1710_1806}":
            jump sp91_scene_1806
        "M-maybe it's impossible, though?{#sp91_c_1710_1807}":
            jump sp91_scene_1807
label sp91_scene_1711:

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # サイト！
    voice "sp91_s1711_003"
    l "Saito!{#sp91_s1711_003}"

    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # な、どうしたんだよ。いきなり俺のこと押し倒して！
    voice "sp91_s1711_005"
    s "W-what's wrong? Pushing me down out of nowhere!{#sp91_s1711_005}"

    # ねえ、サイト。わたしのことをどう思ってる？
    voice "sp91_s1711_006"
    l "Hey, Saito. What do you think of me?{#sp91_s1711_006}"

    # わたしって他の女の子にくらべてそんなに魅力がない？
    voice "sp91_s1711_007"
    l "Am I really that unattractive compared to other girls?{#sp91_s1711_007}"

    # ど、どうしたんだよ、急に。普段はあんなに自信家のくせに。
    voice "sp91_s1711_008"
    s "W-what's with you, all of a sudden? You're usually so confident.{#sp91_s1711_008}"

    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # さ、サイトが悪いんじゃない！あっちの女の子にふらふら、こっちの女の子にふらふら……。
    voice "sp91_s1711_010"
    l "It's Saito's fault! Drifting to that girl, drifting to this girl…{#sp91_s1711_010}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ねぇ？サイトから見て、わたしってかわいい？
    voice "sp91_s1711_012"
    l "Hey? From your point of view, am I cute?{#sp91_s1711_012}"

        "Luise is cute.{#sp91_c_1711_1813}":
            jump sp91_scene_1813
        "Luise is cute too.{#sp91_c_1711_1814}":
            jump sp91_scene_1814
        "But, she's flat-chested…{#sp91_c_1711_1815}":
            jump sp91_scene_1815
label sp91_scene_1712:

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ……ねえ、サイト。
    voice "sp91_s1712_003"
    l "……Hey, Saito.{#sp91_s1712_003}"

    # なんというか……その……、あ、あなたには愛情がたりないわ！
    voice "sp91_s1712_004"
    l "How should I put it… that… Ah, you're just not affectionate enough!{#sp91_s1712_004}"

    # ……あ、愛情？
    voice "sp91_s1712_005"
    s "……Huh? Affection?{#sp91_s1712_005}"

    # え、ええと？それは……。つまり、俺にいったいどうしろと？
    voice "sp91_s1712_006"
    s "E-Erm? That's… So what exactly do you want me to do?{#sp91_s1712_006}"

    # な、なによ！そんなことも分からないの！
    voice "sp91_s1712_007"
    l "W-What?! You can't even figure that out?!{#sp91_s1712_007}"

    # 乙女には花束と愛と情熱に満ちた言葉が必要なのよ！
    voice "sp91_s1712_008"
    l "A maiden needs flowers, love, and words brimming with passion!{#sp91_s1712_008}"

    # （……ホントかよ）
    s "(……Really?){#sp91_s1712_009}"

    # あんたも『ルイズ様の愛のしもべ』ぐらいは言ったらどうなの？
    voice "sp91_s1712_010"
    l "Why don't you say something like 'Louise-sama's servant of love'?{#sp91_s1712_010}"

    # あ、いや、恥ずかしいし……。
    voice "sp91_s1712_011"
    s "Ah, no, it's embarrassing…{#sp91_s1712_011}"

    # ……特訓、ね。
    voice "sp91_s1712_012"
    l "…Special training, is it?{#sp91_s1712_012}"

    # へっ？
    voice "sp91_s1712_013"
    s "Huh?{#sp91_s1712_013}"

    # そんなことだから乙女心が分からないのよ！バカ犬！
    voice "sp91_s1712_014"
    l "That's why you don't understand a maiden's heart! Stupid dog!{#sp91_s1712_014}"

    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # このわたしが徹底的に愛と情熱というものを叩き込んであげる！
    voice "sp91_s1712_016"
    l "I'll drill love and passion into you, thoroughly!{#sp91_s1712_016}"

        "……Eh, I'll pass.{#sp91_c_1712_1821}":
            jump sp91_scene_1821
        "Ah, love and passion, you say…?{#sp91_c_1712_1822}":
            jump sp91_scene_1822
        "Should I do it like Gishe?{#sp91_c_1712_1823}":
            jump sp91_scene_1823
label sp91_scene_1713:

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ……ねぇ、サイト。あなた、わたしのことをどう思ってるの？
    voice "sp91_s1713_003"
    l "……Say, Saito. What do you think of me?{#sp91_s1713_003}"

    # ……へっ？
    voice "sp91_s1713_004"
    s "……Huh?{#sp91_s1713_004}"

    # ちゃんとわたしのこと気にかけてる？
    voice "sp91_s1713_005"
    l "Do you really care about me?{#sp91_s1713_005}"

    # ……え、ええと？
    voice "sp91_s1713_006"
    s "……E-Erm?{#sp91_s1713_006}"

        "I care about you.{#sp91_c_1713_1829}":
            jump sp91_scene_1829
        "Maybe I do…?{#sp91_c_1713_1830}":
            jump sp91_scene_1830
        "What's that even supposed to mean?{#sp91_c_1713_1831}":
            jump sp91_scene_1831
label sp91_scene_1714:

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ……いいわよ！罰ゲームよ！
    voice "sp91_s1714_004"
    l "……Fine! It's a punishment game!{#sp91_s1714_004}"

    # ええっ！ま、また何かむごいことを？
    voice "sp91_s1714_005"
    s "Eh!? Are you up to something cruel again?{#sp91_s1714_005}"

    # もうっ、違うわよ！
    voice "sp91_s1714_006"
    l "No, that's not it!{#sp91_s1714_006}"

    # さ、サイトは見たことないでしょうけど、この世界にはティモシュっていうこういうお菓子があるの。
    voice "sp91_s1714_007"
    l "Now, you've probably never seen these, Saito, but in this world there's a candy called Timoshu.{#sp91_s1714_007}"

    # は、はあ……。
    voice "sp91_s1714_008"
    s "Ha… ah…{#sp91_s1714_008}"

    # （これ、ポッチーだろ。いや、チョコがないからプリッチか？）
    s "(This is Pocchi, right? No, there's no chocolate, so it's Puritchi?){#sp91_s1714_009}"

    # （この世界でもあるんだ。こういうお菓子）
    s "(They have these snacks in this world too.){#sp91_s1714_010}"

    # これは、その。ちょっと変わった食べ方をするお菓子なの。
    voice "sp91_s1714_011"
    l "It's, um, a candy you eat in a rather unusual way.{#sp91_s1714_011}"

    # て、手を使わずに食べるのよ！
    voice "sp91_s1714_012"
    l "You eat it without using your hands!{#sp91_s1714_012}"

    # ……って、えっ？
    voice "sp91_s1714_013"
    s "…Wait, eh?{#sp91_s1714_013}"

    # あの、ルイズ。手を使わずに食べるって、まさか……。
    voice "sp91_s1714_014"
    s "Um, Louise. Eat it without using our hands… surely you don't mean…{#sp91_s1714_014}"

        "…That thing couples do?{#sp91_c_1714_1837}":
            jump sp91_scene_1837
        "How, exactly?{#sp91_c_1714_1838}":
            jump sp91_scene_1838
        "…With our feet?{#sp91_c_1714_1839}":
            jump sp91_scene_1839
label sp91_scene_1715:

    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ……ねぇ、サイト？ちょっとゲームをしない？
    voice "sp91_s1715_003"
    l "……Say, Saito? Wanna play a little game?{#sp91_s1715_003}"

    # へっ、またですか？
    voice "sp91_s1715_004"
    s "Huh? Again?{#sp91_s1715_004}"

    # え、ええ。そうよ。
    voice "sp91_s1715_005"
    l "Y-Yes. That's right.{#sp91_s1715_005}"

    # わたしがこっちの端を咥えて、サイトがそっちから……食べるんだからね。
    voice "sp91_s1715_006"
    l "I'll bite this end, and you bite from that end… and we eat it, okay?{#sp91_s1715_006}"

    # さ、さあ、サイト。どうするの？
    voice "sp91_s1715_007"
    l "W-Well, Saito? What'll it be?{#sp91_s1715_007}"

        "What happens if we eat it all the way?{#sp91_c_1715_1845}":
            jump sp91_scene_1845
        "G-Gladly!{#sp91_c_1715_1846}":
            jump sp91_scene_1846
        "P-Please, spare me.{#sp91_c_1715_1847}":
            jump sp91_scene_1847
label sp91_scene_1716:

    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ……もういいわ！今日はわたしに付き合いなさい！
    voice "sp91_s1716_003"
    l "……Enough! Today you're keeping me company!{#sp91_s1716_003}"

    # な、なんだよっ！急に！
    voice "sp91_s1716_004"
    s "W-What's with you all of a sudden?!{#sp91_s1716_004}"

    # ティータイムにしましょう！
    voice "sp91_s1716_005"
    l "Let's have teatime!{#sp91_s1716_005}"

    # なあ、ルイズ。また、アレやるのか？
    voice "sp91_s1716_006"
    s "Say, Louise. Are we doing that again?{#sp91_s1716_006}"

    # うふふ、そうよ！今回こそ、折らないように食べるんだからね！
    voice "sp91_s1716_007"
    l "Hehe, that's right! This time, eat it without breaking it, okay!{#sp91_s1716_007}"

    # なんというか、その。……本気？
    voice "sp91_s1716_008"
    s "How should I put it… You're serious?{#sp91_s1716_008}"

    # な、なによ！それ！あたりまえじゃない！
    voice "sp91_s1716_009"
    l "W-What's that supposed to mean! Of course I am!{#sp91_s1716_009}"

    # え、えーと、あの……。
    voice "sp91_s1716_010"
    s "E-Erm, um…{#sp91_s1716_010}"

        "It's a bit embarrassing, don't you think?{#sp91_c_1716_1853}":
            jump sp91_scene_1853
        "And if it works out?{#sp91_c_1716_1854}":
            jump sp91_scene_1854
        "……M-Marvelous.{#sp91_c_1716_1855}":
            jump sp91_scene_1855
label sp91_scene_1717:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [SPRITE   lay5     hide]
    # うん！空いてる空いてる！！
    s "Yeah! Hungry, starving!!{#sp91_s1717_003}"

    # （なんかよく分かんないけど……ここはご機嫌とっとくべきだよな）
    s "(I don't really get what's going on… but I should keep her in a good mood.){#sp91_s1717_004}"

    # もう俺、腹ぺこぺこ！！
    s "I'm absolutely starving!!{#sp91_s1717_005}"

    # そう。良かった。
    l "I see. Good.{#sp91_s1717_006}"

    # 良かった？
    s "Good?{#sp91_s1717_007}"

    # あ、ううん。なんでもないの。
    l "Ah, no. It's nothing.{#sp91_s1717_008}"

    # → next scene 1720
    jump sp91_scene_1720

label sp91_scene_1718:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [SPRITE   lay5     hide]
    # なんか、空いてる気がしてきた。
    s "Somehow, I'm starting to feel hungry.{#sp91_s1718_003}"

    # （ここは逆らわない方が良さそうだ。怒らせるとやっかいだし）
    s "(Best not to argue with her here. She's a handful when she's angry.){#sp91_s1718_004}"

    # うん、そうよね。使い魔だからって、遠慮することはないのよ。
    l "Mm, that's right. Just because you're my familiar doesn't mean you have to hold back.{#sp91_s1718_005}"

    # → next scene 1720
    jump sp91_scene_1720

label sp91_scene_1719:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # 断固空いてない。
    s "Absolutely not hungry.{#sp91_s1719_002}"

    # （ここで負けてなるものかっ！）
    s "(I won't lose here!){#sp91_s1719_003}"

    # 全然！全く！完璧に！！
    s "Not at all! Not a bit! Perfectly!!{#sp91_s1719_004}"

    # （俺は断固として自分の意志を……）
    s "(I will firmly stick to my own will…){#sp91_s1719_005}"

    # ……。
    l "……{#sp91_s1719_006}"

    # （って、なんか怒ってるし！！）
    s "(Wait, she's getting angry!!){#sp91_s1719_007}"

    # あ、いや……。やっぱり……空いてるかも……。
    s "Ah, no… Actually… maybe I am hungry…{#sp91_s1719_008}"

    # ホント？
    l "Really?{#sp91_s1719_009}"

    # う、うん。ホントホント。あー、腹減ったなぁ！！
    s "Y-Yeah. Really, really. Man, I'm hungry!!{#sp91_s1719_010}"

    # 良かった。
    l "Good.{#sp91_s1719_011}"

    # へっ？良かったって？何が？
    s "Huh? Good? What's good?{#sp91_s1719_012}"

    # → next scene 1720
    jump sp91_scene_1720

label sp91_scene_1720:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # じゃあ、今から食堂に行きましょう！
    l "Then let's go to the cafeteria now!{#sp91_s1720_002}"

    # へっ？
    s "Huh?{#sp91_s1720_003}"

    # ほらっ、早く！行くわよっ！
    l "Come on, hurry! Let's go!{#sp91_s1720_004}"

    # お、おいおい。なんだよ、急に……。
    s "H-Hey now. What's gotten into you…?{#sp91_s1720_005}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # ほら……食べなさいよ。
    l "Here… eat it.{#sp91_s1720_013}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # へっ？なにこれ？
    s "Huh? What's this?{#sp91_s1720_015}"

    # 何って、シチューよ。これが本に見える？
    l "What do you mean, it's stew. Does this look like a book to you?{#sp91_s1720_016}"

    # いや、見えないけど。
    s "No, it doesn't.{#sp91_s1720_017}"

    # でも、どうして？
    s "But why?{#sp91_s1720_018}"

    # （シチューだよな……。どうして俺に？）[SPRITE   lay1     image=+306, level
    s "(It's stew, right…? Why is she giving it to me?){#sp91_s1720_019}"

    # あ……え、えっと、か、勘違いしないでよね！
    l "Ah… um, don't get the wrong idea, okay?!{#sp91_s1720_020}"

    # 別にあんたに食べさせようってだけで用意したわけじゃないんだから！！
    l "I didn't prepare it just to feed you or anything!!{#sp91_s1720_021}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # た、ただ、その……。
    l "I-It's just, well…{#sp91_s1720_023}"

    # ？
    s "?{#sp91_s1720_024}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # そ、そう！余っちゃったからっ！
    l "T-That's it! I made too much!{#sp91_s1720_026}"

    # あ……うん。分かった分かった。別にそんな、怒んなくても。
    s "Ah… yeah. Got it, got it. You don't have to get mad about it.{#sp91_s1720_027}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # べ、別に怒ってはないけど。それで……どう？食べる？
    l "I-I'm not mad or anything. So…? Will you eat it?{#sp91_s1720_029}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # あ、うん。もらう。美味そうだし。
    s "Ah, yeah. I'll take it. It looks delicious.{#sp91_s1720_031}"

    # [SPRITE   lay1     image=+337, level=160, dir=2A]
    # そ、それじゃあ。
    l "T-Then…{#sp91_s1720_033}"

    # うん。スプーンを。
    s "Yeah. The spoon.{#sp91_s1720_034}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # [TRANS trans("crossfade", 1000)]
    # はい、あーん。
    l "Here, say 'ahh'.{#sp91_s1720_040}"

    # ……は？
    s "……Huh?{#sp91_s1720_041}"

    # だから、あーん。
    l "I said, say 'ahh'.{#sp91_s1720_042}"

    # ……。
    s "……{#sp91_s1720_043}"

        "What punishment game is this?{#sp91_c_1720_1721}":
            jump sp91_scene_1721
        "Is there poison in this?{#sp91_c_1720_1722}":
            jump sp91_scene_1722
        "'Ahh'.{#sp91_c_1720_1723}":
            jump sp91_scene_1723
label sp91_scene_1721:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # 何の罰ゲーム？
    s "What punishment game is this?{#sp91_s1721_002}"

    # [EVENT_CG event    image=+181, level=80]
    $ dissolve_fx("id(181)")
    # な、なによそれっ！
    l "W-What's that supposed to mean!{#sp91_s1721_004}"

    # いや、だから、キュルケと賭けでもして負けたとか。
    s "No, I mean, did you bet with Kirche and lose or something?{#sp91_s1721_005}"

    # そんなことしないわよっ！馬鹿っ！いいから食べなさいっっ！！
    l "I would never do that! Idiot! Just eat it!!{#sp91_s1721_006}"

    # お、怒んなくてもいいだろ。
    s "Y-You don't have to get mad, you know.{#sp91_s1721_007}"

    # ほらっ！あーんっ！
    l "Come on! Say 'ahh'!{#sp91_s1721_008}"

    # あ、あーん……。
    s "A-Ahh…{#sp91_s1721_009}"

    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # → next scene 1724
    jump sp91_scene_1724

label sp91_scene_1722:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # これ、毒でも入ってる？
    s "Is there poison in this?{#sp91_s1722_002}"

    # [EVENT_CG event    image=+181, level=80]
    $ dissolve_fx("id(181)")
    # な、なんてこと言うのよっ！わたしがそんなことするわけないでしょっ！？
    l "H-How can you say that!? I'd never do something like that!{#sp91_s1722_004}"

    # あ、い、いや、ごめん。冗談。
    s "Ah, I-I'm sorry. It was a joke.{#sp91_s1722_005}"

    # まったく、あんたってホント馬鹿。女心を分かってないんだから……。
    l "Honestly, you're such an idiot. You just don't understand a woman's heart…{#sp91_s1722_006}"

    # え？女心って？
    s "Huh? A woman's heart?{#sp91_s1722_007}"

    # なんでもないわよっ！いいから食べなさいっ！！
    l "It's nothing! Just eat it!!{#sp91_s1722_008}"

    # わ、分かったよ。
    s "I-I got it.{#sp91_s1722_009}"

    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # → next scene 1724
    jump sp91_scene_1724

label sp91_scene_1723:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # あーん。
    s "'Ahh'.{#sp91_s1723_002}"

    # （何たくらんでるのか知らないけど……、逆らわない方が身のためだよな）
    s "(I don't know what she's plotting… but it's in my best interest not to argue.){#sp91_s1723_003}"

    # あ、あら、今日は素直じゃない。いつもこうだったらいいのに。
    l "Oh, my, you're being obedient today. If only you were always like this.{#sp91_s1723_004}"

    # → next scene 1724
    jump sp91_scene_1724

label sp91_scene_1724:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # もぐもぐもぐ……。
    s "Munch munch munch…{#sp91_s1724_002}"

    # おいしい？
    l "Is it good?{#sp91_s1724_003}"

    # うん！美味い！！
    s "Yeah! It's delicious!!{#sp91_s1724_004}"

    # ホント！？
    l "Really!?{#sp91_s1724_005}"

    # いやー、やっぱ美味いよなあ、この食堂の料理！
    s "Man, the food in this cafeteria is always so good!{#sp91_s1724_006}"

    # [EVENT_CG event    image=+180, level=80]
    $ dissolve_fx("id(180)")
    # ……。
    l "……{#sp91_s1724_008}"

    # いやー、もう、俺のたったひとつの楽しみなんだよなあ、メシ喰うのはっ！！
    s "Seriously, eating is my one and only pleasure!!{#sp91_s1724_009}"

    # ……。
    l "……{#sp91_s1724_010}"

    # って……あれ？どうした？ルイズ？
    s "Wait… Huh? What's wrong, Louise?{#sp91_s1724_011}"

    # ……。
    l "……{#sp91_s1724_012}"

    # もしもーし。ルイズさーん。
    s "Hellooo. Louise-saaan.{#sp91_s1724_013}"

    # [EVENT_CG event    image=+181, level=80]
    $ dissolve_fx("id(181)")
    # ……なによ。
    l "……What?{#sp91_s1724_015}"

    # へ？
    s "Huh?{#sp91_s1724_016}"

    # なによなによっ！
    l "What, what!?{#sp91_s1724_017}"

    # いや……何が？
    s "No… what do you mean?{#sp91_s1724_018}"

    # どうせ……、どうせ、わたしなんてっっ！！
    l "It's not like… it's not like I matter or anything!!{#sp91_s1724_019}"

    # い、いや、だから、何が？
    s "N-No, I'm asking what's wrong?{#sp91_s1724_020}"

    # サイトのばかぁぁぁっ！！
    l "You stupid Saitooo!!{#sp91_s1724_021}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # あ……。行っちゃった。
    s "Ah… She left.{#sp91_s1724_028}"

    # （何怒ってるんだよ、変な奴……）[SE       se1      stop=1][BGM      bgm
    s "(Why is she so angry? She's such a weirdo…){#sp91_s1724_029}"

label sp91_scene_1733:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # まあ、空いてるかな。
    voice "sp91_s1733_002"
    s "Well, maybe it's not crowded.{#sp91_s1733_002}"

    # な、なによ、別に無理しなくたって、い、いいんだから。
    voice "sp91_s1733_003"
    l "N-No, it's fine. You don't have to force yourself, really.{#sp91_s1733_003}"

    # いや、別に無理はしてないし。
    voice "sp91_s1733_004"
    s "No, I'm not forcing myself.{#sp91_s1733_004}"

    # ……そう？
    voice "sp91_s1733_005"
    l "……Is that so?{#sp91_s1733_005}"

    # → next scene 1736
    jump sp91_scene_1736

label sp91_scene_1734:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # さすがご主人様！実はぺこぺこ！！
    voice "sp91_s1734_002"
    s "As expected of my Master! I'm starving!!{#sp91_s1734_002}"

    # あ、あら、そうだったの。それならそう言えば良かったのに……。
    voice "sp91_s1734_003"
    l "O-Oh, was that it? You should have said so sooner…{#sp91_s1734_003}"

    # いやあ、さすが思慮深いご主人様です。この使い魔めのことを、よく分かっておられる！
    voice "sp91_s1734_004"
    s "Nah, you're such a thoughtful Master. You understand your familiar so well!{#sp91_s1734_004}"

    # な、なによ。お、おだてたって、何も出ないんだから。
    voice "sp91_s1734_005"
    l "W-What are you… F-Flattery won't get you anything.{#sp91_s1734_005}"

    # いやいや、本心からでございます！
    voice "sp91_s1734_006"
    s "No, no, I mean it from the bottom of my heart!{#sp91_s1734_006}"

    # ま、まあ、いいわ。そ、そういうことにしておいてあげる。
    voice "sp91_s1734_007"
    l "F-Fine. I'll let you think that, then.{#sp91_s1734_007}"

    # → next scene 1736
    jump sp91_scene_1736

label sp91_scene_1735:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # じゃあ、そういうことで。
    voice "sp91_s1735_002"
    s "Well, that's settled, then.{#sp91_s1735_002}"

    # ちょ、ちょ、待ちなさいよっ！！
    voice "sp91_s1735_003"
    l "W-Wait a moment!!{#sp91_s1735_003}"

    # いや、だって、空いてないんだったらいいんだろ？
    voice "sp91_s1735_004"
    s "But, I mean, you said it was fine if I wasn't hungry, right?{#sp91_s1735_004}"

    # そ、それは……そうだけど……。それは言葉のアヤよ！
    voice "sp91_s1735_005"
    l "T-That's… well, yes, but… That's just a figure of speech!{#sp91_s1735_005}"

    # えー。
    voice "sp91_s1735_006"
    s "Eeeh.{#sp91_s1735_006}"

    # もう一度聞くわ。おなか、空いてるわよね？
    voice "sp91_s1735_007"
    l "I'll ask again. You're hungry, aren't you?{#sp91_s1735_007}"

    # ハイ……ぼくおなかぺこぺこでしゅ……。
    voice "sp91_s1735_008"
    s "Yeth… my tummy's rumblin'…{#sp91_s1735_008}"

    # → next scene 1736
    jump sp91_scene_1736

label sp91_scene_1736:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # それじゃあ、食堂に行きましょうか。
    voice "sp91_s1736_002"
    l "Then let's go to the dining hall.{#sp91_s1736_002}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # ほら……これ。食べなさいよ。
    voice "sp91_s1736_010"
    l "Here… this. Eat it.{#sp91_s1736_010}"

    # あ、うん。
    voice "sp91_s1736_011"
    s "Ah, okay.{#sp91_s1736_011}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # [TRANS trans("crossfade", 1000)]
    # は、はい。あーん。
    voice "sp91_s1736_017"
    l "H-Here. Open up.{#sp91_s1736_017}"

    # う……。
    voice "sp91_s1736_018"
    s "Ugh…{#sp91_s1736_018}"

    # なによ。イヤなの？
    voice "sp91_s1736_019"
    l "What? Don't you want it?{#sp91_s1736_019}"

    # い、いや、そんなことは……。
    voice "sp91_s1736_020"
    s "N-No, that's not it…{#sp91_s1736_020}"

    # （ま、まあ、見た目美味そうだし、ここは我慢して……）
    s "(Well, it looks delicious, so I'll just put up with it…){#sp91_s1736_021}"

    # あ、あーん。
    voice "sp91_s1736_022"
    s "A-Ahh.{#sp91_s1736_022}"

    # ぱくっ。
    voice "sp91_s1736_023"
    s "Chomp.{#sp91_s1736_023}"

    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     hide, vibrate=14]
    # [SPRITE   lay5     hide, vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # ……！！！！
    voice "sp91_s1736_033"
    s "…!!!!{#sp91_s1736_033}"

    # （こ、これはっっっっ！！）
    s "(Th-This is—!!){#sp91_s1736_034}"

    # どう？おいしい？
    voice "sp91_s1736_035"
    l "How is it? Good?{#sp91_s1736_035}"

    # （い、いや、これはおいしいとかまずいとか、それ以前の問題で……）
    s "(N-No, this isn't a matter of good or bad… it's something else entirely…){#sp91_s1736_036}"

    # 一口じゃ分からなかったかしら？じゃあ、もう一口。あーん。
    voice "sp91_s1736_037"
    l "Maybe one bite wasn't enough? Then here, another. Open up.{#sp91_s1736_037}"

    # あ、あ、あ、あーん……。
    voice "sp91_s1736_038"
    s "A-A-A-Ahh…{#sp91_s1736_038}"

    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # むぐっ！！！！
    voice "sp91_s1736_048"
    s "Mmgh!!!!{#sp91_s1736_048}"

    # （や、やっぱり……美味いっていうか、そうでないっていうか……、ぶっちゃけ不味い……すっごく……）
    s "(I-It's just as I thought… I can't say it's good, or that it's not… honestly, it's bad… really bad…){#sp91_s1736_049}"

    # どう？おいしい？
    voice "sp91_s1736_050"
    l "How is it? Good?{#sp91_s1736_050}"

    # あ、あの、ルイズ様。つかぬ事を伺いますが、コレを作ったのは……。
    voice "sp91_s1736_051"
    s "U-Um, Louise-sama. I don't mean to pry, but… who made this…?{#sp91_s1736_051}"

    # あ、やっぱり分かった？これはね、わたしが作ってみたの。見よう見まねで。
    voice "sp91_s1736_052"
    l "Oh, you figured it out? I made this myself, you know. Just by watching.{#sp91_s1736_052}"

    # [EVENT_CG event    image=+180, level=80]
    $ dissolve_fx("id(180)")
    # あ、で、でもっ！勘違いしないでよね！
    voice "sp91_s1736_054"
    l "A-And, but! Don't get the wrong idea!{#sp91_s1736_054}"

    # 別にアンタのために作ったって訳じゃなくて、作ってみたかったから作っただけで……。
    voice "sp91_s1736_055"
    l "It's not like I made it for you or anything. I just wanted to try making it, that's all…{#sp91_s1736_055}"

    # あ……そ、そでしゅか……。
    voice "sp91_s1736_056"
    s "Ah… I-I see…{#sp91_s1736_056}"

    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # どうしたの？汗、いっぱいかいてるけど。
    voice "sp91_s1736_058"
    l "What's wrong? You're sweating buckets.{#sp91_s1736_058}"

    # い、いえ……なんでもないでしゅ……。
    voice "sp91_s1736_059"
    s "N-No… it's nothing…{#sp91_s1736_059}"

    # それで！どう、味の方は？割と、自信作なんだけど。
    voice "sp91_s1736_060"
    l "So! How's the taste? I'm actually pretty proud of it.{#sp91_s1736_060}"

    # じ、自信作っ！！
    voice "sp91_s1736_061"
    s "Y-You're proud of it!?{#sp91_s1736_061}"

    # （こ、これが……？）【選択肢】大変個性的なお味です → scene 1737【選択肢】なんか、涙が出てきた →
    s "(Th-This is…?) 【Choice】It's a very unique flavor → scene 1737 【Choice】Somehow, tears came to my eyes → scene 1738 【Choice】It's awful!! → scene 1739{#sp91_s1736_062}"

label sp91_scene_1737:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # 大変個性的なお味です……。
    voice "sp91_s1737_002"
    s "It's a very unique flavor…{#sp91_s1737_002}"

    # そう？料理はあんまり得意じゃないんだけど……。もう少し自信もってもいいかな？
    voice "sp91_s1737_003"
    l "Really? I'm not very good at cooking… Maybe I should have a bit more confidence?{#sp91_s1737_003}"

    # あ、あははは。そ、ソウカモネ……。
    voice "sp91_s1737_004"
    s "A-Ahahaha. Maybe so…{#sp91_s1737_004}"

    # （料理ってか……、これはもはや兵器のような……）→ next scene 1740
    s "(Cooking, my eye… This is practically a weapon…) → next scene 1740{#sp91_s1737_005}"

label sp91_scene_1738:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # なんか、涙が出てきた……。
    voice "sp91_s1738_002"
    s "Somehow, I got teary-eyed…{#sp91_s1738_002}"

    # [EVENT_CG event    image=+180, level=80]
    $ dissolve_fx("id(180)")
    # な、なによ、大げさね。そんなに褒めたって、何も出ないんだから。
    voice "sp91_s1738_004"
    l "W-What are you, so dramatic? Flattery won't get you anything.{#sp91_s1738_004}"

    # あ、あはははは。ご、ご主人様は天才でしゅ……。
    voice "sp91_s1738_005"
    s "A-Ahahahaha. M-Master is a genius…{#sp91_s1738_005}"

    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # もう……馬鹿なこと言ってないで、食べなさい。
    voice "sp91_s1738_007"
    l "Honestly… Stop saying silly things and eat.{#sp91_s1738_007}"

    # は、はいでしゅ……。
    voice "sp91_s1738_008"
    s "Y-Yes…{#sp91_s1738_008}"

    # → next scene 1740
    jump sp91_scene_1740

label sp91_scene_1739:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # （マズイ！！）
    s "(It's awful!!){#sp91_s1739_002}"

    # （なんて、言えるわけないよなあ……）[EVENT_CG event    image=+180, level=
    s "(I could never say that out loud…){#sp91_s1739_003}"

    # ねえ、何か言いなさいよ。気になるわねぇ……。
    voice "sp91_s1739_004"
    l "Come on, say something. I'm curious…{#sp91_s1739_004}"

    # は、はあ……大変、美味でしゅ……。
    voice "sp91_s1739_005"
    s "H-Haah… It's very good…{#sp91_s1739_005}"

    # ふぅ……。もう少し気の利いたことを言えるようになって欲しいわ。
    voice "sp91_s1739_006"
    l "Hmph… I wish you could say something a little cleverer.{#sp91_s1739_006}"

    # これ以上気の利いた事なんて言えるか……。
    voice "sp91_s1739_007"
    s "As if I could say anything cleverer than that…{#sp91_s1739_007}"

    # え？何か言った？
    voice "sp91_s1739_008"
    l "Eh? Did you say something?{#sp91_s1739_008}"

    # い、いえっ！！なんでもっっっ！！
    voice "sp91_s1739_009"
    s "N-No!! Nothing at all!!{#sp91_s1739_009}"

    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # → next scene 1740
    jump sp91_scene_1740

label sp91_scene_1740:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # でも、アンタは幸せ者よ？
    voice "sp91_s1740_002"
    l "But you're a lucky one, aren't you?{#sp91_s1740_002}"

    # そ、そうでしょうか……？
    voice "sp91_s1740_003"
    s "D-Do you really think so…?{#sp91_s1740_003}"

    # そうよ！こんなに可愛くて、優しくて、料理の上手なご主人様なんて、そうそういないんだから。
    voice "sp91_s1740_004"
    l "That's right! There aren't many masters as cute, kind, and good at cooking as me.{#sp91_s1740_004}"

    # は、はぁ……。
    voice "sp91_s1740_005"
    s "H-Haah…{#sp91_s1740_005}"

    # 感謝の言葉は？
    voice "sp91_s1740_006"
    l "Where's my thank-you?{#sp91_s1740_006}"

    # へ？
    voice "sp91_s1740_007"
    s "Eh?{#sp91_s1740_007}"

    # [EVENT_CG event    image=+180, level=80]
    $ dissolve_fx("id(180)")
    # か・ん・しゃ・の・こ・と・ば！
    voice "sp91_s1740_009"
    l "Th-a-n-k-y-o-u!{#sp91_s1740_009}"

    # ええっと……。ボ、ボクハステキナゴシュジンサマヲモテテシアワセダナァ、ワァイ。
    voice "sp91_s1740_010"
    s "U-Um… I-I'm happy to have such a wonderful Master. Yay.{#sp91_s1740_010}"

    # 何か引っかかる言い方ね。まあ、いいけど。
    voice "sp91_s1740_011"
    l "Something about the way you said that bothers me. Well, whatever.{#sp91_s1740_011}"

    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # こんなステキなご主人様を放って他の女の子にしっぽ振ったりなんかしちゃ駄目よ？
    voice "sp91_s1740_013"
    l "You mustn't leave a wonderful Master like me and go wagging your tail at other girls, okay?{#sp91_s1740_013}"

    # は、はい……分かりましたぁ……。
    voice "sp91_s1740_014"
    s "Y-Yes… I understand…{#sp91_s1740_014}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1741:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # そ、それって……どういう意味？
    voice "sp91_s1741_002"
    s "W-What do you mean by that…?{#sp91_s1741_002}"

    # ……わたしは答えをあげないもん。
    voice "sp91_s1741_003"
    l "…I'm not going to tell you.{#sp91_s1741_003}"

    # → next scene 1744
    jump sp91_scene_1744

label sp91_scene_1742:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # ……わ、分からないです。女の子が何を考えてるかなんて。
    voice "sp91_s1742_002"
    s "…Well, I don't know. What girls are thinking, and all that.{#sp91_s1742_002}"

    # サイトは知ろうとしていないだけ。どうして分からないの？
    voice "sp91_s1742_003"
    l "You're just not trying to find out. Why don't you know?{#sp91_s1742_003}"

    # → next scene 1744
    jump sp91_scene_1744

label sp91_scene_1743:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # （……ルイズの囁きが……耳元で……。いい匂い……）
    s "(…Louise's whisper… right by my ear… She smells so good…){#sp91_s1743_002}"

    # （お、俺の中の狼さんが……）
    s "(Oh, the Wolf-san inside me is…){#sp91_s1743_003}"

    # うふふ、どうしたのサイト？顔が真っ赤よ。
    voice "sp91_s1743_004"
    l "Ufufu. What's wrong, Saito? Your face is all red.{#sp91_s1743_004}"

    # → next scene 1744
    jump sp91_scene_1744

label sp91_scene_1744:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # （そ、そんな……耳元にルイズの唇が……？）
    s "(N-No way… Louise's lips right by my ear…?){#sp91_s1744_002}"

    # ねえ、サイト。聞いてるの？
    voice "sp91_s1744_003"
    l "Hey, Saito. Are you listening?{#sp91_s1744_003}"

    # は、はひ……聞いておりますぅ……。
    voice "sp91_s1744_004"
    s "H-Hah… I'm listening, I really am…{#sp91_s1744_004}"

    # じゃあ、ちゃんと返事をしなさい。
    voice "sp91_s1744_005"
    l "Then answer me properly.{#sp91_s1744_005}"

    # あ、あの……ちょっと……。近づきすぎてませんか、ご主人様？
    voice "sp91_s1744_006"
    s "U-Um… a little… Aren't you getting too close, mistress?{#sp91_s1744_006}"

    # ……もしかして、イヤ？
    voice "sp91_s1744_007"
    l "…Could it be you don't like it?{#sp91_s1744_007}"

    # ちょ、ちょっと落ち着かないかな～～、なんて。
    voice "sp91_s1744_008"
    s "I-It's just a little hard to sit still, or something…{#sp91_s1744_008}"

    # [EVENT_CG event    image=+183, level=80]
    $ dissolve_fx("id(183)")
    # こ、こうすると男の子が喜ぶってキュルケが言ってたもん。
    voice "sp91_s1744_010"
    l "K-Kirche said that boys like it when you do this.{#sp91_s1744_010}"

    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # ……サ、サイトは嬉しくないの？
    voice "sp91_s1744_012"
    l "…S-Saito, aren't you happy?{#sp91_s1744_012}"

    # ああっ、耳にルイズの桜色の唇がぁ……。
    voice "sp91_s1744_013"
    s "Aah! Louise's cherry-blossom-pink lips on my ear…!{#sp91_s1744_013}"

        "I'm happy, but…!{#sp91_c_1744_1745}":
            jump sp91_scene_1745
        "I-I'm not happy about this at all!{#sp91_c_1744_1746}":
            jump sp91_scene_1746
        "But I can't hold back!{#sp91_c_1744_1747}":
            jump sp91_scene_1747
label sp91_scene_1745:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # ……う、嬉しいけどぉ！り、理性の限界がぁっ！
    voice "sp91_s1745_002"
    s "…I-I'm happy, but! My reason is at its limit!{#sp91_s1745_002}"

    # これはおしおきなの。ちゃんと耐えなさい。
    voice "sp91_s1745_003"
    l "This is your punishment. Endure it properly.{#sp91_s1745_003}"

    # は、はい……。
    voice "sp91_s1745_004"
    s "Y-Yes…{#sp91_s1745_004}"

    # → next scene 1748
    jump sp91_scene_1748

label sp91_scene_1746:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # う、嬉しくなんてないぞっ！
    voice "sp91_s1746_002"
    s "I-I'm not happy about this!{#sp91_s1746_002}"

    # [EVENT_CG event    image=+183, level=80]
    $ dissolve_fx("id(183)")
    # ……むっ、何を怒ってるのよ？
    voice "sp91_s1746_004"
    l "…Hmph. What are you angry about?{#sp91_s1746_004}"

    # る、ルイズの色香になんて惑わされないんだからな！
    voice "sp91_s1746_005"
    s "I-I won't be seduced by Louise's charms, I tell you!{#sp91_s1746_005}"

    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # なによ……。思いっきり動揺してるじゃない。もう、素直じゃないんだから……。
    voice "sp91_s1746_007"
    l "What was that… You're completely flustered. Honestly, you're so stubborn…{#sp91_s1746_007}"

    # これはおしおきなの。ちゃんと耐えなさい。
    voice "sp91_s1746_008"
    l "This is your punishment. Endure it properly.{#sp91_s1746_008}"

    # は、はい……。
    voice "sp91_s1746_009"
    s "Y-Yes…{#sp91_s1746_009}"

    # → next scene 1748
    jump sp91_scene_1748

label sp91_scene_1747:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # （が、我慢できないっ！理性の限界っ！）
    s "(But I can't hold back! My reason is at its limit!){#sp91_s1747_002}"

    # （ルっ、ルイズぅぅっ！）[EVENT_CG event    image=+183, level=80]
    s "(L-Louiseeee…!){#sp91_s1747_003}"

    # 何、振り向こうとしてるのよ、このバカ犬っ！
    voice "sp91_s1747_004"
    l "What are you trying to turn around for, you stupid dog!{#sp91_s1747_004}"

    # き、きゃいーん！
    voice "sp91_s1747_005"
    s "K-Kyaaain!{#sp91_s1747_005}"

    # ホントにもうっ！……バカ犬なんだから。
    voice "sp91_s1747_006"
    l "Honestly, really! …You're such a stupid dog.{#sp91_s1747_006}"

    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # これはおしおきなの。ちゃんと耐えなさい。
    voice "sp91_s1747_008"
    l "This is your punishment. Endure it properly.{#sp91_s1747_008}"

    # は、はい……。
    voice "sp91_s1747_009"
    s "Y-Yes…{#sp91_s1747_009}"

    # → next scene 1748
    jump sp91_scene_1748

label sp91_scene_1748:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1749:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # 気持ちは……良かったかも。
    voice "sp91_s1749_002"
    s "It… might have felt good.{#sp91_s1749_002}"

    # そう？
    voice "sp91_s1749_003"
    l "Really?{#sp91_s1749_003}"

    # ……え、え～と。
    voice "sp91_s1749_004"
    s "…U-Um, well…{#sp91_s1749_004}"

    # [EVENT_CG event    image=+183, level=80]
    $ dissolve_fx("id(183)")
    # な、なによ。もう一度して欲しいのっ？
    voice "sp91_s1749_006"
    l "W-What was that? Do you want me to do it again?{#sp91_s1749_006}"

    # いや、そういう問題じゃなくて！
    voice "sp91_s1749_007"
    s "No, that's not the point!{#sp91_s1749_007}"

    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # ……うふふ、動揺してるんだ？
    voice "sp91_s1749_009"
    l "…Ufufu. You're flustered, aren't you?{#sp91_s1749_009}"

    # → next scene 1752
    jump sp91_scene_1752

label sp91_scene_1750:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # ど、どこでこんなこと覚えてくるんだよっ！
    voice "sp91_s1750_002"
    s "W-Where did you learn to do things like this?!{#sp91_s1750_002}"

    # [EVENT_CG event    image=+183, level=80]
    $ dissolve_fx("id(183)")
    # な、なによ。気持ちよくなかった！？
    voice "sp91_s1750_004"
    l "W-What? Did it not feel good!?{#sp91_s1750_004}"

    # い、いや！その、なんというか……。
    voice "sp91_s1750_005"
    s "N-No! I mean, how should I put it…{#sp91_s1750_005}"

    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # → next scene 1752
    jump sp91_scene_1752

label sp91_scene_1751:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # （へ、平常心！平常心！）
    s "(Hah, calm down! Stay calm!){#sp91_s1751_002}"

    # ……ねぇ、どうしたの、サイト？黙ってばかりで。そんなに嫌だった？
    voice "sp91_s1751_003"
    l "…Hey, what's wrong, Saito? You've been so quiet. Did you hate it that much?{#sp91_s1751_003}"

    # （う、うわ～～っ。ルイズの体が寄ってくるなんて……）
    s "(O-Ohh… Louise's body is pressing closer…){#sp91_s1751_004}"

    # な、なんでこんなことを……。
    voice "sp91_s1751_005"
    s "W-Why are you doing this…?{#sp91_s1751_005}"

    # → next scene 1752
    jump sp91_scene_1752

label sp91_scene_1752:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # ……だって。
    voice "sp91_s1752_002"
    l "…Because.{#sp91_s1752_002}"

    # ……こ、こうすると男の子が喜ぶってキュルケが言ってたもん。
    voice "sp91_s1752_003"
    l "…K-Kirche said that boys like it when you do this.{#sp91_s1752_003}"

    # （……うっ、かわいいっ）
    s "(…Nghh, she's so cute!){#sp91_s1752_004}"

    # ねえ？サイトは……うれしくないの？
    voice "sp91_s1752_005"
    l "Hey? Saito, aren't you… happy?{#sp91_s1752_005}"

    # え、ええと……。
    voice "sp91_s1752_006"
    s "U-Um…{#sp91_s1752_006}"

        "I'm happy. Please continue.{#sp91_c_1752_1753}":
            jump sp91_scene_1753
        "D-Don't be all over me!{#sp91_c_1752_1754}":
            jump sp91_scene_1754
        "My reason is at its limit!{#sp91_c_1752_1755}":
            jump sp91_scene_1755
label sp91_scene_1753:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # う、うれしいです。……続けてください。
    voice "sp91_s1753_002"
    s "I-I'm happy. …Please continue.{#sp91_s1753_002}"

    # あっ……うん。
    voice "sp91_s1753_003"
    l "Ah… Mm.{#sp91_s1753_003}"

    # もうっ、仕方ないんだからっ。
    voice "sp91_s1753_004"
    l "Honestly… I suppose I have no choice.{#sp91_s1753_004}"

    # ねえ……こう？
    voice "sp91_s1753_005"
    l "Hey… like this?{#sp91_s1753_005}"

    # あ、ふぅっ。
    voice "sp91_s1753_006"
    s "Ah… Fwuh.{#sp91_s1753_006}"

    # 首筋に……こういうのはどうかしら？
    voice "sp91_s1753_007"
    l "On the nape of your neck… how's this?{#sp91_s1753_007}"

    # い、いいです。ご主人様っ。それ、もっとっ！
    voice "sp91_s1753_008"
    s "Y-Yes. Mistress! More, do more!{#sp91_s1753_008}"

    # うふふふっ。癖になりそう……。
    voice "sp91_s1753_009"
    l "Ufufufu. I could get used to this…{#sp91_s1753_009}"

    # → next scene 1756
    jump sp91_scene_1756

label sp91_scene_1754:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # べ、ベタベタするんじゃない！
    voice "sp91_s1754_002"
    s "D-Don't get all lovey-dovey on me!{#sp91_s1754_002}"

    # [EVENT_CG event    image=+183, level=80]
    $ dissolve_fx("id(183)")
    # ……な、なによ。いきなり怒り出して。
    voice "sp91_s1754_004"
    l "…W-What was that? Getting angry all of a sudden.{#sp91_s1754_004}"

    # そ、そんなふうにされると……、いろいろ困るんだよ。男の子はっ！
    voice "sp91_s1754_005"
    s "W-When you do that… it causes all sorts of problems. Guys do!{#sp91_s1754_005}"

    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # もうっ、いいじゃない。少しぐらい。うふふっ。
    voice "sp91_s1754_007"
    l "Oh, come on. A little bit won't hurt. Ufufu.{#sp91_s1754_007}"

    # → next scene 1756
    jump sp91_scene_1756

label sp91_scene_1755:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # り、理性の限界がぁっ！
    voice "sp91_s1755_002"
    s "My reason is at its limit!{#sp91_s1755_002}"

    # [EVENT_CG event    image=+183, level=80]
    $ dissolve_fx("id(183)")
    # ……な、なに考えてるのよっ！
    voice "sp91_s1755_004"
    l "…W-What are you thinking about?!{#sp91_s1755_004}"

    # ル、ルイズ！
    voice "sp91_s1755_005"
    s "L-Louise!{#sp91_s1755_005}"

    # もうっ、我慢なさいっ！
    voice "sp91_s1755_006"
    l "Honestly, put up with it!{#sp91_s1755_006}"

    # そ、そんなぁ……。そ、その気にさせといてそれは……。
    voice "sp91_s1755_007"
    s "N-No way… You got me all worked up and then this…?{#sp91_s1755_007}"

    # ……そ、その気って……もうっ！何を考えてるの？
    voice "sp91_s1755_008"
    l "…T-That 'worked up'… Honestly! What are you thinking?{#sp91_s1755_008}"

    # ううっ、すいません。
    voice "sp91_s1755_009"
    s "Ugh… I'm sorry.{#sp91_s1755_009}"

    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # うふふ……。ホントに仕方ないんだから……。
    voice "sp91_s1755_011"
    l "Ufufu… Honestly, there's just no helping it…{#sp91_s1755_011}"

    # → next scene 1756
    jump sp91_scene_1756

label sp91_scene_1756:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1757:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # （これはマズイ！マズイって！）
    s "(This is bad! Really bad!){#sp91_s1757_002}"

    # そ、そういうのはちょっと……。
    voice "sp91_s1757_003"
    s "T-That's a bit…{#sp91_s1757_003}"

    # た、助けてぇぇっ！
    voice "sp91_s1757_004"
    s "H-Help meee!{#sp91_s1757_004}"

    # 逃げないで。サイト。
    voice "sp91_s1757_005"
    l "Don't run away, Saito.{#sp91_s1757_005}"

    # → next scene 1760
    jump sp91_scene_1760

label sp91_scene_1758:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # ちょ、ちょっと。ま、待ってぇ！
    voice "sp91_s1758_002"
    s "W-Wait. J-Just wait a second!{#sp91_s1758_002}"

    # （お、俺の心の狼さんが……暴走を……）
    s "(My inner wolf is… running wild…){#sp91_s1758_003}"

    # ねぇ、なんでわたしのこと拒絶するの？サイト。
    voice "sp91_s1758_004"
    l "Hey, why do you keep rejecting me? Saito.{#sp91_s1758_004}"

    # → next scene 1760
    jump sp91_scene_1760

label sp91_scene_1759:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # （あうっ……や、やわらかい……）
    s "(Ooh… s-so soft…){#sp91_s1759_002}"

    # ほら、じっとしてなさい……。
    voice "sp91_s1759_003"
    l "Now, hold still…{#sp91_s1759_003}"

    # ねぇ、サイト……。わたしのこと……嫌いじゃないわよね？
    voice "sp91_s1759_004"
    l "Say, Saito… You don't hate me… do you?{#sp91_s1759_004}"

    # ……う、うん。そ、そうなんだけど……。
    voice "sp91_s1759_005"
    s "…Y-Yeah. T-That's right, but…{#sp91_s1759_005}"

    # → next scene 1760
    jump sp91_scene_1760

label sp91_scene_1760:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # [EVENT_CG event    image=+184, level=80]
    $ dissolve_fx("id(184)")
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # ……カプっ。
    voice "sp91_s1760_004"
    l "…Chomp.{#sp91_s1760_004}"

    # はうぁっ！ど、どこ噛んでやがりますか！
    voice "sp91_s1760_005"
    s "Ow! Wh-Where did you bite me?!{#sp91_s1760_005}"

    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # ……キュルケに教えてもらったの。こうやって優しく耳を噛んであげると男の子は喜ぶって。
    voice "sp91_s1760_007"
    l "…Kirche told me. She said that if you gently nibble a boy's ear like this, he'll love it.{#sp91_s1760_007}"

    # ……ねぇ、喜んでくれないの？
    voice "sp91_s1760_008"
    l "…Hey, aren't you enjoying it?{#sp91_s1760_008}"

    # そ、そりゃその……あの……。
    voice "sp91_s1760_009"
    s "T-That's… I mean…{#sp91_s1760_009}"

        "S-Stop it!{#sp91_c_1760_1761}":
            jump sp91_scene_1761
        "Don't stop!{#sp91_c_1760_1762}":
            jump sp91_scene_1762
        "M-More!?{#sp91_c_1760_1763}":
            jump sp91_scene_1763
label sp91_scene_1761:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # や、やめてぇっ！
    voice "sp91_s1761_002"
    s "S-Stop it!{#sp91_s1761_002}"

    # [EVENT_CG event    image=+183, level=80]
    $ dissolve_fx("id(183)")
    # な、なにっ！こーゆーのイヤなの？
    voice "sp91_s1761_004"
    l "W-What! You don't like this?{#sp91_s1761_004}"

    # そういうわけじゃないけど……。
    voice "sp91_s1761_005"
    s "That's not it, but…{#sp91_s1761_005}"

    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # うふふ……。
    voice "sp91_s1761_007"
    l "Heh heh…{#sp91_s1761_007}"

    # い、いや、だからっ！
    voice "sp91_s1761_008"
    s "N-No, I mean…!{#sp91_s1761_008}"

    # → next scene 1764
    jump sp91_scene_1764

label sp91_scene_1762:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # や、やめないで！
    voice "sp91_s1762_002"
    s "D-Don't stop!{#sp91_s1762_002}"

    # ふぅん？こーゆーのがいいのね？はむはむ。
    voice "sp91_s1762_003"
    l "Hmm? So you like this? Nibble nibble.{#sp91_s1762_003}"

    # [EVENT_CG event    image=+184, level=80]
    $ dissolve_fx("id(184)")
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # ……ルイズっ……そ、そんな！
    voice "sp91_s1762_006"
    s "…Louise… D-Don't!{#sp91_s1762_006}"

    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # ご主人様のことを見てくれない悪い子にはおしおきなんだから……。
    voice "sp91_s1762_008"
    l "Naughty children who don't look at their master get punished…{#sp91_s1762_008}"

    # [EVENT_CG event    image=+184, level=80]
    $ dissolve_fx("id(184)")
    # はうう……。ご、ご主人様～～っ！
    voice "sp91_s1762_010"
    s "Aah… M-Masterrrr!{#sp91_s1762_010}"

    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # → next scene 1764
    jump sp91_scene_1764

label sp91_scene_1763:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # も、もっとぉ！？
    voice "sp91_s1763_002"
    s "M-More!?{#sp91_s1763_002}"

    # そんなに効くなんて思ってもみなかったわ。はむはむ。
    voice "sp91_s1763_003"
    l "I never thought it would work that well. Nibble nibble.{#sp91_s1763_003}"

    # [EVENT_CG event    image=+184, level=80]
    $ dissolve_fx("id(184)")
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # ……ルイズっ……そ、そんな！
    voice "sp91_s1763_006"
    s "…Louise… D-Don't!{#sp91_s1763_006}"

    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # → next scene 1764
    jump sp91_scene_1764

label sp91_scene_1764:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+182, level=80]
    $ dissolve_fx("id(182)")
    # うふふ、かわいい。もっと噛んじゃお。
    voice "sp91_s1764_002"
    l "Heh heh, you're cute. I'll bite some more.{#sp91_s1764_002}"

    # [EVENT_CG event    image=+184, level=80]
    $ dissolve_fx("id(184)")
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # ひ、ひぅっ。
    voice "sp91_s1764_005"
    s "O-Oof!{#sp91_s1764_005}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1765:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # （でも、寝顔はホントかわいいよな。さすがは貴族のお嬢さま）
    s "(But her sleeping face really is cute. She's a noble lady, after all.){#sp91_s1765_002}"

    # （おとぎ話の眠り姫みたいで……）
    s "(Like a sleeping beauty from a fairy tale…){#sp91_s1765_003}"

    # ……。
    s "…{#sp91_s1765_004}"

    # ……んっ……スゥスゥ……。
    voice "sp91_s1765_005"
    l "…Mm… su-su…{#sp91_s1765_005}"

    # （やばい……ドキドキしてきたぞ……）→ next scene 1768
    s "(This is bad… my heart's starting to race…){#sp91_s1765_006}"

label sp91_scene_1766:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # （ま、まずい、よこしまな考えが……）
    s "(T-This is bad, these wicked thoughts…){#sp91_s1766_002}"

    # ……んっ……スゥスゥ……。
    voice "sp91_s1766_003"
    l "…Mm… su-su…{#sp91_s1766_003}"

    # （や、やめるんだ！俺！）
    s "(Stop it! Me!){#sp91_s1766_004}"

    # ……ふにっ、ふにふにっ。
    th "…Squish… squish-squish…{#sp91_s1766_005}"

    # （ああっ！や、やわらかいっ！やわらかいっすよ！）
    s "(Ah! S-So soft! It's so soft!){#sp91_s1766_006}"

    # （ルイズのほっぺた！）
    s "(Louise's cheek!){#sp91_s1766_007}"

    # ……んっ……んんっ……。
    voice "sp91_s1766_008"
    l "…Mm… mmm…{#sp91_s1766_008}"

    # （やばい……ドキドキしてきたぞ……）→ next scene 1768
    s "(This is bad… my heart's starting to race…){#sp91_s1766_009}"

label sp91_scene_1767:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # （……お、俺も寝よう）
    s "(…I should sleep too.){#sp91_s1767_002}"

    # ……。
    s "…{#sp91_s1767_003}"

    # ……んっ……スゥスゥ……。
    voice "sp91_s1767_004"
    l "…Mm… su-su…{#sp91_s1767_004}"

    # （……ルイズの寝息……体温……）
    s "(…Louise's breathing… her warmth…){#sp91_s1767_005}"

    # （……だ、ダメだ。眠れないって！）→ next scene 1768
    s "(…N-No good. I can't sleep!){#sp91_s1767_006}"

label sp91_scene_1768:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # （はあ～～、信頼してくれてるのは嬉しいけど……）
    s "(Phew… I'm glad she trusts me, but…){#sp91_s1768_002}"

    # （……お、俺だって実は狼さんだっつ～～の！）
    s "(…I'm a wolf too, I tell you!){#sp91_s1768_003}"

    # ……。
    s "…{#sp91_s1768_004}"

    # ……ル、ルイズ？
    voice "sp91_s1768_005"
    s "…L-Louise?{#sp91_s1768_005}"

        "N-No, I can't give in to temptation!{#sp91_c_1768_1769}":
            jump sp91_scene_1769
        "…N-No, I said no!{#sp91_c_1768_1770}":
            jump sp91_scene_1770
        "What if I let myself go wild?{#sp91_c_1768_1771}":
            jump sp91_scene_1771
label sp91_scene_1769:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # （……ゆ、誘惑に負けてはいけないよな）
    s "(…I mustn't give in to temptation.){#sp91_s1769_002}"

    # （や、やせ我慢は男の美学なんだっ！）
    s "(Staying stoic is a man's pride!){#sp91_s1769_003}"

    # ……んっ……サイトぉ……。
    voice "sp91_s1769_004"
    l "…Mm… Saitooo…{#sp91_s1769_004}"

    # （……くっ、そ、そんな寝言で、お、俺を誘惑するんじゃない！）
    s "(…Damn, don't you try to seduce me with that sleep-talk!){#sp91_s1769_005}"

    # （お、俺は誘惑には屈しないのであります！）
    s "(I shall not yield to temptation!){#sp91_s1769_006}"

    # ……バカ犬……スゥスゥ……。
    voice "sp91_s1769_007"
    l "…Stupid dog… su-su…{#sp91_s1769_007}"

    # （と、いうことでおやすみなさい！）
    s "(So, with that said — good night!){#sp91_s1769_008}"

    # （……へ、平常心！平常心！）[SPRITE   lay1     hide][SPRITE   lay5   
    s "(…K-Keep calm! Stay calm!){#sp91_s1769_009}"

    # ………。……。…。[EVENT_CG event    image=+185, level=80][TRANS
    th "…{#sp91_s1769_010}"

    # ……むにゃむにゃ……。
    voice "sp91_s1769_011"
    s "…Mumble mumble…{#sp91_s1769_011}"

    # ……。
    voice "sp91_s1769_012"
    l "…{#sp91_s1769_012}"

    # ……意気地なし……。
    voice "sp91_s1769_013"
    l "…Coward…{#sp91_s1769_013}"

    # → next scene 1772
    jump sp91_scene_1772

label sp91_scene_1770:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # （……だ、駄目だって！俺！）
    s "(…N-No, I said! Stop it, me!){#sp91_s1770_002}"

    # （も、もし、そんなことをしたのがルイズにバレたら……）
    s "(I-If Louise found out I did something like that…){#sp91_s1770_003}"

    # （や、やめろぉぉぉっ！）
    s "(S-Stop itttt!){#sp91_s1770_004}"

    # （ルイズの鼻をつまむなんて！）
    s "(Pinching Louise's nose!){#sp91_s1770_005}"

    # ……ひゅくっ……。
    voice "sp91_s1770_006"
    l "…Eep…{#sp91_s1770_006}"

    # （か、かわいい反応を……。い、いつもの仕返しだからな）
    s "(C-Cute reaction… I-It's just her usual payback, that's all.){#sp91_s1770_007}"

    # ……んっ、んんんっ？
    voice "sp91_s1770_008"
    l "…Mm, mmm?{#sp91_s1770_008}"

    # （ま、まずい！）[SPRITE   lay1     hide][SPRITE   lay5     hide
    s "(T-Trouble!){#sp91_s1770_009}"

    # んっ……サイト……？
    voice "sp91_s1770_010"
    l "Mm… Saito…?{#sp91_s1770_010}"

    # ……ぐうぐうぐう。
    voice "sp91_s1770_011"
    s "…Snore, snore, snore.{#sp91_s1770_011}"

    # ……夢？かしら？
    voice "sp91_s1770_012"
    l "…Was it a dream? I wonder.{#sp91_s1770_012}"

    # ……むにゃむにゃむにゃ。
    voice "sp91_s1770_013"
    s "…Mumble mumble mumble.{#sp91_s1770_013}"

    # ……。
    voice "sp91_s1770_014"
    l "…{#sp91_s1770_014}"

    # ホントにもう……バカなんだから。
    voice "sp91_s1770_015"
    l "Really, you're such an idiot.{#sp91_s1770_015}"

    # → next scene 1772
    jump sp91_scene_1772

label sp91_scene_1771:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # （や、ヤメロ！ヤメロって！）
    s "(S-Stop! I said stop!){#sp91_s1771_002}"

    # （な、なんというか体がいうことを聞かないような……）
    s "(I-It's like my body won't listen to me…){#sp91_s1771_003}"

    # （お、俺の中の獣がぁぁぁっ！）[SE       se0      play=+61][BG       st
    s "(T-The beast inside meeee!){#sp91_s1771_004}"

    # ……サイト、うるさい！むにゃむにゃ……。
    voice "sp91_s1771_005"
    l "…Saito, quiet! Mumble mumble…{#sp91_s1771_005}"

    # （……ぐ、ぐぉぉぉっ！！俺の偉大なところにクリティカルヒット！というか痛恨の一撃！）
    s "(…G-Gah!! A critical hit to my awesomeness! Or rather, a crushing blow!){#sp91_s1771_006}"

    # （な、何しやがる！ルイズ！）
    s "(W-What are you doing! Louise!){#sp91_s1771_007}"

    # ……バカ犬！むにゃむにゃ……。
    voice "sp91_s1771_008"
    l "…Stupid dog! Mumble mumble…{#sp91_s1771_008}"

    # （はあ、もう……。……い、いや、助かったというべきかな？）
    s "(Phew… …N-No, maybe I should be glad?){#sp91_s1771_009}"

    # おやすみ。ルイズ。
    voice "sp91_s1771_010"
    s "Good night, Louise.{#sp91_s1771_010}"

    # ……。
    voice "sp91_s1771_011"
    l "…{#sp91_s1771_011}"

    # ……ん、おやすみ。サイト。
    voice "sp91_s1771_012"
    l "…Mm, good night, Saito.{#sp91_s1771_012}"

    # → next scene 1772
    jump sp91_scene_1772

label sp91_scene_1772:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+185, level=80]
    $ dissolve_fx("id(185)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1773:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+185, level=80]
    $ dissolve_fx("id(185)")
    # ……べ、別にいいけど？
    voice "sp91_s1773_002"
    s "……B-But, it's fine, really……?{#sp91_s1773_002}"

    # ……そう？じゃあ……。
    voice "sp91_s1773_003"
    l "……Is that so? Then……{#sp91_s1773_003}"

    # → next scene 1776
    jump sp91_scene_1776

label sp91_scene_1774:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+185, level=80]
    $ dissolve_fx("id(185)")
    # ちょ、ちょっと！腕枕って……。
    voice "sp91_s1774_002"
    s "W-Wait! You want me to be your arm pillow……?{#sp91_s1774_002}"

    # ……いいの？
    voice "sp91_s1774_003"
    s "……Are you sure?{#sp91_s1774_003}"

    # もう、わたしがしてって言ってるのよ。
    voice "sp91_s1774_004"
    l "Come on, I'm telling you to do it.{#sp91_s1774_004}"

    # え、ええと……了解です。
    voice "sp91_s1774_005"
    s "E-Er…… Understood.{#sp91_s1774_005}"

    # → next scene 1776
    jump sp91_scene_1776

label sp91_scene_1775:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+185, level=80]
    $ dissolve_fx("id(185)")
    # ダ、ダメだって！
    voice "sp91_s1775_002"
    s "N-No, I can't!{#sp91_s1775_002}"

    # ……もうっ、なんで？
    voice "sp91_s1775_003"
    l "……Honestly, why?{#sp91_s1775_003}"

    # ……我慢できなくなるかもしれないし。
    voice "sp91_s1775_004"
    s "……I might not be able to hold back anymore.{#sp91_s1775_004}"

    # 我慢って？何を？
    voice "sp91_s1775_005"
    l "Hold back? From what?{#sp91_s1775_005}"

    # え、ええと……。なんでもない。
    voice "sp91_s1775_006"
    s "E-Er…… It's nothing.{#sp91_s1775_006}"

    # い、いいわよ。別に気にしないから。
    voice "sp91_s1775_007"
    l "I-It's fine. I don't mind at all.{#sp91_s1775_007}"

    # ……え？い、いいの？
    voice "sp91_s1775_008"
    s "……Eh? Are you sure it's okay?{#sp91_s1775_008}"

    # へ、変な意味じゃないわよ？信じてるからって意味よ！
    voice "sp91_s1775_009"
    l "H-It's not some weird meaning! I mean that I trust you!{#sp91_s1775_009}"

    # → next scene 1776
    jump sp91_scene_1776

label sp91_scene_1776:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+185, level=80]
    $ dissolve_fx("id(185)")
    # [SE       se0      play=+59]
    # [EVENT_CG event    image=+186, level=80]
    $ dissolve_fx("id(186)")
    # こ、これでいい？
    voice "sp91_s1776_004"
    s "I-Is this okay?{#sp91_s1776_004}"

    # ……サイトの体、暖かいね。
    voice "sp91_s1776_005"
    l "……Saito, you're so warm.{#sp91_s1776_005}"

    # そ、そう？
    voice "sp91_s1776_006"
    s "R-Really?{#sp91_s1776_006}"

    # うん……。
    voice "sp91_s1776_007"
    l "Mm……{#sp91_s1776_007}"

    # こうやってサイトの腕に耳を当ててると、なんだかすごく落ち着くの……フワ……。
    voice "sp91_s1776_008"
    l "When I put my ear against your arm like this, I feel so at ease…… so soft……{#sp91_s1776_008}"

    # ええと、その……光栄です。
    voice "sp91_s1776_009"
    s "Um, that's…… an honor.{#sp91_s1776_009}"

    # なんだか眠くなっちゃった……。
    voice "sp91_s1776_010"
    l "I'm getting sleepy……{#sp91_s1776_010}"

    # 俺はルイズの体の方が暖かく感じるけど……。
    voice "sp91_s1776_011"
    s "I feel like Louise is the warmer one, though……{#sp91_s1776_011}"

    # もう……ルイズじゃなくて……。……ご主人様……でしょ……。スゥスゥ……。
    voice "sp91_s1776_012"
    l "Come on…… not Louise…… It's…… Master…… right……? Su-su……{#sp91_s1776_012}"

    # ……あ、あの？ルイズ？
    voice "sp91_s1776_013"
    s "……U-Um? Louise?{#sp91_s1776_013}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # （……はぁ、まったく勝手だよな）
    s "(……Haa, she really does as she pleases.){#sp91_s1776_019}"

    # （でも、自分の腕の中に女の子の重さがあるのって……悪くないよな）[SPRITE   lay5     hide
    s "(But having a girl's weight in my arms…… isn't bad at all.){#sp91_s1776_020}"

    # ………。……。…。[BG       stage    image=+90, level=200][TRANS
    th "……… …… …{#sp91_s1776_021}"

    # ……スゥスゥ。
    voice "sp91_s1776_022"
    l "……Su-su.{#sp91_s1776_022}"

    # （……ぐぉぉぉ、し、痺れた！……う、腕の感覚がない）【選択肢】そっと、外して…… → scene 1777【選
    s "(……Guhhh, i-it's gone numb! ……Ugh, I can't feel my arm.) / Gently, take it out…… / Endure it, endure it! / Wake Louise up……{#sp91_s1776_023}"

label sp91_scene_1777:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # （……そ、そおっとルイズの頭の下から腕を抜いて）
    s "(……G-Gently, I slide my arm out from under Louise's head){#sp91_s1777_002}"

    # ……んっ……ダメっ、サイト……。
    voice "sp91_s1777_003"
    l "……Mm…… No, Saito……{#sp91_s1777_003}"

    # （うっ、しがみついてこられた！）
    s "(Ugh, she clung onto me!){#sp91_s1777_004}"

    # ……い、行っちゃヤダ……。
    voice "sp91_s1777_005"
    l "……I don't want you to go……{#sp91_s1777_005}"

    # （寝言？）
    s "(Sleep talking?){#sp91_s1777_006}"

    # はいはい、大丈夫……。どこにも行かないよ。
    voice "sp91_s1777_007"
    s "Yes, yes, it's fine…… I'm not going anywhere.{#sp91_s1777_007}"

    # ……んっ、約束よ……スゥスゥ。
    voice "sp91_s1777_008"
    l "……Mm, promise me…… Su-su.{#sp91_s1777_008}"

    # （はぁ、痺れても仕方ないか）
    s "(Haa, I guess there's no help for it even if it's numb.){#sp91_s1777_009}"

    # ……かわいい寝顔だな。
    voice "sp91_s1777_010"
    s "……What a cute sleeping face.{#sp91_s1777_010}"

    # （いつもこんな感じだったら、かわいくていいのになぁ）→ next scene 1780
    s "(If it was always like this, it'd be so cute……){#sp91_s1777_011}"

label sp91_scene_1778:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # ……かわいい寝顔だな。
    voice "sp91_s1778_002"
    s "……What a cute sleeping face.{#sp91_s1778_002}"

    # （こ、このしびれは男の名誉の負傷なのだ！）
    s "(T-This numbness is a wound of a man's honor!){#sp91_s1778_003}"

    # ……んっ、サイト……スゥスゥ。
    voice "sp91_s1778_004"
    l "……Mm, Saito…… Su-su.{#sp91_s1778_004}"

    # （寝言？）
    s "(Sleep talking?){#sp91_s1778_005}"

    # ……ううっ、我慢するよ！すればいいんだろ！
    voice "sp91_s1778_006"
    s "……Ugh, I'll endure it! That's what I should do, right!{#sp91_s1778_006}"

    # （はぁ、痺れても仕方ないか……）→ next scene 1780
    s "(Haa, I guess there's no help for it even if it's numb……){#sp91_s1778_007}"

label sp91_scene_1779:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # ちょ、ちょっと、起きろ！ルイズ！
    voice "sp91_s1779_002"
    s "H-Hey, wake up! Louise!{#sp91_s1779_002}"

    # ……うるさい、バカ犬……スゥスゥ。
    voice "sp91_s1779_003"
    l "……Noisy, stupid dog…… Su-su.{#sp91_s1779_003}"

    # （……起きてくれないよ）
    s "(……She won't wake up.){#sp91_s1779_004}"

    # ……んっ、サイト……スゥスゥ。
    voice "sp91_s1779_005"
    l "……Mm, Saito…… Su-su.{#sp91_s1779_005}"

    # （寝言？夢に俺が出てるのか……）
    s "(Sleep talking? Am I in her dream……?){#sp91_s1779_006}"

    # ……んっ、ふふ……。
    voice "sp91_s1779_007"
    l "……Mm, hehe……{#sp91_s1779_007}"

    # （こんな寝顔をしてる女の子を起こそうなんて奴は、男じゃないよな……）
    s "(Any guy who'd wake a girl with a face like this…… isn't a man.){#sp91_s1779_008}"

    # （はぁ、我慢するか。おやすみ、ルイズ……）→ next scene 1780
    s "(Haa, I'll just put up with it. Good night, Louise……){#sp91_s1779_009}"

label sp91_scene_1780:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1781:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+185, level=80]
    $ dissolve_fx("id(185)")
    # な、なんというか……。
    voice "sp91_s1781_002"
    s "W-What can I say……{#sp91_s1781_002}"

    # 女の子って暖かくてやわらかいなあ……。って思って。
    voice "sp91_s1781_003"
    s "Girls are so warm and soft…… That's what I was thinking.{#sp91_s1781_003}"

    # ば、馬鹿っ！なに考えてるのよ！
    voice "sp91_s1781_004"
    l "I-Idiot! What are you thinking!{#sp91_s1781_004}"

    # し、仕方ないだろ！ホントにそう思っちゃったんだから！
    voice "sp91_s1781_005"
    s "I-It can't be helped! I really did think that!{#sp91_s1781_005}"

    # ……女の子って不思議だよな。
    voice "sp91_s1781_006"
    s "……Girls are mysterious, aren't they?{#sp91_s1781_006}"

    # ……そう？女の子にしてみたら、男の子のほうがよっぽど不思議な生きものよ。
    voice "sp91_s1781_007"
    l "……Really? From a girl's point of view, boys are far more mysterious creatures.{#sp91_s1781_007}"

    # → next scene 1784
    jump sp91_scene_1784

label sp91_scene_1782:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+185, level=80]
    $ dissolve_fx("id(185)")
    # ……やっぱり、ちいさいよなぁ。
    voice "sp91_s1782_002"
    s "……After all, you're so small.{#sp91_s1782_002}"

    # ……な、なんの話かしら？
    voice "sp91_s1782_003"
    l "……W-What are you talking about?{#sp91_s1782_003}"

    # い、いや、なんでもないです。
    voice "sp91_s1782_004"
    s "N-No, it's nothing.{#sp91_s1782_004}"

    # バ、バカ犬……。わたしのどこについて、誰と比べたの？言ってみなさい。
    voice "sp91_s1782_005"
    l "S-Stupid dog…… What about me, and who did you compare me to? Say it.{#sp91_s1782_005}"

    # ……す、すいましぇん。
    voice "sp91_s1782_006"
    s "……I-I'm sorry.{#sp91_s1782_006}"

    # ……背とか体つきの話です。
    voice "sp91_s1782_007"
    s "……I was talking about your height and build.{#sp91_s1782_007}"

    # ……へ？あ、ああ、そうだったの。て、てっきり……。
    voice "sp91_s1782_008"
    l "……Eh? O-Oh, that's what you meant. I-I thought……{#sp91_s1782_008}"

    # （……やっぱりムネのこと、気にしてるんだ）
    s "(……She really is self-conscious about her chest.){#sp91_s1782_009}"

    # （が、頑張るんだぞ。ルイズ）→ next scene 1784
    s "(But hang in there, Louise.){#sp91_s1782_010}"

label sp91_scene_1783:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+185, level=80]
    $ dissolve_fx("id(185)")
    # あはは、は……なんでもないです。
    voice "sp91_s1783_002"
    s "Ahaha, ha…… It's nothing.{#sp91_s1783_002}"

    # ……き、きっと、わたしのことをなにか馬鹿にしてたんでしょ？
    voice "sp91_s1783_003"
    l "……Y-You were making fun of me somehow, weren't you?{#sp91_s1783_003}"

    # （ひ、被害妄想だって！……ルイズの奴、コンプレックスが強すぎだ）
    s "(H-Her persecution complex! ……Louise has way too much of an inferiority complex.){#sp91_s1783_004}"

    # ほ、ホントホント！ルイズかわいいなあ、とかそんなことだよ。
    voice "sp91_s1783_005"
    s "R-Really, really! I was just thinking how cute Louise is, that's all.{#sp91_s1783_005}"

    # ……ホント？
    voice "sp91_s1783_006"
    l "……Really?{#sp91_s1783_006}"

    # ホントに、サイトはわたしのことをかわいいって思ってくれてるの？
    voice "sp91_s1783_007"
    l "Do you really think I'm cute, Saito?{#sp91_s1783_007}"

    # も、もちろんだって！俺のご主人様は、メチャかわいい女の子だって！
    voice "sp91_s1783_008"
    s "O-Of course! My master is an incredibly cute girl!{#sp91_s1783_008}"

    # うふふ、ありがと。
    voice "sp91_s1783_009"
    l "Ufufu, thank you.{#sp91_s1783_009}"

    # → next scene 1784
    jump sp91_scene_1784

label sp91_scene_1784:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+185, level=80]
    $ dissolve_fx("id(185)")
    # ……それで、その。
    voice "sp91_s1784_002"
    s "……So, um.{#sp91_s1784_002}"

    # もう少し離れてほしいなあ……って。
    voice "sp91_s1784_003"
    s "I want you to move a little farther away…… or something.{#sp91_s1784_003}"

    # ……イヤ！
    voice "sp91_s1784_004"
    l "……No!{#sp91_s1784_004}"

    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # は、はうっっ！そんなぁ……。
    voice "sp91_s1784_006"
    s "G-Gah! That's too much……{#sp91_s1784_006}"

    # こ、これは罰なんだもん！
    voice "sp91_s1784_007"
    l "T-This is a punishment, okay!{#sp91_s1784_007}"

        "This slow torture is too cruel~~!{#sp91_c_1784_1785}":
            jump sp91_scene_1785
        "I-If you come at me, what am I supposed to do?{#sp91_c_1784_1786}":
            jump sp91_scene_1786
        "I'll accept the punishment willingly.{#sp91_c_1784_1787}":
            jump sp91_scene_1787
label sp91_scene_1785:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+185, level=80]
    $ dissolve_fx("id(185)")
    # ……生殺しなんて酷すぎるって～～！
    voice "sp91_s1785_002"
    s "……This slow torture is too cruel~~!{#sp91_s1785_002}"

    # 酷いから罰になるんだもん！
    voice "sp91_s1785_003"
    l "It's cruel, that's why it's a punishment!{#sp91_s1785_003}"

    # ……サイトがちゃんと反省するまでこうするんだから！
    voice "sp91_s1785_004"
    l "……I'll keep this up until Saito properly reflects!{#sp91_s1785_004}"

    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # は、はうっ～～っ！
    voice "sp91_s1785_006"
    s "H-Hugh~~!{#sp91_s1785_006}"

    # か、勘弁してください～～。
    voice "sp91_s1785_007"
    s "P-Please forgive me~~.{#sp91_s1785_007}"

    # ……俺、どうにかなっちゃいますって！
    voice "sp91_s1785_008"
    s "……I'm going to lose it here!{#sp91_s1785_008}"

    # うふふ……おやすみ、サイト。
    voice "sp91_s1785_009"
    l "Ufufu…… Good night, Saito.{#sp91_s1785_009}"

    # ……もし、変なことなんてしたら、許さ……ないんだから……ね……。
    voice "sp91_s1785_010"
    l "……If you do anything strange, I won't…… forgive you…… okay……{#sp91_s1785_010}"

    # → next scene 1788
    jump sp91_scene_1788

label sp91_scene_1786:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+185, level=80]
    $ dissolve_fx("id(185)")
    # お、襲われたらどうするんだよ。
    voice "sp91_s1786_002"
    s "I-If you come at me, what am I supposed to do?{#sp91_s1786_002}"

    # ……わたしを、襲っちゃうの？
    voice "sp91_s1786_003"
    l "……You'd attack me?{#sp91_s1786_003}"

    # 襲わない！誓って絶対に襲わないけど……。
    voice "sp91_s1786_004"
    s "I wouldn't! I swear I'd never attack you……{#sp91_s1786_004}"

    # その、ボク……バカ犬だし……。やっぱり、自信が。
    voice "sp91_s1786_005"
    s "I mean, I'm…… a stupid dog…… After all, I'm not confident.{#sp91_s1786_005}"

    # ……サイトはわたしのこと大事に思ってくれてるのね。
    voice "sp91_s1786_006"
    l "……You do care about me, Saito.{#sp91_s1786_006}"

    # ……なら、わたしはサイトを信じるわ。
    voice "sp91_s1786_007"
    l "……Then I'll trust you, Saito.{#sp91_s1786_007}"

    # ま、まって！だから簡単に信じないでって！
    voice "sp91_s1786_008"
    s "W-Wait! That's why I said don't trust me so easily!{#sp91_s1786_008}"

    # 耐えるハメになるのは俺なんだって！
    voice "sp91_s1786_009"
    s "I'm the one who ends up having to endure it!{#sp91_s1786_009}"

    # ……すぅ。
    voice "sp91_s1786_010"
    l "……Su.{#sp91_s1786_010}"

    # ……ね、寝るな！寝ないで！ちょっと！
    voice "sp91_s1786_011"
    s "……Hey, don't sleep! Don't fall asleep! Hey!{#sp91_s1786_011}"

    # ……うるさい。バカ犬。
    voice "sp91_s1786_012"
    l "……Noisy. Stupid dog.{#sp91_s1786_012}"

    # → next scene 1788
    jump sp91_scene_1788

label sp91_scene_1787:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+185, level=80]
    $ dissolve_fx("id(185)")
    # ……ば、罰なんですか、これ？
    voice "sp91_s1787_002"
    s "…P-Punishment? Is this a punishment?{#sp91_s1787_002}"

    # そ、そうよ！罰なんだからね！
    voice "sp91_s1787_003"
    l "T-That's right! Because it's a punishment!{#sp91_s1787_003}"

    # わ、分かりましたぁ。罰なんでしたら甘んじて受けますぅ。
    voice "sp91_s1787_004"
    s "O-Okay, I understand! If it's a punishment, I'll accept it without complaint!{#sp91_s1787_004}"

    # そ、それでいいのよ！
    voice "sp91_s1787_005"
    l "T-That's how it should be!{#sp91_s1787_005}"

    # ……。
    voice "sp91_s1787_006"
    s "…{#sp91_s1787_006}"

    # じゃ、じゃあね……。……おやすみ。サイト。
    voice "sp91_s1787_007"
    l "W-Well, see you then… …Good night, Saito.{#sp91_s1787_007}"

    # は、はい……ですぅ。
    voice "sp91_s1787_008"
    s "Y-Yes… I-I understand.{#sp91_s1787_008}"

    # → next scene 1788
    jump sp91_scene_1788

label sp91_scene_1788:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+185, level=80]
    $ dissolve_fx("id(185)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1789:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # そ、それはさすがに……ちょっと……。
    voice "sp91_s1789_002"
    s "T-That's… going a bit too far, even for me… I mean…{#sp91_s1789_002}"

    # なによっ。遠慮するものじゃないわ！
    voice "sp91_s1789_003"
    l "What was that? You shouldn't hold back!{#sp91_s1789_003}"

    # いや、そういう意味じゃないんですけどっ！恥ずかしいじゃないですか！
    voice "sp91_s1789_004"
    s "No, that's not what I meant! But it's embarrassing, isn't it?!{#sp91_s1789_004}"

    # な、なにが恥ずかしいのよっ！た、単に背中を流してあげるだけよ！勘違いしないでよねっ。
    voice "sp91_s1789_005"
    l "W-What's embarrassing about it?! I'm just washing your back! Don't get the wrong idea, okay?!{#sp91_s1789_005}"

    # 恥ずかしがってないで全部任せちゃえばいいのよっ！
    voice "sp91_s1789_006"
    l "Don't be shy — just leave it all to me!{#sp91_s1789_006}"

    # そ、そんな～～っ！
    voice "sp91_s1789_007"
    s "N-No wayyy!{#sp91_s1789_007}"

    # 男の子なんでしょ！堂々としてなさいっ！
    voice "sp91_s1789_008"
    l "You're a boy, aren't you?! Then carry yourself with confidence!{#sp91_s1789_008}"

    # → next scene 1792
    jump sp91_scene_1792

label sp91_scene_1790:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # それは、うれしいですけど……。
    voice "sp91_s1790_002"
    s "I'm glad to hear that… but…{#sp91_s1790_002}"

    # じゃあ、いいわね？
    voice "sp91_s1790_003"
    l "Then it's all right?{#sp91_s1790_003}"

    # い、いや、ちょっと待って！
    voice "sp91_s1790_004"
    s "N-No, wait a moment!{#sp91_s1790_004}"

    # み、見せるのは恥ずかしいというか……、心の準備というものが……ほら？
    voice "sp91_s1790_005"
    s "I-It's not just that showing it is embarrassing… I need to prepare myself mentally… you know?{#sp91_s1790_005}"

    # な、何を考えてるのよ！
    voice "sp91_s1790_006"
    l "W-What are you thinking about?!{#sp91_s1790_006}"

    # 男の子でしょ！堂々としなさいっ！
    voice "sp91_s1790_007"
    l "You're a boy, right?! Act boldly!{#sp91_s1790_007}"

    # はい……。
    voice "sp91_s1790_008"
    s "Yes…{#sp91_s1790_008}"

    # → next scene 1792
    jump sp91_scene_1792

label sp91_scene_1791:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # ……そ、それじゃお願いします。
    voice "sp91_s1791_002"
    s "…T-Then, please. Go ahead.{#sp91_s1791_002}"

    # ……え、ええ、いいわよ！
    voice "sp91_s1791_003"
    l "…Y-Yes, it's fine!{#sp91_s1791_003}"

    # ……。
    voice "sp91_s1791_004"
    s "…{#sp91_s1791_004}"

    # ……。
    voice "sp91_s1791_005"
    l "…{#sp91_s1791_005}"

    # え、ええと。
    voice "sp91_s1791_006"
    s "U-Um…{#sp91_s1791_006}"

    # な、なにかしら？
    voice "sp91_s1791_007"
    l "I-Is something wrong?{#sp91_s1791_007}"

    # → next scene 1792
    jump sp91_scene_1792

label sp91_scene_1792:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # な、なによ。顔を赤くしちゃって。何を想像してるのよっ！
    voice "sp91_s1792_002"
    l "W-What's with that red face? What are you imagining?!{#sp91_s1792_002}"

    # だ、だって……。
    voice "sp91_s1792_003"
    s "B-Because…{#sp91_s1792_003}"

    # 飼い主がバカ犬を洗ってあげるのに、なんの不思議があるっていうのよっ！変なこと考えちゃダメなんだからね！
    voice "sp91_s1792_004"
    l "A master washing her silly dog — what's strange about that?! Don't you go thinking weird things, you hear?!{#sp91_s1792_004}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # ………。……。…。[EVENT_CG event    image=+187, level=80][TRANS
    th "……… …… …{#sp91_s1792_008}"

    # ……ま、まったく、無駄に広い背中ね。
    voice "sp91_s1792_009"
    l "…Honestly, what a needlessly broad back.{#sp91_s1792_009}"

    # ……ちょ、ちょっと意外だわ。
    voice "sp91_s1792_010"
    l "…A-A bit surprising, actually.{#sp91_s1792_010}"

    # ……。
    voice "sp91_s1792_011"
    s "…{#sp91_s1792_011}"

    # （……な、なんで俺はこんなことになってるんだよ？）
    s "…Why the heck am I in this situation?{#sp91_s1792_012}"

    # ……。
    voice "sp91_s1792_013"
    l "…{#sp91_s1792_013}"

    # ……き、聞いてるの？洗いにくいわよ。反省しなさい！
    voice "sp91_s1792_014"
    l "…A-Are you listening? You're hard to wash like this! You should be ashamed!{#sp91_s1792_014}"

    # （お、俺にどうしろっていうんだよっ！）
    s "W-What does she want me to do?!{#sp91_s1792_015}"

    # ……ど、どう？こんな感じ？
    voice "sp91_s1792_016"
    l "…H-How's this? Like this?{#sp91_s1792_016}"

    # あ～～、もう少し強くてもいいかな？
    voice "sp91_s1792_017"
    s "Ahh~… a little harder might be good, actually?{#sp91_s1792_017}"

    # ……え、ええと、こうかしら？
    voice "sp91_s1792_018"
    l "…U-Um, like this?{#sp91_s1792_018}"

    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     hide, vibrate=14]
    # [SPRITE   lay5     hide, vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # （ぐわっ！そ、それは……）
    s "Gwah! T-That's…{#sp91_s1792_028}"

    # こうね！うふふ……。
    voice "sp91_s1792_029"
    l "Like this! Ufufu…{#sp91_s1792_029}"

    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # （……ぐはっ、そいつは力を入れすぎ！）【選択肢】ち、ちょっと痛いかも？ → scene 1793【選択肢】我慢
    s "…Guh! That was way too much force!{#sp91_s1792_039}"

label sp91_scene_1793:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # ……あの。ちょ、ちょっと痛いかも？
    voice "sp91_s1793_002"
    s "…U-Um. It might hurt a little?{#sp91_s1793_002}"

    # き、きゃあっ！
    voice "sp91_s1793_003"
    l "K-Kyaa!{#sp91_s1793_003}"

    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # ……ふ、振り向くんじゃないわよ！だ、黙って洗われてなさい！きれいにしてあげてるんだから！
    voice "sp91_s1793_005"
    l "…D-Don't turn around! J-Just be quiet and let me wash you! I'm making you nice and clean!{#sp91_s1793_005}"

    # ちょ……、ちょっと待って！
    voice "sp91_s1793_006"
    s "W-Wait… wait a second!{#sp91_s1793_006}"

    # ダメよ！我慢しなさいっ！
    voice "sp91_s1793_007"
    l "No! You have to put up with it!{#sp91_s1793_007}"

    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # ぐ、ぐあぁぁぁーーーーーっ！
    voice "sp91_s1793_017"
    s "G-Guaaaaaah!{#sp91_s1793_017}"

    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # → next scene 1796
    jump sp91_scene_1796

label sp91_scene_1794:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # （こんな一生懸命に洗ってくれてるんだし、が、我慢！我慢！）
    s "She's washing me so earnestly like this… I've got to endure! Endure!{#sp91_s1794_002}"

    # ……あら、まだ弱かった？
    voice "sp91_s1794_003"
    l "…Oh? Still too weak?{#sp91_s1794_003}"

    # あ、いや、そんなわけでは……。
    voice "sp91_s1794_004"
    s "Ah, no, that's not it…{#sp91_s1794_004}"

    # もう、遠慮なんてしなくていいから！
    voice "sp91_s1794_005"
    l "Come on, you don't need to hold back!{#sp91_s1794_005}"

    # ちょ、ちょっとまったーーっ！
    voice "sp91_s1794_006"
    s "W-Wait a sec—!{#sp91_s1794_006}"

    # ほらほら……。
    voice "sp91_s1794_007"
    l "Here, here…{#sp91_s1794_007}"

    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # ギ、ギニャャーーーっ！
    voice "sp91_s1794_017"
    s "G-Ginyaaaah!{#sp91_s1794_017}"

    # → next scene 1796
    jump sp91_scene_1796

label sp91_scene_1795:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # ええと、じゃあ攻守交代を……。
    voice "sp91_s1795_002"
    s "U-Um, then let's switch places…{#sp91_s1795_002}"

    # へ？交代って？
    voice "sp91_s1795_003"
    l "Huh? Switch?{#sp91_s1795_003}"

    # ……いや、ほら、俺ばかりでも悪いし。ルイズの背中も……。
    voice "sp91_s1795_004"
    s "…No, I mean, it's not right that only I get this. Louise's back too…{#sp91_s1795_004}"

    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # な、なんでそうなるのよ！
    voice "sp91_s1795_006"
    l "W-Why would it turn out like that?!{#sp91_s1795_006}"

    # だ、だまって洗われなさい！
    voice "sp91_s1795_007"
    l "J-Just shut up and let me wash you!{#sp91_s1795_007}"

    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # ギ、ギニャャーーーっ！
    voice "sp91_s1795_017"
    s "G-Ginyaaaah!{#sp91_s1795_017}"

    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # → next scene 1796
    jump sp91_scene_1796

label sp91_scene_1796:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # ……ふうっ！おしまい！
    voice "sp91_s1796_002"
    l "…Fuu! All done!{#sp91_s1796_002}"

    # これできれいになったでしょ！
    voice "sp91_s1796_003"
    l "You're all clean now, right?!{#sp91_s1796_003}"

    # ……きゅう。
    voice "sp91_s1796_004"
    s "…Kyuu.{#sp91_s1796_004}"

    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # ……もうっ、だらしないわね！
    voice "sp91_s1796_006"
    l "…Honestly, you're such a mess!{#sp91_s1796_006}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1797:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # （落ち着けるはずないだろ！）
    s "There's no way I could calm down!{#sp91_s1797_002}"

    # （……やっぱり、お風呂ってのはさ、のんびり入るもんなんだと思うんですよ）
    s "…After all, a bath is something you're supposed to relax in, I really think so.{#sp91_s1797_003}"

    # （……一日の垢をザァーっと落としてね。くてくてになるまでお湯に浸かって、体と心をほぐす）
    s "…Wash away the day's grime in one go, soak in the hot water until you're all wrinkled, and loosen up body and soul.{#sp91_s1797_004}"

    # （そして、風呂上りに飲む一杯の冷たい牛乳。ああ、日本に生まれて良かった。明日も頑張ろう！　と）
    s "And then, a cold glass of milk after the bath. Ah, I'm glad I was born in Japan. I'll do my best again tomorrow! — that's what I was thinking.{#sp91_s1797_005}"

    # ……それが！
    voice "sp91_s1797_006"
    s "…And yet!{#sp91_s1797_006}"

    # なんでこんな男の価値が試されるイベントになってるんだよ！
    voice "sp91_s1797_007"
    s "Why did this turn into some event that tests a man's worth?!{#sp91_s1797_007}"

    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # ……何か文句あるの？
    voice "sp91_s1797_009"
    l "…Got a complaint?{#sp91_s1797_009}"

    # → next scene 1800
    jump sp91_scene_1800

label sp91_scene_1798:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # （正直、怖いよ……）
    s "Honestly, I'm scared…{#sp91_s1798_002}"

    # （あのルイズがこんなサービスをしてくれるなんて……ありえない！）
    s "That Louise doing something like this for me… impossible!{#sp91_s1798_003}"

    # （……ワケ分かんないですよ。ホント）
    s "…I don't understand it at all. Really.{#sp91_s1798_004}"

    # （……もし他の女の子とかにバレたりしたら大変だよな）[EVENT_CG event    image=+188
    s "…That'd be terrible if another girl found out.{#sp91_s1798_005}"

    # ……なにか失礼なコト考えてるわね。
    voice "sp91_s1798_006"
    l "…You're thinking something rude, aren't you.{#sp91_s1798_006}"

    # → next scene 1800
    jump sp91_scene_1800

label sp91_scene_1799:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # （……踊るアホウに、なんとやら）
    s "…Like the dancing fool and the watching fool — or something.{#sp91_s1799_002}"

    # （楽しみで楽しみで……。こう、踊っちゃうよ。俺は！）
    s "I'm so happy, so happy… I just have to dance! Me, I mean!{#sp91_s1799_003}"

    # ふふ、ふふふふふ……。
    voice "sp91_s1799_004"
    s "Fufu, fufufufufu…{#sp91_s1799_004}"

    # [EVENT_CG event    image=+189, level=80]
    $ dissolve_fx("id(189)")
    # ……突然、ニヤけた顔をして踊り出すなんて大丈夫？
    voice "sp91_s1799_006"
    l "…Are you okay, suddenly breaking into a grin and starting to dance?{#sp91_s1799_006}"

    # → next scene 1800
    jump sp91_scene_1800

label sp91_scene_1800:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # さっきから見ていれば……。何をぶつぶつ言ってるの？
    voice "sp91_s1800_003"
    l "I've been watching you a while now… What are you muttering about?{#sp91_s1800_003}"

    # な、なんでもないでしゅ……って。
    voice "sp91_s1800_004"
    s "N-Nothing at all, I tell you…{#sp91_s1800_004}"

    # そういえば、そ、その水着は？
    voice "sp91_s1800_005"
    s "Now that I think of it… that swimsuit?{#sp91_s1800_005}"

    # [EVENT_CG event    image=+189, level=80]
    $ dissolve_fx("id(189)")
    # え、これ？ハルナからサイトの世界の水着だって聞いたんだけど……違ってた？
    voice "sp91_s1800_007"
    l "Eh, this? Haruna told me it's the kind of swimsuit they wear in Saito's world… Was I wrong?{#sp91_s1800_007}"

    # い、いやそれは間違ってないけど……。
    voice "sp91_s1800_008"
    s "N-No, it's not wrong, but…{#sp91_s1800_008}"

    # （す、スクール水着？）[EVENT_CG event    image=+187, level=80]
    s "A-A school swimsuit?{#sp91_s1800_009}"

    # 力加減とかの希望があれば聞いてあげるから、ちゃんと言うのよ？
    voice "sp91_s1800_010"
    l "If you have any preferences about how hard I scrub, I'll listen — so tell me properly, okay?{#sp91_s1800_010}"

    # ……り、了解です。
    voice "sp91_s1800_011"
    s "…U-Understood.{#sp91_s1800_011}"

    # （……ガキの頃とかは、よく親に洗ってもらったりしたけどさ）
    s "…When I was a kid, my parents used to wash me like this pretty often.{#sp91_s1800_012}"

    # （なんか懐かしい感じだよな）
    s "It feels kind of nostalgic, doesn't it?{#sp91_s1800_013}"

    # どう、サイト？こんな感じ？
    voice "sp91_s1800_014"
    l "How is it, Saito? Like this?{#sp91_s1800_014}"

    # ……え？あ、うん。
    voice "sp91_s1800_015"
    s "…Eh? Ah, yeah.{#sp91_s1800_015}"

    # どうしたのよ、ボ～～ッとして。……気持ちよすぎたのかしら？
    voice "sp91_s1800_016"
    l "What's wrong with you, spacing out like that? …Did it feel too good?{#sp91_s1800_016}"

        "Sorry. It just felt so good…{#sp91_c_1800_1801}":
            jump sp91_scene_1801
        "I-It did not feel good at all!{#sp91_c_1800_1802}":
            jump sp91_scene_1802
        "I was just thinking about when I was a kid…{#sp91_c_1800_1803}":
            jump sp91_scene_1803
label sp91_scene_1801:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # ご、ごめん。気持ちよくてつい。
    voice "sp91_s1801_002"
    s "S-Sorry. It just felt good, I couldn't help it.{#sp91_s1801_002}"

    # うふふ、仕方ないわね。
    voice "sp91_s1801_003"
    l "Ufufu. Can't be helped, I suppose.{#sp91_s1801_003}"

    # ……ほらほら、謝らなくていいから。続きよ続き！
    voice "sp91_s1801_004"
    l "…Come on, come on, you don't need to apologize. Continue, continue!{#sp91_s1801_004}"

    # う、うん。
    voice "sp91_s1801_005"
    s "Y-Yeah.{#sp91_s1801_005}"

    # ……でも、ちょっと意外だったな。ルイズにこんな風に背中流してもらって、リラックスできるなんて……。
    voice "sp91_s1801_006"
    s "…But I have to say, I'm a bit surprised. That I could relax with Louise washing my back like this…{#sp91_s1801_006}"

    # もっと緊張するって思ってた。
    voice "sp91_s1801_007"
    s "I thought I'd be much more nervous.{#sp91_s1801_007}"

    # [EVENT_CG event    image=+189, level=80]
    $ dissolve_fx("id(189)")
    # ……不思議ね。わたしもよ。
    voice "sp91_s1801_009"
    l "…Strange, isn't it. I feel the same way.{#sp91_s1801_009}"

    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # ……コホン。訂正。少しは緊張しなさい。
    voice "sp91_s1801_011"
    l "…Ahem. Correction. You should be at least a little nervous.{#sp91_s1801_011}"

    # このわたしが自ら洗ってあげてるんだからね。
    voice "sp91_s1801_012"
    l "After all, I'm the one washing you myself!{#sp91_s1801_012}"

    # → next scene 1804
    jump sp91_scene_1804

label sp91_scene_1802:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # き、気持ちよくなんてないぞ！
    voice "sp91_s1802_002"
    s "I-It's not like it feels good or anything!{#sp91_s1802_002}"

    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # ……よく言うわね。今のサイトの顔を鏡で見せてあげたいわ。
    voice "sp91_s1802_004"
    l "…Oh, really? I'd love to show you the face you're making right now, in a mirror.{#sp91_s1802_004}"

    # ううっ、それは勘弁……。
    voice "sp91_s1802_005"
    s "Ugh, spare me that…!{#sp91_s1802_005}"

    # ほんとにもう。
    voice "sp91_s1802_006"
    l "Honestly, really.{#sp91_s1802_006}"

    # → next scene 1804
    jump sp91_scene_1804

label sp91_scene_1803:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # 子供の頃のこと、ちょっと思い出したよ。
    voice "sp91_s1803_002"
    s "I was just reminded of something from when I was a kid.{#sp91_s1803_002}"

    # よくこうして親に洗ってもらったなあ、って。
    voice "sp91_s1803_003"
    s "How my parents used to wash me just like this, I thought.{#sp91_s1803_003}"

    # ……そう、サイトの家ではそうだったんだ。
    voice "sp91_s1803_004"
    l "…I see. So that's how it was at Saito's home.{#sp91_s1803_004}"

    # どこの家だってそんなもんだろう？
    voice "sp91_s1803_005"
    s "Every family does that, doesn't it?{#sp91_s1803_005}"

    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # ……き、貴族の家じゃそんなことしないわよ。
    voice "sp91_s1803_007"
    l "…N-No, nobles don't do things like that.{#sp91_s1803_007}"

    # そ、そうなの？
    voice "sp91_s1803_008"
    s "R-Really?{#sp91_s1803_008}"

    # ……ホントにもう！ご主人様がこんなことをしてあげるというありがたみを感じなさい！
    voice "sp91_s1803_009"
    l "…Honestly! You should be grateful that your master is doing this for you!{#sp91_s1803_009}"

    # ……は、は～～い！
    voice "sp91_s1803_010"
    s "…Y-Yes~~!{#sp91_s1803_010}"

    # → next scene 1804
    jump sp91_scene_1804

label sp91_scene_1804:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # （……ああ、でも本当に気持ちいいな）
    s "(…Ah, but it really does feel good. ………Hah……){#sp91_s1804_003}"

    # （……はぁ……）
    s "(…Ah, but it really does feel good. ………Hah……){#sp91_s1804_004}"

    # ……ｚｚｚ。
    voice "sp91_s1804_005"
    s "…zzz.{#sp91_s1804_005}"

    # サイト、どんな感じ？……サイト？
    voice "sp91_s1804_006"
    l "Saito, how does it feel? …Saito?{#sp91_s1804_006}"

    # ……ｚｚｚ。
    voice "sp91_s1804_007"
    s "…zzz.{#sp91_s1804_007}"

    # ……寝ちゃってる？
    voice "sp91_s1804_008"
    l "…Did you fall asleep?{#sp91_s1804_008}"

    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # ……な、なによ！ご主人様が一生懸命洗ってあげてるのに本人は気持ちよさそうにうたたね！？
    voice "sp91_s1804_010"
    l "…W-What!? Your master is working so hard washing you, and you're dozing off looking all pleased!?{#sp91_s1804_010}"

    # うわっうわわわっ！ご、ゴメン！気持ちよくて、つい！
    voice "sp91_s1804_011"
    s "Eep! S-Sorry! It felt so good, I just couldn't help it!{#sp91_s1804_011}"

    # ホントにもう！まあ、でも……思わず寝てしまうほど気持ち良かったんでしょ？
    voice "sp91_s1804_012"
    l "Honestly! Well, but… it felt so good you couldn't help falling asleep, didn't it?{#sp91_s1804_012}"

    # [EVENT_CG event    image=+189, level=80]
    $ dissolve_fx("id(189)")
    # うふふ、仕方ないわね。
    voice "sp91_s1804_014"
    l "Ufufu. It can't be helped, I suppose.{#sp91_s1804_014}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1805:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # も、もちろん！
    voice "sp91_s1805_003"
    s "O-Of course!{#sp91_s1805_003}"

    # はぁ、返事はいいけど……。……絶対に無理よね。だって、バカ犬だもの。
    voice "sp91_s1805_004"
    l "Hah, your answer's fine, but… …There's no way, is there. You're a dumb dog, after all.{#sp91_s1805_004}"

    # （し、信用されてない？俺？）
    s "(H-Huh? You don't believe me? Me?){#sp91_s1805_005}"

    # ……でも、いいわ。嘘でもそう言ってくれて。
    voice "sp91_s1805_006"
    l "…But it's fine. Even if it's a lie, you said it for me.{#sp91_s1805_006}"

    # い、いや。結構本気だったんですけど……。
    voice "sp91_s1805_007"
    s "N-No, I was actually quite serious, though…{#sp91_s1805_007}"

    # いいの、無理しなくても。サイトが我慢できるわけないものね。動けないくらいお仕置きしておこうかしら？
    voice "sp91_s1805_008"
    l "It's fine, you don't have to force yourself. There's no way Saito can hold back, right? Shall I punish you until you can't move?{#sp91_s1805_008}"

    # が、頑張りますので……。それはやめてください～～っ！
    voice "sp91_s1805_009"
    s "B-But I'll do my best…! Please, don't do that~~!{#sp91_s1805_009}"

    # うふふ。はい、よろしい。
    voice "sp91_s1805_010"
    l "Ufufu. Yes, that's good.{#sp91_s1805_010}"

    # → next scene 1808
    jump sp91_scene_1808

label sp91_scene_1806:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # ……ま、前向きに善処します。
    voice "sp91_s1806_003"
    s "…Well, I'll take a positive approach.{#sp91_s1806_003}"

    # 前向きに善処って何？もっともらしい言葉でごまかさないでよ。
    voice "sp91_s1806_004"
    l "What's that, 'a positive approach'? Don't fudge it with fancy words.{#sp91_s1806_004}"

    # ううっ、ごめんなさい。
    voice "sp91_s1806_005"
    s "Ugh, I'm sorry.{#sp91_s1806_005}"

    # ちゃんと反省するんだからね！
    voice "sp91_s1806_006"
    l "You'd better really reflect on this, you know!{#sp91_s1806_006}"

    # ……わ、分かりました。反省して努力しますぅ！
    voice "sp91_s1806_007"
    s "…I-I understand. I'll reflect and try harder!{#sp91_s1806_007}"

    # うふふ。はい、よろしい。
    voice "sp91_s1806_008"
    l "Ufufu. Yes, that's good.{#sp91_s1806_008}"

    # → next scene 1808
    jump sp91_scene_1808

label sp91_scene_1807:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # は、反省はしますけど……。他の女の子を見ないなんて……、無理じゃないかと？
    voice "sp91_s1807_003"
    s "I-I do feel remorse, but… Not looking at other girls… Isn't that impossible?{#sp91_s1807_003}"

    # ……ホント、バカ犬なんだから。こんなときは、嘘でもいいから女の子を安心させるものでしょ！
    voice "sp91_s1807_004"
    l "…You really are a dumb dog. At a time like this, you should put a girl at ease — even if it's a lie!{#sp91_s1807_004}"

    # ……ええと、そうなの？
    voice "sp91_s1807_005"
    s "…Um, is that so?{#sp91_s1807_005}"

    # ……で、でも。わたしにウソは許さないからね！
    voice "sp91_s1807_006"
    l "…B-But. I won't forgive lies to me, you know!{#sp91_s1807_006}"

    # ちょっ、それは横暴！
    voice "sp91_s1807_007"
    s "Hey, that's high-handed!{#sp91_s1807_007}"

    # いいのっ、これは命令なんだから！
    voice "sp91_s1807_008"
    l "It's fine — this is an order!{#sp91_s1807_008}"

    # ううっ……はい……。
    voice "sp91_s1807_009"
    s "Ugh… Yes…{#sp91_s1807_009}"

    # うふふ。はい、よろしい。
    voice "sp91_s1807_010"
    l "Ufufu. Yes, that's good.{#sp91_s1807_010}"

    # → next scene 1808
    jump sp91_scene_1808

label sp91_scene_1808:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # もうっ、ずいぶん汚れちゃったわね。
    voice "sp91_s1808_003"
    l "Jeez, you got awfully dirty, didn't you.{#sp91_s1808_003}"

    # （汚した原因はルイズだろ？）
    s "(The one who got me dirty is Louise, right?) ………。……。…。 (Hah, how did it come to this?) (So what's with that school swimsuit, anyway!){#sp91_s1808_004}"

    # ……これは、お風呂が必要ね。
    voice "sp91_s1808_005"
    l "…This calls for a bath, doesn't it.{#sp91_s1808_005}"

    # え？ま、ましゃか……。
    voice "sp91_s1808_006"
    s "Eh? N-No way…{#sp91_s1808_006}"

    # ……飼い主の責任として、バカ犬をキレイにしてあげないとね。
    voice "sp91_s1808_007"
    l "…As your owner, I have to clean up my dumb dog, don't I.{#sp91_s1808_007}"

    # ちょ、ちょっと待って～～っ！
    voice "sp91_s1808_008"
    s "W-Wait a second~~!{#sp91_s1808_008}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # ………。……。…。[EVENT_CG event    image=+187, level=80][TRANS
    th "(The one who got me dirty is Louise, right?) ………。……。…。 (Hah, how did it come to this?) (So what's with that school swimsuit, anyway!){#sp91_s1808_013}"

    # （はあ、なんでこんなことに？）
    s "(The one who got me dirty is Louise, right?) ………。……。…。 (Hah, how did it come to this?) (So what's with that school swimsuit, anyway!){#sp91_s1808_014}"

    # ……ねえ、サイト？どこかかゆいところはある？
    voice "sp91_s1808_015"
    l "…Say, Saito? Is there anywhere that itches?{#sp91_s1808_015}"

    # ええと……しょの……。
    voice "sp91_s1808_016"
    s "Um… the, uh… down there…{#sp91_s1808_016}"

    # （だから、そのスクール水着はなんだよ！）
    s "(The one who got me dirty is Louise, right?) ………。……。…。 (Hah, how did it come to this?) (So what's with that school swimsuit, anyway!){#sp91_s1808_017}"

    # どう？背中流すのもなかなか上手でしょ？
    voice "sp91_s1808_018"
    l "How's that? I'm pretty good at washing backs, aren't I?{#sp91_s1808_018}"

    # は、はぁい。お上手であります！
    voice "sp91_s1808_019"
    s "Y-Yes! Most excellent, it is!{#sp91_s1808_019}"

    # うふふ、ありがと！
    voice "sp91_s1808_020"
    l "Ufufu, thank you!{#sp91_s1808_020}"

    # ……さてと。
    voice "sp91_s1808_021"
    l "…Well, then.{#sp91_s1808_021}"

    # [EVENT_CG event    image=+189, level=80]
    $ dissolve_fx("id(189)")
    # ……じゃあ……次は前ね。
    voice "sp91_s1808_023"
    l "…Well, then… next is the front, okay?{#sp91_s1808_023}"

    # ……。
    voice "sp91_s1808_024"
    s "…{#sp91_s1808_024}"

    # ……へっ？
    voice "sp91_s1808_025"
    s "…Huh?{#sp91_s1808_025}"

    # [EVENT_CG event    image=+187, level=80]
    $ dissolve_fx("id(187)")
    # あらどうしたの？狐につままれたような顔をして……ふふっ。
    voice "sp91_s1808_027"
    l "My, what's wrong? You look like a fox has bewitched you… Fufu.{#sp91_s1808_027}"

    # いや、怖い聞き違いをしたな～～と。
    voice "sp91_s1808_028"
    s "No, I just thought I heard something terrifying~~.{#sp91_s1808_028}"

    # あら、そうだったの？
    voice "sp91_s1808_029"
    l "Oh, was that so?{#sp91_s1808_029}"

    # ……ご主人様の言葉を聞き違えたりなんかしちゃダメよ。
    voice "sp91_s1808_030"
    l "…You mustn't mishear your master's words, you know.{#sp91_s1808_030}"

    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # もう一度言うわね……『次は前よ』。
    voice "sp91_s1808_032"
    l "I'll say it once more… 'Next is the front.'{#sp91_s1808_032}"

        "W-Wait a sec!{#sp91_c_1808_1809}":
            jump sp91_scene_1809
        "I have no choice but to run{#sp91_c_1808_1810}":
            jump sp91_scene_1810
        "Ask boldly{#sp91_c_1808_1811}":
            jump sp91_scene_1811
label sp91_scene_1809:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # ちょ、ちょっと待ったぁ！
    voice "sp91_s1809_002"
    s "W-Wait a sec!{#sp91_s1809_002}"

    # き、きゃあっ！
    voice "sp91_s1809_003"
    l "E-Eep!{#sp91_s1809_003}"

    # ……ま、前ってなんだよ！
    voice "sp91_s1809_004"
    s "…What do you mean, 'the front'!{#sp91_s1809_004}"

    # 背中だけじゃつまらないの！
    voice "sp91_s1809_005"
    l "Just the back is boring!{#sp91_s1809_005}"

    # そこは俺が洗うので大丈夫です！
    voice "sp91_s1809_006"
    s "I'll wash that part myself, so it's fine!{#sp91_s1809_006}"

    # ……え、遠慮しなくてもいいじゃない！バカ犬のクセに！
    voice "sp91_s1809_007"
    l "…Eh? You don't have to hold back! For a dumb dog, you're awfully modest!{#sp91_s1809_007}"

    # ……バ、バカ！も、もう少し恥じらいというものを……！
    voice "sp91_s1809_008"
    s "…I-Idiot! Have a little more shame, would you…!{#sp91_s1809_008}"

    # なによっ！どこが恥ずかしいのよ！言ってみなさいよ。
    voice "sp91_s1809_009"
    l "What!? What's embarrassing about it!? Just say it!{#sp91_s1809_009}"

    # 言えるわけねーだろ！！
    voice "sp91_s1809_010"
    s "There's no way I can say it!!{#sp91_s1809_010}"

    # → next scene 1812
    jump sp91_scene_1812

label sp91_scene_1810:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # （ま、前ってなんだよ！……ダメだ。に、逃げ出すしかない！）
    s "(What do you mean, 'the front'! …No good. I-I have to run! B-But… I'm completely naked right now! …I-If I run like this, will I stay naked forever?){#sp91_s1810_002}"

    # （で、でも、俺って今、全裸じゃん！……こ、このまま、逃げ出したら一生裸？）
    s "(What do you mean, 'the front'! …No good. I-I have to run! B-But… I'm completely naked right now! …I-If I run like this, will I stay naked forever?){#sp91_s1810_003}"

    # ……もう、何逃げようとしてるのよ！
    voice "sp91_s1810_004"
    l "…Jeez, what are you trying to run away from!{#sp91_s1810_004}"

    # バ、バカ！恥じらいってものはないのか！
    voice "sp91_s1810_005"
    s "I-Idiot! Do you have no shame at all!{#sp91_s1810_005}"

    # むぅ、このまま逃げ出したりなんかしたら、大声をあげちゃうわよ？
    voice "sp91_s1810_006"
    l "Mm, if you run off like that, I'll scream, you know?{#sp91_s1810_006}"

    # い、陰謀だ！
    voice "sp91_s1810_007"
    s "I-It's a plot!{#sp91_s1810_007}"

    # ほらほら、遠慮せず……。
    voice "sp91_s1810_008"
    l "Come on, come on, don't hold back…{#sp91_s1810_008}"

    # や、やめろ～～っ！ルイズ～～っ！
    voice "sp91_s1810_009"
    s "S-Stop it~~! Louise~~!{#sp91_s1810_009}"

    # → next scene 1812
    jump sp91_scene_1812

label sp91_scene_1811:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # （だ、ダメだ。恥ずかしがったらおしまいだ）
    s "(N-No. If I let myself get embarrassed, it's over.){#sp91_s1811_002}"

    # え、え～と。じゃあ、お願いします。
    voice "sp91_s1811_003"
    s "U-Um. Well, then… please.{#sp91_s1811_003}"

    # [EVENT_CG event    image=+189, level=80]
    $ dissolve_fx("id(189)")
    # あ、あらそう？ずいぶん素直ね。そ、それでいいのよ。
    voice "sp91_s1811_005"
    l "O-Oh, really? You're being very obedient. T-That's fine with me.{#sp91_s1811_005}"

    # ……。
    voice "sp91_s1811_006"
    s "…{#sp91_s1811_006}"

    # ……。
    voice "sp91_s1811_007"
    l "…{#sp91_s1811_007}"

    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # ……もう！は、恥じらいってものはないの？
    voice "sp91_s1811_009"
    l "…Jeez! H-Have you no shame?{#sp91_s1811_009}"

    # そ、それはそっちだろう！
    voice "sp91_s1811_010"
    s "T-That's you!{#sp91_s1811_010}"

    # → next scene 1812
    jump sp91_scene_1812

label sp91_scene_1812:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+188, level=80]
    $ dissolve_fx("id(188)")
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [EVENT_CG event    hide]
    # [TRANS trans("crossfade", 1000)]
    # ………。……。…。[EVENT_CG event    image=+187, level=80][TRANS
    th "………。……。…。{#sp91_s1812_005}"

    # ……はいっ、おしまいっ！
    voice "sp91_s1812_006"
    l "…There, all done!{#sp91_s1812_006}"

    # ……うっ、ううう。
    voice "sp91_s1812_007"
    s "…Ugh. Uuuh.{#sp91_s1812_007}"

    # も、もうオムコにいけない……。
    voice "sp91_s1812_008"
    s "I-I can't go to Omuko ever again…{#sp91_s1812_008}"

    # [EVENT_CG event    image=+189, level=80]
    $ dissolve_fx("id(189)")
    # ……な、なによ。結局、ぎゃあぎゃあ大騒ぎして！わ、わたしだって恥ずかしかったんだからね！
    voice "sp91_s1812_010"
    l "…W-What!? You ended up making a huge fuss! I-I was embarrassed too, you know!{#sp91_s1812_010}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1813:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ルイズはかわいい。
    voice "sp91_s1813_002"
    s "Louise is cute.{#sp91_s1813_002}"

    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # え、ホントに？
    voice "sp91_s1813_004"
    l "Eh? Really?{#sp91_s1813_004}"

    # ルイズは本当にかわいい！
    voice "sp91_s1813_005"
    s "Louise is really cute!{#sp91_s1813_005}"

    # ……じゃあ、一番かわいい？
    voice "sp91_s1813_006"
    l "…Then, the cutest?{#sp91_s1813_006}"

    # そ、その問いにはまだノーコメントということで。
    voice "sp91_s1813_007"
    s "T-That question… I'll have to say 'no comment' for now.{#sp91_s1813_007}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # むーー。
    voice "sp91_s1813_009"
    l "Muuu~.{#sp91_s1813_009}"

    # （ワガママだったり乱暴だったりするけど……ルイズがかわいいのは本当だな。うん）
    s "(She's selfish and rough sometimes… but Louise really is cute. Yeah.){#sp91_s1813_010}"

    # むー。今、なんかぶつぶつ考えてる！
    voice "sp91_s1813_011"
    l "Muu. You're muttering about something just now!{#sp91_s1813_011}"

    # → next scene 1816
    jump sp91_scene_1816

label sp91_scene_1814:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ルイズもかわいい。
    voice "sp91_s1814_002"
    s "Louise is cute too.{#sp91_s1814_002}"

    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # え、ホントに？
    voice "sp91_s1814_004"
    l "Eh? Really?{#sp91_s1814_004}"

    # 俺はルイズも間違いなくかわいいと思ってるよ……くやしいけど。
    voice "sp91_s1814_005"
    s "I'm sure Louise is cute too… even if it galls me to admit it.{#sp91_s1814_005}"

    # うふふ。ありがとう、サイト。
    voice "sp91_s1814_006"
    l "Ufufu. Thank you, Saito.{#sp91_s1814_006}"

    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # ……でも。ルイズ『も』ってなに？
    voice "sp91_s1814_008"
    l "…But. What's this 'too' about, Louise?{#sp91_s1814_008}"

    # わ、わたしの使い魔だったら、わたしだけを見つめてなさいっ！
    voice "sp91_s1814_009"
    l "I-If you're my familiar, then look only at me!{#sp91_s1814_009}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # → next scene 1816
    jump sp91_scene_1816

label sp91_scene_1815:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ルイズはかわいいっ！
    voice "sp91_s1815_002"
    s "Louise is cute!{#sp91_s1815_002}"

    # かわいいよっ！
    voice "sp91_s1815_003"
    s "She's cute!{#sp91_s1815_003}"

    # （でも、貧乳が……）[EVENT_CG event    image=+191, level=80]
    s "(But… she's flat-chested…){#sp91_s1815_004}"

    # サイト……。……いま、何かとんでもないことを考えなかった？
    voice "sp91_s1815_005"
    l "Saito… …You weren't thinking something terrible just now, were you?{#sp91_s1815_005}"

    # [SPRITE   lay5     hide]
    # いえ、なにも。
    voice "sp91_s1815_007"
    s "No, nothing.{#sp91_s1815_007}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # → next scene 1816
    jump sp91_scene_1816

label sp91_scene_1816:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # もうっ、サイトったら。ちゃんとわたしをほめなさい！
    voice "sp91_s1816_002"
    l "Jeez, Saito. Praise me properly!{#sp91_s1816_002}"

    # （そんな、無茶な……）[EVENT_CG event    image=+191, level=80]
    s "(That's so unreasonable…){#sp91_s1816_003}"

    # な、なによ。不満？
    voice "sp91_s1816_004"
    l "W-What? Are you dissatisfied?{#sp91_s1816_004}"

    # い、いや。そんなことはないぞ。
    voice "sp91_s1816_005"
    s "N-No, that's not it at all.{#sp91_s1816_005}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ……ま、いいわ。じゃ、やってみなさい。さあ。
    voice "sp91_s1816_007"
    l "…Well, fine. Then try it. Go on.{#sp91_s1816_007}"

    # ルイズさま、最高～～っ！ブラボ～～！
    voice "sp91_s1816_008"
    s "Louise-sama, the best~~! Bravo~~!{#sp91_s1816_008}"

    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # ……本当にやる気あるの？サイト？
    voice "sp91_s1816_010"
    l "…Are you really serious, Saito?{#sp91_s1816_010}"

        "My noble Master!{#sp91_c_1816_1817}":
            jump sp91_scene_1817
        "That cuteness is a crime!{#sp91_c_1816_1818}":
            jump sp91_scene_1818
        "Master, it's moe-moe!{#sp91_c_1816_1819}":
            jump sp91_scene_1819
label sp91_scene_1817:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # ああ、気高き俺のご主人様！
    voice "sp91_s1817_002"
    s "Ah, my noble Master!{#sp91_s1817_002}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # 俺はご主人様の可憐な姿を見ると、いつも胸が高鳴り、心が引き裂かれそうです。
    voice "sp91_s1817_004"
    s "Whenever I see your lovely form, my heart races and feels like it's being torn in two.{#sp91_s1817_004}"

    # そのかわいさはほとんど犯罪です！
    voice "sp91_s1817_005"
    s "That cuteness is practically a crime!{#sp91_s1817_005}"

    # 最高です！俺の女神さまです！
    voice "sp91_s1817_006"
    s "It's wonderful! She's my goddess!{#sp91_s1817_006}"

    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # え、ええっ？も、もう。そこまで言わなくても……。
    voice "sp91_s1817_008"
    l "E-Eh? C-Come on. You don't have to go that far…{#sp91_s1817_008}"

    # でも、ええと……あ、ありがと。
    voice "sp91_s1817_009"
    l "But, um… Ah, thanks.{#sp91_s1817_009}"

    # → next scene 1820
    jump sp91_scene_1820

label sp91_scene_1818:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # ご主人様のそのかわいさは罪です！ほほえみさえ、罪っ！
    voice "sp91_s1818_002"
    s "Your cuteness is a crime! Even your smile is a crime!{#sp91_s1818_002}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ご主人様のたまに見せるツンツンは……。俺にとっては薔薇を守る棘。
    voice "sp91_s1818_004"
    s "The tsuntsun you show now and then… To me, they're the thorns that guard the rose.{#sp91_s1818_004}"

    # 俺の体とハートをどんなに傷つけるとしても……。
    voice "sp91_s1818_005"
    s "No matter how much it wounds my body and heart…{#sp91_s1818_005}"

    # その美しい薔薇の棘であれば、俺は甘んじて受けましょう！
    voice "sp91_s1818_006"
    s "If it's the thorns of that beautiful rose, I'll gladly accept them!{#sp91_s1818_006}"

    # （……なんだかギーシュになった気分だなあ）[EVENT_CG event    image=+192, lev
    s "(……Feels like I've become Guiche, somehow.){#sp91_s1818_007}"

    # ちょっと引っかかるところがなくもないけど。でも、ええと……あ、ありがと。
    voice "sp91_s1818_008"
    l "There's something a little bothersome, but… Still, um… Ah, thanks.{#sp91_s1818_008}"

    # → next scene 1820
    jump sp91_scene_1820

label sp91_scene_1819:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # ご主人様、萌え萌えですっ！
    voice "sp91_s1819_002"
    s "Master, it's moe-moe!{#sp91_s1819_002}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ご主人様のツンデレぶりに、このバカ犬はもうメロメロにメルトダウン！
    voice "sp91_s1819_004"
    s "Your tsundere ways have this dumb dog head over heels — meltdown!{#sp91_s1819_004}"

    # モエ？ツンデレ……メルトダウン？
    voice "sp91_s1819_005"
    l "Moe? Tsundere… Meltdown?{#sp91_s1819_005}"

    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # ……ど、どういう意味よ？
    voice "sp91_s1819_007"
    l "…Wh-What do you mean?{#sp91_s1819_007}"

    # （本当のことを言ったら、殺されそうだな……）
    s "(If I told the truth, I'd probably be killed…){#sp91_s1819_008}"

    # あ、いえ、自分の国の言葉で、可愛いってことです。
    voice "sp91_s1819_009"
    s "Ah, no — it means 'cute' in my country's language.{#sp91_s1819_009}"

    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # うふふ。そ、そんなぁ……。
    voice "sp91_s1819_011"
    l "Ufufu. N-No way…{#sp91_s1819_011}"

    # → next scene 1820
    jump sp91_scene_1820

label sp91_scene_1820:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # うふふ。サイトにしてはまんざらでもないわね。いいわ、今日のところは許してあげる。
    voice "sp91_s1820_002"
    l "Ufufu. For Saito, that's not bad at all. Fine — I'll forgive you, just for today.{#sp91_s1820_002}"

    # あ、ありがとうございます。
    voice "sp91_s1820_003"
    s "Ah, thank you very much.{#sp91_s1820_003}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ……あのね、サイト。
    voice "sp91_s1820_005"
    l "…Say, Saito.{#sp91_s1820_005}"

    # 素敵な男の子っていうのは、女の子をほめてあげるものなのよ。覚えておきなさい！
    voice "sp91_s1820_006"
    l "A wonderful boy praises a girl, you know. Remember that!{#sp91_s1820_006}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1821:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # ……え、遠慮します。
    voice "sp91_s1821_002"
    s "…Eh? I'll pass.{#sp91_s1821_002}"

    # 男が愛とか恋とか口に出していうのは、格好悪いっつーか、恥ずかしいっていうか……。
    voice "sp91_s1821_003"
    s "A man saying stuff like love or romance out loud is just… uncool, or rather embarrassing…{#sp91_s1821_003}"

    # あら、サイトは一生恋人がいなくてもいいのかしら？
    voice "sp91_s1821_004"
    l "My, my — is Saito fine with never having a lover his whole life?{#sp91_s1821_004}"

    # そ、そんな……。
    voice "sp91_s1821_005"
    s "Th-That's not…{#sp91_s1821_005}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ……格好をつけてる暇があったら、甘い言葉のひとつでも考えなさい！
    voice "sp91_s1821_007"
    l "…If you have time to act cool, think of at least one sweet word!{#sp91_s1821_007}"

    # ……ううっ。わ、分かりました。
    voice "sp91_s1821_008"
    s "…Ugh. I-I understand.{#sp91_s1821_008}"

    # → next scene 1824
    jump sp91_scene_1824

label sp91_scene_1822:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # あ、愛と情熱って……。
    voice "sp91_s1822_002"
    s "Ah, love and passion…{#sp91_s1822_002}"

    # 女の子はいつだって、気持ちを言葉という形にしてほしいものなの！
    voice "sp91_s1822_003"
    l "A girl always wants her feelings put into words!{#sp91_s1822_003}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ……本当に分かってる、サイト？
    voice "sp91_s1822_005"
    l "…Do you really understand, Saito?{#sp91_s1822_005}"

    # ええと、分かるような分かんないような……。
    voice "sp91_s1822_006"
    s "Um, I kind of get it, kind of don't…{#sp91_s1822_006}"

    # → next scene 1824
    jump sp91_scene_1824

label sp91_scene_1823:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # ……ギ、ギーシュみたいな感じでやればいいのかな？
    voice "sp91_s1823_002"
    s "…Should I do it the way Guiche does?{#sp91_s1823_002}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ……え？ギーシュ？
    voice "sp91_s1823_004"
    l "…Eh? Guiche?{#sp91_s1823_004}"

    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # ……だ、ダメよ！ギーシュよりもっと真剣な感じで！
    voice "sp91_s1823_006"
    l "…N-No! With even more feeling than Guiche!{#sp91_s1823_006}"

    # な、なんだか難しいぞ。
    voice "sp91_s1823_007"
    s "I-It seems kind of hard.{#sp91_s1823_007}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # → next scene 1824
    jump sp91_scene_1824

label sp91_scene_1824:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # と・に・か・く！まず、自分の気持ちを言葉にするの！
    voice "sp91_s1824_002"
    l "A-n-y-w-a-y! First, put your feelings into words!{#sp91_s1824_002}"

    # でも、女の子を傷つけるようなことは絶対に言っちゃダメ！たとえ嘘でもほめたたえるのっ！
    voice "sp91_s1824_003"
    l "But never say anything that hurts a girl! Even if it's a lie, praise her!{#sp91_s1824_003}"

    # ……な、なんか、矛盾してないか？
    voice "sp91_s1824_004"
    s "…Isn't that a bit contradictory?{#sp91_s1824_004}"

    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # うるさいわね！……とりあえず、お手本をあげるから朗読してみなさい！
    voice "sp91_s1824_006"
    l "Quiet, you!… Anyway, I'll give you an example — read it aloud!{#sp91_s1824_006}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # まず、わたしがやってみるわよ。
    voice "sp91_s1824_008"
    l "First, I'll show you how.{#sp91_s1824_008}"

    # ……は、はいです。
    voice "sp91_s1824_009"
    s "…Y-Yes, ma'am.{#sp91_s1824_009}"

    # たとえ嵐が吹いても、大波が荒れても、あなたがいれば関係ない。この恋の中で生きられるなら何もいらない。
    voice "sp91_s1824_010"
    l "Even if storms rage and great waves crash, as long as you're there it doesn't matter. If I can live in this love, I need nothing else.{#sp91_s1824_010}"

    # あなたが望むなら、国も捨てよう。杖も捨てよう。
    voice "sp91_s1824_011"
    l "If you wish it, I'll abandon my country. I'll cast away my wand, too.{#sp91_s1824_011}"

    # あなたと愛し合い、夢を見られるのなら、それでいい。
    voice "sp91_s1824_012"
    l "If I can love you and dream, that's enough.{#sp91_s1824_012}"

    # 荒海へとこぎだせる。大渦でも飛び込める。
    voice "sp91_s1824_013"
    l "I can row out into the raging sea. I can leap into a great whirlpool.{#sp91_s1824_013}"

    # あなたの瞳とぬくもりを信じられれば……、何だってできるのです。
    voice "sp91_s1824_014"
    l "If I can trust your eyes and your warmth… I can do anything.{#sp91_s1824_014}"

    # ……。
    voice "sp91_s1824_015"
    s "…{#sp91_s1824_015}"

    # ……どう？
    voice "sp91_s1824_016"
    l "…Well? How was it?{#sp91_s1824_016}"

    # うっ……や、やっぱり俺もやるの？
    voice "sp91_s1824_017"
    s "Ugh… D-Do I really have to do it too?{#sp91_s1824_017}"

        "Haltingly, but sincerely…{#sp91_c_1824_1825}":
            jump sp91_scene_1825
        "Manfully, with conviction{#sp91_c_1824_1826}":
            jump sp91_scene_1826
        "Acting cool{#sp91_c_1824_1827}":
            jump sp91_scene_1827
label sp91_scene_1825:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # たとえ嵐が吹いても、大波が荒れても、あなたがいれば関係ない。この恋の中で生きられるなら何もいらない。
    voice "sp91_s1825_002"
    s "Even if storms rage and great waves crash, as long as you're there it doesn't matter. If I can live in this love, I need nothing else.{#sp91_s1825_002}"

    # あなたが望むなら、国も捨てよう。杖も捨てよう。
    voice "sp91_s1825_003"
    s "If you wish it, I'll abandon my country. I'll cast away my wand, too.{#sp91_s1825_003}"

    # あなたと愛し合い、夢を見られるのなら、それでいい。
    voice "sp91_s1825_004"
    s "If I can love you and dream, that's enough.{#sp91_s1825_004}"

    # 荒海へとこぎだせる。大渦でも飛び込める。
    voice "sp91_s1825_005"
    s "I can row out into the raging sea. I can leap into a great whirlpool.{#sp91_s1825_005}"

    # あなたの瞳とぬくもりを信じられれば、何だってできるのです。
    voice "sp91_s1825_006"
    s "If I can trust your eyes and your warmth, I can do anything.{#sp91_s1825_006}"

    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # ……うふふ。
    voice "sp91_s1825_008"
    l "…Ufufu.{#sp91_s1825_008}"

    # ううっ、こっぱずかしいって。これ！
    voice "sp91_s1825_009"
    s "Ugh — this is way too embarrassing! Jeez!{#sp91_s1825_009}"

    # ……悪くなかったわよ。
    voice "sp91_s1825_010"
    l "…Not bad, you know.{#sp91_s1825_010}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # でも、もう少し照れないようにしてよ。聞いてるこっちが恥ずかしかったわよ！
    voice "sp91_s1825_012"
    l "But try not to blush so much. I was the one embarrassed, listening to you!{#sp91_s1825_012}"

    # が、頑張ります。
    voice "sp91_s1825_013"
    s "B-But I'll try!{#sp91_s1825_013}"

    # → next scene 1828
    jump sp91_scene_1828

label sp91_scene_1826:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # たとえ嵐が吹いても、大波が荒れても、あなたがいれば関係ない。この恋の中で生きられるなら何もいらない。
    voice "sp91_s1826_002"
    s "Even if storms rage and great waves crash, as long as you're there it doesn't matter. If I can live in this love, I need nothing else.{#sp91_s1826_002}"

    # あなたが望むなら、国も捨てよう。杖も捨てよう。
    voice "sp91_s1826_003"
    s "If you wish it, I'll abandon my country. I'll cast away my wand, too.{#sp91_s1826_003}"

    # あなたと愛し合い、夢を見られるのなら、それでいい。
    voice "sp91_s1826_004"
    s "If I can love you and dream, that's enough.{#sp91_s1826_004}"

    # 荒海へとこぎだせる。大渦でも飛び込める。
    voice "sp91_s1826_005"
    s "I can row out into the raging sea. I can leap into a great whirlpool.{#sp91_s1826_005}"

    # あなたの瞳とぬくもりを信じられれば、何だってできるのです。
    voice "sp91_s1826_006"
    s "If I can trust your eyes and your warmth, I can do anything.{#sp91_s1826_006}"

    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # ……ふ～ん。
    voice "sp91_s1826_008"
    l "…Hm~.{#sp91_s1826_008}"

    # こっぱずかしいって。これ！
    voice "sp91_s1826_009"
    s "So embarrassing, I tell you. This!{#sp91_s1826_009}"

    # 少し意外だったけど……悪くなかったわ。
    voice "sp91_s1826_010"
    l "It was a bit unexpected, but… not bad.{#sp91_s1826_010}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # でも……。最後に投げやりになってたでしょ？あれで台無しよ。
    voice "sp91_s1826_012"
    l "But… you got half-hearted at the end, didn't you? That spoiled it.{#sp91_s1826_012}"

    # ……次は、最後まで照れないようにしてよね。
    voice "sp91_s1826_013"
    l "…Next time, don't blush until the very end, okay?{#sp91_s1826_013}"

    # ううっ、頑張ります。
    voice "sp91_s1826_014"
    s "Ugh, I'll try.{#sp91_s1826_014}"

    # → next scene 1828
    jump sp91_scene_1828

label sp91_scene_1827:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # たとえ嵐が吹いても、大波が荒れても、あなたがいれば関係ない。この恋の中で生きられるなら何もいらない。
    voice "sp91_s1827_002"
    s "Even if storms rage and great waves crash, as long as you're there it doesn't matter. If I can live in this love, I need nothing else.{#sp91_s1827_002}"

    # あなたが望むなら、国も捨てよう。杖も捨てよう。
    voice "sp91_s1827_003"
    s "If you wish it, I'll abandon my country. I'll cast away my wand, too.{#sp91_s1827_003}"

    # あなたと愛し合い、夢を見られるのなら、それでいい。
    voice "sp91_s1827_004"
    s "If I can love you and dream, that's enough.{#sp91_s1827_004}"

    # 荒海へとこぎだせる。大渦でも飛び込める。
    voice "sp91_s1827_005"
    s "I can row out into the raging sea. I can leap into a great whirlpool.{#sp91_s1827_005}"

    # あなたの瞳とぬくもりを信じられれば、俺は……何だってできる。
    voice "sp91_s1827_006"
    s "If I can trust your eyes and your warmth, then I… I can do anything.{#sp91_s1827_006}"

    # ……う～ん。なにかしら、このムカムカ感は？
    voice "sp91_s1827_007"
    l "…Ugh. What's with this prickly feeling?{#sp91_s1827_007}"

    # どうしたんだい？俺のかわいいルイズ？
    voice "sp91_s1827_008"
    s "What's wrong? My cute Louise?{#sp91_s1827_008}"

    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # や、やめなさい。そういうのは！
    voice "sp91_s1827_010"
    l "S-Stop it! Not that sort of thing!{#sp91_s1827_010}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ほんとにもうっ！
    voice "sp91_s1827_012"
    l "Really, honestly!{#sp91_s1827_012}"

    # → next scene 1828
    jump sp91_scene_1828

label sp91_scene_1828:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1829:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ……気にしています。たぶん……きっと……。
    voice "sp91_s1829_002"
    s "…I care. Maybe… surely…{#sp91_s1829_002}"

    # ……最後の方のごにょごにょはなによ！？
    voice "sp91_s1829_003"
    l "…What was all that mumbling at the end!?{#sp91_s1829_003}"

    # だ、だって！そっちはどうなんだよ！
    voice "sp91_s1829_004"
    s "B-Because! What about you!?{#sp91_s1829_004}"

    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # な、なによ！女の子にそういうこと言わせる気っ！？
    voice "sp91_s1829_006"
    l "W-What!? You're making a girl say that!?{#sp91_s1829_006}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # → next scene 1832
    jump sp91_scene_1832

label sp91_scene_1830:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # 気にしてる…かも？
    voice "sp91_s1830_002"
    s "I care… maybe?{#sp91_s1830_002}"

    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # な、なによそれ！無責任よ！サイトの気持ちでしょ！
    voice "sp91_s1830_004"
    l "W-What's that supposed to mean! That's irresponsible! They're your own feelings, aren't they!?{#sp91_s1830_004}"

    # じ、自分の気持ちだからこそ分からないことだってあるんだよ！そっちこそどうなんだよ！
    voice "sp91_s1830_005"
    s "J-Just because they're my feelings doesn't mean I always understand them! What about you!?{#sp91_s1830_005}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # それは、その……。な、なによ！
    voice "sp91_s1830_007"
    l "That is, um… W-What!{#sp91_s1830_007}"

    # → next scene 1832
    jump sp91_scene_1832

label sp91_scene_1831:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # そもそも、質問の内容が正直、よく分からねーよ。
    voice "sp91_s1831_002"
    s "Besides, I honestly don't even understand the question.{#sp91_s1831_002}"

    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # そ、それは、その……。一緒にいるとドキドキしたり……。
    voice "sp91_s1831_004"
    l "I-It's, um… When you're with them, your heart races…{#sp91_s1831_004}"

    # ずっと一緒にいたいって感じたり、その人のためだったら何だってできちゃうと思えたりすることよ。
    voice "sp91_s1831_005"
    l "You feel like you want to be with them forever, and feel like you could do anything for them.{#sp91_s1831_005}"

    # ……逆に、その人が他の女の子と仲良くしてると、腹が立ったり悲しくなったりするの。
    voice "sp91_s1831_006"
    l "…And conversely, if that person gets close to another girl, you get angry or sad.{#sp91_s1831_006}"

    # じ、じゃあ……その……、ルイズは誰かに気があるのか？
    voice "sp91_s1831_007"
    s "S-So… um… Louise, is there someone you like?{#sp91_s1831_007}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # な、なによ！何がいいたいの！
    voice "sp91_s1831_009"
    l "W-What!? What are you trying to say!?{#sp91_s1831_009}"

    # → next scene 1832
    jump sp91_scene_1832

label sp91_scene_1832:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ……サイト、あなたには愛とか情熱とか大切なものが足りないわ。
    voice "sp91_s1832_002"
    l "…Saito, you're missing something important—love, passion, that sort of thing.{#sp91_s1832_002}"

    # （……そ、そうなのかな？）[EVENT_CG event    image=+192, level=80]
    s "…I-Is that really so, I wonder?{#sp91_s1832_003}"

    # ……ねえ、サイト。こういうお話を知ってる？
    voice "sp91_s1832_004"
    l "…Say, Saito. Do you know a story like that?{#sp91_s1832_004}"

    # ある騎士が美しい貴族のお姫さまに身分違いの恋をしたの。
    voice "sp91_s1832_005"
    l "A knight once fell in love with a beautiful noble princess—a love beyond their station.{#sp91_s1832_005}"

    # 貴族のお姫さまはその騎士に戯れに言ったわ。『千日間、部屋の窓の下で愛を語り続ければその思いに応えてあげる』って
    voice "sp91_s1832_006"
    l "The noble princess said to the knight, half in jest: 'If you speak of love beneath my room's window for a thousand days, I shall return your feelings.'{#sp91_s1832_006}"

    # その言葉を信じた騎士は毎晩愛を語りながら立ち続けたわ。
    voice "sp91_s1832_007"
    l "The knight believed those words and kept standing there every night, speaking of love.{#sp91_s1832_007}"

    # 雨の日も風の日も……そしてとうとう死んでしまった。
    voice "sp91_s1832_008"
    l "In rain and in wind… and at last he died.{#sp91_s1832_008}"

    # でも、騎士はそのあとも毎晩お姫さまのところに現れて愛を語り続けたの。幽霊になって。
    voice "sp91_s1832_009"
    l "But even after that, the knight appeared by the princess every night and went on speaking of love. As a ghost.{#sp91_s1832_009}"

    # ……このお話をどう思う？
    voice "sp91_s1832_010"
    l "…What do you make of that story?{#sp91_s1832_010}"

    # そのお話って、むしろ怪談なのでは……。
    voice "sp91_s1832_011"
    s "That story sounds more like a ghost story to me…{#sp91_s1832_011}"

    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # そ、そうじゃないでしょ！
    voice "sp91_s1832_013"
    l "T-That's not it, is it?!{#sp91_s1832_013}"

    # こういうお話に心動かされたりしない？そんな情熱はあなたにはないの？
    voice "sp91_s1832_014"
    l "Doesn't a story like that stir your heart? Don't you have that kind of passion?{#sp91_s1832_014}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # とにかく、熱く、情熱的に！愛の言葉をささげるのよっ！
    voice "sp91_s1832_016"
    l "In any case—ardently, passionately! Devote yourself to words of love!{#sp91_s1832_016}"

    # そんな、どうやって！
    voice "sp91_s1832_017"
    s "H-How am I supposed to do that?!{#sp91_s1832_017}"

    # じ、自分で考えなさい！
    voice "sp91_s1832_018"
    l "T-Think of it yourself!{#sp91_s1832_018}"

    # （そんな、むちゃくちゃな！）
    s "That's utterly unreasonable!{#sp91_s1832_019}"

    # ……いい？わたしの心を甘くとろけさせるのよ！
    voice "sp91_s1832_020"
    l "…Alright? You're going to melt my heart, sweet and slow!{#sp91_s1832_020}"

        "Give it your all, passionately?{#sp91_c_1832_1833}":
            jump sp91_scene_1833
        "Just wing it?{#sp91_c_1832_1834}":
            jump sp91_scene_1834
        "Recklessly…{#sp91_c_1832_1835}":
            jump sp91_scene_1835
label sp91_scene_1833:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # （頑張って情熱的に……って！そもそもどうすればいいんだよ！）
    s "Give it your all, passionately…! How am I even supposed to do that?!{#sp91_s1833_002}"

    # （思い出話を、適当にありがちなフレーズでつなげてけばいいんだよ、相棒）
    voice "sp91_s1833_003"
    th "Just string the old memories together with some run-of-the-mill phrases, partner.{#sp91_s1833_003}"

    # （そんなことをいわれても……）
    s "Even if you say that…{#sp91_s1833_004}"

    # （ちぇっ、耳を貸しな……ごにょごにょ）
    voice "sp91_s1833_005"
    th "Tch, do lend me an ear… mumble, mumble.{#sp91_s1833_005}"

    # え、ええと……。
    voice "sp91_s1833_006"
    s "E-Erm…{#sp91_s1833_006}"

    # ボクはあの日の契約を覚えている。目を閉じれば浮かぶその瞳の色……。
    voice "sp91_s1833_007"
    s "I remember the contract of that day. Close my eyes, and the color of those eyes comes to mind…{#sp91_s1833_007}"

    # 夏の日のような少女。まぶしい太陽。とどろく雷鳴。
    voice "sp91_s1833_008"
    s "A girl like a summer day. The dazzling sun. Roaring thunder.{#sp91_s1833_008}"

    # 夕立と虹。激しいきみは迷うボクの心を震わせた。
    voice "sp91_s1833_009"
    s "A passing shower and a rainbow. Fierce as you were, you shook my wandering heart.{#sp91_s1833_009}"

    # 大丈夫、ボク達は進んでいける。ボクはあの日の契約を覚えているから。
    voice "sp91_s1833_010"
    s "It's all right—we can keep moving forward. Because I remember the contract of that day.{#sp91_s1833_010}"

    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # ……。
    voice "sp91_s1833_012"
    l "…{#sp91_s1833_012}"

    # ……こ、こんな感じでよろしかったでしょうか？
    voice "sp91_s1833_013"
    s "…I-Is this to your liking?{#sp91_s1833_013}"

    # ……そうね。サイトにしては上出来かしら？
    voice "sp91_s1833_014"
    l "…Yes. Quite a good effort for Saito, wouldn't you say?{#sp91_s1833_014}"

    # なかなか悪くないわよ。
    voice "sp91_s1833_015"
    l "It's not bad at all.{#sp91_s1833_015}"

    # （……そ、そうなんでしゅか？）
    s "…R-Really? Are you sure?{#sp91_s1833_016}"

    # これからも精進しなさい。
    voice "sp91_s1833_017"
    l "Keep striving like that from now on, too.{#sp91_s1833_017}"

    # （なんか、複雑……）→ next scene 1836
    s "Somehow, it's all rather complicated… → next scene 1836{#sp91_s1833_018}"

label sp91_scene_1834:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # （とりあえず適当に……って、どんな感じにすればいいんだよ！）
    s "For now, just wing it… but what does that even look like?!{#sp91_s1834_002}"

    # （……相棒の国には吟遊詩人とかいなかったのかよ？）
    voice "sp91_s1834_003"
    th "…No wandering bards in your country, partner?{#sp91_s1834_003}"

    # （そりゃ、いたけど……ゲームの中だけど……）
    s "Well, there were… but only in games…{#sp91_s1834_004}"

    # ……サイト、まだなの？
    voice "sp91_s1834_005"
    l "…Saito, are you still working on it?{#sp91_s1834_005}"

    # ちょ、ちょっと待った！
    voice "sp91_s1834_006"
    s "W-Wait a second!{#sp91_s1834_006}"

    # （とりあえず、それっぽい歌詞とかで作ってみようか？）
    s "For now, maybe I should make up some lyrics that sound the part?{#sp91_s1834_007}"

    # 突然のあの日の出会い。あの日からすべては動き始めた。
    voice "sp91_s1834_008"
    s "That sudden meeting on that day. From that day on, everything began to move.{#sp91_s1834_008}"

    # 新しい世界に、傷つき壊れかけたボク。古い世界に、疲れ破れかけてたきみ。あの日の出会いだったね。
    voice "sp91_s1834_009"
    s "In a new world, I was wounded and nearly broken. In an old world, you were weary and nearly in tatters. That was our meeting, that day.{#sp91_s1834_009}"

    # ボクにはきみが、きみにはボクがいる。だからボク達は生きていられるんだ。
    voice "sp91_s1834_010"
    s "I have you, and you have me. That's why we can keep going.{#sp91_s1834_010}"

    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # ……う～ん、悪くないんだけど。なにか暗いわよ。
    voice "sp91_s1834_012"
    l "…Mm, it's not bad, but… something about it is dark.{#sp91_s1834_012}"

    # ……あ、あれ？
    voice "sp91_s1834_013"
    s "…H-Huh?{#sp91_s1834_013}"

    # ……む、難しいなぁ。
    voice "sp91_s1834_014"
    s "…Mm, this is tricky.{#sp91_s1834_014}"

    # → next scene 1836
    jump sp91_scene_1836

label sp91_scene_1835:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # （こ、こうなりゃヤケクソだ！）
    s "If it's come to this, I may as well go all out!{#sp91_s1835_002}"

    # ……ルイズ、愛してる。好きだ。
    voice "sp91_s1835_003"
    s "…Louise, I love you. I like you.{#sp91_s1835_003}"

    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # ちょっ、ちょっと！何を言いだすのよ！
    voice "sp91_s1835_005"
    l "W-Wait! What are you saying?!{#sp91_s1835_005}"

    # ……なんだよ。愛と情熱の言葉を語りかけろって言ったのは、そっちだろ！
    voice "sp91_s1835_006"
    s "What the—? You're the one who told me to speak words of love and passion!{#sp91_s1835_006}"

    # そ、そうだけど……。
    voice "sp91_s1835_007"
    l "T-That's true, but…{#sp91_s1835_007}"

    # [EVENT_CG event    image=+190, level=80]
    $ dissolve_fx("id(190)")
    # ……き、貴婦人に愛を語るには修辞ってものが大切だって言ってるの！
    voice "sp91_s1835_009"
    l "…I'm telling you that when you speak of love to a noble lady, rhetoric matters!{#sp91_s1835_009}"

    # でも、俺は貴族じゃなくて平民だし。
    voice "sp91_s1835_010"
    s "But I'm not a noble—I'm a commoner.{#sp91_s1835_010}"

    # そ、そんな言い方しなくても……。
    voice "sp91_s1835_011"
    l "Y-You don't have to say it like that…{#sp91_s1835_011}"

    # それとも、ご主人様はこういう愛の言葉はお嫌いで？
    voice "sp91_s1835_012"
    s "Or does my mistress dislike this kind of love talk?{#sp91_s1835_012}"

    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # そんなこと言ってないでしょ！……も、もう！
    voice "sp91_s1835_014"
    l "I never said any such thing!…S-Stop it!{#sp91_s1835_014}"

    # あっはっは、見事に一本とられたようだな。貴族の娘っ子！
    voice "sp91_s1835_015"
    th "Aha ha! Nicely done—you've been neatly outwitted there, little noble lass!{#sp91_s1835_015}"

    # [EVENT_CG event    image=+191, level=80]
    $ dissolve_fx("id(191)")
    # う、うるさい！なによ、２人とも馬鹿にして！
    voice "sp91_s1835_017"
    l "S-Shut up! What's with you two, making fun of me?!{#sp91_s1835_017}"

    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # ……もう、いいもん。じゃあ、サイト。もう一度言って……。今度は心から真剣にね。
    voice "sp91_s1835_019"
    l "…Oh, fine. Then, Saito. Say it once more… This time, from the bottom of your heart.{#sp91_s1835_019}"

    # ……え？
    voice "sp91_s1835_020"
    s "…Huh?{#sp91_s1835_020}"

    # ……ちゃんと言ってくれるわよね。サイト？
    voice "sp91_s1835_021"
    l "…You'll say it properly for me, won't you? Saito?{#sp91_s1835_021}"

    # → next scene 1836
    jump sp91_scene_1836

label sp91_scene_1836:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+192, level=80]
    $ dissolve_fx("id(192)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay19    hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1837:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # ……カ、カップルがやるというあれ？端と端を咥えて。
    voice "sp91_s1837_002"
    s "…T-That thing couples do? Biting each end.{#sp91_s1837_002}"

    # し、知ってるの、サイト！？……い、いやらしい！
    voice "sp91_s1837_003"
    l "Y-You know about it, Saito!?…H-Lewd!{#sp91_s1837_003}"

    # そ、そっちはどうなんだよっ！
    voice "sp91_s1837_004"
    s "W-What about you, then?!{#sp91_s1837_004}"

    # わっ、わたしはキュルケに聞くまで知らなかったもの。
    voice "sp91_s1837_005"
    l "I… I didn't know until Kirche told me.{#sp91_s1837_005}"

    # さあっ、わたしがこっちの端を咥えるから……、サイトがそっちから……食べるのよ？
    voice "sp91_s1837_006"
    l "Here, I'll bite this end… and you eat from that end, Saito?{#sp91_s1837_006}"

    # → next scene 1840
    jump sp91_scene_1840

label sp91_scene_1838:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # ど、どうやって？
    voice "sp91_s1838_002"
    s "H-How?{#sp91_s1838_002}"

    # な、なによ！
    voice "sp91_s1838_003"
    l "W-What?!{#sp91_s1838_003}"

    # だから、わたしがこっちの端を咥えて、サイトが……そっちからその……。
    voice "sp91_s1838_004"
    l "I mean, I bite this end, and you… from that end, that…{#sp91_s1838_004}"

    # （や、やっぱりーーっ！）→ next scene 1840
    s "N-No way——! → next scene 1840{#sp91_s1838_005}"

label sp91_scene_1839:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # まさか……足で？
    voice "sp91_s1839_002"
    s "Surely not… with your foot?{#sp91_s1839_002}"

    # （……ヨガの奥義とか？）
    s "…Some kind of yoga secret art?{#sp91_s1839_003}"

    # ……ホントに試してみる？
    voice "sp91_s1839_004"
    l "…You're really going to try it?{#sp91_s1839_004}"

    # ごめんなさい。
    voice "sp91_s1839_005"
    s "I'm sorry.{#sp91_s1839_005}"

    # あのね、これは２人で端と端を咥えるものなの。
    voice "sp91_s1839_006"
    l "You see, it's something two people bite at either end.{#sp91_s1839_006}"

    # → next scene 1840
    jump sp91_scene_1840

label sp91_scene_1840:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+193, level=80]
    $ dissolve_fx("id(193)")
    # [TRANS trans("crossfade", 1000)]
    # （ええと。な、なんというか……）
    s "Um. H-How should I put this…{#sp91_s1840_007}"

    # （ポッチー１本分の長さの先に、ルイズの顔があるわけで……）
    s "One stick's length away, and Louise's face is right there…{#sp91_s1840_008}"

    # （お、お互いの呼吸を感じちゃう距離というか……）
    s "It's close enough that I can feel each other's breathing…{#sp91_s1840_009}"

    # （ルイズの髪が鼻に当たってこそばゆい）
    s "Louise's hair brushes my nose and tickles.{#sp91_s1840_010}"

    # ひ、緊張するな。
    voice "sp91_s1840_011"
    s "H-Hey, I'm getting nervous here.{#sp91_s1840_011}"

    # ふぁ、何よ！
    voice "sp91_s1840_012"
    l "Fwa, what?!{#sp91_s1840_012}"

    # （ルイズ、頬が少し上気してる……やっぱりかわいいよなあ）
    s "Louise's cheeks are a little flushed… she's adorable as ever.{#sp91_s1840_013}"

    # ふぁ、じゃあ。いっ、いくわよ！
    voice "sp91_s1840_014"
    l "Fwa, well then. H-Here we go!{#sp91_s1840_014}"

    # （そういえば、なんでこんなことに？）
    s "Come to think of it, how did we end up like this?{#sp91_s1840_015}"

    # う、んんっっ！
    voice "sp91_s1840_016"
    l "M-Mmnh!{#sp91_s1840_016}"

    # （うわっ、ルイズと目が合っちゃった！）【選択肢】奇襲作戦！ → scene 1841【選択肢】持久作戦！ → 
    s "Eep—! My eyes met Louise's!【Choice】Surprise attack! → scene 1841【Choice】War of attrition! → scene 1842【Choice】Suicide charge! → scene 1843{#sp91_s1840_017}"

label sp91_scene_1841:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+193, level=80]
    $ dissolve_fx("id(193)")
    # （……先手必勝！一気にルイズの側に攻め込んでやる！）
    s "…First strike wins! I'll charge straight at Louise all at once!{#sp91_s1841_002}"

    # ひゃっ、ひゃほふっ！
    voice "sp91_s1841_003"
    l "Hya——! Hya-ho-fu!{#sp91_s1841_003}"

    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # ────ポッキン。[SPRITE   lay1     hide][SPRITE   lay5     hid
    th "────Snap.{#sp91_s1841_005}"

    # も、もうっ！いきなり何するのよっ！びっくりするじゃないっ！
    voice "sp91_s1841_006"
    l "H-Hey! What were you thinking, doing that out of nowhere?! You made me jump!{#sp91_s1841_006}"

    # そ、そっちが緊張してたのが悪いんじゃねえか！
    voice "sp91_s1841_007"
    s "I-It's your own fault for being so nervous, isn't it?!{#sp91_s1841_007}"

    # → next scene 1844
    jump sp91_scene_1844

label sp91_scene_1842:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+193, level=80]
    $ dissolve_fx("id(193)")
    # （焦るな。焦るなよ……俺っ……！待っていればチャンスは……）
    s "Don't panic. Don't panic, me…! If I wait, my chance will…{#sp91_s1842_002}"

    # あっ！
    voice "sp91_s1842_003"
    l "Ah!{#sp91_s1842_003}"

    # へっ？
    voice "sp91_s1842_004"
    s "Heh?{#sp91_s1842_004}"

    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # ────ポッキン。[SPRITE   lay1     hide][SPRITE   lay5     hid
    th "────Snap.{#sp91_s1842_006}"

    # （そんなっ！もうおしまいっ！？お、俺のドキドキを返せぇっ！）
    s "No way! It's over already!? G-Give me back my pounding heart!{#sp91_s1842_007}"

    # ご、ごめん。
    voice "sp91_s1842_008"
    l "S-Sorry.{#sp91_s1842_008}"

    # ううっ、緊張のしすぎだよな。お互い……。
    voice "sp91_s1842_009"
    s "Ugh, I overdid the nervousness. Both of us…{#sp91_s1842_009}"

    # → next scene 1844
    jump sp91_scene_1844

label sp91_scene_1843:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+193, level=80]
    $ dissolve_fx("id(193)")
    # （ポッチーなぞはただの小道具！本丸はルイズの……）
    s "The stick is just a prop! The real thing is Louise's…{#sp91_s1843_002}"

    # （俺はやる。やってやるぜっ！）
    s "I'll do it. I'll show her!{#sp91_s1843_003}"

    # ひゃっ！
    voice "sp91_s1843_004"
    l "Hya!{#sp91_s1843_004}"

    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # ────ポッキン。[SPRITE   lay1     hide][SPRITE   lay5     hid
    th "────Snap.{#sp91_s1843_006}"

    # いたたた……。
    voice "sp91_s1843_007"
    s "Ow ow…{#sp91_s1843_007}"

    # さ、サイト大丈夫？
    voice "sp91_s1843_008"
    l "S-Saito, are you all right?{#sp91_s1843_008}"

    # もう、いきなり突っ込んでくるから……。口の中に当たっちゃったのよ。
    voice "sp91_s1843_009"
    l "Honestly, charging in so suddenly… It hit the inside of my mouth.{#sp91_s1843_009}"

    # （ポッチー恐るべし……）
    s "…That stick is terrifying…{#sp91_s1843_010}"

    # 何がしたかったの？
    voice "sp91_s1843_011"
    l "What were you trying to do?{#sp91_s1843_011}"

    # い、いやなにも……。というか、ルイズが緊張するから……。
    voice "sp91_s1843_012"
    s "N-No, nothing… I mean, you're nervous too, so…{#sp91_s1843_012}"

    # → next scene 1844
    jump sp91_scene_1844

label sp91_scene_1844:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # べ、別に緊張なんてしてないんだから！
    voice "sp91_s1844_002"
    l "I-I'm not nervous at all!{#sp91_s1844_002}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1845:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # ２人が最後まで折らずに食べたら、どうなるんでしょう？
    voice "sp91_s1845_002"
    s "What happens if we both make it to the end without breaking it?{#sp91_s1845_002}"

    # ……。
    voice "sp91_s1845_003"
    l "…{#sp91_s1845_003}"

    # な、なな、何を考えてるのよ！
    voice "sp91_s1845_004"
    l "W-What are you thinking about?!{#sp91_s1845_004}"

    # そんなことを考えるのは禁止よ！
    voice "sp91_s1845_005"
    l "Thinking about that is forbidden!{#sp91_s1845_005}"

    # そ、そんな無茶苦茶な！
    voice "sp91_s1845_006"
    s "T-That's completely unreasonable!{#sp91_s1845_006}"

    # → next scene 1848
    jump sp91_scene_1848

label sp91_scene_1846:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # よ、よろこんで。
    voice "sp91_s1846_002"
    s "W-With pleasure.{#sp91_s1846_002}"

    # げ、ゲームなんだからね。
    voice "sp91_s1846_003"
    l "I-It's just a game, okay?{#sp91_s1846_003}"

    # でも、ゲームなんだから……。事故があっても怒らないようにするわ。
    voice "sp91_s1846_004"
    l "But since it's just a game… I won't get angry even if something happens.{#sp91_s1846_004}"

    # え、それって？
    voice "sp91_s1846_005"
    s "Eh? What do you mean?{#sp91_s1846_005}"

    # さ、さあ……いくんだからね……。
    voice "sp91_s1846_006"
    l "C-Come on… let's go…{#sp91_s1846_006}"

    # → next scene 1848
    jump sp91_scene_1848

label sp91_scene_1847:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # か、勘弁してください。
    voice "sp91_s1847_002"
    s "C-Cut me some slack, please.{#sp91_s1847_002}"

    # な、なんですって！
    voice "sp91_s1847_003"
    l "W-What was that?!{#sp91_s1847_003}"

    # い、いや、なんというか……。理性に自信がないかな～～！なんて。
    voice "sp91_s1847_004"
    s "N-No, I mean… I was just wondering if I can trust my own self-control, or something.{#sp91_s1847_004}"

    # ……。
    voice "sp91_s1847_005"
    l "…{#sp91_s1847_005}"

    # ……最初からあなたの理性なんてこれっぽっちも信用してないわよ。バカ犬。
    voice "sp91_s1847_006"
    l "…I never trusted your self-control one bit, you know. Stupid dog.{#sp91_s1847_006}"

    # 普段は本能ばっかりで生きてるくせに……もうっ！
    voice "sp91_s1847_007"
    l "You live on nothing but instinct every other day… Geez!{#sp91_s1847_007}"

    # → next scene 1848
    jump sp91_scene_1848

label sp91_scene_1848:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+193, level=80]
    $ dissolve_fx("id(193)")
    # [TRANS trans("crossfade", 1000)]
    # ……。
    voice "sp91_s1848_007"
    s "…{#sp91_s1848_007}"

    # ……。
    voice "sp91_s1848_008"
    l "…{#sp91_s1848_008}"

    # （ポッチー１本分の先にルイズがいる……）
    s "(Louise is just one pocky stick away…){#sp91_s1848_009}"

    # （息苦しいっていうか……）
    s "(It's more like I can't breathe…){#sp91_s1848_010}"

    # （ルイズが上気して……）【選択肢】ルイズの名前を囁いてみる → scene 1849【選択肢】……集中！ → 
    s "(Louise is flushing…){#sp91_s1848_011}"

label sp91_scene_1849:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+193, level=80]
    $ dissolve_fx("id(193)")
    # ……ルイズぅ……。
    voice "sp91_s1849_002"
    s "…Louise…{#sp91_s1849_002}"

    # ……サイトぉ？
    voice "sp91_s1849_003"
    l "…Saito?{#sp91_s1849_003}"

    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # ────ポッキン。[SPRITE   lay1     hide][SPRITE   lay5     hid
    th "────Snap.{#sp91_s1849_005}"

    # ……って。き、きゃあっ！え、ええと。ご、ごめんなさいっ！
    voice "sp91_s1849_006"
    l "…Huh? E-Eep! U-Um… I-I'm sorry!{#sp91_s1849_006}"

    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [SE       se0      play=+58]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # ……ルイズ？あ、あれ？一体どうしたんだろう……。
    voice "sp91_s1849_012"
    s "…Louise? Huh? What just happened…?{#sp91_s1849_012}"

    # → next scene 1852
    jump sp91_scene_1852

label sp91_scene_1850:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+193, level=80]
    $ dissolve_fx("id(193)")
    # （こ、このポッチーを食べきったら……、その先にはルイズの……。ど、どうしよう！）[VIBRATE vibrat
    s "(If I finish this pocky stick… then right after that comes Louise's… W-What do I do!){#sp91_s1850_002}"

    # ────ポッキン。[SPRITE   lay1     hide][SPRITE   lay5     hid
    th "────Snap.{#sp91_s1850_003}"

    # きっ、きゃあああぁぁっっ！！
    voice "sp91_s1850_004"
    l "K-Kyaaaaah!!{#sp91_s1850_004}"

    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     hide, vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # ぐ、ぐはっ！
    voice "sp91_s1850_015"
    s "G-Guh!{#sp91_s1850_015}"

    # え、ええと。あのっ。ご、ごめんなさいっ！
    voice "sp91_s1850_016"
    l "U-Um. Ah. I-I'm sorry!{#sp91_s1850_016}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [SE       se0      play=+58]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # なんで、怒られるの？
    voice "sp91_s1850_023"
    s "Why are you mad at me?{#sp91_s1850_023}"

    # → next scene 1852
    jump sp91_scene_1852

label sp91_scene_1851:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+193, level=80]
    $ dissolve_fx("id(193)")
    # （ポッチーはあと半分……その先には……る、ルイズの……が……）
    s "(Half the pocky left… and beyond that is… L-Louise's…){#sp91_s1851_002}"

    # （こ、ここは思い切って一気に勝負に……）
    s "(Here I should just take the plunge and settle it in one go…){#sp91_s1851_003}"

    # ……サ、サイトっ！
    voice "sp91_s1851_004"
    l "…S-Saito!{#sp91_s1851_004}"

    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # ────ポッキン。[SPRITE   lay1     hide][SPRITE   lay5     hid
    th "────Snap.{#sp91_s1851_006}"

    # きっ、きゃあああぁぁっっ！！
    voice "sp91_s1851_007"
    l "K-Kyaaaaah!!{#sp91_s1851_007}"

    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     hide, vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # あ、あのっ。ええっと……ご、ごめんなさいっ！
    voice "sp91_s1851_018"
    l "A-Ah. Um… I-I'm sorry!{#sp91_s1851_018}"

    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [SE       se0      play=+58]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # そ、そりゃないよ～～！
    voice "sp91_s1851_024"
    s "T-That's not fair…!{#sp91_s1851_024}"

    # → next scene 1852
    jump sp91_scene_1852

label sp91_scene_1852:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [COFFEE]
    $ pause(1.0)
label sp91_scene_1853:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # ちょっと恥ずかしい気が……。
    voice "sp91_s1853_002"
    s "I'm feeling a little embarrassed…{#sp91_s1853_002}"

    # は、恥ずかしいってなによ！
    voice "sp91_s1853_003"
    l "What's so embarrassing about that?!{#sp91_s1853_003}"

    # な、なんでもないです。
    voice "sp91_s1853_004"
    s "I-It's nothing.{#sp91_s1853_004}"

    # （お、男がそういう甘ったるいことをするのにはちょっぴり勇気がいるんだよ！）
    s "(Hey, it takes a little courage for a guy to do something so sweet!){#sp91_s1853_005}"

    # （ま、まあ、いいよな。ここなら誰も見てないし……）
    s "(W-Well, it's fine. Nobody can see us here…){#sp91_s1853_006}"

    # ……。
    voice "sp91_s1853_007"
    th "…{#sp91_s1853_007}"

    # デルフ、ちょっと廊下に出すぞ。
    voice "sp91_s1853_008"
    s "Derf, I'm putting you out in the hallway for a bit.{#sp91_s1853_008}"

    # ……気付いたか。いいじゃねえかよぉ。相棒。
    voice "sp91_s1853_009"
    th "…You noticed, did you? No harm in it, partner.{#sp91_s1853_009}"

    # → next scene 1856
    jump sp91_scene_1856

label sp91_scene_1854:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # う、うまくいったときは？
    voice "sp91_s1854_002"
    s "A-And if it goes well?{#sp91_s1854_002}"

    # ……な、なによ。なにかご褒美でも欲しいの？
    voice "sp91_s1854_003"
    l "…W-What? Do you want a reward or something?{#sp91_s1854_003}"

    # ……え、ええと。
    voice "sp91_s1854_004"
    s "…U-Um.{#sp91_s1854_004}"

    # ゲームだからご褒美はなしよ。
    voice "sp91_s1854_005"
    l "It's a game, so no rewards.{#sp91_s1854_005}"

    # ……そ、そのかわり。……じ、事故が起きても、怒らないでいてあげるわ。
    voice "sp91_s1854_006"
    l "…B-But instead… I won't get mad even if something happens.{#sp91_s1854_006}"

    # へ？じ、事故って？
    voice "sp91_s1854_007"
    s "Huh? An accident?{#sp91_s1854_007}"

    # そ、そのかわりっ！ちゃ、ちゃんと真剣にやるんだからねっ。
    voice "sp91_s1854_008"
    l "T-That's the deal! And you'd better take it seriously, okay?!{#sp91_s1854_008}"

    # なに１人でヒートアップしてるんですか！
    voice "sp91_s1854_009"
    s "Why are you getting all worked up by yourself?!{#sp91_s1854_009}"

    # → next scene 1856
    jump sp91_scene_1856

label sp91_scene_1855:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # い、いや、でも。そんな……まさか……。
    voice "sp91_s1855_002"
    s "N-No, but… that's… no way…{#sp91_s1855_002}"

    # な、なな、何を身悶えてるのよ！気持ち悪いでしょ？
    voice "sp91_s1855_003"
    l "W-What are you squirming like that for?! It's creepy, you know?{#sp91_s1855_003}"

    # す、すいませんでした。犬の分際で大それた夢を見てしまったようです。
    voice "sp91_s1855_004"
    s "I-I'm sorry. I'm only a dog, and I let myself have too audacious a dream.{#sp91_s1855_004}"

    # ……え、ちょ、ちょっと！待ちなさい！どういうことを想像したのよ！
    voice "sp91_s1855_005"
    l "…Eh? W-Wait! Hold on! What exactly were you imagining?!{#sp91_s1855_005}"

    # → next scene 1856
    jump sp91_scene_1856

label sp91_scene_1856:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [SPRITE   lay19    hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+193, level=80]
    $ dissolve_fx("id(193)")
    # [TRANS trans("crossfade", 1000)]
    # ほ、ほらっ！……準備はいいっ？
    voice "sp91_s1856_008"
    l "H-Here! …Ready?{#sp91_s1856_008}"

    # ……。
    voice "sp91_s1856_009"
    s "…{#sp91_s1856_009}"

    # ……。
    voice "sp91_s1856_010"
    l "…{#sp91_s1856_010}"

    # （……うわわっ、間近でルイズと目が合っちゃった）
    s "(…Eep, I locked eyes with Louise up close!){#sp91_s1856_011}"

    # ……め、目は閉じて！
    voice "sp91_s1856_012"
    l "…C-Close your eyes!{#sp91_s1856_012}"

    # ……な、何を緊張してるんだよ！
    voice "sp91_s1856_013"
    s "…W-What are you so nervous about!{#sp91_s1856_013}"

    # うるさい。ほら、目を閉じなさい？
    voice "sp91_s1856_014"
    l "Quiet. Come on, close them.{#sp91_s1856_014}"

    # [EVENT_CG event    image=+195, level=80]
    $ dissolve_fx("id(195)")
    # ふぁい。
    voice "sp91_s1856_016"
    s "Yep.{#sp91_s1856_016}"

    # 目は開けちゃダメなんだからね！
    voice "sp91_s1856_017"
    l "You're not allowed to open them, okay!{#sp91_s1856_017}"

    # [EVENT_CG event    image=+196, level=80]
    $ dissolve_fx("id(196)")
    # ポリ……ポリ……ポリ……。
    voice "sp91_s1856_019"
    s "Crunch… crunch… crunch…{#sp91_s1856_019}"

    # ……ポリ……ポリ……ポリ。
    voice "sp91_s1856_020"
    l "…Crunch… crunch… crunch.{#sp91_s1856_020}"

    # （ぽ、ポッチーを食べる音がこんなに大きく感じるなんて……）
    s "(The sound of eating the pocky feels so loud…){#sp91_s1856_021}"

    # （……ルイズの綺麗な髪がすぐそこで揺れてる気配まで）
    s "(…I can even sense Louise's beautiful hair swaying right there.){#sp91_s1856_022}"

    # （あ、ルイズが震えてる……！）
    s "(Ah, Louise is trembling…!){#sp91_s1856_023}"

    # （……こ、ここは俺がリードして）【選択肢】……目を開く？ → scene 1857【選択肢】残りを一息に？ →
    s "(…I should take the lead here.){#sp91_s1856_024}"

label sp91_scene_1857:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+196, level=80]
    $ dissolve_fx("id(196)")
    # （……どんな表情をしているんだろう？）
    s "(…What kind of face is she making?){#sp91_s1857_002}"

    # （そ、そっと目を開いて……）[EVENT_CG event    image=+194, level=80]
    s "(S-Slowly, I open my eyes…){#sp91_s1857_003}"

    # うわっ！
    voice "sp91_s1857_004"
    s "Whoa!{#sp91_s1857_004}"

    # [EVENT_CG event    image=+193, level=80]
    $ dissolve_fx("id(193)")
    # きゃっ！
    voice "sp91_s1857_006"
    l "Eep!{#sp91_s1857_006}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # ……。
    voice "sp91_s1857_012"
    l "…{#sp91_s1857_012}"

    # ……ええと、あの？
    voice "sp91_s1857_013"
    s "…Um, so?{#sp91_s1857_013}"

    # [SPRITE   lay1     hide]
    # ……も、もうっ！なんで目を開けるのよ！恥ずかしいじゃない！
    voice "sp91_s1857_015"
    l "…G-Geez! Why did you open your eyes?! It's embarrassing!{#sp91_s1857_015}"

    # い、いや、あのその……。
    voice "sp91_s1857_016"
    s "N-No, I just, you see…{#sp91_s1857_016}"

    # [SPRITE   lay1     hide]
    # サ、サイトのバカァっ！
    voice "sp91_s1857_018"
    l "S-Saito, you idiot!{#sp91_s1857_018}"

    # [SPRITE   lay5     hide]
    # ご、ごめんなしゃぁぁい！
    voice "sp91_s1857_020"
    s "I-I'm soooo sorry!{#sp91_s1857_020}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay19    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [EVENT_CG event    hide]
    # [TRANS trans("crossfade", 1000)]
    # → next scene 1860
    jump sp91_scene_1860

label sp91_scene_1858:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+196, level=80]
    $ dissolve_fx("id(196)")
    # ……。
    voice "sp91_s1858_002"
    s "…{#sp91_s1858_002}"

    # ……。
    voice "sp91_s1858_003"
    l "…{#sp91_s1858_003}"

    # （……くっ、とまっちまった！）
    s "(…Gah, I froze!){#sp91_s1858_004}"

    # （ここは残りを一息にっ！）[SPRITE   lay1     hide][SPRITE   lay5    
    s "(Here, finish the rest in one go!){#sp91_s1858_005}"

    # ……ダ、ダメっ！もう限界っ！耐えられないっ！
    voice "sp91_s1858_006"
    l "…N-No! I can't take it anymore! I can't hold back!{#sp91_s1858_006}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay19    vibrate=14]
    # [SPRITE   lay1     hide, vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [EVENT_CG event    hide]
    # [TRANS trans("crossfade", 1000)]
    # って……いきなり、魔法を撃つかよ！普通っ！
    voice "sp91_s1858_022"
    s "Huh?! Casting a spell out of nowhere!? That's not normal!{#sp91_s1858_022}"

    # → next scene 1860
    jump sp91_scene_1860

label sp91_scene_1859:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+196, level=80]
    $ dissolve_fx("id(196)")
    # （……駄目だ、ここはルイズの純潔を守るために俺が身を引こう……）
    s "(…No good. Here I should pull back to protect Louise's purity…){#sp91_s1859_002}"

    # な、何ひっぱってるのよ！
    voice "sp91_s1859_003"
    l "W-What are you pulling away for?!{#sp91_s1859_003}"

    # ご、ごめん。これならどうだ？
    voice "sp91_s1859_004"
    s "S-Sorry. How about this?{#sp91_s1859_004}"

    # （さすがに、引いたらそりゃ失礼か……。少し前に出てみよう……）[SPRITE   lay1     hide]
    s "(Pulling back would be rude, I guess… Let me lean in a little…){#sp91_s1859_005}"

    # きっ、きゃあああぁぁっっ！！近すぎー！
    voice "sp91_s1859_006"
    l "K-Kyaaaaah!! Too close—!{#sp91_s1859_006}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay19    vibrate=14]
    # [SPRITE   lay1     hide, vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # ……サ、サイトが急に動くからよ！は、恥ずかしかったんだからぁ！
    voice "sp91_s1859_023"
    l "…It's because Saito moved all of a sudden! I-It was embarrassing!{#sp91_s1859_023}"

    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # → next scene 1860
    jump sp91_scene_1860

label sp91_scene_1860:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # （そんなに恥ずかしいのなら……、最初からやらなきゃいいだろ）[SE       se1      stop=1
    s "(If it's that embarrassing… you shouldn't have done it in the first place.){#sp91_s1860_004}"

