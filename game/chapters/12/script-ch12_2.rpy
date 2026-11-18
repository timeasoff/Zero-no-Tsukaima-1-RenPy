# Глава 12, часть 2 (сцены 525–534): Акина против Харуны, Пустота, крыша.
# Источник: ps2_source/chapters/chapter_13_もう一人のハルナ.txt (SCENE 525-534).

label ch12_2:
    $ tndl(None)
    $ show_sprites()

label ch12_2_scene_525:

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：どこかの幸せな童話のように、
    voice "ch12_ak_011"
    ak "Like some happy fairy tale, clicking your heels three times won't take you back to your world.{#ch12_ak_011}"

    # アキナ：誰も本当に助けてなんてくれない。
    voice "ch12_ak_012"
    ak "No one will ever really save us. That's our reality!{#ch12_ak_012}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ちくしょう、春奈はどうなるんだよ！  [voice 13331]
    voice "ch12_s_031"
    s "Damn it, what's going to happen to Haruna!?{#ch12_s_031}"

    # アキナ：別にどうなってもいいだろう？
    voice "ch12_ak_013"
    ak "Who cares? She'll just disappear, that's all.{#ch12_ak_013}"

    # [SE       se0      play=+65]
    # [SPRITE   lay5     image=+471, level=160, dir=3B]
    # サイト：な、なんだとぉ！  [voice 13332]
    voice "ch12_s_032"
    s "W-What did you say!?{#ch12_s_032}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # ハルナ：きゃっ！
    voice "ch12_ha_009"
    ha "Eek! W-Why are you pointing a sword at me, Hiraga-kun!?{#ch12_ha_009}"

    # [SPRITE   lay5     image=+473, level=160, dir=3B]
    # サイト：春奈……。  [voice 13333]
    voice "ch12_s_033"
    s "Haruna…{#ch12_s_033}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：あははは……ばーか！  [voice 211]
    voice "ch12_ak_014"
    ak "Ahahaha… idiot!{#ch12_ak_014}"

    # [SPRITE   lay5     image=+471, level=160, dir=3B]
    # サイト：ひ、卑怯な！  [voice 13334]
    voice "ch12_s_034"
    s "T-That's dirty!{#ch12_s_034}"

    # デルフリンガー：おい、相棒。
    voice "ch12_d_001"
    d "Hey, partner. That girl's movements are no joke—watch out.{#ch12_d_001}"

    # サイト：そんなこといわれても！  [voice 13335]
    voice "ch12_s_035"
    s "Don't tell me that!{#ch12_s_035}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # ハルナ：そんな目で私を見ないで……。  [voice 2621]
    voice "ch12_ha_010"
    ha "Don't look at me like that…{#ch12_ha_010}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：なんてね、あはは……。  [voice 212]
    voice "ch12_ak_015"
    ak "Just kidding, ahaha…{#ch12_ak_015}"

    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：……っ！
    voice "ch12_ak_016"
    ak "…! What's this presence!?{#ch12_ak_016}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay21    hide]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 526
    jump ch12_2_scene_526

