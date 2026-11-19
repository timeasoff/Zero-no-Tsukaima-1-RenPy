# Глава 18, часть 2 (сцены 706–713): осада академии.
# Источник: ps2_source/chapters/chapter_19_貴族の意地.txt (SCENE 706-713).

label ch18_2:
    $ tndl(None)
    $ show_sprites()

label ch18_2_scene_706:

    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # サイト：（アキナは結局、学院長室に
    s "(Akina barricaded herself in the headmaster's office.){#ch18_s_128}"

    # サイト：（状況を察した学院長は、
    s "(The headmaster, grasping the situation, proposed negotiating with her.){#ch18_s_129}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：やはり賊は、学院長室に立てこもったか。
    voice "ch18_o_001"
    o "So the thief has barricaded herself in the headmaster's office, eh? We can't storm it carelessly. Let me try talking her down first.{#ch18_o_001}"

    # [SPRITE   lay10    x=-96, y=0]
    # [SPRITE   lay9     image=+933, level=160, dir=1A]
    # コルベール：そんな、危険です！
    voice "ch18_c_010"
    c "That's dangerous! If anything happened to Old Osmond…{#ch18_c_010}"

    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # オスマン：その言葉は嬉しいんじゃがの。
    voice "ch18_o_002"
    o "Your concern warms me, but I am the headmaster. Leave the talking to me.{#ch18_o_002}"

    # コルベール：でも、オールド・オスマンが人質に
    voice "ch18_c_011"
    c "But what if Old Osmond is taken hostage!{#ch18_c_011}"

    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：その場合は、教師全員で攻撃でも、
    voice "ch18_o_003"
    o "In that case, all the teachers can attack, or do whatever—right?{#ch18_o_003}"

    # オスマン：多勢に無勢じゃ。
    voice "ch18_o_004"
    o "Many against few. However many bombs she has, she can't win.{#ch18_o_004}"

    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # コルベール：……。  [voice 1071]
    voice "ch18_c_012"
    c "…{#ch18_c_012}"

    # オスマン：代替意見がない以上、決まりじゃな。  [voice 4441]
    voice "ch18_o_005"
    o "No other options, then it's settled.{#ch18_o_005}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay10    x=64, y=0]
    # オスマン：おほん。
    voice "ch18_o_006"
    o "Ahem. Akina, I'd like to have a word. May I come in?{#ch18_o_006}"

    # アキナ：いいだろう。
    voice "ch18_ak_024"
    ak "Fine. But if you try anything strange—boom!{#ch18_ak_024}"

    # オスマン：こちらはそもそも何もできぬわい。
    voice "ch18_o_007"
    o "We can hardly do anything from here. I'll open the lock myself, if you don't mind?{#ch18_o_007}"

    # [SPRITE   lay10    image=+920, level=160, dir=1A]
    # オスマン：では行ってくる。
    voice "ch18_o_008"
    o "Well, I'm off. The rest is up to you.{#ch18_o_008}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay9     image=+933, level=160, dir=1A]
    # コルベール：オールド・オスマンっ……！  [voice 1072]
    voice "ch18_c_013"
    c "Old Osmond…!{#ch18_c_013}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay21    hide]
    # [BG       stage    hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：（一方俺達は、学院長の計らいで、
    s "(Meanwhile, we were gathered in a classroom by the headmaster's arrangement.){#ch18_s_130}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+23, level=200]
    $ fade_fx("id(23)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：いったい何を話してるのかしら。
    voice "ch18_k_012"
    k "What are they talking about? I wonder.{#ch18_k_012}"

    # [SPRITE   lay6     x=-96, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：まかせて。  [voice 15590]
    voice "ch18_t_009"
    t "Leave it to me.{#ch18_t_009}"

    # タバサ：魔法を使った。
    voice "ch18_t_010"
    t "I used magic. Now we can hear what's inside.{#ch18_t_010}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：あぁタバサ、やっぱりあなたは頼りになるわ！
    voice "ch18_k_013"
    k "Ah, Tabitha, you're so reliable! Let's see…{#ch18_k_013}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # オスマン：今の状況は分かっているはずじゃ、アキナくん。  [voice 4445]
    voice "ch18_o_009"
    o "You know the situation, Akina-kun.{#ch18_o_009}"

    # [SPRITE   lay10    hide]
    # [BG       stage    hide]
    # [BG       stage    image=+29, level=200]
    $ fade_fx("id(29)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：そちらがプロならよく理解できるじゃろ。
    voice "ch18_o_010"
    o "You're a professional, so you understand. We have teachers here, and students with the title of Chevalier.{#ch18_o_010}"

    # オスマン：それらが総がかりできみの敵に回ることを
    voice "ch18_o_011"
    o "Consider all of them turning against you. Even you couldn't get out unharmed… could you?{#ch18_o_011}"

    # アキナ：さあ、それはどうだろうねぇ。  [voice 85]
    voice "ch18_ak_025"
    ak "Well, about that…{#ch18_ak_025}"

    # オスマン：ここは投降して、その能力をトリステインの
    voice "ch18_o_012"
    o "You could surrender and use your abilities for Tristain.{#ch18_o_012}"

    # オスマン：もし投降するというなら、わしからも
    voice "ch18_o_013"
    o "If you surrender, I'll put in a word with Her Majesty. I won't let them mistreat you.{#ch18_o_013}"

    # アキナ：そうだね、それもひとつの道かもしれない。
    voice "ch18_ak_026"
    ak "Yeah, that's one path, maybe. At least Haruna would listen to you obediently.{#ch18_ak_026}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：でも、ね。あたしはもう役目を果たしたんだ。
    voice "ch18_ak_027"
    ak "But see—I've already done my job. You've guessed, haven't you? I didn't come here alone.{#ch18_ak_027}"

    # [SPRITE   lay10    image=+924, level=160, dir=1A]
    # オスマン：……。
    o "…{#ch18_o_014}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay10    hide]
    # [BG       stage    hide]
    # [BG       stage    image=+23, level=200]
    $ fade_fx("id(23)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # ルイズ：な、なにっ！？  [voice 6355]
    voice "ch18_l_094"
    l "W-What!?{#ch18_l_094}"

    # サイト：この音……これは。  [voice 11812]
    voice "ch18_s_131"
    s "That sound… this is…{#ch18_s_131}"

    # [SPRITE   lay19    image=+944, level=147, dir=1A]
    # [SPRITE   lay5     level=156]
    # [SPRITE   lay1     level=155]
    # デルフリンガー：相棒。
    voice "ch18_d_013"
    d "Partner. Everything may have come too late.{#ch18_d_013}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay3     image=+856, level=151, dir=1A]
    # モンモランシー：大変よ、みんな！
    voice "ch18_m_010"
    m "It's terrible, everyone! Look out the window!!{#ch18_m_010}"

    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+136, level=80]
    $ dissolve_fx("id(136)")
    # [SPRITE   lay3     hide]
    # [SPRITE   lay20    x=304, y=416]
    # [LAYER    lay0     hide]
    # [SPRITE   lay21    hide]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay10    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [SPRITE   lay1     hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # タバサ：……。
    t "…{#ch18_t_011}"

    # キュルケ：あの船腹の紋章は……レコン・キスタ？
    voice "ch18_k_014"
    k "That emblem on the hull… Reconquista? Why would Reconquista warships…{#ch18_k_014}"

    # アキナ：どうやら来たみたいだね、本隊が。
    voice "ch18_ak_028"
    ak "Looks like they've arrived. The main force. Now the tables have turned.{#ch18_ak_028}"

    # オスマン：うぬぬ……。  [voice 4450]
    voice "ch18_o_015"
    o "Grr…{#ch18_o_015}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay21    hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay10    hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+29, level=200]
    $ fade_fx("id(29)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay20    image=+1061, level=152, dir=1A]
    # ウェザリー：アキナ、お役目ご苦労様。
    voice "ch18_w_001"
    w "Akina, well done. You've grown quite skilled at diversion, it seems.{#ch18_w_001}"

    # [SPRITE   lay20    hide]
    # [BG       stage    hide]
    # [BG       stage    image=+23, level=200]
    $ fade_fx("id(23)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # [SPRITE   lay5     image=+396, level=156, dir=1A]
    # サイト：この声は……。
    voice "ch18_s_132"
    s "That voice… Weatherly-san?{#ch18_s_132}"

    # ルイズ：まさか……。  [voice 6356]
    voice "ch18_l_095"
    l "No way…{#ch18_l_095}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+682, level=153, dir=1A]
    # キュルケ：……。  [voice 3306]
    voice "ch18_k_015"
    k "…{#ch18_k_015}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 707
    jump ch18_2_scene_707

label ch18_2_scene_707:

    # [BG       stage    image=+29, level=200]
    $ fade_fx("id(29)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：なるほど、おまえさんがこの作戦の指揮官か。
    voice "ch18_o_016"
    o "So you're the commander of this operation. Quite a plan.{#ch18_o_016}"

    # ウェザリー：お褒めに預かり、光栄です。  [voice 16000]
    voice "ch18_w_002"
    w "I'm flattered.{#ch18_w_002}"

    # ウェザリー：さて、窓の外をご覧になればお分かりとは
    voice "ch18_w_003"
    w "Now, as you can see outside, this academy is already under Reconquista's control.{#ch18_w_003}"

    # ウェザリー：兵士はすでに学院各所に配置。
    voice "ch18_w_004"
    w "Soldiers are already stationed throughout. Every cannon is aimed at the academy.{#ch18_w_004}"

    # [SPRITE   lay20    image=+1063, level=160, dir=1A]
    # ウェザリー：はったりだとは思わないでいただきたい。
    voice "ch18_w_005"
    w "Please don't think we're bluffing. We're quite serious.{#ch18_w_005}"

    # オスマン：ここまで大掛かりな制圧作戦を組んだ
    voice "ch18_o_017"
    o "Such a large-scale operation means you have some goal.{#ch18_o_017}"

    # [SPRITE   lay10    image=+924, level=160, dir=1A]
    # オスマン：一体、何が望みかね？  [voice 4453]
    voice "ch18_o_018"
    o "Just what is it you want?{#ch18_o_018}"

    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：話が早くて助かります。  [voice 16004]
    voice "ch18_w_006"
    w "You make it easy to talk. Good.{#ch18_w_006}"

    # ウェザリー：そうですね、まずはこの学院にいる
    voice "ch18_w_007"
    w "First, information about the legendary familiar of this academy and its wielder. Naturally, we'll take the two themselves as test subjects.{#ch18_w_007}"

    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：情報は、そちらのアキナくんから
    voice "ch18_o_019"
    o "Isn't that Akina-kun already getting you information?{#ch18_o_019}"

    # ウェザリー：ごく一般的なものは。
    voice "ch18_w_008"
    w "Only the common ones. Classified information was difficult even for Akina to obtain.{#ch18_w_008}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：も、申し訳ございませんウェザリー様。
    voice "ch18_ak_029"
    ak "I-I'm sorry, Weatherly-sama. I couldn't be of more use…{#ch18_ak_029}"

    # [SPRITE   lay20    image=+1063, level=160, dir=1A]
    # ウェザリー：あなたが気に病むことはないわ。
    voice "ch18_w_009"
    w "Don't blame yourself. You did well in such a short time.{#ch18_w_009}"

    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # ウェザリー：ああ、それと、オールド・オスマン。  [voice 16008]
    voice "ch18_w_010"
    w "Ah, and Old Osmond.{#ch18_w_010}"

    # ウェザリー：この学院に収蔵されている
    voice "ch18_w_011"
    w "We'd like you to hand over the magic items stored in this academy…{#ch18_w_011}"

    # ウェザリー：それについての使用法・情報も提供して
    voice "ch18_w_012"
    w "…and provide information on how to use them. Rumor has it there are many interesting things.{#ch18_w_012}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：ずいぶんと要求するものじゃな。
    voice "ch18_o_020"
    o "Quite the list of demands. Did you think I'd simply say yes?{#ch18_o_020}"

    # [SPRITE   lay20    image=+1063, level=160, dir=1A]
    # ウェザリー：我々が握ってる人質……。
    voice "ch18_w_013"
    w "We hold hostages… The lives of every student—surely that's a small price?{#ch18_w_013}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay20    hide]
    # [BG       stage    hide]
    # [BG       stage    image=+23, level=200]
    $ fade_fx("id(23)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：どうする？
    voice "ch18_s_133"
    s "What do we do? Rush the headmaster's office?{#ch18_s_133}"

    # デルフリンガー：おいおい相棒。
    voice "ch18_d_014"
    d "Hey now, partner. You're as straight ahead as ever.{#ch18_d_014}"

    # デルフリンガー：学院のそこかしこにゃバクダンやら
    voice "ch18_d_015"
    d "There are bombs and soldiers all over the academy, right? How will you slip through?{#ch18_d_015}"

    # サイト：それはそうだけど……。  [voice 11815]
    voice "ch18_s_134"
    s "That's true, but…{#ch18_s_134}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay19    hide]
    # [BG       stage    hide]
    # [BG       stage    image=+29, level=200]
    $ fade_fx("id(29)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # ウェザリー：どうしてもお話ししていただけないよう
    voice "ch18_w_014"
    w "If you refuse to talk… we'll have to take suitable measures.{#ch18_w_014}"

    # ウェザリー：失礼……っ！  [voice 16013]
    voice "ch18_w_015"
    w "Pardon me…!{#ch18_w_015}"

    # [SE       se0      play=+94]
    # [SPRITE   lay10    hide]
    # [SPRITE   lay20    hide]
    # [BG       stage    hide]
    # [BG       stage    image=+23, level=200]
    $ fade_fx("id(23)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：な、なんだっ……？  [voice 11816]
    voice "ch18_s_135"
    s "W-What was that…?{#ch18_s_135}"

    # ルイズ：変な音……。  [voice 6357]
    voice "ch18_l_096"
    l "A strange sound…{#ch18_l_096}"

    # [SPRITE   lay1     hide]
    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：魔法止める。  [voice 15592]
    voice "ch18_t_012"
    t "Stopping the magic.{#ch18_t_012}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：ど、どうしたの、タバサ。  [voice 3307]
    voice "ch18_k_016"
    k "W-What is it, Tabitha?{#ch18_k_016}"

    # タバサ：この魔法……。  [voice 15593]
    voice "ch18_t_013"
    t "This magic…{#ch18_t_013}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+29, level=200]
    $ fade_fx("id(29)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # オスマン：なるほど、面白い魔法じゃな。
    voice "ch18_o_021"
    o "I see. Interesting magic. The forbidden art that controls the heart… But it doesn't seem to work on me.{#ch18_o_021}"

    # [SPRITE   lay10    x=224, y=0]
    # [SPRITE   lay20    image=+1065, level=160, dir=1A]
    # ウェザリー：くっ、老いぼれたとはいえ、
    voice "ch18_w_016"
    w "Tch, even old and worn, that power is the real thing, is it? Then we use the original method.{#ch18_w_016}"

    # ウェザリー：オールド・オスマン。
    voice "ch18_w_017"
    w "Old Osmond. From now on, you'll be under our supervision.{#ch18_w_017}"

    # ウェザリー：このまま沈黙を守り続けるのもまたよし。
    voice "ch18_w_018"
    w "Keeping silent is also fine. But if you persist in your stubbornness…{#ch18_w_018}"

    # ウェザリー：この学院とそこにいる者達はほどなくして、
    voice "ch18_w_019"
    w "This academy and everyone in it will be consumed by the flames of our Reconquista's judgment.{#ch18_w_019}"

    # [SPRITE   lay10    image=+924, level=160, dir=1A]
    # オスマン：……。
    o "…{#ch18_o_022}"

    # ウェザリー：いいでしょう。
    voice "ch18_w_020"
    w "Very well. Akina, go ahead.{#ch18_w_020}"

    # [SPRITE   lay10    hide]
    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：はい。  [voice 90]
    voice "ch18_ak_030"
    ak "Yes.{#ch18_ak_030}"

    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay20    vibrate=14]
    # [LAYER    lay0     vibrate=14]
    # [SPRITE   lay21    vibrate=14]
    # [SPRITE   lay19    vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [SPRITE   lay10    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay20    reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay21    reset]
    # [SPRITE   lay19    hide, reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay10    hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay20    hide]
    # [SPRITE   lay21    hide]
    # [BG       stage    hide]
    # [BG       stage    image=+23, level=200]
    $ fade_fx("id(23)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # ルイズ：ま、また爆発……っ？  [voice 6358]
    voice "ch18_l_097"
    l "A-Another explosion…!?{#ch18_l_097}"

    # サイト：くそっ……。  [voice 11817]
    voice "ch18_s_136"
    s "Damn…{#ch18_s_136}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+29, level=200]
    $ fade_fx("id(29)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay20    image=+1061, level=160, dir=1A]
    # [SPRITE   lay10    image=+918, level=160, dir=1A]
    # ウェザリー：残された時間はそう多くはないということを、
    voice "ch18_w_021"
    w "I do hope that old head considers how little time you have left.{#ch18_w_021}"

    # オスマン：そうじゃな。
    voice "ch18_o_023"
    o "Indeed. Let me think right up to the very last moment.{#ch18_o_023}"

    # ウェザリー：時間稼ぎも結構ですが、
    voice "ch18_w_022"
    w "Buying time is fine, but hoping for reinforcements is pointless.{#ch18_w_022}"

    # ウェザリー：聞いてはいるでしょうけど、
    voice "ch18_w_023"
    w "You've heard, I'm sure—Tristain is a battlefield too. No one can come to your aid.{#ch18_w_023}"

    # [SPRITE   lay10    image=+922, level=160, dir=1A]
    # オスマン：……。
    o "…{#ch18_o_024}"

    # ウェザリー：では、十分お考えください。  [voice 16022]
    voice "ch18_w_024"
    w "Then take all the time you need.{#ch18_w_024}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay20    hide]
    # [SPRITE   lay10    hide]
    # [BG       stage    hide]
    # → next scene 708
    jump ch18_2_scene_708

label ch18_2_scene_708:

    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：ハルナばかりか、ウェザリーまで
    voice "ch18_k_017"
    k "Haruna, and now Weatherly too—both servants of Reconquista…{#ch18_k_017}"

    # キュルケ：まぁ、怪しいとは思って調べては
    voice "ch18_k_018"
    k "Well, I suspected as much and was investigating—but it seems we were always a step behind.{#ch18_k_018}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：完全敗北。  [voice 15594]
    voice "ch18_t_014"
    t "Total defeat.{#ch18_t_014}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ちょ、ちょっと、ウェザリーが怪しいなんて
    voice "ch18_l_098"
    l "W-Wait, since when was Weatherly suspicious…?{#ch18_l_098}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：女王陛下が来てからよ。
    voice "ch18_k_019"
    k "Since the Queen came. Remember when I sulked and skipped practice?{#ch18_k_019}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：あっ！  [voice 6360]
    voice "ch18_l_099"
    l "Ah!{#ch18_l_099}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：ウェザリーの周辺が怪しかったから
    voice "ch18_k_020"
    k "I was investigating everything around Weatherly. The Queen's visit wasn't idle either.{#ch18_k_020}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：どうして、そんな重要なことを……。  [voice 6361]
    voice "ch18_l_100"
    l "Why didn't you tell me something so important…{#ch18_l_100}"

    # キュルケ：そりゃ、ルイズは思い込んだら一途でしょ？
    voice "ch18_k_021"
    k "Because you get single-minded, don't you? You're no good for strategy. And you even played the lead on stage, didn't you?{#ch18_k_021}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：うぅ……、それはそうかもしれないけど……。
    voice "ch18_l_101"
    l "Ugh… That may be true, but… But…{#ch18_l_101}"

    # サイト：（今、ルイズの部屋でキュルケ達を交えて、
    s "(Right now, we're having a strategy meeting in Louise's room with Kirche and the others.){#ch18_s_137}"

    # サイト：（学院の教師達はというと、
    s "(The academy teachers are hiding everywhere to stop the Reconquista troops.){#ch18_s_138}"

    # サイト：（トライアングルはもちろん、ラインの
    s "(They've mobilized even the triangle and the line mages—a real all-academy defense.){#ch18_s_139}"

    # サイト：（だがそれにしたって、相手側にも魔術師……
    s "(But even so, the enemy has mages too—professionals of combat. It doesn't feel reassuring.){#ch18_s_140}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：それであなたはどうするつもり、ルイズ？
    voice "ch18_k_022"
    k "So what will you do, Louise? It seems their target is you two.{#ch18_k_022}"

    # キュルケ：あなたがどう動くかが、今後のカギを
    voice "ch18_k_023"
    k "How you act now holds the key to everything, one might say.{#ch18_k_023}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：そんなの決まってるじゃないの。
    voice "ch18_l_102"
    l "That's obvious. Use the Zero Fighter to save Tristain. Then the academy will be saved too.{#ch18_l_102}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：ちょっと待てよ。
    voice "ch18_s_141"
    s "Wait a second. Isn't that backwards? Shouldn't we save the academy first?{#ch18_s_141}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：全然間違っていないわ。
    voice "ch18_l_103"
    l "I'm not wrong. If we save the academy but Tristain falls, it's all for nothing.{#ch18_l_103}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：……そうかい。
    voice "ch18_s_142"
    s "…So that's the mistress's decision, is it? I refuse!{#ch18_s_142}"

    # ルイズ：なによ……！  [voice 6365]
    voice "ch18_l_104"
    l "What!?{#ch18_l_104}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # キュルケ：あらまぁ。  [voice 3315]
    voice "ch18_k_024"
    k "My, my.{#ch18_k_024}"

    # タバサ：……。
    t "…{#ch18_t_015}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：そりゃあ貴族様はお偉い人優先だろうが、
    voice "ch18_s_143"
    s "Sure, nobles have their priorities—but I can't abandon this academy. Isn't that right!{#ch18_s_143}"

    # ルイズ：見捨てるなんて言ってないわ。  [voice 6366]
    voice "ch18_l_105"
    l "I never said abandon it.{#ch18_l_105}"

    # サイト：俺は確かにお前の使い魔だけどさ、
    voice "ch18_s_144"
    s "Sure, I'm your familiar—but I don't want to listen to someone as cold as you right now.{#ch18_s_144}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：あ、あ……あんたねぇっ！
    voice "ch18_l_106"
    l "Y-You! When I'm quiet, you say whatever you like…!{#ch18_l_106}"

    # ルイズ：わたしだって、気がとがめないわけが
    voice "ch18_l_107"
    l "I'm not exactly easy about it either!{#ch18_l_107}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # キュルケ：あーあー、相変わらず仲の良いこと。  [voice 3316]
    voice "ch18_k_025"
    k "Oh dear, you two are still on such good terms.{#ch18_k_025}"

    # タバサ：時間の無駄。  [voice 15595]
    voice "ch18_t_016"
    t "Waste of time.{#ch18_t_016}"

    # [SE       se0      play=+82]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：待ってルイズ。
    voice "ch18_k_026"
    k "Wait, Louise. Someone's coming.{#ch18_k_026}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：敵？  [voice 15596]
    voice "ch18_t_017"
    t "Enemy?{#ch18_t_017}"

    # シエスタ：サイト……さん？
    voice "ch18_si_001"
    si "Saito…-san? Is Saito-san here?{#ch18_si_001}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：その声はシエスタか？
    voice "ch18_s_145"
    s "That voice—Siesta? But all commoners were told to evacuate to the cafeteria.{#ch18_s_145}"

    # シエスタ：でも、サイトさんのことが心配で、
    voice "ch18_si_002"
    si "But I was worried about you, Saito-san, so I came here.{#ch18_si_002}"

    # サイト：分かった、今開けるから。  [voice 11823]
    voice "ch18_s_146"
    s "All right, I'll open up now.{#ch18_s_146}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay19    image=+944, level=160, dir=1A]
    # デルフリンガー：おい相棒、ちょっと待……  [voice 1317]
    voice "ch18_d_016"
    d "Hey, partner, wait a…{#ch18_d_016}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SE       se0      play=+55]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：シエスタ、無事で……わわっ！？  [voice 11824]
    voice "ch18_s_147"
    s "Siesta, you're safe… Waah!?{#ch18_s_147}"

    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # シエスタ：サイトさん死んでください！  [voice 14791]
    voice "ch18_si_003"
    si "Die, Saito-san!{#ch18_si_003}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：ちょ、ちょっとシエスタ。
    voice "ch18_s_148"
    s "H-Hey, Siesta. Why are you holding a knife…?{#ch18_s_148}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：死んでください、サイトさん……。
    voice "ch18_si_004"
    si "Die, Saito-san… It's your fault…{#ch18_si_004}"

    # [SPRITE   lay2     image=+493, level=160, dir=1A]
    # シエスタ：みんながピンチなのにミス・ヴァリエールと
    voice "ch18_si_005"
    si "Everyone's in danger and you're fooling around with Miss Valliere…{#ch18_si_005}"

    # シエスタ：死んじゃえ……わたしを大事にしてくれない
    voice "ch18_si_006"
    si "Just die… If you won't value me, you can die with me…{#ch18_si_006}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：シ、シエスタっ！
    voice "ch18_s_149"
    s "S-Siesta! What on earth are you…{#ch18_s_149}"

    # [SPRITE   lay2     image=+526, level=160, dir=2A]
    # シエスタ：死んでしんでシンデ死んデ死んデ死ンデ
    voice "ch18_si_007"
    si "Die-die-die-die-die… Ufufufufufufufufu…{#ch18_si_007}"

    # [SPRITE   lay2     level=154]
    # [SPRITE   lay5     level=156]
    # [SPRITE   lay19    image=+944, level=151, dir=1A]
    # デルフリンガー：おい相棒、少しは反撃しろっての！
    voice "ch18_d_017"
    d "Hey partner, put up a fight! We'll be killed at this rate!{#ch18_d_017}"

    menu:
        "But attacking Siesta…{#ch18_2_c_708_1}":
            jump ch18_2_scene_709
        "Derf, can't you do anything!?{#ch18_2_c_708_2}":
            jump ch18_2_scene_710
        "Somebody help!{#ch18_2_c_708_3}":
            jump ch18_2_scene_711

label ch18_2_scene_709:

    # [SPRITE   lay2     image=+526, level=154, dir=2A]
    # [SPRITE   lay5     image=+394, level=156, dir=1A]
    # [SPRITE   lay19    image=+944, level=151, dir=1A]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+396, level=151, dir=1A]
    # [SPRITE   lay2     level=155]
    # [SPRITE   lay5     level=151]
    # [SPRITE   lay19    level=152]
    # サイト：で、でもシエスタを攻撃するなんて……。  [voice 11827]
    voice "ch18_s_150"
    s "B-But attacking Siesta…{#ch18_s_150}"

    # [SPRITE   lay2     level=155]
    # [SPRITE   lay5     level=152]
    # [SPRITE   lay19    image=+944, level=151, dir=1A]
    # デルフリンガー：そんな呑気なこと言ってる場合じゃねーだろ！  [voice 1319]
    voice "ch18_d_018"
    d "You can't be serious! Now's not the time!{#ch18_d_018}"

    # デルフリンガー：何もその娘を殺せって言ってるわけ
    voice "ch18_d_019"
    d "I'm not saying kill her! {#ch18_d_019}"

    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay2     vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [LAYER    lay0     vibrate=7]
    # [SPRITE   lay1     vibrate=7]
    # [SPRITE   lay19    vibrate=7]
    # [SPRITE   lay6     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay2     reset]
    # [SPRITE   lay5     reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay19    reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay5     image=+429, level=151, dir=2A]
    # [SPRITE   lay2     level=155]
    # [SPRITE   lay5     level=151]
    # [SPRITE   lay19    level=152]
    # サイト：そ、そんなこと言ったって……うわわっ！  [voice 11828]
    voice "ch18_s_151"
    s "B-But… Waaah!{#ch18_s_151}"

    # → next scene 712
    jump ch18_2_scene_712

label ch18_2_scene_710:

    # [SPRITE   lay2     image=+526, level=154, dir=2A]
    # [SPRITE   lay5     image=+394, level=156, dir=1A]
    # [SPRITE   lay19    image=+944, level=151, dir=1A]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay2     level=155]
    # [SPRITE   lay5     image=+394, level=151, dir=1A]
    # [SPRITE   lay19    level=152]
    # サイト：デルフ、なんとかならないのか！  [voice 11829]
    voice "ch18_s_152"
    s "Derf, can't you do anything!?{#ch18_s_152}"

    # [SPRITE   lay2     level=155]
    # [SPRITE   lay5     level=152]
    # [SPRITE   lay19    image=+946, level=151, dir=1A]
    # デルフリンガー：なんとかって……。
    voice "ch18_d_020"
    d "Do something!? It's your fault for opening the door defenseless!{#ch18_d_020}"

    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay2     vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [LAYER    lay0     vibrate=7]
    # [SPRITE   lay1     vibrate=7]
    # [SPRITE   lay19    vibrate=7]
    # [SPRITE   lay6     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay2     reset]
    # [SPRITE   lay5     reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay19    reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay2     level=155]
    # [SPRITE   lay5     level=151]
    # [SPRITE   lay19    level=152]
    # サイト：そ、そんなこと言ったって……うわわっ！  [voice 11830]
    voice "ch18_s_153"
    s "B-But… Waaah!{#ch18_s_153}"

    # → next scene 712
    jump ch18_2_scene_712

label ch18_2_scene_711:

    # [SPRITE   lay2     image=+526, level=154, dir=2A]
    # [SPRITE   lay5     image=+394, level=156, dir=1A]
    # [SPRITE   lay19    image=+944, level=151, dir=1A]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay5     image=+396, level=151, dir=1A]
    # [SPRITE   lay2     level=155]
    # [SPRITE   lay5     level=151]
    # [SPRITE   lay19    level=152]
    # サイト：だ、誰か助けて！  [voice 11831]
    voice "ch18_s_154"
    s "Somebody help!{#ch18_s_154}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     level=156]
    # [SPRITE   lay1     image=+339, level=151, dir=2A]
    # [SPRITE   lay19    level=153]
    # ルイズ：なに情けない声出してるのよ！
    voice "ch18_l_108"
    l "Why are you whimpering! Somebody, er…{#ch18_l_108}"

    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay2     vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [LAYER    lay0     vibrate=7]
    # [SPRITE   lay1     vibrate=7]
    # [SPRITE   lay19    vibrate=7]
    # [SPRITE   lay6     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay2     reset]
    # [SPRITE   lay5     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [SPRITE   lay1     reset]
    # [SPRITE   lay19    reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     level=156]
    # [SPRITE   lay5     image=+427, level=151, dir=2A]
    # [SPRITE   lay19    level=153]
    # サイト：うわっ！？
    voice "ch18_s_155"
    s "Wah!? Siesta, stop—!{#ch18_s_155}"

    # → next scene 712
    jump ch18_2_scene_712

label ch18_2_scene_712:

    # [SPRITE   lay19    image=+944, level=152, dir=1A]
    # [SPRITE   lay2     image=+526, level=155, dir=2A]
    # [SPRITE   lay5     image=+429, level=151, dir=2A]
    # [BGM      bgm      play=+27]
    play music t26 fadein 1.0
    # [BG       stage    image=+10, level=200]
    $ fade_fx("id(10)")
    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+625, level=154, dir=2A]
    # タバサ：えい。  [voice 15597]
    voice "ch18_t_018"
    t "Hah.{#ch18_t_018}"

    # [SE       se0      play=+62]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [SPRITE   lay2     image=+528, level=155, dir=2A]
    # シエスタ：あっ？
    voice "ch18_si_008"
    si "Ah? Ugh.{#ch18_si_008}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+396, level=151, dir=1A]
    # サイト：タバサ？
    voice "ch18_s_156"
    s "Tabitha? What did you…?{#ch18_s_156}"

    # [LAYER    lay0     image=+588, level=154, dir=1A]
    # タバサ：問題ない。
    voice "ch18_t_019"
    t "No problem. Just knocked her out.{#ch18_t_019}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+715, level=153, dir=2A]
    # キュルケ：でも、どうしてダーリンを殺そうとした
    voice "ch18_k_027"
    k "Still, why would she try to kill darling? I can't say she has no reason, though…{#ch18_k_027}"

    # [SPRITE   lay5     image=+429, level=151, dir=2A]
    # サイト：いや、待てよ。
    voice "ch18_s_157"
    s "Wait. Something's wrong, isn't it? Siesta trying to kill someone…{#ch18_s_157}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=154, dir=1A]
    # タバサ：催眠魔法。  [voice 15599]
    voice "ch18_t_020"
    t "Hypnosis magic.{#ch18_t_020}"

    # [SPRITE   lay6     image=+682, level=153, dir=1A]
    # キュルケ：え？  [voice 3319]
    voice "ch18_k_028"
    k "Eh?{#ch18_k_028}"

    # タバサ：人の心を操る禁忌の魔法。  [voice 15600]
    voice "ch18_t_021"
    t "The forbidden art that controls the heart.{#ch18_t_021}"

    # キュルケ：そんなの使える人なんているの？
    voice "ch18_k_029"
    k "Could anyone even use that? It's forbidden, isn't it?{#ch18_k_029}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay1     image=+302, level=156, dir=1A]
    # ルイズ：分からないわ。
    voice "ch18_l_109"
    l "I don't know. What Reconquista uses and how they fight…{#ch18_l_109}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+394, level=151, dir=1A]
    # サイト：とりあえず、シエスタをどうする？
    voice "ch18_s_158"
    s "Anyway, what do we do with Siesta? We can't just leave her.{#ch18_s_158}"

    # ルイズ：しょうがないわ。
    voice "ch18_l_110"
    l "Fine. Tie her up and put her in the wardrobe.{#ch18_l_110}"

    # [SPRITE   lay5     image=+429, level=151, dir=2A]
    # サイト：おいおい。  [voice 11836]
    voice "ch18_s_159"
    s "Hey now.{#ch18_s_159}"

    # [SPRITE   lay1     image=+335, level=156, dir=2A]
    # ルイズ：大丈夫よ。
    voice "ch18_l_111"
    l "It's fine. Once everything's over, I'll figure something out.{#ch18_l_111}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+713, level=153, dir=2A]
    # キュルケ：それよりも、外が騒がしくなってきたし、
    voice "ch18_k_030"
    k "More importantly, it's getting noisy outside. We should move soon.{#ch18_k_030}"

    # [SPRITE   lay5     image=+394, level=151, dir=1A]
    # サイト：レコン・キスタの兵士か……。  [voice 11837]
    voice "ch18_s_160"
    s "Reconquista soldiers, huh…{#ch18_s_160}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 713
    jump ch18_2_scene_713

label ch18_2_scene_713:

    # [BG       stage    image=+17, level=200]
    $ fade_fx("id(17)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：はぁ、はぁ……。  [voice 11838]
    voice "ch18_s_161"
    s "Haa, haa…{#ch18_s_161}"

    # キュルケ：なんとか、ここまでは移動できたみたいね。  [voice 3322]
    voice "ch18_k_031"
    k "We made it this far, it seems.{#ch18_k_031}"

    # キュルケ：さすがに訓練された兵士だけあるわね。
    voice "ch18_k_032"
    k "You really can tell they're trained soldiers. No wasted movement.{#ch18_k_032}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：ここまで敵が侵入してるってことは、
    voice "ch18_l_112"
    l "If they've gotten this far, things are serious. Saito, there's no time left.{#ch18_l_112}"

    # [SPRITE   lay5     level=156]
    # [SPRITE   lay19    image=+940, level=152, dir=1A]
    # [SPRITE   lay1     level=155]
    # デルフリンガー：そうだな、相棒。
    voice "ch18_d_021"
    d "Right, partner. I know what you want to say to the noble girl—but…{#ch18_d_021}"

    # デルフリンガー：ここで言い争いしてもいいこたねぇぞ。  [voice 1323]
    voice "ch18_d_022"
    d "This isn't the time to argue.{#ch18_d_022}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay19    hide]
    # [LAYER    lay0     image=+588, level=154, dir=1A]
    # タバサ：今はゼロ戦の力が必要。  [voice 15601]
    voice "ch18_t_022"
    t "We need the Zero Fighter's power now.{#ch18_t_022}"

    # [SPRITE   lay5     image=+401, level=156, dir=1B]
    # サイト：分かった。  [voice 11839]
    voice "ch18_s_162"
    s "Got it.{#ch18_s_162}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+682, level=153, dir=1A]
    # キュルケ：いずれ残りの兵士がやって来るわ。
    voice "ch18_k_033"
    k "The remaining soldiers will come eventually. We'll handle them.{#ch18_k_033}"

    # [SPRITE   lay5     image=+440, level=156, dir=2B]
    # サイト：でも、キュルケ達だけじゃ……。  [voice 11840]
    voice "ch18_s_163"
    s "But Kirche and the others alone…{#ch18_s_163}"

    # [SPRITE   lay6     image=+711, level=153, dir=2A]
    # キュルケ：あたしとタバサのコンビなら、
    voice "ch18_k_034"
    k "Tabitha and I can hold out quite a while. Playing for time is boring, though…{#ch18_k_034}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=154, dir=1A]
    # タバサ：でも、学院が占領されたままじゃ、
    voice "ch18_t_023"
    t "But if the academy stays occupied, we're stuck anyway. You two move.{#ch18_t_023}"

    # [SPRITE   lay6     image=+676, level=153, dir=1A]
    # キュルケ：ほら、行って。
    voice "ch18_k_035"
    k "Now go. And bring reinforcements quickly to help us, my darling.{#ch18_k_035}"

    # ==== КОНЕЦ ЧАСТИ 2 ====
    jump ch18_3
    return

