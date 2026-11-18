# Extra event chapter (chapter_90), all scenes.
# Источник: ps2_source/chapters/chapter_90.txt

label sp90_scene_1533:

label sp90_scene_1534:

label sp90_scene_1535:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # この、バカ犬っ！
    voice "sp90_s1535_003"
    l "You stupid dog!{#sp90_s1535_003}"

    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     hide, vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # ぐはっ！
    voice "sp90_s1535_014"
    s "Guh!{#sp90_s1535_014}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # [TRANS trans("crossfade", 1000)]
    # あっちにほいほい、こっちにほいほい、だらしなくしっぽを振って回ってるんじゃないわよっ！
    voice "sp90_s1535_020"
    l "Don't trot this way and that, wagging your tail all over the place in such a shameless way!{#sp90_s1535_020}"

    # べ、別にしっぽなんか振ってねぇっ！第一俺は、犬なんかじゃなくて……。
    voice "sp90_s1535_021"
    s "I-I'm not wagging my tail or anything! And besides, I'm not a dog or any……{#sp90_s1535_021}"

    # ……じゃあ、なあに？
    voice "sp90_s1535_022"
    l "……Then what are you?{#sp90_s1535_022}"

    # あ、い、いえ、その……。
    voice "sp90_s1535_023"
    s "Ah, n-no, that is……{#sp90_s1535_023}"

    # なんなのよ。言ってみなさいよ。
    voice "sp90_s1535_024"
    l "What are you? Say it.{#sp90_s1535_024}"

    # イエ、イヌデゴザイマス。
    voice "sp90_s1535_025"
    s "Y-yes, I'm a dog!{#sp90_s1535_025}"

    # っていうかご主人様。そんな怖い顔してたら美人が台無し……。
    voice "sp90_s1535_026"
    s "I mean, master. If you keep making that scary face, your beauty goes to waste……{#sp90_s1535_026}"

    # し、しつけのなってない犬は、体に教え込むしかないわよね。
    voice "sp90_s1535_027"
    l "A dog that hasn't been trained has to be taught with the body, you know.{#sp90_s1535_027}"

    # か、からだっ！？
    voice "sp90_s1535_028"
    s "B-Body!?{#sp90_s1535_028}"

    # 覚悟はいいわね？
    voice "sp90_s1535_029"
    l "Are you ready for it?{#sp90_s1535_029}"

    # ちょっ！まっ！！か、覚悟って！！
    voice "sp90_s1535_030"
    s "W-Wait! H-Hold on!! R-Ready for what!!{#sp90_s1535_030}"


    menu:
        "If you'd just talk, I'd understand!{#sp90_c_1535_1553}":
            jump sp90_scene_1553
        "That's tyranny!{#sp90_c_1535_1554}":
            jump sp90_scene_1554
        "Let's be nonviolent here……{#sp90_c_1535_1555}":
            jump sp90_scene_1555

label sp90_scene_1536:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # この、バカ犬っ！
    voice "sp90_s1536_003"
    l "You stupid dog!{#sp90_s1536_003}"

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
    # ぐはっ！
    voice "sp90_s1536_014"
    s "Guh!{#sp90_s1536_014}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # [TRANS trans("crossfade", 1000)]
    # なにニヤニヤニヤニヤしてるのよ！だらしない顔してるんじゃないわよっ！！
    voice "sp90_s1536_020"
    l "What are you grinning away at! Don't make such a shameless face!!{#sp90_s1536_020}"

    # べ、別にだらしない顔なんてしてねぇっ！
    voice "sp90_s1536_021"
    s "I-I'm not making any slovenly face!{#sp90_s1536_021}"

    # 鼻の下伸ばしていやらしい！！
    voice "sp90_s1536_022"
    l "Drooling all over yourself, you pervert!!{#sp90_s1536_022}"

    # や……やらしいって……。この顔は生まれつきだ！！
    voice "sp90_s1536_023"
    s "L-Lecherous……? This face is the way I was born!!{#sp90_s1536_023}"

    # そう……生まれつき。分かったわ。
    voice "sp90_s1536_024"
    l "I see…… Born with it. Got it.{#sp90_s1536_024}"

    # ふぅ……。
    voice "sp90_s1536_025"
    s "Phew……{#sp90_s1536_025}"

    # それじゃあ、わたし好みに作り直してあげる。
    voice "sp90_s1536_026"
    l "Then I'll just remake you to my liking.{#sp90_s1536_026}"

    # へっ！？ちょ、ちょまっっ！！
    voice "sp90_s1536_027"
    s "Heh!? W-Wait, wait!!{#sp90_s1536_027}"

    # じ、じっとしてなさい。ちょっと痛いかも知れないけど、我慢できるわよね。
    voice "sp90_s1536_028"
    l "H-Hold still. It might hurt a little, but you can put up with it, right?{#sp90_s1536_028}"

    # ひ、ひぃっっ！！
    voice "sp90_s1536_029"
    s "Eeep!!{#sp90_s1536_029}"


    menu:
        "Run away!{#sp90_c_1536_1561}":
            jump sp90_scene_1561
        "Resist!{#sp90_c_1536_1562}":
            jump sp90_scene_1562
        "Surrender!{#sp90_c_1536_1563}":
            jump sp90_scene_1563

label sp90_scene_1537:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # ほんっとうにっ！！何度言っても分からないバカ犬ねっっ！！
    voice "sp90_s1537_003"
    l "Really now!! You're a stupid dog who never listens, no matter how many times I tell you!!{#sp90_s1537_003}"

    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     hide, vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # ぐはぁぁぁっ！
    voice "sp90_s1537_014"
    s "Guhaaaa!{#sp90_s1537_014}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # [TRANS trans("crossfade", 1000)]
    # あ・れ・ほ・ど！しっぽ振って回るな、って言ってるのに、まだ分からないのかしら！
    voice "sp90_s1537_020"
    l "How many times have I told you not to go wagging your tail and spinning around? Still don't get it?!{#sp90_s1537_020}"

    # ひ、ひぃっ！ご、誤解です！間違いです！
    voice "sp90_s1537_021"
    s "H-Hii! It's a m-misunderstanding! A mistake!{#sp90_s1537_021}"

    # 却下！却下却下却下！！言い訳なんか聞きたくないわっ！
    voice "sp90_s1537_022"
    l "Rejected! Rejected rejected rejected!! I don't want to hear any excuses!{#sp90_s1537_022}"

    # き、今日という今日はっ！
    voice "sp90_s1537_023"
    l "T-Today, of all days——!{#sp90_s1537_023}"

    # [SE       se0      play=+61]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     hide, vibrate=14]
    # [SPRITE   lay1     hide, vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # ぎゃっ！
    voice "sp90_s1537_034"
    s "Gya!{#sp90_s1537_034}"

    # ……二度とそのしっぽを振れないようにしてあげるわ！
    voice "sp90_s1537_035"
    l "……I'll make sure you can never wag that tail again!{#sp90_s1537_035}"

    # [SE       se0      play=+61]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # いだだだだだだだだっ！！
    voice "sp90_s1537_046"
    s "Ow-ow-ow-ow-ow!!{#sp90_s1537_046}"

    # （や、ヤバイっ！殺られるっっ！！）
    s "(N-No, this is bad! I'm gonna be killed!!){#sp90_s1537_047}"


    menu:
        "Escape!{#sp90_c_1537_1569}":
            jump sp90_scene_1569
        "Tackle!{#sp90_c_1537_1570}":
            jump sp90_scene_1570
        "…Faint!{#sp90_c_1537_1571}":
            jump sp90_scene_1571

label sp90_scene_1538:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # ホントにうちのバカ犬ときたら、節操がないんだから……。
    voice "sp90_s1538_003"
    l "Honestly, my stupid dog has no shame at all……{#sp90_s1538_003}"

    # そ、そうか？
    voice "sp90_s1538_004"
    s "I-Is that right?{#sp90_s1538_004}"

    # そうよ。ご主人様が見てないところで何をしているのか、分からないとでも思っているの？
    voice "sp90_s1538_005"
    l "That's right. Do you think I don't know what you get up to when master isn't looking?{#sp90_s1538_005}"

    # だから、誤解だってば……。
    voice "sp90_s1538_006"
    s "I keep telling you, it's a misunderstanding……{#sp90_s1538_006}"

    # 決めたわっ！バカ犬には……。ホントの犬の気分を味あわせてあげるっ！
    voice "sp90_s1538_007"
    l "I've decided! For this stupid dog…… I'll let you taste what it's really like to be a dog!{#sp90_s1538_007}"

    # な、何する気だよーーっ！
    voice "sp90_s1538_008"
    s "W-What are you going to do——?!{#sp90_s1538_008}"


    menu:
        "O-Of course I'll run away!{#sp90_c_1538_1577}":
            jump sp90_scene_1577
        "I'll wash my neck and brace for it.{#sp90_c_1538_1578}":
            jump sp90_scene_1578
        "Aren't I already living like a dog?!{#sp90_c_1538_1579}":
            jump sp90_scene_1579

label sp90_scene_1539:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # やっぱり、バカ犬に首輪をつけるのは飼い主としての義務のようね。
    voice "sp90_s1539_003"
    l "After all, putting a collar on a stupid dog seems to be a pet owner's duty.{#sp90_s1539_003}"

    # く、首輪ぁ！？
    voice "sp90_s1539_004"
    s "A-A collar!?{#sp90_s1539_004}"

    # ……バカ犬はわたしの足下にだけひざまずいてればいいのよっ！
    voice "sp90_s1539_005"
    l "……A stupid dog only needs to kneel at my feet!{#sp90_s1539_005}"

    # ううっ……。
    voice "sp90_s1539_006"
    s "Ugh……{#sp90_s1539_006}"

    # ……うふふっ。
    voice "sp90_s1539_007"
    l "……Ufufu.{#sp90_s1539_007}"

    # さあ、首をお出しなさい？特別にわたしがつけてあげるんだからね。
    voice "sp90_s1539_008"
    l "Now, stick out your neck. I'll put it on for you, as a special treat.{#sp90_s1539_008}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # [TRANS trans("crossfade", 1000)]
    # うふふふふふ……。新しい首輪、よく似合うわよ。……選ぶの苦労したんだからね？
    voice "sp90_s1539_014"
    l "Ufufufufu…… The new collar suits you.…… I had a hard time picking it out, you know?{#sp90_s1539_014}"


    menu:
        "W-Woof!{#sp90_c_1539_1585}":
            jump sp90_scene_1585
        "……Ah, thank you.{#sp90_c_1539_1586}":
            jump sp90_scene_1586
        "Please don't go to so much trouble.{#sp90_c_1539_1587}":
            jump sp90_scene_1587

label sp90_scene_1540:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # ……くっ、首輪よ！やっぱりバカ犬には首輪が必要なようね！
    voice "sp90_s1540_003"
    l "……Kuh, a collar! It seems a stupid dog really does need a collar!{#sp90_s1540_003}"

    # く、首輪っ！？
    voice "sp90_s1540_004"
    s "A collar!?{#sp90_s1540_004}"

    # バカ犬がこのわたしのモノだってことを思い知らせてあげるんだからっ！
    voice "sp90_s1540_005"
    l "I'm going to make you realize that this stupid dog belongs to me!{#sp90_s1540_005}"

    # やっ、やめろぉーーーっ！！
    voice "sp90_s1540_006"
    s "S-Stop it——!!{#sp90_s1540_006}"

    # 返事は『わん』でしょっ！
    voice "sp90_s1540_007"
    l "The answer is 'woof', right?!{#sp90_s1540_007}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # [TRANS trans("crossfade", 1000)]
    # ……うううっ。なんでこんなことに。
    voice "sp90_s1540_013"
    s "……Ugh. How did it come to this.{#sp90_s1540_013}"

    # あら、なにか文句あるの？
    voice "sp90_s1540_014"
    l "Oh? Do you have a complaint?{#sp90_s1540_014}"


    menu:
        "I-I'm not a dog!{#sp90_c_1540_1593}":
            jump sp90_scene_1593
        "No complaints…… Woof!{#sp90_c_1540_1594}":
            jump sp90_scene_1594
        "O-One of these days, Louise……{#sp90_c_1540_1595}":
            jump sp90_scene_1595

label sp90_scene_1541:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # 魔法の特訓をするわ！
    voice "sp90_s1541_003"
    l "We're going to do some special magic training!{#sp90_s1541_003}"

    # え、ルイズ。一体どうしたの？
    voice "sp90_s1541_004"
    s "Eh, Louise. What's gotten into you?{#sp90_s1541_004}"

    # 「虚無」の魔法を使えるようになったのに、命中率は低いまま。
    voice "sp90_s1541_005"
    l "Even though I've learned to use Void magic, my accuracy is still low.{#sp90_s1541_005}"

    # 分かったの。わたし、実戦経験が足りなかったのよ。サイト、協力してもらうわよ！
    voice "sp90_s1541_006"
    l "I get it now. I was lacking real combat experience. Saito, you're going to help me!{#sp90_s1541_006}"

    # （うっ。ま、まずいっ！なんか昔の傷にでも触れちまったのか？）
    s "(Ugh. T-This is bad! Did I touch an old wound or something?){#sp90_s1541_007}"


    menu:
        "W-Well, you've improved a bit, haven't you?……{#sp90_c_1541_1601}":
            jump sp90_scene_1601
        "No, you're doing great!{#sp90_c_1541_1602}":
            jump sp90_scene_1602
        "Really, it's a waste of effort……{#sp90_c_1541_1603}":
            jump sp90_scene_1603

label sp90_scene_1542:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # 今日はいいお天気だし、すこし外に出ない？
    voice "sp90_s1542_003"
    l "It's nice weather today, so how about we go outside a bit?{#sp90_s1542_003}"

    # へっ？もしかして魔法の特訓ですか？
    voice "sp90_s1542_004"
    s "Huh? You mean magic training?{#sp90_s1542_004}"

    # ……あれ、なんで分かったの？これから魔法の訓練をしようと思ってたの。当然、手伝ってくれるわよね？
    voice "sp90_s1542_005"
    l "……Huh, how did you know? I was just about to do magic training. Of course you'll help me, right?{#sp90_s1542_005}"


    menu:
        "L-Let me help you!{#sp90_c_1542_1609}":
            jump sp90_scene_1609
        "B-But I'm busy with a date……{#sp90_c_1542_1610}":
            jump sp90_scene_1610
        "Training is such a waste of effort……{#sp90_c_1542_1611}":
            jump sp90_scene_1611

label sp90_scene_1543:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # ……そういえば、今日はいいお天気ね。
    voice "sp90_s1543_003"
    l "……Come to think of it, it's nice weather today.{#sp90_s1543_003}"

    # へっ？
    voice "sp90_s1543_004"
    s "Huh?{#sp90_s1543_004}"

    # なんだか、急に魔法の特訓をしたくなってきちゃった。
    voice "sp90_s1543_005"
    l "Suddenly I've gotten the urge to do some magic training.{#sp90_s1543_005}"

    # ま、まさか……。
    voice "sp90_s1543_006"
    s "N-No way……{#sp90_s1543_006}"

    # ……ねえ、バカ犬。手伝ってくれるわよね？
    voice "sp90_s1543_007"
    l "……Hey, stupid dog. You'll help me, right?{#sp90_s1543_007}"

    # ち、ちなみに拒否権なんかは……。
    voice "sp90_s1543_008"
    s "B-By the way, do I have the right to refuse……?{#sp90_s1543_008}"

    # もちろん……。……あるわけないでしょ！
    voice "sp90_s1543_009"
    l "Of course…… ……As if I'd have one!{#sp90_s1543_009}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # [TRANS trans("crossfade", 1000)]
    # さて、こんなものかしら？
    voice "sp90_s1543_015"
    l "Now, how's this?{#sp90_s1543_015}"

    # ……どうして、ボクは縛られてるのでありますか？
    voice "sp90_s1543_016"
    s "……Why am I tied up?{#sp90_s1543_016}"

    # はい、このリンゴを持っててね。今日のリンゴは３個よ。
    voice "sp90_s1543_017"
    l "Here, hold this apple. There are three apples today.{#sp90_s1543_017}"

    # まず、頭の上にひとつ乗せて、と。……ん、両手にもひとつずつ持ってるのよ。
    voice "sp90_s1543_018"
    l "First, put one on top of your head, and…… Mm, you're holding one in each hand too.{#sp90_s1543_018}"

    # な、なんでそんな曲芸じみた設定を！
    voice "sp90_s1543_019"
    s "W-Why such acrobatic conditions!?{#sp90_s1543_019}"

    # うふふ、安心しなさい。見事にリンゴだけを撃ち落してあげる。
    voice "sp90_s1543_020"
    l "Ufufu, don't worry. I'll shoot down only the apples, beautifully.{#sp90_s1543_020}"

    # ……もう、誰もゼロのルイズなんて馬鹿にできないようになるんだから！
    voice "sp90_s1543_021"
    l "……Soon, no one will be able to make fun of Zero Louise again!{#sp90_s1543_021}"


    menu:
        "D-Do you think it'll really succeed……?{#sp90_c_1543_1617}":
            jump sp90_scene_1617
        "What happens if you fail?{#sp90_c_1543_1618}":
            jump sp90_scene_1618
        "……I have a bad feeling about this.{#sp90_c_1543_1619}":
            jump sp90_scene_1619

label sp90_scene_1544:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # さて、今日はどんなお仕置きをしてあげようかしら？
    voice "sp90_s1544_003"
    l "Now, what kind of punishment shall I give you today?{#sp90_s1544_003}"


    menu:
        "I'm being framed!{#sp90_c_1544_1625}":
            jump sp90_scene_1625
        "Dash away!{#sp90_c_1544_1626}":
            jump sp90_scene_1626
        "Call her a cute master!{#sp90_c_1544_1627}":
            jump sp90_scene_1627

label sp90_scene_1545:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # 部屋から、出て行きなさいっ！
    voice "sp90_s1545_003"
    l "Get out of the room!{#sp90_s1545_003}"

    # ちょ、ちょっと待って！ルイズ！
    voice "sp90_s1545_004"
    s "W-Wait! Louise!{#sp90_s1545_004}"

    # ルイズぅ？ご主人様でしょ！
    voice "sp90_s1545_005"
    l "Louise? It's 'master', isn't it!{#sp90_s1545_005}"

    # まったく少し甘い顔をしたら……。すぐにこれなんだから！
    voice "sp90_s1545_006"
    l "Honestly, the moment I show the slightest kindness…… this is what happens!{#sp90_s1545_006}"

    # ほらっ、グズグズしてるんじゃないっ！毛布ぐらいは貸してあげるっ。
    voice "sp90_s1545_007"
    l "Come on, don't dawdle! I'll at least lend you a blanket.{#sp90_s1545_007}"

    # しばらく廊下で寝て、反省しなさいっ！
    voice "sp90_s1545_008"
    l "Sleep in the hallway for a while and reflect on your sins!{#sp90_s1545_008}"

    # ル、ルイズ横暴ぅぅっ！
    voice "sp90_s1545_009"
    s "L-Louise, you're so high-handed!{#sp90_s1545_009}"

    # [SE       se0      play=+56]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # ………。……。…。[EVENT_CG event    image=+170, level=80][TRANS
    th "………。……。…。{#sp90_s1545_014}"

    # ちくしょう、なんで俺がこんな目に……。
    voice "sp90_s1545_015"
    s "Damn, why does this have to happen to me……{#sp90_s1545_015}"

    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # ……あら、どうしたのダーリン？ひょっとして、部屋を追い出されたとか？
    voice "sp90_s1545_022"
    k "……My, what's wrong, darling? Don't tell me you were kicked out of your room?{#sp90_s1545_022}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # ああ、よしよし。かわいそうに。
    voice "sp90_s1545_024"
    k "There, there. You poor thing.{#sp90_s1545_024}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # もうっ、暗い顔しないの！泣くならあたしの胸で泣きなさい。
    voice "sp90_s1545_026"
    k "Come on, don't make such a gloomy face! If you're going to cry, cry on my breast.{#sp90_s1545_026}"


    menu:
        "Cling to her and cry{#sp90_c_1545_1633}":
            jump sp90_scene_1633
        "Bury your face in her chest and cry{#sp90_c_1545_1634}":
            jump sp90_scene_1634
        "Hurriedly pull away from Kirche{#sp90_c_1545_1635}":
            jump sp90_scene_1635

label sp90_scene_1546:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # ……。
    voice "sp90_s1546_003"
    l "……{#sp90_s1546_003}"

    # どうして、このバカ犬はご主人様のありがたみが分からないのかしらね。
    voice "sp90_s1546_004"
    l "Why can't this stupid dog appreciate the honor of serving a master?{#sp90_s1546_004}"

    # え、ええっ！
    voice "sp90_s1546_005"
    s "E-Eh!?{#sp90_s1546_005}"

    # ……出て行きなさい。
    voice "sp90_s1546_006"
    l "……Get out.{#sp90_s1546_006}"

    # ま、また、廊下で寝ろとのおおせで……。
    voice "sp90_s1546_007"
    s "S-So I'm to sleep in the hallway again……{#sp90_s1546_007}"

    # ……別に廊下からも追い出してあげてもいいのよ？
    voice "sp90_s1546_008"
    l "……I don't mind kicking you out of the hallway too, you know?{#sp90_s1546_008}"

    # バカ犬からノラ犬になってみる？……廊下ぐらいじゃ懲りないんでしょ。
    voice "sp90_s1546_009"
    l "Want to go from stupid dog to stray dog?…… A hallway won't teach you a lesson, will it.{#sp90_s1546_009}"

    # い、いや。そ、それは……。
    voice "sp90_s1546_010"
    s "N-No. T-That's……{#sp90_s1546_010}"

    # ……さあ、出て行きなさい！
    voice "sp90_s1546_011"
    l "……Now, get out!{#sp90_s1546_011}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+170, level=80]
    $ dissolve_fx("id(170)")
    # [TRANS trans("crossfade", 1000)]
    # ち、ちくしょう！なんだよ！
    voice "sp90_s1546_017"
    s "D-Damn! What the hell!{#sp90_s1546_017}"

    # 俺だっていつまでもバカ犬じゃないんだ！立派な牙を持った狼だってことを見せてやるさ。もう謝ったからって知らないか
    voice "sp90_s1546_018"
    s "I'm not going to be a stupid dog forever! I'll show you I'm a wolf with real fangs! And don't think you can get away with it just because you apologized!{#sp90_s1546_018}"

    # そのときになって吠え顔をかくなよ！ルイズっ！はっはっはっ……はははっ……。
    voice "sp90_s1546_019"
    s "Don't give me that snarl when that time comes! Louise! Hahahaha…… hahaha……{#sp90_s1546_019}"

    # ……はぁ、どうしよう？
    voice "sp90_s1546_020"
    s "……Hah, now what?{#sp90_s1546_020}"


    menu:
        "Sleeping outside again?{#sp90_c_1546_1641}":
            jump sp90_scene_1641
        "Life in the hallway{#sp90_c_1546_1642}":
            jump sp90_scene_1642
        "To a girl's place……{#sp90_c_1546_1643}":
            jump sp90_scene_1643

label sp90_scene_1547:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # うふふ……。……いいことを思いついたわ。
    voice "sp90_s1547_003"
    l "Ufufu…… ……I've thought of a good idea.{#sp90_s1547_003}"

    # まてっ、なんだよっ！その笑いはっ！
    voice "sp90_s1547_004"
    s "Wait! What's with that laugh!?{#sp90_s1547_004}"

    # バ、バカ犬に女の子がどんな気持ちで生活してるか教えてあげるっ！
    voice "sp90_s1547_005"
    l "I'll teach this stupid dog what it's like to live as a girl!{#sp90_s1547_005}"

    # へっ？
    voice "sp90_s1547_006"
    s "Huh?{#sp90_s1547_006}"

    # ……フフンフンフン。
    voice "sp90_s1547_007"
    l "……Fufun fufun fun.{#sp90_s1547_007}"

    # いや、あのご主人様？な、何を？
    voice "sp90_s1547_008"
    s "U-Um, master? W-What are you doing?{#sp90_s1547_008}"

    # 下着は……。うふふ、これなんてどうかしら？
    voice "sp90_s1547_009"
    l "As for underwear…… Ufufu, how about this?{#sp90_s1547_009}"

    # な、なに考えてやがるっ！ルイズっ！
    voice "sp90_s1547_010"
    s "W-What are you thinking! Louise!{#sp90_s1547_010}"

    # ……そんなに女の子が好きなんだったら、女の子になればいいのよっ！
    voice "sp90_s1547_011"
    l "……If you like girls so much, then just become a girl!{#sp90_s1547_011}"

    # や、やめろっ！早まるなっ！故郷でおかあさんが泣いちゃうぞ！
    voice "sp90_s1547_012"
    s "S-Stop! Don't rush it! Your mom back home will cry!{#sp90_s1547_012}"

    # うるさいっ！バカ犬っ！
    voice "sp90_s1547_013"
    l "Quiet, stupid dog!{#sp90_s1547_013}"

    # 一度、女の子の姿になって、乙女の気持ちを分かりなさいっ！
    voice "sp90_s1547_014"
    l "Become a girl once and understand a maiden's feelings!{#sp90_s1547_014}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+173, level=80]
    $ dissolve_fx("id(173)")
    # [TRANS trans("crossfade", 1000)]
    # いっ、いやぁぁぁぁっ！！
    voice "sp90_s1547_020"
    s "N-Noooo!!{#sp90_s1547_020}"


    menu:
        "Escape!{#sp90_c_1547_1649}":
            jump sp90_scene_1649
        "Endure it!{#sp90_c_1547_1650}":
            jump sp90_scene_1650
        "H-Huh, is this me?{#sp90_c_1547_1651}":
            jump sp90_scene_1651

label sp90_scene_1548:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # ……まだ教育が足りなかったようね。少しは女の子の気持ちが分かるように、教育してあげるっ！
    voice "sp90_s1548_003"
    l "…It seems my lessons weren't enough. I'll teach you some more, so you'll finally understand a girl's feelings!{#sp90_s1548_003}"

    # ま、まてっ！お、俺が悪かったですっ！
    voice "sp90_s1548_004"
    s "W-Wait! I-I was wrong, okay?!{#sp90_s1548_004}"

    # ま、まさか……。
    voice "sp90_s1548_005"
    s "N-No way…{#sp90_s1548_005}"

    # うふふ、今日は特別にお化粧も教えてあげるんだからっ！
    voice "sp90_s1548_006"
    l "Ufufu. As a special treat today, I'll even teach you how to put on makeup!{#sp90_s1548_006}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+174, level=80]
    $ dissolve_fx("id(174)")
    # [TRANS trans("crossfade", 1000)]
    # いっ、いやぁぁっ！やめてぇぇっ！
    voice "sp90_s1548_012"
    s "N-Nooo! Stop ittt!{#sp90_s1548_012}"


    menu:
        "Th-This is… me?{#sp90_c_1548_1657}":
            jump sp90_scene_1657
        "Th-This is… little me?{#sp90_c_1548_1658}":
            jump sp90_scene_1658
        "I'm all dirty. She got me all dirty.{#sp90_c_1548_1659}":
            jump sp90_scene_1659

