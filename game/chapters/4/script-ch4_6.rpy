# Глава 4, часть 6 (сцены 261–268 + даты 1084–1103): финал основной линии
# (бой с Акиной, разговор с Анриеттой) и четыре маршрута дат.
# Источник: ps2_source/chapters/chapter_05_トリスタニアの危機.txt
#   (SCENE 261–268, 1084–1103). Точные аргументы:
#   ps2_source/events_full/chapter_05_トリスタニアの危機.txt.
# Скелет собран генератором tools/gen_ch4_6_script.py (EN — tools/ch4_6_en.py,
#   RU — tools/ch4_6_ru.py), поэтому порядок реплик, голоса, спрайты и
#   события совпадают с источником дословно.
#
# Сцены 265–268 — «мосты» с мыслями Саито перед каждой датой. В PS2 система
#   дат прыгает прямо в 1084/1089/1094/1099 (dateDone → next(info.next)),
#   поэтому 265–268 не проигрываются: их текст перенесён в th в начале
#   соответствующей даты (ACCEPTABLE ADAPTATION — см. reports/ch4/6.md).
#   Сцена 1063 (CG+199) — мёртвая, не портируется.
#   Сцена 269 (конец дат) — принадлежит главе 5, не портируется.
#
# Голоса: ch4.6_<spk>_<NNN> — новая группа части 6, нумерация с 001 по
#   говорящему, порядок порта (261 → 262 → 263 → 264 → 1084 → 1085–1088 →
#   1089–1093 → 1094–1098 → 1099–1103):
#   s ×112, l ×49, h ×34, si ×29, ha ×28, d ×14, ak ×4 — всего 270.
#   Мысли (th, без голоса) — 19, пункты меню — 12.
#
# Не портируются: battle() (система боя не реализована), SE (se0 +63/+65/+72,
#   se1 stop), vibrate, msgon/msgoff, waitAction, sync, point x=/y=,
#   CREATE. COFFEE → pause(1.0).
# Фоны/CG: id(37), id(64), id(70) — имена пусты в image_id_map (заглушки);
#   id(102), id(201), id(202), id(203) — CG без имён (заглушки id(K)).
#   town_square_evening, library_night, sky_night, white — имена заполнены.
# Спрайты: id → имя по references/sprite_id_map.csv; PROVISIONAL:
#   420 = s 5 shy, 471 = s 8 angry, 552 = si 6 shy, 764 = h 1, 766 = h 1 happy,
#   770 = h 1 sad, 786 = h 2, 788 = h 2 happy, 792 = h 2 sad.
#   [471 в ch4_5 показан как "s 4 angry" — не соответствует биекции блоков
#    спрайтов (434 = единственный s 4); см. отчёт части 6 и журнал.]
#   [770 = h 1 sad по унифицированной пиксель-сетке (pos 6 = sad);
#    комментарий ch4_5 ("h 1 angry") без пиксель-сверки — расхождение
#    зафиксировано (RECONCILE) в отчёте и журнале.]
#   Спрайты Акины (lay21 +1028/+1032) в игре отсутствуют — не показываются.
#
# Меню дат: три опции (Луиза/Сиеста/Харуна) повторяют EN главы 1
#   ("Go on a date with ..."), их переводы уже есть в tl (повтор old запрещён —
#   E11); добавлена только Henrietta.
#
# Файл сгенерирован tools/gen_ch4_6_script.py — правки вносить в него
#   и в tools/ch4_6_en.py, затем перегенерировать.


