# Глава 27, часть 2 (сцены 985–993): распределение ролей, чары Табасы, засада.
# Источник: ps2_source/chapters/chapter_28_ハルナの秘密.txt (SCENE 985-993).

label ch27_2:
    $ tndl(None)
    $ show_sprites()

label ch27_2_scene_985:

    # [SPRITE   lay8     image=+797, level=160, dir=2A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：とにかく俺は納得してないですからね。  [voice 12770]
    voice "ch27_s_062"
    s "Anyway, I'm not convinced!{#ch27_s_062}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ちょっと、サイト。
    voice "ch27_l_045"
    l "Hey, Saito. It seems you and I have a difference of opinion about Void magic, don't we?{#ch27_l_045}"

    # サイト：見解の相違ってなんのことだよ？
    voice "ch27_s_063"
    s "A difference of opinion? You're going to blow Tristain and the infiltrators away together, aren't you?{#ch27_s_063}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：だーかーらぁ、そうじゃないって。
    voice "ch27_l_046"
    l "Nooo—I said we'll use a different spell. Don't worry.{#ch27_l_046}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：別の魔法？  [voice 12772]
    voice "ch27_s_064"
    s "A different spell?{#ch27_s_064}"

    # [SPRITE   lay1     image=+337, level=160, dir=2A]
    # ルイズ：そ、別の魔法よ。  [voice 6946]
    voice "ch27_l_047"
    l "Y-Yes, a different spell.{#ch27_l_047}"

    # サイト：（別な魔法って、一体どんな魔法だよ……）
    s "(What kind of 'different spell' could that be…?){#ch27_s_065}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 986
    jump ch27_2_scene_986

