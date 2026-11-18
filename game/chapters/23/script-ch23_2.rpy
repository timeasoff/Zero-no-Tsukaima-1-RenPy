# Глава 23, часть 2 (сцены 868–878): в замке, briefing Генриетты.
# Источник: ps2_source/chapters/chapter_24_沈黙の応援.txt (SCENE 868-878).

label ch23_2:
    $ tndl(None)
    $ show_sprites()

label ch23_2_scene_868:

    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # サイト：おいおい、いきなり城に来ちゃって
    voice "ch23_s_058"
    s "Hey, showing up at the castle so suddenly—is that all right?{#ch23_s_058}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：一刻を争うの。
    voice "ch23_l_022"
    l "Every second counts. I can't worry about details.{#ch23_l_022}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：タバサ、ここまでつれてきてくれて
    voice "ch23_l_023"
    l "Tabitha, thank you for bringing us this far.{#ch23_l_023}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：なんだか、学院もハルナも心配だわ。
    voice "ch23_l_024"
    l "I'm worried about the academy and Haruna. I want you to go back and help Kirche and the others.{#ch23_l_024}"

    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # タバサ：了解。  [voice 15651]
    voice "ch23_t_006"
    t "Understood.{#ch23_t_006}"

    # ルイズ：急ぐわよ、サイト！！  [voice 6689]
    voice "ch23_l_025"
    l "Let's hurry, Saito!!{#ch23_l_025}"

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：（くいくい）  [voice 15652]
    voice "ch23_t_007"
    t "(Tug tug){#ch23_t_007}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：うん？  [voice 12317]
    voice "ch23_s_059"
    s "Hmm?{#ch23_s_059}"

    # タバサ：頑張る。  [voice 15653]
    voice "ch23_t_008"
    t "I'll do my best.{#ch23_t_008}"

    # [SPRITE   lay5     image=+434, level=160, dir=2B]
    # サイト：ああ、頑張るさ。  [voice 12318]
    voice "ch23_s_060"
    s "Yeah, you do that.{#ch23_s_060}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay15    image=+1116, level=160, dir=1A]
    # 味方Ａ：待てっ、おまえ達、王宮に乗り込むとは……！  [voice 4237]
    voice "ch23_soldier_001"
    soldier "Halt! You there, charging into the palace…!{#ch23_soldier_001}"

    # 味方Ａ：見たところ、魔法学院の生徒のようだが、
    voice "ch23_soldier_002"
    soldier "You look like students of the magic academy, but you're suspicious!{#ch23_soldier_002}"

    # [SPRITE   lay15    level=160]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：な、ななななんですってぇ！？
    voice "ch23_l_026"
    l "W-What was that!? Suspicious!? That's outrageous!!{#ch23_l_026}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay5     image=+407, level=156, dir=1B]
    # サイト：お、落ち着け、ルイズ！  [voice 12319]
    voice "ch23_s_061"
    s "O-Oh, calm down, Louise!{#ch23_s_061}"

    # [SPRITE   lay1     image=+339, level=155, dir=2A]
    # ルイズ：いいえ、黙っていられないわ！
    voice "ch23_l_027"
    l "No! I can't stay silent! This concerns the honor of the Valliere family!{#ch23_l_027}"

    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：わたしは、ラ・ヴァリエール公爵家の三女、
    voice "ch23_l_028"
    l "I am Louise Francoise Le Blanc de La Valliere, third daughter of the Duke of La Valliere.{#ch23_l_028}"

    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：俺は、平賀　才人。  [voice 12320]
    voice "ch23_s_062"
    s "And I'm Hiraga Saito.{#ch23_s_062}"

    # ルイズ：こんなのでも、わたしの使い魔よ。  [voice 6693]
    voice "ch23_l_029"
    l "He may look like this, but he's my familiar.{#ch23_l_029}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay15    image=+1118, level=160, dir=1A]
    # 味方Ａ：う……失礼いたしましたっ！
    voice "ch23_soldier_003"
    soldier "O-Oh… My apologies! Please forgive my rudeness!{#ch23_soldier_003}"

    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # 味方Ａ：しかし、公爵家の御方が、
    voice "ch23_soldier_004"
    soldier "But why has a member of a ducal house come to the castle at a time like this?{#ch23_soldier_004}"

    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：もう、なんで細かく聞いてくるのよ。
    voice "ch23_l_030"
    l "Honestly, why are you asking so many questions? We're in a hurry!{#ch23_l_030}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # サイト：ルイズ、落ち着けって。  [voice 12321]
    voice "ch23_s_063"
    s "Louise, calm down, I said.{#ch23_s_063}"

    menu:
        "I'll do the talking{#ch23_2_c_868_1}":
            jump ch23_2_scene_869
        "Leave it to Louise{#ch23_2_c_868_2}":
            jump ch23_2_scene_870
        "Princess~!{#ch23_2_c_868_3}":
            jump ch23_2_scene_871

