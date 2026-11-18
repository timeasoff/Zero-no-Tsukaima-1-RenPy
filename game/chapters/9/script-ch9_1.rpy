# Глава 9, часть 1 (сцены 429–430): «魅惑のお姫さま» — типовая структура,
# Знакомство Сайто/Гарена, падение в старый колодец,
# разговор Сайто/Харюны, поцелуй Анриетты, наказание Луизы, конец главы.
# Источник: ps2_source/chapters/chapter_10_魅惑のお姫さま.txt (SCENE 429-430).
# Точные аргументы: ps2_source/events_full/chapter_10_魅惑のお姫さま.txt.
#
# Голоса: 110 (сцены 429-430). Нумерация ch9_<spk>_<NNN> — с 001 по говорящему.
#   s: 8128-8161 (17)+9304-9321 (18) = 35
#   h: 261-271 (11)+449-458 (10) = 21
#   l: 4601-4602 (2)+4885-4893 (9) = 11
#   g: 1410-1411 (2)
#   ha: 1826-1836 (11)
#   d: 1221-1222 (2)
#   PS2 voice IDs: s=8128-8161,9304-9321; h=261-271,449-458; l=4601-4602,4885-4893;
#     g=1410-1411; ha=1826-1836; d=1221-1222
# Спрайты: id → имя по references/sprite_id_map.csv; PROVISIONAL для не подтверждённых.
# Фоны: id(2)=white, id(12)=louise_room_night, id(28)=yard_night, id(35)=id(35) (ПУСТО),
#   id(58)=town_square, id(88)=sky, id(1145)=overlay, id(1169)=overlay.
# CG: id(268)=id(268), id(293)=id(293), id(294)=id(294), id(295)=id(295), id(296)=id(296)
#   (все ПУСТЫ в image_id_map.csv — заглушки id(K), требуют решения человека).
# BGM: bgm play=+19→t18, +10→t9, +20→t19, +22→t21, +17→t16, +30→t29, +4→t3 — все есть.
# SE: se0 play=+57/+56/+62/+61; se1 stop=1 — не переносятся (SE заглушка).
# Не переносятся: MOVIE(1) — movie(1); beginSkip/endSkip — пропускается;
#   waitSEStop/waitLoad/waitAction/waitTime — паузы/задержки.
#
# К обращению Анриетты: по addresses.md — «Ваше Высочество / мадемуазель»
#   (принцесса до восшествия на престол). В JA Сайто говорит «アンリエッタ», Луиза — «姫さま».

