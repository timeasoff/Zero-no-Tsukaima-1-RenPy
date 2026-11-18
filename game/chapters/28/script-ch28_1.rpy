# Глава 28, часть 2 (сцена 1008): уход Харуны, финал.
# Источник: ps2_source/chapters/chapter_29_夜の秘密.txt (SCENE 1008).

label ch28_2:
    $ tndl(None)
    $ show_sprites()

label ch28_2_scene_1008:

    # [MOVIE movie(1)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：えっ、自立するってどういうことだよ？  [voice 9244]
    voice "ch28_s_070"
    s "Eh? What do you mean, becoming independent?{#ch28_s_070}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # ハルナ：うん、いつまでもこの学院で……。
    voice "ch28_ha_001"
    ha "Yeah. I can't stay at this academy forever… It'd be wrong to keep relying on Louise and the others.{#ch28_ha_001}"

    # サイト：そんなこといったら、俺なんかルイズに
    voice "ch28_s_071"
    s "If you say that, I've been taken care of by this academy ever since Louise summoned me.{#ch28_s_071}"

    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：平賀くんはルイズさんの使い魔じゃない。
    voice "ch28_ha_002"
    ha "Hiraga-kun is Louise-san's familiar. Of course you're taken care of. But I'm not one, so…{#ch28_ha_002}"

    # サイト：そりゃそうなんだけどさ……。
    voice "ch28_s_072"
    s "I know, but… We're probably the only two Japanese people in this world.{#ch28_s_072}"

    # サイト：それに、お互いのことを知らない
    voice "ch28_s_073"
    s "And we're not exactly strangers to each other… So if we worked at the academy, maybe…{#ch28_s_073}"

    # [SPRITE   lay7     image=+959, level=160, dir=1A]
    # ハルナ：あのね、平賀くん……。
    voice "ch28_ha_003"
    ha "The thing is, Hiraga-kun… I've been scouted.{#ch28_ha_003}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：ス、スカウトって、なんの？  [voice 9248]
    voice "ch28_s_074"
    s "S-Scouted for what?{#ch28_s_074}"

    # ハルナ：劇団よ、劇団。  [voice 1794]
    voice "ch28_ha_004"
    ha "A theater troupe, a theater troupe.{#ch28_ha_004}"

    # サイト：劇団って、あのウェザリーの劇団のこと？  [voice 9249]
    voice "ch28_s_075"
    s "A theater troupe? You mean Weatherly's?{#ch28_s_075}"

    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：違うの。
    voice "ch28_ha_005"
    ha "No. Someone from another troupe who saw that play liked me and scouted me.{#ch28_ha_005}"

    # ハルナ：この際、いい機会だから、その劇団のお世話に
    voice "ch28_ha_006"
    ha "Now's a good chance, so I've decided to join that troupe.{#ch28_ha_006}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：でもさ、劇団の世話になるってことは、
    voice "ch28_s_076"
    s "But if you join a troupe, you'll have to perform in other towns, won't you?{#ch28_s_076}"

    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：うん、そうだね。
    voice "ch28_ha_007"
    ha "Yeah. I probably won't get to see Hiraga-kun very often anymore.{#ch28_ha_007}"

    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：でもね、私は楽しみにしてるんだ。
    voice "ch28_ha_008"
    ha "But I'm looking forward to it. I get to see all sorts of towns in this world.{#ch28_ha_008}"

    # ハルナ：ひょっとすると、日本へ戻るためのきっかけ
    voice "ch28_ha_009"
    ha "Maybe I'll even find a clue to get back to Japan.{#ch28_ha_009}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：そっか、そうだよな。  [voice 9251]
    voice "ch28_s_077"
    s "I see. Yeah, that's right.{#ch28_s_077}"

    # ハルナ：だから平賀くん……。
    voice "ch28_ha_010"
    ha "So, Hiraga-kun… If you don't mind, cheer me on, okay?{#ch28_ha_010}"

    # サイト：ああ、もちろんだとも！
    voice "ch28_s_078"
    s "Of course I will! And let's both do our best to find a way back to Japan!{#ch28_s_078}"

    # ハルナ：うん！  [voice 1801]
    voice "ch28_ha_011"
    ha "Mm!{#ch28_ha_011}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     hide]
    # [BG       stage    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # サイト：なあ、ルイズ……。
    voice "ch28_s_079"
    s "Say, Louise… Why didn't Tabitha hand Haruna over to Gallia?{#ch28_s_079}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # ルイズ：……えっ？
    voice "ch28_l_010"
    l "…Eh? You let Haruna go without knowing that?{#ch28_l_010}"

    # サイト：だってさ、春奈には、
    voice "ch28_s_080"
    s "Well, it was hard to ask Haruna directly…{#ch28_s_080}"

    # サイト：タバサには、シュヴァリエとしての面子を
    voice "ch28_s_081"
    s "And I felt awful asking Tabitha—as a Chevalier, she might have lost face…{#ch28_s_081}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：どっちにだって、普通に聞けば教えてくれた
    voice "ch28_l_011"
    l "Either way, you could have just asked normally and they'd have told you…{#ch28_l_011}"

    # サイト：じゃあ、ルイズは事の顛末を知ってるのか？  [voice 9256]
    voice "ch28_s_082"
    s "Then do you know how it all turned out?{#ch28_s_082}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：まあね。  [voice 4860]
    voice "ch28_l_012"
    l "Well, yes.{#ch28_l_012}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：だったら、俺にも教えてくれよ！  [voice 9257]
    voice "ch28_s_083"
    s "Then tell me, too!{#ch28_s_083}"

    # ルイズ：タバサに直接聞けばいいじゃない？  [voice 4861]
    voice "ch28_l_013"
    l "Why don't you ask Tabitha directly?{#ch28_l_013}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：分かったよ……。
    voice "ch28_s_084"
    s "All right… I'll go ask Tabitha, like you said…{#ch28_s_084}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：……ま、待ちなさいよ。
    voice "ch28_l_014"
    l "…Wait. It'd be rude to bother Tabitha over something like that. I'll tell you myself.{#ch28_l_014}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：は、はい……。  [voice 9259]
    voice "ch28_s_085"
    s "Y-Yes…{#ch28_s_085}"

    # サイト：（まったくもう……。
    s "(Honestly… I wish you'd just tell me straight…){#ch28_s_086}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：で、どうしてタバサはガリア王国に
    voice "ch28_s_087"
    s "So—why didn't Tabitha hand Haruna over to Gallia?{#ch28_s_087}"

    # サイト：なのにタバサは、任務は達成したって
    voice "ch28_s_088"
    s "And yet Tabitha said she'd completed the mission…{#ch28_s_088}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：ああ、それね。
    voice "ch28_l_015"
    l "Ah, that. Tabitha reported to Gallia like this.{#ch28_l_015}"

    # ルイズ：突然のトリスタニアでの戦闘で、
    voice "ch28_l_016"
    l "Amid the sudden fighting in Tristain, Haruna went missing.{#ch28_l_016}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：えっ、そんな報告で向こうは納得したのか？
    voice "ch28_s_089"
    s "Eh? They bought that report? They accepted it surprisingly easily…{#ch28_s_089}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：これはわたしの想像なんだけど……。
    voice "ch28_l_017"
    l "This is just my guess… But maybe Gallia was looking for Akina the bomber.{#ch28_l_017}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：え？  [voice 9263]
    voice "ch28_s_090"
    s "Eh?{#ch28_s_090}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：聞けば、ガリア王国でも相当の被害が
    voice "ch28_l_018"
    l "Apparently Gallia suffered quite a bit, too.{#ch28_l_018}"

    # ルイズ：たぶん、人相とか、容姿とかを聞いて、
    voice "ch28_l_019"
    l "Probably—they asked for a description, and by coincidence, it matched Haruna.{#ch28_l_019}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：なんだ、そうだったんだ。
    voice "ch28_s_091"
    s "I see. So that's how it was. I thought they knew the whole mechanism…{#ch28_s_091}"

    # ルイズ：あとはいつもの通り、タバサに面倒ごとを
    voice "ch28_l_020"
    l "Besides, their main aim was probably to dump troublesome jobs on Tabitha, so they didn't care much about the result.{#ch28_l_020}"

    # サイト：そっか……。
    voice "ch28_s_092"
    s "I see… Well, at least it didn't end badly for Tabitha and Haruna…{#ch28_s_092}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：（結局のところ、春奈の別人格であるアキナは
    s "(In the end, Akina—Haruna's other personality—still seems to linger a little.){#ch28_s_093}"

    # サイト：（春奈には内緒だが、魔法の薬を飲むよう、
    s "(It's a secret from Haruna, but the Queen ordered her to take a magic potion.){#ch28_s_094}"

    # サイト：（ウェザリーはその後、行方不明のままだ。
    s "(Weatherly has been missing since then. Probably returned to Reconquista.){#ch28_s_095}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # サイト：（そんなわけで、学院から春奈が去ったあとは、
    s "(And so, after Haruna left the academy, life resumed much as before… But…){#ch28_s_096}"

    # サイト：（ひとつだけ、変わったことがあるんだ……）
    s "(There's just one thing that's changed…){#ch28_s_097}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+340, level=140, dir=2A]
    # [BG       stage    image=+23, level=200]
    $ fade_fx("id(23)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # ルイズ：もうっ！
    voice "ch28_l_021"
    l "Honestly! Why does Tabitha sit next to Saito every single day!?{#ch28_l_021}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+285, level=80]
    $ dissolve_fx("id(285)")
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     x=304, y=416]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     x=-96, y=0]
    # [SPRITE   lay6     x=304, y=416]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # タバサ：座りたいから。  [voice 15403]
    voice "ch28_t_040"
    t "Because I want to.{#ch28_t_040}"

    # ルイズ：どうせ本読んでるだけなんだから、
    voice "ch28_l_022"
    l "You're just reading a book anyway—it's not like it has to be next to Saito!{#ch28_l_022}"

    # タバサ：隣であってもいいはず。  [voice 15404]
    voice "ch28_t_041"
    t "It should be fine even next to him.{#ch28_t_041}"

    # ルイズ：う～っ、サイト！！
    voice "ch28_l_023"
    l "Ugh—Saito! Say something to Tabitha!{#ch28_l_023}"

    # サイト：言ってやれって……。
    voice "ch28_s_098"
    s "You want me to talk to her… It's not like sitting next to me is a problem, is it?{#ch28_s_098}"

    # ルイズ：よくないのっ！
    voice "ch28_l_024"
    l "It is! It makes me irritable—so it's bad!{#ch28_l_024}"

    # キュルケ：ルイズったら、馬鹿ねぇ。
    voice "ch28_k_015"
    k "You're being silly, Louise. That's called jealousy, you know?{#ch28_k_015}"

    # ルイズ：嫉妬じゃないもん……。
    voice "ch28_l_025"
    l "It's not jealousy… I'm just irritated…{#ch28_l_025}"

    # サイト：まったくもう……あのー、タバサさん？
    voice "ch28_s_099"
    s "Honestly… Um, Tabitha-san? My mistress is rather upset, so if possible…{#ch28_s_099}"

    # タバサ：嫌。  [voice 15405]
    voice "ch28_t_042"
    t "No.{#ch28_t_042}"

    # サイト：ははは、タバサさん？
    voice "ch28_s_100"
    s "Ha ha, Tabitha-san? Could this be…{#ch28_s_100}"

    # サイト：俺のそばにいたいとか？  [voice 9269]
    voice "ch28_s_101"
    s "That you want to be next to me?{#ch28_s_101}"

    # [EVENT_CG event    image=+286, level=80]
    $ dissolve_fx("id(286)")
    # タバサ：うん。  [voice 15406]
    voice "ch28_t_043"
    t "Mm.{#ch28_t_043}"

    # サイト：と言っておりますが。  [voice 9270]
    voice "ch28_s_102"
    s "She says she does…{#ch28_s_102}"

    # [EVENT_CG event    image=+285, level=80]
    $ dissolve_fx("id(285)")
    # ルイズ：言っておりますが、じゃないわよ！
    voice "ch28_l_026"
    l "'She says she does' my foot! You idiot, Saito!{#ch28_l_026}"

    # サイト：なんで俺に向かって怒るんだよっ！？  [voice 9271]
    voice "ch28_s_103"
    s "Why are you angry at me!?{#ch28_s_103}"

    # キュルケ：別にさぁ……。
    voice "ch28_k_016"
    k "Look—it's fine for Tabitha to sit next to you. She's just reading a book anyway.{#ch28_k_016}"

    # ルイズ：で、でも……。  [voice 4875]
    voice "ch28_l_027"
    l "B-But…{#ch28_l_027}"

    # キュルケ：じゃあ、タバサの代わりに……。
    voice "ch28_k_017"
    k "Then instead of Tabitha… Shall I sit next to darling and cling to him?{#ch28_k_017}"

    # ルイズ：だったら、タバサでいいわよ。  [voice 4876]
    voice "ch28_l_028"
    l "Then Tabitha's fine.{#ch28_l_028}"

    # [EVENT_CG event    image=+286, level=80]
    $ dissolve_fx("id(286)")
    # タバサ：……。
    t "…{#ch28_t_044}"

    # サイト：（あ、結構喜んでる……）
    s "(Oh—she's rather pleased…){#ch28_s_104}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [EVENT_CG event    hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # サイト：（……というわけで、ルイズの悩みの種を
    s "(…And so Tabitha, who'd added one more worry to Louise's life, was still reading as always…){#ch28_s_105}"

    # サイト：（だけど、俺のすぐそばで本を読んでる
    s "(But—watching Tabitha read right beside me, I found myself feeling oddly at ease.){#ch28_s_106}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ПРОЕКТА ====
    jump attention
    return

