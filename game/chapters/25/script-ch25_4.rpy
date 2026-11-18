# Глава 25, часть 4 (extra 1513–1532): свидания с Табасой.
# Источник: ps2_source/chapters/chapter_26_手紙の秘密.txt (extra 1513-1532).

label ch25_4:
    $ tndl(None)
    $ show_sprites()

label ch25_4_scene_1513:

    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：うーん、劇場かぁ。  [voice 10041]
    voice "ch25_s_164"
    s "Hmm, the theater, huh.{#ch25_s_164}"

    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # タバサ：何？  [voice 15482]
    voice "ch25_t_078"
    t "What?{#ch25_t_078}"

    # サイト：演劇を始める前と終わった後じゃ、
    voice "ch25_s_165"
    s "I was saying how different the impression is before the play starts and after it ends.{#ch25_s_165}"

    # サイト：こうやって劇場の前に来てみるとさ、
    voice "ch25_s_166"
    s "Standing in front of the theater like this, I get a little… well, nostalgic.{#ch25_s_166}"

    # タバサ：……？  [voice 15483]
    voice "ch25_t_079"
    t "…?{#ch25_t_079}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ええっとだなぁ……。  [voice 10044]
    voice "ch25_s_167"
    s "Umm, you see…{#ch25_s_167}"

    menu:
        "It was a good break{#ch25_4_c_1513_1}":
            jump ch25_4_scene_1514
        "A rare experience{#ch25_4_c_1513_2}":
            jump ch25_4_scene_1515
        "We found Haruna's bag{#ch25_4_c_1513_3}":
            jump ch25_4_scene_1516

label ch25_4_scene_1514:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：いい骨休めになったなぁ、って。  [voice 10045]
    voice "ch25_s_168"
    s "It was a nice break, I was saying.{#ch25_s_168}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そりゃまあ、練習や手伝いで大変だったけど、
    voice "ch25_s_169"
    s "Sure, the practice and helping out were hard, but I felt a real sense of fulfillment afterwards.{#ch25_s_169}"

    # タバサ：うん。  [voice 15484]
    voice "ch25_t_080"
    t "Mm.{#ch25_t_080}"

    # → next scene 1517
    jump ch25_4_scene_1517

label ch25_4_scene_1515:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：珍しい経験ができたなぁ、って。  [voice 10047]
    voice "ch25_s_170"
    s "We had a rare experience, I was saying.{#ch25_s_170}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：貴族や王族が演劇に参加することなんて、
    voice "ch25_s_171"
    s "Nobles and royals hardly ever take part in a play, do they?{#ch25_s_171}"

    # タバサ：うん。  [voice 15485]
    voice "ch25_t_081"
    t "Mm.{#ch25_t_081}"

    # サイト：だったら、きっと一生の思い出に
    voice "ch25_s_172"
    s "Then it's sure to become a memory for life, I think.{#ch25_s_172}"

    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_082}"

    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # → next scene 1517
    jump ch25_4_scene_1517

label ch25_4_scene_1516:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：春奈のバッグも見つかったしなぁ。  [voice 10050]
    voice "ch25_s_173"
    s "We found Haruna's bag, too.{#ch25_s_173}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：しかも、演劇を手伝ったことで、
    voice "ch25_s_174"
    s "What's more, by helping with the play, we not only got the bag back—we even got paid.{#ch25_s_174}"

    # [LAYER    lay0     image=+603, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_083}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ん？
    voice "ch25_s_175"
    s "Hmm? What's wrong? Did something bother you?{#ch25_s_175}"

    # タバサ：ううん……。  [voice 15486]
    voice "ch25_t_084"
    t "No…{#ch25_t_084}"

    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # → next scene 1517
    jump ch25_4_scene_1517

