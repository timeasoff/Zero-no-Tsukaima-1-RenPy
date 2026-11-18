# Глава 25, часть 1 (сцены 903–917): письмо для Табасы.
# Источник: ps2_source/chapters/chapter_26_手紙の秘密.txt (SCENE 903-917).

label ch25:
    $ tndl(None)
    # [TITLE] титульная карточка → overlay_screen (K=22)
    call overlay_screen("overlay", "Chapter Twenty-Five: 'Secret of the Letter'{#ch25_title}", isUseBlur=False, text_mode="black") from _call_overlay_screen_22
    pause(2)
    $ show_sprites()

label ch25_1_scene_903:

    # [TITLE title("手紙の秘密")]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # サイト：（演劇が終わってから、かれこれ数日。
    s "(Several days have passed since the play ended. We still have no clue about the bomber.){#ch25_s_001}"

    # サイト：（調査は続けてるんだけど、
    s "(I keep investigating, but I can't get any solid information. Louise is getting irritable, too…){#ch25_s_002}"

    # サイト：（ギーシュとモンモランシーには
    s "(I was right to send Guiche and Montmorency home.){#ch25_s_003}"

    # サイト：（しかし、いつまでこの状態が
    s "(But how long will this go on…?){#ch25_s_004}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1154, level=200]
    $ fade_fx("id(1154)")
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
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：なぁ、ルイズ。
    voice "ch25_s_005"
    s "Hey, Louise. We've been in Tristain for days now—is this really okay?{#ch25_s_005}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：そんなのしょうがないじゃない。
    voice "ch25_l_001"
    l "What do you expect? We can't find any solid clue about the bomber.{#ch25_l_001}"

    # サイト：いや、ないならないでさ、
    voice "ch25_s_006"
    s "No, I mean—if there's no clue, we should at least search more seriously…{#ch25_s_006}"

    # ルイズ：じゃあ、探してきて。  [voice 6768]
    voice "ch25_l_002"
    l "Then go look for one.{#ch25_l_002}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：どこでだよ？  [voice 12390]
    voice "ch25_s_007"
    s "Where?{#ch25_s_007}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：わたしが知ってるわけないじゃない。  [voice 6769]
    voice "ch25_l_003"
    l "How should I know?{#ch25_l_003}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そりゃ、そうだろうけど……。  [voice 12391]
    voice "ch25_s_008"
    s "Well, I suppose…{#ch25_s_008}"

    # ルイズ：どうしたの？
    voice "ch25_l_004"
    l "What is it? Go find that clue already.{#ch25_l_004}"

    # サイト：いやぁ……。  [voice 12392]
    voice "ch25_s_009"
    s "Ugh…{#ch25_s_009}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+500, level=160, dir=1B]
    # シエスタ：でしたら、わたしもサイトさんと一緒に
    voice "ch25_si_001"
    si "In that case, I'll help Saito-san search for clues, too…{#ch25_si_001}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：えっ、本当に！？
    voice "ch25_s_010"
    s "Eh, really!? You really are kind, Siesta.{#ch25_s_010}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay7     image=+964, level=160, dir=1B]
    # ハルナ：じゃあ、私も……。  [voice 2429]
    voice "ch25_ha_001"
    ha "Then I'll come, too.{#ch25_ha_001}"

    # サイト：春奈まで……。
    voice "ch25_s_011"
    s "Even Haruna… How lucky I am to have such kind classmates.{#ch25_s_011}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：ダーリンが行くなら、どこでもついていくわ。  [voice 3449]
    voice "ch25_k_001"
    k "If darling is going, I'll follow him anywhere.{#ch25_k_001}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：緊急脱出。  [voice 15654]
    voice "ch25_t_001"
    t "Emergency evacuation.{#ch25_t_001}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ちょっと、なによー！
    voice "ch25_l_005"
    l "Hey, what's the big idea!? Leaving me out like that!{#ch25_l_005}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+966, level=160, dir=1B]
    # ハルナ：ルイズさんは平賀くんを酷使しすぎなんです！  [voice 2430]
    voice "ch25_ha_002"
    ha "Louise-san overworks Hiraga-kun!{#ch25_ha_002}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     image=+504, level=160, dir=1B]
    # シエスタ：そうですよ。
    voice "ch25_si_002"
    si "That's right. Could you treat him a little more kindly…?{#ch25_si_002}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：だって、使い魔は使い魔じゃない！
    voice "ch25_l_006"
    l "Because a familiar is a familiar! Nothing more, nothing less!{#ch25_l_006}"

    # サイト：（なんだかんだ言ったって、みんな手がかりが
    s "(Whatever you say, they're all just frustrated about having no clues…){#ch25_s_012}"

    # [SE       se0      play=+82]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ん？
    voice "ch25_s_013"
    s "Hmm? What's this? A letter slipped under the door…{#ch25_s_013}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：えっ、手紙？
    voice "ch25_l_007"
    l "Eh, a letter? From whom?{#ch25_l_007}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：さあ？
    voice "ch25_s_014"
    s "Beats me… I can't read this script. It's probably not addressed to you, Louise?{#ch25_s_014}"

    # ルイズ：早く見せて。
    voice "ch25_l_008"
    l "Show it here. Honestly, learn to read at least writing, would you?{#ch25_l_008}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：はいはい、ご主人様。  [voice 12397]
    voice "ch25_s_015"
    s "Yes, yes, mistress.{#ch25_s_015}"

    # ルイズ：これ、わたし宛てじゃないわ。
    voice "ch25_l_009"
    l "This isn't addressed to me. It's to Tabitha.{#ch25_l_009}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch25_t_002}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：それにしても、わざわざ出先の宿屋に
    voice "ch25_s_016"
    s "Even so, having a letter delivered to our lodgings while we're away from home… It must be urgent.{#ch25_s_016}"

    # タバサ：……。
    t "…{#ch25_t_003}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch25_t_004}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：……あれ？
    voice "ch25_s_017"
    s "…Huh? What's wrong, Tabitha? You look gloomy.{#ch25_s_017}"

    # タバサ：……。
    t "…{#ch25_t_005}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：ねぇ、タバサ。
    voice "ch25_k_002"
    k "Hey, Tabitha. That letter—could it be…{#ch25_k_002}"

    # タバサ：……うん。  [voice 15655]
    voice "ch25_t_006"
    t "…Mm.{#ch25_t_006}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ん？
    voice "ch25_s_018"
    s "Hmm? Something happened?{#ch25_s_018}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：実はね……。
    voice "ch25_k_003"
    k "Actually… Tabitha is highly skilled—skilled enough to hold the title of Chevalier.{#ch25_k_003}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：（シュヴァリエの称号……。
    s "(The title of Chevalier… What kind of title is that?){#ch25_s_019}"

    menu:
        "A knight's title?{#ch25_1_c_903_1}":
            jump ch25_1_scene_904
        "A chef's title?{#ch25_1_c_903_2}":
            jump ch25_1_scene_905
        "A mage's title?{#ch25_1_c_903_3}":
            jump ch25_1_scene_906

