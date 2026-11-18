# Глава 19, часть 1 (сцены 739–749): утро операции, подземный ход.
# Источник: ps2_source/chapters/chapter_20_小悪魔と春風の協奏曲.txt (SCENE 739-749).

label ch19:
    $ tndl(None)
    $ show_sprites()

label ch19_1_scene_739:

    # [TITLE title("小悪魔と春風の協奏曲")]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：（ついに作戦開始の朝が来てしまった）
    s "(The morning of the operation has finally arrived.){#ch19_s_248}"

    # [SPRITE   lay5     hide]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1135, level=200]
    $ fade_fx("id(1135)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+82, level=200]
    $ fade_fx("id(82)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # コルベール：では、状況をまとめてみましょうか。  [voice 1134]
    voice "ch19_c_075"
    c "Well, let's go over the situation.{#ch19_c_075}"

    # コルベール：今回の最終目標は、ミス・ヴァリエールが、
    voice "ch19_c_076"
    c "Our final objective: Miss Valliere uses Void magic to eliminate the enemy…{#ch19_c_076}"

    # コルベール：ここまではよろしいですか？  [voice 1136]
    voice "ch19_c_077"
    c "Are we agreed so far?{#ch19_c_077}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：はい。  [voice 11917]
    voice "ch19_s_249"
    s "Yes.{#ch19_s_249}"

    # ルイズ：間違いはないです。  [voice 6449]
    voice "ch19_l_188"
    l "No mistakes.{#ch19_l_188}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：学内には敵兵が多数配置されてるはずです。
    voice "ch19_c_078"
    c "There should be many enemy soldiers inside the academy. And their commander Weatherly uses a special hypnosis magic.{#ch19_c_078}"

    # コルベール：この学院の生徒や教師までもが
    voice "ch19_c_079"
    c "There's a great risk that even the students and teachers here will become your enemies.{#ch19_c_079}"

    # コルベール：そのことについては気をつけるように。  [voice 1139]
    voice "ch19_c_080"
    c "Be careful of that.{#ch19_c_080}"

    # [SPRITE   lay9     x=-96, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：はい。  [voice 6450]
    voice "ch19_l_189"
    l "Yes.{#ch19_l_189}"

    # コルベール：ところで、ミス・ヴァリエール。  [voice 1140]
    voice "ch19_c_081"
    c "Now, Miss Valliere.{#ch19_c_081}"

    # ルイズ：はい。  [voice 6451]
    voice "ch19_l_190"
    l "Yes.{#ch19_l_190}"

    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # コルベール：今回使うという虚無の魔法。
    voice "ch19_c_082"
    c "This Void magic you'll use—what kind of magic is it, exactly?{#ch19_c_082}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……。  [voice 6452]
    voice "ch19_l_191"
    l "…{#ch19_l_191}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：わたしも魔法学院教師のはしくれだ。
    voice "ch19_c_083"
    c "I'm a teacher at the academy, after all. Even a hint of what magic you'll use could help me advise you.{#ch19_c_083}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：今、学院を占領してる艦がいる空に向かって
    voice "ch19_l_192"
    l "It's something aimed at the sky where the ship occupying the academy is.{#ch19_l_192}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：範囲は……そうですね、
    voice "ch19_l_193"
    l "The range… the wider the better, I suppose.{#ch19_l_193}"

    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # コルベール：ふむ、広範囲を狙う魔法か。
    voice "ch19_c_084"
    c "Hmm, a wide-area spell. And aimed at the sky, eh.{#ch19_c_084}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：すみません、ミスタ・コルベール。
    voice "ch19_l_194"
    l "Sorry, Mr. Colbert. I can't explain it in detail myself.{#ch19_l_194}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：いやいや、分かった。
    voice "ch19_c_085"
    c "No, no, I understand. I won't press you.{#ch19_c_085}"

    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # コルベール：だとすると、わたしはきみ達にかなり
    voice "ch19_c_086"
    c "In that case, I'll have to give you advice that's rather unfavorable to you.{#ch19_c_086}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そ、それはどういうことですか、
    voice "ch19_s_250"
    s "W-What do you mean, professor?{#ch19_s_250}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：もしもミス・ヴァリエールが空に向けて魔法を
    voice "ch19_c_087"
    c "If Miss Valliere casts a spell at the sky, the best place is the academy rooftop.{#ch19_c_087}"

    # コルベール：しかしながら、ウェザリーとアキナくんの爆破を
    voice "ch19_c_088"
    c "But if we're to stop Weatherly and Akina's bombing… we should settle the fight in the headmaster's office where they're barricaded.{#ch19_c_088}"

    # コルベール：虚無の魔法を使うより先、学院を爆破させられる
    voice "ch19_c_089"
    c "Before using Void, there's a risk the academy will be blown up. We need to draw their attention too.{#ch19_c_089}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：うっ……確かに。  [voice 11919]
    voice "ch19_s_251"
    s "Ugh… True.{#ch19_s_251}"

    menu:
        "Louise and I split up?{#ch19_1_c_739_1}":
            jump ch19_1_scene_740
        "If we can link up with Kirche and Tabitha{#ch19_1_c_739_2}":
            jump ch19_1_scene_741
        "Which should we do first?{#ch19_1_c_739_3}":
            jump ch19_1_scene_742

label ch19_1_scene_740:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+82, level=200]
    $ fade_fx("id(82)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：俺とルイズは、どうあっても別行動を
    voice "ch19_s_252"
    s "Louise and I have to act separately no matter what, don't we.{#ch19_s_252}"

    # [SPRITE   lay9     image=+933, level=160, dir=1A]
    # コルベール：酷な話ではあるが、それしか作戦を成功させる
    voice "ch19_c_090"
    c "It's a cruel thing to say, but there's no other way to make the plan work.{#ch19_c_090}"

    # サイト：はい。
    voice "ch19_s_253"
    s "Yes. There's no other way, so we'll do our best.{#ch19_s_253}"

    # → next scene 743
    jump ch19_1_scene_743

label ch19_1_scene_741:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+82, level=200]
    $ fade_fx("id(82)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：キュルケやタバサと合流できれば、
    voice "ch19_s_254"
    s "If we can link up with Kirche and Tabitha, somehow…{#ch19_s_254}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：確かに。
    voice "ch19_c_091"
    c "Indeed. We can only pray Miss Zerbst and Miss Tabitha haven't fallen into enemy hands.{#ch19_c_091}"

    # コルベール：きみ達が騒ぎを起こせば、彼女達は
    voice "ch19_c_092"
    c "If you two make a commotion, they'll surely try to join you.{#ch19_c_092}"

    # → next scene 743
    jump ch19_1_scene_743

label ch19_1_scene_742:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+82, level=200]
    $ fade_fx("id(82)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：一体、どちらを先にすればいいんだ……？  [voice 11923]
    voice "ch19_s_255"
    s "Which should we do first…?{#ch19_s_255}"

    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # コルベール：サイトくん、残念ながら……、
    voice "ch19_c_093"
    c "Saito-kun, I'm afraid doing one first is rather difficult here.{#ch19_c_093}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：つまり、俺とルイズは、別行動をとる必要が
    voice "ch19_s_256"
    s "So Louise and I need to split up, is that it?{#ch19_s_256}"

    # → next scene 743
    jump ch19_1_scene_743

label ch19_1_scene_743:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay9     image=+933, level=160, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+82, level=200]
    $ fade_fx("id(82)")
    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # コルベール：ああ……。
    voice "ch19_c_094"
    c "Ah… It's a plan full of holes, but even so, we have no choice but to do it.{#ch19_c_094}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：大丈夫です。
    voice "ch19_l_195"
    l "It's fine. We have the blessing of the First Founder Brimir.{#ch19_l_195}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：そうだね。
    voice "ch19_c_095"
    c "Yes. I can't help but feel uneasy sending you two on such a plan.{#ch19_c_095}"

    # コルベール：もはや君達を信じて託すしかない。  [voice 1155]
    voice "ch19_c_096"
    c "All I can do now is believe in you and leave it to you.{#ch19_c_096}"

    # コルベール：さて、それでは方針も確認できたところで、
    voice "ch19_c_097"
    c "Right, now that we've confirmed the plan—this map for you two.{#ch19_c_097}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：これって……２枚あるわね。
    voice "ch19_l_196"
    l "There are two… One is a map of the academy, but this one…{#ch19_l_196}"

    # コルベール：きみ達が中庭から通ってきた、地下道の地図だ。  [voice 1157]
    voice "ch19_c_098"
    c "It's the map of the underground passage you came through from the courtyard.{#ch19_c_098}"

    # コルベール：屋上への最短ルートに通じる出口は、
    voice "ch19_c_099"
    c "The exit leading to the shortest route to the rooftop is here.{#ch19_c_099}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そこで俺とルイズは、二手に分かれるって
    voice "ch19_s_257"
    s "So Saito and I split up here? Ah, but at this distance it's practically just around the corner.{#ch19_s_257}"

    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # コルベール：風は我々に吹いてる証だよ。
    voice "ch19_c_100"
    c "The wind is at our backs. Oh, there's one more thing I should give you.{#ch19_c_100}"

    # サイト：あ、これは……。  [voice 11926]
    voice "ch19_s_258"
    s "Ah, this is…{#ch19_s_258}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：そう、昨日見せた耳栓だ。
    voice "ch19_c_101"
    c "Yes, the earplugs I showed you yesterday. I gave you a rough explanation then, I think.{#ch19_c_101}"

    # コルベール：敵の中で最も厄介なのは、ウェザリーの
    voice "ch19_c_102"
    c "The most troublesome enemy is Weatherly's hypnosis magic.{#ch19_c_102}"

    # コルベール：でも、これを付けていれば大丈夫だ。  [voice 1162]
    voice "ch19_c_103"
    c "But with these, you'll be fine.{#ch19_c_103}"

    # コルベール：催眠魔法を受けた者と戦うことになっても、
    voice "ch19_c_104"
    c "Even if you fight someone under hypnosis, putting these on should temporarily restore their senses.{#ch19_c_104}"

    # サイト：分かりました。  [voice 11927]
    voice "ch19_s_259"
    s "Understood.{#ch19_s_259}"

    # コルベール：それでは行きたまえ。
    voice "ch19_c_105"
    c "Now go. Once I've confirmed you're outside, I'll make a little commotion outside myself.{#ch19_c_105}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # → next scene 744
    jump ch19_1_scene_744

label ch19_1_scene_744:

    # [BG       stage    image=+74, level=200]
    $ fade_fx("id(74)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # ルイズ：あーもう、なんでこの道は暗くて狭いのよ！
    voice "ch19_l_197"
    l "Ugh, why is this passage so dark and narrow! And it smells like mold!!{#ch19_l_197}"

    # サイト：しょうがないだろ、下水道なんだからさ。
    voice "ch19_s_260"
    s "What do you expect—it's a sewer. Instead of screaming, let's move.{#ch19_s_260}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：もう、この恨みは、何倍にもして
    voice "ch19_l_198"
    l "I'll take this grudge out on Weatherly and Akina a hundredfold!{#ch19_l_198}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：それなんだけどさ。
    voice "ch19_s_261"
    s "That's just it… Are we really okay with defeating those two?{#ch19_s_261}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：はぁ？
    voice "ch19_l_199"
    l "Hah? What nonsense are you talking. They're invaders!{#ch19_l_199}"

    menu:
        "Weatherly may be, but…{#ch19_1_c_744_1}":
            jump ch19_1_scene_745
        "Maybe they have circumstances{#ch19_1_c_744_2}":
            jump ch19_1_scene_746
        "Will Haruna ever come back?{#ch19_1_c_744_3}":
            jump ch19_1_scene_747

label ch19_1_scene_745:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+74, level=200]
    $ fade_fx("id(74)")
    # サイト：ウェザリーは、確かにそうかも
    voice "ch19_s_262"
    s "Weatherly may be, but…{#ch19_s_262}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：な、なによ。
    voice "ch19_l_200"
    l "What? You're being awfully hesitant.{#ch19_l_200}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：少なくとも、アキナはあくまでも春奈の頭の
    voice "ch19_s_263"
    s "At least Akina is just a personality implanted in Haruna's mind. Her body is Haruna's, isn't it?{#ch19_s_263}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：アキナを傷つけるということは、
    voice "ch19_s_264"
    s "Hurting Akina means hurting Haruna…{#ch19_s_264}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：そ、それは……そうだけど。  [voice 6462]
    voice "ch19_l_201"
    l "T-That's… Well, yes.{#ch19_l_201}"

    # → next scene 748
    jump ch19_1_scene_748

label ch19_1_scene_746:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+74, level=200]
    $ fade_fx("id(74)")
    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：彼女達にだって、やむにやまれぬ事情が
    voice "ch19_s_265"
    s "Maybe they have circumstances that forced them into this…{#ch19_s_265}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そんなこと言ったって、あいつらは
    voice "ch19_l_202"
    l "Even so, they're trying to kill everyone in this academy, you know?{#ch19_l_202}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：そうだよな……。  [voice 11934]
    voice "ch19_s_266"
    s "Yeah…{#ch19_s_266}"

    # → next scene 748
    jump ch19_1_scene_748