label ch25_4_scene_1517:

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+50, level=200]
    $ fade_fx("id(50)")
    # タバサ：でも、爆弾使いを探す任務があった。  [voice 15487]
    voice "ch25_t_085"
    t "But there was the mission to find the bomber.{#ch25_t_085}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：おっと、それは思い出さない約束だ。  [voice 10053]
    voice "ch25_s_176"
    s "Oops. That's something we promised not to bring up.{#ch25_s_176}"

    # タバサ：約束？  [voice 15488]
    voice "ch25_t_086"
    t "Promised?{#ch25_t_086}"

    # サイト：約束。  [voice 10054]
    voice "ch25_s_177"
    s "Promised.{#ch25_s_177}"

    # タバサ：うん……。  [voice 15489]
    voice "ch25_t_087"
    t "Mm…{#ch25_t_087}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：で、タバサはどうなの？
    voice "ch25_s_178"
    s "So, Tabitha—do you have any memories that'll turn out nice, too?{#ch25_s_178}"

    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：……。  [voice 15490]
    voice "ch25_t_088"
    t "…{#ch25_t_088}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：えっ、ええーっ！？
    voice "ch25_s_179"
    s "Eh? Ehh!? Why are you so red in the face!?{#ch25_s_179}"

    # [LAYER    lay0     image=+605, level=160, dir=1B]
    # タバサ：き、気のせい。  [voice 15491]
    voice "ch25_t_089"
    t "I-It's nothing.{#ch25_t_089}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：そ、そう？
    voice "ch25_s_180"
    s "R-Really? Still, I enjoyed it—having you as the heroine.{#ch25_s_180}"

    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：……。  [voice 15492]
    voice "ch25_t_090"
    t "…{#ch25_t_090}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なんで、赤くなるのー？  [voice 10058]
    voice "ch25_s_181"
    s "Why are you turning red?{#ch25_s_181}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
label ch25_4_scene_1518:

    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [SE       se1      play=+37]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：へぇー、市場はやっぱり活気が違うなぁ。
    voice "ch25_s_182"
    s "Wow—the market's got a whole different energy. It's overflowing with rare things.{#ch25_s_182}"

    # サイト：あっ、小鳥だ。
    voice "ch25_s_183"
    s "Ah, a little bird. How cute!{#ch25_s_183}"

    # タバサ：かわいい？  [voice 15493]
    voice "ch25_t_091"
    t "Cute?{#ch25_t_091}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：あれ？
    voice "ch25_s_184"
    s "Huh? It's not cute?{#ch25_s_184}"

    # タバサ：それ食用。  [voice 15494]
    voice "ch25_t_092"
    t "It's for eating.{#ch25_t_092}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：えっ、そうなんだ？
    voice "ch25_s_185"
    s "Eh, really? Even though it's so cute…{#ch25_s_185}"

    # タバサ：有名な料理の食材。  [voice 15495]
    voice "ch25_t_093"
    t "It's a famous ingredient.{#ch25_t_093}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そうなんだ。  [voice 10063]
    voice "ch25_s_186"
    s "I see.{#ch25_s_186}"

    # [LAYER    lay0     image=+601, level=160, dir=1B]
    # タバサ：うん。
    voice "ch25_t_094"
    t "Mm. Delicious…{#ch25_t_094}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：美味しいのか……。  [voice 10064]
    voice "ch25_s_187"
    s "It's delicious, huh…{#ch25_s_187}"

    menu:
        "I feel sorry for it{#ch25_4_c_1518_1}":
            jump ch25_4_scene_1519
        "A cross-cultural experience{#ch25_4_c_1518_2}":
            jump ch25_4_scene_1520
        "I'd like to try it{#ch25_4_c_1518_3}":
            jump ch25_4_scene_1521