label ch25_1_scene_904:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：タバサって、魔法使いかと思ったら
    voice "ch25_s_020"
    s "I thought Tabitha was a mage, but she's a knight? So 'Chevalier' is a knight's title, right?{#ch25_s_020}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # ルイズ：サイト……。  [voice 6776]
    voice "ch25_l_010"
    l "Saito…{#ch25_l_010}"

    # キュルケ：ダーリン……。  [voice 3452]
    voice "ch25_k_004"
    k "Darling…{#ch25_k_004}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：えっ、ええっ！？
    voice "ch25_s_021"
    s "Eh, eh!? Why are you both looking at me like that!?{#ch25_s_021}"

    # ルイズ：シュヴァリエというのはね、
    voice "ch25_l_011"
    l "A 'Chevalier' is a title granted to those who've achieved great deeds.{#ch25_l_011}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：なるほどね。  [voice 12403]
    voice "ch25_s_022"
    s "I see.{#ch25_s_022}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # → next scene 907
    jump ch25_1_scene_907

label ch25_1_scene_905:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：実は……料理人だったのか？  [voice 12404]
    voice "ch25_s_023"
    s "Actually… She was a cook, perhaps?{#ch25_s_023}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……何言ってんの、あんた？  [voice 6778]
    voice "ch25_l_012"
    l "…What are you talking about, you?{#ch25_l_012}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：えっ、違うの？
    voice "ch25_s_024"
    s "Eh? Am I wrong? Isn't 'Chevalier' a cook's title?{#ch25_s_024}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ぜんぜん違うわ！  [voice 6779]
    voice "ch25_l_013"
    l "Not remotely!{#ch25_l_013}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：シュヴァリエというのはね、
    voice "ch25_k_005"
    k "A 'Chevalier' is a title granted to those who've achieved great deeds.{#ch25_k_005}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：ははは、そうだったんだ……。  [voice 12406]
    voice "ch25_s_025"
    s "Ha ha, so that's it…{#ch25_s_025}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # → next scene 907
    jump ch25_1_scene_907

