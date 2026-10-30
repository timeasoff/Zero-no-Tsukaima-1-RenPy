# Chapter 6, part 1: scenes 344–355 and route extras 1429–1448.
# Source: ps2_source/chapters/chapter_07_家出のお姫さま.txt.
# EN/RU strings are translated incrementally from the JA source.
# Scene 360 is intentionally outside this part.

label ch6:
    # Source scene 344
    th "_It has been several days since the play ended. We still haven't found any clues about the bomber.{#ch6_344_th_001}"
    # JA: （演劇が終わってから、かれこれ数日。爆弾使いの手がかりは依然として、得られなかった）
    th "_We've kept investigating, but we haven't found any promising information. Louise is getting grumpier, too…{#ch6_344_th_002}"
    # JA: （調査は続けてるんだけど、どうにも有力な情報を得られない。ルイズも機嫌が悪くなってる……）
    th "_How long is this going to go on…?{#ch6_344_th_003}"
    # JA: （しかし、いつまでこの状態が続くんだろう……）
    voice "ch6_s_001"
    s "I'm home!{#ch6_s_001}"
    # JA[13378]: ただいまー。
    voice "ch6_l_001"
    l "Whew, my legs feel like lead…{#ch6_l_001}"
    # JA[7297]: はー、足が棒になっちゃったわ……。
    voice "ch6_si_001"
    si "Welcome back, Miss Vallière, Saito. How did the inquiries go?{#ch6_si_001}"
    # JA[15152]: おかえりなさいませ、 ミス・ヴァリエール、サイトさん。 聞き込みの方はいかがでした？
    voice "ch6_s_002"
    s "Absolutely terrible. We didn't find a single clue.{#ch6_s_002}"
    # JA[13379]: ぜーんぜんだめ。 なーんも手がかりなし。
    voice "ch6_l_002"
    l "What are we supposed to do? We can't just end this by saying, ‘The investigation went nowhere.’{#ch6_l_002}"
    # JA[7298]: どうしたものなのかしらね。 このまま、『捜査が進みませんでした』で、 終わるわけにはいかないわ。
    voice "ch6_s_003"
    s "Let's wait for everyone else to come back. That's why we split up to ask around in the first place.{#ch6_s_003}"
    # JA[13380]: 他のみんなが帰ってくるの待とうぜ。 そのために手分けして聞き込みしてるんだし。
    voice "ch6_l_003"
    l "Yes, you're right.{#ch6_l_003}"
    # JA[7299]: そうね。
    voice "ch6_g_001"
    g "Well, things are starting to get a little serious.{#ch6_g_001}"
    # JA[1539]: いやあ、ちょっと大変な感じになってきてるぞ。
    voice "ch6_l_004"
    l "Serious? What happened? Did you find something out?{#ch6_l_004}"
    # JA[7300]: 大変な、っていったい何が？ 何か分かったの？
    voice "ch6_m_001"
    m "It isn't about the bomber, but soldiers have started patrolling all over the city today.{#ch6_m_001}"
    # JA[4159]: 爆弾使いのことではないけど、 今日になって、兵士が街のあちこちを 見回り始めてるのよ。
    voice "ch6_l_005"
    l "Soldiers?{#ch6_l_005}"
    # JA[7301]: 兵士が？
    voice "ch6_m_002"
    m "Yes. Quite a few of them are going around, separate from the usual city guard patrols.{#ch6_m_002}"
    # JA[4160]: ええ。 街の警備とは別に、けっこうな人数が見て 回ってるの。
    voice "ch6_l_006"
    l "Could the army finally be getting serious about finding the bomber?{#ch6_l_006}"
    # JA[7302]: 軍の方も、本腰入れて爆弾使いを捜し出そうって ことなのかしら。
    voice "ch6_g_002"
    g "Who knows? Those aren't ordinary security patrols.{#ch6_g_002}"
    # JA[1540]: どうかな。 あれは通常の警備じゃない。
    voice "ch6_g_003"
    g "I suspect something happened, but it may not have anything to do with the bomber.{#ch6_g_003}"
    # JA[1541]: おそらく何かあったんだとは思うけど、 それが爆弾使いの件とは限らないんじゃ ないかな。
    voice "ch6_s_004"
    s "So something happened serious enough to rival the bomber incident?{#ch6_s_004}"
    # JA[13381]: 爆弾使いの件にならぶほどの、 事態が起きたってことか。
    voice "ch6_g_004"
    g "Most likely.{#ch6_g_004}"
    # JA[1542]: おそらくね。
    voice "ch6_t_001"
    t "The city is in trouble.{#ch6_t_001}"
    # JA[15802]: 街が、大変。
    voice "ch6_l_007"
    l "Oh, you're back, Tabitha and Kirche. You saw the soldiers in the city too, didn't you?{#ch6_l_007}"
    # JA[7303]: あら、おかえりタバサ、キュルケ。 あなた達も、街の兵士を見かけたのね？
    voice "ch6_t_002"
    t "Yes.{#ch6_t_002}"
    # JA[15803]: そう。
    voice "ch6_k_001"
    k "Indeed. And while we were at it, I asked why the soldiers were wandering around the city.{#ch6_k_001}"
    # JA[3825]: ええ。 ついでに、兵士が街をうろついてる理由も 聞いてきたわ。
    voice "ch6_l_008"
    l "So what exactly is the reason they're patrolling?{#ch6_l_008}"
    # JA[7304]: それで、兵士が見回ってる事情って いったいなに？
    voice "ch6_k_002"
    k "They said some important person has gone missing, though they don't know who.{#ch6_k_002}"
    # JA[3826]: ええ。 誰だかは分からないけど、 重要人物が行方不明になったとか言ってたわ。
    voice "ch6_l_009"
    l "An important person has gone missing…? Who could it be?{#ch6_l_009}"
    # JA[7305]: 重要人物が、行方不明……？ 誰かしら？
    voice "ch6_s_005"
    s "Hmm…{#ch6_s_005}"
    # JA[13382]: うーん……。
    voice "ch6_s_006"
    s "Hm?{#ch6_s_006}"
    # JA[13383]: ん？
    voice "ch6_si_002"
    si "Who is it?{#ch6_si_002}"
    # JA[15153]: どなたでしょうか？
    voice "ch6_h_001"
    h "It is I.{#ch6_h_001}"
    # JA[734]: わたくしです。
    voice "ch6_s_007"
    s "What!?{#ch6_s_007}"
    # JA[13384]: ええっ！？
    menu:
        "The princess!?":
            jump ch6_s345
            # JA: お姫さま！？
        "The innkeeper's voice changed!?":
            jump ch6_s346
            # JA: 宿屋の親父が声変わり！？
        "Who is Miss ‘It-is-I’!?":
            jump ch6_s347
            # JA: ワタクシさんって誰！？

