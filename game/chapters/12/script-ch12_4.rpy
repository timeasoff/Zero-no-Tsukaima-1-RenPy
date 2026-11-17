# Глава 12, часть 4 (сцены 544–548): финал, Луиза и её фамильяр.
# Источник: ps2_source/chapters/chapter_13_もう一人のハルナ.txt (SCENE 544-548).

label ch12_4:
    $ tndl(None)
    $ show_sprites()

label ch12_4_scene_544:

    # [MOVIE movie(1)]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # サイト：（ひとたび士気と統制を失った敵の部隊は
    s "(Once the enemy loses morale and discipline, their units crumble surprisingly easily…){#ch12_s_135}"

    # サイト：（脱出した部隊ともども次々と鎮圧され、
    s "(The units that tried to escape were suppressed one after another and surrendered.){#ch12_s_136}"

    # サイト：（こうして、トリスタニアを舞台にした
    s "(Thus the conspiracy played out in Tristain lowered its curtain at last, leaving deep scars…){#ch12_s_137}"

    # サイト：（俺達はかりそめながらも
    s "(And we regained a temporary peace…){#ch12_s_138}"

    # サイト：（春奈の催眠魔法を直すには長い時間がかかる
    s "(The hypnosis on Haruna would take long to undo, so for now the two personalities go on living side by side…){#ch12_s_139}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # null：………。 (no voice — пропущено по образцу ch11_2)
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：私が王宮に、ですか？  [voice 1822]
    voice "ch12_ha_031"
    ha "Me? At the palace?{#ch12_ha_031}"

    # [SPRITE   lay7     x=-96, y=0]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：ええ、そうです。  [voice 433]
    voice "ch12_h_016"
    h "Yes, that's right.{#ch12_h_016}"

    # アンリエッタ：正確には、わたくし達は、
    voice "ch12_h_017"
    h "More precisely, we need the Akina inside you.{#ch12_h_017}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # アキナ：このあたしをどうしようっていうんだい？  [voice 43]
    voice "ch12_ak_077"
    ak "What do you want with me?{#ch12_ak_077}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：うわっ、アキナ！
    voice "ch12_s_140"
    s "Whoa, Akina! Don't just pop out like that.{#ch12_s_140}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：この国の現状をご存知ですわね。  [voice 435]
    voice "ch12_h_018"
    h "You know the situation in this country, don't you?{#ch12_h_018}"

    # アンリエッタ：そこで、あなたの力を貸して
    voice "ch12_h_019"
    h "So I'd like to ask for your help. Even if that power wasn't something you sought.{#ch12_h_019}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：で、でも、姫さま。  [voice 4877]
    voice "ch12_l_079"
    l "B-But, Your Highness…{#ch12_l_079}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：このアキナは……その……、
    voice "ch12_l_080"
    l "This Akina is… well, she was Weatherly's tool. Is that really all right with you?{#ch12_l_080}"

    # アンリエッタ：ミス・ウェザリーですか。
    voice "ch12_h_020"
    h "Miss Weatherly, you say. She was never found after that, I hear. Whether she's alive or dead is unknown.{#ch12_h_020}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：ウェザリー様……。  [voice 44]
    voice "ch12_ak_078"
    ak "Weatherly-sama…{#ch12_ak_078}"

    # アキナ：もともと貴族であったウェザリー様は
    voice "ch12_ak_079"
    ak "She told me that she, a noblewoman, had suddenly been stripped of her rank by the Kingdom of Tristain.{#ch12_ak_079}"

    # アキナ：なみなみならぬ魔法の力をレコン・キスタに
    voice "ch12_ak_080"
    ak "Weatherly-sama, whose extraordinary magical talent was recognized by Reconquista…{#ch12_ak_080}"

    # アキナ：今回の作戦の成功と引き換えに、
    voice "ch12_ak_081"
    ak "…promised that in return for this operation's success, her noble rank would be restored.{#ch12_ak_081}"

    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # アンリエッタ：ミス・ウェザリーは分かっていなかったのです。
    voice "ch12_h_021"
    h "Miss Weatherly didn't understand. That spell of hers, the one that beguiles the hearts of others, is forbidden in this country…{#ch12_h_021}"

    # [SPRITE   lay8     image=+768, level=160, dir=1A]
    # アンリエッタ：その禁忌にふれたのが貴族剥奪の
    voice "ch12_h_022"
    h "…and that very taboo was why her rank was taken from her.{#ch12_h_022}"

    # アキナ：……。
    ak "…{#ch12_ak_082}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：分かりました、女王陛下。
    voice "ch12_ak_083"
    ak "Understood, Your Majesty. If I'll do, I'll take the job.{#ch12_ak_083}"

    # アキナ：もしかしたら、ウェザリー様の名誉を
    voice "ch12_ak_084"
    ak "I thought that maybe I could restore at least a little of Weatherly-sama's honor.{#ch12_ak_084}"

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：……そうですか。  [voice 440]
    voice "ch12_h_023"
    h "…Is that so.{#ch12_h_023}"

    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # アンリエッタ：あら、でも城勤めとなると、
    voice "ch12_h_024"
    h "Oh, but if you're to work at the castle, you'll have to fix that way of speaking of yours.{#ch12_h_024}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：あははは……。
    voice "ch12_ak_085"
    ak "Ahahaha… As for manners, I suppose I can leave that to Haruna.{#ch12_ak_085}"

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：なるほど。  [voice 442]
    voice "ch12_h_025"
    h "I see.{#ch12_h_025}"

    # サイト：（……ん、待てよ？
    s "(Hm, wait a second. Haruna was…){#ch12_s_141}"

    # サイト：（礼儀作法は大丈夫だけど
    s "(She's fine with manners, but she can't do housework at all, can she…){#ch12_s_142}"

    menu:
        "Mention it, just in case?{#ch12_4_c_544_1}":
            jump ch12_4_scene_545
        "Ah, never mind…{#ch12_4_c_544_2}":
            jump ch12_4_scene_546
        "I don't know anything…{#ch12_4_c_544_3}":
            jump ch12_4_scene_547

