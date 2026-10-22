# Глава 5, часть 3 (сцены 300–314): итог переговоров, начало репетиций,
# рассказ Уэзерби о пьесе «双月天女» и появление Анриетты.
# Источник: ps2_source/chapters/chapter_06_本当の想い.txt (SCENE 300–314).
# Точные аргументы: ps2_source/events_full/chapter_06_本当の想い.txt.
# Скелет собран генератором tools/gen_ch5_3_script.py (EN — tools/ch5_3_en.py,
#   RU — tools/ch5_3_ru.py), поэтому порядок реплик, голоса, спрайты и
#   события совпадают с источником дословно.
#
# Вход — jump ch5_3 из script-ch5_2.rpy; выход — jump ch5_4 (сцена 315) —
#   E7 «forward debt», закроется частью 4.
#
# Голоса: ch5.3_<spk>_<NNN> — новая группа части 3, нумерация с 001 по
#   говорящему, порядок порта (300 → 301–303 → 304 → 305 → 306–308 → 310 →
#   311–313 → 314).
#
# Не портируются: item() (инвентарь не реализован), TNDL, SE, waitAction/
#   waitTime/waitSEStop/waitLoad, msgon/msgoff, back(), beginSkip.
#
# Фоны/CG: id(43), id(54), id(256) — имена пусты в image_id_map.csv
#   (заглушки), bg 88 = sky, bg 90 = sky_night.
#
# Спрайты 572, 632, 638, 863, 867, 869 — PROVISIONAL (пиксель-сверка
#   SCENEDAT невозможна, архив PS2 не смонтирован): имена выведены по
#   блок-правилу справочника (база B = id - ((id - 5) mod 11); 0/1 — база,
#   2/3 — happy, 4/5 — angry, 6/7 — sad, 8/9 — shy).