label ch6_s345:
    # Source scene 345
    voice "ch6_s_008"
    s "The princess!?{#ch6_s_008}"
    # JA[13385]: お姫さま！？
    voice "ch6_si_003"
    si "What!?{#ch6_si_003}"
    # JA[15154]: ええっ！？
    voice "ch6_k_003"
    k "Why is Her Majesty the queen here!?{#ch6_k_003}"
    # JA[3827]: どうしてこんなところに、 女王陛下がいらっしゃるの！？
    voice "ch6_l_010"
    l "We have to welcome her, no matter what!{#ch6_l_010}"
    # JA[7306]: と、とにかくお迎えしないと！
    jump ch6_s348

label ch6_s346:
    # Source scene 346
    voice "ch6_s_009"
    s "When did the innkeeper get such a cute voice!?{#ch6_s_009}"
    # JA[13386]: 宿屋の親父、いつそんな可愛い声に！？
    voice "ch6_l_011"
    l "Idiot! Of course not! Anyone can tell that's the princess!{#ch6_l_011}"
    # JA[7307]: ばかっ！ そんなわけないでしょ！ どう聞いても姫さまじゃないの！
    voice "ch6_s_010"
    s "I-I was just joking.{#ch6_s_010}"
    # JA[13387]: じょ、冗談だよ。
    voice "ch6_l_012"
    l "W-we have to welcome her, no matter what!{#ch6_l_012}"
    # JA[7308]: と、とにかく、お迎えしないと！
    jump ch6_s348

label ch6_s347:
    # Source scene 347
    voice "ch6_s_011"
    s "Who is this ‘It-is-I’ person behind the door!?{#ch6_s_011}"
    # JA[13388]: ドアの向こうにいる、ワタクシさんって誰！？
    voice "ch6_l_013"
    l "Who are you talking about!? That is obviously the princess's voice! You really are a hopeless familiar!{#ch6_l_013}"
    # JA[7309]: どこの誰よ、それ！ どう聞いても姫さまのお声じゃないの！ ほんっとにバカ使い魔ね！
    voice "ch6_s_012"
    s "Aww, it was only a little joke…{#ch6_s_012}"
    # JA[13389]: うう、お茶目な冗談だったのにぃ……。
    jump ch6_s348

label ch6_s348:
    # Source scene 348
    voice "ch6_h_002"
    h "Good day, everyone.{#ch6_h_002}"
    # JA[735]: ごきげんよう、皆さん。
    voice "ch6_l_014"
    l "Good day… Your Highness, why are you here!? Is everything all right at the palace!?{#ch6_l_014}"
    # JA[7310]: ごきげんよう……って、 姫さま、なぜこのような所に！？ 王宮の方はよろしいのですか！？
    voice "ch6_h_003"
    h "I slipped away because I had something I absolutely had to tell you all.{#ch6_h_003}"
    # JA[736]: 皆さんにどうしても伝えなければならない 用事があって、抜け出してきたのです。
    voice "ch6_t_003"
    t "The soldiers are looking for Her Majesty.{#ch6_t_003}"
    # JA[15804]: 兵士達が、陛下を捜してる。
    voice "ch6_g_005"
    g "Ah, Your Majesty! You came all this way just to see me!{#ch6_g_005}"
    # JA[1543]: ああ、女王陛下！ ぼくに会いに来るためにわざわざ！
    voice "ch6_m_003"
    m "Save your daydreams for when you're asleep.{#ch6_m_003}"
    # JA[4161]: 寝言は寝てから。
    voice "ch6_s_013"
    s "B-but Your Highness, what could possibly be so important that you left the palace?{#ch6_s_013}"
    # JA[13390]: で、でもお姫さま、 王宮を抜け出して来るなんて、 いったいどんな用件なんですか？
    voice "ch6_h_004"
    h "It is nothing less than this: I would like you to hide me for a while.{#ch6_h_004}"
    # JA[737]: 用件というのは、ほかでもありません。 しばらくの間、 わたくしをかくまってほしいのです。
    voice "ch6_s_014"
    s "What!?{#ch6_s_014}"
    # JA[13391]: はい！？
    voice "ch6_l_015"
    l "W-wait a moment. Why would you need us to hide you!?{#ch6_l_015}"
    # JA[7311]: ちょ、ちょっと待ってください。 かくまうって、それこそいったいどうして！？
    voice "ch6_l_016"
    l "Please forgive me, Your Highness. Could you tell us what happened?{#ch6_l_016}"
    # JA[7312]: すみません、姫さま。 詳しい話をお聞かせいただけますでしょうか。
    voice "ch6_h_005"
    h "Of course. I shall explain everything now.{#ch6_h_005}"
    # JA[738]: ええ、もちろんですわ。 それをこれから説明いたします。
    jump ch6_s349