label ch27_2_scene_986:

    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+3]
    play music t2 fadein 1.0
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なあ、いったいどうするつもりなんだよ？  [voice 12773]
    voice "ch27_s_066"
    s "Say—what are you actually planning?{#ch27_s_066}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：だーかーらぁ、サイトは心配しなくたって
    voice "ch27_l_048"
    l "I've told you—you don't need to worry, Saito.{#ch27_l_048}"

    # サイト：そんなこといったって、心配だろ？
    voice "ch27_s_067"
    s "Even if you say that—I'm worried! At this rate, the whole capital could be blown away!{#ch27_s_067}"

    # ルイズ：そんなことするわけないでしょ。
    voice "ch27_l_049"
    l "I'm not going to do that. How many times do I have to tell you!?{#ch27_l_049}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：あんまりしつこいこと言ってると、
    voice "ch27_l_050"
    l "If you keep nagging, I'll blow you away first!{#ch27_l_050}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：あのなぁーっ！？  [voice 12775]
    voice "ch27_s_068"
    s "Hey!!{#ch27_s_068}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：ほら、みんながいるわよ。
    voice "ch27_l_051"
    l "See? Everyone's here. Enough—this discussion is over!{#ch27_l_051}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：おしまいって……。  [voice 12776]
    voice "ch27_s_069"
    s "Over, you say…{#ch27_s_069}"

    # サイト：（確かに、キュルケ達がいる前で、
    s "(True—we can't talk about Void magic in front of Kirche and the others…){#ch27_s_070}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あっ、ダーリン！  [voice 3590]
    voice "ch27_k_022"
    k "Ah, darling!{#ch27_k_022}"

    # キュルケ：女王陛下のところまでわざわざ出向いて、
    voice "ch27_k_023"
    k "You went all the way to the Queen—what did you do!?{#ch27_k_023}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：俺がじゃなくて、ルイズがお姫さまに用が
    voice "ch27_s_071"
    s "It wasn't me—Louise had business with the princess.{#ch27_s_071}"

    # キュルケ：ふーん……。
    voice "ch27_k_024"
    k "Hmm… Louise has quite the influence, doesn't she?{#ch27_k_024}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：意外と、ってなによっ！
    voice "ch27_l_052"
    l "What do you mean, 'quite'!? I'm…!!{#ch27_l_052}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：まあ、いいわ。
    voice "ch27_l_053"
    l "Well, whatever. More importantly, let's divide up our roles.{#ch27_l_053}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：役割分担って、何の話だよ？  [voice 12778]
    voice "ch27_s_072"
    s "Divide up roles—what are you talking about?{#ch27_s_072}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：決まってるでしょ？
    voice "ch27_l_054"
    l "It's obvious. We decide who fights what.{#ch27_l_054}"

    # ルイズ：トリステインの外からは、
    voice "ch27_l_055"
    l "Reconquista is closing in from outside Tristain, and Akina is rampaging inside.{#ch27_l_055}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：へっ？
    voice "ch27_s_073"
    s "Huh? Shouldn't we all rush to take down Akina first?{#ch27_s_073}"

    # ルイズ：そんなことしてたら、わたしの呪文の準備が
    voice "ch27_l_056"
    l "If we do that, my spell's preparation might not be ready in time. And how would we even find Akina?{#ch27_l_056}"

    # ルイズ：それよりは、少し考え方を変えて、
    voice "ch27_l_057"
    l "Better to shift our thinking a little—deal with the air fleet while knocking down Akina when she interferes.{#ch27_l_057}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：そう言われてみればそうだな。
    voice "ch27_s_074"
    s "When you put it that way… Even if Akina doesn't show, we can handle the fleet first and deal with her later.{#ch27_s_074}"

    # ルイズ：じゃ、二手に分けるわよ。
    voice "ch27_l_058"
    l "Then we'll split in two. One team for Akina, one for the air fleet.{#ch27_l_058}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：ねえ、ルイズ。
    voice "ch27_k_025"
    k "Hey, Louise. Are we really okay splitting up?{#ch27_k_025}"

    # キュルケ：空中艦隊の相手は全員がかりでも無理よ。
    voice "ch27_k_026"
    k "The air fleet won't be handled even with everyone. And yet you want to split our forces…{#ch27_k_026}"

    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：まあ、その辺はわたしに任せてよ。
    voice "ch27_l_059"
    l "Well, leave that part to me. I have a trump card.{#ch27_l_059}"

    # キュルケ：とっておきって？  [voice 3595]
    voice "ch27_k_027"
    k "A trump card?{#ch27_k_027}"

    # ルイズ：それを言ったら、意味ないじゃない？
    voice "ch27_l_060"
    l "If I told you, it wouldn't be a trump card, would it? So—I'll take the air fleet; Tabitha takes Akina…{#ch27_l_060}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：うん。  [voice 15741]
    voice "ch27_t_011"
    t "Mm.{#ch27_t_011}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：サイトとキュルケはどうするの？  [voice 6960]
    voice "ch27_l_061"
    l "What about Saito and Kirche?{#ch27_l_061}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+713, level=160, dir=2A]
    # キュルケ：えーっ！？
    voice "ch27_k_028"
    k "Ehh!? I can't team up with darling!? What's the reason?{#ch27_k_028}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：理由なんてないわよ。
    voice "ch27_l_062"
    l "There's no reason. It's my strategy.{#ch27_l_062}"

    # [SPRITE   lay6     image=+715, level=160, dir=2A]
    # キュルケ：わ、分かったわよ。  [voice 3597]
    voice "ch27_k_029"
    k "I-I understand.{#ch27_k_029}"

    # ルイズ：で、サイトはわたしとタバサ、
    voice "ch27_l_063"
    l "So, Saito—which do you want to team with, Louise or Tabitha?{#ch27_l_063}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：（どっちと組みたいって……。
    s "Which I want… Shouldn't it be decided by the enemy we're facing?{#ch27_s_075}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch27_t_012}"

    # サイト：（そうだなぁ……。
    s "(Hmm… Louise says she'll use Void, which worries me…){#ch27_s_076}"

    # サイト：（タバサは火傷が治ってるとはいえ、
    s "(Tabitha's burns have healed, but she's not at full strength, so I'm worried…){#ch27_s_077}"

    # サイト：（そんなわけで、どちらかというと、
    s "(So, honestly, I'm far more worried about Tabitha…){#ch27_s_078}"

    # サイト：うーん……。  [voice 12781]
    voice "ch27_s_079"
    s "Hmm…{#ch27_s_079}"

    menu:
        "Leave it to Tabitha{#ch27_2_c_986_1}":
            jump ch27_2_scene_987
        "Worried about after{#ch27_2_c_986_2}":
            jump ch27_2_scene_988
        "Worried about everyone{#ch27_2_c_986_3}":
            jump ch27_2_scene_989

