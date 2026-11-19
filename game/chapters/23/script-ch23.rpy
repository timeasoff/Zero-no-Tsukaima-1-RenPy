# Глава 23, часть 1 (сцены 849–867): Zero Fighter разрушен, оберег Сиэсты.
# Источник: ps2_source/chapters/chapter_24_沈黙の応援.txt (SCENE 849-867).

label ch23:
    $ tndl(None)
    # [TITLE] титульная карточка → overlay_screen (K=20)
    call overlay_screen("overlay", "Chapter Twenty-Three: 'Silent Support'{#ch23_title}", isUseBlur=False, text_mode="black") from _call_overlay_screen_20
    pause(2)
    $ show_sprites(None)

label ch23_1_scene_849:

    # [TITLE title("沈黙の応援")]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1164, level=200]
    $ fade_fx("id(1164)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [SE       se0      play=+69]
    # サイト：……。  [voice 12262]
    voice "ch23_s_001"
    s "…{#ch23_s_001}"

    # ルイズ：サイトっ！  [voice 6665]
    voice "ch23_l_001"
    l "Saito!{#ch23_l_001}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+307, level=140, dir=1A]
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # ルイズ：サイトったら……。
    voice "ch23_l_002"
    l "Saito… Wake up already!{#ch23_l_002}"

    # サイト：……っ！？  [voice 12263]
    voice "ch23_s_002"
    s "…!?{#ch23_s_002}"

    # サイト：（し、しまったっ！！
    s "(Oops!! Siesta isn't here anymore—and I overslept!){#ch23_s_003}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：グズグズしてる暇なんてないんだからっ！！  [voice 6667]
    voice "ch23_l_003"
    l "There's no time for dawdling!!{#ch23_l_003}"

    # サイト：（つまり今、こうしてルイズが俺のことを
    s "(Which means… right now, Louise is waking me up…!?){#ch23_s_004}"

    # サイト：（盛大なるお仕置きの予感！？
    s "(A grand punishment awaits!? Bad!){#ch23_s_005}"

    menu:
        "Sorry, Louise{#ch23_1_c_849_1}":
            jump ch23_1_scene_850
        "I feel a bit sluggish{#ch23_1_c_849_2}":
            jump ch23_1_scene_851
        "Hiraga Saito is out{#ch23_1_c_849_3}":
            jump ch23_1_scene_852

label ch23_1_scene_850:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：ご、ごめんルイズ！！
    voice "ch23_s_006"
    s "S-Sorry, Louise! I apologize for oversleeping, so please, just this once, let it go!!{#ch23_s_006}"

    # サイト：わたくしめにお仕置きしてる暇があったら、
    voice "ch23_s_007"
    s "If you have time to punish me, you should be at class right now…{#ch23_s_007}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：お仕置きなんて後っ！
    voice "ch23_l_004"
    l "Punishment later! This is no time for that!!{#ch23_l_004}"

    # [SPRITE   lay5     image=+451, level=160, dir=2C]
    # サイト：……えっ？  [voice 12266]
    voice "ch23_s_008"
    s "…Eh?{#ch23_s_008}"

    # → next scene 853
    jump ch23_1_scene_853

label ch23_1_scene_851:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+418, level=160, dir=1C]
    # サイト：うううっ、おはようルイズっ。
    voice "ch23_s_009"
    s "Ugh, good morning, Louise. I feel a bit sluggish today. Ah ha ha… Cough, cough… Ugh.{#ch23_s_009}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：えっ！？
    voice "ch23_l_005"
    l "Eh!? Wait a second. Do you have a fever?{#ch23_l_005}"

    # ルイズ：ん……熱はないみたいだけど。
    voice "ch23_l_006"
    l "Hmm… No fever. What terrible timing… What should we do…{#ch23_l_006}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：しっかりしてよ、もぉ……。  [voice 6671]
    voice "ch23_l_007"
    l "Pull yourself together, honestly…{#ch23_l_007}"

    # → next scene 853
    jump ch23_1_scene_853

label ch23_1_scene_852:

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+447, level=160, dir=2C]
    # サイト：ひ、平賀　才人は留守でーす。  [voice 12268]
    voice "ch23_s_010"
    s "H-Hiraga Saito is out.{#ch23_s_010}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：何バカなことやってるのよっ！
    voice "ch23_l_008"
    l "What nonsense are you spouting! This is serious!{#ch23_l_008}"

    # → next scene 853
    jump ch23_1_scene_853

