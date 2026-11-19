# Глава 17, часть 2 (сцены 684–695): просьба королевы, канун побега.
# Источник: ps2_source/chapters/chapter_18_女王の決断.txt (SCENE 684-695).

label ch17_2:
    $ tndl(None)
    $ show_sprites()

label ch17_2_scene_684:

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # アンリエッタ：ルイズと使い魔さんには、
    voice "ch17_h_023"
    h "I have a special request for Louise and her familiar. That's why I called you to the castle.{#ch17_h_023}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：姫さま……？  [voice 6290]
    voice "ch17_l_029"
    l "Princess…?{#ch17_l_029}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay8     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 685
    jump ch17_2_scene_685

label ch17_2_scene_685:

    # [EVENT_CG event    image=+207, level=80]
    $ dissolve_fx("id(207)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # アンリエッタ：ルイズ……これはお友達としてではなく、
    voice "ch17_h_024"
    h "Louise… This isn't as a friend, but as the Queen of Tristain that I ask. Is that all right?{#ch17_h_024}"

    # ルイズ：も、もちろんです！
    voice "ch17_l_030"
    l "O-Of course! Anything you command.{#ch17_l_030}"

    # アンリエッタ：ルイズ、今の軍議を見てもらえれば分かるとは
    voice "ch17_h_025"
    h "Louise, as you saw in the council, Tristain is in a critical situation.{#ch17_h_025}"

    # ルイズ：はい。  [voice 6292]
    voice "ch17_l_031"
    l "Yes.{#ch17_l_031}"

    # アンリエッタ：ですが……ルイズ。
    voice "ch17_h_026"
    h "But… Louise. With your power and your familiar's…{#ch17_h_026}"

    # ルイズ：わたしの……。
    voice "ch17_l_032"
    l "My… Void power, you mean.{#ch17_l_032}"

    # アンリエッタ：そして、使い魔さん……。
    voice "ch17_h_027"
    h "And you, familiar… I ask you too.{#ch17_h_027}"

    # サイト：あ、はい……。  [voice 11740]
    voice "ch17_s_044"
    s "O-Okay…{#ch17_s_044}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # アンリエッタ：使い魔さん……。  [voice 607]
    voice "ch17_h_028"
    h "Familiar…{#ch17_h_028}"

    # アンリエッタ：あなたが持つガンダールヴの力は、
    voice "ch17_h_029"
    h "I hear the power of Gandalf you wield is meant to protect your contract's mistress during spellcasting.{#ch17_h_029}"

    # アンリエッタ：ルイズと使い魔さんの力、
    voice "ch17_h_030"
    h "Could you lend Louise's and your power to me?{#ch17_h_030}"

    # [SPRITE   lay1     hide]
    # ルイズ：姫、さま……。  [voice 6294]
    voice "ch17_l_033"
    l "Pri-ness…{#ch17_l_033}"

    # アンリエッタ：ルイズ……わたくしはあなたを、この世で
    voice "ch17_h_031"
    h "Louise… I think of you as my only precious friend in this world. But…{#ch17_h_031}"

    # アンリエッタ：許してください。
    voice "ch17_h_032"
    h "Forgive me. For sending you, my dear friend, to the battlefield as a tool of war.{#ch17_h_032}"

    # ルイズ：……。  [voice 6295]
    voice "ch17_l_034"
    l "…{#ch17_l_034}"

    menu:
        "Louise, is that okay?{#ch17_2_c_685_1}":
            jump ch17_2_scene_686
        "It's fine, Princess{#ch17_2_c_685_2}":
            jump ch17_2_scene_687
        "Are we really going to be okay?{#ch17_2_c_685_3}":
            jump ch17_2_scene_688

label ch17_2_scene_686:

    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [EVENT_CG event    image=+207, level=80]
    $ dissolve_fx("id(207)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     hide]
    # [EVENT_CG event    hide]
    # [SPRITE   lay8     hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ルイズ、それでいいのか？  [voice 11741]
    voice "ch17_s_045"
    s "Louise, is that okay?{#ch17_s_045}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：何言ってんのよサイト。
    voice "ch17_l_035"
    l "What are you saying, Saito? The Princess is counting on us. Of course we'll do it.{#ch17_l_035}"

    # ルイズ：姫さまがここまでおっしゃってるのに、
    voice "ch17_l_036"
    l "Even after she said all that, you won't respond?{#ch17_l_036}"

    # → next scene 689
    jump ch17_2_scene_689

label ch17_2_scene_687:

    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [EVENT_CG event    image=+207, level=80]
    $ dissolve_fx("id(207)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     hide]
    # [EVENT_CG event    hide]
    # [SPRITE   lay8     hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：大丈夫ですよ、お姫さま。  [voice 11742]
    voice "ch17_s_046"
    s "It's fine, Princess.{#ch17_s_046}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：サイト！？  [voice 6298]
    voice "ch17_l_037"
    l "Saito!?{#ch17_l_037}"

    # サイト：こんなご主人様だけど……。
    voice "ch17_s_047"
    s "Even with such a mistress… It seems my role is to protect you, no matter what.{#ch17_s_047}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：だ、誰が『こんな』なのよっ！  [voice 6299]
    voice "ch17_l_038"
    l "Who are you calling 'such'!{#ch17_l_038}"

    # → next scene 689
    jump ch17_2_scene_689

label ch17_2_scene_688:

    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [EVENT_CG event    image=+207, level=80]
    $ dissolve_fx("id(207)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     hide]
    # [EVENT_CG event    hide]
    # [SPRITE   lay8     hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：お、俺達で大丈夫かな？  [voice 11744]
    voice "ch17_s_048"
    s "Are we really going to be okay?{#ch17_s_048}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：あ、あんたがそんなんでどうするのよ？
    voice "ch17_l_039"
    l "What's wrong with you? I'm the wielder of Void, and you're my familiar.{#ch17_l_039}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：姫さまがここまでおっしゃってるのに、
    voice "ch17_l_040"
    l "Even after she said all that, you won't respond?{#ch17_l_040}"

    # → next scene 689
    jump ch17_2_scene_689

label ch17_2_scene_689:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そんなこと言ってもなあ、
    voice "ch17_s_049"
    s "Even so, it's not easy for us either.{#ch17_s_049}"

    # サイト：うちのご主人様ときたら、
    voice "ch17_s_050"
    s "My mistress bursts into tears at the slightest thing.{#ch17_s_050}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：虚無の魔法使いとかいっても、
    voice "ch17_s_051"
    s "And even if you call her a Void mage, she runs out of mental energy instantly.{#ch17_s_051}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：……。  [voice 6302]
    voice "ch17_l_041"
    l "…{#ch17_l_041}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：炊事洗濯がまるで駄目なうえに、
    voice "ch17_s_052"
    s "She can't cook or clean at all, and she's hopeless at everyday magic.{#ch17_s_052}"

    # サイト：そのくせ食べることだけが一人前と
    voice "ch17_s_053"
    s "And yet she's only a prodigy when it comes to eating…{#ch17_s_053}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：サ～～～イ～～～～～トぉ～～～～～！  [voice 6303]
    voice "ch17_l_042"
    l "SAAAI TOOOO!{#ch17_l_042}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SE       se0      play=+61]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay8     vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay8     hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay1     reset]
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # サイト：ぎゃーすっ！  [voice 11750]
    voice "ch17_s_054"
    s "Gyah!{#ch17_s_054}"

    # ルイズ：こともあろうに姫さまの御前でぇっ！
    voice "ch17_l_043"
    l "In front of the Princess, too! How could you!?{#ch17_l_043}"

    # アンリエッタ：ふふっ……くすくす……。  [voice 612]
    voice "ch17_h_033"
    h "Fufu… hehe…{#ch17_h_033}"

    # ルイズ：……？  [voice 6305]
    voice "ch17_l_044"
    l "…?{#ch17_l_044}"

    # アンリエッタ：ふふふっ……安心しました。
    voice "ch17_h_034"
    h "Fufufu… I'm relieved. If you two are this close… Surely, it'll be all right.{#ch17_h_034}"

    # [EVENT_CG event    image=+214, level=80]
    $ dissolve_fx("id(214)")
    # ルイズ：あう……。  [voice 6306]
    voice "ch17_l_045"
    l "Ugh…{#ch17_l_045}"

    # アンリエッタ：ルイズ、使い魔さん。
    voice "ch17_h_035"
    h "Louise, familiar. The future of this country… I entrust it to you.{#ch17_h_035}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # → next scene 690
    jump ch17_2_scene_690

label ch17_2_scene_690:

    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # サイト：（お姫さまの依頼を聞き届けることになった
    s "(Having accepted the Princess's request, Louise and I hurried back to the academy.){#ch17_s_055}"

    # サイト：（空中艦隊を相手にするには、
    s "(To fight the aerial fleet, we need the Zero Fighter—but it's at the academy now.){#ch17_s_056}"

    # サイト：（ただし、学院に戻るためには、
    s "(But to get back to the academy, we have to slip through the enemy's net of cannons.){#ch17_s_057}"

    # サイト：（さすがにずっと砲撃していられるほど、
    s "(Surely they don't have enough ammo to keep shelling forever.){#ch17_s_058}"

    # サイト：（その隙ができるであろう
    s "(We decided to escape at dawn, when there'd be a gap.){#ch17_s_059}"

    # サイト：（まずは明日の脱出行にそなえて、
    s "(First, let's rest up for tomorrow's escape…){#ch17_s_060}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+70, level=200]
    $ fade_fx("id(70)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+82]
    # ルイズ：サイト……。
    voice "ch17_l_046"
    l "Saito… Are you there?{#ch17_l_046}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ルイズか？  [voice 11751]
    voice "ch17_s_061"
    s "Louise?{#ch17_s_061}"

    # ルイズ：入るわね。  [voice 6308]
    voice "ch17_l_047"
    l "I'm coming in.{#ch17_l_047}"

    # [SE       se0      play=+57]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # サイト：どうしたんだルイズ。
    voice "ch17_s_062"
    s "What is it, Louise? You're acting so formal.{#ch17_s_062}"

    # ルイズ：サイト、明日、夜明けと同時に出発よね。  [voice 6309]
    voice "ch17_l_048"
    l "Saito, we leave at dawn tomorrow, right?{#ch17_l_048}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ああ、さっき兵士に聞いたよ。
    voice "ch17_s_063"
    s "Yeah, I heard from a soldier. We break through the encirclement, head to the academy, then fly the Zero Fighter. That's the plan, right?{#ch17_s_063}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なぁ……ルイズ。  [voice 11754]
    voice "ch17_s_064"
    s "Say… Louise.{#ch17_s_064}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：なによ？  [voice 6310]
    voice "ch17_l_049"
    l "What?{#ch17_l_049}"

    menu:
        "What's happening to the academy?{#ch17_2_c_690_1}":
            jump ch17_2_scene_691
        "Don't get captured by the enemy{#ch17_2_c_690_2}":
            jump ch17_2_scene_692
        "Are you really going to use Void?{#ch17_2_c_690_3}":
            jump ch17_2_scene_693

label ch17_2_scene_691:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+70, level=200]
    $ fade_fx("id(70)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：学院はどうなってるんだろう？  [voice 11755]
    voice "ch17_s_065"
    s "What's happening to the academy?{#ch17_s_065}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：そんなこと、わたしに聞かないでよ。
    voice "ch17_l_050"
    l "Don't ask me. You were with Saito the whole time. How would I know? {#ch17_l_050}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：い、いやそれは分かってるんだけどさ。
    voice "ch17_s_066"
    s "N-No, I know that. I just… can't stop worrying.{#ch17_s_066}"

    # サイト：それにルイズだって気にならないわけ
    voice "ch17_s_067"
    s "And you're worried too, aren't you, Louise?{#ch17_s_067}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：そりゃ、そうだけどさ……。  [voice 6312]
    voice "ch17_l_051"
    l "Well, yes, but…{#ch17_l_051}"

    # → next scene 694
    jump ch17_2_scene_694

label ch17_2_scene_692:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+70, level=200]
    $ fade_fx("id(70)")
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：敵に捕まったりするんじゃないぞ。  [voice 11758]
    voice "ch17_s_068"
    s "Don't get captured by the enemy.{#ch17_s_068}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：な……！
    voice "ch17_l_052"
    l "Wha—! What is this familiar saying to his mistress!?{#ch17_l_052}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：だっておまえ、魔法が使えるったって、
    voice "ch17_s_069"
    s "Even if you can use magic, they outnumber you.{#ch17_s_069}"

    # サイト：虚無の魔法もいいけど、使う場面が来る前に
    voice "ch17_s_070"
    s "Void magic is fine, but if it's all over before you even get to use it, there's no help for it.{#ch17_s_070}"

    # → next scene 694
    jump ch17_2_scene_694

label ch17_2_scene_693:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+70, level=200]
    $ fade_fx("id(70)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：おまえ……。
    voice "ch17_s_071"
    s "You… Are you really going to use Void magic?{#ch17_s_071}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：なに言ってんのよ。
    voice "ch17_l_053"
    l "What are you saying? Of course.{#ch17_l_053}"

    # ルイズ：虚無の力を使わないと、トリステインへの
    voice "ch17_l_054"
    l "Unless we use Void, we can't stop the invasion of Tristain.{#ch17_l_054}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：だよ、な。
    voice "ch17_s_072"
    s "Right. Against the enemy fleet, my Zero Fighter alone won't be enough.{#ch17_s_072}"

    # → next scene 694
    jump ch17_2_scene_694

label ch17_2_scene_694:

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+70, level=200]
    $ fade_fx("id(70)")
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：いちいちうるさいわね。
    voice "ch17_l_055"
    l "You're so annoying. I'm a noble.{#ch17_l_055}"

    # ルイズ：貴族は国と誇りを守るために、
    voice "ch17_l_056"
    l "Nobles have a duty to fight to defend their country and their pride!{#ch17_l_056}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：貴族の義務、か……。
    voice "ch17_s_073"
    s "Duty of a noble, huh… But if you die, there's no honor or pride left.{#ch17_s_073}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……！  [voice 6318]
    voice "ch17_l_057"
    l "…!{#ch17_l_057}"

    # サイト：なぁルイズ、俺はさ……。  [voice 11764]
    voice "ch17_s_074"
    s "Say, Louise, I…{#ch17_s_074}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：今わたしとあんたがしなくちゃならないのは、
    voice "ch17_l_058"
    l "What we have to do now is one: get back to the academy at any cost. Two: fight to defend this city.{#ch17_l_058}"

    # ルイズ：今はそれだけ考えればいいの。
    voice "ch17_l_059"
    l "That's all you need to think about. As my familiar, follow your mistress.{#ch17_l_059}"

    # サイト：ルイズ……。  [voice 11765]
    voice "ch17_s_075"
    s "Louise…{#ch17_s_075}"

    # ルイズ：おやすみ。
    voice "ch17_l_060"
    l "Good night. Sleep well today.{#ch17_l_060}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     x=64, y=0]
    # [SE       se0      play=+57]
    # [SE       se0      play=+56]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：なんだよ、ちくしょう。  [voice 11766]
    voice "ch17_s_076"
    s "What the hell…{#ch17_s_076}"

    # サイト：貴族だからって、ほいほい命を
    voice "ch17_s_077"
    s "Just because you're a noble, you shouldn't throw your life away so easily…{#ch17_s_077}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：……。  [voice 11768]
    voice "ch17_s_078"
    s "…{#ch17_s_078}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ま、今はあれこれ悩んでもしょうがないか。
    voice "ch17_s_079"
    s "Well, worrying won't help. Let's sleep…{#ch17_s_079}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 695
    jump ch17_2_scene_695

label ch17_2_scene_695:

    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：（……だめだ、眠れない）
    s "(No… I can't sleep.){#ch17_s_080}"

    # サイト：（しょうがない、ちょっとその辺をうろうろ
    s "(I guess I'll wander around a bit…){#ch17_s_081}"

    # サイト：（外じゃ、まだ戦闘が続いているみたいだけど、
    s "(The fighting is still going on outside, but it shouldn't reach here yet. Probably…){#ch17_s_082}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ГЛАВЫ 17 ====
    jump ch18
    return