label ch12_4_scene_545:

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay21    hide]
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：でも、春奈ってまったく家事が
    voice "ch12_s_143"
    s "But Haruna couldn't do any housework at all, could she?{#ch12_s_143}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：あ、そういえば。  [voice 4879]
    voice "ch12_l_081"
    l "Ah, now that you mention it.{#ch12_l_081}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：別に気にせずともかまいません。
    voice "ch12_h_026"
    h "There's no need to worry. She can always study at the palace.{#ch12_h_026}"

    # アンリエッタ：わたくしから侍女に、少々の不都合には
    voice "ch12_h_027"
    h "I'll tell the maids to overlook a few small inconveniences…{#ch12_h_027}"

    # サイト：（……大丈夫かな？
    s "(I hope it's all right… I just hope the Princess won't regret this…){#ch12_s_144}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # → next scene 548
    jump ch12_4_scene_548

label ch12_4_scene_546:

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # サイト：（ま、いいか……。
    s "(Ah, let it be… Overthinking it means I lose, right?){#ch12_s_145}"

    # サイト：（そういえば、いくら催眠術だからって、
    s "(Still, even with hypnosis, how did Haruna suddenly become a first-class terrorist?){#ch12_s_146}"

    # サイト：（もしかしてああ見えて、
    s "(Maybe, for all I know, she was into guns and weapons or something?){#ch12_s_147}"

    # [SPRITE   lay21    image=+1021, level=160, dir=1A]
    # アキナ：サイト、その顔は失礼なことを考えてる顔だね。  [voice 51]
    voice "ch12_ak_086"
    ak "Saito, that face means you're thinking something rude.{#ch12_ak_086}"

    # サイト：（……うっ、なんで分かったんだろう。
    s "(Ugh, how did she know? Akina's too sharp.){#ch12_s_148}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # → next scene 548
    jump ch12_4_scene_548

