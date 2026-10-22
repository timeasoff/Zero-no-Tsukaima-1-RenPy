# Глава 5, часть 4 (основная линия 315–319 + extra-сцены
# 1383–1407): пять техпереходов, каждый вызывает свой extra-блок; в блоках —
# разговоры Сайто с Уэзерби, Табитой, Луизой с Анриеттой и Харуной, Кирхе,
# Гишем и Монморанси.
# Источник: ps2_source/chapters/chapter_06_本当の想い.txt (SCENE 315–319,
#   SCENE 1383–1407; «extra scenes: 1104..1875»).
# Точные аргументы: ps2_source/events_full/chapter_06_本当の想い.txt.
# Скелет собран генератором tools/gen_ch5_4_script.py (EN — tools/ch5_4_en.py,
#   RU — tools/ch5_4_ru.py), поэтому порядок реплик, голоса, спрайты и
#   события совпадают с источником дословно.
#
# Вход — jump ch5_4 из script-ch5_3.rpy; выход — jump ch5_5 (сцена 320) —
#   E7 «forward debt», закроется частью 5.
#
# Extra-блоки живут в части, где встретились (AGENTS §3): каждый блок —
#   отдельная метка (ch5_4_a … ch5_4_e), вызов из основной линии — `call`,
#   конец блока — `return`.
#
# Голоса: ch5.4_<spk>_<NNN> — новая группа части 4, нумерация с 001 по
#   говорящему, порядок порта (315 → 1383–1387 → 316 → 1388–1392 → 317 →
#   1393–1397 → 318 → 1398–1402 → 319 → 1403–1407).
#
# Не портируются: item() (инвентарь не реализован), TNDL, SE, waitAction/
#   waitTime/waitSEStop/waitLoad, msgon/msgoff, back(), beginSkip, MOVE/
#   MOVEINIT (карта переходов PS2).
#
# Фоны: bg 38 = town, bg 58 = town_square; id(41), id(50), id(53), id(54) —
#   имена пусты в image_id_map.csv (заглушки). CG нет.
#
# Спрайты 430, 507, 634, 808, 810, 865, 871 — PROVISIONAL (пиксель-сверка
#   SCENEDAT невозможна, архив PS2 не смонтирован): имена выведены по
#   блок-правилу справочника (база B = id - ((id - 5) mod 11); 0/1 — база,
#   2/3 — happy, 4/5 — angry, 6/7 — sad, 8/9 — shy).


label ch5_4:
    # Часть 4: основная линия 315–319 — пять техпереходов, каждый из
    # которых вызывает extra-блок (1383–1407). Сами блоки оформлены
    # отдельными метками с `return`: вызов из основной линии — `call`.

    # ==== SCENE 315 ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black", new_music="t27")
    # [BG hide]
    $ fade_fx("black")
    stop music fadeout 1.0
    # [BG hide]
    $ fade_fx("black")

    # [移動] → next(1383): extra-блок ch5_4_a
    call ch5_4_a from _call_ch5_4_a

    # ==== SCENE 316 ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black", new_music="t27")
    # [BG hide]
    $ fade_fx("black")
    stop music fadeout 1.0
    # [BG hide]
    $ fade_fx("black")

    # [移動] → next(1388): extra-блок ch5_4_b
    call ch5_4_b from _call_ch5_4_b

    # ==== SCENE 317 ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black", new_music="t27")
    # [BG hide]
    $ fade_fx("black")
    stop music fadeout 1.0
    # [BG hide]
    $ fade_fx("black")

    # [移動] → next(1393): extra-блок ch5_4_c
    call ch5_4_c from _call_ch5_4_c

    # ==== SCENE 318 ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black", new_music="t27")
    # [BG hide]
    $ fade_fx("black")
    stop music fadeout 1.0
    # [BG hide]
    $ fade_fx("black")

    # [移動] → next(1398): extra-блок ch5_4_d
    call ch5_4_d from _call_ch5_4_d

    # ==== SCENE 319 ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black", new_music="t27")
    # [BG hide]
    $ fade_fx("black")
    stop music fadeout 1.0
    # [BG hide]
    $ fade_fx("black")

    # [移動] → next(1403): extra-блок ch5_4_e
    call ch5_4_e from _call_ch5_4_e

    # [移動] → next(320): сцена 320 — часть 5 главы 5
    jump ch5_5
    return

