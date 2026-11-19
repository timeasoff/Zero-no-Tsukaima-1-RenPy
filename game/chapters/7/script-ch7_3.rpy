# Глава 7, часть 3 (сцены 400-404, 1169-1173): «失望のお姫さま» — финал главы.
# Возвращение отряда в гостиницу; слёзы Сиесты (развилка «успокоить Сайто»);
#    совет с Анриеттой (Реконкиста, обязанности королевы); гейт даты:
#    дата с Анриеттой (1169-1173, ночная тема о принцессе с Уэзерби)
#    или постдата → сцена 405 (глава 9).
# Источник: ps2_source/chapters/chapter_08_失望のお姫さま.txt (src L1094-1490).
# Точные аргументы: ps2_source/events_full/chapter_08_失望のお姫さま.txt (L1010-1379).
#
# Вход — jump ch7_3 из script-ch7_2.rpy (конец сцены 399); выход — jump attention
#   (PROVISIONAL: постдата +405 = глава 9, не портирована; постдата гейта даты
#   и финал сцены 1173 → next(405)).
#
# Голоса: ch7.3_<spk>_<NNN> — нумерация с 001 по говорящему в порядке источника
#   (сцены 400 → 401 → 402 → 403 → 404 → 1169 → 1170 → 1171 → 1172 → 1173;
#   ветки в порядке пунктов меню):
#   s ×36 (13546-13559, 9167-9188), l ×13 (7394-7406), si ×8 (15159-15166),
#   g ×2 (1560, 1561), m ×3 (4169-4171), h ×28 (845-851, 412-432), k ×4
#   (3854-3857), t ×1 (15810) — всего 95. Мысль Сайто без голоса (сцена 404,
#   тег ch7.3_th_404a). Реплик без голоса в этом диапазоне нет. Пункты меню — 6
#   (ch7.3_c401..c403 из сцены 400, ch7.3_c1170..c1172 из сцены 1169).
#
# Не портируются: SE (+57,+62,+82,+55,+56, se1 stop — система не реализована),
#   MSGON/MSGOFF, BACK, WAIT (waitTime/waitAction), RESET/TRANS (переход через
#   fade_fx), point x=/y= позиции (в т.ч. offstage y=416 сцены 404),
#   [COFFEE] → $ pause(1.0), MOVIE (нет).
#
# BGM: +25 → t24, +26 → t25, +16 → t15 (все в game/definitions.rpy).
# Фоны: 52/43 — имена пусты в image_id_map.csv (заглушки id(52)/id(43));
#   40 = town_night, 60 = town_square_night, 90 = sky_night.
# Спрайты (references/sprite_id_map.csv): 405=s 2 angry, 407=s 2 sad,
#   403=s 2 happy, 401=s 2, 440=s 4 sad, 429=s 3 sad, 390=s 1, 396=s 1 sad,
#   394=s 1 angry; 306=l 1 angry, 302=l 1, 310=l 1 shy, 339=l 3 angry,
#   308=l 1 sad; 561=g 1 sad, 572=g 2 sad PROV; 891=m 4 sad, 858=m 1 sad;
#   779=h 3 angry PROV, 775=h 3 PROV, 781=h 3 sad PROV, 786=h 2 PROV,
#   792=h 2 sad PROV; 528=si 4 sad, 495=si 1 sad, 493=si 1 angry;
#   682=k 1 sad, 676=k 1, 709=k 4; 588=t 1 (LAYER lay0).
#   790 (сцена 1171) в справочнике нет — файла в медиа нет, не показывается
#   (прецедент 1017/1111 в script-ch7_2.rpy).
# Меню 【選択肢】: две развилки по три варианта (400 → 401/402/403 → 404;
#   1169 → 1170/1171/1172 → 1173) — варианты сливаются в общие сцены
#   (fall-through после меню, прецедент script-ch7_2.rpy).
# Гейт даты (конец сцены 404) реплицирует script-ch6_3.rpy; dére-слот 0 —
#   call sp_l1 (K=12), постдата +405 — jump attention (PROVISIONAL).

