# Extra event (chapter_91), scenes 1700,1725,1726,1727,1728,1729,1730,1731,1732.
# Источник: ps2_source/chapters/chapter_91.txt

label sp_d1:
    $ tndl(None)
    $ show_sprites()

label sp_d1_scene_1700:

    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # ね、ねえ、サイト。ちょっとこっちに来て。
    voice "sp_d1_d_000"
    l "Hey, hey, Saito. Come here a moment.{#sp_d1_d_000}"

    # は？なんだよ、一体。
    voice "sp_d1_d_001"
    s "Huh? What is it?{#sp_d1_d_001}"

    # いいから来なさいっ！ご主人様の命令なんだから！
    voice "sp_d1_d_002"
    l "Never mind—come on! That's an order from your mistress!{#sp_d1_d_002}"

    # お、おい。引っ張るなよ。
    voice "sp_d1_d_003"
    s "H-Hey. Don't drag me!{#sp_d1_d_003}"

        "All right, fine.{#sp_d1_c_1700_1725}":
            jump sp_d1_scene_1725
        "I'll accompany you, mistress.{#sp_d1_c_1700_1726}":
            jump sp_d1_scene_1726
        "I refuse, absolutely.{#sp_d1_c_1700_1727}":
            jump sp_d1_scene_1727
label sp_d1_scene_1725:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # 分かったよ、仕方ないな。
    voice "sp_d1_d_004"
    s "All right, fine.{#sp_d1_d_004}"

    # [SPRITE   lay1     hide]
    # な、なによ。べ、別にイヤだったらついて来なくたっていいわよ。
    voice "sp_d1_d_005"
    l "W-What? I mean—if you don't want to, you don't have to come.{#sp_d1_d_005}"

    # 無理について来る必要なんてないんだから。
    voice "sp_d1_d_006"
    l "There's no need to force yourself to follow me.{#sp_d1_d_006}"

    # （おいおい。そんな顔してよく言うよ）
    s "(Hey now. Saying that with such a face…){#sp_d1_d_007}"

    # （ついて行かない、なんて言ったら何されるか……）
    s "(If I said I wasn't coming, who knows what she'd do…){#sp_d1_d_008}"

    # 何か言った？
    voice "sp_d1_d_009"
    l "Did you say something?{#sp_d1_d_009}"

    # い、いえっ！！なんにもっっっ！！
    voice "sp_d1_d_010"
    s "N-No! Nothing at all!!{#sp_d1_d_010}"

    # → next scene 1728
    jump sp_d1_scene_1728

label sp_d1_scene_1726:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # お供します、ご主人様。
    voice "sp_d1_d_011"
    s "I'll accompany you, mistress.{#sp_d1_d_011}"

    # えっ！？あ……う、うん。
    voice "sp_d1_d_012"
    l "Eh!? A… Mm.{#sp_d1_d_012}"

    # どうかしましたか、ご主人様？
    voice "sp_d1_d_013"
    s "Is something wrong, mistress?{#sp_d1_d_013}"

    # べ、別に。あ、ただ……。
    voice "sp_d1_d_014"
    l "N-No. It's just…{#sp_d1_d_014}"

    # ただ、なに？
    voice "sp_d1_d_015"
    s "And what is 'just'?{#sp_d1_d_015}"

    # い、いつもこれくらい素直なら楽なのにって思っただけよ！
    voice "sp_d1_d_016"
    l "I was just thinking—if you were always this obedient, things would be easier!{#sp_d1_d_016}"

    # ほ、ほらっ！行くわよっ！！
    voice "sp_d1_d_017"
    l "T-There! Let's go!{#sp_d1_d_017}"

    # → next scene 1728
    jump sp_d1_scene_1728

label sp_d1_scene_1727:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # 断固断る。
    voice "sp_d1_d_018"
    s "I refuse, absolutely.{#sp_d1_d_018}"

    # （今日は負けてないぞっ！）
    s "(I'm not losing today!){#sp_d1_d_019}"

    # イヤだ！イヤったらイヤだっ！絶対に、世界が逆立ちしてもっっ！！
    voice "sp_d1_d_020"
    s "No! No, no, no! Never, even if the world turns upside down!!{#sp_d1_d_020}"

    # （俺は断固として自分の意志を……）
    s "(I'll stick to my own will, no matter what…){#sp_d1_d_021}"

    # ……。
    voice "sp_d1_d_022"
    l "…{#sp_d1_d_022}"

    # （って、なんか怒ってるし！！）
    s "(Wait—she's angry!!){#sp_d1_d_023}"

    # あ、いや……。やっぱ……行きたくなってきた……かも。
    voice "sp_d1_d_024"
    s "U-Um… Actually… I'm starting to want to go… maybe.{#sp_d1_d_024}"

    # ホント？
    voice "sp_d1_d_025"
    l "Really?{#sp_d1_d_025}"

    # う、うん。ホントホント。
    voice "sp_d1_d_026"
    s "Y-Yeah. Really, really.{#sp_d1_d_026}"

    # そ、それじゃあ、行くわよ。
    voice "sp_d1_d_027"
    l "T-Then let's go.{#sp_d1_d_027}"

    # → next scene 1728
    jump sp_d1_scene_1728

