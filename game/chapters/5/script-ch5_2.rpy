# Глава 5, часть 2 (сцены 285–299): объяснения у гостевого дома, решение
# ехать к театру, попытка войти через дверь и разговор с труппой.
# Источник: ps2_source/chapters/chapter_06_本当の想い.txt (SCENE 285–299).
# Точные аргументы: ps2_source/events_full/chapter_06_本当の想い.txt.
# Скелет собран генератором tools/gen_ch5_2_script.py (EN — tools/ch5_2_en.py,
#   RU — tools/ch5_2_ru.py), поэтому порядок реплик, голоса, спрайты и
#   события совпадают с источником дословно.
#
# Вход — jump ch5_2 из script-ch5_1.rpy; выход — jump ch5_3 (сцена 300) —
#   E7 «forward debt», закроется частью 3.
#
# Голоса: ch5.2_<spk>_<NNN> — новая группа части 2, нумерация с 001 по
#   говорящему, порядок порта (285 → 286–288 → 289 → 290 → 291–293 → 294 →
#   295 → 296–298 → 299).
#
# Не портируются: item() (инвентарь не реализован), TNDL, SE, waitAction/
#   waitTime/waitSEStop/waitLoad, msgon/msgoff, back(), beginSkip.
#
# Фоны/CG: id(43), id(52), id(54), id(131), id(132) — имена пусты в
#   image_id_map.csv (заглушки), bg 90 = sky_night.
#
# Спрайты 309, 500, 593, 963 — PROVISIONAL (пиксель-сверка SCENEDAT
#   невозможна, архив PS2 не смонтирован): имена выведены по блок-правилу
#   справочника (база B = id - ((id - 5) mod 11); 0/1 — база, 2/3 — happy,
#   4/5 — angry, 6/7 — sad, 8/9 — shy).


