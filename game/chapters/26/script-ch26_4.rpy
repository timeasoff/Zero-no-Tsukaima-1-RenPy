# Глава 26, часть 4 (сцены 965–966): атака Акины, прошлое Табасы.
# Источник: ps2_source/chapters/chapter_27_タバサの秘密.txt (SCENE 965-966).

label ch26_4:
    $ tndl(None)
    $ show_sprites()

label ch26_4_scene_965:

    # [SPRITE   lay5     image=+407, level=160, dir=1B]
    # [LAYER    lay0     image=+588, level=160, dir=1A]
    # [BGM      bgm      play=+18]
    play music t17 fadein 1.0
    # [BG       stage    image=+40, level=200]
    $ fade_fx("id(40)")
    # タバサ：これが本当の任務の目的……。  [voice 15715]
    voice "ch26_t_047"
    t "So that was the real purpose of the mission…{#ch26_t_047}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：えっ？
    voice "ch26_s_139"
    s "Eh? The mission…{#ch26_s_139}"

    # [SPRITE   lay5     image=+438, level=160, dir=2B]
    # サイト：それは、ガリア王国がハルナが爆弾使いだと
    voice "ch26_s_140"
    s "Are you saying Gallia knew Haruna was the bomber?{#ch26_s_140}"

    # サイト：タバサ、教えてくれ。
    voice "ch26_s_141"
    s "Tabitha, tell me. Just how much does Gallia know?{#ch26_s_141}"

    # タバサ：……。
    t "…{#ch26_t_048}"

    # [SPRITE   lay5     image=+440, level=160, dir=2B]
    # サイト：ちょっと待てよ？
    voice "ch26_s_142"
    s "Wait a moment. You really intend to capture Haruna and take her to Gallia?{#ch26_s_142}"

    # サイト：今の人格はアキナだろうけど、
    voice "ch26_s_143"
    s "The personality is Akina now, but the body is Haruna's!{#ch26_s_143}"

    # タバサ：……。
    t "…{#ch26_t_049}"

    # サイト：おい、タバサッ！？  [voice 12653]
    voice "ch26_s_144"
    s "Hey, Tabitha!?{#ch26_s_144}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：おいおい、仲間割れかい？
    voice "ch26_ak_017"
    ak "Hey now, infighting? You're still too soft…{#ch26_ak_017}"

    # アキナ：コイツを食らいなっ！！  [voice 145]
    voice "ch26_ak_018"
    ak "Take this!!{#ch26_ak_018}"

    # [SPRITE   lay21    hide]
    # [LAYER    lay0     image=+593, level=140, dir=1A]
    # タバサ：サイト……！！  [voice 15716]
    voice "ch26_t_050"
    t "Saito…!!{#ch26_t_050}"

    # [LAYER    lay0     hide]
    # [SE       se0      play=+63]
    # [BG       stage    vibrate=21]
    # [EVENT_CG event    vibrate=21]
    # [SPRITE   lay21    vibrate=21]
    # [SPRITE   lay5     vibrate=21]
    # [LAYER    lay0     vibrate=21]
    # [VIBRATE vibrate(3)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay21    hide, reset]
    # [SPRITE   lay5     hide, reset]
    # [LAYER    lay0     hide, reset]
    # [LAYER    white    image=+2, level=0]
    $ flash_fx("white")
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [LAYER    lay0     hide]
    # [TRANS trans("crossfade", 0)]
    # [LAYER    white    hide]
    # サイト：なっ、タバサッ！  [voice 12654]
    voice "ch26_s_145"
    s "Wha—Tabitha!{#ch26_s_145}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：ははははははははっ。
    voice "ch26_ak_019"
    ak "Ha ha ha ha ha! This is comedy! That Tabitha shielding Saito!{#ch26_ak_019}"

    # [SPRITE   lay21    x=-96, y=0]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # サイト：うるさいうるさい！
    voice "ch26_s_146"
    s "Shut up, shut up! Be quiet!{#ch26_s_146}"

    # [SPRITE   lay21    image=+1023, level=160, dir=1A]
    # アキナ：おお怖。  [voice 147]
    voice "ch26_ak_020"
    ak "Ooh, scary.{#ch26_ak_020}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay5     image=+408, level=140, dir=1B]
    # サイト：なんだって、俺のことをかばって……。  [voice 12656]
    voice "ch26_s_147"
    s "Why did you shield me…{#ch26_s_147}"

    # タバサ：……無事？  [voice 15717]
    voice "ch26_t_051"
    t "…Are you all right?{#ch26_t_051}"

    # [SPRITE   lay5     image=+402, level=140, dir=1B]
    # サイト：ああ、俺は無事だよ。
    voice "ch26_s_148"
    s "Ah, I'm fine. I'm all right.{#ch26_s_148}"

    # タバサ：良かった……。  [voice 15718]
    voice "ch26_t_052"
    t "Thank goodness…{#ch26_t_052}"

    # [SPRITE   lay5     image=+406, level=140, dir=1B]
    # サイト：おい、タバサッ？
    voice "ch26_s_149"
    s "Hey, Tabitha? Wake up, wake up!{#ch26_s_149}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay5     image=+405, level=160, dir=1B]
    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：アハハッ、思ったとおりだよ。
    voice "ch26_ak_021"
    ak "Ah ha ha, just as I thought. I knew you'd gallantly shield Saito that way.{#ch26_ak_021}"

    # サイト：それを分かったうえで、俺に爆弾を投げたのか？  [voice 12659]
    voice "ch26_s_150"
    s "And knowing that, you still threw the bomb at me?{#ch26_s_150}"

    # [SPRITE   lay21    image=+1017, level=160, dir=1A]
    # アキナ：ああそうだよ、そのとおりさ。
    voice "ch26_ak_022"
    ak "Oh yes, exactly. And sure enough—willing to risk your life to shield him. What a gallant girl.{#ch26_ak_022}"

    # アキナ：それじゃ、あたしはバイバイさせて
    voice "ch26_ak_023"
    ak "Then, I suppose it's time for me to say goodbye.{#ch26_ak_023}"

    # サイト：おいっ、逃げるなっ！  [voice 12660]
    voice "ch26_s_151"
    s "Hey—don't you run away!{#ch26_s_151}"

    # アキナ：だったら、追いかけて来ればいいじゃない？
    voice "ch26_ak_024"
    ak "Then just chase me. Leaving that girl burning for your sake behind—right?~{#ch26_ak_024}"

    # サイト：クッ、ちくしょうっ！  [voice 12661]
    voice "ch26_s_152"
    s "Ugh, damn it!{#ch26_s_152}"

    # [SPRITE   lay21    image=+1019, level=160, dir=1A]
    # アキナ：言ったろ？
    voice "ch26_ak_025"
    ak "I told you, didn't I? That kindness of yours hurts everyone. Ah ha ha, see you~!{#ch26_ak_025}"

    # [SPRITE   lay21    hide]
    # [SPRITE   lay5     x=64, y=0]
    # サイト：春奈の体を使ってるクセに……。
    voice "ch26_s_153"
    s "Using Haruna's body like that… What a horrible thing to do!{#ch26_s_153}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # → next scene 966
    jump ch26_4_scene_966

