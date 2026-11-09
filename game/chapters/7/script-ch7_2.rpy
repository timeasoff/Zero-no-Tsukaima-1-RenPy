# Глава 7, часть 2 (сцены 389-399): «失望のお姫さま» — бегство Уэзерби (бой с
# магами — система боя не реализована), встреча с Кирхе/Табитой/Анриеттой и Гишом
# с Монморанси (подвал с взрывчаткой), взрывы снаружи; CG-обнаружение бомбистки
# (terrorist/terrorist3) и снятие маски: Харуна = Акина, вторая личность,
# созданная Уэзерби; уловка с «пушками» Реконкисты; отряд противников.
# Источник: ps2_source/chapters/chapter_08_失望のお姫さま.txt (SCENE 389-399).
# Точные аргументы: ps2_source/events_full/chapter_08_失望のお姫さま.txt (541-1008).
#
# Вход — jump ch7_2 из веток сцены 385 (script-ch7_1.rpy); выход — jump ch7_3
#   (сцена 400, часть 3) — E7 «forward debt», закроется частью 3.
#
# Голоса: ch7.2_<spk>_<NNN> — нумерация с 001 по говорящему, порядок порта
#   (389 → 390 → ветки 391/392/393 → 394 → 395 → ветки 396/397/398 → 399):
#   s ×32 (13514-13545), l ×16 (7378-7393), w ×9 (16156-16158, 16160-16165),
#   h ×10 (835-844), g ×6 (1554-1559), k ×4 (3850-3853), ha ×5 (2634-2638),
#   m ×3 (4166-4168), ak ×6 (252-257), t ×1 (15809), unk_ak ×2 (250, 251 —
#   DR «？？？», сцена 395), unk_w ×1 (16159 — DR «？？？», сцена 399),
#   es ×1 (1409, 敵兵士ＥＳ) — всего 96. Реплика без голоса в источнике —
#   «……。» Акины (сцена 395, тег ch7.2_395a); мысль Сайто (сцена 395,
#   без голоса, тег ch7.2_th_395a); пункты меню — 6 (ch7.2_c391..c398).
#
# Спикеры: unk_ak и unk_w уже определены (game/characters.rpy); es (敵兵士ＥＳ)
#   зарегистрирован здесь (PROVISIONAL — цвет нейтральный #797979, DR «兵士»).
#
# Не портируются: SE (+63/+64/+65 — взрывы, и se1 stop), MSGON/MSGOFF, BACK,
#   WAIT (waitTime/waitAction/waitLoad), VIBRATE → shake_fx, battle* (система
#   боя не реализована), RESET/TRANS (переход через fade_fx), point x=/y=.
#
# Фоны/CG: bg 54, 52 — имена пусты в image_id_map.csv (заглушки id(K));
#   CG 97 = terrorist, 98 = terrorist3 (кроссфейд через dissolve_fx type="cg").
# Спрайты: 1017/1019 (Акина в lay21) и 1111 (серые солдаты lay14/lay22) не
#   отображены в справочнике — файла в медиа нет, не показываются (комментарии);
#   471 = s 8 angry PROV, 572 = g 2 sad PROV.
# Меню 【選択肢】: две развилки по три варианта (390 → 391/392/393 → 394;
#   395 → 396/397/398 → 399) — варианты сливаются внутрь общих сцен, как в
#   script-ch7_1.rpy (fall-through после меню).