label ch23_1_scene_853:

    # [SPRITE   lay5     image=+451, level=160, dir=2C]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：姫さまのお城が爆弾使いに襲われてるのよ！  [voice 6673]
    voice "ch23_l_009"
    l "The princess's castle has been attacked by the bomber!{#ch23_l_009}"

    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # サイト：マジでっ！？  [voice 12269]
    voice "ch23_s_011"
    s "Seriously!?{#ch23_s_011}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：今すぐ出発よっ。  [voice 6674]
    voice "ch23_l_010"
    l "We're leaving right now.{#ch23_l_010}"

    # [SPRITE   lay5     image=+412, level=160, dir=1C]
    # サイト：オーケー、１分１秒を争う事態なら、
    voice "ch23_s_012"
    s "All right—if every second counts, let's take the Zero Fighter and fly there in a flash!{#ch23_s_012}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：それが、ダメなのっ！  [voice 6675]
    voice "ch23_l_011"
    l "That's the problem!{#ch23_l_011}"

    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # サイト：なんでさっ！？  [voice 12271]
    voice "ch23_s_013"
    s "Why not!?{#ch23_s_013}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：爆弾使いの攻撃で、ゼロ戦も餌食に……。
    voice "ch23_l_012"
    l "The bomber's attack made the Zero Fighter prey too… It looks like it was destroyed this morning.{#ch23_l_012}"

    # [SPRITE   lay5     image=+416, level=160, dir=1C]
    # サイト：……くそぉ！！  [voice 12272]
    voice "ch23_s_014"
    s "…Damn it!!{#ch23_s_014}"

    # [SE       se0      play=+57]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ちょっとぉ！！
    voice "ch23_l_013"
    l "Hey!! Where are you going!? Wait!!{#ch23_l_013}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 854
    jump ch23_1_scene_854

label ch23_1_scene_854:

    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # サイト：マジかよ……。
    voice "ch23_s_015"
    s "No way… The right wing is blown off… There's no way this can fly…{#ch23_s_015}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+227, level=80]
    $ dissolve_fx("id(227)")
    # [TRANS trans("crossfade", 1000)]
    # シエスタ：サイトさんっ！  [voice 14993]
    voice "ch23_si_001"
    si "Saito-san!{#ch23_si_001}"

    # シエスタ：ひいおじいちゃんの形見がっ……。
    voice "ch23_si_002"
    si "My great-grandfather's keepsake… To think a single bomb could tear metal wings this strong…{#ch23_si_002}"

    # サイト：ああ、確かに。
    voice "ch23_s_016"
    s "Ah, indeed. That's more destructive than I thought.{#ch23_s_016}"

    # サイト：急がないと。
    voice "ch23_s_017"
    s "We have to hurry. Tristain's castle and the princess are in danger.{#ch23_s_017}"

    # シエスタ：えっ……、サイトさんっ！？
    voice "ch23_si_003"
    si "Eh… Saito-san!? Surely you're not going to the castle!?{#ch23_si_003}"

    # サイト：ああ、ルイズも呼ばれてるし、
    voice "ch23_s_018"
    s "Yeah. Louise has been called, too—I have to go with her…{#ch23_s_018}"

    # シエスタ：ダメですサイトさんっ！！
    voice "ch23_si_004"
    si "No, Saito-san!! You must not go to Tristain's castle!!{#ch23_si_004}"

    # サイト：そうはいかないよ、シエスタ。
    voice "ch23_s_019"
    s "I can't do that, Siesta. I'm Louise's familiar.{#ch23_s_019}"

    # サイト：ルイズはお姫さまを助けに行きたがってる。
    voice "ch23_s_020"
    s "Louise wants to save the princess. So I have to go with her and protect my mistress.{#ch23_s_020}"

    # シエスタ：でも、そんなの……。
    voice "ch23_si_005"
    si "But… they're too strong. This is reckless!!{#ch23_si_005}"

    # シエスタ：いくらサイトさんが、ミス・ヴァリエールの
    voice "ch23_si_006"
    si "Even if you are Miss Valliere's familiar…{#ch23_si_006}"

    # シエスタ：こんなに恐ろしい爆弾を使う人達を
    voice "ch23_si_007"
    si "Fighting people who use such terrible bombs is far too reckless!!{#ch23_si_007}"

    # シエスタ：もし、この爆弾に巻き込まれてしまったら、
    voice "ch23_si_008"
    si "If you get caught up in that blast, Saito-san, you too…{#ch23_si_008}"

    # シエスタ：そんなのイヤですっ！！
    voice "ch23_si_009"
    si "No! I hate it! The thought of losing you… Just thinking about it…{#ch23_si_009}"

    # シエスタ：だから……。
    voice "ch23_si_010"
    si "So… please don't go!{#ch23_si_010}"

    # サイト：シエスタ……。  [voice 12279]
    voice "ch23_s_021"
    s "Siesta…{#ch23_s_021}"

    # [SPRITE   lay2     hide]
    # シエスタ：お城にはちゃんとした兵士の方がいますし、
    voice "ch23_si_011"
    si "The castle has proper soldiers, and lots of fine nobles, too…{#ch23_si_011}"

    # シエスタ：なのに、どうして、貴族でもなんでもない
    voice "ch23_si_012"
    si "So why must you—who are neither noble nor anything—fight? The world is full of strange things.{#ch23_si_012}"

    # シエスタ：サイトさん、お願い……。
    voice "ch23_si_013"
    si "Saito-san, please… Don't go…{#ch23_si_013}"

    # サイト：ありがとう、シエスタ。
    voice "ch23_s_022"
    s "Thank you, Siesta. Worrying about me this much… I'm really happy.{#ch23_s_022}"

    # シエスタ：じゃあ……。  [voice 15006]
    voice "ch23_si_014"
    si "Then…{#ch23_si_014}"

    menu:
        "I'll definitely come back{#ch23_1_c_854_1}":
            jump ch23_1_scene_855
        "Fight to protect what matters{#ch23_1_c_854_2}":
            jump ch23_1_scene_856
        "I can't run away{#ch23_1_c_854_3}":
            jump ch23_1_scene_857