label sp90_scene_1549:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # まだまだだわ。バカ犬にはもう少し女の子の気持ちを教えるべきね。
    voice "sp90_s1549_003"
    l "You've still got a long way to go. I should teach this stupid dog a little more about a girl's feelings.{#sp90_s1549_003}"

    # （ひっ、ひぃぃっ！）
    s "(Eep, eeeh!){#sp90_s1549_004}"

    # す、すいません！お、俺が悪かったですっ！
    voice "sp90_s1549_005"
    s "S-Sorry! I-I was wrong, okay?!{#sp90_s1549_005}"

    # あら、そんなに謝らなくてもいいわよ。
    voice "sp90_s1549_006"
    l "My, you don't have to apologize that much.{#sp90_s1549_006}"

    # 女の子の気持ちが理解できるようになるまで、ちゃんと教育してあげるんだから！
    voice "sp90_s1549_007"
    l "I'll give you a proper education until you can understand a girl's feelings!{#sp90_s1549_007}"

    # ご、ご主人様にそんなお手をわずらわせていただかなくても……。
    voice "sp90_s1549_008"
    s "Y-You don't need to trouble yourself like that, Master…{#sp90_s1549_008}"

    # 遠慮なんてしなくていいわよ……ほらっ！
    voice "sp90_s1549_009"
    l "There's no need to hold back… Here!{#sp90_s1549_009}"

    # いっ、いやぁぁっ！やめてぇぇっ！
    voice "sp90_s1549_010"
    s "N-Nooo! Stop ittt!{#sp90_s1549_010}"

    # うふふ、いい声で鳴きなさいっ！
    voice "sp90_s1549_011"
    l "Ufufu. Bark in a nice voice!{#sp90_s1549_011}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+174, level=80]
    $ dissolve_fx("id(174)")
    # [TRANS trans("crossfade", 1000)]
    # ……ひ、ひどいです、ご主人様。イ、イヤだっていったのに。
    voice "sp90_s1549_017"
    s "…Y-You're terrible, Master. I told you I didn't want to.{#sp90_s1549_017}"

    # うふふ、今日はそのままおでかけよ。
    voice "sp90_s1549_018"
    l "Ufufu. We're going out just like this today.{#sp90_s1549_018}"

    # ……みんなにも紹介してあげるんだから！
    voice "sp90_s1549_019"
    l "…And I'll introduce you to everyone!{#sp90_s1549_019}"

    # か、勘弁してください。ご主人様……。
    voice "sp90_s1549_020"
    s "S-Spare me, Master…{#sp90_s1549_020}"

    # ホントに往生際が悪いんだから。……いっそ、首輪もつけちゃおうかしら？
    voice "sp90_s1549_021"
    l "You really are a sore loser. …Maybe I should put a collar on you, too?{#sp90_s1549_021}"

    # それはいろんな意味でまずいと思います。
    voice "sp90_s1549_022"
    s "That's a bad idea in more ways than one, I think.{#sp90_s1549_022}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # うふふ、みんな驚くわよっ！あら、ギーシュにモンモランシー……。
    voice "sp90_s1549_031"
    l "Ufufu, everyone will be surprised! Oh my, Guiche and Montmorency…{#sp90_s1549_031}"

    # ごきげんよう、モンモランシー、ギーシュ。
    voice "sp90_s1549_032"
    l "Good day, Montmorency, Guiche.{#sp90_s1549_032}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay4     image=+555, level=160, dir=1A]
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # ……やぁ、ルイズ。
    voice "sp90_s1549_036"
    th "…Oh, Louise.{#sp90_s1549_036}"

    # あら、ルイズ。
    voice "sp90_s1549_037"
    th "My, Louise.{#sp90_s1549_037}"

    # [SPRITE   lay3     image=+885, level=160, dir=2A]
    # ……今日はあの使い魔の彼は一緒じゃないの？
    voice "sp90_s1549_039"
    th "…Isn't that familiar of yours with you today?{#sp90_s1549_039}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # え、ええ。ちょっと。
    voice "sp90_s1549_042"
    l "Y-Y-Yes. Sort of.{#sp90_s1549_042}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay4     image=+563, level=160, dir=1A]
    # そ、そういえばこちらの美しい女性について是非……！
    voice "sp90_s1549_045"
    th "S-Speaking of which, about this beautiful lady here, I simply must…!{#sp90_s1549_045}"

    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # ギ、ギーシュ！
    voice "sp90_s1549_047"
    th "G-Guiche!{#sp90_s1549_047}"

    # （ひっ、手をとるな！ギーシュ！）[SPRITE   lay4     hide][SPRITE   lay1 
    s "(Eep! Don't take her hand, Guiche!){#sp90_s1549_048}"

    # え、ええとね。こちらは……。
    voice "sp90_s1549_049"
    l "U-Um, well. This is…{#sp90_s1549_049}"

    # [SPRITE   lay3     image=+885, level=160, dir=2A]
    # あら？この香水はルイズと同じ……？
    voice "sp90_s1549_051"
    th "Hm? This perfume is the same as Louise's…?{#sp90_s1549_051}"

    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # ……んんっ？んんんん？ま、まさか！
    voice "sp90_s1549_053"
    th "…Mm? Mmmmm? N-No way!{#sp90_s1549_053}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay4     image=+555, level=160, dir=1A]
    # ど、どうした？モンモランシー？
    voice "sp90_s1549_056"
    th "W-What's wrong, Montmorency?{#sp90_s1549_056}"

    # ……まさか、これって使い魔の彼？
    voice "sp90_s1549_057"
    th "…No way. Is this… that familiar of hers?{#sp90_s1549_057}"

    # （……ば、バレた。おしまいだ。グッバイ、俺の青春っ！）[SPRITE   lay4     image=+55
    s "(…B-Busted. It's over. Goodbye, my youth!){#sp90_s1549_058}"

    # ……へっ？な、ななな、なんだってぇぇぇっ！
    voice "sp90_s1549_059"
    th "…Huh? W-Wh-Wh-What did you say!?{#sp90_s1549_059}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ……さ、さすがチェック厳しいわね。
    voice "sp90_s1549_062"
    l "…Y-You certainly are thorough.{#sp90_s1549_062}"

    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # 香水のモンモランシーをなめないことね。……けど、まあよく作ったものね。男の子だなんて分からないわよ。
    voice "sp90_s1549_064"
    th "Don't underestimate Montmorency the Fragrance. …But, well, you did a good job. No one would guess you're a boy.{#sp90_s1549_064}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay4     image=+572, level=160, dir=2A]
    # ど、どういうことだ！まさかこの女性が……サイトだなんて……。
    voice "sp90_s1549_067"
    th "W-What's the meaning of this! Don't tell me this woman is… Saito…{#sp90_s1549_067}"

    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # まったく、今日ばかりはあきれたわ。男を口説くなんて……。
    voice "sp90_s1549_069"
    th "Really, you never cease to amaze me — trying to pick up a man like that…{#sp90_s1549_069}"

    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # こ、こんなに清楚で可憐なのに……。
    voice "sp90_s1549_071"
    th "S-So neat and lovely, too…{#sp90_s1549_071}"


    menu:
        "First of all, let go of her hand, Guiche.{#sp90_c_1549_1665}":
            jump sp90_scene_1665
        "How do you like it, Guiche-sama?{#sp90_c_1549_1666}":
            jump sp90_scene_1666
        "…W-What's with this atmosphere!{#sp90_c_1549_1667}":
            jump sp90_scene_1667

label sp90_scene_1550:

    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # ……なにか言い訳は？わたしは寛大だから、言い訳くらい聞いてあげるわ！
    voice "sp90_s1550_003"
    l "…Any excuses? I'm generous, so I'll hear you out.{#sp90_s1550_003}"

    # な、なにいってるんだ？ルイズ！
    voice "sp90_s1550_004"
    s "W-What are you talking about, Louise?!{#sp90_s1550_004}"

    # ルイズぅ？ご主人様でしょっ！
    voice "sp90_s1550_005"
    l "Louise~? It's 'Master', isn't it!{#sp90_s1550_005}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # [TRANS trans("crossfade", 1000)]
    # きゃいんっ！
    voice "sp90_s1550_011"
    s "Kyaa!{#sp90_s1550_011}"

    # 返事は『わん』よっ！
    voice "sp90_s1550_012"
    l "The answer is 'woof'!{#sp90_s1550_012}"

    # ……くっ……わんっ！
    voice "sp90_s1550_013"
    s "…Ugh… woof!{#sp90_s1550_013}"

    # ……いいかしら？
    voice "sp90_s1550_014"
    l "…Are we clear?{#sp90_s1550_014}"

    # バカ犬のその口を開くときは『わん』と『ご主人様』ってつけなさい！
    voice "sp90_s1550_015"
    l "When that stupid dog opens its mouth, it should say 'woof' and 'Master'!{#sp90_s1550_015}"


    menu:
        "T-That's tyrannical!{#sp90_c_1550_1673}":
            jump sp90_scene_1673
        "Woof! Master!{#sp90_c_1550_1674}":
            jump sp90_scene_1674
        "I didn't do anything wrong!{#sp90_c_1550_1675}":
            jump sp90_scene_1675

label sp90_scene_1551:

    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # 少しは反省したらどうなのっ！
    voice "sp90_s1551_003"
    l "Don't you think you should show some remorse?!{#sp90_s1551_003}"

    # な、なんで俺が反省を……。
    voice "sp90_s1551_004"
    s "W-Why should I be the one repenting…{#sp90_s1551_004}"

    # ふぅーん。それじゃあ、新しい魔法の実験台にでもなってもらおうかしら？
    voice "sp90_s1551_005"
    l "Huuuh. In that case, how would you like to be the test subject for my new spell?{#sp90_s1551_005}"

    # はい、反省させていただきます。
    voice "sp90_s1551_006"
    s "Yes, I'll be sure to repent.{#sp90_s1551_006}"

    # うふふ。それでよしっ！じゃあ、復唱しなさい！
    voice "sp90_s1551_007"
    l "Ufufu. Good! Now then, repeat after me!{#sp90_s1551_007}"

    # これまでのご主人様への数々の失礼な態度、まことに申し訳ありませんでした。
    voice "sp90_s1551_008"
    l "For all the rude behavior I've shown my Master until now, I'm truly sorry.{#sp90_s1551_008}"

    # さあ、復唱よっ。
    voice "sp90_s1551_009"
    l "Come on, repeat it!{#sp90_s1551_009}"

    # これまでの……、
    voice "sp90_s1551_010"
    s "For all the…{#sp90_s1551_010}"


    menu:
        "All my rude behavior toward my Master…{#sp90_c_1551_1681}":
            jump sp90_scene_1681
        "My Master's various rude behaviors…{#sp90_c_1551_1682}":
            jump sp90_scene_1682
        "The various attitudes of a rude Master…{#sp90_c_1551_1683}":
            jump sp90_scene_1683

label sp90_scene_1552:

    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # 聞きなさい。あなた、このまえの洗濯のときの模様をみちゃったの。
    voice "sp90_s1552_003"
    l "Listen. I saw the way you looked while doing the laundry the other day.{#sp90_s1552_003}"

    # ……は？
    voice "sp90_s1552_004"
    s "…Huh?{#sp90_s1552_004}"

    # （待て、俺、ルイズの洗濯をしてるときに何かやってしまったっけ？）
    s "(Wait. Did I do something when I was doing Louise's laundry?){#sp90_s1552_005}"

    # わたしの服を洗ってくれる、それは使い魔として当然の好意だわ。ただ……。
    voice "sp90_s1552_006"
    l "Doing my laundry for me — that's only natural for a familiar. But…{#sp90_s1552_006}"

    # ただ？
    voice "sp90_s1552_007"
    s "But?{#sp90_s1552_007}"

    # [EVENT_CG event    image=+177, level=80]
    $ dissolve_fx("id(177)")
    # 誰もいないのを確認すると、わたしの服に頬ずりしてるのはどうかしら？
    voice "sp90_s1552_009"
    l "I wonder what to call it when someone makes sure no one's around, then rubs their cheek against my clothes?{#sp90_s1552_009}"

    # と思っただけ。言うまい、言うまいと思っていたけど、このまま胸にしまっておくのも無理なようね。
    voice "sp90_s1552_010"
    l "I just thought that. I was trying not to say it, but I can't exactly keep it to myself.{#sp90_s1552_010}"

    # （ま、まじかよ。俺、そんなことしてたっけ？）
    s "(N-No way. Did I really do something like that?){#sp90_s1552_011}"


    menu:
        "Let's run. To the ends of the earth.{#sp90_c_1552_1689}":
            jump sp90_scene_1689
        "Try to talk my way out of it.{#sp90_c_1552_1690}":
            jump sp90_scene_1690
        "Play dumb!{#sp90_c_1552_1691}":
            jump sp90_scene_1691

label sp90_scene_1553:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # 話せば分かる！
    voice "sp90_s1553_002"
    s "If you'd just talk to me, you'd understand!{#sp90_s1553_002}"

    # 問答無用！
    voice "sp90_s1553_003"
    l "No arguments!{#sp90_s1553_003}"

    # [SE       se0      play=+61]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # ぐはっ！
    voice "sp90_s1553_014"
    s "Guh!{#sp90_s1553_014}"

    # → next scene 1556
    jump sp90_scene_1556

label sp90_scene_1554:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # 横暴だぞっ！
    voice "sp90_s1554_002"
    s "That's tyrannical!{#sp90_s1554_002}"

    # 横暴？使い魔をどう扱おうとわたしの勝手よっ！
    voice "sp90_s1554_003"
    l "Tyrannical? It's my business how I treat my familiar!{#sp90_s1554_003}"

    # [SE       se0      play=+61]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # ぐぎゃっ！
    voice "sp90_s1554_014"
    s "Gugyaa!{#sp90_s1554_014}"

    # → next scene 1556
    jump sp90_scene_1556

label sp90_scene_1555:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # （ここは無抵抗主義で……）
    s "(Non-resistance, that's the way to go…){#sp90_s1555_002}"

    # あら。いいわけも抵抗もなし？
    voice "sp90_s1555_003"
    l "My. No excuses and no resistance?{#sp90_s1555_003}"

    # ……。
    voice "sp90_s1555_004"
    s "…{#sp90_s1555_004}"

    # そう……。いい心がけだわ。
    voice "sp90_s1555_005"
    l "I see… That's a good attitude.{#sp90_s1555_005}"

    # まあ、だからといって手加減なんてしないけど。
    voice "sp90_s1555_006"
    l "Well, that doesn't mean I'll go easy on you, though.{#sp90_s1555_006}"

    # えっ？い、いや、そこはほら、多少は、その……。
    voice "sp90_s1555_007"
    s "Eh? N-No, I mean, maybe just a little, you know, so…{#sp90_s1555_007}"

    # [SE       se0      play=+61]
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
    # げふぅっっ！
    voice "sp90_s1555_018"
    s "Gufuuh!{#sp90_s1555_018}"

    # → next scene 1556
    jump sp90_scene_1556

label sp90_scene_1556:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # 馬鹿っ！馬鹿っ！
    voice "sp90_s1556_002"
    l "Idiot! Idiot!{#sp90_s1556_002}"

    # [SE       se0      play=+61]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # いだだっ！
    voice "sp90_s1556_013"
    s "Ow!{#sp90_s1556_013}"

    # 大馬鹿っ！！
    voice "sp90_s1556_014"
    l "Great big idiot!!{#sp90_s1556_014}"

    # [SE       se0      play=+61]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # うぎゃっ！！
    voice "sp90_s1556_025"
    s "Ugyah!!{#sp90_s1556_025}"

    # ちょっとは反省しなさいっ！！
    voice "sp90_s1556_026"
    l "Show a little remorse, will you!!{#sp90_s1556_026}"

    # [SE       se0      play=+61]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # いだだっ！！いだだただだだだっ！
    voice "sp90_s1556_037"
    s "Ow!! Ouch, ouch, ouch, ouch!{#sp90_s1556_037}"

    # したっ！反省した！しましたっっ！！
    voice "sp90_s1556_038"
    s "I did! I repented! I repented, I tell you!!{#sp90_s1556_038}"

    # ……はぁ……はぁ……はぁ……。
    voice "sp90_s1556_039"
    l "…Haa… haa… haa…{#sp90_s1556_039}"

    # ねえ、サイト。
    voice "sp90_s1556_040"
    l "Say, Saito.{#sp90_s1556_040}"

    # は、はいっ！なんでしょう！
    voice "sp90_s1556_041"
    s "Y-Yes! What is it?!{#sp90_s1556_041}"

    # 覚えの悪い犬に、もう一度だけ質問するわ。
    voice "sp90_s1556_042"
    l "I'll ask this slow dog just one more question.{#sp90_s1556_042}"

    # はいっ！なんなりとっっ！！
    voice "sp90_s1556_043"
    s "Yes! Anything at all!!{#sp90_s1556_043}"

    # [EVENT_CG event    image=+163, level=80]
    $ dissolve_fx("id(163)")
    # あなたのご主人は誰だったかしら？
    voice "sp90_s1556_045"
    l "Who was your master, again?{#sp90_s1556_045}"

    # そ、それはもちろん……。
    voice "sp90_s1556_046"
    s "T-That's, of course…{#sp90_s1556_046}"


    menu:
        "The beautiful and lovely Louise-sama.{#sp90_c_1556_1557}":
            jump sp90_scene_1557
        "The wise and forgiving Louise-sama.{#sp90_c_1556_1558}":
            jump sp90_scene_1558
        "The violent and flat-chested Louise-sama.{#sp90_c_1556_1559}":
            jump sp90_scene_1559

label sp90_scene_1557:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+163, level=80]
    $ dissolve_fx("id(163)")
    # 美しく可憐なルイズ様です。
    voice "sp90_s1557_002"
    s "The beautiful and lovely Louise-sama.{#sp90_s1557_002}"

    # [EVENT_CG event    image=+162, level=80]
    $ dissolve_fx("id(162)")
    # えっ！？
    voice "sp90_s1557_004"
    l "Eh!?{#sp90_s1557_004}"

    # ああ！俺はこんな人の使い魔になれて幸せだなぁっ！
    voice "sp90_s1557_005"
    s "Ah! I'm so happy to be the familiar of someone like you!{#sp90_s1557_005}"

    # お、おだてたって、ゆ、許さないんだから……。
    voice "sp90_s1557_006"
    l "F-Flattery won't get you anywhere. I won't forgive you…{#sp90_s1557_006}"

    # お世辞じゃないです。本心です。
    voice "sp90_s1557_007"
    s "It's not flattery. I mean it.{#sp90_s1557_007}"

    # ま、まあ、でも、今日はこんなところでいいかしらね。
    voice "sp90_s1557_008"
    l "W-Well, but… I suppose today can end here.{#sp90_s1557_008}"

    # （ほっ……。助かった……）→ next scene 1560
    s "(Phew… I made it…){#sp90_s1557_009}"

label sp90_scene_1558:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+163, level=80]
    $ dissolve_fx("id(163)")
    # 聡明で寛容なルイズ様です。
    voice "sp90_s1558_002"
    s "The wise and forgiving Louise-sama.{#sp90_s1558_002}"

    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # あら、分かってきたじゃない。最初からそういう殊勝な態度をとっておけば良かったのよ。
    voice "sp90_s1558_004"
    l "My, look who's learning. You should have behaved yourself like that from the start.{#sp90_s1558_004}"

    # 慈悲深きご主人様、どうかこの哀れな犬っころをお許しください。
    voice "sp90_s1558_005"
    s "O merciful Master, please forgive this pitiful little dog.{#sp90_s1558_005}"

    # いいわ。許してあげる。でも、今回だけよ。
    voice "sp90_s1558_006"
    l "Fine. I forgive you. But just this once.{#sp90_s1558_006}"

    # → next scene 1560
    jump sp90_scene_1560

label sp90_scene_1559:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+163, level=80]
    $ dissolve_fx("id(163)")
    # 凶暴で貧乳のルイズ様です。
    voice "sp90_s1559_002"
    s "The violent and flat-chested Louise-sama.{#sp90_s1559_002}"

    # そうそう、分かれば……って！誰が凶暴で貧乳よっっ！
    voice "sp90_s1559_003"
    l "That's right, now you're getting it— wait! Who are you calling violent and flat-chested?!{#sp90_s1559_003}"

    # ええっと……。ご主人様……顔が、怖いです……よ？
    voice "sp90_s1559_004"
    s "Um… Master… your face is scary… I think?{#sp90_s1559_004}"

    # ……そう。分かったわ。あくまでそういう態度なのね。
    voice "sp90_s1559_005"
    l "…I see. I understand. So that's the attitude you're sticking with.{#sp90_s1559_005}"

    # あ、い、いや、やっぱ今のナシ！
    voice "sp90_s1559_006"
    s "Ah, n-no, never mind what I just said!{#sp90_s1559_006}"

    # だったら、こっちにも考えがあるわ。
    voice "sp90_s1559_007"
    l "Then I have an idea of my own.{#sp90_s1559_007}"

    # 冗談！ギャグ！イッツアジョーク！！
    voice "sp90_s1559_008"
    s "I'm joking! It's a gag! It's a joke!!{#sp90_s1559_008}"

    # もう遅いわよっ！！
    voice "sp90_s1559_009"
    l "It's too late!!{#sp90_s1559_009}"

    # 覚えの悪いバカ犬は、徹底的にしつけてあげるわっっ！！
    voice "sp90_s1559_010"
    l "A slow-witted stupid dog like you needs to be thoroughly trained!!{#sp90_s1559_010}"

    # [SE       se0      play=+61]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # ぎぃぃぃぃやぁぁぁぁぁぁぁっっっ！！
    voice "sp90_s1559_021"
    s "Gyyyyaaaaah!!{#sp90_s1559_021}"

    # → next scene 1560
    jump sp90_scene_1560