label ch25_4_scene_1519:

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # [LAYER    lay0     image=+601, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [SE       se1      play=+37]
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：でも、かわいそうな気がするなぁ。  [voice 10065]
    voice "ch25_s_188"
    s "But it makes me feel a little sorry for it.{#ch25_s_188}"

    # [LAYER    lay0     image=+605, level=160, dir=1B]
    # タバサ：かも……。  [voice 15497]
    voice "ch25_t_095"
    t "Maybe.{#ch25_t_095}"

    # サイト：だろ？  [voice 10066]
    voice "ch25_s_189"
    s "Right?{#ch25_s_189}"

    # タバサ：もう、あの料理食べられない。
    voice "ch25_t_096"
    t "I can't eat that dish anymore. I'd think of it.{#ch25_t_096}"

    # サイト：（そんなにがっかりするほど美味いの！？）
    s "(It's that delicious!? ){#ch25_s_190}"

    # → next scene 1522
    jump ch25_4_scene_1522

label ch25_4_scene_1520:

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # [LAYER    lay0     image=+601, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [SE       se1      play=+37]
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：まさに、異文化体験。  [voice 10067]
    voice "ch25_s_191"
    s "Truly a cross-cultural experience.{#ch25_s_191}"

    # [LAYER    lay0     image=+605, level=160, dir=1B]
    # タバサ：異文化？  [voice 15499]
    voice "ch25_t_097"
    t "Cross-cultural?{#ch25_t_097}"

    # サイト：うん。
    voice "ch25_s_192"
    s "Yeah. But once you taste it, you might stop thinking it's cute at all.{#ch25_s_192}"

    # → next scene 1522
    jump ch25_4_scene_1522

label ch25_4_scene_1521:

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # [LAYER    lay0     image=+601, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [SE       se1      play=+37]
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：一度、食べてみたいな。
    voice "ch25_s_193"
    s "I'd like to try it once. If you say it's good, Tabitha, it must be.{#ch25_s_193}"

    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_098}"

    # サイト：あ、でも高級食材だったりするとか？
    voice "ch25_s_194"
    s "Ah, but maybe it's a luxury ingredient? Then it wouldn't be so easy to get.{#ch25_s_194}"

    # タバサ：大丈夫。
    voice "ch25_t_099"
    t "It's fine. It's home cooking.{#ch25_t_099}"

    # サイト：そっかー。
    voice "ch25_s_195"
    s "I see. Then maybe someday I can eat it.{#ch25_s_195}"

    # → next scene 1522
    jump ch25_4_scene_1522

