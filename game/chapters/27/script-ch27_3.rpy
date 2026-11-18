# Глава 27, часть 3 (сцены 994–998): флот Луизы, пленение Акины.
# Источник: ps2_source/chapters/chapter_28_ハルナの秘密.txt (SCENE 994-998).

label ch27_3:
    $ tndl(None)
    $ show_sprites(None)

label ch27_3_scene_994:

    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # [SPRITE   lay5     image=+471, level=160, dir=3B]
    # サイト：……どうだーっ！！  [voice 12823]
    voice "ch27_s_125"
    s "…How's that!?{#ch27_s_125}"

    # デルフリンガー：かなり効いてるみたいだぜ、相棒。
    voice "ch27_d_001"
    d "It seems to be working well, partner. She's reeling now.{#ch27_d_001}"

    # [SPRITE   lay5     image=+473, level=160, dir=3B]
    # サイト：そうか……。  [voice 12824]
    voice "ch27_s_126"
    s "I see…{#ch27_s_126}"

    # サイト：（あとは、春奈の体を確保できれば……）
    s "(Now, if we can just secure Haruna's body…){#ch27_s_127}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    hide]
    # [SPRITE   lay19    hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+140, level=80]
    $ dissolve_fx("id(140)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # キュルケ：ねえ、ルイズ。
    voice "ch27_k_040"
    k "Hey, Louise. I don't know what spell you're chanting, but are you done yet?{#ch27_k_040}"

    # ルイズ：……。
    l "…{#ch27_l_067}"

    # キュルケ：……って、詠唱中には答えられないわよね。
    voice "ch27_k_041"
    k "…I can't answer while chanting, can I? But something's coming into view at the edge of the sky…{#ch27_k_041}"

    # キュルケ：きっと、あれがレコン・キスタの空中艦隊
    voice "ch27_k_042"
    k "That must be the Reconquista air fleet, I suppose…{#ch27_k_042}"

    # キュルケ：でもってあの中から、搭載されてる
    voice "ch27_k_043"
    k "And from it, countless dragon riders will pour out—and cover this Tristain sky completely.{#ch27_k_043}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # アキナ：くそぉ……。
    voice "ch27_ak_008"
    ak "Damn… Losing to these guys…{#ch27_ak_008}"

    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：でも、待ってな。
    voice "ch27_ak_009"
    ak "But wait. Right now, this city will be surrounded by Reconquista's forces!{#ch27_ak_009}"

    # [SPRITE   lay21    hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch27_t_042}"

    # サイト：ルイズ、まだか……？  [voice 12825]
    voice "ch27_s_128"
    s "Louise—are you done yet?{#ch27_s_128}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+140, level=80]
    $ dissolve_fx("id(140)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # ルイズ：……！！  [voice 6966]
    voice "ch27_l_068"
    l "…!!{#ch27_l_068}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+141, level=80]
    $ dissolve_fx("id(141)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # キュルケ：えっ、ええーっ！？
    voice "ch27_k_044"
    k "Eh? Ehh!? What's happening!?{#ch27_k_044}"

    # キュルケ：なっ、何これ？
    voice "ch27_k_045"
    k "Wha—what's this? The sky's filled with countless battleships!?{#ch27_k_045}"

    # キュルケ：ル、ルイズ……？
    voice "ch27_k_046"
    k "L-Louise…? What did you do!?{#ch27_k_046}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay21    hide]
    # [SPRITE   lay19    x=304, y=416]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [EVENT_CG event    hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # アキナ：なっ、なんだっ！？
    voice "ch27_ak_010"
    ak "Wha—what!? What did you people do!?{#ch27_ak_010}"

    # サイト：何って……。
    voice "ch27_s_129"
    s "What do you mean, what? Don't you see? It's as you see.{#ch27_s_129}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：見ての通りだって？
    voice "ch27_ak_011"
    ak "As I see it… Surely not—that many reinforcements…{#ch27_ak_011}"

    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：あのルイズが召喚したっていうのかっ！？  [voice 164]
    voice "ch27_ak_012"
    ak "You mean that Louise summoned them!?{#ch27_ak_012}"

    # [SPRITE   lay5     image=+403, level=160, dir=1B]
    # サイト：どうだ？
    voice "ch27_s_130"
    s "Well? Isn't Louise's magic amazing?{#ch27_s_130}"

    # サイト：なんたって、ルイズは……。
    voice "ch27_s_131"
    s "After all—Louise is… my mistress!{#ch27_s_131}"

    # [SPRITE   lay5     level=157]
    # [SPRITE   lay21    level=153]
    # [SPRITE   lay19    image=+942, level=152, dir=1A]
    # デルフリンガー：ああ、あの貴族の娘っ子は伝説だもんな。
    voice "ch27_d_002"
    d "Ah, that noble girl is a legend, isn't she? Just like me and my partner here.{#ch27_d_002}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay21    hide]
    # [LAYER    lay0     image=+594, level=155, dir=1A]
    # タバサ：伝説……？  [voice 15763]
    voice "ch27_t_043"
    t "Legend…?{#ch27_t_043}"

    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+405, level=157, dir=1B]
    # サイト：よーし、捕まえた。
    voice "ch27_s_132"
    s "All right—caught her. Really made me work for it.{#ch27_s_132}"

    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+594, level=155, dir=1A]
    # タバサ：……。
    t "…{#ch27_t_044}"

    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # サイト：タバサ……。  [voice 12830]
    voice "ch27_s_133"
    s "Tabitha…{#ch27_s_133}"

    menu:
        "Don't hand her to Gallia{#ch27_3_c_994_1}":
            jump ch27_3_scene_995
        "Leave it to Tabitha{#ch27_3_c_994_2}":
            jump ch27_3_scene_996
        "Haruna is innocent, but…{#ch27_3_c_994_3}":
            jump ch27_3_scene_997

label ch27_3_scene_995:

    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # [LAYER    lay0     image=+594, level=155, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [SPRITE   lay5     image=+440, level=157, dir=2B]
    # サイト：ガリア王国には引き渡さないでくれないか。  [voice 12831]
    voice "ch27_s_134"
    s "Please—don't hand her over to Gallia.{#ch27_s_134}"

    # [LAYER    lay0     image=+594, level=155, dir=1A]
    # タバサ：……。
    t "…{#ch27_t_045}"

    # サイト：でも、引き渡さないと、タバサもいろいろと、
    voice "ch27_s_135"
    s "But if you don't hand her over, things will get difficult for you too, won't they?{#ch27_s_135}"

    # タバサ：うん。  [voice 15764]
    voice "ch27_t_046"
    t "Mm.{#ch27_t_046}"

    # サイト：どうしたもんかなぁ？  [voice 12833]
    voice "ch27_s_136"
    s "What should we do…{#ch27_s_136}"

    # サイト：きっと、春奈じゃなくてアキナがやらかした
    voice "ch27_s_137"
    s "Surely the problem is what Akina did, not Haruna…{#ch27_s_137}"

    # [LAYER    lay0     image=+588, level=155, dir=1A]
    # タバサ：あっ。  [voice 15765]
    voice "ch27_t_047"
    t "Ah.{#ch27_t_047}"

    # → next scene 998
    jump ch27_3_scene_998

label ch27_3_scene_996:

    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # [LAYER    lay0     image=+594, level=155, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [SPRITE   lay5     image=+401, level=157, dir=1B]
    # サイト：……タバサの判断に任せるよ。  [voice 12836]
    voice "ch27_s_138"
    s "…I'll leave it to Tabitha's judgment.{#ch27_s_138}"

    # [LAYER    lay0     image=+588, level=155, dir=1A]
    # タバサ：いいの？  [voice 15766]
    voice "ch27_t_048"
    t "Is that all right?{#ch27_t_048}"

    # サイト：タバサにはタバサの事情があるんだろ？  [voice 12835]
    voice "ch27_s_139"
    s "Tabitha has her own circumstances, doesn't she?{#ch27_s_139}"

    # [LAYER    lay0     image=+594, level=155, dir=1A]
    # タバサ：うん……。  [voice 15767]
    voice "ch27_t_049"
    t "…Mm.{#ch27_t_049}"

    # [SPRITE   lay5     image=+440, level=157, dir=2B]
    # サイト：それにしても、春奈も気の毒だよな。
    voice "ch27_s_140"
    s "Even so—poor Haruna. To end up like this because of a separate personality…{#ch27_s_140}"

    # [LAYER    lay0     image=+588, level=155, dir=1A]
    # タバサ：別人格……。
    voice "ch27_t_050"
    t "Separate personality… Separate…{#ch27_t_050}"

    # → next scene 998
    jump ch27_3_scene_998

label ch27_3_scene_997:

    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # [LAYER    lay0     image=+594, level=155, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [SPRITE   lay5     image=+440, level=157, dir=2B]
    # サイト：春奈には罪はないけど、アキナにはな……。  [voice 12838]
    voice "ch27_s_141"
    s "Haruna is innocent, but Akina isn't…{#ch27_s_141}"

    # サイト：うーん……。
    voice "ch27_s_142"
    s "Hmm… I suppose she has the guilt of being the bomber, doesn't she?{#ch27_s_142}"

    # [LAYER    lay0     image=+588, level=155, dir=1A]
    # タバサ：そう、アキナには……。
    voice "ch27_t_051"
    t "Yes—Akina… Ah.{#ch27_t_051}"

    # → next scene 998
    jump ch27_3_scene_998

label ch27_3_scene_998:

    # [SPRITE   lay5     image=+440, level=157, dir=2B]
    # [LAYER    lay0     image=+588, level=155, dir=1A]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # [BG       stage    image=+61, level=200]
    $ fade_fx("id(61)")
    # [SPRITE   lay5     image=+434, level=157, dir=2B]
    # サイト：ん？
    voice "ch27_s_143"
    s "Hmm? What's wrong?{#ch27_s_143}"

    # [LAYER    lay0     image=+588, level=155, dir=1A]
    # タバサ：なんでもない。  [voice 15770]
    voice "ch27_t_052"
    t "It's nothing.{#ch27_t_052}"

    # [SPRITE   lay5     image=+440, level=157, dir=2B]
    # サイト：で、タバサ自身は、春奈のこと、
    voice "ch27_s_144"
    s "So—what do you intend to do with Haruna yourself, Tabitha?{#ch27_s_144}"

    # タバサ：決めた。  [voice 15771]
    voice "ch27_t_053"
    t "I've decided.{#ch27_t_053}"

    # [SPRITE   lay5     image=+407, level=157, dir=1B]
    # サイト：えっ、今か！？  [voice 12842]
    voice "ch27_s_145"
    s "Eh, now!?{#ch27_s_145}"

    # タバサ：うん、今。  [voice 15772]
    voice "ch27_t_054"
    t "Mm. Now.{#ch27_t_054}"

    # サイト：（春奈のこと……。
    s "(Haruna… What are you planning to do…?){#ch27_s_146}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=4000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # → next scene 1008
    jump ch28

    # ==== КОНЕЦ ГЛАВЫ 27 ====
    jump ch28
    return

