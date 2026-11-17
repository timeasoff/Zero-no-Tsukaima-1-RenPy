# Глава 14, часть 1 (сцены 578–598): «私のお兄ちゃん» — слежка за Уэзерби, засада.
# Источник: ps2_source/chapters/chapter_15_私のお兄ちゃん.txt (SCENE 578-598).

label ch14:
    $ tndl(None)
    $ show_sprites()

label ch14_1_scene_578:

    # [TITLE title("私のお兄ちゃん")]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1159, level=200]
    $ fade_fx("id(1159)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：それで、キュルケとのコンビの調子はどう？  [voice 7004]
    voice "ch14_l_001"
    l "So, how's the team-up with Kirche going?{#ch14_l_001}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：ま、まずまずって感じかな。  [voice 12910]
    voice "ch14_s_001"
    s "Well, so-so, I guess.{#ch14_s_001}"

    # ルイズ：ふーん。
    voice "ch14_l_002"
    l "Hm. Is that so.{#ch14_l_002}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そ、そっちは？  [voice 12911]
    voice "ch14_s_002"
    s "H-How about you?{#ch14_s_002}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：教えてあげない。
    voice "ch14_l_003"
    l "I won't tell you. You're my enemy, Saito, aren't you?{#ch14_l_003}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そ、そうですか。  [voice 12912]
    voice "ch14_s_003"
    s "I-Is that so.{#ch14_s_003}"

    # サイト：（な、なんでそんなに怒ってるんだよ！）
    s "(Why are you so angry…!)?{#ch14_s_004}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：と、とりあえず、これから夜の調査の準備が
    voice "ch14_s_005"
    s "A-Anyway, we need to prepare for the night search…{#ch14_s_005}"

    # [SE       se0      play=+57]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SE       se0      play=+56]
    # ルイズ：もうっ、バカ犬。  [voice 7007]
    voice "ch14_l_004"
    l "Really, you stupid dog.{#ch14_l_004}"

    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # null：………。 (no voice)
    # [BG       stage    hide]
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ふぁぁ……。
    voice "ch14_s_006"
    s "Yaaawn… Morning, Kirche.{#ch14_s_006}"

    # サイト：（と、言っても夜だけどさ）
    s "(Though it's night, actually…){#ch14_s_007}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：ふぁ……。
    voice "ch14_k_001"
    k "Fua… Morning, darling.{#ch14_k_001}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：どうしたんだ、キュルケ。
    voice "ch14_s_008"
    s "What's wrong, Kirche? You look sleepy.{#ch14_s_008}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ウェザリーのことを書いた資料を
    voice "ch14_k_002"
    k "I was reading documents about Weatherly.{#ch14_k_002}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ウェザリーの？  [voice 12916]
    voice "ch14_s_009"
    s "About Weatherly?{#ch14_s_009}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：ちょっと、ある筋から仕入れて
    voice "ch14_k_003"
    k "I got them from a certain source… But…{#ch14_k_003}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：もしかすると彼女、ただのネズミじゃないかも
    voice "ch14_k_004"
    k "Maybe she's not just a rat.{#ch14_k_004}"

    # キュルケ：ただの旅役者にしては、資金は豊富。
    voice "ch14_k_005"
    k "Too much money for a mere traveling actress. And she meets with nobles often—and only ones with shady reputations.{#ch14_k_005}"

    menu:
        "Not just a rat, you say?{#ch14_1_c_578_1}":
            jump ch14_1_scene_579
        "It's not like she's doing anything wrong…{#ch14_1_c_578_2}":
            jump ch14_1_scene_580
        "Isn't it wrong to suspect her?{#ch14_1_c_578_3}":
            jump ch14_1_scene_581

label ch14_1_scene_579:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ただのネズミじゃないかも、って？  [voice 12917]
    voice "ch14_s_010"
    s "Not just a rat, you say?{#ch14_s_010}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：もしかしたら、爆弾使いよりも、
    voice "ch14_k_006"
    k "Maybe she's a bigger rat than the bomb-thrower.{#ch14_k_006}"

    # → next scene 582
    jump ch14_1_scene_582

label ch14_1_scene_580:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：べ、別に評判の悪い貴族のところに
    voice "ch14_s_011"
    s "J-Just because she visits nobles with bad reputations…{#ch14_s_011}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：悪いことをしてるわけじゃないだろう？  [voice 12919]
    voice "ch14_s_012"
    s "That doesn't mean she's doing something bad, does it?{#ch14_s_012}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：ダーリンが信じたいのは分かるけど、
    voice "ch14_k_007"
    k "I know you want to believe, but we should be wary of Weatherly. She's black as pitch.{#ch14_k_007}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：それはそうなんだけど。  [voice 12920]
    voice "ch14_s_013"
    s "I know, but…{#ch14_s_013}"

    # → next scene 582
    jump ch14_1_scene_582

label ch14_1_scene_581:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：……疑うのはよくないのでは？  [voice 12921]
    voice "ch14_s_014"
    s "…Isn't it wrong to suspect her?{#ch14_s_014}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：調べて疑いが晴れるのならいいじゃない。
    voice "ch14_k_008"
    k "If investigating clears the suspicion, what's wrong with that? Or are you afraid of the truth?{#ch14_k_008}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そ、そんなつもりじゃないけどさ……。  [voice 12922]
    voice "ch14_s_015"
    s "T-That's not it, but…{#ch14_s_015}"

    # → next scene 582
    jump ch14_1_scene_582

label ch14_1_scene_582:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # サイト：（爆弾使いの騒動。
    s "(The bomb-thrower incident. A traveling actress who might be a spy…){#ch14_s_016}"

    # サイト：（いったい、トリスタニアで何が
    s "(What's about to happen in Tristain…?){#ch14_s_017}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 583
    jump ch14_1_scene_583

label ch14_1_scene_583:

    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # キュルケ：レコン・キスタは、この前の戦いで
    voice "ch14_k_009"
    k "Reconquista lost many of its prized aerial fleet in the last battle, right?{#ch14_k_009}"

    # サイト：そうだけど？  [voice 12923]
    voice "ch14_s_018"
    s "Yeah, but?{#ch14_s_018}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：（もちろん、沈めたのは俺とルイズだったり
    s "(Of course, the ones who sank them were me and Louise… but it's a secret.){#ch14_s_019}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：それで、戦場で不利になったレコン・キスタは、
    voice "ch14_k_010"
    k "So Reconquista, now at a disadvantage, changed the form of the war, I think.{#ch14_k_010}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：戦争の形を変えた？  [voice 12924]
    voice "ch14_s_020"
    s "Changed the form of the war?{#ch14_s_020}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：トリスタニアを爆破事件で混乱させたり、
    voice "ch14_k_011"
    k "They're shaking Tristain from within—sowing confusion with bombings, bribing nobles…{#ch14_k_011}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：……。  [voice 12925]
    voice "ch14_s_021"
    s "…{#ch14_s_021}"

    # [SPRITE   lay19    image=+940, level=155, dir=1A]
    # [SPRITE   lay5     level=157]
    # [SPRITE   lay6     level=156]
    # デルフリンガー：なるほどな。
    voice "ch14_d_001"
    d "I see. Indeed, with firecrackers going off under your feet, you can't chant a proper spell.{#ch14_d_001}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     image=+401, level=157, dir=1B]
    # サイト：そういうことか。  [voice 12926]
    voice "ch14_s_022"
    s "So that's it.{#ch14_s_022}"

    # [SPRITE   lay6     image=+682, level=156, dir=1A]
    # キュルケ：女王陛下もそのあたりを
    voice "ch14_k_012"
    k "I think Her Majesty is wary of that too. I wonder how much she's figured out.{#ch14_k_012}"

    # [SPRITE   lay5     image=+440, level=157, dir=2B]
    # サイト：お姫さまが？  [voice 12927]
    voice "ch14_s_023"
    s "The Princess?{#ch14_s_023}"

    # [SPRITE   lay6     image=+709, level=156, dir=2A]
    # キュルケ：別に、女王陛下は遊びで一座の公演に
    voice "ch14_k_013"
    k "The Queen didn't join a troupe for fun, you know.{#ch14_k_013}"

    menu:
        "Weatherly is an agent, then?{#ch14_1_c_583_1}":
            jump ch14_1_scene_584
        "Too much of a coincidence, isn't it?{#ch14_1_c_583_2}":
            jump ch14_1_scene_585
        "The Princess was just playing, right?{#ch14_1_c_583_3}":
            jump ch14_1_scene_586

label ch14_1_scene_584:

    # [SPRITE   lay5     image=+440, level=157, dir=2B]
    # [SPRITE   lay6     image=+709, level=156, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay5     image=+401, level=157, dir=1B]
    # サイト：つまり、ウェザリーさんはレコン・キスタが
    voice "ch14_s_024"
    s "So Weatherly is an agent sent by Reconquista?{#ch14_s_024}"

    # [SPRITE   lay6     image=+676, level=156, dir=1A]
    # キュルケ：状況だけをみていれば、そうなるわね。  [voice 3705]
    voice "ch14_k_014"
    k "Judging by the situation, that's how it looks.{#ch14_k_014}"

    # → next scene 587
    jump ch14_1_scene_587

label ch14_1_scene_585:

    # [SPRITE   lay5     image=+440, level=157, dir=2B]
    # [SPRITE   lay6     image=+709, level=156, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay5     image=+434, level=157, dir=2B]
    # サイト：おいおい、あまりに話ができすぎてないか？
    voice "ch14_s_025"
    s "Hey, isn't this all too convenient? This isn't a play.{#ch14_s_025}"

    # [SPRITE   lay6     image=+676, level=156, dir=1A]
    # キュルケ：確かに話ができすぎてるわね。
    voice "ch14_k_015"
    k "True, it's too convenient. Especially that we were written into it. There's one more thing we're missing.{#ch14_k_015}"

    # [SPRITE   lay5     image=+401, level=157, dir=1B]
    # サイト：見過ごしてること？  [voice 12930]
    voice "ch14_s_026"
    s "Missing what?{#ch14_s_026}"

    # → next scene 587
    jump ch14_1_scene_587

label ch14_1_scene_586:

    # [SPRITE   lay5     image=+440, level=157, dir=2B]
    # [SPRITE   lay6     image=+709, level=156, dir=2A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay5     image=+434, level=157, dir=2B]
    # サイト：お姫さまは遊びだろ？
    voice "ch14_s_027"
    s "The Princess was just playing around, right? I wanted to spend time with Louise for once.{#ch14_s_027}"

    # [SPRITE   lay6     image=+676, level=156, dir=1A]
    # キュルケ：その冗談は笑えないわね。  [voice 3707]
    voice "ch14_k_016"
    k "That joke isn't funny.{#ch14_k_016}"

    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # サイト：さ、さいですか……。  [voice 12932]
    voice "ch14_s_028"
    s "I-I see…{#ch14_s_028}"

    # → next scene 587
    jump ch14_1_scene_587

label ch14_1_scene_587:

    # [SPRITE   lay5     image=+401, level=157, dir=1B]
    # [SPRITE   lay6     image=+676, level=156, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # サイト：でも、ここまで大事なことが分かってるなら、
    voice "ch14_s_029"
    s "But if you know this much, why not talk to Louise?{#ch14_s_029}"

    # [SPRITE   lay6     image=+676, level=156, dir=1A]
    # キュルケ：ルイズに話すには、まだ証拠が足りないわ。  [voice 3708]
    voice "ch14_k_017"
    k "There isn't enough evidence yet.{#ch14_k_017}"

    # [SPRITE   lay5     image=+405, level=157, dir=1B]
    # サイト：で、でも！  [voice 12934]
    voice "ch14_s_030"
    s "B-But!{#ch14_s_030}"

    # [SPRITE   lay6     image=+682, level=156, dir=1A]
    # キュルケ：だって、あのルイズよ？
    voice "ch14_k_018"
    k "It's Louise, isn't it? Tell her carelessly and she'll charge in and make a scene.{#ch14_k_018}"

    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # サイト：うっ……確かに……。  [voice 12935]
    voice "ch14_s_031"
    s "Ugh… True…{#ch14_s_031}"

    # [SPRITE   lay6     image=+711, level=156, dir=2A]
    # キュルケ：うふふ……。
    voice "ch14_k_019"
    k "Ufufu… Besides, the contest is still going, you know!{#ch14_k_019}"

    # [SPRITE   lay5     image=+440, level=157, dir=2B]
    # サイト：……へ？
    voice "ch14_s_032"
    s "…Eh? You're not putting the contest with Louise ahead of this, are you?{#ch14_s_032}"

    # [SPRITE   lay6     image=+676, level=156, dir=1A]
    # キュルケ：さあ、ダーリン！
    voice "ch14_k_020"
    k "Come on, darling! To the night streets again!{#ch14_k_020}"

    # [SPRITE   lay5     image=+405, level=157, dir=1B]
    # サイト：ちょ、ちょっと待てーーっ！  [voice 12937]
    voice "ch14_s_033"
    s "W-Wait a second!{#ch14_s_033}"

    # [SPRITE   lay6     image=+678, level=156, dir=1A]
    # キュルケ：おほほーーっ！  [voice 3712]
    voice "ch14_k_021"
    k "Ohohoho!{#ch14_k_021}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 588
    jump ch14_1_scene_588

label ch14_1_scene_588:

    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # サイト：ど、どうしたんだよ。
    voice "ch14_s_034"
    s "W-What are you doing? Pressing against me… It's embarrassing!{#ch14_s_034}"

    # キュルケ：あーら、ダーリン。
    voice "ch14_k_022"
    k "My, my, darling. Don't be shy.{#ch14_k_022}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：カモフラージュよ、カモフラージュ。
    voice "ch14_k_023"
    k "It's a disguise, a disguise. If we don't act like lovers, they'll get suspicious, right?{#ch14_k_023}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：そ、そっか？  [voice 12939]
    voice "ch14_s_035"
    s "I-I see?{#ch14_s_035}"

    # [SPRITE   lay6     image=+717, level=160, dir=2A]
    # キュルケ：うふふ、でも、２人でこうしてると、
    voice "ch14_k_024"
    k "Ufufu, but being like this with just the two of us feels like a date.{#ch14_k_024}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：うふふ、ダーリンとデート。
    voice "ch14_k_025"
    k "Ufufu, a date with darling. A date with darling.{#ch14_k_025}"

    # サイト：（うわ、キュルケの体が俺の腕に……。
    s "(Whoa, Kirche's body is against my arm… Why am I surrounded by girls ever since I came to this world…?){#ch14_s_036}"

    # [SPRITE   lay5     image=+442, level=160, dir=2B]
    # サイト：（これってモテ期が来たってことですか？）
    s "(Is this my popular phase…?){#ch14_s_037}"

    # ルイズ：そんなはずないでしょ！
    voice "ch14_l_005"
    l "That's ridiculous! You stupid dog!!{#ch14_l_005}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：……！  [voice 12940]
    voice "ch14_s_038"
    s "…!{#ch14_s_038}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：どうしたの？
    voice "ch14_k_026"
    k "What's wrong, darling?{#ch14_k_026}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：いや、なんかこう……寒気が。  [voice 12941]
    voice "ch14_s_039"
    s "No, it's just… a chill.{#ch14_s_039}"

    # [SPRITE   lay6     image=+684, level=160, dir=1A]
    # キュルケ：あら、じゃあ……。
    voice "ch14_k_027"
    k "Oh, then… shall I warm you up?{#ch14_k_027}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+119, level=80]
    $ dissolve_fx("id(119)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：えっ！
    voice "ch14_s_040"
    s "Eh! That's a bit… dangerous!{#ch14_s_040}"

    # キュルケ：うふふ……。
    voice "ch14_k_028"
    k "Ufufu… A red-faced darling is cute too! I don't want to let go!{#ch14_k_028}"

    # サイト：お願いです。
    voice "ch14_s_041"
    s "Please. Let go of me.{#ch14_s_041}"

    # キュルケ：さぁ、ダーリン。
    voice "ch14_k_029"
    k "Come on, darling. Let's find Weatherly!{#ch14_k_029}"

    # サイト：お願いです。
    voice "ch14_s_042"
    s "Please. Listen to people.{#ch14_s_042}"

    # 【移動】 → extra 1485/1486/1487/1488
    menu:
        "In front of the castle{#ch14_1_c_588_1}":
            jump ch14_2_scene_1485
        "The main street{#ch14_1_c_588_2}":
            jump ch14_2_scene_1486
        "The back alley{#ch14_1_c_588_3}":
            jump ch14_2_scene_1487
        "The street{#ch14_1_c_588_4}":
            jump ch14_2_scene_1488

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
label ch14_1_scene_589:

    # [BG       stage    image=+60, hide, level=10]
    $ fade_fx("id(60)")
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+60, hide, level=10]
    $ fade_fx("id(60)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+60, hide, level=10]
    $ fade_fx("id(60)")
label ch14_1_scene_590:

    # [BG       stage    image=+60, hide, level=10]
    $ fade_fx("id(60)")
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+60, hide, level=10]
    $ fade_fx("id(60)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+60, hide, level=10]
    $ fade_fx("id(60)")
label ch14_1_scene_591:

    # [BG       stage    image=+60, hide, level=10]
    $ fade_fx("id(60)")
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+60, hide, level=10]
    $ fade_fx("id(60)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+60, hide, level=10]
    $ fade_fx("id(60)")
label ch14_1_scene_592:

    # [BG       stage    image=+60, hide, level=10]
    $ fade_fx("id(60)")
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [BG       stage    image=+60, hide, level=10]
    $ fade_fx("id(60)")
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+60, hide, level=10]
    $ fade_fx("id(60)")
label ch14_1_scene_593:

    # [BG       stage    image=+60, level=200]
    $ fade_fx("id(60)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：……。
    w "…{#ch14_w_001}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：いたっ！
    voice "ch14_s_043"
    s "There! It's Weatherly-san!{#ch14_s_043}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+713, level=160, dir=2A]
    # キュルケ：ダーリン、静かにして。
    voice "ch14_k_030"
    k "Darling, quiet. Let's watch for a bit.{#ch14_k_030}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：……。
    w "…{#ch14_w_002}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # サイト：何をしてるんだろう？
    voice "ch14_s_044"
    s "What's she doing? Ah, she's moving.{#ch14_s_044}"

    # キュルケ：追いましょう！  [voice 3722]
    voice "ch14_k_031"
    k "Let's follow!{#ch14_k_031}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # null：………。 (no voice)
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # サイト：キュルケ。
    voice "ch14_s_045"
    s "Kirche. Are you walking rather slowly today?{#ch14_s_045}"

    # [SPRITE   lay5     level=157]
    # [SPRITE   lay19    image=+940, level=153, dir=1A]
    # [SPRITE   lay6     level=156]
    # デルフリンガー：ああ、相棒。
    voice "ch14_d_002"
    d "Ah, partner. It's almost like she's deliberately leading us on…{#ch14_d_002}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay6     image=+680, level=156, dir=1A]
    # キュルケ：え？  [voice 3723]
    voice "ch14_k_032"
    k "Eh?{#ch14_k_032}"

    # [SPRITE   lay5     image=+405, level=157, dir=1B]
    # サイト：なんだっ！？  [voice 12948]
    voice "ch14_s_046"
    s "What!?{#ch14_s_046}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [SPRITE   lay11    image=+1105, level=154, dir=1A]
    # [SPRITE   lay12    image=+1105, level=160, dir=1A]
    # 魔導士：……。
    mage "…{#ch14_mage_001}"

    # [SPRITE   lay11    hide]
    # [SPRITE   lay12    hide]
    # [SPRITE   lay5     image=+405, level=157, dir=1B]
    # [SPRITE   lay6     image=+680, level=156, dir=1A]
    # サイト：くそぉ、囲まれたか。  [voice 12949]
    voice "ch14_s_047"
    s "Damn, we're surrounded?{#ch14_s_047}"

    # キュルケ：はじめから気づかれていたのね。  [voice 3724]
    voice "ch14_k_033"
    k "So they knew from the start.{#ch14_k_033}"

    # [SPRITE   lay6     image=+713, level=156, dir=2A]
    # キュルケ：出てきなさい、ウェザリー！
    voice "ch14_k_034"
    k "Come out, Weatherly! You're here, aren't you?!{#ch14_k_034}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay11    image=+1105, level=154, dir=1A]
    # [SPRITE   lay12    image=+1105, level=160, dir=1A]
    # [SPRITE   lay20    image=+1072, level=152, dir=1B]
    # [SPRITE   lay12    level=153]
    # [SPRITE   lay11    level=155]
    # ウェザリー：……。
    w "…{#ch14_w_003}"

    # [SPRITE   lay20    image=+1061, level=152, dir=1A]
    # ウェザリー：おやおや。
    voice "ch14_w_004"
    w "My my. What does the leading pair want with this troupe leader?{#ch14_w_004}"

    # [SPRITE   lay11    hide]
    # [SPRITE   lay12    hide]
    # [SPRITE   lay20    hide]
    # [SPRITE   lay5     image=+405, level=157, dir=1B]
    # [SPRITE   lay6     image=+680, level=156, dir=1A]
    # サイト：ウェザリーさん！  [voice 12950]
    voice "ch14_s_048"
    s "Weatherly-san!{#ch14_s_048}"

    # キュルケ：ウェザリーこそ、こんな怪しい魔導士を
    voice "ch14_k_035"
    k "And what are you plotting, Weatherly, with such suspicious mages in tow?{#ch14_k_035}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay11    image=+1105, level=155, dir=1A]
    # [SPRITE   lay12    image=+1105, level=153, dir=1A]
    # [SPRITE   lay20    image=+1061, level=152, dir=1A]
    # [SPRITE   lay12    level=153]
    # [SPRITE   lay11    level=155]
    # ウェザリー：さぁ、何もたくらんでいないわよ。  [voice 16051]
    voice "ch14_w_005"
    w "Why, nothing at all.{#ch14_w_005}"

    # ウェザリー：もっとも。
    voice "ch14_w_006"
    w "Though even if I were plotting something…{#ch14_w_006}"

    # ウェザリー：その内容について、あなた達は知ることは
    voice "ch14_w_007"
    w "…you'd never learn what it is.{#ch14_w_007}"

    # [SPRITE   lay20    image=+1063, level=152, dir=1A]
    # ウェザリー：だって、あなた達。
    voice "ch14_w_008"
    w "Because you two will be disposed of right here.{#ch14_w_008}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay20    hide]
    # [SPRITE   lay12    hide]
    # [SPRITE   lay11    hide]
    # [BG       stage    hide]
    # → next scene 594
    jump ch14_1_scene_594

label ch14_1_scene_594:

    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：よっし！
    voice "ch14_s_049"
    s "All right! Next is you, Weatherly!{#ch14_s_049}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：あいにく、エキストラの人手には
    voice "ch14_w_009"
    w "Unfortunately, I'm not short on extras.{#ch14_w_009}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay20    hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+248, level=80]
    $ dissolve_fx("id(248)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # 魔導士：……。
    mage "…{#ch14_mage_002}"

    # キュルケ：ダーリン！
    voice "ch14_k_036"
    k "Darling! New ones!{#ch14_k_036}"

    # 魔導士：……。
    mage "…{#ch14_mage_003}"

    # サイト：くそ、この人数。
    voice "ch14_s_050"
    s "Damn, so many of them. It's endless!{#ch14_s_050}"

    # キュルケ：ホントね。
    voice "ch14_k_037"
    k "True. We have to call Louise and the others.{#ch14_k_037}"

    # サイト：分かってるけど、どうやって！  [voice 12953]
    voice "ch14_s_051"
    s "I know, but how!?{#ch14_s_051}"

    # キュルケ：川の水を蒸発させて霧を作るわ。
    voice "ch14_k_038"
    k "I'll evaporate the river water to make fog. In the confusion, let's split in two.{#ch14_k_038}"

    # キュルケ：あたしは敵をひきつけて逃げるわ。
    voice "ch14_k_039"
    k "I'll draw the enemy and run. Meanwhile, get Louise and the others.{#ch14_k_039}"

    # サイト：そんなことができるのか！  [voice 12954]
    voice "ch14_s_052"
    s "You can do that!?{#ch14_s_052}"

    # [SPRITE   lay6     hide]
    # キュルケ：できないことは言わないわ。
    voice "ch14_k_040"
    k "I don't say what I can't do. I'm Kirche with a slight fever, after all.{#ch14_k_040}"

    menu:
        "Got it{#ch14_1_c_594_1}":
            jump ch14_1_scene_595
        "Let's run together{#ch14_1_c_594_2}":
            jump ch14_1_scene_596
        "You can't evaporate with a slight fever{#ch14_1_c_594_3}":
            jump ch14_1_scene_597

label ch14_1_scene_595:

    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [EVENT_CG event    image=+248, level=80]
    $ dissolve_fx("id(248)")
    # サイト：分かった。
    voice "ch14_s_053"
    s "Got it. Then I'll go get Louise…{#ch14_s_053}"

    # キュルケ：気をつけてね、ダーリン。
    voice "ch14_k_041"
    k "Be careful, darling. Once you link up with Louise and the others, counterattack at once.{#ch14_k_041}"

    # サイト：もちろん。
    voice "ch14_s_054"
    s "Of course. You be careful too, Kirche!{#ch14_s_054}"

    # → next scene 598
    jump ch14_1_scene_598

label ch14_1_scene_596:

    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [EVENT_CG event    image=+248, level=80]
    $ dissolve_fx("id(248)")
    # サイト：キュルケ、１人で敵を引きつけるのか？
    voice "ch14_s_055"
    s "Kirche, drawing them all on alone? That's too dangerous.{#ch14_s_055}"

    # キュルケ：うふふ、あたしを誰だと思ってるの？  [voice 3733]
    voice "ch14_k_042"
    k "Ufufu, who do you think I am?{#ch14_k_042}"

    # サイト：……。  [voice 12958]
    voice "ch14_s_056"
    s "…{#ch14_s_056}"

    # キュルケ：ダーリン、お願い。
    voice "ch14_k_043"
    k "Darling, please. Just listen to me for now.{#ch14_k_043}"

    # キュルケ：大丈夫。
    voice "ch14_k_044"
    k "It's fine. Once you join Louise and the others, counterattack right away.{#ch14_k_044}"

    # サイト：分かった。
    voice "ch14_s_057"
    s "Got it. You be careful too, Kirche.{#ch14_s_057}"

    # → next scene 598
    jump ch14_1_scene_598

label ch14_1_scene_597:

    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [EVENT_CG event    image=+248, level=80]
    $ dissolve_fx("id(248)")
    # サイト：微熱だと水が蒸発しないだろ。  [voice 12960]
    voice "ch14_s_058"
    s "With a slight fever, you can't evaporate water.{#ch14_s_058}"

    # キュルケ：もう、ダーリン。
    voice "ch14_k_045"
    k "Really, darling. Don't fuss over details. I don't say what I can't do.{#ch14_k_045}"

    # キュルケ：ダーリン、お願い。
    voice "ch14_k_046"
    k "Darling, please. Just listen to me for now.{#ch14_k_046}"

    # キュルケ：大丈夫。
    voice "ch14_k_047"
    k "It's fine. Once you join Louise and the others, counterattack right away.{#ch14_k_047}"

    # サイト：分かった。
    voice "ch14_s_059"
    s "Got it. You be careful too, Kirche.{#ch14_s_059}"

    # → next scene 598
    jump ch14_1_scene_598

label ch14_1_scene_598:

    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [EVENT_CG event    image=+248, level=80]
    $ dissolve_fx("id(248)")
    # [SPRITE   lay11    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：大丈夫よ、ダーリン。
    voice "ch14_k_048"
    k "It's fine, darling. It'll work.{#ch14_k_048}"

    # [SPRITE   lay6     image=+746, level=160, dir=3A]
    # キュルケ：本当の『火』の魔法がどんなものか、
    voice "ch14_k_049"
    k "I'll show you what the true magic of 'fire' is—Kirche with a slight fever!{#ch14_k_049}"

    # [SE       se0      play=+95]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay20    vibrate=21]
    # [SPRITE   lay11    vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [SPRITE   lay6     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay20    hide, reset]
    # [SPRITE   lay11    hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay6     reset]
    # [SPRITE   lay6     hide]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 1000)]
    # 魔導士：くっ！
    voice "ch14_mage_004"
    mage "Tch! What is this! This steam!{#ch14_mage_004}"

    # ウェザリー：馬鹿者！
    voice "ch14_w_010"
    w "Fool! Calm down!{#ch14_w_010}"

    # [SPRITE   lay20    hide]
    # [SPRITE   lay11    hide]
    # [BG       stage    hide]
    # [BG       stage    image=+49, level=200]
    $ fade_fx("id(49)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：ダーリン、今よ！！  [voice 3741]
    voice "ch14_k_050"
    k "Darling, now!!{#ch14_k_050}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：分かった！  [voice 12962]
    voice "ch14_s_060"
    s "Got it!{#ch14_s_060}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 599
    jump ch14_2

    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch14_2
    return

