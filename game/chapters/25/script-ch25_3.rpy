# Глава 25, часть 3 (933 + extra 1214–1218): секрет письма, звёзды.
# Источник: ps2_source/chapters/chapter_26_手紙の秘密.txt (SCENE 933, 1214-1218).

label ch25_3:
    $ tndl(None)
    $ show_sprites()

label ch25_3_scene_933:

    # [BG       stage    image=+45, level=200]
    $ fade_fx("id(45)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：サイト。
    voice "ch25_l_043"
    l "Saito. You certainly had your fun today, didn't you?{#ch25_l_043}"

    # サイト：なんで不機嫌になってるんだよ？
    voice "ch25_s_114"
    s "Why are you sulking? Right, Siesta?{#ch25_s_114}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+506, level=160, dir=1B]
    # シエスタ：知りません……。  [voice 15041]
    voice "ch25_si_008"
    si "I don't know…{#ch25_si_008}"

    # サイト：えっ、シエスタまで？  [voice 12495]
    voice "ch25_s_115"
    s "Eh? Even you, Siesta?{#ch25_s_115}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay7     image=+968, level=160, dir=1B]
    # ハルナ：今日の平賀くんって、最低……。  [voice 2436]
    voice "ch25_ha_008"
    ha "Hiraga-kun today was the worst…{#ch25_ha_008}"

    # [SPRITE   lay7     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：だから、なんで春奈まで不機嫌なんだよ？  [voice 12496]
    voice "ch25_s_116"
    s "So why are you sulking too, Haruna?{#ch25_s_116}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：大丈夫。
    voice "ch25_k_026"
    k "It's fine. I'm not in a bad mood, darling.{#ch25_k_026}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：キュルケ！  [voice 12497]
    voice "ch25_s_117"
    s "Kirche!{#ch25_s_117}"

    # [SPRITE   lay6     image=+684, level=160, dir=1A]
    # キュルケ：だって、好きな男がモテてるのを見てると、
    voice "ch25_k_027"
    k "Well, when you watch the man you like being popular, it makes you proud—or makes you burn with jealousy.{#ch25_k_027}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：んー？
    voice "ch25_s_118"
    s "Hmm? Am I really that popular, according to you?{#ch25_s_118}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+307, level=140, dir=1A]
    # ルイズ：……なっ！？  [voice 6810]
    voice "ch25_l_044"
    l "…!?{#ch25_l_044}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+505, level=140, dir=1B]
    # シエスタ：あのですね……。  [voice 15042]
    voice "ch25_si_009"
    si "You see…{#ch25_si_009}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay7     image=+967, level=140, dir=1B]
    # ハルナ：……平賀くん。  [voice 2437]
    voice "ch25_ha_009"
    ha "…Hiraga-kun.{#ch25_ha_009}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：……い、いや。
    voice "ch25_s_119"
    s "…N-No. More importantly, let's eat, eat…{#ch25_s_119}"

    # サイト：そういや、タバサはさっきから静かだけど……。  [voice 12500]
    voice "ch25_s_120"
    s "Come to think of it, Tabitha's been quiet for a while, too…{#ch25_s_120}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # [EVENT_CG event    image=+246, level=80]
    $ dissolve_fx("id(246)")
    # [TRANS trans("crossfade", 1000)]
    # タバサ：……。
    t "…{#ch25_t_053}"

    # ハルナ：あっ、タバサさん、寝ちゃってます……。  [voice 2438]
    voice "ch25_ha_010"
    ha "Ah, Tabitha-san has fallen asleep…{#ch25_ha_010}"

    # キュルケ：ウフフ、食事中に寝ちゃうだなんて……。
    voice "ch25_k_028"
    k "Heh heh, falling asleep during a meal… She must have been quite nervous today, too.{#ch25_k_028}"

    # タバサ：……ん。  [voice 15685]
    voice "ch25_t_054"
    t "…Mm.{#ch25_t_054}"

    # シエスタ：くすっ。
    voice "ch25_si_010"
    si "Heh. Miss Zerbst is like Miss Tabitha's older sister, isn't she?{#ch25_si_010}"

    # キュルケ：まぁね。
    voice "ch25_k_029"
    k "Well, we've known each other a long time.{#ch25_k_029}"

    # キュルケ：でも、こんなところで寝ていたら、
    voice "ch25_k_030"
    k "Still, sleeping here will give her a cold. I'll take her to the inn once.{#ch25_k_030}"

    # サイト：ああ、頼むよ。  [voice 12501]
    voice "ch25_s_121"
    s "Ah, please do.{#ch25_s_121}"

    # キュルケ：ほら、タバサ、宿まで帰るわよ。
    voice "ch25_k_031"
    k "Come on, Tabitha. Let's go back to the inn. Wake up.{#ch25_k_031}"

    # タバサ：……。
    t "…{#ch25_t_055}"

    # キュルケ：それじゃあね。  [voice 3480]
    voice "ch25_k_032"
    k "See you then.{#ch25_k_032}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+89, level=200]
    $ fade_fx("id(89)")
    # [TRANS trans("crossfade", 1000)]
    # null：………。
    th "… … …{#ch25_th_006}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BG       stage    hide]
    # [BG       stage    image=+45, level=200]
    $ fade_fx("id(45)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+31]
    play music t30 fadein 1.0
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay7     image=+962, level=160, dir=1B]
    # ハルナ：あれ？
    voice "ch25_ha_011"
    ha "Oh? It looks like Tabitha-san dropped something.{#ch25_ha_011}"

    # ルイズ：あの手紙じゃない。  [voice 6811]
    voice "ch25_l_045"
    l "That letter, I bet.{#ch25_l_045}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ふう、タバサ、よっぽど疲れたみたい。
    voice "ch25_k_033"
    k "Phew, Tabitha must be exhausted. She's sleeping soundly. Wait—what's with all of you?{#ch25_k_033}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：こ、これ、タバサの手紙……だよな？  [voice 12502]
    voice "ch25_s_122"
    s "T-This is Tabitha's letter… right?{#ch25_s_122}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：あら、落としちゃったの？
    voice "ch25_k_034"
    k "Oh, she dropped it? What a careless girl.{#ch25_k_034}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+506, level=160, dir=1B]
    # シエスタ：ど、どうしましょう？
    voice "ch25_si_011"
    si "W-What should we do? Maybe we should return it right away…{#ch25_si_011}"

    # キュルケ：見ちゃう？  [voice 3483]
    voice "ch25_k_035"
    k "Shall we take a look?{#ch25_k_035}"

    # [SPRITE   lay2     image=+504, level=160, dir=1B]
    # シエスタ：ええ！？  [voice 15045]
    voice "ch25_si_012"
    si "Eh!?{#ch25_si_012}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：タバサって、絶対に自分から人に頼ろうと
    voice "ch25_k_036"
    k "Tabitha never asks anyone for help, does she? So we have to help her, right?{#ch25_k_036}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：だから、黙って手紙を見るの？  [voice 6812]
    voice "ch25_l_046"
    l "So you want to look at the letter without telling her?{#ch25_l_046}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：あら、いや？
    voice "ch25_k_037"
    k "Oh, not interested? Then I'll take a peek by myself.{#ch25_k_037}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：しょうがないな。
    voice "ch25_s_123"
    s "Fine. We'll all apologize later for reading it without permission. Let's look.{#ch25_s_123}"

    # キュルケ：さすが、ダーリン。
    voice "ch25_k_038"
    k "As expected of darling. So understanding. Then I'll read it on everyone's behalf.{#ch25_k_038}"

    # [SE       se0      play=+72]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ふんふん……。  [voice 3487]
    voice "ch25_k_039"
    k "Hmm hmm…{#ch25_k_039}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：……。
    k "…{#ch25_k_040}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+28]
    play music t27 fadein 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：どうしたの、キュルケ？  [voice 6813]
    voice "ch25_l_047"
    l "What's wrong, Kirche?{#ch25_l_047}"

    # キュルケ：たぶん、任務絡みのことだろうから、
    voice "ch25_k_041"
    k "I figured it was something to do with a mission, and therefore serious… but…{#ch25_k_041}"

    # ルイズ：任務？
    voice "ch25_l_048"
    l "A mission? You thought?{#ch25_l_048}"

    # キュルケ：これは面倒なことになりそうね。  [voice 3489]
    voice "ch25_k_042"
    k "This is going to be troublesome.{#ch25_k_042}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：だから、なんなのよ？  [voice 6815]
    voice "ch25_l_049"
    l "So, what is it!?{#ch25_l_049}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：タバサはガリア王国の出身だってこと知ってる？  [voice 3490]
    voice "ch25_k_043"
    k "Do you know Tabitha's from the Kingdom of Gallia?{#ch25_k_043}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：それは知ってるけど……。  [voice 6816]
    voice "ch25_l_050"
    l "I know that much, but…{#ch25_l_050}"

    # キュルケ：まぁ、詳しいことは省略するけど、
    voice "ch25_k_044"
    k "Well, I'll skip the details. Tabitha gets missions from Gallia from time to time.{#ch25_k_044}"

    # キュルケ：今回も、そのガリア王国からの任務なんだけど、
    voice "ch25_k_045"
    k "This one is from Gallia, too—'capture a certain person and bring them to Gallia'—{#ch25_k_045}"

    # キュルケ：それが今回の任務みたい。  [voice 3493]
    voice "ch25_k_046"
    k "…that seems to be the mission.{#ch25_k_046}"

    # ルイズ：まぁ、たしかに楽な任務じゃなさそうね。  [voice 6817]
    voice "ch25_l_051"
    l "Well, it certainly doesn't sound like an easy one.{#ch25_l_051}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：それは捕まえる相手次第だろ？  [voice 12504]
    voice "ch25_s_124"
    s "That depends on who they want captured, doesn't it?{#ch25_s_124}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：簡単に捕まる相手もいるわよね。
    voice "ch25_l_052"
    l "There are people who are easy to catch, you know. If you prepared a girl with a big chest, a dog would come wagging its tail right away.{#ch25_l_052}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ご、ご主人様。
    voice "ch25_s_125"
    s "M-Mistress… I sense something hurtful in that…{#ch25_s_125}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：そう？
    voice "ch25_l_053"
    l "Really? Maybe you're imagining it?{#ch25_l_053}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：しくしく。  [voice 12506]
    voice "ch25_s_126"
    s "Sniff…{#ch25_s_126}"

    # ルイズ：それで、捕まえる相手って誰なの？  [voice 6820]
    voice "ch25_l_054"
    l "So, who is the person to be captured?{#ch25_l_054}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：ハルナ、あなたよ。  [voice 3494]
    voice "ch25_k_047"
    k "Haruna. It's you.{#ch25_k_047}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     hide]
    # [SPRITE   lay7     image=+967, level=140, dir=1B]
    # ハルナ：えっ？  [voice 2440]
    voice "ch25_ha_012"
    ha "Eh?{#ch25_ha_012}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay1     image=+307, level=140, dir=1A]
    # ルイズ：ウソ？  [voice 6821]
    voice "ch25_l_055"
    l "No way?{#ch25_l_055}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay2     image=+505, level=140, dir=1B]
    # シエスタ：そんな……。  [voice 15046]
    voice "ch25_si_013"
    si "That's…{#ch25_si_013}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay2     image=+504, level=160, dir=1B]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：マジかよ？  [voice 12507]
    voice "ch25_s_127"
    s "Seriously?{#ch25_s_127}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay7     image=+968, level=160, dir=1B]
    # ハルナ：……。  [voice 2441]
    voice "ch25_ha_013"
    ha "…{#ch25_ha_013}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ねぇ、ハルナ。
    voice "ch25_l_056"
    l "Say, Haruna. Did you do something that Tabitha would need to bring you in for?{#ch25_l_056}"

    # ハルナ：し、知らない。
    voice "ch25_ha_014"
    ha "I… don't know. Why would I…{#ch25_ha_014}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：でも、タバサが混乱した気持ちも分かるぜ。
    voice "ch25_s_128"
    s "But I understand how confused Tabitha must feel. To be told something like that suddenly…{#ch25_s_128}"

    # サイト：（今日、一緒に街を歩いたのって、
    s "(Walking through town together today was—an escape from reality, I suppose…){#ch25_s_129}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay2     image=+506, level=160, dir=1B]
    # シエスタ：そうですね……。
    voice "ch25_si_014"
    si "Yes… It's not something we could ask others about, is it…?{#ch25_si_014}"

    # ハルナ：私、どうなるんだろう……。  [voice 2443]
    voice "ch25_ha_015"
    ha "What will become of me…{#ch25_ha_015}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：……。  [voice 12509]
    voice "ch25_s_130"
    s "…{#ch25_s_130}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：んー、とりあえず……。  [voice 3495]
    voice "ch25_k_048"
    k "Hmm. For now…{#ch25_k_048}"

    # サイト：とりあえず？  [voice 12510]
    voice "ch25_s_131"
    s "For now what?{#ch25_s_131}"

    # キュルケ：あたしは手紙なんて読んでないし、
    voice "ch25_k_049"
    k "I didn't read the letter, and none of you heard anything. Right?{#ch25_k_049}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：そ、そうだな。
    voice "ch25_s_132"
    s "R-Right. We didn't read it, and we didn't hear anything. That's how it is, right?{#ch25_s_132}"

    # サイト：春奈も不安だろうけど、
    voice "ch25_s_133"
    s "Haruna must be worried, too. Don't worry too much, okay?{#ch25_s_133}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+968, level=160, dir=1B]
    # ハルナ：でも……。  [voice 2444]
    voice "ch25_ha_016"
    ha "But…{#ch25_ha_016}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：大丈夫だって。
    voice "ch25_s_134"
    s "It'll be fine. No matter that it's a mission—Tabitha would never capture Haruna, would she?{#ch25_s_134}"

    # ハルナ：う、うん……。  [voice 2445]
    voice "ch25_ha_017"
    ha "M-Mm…{#ch25_ha_017}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：……。
    k "…{#ch25_k_050}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+89, level=200]
    $ fade_fx("id(89)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：（と言ったものの……。
    s "(Even as I said it… What on earth is going on? Why would Gallia want Haruna…?){#ch25_s_135}"

    # サイト：（きっとタバサも、相当悩んじゃってるん
    s "(Tabitha must be worrying a lot, too… I want to help somehow…){#ch25_s_136}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
label ch25_3_scene_1214:

    # [BG       stage    image=+87, level=200]
    $ fade_fx("id(87)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：やれやれ、なんだかやっかいなことに
    voice "ch25_s_137"
    s "Good grief. We've gotten ourselves into something complicated…{#ch25_s_137}"

    # サイト：あれは……タバサか。  [voice 8992]
    voice "ch25_s_138"
    s "That's… Tabitha, is it?{#ch25_s_138}"

    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch25_t_056}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：タバサ、起きたのか……。
    voice "ch25_s_139"
    s "Tabitha, are you awake? You fell asleep during the meal, so I got a scare.{#ch25_s_139}"

    # タバサ：……。
    t "…{#ch25_t_057}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：実は疲れてたんだってな。
    voice "ch25_s_140"
    s "They say you were tired. Sorry I couldn't notice sooner…{#ch25_s_140}"

    # [LAYER    lay0     image=+596, level=160, dir=1A]
    # タバサ：……。
    t "…{#ch25_t_058}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：で、何してたんだ？
    voice "ch25_s_141"
    s "So, what were you doing? Watching the night sky, perhaps?{#ch25_s_141}"

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：うん。  [voice 15366]
    voice "ch25_t_059"
    t "Mm.{#ch25_t_059}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+244, level=80]
    $ dissolve_fx("id(244)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：前々から気になってたんだけど……。
    voice "ch25_s_142"
    s "I've been curious for a while… Does this world have constellations, too?{#ch25_s_142}"

    # タバサ：星座？  [voice 15367]
    voice "ch25_t_060"
    t "Constellations?{#ch25_t_060}"

    # サイト：星座っていうのは……。
    voice "ch25_s_143"
    s "Constellations are—you connect bright stars with lines and make them into people, animals, objects and so on.{#ch25_s_143}"

    # タバサ：線で結ぶ……。
    voice "ch25_t_061"
    t "Connect with lines… Shapes…{#ch25_t_061}"

    # タバサ：駄目、形にならない。  [voice 15369]
    voice "ch25_t_062"
    t "No good. It doesn't make a shape.{#ch25_t_062}"

    # サイト：本当の図形じゃないよ。
    voice "ch25_s_144"
    s "It's not about real shapes. You draw two lines and go 'a puppy!'—or a diamond and go 'a crow!'—that sort of thing.{#ch25_s_144}"

    # タバサ：……変なの。
    voice "ch25_t_063"
    t "…Weird. What are constellations for?{#ch25_t_063}"

    # サイト：なんのためって……。
    voice "ch25_s_145"
    s "What for… Well, let me see…{#ch25_s_145}"

    menu:
        "As landmarks for travel{#ch25_3_c_1214_1}":
            jump ch25_3_scene_1215
        "For fortune-telling{#ch25_3_c_1214_2}":
            jump ch25_3_scene_1216
        "To tell the time{#ch25_3_c_1214_3}":
            jump ch25_3_scene_1217

label ch25_3_scene_1215:

    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # [EVENT_CG event    image=+244, level=80]
    $ dissolve_fx("id(244)")
    # サイト：旅の目印に使ってたのかな。  [voice 9000]
    voice "ch25_s_146"
    s "Maybe they used them as landmarks while traveling.{#ch25_s_146}"

    # タバサ：目印？  [voice 15371]
    voice "ch25_t_064"
    t "Landmarks?{#ch25_t_064}"

    # サイト：そう、目印。
    voice "ch25_s_147"
    s "Yes, landmarks. Constellations are visible or not depending on where you are.{#ch25_s_147}"

    # サイト：それで、特定の星座が見えるか見えないで、
    voice "ch25_s_148"
    s "So if a particular constellation was visible or not, they could use it to work out where they were.{#ch25_s_148}"

    # タバサ：興味深い。  [voice 15372]
    voice "ch25_t_065"
    t "Interesting.{#ch25_t_065}"

    # → next scene 1218
    jump ch25_3_scene_1218

label ch25_3_scene_1216:

    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # [EVENT_CG event    image=+244, level=80]
    $ dissolve_fx("id(244)")
    # サイト：占いに使われてるね。  [voice 9003]
    voice "ch25_s_149"
    s "They're used for fortune-telling.{#ch25_s_149}"

    # タバサ：占い？  [voice 15373]
    voice "ch25_t_066"
    t "Fortune-telling?{#ch25_t_066}"

    # [SPRITE   lay5     hide]
    # サイト：俺はその理屈はよく分からないんだけど、
    voice "ch25_s_150"
    s "I don't really get how it works, but the stars move—so they tell fortunes from their movements, I think.{#ch25_s_150}"

    # タバサ：星で何を占うの？  [voice 15374]
    voice "ch25_t_067"
    t "What do they tell with stars?{#ch25_t_067}"

    # サイト：そりゃもう色々なこと。
    voice "ch25_s_151"
    s "All sorts of things. Love, work—anything about life, really.{#ch25_s_151}"

    # タバサ：頼りすぎ。  [voice 15375]
    voice "ch25_t_068"
    t "Too much reliance.{#ch25_t_068}"

    # サイト：はは、そうかもな。  [voice 9006]
    voice "ch25_s_152"
    s "Ha ha, maybe so.{#ch25_s_152}"

    # → next scene 1218
    jump ch25_3_scene_1218

label ch25_3_scene_1217:

    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # [EVENT_CG event    image=+244, level=80]
    $ dissolve_fx("id(244)")
    # サイト：時刻とか見たり。  [voice 9007]
    voice "ch25_s_153"
    s "To tell the time, and such.{#ch25_s_153}"

    # タバサ：時刻？  [voice 15376]
    voice "ch25_t_069"
    t "The time?{#ch25_t_069}"

    # サイト：特定の星座の位置でなんとなく分かるんだ。
    voice "ch25_s_154"
    s "You can more or less tell from the position of a particular constellation. The season, too, probably.{#ch25_s_154}"

    # タバサ：季節？  [voice 15377]
    voice "ch25_t_070"
    t "The season?{#ch25_t_070}"

    # サイト：こっちじゃどうか知らないけれど、
    voice "ch25_s_155"
    s "I don't know about here, but where I come from, the visible constellations change with the season.{#ch25_s_155}"

    # タバサ：不思議。  [voice 15378]
    voice "ch25_t_071"
    t "Strange.{#ch25_t_071}"

    # → next scene 1218
    jump ch25_3_scene_1218

label ch25_3_scene_1218:

    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # [EVENT_CG event    image=+244, level=80]
    $ dissolve_fx("id(244)")
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+87, level=200]
    $ fade_fx("id(87)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：それにしても……。  [voice 9010]
    voice "ch25_s_156"
    s "That aside…{#ch25_s_156}"

    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：うん。  [voice 15379]
    voice "ch25_t_072"
    t "Mm.{#ch25_t_072}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：見上げて全く馴染みのない夜空ってだけで、
    voice "ch25_s_157"
    s "Just looking up at a night sky I don't recognize at all tells me this isn't my world…{#ch25_s_157}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：まあ、二つの月を見れば一目瞭然だったり
    voice "ch25_s_158"
    s "Though two moons would give it away at a glance, too.{#ch25_s_158}"

    # [LAYER    lay0     image=+594, level=160, dir=1A]
    # タバサ：さびしいの？  [voice 15380]
    voice "ch25_t_073"
    t "Are you lonely?{#ch25_t_073}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：えっ？
    voice "ch25_s_159"
    s "Eh? N-No, I… That's not it…{#ch25_s_159}"

    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # タバサ：そう。  [voice 15381]
    voice "ch25_t_074"
    t "I see.{#ch25_t_074}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：はは、ははは……。  [voice 9014]
    voice "ch25_s_160"
    s "Ha ha, ha ha ha…{#ch25_s_160}"

    # サイト：（ひょっとして、今のは俺をなぐさめて
    s "(Maybe she was trying to comfort me just now?){#ch25_s_161}"

    # タバサ：今度また……。  [voice 15382]
    voice "ch25_t_075"
    t "Next time…{#ch25_t_075}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：う、うん？  [voice 9015]
    voice "ch25_s_162"
    s "U-Uh?{#ch25_s_162}"

    # [LAYER    lay0     image=+596, level=160, dir=1A]
    # タバサ：お話聞かせて。  [voice 15383]
    voice "ch25_t_076"
    t "Tell me more stories.{#ch25_t_076}"

    # サイト：ああいいよ。
    voice "ch25_s_163"
    s "Ah, sure. If you want my stories, I can tell you as many as you like.{#ch25_s_163}"

    # タバサ：うん。  [voice 15384]
    voice "ch25_t_077"
    t "Mm.{#ch25_t_077}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [COFFEE]
    $ pause(1.0)
    # → next scene 934
    jump ch26

    # ==== КОНЕЦ ЧАСТИ 3 ====
    jump ch25_4
    return