label ch6_s349:
    # Source scene 349
    voice "ch6_h_006"
    h "As for the investigation into the bombing incidents I asked you to conduct…{#ch6_h_006}"
    # JA[739]: あなたがたにお願いした、 爆破事件の調査なのですけれど……。
    voice "ch6_l_017"
    l "Well, um… There hasn't been much progress…{#ch6_l_017}"
    # JA[7313]: あの、その。 進展がなかなか……。
    voice "ch6_h_007"
    h "I am aware of that. I did not come here to reprimand you.{#ch6_h_007}"
    # JA[740]: それは承知しています。 あなたがたをとがめるために 来たのではありません。
    voice "ch6_h_008"
    h "After examining the reports on each incident, we discovered what appears to be a new fact.{#ch6_h_008}"
    # JA[741]: 各事件の報告を元に、こちらでも検討した結果、 新たな事実と思われるものを発見したのです。
    voice "ch6_s_015"
    s "A discovery…?{#ch6_s_015}"
    # JA[13392]: 発見……ですか。
    voice "ch6_h_009"
    h "This series of bombings follows a certain pattern. Everyone, look at this map.{#ch6_h_009}"
    # JA[742]: 今回の一連の爆破事件には、 ある法則があります。 皆さん、この地図を見てください。
    voice "ch6_l_018"
    l "This is a map of Tristain, isn't it?{#ch6_l_018}"
    # JA[7314]: これは……トリスタニアの地図、ですね。
    voice "ch6_h_010"
    h "Yes. This central area is the royal palace, and these marks show the sites of the bombings.{#ch6_h_010}"
    # JA[743]: はい。 この中心部分が王宮。 そして、このマークが爆破された現場です。
    voice "ch6_k_004"
    k "Ah…!{#ch6_k_004}"
    # JA[3828]: あ……！
    voice "ch6_g_006"
    g "Huh? What is it?{#ch6_g_006}"
    # JA[1544]: え、どうしたんだい？
    voice "ch6_k_005"
    k "I see.{#ch6_k_005}"
    # JA[3829]: なるほどね。
    voice "ch6_l_019"
    l "The bombing sites are concentrated around the palace…?{#ch6_l_019}"
    # JA[7315]: 爆破現場は、城の周辺に集中してる……？
    voice "ch6_k_006"
    k "‘Concentrated’ doesn't begin to describe it. The order is random, but they seem to form a ring around the palace.{#ch6_k_006}"
    # JA[3830]: 集中してるどころじゃないわよ。 順番はバラバラだけど、 城を取り囲むような場所で起きてる感じね。
    voice "ch6_m_004"
    m "That is far too precise to be coincidence. It must have been deliberate.{#ch6_m_004}"
    # JA[4162]: 偶然にしては、あまりに正確ですわね。 たしかに、意図的なものでしょう。
    voice "ch6_h_011"
    h "Do you see what I mean? I cannot help thinking that these incidents were not the work of a lone criminal.{#ch6_h_011}"
    # JA[744]: 分かっていただけたでしょうか？ この事件はただの単独犯ではない。 そう思えてならないのです。
    voice "ch6_g_007"
    g "But even if that is true, what would it mean?{#ch6_g_007}"
    # JA[1545]: でも、そうだとして、いったい何の意味が？
    voice "ch6_h_012"
    h "We cannot leave the places damaged by the bombings as they are. We will clear away the rubble and carry out repairs, but…{#ch6_h_012}"
    # JA[745]: 爆破で壊された箇所を、そのままにして おくわけにはまいりません。 瓦礫を片づけ、修復工事を行うのですが……。
    voice "ch6_h_013"
    h "With so many places to repair, there are not enough craftsmen to do the work.{#ch6_h_013}"
    # JA[746]: これだけ修復箇所が多いと、 作業に携わる職人が不足しています。
    voice "ch6_h_014"
    h "So, to begin the repairs as quickly as possible, we are gathering craftsmen from both inside and outside the country.{#ch6_h_014}"
    # JA[747]: そこで、早急に修復作業をおこなうため、 職人を国の内外から集めているのです。
    voice "ch6_s_016"
    s "So…{#ch6_s_016}"
    # JA[13393]: つまり……、
    menu:
        "The culprit was a craftsman who went on a bombing spree to get work?":
            jump ch6_s350
            # JA: 仕事を作るために事件を起こした？
        "The bombings were meant to lure enemy agents here?":
            jump ch6_s351
            # JA: 工作員を誘導するために事件を？
        "Just a bombing fanatic":
            jump ch6_s352
            # JA: ただの爆破マニア

label ch6_s350:
    # Source scene 350
    voice "ch6_s_017"
    s "So the culprit was a craftsman who went on a bombing spree to get work?{#ch6_s_017}"
    # JA[13394]: 犯人は職人で、仕事にありつくために、 爆破してまわったってことか？
    voice "ch6_l_020"
    l "That can't be it, can it?{#ch6_l_020}"
    # JA[7316]: そうじゃないでしょ？
    voice "ch6_l_021"
    l "They disguised agents as craftsmen and used this plan to infiltrate them into our country. That's what you mean, Your Highness?{#ch6_l_021}"
    # JA[7317]: 職人を装って、工作員を我が国に 潜入させる作戦ね。 そういうことでしょうか、姫さま。
    jump ch6_s353

label ch6_s351:
    # Source scene 351
    voice "ch6_s_018"
    s "Did they cause the bombings to lure agents posing as craftsmen into the country?{#ch6_s_018}"
    # JA[13395]: 職人を装う工作員を誘導させるために、 爆破事件を起こした？
    voice "ch6_h_015"
    h "Yes.{#ch6_h_015}"
    # JA[748]: はい。
    voice "ch6_k_007"
    k "They set off bombings around the palace in advance, then planned to infiltrate during the repair work… That is the plan, isn't it?{#ch6_k_007}"
    # JA[3831]: あらかじめ王宮周辺で爆破事件を起こし、 その修復作業に乗じて潜入する……、 そういう手はずなのではないか、ということね。
    jump ch6_s353

label ch6_s352:
    # Source scene 352
    voice "ch6_s_019"
    s "The culprit was just a bombing fanatic, wasn't he?{#ch6_s_019}"
    # JA[13396]: 犯人は、ただの爆破マニアだろ？
    voice "ch6_l_022"
    l "How did you come to that conclusion!? You mean there are agents hiding among all the craftsmen hired for the repairs!{#ch6_l_022}"
    # JA[7318]: なんでそうなるのよっ！ 修復工事のために大量に雇われる職人の中に、 工作員が潜んでるってことでしょ！
    jump ch6_s353

