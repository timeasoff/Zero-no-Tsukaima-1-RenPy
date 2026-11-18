# Глава 23, часть 3 (сцены 879–893): ловушка Акины, иллюзия Пустоты, победа.
# Источник: ps2_source/chapters/chapter_24_沈黙の応援.txt (SCENE 879-893).

label ch23_3:
    $ tndl(None)
    $ show_sprites()

label ch23_3_scene_879:

    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：姫さま。
    voice "ch23_l_060"
    l "Princess. Would you grant me permission to use Void magic?{#ch23_l_060}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：え、まじかよ！  [voice 12341]
    voice "ch23_s_085"
    s "Eh, seriously!?{#ch23_s_085}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：この都で虚無の魔法を、ですか？  [voice 644]
    voice "ch23_h_030"
    h "Void magic, in this capital?{#ch23_h_030}"

    # ルイズ：はい。
    voice "ch23_l_061"
    l "Yes. I think it's the only way.{#ch23_l_061}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：おい、待てよルイズっ！？
    voice "ch23_s_086"
    s "Hey, wait a second, Louise!? If you use Void, the whole city will be blown away!{#ch23_s_086}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：それぐらいのこと、わたしだって分かるわよっ！
    voice "ch23_l_062"
    l "I know that much myself! I've thought of another way, so just be quiet for a moment!!{#ch23_l_062}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：姫さまお願いです。
    voice "ch23_l_063"
    l "Princess, please! Let me use the magic!{#ch23_l_063}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：分かりました、ルイズ。
    voice "ch23_h_031"
    h "All right, Louise. I leave it to you.{#ch23_h_031}"

    # ルイズ：ありがとうございます、姫さま。  [voice 6728]
    voice "ch23_l_064"
    l "Thank you, Princess.{#ch23_l_064}"

    menu:
        "Believe in Louise's power{#ch23_3_c_879_1}":
            jump ch23_3_scene_880
        "Is there a chance of winning?{#ch23_3_c_879_2}":
            jump ch23_3_scene_881
        "If we die, we die together{#ch23_3_c_879_3}":
            jump ch23_3_scene_882

label ch23_3_scene_880:

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：頑張れよ、ルイズ。
    voice "ch23_s_087"
    s "Do your best, Louise. I believe in your magic. When the enemy attacks, I'll definitely protect you.{#ch23_s_087}"

    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：うん……。
    voice "ch23_l_065"
    l "Mm… I'll do my best, too.{#ch23_l_065}"

    # → next scene 883
    jump ch23_3_scene_883

label ch23_3_scene_881:

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：それで、勝算はあるのか？  [voice 12344]
    voice "ch23_s_088"
    s "So, do you have a chance of winning?{#ch23_s_088}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：うーんと、そうねぇ。
    voice "ch23_l_066"
    l "Hmm, let me see. I'd say about fifty-fifty.{#ch23_l_066}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：なんだよそれ、大丈夫なのか？  [voice 12345]
    voice "ch23_s_089"
    s "What's that supposed to mean? Are you going to be okay?{#ch23_s_089}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：大丈夫よ。
    voice "ch23_l_067"
    l "It's fine. Anything's better than zero, right?{#ch23_l_067}"

    # → next scene 883
    jump ch23_3_scene_883

label ch23_3_scene_882:

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：なるほど、死なばもろともって奴だな。  [voice 12346]
    voice "ch23_s_090"
    s "I see. So it's a 'if we die, we die together' kind of thing, is it?{#ch23_s_090}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：何よ、それ。  [voice 6732]
    voice "ch23_l_068"
    l "What's that supposed to mean?{#ch23_l_068}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：全部吹き飛ばしちゃうんだろ？
    voice "ch23_s_091"
    s "You're going to blow everything up with Void magic, aren't you?{#ch23_s_091}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：そんなことしないって言ってるでしょ！
    voice "ch23_l_069"
    l "I told you I won't do that! Honestly, you're so slow! Trust your mistress a little more!{#ch23_l_069}"

    # → next scene 883
    jump ch23_3_scene_883

label ch23_3_scene_883:

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：行くわよ、サイト！  [voice 6734]
    voice "ch23_l_070"
    l "Let's go, Saito!{#ch23_l_070}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：おう！  [voice 12348]
    voice "ch23_s_092"
    s "Right!{#ch23_s_092}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 884
    jump ch23_3_scene_884