label ch12_2_scene_526:

    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+95]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay21    vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [SPRITE   lay11    vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay21    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay11    hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 1000)]
    # アキナ：きゃあぁぁぁっ！  [voice 214]
    voice "ch12_ak_017"
    ak "Eeeeeek!{#ch12_ak_017}"

    # サイト：な、なんだぁぁぁっ！  [voice 13336]
    voice "ch12_s_036"
    s "W-What the hell!?{#ch12_s_036}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # ルイズ：自分の危険もかえりみず、
    voice "ch12_l_033"
    l "Rushing out to meet Saito without a thought for my own danger… and what are you two playing at!? {#ch12_l_033}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：な、なな、なにをじゃれあってるのかしら？
    voice "ch12_l_034"
    l "W-What are you two playing at!?{#ch12_l_034}"

    # サイト：ル、ルイズ！  [voice 13337]
    voice "ch12_s_037"
    s "L-Louise!{#ch12_s_037}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ちょっと待て、ルイズ！
    voice "ch12_s_038"
    s "Wait, Louise! You've got it wrong!{#ch12_s_038}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：いたたたた……。
    voice "ch12_ak_018"
    ak "Ow ow ow… What's your problem, Louise! Trying to kill me!?{#ch12_ak_018}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：……？
    voice "ch12_l_035"
    l "…? Haruna? What's with that way of speaking?{#ch12_l_035}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：いままでの優等生ぶりは嘘で、
    voice "ch12_l_036"
    l "So your goody-two-shoes act was a lie, and this is the real you?{#ch12_l_036}"

    # アキナ：うるさいうるさい！  [voice 216]
    voice "ch12_ak_019"
    ak "Shut up, shut up!{#ch12_ak_019}"

    # アキナ：あたしをハルナと呼ぶな！
    voice "ch12_ak_020"
    ak "Don't call me Haruna! I'm Akina!{#ch12_ak_020}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：どういうことよ？  [voice 7257]
    voice "ch12_l_037"
    l "What's going on here?{#ch12_l_037}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ウェザリーに操られてるらしいんだ。
    voice "ch12_s_039"
    s "Looks like Weatherly's controlling her. She says she's the bomb-thrower.{#ch12_s_039}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：なんですって！
    voice "ch12_l_038"
    l "What!? So Weatherly's the mastermind!?{#ch12_l_038}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：だ、だったら、あの舞台は何だったのよ。
    voice "ch12_l_039"
    l "T-Then what was that play all about? Hmph, making fools of us.{#ch12_l_039}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：ウェザリー様を呼び捨てにするな。
    voice "ch12_ak_021"
    ak "Don't say Weatherly-sama's name without honorifics. And don't ignore me!{#ch12_ak_021}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SE       se0      play=+63]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay21    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay11    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay21    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay11    hide, reset]
    # [SPRITE   lay5     reset]
    # サイト：うわっ！  [voice 13340]
    voice "ch12_s_040"
    s "Whoa!{#ch12_s_040}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：アキナって言ったわね？
    voice "ch12_l_040"
    l "You said Akina, right? What do you want?{#ch12_l_040}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：言っただろ、トリスタニアでの破壊活動よ。
    voice "ch12_ak_022"
    ak "I told you, didn't I? Sabotage in Tristain. As the bomb-thrower.{#ch12_ak_022}"

    # アキナ：魔法学院に入り込んだのは、
    voice "ch12_ak_023"
    ak "I was supposed to infiltrate the academy to gather information about its secrets, though…{#ch12_ak_023}"

    # ルイズ：学院の持つ秘密？  [voice 7261]
    voice "ch12_l_041"
    l "The academy's secrets?{#ch12_l_041}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：おまえのことだよ、ルイズ。
    voice "ch12_ak_024"
    ak "You, Louise. The power of Void you carry.{#ch12_ak_024}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：な、なんですって！  [voice 7262]
    voice "ch12_l_042"
    l "W-What!?{#ch12_l_042}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：サイトに出会っちまったせいで
    voice "ch12_ak_025"
    ak "Meeting Saito made Haruna's consciousness stronger and threw off my plans, but…{#ch12_ak_025}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：この力は姫さまの……。
    voice "ch12_l_043"
    l "This power belongs to the Princess… to the Queen.{#ch12_l_043}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：あなた達のような下郎が
    voice "ch12_l_044"
    l "For lowly wretches like you to touch it so casually—outrageous!{#ch12_l_044}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：ふん、面白い。
    voice "ch12_ak_026"
    ak "Hmph, how interesting. However polite you act, in the end it's power that decides.{#ch12_ak_026}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：さあ、出ておいで！  [voice 224]
    voice "ch12_ak_027"
    ak "Now, come out!{#ch12_ak_027}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay11    image=+1105, level=160, dir=1A]
    # [SPRITE   lay12    image=+1105, level=160, dir=1A]
    # 魔導士：……！
    mage "…!{#ch12_mage_001}"

    # [SPRITE   lay11    hide]
    # [SPRITE   lay12    hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：く、くそぉっ！  [voice 13341]
    voice "ch12_s_041"
    s "D-Damn it!{#ch12_s_041}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 527
    jump ch12_2_scene_527