label ch6_s353:
    # Source scene 353
    voice "ch6_h_016"
    h "Most likely. For now, I am the only one who suspects it,{#ch6_h_016}"
    # JA[749]: おそらくは。 それを疑っているのは、 今のところわたくしだけですし、
    voice "ch6_h_017"
    h "but it may be nothing more than needless worry. However…{#ch6_h_017}"
    # JA[750]: ただの杞憂なのかもしれません。 ですが……。
    voice "ch6_l_023"
    l "If that is true, it would be a disaster! We have to find the agents immediately! It may be difficult, but we could investigate every craftsman…{#ch6_l_023}"
    # JA[7319]: それが本当だったら、大変です！ 今すぐにでも、工作員を見つけ出さないと！ 大変かもしれませんが、職人全員を調べて……。
    voice "ch6_h_018"
    h "…It would probably be pointless.{#ch6_h_018}"
    # JA[751]: ……おそらく無駄になるでしょう。
    voice "ch6_l_024"
    l "Why is that?{#ch6_l_024}"
    # JA[7320]: どうしてです？
    voice "ch6_h_019"
    h "These are unsettled times. Naturally, the identities of craftsmen from abroad are checked. Anyone with a suspicious background cannot enter the country.{#ch6_h_019}"
    # JA[752]: 情勢が不穏なこの時期です。 当然、国外の職人は、身元を確認しています。 素性が怪しい者は国内に入ることはできません。
    voice "ch6_l_025"
    l "Um…?{#ch6_l_025}"
    # JA[7321]: ええと……？
    voice "ch6_h_020"
    h "The influential nobles of our country are the ones who vouch for the craftsmen's identities.{#ch6_h_020}"
    # JA[753]: 職人の身元を保証しているのは、 我が国の有力貴族達なのです。
    voice "ch6_h_021"
    h "I do not want to think about it, but… if one of those nobles were to sell out the country, it would be easy to falsify an agent's identity.{#ch6_h_021}"
    # JA[754]: 考えたくはありませんが……、 もしその貴族の中に国を売る者がいるとしたら。 工作員の身元を偽るのも簡単なことです。
    voice "ch6_l_026"
    l "No! That would be the grave crime of betraying the country!{#ch6_l_026}"
    # JA[7322]: そんな！ 国を裏切る大罪です！
    voice "ch6_h_022"
    h "But I can think of no other explanation.{#ch6_h_022}"
    # JA[755]: ですが、他に考えられません。
    voice "ch6_h_023"
    h "That is why I have a request for all of you. If possible, could you hide me here?{#ch6_h_023}"
    # JA[756]: そこでみなさんにお願いがあるのです。 できれば、ここでわたくしをかくまって いただけませんか？
    voice "ch6_h_024"
    h "If word gets out that I am absent, someone may take advantage of it and make a move. Will you do this for me?{#ch6_h_024}"
    # JA[757]: わたくしの不在を知れば、それに乗じて、 なんらかの動きがあるかもしれません。 お願いできますか？
    voice "ch6_l_027"
    l "Of course!{#ch6_l_027}"
    # JA[7323]: もちろんです！
    voice "ch6_s_020"
    s "It sounds like the decision has already been made for us. We have no choice but to do it.{#ch6_s_020}"
    # JA[13397]: もう決定事項みたいですし。 やるしかないでしょう。
    voice "ch6_g_008"
    g "At Her Majesty's command, Guiche de Gramont will protect her with his life!{#ch6_g_008}"
    # JA[1546]: 女王陛下のご命令とあらば、 このギーシュ・ド・グラモン、 一命を賭してお守りいたします！
    voice "ch6_m_005"
    m "There he goes again… Yes, I will help as well.{#ch6_m_005}"
    # JA[4163]: また調子に乗って……。 ええ、わたしもご協力いたしますわ。
    voice "ch6_si_004"
    si "Um, I-I cannot do much, but if I can be of help…!{#ch6_si_004}"
    # JA[15155]: ええと、わ、わたくしっ、何もできませんけど、 お力になれるのでしたらっ！
    voice "ch6_ha_001"
    ha "I do not really understand, but if everyone says so…{#ch6_ha_001}"
    # JA[2632]: よく分かりませんけど、皆がそう言うなら。
    t "……{#ch6_t_004}"
    # JA: ……
    voice "ch6_k_008"
    k "Well, we're already involved now.{#ch6_k_008}"
    # JA[3832]: ま、乗りかかった船だしね。
    voice "ch6_s_021"
    s "Looks like everyone agrees. From today on, guarding the princess is part of our mission too.{#ch6_s_021}"
    # JA[13398]: どうやら、全員一致のようだな。 今日からは、お姫さまの護衛も任務ってわけだ。
    voice "ch6_h_025"
    h "Please take good care of me.{#ch6_h_025}"
    # JA[758]: どうか、よろしくお願いいたします。
    jump ch6_s354

label ch6_s354:
    # Source scene 354
    voice "ch6_l_028"
    l "So, out you go.{#ch6_l_028}"
    # JA[7324]: と、いうわけで。 出てって。
    voice "ch6_s_022"
    s "Wait a minute! What do you mean, ‘so’? Why am I the only one being kicked out of the room!?{#ch6_s_022}"
    # JA[13399]: ちょっと待て！ なにが『というわけで』なんだ！？ なんで俺だけ部屋の外に追い出されるんだ！？
    voice "ch6_l_029"
    l "Oh, don't worry. Guiche is coming with you.{#ch6_l_029}"
    # JA[7325]: ああ、安心して。 ギーシュも一緒だから。
    voice "ch6_g_009"
    g "Why am I being kicked out too!?{#ch6_g_009}"
    # JA[1547]: なんでぼくまで追い出されるんだ！？
    voice "ch6_s_023"
    s "Exactly! Don't lump me together with this womanizer!{#ch6_s_023}"
    # JA[13400]: そうだぞ、俺をこんな女たらしと一緒にするな！
    voice "ch6_l_030"
    l "From now on, this will be the women's room, so men are forbidden.{#ch6_l_030}"
    # JA[7326]: こっちの部屋は、今後、 女性部屋ってことにするから、男子禁制なの。
    voice "ch6_s_024"
    s "Oh, I see. Well, I guess it can't be helped.{#ch6_s_024}"
    # JA[13401]: ああ、そういうことか。 そりゃまあ、しょうがねえな。
    voice "ch6_g_010"
    g "N-no! This can't be happening! My dream of serving beside Her Majesty and letting her experience my charms…!{#ch6_g_010}"
    # JA[1548]: そ、そんな！ せっかく女王陛下のお側近くにお仕えして、 ぼくの魅力に触れてもらおうという夢がっ！
    voice "ch6_s_025"
    s "Come on, Guiche.{#ch6_s_025}"
    # JA[13402]: ほら、行くぞギーシュ。
    voice "ch6_g_011"
    g "This is too cruel…{#ch6_g_011}"
    # JA[1549]: ああ、あんまりだあああ……。
    voice "ch6_s_026"
    s "Enough. Get some sleep. We have to guard the princess starting tomorrow.{#ch6_s_026}"
    # JA[13403]: いいから。 さっさと寝て、明日からお姫さまの警護だ。
    voice "ch6_l_031"
    l "Good night, then.{#ch6_l_031}"
    # JA[7327]: じゃ、おやすみ。
    voice "ch6_s_027"
    s "Yeah. Don't kick off the futon and catch a chill while you sleep.{#ch6_s_027}"
    # JA[13404]: おう。 フトン蹴飛ばして、寝冷えするなよー。
    voice "ch6_l_032"
    l "I won't!{#ch6_l_032}"
    # JA[7328]: しないわよっ！
    jump ch6_s355