label ch23_3_scene_884:

    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # ルイズ：あと少しで、屋上へ抜けるわっ！！  [voice 6735]
    voice "ch23_l_071"
    l "Just a little more and we'll be on the roof!!{#ch23_l_071}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：なんで、屋上なんだよ！  [voice 12349]
    voice "ch23_s_093"
    s "Why the roof!?{#ch23_s_093}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：今回の魔法のためには、とにかく一番見晴らしの
    voice "ch23_l_072"
    l "For this spell, I need the spot with the best view, more than anything!{#ch23_l_072}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # ルイズ：しっかり詠唱場所を確保するのよ！
    voice "ch23_l_073"
    l "I need to secure a place to cast! Got it!{#ch23_l_073}"

    # サイト：分かった。  [voice 12350]
    voice "ch23_s_094"
    s "Understood.{#ch23_s_094}"

    # [SPRITE   lay19    image=+944, level=153, dir=1A]
    # [SPRITE   lay5     level=156]
    # [SPRITE   lay1     level=155]
    # デルフリンガー：気をつけろ、相棒！  [voice 1351]
    voice "ch23_d_001"
    d "Watch out, partner!{#ch23_d_001}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay21    image=+1028, level=154, dir=1B]
    # アキナ：くらえっ！！  [voice 108]
    voice "ch23_ak_001"
    ak "Take this!!{#ch23_ak_001}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：ルイズ、あぶない！！  [voice 12351]
    voice "ch23_s_095"
    s "Louise, look out!!{#ch23_s_095}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：きゃあああっ！  [voice 6738]
    voice "ch23_l_074"
    l "Kyaaa!!{#ch23_l_074}"

    # [SPRITE   lay1     hide]
    # [SE       se0      play=+63]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay21    vibrate=21]
    # [SPRITE   lay19    vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [SPRITE   lay1     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay21    hide, reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：ぐゎあああっ！！  [voice 12352]
    voice "ch23_s_096"
    s "Gwaaah!!{#ch23_s_096}"

    # [SPRITE   lay5     image=+407, level=156, dir=1B]
    # サイト：くっ……あぶねー。  [voice 12353]
    voice "ch23_s_097"
    s "Ugh… That was close.{#ch23_s_097}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：今の、爆発……？
    voice "ch23_l_075"
    l "That explosion just now… The bomber is here, isn't she!{#ch23_l_075}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [SPRITE   lay21    image=+1017, level=154, dir=1A]
    # アキナ：やはり、ウェザリー様の言う通り、
    voice "ch23_ak_002"
    ak "Just as Weatherly-sama said, we've been interrupted, haven't we.{#ch23_ak_002}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     image=+308, level=155, dir=1A]
    # ルイズ：あ、あなた……。  [voice 6740]
    voice "ch23_l_076"
    l "Ah… You…{#ch23_l_076}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+407, level=156, dir=1B]
    # サイト：ま、まじかよ。  [voice 12354]
    voice "ch23_s_098"
    s "S-Seriously?{#ch23_s_098}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay21    image=+1019, level=154, dir=1A]
    # アキナ：んふっ……こんにちは、サイトくん。
    voice "ch23_ak_003"
    ak "Heh heh… Hello, Saito-kun. Should I call you Hiraga-kun instead?{#ch23_ak_003}"

    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：春奈！？
    voice "ch23_s_099"
    s "Haruna!? What are you doing here!?{#ch23_s_099}"

    # [SPRITE   lay21    image=+1017, level=154, dir=1A]
    # アキナ：そっちこそ。
    voice "ch23_ak_004"
    ak "I should ask you that. Leaving me behind, why are you in a place like this?{#ch23_ak_004}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：んうっ……。
    voice "ch23_l_077"
    l "Mmm… So the bomber was Haruna!?{#ch23_l_077}"

    # アキナ：そうよ、ルイズ。
    voice "ch23_ak_005"
    ak "That's right, Louise. And my name isn't Haruna.{#ch23_ak_005}"

    # [SPRITE   lay21    image=+1019, level=154, dir=1A]
    # アキナ：ウェザリー様につけていただいた、
    voice "ch23_ak_006"
    ak "I have a name given to me by Weatherly-sama—Akina.{#ch23_ak_006}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：アキナだと？
    voice "ch23_s_100"
    s "Akina? And Weatherly… That Weatherly?{#ch23_s_100}"

    # [SPRITE   lay21    image=+1017, level=154, dir=1A]
    # アキナ：そう……。  [voice 114]
    voice "ch23_ak_007"
    ak "That's right…{#ch23_ak_007}"

    # アキナ：あたしはウェザリー様によって、
    voice "ch23_ak_008"
    ak "I'm a persona—the bomber—created by Weatherly-sama separately from Haruna's consciousness.{#ch23_ak_008}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：ウェザリーって、あの劇団の！？  [voice 6742]
    voice "ch23_l_078"
    l "Weatherly—the one from that theater troupe!?{#ch23_l_078}"

    # [SPRITE   lay21    image=+1021, level=154, dir=1A]
    # アキナ：気安く呼ぶことは万死に値するわね。
    voice "ch23_ak_009"
    ak "Speaking of her so casually is worthy of ten thousand deaths. Weatherly-sama is my boss.{#ch23_ak_009}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：なるほど……春奈がこの世界にやって来たときに
    voice "ch23_s_101"
    s "So… the woman who took care of me when I first came to this world was Weatherly!?{#ch23_s_101}"

    # アキナ：サイト、何度も同じことを言わせないで。
    voice "ch23_ak_010"
    ak "Saito, don't make me say the same thing twice. It hurts.{#ch23_ak_010}"

    # サイト：つまり、俺達はウェザリーに用意された
    voice "ch23_s_102"
    s "So we were dancing neatly on a stage prepared for us by Weatherly, were we?{#ch23_s_102}"

    # [SPRITE   lay21    image=+1019, level=154, dir=1A]
    # アキナ：ふふっ！！
    voice "ch23_ak_011"
    ak "Heh heh!! That's right. It was all a farce, all of it.{#ch23_ak_011}"

    # [SPRITE   lay21    image=+1017, level=154, dir=1A]
    # アキナ：舞台を用意したウェザリー様の手から
    voice "ch23_ak_012"
    ak "Not one of us could escape from the hand of Weatherly-sama, who prepared the stage.{#ch23_ak_012}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+335, level=155, dir=2A]
    # ルイズ：まるで、始めからこうなるのを知ってた
    voice "ch23_l_079"
    l "You sound as if you knew this would happen from the start, don't you?{#ch23_l_079}"

    # アキナ：ハルナはたぶん自分の意思で行動していたと
    voice "ch23_ak_013"
    ak "Haruna probably thinks she was acting of her own will, but it was all my will. Not knowing must be pitiful.{#ch23_ak_013}"

    # アキナ：みんな、かわいそうなハルナに同情して、
    voice "ch23_ak_014"
    ak "You all pitied poor Haruna and went along with her, didn't you? And look at you now.{#ch23_ak_014}"

    # [SPRITE   lay21    image=+1019, level=154, dir=1A]
    # アキナ：あまりにうまく行き過ぎて、
    voice "ch23_ak_015"
    ak "It went so well that I had to strain not to laugh.{#ch23_ak_015}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：春奈の心を操りやがって。  [voice 12359]
    voice "ch23_s_103"
    s "Manipulating Haruna's heart like that…{#ch23_s_103}"

    # [SPRITE   lay21    image=+1017, level=154, dir=1A]
    # アキナ：でも、もうそれもお終い。
    voice "ch23_ak_016"
    ak "But that's over, too. Weatherly-sama is calling for my curtain call.{#ch23_ak_016}"

    # サイト：くっ……。  [voice 12360]
    voice "ch23_s_104"
    s "Ugh…{#ch23_s_104}"

    # アキナ：あら、やる気？
    voice "ch23_ak_017"
    ak "Oh? You're motivated? Can you hurt Haruna's body? Well, I won't hold back, either.{#ch23_ak_017}"

    menu:
        "Yes, I can do it{#ch23_3_c_884_1}":
            jump ch23_3_scene_885
        "That's cowardly!{#ch23_3_c_884_2}":
            jump ch23_3_scene_886
        "There's no way I can!{#ch23_3_c_884_3}":
            jump ch23_3_scene_887

