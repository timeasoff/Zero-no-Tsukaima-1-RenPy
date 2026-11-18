# Глава 26, часть 5 (extra 1219–1223): клятва на мизинцах с Табасой.
# Источник: ps2_source/chapters/chapter_27_タバサの秘密.txt (extra 1219-1223).

label ch26_5:
    $ tndl(None)
    $ show_sprites()

label ch26_5_scene_1219:

    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # サイト：あ、タバサがいる。
    voice "ch26_s_198"
    s "Ah, there's Tabitha. She seems well enough to go outside. Good.{#ch26_s_198}"

    # サイト：でも、どうしたんだろ？
    voice "ch26_s_199"
    s "But what's wrong? She keeps looking down… Now I'm curious…{#ch26_s_199}"

    # サイト：おーい、タバサー。  [voice 9019]
    voice "ch26_s_200"
    s "Hey there, Tabitha~.{#ch26_s_200}"

    # [LAYER    lay0     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch26_t_058}"

    # サイト：どうしたんだ？
    voice "ch26_s_201"
    s "What's wrong? Going for a walk? You shouldn't overdo it yet, should you?{#ch26_s_201}"

    # タバサ：うん。  [voice 15385]
    voice "ch26_t_059"
    t "Mm.{#ch26_t_059}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ずっとうつむいたりなんかして？  [voice 9021]
    voice "ch26_s_202"
    s "You keep looking down like that?{#ch26_s_202}"

    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+627, level=160, dir=2A]
    # タバサ：考えごと。  [voice 15386]
    voice "ch26_t_060"
    t "Thinking.{#ch26_t_060}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：えっ、考えごと？
    voice "ch26_s_203"
    s "Eh, thinking? Could it be…{#ch26_s_203}"

    menu:
        "About me?{#ch26_5_c_1219_1}":
            jump ch26_5_scene_1220
        "About shielding you?{#ch26_5_c_1219_2}":
            jump ch26_5_scene_1221
        "About Haruna?{#ch26_5_c_1219_3}":
            jump ch26_5_scene_1222

label ch26_5_scene_1220:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+627, level=160, dir=2A]
    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # サイト：俺のこととか？  [voice 9023]
    voice "ch26_s_204"
    s "About me, perhaps?{#ch26_s_204}"

    # [LAYER    lay0     image=+629, level=160, dir=2A]
    # タバサ：ちょっとだけ合ってる。  [voice 15387]
    voice "ch26_t_061"
    t "A little close.{#ch26_t_061}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：なんだ、ちょっとだけかぁ。
    voice "ch26_s_205"
    s "What do you mean, 'a little'? So what exactly…?{#ch26_s_205}"

    # タバサ：どうしてかばったのかって。  [voice 15388]
    voice "ch26_t_062"
    t "Why I shielded you.{#ch26_t_062}"

    # → next scene 1223
    jump ch26_5_scene_1223

label ch26_5_scene_1221:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+627, level=160, dir=2A]
    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # サイト：俺をかばっちゃったこと？  [voice 9025]
    voice "ch26_s_206"
    s "About how I shielded you?{#ch26_s_206}"

    # [LAYER    lay0     image=+629, level=160, dir=2A]
    # タバサ：うん。  [voice 15389]
    voice "ch26_t_063"
    t "Mm.{#ch26_t_063}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：えーっと……。
    voice "ch26_s_207"
    s "Um… You mean you wish you hadn't?{#ch26_s_207}"

    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # タバサ：そうじゃない。
    voice "ch26_t_064"
    t "No. I thought I should.{#ch26_t_064}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：ハハハ、ハハ……。  [voice 9027]
    voice "ch26_s_208"
    s "Ha ha, ha ha…{#ch26_s_208}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（ちょっと複雑な気分……）
    s "(A complicated feeling…){#ch26_s_209}"

    # タバサ：でも……。  [voice 15391]
    voice "ch26_t_065"
    t "But…{#ch26_t_065}"

    # → next scene 1223
    jump ch26_5_scene_1223

label ch26_5_scene_1222:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+627, level=160, dir=2A]
    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # サイト：春奈のこととか？  [voice 9028]
    voice "ch26_s_210"
    s "About Haruna, perhaps?{#ch26_s_210}"

    # [LAYER    lay0     image=+621, level=160, dir=2A]
    # タバサ：部分的には合ってる。
    voice "ch26_t_066"
    t "Partly right. But not quite.{#ch26_t_066}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：なんだ、違うのか。  [voice 9029]
    voice "ch26_s_211"
    s "What, not quite?{#ch26_s_211}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：じゃあ、何を考えたんだ？  [voice 9030]
    voice "ch26_s_212"
    s "Then what were you thinking about?{#ch26_s_212}"

    # タバサ：あの時、どうしてかばったのかって。  [voice 15393]
    voice "ch26_t_067"
    t "Why I shielded you then.{#ch26_t_067}"

    # → next scene 1223
    jump ch26_5_scene_1223