label ch6_s355:
    # Source scene 355
    voice "ch6_s_028"
    s "Mmm… yawn. Good grief, it's morning already.{#ch6_s_028}"
    # JA[13405]: んー……ふああ。 やれやれ、もう朝か。
    voice "ch6_s_029"
    s "I always wake up early out of habit.{#ch6_s_029}"
    # JA[13406]: いつものクセで、どうにも早く目が 覚めちまうな。
    voice "ch6_s_030"
    s "Where did Guiche get to…?{#ch6_s_030}"
    # JA[13407]: ギーシュのやつは……。
    voice "ch6_g_012"
    g "Mmm… mumble, mumble.{#ch6_g_012}"
    # JA[1550]: うーん……むにゃむにゃ。
    voice "ch6_s_031"
    s "That's nobles for you…{#ch6_s_031}"
    # JA[13408]: 本当に貴族ってやつはぁ……。
    voice "ch6_s_032"
    s "Hm? Who is it?{#ch6_s_032}"
    # JA[13409]: ん、誰です？
    voice "ch6_h_026"
    h "Um, are you awake?{#ch6_h_026}"
    # JA[759]: あの、起きてますか？
    voice "ch6_s_033"
    s "Princess?{#ch6_s_033}"
    # JA[13410]: お姫さま？
    voice "ch6_h_027"
    h "Good, you were already awake.{#ch6_h_027}"
    # JA[760]: 良かった、もう起きてらっしゃいましたね。
    voice "ch6_s_034"
    s "Y-yes. I am an early riser.{#ch6_s_034}"
    # JA[13411]: は、はい。 早起きなもんで。
    voice "ch6_s_035"
    s "What brings you out so early, Princess?{#ch6_s_035}"
    # JA[13412]: お姫さまこそ、どうしたんですかこんな早く。
    voice "ch6_h_028"
    h "Perhaps I woke earlier than usual because I slept in an unfamiliar bed… Since I am awake, I thought I would look around the city.{#ch6_h_028}"
    # JA[761]: 慣れないベッドで寝たせいでしょうか、 いつもより早く目が覚めてしまって……。 それで、せっかくですから街を見て回ろうかと。
    voice "ch6_s_036"
    s "Pardon?{#ch6_s_036}"
    # JA[13413]: はい？
    voice "ch6_s_037"
    s "U-um, it is dangerous to go outside in our current situation, so you should probably give up on the walk…{#ch6_s_037}"
    # JA[13414]: あ、あのー、今の状況で外に出るのは 危険ですし、散歩は控えた方が……。
    voice "ch6_s_038"
    s "A-and if something happens, Louise will…{#ch6_s_038}"
    # JA[13415]: そ、それに何かあったら、俺がルイズに……。
    voice "ch6_h_029"
    h "I will smooth things over with Louise. Now, let us go.{#ch6_h_029}"
    # JA[762]: ルイズには、わたくしがとりなします。 では、まいりましょう。
    voice "ch6_s_039"
    s "W-wait… All right, all right, just don't pull so hard!{#ch6_s_039}"
    # JA[13416]: あ、ちょっと……分かりました。 分かりましたから、そんなに 引っぱらないでください！
    menu:
        "In front of the castle":
            jump ch6_s1429
            # JA: 城前
        "Down a back street":
            jump ch6_s1434
            # JA: 裏通り
        "Along the highway":
            jump ch6_s1439
            # JA: 街道
        "On the main street":
            jump ch6_s1444
            # JA: 表通り

label ch6_s1429:
    # Source scene 1429
    voice "ch6_h_030"
    h "This is a spacious place.{#ch6_h_030}"
    # JA[476]: ここは広いところですね。
    voice "ch6_s_040"
    s "Princess, there seem to be a lot of soldiers here. If we stay too long, they will find you.{#ch6_s_040}"
    # JA[10265]: お姫さま。 ここは兵士が多いみたいですし、 あんまり長くいては見つかりますよ。
    voice "ch6_h_031"
    h "How diligent they are. That is a good thing.{#ch6_h_031}"
    # JA[477]: まあ。 仕事熱心なのはよいことですわ。
    voice "ch6_s_041"
    s "This is no time to be so relaxed. They are looking for you… We need to move, quickly.{#ch6_s_041}"
    th "_Oh no, we're too late!{#ch6_1429_th_001}"
    # JA: （ああっ、遅かった！）
    # JA[10266]: そんなのんびりしてる状況じゃないですって。 お姫さまを探してるんだから……。 とにかく、早く移動しましょう。
    voice "ch6_unk_001"
    unk "Hey, you there.{#ch6_unk_001}"
    # JA[4218]: おい、そこの。
    voice "ch6_h_032"
    h "Yes?{#ch6_h_032}"
    # JA[478]: はい？
    voice "ch6_unk_002"
    unk "Hmm. Height… hair color… You match the description of the person we have orders to find. Come with me to the guard post.{#ch6_unk_002}"
    # JA[4219]: ふむ、身長……髪の色……。 捜索命令のある人物の特徴と合うな。 お前、ちょっと詰め所まで来てもらおう。
    voice "ch6_s_042"
    s "W-wait a moment!{#ch6_s_042}"
    # JA[10267]: ちょ、ちょっと待ってください！
    menu:
        "What about my cousin?":
            jump ch6_s1430
            # JA: 俺のいとこがどうかしましたか
        "What about my sister-in-law?":
            jump ch6_s1431
            # JA: 俺の義姉がどうかしましたか
        "What about my fiancée?":
            jump ch6_s1432
            # JA: 俺の許嫁がどうかしましたか

label ch6_s1430:
    # Source scene 1430
    voice "ch6_s_043"
    s "What about my cousin?{#ch6_s_043}"
    # JA[10268]: 俺のいとこがどうかしましたか？
    voice "ch6_unk_003"
    unk "Your cousin?{#ch6_unk_003}"
    # JA[4220]: いとこ？
    voice "ch6_s_044"
    s "Yes. She is my cousin from the frontier. She only arrived in the city this morning.{#ch6_s_044}"
    # JA[10269]: そうです。 辺境に住んでるいとこで。 今朝この街に着いたばかりなんです。
    voice "ch6_s_045"
    s "I am showing her around right now.{#ch6_s_045}"
    # JA[10270]: 今、俺が道案内してるんですよ。
    voice "ch6_s_046"
    s "Sorry. She is not familiar with the city yet.{#ch6_s_046}"
    # JA[10271]: すいません、本当、街に慣れてないもんで。
    voice "ch6_unk_004"
    unk "Hm? Oh, all right. You may pass.{#ch6_unk_004}"
    # JA[4221]: ん？ ああ、いや、分かった。 通ってよし。
    voice "ch6_s_047"
    s "Then, if you will excuse us!{#ch6_s_047}"
    # JA[10272]: それじゃ、失礼しますっ！
    jump ch6_s1433

