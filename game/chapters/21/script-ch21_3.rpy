# Глава 21, часть 3 (сцены 790–805 + 1204–1208): подготовка, свидание с Сиэстой.
# Источник: ps2_source/chapters/chapter_22_サイトのメイド.txt.

label ch21_3:
    $ tndl(None)
    $ show_sprites()

label ch21_3_scene_790:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     x=144, y=416]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：それじゃあ、勝負の段取りはあたしが
    voice "ch21_k_027"
    k "Well, I'll handle the arrangements for the contest. Look forward to it.{#ch21_k_027}"

    # [SPRITE   lay6     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：分かったわ。  [voice 6595]
    voice "ch21_l_056"
    l "I know.{#ch21_l_056}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：それじゃあ、シエスタ。
    voice "ch21_k_028"
    k "Then, Siesta—let's see what you're capable of, shall we?{#ch21_k_028}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：分かりましたわ、ミス・ツェルプストー。
    voice "ch21_si_051"
    si "Understood, Miss Zerbst. Please go easy on me.{#ch21_si_051}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+986, level=160, dir=2A]
    # ハルナ：よぉし、頑張るわよっ！！  [voice 2395]
    voice "ch21_ha_011"
    ha "All right, I'll do my best!!{#ch21_ha_011}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay2     hide]
    # [SPRITE   lay7     hide]
    # [BG       stage    hide]
    # → next scene 791
    jump ch21_3_scene_791

label ch21_3_scene_791:

    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：やれやれ。
    voice "ch21_s_097"
    s "Good grief. I got dragged into something terrible, didn't I…{#ch21_s_097}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay19    image=+942, level=160, dir=1A]
    # デルフリンガー：へへへっ、相棒っ！
    voice "ch21_d_001"
    d "Heh heh! Things are getting interesting, aren't they, partner?{#ch21_d_001}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：なんだよデルフ……。
    voice "ch21_s_098"
    s "What's that supposed to mean, Derf? Don't act like it's someone else's problem.{#ch21_s_098}"

    # デルフリンガー：どうしたよ、お手並み拝見と行こうじゃねーか？
    voice "ch21_d_002"
    d "What's wrong? Let's just watch the show. Still, being popular is a pain, huh.{#ch21_d_002}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：俺のせいじゃないだろ？  [voice 12085]
    voice "ch21_s_099"
    s "It's not my fault, is it?{#ch21_s_099}"

    # [SPRITE   lay19    image=+946, level=160, dir=1A]
    # デルフリンガー：そうかぁ？
    voice "ch21_d_003"
    d "Is that so? I'd say your wishy-washy attitude is the cause, though…{#ch21_d_003}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：しょうがないだろ？
    voice "ch21_s_100"
    s "I can't help it. I'm not from this world. I do want to go back someday…{#ch21_s_100}"

    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # デルフリンガー：分かった分かった。
    voice "ch21_d_004"
    d "All right, all right. I won't say any more. I just need things to be fun.{#ch21_d_004}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：……。  [voice 12087]
    voice "ch21_s_101"
    s "…{#ch21_s_101}"

    # デルフリンガー：ところで、相棒。
    voice "ch21_d_005"
    d "By the way, partner. Who do you think will win?{#ch21_d_005}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：うーん……。  [voice 12088]
    voice "ch21_s_102"
    s "Hmm…{#ch21_s_102}"

    menu:
        "Siesta, the favorite{#ch21_3_c_791_1}":
            jump ch21_3_scene_792
        "Louise, the dark horse{#ch21_3_c_791_2}":
            jump ch21_3_scene_793
        "Me{#ch21_3_c_791_3}":
            jump ch21_3_scene_794

label ch21_3_scene_792:

    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：やっぱり、本命のシエスタじゃないか？
    voice "ch21_s_103"
    s "Siesta's the favorite, isn't she? She's used to cooking, being a maid and all.{#ch21_s_103}"

    # デルフリンガー：ま、順当ってとこだぁな。
    voice "ch21_d_006"
    d "Yeah, that's the obvious pick. Not much fun in it, though.{#ch21_d_006}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：おいおい、面白みで話すのやめてくれよ。
    voice "ch21_s_104"
    s "Hey, quit talking about 'fun.' I'm the one who has to eat it, you know. I'd be in trouble if they made something 'interesting.'{#ch21_s_104}"

    # → next scene 795
    jump ch21_3_scene_795

