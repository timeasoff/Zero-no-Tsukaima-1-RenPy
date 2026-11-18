# Глава 28, часть 1 (сцены 999–1007): секретный торт Табасы.
# Источник: ps2_source/chapters/chapter_29_夜の秘密.txt (SCENE 999-1007).

label ch28:
    $ tndl(None)
    $ show_sprites()

label ch28_1_scene_999:

    # [TITLE title("夜の秘密")]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1157, level=200]
    $ fade_fx("id(1157)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+12, level=200]
    $ fade_fx("id(12)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：ちょっと、ダーリン！
    voice "ch28_k_001"
    k "Hey, darling! What's the meaning of this!?{#ch28_k_001}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：どういうことって？  [voice 8018]
    voice "ch28_s_001"
    s "What do you mean, what's the meaning?{#ch28_s_001}"

    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：このあたしを差し置いて、タバサと夜な夜な
    voice "ch28_k_002"
    k "Going out on secret dates with Tabitha night after night—behind my back!{#ch28_k_002}"

    # サイト：えーっと……。
    voice "ch28_s_002"
    s "Um… I'm afraid I don't follow?{#ch28_s_002}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：なんですってぇーっ！
    voice "ch28_l_001"
    l "What was that!? You went behind my back and did something with Tabitha…{#ch28_l_001}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：毎晩、同じベッドで寝かせてあげてるのに、
    voice "ch28_l_002"
    l "I let you sleep in my bed every night—why would you sneak out to do that…{#ch28_l_002}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：いや、同じベッドで寝てたら、
    voice "ch28_s_003"
    s "No—if we were sleeping in the same bed, you'd normally notice me sneaking out, wouldn't you?{#ch28_s_003}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：わたしは熟睡するタイプだから、
    voice "ch28_l_003"
    l "I'm a deep sleeper! Not noticing is only natural!{#ch28_l_003}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：そこまでして俺を悪人にしたいのか。  [voice 8021]
    voice "ch28_s_004"
    s "You're that determined to make me the villain?{#ch28_s_004}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：悪人ですって？
    voice "ch28_l_004"
    l "Villain? Hah! You're a dog, aren't you?{#ch28_l_004}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：くっ……。
    voice "ch28_s_005"
    s "…Even as I tell the truth, Louise keeps calling me a dog…{#ch28_s_005}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：ねえ、ダーリン。
    voice "ch28_k_003"
    k "Say, darling. You're really not meeting Tabitha at night?{#ch28_k_003}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：してないって！
    voice "ch28_s_006"
    s "I'm not! Absolutely not!!{#ch28_s_006}"

    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：んー……。
    voice "ch28_k_004"
    k "Hmm… My intuition was wrong, after all.{#ch28_k_004}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：おいおい、キュルケ。
    voice "ch28_s_007"
    s "Hey—what was that just now?{#ch28_s_007}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：やっぱり、違ったのね、って。  [voice 2655]
    voice "ch28_k_005"
    k "I said my intuition was wrong.{#ch28_k_005}"

    # サイト：そこじゃない。
    voice "ch28_s_008"
    s "Not that part. The part after.{#ch28_s_008}"

    # キュルケ：ああ、あたしの勘ってところ？  [voice 2656]
    voice "ch28_k_006"
    k "Oh—that my intuition? {#ch28_k_006}"

    # サイト：そうそれ。
    voice "ch28_s_009"
    s "That's it. You blamed me on intuition alone?{#ch28_s_009}"

    # キュルケ：結果的には。  [voice 2657]
    voice "ch28_k_007"
    k "Well… In the end, yes.{#ch28_k_007}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：で、どうしてサイトとタバサが夜な夜な
    voice "ch28_l_005"
    l "So why did this story about Saito and Tabitha dating at night start?{#ch28_l_005}"

    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：実はね……。
    voice "ch28_k_008"
    k "Actually… There's a rumor that Tabitha's been up to something at night lately.{#ch28_k_008}"

    # キュルケ：で、タバサに関する噂なら、たぶんダーリンが
    voice "ch28_k_009"
    k "And I figured—any rumor about Tabitha probably involves darling, right?{#ch28_k_009}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：あのさ……。  [voice 8027]
    voice "ch28_s_010"
    s "Look here…{#ch28_s_010}"

    # サイト：そんなにタバサが何やってんのか
    voice "ch28_s_011"
    s "If you want to know what Tabitha's doing so badly, why not just ask her directly?{#ch28_s_011}"

    # キュルケ：それがそうもいかないのよ。
    voice "ch28_k_010"
    k "That's the thing—I tried asking casually, but she wouldn't tell me…{#ch28_k_010}"

    # サイト：分かった分かった。
    voice "ch28_s_012"
    s "All right, all right. I'll go ask her now, then.{#ch28_s_012}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+16, level=200]
    $ fade_fx("id(16)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # サイト：まったくもう……。
    voice "ch28_s_013"
    s "Honestly… I wonder what everyone's so worried about.{#ch28_s_013}"

    # [SE       se0      play=+82]
    # サイト：えーっと、サイトだけど……。  [voice 8031]
    voice "ch28_s_014"
    s "Um—this is Saito…{#ch28_s_014}"

    # タバサ：どうぞ。  [voice 15186]
    voice "ch28_t_001"
    t "Come in.{#ch28_t_001}"

    # [SE       se0      play=+57]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+96, level=200]
    $ fade_fx("id(96)")
    # [TRANS trans("crossfade", 1000)]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SE       se0      play=+56]
    # タバサ：……なに？  [voice 15187]
    voice "ch28_t_002"
    t "…What is it?{#ch28_t_002}"

    # サイト：いや、実はさ……。
    voice "ch28_s_015"
    s "Well, actually—have you been keeping anything from everyone lately?{#ch28_s_015}"

    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch28_t_003}"

    # サイト：（あっ、黙ってるけど、
    s "(Ah—she's silent, but I can tell she's hiding something…){#ch28_s_016}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：じゃあさ、俺にだけ話してくれない？
    voice "ch28_s_017"
    s "Then—will you tell just me? What you do at night, Tabitha?{#ch28_s_017}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch28_t_004}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ダメかな？  [voice 8034]
    voice "ch28_s_018"
    s "No good?{#ch28_s_018}"

    # タバサ：ダメ。  [voice 15188]
    voice "ch28_t_005"
    t "No.{#ch28_t_005}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：えーっ、なんでー？  [voice 8035]
    voice "ch28_s_019"
    s "Ehh—why not?{#ch28_s_019}"

    # タバサ：ダメったら、ダメ。  [voice 15189]
    voice "ch28_t_006"
    t "No means no.{#ch28_t_006}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：わ、分かったよ……。
    voice "ch28_s_020"
    s "O-Okay… At least a hint, then…{#ch28_s_020}"

    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：教えない。  [voice 15190]
    voice "ch28_t_007"
    t "I won't tell.{#ch28_t_007}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：……。
    voice "ch28_s_021"
    s "…Say, Tabitha…{#ch28_s_021}"

    menu:
        "You don't want to tell me?{#ch28_1_c_999_1}":
            jump ch28_1_scene_1000
        "Something you can't tell anyone?{#ch28_1_c_999_2}":
            jump ch28_1_scene_1001
        "Do you hate me?{#ch28_1_c_999_3}":
            jump ch28_1_scene_1002

label ch28_1_scene_1000:

    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+96, level=200]
    $ fade_fx("id(96)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そんなに俺には教えたくないの？  [voice 8038]
    voice "ch28_s_022"
    s "You don't want to tell me that badly?{#ch28_s_022}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：うん、あなただけには絶対。  [voice 15191]
    voice "ch28_t_008"
    t "Mm. To you especially.{#ch28_t_008}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：あなただけにはって……。
    voice "ch28_s_023"
    s "'To me especially'… And 'absolutely', too…{#ch28_s_023}"

    # → next scene 1003
    jump ch28_1_scene_1003

label ch28_1_scene_1001:

    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+96, level=200]
    $ fade_fx("id(96)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：人に言えないことやってるの？  [voice 8040]
    voice "ch28_s_024"
    s "Are you doing something you can't tell anyone?{#ch28_s_024}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：そんなことはない。  [voice 15192]
    voice "ch28_t_009"
    t "No, I'm not.{#ch28_t_009}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：じゃあ……。  [voice 8041]
    voice "ch28_s_025"
    s "Then…{#ch28_s_025}"

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：でも、今は言えない。  [voice 15193]
    voice "ch28_t_010"
    t "But I can't tell you now.{#ch28_t_010}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：えっ、どういうこと？  [voice 8042]
    voice "ch28_s_026"
    s "Eh? What do you mean?{#ch28_s_026}"

    # → next scene 1003
    jump ch28_1_scene_1003

label ch28_1_scene_1002:

    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+96, level=200]
    $ fade_fx("id(96)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ひょっとして、俺のこと嫌い？  [voice 8043]
    voice "ch28_s_027"
    s "Could it be—you hate me?{#ch28_s_027}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch28_t_011}"

    # サイト：（答えてくれない……。
    s "(She won't answer… And she looks so troubled…){#ch28_s_028}"

    # サイト：えーっと、変なこと聞いてごめん。  [voice 8044]
    voice "ch28_s_029"
    s "Um—sorry for asking something strange.{#ch28_s_029}"

    # タバサ：……。
    t "…{#ch28_t_012}"

    # サイト：（まだ困ってるし……）
    s "(Still troubled…){#ch28_s_030}"

    # → next scene 1003
    jump ch28_1_scene_1003

label ch28_1_scene_1003:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+96, level=200]
    $ fade_fx("id(96)")
    # サイト：……。  [voice 8045]
    voice "ch28_s_031"
    s "…{#ch28_s_031}"

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch28_t_013}"

    # サイト：あの……。
    voice "ch28_s_032"
    s "Um… I'm going home now.{#ch28_s_032}"

    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：あっ……。  [voice 15194]
    voice "ch28_t_014"
    t "Ah…{#ch28_t_014}"

    # サイト：なに？  [voice 8047]
    voice "ch28_s_033"
    s "What was that?{#ch28_s_033}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch28_t_015}"

    # サイト：……じゃあ。  [voice 8048]
    voice "ch28_s_034"
    s "Well then—{#ch28_s_034}"

    # [SE       se0      play=+57]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SE       se0      play=+56]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+12, level=200]
    $ fade_fx("id(12)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # [SE       se0      play=+57]
    # [SE       se0      play=+56]
    # キュルケ：どうだった、ダーリン？  [voice 2661]
    voice "ch28_k_011"
    k "How did it go, darling?{#ch28_k_011}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：……。  [voice 8049]
    voice "ch28_s_035"
    s "…{#ch28_s_035}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：ちょっと、サイト！
    voice "ch28_l_006"
    l "Hey, Saito! Say something!{#ch28_l_006}"

    # サイト：……ごめん。
    voice "ch28_s_036"
    s "…Sorry. I couldn't do it.{#ch28_s_036}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ってことは……。
    voice "ch28_k_012"
    k "Meaning… She didn't tell you either, did she?{#ch28_k_012}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：それどころか……。
    voice "ch28_s_037"
    s "Far from it… Ugh… Can I just go to sleep now?{#ch28_s_037}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：なんか気の毒になってきたから、
    voice "ch28_l_007"
    l "You're starting to feel sorry for him, so you can go ahead and sleep first.{#ch28_l_007}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：それじゃ、お先に……。  [voice 8052]
    voice "ch28_s_038"
    s "Then, excuse me…{#ch28_s_038}"

    # [SPRITE   lay5     hide]
    # [SE       se0      play=+59]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：こら、サイト！
    voice "ch28_l_008"
    l "Hey! Saito! Why are you trying to sleep on straw on the floor! Get into bed properly…{#ch28_l_008}"

    # サイト：いいんですよ、ボクなんて……。
    voice "ch28_s_039"
    s "It's fine for me… Sleeping on the floor suits a bad dog like me…{#ch28_s_039}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：あらあら、ダーリンったら、
    voice "ch28_k_013"
    k "Oh my—darling's become completely self-deprecating.{#ch28_k_013}"

    # サイト：ぐすっ、ぐすん……。
    voice "ch28_s_040"
    s "Sniff… Sniffle… Hiccup… S-snore…{#ch28_s_040}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……もう、寝ちゃった。  [voice 4574]
    voice "ch28_l_009"
    l "…He's already asleep.{#ch28_l_009}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：タバサってば……。
    voice "ch28_k_014"
    k "Tabitha really drove darling into a corner, didn't she…{#ch28_k_014}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+16, level=200]
    $ fade_fx("id(16)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：うう、早く寝ちゃったら、
    voice "ch28_s_041"
    s "Ugh—I fell asleep too fast and woke up before it was even morning.{#ch28_s_041}"

    # サイト：あれ？
    voice "ch28_s_042"
    s "Huh? The kitchen light's still on. It's not time for prep yet…{#ch28_s_042}"

    # [SE       se0      play=+82]
    # タバサ：あっ。  [voice 15195]
    voice "ch28_t_016"
    t "Ah.{#ch28_t_016}"

    # サイト：この声は……タバサ？  [voice 8057]
    voice "ch28_s_043"
    s "That voice—Tabitha?{#ch28_s_043}"

    # [SE       se0      play=+55]
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+287, level=80]
    $ dissolve_fx("id(287)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # タバサ：……。
    t "…{#ch28_t_017}"

    # サイト：どうしたの？  [voice 8058]
    voice "ch28_s_044"
    s "What's wrong?{#ch28_s_044}"

    # タバサ：ケーキ作ってた。
    voice "ch28_t_018"
    t "I was making a cake. For you.{#ch28_t_018}"

    # サイト：えっ、ケーキ？  [voice 8059]
    voice "ch28_s_045"
    s "Eh? A cake?{#ch28_s_045}"

    # タバサ：うん。  [voice 15197]
    voice "ch28_t_019"
    t "Mm.{#ch28_t_019}"

    # サイト：……タバサが作ってるの？  [voice 8060]
    voice "ch28_s_046"
    s "…Tabitha made it?{#ch28_s_046}"

    # タバサ：手作り。  [voice 15198]
    voice "ch28_t_020"
    t "Homemade.{#ch28_t_020}"

    # サイト：タバサって……。
    voice "ch28_s_047"
    s "Tabitha—you had a hobby of cake-making?{#ch28_s_047}"

    # タバサ：ううん、なかった。
    voice "ch28_t_021"
    t "No, I didn't. But…{#ch28_t_021}"

    # サイト：なかったってことは、ひょっとして……。  [voice 8062]
    voice "ch28_s_048"
    s "'Didn't'—meaning, perhaps…{#ch28_s_048}"

    menu:
        "A baking hobby?{#ch28_1_c_1003_1}":
            jump ch28_1_scene_1004
        "You made it for me?{#ch28_1_c_1003_2}":
            jump ch28_1_scene_1005
        "A human experiment?{#ch28_1_c_1003_3}":
            jump ch28_1_scene_1006

label ch28_1_scene_1004:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+16, level=200]
    $ fade_fx("id(16)")
    # [EVENT_CG event    image=+287, level=80]
    $ dissolve_fx("id(287)")
    # サイト：ケーキ作りを趣味にしたんだ？  [voice 8063]
    voice "ch28_s_049"
    s "Did you take up cake-making as a hobby?{#ch28_s_049}"

    # タバサ：……うん。  [voice 15200]
    voice "ch28_t_022"
    t "…Mm.{#ch28_t_022}"

    # サイト：でも、なんでまた急に？  [voice 8064]
    voice "ch28_s_050"
    s "But why suddenly?{#ch28_s_050}"

    # タバサ：……。
    t "…{#ch28_t_023}"

    # サイト：やっぱり、俺には教えてくれないの？  [voice 8065]
    voice "ch28_s_051"
    s "You still won't tell me, will you?{#ch28_s_051}"

    # [EVENT_CG event    image=+288, level=80]
    $ dissolve_fx("id(288)")
    # タバサ：……。
    voice "ch28_t_024"
    t "…Because I wanted you to eat it.{#ch28_t_024}"

    # サイト：えっ、本当に？  [voice 8066]
    voice "ch28_s_052"
    s "Eh? Really?{#ch28_s_052}"

    # タバサ：うん、本当。
    voice "ch28_t_025"
    t "Mm, really. But it's full of failures.{#ch28_t_025}"

    # → next scene 1007
    jump ch28_1_scene_1007

label ch28_1_scene_1005:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+16, level=200]
    $ fade_fx("id(16)")
    # [EVENT_CG event    image=+287, level=80]
    $ dissolve_fx("id(287)")
    # サイト：俺のために作ってくれてたんだ？  [voice 8067]
    voice "ch28_s_053"
    s "You made it for me?{#ch28_s_053}"

    # [EVENT_CG event    image=+288, level=80]
    $ dissolve_fx("id(288)")
    # タバサ：……うん。  [voice 15203]
    voice "ch28_t_026"
    t "…Mm.{#ch28_t_026}"

    # サイト：……えっ、本当に？  [voice 8068]
    voice "ch28_s_054"
    s "…Eh? Really?{#ch28_s_054}"

    # タバサ：本当。
    voice "ch28_t_027"
    t "Really. But it's full of failures.{#ch28_t_027}"

    # → next scene 1007
    jump ch28_1_scene_1007