label ch12_4_scene_547:

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # サイト：（し、知らないぞ……。
    s "(I don't know anything… even though Haruna really can't do housework…){#ch12_s_149}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # → next scene 548
    jump ch12_4_scene_548

label ch12_4_scene_548:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # サイト：そ、そういえば、これからの春奈とアキナの
    voice "ch12_s_150"
    s "B-By the way, what's going to happen to Haruna and Akina from now on?{#ch12_s_150}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay8     image=+803, level=160, dir=2A]
    # アンリエッタ：宮廷治療士が言うには、症例が少ないので
    voice "ch12_h_028"
    h "The court healer says there are few cases like this, so she can't say for certain…{#ch12_h_028}"

    # [SPRITE   lay8     image=+797, level=160, dir=2A]
    # アンリエッタ：時間をかけて少しづつ回復していく
    voice "ch12_h_029"
    h "But she should recover little by little, given time.{#ch12_h_029}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：そうですか。  [voice 9298]
    voice "ch12_s_151"
    s "I see.{#ch12_s_151}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # null：………。 (no voice — пропущено по образцу ch11_2)
    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+17]
    play music t16 fadein 1.0
    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：じゃあな、サイト。  [voice 52]
    voice "ch12_ak_087"
    ak "Well then, see you, Saito.{#ch12_ak_087}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay21    hide]
    # [SPRITE   lay7     image=+990, level=160, dir=2A]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # ハルナ：いろいろ迷惑かけちゃって……ごめんね。  [voice 1823]
    voice "ch12_ha_032"
    ha "I'm sorry for all the trouble I caused…{#ch12_ha_032}"

    # [SPRITE   lay7     x=-96, y=0]
    # [SPRITE   lay5     image=+436, level=160, dir=2B]
    # サイト：き、気にすんなって！  [voice 9299]
    voice "ch12_s_152"
    s "D-Don't worry about it!{#ch12_s_152}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：でも、寂しくなるな。
    voice "ch12_s_153"
    s "But it'll get lonely. Even though it's one person, it feels like losing two.{#ch12_s_153}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：逢おうと思えばいつでも逢えるわよ。
    voice "ch12_l_082"
    l "You can meet her whenever you want. It's not far from the academy to Tristain.{#ch12_l_082}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：そ、そうだよな。  [voice 9301]
    voice "ch12_s_154"
    s "T-That's right, isn't it.{#ch12_s_154}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：では、そろそろ……。  [voice 447]
    voice "ch12_h_030"
    h "Then, it's about time…{#ch12_h_030}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：……あ、そうそう。
    voice "ch12_l_083"
    l "Oh, right. Haruna.{#ch12_l_083}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：……なんですか？  [voice 1824]
    voice "ch12_ha_033"
    ha "…What is it?{#ch12_ha_033}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：このバカ犬は、一生わたしの使い魔だからね！  [voice 4882]
    voice "ch12_l_084"
    l "This stupid dog is my familiar for life, you know!{#ch12_l_084}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：い、いきなり何言ってんだ。  [voice 9302]
    voice "ch12_s_155"
    s "W-What are you saying all of a sudden.{#ch12_s_155}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：これだけは、はっきりさせておかないとね。  [voice 4883]
    voice "ch12_l_085"
    l "This much I have to make clear.{#ch12_l_085}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+953, level=160, dir=1A]
    # ハルナ：でも、恋愛は関係ないですよ！  [voice 1825]
    voice "ch12_ha_034"
    ha "But this has nothing to do with romance!{#ch12_ha_034}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：え？  [voice 4884]
    voice "ch12_l_086"
    l "Eh?{#ch12_l_086}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     image=+797, level=160, dir=2A]
    # アンリエッタ：あら。  [voice 448]
    voice "ch12_h_031"
    h "My, my.{#ch12_h_031}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：はぁ……。
    voice "ch12_s_156"
    s "Sigh… Give me a break already…{#ch12_s_156}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ГЛАВЫ 12 ====
    jump ch13
    return