label ch5_2:
    # Часть 2: разговор у гостевого дома (сцена 285) → решение ехать к театру → попытка попасть внутрь → разговор с труппой.
    # Сцена 285 начинается с RESET (возврат в гостиницу).

    # ==== SCENE 285 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +90 → sky_night]
    $ fade_fx("sky_night", new_music="t19")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    voice "ch5.2_k_001"
    k "Hmph. So that's how it is, then."
    # JA[3246]: ふーん。 / そういうことがあったのね。
    # [lay6 hide]
    # [BG hide]
    $ fade_fx("black")
    # [BG +43 → id(43)]
    $ fade_fx("id(43)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay6 +676 → k 1]
    $ show_sprites(("k 1"))
    th "We'd gone back to the inn, and Kirche had us cornered there…{#ch5_2_th_001}"
    # JA: （宿に戻った俺達は、キュルケ達に / 　問い詰められて……）
    th "Unable to cover it up, I ended up telling her the Queen's orders{#ch5_2_th_002}"
    # JA: （ごまかすことができなくった俺は、 / 　女王様からの指令を教えてしまった）
    # [lay6 x=-96]
    # [lay5 +390 → s 1]
    $ show_sprites(("k 1", "s 1"))
    voice "ch5.2_s_001"
    s "Well, that's about it. Only, keep it a secret, all right? Officially, it's a secret mission, you know."
    # JA[11617]: まぁ、そういうこと。 / ただし、内緒にしてくれよ。 / 一応、秘密任務ってことになってるんだ。
    # [lay6 +684 → k 1 shy]
    $ show_sprites(("k 1 shy", "s 1"))
    voice "ch5.2_k_002"
    k "Hmm. If it's a request from my darling, maybe I'll hear you out?"
    # JA[3247]: うーん、ダーリンのお願いなら、 / 聞いちゃおうかな？
    # [lay5 hide]
    $ show_sprites(("k 1 shy"))
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("k 1 shy", "l 1 sad"))
    voice "ch5.2_l_001"
    l "…….{#ch5_2_v6192}"
    # JA[6192]: ……。
    # [lay6 +676 → k 1]
    $ show_sprites(("k 1", "l 1 sad"))
    voice "ch5.2_k_003"
    k "Even so — Louise being a childhood friend of the Queen… You can't judge a book by its cover, can you?"
    # JA[3248]: それにしても、ルイズが女王様と幼馴染 / とはねぇ。 / 人は見かけによらないわね。
    # [lay1 +302 → l 1]
    $ show_sprites(("k 1", "l 1"))
    voice "ch5.2_l_002"
    l "That's a secret too, you know."
    # JA[6193]: そのことも秘密だからね。
    voice "ch5.2_k_004"
    k "Yes, yes, yes…"
    # JA[3249]: はいはい……。
    # [lay1 hide]
    $ show_sprites(("k 1"))
    # [lay3 +852 → m 1]
    $ show_sprites(("k 1", "m 1"))
    voice "ch5.2_m_001"
    m "So the rest is about the bag, right? Was it really Haruna's bag?"
    # JA[4073]: 後はバッグのことよね？ / 本当にハルナのバッグだったの？
    # [lay6 hide]
    $ show_sprites(("m 1"))
    # [lay7 +962 → ha 2]
    $ show_sprites(("ha 2", "m 1"))
    voice "ch5.2_ha_001"
    ha "Yes, that's right.{#ch5_2_v2343}"
    # JA[2343]: はい、間違いありません。
    # [lay3 hide]
    $ show_sprites(("ha 2"))
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("ha 2", "s 3 sad"))
    voice "ch5.2_s_002"
    s "Ah… Well, even if you call it proof, I don't know…"
    # JA[11618]: はぁ……。 / それにしても、証拠って言われてもねぇ……。
    voice "ch5.2_ha_002"
    ha "Could we go and ask once more? There's a hidden pocket inside the bag."
    # JA[2344]: もう一度お願いにいきませんか？ / バッグの中に隠しポケットがあるんです。
    voice "ch5.2_ha_003"
    ha "If my things are in there, I think that would be proof."
    # JA[2345]: その中に私のものが入っていれば、 / それが証拠になると思うんです。
    # [lay5 +425 → s 3 happy]
    $ show_sprites(("ha 2", "s 3 happy"))
    voice "ch5.2_s_003"
    s "I see… Right, if it's a hidden pocket, there's no way it would have been found unless something extraordinary happened."
    # JA[11619]: なるほどね……。 / 確かに隠しポケットだったら、 / よほどのことが無い限りばれてないと。
    # [lay7 hide]
    $ show_sprites(("s 3 happy"))
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "s 3 happy"))
    voice "ch5.2_l_003"
    l "Are you sure it's safe? Meeting a traveling troupe is dangerous."
    # JA[6194]: 大丈夫なの？ / 旅役者に会うなんて危険よ。
    # [lay5 +392 → s 1 happy]
    $ show_sprites(("l 1 sad", "s 1 happy"))
    voice "ch5.2_s_004"
    s "What's dangerous about a traveling troupe? They're performers, aren't they? Not exactly ordinary folk."
    # JA[11620]: 旅役者って何が危険なんだよ。 / 芸能人だろ？ / 凄いじゃないか？
    # [lay1 hide]
    $ show_sprites(("s 1 happy"))
    # [lay6 +680 → k 1 angry]
    $ show_sprites(("k 1 angry", "s 1 happy"))
    voice "ch5.2_k_005"
    k "…No, that's out of the question. A shifty drifter like that — you can't expect him not to have something on him."
    # JA[3250]: ……駄目よ。 / あんな得体の知れない流れ者が何もないはずが / ないじゃない。
    # [lay5 hide]
    $ show_sprites(("k 1 angry"))
    # [lay2 +506 → si 2 sad]
    $ show_sprites(("k 1 angry", "si 2 sad"))
    voice "ch5.2_si_001"
    si "When I was a child… I used to look forward to a troupe coming to our village at the festival…"
    # JA[14772]: 子供の頃……。 / お祭りで村に一座が来るのは楽しみにして / ましたけど……。
    voice "ch5.2_si_002"
    si "They say travelers like that are dangerous. They carry off pretty children, so be careful… They used to scare us with that."
    # JA[14773]: ああいう旅の人達は危ないって。 / かわいい子供をさらったりするから / 気をつけろって……よく脅かされました。
    # [lay6 hide]
    $ show_sprites(("si 2 sad"))
    # [lay3 +858 → m 1 sad]
    $ show_sprites(("m 1 sad", "si 2 sad"))
    voice "ch5.2_m_002"
    m "Well, common sense, I suppose."
    # JA[4074]: まぁ、常識よね。
    th "But this world really has changed, hasn't it. …No, wait. Maybe I'm the one who's out of place here…{#ch5_2_th_003}"
    # JA: （しかし、この世界は本当に変わってるよな。 / 　いや、俺のほうがこの世界では非常識 / 　なのか……）
    # [lay3 hide]
    $ show_sprites(("si 2 sad"))
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "si 2 sad"))
    voice "ch5.2_l_004"
    l "Oh, enough! Neither the bag nor the traveling troupe!"
    # JA[6195]: もうっ、いいじゃない！ / バッグも旅役者も！
    # [lay2 hide]
    $ show_sprites(("l 1 angry"))
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("l 1 angry", "ha 2 sad"))
    voice "ch5.2_ha_004"
    ha "No, it's not! Not for me, anyway…"
    # JA[2346]: よ、よくありません！ / 私にとっては……。
    # [lay7 +966 → ha 2 angry]
    $ show_sprites(("l 1 angry", "ha 2 angry"))
    voice "ch5.2_ha_005"
    ha "It's, it's the only thing tying me to my old world… to Japan…. …Let me go and ask once more. Right now."
    # JA[2347]: も、元の世界の……日本の……。 / たったひとつのつながりなんです。 / ……私、今からもう一度頼んできます。
    # [lay1 hide]
    $ show_sprites(("ha 2 angry"))
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("s 1 sad", "ha 2 angry"))
    voice "ch5.2_s_005"
    s "My old world… the bond with Japan… …Yeah. That's right."
    # JA[11621]: 元の世界……日本との絆か……。 / ……そうだよな。

    # ---- 【選択肢】 ----
    menu:
        "I'm coming along too.":
            # JA: 俺も行くよ
            # ==== SCENE 286 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("s 1 sad"))
            # [lay7 +966 → ha 2 angry]
            $ show_sprites(("s 1 sad", "ha 2 angry"))
            play music t19 fadein 1.0
            # [BG +43 → id(43)]
            $ fade_fx("id(43)")
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1", "ha 2 angry"))
            voice "ch5.2_s_006"
            s "…I'm coming along too. Nights are dangerous in all sorts of ways. I can't let you go alone, can I?"
            # JA[11622]: ……俺も行くよ。 / 夜はいろいろ危険だからな。 / １人で行かせるわけにはいかないだろ？
            # [lay7 +970 → ha 2 shy]
            $ show_sprites(("s 1", "ha 2 shy"))
            voice "ch5.2_ha_006"
            ha "Hiraga-kun…{#ch5_2_v2348}"
            # JA[2348]: 平賀くん……。
            $ update_sympathy(10, char_key="haruna")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
        "Take care of yourself.":
            # JA: 気をつけてな
            # ==== SCENE 287 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("s 1 sad"))
            # [lay7 +966 → ha 2 angry]
            $ show_sprites(("s 1 sad", "ha 2 angry"))
            play music t19 fadein 1.0
            # [BG +43 → id(43)]
            $ fade_fx("id(43)")
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1", "ha 2 angry"))
            voice "ch5.2_s_007"
            s "Take care of yourself out there."
            # JA[11623]: 気をつけて行くんだぞ。
            # [lay7 hide]
            $ show_sprites(("s 1"))
            # [lay2 +506 → si 2 sad]
            $ show_sprites(("s 1", "si 2 sad"))
            voice "ch5.2_si_003"
            si "Saito-san. Aren't you going to protect Haruna-san?"
            # JA[14774]: サイトさん。 / ハルナさんを守ってあげないんですか？
            # [lay5 +425 → s 3 happy]
            $ show_sprites(("s 3 happy", "si 2 sad"))
            voice "ch5.2_s_008"
            s "Eh? Ah… Correction, correction! I'll come along as well."
            # JA[11624]: えっ？ / あ……訂正、訂正！ / 俺も行かせていただきます。
            # [lay2 hide]
            $ show_sprites(("s 3 happy"))
            # [lay7 +962 → ha 2]
            $ show_sprites(("s 3 happy", "ha 2"))
            voice "ch5.2_ha_007"
            ha "Hiraga-kun!"
            # JA[2349]: 平賀くん！
            $ update_sympathy(-10, char_key="haruna")
        "What if Siesta came along?":
            # JA: シエスタが付いていったら？
            # ==== SCENE 288 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("s 1 sad"))
            # [lay7 +966 → ha 2 angry]
            $ show_sprites(("s 1 sad", "ha 2 angry"))
            play music t19 fadein 1.0
            # [BG +43 → id(43)]
            $ fade_fx("id(43)")
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1", "ha 2 angry"))
            voice "ch5.2_s_009"
            s "She's the same kind of girl, right? How about Siesta coming along?"
            # JA[11625]: 同じ女の子だろ？ / シエスタが付いていったらどうだ？
            # [lay7 hide]
            $ show_sprites(("s 1"))
            # [lay2 +506 → si 2 sad]
            $ show_sprites(("s 1", "si 2 sad"))
            voice "ch5.2_si_004"
            si "I, I couldn't protect Haruna-san if something happened. So, Saito-san…"
            # JA[14775]: わ、わたしではいざというとき、 / ハルナさんを守れません。 / だから、サイトさん……。
            # [lay5 +425 → s 3 happy]
            $ show_sprites(("s 3 happy", "si 2 sad"))
            voice "ch5.2_s_010"
            s "R-right. It's dangerous on the roads at night, so I'll go with you."
            # JA[11626]: そ、そうだよな。 / 夜道は危ないので、俺が付いてくよ。
            # [lay2 hide]
            $ show_sprites(("s 3 happy"))
            # [lay7 +968 → ha 2 sad]
            $ show_sprites(("s 3 happy", "ha 2 sad"))
            voice "ch5.2_ha_008"
            ha "Hiraga-kun…{#ch5_2_v2350}"
            # JA[2350]: 平賀くん……。

    # ==== SCENE 289 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay7 +970 → ha 2 shy]
    $ show_sprites(("ha 2 shy"))
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1", "ha 2 shy"))
    play music t19 fadein 1.0
    # [BG +43 → id(43)]
    $ fade_fx("id(43)")
    # [lay5 hide]
    $ show_sprites(("ha 2 shy"))
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "ha 2 shy"))
    voice "ch5.2_l_005"
    l "Fine, there's no stopping you. I'm coming too."
    # JA[6196]: もう、しょうがないわね。 / わたしもついていくわよ。
    # [lay7 hide]
    $ show_sprites(("l 1"))
    # [lay6 +676 → k 1]
    $ show_sprites(("l 1", "k 1"))
    voice "ch5.2_k_006"
    k "If Louise insists on coming, then I suppose I have to come along as well."
    # JA[3251]: ルイズがついていくって言うなら、 / わたしもついていかないとね。
    # [lay1 hide]
    $ show_sprites(("k 1"))
    # [lay0 +588 → t 1]
    $ show_sprites(("t 1", "k 1"))
    th "…….{#ch5_2_th_004}"
    # JA: ……。
    # [lay6 hide]
    $ show_sprites(("t 1"))
    # [lay0 hide]
    $ show_sprites()
    # [lay3 +852 → m 1]
    $ show_sprites(("m 1"))
    # [lay4 +561 → g 1 sad]
    $ show_sprites(("m 1", "g 1 sad"))
    voice "ch5.2_m_003"
    m "…What about us? Guiche?"
    # JA[4075]: ……わたし達はどうするの？ / ギーシュ？
    # [lay4 +570 → g 2 angry]
    $ show_sprites(("m 1", "g 2 angry"))
    voice "ch5.2_g_001"
    g "…W-we're going, of course. What else would we do? Montmorency."
    # JA[1508]: ……い、行くさ。 / 行くに決まってるだろう？ / モンモランシー。
    # [lay3 hide]
    $ show_sprites(("g 2 angry"))
    # [lay4 hide]
    $ show_sprites()
    # [lay2 +506 → si 2 sad]
    $ show_sprites(("si 2 sad"))
    voice "ch5.2_si_005"
    si "W-what should I do?"
    # JA[14776]: わ、わたしはどうしましょう？
    # [lay2 x=-96]
    # [lay5 +390 → s 1]
    $ show_sprites(("si 2 sad", "s 1"))
    voice "ch5.2_s_011"
    s "Hmm, I can't leave you alone in your room either. Let's all go, then."
    # JA[11627]: うーん、部屋で１人ってわけにもいかないし、 / みんなで行こうか。
    # [lay2 +500 → si 2]
    $ show_sprites(("si 2", "s 1"))
    voice "ch5.2_si_006"
    si "Yes, Saito-san.{#ch5_2_v14777}"
    # JA[14777]: はい、サイトさん。
    # [lay2 hide]
    $ show_sprites(("s 1"))
    # [lay5 hide]
    $ show_sprites()
    # [lay7 +963 → ha 2]
    $ show_sprites(("ha 2"))
    voice "ch5.2_ha_009"
    ha "Everyone. Thank you."
    # JA[2351]: みなさん。 / ありがとうございます。
    # [lay7 hide]
    $ show_sprites()
    # [lay7 +962 → ha 2]
    $ show_sprites(("ha 2"))
    # [lay1 +310 → l 1 shy]
    $ show_sprites(("l 1 shy", "ha 2"))
    voice "ch5.2_l_006"
    l "B-but it's not for Haruna's sake, you know. I just want this whole troublesome business settled quickly."
    # JA[6197]: べ、べつにハルナのためじゃないんだからね。 / 面倒なことは早く済ませたいだけよ。
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay1 hide]
    $ show_sprites(("ha 2"))
    # [lay7 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")

    # ==== SCENE 290 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +52 → id(52)]
    $ fade_fx("id(52)", new_music="t27")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1"))
    voice "ch5.2_s_012"
    s "Now that we're at the theater, what do we do?"
    # JA[11628]: さて、劇場の前に来たわけだけど、どうしよう？
    # [lay5 x=224]
    # [lay6 +676 → k 1]
    $ show_sprites(("k 1", "s 1"))
    voice "ch5.2_k_007"
    k "Let's go in through the front. You're not planning to do anything guilty, are you?"
    # JA[3252]: 正面から行きましょう。 / 別にやましいことをするわけじゃないん / でしょ？
    th "That's true, but I don't think the door will open…{#ch5_2_th_005}"
    # JA: （そりゃそうなんだけど、 / 　鍵が開かないと思うんだけど……）

    # ---- 【選択肢】 ----
    menu:
        "Ask Kirche.":
            # JA: キュルケに相談する
            # ==== SCENE 291 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1"))
            # [lay6 +676 → k 1]
            $ show_sprites(("k 1", "s 1"))
            play music t27 fadein 1.0
            # [BG +52 → id(52)]
            $ fade_fx("id(52)")
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("k 1", "s 3 sad"))
            voice "ch5.2_s_013"
            s "Kirche, what about the lock? It's obvious what we're after, right?"
            # JA[11629]: キュルケ、鍵はどうする？ / 当然かかってるよな。
            # [lay6 +678 → k 1 happy]
            $ show_sprites(("k 1 happy", "s 3 sad"))
            voice "ch5.2_k_008"
            k "Obviously we open it with unlocking magic."
            # JA[3253]: 開錠の魔法で開けるに決まってるじゃない。
            $ update_sympathy(10, char_key="kirche")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("k 1 happy", "s 1 sad"))
            voice "ch5.2_s_014"
            s "…….{#ch5_2_v11630}"
            # JA[11630]: ……。
            # [lay5 hide]
            $ show_sprites(("k 1 happy"))
            # [lay4 +561 → g 1 sad]
            $ show_sprites(("k 1 happy", "g 1 sad"))
            voice "ch5.2_g_002"
            g "But doesn't that make it breaking and entering?"
            # JA[1509]: それって、不法侵入になるんじゃないのか？
            # [lay6 +676 → k 1]
            $ show_sprites(("k 1", "g 1 sad"))
            voice "ch5.2_k_009"
            k "We're not here to rob anything, so don't nitpick."
            # JA[3254]: 別に物取りってわけじゃないんだから、 / 細かいことは言わないの。
            # [lay4 hide]
            $ show_sprites(("k 1"))
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("k 1", "s 3 sad"))
            voice "ch5.2_s_015"
            s "Well, actually, in a sense we are here to take something."
            # JA[11631]: いや、ある意味物取りに来たわけなんだけど。
            # [lay6 hide]
            $ show_sprites(("s 3 sad"))
            # [lay5 hide]
            $ show_sprites()
        "Give it up.":
            # JA: あきらめる
            # ==== SCENE 292 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +390 → s 1]
            $ show_sprites(("s 1"))
            # [lay6 +676 → k 1]
            $ show_sprites(("k 1", "s 1"))
            play music t27 fadein 1.0
            # [BG +52 → id(52)]
            $ fade_fx("id(52)")
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("k 1", "s 3 sad"))
            voice "ch5.2_s_016"
            s "Haruna. How about we give up for today?"
            # JA[11632]: 春奈。 / 今日はあきらめるってどうだ？
            # [lay6 hide]
            $ show_sprites(("s 3 sad"))
            # [lay7 +968 → ha 2 sad]
            $ show_sprites(("ha 2 sad", "s 3 sad"))
            voice "ch5.2_ha_010"
            ha "Hiraga-kun, that's cruel. I know it's dangerous, but we can't just give up that easily…"
            # JA[2352]: 平賀くん、ひどいよ。 / 確かに危険なのは分かるけど、 / 簡単にあきらめられるはずがない……。
            $ update_sympathy(-10, char_key="haruna")
            # [TNDL       tndl(30)] — не переносится (система не реализована, AGENTS §6)
            # [lay7 hide]
            $ show_sprites(("s 3 sad"))
            # [lay6 +678 → k 1 happy]
            $ show_sprites(("k 1 happy", "s 3 sad"))
            voice "ch5.2_k_010"
            k "Oh, my darling. I'll open it with unlocking magic for you."
            # JA[3255]: もう、ダーリン。 / 開錠の魔法で開けてあげるわ。
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("k 1 happy", "s 1 sad"))
            voice "ch5.2_s_017"
            s "No, that's illegal…"
            # JA[11633]: いや、それって違法……。
            # [lay6 +676 → k 1]
            $ show_sprites(("k 1", "s 1 sad"))
            voice "ch5.2_k_011"
            k "Everything turns out all right in the end."
            # JA[3256]: なるようになるわよ。
            # [lay6 hide]
            $ show_sprites(("s 1 sad"))
            # [lay5 hide]
            $ show_sprites()
        "Break the door down.":
            # JA: 扉を破壊する
            # ==== SCENE 293 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay6 +676 → k 1]
            $ show_sprites(("k 1"))
            # [lay5 +390 → s 1]
            $ show_sprites(("k 1", "s 1"))
            play music t27 fadein 1.0
            # [BG +52 → id(52)]
            $ fade_fx("id(52)")
            # [lay5 +390 → s 1]
            voice "ch5.2_s_018"
            s "Derf. Can you smash that door down?"
            # JA[11634]: デルフ。 / あの扉、ぶちやぶれるか？
            # [lay19 +942 → d 1 happy]
            $ show_sprites(("k 1", "d 1 happy", "s 1"))
            voice "ch5.2_d_001"
            d "Well, I'd say we can manage it somehow. It all depends on my partner's arm, I suppose."
            # JA[1306]: まぁ、なんとかなるんじゃねーの？ / 相棒の腕次第だろうけどな。
            # [lay19 hide]
            $ show_sprites(("k 1", "s 1"))
            # [lay5 hide]
            $ show_sprites(("k 1"))
            # [lay6 hide]
            $ show_sprites()
            # [lay1 +302 → l 1]
            $ show_sprites(("l 1"))
            voice "ch5.2_l_007"
            l "…We don't have to do that. We can just open it with unlocking magic, can't we?"
            # JA[6198]: ……そんなことしなくてもいいわ。 / 開錠の魔法で開ければいいんでしょ？
            # [lay1 x=-96]
            # [lay3 +852 → m 1]
            $ show_sprites(("l 1", "m 1"))
            voice "ch5.2_m_004"
            m "Oh? Can Louise use unlocking magic now?"
            # JA[4076]: あら、ルイズって開錠の魔法を使えたのかしら？
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry", "m 1"))
            voice "ch5.2_l_008"
            l "I can use it now!"
            # JA[6199]: 使えるようになったの！
            # [lay3 hide]
            $ show_sprites(("l 1 angry"))
            # [lay6 +678 → k 1 happy]
            $ show_sprites(("l 1 angry", "k 1 happy"))
            voice "ch5.2_k_012"
            k "Now, now. With Zero Louise, you'd only break the door down. I'll open it for you."
            # JA[3257]: まぁまぁ。 / ゼロのルイズじゃ、扉を破壊しそうだから、 / わたしが開けてあげるわ。
            # [lay1 +308 → l 1 sad]
            $ show_sprites(("l 1 sad", "k 1 happy"))
            voice "ch5.2_l_009"
            l "…….{#ch5_2_v6200}"
            # JA[6200]: ……。
            # [lay1 hide]
            $ show_sprites(("k 1 happy"))
            # [lay6 hide]
            $ show_sprites()

    # ==== SCENE 294 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    play music t27 fadein 1.0
    # [BG +52 → id(52)]
    $ fade_fx("id(52)")
    # [lay0 +593 → t 1 angry]
    $ show_sprites(("t 1 angry"))
    voice "ch5.2_t_001"
    t "…Quietly."
    # JA[15575]: ……静かに。
    # [lay0 hide]
    $ show_sprites()
    # [lay6 +678 → k 1 happy]
    $ show_sprites(("k 1 happy"))
    voice "ch5.2_k_013"
    k "Yes, yes. Opening, one moment."
    # JA[3258]: はいはい。 / 開錠っと。
    # [lay6 x=-96]
    # [lay5 +425 → s 3 happy]
    $ show_sprites(("k 1 happy", "s 3 happy"))
    voice "ch5.2_s_019"
    s "Thanks! Kirche…"
    # JA[11635]: サンキュ！ / キュルケ……。
    # [lay6 hide]
    $ show_sprites(("s 3 happy"))
    # [lay5 hide]
    $ show_sprites()
    # [lay1 +309 → l 1 sad]
    $ show_sprites(("l 1 sad"))
    voice "ch5.2_l_010"
    l "Mmph, I could do that much too…"
    # JA[6201]: むぅ、わたしだってそれぐらい……。
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay1 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")

    # ==== SCENE 295 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay1 +303 → l 1]
    $ show_sprites(("l 1"))
    play music t22 fadein 1.0
    voice "ch5.2_l_011"
    l "The stage is still lit. And I can hear voices."
    # JA[6202]: 舞台は明かりがついたままよ。 / それに声が聞こえるわ。
    voice "ch5.2_w_001"
    w "…Ah, my beloved. How greatly I have loved you."
    # JA[15896]: ……ああ、愛しい人よ。 / 僕がどれほどきみを愛したことか。
    # [lay1 hide]
    $ show_sprites()
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1"))
    # [lay5 +390 → s 1]
    $ show_sprites(("l 1", "s 1"))
    th "Are they rehearsing a play?{#ch5_2_th_006}"
    # JA: （芝居の練習をしてるのか？）
    # [lay20 hide]
    # [lay5 hide]
    $ show_sprites(("l 1"))
    # [lay1 hide]
    $ show_sprites()
    # [BG hide] — поглощается переходом на CG
    # [EVENT_CG +131 → id(131)]
    $ fade_fx("id(131)", type="cg")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    voice "ch5.2_w_002"
    w "…Love blinds and maddens everyone. The noblemen who whispered love in your ear all tried to answer your riddle, and every one of them was ruined."
    # JA[15897]: ……愛は誰もを盲目にし狂わせる。 / きみに愛を囁いた貴公子達は、きみの謎かけに / 答えようとしてみな破滅していった。
    voice "ch5.2_w_003"
    w "But I will never laugh at that folly again. …Because I myself staked this kingdom on you, and ruined it!"
    # JA[15898]: だが、僕はもうその愚を笑うことはすまい。 / ……僕自身もきみのためにこの王国を賭け、 / そして滅ぼしたからだ！
    voice "ch5.2_w_004"
    w "…Now, the castle falls. Depart."
    # JA[15899]: ……さあ、城が落ちる。 / 去りたまえ。
    voice "ch5.2_w_005"
    w "Those rebel soldiers will welcome you as the new queen with cries of joy!"
    # JA[15900]: あの寄せ手の兵どもは、きみを新しい女王 / として歓喜の声で迎えるだろう！
    voice "ch5.2_w_006"
    w "…Ah, my beloved. But there will be no regret."
    # JA[15901]: ……ああ愛しい人。 / だが、後悔はすまい。
    voice "ch5.2_w_007"
    w "My love for you was worth that much. Only, if I could… just once…"
    # JA[15902]: きみへの愛にはそれだけの価値があった。 / ただ、願わくば……ただ一度……。
    voice "ch5.2_w_008"
    w "The words of love on your lips…"
    # JA[15903]: あなたの口唇に愛の言葉を……。
    # [SET        set("se0", {play = (0x03000000 +55)})] — SE не портируется
    voice "ch5.2_s_020"
    s "…Oops, busted."
    # JA[11636]: ……うわっ、しまった。
    # [EVENT_CG +132 → id(132)]
    $ fade_fx("id(132)", type="cg")
    voice "ch5.2_w_009"
    w "Who is it! — Oh, you people, from this afternoon…"
    # JA[15904]: 誰だ！ / って、きみ達は昼間の……。
    voice "ch5.2_ha_011"
    ha "I-I're sorry. We didn't mean to peek…"
    # JA[2353]: ご、ごめんなさい。 / 覗くつもりは……。
    # [lay20 hide]
    # [lay5 hide]
    # [lay7 hide]
    # [BG hide]
    $ fade_fx("black")
    # [EVENT_CG hide] — поглощается переходом на фон
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("w 1 angry"))
    voice "ch5.2_w_010"
    w "It seems you had no intention of peeking, but how do you mean to apologize for having sneaked in?"
    # JA[15905]: 覗くつもりはないようだが、 / 忍び込んできたことについては / どう謝罪するつもりなんだ？
    # [lay20 x=-96]
    # [lay7 +966 → ha 2 angry]
    $ show_sprites(("w 1 angry", "ha 2 angry"))
    voice "ch5.2_ha_012"
    ha "Um, it isn't Miss Louise and the others' fault. I insisted on it. I had business with Weatherby-san…"
    # JA[2354]: あの、ルイズさん達が悪いのではありません。 / 私が無理やりお願いしたんです。 / ウェザリーさんに用があったので……。
    voice "ch5.2_w_011"
    w "I see. I wouldn't think a matter urgent enough to put on a show of thieving, but what is it you need at this late hour?"
    # JA[15906]: なるほど、盗賊の真似事をするほどの / 緊急の用事があるとは思えませんが、 / こんな夜更けに何の御用で？

    # ---- 【選択肢】 ----
    menu:
        "We came to talk about it again.":
            # JA: もう一度相談に来た
            # ==== SCENE 296 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay7 +966 → ha 2 angry]
            $ show_sprites(("w 1 angry", "ha 2 angry"))
            play music t22 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay7 hide]
            $ show_sprites(("w 1 angry"))
            # [lay5 +390 → s 1]
            $ show_sprites(("w 1 angry", "s 1"))
            voice "ch5.2_s_021"
            s "We came to talk about the bag again."
            # JA[11637]: バッグの件でもう一度相談に来たんだ。
            # [lay20 +1067 → w 1 sad]
            $ show_sprites(("w 1 sad", "s 1"))
            voice "ch5.2_w_012"
            w "You people never learn, do you."
            # JA[15907]: きみ達も懲りないな。
        "W-we came looking for something we lost.{#ch5_2_c297}":
            # JA: わ、忘れ物を捜しに来た
            # ==== SCENE 297 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay7 +966 → ha 2 angry]
            $ show_sprites(("w 1 angry", "ha 2 angry"))
            play music t22 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay7 hide]
            $ show_sprites(("w 1 angry"))
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("w 1 angry", "s 1 sad"))
            voice "ch5.2_s_022"
            s "W-we came looking for something we lost.{#ch5_2_v11638}"
            # JA[11638]: わ、忘れ物を捜しに来た。
            # [lay20 +1067 → w 1 sad]
            $ show_sprites(("w 1 sad", "s 1 sad"))
            voice "ch5.2_w_013"
            w "…Something you lost…?"
            # JA[15908]: ……忘れ物……ね？
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1", "s 1 sad"))
            voice "ch5.2_w_014"
            w "If you happen to mean that bag, you couldn't be more off target…"
            # JA[15909]: まさか、あのバッグのことを / 言ってるんだったら、お門違いも / いいところなんだけど……。
        "S-stay silent.":
            # JA: も、黙秘する
            # ==== SCENE 298 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay7 +966 → ha 2 angry]
            $ show_sprites(("w 1 angry", "ha 2 angry"))
            play music t22 fadein 1.0
            # [BG +54 → id(54)]
            $ fade_fx("id(54)")
            # [lay7 hide]
            $ show_sprites(("w 1 angry"))
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("w 1 angry", "s 1 angry"))
            voice "ch5.2_s_023"
            s "…S-stay silent!"
            # JA[11639]: ……も、黙秘する！
            # [lay20 +1065 → w 1 angry]
            voice "ch5.2_w_015"
            w "I see. Then it's confinement, is it."
            # JA[15910]: そうか、じゃあ監禁だな。
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("w 1 angry", "s 3 sad"))
            voice "ch5.2_s_024"
            s "C-confinement? Is there such a thing in a theater?"
            # JA[11640]: か、監禁？ / そんなのが劇場にあるのかよ。
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1", "s 3 sad"))
            voice "ch5.2_w_016"
            w "…I'm joking."
            # JA[15911]: ……冗談よ。

    # ==== SCENE 299 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay20 +1067 → w 1 sad]
    $ show_sprites(("w 1 sad"))
    # [lay5 +390 → s 1]
    $ show_sprites(("w 1 sad", "s 1"))
    play music t22 fadein 1.0
    # [BG +54 → id(54)]
    $ fade_fx("id(54)")
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("w 1 angry", "s 1"))
    voice "ch5.2_w_017"
    w "I told you this afternoon, didn't I? That bag is mine."
    # JA[15912]: 昼も言ったはずだ。 / このバッグについてはわたしのものだと。
    # [lay5 hide]
    $ show_sprites(("w 1 angry"))
    # [lay7 +966 → ha 2 angry]
    $ show_sprites(("w 1 angry", "ha 2 angry"))
    voice "ch5.2_ha_013"
    ha "Weatherby-san. Could you show us the bag, just for a moment? It would prove that it's mine."
    # JA[2355]: ウェザリーさん。 / バッグを少しだけ、見せてくれませんか？ / 私のものだと証明できます。
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1", "ha 2 angry"))
    voice "ch5.2_w_018"
    w "Hm? That's interesting. If you're that certain, I could show it to you."
    # JA[15913]: ふーん？ / それは面白い。 / そこまで言い切るのなら見せてあげてもいい。
    # [lay20 +1067 → w 1 sad]
    $ show_sprites(("w 1 sad", "ha 2 angry"))
    voice "ch5.2_w_019"
    w "But…{#ch5_2_v15914}"
    # JA[15914]: ただし……。
    # [lay7 hide]
    $ show_sprites(("w 1 sad"))
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("w 1 sad", "s 1 sad"))
    voice "ch5.2_s_025"
    s "But?{#ch5_2_v11641}"
    # JA[11641]: ただし？
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1", "s 1 sad"))
    voice "ch5.2_w_020"
    w "It's not… free, you know? That's what negotiation is."
    # JA[15915]: タダ…というわけには行かないだろ？ / それが交渉ってもんだ。
    # [lay20 hide]
    $ show_sprites(("s 1 sad"))
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "s 1 sad"))
    voice "ch5.2_l_012"
    l "It's only to show it to us — why are you acting so proud? It's not as if you were giving the bag away."
    # JA[6203]: 見せるだけなのになんで、 / そんなにえらそうなのよ。 / いいじゃないバッグを見せてくれるくらい。
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("l 1 angry", "s 1 angry"))
    voice "ch5.2_s_026"
    s "D-don't be ridiculous, don't get excited. Louise, this is where you bow your head, you know?"
    # JA[11642]: バ、バカ、興奮するんじゃねーよ。 / ルイズ、ここは頭を下げるところだろ？
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "s 1 angry"))
    voice "ch5.2_l_013"
    l "But…{#ch5_2_v6204}"
    # JA[6204]: だって……。
    # [lay1 hide]
    $ show_sprites(("s 1 angry"))
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1", "s 1 angry"))
    voice "ch5.2_w_021"
    w "Then let's do this. One condition!"
    # JA[15916]: なら、こうしよう。 / ひとつ条件がある！
    # [lay5 +390 → s 1]
    $ show_sprites(("w 1", "s 1"))
    voice "ch5.2_s_027"
    s "A condition?"
    # JA[11643]: 条件？
    voice "ch5.2_w_022"
    w "It's simple. I want you to help me on stage. The content is the piece you saw earlier."
    # JA[15917]: 簡単なことだ。 / キミ達に舞台の手伝いをしてほしい。 / 内容はさっきの演目だ。
    voice "ch5.2_w_023"
    w "Watching you, I was struck by inspiration. If so, I can show you the bag."
    # JA[15918]: キミ達を見て、インスピレーションが / ひらめいた。 / それなら、バッグを見せてやってもいい。
    # [lay5 hide]
    $ show_sprites(("w 1"))
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("w 1", "l 1 angry"))
    voice "ch5.2_l_014"
    l "W-what are you saying? We're nobility. There's no way we could do that."
    # JA[6205]: な、何言ってるの？ / 貴族なのよ、わたし達。 / そんなことできるはずないでしょ？
    # [lay1 hide]
    $ show_sprites(("w 1"))
    # [lay7 +966 → ha 2 angry]
    $ show_sprites(("w 1", "ha 2 angry"))
    voice "ch5.2_ha_014"
    ha "I'll do it."
    # JA[2356]: やります。
    voice "ch5.2_w_024"
    w "Ho."
    # JA[15919]: ほぅ。
    voice "ch5.2_ha_015"
    ha "So if we help, you'll show us the bag. I'll do it. Please let me."
    # JA[2357]: 手伝いをすればバッグを見せてくれるんですね。 / やります。 / やらせてください。
    # [lay7 hide]
    $ show_sprites(("w 1"))
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("w 1", "s 3 sad"))
    voice "ch5.2_s_028"
    s "Haruna…"
    # JA[11644]: 春奈……。
    # [lay20 hide]
    $ show_sprites(("s 3 sad"))
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "s 3 sad"))
    voice "ch5.2_l_015"
    l "Hey, don't drag people into this on your own!"
    # JA[6206]: ちょっと、勝手に人を巻き込まないでよ！
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("l 1 angry", "s 1 sad"))
    voice "ch5.2_s_029"
    s "Louise, I'm asking you too. It's the only way."
    # JA[11645]: ルイズ、俺からも頼む。 / これしかないんだ。
    # [lay1 hide]
    $ show_sprites(("s 1 sad"))
    # [lay6 +676 → k 1]
    $ show_sprites(("k 1", "s 1 sad"))
    voice "ch5.2_k_014"
    k "Well, if my darling says so, I suppose it's fine…"
    # JA[3259]: まぁ、ダーリンがそういうなら、 / わたしはいいけど……。
    # [lay5 hide]
    $ show_sprites(("k 1"))
    # [lay0 +588 → t 1]
    $ show_sprites(("k 1", "t 1"))
    voice "ch5.2_t_002"
    t "Same as the one on the right."
    # JA[15576]: 右に同じ。
    # [lay0 hide]
    $ show_sprites(("k 1"))
    # [lay6 hide]
    $ show_sprites()
    # [lay1 +307 → l 1 angry]
    $ show_sprites(("l 1 angry"))
    voice "ch5.2_l_016"
    l "Fine, do as you please!"
    # JA[6207]: もう、勝手にしなさい！
    # [lay1 hide]
    $ show_sprites()
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1"))
    voice "ch5.2_w_025"
    w "Then we have a deal."
    # JA[15920]: なら、交渉成立だ。
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("w 1 angry"))
    voice "ch5.2_w_026"
    w "By the way, I used to have a noble title. I won't let you say you can't do it."
    # JA[15921]: ちなみにわたしは過去、貴族の名を / 持っていた者だ。 / できないとは言わせないぞ。
    # [lay20 x=-96]
    # [lay7 +962 → ha 2]
    $ show_sprites(("w 1 angry", "ha 2"))
    voice "ch5.2_ha_016"
    ha "The piece from earlier…"
    # JA[2358]: さっきの演目……。
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1", "ha 2"))
    voice "ch5.2_w_027"
    w "I'd put it together as the title of the next play, 'The Twin-Moon Maiden'."
    # JA[15922]: 『双月天女』っていう、次のお芝居の演目として / まとめていたものだ。
    voice "ch5.2_w_028"
    w "…A story of a country, of a princess buffeted by fate and the noblemen who fell in love with her and were ruined."
    # JA[15923]: ……運命に翻弄される王族の少女と、 / 彼女に恋をし破滅していく貴公子達との / 国家の物語。
    voice "ch5.2_w_029"
    w "Wouldn't that suit the times we live in?"
    # JA[15924]: こんなご時世にお似合いでしょう？
    # [lay7 hide]
    $ show_sprites(("w 1"))
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("w 1", "l 1 angry"))
    voice "ch5.2_l_017"
    l "How improper."
    # JA[6208]: 不謹慎だわ。
    # [lay20 +1067 → w 1 sad]
    $ show_sprites(("w 1 sad", "l 1 angry"))
    voice "ch5.2_w_030"
    w "…Improper? Nobility throwing away their station to live for their own love. There's no subject that would catch the crowd's interest like that."
    # JA[15925]: ……不謹慎？ / 貴族が身分を捨てて己の恋に生きる。 / これほど民衆の興味を引ける題材もないだろ？
    # [lay1 hide]
    $ show_sprites(("w 1 sad"))
    # [lay5 +390 → s 1]
    $ show_sprites(("w 1 sad", "s 1"))
    voice "ch5.2_s_030"
    s "…By the way, when you say help on stage, do you mean carrying the props and such?"
    # JA[11646]: ……ところで、舞台の手伝いって / 大道具とかをすればいいのか？
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1", "s 1"))
    voice "ch5.2_w_031"
    w "No, I want you to stand on the stage as actors as well."
    # JA[15926]: いや、役者としても舞台に立ってもらう。
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("w 1", "s 3 sad"))
    voice "ch5.2_s_031"
    s "…What!"
    # JA[11647]: ……えっ！
    # [lay5 hide]
    $ show_sprites(("w 1"))
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("w 1", "l 1 sad"))
    voice "ch5.2_l_018"
    l "…Hey, wait!"
    # JA[6209]: ……え、ちょっと！
    th "Whoa, whoa… This is getting out of hand. Can we even manage a stage, for crying out loud?{#ch5_2_th_007}"
    # JA: （おいおい……。 / 　なんだかとんでもないことになったぞ。 / 　できるのか、舞台なんて）
    # [lay1 hide]
    $ show_sprites(("w 1"))
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("w 1", "ha 2 sad"))
    th "…….{#ch5_2_th_008}"
    # JA: ……。
    # [lay7 +962 → ha 2]
    $ show_sprites(("w 1", "ha 2"))
    voice "ch5.2_ha_017"
    ha "…Um, Weatherby-san? Have we met somewhere before?"
    # JA[2359]: ……あの、ウェザリーさん？ / どこかでお会いしたことありませんか？
    voice "ch5.2_w_032"
    w "This is the actor's life, you know. Perhaps you've seen me before?"
    # JA[15927]: こういう役者商売だからね。 / 見かけたこともあるんじゃない？
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("w 1", "ha 2 sad"))
    voice "ch5.2_ha_018"
    ha "So… it seems."
    # JA[2360]: そう……、ですか。
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay20 hide]
    $ show_sprites(("ha 2 sad"))
    # [lay7 hide]
    $ show_sprites()
    # [lay5 hide]
    # [BG hide]
    $ fade_fx("black")

    # [移動] → next(300): сцена 300 — часть 3 главы 5
    jump ch5_3
    return
