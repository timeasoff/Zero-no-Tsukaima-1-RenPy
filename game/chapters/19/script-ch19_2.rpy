# Глава 19, часть 2 (сцены 750–763): поцелуй, иллюзорный флот, Уэзерби.
# Источник: ps2_source/chapters/chapter_20_小悪魔と春風の協奏曲.txt (SCENE 750-763).

label ch19_2:
    $ tndl(None)
    $ show_sprites()

label ch19_2_scene_750:

    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：それじゃみんな、手筈は分かってるわね？  [voice 6475]
    voice "ch19_l_214"
    l "So, everyone knows the plan, right?{#ch19_l_214}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：まずはルイズとキュルケが屋上をめざす……。
    voice "ch19_s_286"
    s "First, Louise and Kirche head for the rooftop… Right?{#ch19_s_286}"

    # ルイズ：そうね。
    voice "ch19_l_215"
    l "Right. You and Tabitha make your way to the headmaster's office, making sure you're noticed.{#ch19_l_215}"

    # サイト：ウェザリー達の注意をこっちに向けるため
    voice "ch19_s_287"
    s "To draw Weatherly's attention our way, yeah?{#ch19_s_287}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：そして、わたしは例の魔法を使うわ。
    voice "ch19_l_216"
    l "And I'll use that spell. It should throw the enemies in the academy into confusion.{#ch19_l_216}"

    # ルイズ：サイトは混乱に乗じて、ウェザリーと
    voice "ch19_l_217"
    l "You'll use the confusion to restrain Weatherly and Akina.{#ch19_l_217}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：ねぇ、例の魔法って何？  [voice 3342]
    voice "ch19_k_049"
    k "Hey, what is that spell?{#ch19_k_049}"

    # [SPRITE   lay1     image=+337, level=160, dir=2A]
    # ルイズ：秘密よ。  [voice 6479]
    voice "ch19_l_218"
    l "It's a secret.{#ch19_l_218}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：何それ？  [voice 3343]
    voice "ch19_k_050"
    k "What kind of secret?{#ch19_k_050}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：当然でしょ。
    voice "ch19_l_219"
    l "Obviously. To deceive the enemy, you first deceive your allies. Anyone could be listening.{#ch19_l_219}"

    # ルイズ：わたし達も失敗はしないようにするけど、
    voice "ch19_l_220"
    l "We won't fail either—but you two can't afford to fail.{#ch19_l_220}"

    # ルイズ：学院も、ハルナも、両方助けなくちゃ
    voice "ch19_l_221"
    l "We have to save both the academy and Haruna.{#ch19_l_221}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # タバサ：責任重大。  [voice 15611]
    voice "ch19_t_034"
    t "Heavy responsibility.{#ch19_t_034}"

    # サイト：よし、それじゃ行くぞ。  [voice 11956]
    voice "ch19_s_288"
    s "All right, let's go.{#ch19_s_288}"

    # タバサ：うん。  [voice 15612]
    voice "ch19_t_035"
    t "Mm.{#ch19_t_035}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 751
    jump ch19_2_scene_751

label ch19_2_scene_751:

    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # ルイズ：あ、あの……。
    voice "ch19_l_222"
    l "U-Um… Wait, Saito.{#ch19_l_222}"

    # サイト：なんだよ。
    voice "ch19_s_289"
    s "What is it? Anything left undecided? Something you don't understand?{#ch19_s_289}"

    # ルイズ：そ、その……。
    voice "ch19_l_223"
    l "T-That is… Are you all right?{#ch19_l_223}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：へ？  [voice 11958]
    voice "ch19_s_290"
    s "Huh?{#ch19_s_290}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：わ、わたしとキュルケは屋上まで
    voice "ch19_l_224"
    l "W-We only have to reach the rooftop…{#ch19_l_224}"

    # ルイズ：魔法さえ成功してしまえば
    voice "ch19_l_225"
    l "If the spell works, we can just hide somewhere afterwards.{#ch19_l_225}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：あんたとタバサは、レコン・キスタの兵士や
    voice "ch19_l_226"
    l "But you and Tabitha have to fight Reconquista's soldiers and Weatherly, don't you?{#ch19_l_226}"

    # ルイズ：別に、タバサがいるし、デルフリンガーも
    voice "ch19_l_227"
    l "I mean, Tabitha's there, and there's Derflinger too… But still…{#ch19_l_227}"

    menu:
        "Leave it to me.{#ch19_2_c_751_1}":
            jump ch19_2_scene_752
        "Don't you trust me?{#ch19_2_c_751_2}":
            jump ch19_2_scene_753
        "I'm more worried about you, Louise.{#ch19_2_c_751_3}":
            jump ch19_2_scene_754