label ch23_3_scene_885:

    # [SPRITE   lay21    image=+1017, level=154, dir=1A]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：ああ、やれるね。
    voice "ch23_s_105"
    s "Yeah, I can. Without a moment's hesitation.{#ch23_s_105}"

    # [SPRITE   lay21    image=+1021, level=154, dir=1A]
    # アキナ：何？  [voice 125]
    voice "ch23_ak_018"
    ak "What?{#ch23_ak_018}"

    # サイト：俺は、ルイズの使い魔だからな！
    voice "ch23_s_106"
    s "Because I'm Louise's familiar! I won't let anyone lay a finger on my mistress!{#ch23_s_106}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # → next scene 888
    jump ch23_3_scene_888

label ch23_3_scene_886:

    # [SPRITE   lay21    image=+1017, level=154, dir=1A]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：卑怯だぞ！  [voice 12363]
    voice "ch23_s_107"
    s "Coward!{#ch23_s_107}"

    # [SPRITE   lay21    image=+1019, level=154, dir=1A]
    # アキナ：あーっはっはっは！
    voice "ch23_ak_019"
    ak "A-ha-ha-ha! Say whatever you like!{#ch23_ak_019}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：やるしかないわ、サイト！  [voice 6744]
    voice "ch23_l_080"
    l "We have no choice but to fight, Saito!{#ch23_l_080}"

    # [SPRITE   lay5     image=+438, level=156, dir=2B]
    # サイト：みたいだな……くそっ！  [voice 12364]
    voice "ch23_s_108"
    s "Looks like it… Damn it!{#ch23_s_108}"

    # → next scene 888
    jump ch23_3_scene_888