label ch25_4_scene_1522:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [LAYER    lay0     image=+605, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [SE       se1      play=+37]
    # [BG       stage    image=+38, level=200]
    $ fade_fx("town")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：で、具体的にはどんな感じの料理なの？  [voice 10072]
    voice "ch25_s_196"
    s "So, what kind of dish is it, exactly?{#ch25_s_196}"

    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # タバサ：長くなるけど？  [voice 15501]
    voice "ch25_t_100"
    t "It'll take a while.{#ch25_t_100}"

    # サイト：できれば簡潔にお願いします。  [voice 10073]
    voice "ch25_s_197"
    s "Please keep it short, if possible.{#ch25_s_197}"

    # タバサ：ひと口大に切ったお肉を串に刺して
    voice "ch25_t_101"
    t "You skewer bite-sized pieces of meat and roast them while brushing on sauce.{#ch25_t_101}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：や、焼き鳥じゃないですか……。  [voice 10074]
    voice "ch25_s_198"
    s "Hey, that's yakitori…{#ch25_s_198}"

    # [LAYER    lay0     image=+605, level=160, dir=1B]
    # タバサ：？？？  [voice 15503]
    voice "ch25_t_102"
    t "???{#ch25_t_102}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
label ch25_4_scene_1523:

    # [BG       stage    image=+47, level=200]
    $ fade_fx("id(47)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：裏街道といっても、そんなに裏って
    voice "ch25_s_199"
    s "They call it a back street, but it doesn't feel very back-alleyish, does it?{#ch25_s_199}"

    # サイト：人通りも店もそれなりにあるし。
    voice "ch25_s_200"
    s "There are plenty of people and shops. Just…{#ch25_s_200}"

    # タバサ：ただ？  [voice 15504]
    voice "ch25_t_103"
    t "Just?{#ch25_t_103}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：ちょっと喉が渇いててさ。
    voice "ch25_s_201"
    s "I'm a bit thirsty. I was thinking I'd like a drink. There are no convenience stores here, though.{#ch25_s_201}"

    # [LAYER    lay0     image=+605, level=160, dir=1B]
    # タバサ：コンビニ？  [voice 15505]
    voice "ch25_t_104"
    t "Convenience store?{#ch25_t_104}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：あ、いや、俺の世界でよくある
    voice "ch25_s_202"
    s "Ah, no—I mean one of those shops back home that's open 24 hours…{#ch25_s_202}"

    # タバサ：？？？  [voice 15506]
    voice "ch25_t_105"
    t "???{#ch25_t_105}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：いやー、喉がかわいたなぁ。  [voice 10079]
    voice "ch25_s_203"
    s "Man, I'm thirsty.{#ch25_s_203}"

    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_106}"

    # サイト：どうしたの？  [voice 10080]
    voice "ch25_s_204"
    s "What's wrong?{#ch25_s_204}"

    # タバサ：お酒。  [voice 15507]
    voice "ch25_t_107"
    t "Alcohol.{#ch25_t_107}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：いや、確かに目の前にバーがあるけどね……。  [voice 10081]
    voice "ch25_s_205"
    s "No, I mean—there is a bar right in front of us, though…{#ch25_s_205}"

    menu:
        "I'm underage{#ch25_4_c_1523_1}":
            jump ch25_4_scene_1524
        "Drinking in the morning?{#ch25_4_c_1523_2}":
            jump ch25_4_scene_1525
        "I'd rather have a normal drink{#ch25_4_c_1523_3}":
            jump ch25_4_scene_1526

label ch25_4_scene_1524:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+47, level=200]
    $ fade_fx("id(47)")
    # サイト：俺、未成年だから……。  [voice 10082]
    voice "ch25_s_206"
    s "I'm underage back home…{#ch25_s_206}"

    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # タバサ：未成年？  [voice 15508]
    voice "ch25_t_108"
    t "Underage?{#ch25_t_108}"

    # サイト：えーっと、俺の国じゃ、
    voice "ch25_s_207"
    s "Well, where I come from, you're not allowed to drink until you're an adult.{#ch25_s_207}"

    # タバサ：飲んじゃいけない？  [voice 15509]
    voice "ch25_t_109"
    t "Not allowed to drink?{#ch25_t_109}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：飲むとえらい怒られる。  [voice 10084]
    voice "ch25_s_208"
    s "If you do, you get scolded something fierce.{#ch25_s_208}"

    # タバサ：不思議。  [voice 15510]
    voice "ch25_t_110"
    t "Strange.{#ch25_t_110}"

    # → next scene 1527
    jump ch25_4_scene_1527

label ch25_4_scene_1525:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+47, level=200]
    $ fade_fx("id(47)")
    # サイト：ひょっとして、昼間からお酒を？  [voice 10085]
    voice "ch25_s_209"
    s "Could it be you're drinking from morning?{#ch25_s_209}"

    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_111}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：あのぉ……。
    voice "ch25_s_210"
    s "Um… I'd prefer a drink without alcohol…{#ch25_s_210}"

    # [LAYER    lay0     image=+605, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_112}"

    # → next scene 1527
    jump ch25_4_scene_1527