label ch21_3_scene_793:

    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：意外と大穴でルイズかもしれない。  [voice 12091]
    voice "ch21_s_105"
    s "Actually, Louise might be a dark horse.{#ch21_s_105}"

    # [SPRITE   lay19    image=+946, level=160, dir=1A]
    # デルフリンガー：おいおい相棒、本気で言ってんのかい？  [voice 1342]
    voice "ch21_d_007"
    d "Hey, partner, are you serious?{#ch21_d_007}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：あいつ、いざって時にすごいこと
    voice "ch21_s_106"
    s "She does amazing things when push comes to shove. You never know.{#ch21_s_106}"

    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # デルフリンガー：なるほどな。
    voice "ch21_d_008"
    d "I see. Well, that'd be the best outcome for you, partner.{#ch21_d_008}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：どして？  [voice 12093]
    voice "ch21_s_107"
    s "Why's that?{#ch21_s_107}"

    # [SPRITE   lay19    image=+946, level=160, dir=1A]
    # デルフリンガー：貴族の娘っ子が優勝するような料理を
    voice "ch21_d_009"
    d "If a noble girl cooks something good, fine—but if not… What do you think she'll come up with?{#ch21_d_009}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そ、そうだった……。
    voice "ch21_s_108"
    s "R-Right… Louise, please…{#ch21_s_108}"

    # → next scene 795
    jump ch21_3_scene_795

label ch21_3_scene_794:

    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：俺。  [voice 12095]
    voice "ch21_s_109"
    s "Me.{#ch21_s_109}"

    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # デルフリンガー：は？
    voice "ch21_d_010"
    d "Huh? You don't cook, partner.{#ch21_d_010}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：考えてもみろよ。
    voice "ch21_s_110"
    s "Think about it. I'm the one eating what they make, right? Siesta's reassuring, sure, but…{#ch21_s_110}"

    # [SPRITE   lay19    image=+946, level=160, dir=1A]
    # デルフリンガー：頑張れ、相棒。  [voice 1346]
    voice "ch21_d_011"
    d "Hang in there, partner.{#ch21_d_011}"

    # → next scene 795
    jump ch21_3_scene_795

label ch21_3_scene_795:

    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：なんだか、ちょっと心配になってきたな。
    voice "ch21_s_111"
    s "I'm getting a little worried. Maybe I should go check on them…{#ch21_s_111}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # 【移動】タバサの部屋 → scene 588  ((0x01000000 +1493))
    th "[Move] Tabitha's room{#ch21_th_001}"

    # 【移動】中庭 → scene 676  ((0x01000000 +1498))
    th "[Move] Courtyard{#ch21_th_002}"

    # 【移動】ルイズの部屋 → scene 302  ((0x01000000 +1503))
    th "[Move] Louise's room{#ch21_th_003}"

    # 【移動】中庭 → scene 951  ((0x01000000 +1508))
    th "[Move] Courtyard{#ch21_th_004}"