label sp_d1_scene_1728:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # ほら……これ。
    voice "sp_d1_d_028"
    l "Here… this.{#sp_d1_d_028}"

    # へっ？
    voice "sp_d1_d_029"
    s "Huh?{#sp_d1_d_029}"

    # わたしが特別に作らせたんだから、ありがたく食べなさい。
    voice "sp_d1_d_030"
    l "I had it specially made for you, so eat it gratefully.{#sp_d1_d_030}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # え？作らせた？
    voice "sp_d1_d_031"
    s "Eh? You had it made?{#sp_d1_d_031}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ……えっ？あっっ！？
    voice "sp_d1_d_032"
    l "…Eh? Ah!{#sp_d1_d_032}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ち、違うわよっ！何言ってるのっ！！
    voice "sp_d1_d_033"
    l "N-No, that's not it! Don't say weird things!{#sp_d1_d_033}"

    # お、思い上がらないでよねっ！の、残っちゃったから、取っておいてもらったのよっっ！！
    voice "sp_d1_d_034"
    l "D-Don't get full of yourself! I-It's just left over, so I had them keep it for you!{#sp_d1_d_034}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # わ、わた、わたしが、何でわざわざあんたのために作ってもらわないといけないのよっ！
    voice "sp_d1_d_035"
    l "W-Why do I have to specially order food for you anyway!{#sp_d1_d_035}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # あ……うん。分かった分かった。それで……これ、もらっていいのか？
    voice "sp_d1_d_036"
    s "Ah… Okay, okay. I get it. So… can I take this?{#sp_d1_d_036}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # だ、だからそう言ってるでしょ！目の前に置いてお預け、なんて言わないわよ。
    voice "sp_d1_d_037"
    l "T-That's what I'm saying! I'm not one to dangle food in front of you!{#sp_d1_d_037}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # うん。それじゃ、いただきまーす。
    voice "sp_d1_d_038"
    s "Mm. Then, let's dig in.{#sp_d1_d_038}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # [TRANS trans("crossfade", 1000)]
    # はい、あーん。
    voice "sp_d1_d_039"
    l "Here—open up.{#sp_d1_d_039}"

    # ま、またっ！！
    voice "sp_d1_d_040"
    s "W-Wait!!{#sp_d1_d_040}"

    # なによ。イヤなの？
    voice "sp_d1_d_041"
    l "What? Don't you want it?{#sp_d1_d_041}"

    # いや、その……イヤって言うか……。
    voice "sp_d1_d_042"
    s "N-No, it's not that I don't want… it's just…{#sp_d1_d_042}"

        "Because it's embarrassing!{#sp_d1_c_1728_1729}":
            jump sp_d1_scene_1729
        "No, I don't want to!{#sp_d1_c_1728_1730}":
            jump sp_d1_scene_1730
        "A-Ahh, aaahn!{#sp_d1_c_1728_1731}":
            jump sp_d1_scene_1731
label sp_d1_scene_1729:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # だって恥ずかしいじゃん。
    voice "sp_d1_d_043"
    s "Because it's embarrassing!{#sp_d1_d_043}"

    # [EVENT_CG event    image=+180, level=80]
    $ dissolve_fx("id(180)")
    # なっ！ななななな……。
    voice "sp_d1_d_044"
    l "Wha—! N-No, no, no…{#sp_d1_d_044}"

    # べ、べ、べ、別にっ！は、恥ずかしくなんかないわよっ！
    voice "sp_d1_d_045"
    l "I-It's not! I'm not embarrassed at all!{#sp_d1_d_045}"

    # な、何言ってるのよっ！ば、馬鹿じゃないかしらっ！べ、別にわたしは恥ずかしくなんか……。
    voice "sp_d1_d_046"
    l "W-What are you saying? Are you an idiot?{#sp_d1_d_046}"

    # いや……ルイズじゃなくて、俺が……。
    voice "sp_d1_d_047"
    s "I-I wasn't talking about you, Louise—about me…{#sp_d1_d_047}"

    # と、とにかくっ！いいから食べなさいっ！！
    voice "sp_d1_d_048"
    l "A-Anyway! Just eat it!!{#sp_d1_d_048}"

    # ほらっ！あーんっ！
    voice "sp_d1_d_049"
    l "Here! Open up!{#sp_d1_d_049}"

    # あ、あーん……。
    voice "sp_d1_d_050"
    s "A-Ahh…{#sp_d1_d_050}"

    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # → next scene 1732
    jump sp_d1_scene_1732