label ch23_3_scene_887:

    # [SPRITE   lay21    image=+1017, level=154, dir=1A]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：やれるわけねーじゃねぇか！
    voice "ch23_s_109"
    s "As if I could fight her! Damn it!{#ch23_s_109}"

    # [SPRITE   lay21    image=+1019, level=154, dir=1A]
    # アキナ：あーっはっはっは！
    voice "ch23_ak_020"
    ak "A-ha-ha-ha! If you're going to be killed by the woman you loved, that's a fine end for you, isn't it!?{#ch23_ak_020}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：サイト！
    voice "ch23_l_081"
    l "Saito! That's not Haruna now! We have to save her!{#ch23_l_081}"

    # [SPRITE   lay5     image=+438, level=156, dir=2B]
    # サイト：そうだな。
    voice "ch23_s_110"
    s "You're right. Damn it!{#ch23_s_110}"

    # → next scene 888
    jump ch23_3_scene_888

label ch23_3_scene_888:

    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [SE       se0      play=+65]
    # [SPRITE   lay5     image=+471, level=156, dir=3B]
    # サイト：行くぜ、ルイズ！  [voice 12367]
    voice "ch23_s_111"
    s "Let's go, Louise!{#ch23_s_111}"

    # [SPRITE   lay1     image=+368, level=155, dir=3A]
    # ルイズ：ええ、分かったわ。  [voice 6746]
    voice "ch23_l_082"
    l "Yes, I understand.{#ch23_l_082}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 889
    jump ch23_3_scene_889