label sp90_scene_1560:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+162, level=80]
    $ dissolve_fx("id(162)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1561:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # す、隙あり！
    voice "sp90_s1561_002"
    s "An opening!{#sp90_s1561_002}"

    # 逃がさないわよ！
    voice "sp90_s1561_003"
    l "I won't let you get away!{#sp90_s1561_003}"

    # [SE       se0      play=+61]
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
    # ぐはっ！
    voice "sp90_s1561_014"
    s "Guh!{#sp90_s1561_014}"

    # → next scene 1564
    jump sp90_scene_1564

label sp90_scene_1562:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # む、無茶な命令には反対する権利があるっっっ！！
    voice "sp90_s1562_002"
    s "I have the right to object to unreasonable orders!!{#sp90_s1562_002}"

    # そんなものないわよっ！バカ犬のくせに生意気よっ！
    voice "sp90_s1562_003"
    l "You have no such right! Don't get cheeky with me, you stupid dog!{#sp90_s1562_003}"

    # [SE       se0      play=+61]
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
    # ぐぎゃっ！
    voice "sp90_s1562_014"
    s "Gugyaa!{#sp90_s1562_014}"

    # → next scene 1564
    jump sp90_scene_1564

label sp90_scene_1563:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # キャインキャイン！
    voice "sp90_s1563_002"
    s "Kyah! Kyah!{#sp90_s1563_002}"

    # ……な、なんのつもり？
    voice "sp90_s1563_003"
    l "…Wh-what are you trying to do?{#sp90_s1563_003}"

    # ほ、ほら。犬って降参のときはこうやって……。
    voice "sp90_s1563_004"
    s "S-see? That's how a dog acts when it surrenders…{#sp90_s1563_004}"

    # ふ～ん、そうそうアンタは犬だったわね。
    voice "sp90_s1563_005"
    l "Hmm~ That's right, you were a dog, weren't you.{#sp90_s1563_005}"

    # そ、そうそう。俺、犬。わんわんっ！
    voice "sp90_s1563_006"
    s "T-that's right. I'm a dog. Woof woof!{#sp90_s1563_006}"

    # だったら、ご主人様の言うことはちゃあんと聞かないとね。
    voice "sp90_s1563_007"
    l "Then you have to listen properly to your mistress, got it?{#sp90_s1563_007}"

    # えっ……あ……。ちょっと……。
    voice "sp90_s1563_008"
    s "Eh… ah… hold on…{#sp90_s1563_008}"

    # ……覚悟はいいわね？
    voice "sp90_s1563_009"
    l "…Ready for this?{#sp90_s1563_009}"

    # [SE       se0      play=+61]
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
    # ぐはっっ！
    voice "sp90_s1563_020"
    s "Guh!{#sp90_s1563_020}"

    # → next scene 1564
    jump sp90_scene_1564

label sp90_scene_1564:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # 反省して、わたしに謝りなさい！
    voice "sp90_s1564_002"
    l "Reflect on it and apologize to me!{#sp90_s1564_002}"

    # します！反省しました！謝ります！
    voice "sp90_s1564_003"
    s "I will! I'm sorry! I apologize!{#sp90_s1564_003}"

    # 誠意が感じられないのよっ！！
    voice "sp90_s1564_004"
    l "I don't feel any sincerity!!{#sp90_s1564_004}"

    # りっ、理不尽なぁっ！
    voice "sp90_s1564_005"
    s "Th-that's unreasonable!{#sp90_s1564_005}"

    # [EVENT_CG event    image=+163, level=80]
    $ dissolve_fx("id(163)")
    # こ、これでも喰らいなさいっ！
    voice "sp90_s1564_007"
    l "T-take this too!{#sp90_s1564_007}"

    # ……っ！
    voice "sp90_s1564_008"
    l "…!{#sp90_s1564_008}"

    # だあっ、魔法は反則っっ！
    voice "sp90_s1564_009"
    s "Hey! Magic is cheating!{#sp90_s1564_009}"

    # [SE       se0      play=+95]
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
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # ……はぁ……はぁ……はぁ……。
    voice "sp90_s1564_024"
    l "…Haah… haah… haah…{#sp90_s1564_024}"

    # こ、殺す気かよ！
    voice "sp90_s1564_025"
    s "Y-you're trying to kill me!{#sp90_s1564_025}"

    # さあ、サイト！あなたのご主人様はどんなご主人様？
    voice "sp90_s1564_026"
    l "Now, Saito! What kind of mistress is your mistress?{#sp90_s1564_026}"

    # ルイズ様は……、
    voice "sp90_s1564_027"
    s "Louise-sama is…{#sp90_s1564_027}"


    menu:
        "My cute mistress!{#sp90_c_1564_1565}":
            jump sp90_scene_1565
        "My kind mistress!{#sp90_c_1564_1566}":
            jump sp90_scene_1566
        "My unreasonable mistress!{#sp90_c_1564_1567}":
            jump sp90_scene_1567

label sp90_scene_1565:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # 俺のかわいいご主人様です！
    voice "sp90_s1565_002"
    s "My cute mistress!{#sp90_s1565_002}"

    # [EVENT_CG event    image=+162, level=80]
    $ dissolve_fx("id(162)")
    # ……うっ。
    voice "sp90_s1565_004"
    l "…Ugh.{#sp90_s1565_004}"

    # なっ、なによ！？それは！ま、またからかってるんでしょ！
    voice "sp90_s1565_005"
    l "Wh-what was that!? You're teasing me again, aren't you!{#sp90_s1565_005}"

    # そんなふうに言っても、ゆ、許さないんだからね！
    voice "sp90_s1565_006"
    l "Say it all you want, I still won't forgive you! N-not a chance!{#sp90_s1565_006}"

    # でも、全部本当のことだろ！
    voice "sp90_s1565_007"
    s "But it's all true, isn't it!{#sp90_s1565_007}"

    # ええ、そうよっ！
    voice "sp90_s1565_008"
    l "N-no, it isn't!{#sp90_s1565_008}"

    # サ、サイトが分かればいいのよ！
    voice "sp90_s1565_009"
    l "I-it's fine as long as Saito understands!{#sp90_s1565_009}"

    # けどっ！
    voice "sp90_s1565_010"
    l "B-but!{#sp90_s1565_010}"

    # 次にこんな事があったら、本当に許さないんだからねっ！
    voice "sp90_s1565_011"
    l "If you ever do this again, I really won't forgive you!{#sp90_s1565_011}"

    # → next scene 1568
    jump sp90_scene_1568

label sp90_scene_1566:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # 俺の優しいご主人様です！
    voice "sp90_s1566_002"
    s "My kind mistress!{#sp90_s1566_002}"

    # ……ふん、分かればいいのよ。最初からそういう態度ならね。
    voice "sp90_s1566_003"
    l "…Hmph. Fine, as long as you understand. If you'd acted like that from the start.{#sp90_s1566_003}"

    # わんわん！どうぞ、犬めとお呼びください。
    voice "sp90_s1566_004"
    s "Woof woof! Please, call me 'dog'.{#sp90_s1566_004}"

    # はあっ、もういいわよ。許してあげる。でも、本当に今回だけよ。
    voice "sp90_s1566_005"
    l "Hah, enough. I'll forgive you. But just this once, really.{#sp90_s1566_005}"

    # 次に他の女にしっぽ振ってご覧なさい！分かってるわねっ！
    voice "sp90_s1566_006"
    l "Just try wagging your tail at another girl again! You understand me, don't you!{#sp90_s1566_006}"

    # きっ、きゃいん！
    voice "sp90_s1566_007"
    s "K-Kyah!{#sp90_s1566_007}"

    # わんわん！！
    voice "sp90_s1566_008"
    s "Woof woof!!{#sp90_s1566_008}"

    # → next scene 1568
    jump sp90_scene_1568

label sp90_scene_1567:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # 俺の理不尽なご主人様です。
    voice "sp90_s1567_002"
    s "My unreasonable mistress.{#sp90_s1567_002}"

    # ……リフジン？聞き間違いかしら。な、なにか変な声が聞こえた気がしたけど。
    voice "sp90_s1567_003"
    l "…Rifujin? Did I mishear? I thought I heard something odd just now.{#sp90_s1567_003}"

    # 念のために聞いてあげるから、もう一度、言ってみなさい！
    voice "sp90_s1567_004"
    l "Just to be sure, I'll let you say it again. Try once more!{#sp90_s1567_004}"

    # ル、ルイズ様は……、俺の理不尽なご主人様です！
    voice "sp90_s1567_005"
    s "L-Louise-sama is… my unreasonable mistress!{#sp90_s1567_005}"

    # ……いい度胸ね。
    voice "sp90_s1567_006"
    l "…You've got some nerve.{#sp90_s1567_006}"

    # 随分、お仕置きしてあげたと思ってたんだけど……。
    voice "sp90_s1567_007"
    l "I thought I'd punished you quite a bit…{#sp90_s1567_007}"

    # [EVENT_CG event    image=+163, level=80]
    $ dissolve_fx("id(163)")
    # 全然っ、足りてなかったってワケね？
    voice "sp90_s1567_009"
    l "Apparently it was nowhere near enough!{#sp90_s1567_009}"

    # お顔が、なんだか……、スゴイコトニナッテマスヨ……？
    voice "sp90_s1567_010"
    s "Your face is, like… getting all scary…?{#sp90_s1567_010}"

    # ……ご、ごっ、ごめん。や、やっぱ今の間違いっ！
    voice "sp90_s1567_011"
    s "…I-I'm… sorry. I-I take it back!{#sp90_s1567_011}"

    # 問答無用っ！！
    voice "sp90_s1567_012"
    l "No arguments!!{#sp90_s1567_012}"

    # 今日という今日は！徹底的にしつけてあげるっっ！！
    voice "sp90_s1567_013"
    l "Today of all days—I'll train you thoroughly!!{#sp90_s1567_013}"

    # [SE       se0      play=+61]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # ぐぎぃぃぃぃやぁぁぁぁぁぁっっっ！！
    voice "sp90_s1567_024"
    s "Guhiiii—yaaaaah!!{#sp90_s1567_024}"

    # → next scene 1568
    jump sp90_scene_1568

label sp90_scene_1568:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+162, level=80]
    $ dissolve_fx("id(162)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1569:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # （脱出するっっ！！）
    s "(I'm getting out of here!!){#sp90_s1569_002}"

    # さ、さようなら！アデュ～～！
    voice "sp90_s1569_003"
    s "S-see you! Adieu~~!{#sp90_s1569_003}"

    # どこに行く気よ！に、逃がすもんですか！
    voice "sp90_s1569_004"
    l "Where do you think you're going! As if I'd let you go!{#sp90_s1569_004}"

    # [SE       se0      play=+61]
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
    # ぐはっ！
    voice "sp90_s1569_015"
    s "Guh!{#sp90_s1569_015}"

    # → next scene 1572
    jump sp90_scene_1572

label sp90_scene_1570:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # （……そ、そうだ。こんなときは相手をひるませて、脱出路を作るのだ！）
    s "(…Th-that's it. In a case like this, you stun your opponent and create an escape route!){#sp90_s1570_002}"

    # タックルー！
    voice "sp90_s1570_003"
    s "Tackle!{#sp90_s1570_003}"

    # ……いっ、いやぁぁっ！！むかってこないで！
    voice "sp90_s1570_004"
    l "…D-don't! Stay back!!{#sp90_s1570_004}"

    # [SE       se0      play=+61]
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
    # きゃ、ぎゃーんっ！
    voice "sp90_s1570_015"
    s "Kya—gyahn!{#sp90_s1570_015}"

    # ……な、なななな何するのよ！このっ、バカ犬っ！
    voice "sp90_s1570_016"
    l "…Wh-what are you doing! You— stupid dog!{#sp90_s1570_016}"

    # くそっ、俺の大事なところにクリーンヒットが！！何かうらみでもあるのか！
    voice "sp90_s1570_017"
    s "Damn—a clean hit right where it hurts!! What, do you have a grudge against me?!{#sp90_s1570_017}"

    # → next scene 1572
    jump sp90_scene_1572

label sp90_scene_1571:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # ひっ、ひぃぃぃっ！！……バタッ。
    voice "sp90_s1571_002"
    s "H-hiiii!! …Thud.{#sp90_s1571_002}"

    # ななな、なによその態度！
    voice "sp90_s1571_003"
    l "Wh-what's with that attitude!{#sp90_s1571_003}"

    # ……。
    voice "sp90_s1571_004"
    s "…{#sp90_s1571_004}"

    # そんなふうに気絶したって許してあげないんだからね！
    voice "sp90_s1571_005"
    l "Even if you pass out like that, I won't forgive you, you know!{#sp90_s1571_005}"

    # [SE       se0      play=+61]
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
    # ぐはっっ！
    voice "sp90_s1571_016"
    s "Guh!{#sp90_s1571_016}"

    # 目は覚めたかしら？
    voice "sp90_s1571_017"
    l "Have you come to?{#sp90_s1571_017}"

    # → next scene 1572
    jump sp90_scene_1572

label sp90_scene_1572:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # そ、そんなしっぽ……。
    voice "sp90_s1572_002"
    l "T-that tail of yours…{#sp90_s1572_002}"

    # に、二度とほいほい振れないようにしてあげるわ！
    voice "sp90_s1572_003"
    l "I'll make sure you never wag it again!{#sp90_s1572_003}"

    # [SE       se0      play=+61]
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
    # ぐぎゃぁぁぁぁぁっっっ！！そこはしっぽじゃなくてぇぇぇぇぇっっっ！！
    voice "sp90_s1572_014"
    s "Guhyaaaa!! That's not my tail!!{#sp90_s1572_014}"

    # ……嫌い！嫌い！バカ犬なんて大嫌いなんだから！
    voice "sp90_s1572_015"
    l "I hate it! I hate it! I hate stupid dogs!{#sp90_s1572_015}"

    # [SE       se0      play=+61]
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
    # ぎえええぇーーっ！
    voice "sp90_s1572_026"
    s "Gieee—!{#sp90_s1572_026}"

    # ちょっとかわいい女の子と見ればふらふらしちゃって！
    voice "sp90_s1572_027"
    l "One look at a cute girl and you go all weak in the knees!{#sp90_s1572_027}"

    # こ、こ、こ、これ以上は……男の尊厳が……。
    voice "sp90_s1572_028"
    s "T-this is… a man's dignity…{#sp90_s1572_028}"

    # あんたのご主人様がだれなのかっ！たっぷり体に教え込んであげるんだからーーーっっ！！
    voice "sp90_s1572_029"
    l "Who your mistress is—I'll teach it to your body thoroughly!!{#sp90_s1572_029}"

    # [SE       se0      play=+61]
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
    # ぎゃぁぁぁぁぁぁっっっっ！！
    voice "sp90_s1572_040"
    s "Gyaaaa!!{#sp90_s1572_040}"

    # は、反省します！ご、ご主人様はルイズ様です！唯一絶対です！
    voice "sp90_s1572_041"
    s "I-I'm sorry! My mistress is Louise-sama! The one and only!{#sp90_s1572_041}"

    # だ、だからご主人様！せ、せめてもう少し優しくっっ！
    voice "sp90_s1572_042"
    s "S-so, mistress! At least be a little gentler!!{#sp90_s1572_042}"

    # わ、分かればいいのよ！わ、分かれば。
    voice "sp90_s1572_043"
    l "F-fine, as long as you understand! Th-that's enough.{#sp90_s1572_043}"

    # ひ……ひい……。た、助かった……。
    voice "sp90_s1572_044"
    s "Hee… hee… I-I survived…{#sp90_s1572_044}"

    # [EVENT_CG event    image=+163, level=80]
    $ dissolve_fx("id(163)")
    # ……さあ、サイト。もう一度聞いてあげる。
    voice "sp90_s1572_046"
    l "…Now, Saito. I'll ask you once more.{#sp90_s1572_046}"

    # バカ犬のご主人様はだれ？……わたしは、サイトのなに？
    voice "sp90_s1572_047"
    l "Who's the stupid dog's mistress? …And what am I to you, Saito?{#sp90_s1572_047}"

    # う、うっ……。
    voice "sp90_s1572_048"
    s "U-ugh…{#sp90_s1572_048}"


    menu:
        "Lovely Louise-sama!{#sp90_c_1572_1573}":
            jump sp90_scene_1573
        "Lovely mistress!{#sp90_c_1572_1574}":
            jump sp90_scene_1574
        "Lovely queen!{#sp90_c_1572_1575}":
            jump sp90_scene_1575

label sp90_scene_1573:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+163, level=80]
    $ dissolve_fx("id(163)")
    # ……お、俺のご主人様は、
    voice "sp90_s1573_002"
    s "…M-my mistress is,{#sp90_s1573_002}"

    # う、麗しのルイズ様です！
    voice "sp90_s1573_003"
    s "u—lovely Louise-sama!{#sp90_s1573_003}"

    # [EVENT_CG event    image=+162, level=80]
    $ dissolve_fx("id(162)")
    # ……そ、そうよ。分かればいいのよ、分かれば。
    voice "sp90_s1573_005"
    l "…T-that's right. As long as you understand, that's all.{#sp90_s1573_005}"

    # バ、バカ犬のご主人様は、世界でたった一人。このわたししかいないんだからね！
    voice "sp90_s1573_006"
    l "The stupid dog's mistress is the only one in the world. There's no one but me, got it!{#sp90_s1573_006}"

    # → next scene 1576
    jump sp90_scene_1576

label sp90_scene_1574:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+163, level=80]
    $ dissolve_fx("id(163)")
    # ル、ルイズ様は俺の……、麗しのご主人様です！
    voice "sp90_s1574_002"
    s "L-Louise-sama is my… lovely mistress!{#sp90_s1574_002}"

    # ……そ、それでいいのよ！
    voice "sp90_s1574_003"
    l "…T-that's fine with me!{#sp90_s1574_003}"

    # ち、ちくしょう……ご主人様、最高ぉ！バンザーイ！ブラボー！
    voice "sp90_s1574_004"
    s "D-damn… Mistress is the best! Banzai! Bravo!{#sp90_s1574_004}"

    # ……なによ、その態度。まだお仕置きが足りなかったかしら？
    voice "sp90_s1574_005"
    l "…What's with that attitude? I didn't punish you enough, did I?{#sp90_s1574_005}"

    # ……それとも。まさか、変なクセとかついたんじゃないでしょうね？
    voice "sp90_s1574_006"
    l "…Or maybe. You didn't pick up some weird habit, did you?{#sp90_s1574_006}"

    # 滅相もないっ！！俺は最初からご主人様にメロメロです！
    voice "sp90_s1574_007"
    s "Perish the thought!! I've been head over heels for my mistress from the very start!{#sp90_s1574_007}"

    # [EVENT_CG event    image=+161, level=80]
    $ dissolve_fx("id(161)")
    # まあ、いいけど……。
    voice "sp90_s1574_009"
    l "Well, fine…{#sp90_s1574_009}"

    # とにかくっ！バカ犬は、ご主人様だけ見ていればいいのっ！分かった？
    voice "sp90_s1574_010"
    l "Anyway! The stupid dog only needs to look at his mistress! Got it?{#sp90_s1574_010}"

    # わ、わんわんっ！！
    voice "sp90_s1574_011"
    s "W-woof woof!!{#sp90_s1574_011}"

    # → next scene 1576
    jump sp90_scene_1576

label sp90_scene_1575:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+163, level=80]
    $ dissolve_fx("id(163)")
    # ……お、俺のご主人様は、
    voice "sp90_s1575_002"
    s "…M-my mistress is,{#sp90_s1575_002}"

    # 麗しの女王様です！
    voice "sp90_s1575_003"
    s "Lovely queen!{#sp90_s1575_003}"

    # なんですって！まさかあんた、女王様にまで色目を！
    voice "sp90_s1575_004"
    l "What was that?! Don't tell me you're making eyes at a queen too!{#sp90_s1575_004}"

    # え？いや、そういう意味じゃなくて……。
    voice "sp90_s1575_005"
    s "Huh? No, I didn't mean it like that…{#sp90_s1575_005}"

    # ……よ、よくもまぁ……。学院の女の子だけでは飽き足らず、アンリエッタ様まで毒牙にかける気なのね！
    voice "sp90_s1575_006"
    l "…How dare you… Not content with the girls at the academy, now you want to sink your fangs into Henrietta-sama too!{#sp90_s1575_006}"

    # い、いや。あの、その……。
    voice "sp90_s1575_007"
    s "N-no. I mean, that…{#sp90_s1575_007}"

    # この身の程知らずのバカ犬には、念入りにお仕置きしないとね！
    voice "sp90_s1575_008"
    l "This presumptuous stupid dog needs a really thorough punishment!{#sp90_s1575_008}"

    # ル、ルイズっ！ち、違う！御慈悲をっっ！！
    voice "sp90_s1575_009"
    s "L-Louise! N-no, that's not it! Mercy!!{#sp90_s1575_009}"

    # ……ご、ご主人様って呼びなさい！
    voice "sp90_s1575_010"
    l "…C-call me mistress!{#sp90_s1575_010}"

    # [SE       se0      play=+61]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # ぎぃぃぃぃやぁぁぁぁぁぁっっっ！！
    voice "sp90_s1575_021"
    s "Ghiii—yaaaaah!!{#sp90_s1575_021}"

    # → next scene 1576
    jump sp90_scene_1576

label sp90_scene_1576:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+162, level=80]
    $ dissolve_fx("id(162)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1577:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # に、逃げるに決まってるだろっ！って、鍵が開かない！！
    voice "sp90_s1577_002"
    s "O-of course I'm going to escape! But the lock won't open!!{#sp90_s1577_002}"

    # ……逃げられるはずないでしょ？少しは学習しなさいっ！
    voice "sp90_s1577_003"
    l "…As if you could ever escape? Do a little learning for once!{#sp90_s1577_003}"

    # [SE       se0      play=+62]
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
    # い、いやぁぁぁぁぁぁっ！！
    voice "sp90_s1577_014"
    s "N-noooo!!{#sp90_s1577_014}"

    # → next scene 1580
    jump sp90_scene_1580

label sp90_scene_1578:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # く、首を洗って覚悟を決めるか……。
    voice "sp90_s1578_002"
    s "K-Kuh… wash your neck and brace yourself…{#sp90_s1578_002}"

    # あら？ずいぶんおとなしいのね？
    voice "sp90_s1578_003"
    l "Oh? My, you're being awfully well-behaved, aren't you?{#sp90_s1578_003}"

    # お、おうっ！
    voice "sp90_s1578_004"
    s "Y-Yeah!{#sp90_s1578_004}"

    # でも、お仕置きがなくなると思ったら、大間違いよ！
    voice "sp90_s1578_005"
    l "But if you thought that meant no more punishment, you're dead wrong!{#sp90_s1578_005}"

    # へ、へっ？？？
    voice "sp90_s1578_006"
    s "H-Huh???{#sp90_s1578_006}"

    # → next scene 1580
    jump sp90_scene_1580

label sp90_scene_1579:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # ち、ちくしょうっ！今でも犬の生活じゃないかっ！
    voice "sp90_s1579_002"
    s "D-Damn it! This is still a dog's life!{#sp90_s1579_002}"

    # ……な、なんですって！
    voice "sp90_s1579_003"
    l "……W-What did you say?!{#sp90_s1579_003}"

    # ふんっ！だったらホントの犬の生活になっても文句はないわよねっ！
    voice "sp90_s1579_004"
    l "Hmph! Then you won't mind if I give you a real dog's life, will you?!{#sp90_s1579_004}"

    # → next scene 1580
    jump sp90_scene_1580

label sp90_scene_1580:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # [TRANS trans("crossfade", 1000)]
    # ジャラ……ジャラララ……。
    th "Jingle… jingle-jingle-jingle…{#sp90_s1580_007}"

    # うふふ、なかなか似合うじゃない。
    voice "sp90_s1580_008"
    l "Ufufu, it actually suits you, doesn't it?{#sp90_s1580_008}"

    # く、首輪なんて、今すぐはずせ！
    voice "sp90_s1580_009"
    s "K-Kuh! Take this collar off me right now!{#sp90_s1580_009}"

    # うるさいっ！バカ犬っ！
    voice "sp90_s1580_010"
    l "Shut up! You stupid dog!{#sp90_s1580_010}"

    # [SE       se0      play=+61]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     hide, vibrate=14]
    # [SPRITE   lay1     hide, vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # くきゃっ！！！
    voice "sp90_s1580_021"
    s "G-Gyah!!!{#sp90_s1580_021}"

    # ご、ご主人様。く、鎖をゆるめてっ！首……吊ってる……。
    voice "sp90_s1580_022"
    s "M-Master! Kuh, loosen the chain! My neck… it's choking me…{#sp90_s1580_022}"

    # 男の子でしょっ！我慢しなさいっ！
    voice "sp90_s1580_023"
    l "You're a boy, aren't you?! Endure it!{#sp90_s1580_023}"

    # む、無茶言うなっ！
    voice "sp90_s1580_024"
    s "D-Don't be ridiculous!{#sp90_s1580_024}"

    # うふふ、なにか楽しいわね。コレ？
    voice "sp90_s1580_025"
    l "Ufufu, this is kind of fun, isn't it? This?{#sp90_s1580_025}"

    # ルイズっ、いやご主人様っ！その目やばい！目がイってるって！
    voice "sp90_s1580_026"
    s "Louise! I mean, Master! Those eyes are bad news! Your eyes are totally frenzied!{#sp90_s1580_026}"

    # 犬はワンでしょっ！バカ犬っ！やっぱりおしおきしかないのかしら？
    voice "sp90_s1580_027"
    l "Dogs go 'woof', don't they?! Stupid dog! I guess you really do need a punishment, hmm?{#sp90_s1580_027}"

    # [SE       se0      play=+71]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # ちょっ、ちょっと待てっ！ルイズぅぅっ！
    voice "sp90_s1580_038"
    s "W-Wait a second! L-Louise!!{#sp90_s1580_038}"

    # [EVENT_CG event    image=+167, level=80]
    $ dissolve_fx("id(167)")
    # さあ、バカ犬？お前は「ワン」しかいえないはずよね？
    voice "sp90_s1580_040"
    l "Come on, stupid dog. You can only say 'woof', right?{#sp90_s1580_040}"

    # （……ほ、本気の目だよ）
    s "Jingle… jingle-jingle-jingle…{#sp90_s1580_041}"

    # さあ、バカ犬？お返事は？
    voice "sp90_s1580_042"
    l "Well? Your answer, stupid dog?{#sp90_s1580_042}"


    menu:
        "Don't mess with me, Louise!{#sp90_c_1580_1581}":
            jump sp90_scene_1581
        "Woof woof woof!{#sp90_c_1580_1582}":
            jump sp90_scene_1582
        "Master! I need the bathroom!{#sp90_c_1580_1583}":
            jump sp90_scene_1583

label sp90_scene_1581:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+167, level=80]
    $ dissolve_fx("id(167)")
    # ふざけるな、ルイズ！これ以上、付き合うほどお人よしじゃねーぞ。
    voice "sp90_s1581_002"
    s "Don't mess with me, Louise! I'm not good-natured enough to put up with this any longer!{#sp90_s1581_002}"

    # バカ犬っ！しゃべるんじゃない！
    voice "sp90_s1581_003"
    l "Stupid dog! I told you not to talk!{#sp90_s1581_003}"

    # [SE       se0      play=+71]
    # パシィィィンっっ！[BG       stage    vibrate=14][EVENT_CG event 
    th "Smack!!!{#sp90_s1581_005}"

    # ぎゃぃーんっ！
    voice "sp90_s1581_006"
    s "Gyaaain!{#sp90_s1581_006}"

    # → next scene 1584
    jump sp90_scene_1584

label sp90_scene_1582:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+167, level=80]
    $ dissolve_fx("id(167)")
    # わんわんわん！
    voice "sp90_s1582_002"
    s "Woof woof woof!{#sp90_s1582_002}"

    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # ……あ～ら、よくできたわね。バカ犬にしては上出来よ？
    voice "sp90_s1582_004"
    l "……Oh my, well done. Not bad for a stupid dog, hmm?{#sp90_s1582_004}"

    # わんっ！
    voice "sp90_s1582_005"
    s "Woof!{#sp90_s1582_005}"

    # （ちっ、ちくしょうっ！）[EVENT_CG event    image=+167, level=80]
    s "(Tch, damn it!){#sp90_s1582_006}"

    # なによその目はっ！歯向かうなら、即お仕置きよ！
    voice "sp90_s1582_007"
    l "What's with that look?! If you're going to defy me, that's an instant punishment!{#sp90_s1582_007}"

    # → next scene 1584
    jump sp90_scene_1584

label sp90_scene_1583:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+167, level=80]
    $ dissolve_fx("id(167)")
    # ご主人様っ、トイレっ！
    voice "sp90_s1583_002"
    s "Master! I need the bathroom!{#sp90_s1583_002}"

    # ま、まじめに言ってるの？
    voice "sp90_s1583_003"
    l "A-Are you serious?{#sp90_s1583_003}"

    # ……しょうがねーだろ？トイレはトイレなんだ。
    voice "sp90_s1583_004"
    s "……Can't be helped, right? When you gotta go, you gotta go.{#sp90_s1583_004}"

    # ごごご、ご主人様にっ！なんて口を聞いてるの？お、おしおきなんだからっ！
    voice "sp90_s1583_005"
    l "M-M-Master! How dare you talk to me like that?! I-I'm punishing you, you know!{#sp90_s1583_005}"

    # [SE       se0      play=+71]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # パシィィィンっっ！
    th "Smack!!!{#sp90_s1583_016}"

    # きゃぃーん！
    voice "sp90_s1583_017"
    s "Kyaain!{#sp90_s1583_017}"

    # → next scene 1584
    jump sp90_scene_1584

