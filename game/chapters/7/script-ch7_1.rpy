# Глава 7, часть 1 (сцены 375-388): «失望のお姫さま» — титульная карточка-overlay K=12,
# интрига с бомбистом (Кирхе ведёт расследование театра), ночная вылазка
# к театру и столкновение с Уэзерби; три развилки (-choice) — части
# сливаются в общие сцены 379/384; третья развилка подводит к части 2.
# Источник: ps2_source/chapters/chapter_08_失望のお姫さま.txt (SCENE 375-388).
# Точные аргументы: ps2_source/events_full/chapter_08_失望のお姫さま.txt.
# Скелет собран генератором tools/gen_ch7_1_script.py (EN — tools/ch7_1_en.py,
#   RU — tools/ch7_1_ru.py), порядок реплик, голоса, спрайты и события
#   совпадают с источником; структура — из reports/_tmp_manifest.txt.
#
# Титульная карточка: K=12 (11 занято script-ch5_1.rpy). Вход — jump ch7
#   из главы 6; выход — jump ch7_2 (сцена 389) — E7 «forward debt»,
#   закроется частью 2.
#
# Голоса: ch7_<spk>_<NNN> — нумерация с 001 по говорящему, порядок порта
#   (375 → ветки 376/377/378 → 379 → 380 → ветки 381/382/383 → 384 → 385 →
#   ветки 386/387/388):
#   l ×37, s ×33, h ×22, k ×17, w ×18, t ×4, g ×3, si ×3, m ×2, ha ×1 —
#   всего 140. Мысли (th, без голоса) — 2, пункты меню — 9.
#
# Не портируются: ITEM ×3 (バナナ/ハート型チョコ/青汁 — инвентарь не реализован),
#   SE (se1 stop), MSGON/MSGOFF, beginSkip/endSkip, back(), waitTime/waitAction,
#   TRANS (переход выполняется fade_fx), BGU, TNDL — переносится (as tndl).
#
# Фоны/CG: id(41), id(53), id(54), id(264) — имена пусты в image_id_map
#   (заглушки id(K), требуют решения человека); 2/1145/1167 = титульный
#   монтаж (white/overlay/overlay, только в комментариях).
# Спрайты: id → имя по references/sprite_id_map.csv; PROVISIONAL (пиксель-
#   сверка недоступна — архив PS2 не подключён): 572 = g 2 sad, 621 = t 4,
#   1061 = w 1, 1063 = w 1 happy, 1065 = w 1 angry.
#
# Меню 【選択肢】: три развилки по три варианта (сцены 375, 380, 385) —
#   варианты разворачиваются внутрь пунктов меню, слияние — общая сцена
#   (379 / 384), как в script-ch5_1.rpy; третья развилка (сцена 385) уводит
#   в часть 2 (каждый вариант завершается jump ch7_2).
#
# Файл сгенерирован tools/gen_ch7_1_script.py — правки вносить в него
#   и в tools/ch7_1_en.py, затем перегенерировать.

