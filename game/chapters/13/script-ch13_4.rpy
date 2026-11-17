# Глава 13, часть 4 (сцены 1184–1188): волейбол, « demonic ball».
# Источник: ps2_source/chapters/chapter_14_炎の予感.txt (SCENE 1184-1188).

label ch13_4:
    $ tndl(None)
    $ show_sprites()

label ch13_4_scene_1184:

    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+8]
    play music t7 fadein 1.0
    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：あ～～、いいお天気……。  [voice 2838]
    voice "ch13_k_125"
    k "Ah, what lovely weather…{#ch13_k_125}"

    # [SPRITE   lay6     x=-96, y=0]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：はぁ、呑気なんだから。  [voice 9048]
    voice "ch13_s_133"
    s "Sigh, you're so carefree.{#ch13_s_133}"

    # [SPRITE   lay6     image=+713, level=160, dir=2A]
    # キュルケ：な、なによ。  [voice 2839]
    voice "ch13_k_126"
    k "W-What's that!?{#ch13_k_126}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ルイズに負けたら何をされるか
    voice "ch13_s_134"
    s "You don't know what Louise will do to us if we lose.{#ch13_s_134}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：大丈夫よ。
    voice "ch13_k_127"
    k "It's fine. Darling is with me.{#ch13_k_127}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：いや、だから……。  [voice 9050]
    voice "ch13_s_135"
    s "Yeah, that's what I mean…{#ch13_s_135}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：ねえ、何か暇つぶしにダーリンの国の遊びを
    voice "ch13_k_128"
    k "Hey, won't you teach me a game from your country to pass the time?{#ch13_k_128}"

    # サイト：えー。  [voice 9051]
    voice "ch13_s_136"
    s "Eh?{#ch13_s_136}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：もう！
    voice "ch13_k_129"
    k "Come on, now's the time for that. We need to relax a little.{#ch13_k_129}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（……そんなこと急に言われても、
    s "(You can't just spring that on me, you moody girl…){#ch13_s_137}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：しょうがないなぁ。
    voice "ch13_s_138"
    s "I suppose so. What should we do?{#ch13_s_138}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：そうこなくっちゃ。  [voice 2843]
    voice "ch13_k_130"
    k "That's the spirit.{#ch13_k_130}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：やっぱり、女の子の遊びとかのほうが
    voice "ch13_s_139"
    s "Maybe a girl's game would be better…?{#ch13_s_139}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：ん～～、何でもいいわよ？  [voice 2844]
    voice "ch13_k_131"
    k "Mm, anything's fine.{#ch13_k_131}"

    # [SPRITE   lay5     image=+423, level=160, dir=2A]
    # サイト：とりあえず定番といえば……。
    voice "ch13_s_140"
    s "Well, the classic would be… volleyball, I guess…?{#ch13_s_140}"

    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：バレーボール？  [voice 2845]
    voice "ch13_k_132"
    k "Volleyball?{#ch13_k_132}"

    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：うん、俺の国の球技。  [voice 9055]
    voice "ch13_s_141"
    s "Yeah, a ball game from my country.{#ch13_s_141}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：へー。  [voice 2846]
    voice "ch13_k_133"
    k "Huh.{#ch13_k_133}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # null：………。 (no voice)
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：とはいったものの……。
    voice "ch13_s_142"
    s "That said, we're too few for volleyball. Let's practice setting.{#ch13_s_142}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：トス？  [voice 2847]
    voice "ch13_k_134"
    k "Setting?{#ch13_k_134}"

    # サイト：簡単に言うと、手で持ったりしないように、
    voice "ch13_s_143"
    s "Simply put, you pass the ball to the other person without holding it.{#ch13_s_143}"

    # [SPRITE   lay5     image=+392, level=160, dir=1A]
    # サイト：こんな風にっと。  [voice 9058]
    voice "ch13_s_144"
    s "Like this.{#ch13_s_144}"

    # [SE       se0      play=+80]
    # [SPRITE   lay6     image=+709, level=160, dir=2A]
    # キュルケ：へー。
    voice "ch13_k_135"
    k "Huh. I think I get it.{#ch13_k_135}"

    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # サイト：いくぞ！
    voice "ch13_s_145"
    s "Here we go! Up!{#ch13_s_145}"

    # [SE       se0      play=+80]
    # null：ぽ～～ん！
    th "Pon!{#ch13_th_003}"

    # [SPRITE   lay6     image=+678, level=160, dir=1A]
    # キュルケ：きゃっ！  [voice 2849]
    voice "ch13_k_136"
    k "Eek!{#ch13_k_136}"

    # [SE       se0      play=+80]
    # null：ぽ～～ん！
    th "Pon!{#ch13_th_004}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：あれ？
    voice "ch13_ha_003"
    ha "Oh? Hiraga-kun, are you playing volleyball?{#ch13_ha_003}"

    # [SPRITE   lay7     x=-96, y=0]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：あ、春奈。
    voice "ch13_s_146"
    s "Ah, Haruna. Kirche asked me to teach her something to pass the time.{#ch13_s_146}"

    # [SPRITE   lay7     image=+957, level=160, dir=1A]
    # ハルナ：こんなところで遊んでて、知らないよ。  [voice 1700]
    voice "ch13_ha_004"
    ha "Playing here of all places… I don't know you.{#ch13_ha_004}"

    # [SPRITE   lay7     image=+951, level=160, dir=1A]
    # ハルナ：ルイズさん、勝ったら逆立ちのままパスタを
    voice "ch13_ha_005"
    ha "Louise-san was fuming, saying she'd make you eat pasta doing handstands if she wins.{#ch13_ha_005}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：げ、まじですか？  [voice 9061]
    voice "ch13_s_147"
    s "Ugh, seriously?{#ch13_s_147}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：大丈夫、大丈夫。
    voice "ch13_k_137"
    k "It's fine, it's fine. I've got it all figured out.{#ch13_k_137}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：本当かよ。  [voice 9062]
    voice "ch13_s_148"
    s "Really?{#ch13_s_148}"

    # [SPRITE   lay6     image=+676, level=160, dir=1A]
    # キュルケ：それより、ハルナ。
    voice "ch13_k_138"
    k "More importantly, Haruna. Will you practice setting with me?{#ch13_k_138}"

    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：ダーリンだと、どうも下手みたい。  [voice 2852]
    voice "ch13_k_139"
    k "With darling, I just can't seem to do it.{#ch13_k_139}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そりゃ、悪かったですね。  [voice 9063]
    voice "ch13_s_149"
    s "Well, excuse me.{#ch13_s_149}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     image=+986, level=160, dir=2A]
    # ハルナ：うん、いいよ。
    voice "ch13_ha_006"
    ha "Sure. I wanted to move my body a bit anyway.{#ch13_ha_006}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # null：………。 (no voice)
    # [EVENT_CG event    image=+250, level=80]
    $ dissolve_fx("id(250)")
    # [TRANS trans("crossfade", 1000)]
    # [SE       se0      play=+80]
    # サイト：（さすがキュルケ。
    s "(Kirche's coordination is great… wait!){#ch13_s_150}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SE       se0      play=+80]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # サイト：（な、なんですか、あの……、
    s "(W-What are those two things swaying at Kirche's chest…?){#ch13_s_151}"

    # キュルケ：あはは。
    voice "ch13_k_140"
    k "Ahahaha. Quite interesting, isn't it?{#ch13_k_140}"

    # [SE       se0      play=+80]
    # null：ぽ～～ん！
    th "Pon!{#ch13_th_005}"

    # ハルナ：そーれ！  [voice 1703]
    voice "ch13_ha_007"
    ha "There!{#ch13_ha_007}"

    # [SE       se0      play=+80]
    # サイト：（……ゆ、揺れる……魔球？
    s "(…A swaying… demonic ball? The charm and the thrill of it…){#ch13_s_152}"

    # [SE       se0      play=+80]
    # サイト：（しまった、この世界は危険だらけで
    s "This world is full of danger!{#ch13_s_153}"

    menu:
        "Look away from Kirche{#ch13_4_c_1184_1}":
            jump ch13_4_scene_1185
        "Not look away from Kirche{#ch13_4_c_1184_2}":
            jump ch13_4_scene_1186
        "…Is that killing intent?{#ch13_4_c_1184_3}":
            jump ch13_4_scene_1187