label sp90_scene_1584:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+167, level=80]
    $ dissolve_fx("id(167)")
    # えいっ！えいっ！えいっ！
    voice "sp90_s1584_002"
    l "Ei! Ei! Ei!{#sp90_s1584_002}"

    # [SE       se0      play=+71]
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
    # パシィィィンっっ！[SE       se0      play=+71][BG       stage   
    th "Smack!!{#sp90_s1584_013}"

    # パシィィィィィィンっっ！[SE       se0      play=+71][BG       stage
    th "Smack!!{#sp90_s1584_014}"

    # パシィィィィィィィィィンっっ！
    th "Smack!!{#sp90_s1584_015}"

    # ぎにゃあ！
    voice "sp90_s1584_016"
    s "Ginyaa!{#sp90_s1584_016}"

    # [EVENT_CG event    image=+166, level=80]
    $ dissolve_fx("id(166)")
    # ああっ、癖になりそう……。
    voice "sp90_s1584_018"
    l "Aah… I could get used to this…{#sp90_s1584_018}"

    # 勘弁してくれぇ……。
    voice "sp90_s1584_019"
    s "Have mercy… please…{#sp90_s1584_019}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1585:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # ……わ、わん！
    voice "sp90_s1585_002"
    s "……W-Woof!{#sp90_s1585_002}"

    # あらあら、物分かりがいいわね……。
    voice "sp90_s1585_003"
    l "My, my, you're a quick learner, aren't you…{#sp90_s1585_003}"

    # わんっ！
    voice "sp90_s1585_004"
    s "Woof!{#sp90_s1585_004}"

    # [EVENT_CG event    image=+166, level=80]
    $ dissolve_fx("id(166)")
    # ホントに。いつもそう従順だったら、もっとかわいがってあげられるのに……。
    voice "sp90_s1585_006"
    l "Really. If you were always this obedient, I could spoil you more…{#sp90_s1585_006}"

    # ……えっ？
    voice "sp90_s1585_007"
    s "……Huh?{#sp90_s1585_007}"

    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # 返事は『わん』でしょ！
    voice "sp90_s1585_009"
    l "Your answer is 'woof', isn't it!{#sp90_s1585_009}"

    # きゃっ、キャイン！
    voice "sp90_s1585_010"
    s "Kyah! Kyaain!{#sp90_s1585_010}"

    # → next scene 1588
    jump sp90_scene_1588

label sp90_scene_1586:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # ……あ、ありがとうございます。
    voice "sp90_s1586_002"
    s "……Ah, thank you.{#sp90_s1586_002}"

    # 返事は『わん』よっ！
    voice "sp90_s1586_003"
    l "The answer is 'woof'!{#sp90_s1586_003}"

    # ……わ、わんっ！わんわん！
    voice "sp90_s1586_004"
    s "……W-Woof! Woof woof!{#sp90_s1586_004}"

    # → next scene 1588
    jump sp90_scene_1588

label sp90_scene_1587:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # そ、そんな労力は使わないでください。
    voice "sp90_s1587_002"
    s "P-Please don't go to so much trouble.{#sp90_s1587_002}"

    # な、なによっ！わたしのプレゼントが気にいらないっていうの？
    voice "sp90_s1587_003"
    l "W-What?! You mean you don't like my present?!{#sp90_s1587_003}"

    # いや、だって。首輪なんて……。
    voice "sp90_s1587_004"
    s "No, it's just… a collar is…{#sp90_s1587_004}"

    # ばっ、バカ犬のくせに生意気に人間の言葉を話してるんじゃないわよっ！
    voice "sp90_s1587_005"
    l "D-Don't you get cheeky with me, you stupid dog, talking like a human!{#sp90_s1587_005}"

    # バカ犬なんて『わん』だけ言ってれば十分なんだからねっ！
    voice "sp90_s1587_006"
    l "A stupid dog only needs to say 'woof', and that's more than enough!{#sp90_s1587_006}"

    # ううっ、分かりました……わんっ！
    voice "sp90_s1587_007"
    s "Ugh… I understand… Woof!{#sp90_s1587_007}"

    # → next scene 1588
    jump sp90_scene_1588

label sp90_scene_1588:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # ふんっ！それでいいのよっ！
    voice "sp90_s1588_002"
    l "Hmph! That's more like it!{#sp90_s1588_002}"

    # ほらっ、バカ犬！今度は３回まわってワン！と言ってみなさい。
    voice "sp90_s1588_003"
    l "Now, stupid dog! This time, spin around three times and say 'woof'!{#sp90_s1588_003}"

    # な、なにぃっ！！！
    voice "sp90_s1588_004"
    s "W-What?!!{#sp90_s1588_004}"

    # 『わん』でしょ？『わん』！
    voice "sp90_s1588_005"
    l "It's 'woof', right? 'Woof'!{#sp90_s1588_005}"

    # あら、できないっていうの？やっぱりバカ犬はバカ犬ね……。
    voice "sp90_s1588_006"
    l "Oh? You say you can't do it? A stupid dog is a stupid dog after all…{#sp90_s1588_006}"


    menu:
        "F-Fine. I'll do it!{#sp90_c_1588_1589}":
            jump sp90_scene_1589
        "I've got my pride too, you know…{#sp90_c_1588_1590}":
            jump sp90_scene_1590
        "'Spin three times and woof!'{#sp90_c_1588_1591}":
            jump sp90_scene_1591

label sp90_scene_1589:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # （し、仕方ない。やってやる！やってやるよぉっ！）
    s "(F-Fine. I'll do it! I'll do it, I tell you!){#sp90_s1589_002}"

    # ほらほら、早くしなさいっ！
    voice "sp90_s1589_003"
    l "Come on, come on, hurry up!{#sp90_s1589_003}"

    # ……い、１回……２回……３回っ！
    voice "sp90_s1589_004"
    s "……O-One… two… three!{#sp90_s1589_004}"

    # わ、わん！
    voice "sp90_s1589_005"
    s "W-Woof!{#sp90_s1589_005}"

    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay1     vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # き、きゃあっ！
    voice "sp90_s1589_015"
    l "K-Kyah!{#sp90_s1589_015}"

    # な、何で飛びついてきてるのよ！
    voice "sp90_s1589_016"
    l "W-Why are you jumping on me?!{#sp90_s1589_016}"

    # ワンワンワン！
    voice "sp90_s1589_017"
    s "Woof woof woof!{#sp90_s1589_017}"

    # [EVENT_CG event    image=+166, level=80]
    $ dissolve_fx("id(166)")
    # ち、ちょっと！どこ触ってるのっ！ち、ちちち、調子にのるんじゃなぁ～いっ！
    voice "sp90_s1589_019"
    l "H-Hey! Where are you touching?! D-Don't, don't, don't get carried away now!{#sp90_s1589_019}"

    # [SE       se0      play=+62]
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
    # きゃっ、キャイ～ン！
    voice "sp90_s1589_030"
    s "Kyah! Kya~in!{#sp90_s1589_030}"

    # → next scene 1592
    jump sp90_scene_1592

label sp90_scene_1590:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # お、俺にもプライドってものが……。
    voice "sp90_s1590_002"
    s "I-I've got my pride too, you know…{#sp90_s1590_002}"

    # ふーん。バカ犬のクセに生意気ね。
    voice "sp90_s1590_003"
    l "Huuuh. Cheeky for a stupid dog, aren't you?{#sp90_s1590_003}"

    # 美しい令嬢にひざまずくこと以上の名誉はこの世には存在しないとか思わないの？
    voice "sp90_s1590_004"
    l "Don't you think there's no greater honor in this world than kneeling before a beautiful young lady?{#sp90_s1590_004}"

    # そ、そんな名誉はいらねーっ！第一、ホントの令嬢は『３回まわってワン！』なんて要求しないっ！
    voice "sp90_s1590_005"
    s "I don't need that kinda honor! Besides, a real young lady wouldn't ask you to 'spin three times and woof'!{#sp90_s1590_005}"

    # [EVENT_CG event    image=+167, level=80]
    $ dissolve_fx("id(167)")
    # うっ、うるさぁーい！
    voice "sp90_s1590_007"
    l "Guh, shut uuup!{#sp90_s1590_007}"

    # [SE       se0      play=+71]
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
    # パシィィィンっっ！
    th "Smack!!!{#sp90_s1590_018}"

    # き、きゃいーん！
    voice "sp90_s1590_019"
    s "K-Kyaiin!{#sp90_s1590_019}"

    # → next scene 1592
    jump sp90_scene_1592

label sp90_scene_1591:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # ……３回まわってワン！
    voice "sp90_s1591_002"
    s "……Spin three times and woof!{#sp90_s1591_002}"

    # ？？？……なによ、それ？
    voice "sp90_s1591_003"
    l "???……What's that supposed to be?{#sp90_s1591_003}"

    # ちゃんと『３回まわってワン！』って言いなさいっ！
    voice "sp90_s1591_004"
    l "Say it properly! 'Spin three times and woof!'{#sp90_s1591_004}"

    # ３回まわってワン！
    voice "sp90_s1591_005"
    s "Spin three times and woof!{#sp90_s1591_005}"

    # ……ほら、ちゃんとご主人様の命令どおりに言ってるだろ？
    voice "sp90_s1591_006"
    s "……See? I said it exactly as you ordered, Master, didn't I?{#sp90_s1591_006}"

    # [EVENT_CG event    image=+167, level=80]
    $ dissolve_fx("id(167)")
    # ……っ！
    voice "sp90_s1591_008"
    l "……!{#sp90_s1591_008}"

    # つまり、バカにしてるワケね？
    voice "sp90_s1591_009"
    l "So you're making fun of me, is that it?{#sp90_s1591_009}"

    # [SE       se0      play=+71]
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
    # パシィィィンっっ！
    th "Smack!!!{#sp90_s1591_020}"

    # き、きゃいーん！
    voice "sp90_s1591_021"
    s "K-Kyaiin!{#sp90_s1591_021}"

    # バカ犬には反省ってものを教えてあげるわっ！
    voice "sp90_s1591_022"
    l "I'll teach this stupid dog what remorse is!{#sp90_s1591_022}"

    # → next scene 1592
    jump sp90_scene_1592