label ch25_1_scene_906:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # サイト：もしかして、魔法使いの称号なのか？  [voice 12407]
    voice "ch25_s_026"
    s "Could it be a mage's title, then?{#ch25_s_026}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：うーん。
    voice "ch25_k_006"
    k "Hmm. It's not exactly right, but not completely wrong, either.{#ch25_k_006}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：シュヴァリエというのはね、
    voice "ch25_l_014"
    l "A 'Chevalier' is a title granted to those who've achieved great deeds.{#ch25_l_014}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：へー。  [voice 12408]
    voice "ch25_s_027"
    s "Huh.{#ch25_s_027}"

    # → next scene 907
    jump ch25_1_scene_907

label ch25_1_scene_907:

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # ルイズ：ということは……。
    voice "ch25_l_015"
    l "Which means… Tabitha did something to earn such a title?{#ch25_l_015}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：そうよ。
    voice "ch25_k_007"
    k "That's right. Tabitha is amazing!{#ch25_k_007}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：へぇー、大したもんだなぁ。  [voice 12409]
    voice "ch25_s_028"
    s "Wow, impressive.{#ch25_s_028}"

    # [SPRITE   lay5     level=157]
    # [LAYER    lay0     image=+588, level=152, dir=1A]
    # [SPRITE   lay6     level=154]
    # タバサ：……。
    t "…{#ch25_t_007}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=156, dir=1A]
    # ルイズ：で、タバサがシュヴァリエなのと、今回の手紙。
    voice "ch25_l_016"
    l "So—is Tabitha's Chevalier title connected to this letter somehow?{#ch25_l_016}"

    # キュルケ：実はタバサって、毎回ある国から任務を
    voice "ch25_k_008"
    k "Actually, Tabitha gets requests for missions from a certain country from time to time…{#ch25_k_008}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+390, level=157, dir=1A]
    # サイト：だけど？  [voice 12410]
    voice "ch25_s_029"
    s "But?{#ch25_s_029}"

    # [SPRITE   lay6     image=+682, level=154, dir=1A]
    # キュルケ：……。  [voice 3457]
    voice "ch25_k_009"
    k "…{#ch25_k_009}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+594, level=152, dir=1A]
    # タバサ：……。
    t "…{#ch25_t_008}"

    # キュルケ：その内容は非常に困難。
    voice "ch25_k_010"
    k "The missions are extremely difficult. They're the kind only Tabitha could pull off.{#ch25_k_010}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=156, dir=1A]
    # ルイズ：ちょ、ちょっと。
    voice "ch25_l_017"
    l "Wait—is this mission difficult, too?{#ch25_l_017}"

    # [LAYER    lay0     image=+588, level=152, dir=1A]
    # タバサ：……。
    t "…{#ch25_t_009}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+429, level=157, dir=2A]
    # サイト：なあ、タバサ。
    voice "ch25_s_030"
    s "Say, Tabitha. If you don't mind, could you tell me what's in that letter, too?{#ch25_s_030}"

    # サイト：何か力になれるかもしれないだろ？  [voice 12412]
    voice "ch25_s_031"
    s "Maybe I could be of some help.{#ch25_s_031}"

    # [LAYER    lay0     image=+594, level=152, dir=1A]
    # タバサ：……。
    t "…{#ch25_t_010}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     x=64, y=0]
    # サイト：あっ、タバサ……。  [voice 12413]
    voice "ch25_s_032"
    s "Ah, Tabitha…{#ch25_s_032}"

    # [SE       se0      play=+57]
    # [SE       se0      play=+56]
    # サイト：出てっちゃったよ……。  [voice 12414]
    voice "ch25_s_033"
    s "She left…{#ch25_s_033}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 908
    jump ch25_1_scene_908

