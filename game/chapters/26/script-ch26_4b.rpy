# Глава 26, часть 4b (сцены 967–971): пробуждение Табасы — восстановленный пропуск.
# Источник: ps2_source/chapters/chapter_27_タバサの秘密.txt (SCENE 967-971).

label ch26_4b:
    $ tndl(None)
    $ show_sprites()

label ch26_4b_scene_967:

    # [EVENT_CG event    image=+241, level=80]
    $ dissolve_fx("id(241)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+4]
    play music t3 fadein 1.0
    # タバサ：……ん。  [voice 15724]
    voice "ch26_4b_t_001"
    t "……Mm.{#ch26_4b_t_001}"

    # [EVENT_CG event    image=+243, level=80]
    $ dissolve_fx("id(243)")
    # キュルケ：おはよう、タバサ。  [voice 3545]
    voice "ch26_4b_k_001"
    k "Good morning, Tabitha.{#ch26_4b_k_001}"

    # タバサ：おはよう。  [voice 15725]
    voice "ch26_4b_t_002"
    t "Good morning.{#ch26_4b_t_002}"

    # キュルケ：体の具合はどう？  [voice 3546]
    voice "ch26_4b_k_002"
    k "How are you feeling?{#ch26_4b_k_002}"

    # タバサ：大丈夫、みたい。  [voice 15726]
    voice "ch26_4b_t_003"
    t "I seem to be fine.{#ch26_4b_t_003}"

    # キュルケ：どうして眠ってたのかは思い出せる？  [voice 3547]
    voice "ch26_4b_k_003"
    k "Do you remember why you were asleep?{#ch26_4b_k_003}"

    # タバサ：うん。  [voice 15727]
    voice "ch26_4b_t_004"
    t "Yeah.{#ch26_4b_t_004}"

    # キュルケ：あなたは、アキナとの戦いでダーリンを
    voice "ch26_4b_k_004"
    k "You shielded darling in the fight with Akina and got terrible burns.{#ch26_4b_k_004}"

    # タバサ：うん。  [voice 15728]
    voice "ch26_4b_t_005"
    t "Yeah.{#ch26_4b_t_005}"

    # タバサ：……。
    t "……{#ch26_4b_t_006}"

    # キュルケ：どうしたの？  [voice 3549]
    voice "ch26_4b_k_005"
    k "What's wrong?{#ch26_4b_k_005}"

    # タバサ：分からない。
    voice "ch26_4b_t_007"
    t "I don't know. Why I shielded him.{#ch26_4b_t_007}"

    # キュルケ：……そう。  [voice 3550]
    voice "ch26_4b_k_006"
    k "……I see.{#ch26_4b_k_006}"

    # タバサ：キュルケは分かるの？  [voice 15730]
    voice "ch26_4b_t_008"
    t "Do you understand, Kirche?{#ch26_4b_t_008}"

    # キュルケ：そりゃ、分かるけど……。
    voice "ch26_4b_k_007"
    k "Well, I understand, but…… But it's better that you think about it yourself.{#ch26_4b_k_007}"

    # タバサ：……。
    t "……{#ch26_4b_t_009}"

    # キュルケ：それにしても、あたしったら間の悪いこと
    voice "ch26_4b_k_008"
    k "Even so, I really picked a bad moment. I'm sorry, Tabitha.{#ch26_4b_k_008}"

    # タバサ：どういうこと？  [voice 15731]
    voice "ch26_4b_t_010"
    t "What do you mean?{#ch26_4b_t_010}"

    # キュルケ：大事なお目覚めの瞬間に、あたしなんかが
    voice "ch26_4b_k_009"
    k "At the very moment you woke up, it was me who was nursing you.{#ch26_4b_k_009}"

    # キュルケ：せっかく、今までダーリンがずっと
    voice "ch26_4b_k_010"
    k "Even though darling had been nursing you this whole time……{#ch26_4b_k_010}"

    # タバサ：……。
    t "……{#ch26_4b_t_011}"

    # キュルケ：あはは、そんなに怒らないでよ。  [voice 3555]
    voice "ch26_4b_k_011"
    k "Ahaha, don't be so mad.{#ch26_4b_k_011}"

    # [SE       se0      play=+82]
    # キュルケ：あら、誰か来たみたい。
    voice "ch26_4b_k_012"
    k "Oh, someone's here. Come in~{#ch26_4b_k_012}"

    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [LAYER    lay0     hide]
    # [SPRITE   lay6     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [SE       se0      play=+57]
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：あっ、タバサ！？
    voice "ch26_4b_s_001"
    s "Ah, Tabitha!? You woke up?{#ch26_4b_s_001}"

    # [SPRITE   lay5     x=224, y=0]
    # [LAYER    lay0     image=+618, level=160, dir=1C]
    # タバサ：……。
    t "……{#ch26_4b_t_012}"

    # サイト：良かったぁ……。
    voice "ch26_4b_s_002"
    s "I'm so glad…… You woke up properly. Does anything hurt?{#ch26_4b_s_002}"

    # タバサ：……ない。  [voice 15732]
    voice "ch26_4b_t_013"
    t "……No.{#ch26_4b_t_013}"

    # サイト：そっか……。
    voice "ch26_4b_s_003"
    s "I see…… That's good.{#ch26_4b_s_003}"

    # [LAYER    lay0     image=+616, level=160, dir=1C]
    # タバサ：トリステインは？  [voice 15733]
    voice "ch26_4b_t_014"
    t "Tristain?{#ch26_4b_t_014}"

    # [SPRITE   lay5     image=+427, level=160, dir=2A]
    # サイト：ああ、都ではまだ市街戦が続いてる。
    voice "ch26_4b_s_004"
    s "Ah, the street fighting in the capital is still going on. I went to take a look just now, and it seems to be a complete stalemate.{#ch26_4b_s_004}"

    # サイト：本格的な戦闘が治まるまで、
    voice "ch26_4b_s_005"
    s "I think it'd be better to stay away from the capital until the fighting really settles down…… But I still can't find Haruna.{#ch26_4b_s_005}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：都を離れるわけにはいかないんだ。
    voice "ch26_4b_s_006"
    s "I can't leave the capital. Tabitha, won't you stay with us a little longer?{#ch26_4b_s_006}"

    # タバサ：……うん。  [voice 15734]
    voice "ch26_4b_t_015"
    t "……Yeah.{#ch26_4b_t_015}"

    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：でも、タバサ。
    voice "ch26_4b_s_007"
    s "But, Tabitha. Even if we catch Haruna…… that…… are you going to send her to that Gallia kingdom or whatever?{#ch26_4b_s_007}"

    # [LAYER    lay0     image=+614, level=160, dir=1C]
    # タバサ：……。
    t "……{#ch26_4b_t_016}"

    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # サイト：あっ……。
    voice "ch26_4b_s_008"
    s "Ah…… Hey, what's wrong? Suddenly grabbing my hand and……{#ch26_4b_s_008}"

    # タバサ：……。
    t "……{#ch26_4b_t_017}"

    # サイト：（えーっと、どうしよう……？）
    s "(Um, what should I do……?){#ch26_4b_s_009}"

    menu:
        "Let's stay quiet just like this.{#ch26_4b_c_967_1}":
            jump ch26_4b_scene_968
        "Could this be……?{#ch26_4b_c_967_2}":
            jump ch26_4b_scene_969
        "I have to properly continue the conversation……{#ch26_4b_c_967_3}":
            jump ch26_4b_scene_970

label ch26_4b_scene_968:

    # [LAYER    lay0     image=+614, level=160, dir=1C]
    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+390, level=160, dir=1A]
    # サイト：（まあいいや、黙ってこのままでいよう）
    s "(Well, fine. Let's just stay quiet like this.){#ch26_4b_s_010}"

    # [LAYER    lay0     image=+616, level=160, dir=1C]
    # タバサ：……。
    t "……{#ch26_4b_t_018}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+240, level=80]
    $ dissolve_fx("id(240)")
    # [TRANS trans("crossfade", 1000)]
    # → next scene 971
    jump ch26_4b_scene_971