label ch19_2_scene_752:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [SPRITE   lay5     image=+436, level=160, dir=2B]
    # サイト：心配すんな。
    voice "ch19_s_291"
    s "Don't worry. Leave it to me.{#ch19_s_291}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：カッコつけてて、やられるんじゃないわよ。
    voice "ch19_l_228"
    l "Don't act cool and get yourself hurt. You're always missing the important point…{#ch19_l_228}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：ホント心配。  [voice 6490]
    voice "ch19_l_229"
    l "I really am worried.{#ch19_l_229}"

    # → next scene 755
    jump ch19_2_scene_755

label ch19_2_scene_753:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：なんだよ、俺ってそんなに信用されてないのか？
    voice "ch19_s_292"
    s "What's that? Don't you trust me? That hurts a little.{#ch19_s_292}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：ち、違うっ……。
    voice "ch19_l_230"
    l "N-No, that's not it… I do trust you, I just…{#ch19_l_230}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：あらルイズ、もしかしてダーリンのことが
    voice "ch19_k_051"
    k "Oh, Louise. Are you worried about darling?{#ch19_k_051}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：な、なによ……。
    voice "ch19_l_231"
    l "W-What… It's only natural to worry about your own familiar.{#ch19_l_231}"

    # [SPRITE   lay6     hide]
    # → next scene 755
    jump ch19_2_scene_755

label ch19_2_scene_754:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：なに言ってんだよルイズ。
    voice "ch19_s_293"
    s "What are you talking about, Louise? I'm more worried about you.{#ch19_s_293}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：ご、ご、ご主人様に向かって、
    voice "ch19_l_232"
    l "Wh-What are you saying to your mistress, you familiar!{#ch19_l_232}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：あらルイズ、ダーリンに心配されて
    voice "ch19_k_052"
    k "Oh, Louise. Are you a little happy that darling is worrying about you?{#ch19_k_052}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # タバサ：動揺。  [voice 15613]
    voice "ch19_t_036"
    t "Agitation.{#ch19_t_036}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：ち、違うわよ！
    voice "ch19_l_233"
    l "N-No I'm not! Just because the master showed a little concern for his familiar doesn't mean I'm pleased!{#ch19_l_233}"

    # [LAYER    lay0     hide]
    # → next scene 755
    jump ch19_2_scene_755

label ch19_2_scene_755:

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # [SPRITE   lay5     image=+436, level=160, dir=2B]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [SPRITE   lay5     image=+436, level=160, dir=2B]
    # サイト：大丈夫だよ。
    voice "ch19_s_294"
    s "It'll be fine. I'm sure we'll manage somehow.{#ch19_s_294}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：どうしてそう適当なのよ、あんたは。
    voice "ch19_l_234"
    l "Why are you so casual about it? You're always like this…{#ch19_l_234}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：そもそも俺って伝説の使い魔ガンダールヴ
    voice "ch19_s_295"
    s "After all, I'm the legendary familiar Gandalfr, right?{#ch19_s_295}"

    # サイト：一番しっくりくる武器で、
    voice "ch19_s_296"
    s "The weapon that suits me best, and it absorbs enemy magic too. I won't go down that easily.{#ch19_s_296}"

    # [SPRITE   lay19    image=+942, level=153, dir=1A]
    # [SPRITE   lay1     level=156]
    # [SPRITE   lay5     level=157]
    # デルフリンガー：おいおい、うれしいこと言ってくれる
    voice "ch19_d_032"
    d "Hey now, that's nice to hear. I'll be fired up today, you bet.{#ch19_d_032}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     image=+440, level=157, dir=2B]
    # サイト：今日はって、いつも張り切ってくれよ……。  [voice 11965]
    voice "ch19_s_297"
    s "Today—come on, be fired up every day…{#ch19_s_297}"

    # [SPRITE   lay1     image=+306, level=156, dir=1A]
    # ルイズ：なによ、なによ。
    voice "ch19_l_235"
    l "What is it? You think you can do everything on your own?{#ch19_l_235}"

    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # サイト：ル、ルイズ？  [voice 11966]
    voice "ch19_s_298"
    s "L-Louise?{#ch19_s_298}"

    # ルイズ：あんたなんか使い魔のくせに、
    voice "ch19_l_236"
    l "You're a familiar, yet you always ignore me and run off on your own, and then you get into danger…{#ch19_l_236}"

    # [SPRITE   lay1     image=+310, level=156, dir=1A]
    # ルイズ：ほんと、バカなんだから！  [voice 6498]
    voice "ch19_l_237"
    l "Honestly, you're such an idiot!{#ch19_l_237}"

    # → next scene 756
    jump ch19_2_scene_756

    # → next scene 757
    jump ch19_2_scene_757