label ch25_1_scene_908:

    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：やっぱり、あの手紙のことを聞いたのが
    voice "ch25_l_018"
    l "Maybe asking about that letter was a mistake, wasn't it?{#ch25_l_018}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：そりゃあ、任務だもの。
    voice "ch25_k_011"
    k "Of course it was. It's a mission. She didn't want us to know.{#ch25_k_011}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：……ねえ、キュルケ？
    voice "ch25_l_019"
    l "…Hey, Kirche. Why do you get so gloomy over Tabitha?{#ch25_l_019}"

    # キュルケ：べ、べつにあたしは暗くなってなんか……。  [voice 3460]
    voice "ch25_k_012"
    k "I-I'm not gloomy or anything…{#ch25_k_012}"

    # ルイズ：どうやら、フクザツな事情があるみたいね。
    voice "ch25_l_020"
    l "Looks like there's a complicated story there. Doesn't it interest you, Saito?{#ch25_l_020}"

    menu:
        "I am a little curious{#ch25_1_c_908_1}":
            jump ch25_1_scene_909
        "Everyone has their reasons{#ch25_1_c_908_2}":
            jump ch25_1_scene_910
        "Not really{#ch25_1_c_908_3}":
            jump ch25_1_scene_911

label ch25_1_scene_909:

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そりゃあ、俺だって少しは……。  [voice 12415]
    voice "ch25_s_034"
    s "Well, I suppose I am a little curious…{#ch25_s_034}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：でしょう？
    voice "ch25_l_021"
    l "Right? Saito's curious, too, isn't he?{#ch25_l_021}"

    # → next scene 912
    jump ch25_1_scene_912

label ch25_1_scene_910:

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：でも、人には人の事情があるわけなんだし。  [voice 12416]
    voice "ch25_s_035"
    s "But, people have their own circumstances…{#ch25_s_035}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：なに言ってんのよ。
    voice "ch25_l_022"
    l "What are you talking about? Tabitha is our classmate and friend! Of course you'd worry about her!{#ch25_l_022}"

    # → next scene 912
    jump ch25_1_scene_912

label ch25_1_scene_911:

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：いや、別に。  [voice 12417]
    voice "ch25_s_036"
    s "No, I mean… I don't really care.{#ch25_s_036}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：別にって……。
    voice "ch25_l_023"
    l "You don't care… You're so cold.{#ch25_l_023}"

    # → next scene 912
    jump ch25_1_scene_912