label ch4_6:

    # ==== SCENE 261 ====
    # [BG +59 → town_square_evening]
    $ fade_fx("town_square_evening", new_music="t27")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("s 2 angry"))
    voice "ch4.6_s_001"
    s "Damn… Where are you? You're nowhere to be found."
    # JA[11557]: くそっ……。 / どこにいるんだ？ / どこにもいねぇぞ。
    # [lay5 x=224]
    # [lay19 +940 → d 1]
    $ show_sprites(("d 1", "s 2 angry"))
    voice "ch4.6_d_001"
    d "First off, we should head to where the explosion happened, shouldn't we?"
    # JA[1295]: とりあえず、爆発があったところへ / 行ってみるしかねぇなぁ？
    # [lay19 hide]
    $ show_sprites(("s 2 angry"))
    # [lay1 +339 → l 3 angry]
    $ show_sprites(("l 3 angry", "s 2 angry"))
    voice "ch4.6_l_001"
    l "…Saito, it's not that way! Don't just run off in some random direction! Hah… haah…."
    # JA[6136]: ……サイト、そっちじゃないってばっ！ / 勝手に変な方向に突っ走らないでよっ！ / はあっ、はあっ……。
    # [lay5 +440 → s 4 sad]
    $ show_sprites(("l 3 angry", "s 4 sad"))
    voice "ch4.6_s_002"
    s "I thought she'd run off over this way, though."
    # JA[11558]: こっちの方に走り去ったと思ったんだけどなぁ。
    stop music fadeout 1.0
    play music t17 fadein 1.0
    voice "ch4.6_ak_001"
    unk_ak "Hahaha… Seriously, I can't help but admire how dedicated you two are to your work."
    # JA[57]: ははははっ……。 / まったく、君達の仕事熱心さには / 頭がさがるよ。
    # [lay19 +940 → d 1]
    $ show_sprites(("l 3 angry", "d 1", "s 4 sad"))
    voice "ch4.6_d_002"
    d "Partner, she's on the roof."
    # JA[1296]: 相棒、屋根の上にいるぜ。
    # [lay21 hide]
    # [lay19 hide]
    $ show_sprites(("l 3 angry", "s 4 sad"))
    # [lay1 hide]
    $ show_sprites(("s 4 sad"))
    # [lay5 hide]
    $ show_sprites()
    # [BG hide] — поглощается переходом на CG
    # [EVENT_CG +102 → id(102)]
    $ fade_fx("id(102)", type="cg")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    voice "ch4.6_s_003"
    s "What!"
    # JA[11559]: 何！
    voice "ch4.6_l_002"
    l "There she is!! It's all that guy's fault, and I'm the one who…!!"
    # JA[6137]: いたわっ！！ / アイツのお陰で、わたしはぁ！！
    voice "ch4.6_d_003"
    d "Watch yourselves, you two. She's far more skilled than she looks. Underestimate her and it costs you your life."
    # JA[1297]: 気をつけな、お二人さん。 / ヤツは見かけに反してかなりの手練れだ。 / オンナ子供となめてかかっちゃ、命がない。
    voice "ch4.6_s_004"
    s "Yeah, I can believe that."
    # JA[11560]: ああ、それはなんとなく分かる。
    voice "ch4.6_l_003"
    l "O-of course, obviously."
    # JA[6138]: も……もちろんよっ。
    # [lay19 hide]
    # [lay1 hide]
    # [lay5 hide]
    # [BG hide]
    $ fade_fx("black")
    # [EVENT_CG hide] — поглощается переходом на фон
    # [BG +59 → town_square_evening]
    $ fade_fx("town_square_evening")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("s 2 angry"))
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "s 2 angry"))
    voice "ch4.6_s_005"
    s "…Are you scared, Louise?"
    # JA[11561]: ……怖いか、ルイズ？
    voice "ch4.6_l_004"
    l "…Mm.…I'm fine."
    # JA[6139]: ……ん。 / ……平気。
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "s 2 angry"))
    voice "ch4.6_l_005"
    l "As long as Saito is… As long as he'll protect me, I'm fine."
    # JA[6140]: サイトが……。 / ちゃんと守ってくれるなら平気。
    # [lay5 +405 → s 2 angry]
    voice "ch4.6_s_006"
    s "Got it. Then let's start the fight."
    # JA[11562]: 分かった、それなら戦闘開始だ。
    # [lay1 +335 → l 3]
    $ show_sprites(("l 3", "s 2 angry"))
    voice "ch4.6_l_006"
    l "Yeah.{#ch4.6_v6141}"
    # JA[6141]: うん。
    # [lay19 +940 → d 1]
    $ show_sprites(("l 3", "d 1", "s 2 angry"))
    voice "ch4.6_d_004"
    d "Here she comes, partner."
    # JA[1298]: さぁ相棒、相手も来るぞ？
    # [lay5 +440 → s 4 sad]
    $ show_sprites(("l 3", "d 1", "s 4 sad"))
    voice "ch4.6_s_007"
    s "Her bombs aren't magic, right? There's nothing I can do about them? It's not like I can just absorb them like usual."
    # JA[11563]: あいつの爆弾は、魔法じゃないんだろう。 / なんとかなるのか？ / いつもの魔法吸収ってわけにはいかないんだろ？
    voice "ch4.6_d_005"
    d "For now, you mix things up with your speed. The noble's girl casts magic while she's at it. That's all we've got."
    # JA[1299]: とりあえず、相棒は速さでかく乱しな。 / 貴族の娘っ子はその間に魔法で攻撃。 / これしかないな。
    # [lay19 hide]
    $ show_sprites(("l 3", "s 4 sad"))
    # [lay5 +471 → s 8 angry]
    $ show_sprites(("l 3", "s 8 angry"))
    voice "ch4.6_s_008"
    s "Got it. Doesn't look like there's anything else to do. Louise, we're going with that!"
    # JA[11564]: 分かった。 / それしかなさそうだな。 / ルイズ、それでいくぞ！
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "s 8 angry"))
    voice "ch4.6_l_007"
    l "Don't give me orders. I know perfectly well what I'm doing."
    # JA[6142]: わたしに指図しないでよね。 / ちゃんと分かってるわよ。
    voice "ch4.6_s_009"
    s "…Here we go!!"
    # JA[11565]: ……いくぞっ！！
    # [lay5 hide]
    $ show_sprites(("l 1 angry"))
    # [lay1 hide]
    $ show_sprites()
    # [lay21 +1028] — спрайт Акины: файла в медиа нет, не показывается
    voice "ch4.6_ak_002"
    unk_ak "…Heh."
    # JA[58]: ……ふっ。
    stop music fadeout 1.0
    # [lay21 hide]
    # [BG hide]
    $ fade_fx("black")
    # [BATTLE battleInit battleInit((0x02000000 +59))] — система боя не реализована, вызов не переносится
    # [BATTLE battleAdd  battleAdd("サイト")] — система боя не реализована, вызов не переносится
    # [BATTLE battleAdd  battleAdd("ルイズ")] — система боя не реализована, вызов не переносится
    # [BATTLE battleEnemy battleEnemy("左", "マントアキナ", (0x02000000 +1054))] — система боя не реализована, вызов не переносится
    # [BATTLE battleEnemy battleEnemy("右", "魔道士", (0x02000000 +1108))] — система боя не реализована, вызов не переносится
    # [BATTLE battle     battle()] — система боя не реализована, вызов не переносится

    # ==== SCENE 262 ====
    # [BG +59 → town_square_evening]
    $ fade_fx("town_square_evening", new_music="t24")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay21 +1032] — спрайт Акины: файла в медиа нет, не показывается
    voice "ch4.6_ak_003"
    unk_ak "…Tch!!!! Against an opponent like this…"
    # JA[59]: ……くっ！！！！ / こんな相手に……。
    # [lay21 x=-96]
    # [lay5 +405 → s 2 angry]
    $ show_sprites(("s 2 angry"))
    voice "ch4.6_s_010"
    s "How about… giving up? If you keep this up, you don't stand a chance."
    # JA[11566]: そろそろ……降参したらどうだぁ？ / このまま続けても、おまえに勝ち目はない。
    voice "ch4.6_ak_004"
    unk_ak "…Come and get me!!"
    # JA[60]: ……くらえ！！
    voice "ch4.6_s_011"
    s "Louise! Bombs! Get down!!"
    # JA[11567]: ルイズっ、爆弾だ！ / 隠れろっ！！
    # [lay21 hide]
    # [lay5 hide]
    $ show_sprites()
    # [VIBRATE    vibrate(3)] — SE не портируется
    # [EVENT_CG hide]
    $ fade_fx("black")
    # [lay5 hide]
    # [lay21 hide]
    # [lay19 hide]
    # [lay1 hide]
    # [BG +2 → white]
    $ fade_fx("white")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    voice "ch4.6_l_008"
    l "Hyaah!!"
    # JA[6143]: ひゃあっ！！
    voice "ch4.6_s_012"
    s "Guaah…!!"
    # JA[11568]: ぐあっ……！！
    voice "ch4.6_d_006"
    d "…! Blindfolding trick?! Partner, let's get out of here!"
    # JA[1300]: くっ……目くらましかっ！？ / やっこさん、逃げていくぞっ！？
    voice "ch4.6_s_013"
    s "No good… I can't see a thing, it's all blurred!!"
    # JA[11569]: ダメだっ……まぶしくて何も見えない！！
    voice "ch4.6_l_009"
    l "Uuaah… kuuhhh!!!"
    # JA[6144]: ぅぁ……くううっ！！！
    stop music fadeout 1.0
    # [TRANS   trans("crossfade", 0)] — переход выполняется fade_fx
    # [lay1 hide]
    # [lay5 hide]
    # [lay19 hide]
    # [BG +89 → sky_evening]
    $ fade_fx("sky_evening")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    th "….\n….\n….{#ch4.6_th_001}"
    # JA: ………。 / ……。 / …。
    th "In the end, we missed catching the Bomb User by just one step.{#ch4.6_th_002}"
    # JA: （結局、あと一歩の所で俺達は、 / 　爆弾使いを捕まえることができなかった）
    # [lay5 hide]
    # [lay19 hide]
    # [BG hide]
    $ fade_fx("black")
    # [BG +59 → town_square_evening]
    $ fade_fx("town_square_evening", new_music="t5")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry"))
    voice "ch4.6_l_010"
    l "Youu! She got away when I almost had her!! Next time I see her, I won't let her escape!"
    # JA[6145]: もおっ！ / あと少しで捕まえられたのにぃ！！ / 今度会ったときは、絶対に逃がさないんだから！
    # [lay1 hide]
    $ show_sprites()
    # [lay1 +307 → l 1 angry]
    $ show_sprites(("l 1 angry"))
    voice "ch4.6_l_011"
    l "Just watch!"
    # JA[6146]: 見てなさい！
    voice "ch4.6_l_012"
    l "When I do catch her, I'll repay the humiliation I suffered a hundredfold over!!!"
    # JA[6147]: 捕まえた暁には、 / わたしが受けた屈辱を何百倍にもして / 返してあげるんだから！！！
    # [lay1 hide]
    $ show_sprites()
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry"))
    # [lay5 +407 → s 2 sad]
    $ show_sprites(("l 1 angry", "s 2 sad"))
    voice "ch4.6_s_014"
    s "Louise, are you hurt anywhere?"
    # JA[11570]: ルイズ、どこもケガはないか？
    # [lay1 +310 → l 1 shy]
    $ show_sprites(("l 1 shy", "s 2 sad"))
    voice "ch4.6_l_013"
    l "Eh…!? …Yeah, I'm fine."
    # JA[6148]: えっ……！？ / ……うん、平気。
    # [lay5 +401 → s 2]
    $ show_sprites(("l 1 shy", "s 2"))
    voice "ch4.6_s_015"
    s "I see… Then let's head back to the castle and report to the princess."
    # JA[11571]: そっか……。 / それじゃあ、城へ戻ってお姫さまに報告しよう。
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "s 2"))
    voice "ch4.6_l_014"
    l "Yeah, that's right."
    # JA[6149]: うん、そうね。
    # [lay19 +940 → d 1]
    $ show_sprites(("l 1", "d 1", "s 2"))
    voice "ch4.6_d_007"
    d "Looks like we'll get home safe. Good work, both of you — the partner and the lady."
    # JA[1301]: どうやら無事に帰れそうだなぁ。 / 相棒も娘っ子もご苦労さん。
    # [lay5 +434 → s 4]
    $ show_sprites(("l 1", "d 1", "s 4"))
    voice "ch4.6_s_016"
    s "Yeah… you helped again this time, Delphy."
    # JA[11572]: ああ……今回も助かったよ、デルフ。
    voice "ch4.6_d_008"
    d "Just leave it to me."
    # JA[1302]: まぁ、任せておきなって。
    # [lay19 hide]
    $ show_sprites(("l 1", "s 4"))
    # [lay1 +310 → l 1 shy]
    $ show_sprites(("l 1 shy", "s 4"))
    voice "ch4.6_l_015"
    l "Saito…{#ch4.6_v6150}"
    # JA[6150]: サイトっ……。
    # [lay5 +401 → s 2]
    $ show_sprites(("l 1 shy", "s 2"))
    voice "ch4.6_s_017"
    s "What is it, Louise?"
    # JA[11573]: なんだい、ルイズ？
    # [lay5 +407 → s 2 sad]
    $ show_sprites(("l 1 shy", "s 2 sad"))
    th "What's with Louise? She's acting all hesitant for some reason.{#ch4.6_th_003}"
    # JA: （なんだぁ、ルイズのやつ？ / 　やけにモジモジしやがって）
    # [lay1 +343 → l 3 shy]
    $ show_sprites(("l 3 shy", "s 2 sad"))
    voice "ch4.6_l_016"
    l "…Um… no, it's… …I'm going back to the castle."
    # JA[6151]: ……あのっ……ううん、その。 / ……城に帰るわ。
    # [lay5 +401 → s 2]
    $ show_sprites(("l 3 shy", "s 2"))
    voice "ch4.6_s_018"
    s "Sure, let's head back."
    # JA[11574]: ああ、戻るとするか。
    stop music fadeout 1.0
    # [lay5 hide]
    $ show_sprites(("l 3 shy"))
    # [lay1 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")

    # ==== SCENE 263 ====
    # [BG +90 → sky_night]
    $ fade_fx("sky_night", new_music="t19")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    th "Saito and Louise reported to the princess that they had let the Bomb User escape.{#ch4.6_th_004}"
    # JA: （俺とルイズは、爆弾使いを取り逃がしたことを / 　お姫さまに報告した）
    # [lay5 hide]
    # [BG hide]
    $ fade_fx("black")
    # [BG +37 → id(37)]
    $ fade_fx("id(37)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay8 +764 → h 1]
    $ show_sprites(("h 1"))
    voice "ch4.6_h_001"
    h "I see. Even so, thanks to your efforts this time, we were able to repel them safely."
    # JA[562]: そうでしたか。 / ですが、今回は、あなた達の活躍で / 無事撃退をすることができました。
    voice "ch4.6_h_002"
    h "Allow me to give thanks on behalf of the citizens."
    # JA[563]: 市民に成り代わりお礼を言わせてください。
    # [lay8 x=224]
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "h 1"))
    voice "ch4.6_l_017"
    l "Such unnecessary words."
    # JA[6152]: そんな、もったいないお言葉です。
    # [lay8 +766 → h 1 happy]
    $ show_sprites(("l 1 sad", "h 1 happy"))
    voice "ch4.6_h_003"
    h "Stay at the palace tonight, and take the fatigue of your journey off slowly."
    # JA[564]: 今宵はこの王宮に留まって、 / 旅の疲れをゆっくりといやしてください。
    # [lay1 hide]
    $ show_sprites(("h 1 happy"))
    # [lay5 +403 → s 2 happy]
    $ show_sprites(("s 2 happy", "h 1 happy"))
    voice "ch4.6_s_019"
    s "Thank you, Your Highness."
    # JA[11575]: ありがとうございます、お姫さま。
    # [lay5 hide]
    $ show_sprites(("h 1 happy"))
    # [lay1 +304 → l 1 happy]
    $ show_sprites(("l 1 happy", "h 1 happy"))
    voice "ch4.6_l_018"
    l "Thank you, Your Majesty.{#ch4.6_v6153}"
    # JA[6153]: ありがとうございます、女王陛下。
    # [lay8 +764 → h 1]
    $ show_sprites(("l 1 happy", "h 1"))
    voice "ch4.6_h_004"
    h "No, no, it's quite all right, Louise."
    # JA[565]: そんな、いいのですよルイズ。
    # [lay8 +770 → h 1 sad]
    $ show_sprites(("l 1 happy", "h 1 sad"))
    voice "ch4.6_h_005"
    h "I would like to make at least some amends for my own foolishness, which would have put even my precious friends in danger."
    # JA[566]: 大切な友人までも、危険に晒そうとする / ような愚かなわたくしに、せめてもの償いを / させてちょうだい。
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "h 1 sad"))
    voice "ch4.6_l_019"
    l "We acted of our own will. I never once thought the princess was to blame."
    # JA[6154]: わたし達は、自分の意思で行動しています。 / 姫さまが悪いなんて、思ったことはありません。
    # [lay8 +764 → h 1]
    $ show_sprites(("l 1", "h 1"))
    voice "ch4.6_h_006"
    h "Mm… Thank you, Louise."
    # JA[567]: うん……。 / ありがとう、ルイズ。
    voice "ch4.6_h_007"
    h "Well then, I have a great many things to clean up. I will take my leave."
    # JA[568]: では、わたくしはいろいろと / 後始末をせねばなりませんので。 / これで失礼します。
    # [lay8 hide]
    $ show_sprites(("l 1"))
    # [lay1 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [BG +70 → id(70)]
    $ fade_fx("id(70)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay2 +491 → si 1 happy]
    $ show_sprites(("si 1 happy"))
    voice "ch4.6_si_001"
    si "Mr. Saito!!"
    # JA[14760]: サイトさんっ！！
    # [lay2 x=224]
    # [lay7 +964 → ha 2 happy]
    $ show_sprites(("ha 2 happy", "si 1 happy"))
    voice "ch4.6_ha_001"
    ha "Mr. Hiraga!!"
    # JA[2309]: 平賀くんっ！！
    # [lay2 hide]
    $ show_sprites(("ha 2 happy"))
    # [lay7 hide]
    $ show_sprites()
    # [lay5 +401 → s 2]
    $ show_sprites(("s 2"))
    voice "ch4.6_s_020"
    s "Hey, you two — are you both unharmed?"
    # JA[11576]: やあ、２人とも無事だったかい？
    # [lay5 x=224]
    # [lay2 +489 → si 1]
    $ show_sprites(("si 1", "s 2"))
    voice "ch4.6_si_002"
    si "Yes. The castle soldiers saw us to safety properly."
    # JA[14761]: はい、お城の兵士さんがちゃんと / 避難させてくれましたから。
    # [lay2 hide]
    $ show_sprites(("s 2"))
    # [lay7 +962 → ha 2]
    $ show_sprites(("ha 2", "s 2"))
    voice "ch4.6_ha_002"
    ha "Are you all right, Mr. Hiraga?"
    # JA[2310]: 平賀くんは大丈夫だった？
    # [lay5 +434 → s 4]
    $ show_sprites(("ha 2", "s 4"))
    voice "ch4.6_s_021"
    s "I'm fine. Even if I am hurt, it's nothing but a scratch."
    # JA[11577]: 大丈夫。 / あってもかすり傷ぐらいだから。
    # [lay5 hide]
    $ show_sprites(("ha 2"))
    # [lay7 hide]
    $ show_sprites()
    # [lay1 +304 → l 1 happy]
    $ show_sprites(("l 1 happy"))
    voice "ch4.6_l_020"
    l "But I'm glad it wasn't you, Haruna."
    # JA[6155]: でも、ハルナのことじゃなくて、良かったわね。
    # [lay1 x=-96]
    # [lay7 +964 → ha 2 happy]
    $ show_sprites(("l 1 happy", "ha 2 happy"))
    voice "ch4.6_ha_003"
    ha "Thank you, Miss Louise. Please at least let me say thanks."
    # JA[2311]: ありがとうございます、ルイズさん。 / お礼だけでも言わせてください。
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "ha 2 happy"))
    voice "ch4.6_l_021"
    l "It's nothing, don't worry about it. That settles the matter of Haruna between the Academy and the palace."
    # JA[6156]: 別にいいわよ、気にしてないから。 / これで、ハルナのことに関して / 魔法学院と王宮は解決したわけだけど。
    # [lay1 +335 → l 3]
    $ show_sprites(("l 3", "ha 2 happy"))
    voice "ch4.6_l_022"
    l "But the problem isn't solved yet."
    # JA[6157]: でも、問題は、まだ残ってるわ。
    # [lay7 hide]
    $ show_sprites(("l 3"))
    # [lay5 +440 → s 4 sad]
    $ show_sprites(("l 3", "s 4 sad"))
    voice "ch4.6_s_022"
    s "Huh? Is there still something?"
    # JA[11578]: はぁ？ / まだ、何かあるのかよ？
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "s 4 sad"))
    voice "ch4.6_l_023"
    l "Yes, exactly. This is a very serious problem."
    # JA[6158]: ええ、そうよ。 / これはきわめて重大な問題よ。
    # [lay5 hide]
    $ show_sprites(("l 1"))
    # [lay2 +489 → si 1]
    $ show_sprites(("l 1", "si 1"))
    voice "ch4.6_si_003"
    si "What on earth could it be?"
    # JA[14762]: それはいったい何なんですか？
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad", "si 1"))
    voice "ch4.6_l_024"
    l "To put it plainly: money. She's a commoner, but a girl has been added to the household, hasn't she? Her current allowance won't come close to covering it."
    # JA[6159]: ハッキリ言ってしまえば、それはお金よ。 / 平民とはいえ、女の子が１人増えたのよ？ / 今の生活費だけじゃとても足りないわ。
    # [lay2 hide]
    $ show_sprites(("l 1 sad"))
    # [lay5 +407 → s 2 sad]
    $ show_sprites(("l 1 sad", "s 2 sad"))
    voice "ch4.6_s_023"
    s "Heh~. What a difference in treatment compared to me, if I may say so, my master."
    # JA[11579]: へぇ～。 / ボクとはえらい待遇の違いですねぇ、ご主人様。
    # [lay1 +335 → l 3]
    $ show_sprites(("l 3", "s 2 sad"))
    voice "ch4.6_l_025"
    l "My, is something rather mistaken going on in your head? You're a familiar, aren't you? That's only natural."
    # JA[6160]: あら、何かひどい思い違いをしてるようね？ / あなたは使い魔でしょ。 / そんなの、当たり前じゃないの。
    # [lay5 +440 → s 4 sad]
    $ show_sprites(("l 3", "s 4 sad"))
    voice "ch4.6_s_024"
    s "….{#ch4.6_v11580}"
    # JA[11580]: ……。
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "s 4 sad"))
    voice "ch4.6_l_026"
    l "It is a master's duty to provide for their familiar. That's all well and good, though. But Haruna…"
    # JA[6161]: 使い魔を養っていくのは飼い主の務めだから。 / それはいいんだけど。 / でも、ハルナは……。
    # [lay5 hide]
    $ show_sprites(("l 1"))
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("l 1", "ha 2 sad"))
    voice "ch4.6_ha_004"
    ha "That's true. If only we could find a way to get back to Japan soon…"
    # JA[2312]: そうですね。 / 早く日本へ帰る方法が見つかれば / いいんですけど。
    # [lay1 hide]
    $ show_sprites(("ha 2 sad"))
    # [lay5 +407 → s 2 sad]
    $ show_sprites(("s 2 sad", "ha 2 sad"))
    voice "ch4.6_s_025"
    s "Yeah… that's true…"
    # JA[11581]: ホント、そうだよなぁ……。
    # [lay7 hide]
    $ show_sprites(("s 2 sad"))
    # [lay5 hide]
    $ show_sprites()
    # [lay2 +491 → si 1 happy]
    $ show_sprites(("si 1 happy"))
    voice "ch4.6_si_004"
    si "Oh! That's a good idea! Miss Haruna, would you like to help us with the kitchen work at the Academy?"
    # JA[14763]: あっ、そうですよっ！ / ハルナさん、わたし達と一緒に魔法学院で / 給仕の仕事を手伝いませんか？
    # [lay2 x=-96]
    # [lay5 +403 → s 2 happy]
    $ show_sprites(("si 1 happy", "s 2 happy"))
    voice "ch4.6_s_026"
    s "Oh…! Right! That's a good idea, isn't it!"
    # JA[11582]: おおっ……。 / そうかっ、その手があったじゃないか！
    # [lay2 hide]
    $ show_sprites(("s 2 happy"))
    # [lay5 +401 → s 2]
    $ show_sprites(("s 2"))
    th "Does this mean I'll be ogling Haruna in her maid outfit every day!?{#ch4.6_th_005}"
    # JA: （これはもしや、春奈のメイド服姿が毎日 / 　おがめる事になるのではっ！？）
    th "Let me imagine it… Haruna in a maid outfit!!{#ch4.6_th_006}"
    # JA: （想像してみよう……。 / 　春奈のメイド服姿をっ！！）
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    th "….{#ch4.6_th_007}"
    # JA: ………。
    # [lay5 hide]
    # [BG +70 → id(70)]
    $ fade_fx("id(70)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +403 → s 2 happy]
    $ show_sprites(("s 2 happy"))
    # [waitSEStop waitSEStop(null, true)] — не портируется
    voice "ch4.6_s_027"
    s "Haruna! I think that's a great idea too!"
    # JA[11583]: 春奈っ！ / それは、グッドアイデアだと俺も思うぞ！
    # [lay5 x=224]
    # [lay1 +306 → l 1 angry]
    $ show_sprites(("l 1 angry", "s 2 happy"))
    voice "ch4.6_l_027"
    l "Why is Saito so happy about that?"
    # JA[6162]: なんでサイトが、そこで喜ぶのよっ？
    # [lay5 +434 → s 4]
    $ show_sprites(("l 1 angry", "s 4"))
    voice "ch4.6_s_028"
    s "Hmph, n-no, you don't need to worry about it."
    # JA[11584]: ベツニ、ヨロコンデナンテイマセンヨ。
    # [lay1 +339 → l 3 angry]
    $ show_sprites(("l 3 angry", "s 4"))
    voice "ch4.6_l_028"
    l "…Hmph."
    # JA[6163]: ……ふん。
    # [lay5 hide]
    $ show_sprites(("l 3 angry"))
    # [lay1 hide]
    $ show_sprites()
    # [lay7 +968 → ha 2 sad]
    $ show_sprites(("ha 2 sad"))
    voice "ch4.6_ha_005"
    ha "Hmm, but I've always left everything around the house to my parents… I don't know if I can really do anything…"
    # JA[2313]: う～ん、でも私、身の回りのことは、 / すべて親に任せっきりだったから。 / 本当に、何かできるかどうか……。
    # [lay7 x=224]
    # [lay2 +491 → si 1 happy]
    $ show_sprites(("si 1 happy", "ha 2 sad"))
    voice "ch4.6_si_005"
    si "You needn't worry about that. Everyone here is kind and helpful. They'll teach you one thing at a time, carefully."
    # JA[14764]: そんなこと、心配いりませんよ。 / みんな優しくて親切な方ばかりですから。 / ひとつずつ、丁寧に教えてくれます。
    # [lay2 +489 → si 1]
    $ show_sprites(("si 1", "ha 2 sad"))
    voice "ch4.6_si_006"
    si "If Miss Haruna feels like it, please don't hesitate to come to any of us."
    # JA[14765]: ハルナさんがもしその気になったら、 / いつでも声をかけてくださいね。
    # [lay7 +964 → ha 2 happy]
    $ show_sprites(("si 1", "ha 2 happy"))
    voice "ch4.6_ha_006"
    ha "Yes… Thank you.{#ch4.6_v2314}"
    # JA[2314]: はい……。 / ありがとうございます。
    stop music fadeout 1.0
    # [lay2 hide]
    $ show_sprites(("ha 2 happy"))
    # [lay7 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")

    # ==== SCENE 264 ====
    # [BG +64 → id(64)]
    $ fade_fx("id(64)", new_music="t20")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +412 → s 5]
    $ show_sprites(("s 5"))
    th "A lot happened today, huh.{#ch4.6_th_008}"
    # JA: （今日は色々あったなぁ）
    th "Meeting the princess. Fighting the Bomb User…{#ch4.6_th_009}"
    # JA: （お姫さまとの対面。 / 　爆弾使いとの戦闘……）
    th "Well, at least Haruna's matter is settled, so that's something.{#ch4.6_th_010}"
    # JA: （まぁ、春奈のことが / 　解決しただけでも良しとするか）
    th "Huh? Where did everyone go? Maybe I should go out for a bit.{#ch4.6_th_011}"
    # JA: （あれ？ / 　みんなどこに行ったんだろう。 / 　ちょっと出歩いてみるとしますか）
    stop music fadeout 1.0
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [DATE       dateItem("ルイズ", (0x01000000 +1084))] — не портируется
    # [DATE       dateItem("シエスタ", (0x01000000 +1089))] — не портируется
    # [DATE       dateItem("ハルナ", (0x01000000 +1094))] — не портируется
    # [DATE       dateItem("アンリエッタ", (0x01000000 +1099))] — не портируется
    # [DATE       date((0x01000000 +269),false,(0x03000000 +4))] — не портируется

    # ---- 【デート】 меню выбора даты ----
    $ portrait_choice([
        {"char": "louise",    "text": "Go on a date with Louise",     "target": "date_louise_ch4_6"},
        {"char": "siesta",    "text": "Go on a date with Siesta",     "target": "date_siesta_ch4_6"},
        {"char": "haruna",    "text": "Go on a date with Haruna",     "target": "date_haruna_ch4_6"},
        {"char": "henrietta", "text": "Go on a date with Henrietta",  "target": "date_henrietta_ch4_6"},
    ])

    $ fade_fx("black")
    stop music fadeout 1.0
    # [移動] → next(269): глава 5 (часть 1) — вместо jump attention
    #   (PS2: date((0x01000000 +269), …) — после даты сцена 269; правка
    #   от 2026-10-22, см. reports/log.md)
    jump ch5
    return

