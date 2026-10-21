# Глава 5, часть 1 (сцены 269–284): переезд в городской дом, начало
# расследования бомбиста, погоня за похитителем сумки Харуны и встреча
# с Уэзерби у городской оперы.
# Источник: ps2_source/chapters/chapter_06_本当の想い.txt (SCENE 269–284).
# Точные аргументы: ps2_source/events_full/chapter_06_本当の想い.txt.
# Скелет собран генератором tools/gen_ch5_1_script.py (EN — tools/ch5_1_en.py,
#   RU — tools/ch5_1_ru.py), поэтому порядок реплик, голоса, спрайты и
#   события совпадают с источником дословно.
#
# Титульная карточка: K=11 (10 занят script-ch4_4.rpy). Вход — jump ch5
#   из главы 4; выход — jump ch5_2 (сцена 285) — E7 «forward debt»,
#   закроется частью 2.
#
# Голоса: ch5_<spk>_<NNN> — новая группа части 1, нумерация с 001 по
#   говорящему, порядок порта (269 → 270 → 271–273 → 274 → 275 → 276–278 →
#   279 → 280 → 281–283 → 284):
#   s ×32, l ×28, ha ×28, si ×6, w ×9, d ×3, k ×7, g ×2, t ×2, m ×1 —
#   всего 118. Мысли (th, без голоса) — 16, пункты меню — 9.
#
# Не портируются: battle() (система боя не подключена — прецедент ch2_3,
#   ch3_7, ch4_6), item() (инвентарь не реализован), TNDL, SE (se0 +67/+69,
#   se1 stop), waitAction/waitTime/waitSEStop, msgon/msgoff, back(), beginSkip.
#   COFFEE → pause(1.0).
# Фоны/CG: id(41), id(50), id(129), id(130) — имена пусты в image_id_map
#   (заглушки, требуют решения человека); sky, overlay, white, cafe,
#   town_square, cafe_entrance, l_si_sleep — имена заполнены.
# Спрайты: id → имя по references/sprite_id_map.csv; PROVISIONAL (пиксель-
#   сверка недоступна — архив PS2 не подключён): 504 = si 2 angry,
#   506 = si 2 sad, 654 = t 7, 742 = k 7, 1061 = w 1, 1063 = w 1 happy,
#   1065 = w 1 angry, 1067 = w 1 sad.
#
# Меню 【選択肢】: три развилки по три варианта (сцены 270, 275, 280) —
#   варианты развёрнуты внутрь пунктов меню, слияние — общая сцена
#   (274 / 279 / 284), как в script-ch1_10.rpy и script-ch4_6.rpy.
#
# Файл сгенерирован tools/gen_ch5_1_script.py — правки вносить в него
#   и в tools/ch5_1_en.py, затем перегенерировать.