label ch5_4_a:
    # ==== SCENE 1383 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +54 → id(54)]
    $ fade_fx("id(54)", new_music="t6")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("w 1 angry"))
    # [lay2 +506 → si 2 sad]
    $ show_sprites(("w 1 angry", "si 2 sad"))
    th "Oh — Siesta and Weatherby are here.{#ch5_4_th_001}"
    # JA: （あれ、シエスタとウェザリーがいる）
    voice "ch5.4_w_001"
    w "Why are all the young people these days like this! They have such fine talent, and it goes to waste."
    # JA[15866]: どうして最近の若い子はみんなこうなの！ / せっかくいい才能を持ってるのに、 / もったいないわ。
    # [lay20 hide]
    $ show_sprites(("si 2 sad"))
    # [lay2 hide]
    $ show_sprites()
    # [lay2 +507 → si 2 sad]
    $ show_sprites(("si 2 sad"))
    voice "ch5.4_si_001"
    si "Saito-san… I've been listening to everyone's complaints, in that same way, all this time…"
    # JA[14458]: サイトさん……。 / わたし、あの調子でずっとみんなの愚痴を / 聞いてるんです……。
    $ update_sympathy(20, char_key="siesta")
    # [lay2 hide]
    $ show_sprites()
    # [lay2 +506 → si 2 sad]
    $ show_sprites(("si 2 sad"))
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("s 3 sad", "si 2 sad"))
    th "…R-really?{#ch5_4_th_002}"
    # JA: （……マ、マジ？）
    # [lay5 hide]
    $ show_sprites(("si 2 sad"))
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("w 1 angry", "si 2 sad"))
    voice "ch5.4_w_002"
    w "I'm listening, you know! Honestly, the young people these days!"
    # JA[15867]: ちょっと、聞いてるの！ / ホントに今の若い子達は！

    # ---- 【選択肢】 ----
    menu:
        "That's not true!{#ch5_4_c1384}":
            # JA: そんなことはないです！
            # ==== SCENE 1384 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay2 +506 → si 2 sad]
            $ show_sprites(("w 1 angry", "si 2 sad"))
            play music t6 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay2 hide]
            $ show_sprites(("w 1 angry"))
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("w 1 angry", "s 1 angry"))
            voice "ch5.4_s_001"
            s "That's not true!{#ch5_4_v9873}"
            # JA[9873]: そんなことはないです！
            voice "ch5.4_s_002"
            s "They're the best of companions. I mean, sure, they're spoiled, and some of them are hard to stomach…"
            # JA[9874]: あいつらは最高の仲間達です。 / そりゃ、ワガママだったり、 / 鼻持ちならなかったりするけど……。
            voice "ch5.4_s_003"
            s "But they're not the sort of people who do things carelessly."
            # JA[9875]: でも、いいかげんなことをする奴らじゃ / ないです。
            # [lay5 hide]
            $ show_sprites(("w 1 angry"))
            # [lay2 +506 → si 2 sad]
            $ show_sprites(("w 1 angry", "si 2 sad"))
            voice "ch5.4_si_002"
            si "Saito-san…{#ch5_4_v14459}"
            # JA[14459]: サイトさん……。
            # [TNDL       tndl(30)] — не переносится (система не реализована, AGENTS §6)
            # [lay20 +1067 → w 1 sad]
            $ show_sprites(("w 1 sad", "si 2 sad"))
            voice "ch5.4_w_003"
            w "It seems I insulted your friend. I'm sorry.{#ch5_4_v15868}"
            # JA[15868]: きみの友人を侮辱してしまったようだな。 / すまなかった。
            # [lay2 hide]
            $ show_sprites(("w 1 sad"))
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("w 1 sad", "s 1 sad"))
            voice "ch5.4_s_004"
            s "N-no, this time I do think their spoiledness is to blame too."
            # JA[9876]: い、いや今回はあいつらのワガママも / 悪いとは思うんですよ。
            voice "ch5.4_s_005"
            s "Well, I think they're overthinking all those complicated things, like their family's standing and whatnot."
            # JA[9877]: まあ、実家の体面とかいろいろ難しいことを / 考えすぎてるんだと思うんです。
            voice "ch5.4_w_004"
            w "Well, nobles are like that, you know."
            # JA[15869]: まぁ、貴族とはそういう生き物だからね。
        "Well, you're right.":
            # JA: まあ、そうですね
            # ==== SCENE 1385 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay2 +506 → si 2 sad]
            $ show_sprites(("w 1 angry", "si 2 sad"))
            play music t6 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay2 hide]
            $ show_sprites(("w 1 angry"))
            # [lay5 +390 → s 1]
            $ show_sprites(("w 1 angry", "s 1"))
            voice "ch5.4_s_006"
            s "Well, you're right. They are spoiled, they don't listen to others, and they immediately start talking about commoners."
            # JA[9878]: まぁ、そうですね。 / 確かにワガママだし、人の話を聞かないし。 / すぐ、平民だと言い出す。
            voice "ch5.4_s_007"
            s "But they're not the sort of people to throw in the towel halfway. Can you believe me that much, at least?"
            # JA[9879]: でも、途中で投げ出すような / 人達じゃないんです。 / それだけは信じてもらえますか？
            # [lay20 hide]
            $ show_sprites(("s 1"))
            # [lay2 +500 → si 2]
            $ show_sprites(("si 2", "s 1"))
            voice "ch5.4_si_003"
            si "Saito-san…{#ch5_4_v14460}"
            # JA[14460]: サイトさん……。
            # [lay2 hide]
            $ show_sprites(("s 1"))
            # [lay20 +1067 → w 1 sad]
            $ show_sprites(("w 1 sad", "s 1"))
            voice "ch5.4_w_005"
            w "It seems I insulted your friend. I'm sorry.{#ch5_4_v15870}"
            # JA[15870]: きみの友人を侮辱してしまったようだな。 / すまなかった。
        "It's no use telling me that.":
            # JA: 俺に言われても困る！
            # ==== SCENE 1386 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay2 +506 → si 2 sad]
            $ show_sprites(("w 1 angry", "si 2 sad"))
            play music t6 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay2 hide]
            $ show_sprites(("w 1 angry"))
            # [lay5 +427 → s 3 angry]
            $ show_sprites(("w 1 angry", "s 3 angry"))
            voice "ch5.4_s_008"
            s "O-oh, it's no use telling me that. I'm the one who's always being run around by their spoiled ways!"
            # JA[9880]: お、俺に言われても困りますよ。 / あいつらのワガママにいつも振り回されてる / のは俺なんですから！
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            # [lay20 +1063 → w 1 happy]
            $ show_sprites(("w 1 happy", "s 3 angry"))
            voice "ch5.4_w_006"
            w "Saito seems to be having a hard time too, doesn't he."
            # JA[15871]: サイトも苦労してるようだな。

    # ==== SCENE 1387 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay20 +1067 → w 1 sad]
    $ show_sprites(("w 1 sad"))
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("w 1 sad", "s 1 sad"))
    play music t6 fadein 1.0
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [lay20 hide]
    $ show_sprites(("s 1 sad"))
    # [lay2 +500 → si 2]
    $ show_sprites(("si 2", "s 1 sad"))
    voice "ch5.4_si_004"
    si "By the way. What happened to the other actors? I don't see them much."
    # JA[14461]: そういえば。 / 他の役者さんはどうされたんですか？ / あまりお見かけしないんですけど。
    # [lay5 +396 → s 1 sad]
    th "By the way…{#ch5_4_th_003}"
    # JA: （そういえば……）
    # [lay5 hide]
    $ show_sprites(("si 2"))
    # [lay2 hide]
    $ show_sprites()
    # [lay20 +1067 → w 1 sad]
    $ show_sprites(("w 1 sad"))
    voice "ch5.4_w_007"
    w "There wasn't an actor who fit the image this time."
    # JA[15872]: 今回はイメージに合う役者がいなくてね。
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1"))
    voice "ch5.4_w_008"
    w "You, for all you're amateurs, match the image of this play perfectly… so I invited you, hoping to make use of you."
    # JA[15873]: きみ達は素人ながら今回の芝居のイメージと / ぴったりで……それで是非とも使いたいと / 声をかけたのだけど。
    # [lay20 x=-96]
    # [lay2 +504 → si 2 angry]
    $ show_sprites(("w 1", "si 2 angry"))
    voice "ch5.4_si_005"
    si "S-so that's what it was!"
    # JA[14462]: そ、そうだったんですか！
    th "Is that really true?{#ch5_4_th_004}"
    # JA: （それって本当かな？）
    th "Weatherby-san doesn't seem like someone who would consider it all right to hand the leading role to an amateur, someone who'd be fine with such a bold thing…{#ch5_4_th_005}"
    # JA: （ウェザリーさんは素人に主役を任せるような、 / 　そんなアバウトな事をよしとする人には / 　見えないんだけど……）
    th "Well, fine, I guess.{#ch5_4_th_006}"
    # JA: （まぁ、いいか）
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay20 hide]
    $ show_sprites(("si 2 angry"))
    # [lay2 hide]
    $ show_sprites()
    # [lay5 hide]
    # [BG hide]
    $ fade_fx("black")
    # [MOVE       move()] — не портируется
    return