label ch9:
    $ tndl(None)
    # Титульный монтаж → overlay_screen (образ «overlay»).
    call overlay_screen("overlay", "Chapter Nine: 'The Enchanting Princess'{#ch9_title}", isUseBlur=False, text_mode="black") from _call_overlay_screen_14
    pause(2)


    # ==== SCENE 429 ====
    # [TITLE title("魅惑のお姫さま")] — входит в титульный монтаж overlay_screen
    # [BG stage image=+2] [TRANS trans("crossfade", 500)]
    # [BG stage image=+1145] [TRANS trans("crossfade", 1000)]
    # [BG stage image=+1169] [TRANS trans("crossfade", 1000)]
    # [BG stage image=+1145] [TRANS trans("crossfade", 1000)]
    # [BG stage image=+2] [TRANS trans("crossfade", 2000)]
    # [BG stage image=+12] [TRANS trans("crossfade", 1000)]
    # [BGM bgm play=+19 → t18]
    $ show_sprites()
    # [SPRITE lay5 image=+423 → s 3]
    $ show_sprites(("s 3"))
    # サイト：ふう……。 / あれからしばらく経つのに、 / まだ根に持ってるな、ルイズのやつ。  [voice 8128]
    voice "ch9_s_001"
    s "Hah… / It's been a while since then, / but Louise is still holding a grudge. {#ch9_s_001}"
    # JA[8128]: サイト：ふう……。 / あれからしばらく経つのに、 / まだ根に持ってるな、ルイズのやつ。
    # サイト：お姫さまのキスは不可抗力だって言ってんのに。  [voice 8129]
    voice "ch9_s_002"
    s "I said it was involuntary, the Princess's kiss… {#ch9_s_002}"
    # JA[8129]: お姫さまのキスは不可抗力だって言ってんのに。
    # [SPRITE lay5 image=+390 → s 1]
    $ show_sprites(("s 1"))
    # サイト：そういえば、お姫さまは今頃どうしてるかな。 / 頑張って仕事をしてるのかな？  [voice 8130]
    voice "ch9_s_003"
    s "Come to think of it, what's the Princess up to now? / Is she working hard? {#ch9_s_003}"
    # JA[8130]: サイト：そういえば、お姫さまは今頃どうしてるかな。 / 頑張って仕事をしてるのかな？
    # [SPRITE lay5 image=+429 → s 3 sad]
    $ show_sprites(("s 3 sad"))
    # サイト：今回の事件解決で、周りの支持を / 増やしたらしいけど……。 / 苦労が絶えないよなあ、本当。  [voice 8131]
    voice "ch9_s_004"
    s "I hear she gained more support after solving the incident… / But I bet it's still hard. {#ch9_s_004}"
    # JA[8131]: サイト：今回の事件解決で、周りの支持を / 増やしたらしいけど……。 / 苦労が絶えないよなあ、本当。
    # サイト：俺、気軽に見守りますなんて言っちゃったけど、 / 簡単に会えるような相手じゃないし……。  [voice 8132]
    voice "ch9_s_005"
    s "I said I'd keep an eye on her casually… / But she's not someone easy to meet. {#ch9_s_005}"
    # JA[8132]: サイト：俺、気軽に見守りますなんて言っちゃったけど、 / 簡単に会えるような相手じゃないし……。
    # [SE se0 play=+57] — не переносится
    # [SPRITE lay5 image=+423 → s 3]
    $ show_sprites(("s 3"))
    # サイト：あれ、ルイズ。 / なんか忘れ物か？  [voice 8133]
    voice "ch9_s_006"
    s "Hmm? Louise. / Did you forget something? {#ch9_s_006}"
    # JA[8133]: サイト：あれ、ルイズ。 / なんか忘れ物か？
    # [BGM bgm stop=1000] → fadeout
    stop music fadeout 1.0
    # [BGM bgm play=+10 → t9]
    play music t9 fadein 1.0
    # [SE se0 play=+56] — не переносится
    # [SPRITE lay5 x=224, y=0]
    # [SPRITE lay8 image=+797 → h 2]
    $ show_sprites(("s 1", "h 2"))
    # アンリエッタ：今晩は、使い魔さん。 / ルイズなら、お風呂に行ったようですけど。  [voice 261]
    voice "ch9_h_001"
    h "Good evening, familiar. / Louise went to take a bath. {#ch9_h_001}"
    # JA[261]: アンリエッタ：今晩は、使い魔さん。 / ルイズなら、お風呂に行ったようですけど。
    # [SPRITE lay5 image=+429 → s 3 sad]
    $ show_sprites(("s 3 sad", "h 2"))
    # サイト：……。  [voice 8134]
    voice "ch9_s_007"
    s "…{#ch9_s_007}"
    # JA[8134]: サイト：……。
    # [SPRITE lay5 image=+427 → s 3 angry]
    $ show_sprites(("s 3 angry", "h 2"))
    # サイト：（はっ！ /　これはルイズの罠か！）  [null]
    s "(Wait! / Is this Louise's trap?){#ch9_s_008}"
    # JA[null]: サイト：（はっ！ /　これはルイズの罠か！）
    # [SPRITE lay5 image=+396 → s 1 sad]
    $ show_sprites(("s 1 sad", "h 2"))
    # サイト：（例の魔法で、お姫さまの幻を俺に見せて、 /　ここで俺が飛びついたところで / お仕置きって罠！？）  [null]
    s "(That magic… showing me an illusion of the Princess, / and here I jump at her, / and she punishes me?!){#ch9_s_009}"
    # JA[null]: サイト：（例の魔法で、お姫さまの幻を俺に見せて、 /　ここで俺が飛びついたところで / お仕置きって罠！！？）
    # [SPRITE lay8 image=+803 → h 2 sad]
    $ show_sprites(("s 1 sad", "h 2 sad"))
    # アンリエッタ：どうしたのですか使い魔さん。 / 熱でもあるのですか……。  [voice 262]
    voice "ch9_h_002"
    h "What's wrong, my familiar? / Do you have a fever…? {#ch9_h_002}"
    # JA[262]: アンリエッタ：どうしたのですか使い魔さん。 / 熱でもあるのですか……。
    # [SPRITE lay5 image=+394 → s 1 angry]
    $ show_sprites(("s 1 angry", "h 2 sad"))
    # サイト：おわあっ！？ / ひんやりとして柔らかい肌の感触が！？  [voice 8135]
    voice "ch9_s_008"
    s "Ow!? / Cold and soft skin?! {#ch9_s_010}"
    # JA[8135]: サイト：おわあっ！？ / ひんやりとして柔らかい肌の感触が！？
    # [SPRITE lay5 image=+396 → s 1 sad]
    $ show_sprites(("s 1 sad", "h 2 sad"))
    # サイト：ええと、お姫さま、本物ですか？  [voice 8136]
    voice "ch9_s_009"
    s "Um, Princess, are you real? {#ch9_s_011}"
    # JA[8136]: サイト：ええと、お姫さま、本物ですか？
    # [SPRITE lay8 image=+799 → h 2 happy]
    $ show_sprites(("s 1 sad", "h 2 happy"))
    # アンリエッタ：いやですわ。 / 本物ですよ？ / ちょっとだけ……抜け出してきましたの。  [voice 263]
    voice "ch9_h_003"
    h "No. I'm the real one, you know? I just… snuck out a little. {#ch9_h_003}"
    # JA[263]: アンリエッタ：いやですわ。 / 本物ですよ？ / ちょっとだけ……抜け出してきましたの。
    # [SPRITE lay5 image=+429 → s 3 sad]
    $ show_sprites(("s 3 sad", "h 2 happy"))
    # サイト：ちょっとだけって……。 / そんなことしたら、王宮が大騒ぎに / なってるんじゃないんですか！？  [voice 8137]
    voice "ch9_s_010"
    s "Just a little?! / Wouldn't the royal palace be in an uproar?! {#ch9_s_012}"
    # JA[8137]: サイト：ちょっとだけって……。 / そんなことしたら、王宮が大騒ぎに / なってるんじゃないんですか！？
    # [SPRITE lay8 image=+797 → h 2]
    $ show_sprites(("s 3 sad", "h 2"))
    # アンリエッタ：少しの間なら大丈夫です。 / 代わりの者も用意しましたから。  [voice 264]
    voice "ch9_h_004"
    h "It's fine for a little while. / I've arranged a substitute. {#ch9_h_004}"
    # JA[264]: アンリエッタ：少しの間なら大丈夫です。 / 代わりの者も用意しましたから。
    # [SPRITE lay5 image=+396 → s 1 sad]
    $ show_sprites(("s 1 sad", "h 2"))
    # サイト：いや、大丈夫じゃないですよ。 / それにしても、またどうしてこんなところへ？ / ひょっとして、ルイズになにか用事ですか？  [voice 8138]
    voice "ch9_s_011"
    s "No, it's not fine at all. / And why are you here again? / Could it be you have business with Louise? {#ch9_s_013}"
    # JA[8138]: サイト：いや、大丈夫じゃないですよ。 / それでも、またどうしてこんなところへ？ / ひょっとして、ルイズになにか用事ですか？
    # アンリエッタ：実は、しばらくの間頑張って公務に励んで / おりましたが、ちょっと寂しくなったので、 / 使い魔さんのいる学院まで来たというわけです。  [voice 265]
    voice "ch9_h_005"
    h "Actually, I've been working hard on official duties / for a while now, but I got a little lonely, / so I came to the academy where my familiar is. {#ch9_h_005}"
    # JA[265]: アンリエッタ：実は、しばらくの間頑張って公務に励んで / おりましたが、ちょっと寂しくなったので、 / 使い魔さんのいる学院まで来たというわけです。
    # サイト：つながりがよく見えないんですが。  [voice 8139]
    voice "ch9_s_012"
    s "I don't see the connection. {#ch9_s_014}"
    # JA[8139]: サイト：つながりがよく見えないんですが。
    # アンリエッタ：そうですか？  [voice 266]
    voice "ch9_h_006"
    h "Is that so? {#ch9_h_006}"
    # JA[266]: アンリエッタ：そうですか？
    # [SPRITE lay5 image=+429 → s 3 sad]
    $ show_sprites(("s 3 sad", "h 2"))
    # サイト：ちなみにですね、こうして俺がお姫さまと / 会ってるところを見られたら、 / どうなるんでしょう。  [voice 8140]
    voice "ch9_s_013"
    s "By the way, if someone saw me / talking with you like this, / what would happen? {#ch9_s_015}"
    # JA[8140]: サイト：ちなみにですね、こうして俺がお姫さまと / 会ってるところを見られたら、 / どうなるんでしょう。
    # [SPRITE lay8 image=+799 → h 2 happy]
    $ show_sprites(("s 3 sad", "h 2 happy"))
    # アンリエッタ：そうですねえ、 / 銃士隊あたりに知られたら大変怒ると思います。  [voice 267]
    voice "ch9_h_007"
    h "I suppose so. / The Musketeers would surely be furious. {#ch9_h_007}"
    # JA[267]: アンリエッタ：そうですねえ、 / 銃士隊あたりに知られたら大変怒ると思います。
    # [SPRITE lay5 image=+394 → s 1 angry]
    $ show_sprites(("s 1 angry", "h 2 happy"))
    # サイト：俺、極悪人決定！？  [voice 8141]
    voice "ch9_s_014"
    s "I'm an evildoer?! {#ch9_s_016}"
    # JA[8141]: サイト：俺、極悪人決定！？
    # [SPRITE lay8 image=+803 → h 2 sad]
    $ show_sprites(("s 1 angry", "h 2 sad"))
    # アンリエッタ：やはり、見られるといけないんでしょうか。  [voice 268]
    voice "ch9_h_008"
    h "I shouldn't be seen, after all? {#ch9_h_008}"
    # JA[268]: アンリエッタ：やはり、見られるといけないんでしょうか。
    # [SPRITE lay5 image=+396 → s 1 sad]
    $ show_sprites(("s 1 sad", "h 2 sad"))
    # サイト：すみません、俺を助けると思って、 / もう少し人目を忍んでください。  [voice 8142]
    voice "ch9_s_015"
    s "Sorry, I thought you were helping me, / but please be more discreet. {#ch9_s_017}"
    # JA[8142]: サイト：すみません、俺を助けると思って、 / もう少し人目を忍んでください。
    # [SPRITE lay8 image=+797 → h 2]
    $ show_sprites(("s 1 sad", "h 2"))
    # アンリエッタ：分かりました。 / では、こっそり来ればよろしいのですね。  [voice 269]
    voice "ch9_h_009"
    h "Understood. / So I should come secretly? {#ch9_h_009}"
    # JA[269]: アンリエッタ：分かりました。 / では、こっそり来ればよろしいのですね。
    # [SPRITE lay5 image=+429 → s 3 sad]
    $ show_sprites(("s 3 sad", "h 2"))
    # サイト：いや、まあ、そうですけど。 / って、次もあるような言い方！？  [voice 8143]
    voice "ch9_s_016"
    s "Well, yes, that's… / But you make it sound like there'll be a next time!? {#ch9_s_018}"
    # JA[8143]: サイト：いや、まあ、そうですけど。 / って、次もあるような言い方！？
    # [SPRITE lay5 image=+394 → s 1 angry]
    $ show_sprites(("s 1 angry", "h 2"))
    # サイト：と、とにかく、ここにいたらいつルイズが / 帰ってくるか分かりません。  [voice 8144]
    voice "ch9_s_017"
    s "Anyway, if we stay here we don't know when Louise / will come back. {#ch9_s_019}"
    # JA[8144]: サイト：と、とにかく、ここにいたらいつルイズが / 帰ってくるか分かりません。
    # サイト：違うところに行きましょう！  [voice 8145]
    voice "ch9_s_018"
    s "Let's go somewhere else! {#ch9_s_020}"
    # JA[8145]: サイト：違うところに行きましょう！
    # アンリエッта：は、はい。  [voice 270]
    voice "ch9_h_010"
    h "Y-yes. {#ch9_h_010}"
    # JA[270]: アンリエッタ：は、はい。
    # [BGM bgm stop=1000] → fadeout
    stop music fadeout 1.0
    # [SPRITE lay8 hide]
    # [SPRITE lay5 hide]
    # [BG stage hide]
    $ show_sprites()
    # [BG stage image=+28 → yard_night] [TRANS trans("crossfade", 1000)]
    # [BGM bgm play=+20 → t19]
    play music t19 fadein 1.0
    $ fade_fx("yard_night")
    # [SPRITE lay5 image=+396 → s 1 sad]
    $ show_sprites(("s 1 sad"))
    # サイト：こ、ここなら大丈夫かな……。  [voice 8146]
    voice "ch9_s_019"
    s "Is it safe here…? {#ch9_s_021}"
    # JA[8146]: サイト：こ、ここなら大丈夫かな……。
    # [SPRITE lay5 hide]
    # [SPRITE lay4 image=+557 → g 1 happy]
    $ show_sprites(("g 1 happy"))
    # ギーシュ：おお！ / モンモランシー、そこにいるのかい? / きみに渡すプレゼントが、やっと完成したんだ。  [voice 1410]
    voice "ch9_g_001"
    g "Oh! / Montmorency, are you there? / I finally finished the present I wanted to give you. {#ch9_g_001}"
    # JA[1410]: ギーシュ：おお！ / モンモランシー、そこにいるのかい? / きみに渡すプレゼントが、やっと完成したんだ。
    # サイト：（うわー！？ /　なんでよりによってギーシュが /　こんなところにー！）  [null]
    s "(Wah!? / Why out of all people, Guiche / is in such a place!){#ch9_s_022}"
    # JA[null]: サイト：（うわー！？ /　なんでよりによってギーシュが /　こんなところにー！）
    # [SPRITE lay4 hide]
    $ show_sprites(("s 1 sad"))
    # [SPRITE lay5 image=+394 → s 1 angry]
    $ show_sprites(("s 1 angry"))
    # サイト：逃げなきゃ……って、ああっ！  [voice 8147]
    voice "ch9_s_020"
    s "I have to run… waaah! {#ch9_s_023}"
    # JA[8147]: サイト：逃げなきゃ……って、ああっ！
    # [SPRITE lay5 hide]
    # [SPRITE lay8 image=+768 → h 2 scared]
    $ show_sprites(("h 2 scared"))
    # アンリエッタ：きゃっ！？  [voice 271]
    voice "ch9_h_011"
    h "Kyaa!? {#ch9_h_011}"
    # JA[271]: アンリエッタ：きゃっ！？
    # [SPRITE lay8 hide]
    # [SPRITE lay4 image=+561 → g 1 sad]
    $ show_sprites(("g 1 sad"))
    # ギーシュ：あれ？ / 誰かいたと思ったのに、気のせいかな。  [voice 1411]
    voice "ch9_g_002"
    g "Huh? / I thought I saw someone, / but I guess it was nothing. {#ch9_g_002}"
    # JA[1411]: ギーシュ：あれ？ / 誰かいたと思ったのに、気のせいかな。
    # [BGM bgm stop=1000] → fadeout
    stop music fadeout 1.0
    # [SPRITE lay4 hide]
    # [BG stage hide]
    $ show_sprites()
    # [EVENT_CG event image=+296 → id(296)] — колодец, CG
    $ dissolve_fx("id(296)", type="cg")
    # [TRANS trans("crossfade", 1000)] — fade_fx
    # [BGM bgm play=+22 → t21]
    play music t21 fadein 1.0
    # サイト：あいたたた……。 / だ、大丈夫ですか、お姫さま。  [voice 8148]
    voice "ch9_s_021"
    s "Ouch… / Are you okay, Princess? {#ch9_s_024}"
    # JA[8148]: サイト：あいたたた……。 / だ、大丈夫ですか、お姫さま。
    # [EVENT_CG event image=+295 → id(295)]
    # アンリエッタ：あ、わたくしは大丈夫ですけど……。 / 使い魔さんは大丈夫でしょうか。 / わたくし、下敷きにしてしまいました。  [voice 272]
    voice "ch9_h_012"
    h "I'm fine, but… / Is my familiar all right? / I… fell on top of you. {#ch9_h_012}"
    # JA[272]: アンリエッタ：あ、わたくしは大丈夫ですけど……。 / 使い魔さんは大丈夫でしょうか。 / わたくし、下敷きにしてしまいました。
    # サイト：あ、平気ですよ、これくらい。 / むしろ考えようによっては役得で。  [voice 8149]
    voice "ch9_s_022"
    s "I'm fine, it's nothing. / Well, you could say it's a perk. {#ch9_s_025}"
    # JA[8149]: サイト：あ、平気ですよ、これくらい。 / むしろ考えようによっては役得で。
    # Аンリエッタ：はい？  [voice 273]
    voice "ch9_h_013"
    h "Huh? {#ch9_h_013}"
    # JA[273]: アンリエッタ：はい？
    # サイト：いえ、こっちの話です。  [voice 8150]
    voice "ch9_s_023"
    s "Oh, nothing. {#ch9_s_026}"
    # JA[8150]: サイト：いえ、こっちの話です。
    # アンリエッта：それにしても、ここはいったいどこです？  [voice 274]
    voice "ch9_h_014"
    h "By the way, where on earth is this? {#ch9_h_014}"
    # JA[274]: アンリエッタ：それにしても、ここはいったいどこです？
    # サイト：たぶん、今は使っていない古井戸ですね。 / 上を塞いでなかったのかな。  [voice 8151]
    voice "ch9_s_024"
    s "I think this is an old well not in use now. / Maybe they didn't cover the top. {#ch9_s_027}"
    # JA[8151]: サイト：たぶん、今は使っていない古井戸ですね。 / 上を塞いでなかったのかな。
    # サイト：よっと……うわわっ。  [voice 8152]
    voice "ch9_s_025"
    s "All right… whoa! {#ch9_s_028}"
    # JA[8152]: サイト：よっと……うわわっ。
    # サイト：この壁じゃ、脆すぎて登れませんね。 / 俺だけなら無理すれば登れるかと / 思ったんですが……。  [voice 8153]
    voice "ch9_s_026"
    s "These walls are too crumbly to climb. / I might manage alone / if I pushed myself… {#ch9_s_029}"
    # JA[8153]: サイト：この壁じゃ、脆すぎて登れませんね。 / 俺だけなら無理すれば登れるかと / 思ったんですが……。
    # アンリエッタ：困りましたわ。 / どうしましょう。  [voice 275]
    voice "ch9_h_015"
    h "What a trouble. / What shall we do? {#ch9_h_015}"
    # JA[275]: アンリエッタ：困りましたわ。 / どうしましょう。
    # サイト：気のせいか、あんまり困ってるようには / 聞こえませんけど……。  [voice 8154]
    voice "ch9_s_027"
    s "Am I imagining it, or / you don't sound too worried? {#ch9_s_030}"
    # JA[8154]: サイト：気のせいか、あんまり困ってるようには / 聞こえませんけど……。
    # サイト：お姫さま、魔法で宙に浮いたりとか、 / 空を飛んで上まであがったりできます？  [voice 8155]
    voice "ch9_s_028"
    s "Princess, can you float in the air with magic, / or fly up? {#ch9_s_031}"
    # JA[8155]: サイト：お姫さま、魔法で宙に浮いたりとか、 / 空を飛んで上まであがったりできます？
    # アンリエッта：ええ、そういう魔法はありますし、 / わたくし覚えておりますけど。  [voice 276]
    voice "ch9_h_016"
    h "Yes, there is such magic, / and I know it. {#ch9_h_016}"
    # JA[276]: アンリエッタ：ええ、そういう魔法はありますし、 / わたくし覚えておりますけど。
    # サイト：うわー、助かった。 / 一時はどうなることかと思った。  [voice 8156]
    voice "ch9_s_029"
    s "Phew, thank goodness. / I was worried for a moment. {#ch9_s_032}"
    # JA[8156]: サイト：うわー、助かった。 / 一時はどうなることかと思った。
    # [EVENT_CG event image=+294 → id(294)]
    $ dissolve_fx("id(294)", type="cg")
    # アンリエッта：でもわたくし、杖を持って来ておりませんので、 / 魔法は使えませんわ。  [voice 277]
    voice "ch9_h_017"
    h "But I didn't bring my wand, / so I can't use magic. {#ch9_h_017}"
    # JA[277]: アンリエッタ：でもわたくし、杖を持って来ておりませんので、 / 魔法は使えませんわ。
    # サイト：はい？  [voice 8157]
    voice "ch9_s_030"
    s "Huh? {#ch9_s_033}"
    # JA[8157]: サイト：はい？
    # サイト：ええと、それじゃあれですか。 / ここから登って脱出する手段はない / ということですか？  [voice 8158]
    voice "ch9_s_031"
    s "Um, so / there's no way to escape by climbing out? {#ch9_s_034}"
    # JA[8158]: サイト：ええと、それじゃあれですか。 / ここから登って脱出する手段はない / ということですか？
    # [EVENT_CG event image=+296 → id(296)]
    $ dissolve_fx("id(296)", type="cg")
    # アンリエッта：ええと、そうなりますわね。  [voice 278]
    voice "ch9_h_018"
    h "I suppose so. {#ch9_h_018}"
    # JA[278]: アンリエッタ：ええと、そうなりますわね。
    # アンриетта：でも、誰か人を呼べば、ロープを下ろして / もらって出られるのではありませんか？  [voice 279]
    voice "ch9_h_019"
    h "But if we call someone, / they could lower a rope, couldn't they? {#ch9_h_019}"
    # JA[279]: アンリエッタ：でも、誰か人を呼べば、ロープを下ろして / もらって出られるのではありませんか？
    # サイト：それはそのとおりですが、 / その場合、俺の命がピンチになります。  [voice 8159]
    voice "ch9_s_032"
    s "That's true, but / my life would be in danger then. {#ch9_s_035}"
    # JA[8159]: サイト：それはそのとおりですが、 / その場合、俺の命がピンチになります。
    # アンリエッта：あら。 / それでは、なにか自力で助かる方法を / 考えなければいけませんね。  [voice 280]
    voice "ch9_h_020"
    h "Oh my. / Then we must think of a way / to save ourselves. {#ch9_h_020}"
    # JA[280]: アンリエッタ：あら。 / それでは、なにか自力で助かる方法を / 考えなければいけませんね。
    # サイト：なにかありますか！？  [voice 8160]
    voice "ch9_s_033"
    s "Do you have any ideas?! {#ch9_s_036}"
    # JA[8160]: サイト：なにかありますか！？
    # [EVENT_CG event image=+295 → id(295)]
    $ dissolve_fx("id(295)", type="cg")
    # アンриетта：さあ……ちょっと思いつきません。  [voice 281]
    voice "ch9_h_021"
    h "Well… I can't think of anything. {#ch9_h_021}"
    # JA[281]: アンリエッタ：さあ……ちょっと思いつきません。
    # [EVENT_CG event image=+294 → id(294)]
    $ dissolve_fx("id(294)", type="cg")
    # アンриетта：それに……これはこれでけっこう / 楽しいですから、いいのかなって。 / 使い魔さんと一緒ですし。  [voice 282]
    voice "ch9_h_022"
    h "Besides… this is actually / kind of fun, isn't it? / We're together, after all. {#ch9_h_022}"
    # JA[282]: アンリエッタ：それに……これはこれでけっこう / 楽しいですから、いいのかなって。 / 使い魔さんと一緒ですし。
    # サイト：なんだか嬉しい台詞のような気もするけど、 / それどころじゃないですよ。 / どうしたらいいんだーっ！？  [voice 8161]
    voice "ch9_s_034"
    s "Those sound like glad words, but / this isn't the time for that. / What should I do—?! {#ch9_s_037}"
    # JA[8161]: サイト：なんだか嬉しい台詞のような気もするけど、 / それどころじゃないですよ。 / どうしたらいいんだーっ！？
    # [SPRITE lay8 hide]
    # [SPRITE lay5 hide]
    # [BG stage hide]
    # [EVENT_CG event hide]
    # [SPRITE lay4 hide]
    # [SPRITE lay1 hide]
    $ show_sprites()
    # [BG stage image=+88 → sky] [TRANS trans("crossfade", 1000)]
    $ fade_fx("sky")
    # サイト：（結局、その後、朝に俺達は見つかり、 /　地獄のようなお仕置きをルイズに /　うけるのであった）  [null]
    s "(In the end, the next morning we were found, / and I received / Louise's hellish punishment.){#ch9_s_038}"
    # JA[null]: サイト：（結局、その後、朝に俺達は見つかり、 /　地獄のようなお仕置きをルイズに /　うけるのであった）
    # サイト：（それでもお姫さまは、楽しかったらしく、 /　俺にまた会いに来ると言って、帰っていった）  [null]
    s "(Still, the Princess seemed to enjoy herself, / and said she'd come see me again before leaving.){#ch9_s_039}"
    # JA[null]: サイト：（それでもお姫さまは、楽しかったらしく、 /　俺にまた会いに来ると言って、帰っていった）
    # [SE se1 stop=1] — не переносится
    # [BGM bgm stop=1000] → fadeout
    stop music fadeout 1.0
    # [SPRITE lay5 hide]
    # [BG stage hide]
    $ show_sprites()
    syssave()


    # ==== SCENE 430 ====
    # [MOVIE movie(1)] — MOVIE не портируется, заглушка (не переносится)
    play music t3 fadein 1.0
    # [BG stage image=+88 → sky] [TRANS trans("crossfade", 1000)]
    $ fade_fx("sky")
    # サイト：えっ、自立するってどういうことだよ？  [voice 9304]
    voice "ch9_s_035"
    s "Huh? What do you mean by 'become independent'? {#ch9_s_040}"
    # JA[9304]: サイト：えっ、自立するってどういうことだよ？
    # [SPRITE lay5 hide]
    # [BG stage hide]
    $ show_sprites()
    # [BG stage image=+58 → town_square] [TRANS trans("crossfade", 1000)]
    $ fade_fx("town_square")
    # [SPRITE lay7 image=+951 → ha 1]
    $ show_sprites(("ha 1"))
    # [SPRITE lay5 image=+394 → s 1 angry]
    $ show_sprites(("s 1 angry", "ha 1"))
    # ハルナ：うん、いつまでもこの学院で……。 / ルイズさん達の世話になってるのも / どうかなって思って。  [voice 1826]
    voice "ch9_ha_001"
    ha "Yeah, staying in this academy forever… / I wonder if being taken care of by Louise and the others / is okay. {#ch9_ha_001}"
    # JA[1826]: ハルナ：うん、いつまでもこの学院で……。 / ルイズさん達の世話になってるのも / どうかなって思って。
    # [SPRITE lay5 image=+429 → s 3 sad]
    $ show_sprites(("s 3 sad", "ha 1"))
    # サイト：そんなこといったら、俺なんかルイズに / 召喚されて以来、なんだかんだでずっと / この学院のお世話になってるんだけど。  [voice 9305]
    voice "ch9_s_036"
    s "Well, since I was summoned by Louise, / I've always been taken care of by this academy. {#ch9_s_041}"
    # JA[9305]: サイト：そんなこといったら、俺なんかルイズに / 召喚されて以来、なんだかんだでずっと / この学院のお世話になってるんだけど。
    # ハルナ：平賀くんはルイズさんの使い魔じゃない。 / お世話になって当然よ。 / でも、私はそうじゃないから……。  [voice 1827]
    voice "ch9_ha_002"
    ha "But you're Louise's familiar, Saito — of course you're taken care of. But I'm not… {#ch9_ha_002}"
    # JA[1827]: ハルナ：平賀くんはルイズさんの使い魔じゃない。 / お世話になって当然よ。 / でも、私はそうじゃないから……。
    # [SPRITE lay5 image=+390 → s 1]
    $ show_sprites(("s 1", "ha 1"))
    # サイト：そりゃそうなんだけどさ……。 / 俺達、この世界でたぶん２人だけの / 日本人じゃないか。  [voice 9306]
    voice "ch9_s_037"
    s "Well, that's true… / But we're probably the only two Japanese / in this world. {#ch9_s_042}"
    # JA[9306]: サイト：そりゃそうなんだけどさ……。 / 俺達、この世界でたぶん２人だけの / 日本人じゃないか。
    # サイト：それに、お互いのことを知らない / 間柄でもないんだしさ……。 / だから、学院で働くとかすれば……。  [voice 9307]
    voice "ch9_s_038"
    s "Besides, we're not strangers to each other. / So maybe I should work here… {#ch9_s_043}"
    # JA[9307]: サイト：それに、お互いのことを知らない / 間柄でもないんだしさ……。 / だから、学院で働くとかすれば……。
    # [SPRITE lay7 image=+959 → ha 1 shy]
    $ show_sprites(("ha 1 shy", "s 1"))
    # ハルナ：あのね、平賀くん……。 / 私、スカウトされちゃったんだ。  [voice 1828]
    voice "ch9_ha_003"
    ha "Hey, Saito… / I got scouted, you know. {#ch9_ha_003}"
    # JA[1828]: ハルナ：あのね、平賀くん……。 / 私、スカウトされちゃったんだ。
    # [SPRITE lay5 image=+396 → s 1 sad]
    $ show_sprites(("s 1 sad", "ha 1 shy"))
    # サイト：ス、スカウトって、なんの？  [voice 9308]
    voice "ch9_s_039"
    s "S-scouted? What's that? {#ch9_s_044}"
    # JA[9308]: サイト：ス、スカウトって、なんの？
    # [SPRITE lay7 image=+953 → ha 1 happy]
    $ show_sprites(("ha 1 happy", "s 1 sad"))
    # ハルナ：劇団よ、劇団。  [voice 1829]
    voice "ch9_ha_004"
    ha "Theater, the theater. {#ch9_ha_004}"
    # JA[1829]: ハルナ：劇団よ、劇団。
    # [SPRITE lay5 image=+396 → s 1 sad]
    $ show_sprites(("s 1 sad", "ha 1 happy"))
    # サイト：劇団って、あのウェザリーの劇団は / もうなくなったんだろ？  [voice 9309]
    voice "ch9_s_040"
    s "Theater? I mean, isn't Weatherly's theater / out of business? {#ch9_s_045}"
    # JA[9309]: サイト：劇団って、あのウェザリーの劇団は / もうなくなったんだろ？
    # ハルナ：違うの。 / あの劇を見てくれた別の劇団の人が、 / 私のことを気に入ってスカウトしてくれたのよ。  [voice 1830]
    voice "ch9_ha_005"
    ha "No. Another theater troupe saw that play / and scouted me because they liked me. {#ch9_ha_005}"
    # JA[1830]: ハルナ：違うの。 / あの劇を見てくれた別の劇団の人が、 / 私のことを気に入ってスカウトしてくれたのよ。
    # ハルナ：この際、いい機会だから、その劇団のお世話に / なろうと思ってね。  [voice 1831]
    voice "ch9_ha_006"
    ha "This is a good opportunity, / so I'm going to join that troupe. {#ch9_ha_006}"
    # JA[1831]: ハルナ：この際、いい機会だから、その劇団のお世話に / なろうと思ってね。
    # [SPRITE lay5 image=+396 → s 1 sad]
    $ show_sprites(("s 1 sad", "ha 1 happy"))
    # サイト：でもさ、劇団の世話になるってことは、 / 他の街への公演に出ることだってあるんだよな？  [voice 9310]
    voice "ch9_s_041"
    s "But being in a troupe means / there might be performances in other towns, right? {#ch9_s_046}"
    # JA[9310]: サイト：でもさ、劇団の世話になるってことは、 / 他の街への公演に出ることだってあるんだよな？
    # [SPRITE lay7 image=+957 → ha 1 sad]
    $ show_sprites(("ha 1 sad", "s 1 sad"))
    # ハルナ：うん、そうだね。 / 平賀くんとは会うことが少なく / なっちゃいそうだけどね。  [voice 1832]
    voice "ch9_ha_007"
    ha "Yeah. We probably won't see each other / as much anymore. {#ch9_ha_007}"
    # JA[1832]: ハルナ：うん、そうだね。 / 平賀くんとは会うことが少なく / なっちゃいそうだけどね。
    # ハルナ：でもね、私は楽しみにしてるんだ。 / この世界のいろんな街を見て回ることが / できるから。  [voice 1833]
    voice "ch9_ha_008"
    ha "But I'm looking forward to it. / I can see all sorts of towns in this world. {#ch9_ha_008}"
    # JA[1833]: ハルナ：でもね、私は楽しみにしてるんだ。 / この世界のいろんな街を見て回ることが / できるから。
    # ハルナ：ひょっとすると、日本へ戻るためのきっかけ / だって見つかるかもしれない。  [voice 1834]
    voice "ch9_ha_009"
    ha "Maybe I'll find a way back to Japan. {#ch9_ha_009}"
    # JA[1834]: ハルナ：ひょっとすると、日本へ戻るためのきっかけ / だって見つかるかもしれない。
    # [SPRITE lay5 image=+390 → s 1]
    $ show_sprites(("s 1", "ha 1 sad"))
    # サイト：そっか、そうだよな。  [voice 9311]
    voice "ch9_s_042"
    s "I see, that's right. {#ch9_s_047}"
    # JA[9311]: サイト：そっか、そうだよな。
    # [SPRITE lay7 image=+953 → ha 1 happy]
    $ show_sprites(("ha 1 happy", "s 1"))
    # ハルナ：だから平賀くん……。 / 良かったら、私のこと応援していてね。  [voice 1835]
    voice "ch9_ha_010"
    ha "So, Saito… / If you're willing, please support me. {#ch9_ha_010}"
    # JA[1835]: ハルナ：だから平賀くん……。 / 良かったら、私のこと応援していてね。
    # [SPRITE lay5 image=+392 → s 1 happy]
    $ show_sprites(("s 1 happy", "ha 1 happy"))
    # サイト：ああ、もちろんだとも！ / それから、日本へ帰る方法、 / お互いに頑張って見つけだそうぜ。  [voice 9312]
    voice "ch9_s_043"
    s "Ah, of course! / Let's both do our best / to find a way back to Japan. {#ch9_s_048}"
    # JA[9312]: サイト：ああ、もちろんだとも！ / それから、日本へ帰る方法、 / お互いに頑張って見つけだそうぜ。
    # ハルナ：うん！  [voice 1836]
    voice "ch9_ha_011"
    ha "Yeah! {#ch9_ha_011}"
    # JA[1836]: ハルナ：うん！
    # [SPRITE lay5 hide]
    # [SPRITE lay7 hide]
    # [BG stage hide]
    $ show_sprites()
    # [BG stage image=+88 → sky] [TRANS trans("crossfade", 1000)]
    $ fade_fx("sky")
    # サイト：（春奈……正確にはアキナに支配された / 状態の春奈は、あの後ウェザリーに / 魔法を解いてもらった）  [null]
    s "(Haruna… to be precise, Haruna / under Akina's control, had her magic / dispelled by Weatherly afterwards.){#ch9_s_049}"
    # JA[null]: サイト：（春奈……正確にはアキナに支配された / 状態の春奈は、あの後ウェザリーに / 魔法を解いてもらった）
    # サイト：（それから、アキナが再び現れることも /　なくなり……）  [null]
    s "(And Akina never appeared again…) {#ch9_s_050}"
    # JA[null]: サイト：（それから、アキナが再び現れることも /　なくなり……）
    # サイト：（春奈は何もしらないまま事件は終わること /　になった）  [null]
    s "(The incident ended without Haruna / knowing anything at all.){#ch9_s_051}"
    # JA[null]: サイト：（春奈は何もしらないまま事件は終わること /　になった）
    # [BGM bgm stop=1000] → fadeout
    stop music fadeout 1.0
    # [SPRITE lay5 hide]
    # [BG stage hide]
    $ show_sprites()
    # [BG stage image=+35 → id(35)] [TRANS trans("crossfade", 1000)]
    $ fade_fx("id(35)")
    # [BGM bgm play=+22 → t21]
    play music t21 fadein 1.0
    # [SPRITE lay8 image=+797 → h 2]
    $ show_sprites(("h 2"))
    # アンриетта：そうですか、彼女も自分が / 生きていくための道を、見つけたのですね。  [voice 449]
    voice "ch9_h_023"
    h "So she found her own path in life. {#ch9_h_023}"
    # JA[449]: アンリエッタ：そうですか、彼女も自分が / 生きていくための道を、見つけたのですね。
    # [SPRITE lay8 x=-96, y=0]
    # [SPRITE lay5 image=+390 → s 1]
    $ show_sprites(("h 2", "s 1"))
    # サイト：はい。 / おかげさまで。  [voice 9313]
    voice "ch9_s_044"
    s "Yes. Thanks to her. {#ch9_s_052}"
    # JA[9313]: サイト：はい。 / おかげさまで。
    # [SPRITE lay8 image=+803 → h 2 sad]
    $ show_sprites(("h 2 sad", "s 1"))
    # アンриетта：せめて最後に会いたかったのに、 / 残念ですわ。  [voice 450]
    voice "ch9_h_024"
    h "I wished I could meet her one last time. {#ch9_h_024}"
    # JA[450]: アンリエッタ：せめて最後に会いたかったのに、 / 残念ですわ。
    # [SPRITE lay8 image=+797 → h 2]
    $ show_sprites(("h 2", "s 1"))
    # アンриетта：彼女にもお礼と謝罪を述べたかったのですが、 / 旅立ってしまったのでは仕方ありませんね。  [voice 451]
    voice "ch9_h_025"
    h "I wanted to thank and apologize to her, / but she's already left. {#ch9_h_025}"
    # JA[451]: アンリエッタ：彼女にもお礼と謝罪を述べたかったのですが、 / 旅立ってしまったのでは仕方ありませんね。
    # [SPRITE lay8 image=+803 → h 2 sad]
    $ show_sprites(("h 2 sad", "s 1"))
    # アンриетта：それに、今回の件では、 / 皆の功に報いることができないのが、 / なにより心苦しいですわ。  [voice 452]
    voice "ch9_h_026"
    h "And yet, I can't celebrate everyone's efforts, / which is the hardest part. {#ch9_h_026}"
    # JA[452]: アンриетта：それに、今回の件では、 / 皆の功に報いることができないのが、 / なにより心苦しいですわ。
    # [SPRITE lay5 hide]
    # [SPRITE lay1 image=+304 → l 1 happy]
    $ show_sprites(("h 2 sad", "l 1 happy"))
    # ルイズ：それこそ仕方ありませんわ。 / 表だってしまっては問題があることを / 全員承知してますから。  [voice 4885]
    voice "ch9_l_003"
    l "Of course it can't be helped. / Everyone knows it's a problem / if it becomes public. {#ch9_l_001}"
    # JA[4885]: ルイズ：それこそ仕方ありませんわ。 / 表だってしまっては問題があることを / 全員承知してますから。
    # [SPRITE lay1 image=+302 → l 1]
    $ show_sprites(("h 2 sad", "l 1"))
    # ルイズ：それでなくても、ウェザリーや、ハルナの件。 / それに虚無の件と極秘事項が目白押しです。  [voice 4886]
    voice "ch9_l_004"
    l "And then there's Weatherly, Haruna, / the Void matter and classified business — / it's all piled up. {#ch9_l_002}"
    # JA[4886]: ルイズ：それでなくても、ウェザリーや、ハルナの件。 / それに虚無の件と極秘事項が目白押しです。
    # ルイズ：貴族は民を守るために存在するもの。 / それはみんなが理解していることです。  [voice 4887]
    voice "ch9_l_005"
    l "Nobles exist to protect the common folk. / Everyone understands that. {#ch9_l_003}"
    # JA[4887]: ルイズ：貴族は民を守るために存在するもの。 / それはみんなが理解していることです。
    # [SPRITE lay1 hide]
    $ show_sprites(("h 2 sad", "s 1"))
    # [SPRITE lay5 image=+390 → s 1]
    $ show_sprites(("h 2 sad", "l 1", "s 1"))
    # サイト：俺も構いませんよ。 / 事情は分かってますから。  [voice 9314]
    voice "ch9_s_045"
    s "I don't mind either. / I understand the situation. {#ch9_s_053}"
    # JA[9314]: サイト：俺も構いませんよ。 / 事情は分かってますから。
    # アンриетта：それではわたくしが心苦しいというもの。  [voice 453]
    voice "ch9_h_027"
    h "Then I feel sorry myself. {#ch9_h_027}"
    # JA[453]: アンриетта：それではわたくしが心苦しいというもの。
    # [SPRITE lay8 image=+797 → h 2]
    $ show_sprites(("h 2", "l 1", "s 1"))
    # アンриетта：せめて、使い魔さんには、 / 個人としてのわたくしにできることを / 褒美としたいと思います。  [voice 454]
    voice "ch9_h_028"
    h "At least for you, my familiar, / I'd like to offer / what I can do for you personally. {#ch9_h_028}"
    # JA[454]: アンриетта：せめて、使い魔さんには、 / 個人としてのわたくしにできることを / 褒美としたいと思います。
    # [SPRITE lay8 image=+799 → h 2 happy]
    $ show_sprites(("h 2 happy", "l 1", "s 1"))
    # アンриетта：受け取っていただけますか？  [voice 455]
    voice "ch9_h_029"
    h "Will you accept it? {#ch9_h_029}"
    # JA[455]: アンриетта：受け取っていただけますか？
    # [SPRITE lay5 image=+429 → s 3 sad]
    $ show_sprites(("h 2 happy", "l 1", "s 3 sad"))
    # サイト：え？ / いや、そんなに気使わないで……。  [voice 9315]
    voice "ch9_s_046"
    s "Huh? / No, don't go to so much trouble… {#ch9_s_054}"
    # JA[9315]: サイト：え？ / いや、そんなに気使わないで……。
    # [BGM bgm stop=1000] → fadeout
    stop music fadeout 1.0
    # [SPRITE lay8 hide]
    # [SPRITE lay5 hide]
    # [BG stage hide]
    $ show_sprites()
    # [EVENT_CG event image=+268 → id(268)] — колодец, CG
    $ dissolve_fx("id(268)", type="cg")
    # [TRANS trans("crossfade", 1000)] — fade_fx
    # [BGM bgm play=+17 → t16]
    play music t16 fadein 1.0
    # サイト：え？  [voice 9316]
    voice "ch9_s_047"
    s "Huh? {#ch9_s_055}"
    # JA[9316]: サイト：え？
    # サイト：（このやわらかいものは一体……）  [null]
    s "(What in the world is this soft thing…) {#ch9_s_056}"
    # JA[null]: サイト：（このやわらかいものは一体……）
    # [SPRITE lay5 hide]
    $ show_sprites()
    # サイト：（ええい、こうなったら……）  [null]
    s "(Screw it, if it's come to this…) {#ch9_s_057}"
    # JA[null]: サイト：（ええい、こうなったら……）
    # [EVENT_CG event image=+293 → id(293)]
    $ dissolve_fx("id(293)", type="cg")
    # ルイズ：え……ええーっ！？ / ひ、姫さま、ききききききキスなんてそんなっ！  [voice 4888]
    voice "ch9_l_006"
    l "Eh… ee-?! P-Princess! A k-k-k-k-k-kiss! Such a thing, no! {#ch9_l_004}"
    # JA[4888]: ルイズ：え……ええーっ！？ / ひ、姫さま、ききききききキスなんてそんなっ！
    # ルイズ：しかも……。 / 唇に……。  [voice 4889]
    voice "ch9_l_007"
    l "And… / on the lips… {#ch9_l_005}"
    # JA[4889]: ルイズ：しかも……。 / 唇に……。
    # [SPRITE lay5 hide]
    # [SPRITE lay1 hide]
    # [BG stage hide]
    # [EVENT_CG event hide]
    $ show_sprites()
    # [BG stage image=+35 → id(35)] [TRANS trans("crossfade", 1000)]
    $ fade_fx("id(35)")
    # [SPRITE lay8 image=+805 → h 2]
    $ show_sprites(("h 2"))
    # アンриетта：これでは足りませんか？  [voice 456]
    voice "ch9_h_030"
    h "Is this not enough? {#ch9_h_030}"
    # JA[456]: アンриетта：これでは足りませんか？
    # [SPRITE lay8 x=-96, y=0]
    # [SPRITE lay5 image=+427 → s 3 angry]
    $ show_sprites(("h 2", "s 3 angry"))
    # サイト：たっ、たっ、足りるもなにも、ええー！  [voice 9317]
    voice "ch9_s_048"
    s "E-enough?! I-It's enough already—! {#ch9_s_058}"
    # JA[9317]: サイト：たっ、たっ、足りるもなにも、ええー！
    # [BGM bgm stop=1000] → fadeout
    stop music fadeout 1.0
    # [BGM bgm play=+30 → t29]
    play music t29 fadein 1.0
    # [SPRITE lay8 hide]
    $ show_sprites(("s 3 angry"))
    # [SPRITE lay1 image=+306 → l 1 angry]
    $ show_sprites(("s 3 angry", "l 1 angry"))
    # ルイズ：サイトっ！！ / このバカ犬。 / 一体、姫さまに何をしたのよ！  [voice 4890]
    voice "ch9_l_008"
    l "Saito!! / You stupid dog. / What on earth did you do to the Princess?! {#ch9_l_006}"
    # JA[4890]: ルイズ：サイトっ！！ / このバカ犬。 / 一体、姫さまに何をしたのよ！
    # [SPRITE lay5 image=+394 → s 1 angry]
    $ show_sprites(("s 3 angry", "l 1 angry", "s 1 angry"))
    # サイト：なにもしてねーって！？ / いやその前に、その手に持った杖はなに！？  [voice 9318]
    voice "ch9_s_049"
    s "I didn't do anything!? / But before that, what's that wand in your hand?! {#ch9_s_059}"
    # JA[9318]: サイト：なにもしてねーって！？ / いやその前に、その手に持った杖はなに！？
    # [SPRITE lay1 image=+372 → l 2 angry]
    $ show_sprites(("s 3 angry", "l 2 angry", "s 1 angry"))
    # ルイズ：ふふふ……。 / これは正義の罰を与える正義の杖！ / その罪深い魂を、これで浄化してあげるわ！  [voice 4891]
    voice "ch9_l_009"
    l "Fufu… / This is a righteous rod / that administers righteous punishment! / I'll purify your sinful soul with it! {#ch9_l_007}"
    # JA[4891]: ルイズ：ふふふ……。 / これは正義の罰を与える正義の杖！ / その罪深い魂を、これで浄化してあげるわ！
    # [SPRITE lay5 image=+427 → s 3 angry]
    $ show_sprites(("s 3 angry", "l 2 angry", "s 1 angry", "s 3 angry"))
    # サイト：うわ待てちょっとルイズやめれ！  [voice 9319]
    voice "ch9_s_050"
    s "Wait a minute, Louise, stop! {#ch9_s_060}"
    # JA[9319]: サイト：うわ待てちょっとルイズやめれ！
    # [SPRITE lay5 hide]
    # [SPRITE lay1 hide]
    $ show_sprites()
    # [SPRITE lay1 image=+373, level=140, dir=3A → l 3 angry]
    $ show_sprites(("l 3 angry"))
    # ルイズ：問答無用！  [voice 4892]
    voice "ch9_l_010"
    l "No questions asked! {#ch9_l_008}"
    # JA[4892]: ルイズ：問答無用！
    # [SPRITE lay1 hide]
    $ show_sprites()
    # [SE se0 play=+95] — не переносится
    # [BG stage vibrate=14] — flash_fx("white")
    # [EVENT_CG event vibrate=14] — flash_fx("white")
    # [SPRITE lay8 vibrate=14] — flash_fx("white")
    # [SPRITE lay5 vibrate=14] — flash_fx("white")
    # [SPRITE lay19 vibrate=14] — flash_fx("white")
    # [SPRITE lay1 vibrate=14] — flash_fx("white")
    # [SPRITE lay7 vibrate=14] — flash_fx("white")
    # [VIBRATE vibrate(3)] — flash_fx("white")
    $ flash_fx("white")
    # WAIT waitTime(1100, true) — pause
    pause(1.1)
    # [BG stage show=1,reset=1] — reset layers
    $ show_sprites()
    # [EVENT_CG event show=0,reset=1] — reset event
    $ dissolve_fx("id(268)", type="cg")
    # [SPRITE lay8 hide, reset=1] — reset layer
    $ show_sprites()
    # [SPRITE lay5 hide, reset=1] — reset layer
    $ show_sprites()
    # [SPRITE lay19 hide, reset=1] — reset layer
    $ show_sprites()
    # [SPRITE lay1 hide, reset=1] — reset layer
    $ show_sprites()
    # [SPRITE lay7 hide, reset=1] — reset layer
    $ show_sprites()
    # WAIT waitTime(0, true)
    # サイト：おあーっ！  [voice 9320]
    voice "ch9_s_051"
    s "Ooh! {#ch9_s_061}"
    # JA[9320]: サイト：おあーっ！
    # [MSGOFF msgoff()] — msgoff()
    # [LAYER white image=+2, level=0] — flash_fx("white")
    $ flash_fx("white")
    # WAIT waitAction(null, true) — pause
    pause(1.0)
    # BACK back()
    # WAIT waitTime(1000, true) — pause
    pause(1.0)
    # [SPRITE lay8 image=+766 → h 2 happy]
    $ show_sprites(("h 2 happy"))
    # [SPRITE lay5 y=0, show=0, x=224]
    # [TRANS trans("crossfade", 0)] — fade_fx(0)
    # [LAYER white hide] — flash_fx("white", hide)
    $ flash_fx("white")
    # WAIT waitAction(null, true) — pause
    pause(0.5)
    # アンриетта：あらまあ、ルイズったら。  [voice 457]
    voice "ch9_h_031"
    h "Oh my, Louise. {#ch9_h_031}"
    # JA[457]: アンриетта：あらまあ、ルイズったら。
    # [SPRITE lay8 x=224, y=0]
    # [SPRITE lay19 image=+944 → d 1 angry]
    $ show_sprites(("h 2 happy", "d 1 angry"))
    # デルフリンガー：おい、姫さん。 / うちの相棒をからかうのも、 / 大概にしてほしいんだがね。  [voice 1221]
    voice "ch9_d_001"
    d "Hey, Princess. / I'd appreciate it if you / didn't tease my familiar. {#ch9_d_001}"
    # JA[1221]: デルフリンガー：おい、姫さん。 / うちの相棒をからかうのも、 / 大概にしてほしいんだがね。
    # [SPRITE lay8 image=+764 → h 2]
    $ show_sprites(("h 2", "d 1 angry"))
    # アンриетта：あら。 / からかってなどいませんよ？  [voice 458]
    voice "ch9_h_032"
    h "Oh. / I wasn't teasing. {#ch9_h_032}"
    # JA[458]: アンриетта：あら。 / からкаってなどいませんよ？
    # [SPRITE lay19 image=+946 → d 1 sad]
    $ show_sprites(("h 2", "d 1 sad"))
    # デルфリнгер：やれやれ。 / 相棒も難儀だねえ。  [voice 1222]
    voice "ch9_d_002"
    d "Goodness. / My familiar's in trouble too. {#ch9_d_002}"
    # JA[1222]: デルフリンガー：やれやれ。 / 相棒も難儀だねえ。
    # [SPRITE lay8 hide]
    # [SPRITE lay19 hide]
    $ show_sprites()
    # [SPRITE lay1 image=+306 → l 1 angry]
    $ show_sprites(("l 1 angry"))
    # [SPRITE lay5 image=+396 → s 1 sad]
    $ show_sprites(("l 1 angry", "s 1 sad"))
    # ルイズ：このバカっ！ / このバカっ！ / この大バカっ！！  [voice 4893]
    voice "ch9_l_011"
    l "This idiot! / This idiot! / This big idiot!! {#ch9_l_009}"
    # JA[4893]: ルイズ：このバカっ！ / このバカっ！ / この大バカっ！！
    # [SE se0 play=+62] — не переносится
    # [SE se0 play=+61] — не переносится
    # [BG stage vibrate=14] — flash_fx("white")
    # [EVENT_CG event vibrate=14] — flash_fx("white")
    # [SPRITE lay8 vibrate=14] — flash_fx("white")
    # [SPRITE lay5 vibrate=14] — flash_fx("white")
    # [SPRITE lay19 vibrate=14] — flash_fx("white")
    # [SPRITE lay1 vibrate=14] — flash_fx("white")
    # [SPRITE lay7 vibrate=14] — flash_fx("white")
    # [VIBRATE vibrate(2)] — flash_fx("white")
    $ flash_fx("white")
    # WAIT waitTime(800, true) — pause
    pause(0.8)
    # [BG stage show=1,reset=1] — reset layers
    $ show_sprites()
    # [EVENT_CG event show=0,reset=1] — reset event
    $ dissolve_fx("id(294)", type="cg")
    # [SPRITE lay8 hide, reset=1] — reset layer
    $ show_sprites()
    # [SPRITE lay5 show=1,reset=1] — reset layer
    $ show_sprites()
    # [SPRITE lay19 hide, reset=1] — reset layer
    $ show_sprites()
    # [SPRITE lay1 show=1,reset=1] — reset layer
    $ show_sprites()
    # [SPRITE lay7 hide, reset=1] — reset layer
    $ show_sprites()
    # WAIT waitTime(0, true)
    # [SPRITE lay5 image=+394 → s 1 angry]
    $ show_sprites(("s 1 angry", "l 1 angry"))
    # サイト：のおおぉーっ！！！  [voice 9321]
    voice "ch9_s_052"
    s "Oooh! {#ch9_s_062}"
    # JA[9321]: サイト：のおおぉーっ！！！
    # [SE se1 stop=1] — не переносится
    # [BGM bgm stop=1000] → fadeout
    stop music fadeout 1.0
    # [SPRITE lay5 hide]
    # [SPRITE lay1 hide]
    # [BG stage hide]
    $ show_sprites()
    # [EVENT_CG event image=+296 → id(296)]
    $ dissolve_fx("id(296)", type="cg")
    # → next scene 430 — глава окончена (конец chapter 9 = chapter_10)
    # → jump attention (конец игры/главы)
    jump attention
    return