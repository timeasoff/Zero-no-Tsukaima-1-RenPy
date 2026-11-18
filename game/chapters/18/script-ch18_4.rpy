# Глава 18, часть 4 (сцены 724–738): кризис, лаборатория Кольбера, новый план.
# Источник: ps2_source/chapters/chapter_19_貴族の意地.txt (SCENE 724-738).

label ch18_4:
    $ tndl(None)
    $ show_sprites()

label ch18_4_scene_724:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：よし、なんとかして先生の研究室まで
    voice "ch18_s_184"
    s "Right, let's try to reach the professor's lab somehow. We have nowhere else to go.{#ch18_s_184}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ちょっと待ってサイト！
    voice "ch18_l_133"
    l "Wait, Saito! That's far too dangerous.{#ch18_l_133}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：じゃあ……。
    voice "ch18_s_185"
    s "Then… what should we do?{#ch18_s_185}"

    # → next scene 727
    jump ch18_4_scene_727

label ch18_4_scene_725:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：一旦退却するしかないか。  [voice 11862]
    voice "ch18_s_186"
    s "I guess we have to retreat for now.{#ch18_s_186}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：退却って……どこによ？  [voice 6395]
    voice "ch18_l_134"
    l "Retreat… to where?{#ch18_l_134}"

    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：えーと……。
    voice "ch18_s_187"
    s "Um… Damn, I can't think of anywhere. We're boxed in, huh.{#ch18_s_187}"

    # → next scene 727
    jump ch18_4_scene_727

label ch18_4_scene_726:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：くそぉ……。
    voice "ch18_s_188"
    s "Damn it… What do we do?{#ch18_s_188}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：この場にとどまってるわけにもいかないし、
    voice "ch18_l_135"
    l "We can't just stay here. Is there anywhere still safe?{#ch18_l_135}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：この状況じゃ、それも期待できない……か。  [voice 11865]
    voice "ch18_s_189"
    s "In this situation, I wouldn't count on that either…{#ch18_s_189}"

    # → next scene 727
    jump ch18_4_scene_727