label ch23_1_scene_855:

    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [EVENT_CG event    image=+227, level=80]
    $ dissolve_fx("id(227)")
    # サイト：大丈夫、無茶はしないよ。  [voice 12281]
    voice "ch23_s_023"
    s "Don't worry. I won't do anything reckless.{#ch23_s_023}"

    # シエスタ：え……？  [voice 15007]
    voice "ch23_si_015"
    si "Eh…?{#ch23_si_015}"

    # サイト：俺は、ルイズを守る使い魔だ。
    voice "ch23_s_024"
    s "I'm the familiar who protects Louise. I'll never throw my life away fighting for rank or honor.{#ch23_s_024}"

    # サイト：俺はルイズを連れて、必ずここへ帰ってくる。
    voice "ch23_s_025"
    s "I'll bring Louise back here, safe and sound. So pray for us and wait here, Siesta.{#ch23_s_025}"

    # → next scene 858
    jump ch23_1_scene_858

label ch23_1_scene_856:

    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [EVENT_CG event    image=+227, level=80]
    $ dissolve_fx("id(227)")
    # サイト：ごめん、シエスタ。
    voice "ch23_s_026"
    s "Sorry, Siesta. I'm… going to fight the bomber. To protect the people I care about.{#ch23_s_026}"

    # シエスタ：そんな……。  [voice 15008]
    voice "ch23_si_016"
    si "No…{#ch23_si_016}"

    # サイト：俺はそれを義務でやろうってワケじゃない。
    voice "ch23_s_027"
    s "I'm not doing it out of duty. I've decided to protect them of my own free will. So…{#ch23_s_027}"

    # → next scene 858
    jump ch23_1_scene_858

label ch23_1_scene_857:

    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [EVENT_CG event    image=+227, level=80]
    $ dissolve_fx("id(227)")
    # サイト：俺だって戦いは怖いよ。  [voice 12286]
    voice "ch23_s_028"
    s "I'm scared of fighting, too.{#ch23_s_028}"

    # シエスタ：それじゃあ！  [voice 15009]
    voice "ch23_si_017"
    si "Then!{#ch23_si_017}"

    # サイト：でも、さ。
    voice "ch23_s_029"
    s "But, see—I can't run away here. If I run away here…{#ch23_s_029}"

    # サイト：俺、ずっと逃げを選ぶ人生になっちゃう。
    voice "ch23_s_030"
    s "…I'll spend the rest of my life running. That's… No, that's why. That's why I'm going.{#ch23_s_030}"

    # → next scene 858
    jump ch23_1_scene_858

label ch23_1_scene_858:

    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [EVENT_CG event    image=+227, level=80]
    $ dissolve_fx("id(227)")
    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # → next scene 859
    jump ch23_1_scene_859