label ch28_1_scene_1006:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+16, level=200]
    $ fade_fx("id(16)")
    # [EVENT_CG event    image=+287, level=80]
    $ dissolve_fx("id(287)")
    # サイト：人体実験の一環なんだ？  [voice 8069]
    voice "ch28_s_055"
    s "Is it part of a human experiment?{#ch28_s_055}"

    # タバサ：ちがう。  [voice 15205]
    voice "ch28_t_028"
    t "No.{#ch28_t_028}"

    # サイト：じゃあ、ドッキリ？  [voice 8070]
    voice "ch28_s_056"
    s "Then—a surprise prank?{#ch28_s_056}"

    # タバサ：ドッキリって？  [voice 15206]
    voice "ch28_t_029"
    t "A what?{#ch28_t_029}"

    # サイト：はは、伝わらないよね？
    voice "ch28_s_057"
    s "Ha ha, you don't get it, do you? It means tricking and scaring someone.{#ch28_s_057}"

    # [EVENT_CG event    image=+288, level=80]
    $ dissolve_fx("id(288)")
    # タバサ：じゃあ、そうかも。  [voice 15207]
    voice "ch28_t_030"
    t "Then… maybe.{#ch28_t_030}"

    # サイト：えっ、ドッキリなの？  [voice 8072]
    voice "ch28_s_058"
    s "Eh—it's a prank?{#ch28_s_058}"

    # タバサ：うん。
    voice "ch28_t_031"
    t "Mm. I wanted to surprise you.{#ch28_t_031}"

    # サイト：……。  [voice 8073]
    voice "ch28_s_059"
    s "…{#ch28_s_059}"

    # → next scene 1007
    jump ch28_1_scene_1007