label ch5_4_b:
    # ==== SCENE 1388 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +50 → id(50)]
    $ fade_fx("id(50)", new_music="t8")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay0 +632 → t 5]
    $ show_sprites(("t 5"))
    th "Oh — Tabitha's here.{#ch5_4_th_007}"
    # JA: （あれ、タバサがいる）
    # [SET        set("se0", {play = (0x03000000 +72)})] — SE не портируется
    th "…….{#ch5_4_th_008}"
    # JA: ……。
    $ update_sympathy(30, char_key="tabitha")
    th "She's even reading a book at a time like this…{#ch5_4_th_009}"
    # JA: （こんなときにも本を読んでるのか……）

    # ---- 【選択肢】 ----
    menu:
        "I wonder what book she's reading?":
            # JA: どんな本を読んでるんだろう？
            # ==== SCENE 1389 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay0 +632 → t 5]
            $ show_sprites(("t 5"))
            play music t8 fadein 1.0
            # [BG +50 → id(50)]
            $ fade_fx("id(50)")
            th "What book could she be reading? L-let me just peek…{#ch5_4_th_010}"
            # JA: （どんな本を読んでるんだろう？ / 　そ、そぉっと覗いてみて……）
            voice "ch5.4_t_001"
            t "A book on command magic.{#ch5_4_v15452}"
            # JA[15452]: 統率術の本。
            # [lay0 x=-96]
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("t 5", "s 1 angry"))
            voice "ch5.4_s_009"
            s "U-wha, wha! She noticed!"
            # JA[9881]: うわっ、わわっ！ / 気付いてたのか！
        "It'd be rude to disturb her":
            # JA: 邪魔をしたら悪いな
            # ==== SCENE 1390 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay0 +632 → t 5]
            $ show_sprites(("t 5"))
            play music t8 fadein 1.0
            # [BG +50 → id(50)]
            $ fade_fx("id(50)")
            th "It'd be rude to interrupt her reading… Maybe I should back off?{#ch5_4_th_011}"
            # JA: （読書の邪魔をしたら悪いな……。 / 　こりゃ撤退したほうがいいかな？）
            voice "ch5.4_t_002"
            t "A book on command magic.{#ch5_4_v15453}"
            # JA[15453]: 統率術の本。
            $ update_sympathy(15, char_key="tabitha")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            # [lay0 x=-96]
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("t 5", "s 1 angry"))
            voice "ch5.4_s_010"
            s "U-wha! She noticed!"
            # JA[9882]: うわっ！ / 気付いてたのか！
        "Let me play a prank":
            # JA: いたずらしてみよう
            # ==== SCENE 1391 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay0 +632 → t 5]
            $ show_sprites(("t 5"))
            play music t8 fadein 1.0
            # [BG +50 → id(50)]
            $ fade_fx("id(50)")
            th "She's reading it with such dedication…{#ch5_4_th_012}"
            # JA: （ずいぶんと熱心に読んでるなぁ……）
            th "Tabitha, quietly reading a book like this… she's like a princess from some country, like a doll…{#ch5_4_th_013}"
            # JA: （こうして静かに本を読んでるタバサって、 / 　どこかの国のお姫さまみたいというか、 / 　お人形さんみたいで……）
            th "…I-I want to poke her cheek… It looks soft…{#ch5_4_th_014}"
            # JA: （……ほ、頬っぺたとかつついてみたく / 　なるよな。 / 　や、柔らかそうで……）
            th "Swallowed. S-slowly…{#ch5_4_th_015}"
            # JA: （ゴクン。 / 　そ、そおっと……）
            voice "ch5.4_t_003"
            t "A book on command magic.{#ch5_4_v15454}"
            # JA[15454]: 統率術の本。
            $ update_sympathy(-15, char_key="tabitha")
            # [TNDL       tndl(30)] — не переносится (система не реализована, AGENTS §6)
            # [lay0 x=-96]
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("t 5", "s 1 angry"))
            voice "ch5.4_s_011"
            s "U-woah! Y-you scared me!"
            # JA[9883]: うわわっ！ / びっ、びっくりしたぁ！

    # ==== SCENE 1392 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("s 1 angry"))
    # [lay0 +632 → t 5]
    $ show_sprites(("t 5", "s 1 angry"))
    play music t8 fadein 1.0
    # [BG +50 → id(50)]
    $ fade_fx("id(50)")
    # [lay5 +390 → s 1]
    $ show_sprites(("t 5", "s 1"))
    voice "ch5.4_s_012"
    s "A book on command magic?"
    # JA[9884]: 統率術の本？
    voice "ch5.4_t_004"
    t "The title is 'How to Become the Ideal Boss.'"
    # JA[15455]: タイトルは「理想の上司になるための本」。
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("t 5", "s 3 sad"))
    voice "ch5.4_s_013"
    s "S-so that's what it is."
    # JA[9885]: そ、そうなんだ。
    th "I see — she's thinking about it in her own way, Tabitha-style.{#ch5_4_th_016}"
    # JA: （そうか、タバサなりに考えてくれてるんだ）
    voice "ch5.4_t_005"
    t "Don't worry — you can do it."
    # JA[15456]: 大丈夫、あなたならできるわ。
    voice "ch5.4_s_014"
    s "Huh?{#ch5_4_v9886}"
    # JA[9886]: えっ？
    th "A-am I being encouraged?{#ch5_4_th_017}"
    # JA: （は、励まされてる？）
    voice "ch5.4_t_006"
    t "Believe in yourself."
    # JA[15457]: 自分を信じて。
    # [lay5 +425 → s 3 happy]
    $ show_sprites(("t 5", "s 3 happy"))
    voice "ch5.4_s_015"
    s "A-ah, yes! I understand!"
    # JA[9887]: あ、ああ！ / 分かった！
    voice "ch5.4_s_016"
    s "Thanks, Tabitha! I'll give it a try!"
    # JA[9888]: ありがとう、タバサ！ / 頑張ってみるよ！
    # [lay5 hide]
    $ show_sprites(("t 5"))
    # [lay0 x=64]
    # [lay0 +634 → t 5 happy]
    $ show_sprites(("t 5 happy"))
    voice "ch5.4_t_007"
    t "It really worked."
    # JA[15458]: 本当に効いた。
    # [lay0 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +392 → s 1 happy]
    $ show_sprites(("s 1 happy"))
    voice "ch5.4_s_017"
    s "To think Tabitha is cheering me on like that… I have to do my best."
    # JA[9889]: タバサがあんなに励ましてくれるなんて。 / 頑張らないとな。
    # [lay5 hide]
    $ show_sprites()
    # [lay19 +946 → d 1 sad]
    $ show_sprites(("d 1 sad"))
    voice "ch5.4_d_001"
    th "…Hey, partner. Aren't you being a bit too simple?"
    # JA[1246]: （……あ、相棒。 / 　ちと、単純すぎねーか？）
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay19 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [MOVE       move()] — не портируется
    return

