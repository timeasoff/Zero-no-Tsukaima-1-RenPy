# -*- coding: utf-8 -*-
# Генератор TL-блоков и манифеста голосов для главы 3, части 2 (сцены 147–157).
# old = точная строка EN-базы из script-ch3_2.rpy; ja_new — дословно из канона
# (переносы строк склеены, мысли в （ ）); ru_new — по JA.
# Дополнительно: добавляет 90 строк ch3.2_* в references/voice_id_map.csv.
# Запуск: python tools/gen_p2_tl.py
import io

# (bucket, old, ja_new, ru_new)
ROWS = [
    # ==== SCENE 147 ====
    ("dialogs", "Well then, Miss Valiere. Haruna-san, I have work to do, so I'll be going on ahead.",
     "それでは、ミス・ヴァリエール。ハルナさん。わたくしは仕事がありますのでお先に。",
     "Ну что ж, мадемуазель Вальер. Харуна-сан, у меня дела, так что пойду вперёд."),
    ("dialogs", "All right. Give it your all at work.",
     "分かったわ。お仕事に励みなさい。",
     "Хорошо. Работай усердно."),
    ("dialogs", "Then, if you'll excuse me.",
     "では、失礼いたします。",
     "Тогда разрешите откланяться."),
    ("dialogs", "Ah, Siesta — you're off to work?",
     "あ、シエスタ、仕事なんだ？",
     "А, Сиеста — ты на работу?"),
    ("dialogs", "Ah, Saito-san. Pardon me.",
     "あ、サイトさん。失礼します。",
     "А, Сайто-сан. Прошу прощения."),
    ("dialogs", "Good luck at work!",
     "お仕事、頑張ってね。",
     "Удачи на работе!"),
    ("dialogs", "Yes, I will. Well then.",
     "はい、頑張ります。それでは。",
     "Да, постараюсь. Тогда пойду."),
    ("dialogs", "Saito, I'm sorry for making you go outside.",
     "サイト、わるかったわね。外に出てもらって。",
     "Сайто, виновата, что заставила тебя выйти."),
    ("dialogs", "Louise, don't worry about it.",
     "ルイズ、気にするなよ。",
     "Луиза, не переживай."),
    ("dialogs", "I'm actually kind of happy — I was thinking you might be starting to see me as a man.",
     "俺のことをそろそろ男性として見てくれてるのかなぁってちょっとはうれしくなってるんだから。",
     "Я даже немного рад — думал, ты понемногу начинаешь смотреть на меня как на мужчину."),
    ("dialogs", "I wasn't thinking anything of the sort. Propriety, that's all — propriety!",
     "わたしはどうも思って無いわ。体面よ、体面。",
     "Я ничего такого не думала. Дело в приличиях — в приличиях!"),
    ("dialogs", "Sure, sure. Is that so…",
     "へーへー。そうですか……。",
     "Угу-угу. Неужели…"),
    ("dialogs", "Come to think of it, Haruna — how are you feeling?",
     "そういえば、春奈。具合はどう？",
     "Кстати, Харуна — как ты себя чувствуешь?"),
    ("dialogs", "Yeah, I'm fine. Sorry for making you worry, Hiraga-kun.",
     "うん、大丈夫。平賀くん、心配してもらってごめんね。",
     "Да, в порядке. Хирага-кун, прости, что из-за меня волновался."),
    ("dialogs", "Glad to hear it… Don't push yourself. There are no classes anyway, so take it easy.",
     "ならいいんだけど……。無理はするなよ。学校もないし、ゆっくりしてていいんだからさ。",
     "Раз так хорошо… Не перенапрягайся. Занятий-то всё равно нет — отдыхай спокойно."),
    ("dialogs", "Yeah… Thanks.",
     "うん……。ありがとう。",
     "Да… Спасибо."),
    ("dialogs", "Uuuugh.",
     "うーー。",
     "Уууу."),
    ("dialogs", "What's wrong, Louise?",
     "どうした、ルイズ。",
     "Что такое, Луиза?"),
    # ==== SCENE 148 ====
    ("dialogs", "Are you feeling under the weather?",
     "もしかして、体調が悪いのか？",
     "Может, тебе нездоровится?"),
    ("dialogs", "O-of course not! I was just humming a little.",
     "そ、そんなはずないでしょ？ただうなっただけよ。",
     "К-конечно, нет! Я просто пробурчала."),
    ("dialogs", "You wouldn't just hum for no reason, right?",
     "何も無いのにうなったりしないだろ？",
     "Без причины же не пробурчешь, да?"),
    ("dialogs", "I'm fine, don't worry about it.",
     "大丈夫よ、気にしないで。",
     "Всё в порядке, не переживай."),
    ("dialogs", "Well, all right… If you're feeling sick, say so right away, okay?",
     "まぁ、いいけど……。体調が悪いなら、すぐに言えよ。",
     "Ну, ладно… Если нездорова — сразу говори, ладно?"),
    ("dialogs", "I get it!",
     "分かったわよ！",
     "Понятно!"),
    # ==== SCENE 149 ====
    ("dialogs", "Are you sleepy?",
     "もしかして、眠いのか？",
     "Может, клонит в сон?"),
    ("dialogs", "How do you figure?",
     "なんでそうなるのよ？",
     "Откуда ты это взял?"),
    ("dialogs", "Nah. Just a feeling.",
     "いやー。なんとなく。",
     "Да нет. Просто так."),
    ("dialogs", "Don't go deciding how someone feels just on a whim.",
     "なんとなくで、人の体調を勝手に決めないでよね。",
     "Не решай за других, как они себя чувствуют, просто по наитию!"),
    ("dialogs", "Yeah, yeah.{#ch3.2_s_014}",
     "へいへい。",
     "Да-да."),
    # ==== SCENE 150 ====
    ("dialogs", "Are you hungry? It's still a while until lunch.",
     "もしかして、お腹が減ったのか？昼ご飯までまだ時間があるぞ。",
     "Может, проголодалась? До обеда ещё далеко."),
    ("dialogs", "It's not like I'm starving like you. Don't lump me in with you!",
     "あんたみたいにガツガツしてないわよ。一緒にしないで！",
     "Я не такая прожорливая, как ты! Не сравнивай меня с собой!"),
    ("dialogs", "I see, I see.",
     "さいですか。",
     "Понятненько."),
    # ==== SCENE 151 ====
    ("dialogs", "Well then, I've got things to do, so I'm heading out first. Saito, come to the classroom after.",
     "それじゃあ、わたしは用があるから先に行ってるわね。サイトは後から教室に来なさい。",
     "Ну а у меня дела, так что пойду вперёд. Сайто, приходи в класс потом."),
    ("dialogs", "Huh? Why?{#ch3.2_s_017}",
     "えっ、なんで？",
     "А? Почему?"),
    ("dialogs", "…A-anyway, you don't have to come, Saito!",
     "……。と、とにかく、サイトは来なくていーのっ！",
     "…В-в общем, тебе идти необязательно, Сайто!"),
    ("dialogs", "That's not even a reason.",
     "理由になってないし。",
     "Это даже не причина."),
    ("dialogs", "And you, Haruna! You're a patient, so you'd better stay put and rest, okay!?",
     "それから、ハルナ！あなた病人なんだから、ちゃんと大人しく寝てなきゃダメなんだからね！",
     "И ты, Харуна! Ты больная — так что лежи смирно и отдыхай, ясно!?"),
    ("dialogs", "Y-yes…",
     "は、はい……。",
     "Д-да…"),
    ("dialogs", "Louise — she's worried about Haruna, in her own way, isn't she.",
     "ルイズのやつ、なんだかんだで春奈のこと、心配してんだなぁ。",
     "Видно, Луиза по-своему волнуется за Харуну."),
    ("dialogs", "Do you think so…",
     "そうなのかな……。",
     "Ты так думаешь…"),
    ("dialogs", "Hm? Did you say something just now?",
     "ん？今、なんか言った？",
     "А? Ты что-то сказала?"),
    ("dialogs", "Nope, nothing.",
     "ううん、なんでもない。",
     "Нет, ничего."),
    ("dialogs", "Still — what do you suppose Louise is up to?",
     "それにしても、ルイズのやつ。何の用事があるんだろ？",
     "Впрочем, что это за дела у Луизы, интересно?"),
    # ==== SCENE 152 ====
    ("dialogs", "Grr, this is no fun! For all that he's my familiar, all he does is fuss over Haruna!!",
     "もうっ、面白くない！わたしの使い魔のクセに、ハルナの面倒ばっかり見ちゃってさ！！",
     "Фу, неинтересно! Мой фамильяр, а заботится лишь о Харуне!!"),
    ("dialogs", "Siesta, you think so too, right?",
     "シエスタ、あなたもそう思うでしょ？",
     "Сиеста, ты ведь тоже так думаешь?"),
    ("dialogs", "Y-yes… It's not fair of Haruna-san to fake an illness and have Saito-san fuss over her.",
     "は、はい……。ハルナさん、病気のふりをしてサイトさんに面倒見てもらうだなんてずるいです。",
     "Д-да… Это нечестно со стороны Харуна-сан — симулировать и устраивать, чтобы Сайто-сан о ней заботился."),
    ("dialogs", "But maybe I'm a little happy about it. Thanks to that I got to sleep next to Saito-san… …Hehe.",
     "でも、ちょっと嬉しいかも。おかげでサイトさんの隣で寝られたし……。……うふふ。",
     "Но мне, может, даже немного радостно — благодаря этому я могла спать рядом с Сайто-сан… …Уфуфу."),
    ("dialogs", "Eh? Did you say something?",
     "えっ、今なんか言った？",
     "А? Что-то сказала?"),
    ("dialogs", "No, nothing…",
     "いえ、なんでも……。",
     "Нет, ничего…"),
    ("dialogs", "Unforgivable~! Saito didn't have to get taken in by Haruna's little feigned illness like that!!",
     "許せなぁーい！サイトったら、ハルナのあんな仮病に騙されなくたっていいのにーっ！！",
     "Непростимо-о! Сайто ведь мог и не вестись на такую симуляцию Харуны!!"),
    ("dialogs", "Miss Valiere. I believe we should make Haruna-san confess that she's faking.",
     "ミス・ヴァリエール。わたくしは、仮病だということをハルナさんに白状してもらいたいと思います。",
     "Мадемуазель Вальер. Я бы хотела, чтобы Харуна-сан созналась, что симулирует."),
    ("dialogs", "But wouldn't it be faster if we just told Saito ourselves?",
     "でも、それって、わたし達がサイトにそのことを言ったほうが早くない？",
     "Но разве быстрее не сказать это Сайто самим?"),
    ("dialogs", "Do you think so? In the end, it's someone else's illness. There's no way others could tell.",
     "そうでしょうか？結局は他人の病気。他の人が分かるはずがありません。",
     "Вы уверены? Это всё-таки болезнь другого человека. Посторонние вряд ли её распознают."),
    ("dialogs", "Then we'll just use magic. There's bound to be a perfect spell.",
     "なら、魔法を使うだけよ。きっとぴったりな魔法があるはずだわ。",
     "Тогда просто используем магию. Наверняка найдётся подходящее заклинание."),
    ("dialogs", "Um, Miss Valiere — if it's all right, I have a good idea…",
     "あの、ミス・ヴァリエール。よろしければ、わたくしにいい考えがあります……。",
     "Мадемуазель Вальер, если позволите — у меня есть хорошая идея…"),
    ("dialogs", "Eh? What is it, what is it!?",
     "えっ、どんなどんな！？",
     "А? Какая, какая!?"),
    ("dialogs", "What if we…….……how does that sound?",
     "ここは……。……。……というのは、いかがですか？",
     "А если…….…… Как вам такое?"),
    ("dialogs", "…I like that! All right, let's do it!",
     "……いいわね、それ！分かったわ、実行しましょう！",
     "…Мне нравится! Хорошо, приступим!"),
    ("dialogs", "Then I'll get things ready later…",
     "では、後ほど準備を……。",
     "Тогда позже всё подготовлю…"),
    ("dialogs", "Nfufufufu… Just you watch, Haruna! I'll expose your fake illness completely, I swear it~!!",
     "んふふふふ……見てらっしゃい、ハルナ！あなたの仮病、ばっちり暴いてみせちゃうんだからぁ～っ！！",
     "Нфуфуфуфу… Погляди-ка, Харуна! Я непременно разоблачу твою симуляцию~!!"),
    # ==== SCENE 153 ====
    ("thoughs", "As always, I have no idea what the lesson's about.",
     "（相変わらず、授業の内容は　なんだか分からない）",
     "Как обычно, я понятия не имею, о чём этот урок."),
    ("thoughs", "Nobles who sit through lessons like this every day really have it tough. Well, I mostly sleep through it myself, but…",
     "（こんな授業を毎日受けてる貴族って　ほんと大変なんだな。　まぁ、ほとんど俺は寝てるわけだけど……）",
     "Аристократам, что каждый день ходят на такие уроки, правда непросто. Ну, я в основном сплю, но…"),
    ("thoughs", "But Louise seems to be enjoying today's lesson an awful lot. Did something fun happen or what?",
     "（けど、今日のルイズはずいぶん楽しそうに　授業を受けてるな。　なんか、楽しいことでもあったのか？）",
     "Но Луиза сегодня на уроке какая-то слишком весёлая. Не случилось ли чего забавного?"),
    ("dialogs", "…Hm? What's with the gawking? Is there something on my face?",
     "……ん？なによ、人の顔をじろじろと見ちゃって。何かついてる？",
     "…А? Чего мне в лицо уставился? У меня что-то прилипло?"),
    ("dialogs", "No, it's just — you seem to be enjoying the lesson more than usual today. Did something fun happen?",
     "いや、今日は普段よりも楽しそうに授業受けてるなって。何か面白いことでもあったのか？",
     "Нет, просто ты сегодня на уроке веселишься больше обычного. Что-то забавное случилось?"),
    ("dialogs", "Ghk. N-nothing at all!",
     "ぎくっ。べ、別になんでもないわよっ！",
     "Гх. Н-ничего такого!"),
    ("dialogs", "Really? You're really not hiding anything from me?",
     "本当か？本当に俺に隠し事してないか？",
     "Правда? Ты правда ничего от меня не скрываешь?"),
    ("dialogs", "I-I'm not hiding anything.",
     "な、何も隠してなんていないわよ。",
     "Я-я ничего не скрываю."),
    ("dialogs", "Besides, Saito — you're the one who's dying to know how Haruna is, aren't you!?",
     "それより、サイト。あんたこそ、ハルナの様子が気になって仕方がないんじゃないのっ！？",
     "И вообще, Сайто — сам ты не можешь не думать о Харуне, не так ли!?"),
    ("dialogs", "What's with you, Louise? Bringing up Haruna out of nowhere…",
     "どうしたんだよルイズ。急に、春奈のこと言い出して……。",
     "Что с тобой, Луиза? Вдруг ни с чего про Харуну…"),
    # ==== SCENE 154 ====
    ("dialogs", "I mean… she's probably fine.",
     "別に……まあ、大丈夫だろうし。",
     "Ну… она вроде бы в порядке."),
    ("dialogs", "Eh, Saito — do you really mean that?",
     "えっ、サイト。あなた本気でそう言ってるの？",
     "А? Сайто — ты это всерьёз говоришь?"),
    ("dialogs", "What's there to be serious about? She's sleeping in your room, so there's no problem, right?",
     "本気も何も、おまえの部屋で寝てんだから、なにも問題ないだろ。",
     "Не о чём тут волноваться — она же в твоей комнате спит, всё в порядке, да?"),
    ("dialogs", "Besides, Siesta said she'd look after her whenever she has free time…",
     "それにシエスタが時間が空いたら、見てくれるって言ってるんだし……。",
     "К тому же Сиеста говорила, что будет навещать её, когда освободится…"),
    ("dialogs", "W-well, when you put it that way… Maybe she'll be fine.",
     "そ、そういわれればそうね。大丈夫かもね。",
     "Н-ну, если так сказать… Может, и в порядке."),
    # ==== SCENE 155 ====
    ("dialogs", "Well, yeah, I'm a little worried. She's laid up sick, after all.",
     "そりゃまあ、ちょっとは心配かな。病気で寝込んでるわけなんだし。",
     "Ну да, немного волнуюсь. Она же болеет и лежит."),
    ("dialogs", "Muuu…",
     "う～～……。",
     "Мууу…"),
    ("dialogs", "But it doesn't seem like a life-threatening illness, and I figure she'll get better with rest — so I'm not that worried.",
     "でも、命に関わる病気でもなさそうだし、寝てれば治ると思ってるから、そんなに心配はしてないんだ。",
     "Но это, похоже, не болезнь, угрожающая жизни, и я думаю, от отдыха пройдёт, так что особо не волнуюсь."),
    ("dialogs", "Eh, is that so?",
     "えっ、そうなの？",
     "А, правда?"),
    ("dialogs", "Yeah — no matter how much I worry, it's not going to make her recover any faster.",
     "ああ、いくら俺が心配したところで病気の治りが早まるってわけでもないしな。",
     "Ага, я ведь волнованием не ускорю её выздоровление."),
    ("dialogs", "Still, I'd like her to get better soon, if she can.",
     "だけど、早く治るもんなら治ってほしいよな。",
     "Но всё равно хочется, чтобы она скорее поправилась."),
    # ==== SCENE 156 ====
    ("dialogs", "…{#ch3.2_l_031}",
     "……。",
     "…"),
    ("dialogs", "Hm? What's wrong, glaring at me like that?",
     "ん、どうしたんだ？俺のこと、にらみつけたりして。",
     "А? Что такое, чего на меня уставилась?"),
    ("dialogs", "I'm not glaring or anything…",
     "別に、にらんでなんかないわよ……。",
     "Вовсе не смотрю с ненавистью…"),
    ("dialogs", "Yeah… you're right, it does bug me.",
     "そうだな、確かに気になるな。",
     "Да… ты прав, мне тоже любопытно."),
    ("dialogs", "Mmm…",
     "む～……。",
     "Ммм…"),
    ("dialogs", "To Haruna, I'm the only person she knows in this world — I've got to look after her.",
     "春奈にとっては、俺がこの世界での唯一の知り合いなわけだし、面倒は見てあげないと。",
     "Для Харуны я единственный знакомый в этом мире — о ней ведь надо заботиться."),
    ("dialogs", "But I know I'm being a nuisance to you and Siesta, and I'm sorry about that.",
     "でも、なんだかんだでルイズやシエスタに迷惑かけちゃってるし、それはすまないと思ってる。",
     "Но я доставляю немало хлопот тебе и Сиесте — и мне это неприятно."),
    ("dialogs", "U-um… That part's fine, I don't really mind…",
     "う、うん……。別にそれはかまわないんだけどね……。",
     "Н-ну… Это, впрочем, меня не смущает…"),
    # ==== SCENE 157 ====
    ("dialogs", "Hm? What's wrong? Did I say something that bothered you?",
     "ん、どうした？俺、なんか気にさわるようなこと言っちゃったか？",
     "Что такое? Я что-то не то сказал?"),
    ("dialogs", "Nope, you didn't say anything.",
     "ううん、何も言ってない。",
     "Нет, ты ничего не сказал."),
    ("dialogs", "Oh, class is over. Now then, Louise— hm?",
     "おっ、授業が終わったぞ。さぁて、ルイズ……んんっ？",
     "О, урок окончен. Ну что ж, Луиза… мм?"),
    ("dialogs", "Huh? Where did Louise go? She up and ditched me without saying a word…",
     "あれ、ルイズのヤツ。どこに行っちまったんだ？俺をおいて、いなくなっちまうなんて……。",
     "Э? Куда это Луиза делась? И вот так ушла, оставив меня одного…"),
    ("thoughs", "Now then, what should I do…",
     "（さてと、どうしよう……）",
     "И что теперь делать…"),
    # ==== CHOISE (scene 147) ====
    ("choises", "Are you feeling under the weather?{#ch3_m147a}",
     "もしかして、体調が悪いのか？",
     "Может, тебе нездоровится?"),
    ("choises", "Are you sleepy?{#ch3_m147b}",
     "もしかして、眠いのか？",
     "Может, клонит в сон?"),
    ("choises", "Are you hungry?{#ch3_m147c}",
     "もしかして、お腹が減ったのか？",
     "Может, проголодалась?"),
    # ==== CHOISE (scene 153) ====
    ("choises", "Well, she's probably fine, right?{#ch3_m153a}",
     "まあ、大丈夫だろ？",
     "Ну, она вроде бы в порядке, да?"),
    ("choises", "I'm a little worried, I guess.{#ch3_m153b}",
     "ちょっとは心配かな",
     "Немного волнуюсь, наверное."),
    ("choises", "Yeah, it does bug me.{#ch3_m153c}",
     "確か気になるな",
     "Да, правда любопытно."),
    # ==== CHOICE (map ch3_2) — новые теги; Classroom/Courtyard/Leave переиспользуются ====
    ("choises", "Hallway{#ch3.2.hallway}",
     "廊下",
     "Коридор"),
    ("choises", "Hallway{#ch3.2.siesta}",
     "廊下",
     "Коридор"),
    ("choises", "Louise's Room{#ch3.2.lroom}",
     "ルイズの部屋",
     "Комната Луизы"),
]