label ch6_s1431:
    # Source scene 1431
    voice "ch6_s_048"
    s "What about my sister-in-law?{#ch6_s_048}"
    # JA[10273]: 俺の義姉がどうかしましたか？
    voice "ch6_unk_005"
    unk "Is that so? Still, we should question her, just in case…{#ch6_unk_005}"
    # JA[4222]: そうなのか？ だが、一応取り調べを……。
    voice "ch6_h_033"
    h "Oh, but I have to go to the Duke of Vallière's estate on my husband's business.{#ch6_h_033}"
    # JA[479]: あら、わたくしこれから夫の用事で、 ヴァリエール公爵様のお屋敷に行かねば いけないのですけれど。
    voice "ch6_unk_006"
    unk "The Duke of Vallière's estate? Hmm… In that case, perhaps I will ask at the duke's residence later.{#ch6_unk_006}"
    # JA[4223]: ヴァリエール公爵邸に？ ううむ……。 そういうことなら、後ほど公爵邸に尋ねるか。
    voice "ch6_s_049"
    s "Then, if you will excuse us!{#ch6_s_049}"
    # JA[10274]: それじゃ、失礼しますっ！
    jump ch6_s1433

label ch6_s1432:
    # Source scene 1432
    voice "ch6_s_050"
    s "What about my fiancée?{#ch6_s_050}"
    # JA[10275]: 俺の許嫁がどうかしましたか？
    voice "ch6_unk_007"
    unk "Your fiancée?{#ch6_unk_007}"
    # JA[4224]: 許嫁だと？
    voice "ch6_s_051"
    s "That's right.{#ch6_s_051}"
    # JA[10276]: そうです。
    voice "ch6_s_052"
    s "She lived on the frontier until now and only arrived in the city this morning so I could introduce her to my family before the wedding.{#ch6_s_052}"
    # JA[10277]: 今まで辺境に住んでた娘で、 結婚式の前に家族に紹介するために、 今朝この街に着いたばかりなんですよ。
    voice "ch6_unk_008"
    unk "Is that so? Ah, congratulations.{#ch6_unk_008}"
    # JA[4225]: そうなのか？ あー、おめでとう。
    voice "ch6_s_053"
    s "Then, if you will excuse us, we are in a hurry!{#ch6_s_053}"
    # JA[10278]: それじゃ、急いでるんで失礼しますっ！
    jump ch6_s1433

label ch6_s1433:
    # Source scene 1433
    voice "ch6_s_054"
    s "Now, let's move before any more nuisances stop us.{#ch6_s_054}"
    # JA[10279]: さあて、これ以上余計な連中につかまらない ように、さっさと移動しちゃいましょう。
    voice "ch6_h_034"
    h "Yes, indeed.{#ch6_h_034}"
    # JA[502]: ええ。 そうですね。

label ch6_s1434:
    # Source scene 1434
    voice "ch6_h_035"
    h "Oh, this is… a back street, isn't it? What a desolate road…{#ch6_h_035}"
    # JA[480]: あら、ここは確か……裏路地、ですね？ ずいぶんと寂しい通り……。
    voice "ch6_s_055"
    s "Whoa, whoa, whoa, Princess, this won't do! This is dangerous territory where rough characters hang around.{#ch6_s_055}"
    # JA[10280]: うわわわわわ、駄目ですよお姫さま。 ここは柄の悪い連中がたむろってる、 危険地帯ですよ。
    voice "ch6_h_036"
    h "Dangerous?{#ch6_h_036}"
    # JA[481]: 危険、ですか。
    voice "ch6_s_056"
    s "Yes. It is dangerous for a girl like you to come to a place like this!{#ch6_s_056}"
    # JA[10281]: そうですよ。 こんなところに、お姫さまみたいな女の子が 来たら危険です！
    voice "ch6_h_037"
    h "Is that so? Then what sort of girl is allowed to come here?{#ch6_h_037}"
    # JA[482]: そうなのですか。 では、どんな女の子なら来てもいいのですか？
    voice "ch6_s_057"
    s "Um…{#ch6_s_057}"
    # JA[10282]: ええと……。
    menu:
        "A girl like Kirche":
            jump ch6_s1435
            # JA: キュルケみたいな子
        "Someone like me":
            jump ch6_s1436
            # JA: 俺みたいなやつ
        "No girl should come here":
            jump ch6_s1437
            # JA: どんな子でもだめです

label ch6_s1435:
    # Source scene 1435
    voice "ch6_s_058"
    s "Maybe a girl like Kirche.{#ch6_s_058}"
    # JA[10283]: キュルケみたいな子かな。
    voice "ch6_h_038"
    h "Miss Kirche?{#ch6_h_038}"
    # JA[483]: キュルケさん、ですの？
    voice "ch6_s_059"
    s "Yes. Kirche is good at handling people, you know…{#ch6_s_059}"
    # JA[10284]: ええ。 キュルケって、人あしらいが 上手っていうか……。
    voice "ch6_s_060"
    s "So even if she met some dangerous-looking people here, I think she could talk her way out of it.{#ch6_s_060}"
    # JA[10285]: だから、こういうところで危なそうな 連中に会っても、うまいこと切り抜けると 思いますよ。
    voice "ch6_h_039"
    h "I see. She is good at handling people.{#ch6_h_039}"
    # JA[484]: なるほど。 人あしらいですか。
    jump ch6_s1438

label ch6_s1436:
    # Source scene 1436
    voice "ch6_s_061"
    s "Someone like me!{#ch6_s_061}"
    # JA[10286]: 俺みたいな子です！
    voice "ch6_h_040"
    h "Hm? Familiar… are you a girl?{#ch6_h_040}"
    # JA[485]: え？ 使い魔さん……女の子でした？
    voice "ch6_s_062"
    s "No, no, no, no, that's not it. I'm a man.{#ch6_s_062}"
    # JA[10287]: いえいえいえいえ、違います。 俺は男です。
    voice "ch6_s_063"
    s "I mean, a manly girl like me probably wouldn't get attacked.{#ch6_s_063}"
    # JA[10288]: ですから、俺みたいな…… 男っぽい女の子なら、 襲われたりはしないだろうなあと。
    voice "ch6_h_041"
    h "Oh… is that so? If you were a girl, familiar, I imagine you would be rather cute.{#ch6_h_041}"
    # JA[486]: はあ……そうなんですの？ 使い魔さんが女の子だったら、 それなりにかわいい気がしますけれど。
    voice "ch6_s_064"
    s "Please don't say creepy things like that.{#ch6_s_064}"
    # JA[10289]: 気色悪いこと言わないでください。
    jump ch6_s1438

