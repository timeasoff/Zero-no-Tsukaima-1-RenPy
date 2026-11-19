# Глава 22, часть 5 (extra 1209–1213): чай с Сиэстой на кухне.
# Источник: ps2_source/chapters/chapter_23_料理の鉄人.txt (extra SCENE 1209-1213).

label ch22_5:
    $ tndl(None)
    $ show_sprites(None)

label ch22_5_scene_1209:

    # [BG       stage    image=+28, level=200]
    $ fade_fx("id(28)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [SPRITE   lay19    image=+940, level=160, dir=1A]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # デルフリンガー：相棒、ずいぶん寂しい表情してるじゃねーか。  [voice 1218]
    voice "ch22_d_001"
    d "Partner, you're looking pretty lonely there, aren't you?{#ch22_d_001}"

    # サイト：あ、分かる？  [voice 8965]
    voice "ch22_s_171"
    s "Ah, you can tell?{#ch22_s_171}"

    # デルフリンガー：相棒って、すぐ顔に出るからなぁ。  [voice 1219]
    voice "ch22_d_002"
    d "You always wear your heart on your face, partner.{#ch22_d_002}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：ちょっと寂しいよなぁって思って。
    voice "ch22_s_172"
    s "I was just thinking—it's a little lonely. Starting tomorrow, when I go back to my room, Siesta's smile won't be there anymore…{#ch22_s_172}"

    # [SPRITE   lay19    hide]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：誰の笑顔ですか？  [voice 14330]
    voice "ch22_si_088"
    si "Whose smile?{#ch22_si_088}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：どわあああ！  [voice 8967]
    voice "ch22_s_173"
    s "Whoaah!{#ch22_s_173}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：こんばんは、サイトさん。
    voice "ch22_si_089"
    si "Good evening, Saito-san. What's wrong? Out so late…{#ch22_si_089}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：い、いやちょっと風に当たってみよう
    voice "ch22_s_174"
    s "N-No, I just thought I'd get some air. And you, Siesta?{#ch22_s_174}"

    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：今、マルトーさんの所にごあいさつに行って
    voice "ch22_si_090"
    si "I just went to greet Marto-san. Starting tomorrow, I get to work in the dining hall!{#ch22_si_090}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：これも、全部サイトさんのおかげです。  [voice 14333]
    voice "ch22_si_091"
    si "That's all thanks to you, Saito-san, too.{#ch22_si_091}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：いや、俺のおかげって言われると、
    voice "ch22_s_175"
    s "No, being told it's thanks to me makes me itch a bit… Still, I'm glad it worked out.{#ch22_s_175}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：はいっ。
    voice "ch22_si_092"
    si "Yes. From tomorrow I'll always be in the dining hall, so please come see me.{#ch22_si_092}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：うん、分かった。
    voice "ch22_s_176"
    s "Yeah, I got it. At noon, I'll definitely come to see you.{#ch22_s_176}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：はい、お待ちしていますね。  [voice 14335]
    voice "ch22_si_093"
    si "Yes, I'll be waiting.{#ch22_si_093}"

    # サイト：ところで、シエスタはもう帰るのかい？  [voice 8971]
    voice "ch22_s_177"
    s "By the way, Siesta, are you heading home already?{#ch22_s_177}"

    # シエスタ：いえ、明日の準備もありますし、
    voice "ch22_si_094"
    si "No. I have to prepare for tomorrow, so I'm going to clean the kitchen.{#ch22_si_094}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：うん？  [voice 8972]
    voice "ch22_s_178"
    s "Hmm?{#ch22_s_178}"

    # [SPRITE   lay2     image=+522, level=160, dir=2A]
    # シエスタ：あの、よろしければ厨房でお茶でもどうですか？  [voice 14337]
    voice "ch22_si_095"
    si "Um… If it's all right, would you like some tea in the kitchen?{#ch22_si_095}"

    # サイト：（ど、どうしよう？）
    s "(W-What should I do?){#ch22_s_179}"

    menu:
        "Yeah, I'll go{#ch22_5_c_1209_1}":
            jump ch22_5_scene_1210
        "No, I won't{#ch22_5_c_1209_2}":
            jump ch22_5_scene_1211
        "Hmm, not sure{#ch22_5_c_1209_3}":
            jump ch22_5_scene_1212

label ch22_5_scene_1210:

    # [SPRITE   lay2     image=+522, level=160, dir=2A]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [BG       stage    image=+28, level=200]
    $ fade_fx("id(28)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：うん、行くよ。  [voice 8973]
    voice "ch22_s_180"
    s "Yeah, I'll go.{#ch22_s_180}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：そうですか！
    voice "ch22_si_096"
    si "Is that so! Thank you very much.{#ch22_si_096}"

    # → next scene 1213
    jump ch22_5_scene_1213

label ch22_5_scene_1211:

    # [SPRITE   lay2     image=+522, level=160, dir=2A]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [BG       stage    image=+28, level=200]
    $ fade_fx("id(28)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：いや、行かない。  [voice 8974]
    voice "ch22_s_181"
    s "No, I won't.{#ch22_s_181}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：サイトさん、お忙しいんですか？  [voice 14339]
    voice "ch22_si_097"
    si "Are you busy, Saito-san?{#ch22_si_097}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：いや、そんなことはないけど……。  [voice 8975]
    voice "ch22_s_182"
    s "No, that's not it, but…{#ch22_s_182}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：でしたら！  [voice 14340]
    voice "ch22_si_098"
    si "Then!{#ch22_si_098}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：わ、分かったよ。
    voice "ch22_s_183"
    s "O-Okay, I get it. Don't make that sad face. I'll go.{#ch22_s_183}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：そうですか！
    voice "ch22_si_099"
    si "Is that so! Thank you very much.{#ch22_si_099}"

    # → next scene 1213
    jump ch22_5_scene_1213

label ch22_5_scene_1212:

    # [SPRITE   lay2     image=+522, level=160, dir=2A]
    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [BG       stage    image=+28, level=200]
    $ fade_fx("id(28)")
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：うーん、どうしようかなぁ？  [voice 8977]
    voice "ch22_s_184"
    s "Umm, what should I do…?{#ch22_s_184}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：サイトさん、お忙しいんですか？  [voice 14342]
    voice "ch22_si_100"
    si "Are you busy, Saito-san?{#ch22_si_100}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：いや、そんなことはないけど……。  [voice 8978]
    voice "ch22_s_185"
    s "No, that's not it, but…{#ch22_s_185}"

    # [SPRITE   lay2     image=+495, level=160, dir=1A]
    # シエスタ：でしたら！  [voice 14343]
    voice "ch22_si_101"
    si "Then!{#ch22_si_101}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：わ、分かったよ。
    voice "ch22_s_186"
    s "O-Okay, I get it. Don't make that sad face. I'll go.{#ch22_s_186}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：そうですか！
    voice "ch22_si_102"
    si "Is that so! Thank you very much.{#ch22_si_102}"

    # → next scene 1213
    jump ch22_5_scene_1213

label ch22_5_scene_1213:

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # [BGM      bgm      play=+13]
    play music t12 fadein 1.0
    # [BG       stage    image=+28, level=200]
    $ fade_fx("id(28)")
    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # null：………。
    th "… … …{#ch22_th_001}"

    # [BG       stage    image=+34, level=200]
    $ fade_fx("id(34)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：はい、どうぞ。
    voice "ch22_si_103"
    si "Yes, here you are. It's hot, so please drink carefully, okay?{#ch22_si_103}"

    # [SPRITE   lay2     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：ありがとう。
    voice "ch22_s_187"
    s "Thanks. Huh? Aren't you drinking, Siesta?{#ch22_s_187}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：わたしは、掃除が残っていますから……。  [voice 14346]
    voice "ch22_si_104"
    si "I still have cleaning left to do…{#ch22_si_104}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：それなら俺も手伝うよ。
    voice "ch22_s_188"
    s "Then I'll help you. Won't that be faster?{#ch22_s_188}"

    # [SPRITE   lay2     image=+491, level=160, dir=1A]
    # シエスタ：いえ、サイトさんはゆっくりしててください。
    voice "ch22_si_105"
    si "No, Saito-san, please relax. All that's left is wiping down the shelf in the back.{#ch22_si_105}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：でも、そうなると俺もゆっくりできないし、
    voice "ch22_s_189"
    s "But if you do that, I can't relax either. Please, Siesta, have some tea with me, won't you?{#ch22_s_189}"

    # [SPRITE   lay2     image=+522, level=160, dir=2A]
    # シエスタ：……うーん。
    voice "ch22_si_106"
    si "…Mm. If Saito-san insists, I'll be indulgent and have some tea.{#ch22_si_106}"

    # [SPRITE   lay2     image=+489, level=160, dir=1A]
    # シエスタ：あ、もちろん。
    voice "ch22_si_107"
    si "Ah, of course. I'll clean properly once I'm done.{#ch22_si_107}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+221, level=80]
    $ dissolve_fx("id(221)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：シエスタって、なんかすごく家庭的だよね？  [voice 8983]
    voice "ch22_s_190"
    s "You're so domestic, Siesta, aren't you?{#ch22_s_190}"

    # シエスタ：そうでしょうか？  [voice 14350]
    voice "ch22_si_108"
    si "Is that so?{#ch22_si_108}"

    # サイト：だって、炊事、洗濯、掃除だろ？
    voice "ch22_s_191"
    s "Well—cooking, laundry, cleaning, right? And you even look after a noble.{#ch22_s_191}"

    # シエスタ：それぐらいのことでしたら、わたしと同い年の
    voice "ch22_si_109"
    si "I think anyone my age could do that much, couldn't they?{#ch22_si_109}"

    # シエスタ：小さい頃から、近所同士で年下の子供達の
    voice "ch22_si_110"
    si "I grew up looking after younger kids in the neighborhood, you see.{#ch22_si_110}"

    # シエスタ：父親が出稼ぎで家にいないと、
    voice "ch22_si_111"
    si "When my father was away working, my mother protected our home and fields with my grandparents.{#ch22_si_111}"

    # シエスタ：糸をつむいで服の生地を織ったり
    voice "ch22_si_112"
    si "She spun thread and wove cloth for clothes, too.{#ch22_si_112}"

    # シエスタ：それに、わたしってお節介を焼くのが
    voice "ch22_si_113"
    si "Besides, I might just like being a busybody, you know?{#ch22_si_113}"

    # サイト：ふーん。  [voice 8985]
    voice "ch22_s_192"
    s "Huh.{#ch22_s_192}"

    # サイト：俺の世界だと、そこまで働いている人なんて
    voice "ch22_s_193"
    s "In my world, nobody worked that hard… I'm impressed, really.{#ch22_s_193}"

    # シエスタ：サイトさん、ありがとうございます。
    voice "ch22_si_114"
    si "Thank you, Saito-san. But I…{#ch22_si_114}"

    # サイト：ん？  [voice 8987]
    voice "ch22_s_194"
    s "Hmm?{#ch22_s_194}"

    # [EVENT_CG event    image=+222, level=80]
    $ dissolve_fx("id(222)")
    # シエスタ：わたし、いつかサイトさんのことだけを
    voice "ch22_si_115"
    si "I want to be a busybody only for you, Saito-san, someday.{#ch22_si_115}"

    # サイト：ええ？
    voice "ch22_s_195"
    s "Eh? T-That is…{#ch22_s_195}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+34, level=200]
    $ fade_fx("id(34)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay2     image=+524, level=160, dir=2A]
    # シエスタ：えへへっ！
    voice "ch22_si_116"
    si "Heh heh! Well then, I'll start cleaning the kitchen. Saito-san, please relax.{#ch22_si_116}"

    # [SPRITE   lay2     hide]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：あ、ああ……。  [voice 8989]
    voice "ch22_s_196"
    s "A… Okay…{#ch22_s_196}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay19    image=+946, level=160, dir=1A]
    # デルフリンガー：まったく、相棒は大変だね。  [voice 1220]
    voice "ch22_d_003"
    d "Honestly, you have it rough, partner.{#ch22_d_003}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：いや、まったく……。  [voice 8990]
    voice "ch22_s_197"
    s "Yeah, truly…{#ch22_s_197}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay19    hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [COFFEE]
    $ pause(1.0)
    # → next scene 849
    jump ch23

    # ==== КОНЕЦ ГЛАВЫ 22 ====
    jump ch23
    return