# Голоса части 2 в порядке следования в сценарии: имя -> [voice N] канона.
VOICES = [
    ("ch3.2_si_001", 14647), ("ch3.2_l_001", 5903), ("ch3.2_si_002", 14648),
    ("ch3.2_s_001", 11244), ("ch3.2_si_003", 14649), ("ch3.2_s_002", 11245),
    ("ch3.2_si_004", 14650), ("ch3.2_l_002", 5904), ("ch3.2_s_003", 11246),
    ("ch3.2_s_004", 11247), ("ch3.2_l_003", 5905), ("ch3.2_s_005", 11248),
    ("ch3.2_s_006", 11249), ("ch3.2_ha_001", 2159), ("ch3.2_s_007", 11250),
    ("ch3.2_ha_002", 2160), ("ch3.2_l_004", 5906), ("ch3.2_s_008", 11251),
    ("ch3.2_s_009", 11252), ("ch3.2_l_005", 5907), ("ch3.2_s_010", 11253),
    ("ch3.2_l_006", 5908), ("ch3.2_s_011", 11254), ("ch3.2_l_007", 5909),
    ("ch3.2_s_012", 11255), ("ch3.2_l_008", 5910), ("ch3.2_s_013", 11256),
    ("ch3.2_l_009", 5911), ("ch3.2_s_014", 11257),
    ("ch3.2_s_015", 11258), ("ch3.2_l_010", 5912), ("ch3.2_s_016", 11259),
    ("ch3.2_l_011", 5913), ("ch3.2_s_017", 11260), ("ch3.2_l_012", 5914),
    ("ch3.2_s_018", 11261), ("ch3.2_l_013", 5915), ("ch3.2_ha_003", 2161),
    ("ch3.2_s_019", 11262), ("ch3.2_ha_004", 2162), ("ch3.2_s_020", 11263),
    ("ch3.2_ha_005", 2163), ("ch3.2_s_021", 11264),
    ("ch3.2_l_014", 5916), ("ch3.2_l_015", 5917), ("ch3.2_si_005", 14651),
    ("ch3.2_si_006", 14652), ("ch3.2_l_016", 5918), ("ch3.2_si_007", 14653),
    ("ch3.2_l_017", 5919), ("ch3.2_si_008", 14654), ("ch3.2_l_018", 5920),
    ("ch3.2_si_009", 14655), ("ch3.2_l_019", 5921), ("ch3.2_si_010", 14656),
    ("ch3.2_l_020", 5922), ("ch3.2_si_011", 14657), ("ch3.2_l_021", 5923),
    ("ch3.2_si_012", 14658), ("ch3.2_l_022", 5924),
    ("ch3.2_l_023", 5925), ("ch3.2_s_022", 11265), ("ch3.2_l_024", 5926),
    ("ch3.2_s_023", 11266), ("ch3.2_l_025", 5927), ("ch3.2_l_026", 5928),
    ("ch3.2_s_024", 11267),
    ("ch3.2_s_025", 11268), ("ch3.2_l_027", 5929), ("ch3.2_s_026", 11269),
    ("ch3.2_s_027", 11270), ("ch3.2_l_028", 5930),
    ("ch3.2_s_028", 11271), ("ch3.2_l_029", 5931), ("ch3.2_s_029", 11272),
    ("ch3.2_l_030", 5932), ("ch3.2_s_030", 11273), ("ch3.2_s_031", 11274),
    ("ch3.2_l_031", 5933), ("ch3.2_s_032", 11275), ("ch3.2_l_032", 5934),
    ("ch3.2_s_033", 11276), ("ch3.2_l_033", 5935), ("ch3.2_s_034", 11277),
    ("ch3.2_s_035", 11278), ("ch3.2_l_034", 5936),
    ("ch3.2_s_036", 11279), ("ch3.2_l_035", 5937), ("ch3.2_s_037", 11280),
    ("ch3.2_s_038", 11281),
]