label ch5:
    # Титульный монтаж (BG 2/1145/1132/1145/2) → overlay_screen (образ «overlay»).
    call overlay_screen("overlay", "Chapter Five: 'True Feelings'", isUseBlur=False, text_mode="black") from _call_overlay_screen_11
    pause(2)

    # ==== SCENE 269 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [TITLE      title("本当の想い")] — титульная карточка → overlay_screen
    # [TNDL       tndl(null)] — не переносится (система не реализована, AGENTS §6)
    # [BG +2 — титульный монтаж → overlay_screen]
    # [TRANS   trans("crossfade", 500)] — переход выполняется fade_fx
    # [BG +1145 — титульный монтаж → overlay_screen]
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [BG +1132 — титульный монтаж → overlay_screen]
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [BG +1145 — титульный монтаж → overlay_screen]
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [BG +2 — титульный монтаж → overlay_screen]
    # [TRANS   trans("crossfade", 2000)] — переход выполняется fade_fx
    # [endSkip    endSkip()] — не портируется
    # [ITEM item("パン", 3)] — система инвентаря не реализована, вызов не переносится
    # [ITEM item("ハーブ", 3)] — система инвентаря не реализована, вызов не переносится
    # [ITEM item("エリクサー", 3)] — система инвентаря не реализована, вызов не переносится
    # [BG +88 → sky]
    $ fade_fx("sky", new_music="t4")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [SET        set("se0", {play = (0x03000000 +69)})] — SE не портируется
    th "After that, the three of us moved our base of operations to an inn in town, and spent the next several days getting ready to investigate the bomb user…{#ch5_th_001}"
    # JA: （あれから、街の宿に拠点を移した俺たちは、 / 　爆弾使いの調査の準備に数日追われることに / 　なった……）
    # [lay5 hide]
    th "Louise seems fired up, but… is she really okay?{#ch5_th_002}"
    # JA: （ルイズは張り切っているみたいだけど、 / 　大丈夫かなぁ……）
    voice "ch5_ha_001"
    ha "Mm, mm～! Nice weather!"
    # JA[2315]: ん、ん～～っ！ / いいお天気！
    voice "ch5_ha_002"
    ha "I hope today turns out well, too… I thought so, but… …Ugh, in the end, the three of us are sleeping together…"
    # JA[2316]: 今日も一日良い日でありますように。 / って思ったのに……。 / ……ううっ、結局３人で寝てる……。
    stop music fadeout 1.0
    # [LAYER white +2] → flash_fx("white")
    $ flash_fx("white")
    # [EVENT_CG +114 → l_si_sleep]
    $ fade_fx("l_si_sleep", type="cg", new_music="t29")
    # [TRANS   trans("crossfade", 0)] — переход выполняется fade_fx
    # [LAYER white hide] — вспышка гаснет (fade)
    voice "ch5_ha_003"
    ha "Louise and Siesta are both all over Hiraga-kun first thing in the morning too!"
    # JA[2317]: ルイズさんや、シエスタさんも、 / 朝から平賀くんにベタベタしちゃって！
    voice "ch5_ha_004"
    ha "…….{#ch5_v2318}"
    # JA[2318]: ……。
    voice "ch5_ha_005"
    ha "How envious… Maybe I should try to get in on it too."
    # JA[2319]: うらやましいなぁ…。 / 私も入ってみようかな。
    voice "ch5_ha_006"
    ha "First, let me just shift Siesta over a bit."
    # JA[2320]: まずはシエスタさんを横にずらしてっと。
    voice "ch5_si_001"
    si "…snore.{#ch5_v14766}"
    # JA[14766]: ……ぎろ。
    voice "ch5_ha_007"
    ha "O-oh, Siesta-san. Were you awake?"
    # JA[2321]: あ、あら、シエスタさん。 / 起きていたんですか？
    voice "ch5_si_002"
    si "Snoooore…{#ch5_v14767}"
    # JA[14767]: すーすーすー。
    voice "ch5_ha_008"
    ha "Ugh. Then Louise…"
    # JA[2322]: くっ。 / なら、ルイズさんを……。
    voice "ch5_l_001"
    l "…snore.{#ch5_v6164}"
    # JA[6164]: ……ぎろ。
    voice "ch5_ha_009"
    ha "Huh, Louise was awake too?"
    # JA[2323]: え、ルイズさんも起きてたんですか？
    voice "ch5_l_002"
    l "Snoooore…{#ch5_v6165}"
    # JA[6165]: すーすーすー。
    # [lay7 hide]
    # [lay2 hide]
    # [lay5 hide]
    # [lay1 hide]
    # [BG hide]
    $ fade_fx("black")
    # [EVENT_CG hide] — поглощается переходом на фон
    # [BG +41 → id(41)]
    $ fade_fx("id(41)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay7 +979 → ha 3 sad]
    $ show_sprites(("ha 3 sad"))
    voice "ch5_ha_010"
    ha "I-I'm not going to lose! Tomorrow I will definitely sleep next to Hiraga-kun! …if I can muster the courage."
    # JA[2324]: ま、負けないもん。 / 明日こそは平賀くんの隣に寝てみるんだから！ / ……勇気が出たらね。
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay7 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")

    # ==== SCENE 270 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +44 → cafe]
    $ fade_fx("cafe", new_music="t30")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1"))
    voice "ch5_l_003"
    l "The investigation starts today! I'll catch that newbie bomb user and show you all!"
    # JA[6166]: 今日からさっそく調査開始ね！ / あのにっくき爆弾使いを捕まえて / みせるんだから！
    # [lay1 +304 → l 1 happy]
    $ show_sprites(("l 1 happy"))
    voice "ch5_l_004"
    l "And I'll pay back the humiliation I suffered, twofold! Hee-hee, hee-hee-hee-hee…"
    # JA[6167]: そして、わたしが受けた屈辱を倍にして / 返してあげるわ！ / くくっ、くくくくくく……。
    # [lay1 x=-96]
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("l 1 happy", "s 3 sad"))
    voice "ch5_s_001"
    s "…Honestly, you do take on all the scut work."
    # JA[11585]: ……まったく、安請け合いなんかしやがって。
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "s 3 sad"))
    voice "ch5_l_005"
    l "W-what's that supposed to mean? That sour look on your face!"
    # JA[6168]: な、なによ。 / その不満そうな顔は！

    # ---- 【選択肢】 ----
    menu:
        "It's nothing, nothing at all.{#ch5_c271}":
            # JA: いえ、なんでもないです
            # ==== SCENE 271 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry", "s 3 sad"))
            play music t30 fadein 1.0
            # [BG +44 → cafe]
            $ fade_fx("cafe")
            # [lay5 +423 → s 3]
            $ show_sprites(("l 1 angry", "s 3"))
            voice "ch5_s_002"
            s "It's nothing, nothing at all.{#ch5_v11586}"
            # JA[11586]: いえ、なんでもないです。
            # [lay1 +306 → l 1 angry]
            voice "ch5_l_006"
            l "You're so evasive. If you're a man, say it plainly!"
            # JA[6169]: 煮え切らないわね。 / 男の子だったら、はっきり言いなさいよ！
            $ update_sympathy(-10, char_key="louise")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("l 1 angry", "s 1 angry"))
            voice "ch5_s_003"
            s "Fine, I'll say it!{#ch5_v11587}"
            # JA[11587]: なら、言ってやる。
            voice "ch5_s_004"
            s "Taking on the scut work is fine, but how exactly do you plan to track down that bomb user?!{#ch5_v11588}"
            # JA[11588]: 安請け合いするのはいいけど、 / どうやってあの爆弾使いを見つけだすつもり / なんだよ！
        "Let me tell you something, though.{#ch5_c272}":
            # JA: 言わせてもらいますけどね
            # ==== SCENE 272 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry", "s 3 sad"))
            play music t30 fadein 1.0
            # [BG +44 → cafe]
            $ fade_fx("cafe")
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("l 1 angry", "s 1 angry"))
            voice "ch5_s_005"
            s "Let me tell you something, though.{#ch5_v11589}"
            # JA[11589]: 言わせてもらいますけどね。
            voice "ch5_s_006"
            s "Taking on the scut work is fine, but how exactly do you plan to track down that bomb user?!{#ch5_v11590}"
            # JA[11590]: 安請け合いするのはいいけど、 / どうやってあの爆弾使いを見つけだすつもり / なんだよ！
        "I'm not making a sour face at all.{#ch5_c273}":
            # JA: 不満そうな顔なんてしてない
            # ==== SCENE 273 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("s 3 sad"))
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry", "s 3 sad"))
            play music t30 fadein 1.0
            # [BG +44 → cafe]
            $ fade_fx("cafe")
            voice "ch5_s_007"
            s "I'm not making a sour face at all.{#ch5_v11591}"
            # JA[11591]: 別に不満そうな顔なんてしてねーよ。
            # [lay1 +306 → l 1 angry]
            voice "ch5_l_007"
            l "That can't be. Say it plainly. You're a man, aren't you?"
            # JA[6170]: そんなはずないでしょ？ / はっきり言いなさい。 / 男の子でしょ？
            $ update_sympathy(-10, char_key="louise")
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            # [lay5 +394 → s 1 angry]
            $ show_sprites(("l 1 angry", "s 1 angry"))
            voice "ch5_s_008"
            s "Fine, I'll say it!{#ch5_v11592}"
            # JA[11592]: なら、言ってやる。
            voice "ch5_s_009"
            s "Taking on the scut work is fine, but how exactly do you plan to track down that bomb user?!{#ch5_v11593}"
            # JA[11593]: 安請け合いするのはいいけど、 / どうやってあの爆弾使いを見つけだすつもり / なんだよ！

    # ==== SCENE 274 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("s 1 angry"))
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "s 1 angry"))
    play music t30 fadein 1.0
    # [BG +44 → cafe]
    $ fade_fx("cafe")
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "s 1 angry"))
    voice "ch5_l_008"
    l "W-well… um… Obviously we'd go and catch them when the explosion happens!"
    # JA[6171]: そ、それは……えっと……。 / 爆発が起きたときに捕まえに行くに / 決まってるでしょ？
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("l 1 sad", "s 1 sad"))
    voice "ch5_s_010"
    s "…Wow, you really hadn't thought of anything at all?"
    # JA[11594]: ……はぁ、ホントになにも考えて / なかったのかよ。
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "s 1 sad"))
    voice "ch5_l_009"
    l "W-what's that?! Don't laugh at me!"
    # JA[6172]: な、なによ！ / バカにして。
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("l 1 angry", "s 1 angry"))
    voice "ch5_s_011"
    s "Nobody can catch them if they don't know when the explosion will happen, right? Think it through a little more."
    # JA[11595]: 爆発がいつ起こるのか分からないから、 / 誰も捕まえられないんだろ？ / もう少し考えろよ。
    voice "ch5_l_010"
    l "W-what do you mean?! Why don't you think it through yourself before you criticize!"
    # JA[6173]: な、なんですってぇっ！ / 文句を言う前に自分で考えたらどうなの！
    voice "ch5_s_012"
    s "W-what?! You're the one who took on the scut work, Louise!"
    # JA[11596]: な、なんだよ！ / 安請け合いしたのはルイズだろ？
    voice "ch5_l_011"
    l "Shut up, shut up!"
    # JA[6174]: うるさいうるさい！
    # [lay5 hide]
    $ show_sprites(("l 1 angry"))
    # [lay7 +966 → ha 2 angry]
    $ show_sprites(("l 1 angry", "ha 2 angry"))
    voice "ch5_ha_011"
    ha "H-hey, you two!"
    # JA[2325]: ちょ、ちょっと２人とも！
    # [lay1 hide]
    $ show_sprites(("ha 2 angry"))
    # [lay2 +504 → si 2 angry]
    $ show_sprites(("si 2 angry", "ha 2 angry"))
    voice "ch5_si_003"
    si "Fighting here won't get us anywhere."
    # JA[14768]: こんなところで喧嘩をしても何も / 始まりませんよ。
    # [lay2 hide]
    $ show_sprites(("ha 2 angry"))
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "ha 2 angry"))
    voice "ch5_l_012"
    l "I know, but… it's because of Saito…"
    # JA[6175]: そりゃそうだけど……。 / だって、サイトが……。
    # [lay7 hide]
    $ show_sprites(("l 1 sad"))
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("l 1 sad", "s 1 angry"))
    voice "ch5_s_013"
    s "Look around you. The ladies around here are perfectly calm, you know? Compare that with our master here…"
    # JA[11597]: ほら見ろ。 / 周りのご婦人方はいたって冷静ですよ？ / それに比べてウチのご主人様ときたら……。
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "s 1 angry"))
    voice "ch5_l_013"
    l "Shut up! Fine, I get it. I just have to think a bit more, right?"
    # JA[6176]: うるさい！ / 分かったわよ。 / もう少し考えればいいんでしょ？
    # [lay5 hide]
    $ show_sprites(("l 1 angry"))
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("l 1 angry", "ha 2 sad"))
    voice "ch5_ha_012"
    ha "…Phew. What's going to become of me… And Hiraga-kun is in this state too…"
    # JA[2326]: ……ふぅ。 / 私、どうなっちゃうんだろう……。 / 平賀くんもこの調子だし……。
    # [lay7 +966 → ha 2 angry]
    $ show_sprites(("l 1 angry", "ha 2 angry"))
    voice "ch5_ha_013"
    ha "U-um, that bag!"
    # JA[2327]: あ、あの鞄！
    # [lay7 hide]
    $ show_sprites(("l 1 angry"))
    # [lay2 +506 → si 2 sad]
    $ show_sprites(("l 1 angry", "si 2 sad"))
    voice "ch5_si_004"
    si "…Huh? Where are you going, Haruna-san?"
    # JA[14769]: ……えっ、ハルナさんどちらへ？
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "si 2 sad"))
    voice "ch5_l_014"
    l "W-wait! Haruna, what's wrong?"
    # JA[6177]: ちょ、ちょっと！ / ハルナ、どうしたの？
    voice "ch5_ha_014"
    ha "I'm sorry. I'll be right back!"
    # JA[2328]: ごめんなさい。 / すぐに戻ります！
    # [lay2 hide]
    $ show_sprites(("l 1"))
    # [lay1 hide]
    $ show_sprites()
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("s 1 angry"))
    voice "ch5_s_014"
    s "What's going on?"
    # JA[11598]: どうしたんだよ？
    # [lay5 x=224]
    # [lay2 +506 → si 2 sad]
    $ show_sprites(("si 2 sad", "s 1 angry"))
    voice "ch5_si_005"
    si "Yes. Miss Haruna suddenly ran off…"
    # JA[14770]: はい、ハルナさんが、いきなり走って行って / しまいまして……。
    # [lay2 hide]
    $ show_sprites(("s 1 angry"))
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "s 1 angry"))
    voice "ch5_l_015"
    l "Desertion? Fleeing in the face of the enemy is a serious crime, you know."
    # JA[6178]: もしかして、脱走？ / 敵前逃亡は重罪なのよ。
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("l 1 angry", "s 3 sad"))
    voice "ch5_s_015"
    s "Why does it have to be that…? Anyway, I'm going after her. Siesta, go back to the inn."
    # JA[11599]: なんで、そうなるんだよ……。 / とにかく、追いかけるぞ。 / シエスタは宿に戻ってて。
    # [lay1 hide]
    $ show_sprites(("s 3 sad"))
    # [lay5 hide]
    $ show_sprites()
    # [lay2 +506 → si 2 sad]
    $ show_sprites(("si 2 sad"))
    voice "ch5_si_006"
    si "Y-yes… Understood."
    # JA[14771]: は、はい……。 / 分かりました。
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay7 hide]
    # [lay2 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")

    # ==== SCENE 275 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +58 → town_square]
    $ fade_fx("town_square", new_music="t29")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("ha 2 sad"))
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("ha 2 sad", "s 1 sad"))
    voice "ch5_s_016"
    s "Finally caught up… …Haaah, haaah, what's wrong, Haruna?"
    # JA[11600]: やっと追いついた……。 / ……はぁはぁ、どうしたんだよ春奈？
    voice "ch5_ha_015"
    ha "Someone was carrying my bag!"
    # JA[2329]: わ、私のバッグを持っていた人がいたの！
    # [lay5 hide]
    $ show_sprites(("ha 2 sad"))
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("ha 2 sad", "l 1 angry"))
    voice "ch5_l_016"
    l "A bag? What about it?"
    # JA[6179]: バッグ？ / それがどうしたのよ？
    # [lay7 +966 → ha 2 angry]
    $ show_sprites(("ha 2 angry", "l 1 angry"))
    voice "ch5_ha_016"
    ha "It's not just any bag. …It's the only bag I brought with me when I came to this world!"
    # JA[2330]: ただのバッグじゃないの。 / ……私がこの世界に来たときに / 持ってきていた唯一のバッグなの！
    # [lay1 hide]
    $ show_sprites(("ha 2 angry"))
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("ha 2 angry", "s 1 angry"))
    voice "ch5_s_017"
    s "Could you get that out faster? Which way did they go?! The one who had your bag!"
    # JA[11601]: そ、それを早く言えよ。 / どっち行ったんだよ！ / そのバッグを持った奴って！
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("ha 2 sad", "s 1 angry"))
    voice "ch5_ha_017"
    ha "Um… th-that way!"
    # JA[2331]: ええと……。 / あ、あっちのほう！
    # [lay7 hide]
    $ show_sprites(("s 1 angry"))
    # [lay5 x=64]
    voice "ch5_s_018"
    s "W-wait! Haruna!"
    # JA[11602]: ま、待てって！ / 春奈っ！
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [BG +88 → sky]
    $ fade_fx("sky")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    th "……. ……. ….{#ch5_th_003}"
    # JA: ………。 / ……。 / …。
    # [BG hide]
    $ fade_fx("black")
    stop music fadeout 1.0
    # [BG +47 → cafe_entrance]
    $ fade_fx("cafe_entrance", new_music="t17")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("s 1 angry"))
    voice "ch5_s_019"
    s "D-damn it! Where'd they go?!"
    # JA[11603]: く、くそぅ！ / どこ行ったんだよ！
    # [lay5 x=224]
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "s 1 angry"))
    voice "ch5_l_017"
    l "…Wait a moment. Saito. Something's off here."
    # JA[6180]: ……ちょっと待って。 / サイト。 / 何か様子が変よ。
    # [lay19 +944 → d 1 angry]
    $ show_sprites(("l 1", "d 1 angry", "s 1 angry"))
    voice "ch5_d_001"
    d "…Hey, partner. Looks like we've got them surrounded."
    # JA[1303]: ……おい、相棒。 / こいつはどうも囲まれたみたいだぞ。
    # [lay5 hide]
    $ show_sprites(("l 1", "d 1 angry"))
    # [lay1 hide]
    $ show_sprites(("d 1 angry"))
    # [lay19 hide]
    $ show_sprites()
    # [lay11 +1105 → mage]
    $ show_sprites(("mage"))
    # [lay12 +1105 → mage]
    voice "ch5_l_018"
    l "Who are you people…? I don't suppose you'd answer if I asked, would you?"
    # JA[6181]: あなた達、何者っ……。 / って聞いて答えるとは思えないわね。
    voice "ch5_s_020"
    s "Damn! At a time like this…"
    # JA[11604]: ちくしょう！ / こんなときに……。

    # ---- 【選択肢】 ----
    menu:
        "Is Haruna all right?":
            # JA: 春奈は大丈夫か？
            # ==== SCENE 276 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay12 +1105 → mage]
            $ show_sprites(("mage"))
            # [lay11 +1105 → mage]
            play music t17 fadein 1.0
            # [BG +47 → cafe_entrance]
            $ fade_fx("cafe_entrance")
            th "They're probably the ones who were chasing Haruna. If they'd watched Haruna closely, this wouldn't have…{#ch5_th_004}"
            # JA: （たぶん、春奈を追いかけていた連中だよな。 / 　ちゃんと春奈のことを見ていれば、 / 　こんなことには……）
            th "Damn! She might be being attacked right now…{#ch5_th_005}"
            # JA: （くそっ！ / 　もしかしたら、春奈が襲われてる / 　かもしれないのに……）
        "Is Louise all right?":
            # JA: ルイズは大丈夫か？
            # ==== SCENE 277 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay12 +1105 → mage]
            $ show_sprites(("mage"))
            # [lay11 +1105 → mage]
            play music t17 fadein 1.0
            # [BG +47 → cafe_entrance]
            $ fade_fx("cafe_entrance")
            th "There are too many of them. Can Louise and I really manage on our own?{#ch5_th_006}"
            # JA: （相手が多すぎる。 / 　俺とルイズだけでなんとかなるのか？）
            th "Damn! She might be being attacked right now…{#ch5_th_007}"
            # JA: （くそっ！ / 　もしかしたら、春奈が襲われてる / 　かもしれないのに……）
        "Is Siesta all right?":
            # JA: シエスタは大丈夫か？
            # ==== SCENE 278 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay12 +1105 → mage]
            $ show_sprites(("mage"))
            # [lay11 +1105 → mage]
            play music t17 fadein 1.0
            # [BG +47 → cafe_entrance]
            $ fade_fx("cafe_entrance")
            th "Siesta is… I sent her back to the inn, so she should be fine, right?{#ch5_th_008}"
            # JA: （シエスタは……。 / 　宿に戻ってもらってるから、大丈夫だよな）
            th "Damn! She might be being attacked right now…{#ch5_th_009}"
            # JA: （くそっ！ / 　もしかしたら、春奈が襲われてる / 　かもしれないのに……）

    # ==== SCENE 279 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay12 +1105 → mage]
    $ show_sprites(("mage"))
    # [lay11 +1105 → mage]
    play music t17 fadein 1.0
    # [BG +47 → cafe_entrance]
    $ fade_fx("cafe_entrance")
    # [lay11 hide]
    # [lay12 hide]
    $ show_sprites()
    # [lay19 +940 → d 1]
    $ show_sprites(("d 1"))
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "d 1"))
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("l 1 angry", "d 1", "s 1 angry"))
    voice "ch5_d_002"
    d "Partner, there are too many of them. Wouldn't it be better to pull back for now?"
    # JA[1304]: 相棒、相手が多すぎる。 / 一度引き上げたほうが良くねーか？
    voice "ch5_d_003"
    d "And this is the city. We can't use flashy magic here."
    # JA[1305]: それに市街地だ。 / 派手に魔法は使えないぞ。
    voice "ch5_s_021"
    s "Like we could? Haruna might be being attacked right now!"
    # JA[11605]: そんなことできるはずねーだろ？ / 春奈が襲われてるかもしれないのに。
    th "What do I do…{#ch5_th_010}"
    # JA: （どうする……）
    # [lay1 hide]
    $ show_sprites(("d 1", "s 1 angry"))
    # [lay19 hide]
    $ show_sprites(("s 1 angry"))
    # [lay5 hide]
    $ show_sprites()
    # [BG hide] — поглощается переходом на CG
    # [EVENT_CG +130 → id(130)]
    $ fade_fx("id(130)", type="cg")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [SET        set("se0", {play = (0x03000000 +67)})] — SE не портируется
    th "The shadow just now…?{#ch5_th_011}"
    # JA: （い、いまの影は？）
    # [lay5 hide]
    # [BG hide]
    $ fade_fx("black")
    # [EVENT_CG hide]
    $ fade_fx("black")
    stop music fadeout 1.0
    # [EVENT_CG +129 → id(129)]
    $ fade_fx("id(129)", type="cg", new_music="t4")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [SET        set("se0", {play = (0x03000000 +67)})] — SE не портируется
    voice "ch5_k_001"
    unk_k "Oh-ho. It does look like something interesting is happening, doesn't it?"
    # JA[3239]: あーら。 / やっぱり、面白そうなことになってるじゃない！
    voice "ch5_l_019"
    l "Kirche! Tabitha! Montmorency!"
    # JA[6182]: キュルケ！ / タバサ！ / モンモランシー！
    voice "ch5_g_001"
    g "M-me too, I'm here!"
    # JA[1506]: ぼ、ぼくもいるぞ！
    voice "ch5_l_020"
    l "…Ah, Guiche is here too?"
    # JA[6183]: ……ああ、ギーシュもいたの？
    voice "ch5_g_002"
    g "Th-that treatment…"
    # JA[1507]: そ、その扱いは……。
    # [lay4 hide]
    # [lay1 hide]
    # [lay6 hide]
    # [EVENT_CG hide] — поглощается переходом на фон
    # [BG +47 → cafe_entrance]
    $ fade_fx("cafe_entrance")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad"))
    # [lay6 +676 → k 1]
    $ show_sprites(("l 1 sad", "k 1"))
    voice "ch5_k_002"
    k "Since you two weren't coming back to the academy, I figured you must have gotten involved in something interesting."
    # JA[3240]: あなた達がなかなか学院に戻ってこないから、 / 何か面白そうなことに、巻き込まれてるのに / 違いないって思ったんだけど。
    voice "ch5_k_003"
    k "Seems I hit the mark, then."
    # JA[3241]: ドンピシャだったみたいね。
    # [lay6 hide]
    $ show_sprites(("l 1 sad"))
    # [lay0 +588 → t 1]
    $ show_sprites(("l 1 sad", "t 1"))
    voice "ch5_t_001"
    t "Jackpot."
    # JA[15573]: 大当たり。
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "t 1"))
    voice "ch5_l_021"
    l "W-what do you mean, something interesting?! Don't act like it's none of your business!"
    # JA[6184]: お、面白そうなことってなによ！ / 他人事だと思って！
    # [lay0 hide]
    $ show_sprites(("l 1 angry"))
    # [lay6 +678 → k 1 happy]
    $ show_sprites(("l 1 angry", "k 1 happy"))
    voice "ch5_k_004"
    k "Yes, yes, I won't nag, I won't nag. It's not that Kirche the Ardent is offering to help, you know."
    # JA[3242]: はいはい、ぼやかないぼやかない。 / この微熱のキュルケがお手伝いして / あげようっていうんじゃない。
    # [lay6 +742 → k 7]
    $ show_sprites(("l 1 angry", "k 7"))
    voice "ch5_k_005"
    k "…Tabitha!"
    # JA[3243]: ……タバサ！
    # [lay1 hide]
    $ show_sprites(("k 7"))
    # [lay0 +654 → t 7]
    $ show_sprites(("t 7", "k 7"))
    voice "ch5_t_002"
    t "Watch this. Sylphid."
    # JA[15574]: いくよ。 / シルフィード。
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay6 hide]
    $ show_sprites(("t 7"))
    # [lay0 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [BATTLE battleInit battleInit((0x02000000 +47))] — система боя не реализована, вызов не переносится
    # [BATTLE battleAdd  battleAdd("サイト")] — система боя не реализована, вызов не переносится
    # [BATTLE battleAdd  battleAdd("ルイズ")] — система боя не реализована, вызов не переносится
    # [BATTLE battleAdd  battleAdd("キュルケ")] — система боя не реализована, вызов не переносится
    # [BATTLE battleAdd  battleAdd("タバサ")] — система боя не реализована, вызов не переносится
    # [BATTLE battleEnemy battleEnemy("左", "魔道士", (0x02000000 +1108))] — система боя не реализована, вызов не переносится
    # [BATTLE battleEnemy battleEnemy("右", "魔道士", (0x02000000 +1108))] — система боя не реализована, вызов не переносится
    # [BATTLE battle     battle()] — система боя не реализована, вызов не переносится

    # ==== SCENE 280 ====
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [BG +47 → cafe_entrance]
    $ fade_fx("cafe_entrance", new_music="t24")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry"))
    voice "ch5_l_022"
    l "Honestly, what is wrong with them! All of them!"
    # JA[6185]: まったく、なんだっていうのよ！ / 連中は！
    # [lay1 hide]
    $ show_sprites()
    # [lay6 +682 → k 1 sad]
    $ show_sprites(("k 1 sad"))
    voice "ch5_k_006"
    k "What happened, Darling? You've made quite a fuss, haven't you?"
    # JA[3244]: どうしたの、ダーリン。 / ずいぶん大事になってるみたいじゃない？
    # [lay6 x=-96]
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("k 1 sad", "s 1 angry"))
    voice "ch5_s_022"
    s "I'd love to explain it all, but… we don't have the time."
    # JA[11606]: 詳しく説明してあげたいのは山々なんだが……、 / 今は時間がないんだ。
    voice "ch5_s_023"
    s "We need to hurry ahead."
    # JA[11607]: 先を急ごう。
    # [lay6 +676 → k 1]
    $ show_sprites(("k 1", "s 1 angry"))
    voice "ch5_k_007"
    k "All right, Darling. But you'll have to tell me all about it later."
    # JA[3245]: 分かったわダーリン。 / その代わり、後でじっくり教えてもらうからね。
    stop music fadeout 1.0
    # [lay5 hide]
    $ show_sprites(("k 1"))
    # [lay6 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    th "……. ……. ….{#ch5_th_012}"
    # JA: ………。 / ……。 / …。
    # [BG +50 → id(50)]
    $ fade_fx("id(50)", new_music="t18")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay3 +852 → m 1]
    $ show_sprites(("m 1"))
    voice "ch5_m_001"
    m "Oh my, in front of the theater. This is the city opera house. Traveling troupes often perform here."
    # JA[4072]: あら、劇場の前ね。 / ここは市街歌劇場よ。 / よく旅回りの劇団が演劇をしてるわ。
    # [lay3 hide]
    $ show_sprites()
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("ha 2 sad"))
    voice "ch5_ha_018"
    ha "…….{#ch5_v2332}"
    # JA[2332]: ……。
    # [lay7 x=-96]
    # [lay5 +390 → s 1]
    $ show_sprites(("ha 2 sad", "s 1"))
    voice "ch5_s_024"
    s "There you are. Haruna! You were safe."
    # JA[11608]: いた。 / 春奈！ / 無事だったんだな。
    # [lay7 +968 → ha 2 sad]
    voice "ch5_ha_019"
    ha "H-Hiraga-kun…!"
    # JA[2333]: ひ、平賀くん……！
    # [lay5 hide]
    $ show_sprites(("ha 2 sad"))
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("ha 2 sad", "l 1 angry"))
    voice "ch5_l_023"
    l "That was quite a scare, wasn't it. I know what matters now, so don't just run off without warning."
    # JA[6186]: もう、大変だったんだからね。 / 大切なのは分かったから、 / いきなり走り出さないでよ。
    voice "ch5_ha_020"
    ha "I-I'm sorry…"
    # JA[2334]: ご、ごめんなさい……。
    # [lay1 hide]
    $ show_sprites(("ha 2 sad"))
    # [lay5 +394 → s 1 angry]
    $ show_sprites(("ha 2 sad", "s 1 angry"))
    voice "ch5_s_025"
    s "So, where did they go? The one with your bag."
    # JA[11609]: で、どこに行ったんだ？ / そのバッグを持った人。
    voice "ch5_ha_021"
    ha "The person with my bag went inside here and won't come back out…"
    # JA[2335]: 私のバッグをもった人はこの中に入って / いってしまって、出てこないの……。
    # [lay5 hide]
    $ show_sprites(("ha 2 sad"))
    # [lay1 +302 → l 1]
    $ show_sprites(("ha 2 sad", "l 1"))
    voice "ch5_l_024"
    l "…So they really did go inside?"
    # JA[6187]: ……確かにここに入っていったっていうのね？
    voice "ch5_ha_022"
    ha "…gulp."
    # JA[2336]: （……こくん）
    # [lay7 hide]
    $ show_sprites(("l 1"))
    # [lay1 hide]
    $ show_sprites()
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1"))
    voice "ch5_w_001"
    unk_w "…Oh my, is something the matter? The theater is closed for today, though…"
    # JA[15887]: ……おや、どうかされましたか？ / 今日は劇場は休演なのですが……。
    # [lay20 x=224]
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "w 1"))
    voice "ch5_l_025"
    l "Who are you?"
    # JA[6188]: あなたは？
    voice "ch5_w_002"
    unk_w "Forgive the intrusion."
    # JA[15888]: これは失礼しました。
    voice "ch5_w_003"
    w "I am given leave to perform at this theater. I am the leader of a traveling troupe. My name is Weatherby."
    # JA[15889]: わたしはこの劇場で芝居をやらせて / もらっている、旅の一座の座長、 / ウェザリーと申します。
    # [lay1 hide]
    $ show_sprites(("w 1"))
    # [lay7 +966 → ha 2 angry]
    $ show_sprites(("ha 2 angry", "w 1"))
    voice "ch5_ha_023"
    ha "That bag! That's my bag!"
    # JA[2337]: そのバッグ！ / 私のバッグです。
    th "…No doubt about it. The design is utterly out of place in this world. It's Haruna's bag.{#ch5_th_013}"
    # JA: （……ま、間違いない。 / 　この世界では違和感ありまくりのデザイン。 / 　春奈のバックだ）
    # [lay20 +1067 → w 1 sad]
    $ show_sprites(("ha 2 angry", "w 1 sad"))
    voice "ch5_w_004"
    w "Is this person unwell?"
    # JA[15890]: この方はどうかされたのですか？
    # [lay7 hide]
    $ show_sprites(("w 1 sad"))
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "w 1 sad"))
    voice "ch5_l_026"
    l "Ah, excuse us. I am Louise. And this is Haruna."
    # JA[6189]: ああ、ごめんなさい。 / わたしはルイズ。 / そして、彼女はハルナ。
    voice "ch5_l_027"
    l "She says the bag you're holding belongs to her."
    # JA[6190]: 彼女はあなたの持ってるバッグが / 自分のものであるといってるの。
    # [lay1 hide]
    $ show_sprites(("w 1 sad"))
    # [lay7 +966 → ha 2 angry]
    $ show_sprites(("ha 2 angry", "w 1 sad"))
    voice "ch5_ha_024"
    ha "My precious bag! Please give it back to me!"
    # JA[2338]: わ、私の大切なバッグなんです！ / 返してください！
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("ha 2 angry", "w 1 angry"))
    voice "ch5_w_005"
    w "…What a remarkably ungentle way to speak. As if I were the one who took your bag."
    # JA[15891]: ……なんだかおだやかじゃない物言いね。 / まるで、わたしがこのバッグを奪った / みたいじゃない？
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("ha 2 sad", "w 1 angry"))
    voice "ch5_ha_025"
    ha "W-well, that's not what I…"
    # JA[2339]: そ、そうじゃないけど……。
    voice "ch5_w_006"
    w "This is something I picked up on the road. You say it belongs to you — but what proof do you have?"
    # JA[15892]: これは、旅の途中で拾ったものなの。 / きみはこれが自分のものだというけど、 / その証拠は？
    voice "ch5_ha_026"
    ha "S-such a thing…"
    # JA[2340]: そ、そんな……。

    # ---- 【選択肢】 ----
    menu:
        "Watch over her.":
            # JA: 見守る
            # ==== SCENE 281 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay7 +968 → ha 2 sad]
            $ show_sprites(("ha 2 sad", "w 1 angry"))
            play music t18 fadein 1.0
            # [BG +50 → id(50)]
            $ fade_fx("id(50)")
            th "Go for it, Haruna!{#ch5_th_014}"
            # JA: （頑張れ、春奈！）
            # [lay20 hide]
            $ show_sprites(("ha 2 sad"))
            # [lay7 hide]
            $ show_sprites()
            # [lay1 +307 → l 1 angry]
            $ show_sprites(("l 1 angry"))
            voice "ch5_l_028"
            l "…Hey, Saito. What are you staring into space for? Why don't you go and help her?"
            # JA[6191]: ……ちょっと、サイト。 / なにボーっと見てるのよ！ / 助けてあげたらどうなの？
            # [TNDL       tndl(-30)] — не переносится (система не реализована, AGENTS §6)
            # [lay1 hide]
            $ show_sprites()
            # [lay1 +306 → l 1 angry]
            $ show_sprites(("l 1 angry"))
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("l 1 angry", "s 3 sad"))
            voice "ch5_s_026"
            s "No, I was just thinking about how I could help her…"
            # JA[11610]: いや、どう助けたらいいのかなぁって、 / 考えてたんだけど……。
            # [lay1 hide]
            $ show_sprites(("s 3 sad"))
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1", "s 3 sad"))
        "Offer to help.":
            # JA: 助け舟をだす
            # ==== SCENE 282 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay7 +968 → ha 2 sad]
            $ show_sprites(("ha 2 sad", "w 1 angry"))
            play music t18 fadein 1.0
            # [BG +50 → id(50)]
            $ fade_fx("id(50)")
            th "I-I have to offer to help…{#ch5_th_015}"
            # JA: （た、助け舟をださないと……）
            # [lay7 hide]
            $ show_sprites(("w 1 angry"))
            # [lay20 hide]
            $ show_sprites()
            # [lay5 +396 → s 1 sad]
            $ show_sprites(("s 1 sad"))
            voice "ch5_s_027"
            s "But there's no proof that it's your bag, either…"
            # JA[11611]: でも、あなたのバッグだという / 証明もないわけですが……。
            # [lay5 x=224]
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1", "s 1 sad"))
            voice "ch5_w_007"
            w "I picked it up a long time ago. If you want witnesses, there are plenty in the troupe."
            # JA[15893]: かなり前に拾ったの。 / 証人なら劇団に何人もいるわ。
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("w 1", "s 3 sad"))
            voice "ch5_s_028"
            s "No, well, that's…"
            # JA[11612]: いや、それはその……。
        "Tell Haruna to give up.":
            # JA: 春奈にあきらめさせる
            # ==== SCENE 283 ====
            # [if         if(isJump())] — не портируется
            # [RESET      reset()] — сброс сцены: спрайты скрываются
            $ show_sprites()
            # [lay20 +1065 → w 1 angry]
            $ show_sprites(("w 1 angry"))
            # [lay7 +968 → ha 2 sad]
            $ show_sprites(("ha 2 sad", "w 1 angry"))
            play music t18 fadein 1.0
            # [BG +50 → id(50)]
            $ fade_fx("id(50)")
            # [lay20 hide]
            $ show_sprites(("ha 2 sad"))
            # [lay5 +429 → s 3 sad]
            $ show_sprites(("ha 2 sad", "s 3 sad"))
            voice "ch5_s_029"
            s "…Haruna… let's give up."
            # JA[11613]: ……春奈……あきらめよう。
            # [lay7 +966 → ha 2 angry]
            $ show_sprites(("ha 2 angry", "s 3 sad"))
            voice "ch5_ha_027"
            ha "N-no! Never! Please, Hiraga-kun, ask her too!"
            # JA[2341]: い、いやよ！ / 絶対！ / 平賀くんからもお願いして！
            $ update_sympathy(-10, char_key="haruna")
            # [TNDL       tndl(30)] — не переносится (система не реализована, AGENTS §6)
            # [lay7 hide]
            $ show_sprites(("s 3 sad"))
            # [lay20 +1061 → w 1]
            $ show_sprites(("w 1", "s 3 sad"))

    # ==== SCENE 284 (переход после вариантов) ====
    # [if         if(isJump())] — не портируется
    # [RESET      reset()] — сброс сцены: спрайты скрываются
    $ show_sprites()
    # [lay20 +1061 → w 1]
    $ show_sprites(("w 1"))
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("w 1", "s 3 sad"))
    play music t18 fadein 1.0
    # [BG +50 → id(50)]
    $ fade_fx("id(50)")
    # [lay5 +429 → s 3 sad]
    voice "ch5_s_030"
    s "U-um… excuse me, troupe leader… That bag is very precious to her. Could you somehow return it to her?"
    # JA[11614]: あ、あの……座長さん……。 / そのバッグはとても大切なものなんです。 / なんとか返してもらえませんか？
    voice "ch5_w_008"
    w "I've taken a liking to it myself. Even if it really is yours, I can't hand it back so easily."
    # JA[15894]: こちらも気に入ってるんだ。 / 仮にあなた達のものであっても、 / 簡単には返せないな。
    voice "ch5_s_031"
    s "B-but that's!"
    # JA[11615]: そ、そんな！
    # [lay20 +1065 → w 1 angry]
    $ show_sprites(("w 1 angry", "s 3 sad"))
    voice "ch5_w_009"
    w "For now, what's not to be shall not be!"
    # JA[15895]: とりあえず、駄目なものは駄目だ！
    th "…This is hopeless. Let's come back later.{#ch5_th_016}"
    # JA: （……ダメだこりゃ。 / 　一度出直そう）
    # [lay20 hide]
    $ show_sprites(("s 3 sad"))
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("ha 2 sad", "s 3 sad"))
    voice "ch5_s_032"
    s "Let's pull back for now."
    # JA[11616]: とりあえずいったん引き上げよう。
    voice "ch5_ha_028"
    ha "Y-yeah…"
    # JA[2342]: う、うん……。
    # [SET        set("se1", {stop = 1})] — SE не портируется
    stop music fadeout 1.0
    # [lay5 hide]
    $ show_sprites(("ha 2 sad"))
    # [lay7 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")

    # [移動] → next(285): сцена 285 — часть 2 главы 5
    jump ch5_2
    return
