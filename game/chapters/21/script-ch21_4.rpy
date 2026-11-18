# Глава 21, часть 4 (extra 1493–1512): разведка перед боем, мини-свидания.
# Источник: ps2_source/chapters/chapter_22_サイトのメイド.txt (extra scenes).

label ch21_4:
    $ tndl(None)
    $ show_sprites()

label ch21_4_scene_1493:

    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：（タバサってどんな料理を
    s "(I wonder what Tabitha's planning to cook…){#ch21_s_168}"

    # [SE       se0      play=+82]
    # タバサ：誰？  [voice 15471]
    voice "ch21_t_052"
    t "Who is it?{#ch21_t_052}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：俺だよ、タバサ。
    voice "ch21_s_169"
    s "It's me, Tabitha. Mind if I come in?{#ch21_s_169}"

    # タバサ：入って。  [voice 15472]
    voice "ch21_t_053"
    t "Come in.{#ch21_t_053}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：お邪魔しますっ。  [voice 9983]
    voice "ch21_s_170"
    s "Sorry to intrude.{#ch21_s_170}"

    # [SE       se0      play=+57]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [TRANS trans("crossfade", 1000)]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SE       se0      play=+56]
    # タバサ：偵察に来たのなら、無駄。  [voice 15473]
    voice "ch21_t_054"
    t "If you're here to scout, don't bother.{#ch21_t_054}"

    # [LAYER    lay0     x=-96, y=0]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：あ、ばれた？  [voice 9984]
    voice "ch21_s_171"
    s "Ah, I'm found out?{#ch21_s_171}"

    # [SE       se0      play=+72]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：今読んでるその本って、
    voice "ch21_s_172"
    s "That book you're reading—is it by any chance about cooking?{#ch21_s_172}"

    # タバサ：秘密。  [voice 15474]
    voice "ch21_t_055"
    t "Secret.{#ch21_t_055}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：どうしても？  [voice 9986]
    voice "ch21_s_173"
    s "You won't tell me?{#ch21_s_173}"

    # タバサ：だめ。  [voice 15475]
    voice "ch21_t_056"
    t "No.{#ch21_t_056}"

    # サイト：（さすが、タバサだ。
    s "(As expected of Tabitha. Her defenses are impenetrable. Now, what to do?){#ch21_s_174}"

    menu:
        "Tease her{#ch21_4_c_1493_1}":
            jump ch21_4_scene_1494
        "Peek{#ch21_4_c_1493_2}":
            jump ch21_4_scene_1495
        "Sulk{#ch21_4_c_1493_3}":
            jump ch21_4_scene_1496

label ch21_4_scene_1494:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：（よし、ここは作戦を変えよう。
    s "(All right, time to change tactics. I'll tease her.){#ch21_s_175}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：俺はぜんぜん見たくないなぁ～。  [voice 9987]
    voice "ch21_s_176"
    s "I don't want to see it at all~.{#ch21_s_176}"

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SE       se0      play=+72]
    # タバサ：……。
    t "…{#ch21_t_057}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：見たくないよー。  [voice 9988]
    voice "ch21_s_177"
    s "I don't want to see it, really.{#ch21_s_177}"

    # [SE       se0      play=+72]
    # タバサ：……。
    t "…{#ch21_t_058}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：ってことで、見せて。  [voice 9989]
    voice "ch21_s_178"
    s "So, show me.{#ch21_s_178}"

    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # タバサ：駄目。  [voice 15476]
    voice "ch21_t_059"
    t "No.{#ch21_t_059}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：しくしくしく……。  [voice 9990]
    voice "ch21_s_179"
    s "Sniff sniff…{#ch21_s_179}"

    # → next scene 1497
    jump ch21_4_scene_1497