label ch27_2_scene_987:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [BGM      bgm      play=+3]
    play music t2 fadein 1.0
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：やっぱり、ルイズかな。  [voice 12782]
    voice "ch27_s_080"
    s "I think… Louise, after all.{#ch27_s_080}"

    # サイト：（空中艦隊を相手にするとか言ってるけど、
    s "(She says she'll fight the air fleet, but Void's power worries me…){#ch27_s_081}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+713, level=160, dir=2A]
    # キュルケ：ちょっと、ダーリン！  [voice 3598]
    voice "ch27_k_030"
    k "Hey, darling!{#ch27_k_030}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：な、なんだよ……。  [voice 12783]
    voice "ch27_s_082"
    s "Wh-What is it…?{#ch27_s_082}"

    # キュルケ：ダーリンはタバサと組んで。
    voice "ch27_k_031"
    k "Darling will team with Tabitha. I'll team with Louise.{#ch27_k_031}"

    # サイト：えっ、でも俺がタバサと組んだら……。
    voice "ch27_s_083"
    s "Eh, but if I team with Tabitha… It'll be like last time…{#ch27_s_083}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：今度は大丈夫……。  [voice 15742]
    voice "ch27_t_013"
    t "It'll be fine this time…{#ch27_t_013}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：ということで、ルイズとはあたしが組むから。  [voice 3600]
    voice "ch27_k_032"
    k "So—I'll be with Louise.{#ch27_k_032}"

    # → next scene 990
    jump ch27_2_scene_990

label ch27_2_scene_988:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [BGM      bgm      play=+3]
    play music t2 fadein 1.0
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：やっぱり、タバサかな。  [voice 12785]
    voice "ch27_s_084"
    s "I think… Tabitha, after all.{#ch27_s_084}"

    # [LAYER    lay0     image=+590, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch27_t_014}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：（アキナの相手は急がなくちゃならないけれど、
    s "(Akina needs dealing with quickly, but the fleet won't arrive for a while yet…){#ch27_s_085}"

    # サイト：（それに、アキナを倒したあと、春奈の身柄を
    s "(And after Akina's down, I need to be there when they decide Haruna's fate…){#ch27_s_086}"

    # サイト：（あと何より、タバサが無茶しないかどうかが
    s "(More than anything, I'm worried Tabitha will overdo it…){#ch27_s_087}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：いい判断をしたわね、ダーリン。  [voice 3601]
    voice "ch27_k_033"
    k "Good choice, darling.{#ch27_k_033}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ん？
    voice "ch27_s_088"
    s "Hmm? Why?{#ch27_s_088}"

    # キュルケ：だって、タバサが喜んでるもの。  [voice 3602]
    voice "ch27_k_034"
    k "Because Tabitha is happy.{#ch27_k_034}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+596, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch27_t_015}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：それって、わたしはどうでもいいわけ？  [voice 6963]
    voice "ch27_l_064"
    l "So I don't matter, do I?{#ch27_l_064}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：い、いやそんなこと無いって。
    voice "ch27_s_089"
    s "N-No, that's not it! Well then—Kirche, take care of Louise, please.{#ch27_s_089}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：任せといて、ダーリン。
    voice "ch27_k_035"
    k "Leave it to me, darling. I'll keep a close eye on Louise.{#ch27_k_035}"

    # → next scene 990
    jump ch27_2_scene_990

