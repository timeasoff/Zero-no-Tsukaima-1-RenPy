# Глава 15, часть 2 (сцены 633–642): военный совет, разрешение на Пустоту.
# Источник: ps2_source/chapters/chapter_16_魔法の薬.txt (SCENE 633-642).

label ch15_2:
    $ tndl(None)
    $ show_sprites()

label ch15_2_scene_633:

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ふう、でも問題はこれからどうするかね。
    voice "ch15_l_024"
    l "Whew. But the problem is what we do now. Why reveal herself now?{#ch15_l_024}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：アキナは『最後の幕が開く』とか
    voice "ch15_s_048"
    s "Akina said 'the final act is about to begin'…{#ch15_s_048}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：『隠す必要がなくなった』から。  [voice 15792]
    voice "ch15_t_001"
    t "'Because there's no need to hide anymore.'{#ch15_t_001}"

    # [LAYER    lay0     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：タバサ！  [voice 7073]
    voice "ch15_l_025"
    l "Tabitha!{#ch15_l_025}"

    # タバサ：頼まれたお薬の材料。  [voice 15793]
    voice "ch15_t_002"
    t "The medicine ingredients you asked for.{#ch15_t_002}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # モンモランシー：あ、ありがとう。
    voice "ch15_m_007"
    m "Ah, thank you, Tabitha. Now we can manage.{#ch15_m_007}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：『隠す必要がなくなった』って……、
    voice "ch15_s_049"
    s "'No need to hide anymore'… What does that mean, Tabitha?{#ch15_s_049}"

    # [LAYER    lay0     image=+592, level=160, dir=1A]
    # タバサ：今、街のあちこちで火の手が上がってる。  [voice 15794]
    voice "ch15_t_003"
    t "Fires are breaking out all over the city now.{#ch15_t_003}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：な、なんですって。
    voice "ch15_l_026"
    l "W-What!? It wasn't just the market!?{#ch15_l_026}"

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：市場の炎上はただの始まり。
    voice "ch15_t_004"
    t "The market fire was just the beginning. There's shelling of the palace too, it seems.{#ch15_t_004}"

    # [LAYER    lay0     level=155]
    # [SPRITE   lay19    image=+944, level=152, dir=1A]
    # [SPRITE   lay1     level=156]
    # デルフリンガー：どうやら、今日が奴らの、
    voice "ch15_d_002"
    d "Looks like today was the day they were to act.{#ch15_d_002}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay19    hide]
    # [SPRITE   lay1     image=+339, level=156, dir=2A]
    # ルイズ：と、とにかく登城しましょう！
    voice "ch15_l_027"
    l "A-Anyway, let's get to the castle! I'm worried about the Princess! Hurry!{#ch15_l_027}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 634
    jump ch15_2_scene_634