label date_louise_ch4_6:
    # ==== SCENE 265 (мост): в PS2 не проигрывается (dateDone → next(1084) прямо)
    # текст мысли канонически сохранён здесь (ACCEPTABLE ADAPTATION)
    th "Where did Louise go…? Maybe I should go look for her.{#ch4.6_th_012}"
    # JA: （ルイズはどこに行ったんだろう……。 / 　ちょっと探してみるか）

    # ==== SCENE 1084 ====
    # [BG +67 → library_night]
    $ fade_fx("library_night", new_music="t5")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +429 → s 3 sad]
    $ show_sprites(("s 3 sad"))
    voice "ch4.6_s_029"
    s "Siesta told me Louise was in here. There's quite a mountain of books, isn't there?"
    # JA[8547]: ここにルイズがいるってシエスタに / 聞いてきたけど、ずいぶん本が / たくさんあるなぁ。
    # [lay5 +390 → s 1]
    $ show_sprites(("s 1"))
    voice "ch4.6_s_030"
    s "Louise! You in there?"
    # JA[8548]: ルイズー、いるかー。
    # [lay5 hide]
    $ show_sprites()
    # [BG hide] — поглощается переходом на CG
    # [EVENT_CG +201 → id(201)]
    $ fade_fx("id(201)", type="cg")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    voice "ch4.6_l_029"
    l "Saito, you're supposed to keep quiet in the library. Manners, you know?"
    # JA[4711]: もうっ。 / サイト、図書室は静かにしなさいよね。 / マナーでしょ？
    $ update_sympathy(20, char_key="louise")
    # [EVENT_CG +202 → id(202)]
    $ fade_fx("id(202)", type="cg")
    voice "ch4.6_s_031"
    s "Ah, sorry. Whoa, that's a mountain of books. Have you read all of these?"
    # JA[8549]: あ、ごめん。 / って、すごい山だな。 / これ全部読んでるのか？
    # [waitSEStop waitSEStop(null, true)] — не портируется
    voice "ch4.6_l_030"
    l "They're books on magic. Some of them are valuable works written down from the legends of Founder Brimir Valtori, from long ago."
    # JA[4712]: 魔法に関する本よ。 / 古くは、始祖ブリミル・ヴァルトリの伝承から / 書きつづられた貴重な書物もあるわ。
    voice "ch4.6_l_031"
    l "Normally, these books can't be read without the palace's permission — but I got it from the princess."
    # JA[4713]: これらの本は、本来王宮からの許可が / 出ないと読めない本なんだけど、 / 姫さまに許可をいただいたの。
    voice "ch4.6_s_032"
    s "Hmm, I have no idea what any of that means. What are you researching?"
    # JA[8550]: はぁ、俺にはサッパリ分からないや。 / 何を調べてるんだ？
    voice "ch4.6_l_032"
    l "…The magic of the Void."
    # JA[4714]: ……虚無の魔法。
    voice "ch4.6_s_033"
    s "….{#ch4.6_v8551}"
    # JA[8551]: ……。
    voice "ch4.6_l_033"
    l "A power too great for human hands."
    # JA[4715]: 人の手には余る、その力。
    # [EVENT_CG +203 → id(203)]
    $ fade_fx("id(203)", type="cg")
    voice "ch4.6_l_034"
    l "It's… a bit unsettling, you could say. When I'm alone… I always end up feeling anxious."
    # JA[4716]: ちょっと、気になるっていうか。 / １人で居たりすると…… / どうしても、不安になるのよね。
    voice "ch4.6_l_035"
    l "After all… it is unsettling. In my case, the magic is still incomplete, and its nature is unknown."
    # JA[4717]: だって……気味悪いじゃない。 / わたしの場合はまだ、得体の知れない / 不完全な魔法だから。
    # [EVENT_CG +202 → id(202)]
    $ fade_fx("id(202)", type="cg")
    voice "ch4.6_l_036"
    l "I thought that if I could learn even a little something new, it would be worth reading… but I understand absolutely nothing."
    # JA[4718]: なにか、新しいことが少しでも分かるなら、 / と思って読んでたんだけど……。 / でも、ぜ～んぜん、分かんない。
    voice "ch4.6_s_034"
    s "….{#ch4.6_v8552}"
    # JA[8552]: ……。

    # ---- 【選択肢】 ----
    menu:
        "She really is hardworking, isn't she?":
            # JA: ルイズは努力家なんだな
            # ==== SCENE 1085 ====
            play music t5 fadein 1.0
            # [EVENT_CG +202 → id(202)]
            $ fade_fx("id(202)", type="cg")
            voice "ch4.6_s_035"
            s "Louise really is incredibly serious, isn't she?"
            # JA[8553]: ルイズって、凄く真面目だよな。
            # [EVENT_CG +203 → id(203)]
            $ fade_fx("id(203)", type="cg")
            voice "ch4.6_l_037"
            l "Oh? Is that a bad thing?"
            # JA[4719]: あら、いけないのかしら？
            voice "ch4.6_s_036"
            s "No, it's not that I could ever match her. Um, wait, that's not what I—"
            # JA[8554]: いや、俺なんかじゃ到底マネ / できないっていうか。 / ええっと、そうじゃなくって……。
            voice "ch4.6_s_037"
            s "When she's focused on something, the way she comes across is… quite different from when she's with me, I guess."
            # JA[8555]: 何かに取り組んでる時のルイズって、 / 俺と居る時なんかとイメージが / 違ってるなぁって。
            voice "ch4.6_l_038"
            l "Really?{#ch4.6_v4720}"
            # JA[4720]: そう？
            $ update_sympathy(10, char_key="louise")
            # [EVENT_CG +202 → id(202)]
            $ fade_fx("id(202)", type="cg")
        "Why not try doing it without relying on books?{#ch4.6_c1086}":
            # JA: 本に頼らないってどうだ？
            # ==== SCENE 1086 ====
            play music t5 fadein 1.0
            # [EVENT_CG +202 → id(202)]
            $ fade_fx("id(202)", type="cg")
            # [lay5 hide]
            voice "ch4.6_s_038"
            s "Why not try doing it without relying on books?{#ch4.6_v8556}"
            # JA[8556]: 本に頼らないってどうだ？
            # [EVENT_CG +203 → id(203)]
            $ fade_fx("id(203)", type="cg")
            voice "ch4.6_l_039"
            l "I'd be relieved if it did, but… no, that won't work either."
            # JA[4721]: それで安心できるならいいんだけど……。 / やっぱり駄目。
            voice "ch4.6_l_040"
            l "In the end, where this power comes from and where it's heading… I have no way of understanding any of it on my own."
            # JA[4722]: 結局この力がどこから来て、 / どこに向かうのか……。 / わたしだけでは全然分からないもの。
            voice "ch4.6_l_041"
            l "Thinking about it that way… I'm not even a wielder of the Void, I'm just—"
            # JA[4723]: そう考えると、わたし……。 / 虚無の使い手でもなんでもなく、
            # [EVENT_CG +202 → id(202)]
            $ fade_fx("id(202)", type="cg")
            voice "ch4.6_l_042"
            l "—maybe only someone who is being lured to the Void."
            # JA[4724]: ただ、虚無にほんろうされてる / だけかもしれないわ。
            voice "ch4.6_s_039"
            s "….{#ch4.6_v8557}"
            # JA[8557]: ……。
        "Why not ask Tabitha about it?":
            # JA: タバサに聞いてみるのは？
            # ==== SCENE 1087 ====
            play music t5 fadein 1.0
            # [EVENT_CG +202 → id(202)]
            $ fade_fx("id(202)", type="cg")
            voice "ch4.6_s_040"
            s "If it's about books, maybe you should ask Tabitha about it?"
            # JA[8558]: 本のことだったらさ、タバサにでも相談した方が / いいんじゃないのか？
            # [EVENT_CG +203 → id(203)]
            $ fade_fx("id(203)", type="cg")
            voice "ch4.6_l_043"
            l "I see, Tabitha. If I say I'm looking for books on Founder Brimir, she might know something."
            # JA[4725]: なるほど、タバサね。 / 始祖ブリミルについての本を探してるって / 言えば何か知ってるかもしれないわね。
            $ update_sympathy(-10, char_key="louise")
            voice "ch4.6_s_041"
            s "Well, I can't exactly tell Tabitha I'm researching the power of the Void, can I?"
            # JA[8559]: まぁ、でもタバサに虚無の力について / 調べています、って話すわけにもいかないよな。
            # [EVENT_CG +202 → id(202)]
            $ fade_fx("id(202)", type="cg")
            voice "ch4.6_l_044"
            l "That's true, but never mind. Once we're back at the Academy, I'll ask her about it."
            # JA[4726]: それはそうでしょうけど、まぁいいわ。 / 魔法学院に帰ったら、一度相談にのってもらう / ことにする。

    # ==== SCENE 1088 (переход после вариантов) ====
    play music t5 fadein 1.0
    # [EVENT_CG +202 → id(202)]
    $ fade_fx("id(202)", type="cg")
    voice "ch4.6_s_042"
    s "You're going to start investigating the Bomb User tomorrow, aren't you?"
    # JA[8560]: どうせ明日から、爆弾使いの調査を / 始めるんだろ？
    voice "ch4.6_s_043"
    s "You'd better not let your magic research get out of hand, or you'll wear yourself out."
    # JA[8561]: 魔法の研究も程々にしておかないと、 / そのうち身が持たなくなるぞ？
    # [EVENT_CG +203 → id(203)]
    $ fade_fx("id(203)", type="cg")
    voice "ch4.6_l_045"
    l "I know, I know."
    # JA[4727]: 分かってるわよ。
    voice "ch4.6_s_044"
    s "But maybe I should learn from Louise's serious, devoted side too. I just can't go around swinging a sword, though."
    # JA[8562]: でも俺もさ、ルイズの真面目でひたむきな所を / 見習わなくちゃいけないのかもな。 / ただ、剣を振り回してちゃいけないもんな。
    voice "ch4.6_l_046"
    l "You don't have to copy me. That wouldn't be like you at all."
    # JA[4728]: 別にマネしなくたっていいわよ。 / それこそ、サイトらしくないわ。
    voice "ch4.6_s_045"
    s "Right, then I'll head back to my room too."
    # JA[8563]: ああ、それじゃあ俺も部屋に帰るよ。
    # [lay1 hide]
    # [lay5 hide]
    # [EVENT_CG hide] — поглощается переходом на фон
    # [BG +67 → library_night]
    $ fade_fx("library_night")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay1 +308 → l 1 sad]
    $ show_sprites(("l 1 sad"))
    # [lay5 +390 → s 1]
    $ show_sprites(("l 1 sad", "s 1"))
    voice "ch4.6_l_047"
    l "….{#ch4.6_v4729}"
    # JA[4729]: ……。
    # [lay1 +302 → l 1]
    $ show_sprites(("l 1", "s 1"))
    voice "ch4.6_l_048"
    l "Saito."
    # JA[4730]: サイトっ。
    # [lay5 +396 → s 1 sad]
    $ show_sprites(("l 1", "s 1 sad"))
    voice "ch4.6_s_046"
    s "Wh-what is it?"
    # JA[8564]: なんだよぉ、一体？
    # [lay1 +304 → l 1 happy]
    $ show_sprites(("l 1 happy", "s 1 sad"))
    voice "ch4.6_l_049"
    l "Thank you.{#ch4.6_v4731}"
    # JA[4731]: ありがとうっ。
    stop music fadeout 1.0
    # [lay1 hide]
    $ show_sprites(("s 1 sad"))
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [COFFEE] → pause(1.0)
    $ pause(1.0)

    # [移動] → next(269): сцена 269 — глава 5, НЕ портируется
    return