label sp90_scene_1592:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+166, level=80]
    $ dissolve_fx("id(166)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1593:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # お、俺は犬じゃないっ！
    voice "sp90_s1593_002"
    s "Oh, I'm not a dog!{#sp90_s1593_002}"

    # [EVENT_CG event    image=+166, level=80]
    $ dissolve_fx("id(166)")
    # ……だ、だから困ってるのよっ！
    voice "sp90_s1593_004"
    l "……T-That's why I'm at my wit's end!{#sp90_s1593_004}"

    # まったく、ご主人様をほったらかして、よその子のところに行ってばかり。
    voice "sp90_s1593_005"
    l "Honestly, leaving your master all alone and always running off to other girls.{#sp90_s1593_005}"

    # （ぎ、ぎくっ！）[EVENT_CG event    image=+165, level=80]
    s "(G-Gasp!){#sp90_s1593_006}"

    # ほ、ホントにだらしないんだからっ！
    voice "sp90_s1593_007"
    l "Y-You're so sloppy!{#sp90_s1593_007}"

    # ……わ、わん！どうぞ犬と呼んでくださいワン！
    voice "sp90_s1593_008"
    s "……W-Woof! Please call me a dog, woof!{#sp90_s1593_008}"

    # → next scene 1596
    jump sp90_scene_1596

label sp90_scene_1594:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # も、文句はないです……ワン！
    voice "sp90_s1594_002"
    s "N-No complaints…… Woof!{#sp90_s1594_002}"

    # ……ふん。いつもそれぐらい素直でいることね。
    voice "sp90_s1594_003"
    l "……Hmph. Always stay that obedient, all right?{#sp90_s1594_003}"

    # → next scene 1596
    jump sp90_scene_1596

label sp90_scene_1595:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # ち、ちくしょう！い、いつかはルイズに……逆に……。
    voice "sp90_s1595_002"
    s "D-Damn it! S-Someday I'll turn the tables on Louise……{#sp90_s1595_002}"

    # （逆に……）
    s "(The other way around……){#sp90_s1595_003}"

    # ふふっ……ふふふふふ……。
    voice "sp90_s1595_004"
    s "Fufu…… Fufufufufu……{#sp90_s1595_004}"

    # [EVENT_CG event    image=+166, level=80]
    $ dissolve_fx("id(166)")
    # ななな、何を笑いだすのよっ！気持ち悪いっ！
    voice "sp90_s1595_006"
    l "W-What are you laughing at! It's gross!{#sp90_s1595_006}"

    # な、なんでもありませんですっ！
    voice "sp90_s1595_007"
    s "I-It's nothing at all!{#sp90_s1595_007}"

    # [EVENT_CG event    image=+167, level=80]
    $ dissolve_fx("id(167)")
    # う、嘘おっしゃいっ！何を考えてたのよっ！
    voice "sp90_s1595_009"
    l "D-Don't lie to me! What were you thinking about!{#sp90_s1595_009}"

    # [SE       se0      play=+61]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [SPRITE   lay4     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay3     hide, reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # きゃいんきゃいん！
    voice "sp90_s1595_024"
    s "Kya-in, kya-in!{#sp90_s1595_024}"

    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # → next scene 1596
    jump sp90_scene_1596

label sp90_scene_1596:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # そう、ね……。
    voice "sp90_s1596_002"
    l "Yes……{#sp90_s1596_002}"

    # サイトが誰の使い魔か、もう一度はっきりさせる必要があるかしらね。
    voice "sp90_s1596_003"
    l "I wonder if I should make it clear once again whose familiar Saito is.{#sp90_s1596_003}"

    # ……へっ？
    voice "sp90_s1596_004"
    s "……Huh?{#sp90_s1596_004}"

    # 犬といったらもちろん散歩、よね？
    voice "sp90_s1596_005"
    l "Dogs mean walks, of course, right?{#sp90_s1596_005}"

    # さ、散歩ですか……ってまさかこのまま！？
    voice "sp90_s1596_006"
    s "S-So, a walk?…… No way, not like this!?{#sp90_s1596_006}"

    # うふふ、そうよっ！
    voice "sp90_s1596_007"
    l "Ufufu, that's right!{#sp90_s1596_007}"

    # さあ、ご主人様とのお散歩なんだからねっ！
    voice "sp90_s1596_008"
    l "Come on, it's a walk with your master, you know!{#sp90_s1596_008}"


    menu:
        "……I-I'm happy, woof!{#sp90_c_1596_1597}":
            jump sp90_scene_1597
        "M-My stomach suddenly started hurting……{#sp90_c_1596_1598}":
            jump sp90_scene_1598
        "I-If my friends hear about this……{#sp90_c_1596_1599}":
            jump sp90_scene_1599

label sp90_scene_1597:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # ……う、うれしいですワン！
    voice "sp90_s1597_002"
    s "……I-I'm happy, woof!{#sp90_s1597_002}"

    # （ち、ちくしょう～～っ！）
    s "(D-Damn it~~~!){#sp90_s1597_003}"

    # うふふっ。
    voice "sp90_s1597_004"
    l "Ufufu.{#sp90_s1597_004}"

    # いつもそれぐらいでいなさい。バカ犬！
    voice "sp90_s1597_005"
    l "Always stay like this. Stupid dog!{#sp90_s1597_005}"

    # → next scene 1600
    jump sp90_scene_1600

label sp90_scene_1598:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # あ、あれ？
    voice "sp90_s1598_002"
    s "H-Huh?{#sp90_s1598_002}"

    # きゅ、急におなかが痛く……なったワン。
    voice "sp90_s1598_003"
    s "S-Suddenly my stomach started hurting…… woof.{#sp90_s1598_003}"

    # ……仮病ね。
    voice "sp90_s1598_004"
    l "……Faking it, I see.{#sp90_s1598_004}"

    # そ、そんなことねえっ！
    voice "sp90_s1598_005"
    s "N-No, that's not it!{#sp90_s1598_005}"

    # [EVENT_CG event    image=+167, level=80]
    $ dissolve_fx("id(167)")
    # だったらトイレに連れて行ってあげるわよ？……もちろん、犬用のだけど。
    voice "sp90_s1598_007"
    l "Then I'll take you to the toilet, shall I?…… The dog one, of course.{#sp90_s1598_007}"

    # （……げっ。目が本気だ）
    s "(……Gah. She means it.){#sp90_s1598_008}"

    # あ、あれ？急に治った気が……ワン。
    voice "sp90_s1598_009"
    s "H-Huh? It suddenly feels better…… woof.{#sp90_s1598_009}"

    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # そう？……それでいいのよ。
    voice "sp90_s1598_011"
    l "Oh?…… That's fine, then.{#sp90_s1598_011}"

    # → next scene 1600
    jump sp90_scene_1600

label sp90_scene_1599:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # と、友達に噂されると恥ずかしいし……。
    voice "sp90_s1599_002"
    s "B-Besides, it'd be embarrassing if my friends heard about it……{#sp90_s1599_002}"

    # いまさら恥ずかしがっても無駄でしょ？い、行くわよっ！バカ犬っ！
    voice "sp90_s1599_003"
    l "It's no use being embarrassed now, is it? I-I'm going! Stupid dog!{#sp90_s1599_003}"

    # → next scene 1600
    jump sp90_scene_1600

label sp90_scene_1600:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+165, level=80]
    $ dissolve_fx("id(165)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [SE       se0      play=+57]
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # ……さあ、お散歩はどこがいいかしら？
    voice "sp90_s1600_012"
    l "……Now, where would be a good place to walk?{#sp90_s1600_012}"

    # わ、わんわん！
    voice "sp90_s1600_013"
    s "W-Woof, woof!{#sp90_s1600_013}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # あら？
    voice "sp90_s1600_015"
    l "Oh?{#sp90_s1600_015}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # こんにちは、モンモランシー。……ついでにギーシュも。
    voice "sp90_s1600_018"
    l "Hello, Montmorency.…… And Guiche too.{#sp90_s1600_018}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # [SPRITE   lay4     image=+555, level=160, dir=1A]
    # ……。
    th "……{#sp90_s1600_022}"

    # ……。
    voice "sp90_s1600_023"
    th "……{#sp90_s1600_023}"

    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # ……そ、そういうプレイ？
    voice "sp90_s1600_025"
    th "……S-So that's the kind of 'play' you're into?{#sp90_s1600_025}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay4     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # なっ！バカ犬に教育しながら散歩させてるだけなんだからっ！
    voice "sp90_s1600_029"
    l "N-No! I'm just walking the stupid dog while teaching him a lesson!{#sp90_s1600_029}"

    # [SPRITE   lay1     x=224, y=0]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # そ、そう。倒錯してるのね。
    voice "sp90_s1600_032"
    th "I-I see. You're quite perverted, aren't you?{#sp90_s1600_032}"

    # ど、どういう意味よっ！
    voice "sp90_s1600_033"
    l "W-What do you mean!{#sp90_s1600_033}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay4     image=+563, level=160, dir=1A]
    # くっ！な、なんだかしらんが……、ドキドキする光景だな！
    voice "sp90_s1600_036"
    th "Tch! I don't know what it is, but…… what a heart-pounding sight!{#sp90_s1600_036}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # ま、まて！妙な誤解をするんじゃない！ギーシュ！
    voice "sp90_s1600_039"
    s "W-Wait! Don't get the wrong idea! Guiche!{#sp90_s1600_039}"

    # [SPRITE   lay4     image=+559, level=160, dir=1A]
    # 貴様、ルイズに……。いや、羨ましくなんかないぞ！ぜんぜん羨ましくないんだからなっ！
    voice "sp90_s1600_041"
    th "You and Louise…… No, I'm not jealous! I'm not jealous at all, you hear!{#sp90_s1600_041}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay3     image=+889, level=160, dir=2A]
    # ギーシュ？あなたそれどういう意味？
    voice "sp90_s1600_044"
    th "Guiche? What do you mean by that?{#sp90_s1600_044}"

    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # いやっ、そ、それは……。ち、違うんだモンモランシー……。
    voice "sp90_s1600_046"
    th "N-No, that was…… Th-That's not it, Montmorency……{#sp90_s1600_046}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay4     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # な、なに勝手に話を進めてるのよ！
    voice "sp90_s1600_050"
    l "W-What are you talking about on your own!{#sp90_s1600_050}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # そ、そうだぞ！お、俺達は……。
    voice "sp90_s1600_053"
    s "T-That's right! W-We're……{#sp90_s1600_053}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # ……え、ええ。そうね。お邪魔しちゃったみたいで。
    voice "sp90_s1600_057"
    th "……Y-Yes. That's right. Looks like we interrupted.{#sp90_s1600_057}"

    # [SPRITE   lay3     x=-96, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # な、なによっ！そ、その生暖かい目をやめなさいっ！
    voice "sp90_s1600_060"
    l "W-What! S-Stop looking at me with those lukewarm eyes!{#sp90_s1600_060}"

    # ほ、本当にバカ犬にお散歩させてただけなんだからねっ！
    voice "sp90_s1600_061"
    l "I-I really was just taking the stupid dog for a walk, you know!{#sp90_s1600_061}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay3     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1601:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # ま、まあ少しは進歩したんでは……。
    voice "sp90_s1601_002"
    s "W-Well, you have improved a little, haven't you……{#sp90_s1601_002}"

    # 確かに進歩はしたわ。でも、それは昔のわたしからの進歩であって、人並みとは言えないわ。
    voice "sp90_s1601_003"
    l "It's true I improved. But that's progress from my past self——I wouldn't call it normal.{#sp90_s1601_003}"

    # い、いや、まぁ、そうなんだけどさ……。
    voice "sp90_s1601_004"
    s "N-No, well, that's true, but……{#sp90_s1601_004}"

    # → next scene 1604
    jump sp90_scene_1604

label sp90_scene_1602:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # いや、立派だと思うぜっ！
    voice "sp90_s1602_002"
    s "No, I think you're magnificent!{#sp90_s1602_002}"

    # えっ？
    voice "sp90_s1602_003"
    l "Huh?{#sp90_s1602_003}"

    # たとえ落ちこぼれでも、諦めずに前に進もうって気持ちは大切だって！努力しなかったら、そこで終わりだしな。
    voice "sp90_s1602_004"
    s "Even if you're a failure, that feeling of moving forward without giving up is important! If you don't try, it ends right there.{#sp90_s1602_004}"

    # ねえ、バカ犬……。その落ちこぼれっていったい誰のこと？
    voice "sp90_s1602_005"
    l "Hey, stupid dog…… Who exactly is that 'failure'?{#sp90_s1602_005}"

    # へっ？そりゃ、もちろんルイズ……。
    voice "sp90_s1602_006"
    s "Huh? Why, Louise, of course……{#sp90_s1602_006}"

    # ごごご、ご主人様を落ちこぼれ呼ばわりとはたいした度胸ねっ！
    voice "sp90_s1602_007"
    l "H-H-How dare you call your master a failure! That's some nerve!{#sp90_s1602_007}"

    # し、しまったー。
    voice "sp90_s1602_008"
    s "S-Shit……{#sp90_s1602_008}"

    # → next scene 1604
    jump sp90_scene_1604

label sp90_scene_1603:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # まあ、本当に無駄な努力だよな……。
    voice "sp90_s1603_002"
    s "Well, it really is a waste of effort, isn't it……{#sp90_s1603_002}"

    # 普通、そこまで言うっ？
    voice "sp90_s1603_003"
    l "Is that something you'd normally say?!{#sp90_s1603_003}"

    # （げっ、聞こえてたっ！？）
    s "(Gah, she heard me!?){#sp90_s1603_004}"

    # ご主人様にそんな口をきくなんて……。覚悟はいいわねっ！
    voice "sp90_s1603_005"
    l "Talking to your master like that…… Are you ready for this?!{#sp90_s1603_005}"

    # [SE       se0      play=+62]
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
    # ひ、ひいっっ！
    voice "sp90_s1603_016"
    s "E-Eek!{#sp90_s1603_016}"

    # → next scene 1604
    jump sp90_scene_1604

label sp90_scene_1604:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # [TRANS trans("crossfade", 1000)]
    # な、なんだよ。これっ！なんで俺が縛られないとっ！
    voice "sp90_s1604_007"
    s "W-What's this! Why do I have to be tied up!{#sp90_s1604_007}"

    # おだまりっ！バカ犬はそこでじっとしてればいいのよっ！
    voice "sp90_s1604_008"
    l "Silence! The stupid dog just needs to stay put right there!{#sp90_s1604_008}"

    # ……って！なんだよっ、そのリンゴっ！
    voice "sp90_s1604_009"
    s "……Hey! What's with that apple!{#sp90_s1604_009}"

    # な、なんで俺の頭の上に置こうとすんだよっ！
    voice "sp90_s1604_010"
    s "W-Why are you putting it on my head!{#sp90_s1604_010}"

    # 旅芸人達がやってるのを見て思いついたのよ。ほら、よくあるじゃない？頭の上のリンゴにナイフを投げるヤツ。
    voice "sp90_s1604_011"
    l "I got the idea from the traveling performers. You know the one——throwing knives at an apple on someone's head?{#sp90_s1604_011}"

    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # や、やっぱりぃーーーーっっ！！
    voice "sp90_s1604_013"
    s "N-Noo waaay——!!{#sp90_s1604_013}"

    # ややや、やめろーーっ！おまえはウイリアム・テルじゃないぞーーっ！
    voice "sp90_s1604_014"
    s "H-Hey, stopp——! You're not William Teeeell——!{#sp90_s1604_014}"

    # 誰よ、それ？
    voice "sp90_s1604_015"
    l "Who's that?{#sp90_s1604_015}"

    # ……ええと、確か俺の世界の昔話で、自分の息子の頭だか頭の上のリンゴだかを射ち落とした弓の名人だよっ！
    voice "sp90_s1604_016"
    s "……Um, I think it's from an old tale in my world——a master archer who shot down his own son's head, or the apple on top of it!{#sp90_s1604_016}"

    # バカ犬の地元の有名人なんて知ってるわけないじゃない。
    voice "sp90_s1604_017"
    l "How would I know a celebrity from the stupid dog's hometown?{#sp90_s1604_017}"

    # ……まあ、バカ犬が励ましてくれたのだけは分かったわ。
    voice "sp90_s1604_018"
    l "……Well, at least I get that the stupid dog was trying to cheer me on.{#sp90_s1604_018}"

    # ご主人様の特訓にその身を捧げようという意志も。
    voice "sp90_s1604_019"
    l "And the will to devote himself to his master's special training.{#sp90_s1604_019}"

    # そんな意志はねーーっ！いや励ましはしたけど、どんな解釈だよっ！
    voice "sp90_s1604_020"
    s "No such will——! I did cheer you on, but what kind of interpretation is that?!{#sp90_s1604_020}"

    # さあ、特訓開始よっ！
    voice "sp90_s1604_021"
    l "Now, special training begins!{#sp90_s1604_021}"

    # や、やめろーーっ！ルイズーーーっ！
    voice "sp90_s1604_022"
    s "S-Stop——! Louiiise!{#sp90_s1604_022}"

    # ……っ！
    voice "sp90_s1604_023"
    l "……!{#sp90_s1604_023}"

    # ひっ、ヒィィィィィッ！！！
    voice "sp90_s1604_024"
    s "E-Eeeeeeeek!!!{#sp90_s1604_024}"


    menu:
        "Run until the very last moment!{#sp90_c_1604_1605}":
            jump sp90_scene_1605
        "Steel myself!{#sp90_c_1604_1606}":
            jump sp90_scene_1606
        "Try trusting Louise?{#sp90_c_1604_1607}":
            jump sp90_scene_1607

label sp90_scene_1605:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # ……あ、諦めたらおしまいなんだぁっ！
    voice "sp90_s1605_002"
    s "……Ah, if you give up, it's all over!{#sp90_s1605_002}"

    # 少しは信用したらどうなのっ！
    voice "sp90_s1605_003"
    l "Why don't you trust me a little?!{#sp90_s1605_003}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # ドゴォォーーーン！
    th "Dogo-o-o-oon!{#sp90_s1605_014}"

    # ど、どわーーーっ！
    voice "sp90_s1605_015"
    s "G-Gwaaaaah!!{#sp90_s1605_015}"

    # → next scene 1608
    jump sp90_scene_1608

label sp90_scene_1606:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # も、もうダメだーーーっ！
    voice "sp90_s1606_002"
    s "I-I'm done for——!{#sp90_s1606_002}"

    # な、なによ！バカにして！
    voice "sp90_s1606_003"
    l "W-What! You're making fun of me!{#sp90_s1606_003}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # ドゴォォーーーン！
    th "Dogo-o-o-oon!{#sp90_s1606_014}"

    # ど、どわーーーっ！
    voice "sp90_s1606_015"
    s "G-Gwaaaaah!!{#sp90_s1606_015}"

    # → next scene 1608
    jump sp90_scene_1608

label sp90_scene_1607:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # ルイズっ！し、信じたからなーーーっ！
    voice "sp90_s1607_002"
    s "Louise! I trusted you, you know——!{#sp90_s1607_002}"

    # と、当然よぉっ！！
    voice "sp90_s1607_003"
    l "O-Of course!!{#sp90_s1607_003}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # ドゴォォーーーン！
    th "Dogo-o-o-oon!{#sp90_s1607_014}"

    # ど、どわーーーっ！
    voice "sp90_s1607_015"
    s "G-Gwaaaaah!!{#sp90_s1607_015}"

    # → next scene 1608
    jump sp90_scene_1608

label sp90_scene_1608:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # ……。
    voice "sp90_s1608_005"
    s "……{#sp90_s1608_005}"

    # ……いっ、生きてるっ？
    voice "sp90_s1608_006"
    s "……H-Huh… am I alive?{#sp90_s1608_006}"

    # 生きてるっ！生きてるぞっ！ひ、ひゃっほぉーーーーっ！！
    voice "sp90_s1608_007"
    s "I'm alive! I'm alive! H-Hyahhooooo!!{#sp90_s1608_007}"

    # ……えっ！？う、うそっ！ホントに成功したの？
    voice "sp90_s1608_008"
    l "……Eh!? N-No way! It really succeeded?{#sp90_s1608_008}"

    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # お、おいっ！そりゃどういう意味だよっ！
    voice "sp90_s1608_010"
    s "H-Hey! What's that supposed to mean!{#sp90_s1608_010}"

    # せ、成功したからいいじゃないっ！
    voice "sp90_s1608_011"
    l "I-It succeeded, so it's fine, isn't it!{#sp90_s1608_011}"

    # ほらっ、リンゴだけきれいに砕けてるわ！
    voice "sp90_s1608_012"
    l "See? The apple's the only thing that got smashed to bits!{#sp90_s1608_012}"

    # （し、失敗してたら、俺の頭がああなってたのかよ？）
    s "(I-If it had failed, my head would've ended up like that? S-So I was made a practice dummy for magic she isn't even that confident about… Me…){#sp90_s1608_013}"

    # これで、サイトもわたしの魔法がちゃんと成功することもあるってことが、よく分かったでしょ！
    voice "sp90_s1608_014"
    l "Now you get it too, Saito — my magic does succeed properly sometimes, doesn't it!{#sp90_s1608_014}"

    # （そ、そこまで自信のない魔法の練習台にされたのか……俺は……）[SE       se1      stop=
    s "(I-If it had failed, my head would've ended up like that? S-So I was made a practice dummy for magic she isn't even that confident about… Me…){#sp90_s1608_015}"

label sp90_scene_1609:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # て、手伝わせていただきますですっ！
    voice "sp90_s1609_002"
    s "L-Let me help you, I insist!{#sp90_s1609_002}"

    # あら、ずいぶん素直ね。
    voice "sp90_s1609_003"
    l "My, you're awfully obedient today.{#sp90_s1609_003}"

    # そりゃぁ…、もう、ご主人様ですから。
    voice "sp90_s1609_004"
    s "Well… because you're my mistress now.{#sp90_s1609_004}"

    # → next scene 1612
    jump sp90_scene_1612

label sp90_scene_1610:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # で、デートで忙しいので……。
    voice "sp90_s1610_002"
    s "A-And I'm busy with a date, so…{#sp90_s1610_002}"

    # デート？……いい度胸ね？いっぺん死んでみる？
    voice "sp90_s1610_003"
    l "A date? …You've got some nerve. Want to try dying once?{#sp90_s1610_003}"

    # お、お手伝いをさせていただくであります！ご主人様！
    voice "sp90_s1610_004"
    s "L-Let me help you, I must! Mistress!{#sp90_s1610_004}"

    # それでいいのよっ。
    voice "sp90_s1610_005"
    l "That'll do nicely!{#sp90_s1610_005}"

    # → next scene 1612
    jump sp90_scene_1612

label sp90_scene_1611:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # 訓練なんて無駄な努力を……。
    voice "sp90_s1611_002"
    s "Training's just a waste of effort…{#sp90_s1611_002}"

    # ど、どういう意味よ！どんな才能だって磨かなければ輝きはしないんだからねっ！
    voice "sp90_s1611_003"
    l "W-What do you mean! Any talent won't shine unless you polish it!{#sp90_s1611_003}"

    # そ、それなら一人で山にでもこもったら……。
    voice "sp90_s1611_004"
    s "T-Then why don't you just lock yourself up in the mountains alone…?{#sp90_s1611_004}"

    # わたしだけの修行じゃないの。使い魔の修行もかねてるんだから、黙って言うことを聞きなさい。
    voice "sp90_s1611_005"
    l "It's not just my training. It doubles as familiar training, so shut up and do as you're told.{#sp90_s1611_005}"

    # えー。
    voice "sp90_s1611_006"
    s "Ehh.{#sp90_s1611_006}"

    # → next scene 1612
    jump sp90_scene_1612

label sp90_scene_1612:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # [TRANS trans("crossfade", 1000)]
    # 今日はリンゴを２個。……ほら、手を出しなさい。
    voice "sp90_s1612_007"
    l "Two apples today. …Come on, hold out your hand.{#sp90_s1612_007}"

    # ち、ちょっとこれは訓練としては危険じゃねーのか？
    voice "sp90_s1612_008"
    s "H-Hey, isn't this a little dangerous for training?{#sp90_s1612_008}"

    # ……逃げてもいいけど、狙いが外れたらどうなるか責任もてないわよっ！
    voice "sp90_s1612_009"
    l "…You can run if you like, but if my aim slips I can't be responsible for what happens!{#sp90_s1612_009}"

    # それとも、逃げる的の方が訓練にはよいのかしら？
    voice "sp90_s1612_010"
    l "Or maybe a running target makes for better training, I wonder?{#sp90_s1612_010}"

    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # ちっ、ちくしょうっ！
    voice "sp90_s1612_012"
    s "Tch, damn it!{#sp90_s1612_012}"


    menu:
        "Try running away…?{#sp90_c_1612_1613}":
            jump sp90_scene_1613
        "A-At least say one thing…{#sp90_c_1612_1614}":
            jump sp90_scene_1614
        "Damn it! Go ahead and shoot!{#sp90_c_1612_1615}":
            jump sp90_scene_1615

label sp90_scene_1613:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # （に、逃げ出さないと……って……）[EVENT_CG event    image=+168, level=8
    s "(I-I have to run… but… No good. The rope won't come undone!){#sp90_s1613_002}"

    # （……ダメだ。縄がほどけない！）
    s "(I-I have to run… but… No good. The rope won't come undone!){#sp90_s1613_003}"

    # あら？逃げださないの？
    voice "sp90_s1613_004"
    l "Oh? Not running?{#sp90_s1613_004}"

    # いや、ちょっと！この縄っ！
    voice "sp90_s1613_005"
    s "No, wait! This rope!{#sp90_s1613_005}"

    # うふふ。サイトの犠牲は忘れないわ。
    voice "sp90_s1613_006"
    l "Ufufu. I won't forget Saito's sacrifice.{#sp90_s1613_006}"

    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # ま、まてぇぇぇっ！
    voice "sp90_s1613_008"
    s "W-Waittttt!{#sp90_s1613_008}"

    # → next scene 1616
    jump sp90_scene_1616

label sp90_scene_1614:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # せ、せめて最後になにか一言を……。
    voice "sp90_s1614_003"
    s "A-At least let me say one last thing…{#sp90_s1614_003}"

    # 一言？謝っても、もう許してあげないわよ。
    voice "sp90_s1614_004"
    l "One thing? Even if you apologize, I won't forgive you.{#sp90_s1614_004}"

    # ル、ルイズ横暴～～っ！
    voice "sp90_s1614_005"
    s "L-Louise, you're so tyrannical~!{#sp90_s1614_005}"

    # ……それが、最後の一言？まったく、懺悔のひとつもするかと思えば……。
    voice "sp90_s1614_006"
    l "…That's your last word? Honestly, I thought you'd show at least a little remorse…{#sp90_s1614_006}"

    # い、いや。ちょっと待って！
    voice "sp90_s1614_007"
    s "N-No. Wait a moment!{#sp90_s1614_007}"

    # 大丈夫。お墓はちゃんと作ってあげるわ。
    voice "sp90_s1614_008"
    l "Don't worry. I'll make you a nice grave.{#sp90_s1614_008}"

    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # やっ、やめろぉぉぉっ！
    voice "sp90_s1614_010"
    s "S-Stop ittt!{#sp90_s1614_010}"

    # → next scene 1616
    jump sp90_scene_1616

label sp90_scene_1615:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # ち、ちくしょうっ！さあ撃ちやがれっ！
    voice "sp90_s1615_002"
    s "D-Damn it! Go ahead and shoot!{#sp90_s1615_002}"

    # わ、分かったわよ！い、いくわよっ！本当にいくんだからねっ！
    voice "sp90_s1615_003"
    l "F-Fine! I-I'll do it! I really will, you know!{#sp90_s1615_003}"

    # や、やっぱりやめろ～～っ！
    voice "sp90_s1615_004"
    s "N-No, stop, I changed my mind~!{#sp90_s1615_004}"

    # → next scene 1616
    jump sp90_scene_1616

label sp90_scene_1616:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # [SE       se0      play=+95]
    # [SE       se0      play=+95]
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
    # ドドォォーン！[LAYER    white    image=+2, level=0][TRANS tran
    th "Dodoooon!{#sp90_s1616_013}"

    # ぐ、ぐわぁぁぁーーっっ！
    voice "sp90_s1616_014"
    s "G-Gwaaaaah!!{#sp90_s1616_014}"

    # 失敗じゃない！ちゃんと２つとも割れてる！すごい、わたしすごいわー！
    voice "sp90_s1616_015"
    l "It's not a failure! Both of them cracked perfectly! Amazing, I'm amazing!{#sp90_s1616_015}"

    # ……い、言うことはそれだけか？
    voice "sp90_s1616_016"
    s "…I-Is that all you have to say?{#sp90_s1616_016}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1617:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # （ホ、ホントに成功……するかも？）
    s "(R-Really… it might actually succeed? N-No. I've got to believe in Louise… T-This is bad! Something about Louise's mood today is definitely off!){#sp90_s1617_002}"

    # （い、いや。ルイズを信じないと……）
    s "(R-Really… it might actually succeed? N-No. I've got to believe in Louise… T-This is bad! Something about Louise's mood today is definitely off!){#sp90_s1617_003}"

    # うふっ……うふふふふ……。
    voice "sp90_s1617_004"
    l "Ufufu… ufufufufu…{#sp90_s1617_004}"

    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # って、なんですか！そのアブナイ笑い方っ！
    voice "sp90_s1617_006"
    s "W-What is it!? That creepy laugh!{#sp90_s1617_006}"

    # （……ヤ、ヤバイっ！なんか、今日のルイズのノリはぜったいまずい気がするぞぉぉっ！）→ next scene 1
    s "(R-Really… it might actually succeed? N-No. I've got to believe in Louise… T-This is bad! Something about Louise's mood today is definitely off!){#sp90_s1617_007}"

label sp90_scene_1618:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # （……し、失敗したらどうなるの？）
    s "(I-If it fails, what'll happen? A pleasant splatter? Or before that I might be wiped out without a trace… H-Huh? Could it be I'm… going to die?){#sp90_s1618_002}"

    # （……愉快にスプラッタ？それ以前に跡形もなくなったりして……）
    s "(I-If it fails, what'll happen? A pleasant splatter? Or before that I might be wiped out without a trace… H-Huh? Could it be I'm… going to die?){#sp90_s1618_003}"

    # うふっ……うふふふふ……。
    voice "sp90_s1618_004"
    l "Ufuh… Ufufufufu…{#sp90_s1618_004}"

    # （……あ、あれ？も、もしかしてボク……死んじゃう？）[SPRITE   lay1     hide][SPRI
    s "(I-If it fails, what'll happen? A pleasant splatter? Or before that I might be wiped out without a trace… H-Huh? Could it be I'm… going to die?){#sp90_s1618_005}"

    # 今日は皆さんに悲しいお知らせがあります。
    voice "sp90_s1618_006"
    c "Today I have some sad news for all of you.{#sp90_s1618_006}"

    # サイトくんがミス・ヴェリエールとの特訓中に事故で亡くなりました……。
    voice "sp90_s1618_007"
    c "Saito-kun died in an accident during special training with Miss Vallière…{#sp90_s1618_007}"

    # 皆さんもくれぐれも無理な魔法の練習には、注意をしてください……。
    voice "sp90_s1618_008"
    c "Everyone, please be very careful with reckless magic practice…{#sp90_s1618_008}"

    # さて、今日の授業はこの新しい『タロイモヘビくん』について……。
    voice "sp90_s1618_009"
    c "Now, today's lesson is about this new 'Taro Snake-kun'…{#sp90_s1618_009}"

    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # [TRANS trans("crossfade", 1000)]
    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # あ、あんまりだぁぁぁっっ！
    voice "sp90_s1618_013"
    s "T-That's too much!!{#sp90_s1618_013}"

    # きゃっ！
    voice "sp90_s1618_014"
    l "Kya!{#sp90_s1618_014}"

    # そんなおざなりな扱いはないっすよ！コルベール先生っ！
    voice "sp90_s1618_015"
    s "You can't be so dismissive! Mr. Colbert!{#sp90_s1618_015}"

    # な、何を突然叫び出すのよっ！
    voice "sp90_s1618_016"
    l "W-Why are you shouting all of a sudden!?{#sp90_s1618_016}"

    # ホ、ホントにもう勘弁してください。ご主人様……。
    voice "sp90_s1618_017"
    s "P-Please, I've had enough. Mistress…{#sp90_s1618_017}"

    # → next scene 1620
    jump sp90_scene_1620

label sp90_scene_1619:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # い、嫌な予感がする……。
    voice "sp90_s1619_002"
    s "I-I've got a bad feeling…{#sp90_s1619_002}"

    # うふっ……うふふふふ……。
    voice "sp90_s1619_003"
    l "Ufufu… ufufufufu…{#sp90_s1619_003}"

    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # いっ、いやだぁぁぁぁっ！助けてくれぇぇぇっっ！
    voice "sp90_s1619_005"
    s "N-Noooo! Help meeee!{#sp90_s1619_005}"

    # な、なによその態度！
    voice "sp90_s1619_006"
    l "W-What's with that attitude!{#sp90_s1619_006}"

    # い、命だけはご勘弁を！
    voice "sp90_s1619_007"
    s "S-Spare my life, at least!{#sp90_s1619_007}"

    # → next scene 1620
    jump sp90_scene_1620

label sp90_scene_1620:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # ……そ、そもそも。
    voice "sp90_s1620_003"
    s "…F-First of all.{#sp90_s1620_003}"

    # ほ、他の的での成功率とかはどうだったんですか？
    voice "sp90_s1620_004"
    s "H-How was your success rate with the other targets?{#sp90_s1620_004}"

    # ちゃんと命中してるわよ！
    voice "sp90_s1620_005"
    l "I hit the target properly!{#sp90_s1620_005}"

    # ……ただ、ちょっとだけ的の周辺とかも壊しちゃってるけど……。
    voice "sp90_s1620_006"
    l "…It's just that I also wreck a little of the area around the target…{#sp90_s1620_006}"

    # そ、それダメダメじゃん！
    voice "sp90_s1620_007"
    s "T-That's no good at all!{#sp90_s1620_007}"

    # な、なによっ！わたしは本番に強いタイプなのっ！
    voice "sp90_s1620_008"
    l "W-What!? I'm the type who comes through when it counts!{#sp90_s1620_008}"

    # ま、待てぇぇっ！ルイズぅぅっ！
    voice "sp90_s1620_009"
    s "W-Waiiiit! Louiiise!{#sp90_s1620_009}"


    menu:
        "Bawl and beg her to stop{#sp90_c_1620_1621}":
            jump sp90_scene_1621
        "Actually let her use me as the target{#sp90_c_1620_1622}":
            jump sp90_scene_1622
        "Give up and pray to God?{#sp90_c_1620_1623}":
            jump sp90_scene_1623

label sp90_scene_1621:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # ストップ！ストップ！ストーップ！
    voice "sp90_s1621_002"
    s "Stop! Stop! Stoooop!{#sp90_s1621_002}"

    # な、なによっ！わたしの魔法を信用できないの！？
    voice "sp90_s1621_003"
    l "W-What!? You don't trust my magic!?{#sp90_s1621_003}"

    # し、信用してないってわけじゃないけど……。
    voice "sp90_s1621_004"
    s "I-It's not that I don't trust it, but…{#sp90_s1621_004}"

    # こ、今回だけは勘弁してください～～。とてもいやな予感がしますぅぅっ！
    voice "sp90_s1621_005"
    s "J-Just this once, please let me off~~. I've got a really bad feeling about this!{#sp90_s1621_005}"

    # なによっ！いまさら、命乞い？……な、泣かなくてもいいじゃない！
    voice "sp90_s1621_006"
    l "What!? Begging for your life now? …Y-You don't have to cry, you know!{#sp90_s1621_006}"

    # 命乞いでもなんでもいいっスっ！洒落にならないって、それはーーっ！
    voice "sp90_s1621_007"
    s "Begging or whatever, I don't care! This is no joke, I tell you—!{#sp90_s1621_007}"

    # （そもそも、つい最近まで自分がどう呼ばれてたのか忘れたのかよーーっ！）→ next scene 1624
    s "(First of all, did you already forget how you were calling me just a moment ago——!?){#sp90_s1621_008}"

label sp90_scene_1622:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # ……。
    voice "sp90_s1622_002"
    s "…{#sp90_s1622_002}"

    # ……う、うううっ。分かりました。覚悟決めました。
    voice "sp90_s1622_003"
    s "…U-Ugh. All right. I've steeled myself.{#sp90_s1622_003}"

    # そ、それでいいのよっ！
    voice "sp90_s1622_004"
    l "T-That's the way! That's good!{#sp90_s1622_004}"

    # ……。
    voice "sp90_s1622_005"
    s "…{#sp90_s1622_005}"

    # → next scene 1624
    jump sp90_scene_1624

label sp90_scene_1623:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # ……ち、ちくしょう！か、覚悟決めてやるよぉっ！
    voice "sp90_s1623_003"
    s "…D-Damn it! I-I'll steel myself and do it!{#sp90_s1623_003}"

    # それでいいのよっ！
    voice "sp90_s1623_004"
    l "That's fine with me!{#sp90_s1623_004}"

    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # ……って、やっぱ無理だって！し、死ぬのはいやぁぁぁっ！
    voice "sp90_s1623_006"
    s "…Wait—I still can't do this! I-I don't want to dieee!{#sp90_s1623_006}"

    # こ、この世界の神様はよく知らないけど！……か、神さまぁぁっ！
    voice "sp90_s1623_007"
    s "I-I don't know this world's gods that well, but! …G-Goddd!{#sp90_s1623_007}"

    # → next scene 1624
    jump sp90_scene_1624

label sp90_scene_1624:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+168, level=80]
    $ dissolve_fx("id(168)")
    # ……。
    voice "sp90_s1624_002"
    l "…{#sp90_s1624_002}"

    # ……もうっ！ホント、意気地がないんだから！
    voice "sp90_s1624_003"
    l "…Honestly! You're so spineless, really!{#sp90_s1624_003}"

    # 分かったわよっ！中止すればいいんでしょ！
    voice "sp90_s1624_004"
    l "All right, I understand! I just have to call it off, right?!{#sp90_s1624_004}"

    # ……た、助かった。
    voice "sp90_s1624_005"
    s "…T-Thank goodness.{#sp90_s1624_005}"

    # ……って、あらっ？無効化できない？
    voice "sp90_s1624_006"
    l "…Wait—huh? It won't cancel?{#sp90_s1624_006}"

    # [EVENT_CG event    image=+169, level=80]
    $ dissolve_fx("id(169)")
    # ひっ、ひぃぃぃっっっ！
    voice "sp90_s1624_008"
    s "E-Eeeek!!{#sp90_s1624_008}"

    # サ、サイトっ！に、逃げてーーっ！
    voice "sp90_s1624_009"
    l "S-Saito! R-Run for it!!{#sp90_s1624_009}"

    # デ、デルフリンガぁぁぁっっっ！
    voice "sp90_s1624_010"
    s "D-Derflinger!!{#sp90_s1624_010}"

    # な、なにやってやがんだよ！……やべぇっ、間に合わねーーっ！
    voice "sp90_s1624_011"
    th "W-What the hell are you doing?! …Damn, I can't make it!!{#sp90_s1624_011}"

    # ノ、ノォォォォッッ！！
    voice "sp90_s1624_012"
    s "N-Noooo!!{#sp90_s1624_012}"

    # き、きゃーーっ！サイトぉぉっ！
    voice "sp90_s1624_013"
    l "K-Kyaaah! Saitooo!!{#sp90_s1624_013}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay19    hide, vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [SPRITE   lay9     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay9     hide, reset]
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay19    hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # ………。……。…。[BG       stage    image=+88, level=200][TRANS
    th "………。……。…。{#sp90_s1624_035}"

    # ……い、生きてるか相棒？
    voice "sp90_s1624_036"
    th "…H-Hey, you still alive, partner?{#sp90_s1624_036}"

    # ……ああ。多分、な。
    voice "sp90_s1624_037"
    s "…Yeah. Maybe.{#sp90_s1624_037}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1625:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # ち、違うっ！誤解だっ！冤罪でありますぅっ！
    voice "sp90_s1625_002"
    s "N-No, that's not it! It's a misunderstanding! It's a false accusation!{#sp90_s1625_002}"

    # 大却下よっ！
    voice "sp90_s1625_003"
    l "Utterly rejected!{#sp90_s1625_003}"

    # → next scene 1628
    jump sp90_scene_1628

label sp90_scene_1626:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # （に、逃げるが勝ちだよなっ！）
    s "(Heh, running away is the winning move, right?!){#sp90_s1626_002}"

    # ……って、げえっ！鍵がかけられてて逃げられない。
    voice "sp90_s1626_003"
    s "…Wait—ugh! It's locked, I can't get out.{#sp90_s1626_003}"

    # 甘いわよっ！このバカ犬っ！
    voice "sp90_s1626_004"
    l "You're way too naive! You stupid dog!{#sp90_s1626_004}"

    # → next scene 1628
    jump sp90_scene_1628

label sp90_scene_1627:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # お、俺のご主人様は、こ、これ以上ないってぐらい可愛いです。
    voice "sp90_s1627_002"
    s "Ah, my mistress is—c-cuter than anything!{#sp90_s1627_002}"

    # ……な、なによっ！バカにしてっ！そんな言葉じゃ、だまされないんだから……。
    voice "sp90_s1627_003"
    l "…W-What are you saying?! Are you making fun of me?! I won't be fooled by words like that…{#sp90_s1627_003}"

    # → next scene 1628
    jump sp90_scene_1628

label sp90_scene_1628:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # まったくもう、このバカ犬は。少しはご主人様のありがたみってものを感じてもらう必要があるみたいね。
    voice "sp90_s1628_002"
    l "Honestly, this stupid dog. I suppose I need to make him feel a little gratitude toward his mistress.{#sp90_s1628_002}"

    # 今日の夜は、部屋から追い出してみようかな。廊下で寝てみる？
    voice "sp90_s1628_003"
    l "Tonight, I think I'll try kicking you out of the room. How about sleeping in the hallway?{#sp90_s1628_003}"

    # ル、ルイズっ！！！それだけは！！は、反省するから、な、な！
    voice "sp90_s1628_004"
    s "L-Louise!! Anything but that!! I-I'll reflect on it, I—!{#sp90_s1628_004}"

    # いまさら反省しても遅い！！
    voice "sp90_s1628_005"
    l "It's too late to be sorry now!!{#sp90_s1628_005}"

    # （廊下は寒いしなぁ……。なんとしても拒絶したい）
    s "(The hallway's cold, too… I've got to refuse somehow!){#sp90_s1628_006}"


    menu:
        "Yip yip!{#sp90_c_1628_1629}":
            jump sp90_scene_1629
        "…Please just call me a dog already!{#sp90_c_1628_1630}":
            jump sp90_scene_1630
        "H-Hey! I'm not a dog!{#sp90_c_1628_1631}":
            jump sp90_scene_1631

label sp90_scene_1629:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # キャインキャイン！
    voice "sp90_s1629_002"
    s "Yip yip!{#sp90_s1629_002}"

    # なっ、なによ！それっ！
    voice "sp90_s1629_003"
    l "W-What? What's that?!{#sp90_s1629_003}"

    # いや、犬とかの降伏のしるし。お腹みせて横になるヤツ。
    voice "sp90_s1629_004"
    s "No, it's a dog's way of surrendering. You show your belly and lie down.{#sp90_s1629_004}"

    # プッ、プライドってものがないのっ！お、男の子でしょ！
    voice "sp90_s1629_005"
    l "Pff! You have no pride at all! You're a boy, aren't you?!{#sp90_s1629_005}"

    # ……部屋から出て行きなさい。
    voice "sp90_s1629_006"
    l "…Get out of my room.{#sp90_s1629_006}"

    # しばらく廊下で寝て反省してればいいのよ！
    voice "sp90_s1629_007"
    l "Just sleep in the hallway for a while and reflect!{#sp90_s1629_007}"

    # → next scene 1632
    jump sp90_scene_1632