label ch7_3:

    # ==== SCENE 400 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +52 → id(52)]
    $ fade_fx("id(52)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [BGM play=+25 → t24]
    play music t24 fadein 1.0
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("s 2 angry",))
    voice "ch7.3_s_001"
    s "Is everyone all right!{#ch7.3_s_001}"
    # JA[13546]: みんな、無事か！
    # [lay5 y=0,x=224]
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("s 2 angry", "l 1 angry"))
    voice "ch7.3_l_001"
    l "Hardly!{#ch7.3_l_001}"
    # JA[7394]: 無事じゃないわよ！
    # [lay5 hide]
    # [lay1 hide]
    $ show_sprites()
    # [lay4 +561 → g 1 sad]
    $ show_sprites(("g 1 sad",))
    voice "ch7.3_g_001"
    g "Ha-ha-ha… A bunch like that — with me on the job, they might as well have been babies… yeah.{#ch7.3_g_001}"
    # JA[1560]: は、は、は……。 / あんな連中、ぼくにかかれば赤子も同然……さ。
    # [lay4 y=0,x=224]
    # [lay3 +891 → m 4 sad]
    $ show_sprites(("g 1 sad", "m 4 sad"))
    voice "ch7.3_m_001"
    m "Honestly — saying it while your knees are shaking doesn't exactly make it convincing.{#ch7.3_m_001}"
    # JA[4169]: もう、膝がくがくさせながら言っても / 説得力ないわよ。
    # [lay3 +858 → m 1 sad]
    $ show_sprites(("g 1 sad", "m 1 sad"))
    voice "ch7.3_m_002"
    m "I know you tried your hardest, so don't strain yourself keeping up appearances.{#ch7.3_m_002}"
    # JA[4170]: 頑張ったのは知ってるから、 / 無理に見栄はらないで。
    # [lay4 hide]
    # [lay3 hide]
    $ show_sprites()
    # [lay8 +779 → h 3 angry — PROVISIONAL]
    $ show_sprites(("h 3 angry",))
    voice "ch7.3_h_001"
    h "This being the case, I worry about Siesta back at the inn. Let's hurry home.{#ch7.3_h_001}"
    # JA[845]: こうなると、宿のシエスタさんが心配です。 / 早く戻りましょう。
    # [lay8 y=0,x=-96]
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("s 2 angry",))
    voice "ch7.3_s_002"
    s "Right — Siesta! She should still be back at the inn with Haruna!{#ch7.3_s_002}"
    # JA[13547]: そうだ、シエスタ！ / 春奈と一緒に宿屋に残っていたはずだ！
    # [lay8 hide]
    # [lay1 +339 → l 3 angry]
    $ show_sprites(("l 3 angry",))
    voice "ch7.3_l_002"
    l "Then, don't tell me those people…!?{#ch7.3_l_002}"
    # JA[7395]: じゃ、もしかしてあいつらに……！？
    voice "ch7.3_s_003"
    s "Let's hurry back!{#ch7.3_s_003}"
    # JA[13548]: 急いで戻ろう！
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1",))
    voice "ch7.3_l_003"
    l "Yes!{#ch7.3_l_003}"
    # JA[7396]: ええ！
    # [BGM stop] — стоп музыки
    stop music fadeout 1.0
    # [MSGOFF     msgoff()] — не портируется
    # [lay1 hide]
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    # [BG +60 → town_square_night]
    $ fade_fx("town_square_night")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [WAIT       waitTime(500, true)] — не портируется
    # [BG +40 → town_night]
    $ fade_fx("town_night")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [WAIT       waitTime(500, true)] — не портируется
    # [BG +43 → id(43)]
    $ fade_fx("id(43)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [BGM play=+26 → t25]
    play music t25 fadein 1.0
    # [SE        se0      play=+57] — не портируется (система SE)
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("s 2 angry",))
    voice "ch7.3_s_004"
    s "Siesta! You're okay, Siesta!?{#ch7.3_s_004}"
    # JA[13549]: シエスタ！ / 無事か、シエスタ！
    # [lay5 y=0,x=224]
    # [lay2 +528 → si 4 sad]
    $ show_sprites(("si 4 sad",))
    voice "ch7.3_si_001"
    si "Ah….{#ch7.3_si_001}"
    # JA[15159]: あ……。
    # [lay2 +495 → si 1 sad]
    $ show_sprites(("si 1 sad",))
    voice "ch7.3_si_002"
    si "Saito-san, everyone! Weeh… weeeeh-hah!{#ch7.3_si_002}"
    # JA[15160]: サイトさん、皆さん！ / ふえ……ふえええええん！
    # [lay5 +440 → s 4 sad]
    $ show_sprites(("s 4 sad", "si 1 sad"))
    voice "ch7.3_s_005"
    s "Whoa — Siesta?{#ch7.3_s_005}"
    # JA[13550]: おっと、シエスタ？
    voice "ch7.3_si_003"
    si "Haruna-san suddenly got such a scary face and left somewhere, and then… hic. And then I heard explosions from outside…{#ch7.3_si_003}"
    # JA[15161]: いきなりハルナさんが怖い顔になって、 / どこかに行ってしまって……ひっく。 / そしたら、外から爆発が聞こえるし……。
    voice "ch7.3_si_004"
    si "And nobody came back, and I… I…!{#ch7.3_si_004}"
    # JA[15162]: 誰も帰って来ないし、わたし、わたしぃ……！
    # [lay5 +407 → s 2 sad]
    $ show_sprites(("s 2 sad", "si 1 sad"))
    voice "ch7.3_s_006"
    s "Siesta…….{#ch7.3_s_006}"
    # JA[13551]: シエスタ……。

    # ---- 【選択肢】 ----
    menu:
        "We all came back, so it's all right already.{#ch7.3_c401}":
            # JA: 俺達が帰ってきたからもう大丈夫だ
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay2 +495 → si 1 sad]
            # [lay5 +407 → s 2 sad]
            $ show_sprites(("si 1 sad", "s 2 sad"))
            # [BGM play=+26 → t25] — музыка раньше фона
            play music t25 fadein 1.0
            # [BG +43 → id(43)]
            $ fade_fx("id(43)")
            # [lay5 +403 → s 2 happy]
            $ show_sprites(("si 1 sad", "s 2 happy"))
            voice "ch7.3_s_007"
            s "We've all come back, so everything's fine now.{#ch7.3_s_007}"
            # JA[13552]: 俺達が帰ってきたから、もう大丈夫だよ。
            voice "ch7.3_si_005"
            si "Saito-saaan…!{#ch7.3_si_005}"
            # JA[15163]: サイトさあん……！
            # [lay2 hide]
            # [lay1 +310 → l 1 shy]
            $ show_sprites(("s 2 happy", "l 1 shy"))
            voice "ch7.3_l_004"
            l "Mmgh — ugh…!{#ch7.3_l_004}"
            # JA[7397]: うー、うー！
            # [lay5 hide]
            # [lay6 +682 → k 1 sad]
            $ show_sprites(("l 1 shy", "k 1 sad"))
            voice "ch7.3_k_001"
            k "Settle down, Louise. You can surely imagine how lonely Siesta must have felt, can't you?{#ch7.3_k_001}"
            # JA[3854]: 落ち着きなさい、ルイズ。 / シエスタがどれだけ心細かったか、 / 分かるでしょ。
            # [lay1 +339 → l 3 angry]
            $ show_sprites(("k 1 sad", "l 3 angry"))
            voice "ch7.3_l_005"
            l "I do understand. Even I wouldn't be so boorish as to say otherwise. It's that fool's pathetic, lovesick face that sets me off, that's all!{#ch7.3_l_005}"
            # JA[7398]: 分かってるわよ。 / いくらわたしでも、そこまで野暮じゃないわ。 / あの馬鹿の情けないでれでれ顔が腹立つだけよ！
            # [lay6 hide]
            # [LAYER     lay0     image=+588, level=160, dir=1A] → t 1
            $ show_sprites(("l 3 angry", "t 1"))
            voice "ch7.3_t_001"
            t "Jealousy.{#ch7.3_t_001}"
            # JA[15810]: 嫉妬。
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("t 1", "l 1 angry"))
            voice "ch7.3_l_006"
            l "It is not!{#ch7.3_l_006}"
            # JA[7399]: そんなんじゃないわ！
            # [移動] → next(404)

        "Don't fret over Haruna now.{#ch7.3_c402}":
            # JA: 春奈のことは、気にするな
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay2 +495 → si 1 sad]
            # [lay5 +407 → s 2 sad]
            $ show_sprites(("si 1 sad", "s 2 sad"))
            # [BGM play=+26 → t25] — музыка раньше фона
            play music t25 fadein 1.0
            # [BG +43 → id(43)]
            $ fade_fx("id(43)")
            # [lay5 +401 → s 2]
            $ show_sprites(("si 1 sad", "s 2"))
            voice "ch7.3_s_008"
            s "Don't worry about Haruna.{#ch7.3_s_008}"
            # JA[13553]: 春奈のことは、気にするな。
            # [lay2 +493 → si 1 angry]
            $ show_sprites(("s 2", "si 1 angry"))
            voice "ch7.3_si_006"
            si "But still, but still…!{#ch7.3_si_006}"
            # JA[15164]: だって、だって……！
            voice "ch7.3_s_009"
            s "The truth is, Haruna was being controlled by those bad men through magic. So we're the ones who have to go save her.{#ch7.3_s_009}"
            # JA[13554]: 実は、春奈は、悪いやつらに魔法で / 操られてたんだ。 / だから、俺達で助けないと。
            # [lay5 +403 → s 2 happy]
            $ show_sprites(("s 2 happy", "si 1 angry"))
            voice "ch7.3_s_010"
            s "I'm sorry we put you through something that frightening, Siesta.{#ch7.3_s_010}"
            # JA[13555]: シエスタには、怖い思いをさせてしまって / ごめんな。
            # [lay2 +495 → si 1 sad]
            $ show_sprites(("s 2 happy", "si 1 sad"))
            voice "ch7.3_si_007"
            si "No, it's not as if you did anything wrong, Saito-san. It's just that I was so startled…{#ch7.3_si_007}"
            # JA[15165]: いいえ、サイトさんが悪いわけじゃないんです。 / ただ、わたしびっくりしてしまって……。
            # [lay2 hide]
            # [lay1 +302 → l 1]
            $ show_sprites(("s 2 happy", "l 1"))
            voice "ch7.3_l_007"
            l "Setting aside holding back those men — just how, concretely, are we supposed to rescue Haruna, I wonder?{#ch7.3_l_007}"
            # JA[7400]: でも、やつらを止めるのはともかく、 / 具体的にどうやったらハルナを / 助けられるのかしら。
            # [TNDL      tndl(50)]
            $ tndl(50)
            # [lay5 hide]
            # [lay8 +781 → h 3 sad — PROVISIONAL]
            $ show_sprites(("h 3 sad",))
            voice "ch7.3_h_002"
            h "……{#ch7.3_h_002}"
            # JA[846]: ……。
            # [移動] → next(404)

        "Come cry in my arms right now.{#ch7.3_c403}":
            # JA: 今は俺の胸でお泣き
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay2 +495 → si 1 sad]
            # [lay5 +407 → s 2 sad]
            $ show_sprites(("si 1 sad", "s 2 sad"))
            # [BGM play=+26 → t25] — музыка раньше фона
            play music t25 fadein 1.0
            # [BG +43 → id(43)]
            $ fade_fx("id(43)")
            # [lay5 +409 → s 2 shy]
            $ show_sprites(("si 1 sad", "s 2 shy"))
            voice "ch7.3_s_011"
            s "Come cry in my arms right now.{#ch7.3_s_011}"
            # JA[13556]: 今は俺の胸でお泣き。
            voice "ch7.3_si_008"
            si "Saito-saaan…!{#ch7.3_si_008}"
            # JA[15166]: サイトさあん……っ！
            # [lay2 hide]
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("s 2 shy", "l 1 angry"))
            voice "ch7.3_l_008"
            l "Don't get carried away!{#ch7.3_l_008}"
            # JA[7401]: 調子に乗るなっ！
            # [SE        se0      play=+62] — не портируется (система SE)
            # [VIBRATE vibrate(2)] — не портируется; дрожание экрана → shake_fx
            $ shake_fx(duration=0.8)
            # [stage/event/lay* hide, reset] — спрайты восстанавливаются на месте
            # [lay5 +405 → s 2 angry]
            $ show_sprites(("l 1 angry", "s 2 angry"))
            voice "ch7.3_s_012"
            s "Guooh! You just sock me with a fist out of nowhere!?{#ch7.3_s_012}"
            # JA[13557]: ぐおおっ！ / いきなりぐーで殴るかお前っ！？
            # [lay1 +339 → l 3 angry]
            $ show_sprites(("s 2 angry", "l 3 angry"))
            voice "ch7.3_l_009"
            l "I understand about comforting Siesta, but a lovesick display like that is not authorized!{#ch7.3_l_009}"
            # JA[7402]: シエスタをなぐさめるのは分かるけど、 / そこでデレデレするあんたは不許可よっ！
            # [TNDL tndl(-40)]
            $ tndl(-40)
            # [移動] → next(404)

    # ==== SCENE 404 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [LAYER     lay0     image=+588, level=160, dir=1A] → t 1
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("t 1", "l 1 angry"))
    # [BGM play=+26 → t25] — музыка раньше фона
    play music t25 fadein 1.0
    # [BG +43 → id(43)]
    $ fade_fx("id(43)")
    # [lay1 hide]
    # [LAYER     lay0     hide]
    # [lay5 y=416,x=464] — offstage-позиция не портируется
    # [lay8 y=416,x=144] — offstage-позиция не портируется
    $ show_sprites()
    # [lay6 +676 → k 1]
    $ show_sprites(("k 1",))
    voice "ch7.3_k_002"
    k "In any case, the Reconquista may well swing into full motion. Her Majesty had best head back to the castle.{#ch7.3_k_002}"
    # JA[3855]: とにかく、レコン・キスタが本格的に / 動き出すかもしれない。 / 女王陛下はお城に戻った方がいいわね。
    # [lay6 y=0,x=224]
    # [lay1 +302 → l 1]
    $ show_sprites(("k 1", "l 1"))
    voice "ch7.3_l_010"
    l "In the meantime, we will stop Weatherby and Akina ourselves. We simply have to see this through to a proper reckoning.{#ch7.3_l_010}"
    # JA[7403]: その間に、私達でウェザリーとアキナを / 止めるわ。 / 落とし前はきっちりつけさせてもらわないとね。
    # [lay6 +709 → k 4]
    $ show_sprites(("k 4", "l 1"))
    voice "ch7.3_k_003"
    k "That's right. They looked down on us, and that has to be paid for.{#ch7.3_k_003}"
    # JA[3856]: そうね。 / あたし達を舐めたこと、 / お返ししないといけないわね。
    # [lay1 hide]
    # [lay6 hide]
    # [lay8 +781 → h 3 sad — PROVISIONAL]
    $ show_sprites(("h 3 sad",))
    voice "ch7.3_h_003"
    h "So in the end, there was nothing at all that I could manage, was there.{#ch7.3_h_003}"
    # JA[847]: 結局、わたくしには何もできなかった / わけですね。
    # [lay8 y=0,x=-96]
    # [lay5 +440 → s 4 sad]
    $ show_sprites(("h 3 sad", "s 4 sad"))
    voice "ch7.3_s_013"
    s "I'm sorry, Princess. Our investigation couldn't quite keep up.{#ch7.3_s_013}"
    # JA[13558]: すみません、お姫さま。 / 俺達の調査がおいつかなくて。
    # [lay8 +775 → h 3 — PROVISIONAL]
    $ show_sprites(("h 3", "s 4 sad"))
    voice "ch7.3_h_004"
    h "No — if you consider how this whole affair began, it was because I was still green as a queen.{#ch7.3_h_004}"
    # JA[848]: いいえ、そもそもの発端を考えれば、 / わたくしが女王として未熟だったからです。
    # [lay8 +781 → h 3 sad — PROVISIONAL]
    $ show_sprites(("h 3 sad", "s 4 sad"))
    voice "ch7.3_h_005"
    h "And because of that, I gave them the opening they needed to win over the nobles within our realm. {#ch7.3_h_005}"
    # JA[849]: そのために、国内の貴族達を籠絡する / 隙を与えてしまった。
    # [lay5 +401 → s 2]
    $ show_sprites(("h 3 sad", "s 2"))
    voice "ch7.3_s_014"
    s "None of that is something you need to brood over, Princess.{#ch7.3_s_014}"
    # JA[13559]: そんなの、お姫さまが気に病むこと / じゃないですよ。
    voice "ch7.3_h_006"
    h "It makes me happy to hear you say so, but… nevertheless, as long as I am Queen, I must bear the responsibility…{#ch7.3_h_006}"
    # JA[850]: そう言ってくれるのは嬉しいけど……。 / でも、女王である以上、わたくしはやはり / 責を負わねばなりません……。
    # [lay5 hide]
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad",))
    voice "ch7.3_l_011"
    l "Your Highness… please don't blame yourself so much.{#ch7.3_l_011}"
    # JA[7404]: 姫さま……そんなにご自分を責めないで / ください。
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1",))
    voice "ch7.3_l_012"
    l "Whatever reasons there may be, the fact remains that they are in the wrong.{#ch7.3_l_012}"
    # JA[7405]: どんな理由があろうが、あいつらが悪いことは / 変わりません。
    voice "ch7.3_h_007"
    h "Forgive me… Might I lie down for a little while?{#ch7.3_h_007}"
    # JA[851]: すみません……。 / わたくし、少し横にならせてください。
    # [lay8 hide]
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad",))
    voice "ch7.3_l_013"
    l "Your Highness… She's taking it quite hard, I'd say.{#ch7.3_l_013}"
    # JA[7406]: 姫さま……。 / かなり、気にしてるわね。
    # [lay1 y=0,x=-96]
    # [lay6 +682 → k 1 sad]
    $ show_sprites(("k 1 sad", "l 1 sad"))
    voice "ch7.3_k_004"
    k "For tonight, let's leave her be.{#ch7.3_k_004}"
    # JA[3857]: 今晩のところは、１人にしてあげましょう。
    # [lay1 hide]
    # [lay6 hide]
    # [lay4 +572 → g 2 sad — PROVISIONAL]
    $ show_sprites(("g 2 sad",))
    voice "ch7.3_g_002"
    g "Ahh — what a thing to happen! If only it could be me to comfort her–!{#ch7.3_g_002}"
    # JA[1561]: ああっ、なんということだ。 / ぼくがなぐさめてあげられるのならばー！
    # [lay6 hide]
    # [lay3 +891 → m 4 sad]
    $ show_sprites(("g 2 sad", "m 4 sad"))
    voice "ch7.3_m_003"
    m "You'd better calm down yourself.{#ch7.3_m_003}"
    # JA[4171]: あなたも落ち着きなさい。
    # [lay4 hide]
    # [lay3 hide]
    # [lay5 +407 → s 2 sad]
    $ show_sprites(("s 2 sad",))
    th "Princess… she's so serious about everything that moments like this must weigh on her all the heavier…{#ch7.3_th_404a}"
    # JA: （お姫さま……真面目なだけに、 / 　こういうときは辛いんだろうな……）
    # [MSGOFF     msgoff()] — не портируется
    # [SE        se1      stop=1] — не портируется (система SE)
    # [BGM stop] — стоп музыки
    stop music fadeout 1.0
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [WAIT       waitTime(1000, true)] — не портируется
    # Date gate (events_full chapter_08 L229-230):
    #   dateItem("アンリエッタ", +1169); date(+405, false, +4).
    # Дере/тундере-событие вместо даты — гейт как в script-ch6_3.rpy (эталон
    # script-ch5_10.rpy): zero_tundele >= 211 → tndl_pick() (dére, chapter_91);
    # слот 0 дере — ухаживание (sp_l1), K=12; остальные дере-слоты 1..5 и весь
    # тундере-блок (chapter_90) не портированы → fallthrough в дату.
    if zero_tundele >= 211:
        $ zero_tndl_no = tndl_pick(zero_dele_event)
        if zero_tndl_no == 0:
            $ zero_dele_event[0] += 1
            $ zero_tundele_count += 1
            call sp_l1 from _call_sp_l1_12
            $ fade_fx("black")
            stop music fadeout 1.0
            # Постдата +405 = глава 9 (не портирована): PROVISIONAL-конец,
            # перецепится на ch8 при портировании.
            jump attention

    jump ch7_3_s1169