label ch23_2_scene_869:

    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：俺が話をつける。  [voice 12322]
    voice "ch23_s_064"
    s "I'll do the talking.{#ch23_s_064}"

    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：あ、ちょっと、サイト！？  [voice 6695]
    voice "ch23_l_031"
    l "Ah, wait, Saito!?{#ch23_l_031}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+434, level=156, dir=2B]
    # サイト：あんた、隊長さん？
    voice "ch23_s_065"
    s "You there—are you the captain? Look, we want to see the princess. Could you announce us?{#ch23_s_065}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay15    image=+1116, level=160, dir=1A]
    # 味方Ａ：女王陛下に？
    voice "ch23_soldier_005"
    soldier "To Her Majesty? No, no! She's busy right now!{#ch23_soldier_005}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：ああ、もういいわよ！
    voice "ch23_l_032"
    l "Oh, that's enough! Saito, be quiet!{#ch23_l_032}"

    # → next scene 872
    jump ch23_2_scene_872

label ch23_2_scene_870:

    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：ルイズ、任せた。  [voice 12324]
    voice "ch23_s_066"
    s "Louise, I'll leave it to you.{#ch23_s_066}"

    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：分かったわ。  [voice 6697]
    voice "ch23_l_033"
    l "I understand.{#ch23_l_033}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     x=64, y=0]
    # ルイズ：姫さま……。
    voice "ch23_l_034"
    l "Princess… No, I wish an audience with Her Majesty the Queen. Please announce me.{#ch23_l_034}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # 味方Ａ：今、女王陛下は、
    voice "ch23_soldier_006"
    soldier "Her Majesty is currently occupied with emergency deliberations. I'm sorry, but I cannot announce you.{#ch23_soldier_006}"

    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：その緊急事態について、お会いしたいのよ！
    voice "ch23_l_035"
    l "It's about that emergency that I want to see her! Never mind, just announce me!{#ch23_l_035}"

    # → next scene 872
    jump ch23_2_scene_872

label ch23_2_scene_871:

    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：お姫さまー！
    voice "ch23_s_067"
    s "Princess~! Princess~! Come out~!{#ch23_s_067}"

    # [SPRITE   lay1     image=+339, level=155, dir=2A]
    # ルイズ：ちょっと、サイト！？  [voice 6700]
    voice "ch23_l_036"
    l "Hey, Saito!?{#ch23_l_036}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay15    image=+1116, level=160, dir=1A]
    # 味方Ａ：ぬぬぬ！
    voice "ch23_soldier_007"
    soldier "Nu nu nu! Suspicious fellow!{#ch23_soldier_007}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：もう、いいから、あんたは黙ってなさい！  [voice 6701]
    voice "ch23_l_037"
    l "Honestly, you—just be quiet!{#ch23_l_037}"

    # → next scene 872
    jump ch23_2_scene_872