label ch21_4_scene_1495:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：（こうなりゃ強行突破だ。
    s "(If that's how it is, I'll go with force. I'll make her show me!){#ch21_s_180}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # [LAYER    lay0     level=156]
    # サイト：おりゃ。  [voice 9991]
    voice "ch21_s_181"
    s "Hiyah!{#ch21_s_181}"

    # [LAYER    lay0     image=+621, level=156, dir=2A]
    # タバサ：ひょい。  [voice 15477]
    voice "ch21_t_060"
    t "Whoops.{#ch21_t_060}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [LAYER    lay0     level=156]
    # サイト：こなくそ！！  [voice 9992]
    voice "ch21_s_182"
    s "You little—!!{#ch21_s_182}"

    # [LAYER    lay0     image=+588, level=156, dir=1A]
    # タバサ：ひょい。  [voice 15478]
    voice "ch21_t_061"
    t "Whoops.{#ch21_t_061}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：しくしくしく……。  [voice 9993]
    voice "ch21_s_183"
    s "Sniff sniff…{#ch21_s_183}"

    # → next scene 1497
    jump ch21_4_scene_1497

label ch21_4_scene_1496:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ふん、どうせ俺なんて……。  [voice 9994]
    voice "ch21_s_184"
    s "Hmph, I suppose I'm just not good enough…{#ch21_s_184}"

    # サイト：いじいじいじいじ……。  [voice 9995]
    voice "ch21_s_185"
    s "Sulk, sulk, sulk…{#ch21_s_185}"

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SE       se0      play=+72]
    # タバサ：……。
    t "…{#ch21_t_062}"

    # サイト：いじいじいじいじ……。  [voice 9996]
    voice "ch21_s_186"
    s "Sulk, sulk, sulk…{#ch21_s_186}"

    # [SE       se0      play=+72]
    # タバサ：……。
    t "…{#ch21_t_063}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：ってことで、見せて。  [voice 9997]
    voice "ch21_s_187"
    s "So, show me.{#ch21_s_187}"

    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # タバサ：駄目。  [voice 15479]
    voice "ch21_t_064"
    t "No.{#ch21_t_064}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：しくしくしく……。  [voice 9998]
    voice "ch21_s_188"
    s "Sniff sniff…{#ch21_s_188}"

    # → next scene 1497
    jump ch21_4_scene_1497

label ch21_4_scene_1497:

    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+94, level=200]
    $ fade_fx("id(94)")
    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # タバサ：レビテーション。  [voice 15480]
    voice "ch21_t_065"
    t "Levitation.{#ch21_t_065}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：わわわっ！？
    voice "ch21_s_189"
    s "Whoa!? I'm floating!{#ch21_s_189}"

    # タバサ：お願い。  [voice 15481]
    voice "ch21_t_066"
    t "Please.{#ch21_t_066}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # サイト：廊下に連れ出されるー。  [voice 10000]
    voice "ch21_s_190"
    s "I'm being dragged into the hallway—!{#ch21_s_190}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+14, level=200]
    $ fade_fx("id(14)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（そこまで秘密にしなきゃだめなものって
    s "(What on earth could be so secret that she'd go this far?){#ch21_s_191}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
label ch21_4_scene_1498:

    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：あれ、キュルケじゃないか。
    voice "ch21_s_192"
    s "Oh, it's Kirche. What are you doing?{#ch21_s_192}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あ～ら、サイトじゃない。
    voice "ch21_k_029"
    k "A~h, it's Saito. Heh heh, curious?{#ch21_k_029}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：まあ、少しは。
    voice "ch21_s_193"
    s "Well, a little. What were you looking at so intently?{#ch21_s_193}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：やだっ、ちょっとサイトったらぁ。
    voice "ch21_k_030"
    k "No, Saito, seriously—stop peeking!{#ch21_k_030}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なんだ、ただの草じゃん。
    voice "ch21_s_194"
    s "What's this, just grass. Why is the shelf full of grass?{#ch21_s_194}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ただの草じゃないわ。
    voice "ch21_k_031"
    k "It's not just grass. These are medicinal herbs Mr. Colbert is growing.{#ch21_k_031}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：へぇ～。
    voice "ch21_s_195"
    s "Huh~. So what are you going to do with them?{#ch21_s_195}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：ナイショ。  [voice 3012]
    voice "ch21_k_032"
    k "It's a secret.{#ch21_k_032}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：はぁ。
    voice "ch21_s_196"
    s "Haah. I see.{#ch21_s_196}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：……ねぇ、ダーリン？
    voice "ch21_k_033"
    k "…Hey, darling? If I come first in the cooking contest, will you go on a date with me?{#ch21_k_033}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：デートぉ！？  [voice 10006]
    voice "ch21_s_197"
    s "A date!?{#ch21_s_197}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：約束してくれるなら、
    voice "ch21_k_034"
    k "If you promise, I might tell you.{#ch21_k_034}"

    menu:
        "Gladly!{#ch21_4_c_1498_1}":
            jump ch21_4_scene_1499
        "That's a little…{#ch21_4_c_1498_2}":
            jump ch21_4_scene_1500
        "That aside…{#ch21_4_c_1498_3}":
            jump ch21_4_scene_1501

label ch21_4_scene_1499:

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay5     image=+431, level=160, dir=2A]
    # サイト：よ、喜んで。  [voice 10007]
    voice "ch21_s_198"
    s "Y-Yes, gladly.{#ch21_s_198}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+119, level=80]
    $ dissolve_fx("id(119)")
    # [BGM      bgm      play=+14]
    play music t13 fadein 1.0
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [SPRITE   lay6     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay6     reset]
    # キュルケ：ほんと！？
    voice "ch21_k_035"
    k "Really!? Heh heh! I'm so happy!{#ch21_k_035}"

    # サイト：がふっ！
    voice "ch21_s_199"
    s "Guh! Kirche, it's fine to hug me, but I can't—can't breathe!{#ch21_s_199}"

    # キュルケ：あら、ごめんなさい。  [voice 3016]
    voice "ch21_k_036"
    k "Oh, sorry.{#ch21_k_036}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：うふふ、でも、そうと決まったら
    voice "ch21_k_037"
    k "Heh heh, but now that it's decided, I'll do my best!{#ch21_k_037}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # → next scene 1502
    jump ch21_4_scene_1502