label ch7:
    $ tndl(None)
    # Титульный монтаж (BG 2/1145/1167/1145/2) → overlay_screen (образ «overlay»).
    call overlay_screen("overlay", "Chapter Seven: 'The Disappointed Princess'{#ch7_title}", isUseBlur=False, text_mode="black") from _call_overlay_screen_12
    pause(2)


    # ==== SCENE 375 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [TITLE      title("失望のお姫さま")] — титульная карточка → overlay_screen
    # [SKIP       beginSkip()] — не портируется
    # [MSGOFF     msgoff()] — не портируется
    # [BACK       back()] — не портируется
    # [BG +2 — титульный монтаж → overlay_screen]
    # [TRANS   trans("crossfade", 500)] — переход выполняется fade_fx
    # [BACK       back()] — не портируется
    # [BG +1145 — титульный монтаж → overlay_screen]
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [BACK       back()] — не портируется
    # [BG +1167 — титульный монтаж → overlay_screen]
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [WAIT       waitTime(1200, true)] — не портируется
    # [BACK       back()] — не портируется
    # [BG +1145 — титульный монтаж → overlay_screen]
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [BACK       back()] — не портируется
    # [BG +2 — титульный монтаж → overlay_screen]
    # [TRANS   trans("crossfade", 2000)] — переход выполняется fade_fx
    # [endSkip    endSkip()] — не портируется
    # [ITEM      item("バナナ", 3)] — система инвентаря не реализована, вызов не переносится
    # [ITEM      item("ハート型チョコ", 3)] — система инвентаря не реализована, вызов не переносится
    # [ITEM      item("青汁", 3)] — система инвентаря не реализована, вызов не переносится
    # [BACK       back()] — не портируется
    # [BG +41 → id(41)]
    $ fade_fx("id(41)", new_music="t4")
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry"))
    # [MSGON      msgon()] — не портируется
    voice "ch7_l_001"
    l "Good grief! As it turns out, we went and wasted a whole day yesterday, all for nothing!{#ch7_l_001}"
    # JA[7341]: まったくもう！ / 結局、昨日はまるまる１日、 / 無駄に過ごしちゃったじゃないの！
    # [lay1 y=0,x=-96]
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("l 1 angry", "s 3 sad"))
    voice "ch7_s_001"
    s "Ah, no, I really am sorry about that.{#ch7_s_001}"
    # JA[13481]: あー、いや、それは本当にすまない。
    # [lay1 +339 → l 3 angry]
    $ show_sprites(("l 3 angry", "s 3 sad"))
    voice "ch7_l_002"
    l "Are you really reflecting on it?{#ch7_l_002}"
    # JA[7342]: 本当に反省してるの？
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("l 3 angry", "s 1 sad"))
    th "The Princess is the one who brought up going to see the town, so there's no way I could have stopped her.{#ch7_th_375a}"
    # JA: （お姫さまが街を見に行こうって / 言い出したのに、俺が止められるわけ / ないだろう）
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("l 3 angry", "s 3 sad"))
    th "Not that saying it would make her accept it — I know that too… Sigh.{#ch7_th_375b}"
    # JA: （って言っても納得してくれないのは / 分かってるしなあ。 / とほほ）
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "s 3 sad"))
    voice "ch7_l_003"
    l "Why are you just sitting there in silence, making all those faces? It's frankly unsettling.{#ch7_l_003}"
    # JA[7343]: なにを黙ったまま百面相してるのよ。 / なんだか気味悪いわね。
    # [lay1 hide]
    $ show_sprites(("s 3 sad"))
    # [lay5 hide]
    $ show_sprites()
    # [lay6 +676 → k 1]
    $ show_sprites(("k 1"))
    voice "ch7_k_001"
    k "You two are lively for this early in the morning.{#ch7_k_001}"
    # JA[3833]: 朝からにぎやかね、あんた達。
    # [lay6 +709 → k 4]
    $ show_sprites(("k 4"))
    voice "ch7_k_002"
    k "There's something important I want to talk about, if I may? It's about the bomb user.{#ch7_k_002}"
    # JA[3834]: 大事な話があるんだけど、いいかしら？ / 爆弾使いのことなんだけど。
    # [lay6 y=0,x=224]
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "k 4"))
    voice "ch7_l_004"
    l "……! Did you find something!?{#ch7_l_004}"
    # JA[7344]: ……！ / なにか分かったの！？
    # [lay6 +676 → k 1]
    $ show_sprites(("l 1 angry", "k 1"))
    voice "ch7_k_003"
    k "This is only at the stage of being suspicious, mind you.{#ch7_k_003}"
    # JA[3835]: これはあくまでも、疑わしいって / 段階の話だけど。
    voice "ch7_k_004"
    k "But I've thought of the perfect place for the bomb user to hole up in.{#ch7_k_004}"
    # JA[3836]: 爆弾使いが潜伏するのに、 / 最適な場所を思いついたの。
    # [lay1 hide]
    $ show_sprites(("k 1"))
    # [lay2 +489 → si 1]
    $ show_sprites(("k 1", "si 1"))
    voice "ch7_si_001"
    si "And where is that?{#ch7_si_001}"
    # JA[15156]: それってどこですか？
    # [lay6 +709 → k 4]
    $ show_sprites(("k 4", "si 1"))
    voice "ch7_k_005"
    k "The theater. Just to be thorough — I had already been looking into it since before, you know.{#ch7_k_005}"
    # JA[3837]: 劇場よ。 / 念のため、前から調べは進めていたんだけどね。
    # [lay2 hide]
    $ show_sprites(("k 4"))
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "k 4"))
    voice "ch7_l_005"
    l "Hold on. 'Since before'? How long have you suspected the theater?{#ch7_l_005}"
    # JA[7345]: ちょっと待って。 / 前からって、あんたいつから劇場を / 疑っていたの？
    # [lay1 hide]
    $ show_sprites(("k 4"))
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("s 3 sad", "k 4"))
    voice "ch7_s_002"
    s "Don't tell me you already suspected it back when we were helping out with the play?{#ch7_s_002}"
    # JA[13482]: ひょっとして、 / 俺達が劇を手伝っていた時から、 / 既に疑ってたってことか？
    # [lay6 +676 → k 1]
    $ show_sprites(("s 3 sad", "k 1"))
    voice "ch7_k_006"
    k "Yes, that's right.{#ch7_k_006}"
    # JA[3838]: ええ、そうよ。
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1", "k 1"))
    voice "ch7_s_003"
    s "I see. So that was the reason you stormed out mid-play faking a fit, too — to check the inside and the surroundings. {#ch7_s_003}"
    # JA[13483]: なるほどな。 / 途中でキレたふりして出て行ったのも、 / 内部や周辺を調べるためだったのか。
    # [lay6 +678 → k 1 happy]
    $ show_sprites(("s 1", "k 1 happy"))
    voice "ch7_k_007"
    k "Exactly. Her Majesty asked me to the moment she arrived, so I did my digging on the side.{#ch7_k_007}"
    # JA[3839]: そういうこと。 / 女王陛下がやってきてすぐに頼まれてね。 / 裏でいろいろ調べてたのよ。
    # [lay5 hide]
    $ show_sprites(("k 1 happy"))
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "k 1 happy"))
    voice "ch7_l_006"
    l "Kirche!? Is that true!?{#ch7_l_006}"
    # JA[7346]: キュルケ！？ / それ本当！？
    # [lay6 +676 → k 1]
    $ show_sprites(("l 1 angry", "k 1"))
    voice "ch7_k_008"
    k "What would lying to you accomplish? Feel free to have Her Majesty confirm it.{#ch7_k_008}"
    # JA[3840]: 嘘ついてどうするのよ。 / 女王陛下に確認してもらってもいいわよ。
    # [lay1 +339 → l 3 angry]
    $ show_sprites(("l 3 angry", "k 1"))
    voice "ch7_l_007"
    l "How could you keep something that important to yourself!? Is it that you think I can't be relied on?{#ch7_l_007}"
    # JA[7347]: なんで、そんな重要なことを言わないのよ！ / わたしじゃ頼りにならないってこと？
    # [lay6 hide]
    $ show_sprites(("l 3 angry"))
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("l 3 angry", "s 3 sad"))
    voice "ch7_s_004"
    s "Calm down, Louise.{#ch7_s_004}"
    # JA[13484]: 落ち着けよ、ルイズ。
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "s 3 sad"))
    voice "ch7_l_008"
    l "How could I possibly calm down!? Why would you entrust such an important duty to Kirche! And behind our backs, no less!{#ch7_l_008}"
    # JA[7348]: 落ち着いてなんかいられないわよ！ / なんでキュルケにそんな大事な役目を任せるの！ / しかも、わたし達に内緒で！
    # [lay5 +390 → s 1]
    $ show_sprites(("l 1 angry", "s 1"))
    voice "ch7_s_005"
    s "That's… well…{#ch7_s_005}"
    # JA[13485]: それは……。

    # ---- 【選択肢】 ----
    menu:
        "Because Kirche was the one for the job.{#ch7_c376}":
            # JA: キュルケが適役だったから
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1"))
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry", "s 1"))
            # [BGM play=+5 → t4] — музыка раньше фона
            play music t4 fadein 1.0
            # [BG +41 → id(41)]
            $ fade_fx("id(41)")
            # [lay5 +423 → s 3]
            $ show_sprites(("l 1 angry", "s 3"))
            voice "ch7_s_006"
            s "It's because Kirche was the one for the job, obviously.{#ch7_s_006}"
            # JA[13486]: キュルケが適役だったからだろ。
            # [lay1 +302 → l 1]
            $ show_sprites(("l 1", "s 3"))
            voice "ch7_l_009"
            l "What exactly makes Kirche 'the one'?{#ch7_l_009}"
            # JA[7349]: キュルケのどこが？
            # [lay5 +390 → s 1]
            $ show_sprites(("l 1", "s 1"))
            voice "ch7_s_007"
            s "Well, more than anything, how good she is at handling people. Her feminine wiles especially.{#ch7_s_007}"
            # JA[13487]: ま、なんと言っても人あしらいのうまさだな。 / 特に色仕掛けとか。
            # [lay5 hide]
            $ show_sprites(("l 1"))
            # [lay6 +678 → k 1 happy]
            $ show_sprites(("l 1", "k 1 happy"))
            voice "ch7_k_009"
            k "That's beyond you, Louise.{#ch7_k_009}"
            # JA[3841]: ルイズには無理よね。
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry", "k 1 happy"))
            voice "ch7_l_010"
            l "What did you just say!?{#ch7_l_010}"
            # JA[7350]: なんですってえ！？
            # [lay6 +676 → k 1]
            $ show_sprites(("l 1 angry", "k 1"))
            # [移動] → next(379)

        "Because I felt uneasy leaving it to Louise.{#ch7_c377}":
            # JA: ルイズに任せるのは不安だったから
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1"))
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry", "s 1"))
            # [BGM play=+5 → t4] — музыка раньше фона
            play music t4 fadein 1.0
            # [BG +41 → id(41)]
            $ fade_fx("id(41)")
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("l 1 angry", "s 3 sad"))
            voice "ch7_s_008"
            s "It's because leaving it to you made me uneasy.{#ch7_s_008}"
            # JA[13488]: ルイズに任せるのは不安だったからだろ。
            # [lay1 +306 → l 1 angry]
            voice "ch7_l_011"
            l "What did you just say!?{#ch7_l_011}"
            # JA[7351]: なんですってえ！？
            $ tndl(-40)
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("l 1 angry", "s 1 sad"))
            voice "ch7_s_009"
            s "There, see? You fly into a rage at the slightest thing. Investigating is hard when you're that short-tempered.{#ch7_s_009}"
            # JA[13489]: ほら、そうやってすぐ怒る。 / 短気だと調査って難しいだろ。
            # [lay1 +341 → l 3 sad]
            $ show_sprites(("l 3 sad", "s 1 sad"))
            voice "ch7_l_012"
            l "Uuuugh. The last person I want to hear that from is you.{#ch7_l_012}"
            # JA[7352]: ううう。 / あんたにだけは言われたくないわよ。
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("l 3 sad", "s 1 angry"))
            voice "ch7_s_010"
            s "W-why!?{#ch7_s_010}"
            # JA[13490]: な、なんでだよ！
            # [lay5 hide]
            $ show_sprites(("l 3 sad"))
            # [lay6 +676 → k 1]
            $ show_sprites(("l 3 sad", "k 1"))
            # [移動] → next(379)

        "Just… because.{#ch7_c378}":
            # JA: なんとなく
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1"))
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry", "s 1"))
            # [BGM play=+5 → t4] — музыка раньше фона
            play music t4 fadein 1.0
            # [BG +41 → id(41)]
            $ fade_fx("id(41)")
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("l 1 angry", "s 3 sad"))
            voice "ch7_s_011"
            s "No particular reason.{#ch7_s_011}"
            # JA[13491]: なんとなく。
            # [lay1 +302 → l 1]
            $ show_sprites(("l 1", "s 3 sad"))
            voice "ch7_l_013"
            l "Honestly. What is that even supposed to mean, 'no particular reason'?{#ch7_l_013}"
            # JA[7353]: ちょっと。 / なんとなくってなによ、なんとなくって。
            # [lay5 +423 → s 3]
            $ show_sprites(("l 1", "s 3"))
            voice "ch7_s_012"
            s "'No particular reason' is a handy little phrase. Doesn't it make everything sound resolved?{#ch7_s_012}"
            # JA[13492]: 便利な言葉だよな、なんとなく。 / なんでも解決したっぽくない？
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry", "s 3"))
            voice "ch7_l_014"
            l "As if that could resolve anything!{#ch7_l_014}"
            # JA[7354]: そんなわけないでしょ！
            # [lay5 hide]
            $ show_sprites(("l 1 angry"))
            # [lay6 +676 → k 1]
            $ show_sprites(("l 1 angry", "k 1"))
            # [移動] → next(379)


    # ==== SCENE 379 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry"))
    # [lay6 +676 → k 1]
    $ show_sprites(("l 1 angry", "k 1"))
    # [BGM play=+5 → t4] — музыка раньше фона
    play music t4 fadein 1.0
    # [BG +41 → id(41)]
    $ fade_fx("id(41)")
    voice "ch7_k_010"
    k "Louise had Louise's role, and I had mine. So please don't take it out on Her Majesty.{#ch7_k_010}"
    # JA[3842]: ルイズにはルイズの、あたしにはあたしの / 役割があったってことよ。 / そのことについて女王陛下を責めないであげて。
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "k 1"))
    voice "ch7_l_015"
    l "……{#ch7_l_015}"
    # JA[7355]: ……。
    # [lay6 hide]
    $ show_sprites(("l 1 sad"))
    # [lay8 +781 → h 3 sad]
    $ show_sprites(("l 1 sad", "h 3 sad"))
    voice "ch7_h_001"
    h "Louise… I'm sorry.{#ch7_h_001}"
    # JA[813]: ルイズ……。 / ごめんなさい。
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "h 3 sad"))
    voice "ch7_l_016"
    l "No, not at all. If that is what Your Highness has decided, I have nothing to say.{#ch7_l_016}"
    # JA[7356]: いえ、いいんです。 / それが姫さまが決めたことなら、 / わたしは何も言いません。
    # [lay8 hide]
    $ show_sprites(("l 1"))
    # [lay1 hide]
    $ show_sprites()
    # [lay6 +676 → k 1]
    $ show_sprites(("k 1"))
    voice "ch7_k_011"
    k "Now, as for what the investigation turned up…{#ch7_k_011}"
    # JA[3843]: 調査の結果判明したことだけど……。
    # [lay6 y=0,x=-96]
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("s 1 angry", "k 1"))
    voice "ch7_s_013"
    s "So there was something suspicious after all.{#ch7_s_013}"
    # JA[13493]: なにか怪しい点があったんだな。
    voice "ch7_k_012"
    k "Yes. For one thing, that theater sees more people coming and going than an actual production would need.{#ch7_k_012}"
    # JA[3844]: ええ。 / まず、あの劇場は、実際の公演に必要な / 人手以上に、人間の出入りがあるわ。
    # [lay6 +682 → k 1 sad]
    $ show_sprites(("s 1 angry", "k 1 sad"))
    voice "ch7_k_013"
    k "And another thing — for a little playhouse serving commoners, quite a few people of rather high station have been coming and going there.{#ch7_k_013}"
    # JA[3845]: それにね、庶民相手の芝居小屋にしては、 / どうも身分が高そうな人達も出入りしてるの。
    # [lay5 hide]
    $ show_sprites(("k 1 sad"))
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "k 1 sad"))
    voice "ch7_l_017"
    l "Huh? You mean…{#ch7_l_017}"
    # JA[7357]: え？ / それって……。
    # [lay6 +676 → k 1]
    $ show_sprites(("l 1", "k 1"))
    voice "ch7_k_014"
    k "Incognito, presumably, but most likely nobles of Tristain itself.{#ch7_k_014}"
    # JA[3846]: お忍びだろうけど、おそらくトリステイン国内の / 貴族達でしょうね。
    # [lay6 hide]
    $ show_sprites(("l 1"))
    # [lay1 hide]
    $ show_sprites()
    # [lay8 +781 → h 3 sad]
    $ show_sprites(("h 3 sad"))
    voice "ch7_h_002"
    h "So… it is as I thought.{#ch7_h_002}"
    # JA[814]: やはり……そうですか。
    # [lay8 y=0,x=-96]
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("s 1 sad", "h 3 sad"))
    voice "ch7_s_014"
    s "Your Highness? Do you know something about this?{#ch7_s_014}"
    # JA[13494]: お姫さま？ / なんか知ってるんですか？
    voice "ch7_h_003"
    h "……{#ch7_h_003}"
    # JA[815]: ……。
    # [MSGOFF     msgoff()] — не портируется
    # [SET       set("se1", {stop = 1})] — SE не портируется
    # [BGM stop] — стоп музыки
    stop music fadeout 1.0
    # [lay8 hide]
    $ show_sprites(("s 1 sad"))
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [WAIT       waitTime(1000, true)] — не портируется
    # [移動] → next(380)

    # ==== SCENE 380 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BACK       back()] — не портируется
    # [BG +41 → id(41)]
    $ fade_fx("id(41)", new_music="t18")
    # [lay8 +781 → h 3 sad]
    $ show_sprites(("h 3 sad"))
    voice "ch7_h_004"
    h "They will most likely… sell me off in exchange for their own standing.{#ch7_h_004}"
    # JA[816]: おそらく……自分の地位と引き換えに、 / わたくしを売るつもりなのでしょう。
    # [lay8 y=0,x=224]
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "h 3 sad"))
    voice "ch7_l_018"
    l "Wh-what!? How could they even…!{#ch7_l_018}"
    # JA[7358]: ええっ！？ / な、なんてことなの……。
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "h 3 sad"))
    voice "ch7_l_019"
    l "There's no one who could be that reckless, never thinking of the consequences!{#ch7_l_019}"
    # JA[7359]: いくらなんだって、そこまで後先考えない / 人がいるなんて！
    # [lay1 +339 → l 3 angry]
    $ show_sprites(("l 3 angry", "h 3 sad"))
    voice "ch7_l_020"
    l "Destroying the royal house, descended from Founder Brimir, would only cause this land to lose Brimir's blessing!{#ch7_l_020}"
    # JA[7360]: 始祖ブリミルの後裔たる王家を滅ぼすことは、 / この国からブリミルの加護を失わせるだけです！
    # [lay8 +775 → h 3]
    $ show_sprites(("l 3 angry", "h 3"))
    voice "ch7_h_005"
    h "But listen, Louise. Quite a few voices wonder what a single queen can actually accomplish.{#ch7_h_005}"
    # JA[817]: でもね、ルイズ。 / 女王１人で何ができるのか、と / 疑問視する声は少なくないのです。
    # [lay8 +781 → h 3 sad]
    $ show_sprites(("l 3 angry", "h 3 sad"))
    voice "ch7_h_006"
    h "The ones among them who were impatient have evidently moved to act. That is what this must be.{#ch7_h_006}"
    # JA[818]: その中の、事を急ぐ人達が実際の行動に出た、 / そういうことなのでしょう。
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "h 3 sad"))
    voice "ch7_l_021"
    l "How… how utterly shallow of them! The nobles who are supposed to protect Your Highness… what a disgrace!{#ch7_l_021}"
    # JA[7361]: なんて……なんて浅はかなっ！ / 姫さまを守るべき貴族が……っ！ / なんてことを！
    voice "ch7_h_007"
    h "Louise…{#ch7_h_007}"
    # JA[819]: ルイズ……。
    # [lay1 +335 → l 3]
    $ show_sprites(("l 3", "h 3 sad"))
    voice "ch7_l_022"
    l "If that's how it is, then let's head straight to the theater!{#ch7_l_022}"
    # JA[7362]: そうと決まったら、 / さっそく劇場に行きましょう！
    # [lay1 hide]
    $ show_sprites(("h 3 sad"))
    # [lay8 hide]
    $ show_sprites()
    # [lay0 +588 → t 1]
    $ show_sprites(("t 1"))
    voice "ch7_t_001"
    t "No rushing.{#ch7_t_001}"
    # JA[15805]: 急いではだめ。
    # [lay0 y=0,x=-96]
    # [lay6 +676 → k 1]
    $ show_sprites(("k 1", "t 1"))
    voice "ch7_k_015"
    k "She's right. Going while it's still daylight would accomplish nothing but danger.{#ch7_k_015}"
    # JA[3847]: そうね。 / まだ日が明るいうちに行くのは危険なだけよ。
    # [lay0 +621 → t 4]
    $ show_sprites(("k 1", "t 4"))
    voice "ch7_t_002"
    t "And splitting into teams.{#ch7_t_002}"
    # JA[15806]: あと、チーム分け。
    # [lay6 hide]
    $ show_sprites(("t 4"))
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1", "t 4"))
    voice "ch7_s_015"
    s "So, we split into several groups and each enter the theater through one of its main entrances? That's more efficient, right?{#ch7_s_015}"
    # JA[13495]: ええと、つまり何組かに分かれて、 / 劇場の主な出入口から別々に入った方が、 / 効率的だってことか？
    # [lay0 +588 → t 1]
    $ show_sprites(("s 1", "t 1"))
    voice "ch7_t_003"
    t "{i}(Nods){/i}{#ch7_t_003}"
    # JA[15807]: （こくり）
    # [lay5 hide]
    $ show_sprites(("t 1"))
    # [lay4 +555 → g 1]
    $ show_sprites(("t 1", "g 1"))
    voice "ch7_g_001"
    g "I see — there's some sense to Tabitha's point. Then once night falls, we split up and each head for the theater.{#ch7_g_001}"
    # JA[1551]: なるほど、タバサの意見には一理あるな。 / それじゃ、夜になったら分かれてそれぞれ劇場へ / 向かうことにしよう。
    # [lay0 hide]
    $ show_sprites(("g 1"))
    # [lay6 +676 → k 1]
    $ show_sprites(("k 1", "g 1"))
    voice "ch7_k_016"
    k "And how do we split up?{#ch7_k_016}"
    # JA[3848]: それじゃ、どうやって分ける？
    # [lay4 hide]
    $ show_sprites(("k 1"))
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1", "k 1"))
    voice "ch7_s_016"
    s "Given the situation, pairs of two would do fine, no?{#ch7_s_016}"
    # JA[13496]: この際、２人１組でいいんじゃないか？
    # [lay6 +678 → k 1 happy]
    $ show_sprites(("s 1", "k 1 happy"))
    voice "ch7_k_017"
    k "True enough. Then I'm going with Tabitha.{#ch7_k_017}"
    # JA[3849]: そうね。 / それじゃ、あたしはタバサと行くわ。
    # [lay5 hide]
    $ show_sprites(("k 1 happy"))
    # [lay0 +588 → t 1]
    $ show_sprites(("k 1 happy", "t 1"))
    voice "ch7_t_004"
    t "Understood.{#ch7_t_004}"
    # JA[15808]: 分かった。
    # [lay6 hide]
    $ show_sprites(("t 1"))
    # [lay0 hide]
    $ show_sprites()
    # [lay3 +852 → m 1]
    $ show_sprites(("m 1"))
    # [lay4 +555 → g 1]
    $ show_sprites(("g 1", "m 1"))
    voice "ch7_m_001"
    m "Then that makes me and Guiche.{#ch7_m_001}"
    # JA[4164]: それじゃあ、わたしはギーシュね。
    # [lay4 +574 → g 2 shy]
    $ show_sprites(("g 2 shy", "m 1"))
    voice "ch7_g_002"
    g "Hmm — escorting Her Majesty myself is not a duty I would shirk, but if my beloved Montmorency asks for my support, then of course I shall go with her.{#ch7_g_002}"
    # JA[1552]: うむ、ぼくとしては女王陛下をお守りして行く / のもやぶさかではないが、愛するモンモランシー / が、ぼくを頼ってくれるなら、ぜひ同行しよう。
    # [lay3 +891 → m 4 sad]
    $ show_sprites(("g 2 shy", "m 4 sad"))
    voice "ch7_m_002"
    m "That's Guiche for you — somebody really does have to look after him.{#ch7_m_002}"
    # JA[4165]: このノリだもの、ギーシュのお守りが / 必要でしょ。
    # [lay4 hide]
    $ show_sprites(("m 4 sad"))
    # [lay3 hide]
    $ show_sprites()
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad"))
    voice "ch7_l_023"
    l "Good. Keep a close eye on him.{#ch7_l_023}"
    # JA[7363]: そうね、よく見張ってて。
    # [lay1 y=0,x=-96]
    # [lay4 +572 → g 2 sad]
    $ show_sprites(("l 1 sad", "g 2 sad"))
    voice "ch7_g_003"
    g "Ha-ha-ha-haa! Such remarkable trust! I swear I could weep!{#ch7_g_003}"
    # JA[1553]: はーっはっはっは！ / この信用の無さ！ / 泣けてくるね！
    # [lay4 hide]
    $ show_sprites(("l 1 sad"))
    # [lay5 +390 → s 1]
    $ show_sprites(("l 1 sad", "s 1"))
    voice "ch7_s_017"
    s "That leaves Louise and me, then.{#ch7_s_017}"
    # JA[13497]: それじゃ、残りはルイズと俺だな。
    # [lay1 hide]
    $ show_sprites(("s 1"))
    # [lay5 hide]
    $ show_sprites()
    # [lay2 +495 → si 1 sad]
    $ show_sprites(("si 1 sad"))
    voice "ch7_si_002"
    si "Um… and what am I supposed to do?{#ch7_si_002}"
    # JA[15157]: あの、わたしはどうしたらいいんでしょう？
    # [lay2 y=0,x=-96]
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1", "si 1 sad"))
    voice "ch7_s_018"
    s "Siesta and Haruna, you two stay here and keep the Princess company.{#ch7_s_018}"
    # JA[13498]: シエスタと春奈は、ここでお姫さまと一緒に / 留守番しててくれ。
    # [lay2 +493 → si 1 angry]
    $ show_sprites(("s 1", "si 1 angry"))
    voice "ch7_si_003"
    si "Y-yes.{#ch7_si_003}"
    # JA[15158]: は、はい。
    # [lay2 hide]
    $ show_sprites(("s 1"))
    # [lay7 +951 → ha 1]
    $ show_sprites(("s 1", "ha 1"))
    voice "ch7_ha_001"
    ha "Understood. Do be careful out there, Hiraga-kun.{#ch7_ha_001}"
    # JA[2633]: 分かった。 / 平賀くん、気をつけてね。
    # [lay7 hide]
    $ show_sprites(("s 1"))
    # [lay5 hide]
    $ show_sprites()
    # [lay8 +779 → h 3 angry]
    $ show_sprites(("h 3 angry"))
    voice "ch7_h_008"
    h "Wait, please. I will go with them as well.{#ch7_h_008}"
    # JA[820]: 待ってください。 / わたくしも共にまいります。
    # [lay8 y=0,x=224]
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "h 3 angry"))
    voice "ch7_l_024"
    l "You must not, Your Highness! We are about to storm what may well be the enemy's hideout.{#ch7_l_024}"
    # JA[7364]: それはいけませんわ！ / わたし達、これから敵のアジトかもしれない / 場所に乗り込もうとしているのですよ。
    # [lay8 +775 → h 3]
    $ show_sprites(("l 1", "h 3"))
    voice "ch7_h_009"
    h "Yes, I am fully aware of it.{#ch7_h_009}"
    # JA[821]: ええ、承知しています。
    voice "ch7_l_025"
    l "In that case, Your Highness, please stay here and look to your own safety. Storming in yourself is exactly what the enemy wants!{#ch7_l_025}"
    # JA[7365]: でしたら、姫さまはここでご自分の身を / お守りください。 / 御自らが乗り込むのは敵の思うつぼです！
    # [lay8 +775 → h 3]
    voice "ch7_h_010"
    h "It makes me happy that you worry, Louise. But this whole affair is my doing. It was I who asked you all to investigate.{#ch7_h_010}"
    # JA[822]: 心配してくれる気持ちは嬉しいわ、ルイズ。 / でも今回の一件、わたくしが原因。 / あなた達に調査を依頼したのもわたくしです。
    voice "ch7_h_011"
    h "I cannot send you all off into danger and remain idle in safety by myself.{#ch7_h_011}"
    # JA[823]: あなた達を危険な場所に向かわせて、 / わたくしだけが安全な場所で安穏としている / わけにはまいりません。

    # ---- 【選択肢】 ----
    menu:
        "Promise me you won't overdo it.{#ch7_c381}":
            # JA: 無理はしないと約束してください
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay8 +775 → h 3]
            $ show_sprites(("h 3"))
            # [lay1 +302 → l 1]
            $ show_sprites(("l 1", "h 3"))
            # [BGM play=+19 → t18] — музыка раньше фона
            play music t18 fadein 1.0
            # [BG +41 → id(41)]
            $ fade_fx("id(41)")
            # [lay1 hide]
            $ show_sprites(("h 3"))
            # [lay8 hide]
            $ show_sprites()
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1"))
            voice "ch7_s_019"
            s "Promise me you won't overdo it. If it gets dangerous, you run. Understood?{#ch7_s_019}"
            # JA[13499]: 無理はしないと約束してください。 / 危なくなったら、逃げる。 / いいですね？
            # [lay5 y=0,x=224]
            # [lay8 +775 → h 3]
            $ show_sprites(("s 1", "h 3"))
            voice "ch7_h_012"
            h "Then… that is acceptable, yes?{#ch7_h_012}"
            # JA[824]: では……よろしいのですね？
            # [lay8 hide]
            $ show_sprites(("s 1"))
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry", "s 1"))
            voice "ch7_l_026"
            l "Saito! Don't go deciding things all on your own!{#ch7_l_026}"
            # JA[7366]: ちょっとサイト！ / なに勝手に決めてるのよ！
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("l 1 angry", "s 3 sad"))
            voice "ch7_s_020"
            s "When Her Highness has put it that strongly, it's not something one can stop anymore.{#ch7_s_020}"
            # JA[13500]: お姫さまにここまで言われちゃ、 / 止められないじゃないか。
            # [移動] → next(384)

        "I will protect Your Highness.{#ch7_c382}":
            # JA: お姫さまは俺が守ります
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay8 +775 → h 3]
            $ show_sprites(("h 3"))
            # [lay1 +302 → l 1]
            $ show_sprites(("l 1", "h 3"))
            # [BGM play=+19 → t18] — музыка раньше фона
            play music t18 fadein 1.0
            # [BG +41 → id(41)]
            $ fade_fx("id(41)")
            # [lay1 hide]
            $ show_sprites(("h 3"))
            # [lay8 hide]
            $ show_sprites()
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1"))
            voice "ch7_s_021"
            s "Then it can't be helped. I will protect Your Highness.{#ch7_s_021}"
            # JA[13501]: 仕方ないです。 / お姫さまは俺が守ります。
            # [lay5 y=0,x=224]
            # [lay8 +777 → h 3 happy]
            $ show_sprites(("s 1", "h 3 happy"))
            voice "ch7_h_013"
            h "Oh… so it is acceptable, then?{#ch7_h_013}"
            # JA[825]: え……。 / それでは、よろしいのですね？
            # [lay8 hide]
            $ show_sprites(("s 1"))
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry", "s 1"))
            voice "ch7_l_027"
            l "Saito! Don't go deciding things all on your own!{#ch7_l_027}"
            # JA[7367]: ちょっとサイト！ / なに勝手に決めてるのよ！
            $ tndl(-40)
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("l 1 angry", "s 3 sad"))
            voice "ch7_s_022"
            s "When Her Highness has put it that strongly, it's not something one can stop anymore.{#ch7_s_022}"
            # JA[13502]: お姫さまにここまで言われちゃ、 / 止められないじゃないか。
            # [lay1 +308 → l 1 sad]
            $ show_sprites(("l 1 sad", "s 3 sad"))
            voice "ch7_l_028"
            l "Urgh, true enough, but…{#ch7_l_028}"
            # JA[7368]: うう、それはそうだけど……。
            # [移動] → next(384)

        "Please stay here quietly.{#ch7_c383}":
            # JA: おとなしく待っててください
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay8 +775 → h 3]
            $ show_sprites(("h 3"))
            # [lay1 +302 → l 1]
            $ show_sprites(("l 1", "h 3"))
            # [BGM play=+19 → t18] — музыка раньше фона
            play music t18 fadein 1.0
            # [BG +41 → id(41)]
            $ fade_fx("id(41)")
            # [lay1 hide]
            $ show_sprites(("h 3"))
            # [lay8 hide]
            $ show_sprites()
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("s 1 angry"))
            voice "ch7_s_023"
            s "Just sit tight and wait here, please!{#ch7_s_023}"
            # JA[13503]: いいからおとなしく待っててください！
            # [lay5 y=0,x=224]
            # [lay8 +779 → h 3 angry]
            $ show_sprites(("s 1 angry", "h 3 angry"))
            voice "ch7_h_014"
            h "That is not happening.{#ch7_h_014}"
            # JA[826]: そうはいきません。
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("s 1 sad", "h 3 angry"))
            voice "ch7_s_024"
            s "B-but if anything happens to Your Highness, the entire country is in jeopardy! I'm begging you, please wait here.{#ch7_s_024}"
            # JA[13504]: だ、だけど、お姫さまになにかあったら、 / この国がピンチなんですよ？ / お願いですから、ここで待っててくださいよ。
            voice "ch7_h_015"
            h "I refuse.{#ch7_h_015}"
            # JA[827]: 嫌です。
            # [lay8 hide]
            $ show_sprites(("s 1 sad"))
            # [lay1 +308 → l 1 sad]
            $ show_sprites(("l 1 sad", "s 1 sad"))
            voice "ch7_l_029"
            l "Haah… hopeless, Saito. Once Her Highness gets this stubborn, there is no changing her mind.{#ch7_l_029}"
            # JA[7369]: はあ……無理よ、サイト。 / ここまで意固地になっちゃったら、 / 姫さまが意見を変えるなんてありえないわ。
            $ tndl(50)
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("l 1 sad", "s 3 sad"))
            voice "ch7_s_025"
            s "Unbelievable…{#ch7_s_025}"
            # JA[13505]: なんてこった……。
            # [移動] → next(384)


    # ==== SCENE 384 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("s 3 sad"))
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "s 3 sad"))
    # [BGM play=+19 → t18] — музыка раньше фона
    play music t18 fadein 1.0
    # [BG +41 → id(41)]
    $ fade_fx("id(41)")
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "s 3 sad"))
    voice "ch7_l_030"
    l "Understood. My familiar and I shall serve as Your Highness's escort.{#ch7_l_030}"
    # JA[7370]: 分かりました。 / 姫さまの供はわたしと使い魔が、 / 勤めさせていただきます。
    # [lay1 +335 → l 3]
    $ show_sprites(("l 3", "s 3 sad"))
    voice "ch7_l_031"
    l "Whatever may come, we shall protect Your Highness.{#ch7_l_031}"
    # JA[7371]: 何があろうと、姫さまはわたし達が / お守りいたしますわ。
    # [lay5 hide]
    $ show_sprites(("l 3"))
    # [lay8 +775 → h 3]
    $ show_sprites(("l 3", "h 3"))
    voice "ch7_h_016"
    h "Thank you, Louise. I am grateful. I will take care not to get in your way.{#ch7_h_016}"
    # JA[828]: ありがとう、ルイズ。 / 感謝します。 / あなたがたの邪魔にならないよう気をつけます。
    # [lay1 hide]
    $ show_sprites(("h 3"))
    # [lay8 hide]
    $ show_sprites()
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("s 1 angry"))
    voice "ch7_s_026"
    s "Right! Then we wait for nightfall and storm the theater!{#ch7_s_026}"
    # JA[13506]: よし！ / それじゃ、夜を待って演劇場に乗り込むぞ！
    # [MSGOFF     msgoff()] — не портируется
    # [SET       set("se1", {stop = 1})] — SE не портируется
    # [BGM stop] — стоп музыки
    stop music fadeout 1.0
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [WAIT       waitTime(1000, true)] — не портируется
    # [移動] → next(385)

    # ==== SCENE 385 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BACK       back()] — не портируется
    # [BG +53 → id(53)]
    $ fade_fx("id(53)", new_music="t19")
    voice "ch7_l_032"
    l "I hardly noticed while we were helping out, but a theater at night with all the crowds gone is eerie.{#ch7_l_032}"
    # JA[7372]: 手伝っていたときはあまり気づかなかったけど、 / 夜の人気がなくなった劇場って、気味が悪いわね。
    # [BACK       back()] — не портируется
    # [lay1 hide]
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad"))
    # [lay8 +779 → h 3 angry]
    $ show_sprites(("l 1 sad", "h 3 angry"))
    voice "ch7_h_017"
    h "Doesn't something seem off to you?{#ch7_h_017}"
    # JA[829]: おかしくありませんか？
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "h 3 angry"))
    voice "ch7_l_033"
    l "Your Highness? What is the matter?{#ch7_l_033}"
    # JA[7373]: 姫さま？ / どうなさったんです？
    # [lay8 +781 → h 3 sad]
    $ show_sprites(("l 1", "h 3 sad"))
    voice "ch7_h_018"
    h "Even at night, there being so little as a trace of people around is…{#ch7_h_018}"
    # JA[830]: 夜とはいえ、ここまで人の気配がない / というのは……。
    # [lay1 hide]
    $ show_sprites(("h 3 sad"))
    # [lay8 hide]
    $ show_sprites()
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1"))
    voice "ch7_w_001"
    w "My, my, look who it is… What brings you here at this late hour?{#ch7_w_001}"
    # JA[16138]: おやおや、誰かと思ったら……。 / どうしたの、こんな夜更けに？
    # [lay20 y=0,x=224]
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "w 1"))
    voice "ch7_l_034"
    l "Weatherby!{#ch7_l_034}"
    # JA[7374]: ウェザリー！
    # [lay20 hide]
    $ show_sprites(("l 1 angry"))
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("l 1 angry", "s 2 angry"))
    voice "ch7_s_027"
    s "There's something I wanted to ask you about. That's why we've dropped in at this hour.{#ch7_s_027}"
    # JA[13507]: あんたに聞きたいことがあってね、 / こんな時間にお邪魔したってわけさ。
    # [lay1 hide]
    $ show_sprites(("s 2 angry"))
    # [lay5 hide]
    $ show_sprites()
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1"))
    voice "ch7_w_002"
    w "I see. Even so, sneaking in without so much as a greeting — isn't that rather rude?{#ch7_w_002}"
    # JA[16139]: なるほど。 / だからって挨拶もなしに / こっそり入って来るのは失礼じゃない？
    # [lay20 y=0,x=224]
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "w 1"))
    voice "ch7_l_035"
    l "Creeping about without a word of greeting started with you, if I may say. Now where have you hidden the bomb user?{#ch7_l_035}"
    # JA[7375]: 挨拶もなしにコソコソ動いてるのは、 / そちらが先じゃないのかしら。 / 爆弾使いはどこに隠したの？
    # [lay20 +1063 → w 1 happy]
    $ show_sprites(("l 1", "w 1 happy"))
    voice "ch7_w_003"
    w "Oh dear. So you saw through it after all.{#ch7_w_003}"
    # JA[16140]: あら、やっぱり見破られたのね。
    # [lay1 hide]
    $ show_sprites(("w 1 happy"))
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("s 2 angry", "w 1 happy"))
    voice "ch7_s_028"
    s "Who put you up to it? The one standing behind you — of what country, and who?{#ch7_s_028}"
    # JA[13508]: 誰の差し金だ？ / お前の背後にいるのは、 / いったいどこの国の、誰だ？
    # [lay20 +1061 → w 1]
    $ show_sprites(("s 2 angry", "w 1"))
    voice "ch7_w_004"
    w "First, shall I tell you an interesting story?{#ch7_w_004}"
    # JA[16141]: その前に面白い話をしましょうか。
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("s 2 angry", "w 1 angry"))
    voice "ch7_w_005"
    w "You see, the village I was born in has been officially ruled to have never existed. All because I existed.{#ch7_w_005}"
    # JA[16142]: わたしが生まれた村はね、 / 公式には存在しないことにされてしまったの。 / わたしが存在していたためにね。
    # [MSGOFF     msgoff()] — не портируется
    # [BGM stop] — стоп музыки
    stop music fadeout 1.0
    # [MSGOFF     msgoff()] — не портируется
    # [lay20 hide]
    $ show_sprites(("s 2 angry"))
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [WAIT       waitAction(null, true)] — не портируется
    # [MSGOFF     msgoff()] — не портируется
    # [BACK       back()] — не портируется
    # [EVENT_CG hide] — гаснет (без перехода)
    # [MSGON      msgon()] — не портируется
    voice "ch7_h_019"
    h "Huh…?{#ch7_h_019}"
    # JA[831]: え……？
    voice "ch7_w_006"
    w "I was raised by a noble father, and brought up as nobility.{#ch7_w_006}"
    # JA[16143]: わたしは、貴族の父に育てられて、 / 貴族として育ったわ。
    voice "ch7_w_007"
    w "My magic was considerable, too. I never slacked in my studies or my daily training.{#ch7_w_007}"
    # JA[16144]: 魔力も相当なものだったわ。 / 勉強も、日々の努力も怠らなかったからね。
    voice "ch7_w_008"
    w "But the moment my existence became known to the capital, everything changed. It was all denied.{#ch7_w_008}"
    # JA[16145]: でも、わたしの存在が都に知られた瞬間、 / 状況が一変したわ。 / 全てが否定されたのよ。
    voice "ch7_w_009"
    w "My father was persecuted, then killed. What's more, our whole family was stripped of its rank, and our property was confiscated.{#ch7_w_009}"
    # JA[16146]: 父は迫害され、殺され。 / しかも、一族すべての身分は剥奪され、 / 財産も没収されたわ。
    voice "ch7_h_020"
    h "You are a daughter of the beast-people, then. A child born between a noble and one of the beast-folk…{#ch7_h_020}"
    # JA[832]: あなたは、獣人の娘なのですね。 / 貴族と獣人の間に生まれた子……。
    voice "ch7_s_029"
    s "Beast-people?{#ch7_s_029}"
    # JA[13509]: 獣人？
    voice "ch7_h_021"
    h "The native people of Halkeginia. Because of all sorts of prejudice, they are often the ones persecuted.{#ch7_h_021}"
    # JA[833]: ハルケギニアの先住民族です。 / さまざまな偏見から、迫害を受けることが / 多いのです。
    voice "ch7_w_010"
    w "Hm? Persecution? Wrong — it was elimination.{#ch7_w_010}"
    # JA[16147]: あん？ / 迫害？ / 違うだろ、排除だろ？
    voice "ch7_w_011"
    w "To protect the nobles' standing, they loathe and eliminate every unlike element.{#ch7_w_011}"
    # JA[16148]: 貴族の地位を守るためには / あらゆる異分子を忌み嫌い、排除する。
    voice "ch7_w_012"
    w "If it were only me, so be it. That much could be put down to a personal grudge.{#ch7_w_012}"
    # JA[16149]: わたしだけなら、まだいいさ。 / 個人的な恨みで済まされるからね。
    voice "ch7_w_013"
    w "But look at what happened. They burned down every village my father held and drove out the inhabitants.{#ch7_w_013}"
    # JA[16150]: ところがどうだい。 / 父が持っていた村すべてを焼き払い、 / 住人を追い払ったのさ。
    voice "ch7_h_022"
    h "……{#ch7_h_022}"
    # JA[834]: ……。
    voice "ch7_w_014"
    w "And the princess over there — her station was built on just such sacrifice, and yet she simply lives at ease. Is that something to be permitted?{#ch7_w_014}"
    # JA[16151]: そこのお姫様は、そんな犠牲の上に作られた / 身分のはずなのに、ただ安穏と暮らしてる。 / そんなことが許されていいの？
    voice "ch7_w_015"
    w "I intend to turn this absurd world upside down. And I will not balk at any means to do it.{#ch7_w_015}"
    # JA[16152]: わたしとしてはこのふざけた世界を / ひっくり返したいの。 / そのためにはどんな手段でも選ばないわ。
    # [MSGOFF     msgoff()] — не портируется
    # [lay20 hide]
    # [lay8 hide]
    # [lay5 hide]
    # [BGU        show = 0] — не портируется
    # [EVENT_CG hide] — гаснет (без перехода)
    # [WAIT       waitAction(null, true)] — не портируется
    # [BACK       back()] — не портируется
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("w 1 angry"))
    # [MSGON      msgon()] — не портируется
    voice "ch7_w_016"
    w "You would know, wouldn't you, Saito? This world as seen from another world — how does it look?{#ch7_w_016}"
    # JA[16153]: サイトなら分かるでしょ？ / 異世界から見た、この世界はどう？
    # [lay20 y=0,x=-96]
    # [lay5 +407 → s 2 sad]
    $ show_sprites(("s 2 sad", "w 1 angry"))
    voice "ch7_s_030"
    s "That's…{#ch7_s_030}"
    # JA[13510]: それは……。

    # ---- 【選択肢】 ----
    menu:
        "I think I understand her.{#ch7_c386}":
            # JA: 分かる気がする
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay5 +407 → s 2 sad]
            $ show_sprites(("s 2 sad", "w 1 angry"))
            # [BGM play=+28 → t27] — музыка раньше фона
            play music t27 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay5 +440 → s 4 sad]
            $ show_sprites(("s 4 sad", "w 1 angry"))
            voice "ch7_s_031"
            s "I think I understand her.{#ch7_s_031}"
            # JA[13511]: 分かる気がする。
            # [lay20 hide]
            $ show_sprites(("s 4 sad"))
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry", "s 4 sad"))
            voice "ch7_l_036"
            l "You utter dog fool. Just what is it you 'understand'?{#ch7_l_036}"
            # JA[7376]: このバカ犬。 / 何が分かる気がするよ。
            $ tndl(-40)
            # [lay1 +339 → l 3 angry]
            $ show_sprites(("l 3 angry", "s 4 sad"))
            voice "ch7_l_037"
            l "That still doesn't mean anything she does will ever be accepted.{#ch7_l_037}"
            # JA[7377]: だからといって、何をやっても / 認められるはずがないわ。
            # [移動] → next(389)
            # Часть 1 заканчивается: сцена 389 → глава 7, часть 2.
            jump ch7_2

        "Even so, I won't allow crime.{#ch7_c387}":
            # JA: だからって犯罪は許さない
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay5 +407 → s 2 sad]
            $ show_sprites(("s 2 sad", "w 1 angry"))
            # [BGM play=+28 → t27] — музыка раньше фона
            play music t27 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay5 +405 → s 2 angry]
            $ show_sprites(("s 2 angry", "w 1 angry"))
            voice "ch7_s_032"
            s "Even so, crime is not something I can allow!{#ch7_s_032}"
            # JA[13512]: だからと言って、 / 犯罪を許すわけにはいかない！
            $ tndl(50)
            # [lay20 +1061 → w 1]
            $ show_sprites(("s 2 angry", "w 1"))
            voice "ch7_w_017"
            w "What's that? That we should patiently go around persuading everyone? Don't be absurd.{#ch7_w_017}"
            # JA[16154]: なにそれ？ / 辛抱強く説得でもしてまわれって言うの？ / 馬鹿言ってるんじゃないわよ。
            # [移動] → next(389)
            # Часть 1 заканчивается: сцена 389 → глава 7, часть 2.
            jump ch7_2

        "How should I know.{#ch7_c388}":
            # JA: そんなこと知るか
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay5 +407 → s 2 sad]
            $ show_sprites(("s 2 sad", "w 1 angry"))
            # [BGM play=+28 → t27] — музыка раньше фона
            play music t27 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay5 +405 → s 2 angry]
            $ show_sprites(("s 2 angry", "w 1 angry"))
            voice "ch7_s_033"
            s "How should I know.{#ch7_s_033}"
            # JA[13513]: そんなこと知るか。
            # [lay20 +1061 → w 1]
            $ show_sprites(("s 2 angry", "w 1"))
            voice "ch7_w_018"
            w "Well, that figures. In the end, it's someone else's problem to you.{#ch7_w_018}"
            # JA[16155]: まあ、そんなところでしょうね。 / 結局は他人事だものね。
            # [移動] → next(389)
            # Часть 1 заканчивается: сцена 389 → глава 7, часть 2.
            jump ch7_2


    # конец части 1: сцена 389 — в script-ch7_2.rpy (jump внутри веток)