label ch13_4_scene_1185:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+250, level=80]
    $ dissolve_fx("id(250)")
    # [SPRITE   lay5     hide]
    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+88, level=200]
    $ fade_fx("id(88)")
    # [TRANS trans("crossfade", 1000)]
    # サイト：み、見ちゃダメだ！  [voice 9064]
    voice "ch13_s_154"
    s "D-Don't look!{#ch13_s_154}"

    # キュルケ：ダーリン、危ないっ！  [voice 2854]
    voice "ch13_k_141"
    k "Darling, look out!{#ch13_k_141}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay6     hide, reset]
    # サイト：ぐはっ！  [voice 9065]
    voice "ch13_s_155"
    s "Guh!{#ch13_s_155}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     x=144, y=416]
    # [SPRITE   lay7     image=+988, level=160, dir=2A]
    # ハルナ：もう、平賀くん。
    voice "ch13_ha_008"
    ha "Really, Hiraga-kun. What are you looking at with that red face?{#ch13_ha_008}"

    # [SPRITE   lay7     x=-96, y=0]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：あ、あてないでください。
    voice "ch13_s_156"
    s "D-Don't guess, Haruna-chan.{#ch13_s_156}"

    # ハルナ：もう、平賀くんなんて、知らない。  [voice 1705]
    voice "ch13_ha_009"
    ha "I don't know Hiraga-kun anymore.{#ch13_ha_009}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：はうう。
    voice "ch13_s_157"
    s "Eeeh. S-Sorry…{#ch13_s_157}"

    # → next scene 1188
    jump ch14