label ch26_5_scene_1223:

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [LAYER    lay0     image=+629, level=160, dir=2A]
    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：今思えば……。
    voice "ch26_t_068"
    t "Looking back… I could have handled it with magic.{#ch26_t_068}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：た、たしかにそうだったかも……。  [voice 9031]
    voice "ch26_s_213"
    s "T-That's true, maybe…{#ch26_s_213}"

    # タバサ：失敗。  [voice 15395]
    voice "ch26_t_069"
    t "Failure.{#ch26_t_069}"

    # サイト：んー、要は冷静になる前に
    voice "ch26_s_214"
    s "Hmm—so you mean your body moved before you could calm down, basically?{#ch26_s_214}"

    # タバサ：そうみたい。
    voice "ch26_t_070"
    t "Looks like it. I wonder why that happened.{#ch26_t_070}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：ハハハ……。
    voice "ch26_s_215"
    s "Ha ha ha… Well then, if something like that happens again, you can just let me get hit, okay?{#ch26_s_215}"

    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：駄目。
    voice "ch26_t_071"
    t "No. I'm sure I won't be able to ignore it…{#ch26_t_071}"

    # サイト：大丈夫だって。
    voice "ch26_s_216"
    s "It's fine. I'm used to getting hurt.{#ch26_s_216}"

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch26_t_072}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：あ、信用してないだろ？
    voice "ch26_s_217"
    s "Ah—you don't believe me, do you? I'm tougher than Tabitha thinks!{#ch26_s_217}"

    # サイト：（いつもルイズにおしおきされてるしな……）
    s "(I do get punished by Louise all the time, after all…){#ch26_s_218}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：だからさ、あんなことになったら、
    voice "ch26_s_219"
    s "So—if that happens again, just fight without worrying about me, all right?{#ch26_s_219}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch26_t_073}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：そんな顔しないでくれよー。
    voice "ch26_s_220"
    s "Don't make that face. I was more upset that you got burned than that I was safe.{#ch26_s_220}"

    # [LAYER    lay0     image=+596, level=160, dir=1A]
    # タバサ：……うん。  [voice 15398]
    voice "ch26_t_074"
    t "…Mm.{#ch26_t_074}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：だからもうさ……。
    voice "ch26_s_221"
    s "So please… Don't do anything reckless again, okay?{#ch26_s_221}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch26_t_075}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：あっ、さては守る自信がないな？  [voice 9039]
    voice "ch26_s_222"
    s "Oh—so you're not sure you can protect me, are you?{#ch26_s_222}"

    # タバサ：……。
    t "…{#ch26_t_076}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：じゃあ、指きりで約束しようか？  [voice 9040]
    voice "ch26_s_223"
    s "Then, how about a pinky promise?{#ch26_s_223}"

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：ゆびきり？  [voice 15399]
    voice "ch26_t_077"
    t "Pinky promise?{#ch26_t_077}"

    # サイト：俺のところじゃ、２人だけの約束をするときは
    voice "ch26_s_224"
    s "Where I come from, when two people make a private promise, they do it like this…{#ch26_s_224}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+238, level=80]
    $ dissolve_fx("id(238)")
    # [TRANS trans("crossfade", 1000)]
    # タバサ：あっ……。  [voice 15400]
    voice "ch26_t_078"
    t "Ah…{#ch26_t_078}"

    # サイト：お互いの小指と小指を絡めて……。  [voice 9042]
    voice "ch26_s_225"
    s "Hooking little fingers together…{#ch26_s_225}"

    # タバサ：……。
    t "…{#ch26_t_079}"

    # サイト：唄の節に合わせて約束を交わすんだ。  [voice 9043]
    voice "ch26_s_226"
    s "…and sealing the promise to the rhyme.{#ch26_s_226}"

    # タバサ：つまり……契約？  [voice 15401]
    voice "ch26_t_080"
    t "Meaning… a contract?{#ch26_t_080}"

    # サイト：うーん、そんな感じかな？
    voice "ch26_s_227"
    s "Hmm, something like that. Well then, here we go…{#ch26_s_227}"

    # サイト：ゆーびりきげんまん。
    voice "ch26_s_228"
    s "Yubi-piki, genman. If you lie—too bad! And I'll cut your finger off!{#ch26_s_228}"

    # [EVENT_CG event    image=+239, level=80]
    $ dissolve_fx("id(239)")
    # タバサ：……。
    t "…{#ch26_t_081}"

    # サイト：じゃ、これで約束したってことで頼むぜ？  [voice 9046]
    voice "ch26_s_229"
    s "So, that means we promised, right?{#ch26_s_229}"

    # タバサ：……うん。
    voice "ch26_t_082"
    t "…Mm. I'll try not to be reckless.{#ch26_t_082}"

    # サイト：ハハハ……。
    voice "ch26_s_230"
    s "Ha ha ha… 'Try' won't do, you know…{#ch26_s_230}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [COFFEE]
    $ pause(1.0)
    # → next scene 972
    jump ch27

    # ==== КОНЕЦ ГЛАВЫ 26 ====
    jump ch27
    return