label ch19_1_scene_747:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+74, level=200]
    $ fade_fx("id(74)")
    # サイト：春奈は元に戻らないのかな……。  [voice 11935]
    voice "ch19_s_267"
    s "I wonder if Haruna will ever come back…{#ch19_s_267}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：それは、先生に任せるべきだわ。
    voice "ch19_l_203"
    l "That's something to leave to the professor. In the end, maybe he can do something.{#ch19_l_203}"

    # サイト：できないかもしれない。  [voice 11936]
    voice "ch19_s_268"
    s "Or maybe he can't.{#ch19_s_268}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……。  [voice 6465]
    voice "ch19_l_204"
    l "…{#ch19_l_204}"

    # → next scene 748
    jump ch19_1_scene_748

label ch19_1_scene_748:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+74, level=200]
    $ fade_fx("id(74)")
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：俺は、春奈を絶対に元に戻してあげたいんだ。
    voice "ch19_s_269"
    s "I want to restore Haruna no matter what. Even if, once she's back, she's tormented by what she did as Akina…{#ch19_s_269}"

    # サイト：それでも春奈は春奈に戻んなくちゃ
    voice "ch19_s_270"
    s "Even so, Haruna has to become Haruna again.{#ch19_s_270}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……。  [voice 6466]
    voice "ch19_l_205"
    l "…{#ch19_l_205}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：でも、ウェザリーにしか春奈を直すことが
    voice "ch19_s_271"
    s "But if only Weatherly can fix Haruna…{#ch19_s_271}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：それはすべてが終わってから考えましょ。
    voice "ch19_l_206"
    l "Let's think about that once it's all over. Now is not the time to hesitate.{#ch19_l_206}"

    # サイト：それは分かってる。
    voice "ch19_s_272"
    s "I know. I know it, but…{#ch19_s_272}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……。  [voice 6468]
    voice "ch19_l_207"
    l "…{#ch19_l_207}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [SPRITE   lay5     level=157]
    # [SPRITE   lay1     level=156]
    # [SPRITE   lay19    image=+940, level=153, dir=1A]
    # デルフリンガー：おいおい、お二人さん。
    voice "ch19_d_026"
    d "Hey, you two. Mind if I join the conversation? Someone's coming.{#ch19_d_026}"

    # [SPRITE   lay1     image=+339, level=153, dir=2A]
    # [SPRITE   lay5     level=157]
    # [SPRITE   lay1     level=153]
    # [SPRITE   lay19    level=154]
    # ルイズ：えっ……。  [voice 6469]
    voice "ch19_l_208"
    l "Eh…?{#ch19_l_208}"

    # [SPRITE   lay5     level=157]
    # [SPRITE   lay1     level=154]
    # [SPRITE   lay19    image=+942, level=153, dir=1A]
    # デルフリンガー：足音は二つか。  [voice 1328]
    voice "ch19_d_027"
    d "Two sets of footsteps.{#ch19_d_027}"

    # [SPRITE   lay5     image=+405, level=153, dir=1B]
    # [SPRITE   lay5     level=153]
    # [SPRITE   lay1     level=155]
    # [SPRITE   lay19    level=154]
    # サイト：敵、か？  [voice 11941]
    voice "ch19_s_273"
    s "Enemies?{#ch19_s_273}"

    # [SPRITE   lay5     level=154]
    # [SPRITE   lay1     level=155]
    # [SPRITE   lay19    image=+940, level=153, dir=1A]
    # デルフリンガー：どうする相棒、こっちから打って出るか？  [voice 1329]
    voice "ch19_d_028"
    d "What'll you do, partner? Go out and meet them?{#ch19_d_028}"

    # [SPRITE   lay5     image=+401, level=153, dir=1B]
    # [SPRITE   lay1     level=155]
    # [SPRITE   lay19    level=154]
    # サイト：いや、味方かもしれない。
    voice "ch19_s_274"
    s "No, they could be allies. Let's see who it is first.{#ch19_s_274}"

    # [SPRITE   lay5     level=154]
    # [SPRITE   lay1     level=155]
    # [SPRITE   lay19    image=+944, level=153, dir=1A]
    # デルフリンガー：くるぜ、相棒……あれだっ！  [voice 1330]
    voice "ch19_d_029"
    d "They're coming, partner… That's it!{#ch19_d_029}"

    # [SPRITE   lay5     image=+405, level=153, dir=1B]
    # [SPRITE   lay1     level=155]
    # [SPRITE   lay19    level=154]
    # サイト：誰だっ！
    voice "ch19_s_275"
    s "Who's there!? Huh? It's Kirche and Tabitha.{#ch19_s_275}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay19    hide]
    # [LAYER    lay0     image=+658, level=157, dir=3A]
    # [SPRITE   lay6     image=+746, level=156, dir=3A]
    # キュルケ：……。
    k "…{#ch19_k_034}"

    # タバサ：……。
    t "…{#ch19_t_024}"

    # デルフリンガー：近づくな相棒！
    voice "ch19_d_030"
    d "Don't come closer, partner! Something's off about them.{#ch19_d_030}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+308, level=155, dir=1A]
    # [SPRITE   lay5     image=+405, level=153, dir=1B]
    # ルイズ：な、なっ……まさかっ！  [voice 6470]
    voice "ch19_l_209"
    l "N-No… It can't be!{#ch19_l_209}"

    # [SPRITE   lay5     image=+471, level=153, dir=3B]
    # [SE       se0      play=+65]
    # サイト：くそっ。
    voice "ch19_s_276"
    s "Damn. I can't hold back, then!{#ch19_s_276}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay19    hide]
    # [BG       stage    hide]
    # → next scene 749
    jump ch19_1_scene_749