label ch19_2_scene_756:

    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # [SPRITE   lay1     image=+310, level=156, dir=1A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [SPRITE   lay1     image=+343, level=156, dir=2A]
    # ルイズ：あんたなんか、あんたなんかっ……。  [voice 6499]
    voice "ch19_l_238"
    l "You, you…!{#ch19_l_238}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+212, level=80]
    $ dissolve_fx("id(212)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # サイト：わ、わぷっ！？  [voice 11967]
    voice "ch19_s_299"
    s "W-Wah!?{#ch19_s_299}"

    # キュルケ：あらまぁ。  [voice 3346]
    voice "ch19_k_053"
    k "Oh my.{#ch19_k_053}"

    # タバサ：……。
    t "…{#ch19_t_037}"

    # サイト：（え、えっと……なんだか俺の唇にやーらかい
    s "(E-Er… Something soft just touched my lips…){#ch19_s_300}"

    # ルイズ：んっ……。  [voice 6500]
    voice "ch19_l_239"
    l "Mm…{#ch19_l_239}"

    # サイト：（ひょっとしてこれはアレか？
    s "(Could this be it? Am I being kissed by Louise?){#ch19_s_301}"

    # サイト：え、えぇっ？
    voice "ch19_s_302"
    s "E-Eh? You… You kissed me…!?{#ch19_s_302}"

    # ルイズ：あ、あのっ……こ、これっ、これはっ……！
    voice "ch19_l_240"
    l "T-That was… This was…! Ka-ka-ka-ka… D-Don't get the wrong idea!{#ch19_l_240}"

    # ルイズ：あんたは、ほんとにまったくご主人様の
    voice "ch19_l_241"
    l "You really never listen to your mistress…{#ch19_l_241}"

    # ルイズ：わたしの気持ちを無視してばっかりだからっ！  [voice 6503]
    voice "ch19_l_242"
    l "You always ignore my feelings!{#ch19_l_242}"

    # ルイズ：ちゃんとわたしの言うこと聞くように、
    voice "ch19_l_243"
    l "I just renewed the contract so that you'd listen to me properly! That's it—a contract, a contract!!{#ch19_l_243}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [TRANS trans("crossfade", 1000)]
    # [LAYER    lay0     image=+629, level=155, dir=2A]
    # [SPRITE   lay6     image=+717, level=154, dir=2A]
    # タバサ：契約。  [voice 15614]
    voice "ch19_t_038"
    t "Contract.{#ch19_t_038}"

    # キュルケ：契約、ねぇ……。
    voice "ch19_k_054"
    k "Contract, is it… Hmm.{#ch19_k_054}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+343, level=156, dir=2A]
    # ルイズ：召喚の契約じゃないわよ。
    voice "ch19_l_244"
    l "Not a summoning contract. It's a contract that you'll come back properly!{#ch19_l_244}"

    # キュルケ：ま、そういうことにしておきましょ。
    voice "ch19_k_055"
    k "Well, let's leave it at that. Right, darling?{#ch19_k_055}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+442, level=157, dir=2B]
    # サイト：……。  [voice 11969]
    voice "ch19_s_303"
    s "…{#ch19_s_303}"

    # サイト：（いかん、今頃になって胸がバクバクしてきた。
    s "(No good. My heart started pounding now of all times. A kiss, huh…){#ch19_s_304}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+588, level=155, dir=1A]
    # タバサ：サイト、顔が真っ赤。  [voice 15615]
    voice "ch19_t_039"
    t "Saito, your face is bright red.{#ch19_t_039}"

    # [SPRITE   lay5     level=157]
    # [LAYER    lay0     level=155]
    # [SPRITE   lay19    image=+948, level=153, dir=1A]
    # デルフリンガー：おぅおぅ、若いねぇ相棒。
    voice "ch19_d_033"
    d "Ooh, you're young, partner. But the rest comes after the operation.{#ch19_d_033}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # サイト：あ、あぁ。
    voice "ch19_s_305"
    s "A-Ah. I know.{#ch19_s_305}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+335, level=156, dir=2A]
    # ルイズ：い、行くわよ、キュルケ。  [voice 6506]
    voice "ch19_l_245"
    l "L-Let's go, Kirche.{#ch19_l_245}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=154, dir=1A]
    # キュルケ：はいはい。
    voice "ch19_k_056"
    k "Yes, yes. See you later, darling, Tabitha.{#ch19_k_056}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    hide]
    # → next scene 759
    jump ch19_2_scene_759

label ch19_2_scene_757:

    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # [SPRITE   lay1     image=+310, level=156, dir=1A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [SPRITE   lay1     image=+339, level=156, dir=2A]
    # ルイズ：あんたは生意気でご主人様の言うことを
    voice "ch19_l_246"
    l "You're a cocky familiar who doesn't listen to your mistress!{#ch19_l_246}"

    # ルイズ：だから、学院が元に戻って王都も助かったら！
    voice "ch19_l_247"
    l "So once the academy is back to normal and the capital is saved, I'm going to re-educate you, absolutely!{#ch19_l_247}"

    # [SPRITE   lay1     image=+310, level=156, dir=1A]
    # ルイズ：だからそれまで、やられんじゃないわよ！  [voice 6509]
    voice "ch19_l_248"
    l "So until then, don't get yourself hurt!{#ch19_l_248}"

    # [SPRITE   lay1     image=+306, level=156, dir=1A]
    # ルイズ：いい？
    voice "ch19_l_249"
    l "Got it? If you break even one of my orders, it's punishment!{#ch19_l_249}"

    # [SPRITE   lay5     image=+438, level=157, dir=2B]
    # サイト：お、おぅ……。
    voice "ch19_s_306"
    s "O-Oh… Got it.{#ch19_s_306}"

    # [SPRITE   lay1     image=+335, level=156, dir=2A]
    # ルイズ：分かればいいのよ。
    voice "ch19_l_250"
    l "As long as you understand. Don't ever forget those words. Let's go, Kirche.{#ch19_l_250}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+715, level=154, dir=2A]
    # キュルケ：はいはい。
    voice "ch19_k_057"
    k "Yes, yes. Well… thanks for the meal.{#ch19_k_057}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+588, level=155, dir=1A]
    # [SPRITE   lay5     image=+401, level=157, dir=1B]
    # タバサ：サイト、わたし達も。  [voice 15616]
    voice "ch19_t_040"
    t "Saito, let's go too.{#ch19_t_040}"

    # サイト：う、うん。  [voice 11972]
    voice "ch19_s_307"
    s "O-Okay.{#ch19_s_307}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=154, dir=1A]
    # キュルケ：それじゃね、タバサ。  [voice 3351]
    voice "ch19_k_058"
    k "See you, Tabitha.{#ch19_k_058}"

    # タバサ：（こくっ）  [voice 15617]
    voice "ch19_t_041"
    t "(Gulp){#ch19_t_041}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    hide]
    # → next scene 759
    jump ch19_2_scene_759

label ch19_2_scene_758:

    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    hide]
    # → next scene 759
    jump ch19_2_scene_759