label ch23_1_scene_859:

    # [EVENT_CG event    image=+224, level=80]
    $ dissolve_fx("id(224)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # シエスタ：分かりました……。
    voice "ch23_si_018"
    si "I understand… Then at least, please take this charm with you…{#ch23_si_018}"

    # サイト：お守り？  [voice 12290]
    voice "ch23_s_031"
    s "A charm?{#ch23_s_031}"

    # シエスタ：はいっ……これですっ。  [voice 15013]
    voice "ch23_si_019"
    si "Yes… This one.{#ch23_si_019}"

    # サイト：このお守りは……？
    voice "ch23_s_032"
    s "This charm is… Could it be…{#ch23_s_032}"

    # シエスタ：はい、ひいおじいちゃんの形見です
    voice "ch23_si_020"
    si "Yes, it's my great-grandfather's keepsake. They say if you wear it, danger will avoid you.{#ch23_si_020}"

    # シエスタ：だから、わたしの祈りをこめたこの
    voice "ch23_si_021"
    si "So please, at least wear this charm with my prayers in it…{#ch23_si_021}"

    menu:
        "I'll return it first thing{#ch23_1_c_859_1}":
            jump ch23_1_scene_860
        "With this, I'm fine{#ch23_1_c_859_2}":
            jump ch23_1_scene_861
        "I feel stronger{#ch23_1_c_859_3}":
            jump ch23_1_scene_862

label ch23_1_scene_860:

    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [EVENT_CG event    image=+224, level=80]
    $ dissolve_fx("id(224)")
    # サイト：うん、ありがとう。
    voice "ch23_s_033"
    s "Yeah, thanks. When the fight's over, I'll come straight back to return it.{#ch23_s_033}"

    # シエスタ：はいっ！
    voice "ch23_si_022"
    si "Yes! You promised, didn't you?{#ch23_si_022}"

    # → next scene 863
    jump ch23_1_scene_863

label ch23_1_scene_861:

    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [EVENT_CG event    image=+224, level=80]
    $ dissolve_fx("id(224)")
    # サイト：ありがとう、シエスタ。
    voice "ch23_s_034"
    s "Thanks, Siesta. With this, not even a bomb can hit me.{#ch23_s_034}"

    # サイト：たとえ、当たっても、
    voice "ch23_s_035"
    s "Even if it does, I'll pretend it didn't.{#ch23_s_035}"

    # [EVENT_CG event    image=+225, level=80]
    $ dissolve_fx("id(225)")
    # シエスタ：もぅ、サイトさんったら……。
    voice "ch23_si_023"
    si "Honestly, Saito-san… Please don't do anything reckless…?{#ch23_si_023}"

    # サイト：ああ、分かってるさ。  [voice 12295]
    voice "ch23_s_036"
    s "Yeah, I know.{#ch23_s_036}"

    # → next scene 863
    jump ch23_1_scene_863

label ch23_1_scene_862:

    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [EVENT_CG event    image=+224, level=80]
    $ dissolve_fx("id(224)")
    # サイト：お守りをつけてると、
    voice "ch23_s_037"
    s "Wearing this charm makes me feel stronger. I'll do my best.{#ch23_s_037}"

    # [EVENT_CG event    image=+225, level=80]
    $ dissolve_fx("id(225)")
    # シエスタ：サイトさん……。  [voice 15018]
    voice "ch23_si_024"
    si "Saito-san…{#ch23_si_024}"

    # → next scene 863
    jump ch23_1_scene_863

label ch23_1_scene_863:

    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [EVENT_CG event    image=+224, level=80]
    $ dissolve_fx("id(224)")
    # → next scene 864
    jump ch23_1_scene_864

    # checkKiss(): ветка 864/865 — zero_kiss не портирован; идём по ветке zero_kiss (864), как в гл.12
label ch23_1_scene_864:

    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [EVENT_CG event    image=+224, level=80]
    $ dissolve_fx("id(224)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：それから……。  [voice 15019]
    voice "ch23_si_025"
    si "And also…{#ch23_si_025}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：なんだい、シエスタ？  [voice 12297]
    voice "ch23_s_038"
    s "What is it, Siesta?{#ch23_s_038}"

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：あとひとつだけ……。
    voice "ch23_si_026"
    si "Just one more thing… Um, could you… let me do a little charm? A special one.{#ch23_si_026}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：とっておきかぁ。
    voice "ch23_s_039"
    s "A special one, huh? Sure, go ahead. What should I do?{#ch23_s_039}"

    # [SPRITE   lay2     image=+497, level=160, dir=1A]
    # シエスタ：じゃ、じゃあ……。
    voice "ch23_si_027"
    si "T-Then… Could you close your eyes for just a moment?{#ch23_si_027}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：目を？
    voice "ch23_s_040"
    s "Close my eyes? Why?{#ch23_s_040}"

    # [SPRITE   lay2     image=+530, level=160, dir=2A]
    # シエスタ：ど、どうして……って、その、ええと……。
    voice "ch23_si_028"
    si "W-Why… Well, um… It's embarrassing, that's…{#ch23_si_028}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：恥ずかしい？
    voice "ch23_s_041"
    s "Embarrassed? I don't really get it, but…{#ch23_s_041}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # サイト：これでいい？  [voice 12301]
    voice "ch23_s_042"
    s "Is this okay?{#ch23_s_042}"

    # シエスタ：は、はい。  [voice 15023]
    voice "ch23_si_029"
    si "Y-Yes.{#ch23_si_029}"

    # シエスタ：すー……はー……。
    voice "ch23_si_030"
    si "In… out… Okay, I'm ready. H-Here I go!{#ch23_si_030}"

    # サイト：……ぁ！？  [voice 12302]
    voice "ch23_s_043"
    s "…Hah!?{#ch23_s_043}"

    # [EVENT_CG event    image=+226, level=80]
    $ dissolve_fx("id(226)")
    # [TRANS trans("crossfade", 1000)]
    # シエスタ：んっ……。  [voice 15025]
    voice "ch23_si_031"
    si "Mm…{#ch23_si_031}"

    # サイト：……っ！！！  [voice 12303]
    voice "ch23_s_044"
    s "…!!{#ch23_s_044}"

    # シエスタ：……。  [voice 15026]
    voice "ch23_si_032"
    si "…{#ch23_si_032}"

    # シエスタ：あ、あの、ごめんなさい……。
    voice "ch23_si_033"
    si "U-Um, I'm sorry… Doing something like this suddenly…{#ch23_si_033}"

    # シエスタ：で、でも、あの、おまじない……、
    voice "ch23_si_034"
    si "B-But, that was a charm… a charm, you see…{#ch23_si_034}"

    # サイト：あっ……ああっ。  [voice 12304]
    voice "ch23_s_045"
    s "Ah… Aah.{#ch23_s_045}"

    # → next scene 866
    jump ch23_1_scene_866

label ch23_1_scene_865:

    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [EVENT_CG event    image=+224, level=80]
    $ dissolve_fx("id(224)")
    # → next scene 866
    jump ch23_1_scene_866

label ch23_1_scene_866:

    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [EVENT_CG event    image=+226, level=80]
    $ dissolve_fx("id(226)")
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+67]
    # [SE       se0      play=+66]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：この声は、シルフィード！？  [voice 12305]
    voice "ch23_s_046"
    s "That voice is Sylphid!?{#ch23_s_046}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あれはミス・タバサの……。  [voice 15029]
    voice "ch23_si_035"
    si "That's Miss Tabitha's…{#ch23_si_035}"

    # [SE       se0      play=+66]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：ここにいたのねっ！
    voice "ch23_l_014"
    l "There you are! We're taking Tabitha's Sylphid to the castle!{#ch23_l_014}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 867
    jump ch23_1_scene_867

label ch23_1_scene_867:

    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SE       se0      play=+67]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：乗って。  [voice 15646]
    voice "ch23_t_001"
    t "Get on.{#ch23_t_001}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # モンモランシー：はあ、はあ、お待ちなさいったらっ！！  [voice 4110]
    voice "ch23_m_001"
    m "Hah, hah, wait for us!!{#ch23_m_001}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ルイズ、キュルケと、モンモンも
    voice "ch23_s_047"
    s "Louise—are Kirche and Montmorency coming, too?{#ch23_s_047}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：いえ、違うわ。  [voice 6679]
    voice "ch23_l_015"
    l "No, they're not.{#ch23_l_015}"

    # ルイズ：今朝はお城の騒ぎに気を取られて、
    voice "ch23_l_016"
    l "This morning I was so distracted by the castle incident that I didn't notice—Haruna wasn't in her room, was she?{#ch23_l_016}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：え、まじかよ。  [voice 12307]
    voice "ch23_s_048"
    s "Eh, seriously?{#ch23_s_048}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay3     image=+891, level=160, dir=2A]
    # モンモランシー：その、まじ、ですわ。
    voice "ch23_m_002"
    m "Y-Yes, seriously. Haruna vanished this morning.{#ch23_m_002}"

    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # モンモランシー：今も探していたんですけど、
    voice "ch23_m_003"
    m "We've been looking, but there's no trace of her anywhere.{#ch23_m_003}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：学院にも爆弾使いが来たわけだし、
    voice "ch23_l_017"
    l "A bomber came to the academy, too, so I worried something might have happened…{#ch23_l_017}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：キュルケとモンモランシーに
    voice "ch23_l_018"
    l "I asked Kirche and Montmorency to search for her.{#ch23_l_018}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：ほんと、どこ行っちゃったのかしらね。
    voice "ch23_k_001"
    k "Honestly, where could she have gone? Even magic can't find her…{#ch23_k_001}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：とにかく、今は緊急事態だ。
    voice "ch23_s_049"
    s "Anyway, this is an emergency. Let's hurry to Tristain.{#ch23_s_049}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：キュルケ、モンモン。
    voice "ch23_s_050"
    s "Kirche, Montmorency—can I leave Haruna to you?{#ch23_s_050}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # キュルケ：あたしがダーリンの頼みを断れると思う？
    voice "ch23_k_002"
    k "You think I'd refuse darling's request? We're in too deep to back out now. Right, Montmorency?{#ch23_k_002}"

    # [SPRITE   lay3     image=+885, level=160, dir=2A]
    # モンモランシー：仕方ありませんわね。
    voice "ch23_m_004"
    m "I suppose we must. I'll extend the range of my magic a little further.{#ch23_m_004}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：ありがとう、助かる！  [voice 12310]
    voice "ch23_s_051"
    s "Thanks. That helps.{#ch23_s_051}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：サイトさん。  [voice 15030]
    voice "ch23_si_036"
    si "Saito-san.{#ch23_si_036}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：シエスタ……。
    voice "ch23_s_052"
    s "Siesta… It's fine. We'll definitely come back. Definitely!{#ch23_s_052}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：はい！  [voice 15031]
    voice "ch23_si_037"
    si "Yes!{#ch23_si_037}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：よし、行こう！
    voice "ch23_s_053"
    s "All right, let's go! Louise! Tabitha!{#ch23_s_053}"

    # [SPRITE   lay2     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：シルフィード。  [voice 15647]
    voice "ch23_t_002"
    t "Sylphid.{#ch23_t_002}"

    # タバサ：トリスタニア。
    voice "ch23_t_003"
    t "Tristain. Hurry.{#ch23_t_003}"

    # [SE       se0      play=+66]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+130, level=80]
    $ dissolve_fx("id(130)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+67]
    # サイト：（俺達を乗せたシルフィードが、
    s "(Sylphid, carrying us, flapped her wings wider.){#ch23_s_054}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：サイトさんっ！！  [voice 15032]
    voice "ch23_si_038"
    si "Saito-san!!{#ch23_si_038}"

    # シエスタ：わたし、待ってますからっ！！
    voice "ch23_si_039"
    si "I'll be waiting for you! I'll definitely be waiting!{#ch23_si_039}"

    # [SPRITE   lay2     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1150, level=200]
    $ fade_fx("id(1150)")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1141, level=200]
    $ fade_fx("id(1141)")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1150, level=200]
    $ fade_fx("id(1150)")
    # [TRANS trans("crossfade", 750)]
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # タバサ：着いた。  [voice 15649]
    voice "ch23_t_004"
    t "We're here.{#ch23_t_004}"

    # ルイズ：見て！
    voice "ch23_l_019"
    l "Look! There's smoke! The capital is in chaos, too…{#ch23_l_019}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：爆弾使いのやつ、相当暴れたみたいだな。
    voice "ch23_s_055"
    s "That bomber really went wild. The whole city's in confusion.{#ch23_s_055}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：街の人が逃げ出してる。  [voice 15650]
    voice "ch23_t_005"
    t "People are running away.{#ch23_t_005}"

    # サイト：ほんとだ。
    voice "ch23_s_056"
    s "Right. It's less like they're afraid of the bomber, and more like they're fleeing from something…{#ch23_s_056}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：何かって何よ！  [voice 6684]
    voice "ch23_l_020"
    l "What do you mean, something!{#ch23_l_020}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：地震とか……戦争とかか？  [voice 12315]
    voice "ch23_s_057"
    s "An earthquake… or a war?{#ch23_s_057}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：お城に行きましょう！
    voice "ch23_l_021"
    l "Let's go to the castle! I'm worried about the princess!{#ch23_l_021}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 868
    jump ch23_2

    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch23_2
    return