label sp_d1_scene_1730:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # イヤだっ！！
    voice "sp_d1_d_051"
    s "No!!{#sp_d1_d_051}"

    # [EVENT_CG event    image=+181, level=80]
    $ dissolve_fx("id(181)")
    # なんですって！人の厚意を受け取れないって言うのっ！
    voice "sp_d1_d_052"
    l "What? You're saying you can't accept someone's kindness?{#sp_d1_d_052}"

    # あのなぁ、厚意っていうのは押しつけるもんじゃあ……。
    voice "sp_d1_d_053"
    s "Look—kindness isn't something you force on someone…{#sp_d1_d_053}"

    # 許さないわ、そんなワガママっ！食べないっていうんなら、力づくでも……。
    voice "sp_d1_d_054"
    l "I won't forgive you for that! If you won't eat it, I'll make you—{#sp_d1_d_054}"

    # （さ、殺気！？）
    s "(Whoa—killing intent!?){#sp_d1_d_055}"

    # わ、分かった！喰う、食べるっ！いただきます！！
    voice "sp_d1_d_056"
    s "O-Okay! I'll eat it! I'll eat it! Let's dig in!{#sp_d1_d_056}"

    # [EVENT_CG event    image=+180, level=80]
    $ dissolve_fx("id(180)")
    # まったく……。最初からそういえばいいのよ。
    voice "sp_d1_d_057"
    l "Honestly… You should've just said so from the start.{#sp_d1_d_057}"

    # ほらっ！あーんっ！
    voice "sp_d1_d_058"
    l "Here! Open up!{#sp_d1_d_058}"

    # ……あーん。
    voice "sp_d1_d_059"
    s "…Aahn.{#sp_d1_d_059}"

    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # → next scene 1732
    jump sp_d1_scene_1732

label sp_d1_scene_1731:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # あ、あーん。
    voice "sp_d1_d_060"
    s "A-Ahh.{#sp_d1_d_060}"

    # （ま、まあ、変なもの入ってないだろうし、美味いことは美味いし……）
    s "(Well… nothing weird in it, and it tastes good…){#sp_d1_d_061}"

    # あ、あら、素直ね。少しは分かって来たのかしら。
    voice "sp_d1_d_062"
    l "Oh, you're being obedient. Maybe you're finally starting to understand.{#sp_d1_d_062}"

    # → next scene 1732
    jump sp_d1_scene_1732

label sp_d1_scene_1732:

    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # もぐもぐもぐ……。
    voice "sp_d1_d_063"
    s "Munch munch munch…{#sp_d1_d_063}"

    # おいしい？
    voice "sp_d1_d_064"
    l "Is it good?{#sp_d1_d_064}"

    # うん！美味い！！
    voice "sp_d1_d_065"
    s "Mm! Delicious!!{#sp_d1_d_065}"

    # ホント！？それじゃあ、もう一回！あーん！
    voice "sp_d1_d_066"
    l "Really!? Then once more! Open up!{#sp_d1_d_066}"

    # ……へ？
    voice "sp_d1_d_067"
    s "…Eh?{#sp_d1_d_067}"

    # [EVENT_CG event    image=+180, level=80]
    $ dissolve_fx("id(180)")
    # もう一回！
    voice "sp_d1_d_068"
    l "Once more!{#sp_d1_d_068}"

    # わ、分かったよ……。……あーん。
    voice "sp_d1_d_069"
    s "O-Okay… Aahn.{#sp_d1_d_069}"

    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # よく出来ました。はい、あーん。
    voice "sp_d1_d_070"
    l "Very good. Here—open up.{#sp_d1_d_070}"

    # え……ま、また？
    voice "sp_d1_d_071"
    s "E… Again?{#sp_d1_d_071}"

    # [EVENT_CG event    image=+181, level=80]
    $ dissolve_fx("id(181)")
    # あ、あたりまえでしょ！わたしの気が済む……こ、こほん、わたしがいいって言うまでさせるんだから。
    voice "sp_d1_d_072"
    l "O-Of course! I won't stop until I'm satisfied—ahem, until I say so!{#sp_d1_d_072}"

    # マ、マジっすか？
    voice "sp_d1_d_073"
    s "R-Really!?{#sp_d1_d_073}"

    # なによ？いやなの？
    voice "sp_d1_d_074"
    l "What? Don't you like it?{#sp_d1_d_074}"

    # い、いや、そんなことはないけど……。
    voice "sp_d1_d_075"
    s "N-No, that's not it, but…{#sp_d1_d_075}"

    # [EVENT_CG event    image=+179, level=80]
    $ dissolve_fx("id(179)")
    # ほらっ、あーん。
    voice "sp_d1_d_076"
    l "Here—open up.{#sp_d1_d_076}"

    # あ、あーん……。
    voice "sp_d1_d_077"
    s "A-Ahh…{#sp_d1_d_077}"

    # （なんだこの、気恥ずかしいやら痒いやら、複雑な気分は……）
    s "(What's this weird feeling—embarrassing and itchy all at once…){#sp_d1_d_078}"

    # （なんの罰ゲームっすか……）[SE       se1      stop=1][BGM      bgm      s
    s "(What kind of penalty game is this…?){#sp_d1_d_079}"

    return