label ch6_s1437:
    # Source scene 1437
    voice "ch6_s_065"
    s "There is no girl who should come to a place like this. That is how dangerous it is.{#ch6_s_065}"
    # JA[10290]: こんなとこに来てもいい女の子なんていません。 それだけ危ないところなんですから。
    voice "ch6_h_042"
    h "Hee hee. You treat women with respect, don't you, familiar?{#ch6_h_042}"
    # JA[487]: くすっ。 使い魔さんは女性を大事に 扱ってくださるんですね。
    voice "ch6_s_066"
    s "Actually, I do. Just kidding.{#ch6_s_066}"
    # JA[10291]: 実はそうなんです。 なんちて。
    voice "ch6_h_043"
    h "Protecting women… That is the spirit of chivalry. How admirable. Though, familiar, you have quite a silly grin on your face.{#ch6_h_043}"
    # JA[488]: 女性を守る……騎士道精神ですね。 すばらしいことですわ。 でも、使い魔さん、顔が緩んでますけど。
    voice "ch6_s_067"
    s "I do not! Heh heh heh.{#ch6_s_067}"
    # JA[10292]: そんなことないですよ、でへへへ。
    jump ch6_s1438

label ch6_s1438:
    # Source scene 1438
    voice "ch6_s_068"
    s "A-anyway. It is dangerous to stay here, so let's move on quickly.{#ch6_s_068}"
    # JA[10293]: と、とにかく。 こんなところにいたら危険ですから、 さっさと移動しましょう。
    voice "ch6_h_044"
    h "All right.{#ch6_h_044}"
    # JA[489]: 分かりました。

label ch6_s1439:
    # Source scene 1439
    voice "ch6_h_045"
    h "This place is so lush and green. It is wide open… What a pleasant view.{#ch6_h_045}"
    # JA[490]: ここは、緑が豊かな場所ですね。 広々として……気持ちの良い光景です。
    voice "ch6_s_069"
    s "If we leave the city and follow this highway straight ahead, we will reach the Academy of Magic.{#ch6_s_069}"
    # JA[10294]: このまま街を出て、 この街道をまっすぐ進むと、魔法学院ですね。
    voice "ch6_h_046"
    h "So this is the city's boundary.{#ch6_h_046}"
    # JA[491]: ここが、街の境界になるのですね。
    voice "ch6_s_070"
    s "Yes.{#ch6_s_070}"
    # JA[10295]: そうですね。
    voice "ch6_h_047"
    h "If only I could keep following this road and go far away…{#ch6_h_047}"
    # JA[492]: このまま、この道を進んで遠くに行けたら……。
    voice "ch6_s_071"
    s "Princess?{#ch6_s_071}"
    # JA[10296]: お姫さま？
    voice "ch6_h_048"
    h "Oh, it is nothing. Just idle chatter.{#ch6_h_048}"
    # JA[493]: いえ、なんでもありません。 ただの戯言です。
    voice "ch6_s_072"
    s "Princess…{#ch6_s_072}"
    # JA[10297]: お姫さま……。
    menu:
        "Someday, you will be able to go wherever you wish":
            jump ch6_s1440
            # JA: いつか、自由に行けますよ
        "You must not run away":
            jump ch6_s1441
            # JA: 逃げちゃ駄目です
        "It is dangerous to lose your way":
            jump ch6_s1442
            # JA: 道に迷うと大変ですよ

label ch6_s1440:
    # Source scene 1440
    voice "ch6_s_073"
    s "Someday, you will be able to go wherever you wish.{#ch6_s_073}"
    # JA[10298]: いつか、自由に行けますよ。
    voice "ch6_h_049"
    h "Do you think so…?{#ch6_h_049}"
    # JA[494]: そうでしょうか……。
    voice "ch6_s_074"
    s "In the world I came from, anyone can travel freely. Someday, perhaps this world will be the same…{#ch6_s_074}"
    # JA[10299]: 俺のいた世界は誰だって自由に旅ができます。 この世界だっていつかは……。
    voice "ch6_h_050"
    h "Yes, perhaps. Familiar… thank you.{#ch6_h_050}"
    # JA[495]: そうですね。 使い魔さん……ありがとう。
    jump ch6_s1443

label ch6_s1441:
    # Source scene 1441
    voice "ch6_s_075"
    s "You must not run away.{#ch6_s_075}"
    # JA[10300]: 逃げちゃ駄目ですよ。
    voice "ch6_h_051"
    h "Yes, I understand that. As long as I am queen, I must not forget the responsibilities I bear.{#ch6_h_051}"
    # JA[496]: ええ、それは分かっています。 わたくしが女王である以上、 忘れてはならない責務があることは。
    voice "ch6_h_052"
    h "That is why I told you, was it not? It was only idle chatter, nothing more.{#ch6_h_052}"
    # JA[497]: ですから、申し上げたでしょう？ 戯言なのですよ、ただの。
    voice "ch6_s_076"
    s "I'm sorry.{#ch6_s_076}"
    # JA[10301]: すみません。
    jump ch6_s1443

label ch6_s1442:
    # Source scene 1442
    voice "ch6_s_077"
    s "It is dangerous when you lose your way.{#ch6_s_077}"
    # JA[10302]: 道に迷うと大変ですよ。
    voice "ch6_h_053"
    h "…Yes. My path… Where in the world is it…?{#ch6_h_053}"
    # JA[498]: ……そうですね。 わたくしの道……。 一体どこにあるのかしら……。
    voice "ch6_s_078"
    s "Well, if you let your guard down because it looks like a straight road, it turns out the paths are actually pretty tangled.{#ch6_s_078}"
    # JA[10303]: いや、一本道だと思って油断してると、 けっこう道が複雑に絡み合ってるらしくて。
    voice "ch6_h_054"
    h "Oh my, that sounds difficult.{#ch6_h_054}"
    # JA[499]: まあ、それは大変ですね。
    voice "ch6_s_079"
    s "Even when you think you are doing fine, from the outside it can look like nothing but reckless behavior.{#ch6_s_079}"
    # JA[10304]: 自分は大丈夫なつもりでも、はたから見れば ただの無茶ってこともよくある話ですよ。
    voice "ch6_h_055"
    h "That is a very literal way to get lost.{#ch6_h_055}"
    # JA[500]: それは、本当に道に迷う話ですね。
    voice "ch6_s_080"
    s "Huh? Did you mean something else?{#ch6_s_080}"
    # JA[10305]: え？ 他になにか？
    voice "ch6_h_056"
    h "It was nothing.{#ch6_h_056}"
    # JA[501]: 何でもありませんわ。
    jump ch6_s1443