label ch5_4_c:
    # ==== SCENE 1393 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +58 → town_square]
    $ fade_fx("town_square", new_music="t9")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1"))
    th "Oh — Louise, the princess, and Haruna are here too.{#ch5_4_th_018}"
    # JA: （あ、ルイズとお姫さま。 / 　春奈もいる）
    # [lay5 hide]
    $ show_sprites()
    # [lay1 +317 → l 6 angry]
    $ show_sprites(("l 6 angry"))
    # [lay8 +808 → h 3]
    $ show_sprites(("l 6 angry", "h 3"))
    voice "ch5.4_l_001"
    l "Why on earth did you join a troupe like this?!"
    # JA[4986]: なんで、こんな劇団においでに / なったんですか！？
    voice "ch5.4_h_001"
    h "Oh, but even I am interested in the troupe."
    # JA[459]: あら、わたくしだって劇団に興味があるのよ。
    voice "ch5.4_l_002"
    l "B-but that doesn't mean you have to go on stage!"
    # JA[4987]: だ、だからって舞台にまで立つ必要なんて！
    th "It's gotten hard to walk away, somehow. Maybe I should retreat…{#ch5_4_th_019}"
    # JA: （なんか、出て行きにくくなっちゃったな。 / 　退散するか……）
    # [lay1 hide]
    $ show_sprites(("h 3"))
    # [lay8 hide]
    $ show_sprites()
    # [lay7 +962 → ha 2]
    $ show_sprites(("ha 2"))
    voice "ch5.4_ha_001"
    ha "A-Hiraga-kun!"
    # JA[1939]: あ、平賀くん！
    # [lay7 x=-96]
    # [lay5 +425 → s 3 happy]
    $ show_sprites(("ha 2", "s 3 happy"))
    voice "ch5.4_s_018"
    s "…H-how do you do."
    # JA[9890]: ……ど、どもッス。
    # [lay7 hide]
    $ show_sprites(("s 3 happy"))
    # [lay8 +808 → h 3]
    $ show_sprites(("h 3", "s 3 happy"))
    voice "ch5.4_h_002"
    h "Thank you for your hard work. Familiar-san."
    # JA[460]: お疲れさまです。 / 使い魔さん。
    $ update_sympathy(50, char_key="henrietta")
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("h 3", "s 3 sad"))
    voice "ch5.4_s_019"
    s "Are you really all right? Doing something like this."
    # JA[9891]: 本当に大丈夫なんですか？ / こんなことをしてて。
    # [lay5 hide]
    $ show_sprites(("h 3"))
    # [lay1 +317 → l 6 angry]
    $ show_sprites(("h 3", "l 6 angry"))
    voice "ch5.4_l_003"
    l "O-of course I'm not!"
    # JA[4988]: だ、大丈夫なワケないでしょ！
    # [lay8 +810 → h 3 happy]
    $ show_sprites(("h 3 happy", "l 6 angry"))
    voice "ch5.4_h_003"
    h "It's fine… As long as the commoners don't find out."
    # JA[461]: 大丈夫ですよ……。 / 民衆にバレなければ。
    # [lay1 +319 → l 6 sad]
    $ show_sprites(("h 3 happy", "l 6 sad"))
    voice "ch5.4_l_004"
    l "S-such a sloppy thing!"
    # JA[4989]: そ、そんないい加減な！
    # [lay8 hide]
    $ show_sprites(("l 6 sad"))
    # [lay7 +962 → ha 2]
    $ show_sprites(("ha 2", "l 6 sad"))
    voice "ch5.4_ha_002"
    ha "A-but, well. Everyone is very good at dancing and acting, aren't they?"
    # JA[1940]: あ、で、でも。 / 皆さんダンスや、演技がとても上手なんですね。
    voice "ch5.4_l_005"
    l "W-well, dancing is a noble accomplishment…"
    # JA[4990]: ま、まぁ、ダンスは貴族のたしなみだし……。
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("ha 2 sad", "l 6 sad"))
    voice "ch5.4_ha_003"
    ha "I see… a noble accomplishment, huh… Compared to that, I'm…"
    # JA[1941]: はあ……貴族のたしなみかぁ……。 / それにひきかえ私なんか……。
    # [lay19 +946 → d 1 sad]
    $ show_sprites(("ha 2 sad", "d 1 sad", "l 6 sad"))
    voice "ch5.4_d_002"
    th "Partner, say something… She's really getting down on herself?"
    # JA[1247]: （相棒、何か言ってやれ……。 / 　何か本気で落ち込んでるぞ？）
    # [lay8 hide]
    # [lay5 hide]
    # [lay1 hide]
    $ show_sprites(("ha 2 sad", "d 1 sad"))
    # [lay19 hide]
    $ show_sprites(("ha 2 sad"))
    # [lay7 hide]
    $ show_sprites()
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("s 3 sad"))
    voice "ch5.4_s_020"
    s "W-well, even if they say that."
    # JA[9892]: そ、そんなこといわれても。

    # ---- 【選択肢】 ----
    menu:
        "A girl's value isn't in her dancing!":
            # JA: 女の子の価値はダンスじゃない！
            # ==== SCENE 1394 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            play music t9 fadein 1.0
            # [BG +58 → town_square]
            $ fade_fx("town_square")
            # [lay19 x=304]
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1"))
            voice "ch5.4_s_021"
            s "A girl's value isn't in dancing and stuff!"
            # JA[9893]: 女の子の価値はダンスとかじゃないって！
            # [lay5 x=224]
            # [lay7 +962 → ha 2]
            $ show_sprites(("ha 2", "s 1"))
            voice "ch5.4_ha_004"
            ha "Eh, really?{#ch5_4_v1942}"
            # JA[1942]: え、そうなの？
            voice "ch5.4_s_022"
            s "Just because she's a bit good at dancing what does that prove! Haruna has something Louise doesn't!"
            # JA[9894]: ちょっとダンスが出来たからって / なんだっていうんだ！ / 春奈にはルイズにないものがあるさ！
            # [lay7 hide]
            $ show_sprites(("s 1"))
            # [lay1 +313 → l 6]
            $ show_sprites(("l 6", "s 1"))
            voice "ch5.4_l_006"
            l "Saito, I'll ask for comparison. What does Haruna have that I don't?"
            # JA[4991]: サイト、参考までに聞くけど。 / わたしになくてハルナが持ってる / ものってなぁに？
            $ update_sympathy(-10, char_key="louise")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("l 6", "s 3 sad"))
            voice "ch5.4_s_023"
            s "W-well, that… what would it be, I wonder."
            # JA[9895]: そ、そりゃ、その……。 / なんだろうねぇ。
            # [lay1 hide]
            $ show_sprites(("s 3 sad"))
            # [lay7 +968 → ha 2 sad]
            $ show_sprites(("ha 2 sad", "s 3 sad"))
            voice "ch5.4_ha_005"
            ha "Hiraga-kun…{#ch5_4_v1943}"
            # JA[1943]: 平賀くん……。
        "Why don't you ask Louise?":
            # JA: ルイズに教えてもらえば？
            # ==== SCENE 1395 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            play music t9 fadein 1.0
            # [BG +58 → town_square]
            $ fade_fx("town_square")
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1"))
            voice "ch5.4_s_024"
            s "Why don't you ask Louise? Asking Louise about dancing and all that…"
            # JA[9896]: 教えてもらえばいいんじゃないか？ / ルイズにダンスとか……。
            # [lay5 x=224]
            # [lay7 +962 → ha 2]
            $ show_sprites(("ha 2", "s 1"))
            voice "ch5.4_ha_006"
            ha "Eh?{#ch5_4_v1944}"
            # JA[1944]: え？
            voice "ch5.4_s_025"
            s "This is a good chance to study what they call a noble accomplishment!"
            # JA[9897]: この機会に、貴族のたしなみっていうのを / 勉強したらいいじゃん。
            # [lay7 +964 → ha 2 happy]
            $ show_sprites(("ha 2 happy", "s 1"))
            voice "ch5.4_ha_007"
            ha "Y-yes, you're right. I should take it as a good opportunity."
            # JA[1945]: そ、そうだよね。 / これを良い機会と思わなくちゃ。
        "Haruna has her own good points!":
            # JA: 春奈には春奈の良さがある！
            # ==== SCENE 1396 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            play music t9 fadein 1.0
            # [BG +58 → town_square]
            $ fade_fx("town_square")
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1"))
            voice "ch5.4_s_026"
            s "Haruna has her own good points, I tell you!"
            # JA[9898]: 春奈には春奈の良いところがあるって！
            # [lay5 x=224]
            # [lay7 +968 → ha 2 sad]
            $ show_sprites(("ha 2 sad", "s 1"))
            voice "ch5.4_ha_008"
            ha "…M-maybe?"
            # JA[1946]: ……そ、そうかな？
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("ha 2 sad", "s 3 sad"))
            voice "ch5.4_s_027"
            s "M-maybe."
            # JA[9899]: た、たぶん。
            # [lay7 +964 → ha 2 happy]
            $ show_sprites(("ha 2 happy", "s 3 sad"))
            voice "ch5.4_ha_009"
            ha "Hehehe… thank you, Hiraga-kun. For cheering me up."
            # JA[1947]: ふふふ……ありがとう、平賀くん。 / 励ましてくれて。
            $ update_sympathy(10, char_key="haruna")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)

    # ==== SCENE 1397 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("ha 2 sad"))
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("ha 2 sad", "s 3 sad"))
    play music t9 fadein 1.0
    # [BG +58 → town_square]
    $ fade_fx("town_square")
    # [lay7 hide]
    $ show_sprites(("s 3 sad"))
    # [lay1 +313 → l 6]
    $ show_sprites(("l 6", "s 3 sad"))
    voice "ch5.4_l_007"
    l "For now, Saito has to get better at dancing too. The way things stand, he's completely hopeless."
    # JA[4992]: とりあえず、サイトにもダンスが / 上手くなってもらわないとね。 / このままじゃ、ぜんぜん駄目だわ。
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("l 6", "s 1 sad"))
    voice "ch5.4_s_028"
    s "G-gee! It really is going to end up like that?"
    # JA[9900]: げ、げぇっ！ / やっぱりそうなる？
    # [lay1 hide]
    $ show_sprites(("s 1 sad"))
    # [lay7 +962 → ha 2]
    $ show_sprites(("ha 2", "s 1 sad"))
    voice "ch5.4_ha_010"
    ha "Y-yes, that's right. Hiraga-kun has to do his best too!"
    # JA[1948]: そ、そうですね。 / 平賀くんにも頑張ってもらわないと！
    # [lay5 hide]
    $ show_sprites(("ha 2"))
    # [lay8 +810 → h 3 happy]
    $ show_sprites(("ha 2", "h 3 happy"))
    voice "ch5.4_h_004"
    h "Then I'll help out as well."
    # JA[462]: じゃあ、わたくしもお手伝いするわ。
    # [lay1 hide]
    # [lay19 x=304]
    # [lay7 hide]
    $ show_sprites(("h 3 happy"))
    # [lay8 hide]
    $ show_sprites()
    # [lay5 hide]
    # [lay5 +430 → s 3 sad]
    $ show_sprites(("s 3 sad"))
    voice "ch5.4_s_029"
    s "H-help meee!"
    # JA[9901]: た、助けてぇぇぇっ！
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [MOVE       move()] — не портируется
    return