label sp90_scene_1630:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # ……もう犬と呼んでくださいワン。
    voice "sp90_s1630_002"
    s "…Just call me a dog from now on. Woof.{#sp90_s1630_002}"

    # な、なによその態度は！バカにしてっ！
    voice "sp90_s1630_003"
    l "W-What's with that attitude?! Are you making fun of me?!{#sp90_s1630_003}"

    # しばらく廊下で寝て反省してなさい！
    voice "sp90_s1630_004"
    l "Sleep in the hallway for a while and reflect!{#sp90_s1630_004}"

    # → next scene 1632
    jump sp90_scene_1632

label sp90_scene_1631:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # お、俺は犬じゃねえっ！
    voice "sp90_s1631_002"
    s "H-Hey, I'm not a dog!{#sp90_s1631_002}"

    # ……じゃあ、何なの？
    voice "sp90_s1631_003"
    l "…Then what are you?{#sp90_s1631_003}"

    # え？……ええと……使い魔かな？
    voice "sp90_s1631_004"
    s "Huh? …Well… a familiar, I guess?{#sp90_s1631_004}"

    # だったら、ご主人様の言うことを聞くわよね？わたしの部屋から出て行きなさいっ！
    voice "sp90_s1631_005"
    l "Then you'll obey your mistress, won't you? Now get out of my room!{#sp90_s1631_005}"

    # ご主人様のありがたみというものを一度しっかり噛みしめてみることねっ！
    voice "sp90_s1631_006"
    l "Make sure you really savor the favor of having a mistress at least once!{#sp90_s1631_006}"

    # → next scene 1632
    jump sp90_scene_1632

label sp90_scene_1632:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # ………。……。…。[EVENT_CG event    image=+170, level=80][TRANS
    th "………。……。…。{#sp90_s1632_005}"

    # ううっ、ちくしょう……。
    voice "sp90_s1632_006"
    s "Ugh… damn it…{#sp90_s1632_006}"

    # ほ、本当に部屋を追い出しやがって。ルイズめ……。
    voice "sp90_s1632_007"
    s "H-She really went and kicked me out. That Louise…{#sp90_s1632_007}"

    # ……ったく。なにやってるんだか。相棒。
    voice "sp90_s1632_008"
    th "…Honestly. What are you up to, partner?{#sp90_s1632_008}"

    # う、うるせー！
    voice "sp90_s1632_009"
    s "S-Shut up!{#sp90_s1632_009}"

    # 床は硬くて冷たいのう。
    voice "sp90_s1632_010"
    th "The floor's hard and cold, isn't it.{#sp90_s1632_010}"

    # ああ、まったくだ……。デルフ。
    voice "sp90_s1632_011"
    s "Yeah, tell me about it… Derf.{#sp90_s1632_011}"

    # [SE       se0      play=+57]
    # [EVENT_CG event    image=+171, level=80]
    $ dissolve_fx("id(171)")
    # ……サイト、起きてる？
    voice "sp90_s1632_014"
    l "…Saito, are you awake?{#sp90_s1632_014}"

    # おかげさまで眠れてないですよ……。廊下は硬くて冷たいし。
    voice "sp90_s1632_015"
    s "Thanks to you, I can't sleep a wink… The hallway's hard and cold, too.{#sp90_s1632_015}"

    # [EVENT_CG event    image=+172, level=80]
    $ dissolve_fx("id(172)")
    # [SPRITE   lay1     hide]
    # もうっ、仕方ないわね。部屋に入っていいわよ。
    voice "sp90_s1632_018"
    l "Honestly, I suppose it can't be helped. You can come back inside.{#sp90_s1632_018}"

    # い、いいんですか？そ、それじゃあお言葉に甘えて……。
    voice "sp90_s1632_019"
    s "A-Are you sure? Well then, I'll take you up on it…{#sp90_s1632_019}"

    # ホントに……もうっ！
    voice "sp90_s1632_020"
    l "Really… Honestly!{#sp90_s1632_020}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay19    hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1633:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+119, level=80]
    $ dissolve_fx("id(119)")
    # [TRANS trans("crossfade", 1000)]
    # キュルケ～～っ！
    voice "sp90_s1633_009"
    s "Kircheeee!{#sp90_s1633_009}"

    # やれやれ、ホントにヴァリエールにも困ったものよね。このままだと、ダーリンをもらっちゃうわよ？
    voice "sp90_s1633_010"
    k "My, my. La Vallière really is hopeless, isn't she? At this rate, I'll be stealing darling from you.{#sp90_s1633_010}"

    # → next scene 1636
    jump sp90_scene_1636

label sp90_scene_1634:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+119, level=80]
    $ dissolve_fx("id(119)")
    # [TRANS trans("crossfade", 1000)]
    # キュルケ～～っ！
    voice "sp90_s1634_009"
    s "Kircheeee!{#sp90_s1634_009}"

    # き、きゃあっっ！あんっ、ダーリンったら……。
    voice "sp90_s1634_010"
    k "K-Kyaa! Oh, darling…{#sp90_s1634_010}"

    # もうっ、仕方がないわね……。
    voice "sp90_s1634_011"
    k "Honestly, it can't be helped…{#sp90_s1634_011}"

    # → next scene 1636
    jump sp90_scene_1636

label sp90_scene_1635:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+119, level=80]
    $ dissolve_fx("id(119)")
    # [TRANS trans("crossfade", 1000)]
    # あっ！ご、ごめんっ！
    voice "sp90_s1635_009"
    s "Ah! I-I'm sorry!{#sp90_s1635_009}"

    # あら、あたしの胸はお気に召さなかった？
    voice "sp90_s1635_010"
    k "Oh? Didn't my chest meet with your approval?{#sp90_s1635_010}"

    # そ、そんなことはない……けど……。
    voice "sp90_s1635_011"
    s "N-No, that's not it… but…{#sp90_s1635_011}"

    # それとも……。実はルイズみたいなぺったんこがお好みかしら？
    voice "sp90_s1635_012"
    k "Or… do you actually prefer them flat like Louise?{#sp90_s1635_012}"

    # そ、そんなことはまったくないです。
    voice "sp90_s1635_013"
    s "N-No, not at all!{#sp90_s1635_013}"

    # → next scene 1636
    jump sp90_scene_1636

label sp90_scene_1636:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+119, level=80]
    $ dissolve_fx("id(119)")
    # ねえ、ここじゃなんだし……。あたしの部屋においでなさいよ？ダーリンのこと暖めてあげるわよ？
    voice "sp90_s1636_002"
    k "Hey, this is no place for it… Why don't you come to my room? I'll warm darling up for you.{#sp90_s1636_002}"


    menu:
        "…Maybe I'll take you up on that.{#sp90_c_1636_1637}":
            jump sp90_scene_1637
        "…E-Eh, I'll pass.{#sp90_c_1636_1638}":
            jump sp90_scene_1638
        "What should I do?{#sp90_c_1636_1639}":
            jump sp90_scene_1639

label sp90_scene_1637:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+119, level=80]
    $ dissolve_fx("id(119)")
    # ……お、お邪魔しちゃおうかな？
    voice "sp90_s1637_002"
    s "…I-I suppose I'll intrude, then?{#sp90_s1637_002}"

    # うふふ、さあいらっしゃいな。
    voice "sp90_s1637_003"
    k "Ufufu, come on in.{#sp90_s1637_003}"

    # [SE       se0      play=+57]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+171, level=80]
    $ dissolve_fx("id(171)")
    # [TRANS trans("crossfade", 1000)]
    # な、なに考えてるのよ！バカ犬！
    voice "sp90_s1637_010"
    l "W-What are you thinking?! You stupid dog!{#sp90_s1637_010}"

    # ……ひいっ！い、いえ、あのその。
    voice "sp90_s1637_011"
    s "…Eek! N-No, I—uh, that is…{#sp90_s1637_011}"

    # 部屋を追い出されたかわいそうなダーリンを、暖めてあげようとしただけよ？ダーリンだってあたしがいいわよね？
    voice "sp90_s1637_012"
    k "I only wanted to warm up poor darling, who'd been kicked out of his room. You like me more, don't you, darling?{#sp90_s1637_012}"

    # お、おおうっ……そんな……胸を押し付けられると……。
    voice "sp90_s1637_013"
    s "O-Ooh… that's… when your chest is pressed against mine…{#sp90_s1637_013}"

    # [EVENT_CG event    image=+172, level=80]
    $ dissolve_fx("id(172)")
    # ……バババ、バカ犬っ！今日のところは許してあげるわ！早く部屋に戻りなさいっ！
    voice "sp90_s1637_015"
    l "…B-B-Baka dog! I'll let you off today! Now get back to your room!{#sp90_s1637_015}"

    # うふふ、ムキにならなくてもいいのに……。
    voice "sp90_s1637_016"
    k "Ufufu, there's no need to get so worked up…{#sp90_s1637_016}"

    # お、大きなお世話よ！
    voice "sp90_s1637_017"
    l "T-That's none of your business!{#sp90_s1637_017}"

    # → next scene 1640
    jump sp90_scene_1640

label sp90_scene_1638:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+119, level=80]
    $ dissolve_fx("id(119)")
    # ……え、遠慮します。
    voice "sp90_s1638_002"
    s "……E-Eh, I'll pass.{#sp90_s1638_002}"

    # え～～っ！つまんな～～いっ！
    voice "sp90_s1638_003"
    k "Ehhh~! How boriiing!{#sp90_s1638_003}"

    # ほらほら、ね。いいじゃない？ダーリンのこと、暖めてあげるわよ。
    voice "sp90_s1638_004"
    k "Come on, now. It's fine, isn't it? I'll keep you warm, darling.{#sp90_s1638_004}"

    # う、うわっ、そんな胸を押し付けないで……。
    voice "sp90_s1638_005"
    s "U-Uwah! Don't press your chest against me like that……{#sp90_s1638_005}"

    # [SE       se0      play=+57]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+171, level=80]
    $ dissolve_fx("id(171)")
    # [TRANS trans("crossfade", 1000)]
    # な、なに考えてるのよ！キュルケ！
    voice "sp90_s1638_012"
    l "W-What are you thinking, Kirche?!{#sp90_s1638_012}"

    # ……ひいっ、ルイズっ！
    voice "sp90_s1638_013"
    s "……Eep! Louise!{#sp90_s1638_013}"

    # あら、別に……。部屋を追い出されたかわいそうなダーリンを、拾ってさしあげようとしただけよ？
    voice "sp90_s1638_014"
    k "Oh, not at all…… I was just trying to take in a poor darling who'd been kicked out of his room, that's all?{#sp90_s1638_014}"

    # な、なによ！むりやり部屋に連れ込もうとしてたじゃないっ！
    voice "sp90_s1638_015"
    l "W-What do you mean, 'just'!? You were trying to drag him into your room by force!{#sp90_s1638_015}"

    # [SPRITE   lay6     hide]
    # つまり、ずっとドアの内側でこちらの様子をうかがってたの？
    voice "sp90_s1638_017"
    k "So you were hiding behind the door, watching us this whole time?{#sp90_s1638_017}"

    # [EVENT_CG event    image=+172, level=80]
    $ dissolve_fx("id(172)")
    # ち、違うわよ！
    voice "sp90_s1638_019"
    l "T-That's not it!{#sp90_s1638_019}"

    # ツェルプストーの誘いを断ったことに免じて今日のところは許してあげる。だから、早く部屋に戻りなさいっ！
    voice "sp90_s1638_020"
    l "I'll forgive you for today, since you turned down Zerbst's invitation. So hurry back to your room!{#sp90_s1638_020}"

    # うふふ、ムキにならなくてもいいのに……。
    voice "sp90_s1638_021"
    k "Ufufu. You don't have to get so worked up, you know……{#sp90_s1638_021}"

    # お、大きなお世話よ！
    voice "sp90_s1638_022"
    l "O-Oh, mind your own business!{#sp90_s1638_022}"

    # → next scene 1640
    jump sp90_scene_1640

label sp90_scene_1639:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+119, level=80]
    $ dissolve_fx("id(119)")
    # ……ど、どうしようかな？
    voice "sp90_s1639_002"
    s "……W-What should I do?{#sp90_s1639_002}"

    # もう、ダーリン。何を迷ってるのよ……。
    voice "sp90_s1639_003"
    k "Really, darling. What are you hesitating about……?{#sp90_s1639_003}"

    # はうっ！
    voice "sp90_s1639_004"
    s "Guh!{#sp90_s1639_004}"

    # （そんな、胸を押し付けられると……）
    s "(N-No, not with her chest pressed against me like this……){#sp90_s1639_005}"

    # ほらほら、ね。いいじゃない？いっしょに暖かいことしよう。
    voice "sp90_s1639_006"
    k "Come on, now. It's fine, isn't it? Let's get warm together.{#sp90_s1639_006}"

    # （う、ううっ、このまま流されたい……）[SE       se0      play=+57][SPRITE 
    s "(U-Ugh…… I want to just let myself be swept away……){#sp90_s1639_007}"

    # ちゃんと断りなさい！！バカ犬っ！
    voice "sp90_s1639_008"
    l "Refuse her properly!! You stupid dog!{#sp90_s1639_008}"

    # はっ、はいっ！ご主人様っ！
    voice "sp90_s1639_009"
    s "Hah! Y-Yes, master!{#sp90_s1639_009}"

    # ひ、人の使い魔にあまりちょっかいを出さないでよね！キュルケ！
    voice "sp90_s1639_010"
    l "D-Don't you go messing with someone else's familiar! Kirche!{#sp90_s1639_010}"

    # そう思ってるんだったら、もう少し大事にしたら？
    voice "sp90_s1639_011"
    k "If that's what you think, then maybe you should treat him a little better?{#sp90_s1639_011}"

    # [EVENT_CG event    image=+172, level=80]
    $ dissolve_fx("id(172)")
    # な、なんですって！
    voice "sp90_s1639_013"
    l "W-What did you say!?{#sp90_s1639_013}"

    # サイト、早く部屋に戻りなさいっ！今日のところは許してあげる。
    voice "sp90_s1639_014"
    l "Saito, get back to your room at once! I'll let you off today.{#sp90_s1639_014}"

    # ……は、は～い！
    voice "sp90_s1639_015"
    s "……Y-Yes, ma'am!{#sp90_s1639_015}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [EVENT_CG event    hide]
    # 続きは今度ね。……バイバイ、ダーリン。
    voice "sp90_s1639_020"
    k "To be continued next time…… Bye-bye, darling.{#sp90_s1639_020}"

    # → next scene 1640
    jump sp90_scene_1640

label sp90_scene_1640:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+172, level=80]
    $ dissolve_fx("id(172)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1641:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+170, level=80]
    $ dissolve_fx("id(170)")
    # みんなのところに転がり込んだら……、ルイズはまたへそを曲げるよなあ。
    voice "sp90_s1641_002"
    s "If I move in with the others…… Louise will just sulk again, I bet.{#sp90_s1641_002}"

    # ……。
    voice "sp90_s1641_003"
    s "……{#sp90_s1641_003}"

    # （……子供の頃、よく秘密基地とか作ったもんだよな）
    s "(……I used to make secret hideouts and stuff as a kid, didn't I?){#sp90_s1641_004}"

    # （こっちの世界にはダンボールとかビニールシートはないけどさ……ホント、日本とは違う世界なんだよな）
    s "(No cardboard or plastic sheeting in this world, though…… Honestly, it really is a different world from Japan.){#sp90_s1641_005}"

    # ……はぁ。日本に帰りたい。
    voice "sp90_s1641_006"
    s "……Haaah. I want to go home to Japan.{#sp90_s1641_006}"

    # → next scene 1644
    jump sp90_scene_1644

label sp90_scene_1642:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+170, level=80]
    $ dissolve_fx("id(170)")
    # 廊下生活か……。まあ、食事の心配がないだけましだよな。
    voice "sp90_s1642_002"
    s "Living in the hallway, huh…… Well, at least I don't have to worry about food.{#sp90_s1642_002}"

    # （……もし、ご飯を食べさせてもらえなくなったら、俺はどうなるんだろう？）
    s "(……If she stopped feeding me, what would happen to me?){#sp90_s1642_003}"

    # （……やっぱ、野垂れ死に？）
    s "(……Guess I'd just die by the roadside, huh?){#sp90_s1642_004}"

    # ……はぁ、考えるのやめよう。
    voice "sp90_s1642_005"
    s "……Haaah, I'll stop thinking about it.{#sp90_s1642_005}"

    # 元の世界はどうなってるんだろうなぁ。帰りてえよぉ～～っ！
    voice "sp90_s1642_006"
    s "I wonder what's happening back in my old world…… I wanna go hooome~!{#sp90_s1642_006}"

    # → next scene 1644
    jump sp90_scene_1644

label sp90_scene_1643:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+170, level=80]
    $ dissolve_fx("id(170)")
    # ……女の子のところに転がり込もうかな？
    voice "sp90_s1643_002"
    s "……Maybe I should go crash at one of the girls' places?{#sp90_s1643_002}"

    # おい相棒……。その発想はなんだかダメ人間っぽいぞ。
    voice "sp90_s1643_003"
    th "Hey, buddy…… That's a pretty pathetic way to think, you know.{#sp90_s1643_003}"

    # ……うっ。そ、そうだよな。
    voice "sp90_s1643_004"
    s "……Ugh. Y-Yeah, you're right.{#sp90_s1643_004}"

    # しかも、そんなことしたらルイズを怒らせるだけだし。
    voice "sp90_s1643_005"
    s "And besides, doing that would just make Louise angry.{#sp90_s1643_005}"

    # （……ホント。ご飯を食べるのって大変だよなあ）
    s "(……True enough. Getting to eat is real work, isn't it?){#sp90_s1643_006}"

    # （……はぁ、日本に帰りたい）→ next scene 1644
    s "(……Haaah. I want to go back to Japan.){#sp90_s1643_007}"

label sp90_scene_1644:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+170, level=80]
    $ dissolve_fx("id(170)")
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # ………。……。…。[EVENT_CG event    image=+170, level=80][TRANS
    th "………。……。…。{#sp90_s1644_004}"

    # ちくしょう、カップ麺食いたいなぁ。
    voice "sp90_s1644_005"
    s "Damn, I could go for some cup noodles.{#sp90_s1644_005}"

    # 白いご飯とみそ汁なんかもいいよなぁ。
    voice "sp90_s1644_006"
    s "Some white rice and miso soup would be nice too, huh.{#sp90_s1644_006}"

    # ……はぁ。
    voice "sp90_s1644_007"
    s "……Haaah.{#sp90_s1644_007}"

    # ……ため息ばかりついてると幸せが逃げるぜ。相棒。
    voice "sp90_s1644_008"
    th "……If you keep sighing like that, happiness'll run away from you, buddy.{#sp90_s1644_008}"

    # うるせー。俺だってホームシックになるときぐらいあるんだよ。
    voice "sp90_s1644_009"
    s "Shut up. Even I get homesick sometimes, you know.{#sp90_s1644_009}"


    menu:
        "……Why did this have to happen to me?{#sp90_c_1644_1645}":
            jump sp90_scene_1645
        "Japan was nice, wasn't it……{#sp90_c_1644_1646}":
            jump sp90_scene_1646
        "This place is nice too, but……{#sp90_c_1644_1647}":
            jump sp90_scene_1647

label sp90_scene_1645:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+170, level=80]
    $ dissolve_fx("id(170)")
    # 俺は平凡に日本で暮らしてたのにさ……。
    voice "sp90_s1645_002"
    s "I was just living an ordinary life in Japan……{#sp90_s1645_002}"

    # ……なんでこんな目に？
    voice "sp90_s1645_003"
    s "……Why did this happen to me?{#sp90_s1645_003}"

    # まあ、とりあえず、あの貴族の娘っ子を恨むんじゃねえぜ……。
    voice "sp90_s1645_004"
    th "Well, for starters, don't go blaming that noble girl……{#sp90_s1645_004}"

    # 分かってるけど……。こういう仕打ちを受けてると……。
    voice "sp90_s1645_005"
    s "I know, but…… When you're treated like this……{#sp90_s1645_005}"

    # → next scene 1648
    jump sp90_scene_1648

label sp90_scene_1646:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+170, level=80]
    $ dissolve_fx("id(170)")
    # 日本は良かったな……。
    voice "sp90_s1646_002"
    s "Japan was nice, wasn't it……{#sp90_s1646_002}"

    # 豊かで……平和で……。いろいろ不満や問題もあったけど……、
    voice "sp90_s1646_003"
    s "Prosperous…… peaceful…… There were all kinds of complaints and problems, but……{#sp90_s1646_003}"

    # 思い出してみると、やっぱり自慢できるいい故郷だった気がするなぁ。
    voice "sp90_s1646_004"
    s "Thinking back on it, I really think it was a hometown I could be proud of.{#sp90_s1646_004}"

    # ……相棒、そういうことを言っている奴は、戦場で死んだりするぞ。
    voice "sp90_s1646_005"
    th "……Buddy, people who talk like that end up dying on the battlefield, you know.{#sp90_s1646_005}"

    # うっ、それって俺の故郷じゃ死亡フラグっていうんだよ。
    voice "sp90_s1646_006"
    s "Ugh, that's what people call a 'death flag' for my hometown, isn't it?{#sp90_s1646_006}"

    # ……まあ、相棒は死にそうにないな。
    voice "sp90_s1646_007"
    th "……Well, you don't look like you're about to die, buddy.{#sp90_s1646_007}"

    # → next scene 1648
    jump sp90_scene_1648

label sp90_scene_1647:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+170, level=80]
    $ dissolve_fx("id(170)")
    # ここもいいところだよ。
    voice "sp90_s1647_002"
    s "This place is nice too.{#sp90_s1647_002}"

    # 退屈な日本じゃ体験できないことがいろいろあるし、かわいい女の子達がたくさんいる。
    voice "sp90_s1647_003"
    s "There are lots of things you can't experience in boring Japan, and plenty of cute girls.{#sp90_s1647_003}"

    # ……でも、やっぱり帰りたいよな。日本には。
    voice "sp90_s1647_004"
    s "……But still, I want to go back. To Japan.{#sp90_s1647_004}"

    # ……ふ～～ん。そうかい。
    voice "sp90_s1647_005"
    th "……Huuuuh. I see.{#sp90_s1647_005}"

    # → next scene 1648
    jump sp90_scene_1648

label sp90_scene_1648:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+170, level=80]
    $ dissolve_fx("id(170)")
    # [SE       se0      play=+57]
    # [EVENT_CG event    image=+171, level=80]
    $ dissolve_fx("id(171)")
    # ……サイト、ちゃんといたのね。
    voice "sp90_s1648_004"
    l "……Saito, you were where you were supposed to be, I see.{#sp90_s1648_004}"

    # は、はいっ！なんでしょうかご主人様！
    voice "sp90_s1648_005"
    s "Y-Yes! What is it, master!?{#sp90_s1648_005}"

    # ……外に使い魔を放っておいては、変な噂が立つでしょ！もういいから、入りなさい！
    voice "sp90_s1648_006"
    l "……If you leave your familiar outside, people will start weird rumors, won't they! Never mind, just come in!{#sp90_s1648_006}"

    # え、いいの？ホントに？
    voice "sp90_s1648_007"
    s "Eh? Are you sure? Really?{#sp90_s1648_007}"

    # バカ犬はお外がいいのかしら？
    voice "sp90_s1648_008"
    l "Does the stupid dog prefer being outside, I wonder?{#sp90_s1648_008}"

    # キャインキャイン！ワンワン！
    voice "sp90_s1648_009"
    s "Kyain! Kyain! Woof, woof!{#sp90_s1648_009}"

    # ……おやおや、全く現金なもんだ。
    voice "sp90_s1648_010"
    th "……My, my. How mercenary.{#sp90_s1648_010}"

    # ところで、サイト？
    voice "sp90_s1648_011"
    l "By the way, Saito?{#sp90_s1648_011}"

    # さっき、何の話をしていたの？
    voice "sp90_s1648_012"
    l "What were you talking about just now?{#sp90_s1648_012}"

    # べ、別になにも？
    voice "sp90_s1648_013"
    s "N-Nothing at all?{#sp90_s1648_013}"

    # [EVENT_CG event    image=+172, level=80]
    $ dissolve_fx("id(172)")
    # [SPRITE   lay1     hide]
    # フ、フンだ！ならいいんだけど！あんたのご主人様はわたしだけなんだからね！
    voice "sp90_s1648_016"
    l "H-Hmph! Then it's fine! Just remember I'm the only master you have!{#sp90_s1648_016}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1649:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+173, level=80]
    $ dissolve_fx("id(173)")
    # つ、付き合ってられるかっ！
    voice "sp90_s1649_002"
    s "T-There's no way I can take this!{#sp90_s1649_002}"

    # あら？そんな格好でどこに行くつもり？
    voice "sp90_s1649_003"
    l "Oh? And where do you think you're going dressed like that?{#sp90_s1649_003}"

    # へっ？……はっ！
    voice "sp90_s1649_004"
    s "Heh?…… Hah!{#sp90_s1649_004}"

    # しまった！女の子の衣装ぉぉっ！？いつの間に！
    voice "sp90_s1649_005"
    s "Shit! I'm wearing girls' clothes!? Since when!?{#sp90_s1649_005}"

    # さっそく変身した姿を誰かに見てもらいたいなんて……。気に入ってもらえたのかしら？
    voice "sp90_s1649_006"
    l "Can't wait to show off your new look to someone…… Do you like it, I wonder?{#sp90_s1649_006}"

    # ちっ、違うぅぅぅっ！
    voice "sp90_s1649_007"
    s "Tch, that's not it at all!{#sp90_s1649_007}"

    # → next scene 1652
    jump sp90_scene_1652

label sp90_scene_1650:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+173, level=80]
    $ dissolve_fx("id(173)")
    # （……が、我慢だ！）
    s "(……But I've got to put up with it!){#sp90_s1650_002}"

    # あら？どうしたの黙っちゃって。
    voice "sp90_s1650_003"
    l "Oh? Why so quiet all of a sudden?{#sp90_s1650_003}"

    # ほらほら、ちゃんと鏡を見るのよっ！
    voice "sp90_s1650_004"
    l "Come on, take a proper look in the mirror!{#sp90_s1650_004}"

    # ううっ。お、男の尊厳が……プライドが……。
    voice "sp90_s1650_005"
    s "Ugh. My…… my dignity as a man…… my pride……{#sp90_s1650_005}"

    # （な、何か大切なものを失った気がする……）→ next scene 1652
    s "(I-I feel like I've lost something important……){#sp90_s1650_006}"

