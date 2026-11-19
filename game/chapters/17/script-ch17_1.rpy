# Глава 17, часть 1 (сцены 670–683): «女王の決断» — напряжение, совет.
# Источник: ps2_source/chapters/chapter_18_女王の決断.txt (SCENE 670-683).

label ch17:
    $ tndl(None)
    $ show_sprites()

label ch17_1_scene_670:

    # [TITLE title("女王の決断")]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # サイト：（演劇が終わってから、かれこれ数日。
    s "(A few days since the play ended. No leads on the bomb-thrower, only time passing…){#ch17_s_001}"

    # サイト：（一度、みんなそろって魔法学院に
    s "(We all went back to the academy once, but…){#ch17_s_002}"

    # サイト：（結果らしい結果をだせなかったことと、
    s "(No real results, and we still don't know who the bomb-thrower is—everyone's on edge…){#ch17_s_003}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1133, level=200]
    $ fade_fx("id(1133)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+23, level=200]
    $ fade_fx("id(23)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：もう一度言ってみなさいよ、キュルケ？  [voice 6259]
    voice "ch17_l_001"
    l "Say that again, Kirche?{#ch17_l_001}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：あら、ヴァリエールの御令嬢はおつむばかりか
    voice "ch17_k_001"
    k "Oh, is the young lady of Valliere hard of hearing as well as empty-headed? Well, darling, what do you think?{#ch17_k_001}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+431, level=160, dir=2A]
    # サイト：いや……。
    voice "ch17_s_004"
    s "Well… I mean…{#ch17_s_004}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ど、どさくさにまぎれてサイトに
    voice "ch17_l_002"
    l "Stop clinging to Saito in the confusion!{#ch17_l_002}"

    # サイト：（と、まあこうなってるわけだ。
    s "(So that's how things stand. Oh well.){#ch17_s_005}"

    menu:
        "Louise, cut it out{#ch17_1_c_670_1}":
            jump ch17_1_scene_671
        "Kirche, that's a bit much…{#ch17_1_c_670_2}":
            jump ch17_1_scene_672
        "Tabitha, stop them{#ch17_1_c_670_3}":
            jump ch17_1_scene_673

label ch17_1_scene_671:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+23, level=200]
    $ fade_fx("id(23)")
    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ルイズ、いい加減にしろよ。
    voice "ch17_s_006"
    s "Louise, cut it out. I understand you're irritated, but calm down, okay?{#ch17_s_006}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：ちょっと、サイト！
    voice "ch17_l_003"
    l "Saito! What kind of language is that to use with your mistress?{#ch17_l_003}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：もう一度使い魔の立場について、
    voice "ch17_l_004"
    l "I think we need to re-educate you on your place as a familiar!?{#ch17_l_004}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：お、俺に八つ当たりすんなって！  [voice 11707]
    voice "ch17_s_007"
    s "Hey, don't take it out on me!{#ch17_s_007}"

    # → next scene 674
    jump ch17_1_scene_674

label ch17_1_scene_672:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+23, level=200]
    $ fade_fx("id(23)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：なあ、キュルケ。
    voice "ch17_s_008"
    s "Kirche, that's a bit much…{#ch17_s_008}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+713, level=160, dir=2A]
    # キュルケ：ダーリンは黙ってて！
    voice "ch17_k_002"
    k "You stay out of it, darling! This is between me and Louise.{#ch17_k_002}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そ、それは失礼しました……。  [voice 11709]
    voice "ch17_s_009"
    s "O-My apologies…{#ch17_s_009}"

    # → next scene 674
    jump ch17_1_scene_674

label ch17_1_scene_673:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+23, level=200]
    $ fade_fx("id(23)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：タバサ、２人を止めてくれよ。  [voice 11710]
    voice "ch17_s_010"
    s "Tabitha, stop them, please.{#ch17_s_010}"

    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：ストレス発散。  [voice 15583]
    voice "ch17_t_001"
    t "Stress relief.{#ch17_t_001}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そういわれると、そうかもしれないけどさ。
    voice "ch17_s_011"
    s "Well, maybe… but don't you think there's a better way?{#ch17_s_011}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch17_t_002}"

    # → next scene 674
    jump ch17_1_scene_674

label ch17_1_scene_674:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+23, level=200]
    $ fade_fx("id(23)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     x=144, y=416]
    # [LAYER    lay0     x=304, y=416]
    # [SPRITE   lay1     image=+340, level=140, dir=2A]
    # ルイズ：サイト！  [voice 6263]
    voice "ch17_l_005"
    l "Saito!{#ch17_l_005}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：は、はいぃ！  [voice 11712]
    voice "ch17_s_012"
    s "Y-Yes!{#ch17_s_012}"

    # ルイズ：何、ぼーっとしてるのよ。
    voice "ch17_l_006"
    l "What are you spacing out for? Cleaning and laundry! And you haven't made the bed yet, have you?{#ch17_l_006}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：あら、ダーリンはあたしと一緒に
    voice "ch17_k_003"
    k "Oh, darling is going out with me. Overworking is bad for the body.{#ch17_k_003}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：誰がそんなこと許したのよ！  [voice 6265]
    voice "ch17_l_007"
    l "Who gave you permission!{#ch17_l_007}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：もちろん、あたし。  [voice 3295]
    voice "ch17_k_004"
    k "Why, me, of course.{#ch17_k_004}"

    # ルイズ：キュルケは、サイトのご主人様じゃない
    voice "ch17_l_008"
    l "You're not Saito's mistress, are you!{#ch17_l_008}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：あら、サイトはあたしのダーリンなんだから、
    voice "ch17_k_005"
    k "Oh, but he's my darling, so it's much the same thing.{#ch17_k_005}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：全っ然似てないっ！
    voice "ch17_l_009"
    l "It's nothing like it! It makes no sense!{#ch17_l_009}"

    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：うふふ、まあ、あなたには分からないこと
    voice "ch17_k_006"
    k "Ufufu. Well, there are things you just don't understand, my dear. The complicated relationship between a man and a woman.{#ch17_k_006}"

    # ルイズ：なんですってぇ！？  [voice 6268]
    voice "ch17_l_010"
    l "What was that!?{#ch17_l_010}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：（このままいたら、俺は間違いなく２人の戦いに
    s "(If I stay, I'll definitely get dragged into their fight…){#ch17_s_013}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：あ、俺、ゼロ戦のことで、コルベール先生に
    voice "ch17_s_014"
    s "Ah, I remember—Colbert-sen called me about the Zero Fighter. See you!{#ch17_s_014}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：ちょ、ちょっとサイト？  [voice 6269]
    voice "ch17_l_011"
    l "W-Wait, Saito?{#ch17_l_011}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：ダーリンっ？  [voice 3298]
    voice "ch17_k_007"
    k "Darling?{#ch17_k_007}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：敵前逃亡。  [voice 15584]
    voice "ch17_t_003"
    t "Desertion under fire.{#ch17_t_003}"

    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # サイト：（ふぅ……。
    s "(Phew… I wasn't actually called by Colbert-sen…){#ch17_s_015}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（ほとぼりが冷めるまで、
    s "(I'll ask him to hide me until things cool down…){#ch17_s_016}"

    # [SE       se0      play=+82]
    # [SE       se0      play=+57]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：おや、サイトくん。
    voice "ch17_c_001"
    c "Oh, Saito-kun. What's wrong?{#ch17_c_001}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：あのー。
    voice "ch17_s_017"
    s "Um… Sorry, could you hide me for a bit?{#ch17_s_017}"

    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # コルベール：うん？
    voice "ch17_c_002"
    c "Hm? What happened?{#ch17_c_002}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    hide]
    # [BG       stage    image=+82, level=200]
    $ fade_fx("id(82)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # コルベール：はははははっ。
    voice "ch17_c_003"
    c "Hahahaha! Of course—even Saito-kun is powerless before women, eh?{#ch17_c_003}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：笑い事じゃないですよ。
    voice "ch17_s_018"
    s "This is no laughing matter. I'm trembling, wondering when I'll be punished.{#ch17_s_018}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：いや、失礼。
    voice "ch17_c_004"
    c "No, excuse me. I was just thinking Saito-kun is human too.{#ch17_c_004}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：……。  [voice 11716]
    voice "ch17_s_019"
    s "…{#ch17_s_019}"

    # コルベール：いやいや、怒らないでくれたまえ。
    voice "ch17_c_005"
    c "No, don't be angry. The fact you brought me this truth has changed my view of life.{#ch17_c_005}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：人生観？  [voice 11717]
    voice "ch17_s_020"
    s "View of life?{#ch17_s_020}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：そう、人生観。
    voice "ch17_c_006"
    c "Yes. Magic isn't something to attack others with, nor to create hierarchy.{#ch17_c_006}"

    # コルベール：魔法は、魔法を使わない人のために
    voice "ch17_c_007"
    c "Magic is only true magic when it helps those who can't use it. That's what I believe.{#ch17_c_007}"

    # サイト：はぁ……。  [voice 11718]
    voice "ch17_s_021"
    s "Haa…{#ch17_s_021}"

    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # コルベール：いや、すまない……。
    voice "ch17_c_008"
    c "No, I'm sorry… I got carried away.{#ch17_c_008}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：いえ……。  [voice 11719]
    voice "ch17_s_022"
    s "Not at all…{#ch17_s_022}"

    # サイト：（考えてみれば、コルベール先生と、
    s "(Come to think of it, I've known Colbert-sen since I found the Zero Fighter…){#ch17_s_023}"

    # サイト：（もともとはルイズの先生って立場から
    s "(At first he seemed interested in me as Louise's teacher…){#ch17_s_024}"

    # サイト：（ゼロ戦を飛ばすっていう一緒の目的を
    s "(Ever since we shared the goal of flying the Zero Fighter, he's become my teacher too…){#ch17_s_025}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # モンモランシー：サイト。
    voice "ch17_m_001"
    m "Saito. I thought you'd be here.{#ch17_m_001}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：モンモン！
    voice "ch17_s_026"
    s "Montmon! How did you know I was here?{#ch17_s_026}"

    # [SPRITE   lay3     image=+887, level=160, dir=2A]
    # モンモランシー：あなたがさっき、ミスタ・コルベールの
    voice "ch17_m_002"
    m "I saw you enter Mr. Colbert's room just now.{#ch17_m_002}"

    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # モンモランシー：わたしはただオールド・オスマンに
    voice "ch17_m_003"
    m "I was just told by old Osmond to call you and Louise.{#ch17_m_003}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：学院長が？
    voice "ch17_s_027"
    s "The headmaster? What for?{#ch17_s_027}"

    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # モンモランシー：さあ？
    voice "ch17_m_004"
    m "Beats me. I wasn't told the details.{#ch17_m_004}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：分かった、向かうよ。
    voice "ch17_s_028"
    s "All right, let's go. Thanks, Colbert-sen.{#ch17_s_028}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：いや、なに。
    voice "ch17_c_009"
    c "No, no. Come anytime.{#ch17_c_009}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+29, level=200]
    $ fade_fx("id(29)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # ルイズ：姫さまが、わたし達に？  [voice 6270]
    voice "ch17_l_012"
    l "The Princess wants to see us?{#ch17_l_012}"

    # オスマン：うむ、どうやら火急の用件らしくてのぅ。
    voice "ch17_o_001"
    o "Aye, seems urgent. Sorry, but could you head to the palace at once? She said she'll explain in person.{#ch17_o_001}"

    # ルイズ：分かりました。
    voice "ch17_l_013"
    l "Understood. We'll go at once.{#ch17_l_013}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なんだか、いやな予感がするな……。  [voice 11723]
    voice "ch17_s_029"
    s "I've got a bad feeling about this…{#ch17_s_029}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 675
    jump ch17_1_scene_675

label ch17_1_scene_675:

    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # 味方Ａ：女王陛下、ラ・ヴァリエール公爵家三女、
    voice "ch17_soldier_001"
    soldier "Her Majesty—Louise Francoise, third daughter of the La Valliere family, and her familiar have arrived.{#ch17_soldier_001}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：女王陛下……。
    voice "ch17_l_014"
    l "Your Majesty… Fair morning to you.{#ch17_l_014}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     image=+797, level=160, dir=2A]
    # アンリエッタ：ああ、やっと来てくれたのね！
    voice "ch17_h_001"
    h "Ah, you finally came! Come in, Louise. You too, familiar.{#ch17_h_001}"

    # [SPRITE   lay8     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：で、でも……。  [voice 11724]
    voice "ch17_s_030"
    s "B-But…{#ch17_s_030}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay18    image=+1123, level=160, dir=1A]
    # 将校：……。  [voice 4298]
    voice "ch17_commander_001"
    commander "…{#ch17_commander_001}"

    # [SPRITE   lay18    hide]
    # [SPRITE   lay8     image=+797, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なんか軍人さんがたくさんいますけど、
    voice "ch17_s_031"
    s "There are a lot of soldiers here. Were you in the middle of a meeting?{#ch17_s_031}"

    # アンリエッタ：ええ。
    voice "ch17_h_002"
    h "Yes. That's why I called you.{#ch17_h_002}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：どういうことでございますか、陛下？  [voice 6273]
    voice "ch17_l_015"
    l "What do you mean, Your Majesty?{#ch17_l_015}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     level=154]
    # [SPRITE   lay18    image=+1121, level=160, dir=1A]
    # 将校：陛下。
    voice "ch17_commander_002"
    commander "Your Majesty, shall we resume the meeting soon?{#ch17_commander_002}"

    # 将校：いかなるお考えかは分かりませんが、
    voice "ch17_commander_003"
    commander "Whatever your reasoning, waiting for such children has cost us considerable time.{#ch17_commander_003}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：……。  [voice 6274]
    voice "ch17_l_016"
    l "…{#ch17_l_016}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+396, level=156, dir=1A]
    # サイト：感じワル。  [voice 11726]
    voice "ch17_s_032"
    s "Rude.{#ch17_s_032}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+797, level=154, dir=2A]
    # アンリエッタ：そうですね。
    voice "ch17_h_003"
    h "True. This is urgent. A map of the capital, here.{#ch17_h_003}"

    # 味方Ａ：は。  [voice 4227]
    # voice id 4227 — нет аудиодорожки, строка voice пропущена
    soldier "Yes.{#ch17_soldier_002}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay18    hide]
    # [SPRITE   lay15    hide]
    # [BG       stage    hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [EVENT_CG event    image=+135, level=80]
    $ dissolve_fx("id(135)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # アンリエッタ：ありがとう。
    voice "ch17_h_004"
    h "Thank you. About the bombings occurring around the capital lately…{#ch17_h_004}"

    # アンリエッタ：それについて、わたくしなりに調査し、
    voice "ch17_h_005"
    h "I investigated them myself and arrived at a certain hypothesis.{#ch17_h_005}"

    # アンリエッタ：それを皆さんに説明し、
    voice "ch17_h_006"
    h "I wanted to explain it to everyone and have you judge it.{#ch17_h_006}"

    # 将校：そのようなことのために、
    voice "ch17_commander_004"
    commander "You summoned us for something like this!?{#ch17_commander_004}"

    # 将校：それよりも、今、目の前にいる敵を、
    voice "ch17_commander_005"
    commander "Rather than that, what do you intend to do about the enemy right before your eyes!?{#ch17_commander_005}"

    # サイト：あのさあ、おっさん。
    voice "ch17_s_033"
    s "Hey, mister. Shut up for a bit and listen to the Princess. She thought hard about this, you know.{#ch17_s_033}"

    # 将校：お、おっさん！？
    voice "ch17_commander_006"
    commander "M-Mister!? You—insolence!{#ch17_commander_006}"

    # ルイズ：サ、サイト！
    voice "ch17_l_017"
    l "S-Saito! Apologize at once!{#ch17_l_017}"

    # サイト：いやだね。  [voice 11728]
    voice "ch17_s_034"
    s "No way.{#ch17_s_034}"

    # 将校：貴様……。  [voice 4304]
    voice "ch17_commander_007"
    commander "You…{#ch17_commander_007}"

    # アンリエッタ：みなさん、今は会議の時です。
    voice "ch17_h_007"
    h "Everyone, this is a meeting. Put away your swords!{#ch17_h_007}"

    # 将校：むぐぐ……。  [voice 4305]
    voice "ch17_commander_008"
    commander "Grr…{#ch17_commander_008}"

    # ルイズ：申し訳ございません、女王陛下。
    voice "ch17_l_018"
    l "I'm sorry, Your Majesty. My familiar's insult is my insult. Punish me.{#ch17_l_018}"

    # アンリエッタ：いえ、いいのです。
    voice "ch17_h_008"
    h "No, it's fine. My chairing of the meeting was at fault. Just a little more time, please.{#ch17_h_008}"

    # 将校：……。  [voice 4306]
    voice "ch17_commander_009"
    commander "…{#ch17_commander_009}"

    # アンリエッタ：では、話を続けます。  [voice 588]
    voice "ch17_h_009"
    h "Then let's continue.{#ch17_h_009}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay18    hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [EVENT_CG event    image=+259, level=80]
    $ dissolve_fx("id(259)")
    # [TRANS trans("crossfade", 1000)]
    # アンリエッタ：地図を見てください。
    voice "ch17_h_010"
    h "Look at the map. These are the sites of the bombings so far. First here, then here…{#ch17_h_010}"

    # ルイズ：え、これって……？  [voice 6277]
    voice "ch17_l_019"
    l "Eh, this is…?{#ch17_l_019}"

    # サイト：城を……ぐるっと丸くかこむような形で
    voice "ch17_s_035"
    s "They're arranged in a circle around the castle.{#ch17_s_035}"

    # アンリエッタ：そうです。
    voice "ch17_h_011"
    h "Yes. I can't call it mere coincidence. {#ch17_h_011}"

    # ルイズ：偶然ではないとしたら、一体……？  [voice 6278]
    voice "ch17_l_020"
    l "If it's not coincidence, then what…?{#ch17_l_020}"

    # アンリエッタ：今回の爆破事件の現場を修復するに当たり、
    voice "ch17_h_012"
    h "Repairing the bomb sites requires more craftsmen than this country has. So many from abroad were brought in.{#ch17_h_012}"

    # アンリエッタ：わたくし達が国外から呼び入れた職人達が、
    voice "ch17_h_013"
    h "If those craftsmen were honest, fine… But considering the bombings…{#ch17_h_013}"

    # サイト：ってことは……？  [voice 11730]
    voice "ch17_s_036"
    s "So you mean…?{#ch17_s_036}"

    menu:
        "A bomb-loving craftsman!?{#ch17_1_c_675_1}":
            jump ch17_1_scene_676
        "An agent disguised as a craftsman!?{#ch17_1_c_675_2}":
            jump ch17_1_scene_677
        "A sightseeing craftsman!?{#ch17_1_c_675_3}":
            jump ch17_1_scene_678

label ch17_1_scene_676:

    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [EVENT_CG event    image=+259, level=80]
    $ dissolve_fx("id(259)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+392, level=156, dir=1A]
    # サイト：犯人は爆弾好きな職人ってことですか！
    voice "ch17_s_037"
    s "The culprit is a bomb-loving craftsman!? Or did they hire a fireworks maker by mistake!?{#ch17_s_037}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+308, level=155, dir=1A]
    # ルイズ：今、あんたを召喚したこと、
    voice "ch17_l_021"
    l "I so regret summoning you right now.{#ch17_l_021}"

    # [SPRITE   lay5     image=+396, level=156, dir=1A]
    # サイト：どうした、ルイズ。
    voice "ch17_s_038"
    s "What, Louise. You look really depressed… Maybe I'm wrong?{#ch17_s_038}"

    # [SPRITE   lay1     image=+339, level=155, dir=2A]
    # ルイズ：職人達が呼ばれたのは、事件の後でしょう？
    voice "ch17_l_022"
    l "The craftsmen were called after the incidents, right? Then why bomb first! That bomb-loving craftsman!{#ch17_l_022}"

    # [SPRITE   lay5     image=+429, level=156, dir=2A]
    # サイト：そ、そうだな。  [voice 11733]
    voice "ch17_s_039"
    s "R-Right.{#ch17_s_039}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     image=+803, level=154, dir=2A]
    # → next scene 679
    jump ch17_1_scene_679

label ch17_1_scene_677:

    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [EVENT_CG event    image=+259, level=80]
    $ dissolve_fx("id(259)")
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+427, level=156, dir=2A]
    # サイト：職人を装って、
    voice "ch17_s_040"
    s "You mean an agent may have infiltrated disguised as a craftsman?{#ch17_s_040}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+341, level=155, dir=2A]
    # ルイズ：そうだとしたら、今頃、爆破事件のあった
    voice "ch17_l_023"
    l "If so, the bomb sites by now…{#ch17_l_023}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     image=+803, level=154, dir=2A]
    # アンリエッタ：はい、そのとおりです。  [voice 593]
    voice "ch17_h_014"
    h "Yes, exactly.{#ch17_h_014}"

    # → next scene 679
    jump ch17_1_scene_679

label ch17_1_scene_678:

    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [EVENT_CG event    image=+259, level=80]
    $ dissolve_fx("id(259)")
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+427, level=156, dir=2A]
    # サイト：この都を観光したかった職人が、
    voice "ch17_s_041"
    s "A craftsman who wanted to sightsee in the capital caused the bombings!? What a roundabout way…!{#ch17_s_041}"

    # [SPRITE   lay5     image=+427, level=156, dir=2A]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：ばかっ！
    voice "ch17_l_024"
    l "Idiot! Why would he!{#ch17_l_024}"

    # [SPRITE   lay5     image=+429, level=156, dir=2A]
    # サイト：え、ちがうの？  [voice 11736]
    voice "ch17_s_042"
    s "Eh, am I wrong?{#ch17_s_042}"

    # ルイズ：全っ然ちがうっ！  [voice 6283]
    voice "ch17_l_025"
    l "Completely wrong!{#ch17_l_025}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     image=+803, level=154, dir=2A]
    # → next scene 679
    jump ch17_1_scene_679

label ch17_1_scene_679:

    # [SPRITE   lay8     image=+803, level=154, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # アンリエッタ：おそらくですが、これを機会に、
    voice "ch17_h_015"
    h "Most likely, taking this chance, an agent has infiltrated disguised as a craftsman…{#ch17_h_015}"

    # [SPRITE   lay8     x=-96, y=0]
    # [SPRITE   lay18    image=+1123, level=160, dir=1A]
    # 将校：ばかな！
    voice "ch17_commander_010"
    commander "Nonsense! Impossible!{#ch17_commander_010}"

    # [SPRITE   lay8     image=+801, level=154, dir=2A]
    # アンリエッタ：なぜ、そう言い切れるのです？
    voice "ch17_h_016"
    h "Why can you say that so certainly? Analyzing all the evidence and the culprit's movements, there's no other explanation.{#ch17_h_016}"

    # [SPRITE   lay18    hide]
    # [SPRITE   lay1     image=+339, level=155, dir=2A]
    # ルイズ：それでは、急いで対処しなければ！  [voice 6284]
    voice "ch17_l_026"
    l "Then we must act quickly!{#ch17_l_026}"

    # [SPRITE   lay8     image=+803, level=154, dir=2A]
    # アンリエッタ：はい。
    voice "ch17_h_017"
    h "Yes. Investigate the craftsmen at once. It may already be too late…{#ch17_h_017}"

    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay16    vibrate=14]
    # [SPRITE   lay15    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay8     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay18    vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay16    hide, reset]
    # [SPRITE   lay15    hide, reset]
    # [SPRITE   lay1     reset]
    # [SPRITE   lay8     reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay18    hide, reset]
    # [SPRITE   lay1     image=+308, level=155, dir=1A]
    # ルイズ：きゃあっ！  [voice 6285]
    voice "ch17_l_027"
    l "Eek!{#ch17_l_027}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay18    image=+1123, level=160, dir=1A]
    # 将校：な、なんだっ！？  [voice 4308]
    voice "ch17_commander_011"
    commander "W-What was that!?{#ch17_commander_011}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay18    hide]
    # [BG       stage    hide]
    # → next scene 680
    jump ch17_1_scene_680

label ch17_1_scene_680:

    # [EVENT_CG event    image=+135, level=80]
    $ dissolve_fx("id(135)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # 将校：爆破事件の犯人が、城を狙ってきたのか？  [voice 4309]
    voice "ch17_commander_012"
    commander "Has the bomber come for the castle?{#ch17_commander_012}"

    # アンリエッタ：お待ちなさい、この攻撃は……。
    voice "ch17_h_018"
    h "Wait. This attack is—Report the situation!{#ch17_h_018}"

    # 味方Ａ：はっ。
    voice "ch17_soldier_003"
    soldier "Yes! Shelling toward the palace confirmed from points all over the city!{#ch17_soldier_003}"

    # 将校：市内に砲台とはどういうことだ？
    voice "ch17_commander_013"
    commander "Cannons inside the city? How is that possible?{#ch17_commander_013}"

    # 味方Ａ：砲台が設置されているのは、先般の爆破事件の
    voice "ch17_soldier_004"
    soldier "Reports say the cannons are installed at the sites of the recent bombings' repairs!{#ch17_soldier_004}"

    # アンリエッタ：砲台まであるというのですか！
    voice "ch17_h_019"
    h "There are cannons too! To let the enemy into this city… What has happened…!{#ch17_h_019}"

    # 味方Ａ：女王陛下、もうひとつ……。
    voice "ch17_soldier_005"
    soldier "Your Majesty, one more… report.{#ch17_soldier_005}"

    # アンリエッタ：それは？  [voice 599]
    voice "ch17_h_020"
    h "And that is?{#ch17_h_020}"

    # 味方Ａ：レコン・キスタの空中艦隊が、トリステインを
    voice "ch17_soldier_006"
    soldier "Scouts report Reconquista's aerial fleet has begun moving toward Tristain.{#ch17_soldier_006}"

    # 将校：何だと！
    voice "ch17_commander_014"
    commander "What!? Have they already forgotten their defeat the other day!{#ch17_commander_014}"

    # 味方Ａ：現在の位置から推測するに、
    voice "ch17_soldier_007"
    soldier "Judging from their current position, the fleet will enter Tristain's airspace in a little over two days.{#ch17_soldier_007}"

    # アンリエッタ：出動可能な部隊は、速やかに砲台の奪還を！
    voice "ch17_h_021"
    h "All available units—recover the cannons immediately! Mages, don't lose sight of the fleet!{#ch17_h_021}"

    # 将校：はっ！  [voice 4312]
    voice "ch17_commander_015"
    commander "Yes!{#ch17_commander_015}"

    # アンリエッタ：また、砲台付近の住民を急ぎ避難させなさい！
    voice "ch17_h_022"
    h "Also, evacuate residents near the cannons at once! Not a single drop of our people's blood may be spilled in Tristain!{#ch17_h_022}"

    # 将校：はっ！  [voice 4313]
    voice "ch17_commander_016"
    commander "Yes!{#ch17_commander_016}"

    # サイト：（将校達がどんどん部屋を出て行くな。
    s "(The officers are leaving one by one. Should we go too…?){#ch17_s_043}"

    # ルイズ：……。  [voice 6286]
    voice "ch17_l_028"
    l "…{#ch17_l_028}"

    menu:
        "Princess, what we can do is…{#ch17_1_c_680_1}":
            jump ch17_1_scene_681
        "I just follow Louise{#ch17_1_c_680_2}":
            jump ch17_1_scene_682
        "The academy's in danger! We have to go back!{#ch17_1_c_680_3}":
            jump ch17_1_scene_683

label ch17_1_scene_681:

    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [EVENT_CG event    image=+135, level=80]
    $ dissolve_fx("id(135)")
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay18    hide]
    # [SPRITE   lay15    hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # → next scene 684
    jump ch17_2

label ch17_1_scene_682:

    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [EVENT_CG event    image=+135, level=80]
    $ dissolve_fx("id(135)")
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay18    hide]
    # [SPRITE   lay15    hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # [SPRITE   lay5     hide]
    # → next scene 684
    jump ch17_2

label ch17_1_scene_683:

    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [EVENT_CG event    image=+135, level=80]
    $ dissolve_fx("id(135)")
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay18    hide]
    # [SPRITE   lay15    hide]
    # [SPRITE   lay1     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # → next scene 684
    jump ch17_2

    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch17_2
    return