label ch23_2_scene_872:

    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # [SPRITE   lay5     image=+434, level=156, dir=2B]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay15    x=144, y=416]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：もう……。
    voice "ch23_l_038"
    l "Honestly… I have a direct warrant from Her Majesty!{#ch23_l_038}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # 味方Ａ：これは……確かに王家の紋章……。  [voice 4244]
    voice "ch23_soldier_008"
    soldier "This is… indeed the royal crest…{#ch23_soldier_008}"

    # [SPRITE   lay1     image=+335, level=155, dir=2A]
    # ルイズ：分かったら、早く取り次いでちょうだい。
    voice "ch23_l_039"
    l "Now that you understand, announce me at once. We have no time!{#ch23_l_039}"

    # 味方Ａ：分かりました。
    voice "ch23_soldier_009"
    soldier "Understood. Please wait here.{#ch23_soldier_009}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：なぁ、ルイズ。
    voice "ch23_s_068"
    s "Say, Louise. Wouldn't it have been better to show that from the start?{#ch23_s_068}"

    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：そう、ひょいひょい出すものじゃないわよ。
    voice "ch23_l_040"
    l "It's not something you flash around casually. It was supposed to be a top-secret mission.{#ch23_l_040}"

    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # サイト：まぁ、そうだな。  [voice 12327]
    voice "ch23_s_069"
    s "Well, I suppose so.{#ch23_s_069}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 873
    jump ch23_2_scene_873