label ch25_1_scene_912:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+29]
    play music t28 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ダーリン。  [voice 3461]
    voice "ch25_k_013"
    k "Darling.{#ch25_k_013}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：うん？  [voice 12418]
    voice "ch25_s_037"
    s "Hmm?{#ch25_s_037}"

    # キュルケ：お願いがあるんだけどいいかな？  [voice 3462]
    voice "ch25_k_014"
    k "Can I ask you a favor?{#ch25_k_014}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：無理なことでなければ……。  [voice 12419]
    voice "ch25_s_038"
    s "If it's not something impossible…{#ch25_s_038}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：ダーリンから手紙のことについてタバサに
    voice "ch25_k_015"
    k "I want you to ask Tabitha about that letter. I'm just… worried.{#ch25_k_015}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：俺が？  [voice 12420]
    voice "ch25_s_039"
    s "Me?{#ch25_s_039}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：なんでサイトが行くのよ？  [voice 6790]
    voice "ch25_l_024"
    l "Why Saito?{#ch25_l_024}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：うーん。
    voice "ch25_k_016"
    k "Hmm. Women's intuition, maybe?{#ch25_k_016}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：ダーリン、最近タバサと仲いいでしょ？  [voice 3465]
    voice "ch25_k_017"
    k "Darling, you've gotten close to Tabitha lately, haven't you?{#ch25_k_017}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：ギク。  [voice 12421]
    voice "ch25_s_040"
    s "Eep.{#ch25_s_040}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あの娘、黙ってるから分からないと
    voice "ch25_k_018"
    k "She may be quiet and you may think I can't tell, but I can see it perfectly well.{#ch25_k_018}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+307, level=140, dir=1A]
    # ルイズ：な、なんですって？
    voice "ch25_l_025"
    l "Wh-What was that!? You like small ones, don't you!{#ch25_l_025}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+505, level=140, dir=1B]
    # シエスタ：そ、そうなんですか、サイトさん。  [voice 15036]
    voice "ch25_si_003"
    si "I-Is that true, Saito-san?{#ch25_si_003}"

    # [SPRITE   lay2     image=+504, level=160, dir=1B]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：い、いや、誤解だって。  [voice 12422]
    voice "ch25_s_041"
    s "N-No, it's a misunderstanding!{#ch25_s_041}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：まぁ、そのことは今度尋問すれば
    voice "ch25_k_019"
    k "Well, we can question you about that later. For now, Tabitha is the priority.{#ch25_k_019}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：わ、分かったわ。
    voice "ch25_l_026"
    l "I-Understood. There's one thing I can't accept, but you're right—Saito is the right person for this.{#ch25_l_026}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：サイト、タバサの様子を見てきなさい。
    voice "ch25_l_027"
    l "Saito, go check on Tabitha. Understand? That's an order. Don't come back empty-handed.{#ch25_l_027}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：はいはい……。  [voice 12423]
    voice "ch25_s_042"
    s "Yes, yes…{#ch25_s_042}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 913
    jump ch25_1_scene_913

label ch25_1_scene_913:

    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：タバサのヤツ……。
    voice "ch25_s_043"
    s "Tabitha… Where did she go?{#ch25_s_043}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # サイト：……って、あっさり見つかったよ。  [voice 12425]
    voice "ch25_s_044"
    s "…Oh, I found her easily.{#ch25_s_044}"

    # タバサ：……。
    t "…{#ch25_t_011}"

    menu:
        "Call out to her{#ch25_1_c_913_1}":
            jump ch25_1_scene_914
        "Leave her alone{#ch25_1_c_913_2}":
            jump ch25_1_scene_915
        "What was that letter?{#ch25_1_c_913_3}":
            jump ch25_1_scene_916

label ch25_1_scene_914:

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # サイト：まぁ、あんまり考えてもしかたがないよな。
    voice "ch25_s_045"
    s "Well, there's no point overthinking it. For now, let me call out to her.{#ch25_s_045}"

    # サイト：おーい、タバサー。  [voice 12427]
    voice "ch25_s_046"
    s "Hey there, Tabitha~.{#ch25_s_046}"

    # → next scene 917
    jump ch25_1_scene_917