label ch13_4_scene_1186:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+250, level=80]
    $ dissolve_fx("id(250)")
    # サイト：（うわ、目を離すことができない。
    s "(Wow, I can't look away. Is this what charm is…?){#ch13_s_158}"

    # キュルケ：ダーリン、危ないっ！  [voice 2855]
    voice "ch13_k_142"
    k "Darling, look out!{#ch13_k_142}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay6     hide, reset]
    # サイト：ぐはっ！  [voice 9068]
    voice "ch13_s_159"
    s "Guh!{#ch13_s_159}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：な、何してるのよ。
    voice "ch13_k_143"
    k "What are you doing, getting between Haruna and me?{#ch13_k_143}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：え、ええと、そにょ……。  [voice 9069]
    voice "ch13_s_160"
    s "W-Well, er…{#ch13_s_160}"

    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：……うふふ。
    voice "ch13_k_144"
    k "…Ufufu. Where were you looking?{#ch13_k_144}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：い、いえないばしょです……。  [voice 9070]
    voice "ch13_s_161"
    s "S-Somewhere I can't say…{#ch13_s_161}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+988, level=160, dir=2A]
    # ハルナ：平賀くんのエッチ！  [voice 1706]
    voice "ch13_ha_010"
    ha "Hiraga-kun's pervert!{#ch13_ha_010}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：はうう。
    voice "ch13_s_162"
    s "Eeeh. S-Sorry…{#ch13_s_162}"

    # → next scene 1188
    jump ch14

label ch13_4_scene_1187:

    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [EVENT_CG event    image=+250, level=80]
    $ dissolve_fx("id(250)")
    # サイト：……ん？
    voice "ch13_s_163"
    s "…Hm? What's with this pressure!?{#ch13_s_163}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay7     image=+989, level=140, dir=2A]
    # ハルナ：……。  [voice 1707]
    voice "ch13_ha_011"
    ha "…{#ch13_ha_011}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     image=+394, level=160, dir=1A]
    # [SE       se0      play=+62]
    # [BG       stage    vibrate=14]
    # [EVENT_CG event    vibrate=14]
    # [SPRITE   lay7     vibrate=14]
    # [SPRITE   lay5     vibrate=14]
    # [SPRITE   lay6     vibrate=14]
    # [VIBRATE vibrate(2)]
    $ shake_fx(duration=0.8)
    # [BG       stage    reset]
    # [EVENT_CG event    hide, reset]
    # [SPRITE   lay7     hide, reset]
    # [SPRITE   lay5     reset]
    # [SPRITE   lay6     hide, reset]
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：ぐはっ！  [voice 9073]
    voice "ch13_s_164"
    s "Guh!{#ch13_s_164}"

    # [SPRITE   lay5     x=224, y=0]
    # [SPRITE   lay7     image=+988, level=160, dir=2A]
    # ハルナ：もう、知らない。  [voice 1708]
    voice "ch13_ha_012"
    ha "I don't know.{#ch13_ha_012}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：痛たた、いやその……。  [voice 9074]
    voice "ch13_s_165"
    s "Ouch, I mean…{#ch13_s_165}"

    # → next scene 1188
    jump ch14

label ch13_4_scene_1188:

    # [SPRITE   lay7     image=+988, level=160, dir=2A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # [BGM      bgm      play=+30]
    play music t29 fadein 1.0
    # [BG       stage    image=+58, level=200]
    $ fade_fx("town_square")
    # [SPRITE   lay7     image=+955, level=160, dir=1A]
    # ハルナ：キュルケさん、別な場所で遊びません？
    voice "ch13_ha_013"
    ha "Kirche-san, shall we play somewhere else? Hiraga-kun keeps looking at strange places.{#ch13_ha_013}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：あわわ……。  [voice 9075]
    voice "ch13_s_166"
    s "Eep…{#ch13_s_166}"

    # [SPRITE   lay7     hide]
    # [SPRITE   lay6     image=+711, level=160, dir=2A]
    # キュルケ：えー。
    voice "ch13_k_145"
    k "Eh. I don't mind being watched…{#ch13_k_145}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：いや、あの……。  [voice 9076]
    voice "ch13_s_167"
    s "No, I mean…{#ch13_s_167}"

    # [SPRITE   lay6     hide]
    # [SPRITE   lay7     image=+955, level=160, dir=1A]
    # ハルナ：ふん。  [voice 1710]
    voice "ch13_ha_014"
    ha "Hmph.{#ch13_ha_014}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：あはは……。  [voice 9077]
    voice "ch13_s_168"
    s "Ahahaha…{#ch13_s_168}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay7     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [COFFEE]
    $ pause(1.0)
    # → next scene 578
    jump ch14

    # ==== КОНЕЦ ЧАСТИ 4 ====
    jump ch14
    return