label date_siesta_ch4_6:
    # ==== SCENE 266 (мост): в PS2 не проигрывается (dateDone → next(1089) прямо)
    # текст мысли канонически сохранён здесь (ACCEPTABLE ADAPTATION)
    th "I wonder how Siesta is doing…? Maybe I should go check on her.{#ch4.6_th_013}"
    # JA: （シエスタはどうしてるかな……。 / 　ちょっと様子を見に行くか）

    # ==== SCENE 1089 ====
    # [BG +64 → id(64)]
    $ fade_fx("id(64)", new_music="t6")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +412 → s 5]
    $ show_sprites(("s 5"))
    # [waitSEStop waitSEStop(null, true)] — не портируется
    voice "ch4.6_s_047"
    s "Good evening, Siesta."
    # JA[8565]: こんばんは、シエスタ。
    voice "ch4.6_si_007"
    si "Eh…? Mr. Saito?"
    # JA[14240]: えっ……サイトさん？
    # [lay5 x=224]
    # [lay2 +546 → si 6 happy]
    $ show_sprites(("si 6 happy", "s 5"))
    voice "ch4.6_si_008"
    si "…Wah! Mr. Saito! Please, come right in!"
    # JA[14241]: ……わあっ、サイトさんっ！ / どうぞ、遠慮なくお入りくださいっ！
    $ update_sympathy(20, char_key="siesta")
    # [lay2 hide]
    $ show_sprites(("s 5"))
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [BG +70 → id(70)]
    $ fade_fx("id(70)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay2 +550 → si 6 sad]
    $ show_sprites(("si 6 sad"))
    voice "ch4.6_si_009"
    si "Um, um, Mr. Saito, I'm sorry! I came along on my own without warning today…"
    # JA[14242]: あ、あのっ、サイトさんゴメンなさい。 / 今日は、勝手について来てしまったりして。
    # [lay2 x=-96]
    # [lay5 +445 → s 6]
    $ show_sprites(("si 6 sad", "s 6"))
    voice "ch4.6_s_048"
    s "N-no, it's already all settled. Don't worry about it. I was just… startled, that's all."
    # JA[8566]: い、いや、もう済んだことだし。 / それは大丈夫だよ。 / ただ、ビックリしたけどね。
    # [lay2 +544 → si 6]
    $ show_sprites(("si 6", "s 6"))
    voice "ch4.6_si_010"
    si "For a while there, the Bomb User showed up and I thought… I didn't know what would happen."
    # JA[14243]: 一時は、爆弾使いが現われたりして、 / どうなるかと思いましたけど。
    # [lay2 +546 → si 6 happy]
    $ show_sprites(("si 6 happy", "s 6"))
    voice "ch4.6_si_011"
    si "I'm so glad Mr. Saito won his fight with the Bomb User and came through it safely."
    # JA[14244]: サイトさんが爆弾使いとの戦いに勝って、 / 無事で、ホントに良かったです。
    # [lay2 +552 → si 6 shy]
    $ show_sprites(("si 6 shy", "s 6"))
    voice "ch4.6_si_012"
    si "Even after we evacuated, I kept praying that Mr. Saito would be safe. You know?"
    # JA[14245]: わたし、避難してからもずっとサイトさんが / 無事でいますようにって、 / お祈りしてたんですよ？
    # [lay5 +420 → s 5 shy]
    $ show_sprites(("si 6 shy", "s 5 shy"))
    voice "ch4.6_s_049"
    s "Ahh, that's… kind of embarrassing…"
    # JA[8567]: いやあ、なんだか照れるなぁ……。
    # [lay2 +544 → si 6]
    $ show_sprites(("si 6", "s 5 shy"))
    voice "ch4.6_si_013"
    si "But Miss Valliere really does know Her Majesty personally, don't you?"
    # JA[14246]: でも、ミス・ヴァリエールは本当に / 女王陛下とお知り合いだったんですね。
    # [lay5 +412 → s 5]
    $ show_sprites(("si 6", "s 5"))
    voice "ch4.6_s_050"
    s "Yeah, I was surprised at first, too. Apparently, back when we were little, we used to play together."
    # JA[8568]: うん、俺もはじめはびっくりしたけど。 / 何でも幼いときは遊び友達だったんだって。
    # [lay2 +550 → si 6 sad]
    $ show_sprites(("si 6 sad", "s 5"))
    voice "ch4.6_si_014"
    si "I keep wondering. Why was I born a commoner, I wonder?"
    # JA[14247]: わたし、思うんです。 / なんで、平民に生まれたんだろうって。
    # [lay5 +418 → s 5 sad]
    $ show_sprites(("si 6 sad", "s 5 sad"))
    voice "ch4.6_s_051"
    s "….{#ch4.6_v8569}"
    # JA[8569]: ……。
    # [lay2 +548 → si 6 angry]
    $ show_sprites(("si 6 angry", "s 5 sad"))
    voice "ch4.6_si_015"
    si "Doesn't it seem strange that your status is decided the moment you're born?"
    # JA[14248]: 生まれた時に身分が決まるなんて、 / おかしいと思いませんか？
    # [lay2 +550 → si 6 sad]
    $ show_sprites(("si 6 sad", "s 5 sad"))
    voice "ch4.6_si_016"
    si "No, I do realize I'm not in any position to say such things."
    # JA[14249]: いえ、わたしがそんなことを言える立場では / ないのは分かってるつもりです。
    # [lay2 +552 → si 6 shy]
    $ show_sprites(("si 6 shy", "s 5 sad"))
    voice "ch4.6_si_017"
    si "But perhaps because I'm that sort of person, I was drawn to you, Mr. Saito."
    # JA[14250]: でも、そんなわたしだから、 / サイトさんに惹かれたのかもしれませんね。
    # [lay5 +451 → s 6 sad]
    $ show_sprites(("si 6 shy", "s 6 sad"))
    voice "ch4.6_s_052"
    s "To me?"
    # JA[8570]: 俺に？
    # [lay2 +544 → si 6]
    $ show_sprites(("si 6", "s 6 sad"))
    voice "ch4.6_si_018"
    si "You're a free man, Mr. Saito. You're not bound by anything."
    # JA[14251]: サイトさんは自由なんです。 / 何にもとらわれない。
    voice "ch4.6_si_019"
    si "You overcome everything that we, who consider it perfectly normal, brush off as nothing. You're an amazing person."
    # JA[14252]: わたし達がこれは普通と思ってちゅうちょ / してることをなんでも乗り越えてしまう。 / すごい人です。
    # [lay5 +445 → s 6]
    $ show_sprites(("si 6", "s 6"))
    voice "ch4.6_s_053"
    s "D-do you think so?{#ch4.6_v8571}"
    # JA[8571]: そ、そうかな？
    # [lay2 +546 → si 6 happy]
    $ show_sprites(("si 6 happy", "s 6"))
    voice "ch4.6_si_020"
    si "Yes. It must be so."
    # JA[14253]: そうです。 / そうに決まってます。
    # [lay5 +418 → s 5 sad]
    $ show_sprites(("si 6 happy", "s 5 sad"))
    th "I think she's exaggerating… but those earnest eyes really do cut deep.{#ch4.6_th_014}"
    # JA: （それは買いかぶりだと思うんだけどな……。 / 　でも、この純粋な視線が痛い）

    # ---- 【選択肢】 ----
    menu:
        "That's not true at all.":
            # JA: そんなことないよ
            # ==== SCENE 1090 ====
            # [lay2 +546 → si 6 happy]
            # [lay5 +418 → s 5 sad]
            play music t6 fadein 1.0
            # [BG +70 → id(70)]
            $ fade_fx("id(70)")
            # [lay5 +412 → s 5]
    $ show_sprites(("si 6 happy", "s 5"))
            voice "ch4.6_s_054"
            s "That's not true at all. You're exaggerating, Siesta."
            # JA[8572]: そんなことないよ。 / それはシエスタの買いかぶりさ。
            # [lay2 +544 → si 6]
    $ show_sprites(("si 6", "s 5"))
            voice "ch4.6_si_021"
            si "Really?{#ch4.6_v14254}"
            # JA[14254]: そうですか？
            voice "ch4.6_s_055"
            s "That's right. I'm neither a superhero nor a mage."
            # JA[8573]: そうだよ。 / 俺はスーパーマンでもなければ、 / 魔法使いでもないんだ。
            # [lay5 +414 → s 5 happy]
    $ show_sprites(("si 6", "s 5 happy"))
            voice "ch4.6_s_056"
            s "I suppose. Just a guy without any common sense?"
            # JA[8574]: そうだなぁ。 / ただの常識知らずってところかな？
            # [lay2 +550 → si 6 sad]
    $ show_sprites(("si 6 sad", "s 5 happy"))
            voice "ch4.6_si_022"
            si "Without common sense… is it?"
            # JA[14255]: 常識知らず……ですか。
        "Would it be normal in my world?":
            # JA: 俺の世界だったら普通かな？
            # ==== SCENE 1091 ====
            # [lay2 +546 → si 6 happy]
    $ show_sprites(("si 6 happy", "s 5 happy"))
            # [lay5 +418 → s 5 sad]
    $ show_sprites(("si 6 happy", "s 5 sad"))
            play music t6 fadein 1.0
            # [BG +70 → id(70)]
            $ fade_fx("id(70)")
            # [lay5 +412 → s 5]
    $ show_sprites(("si 6 happy", "s 5"))
            voice "ch4.6_s_057"
            s "In my world? It'd be normal, I suppose. There are still places with class systems, but mostly it's an ordinary thing."
            # JA[8575]: 俺の世界だったら普通かな？ / まぁ、まだ身分制度が残ってる / ところもあるけど、大体普通のことだよ。
            # [lay2 +544 → si 6]
    $ show_sprites(("si 6", "s 5"))
            voice "ch4.6_si_023"
            si "Is that so…? I wish I could be born into your world. It must be a wonderful place, right?"
            # JA[14256]: そうなんですか……。 / サイトさんの世界に生まれてみたかったです。 / きっとすばらしい世界なんでしょうね？
            $ update_sympathy(10, char_key="siesta")
            # [lay5 +451 → s 6 sad]
    $ show_sprites(("si 6", "s 6 sad"))
            voice "ch4.6_s_058"
            s "I wonder? My world is my own, and it has problems of its own. I think problems are the same everywhere."
            # JA[8576]: そうかな？ / 俺の世界は俺の世界で、別の問題はあるよ。 / 問題があるのは、どこでも同じだと思うんだ。
            # [lay2 +550 → si 6 sad]
    $ show_sprites(("si 6 sad", "s 6 sad"))
            voice "ch4.6_si_024"
            si "The same everywhere…?"
            # JA[14257]: どこでも同じ……ですか。
        "It was because of Louise's power.":
            # JA: ルイズの力があったからだよ
            # ==== SCENE 1092 ====
            # [lay2 +546 → si 6 happy]
    $ show_sprites(("si 6 happy", "s 6 sad"))
            # [lay5 +418 → s 5 sad]
    $ show_sprites(("si 6 happy", "s 5 sad"))
            play music t6 fadein 1.0
            # [BG +70 → id(70)]
            $ fade_fx("id(70)")
            # [lay5 +412 → s 5]
    $ show_sprites(("si 6 happy", "s 5"))
            voice "ch4.6_s_059"
            s "I think it was because of Louise's power. Honestly, the only reason I've survived this long is because of Louise's power."
            # JA[8577]: ルイズの力があったからだと思う。 / 正直、ここまで生きてこれたのも、 / ルイズの力があるからだし。
            # [lay2 +550 → si 6 sad]
    $ show_sprites(("si 6 sad", "s 5"))
            voice "ch4.6_si_025"
            si "Miss Valliere's power…?"
            # JA[14258]: ミス・ヴァリエールの力……ですか。
            $ update_sympathy(-10, char_key="siesta")

    # ==== SCENE 1093 (переход после вариантов) ====
    # [lay2 +550 → si 6 sad]
    # [lay5 +414 → s 5 happy]
    $ show_sprites(("si 6 sad", "s 5 happy"))
    play music t6 fadein 1.0
    # [BG +70 → id(70)]
    $ fade_fx("id(70)")
    # [lay5 +445 → s 6]
    $ show_sprites(("si 6 sad", "s 6"))
    voice "ch4.6_s_060"
    s "But you've got an amazing power too, Siesta."
    # JA[8578]: でも、シエスタだって、 / すごい力を持ってるんだぜ。
    # [lay2 +544 → si 6]
    $ show_sprites(("si 6", "s 6"))
    voice "ch4.6_si_026"
    si "Really?{#ch4.6_v14259}"
    # JA[14259]: そうですか？
    # [lay5 +447 → s 6 happy]
    $ show_sprites(("si 6", "s 6 happy"))
    voice "ch4.6_s_061"
    s "Your smile. That's already full of charm."
    # JA[8579]: 笑顔。 / それはもう、魅力たっぷりだよ。
    voice "ch4.6_si_027"
    si "Is that so?{#ch4.6_v14260}"
    # JA[14260]: そうでしょうか？
    # [lay5 +412 → s 5]
    $ show_sprites(("si 6", "s 5"))
    voice "ch4.6_s_062"
    s "You can be confident. I guarantee it. Siesta's smile is the best in the world."
    # JA[8580]: 自信もっていいよ。 / 俺が保証する。 / シエスタの笑顔は世界一だって。
    # [lay2 +552 → si 6 shy]
    $ show_sprites(("si 6 shy", "s 5"))
    voice "ch4.6_si_028"
    si "Well… Mr. Saito, honestly."
    # JA[14261]: まぁ……、サイトさんったら。
    # [lay5 +414 → s 5 happy]
    $ show_sprites(("si 6 shy", "s 5 happy"))
    voice "ch4.6_s_063"
    s "You don't have to care about status. Siesta has something wonderful, so you can rest easy."
    # JA[8581]: 身分なんて気にしなくたって、 / シエスタはすごいものを持ってるんだから、 / 安心していいよ。
    # [lay5 +412 → s 5]
    $ show_sprites(("si 6 shy", "s 5"))
    voice "ch4.6_s_064"
    s "You'll absolutely be able to be happy."
    # JA[8582]: 絶対に幸せになれる。
    # [lay2 +546 → si 6 happy]
    $ show_sprites(("si 6 happy", "s 5"))
    voice "ch4.6_si_029"
    si "Yes, I understand. Thank you."
    # JA[14262]: はい、分かりました。 / ありがとうございます。
    stop music fadeout 1.0
    # [lay2 hide]
    $ show_sprites(("s 5"))
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [COFFEE] → pause(1.0)
    $ pause(1.0)

    # [移動] → next(269): сцена 269 — глава 5, НЕ портируется
    return

label date_haruna_ch4_6:
    # ==== SCENE 267 (мост): в PS2 не проигрывается (dateDone → next(1094) прямо)
    # текст мысли канонически сохранён здесь (ACCEPTABLE ADAPTATION)
    th "Is Haruna all right? Maybe I should go check on her…{#ch4.6_th_015}"
    # JA: （春奈は大丈夫かな？ / 　ちょっと様子を見てみるか……）

    # ==== SCENE 1094 ====
    # [BG +64 → id(64)]
    $ fade_fx("id(64)", new_music="t10")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    voice "ch4.6_ha_007"
    ha "Aaaaah-aaaaaah. Aaaah-aaah."
    # JA[1639]: アーアアアーアアアー。 / アーアーアーアー。
    th "Is that singing? It must be coming from Haruna's room.{#ch4.6_th_016}"
    # JA: （これは歌声？ / 　春奈の部屋からだよな）
    voice "ch4.6_s_065"
    s "Haruna?{#ch4.6_v8583}"
    # JA[8583]: 春奈？
    # [lay7 hide]
    # [lay5 hide]
    # [BG hide]
    $ fade_fx("black")
    # [BG +70 → id(70)]
    $ fade_fx("id(70)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay7 +977 → ha 3 angry]
    $ show_sprites(("ha 3 angry"))
    voice "ch4.6_ha_008"
    ha "Kyaa! Mr. Hiraga! You were right there…"
    # JA[1640]: きゃっ。 / 平賀くん。 / そこにいたんだ……。
    $ update_sympathy(20, char_key="haruna")
    # [lay7 +973 → ha 3]
    $ show_sprites(("ha 3"))
    # [lay5 +412 → s 5]
    $ show_sprites(("ha 3", "s 5"))
    voice "ch4.6_s_066"
    s "I was just… checking on you. …Was I in the way?"
    # JA[8584]: ちょっと、様子を見に来たんだけど。 / ……邪魔だったかな？
    voice "ch4.6_ha_009"
    ha "No, no. It's fine."
    # JA[1641]: ううん。 / 大丈夫だよ。
    voice "ch4.6_s_067"
    s "So, what song were you singing?"
    # JA[8585]: それで、なんの曲を歌ってたの？
    voice "ch4.6_ha_010"
    ha "The song we're supposed to sing at the next club meeting."
    # JA[1642]: 今度の部活で歌うはずだった曲。
    # [lay7 +981 → ha 3 shy]
    $ show_sprites(("ha 3 shy", "s 5"))
    voice "ch4.6_ha_011"
    ha "But I didn't expect you to hear it… It's a little embarrassing."
    # JA[1643]: でも、平賀くんに聞かれるとは / 思ってなかったから……。 / ちょっと恥ずかしいな。
    # [lay5 +445 → s 6]
    $ show_sprites(("ha 3 shy", "s 6"))
    voice "ch4.6_s_068"
    s "No, you were good. Come on, I can't sing at all."
    # JA[8586]: いや、うまかったよ。 / ほら、俺、全然歌が駄目だし。
    voice "ch4.6_ha_012"
    ha "That's not true at all… Ugh, so embarrassing."
    # JA[1644]: そんなことないよぅ……。 / もう、恥ずかしいなぁ。
    # [lay5 +412 → s 5]
    $ show_sprites(("ha 3 shy", "s 5"))
    voice "ch4.6_s_069"
    s "Haruna, you were in the choir club?"
    # JA[8587]: 春奈って合唱部だったんだ？
    # [lay7 +973 → ha 3]
    $ show_sprites(("ha 3", "s 5"))
    voice "ch4.6_ha_013"
    ha "Yes, that's right. But I'm not sure I'm good enough to be a main member."
    # JA[1645]: うん、そう。 / でも、メインメンバーになれるほど / 上手ではないかな？
    # [lay5 +445 → s 6]
    $ show_sprites(("ha 3", "s 6"))
    voice "ch4.6_s_070"
    s "I don't know. If it were me, I think I'd definitely make it as a main member."
    # JA[8588]: そうかなぁ。 / 俺だったら、絶対メインメンバーに / 入れると思うけどなぁ。
    # [lay7 +975 → ha 3 happy]
    $ show_sprites(("ha 3 happy", "s 6"))
    voice "ch4.6_ha_014"
    ha "Thank you, Mr. Hiraga."
    # JA[1646]: ありがとう、平賀くん。
    # [lay5 +412 → s 5]
    $ show_sprites(("ha 3 happy", "s 5"))
    voice "ch4.6_s_071"
    s "Does the choir hold competitions?"
    # JA[8589]: 合唱って大会があるの？
    # [lay7 +973 → ha 3]
    $ show_sprites(("ha 3", "s 5"))
    voice "ch4.6_ha_015"
    ha "Yes, there are several. The big ones have a regional round, a prefectural round, and then the national one."
    # JA[1647]: うん、大会はいくつかあるよ。 / 大きな大会だと、地区大会があって、 / 県大会があって、全国大会があるの。
    voice "ch4.6_s_072"
    s "Heh, like a sports club."
    # JA[8590]: へー、運動部みたいだな。
    voice "ch4.6_ha_016"
    ha "Of course there are smaller ones too, but mostly everyone pushes for the big competitions, you know?"
    # JA[1648]: もちろん、小さい大会もあるけど、 / 大抵は大きな大会を目標に頑張ってる / って感じかな？
    # [lay7 +979 → ha 3 sad]
    $ show_sprites(("ha 3 sad", "s 5"))
    voice "ch4.6_ha_017"
    ha "But entering this year's competitions… is out of the question, right…"
    # JA[1649]: でも、今年の大会の参加は、無理だよね……。
    # [lay5 +418 → s 5 sad]
    $ show_sprites(("ha 3 sad", "s 5 sad"))
    voice "ch4.6_s_073"
    s "….{#ch4.6_v8591}"
    # JA[8591]: ……。
    # [lay5 +445 → s 6]
    $ show_sprites(("ha 3 sad", "s 6"))
    voice "ch4.6_s_074"
    s "R-right. Haruna, do you go to karaoke?"
    # JA[8592]: そ、そうだ。 / 春奈ってカラオケに行くの？
    # [lay7 +973 → ha 3]
    $ show_sprites(("ha 3", "s 6"))
    voice "ch4.6_ha_018"
    ha "Karaoke? Hmm, sometimes… maybe. How about you, Mr. Hiraga?"
    # JA[1650]: カラオケ？ / うーん、たまに……かな。 / 平賀くんは？
    # [lay5 +412 → s 5]
    $ show_sprites(("ha 3", "s 5"))
    voice "ch4.6_s_075"
    s "Me too, sometimes…"
    # JA[8593]: 俺もたまに……。
    voice "ch4.6_ha_019"
    ha "What kind of songs do you sing, Mr. Hiraga?"
    # JA[1651]: 平賀くんはどんな歌を歌うの？
    # [lay5 +445 → s 6]
    $ show_sprites(("ha 3", "s 6"))
    voice "ch4.6_s_076"
    s "Hmm… let me think…"
    # JA[8594]: そうだなぁ……。

    # ---- 【選択肢】 ----
    menu:
        "Japanese songs, I guess.":
            # JA: 邦楽かなぁ
            # ==== SCENE 1095 ====
            # [lay7 +973 → ha 3]
            # [lay5 +445 → s 6]
            play music t10 fadein 1.0
            # [BG +70 → id(70)]
            $ fade_fx("id(70)")
            # [lay5 +414 → s 5 happy]
    $ show_sprites(("ha 3", "s 5 happy"))
            voice "ch4.6_s_077"
            s "Japanese songs, I guess. There are more songs everyone can get excited about together."
            # JA[8595]: やっぱり邦楽かなぁ。 / みんなで盛り上がれる歌が多いしね。
            # [lay7 +979 → ha 3 sad]
    $ show_sprites(("ha 3 sad", "s 5 happy"))
            voice "ch4.6_ha_020"
            ha "Hmm, I see. I can never quite keep up with popular songs."
            # JA[1652]: ふーん、そうなんだ。 / 私、流行の歌ってどうもついていけなくって。
            # [lay5 +412 → s 5]
    $ show_sprites(("ha 3 sad", "s 5"))
            voice "ch4.6_s_078"
            s "At a convenience store, songs play on the pipe radio, and if you listen, you pick them up naturally."
            # JA[8596]: コンビニだったら有線で曲が流れるし、 / それを聞いてれば自然と覚えるって。
            # [lay7 +975 → ha 3 happy]
    $ show_sprites(("ha 3 happy", "s 5"))
            voice "ch4.6_ha_021"
            ha "Heh. That's a bit of life wisdom, isn't it?"
            # JA[1653]: へー。 / それは生活の知恵だね。
            # [lay5 +447 → s 6 happy]
    $ show_sprites(("ha 3 happy", "s 6 happy"))
            voice "ch4.6_s_079"
            s "Haha."
            # JA[8597]: はははっ。
        "Western songs, maybe.":
            # JA: 洋楽かな
            # ==== SCENE 1096 ====
            # [lay7 +973 → ha 3]
    $ show_sprites(("ha 3", "s 6 happy"))
            # [lay5 +445 → s 6]
    $ show_sprites(("ha 3", "s 6"))
            play music t10 fadein 1.0
            # [BG +70 → id(70)]
            $ fade_fx("id(70)")
            # [lay5 +412 → s 5]
    $ show_sprites(("ha 3", "s 5"))
            voice "ch4.6_s_080"
            s "Actually, I sing Western music."
            # JA[8598]: 実は洋楽を歌ってるんだ。
            # [lay7 +975 → ha 3 happy]
    $ show_sprites(("ha 3 happy", "s 5"))
            voice "ch4.6_ha_022"
            ha "Eh, you sing in English? You're good at English, Mr. Hiraga?"
            # JA[1654]: え、英語で歌うんだよね。 / 平賀くん、英語得意なんだ？
            $ update_sympathy(10, char_key="haruna")
            # [lay5 +445 → s 6]
    $ show_sprites(("ha 3 happy", "s 6"))
            voice "ch4.6_s_081"
            s "N-not really. I mean, I sort of understand what it means…"
            # JA[8599]: いやー。 / 意味はそれっぽく理解してるつもりだけど……、
            # [lay5 +447 → s 6 happy]
    $ show_sprites(("ha 3 happy", "s 6 happy"))
            voice "ch4.6_s_082"
            s "In the end, I'm probably just copying the intonation and singing it as if I know what I'm doing, right?"
            # JA[8600]: 結局はイントネーションをまねしながら、 / それっぽく歌ってるだけかな？
            # [lay7 +973 → ha 3]
    $ show_sprites(("ha 3", "s 6 happy"))
            voice "ch4.6_ha_023"
            ha "Even so, that's amazing."
            # JA[1655]: それでもすごいよ。
        "Actually, I mostly just listen.":
            # JA: 実は聞いてるだけ
            # ==== SCENE 1097 ====
            # [lay7 +973 → ha 3]
            # [lay5 +445 → s 6]
    $ show_sprites(("ha 3", "s 6"))
            play music t10 fadein 1.0
            # [BG +70 → id(70)]
            $ fade_fx("id(70)")
            # [lay5 +451 → s 6 sad]
    $ show_sprites(("ha 3", "s 6 sad"))
            voice "ch4.6_s_083"
            s "Actually, I mostly just listen. I don't sing much…"
            # JA[8601]: 実は聞いてるのがほとんど。 / あまり歌ってないなぁ……。
            # [lay7 +979 → ha 3 sad]
    $ show_sprites(("ha 3 sad", "s 6 sad"))
            voice "ch4.6_ha_024"
            ha "That's a waste, though. You came all the way to sing."
            # JA[1656]: それってもったいないよ。 / せっかく歌いに来たんだし。
            $ update_sympathy(-10, char_key="haruna")
            # [lay5 +418 → s 5 sad]
    $ show_sprites(("ha 3 sad", "s 5 sad"))
            voice "ch4.6_s_084"
            s "I just don't feel confident about singing."
            # JA[8602]: 歌ってどうも自信がなくて。
            # [lay7 +973 → ha 3]
    $ show_sprites(("ha 3", "s 5 sad"))
            voice "ch4.6_ha_025"
            ha "They say if you start by singing along with other people, you pick up a sense of pitch. How about we try singing together?"
            # JA[1657]: 他人に合わせて歌うことから始めれば、 / 音感がついてくるっていうよ。 / 一緒に歌ってみるのはどうかな？
            # [lay5 +445 → s 6]
    $ show_sprites(("ha 3", "s 6"))
            voice "ch4.6_s_085"
            s "D-do you think so?{#ch4.6_v8603}"
            # JA[8603]: そ、そうかな？

    # ==== SCENE 1098 (переход после вариантов) ====
    # [lay7 +975 → ha 3 happy]
    $ show_sprites(("ha 3 happy", "s 6"))
    # [lay5 +447 → s 6 happy]
    $ show_sprites(("ha 3 happy", "s 6 happy"))
    play music t10 fadein 1.0
    # [BG +70 → id(70)]
    $ fade_fx("id(70)")
    # [lay7 +973 → ha 3]
    $ show_sprites(("ha 3", "s 6 happy"))
    voice "ch4.6_ha_026"
    ha "Mr. Hiraga."
    # JA[1658]: 平賀くん。
    # [lay5 +412 → s 5]
    $ show_sprites(("ha 3", "s 5"))
    voice "ch4.6_s_086"
    s "Hm?{#ch4.6_v8604}"
    # JA[8604]: うん？
    # [lay7 +975 → ha 3 happy]
    $ show_sprites(("ha 3 happy", "s 5"))
    voice "ch4.6_ha_027"
    ha "When we go back to Japan, let's go to karaoke together, okay?"
    # JA[1659]: 日本に帰れたら、一緒にカラオケ行こうね。
    # [lay5 +414 → s 5 happy]
    $ show_sprites(("ha 3 happy", "s 5 happy"))
    voice "ch4.6_s_087"
    s "Yeah. Absolutely, we'll go."
    # JA[8605]: ああ。 / 絶対行こうな。
    voice "ch4.6_ha_028"
    ha "Yes. It's a promise."
    # JA[1660]: うん。 / 約束だよ。
    stop music fadeout 1.0
    # [lay7 hide]
    $ show_sprites(("s 5 happy"))
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [COFFEE] → pause(1.0)
    $ pause(1.0)

    # [移動] → next(269): сцена 269 — глава 5, НЕ портируется
    return

label date_henrietta_ch4_6:
    # ==== SCENE 268 (мост): в PS2 не проигрывается (dateDone → next(1099) прямо)
    # текст мысли канонически сохранён здесь (ACCEPTABLE ADAPTATION)
    th "Since I'm here anyway, maybe I'll take a walk around the castle…{#ch4.6_th_017}"
    # JA: （せっかくだから、お城の中でも / 　歩いてみるか……）

    # ==== SCENE 1099 ====
    # [BG +64 → id(64)]
    $ fade_fx("id(64)", new_music="t20")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +418 → s 5 sad]
    $ show_sprites(("s 5 sad"))
    voice "ch4.6_s_088"
    s "…Hmm~."
    # JA[8606]: ……う～ん。
    # [lay5 x=224]
    # [lay19 +940 → d 1]
    $ show_sprites(("d 1", "s 5 sad"))
    voice "ch4.6_d_009"
    d "What's wrong, partner? Going round and round the same spot."
    # JA[1209]: どうした、相棒？ / 同じところをぐるぐる回って。
    # [lay5 +451 → s 6 sad]
    $ show_sprites(("d 1", "s 6 sad"))
    voice "ch4.6_s_089"
    s "I can't find my way back to my own room…"
    # JA[8607]: 自分の部屋にたどり着けない……。
    # [lay19 +946 → d 1 sad]
    $ show_sprites(("d 1 sad", "s 6 sad"))
    voice "ch4.6_d_010"
    d "Hey, hey, hey, hey! Partner, that's too pitiful by any measure."
    # JA[1210]: おいおいおいおいっ。 / 相棒、そりゃいくらなんでも情けなさすぎだろ。
    # [lay19 +942 → d 1 happy]
    $ show_sprites(("d 1 happy", "s 6 sad"))
    voice "ch4.6_d_011"
    d "So how about we just camp out somewhere around here? By morning, someone will pick us up, right?"
    # JA[1211]: そいじゃあ、どこかそこいら辺で / 野宿でもすっか？ / 朝になれば、誰かが拾ってくれるだろ？
    # [lay5 +416 → s 5 angry]
    $ show_sprites(("d 1 happy", "s 5 angry"))
    voice "ch4.6_s_090"
    s "Are you kidding me? They went and prepared a bed for me, and you want me to camp out? No way."
    # JA[8608]: 冗談じゃねーって。 / せっかくベッドも用意してもらったのに、 / 野宿なんてありえないだろ？
    # [lay5 hide]
    $ show_sprites(("d 1 happy"))
    # [lay19 hide]
    $ show_sprites()
    stop music fadeout 1.0
    play music t9 fadein 1.0
    voice "ch4.6_h_008"
    unk_h "Oh…? That voice…"
    # JA[321]: あら……その声はっ……。
    # [lay5 +418 → s 5 sad]
    $ show_sprites(("s 5 sad"))
    voice "ch4.6_s_091"
    s "Eh?{#ch4.6_v8609}"
    # JA[8609]: え？
    # [lay5 x=224]
    # [lay8 +788 → h 2 happy]
    $ show_sprites(("h 2 happy", "s 5 sad"))
    voice "ch4.6_h_009"
    h "Well, as I thought! Good evening, familiar."
    # JA[322]: まぁ、やっぱり！ / こんばんは、使い魔さん。
    $ update_sympathy(50, char_key="henrietta")
    # [lay5 +412 → s 5]
    $ show_sprites(("h 2 happy", "s 5"))
    voice "ch4.6_s_092"
    s "Good evening, Your Highness."
    # JA[8610]: こんばんは、お姫さま。
    # [lay8 +786 → h 2]
    $ show_sprites(("h 2", "s 5"))
    voice "ch4.6_h_010"
    h "What is the matter? Walking about the castle in the middle of the night like this…"
    # JA[323]: どうしたんですか？ / こんな夜更けに城内を歩いてるなんて。
    # [lay5 +451 → s 6 sad]
    $ show_sprites(("h 2", "s 6 sad"))
    voice "ch4.6_s_093"
    s "N-no, it's, um…"
    # JA[8611]: いえ、その、あの。
    # [lay19 +946 → d 1 sad]
    $ show_sprites(("h 2", "d 1 sad", "s 6 sad"))
    voice "ch4.6_d_012"
    d "Listen, Your Majesty. It seems my poor partner has gotten himself lost in the castle."
    # JA[1212]: 聞いてくださいよ、女王陛下。 / あわれな相棒が、城の中で迷子に / なっちまったみたいなんです。
    # [lay8 +788 → h 2 happy]
    $ show_sprites(("h 2 happy", "d 1 sad", "s 6 sad"))
    voice "ch4.6_h_011"
    h "Oh my. Does this sword talk?"
    # JA[324]: あらあら。 / この剣はしゃべるのかしら？
    # [lay19 +948 → d 1 shy]
    $ show_sprites(("h 2 happy", "d 1 shy", "s 6 sad"))
    voice "ch4.6_d_013"
    d "What an honor for a nobody like me to have your attention. My name is Delphlinger."
    # JA[1213]: 俺っちに気をかけてくれるとは / なんとすばらしい。 / デルフリンガーと申します。
    # [lay19 hide]
    $ show_sprites(("h 2 happy", "s 6 sad"))
    # [lay5 +416 → s 5 angry]
    $ show_sprites(("h 2 happy", "s 5 angry"))
    voice "ch4.6_s_094"
    s "Hey! Delphy, don't say things you shouldn't!"
    # JA[8612]: こら！ / デルフ、余計なことを言うなって。
    # [lay8 +786 → h 2]
    $ show_sprites(("h 2", "s 5 angry"))
    voice "ch4.6_h_012"
    h "Well, Louise seems to gather interesting people around her. I envy that."
    # JA[325]: まあ、ルイズの周りは面白い人が多くて、 / うらやましいです。
    # [lay8 +788 → h 2 happy]
    $ show_sprites(("h 2 happy", "s 5 angry"))
    voice "ch4.6_h_013"
    h "Very well. Then I shall show you the way. Do make sure you follow me, won't you?"
    # JA[326]: 分かりました。 / それでは案内しますわ。 / ちゃんと、わたくしに付いてきてくださいね？
    # [lay5 +412 → s 5]
    $ show_sprites(("h 2 happy", "s 5"))
    voice "ch4.6_s_095"
    s "Y-yes. Thank you."
    # JA[8613]: は、はい。 / よろしくお願いします。
    # [lay8 hide]
    $ show_sprites(("s 5"))
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [BG +90 → sky_night]
    $ fade_fx("sky_night")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    th "….\n….\n….{#ch4.6_th_018}"
    # JA: ………。 / ……。 / …。
    # [BG hide]
    $ fade_fx("black")
    # [BG +64 → id(64)]
    $ fade_fx("id(64)")
    # [TRANS   trans("crossfade", 1000)] — переход выполняется fade_fx
    # [lay5 +412 → s 5]
    $ show_sprites(("s 5"))
    # [lay8 +792 → h 2 sad]
    $ show_sprites(("h 2 sad", "s 5"))
    voice "ch4.6_h_014"
    h "Familiar. Louise looks tough, but she is a fragile girl who needs someone to support her."
    # JA[327]: 使い魔さん。 / ルイズは、ああ見えて誰かが / 支えてあげないといけない弱い子だから。
    # [lay8 +786 → h 2]
    $ show_sprites(("h 2", "s 5"))
    voice "ch4.6_h_015"
    h "Please keep being good to Louise from now on, yes?"
    # JA[328]: ルイズとは、これからも仲良くしてやって / くださいね？
    # [lay5 +451 → s 6 sad]
    $ show_sprites(("h 2", "s 6 sad"))
    voice "ch4.6_s_096"
    s "…That Louise? Huh. No matter how you look at her, she doesn't seem fragile at all."
    # JA[8614]: ……あのルイズが、ですか？ / ふーん、どう見ても弱い子には見えないけど。
    # [lay8 +792 → h 2 sad]
    $ show_sprites(("h 2 sad", "s 6 sad"))
    voice "ch4.6_h_016"
    h "It is true. You can plainly see how she is taken aback by the power of the Void she holds."
    # JA[329]: 本当です。 / 正直、虚無の力を手にして戸惑っている姿が / 見て分かります。
    # [lay8 +786 → h 2]
    $ show_sprites(("h 2", "s 6 sad"))
    voice "ch4.6_h_017"
    h "Louise doesn't say so herself, but she must be fighting her fears every single day."
    # JA[330]: ルイズは自らあまり言いませんが、 / 本当は日々不安と戦ってるはずなのです。
    # [lay5 +412 → s 5]
    $ show_sprites(("h 2", "s 5"))
    voice "ch4.6_s_097"
    s "I understand. If Your Highness says so, I want to believe it… I want to…"
    # JA[8615]: 分かりました。 / お姫さまがそこまでいうのなら、信じる…… / ようにしたいなぁ……。
    # [lay8 +788 → h 2 happy]
    $ show_sprites(("h 2 happy", "s 5"))
    voice "ch4.6_h_018"
    h "Well, you are honest, aren't you, familiar."
    # JA[331]: まぁ、使い魔さんって正直なんですね。
    # [lay5 +445 → s 6]
    $ show_sprites(("h 2 happy", "s 6"))
    voice "ch4.6_s_098"
    s "Ahhh…"
    # JA[8616]: いやぁ……。
    # [lay8 +792 → h 2 sad]
    $ show_sprites(("h 2 sad", "s 6"))
    voice "ch4.6_h_019"
    h "I envy Louise. To have such a kind familiar as you. I am always alone…"
    # JA[332]: ルイズはうらやましいです。 / こんな優しい使い魔さんが居てくれて。 / わたくしはいつも１人ぼっち……。
    # [lay5 +412 → s 5]
    $ show_sprites(("h 2 sad", "s 5"))
    voice "ch4.6_s_099"
    s "Eh? You don't have any other friends?"
    # JA[8617]: え？ / 他に友達はいないんですか？
    # [lay8 +786 → h 2]
    $ show_sprites(("h 2", "s 5"))
    voice "ch4.6_h_020"
    h "No. When one is a queen, even her subjects — everything around her is like an enemy."
    # JA[333]: ええ。 / 女王ともなると、臣下も含めて、周りのすべてが / 敵のようなものですから。
    voice "ch4.6_h_021"
    h "If only I had someone I could open up to, there is so much that would ease my mind…"
    # JA[334]: せめて、気を許せる話し相手でもいれば / 気も紛れる事だって、多々あるのですけどね。
    # [lay5 +418 → s 5 sad]
    $ show_sprites(("h 2", "s 5 sad"))
    voice "ch4.6_s_100"
    s "Everything an enemy… huh. Somehow it makes me feel that being a princess isn't easy either."
    # JA[8618]: すべてが敵……かぁ。 / なんだかお姫さまも楽じゃないなぁって、 / 気がしてきますよ。
    # [lay8 +792 → h 2 sad]
    $ show_sprites(("h 2 sad", "s 5 sad"))
    voice "ch4.6_h_022"
    h "The days change so dizzyingly that even my memories of playing as a child have all faded away."
    # JA[335]: 幼き頃、遊戯にいそしんでいた記憶も / どこかにかすんでしまう程に、 / 日々がめまぐるしく変わっているのです。
    # [lay8 +786 → h 2]
    $ show_sprites(("h 2", "s 5 sad"))
    voice "ch4.6_h_023"
    h "Saying all this to you doesn't change anything, I suppose. I'm sorry — I seem to be complaining."
    # JA[336]: こんな事をあなたに対して言ったところで、 / 何にもならないんですけどね。 / ごめんなさい、なんだか愚痴っぽくて。
    th "Your Highness…{#ch4.6_th_019}"
    # JA: （お姫さま……）

    # ---- 【選択肢】 ----
    menu:
        "I'm on the princess's side.":
            # JA: 俺はお姫さまの味方だ
            # ==== SCENE 1100 ====
            # [lay8 +786 → h 2]
            # [lay5 +418 → s 5 sad]
            play music t9 fadein 1.0
            # [BG +64 → id(64)]
            $ fade_fx("id(64)")
            # [lay5 +451 → s 6 sad]
    $ show_sprites(("h 2", "s 6 sad"))
            voice "ch4.6_s_101"
            s "At the very least, I'm on the princess's side. If anything troublesome comes up, I can lend a hand?"
            # JA[8619]: 俺はその、少なくともお姫さまの味方ですから。 / 何か困ったことがあったら、お力になれますよ？
            # [lay5 +412 → s 5]
    $ show_sprites(("h 2", "s 5"))
            voice "ch4.6_s_102"
            s "Louise probably thinks so too. At least, I believe she does."
            # JA[8620]: たぶん、ルイズもそう思っているはずです。 / 少なくとも、俺はそう信じていますし。
            # [lay8 +788 → h 2 happy]
    $ show_sprites(("h 2 happy", "s 5"))
            voice "ch4.6_h_024"
            h "Well, thank you so much!"
            # JA[337]: まぁ、ありがとうございますっ！
            $ update_sympathy(30, char_key="henrietta")
            # [lay8 +786 → h 2]
    $ show_sprites(("h 2", "s 5"))
            voice "ch4.6_h_025"
            h "But just having you, familiar, listen to my rambling has lightened my heart a good deal."
            # JA[338]: でも、使い魔さんに、このとりとめのない話を / 聞いていただいただけでも、 / 随分と気持ちが楽になりました。
            # [lay5 +451 → s 6 sad]
    $ show_sprites(("h 2", "s 6 sad"))
            voice "ch4.6_s_103"
            s "I see… But if it made the princess happy, that's enough for me."
            # JA[8621]: そうですか……。 / でも、お姫さまが喜んでくれたのならそれで / 充分です。
        "Why not take Louise into your service?":
            # JA: ルイズを側近に迎えたら？
            # ==== SCENE 1101 ====
            # [lay8 +786 → h 2]
            # [lay5 +418 → s 5 sad]
    $ show_sprites(("h 2", "s 5 sad"))
            play music t9 fadein 1.0
            # [BG +64 → id(64)]
            $ fade_fx("id(64)")
            # [lay5 +412 → s 5]
    $ show_sprites(("h 2", "s 5"))
            voice "ch4.6_s_104"
            s "Wouldn't it be better to have Louise stay at the princess's side?"
            # JA[8622]: ルイズの事を、お姫さまの側近に置いてあげる / というのではダメなんですか？
            # [lay8 +792 → h 2 sad]
    $ show_sprites(("h 2 sad", "s 5"))
            voice "ch4.6_h_026"
            h "…In truth, I want nothing more. But that would be far too selfish of me."
            # JA[339]: ……本当はそうしたくて仕方がないのですけど。 / それは余りにもわたくしの身勝手 / というものです。
            # [lay8 +786 → h 2]
    $ show_sprites(("h 2", "s 5"))
            voice "ch4.6_h_027"
            h "I want Louise to live freely."
            # JA[340]: ルイズには、自由に生活して欲しいのです。
            # [lay8 +792 → h 2 sad]
    $ show_sprites(("h 2 sad", "s 5"))
            voice "ch4.6_h_028"
            h "I could never make Louise live day after day imprisoned by stone walls and a magical cage, like I do."
            # JA[341]: こうして日々、石壁と魔法の檻に囚われた生活を / ルイズにもさせるなんて、 / わたくしにはとてもできませんから。
            # [lay5 +451 → s 6 sad]
    $ show_sprites(("h 2 sad", "s 6 sad"))
            voice "ch4.6_s_105"
            s "I see.{#ch4.6_v8623}"
            # JA[8623]: そっかぁ。
        "You have to protect yourself.":
            # JA: 自分の身は自分で守らないと
            # ==== SCENE 1102 ====
            # [lay8 +786 → h 2]
    $ show_sprites(("h 2", "s 6 sad"))
            # [lay5 +418 → s 5 sad]
    $ show_sprites(("h 2", "s 5 sad"))
            play music t9 fadein 1.0
            # [BG +64 → id(64)]
            $ fade_fx("id(64)")
            # [lay5 +451 → s 6 sad]
    $ show_sprites(("h 2", "s 6 sad"))
            voice "ch4.6_s_106"
            s "I shouldn't say this, but doesn't that depend on how Your Highness sees it yourself?"
            # JA[8624]: 俺が言うのも何ですけど、 / それはお姫さま自身の考え方次第 / じゃないですか？
            # [lay8 +786 → h 2]
            voice "ch4.6_h_029"
            h "On how I see it…?"
            # JA[342]: 考え方次第……ですか？
            # [lay5 +412 → s 5]
    $ show_sprites(("h 2", "s 5"))
            voice "ch4.6_s_107"
            s "Unless you reach out to them first, I thought they'd stay enemies forever."
            # JA[8625]: お姫さまから近寄っていかないと、 / いつまでも周りは敵のままじゃないかと / 思うんです。
            # [lay8 +792 → h 2 sad]
    $ show_sprites(("h 2 sad", "s 5"))
            voice "ch4.6_h_030"
            h "….{#ch4.6_v343}"
            # JA[343]: ……。
            $ update_sympathy(-30, char_key="henrietta")
            # [lay5 +418 → s 5 sad]
    $ show_sprites(("h 2 sad", "s 5 sad"))
            voice "ch4.6_s_108"
            s "Well, I'm not a princess, so I don't know what the cause of it is."
            # JA[8626]: そりゃ、俺はお姫さまじゃないから、 / 何が原因なのかは分かりませんけど。
            # [lay5 +412 → s 5]
    $ show_sprites(("h 2 sad", "s 5"))
            voice "ch4.6_s_109"
            s "But at least, the people who fought in the last war must have been fighting for you."
            # JA[8627]: でも、少なくとも前の戦争で戦ってくれた / 人達は、お姫さまのために戦ってくれた / はずです。
            # [lay5 +451 → s 6 sad]
    $ show_sprites(("h 2 sad", "s 6 sad"))
            voice "ch4.6_s_110"
            s "Sorry. I don't even know what I'm saying."
            # JA[8628]: すいません。 / 何言ってるんだか俺にも分からないや。
            # [lay8 +786 → h 2]
    $ show_sprites(("h 2", "s 6 sad"))
            voice "ch4.6_h_031"
            h "No. I've taken that feeling to heart. I must do my best as well."
            # JA[344]: いいえ。 / その気持ち、確かにいただきました。 / わたくしも頑張らなければなりませんね。

    # ==== SCENE 1103 (переход после вариантов) ====
    # [lay8 +786 → h 2]
    # [lay5 +451 → s 6 sad]
    play music t9 fadein 1.0
    # [BG +64 → id(64)]
    $ fade_fx("id(64)")
    # [lay8 +786 → h 2]
    voice "ch4.6_h_032"
    h "Ah, we've arrived. This is your room, familiar."
    # JA[345]: あ、着きましたね。 / ここが使い魔さんのお部屋です。
    # [lay5 +418 → s 5 sad]
    $ show_sprites(("h 2", "s 5 sad"))
    voice "ch4.6_s_111"
    s "Huh, we're already here? …Why was I so lost earlier?"
    # JA[8629]: あれ、もう着いたんですか。 / ……俺、なんであんなに迷ってたんだろ？
    # [lay19 +946 → d 1 sad]
    $ show_sprites(("h 2", "d 1 sad", "s 5 sad"))
    voice "ch4.6_d_014"
    d "Haaah… pitiful, that was."
    # JA[1214]: はぁ～あ、情けねぇこった。
    # [lay19 hide]
    $ show_sprites(("h 2", "s 5 sad"))
    # [lay8 +788 → h 2 happy]
    $ show_sprites(("h 2 happy", "s 5 sad"))
    voice "ch4.6_h_033"
    h "Hehe, there are so many similar places inside the castle. It can't be helped."
    # JA[346]: ふふ、お城の中は似たような場所が / 多いですから、仕方ありませんよ。
    # [lay8 +786 → h 2]
    $ show_sprites(("h 2", "s 5 sad"))
    voice "ch4.6_h_034"
    h "Then good night, familiar."
    # JA[347]: それでは使い魔さん、おやすみなさい。
    # [lay5 +412 → s 5]
    $ show_sprites(("h 2", "s 5"))
    voice "ch4.6_s_112"
    s "Thank you so much. Good night, Your Highness."
    # JA[8630]: どうもありがとうございました。 / おやすみなさい、お姫さま。
    stop music fadeout 1.0
    # [lay8 hide]
    $ show_sprites(("s 5"))
    # [lay5 hide]
    $ show_sprites()
    # [BG hide]
    $ fade_fx("black")
    # [COFFEE] → pause(1.0)
    $ pause(1.0)

    # [移動] → next(269): сцена 269 — глава 5, НЕ портируется
    return