label ch26_4_scene_966:

    # [BG       stage    image=+90, level=200]
    $ fade_fx("id(90)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+20]
    play music t19 fadein 1.0
    # サイト：（あれから俺達は、駆けつけてきたルイズと
    s "(After that, we were taken in by Louise and Kirche, who'd rushed to the scene.){#ch26_s_154}"

    # サイト：（タバサの火傷を治療するには
    s "(It took a lot of medicine and magic to treat Tabitha's burns…){#ch26_s_155}"

    # サイト：（しかし、幸いというべきか、
    s "(But fortunately—if one can call it that—Montmorency and Guiche, having heard the commotion, came to our lodgings.){#ch26_s_156}"

    # サイト：（事情を聞きたがる２人をなんとか
    s "(I managed to calm the two down, who wanted to hear the story, and had Montmorency treat Tabitha's injuries right away.){#ch26_s_157}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # モンモランシー：ふう……。
    voice "ch26_m_003"
    m "Phew… She should be all right now.{#ch26_m_003}"

    # [SPRITE   lay3     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：本当か？
    voice "ch26_s_158"
    s "Really? Is she really all right?{#ch26_s_158}"

    # モンモランシー：火傷を全部治したもの。
    voice "ch26_m_004"
    m "I healed all the burns. She's truly fine.{#ch26_m_004}"

    # モンモランシー：あとは体力の回復が必要なの。
    voice "ch26_m_005"
    m "What she needs now is rest. She should stay quiet for a few days.{#ch26_m_005}"

    # モンモランシー：それと、熱には注意してね。
    voice "ch26_m_006"
    m "And watch for fever. There's still a chance the burns could become inflamed.{#ch26_m_006}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：分かった。
    voice "ch26_s_159"
    s "Got it. I'll nurse her with all my care.{#ch26_s_159}"

    # モンモランシー：それじゃ、わたしも休ませてもらうわね。  [voice 4118]
    voice "ch26_m_007"
    m "Then, I'll go rest, too.{#ch26_m_007}"

    # [SPRITE   lay5     image=+425, level=160, dir=2A]
    # サイト：ありがとな、モンモン。  [voice 12665]
    voice "ch26_s_160"
    s "Thanks, Montmorency.{#ch26_s_160}"

    # [SPRITE   lay3     image=+854, level=160, dir=1A]
    # モンモランシー：良かったわよ。
    voice "ch26_m_008"
    m "Good—that we're still in the capital.{#ch26_m_008}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：そうだな。  [voice 12666]
    voice "ch26_s_161"
    s "You're right.{#ch26_s_161}"

    # [SPRITE   lay3     image=+852, level=160, dir=1A]
    # モンモランシー：この戦争みたいな騒ぎでしょ？
    voice "ch26_m_009"
    m "With all this war-like commotion, we couldn't leave the capital—it was a real problem.{#ch26_m_009}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：まぁ、幸運ってやつか……。  [voice 12667]
    voice "ch26_s_162"
    s "Well, that's what you call luck, I suppose…{#ch26_s_162}"

    # モンモランシー：まぁ、そういうものね。
    voice "ch26_m_010"
    m "Yes, it is. Now, let me rest. I'm quite tired myself.{#ch26_m_010}"

    # [SPRITE   lay3     hide]
    # [SPRITE   lay5     x=64, y=0]
    # [SE       se0      play=+56]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：……。  [voice 12668]
    voice "ch26_s_163"
    s "…{#ch26_s_163}"

    # サイト：（タバサが怪我したのって、
    s "(Tabitha getting hurt—it's my fault, after all…){#ch26_s_164}"

    # サイト：（俺がタバサのあとについて行かなけりゃ、
    s "(If I hadn't followed her, maybe Tabitha would've beaten Haruna—no, Akina—on her own…){#ch26_s_165}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：はぁ……。
    voice "ch26_s_166"
    s "Haa… What am I…{#ch26_s_166}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：なにヘコんでるのよ？  [voice 6887]
    voice "ch26_l_065"
    l "What are you moping about?{#ch26_l_065}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：な、なんでもねーよ。  [voice 12670]
    voice "ch26_s_167"
    s "N-Nothing!{#ch26_s_167}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：ふーん、そう。  [voice 6888]
    voice "ch26_l_066"
    l "Hmm. Is that so.{#ch26_l_066}"

    # サイト：……。  [voice 12671]
    voice "ch26_s_168"
    s "…{#ch26_s_168}"

    # ルイズ：……。  [voice 6889]
    voice "ch26_l_067"
    l "…{#ch26_l_067}"

    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：で、タバサの看病なんだけど、
    voice "ch26_l_068"
    l "Well—about nursing Tabitha. I'll help you, too.{#ch26_l_068}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：えっ、なんで？  [voice 12672]
    voice "ch26_s_169"
    s "Eh? Why?{#ch26_s_169}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：なんでって……。
    voice "ch26_l_069"
    l "Why? It's obvious. A familiar's mess is the mistress's responsibility.{#ch26_l_069}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：そっか。
    voice "ch26_s_170"
    s "I see. Thanks.{#ch26_s_170}"

    # ルイズ：なによ……。
    voice "ch26_l_070"
    l "What's that…? Talk back to me like usual. It throws me off…{#ch26_l_070}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：タバサがこうなったのって、俺のせいだし……。  [voice 12674]
    voice "ch26_s_171"
    s "Tabitha ended up like this because of me…{#ch26_s_171}"

    # [SPRITE   lay1     image=+306, level=160, dir=1A]
    # ルイズ：あんたが落ち込んだって、
    voice "ch26_l_071"
    l "You being down won't make Tabitha heal any faster, you know?{#ch26_l_071}"

    # サイト：ま、そうだけどさ……。  [voice 12675]
    voice "ch26_s_172"
    s "Well, yes, but…{#ch26_s_172}"

    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：もう……。
    voice "ch26_l_072"
    l "Honestly… I'll go change the water.{#ch26_l_072}"

    # サイト：うん……。
    voice "ch26_s_173"
    s "Mm… Please.{#ch26_s_173}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+240, level=80]
    $ dissolve_fx("id(240)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+15]
    play music t14 fadein 1.0
    # サイト：（タバサの手って、ちっちゃいな……）
    s "(Tabitha's hands are so small…){#ch26_s_174}"

    # サイト：（こうして手を握って寝顔を見てると、
    s "(Holding her hand and watching her sleep—even I, nursing her, can relax a little…){#ch26_s_175}"

    # サイト：（そういえば……）
    s "(Come to think of it…){#ch26_s_176}"

    # サイト：（俺がギーシュと決闘した後、
    s "(I remember—after my duel with Guiche, Louise nursed me…){#ch26_s_177}"

    # サイト：（あのときのルイズも、こんな感じの
    s "(Was Louise feeling the same way back then…?){#ch26_s_178}"

    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：はい、水を換えてきたわよ。  [voice 6895]
    voice "ch26_l_073"
    l "Here, I've changed the water.{#ch26_l_073}"

    # [SPRITE   lay1     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：……。  [voice 12677]
    voice "ch26_s_179"
    s "…{#ch26_s_179}"

    # [SPRITE   lay1     image=+310, level=160, dir=1A]
    # ルイズ：なっ、なによ？
    voice "ch26_l_074"
    l "Wh-What? Staring at my face like that.{#ch26_l_074}"

    # サイト：いや、なんでもない。  [voice 12678]
    voice "ch26_s_180"
    s "No, it's nothing.{#ch26_s_180}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+241, level=80]
    $ dissolve_fx("id(241)")
    # [TRANS trans("crossfade", 1000)]
    # タバサ：んっ……。  [voice 15719]
    voice "ch26_t_053"
    t "Mm…{#ch26_t_053}"

    # サイト：あっ、タバサ？  [voice 12679]
    voice "ch26_s_181"
    s "Ah, Tabitha?{#ch26_s_181}"

    # タバサ：……ん、んんっ。  [voice 15720]
    voice "ch26_t_054"
    t "…Mm, mmph.{#ch26_t_054}"

    # ルイズ：寝言みたいね。
    voice "ch26_l_075"
    l "Sounds like she's talking in her sleep. She seems a little restless, but is she all right?{#ch26_l_075}"

    # サイト：どうだろ？  [voice 12680]
    voice "ch26_s_182"
    s "Who knows?{#ch26_s_182}"

    # タバサ：……さま。  [voice 15721]
    voice "ch26_t_055"
    t "…Sama.{#ch26_t_055}"

    # サイト：え？
    voice "ch26_s_183"
    s "Eh? What did she say?{#ch26_s_183}"

    # タバサ：……母さま。  [voice 15722]
    voice "ch26_t_056"
    t "…Mother.{#ch26_t_056}"

    # サイト：母さま、って聞こえたような……？  [voice 12682]
    voice "ch26_s_184"
    s "I thought I heard 'mother'…?{#ch26_s_184}"

    # タバサ：母さま、それを飲んじゃだめ。
    voice "ch26_t_057"
    t "Mother, don't drink that. Mother.{#ch26_t_057}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    hide]
    # [SE       se0      play=+82]
    # [BG       stage    image=+43, level=200]
    $ fade_fx("id(43)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # [SE       se0      play=+56]
    # キュルケ：入るわよ？
    voice "ch26_k_032"
    k "I'm coming in. How's Tabitha?{#ch26_k_032}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：モンモランシーの治癒の魔法のおかげで、
    voice "ch26_s_185"
    s "Thanks to Montmorency's healing magic, I think her condition is stable.{#ch26_s_185}"

    # キュルケ：そう、良かった……。  [voice 3529]
    voice "ch26_k_033"
    k "Oh, good…{#ch26_k_033}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：なあ、キュルケ。
    voice "ch26_s_186"
    s "Say, Kirche. There's something I want to ask. Can I?{#ch26_s_186}"

    # キュルケ：タバサのことかしら？
    voice "ch26_k_034"
    k "About Tabitha? Sure.{#ch26_k_034}"

    # サイト：どうしてタバサは、ガリア王国の任務を
    voice "ch26_s_187"
    s "Why does Tabitha keep taking missions from Gallia?{#ch26_s_187}"

    # サイト：ガリア王国は春奈のことを知っていたぐらい、
    voice "ch26_s_188"
    s "Gallia knew about Haruna—it's suspicious. What exactly is Tabitha carrying?{#ch26_s_188}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：それはね……。
    voice "ch26_k_035"
    k "That… I'll have to tell you about Tabitha's family.{#ch26_k_035}"

    # キュルケ：いい？
    voice "ch26_k_036"
    k "Got it? Just between us.{#ch26_k_036}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：あ……、うん。  [voice 12687]
    voice "ch26_s_189"
    s "Ah… Yeah.{#ch26_s_189}"

    # キュルケ：タバサの実家ってね。
    voice "ch26_k_037"
    k "Tabitha's family—they were actually of the royal line that rules Gallia.{#ch26_k_037}"

    # サイト：だった、ってことは……？
    voice "ch26_s_190"
    s "Were, meaning…? Don't tell me…?{#ch26_s_190}"

    # キュルケ：そう、タバサってお姫様なの。  [voice 3534]
    voice "ch26_k_038"
    k "Yes. Tabitha is a princess.{#ch26_k_038}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay1     image=+308, level=160, dir=1A]
    # ルイズ：そうなんだ……。  [voice 6898]
    voice "ch26_l_076"
    l "So that's it…{#ch26_l_076}"

    # キュルケ：でも、権力闘争に巻き込まれたうえに、
    voice "ch26_k_039"
    k "But she got caught up in a power struggle, and her father was assassinated.{#ch26_k_039}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：ひでぇな……。
    voice "ch26_s_191"
    s "That's awful… They'd go that far against family?{#ch26_s_191}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：あら、普通のことよ？
    voice "ch26_k_040"
    k "Oh, that's normal. It happens in every country.{#ch26_k_040}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：そうなのか？  [voice 12690]
    voice "ch26_s_192"
    s "Is that so?{#ch26_s_192}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：でね、母親の方もタバサをかばって、
    voice "ch26_k_041"
    k "And her mother, protecting Tabitha, drank poison as well.{#ch26_k_041}"

    # キュルケ：そのために精神を犯されちゃって……。
    voice "ch26_k_042"
    k "It affected her mind… She no longer seems to recognize Tabitha.{#ch26_k_042}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：母親を毒で？
    voice "ch26_s_193"
    s "Her mother—poisoned? Ah, now I remember…{#ch26_s_193}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay1     image=+302, level=160, dir=1A]
    # ルイズ：タバサが寝言で言っていた……。  [voice 6899]
    voice "ch26_l_077"
    l "The words Tabitha said in her sleep…{#ch26_l_077}"

    # [SPRITE   lay1     hide]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：寝言がどうかしたの？  [voice 3539]
    voice "ch26_k_043"
    k "What about her sleep-talking?{#ch26_k_043}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：タバサが寝言で言ってたんだ。
    voice "ch26_s_194"
    s "She said—'Mother, don't drink that.'{#ch26_s_194}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：そう……。  [voice 3540]
    voice "ch26_k_044"
    k "I see…{#ch26_k_044}"

    # キュルケ：でも、それだけでガリア王国の攻撃の
    voice "ch26_k_045"
    k "But that alone didn't stop Gallia's attacks.{#ch26_k_045}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：依頼という形で、タバサに過酷な任務を
    voice "ch26_k_046"
    k "They kept dumping brutal missions on Tabitha, in the form of 'requests.' And all of them were life-threatening.{#ch26_k_046}"

    # サイト：タバサが……。  [voice 12693]
    voice "ch26_s_195"
    s "Tabitha…{#ch26_s_195}"

    # キュルケ：それでも、文句を言わずに与えられた任務を
    voice "ch26_k_047"
    k "Even so, she carries them out without complaint to protect her mother.{#ch26_k_047}"

    # キュルケ：仇から母親に手を出させないことこそが、
    voice "ch26_k_048"
    k "Keeping the enemy from laying a hand on her mother—that's Tabitha's reason to live.{#ch26_k_048}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そうだったのか……。
    voice "ch26_s_196"
    s "I see… That's how it was…{#ch26_s_196}"

    # サイト：（これじゃあ、春奈をガリア王国へ
    s "(Then I can't tell her to stop taking Haruna to Gallia…){#ch26_s_197}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # → next scene 967
    jump ch26_4b

    # ==== КОНЕЦ ЧАСТИ 4 ====
    jump ch26_4b
    return

