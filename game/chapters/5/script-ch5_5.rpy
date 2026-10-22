# Глава 5, часть 5 (сцены 320–334): инцидент с пэдами Харуны, репетиции
# и рассказ Уэзерби о пьесе, объявление ролей, распускание и загадка Кирхе.
# Источник: ps2_source/chapters/chapter_06_本当の想い.txt (SCENE 320–334).
# Точные аргументы: ps2_source/events_full/chapter_06_本当の想い.txt.
# Скелет собран генератором tools/gen_ch5_5_script.py (EN — tools/ch5_5_en.py,
#   RU — tools/ch5_5_ru.py), поэтому порядок реплик, голоса, спрайты и
#   события совпадают с источником дословно.
#
# Вход — jump ch5_5 из script-ch5_4.rpy; выход — jump ch5_6 (сцена 335) —
#   E7 «forward debt», закроется частью 6.
#
# Голоса: ch5.5_<spk>_<NNN> — новая группа части 5, нумерация с 001 по
#   говорящему, порядок порта (320 → 321 → 322–324 → 325 → 326–328 → 329 →
#   330 → 331–333 → 334). Всего 126: l=26, ha=14, s=25, d=1, w=31, si=3,
#   k=20, m=2, g=1, t=3.
# Голос-мысль ch5.5_t_001 （くいくい） (сцена 330) выводится как th —
#   реплика в （…）, references/ps2_to_renpy.csv п. 2.
#
# Не портируются: item() (инвентарь не реализован), TNDL, SE (в т.ч. se0
#   +57/+82 в сцене 320), waitAction/waitTime/waitSEStop/waitLoad,
#   msgon/msgoff, back(), beginSkip, MOVE/MOVEINIT (карта переходов PS2).
#
# Фоны/CG: bg 89 = sky_evening, bg 88 = sky; id(53), id(54), id(271) —
#   имена пусты в image_id_map.csv (заглушки id(K)).
#
# Спрайт 502 (si 2 happy) — PROVISIONAL (пиксель-сверка SCENEDAT невозможна,
#   архив PS2 не смонтирован); строка добавлена в sprite_id_map.csv.


