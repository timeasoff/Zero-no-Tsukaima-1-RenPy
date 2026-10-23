# Глава 5, часть 6 (сцена 335 core + extra-блок 1408–1428): пауза перед
# объявлением ролей, меню выбора локации; 5 веток — Курке/ハルナ, ルイズ/ギーシュ,
# シエスタ/モンモランシー, タバサ/アンリエッタ, ウェザリー.
# Источник: ps2_source/chapters/chapter_06_本当の想い.txt (SCENE 335; extra
#   1408–1428). Точные аргументы: ps2_source/events_full/chapter_06_本当の想い.txt.
#
# Структура пересобрана (tools/gen_ch5_6_script2.py): сцена 335 -> главное меню
#   5 веток -> каждая ветка = head + мини-меню выбора + rejoin. Порядок реплик,
#   голоса, спрайты и события строго из источника (depth-first обход).
# EN — tools/ch5_6_en.py, RU — tools/ch5_6_ru.py, JA — events-источник.
# old/new пары переводов — tools/gen_ch5_6_tl.py (tl/japanese, tl/russian).
# Голоса — references/voice_id_map.csv (tools/gen_ch5_6_script2.py --manifest).
#
# Вход — jump ch5_6 из script-ch5_5.rpy (сцена 335). Выход — jump ch5_7
#   (сцена 341, core, объявление ролей); сцена 341 ведет в extra-ветки состава
#   (1104–1163), которые портируются отдельно (sp-файл).
#
# ЗАДОЛЖЕННОСТЬ (E7): jump ch5_7 — форвард-переход к части 7 (не портирована);
#   метка добавится в part 7. Скрипт компилируется, игра переходит на экран
#   внимания/сбоя метки только в этом месте.
#
# Голоса: ch5.6_<spk>_<NNN> — новая группа части 6, нумерация с 001 по
#   говорящему, порядок порта: 1408->1409/1410/1411->1412,
#   1413->1414/1415/1416->1417, 1418->1419/1420/1421->1422,
#   1423->1424/1425/1426->1427, 1428. Всего 127 голосов (+17 мыслей).
#
# mapping old->new (из tools/.tmp/mapping6.py): k — пропуск 3000; ha —
#   merge(1949), split(1951); h — split(473+474); s — merge(9937); t — пропуски;
#   w — сдвиг +8; l/g/m/si — сдвиг +2; fresh: k_002=「あら、ダーリン！」,
#   ha_002=「ひ、平賀くん！」.
#
# Не портируются:
#   - сцена 341 (core): ведет в extra-ветки состава (1104–1163), портируются
#     отдельно (sp-файл);
#   - сцена 342 (core): ведет в меню дат 1870–1875, портируется отдельно;
#   - сцена 343 (core): пустой переход (E7 forward debt, закроется частью 7+);
#   - MOVEINIT/MAPDEST/MOVE, waitAction, msgon/msgoff — перенос карты переходов
#     PS2 не реализован;
#   - SE (se1) — не переносится.
#
# Фоны: bg 58 = stage (stub, id(58)), bg 54 = stage2 (stub id(54)),
#   bg 53/57/55/50/38/41/90 — имена пусты в image_id_map.csv (заглушки id(K));
#   имена заполняет человек через tools/build_image_id_map.py +
#   tools/replace_bg_placeholders.py --apply.
#
# Спрайты: lay20 (ウェザリー 1061/1063/1067), lay5 (サイト 390/392/429/…);
#   id спрайтов без строки в sprite_id_map.csv → заглушки id(K).