label ch18_4_scene_727:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [BGM      bgm      play=+25]
    play music t24 fadein 1.0
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：そもそもゼロ戦を動かすには、
    voice "ch18_s_190"
    s "To fly the Zero Fighter, we need an open space in the first place.{#ch18_s_190}"

    # サイト：こんなに兵士が多いようだと、
    voice "ch18_s_191"
    s "With this many soldiers around, even with gasoline, we can't just take off.{#ch18_s_191}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：駄目よ！
    voice "ch18_l_136"
    l "No! I have to save everyone…{#ch18_l_136}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+26]
    play music t25 fadein 1.0
    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：はぁ？
    voice "ch18_s_192"
    s "Hah? What are you talking about?{#ch18_s_192}"

    # ルイズ：わたしが、女王陛下も学院長も学院のみんなも、
    voice "ch18_l_137"
    l "I have to protect the Queen, the headmaster, everyone at the academy—all of them.{#ch18_l_137}"

    # ルイズ：だって、わたしは虚無の使い手なのよ。
    voice "ch18_l_138"
    l "Because I'm the wielder of Void. The legendary mage. That's why I won the last war.{#ch18_l_138}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：今回だって……。
    voice "ch18_l_139"
    l "This time too… Yes—even if it costs me my life.{#ch18_l_139}"

    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：この、ばか野郎！  [voice 11869]
    voice "ch18_s_193"
    s "You stupid idiot!{#ch18_s_193}"

    # [SE       se0      play=+71]
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：なんで殴るの……？
    voice "ch18_l_140"
    l "Why did you hit me…? You familiar, you cur—hitting your mistress!{#ch18_l_140}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：あぁ、殴ったよ。
    voice "ch18_s_194"
    s "Yeah, I hit you. Look, Louise. There's one thing I just can't accept.{#ch18_s_194}"

    # サイト：なんで貴族ってのは、自分の命に割り切りが
    voice "ch18_s_195"
    s "Why are you nobles so ready to throw your lives away?{#ch18_s_195}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：貴族だからじゃないわ。
    voice "ch18_l_141"
    l "It's not because I'm a noble. Unless I use Void, the crisis facing Tristain can't be stopped.{#ch18_l_141}"

    # ルイズ：なら、自分ができることをするのは
    voice "ch18_l_142"
    l "Then isn't it natural to do what I can?{#ch18_l_142}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：ルイズ……。
    voice "ch18_s_196"
    s "Louise… But right now, you're clearly pushing yourself too hard.{#ch18_s_196}"

    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：……！  [voice 6404]
    voice "ch18_l_143"
    l "…!{#ch18_l_143}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：確かにおまえは虚無の魔法使いだよ。
    voice "ch18_s_197"
    s "Sure, you're a Void mage. Even I can see that power is incredible.{#ch18_s_197}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：だけどさ、ルイズはさ……、
    voice "ch18_s_198"
    s "But, Louise… you're just a girl.{#ch18_s_198}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：今のおまえ……強がってるだろ？
    voice "ch18_s_199"
    s "Right now you're pretending to be strong, aren't you? You're scared, aren't you? I can't stand seeing you like that.{#ch18_s_199}"

    # サイト：もっと自分のこと、大事に思ってみろよ。
    voice "ch18_s_200"
    s "Try to value yourself more. Like you always do with me—it's fine to be a selfish Louise.{#ch18_s_200}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：サイト……。  [voice 6405]
    voice "ch18_l_144"
    l "Saito…{#ch18_l_144}"

    # サイト：な、だから……。  [voice 11877]
    voice "ch18_s_201"
    s "So, look…{#ch18_s_201}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+211, level=80]
    $ dissolve_fx("id(211)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+22]
    play music t21 fadein 1.0
    # ルイズ：あんたなんかに、あんたなんかに
    voice "ch18_l_145"
    l "What would you know about me… what would you know…{#ch18_l_145}"

    # サイト：ルイズ？  [voice 11878]
    voice "ch18_s_202"
    s "Louise?{#ch18_s_202}"

    # ルイズ：ご主人様の言うことなんか全然聞かなくて、
    voice "ch18_l_146"
    l "You never listen to your mistress, you fawn over girls, you're useless and yet you eat like there's no tomorrow…{#ch18_l_146}"

    # ルイズ：そんなあんたに、言われたくないわよ……。
    voice "ch18_l_147"
    l "I don't want to hear that from you—you know nothing of the burden of being born a noble, or of staying one…{#ch18_l_147}"

    # ルイズ：言われたくなんか……、ないわよおっ……。  [voice 6409]
    voice "ch18_l_148"
    l "I don't want to hear it…!{#ch18_l_148}"

    # サイト：……。  [voice 11879]
    voice "ch18_s_203"
    s "…{#ch18_s_203}"

    # ルイズ：わたしだって、虚無の魔法を使うのは
    voice "ch18_l_149"
    l "I'm scared of using Void magic too, you know…{#ch18_l_149}"

    # ルイズ：伝説の魔法とかいっても、
    voice "ch18_l_150"
    l "They call it legendary magic, but I have no idea what it even is.{#ch18_l_150}"

    # ルイズ：もしかしたら、使ったことで死んじゃうかも
    voice "ch18_l_151"
    l "Maybe using it will kill me.{#ch18_l_151}"

    # ルイズ：わたしだって、もっと楽しく生きていたいわよ。
    voice "ch18_l_152"
    l "I want to live a happier life too. But this is the magic I finally got.{#ch18_l_152}"

    # ルイズ：ゼロのルイズ、ゼロのルイズって
    voice "ch18_l_153"
    l "The Zero Louise, the Zero Louise they mocked me as…{#ch18_l_153}"

    # ルイズ：やっと手に入れた、ゼロじゃない初めての
    voice "ch18_l_154"
    l "This is the first thing I've ever had that isn't zero… sniff, ugh…{#ch18_l_154}"

    # サイト：ルイ……  [voice 11880]
    voice "ch18_s_204"
    s "Loui…{#ch18_s_204}"

    # ルイズ：ばかっ……こっちみるな、
    voice "ch18_l_155"
    l "Idiot… Don't look at me, don't talk to me…!{#ch18_l_155}"

    # ルイズ：使い魔のくせに、ご主人様が泣いてる
    voice "ch18_l_156"
    l "As my familiar, you shouldn't see your mistress crying…!{#ch18_l_156}"

    # サイト：ルイズ……。  [voice 11881]
    voice "ch18_s_205"
    s "Louise…{#ch18_s_205}"

    # ルイズ：な、なによっ……。
    voice "ch18_l_157"
    l "W-What is it… Are you pitying me?{#ch18_l_157}"

    # サイト：そんなんじゃ……ねぇよ。  [voice 11882]
    voice "ch18_s_206"
    s "That's not it… no.{#ch18_s_206}"

    # サイト：ただ……。
    voice "ch18_s_207"
    s "It's just… I couldn't leave you alone, that's all.{#ch18_s_207}"

    # ルイズ：……。  [voice 6419]
    voice "ch18_l_158"
    l "…{#ch18_l_158}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # → next scene 728
    jump ch18_4_scene_728

label ch18_4_scene_728:

    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [SE       se0      play=+75]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：ひっ！？  [voice 6420]
    voice "ch18_l_159"
    l "Eek!?{#ch18_l_159}"

    # [SPRITE   lay5     image=+471, level=160, dir=3B]
    # サイト：誰だっ！  [voice 11884]
    voice "ch18_s_208"
    s "Who's there!{#ch18_s_208}"

    # コルベール：いやいや、その剣を向けるのは勘弁して
    voice "ch18_c_014"
    c "Now, now, surely you can put that sword away, Saito-kun.{#ch18_c_014}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+473, level=160, dir=3B]
    # ルイズ：その声……。
    voice "ch18_l_160"
    l "That voice… Mr. Colbert?{#ch18_l_160}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：その通り。
    voice "ch18_c_015"
    c "Indeed. And I apologize for interrupting.{#ch18_c_015}"

    # コルベール：だが、知っての通り今は学院の内も外も
    voice "ch18_c_016"
    c "But as you know, things are critical inside and outside the academy. I hope you'll forgive the breach of etiquette.{#ch18_c_016}"

    # [SPRITE   lay9     x=-96, y=0]
    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：べ、別に……。
    voice "ch18_l_161"
    l "N-Not at all… I-I'm fine!{#ch18_l_161}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：ところでコルベール先生、よく無事でしたね。  [voice 11885]
    voice "ch18_s_209"
    s "By the way, professor, you're safe—that's good.{#ch18_s_209}"

    # コルベール：オールド・オスマンの要請があり、
    voice "ch18_c_017"
    c "Old Osmond asked me to find you. I'm glad we met up safely.{#ch18_c_017}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：学院長の？  [voice 11886]
    voice "ch18_s_210"
    s "From the headmaster?{#ch18_s_210}"

    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # コルベール：うん。
    voice "ch18_c_018"
    c "Yes. Though it seems our last hope—this Zero Fighter—is in a sorry state.{#ch18_c_018}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：えぇ、ガソリンが足りなくて……。
    voice "ch18_s_211"
    s "Eh, we're short on gasoline… Don't you have a spare, professor?{#ch18_s_211}"

    # コルベール：すみません。
    voice "ch18_c_019"
    c "Sorry. With all the recent turmoil, I neglected the refining. This is a lifelong shame for me.{#ch18_c_019}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：そうですか……。  [voice 6423]
    voice "ch18_l_162"
    l "I see…{#ch18_l_162}"

    # [SPRITE   lay9     image=+933, level=160, dir=1A]
    # コルベール：しかし、ゼロ戦が使用不可能と分かった以上、
    voice "ch18_c_020"
    c "Still, now that the Zero Fighter is unusable, staying here is dangerous.{#ch18_c_020}"

    # コルベール：実は今、学院のほとんどがレコン・キスタ軍の
    voice "ch18_c_021"
    c "In fact, most of the academy is now under Reconquista's control.{#ch18_c_021}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：ひとまずゼロ戦には不可視の魔法を
    voice "ch18_c_022"
    c "For now, let's put an invisibility spell on the Zero Fighter. We can't let it be destroyed.{#ch18_c_022}"

    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # コルベール：さて、今は身を隠すのが先決ですね。
    voice "ch18_c_023"
    c "Now, first we need to hide. And I know just the place for it.{#ch18_c_023}"

    menu:
        "Is there such a place in the academy?{#ch18_4_c_728_1}":
            jump ch18_4_scene_729
        "Louise's room?{#ch18_4_c_728_2}":
            jump ch18_4_scene_730
        "The professor's lab?{#ch18_4_c_728_3}":
            jump ch18_4_scene_731

label ch18_4_scene_729:

    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：今の学院に、そんな場所があるんですか？
    voice "ch18_s_212"
    s "Is there such a place left in the academy? From what you say, we can neither flee nor hide…{#ch18_s_212}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：そ、そうですミスタ・コルベール。
    voice "ch18_l_163"
    l "R-Right, Mr. Colbert. Isn't staying inside the academy more dangerous?{#ch18_l_163}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：おいおい、サイトくんも何度か来てる
    voice "ch18_c_024"
    c "Come now, Saito-kun has been there several times, haven't you? It's my lab.{#ch18_c_024}"

    # [SPRITE   lay1     hide]
    # → next scene 732
    jump ch18_4_scene_732

label ch18_4_scene_730:

    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：もしかして、ルイズの部屋ですか？  [voice 11889]
    voice "ch18_s_213"
    s "Could it be Louise's room?{#ch18_s_213}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：そんなはずないでしょ？
    voice "ch18_l_164"
    l "That can't be. Why would my room be a perfect hiding place?{#ch18_l_164}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：ほら、相手の裏をかくというか、
    voice "ch18_s_214"
    s "Well, it's, you know, outsmarting the enemy, or…{#ch18_s_214}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：おいおい、サイトくんも何度か来てる
    voice "ch18_c_025"
    c "Come now, Saito-kun has been there several times, haven't you? It's my lab.{#ch18_c_025}"

    # → next scene 732
    jump ch18_4_scene_732

label ch18_4_scene_731:

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：まさか、先生の研究室ですか？  [voice 11891]
    voice "ch18_s_215"
    s "Surely not the professor's lab?{#ch18_s_215}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+341, level=160, dir=2A]
    # ルイズ：研究室？  [voice 6426]
    voice "ch18_l_165"
    l "The lab?{#ch18_l_165}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：そのとおり。
    voice "ch18_c_026"
    c "Exactly. Correct, Saito-kun.{#ch18_c_026}"

    # [SPRITE   lay1     hide]
    # → next scene 732
    jump ch18_4_scene_732

label ch18_4_scene_732:

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+75, level=200]
    $ fade_fx("id(75)")
    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：え、でもコルベール先生の研究室って校舎の中
    voice "ch18_s_216"
    s "Eh, but the professor's lab is pretty deep inside the school building… We'll be spotted, won't we?{#ch18_s_216}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：そうだな、確かに正規のルートを通っていったら
    voice "ch18_c_027"
    c "True, the official route would be dangerous. Yes, the official route is dangerous.{#ch18_c_027}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ミスタ・コルベール……まさか。  [voice 6427]
    voice "ch18_l_166"
    l "Mr. Colbert… surely not.{#ch18_l_166}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # コルベール：ご案内するよ、ミス・ヴァリエールに
    voice "ch18_c_028"
    c "Allow me to guide you, Miss Valliere and Saito-kun. This is… the shortcut to my lab.{#ch18_c_028}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+74, level=200]
    $ fade_fx("id(74)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+19]
    play music t18 fadein 1.0
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：え、えぇっ？  [voice 11893]
    voice "ch18_s_217"
    s "E-Eh!?{#ch18_s_217}"

    # ルイズ：これって、もしかして……。  [voice 6428]
    voice "ch18_l_167"
    l "This is, could it be…{#ch18_l_167}"

    # サイト：地下道ッ！？  [voice 11894]
    voice "ch18_s_218"
    s "A secret tunnel!?{#ch18_s_218}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：これこそがこのコルベールに、
    voice "ch18_c_029"
    c "This is exactly why I'm called the ever-appearing Colbert, you two.{#ch18_c_029}"

    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # コルベール：さぁ、いざゆかん。
    voice "ch18_c_030"
    c "Now, onward! To my beloved lab!{#ch18_c_030}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [SPRITE   lay5     image=+436, level=160, dir=2B]
    # サイト：はは……。
    voice "ch18_s_219"
    s "Heh. This is a bit of an adventure, isn't it? Right, Louise?{#ch18_s_219}"

    # ルイズ：しらないわよ、もう。  [voice 6429]
    voice "ch18_l_168"
    l "Don't ask me.{#ch18_l_168}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # → next scene 733
    jump ch18_4_scene_733

label ch18_4_scene_733:

    # [BG       stage    image=+83, level=200]
    $ fade_fx("id(83)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：さ、むさくるしいところだが入ってくれたまえ。  [voice 1090]
    voice "ch18_c_031"
    c "Come in, it's a bit of a mess.{#ch18_c_031}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：お邪魔します……。  [voice 11896]
    voice "ch18_s_220"
    s "Pardon the intrusion…{#ch18_s_220}"

    # ルイズ：失礼します。  [voice 6430]
    voice "ch18_l_169"
    l "Excuse us.{#ch18_l_169}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：さて、早速だが。
    voice "ch18_c_032"
    c "Right, without further ado. The academy is currently under Reconquista's control.{#ch18_c_032}"

    # コルベール：ほぼ唯一の例外と言えるのがこの場所だがね。  [voice 1092]
    voice "ch18_c_033"
    c "The only exception is this place, more or less.{#ch18_c_033}"

    # コルベール：この研究室は、学院からはかなり離れた
    voice "ch18_c_034"
    c "This lab is quite far from the academy, and from the outside it looks like just a stone shack.{#ch18_c_034}"

    # コルベール：しかも、わたしはこの学院では誰よりも
    voice "ch18_c_035"
    c "And I probably understand the situation better than anyone here. Because…{#ch18_c_035}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [EVENT_CG event    image=+133, level=80]
    $ dissolve_fx("id(133)")
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [SE       se0      play=+68]
    # [BG       stage    vibrate=7]
    # [EVENT_CG event    vibrate=7]
    # [SPRITE   lay5     vibrate=7]
    # [SPRITE   lay9     vibrate=7]
    # [SPRITE   lay1     vibrate=7]
    # [VIBRATE vibrate(1)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    reset]
    # [SPRITE   lay5     hide, reset]
    # [SPRITE   lay9     reset]
    # [SPRITE   lay1     hide, reset]
    # ルイズ：ひっ、ネ……ネズミっ！？  [voice 6431]
    voice "ch18_l_170"
    l "Eek, a m-mouse!?{#ch18_l_170}"

    # コルベール：あー、つぶさんでくれよ。
    voice "ch18_c_036"
    c "Oh, don't crush it. This is no ordinary mouse.{#ch18_c_036}"

    # コルベール：何を隠そう、オールド・オスマンの
    voice "ch18_c_037"
    c "Believe it or not, it's Old Osmond's familiar.{#ch18_c_037}"

    # ルイズ：これが？
    voice "ch18_l_171"
    l "This? It just looks like a small white mouse…{#ch18_l_171}"

    # コルベール：物事を見かけだけで判断してはいけないよ、
    voice "ch18_c_038"
    c "Don't judge by appearances, Miss Valliere. That goes for your familiar too.{#ch18_c_038}"

    # ルイズ：え、えぇ……まぁ。  [voice 6433]
    voice "ch18_l_172"
    l "E-Eh… Well, yes.{#ch18_l_172}"

    # コルベール：わたしは、オールド・オスマンが
    voice "ch18_c_039"
    c "I was given a task before Old Osmond entered negotiations with Akina.{#ch18_c_039}"

    # [EVENT_CG event    image=+134, level=80]
    $ dissolve_fx("id(134)")
    # コルベール：この使い魔……モートソグニルを
    voice "ch18_c_040"
    c "I was entrusted with this familiar—Mortosgnir.{#ch18_c_040}"

    # コルベール：それから、彼を通じて学院長室に軟禁されてる
    voice "ch18_c_041"
    c "Through him, I've been in contact with Old Osmond, confined in the headmaster's office.{#ch18_c_041}"

    # [EVENT_CG event    image=+133, level=80]
    $ dissolve_fx("id(133)")
    # サイト：は、はぁ……そうなんですか。  [voice 11897]
    voice "ch18_s_221"
    s "H-Haa… Is that so.{#ch18_s_221}"

    # サイト：（いったいどうやってネズミと
    s "(How does one even communicate with a mouse…?){#ch18_s_222}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     hide]
    # [SPRITE   lay1     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+83, level=200]
    $ fade_fx("id(83)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay9     image=+933, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # コルベール：さて、重要なのはここからだ。
    voice "ch18_c_042"
    c "Now, here's the important part. Weatherly's target is the Void mage and her familiar…{#ch18_c_042}"

    # コルベール：つまりミス・ヴァリエールとサイトくんについて
    voice "ch18_c_043"
    c "In other words, information on Miss Valliere and Saito-kun, and probably capturing you both.{#ch18_c_043}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：さらに、学院が収集した
    voice "ch18_c_044"
    c "Plus, seizing the magic items the academy has collected and learning how to use them.{#ch18_c_044}"

    # コルベール：オールド・オスマンはウェザリーの
    voice "ch18_c_045"
    c "Old Osmond has steadfastly refused all of Weatherly's demands.{#ch18_c_045}"

    # [SPRITE   lay9     image=+933, level=160, dir=1A]
    # コルベール：それに対してウェザリーは、
    voice "ch18_c_046"
    c "In response, Weatherly threatens to wipe out everyone inside the academy, teachers and students alike, whether they resist or not. {#ch18_c_046}"

    # コルベール：無論その手段はアキナくんの爆弾と、
    voice "ch18_c_047"
    c "Naturally, the means would be Akina's bombs and a barrage from the aerial ships.{#ch18_c_047}"

    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # コルベール：聞くところによると、王都トリスタニアの方
    voice "ch18_c_048"
    c "I hear the capital, Tristain, is in terrible shape too—street fighting, the approaching Reconquista fleet.{#ch18_c_048}"

    # コルベール：これでは、支援は期待できないだろう。
    voice "ch18_c_049"
    c "We can't expect reinforcements. The same goes for the surrounding nobles.{#ch18_c_049}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：そこで、今回、わたしは今回の事件を
    voice "ch18_c_050"
    c "So I'd like to take charge of this incident myself.{#ch18_c_050}"

    # [SPRITE   lay9     x=-96, y=0]
    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：は、はぁ……。  [voice 11898]
    voice "ch18_s_223"
    s "H-Haa…{#ch18_s_223}"

    # コルベール：作戦の目的は幾つかある。
    voice "ch18_c_051"
    c "The operation has several goals. First, eliminate the enemy forces inside the academy.{#ch18_c_051}"

    # コルベール：さらに作戦指揮官であるウェザリーと、
    voice "ch18_c_052"
    c "Then, neutralizing and restraining Weatherly—the operation's commander—and Akina.{#ch18_c_052}"

    # コルベール：学院内に仕掛けられた爆弾の無効化も
    voice "ch18_c_053"
    c "Disarming the bombs planted around the academy is also pending, but probably only Akina can handle them.{#ch18_c_053}"

    # コルベール：彼女を拘束すれば爆弾の脅威は消える。  [voice 1113]
    voice "ch18_c_054"
    c "If we restrain her, the bomb threat disappears.{#ch18_c_054}"

    # [SPRITE   lay9     image=+933, level=160, dir=1A]
    # コルベール：最後に……これが問題だが、
    voice "ch18_c_055"
    c "Finally… here's the problem—the aerial ship lounging above the academy.{#ch18_c_055}"

    # コルベール：これは取り扱いが難しい。
    voice "ch18_c_056"
    c "This one is difficult. Left alone, it could link up with Reconquista's main fleet.{#ch18_c_056}"

    # [SPRITE   lay9     x=-96, y=0]
    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：ゼロ戦さえ動かせりゃなぁ……。
    voice "ch18_s_224"
    s "If only I could get the Zero Fighter running… One ship, I think I could manage.{#ch18_s_224}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：うーん……。  [voice 6434]
    voice "ch18_l_173"
    l "Mm…{#ch18_l_173}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # コルベール：ないものねだりをしても仕方がない。
    voice "ch18_c_057"
    c "Wishing for what we don't have is pointless. We'll have to improvise…{#ch18_c_057}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：やります。  [voice 6435]
    voice "ch18_l_174"
    l "I'll do it.{#ch18_l_174}"

    # [SPRITE   lay9     image=+933, level=160, dir=1A]
    # コルベール：ん？
    voice "ch18_c_058"
    c "Hm? Miss Valliere, you just said…{#ch18_c_058}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：あの戦艦は、わたしが引き受けます。  [voice 6436]
    voice "ch18_l_175"
    l "I'll take that battleship.{#ch18_l_175}"

    # [SPRITE   lay9     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ルイズ、おまえまさか……。  [voice 11900]
    voice "ch18_s_225"
    s "Louise, surely you don't mean…{#ch18_s_225}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：そうよ、虚無の魔法を使うの。
    voice "ch18_l_176"
    l "Yes. I'll use Void magic. Fortunately, they don't seem to know exactly what my Void magic does.{#ch18_l_176}"

    # ルイズ：誰もその全容を知らない魔法なら……
    voice "ch18_l_177"
    l "If nobody knows its full nature, it should surprise them—and be quite effective.{#ch18_l_177}"

    # ルイズ：いかがでしょうか？
    voice "ch18_l_178"
    l "What do you think, Mr. Colbert?{#ch18_l_178}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：ふむ……そうだね。
    voice "ch18_c_059"
    c "Hmm… Yes, it's worth trying. But how good are our chances?{#ch18_c_059}"

    menu:
        "No, that's a bit much…{#ch18_4_c_733_1}":
            jump ch18_4_scene_734
        "What is Louise going to use?{#ch18_4_c_733_2}":
            jump ch18_4_scene_735
        "Oh, even I don't get it{#ch18_4_c_733_3}":
            jump ch18_4_scene_736

label ch18_4_scene_734:

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+83, level=200]
    $ fade_fx("id(83)")
    # [SPRITE   lay9     hide]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：いや、ルイズのアレは……。
    voice "ch18_s_226"
    s "No, Louise's power is… I mean, we might turn the whole academy to ash with it.{#ch18_s_226}"

    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # ルイズ：な、なんですってぇっ……！  [voice 6440]
    voice "ch18_l_179"
    l "W-What was that!?{#ch18_l_179}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：いや、だってあの時もさ……。  [voice 11902]
    voice "ch18_s_227"
    s "I mean, back then too…{#ch18_s_227}"

    # → next scene 737
    jump ch18_4_scene_737

label ch18_4_scene_735:

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+83, level=200]
    $ fade_fx("id(83)")
    # [SPRITE   lay9     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ルイズ、おまえ……。
    voice "ch18_s_228"
    s "Louise… what do you intend to use? Surely not that thing from the other day…?{#ch18_s_228}"

    # → next scene 737
    jump ch18_4_scene_737

label ch18_4_scene_736:

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+83, level=200]
    $ fade_fx("id(83)")
    # [SPRITE   lay9     hide]
    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：お、俺にも分からないんだけど。  [voice 11904]
    voice "ch18_s_229"
    s "E-Er, I don't understand it myself.{#ch18_s_229}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：大丈夫よ、あの戦艦をバッチリ
    voice "ch18_l_180"
    l "It's fine! I'll take that battleship down perfectly!{#ch18_l_180}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：ま、まさかこのあいだのアレを……？  [voice 11905]
    voice "ch18_s_230"
    s "Surely not that thing from the other day…?{#ch18_s_230}"

    # → next scene 737
    jump ch18_4_scene_737