label ch19_2_scene_759:

    # [BG       stage    image=+20, level=200]
    $ fade_fx("id(20)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # タバサ：こっち。  [voice 15618]
    voice "ch19_t_042"
    t "This way.{#ch19_t_042}"

    # サイト：お、おう。  [voice 11973]
    voice "ch19_s_308"
    s "O-Okay.{#ch19_s_308}"

    # サイト：（ルイズ、大丈夫かなぁ）
    s "(I wonder if Louise is all right…){#ch19_s_309}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # キュルケ：ねぇルイズ？  [voice 3352]
    voice "ch19_k_059"
    k "Hey, Louise?{#ch19_k_059}"

    # ルイズ：な、なによ？  [voice 6512]
    voice "ch19_l_251"
    l "W-What now?{#ch19_l_251}"

    # キュルケ：さっきのあれ……本気だったの？  [voice 3353]
    voice "ch19_k_060"
    k "That thing earlier… were you serious?{#ch19_k_060}"

    # ルイズ：え……。
    voice "ch19_l_252"
    l "Eh… What thing?{#ch19_l_252}"

    # → next scene 760
    jump ch19_2_scene_760

    # → next scene 761
    jump ch19_2_scene_761

label ch19_2_scene_760:

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：とぼけないで。
    voice "ch19_k_061"
    k "Don't play dumb. You kissed Saito, didn't you?{#ch19_k_061}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：うぐ。  [voice 6514]
    voice "ch19_l_253"
    l "Ugh.{#ch19_l_253}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：まさか貴族の、しかもヴァリエールの
    voice "ch19_k_062"
    k "I can't believe a noble—and the daughter of a Valliere, no less—doing that to a commoner…{#ch19_k_062}"

    # キュルケ：まさかとは思うけど、
    voice "ch19_k_063"
    k "I hate to say it, but were you serious about it?{#ch19_k_063}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：そ、そんなこと、あんたには関係ないでしょう！  [voice 6515]
    voice "ch19_l_254"
    l "T-That's none of your business!{#ch19_l_254}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：関係あるのよねぇ。
    voice "ch19_k_064"
    k "It does concern me. Saito is my darling, after all.{#ch19_k_064}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：か、勝手に決めないでよっ！  [voice 6516]
    voice "ch19_l_255"
    l "D-Don't decide that on your own!{#ch19_l_255}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：んー、でもあなたが本気っていうなら、
    voice "ch19_k_065"
    k "Mm, but if you're serious, I'll have to rethink my position too… So, are you serious?{#ch19_k_065}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：あぁもう、うるさいうるさいっ！  [voice 6517]
    voice "ch19_l_256"
    l "Oh, shut up, shut up!{#ch19_l_256}"

    # → next scene 762
    jump ch19_2_scene_762

label ch19_2_scene_761:

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：あら、あたしはばっちり聞いてたわよ。
    voice "ch19_k_066"
    k "Oh, I heard you perfectly. You declared you'd re-educate darling.{#ch19_k_066}"

    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：ダーリンも哀れよねぇ、ルイズみたいな
    voice "ch19_k_067"
    k "Poor darling, stuck with a brutal mistress like Louise.{#ch19_k_067}"

    # キュルケ：どうせルイズのことだから、
    voice "ch19_k_068"
    k "You know what Louise is like. She'll throw darling out of her room, skip his meals, and mistreat him.{#ch19_k_068}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：あぁ、かわいそうなダーリン……。  [voice 3362]
    voice "ch19_k_069"
    k "Ah, poor darling…{#ch19_k_069}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：な、なによ……。
    voice "ch19_l_257"
    l "What… Saito is my familiar; I can do whatever I want with him!{#ch19_l_257}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ま、いいけどね。  [voice 3363]
    voice "ch19_k_070"
    k "Well, fine.{#ch19_k_070}"

    # [SPRITE   lay6     image=+684, level=160, dir=1A]
    # キュルケ：あなたがダーリンを虐待すればするほど、
    voice "ch19_k_071"
    k "The more you mistreat darling, the more likely he'll become only mine.{#ch19_k_071}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：な、なっ……！
    voice "ch19_l_258"
    l "W-What!? You're a noble, flirting with a commoner—aren't you ashamed?{#ch19_l_258}"

    # [SPRITE   lay6     image=+684, level=160, dir=1A]
    # キュルケ：別に愛に身分なんて、関係ないわ。
    voice "ch19_k_072"
    k "Love knows no rank. If anything, I'd even take a noble title for darling.{#ch19_k_072}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：そ、そんなのだめ！
    voice "ch19_l_259"
    l "T-That's no good! Saito is only my familiar; you can't take him!{#ch19_l_259}"

    # → next scene 762
    jump ch19_2_scene_762

label ch19_2_scene_762:

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay11    image=+1105, level=160, dir=1A]
    # 魔導士：……。
    mage "…{#ch19_mage_001}"

    # [SPRITE   lay11    hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：あーあー。
    voice "ch19_k_073"
    k "Oh dear. You made such a fuss that the enemy gathered.{#ch19_k_073}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：な、なに言ってるのよ！
    voice "ch19_l_260"
    l "What are you talking about! It's because Kirche said something strange!{#ch19_l_260}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：もういい！
    voice "ch19_l_261"
    l "Enough! Everyone, finish them off!{#ch19_l_261}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：おお、怖い怖い。  [voice 3367]
    voice "ch19_k_074"
    k "Ooh, scary, scary.{#ch19_k_074}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 763
    jump ch19_2_scene_763