label ch7_2:

    # ==== SCENE 389 ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay5 +440 → s 4 sad]
    $ show_sprites(("s 4 sad"))
    # [lay1 +339 → l 3 angry]
    $ show_sprites(("s 4 sad", "l 3 angry"))
    # [BGM play=+28 → t27] — музыка раньше фона (перезапуск после jump из части 1)
    play music t27 fadein 1.0
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [lay1 hide]
    # [lay5 hide]
    $ show_sprites()
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1"))
    voice "ch7.2_w_001"
    w "And that's when it happened. Someone appeared, promising to restore me to the rank I originally held.{#ch7.2_w_001}"
    # JA[16156]: そんな時よ。 / わたしに本来の身分を取り戻してやるって / 言ってくれる人が現れたの。
    # [lay20 y=0,x=-96]
    # [lay8 +779 → h 3 angry]
    $ show_sprites(("h 3 angry", "w 1"))
    voice "ch7.2_h_001"
    h "Which means… your mastermind intends to grant you the standing of a noble?{#ch7.2_h_001}"
    # JA[835]: それは……あなたの黒幕が、 / あなたに貴族の身分を与えるという意味ですか？
    voice "ch7.2_w_002"
    w "The standing that was originally mine in the first place. I would simply be taking it back. Besides, there is a promise to restore the village as well.{#ch7.2_w_002}"
    # JA[16157]: 本来、わたしが受けとっていた身分。 / それを取り戻すだけよ。 / それに、村も復興させるって約束だしね。
    # [BGM stop] — стоп музыки
    stop music fadeout 1.0
    # [WAIT       waitTime(1000, true)] — не портируется
    # [lay8 hide]
    # [lay20 hide]
    $ show_sprites()
    # [lay11 +1105 → mage]
    $ show_sprites(("mage"))
    # [lay12 +1105 → mage]
    $ show_sprites(("mage", "mage"))
    # [BGM play=+18 → t17] — музыка раньше фона
    play music t17 fadein 1.0
    voice "ch7.2_l_001"
    l "……! Since when did she have this many companions!?{#ch7.2_l_001}"
    # JA[7378]: ……！ / いつのまに、こんなに仲間が！？
    voice "ch7.2_s_001"
    s "Ugh — we've been surrounded.{#ch7.2_s_001}"
    # JA[13514]: くっ、囲まれたか。
    # [lay20 +1063 → w 1 happy (level 152)]
    $ show_sprites(("mage", "w 1 happy", "mage"))
    voice "ch7.2_w_003"
    w "It was a short acquaintance, but I enjoyed it. Now then, ladies and gentlemen — I bid you a good day.{#ch7.2_w_003}"
    # JA[16158]: 短い付き合いだったけど、楽しかったわ。 / それでは皆様、ごきげんよう。
    # [lay11 hide]
    # [lay12 hide]
    # [lay20 hide]
    # [lay1 +306 → l 1 angry (level 156)]
    $ show_sprites(("l 1 angry"))
    voice "ch7.2_l_002"
    l "Ah — stop right there!{#ch7.2_l_002}"
    # JA[7379]: あ、待ちなさいっ！
    # [lay1 y=0,x=-96]
    # [lay5 +405 → s 2 angry (level 157)]
    $ show_sprites(("l 1 angry", "s 2 angry"))
    voice "ch7.2_s_002"
    s "We have to hurry after her… is what I'd like to say, but first we have to deal with this lot.{#ch7.2_s_002}"
    # JA[13515]: 早く追いかけなきゃ……と言いたいが、 / その前にこいつらを片づけないとな。
    # [SE se0 play=+65] — SE не портируется
    # [lay1 hide]
    # [lay5 +471 → s 8 angry — PROVISIONAL]
    $ show_sprites(("s 8 angry"))
    voice "ch7.2_s_003"
    s "They're coming! Both of you, watch out!{#ch7.2_s_003}"
    # JA[13516]: 来るぞ！ / ２人とも気をつけろ！
    # [MSGOFF     msgoff()] — не портируется
    # [SET       set("se1", {stop = 1})] — SE не портируется
    # [BGM stop] — стоп музыки
    stop music fadeout 1.0
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [WAIT       waitTime(1000, true)] — не портируется
    # [BATTLE battleInit battleInit((0x02000000 +54))] — система боя не реализована, вызов не переносится
    # [BATTLE battleAdd  battleAdd("サイト")] — система боя не реализована, вызов не переносится
    # [BATTLE battleAdd  battleAdd("ルイズ")] — система боя не реализована, вызов не переносится
    # [BATTLE battleEnemy battleEnemy("左", "魔道士", (0x02000000 +1108))] — система боя не реализована, вызов не переносится
    # [BATTLE battleEnemy battleEnemy("右", "魔道士", (0x02000000 +1108))] — система боя не реализована, вызов не переносится
    # [BATTLE battle     battle()] — система боя не реализована, вызов не переносится

    # ==== SCENE 390 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BACK       back()] — не портируется
    # [BG +54 → id(54)]
    $ fade_fx("id(54)", new_music="t24")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1"))
    voice "ch7.2_l_003"
    l "Come on! We must hurry after Weatherby!{#ch7.2_l_003}"
    # JA[7380]: さあっ！ / 早くウェザリーを追うわよ。
    # [lay1 hide]
    # [lay6 +680 → k 1 angry]
    # [lay0 +588 → t 1]
    $ show_sprites(("k 1 angry", "t 1"))
    voice "ch7.2_k_001"
    k "So it was you after all, darling! We heard the sounds of the fighting, so we came running in a panic!{#ch7.2_k_001}"
    # JA[3850]: やっぱり、ダーリンだったのね！ / 戦闘の音が聞こえたから、 / 慌てて来てみたのよ！
    # [lay6 hide]
    # [lay0 hide]
    # [lay1 +304 → l 1 happy]
    $ show_sprites(("l 1 happy"))
    voice "ch7.2_l_004"
    l "Kirche! And Tabitha, too!{#ch7.2_l_004}"
    # JA[7381]: キュルケ！ / それに、タバサ！
    # [lay1 y=0,x=-96]
    # [lay8 +777 → h 3 happy]
    $ show_sprites(("l 1 happy", "h 3 happy"))
    voice "ch7.2_h_002"
    h "I see you both came through unharmed.{#ch7.2_h_002}"
    # JA[836]: ２人とも、無事でしたのね。
    # [lay1 hide]
    # [lay0 +588 → t 1]
    $ show_sprites(("t 1"))
    voice "ch7.2_t_001"
    t "I'm fine.{#ch7.2_t_001}"
    # JA[15809]: 大丈夫。
    # [lay8 hide]
    # [lay6 +682 → k 1 sad]
    $ show_sprites(("k 1 sad"))
    voice "ch7.2_k_002"
    k "I had a look around the back entrance, but there was nothing in particular there.{#ch7.2_k_002}"
    # JA[3851]: 裏口からひととおり見てきたけど、 / 特に何もなかったわ。
    # [lay6 hide]
    # [lay0 hide]
    # [lay4 +559 → g 1 angry]
    # [lay3 +856 → m 1 angry]
    $ show_sprites(("g 1 angry", "m 1 angry"))
    voice "ch7.2_g_001"
    g "There you all are! Something terrible has happened, you know.{#ch7.2_g_001}"
    # JA[1554]: みんな、ここにいたのか！ / 大変なことになったぞ。
    # [lay4 hide]
    # [lay3 hide]
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("s 2 angry"))
    voice "ch7.2_s_004"
    s "Guiche with Montmorency!? Just what happened?{#ch7.2_s_004}"
    # JA[13517]: ギーシュにモンモン！？ / いったいどうしたんだ。
    # [lay5 y=0,x=224]
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "s 2 angry"))
    voice "ch7.2_l_005"
    l "Did something happen?{#ch7.2_l_005}"
    # JA[7382]: 何かあったの？
    # [lay5 +407 → s 2 sad]
    $ show_sprites(("l 1", "s 2 sad"))
    voice "ch7.2_s_005"
    s "Don't tell me…{#ch7.2_s_005}"
    # JA[13518]: まさか……。

    # ---- 【選択肢】 ----
    menu:
        "Weatherby went that way?{#ch7.2_c391}":
            # JA: ウェザリーがそっちに？
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +407 → s 2 sad]
            $ show_sprites(("s 2 sad"))
            # [lay1 +302 → l 1]
            $ show_sprites(("s 2 sad", "l 1"))
            # [BGM play=+25 → t24] — музыка раньше фона
            play music t24 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay5 +405 → s 2 angry]
            $ show_sprites(("s 2 angry", "l 1"))
            voice "ch7.2_s_006"
            s "Don't tell me Weatherby went off that way!?{#ch7.2_s_006}"
            # JA[13519]: まさか、ウェザリーがそっちに行ったのか！？
            # [lay1 hide]
            # [lay4 +561 → g 1 sad]
            $ show_sprites(("s 2 angry", "g 1 sad"))
            voice "ch7.2_g_002"
            g "No, that's not it…!{#ch7.2_g_002}"
            # JA[1555]: いや、そうじゃなくて……！
            voice "ch7.2_s_007"
            s "Then what is it? Quit dangling it in front of us and just say it!{#ch7.2_s_007}"
            # JA[13520]: じゃあ、なんだってんだよ。 / もったいつけないで、さっさと言えよ！
            # [移動] → next(394)

        "Some kind of trap?{#ch7.2_c392}":
            # JA: 何かトラップでも？
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +407 → s 2 sad]
            $ show_sprites(("s 2 sad"))
            # [lay1 +302 → l 1]
            $ show_sprites(("s 2 sad", "l 1"))
            # [BGM play=+25 → t24] — музыка раньше фона
            play music t24 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay5 +405 → s 2 angry]
            $ show_sprites(("s 2 angry", "l 1"))
            voice "ch7.2_s_008"
            s "Was there some kind of trap?{#ch7.2_s_008}"
            # JA[13521]: 何か罠でもあったのか？
            # [lay1 hide]
            # [lay4 +572 → g 2 sad — PROVISIONAL]
            $ show_sprites(("s 2 angry", "g 2 sad"))
            voice "ch7.2_g_003"
            g "Close! Oh-so very close! But you're just a little off, you see.{#ch7.2_g_003}"
            # JA[1556]: 惜しい！ / 非常に惜しいね！ / でも、ちょっと違うんだなぁ。
            # [lay5 +407 → s 2 sad]
            $ show_sprites(("s 2 sad", "g 2 sad"))
            voice "ch7.2_s_009"
            s "You really do know how to make a person mad.{#ch7.2_s_009}"
            # JA[13522]: お前、ほんとむかつくな。
            # [lay4 hide]
            # [lay8 +779 → h 3 angry]
            $ show_sprites(("h 3 angry"))
            voice "ch7.2_h_003"
            h "Just what happened here?{#ch7.2_h_003}"
            # JA[837]: いったい、何があったのです？
            # [移動] → next(394)

        "Did you have another fight?{#ch7.2_c393}":
            # JA: またケンカでもしたのか
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +407 → s 2 sad]
            $ show_sprites(("s 2 sad"))
            # [lay1 +302 → l 1]
            $ show_sprites(("s 2 sad", "l 1"))
            # [BGM play=+25 → t24] — музыка раньше фона
            play music t24 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay5 +440 → s 4 sad]
            $ show_sprites(("s 4 sad", "l 1"))
            voice "ch7.2_s_010"
            s "Did you have another fight with Montmorency?{#ch7.2_s_010}"
            # JA[13523]: またモンモンとケンカでもしたのか？
            # [lay1 hide]
            # [lay4 +559 → g 1 angry]
            $ show_sprites(("s 4 sad", "g 1 angry"))
            voice "ch7.2_g_004"
            g "How could there be!{#ch7.2_g_004}"
            # JA[1557]: そんなわけあるか！
            # [lay4 hide]
            # [lay8 +779 → h 3 angry]
            $ show_sprites(("h 3 angry"))
            voice "ch7.2_h_004"
            h "Just what happened, then?{#ch7.2_h_004}"
            # JA[838]: いったい何があったというのですか。
            # [移動] → next(394)


    # ==== SCENE 394 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay4 +561 → g 1 sad]
    $ show_sprites(("g 1 sad"))
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("g 1 sad", "s 2 angry"))
    # [BGM play=+25 → t24] — музыка раньше фона
    play music t24 fadein 1.0
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [lay5 hide]
    # [lay4 hide]
    $ show_sprites()
    # [lay8 y=416,x=464]
    # [lay3 +856 → m 1 angry]
    $ show_sprites(("m 1 angry"))
    voice "ch7.2_m_001"
    m "We went around to the underground through the prop loading entrance — and that cellar was packed full of hidden explosives!{#ch7.2_m_001}"
    # JA[4166]: 私達は大道具の搬入口から、 / 地下に回ったんだけど、その地下室いっぱいに / 爆薬が隠されていたのよ！
    # [lay3 y=0,x=-96]
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("m 1 angry", "s 2 angry"))
    voice "ch7.2_s_011"
    s "What did you just say!?{#ch7.2_s_011}"
    # JA[13524]: 何だって！？
    # [lay3 hide]
    # [lay6 +682 → k 1 sad]
    $ show_sprites(("k 1 sad", "s 2 angry"))
    voice "ch7.2_k_003"
    k "Well, it stands to reason a bomb user in hiding would have explosives, after all. I'd simply let it entirely slip my mind.{#ch7.2_k_003}"
    # JA[3852]: たしかに、爆弾使いが潜伏してるんだから、 / 爆薬だってあって当然なのよね。 / すっかり失念していたわ。
    # [lay5 hide]
    # [lay6 hide]
    # [lay4 +559 → g 1 angry]
    # [lay3 +858 → m 1 sad]
    $ show_sprites(("g 1 angry", "m 1 sad"))
    voice "ch7.2_g_005"
    g "We couldn't just leave it be, and not telling you would have been bad too — so that's why we've come to fetch you.{#ch7.2_g_005}"
    # JA[1558]: このまま放置するわけにもいかないし、 / 知らせないのもまずいだろうしというわけで、 / 呼びに来たんだよ。
    # [lay3 +891 → m 4 sad]
    $ show_sprites(("g 1 angry", "m 4 sad"))
    voice "ch7.2_m_002"
    m "With my 'Water' magic I dampened the gunpowder to make it temporarily unusable, but there's far too much of it for the two of us to manage…{#ch7.2_m_002}"
    # JA[4167]: 『水』の魔法で、火薬を湿らせて、 / 一時的に使えなくしておいたけど、 / 量が多すぎて、私達だけじゃどうにも…。
    # [lay4 hide]
    # [lay3 hide]
    # [lay8 +775 → h 3]
    $ show_sprites(("h 3"))
    voice "ch7.2_h_005"
    h "That is the right call. For now, let us give priority to dealing with the explosives they left behind.{#ch7.2_h_005}"
    # JA[839]: それで正解です。 / 今は、まず彼女達が残していった / 爆薬の処理を優先しましょう。
    # [lay8 y=0,x=224]
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "h 3"))
    voice "ch7.2_l_006"
    l "Is it all right to leave off chasing Weatherby?{#ch7.2_l_006}"
    # JA[7383]: ウェザリーの追跡はいいんですか？
    # [lay8 +779 → h 3 angry]
    $ show_sprites(("l 1", "h 3 angry"))
    voice "ch7.2_h_006"
    h "Of course the pursuit is important, but if the explosives are left as they are and something is done with them, it would be a catastrophe.{#ch7.2_h_006}"
    # JA[840]: もちろん追跡は重要ですが、 / このまま爆薬を放置しておいて、 / 使われてしまっては一大事です。
    # [lay8 hide]
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("l 1", "s 2 angry"))
    voice "ch7.2_s_012"
    s "Understood.{#ch7.2_s_012}"
    # JA[13525]: 分かりました。
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "s 2 angry"))
    voice "ch7.2_l_007"
    l "Still — why would Weatherby tell us everything, I wonder?{#ch7.2_l_007}"
    # JA[7384]: それにしても、なんでウェザリーは、 / 私達にすべてを話したのかしら？
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "s 2 angry"))
    voice "ch7.2_l_008"
    l "She confessed so readily that I nearly took it for a surrender.{#ch7.2_l_008}"
    # JA[7385]: あんまりあっさり自白するものだから、 / 投降するのかと思ったくらい。
    # [lay5 hide]
    # [lay8 +781 → h 3 sad]
    $ show_sprites(("l 1", "h 3 sad"))
    voice "ch7.2_h_007"
    h "I expect that at least as far as the likes of us were concerned, there was no longer any point in concealing her identity and her motives.{#ch7.2_h_007}"
    # JA[841]: おそらく、正体とその動機を、少なくとも / わたくし達には隠しておく意味が / なくなったのでしょうね。
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "h 3 sad"))
    voice "ch7.2_l_009"
    l "Hm? What do you mean by…{#ch7.2_l_009}"
    # JA[7386]: え？ / それって、どういう……。
    # [SE se0 play=+64] — SE не портируется
    # [VIBRATE vibrate(2)] — тряска (SE +64)
    $ shake_fx(duration=0.8)
    # [BG/EVENT_CG/sprites reset — сброс вибрации]
    $ show_sprites(("l 1 sad", "h 3 sad"))
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "h 3 sad"))
    voice "ch7.2_l_010"
    l "Eek!{#ch7.2_l_010}"
    # JA[7387]: きゃあっ！
    # [lay8 hide]
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("l 1 angry", "s 2 angry"))
    voice "ch7.2_s_013"
    s "What was that!? Where did it explode!?{#ch7.2_s_013}"
    # JA[13526]: なんだ！？ / どこで爆発した！？
    # [lay5 hide]
    # [lay4 +559 → g 1 angry]
    $ show_sprites(("l 1 angry", "g 1 angry"))
    voice "ch7.2_g_006"
    g "Outside!{#ch7.2_g_006}"
    # JA[1559]: 外だ！
    # [lay1 +339 → l 3 angry]
    $ show_sprites(("l 3 angry", "g 1 angry"))
    voice "ch7.2_l_011"
    l "Let's go and see!{#ch7.2_l_011}"
    # JA[7388]: 行ってみましょう！
    # [MSGOFF     msgoff()] — не портируется
    # [SET       set("se1", {stop = 1})] — SE не портируется
    # [BGM stop] — стоп музыки
    stop music fadeout 1.0
    # [lay4 hide]
    # [lay1 hide]
    # [BG hide]
    $ fade_fx("black")
    # [WAIT       waitTime(1000, true)] — не портируется
    # [移動] → next(395)

    # ==== SCENE 395 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BACK       back()] — не портируется
    # [BG +52 → id(52)]
    $ fade_fx("id(52)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [SE se0 play=+63] — SE не портируется
    # [VIBRATE vibrate(2)] — тряска (SE +63)
    $ shake_fx(duration=0.8)
    # [BGM play=+27 → t26] — музыка входит после фона и тряски
    play music t26 fadein 1.0
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("s 2 angry"))
    voice "ch7.2_s_014"
    s "Damn it, don't tell me the explosions weren't just in one place!{#ch7.2_s_014}"
    # JA[13527]: くそっ、爆発は１ヶ所じゃないのか！
    # [lay5 y=0,x=224]
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "s 2 angry"))
    voice "ch7.2_l_012"
    l "And the bomb user? Has she already fled?{#ch7.2_l_012}"
    # JA[7389]: 爆弾使いは？ / もう、逃げちゃったの？
    voice "ch7.2_s_015"
    s "No… there's someone over there!{#ch7.2_s_015}"
    # JA[13528]: いや……。 / そこに誰かいる！
    # [MSGOFF     msgoff()] — не портируется
    # [lay1 hide]
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [WAIT       waitAction(null, true)] — не портируется
    # [MSGOFF     msgoff()] — не портируется
    # [BACK       back()] — не портируется
    # [EVENT_CG +97 → terrorist (level 80)]
    $ dissolve_fx("terrorist", type="cg")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется dissolve_fx
    # [MSGON      msgon()] — не портируется
    # [lay21] Акины во время CG не показывается — спрайта в медиа нет
    # реплика без голоса в источнике (no-voice line) — тег PROVISIONAL
    unk_ak "……{#ch7.2_395a}"
    # JA: ……。
    voice "ch7.2_s_016"
    s "You're the bomb user… aren't you.{#ch7.2_s_016}"
    # JA[13529]: お前、爆弾使いだな……。
    voice "ch7.2_unk_ak_001"
    unk_ak "Quite right…{#ch7.2_unk_ak_001}"
    # JA[250]: ご名答……。
    th "…! That voice… could it be?{#ch7.2_th_395a}"
    # JA: （……！ / 　この声……まさか？）
    # [EVENT_CG +98 → terrorist3 (кроссфейд 1000)]
    $ dissolve_fx("terrorist3", type="cg")
    voice "ch7.2_unk_ak_002"
    unk_ak "Long time no see!{#ch7.2_unk_ak_002}"
    # JA[251]: 久しぶりだな！
    voice "ch7.2_l_013"
    l "Wha…?{#ch7.2_l_013}"
    # JA[7390]: え……？
    voice "ch7.2_k_004"
    k "Haruna…? What are you doing in a place like this?{#ch7.2_k_004}"
    # JA[3853]: ハルナ……？ / なんでこんなところにいるの？
    voice "ch7.2_s_017"
    s "And those last words from you… what on earth are you saying!?{#ch7.2_s_017}"
    # JA[13530]: それに、今の台詞……。 / いったい、なにを言ってるんだ！？
    # [MSGOFF     msgoff()] — не портируется
    # [lay21/lay1/lay5/lay6 hide] — спрайты не показывались
    # [BG hide]
    $ fade_fx("black")
    # [EVENT_CG hide] — гаснет (без перехода)
    # [WAIT       waitAction(null, true)] — не портируется
    # [BACK       back()] — не портируется
    # [BG +52 → id(52)]
    $ fade_fx("id(52)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay21 +1017] — спрайт Акины: файла в медиа нет, не показывается
    # [MSGON      msgon()] — не портируется
    voice "ch7.2_ha_001"
    ha "What for? Just what you heard me say. The bomb user you've all been looking for — that was me all along.{#ch7.2_ha_001}"
    # JA[2634]: 何って、いまお前が聞いたとおりさ。 / おまえ達がずっと探してた爆弾使いってのは、 / あたしのことだったんだよ。
    # [lay21 y=0,x=-96]
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("s 2 angry"))
    voice "ch7.2_s_018"
    s "Haruna is?{#ch7.2_s_018}"
    # JA[13531]: 春奈が？

    # ---- 【選択肢】 ----
    menu:
        "Are you really Haruna?{#ch7.2_c396}":
            # JA: お前、本当に春奈なのか？
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay21 +1017] — спрайт Акины: файла в медиа нет, не показывается
            # [lay5 +405 → s 2 angry]
            $ show_sprites(("s 2 angry"))
            # [BGM play=+27 → t26] — музыка раньше фона
            play music t26 fadein 1.0
            # [BG +52 → id(52)]
            $ fade_fx("id(52)")
            # [lay5 +407 → s 2 sad]
            $ show_sprites(("s 2 sad"))
            voice "ch7.2_s_019"
            s "You — are you really Haruna?{#ch7.2_s_019}"
            # JA[13532]: お前、本当に春奈なのか？
            # [lay21 +1019] — спрайт Акины: файла в медиа нет, не показывается
            voice "ch7.2_ha_002"
            ha "Who can say, hmm?{#ch7.2_ha_002}"
            # JA[2635]: さあ、どうだろうねぇ？
            voice "ch7.2_s_020"
            s "However I look at it, you aren't the Haruna we know.{#ch7.2_s_020}"
            # JA[13533]: どう考えても、お前は俺達が知ってる / 春奈じゃない。
            # [lay5 +405 → s 2 angry]
            $ show_sprites(("s 2 angry"))
            voice "ch7.2_s_021"
            s "I'll ask once more. Who are you?{#ch7.2_s_021}"
            # JA[13534]: もう一度聞く。 / お前は誰だ？
            # [移動] → next(399)

        "Why are you on their side?{#ch7.2_c397}":
            # JA: なんであいつらの味方をするんだ？
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay21 +1017] — спрайт Акины: файла в медиа нет, не показывается
            # [lay5 +405 → s 2 angry]
            $ show_sprites(("s 2 angry"))
            # [BGM play=+27 → t26] — музыка раньше фона
            play music t26 fadein 1.0
            # [BG +52 → id(52)]
            $ fade_fx("id(52)")
            voice "ch7.2_s_022"
            s "Why would you ever take those people's side?{#ch7.2_s_022}"
            # JA[13535]: なんであいつらの味方をするんだ？
            # [lay21 +1019] — спрайт Акины: файла в медиа нет, не показывается
            voice "ch7.2_ha_003"
            ha "Well, my mistress is Lady Weatherby, you see. There isn't any 'side' to take in the first place.{#ch7.2_ha_003}"
            # JA[2636]: そりゃ、あたしの飼い主は / ウェザリー様だからねぇ。 / 味方も、何もないんじゃない？
            voice "ch7.2_s_023"
            s "You're not Haruna. Just who are you?{#ch7.2_s_023}"
            # JA[13536]: 春奈じゃない。 / いったい、誰なんだ？
            # [移動] → next(399)

        "Someone's transformed into her!{#ch7.2_c398}":
            # JA: 誰かが変身してるんだ！
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay21 +1017] — спрайт Акины: файла в медиа нет, не показывается
            # [lay5 +405 → s 2 angry]
            $ show_sprites(("s 2 angry"))
            # [BGM play=+27 → t26] — музыка раньше фона
            play music t26 fadein 1.0
            # [BG +52 → id(52)]
            $ fade_fx("id(52)")
            # [lay5 +407 → s 2 sad]
            $ show_sprites(("s 2 sad"))
            voice "ch7.2_s_024"
            s "Is someone disguised as Haruna, hoping to confuse us?{#ch7.2_s_024}"
            # JA[13537]: 俺達を混乱させようとして、 / 誰かが春奈の変装をしてるのか？
            # [lay21 +1019] — спрайт Акины: файла в медиа нет, не показывается
            voice "ch7.2_ha_004"
            ha "Too bad, isn't it. This body of mine is genuine Haruna, through and through.{#ch7.2_ha_004}"
            # JA[2637]: 残念だねぇ。 / あたしのこの体は正真正銘、ハルナのものさ。
            # [lay5 +405 → s 2 angry]
            $ show_sprites(("s 2 angry"))
            voice "ch7.2_s_025"
            s "That's… a lie! Who are you!?{#ch7.2_s_025}"
            # JA[13538]: そんなの……うそだ！ / お前、誰だ！
            # [移動] → next(399)


    # ==== SCENE 399 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay21 +1019] — спрайт Акины: файла в медиа нет, не показывается
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("s 2 angry"))
    # [BGM play=+27 → t26] — музыка раньше фона
    play music t26 fadein 1.0
    # [BG +52 → id(52)]
    $ fade_fx("id(52)")
    # [lay21 +1017] — спрайт Акины: файла в медиа нет, не показывается
    voice "ch7.2_ha_005"
    ha "Then let me introduce myself all over again. I am Haruna, and yet I am not Haruna. My name is 'Akina'.{#ch7.2_ha_005}"
    # JA[2638]: 改めて名乗ってやるよ。 / あたしは、ハルナであってハルナじゃない。 / あたしの名前は『アキナ』って言うのさ。
    # [lay5 +407 → s 2 sad]
    $ show_sprites(("s 2 sad"))
    voice "ch7.2_s_026"
    s "Akina…?{#ch7.2_s_026}"
    # JA[13539]: アキナ……？
    voice "ch7.2_ak_001"
    ak "That's right. This is Haruna's body, but I am an entirely different person. Think of me as her other personality.{#ch7.2_ak_001}"
    # JA[252]: そう。 / ハルナと同じ体だけど、まったくの別人。 / もうひとつの人格ってところさ。
    voice "ch7.2_s_027"
    s "Her other personality?{#ch7.2_s_027}"
    # JA[13540]: もうひとつの人格？
    # [lay21 +1019] — спрайт Акины: файла в медиа нет, не показывается
    voice "ch7.2_ak_002"
    ak "Well then, why don't I show you the trick behind it?{#ch7.2_ak_002}"
    # JA[253]: 種明かししてあげようじゃないか。
    # [lay21 +1017] — спрайт Акины: файла в медиа нет, не показывается
    voice "ch7.2_ak_003"
    ak "Haruna came to this Halkeginia long, long before you ever rescued her. And there, Lady Weatherby gave her shelter.{#ch7.2_ak_003}"
    # JA[254]: ハルナは、あんたに助けられるずっと前に、 / このハルケギニアにやってきてたんだ。 / そして、そこでウェザリー様に保護された。
    # [lay21 +1019] — спрайт Акины: файла в медиа нет, не показывается
    voice "ch7.2_ak_004"
    ak "Lady Weatherby judged me of use — and brought me into being.{#ch7.2_ak_004}"
    # JA[255]: これは使えるって思ったウェザリー様が / あたしを生み出したのさ。
    # [lay21 +1017] — спрайт Акины: файла в медиа нет, не показывается
    voice "ch7.2_ak_005"
    ak "To gather information on you, Saito — the legendary familiar said to have appeared in Tristain — and on your master Louise.{#ch7.2_ak_005}"
    # JA[256]: トリステインに現れたっていう / 伝説の使い魔サイトと、 / その主人であるルイズの情報を集めるためにね。
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("s 2 angry"))
    voice "ch7.2_s_028"
    s "Wha—!? Their sights set on me and Louise…!?{#ch7.2_s_028}"
    # JA[13541]: なっ！？ / 俺とルイズを狙って……！？
    voice "ch7.2_unk_w_001"
    unk_w "Ahaha! Looks like you had quite the fright!{#ch7.2_unk_w_001}"
    # JA[16159]: あははっ！ / 驚いてもらえたようだね！
    # [lay21 hide]
    # [lay5 hide]
    $ show_sprites()
    # [lay14 +1111] — спрайт серого солдата: файла в медиа нет, не показывается
    # [lay22 +1111] — спрайт серого солдата: файла в медиа нет, не показывается
    # [lay20 +1061 → w 1 (level 147)]
    $ show_sprites(("w 1"))
    voice "ch7.2_s_029"
    s "Weatherby!?{#ch7.2_s_029}"
    # JA[13542]: ウェザリー！？
    # [lay14 hide]
    # [lay22 hide]
    # [lay20 hide]
    # [lay8 +779 → h 3 angry (level 153)]
    $ show_sprites(("h 3 angry"))
    voice "ch7.2_h_008"
    h "The ones standing behind you are Reconquista, are they not.{#ch7.2_h_008}"
    # JA[842]: あなたがたの背後にいるのは / レコン・キスタですね。
    # [lay8 hide]
    # [lay8 +779 → h 3 angry]
    # [lay1 +302 → l 1 (level 156)]
    $ show_sprites(("l 1", "h 3 angry"))
    voice "ch7.2_l_014"
    l "Reconquista!?{#ch7.2_l_014}"
    # JA[7391]: レコン・キスタ！？
    # [lay1 hide]
    # [lay20 +1061 → w 1 (level 147)]
    $ show_sprites(("w 1"))
    voice "ch7.2_w_004"
    w "Well, well, Your Highness. So it finally got through to you? But it is already too late.{#ch7.2_w_004}"
    # JA[16160]: おやおや、お姫様。 / やっと分かったのかい？ / でも、もう遅いわ。
    # [lay20 +1063 → w 1 happy]
    $ show_sprites(("w 1 happy"))
    voice "ch7.2_w_005"
    w "Seen in the morning light it would be perfectly plain, but I'll tell you while it's still dark: I have installed cannon batteries at the sites in every district.{#ch7.2_w_005}"
    # JA[16161]: 朝になって眺めれば一目瞭然だけど、 / 今のうちに教えてあげる。 / 各地区の現場に、砲台を設置したのよ。
    # [lay8 +779 → h 3 angry]
    $ show_sprites(("w 1 happy", "h 3 angry"))
    voice "ch7.2_h_009"
    h "What did you say!?{#ch7.2_h_009}"
    # JA[843]: なんですって！？
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1", "h 3 angry"))
    voice "ch7.2_w_006"
    w "I will destroy every last seat of tainted power there is.{#ch7.2_w_006}"
    # JA[16162]: わたしが穢れた権力すべてを破壊してみせる。
    # [lay8 hide]
    # [lay5 +405 → s 2 angry (level 157)]
    $ show_sprites(("w 1", "s 2 angry"))
    voice "ch7.2_s_030"
    s "Like hell I'll let you do that!{#ch7.2_s_030}"
    # JA[13543]: そんなこと、させるかよ！
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("w 1 angry", "s 2 angry"))
    voice "ch7.2_w_007"
    w "You will not stop me. I survived to this very day for that very purpose.{#ch7.2_w_007}"
    # JA[16163]: 止めさせないわ。 / わたしは、そのために今日まで / 生き抜いたんだから。
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1", "s 2 angry"))
    voice "ch7.2_w_008"
    w "Come along, Akina — we're off.{#ch7.2_w_008}"
    # JA[16164]: さあ、行くわよアキナ。
    # [lay5 hide]
    # [lay21 +1017] — спрайт Акины: файла в медиа нет, не показывается (level 151)
    $ show_sprites(("w 1"))
    voice "ch7.2_ak_006"
    ak "Yes, Lady Weatherby.{#ch7.2_ak_006}"
    # JA[257]: はい、ウェザリー様。
    # [lay20 hide]
    # [lay21 hide]
    # [lay1 +306 → l 1 angry (level 156)]
    $ show_sprites(("l 1 angry"))
    voice "ch7.2_l_015"
    l "Stop right there!{#ch7.2_l_015}"
    # JA[7392]: 待ちなさい！
    # [lay1 y=0,x=-96]
    # [lay5 +405 → s 2 angry (level 157)]
    $ show_sprites(("l 1 angry", "s 2 angry"))
    voice "ch7.2_s_031"
    s "Damn it! We have to run them down and stop them!{#ch7.2_s_031}"
    # JA[13544]: くそっ！ / 追いかけて止めなきゃ！
    # [lay1 hide]
    # [lay5 hide]
    $ show_sprites()
    # [lay14 +1111] — спрайт серого солдата: файла в медиа нет, не показывается (level 149)
    # [lay22 +1111] — спрайт серого солдата: файла в медиа нет, не показывается (level 148)
    voice "ch7.2_w_009"
    w "Oh my, I had almost forgotten. I've had a great many extras on standby. Do enjoy yourselves thoroughly.{#ch7.2_w_009}"
    # JA[16165]: あら、忘れてた。 / エキストラは多数用意しておいたわよ。 / しっかり、楽しんでね。
    # [lay14 hide]
    # [lay22 hide]
    # [lay3 +891 → m 4 sad (level 152)]
    $ show_sprites(("m 4 sad"))
    voice "ch7.2_m_003"
    m "Eek!? Who are these people!?{#ch7.2_m_003}"
    # JA[4168]: きゃっ！？ / なに、この連中は！？
    # [lay3 hide]
    # [lay14 +1111] — спрайт серого солдата: файла в медиа нет, не показывается (level 149)
    # [lay22 +1111] — спрайт серого солдата: файла в медиа нет, не показывается (level 148)
    $ show_sprites()
    voice "ch7.2_es_001"
    es "You shall not pass from here. You will die right where you stand.{#ch7.2_es_001}"
    # JA[1409]: 貴様らを進ませるわけにはいかん。 / ここで死んでもらおう。
    # [lay14 hide]
    # [lay22 hide]
    # [lay5 +405 → s 2 angry (level 157)]
    $ show_sprites(("s 2 angry"))
    voice "ch7.2_s_032"
    s "Ugh! So first we have to beat down this lot before anything else can be done, is that it!{#ch7.2_s_032}"
    # JA[13545]: くっ！ / まずはこいつらを倒さなきゃ、 / どうしようもないってことか！
    # [lay5 y=0,x=224]
    # [lay8 +779 → h 3 angry (level 153)]
    $ show_sprites(("h 3 angry", "s 2 angry"))
    voice "ch7.2_h_010"
    h "We must make haste… we have to stop them before the capital is turned into a sea of flames!{#ch7.2_h_010}"
    # JA[844]: 急がないと……。 / 都が火の海になる前に、止めなくては！
    # [lay8 hide]
    # [lay1 +339 → l 3 angry (level 156)]
    $ show_sprites(("l 3 angry", "s 2 angry"))
    voice "ch7.2_l_016"
    l "We'll sweep them aside in short order. All right?{#ch7.2_l_016}"
    # JA[7393]: さっさと蹴散らすわよ、いいわね！
    # [MSGOFF     msgoff()] — не портируется
    # [SET       set("se1", {stop = 1})] — SE не портируется
    # [BGM stop] — стоп музыки
    stop music fadeout 1.0
    # [lay20 hide]
    # [lay7 hide]
    # [lay5 hide]
    # [lay1 hide]
    # [BG hide]
    $ fade_fx("black")
    # [WAIT       waitTime(1000, true)] — не портируется
    # [BATTLE battleInit battleInit((0x02000000 +52))] — система боя не реализована, вызов не переносится
    # [BATTLE battleAdd  battleAdd("サイト")] — система боя не реализована, вызов не переносится
    # [BATTLE battleAdd  battleAdd("ルイズ")] — система боя не реализована, вызов не переносится
    # [BATTLE battleEnemy battleEnemy("左", "兵士", (0x02000000 +1111))] — система боя не реализована, вызов не переносится
    # [BATTLE battleEnemy battleEnemy("右", "兵士", (0x02000000 +1111))] — система боя не реализована, вызов не переносится
    # [BATTLE battle     battle()] — система боя не реализована, вызов не переносится
    # [移動] → next(400)

    # конец части 2: сцена 400 — в script-ch7_3.rpy (часть 3)
    jump ch7_3