BUCKET_FILES = {
    "dialogs": "dialogs.rpy",
    "thoughs": "thoughs.rpy",
    "choises": "choises.rpy",
}

SCRIPT_PATH = "game/chapters/3/script-ch3_2.rpy"
MANIFEST_PATH = "references/voice_id_map.csv"

def main():
    script = io.open(SCRIPT_PATH, encoding="utf-8").read()

    # 1. Сверка: каждый old реально есть в сценарии.
    missing = [old for bucket, old, ja, ru in ROWS if old not in script]
    if missing:
        print("ERROR: old not found in %s:" % SCRIPT_PATH)
        for m in missing:
            print("  - %s" % m)
        raise SystemExit(1)

    # 2. Дубликаты внутри ROWS.
    seen = set()
    dup_rows = []
    for bucket, old, ja, ru in ROWS:
        if old in seen:
            dup_rows.append(old)
        seen.add(old)
    if dup_rows:
        print("ERROR: duplicate old inside ROWS:")
        for d in dup_rows:
            print("  - %s" % d)
        raise SystemExit(1)

    # 3. Группировка с проверкой, нет ли old уже в целевом файле.
    by_bucket = {"dialogs": [], "thoughs": [], "choises": []}
    skipped = []
    for bucket, old, ja, ru in ROWS:
        fname = BUCKET_FILES[bucket]
        probe = 'old "%s"' % old
        already = False
        for lang in ("japanese", "russian"):
            path = "game/tl/%s/%s" % (lang, fname)
            text = io.open(path, encoding="utf-8").read()
            if probe in text:
                already = True
                break
        if already:
            skipped.append((bucket, old))
        else:
            by_bucket[bucket].append((old, ja, ru))

    # 4. Дозапись блоков.
    total = 0
    for bucket, pairs in by_bucket.items():
        if not pairs:
            continue
        fname = BUCKET_FILES[bucket]
        block_ja = "".join('\n    old "%s"\n    new "%s"\n' % (o, j) for o, j, r in pairs)
        block_ru = "".join('\n    old "%s"\n    new "%s"\n' % (o, r) for o, j, r in pairs)
        for lang, block in (("japanese", block_ja), ("russian", block_ru)):
            path = "game/tl/%s/%s" % (lang, fname)
            text = io.open(path, encoding="utf-8").read()
            if text and not text.endswith("\n"):
                text += "\n"
            text += block
            io.open(path, "w", encoding="utf-8").write(text)
        total += len(pairs)

    print("P2 TL pairs written:", total)
    if skipped:
        print("SKIPPED (old already present): %d" % len(skipped))
        for bucket, old in skipped:
            print("  - [%s] %s" % (bucket, old))

    # 5. Манифест голосов: добавить недостающие ch3.2_*.
    mtext = io.open(MANIFEST_PATH, encoding="utf-8").read()
    existing = set()
    for line in mtext.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("voice_name"):
            continue
        existing.add(line.split(",")[0])
    add = [(n, i) for n, i in VOICES if n not in existing]
    if add:
        if mtext and not mtext.endswith("\n"):
            mtext += "\n"
        mtext += "".join("%s,%d\n" % (n, i) for n, i in add)
        io.open(MANIFEST_PATH, "w", encoding="utf-8").write(mtext)
    print("Manifest rows added: %d (of %d)" % (len(add), len(VOICES)))

if __name__ == "__main__":
    main()
