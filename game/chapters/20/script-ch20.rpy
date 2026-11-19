# Глава 20 (источник chapter_21): наказание, уход Харуны, повседневность.
# Источник: ps2_source/chapters/chapter_21_小悪魔のおしおき.txt (SCENE 769-770).

label ch20:
    $ tndl(None)
    $ show_sprites()

label ch20_scene_769:

    # [TITLE title("小悪魔のおしおき")]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 500)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1136, level=200]
    $ fade_fx("id(1136)")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+1145, level=200]
    $ fade_fx("overlay")
    # [TRANS trans("crossfade", 1000)]
    # [BG       stage    image=+2, level=200]
    $ fade_fx("white")
    # [TRANS trans("crossfade", 2000)]
    # [BG       stage    image=+80, level=200]
    $ fade_fx("id(80)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+7]
    play music t6 fadein 1.0
    # [SPRITE   lay2     image=+535, level=160, dir=2B]
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：いやぁ、完璧！
    voice "ch20_s_001"
    s "Ah, perfect! Good, great, perfect, Siesta!{#ch20_s_001}"

    # シエスタ：そ、そうですか……。
    voice "ch20_si_001"
    si "I-Is that so… But this is a strange outfit, isn't it?{#ch20_si_001}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：何を言うかっ！
    voice "ch20_s_002"
    s "Don't say that! This was the most popular uniform in the world I came from!{#ch20_s_002}"

    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # サイト：その名も『ブレザー』！！  [voice 7955]
    voice "ch20_s_003"
    s "And its name is 'Blazer'!!{#ch20_s_003}"

    # [SPRITE   lay2     image=+539, level=160, dir=2B]
    # シエスタ：ぶ、ぶれぃざぁ、ですか……。
    voice "ch20_si_002"
    si "B-Blazer, is it… A-Ah ha ha…{#ch20_si_002}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：いやぁ、この短いチェックのスカートに
    voice "ch20_s_004"
    s "Man, this short checkered skirt, the neat navy jacket, and on top of that, these navy socks!!{#ch20_s_004}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：はぁぁ、その姿を見てると元の世界に
    voice "ch20_s_005"
    s "Haaah, looking at you like this makes me think of back home…{#ch20_s_005}"

    # シエスタ：はぁ……。  [voice 14147]
    voice "ch20_si_003"
    si "Haa…{#ch20_si_003}"

    # サイト：でもシエスタ、その格好よく似合ってるよ。  [voice 7958]
    voice "ch20_s_006"
    s "But Siesta, it really suits you.{#ch20_s_006}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：いつものメイド服と似ていながらも、
    voice "ch20_s_007"
    s "It's similar to your usual maid uniform, but the shorter skirt really emphasizes how cute you are.{#ch20_s_007}"

    # [SPRITE   lay2     image=+541, level=160, dir=2B]
    # シエスタ：ほ、ほんとですかっ？
    voice "ch20_si_004"
    si "R-Really? Saito-san… I'm happy. Ehehe.{#ch20_si_004}"

    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # サイト：（うわ、ブレザー姿で頬を赤らめてるって……。
    s "(Whoa, blushing in a blazer… That's way too moe.){#ch20_s_008}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+307, level=140, dir=1A]
    # ルイズ：サ～イ～ト～！  [voice 4516]
    voice "ch20_l_001"
    l "SAAIITOOO!{#ch20_l_001}"

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # サイト：はぅあー、ご主人様！  [voice 7960]
    voice "ch20_s_009"
    s "Eep! Mistress!{#ch20_s_009}"

    # ルイズ：わたしがちょおっと目を離したスキに、
    voice "ch20_l_002"
    l "While I looked away for just a moment, you dress the maid up in strange clothes and grin like an idiot. You've got some nerve, Saito.{#ch20_l_002}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+533, level=160, dir=2B]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # シエスタ：サ、サイトさん！
    voice "ch20_si_005"
    si "S-Saito-san! I have some work to do, so excuse me!{#ch20_si_005}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：あぁっ、シエスタ！
    voice "ch20_s_010"
    s "Ah, Siesta! Where are you going in that blazer!{#ch20_s_010}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+213, level=80]
    $ dissolve_fx("id(213)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：逃がさないわよサイト！  [voice 4518]
    voice "ch20_l_003"
    l "I won't let you escape, Saito!{#ch20_l_003}"

    # サイト：ゆ、許してください……。  [voice 7962]
    voice "ch20_s_011"
    s "F-Forgive me…{#ch20_s_011}"

    # ルイズ：許さないっ！  [voice 4519]
    voice "ch20_l_004"
    l "I won't!{#ch20_l_004}"

    # サイト：そ、そんな……。  [voice 7963]
    voice "ch20_s_012"
    s "N-No way…{#ch20_s_012}"

    # ルイズ：まったくあんたって使い魔は、
    voice "ch20_l_005"
    l "You really are a familiar who ogles maids and Zerbst's daughter and so on…{#ch20_l_005}"

    # ルイズ：犬だって３日飼えばご主人様への忠誠を身に
    voice "ch20_l_006"
    l "Even a dog, if you keep it three days, learns loyalty to its master. You're not even a dog.{#ch20_l_006}"

    # ルイズ：どうやら、今回は徹底的にしつけを
    voice "ch20_l_007"
    l "Looks like I'll have to train you thoroughly this time.{#ch20_l_007}"

    # サイト：ひ、ひぃっ！？
    voice "ch20_s_013"
    s "E-Eep! Mistress is scary! Your beautiful face is ruined!{#ch20_s_013}"

    # ルイズ：おだまり！
    voice "ch20_l_008"
    l "Silence! It's all Saito's fault to begin with.{#ch20_l_008}"

    # ルイズ：こうなったら徹底的にお仕置きしてやるわ！
    voice "ch20_l_009"
    l "If that's how it is, I'll punish you thoroughly! I'll make you remember your place.{#ch20_l_009}"

    # サイト：ひ、ひぃえぇぇぇぇ。  [voice 7965]
    voice "ch20_s_014"
    s "H-Hiiiii!{#ch20_s_014}"

    # ルイズ：そ、そうね。
    voice "ch20_l_010"
    l "W-Well. How about you wash mistress's back in the bath?{#ch20_l_010}"

    # サイト：へっ？  [voice 7966]
    voice "ch20_s_015"
    s "Heh?{#ch20_s_015}"

    # ルイズ：ど、どう？
    voice "ch20_l_011"
    l "H-How about it? It's humiliating, isn't it? It's punishment, isn't it?{#ch20_l_011}"

    # サイト：い、いや、少しうれしいかも。  [voice 7967]
    voice "ch20_s_016"
    s "U-Um, maybe I'd actually like it a little.{#ch20_s_016}"

    # ルイズ：な、な、なんですって！
    voice "ch20_l_012"
    l "W-What was that! Treat it as punishment! Be afraid!{#ch20_l_012}"

    # サイト：は、はい、お仕置きです。
    voice "ch20_s_017"
    s "Y-Yes, it's punishment. I'm trembling, trembling, trembling.{#ch20_s_017}"

    # ルイズ：わ、分かったのなら、一緒にお風呂に行くわよ。
    voice "ch20_l_013"
    l "W-Well, if you understand, let's go to the bath together. I'll get ready, so wait there.{#ch20_l_013}"

    # サイト：は、はい。  [voice 7969]
    voice "ch20_s_018"
    s "Y-Yes.{#ch20_s_018}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+12, level=200]
    $ fade_fx("id(12)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（しかし……。
    s "(But… In the bath with Louise… And washing Louise's back…){#ch20_s_019}"

    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # サイト：（………）
    s "(…){#ch20_s_020}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（いやいや、これはお仕置き、
    s "(No, no, this is punishment, punishment…){#ch20_s_021}"

    # サイト：（お仕置き、お仕置き、お仕置き）
    s "(Punishment, punishment, punishment.){#ch20_s_022}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：ほら、何ブツブツ言っているの？
    voice "ch20_l_014"
    l "Hey, what are you muttering about? Hurry up, I'll punish you. {#ch20_l_014}"

    # サイト：はーい。  [voice 7970]
    voice "ch20_s_023"
    s "Yeees.{#ch20_s_023}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [EVENT_CG event    image=+281, level=80]
    $ dissolve_fx("id(281)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # サイト：えーと、ご主人様。
    voice "ch20_s_024"
    s "Um, mistress. What is that swimsuit?{#ch20_s_024}"

    # サイト：しかも、どう見てもスクール水着にしか
    voice "ch20_s_025"
    s "And no matter how I look at it, it looks like a school swimsuit…{#ch20_s_025}"

    # ルイズ：この水着は、ハルナからセンベツで
    voice "ch20_l_015"
    l "This swimsuit is a parting gift from Haruna.{#ch20_l_015}"

    # サイト：センベツ！？  [voice 7973]
    voice "ch20_s_026"
    s "A parting gift!?{#ch20_s_026}"

    # ルイズ：サイトが言うことを聞かなかったら、
    voice "ch20_l_016"
    l "She said to use it if you didn't listen to me.{#ch20_l_016}"

    # サイト：春奈……。
    voice "ch20_s_027"
    s "Haruna… What did you think of me? I mean, I'm really happy, but…{#ch20_s_027}"

    # サイト：でも、お風呂に水着で入るのは
    voice "ch20_s_028"
    s "But I think going into the bath in a swimsuit is a mistake.{#ch20_s_028}"

    # [EVENT_CG event    image=+280, level=80]
    $ dissolve_fx("id(280)")
    # ルイズ：な、何言ってるの？
    voice "ch20_l_017"
    l "What are you talking about? I can't get in the bath with you without a swimsuit, can I?{#ch20_l_017}"

    # サイト：まぁ、そうですよね。  [voice 7976]
    voice "ch20_s_029"
    s "Well, yes, I suppose.{#ch20_s_029}"

    # [EVENT_CG event    image=+281, level=80]
    $ dissolve_fx("id(281)")
    # ルイズ：ほら。  [voice 4533]
    voice "ch20_l_018"
    l "Here.{#ch20_l_018}"

    # サイト：え？
    voice "ch20_s_030"
    s "Eh? Here, with this towel, what are you going to…{#ch20_s_030}"

    # [EVENT_CG event    image=+280, level=80]
    $ dissolve_fx("id(280)")
    # ルイズ：あぁもうじれったいわね！  [voice 4534]
    voice "ch20_l_019"
    l "Oh, how slow you are!{#ch20_l_019}"

    # ルイズ：それでわたしの背中を流しなさいって
    voice "ch20_l_020"
    l "I'm telling you to wash my back. Ah, but before that…{#ch20_l_020}"

    # ルイズ：もう一枚タオルがあるでしょ？
    voice "ch20_l_021"
    l "There's another towel, right? Don't forget to blindfold yourself tightly with it.{#ch20_l_021}"

    # ルイズ：背中を洗うとき、少し背中を見せるけど、
    voice "ch20_l_022"
    l "When I wash my back, I'll show a little of it. If you even loosen the blindfold a bit… I'll kill you.{#ch20_l_022}"

    # サイト：わ、分かったよ……。  [voice 7978]
    voice "ch20_s_031"
    s "O-Okay…{#ch20_s_031}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # サイト：ほらよ、これでいいだろ？  [voice 7979]
    voice "ch20_s_032"
    s "Here, this should do, right?{#ch20_s_032}"

    # ルイズ：ん、どれどれ……。
    voice "ch20_l_023"
    l "Mm, let's see… Hmm, seems you followed my order properly.{#ch20_l_023}"

    # ルイズ：よっと。
    voice "ch20_l_024"
    l "All right. Ready. Hurry up and wash my back!{#ch20_l_024}"

    # サイト：ふぇーい……。  [voice 7980]
    voice "ch20_s_033"
    s "Yehehe…{#ch20_s_033}"

    # サイト：（あぁ、前にもさわったことがあるけど、
    s "(Ah, I've touched it before, but Louise's back is so smooth…){#ch20_s_034}"

    # サイト：（これで目隠しさえされてなけりゃ……。
    s "(If only I weren't blindfolded… No, what am I thinking, me…){#ch20_s_035}"

    # サイト：どうっすかご主人様、お背中の方は気持ち
    voice "ch20_s_036"
    s "How's it going, mistress? Does your back feel good?{#ch20_s_036}"

    # ルイズ：そうねぇ、もうちょっと強くしてもいいわよ。  [voice 4540]
    voice "ch20_l_025"
    l "Yeah, a little harder is fine.{#ch20_l_025}"

    # サイト：ういー……。  [voice 7982]
    voice "ch20_s_037"
    s "Ouii…{#ch20_s_037}"

    # ルイズ：あー、そこそこ……。
    voice "ch20_l_026"
    l "Ah, there, there… Mm, right there. More, focus on that spot.{#ch20_l_026}"

    # サイト：うーい。  [voice 7983]
    voice "ch20_s_038"
    s "Oooi.{#ch20_s_038}"

    # ルイズ：ふんふんふーん。
    voice "ch20_l_027"
    l "Hmm hmm hmm. Hey, Saito. What's going through your mind right now?{#ch20_l_027}"

    # サイト：へ？
    voice "ch20_s_039"
    s "Eh? I'm thinking about nothing in particular… Just a little lightheaded.{#ch20_s_039}"

    # サイト：（やばい、蒸気がこもりすぎて、
    s "(Bad. The steam is building up, the temperature is rising. It's like a sauna.){#ch20_s_040}"

    # ルイズ：ふふん、負け惜しみは言わなくていいわよ。
    voice "ch20_l_028"
    l "Hmph, no need for sore-loser talk. Alone with me in the bath, washing my back and all…{#ch20_l_028}"

    # ルイズ：なんにも見えないってのはつらいでしょ？
    voice "ch20_l_029"
    l "Not being able to see a thing is painful, isn't it? Frustrating, isn't it? Honestly, it's torture.{#ch20_l_029}"

    # ルイズ：まぁ、それこそが今回のお仕置きの
    voice "ch20_l_030"
    l "Well, that's the real purpose of this punishment, though.{#ch20_l_030}"

    # ルイズ：これに懲りたらもう、わたしをないがしろに
    voice "ch20_l_031"
    l "If you've learned your lesson, don't you neglect me again, okay? {#ch20_l_031}"

    # サイト：（目の前がくらくらしてくる。
    s "(My head is spinning. Why is Louise fine with this?){#ch20_s_041}"

    # ルイズ：ちょっとサイト、わたしの話聞いてるの？
    voice "ch20_l_032"
    l "Hey, Saito, are you listening to me? Your hands have been stopped for a while now!{#ch20_l_032}"

    # サイト：あ……ご、ごめん。  [voice 7985]
    voice "ch20_s_042"
    s "A… S-Sorry.{#ch20_s_042}"

    # ルイズ：まったく、ちょっとほめたらすぐいい気に
    voice "ch20_l_033"
    l "Honestly, praise you a little and you get cocky right away. That's Saito for you.{#ch20_l_033}"

    # null：………。
    th "……… …. ..{#ch20_th_001}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：あー、気持ちいい。
    voice "ch20_l_034"
    l "Aah, that feels good. Saito, you're good at washing bodies.{#ch20_l_034}"

    # ルイズ：んー、それにしても……。
    voice "ch20_l_035"
    l "Mm, even so… Haa… It doesn't get big, does it.{#ch20_l_035}"

    # サイト：な、何がですか！  [voice 7986]
    voice "ch20_s_043"
    s "W-What is?{#ch20_s_043}"

    # ルイズ：な、なんだっていいでしょ。
    voice "ch20_l_036"
    l "A-Any… No, anything's fine. Your hands stopped!{#ch20_l_036}"

    # サイト：は、はい！  [voice 7987]
    voice "ch20_s_044"
    s "Y-Yes!{#ch20_s_044}"

    # ルイズ：ちょっとサイト、あんたさっきから様子が
    voice "ch20_l_037"
    l "Hey, Saito, you've been acting strange for a while now. Did you get heatstroke or something?{#ch20_l_037}"

    # サイト：い、いや……そんなことはないです……。  [voice 7988]
    voice "ch20_s_045"
    s "N-No… Nothing like that…{#ch20_s_045}"

    # ルイズ：もうちょっといろんなところが大きくなれば
    voice "ch20_l_038"
    l "If only more parts of you would get bigger… Saito, your hands stopped again?{#ch20_l_038}"

    # サイト：（もう限界です。
    s "(I'm at my limit. Mommy. I tried my best.){#ch20_s_046}"

    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay2     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay2     hide, reset]
    # [SPRITE   lay5     hide, reset]
    # サイト：ばた……。  [voice 7989]
    voice "ch20_s_047"
    s "Bata…{#ch20_s_047}"

    # ルイズ：きゃ、きゃあぁっ！
    voice "ch20_l_039"
    l "Kyaa! Saito? What happened to you, you collapsed!{#ch20_l_039}"

    # ルイズ：ちょ……サイト！
    voice "ch20_l_040"
    l "Hey… Saito! Are you okay?{#ch20_l_040}"

    # ルイズ：目を開けなさいって！
    voice "ch20_l_041"
    l "Open your eyes! Saito, Saito, Saitooooooo!!!!{#ch20_l_041}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
label ch20_scene_770:

    # [MOVIE movie(1)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：えっ、自立するってどういうことだよ？  [voice 9189]
    voice "ch20_s_048"
    s "Eh? What do you mean, becoming independent?{#ch20_s_048}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # ハルナ：うん、いつまでもこの学院で……。
    voice "ch20_ha_001"
    ha "Yeah. I can't stay at this academy forever… I've been wondering whether it's right to keep relying on Louise and the others.{#ch20_ha_001}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そんなこといったら、俺なんかルイズに
    voice "ch20_s_049"
    s "If you say that, then I've been taken care of by this academy ever since Louise summoned me.{#ch20_s_049}"

    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：平賀くんはルイズさんの使い魔じゃない。
    voice "ch20_ha_002"
    ha "Hiraga-kun is Louise's familiar. Of course you're taken care of. But I'm not one, so…{#ch20_ha_002}"

    # サイト：そりゃそうなんだけどさ……。
    voice "ch20_s_050"
    s "I know, but… We're probably the only two Japanese people in this world.{#ch20_s_050}"

    # サイト：それに、お互いのことを知らない
    voice "ch20_s_051"
    s "And we're not exactly strangers to each other… So if we worked at the academy, maybe…{#ch20_s_051}"

    # [SPRITE   lay7     image=+959, level=160, dir=1A]
    # ハルナ：あのね、平賀くん……。
    voice "ch20_ha_003"
    ha "The thing is, Hiraga-kun… I've been scouted.{#ch20_ha_003}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：ス、スカウトって、なんの？  [voice 9193]
    voice "ch20_s_052"
    s "S-Scouted for what?{#ch20_s_052}"

    # ハルナ：劇団よ、劇団。  [voice 1772]
    voice "ch20_ha_004"
    ha "A theater troupe, a theater troupe.{#ch20_ha_004}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：劇団って、あのウェザリーの劇団のこと？  [voice 9194]
    voice "ch20_s_053"
    s "A theater troupe? You mean Weatherly's troupe?{#ch20_s_053}"

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：違うの。
    voice "ch20_ha_005"
    ha "No. Someone from another troupe who saw that play liked me and scouted me.{#ch20_ha_005}"

    # ハルナ：この際、いい機会だから、その劇団のお世話に
    voice "ch20_ha_006"
    ha "Now's a good chance, so I was thinking of going along with that troupe.{#ch20_ha_006}"

    # サイト：でもさ、劇団の世話になるってことは、
    voice "ch20_s_054"
    s "But if you join a troupe, you'll have to go on tours to other towns, won't you?{#ch20_s_054}"

    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：うん、そうだね。
    voice "ch20_ha_007"
    ha "Yeah. I probably won't get to see Hiraga-kun very often anymore.{#ch20_ha_007}"

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：でもね、私は楽しみにしてるんだ。
    voice "ch20_ha_008"
    ha "But I'm looking forward to it. I get to see all sorts of towns in this world.{#ch20_ha_008}"

    # ハルナ：ひょっとすると、日本へ戻るためのきっかけ
    voice "ch20_ha_009"
    ha "Maybe I'll even find a clue to get back to Japan.{#ch20_ha_009}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そっか、そうだよな。  [voice 9196]
    voice "ch20_s_055"
    s "I see. Yeah, that's right.{#ch20_s_055}"

    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：だから平賀くん……。
    voice "ch20_ha_010"
    ha "So, Hiraga-kun… If you don't mind, cheer me on, okay?{#ch20_ha_010}"

    # サイト：ああ、もちろんだとも！
    voice "ch20_s_056"
    s "Of course I will! And let's both do our best to find a way back to Japan!{#ch20_s_056}"

    # ハルナ：うん！  [voice 1779]
    voice "ch20_ha_011"
    ha "Mm!{#ch20_ha_011}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：（ウェザリーの協力もあり、
    s "(With Weatherly's help, Haruna was completely back to her old self.){#ch20_s_057}"

    # サイト：（アキナのことはほとんど覚えていないようだ。
    s "(She hardly remembers being Akina at all. I wonder if that's Weatherly's magic too…){#ch20_s_058}"

    # サイト：（ウェザリーは、レコン・キスタに与したことを
    s "(Weatherly was charged with siding with Reconquista, but…){#ch20_s_059}"

    # サイト：（レコン・キスタの情報提供を行うことと、
    s "(For providing information on Reconquista, and through the princess's consideration, she seems to have avoided punishment with just a few months of house arrest.){#ch20_s_060}"

    # サイト：（そんなわけで、学院から春奈が去ったあとは、
    s "(And so, after Haruna left the academy, life at the academy resumed pretty much as before… But…){#ch20_s_061}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # サイト：ところでさ、ルイズ。  [voice 9198]
    voice "ch20_s_062"
    s "By the way, Louise.{#ch20_s_062}"

    # ルイズ：なにかしら、サイト？  [voice 4819]
    voice "ch20_l_042"
    l "What is it, Saito?{#ch20_l_042}"

    # サイト：なんで、ご主人様は、鎖とか、縄とか
    voice "ch20_s_063"
    s "Why are you taking out chains and ropes, mistress?{#ch20_s_063}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：いい？
    voice "ch20_l_043"
    l "Listen. You are my familiar.{#ch20_l_043}"

    # サイト：はぁ……。  [voice 9200]
    voice "ch20_s_064"
    s "Haa…{#ch20_s_064}"

    # ルイズ：使い魔であるからには、
    voice "ch20_l_044"
    l "As a familiar, the orders of the mistress who summoned you are absolute. So far, so good?{#ch20_l_044}"

    # サイト：まぁ……。  [voice 9201]
    voice "ch20_s_065"
    s "Well…{#ch20_s_065}"

    # ルイズ：にもかかわらず、あんたときたら授業中に
    voice "ch20_l_045"
    l "And yet you wander away from me during class, and ogle every girl you see.{#ch20_l_045}"

    # ルイズ：挙げ句の果てにはシエスタやキュルケと、
    voice "ch20_l_046"
    l "And on top of that, you flirt with Siesta and Kirche behind my back! You have far too little awareness as a familiar!{#ch20_l_046}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：と、いうわけで。
    voice "ch20_l_047"
    l "So, I've decided to re-educate you thoroughly.{#ch20_l_047}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：げっ。  [voice 9202]
    voice "ch20_s_066"
    s "Gulp.{#ch20_s_066}"

    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：まずは、鎖ね。
    voice "ch20_l_048"
    l "First, the chains. And restraints. What else do I need…{#ch20_l_048}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：あと、言っておくけど、返事は『はい』か
    voice "ch20_l_049"
    l "And let me tell you, I only accept 'yes', 'understood', or 'roger' as a reply.{#ch20_l_049}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：あ、いや……。  [voice 9203]
    voice "ch20_s_067"
    s "A… No…{#ch20_s_067}"

    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay1     reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ぐは、いたー！  [voice 9204]
    voice "ch20_s_068"
    s "Guh, it hurts!{#ch20_s_068}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：返事は『はい』と『分かりました』と
    voice "ch20_l_050"
    l "I told you I only accept 'yes', 'understood', or 'roger'. The re-education has already begun!{#ch20_l_050}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：とほほ……。  [voice 9205]
    voice "ch20_s_069"
    s "Sigh…{#ch20_s_069}"

    # サイト：なぁ、ルイズ。  [voice 9206]
    voice "ch20_s_070"
    s "Say, Louise.{#ch20_s_070}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：なによ。  [voice 4828]
    voice "ch20_l_051"
    l "What is it?{#ch20_l_051}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # サイト：確かに、俺は使い魔としては、
    voice "ch20_s_071"
    s "I'm probably the worst familiar there is. I know that.{#ch20_s_071}"

    # ルイズ：あら、分かってるじゃない。  [voice 4829]
    voice "ch20_l_052"
    l "Oh? So you understand.{#ch20_l_052}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：けれども、男として、ルイズを絶対守って
    voice "ch20_s_072"
    s "But as a man, I've decided I'll absolutely protect Louise.{#ch20_s_072}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：……！  [voice 4830]
    voice "ch20_l_053"
    l "…!{#ch20_l_053}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：服も洗ってやる、部屋の掃除もしてやる。
    voice "ch20_s_073"
    s "I'll wash your clothes, clean your room. I don't mind moderate food either. But could you spare me the ropes and chains?{#ch20_s_073}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：……。  [voice 4831]
    voice "ch20_l_054"
    l "…{#ch20_l_054}"

    # ルイズ：サイト……。  [voice 4832]
    voice "ch20_l_055"
    l "Saito…{#ch20_l_055}"

    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # サイト：うん？  [voice 9210]
    voice "ch20_s_074"
    s "Hm?{#ch20_s_074}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：このバカ犬ー！  [voice 4833]
    voice "ch20_l_056"
    l "You stupid dog!{#ch20_l_056}"

    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay1     reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ぐふっ。  [voice 9211]
    voice "ch20_s_075"
    s "Guh!{#ch20_s_075}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+278, level=80]
    $ dissolve_fx("id(278)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：ほら、何ぐずぐずしてるの！
    voice "ch20_l_057"
    l "Come on, stop dawdling! Change your clothes—help me quickly!{#ch20_l_057}"

    # サイト：なんだよ、この前まで着替えなんか
    voice "ch20_s_076"
    s "What? You just said I didn't need to help you change…{#ch20_s_076}"

    # ルイズ：うっさいわねぇ！  [voice 4835]
    voice "ch20_l_058"
    l "Shut up!{#ch20_l_058}"

    # [EVENT_CG event    image=+279, level=80]
    $ dissolve_fx("id(279)")
    # ルイズ：あんたはわたしの使い魔なんだから、
    voice "ch20_l_059"
    l "You're my familiar, so you do as I say. I've decided it, so that's how it is!!{#ch20_l_059}"

    # ルイズ：そうよ、あんたはずーっと、
    voice "ch20_l_060"
    l "That's right. You're always my familiar.{#ch20_l_060}"

    # ルイズ：他の誰がなんて言おうが、わたしだけの……。  [voice 4838]
    voice "ch20_l_061"
    l "No matter what anyone else says, you're only mine…{#ch20_l_061}"

    # サイト：ん、なんか言ったルイズ？  [voice 9213]
    voice "ch20_s_077"
    s "Hm? Did you say something, Louise?{#ch20_s_077}"

    # [EVENT_CG event    image=+278, level=80]
    $ dissolve_fx("id(278)")
    # ルイズ：なにも言ってない！
    voice "ch20_l_062"
    l "I said nothing! Now that you've changed, let's go to class at once. Follow me!{#ch20_l_062}"

    # サイト：へいへい、お嬢様。  [voice 9214]
    voice "ch20_s_078"
    s "Yes, yes, milady.{#ch20_s_078}"

    # ルイズ：ご主人様には『はい』でしょうがっ！  [voice 4840]
    voice "ch20_l_063"
    l "It's 'yes' when addressing your mistress!{#ch20_l_063}"

    # サイト：はーい。  [voice 9215]
    voice "ch20_s_079"
    s "Yeees.{#ch20_s_079}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [EVENT_CG event    hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # サイト：（……こんな感じで、
    s "(…And so, our daily life continued like this.){#ch20_s_080}"

    # サイト：（小さな事件も起きるけど、俺がルイズの
    s "(Small incidents happen, but the hard fact that I'm Louise's familiar doesn't change at all.){#ch20_s_081}"

    # サイト：（結局、今日も俺はルイズの使い魔なのです）
    s "(After all, today too I am Louise's familiar.){#ch20_s_082}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ГЛАВЫ 20 ====
    jump attention
    return