label ch25_1_scene_915:

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # サイト：しばらく、そっとしておいてやるか。
    voice "ch25_s_047"
    s "I'll leave her alone for a while. She must have her own way of sorting out her feelings…{#ch25_s_047}"

    # サイト：……ってだめだ。
    voice "ch25_s_048"
    s "…No, this won't do. If I go back like this, Louise will beat me to death.{#ch25_s_048}"

    # サイト：おーい、タバサー。  [voice 12430]
    voice "ch25_s_049"
    s "Hey there, Tabitha~.{#ch25_s_049}"

    # → next scene 917
    jump ch25_1_scene_917

label ch25_1_scene_916:

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # サイト：あの手紙ってなんだったんだろう。
    voice "ch25_s_050"
    s "What was in that letter? Something that made Tabitha run out of the room?{#ch25_s_050}"

    # サイト：切ない内容？
    voice "ch25_s_051"
    s "Something painful? Something sad? Something difficult?{#ch25_s_051}"

    # サイト：……。  [voice 12433]
    voice "ch25_s_052"
    s "…{#ch25_s_052}"

    # サイト：……。  [voice 12434]
    voice "ch25_s_053"
    s "…{#ch25_s_053}"

    # サイト：まぁ、考えても答えがでるはずもないし、
    voice "ch25_s_054"
    s "Well, thinking won't give me an answer. Let me just ask her directly.{#ch25_s_054}"

    # サイト：おーい、タバサー。  [voice 12436]
    voice "ch25_s_055"
    s "Hey there, Tabitha~.{#ch25_s_055}"

    # → next scene 917
    jump ch25_1_scene_917

label ch25_1_scene_917:

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [LAYER    lay0     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # タバサ：何？  [voice 15656]
    voice "ch25_t_012"
    t "What?{#ch25_t_012}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：えーっと、タバサさん。  [voice 12437]
    voice "ch25_s_056"
    s "Um, Tabitha-san.{#ch25_s_056}"

    # タバサ：……。
    t "…{#ch25_t_013}"

    # サイト：あの、手紙のことでちょっとお話を聞ければ
    voice "ch25_s_057"
    s "Um, I wouldn't mind hearing about that letter…{#ch25_s_057}"

    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch25_t_014}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：あははははは……。  [voice 12439]
    voice "ch25_s_058"
    s "Ah ha ha ha ha…{#ch25_s_058}"

    # タバサ：……。
    t "…{#ch25_t_015}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：あのぉ、せめて一言だけで結構ですから、
    voice "ch25_s_059"
    s "Um, even just one word would be fine—please just react somehow…{#ch25_s_059}"

    # タバサ：……。
    t "…{#ch25_t_016}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ダ、ダメ？  [voice 12441]
    voice "ch25_s_060"
    s "N-No?{#ch25_s_060}"

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：分かった。
    voice "ch25_t_017"
    t "All right. I'll talk.{#ch25_t_017}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：良かった……。
    voice "ch25_s_061"
    s "Great… So first…{#ch25_s_061}"

    # タバサ：時間がほしい。  [voice 15658]
    voice "ch25_t_018"
    t "I need time.{#ch25_t_018}"

    # サイト：いいけど、なんで？  [voice 12443]
    voice "ch25_s_062"
    s "Fine, but why?{#ch25_s_062}"

    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：時間。  [voice 15659]
    voice "ch25_t_019"
    t "Time.{#ch25_t_019}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：う、うん……。  [voice 12444]
    voice "ch25_s_063"
    s "O-Okay…{#ch25_s_063}"

    # タバサ：じゃあ。  [voice 15660]
    voice "ch25_t_020"
    t "Then.{#ch25_t_020}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：って、どこかに行っちゃったんですけど！！  [voice 12445]
    voice "ch25_s_064"
    s "Wait—and she walked off somewhere!!{#ch25_s_064}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 918
    jump ch25_2

    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch25_2
    return