label ch21_4_scene_1500:

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そ、それはちょっと……。  [voice 10009]
    voice "ch21_s_200"
    s "T-That's a little…{#ch21_s_200}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：だめなの？  [voice 3018]
    voice "ch21_k_038"
    k "Is it no good?{#ch21_k_038}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：ほ、ほら、ルイズがどこで見てるか、
    voice "ch21_s_201"
    s "W-Well, Louise could be watching from anywhere, you know!{#ch21_s_201}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：大丈夫よ、あたしが一番になったら、
    voice "ch21_k_039"
    k "It's fine. If I come first, even Louise won't have anything to say. So—a date.{#ch21_k_039}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：ね、ね、ね！  [voice 3020]
    voice "ch21_k_040"
    k "Come on, come on, come on!{#ch21_k_040}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：わ、分かりました。  [voice 10011]
    voice "ch21_s_202"
    s "O-Okay, I understand.{#ch21_s_202}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：うふっ！
    voice "ch21_k_041"
    k "Heh heh! I'm so happy!{#ch21_k_041}"

    # → next scene 1502
    jump ch21_4_scene_1502

label ch21_4_scene_1501:

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：それはそれとして、キュルケはどんな料理を
    voice "ch21_s_203"
    s "That aside, Kirche—what dish are you planning to make?{#ch21_s_203}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あら、うまくごまかしたつもり？  [voice 3022]
    voice "ch21_k_042"
    k "Oh? Trying to change the subject, are we?{#ch21_k_042}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：あう。  [voice 10013]
    voice "ch21_s_204"
    s "Ouch.{#ch21_s_204}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：でもいいわ、許してあげる。  [voice 3023]
    voice "ch21_k_043"
    k "Fine. I'll forgive you.{#ch21_k_043}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：じゃ、どんな料理を？  [voice 10014]
    voice "ch21_s_205"
    s "So, what dish?{#ch21_s_205}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ナイショ。  [voice 3024]
    voice "ch21_k_044"
    k "It's a secret.{#ch21_k_044}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：さいですか。  [voice 10015]
    voice "ch21_s_206"
    s "I see.{#ch21_s_206}"

    # → next scene 1502
    jump ch21_4_scene_1502