label ch5_6:
    # Часть 6: сцена 335 — пауза перед объявлением ролей + меню
    # выбора локации; extra-блок 1408–1428 — 5 веток (Курке/Харуна,
    # Луиза/ギーシュ, Сиеста/Монモン, タバサ/アンリエッタ, ウェザリー).
    # Сцены 341–343 (core) не входят — ведут в extra-цепочки
    # (1104–1163 состав, 1870–1875 меню дат), портируются отдельно.


    # ==== SCENE 335 (core: пауза перед объявлением ролей) ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +58 → town_square]
    $ fade_fx("town_square", new_music="t30")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1"))
    th "Hah… practice is off today, isn't it?{#ch5.6_th_001}"
    # JA: （はあ、今日は練習が休みか）
    th "Wealthy-sama said that tomorrow the final casting will finally be announced...{#ch5.6_th_002}"
    # JA: （明日にはいよいよ役柄の最終発表をするって / 　ウェザリーさんはいってたけど……）
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("s 3 sad"))
    th "I wonder how it's going to turn out? Really...{#ch5.6_th_003}"
    # JA: （どうなるんだろうな？ / 　本当に……）
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1"))
    th "It's a rare day off... what should I do?{#ch5.6_th_004}"
    # JA: （せっかくの休みだけど、どうしよ？）
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")

    # ---- 【選択肢】 — выбор локации (【移動】) ----
    menu:
        "To the theater (stage){#ch5_6_c1408}":
            # JA: 舞台
            # ==== SCENE 1408 (ветка: head) ====
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [BG +54 → id(54)]
            $ fade_fx("id(54)", new_music="t7")
            # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
            # [lay6 +691 → k 2 angry]
            $ show_sprites(("k 2 angry"))
            # [lay7 +966 → ha 2 angry]
            $ show_sprites(("k 2 angry", "ha 2 angry"))
            th "Kirche and Haruna are rehearsing the play.{#ch5.6_th_005}"
            # JA: （キュルケとハルナが劇の練習をしてるな）
            voice "ch5.6_k_001"
            k "Kirche, let's go through that dance one more time, from the beginning!{#ch5_6_v2999}"
            # JA[2999]: そのダンス、もう一度最初から行くわよ！
            $ update_sympathy(20, char_key="kirche")
            voice "ch5.6_ha_001"
            ha "Yes! Kirche-sama!{#ch5_6_v1949}"
            # JA[1949]: はいっ！ / キュルケさん！
            th "They're practicing with such enthusiasm, it's something I wouldn't have imagined.{#ch5.6_th_006}"
            # JA: （ずいぶん熱心に練習をしてるな。 / 　前からは考えられないくらいだ）
            # [lay6 +689 → k 2 happy]
            $ show_sprites(("k 2 happy", "ha 2 angry"))
            voice "ch5.6_k_002"
            k "Oh, darling!{#ch5_6_v3000}"
            # JA[3000]: あら、ダーリン！
            # [lay7 +968 → ha 2 sad]
            $ show_sprites(("k 2 happy", "ha 2 sad"))
            voice "ch5.6_ha_002"
            ha "H- Hiraga-kun!{#ch5_6_v1950}"
            # JA[1950]: ひ、平賀くん！
            # [lay7 hide]
            $ show_sprites(("k 2 happy"))
            # [lay5 +425 → s 3 happy]
            $ show_sprites(("k 2 happy", "s 3 happy"))
            voice "ch5.6_s_001"
            s "Did I disturb you?{#ch5_6_v9932}"
            # JA[9932]: 邪魔しちゃったかな？
            # [lay6 +687 → k 2]
            $ show_sprites(("k 2", "s 3 happy"))
            voice "ch5.6_k_003"
            k "Hehe, it's fine. If it's you, darling, it's fine.{#ch5_6_v3001}"
            # JA[3001]: うふふ、いいのよ。 / 別にダーリンなら。
            voice "ch5.6_s_002"
            s "You practiced so hard, I couldn't bring myself to call out to you.{#ch5_6_v9933}"
            # JA[9933]: ずいぶんと熱心だったから、 / 声をかけづらくてさ。
            voice "ch5.6_k_004"
            k "Mm, I did slack off a bit, though.{#ch5_6_v3002}"
            # JA[3002]: まぁ、結構練習さぼっちゃったしね。
            # [lay5 +392 → s 1 happy]
            $ show_sprites(("k 2", "s 1 happy"))
            voice "ch5.6_s_003"
            s "Ah hah hah hah...{#ch5_6_v9934}"
            # JA[9934]: あははは……。
            # ---- 【選択肢】 — выбор места в локации ----
            menu:
                "I was worried about Kirche.{#ch5_6_c1409}":
                    # JA: 心配したんだぞ
                    # ==== SCENE 1409 ====
                    # [if         if(isJump())] — не портируется
                    # [RESET      reset()] — сброс сцены: спрайты скрываются
                    $ show_sprites()
                    # [lay5 +392 → s 1 happy]
                    $ show_sprites(("s 1 happy"))
                    # [lay6 +687 → k 2]
                    $ show_sprites(("k 2", "s 1 happy"))
                    play music t7 fadein 1.0
                    # [BG +54 → id(54)]
                    $ fade_fx("id(54)")
                    # [lay5 +390 → s 1]
                    $ show_sprites(("k 2", "s 1"))
                    voice "ch5.6_s_004"
                    s "I was worried about Kirche.{#ch5_6_v9935}"
                    # JA[9935]: キュルケのこと、心配したんだぞ。
                    # [lay6 +695 → k 2 shy]
                    $ show_sprites(("k 2 shy", "s 1"))
                    voice "ch5.6_k_005"
                    k "Oh? Did you worry about me?{#ch5_6_v3003}"
                    # JA[3003]: あら？ / 心配してくれたんだ。
                    # [lay5 +394 → s 1 angry]
                    $ show_sprites(("k 2 shy", "s 1 angry"))
                    voice "ch5.6_s_005"
                    s "Of course!{#ch5_6_v9936}"
                    # JA[9936]: あたりまえだろ！
                "I wasn't worried at all.{#ch5_6_c1410}":
                    # JA: 心配なんかしてなかったよ
                    # ==== SCENE 1410 ====
                    # [if         if(isJump())] — не портируется
                    # [RESET      reset()] — сброс сцены: спрайты скрываются
                    $ show_sprites()
                    # [lay5 +392 → s 1 happy]
                    $ show_sprites(("s 1 happy"))
                    # [lay6 +687 → k 2]
                    $ show_sprites(("k 2", "s 1 happy"))
                    play music t7 fadein 1.0
                    # [BG +54 → id(54)]
                    $ fade_fx("id(54)")
                    # [lay5 +390 → s 1]
                    $ show_sprites(("k 2", "s 1"))
                    voice "ch5.6_s_006"
                    s "Really? I knew you'd come back, so I wasn't worried at all.{#ch5_6_v9937}"
                    # JA[9937]: そうか？ / 俺はキュルケが戻ってくるって信じてたから、 / 心配なんてしてなかったぞ。
                    # [lay6 hide]
                    $ show_sprites(("s 1"))
                    # [lay7 +962 → ha 2]
                    $ show_sprites(("ha 2", "s 1"))
                    voice "ch5.6_ha_003"
                    ha "Really? I kinda felt like you were the most nervous of all, Hiraga-kun.{#ch5_6_v1951}"
                    # JA[1951]: 本当？ / 一番おどおどしていたの、 / 平賀くんだったような気がするけど。
                    # [lay5 +429 → s 3 sad]
                    $ show_sprites(("ha 2", "s 3 sad"))
                    voice "ch5.6_s_007"
                    s "B-baka. Don't say that.{#ch5_6_v9938}"
                    # JA[9938]: ば、ばか。 / そんなこと言うなって。
                    # [lay7 hide]
                    $ show_sprites(("s 3 sad"))
                    # [lay6 +689 → k 2 happy]
                    $ show_sprites(("k 2 happy", "s 3 sad"))
                    voice "ch5.6_k_006"
                    k "Really now, darling. You could just say it honestly.{#ch5_6_v3004}"
                    # JA[3004]: もう、ダーリンったら。 / 素直に言ってもいいのよ。
                    $ update_sympathy(10, char_key="kirche")
                    # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
                "Was that so?{#ch5_6_c1411}":
                    # JA: そうだっけ？
                    # ==== SCENE 1411 ====
                    # [if         if(isJump())] — не портируется
                    # [RESET      reset()] — сброс сцены: спрайты скрываются
                    $ show_sprites()
                    # [lay5 +392 → s 1 happy]
                    $ show_sprites(("s 1 happy"))
                    # [lay6 +687 → k 2]
                    $ show_sprites(("k 2", "s 1 happy"))
                    play music t7 fadein 1.0
                    # [BG +54 → id(54)]
                    $ fade_fx("id(54)")
                    # [lay5 +425 → s 3 happy]
                    $ show_sprites(("k 2", "s 3 happy"))
                    voice "ch5.6_s_008"
                    s "W-was that so?{#ch5_6_v9939}"
                    # JA[9939]: そ、そうだっけ？
                    # [lay6 +691 → k 2 angry]
                    $ show_sprites(("k 2 angry", "s 3 happy"))
                    voice "ch5.6_k_007"
                    k "That hurts~. Does it matter to you whether I'm here or not?{#ch5_6_v3005}"
                    # JA[3005]: ひどーい。 / あたしがいてもいなくても同じってこと？
                    $ update_sympathy(-10, char_key="kirche")
                    # [lay6 hide]
                    $ show_sprites(("s 3 happy"))
                    # [lay7 +966 → ha 2 angry]
                    $ show_sprites(("ha 2 angry", "s 3 happy"))
                    voice "ch5.6_ha_004"
                    ha "Hiraga-kun, that's so mean~~!!{#ch5_6_v1952}"
                    # JA[1952]: 平賀くん、それヒドイよ～～！！
                    $ update_sympathy(-10, char_key="haruna")
                    # [TNDL       tndl(30)] — не переносится (система не реализована, AGENTS §6)
                    # [lay5 +429 → s 3 sad]
                    $ show_sprites(("ha 2 angry", "s 3 sad"))
                    voice "ch5.6_s_009"
                    s "I'm sorry.{#ch5_6_v9940}"
                    # JA[9940]: ごめんなさい。
            # ==== SCENE 1412 (rejoin, после мини-меню) ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("s 1 angry"))
            # [lay6 +695 → k 2 shy]
            $ show_sprites(("k 2 shy", "s 1 angry"))
            play music t7 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay5 +390 → s 1]
            $ show_sprites(("k 2 shy", "s 1"))
            voice "ch5.6_s_010"
            s "But, there's no need for you to practice this hard until the day of the show...{#ch5_6_v9941}"
            # JA[9941]: でも、こんな日まで練習しなくても / いいのに……。
            # [lay7 x=464]
            $ show_sprites(("k 2 shy", "s 1"))
            # [lay6 +687 → k 2]
            $ show_sprites(("k 2", "s 1"))
            voice "ch5.6_k_008"
            k "It's practice to make up for lost time. The more, the better.{#ch5_6_v3006}"
            # JA[3006]: 遅れを取り戻すための練習だもの。 / どれだけやっても、足りないことはないわ。
            # [lay5 hide]
            $ show_sprites(("k 2"))
            # [lay7 +968 → ha 2 sad]
            $ show_sprites(("k 2", "ha 2 sad"))
            voice "ch5.6_ha_005"
            ha "And... I'm the one holding everyone back the most...{#ch5_6_v1953}"
            # JA[1953]: それに……。 / 私も一番足を引っ張ってるし……。
            voice "ch5.6_k_009"
            k "Oh my, you're aware?{#ch5_6_v3007}"
            # JA[3007]: あら、自覚あるんだ？
            # [lay7 +966 → ha 2 angry]
            $ show_sprites(("k 2", "ha 2 angry"))
            voice "ch5.6_ha_006"
            ha "That's mean! Kirche-sama!{#ch5_6_v1954}"
            # JA[1954]: ヒドイです！ / キュルケさん！
            # [lay6 hide]
            $ show_sprites(("ha 2 angry"))
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1", "ha 2 angry"))
            voice "ch5.6_s_011"
            s "It'll be all right. If you've got the will to do it, you'll make it.{#ch5_6_v9942}"
            # JA[9942]: 大丈夫だよ。 / それだけやる気があればなんとかなるって。
            # [lay5 hide]
            $ show_sprites(("ha 2 angry"))
            # [lay6 +689 → k 2 happy]
            $ show_sprites(("k 2 happy", "ha 2 angry"))
            voice "ch5.6_k_010"
            k "That's right. As my darling says.{#ch5_6_v3008}"
            # JA[3008]: そうそう。 / ダーリンの言う通りよ。
            # [lay7 +968 → ha 2 sad]
            $ show_sprites(("k 2 happy", "ha 2 sad"))
            voice "ch5.6_ha_007"
            ha "Yes...{#ch5_6_v1955}"
            # JA[1955]: はい……。
            # [SET        set("se1", {stop = 1})] — SE не портируется
            stop music fadeout 1.0
            # [lay7 hide]
            $ show_sprites(("k 2 happy"))
            # [lay6 hide]
            $ show_sprites()
            # [BG hide]
            $ fade_fx("black")
        "To the auditorium{#ch5_6_c1413}":
            # JA: 劇場
            # ==== SCENE 1413 (ветка: head) ====
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [BG +50 → id(50)]
            $ fade_fx("id(50)", new_music="t5")
            # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
            # [lay1 +313 → l 6]
            $ show_sprites(("l 6"))
            # [lay4 +555 → g 1]
            $ show_sprites(("l 6", "g 1"))
            th "Huh? Louise and Guiche together? That's rare.{#ch5.6_th_007}"
            # JA: （あれっ？ / 　ルイズとギーシュとは珍しい組み合わせだな）
            th "Could it be that Guiche... is hitting on Louise?!{#ch5.6_th_008}"
            # JA: （まさかギーシュのやつ！ / 　ルイズに色目でも使ってるのか！？）
            # ---- 【選択肢】 — выбор места в локации ----
            menu:
                "Confront Guiche{#ch5_6_c1414}":
                    # JA: ギーシュを問い詰める
                    # ==== SCENE 1414 ====
                    # [if         if(isJump())] — не портируется
                    # [RESET      reset()] — сброс сцены: спрайты скрываются
                    $ show_sprites()
                    # [lay4 +555 → g 1]
                    $ show_sprites(("g 1"))
                    # [lay1 +313 → l 6]
                    $ show_sprites(("l 6", "g 1"))
                    play music t5 fadein 1.0
                    # [BG +50 → id(50)]
                    $ fade_fx("id(50)")
                    # [lay1 hide]
                    $ show_sprites(("g 1"))
                    # [lay4 hide]
                    $ show_sprites()
                    # [lay5 +394 → s 1 angry]
                    $ show_sprites(("s 1 angry"))
                    voice "ch5.6_s_012"
                    s "Hey, Guiche!{#ch5_6_v9943}"
                    # JA[9943]: おいっ、ギーシュ！
                    # [lay5 hide]
                    $ show_sprites()
                    # [lay1 +313 → l 6]
                    $ show_sprites(("l 6"))
                    # [lay4 +555 → g 1]
                    $ show_sprites(("l 6", "g 1"))
                    voice "ch5.6_l_001"
                    l "Oh, Saito?{#ch5_6_v4993}"
                    # JA[4993]: あら、サイト？
                    $ update_sympathy(10, char_key="louise")
                    # [TNDL       tndl(30)] — не переносится (система не реализована, AGENTS §6)
                    voice "ch5.6_g_001"
                    g "W-what, is it you?{#ch5_6_v1443}"
                    # JA[1443]: な、なんだ、きみか？
                    # [lay1 hide]
                    $ show_sprites(("g 1"))
                    # [lay4 hide]
                    $ show_sprites()
                    # [lay5 +394 → s 1 angry]
                    $ show_sprites(("s 1 angry"))
                    voice "ch5.6_s_013"
                    s "What are you doing with Louise! Where's Montmorency?{#ch5_6_v9944}"
                    # JA[9944]: ルイズに何をしてるんだよ！ / モンモランシーはどうしたんだ？
                    # [lay5 hide]
                    $ show_sprites()
                    # [lay1 +313 → l 6]
                    $ show_sprites(("l 6"))
                    # [lay4 +559 → g 1 angry]
                    $ show_sprites(("l 6", "g 1 angry"))
                "Confront Louise{#ch5_6_c1415}":
                    # JA: ルイズを問い詰める
                    # ==== SCENE 1415 ====
                    # [if         if(isJump())] — не портируется
                    # [RESET      reset()] — сброс сцены: спрайты скрываются
                    $ show_sprites()
                    # [lay4 +555 → g 1]
                    $ show_sprites(("g 1"))
                    # [lay1 +313 → l 6]
                    $ show_sprites(("l 6", "g 1"))
                    play music t5 fadein 1.0
                    # [BG +50 → id(50)]
                    $ fade_fx("id(50)")
                    # [lay1 hide]
                    $ show_sprites(("g 1"))
                    # [lay4 hide]
                    $ show_sprites()
                    # [lay5 +394 → s 1 angry]
                    $ show_sprites(("s 1 angry"))
                    voice "ch5.6_s_014"
                    s "Hey, Louise.{#ch5_6_v9945}"
                    # JA[9945]: おいっ、ルイズ。
                    # [lay5 hide]
                    $ show_sprites()
                    # [lay1 +317 → l 6 angry]
                    $ show_sprites(("l 6 angry"))
                    # [lay4 +555 → g 1]
                    $ show_sprites(("l 6 angry", "g 1"))
                    voice "ch5.6_l_002"
                    l "What is it, Saito?{#ch5_6_v4994}"
                    # JA[4994]: なによ、サイト。
                    # [lay1 hide]
                    $ show_sprites(("g 1"))
                    # [lay4 hide]
                    $ show_sprites()
                    # [lay5 +396 → s 1 sad]
                    $ show_sprites(("s 1 sad"))
                    voice "ch5.6_s_015"
                    s "Why are you walking around together with Guiche?{#ch5_6_v9946}"
                    # JA[9946]: なんで、ギーシュと一緒に / 歩いてるんですか？
                    # [lay5 hide]
                    $ show_sprites()
                    # [lay1 +313 → l 6]
                    $ show_sprites(("l 6"))
                    # [lay4 +555 → g 1]
                    $ show_sprites(("l 6", "g 1"))
                    voice "ch5.6_l_003"
                    l "What, you're asking in a bitter tone? There's nothing to it.{#ch5_6_v4995}"
                    # JA[4995]: 何、卑屈になって聞いてるのよ。 / 別になんでもないわよ。
                    # [lay4 +559 → g 1 angry]
                    $ show_sprites(("l 6", "g 1 angry"))
                "Throw a rock{#ch5_6_c1416}":
                    # JA: 石を投げる
                    # ==== SCENE 1416 ====
                    # [if         if(isJump())] — не портируется
                    # [RESET      reset()] — сброс сцены: спрайты скрываются
                    $ show_sprites()
                    # [lay4 +555 → g 1]
                    $ show_sprites(("g 1"))
                    # [lay1 +313 → l 6]
                    $ show_sprites(("l 6", "g 1"))
                    play music t5 fadein 1.0
                    # [BG +50 → id(50)]
                    $ fade_fx("id(50)")
                    th "Eat this, Guiche!{#ch5.6_th_009}"
                    # JA: （喰らえ、ギーシュ！）
                    # [SET        set("se0", {play = (0x03000000 +62)})] — SE не портируется
                    # [VIBRATE    vibrate(1)] — SE не портируется
                    # [EVENT_CG hide]
                    $ fade_fx("black")
                    # [lay5 hide]
                    $ show_sprites(("l 6", "g 1"))
                    # [lay4 +559 → g 1 angry]
                    $ show_sprites(("l 6", "g 1 angry"))
                    voice "ch5.6_g_002"
                    g "...Ouch! Who is it! To think you'd throw a rock at me!{#ch5_6_v1444}"
                    # JA[1444]: ……痛てっ！ / だ、誰だ！ / このぼくに石を投げるとは！
                    th "Hehehe. Heaven's punishment succeeded! Now for the second shot...{#ch5.6_th_010}"
                    # JA: （ふふふ。 / 　天誅成功！ / 　続いて第２弾を……）
                    # [lay1 +317 → l 6 angry]
                    $ show_sprites(("l 6 angry", "g 1 angry"))
                    voice "ch5.6_l_004"
                    l "Saito, what are you doing?{#ch5_6_v4996}"
                    # JA[4996]: サイト、何してるのよ？
                    $ update_sympathy(-10, char_key="louise")
                    # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
                    # [lay1 hide]
                    $ show_sprites(("g 1 angry"))
                    # [lay4 hide]
                    $ show_sprites()
                    # [lay5 +396 → s 1 sad]
                    $ show_sprites(("s 1 sad"))
                    voice "ch5.6_s_016"
                    s "Whoa! I've been caught! ...I-I'm sorry.{#ch5_6_v9947}"
                    # JA[9947]: うわっ！ / 見つかった！ / ……ご、ごめんなさい。
                    # [lay5 hide]
                    $ show_sprites()
                    # [lay1 +313 → l 6]
                    $ show_sprites(("l 6"))
                    # [lay4 +559 → g 1 angry]
                    $ show_sprites(("l 6", "g 1 angry"))
            # ==== SCENE 1417 (rejoin, после мини-меню) ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay4 +559 → g 1 angry]
            $ show_sprites(("g 1 angry"))
            # [lay1 +313 → l 6]
            $ show_sprites(("l 6", "g 1 angry"))
            play music t5 fadein 1.0
            # [BG +50 → id(50)]
            $ fade_fx("id(50)")
            voice "ch5.6_g_003"
            g "We were just sent shopping by Wealthy-sama! Honestly!{#ch5_6_v1445}"
            # JA[1445]: ぼく達はただ、ウェザリーに買い物を / 頼まれただけだ！ / まったく！
            # [lay4 hide]
            $ show_sprites(("l 6"))
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("l 6", "s 3 sad"))
            voice "ch5.6_s_017"
            s "O-oh really?{#ch5_6_v9948}"
            # JA[9948]: そ、そうなのか？
            # [lay1 +313 → l 6]
            $ show_sprites(("l 6", "s 3 sad"))
            voice "ch5.6_l_005"
            l "That's right. Guiche is just carrying the bags for me.{#ch5_6_v4997}"
            # JA[4997]: そういうわけ。 / ギーシュはただの荷物持ちよ。
            # [lay5 hide]
            $ show_sprites(("l 6"))
            # [lay4 +561 → g 1 sad]
            $ show_sprites(("l 6", "g 1 sad"))
            voice "ch5.6_g_004"
            g "Y-you can say that so confidently...? Hmm...{#ch5_6_v1446}"
            # JA[1446]: そ、そう断言されるとちょっと……。
            # [lay4 hide]
            $ show_sprites(("l 6"))
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("l 6", "s 1 angry"))
            voice "ch5.6_s_018"
            s "T-then why didn't you ask me to help!?{#ch5_6_v9949}"
            # JA[9949]: だ、だったら俺に頼めよ！
            # [lay1 +315 → l 6 happy]
            $ show_sprites(("l 6 happy", "s 1 angry"))
            voice "ch5.6_l_006"
            l "Oh? Could it be... you're jealous?{#ch5_6_v4998}"
            # JA[4998]: あれ？ / もしかして、ヤキモチなの？
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("l 6 happy", "s 1 sad"))
            voice "ch5.6_s_019"
            s "I-I don't think so...{#ch5_6_v9950}"
            # JA[9950]: そ、そんなことないけどさ……。
            # [lay1 +313 → l 6]
            $ show_sprites(("l 6", "s 1 sad"))
            voice "ch5.6_l_007"
            l "Then, shall I have you help me carry the bags? Guiche alone isn't reliable enough.{#ch5_6_v4999}"
            # JA[4999]: だったら、荷物を持つの手伝って / もらおうかしら？ / ギーシュだけでは心もとないし。
            # [lay5 +392 → s 1 happy]
            $ show_sprites(("l 6", "s 1 happy"))
            voice "ch5.6_s_020"
            s "O-ok, got it!{#ch5_6_v9951}"
            # JA[9951]: りょ、了解であります！
            # [lay1 +321 → l 6 shy]
            $ show_sprites(("l 6 shy", "s 1 happy"))
            voice "ch5.6_l_008"
            l "Just so you know... There are still more bags to carry.{#ch5_6_v5000}"
            # JA[5000]: 言っておくけど……。 / まだまだ荷物はあるんだからね！
            # [lay5 +390 → s 1]
            $ show_sprites(("l 6 shy", "s 1"))
            voice "ch5.6_s_021"
            s "H-haaai! Your ladyship!{#ch5_6_v9952}"
            # JA[9952]: は、は～～い！ / ご主人様！
            # [SET        set("se1", {stop = 1})] — SE не портируется
            stop music fadeout 1.0
            # [lay1 hide]
            $ show_sprites(("s 1"))
            # [lay5 hide]
            $ show_sprites()
            # [BG hide]
            $ fade_fx("black")
        "To the main street{#ch5_6_c1418}":
            # JA: 表通り
            # ==== SCENE 1418 (ветка: head) ====
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [BG +38 → town]
            $ fade_fx("town", new_music="t6")
            # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
            # [lay2 +500 → si 2]
            $ show_sprites(("si 2"))
            # [lay3 +863 → m 2]
            $ show_sprites(("si 2", "m 2"))
            th "Huh? Siesta and Montmon... what a rare combination.{#ch5.6_th_011}"
            # JA: （あれっ？ / 　シエスタとモンモンって……。 / 　珍しい組み合わせもあったもんだな）
            # [lay2 +502 → si 2 happy]
            $ show_sprites(("si 2 happy", "m 2"))
            voice "ch5.6_si_001"
            si "Ah, Saito-san!{#ch5_6_v14463}"
            # JA[14463]: あ、サイトさん！
            $ update_sympathy(20, char_key="siesta")
            # [lay3 hide]
            $ show_sprites(("si 2 happy"))
            # [lay5 +425 → s 3 happy]
            $ show_sprites(("si 2 happy", "s 3 happy"))
            voice "ch5.6_s_022"
            s "What are the two of you up to?{#ch5_6_v9953}"
            # JA[9953]: ２人でどうしたの？
            # [lay2 +500 → si 2]
            $ show_sprites(("si 2", "s 3 happy"))
            voice "ch5.6_si_002"
            si "U-um, well...{#ch5_6_v14464}"
            # JA[14464]: え、ええとですね。
            # [lay5 hide]
            $ show_sprites(("si 2"))
            # [lay3 +863 → m 2]
            $ show_sprites(("si 2", "m 2"))
            voice "ch5.6_m_001"
            m "I'm learning to cook from Siesta.{#ch5_6_v3994}"
            # JA[3994]: シエスタにお料理を習ってるの。
            # [lay2 +506 → si 2 sad]
            $ show_sprites(("si 2 sad", "m 2"))
            voice "ch5.6_si_003"
            si "Eh, is it okay to let it slip?{#ch5_6_v14465}"
            # JA[14465]: えっ、バラしちゃっていいんですか？
            voice "ch5.6_m_002"
            m "There's nothing suspicious about it.{#ch5_6_v3995}"
            # JA[3995]: 別にやましいことはしてないもの。
            th "Even rare things happen.{#ch5.6_th_012}"
            # JA: （珍しいこともあるもんだな）
            # ---- 【選択肢】 — выбор места в локации ----
            menu:
                "I'd love to try Montmon's cooking{#ch5_6_c1419}":
                    # JA: 手料理を食べさせて欲しいな
                    # ==== SCENE 1419 ====
                    # [if         if(isJump())] — не портируется
                    # [RESET      reset()] — сброс сцены: спрайты скрываются
                    $ show_sprites()
                    # [lay3 +863 → m 2]
                    $ show_sprites(("m 2"))
                    # [lay2 +506 → si 2 sad]
                    $ show_sprites(("si 2 sad", "m 2"))
                    play music t6 fadein 1.0
                    # [BG +38 → town]
                    $ fade_fx("town")
                    # [lay2 hide]
                    $ show_sprites(("m 2"))
                    # [lay5 +425 → s 3 happy]
                    $ show_sprites(("s 3 happy", "m 2"))
                    voice "ch5.6_s_023"
                    s "Then, next time, let me try Montmon's cooking.{#ch5_6_v9954}"
                    # JA[9954]: じゃあ、こんどモンモンの手料理を / 食べさせてほしいな。
                    # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
                    # [lay3 +867 → m 2 angry]
                    $ show_sprites(("s 3 happy", "m 2 angry"))
                    voice "ch5.6_m_003"
                    m "There's no way I'd cook for someone who calls me 'Montmon'.{#ch5_6_v3996}"
                    # JA[3996]: モンモンなんて言ってる人に / 食べさせる料理なんて無いわ。
                    # [lay5 +429 → s 3 sad]
                    $ show_sprites(("s 3 sad", "m 2 angry"))
                    voice "ch5.6_s_024"
                    s "Ouch...{#ch5_6_v9955}"
                    # JA[9955]: あらら……。
                "What's your specialty?{#ch5_6_c1420}":
                    # JA: 得意な料理って何？
                    # ==== SCENE 1420 ====
                    # [if         if(isJump())] — не портируется
                    # [RESET      reset()] — сброс сцены: спрайты скрываются
                    $ show_sprites()
                    # [lay3 +863 → m 2]
                    $ show_sprites(("m 2"))
                    # [lay2 +506 → si 2 sad]
                    $ show_sprites(("si 2 sad", "m 2"))
                    play music t6 fadein 1.0
                    # [BG +38 → town]
                    $ fade_fx("town")
                    # [lay2 hide]
                    $ show_sprites(("m 2"))
                    # [lay5 +423 → s 3]
                    $ show_sprites(("s 3", "m 2"))
                    voice "ch5.6_s_025"
                    s "What's your specialty?{#ch5_6_v9956}"
                    # JA[9956]: 得意な料理って何？
                    # [lay3 +869 → m 2 sad]
                    $ show_sprites(("s 3", "m 2 sad"))
                    voice "ch5.6_m_004"
                    m "Hmm, I think pickled vegetables are the limit for now. Fried food and bread — I still have plenty of training to do.{#ch5_6_v3997}"
                    # JA[3997]: うーん、まだ煮物が限界みたい。 / 焼き物とか、パンとか、 / まだまだ修行が必要かもね。
                    # [lay5 hide]
                    $ show_sprites(("m 2 sad"))
                    # [lay2 +502 → si 2 happy]
                    $ show_sprites(("si 2 happy", "m 2 sad"))
                    voice "ch5.6_si_004"
                    si "Miss Montmonmon has natural talent, so I think you're just a little short.{#ch5_6_v14466}"
                    # JA[14466]: ミス・モンモランシーは筋がいいんですから、 / あと少しだと思いますよ。
                "Can you actually make something edible?{#ch5_6_c1421}":
                    # JA: 食べられるモノを作れるの？
                    # ==== SCENE 1421 ====
                    # [if         if(isJump())] — не портируется
                    # [RESET      reset()] — сброс сцены: спрайты скрываются
                    $ show_sprites()
                    # [lay3 +863 → m 2]
                    $ show_sprites(("m 2"))
                    # [lay2 +506 → si 2 sad]
                    $ show_sprites(("si 2 sad", "m 2"))
                    play music t6 fadein 1.0
                    # [BG +38 → town]
                    $ fade_fx("town")
                    # [lay2 hide]
                    $ show_sprites(("m 2"))
                    # [lay5 +425 → s 3 happy]
                    $ show_sprites(("s 3 happy", "m 2"))
                    voice "ch5.6_s_026"
                    s "Can you actually make something edible?{#ch5_6_v9957}"
                    # JA[9957]: ちゃんと食べられるモノを作れるの？
                    # [lay3 +867 → m 2 angry]
                    $ show_sprites(("s 3 happy", "m 2 angry"))
                    voice "ch5.6_m_005"
                    m "Mmm, that's rude. As of now, I'm able to make something edible.{#ch5_6_v3998}"
                    # JA[3998]: まぁ、失礼ね。 / 今はちゃんと食べられるものを作れるように / なっているわ。
                    # [lay5 hide]
                    $ show_sprites(("m 2 angry"))
                    # [lay2 +504 → si 2 angry]
                    $ show_sprites(("si 2 angry", "m 2 angry"))
                    voice "ch5.6_si_005"
                    si "That's right. First of all, it's not that easy to make something that's not edible.{#ch5_6_v14467}"
                    # JA[14467]: そうですよ。 / 第一、食べられないものなんて、 / そう簡単に作れるものじゃないです。
                    # [lay3 +869 → m 2 sad]
                    $ show_sprites(("si 2 angry", "m 2 sad"))
                    voice "ch5.6_m_006"
                    m "I think that's a different meaning...{#ch5_6_v3999}"
                    # JA[3999]: それは意味が違うと思うけど……。
            # ==== SCENE 1422 (rejoin, после мини-меню) ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay3 +867 → m 2 angry]
            $ show_sprites(("m 2 angry"))
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad", "m 2 angry"))
            play music t6 fadein 1.0
            # [BG +38 → town]
            $ fade_fx("town")
            # [lay2 x=144]
            $ show_sprites(("s 3 sad", "m 2 angry"))
            # [lay5 +431 → s 3 shy]
            $ show_sprites(("s 3 shy", "m 2 angry"))
            voice "ch5.6_s_027"
            s "So, in the end, you're going to treat Guiche, right?{#ch5_6_v9958}"
            # JA[9958]: やっぱり、最後にはギーシュにご馳走するの？
            # [lay3 +871 → m 2 shy]
            $ show_sprites(("s 3 shy", "m 2 shy"))
            voice "ch5.6_m_007"
            m "T-that is, it's just that... I mean...{#ch5_6_v4000}"
            # JA[4000]: そ、それはその……つまり……。
            # [lay3 hide]
            $ show_sprites(("s 3 shy"))
            # [lay2 +504 → si 2 angry]
            $ show_sprites(("s 3 shy", "si 2 angry"))
            voice "ch5.6_si_006"
            si "Really, Saito-san! Men shouldn't ask questions like that.{#ch5_6_v14468}"
            # JA[14468]: もう、サイトさん！ / 男の人はそういうことを聞いちゃ駄目ですよ。
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad", "si 2 angry"))
            voice "ch5.6_s_028"
            s "I-is that how it is?{#ch5_6_v9959}"
            # JA[9959]: そ、そういうものなのかな？
            voice "ch5.6_si_007"
            si "That's right.{#ch5_6_v14469}"
            # JA[14469]: そうです。
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1", "si 2 angry"))
            voice "ch5.6_s_029"
            s "Mmm, let's go with that.{#ch5_6_v9960}"
            # JA[9960]: まぁ、そういうことにしておきますか。
            # [SET        set("se1", {stop = 1})] — SE не портируется
            stop music fadeout 1.0
            # [lay2 hide]
            $ show_sprites(("s 1"))
            # [lay5 hide]
            $ show_sprites()
            # [BG hide]
            $ fade_fx("black")
        "To the inn{#ch5_6_c1423}":
            # JA: 宿
            # ==== SCENE 1423 (ветка: head) ====
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [BG +41 → id(41)]
            $ fade_fx("id(41)", new_music="t9")
            # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
            # [lay0 +632 → t 5]
            $ show_sprites(("t 5"))
            # [lay8 +781 → h 3 sad]
            $ show_sprites(("h 3 sad", "t 5"))
            th "Huh? Tabitha and the princess are here. The princess looks quite troubled...{#ch5.6_th_013}"
            # JA: （あれ、タバサと、お姫さまがいる。 / 　ずいぶんお姫さまが困ってる / 　みたいだけど……）
            voice "ch5.6_h_001"
            h "Thank you for your cooperation with this investigation.{#ch5_6_v463}"
            # JA[463]: 今回の調査のご協力に感謝します。
            voice "ch5.6_t_001"
            t "Yes.{#ch5_6_v15459}"
            # JA[15459]: はい。
            voice "ch5.6_h_002"
            h "U-um... It's such nice weather today, isn't it?{#ch5_6_v464}"
            # JA[464]: え、ええと。 / きょ、今日はいいお天気ですね。
            voice "ch5.6_t_002"
            t "Yes, it is.{#ch5_6_v15460}"
            # JA[15460]: そうですね。
            voice "ch5.6_h_003"
            h "…….{#ch5_6_v465}"
            # JA[465]: ……。
            th "…….{#ch5.6_th_014}"
            # JA: ……。
            th "W-what's going on. This awkward atmosphere!{#ch5.6_th_015}"
            # JA: （な、なんだよ。 / 　この気まずい雰囲気は！）
            # [lay0 hide]
            $ show_sprites(("h 3 sad"))
            # [lay8 +779 → h 3 angry]
            $ show_sprites(("h 3 angry"))
            voice "ch5.6_h_004"
            h "U-um, familiar~! You've come at just the right time.{#ch5_6_v466}"
            # JA[466]: つ、使い魔さん！ / いいところに来てくれました。
            # [lay8 x=-96]
            $ show_sprites(("h 3 angry"))
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("h 3 angry", "s 3 sad"))
            voice "ch5.6_s_030"
            s "W-what's wrong, Your Highness? You're pulling me along... You were talking to Tabitha, weren't you?{#ch5_6_v9961}"
            # JA[9961]: ど、どうしたんですか、お姫さま。 / 俺のことひっぱって……。 / タバサと話をしていたんじゃないですか？
            # [lay8 +781 → h 3 sad]
            $ show_sprites(("h 3 sad", "s 3 sad"))
            voice "ch5.6_h_005"
            h "I just couldn't keep the conversation going...{#ch5_6_v467}"
            # JA[467]: ど、どうしても会話が続かなくて……。
            voice "ch5.6_s_031"
            s "Ah, Tabitha and...{#ch5_6_v9962}"
            # JA[9962]: ああ、タバサと……。
            # [lay8 hide]
            $ show_sprites(("s 3 sad"))
            # [lay5 hide]
            $ show_sprites()
            # [lay0 hide]
            # [lay0 +632 → t 5]
            $ show_sprites(("t 5"))
            th "…….{#ch5.6_th_016}"
            # JA: ……。
            # [lay0 hide]
            $ show_sprites()
            # [lay5 +423 → s 3]
            $ show_sprites(("s 3"))
            # [lay8 +781 → h 3 sad]
            $ show_sprites(("h 3 sad", "s 3"))
            voice "ch5.6_s_032"
            s "Alright. Let me try to fix it.{#ch5_6_v9963}"
            # JA[9963]: 分かりました。 / 俺がなんとかしてみましょう。
            # [lay0 hide]
            $ show_sprites(("h 3 sad", "s 3"))
            # [lay8 +777 → h 3 happy]
            $ show_sprites(("h 3 happy", "s 3"))
            voice "ch5.6_h_006"
            h "Thank you very much!{#ch5_6_v468}"
            # JA[468]: ありがとうございます！
            # [lay8 hide]
            $ show_sprites(("s 3"))
            # [lay0 +632 → t 5]
            $ show_sprites(("t 5", "s 3"))
            # [lay5 +425 → s 3 happy]
            $ show_sprites(("t 5", "s 3 happy"))
            voice "ch5.6_s_033"
            s "T-Tabitha. By the way, what about the play casting?{#ch5_6_v9964}"
            # JA[9964]: タ、タバサ。 / そういえばお芝居の配役はどうなるのかな？
            voice "ch5.6_t_003"
            t "I don't know.{#ch5_6_v15461}"
            # JA[15461]: 分からない。
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("t 5", "s 3 sad"))
            th "W-was that too sudden?{#ch5.6_th_017}"
            # JA: （い、いきなりそれか？）
            # [lay5 hide]
            $ show_sprites(("t 5"))
            # [lay8 +777 → h 3 happy]
            $ show_sprites(("t 5", "h 3 happy"))
            voice "ch5.6_h_007"
            h "Right. Everyone's working hard, so anyone could be chosen.{#ch5_6_v469}"
            # JA[469]: そ、そうですよね。 / みんな頑張っていますし、 / 誰に決まってもおかしくないですわ。
            th "…….{#ch5.6_th_018}"
            # JA: ……。
            # [lay0 hide]
            $ show_sprites(("h 3 happy"))
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("s 1 sad", "h 3 happy"))
            voice "ch5.6_s_034"
            s "…….{#ch5_6_v9965}"
            # JA[9965]: ……。
            # [lay8 +781 → h 3 sad]
            $ show_sprites(("s 1 sad", "h 3 sad"))
            voice "ch5.6_h_008"
            h "Familiar~, that's not good, is it? The situation hasn't improved at all.{#ch5_6_v470}"
            # JA[470]: 使い魔さん、駄目じゃないですか？ / あまり状況が好転していませんよ。
            voice "ch5.6_s_035"
            s "No, even when you say that, to me...{#ch5_6_v9966}"
            # JA[9966]: いや、俺にそう言われても……。
            # [lay8 hide]
            $ show_sprites(("s 1 sad"))
            # [lay5 x=64]
            $ show_sprites(("s 1 sad"))
            th "What a problem. What should I talk about?{#ch5.6_th_019}"
            # JA: （困ったなぁ。 / 　何の話題を話そう）
            # ---- 【選択肢】 — выбор места в локации ----
            menu:
                "Topic: the weather{#ch5_6_c1424}":
                    # JA: 天気の話題
                    # ==== SCENE 1424 ====
                    # [if         if(isJump())] — не портируется
                    # [RESET      reset()] — сброс сцены: спрайты скрываются
                    $ show_sprites()
                    # [lay5 +396 → s 1 sad]
                    $ show_sprites(("s 1 sad"))
                    play music t9 fadein 1.0
                    # [BG +41 → id(41)]
                    $ fade_fx("id(41)")
                    # [lay5 +390 → s 1]
                    $ show_sprites(("s 1"))
                    # [lay0 +632 → t 5]
                    $ show_sprites(("t 5", "s 1"))
                    voice "ch5.6_s_036"
                    s "Tabitha, the weather is nice today.{#ch5_6_v9967}"
                    # JA[9967]: タバサ、今日は天気がいいな。
                    voice "ch5.6_t_004"
                    t "Sunny.{#ch5_6_v15462}"
                    # JA[15462]: 晴れ。
                    # [lay5 hide]
                    $ show_sprites(("t 5"))
                    # [lay8 +777 → h 3 happy]
                    $ show_sprites(("t 5", "h 3 happy"))
                    voice "ch5.6_h_009"
                    h "Yes, it's nice weather. On days like this, I want to run around in the fields.{#ch5_6_v471}"
                    # JA[471]: ええ、いい天気ですね。 / こういう天気の時は野原を / 駆け回りたいですね。
                    voice "ch5.6_t_005"
                    t "Books are better.{#ch5_6_v15463}"
                    # JA[15463]: 本がいい。
                    # [lay8 hide]
                    $ show_sprites(("t 5"))
                    # [lay0 hide]
                    $ show_sprites()
                    # [lay5 +396 → s 1 sad]
                    $ show_sprites(("s 1 sad"))
                    voice "ch5.6_s_037"
                    s "…….{#ch5_6_v9968}"
                    # JA[9968]: ……。
                    # [lay5 hide]
                    $ show_sprites()
                "Topic: the familiar{#ch5_6_c1425}":
                    # JA: 使い魔の話題
                    # ==== SCENE 1425 ====
                    # [if         if(isJump())] — не портируется
                    # [RESET      reset()] — сброс сцены: спрайты скрываются
                    $ show_sprites()
                    # [lay5 +396 → s 1 sad]
                    $ show_sprites(("s 1 sad"))
                    play music t9 fadein 1.0
                    # [BG +41 → id(41)]
                    $ fade_fx("id(41)")
                    # [lay5 +390 → s 1]
                    $ show_sprites(("s 1"))
                    # [lay0 +632 → t 5]
                    $ show_sprites(("t 5", "s 1"))
                    voice "ch5.6_s_038"
                    s "Hey, Tabitha, your familiar..., what was its name again.{#ch5_6_v9969}"
                    # JA[9969]: ほら、タバサ、お前の使い魔の…、 / なんて言ったっけ。
                    voice "ch5.6_t_006"
                    t "Sylphid.{#ch5_6_v15464}"
                    # JA[15464]: シルフィード。
                    # [lay5 +425 → s 3 happy]
                    $ show_sprites(("t 5", "s 3 happy"))
                    voice "ch5.6_s_039"
                    s "Yes! That Sylphid. Where is it usually?{#ch5_6_v9970}"
                    # JA[9970]: そう！ / そのシルフィード。 / 普段はどこにいるんだ？
                    voice "ch5.6_t_007"
                    t "It's in the sky.{#ch5_6_v15465}"
                    # JA[15465]: 空の上にいる。
                    # [lay5 hide]
                    $ show_sprites(("t 5"))
                    # [lay0 hide]
                    $ show_sprites()
                    # [BG hide] — поглощается переходом на CG
                    # [EVENT_CG +130 → id(130)]
                    $ fade_fx("id(130)", type="cg")
                    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
                    voice "ch5.6_h_010"
                    h "That's right. It's really up in the sky.{#ch5_6_v472}"
                    # JA[472]: 本当です。 / 空にちゃんといます。
                    voice "ch5.6_s_040"
                    s "You've always been together.{#ch5_6_v9971}"
                    # JA[9971]: いつも一緒にいたんだな。
                    voice "ch5.6_t_008"
                    t "With Saito.{#ch5_6_v15466}"
                    # JA[15466]: サイトと一緒。
                    # [lay8 hide]
                    # [lay5 hide]
                    # [lay0 hide]
                    # [BG hide]
                    $ fade_fx("black")
                    # [EVENT_CG hide] — поглощается переходом на CG
                    # [BG +41 → id(41)]
                    $ fade_fx("id(41)")
                    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
                "Topic: books{#ch5_6_c1426}":
                    # JA: 本の話題
                    # ==== SCENE 1426 ====
                    # [if         if(isJump())] — не портируется
                    # [RESET      reset()] — сброс сцены: спрайты скрываются
                    $ show_sprites()
                    # [lay5 +396 → s 1 sad]
                    $ show_sprites(("s 1 sad"))
                    play music t9 fadein 1.0
                    # [BG +41 → id(41)]
                    $ fade_fx("id(41)")
                    # [lay5 +390 → s 1]
                    $ show_sprites(("s 1"))
                    # [lay0 +632 → t 5]
                    $ show_sprites(("t 5", "s 1"))
                    voice "ch5.6_s_041"
                    s "Tabitha likes to read books, doesn't she?{#ch5_6_v9972}"
                    # JA[9972]: タバサは本を読むのが好きなんだよな。
                    voice "ch5.6_t_009"
                    t "Yes.{#ch5_6_v15467}"
                    # JA[15467]: うん。
                    # [lay5 hide]
                    $ show_sprites(("t 5"))
                    # [lay8 +777 → h 3 happy]
                    $ show_sprites(("t 5", "h 3 happy"))
                    voice "ch5.6_h_011"
                    h "Yes, it's nice weather. On days like this, I want to run around in the fields.{#ch5_6_v473}"
                    # JA[473]: だったら、今度王宮の書庫に来てみては / いかがですか？
                    voice "ch5.6_h_012"
                    h "That's right. It's really up in the sky.{#ch5_6_v474}"
                    # JA[474]: 持ち出しや、見せることができない本も / ありますが、ある程度の本は / お見せできると思いますよ。
                    # [lay0 +640 → t 5 shy]
                    $ show_sprites(("t 5 shy", "h 3 happy"))
                    voice "ch5.6_t_010"
                    t "…….{#ch5_6_v15468}"
                    # JA[15468]: ……。
                    $ update_sympathy(15, char_key="tabitha")
                    $ update_sympathy(30, char_key="henrietta")
                    # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
                    # [lay8 hide]
                    $ show_sprites(("t 5 shy"))
                    # [lay0 hide]
                    $ show_sprites()
                    # [lay5 +390 → s 1]
                    $ show_sprites(("s 1"))
                    th "She seems happy. Can't put it into words, can she?{#ch5.6_th_020}"
                    # JA: （なんだか、うれしそうだな。 / 　言葉にできないってやつかな？）
                    # [lay5 hide]
                    $ show_sprites()
            # ==== SCENE 1427 (rejoin, после мини-меню) ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            play music t9 fadein 1.0
            # [BG +41 → id(41)]
            $ fade_fx("id(41)")
            # [lay8 +775 → h 3]
            $ show_sprites(("h 3"))
            voice "ch5.6_h_013"
            h "Hmm. I think I have some idea now of how to talk to Tabitha-san.{#ch5_6_v475}"
            # JA[475]: うーん。 / なんとなくタバサさんとの会話の方法、 / 分かったような気がします。
            # [lay8 x=-96]
            $ show_sprites(("h 3"))
            # [lay5 +425 → s 3 happy]
            $ show_sprites(("h 3", "s 3 happy"))
            voice "ch5.6_s_042"
            s "R-really?{#ch5_6_v9973}"
            # JA[9973]: そ、そうですか？
            # [lay8 hide]
            $ show_sprites(("s 3 happy"))
            # [lay0 +638 → t 5 sad]
            $ show_sprites(("t 5 sad", "s 3 happy"))
            voice "ch5.6_t_011"
            t "I'm sorry.{#ch5_6_v15469}"
            # JA[15469]: ごめんなさい。
            # [lay5 +390 → s 1]
            $ show_sprites(("t 5 sad", "s 1"))
            voice "ch5.6_s_043"
            s "N-no, it's not Tabitha's fault. Next time, let's all talk a bit more.{#ch5_6_v9974}"
            # JA[9974]: い、いや、タバサのせいじゃねーって。 / 今度、もう少しみんなで話そうぜ。
            # [lay0 +634 → t 5 happy]
            $ show_sprites(("t 5 happy", "s 1"))
            voice "ch5.6_t_012"
            t "Yes.{#ch5_6_v15470}"
            # JA[15470]: うん。
            $ update_sympathy(30, char_key="tabitha")
            # [SET        set("se1", {stop = 1})] — SE не портируется
            stop music fadeout 1.0
            # [lay5 hide]
            $ show_sprites(("t 5 happy"))
            # [lay0 hide]
            $ show_sprites()
            # [BG hide]
            $ fade_fx("black")
        "To the main street{#ch5_6_c1428}":
            # JA: 表通り
            # ==== SCENE 1428 (ветка: head) ====
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [BG +38 → town]
            $ fade_fx("town", new_music="t30")
            # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1"))
            voice "ch5.6_s_044"
            s "...Huh? Wealthy-sama?{#ch5_6_v9975}"
            # JA[9975]: ……あれ？ / ウェザリーさん？
            # [lay20 x=-96]
            $ show_sprites(("w 1"))
            # [lay5 +390 → s 1]
            $ show_sprites(("w 1", "s 1"))
            voice "ch5.6_w_001"
            w "Ah, Saito...{#ch5_6_v15874}"
            # JA[15874]: ああ、サイトか……。
            # [lay20 hide]
            $ show_sprites(("s 1"))
            # [lay5 hide]
            $ show_sprites()
            # [BG hide]
            $ fade_fx("black")
            th "………. ……. ….{#ch5.6_th_021}"
            # JA: ………。 / ……。 / …。
            # [BG +55 → id(55)]
            $ fade_fx("id(55)")
            # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1"))
            # [lay5 +390 → s 1]
            $ show_sprites(("w 1", "s 1"))
            voice "ch5.6_s_045"
            s "By the way, Wealthy-sama, you said you used to be a noble, but why are you a traveling actor now?{#ch5_6_v9976}"
            # JA[9976]: そういえばウェザリーさんって前は、 / 貴族だったって言ってましたけど、 / どうして今は旅役者なんですか？
            # [lay20 +1063 → w 1 happy]
            $ show_sprites(("w 1 happy", "s 1"))
            voice "ch5.6_w_002"
            w "You know what, probing into a traveling actor's past is more than a little rude.{#ch5_6_v15875}"
            # JA[15875]: 旅役者の過去を詮索しようなんて / 野暮もいいところだよ。
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("w 1 happy", "s 1 sad"))
            voice "ch5.6_s_046"
            s "I-I'm sorry.{#ch5_6_v9977}"
            # JA[9977]: ご、ごめんなさい。
            # [lay20 +1067 → w 1 sad]
            $ show_sprites(("w 1 sad", "s 1 sad"))
            voice "ch5.6_w_003"
            w "Well, it's fine, though. By now, most of the mother country is already gone.{#ch5_6_v15876}"
            # JA[15876]: まあいいけどね。 / もう、祖国はほとんど残っていないしね。
            voice "ch5.6_s_047"
            s "Gone...? Does a country fall that easily?{#ch5_6_v9978}"
            # JA[9978]: 残っていないって……？ / そんな簡単に国が滅ぶんですか？
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1", "s 1 sad"))
            voice "ch5.6_w_004"
            w "You don't know what's going on in the world, do you. When a country falls, it's easy. Just like it's blown away.{#ch5_6_v15877}"
            # JA[15877]: きみは世間を知らないね。 / 滅ぶ時は簡単なものさ。 / 吹き飛ぶようにね。
            # [lay20 +1067 → w 1 sad]
            $ show_sprites(("w 1 sad", "s 1 sad"))
            voice "ch5.6_w_005"
            w "…It's only when you lose your country that you learn its value.{#ch5_6_v15878}"
            # JA[15878]: ……祖国というのは失ってはじめて / その価値を知るんだな。
            voice "ch5.6_w_006"
            w "Only when you consider the huge price of regaining it do people finally despair.{#ch5_6_v15879}"
            # JA[15879]: 取り戻すための代価の大きさを考えて、 / はじめて人は絶望するのさ。
            # [lay5 +390 → s 1]
            $ show_sprites(("w 1 sad", "s 1"))
            voice "ch5.6_s_048"
            s "At the place where I was born, I was taught that there are things more important than countries...{#ch5_6_v9979}"
            # JA[9979]: 俺が生まれたところじゃ、 / 国とかよりもっと大切なものがあるって / 教えられましたけど。
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1", "s 1"))
            voice "ch5.6_w_007"
            w "For example?{#ch5_6_v15880}"
            # JA[15880]: たとえば？
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("w 1", "s 3 sad"))
            voice "ch5.6_s_049"
            s "Let me see... equality... family... a lover...{#ch5_6_v9980}"
            # JA[9980]: ええと、平等とか、家族とか恋人とか……。
            voice "ch5.6_w_008"
            w "I wouldn't say it's wrong. But that's something only someone rich enough to be overflowing with wealth can say.{#ch5_6_v15881}"
            # JA[15881]: 間違いとは言わない。 / だが、それは富にあふれた人の言う台詞だな。
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("w 1", "s 1 sad"))
            voice "ch5.6_s_050"
            s "Wealthy-sama?{#ch5_6_v9981}"
            # JA[9981]: ウェザリーさん？
            voice "ch5.6_w_009"
            w "I think I talked too much. I'll go rest over there...{#ch5_6_v15882}"
            # JA[15882]: 少し話しすぎたみたいだな。 / わたしは奥で休んでることにしよう……。
            # [SET        set("se1", {stop = 1})] — SE не портируется
            stop music fadeout 1.0
            # [lay20 hide]
            $ show_sprites(("s 1 sad"))
            # [lay5 hide]
            $ show_sprites()
            # [BG hide]
            $ fade_fx("black")

    # [移動] → next(341): сцена 341 (core) — часть 7 главы 5
    jump ch5_7