label ch12_2_scene_527:

    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：よ、よくも……。  [voice 225]
    voice "ch12_ak_028"
    ak "H-How dare you…!{#ch12_ak_028}"

    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：ふふふ、思い知ったかしら？  [voice 7265]
    voice "ch12_l_045"
    l "Fufufu, now do you understand?{#ch12_l_045}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # ハルナ：た、助けて。
    voice "ch12_ha_011"
    ha "H-Help me, Hiraga-kun.{#ch12_ha_011}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：また、春奈のふりをしようという作戦か。  [voice 13342]
    voice "ch12_s_042"
    s "Another trick to make me think she's Haruna, is it?{#ch12_s_042}"

    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：やめろ、出てくるんじゃねぇ！
    voice "ch12_ak_029"
    ak "Stop it, don't come out! I am me!{#ch12_ak_029}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # ハルナ：ひ、平賀く……。  [voice 2623]
    voice "ch12_ha_012"
    ha "H-Hiraga-kun…{#ch12_ha_012}"

    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：ちくしょう！
    voice "ch12_ak_030"
    ak "Damn it! Stop it, Haruna!{#ch12_ak_030}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：お、おいっ。
    voice "ch12_s_043"
    s "H-Hey. Could it really be Haruna…?{#ch12_s_043}"

    # アキナ：黙れ、あたしはアキナだ！  [voice 228]
    voice "ch12_ak_031"
    ak "Shut up. I am Akina!{#ch12_ak_031}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：きゃっ！
    voice "ch12_l_046"
    l "Eek! W-Wait!{#ch12_l_046}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：しまった！
    voice "ch12_s_044"
    s "No! Haruna!{#ch12_s_044}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # null：………。  (no voice — пропущено по образцу ch11_2)
    # [BG       stage    hide]
    # [BG       stage    image=+47, level=200]
    $ fade_fx("id(47)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：くそっ、アキナを取り逃がしちまうなんて。
    voice "ch12_s_045"
    s "Damn, I let Akina get away. What a blunder.{#ch12_s_045}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：何なのよ。
    voice "ch12_l_047"
    l "What was that? Haruna and Akina…?{#ch12_l_047}"

    # [SPRITE   lay19    image=+940, level=151, dir=1A]
    # [SPRITE   lay1     level=154]
    # [SPRITE   lay5     level=155]
    # デルフリンガー：催眠魔法だな。
    voice "ch12_d_002"
    d "Hypnosis. They've implanted a false second personality into her to control and manipulate her.{#ch12_d_002}"

    # デルフリンガー：それともうひとつ。
    voice "ch12_d_003"
    d "And one more thing. The girl's physical abilities are boosted by another suggestion or spell.{#ch12_d_003}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     image=+429, level=155, dir=2A]
    # サイト：なんてこった……。
    voice "ch12_s_046"
    s "Unbelievable… Haruna…{#ch12_s_046}"

    # [SE       se0      play=+63]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay21    vibrate=14]
    # [SPRITE   lay19    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay21    hide, reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay1     reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay5     image=+394, level=155, dir=1A]
    # サイト：そうだ！
    voice "ch12_s_047"
    s "Right! How's the battle going!?{#ch12_s_047}"

    # ルイズ：まだ、続いているわ。
    voice "ch12_l_048"
    l "Still going. It's actually getting more intense, if anything.{#ch12_l_048}"

    # [SPRITE   lay1     image=+308, level=154, dir=1A]
    # ルイズ：どうやらレコン・キスタは、
    voice "ch12_l_049"
    l "Apparently Reconquista used the repair work after the bombings to slip in soldiers and plant cannons…{#ch12_l_049}"

    # ルイズ：今回のトリスタニアへの攻撃を準備していたの。  [voice 7270]
    voice "ch12_l_050"
    l "—and prepare this attack on Tristain.{#ch12_l_050}"

    # [SPRITE   lay1     image=+335, level=154, dir=2A]
    # ルイズ：この攻撃の混乱に乗じて、残った空中艦隊で、
    voice "ch12_l_051"
    l "They mean to use the confusion to strike Tristain with the remaining aerial fleet, I'd wager.{#ch12_l_051}"

    # [SPRITE   lay1     image=+302, level=154, dir=1A]
    # ルイズ：すでにこちらに向かってくる空中艦隊が
    voice "ch12_l_052"
    l "I hear the fleet has already been spotted heading this way.{#ch12_l_052}"

    # [SPRITE   lay5     image=+396, level=155, dir=1A]
    # サイト：じゃあ、早く援軍に向かわないと！  [voice 13348]
    voice "ch12_s_048"
    s "Then we have to get to the reinforcements fast!{#ch12_s_048}"

    # [SPRITE   lay1     image=+335, level=154, dir=2A]
    # ルイズ：……ええ。
    voice "ch12_l_053"
    l "…Yes. About that.{#ch12_l_053}"

    # [SPRITE   lay1     image=+302, level=154, dir=1A]
    # ルイズ：姫さまからこのトリスタニアで
    voice "ch12_l_054"
    l "I got permission from the Princess to use Void magic here in Tristain.{#ch12_l_054}"

    # ルイズ：虚無の魔法で艦隊を追い返してみせるわ。  [voice 7275]
    voice "ch12_l_055"
    l "I'll drive the fleet back with Void.{#ch12_l_055}"

    # [SPRITE   lay5     image=+394, level=155, dir=1A]
    # サイト：そ、それはいいけど。
    voice "ch12_s_049"
    s "T-That's fine, but if you use that magic here, the whole capital will be blown away!{#ch12_s_049}"

    # [SPRITE   lay1     image=+335, level=154, dir=2A]
    # ルイズ：大丈夫よ。
    voice "ch12_l_056"
    l "It's all right. I won't use Explosion.{#ch12_l_056}"

    # サイト：どういうことだよ！  [voice 13350]
    voice "ch12_s_050"
    s "What do you mean!?{#ch12_s_050}"

    # [SPRITE   lay1     image=+302, level=154, dir=1A]
    # ルイズ：虚無の系列は、エクスプロージョンだけ
    voice "ch12_l_057"
    l "The Void lineage isn't only Explosion.{#ch12_l_057}"

    # [SPRITE   lay5     image=+429, level=155, dir=2A]
    # サイト：（……確かに。
    s "(True enough. Now that Void is barely known, we can catch the enemy off guard…){#ch12_s_051}"

    menu:
        "Believe Louise.{#ch12_2_c_527_1}":
            jump ch12_2_scene_528
        "It's Louise, isn't it?{#ch12_2_c_527_2}":
            jump ch12_2_scene_529
        "Come what may!{#ch12_2_c_527_3}":
            jump ch12_2_scene_530

label ch12_2_scene_528:

    # [SPRITE   lay5     image=+429, level=155, dir=2A]
    # [SPRITE   lay1     image=+302, level=154, dir=1A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+47, level=200]
    $ fade_fx("id(47)")
    # [SPRITE   lay5     image=+394, level=155, dir=1A]
    # サイト：よし、ルイズに……、ご主人様に任せたぜ！  [voice 13351]
    voice "ch12_s_052"
    s "All right, Louise… I mean, mistress, it's in your hands!{#ch12_s_052}"

    # [SPRITE   lay1     image=+304, level=154, dir=1A]
    # ルイズ：よろしい。
    voice "ch12_l_058"
    l "Good. That's my familiar.{#ch12_l_058}"

    # → next scene 531
    jump ch12_2_scene_531

label ch12_2_scene_529:

    # [SPRITE   lay5     image=+429, level=155, dir=2A]
    # [SPRITE   lay1     image=+302, level=154, dir=1A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+47, level=200]
    $ fade_fx("id(47)")
    # [SPRITE   lay5     image=+396, level=155, dir=1A]
    # サイト：（……でも、ルイズだしなあ？）
    s "(But… it is Louise, isn't it…?){#ch12_s_053}"

    # [SPRITE   lay1     image=+306, level=154, dir=1A]
    # ルイズ：なによ、その不安そうな顔は！
    voice "ch12_l_059"
    l "What's that worried look for! You're still my familiar, aren't you!? Perhaps you need a punishment right now…{#ch12_l_059}"

    # [SPRITE   lay5     image=+394, level=155, dir=1A]
    # サイト：り、了解であります。
    voice "ch12_s_054"
    s "U-Understood, mistress!{#ch12_s_054}"

    # [SPRITE   lay1     image=+304, level=154, dir=1A]
    # ルイズ：よろしい！  [voice 7280]
    voice "ch12_l_060"
    l "Good!{#ch12_l_060}"

    # → next scene 531
    jump ch12_2_scene_531

label ch12_2_scene_530:

    # [SPRITE   lay5     image=+429, level=155, dir=2A]
    # [SPRITE   lay1     image=+302, level=154, dir=1A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+47, level=200]
    $ fade_fx("id(47)")
    # [SPRITE   lay5     image=+394, level=155, dir=1A]
    # サイト：分かったよ！
    voice "ch12_s_055"
    s "All right! Come what may!{#ch12_s_055}"

    # [SPRITE   lay1     image=+335, level=154, dir=2A]
    # ルイズ：なんか、納得できないけど、
    voice "ch12_l_061"
    l "Somehow, you don't look convinced, but I think you understood.{#ch12_l_061}"

    # → next scene 531
    jump ch12_2_scene_531

label ch12_2_scene_531:

    # [SPRITE   lay1     image=+304, level=154, dir=1A]
    # [SPRITE   lay5     image=+394, level=155, dir=1A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+47, level=200]
    $ fade_fx("id(47)")
    # [SPRITE   lay5     image=+429, level=155, dir=2A]
    # サイト：それで、魔法はどこで仕掛けるんだ？
    voice "ch12_s_056"
    s "So where are you casting the spell? I didn't bring the Zero Fighter.{#ch12_s_056}"

    # [SPRITE   lay1     image=+302, level=154, dir=1A]
    # ルイズ：それは決めてるわ。  [voice 7282]
    voice "ch12_l_062"
    l "I've decided.{#ch12_l_062}"

    # [SPRITE   lay1     image=+339, level=154, dir=2A]
    # ルイズ：王宮のいちばん上よ！  [voice 7283]
    voice "ch12_l_063"
    l "The very top of the palace!{#ch12_l_063}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 532
    jump ch12_2_scene_532

label ch12_2_scene_532:

    # [BG       stage    image=+47, level=200]
    $ fade_fx("id(47)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：ハァハァハァハァハァ……。  [voice 229]
    voice "ch12_ak_032"
    ak "Haa haa haa haa haa…{#ch12_ak_032}"

    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：チクショウチクショウ……。
    voice "ch12_ak_033"
    ak "Damn, damn… that Haruna is getting in my way!{#ch12_ak_033}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：（こんなことをしてどうなるというの。
    voice "ch12_ha_013"
    ha "(What good will this do? Stop this foolishness…){#ch12_ha_013}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：うるさいうるさい！  [voice 231]
    voice "ch12_ak_034"
    ak "Shut up, shut up!{#ch12_ak_034}"

    # アキナ：あたしはあいつらを倒して、
    voice "ch12_ak_035"
    ak "I'll beat them and take Saito for myself!{#ch12_ak_035}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：（無理よ、そんなことしても
    voice "ch12_ha_014"
    ha "(It's no use. Even if you do, Hiraga-kun won't change…){#ch12_ha_014}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：じゃあ。
    voice "ch12_ak_036"
    ak "Then I'll just have Weatherly-sama tinker with your head.{#ch12_ak_036}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：あたし達だけを見てくれるサイトの
    voice "ch12_ak_037"
    ak "And I'll have a Saito who only looks at us.{#ch12_ak_037}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：そうだな。
    voice "ch12_ak_038"
    ak "All right. I suppose I can let you show your face once in a while.{#ch12_ak_038}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：（そんなことして、何になるの……）  [voice 2626]
    voice "ch12_ha_015"
    ha "(What good would that do…){#ch12_ha_015}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：じゃあ、サイトの隣に別の女がいる姿を、
    voice "ch12_ak_039"
    ak "Or would you rather watch another woman beside Saito forever?{#ch12_ak_039}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：あたしじゃない誰か、が……、いるんだぞ。  [voice 237]
    voice "ch12_ak_040"
    ak "Someone who isn't me… is there, you know.{#ch12_ak_040}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：（し、仕方ないじゃない。
    voice "ch12_ha_016"
    ha "(I-It can't be helped. If that's fate…){#ch12_ha_016}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：偽善者！
    voice "ch12_ak_041"
    ak "Hypocrite! Liar! Shut up, shut up!{#ch12_ak_041}"

    # アキナ：あたしはいやだ、他の女なんて許さない。
    voice "ch12_ak_042"
    ak "I won't have it—no other woman. If it were me… I could have Saito.{#ch12_ak_042}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：サイトの腕の中で抱きしめてもらえるんだぞ。
    voice "ch12_ak_043"
    ak "He'd hold me in his arms. Only me. Only me.{#ch12_ak_043}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：力を貸すんだ。
    voice "ch12_ak_044"
    ak "Lend me your power, Haruna.{#ch12_ak_044}"

    # アキナ：あんなルイズなんかやっつけて、
    voice "ch12_ak_045"
    ak "Let's beat that Louise and make Saito ours alone.{#ch12_ak_045}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay7     image=+955, level=160, dir=1A]
    # ハルナ：（やめて、やめて、やめて！）  [voice 2628]
    voice "ch12_ha_017"
    ha "(Stop, stop, stop!){#ch12_ha_017}"

    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：（そんなことは駄目！
    voice "ch12_ha_018"
    ha "(No! I don't want this! I don't want it at all!){#ch12_ha_018}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：よく言うよ。
    voice "ch12_ak_046"
    ak "Well said. I'm another you. I couldn't lie to myself.{#ch12_ak_046}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：（ちがうちがう……。
    voice "ch12_ha_019"
    ha "(No, no… it isn't like that!){#ch12_ha_019}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay7     hide]
    # [BG       stage    hide]
    # → next scene 533
    jump ch12_2_scene_533

label ch12_2_scene_533:

    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # ルイズ：今回の魔法のためには、
    voice "ch12_l_064"
    l "For this spell, we need the spot with the best view in the whole castle!{#ch12_l_064}"

    # ルイズ：それに、こないだもそうだったけど、
    voice "ch12_l_065"
    l "And, as last time, Void magic takes time to chant.{#ch12_l_065}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：両方とも、しっかり確保するのよ！
    voice "ch12_l_066"
    l "Secure both. Understood?{#ch12_l_066}"

    # サイト：分かってる！
    voice "ch12_s_057"
    s "I got it! Leave it to me!{#ch12_s_057}"

    # サイト：（……しかし、城内まで戦場になってるとはな。
    s "(Still, the castle grounds have turned into a battlefield too. This is rough…){#ch12_s_058}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ここが屋上か。  [voice 13356]
    voice "ch12_s_059"
    s "So this is the rooftop, huh.{#ch12_s_059}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay19    image=+944, level=160, dir=1A]
    # デルフリンガー：気をつけろ、相棒！  [voice 1371]
    voice "ch12_d_004"
    d "Careful, partner!{#ch12_d_004}"

    # [SE       se0      play=+63]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay21    vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [SPRITE   lay20    vibrate=21]
    # [SPRITE   lay19    vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [SPRITE   lay7     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay21    hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay20    hide, reset]
    # [SPRITE   lay19    reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……大丈夫！？
    voice "ch12_l_067"
    l "…You all right!? Saito!{#ch12_l_067}"

    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：な、なんとか大丈夫！  [voice 13357]
    voice "ch12_s_060"
    s "I-I'm fine, somehow!{#ch12_s_060}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：（……容赦なしかよ！）
    s "(No mercy at all, huh!){#ch12_s_061}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    hide]
    # [EVENT_CG event    image=+139, level=80]
    $ dissolve_fx("id(139)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # アキナ：……。
    ak "…{#ch12_ak_047}"

    # ウェザリー：あら。
    voice "ch12_w_001"
    w "My, what a coincidence… Or should I say, the cast has assembled?{#ch12_w_001}"

    # ウェザリー：ここで何をする気かしらないけど……。
    voice "ch12_w_002"
    w "I don't know what you plan to do here… but meeting me was your misfortune.{#ch12_w_002}"

    menu:
        "Haruna!{#ch12_2_c_533_1}":
            jump ch12_2_scene_534
        "Akina!{#ch12_2_c_533_2}":
            jump ch12_3
        "Weatherly!{#ch12_2_c_533_3}":
            jump ch12_3

label ch12_2_scene_534:

    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [EVENT_CG event    image=+139, level=80]
    $ dissolve_fx("id(139)")
    # サイト：春奈っ！  [voice 13358]
    voice "ch12_s_062"
    s "Haruna!{#ch12_s_062}"

    # [SPRITE   lay21    hide]
    # アキナ：あたしをその名前で呼ぶなと言ってるだろ！  [voice 244]
    voice "ch12_ak_048"
    ak "I told you not to call me that!{#ch12_ak_048}"

    # サイト：うるさい、春奈は春奈だ！  [voice 13359]
    voice "ch12_s_063"
    s "Shut up. Haruna is Haruna!{#ch12_s_063}"

    # サイト：絶対になんとかするから待ってるんだぞ！
    voice "ch12_s_064"
    s "I'll think of something, just wait for me! Haruna!{#ch12_s_064}"

    # → next scene 537
    jump ch12_3

    # ==== КОНЕЦ ЧАСТИ 2 ====
    jump ch12_3
    return