label ch21_4_scene_1502:

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+14]
    play music t13 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：じゃあ、当日楽しみにしててね。
    voice "ch21_k_045"
    k "Well then, look forward to it on the day. I'll make something special for darling!{#ch21_k_045}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：あ、ああ。
    voice "ch21_s_207"
    s "A-Ah. Well then.{#ch21_s_207}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（高まる期待と不安……。
    s "(Growing anticipation and anxiety… Will I be all right…){#ch21_s_208}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：（って、薬草のこと聞けてねー！）
    s "(Wait—I never found out about the herbs!){#ch21_s_209}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
label ch21_4_scene_1503:

    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [SE       se0      play=+57]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：むぅ。  [voice 5001]
    voice "ch21_l_064"
    l "Muu.{#ch21_l_064}"

    # サイト：（うわあ……。
    s "(Whoa… Louise is in a bad mood.){#ch21_s_210}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：サイトっ！！
    voice "ch21_l_065"
    l "Saito!! I'll hear your request. Right now, name the dish you want!{#ch21_l_065}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：好きな食べ物って言われてもなぁ……。  [voice 10017]
    voice "ch21_s_211"
    s "Even if you ask what my favorite food is…{#ch21_s_211}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：もう、ぐずぐずしないでよね。
    voice "ch21_l_066"
    l "Come on, don't dawdle. We'll run out of time for practice, won't we?{#ch21_l_066}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（って言われても……。
    s "(Easy for you to say… A Japanese dish wouldn't make sense to you…){#ch21_s_212}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：し、シチュー……かな。
    voice "ch21_s_213"
    s "S-Stew, I guess… Mom used to make it a lot.{#ch21_s_213}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：シチューね……。
    voice "ch21_l_067"
    l "Stew, huh… Hmm…{#ch21_l_067}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そ、その反応は……。  [voice 10019]
    voice "ch21_s_214"
    s "T-That reaction…{#ch21_s_214}"

    menu:
        "Very confident?{#ch21_4_c_1503_1}":
            jump ch21_4_scene_1504
        "Never made it?{#ch21_4_c_1503_2}":
            jump ch21_4_scene_1505
        "Don't know stew?{#ch21_4_c_1503_3}":
            jump ch21_4_scene_1506

label ch21_4_scene_1504:

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：もしや、とても自信がある料理だったり！？
    voice "ch21_s_215"
    s "Could it be you're really confident in it!? Like, 'I'm particular about the cream!' or something!?{#ch21_s_215}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：そっ、そこまででもないけどっ！
    voice "ch21_l_068"
    l "N-Not that much! B-But, well, yes, it is one of my, um, specialties!{#ch21_l_068}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（ウソだな……）
    s "(That's a lie…){#ch21_s_216}"

    # → next scene 1507
    jump ch21_4_scene_1507

label ch21_4_scene_1505:

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：シチュー作ったことないとか？  [voice 10021]
    voice "ch21_s_217"
    s "You've never made stew before?{#ch21_s_217}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：な、な、ないはずないでしょ！
    voice "ch21_l_069"
    l "O-Of course I have! I'm practically a chef! You'd be surprised, and I don't care!{#ch21_l_069}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（絶対ウソだな……）
    s "(That's definitely a lie…){#ch21_s_218}"

    # → next scene 1507
    jump ch21_4_scene_1507

label ch21_4_scene_1506:

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：シチュー知らないとか？  [voice 10022]
    voice "ch21_s_219"
    s "You don't know what stew is?{#ch21_s_219}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：知ってるわよ！
    voice "ch21_l_070"
    l "I know! How rude!{#ch21_l_070}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：シチューと言ったらこのわたし。
    voice "ch21_l_071"
    l "If we're talking stew, I'm the one. If you mention me, you mention stew—that's how well I know it!{#ch21_l_071}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（絶対ありえねー）
    s "(That's impossible…){#ch21_s_220}"

    # → next scene 1507
    jump ch21_4_scene_1507