label ch5_5:
    # Часть 5: инцидент с пэдами Харуны (320) → репетиции и рассказ Уэзерби
    # о пьесе (321, ветки 322–324) → объявление ролей (325, ветки
    # 326–328) → распускание и загадка Кирхе (329–330, ветки
    # 331–333) → благодарность (334).

    # ==== SCENE 320 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +89 → sky_evening]
    $ fade_fx("sky_evening", new_music="t18")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    voice "ch5.5_l_001"
    l "Hah… practice again today. Practice again tomorrow… Even so, something still feels unresolved."
    # JA[6231]: はぁ、今日も練習。 / 明日も練習……。 / それにしても、なにか釈然としないわね。
    # [SET        set("se0", {play = (0x03000000 +82)})] — SE не портируется
    # [SET        set("se0", {play = (0x03000000 +57)})] — SE не портируется
    stop music fadeout 1.0
    # [LAYER white +2] → flash_fx("white")
    $ flash_fx("white")
    # [EVENT_CG +271 → id(271)]
    $ fade_fx("id(271)", type="cg", new_music="t29")
    # [TRANS   trans("crossfade", 0)] — переход выполняется fade_fx
    # [LAYER white hide] — вспышка гаснет (fade)
    voice "ch5.5_l_002"
    l "…Oh? Haruna, you were here?"
    # JA[6232]: ……あ、あれ？ / ハルナ、いたんだ？
    voice "ch5.5_ha_001"
    ha "A-Ah!"
    # JA[2363]: き、きゃあっ！
    voice "ch5.5_l_003"
    l "W-What! It's me! Me!"
    # JA[6233]: な、なによ！ / わたしよ！ / わたし！
    voice "ch5.5_l_004"
    l "…Hold on! Eh? Why don't you have a chest?"
    # JA[6234]: ……って！ / え？ / なんで、ムネがないの？
    voice "ch5.5_ha_002"
    ha "N-no! Don't look!"
    # JA[2364]: い、いやっ！ / み、見ないでください！
    voice "ch5.5_l_005"
    l "…Wh-what is that! Haruna, was your chest padded?"
    # JA[6235]: ……な、なによそれ！ / ハルナのムネは上げ底だったの？
    voice "ch5.5_ha_003"
    ha "S-sorry!{#ch5_5_v2365}"
    # JA[2365]: ご、ごめんなさぁい！
    voice "ch5.5_l_006"
    l "Sorry doesn't cut it!"
    # JA[6236]: ごめんなさいじゃないわよ！
    voice "ch5.5_l_007"
    l "B-because of that stuffing, do you know how much my small chest ached — or rather, how self-conscious I felt!"
    # JA[6237]: そ、その詰め物のせいで、 / どれだけわたしが小さな胸を痛めて……、 / もとい肩身の狭い思いをしたと思ってるのよ！
    voice "ch5.5_ha_004"
    ha "Please! Keep it a secret from everyone!"
    # JA[2366]: お願い！ / みんなには黙っていて！
    voice "ch5.5_l_008"
    l "…….{#ch5_5_v6238}"
    # JA[6238]: ……。
    voice "ch5.5_ha_005"
    ha "…….{#ch5_5_v2367}"
    # JA[2367]: ……。
    voice "ch5.5_l_009"
    l "…Honestly, what am I to do with you. All right, I get it. I'll keep your secret."
    # JA[6239]: ……まったく、仕方ないわね。 / 分かったわよ。 / 黙っててあげる。
    voice "ch5.5_ha_006"
    ha "…Th-thank you…"
    # JA[2368]: ……あ、ありがとう……。
    voice "ch5.5_ha_007"
    ha "…Once, for the sake of appearances… one pad, then another — before I knew it there was no going back… and finally…"
    # JA[2369]: ……昔、見栄をはって……パッドを一枚、 / また一枚と入れていくうちに後戻り / できなくなって……とうとう……。
    voice "ch5.5_l_010"
    l "…O-oh. So this is what a pad is?"
    # JA[6240]: ……ふ、ふぅん。 / パッドってこれのこと？
    voice "ch5.5_ha_008"
    ha "…Y-yes. You put them on like this… I suppose you'd call it padding…"
    # JA[2370]: ……う、うん。 / こうやってつける……、上げ底というか……。
    voice "ch5.5_ha_009"
    ha "…It's a girl's secret tool, found in our world."
    # JA[2371]: ……私達の世界にある、女の子の秘密道具なの。
    voice "ch5.5_l_011"
    l "…H-hm. Odd shape."
    # JA[6241]: ……ふ、ふ～ん。 / 変な形ね。
    voice "ch5.5_l_012"
    l "…….{#ch5_5_v6242}"
    # JA[6242]: ……。
    voice "ch5.5_l_013"
    l "…B-but. It's wonderful."
    # JA[6243]: ……で、でも。 / すばらしいわ。
    voice "ch5.5_l_014"
    l "It's just now, for the first time, I felt interest and respect for the world Saito was in."
    # JA[6244]: いま初めて、サイトがいた世界に興味と / 尊敬を感じたわ。
    voice "ch5.5_ha_010"
    ha "I thought I didn't need them anymore, but Hiraga-kun seems to like girls with big chests, so…"
    # JA[2372]: 最近はつける必要ないと思ってたんだけど、 / 平賀くん、胸の大きい女の子が / 好きみたいだし……。
    voice "ch5.5_l_015"
    l "Right. He pretends not to be interested, but it's obvious."
    # JA[6245]: そうよね。 / 本人は興味なさそうなふりをしてる / みたいだけど、バレバレよ。
    voice "ch5.5_ha_011"
    ha "Louise-san, I'm sorry."
    # JA[2373]: ルイズさん、ごめんなさい。
    voice "ch5.5_l_016"
    l "No, it's all right, Haruna. It's all that stupid dog's fault. He doesn't understand girls' feelings."
    # JA[6246]: いえ、いいのよハルナ。 / すべてはあのバカ犬が悪いのよ。 / 女の子の気持ち、分かってくれないんだから。
    voice "ch5.5_ha_012"
    ha "That's right.{#ch5_5_v2374}"
    # JA[2374]: そうですね。
    voice "ch5.5_l_017"
    l "…Pfft, heh heh heh."
    # JA[6247]: ……プッ、くすくすくす。
    voice "ch5.5_ha_013"
    ha "Ah ha, ah ha ha ha…"
    # JA[2375]: あは、あはははは……。
    # [lay1 hide]
    # [lay7 hide]
    # [BG hide]
    $ fade_fx("black")
    # [EVENT_CG hide] — поглощается переходом на фон
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("s 3 sad"))
    # [lay19 +940 → d 1]
    $ show_sprites(("d 1", "s 3 sad"))
    voice "ch5.5_s_001"
    s "They sure seem to be enjoying themselves, huh? …What were those two talking about?"
    # JA[11676]: なんか、楽しそうに笑ってるぞ？ / ……あの２人……何を話してたんだ？
    # [lay19 +946 → d 1 sad]
    $ show_sprites(("d 1 sad", "s 3 sad"))
    voice "ch5.5_d_001"
    d "Partner. Well — better not to ask, as they say."
    # JA[1307]: 相棒。 / まぁ、聞かぬが華ってヤツだよ。
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("d 1 sad", "s 1 sad"))
    voice "ch5.5_s_002"
    s "What's that supposed to mean?{#ch5_5_v11677}"
    # JA[11677]: なんだそりゃ。
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay19 hide]
    $ show_sprites(("s 1 sad"))
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")

    # ==== SCENE 321 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +53 → id(53)]
    $ fade_fx("id(53)", new_music="t18")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    th "Even after that, the days of practice continued.{#ch5_5_th_001}"
    # JA: （それからも練習の日々は続いた）
    th "The little princess's behavior on her daily visits is mystery enough, but it's just as mysterious that Kirche, Montmorency, and Guiche haven't come back.{#ch5_5_th_002}"
    # JA: （毎日通ってくるお姫さまの行動も謎だが、 / 　相変わらず、キュルケ、モンモランシー、 / 　ギーシュが戻ってこないのも謎だな）
    th "Who knows how this will turn out…{#ch5_5_th_003}"
    # JA: （まったく、どうなることやら……）
    stop music fadeout 1.0
    # [lay5 hide]
    # [BG hide]
    $ fade_fx("black")
    # [BG +54 → id(54)]
    $ fade_fx("id(54)", new_music="t22")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1"))
    voice "ch5.5_w_001"
    w "Everyone, attention!"
    # JA[15960]: 諸君、注目っ！
    voice "ch5.5_w_002"
    w "The script is done, and you've come a long way with the basics, so I'd like to move on to proper rehearsals."
    # JA[15961]: 台本も上がったし、基礎も大分出来るように / なってきたので、本格的に立ち稽古に / 入ろうと思います。
    # [lay20 x=-96]
    # [lay7 +962 → ha 2]
    $ show_sprites(("w 1", "ha 2"))
    voice "ch5.5_ha_014"
    ha "E-at last…?"
    # JA[2376]: え、ついに……ですか？
    # [lay7 hide]
    $ show_sprites(("w 1"))
    # [lay2 +502 → si 2 happy]
    $ show_sprites(("w 1", "si 2 happy"))
    voice "ch5.5_si_001"
    si "We did it, everyone."
    # JA[14785]: やりましたね、みなさん。
    voice "ch5.5_w_003"
    w "…Well, since those who aren't here can't be helped — here are the main roles as I picture them now."
    # JA[15962]: ……まあ、いない人達はしょうがないので、 / それでは現時点でイメージしてる / 主な配役を発表します。
    voice "ch5.5_w_004"
    w "Oh — but first, the plot of the second half…"
    # JA[15963]: っと、その前に後半の筋ね……。
    # [lay2 hide]
    $ show_sprites(("w 1"))
    # [lay20 x=64]
    voice "ch5.5_w_005"
    w "By the time their love had advanced as far as the prince's proposal, an epidemic breaks out in the girl's homeland — the enemy kingdom — and the royal family all perish."
    # JA[15964]: ２人の恋が王子の求婚にまで進展していた頃、 / 少女の故郷である敵国で疫病が流行り、王族が / すべて倒れるという事件が起こるの。
    voice "ch5.5_w_006"
    w "The panicked enemy country looks for an heir and finally finds Noelle. It immediately pressures the girl to return home at once."
    # JA[15965]: 慌てた敵国は後継者を探し、とうとうノエルを / 見つけだした。敵国はすぐさま少女を / 帰国させるよう、圧力をかけてくる。
    voice "ch5.5_w_007"
    w "It also insisted that her marriage to the prince of the enemy royal family would not be permitted."
    # JA[15966]: また、敵の王族である王子との結婚は許さない / とも主張してきたの。
    voice "ch5.5_si_002"
    si "So — what happens then?"
    # JA[14786]: で、どうなるんですか？
    voice "ch5.5_w_008"
    w "The kingdom and Prince Kane keep refusing the demands, but the angry enemy country finally uses its army to take Noelle back."
    # JA[15967]: 王国とケイン王子は要求を断り続けるけど、 / 怒った敵国は、とうとう軍隊を使ってノエルを / 取り戻そうとする。
    voice "ch5.5_w_009"
    w "The overwhelming enemy army. At last, the royal castle falls…"
    # JA[15968]: 圧倒的な敵軍。 / ついに落とされる王城……。
    voice "ch5.5_w_010"
    w "Holding back the enemy soldiers pouring in, the knights cry 'Long live the kingdom!' and die, one after another."
    # JA[15969]: 殺到する敵兵を食い止めながら、騎士達は / 王国万歳を叫び次々と死んでいく。
    voice "ch5.5_w_011"
    w "Prince Kane, wounded in battle, takes Noelle up the tower to make his final confession… And at the same time, he tells her to leave the castle."
    # JA[15970]: 戦いで傷ついたケイン王子は、ノエルを連れて / 塔へと登り、最後の告白をするの……。 / そして、同時に城を出るように告げた。
    voice "ch5.5_w_012"
    w "But the girl shakes her head. Even giving up her throne and life, she answered the prince's confession."
    # JA[15971]: けれど、少女は首を振る。 / 王位と命を捨てても、少女は王子の告白に / 応えた。
    voice "ch5.5_w_013"
    w "Then, surrounded by enemy soldiers, the two leap from the tower and end their own lives."
    # JA[15972]: そして、敵兵に囲まれた２人は、塔から身を投げ、 / 自らの命を絶つのでした。
    voice "ch5.5_w_014"
    w "From where the two fell, beautiful white flowers began to bloom. …That's the story."
    # JA[15973]: ２人が落ちた場所からは、美しい白い花が / 咲くようになった。 / ……ってお話。
    # [lay20 x=-96]
    # [lay5 +427 → s 3 angry]
    $ show_sprites(("w 1", "s 3 angry"))
    voice "ch5.5_s_003"
    s "Th-that's it? A bad ending?"
    # JA[11678]: そ、それでおしまい？ / バッドエンドかよ？
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("w 1 angry", "s 3 angry"))
    voice "ch5.5_w_015"
    w "Got some complaint?"
    # JA[15974]: なにか不満でも？

    # ---- 【選択肢】 ----
    menu:
        "What a horrible story":
            # JA: ひどい話だ
            # ==== SCENE 322 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay5 +427 → s 3 angry]
            $ show_sprites(("w 1 angry", "s 3 angry"))
            play music t22 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("w 1 angry", "s 1 angry"))
            voice "ch5.5_s_004"
            s "What a horrible story."
            # JA[11679]: ひどい話だな。
            # [lay20 hide]
            $ show_sprites(("s 1 angry"))
            # [lay1 +319 → l 6 sad]
            $ show_sprites(("l 6 sad", "s 1 angry"))
            voice "ch5.5_l_018"
            l "What do you mean? It's a good story!"
            # JA[6248]: なによ、いいお話じゃない！
            $ update_sympathy(-10, char_key="louise")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            # [lay5 hide]
            $ show_sprites(("l 6 sad"))
            # [lay2 +506 → si 2 sad]
            $ show_sprites(("l 6 sad", "si 2 sad"))
            voice "ch5.5_si_003"
            si "That's right, Saito-san!"
            # JA[14787]: そうですよ、サイトさん！
            $ update_sympathy(-10, char_key="siesta")
            # [lay2 hide]
            $ show_sprites(("l 6 sad"))
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("l 6 sad", "s 1 angry"))
            voice "ch5.5_s_005"
            s "But it's a tragedy! Nothing beats a happy ending!"
            # JA[11680]: だって悲劇だろ！ / 物語はハッピーエンドに限るって！
            # [lay1 +317 → l 6 angry]
            $ show_sprites(("l 6 angry", "s 1 angry"))
            voice "ch5.5_l_019"
            l "A happy ending without any reason — isn't it just a comedy?!"
            # JA[6249]: 理由の無いハッピーエンドなんて / 喜劇じゃないの！
            # [lay1 hide]
            $ show_sprites(("s 1 angry"))
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1", "s 1 angry"))
            voice "ch5.5_w_016"
            w "I understand that Saito likes those comedy-style happy endings, though."
            # JA[15975]: サイトは、喜劇じみたハッピーエンドが / 好みなのは解ったけど。
            voice "ch5.5_w_017"
            w "But I'd like to save that for another performance. This play is a 'tragedy.'"
            # JA[15976]: でも、それはまた別の公演にして欲しいな。 / 今回の芝居は『悲劇』なんだよ。
        "It's a good story":
            # JA: いい話だ
            # ==== SCENE 323 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay5 +427 → s 3 angry]
            $ show_sprites(("w 1 angry", "s 3 angry"))
            play music t22 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay5 +390 → s 1]
            $ show_sprites(("w 1 angry", "s 1"))
            voice "ch5.5_s_006"
            s "No, I think it's a good story."
            # JA[11681]: いや、いい話だと思うけど。
            # [lay20 hide]
            $ show_sprites(("s 1"))
            # [lay1 +313 → l 6]
            $ show_sprites(("l 6", "s 1"))
            voice "ch5.5_l_020"
            l "My? Saito, can you tell a good story from a bad one?"
            # JA[6250]: あら？ / サイトにお話の良し悪しが分かるの？
            # [lay5 +423 → s 3]
            $ show_sprites(("l 6", "s 3"))
            voice "ch5.5_s_007"
            s "I read quite a lot, you know. W-well, so I like to think my eye is reasonably sharp!"
            # JA[11682]: 結構、本を読んでるんでね。 / ま、まあ、そんなわけで、 / それなりに目は肥えてるつもりだ！
            # [TNDL       tndl(30)] — не переносится (система не реализована, AGENTS §6)
            th "They're comics, though.{#ch5_5_th_004}"
            # JA: （マンガだけどな）
            # [lay1 hide]
            $ show_sprites(("s 3"))
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1", "s 3"))
            voice "ch5.5_w_018"
            w "Is that so."
            # JA[15977]: へえ。
        "I don't get it":
            # JA: よく分かんない
            # ==== SCENE 324 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay5 +427 → s 3 angry]
            $ show_sprites(("w 1 angry", "s 3 angry"))
            play music t22 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("w 1 angry", "s 1 sad"))
            voice "ch5.5_s_008"
            s "No, I don't really get it."
            # JA[11683]: いや、よく分かんない。
            # [lay20 +1067 → w 1 sad]
            $ show_sprites(("w 1 sad", "s 1 sad"))
            voice "ch5.5_w_019"
            w "Now, now. Saito, that's a problem."
            # JA[15978]: おいおい。 / サイト、それでは困るよ。
            voice "ch5.5_w_020"
            w "Well, next time I'll just have to make you read books until you're sick of them, won't I?"
            # JA[15979]: まぁ、今度嫌というほど、 / 本を読んでもらわないといけないかな？
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("w 1 sad", "s 3 sad"))
            voice "ch5.5_s_009"
            s "N-no… And, well…"
            # JA[11684]: い、いや……。 / その……。

    # ==== SCENE 325 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1"))
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("w 1", "s 1 angry"))
    play music t22 fadein 1.0
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [lay5 hide]
    $ show_sprites(("w 1"))
    # [lay20 +1061 → w 1]
    voice "ch5.5_w_021"
    w "Now, about the casting…"
    # JA[15980]: さて、配役だけど……。
    th "…….{#ch5_5_th_005}"
    # JA: ……。
    voice "ch5.5_w_022"
    w "First, our own Prince Kane — you, Saito!"
    # JA[15981]: まず、自国の王子ケインは……サイト！
    # [lay20 x=-96]
    # [lay5 +427 → s 3 angry]
    $ show_sprites(("w 1", "s 3 angry"))
    voice "ch5.5_s_010"
    s "…Whaaat!? M-me?"
    # JA[11685]: ……ええっ！ / お、俺？
    voice "ch5.5_w_023"
    w "The heroine, the girl Noelle — you, Louise!"
    # JA[15982]: ヒロインの少女ノエルは……ルイズ！
    # [lay5 hide]
    $ show_sprites(("w 1"))
    # [lay1 +315 → l 6 happy]
    $ show_sprites(("w 1", "l 6 happy"))
    voice "ch5.5_l_021"
    l "…Ufufu, of course!"
    # JA[6251]: ……うふふ、当然ね！
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("w 1 angry", "l 6 happy"))
    voice "ch5.5_w_024"
    w "However — provisional!"
    # JA[15983]: ただし、暫定！
    # [lay1 +317 → l 6 angry]
    $ show_sprites(("w 1 angry", "l 6 angry"))
    voice "ch5.5_l_022"
    l "…Eh? W-wait! What do you mean, provisional?!"
    # JA[6252]: ……え？ / ち、ちょっと！ / 暫定って何よ！
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1", "l 6 angry"))
    voice "ch5.5_w_025"
    w "Everyone's still rough, but they've got the right stuff. Depending on how the other candidates turn out, I may swap you out."
    # JA[15984]: まだ、みんな荒削りだが筋はいい。 / 他の候補の仕上がり次第では / 差し替えるかもしれない。
    voice "ch5.5_w_026"
    w "I need a little more time before the final decision."
    # JA[15985]: もう少し決定まで時間がほしいんだ。
    # [lay20 hide]
    $ show_sprites(("l 6 angry"))
    # [lay1 hide]
    $ show_sprites()
    # [lay6 +689 → k 2 happy]
    $ show_sprites(("k 2 happy"))
    voice "ch5.5_k_001"
    k "Oh my? Then I might still have a shot at the lead?"
    # JA[3272]: あら？ / じゃあまだ主役を狙えたりするの？
    stop music fadeout 1.0
    play music t4 fadein 1.0
    # [lay6 x=224]
    # [lay1 +317 → l 6 angry]
    $ show_sprites(("l 6 angry", "k 2 happy"))
    voice "ch5.5_l_023"
    l "Kirche!"
    # JA[6253]: キュルケ！
    # [lay6 hide]
    $ show_sprites(("l 6 angry"))
    # [lay3 +867 → m 2 angry]
    $ show_sprites(("l 6 angry", "m 2 angry"))
    voice "ch5.5_m_001"
    m "Louise as the lead over me — that's impossible."
    # JA[4084]: わたしを差し置いて、 / ルイズが主役なんてありえないわよ。
    # [lay1 hide]
    $ show_sprites(("m 2 angry"))
    # [lay4 +570 → g 2 angry]
    $ show_sprites(("g 2 angry", "m 2 angry"))
    voice "ch5.5_g_001"
    g "Y-you, the lead… U-unforgivable!"
    # JA[1516]: き、きみが主役だと……。 / ゆ、許せん！
    # [lay3 hide]
    $ show_sprites(("g 2 angry"))
    # [lay5 +392 → s 1 happy]
    $ show_sprites(("g 2 angry", "s 1 happy"))
    voice "ch5.5_s_011"
    s "Everyone!"
    # JA[11686]: みんな！
    # [lay4 hide]
    $ show_sprites(("s 1 happy"))
    # [lay20 +1067 → w 1 sad]
    $ show_sprites(("w 1 sad", "s 1 happy"))
    voice "ch5.5_w_027"
    w "…Never mind. Everything is decided on merit alone. You all truly have a chance."
    # JA[15986]: ……まあいいわ。 / 全ては実力で決める。 / 確かにあなた達にもチャンスはあるわよ。
    # [lay5 hide]
    $ show_sprites(("w 1 sad"))
    # [lay6 +687 → k 2]
    $ show_sprites(("w 1 sad", "k 2"))
    voice "ch5.5_k_002"
    k "What a generous decision."
    # JA[3273]: さすが、寛大な処置ね。

    # ==== SCENE 325 ====

    # ---- 【選択肢】 ----
    menu:
        "I'm glad!":
            # JA: 良かったな！
            # ==== SCENE 326 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1067 → w 1 sad]
            $ show_sprites(("w 1 sad"))
            # [lay6 +687 → k 2]
            $ show_sprites(("w 1 sad", "k 2"))
            play music t4 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay20 hide]
            $ show_sprites(("k 2"))
            # [lay5 +392 → s 1 happy]
            $ show_sprites(("s 1 happy", "k 2"))
            voice "ch5.5_s_012"
            s "I'm glad for you. Kirche, Montmon!"
            # JA[11687]: 良かったな。 / キュルケ、モンモン！
            # [lay6 +689 → k 2 happy]
            $ show_sprites(("s 1 happy", "k 2 happy"))
            voice "ch5.5_k_003"
            k "Oh, thank you. My darling."
            # JA[3274]: あら、ありがと。 / ダーリン。
            $ update_sympathy(10, char_key="kirche")
            # [lay5 hide]
            $ show_sprites(("k 2 happy"))
            # [lay3 +869 → m 2 sad]
            $ show_sprites(("m 2 sad", "k 2 happy"))
            voice "ch5.5_m_002"
            m "Well, it'll be work making up the lost ground, though."
            # JA[4085]: まあ、遅れを取り戻すぶん大変ですけどね。
            # [lay3 hide]
            $ show_sprites(("k 2 happy"))
            # [lay1 +317 → l 6 angry]
            $ show_sprites(("l 6 angry", "k 2 happy"))
            voice "ch5.5_l_024"
            l "…Saito, one moment. Does that mean you're dissatisfied with me as the heroine?"
            # JA[6254]: ……ちょっと、サイト。 / それはわたしがヒロインでは不満ってこと / かしら？
            $ update_sympathy(-10, char_key="louise")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            # [lay6 hide]
            $ show_sprites(("l 6 angry"))
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("l 6 angry", "s 3 sad"))
            voice "ch5.5_s_013"
            s "N-no, that's not what I mean at all…"
            # JA[11688]: い、いや、そういうわけでは決して……。
            # [lay1 hide]
            $ show_sprites(("s 3 sad"))
            # [lay5 hide]
            $ show_sprites()
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1"))
        "Don't underestimate us!":
            # JA: 俺達を甘く見るなよ！
            # ==== SCENE 327 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1067 → w 1 sad]
            $ show_sprites(("w 1 sad"))
            # [lay6 +687 → k 2]
            $ show_sprites(("w 1 sad", "k 2"))
            play music t4 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay20 hide]
            $ show_sprites(("k 2"))
            # [lay5 +392 → s 1 happy]
            $ show_sprites(("s 1 happy", "k 2"))
            voice "ch5.5_s_014"
            s "Don't underestimate us — you had us do nothing but grueling basics!"
            # JA[11689]: ずっとつらい基礎ばかりやらされていた / 俺達を舐めるなよ！
            # [TNDL       tndl(30)] — не переносится (система не реализована, AGENTS §6)
            # [lay6 +689 → k 2 happy]
            $ show_sprites(("s 1 happy", "k 2 happy"))
            voice "ch5.5_k_004"
            k "Oh my, quite the confidence. My darling."
            # JA[3275]: あら、なかなかたいした自信ね。 / ダーリン。
            # [lay6 hide]
            $ show_sprites(("s 1 happy"))
            # [lay5 hide]
            $ show_sprites()
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1"))
        "Could my role be swapped too?":
            # JA: 俺の役も交替の可能性が？
            # ==== SCENE 328 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1067 → w 1 sad]
            $ show_sprites(("w 1 sad"))
            # [lay6 +687 → k 2]
            $ show_sprites(("w 1 sad", "k 2"))
            play music t4 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay6 hide]
            $ show_sprites(("w 1 sad"))
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("w 1 sad", "s 3 sad"))
            voice "ch5.5_s_015"
            s "U-um. Is there a chance my role could be swapped too?"
            # JA[11690]: あ、あの。 / 俺の役も交替の可能性が？
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1", "s 3 sad"))
            voice "ch5.5_w_028"
            w "Of course there is. Like I said just now. It's provisional through and through."
            # JA[15987]: もちろんありうるわよ。 / さっきも言ったとおりよ。 / あくまで暫定。
            voice "ch5.5_w_029"
            w "Besides, sometimes a woman plays the part. Don't get complacent."
            # JA[15988]: それに女性が演じる場合もあるの。 / うかうかしないでね。
            # [lay5 hide]
            $ show_sprites(("w 1"))
            # [lay20 x=64]

    # ==== SCENE 329 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1"))
    play music t4 fadein 1.0
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    voice "ch5.5_w_030"
    w "…The final roles, including the rest of the cast, will be announced another day."
    # JA[15989]: ……その他のキャストを含めた最終的な役は、 / 後日発表します。
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("w 1 angry"))
    voice "ch5.5_w_031"
    w "Now, work hard at rehearsal. Dismissed!"
    # JA[15990]: では稽古に精を出すように。 / 解散！
    # [lay20 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [BG +88 → sky]
    $ fade_fx("sky")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    th "And then the days of preparing and rehearsing for the show flew by in a blink.{#ch5_5_th_006}"
    # JA: （そして、公演の準備と稽古にあけくれる / 　日々は瞬く間に過ぎていった）
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay5 hide]
    # [BG hide]
    $ fade_fx("black")

    # ==== SCENE 330 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +54 → id(54)]
    $ fade_fx("id(54)", new_music="t18")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay6 +689 → k 2 happy]
    $ show_sprites(("k 2 happy"))
    voice "ch5.5_k_005"
    k "Well then — good work, everyone!"
    # JA[3276]: それじゃ、おつかれさまーっ！
    # [lay6 x=-96]
    # [lay1 +313 → l 6]
    $ show_sprites(("k 2 happy", "l 6"))
    voice "ch5.5_l_025"
    l "…What's with you, Kirche. You were complaining the whole time, but lately you've gone completely zealous?"
    # JA[6255]: ……なによ、キュルケ。 / あんなにぶつぶつ文句ばかり言ってたのに、 / 最近はすっかり熱心じゃない？
    # [lay6 +687 → k 2]
    $ show_sprites(("k 2", "l 6"))
    voice "ch5.5_k_006"
    k "…Oh my, I've never been one to mind this sort of thing, to begin with."
    # JA[3277]: ……あら、だってあたしはもともと / こーゆーの嫌いじゃないし。
    # [lay1 +317 → l 6 angry]
    $ show_sprites(("k 2", "l 6 angry"))
    voice "ch5.5_l_026"
    l "Easy for you to say. Even though you ran away halfway…"
    # JA[6256]: ふん、よくいうわよ。 / 途中で一度逃げだしたくせに……。
    # [lay6 +693 → k 2 sad]
    $ show_sprites(("k 2 sad", "l 6 angry"))
    voice "ch5.5_k_007"
    k "That's…!"
    # JA[3278]: それは……！
    # [lay0 +632 → t 5]
    $ show_sprites(("k 2 sad", "t 5", "l 6 angry"))
    voice "ch5.5_t_001"
    th "Kui kui."
    # JA[15580]: （くいくい）
    # [lay0 hide]
    $ show_sprites(("k 2 sad", "l 6 angry"))
    # [lay6 +687 → k 2]
    $ show_sprites(("k 2", "l 6 angry"))
    voice "ch5.5_k_008"
    k "That's true."
    # JA[3279]: それは、そうね。
    voice "ch5.5_k_009"
    k "…By the way. Say, my darling."
    # JA[3280]: ……ところで。 / ねえ、ダーリン。
    # [lay1 hide]
    $ show_sprites(("k 2"))
    # [lay5 +390 → s 1]
    $ show_sprites(("k 2", "s 1"))
    voice "ch5.5_s_016"
    s "What is it, Kirche?"
    # JA[11691]: なんだ、キュルケ？
    voice "ch5.5_k_010"
    k "Haven't you forgotten something? Something very important."
    # JA[3281]: 『何か忘れてること』ないかしら？ / とても大切なこと。
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("k 2", "s 3 sad"))
    voice "ch5.5_s_017"
    s "Eh? Something I forgot?"
    # JA[11692]: へ？ / 忘れてること？

    # ---- 【選択肢】 ----
    menu:
        "Looking for the bomb user?":
            # JA: 爆弾使い探し？
            # ==== SCENE 331 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            # [lay6 +687 → k 2]
            $ show_sprites(("k 2", "s 3 sad"))
            play music t18 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("k 2", "s 1 sad"))
            voice "ch5.5_s_018"
            s "Do you mean looking for 'the bomb user' the Queen asked me about?"
            # JA[11693]: それってもしかして、女王様から頼まれた / 「爆弾使い」を探すこと？
            # [lay6 +689 → k 2 happy]
            $ show_sprites(("k 2 happy", "s 1 sad"))
            voice "ch5.5_k_011"
            k "Correct."
            # JA[3282]: そう、正解。
            $ update_sympathy(10, char_key="kirche")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
        "Kirche's birthday?":
            # JA: キュルケの誕生日？
            # ==== SCENE 332 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            # [lay6 +687 → k 2]
            $ show_sprites(("k 2", "s 3 sad"))
            play music t18 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("k 2", "s 1 sad"))
            voice "ch5.5_s_019"
            s "Do you mean that today is Kirche's birthday?"
            # JA[11694]: それってもしかして、 / 今日がキュルケの誕生日ってこと？
            # [lay6 +693 → k 2 sad]
            $ show_sprites(("k 2 sad", "s 1 sad"))
            voice "ch5.5_k_012"
            k "I'm sorry. Today isn't that day."
            # JA[3283]: ごめんなさい。 / 今日はその日ではないの。
            $ update_sympathy(-10, char_key="kirche")
            # [lay6 +687 → k 2]
            $ show_sprites(("k 2", "s 1 sad"))
            voice "ch5.5_k_013"
            k "The answer is: what happened to finding 'the bomb user'?{#ch5_5_v3284}"
            # JA[3284]: 正解は、「爆弾使い」を探すこと / ってどうなったのかなぁってこと。
        "My dance footwork?":
            # JA: ダンスの足さばき？
            # ==== SCENE 333 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            # [lay6 +687 → k 2]
            $ show_sprites(("k 2", "s 3 sad"))
            play music t18 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("k 2", "s 1 sad"))
            voice "ch5.5_s_020"
            s "Could it be that my footwork in the dance wasn't good today?"
            # JA[11695]: もしかして、ダンスの足さばきが / 今日は上手くなかったとか？
            # [lay6 +693 → k 2 sad]
            $ show_sprites(("k 2 sad", "s 1 sad"))
            voice "ch5.5_k_014"
            k "Hmm. No, that's not it."
            # JA[3285]: うーん。 / そうじゃないのよ。
            # [lay6 +693 → k 2 sad]
            voice "ch5.5_k_015"
            k "The answer is: what happened to finding 'the bomb user'?{#ch5_5_v3286}"
            # JA[3286]: 正解は、「爆弾使い」を探すこと / ってどうなったのかなぁってこと。

    # ==== SCENE 334 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("s 1 sad"))
    # [lay6 +689 → k 2 happy]
    $ show_sprites(("k 2 happy", "s 1 sad"))
    play music t18 fadein 1.0
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [lay5 +427 → s 3 angry]
    $ show_sprites(("k 2 happy", "s 3 angry"))
    voice "ch5.5_s_021"
    s "Crap. I've been so busy with practice lately I haven't been able to look around at all."
    # JA[11696]: やばっ。 / ここ最近練習に忙しくて、 / ぜんぜん見て回れていないよ。
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("k 2 happy", "s 3 sad"))
    voice "ch5.5_s_022"
    s "I-I have to tell Louise about this…"
    # JA[11697]: ル、ル、ルイズにこのことを知らせないと……。
    # [lay6 hide]
    $ show_sprites(("s 3 sad"))
    # [lay0 +632 → t 5]
    $ show_sprites(("t 5", "s 3 sad"))
    voice "ch5.5_t_002"
    t "…It's fine."
    # JA[15581]: ……大丈夫。
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("t 5", "s 1 sad"))
    voice "ch5.5_s_023"
    s "…Eh?"
    # JA[11698]: ……えっ？
    th "According to Tabitha, Kirche, Montmorency, and Guiche had looked into the bomb user for me.{#ch5_5_th_007}"
    # JA: （タバサが言うには、キュルケ、 / 　モンモランシー、ギーシュで、 / 　爆弾使いの調べをしてくれたらしい）
    # [lay0 hide]
    $ show_sprites(("s 1 sad"))
    # [lay6 +693 → k 2 sad]
    $ show_sprites(("k 2 sad", "s 1 sad"))
    voice "ch5.5_k_016"
    k "…Aah, you didn't have to give me away so soon. I wanted to watch my darling squirm a little longer…"
    # JA[3287]: ……ああ、そんなにすぐにバラさなくても。 / もう少し、ダーリンがあわてるところを / 見たかったのに……。
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("k 2 sad", "s 3 sad"))
    voice "ch5.5_s_024"
    s "Kirche. You could have just told me so."
    # JA[11699]: キュルケ。 / そうならそうと言ってくれれば良かったのに。
    # [lay6 +687 → k 2]
    $ show_sprites(("k 2", "s 3 sad"))
    voice "ch5.5_k_017"
    k "Well, you know Louise — when she gets going, she goes straight ahead, doesn't she?"
    # JA[3288]: まあ、ほら、ルイズって、 / 入れ込むと一直線でしょ？
    voice "ch5.5_k_018"
    k "Besides, that girl isn't good at asking others for favors, so we just kept quiet."
    # JA[3289]: それにあの子、他人にお願いするのが / 苦手みたいだし。 / だから、黙ってただけよ。
    # [lay0 +632 → t 5]
    $ show_sprites(("k 2", "t 5", "s 3 sad"))
    voice "ch5.5_t_003"
    t "Just covering your embarrassment."
    # JA[15582]: 照れ隠し。
    # [lay0 hide]
    $ show_sprites(("k 2", "s 3 sad"))
    # [lay6 +695 → k 2 shy]
    $ show_sprites(("k 2 shy", "s 3 sad"))
    voice "ch5.5_k_019"
    k "Th-that's not it!"
    # JA[3290]: ち、違うわよ！
    # [lay0 hide]
    # [lay5 +390 → s 1]
    $ show_sprites(("k 2 shy", "s 1"))
    voice "ch5.5_s_025"
    s "Kirche, thanks. I'll say it in Louise's place."
    # JA[11700]: キュルケ、ありがとうな。 / ルイズの代わりに言っておくよ。
    # [lay6 +689 → k 2 happy]
    $ show_sprites(("k 2 happy", "s 1"))
    voice "ch5.5_k_020"
    k "Honestly, my darling."
    # JA[3291]: もう、ダーリンったら。
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay5 hide]
    $ show_sprites(("k 2 happy"))
    # [lay6 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")

    # [移動] → next(335): сцена 335 — часть 6 главы 5
    jump ch5_6