label ch25_4_scene_1526:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+47, level=200]
    $ fade_fx("id(47)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：お酒よりも普通のものが飲みたいなぁ。  [voice 10087]
    voice "ch25_s_211"
    s "I'd rather have a normal drink than alcohol.{#ch25_s_211}"

    # [LAYER    lay0     image=+605, level=160, dir=1B]
    # タバサ：普通？  [voice 15511]
    voice "ch25_t_113"
    t "Normal?{#ch25_t_113}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：えーっと、アルコール……じゃなくて、
    voice "ch25_s_212"
    s "Um, not alcohol—if possible, something without alcohol in it.{#ch25_s_212}"

    # タバサ：どうして？  [voice 15512]
    voice "ch25_t_114"
    t "Why?{#ch25_t_114}"

    # サイト：そりゃあ、やっぱり……。
    voice "ch25_s_213"
    s "Because… Well, drinking in the daytime is a bit… No, of course it's no good at night, either.{#ch25_s_213}"

    # タバサ：……？  [voice 15513]
    voice "ch25_t_115"
    t "…?{#ch25_t_115}"

    # サイト：あと、酔っ払ってタバサに迷惑かけたら
    voice "ch25_s_214"
    s "Besides, I'd hate to get drunk and cause you trouble, Tabitha.{#ch25_s_214}"

    # → next scene 1527
    jump ch25_4_scene_1527

label ch25_4_scene_1527:

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+47, level=200]
    $ fade_fx("id(47)")
    # [LAYER    lay0     image=+605, level=160, dir=1B]
    # タバサ：ごめんなさい。  [voice 15514]
    voice "ch25_t_116"
    t "I'm sorry.{#ch25_t_116}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：あっ、いや……。
    voice "ch25_s_215"
    s "Ah, no—you don't need to apologize. If we look hard enough, there'll be a drink somewhere…{#ch25_s_215}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：あっ、ほらほら！
    voice "ch25_s_216"
    s "Ah, look! I'll buy a drink at that shop!{#ch25_s_216}"

    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # タバサ：あっ……。
    voice "ch25_t_117"
    t "Ah… That's seasoning…{#ch25_t_117}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ぶはっ！
    voice "ch25_s_217"
    s "Whoa! Why do they sell it in such huge quantities!{#ch25_s_217}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # タバサ：ごめん。  [voice 15516]
    voice "ch25_t_118"
    t "Sorry.{#ch25_t_118}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：いや、大丈夫だって。
    voice "ch25_s_218"
    s "No, it's fine. Look, let's search somewhere else.{#ch25_s_218}"

    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # タバサ：うん。  [voice 15517]
    voice "ch25_t_119"
    t "Mm.{#ch25_t_119}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
label ch25_4_scene_1528:

    # [BG       stage    image=+85, level=200]
    $ fade_fx("id(85)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：こうやって、２人で周りを眺めながら
    voice "ch25_s_219"
    s "Walking like this, the two of us looking around—it's nice, but…{#ch25_s_219}"

    # タバサ：……。
    t "…{#ch25_t_120}"

    # サイト：（うーむ、タバサの私服姿に、
    s "(Who would have thought Tabitha's casual clothes had this much destructive power…){#ch25_s_220}"

    # タバサ：どうしたの？  [voice 15518]
    voice "ch25_t_121"
    t "What's wrong?{#ch25_t_121}"

    # [SPRITE   lay5     image=+431, level=160, dir=2A]
    # サイト：いや、その……！？
    voice "ch25_s_221"
    s "No, it's just…!? I was thinking these casual clothes suit you really well.{#ch25_s_221}"

    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_122}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：えっと……。
    voice "ch25_s_222"
    s "Um… Outside the academy, do you always dress like this?{#ch25_s_222}"

    # [LAYER    lay0     image=+599, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_123}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：えっ？
    voice "ch25_s_223"
    s "Eh? That's not it?{#ch25_s_223}"

    # [LAYER    lay0     image=+601, level=160, dir=1B]
    # タバサ：これ、キュルケが選んだ。  [voice 15519]
    voice "ch25_t_124"
    t "Kirche picked this out.{#ch25_t_124}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：なるほど……。  [voice 10099]
    voice "ch25_s_224"
    s "I see…{#ch25_s_224}"

    menu:
        "As expected of Kirche{#ch25_4_c_1528_1}":
            jump ch25_4_scene_1529
        "Clothes Tabitha picked{#ch25_4_c_1528_2}":
            jump ch25_4_scene_1530
        "Kirche worries too much{#ch25_4_c_1528_3}":
            jump ch25_4_scene_1531