label ch21_4_scene_1507:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # [BGM      bgm      play=+6]
    play music t5 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ご主人様に質問です。  [voice 10023]
    voice "ch21_s_221"
    s "A question for my mistress.{#ch21_s_221}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：なによ。
    voice "ch21_l_072"
    l "What is it? I'll allow you to ask, just this once.{#ch21_l_072}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：シチュー云々の前に、料理したことあるの？  [voice 10024]
    voice "ch21_s_222"
    s "Before we talk about stew—have you ever cooked anything?{#ch21_s_222}"

    # ルイズ：……。  [voice 5010]
    voice "ch21_l_073"
    l "…{#ch21_l_073}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：……。
    s "…{#ch21_s_223}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：か、簡単よ。
    voice "ch21_l_074"
    l "I-It's easy. You just follow the book—put the cut ingredients and seasonings in a pot, right?{#ch21_l_074}"

    # サイト：（頑張れ、俺。
    s "(Hang in there, me. I can do it if I try. I will definitely survive this.){#ch21_s_224}"

    # [SPRITE   lay1     image=+343, level=160, dir=2A]
    # ルイズ：何よ！
    voice "ch21_l_075"
    l "What! Simply being able to eat the food my familiar makes should be thanks enough!{#ch21_l_075}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SE       se0      play=+57]
    # [SE       se0      play=+58]
    # サイト：うわ、部屋を出て行っちゃったよ。
    voice "ch21_s_225"
    s "Whoa, she left the room… What's going to become of me…{#ch21_s_225}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
label ch21_4_scene_1508:

    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # サイト：（あれ、春奈とモンモン？
    s "(Huh, Haruna and Montmorency? An unusual pair.){#ch21_s_226}"

    # モンモランシー：あら、サイトじゃない。
    voice "ch21_m_011"
    m "Oh, it's Saito. Louise isn't here, you know.{#ch21_m_011}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：散歩だよ、散歩。
    voice "ch21_s_227"
    s "Just a walk, a walk. By the way, what were you two talking about?{#ch21_s_227}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：料理対決の事で相談に乗ってもらってたのよ。
    voice "ch21_ha_014"
    ha "They were asking my advice about the cooking contest. I was thinking of trying a local dish from this world.{#ch21_ha_014}"

    # サイト：郷土料理か……。  [voice 10027]
    voice "ch21_s_228"
    s "Local cuisine, huh…{#ch21_s_228}"

    menu:
        "Charcoal-grilled frog?{#ch21_4_c_1508_1}":
            jump ch21_4_scene_1509
        "Salamander tongue?{#ch21_4_c_1508_2}":
            jump ch21_4_scene_1510
        "Never heard of it{#ch21_4_c_1508_3}":
            jump ch21_4_scene_1511

label ch21_4_scene_1509:

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：カエルの黒焼きとか……？  [voice 10028]
    voice "ch21_s_229"
    s "Charcoal-grilled frog, perhaps…?{#ch21_s_229}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # モンモランシー：そんなもの食べないわよっ！  [voice 4002]
    voice "ch21_m_012"
    m "We don't eat such things!{#ch21_m_012}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：だ、だよな。  [voice 10029]
    voice "ch21_s_230"
    s "R-Right I thought so.{#ch21_s_230}"

    # → next scene 1512
    jump ch21_4_scene_1512

label ch21_4_scene_1510:

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：サラマンダーのタン……とか？  [voice 10030]
    voice "ch21_s_231"
    s "Salamander tongue… perhaps?{#ch21_s_231}"

    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：サラマンダーって、あのキュルケさんの
    voice "ch21_ha_015"
    ha "Salamander—that's Kirche's familiar, isn't it? Hiraga-kun, stop joking.{#ch21_ha_015}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：ははは、悪い悪い。
    voice "ch21_s_232"
    s "Ha ha, sorry, sorry. Of course nobody would eat that.{#ch21_s_232}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # モンモランシー：あら、食べるわよ？  [voice 4003]
    voice "ch21_m_013"
    m "Oh, but they do.{#ch21_m_013}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：え。  [voice 10032]
    voice "ch21_s_233"
    s "Eh?{#ch21_s_233}"

    # [SPRITE   lay3     image=+885, level=160, dir=2A]
    # モンモランシー：美食家の間で珍重されてるわ。
    voice "ch21_m_014"
    m "It's prized among gourmets. Since only a small amount can be harvested, it's traded at a high price.{#ch21_m_014}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そうか……。
    voice "ch21_s_234"
    s "I see… Kirche will look at Flame differently from now on.{#ch21_s_234}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：平賀くん、だめだよ？
    voice "ch21_ha_016"
    ha "Hiraga-kun, don't! It's cruel.{#ch21_ha_016}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：わ、分かってるって。  [voice 10034]
    voice "ch21_s_235"
    s "I-I know, I know.{#ch21_s_235}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # → next scene 1512
    jump ch21_4_scene_1512