label ch26_4b_scene_969:

    # [LAYER    lay0     image=+614, level=160, dir=1C]
    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # サイト：（ひょっとして、これは……）
    s "(Could this be……?){#ch26_4b_s_011}"

    # サイト：（タバサからのある種のメッセージ！？
    s "(Some kind of message from Tabitha!? And what's more, it's like…… between a man and a woman…!!){#ch26_4b_s_012}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # キュルケ：ダーリン……。  [voice 3557]
    voice "ch26_4b_k_013"
    k "Darling……{#ch26_4b_k_013}"

    # サイト：な、なにかな？  [voice 12703]
    voice "ch26_4b_s_013"
    s "Wh-what is it?{#ch26_4b_s_013}"

    # キュルケ：今、だらしのないこと考えてたんでしょ？  [voice 3558]
    voice "ch26_4b_k_014"
    k "You were thinking something improper just now, weren't you?{#ch26_4b_k_014}"

    # [SPRITE   lay5     image=+431, level=160, dir=2A]
    # サイト：あの、なんのことでしょうか？  [voice 12704]
    voice "ch26_4b_s_014"
    s "Um, what could you mean?{#ch26_4b_s_014}"

    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：ごまかそうとしたってダメよ。
    voice "ch26_4b_k_015"
    k "You can't bluff your way out of it. It was written all over your face.{#ch26_4b_k_015}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：す、すみません……。  [voice 12705]
    voice "ch26_4b_s_015"
    s "I-I'm sorry……{#ch26_4b_s_015}"

    # [SPRITE   lay5     hide]
    # [SPRITE   lay6     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+240, level=80]
    $ dissolve_fx("id(240)")
    # [TRANS trans("crossfade", 1000)]
    # → next scene 971
    jump ch26_4b_scene_971