label ch7_3_s1169:
    # ==== SCENE 1169 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BACK       back()] — не портируется
    # [BG +90 → sky_night]
    $ fade_fx("sky_night")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [BGM play=+16 → t15]
    play music t15 fadein 1.0
    # [SE        se0      play=+82] — не портируется (система SE)
    voice "ch7.3_s_015"
    s "Princess? I'm coming in.{#ch7.3_s_015}"
    # JA[9167]: お姫さま？ / 入りますよ？
    # [SE        se0      play=+55] — не портируется (система SE)
    # [MSGOFF     msgoff()] — не портируется
    # [lay5 hide]
    # [BG hide]
    $ show_sprites()
    # [WAIT       waitAction(null, true)] — не портируется
    # [BACK       back()] — не портируется
    # [BG +43 → id(43)]
    $ fade_fx("id(43)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [SE        se0      play=+56] — не портируется (система SE)
    # [lay8 +792 → h 2 sad — PROVISIONAL]
    $ show_sprites(("h 2 sad",))
    # [MSGON      msgon()] — не портируется
    voice "ch7.3_h_008"
    h "Ah… the familiar… {#ch7.3_h_008}"
    # JA[412]: あ……使い魔さん……。
    # [lay8 y=0,x=-96]
    # [lay5 +390 → s 1]
    $ show_sprites(("h 2 sad", "s 1"))
    voice "ch7.3_s_016"
    s "You're awake after all, I see.{#ch7.3_s_016}"
    # JA[9168]: やっぱり、起きてたんですね。
    voice "ch7.3_h_009"
    h "Yes. I couldn't sleep…{#ch7.3_h_009}"
    # JA[413]: ええ、眠れなくて……。
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("h 2 sad", "s 3 sad"))
    voice "ch7.3_s_017"
    s "Over your thoughts?{#ch7.3_s_017}"
    # JA[9169]: 考えごとで？
    # [lay8 +786 → h 2 — PROVISIONAL]
    $ show_sprites(("h 2", "s 3 sad"))
    voice "ch7.3_h_010"
    h "Yes. Every time I catch myself, I begin to think it over. This entire incident was, in the end, all my…{#ch7.3_h_010}"
    # JA[414]: はい。 / ふと気がつくと、考えてしまうのです。 / 今回の事件は全てわたくしの……。
    # [lay8 +792 → h 2 sad — PROVISIONAL]
    $ show_sprites(("h 2 sad", "s 3 sad"))
    voice "ch7.3_h_011"
    h "…that it was a blunder of my own making, I can't help but think. And when I think of that…{#ch7.3_h_011}"
    # JA[415]: わたくしの失態ではないかと……。 / それを思うと……。
    # [lay5 +390 → s 1]
    $ show_sprites(("h 2 sad", "s 1"))
    voice "ch7.3_s_018"
    s "…You haven't touched your supper, have you? Worrying is worrying, but you still have to eat.{#ch7.3_s_018}"
    # JA[9170]: ……夕食、手をつけてないじゃないですか。 / 悩んでても、ご飯は食べなきゃ。
    voice "ch7.3_h_012"
    h "Yes…{#ch7.3_h_012}"
    # JA[416]: ええ……。
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("h 2 sad", "s 1 sad"))
    voice "ch7.3_s_019"
    s "Princess…{#ch7.3_s_019}"
    # JA[9171]: お姫さま……。

    # ---- 【選択肢】 ----
    menu:
        "You must take better care of yourself.{#ch7.3_c1170}":
            # JA: 自分を大切にしてください
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay8 +792 → h 2 sad — PROVISIONAL]
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("h 2 sad", "s 1 sad"))
            # [BGM play=+16 → t15] — музыка раньше фона
            play music t15 fadein 1.0
            # [BG +43 → id(43)]
            $ fade_fx("id(43)")
            # [lay5 +390 → s 1]
            $ show_sprites(("h 2 sad", "s 1"))
            voice "ch7.3_s_020"
            s "You must take better care of yourself.{#ch7.3_s_020}"
            # JA[9172]: 自分を大切にしてください。
            voice "ch7.3_h_013"
            h "Take care… I make every effort to. No — everyone treats me so kindly. Perhaps even more kindly than I believe I deserve…{#ch7.3_h_013}"
            # JA[417]: 大切に……しているつもりです。 / いえ、皆がわたくしを大切に扱ってくれます。 / おそらく、わたくしが思っている以上に……。
            voice "ch7.3_s_021"
            s "That's exactly right. So it is you too, Princess, who…{#ch7.3_s_021}"
            # JA[9173]: そうです。 / だから、お姫さまも……。
            # [lay8 +786 → h 2 — PROVISIONAL]
            $ show_sprites(("h 2", "s 1"))
            voice "ch7.3_h_014"
            h "If even a tiny, tiny fragment of the care that is poured out on me…{#ch7.3_h_014}"
            # JA[418]: その、わたくしに注がれた分の / ほんのわずかでも……。
            # [lay8 +792 → h 2 sad — PROVISIONAL]
            $ show_sprites(("h 2 sad", "s 1"))
            voice "ch7.3_h_015"
            h "…had been given to Miss Weatherby as well — would she not then have refrained from doing what she has done?{#ch7.3_h_015}"
            # JA[419]: ミス・ウェザリーにも与えられていたなら、 / 彼女はこのようなことをしなかったの / でしょうか。
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("h 2 sad", "s 1 sad"))
            voice "ch7.3_s_022"
            s "That's…{#ch7.3_s_022}"
            # JA[9174]: それは……。
            # [移動] → next(1173)

        "Thinking about needless things is a waste.{#ch7.3_c1171}":
            # JA: 余計なことを考えるだけ無駄
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay8 +792 → h 2 sad — PROVISIONAL]
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("h 2 sad", "s 1 sad"))
            # [BGM play=+16 → t15] — музыка раньше фона
            play music t15 fadein 1.0
            # [BG +43 → id(43)]
            $ fade_fx("id(43)")
            # [lay5 +390 → s 1]
            $ show_sprites(("h 2 sad", "s 1"))
            voice "ch7.3_s_023"
            s "Thinking about needless things is a waste, you know.{#ch7.3_s_023}"
            # JA[9175]: 余計なことを考えるだけ無駄ですよ。
            # [lay8 +790] — спрайт отсутствует в справочнике (файла в медиа нет),
            #   не показывается (прецедент 1017/1111 в script-ch7_2.rpy)
            voice "ch7.3_h_016"
            h "Needless things? Can what Miss Weatherby suffered — the unprovoked outrage done to her — really be called needless?{#ch7.3_h_016}"
            # JA[420]: 余計なこと？ / ミス・ウェザリーが受けた、いわれなき所業を、 / 余計なことと言うのですか？
            voice "ch7.3_s_024"
            s "At the very least, for you as you are now, Princess — isn't it needless?{#ch7.3_s_024}"
            # JA[9176]: 少なくとも、今のお姫さまにとっては、 / 余計なことじゃないですか？
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("h 2 sad", "s 3 sad"))
            voice "ch7.3_s_025"
            s "Even if everything Weatherby says were true — what she is actually doing is wrong.{#ch7.3_s_025}"
            # JA[9177]: ウェザリーの言ってることが正しいとしても、 / 彼女がやってることは間違ってます。
            # [lay8 +792 → h 2 sad — PROVISIONAL]
            $ show_sprites(("h 2 sad", "s 3 sad"))
            voice "ch7.3_h_017"
            h "That may well be so, but still.{#ch7.3_h_017}"
            # JA[421]: それは、そうですが。
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("h 2 sad", "s 1 angry"))
            voice "ch7.3_s_026"
            s "What we have to do right now is protect the realm and the town from this scheme — not sympathize with Weatherby.{#ch7.3_s_026}"
            # JA[9178]: 今、俺達がしなくちゃいけないのは、 / この企みから国や街を守ることです。 / ウェザリーに同情することじゃありません。
            # [lay8 +786 → h 2 — PROVISIONAL]
            $ show_sprites(("h 2", "s 1 angry"))
            voice "ch7.3_h_018"
            h "That is true, isn't it.{#ch7.3_h_018}"
            # JA[422]: そうですね。
            # [移動] → next(1173)

        "Leaving food uneaten is a shame, you know.{#ch7.3_c1172}":
            # JA: 食べないとご飯がもったいない
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay8 +792 → h 2 sad — PROVISIONAL]
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("h 2 sad", "s 1 sad"))
            # [BGM play=+16 → t15] — музыка раньше фона
            play music t15 fadein 1.0
            # [BG +43 → id(43)]
            $ fade_fx("id(43)")
            # [lay5 +390 → s 1]
            $ show_sprites(("h 2 sad", "s 1"))
            voice "ch7.3_s_027"
            s "Leaving food uneaten is a shame, you know.{#ch7.3_s_027}"
            # JA[9179]: 食べないとご飯がもったいないですよ。
            voice "ch7.3_h_019"
            h "A shame…?{#ch7.3_h_019}"
            # JA[423]: もったいない……？
            voice "ch7.3_s_028"
            s "Indeed. Seven gods dwell within your bowl of rice, they say. Leaving a meal unfinished is not to be done.{#ch7.3_s_028}"
            # JA[9180]: そうです。 / ご飯には７人の神様が宿るんですよ。 / 食事は残しちゃ駄目です。
            # [lay8 +786 → h 2 — PROVISIONAL]
            $ show_sprites(("h 2", "s 1"))
            voice "ch7.3_h_020"
            h "You are… rather sturdy in spirit, aren't you. I suppose that kind of strength of heart… is something I lack.{#ch7.3_h_020}"
            # JA[424]: あなたは……たくましいのですね。 / わたくしには、そんな心の強さが……、 / 足りないのでしょう。
            # [移動] → next(1173)

    # ==== SCENE 1173 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay8 +792 → h 2 sad — PROVISIONAL]
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("h 2 sad", "s 1 sad"))
    # [BGM play=+16 → t15] — музыка раньше фона
    play music t15 fadein 1.0
    # [BG +43 → id(43)]
    $ fade_fx("id(43)")
    # [lay8 +792] — образ на месте (повторный вызов в источнике)
    voice "ch7.3_h_021"
    h "I know full well that thinking about it serves no purpose. And yet the regret… yes, the regret — even once I push it away, it comes floating back afterward.{#ch7.3_h_021}"
    # JA[425]: 考えても仕方がないことだとは分かっています。 / でも、後悔……そう、後悔が打ち消しても / 後から浮かんでくるのです。
    voice "ch7.3_h_022"
    h "What in childhood one never had to think of — that there are people to whom was never given what I accepted as naturally as the air I breathed…{#ch7.3_h_022}"
    # JA[426]: 幼い頃は考えずとも良かったこと、 / わたくしが空気のように受けとっていたものを / 与えられなかった者達がいること……。
    # [lay5 +396] — образ на месте (повторный вызов в источнике)
    voice "ch7.3_s_029"
    s "……{#ch7.3_s_029}"
    # JA[9181]: ……。
    # [lay8 +786 → h 2 — PROVISIONAL]
    $ show_sprites(("h 2", "s 1 sad"))
    voice "ch7.3_h_023"
    h "What is it… that I can do? Merely passing sentence changes nothing at all.{#ch7.3_h_023}"
    # JA[427]: わたくしは……何ができるのでしょう？ / ただ断罪するだけでは、何も変わらないのに。
    voice "ch7.3_h_024"
    h "And even when I ask myself what it is I could do, no answer comes back to me.{#ch7.3_h_024}"
    # JA[428]: では何ができるのかと自らに問うても、 / 答えは返ってこないのに。
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("h 2", "s 3 sad"))
    voice "ch7.3_s_030"
    s "Princess…{#ch7.3_s_030}"
    # JA[9182]: お姫さま……。
    # [lay8 +792 → h 2 sad — PROVISIONAL]
    $ show_sprites(("h 2 sad", "s 3 sad"))
    voice "ch7.3_h_025"
    h "The familiar…! {#ch7.3_h_025}"
    # JA[429]: 使い魔さん……っ！
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("h 2 sad", "s 1 sad"))
    voice "ch7.3_s_031"
    s "P-Princess. If anyone saw me like this, I dread to think what Louise would say…{#ch7.3_s_031}"
    # JA[9183]: お、お姫さま。 / こんなとこ見られたら、 / ルイズになんて言われるか……。
    voice "ch7.3_h_026"
    h "Please. Just now… just for this moment, let me stay like this. Just for now…{#ch7.3_h_026}"
    # JA[430]: お願いします。 / 今だけ……今だけ、こうさせていてください。 / 今だけ……。
    # [lay8 hide]
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1",))
    voice "ch7.3_s_032"
    s "…Yes.{#ch7.3_s_032}"
    # JA[9184]: ……はい。
    voice "ch7.3_h_027"
    h "……{#ch7.3_h_027}"
    # JA[431]: ……。
    voice "ch7.3_s_033"
    s "……{#ch7.3_s_033}"
    # JA[9185]: ……。
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("s 1 sad",))
    voice "ch7.3_s_034"
    s "Princess?{#ch7.3_s_034}"
    # JA[9186]: お姫さま？
    voice "ch7.3_h_028"
    h "Zzz… zzz…{#ch7.3_h_028}"
    # JA[432]: すう……すう……。
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1",))
    voice "ch7.3_s_035"
    s "So she finally fell asleep, did she. …If Louise spotted me here, I'd get knocked about black and blue again.{#ch7.3_s_035}"
    # JA[9187]: やっと眠れたのか。 / ……こんなとこ、ルイズに見られたら / またボコボコにされるな。
    voice "ch7.3_s_036"
    s "Good night, Princess…{#ch7.3_s_036}"
    # JA[9188]: おやすみなさい、お姫さま……。
    # [MSGOFF     msgoff()] — не портируется
    # [SE        se1      stop=1] — не портируется (система SE)
    # [BGM stop] — стоп музыки
    stop music fadeout 1.0
    # [lay8 hide]
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [WAIT       waitTime(1000, true)] — не портируется
    # [COFFEE     coffee()] — не реализована → пауза
    $ pause(1.0)
    # [移動] → next(405) — глава 9 (chapter_09) не портирована
    # PROVISIONAL-конец главы 7: сцена 405 появится в главе 8.
    jump attention