label ch5_4_d:
    # ==== SCENE 1398 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +41 → id(41)]
    $ fade_fx("id(41)", new_music="t7")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1"))
    th "Oh — Kirche is here.{#ch5_4_th_020}"
    # JA: （あれ、キュルケがいる）
    voice "ch5.4_s_030"
    s "Yo, Kirche."
    # JA[9902]: やぁ、キュルケ。
    # [lay5 x=224]
    # [lay6 +693 → k 2 sad]
    $ show_sprites(("k 2 sad", "s 1"))
    voice "ch5.4_k_001"
    k "…Eek! Oh my, what is it? My darling?"
    # JA[2987]: ……キャッ！ / あら、どうしたの？ / ダーリン？
    $ update_sympathy(20, char_key="kirche")
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("k 2 sad", "s 3 sad"))
    voice "ch5.4_s_031"
    s "Um, well, that is…"
    # JA[9903]: えっと、だな……。
    # [lay6 +687 → k 2]
    $ show_sprites(("k 2", "s 3 sad"))
    voice "ch5.4_k_002"
    k "…You're not going back to rehearsal, are you?"
    # JA[2988]: ……練習には戻らないのか、でしょう？
    voice "ch5.4_s_032"
    s "U-um… no, well… …Yes."
    # JA[9904]: うっ……いや、まあ……。 / ……そうです。
    # [lay6 +693 → k 2 sad]
    $ show_sprites(("k 2 sad", "s 3 sad"))
    voice "ch5.4_k_003"
    k "Eeeh~. Well, it is a bother, you know…"
    # JA[2989]: え～～。 / だって、面倒くさいし……。

    # ---- 【選択肢】 ----
    menu:
        "A-a bother, you say…":
            # JA: め、面倒くさいって
            # ==== SCENE 1399 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            # [lay6 +693 → k 2 sad]
            $ show_sprites(("k 2 sad", "s 3 sad"))
            play music t7 fadein 1.0
            # [BG +41 → id(41)]
            $ fade_fx("id(41)")
            # [lay5 +427 → s 3 angry]
            $ show_sprites(("k 2 sad", "s 3 angry"))
            voice "ch5.4_s_033"
            s "A-a bother, you say…? That's no way to talk!"
            # JA[9905]: め、面倒くさいって……そんないい加減な！
            # [lay6 +689 → k 2 happy]
            $ show_sprites(("k 2 happy", "s 3 angry"))
            voice "ch5.4_k_004"
            k "Oh, come on. Stop that… You've just gotten bored of it."
            # JA[2990]: もう、いいじゃない。 / そんなこと……。 / 飽きちゃったんだし。
            voice "ch5.4_s_034"
            s "You can say that, but!"
            # JA[9906]: そうはいってもさ！
            voice "ch5.4_k_005"
            k "Ufufufu…{#ch5_4_v2991}"
            # JA[2991]: うふふふ……。
        "Hey, come back to rehearsal":
            # JA: なあ、戻ってこいよ
            # ==== SCENE 1400 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            # [lay6 +693 → k 2 sad]
            $ show_sprites(("k 2 sad", "s 3 sad"))
            play music t7 fadein 1.0
            # [BG +41 → id(41)]
            $ fade_fx("id(41)")
            # [lay5 +429 → s 3 sad]
            voice "ch5.4_s_035"
            s "Hey, come back to rehearsal…"
            # JA[9907]: なあ、戻ってこいよ……。
            # [lay6 +689 → k 2 happy]
            $ show_sprites(("k 2 happy", "s 3 sad"))
            voice "ch5.4_k_006"
            k "I wonder what I should do~?"
            # JA[2992]: どうしようかな～～？
            # [lay5 +390 → s 1]
            $ show_sprites(("k 2 happy", "s 1"))
            voice "ch5.4_s_036"
            s "It's obvious — it's only Kirche who shines on stage!"
            # JA[9908]: やっぱり舞台で映えるのは / キュルケじゃないと無理だって！
            # [lay6 +687 → k 2]
            $ show_sprites(("k 2", "s 1"))
            voice "ch5.4_k_007"
            k "…Oh my, my darling thinks so too?"
            # JA[2993]: ……あらあら、ダーリンもそう思う？
            $ update_sympathy(10, char_key="kirche")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            # [lay5 +425 → s 3 happy]
            $ show_sprites(("k 2", "s 3 happy"))
            voice "ch5.4_s_037"
            s "I do! I do!"
            # JA[9909]: 思う！ / 思う！
        "I want to slack off too, but…":
            # JA: 俺もサボりたいけどさ
            # ==== SCENE 1401 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            # [lay6 +693 → k 2 sad]
            $ show_sprites(("k 2 sad", "s 3 sad"))
            play music t7 fadein 1.0
            # [BG +41 → id(41)]
            $ fade_fx("id(41)")
            # [lay5 +429 → s 3 sad]
            voice "ch5.4_s_038"
            s "W-well, I want to slack off too, but…"
            # JA[9910]: そ、そりゃ俺もサボりたいけどさ……。
            # [lay6 +691 → k 2 angry]
            $ show_sprites(("k 2 angry", "s 3 sad"))
            voice "ch5.4_k_008"
            k "Mmm, I'm not the one slacking off, you know."
            # JA[2994]: む、別にあたしはサボってるわけじゃないわよ。
            $ update_sympathy(-10, char_key="kirche")
            # [TNDL       tndl(30)] — не переносится (система не реализована, AGENTS §6)
            # [lay5 +390 → s 1]
            $ show_sprites(("k 2 angry", "s 1"))
            voice "ch5.4_s_039"
            s "…Eh? What do you mean?{#ch5_4_v9911}"
            # JA[9911]: ……え？ / それってどういう？
            # [lay6 +687 → k 2]
            $ show_sprites(("k 2", "s 1"))
            voice "ch5.4_k_009"
            k "A-ah! N-no, it's fine! Don't worry about it!"
            # JA[2995]: あ！ / い、いいじゃない！ / 気にしないで！

    # ==== SCENE 1402 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay5 +427 → s 3 angry]
    $ show_sprites(("s 3 angry"))
    # [lay6 +689 → k 2 happy]
    $ show_sprites(("k 2 happy", "s 3 angry"))
    play music t7 fadein 1.0
    # [BG +41 → id(41)]
    $ fade_fx("id(41)")
    # [lay6 +687 → k 2]
    $ show_sprites(("k 2", "s 3 angry"))
    voice "ch5.4_k_010"
    k "Rest easy, my darling. There's a good reason I won't come back. I'm just a little busy right now."
    # JA[2996]: ダーリン、安心して。 / 戻らないのにはちゃんと理由があるのよ。 / それで、今はちょっと忙しいだけ。
    # [lay5 +390 → s 1]
    $ show_sprites(("k 2", "s 1"))
    voice "ch5.4_s_040"
    s "…Eh? What do you mean?{#ch5_4_v9912}"
    # JA[9912]: ……えっ？ / それって、どういう？
    voice "ch5.4_k_011"
    k "Yes, yes! We'll continue this another time!"
    # JA[2997]: はいはい！ / この続きはまたこんどね！
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("k 2", "s 3 sad"))
    voice "ch5.4_s_041"
    s "W-wait! Kirche!"
    # JA[9913]: ちょ、ちょっと！ / キュルケ！
    # [lay6 +689 → k 2 happy]
    $ show_sprites(("k 2 happy", "s 3 sad"))
    voice "ch5.4_k_012"
    k "Bye-bye~. My darling~."
    # JA[2998]: じゃあね～～。 / ダーリン～～。
    # [lay6 hide]
    $ show_sprites(("s 3 sad"))
    # [lay5 x=64]
    voice "ch5.4_s_042"
    s "O-oi!"
    # JA[9914]: お、おいっ！
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("s 1 sad"))
    voice "ch5.4_s_043"
    s "Ahh, I feel like I've been caught in the smoke."
    # JA[9915]: あ～あ、なんだか煙にまかれちゃったな。
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [MOVE       move()] — не портируется
    return