label ch28_1_scene_1007:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # [BG       stage    image=+16, level=200]
    $ fade_fx("id(16)")
    # [EVENT_CG event    image=+288, level=80]
    $ dissolve_fx("id(288)")
    # [EVENT_CG event    image=+287, level=80]
    $ dissolve_fx("id(287)")
    # サイト：これ、作りかけ？  [voice 8074]
    voice "ch28_s_060"
    s "Is this still being made?{#ch28_s_060}"

    # タバサ：失敗作。
    voice "ch28_t_032"
    t "A failure. It isn't perfect yet.{#ch28_t_032}"

    # サイト：食べてもいいかな？  [voice 8075]
    voice "ch28_s_061"
    s "May I eat it?{#ch28_s_061}"

    # タバサ：……。
    t "…{#ch28_t_033}"

    # サイト：じゃ、食べるな。
    voice "ch28_s_062"
    s "Then I'll eat it. Here—open up.{#ch28_s_062}"

    # [EVENT_CG event    image=+288, level=80]
    $ dissolve_fx("id(288)")
    # タバサ：美味しい？  [voice 15210]
    voice "ch28_t_034"
    t "Is it good?{#ch28_t_034}"

    # サイト：うん、すごく美味しいよっ！
    voice "ch28_s_063"
    s "Mm, it's really good! You really only just learned to make cakes?{#ch28_s_063}"

    # タバサ：うん。  [voice 15211]
    voice "ch28_t_035"
    t "Mm.{#ch28_t_035}"

    # サイト：信じられないなぁ。  [voice 8078]
    voice "ch28_s_064"
    s "I can't believe it.{#ch28_s_064}"

    # タバサ：それはきっと……。
    voice "ch28_t_036"
    t "It must be… because the teacher was good.{#ch28_t_036}"

    # サイト：先生？  [voice 8079]
    voice "ch28_s_065"
    s "Teacher?{#ch28_s_065}"

    # タバサ：シエスタ。  [voice 15213]
    voice "ch28_t_037"
    t "Siesta.{#ch28_t_037}"

    # サイト：そうだったんだ……。
    voice "ch28_s_066"
    s "I see… But why didn't you tell me when I asked?{#ch28_s_066}"

    # タバサ：だって……。  [voice 15214]
    voice "ch28_t_038"
    t "Because…{#ch28_t_038}"

    # サイト：だって？  [voice 8081]
    voice "ch28_s_067"
    s "Because why?{#ch28_s_067}"

    # [EVENT_CG event    image=+289, level=80]
    $ dissolve_fx("id(289)")
    # タバサ：だって、あなたの喜ぶ顔が見たかったから。  [voice 15215]
    voice "ch28_t_039"
    t "Because I wanted to see your face light up.{#ch28_t_039}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：（タバサが作ったこのケーキ……。
    s "(This cake Tabitha made… Word of its taste will spread from the academy kitchen to the town…){#ch28_s_068}"

    # サイト：（国中に一大ケーキブームを
    s "(…and spark a cake craze across the country. But that's another story.){#ch28_s_069}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ЧАСТИ 1 ====
    jump ch28_2
    return

