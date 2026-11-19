# Глава 8, часть 1 (сцены 405–416): «決意のお姫さま» — старт с титульной карточки,
# встреча с Уэзерби, диалоги Сайто/Анриетта/Луизы, три развилки выбора (сцены 405–412).
# Источник: ps2_source/chapters/chapter_09_決意のお姫さま.txt (SCENE 405-416).
# Точные аргументы: ps2_source/events_full/chapter_09_決意のお姫さま.txt.
#
# Голоса: 125 (сцены 405-416). Нумерация ch8_<spk>_<NNN> — с 001 по говорящему.
#   s: 57, h: 40, l: 14, k: 5, m: 2, si: 7
#   PS2 voice IDs: s=13560-13616, h=852-891, l=7407-7420, k=3858-3862, m=4172-4173, si=15167-15173
# Спрайты: id → имя по references/sprite_id_map.csv; PROVISIONAL.
#   398 → s 1 shy (есть в справочнике sprite_id_map.csv).
#   787 → id(787) (НЕТ в sprite_id_map.csv — placeholder).
# Фоны: id(2)=white, id(41)=..., id(42)=..., id(90)=... — некоторые пустые filenames
#   в image_id_map.csv (заглушки id(K), требуют решения человека).
# CG: 265, 266, 267 — в справочнике (каждое по одной сцене).
# Меню 【選択肢】: две развилки по три варианта (сцены 405 и 412) —
#   варианты разворачиваются внутрь пунктов меню, слияние — общие сцены (409 и 416).
# Не портируются: ITEM ××, SE (se1 stop), MSGON/MSGOFF, beginSkip/endSkip,
#   TRANS (выполняется fade_fx), BGU, TNDL — переносится (as tndl), VIBRATE → flash_fx("white").
#
# К обращению Анриетты: по addresses.md — «Ваше Высочество / мадемуазель»
#   (принцесса до восшествия на престол). В JA Сайто говорит «アンリエッта», Луиза — «姫さま»,
#   Кирхе — «マデモアゼル Kirche».
#
# Титульная карточка: K=13 (1..12 заняты главами 0-7). Вход — jump ch8
#   из главы 7; выход — jump ch8_2 (сцена 417) — E7 «forward debt»,
#   закроется частью 2.