label ch5_4_e:
    # ==== SCENE 1403 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +38 → town]
    $ fade_fx("town", new_music="t18")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay3 +863 → m 2]
    $ show_sprites(("m 2"))
    # [lay4 +555 → g 1]
    $ show_sprites(("m 2", "g 1"))
    th "Guiche and Montmorency are here.{#ch5_4_th_021}"
    # JA: （ギーシュとモンモンがいる）
    # [lay4 hide]
    $ show_sprites(("m 2"))
    # [lay5 +425 → s 3 happy]
    $ show_sprites(("m 2", "s 3 happy"))
    voice "ch5.4_s_044"
    s "Hey, Montmon."
    # JA[9916]: よう、モンモン。
    # [lay3 +865 → m 2 happy]
    $ show_sprites(("m 2 happy", "s 3 happy"))
    voice "ch5.4_m_001"
    m "Oh, Saito. What a coincidence to meet here."
    # JA[3984]: あら、サイト。 / こんなところで奇遇ね。
    # [lay3 hide]
    $ show_sprites(("s 3 happy"))
    # [lay4 +570 → g 2 angry]
    $ show_sprites(("g 2 angry", "s 3 happy"))
    voice "ch5.4_g_001"
    g "Hey, are you ignoring me?!"
    # JA[1430]: おい、ぼくのことは無視かい！
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("g 2 angry", "s 1 sad"))
    voice "ch5.4_s_045"
    s "Ah, Guiche is here too…"
    # JA[9917]: ああ、ギーシュもいたのか……。
    voice "ch5.4_g_002"
    g "What's with that blatant rudeness?!"
    # JA[1431]: なんなんだい、そのあからさまな扱いの悪さは！

    # ---- 【選択肢】 ----
    menu:
        "It's just your imagination":
            # JA: 気のせいだって
            # ==== SCENE 1404 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("s 1 sad"))
            # [lay4 +570 → g 2 angry]
            $ show_sprites(("g 2 angry", "s 1 sad"))
            play music t18 fadein 1.0
            # [BG +38 → town]
            $ fade_fx("town")
            # [lay5 +390 → s 1]
            $ show_sprites(("g 2 angry", "s 1"))
            voice "ch5.4_s_046"
            s "It's just your imagination."
            # JA[9918]: 気のせいだって。
            # [lay4 +559 → g 1 angry]
            $ show_sprites(("g 1 angry", "s 1"))
            voice "ch5.4_g_003"
            g "Is that really so?{#ch5_4_v1432}"
            # JA[1432]: 本当だろうな？
            # [lay4 +570 → g 2 angry]
            $ show_sprites(("g 2 angry", "s 1"))
            voice "ch5.4_g_004"
            g "Surely you're not after my Montmorency as well?"
            # JA[1433]: まさか、きみはぼくのモンモランシーまで / 狙ってるのではあるまいな？
            # [lay5 hide]
            $ show_sprites(("g 2 angry"))
            # [lay3 +871 → m 2 shy]
            $ show_sprites(("g 2 angry", "m 2 shy"))
            voice "ch5.4_m_002"
            m "Eh!{#ch5_4_v3985}"
            # JA[3985]: えっ！
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            # [lay4 +572 → g 2 sad]
            $ show_sprites(("g 2 sad", "m 2 shy"))
            voice "ch5.4_g_005"
            g "W-what are you blushing about? Montmorency?"
            # JA[1434]: な、何を頬を赤らめてるんだい？ / モンモランシー？
            # [lay3 +869 → m 2 sad]
            $ show_sprites(("g 2 sad", "m 2 sad"))
            voice "ch5.4_m_003"
            m "S-such a thing…{#ch5_4_v3986}"
            # JA[3986]: そ、そんなことは……。
            # [lay4 hide]
            $ show_sprites(("m 2 sad"))
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1", "m 2 sad"))
            voice "ch5.4_s_047"
            s "W-well, more important than that!"
            # JA[9919]: そ、そんなことより！
        "Don't worry about it!":
            # JA: 気にするな
            # ==== SCENE 1405 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("s 1 sad"))
            # [lay4 +570 → g 2 angry]
            $ show_sprites(("g 2 angry", "s 1 sad"))
            play music t18 fadein 1.0
            # [BG +38 → town]
            $ fade_fx("town")
            # [lay5 +390 → s 1]
            $ show_sprites(("g 2 angry", "s 1"))
            voice "ch5.4_s_048"
            s "…Don't worry about it!"
            # JA[9920]: ……気にするなって！
            # [lay4 +559 → g 1 angry]
            $ show_sprites(("g 1 angry", "s 1"))
            voice "ch5.4_g_006"
            g "Deny it!"
            # JA[1435]: 否定しろよ！
            # [lay5 hide]
            $ show_sprites(("g 1 angry"))
            # [lay3 +869 → m 2 sad]
            $ show_sprites(("g 1 angry", "m 2 sad"))
            voice "ch5.4_m_004"
            m "It does feel like a rather fitting way to treat me, though."
            # JA[3987]: なんだか妥当な扱いのような気もするけど。
            # [lay4 +561 → g 1 sad]
            $ show_sprites(("g 1 sad", "m 2 sad"))
            voice "ch5.4_g_007"
            g "Montmorency!"
            # JA[1436]: モンモランシー！
            # [lay4 hide]
            $ show_sprites(("m 2 sad"))
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1", "m 2 sad"))
            voice "ch5.4_s_049"
            s "W-well, that matters more!"
            # JA[9921]: そ、そんなことよりも！
        "It's always like that, isn't it?{#ch5_4_c1406}":
            # JA: いつものことだろ？
            # ==== SCENE 1406 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("s 1 sad"))
            # [lay4 +570 → g 2 angry]
            $ show_sprites(("g 2 angry", "s 1 sad"))
            play music t18 fadein 1.0
            # [BG +38 → town]
            $ fade_fx("town")
            # [lay5 +396 → s 1 sad]
            voice "ch5.4_s_050"
            s "It's always like that, isn't it?{#ch5_4_v9922}"
            # JA[9922]: いつものことだろ？
            # [lay4 +559 → g 1 angry]
            $ show_sprites(("g 1 angry", "s 1 sad"))
            voice "ch5.4_g_008"
            g "You didn't just say something outrageous, did you?"
            # JA[1437]: きみは今、なにかとんでもないことを / 言わなかったか？
            # [lay5 +425 → s 3 happy]
            $ show_sprites(("g 1 angry", "s 3 happy"))
            voice "ch5.4_s_051"
            s "A-ah, no. I didn't say anything."
            # JA[9923]: あ、いや。 / なにも言ってないぞ。
            # [lay4 +568 → g 2 happy]
            $ show_sprites(("g 2 happy", "s 3 happy"))
            voice "ch5.4_g_009"
            g "I see. A mishearing, then. Hahaha, good."
            # JA[1438]: そうか。聞き違いか。 / ははは、良かった。
            # [lay5 hide]
            $ show_sprites(("g 2 happy"))
            # [lay3 +869 → m 2 sad]
            $ show_sprites(("g 2 happy", "m 2 sad"))
            voice "ch5.4_m_005"
            m "More important than that. It wasn't that you had some business, was it?"
            # JA[3988]: そんなことよりも。 / なにか用事があったのではなくて？
            # [lay4 hide]
            $ show_sprites(("m 2 sad"))
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1", "m 2 sad"))
            voice "ch5.4_s_052"
            s "Yeah.{#ch5_4_v9924}"
            # JA[9924]: ああ。

    # ==== SCENE 1407 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay3 +869 → m 2 sad]
    $ show_sprites(("m 2 sad"))
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1", "m 2 sad"))
    play music t18 fadein 1.0
    # [BG +38 → town]
    $ fade_fx("town")
    voice "ch5.4_s_053"
    s "Hey, aren't you going back to rehearse on the stage?"
    # JA[9925]: なあ、舞台の練習に戻らないのか？
    # [lay3 +863 → m 2]
    $ show_sprites(("s 1", "m 2"))
    voice "ch5.4_m_006"
    m "It's that, after all. I'm sorry. I can't for a while yet."
    # JA[3989]: やっぱり、その話ね。 / ごめんなさい。 / もうしばらくはダメよ。
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("s 1 sad", "m 2"))
    voice "ch5.4_s_054"
    s "Well, I imagine being a noble makes a lot of things difficult…"
    # JA[9926]: まぁ、貴族だからいろいろ大変だと / 思うんだけどさ……。
    # [lay3 hide]
    $ show_sprites(("s 1 sad"))
    # [lay4 +566 → g 2]
    $ show_sprites(("s 1 sad", "g 2"))
    voice "ch5.4_g_010"
    g "A-ah, no! That's a separate matter, it's all right."
    # JA[1439]: あ、いや！ / それは別にもういいんだ。
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("s 1 angry", "g 2"))
    voice "ch5.4_s_055"
    s "W-well, then. Why…!"
    # JA[9927]: じ、じゃあ。 / なんで……！
    # [lay4 +572 → g 2 sad]
    $ show_sprites(("s 1 angry", "g 2 sad"))
    voice "ch5.4_g_011"
    g "N-no, it's, um. K-kirche was…"
    # JA[1440]: いやその、なんだ。 / キュ、キュルケが……。
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("s 1 sad", "g 2 sad"))
    voice "ch5.4_s_056"
    s "Huh? Kirche?"
    # JA[9928]: へ？ / キュルケが？
    # [lay5 hide]
    $ show_sprites(("g 2 sad"))
    # [lay3 +867 → m 2 angry]
    $ show_sprites(("m 2 angry", "g 2 sad"))
    voice "ch5.4_m_007"
    m "Idiot!"
    # JA[3990]: バカっ！
    stop music fadeout 1.0
    # [SET        set("se0", {play = (0x03000000 +62)})] — SE не портируется
    # [VIBRATE    vibrate(2)] — SE не портируется
    # [EVENT_CG hide]
    $ fade_fx("black", new_music="t29")
    # [lay5 hide]
    voice "ch5.4_g_012"
    g "Gah!"
    # JA[1441]: ぐはっ！
    voice "ch5.4_m_008"
    m "Honestly, you two! You can't keep a secret!"
    # JA[3991]: ホントにもう！ / 口が軽いんだから！
    # [lay4 hide]
    $ show_sprites(("m 2 angry"))
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("m 2 angry", "s 1 sad"))
    voice "ch5.4_s_057"
    s "M-montmorency!?"
    # JA[9929]: モ、モンモランシー！？
    # [lay3 +865 → m 2 happy]
    $ show_sprites(("m 2 happy", "s 1 sad"))
    voice "ch5.4_m_009"
    m "Once my own affairs are settled, I'll return to the theater, so please rest easy."
    # JA[3992]: こちらの都合がつき次第、劇場には戻りますから、 / 安心してください。
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("m 2 happy", "s 3 sad"))
    voice "ch5.4_s_058"
    s "Y-yes…{#ch5_4_v9930}"
    # JA[9930]: は、はあ……。
    th "…W-what on earth is going on?{#ch5_4_th_022}"
    # JA: （……な、何がどうなってるんだか？）
    # [lay3 +863 → m 2]
    $ show_sprites(("m 2", "s 3 sad"))
    voice "ch5.4_m_010"
    m "Well then, we must be on our way. S-so, bye~."
    # JA[3993]: それでは、わたし達は急ぎますので。 / で、では～～。
    # [lay3 hide]
    $ show_sprites(("s 3 sad"))
    # [lay4 +572 → g 2 sad]
    $ show_sprites(("g 2 sad", "s 3 sad"))
    voice "ch5.4_g_013"
    g "D-don't pull me. Montmorency~~~."
    # JA[1442]: ひ、ひっぱらないで。 / モンモランシー～～～。
    # [lay4 hide]
    $ show_sprites(("s 3 sad"))
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("s 1 sad"))
    voice "ch5.4_s_059"
    s "Ahh! They got away."
    # JA[9931]: ああっ！ / 逃げられた。
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [MOVE       move()] — не портируется
    return