label sp90_scene_1651:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+173, level=80]
    $ dissolve_fx("id(173)")
    # ……こ、これが、ボク？
    voice "sp90_s1651_002"
    s "……Th-This is me…?{#sp90_s1651_002}"

    # な、なにうっとり鏡なんて見てるのよっ！
    voice "sp90_s1651_003"
    l "W-Why are you gazing at the mirror in a daze like that!?{#sp90_s1651_003}"

    # なにか新しい自分に……。
    voice "sp90_s1651_004"
    s "Like something new inside me……{#sp90_s1651_004}"

    # 目覚めるんじゃないわよっ！
    voice "sp90_s1651_005"
    l "You're not 'awakening' to anything, got it!?{#sp90_s1651_005}"

    # きゃいん！
    voice "sp90_s1651_006"
    s "Kyaing!{#sp90_s1651_006}"

    # → next scene 1652
    jump sp90_scene_1652

label sp90_scene_1652:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+173, level=80]
    $ dissolve_fx("id(173)")
    # ううっ、しかし……。
    voice "sp90_s1652_002"
    s "Ugh. But still……{#sp90_s1652_002}"

    # スカートってなんでこんなにスースーとするんだよ？
    voice "sp90_s1652_003"
    s "Why does wearing a skirt feel so drafty?{#sp90_s1652_003}"

    # 知らないわよっ！
    voice "sp90_s1652_004"
    l "How would I know!?{#sp90_s1652_004}"

    # それにしても、なかなか似合うわね……。
    voice "sp90_s1652_005"
    l "That said, it suits you quite well, doesn't it……{#sp90_s1652_005}"

    # お、大きなお世話だ！
    voice "sp90_s1652_006"
    s "O-Oh, mind your own business!{#sp90_s1652_006}"

    # 違和感もあんまり……少しつまらないかも？
    voice "sp90_s1652_007"
    l "Hardly any awkwardness either…… Maybe it's a bit dull?{#sp90_s1652_007}"

    # （まあ、さすがに胸はないから、まだ正気を保っていられるんだな……。うんうん）
    s "(Well, at least I don't have breasts, so I can still keep my sanity…… Uh-huh.){#sp90_s1652_008}"

    # な、何か言いたいことでもあるわけ？
    voice "sp90_s1652_009"
    l "D-Do you have something you want to say or something?{#sp90_s1652_009}"

    # あ、いや……。
    voice "sp90_s1652_010"
    s "Ah, no……{#sp90_s1652_010}"


    menu:
        "No breasts, so the clothes feel normal?{#sp90_c_1652_1653}":
            jump sp90_scene_1653
        "Even without a chest, I'm still cute, right?{#sp90_c_1652_1654}":
            jump sp90_scene_1654
        "Could it be that my chest is bigger?{#sp90_c_1652_1655}":
            jump sp90_scene_1655

label sp90_scene_1653:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+173, level=80]
    $ dissolve_fx("id(173)")
    # 胸がないからルイズの服を借りても違和感がないのかなぁ……と思って。
    voice "sp90_s1653_002"
    s "I was thinking… since I don't have a chest, maybe borrowing Louise's clothes wouldn't look strange at all…{#sp90_s1653_002}"

    # ど、どういう意味よっ？
    voice "sp90_s1653_003"
    l "Wh-What's that supposed to mean?!{#sp90_s1653_003}"

    # い、いやほら。俺とスタイルがあんまり変わらないような気がしただけで……。
    voice "sp90_s1653_004"
    s "N-No, see. I just had a feeling our builds weren't all that different… that's all…{#sp90_s1653_004}"

    # そそそ、そんなわけないでしょっ！？
    voice "sp90_s1653_005"
    l "N-No, no, no! That can't possibly be true, can it!?{#sp90_s1653_005}"

    # い、いい加減なことをいうと……。
    voice "sp90_s1653_006"
    l "S-Say another word like that and…!{#sp90_s1653_006}"

    # ま、待った！冗談！勘違い！
    voice "sp90_s1653_007"
    s "W-Wait! I was joking! You've got it all wrong!{#sp90_s1653_007}"

    # 自業自得よっ！
    voice "sp90_s1653_008"
    l "Serves you right!{#sp90_s1653_008}"

    # [SE       se0      play=+62]
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
    # ひっ、ひいいぃーーーーっ！
    voice "sp90_s1653_019"
    s "G-Guh… hiiiiii—!!{#sp90_s1653_019}"

    # → next scene 1656
    jump sp90_scene_1656

label sp90_scene_1654:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+173, level=80]
    $ dissolve_fx("id(173)")
    # 胸がなくても、かわいいものはかわいいな、と……。
    voice "sp90_s1654_002"
    s "Even without a chest, cute is still cute, I figured…{#sp90_s1654_002}"

    # あ、あら？そうかしら？
    voice "sp90_s1654_003"
    l "O-Oh? Is that so, then?{#sp90_s1654_003}"

    # 自分を見てつくづくそう思ったね。
    voice "sp90_s1654_004"
    s "Looking at myself, I really thought so.{#sp90_s1654_004}"

    # し、死になさい！このバカ犬！
    voice "sp90_s1654_005"
    l "G-Go die! You stupid dog!{#sp90_s1654_005}"

    # [SE       se0      play=+62]
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
    # ぐ、ぐはーーーっ！
    voice "sp90_s1654_016"
    s "G-Guhhh—!!{#sp90_s1654_016}"

    # → next scene 1656
    jump sp90_scene_1656

label sp90_scene_1655:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+173, level=80]
    $ dissolve_fx("id(173)")
    # もしかして、俺の方が胸が大きくない？
    voice "sp90_s1655_002"
    s "Wait… do I actually have bigger breasts than you?{#sp90_s1655_002}"

    # そんなわけあるはずないでしょ！
    voice "sp90_s1655_003"
    l "That's impossible, isn't it!?{#sp90_s1655_003}"

    # 言うに事欠いてこのバカ犬は……。ななな、なんてことを言うのよっ！
    voice "sp90_s1655_004"
    l "Of all things to say, you stupid dog…! Wh-Wh-What are you saying!?{#sp90_s1655_004}"

    # [SE       se0      play=+62]
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
    # ぐ、ぐほっ！
    voice "sp90_s1655_015"
    s "G-Guh!{#sp90_s1655_015}"

    # お、女の子の気持ちを考えなさいっ！
    voice "sp90_s1655_016"
    l "O-Oh, think about a girl's feelings for once!{#sp90_s1655_016}"

    # → next scene 1656
    jump sp90_scene_1656

label sp90_scene_1656:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+173, level=80]
    $ dissolve_fx("id(173)")
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [EVENT_CG event    hide]
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1657:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+174, level=80]
    $ dissolve_fx("id(174)")
    # こ、これが……俺？
    voice "sp90_s1657_002"
    s "T-This is… 'ore'?{#sp90_s1657_002}"

    # むっ、女の子が俺なんて言わないの！
    voice "sp90_s1657_003"
    l "Mm! A girl doesn't say 'ore'!{#sp90_s1657_003}"

    # ……ちょっと待て。俺は男の子だ。
    voice "sp90_s1657_004"
    s "…Hold on. I'm a boy.{#sp90_s1657_004}"

    # [EVENT_CG event    image=+175, level=80]
    $ dissolve_fx("id(175)")
    # ご主人様が黒と言ったら黒！女の子と言ったら女の子なんだからっ！
    voice "sp90_s1657_006"
    l "If master says black, it's black! If master says girl, you're a girl!{#sp90_s1657_006}"

    # → next scene 1660
    jump sp90_scene_1660

label sp90_scene_1658:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+174, level=80]
    $ dissolve_fx("id(174)")
    # こ、これが……ボク？
    voice "sp90_s1658_002"
    s "T-This is… 'boku'?{#sp90_s1658_002}"

    # むっ、女の子は自分のことを『ボク』なんていわないのっ！
    voice "sp90_s1658_003"
    l "Mm! A girl wouldn't call herself 'boku'!{#sp90_s1658_003}"

    # むっ、自分のことをボクっていう女の子は男のロマンなんだよっ！
    voice "sp90_s1658_004"
    s "Mm! A girl who calls herself 'boku' is a guy's romance!{#sp90_s1658_004}"

    # [EVENT_CG event    image=+175, level=80]
    $ dissolve_fx("id(175)")
    # な、なにワケの分からないことを力説してるのよ！
    voice "sp90_s1658_006"
    l "W-What are you going on about, laying it on so thick!?{#sp90_s1658_006}"

    # → next scene 1660
    jump sp90_scene_1660

label sp90_scene_1659:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+174, level=80]
    $ dissolve_fx("id(174)")
    # ……俺、汚れちゃった。汚されちゃったよ。
    voice "sp90_s1659_002"
    s "…I got dirty. I've been defiled.{#sp90_s1659_002}"

    # [EVENT_CG event    image=+175, level=80]
    $ dissolve_fx("id(175)")
    # な、なによ！女装のひとつやふたつで、めそめそするんじゃないのっ！
    voice "sp90_s1659_004"
    l "W-What's that?! Don't go sniveling over just one or two outfits!{#sp90_s1659_004}"

    # → next scene 1660
    jump sp90_scene_1660

label sp90_scene_1660:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+175, level=80]
    $ dissolve_fx("id(175)")
    # はあ……まったく、もう！
    voice "sp90_s1660_002"
    l "Haa… honestly, really!{#sp90_s1660_002}"

    # [EVENT_CG event    image=+174, level=80]
    $ dissolve_fx("id(174)")
    # け、けど。なんだか本当に似合うわね。少し悔しいかも？
    voice "sp90_s1660_004"
    l "B-But… it really does suit you, doesn't it? Maybe I'm a little annoyed?{#sp90_s1660_004}"

    # ……ま、まあ……な。
    voice "sp90_s1660_005"
    s "…W-Well… yeah.{#sp90_s1660_005}"

    # もう、女の子がそんな口をきいちゃダメでしょっ！
    voice "sp90_s1660_006"
    l "Honestly, a girl shouldn't talk like that!{#sp90_s1660_006}"

    # ……か、勘弁してくださいご主人様！
    voice "sp90_s1660_007"
    s "…P-Please spare me, master!{#sp90_s1660_007}"

    # [EVENT_CG event    image=+175, level=80]
    $ dissolve_fx("id(175)")
    # ほらほら！足を開かない！
    voice "sp90_s1660_009"
    l "Come on, come on! Spread your legs!{#sp90_s1660_009}"

    # 背筋を伸ばして！だらしなくしないっ！
    voice "sp90_s1660_010"
    l "Straighten your back! Don't slouch!{#sp90_s1660_010}"

    # 女の子は同性のチェックが厳しいんだからねっ！
    voice "sp90_s1660_011"
    l "Girls check each other strictly, you know!{#sp90_s1660_011}"

    # お、俺は男の子だ～～っ！！
    voice "sp90_s1660_012"
    s "I-I'm a boy, I tell you~~!!{#sp90_s1660_012}"

    # だから女の子の大変さを思い知りなさいっていうのよっ！
    voice "sp90_s1660_013"
    l "That's why you're going to learn how hard being a girl is!{#sp90_s1660_013}"

    # う、うっうっう……。
    voice "sp90_s1660_014"
    s "U-Ugh… ugh… ug…{#sp90_s1660_014}"

    # [EVENT_CG event    image=+174, level=80]
    $ dissolve_fx("id(174)")
    # ほらほら。くるって回ってごらんなさい！
    voice "sp90_s1660_016"
    l "Come on, come on. Spin around for me!{#sp90_s1660_016}"

    # そ、そんなのできないって。
    voice "sp90_s1660_017"
    s "T-There's no way I can do that.{#sp90_s1660_017}"

    # あら？なんなら、首輪もしてみようかしら？
    voice "sp90_s1660_018"
    l "Oh? Then maybe we try a collar on you, too?{#sp90_s1660_018}"

    # （ぐ、ぐはっ、いきなりピンチなんですが）
    s "(G-Guh, this came out of nowhere…!){#sp90_s1660_019}"


    menu:
        "Q-Quick, spin around!{#sp90_c_1660_1661}":
            jump sp90_scene_1661
        "Have mercy!{#sp90_c_1660_1662}":
            jump sp90_scene_1662
        "D-Do you want to see?{#sp90_c_1660_1663}":
            jump sp90_scene_1663

label sp90_scene_1661:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+174, level=80]
    $ dissolve_fx("id(174)")
    # （……やってやる！やってやるよっ！）
    s "(…I'll do it! I'll do it, I tell you!){#sp90_s1661_002}"

    # （くるって回って……）
    s "(Spin around…){#sp90_s1661_003}"

    # お、お待たせ！
    voice "sp90_s1661_004"
    s "S-Sorry for the wait!{#sp90_s1661_004}"

    # ……サイト。あなたやっぱりバカでしょ？
    voice "sp90_s1661_005"
    l "…Saito. You really are an idiot, aren't you?{#sp90_s1661_005}"

    # そ、そりゃないっすよ！ご主人様～っ！
    voice "sp90_s1661_006"
    s "T-That's not true! Master~!!{#sp90_s1661_006}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # → next scene 1664
    jump sp90_scene_1664

label sp90_scene_1662:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+174, level=80]
    $ dissolve_fx("id(174)")
    # か、勘弁してください。
    voice "sp90_s1662_002"
    s "P-Please, spare me…{#sp90_s1662_002}"

    # [EVENT_CG event    image=+175, level=80]
    $ dissolve_fx("id(175)")
    # むっ、男らしくないわよ。サイト！
    voice "sp90_s1662_004"
    l "Mm! Not very manly of you. Saito!{#sp90_s1662_004}"

    # こんな格好をさせといて男らしさなんて求めるなーーっ！
    voice "sp90_s1662_005"
    s "Don't expect me to be manly after making me dress like this—!!{#sp90_s1662_005}"

    # ほら、さっさとやりなさい！
    voice "sp90_s1662_006"
    l "Come on, hurry up and do it!{#sp90_s1662_006}"

    # （ち、ちくしょう。くるって回って……）
    s "(D-Damn it. Spin around…){#sp90_s1662_007}"

    # お、お待たせ！
    voice "sp90_s1662_008"
    s "S-Sorry for the wait!{#sp90_s1662_008}"

    # [EVENT_CG event    image=+174, level=80]
    $ dissolve_fx("id(174)")
    # はあ～～っ、ダメダメ……。はい、もう一度！
    voice "sp90_s1662_010"
    l "Haa~~, no, no… Okay, once more!{#sp90_s1662_010}"

    # （ち、ちくしょうぉぉ～～っ！）[SE       se1      stop=1][BGM      bgm 
    s "(D-Damn iiit~~!!)→ next scene 1664{#sp90_s1662_011}"

label sp90_scene_1663:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+174, level=80]
    $ dissolve_fx("id(174)")
    # ……え、え～と、ご、ご主人様は見たいんですか？
    voice "sp90_s1663_002"
    s "…U-Um, do you want to see, master?{#sp90_s1663_002}"

    # へっ？
    voice "sp90_s1663_003"
    l "Heh?{#sp90_s1663_003}"

    # お、俺のスカートの中なんか……。
    voice "sp90_s1663_004"
    s "U-Under my skirt, or… something…?{#sp90_s1663_004}"

    # [EVENT_CG event    image=+175, level=80]
    $ dissolve_fx("id(175)")
    # ……なっ、ななな！
    voice "sp90_s1663_006"
    l "…W-Wh-Wha-What?!{#sp90_s1663_006}"

    # なんてこと言うのよっ！このバカ犬っ！変態っ！
    voice "sp90_s1663_007"
    l "What a thing to say! You stupid dog! Pervert!{#sp90_s1663_007}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # → next scene 1664
    jump sp90_scene_1664

label sp90_scene_1664:

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1665:

    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # とりあえず、その手を離せギーシュ。
    voice "sp90_s1665_004"
    s "Anyway, let go of my hand, Guiche.{#sp90_s1665_004}"

    # [SPRITE   lay4     image=+559, level=160, dir=1A]
    # き、きみはっ……！だ、駄目だ、この手を離すことができない！可憐なきみが男の子だったなんて！
    voice "sp90_s1665_006"
    th "Y-You…! N-No, I can't let go of this hand! That you, so lovely, were a boy!{#sp90_s1665_006}"

    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # ……現実を見つめなさい。
    voice "sp90_s1665_008"
    th "…Face reality.{#sp90_s1665_008}"

    # [SPRITE   lay4     image=+572, level=160, dir=2A]
    # い、いや。そんなはずがない。これはきっと悪い夢だ……間違いない！
    voice "sp90_s1665_010"
    th "N-No. It can't be. This has to be a bad dream… I'm sure of it!{#sp90_s1665_010}"

    # [SPRITE   lay3     image=+889, level=160, dir=2A]
    # もうっ、情けないっ！
    voice "sp90_s1665_012"
    th "Honestly! Pathetic!{#sp90_s1665_012}"

    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # ところで、何やってたのよ。あなた達？
    voice "sp90_s1665_014"
    th "By the way, what were you two doing?{#sp90_s1665_014}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # → next scene 1668
    jump sp90_scene_1668

label sp90_scene_1666:

    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # いかがです。ギーシュさま？
    voice "sp90_s1666_004"
    s "How's it going, Guiche-sama?{#sp90_s1666_004}"

    # [SPRITE   lay4     image=+559, level=160, dir=1A]
    # き、気持ち悪い声で話しかけるなぁ！
    voice "sp90_s1666_006"
    th "D-Don't talk to me in that creepy voice!{#sp90_s1666_006}"

    # う、うるせえっ！俺だって好きでこんな格好してんじゃねぇんだっ！
    voice "sp90_s1666_007"
    s "S-Shut up! I'm not doing this because I want to, you know!{#sp90_s1666_007}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ……さ、さすがに声はどうしようもないか。
    voice "sp90_s1666_010"
    l "…E-Even so, the voice is beyond saving.{#sp90_s1666_010}"

    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # ところで、なんであんな格好させてるの？
    voice "sp90_s1666_012"
    th "By the way, why are you making him dress like that?{#sp90_s1666_012}"

    # → next scene 1668
    jump sp90_scene_1668

label sp90_scene_1667:

    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # ……な、なんだよ。この微妙な空気は！
    voice "sp90_s1667_004"
    s "…W-What's with this awkward atmosphere!?{#sp90_s1667_004}"

    # [SPRITE   lay4     image=+561, level=160, dir=1A]
    # な、なんというか……だな。
    voice "sp90_s1667_006"
    th "W-Well… how should I put it… yeah.{#sp90_s1667_006}"

    # そ、そんな生暖かい目で俺をみるなぁ！それに、その手を離せ！
    voice "sp90_s1667_007"
    s "D-Don't look at me with those lukewarm eyes! And let go of my hand!{#sp90_s1667_007}"

    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # な、なにしてたの？あなた達？
    voice "sp90_s1667_009"
    th "W-What were you two doing, anyway?{#sp90_s1667_009}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # → next scene 1668
    jump sp90_scene_1668

label sp90_scene_1668:

    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ええと……その……。
    voice "sp90_s1668_005"
    l "Um… that's…{#sp90_s1668_005}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # ………………[SPRITE   lay3     image=+858, level=160, dir=1A]
    th "…………{#sp90_s1668_007}"

    # 女の子の気持ちを……ねえ。
    voice "sp90_s1668_008"
    th "A girl's feelings… you know.{#sp90_s1668_008}"

    # え、ええ……ちょっと……。
    voice "sp90_s1668_009"
    l "Y-yes… just a little…{#sp90_s1668_009}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay4     image=+555, level=160, dir=1A]
    # たしかに、いい薬かもしれないな。
    voice "sp90_s1668_012"
    th "Indeed, it might be a good medicine.{#sp90_s1668_012}"

    # [SPRITE   lay3     image=+885, level=160, dir=2A]
    # ……あなたにも必要よ。ギーシュ。
    voice "sp90_s1668_014"
    th "…You need it too, Guiche.{#sp90_s1668_014}"

    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # それにしても……まるで別人ね……。
    voice "sp90_s1668_016"
    th "And yet… you're like a completely different person…{#sp90_s1668_016}"

    # [SPRITE   lay4     image=+572, level=160, dir=2A]
    # ……信じられん……。
    voice "sp90_s1668_018"
    th "…I can't believe it…{#sp90_s1668_018}"

    # 綺麗よね～。ルイズよりいけてるんじゃない？
    voice "sp90_s1668_019"
    th "Looking gorgeous, aren't you~? Aren't you even cuter than Louise?{#sp90_s1668_019}"

    # ……え、ルイズより？
    voice "sp90_s1668_020"
    s "…Eh? More than Louise?{#sp90_s1668_020}"


    menu:
        "A-am I really that pretty…{#sp90_c_1668_1669}":
            jump sp90_scene_1669
        "…W-well, of course… wouldn't you say?{#sp90_c_1668_1670}":
            jump sp90_scene_1670
        "I-I'm not happy…{#sp90_c_1668_1671}":
            jump sp90_scene_1671

label sp90_scene_1669:

    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # [SPRITE   lay4     image=+572, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # そ、そんなにきれいかしら……。
    voice "sp90_s1669_004"
    s "A-am I really that pretty…{#sp90_s1669_004}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # な、なに女言葉になってるのよっ！バカ犬っ！
    voice "sp90_s1669_008"
    l "W-what's with the girly talk?! Stupid dog!{#sp90_s1669_008}"

    # ……え？あ、いや！
    voice "sp90_s1669_009"
    s "…Huh? Ah, no!{#sp90_s1669_009}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ……む。
    voice "sp90_s1669_011"
    l "…Mm.{#sp90_s1669_011}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # 使い魔が女装に目覚めたなんて噂になったら大変なんだからっ。おおお、お仕置きよ！
    voice "sp90_s1669_013"
    l "If word got out that my familiar had taken up cross-dressing, it'd be a disaster! Ooh, it's punishment time!{#sp90_s1669_013}"

    # じょ、女装させたのはそっちじゃないかーーっ！
    voice "sp90_s1669_014"
    s "Y-you're the one who made me dress up like that!!{#sp90_s1669_014}"

    # ううう、うるさ～～いっ！
    voice "sp90_s1669_015"
    l "Uugh, shut uuup!{#sp90_s1669_015}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay4     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay1     reset]
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # → next scene 1672
    jump sp90_scene_1672

label sp90_scene_1670:

    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # [SPRITE   lay4     image=+572, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # ……と、当然……かな？
    voice "sp90_s1670_004"
    s "…W-well, of course… wouldn't you say?{#sp90_s1670_004}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # な、なんですってぇぇ！
    voice "sp90_s1670_008"
    l "W-what did you saaay?!{#sp90_s1670_008}"

    # ま、まったく。うちのバカ犬ったらすぐに調子にのって……。
    voice "sp90_s1670_009"
    l "R-really. My stupid dog always lets it go to his head…{#sp90_s1670_009}"

    # ふ、ふふん。ヤキモチはいけないと思います。ご主人様。
    voice "sp90_s1670_010"
    s "Hm, hmmph. Jealousy doesn't become you, Master.{#sp90_s1670_010}"

    # ……い、いい度胸ね？
    voice "sp90_s1670_011"
    l "…Oh, you've certainly got some nerve.{#sp90_s1670_011}"

    # おおお……。お・仕・置・き・よぉ～～っ！
    voice "sp90_s1670_012"
    l "Oooh… i-it's pu-ni-sh-me-eent tiiime!{#sp90_s1670_012}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay4     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay1     reset]
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # → next scene 1672
    jump sp90_scene_1672

label sp90_scene_1671:

    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # [SPRITE   lay4     image=+572, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # う、うれしくない……。
    voice "sp90_s1671_004"
    s "I-I'm not happy…{#sp90_s1671_004}"

    # [SPRITE   lay3     image=+887, level=160, dir=2A]
    # え～っ、そうかしら？ねえ、ルイズ……。
    voice "sp90_s1671_006"
    th "Eh~? Are you sure? I mean, Louise…{#sp90_s1671_006}"

    # [SPRITE   lay4     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # だ、だだ、誰がわたしよりですって？
    voice "sp90_s1671_009"
    l "W-who, who's better than me, did you say?!{#sp90_s1671_009}"

    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # あら、ええと……ほら……。
    voice "sp90_s1671_011"
    th "Oh my, well… you know…{#sp90_s1671_011}"

    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # ……む、胸はルイズの方があるんだからいいじゃない？
    voice "sp90_s1671_013"
    th "…Mm, Louise has more up top, so it's fine, isn't it?{#sp90_s1671_013}"

    # あ、あああ、あたりまえでしょぉぉっ！
    voice "sp90_s1671_014"
    l "O-obviously!!{#sp90_s1671_014}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay3     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay4     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay3     reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay4     hide, reset]
    # [SPRITE   lay1     reset]
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # → next scene 1672
    jump sp90_scene_1672

label sp90_scene_1672:

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1673:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # お、横暴だっ！
    voice "sp90_s1673_002"
    s "H-hey, that's domineering!{#sp90_s1673_002}"

    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # 口答えするんじゃないっ！
    voice "sp90_s1673_004"
    l "Don't talk back to me!{#sp90_s1673_004}"

    # [SE       se0      play=+61]
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
    # きゃいんっ！
    voice "sp90_s1673_015"
    s "Kyaah!{#sp90_s1673_015}"

    # わ、わん！分かりました～～っ！ご主人様～～っ！
    voice "sp90_s1673_016"
    s "W-woof! I understand~~! Master~~!{#sp90_s1673_016}"

    # → next scene 1676
    jump sp90_scene_1676

label sp90_scene_1674:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # わ、わん！ご主人様っ！
    voice "sp90_s1674_002"
    s "W-woof! Master!{#sp90_s1674_002}"

    # 覚えておきなさい。バカ犬はわたしの使い魔なのよ！
    voice "sp90_s1674_003"
    l "You'd better remember this: you're my familiar, you stupid dog!{#sp90_s1674_003}"

    # だから、バカ犬のその命はわたしのものなんだからね。
    voice "sp90_s1674_004"
    l "So that means your very life belongs to me, got it?{#sp90_s1674_004}"

    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # 分かったわねっ！バカ犬っ！
    voice "sp90_s1674_006"
    l "Got it?! Stupid dog!{#sp90_s1674_006}"

    # わんっ！分かりましたぁっ！ご主人様っ！
    voice "sp90_s1674_007"
    s "Woof! I understand!! Master!!{#sp90_s1674_007}"

    # → next scene 1676
    jump sp90_scene_1676