label ch19_2_scene_763:

    # [BG       stage    image=+81, level=200]
    $ fade_fx("id(81)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # ルイズ：なんとか、やっつけたわね。  [voice 6523]
    voice "ch19_l_262"
    l "We managed to beat them, didn't we.{#ch19_l_262}"

    # キュルケ：時間が無いみたい。
    voice "ch19_k_075"
    k "We're short on time. Could you show us that spell of yours already?{#ch19_k_075}"

    # ルイズ：分かったわ。  [voice 6524]
    voice "ch19_l_263"
    l "I know.{#ch19_l_263}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+140, level=80]
    $ dissolve_fx("id(140)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # キュルケ：ルイズ、まだ？  [voice 3369]
    voice "ch19_k_076"
    k "Louise, still not ready?{#ch19_k_076}"

    # ルイズ：今詠唱が完了したところよ。
    voice "ch19_l_264"
    l "I've just finished the incantation. Come forth, that which is not here… Be as though you were here.{#ch19_l_264}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # ルイズ：イリュージョン！！  [voice 6526]
    voice "ch19_l_265"
    l "Illusion!!{#ch19_l_265}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+141, level=80]
    $ dissolve_fx("id(141)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # キュルケ：な……。
    voice "ch19_k_077"
    k "Wha… Such a thing!{#ch19_k_077}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [TRANS trans("crossfade", 1000)]
    # [LAYER    lay0     image=+623, level=160, dir=2A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # タバサ：成功みたい。  [voice 15619]
    voice "ch19_t_043"
    t "Looks like it worked.{#ch19_t_043}"

    # サイト：え……！？  [voice 11974]
    voice "ch19_s_310"
    s "Eh…!?{#ch19_s_310}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+141, level=80]
    $ dissolve_fx("id(141)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：（その時俺は、我が目を疑った。
    s "(At that moment, I doubted my own eyes. Dozens of aerial ships bearing Tristain's crest appeared in the sky in an instant.){#ch19_s_311}"

    # サイト：（ルイズの虚無の魔法は、見事に成功したのだ）
    s "(Louise's Void magic had succeeded perfectly.){#ch19_s_312}"

    # サイト：そうか、ルイズのやつが使うって言ってたのは
    voice "ch19_s_313"
    s "So that's what she meant by the spell she'd use…{#ch19_s_313}"

    # サイト：さすがはルイズだよ、うん。
    voice "ch19_s_314"
    s "As expected of Louise. She really is my mistress!{#ch19_s_314}"

    # タバサ：わたし達も急がないと。  [voice 15620]
    voice "ch19_t_044"
    t "We need to hurry too.{#ch19_t_044}"

    # サイト：うん、学院長室はもう目の前だ。
    voice "ch19_s_315"
    s "Right. The headmaster's office is right in front of us. Shall we go in one rush?{#ch19_s_315}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+29, level=200]
    $ fade_fx("id(29)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # ウェザリー：な……なんだ、あの大艦隊は！
    voice "ch19_w_001"
    w "Wh-What is that huge fleet! Where did so many…{#ch19_w_001}"

    # アキナ：そんな、情報にありません。  [voice 91]
    voice "ch19_ak_001"
    ak "That's not in the data.{#ch19_ak_001}"

    # アキナ：ウェザリー様、兵士達が浮き足立ってます！
    voice "ch19_ak_002"
    ak "Weatherly-sama, the soldiers are panicking! They're leaving their posts and running around!{#ch19_ak_002}"

    # ウェザリー：ここで混乱しては敵の思うツボよ。
    voice "ch19_w_002"
    w "Panicking here plays right into the enemy's hands. Tell them to restore formation at once.{#ch19_w_002}"

    # アキナ：はい！  [voice 93]
    voice "ch19_ak_003"
    ak "Yes!{#ch19_ak_003}"

    # ウェザリー：一体誰が、こんなことを。
    voice "ch19_w_003"
    w "Who could have done this… Don't tell me Tristain has been retaken?{#ch19_w_003}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay21    hide]
    # [LAYER    lay0     image=+658, level=160, dir=3A]
    # [SPRITE   lay5     image=+471, level=160, dir=3B]
    # ウェザリー：お、おまえ達はっ……！  [voice 16026]
    voice "ch19_w_004"
    w "Y-You people…!{#ch19_w_004}"

    # アキナ：サ、サイトっ……！？  [voice 94]
    voice "ch19_ak_004"
    ak "S-Saito…!?{#ch19_ak_004}"

    # サイト：ウェザリー、それにアキナ。
    voice "ch19_s_316"
    s "Weatherly. And Akina. We've come to demand you return our academy and Haruna.{#ch19_s_316}"

    # → next scene 764
    jump ch19_3

    # ==== КОНЕЦ ЧАСТИ 2 ====
    jump ch19_3
    return