label ch23_2_scene_873:

    # [SE       se0      play=+57]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # ルイズ：姫さまっご無事で！！  [voice 6705]
    voice "ch23_l_041"
    l "Princess! Are you safe!?{#ch23_l_041}"

    # アンリエッタ：ルイズ、ルイズ・フランソワーズですね！
    voice "ch23_h_001"
    h "Louise, Louise Francoise, is that you! We've been waiting for you.{#ch23_h_001}"

    # サイト：（でかいテーブルを囲んでるのは、
    s "(The people around the big table must be military and officials of high rank. The way they look at me and Louise is stern.){#ch23_s_070}"

    # ルイズ：姫さま……。
    voice "ch23_l_042"
    l "Princess… I'm glad you're safe.{#ch23_l_042}"

    # アンリエッタ：こんな危険な時にやってくきてくれるなんて。
    voice "ch23_h_002"
    h "To come here at such a dangerous time… Why are you always like this, Louise?{#ch23_h_002}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：それは姫さまのことが心配だからに
    voice "ch23_l_043"
    l "Because I was worried about you, of course!{#ch23_l_043}"

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：ありがとう、ルイズ。
    voice "ch23_h_003"
    h "Thank you, Louise. I'm grateful for your friendship.{#ch23_h_003}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：アンリエッタ様……。  [voice 6708]
    voice "ch23_l_044"
    l "Henrietta-sama…{#ch23_l_044}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：それにしてもさ。
    voice "ch23_s_071"
    s "That aside, why is the castle in such an uproar? That soldier earlier was unusually tense, too.{#ch23_s_071}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ええ。
    voice "ch23_l_045"
    l "Yes. For precautions against the bomber, the security seems excessive to me, though…?{#ch23_l_045}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：そのとおりです、ルイズ。
    voice "ch23_h_004"
    h "That's right, Louise. This whole disturbance isn't about the bomber.{#ch23_h_004}"

    # ルイズ：ものではない、とは？  [voice 6710]
    voice "ch23_l_046"
    l "Not about, you say?{#ch23_l_046}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：どういうことなんですか？  [voice 12329]
    voice "ch23_s_072"
    s "What do you mean?{#ch23_s_072}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+803, level=160, dir=2A]
    # アンリエッタ：……。  [voice 619]
    voice "ch23_h_005"
    h "…{#ch23_h_005}"

    # [SPRITE   lay8     image=+797, level=160, dir=2A]
    # アンリエッタ：わたくし達がこれまで敵視していた
    voice "ch23_h_006"
    h "The 'bomber' we've been treating as our enemy appears to have been merely a pawn.{#ch23_h_006}"

    # [SPRITE   lay8     x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：爆弾使いが先兵？
    voice "ch23_s_073"
    s "The bomber a pawn? You mean there's a mastermind?{#ch23_s_073}"

    # アンリエッタ：はい。
    voice "ch23_h_007"
    h "Yes. It's because we failed to see that that this country is in its current predicament.{#ch23_h_007}"

    # アンリエッタ：まず、これまでに起きた爆破事件ですが、
    voice "ch23_h_008"
    h "First, the explosions that have happened so far—we thought the bomber was detonating them without a plan.{#ch23_h_008}"

    # [SPRITE   lay8     image=+803, level=160, dir=2A]
    # アンリエッタ：ですが、そうではなかったのです。
    voice "ch23_h_009"
    h "But that wasn't so. Look at this map.{#ch23_h_009}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+259, level=80]
    $ dissolve_fx("id(259)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：これはトリスタニアとその周辺の地図ですね。
    voice "ch23_l_047"
    l "This is a map of Tristain and its surroundings. These marks are where the explosions occurred?{#ch23_l_047}"

    # アンリエッタ：そうです。
    voice "ch23_h_010"
    h "Yes. Looking at this, do you notice anything?{#ch23_h_010}"

    # サイト：なんだか、城の周りを丸く囲んでるように
    voice "ch23_s_074"
    s "It looks like they're arranged in a circle around the castle…{#ch23_s_074}"

    # アンリエッタ：いいえ。
    voice "ch23_h_011"
    h "No. They don't just look like they're surrounding it. They are surrounding it.{#ch23_h_011}"

    # アンリエッタ：今、城はぐるりと敵の大砲に囲まれています。  [voice 626]
    voice "ch23_h_012"
    h "Right now, the castle is completely encircled by the enemy's cannons.{#ch23_h_012}"

    # ルイズ：大砲？
    voice "ch23_l_048"
    l "Cannons? Princess, what on earth do you mean?{#ch23_l_048}"

    # アンリエッタ：爆破が断続的に繰り返されたため、
    voice "ch23_h_013"
    h "Because the bombings kept recurring, there was a shortage of craftsmen for repairs, so workers were brought in from abroad.{#ch23_h_013}"

    # アンリエッタ：敵はその職人の中に工作員を潜入させ、
    voice "ch23_h_014"
    h "The enemy infiltrated agents among those craftsmen and installed gun emplacements at the repair sites.{#ch23_h_014}"

    # サイト：何だって！？
    voice "ch23_s_075"
    s "What!? So right now, this castle is…{#ch23_s_075}"

    # アンリエッタ：はい。
    voice "ch23_h_015"
    h "Yes. It's surrounded by enemy strongholds.{#ch23_h_015}"

    # アンリエッタ：今はまだそれほど活発に動いていませんが、
    voice "ch23_h_016"
    h "They're not very active yet, but if they all move at once, the castle could even fall.{#ch23_h_016}"

    # ルイズ：なんてことなの……。
    voice "ch23_l_049"
    l "That's terrible… If only we'd caught the bomber before it came to this…{#ch23_l_049}"

    # アンリエッタ：いいえ、ルイズ。  [voice 631]
    voice "ch23_h_017"
    h "No, Louise.{#ch23_h_017}"

    # アンリエッタ：あの時、あなた方が深追いをして、
    voice "ch23_h_018"
    h "Back then, the fact that you didn't pursue too far and avoid disaster was blessing enough.{#ch23_h_018}"

    # ルイズ：姫さま……。  [voice 6714]
    voice "ch23_l_050"
    l "Princess…{#ch23_l_050}"

    # アンリエッタ：とにかく、今は各砲台を個別に
    voice "ch23_h_019"
    h "In any case, we're attacking each battery separately now, but the situation isn't going well.{#ch23_h_019}"

    # アンリエッタ：市民の避難にも、兵を割かなければ
    voice "ch23_h_020"
    h "We also have to spare soldiers for evacuating the citizens… In short, we're on the defensive.{#ch23_h_020}"

    # アンリエッタ：以上が、今の状況です。  [voice 635]
    voice "ch23_h_021"
    h "That's the situation for now.{#ch23_h_021}"

    # アンリエッタ：ルイズ、それに使い魔さん。
    voice "ch23_h_022"
    h "Louise, and you, familiar. Please wait a little. I'll wrap up the deliberations now.{#ch23_h_022}"

    # ルイズ：かしこまりました。  [voice 6715]
    voice "ch23_l_051"
    l "Understood.{#ch23_l_051}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # → next scene 874
    jump ch23_2_scene_874

label ch23_2_scene_874:

    # [EVENT_CG event    image=+135, level=80]
    $ dissolve_fx("id(135)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # サイト：（それから、協議は長く続いた。
    s "(After that, the meeting dragged on. By any reckoning, the situation wasn't good. It was bound to take a long time.){#ch23_s_076}"

    # アンリエッタ：分かりました。
    voice "ch23_h_023"
    h "Understood. Then everyone, proceed as decided in the meeting.{#ch23_h_023}"

    # アンリエッタ：犠牲は最小限に。
    voice "ch23_h_024"
    h "Keep casualties to a minimum. Now, dismissed.{#ch23_h_024}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：やっと協議が終わったみたいだな。  [voice 12333]
    voice "ch23_s_077"
    s "Looks like the meeting finally ended.{#ch23_s_077}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：お待たせしてしまいましたね。  [voice 639]
    voice "ch23_h_025"
    h "Sorry to keep you waiting.{#ch23_h_025}"

    # [SPRITE   lay8     x=224, y=0]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：いえ。
    voice "ch23_l_052"
    l "Not at all. Rather, you look tired, Princess…{#ch23_l_052}"

    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # アンリエッタ：爆弾使いの策略にかかって、
    voice "ch23_h_026"
    h "Falling for the bomber's trick, I let the enemy into the capital. It's my lack of ability…{#ch23_h_026}"

    # ルイズ：姫さま……。
    voice "ch23_l_053"
    l "Princess… We're responsible, too.{#ch23_l_053}"

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：いえ、あなたがたはよくやってくれました。
    voice "ch23_h_027"
    h "No. You did well. I'm grateful.{#ch23_h_027}"

    # サイト：……。  [voice 12334]
    voice "ch23_s_078"
    s "…{#ch23_s_078}"

    menu:
        "The princess isn't to blame{#ch23_2_c_874_1}":
            jump ch23_2_scene_875
        "Any good ideas, Louise?{#ch23_2_c_874_2}":
            jump ch23_2_scene_876
        "What's the army doing?{#ch23_2_c_874_3}":
            jump ch23_2_scene_877

label ch23_2_scene_875:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：お姫さまは悪くなんかないさ。
    voice "ch23_s_079"
    s "The princess isn't at fault. The fault lies with the bomber and whoever's pulling his strings.{#ch23_s_079}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そうね。
    voice "ch23_l_054"
    l "Right. We'll defeat them with our own hands, somehow.{#ch23_l_054}"

    # → next scene 878
    jump ch23_2_scene_878

label ch23_2_scene_876:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ルイズ、何かいい考えないか？
    voice "ch23_s_080"
    s "Louise, got any good ideas? We can't go on like this, can we?{#ch23_s_080}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そうね……。  [voice 6719]
    voice "ch23_l_055"
    l "Hmm…{#ch23_l_055}"

    # → next scene 878
    jump ch23_2_scene_878

label ch23_2_scene_877:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：軍人さん達は何やってんのさ。
    voice "ch23_s_081"
    s "What are the soldiers doing? Sitting around looking important here won't help.{#ch23_s_081}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：サイト！  [voice 6720]
    voice "ch23_l_056"
    l "Saito!{#ch23_l_056}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     image=+803, level=160, dir=2A]
    # アンリエッタ：将校達は、いえ、末端の兵士に至るまで、
    voice "ch23_h_028"
    h "The military—down to the lowliest soldier—has done well. But given how sudden this was…{#ch23_h_028}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：そ、そうなんだ。  [voice 12338]
    voice "ch23_s_082"
    s "O-Oh. I see.{#ch23_s_082}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：何も知らないあんたが偉そうに、
    voice "ch23_l_057"
    l "What do you know, putting on airs!{#ch23_l_057}"

    # → next scene 878
    jump ch23_2_scene_878

label ch23_2_scene_878:

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：何か、いい考えでもあんの？  [voice 12339]
    voice "ch23_s_083"
    s "Got any good idea, then?{#ch23_s_083}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：無いことは無いけど……。
    voice "ch23_l_058"
    l "It's not that I don't… But yes. Maybe this is the only way.{#ch23_l_058}"

    # [SPRITE   lay5     image=+403, level=160, dir=1B]
    # サイト：おおっ。
    voice "ch23_s_084"
    s "Oh! You've thought of a plan?{#ch23_s_084}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：姫さま。
    voice "ch23_l_059"
    l "Princess. There's something I must ask your forgiveness for.{#ch23_l_059}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：わたくしにですか？
    voice "ch23_h_029"
    h "Of me? What is it?{#ch23_h_029}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay8     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 879
    jump ch23_3

    # ==== КОНЕЦ ЧАСТИ 2 ====
    jump ch23_3
    return