label ch15_2_scene_634:

    # [BG       stage    image=+62, level=200]
    $ fade_fx("id(62)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+21]
    play music t20 fadein 1.0
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：通しなさい！
    voice "ch15_l_028"
    l "Let us through! It's urgent!{#ch15_l_028}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay15    image=+1116, level=160, dir=1A]
    # [SPRITE   lay1     level=155]
    # 兵士ＭＳ：止まれ。
    voice "ch15_soldier_001"
    soldier "Halt. This is the palace! Follow the proper procedures.{#ch15_soldier_001}"

    # 兵士ＭＳ：魔法学院の生徒風情が何の用か！  [voice 4258]
    voice "ch15_soldier_002"
    soldier "What business do academy students have here!?{#ch15_soldier_002}"

    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：な、なんですって！  [voice 7077]
    voice "ch15_l_029"
    l "W-What did you say!?{#ch15_l_029}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay5     image=+407, level=156, dir=1B]
    # サイト：ルイズ、落ち着けって！  [voice 13066]
    voice "ch15_s_050"
    s "Louise, calm down!{#ch15_s_050}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay15    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay15    hide, reset]
    # [SPRITE   lay1     hide, reset]
    # [SPRITE   lay15    image=+1116, level=160, dir=1A]
    # 兵士ＭＳ：うわぁっ！  [voice 4259]
    voice "ch15_soldier_003"
    soldier "Wah!{#ch15_soldier_003}"

    # [SPRITE   lay15    x=160, y=0]
    # [SPRITE   lay1     image=+306, level=155, dir=1A]
    # ルイズ：きゃあ！  [voice 7078]
    voice "ch15_l_030"
    l "Eek!{#ch15_l_030}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay5     image=+405, level=156, dir=1B]
    # サイト：ルイズ！
    voice "ch15_s_051"
    s "Louise! Are you all right!{#ch15_s_051}"

    # サイト：（……砲撃だって？）
    s "(Shelling, you said?){#ch15_s_052}"

    # サイト：（……くそ、冗談じゃないぜ。
    s "(Damn, this is ridiculous. Why is shelling reaching the palace!?){#ch15_s_053}"

    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay15    vibrate=14]
    # [SPRITE   lay1     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay15    hide, reset]
    # [SPRITE   lay1     reset]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay1     image=+302, level=155, dir=1A]
    # ルイズ：事の重要さが分かったでしょう？
    voice "ch15_l_031"
    l "Now do you understand how serious this is? I'm Louise Francoise, third daughter of Duke La Valliere.{#ch15_l_031}"

    # ルイズ：女王陛下ご下命の調査につき、
    voice "ch15_l_032"
    l "I have an urgent report concerning the Queen's order. Please announce me.{#ch15_l_032}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay15    image=+1118, level=160, dir=1A]
    # 兵士ＭＳ：し、しかし……。  [voice 4260]
    voice "ch15_soldier_004"
    soldier "B-But…{#ch15_soldier_004}"

    # [SPRITE   lay1     image=+339, level=155, dir=2A]
    # ルイズ：早く取り次ぎなさい！
    voice "ch15_l_033"
    l "Announce me at once! You can see the fires too! We don't have time for this!{#ch15_l_033}"

    # [SPRITE   lay15    image=+1116, level=160, dir=1A]
    # 兵士ＭＳ：し、しばらくお待ちください！  [voice 4261]
    voice "ch15_soldier_005"
    soldier "P-Please wait a moment!{#ch15_soldier_005}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay15    hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 635
    jump ch15_2_scene_635