label ch18_4_scene_737:

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # [SPRITE   lay1     image=+339, level=160, dir=2A]
    # [BGM      bgm      play=+32]
    play music t31 fadein 1.0
    # [BG       stage    image=+83, level=200]
    $ fade_fx("id(83)")
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：あんた、まさかわたしがエクスプロージョンを
    voice "ch18_l_181"
    l "You don't think I'd use Explosion, do you?{#ch18_l_181}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：え……。
    voice "ch18_s_231"
    s "Eh… Isn't it?{#ch18_s_231}"

    # [SPRITE   lay1     image=+335, level=160, dir=2A]
    # ルイズ：いくらわたしでも、学院でエクスプロージョンを
    voice "ch18_l_182"
    l "Even I can imagine what would happen if I used Explosion in the academy.{#ch18_l_182}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：え、ということは……。  [voice 11907]
    voice "ch18_s_232"
    s "Eh, so that means…{#ch18_s_232}"

    # [SPRITE   lay1     image=+337, level=160, dir=2A]
    # ルイズ：新しい魔法をつかうの。
    voice "ch18_l_183"
    l "I'll use a new spell. The right magic for a situation like this.{#ch18_l_183}"

    # ルイズ：うまくいけば、１人の犠牲もナシに学院を
    voice "ch18_l_184"
    l "If it works, we can retake the academy without a single casualty.{#ch18_l_184}"

    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：信じて、いいんだな？  [voice 11908]
    voice "ch18_s_233"
    s "I can trust you, right?{#ch18_s_233}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：わたしはあんたのご主人様よ。
    voice "ch18_l_185"
    l "I'm your mistress. Who else would you trust?{#ch18_l_185}"

    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：分かったよ。
    voice "ch18_s_234"
    s "Got it. Let's bet on my mistress, then.{#ch18_s_234}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：どうやらご主人様と使い魔で話はまとまった
    voice "ch18_c_060"
    c "Looks like mistress and familiar have come to an agreement. Then I'll help too.{#ch18_c_060}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：協力ですか？  [voice 11910]
    voice "ch18_s_235"
    s "Help?{#ch18_s_235}"

    # コルベール：ウェザリーのことだ。  [voice 1120]
    voice "ch18_c_061"
    c "About Weatherly.{#ch18_c_061}"

    # サイト：ウェザリーの？  [voice 11911]
    voice "ch18_s_236"
    s "Weatherly?{#ch18_s_236}"

    # コルベール：学院長室の中で、おかしな音が聞こえた
    voice "ch18_c_062"
    c "Do you remember the strange sound in the headmaster's office?{#ch18_c_062}"

    # [SPRITE   lay9     image=+933, level=160, dir=1A]
    # コルベール：実はだね、ウェザリーは心を操る
    voice "ch18_c_063"
    c "The truth is, Weatherly seems to be a user of mind-controlling magic. She controls hearts through sound.{#ch18_c_063}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：催眠術、みたいなものですか？  [voice 11912]
    voice "ch18_s_237"
    s "Like hypnosis?{#ch18_s_237}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：わたしも見たことがない魔法だがね。
    voice "ch18_c_064"
    c "It's magic I've never seen before. Probably unique to Weatherly.{#ch18_c_064}"

    # コルベール：アキナくんだったかな？
    voice "ch18_c_065"
    c "And Akina-kun? She must be controlling Haruna-kun in a similar way.{#ch18_c_065}"

    # サイト：何か対抗する方法はないんですか？  [voice 11913]
    voice "ch18_s_238"
    s "Isn't there a way to counter it?{#ch18_s_238}"

    # コルベール：これを見たまえ。  [voice 1125]
    voice "ch18_c_066"
    c "Look at this.{#ch18_c_066}"

    # サイト：（そう言うとコルベール先生は、何やら木製の小さな物体を取り出した）
    s "(As he said that, Professor Colbert took out some small wooden object.){#ch18_s_248}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：えと……なんでしょうか、これ？
    voice "ch18_l_186"
    l "Um… What's this? It looks like earplugs.{#ch18_l_186}"

    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # コルベール：見てのとおり、耳栓だ。
    voice "ch18_c_067"
    c "As you see, earplugs. Though enchanted with a special wind spell.{#ch18_c_067}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：この耳栓をつけていれば、ウェザリーが
    voice "ch18_c_068"
    c "With these in, Weatherly's magic will be nullified when she tries it.{#ch18_c_068}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+401, level=160, dir=1B]
    # サイト：すごいですね。
    voice "ch18_s_239"
    s "Amazing. Made in no time…{#ch18_s_239}"

    # [SPRITE   lay9     image=+931, level=160, dir=1A]
    # コルベール：あ、いや、基本的にはオールド・オスマンの
    voice "ch18_c_069"
    c "Ah, no—it's mostly thanks to Old Osmond's help. Quite the headmaster, isn't he?{#ch18_c_069}"

    # サイト：これで春奈を元に戻せるのですか？  [voice 11915]
    voice "ch18_s_240"
    s "Can this bring Haruna back?{#ch18_s_240}"

    # [SPRITE   lay9     image=+935, level=160, dir=1A]
    # コルベール：残念ながら、それは難しいと思う。  [voice 1129]
    voice "ch18_c_070"
    c "Sadly, that will be difficult.{#ch18_c_070}"

    # コルベール：操ることはできなくても、
    voice "ch18_c_071"
    c "Even if we stop the control, removing the personality created in her mind won't be easy.{#ch18_c_071}"

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # サイト：そうですか……。  [voice 11916]
    voice "ch18_s_241"
    s "I see…{#ch18_s_241}"

    # [SPRITE   lay9     image=+929, level=160, dir=1A]
    # コルベール：同じものは１０個ほど用意することができた。
    voice "ch18_c_072"
    c "I managed to prepare about ten of these. Use them when calling on Miss Zerbst or Miss Tabitha for help.{#ch18_c_072}"

    # コルベール：モートソグニルによれば、あの２人は未だ
    voice "ch18_c_073"
    c "According to Mortosgnir, those two haven't been captured yet.{#ch18_c_073}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：ミスタ・コルベール。
    voice "ch18_l_187"
    l "Mr. Colbert, thank you for your efforts.{#ch18_l_187}"

    # コルベール：うむ。
    voice "ch18_c_074"
    c "Good. Now that we have a countermeasure, let's hold a real strategy meeting.{#ch18_c_074}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay9     hide]
    # [BG       stage    hide]
    # → next scene 738
    jump ch18_4_scene_738

label ch18_4_scene_738:

    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # サイト：（結局、俺達の学園奪還計画は、
    s "(In the end, our plan to retake the academy was set for just after dawn.){#ch18_s_242}"

    # サイト：（敵兵士達の動きも鈍いと思われることと、
    s "(The enemy soldiers would be slower then, and Louise wanted to reach the capital as soon as possible.){#ch18_s_243}"

    # サイト：（というわけで、俺達は明日に備えて
    s "(So we decided to turn in early to prepare for tomorrow—but…){#ch18_s_244}"

    # サイト：（だめだ、最初の２、３時間軽く寝ただけで
    s "(No good. I slept lightly for the first two or three hours, then couldn't sleep anymore.){#ch18_s_245}"

    # サイト：（なんだかちょっと前にも
    s "(I feel like something like this happened not too long ago…){#ch18_s_246}"

    # サイト：（俺ってつくづくワンパターンな行動しか
    s "(I really only ever act the same way, don't I…){#ch18_s_247}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # ==== КОНЕЦ ГЛАВЫ 18 ====
    jump attention
    return