label ch27_2_scene_989:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [BGM      bgm      play=+3]
    play music t2 fadein 1.0
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ごめん、キュルケが先に決めて。  [voice 12788]
    voice "ch27_s_090"
    s "Sorry—let Kirche decide first.{#ch27_s_090}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+713, level=160, dir=2A]
    # キュルケ：えーっ！？
    voice "ch27_k_036"
    k "Ehh!? In a case like this, a boy needs to decide firmly, darling!{#ch27_k_036}"

    # サイト：そうは言うけど……。
    voice "ch27_s_091"
    s "I know, but… I want to be with both of them, you see…{#ch27_s_091}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：じゃあ、ダーリンはタバサと組むべきね。  [voice 3605]
    voice "ch27_k_037"
    k "Then darling should team with Tabitha.{#ch27_k_037}"

    # サイト：えっ、なんで？  [voice 12790]
    voice "ch27_s_092"
    s "Eh, why?{#ch27_s_092}"

    # キュルケ：ああ見えて、タバサはダーリンと
    voice "ch27_k_038"
    k "Even if she looks like that, Tabitha wants to team with darling.{#ch27_k_038}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+596, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch27_t_016}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：分かった。
    voice "ch27_s_093"
    s "Got it. Tabitha, please.{#ch27_s_093}"

    # [LAYER    lay0     image=+590, level=160, dir=1A]
    # タバサ：うん……。  [voice 15743]
    voice "ch27_t_017"
    t "…Mm.{#ch27_t_017}"

    # [LAYER    lay0     hide]
    # → next scene 990
    jump ch27_2_scene_990

label ch27_2_scene_990:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [BGM      bgm      play=+3]
    play music t2 fadein 1.0
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：じゃあ、ダーリン、タバサ。
    voice "ch27_k_039"
    k "Well then, darling, Tabitha—take care of Haruna.{#ch27_k_039}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ああ、分かった。
    voice "ch27_s_094"
    s "Ah, I understand. Louise, Kirche—please.{#ch27_s_094}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：もう、バカ使い魔はご主人様を信じていれば
    voice "ch27_l_065"
    l "Honestly—you just need to trust your mistress, you silly familiar.{#ch27_l_065}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：それにタバサに何かしたら、
    voice "ch27_l_066"
    l "And if you do anything to Tabitha, you'll be punished later!{#ch27_l_066}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：何もしないって。  [voice 12793]
    voice "ch27_s_095"
    s "I won't do anything.{#ch27_s_095}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [TRANS trans("crossfade", 1000)]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # サイト：さて……。  [voice 12794]
    voice "ch27_s_096"
    s "Well then…{#ch27_s_096}"

    # サイト：アキナは、こっちが屋上で変な動きを
    voice "ch27_s_097"
    s "If we make a scene on the roof, we can probably lure Akina out—but…{#ch27_s_097}"

    # サイト：でも、タバサの体は大丈夫なのか？
    voice "ch27_s_098"
    s "Is Tabitha's body really all right? Her burns are healed, but she's not at full strength, is she…{#ch27_s_098}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch27_t_018}"

    # サイト：やっぱり、不安なのか？  [voice 12797]
    voice "ch27_s_099"
    s "You're still worried?{#ch27_s_099}"

    # タバサ：……うん。  [voice 15744]
    voice "ch27_t_019"
    t "…Mm.{#ch27_t_019}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：俺としては、タバサに無理はして
    voice "ch27_s_100"
    s "I don't want Tabitha to overdo it…{#ch27_s_100}"

    # タバサ：……。
    t "…{#ch27_t_020}"

    # → next scene 991
    jump ch27_2_scene_991

    # checkKiss(): ветка 991/992 — zero_kiss не портирован; идём по ветке zero_kiss (991), как в гл.12