label ch25_4_scene_1529:

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [LAYER    lay0     image=+601, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+85, level=200]
    $ fade_fx("id(85)")
    # サイト：さすがキュルケだな。
    voice "ch25_s_225"
    s "As expected of Kirche. It really suits you, Tabitha.{#ch25_s_225}"

    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_125}"

    # [SPRITE   lay5     image=+431, level=160, dir=2A]
    # サイト：できれば露出度もキュルケくらいに……。  [voice 10101]
    voice "ch25_s_226"
    s "If only the amount of skin shown were more like Kirche's…{#ch25_s_226}"

    # [LAYER    lay0     image=+603, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_126}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：……すみませんでした。
    voice "ch25_s_227"
    s "…I'm sorry. I got carried away.{#ch25_s_227}"

    # → next scene 1532
    jump ch25_4_scene_1532

label ch25_4_scene_1530:

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [LAYER    lay0     image=+601, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+85, level=200]
    $ fade_fx("id(85)")
    # [SPRITE   lay5     image=+431, level=160, dir=2A]
    # サイト：今度は、タバサが選んだ服も見たいな。  [voice 10103]
    voice "ch25_s_228"
    s "Next time, I want to see clothes Tabitha picked herself.{#ch25_s_228}"

    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：そのうち。  [voice 15520]
    voice "ch25_t_127"
    t "Someday.{#ch25_t_127}"

    # → next scene 1532
    jump ch25_4_scene_1532

label ch25_4_scene_1531:

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [LAYER    lay0     image=+601, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+85, level=200]
    $ fade_fx("id(85)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：キュルケも心配性だな。  [voice 10104]
    voice "ch25_s_229"
    s "Kirche worries too much, doesn't she.{#ch25_s_229}"

    # [LAYER    lay0     image=+605, level=160, dir=1B]
    # タバサ：……？  [voice 15521]
    voice "ch25_t_128"
    t "…?{#ch25_t_128}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：タバサなら、
    voice "ch25_s_230"
    s "Tabitha, I think you'd look good in anything—Kirche doesn't need to look after you.{#ch25_s_230}"

    # [LAYER    lay0     image=+603, level=160, dir=1B]
    # タバサ：そんなことない。  [voice 15522]
    voice "ch25_t_129"
    t "That's not true.{#ch25_t_129}"

    # サイト：そうかなぁ？
    voice "ch25_s_231"
    s "Isn't it? I don't think so, though.{#ch25_s_231}"

    # タバサ：本気？  [voice 15523]
    voice "ch25_t_130"
    t "Seriously?{#ch25_t_130}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：うん、本気。  [voice 10107]
    voice "ch25_s_232"
    s "Yeah. Seriously.{#ch25_s_232}"

    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：……。
    t "…{#ch25_t_131}"

    # → next scene 1532
    jump ch25_4_scene_1532

label ch25_4_scene_1532:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [LAYER    lay0     image=+603, level=160, dir=1B]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+85, level=200]
    $ fade_fx("id(85)")
    # [LAYER    lay0     image=+607, level=160, dir=1B]
    # タバサ：でも……。
    voice "ch25_t_132"
    t "But… I don't look at it much.{#ch25_t_132}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：えっ、なんで？  [voice 10108]
    voice "ch25_s_233"
    s "Eh, why not?{#ch25_s_233}"

    # タバサ：やっぱり恥ずかしい。  [voice 15525]
    voice "ch25_t_133"
    t "It's embarrassing, after all.{#ch25_t_133}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：そ、そりゃそうだよね。
    voice "ch25_s_234"
    s "O-Of course it is. Ha ha, ha ha…{#ch25_s_234}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ГЛАВЫ 25 ====
    jump ch26
    return