label ch5_3:
    # Часть 3: итог переговоров (сцена 300) → решение играть в театре → репетиции и рассказ о пьесе → появление Анриетты.
    # Сцена 300 начинается с RESET (возврат в гостиницу).

    # ==== SCENE 300 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +90 → sky_night]
    $ fade_fx("sky_night", new_music="t29")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    voice "ch5.3_l_001"
    l "Haaah…! You stupid dog…."
    # JA[6210]: はぁ～～っ！ / この、バカ犬は……。
    voice "ch5.3_s_001"
    s "……."
    # JA[11648]: ……。
    # [lay1 hide]
    # [lay5 hide]
    # [BG +43 → id(43)]
    $ fade_fx("id(43)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay1 +339 → l 3 angry]
    $ show_sprites(("l 3 angry"))
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("l 3 angry", "s 1 sad"))
    voice "ch5.3_l_002"
    l "'Honestly, you always take on the scut work' — who might that be?"
    # JA[6211]: 「まったく、安請け合いなんかしやがって」 / そういったのは誰かしら？
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("l 3 angry", "s 1 angry"))
    voice "ch5.3_s_002"
    s "W-what's with that face?! What are you so grumpy about?"
    # JA[11649]: な、なんだよ。 / その不機嫌そうな顔は！
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "s 1 angry"))
    voice "ch5.3_l_003"
    l "N-no, it's just that… I was wondering whether we'd really have to pass ourselves off as traveling entertainers. That's all I meant."
    # JA[6212]: な・ん・で、わたし達が旅芸人のマネゴト / なんてしなくちゃいけないのかなーって。 / そう思っただけよ。
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("l 1 angry", "s 3 sad"))
    voice "ch5.3_s_003"
    s "……Uuugh, sorry about that."
    # JA[11650]: ……うう、ごめんなしゃい。
    # [lay5 hide]
    $ show_sprites(("l 1 angry"))
    # [lay6 +682 → k 1 sad]
    $ show_sprites(("l 1 angry", "k 1 sad"))
    voice "ch5.3_k_001"
    k "Well, if my family found out, they'd disown me…"
    # JA[3260]: まぁ、実家に知れたら勘当ものよね……。
    # [lay1 hide]
    $ show_sprites(("k 1 sad"))
    # [lay0 +594 → t 1 sad]
    $ show_sprites(("t 1 sad", "k 1 sad"))
    th "…….{#ch5_3_th_001}"
    # JA: ……。
    # [lay6 hide]
    $ show_sprites(("t 1 sad"))
    # [lay2 +500 → si 2]
    $ show_sprites(("t 1 sad", "si 2"))
    voice "ch5.3_si_001"
    si "I, I'm perfectly fine with it, you know. Saito-san."
    # JA[14778]: わ、わたしは別にかまいませんよ。 / サイトさん。
    # [lay0 hide]
    $ show_sprites(("si 2"))
    # [lay4 +572 → g 2 sad]
    $ show_sprites(("g 2 sad", "si 2"))
    voice "ch5.3_g_001"
    g "W-what do I do?! If my father finds out!"
    # JA[1510]: ど、どうするんだよ！ / 父上に知られたら！
    # [lay2 hide]
    $ show_sprites(("g 2 sad"))
    # [lay3 +858 → m 1 sad]
    $ show_sprites(("g 2 sad", "m 1 sad"))
    voice "ch5.3_m_001"
    m "Come on, Guiche… Stop crying."
    # JA[4077]: ちょっとギーシュ……泣くのはやめなさいよ。
    # [lay3 hide]
    $ show_sprites(("g 2 sad"))
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("g 2 sad", "s 3 sad"))
    voice "ch5.3_s_004"
    s "S-so overdramatic… Why are you so worked up over it?"
    # JA[11651]: そ、そんなオーバーな……。 / なんでそこまで落ち込むんだよ。
    # [lay4 hide]
    $ show_sprites(("s 3 sad"))
    # [lay6 +680 → k 1 angry]
    $ show_sprites(("k 1 angry", "s 3 sad"))
    voice "ch5.3_k_002"
    k "My darling may not understand, but… performing a play for the sake of commoners — that's a matter of noble authority."
    # JA[3261]: ダーリンには分からないかもしれないけど、 / 平民のために芝居を演じるなんて、 / 貴族の権威にかかわるのよ。
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("k 1 angry", "s 1 sad"))
    voice "ch5.3_s_005"
    s "Seriously…."
    # JA[11652]: まじかよ……。
    # [lay6 hide]
    $ show_sprites(("s 1 sad"))
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "s 1 sad"))
    voice "ch5.3_l_004"
    l "That's reality."
    # JA[6213]: それが現実よ。
    # [lay1 hide]
    $ show_sprites(("s 1 sad"))
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("ha 2 sad", "s 1 sad"))
    voice "ch5.3_ha_001"
    ha "I'm sorry. I'm causing you all so much trouble…"
    # JA[2361]: ごめんなさい。 / 皆さんにご迷惑までかけて……。
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("ha 2 sad", "s 3 sad"))
    th "This is a problem… Who should I try to persuade…?{#ch5_3_th_002}"
    # JA: （こりゃ、困ったな。 / 　誰から説得すればいいんだろう……）

    # ---- 【選択肢】 ----
    menu:
        "Persuade Siesta":
            # JA: シエスタを説得する
            # ==== SCENE 301 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            # [lay7 +968 → ha 2 sad]
            $ show_sprites(("ha 2 sad", "s 3 sad"))
            play music t29 fadein 1.0
            # [BG +43 → id(43)]
            $ fade_fx("id(43)")
            th "Persuade Siesta{#ch5_3_th_003}"
            # JA: （シエスタを説得するか）
            # [lay5 +423 → s 3]
            $ show_sprites(("ha 2 sad", "s 3"))
            voice "ch5.3_s_006"
            s "How about Siesta?"
            # JA[11653]: シエスタはどうなんだ？
            # [lay7 hide]
            $ show_sprites(("s 3"))
            # [lay2 +500 → si 2]
            $ show_sprites(("si 2", "s 3"))
            voice "ch5.3_si_002"
            si "Saito-san. As I told you earlier, I'm perfectly fine."
            # JA[14779]: サイトさん。 / さっきも言いましたとおり、 / わたしは大丈夫ですよ。
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("si 2", "s 3 sad"))
            voice "ch5.3_s_007"
            s "Huh, was it?"
            # JA[11654]: あれ、そうだっけ？
            # [lay2 +504 → si 2 angry]
            $ show_sprites(("si 2 angry", "s 3 sad"))
            voice "ch5.3_si_003"
            si "Saito-san, please listen to me properly."
            # JA[14780]: サイトさん、ちゃんと話を聞いてください。
            $ update_sympathy(-10, char_key="siesta")
            # [lay2 hide]
            $ show_sprites(("s 3 sad"))
        "Persuade Louise":
            # JA: ルイズを説得する
            # ==== SCENE 302 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay7 +968 → ha 2 sad]
            $ show_sprites(("ha 2 sad"))
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("ha 2 sad", "s 3 sad"))
            play music t29 fadein 1.0
            # [BG +43 → id(43)]
            $ fade_fx("id(43)")
            th "Persuade Louise{#ch5_3_th_004}"
            # JA: （ルイズを説得するか）
            # [lay5 +425 → s 3 happy]
            $ show_sprites(("ha 2 sad", "s 3 happy"))
            voice "ch5.3_s_008"
            s "U-um, our master…"
            # JA[11655]: あのー、ご主人様……。
            # [lay7 hide]
            $ show_sprites(("s 3 happy"))
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry", "s 3 happy"))
            voice "ch5.3_l_005"
            l "No!{#ch5_3_v6214}"
            # JA[6214]: 駄目よ！
            $ update_sympathy(-10, char_key="louise")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            # [lay5 +427 → s 3 angry]
            $ show_sprites(("l 1 angry", "s 3 angry"))
            voice "ch5.3_s_009"
            s "I haven't even said anything yet!"
            # JA[11656]: まだ、何も言ってねーじゃねーか！
            voice "ch5.3_l_006"
            l "What doesn't work is what doesn't work!"
            # JA[6215]: 駄目なものは駄目なの！
            # [lay1 hide]
            $ show_sprites(("s 3 angry"))
        "Persuade Kirche":
            # JA: キュルケを説得する
            # ==== SCENE 303 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay7 +968 → ha 2 sad]
            $ show_sprites(("ha 2 sad"))
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("ha 2 sad", "s 3 sad"))
            play music t29 fadein 1.0
            # [BG +43 → id(43)]
            $ fade_fx("id(43)")
            th "Persuade Kirche{#ch5_3_th_005}"
            # JA: （キュルケを説得するか）
            # [lay5 +423 → s 3]
            $ show_sprites(("ha 2 sad", "s 3"))
            voice "ch5.3_s_010"
            s "How about Kirche? Doesn't she look like she's enjoying this?"
            # JA[11657]: キュルケはどうなんだ？ / 面白そうに感じないか？
            # [lay7 hide]
            $ show_sprites(("s 3"))
            # [lay6 +682 → k 1 sad]
            $ show_sprites(("k 1 sad", "s 3"))
            voice "ch5.3_k_003"
            k "Hmm… well, if it's a stage I share with my darling… I suppose I could consider it…"
            # JA[3262]: うーん、まぁダーリンと一緒の舞台だったら / 考えてもいいけど……。
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("k 1 sad", "s 3 sad"))
            voice "ch5.3_s_011"
            s "Come on, don't make it so hard. There's no way I could do that."
            # JA[11658]: また、難しいことを言うなよ。 / そんなこと絶対無理だって。
            voice "ch5.3_k_004"
            k "Then it wouldn't be much fun, would it…"
            # JA[3263]: だったら、つまらないかなぁ……。
            $ update_sympathy(-10, char_key="kirche")
            # [TNDL       tndl(30)] — не переносится (система не реализована, AGENTS §6)
            # [lay6 hide]
            $ show_sprites(("s 3 sad"))

    # ==== SCENE 304 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("s 3 sad"))
    play music t29 fadein 1.0
    # [BG +43 → id(43)]
    $ fade_fx("id(43)")
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("s 1 sad"))
    voice "ch5.3_s_012"
    s "Well…."
    # JA[11659]: とほほ……。
    # [lay5 x=224]
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "s 1 sad"))
    voice "ch5.3_l_007"
    l "Well, what's done is done. We just have to cooperate, right?"
    # JA[6216]: まぁ、なってしまったものはしょうがないわ。 / わたし達が協力すればいいんでしょ？
    # [lay5 +392 → s 1 happy]
    $ show_sprites(("l 1 sad", "s 1 happy"))
    voice "ch5.3_s_013"
    s "Are you sure about this?"
    # JA[11660]: 本当にいいのか？
    # [lay1 +310 → l 1 shy]
    $ show_sprites(("l 1 shy", "s 1 happy"))
    voice "ch5.3_l_008"
    l "D-don't get the wrong idea. A theater, after all, is a place where lots of commoners gather, isn't it?"
    # JA[6217]: か、勘違いしないでよね。 / 劇場っていったら、平民がたくさん集まる / 場所なんでしょ？
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "s 1 happy"))
    voice "ch5.3_l_009"
    l "That means information about the bomb user would gather there too. If that's the reason… well, it should work out."
    # JA[6218]: だったら、爆弾使いの情報も集まるってこと / じゃない。 / そういう理由だったら、まぁ、なんとかなるわ。
    # [lay5 +390 → s 1]
    $ show_sprites(("l 1", "s 1"))
    voice "ch5.3_s_014"
    s "As expected of our master. When I do something, I do it right."
    # JA[11661]: さすが、ご主人様。 / やるときはやるぜ。
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "s 1"))
    voice "ch5.3_l_010"
    l "Hmph. Being praised doesn't get you anything. Everyone, how about it?"
    # JA[6219]: ふん。 / 褒めたって何もでないんだから。 / みんな、それでどう？
    # [lay5 hide]
    $ show_sprites(("l 1 angry"))
    # [lay6 +676 → k 1]
    $ show_sprites(("l 1 angry", "k 1"))
    voice "ch5.3_k_005"
    k "It can't be helped, then. Well, it'll work out somehow."
    # JA[3264]: しょうがないわね。 / まぁ、なるようになるわ。
    # [lay1 hide]
    $ show_sprites(("k 1"))
    # [lay0 +588 → t 1]
    $ show_sprites(("t 1", "k 1"))
    voice "ch5.3_t_001"
    t "…Understood."
    # JA[15577]: ……了解。
    # [lay6 hide]
    $ show_sprites(("t 1"))
    # [lay3 +852 → m 1]
    $ show_sprites(("t 1", "m 1"))
    voice "ch5.3_m_002"
    m "Well, just don't let it show."
    # JA[4078]: まぁ、バレないようにしてね。
    # [lay0 hide]
    $ show_sprites(("m 1"))
    # [lay4 +570 → g 2 angry]
    $ show_sprites(("g 2 angry", "m 1"))
    voice "ch5.3_g_002"
    g "H-huh? Am I the only one against it?"
    # JA[1511]: あ、あれ？ / 反対なのはぼくだけなのかい？
    # [lay3 hide]
    $ show_sprites(("g 2 angry"))
    # [lay5 +390 → s 1]
    $ show_sprites(("g 2 angry", "s 1"))
    th "Good — now's my chance to make a play for it!{#ch5_3_th_006}"
    # JA: （よし、たたみかけるなら今だ！）
    # [lay5 +425 → s 3 happy]
    $ show_sprites(("g 2 angry", "s 3 happy"))
    voice "ch5.3_s_015"
    s "With a beauty like Guiche-sama's… common girls might come running, you know?"
    # JA[11662]: ギーシュ様の美貌をもってすれば、 / 平民の女の子が寄ってくるかもよ？
    # [lay4 +557 → g 1 happy]
    $ show_sprites(("g 1 happy", "s 3 happy"))
    voice "ch5.3_g_003"
    g "Oh, really? No, I mean, common girls like that… I'm not especially interested."
    # JA[1512]: あ、そうかな？ / いや、平民の女の子なんて、 / 特に興味はないんだけどね。
    # [lay4 +568 → g 2 happy]
    $ show_sprites(("g 2 happy", "s 3 happy"))
    voice "ch5.3_g_004"
    g "Ahahahaha!"
    # JA[1513]: あははははっ。
    # [lay5 hide]
    $ show_sprites(("g 2 happy"))
    # [lay3 +856 → m 1 angry]
    $ show_sprites(("g 2 happy", "m 1 angry"))
    voice "ch5.3_m_003"
    m "Oh, come on… Guiche…"
    # JA[4079]: もー。 / ギーシュったら……。
    # [lay4 hide]
    $ show_sprites(("m 1 angry"))
    # [lay3 hide]
    $ show_sprites()
    # [lay7 +962 → ha 2]
    $ show_sprites(("ha 2"))
    voice "ch5.3_ha_002"
    ha "Everyone. Thank you. With this, it'll surely work out."
    # JA[2362]: 皆さん。 / ありがとうございます。 / これで、なんとかなります。
    # [lay7 x=224]
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "ha 2"))
    voice "ch5.3_l_011"
    l "Good, everyone. We start working hard from tomorrow!"
    # JA[6220]: いい、みんな。 / 明日から頑張るんだからね！
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay1 hide]
    $ show_sprites(("ha 2"))
    # [lay7 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")

    # ==== SCENE 305 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +88 → sky]
    $ fade_fx("sky", new_music="t18")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    th "The moment we step onto the stage, rehearsal starts out of nowhere{#ch5_3_th_007}"
    # JA: （俺達が舞台に上がると、 / 　いきなり練習が始まった）
    # [lay5 hide]
    # [BG hide]
    $ fade_fx("black")
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 x=304]
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1"))
    voice "ch5.3_w_001"
    w "All right, everyone, gather round."
    # JA[15928]: それじゃあ、みんな、集まって。
    voice "ch5.3_w_002"
    w "Before we get to explaining the rehearsal, let me tell you a little more about the finer details of 'The Maiden of the Twin Moons'."
    # JA[15929]: それでは練習の説明に入る前に / 『双月天女』のもう少し細かい内容の / 説明をするわ。
    voice "ch5.3_w_003"
    w "For now, it's an old story. In a certain country, an aged nobleman found a little girl in a forest on a hunt."
    # JA[15930]: 今は昔の物語。 / ある国で、年老いた貴族が、狩猟の途中の森で / 幼い少女を拾ったの。
    voice "ch5.3_w_004"
    w "The old noble couple, who had been blessed with no children, decided to raise that girl, Noelle, as their own."
    # JA[15931]: 子供に恵まれていなかった老貴族夫婦は、 / その少女ノエルをわが子として育てることに / したわ。
    voice "ch5.3_w_005"
    w "And then, ten years passed… Noelle grew into a beautiful lady, and many suitors appeared."
    # JA[15932]: それから１０年……。 / ノエルは美しい貴婦人に成長し、 / 多くの求婚者が現れるの。
    voice "ch5.3_w_006"
    w "But she kept turning those proposals down for all manner of reasons, and would become no one's wife."
    # JA[15933]: けれども、彼女はその求婚をさまざまな理由 / で断り続け、誰の妻にもなろうとしません。
    voice "ch5.3_w_007"
    w "Because she had regained her memories of childhood. And so, she learned the truth."
    # JA[15934]: なぜなら、彼女は幼い頃の記憶を / 取り戻していたの。 / そして、彼女は知ったわ。
    voice "ch5.3_w_008"
    w "That she was the hidden child of an enemy country's king…"
    # JA[15935]: 自分が敵国の王の隠し子だったことを……。
    # [lay20 x=-96]
    # [lay2 +506 → si 2 sad]
    $ show_sprites(("w 1", "si 2 sad"))
    voice "ch5.3_si_004"
    si "A-and what happens to her?"
    # JA[14781]: そ、それで彼女はどうなるのですか？
    voice "ch5.3_w_009"
    w "For now, that's as far as we've got. We're still undecided about the ending, I suppose?"
    # JA[15936]: とりあえず、今出来てるのはこのあたり / までなの。 / 最後はもう少し悩んでるところかな？
    voice "ch5.3_w_010"
    w "The climax scene we performed yesterday is only one of several possibilities."
    # JA[15937]: 昨日演じていたクライマックスのシーンは / あくまで、ひとつの案なのよ。
    voice "ch5.3_si_005"
    si "Is that so…."
    # JA[14782]: そうなんですか……。
    voice "ch5.3_w_011"
    w "For now, we'll start with basic training. I'll have the script finished before the real rehearsals begin, so wait for it."
    # JA[15938]: 当分は基礎練習を中心に始めてもらうわ。 / 実際の練習までには本を完成させておくから、 / 待っててね。
    # [lay20 hide]
    $ show_sprites(("si 2 sad"))
    # [lay2 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [BG +88 → sky]
    $ fade_fx("sky")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    th "And then the hellish special training began{#ch5_3_th_008}"
    # JA: （それから、血のでるような特訓が始まった）
    th "Walking practice, then pronunciation practice{#ch5_3_th_009}"
    # JA: （歩き方の練習に発音練習）
    th "It's a sight I saw often in the drama club, but I never thought I'd be the one made to do it{#ch5_3_th_010}"
    # JA: （演劇部でよく見た光景だけど。 / 　まさか、自分がやらされるとは思っても / 　みなかったな）
    # [lay5 hide]
    # [BG hide]
    $ fade_fx("black")
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay1 +317 → l 6 angry]
    $ show_sprites(("l 6 angry"))
    voice "ch5.3_l_012"
    l "…What is all this?!"
    # JA[6221]: ……なによこれ！
    voice "ch5.3_l_013"
    l "Why do I have to practice walking, why do I have to practice all these exaggerated gestures and poses!"
    # JA[6222]: なんでいちいち歩き方や、 / 大げさな身振り手振りの練習をしなくちゃ / いけないの！
    voice "ch5.3_l_014"
    l "And on top of that, diaphragmatic breathing and voice training!"
    # JA[6223]: それに腹式呼吸に発声練習って！
    # [lay1 x=-96]
    # [lay0 +638 → t 5 sad]
    $ show_sprites(("l 6 angry", "t 5 sad"))
    voice "ch5.3_t_002"
    t "I'm bad at voice training."
    # JA[15578]: 発声は苦手。
    # [lay0 hide]
    $ show_sprites(("l 6 angry"))
    # [lay20 +1061 → w 1]
    $ show_sprites(("l 6 angry", "w 1"))
    voice "ch5.3_w_012"
    w "There's a good reason for exaggerating your movements and giving them contrast."
    # JA[15939]: 動きをオーバーにしたりメリハリをつけるのは / ちゃんと理由があるのよ。
    voice "ch5.3_w_013"
    w "When you look at the stage from the audience, it's quite far away, and rather dark, isn't it? If your movements are too small, the audience won't see them."
    # JA[15940]: 客席から舞台を見た時、結構遠かったり / 暗かったりするでしょ？ / あまり動きが小さいと客席から見えないのよ。
    voice "ch5.3_w_014"
    w "By the way, the flashy stage costumes and makeup are for the same reason."
    # JA[15941]: ちなみに、舞台衣装や化粧が派手なのも / 同じ理由。
    # [lay20 hide]
    $ show_sprites(("l 6 angry"))
    # [lay6 +689 → k 2 happy]
    $ show_sprites(("l 6 angry", "k 2 happy"))
    voice "ch5.3_k_006"
    k "Fuuun. It's true, from a distance small things are hard to make out. Isn't that right, Louise?"
    # JA[3265]: ふ～～ん。 / 確かに、小さいと遠目では判らないものね。 / ね、ルイズ。
    # [lay1 +319 → l 6 sad]
    $ show_sprites(("l 6 sad", "k 2 happy"))
    voice "ch5.3_l_015"
    l "W-where are you even looking?!"
    # JA[6224]: ど、どこを見て言ってるのよ！
    # [lay6 hide]
    $ show_sprites(("l 6 sad"))
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("l 6 sad", "w 1 angry"))
    voice "ch5.3_w_015"
    w "Besides, a theater is a large space. If you want your voice to reach the whole audience, you need an enormous volume."
    # JA[15942]: それに、劇場は広いのよ。 / 客席全体に声を届かせようと思ったら / 大変な声量が必要なの。
    # [lay20 +1067 → w 1 sad]
    $ show_sprites(("l 6 sad", "w 1 sad"))
    voice "ch5.3_w_016"
    w "Try performing every day. If you keep pushing your voice out of your throat, your throat will be ruined in no time!"
    # JA[15943]: 毎日公演してごらんなさい。 / のどで声を出してると、アッという間に / のどが潰れちゃうんだから！
    # [lay1 hide]
    $ show_sprites(("w 1 sad"))
    # [lay6 +693 → k 2 sad]
    $ show_sprites(("k 2 sad", "w 1 sad"))
    voice "ch5.3_k_007"
    k "I suppose I understand, but…"
    # JA[3266]: そりゃ分かるけど……。
    # [lay6 hide]
    $ show_sprites(("w 1 sad"))
    # [lay4 +561 → g 1 sad]
    $ show_sprites(("g 1 sad", "w 1 sad"))
    voice "ch5.3_g_005"
    g "W-why, for the sake of commoners…"
    # JA[1514]: な、なんで平民なんかのために……。
    # [lay20 +1061 → w 1]
    $ show_sprites(("g 1 sad", "w 1"))
    voice "ch5.3_w_017"
    w "Before we break, there's one thing to say. Mademoiselle Vallière!"
    # JA[15944]: 休憩の前にひとつ話しがあるの。 / ミス・ヴァリエール！
    # [lay4 hide]
    $ show_sprites(("w 1"))
    # [lay1 +317 → l 6 angry]
    $ show_sprites(("l 6 angry", "w 1"))
    voice "ch5.3_l_016"
    l "What now! More acting lessons?!"
    # JA[6225]: もう、なによ！ / また演技指導！？
    voice "ch5.3_w_018"
    w "No, rather, it seems a friend of Mademoiselle Vallière wishes to take part in the performance uninvited…"
    # JA[15945]: いいえ、ミス・ヴァリエールの知り合いだと / いう方が、飛び入り参加を希望されてるの / だけれど……。
    # [lay1 +319 → l 6 sad]
    $ show_sprites(("l 6 sad", "w 1"))
    voice "ch5.3_l_017"
    l "…A friend? Who?"
    # JA[6226]: ……知り合い？ / 誰？
    stop music fadeout 1.0
    # [lay20 hide]
    $ show_sprites(("l 6 sad"))
    # [lay1 hide]
    $ show_sprites()
    # [BG hide] — поглощается переходом на CG
    # [EVENT_CG +256 → id(256)]
    $ fade_fx("id(256)", type="cg", new_music="t29")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    voice "ch5.3_h_001"
    unk_h "It is I. Louise."
    # JA[569]: わたくしよ。 / ルイズ。
    voice "ch5.3_l_018"
    l "…Eh? A-aaaah!"
    # JA[6227]: ……えっ？ / あ、あああっ！
    th "Hold on. Why is a princess here?!{#ch5_3_th_011}"
    # JA: （ちょっと待て。 / 　なんで、お姫さまがここに来てるんだよ！）
    voice "ch5.3_h_002"
    h "'A friend' — just because we met in an unexpected place, you don't have to be so startled…"
    # JA[570]: 『お友達』に意外なところで会ったからって、 / そんなに驚かなくてもいいのに……。
    voice "ch5.3_l_019"
    l "U-um…{#ch5_3_v6228}"
    # JA[6228]: え、ええと……。
    th "'A friend'… I suppose she means a ninja{#ch5_3_th_012}"
    # JA: （『お友達』って……。 / 　つまり、お忍びだって言いたいのか）
    th "Even so… W-what are you thinking?! Th-that princess, she…!{#ch5_3_th_013}"
    # JA: （それにしたって……。 / 　な、なに考えてるんだよ！ / 　あの、お姫さまは！）
    voice "ch5.3_w_019"
    w "You are a student of the Academy as well? I feel as though I've seen you somewhere?"
    # JA[15946]: こちらも魔法学院の生徒？ / どこかでお見かけしたような気が？
    voice "ch5.3_l_020"
    l "Y-yes. She isn't a student of the Academy, but… she's my childhood friend… or rather, my best friend."
    # JA[6229]: え、ええ。 / 魔法学院の生徒ではないのですが、 / わたしの、幼馴染……というか親友です。
    voice "ch5.3_w_020"
    w "Hm.{#ch5_3_v15947}"
    # JA[15947]: ふーん。
    voice "ch5.3_w_021"
    w "Your name is… 'Rietta', as I heard — that's right, isn't it?"
    # JA[15948]: 名前は……、聞いたとおり「リエッタ」で / いいんですね？
    voice "ch5.3_h_003"
    h "Yes. Please call me Rietta from now on."
    # JA[571]: はい。 / 今後、リエッタとお呼びください。
    th "That's hardly a cover! You could at least put a little spin on it{#ch5_3_th_014}"
    # JA: （それってバレバレだろ！ / 　もう少しひねれっつーの）
    voice "ch5.3_h_004"
    h "Familiar-san."
    # JA[572]: 使い魔さん。
    voice "ch5.3_s_016"
    s "Y-yes!{#ch5_3_v11663}"
    # JA[11663]: は、はい！
    voice "ch5.3_h_005"
    h "…Even if my face is somewhat known, people don't recognize me as easily as you'd think. Hehehe."
    # JA[573]: ……顔が多少知られていても、 / 意外とバレないものですね。 / ふふふっ。

    # ---- 【選択肢】 ----
    menu:
        "S-so, exactly":
            # JA: そ、そうですね
            # ==== SCENE 306 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            play music t29 fadein 1.0
            # [EVENT_CG +256 → id(256)]
            $ fade_fx("id(256)", type="cg")
            voice "ch5.3_s_017"
            s "…S-so, exactly."
            # JA[11664]: ……そ、そうですね。
            voice "ch5.3_h_006"
            h "Or is it the clothes?"
            # JA[574]: それとも服のせいかしら？
            voice "ch5.3_s_018"
            s "Y-yes…{#ch5_3_v11665}"
            # JA[11665]: は、はあ……。
            th "Truly, is everything all right?{#ch5_3_th_015}"
            # JA: （ほ、本当に大丈夫なのか？）
            # [SET        set("se1", {stop = 1})] — SE не портируется
            stop music fadeout 1.0
            # [lay20 hide]
            # [lay8 hide]
            # [lay5 hide]
            # [lay1 hide]
            # [EVENT_CG hide]
            $ fade_fx("black")
        "That's just how it is…":
            # JA: そりゃだって……
            # ==== SCENE 307 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            play music t29 fadein 1.0
            # [EVENT_CG +256 → id(256)]
            $ fade_fx("id(256)", type="cg")
            voice "ch5.3_s_019"
            s "…That's just how it is. No one would ever expect to find you in a place like this."
            # JA[11666]: ……そりゃだって。 / まさかこんな場所におられるなんて / 誰も思いませんよ。
            voice "ch5.3_s_020"
            s "Besides, the only people who've ever seen you this close up are people of real standing, aren't they?"
            # JA[11667]: それに、ここまで近くで見たことが / ある人なんて、本当に地位のある人 / だけなんでしょ？
            voice "ch5.3_h_007"
            h "Ufufufu…{#ch5_3_v575}"
            # JA[575]: うふふ……。
            $ update_sympathy(30, char_key="henrietta")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            th "As I thought, she really is a friend of Louise, at least…{#ch5_3_th_016}"
            # JA: （やっぱり、この人はルイズの友達なだけは / 　あるよ……）
            # [SET        set("se1", {stop = 1})] — SE не портируется
            stop music fadeout 1.0
            # [lay20 hide]
            # [lay8 hide]
            # [lay5 hide]
            # [lay1 hide]
            # [EVENT_CG hide]
            $ fade_fx("black")
        "Are you sure it's all right?":
            # JA: 大丈夫なんですか？
            # ==== SCENE 308 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            play music t29 fadein 1.0
            # [EVENT_CG +256 → id(256)]
            $ fade_fx("id(256)", type="cg")
            voice "ch5.3_s_021"
            s "A-are you sure it's all right?"
            # JA[11668]: だ、大丈夫なんですか？
            voice "ch5.3_h_008"
            h "It's perfectly fine. I have permission from the castle. Only from the upper levels, of course."
            # JA[576]: 大丈夫です。 / お城には許可を取っています。 / もちろん、上層部だけですけど。
            voice "ch5.3_h_009"
            h "This is a s-e-c-r-e-t. So you understand!"
            # JA[577]: これは、ひ・み・つ。 / ですからね！
            $ update_sympathy(30, char_key="henrietta")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            voice "ch5.3_s_022"
            s "Y-yes!{#ch5_3_v11669}"
            # JA[11669]: は、はいっ！
            th "Truly, is everything all right?{#ch5_3_th_017}"
            # JA: （ほ、本当に大丈夫なのかよ？）
            # [SET        set("se1", {stop = 1})] — SE не портируется
            stop music fadeout 1.0
            # [lay20 hide]
            # [lay8 hide]
            # [lay5 hide]
            # [lay1 hide]
            # [EVENT_CG hide]
            $ fade_fx("black")

    # ==== SCENE 310 (переход после вариантов) ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +54 → id(54)]
    $ fade_fx("id(54)", new_music="t22")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1"))
    voice "ch5.3_w_022"
    w "The young Princess Noelle, caught up in a struggle for power in a neighboring country, was secretly smuggled away by a loyal retainer."
    # JA[15949]: 隣国での権力争いに巻き込まれた / 幼いノエル王女は、忠臣の手で密かに / 逃がされた。
    voice "ch5.3_w_023"
    w "However, lost in the deep forest, she was picked up by the old nobleman like a forgotten child, having lost her memory."
    # JA[15950]: しかし、深い森の中で迷う中で、 / 記憶を失い捨て子同然の姿で老貴族に拾われた。
    voice "ch5.3_w_024"
    w "…A girl who sighed every night as she gazed at the two moons in the sky."
    # JA[15951]: ……毎夜、天空の二つの月を眺めては / ため息をつく少女。
    voice "ch5.3_w_025"
    w "That if she involved herself, something bad would happen. Within her lost memories, the girl was aware of it."
    # JA[15952]: 自分に関われば良くないことが起こる。 / 失われた記憶の中で、少女はそれを / 自覚していた。
    voice "ch5.3_w_026"
    w "Noelle, who kept turning down proposals by posing impossible questions. But her meeting with Prince Cain, who had heard the rumors, began the tragedy."
    # JA[15953]: 無理難題を言って求婚を断り続けるノエル。 / しかし、噂を聞きつけた王子ケインとの / 出会いが、悲劇の始まりだった。
    voice "ch5.3_w_027"
    w "Yes, the two of them fell in love. That's where we left off last time."
    # JA[15954]: そう、２人は恋に落ちてしまった。 / というのが前回の続きね。
    # [lay20 x=-96]
    # [lay6 +693 → k 2 sad]
    $ show_sprites(("w 1", "k 2 sad"))
    voice "ch5.3_k_008"
    k "That's all very well, but I'm sick of voice training."
    # JA[3267]: それはいいんだけど、 / もう発声練習は飽き飽きよ。
    # [lay20 hide]
    $ show_sprites(("k 2 sad"))
    # [lay3 +869 → m 2 sad]
    $ show_sprites(("m 2 sad", "k 2 sad"))
    voice "ch5.3_m_004"
    m "All that running about and jumping on stage… I never imagined it would take so much exertion…"
    # JA[4080]: 舞台の上で飛んだり跳ねたりとか、 / まさかこんなに運動量が必要だなんて……。
    # [lay6 hide]
    $ show_sprites(("m 2 sad"))
    # [lay0 +638 → t 5 sad]
    $ show_sprites(("m 2 sad", "t 5 sad"))
    th "…….{#ch5_3_th_018}"
    # JA: ……。
    # [lay3 hide]
    $ show_sprites(("t 5 sad"))
    # [lay2 +506 → si 2 sad]
    $ show_sprites(("si 2 sad", "t 5 sad"))
    voice "ch5.3_si_006"
    si "…Acting is harder than I expected."
    # JA[14783]: ……お芝居って意外と大変なんですねぇ。
    # [lay0 hide]
    $ show_sprites(("si 2 sad"))
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("si 2 sad", "w 1 angry"))
    voice "ch5.3_w_028"
    w "Come, come! Stop chattering!"
    # JA[15955]: ほらほら！ / 無駄口を叩かない！
    voice "ch5.3_w_029"
    w "If you've got time to complain, make the foundations your own!"
    # JA[15956]: 文句を言ってる暇があったら、みっちりと / 基礎を身につけることよ！
    voice "ch5.3_w_030"
    w "On stage, titles like noble or commoner are of no use at all!"
    # JA[15957]: 舞台の上では、貴族だ、平民だ、 / なんていう肩書きは役に立たないんだからね！
    # [lay2 hide]
    $ show_sprites(("w 1 angry"))
    # [lay6 +693 → k 2 sad]
    $ show_sprites(("k 2 sad", "w 1 angry"))
    voice "ch5.3_k_009"
    k "I'm not in the mood today. I'll go up ahead."
    # JA[3268]: 今日は気が乗らないの。 / 先に上がらせてもらうわ。
    stop music fadeout 1.0
    play music t29 fadein 1.0
    # [lay20 +1067 → w 1 sad]
    $ show_sprites(("k 2 sad", "w 1 sad"))
    voice "ch5.3_w_031"
    w "W-wait!"
    # JA[15958]: ちょ、ちょっと！
    # [lay6 +687 → k 2]
    $ show_sprites(("k 2", "w 1 sad"))
    voice "ch5.3_k_010"
    k "If I want to build the foundations, I don't have to practice here. Self-practice, self-practice."
    # JA[3269]: 基礎をつけるなら、別にここで練習しなくても / いいじゃない。 / 自主練習よ、自主練習。
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("k 2", "w 1 angry"))
    voice "ch5.3_w_032"
    w "Fine. Go out. If you have no heart for it, you're not needed."
    # JA[15959]: いいわ、出て行きなさい。 / やる気がないのなら、いなくてもいいわ。
    # [lay6 hide]
    $ show_sprites(("w 1 angry"))
    # [lay4 +572 → g 2 sad]
    $ show_sprites(("g 2 sad", "w 1 angry"))
    voice "ch5.3_g_006"
    g "Then I'll…."
    # JA[1515]: じゃあ、ぼくも……。
    # [lay20 hide]
    $ show_sprites(("g 2 sad"))
    # [lay3 +869 → m 2 sad]
    $ show_sprites(("g 2 sad", "m 2 sad"))
    voice "ch5.3_m_005"
    m "…Wait a moment, you there! Guiche!"
    # JA[4081]: ……ちょっと、待ちなさいよ！ / ギーシュ！
    # [lay4 hide]
    $ show_sprites(("m 2 sad"))
    # [lay2 +506 → si 2 sad]
    $ show_sprites(("si 2 sad", "m 2 sad"))
    voice "ch5.3_si_007"
    si "E-everyone, calm down! After all we've worked this hard to get here."
    # JA[14784]: み、みなさん、落ち着いてください！ / ここまで頑張ってやってきたのに。

    # ==== SCENE 310 ====

    # ---- 【選択肢】 ----
    menu:
        "Stop Kirche":
            # JA: キュルケを止める
            # ==== SCENE 311 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay3 +869 → m 2 sad]
            $ show_sprites(("m 2 sad"))
            # [lay2 +506 → si 2 sad]
            $ show_sprites(("si 2 sad", "m 2 sad"))
            play music t29 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay2 hide]
            $ show_sprites(("m 2 sad"))
            # [lay3 hide]
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            voice "ch5.3_s_023"
            s "Kirche! W-wait a moment…"
            # JA[11670]: キュルケ！ / ちょ、ちょっと……。
            # [lay5 x=224]
            # [lay0 +638 → t 5 sad]
            $ show_sprites(("t 5 sad", "s 3 sad"))
            th "…….{#ch5_3_th_019}"
            # JA: ……。
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("t 5 sad", "s 1 sad"))
            voice "ch5.3_s_024"
            s "T-Tabitha! If we don't stop Kirche…"
            # JA[11671]: タ、タバサ！ / キュルケを止めないと……。
            # [lay0 +632 → t 5]
            $ show_sprites(("t 5", "s 1 sad"))
            voice "ch5.3_t_003"
            t "It's fine."
            # JA[15579]: 大丈夫。
            $ update_sympathy(15, char_key="tabitha")
            voice "ch5.3_s_025"
            s "B-but!"
            # JA[11672]: で、でも！
            # [lay5 hide]
            $ show_sprites(("t 5"))
            # [lay0 hide]
            $ show_sprites()
        "Stop Montmorency":
            # JA: モンモンを止める
            # ==== SCENE 312 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay3 +869 → m 2 sad]
            $ show_sprites(("m 2 sad"))
            # [lay2 +506 → si 2 sad]
            $ show_sprites(("si 2 sad", "m 2 sad"))
            play music t29 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay2 hide]
            $ show_sprites(("m 2 sad"))
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("s 1 angry", "m 2 sad"))
            voice "ch5.3_s_026"
            s "M-Montmorency!"
            # JA[11673]: モ、モンモン！
            # [lay3 +867 → m 2 angry]
            $ show_sprites(("s 1 angry", "m 2 angry"))
            voice "ch5.3_m_006"
            m "I understand it's an emergency, but will you do something about the way you call him?"
            # JA[4082]: 緊急なのは分かるけど、 / その呼び方、そろそろ直してくださらない？
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad", "m 2 angry"))
            voice "ch5.3_s_027"
            s "S-sorry!"
            # JA[11674]: ご、ごめん！
            # [lay3 +863 → m 2]
            $ show_sprites(("s 3 sad", "m 2"))
            voice "ch5.3_m_007"
            m "…I know what you want to say. Don't worry."
            # JA[4083]: ……言いたいことは分かってるわ。 / 安心なさい。
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("s 1 sad", "m 2"))
            voice "ch5.3_s_028"
            s "…Y-yes. P-please do."
            # JA[11675]: ……は、はい。 / お願いしましゅ。
            # [lay5 hide]
            $ show_sprites(("m 2"))
            # [lay3 hide]
            $ show_sprites()
        "Don't chase after those who leave":
            # JA: 去るものは追わない
            # ==== SCENE 313 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay3 +869 → m 2 sad]
            $ show_sprites(("m 2 sad"))
            # [lay2 +506 → si 2 sad]
            $ show_sprites(("si 2 sad", "m 2 sad"))
            play music t29 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay2 hide]
            $ show_sprites(("m 2 sad"))
            # [lay3 hide]
            $ show_sprites()
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("s 1 sad"))
            th "Well, they say don't chase after those who leave, but…{#ch5_3_th_020}"
            # JA: （さ、去るものは追わずというけど……）
            th "This is bad…{#ch5_3_th_021}"
            # JA: （ヤバイよなあ……）
            # [lay5 hide]
            $ show_sprites()

    # ==== SCENE 314 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    play music t29 fadein 1.0
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [lay6 +687 → k 2]
    $ show_sprites(("k 2"))
    voice "ch5.3_k_011"
    k "…Oh? Louise is staying? How unexpected."
    # JA[3270]: ……あら、ルイズは残るの？ / 意外ね。
    # [lay6 x=-96]
    # [lay1 +313 → l 6]
    $ show_sprites(("k 2", "l 6"))
    voice "ch5.3_l_021"
    l "…I hate the way you make a scene in the middle of things. It looks like running away."
    # JA[6230]: ……あなたみたいに途中で音をあげるのは、 / 逃げ出すみたいで嫌いだし。
    # [lay6 +691 → k 2 angry]
    $ show_sprites(("k 2 angry", "l 6"))
    voice "ch5.3_k_012"
    k "…Hmph, I suppose. Then do your very best."
    # JA[3271]: ……ふん、だ。 / それじゃ、せいぜい頑張りなさい。
    # [lay1 hide]
    $ show_sprites(("k 2 angry"))
    # [lay6 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("s 3 sad"))
    th "Sigh… what a bind. Today's practice somehow got through, but Kirche hitting her limit, of all things…{#ch5_3_th_022}"
    # JA: （はぁ……困ったなぁ。 / 　今日の練習はなんとか終わったけど、 / 　キュルケが限界とは……）
    th "Now, what should I do?{#ch5_3_th_023}"
    # JA: （さて、どうしようかな？）
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [MOVEINIT   moveInit((0x01000000 +320),(0x02000000 +53),3,(0x03000000 +4))] — не портируется
    # [MAPDEST    moveItem("舞台", (0x02000000 +500), (0x01000000 +1383))] — не портируется
    # [MAPDEST    moveItem("劇場", (0x02000000 +632), (0x01000000 +1388))] — не портируется
    # [MAPDEST    moveItem("城前", (0x02000000 +962), (0x01000000 +1393))] — не портируется
    # [MAPDEST    moveItem("宿", (0x02000000 +687), (0x01000000 +1398))] — не портируется
    # [MAPDEST    moveItem("表通り", (0x02000000 +863), (0x01000000 +1403))] — не портируется
    # [MOVE       move()] — не портируется

    # [移動] → next(315): сцена 315 — часть 4 главы 5
    jump ch5_4

label ch5_3_sc309:
    # Сцена 309: «переход» движка пропуска (PS2). В потоке сцен
    #   недостижима — ветки 306–308 ведут сразу в 310; её события
    #   дублируются финалом веток. Текста нет.
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    play music t29 fadein 1.0
    # [EVENT_CG +256 → id(256)]
    $ fade_fx("id(256)", type="cg")
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay1 hide]
    # [lay20 hide]
    # [lay8 hide]
    # [lay5 hide]
    # [EVENT_CG hide]
    $ fade_fx("black")

    # [移動] → next(315): сцена 315 — часть 4 главы 5
    jump ch5_4
    return