label ch8:
    $ tndl(None)
    # Титульный монтаж → overlay_screen (образ «overlay»).
    call overlay_screen("overlay", "Chapter Eight: 'The Determined Princess'{#ch8_title}", isUseBlur=False, text_mode="black") from _call_overlay_screen_13
    pause(2)


    # ==== SCENE 405 ====
    # [TITLE title("決意のお姫さま")] — входит в титульный монтаж overlay_screen
    # [BG +2/+1145/+1168/+1145/+2/+41 —タイトルモンターж → fade_fx]
    $ show_sprites()
    # [SPRITE lay5 image=+412 → s 5]
    $ show_sprites(("s 5"))
    # サイト：朝になっちまったな。 / お姫さま、大丈夫かな……。  [voice 13560]
    voice "ch8_s_001"
    s "Morning came, huh? / I wonder if the Princess is all right…{#ch8_s_001}"
    # JA[13560]: 朝になっちまったな。 / お姫さま、大丈夫かな……。
    # [SPRITE lay5 image=+418 → s 5 sad]
    $ show_sprites(("s 5 sad"))
    # サイト：昨日、かなり悩んでたし。 / ……見にいってみるか。  [voice 13561]
    voice "ch8_s_002"
    s "You were quite troubled yesterday… / …Maybe I'll go take a look.{#ch8_s_002}"
    # JA[13561]: 昨日、かなり悩んでたし。 / ……見にいってみるか。
    # [BGM stop=1000]
    stop music fadeout 1.0
    # [SPRITE lay5 hide]
    # [BG stage hide]
    $ show_sprites()
    # [BG stage image=+41 → id(41)]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)] → fade_fx
    # [SPRITE lay5 image=+390 dir=1A → s 1]
    $ show_sprites(("s 1"))
    # [BGM play=+26 → t25]
    play music t25 fadein 1.0
    # サイト：お姫さまー、失礼しますよー。  [voice 13562]
    voice "ch8_s_003"
    s "Princess, excuse me!{#ch8_s_003}"
    # JA[13562]: お姫さまー、失礼しますよー。
    # [SPRITE lay5 x=224, y=0]
    # [SPRITE lay8 image=+792 → h 2 sad]
    $ show_sprites(("s 1", "h 2 sad"))
    # アンリエッタ：あ……使い魔さん。  [voice 852]
    voice "ch8_h_001"
    h "Ah… my familiar.{#ch8_h_001}"
    # JA[852]: あ……使い魔さん。
    # [SPRITE lay5 image=+394 dir=1A → s 1 angry]
    $ show_sprites(("s 1 angry", "h 2 sad"))
    # サイト：お姫さま！？ / そんな疲れた顔して……。 / やっぱり寝てなかったんですか？  [voice 13563]
    voice "ch8_s_004"
    s "Princess!? / You look so tired… / Did you not sleep after all?{#ch8_s_004}"
    # JA[13563]: お姫さま！？ / そんな疲れた顔して……。 / やっぱり寝てなかったんですか？
    # アンリエッタ：いえ、ちゃんと寝ました。 / でも、いろいろなことを考えてしまって……。  [voice 853]
    voice "ch8_h_002"
    h "No, I slept fine. / But I kept thinking about so many things…{#ch8_h_002}"
    # JA[853]: いえ、ちゃんと寝ました。 / でも、いろいろなことを考えてしまって……。
    # アンリエッタ：わたくしは、国も民も幸せにできない / のでしょうか？  [voice 854]
    voice "ch8_h_003"
    h "Can I really make both the country and its people happy?{#ch8_h_003}"
    # JA[854]: わたくしは、国も民も幸せにできない / のでしょうか？
    # アンリエッタ：ただ、地位にしがみつくだけの日々……。  [voice 855]
    voice "ch8_h_004"
    h "It's just days spent clinging to my position and nothing more…{#ch8_h_004}"
    # JA[855]: ただ、地位にしがみつくだけの日々……。
    # [SPRITE lay5 image=+390 dir=1A → s 1]
    $ show_sprites(("s 1", "h 2 sad"))
    # サイト：しっかりしてください、お姫さま。  [voice 13564]
    voice "ch8_s_005"
    s "Please pull yourself together, Princess.{#ch8_s_005}"
    # JA[13564]: しっかりしてください、お姫さま。
    # アンリエッタ：使い魔さん……。  [voice 856]
    voice "ch8_h_005"
    h "My familiar…{#ch8_h_005}"
    # JA[856]: 使い魔さん……。
    # [SPRITE lay8 image=+786, level=160, dir=1C]
    $ show_sprites(("s 1", "h 2"))
    # アンリエッタ：お願いです……。 / わたくしを、どこかに連れて行ってください。  [voice 857]
    voice "ch8_h_006"
    h "Please… / Take me away from here, somewhere, anywhere.{#ch8_h_006}"
    # JA[857]: お願いです……。 / わたくしを、どこかに連れて行ってください。
    # [SPRITE lay5 image=+429, level=160, dir=2A]
    $ show_sprites(("s 3", "h 2"))
    # サイト：へっ！？ / お姫さま！？  [voice 13565]
    voice "ch8_s_006"
    s "Huh!? / Princess!?{#ch8_s_006}"
    # JA[13565]: へっ！？ / お姫さま！？
    # [SPRITE lay8 image=+792, level=160, dir=1C]
    $ show_sprites(("s 3", "h 2 sad"))
    # アンリエッタ：お願い……ここではないどこかへ……！  [voice 858]
    voice "ch8_h_007"
    h "Please… anywhere but here…!{#ch8_h_007}"
    # JA[858]: お願い……ここではないどこかへ……！
    # [SPRITE lay5 image=+390, level=160, dir=1A]
    $ show_sprites(("s 1", "h 2 sad"))
    # サイト：……。  [voice 13566]
    voice "ch8_s_007"
    s "…{#ch8_s_007}"
    # JA[13566]: ……。


    # ---- 【選択肢】 ----
    menu:
        "It's impossible.{#ch8_c001}":
            # JA: それはできません。
            # [SPRITE lay8 image=+792 dir=1C → h 2 sad]
            # [SPRITE lay5 image=+390 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2 sad"))
            # [BGM play=+26 → t25]
            play music t25 fadein 1.0
            # [BG stage image=+41 → id(41)]
            $ fade_fx("id(41)")
            # [SPRITE lay5 image=+396 dir=1A → s 1 sad]
            $ show_sprites(("s 1 sad", "h 2 sad"))
            # サイト：それはできません。  [voice 13567]
            voice "ch8_s_008"
            s "I can't do that.{#ch8_s_008}"
            # JA[13567]: それはできません。
            # アンリエッタ：ああ……！  [voice 859]
            voice "ch8_h_008"
            h "Oh…!{#ch8_h_008}"
            # JA[859]: ああ……！
            # [SPRITE lay5 image=+429 dir=2A → s 3 sad]
            $ show_sprites(("s 3 sad", "h 2 sad"))
            # サイト：うまく言えないけど、 / 今、逃げちゃだめなんじゃないですか？ / つらいだろうけど。  [voice 13568]
            voice "ch8_s_009"
            s "I can't put it well, but / shouldn't you not run away now? / I know it's tough.{#ch8_s_009}"
            # JA[13568]: うまく言えないけど、 / 今、逃げちゃだめなんじゃないですか？ / つらいだろうけど。
            # アンリエッタ：……。  [voice 860]
            voice "ch8_h_009"
            h "…{#ch8_h_009}"
            # JA[860]: ……。
            # [SPRITE lay5 image=+390 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2"))
            # サイト：俺やルイズで良かったら / 泣き言くらい聞きますよ。 / 手伝えることがあったら、命令してください。  [voice 13569]
            voice "ch8_s_010"
            s "If you want, me or Louise / will listen to your complaints. / If there's anything I can do, just tell me.{#ch8_s_010}"
            # JA[13569]: 俺やルイズで良かったら / 泣き言くらい聞きますよ。 / 手伝えることがあったら、命令してください。
            # → next scene 409

        "Alright, let's go.{#ch8_c002}":
            # JA: 分かりました、行きましょう
            # [SPRITE lay8 image=+792 dir=1C → h 2 sad]
            # [SPRITE lay5 image=+390 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2 sad"))
            # [BGM play=+26 → t25]
            play music t25 fadein 1.0
            # [BG stage image=+41 → id(41)]
            $ fade_fx("id(41)")
            # [SPRITE lay5 image=+390 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2 sad"))
            # サイト：分かりました、どこに行きましょうか？  [voice 13570]
            voice "ch8_s_011"
            s "Understood. Where shall we go?{#ch8_s_011}"
            # JA[13570]: 分かりました、どこに行きましょうか？
            # [SPRITE lay8 image=+786 dir=1C → h 2]
            $ show_sprites(("s 1", "h 2"))
            # アンリエッタ：え……？  [voice 861]
            voice "ch8_h_010"
            h "Eh…?{#ch8_h_010}"
            # JA[861]: え……？.
            # サイト：お姫さまが、本当に何もかも捨てる覚悟が / できてるなら、どこにでも連れて行きますよ。  [voice 13571]
            voice "ch8_s_012"
            s "If the Princess is truly ready to throw everything away, I'll take you anywhere.{#ch8_s_012}"
            # JA[13571]: お姫さまが、本当に何もかも捨てる覚悟が / できてるなら、どこにでも連れて行きますよ。
            # [SPRITE lay8 image=+792 dir=1C → h 2 sad]
            $ show_sprites(("s 1", "h 2 sad"))
            # アンリエッタ：覚悟……。  [voice 862]
            voice "ch8_h_011"
            h "Resolution…?{#ch8_h_011}"
            # JA[862]: 覚悟……。

            # サイト：でも、その覚悟があるなら、 / もう一度頑張れるんじゃないですか？  [voice 13572]
            voice "ch8_s_013"
            s "But if you have that resolve, / can't you try again?{#ch8_s_013}"
            # JA[13572]: でも、その覚悟があるなら、 / もう一度頑張れるんじゃないですか？
            # [SPRITE lay5 image=+390 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2"))
            # アンリエッタ：使い魔さん……ありがとう……。  [voice 863]
            voice "ch8_h_012"
            h "My familiar… thank you…{#ch8_h_012}"
            # JA[863]: 使い魔さん……ありがとう……。
            # → next scene 409

        "Or, let's go to my hometown.{#ch8_c003}":
            # JA: いっそ、俺の故郷に行けたら
            # [SPRITE lay8 image=+792 dir=1C → h 2 sad]
            # [SPRITE lay5 image=+390 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2 sad"))
            # [BGM play=+26 → t25]
            play music t25 fadein 1.0
            # [BG stage image=+41 → id(41)]
            $ fade_fx("id(41)")
            # [SPRITE lay5 image=+396 dir=1A → s 1 sad]
            $ show_sprites(("s 1 sad", "h 2 sad"))
            # サイト：いっそ、俺の故郷に行けたら……。  [voice 13573]
            voice "ch8_s_014"
            s "If only we could go to my hometown…{#ch8_s_014}"
            # JA[13573]: いっそ、俺の故郷に行けたら……。
            # [SPRITE lay8 image=+786 dir=1C → h 2]
            $ show_sprites(("s 1 sad", "h 2"))
            # アンリエッタ：使い魔さんの、故郷……？ / どんなところでしょう？  [voice 864]
            voice "ch8_h_013"
            h "Your hometown…? / What's it like?{#ch8_h_013}"
            # JA[864]: 使い魔さんの、故郷……？ / どんなところでしょう？
            # [SPRITE lay5 image=+390 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2"))
            # サイト：特に良くも悪くもない、いや逆かな。 / 良い人もいれば悪い人もいて、 / みんながみんな幸せってわけでもない。  [voice 13574]
            voice "ch8_s_015"
            s "It's neither particularly good nor bad. / There are good people and bad people, / and not everyone is happy.{#ch8_s_015}"
            # JA[13574]: 特に良くも悪くもない、いや逆かな。 / 良い人もいれば悪い人もいて、 / みんながみんな幸せってわけでもない。
            # [SPRITE lay5 image=+423 dir=2A → s 3]
            $ show_sprites(("s 3", "h 2"))
            # サイト：それでも帰りたいんですけどね、俺。 / 春奈もそうだったし。  [voice 13575]
            voice "ch8_s_016"
            s "I still want to go back, you see. / Haruna felt the same way.{#ch8_s_016}"
            # JA[13575]: それでも帰りたいんですけどね、俺。 / 春奈もそうだったし。
            # [SPRITE lay8 image=+792 dir=1C → h 2 sad]
            $ show_sprites(("s 3", "h 2 sad"))
            # アンリエッタ：ハルナ、さん……。  [voice 865]
            voice "ch8_h_014"
            h "Haruna-san…{#ch8_h_014}"
            # JA[865]: ハルナ、さん……。
            # [SPRITE lay8 image=+786 dir=1C → h 2]
            $ show_sprites(("s 3", "h 2"))
            # アンリエッタ：そう、そうでしたね……。 / あの娘も、あなたと同じ世界から / 来たのでしたね。  [voice 866]
            voice "ch8_h_015"
            h "That's right… / That girl came from the same world as you, didn't she?{#ch8_h_015}"
            # JA[866]: そう、そうでしたね……。 / あの娘も、あなたと同じ世界から / 来たのでしたね。
            # [SPRITE lay5 image=+390 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2"))
            # サイト：はい……。 / いつか帰れるはずだ。 / あきらめないでいようって。  [voice 13576]
            voice "ch8_s_017"
            s "Yes… / We'll be able to go back someday. / That's what we promised.{#ch8_s_017}"
            # JA[13576]: はい……。 / いつか帰れるはずだ。 / あきらめないでいようって。
            # [SPRITE lay5 image=+392 dir=1A → s 1 happy]
            $ show_sprites(("s 1 happy", "h 2"))
            # サイト：そう、２人で約束したんです。  [voice 13577]
            voice "ch8_s_018"
            s "That's what the two of us promised.{#ch8_s_018}"
            # JA[13577]: そう、２人で約束したんです。
            # [SPRITE lay8 image=+792 dir=1C → h 2 sad]
            $ show_sprites(("s 1 happy", "h 2 sad"))
            # アンリエッタ：……。  [voice 867]
            voice "ch8_h_016"
            h "…{#ch8_h_016}"
            # JA[867]: ……。

            # アンリエッタ：ならば、彼女を見捨てて行くわけには、 / いきませんね……。  [voice 868]
            voice "ch8_h_017"
            h "Then I can't abandon her…{#ch8_h_017}"
            # JA[868]: ならば、彼女を見捨てて行くわけには、 / いきませんね……。
            # アンリエッタ：彼女がこうなったのは、 / わたくしの責任なのですから。  [voice 869]
            voice "ch8_h_018"
            h "It's my fault she ended up like this.{#ch8_h_018}"
            # JA[869]: 彼女がこうなったのは、 / わたくしの責任なのですから。
            # [SPRITE lay5 image=+396 dir=1A → s 1 sad]
            $ show_sprites(("s 1 sad", "h 2 sad"))
            # サイト：お姫さま……。  [voice 13578]
            voice "ch8_s_019"
            s "Princess…{#ch8_s_019}"
            # JA[13578]: お姫さま……。
            # → next scene 409

    # ==== SCENE 409 (переход после вариантов) ====
    # [SPRITE lay8 image=+792 dir=1C → h 2 sad]
    # [SPRITE lay5 image=+390 dir=1A → s 1]
    $ show_sprites(("s 1", "h 2 sad"))
    # [BGM play=+26 → t25]
    play music t25 fadein 1.0
    # [BG stage image=+41 → id(41)]
    $ fade_fx("id(41)")
    # アンリエッタ：う……ふ、ううっ……うっ、うっ……！  [voice 870]
    voice "ch8_h_019"
    h "Ugh… nnh… ugh, ugh…!{#ch8_h_019}"
    # JA[870]: う……ふ、ううっ……うっ、うっ……！
    # [SPRITE lay5 image=+429 dir=2A → s 3 sad]
    $ show_sprites(("s 3 sad", "h 2 sad"))
    # サイト：あ、ええと？ / お、お姫さま……っ！  [voice 13579]
    voice "ch8_s_020"
    s "Ah, um… / P-Princess…!{#ch8_s_020}"
    # JA[13579]: あ、ええと？ / お、お姫さま……っ！
    # [SPRITE lay5 image=+396 dir=1A → s 1 sad]
    $ show_sprites(("s 1 sad", "h 2 sad"))
    # サイト：（ど、どうしよう。 / 女の子が泣いちゃったら、 / 一体どうすればいいんだ？）
    th "(W-what should I do? / What am I supposed to do if she cries?){#ch8_th_409a}"
    # JA: （ど、どうしよう。 / 女の子が泣いちゃったら、 / 一体どうすればいいんだ？）
    # [SPRITE lay5 hide]
    # [SPRITE lay8 hide]
    $ show_sprites()
    # [SPRITE lay1 image=+304 dir=1A → l 1 happy]
    $ show_sprites(("l 1 happy"))
    # ルイズ：おはようございます、姫さま。 / お加減は……。 / って、姫さまっ！？  [voice 7407]
    voice "ch8_l_001"
    l "Good morning, Princess. / Are you feeling better? / Wait, Princess!?{#ch8_l_001}"
    # JA[7407]: おはようございます、姫さま。 / お加減は……。 / って、姫さまっ！？
    # [BGM stop=1000]
    stop music fadeout 1.0
    # [BGM play=+30 → t29]
    play music t29 fadein 1.0
    # [SPRITE lay1 image=+302 dir=1A → l 1]
    $ show_sprites(("l 1"))
    # [SPRITE lay5 image=+429 dir=2A → s 3 sad]
    $ show_sprites(("l 1", "s 3 sad"))
    # サイト：あ、こ、これは違うんだ、ルイズっ！  [voice 13580]
    voice "ch8_s_021"
    s "Ah, n-no, this isn't what it looks like, Louise!{#ch8_s_021}"
    # JA[13580]: あ、こ、これは違うんだ、ルイズっ！
    # [SPRITE lay1 image=+306 dir=1A → l 1 angry]
    $ show_sprites(("l 1 angry", "s 3 sad"))
    # ルイズ：サイトぉぉぉっ！ / 姫さまに何したのー！？ / 正直に言ってごらんなさい。  [voice 7408]
    voice "ch8_l_002"
    l "Saito-o-o-o! / What did you do to the Princess!? / Tell me the truth!{#ch8_l_002}"
    # JA[7408]: サイトぉぉぉっ！ / 姫さまに何したのー！？ / 正直に言ってごらんなさい。
    # [SPRITE lay5 image=+394 dir=1A → s 1 angry]
    $ show_sprites(("l 1 angry", "s 1 angry"))
    # サイト：だから違うんだってー！ / 何もやってないって。  [voice 13581]
    voice "ch8_s_022"
    s "I'm telling you it's not like that! / I didn't do anything!{#ch8_s_022}"
    # JA[13581]: だから違うんだってー！ / 何もやってないって。
    # [SPRITE lay1 hide]
    $ show_sprites(("s 1 angry"))
    # [SPRITE lay5 x=64, y=0]
    # [SE se0 play=+62]
    play sound se_62
    # [BG stage vibrate=14] → flash_fx("white")
    $ flash_fx("white")
    # [EVENT_CG event vibrate=14] → flash_fx("white")
    # [SPRITE lay1 vibrate=14]
    # [SPRITE lay5 vibrate=14]
    # [SPRITE lay8 vibrate=14]
    # [VIBRATE vibrate(2)] → flash_fx("white")
    # [BG stage reset]
    # [EVENT_CG event hide, reset]
    # [SPRITE lay8 hide, reset]
    # [SPRITE lay5 reset]
    # [SPRITE lay1 hide, reset]
    # サイト：うぎゃー。  [voice 13582]
    voice "ch8_s_023"
    s "Uwaaah!{#ch8_s_023}"
    # JA[13582]: うぎゃー。
    # [SE se1 stop=1]
    stop sound se_61
    # [BGM stop=1000]
    stop music fadeout 1.0
    # [SPRITE lay5 hide]
    # [BG stage hide]
    $ show_sprites()
    $ fade_fx("black")
    # → next scene 410


    # ==== SCENE 410 ====
    # [BG stage image=+41 → id(41)]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM play=+28 → t27]
    play music t27 fadein 1.0
    # アンリエッタ：すう……すう……。  [voice 871]
    voice "ch8_h_020"
    h "Snore… snore…{#ch8_h_020}"
    # JA[871]: すう……すう……。
    # [SPRITE lay5 image=+390 dir=1A → s 1]
    $ show_sprites(("s 1"))
    # サイト：泣き疲れて、寝ちゃったか。 / いくら王家だ女王だなんていっても、 / やっぱり、１人の人間なんだな。  [voice 13583]
    voice "ch8_s_024"
    s "She cried herself to sleep. / No matter how royal or queenly she is, / she's still just one person.{#ch8_s_024}"
    # JA[13583]: 泣き疲れて、寝ちゃったか。 / いくら王家だ女王だなんていっても、 / やっぱり、１人の人間なんだな。
    # [SPRITE lay5 x=224, y=0]
    # [SPRITE lay1 image=+302 dir=1A → l 1]
    $ show_sprites(("l 1", "s 1"))
    # ルイズ：この数ヶ月、大事件が立て続きに起きてたしね。 / 女王ってだけでも、大変な責務だって / いうのに……。  [voice 7409]
    voice "ch8_l_003"
    l "There've been so many big incidents these past few months. / And being a queen is already such a heavy responsibility…{#ch8_l_003}"
    # JA[7409]: この数ヶ月、大事件が立て続きに起きてたしね。 / 女王ってだけでも、大変な責務だって / いうのに……。
    # [SE se0 play=+64]
    play sound se_64
    # [BG stage vibrate=14] → flash_fx("white")
    $ flash_fx("white")
    # [EVENT_CG event vibrate=14]
    # [SPRITE lay3 vibrate=14]
    # [SPRITE lay2 vibrate=14]
    # [SPRITE lay8 hide, vibrate=14]
    # [SPRITE lay5 vibrate=14]
    # [SPRITE lay1 vibrate=14]
    # [SPRITE lay6 vibrate=14]
    # [VIBRATE vibrate(2)]
    # [BG stage reset]
    # [EVENT_CG event hide, reset]
    # [SPRITE lay3 hide, reset]
    # [SPRITE lay2 hide, reset]
    # [SPRITE lay8 hide, reset]
    # [SPRITE lay5 reset]
    # [SPRITE lay1 reset]
    # [SPRITE lay6 hide, reset]
    # [SPRITE lay1 image=+306 dir=1A → l 1 angry]
    $ show_sprites(("l 1 angry"))
    # ルイズ：きゃあっ！  [voice 7410]
    voice "ch8_l_004"
    l "Kyaa!{#ch8_l_004}"
    # JA[7410]: キャあっ！
    # [SPRITE lay5 image=+427 dir=2A → s 3 angry]
    $ show_sprites(("l 1 angry", "s 3 angry"))
    # サイト：くそ、始まったか！  [voice 13584]
    voice "ch8_s_025"
    s "Damn it, it's starting!{#ch8_s_025}"
    # JA[13584]: くそ、始まったか！
    # [SPRITE lay1 image=+302 dir=1A → l 1]
    $ show_sprites(("l 1", "s 3 angry"))
    # ルイズ：軍が、各砲台に向かっているって / 聞いてはいたけど、やっぱり苦戦してるようね。  [voice 7411]
    voice "ch8_l_005"
    l "I heard the army's heading for the fortresses, / but it looks like they're struggling.{#ch8_l_005}"
    # JA[7411]: 軍が、各砲台に向かっているって / 聞いてはいたけど、やっぱり苦戦してるようね。
    # ルイズ：さっき、キュルケが銃士隊の人から情報を / 貰ったって言ってた。  [voice 7412]
    voice "ch8_l_006"
    l "Kirche said she got intel from the Musketeers earlier.{#ch8_l_006}"
    # JA[7412]: さっき、キュルケが銃士隊の人から情報を / 貰ったって言ってた。
    # [SPRITE lay5 image=+394 dir=1A → s 1 angry]
    $ show_sprites(("l 1", "s 1 angry"))
    # サイト：それじゃ、その話を聞いたうえで / 今後の行動を決めようか。  [voice 13585]
    voice "ch8_s_026"
    s "Then let's hear it and decide what to do next.{#ch8_s_026}"
    # JA[13585]: それじゃ、その話を聞いたうえで / 今後の行動を決めようか。
    # [SPRITE lay1 image=+335 dir=2A → l 3]
    $ show_sprites(("l 3", "s 1 angry"))
    # ルイズ：そうね。 / 姫さまには、シエスタについてて / もらいましょう。  [voice 7413]
    voice "ch8_l_007"
    l "Right. / Let's have Siesta stay with the Princess.{#ch8_l_007}"
    # JA[7413]: そうね。 / 姫さまには、シエスタについてて / もらいましょう。
    # [SPRITE lay5 image=+390 dir=1A → s 1]
    $ show_sprites(("l 3", "s 1"))
    # サイト：分かった。 / シエスタにそう伝えてくるよ。  [voice 13586]
    voice "ch8_s_027"
    s "Got it. I'll tell Siesta.{#ch8_s_027}"
    # JA[13586]: 分かった。 / シエスタにそう伝えてくるよ。
    # [SPRITE lay8 hide]
    # [SPRITE lay5 hide]
    # [SPRITE lay1 hide]
    $ show_sprites()
    # [BG stage hide]
    # [BG stage image=+41 → id(41)]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE lay6 image=+676 dir=1A → k 1]
    $ show_sprites(("k 1"))
    # キュルケ：各所の大砲に対して、いちはやく銃士隊が / 制圧に動いたそうだけど、戦力差がありすぎて、 / こうちゃく状態に持ち込むのが精一杯だそうよ。  [voice 3858]
    voice "ch8_k_001"
    k "I heard the Musketeers moved quickly to secure the cannons, / but the difference in numbers is too great, / so they're just barely holding the line.{#ch8_k_001}"
    # JA[3858]: 各所の大砲に対して、いちはやく銃士隊が / 制圧に動いたそうだけど、戦力差がありすぎて、 / こうちゃく状態に持ち込むのが精一杯だそうよ。
    # [SPRITE lay6 image=+682 dir=1A → k 1 sad]
    $ show_sprites(("k 1 sad"))
    # キュルケ：その上……。  [voice 3859]
    voice "ch8_k_002"
    k "And on top of that…{#ch8_k_002}"
    # JA[3859]: その上……。
    # [SPRITE lay6 x=224, y=0]
    # [SPRITE lay1 image=+302 dir=1A → l 1]
    $ show_sprites(("l 1", "k 1 sad"))
    # ルイズ：なにか良くないしらせがあるみたいね……。  [voice 7414]
    voice "ch8_l_008"
    l "Sounds like there's some bad news…{#ch8_l_008}"
    # JA[7414]: なにか良くないしらせがあるみたいね……。
    # キュルケ：とびきりのね。  [voice 3860]
    voice "ch8_k_003"
    k "Terrible news.{#ch8_k_003}"
    # JA[3860]: とびきりのね。
    # [SPRITE lay6 image=+676 dir=1A → k 1]
    $ show_sprites(("l 1", "k 1"))
    # キュルケ：レコン・キスタ軍の空中艦隊が、 / トリステインをめざして動き始めたって。 / 遠見の魔術師隊からの報告よ。  [voice 3861]
    voice "ch8_k_004"
    k "The Reconquista air fleet has started moving toward Tristain. / That's from the Far-Seer mages.{#ch8_k_004}"
    # JA[3861]: レコン・キスタ軍の空中艦隊が、 / トリステインをめざして動き始めたって。 / 遠見の魔術師隊からの報告よ。
    # [SPRITE lay1 image=+306 dir=1A → l 1 angry]
    $ show_sprites(("l 1 angry", "k 1"))
    # ルイズ：なんですって！？  [voice 7415]
    voice "ch8_l_009"
    l "What do you mean!?{#ch8_l_009}"
    # JA[7415]: なんですって！？
    # [SPRITE lay1 hide]
    # [SPRITE lay3 image=+858 dir=1A → m 1 sad]
    $ show_sprites(("m 1 sad"))
    # モンモランシー：今のままでは、トリステインの艦隊を / 動かすのも危険な状態ね。 / 王都がここまで砲台に囲まれては……。  [voice 4172]
    voice "ch8_m_001"
    m "As things stand, it's dangerous to move the Tristain fleet. / The capital's surrounded by fortresses…{#ch8_m_001}"
    # JA[4172]: 今のままでは、トリステインの艦隊を / 動かすのも危険な状態ね。 / 王都がここまで砲台に囲まれては……。
    # [SPRITE lay3 image=+891 dir=2A → m 4 sad]
    $ show_sprites(("m 4 sad"))
    # モンモランシー：せめて、レコン・キスタの艦隊が来るまでに、 / 砲台を何とかしないと！  [voice 4173]
    voice "ch8_m_002"
    m "At the very least, / we need to do something about the fortresses before the Reconquista fleet arrives!{#ch8_m_002}"
    # JA[4173]: せめて、レコン・キスタの艦隊が来るまでに、 / 砲台を何とかしないと！
    # [SPRITE lay6 hide]
    $ show_sprites(("m 4 sad"))
    # [SPRITE lay5 image=+394 dir=1A → s 1 angry]
    $ show_sprites(("s 1 angry", "m 4 sad"))
    # サイト：くそっ。 / ここまで用意周到とは……。  [voice 13587]
    voice "ch8_s_028"
    s "Damn. / They're that well-prepared…{#ch8_s_028}"
    # JA[13587]: くそっ。 / ここまで用意周到とは……。
    # [SPRITE lay3 hide]
    # [SPRITE lay1 image=+308 dir=1A → l 1 sad]
    $ show_sprites(("l 1 sad", "s 1 angry"))
    # ルイズ：どうすればいいの……。  [voice 7416]
    voice "ch8_l_010"
    l "What should we do…{#ch8_l_010}"
    # JA[7416]: どうすればいいの……。
    # [SPRITE lay5 hide]
    # [SPRITE lay1 hide]
    $ show_sprites()
    # [SPRITE lay2 image=+489 dir=1A → si 1]
    $ show_sprites(("si 1"))
    # シエスタ：あの、みなさん。  [voice 15167]
    voice "ch8_si_001"
    si "Um, everyone.{#ch8_si_001}"
    # JA[15167]: あの、みなさん。
    # [SPRITE lay2 x=-96, y=0]
    # [SPRITE lay5 image=+390 dir=1A → s 1]
    $ show_sprites(("si 1", "s 1"))
    # サイト：シエスタ、どうしたんだ？  [voice 13588]
    voice "ch8_s_029"
    s "Siesta, what's wrong?{#ch8_s_029}"
    # JA[13588]: シエスタ、どうしたんだ？
    # シエスタ：女王陛下が落ち着いて、 / お休みになられたようなので、 / お知らせに……。  [voice 15168]
    voice "ch8_si_002"
    si "Her Majesty seemed to have settled down and gone to rest, / so I came to let you know…{#ch8_si_002}"
    # JA[15168]: 女王陛下が落ち着いて、 / お休みになられたようなので、 / お知らせに……。
    # [SPRITE lay5 image=+423 dir=2A → s 3]
    $ show_sprites(("si 1", "s 3"))
    # サイト：ああ、ありがとうシエスタ。  [voice 13589]
    voice "ch8_s_030"
    s "Ah, thanks, Siesta.{#ch8_s_030}"
    # JA[13589]: ああ、ありがとうシエスタ。
    # シエスタ：サイトさん……。  [voice 15169]
    voice "ch8_si_003"
    si "Saito-san…{#ch8_si_003}"
    # JA[15169]: サイトさん……。

    # [SPRITE lay5 image=+390 dir=1A → s 1]
    $ show_sprites(("si 1", "s 1"))
    # サイト：うん？  [voice 13590]
    voice "ch8_s_031"
    s "Huh?{#ch8_s_031}"
    # JA[13590]: うん？
    # [SPRITE lay2 image=+495 dir=1A → si 1 sad]
    $ show_sprites(("si 1 sad", "s 1"))
    # シエスタ：私達、これからどうなるんですか？  [voice 15170]
    voice "ch8_si_004"
    si "What's going to happen to us?{#ch8_si_004}"
    # JA[15170]: 私達、これからどうなるんですか？
    # [SPRITE lay5 hide]
    # [SPRITE lay1 image=+302 dir=1A → l 1]
    $ show_sprites(("si 1 sad", "l 1"))
    # ルイズ：シエスタ？  [voice 7417]
    voice "ch8_l_011"
    l "Siesta?{#ch8_l_011}"
    # JA[7417]: シエスタ？
    # [SPRITE lay2 image=+493 dir=1A → si 1 angry]
    $ show_sprites(("l 1", "si 1 angry"))
    # シエスタ：だって、戦争が始まるんですよ？ / 家が焼けて、人がいっぱい死ぬんですよ！？  [voice 15171]
    voice "ch8_si_005"
    si "Because war is starting, right? / Houses will burn and lots of people will die!?{#ch8_si_005}"
    # JA[15171]: だって、戦争が始まるんですよ？ / 家が焼けて、人がいっぱい死ぬんですよ！？
    # シエスタ：早く、学院に戻りましょう！ / あそこなら、ここと違って安全なんでしょう？ / だったら……！  [voice 15172]
    voice "ch8_si_006"
    si "Let's go back to the academy quickly! / It should be safer there, right? / So…!{#ch8_si_006}"
    # JA[15172]: 早く、学院に戻りましょう！ / あそこなら、ここと違って安全なんでしょう？ / だったら……！
    # [SPRITE lay1 hide]
    $ show_sprites(("si 1 angry"))
    # [SPRITE lay5 image=+390 dir=1A → s 1]
    $ show_sprites(("si 1 angry", "s 1"))
    # サイト：それはできないよ。 / この街の人達を放っておいていけないよ。 / 何かできることがあったらしたいと思うんだ。  [voice 13591]
    voice "ch8_s_032"
    s "I can't do that. / I can't just leave these people behind. / If there's something I can do, I want to try.{#ch8_s_032}"
    # JA[13591]: それはできないよ。 / この街の人達を放っておいていけないよ。 / 何かできることがあったらしたいと思うんだ。
    # [SPRITE lay2 image=+495 dir=1A → si 1 sad]
    $ show_sprites(("s 1", "si 1 sad"))
    # シエスタ：そうですよね……。 / すみません、変なこと言って。  [voice 15173]
    voice "ch8_si_007"
    si "You're right… / Sorry, I said something stupid.{#ch8_si_007}"
    # JA[15173]: そうですよね……。 / すみません、変なこと言って。
    # [SPRITE lay2 hide]
    $ show_sprites(("si 1 sad"))
    # [SPRITE lay5 hide]
    # [SPRITE lay1 image=+302 dir=1A → l 1]
    $ show_sprites(("l 1"))
    # ルイズ：それじゃとりあえず、 / 姫さまが目を覚ましたら、城まで護衛しましょう。  [voice 7418]
    voice "ch8_l_012"
    l "Then for now, / let's escort the Princess back to the castle when she wakes up.{#ch8_l_012}"
    # JA[7418]: それじゃとりあえず、 / 姫さまが目を覚ましたら、城まで護衛しましょう。
    # ルイズ：危険なのは分かるけど、 / 女王がいないことには、何も動かないわ。  [voice 7419]
    voice "ch8_l_013"
    l "I know it's dangerous, / but nothing will move without the queen.{#ch8_l_013}"
    # JA[7419]: 危険なのは分かるけど、女王がいないことには、何も動かないわ。
    # [SPRITE lay1 x=-96, y=0]
    # [SPRITE lay6 image=+676 dir=1A → k 1]
    $ show_sprites(("l 1", "k 1"))
    # キュルケ：賛成。  [voice 3862]
    voice "ch8_k_005"
    k "Agreed.{#ch8_k_005}"
    # JA[3862]: 賛成。
    # [SPRITE lay1 image=+335 dir=2A → l 3]
    $ show_sprites(("l 3", "k 1"))
    # ルイズ：じゃあ、解散ね。  [voice 7420]
    voice "ch8_l_014"
    l "Then, dismissed.{#ch8_l_014}"
    # JA[7420]: じゃあ、解散ね。
    # [SPRITE lay1 hide]
    # [SPRITE lay6 hide]
    $ show_sprites()
    # [SPRITE lay5 image=+396 dir=1A → s 1 sad]
    $ show_sprites(("s 1 sad"))
    # サイト：ふう……。 / お姫さまを城まで送って、その後か……。 / 一体どうなるんだろう。  [voice 13592]
    voice "ch8_s_033"
    s "Phew… / Take the Princess to the castle, and then… / What will happen, I wonder.{#ch8_s_033}"
    # JA[13592]: ふう……。 / お姫さまを城まで送って、その後か……。 / 一体どうなるんだろう。
    # [SE se1 stop=1]
    stop sound se_61
    # [BGM stop=1000]
    stop music fadeout 1.0
    # [SPRITE lay5 hide]
    # [BG stage hide]
    $ show_sprites()
    $ fade_fx("black")
    # → next scene 411


    # ==== SCENE 411 ====
    # [BG stage image=+41 → id(41)]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM play=+22 → t21]
    play music t21 fadein 1.0
    # [SE se0 play=+55]
    play sound se_55
    # [SPRITE lay5 image=+396 dir=1A → s 1 sad]
    $ show_sprites(("s 1 sad"))
    # サイト：お姫さま……？  [voice 13593]
    voice "ch8_s_034"
    s "Princess…?{#ch8_s_034}"
    # JA[13593]: お姫さま……？.
    # [SE se0 play=+56]
    play sound se_56
    # [SPRITE lay5 hide]
    # [BG stage hide]
    $ show_sprites()
    # [EVENT_CG event image=+265 level=80]
    $ fade_fx("id(265)")
    # [TRANS trans("crossfade", 1000)]
    # アンリエッタ：う、ん……。  [voice 872]
    voice "ch8_h_021"
    h "Mm… hmm…{#ch8_h_021}"
    # JA[872]: う、ん……。
    # サイト：おっと、起こさないように静かにしないとな。  [voice 13594]
    voice "ch8_s_035"
    s "Careful, let's be quiet so we don't wake her.{#ch8_s_035}"
    # JA[13594]: おっと、起こさないように静かにしないとな。
    # サイト：こうしてると、本当にただの女の子だよな。 / でも、彼女が国を背負ってる。 / そりゃ大変だよな。  [voice 13595]
    voice "ch8_s_036"
    s "Looking at her like this, she's really just an ordinary girl. / But she carries a nation on her back. / That's tough, huh.{#ch8_s_036}"
    # JA[13595]: こうしてると、本当にただの女の子だよな。 / でも、彼女が国を背負ってる。 / そりゃ大変だよな。
    # [SPRITE lay8 hide]
    # アンリエッタ：ん……。  [voice 873]
    voice "ch8_h_022"
    h "Mm…{#ch8_h_022}"
    # JA[873]: ん……。
    # サイト：今の俺にできるのは、 / こうして見守ることだけだけど……。  [voice 13596]
    voice "ch8_s_037"
    s "All I can do right now is watch over her like this…{#ch8_s_037}"
    # JA[13596]: 今の俺にできるのは、 / こうして見守ることだけだけど……。
    # サイト：せめて、少しでもお姫さまのお役に立つことが / あればいいのにな……。  [voice 13597]
    voice "ch8_s_038"
    s "If only I could be even a little bit useful to the Princess…{#ch8_s_038}"
    # JA[13597]: せめて、少しでもお姫さまのお役に立つことが / あればいいのにな……。
    # [SE se1 stop=1]
    stop sound se_61
    # [BGM stop=1000]
    stop music fadeout 1.0
    # [SPRITE lay8 hide]
    # [SPRITE lay5 hide]
    # [BG stage hide]
    # [EVENT_CG event hide]
    $ show_sprites()
    $ fade_fx("black")
    # → next scene 412


    # ==== SCENE 412 ====
    # [EVENT_CG event image=+265 level=80]
    $ fade_fx("id(265)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM play=+16 → t15]
    play music t15 fadein 1.0
    # アンリエッタ：う、ん……。  [voice 874]
    voice "ch8_h_023"
    h "Mm… hmm…{#ch8_h_023}"
    # JA[874]: う、ん……。
    # [EVENT_CG event image=+266 level=80]
    $ fade_fx("id(266)")
    # アンリエッタ：あ……ここ、は……。 / そう、宿屋でしたわね……。  [voice 875]
    voice "ch8_h_024"
    h "Ah… where is this…? / Right, it's an inn…{#ch8_h_024}"
    # JA[875]: あ……ここ、は……。 / そう、宿屋でしたわね……。
    # サイト：あ、起きたんすね。 / お姫さま、おはようございます。 / ってもう夕方ですけど。  [voice 13598]
    voice "ch8_s_039"
    s "Oh, you're awake. / Good morning, Princess. / Although it's already evening.{#ch8_s_039}"
    # JA[13598]: あ、起きたんすね。 / お姫さま、おはようございます。 / ってもう夕方ですけど。
    # [SPRITE lay8 hide]
    # [SPRITE lay5 hide]
    # [EVENT_CG event hide]
    $ show_sprites()
    # [BG stage image=+42 → id(42)]
    $ fade_fx("id(42)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE lay8 image=+794 dir=1C → h 2 shy]
    $ show_sprites(("h 2 shy"))
    # [SPRITE lay5 image=+390 dir=1A → s 1]
    $ show_sprites(("h 2 shy", "s 1"))
    # アンリエッタ：あ、あの、あのっ……！？  [voice 876]
    voice "ch8_h_025"
    h "Ah, w-wait…!?{#ch8_h_025}"
    # JA[876]: あ、あの、あのっ……！？
    # サイト：（お姫さま、どうしたんだ？ / あんなに顔を真っ赤にして……）
    th "(Princess, what's wrong? / Why are you so red in the face…){#ch8_th_412a}"
    # JA: （お姫さま、どうしたんだ？ / あんなに顔を真っ赤にして……）
    # アンリエッタ：あのっ、使い魔さんずっといたんですか！？  [voice 877]
    voice "ch8_h_026"
    h "Wait, you've been here the whole time!?{#ch8_h_026}"
    # JA[877]: あのっ、使い魔さんずっといたんですか！？
    # サイト：ええ、護衛だから。 / ずっといましたよ。  [voice 13599]
    voice "ch8_s_040"
    s "Yes, I'm your guard. / I've been here the whole time.{#ch8_s_040}"
    # JA[13599]: ええ、護衛だから。 / ずっといましたよ。
    # アンリエッタ：ずっと、って、その、あの……っ！  [voice 878]
    voice "ch8_h_027"
    h "The whole time, you… w-wait…!{#ch8_h_027}"
    # JA[878]: ずっと、って、その、あの……っ！
    # [SPRITE lay5 image=+429 dir=2A → s 3 sad]
    $ show_sprites(("h 2 shy", "s 3 sad"))
    # サイト：あ、いや、寝てる間に何かしたとか / 絶対ないですよ。 / そんなことは護衛じゃないし。  [voice 13600]
    voice "ch8_s_041"
    s "Ah, no, I absolutely didn't do anything while you were sleeping. / That's not what a guard does.{#ch8_s_041}"
    # JA[13600]: あ、いや、寝てる間に何かしたとか / 絶対ないですよ。 / そんなことは護衛じゃないし。
    # [SPRITE lay5 image=+431 dir=2A → s 3 shy]
    $ show_sprites(("h 2 shy", "s 3 shy"))
    # サイト：もちろん、寝顔が可愛いなぁ。 / とか思ったりはしましたけど、 / まあ、そういう感じで。  [voice 13601]
    voice "ch8_s_042"
    s "Of course, I did think your sleeping face was cute. / But, you know, just a thought.{#ch8_s_042}"
    # JA[13601]: もちろん、寝顔が可愛いなぁ。 / とか思ったりはしましたけど、 / まあ、そういう感じで。
    # [SPRITE lay8 image=+788 dir=1C → h 2 happy]
    $ show_sprites(("h 2 happy", "s 3 shy"))
    # アンリエッタ：ふふっ。  [voice 879]
    voice "ch8_h_028"
    h "Hehe.{#ch8_h_028}"
    # JA[879]: ふふっ。
    # [SPRITE lay5 image=+396 dir=1A → s 1 sad]
    $ show_sprites(("h 2 happy", "s 1 sad"))
    # サイト：ど、どうしました？ / 何かおかしかったですか？  [voice 13602]
    voice "ch8_s_043"
    s "W-what's wrong? / Was something wrong?{#ch8_s_043}"
    # JA[13602]: ど、どうしました？ / 何かおかしかったですか？
    # [SPRITE lay8 image=+786 dir=1C → h 2]
    $ show_sprites(("h 2", "s 1 sad"))
    # アンリエッタ：いいえ。 / ひとつ、お聞きしてよろしいですか？  [voice 880]
    voice "ch8_h_029"
    h "No. / May I ask you one thing?{#ch8_h_029}"
    # JA[880]: いいえ。 / ひとつ、お聞きしてよろしいですか？
    # [SPRITE lay5 image=+390 dir=1A → s 1]
    $ show_sprites(("h 2", "s 1"))
    # サイト：なんでしょう。  [voice 13603]
    voice "ch8_s_044"
    s "What is it?{#ch8_s_044}"
    # JA[13603]: なんでしょう。
    # アンリエッタ：サイトさんは、女王であるわたくしに / あまり遠慮はしないのですね。 / なぜですか？  [voice 881]
    voice "ch8_h_030"
    h "Saito-san, you don't hold back much around me, the Queen. / Why is that?{#ch8_h_030}"
    # JA[881]: サイトさんは、女王であるわたくしに / あまり遠慮はしないのですね。 / なぜですか？


    # ---- 【選択肢】 ----
    menu:
        "Because she's cute.{#ch8_c004}":
            # JA: だってかわいいし
            # [SPRITE lay8 image=+786 dir=1C → h 2]
            # [SPRITE lay5 image=+390 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2"))
            # [BGM play=+16 → t15]
            play music t15 fadein 1.0
            # [BG stage image=+42 → id(42)]
            $ fade_fx("id(42)")
            # [SPRITE lay5 image=+398 dir=1A → s 1 shy]
            $ show_sprites(("s 1 shy", "h 2"))
            # サイト：だって、お姫さまがかわいかったし……。  [voice 13604]
            voice "ch8_s_045"
            s "Because you're cute, Princess…{#ch8_s_045}"
            # JA[13604]: だって、お姫さまがかわいかったし……。
            # [SPRITE lay8 image=+794 dir=1C → h 2 shy]
            $ show_sprites(("s 1 shy", "h 2 shy"))
            # アンリエッタ：えっ。  [voice 882]
            voice "ch8_h_031"
            h "Eh.{#ch8_h_031}"
            # JA[882]: えっ。
            # [SPRITE lay5 image=+429 dir=2A → s 3 sad]
            $ show_sprites(("s 3 sad", "h 2 shy"))
            # サイト：い、いや、そういうわけじゃないんですけど、 / なんか、普通の女の子に思えて……。 / それで……。  [voice 13605]
            voice "ch8_s_046"
            s "N-no, that's not it. / You just seem like an ordinary girl to me… / And so…{#ch8_s_046}"
            # JA[13605]: い、いや、そういうわけじゃないんですけど、 / なんか、普通の女の子に思えて……。 / それで……。
            # → next scene 416

        "Because princess is also human.{#ch8_c005}":
            # JA: お姫さまも同じ人間だから
            # [SPRITE lay8 image=+786 dir=1C → h 2]
            # [SPRITE lay5 image=+390 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2"))
            # [BGM play=+16 → t15]
            play music t15 fadein 1.0
            # [BG stage image=+42 → id(42)]
            $ fade_fx("id(42)")
            # [SPRITE lay5 image=+423 dir=2A → s 3]
            $ show_sprites(("s 3", "h 2"))
            # サイト：お姫さまも同じ人間だし。  [voice 13606]
            voice "ch8_s_047"
            s "Because you're human, just like me.{#ch8_s_047}"
            # JA[13606]: お姫さまも同じ人間だから。
            # [SPRITE lay8 image=+792 dir=1C → h 2 sad]
            $ show_sprites(("s 3", "h 2 sad"))
            # アンリエッタ：同じ、人間……？  [voice 883]
            voice "ch8_h_032"
            h "Same… human…?{#ch8_h_032}"
            # JA[883]: 同じ、人間……？.
            # [SPRITE lay5 image=+390 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2 sad"))
            # サイト：そうですよ。 / お姫さまは、そりゃ女王様で魔法使いですけど、 / 人間なのは同じじゃないですか。  [voice 13607]
            voice "ch8_s_048"
            s "That's right. / You're a queen and a mage, but / you're still human, aren't you?{#ch8_s_048}"
            # JA[13607]: そうですよ。 / お姫さまは、そりゃ女王様で魔法使いですけど、 / 人間なのは同じじゃないですか。
            # サイト：別に神様じゃないんだから、 / そこまで身分を強調する必要はないんじゃない / ですか？  [voice 13608]
            voice "ch8_s_049"
            s "You're not a god, after all. / Is there really a need / to emphasize your status so much?{#ch8_s_049}"
            # JA[13608]: 別に神様じゃないんだから、 / そこまで身分を強調する必要はないんじゃない / ですか？
            # → next scene 416

        "Because I'm just acting normal.{#ch8_c006}":
            # JA: なんとなく普通にしてるだけ
            # [SPRITE lay8 image=+786 dir=1C → h 2]
            # [SPRITE lay5 image=+390 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2"))
            # [BGM play=+16 → t15]
            play music t15 fadein 1.0
            # [BG stage image=+42 → id(42)]
            $ fade_fx("id(42)")
            # [SPRITE lay5 image=+423 dir=2A → s 3]
            $ show_sprites(("s 3", "h 2"))
            # サイト：なんとなく普通にしてるだけですよ。  [voice 13609]
            voice "ch8_s_050"
            s "I'm just acting normal, that's all.{#ch8_s_050}"
            # JA[13609]: なんとなく普通にしてるだけですよ。
            # [SPRITE lay8 image=+792 dir=1C → h 2 sad]
            $ show_sprites(("s 3", "h 2 sad"))
            # アンリエッタ：なんとなく……なのですか？ / もっとこう、考えがあるのではなくて？  [voice 884]
            voice "ch8_h_033"
            h "Just… like that? / You don't have any deeper reason?{#ch8_h_033}"
            # JA[884]: なんとなく……なのですか？ / もっとこう、考えがあるのではなくて？
            # [SPRITE lay5 image=+390 dir=1A → s 1]
            $ show_sprites(("s 1", "h 2 sad"))
            # サイト：なーんにも考えてないんです。 / だから、自然と普通の女の子扱い / しちゃうのかな。  [voice 13610]
            voice "ch8_s_051"
            s "I'm not thinking about anything at all. / So I guess I just naturally treat you like an ordinary girl.{#ch8_s_051}"
            # JA[13610]: なーんにも考えてないです。 / だから、自然と普通の女の子扱い / しちゃうのかな。
            # → next scene 416


    # ==== SCENE 416 (переход после вариантов) ====
    # [SPRITE lay8 image=+794 dir=1C → h 2 shy]
    # [SPRITE lay5 image=+429 dir=2A → s 3 sad]
    $ show_sprites(("s 3 sad", "h 2 shy"))
    # [BGM play=+16 → t15]
    play music t15 fadein 1.0
    # [BG stage image=+42 → id(42)]
    $ fade_fx("id(42)")
    # [SPRITE lay8 image=+786 dir=1C → h 2]
    $ show_sprites(("s 3 sad", "h 2"))
    # アンリエッタ：そうでしたね。 / 使い魔さんは他の世界の方でしたね。  [voice 885]
    voice "ch8_h_034"
    h "That's right. / You're from another world, after all.{#ch8_h_034}"
    # JA[885]: そうでしたね。 / 使い魔さんは他の世界の方でしたね。
    # [SPRITE lay5 image=+429 dir=2A → s 3 sad]
    $ show_sprites(("s 3 sad", "h 2"))
    # サイト：あ、だからと言って、別にお姫さまを / 軽んじてるってわけじゃないです。 / むしろ尊敬してます。  [voice 13611]
    voice "ch8_s_052"
    s "Ah, that's not to say I don't respect you. / In fact, I admire you.{#ch8_s_052}"
    # JA[13611]: あ、だからと言って、別にお姫さまを / 軽んじるってわけじゃないです。 / むしろ尊敬してます。
    # [SPRITE lay8 image=+788 dir=1C → h 2 happy]
    $ show_sprites(("s 3 sad", "h 2 happy"))
    # アンリエッタ：ありがとうございます。  [voice 886]
    voice "ch8_h_035"
    h "Thank you.{#ch8_h_035}"
    # JA[886]: ありがとうございます。
    # [SPRITE lay5 image=+431 dir=2A → s 3 shy]
    $ show_sprites(("s 3 shy", "h 2 happy"))
    # サイト：あ、いえ……。  [voice 13612]
    voice "ch8_s_053"
    s "Ah, no…{#ch8_s_053}"
    # JA[13612]: あ、いえ……。

    # [SPRITE lay8 image=+786 dir=1C → h 2]
    $ show_sprites(("s 3 shy", "h 2"))
    # アンリエッタ：でも、知っていますか？  [voice 887]
    voice "ch8_h_036"
    h "But did you know?{#ch8_h_036}"
    # JA[887]: でも、知っていますか？
    # アンリエッタ：ここトリステインでは、 / 女王の寝顔をずっと見ていたなど、 / 大変に無礼な行為なのですよ。  [voice 888]
    voice "ch8_h_037"
    h "In Tristain, / watching the Queen sleep like that / is considered extremely rude.{#ch8_h_037}"
    # JA[888]: ここトリステインでは、 / 女王の寝顔をずっと見ていたなど、 / 大変に無礼な行為なのですよ。
    # [SPRITE lay5 image=+429 dir=2A → s 3 sad]
    $ show_sprites(("s 3 sad", "h 2"))
    # サイト：え、あ、はい。  [voice 13613]
    voice "ch8_s_054"
    s "Er, ah, yes.{#ch8_s_054}"
    # JA[13613]: え、あ、はい。
    # [SPRITE lay8 image=+792 dir=1C → h 2 sad]
    $ show_sprites(("s 3 sad", "h 2 sad"))
    # アンリエッタ：いくらこの世界の生活習慣を知らないとはいえ、 / 許されることではありません。 / 反省してください。  [voice 889]
    voice "ch8_h_038"
    h "No matter how unfamiliar you are with our customs, / it's not excusable. / Reflect on your behavior.{#ch8_h_038}"
    # JA[889]: いくらこの世界の生活習慣を知らないとはいえ、 / 許されることではありません。 / 反省してください。
    # [SPRITE lay5 image=+396 dir=1A → s 1 sad]
    $ show_sprites(("s 1 sad", "h 2 sad"))
    # サイト：は、はい。 / すみませんでした。  [voice 13614]
    voice "ch8_s_055"
    s "Y-yes. / I'm sorry.{#ch8_s_055}"
    # JA[13614]: は、はい。 / すみませんでした。
    # [SPRITE lay8 image=+788 dir=1C → h 2 happy]
    $ show_sprites(("s 1 sad", "h 2 happy"))
    # アンリエッタ：ちゃんと聞いているのですか？  [voice 890]
    voice "ch8_h_039"
    h "Are you really listening?{#ch8_h_039}"
    # JA[890]: ちゃんと聞いているのですか？
    # [SPRITE lay5 image=+429 dir=2A → s 3 sad]
    $ show_sprites(("s 3 sad", "h 2 happy"))
    # サイト：は、はい。 / 聞いてます。  [voice 13615]
    voice "ch8_s_056"
    s "Y-yes. / I'm listening.{#ch8_s_056}"
    # JA[13615]: は、はい。 / 聞いてます。
    # [SPRITE lay8 hide]
    # [SPRITE lay5 hide]
    # [SPRITE lay8 image=+787 level=140 dir=1C → id(787)]
    $ show_sprites(("id(787)"))
    # アンリエッタ：本当に？  [voice 891]
    voice "ch8_h_040"
    h "Really?{#ch8_h_040}"
    # JA[891]: 本当に？。
    # サイト：本当ですってば。 / そんなに詰め寄らなくても……。  [voice 13616]
    voice "ch8_s_057"
    s "I'm telling you the truth. / You don't need to press me so hard…{#ch8_s_057}"
    # JA[13616]: 本当ですってば。 / そんなに詰め寄らなくても……。
    # → next scene 417 / → next scene 418
    # Часть 1 заканчивается: сцена 417 — в script-ch8_2.rpy.
    jump ch8_2