label ch15_2_scene_635:

    # [EVENT_CG event    image=+135, level=80]
    $ dissolve_fx("id(135)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # アンリエッタ：それで、状況は……。  [voice 684]
    voice "ch15_h_001"
    h "So, the situation is…{#ch15_h_001}"

    # 将校：はっ、中央市場の炎上を皮切りに、
    voice "ch15_commander_001"
    commander "Yes. Starting with the fire at the central market, buildings and bridges across the city have been bombed…{#ch15_commander_001}"

    # 将校：その後も市内各地に隠匿されていた
    voice "ch15_commander_002"
    commander "Since then, continuous shelling of the palace from cannons hidden around the city has been confirmed.{#ch15_commander_002}"

    # [SE       se0      play=+64]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay15    vibrate=14]
    # [SPRITE   lay8     hide, vibrate=14]
    # [SPRITE   lay18    hide, vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    hide, reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay15    hide, reset]
    # [SPRITE   lay8     hide, reset]
    # [SPRITE   lay18    hide, reset]
    # [SPRITE   lay8     hide]
    # アンリエッタ：市内に砲台とはどういうことです？
    voice "ch15_h_002"
    h "Cannons inside the city? How on earth—!{#ch15_h_002}"

    # 将校：制圧に成功した兵士からの報告ですが……。  [voice 4327]
    voice "ch15_commander_003"
    commander "Reports from the soldiers who subdued the attackers say…{#ch15_commander_003}"

    # 将校：先日来の爆破事件を利用して、
    voice "ch15_commander_004"
    commander "Reconquista used the recent bombings to slip soldiers disguised as repair workers into the country.{#ch15_commander_004}"

    # 将校：破壊された現場の修復に紛れ込んでは、
    voice "ch15_commander_005"
    commander "They seem to have slipped into the damaged sites and installed numerous small cannons.{#ch15_commander_005}"

    # アンリエッタ：なんですって！  [voice 686]
    voice "ch15_h_003"
    h "What!?{#ch15_h_003}"

    # 将校：こちらの地図をご覧ください。
    voice "ch15_commander_006"
    commander "Please look at this map. The sites of the bombings and the cannon positions match exactly.{#ch15_commander_006}"

    # [EVENT_CG event    image=+259, level=80]
    $ dissolve_fx("id(259)")
    # アンリエッタ：こ、これは……。  [voice 687]
    voice "ch15_h_004"
    h "T-This is…{#ch15_h_004}"

    # 将校：はい。
    voice "ch15_commander_007"
    commander "Yes. The bombings were carried out at the positions best suited for shelling the palace.{#ch15_commander_007}"

    # アンリエッタ：なんてことでしょう。
    voice "ch15_h_005"
    h "Good heavens. So once again we were one step behind…{#ch15_h_005}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay18    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay15    image=+1116, level=160, dir=1A]
    # 味方Ａ：報告します。  [voice 4262]
    voice "ch15_soldier_006"
    soldier "Reporting.{#ch15_soldier_006}"

    # [SPRITE   lay15    image=+1114, level=160, dir=1A]
    # 味方Ａ：ラ・ヴェリエール家三女、
    voice "ch15_soldier_007"
    soldier "Third daughter of the La Valliere family, Louise Francoise.{#ch15_soldier_007}"

    # 味方Ａ：火急の件につき女王陛下への謁見を
    voice "ch15_soldier_008"
    soldier "She requests an audience with Her Majesty regarding an urgent matter.{#ch15_soldier_008}"

    # [SPRITE   lay15    hide]
    # [SPRITE   lay8     image=+766, level=160, dir=1A]
    # アンリエッタ：ルイズが？
    voice "ch15_h_006"
    h "Louise? Show her in at once.{#ch15_h_006}"

    # [SPRITE   lay8     x=224, y=0]
    # [SPRITE   lay8     level=155]
    # [SPRITE   lay18    image=+1125, level=159, dir=1A]
    # 将校：陛下？
    voice "ch15_commander_008"
    commander "Your Majesty, this Louise you mention…?{#ch15_commander_008}"

    # [SPRITE   lay8     image=+764, level=155, dir=1A]
    # アンリエッタ：爆弾使いについて調べさせていた者達です。
    voice "ch15_h_007"
    h "They're the ones I had investigating the bomb-thrower. They may have an important report.{#ch15_h_007}"

    # [SPRITE   lay18    image=+1121, level=159, dir=1A]
    # 将校：今は軍議の場ですぞ。  [voice 4333]
    voice "ch15_commander_009"
    commander "But this is a war council.{#ch15_commander_009}"

    # アンリエッタ：分かりました。
    voice "ch15_h_008"
    h "Understood. Let's pause the council. You may step down.{#ch15_h_008}"

    # 将校：……はっ。  [voice 4334]
    voice "ch15_commander_010"
    commander "…Yes.{#ch15_commander_010}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay8     hide]
    # [SPRITE   lay18    hide]
    # [BG       stage    hide]
    # → next scene 636
    jump ch15_2_scene_636

label ch15_2_scene_636:

    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [SE       se0      play=+57]
    # [SPRITE   lay1     image=+304, level=160, dir=1A]
    # ルイズ：姫さま！  [voice 7082]
    voice "ch15_l_034"
    l "Princess!{#ch15_l_034}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay8     image=+766, level=160, dir=1A]
    # アンリエッタ：ルイズ。
    voice "ch15_h_009"
    h "Louise. You came. And your familiars too.{#ch15_h_009}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：申し訳ありません、姫さま……。
    voice "ch15_l_035"
    l "I'm sorry, Princess… We couldn't stop the bomb-throwers.{#ch15_l_035}"

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：過去を悔やんでいてもはじまりません。
    voice "ch15_h_010"
    h "There's no use regretting the past. Your report, then.{#ch15_h_010}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：はい。  [voice 7084]
    voice "ch15_l_036"
    l "Yes.{#ch15_l_036}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # アンリエッタ：そうですか、やはりあのウェザリーの
    voice "ch15_h_011"
    h "I see. So that Weatherly troupe after all…{#ch15_h_011}"

    # ルイズ：ご存知だったのですか？
    voice "ch15_l_037"
    l "You knew? Then your joining the performance was…?{#ch15_l_037}"

    # アンリエッタ：内偵を進めていたのは事実です。
    voice "ch15_h_012"
    h "I was indeed conducting a secret investigation. I hated keeping it from Louise.{#ch15_h_012}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：ひ、ひとこと言っていただければ……。  [voice 7086]
    voice "ch15_l_038"
    l "You could have told me even one thing…{#ch15_l_038}"

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：人には向き不向きがありますもの。
    voice "ch15_h_013"
    h "Everyone has their strengths. Louise isn't good at keeping secrets.{#ch15_h_013}"

    # ルイズ：……。  [voice 7087]
    voice "ch15_l_039"
    l "…{#ch15_l_039}"

    # アンリエッタ：ともあれ、ミス・ウェザリーの能力には
    voice "ch15_h_014"
    h "In any case, we must be wary of Miss Weatherly's abilities…{#ch15_h_014}"

    # アンリエッタ：気の毒なキュルケやハルナだけではなく、
    voice "ch15_h_015"
    h "Not only poor Kirche and Haruna—there may be others in the army and nobility under hypnosis.{#ch15_h_015}"

    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # アンリエッタ：不覚でした。
    voice "ch15_h_016"
    h "I was careless. I had no idea things had gone this far. If I'd noticed sooner…{#ch15_h_016}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：どういうことですか？  [voice 7088]
    voice "ch15_l_040"
    l "What do you mean?{#ch15_l_040}"

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：どうやら、爆弾使いの事件は敵の単なる第一手に
    voice "ch15_h_017"
    h "It seems the bomb-thrower incident was merely the enemy's first move.{#ch15_h_017}"

    # アンリエッタ：トリスタニア市街では、爆弾使いの事件を
    voice "ch15_h_018"
    h "In Tristain, enemy soldiers who infiltrated during the incident have begun moving, and street fighting is breaking out.{#ch15_h_018}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：そ、そんな！  [voice 7089]
    voice "ch15_l_041"
    l "T-That can't be!{#ch15_l_041}"

    menu:
        "We'll go destroy the cannons!{#ch15_2_c_636_1}":
            jump ch15_2_scene_637
        "We'll join the street fighting!{#ch15_2_c_636_2}":
            jump ch15_2_scene_638
        "We'll help the citizens evacuate!{#ch15_2_c_636_3}":
            jump ch15_2_scene_639

label ch15_2_scene_637:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：じゃあ、俺達で砲台をつぶしに……。  [voice 13068]
    voice "ch15_s_054"
    s "Then we'll go take out the cannons…{#ch15_s_054}"

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：おまちなさい。
    voice "ch15_h_019"
    h "Wait. There are a great many cannons, heavily guarded.{#ch15_h_019}"

    # アンリエッタ：あなた達の力はよく承知していますが、
    voice "ch15_h_020"
    h "I know your strength well. But now, I want you to save it.{#ch15_h_020}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ですが、姫さま！  [voice 7090]
    voice "ch15_l_042"
    l "But, Princess!{#ch15_l_042}"

    # [SPRITE   lay8     image=+768, level=160, dir=1A]
    # アンリエッタ：あなた達はわが国にとって、切り札なのです。
    voice "ch15_h_021"
    h "You are our country's trump card. You must not act recklessly.{#ch15_h_021}"

    # → next scene 640
    jump ch15_2_scene_640

label ch15_2_scene_638:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：とにかく、敵兵を減らさないと、
    voice "ch15_s_055"
    s "Anyway, we need to thin out the enemy troops! Let us join the street fighting!{#ch15_s_055}"

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：その言葉、本当にうれしく思います。  [voice 705]
    voice "ch15_h_022"
    h "I'm truly glad to hear that.{#ch15_h_022}"

    # アンリエッタ：ですが、その件については許可できません。  [voice 706]
    voice "ch15_h_023"
    h "But I can't allow it.{#ch15_h_023}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ですが、姫さま！  [voice 7091]
    voice "ch15_l_043"
    l "But, Princess!{#ch15_l_043}"

    # [SPRITE   lay8     image=+768, level=160, dir=1A]
    # アンリエッタ：あなた達はわが国にとって、切り札なのです。
    voice "ch15_h_024"
    h "You are our country's trump card. You must not act recklessly.{#ch15_h_024}"

    # → next scene 640
    jump ch15_2_scene_640

label ch15_2_scene_639:

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：市街で戦いになってるということは、
    voice "ch15_s_056"
    s "If there's street fighting, civilians must be getting hurt, right?{#ch15_s_056}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：なんてことなの……。  [voice 7092]
    voice "ch15_l_044"
    l "Good heavens…{#ch15_l_044}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：俺達で避難の誘導を手伝おう。
    voice "ch15_s_057"
    s "Let's help guide the evacuation. It's the least we can do right now.{#ch15_s_057}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そうね……。
    voice "ch15_l_045"
    l "Right. Let's hurry!{#ch15_l_045}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：なりません。
    voice "ch15_h_025"
    h "No. Wait here for now.{#ch15_h_025}"

    # [SPRITE   lay8     image=+768, level=160, dir=1A]
    # アンリエッタ：あなた達はわが国にとって、切り札なのです。
    voice "ch15_h_026"
    h "You are our country's trump card. You must not act recklessly.{#ch15_h_026}"

    # → next scene 640
    jump ch15_2_scene_640

label ch15_2_scene_640:

    # [SPRITE   lay8     image=+768, level=160, dir=1A]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：しかし！  [voice 7094]
    voice "ch15_l_046"
    l "But!{#ch15_l_046}"

    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：このトリスタニアを攻撃するのに、
    voice "ch15_h_027"
    h "They wouldn't send only those infiltrated soldiers to attack Tristain.{#ch15_h_027}"

    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # アンリエッタ：おそらくは……。  [voice 711]
    voice "ch15_h_028"
    h "Most likely…{#ch15_h_028}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     hide]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay18    image=+1123, level=160, dir=1A]
    # 将校：報告します！  [voice 4335]
    voice "ch15_commander_011"
    commander "Reporting!{#ch15_commander_011}"

    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # 将校：アルビオン方面より敵艦隊の出撃が
    voice "ch15_commander_012"
    commander "Enemy fleet spotted departing from the direction of Albion.{#ch15_commander_012}"

    # [SPRITE   lay18    image=+1121, level=160, dir=1A]
    # 将校：進路はほぼまっすぐ。
    voice "ch15_commander_013"
    commander "Course is almost straight. It appears to be heading for Tristain.{#ch15_commander_013}"

    # [SPRITE   lay18    hide]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # ルイズ：なんですって！？  [voice 7095]
    voice "ch15_l_047"
    l "What!?{#ch15_l_047}"

    # アンリエッタ：来ましたか。  [voice 712]
    voice "ch15_h_029"
    h "So it's come.{#ch15_h_029}"

    # [SPRITE   lay8     image=+770, level=160, dir=1A]
    # アンリエッタ：破壊工作により最大限に混乱させたうえでの、
    voice "ch15_h_030"
    h "A surprise attack on the capital after maximum chaos from sabotage…{#ch15_h_030}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     level=152]
    # [SPRITE   lay18    image=+1125, level=158, dir=1A]
    # 将校：ま、まさか……。  [voice 4338]
    voice "ch15_commander_014"
    commander "N-No way…{#ch15_commander_014}"

    # アンリエッタ：もっとも恐れていたのですが……。  [voice 714]
    voice "ch15_h_031"
    h "It's what I feared most…{#ch15_h_031}"

    # [SPRITE   lay18    hide]
    # [SPRITE   lay1     image=+302, level=153, dir=1A]
    # ルイズ：……。  [voice 7096]
    voice "ch15_l_048"
    l "…{#ch15_l_048}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+407, level=154, dir=1B]
    # サイト：おい、ルイズ。
    voice "ch15_s_058"
    s "Hey, Louise. You've gone quiet—what's wrong?{#ch15_s_058}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 641
    jump ch15_2_scene_641

label ch15_2_scene_641:

    # [EVENT_CG event    image=+206, level=80]
    $ dissolve_fx("id(206)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+5]
    play music t4 fadein 1.0
    # ルイズ：姫さま……いえ、女王陛下。  [voice 7097]
    voice "ch15_l_049"
    l "Princess… no, Your Majesty.{#ch15_l_049}"

    # ルイズ：ルイズ・フランソワーズ、
    voice "ch15_l_050"
    l "Louise Francoise applies for permission to use Void magic in Tristain.{#ch15_l_050}"

    # サイト：お、おい。
    voice "ch15_s_059"
    s "H-Hey, Louise!{#ch15_s_059}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：このトリスタニアで虚無を使用するのですか？  [voice 715]
    voice "ch15_h_032"
    h "You intend to use Void here in Tristain?{#ch15_h_032}"

    # サイト：無茶だ。
    voice "ch15_s_060"
    s "That's insane. It's a fleet, a fleet! You saw the one that fell at Talb's plains!{#ch15_s_060}"

    # サイト：こんな市街地で墜落したら
    voice "ch15_s_061"
    s "If one crashes in a city like this, do you have any idea what'll happen!?{#ch15_s_061}"

    # [EVENT_CG event    image=+207, level=80]
    $ dissolve_fx("id(207)")
    # ルイズ：じゃあ、落させなきゃいいんでしょう！  [voice 7099]
    voice "ch15_l_051"
    l "Then just don't let it fall, silly!{#ch15_l_051}"

    # [SPRITE   lay5     hide]
    # サイト：そ、そんなに都合よくいくのかよ！  [voice 13076]
    voice "ch15_s_062"
    s "You make it sound so easy!{#ch15_s_062}"

    # ルイズ：うるさい、バカ犬！
    voice "ch15_l_052"
    l "Quiet, stupid dog! I have a plan!{#ch15_l_052}"

    # ルイズ：姫さま。
    voice "ch15_l_053"
    l "Princess. Please, grant permission…{#ch15_l_053}"

    # アンリエッタ：……。  [voice 716]
    voice "ch15_h_033"
    h "…{#ch15_h_033}"

    # アンリエッタ：分かりました。
    voice "ch15_h_034"
    h "Very well. I approve.{#ch15_h_034}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [SPRITE   lay8     hide]
    # [BG       stage    image=+35, level=200]
    $ fade_fx("id(35)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：都は、トリスタニアは本当に
    voice "ch15_s_063"
    s "The capital… Tristain will really be all right?{#ch15_s_063}"

    # ルイズ：……大丈夫、虚無の魔法といっても
    voice "ch15_l_054"
    l "…It's fine. Even if it's Void, I won't use Explosion.{#ch15_l_054}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ちょっと待て、どういうことだよ！  [voice 13078]
    voice "ch15_s_064"
    s "Wait, what do you mean!?{#ch15_s_064}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：虚無の魔法はエクスプロージョンだけ
    voice "ch15_l_055"
    l "Void isn't only Explosion, that's all.{#ch15_l_055}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：ん？
    voice "ch15_s_065"
    s "Hm? What do you mean?{#ch15_s_065}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay8     image=+764, level=160, dir=1A]
    # アンリエッタ：ルイズ、頼みましたよ。  [voice 718]
    voice "ch15_h_035"
    h "Louise, I'm counting on you.{#ch15_h_035}"

    # ルイズ：はい。
    voice "ch15_l_056"
    l "Yes. I won't fail you.{#ch15_l_056}"

    # [SPRITE   lay8     hide]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：うーん。  [voice 13080]
    voice "ch15_s_066"
    s "Ugh.{#ch15_s_066}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：まだ悩んでるの？
    voice "ch15_l_057"
    l "Still worrying? Let's go back to the inn!{#ch15_l_057}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：や、宿に？
    voice "ch15_s_067"
    s "Huh? Why the inn?{#ch15_s_067}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：虚無の魔法を使うためには、
    voice "ch15_l_058"
    l "To use Void, we need everyone's power.{#ch15_l_058}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：みんなの力？  [voice 13082]
    voice "ch15_s_068"
    s "Everyone's power?{#ch15_s_068}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # → next scene 642
    jump ch15_2_scene_642

label ch15_2_scene_642:

    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # サイト：なあ、ルイズ、ほんとに虚無を使うのか？  [voice 13083]
    voice "ch15_s_069"
    s "Say, Louise. Are you really going to use Void?{#ch15_s_069}"

    # ルイズ：あんたもしつこいわね。
    voice "ch15_l_059"
    l "You're so persistent. If I say I will, I will. What else can we do?{#ch15_l_059}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：それはそうなんだけどさ……。  [voice 13084]
    voice "ch15_s_070"
    s "That's true, but…{#ch15_s_070}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：あんたは、虚無を使った後のことばかり
    voice "ch15_l_060"
    l "You keep worrying about what happens after. What matters is before you use it.{#ch15_l_060}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：使う前？  [voice 13085]
    voice "ch15_s_071"
    s "Before?{#ch15_s_071}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：それでなくても、虚無の詠唱が長いのは、
    voice "ch15_l_061"
    l "You know the Void chant takes a long time, don't you?{#ch15_l_061}"

    # ルイズ：そこを邪魔しに、ウェザリーとアキナが
    voice "ch15_l_062"
    l "That's when Weatherly and Akina will come to interrupt.{#ch15_l_062}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：そうか。
    voice "ch15_s_072"
    s "Right. That's certainly possible.{#ch15_s_072}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：今、あの２人と戦えるのって、
    voice "ch15_l_063"
    l "Right now, only Tabitha and you can fight those two. That's… not enough, to put it mildly.{#ch15_l_063}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：戦力不足。  [voice 15796]
    voice "ch15_t_005"
    t "Not enough manpower.{#ch15_t_005}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：なのよ。
    voice "ch15_l_064"
    l "Exactly. If only Kirche were back to normal…{#ch15_l_064}"

    # ==== КОНЕЦ ЧАСТИ 2 ====
    jump ch15_3
    return