label ch6_s1443:
    # Source scene 1443
    voice "ch6_s_081"
    s "Come on, let's head back into the city.{#ch6_s_081}"
    # JA[10306]: さあ、街の中に戻りましょう。
    voice "ch6_h_057"
    h "Yes, let us.{#ch6_h_057}"
    # JA[502]: ええ、そうですね。

label ch6_s1444:
    # Source scene 1444
    voice "ch6_h_058"
    h "This is the market, isn't it? It is so lively and bustling. They sell all sorts of things here.{#ch6_h_058}"
    # JA[503]: ここは市場ですね。 とても活気に溢れてて、賑やか。 さまざまな物が売られているのですね。
    voice "ch6_s_082"
    s "I think that shows how peaceful this city is.{#ch6_s_082}"
    # JA[10308]: それだけ、この街が平和ってことだと 思いますよ。
    voice "ch6_h_059"
    h "Peaceful… Do you really think so?{#ch6_h_059}"
    # JA[504]: 平和……。 そうなのでしょうか。
    voice "ch6_s_083"
    s "Princess?{#ch6_s_083}"
    # JA[10309]: お姫さま？
    voice "ch6_h_060"
    h "I can be here like this now, but… if you and Louise had not been there in the last battle…{#ch6_h_060}"
    # JA[505]: 今は、こうしていられますけど……。 先の戦いで、もしもルイズと使い魔さんが いなければ……。
    voice "ch6_h_061"
    h "The scene would surely have been very different. This peaceful sight exists only because a series of coincidences came together.{#ch6_h_061}"
    # JA[506]: きっともっと違った風景になっていたはずです。 今この平和な光景があるのも、 偶然が重なった結果にすぎないのですわ。
    voice "ch6_s_084"
    s "Princess…{#ch6_s_084}"
    # JA[10310]: お姫さま……。
    menu:
        "Even if it was coincidence, isn't it enough that the outcome was good?":
            jump ch6_s1445
            # JA: 偶然だって結果が良ければＯＫ
        "Our efforts were not a coincidence":
            jump ch6_s1446
            # JA: 俺達の努力は偶然じゃない
        "It will be all right next time":
            jump ch6_s1447
            # JA: 今度は大丈夫

label ch6_s1445:
    # Source scene 1445
    voice "ch6_s_085"
    s "Even if it was coincidence, isn't it enough that the outcome was good?{#ch6_s_085}"
    # JA[10311]: 偶然だって、結果が良ければ いいじゃないですか。
    voice "ch6_h_062"
    h "Yes, I suppose so. The people were saved, so we certainly ought to rejoice in that first.{#ch6_h_062}"
    # JA[507]: そうですね。 民が救われたのですから、 それをまず喜ぶべきなのは確かです。
    voice "ch6_s_086"
    s "Exactly. Let's just be happy about it. Yay.{#ch6_s_086}"
    # JA[10312]: そうですよ。 素直に喜びましょ。 わーい。
    voice "ch6_h_063"
    h "Hee hee. Yes, let us.{#ch6_h_063}"
    # JA[508]: くすっ。 そうですね。 うふふ。
    jump ch6_s1448

label ch6_s1446:
    # Source scene 1446
    voice "ch6_s_087"
    s "Our efforts were not a coincidence.{#ch6_s_087}"
    # JA[10313]: 俺達の努力は偶然じゃありませんよ。
    voice "ch6_h_064"
    h "Oh, I am sorry. That is not what I meant.{#ch6_h_064}"
    # JA[509]: あ、すみません。 そういう意味で言ったのではないのです。
    voice "ch6_h_065"
    h "It is just that, when we fell into that crisis, you and Louise happened to be in this country… That itself seemed like a coincidence to me…{#ch6_h_065}"
    # JA[510]: ただ、あの危機に陥った時に、 ルイズと使い魔さんがこの国にいてくれた……。 そのこと自体が偶然のように思えて……。
    voice "ch6_s_088"
    s "True… That may have been coincidence. I was summoned by Louise by coincidence, too.{#ch6_s_088}"
    # JA[10314]: 確かに……。 それは偶然かもしれないですね 俺もルイズに偶然召喚されたんだし。
    voice "ch6_s_089"
    s "But because Louise, the soldiers… and above all, you, Princess, worked so hard, we were able to make use of that coincidence.{#ch6_s_089}"
    # JA[10315]: でも、ルイズや軍人さんや……。 何よりお姫さまが頑張ったから、 その偶然も活かせたんですよ。
    voice "ch6_h_066"
    h "Do you think so…? Unlike the others, I…{#ch6_h_066}"
    # JA[511]: そうでしょうか……。 他の者はともかく、わたくしは……。
    voice "ch6_s_090"
    s "Please don't say that. You worked hard, Princess. Everyone knows it.{#ch6_s_090}"
    # JA[10316]: そんな風に言わないでくださいよ。 お姫さまは頑張った。 それはみんなが分かってますよ。
    voice "ch6_h_067"
    h "I… hope that is true.{#ch6_h_067}"
    # JA[512]: だと……いいのですが。
    jump ch6_s1448

label ch6_s1447:
    # Source scene 1447
    voice "ch6_s_091"
    s "I do not know what the princess regrets, but it will be all right next time.{#ch6_s_091}"
    # JA[10317]: お姫さまが、なにを後悔してるか 分かりませんけど、次は大丈夫ですよ。
    voice "ch6_h_068"
    h "Next time…?{#ch6_h_068}"
    # JA[513]: 次……ですか？
    voice "ch6_s_092"
    s "Yes. If you have regrets, you can use what you learned from them next time.{#ch6_s_092}"
    # JA[10318]: そうです。 もし、悔いが残ってるなら、 その反省を次に活かせばいいんですよ。
    voice "ch6_h_069"
    h "Yes. Next time, I will protect the capital myself.{#ch6_h_069}"
    # JA[514]: そうですね。 今度は、わたくしが都を守ってみせましょう。
    voice "ch6_s_093"
    s "That's the spirit.{#ch6_s_093}"
    # JA[10319]: そうそう、その意気です。
    jump ch6_s1448

label ch6_s1448:
    # Source scene 1448
    voice "ch6_s_094"
    s "We should move on. If we keep standing here, we will only block the way.{#ch6_s_094}"
    # JA[10320]: さて、あんまりここに突っ立ってると、 通行の邪魔かな。
    voice "ch6_h_070"
    h "Then let us go somewhere else as well.{#ch6_h_070}"
    # JA[515]: それでは、他の所にも行ってみましょう。
    jump ch6_2  # return to the continuation after route extras