label ch21_3_scene_796:

    # [BG       stage    image=+14, hide, level=10]
    $ fade_fx("id(14)")
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+14, hide, level=10]
    $ fade_fx("id(14)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+14, hide, level=10]
    $ fade_fx("id(14)")
    # → next scene 1493
    # date event → ch21_4 (extra)
    jump ch21_4

label ch21_3_scene_797:

    # [BG       stage    image=+14, hide, level=10]
    $ fade_fx("id(14)")
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+14, hide, level=10]
    $ fade_fx("id(14)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+14, hide, level=10]
    $ fade_fx("id(14)")
    # → next scene 1498
    # date event → ch21_4 (extra)
    jump ch21_4

label ch21_3_scene_798:

    # [BG       stage    image=+14, hide, level=10]
    $ fade_fx("id(14)")
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+14, hide, level=10]
    $ fade_fx("id(14)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+14, hide, level=10]
    $ fade_fx("id(14)")
    # → next scene 1503
    # date event → ch21_4 (extra)
    jump ch21_4

label ch21_3_scene_799:

    # [BG       stage    image=+14, hide, level=10]
    $ fade_fx("id(14)")
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+14, hide, level=10]
    $ fade_fx("id(14)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+14, hide, level=10]
    $ fade_fx("id(14)")
    # → next scene 1508
    # date event → ch21_4 (extra)
    jump ch21_4

label ch21_3_scene_800:

    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # サイト：ああ、何だか疲れたなぁ。
    voice "ch21_s_112"
    s "Ah, I'm exhausted. I think I'll sleep great on a straw bed tonight, too.{#ch21_s_112}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+12, level=200]
    $ fade_fx("id(12)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：サイトさん、お疲れさまでした。  [voice 14863]
    voice "ch21_si_052"
    si "Saito-san, you've worked hard.{#ch21_si_052}"

    # サイト：ああ、シエスタの方こそお疲れ。
    voice "ch21_s_113"
    s "Ah, Siesta, you too. Cleaning and laundry from morning, and on top of that preparing for the cooking contest…{#ch21_s_113}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ホント、平気かい？  [voice 12100]
    voice "ch21_s_114"
    s "Really, are you all right?{#ch21_s_114}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：ええ。
    voice "ch21_si_053"
    si "Yes. Thank you for worrying about me, Saito-san.{#ch21_si_053}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：まったく……。
    voice "ch21_s_115"
    s "Honestly… What are those two thinking?{#ch21_s_115}"

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：でも、ちょっと楽しそう。
    voice "ch21_si_054"
    si "But it's a little fun, isn't it? Perhaps they're worried because I was down?{#ch21_si_054}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：強いんだな、シエスタは。  [voice 12102]
    voice "ch21_s_116"
    s "You're strong, Siesta.{#ch21_s_116}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：うふふ、わたしだけじゃありません。
    voice "ch21_si_055"
    si "Heh heh, I'm not the only one. Girls are much stronger than Saito-san thinks, you know?{#ch21_si_055}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：うーん、よく分かんねーよ。  [voice 12103]
    voice "ch21_s_117"
    s "Hmm, I don't really get it.{#ch21_s_117}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：うふふ、もう、サイトさんったら。  [voice 14867]
    voice "ch21_si_056"
    si "Heh heh, really, Saito-san.{#ch21_si_056}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：ははははっ。  [voice 12104]
    voice "ch21_s_118"
    s "Ha ha ha!{#ch21_s_118}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あのっ……サイトさん。  [voice 14868]
    voice "ch21_si_057"
    si "Um… Saito-san.{#ch21_si_057}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：うん？  [voice 12105]
    voice "ch21_s_119"
    s "Hmm?{#ch21_s_119}"

    # [SPRITE   lay2     image=+497, level=160, dir=1A]
    # シエスタ：その……ぅ……。
    voice "ch21_si_058"
    si "Um… Could I… sit next to you?{#ch21_si_058}"

    # [SPRITE   lay5     image=+431, level=160, dir=2A]
    # サイト：え？
    voice "ch21_s_120"
    s "Eh? A-Ah… Sure.{#ch21_s_120}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SE       se0      play=+59]
    # シエスタ：しょっと……。
    voice "ch21_si_059"
    si "Eep… Heh heh, straw is soft, isn't it?{#ch21_si_059}"

    # サイト：（ちょ、ちょっと……。
    s "(H-Hey… Cuddling up to me is cheating!!){#ch21_s_121}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SE       se0      play=+57]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # ルイズ：ただいまぁ……。
    voice "ch21_l_057"
    l "I'm back… Wait, hey! What are you two doing, all cuddled up together!?{#ch21_l_057}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # サイト：うわっ、ルイズっ！！  [voice 12107]
    voice "ch21_s_122"
    s "Whoa, Louise!!{#ch21_s_122}"

    # シエスタ：……あっ！！
    voice "ch21_si_060"
    si "…Ah! W-Welcome back, Miss Valliere. Haruna-san…{#ch21_si_060}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay7     image=+990, level=160, dir=2A]
    # ルイズ：一体、何してたの！
    voice "ch21_l_058"
    l "Just what were you doing! Tell me!{#ch21_l_058}"

    # ハルナ：シエスタさんひどいです。
    voice "ch21_ha_012"
    ha "Siesta, that was awful. Sneaking up on Hiraga-kun like that…{#ch21_ha_012}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：な、なんでもない、話してただけだよ！  [voice 12108]
    voice "ch21_s_123"
    s "N-Nothing! We were just talking!{#ch21_s_123}"

    # ルイズ：何をよ！  [voice 6598]
    voice "ch21_l_059"
    l "Talking about what!{#ch21_l_059}"

    menu:
        "About the cooking contest{#ch21_3_c_800_1}":
            jump ch21_3_scene_801
        "About Louise's strength{#ch21_3_c_800_2}":
            jump ch21_3_scene_802
        "About how soft the straw is{#ch21_3_c_800_3}":
            jump ch21_3_scene_803

label ch21_3_scene_801:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+12, level=200]
    $ fade_fx("id(12)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：ほ、ほら、料理対決があるだろ！？
    voice "ch21_s_124"
    s "L-Look, the cooking contest is coming up, right? So we were talking about all sorts—{#ch21_s_124}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：ほほー……。
    voice "ch21_l_060"
    l "Heh heh… You really think that excuse will work?{#ch21_l_060}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ほ、ほんとだって！  [voice 12110]
    voice "ch21_s_125"
    s "I-It's true!{#ch21_s_125}"

    # → next scene 804
    jump ch21_3_scene_804

label ch21_3_scene_802:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+12, level=200]
    $ fade_fx("id(12)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：ほ、ほら、女の子は強いなって話をさ！
    voice "ch21_s_126"
    s "L-Look, we were talking about how strong girls are! Like Louise and…{#ch21_s_126}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：わたしが強いですって？
    voice "ch21_l_061"
    l "Me, strong? That's rude to a lady!{#ch21_l_061}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ち、ちがっ、そういう意味じゃなくて！  [voice 12112]
    voice "ch21_s_127"
    s "N-No, I didn't mean it that way!{#ch21_s_127}"

    # → next scene 804
    jump ch21_3_scene_804

label ch21_3_scene_803:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+12, level=200]
    $ fade_fx("id(12)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：ほ、ほら、意外と柔らかいもんだなってさ！  [voice 12113]
    voice "ch21_s_128"
    s "L-Look, I was saying how surprisingly soft it is!{#ch21_s_128}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：な、な、なななな何が柔らかいのよ！
    voice "ch21_l_062"
    l "Wh-Wh-What's soft! Did you touch it! You did, didn't you!{#ch21_l_062}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：誰もそんなこと言ってねーだろっ！
    voice "ch21_s_129"
    s "Nobody said anything like that! I said the straw was soft…{#ch21_s_129}"

    # → next scene 804
    jump ch21_3_scene_804

label ch21_3_scene_804:

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+12, level=200]
    $ fade_fx("id(12)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：問答無用よ！  [voice 6602]
    voice "ch21_l_063"
    l "No questions asked!{#ch21_l_063}"

    # ハルナ：ルイズさん、懲らしめてください！  [voice 2397]
    voice "ch21_ha_013"
    ha "Louise, punish him!{#ch21_ha_013}"

    # サイト：げえっ！？
    voice "ch21_s_130"
    s "Geeh!? Wait, wait, Louise!! Not the whip, not the whi—!!{#ch21_s_130}"

    # サイト：ひええっ！！
    voice "ch21_s_131"
    s "Hiiih! Help meee~!!{#ch21_s_131}"

    # [SE       se0      play=+71]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay7     hide, vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     hide, vibrate=14]
    # [SPRITE   lay1     hide, vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SE       se0      play=+71]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # サイト：ぐあっ……ぎぃええっ……あふんっ。  [voice 12117]
    voice "ch21_s_132"
    s "Guh… Giiih… Ugh.{#ch21_s_132}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # → next scene 805
    jump ch21_3_scene_805

label ch21_3_scene_805:

    # [BG       stage    image=+16, level=200]
    $ fade_fx("id(16)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：……ううっ、どこだここは？  [voice 12118]
    voice "ch21_s_133"
    s "…Ugh, where am I?{#ch21_s_133}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # デルフリンガー：よう、相棒。
    voice "ch21_d_012"
    d "Yo, partner. Finally awake? I thought you'd never wake up.{#ch21_d_012}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：よぉ、デルフ。
    voice "ch21_s_134"
    s "Hey, Derf. That was the worst way to wake up.{#ch21_s_134}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ここは……廊下かぁ。
    voice "ch21_s_135"
    s "So this is a hallway… I guess they dragged me out of the room. My body hurts…{#ch21_s_135}"

    # デルフリンガー：まぁ、しゃーねーわな。  [voice 1348]
    voice "ch21_d_013"
    d "Well, it couldn't be helped.{#ch21_d_013}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：はあっ～。
    voice "ch21_s_136"
    s "Haaah. What awful luck I have.{#ch21_s_136}"

    # サイト：この分じゃあ、シエスタも春奈も、
    voice "ch21_s_137"
    s "At this rate, Siesta, Haruna, and even Louise are all asleep by now…{#ch21_s_137}"

    # [SPRITE   lay19    image=+946, level=160, dir=1A]
    # デルフリンガー：ああ、相棒の巻き添えを食って、
    voice "ch21_d_014"
    d "Yeah. I got dragged into it as your partner and got kicked out, too.{#ch21_d_014}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：すまん。  [voice 12123]
    voice "ch21_s_138"
    s "Sorry.{#ch21_s_138}"

    # [SPRITE   lay19    image=+942, level=160, dir=1A]
    # デルフリンガー：良いってことよ、相棒。  [voice 1350]
    voice "ch21_d_015"
    d "It's fine, partner.{#ch21_d_015}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：まぁ、少し気分転換に散歩でもしてくるか……。  [voice 12124]
    voice "ch21_s_139"
    s "Well, I guess I'll go for a walk to clear my head…{#ch21_s_139}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
label ch21_3_scene_1204:

    # [BG       stage    image=+19, level=200]
    $ fade_fx("id(19)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：さすがに夜ともなると、
    voice "ch21_s_140"
    s "Even at night, it's deserted and a little eerie, isn't it?{#ch21_s_140}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # デルフリンガー：なんでぇ、暗闇が怖いってのかい？
    voice "ch21_d_016"
    d "What's wrong, scared of the dark? Don't be silly, you're no child.{#ch21_d_016}"

    # シエスタ：……わたしが敵の陣を説きましょう。
    voice "ch21_si_061"
    si "…Allow me to dissuade the enemy. If I return to the Empire, everything will be settled.{#ch21_si_061}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：……あれ？
    voice "ch21_s_141"
    s "…Huh? That voice just now… Siesta?{#ch21_s_141}"

    # デルフリンガー：ああ、村娘の声に違いねぇ。
    voice "ch21_d_017"
    d "Aye, that's the village girl's voice, all right. And I've heard those lines before, too.{#ch21_d_017}"

    # シエスタ：……ですが、このままでは王子は王国とお命を
    voice "ch21_si_062"
    si "…But if we go on like this, the prince will lose both his kingdom and his life!{#ch21_si_062}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+28, level=200]
    $ fade_fx("id(28)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：王子、いつぞやの求婚をいただいた
    voice "ch21_si_063"
    si "Prince, do you remember the night I received your proposal?{#ch21_si_063}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：今宵のように双月の美しい夜でございました。
    voice "ch21_si_064"
    si "It was a beautiful twin-moon night, just like tonight. Let me give you my answer now.{#ch21_si_064}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：……シエスタ。  [voice 8939]
    voice "ch21_s_142"
    s "…Siesta.{#ch21_s_142}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+526, level=160, dir=2A]
    # シエスタ：きゃあっ！？  [voice 14305]
    voice "ch21_si_065"
    si "Eep!?{#ch21_si_065}"

    # [SPRITE   lay2     image=+530, level=160, dir=2A]
    # シエスタ：……サイトさんっ。  [voice 14306]
    voice "ch21_si_066"
    si "…Saito-san.{#ch21_si_066}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：今のは、舞台で俺達がやった劇のセリフだろう？  [voice 8940]
    voice "ch21_s_143"
    s "That was the line from the play we did on stage, wasn't it?{#ch21_s_143}"

    # [SPRITE   lay2     image=+497, level=160, dir=1A]
    # シエスタ：あは、サイトさんならすぐに分かりますよね。
    voice "ch21_si_067"
    si "Ah, Saito-san figured it out right away, didn't you. You saw something embarrassing, didn't you~?{#ch21_si_067}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：俺はあんな舞台で芝居するなんて、
    voice "ch21_s_144"
    s "It was my first time acting on a stage like that… I was worried I'd mess up.{#ch21_s_144}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：そうですよねっ！
    voice "ch21_si_068"
    si "Isn't it! Especially the fear before the curtain rises—{#ch21_si_068}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：それは俺だって同じさ。
    voice "ch21_s_145"
    s "I felt the same. I kept thinking my voice would crack and ruin the mood.{#ch21_s_145}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：しかも俺、王子様なんて柄じゃないし。
    voice "ch21_s_146"
    s "And I'm not exactly prince material. But Siesta's princess suited you perfectly?{#ch21_s_146}"

    # [SPRITE   lay2     image=+497, level=160, dir=1A]
    # シエスタ：そうですか？
    voice "ch21_si_069"
    si "Really? …Thank you. Ehehe.{#ch21_si_069}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：あっははは……。
    voice "ch21_s_147"
    s "Ah ha ha… Still, the reception was better than I expected. Thank goodness.{#ch21_s_147}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：あれで全然ダメでした……なんて言ったら、
    voice "ch21_s_148"
    s "If I'd said it was terrible, Haruna's bag wouldn't have been returned, either.{#ch21_s_148}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：そうですね。
    voice "ch21_si_070"
    si "Right. It was the fruit of everyone's efforts—something we built together.{#ch21_si_070}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：そうだね。
    voice "ch21_s_149"
    s "Yeah. I think it was a really precious experience.{#ch21_s_149}"

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：はいっ、とてもいい思い出になりました。  [voice 14311]
    voice "ch21_si_071"
    si "Yes. It became a wonderful memory for me, too.{#ch21_si_071}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：でも……。  [voice 14312]
    voice "ch21_si_072"
    si "But…{#ch21_si_072}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ん？
    voice "ch21_s_150"
    s "Hmm? What's wrong?{#ch21_s_150}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：王子様とお姫様……。
    voice "ch21_si_073"
    si "The prince and princess… Why did they choose death?{#ch21_si_073}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：え？  [voice 8948]
    voice "ch21_s_151"
    s "Eh?{#ch21_s_151}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：もっと、別の方法も考えられたん
    voice "ch21_si_074"
    si "I keep thinking there might have been another way…{#ch21_si_074}"

    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # シエスタ：そう思うと、何だかちょっとやるせない
    voice "ch21_si_075"
    si "And when I think about it, I feel so very heavy-hearted.{#ch21_si_075}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：サイトさんは、どう思います？  [voice 14316]
    voice "ch21_si_076"
    si "What do you think, Saito-san?{#ch21_si_076}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：うーん……そうだなぁ。
    voice "ch21_s_152"
    s "Hmm… Let me see. If I were…{#ch21_s_152}"

    menu:
        "Send the princess home{#ch21_3_c_1204_1}":
            jump ch21_3_scene_1205
        "Run away together{#ch21_3_c_1204_2}":
            jump ch21_3_scene_1206
        "Destroy both countries{#ch21_3_c_1204_3}":
            jump ch21_3_scene_1207

label ch21_3_scene_1205:

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [BG       stage    image=+28, level=200]
    $ fade_fx("id(28)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：姫を自分の国に戻すかな……。  [voice 8950]
    voice "ch21_s_153"
    s "I'd send the princess back to her own country, I suppose…{#ch21_s_153}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：……そう、ですね……。  [voice 14317]
    voice "ch21_si_077"
    si "…Yes. That's right…{#ch21_si_077}"

    # サイト：やっぱり、生まれ育った場所を捨てさせるのは、
    voice "ch21_s_154"
    s "After all, forcing her to abandon the place she was born and raised would be cruel…{#ch21_s_154}"

    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # シエスタ：サイトさん……。  [voice 14318]
    voice "ch21_si_078"
    si "Saito-san…{#ch21_si_078}"

    # → next scene 1208
    jump ch21_3_scene_1208

label ch21_3_scene_1206:

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [BG       stage    image=+28, level=200]
    $ fade_fx("id(28)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：姫を連れて、どこかに逃げるかな……。
    voice "ch21_s_155"
    s "I'd take the princess and run away somewhere… where neither country could find us.{#ch21_s_155}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：素敵ですね。
    voice "ch21_si_079"
    si "How wonderful. Living together in some small village, just the two of us.{#ch21_si_079}"

    # サイト：うん、そうだね。  [voice 8953]
    voice "ch21_s_156"
    s "Yeah, that's right.{#ch21_s_156}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：それで、小さな畑を２人で耕して暮らして。
    voice "ch21_si_080"
    si "And we'd tend a small field together, and before long a child would be born… Saito-san, how many children would you like?{#ch21_si_080}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：え、ええ！？  [voice 8954]
    voice "ch21_s_157"
    s "E-Eh!?{#ch21_s_157}"

    # [SPRITE   lay2     image=+530, level=160, dir=2A]
    # シエスタ：い、いけない、わたし……。
    voice "ch21_si_081"
    si "N-No, I'm sorry… I got carried away imagining it…{#ch21_si_081}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：はははっ。  [voice 8955]
    voice "ch21_s_158"
    s "Ha ha ha!{#ch21_s_158}"

    # → next scene 1208
    jump ch21_3_scene_1208

label ch21_3_scene_1207:

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [BG       stage    image=+28, level=200]
    $ fade_fx("id(28)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：どっちの国も滅ぼして、俺が王様になるかな。  [voice 8956]
    voice "ch21_s_159"
    s "I'd destroy both countries and become king myself.{#ch21_s_159}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：くすっ。
    voice "ch21_si_082"
    si "Hehe. How heroic.{#ch21_si_082}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：なーんて、俺にはそんなことできるわけ
    voice "ch21_s_160"
    s "I'm kidding. I could never do something like that.{#ch21_s_160}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：サイトさんならできます。
    voice "ch21_si_083"
    si "You could, Saito-san. You can do anything, Saito-san.{#ch21_si_083}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そ、そうかな……。  [voice 8958]
    voice "ch21_s_161"
    s "R-Really…?{#ch21_s_161}"

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：そうです。  [voice 14324]
    voice "ch21_si_084"
    si "Yes.{#ch21_si_084}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：たはは、断言されちゃった。  [voice 8959]
    voice "ch21_s_162"
    s "Ha ha, you say it so confidently.{#ch21_s_162}"

    # → next scene 1208
    jump ch21_3_scene_1208

label ch21_3_scene_1208:

    # [SPRITE   lay2     image=+528, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [BG       stage    image=+28, level=200]
    $ fade_fx("id(28)")
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：もし、サイトさんが王子様だったら。  [voice 14325]
    voice "ch21_si_085"
    si "If you were the prince, Saito-san—{#ch21_si_085}"

    # [SPRITE   lay2     image=+497, level=160, dir=1A]
    # シエスタ：今の優しいサイトさんのまま、
    voice "ch21_si_086"
    si "Stay as kind as you are now, and just grow even stronger, okay? I'll be cheering you on from the shadows, too.{#ch21_si_086}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：うん。
    voice "ch21_s_163"
    s "Yeah. I'll try my best.{#ch21_s_163}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：いざとなったら、コイツでみんなを守ってやるさ。
    voice "ch21_s_164"
    s "If it comes to it, I'll protect everyone with this. Right, Derf—I'm counting on you, partner!{#ch21_s_164}"

    # [SE       se0      play=+65]
    # [SPRITE   lay19    image=+944, level=155, dir=1A]
    # [SPRITE   lay2     level=156]
    # [SPRITE   lay5     level=157]
    # デルフリンガー：へっ……。
    voice "ch21_d_018"
    d "Hah… Just one village girl — handle her with that one arm of yours, I'm telling you. Figure it out yourself.{#ch21_d_018}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     image=+396, level=157, dir=1A]
    # サイト：そ、そんなこと言わないでさああぁ～。
    voice "ch21_s_165"
    s "D-Don't say that! Please, Derflinger-saaan!{#ch21_s_165}"

    # [SPRITE   lay2     image=+524, level=156, dir=2A]
    # シエスタ：サイトさんたら、もぉ！
    voice "ch21_si_087"
    si "Oh, Saito-san, really! Hehe hehe hehe…{#ch21_si_087}"

    # [SPRITE   lay5     image=+429, level=157, dir=2A]
    # サイト：ははっ、カッコつかないなぁ……。  [voice 8963]
    voice "ch21_s_166"
    s "Ha ha, I can't keep a cool act, can't I…{#ch21_s_166}"

    # [SPRITE   lay2     image=+489, level=156, dir=1A]
    # シエスタ：それじゃあ、サイトさん。
    voice "ch21_si_088"
    si "Well then, Saito-san. Should we head back soon?{#ch21_si_088}"

    # [SPRITE   lay5     image=+390, level=157, dir=1A]
    # サイト：ああ、随分と遅くまで話し込んじゃったな。
    voice "ch21_s_167"
    s "Ah, we talked until quite late, didn't we. Let's go, then.{#ch21_s_167}"

    # [SPRITE   lay2     image=+491, level=156, dir=1A]
    # シエスタ：はい、王子様。  [voice 14329]
    voice "ch21_si_089"
    si "Yes, prince.{#ch21_si_089}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [COFFEE]
    $ pause(1.0)
    # → next scene 806
    jump ch22

    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SE       se0      play=+82]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SE       se0      play=+57]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [TRANS trans("crossfade", 1000)]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SE       se0      play=+56]
    # [LAYER    lay0     x=-96, y=0]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SE       se0      play=+72]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SE       se0      play=+72]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SE       se0      play=+72]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # → next scene 1497
    # date event → ch21_4 (extra)
    jump ch21_4

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # [LAYER    lay0     level=156]
    # [LAYER    lay0     image=+621, level=156, dir=2A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [LAYER    lay0     level=156]
    # [LAYER    lay0     image=+588, level=156, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # → next scene 1497
    # date event → ch21_4 (extra)
    jump ch21_4

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SE       se0      play=+72]
    # [SE       se0      play=+72]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # → next scene 1497
    # date event → ch21_4 (extra)
    jump ch21_4

    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay5     image=+431, level=160, dir=2A]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+119, level=80]
    $ dissolve_fx("id(119)")
    # [BGM      bgm      play=+14]
    play music t13 fadein 1.0
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [SPRITE   lay6     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay6     reset]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # → next scene 1502
    # date event → ch21_4 (extra)
    jump ch21_4

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # → next scene 1502
    # date event → ch21_4 (extra)
    jump ch21_4

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # → next scene 1502
    # date event → ch21_4 (extra)
    jump ch21_4

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+14]
    play music t13 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [SE       se0      play=+57]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # → next scene 1507
    # date event → ch21_4 (extra)
    jump ch21_4

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # → next scene 1507
    # date event → ch21_4 (extra)
    jump ch21_4

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # → next scene 1507
    # date event → ch21_4 (extra)
    jump ch21_4

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SE       se0      play=+57]
    # [SE       se0      play=+58]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # → next scene 1512
    # date event → ch21_4 (extra)
    jump ch21_4

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay3     image=+885, level=160, dir=2A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # → next scene 1512
    # date event → ch21_4 (extra)
    jump ch21_4

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay3     image=+885, level=160, dir=2A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # [SPRITE   lay3     image=+854, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # → next scene 1512
    # date event → ch21_4 (extra)
    jump ch21_4

    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay3     image=+887, level=160, dir=2A]
    # [SPRITE   lay3     hide]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ЧАСТИ 3 ====
    jump ch21_4
    return