label sp90_scene_1675:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # お、俺は何もしてないっ！
    voice "sp90_s1675_002"
    s "I-I didn't do anything!{#sp90_s1675_002}"

    # ……なるほど。もう少しお仕置きの必要があるみたいね。泣いたり笑ったり出来なくなるぐらい。
    voice "sp90_s1675_003"
    l "…I see. Looks like you need a bit more punishment. Enough that you can't laugh or cry anymore.{#sp90_s1675_003}"

    # な、無茶苦茶だっ！
    voice "sp90_s1675_004"
    s "T-that's completely unreasonable!{#sp90_s1675_004}"

    # [SE       se0      play=+61]
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
    # きゃいんっ！
    voice "sp90_s1675_015"
    s "Kyaah!{#sp90_s1675_015}"

    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # 言ったわよねっ。返事はっ！
    voice "sp90_s1675_017"
    l "I told you, didn't I?! Answer me!{#sp90_s1675_017}"

    # わ、わん！分かりましたっ！ご主人様っ！
    voice "sp90_s1675_018"
    s "W-woof! I understand! Master!{#sp90_s1675_018}"

    # → next scene 1676
    jump sp90_scene_1676

label sp90_scene_1676:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # [SE       se0      play=+61]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # 声が小さい！もっと大声で！
    voice "sp90_s1676_013"
    l "Too quiet! Louder!{#sp90_s1676_013}"

    # わん！分かりました！ご主人様っ！
    voice "sp90_s1676_014"
    s "Woof! Understood! Master!{#sp90_s1676_014}"

    # [SE       se0      play=+61]
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
    # 気持ちがこもってないわっ！
    voice "sp90_s1676_025"
    l "There's no feeling in that!{#sp90_s1676_025}"

    # わんっ！わ、分かりましたぁっ！ご主人様っ！
    voice "sp90_s1676_026"
    s "Woof! I-I understand!! Master!!{#sp90_s1676_026}"

    # （ち、ちくしょう……）[EVENT_CG event    image=+178, level=80]
    s "(D-damn it…){#sp90_s1676_027}"

    # ……あら？なに、その顔は？
    voice "sp90_s1676_028"
    l "…Oh? What's with that face?{#sp90_s1676_028}"

    # [SPRITE   lay5     hide]
    # （う、うっ……）
    s "(G-guh…){#sp90_s1676_030}"

    # もっと、使い魔っぽい顔をしなさいっ！
    voice "sp90_s1676_031"
    l "Look more like a familiar!{#sp90_s1676_031}"


    menu:
        "W-what kind of face do you want me to make?!{#sp90_c_1676_1677}":
            jump sp90_scene_1677
        "…W-what do you mean, a familiar-like face?{#sp90_c_1676_1678}":
            jump sp90_scene_1678
        "Woof! Master!{#sp90_c_1676_1679}":
            jump sp90_scene_1679

label sp90_scene_1677:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # ど、どんな顔しろっていうんだよっ！
    voice "sp90_s1677_002"
    s "W-what kind of face do you want me to make?!{#sp90_s1677_002}"

    # 質問するのはわたしの役よっ！このバカ犬っ！
    voice "sp90_s1677_003"
    l "Asking the questions is my job! You stupid dog!{#sp90_s1677_003}"

    # [SE       se0      play=+61]
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
    # きゃ、きゃいーーーんっ！
    voice "sp90_s1677_014"
    s "K-kyaaaiin!!{#sp90_s1677_014}"

    # まったく、その首の上についてるのは何かしら？少しは自分で考えなさいっ！
    voice "sp90_s1677_015"
    l "Honestly, what IS on top of that neck of yours? Do some thinking on your own for once!{#sp90_s1677_015}"

    # → next scene 1680
    jump sp90_scene_1680

label sp90_scene_1678:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # ……つ、使い魔らしい顔って？
    voice "sp90_s1678_002"
    s "…W-what do you mean, a familiar-like face?{#sp90_s1678_002}"

    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # キュルケのフレイムとか、タバサのシルフィードとか……、ギーシュのヴェルダンデとか？
    voice "sp90_s1678_004"
    l "Like Kirche's Flame, or Tabitha's Sylphid… or Guiche's Verdande?{#sp90_s1678_004}"

    # わ、分かるかよっ！
    voice "sp90_s1678_005"
    s "H-how would I know?!{#sp90_s1678_005}"

    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # うるさいっ！少しは自分で考えなさいっ！このバカ犬っ！
    voice "sp90_s1678_007"
    l "Shut up! Think for yourself, just a little! You stupid dog!{#sp90_s1678_007}"

    # [SE       se0      play=+61]
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
    # きゃ、きゃいーーーんっ！
    voice "sp90_s1678_018"
    s "K-kyaaaiin!!{#sp90_s1678_018}"

    # → next scene 1680
    jump sp90_scene_1680

label sp90_scene_1679:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # わんっ！こ、こうですかっ？ご主人様っ！
    voice "sp90_s1679_002"
    s "Woof! L-like this? Master!{#sp90_s1679_002}"

    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # ダメダメねっ！練習しときなさいっ！
    voice "sp90_s1679_004"
    l "No good, no good! You'd better practice!{#sp90_s1679_004}"

    # わん！分かりました！ご主人様！
    voice "sp90_s1679_005"
    s "Woof! Understood! Master!{#sp90_s1679_005}"

    # （ひゃ、百面相の練習でもしろってか！）
    s "(Hah! Does she want me to practice a hundred different faces?!){#sp90_s1679_006}"

    # （ほ、本気で練習するつもりかしら？）
    voice "sp90_s1679_007"
    l "(H-he actually means to practice…?){#sp90_s1679_007}"

    # → next scene 1680
    jump sp90_scene_1680

label sp90_scene_1680:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1681:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # ……ご主人様への数々の失礼な態度、まことに申し訳ありませんでしたぁっ！
    voice "sp90_s1681_002"
    s "…I'm truly sorry for all the disrespectful behavior I showed you, Master!{#sp90_s1681_002}"

    # うふふ、それでいいのよ。仕方ないわね。特別に許してあげようかしら？
    voice "sp90_s1681_003"
    l "Heh heh, that's more like it. Can't be helped. Shall I forgive you, as a special favor?{#sp90_s1681_003}"

    # （……くそっ。なんで俺が謝らなくちゃいけないんだよ）
    s "(…Damn it. Why do I have to be the one apologizing?){#sp90_s1681_004}"

    # なにか、言ったかしら？
    voice "sp90_s1681_005"
    l "Did you say something?{#sp90_s1681_005}"

    # → next scene 1684
    jump sp90_scene_1684

label sp90_scene_1682:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # ……ご主人様の数々の失礼な態度、まことに申し訳ありませんでしたぁっ！
    voice "sp90_s1682_002"
    s "…I'm truly sorry for Master's countless rude behaviors!{#sp90_s1682_002}"

    # ん？なにか今、微妙におかしくなかった？
    voice "sp90_s1682_003"
    l "Hmm? Wasn't that just now a little… off?{#sp90_s1682_003}"

    # ……と、とんでもない。
    voice "sp90_s1682_004"
    s "…N-not at all.{#sp90_s1682_004}"

    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # まあ、いいわ。……とりあえず、殴っておくから。
    voice "sp90_s1682_006"
    l "Oh, whatever. …In any case, I'm going to hit you first.{#sp90_s1682_006}"

    # [SE       se0      play=+62]
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
    # きゃいん！
    voice "sp90_s1682_017"
    s "Kyaah!{#sp90_s1682_017}"

    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # → next scene 1684
    jump sp90_scene_1684

label sp90_scene_1683:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # 失礼なご主人様の数々の態度……。
    voice "sp90_s1683_002"
    s "My master's rude behavior, one thing after another…{#sp90_s1683_002}"

    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # なんですってぇ！
    voice "sp90_s1683_004"
    l "What was that?!{#sp90_s1683_004}"

    # ……あれ？違った？
    voice "sp90_s1683_005"
    s "…Huh? Did I get it wrong?{#sp90_s1683_005}"

    # うふふ、いい度胸ね……。
    voice "sp90_s1683_006"
    l "Heh heh, you've got some nerve…{#sp90_s1683_006}"

    # その、もの覚えの悪いアタマを、少し良くしてあげるわ！
    voice "sp90_s1683_007"
    l "I'll just make that forgetful head of yours a little better!{#sp90_s1683_007}"

    # [SE       se0      play=+61]
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
    # きゃいん！
    voice "sp90_s1683_018"
    s "Yip!{#sp90_s1683_018}"

    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # → next scene 1684
    jump sp90_scene_1684

label sp90_scene_1684:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # それと……。反省の言葉を教えてあげるから、わたしの後について復唱しなさい！
    voice "sp90_s1684_002"
    l "And also… I'll teach you the words of repentance, so repeat after me!{#sp90_s1684_002}"

    # わたしは、みにくいあわれな犬っころです。
    voice "sp90_s1684_003"
    l "I am an ugly, pitiful little cur.{#sp90_s1684_003}"

    # （……く、くそっ）
    s "…D-Damn it.{#sp90_s1684_004}"

    # わたしは、みにくいあわれな犬っころです。
    voice "sp90_s1684_005"
    s "I am an ugly, pitiful little cur.{#sp90_s1684_005}"

    # ご主人様のお言葉は、わたしにとって絶対です。
    voice "sp90_s1684_006"
    l "My master's words are absolute to me.{#sp90_s1684_006}"

    # ご、ご主人様のお言葉は、わたしにとって絶対です。
    voice "sp90_s1684_007"
    s "M-My master's words are absolute to me.{#sp90_s1684_007}"

    # ご主人様なしで、わたしは生きていくことはできません。
    voice "sp90_s1684_008"
    l "Without my master, I can't go on living.{#sp90_s1684_008}"

    # ご主人様なしで、わたしは生きていくことはできません！
    voice "sp90_s1684_009"
    s "Without my master, I can't go on living!{#sp90_s1684_009}"

    # これからもご主人様に忠誠を尽くしますので、どうか見捨てないでくださいませ。
    voice "sp90_s1684_010"
    l "From now on I'll keep serving my master with loyalty, so please don't abandon me.{#sp90_s1684_010}"

    # これからもご主人様に忠誠を尽くしますので、どうか見捨てないでくださいませ。
    voice "sp90_s1684_011"
    s "From now on I'll keep serving my master with loyalty, so please don't abandon me.{#sp90_s1684_011}"

    # 他の女の子にはもう二度と目を向けません。
    voice "sp90_s1684_012"
    l "I will never look at another girl again.{#sp90_s1684_012}"

    # 他の女の子にはもう二度と目を向けません……って、え？
    voice "sp90_s1684_013"
    s "I will never look at another girl again… Wait, what?{#sp90_s1684_013}"

    # うふふ、よくできたわね！
    voice "sp90_s1684_014"
    l "Heh heh, very good!{#sp90_s1684_014}"


    menu:
        "W-Woof!{#sp90_c_1684_1685}":
            jump sp90_scene_1685
        "Could I take back the last one…?{#sp90_c_1684_1686}":
            jump sp90_scene_1686
        "What about Louise's repentance?{#sp90_c_1684_1687}":
            jump sp90_scene_1687

label sp90_scene_1685:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # わ、わんっ！
    voice "sp90_s1685_002"
    s "W-Woof!{#sp90_s1685_002}"

    # うふふ、誓いは絶対なんだからね。サイト……。
    voice "sp90_s1685_003"
    l "Heh heh, because a promise is absolute, you know. Saito…{#sp90_s1685_003}"

    # ご、ご主人様。目が怖いです……。
    voice "sp90_s1685_004"
    s "M-Master. Your eyes are scary…{#sp90_s1685_004}"

    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # ……なにか文句があるのかしら？
    voice "sp90_s1685_006"
    l "…Do you have some complaint, I wonder?{#sp90_s1685_006}"

    # い、いえ。なんでもありませんです。
    voice "sp90_s1685_007"
    s "N-No. It's nothing at all.{#sp90_s1685_007}"

    # → next scene 1688
    jump sp90_scene_1688

label sp90_scene_1686:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # さ、最後のは取り消しては……？
    voice "sp90_s1686_002"
    s "Well, could I take back the last one…?{#sp90_s1686_002}"

    # 何言ってるのよ！と・に・か・く、ダメなものはダメなんだから！
    voice "sp90_s1686_003"
    l "What are you talking about! In·any·case, what's no is no!{#sp90_s1686_003}"

    # うっ……。
    voice "sp90_s1686_004"
    s "Ugh…{#sp90_s1686_004}"

    # [EVENT_CG event    image=+177, level=80]
    $ dissolve_fx("id(177)")
    # ど、どうして、そこで約束を守るって断言してくれないのよっ！もうっ！
    voice "sp90_s1686_006"
    l "W-Why won't you just say outright that you'll keep your promise? Really now!{#sp90_s1686_006}"

    # お、お仕置きよっ！
    voice "sp90_s1686_007"
    l "P-Punishment time!{#sp90_s1686_007}"

    # [SE       se0      play=+61]
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
    # → next scene 1688
    jump sp90_scene_1688

label sp90_scene_1687:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # ルイズの反省はないのかよ。
    voice "sp90_s1687_002"
    s "Don't you feel any remorse, Louise?{#sp90_s1687_002}"

    # 反省？なんで？
    voice "sp90_s1687_003"
    l "Remorse? Why?{#sp90_s1687_003}"

    # ご主人様として反省することはないのかって言ってるんだよ？
    voice "sp90_s1687_004"
    s "I'm asking if you have anything to feel remorse for as my master!{#sp90_s1687_004}"

    # あら？　寝るところと、食べるものを提供し、剣まで買い与えたご主人様が何を反省すればいいのかしら？
    voice "sp90_s1687_005"
    l "Oh? What should a master who gives you a place to sleep, food to eat, and even buys you a sword have to feel remorse for, I wonder?{#sp90_s1687_005}"

    # いえ、なんでもないです。
    voice "sp90_s1687_006"
    s "No. It's nothing.{#sp90_s1687_006}"

    # → next scene 1688
    jump sp90_scene_1688

label sp90_scene_1688:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
label sp90_scene_1689:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+177, level=80]
    $ dissolve_fx("id(177)")
    # （……逃げるんだ！地平線の果てまで）
    s "…I'll run away! To the ends of the earth!{#sp90_s1689_002}"

    # ち、ちょっと、サイト？
    voice "sp90_s1689_003"
    l "S-Saito?{#sp90_s1689_003}"

    # た、旅に出ます。探さないでください。
    voice "sp90_s1689_004"
    s "I-I'm going on a journey. Don't look for me.{#sp90_s1689_004}"

    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # 逃がすわけないでしょう！
    voice "sp90_s1689_006"
    l "As if I'd ever let you get away!{#sp90_s1689_006}"

    # [SE       se0      play=+61]
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
    # → next scene 1692
    jump sp90_scene_1692

label sp90_scene_1690:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+177, level=80]
    $ dissolve_fx("id(177)")
    # ご、ごめんなちゃい。
    voice "sp90_s1690_002"
    s "S-Sorry 'bout that.{#sp90_s1690_002}"

    # ……なんであんなことしたの？
    voice "sp90_s1690_003"
    l "…Why did you do that?{#sp90_s1690_003}"

    # い、いや。あれは出来心というか、異世界の衣服への興味でして。
    voice "sp90_s1690_004"
    s "N-No. That was… a moment of weakness, or rather, an interest in another world's clothing.{#sp90_s1690_004}"

    # 突然現れた異国の文化に知的好奇心にかられまして、ちょっくら調査研究をしてみたといいますか……。
    voice "sp90_s1690_005"
    s "Faced with a foreign culture all of a sudden, my intellectual curiosity got the better of me, and I thought I'd do a little investigating, so to speak…{#sp90_s1690_005}"

    # 純粋な青少年として当然の行為といいますか……。
    voice "sp90_s1690_006"
    s "The natural behavior of a pure young man, one might say…{#sp90_s1690_006}"

    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # ……いいたいのはそれだけ？
    voice "sp90_s1690_008"
    l "…Is that all you want to say?{#sp90_s1690_008}"

    # [SE       se0      play=+61]
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
    # → next scene 1692
    jump sp90_scene_1692

label sp90_scene_1691:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+177, level=80]
    $ dissolve_fx("id(177)")
    # ナ、ナンのコトでしょう。るいずサマ？
    voice "sp90_s1691_002"
    s "W-What could you mean? Louise-sama?{#sp90_s1691_002}"

    # な、なによ。しらを切るつもり？
    voice "sp90_s1691_003"
    l "W-What? You're going to play dumb?{#sp90_s1691_003}"

    # ア、アレはボクの故郷で男性が女性の下着を洗うトキの一般的な作法でアリマシテ……。
    voice "sp90_s1691_004"
    s "T-That's just the usual practice in my homeland when a man washes a woman's underwear, you see…{#sp90_s1691_004}"

    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # ど、どこの世界にあんな作法があるのよっ！
    voice "sp90_s1691_006"
    l "W-What kind of world has a custom like that?!{#sp90_s1691_006}"

    # [SE       se0      play=+61]
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
    # → next scene 1692
    jump sp90_scene_1692

label sp90_scene_1692:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # [EVENT_CG event    image=+177, level=80]
    $ dissolve_fx("id(177)")
    # まったく、もうっ！
    voice "sp90_s1692_003"
    l "Honestly, really!{#sp90_s1692_003}"

    # ……すいません。
    voice "sp90_s1692_004"
    s "…Sorry.{#sp90_s1692_004}"

    # 洗濯場で見たときはなにかと思ったわよ。サイトったら挙動不審そのもので。
    voice "sp90_s1692_005"
    l "When I saw you at the laundry, I wondered what was wrong with you. You were acting completely suspicious, Saito.{#sp90_s1692_005}"

    # ……す、すいません。
    voice "sp90_s1692_006"
    s "…S-Sorry.{#sp90_s1692_006}"

    # 突然、洗濯の手を止めてきょろきょろしはじめたかと思うと……そのあと……、まさか、あんなことをするなんて。
    voice "sp90_s1692_007"
    l "One moment you suddenly stop washing and start looking around furtively… and then… to think you'd go and do such a thing.{#sp90_s1692_007}"

    # そ、それ以上の説明は……や、やめて！ご主人様！
    voice "sp90_s1692_008"
    s "A-Any more explanation would… st-stop! Master!{#sp90_s1692_008}"


    menu:
        "W-Were you watching the whole time?!{#sp90_c_1692_1693}":
            jump sp90_scene_1693
        "Then don't make me wash them in the first place!{#sp90_c_1692_1694}":
            jump sp90_scene_1694
        "It's a dream! It's a dream! It's a dream!{#sp90_c_1692_1695}":
            jump sp90_scene_1695

label sp90_scene_1693:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+177, level=80]
    $ dissolve_fx("id(177)")
    # い、いつから覗いてたんですか！
    voice "sp90_s1693_002"
    s "S-Since when have you been watching?!{#sp90_s1693_002}"

    # の、覗いてたわけじゃないわ！
    voice "sp90_s1693_003"
    l "I-I wasn't peeping at you or anything!{#sp90_s1693_003}"

    # バカ犬がちゃんとお仕事してるな～～って、感心して見ていたら……、
    voice "sp90_s1693_004"
    l "I was watching admiringly, thinking 'look at the stupid dog, doing his job properly~'…{#sp90_s1693_004}"

    # 途中から、マタタビを手に入れた猫みたいになっちゃって！
    voice "sp90_s1693_005"
    l "But halfway through, you started acting like a cat that got hold of catnip!{#sp90_s1693_005}"

    # そ、そのまま見てることないだろ！
    voice "sp90_s1693_006"
    s "Y-You didn't have to just keep watching!{#sp90_s1693_006}"

    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # な、なによ！そういうことが言える立場なの！
    voice "sp90_s1693_008"
    l "W-What?! And what right do you have to say that?!{#sp90_s1693_008}"

    # ……うっ！
    voice "sp90_s1693_009"
    s "…Guh!{#sp90_s1693_009}"

    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # ほかの女の子にも教えてあげようかしら？気をつけないとダメよって……。
    voice "sp90_s1693_011"
    l "Should I tell the other girls too? That they'd better watch out…{#sp90_s1693_011}"

    # そ、それだけは……。
    voice "sp90_s1693_012"
    s "N-Not that, at least…{#sp90_s1693_012}"

    # 秘密にしておいて欲しいのかしら？
    voice "sp90_s1693_013"
    l "You want me to keep it a secret, do you?{#sp90_s1693_013}"

    # わ、わん！
    voice "sp90_s1693_014"
    s "W-Woof!{#sp90_s1693_014}"

    # あら、物分りがいいようね。
    voice "sp90_s1693_015"
    l "My, you're quick to understand.{#sp90_s1693_015}"

    # なら、ご主人様をもっと大切にしなさい。いいわね？
    voice "sp90_s1693_016"
    l "Then cherish your master even more. All right?{#sp90_s1693_016}"

    # わ、わん！わん！
    voice "sp90_s1693_017"
    s "W-Woof! Woof!{#sp90_s1693_017}"

    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # 大切にしないと……分かってるわね？
    voice "sp90_s1693_019"
    l "If you don't cherish her… you understand, don't you?{#sp90_s1693_019}"

    # （い、陰謀だぁっ！）[EVENT_CG event    image=+177, level=80]
    s "I-It's a conspiracy!{#sp90_s1693_020}"

    # ……ホントにもう……。バカなんだから。
    voice "sp90_s1693_021"
    l "…Really, honestly… You're such an idiot.{#sp90_s1693_021}"

    # → next scene 1696
    jump sp90_scene_1696

label sp90_scene_1694:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+177, level=80]
    $ dissolve_fx("id(177)")
    # だったら最初から洗わせるな！
    voice "sp90_s1694_002"
    s "Then don't make me wash them in the first place!{#sp90_s1694_002}"

    # ……ば、バカ犬があんな事するなんて想像もしてなかったわよ！
    voice "sp90_s1694_003"
    l "…I-I never imagined the stupid dog would do something like that!{#sp90_s1694_003}"

    # だ、大体あんな事して何が楽しいのよ！
    voice "sp90_s1694_004"
    l "B-Besides, what's fun about doing something like that?!{#sp90_s1694_004}"

    # べ、別に楽しいわけじゃないぞっ！
    voice "sp90_s1694_005"
    s "I-It's not like it's fun or anything!{#sp90_s1694_005}"

    # ……あ、あれはお約束というか礼儀みたいなもので……。
    voice "sp90_s1694_006"
    s "…I-It's more like a tradition, or a matter of courtesy…{#sp90_s1694_006}"

    # [EVENT_CG event    image=+178, level=80]
    $ dissolve_fx("id(178)")
    # ど、どこの礼儀よっ！
    voice "sp90_s1694_008"
    l "W-What kind of courtesy is that?!{#sp90_s1694_008}"

    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # ……そういうんだったら、他の女の子の前で同じ主張をさせてあげましょうか？
    voice "sp90_s1694_010"
    l "…In that case, should I let you make the same claim in front of the other girls?{#sp90_s1694_010}"

    # ……うっ。
    voice "sp90_s1694_011"
    s "…Ugh.{#sp90_s1694_011}"

    # そうね。キュルケやシエスタなら許してくれるかもしれないわね。
    voice "sp90_s1694_012"
    l "Yes. Kirche or Siesta might forgive you, don't you think?{#sp90_s1694_012}"

    # ……生暖かい目で。
    voice "sp90_s1694_013"
    l "…With lukewarm, forgiving eyes.{#sp90_s1694_013}"

    # ぐはっ。
    voice "sp90_s1694_014"
    s "Gah!{#sp90_s1694_014}"

    # ……ふふふ。もうご主人様に生意気な口をきいちゃダメよ。バカ犬？
    voice "sp90_s1694_015"
    l "…Heh heh heh. No more cheeky talk to your master, okay? Stupid dog?{#sp90_s1694_015}"

    # （……ちくしょう、俺か悪いんじゃない！あの悪魔の布キレが……俺をぉぉ……）[EVENT_CG event   
    s "…Damn it, I'm not the one at fault! That devilish scrap of cloth… it's getting the better of me…{#sp90_s1694_016}"

    # ホントにおバカなんだから……。
    voice "sp90_s1694_017"
    l "You really are such an idiot…{#sp90_s1694_017}"

    # → next scene 1696
    jump sp90_scene_1696

label sp90_scene_1695:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+177, level=80]
    $ dissolve_fx("id(177)")
    # 夢だ……。夢だ、夢だ、夢だ！あれは悪い夢だったんです！
    voice "sp90_s1695_002"
    s "It's a dream… A dream, a dream, a dream! It was a bad dream!{#sp90_s1695_002}"

    # ……へぇ、夢っていうのなら、誰に話しても全然問題ないわよね？
    voice "sp90_s1695_003"
    l "…Oh? If it was just a dream, then there's no problem telling anyone about it, is there?{#sp90_s1695_003}"

    # わ、忘れてください。お願いします。
    voice "sp90_s1695_004"
    s "F-Forget it. Please.{#sp90_s1695_004}"

    # [EVENT_CG event    image=+176, level=80]
    $ dissolve_fx("id(176)")
    # とっても、面白い夢だったのに……ねぇ？残念だわ。
    voice "sp90_s1695_006"
    l "It was such an interesting dream, though… Huh? What a shame.{#sp90_s1695_006}"

    # わ、わん。
    voice "sp90_s1695_007"
    s "W-Woof.{#sp90_s1695_007}"

    # まあ、バカ犬だからしょうがないわよねぇ。ああいうもの、犬は大好きだものね。
    voice "sp90_s1695_008"
    l "Well, you're a stupid dog, so it can't be helped. Dogs just love that sort of thing, don't they.{#sp90_s1695_008}"

    # わんわん！
    voice "sp90_s1695_009"
    s "Woof woof!{#sp90_s1695_009}"

    # [EVENT_CG event    image=+177, level=80]
    $ dissolve_fx("id(177)")
    # ……ホントに、調子がいいんだから。
    voice "sp90_s1695_011"
    l "…Really, you're feeling awfully full of yourself.{#sp90_s1695_011}"

    # → next scene 1696
    jump sp90_scene_1696

label sp90_scene_1696:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+177, level=80]
    $ dissolve_fx("id(177)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)

    return