label ch19_1_scene_749:

    # [BG       stage    image=+74, level=200]
    $ fade_fx("id(74)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ふぅ。
    voice "ch19_l_210"
    l "Phew. That's done.{#ch19_l_210}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あ、あら？
    voice "ch19_k_035"
    k "O-Oh? Why are you here, Louise? And where are we?{#ch19_k_035}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：地下道。  [voice 15603]
    voice "ch19_t_025"
    t "The underground passage.{#ch19_t_025}"

    # [LAYER    lay0     level=155]
    # [SPRITE   lay19    image=+946, level=153, dir=1A]
    # [SPRITE   lay6     level=154]
    # デルフリンガー：やれやれ、ようやく正気に戻ったのかよ、
    voice "ch19_d_031"
    d "Well, well. You're back to your senses at last, eh?{#ch19_d_031}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay6     image=+680, level=154, dir=1A]
    # キュルケ：説明してちょうだい、ダーリン。
    voice "ch19_k_036"
    k "Explain, darling. What's going on?{#ch19_k_036}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # サイト：その前に確認しておきたいんだけど。
    voice "ch19_s_277"
    s "First, let me check. Kirche, what's the last thing you remember?{#ch19_s_277}"

    # [SPRITE   lay6     image=+676, level=154, dir=1A]
    # キュルケ：えーと、実はあらかた中庭の敵を排除
    voice "ch19_k_037"
    k "Um. Well, after clearing most of the courtyard enemies, we stormed the headmaster's office where Weatherly and Akina were.{#ch19_k_037}"

    # キュルケ：そこで、ウェザリーと対面して……、  [voice 3331]
    voice "ch19_k_038"
    k "There, I came face to face with Weatherly…{#ch19_k_038}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+594, level=155, dir=1A]
    # タバサ：返り討ち。  [voice 15604]
    voice "ch19_t_026"
    t "Routed.{#ch19_t_026}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+682, level=154, dir=1A]
    # キュルケ：確かに、そこから先の記憶がないわね。  [voice 3332]
    voice "ch19_k_039"
    k "Indeed, I have no memory after that.{#ch19_k_039}"

    # キュルケ：それより、ダーリン。
    voice "ch19_k_040"
    k "More importantly, darling—why am I wearing earplugs?{#ch19_k_040}"

    # サイト：いや、それがだなぁ……。  [voice 11946]
    voice "ch19_s_278"
    s "Well, that's the thing…{#ch19_s_278}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+74, level=200]
    $ fade_fx("id(74)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # [SPRITE   lay6     image=+682, level=154, dir=1A]
    # [SPRITE   lay6     image=+680, level=154, dir=1A]
    # キュルケ：やっぱりね。
    voice "ch19_k_041"
    k "I thought so. Tabitha said as much—that there was such a countermeasure.{#ch19_k_041}"

    # [SPRITE   lay5     image=+401, level=157, dir=1B]
    # サイト：ところで、２人は俺達の計画に
    voice "ch19_s_279"
    s "By the way, you two do agree with our plan, don't you?{#ch19_s_279}"

    # [SPRITE   lay6     image=+676, level=154, dir=1A]
    # キュルケ：ことわる理由がないわね。  [voice 3335]
    voice "ch19_k_042"
    k "No reason to refuse.{#ch19_k_042}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+588, level=155, dir=1A]
    # タバサ：右に同じ。  [voice 15605]
    voice "ch19_t_027"
    t "Same here.{#ch19_t_027}"

    # サイト：ありがとう。  [voice 11948]
    voice "ch19_s_280"
    s "Thanks.{#ch19_s_280}"

    # サイト：正直２人が見つからなかったら
    voice "ch19_s_281"
    s "Honestly, I was worried about what we'd do if we couldn't find you two. I'm glad we have more allies.{#ch19_s_281}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+676, level=154, dir=1A]
    # キュルケ：確かに二手に分かれて行動するしか
    voice "ch19_k_043"
    k "We really have no choice but to split into two groups.{#ch19_k_043}"

    # キュルケ：屋上から学院長室への移動は
    voice "ch19_k_044"
    k "Going from the rooftop to the headmaster's office takes too long.{#ch19_k_044}"

    # キュルケ：ダーリン。
    voice "ch19_k_045"
    k "Darling, how will you divide the groups?{#ch19_k_045}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+335, level=156, dir=2A]
    # ルイズ：なんで、わたしに聞かないのよ。  [voice 6472]
    voice "ch19_l_211"
    l "Why aren't you asking me?{#ch19_l_211}"

    # [SPRITE   lay6     image=+678, level=154, dir=1A]
    # キュルケ：あら？
    voice "ch19_k_046"
    k "Oh? Can Louise decide?{#ch19_k_046}"

    # [SPRITE   lay1     image=+306, level=156, dir=1A]
    # ルイズ：なんですってー！  [voice 6473]
    voice "ch19_l_212"
    l "What was that—!{#ch19_l_212}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+405, level=157, dir=1B]
    # サイト：もうケンカはやめろよ。  [voice 11950]
    voice "ch19_s_282"
    s "Come on, stop fighting.{#ch19_s_282}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+627, level=155, dir=2A]
    # タバサ：……。
    t "…{#ch19_t_028}"

    # [SPRITE   lay5     image=+440, level=157, dir=2B]
    # サイト：うん？
    voice "ch19_s_283"
    s "Hm? What is it, Tabitha?{#ch19_s_283}"

    # [LAYER    lay0     image=+588, level=155, dir=1A]
    # タバサ：キュルケとルイズ。  [voice 15606]
    voice "ch19_t_029"
    t "Kirche and Louise.{#ch19_t_029}"

    # タバサ：わたしとサイト。  [voice 15607]
    voice "ch19_t_030"
    t "Me and Saito.{#ch19_t_030}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+715, level=154, dir=2A]
    # キュルケ：ルイズと？
    voice "ch19_k_047"
    k "With Louise? Well, if Tabitha says so, I suppose it can't be helped. She must have a reason…{#ch19_k_047}"

    # タバサ：うん。  [voice 15608]
    voice "ch19_t_031"
    t "Mm.{#ch19_t_031}"

    # [SPRITE   lay6     image=+676, level=154, dir=1A]
    # キュルケ：というわけだから。
    voice "ch19_k_048"
    k "So that's how it is. Louise, I'll go with you.{#ch19_k_048}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+335, level=156, dir=2A]
    # ルイズ：しょうがないわね。
    voice "ch19_l_213"
    l "Fine. If you insist, I'll go with Kirche.{#ch19_l_213}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+588, level=155, dir=1A]
    # [SPRITE   lay5     image=+401, level=157, dir=1B]
    # サイト：タバサ、よろしく頼むな。  [voice 11952]
    voice "ch19_s_284"
    s "Tabitha, I'm counting on you.{#ch19_s_284}"

    # タバサ：お願い。  [voice 15609]
    voice "ch19_t_032"
    t "Please.{#ch19_t_032}"

    # [SPRITE   lay5     image=+436, level=157, dir=2B]
    # サイト：うん、タバサが一緒なら俺も心強いよ。  [voice 11953]
    voice "ch19_s_285"
    s "Yeah. With Tabitha, I feel better.{#ch19_s_285}"

    # タバサ：ありがとう。  [voice 15610]
    voice "ch19_t_033"
    t "Thank you.{#ch19_t_033}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 750
    jump ch19_2

    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch19_2
    return