label ch27_2_scene_991:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [LAYER    lay0     image=+596, level=160, dir=1A]
    # タバサ：……あの。  [voice 15745]
    voice "ch27_t_021"
    t "…Um.{#ch27_t_021}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ん？
    voice "ch27_s_101"
    s "Hmm? What's wrong?{#ch27_s_101}"

    # タバサ：おまじない。  [voice 15746]
    voice "ch27_t_022"
    t "A charm.{#ch27_t_022}"

    # サイト：おまじない？  [voice 12800]
    voice "ch27_s_102"
    s "A charm?{#ch27_s_102}"

    # タバサ：うん。
    voice "ch27_t_023"
    t "Mm. I want a charm.{#ch27_t_023}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：えっと、俺にできることならするけど……？  [voice 12801]
    voice "ch27_s_103"
    s "Um, I'll do what I can, but…?{#ch27_s_103}"

    # タバサ：あなたじゃなきゃダメ。  [voice 15748]
    voice "ch27_t_024"
    t "It has to be you.{#ch27_t_024}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：そっか。
    voice "ch27_s_104"
    s "I see. Then what should I do?{#ch27_s_104}"

    # タバサ：目を閉じていて。  [voice 15749]
    voice "ch27_t_025"
    t "Close your eyes.{#ch27_t_025}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：えっ、そんなことでいいの？
    voice "ch27_s_105"
    s "Eh? That's all? Well then, I'll close them…{#ch27_s_105}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # タバサ：……。
    t "…{#ch27_t_026}"

    # サイト：本当にいいのか？  [voice 12804]
    voice "ch27_s_106"
    s "Are you sure?{#ch27_s_106}"

    # タバサ：うん。  [voice 15750]
    voice "ch27_t_027"
    t "Mm.{#ch27_t_027}"

    # サイト：（何をするつもりなんだろ？）
    s "(What is she going to do…?){#ch27_s_107}"

    # [EVENT_CG event    image=+245, level=80]
    $ dissolve_fx("id(245)")
    # [TRANS trans("crossfade", 1000)]
    # タバサ：（……チュッ）  [voice 15751]
    voice "ch27_t_028"
    t "(…Chu.){#ch27_t_028}"

    # サイト：えっ、ええーっ？
    voice "ch27_s_108"
    s "Eh? Ehh!? W-What did you just do!?{#ch27_s_108}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # [LAYER    lay0     image=+596, level=160, dir=1A]
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [EVENT_CG event    hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # タバサ：……。
    t "…{#ch27_t_029}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：あ、あの……。
    voice "ch27_s_109"
    s "U-Um… There was something incredibly soft…{#ch27_s_109}"

    # タバサ：……。
    t "…{#ch27_t_030}"

    # [SPRITE   lay5     image=+431, level=160, dir=2A]
    # サイト：こっ、これはひょっとして……。
    voice "ch27_s_110"
    s "Th-This couldn't be… I-It's a k-k-k…{#ch27_s_110}"

    # タバサ：……い、言わないで。
    voice "ch27_t_031"
    t "…D-Don't say it. It's embarrassing.{#ch27_t_031}"

    # サイト：恥ずかしいって……。  [voice 12808]
    voice "ch27_s_111"
    s "Embarrassing, you say…{#ch27_s_111}"

    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # サイト：もし良かったら、今のおまじない。
    voice "ch27_s_112"
    s "If it's all right… Could you do that charm again?{#ch27_s_112}"

    # タバサ：ダ、ダメ。  [voice 15753]
    voice "ch27_t_032"
    t "N-No.{#ch27_t_032}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：そ、そっか……。
    voice "ch27_s_113"
    s "O-Oh… Ha ha ha…{#ch27_s_113}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # → next scene 993
    jump ch27_2_scene_993

label ch27_2_scene_992:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：うん、大丈夫。  [voice 15754]
    voice "ch27_t_033"
    t "Mm, I'm fine.{#ch27_t_033}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：だったらいいんだけど……。
    voice "ch27_s_114"
    s "Then that's fine… But don't overdo it, okay?{#ch27_s_114}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # → next scene 993
    jump ch27_2_scene_993

label ch27_2_scene_993:

    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：街に出たのはいいけれど……。
    voice "ch27_s_115"
    s "We made it to the town—but will Akina really show up before us?{#ch27_s_115}"

    # タバサ：来る。  [voice 15755]
    voice "ch27_t_034"
    t "She'll come.{#ch27_t_034}"

    # [SPRITE   lay5     image=+434, level=160, dir=2B]
    # サイト：言い切ったね。  [voice 12813]
    voice "ch27_s_116"
    s "You sound sure.{#ch27_s_116}"

    # タバサ：わたしがハルナを狙っていることを、
    voice "ch27_t_035"
    t "I spread word that I'm targeting Haruna.{#ch27_t_035}"

    # タバサ：狙ってくるのはわたし。  [voice 15757]
    voice "ch27_t_036"
    t "The one she'll go after is me.{#ch27_t_036}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：自らエサになるって作戦か……。
    voice "ch27_s_117"
    s "A plan to become bait yourself…? Say—is a request always this painful?{#ch27_s_117}"

    # タバサ：つらい。
    voice "ch27_t_037"
    t "Painful. But now, just a little less painful.{#ch27_t_037}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：なんで？  [voice 12815]
    voice "ch27_s_118"
    s "Why?{#ch27_s_118}"

    # [LAYER    lay0     image=+596, level=160, dir=1A]
    # タバサ：サイトがいるから。  [voice 15759]
    voice "ch27_t_038"
    t "Because Saito is here.{#ch27_t_038}"

    # [SPRITE   lay5     image=+409, level=160, dir=1B]
    # サイト：……。  [voice 12816]
    voice "ch27_s_119"
    s "…{#ch27_s_119}"

    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：……来た。  [voice 15760]
    voice "ch27_t_039"
    t "…She's here.{#ch27_t_039}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：えっ？  [voice 12817]
    voice "ch27_s_120"
    s "Eh?{#ch27_s_120}"

    # アキナ：アッハハハッ、ハハーッ！
    voice "ch27_ak_003"
    ak "Ah ha ha ha! Ha ha! A-ha-ha-ha!!{#ch27_ak_003}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：この声は、まさか？  [voice 12818]
    voice "ch27_s_121"
    s "That voice—could it be?{#ch27_s_121}"

    # タバサ：うん。  [voice 15761]
    voice "ch27_t_040"
    t "Mm.{#ch27_t_040}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：アハハッ、見つけたわよーっ？  [voice 156]
    voice "ch27_ak_004"
    ak "Ah ha—found you!{#ch27_ak_004}"

    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：というか、お前……。
    voice "ch27_s_122"
    s "I mean—how did you know we were here?{#ch27_s_122}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：おまえ達の動向は、このあたしが逐一監視
    voice "ch27_ak_005"
    ak "I've been watching your every move!{#ch27_ak_005}"

    # アキナ：タバサがあたしの命を狙ってるんだって？
    voice "ch27_ak_006"
    ak "Tabitha's after my life? That's a million years too early.{#ch27_ak_006}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：おいおい、春奈はまだ１０代だって。  [voice 12820]
    voice "ch27_s_123"
    s "Hey now—Haruna's still a teenager.{#ch27_s_123}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+658, level=160, dir=3A]
    # タバサ：今度は倒す。  [voice 15762]
    voice "ch27_t_041"
    t "This time I'll defeat you.{#ch27_t_041}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：へぇーっ、そりゃあ楽しみだね。  [voice 159]
    voice "ch27_ak_007"
    ak "Ehh—that sounds fun.{#ch27_ak_007}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：デルフッ、抜くぞっ！  [voice 12821]
    voice "ch27_s_124"
    s "Derf—draw!{#ch27_s_124}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    hide]
    # [BG       stage    hide]
    # → next scene 994
    jump ch27_3

    # ==== КОНЕЦ ЧАСТИ 2 ====
    jump ch27_3
    return