label ch21_4_scene_1511:

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：聞いたことないな。
    voice "ch21_s_236"
    s "I've never heard of it. There's no such thing, is there?{#ch21_s_236}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # モンモランシー：あら、あるわよ。
    voice "ch21_m_015"
    m "Oh, it exists. How rude.{#ch21_m_015}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：たとえばどんなものが？  [voice 1959]
    voice "ch21_ha_017"
    ha "For example, what kind?{#ch21_ha_017}"

    # [SPRITE   lay3     image=+885, level=160, dir=2A]
    # モンモランシー：そうね……。
    voice "ch21_m_016"
    m "Hmm… It might be a dish unique to our lands, it's so rare.{#ch21_m_016}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：おお、なんか期待できそう！  [voice 10036]
    voice "ch21_s_237"
    s "Oh, this sounds promising!{#ch21_s_237}"

    # [SPRITE   lay3     image=+854, level=160, dir=1A]
    # モンモランシー：鍋でチーズを溶かして、
    voice "ch21_m_017"
    m "You melt cheese in a pot and eat it by dipping skewers of bread into it. Rare, isn't it?{#ch21_m_017}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：チーズフォンデュですか。  [voice 10037]
    voice "ch21_s_238"
    s "Fondue?{#ch21_s_238}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：こっちの世界にもあったのね……。  [voice 1960]
    voice "ch21_ha_018"
    ha "So it existed in this world, too…{#ch21_ha_018}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # → next scene 1512
    jump ch21_4_scene_1512

label ch21_4_scene_1512:

    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [BGM      bgm      play=+11]
    play music t10 fadein 1.0
    # [BG       stage    image=+26, level=200]
    $ fade_fx("id(26)")
    # [SPRITE   lay3     image=+858, level=160, dir=1A]
    # モンモランシー：でも、わたしの家ではすべて給仕が
    voice "ch21_m_018"
    m "But in my house, all the servants handle everything. Even if you call it commoners' local food, it means nothing to me.{#ch21_m_018}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：だめじゃん。  [voice 10038]
    voice "ch21_s_239"
    s "That's no good.{#ch21_s_239}"

    # [SPRITE   lay3     image=+856, level=160, dir=1A]
    # モンモランシー：なによ、悪かったわね。
    voice "ch21_m_019"
    m "What! How rude! If you say that, I'll teach Haruna an amazing dish instead!{#ch21_m_019}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：な、なんだよそれ。  [voice 10039]
    voice "ch21_s_240"
    s "W-What was that?{#ch21_s_240}"

    # [SPRITE   lay3     image=+887, level=160, dir=2A]
    # モンモランシー：ふふっ、それじゃハルナ行くわよ。  [voice 4010]
    voice "ch21_m_020"
    m "Heh heh, well then, Haruna, let's go.{#ch21_m_020}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：それじゃあ平賀くんっ。
    voice "ch21_ha_019"
    ha "Well then, Hiraga-kun. Please look forward to my cooking, too!{#ch21_ha_019}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ああ、楽しみにしてるよ。  [voice 10040]
    voice "ch21_s_241"
    s "Ah, I'm looking forward to it.{#ch21_s_241}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（春奈……。
    s "(Haruna… What are they going to teach you…){#ch21_s_242}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ГЛАВЫ 21 ====
    jump ch22
    return