label ch23_3_scene_889:

    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：んぐはぁっ……！！  [voice 128]
    voice "ch23_ak_021"
    ak "Mmguah…!!{#ch23_ak_021}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # ルイズ：はぁ……やったゎ……。  [voice 6747]
    voice "ch23_l_083"
    l "Haa… We did it…{#ch23_l_083}"

    # サイト：ぐはぁ……。
    voice "ch23_s_112"
    s "Guh… You okay, Louise?{#ch23_s_112}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：うん……。
    voice "ch23_l_084"
    l "Mm… Somehow.{#ch23_l_084}"

    # サイト：（俺もルイズも、その場にへたり込んでいた）
    s "(Both Louise and I had collapsed on the spot.){#ch23_s_113}"

    # [SPRITE   lay5     level=156]
    # [SPRITE   lay1     level=155]
    # [SPRITE   lay19    image=+940, level=152, dir=1A]
    # デルフリンガー：てぇしたもんだな、相棒はよぉ。  [voice 1352]
    voice "ch23_d_002"
    d "Nice work, partner.{#ch23_d_002}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     image=+434, level=156, dir=2B]
    # サイト：へへっ。
    voice "ch23_s_114"
    s "Heh. Praising me here won't get you anything. More importantly, is Haruna all right…!?{#ch23_s_114}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+407, level=156, dir=1B]
    # サイト：（特にひどい外傷は無さそうだが……）
    s "(No serious external injuries, it seems…){#ch23_s_115}"

    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：大丈夫かぁ、春奈っ？  [voice 12370]
    voice "ch23_s_116"
    s "You okay, Haruna?{#ch23_s_116}"

    # ハルナ：……。
    ha "…{#ch23_ha_001}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：大丈夫みたい。
    voice "ch23_l_085"
    l "She seems fine. No danger to her life.{#ch23_l_085}"

    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：ああ、大丈夫みたいだ。  [voice 12371]
    voice "ch23_s_117"
    s "Ah, she seems fine.{#ch23_s_117}"

    # [SPRITE   lay1     image=+335, level=155, dir=2A]
    # ルイズ：でも、縄で縛っておいて。
    voice "ch23_l_086"
    l "But tie her up with rope. If she's still Akina, she'd be dangerous.{#ch23_l_086}"

    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # サイト：でも……。  [voice 12372]
    voice "ch23_s_118"
    s "But…{#ch23_s_118}"

    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：お願い。  [voice 6751]
    voice "ch23_l_087"
    l "Please.{#ch23_l_087}"

    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：分かった。  [voice 12373]
    voice "ch23_s_119"
    s "All right.{#ch23_s_119}"

    # [SPRITE   lay5     image=+403, level=156, dir=1B]
    # サイト：それより、ルイズ。
    voice "ch23_s_120"
    s "More importantly, Louise. Use Void magic, please!{#ch23_s_120}"

    # ルイズ：うん。  [voice 6752]
    voice "ch23_l_088"
    l "Mm.{#ch23_l_088}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+140, level=80]
    $ dissolve_fx("id(140)")
    # [TRANS trans("crossfade", 1000)]
    # ルイズ：必ず成功させるから。
    voice "ch23_l_089"
    l "I'll make it succeed, for sure. Watch closely!{#ch23_l_089}"

    # サイト：ああ……見せてくれ。  [voice 12375]
    voice "ch23_s_121"
    s "Ah… Show me.{#ch23_s_121}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # ルイズ：イリュージョン！！  [voice 6754]
    voice "ch23_l_090"
    l "Illusion!!{#ch23_l_090}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+141, level=80]
    $ dissolve_fx("id(141)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # ルイズ：サイト！
    voice "ch23_l_091"
    l "Saito! Look at the legendary spell I chanted!{#ch23_l_091}"

    # サイト：……こいつは、すげぇや。  [voice 12376]
    voice "ch23_s_122"
    s "…This is incredible.{#ch23_s_122}"

    # サイト：（空一面を埋め尽くすかのような大艦隊が、
    s "(A huge fleet, enough to fill the whole sky, covered Tristain above in darkness.){#ch23_s_123}"

    # サイト：ルイズが使おうとしていた魔法ってのは、
    voice "ch23_s_124"
    s "The spell Louise was about to use was an incredible one, wasn't it.{#ch23_s_124}"

    # ルイズ：だけど、これは虚無の産物だから。
    voice "ch23_l_092"
    l "But this is a product of Void. An illusion born of Void… a dream spell.{#ch23_l_092}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+403, level=156, dir=1B]
    # サイト：あっ……すげぇ！！
    voice "ch23_s_125"
    s "Ah… Amazing!! The enemy is running from the batteries!{#ch23_s_125}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+337, level=155, dir=2A]
    # ルイズ：うふふっ……。
    voice "ch23_l_093"
    l "Heh heh… My magic is quite something, too, isn't it?{#ch23_l_093}"

    menu:
        "Good work, Louise{#ch23_3_c_889_1}":
            jump ch23_3_scene_890
        "I can return the charm{#ch23_3_c_889_2}":
            jump ch23_3_scene_891
        "The fight will go on{#ch23_3_c_889_3}":
            jump ch23_3_scene_892

label ch23_3_scene_890:

    # [SPRITE   lay5     image=+403, level=156, dir=1B]
    # [SPRITE   lay1     image=+337, level=155, dir=2A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [SPRITE   lay5     image=+434, level=156, dir=2B]
    # サイト：ひとまずお疲れさま、ルイズ。  [voice 12379]
    voice "ch23_s_126"
    s "Well done for now, Louise.{#ch23_s_126}"

    # [SPRITE   lay1     image=+304, level=155, dir=1A]
    # ルイズ：うん……。
    voice "ch23_l_094"
    l "Mm… The fighting isn't over yet. But there's nothing more we can do now.{#ch23_l_094}"

    # [SPRITE   lay1     image=+337, level=155, dir=2A]
    # ルイズ：サイトも、お疲れさま。
    voice "ch23_l_095"
    l "You've worked hard too, Saito. I'm grateful to you today.{#ch23_l_095}"

    # → next scene 893
    jump ch23_3_scene_893

label ch23_3_scene_891:

    # [SPRITE   lay5     image=+403, level=156, dir=1B]
    # [SPRITE   lay1     image=+337, level=155, dir=2A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [SPRITE   lay5     image=+434, level=156, dir=2B]
    # サイト：これでどうにか、約束は果たせそうだ。  [voice 12380]
    voice "ch23_s_127"
    s "Now I might be able to keep my promise.{#ch23_s_127}"

    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：約束っ？  [voice 6760]
    voice "ch23_l_096"
    l "Promise?{#ch23_l_096}"

    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：シエスタから、お守りを預かってきたから。
    voice "ch23_s_128"
    s "I borrowed a charm from Siesta. Now I can return it to her.{#ch23_s_128}"

    # ルイズ：ふぅ～～～ん、お守りかぁ。  [voice 6761]
    voice "ch23_l_097"
    l "Huuuuh, a charm, was it…{#ch23_l_097}"

    # サイト：こいつを身につけていれば、
    voice "ch23_s_129"
    s "They say wearing it lets you avoid any disaster.{#ch23_s_129}"

    # ルイズ：そっか……意外と効いてたのかもね？  [voice 6762]
    voice "ch23_l_098"
    l "I see… Maybe it really worked, then?{#ch23_l_098}"

    # [SPRITE   lay5     image=+434, level=156, dir=2B]
    # サイト：ん、そうだな。
    voice "ch23_s_130"
    s "Yeah, I'd say so. It was rough, but we won.{#ch23_s_130}"

    # [SPRITE   lay1     image=+335, level=155, dir=2A]
    # ルイズ：……なんか頭にきちゃう。  [voice 6763]
    voice "ch23_l_099"
    l "…It makes me angry, somehow.{#ch23_l_099}"

    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # サイト：な、なんでだよ！  [voice 12384]
    voice "ch23_s_131"
    s "W-Why!?{#ch23_s_131}"

    # → next scene 893
    jump ch23_3_scene_893

label ch23_3_scene_892:

    # [SPRITE   lay5     image=+403, level=156, dir=1B]
    # [SPRITE   lay1     image=+337, level=155, dir=2A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # サイト：今日はこれでしのげたけど、
    voice "ch23_s_132"
    s "We got through today, but do you think there'll be another war?{#ch23_s_132}"

    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：たぶんね。  [voice 6764]
    voice "ch23_l_100"
    l "Probably.{#ch23_l_100}"

    # [SPRITE   lay1     image=+337, level=155, dir=2A]
    # ルイズ：とりあえず今日は都を守ることができた。
    voice "ch23_l_101"
    l "For now we saved the capital. Isn't that enough? We'll think about the rest when the time comes.{#ch23_l_101}"

    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：ん……。
    voice "ch23_s_133"
    s "Mm… You're right.{#ch23_s_133}"

    # → next scene 893
    jump ch23_3_scene_893

label ch23_3_scene_893:

    # [SPRITE   lay1     image=+337, level=155, dir=2A]
    # [SPRITE   lay5     image=+434, level=156, dir=2B]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+71, level=200]
    $ fade_fx("id(71)")
    # [SPRITE   lay1     image=+337, level=155, dir=2A]
    # ルイズ：それじゃ行きましょ。
    voice "ch23_l_102"
    l "Well then, let's go. The princess is waiting.{#ch23_l_102}"

    # [SPRITE   lay5     image=+434, level=156, dir=2B]
    # サイト：そうだな。  [voice 12387]
    voice "ch23_s_134"
    s "You're right.{#ch23_s_134}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：（シエスタ、約束は守ったよ）
    s "(Siesta, I kept my promise.){#ch23_s_135}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=4000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 899
    jump ch24

    # ==== КОНЕЦ ГЛАВЫ 23 ====
    jump ch24
    return