label ch26_4b_scene_970:

    # [SPRITE   lay5     image=+398, level=160, dir=1A]
    # [LAYER    lay0     image=+614, level=160, dir=1C]
    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [SPRITE   lay5     image=+396, level=160, dir=1A]
    # サイト：（ちゃんと話の続きをしなくちゃ……）
    s "(I have to properly continue the conversation……){#ch26_4b_s_016}"

    # サイト：で、春奈のことなんだけど……。  [voice 12706]
    voice "ch26_4b_s_017"
    s "So, about Haruna……{#ch26_4b_s_017}"

    # [LAYER    lay0     image=+616, level=160, dir=1C]
    # タバサ：……。
    t "……{#ch26_4b_t_019}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     image=+680, level=160, dir=1A]
    # キュルケ：ちょっと、ダーリン。
    voice "ch26_4b_k_016"
    k "Now, darling. Right now you should just stay quiet and go along with her.{#ch26_4b_k_016}"

    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # サイト：そ、そうか……。  [voice 12707]
    voice "ch26_4b_s_018"
    s "I-I see……{#ch26_4b_s_018}"

    # [SPRITE   lay6     hide]
    # [LAYER    lay0     image=+616, level=160, dir=1C]
    # タバサ：……。
    t "……{#ch26_4b_t_020}"

    # [SPRITE   lay5     hide]
    # [LAYER    lay0     hide]
    # [BG       stage    hide]
    # [EVENT_CG event    image=+240, level=80]
    $ dissolve_fx("id(240)")
    # [TRANS trans("crossfade", 1000)]
    # → next scene 971
    jump ch26_4b_scene_971

label ch26_4b_scene_971:

    # [BGM      bgm      play=+9]
    play music t8 fadein 1.0
    # [EVENT_CG event    image=+240, level=80]
    $ dissolve_fx("id(240)")
    # タバサ：……。
    t "……{#ch26_4b_t_021}"

    # サイト：あ、あれ？  [voice 12708]
    voice "ch26_4b_s_019"
    s "H-huh?{#ch26_4b_s_019}"

    # キュルケ：どうやらまた眠っちゃったみたいね。  [voice 3561]
    voice "ch26_4b_k_017"
    k "Looks like she's fallen asleep again.{#ch26_4b_k_017}"

    # サイト：だ、大丈夫なのか？  [voice 12709]
    voice "ch26_4b_s_020"
    s "I-Is she going to be okay?{#ch26_4b_s_020}"

    # キュルケ：大丈夫でしょ。
    voice "ch26_4b_k_018"
    k "She'll be fine. She did wake up once, after all.{#ch26_4b_k_018}"

    # キュルケ：そんなに心配だって言うのなら、
    voice "ch26_4b_k_019"
    k "If you're that worried, then hold her hand for a while.{#ch26_4b_k_019}"

    # キュルケ：きっとタバサが、安心して眠っていられる
    voice "ch26_4b_k_020"
    k "Because I'm sure that way Tabitha can sleep in peace.{#ch26_4b_k_020}"

    # サイト：そ、そうだな……。  [voice 12710]
    voice "ch26_4b_s_021"
    s "Y-You're right……{#ch26_4b_s_021}"

    # キュルケ：それより、問題山積みって感じよね。  [voice 3565]
    voice "ch26_4b_k_021"
    k "Besides, it feels like the problems are piling up, doesn't it?{#ch26_4b_k_021}"

    # サイト：ああ、どうしたもんかなぁ。
    voice "ch26_4b_s_022"
    s "Ah, what to do…… Haruna's case…… and Gallia's case.{#ch26_4b_s_022}"

    # [LAYER    lay0     hide]
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [EVENT_CG event    hide]
    # [BG       stage    image=+41, level=200]
    $ fade_fx("id(41)")
    # [TRANS trans("crossfade", 1000)]
    # [SPRITE   lay6     image=+682, level=160, dir=1A]
    # [SPRITE   lay5     image=+429, level=160, dir=2A]
    # キュルケ：……。  [voice 3566]
    voice "ch26_4b_k_022"
    k "……{#ch26_4b_k_022}"

    # サイト：なんだよ、その顔は？  [voice 12712]
    voice "ch26_4b_s_023"
    s "What's with that face?{#ch26_4b_s_023}"

    # キュルケ：ダーリンを想うのって大変ね。
    voice "ch26_4b_k_023"
    k "Longing for darling is tough, isn't it? Maybe I shouldn't give you up to Tabitha — maybe I'll just steal you away?{#ch26_4b_k_023}"

    # サイト：……？  [voice 12713]
    voice "ch26_4b_s_024"
    s "……?{#ch26_4b_s_024}"

    # キュルケ：もう……。  [voice 3568]
    voice "ch26_4b_k_024"
    k "Honestly……{#ch26_4b_k_024}"

    # [SE       se1      stop=1]
    # [BGM      bgm      stop=1000]
    stop music fadeout 1.0
    # [SPRITE   lay6     hide]
    # [SPRITE   lay5     hide]
    # [BG       stage    hide]
    # 【デート】タバサ → scene 1219
    jump ch26_5

    # 【デート】 → scene 972
    # 【デート進行】 → scene 972 (выход в следующую главу)
    jump ch27

    # ==== КОНЕЦ ЧАСТИ 4b ====
    jump ch26_5
    return

