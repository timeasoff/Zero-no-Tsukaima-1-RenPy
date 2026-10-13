# -*- coding: utf-8 -*-
# Генератор TL-блоков для главы 3, части 4 (сцены 163–168).
# old = точная строка EN-базы из script-ch3_4.rpy; ja_new — дословно из канона
# (переносы склеены, мысли в （ ）); ru_new — по JA.
# Запуск: python tools/gen_p4_tl.py
import io

# (bucket, old, ja_new, ru_new)
ROWS = [
    # ==== SCENE 163 ====
    ("dialogs", "Haruna-san, pardon me~!", "ハルナさーん、失礼しますねー。", "Харуна-сан, не буду мешать~."),
    ("dialogs", "Siesta-san… What's with all this luggage…?", "シエスタさん……。その荷物って一体……。", "Сиеста-сан… Что это за вещи вообще…?"),
    ("dialogs", "How are you feeling?", "体のお加減はいかがですか？", "Как ваше самочувствие?"),
    ("dialogs", "Somehow, I'm managing…", "ええ、なんとか……。", "Ну, как-нибудь…"),
    ("dialogs", "…But your complexion still doesn't look good. Could it be a cold?", "……でも、まだ顔色がよくないみたいですね。ひょっとして、風邪なんでしょうか？", "…Но цвет лица у вас всё ещё не очень. Может, это простуда?"),
    ("dialogs", "Maybe… something like that?", "たぶん、そんな感じ……かな？", "Наверное… примерно так?"),
    ("dialogs", "...{#ch3.2_si_004}", "……。", "…"),
    ("dialogs", "...{#ch3.2_ha_004}", "……。", "…"),
    ("dialogs", "I've prepared all sorts of things for you, Haruna.", "わたしハルナさんのために色々とご用意してきたんですよ。", "Я кое-что заготовила для Харуна-сан."),
    ("dialogs", "Eh…?", "えっ……？", "Э…?"),
    ("dialogs", "First, let me tuck you into this thick quilt.", "まずは、この厚手の布団をハルナさんにかけますね。", "Сначала укрою Харуна-сан этим плотным одеялом."),
    ("dialogs", "Ah, if you do that…", "あっ、そんなことされたら……。", "Ах, если так сделаешь…"),
    ("dialogs", "They say it's good to sweat out a cold. This is kindness.", "風邪は汗をかくのがいいって言いますよ。これは親切です。", "Говорят, при простуде лучше пропотеть. Это из заботы."),
    ("dialogs", "R-right. Ju-just the right temperature, or so I thought.", "あ、そうですね。ちょ、ちょーどいい加減かなー、なぁんて。", "А-ага. Ка-как раз нормально, ну, так мне кажется."),
    ("dialogs", "I'm glad! I wanted to warm you up, so I made something really hot!", "良かったです。体を温めていただこうかと思って、すごく熱い料理も用意しましたよ！", "Как хорошо! Я хотела вас согреть и приготовила очень горячее блюдо!"),
    ("dialogs", "Um, I don't really have an appetite right now…", "あの、今はちょっと食欲がなくて……。", "Ну, у меня сейчас нет аппетита…"),
    ("dialogs", "No good, Haruna. You have to eat precisely because you have a cold.", "ダメですよ、ハルナさん。風邪のときだからこそ食べないとー。", "Так нельзя, Харуна-сан. Как раз при простуде и надо есть."),
    ("dialogs", "If you don't get proper nutrition, your cold will never get better, you know.", "ちゃんと栄養を取らないといつまでたっても風邪は治りませんからねー。", "Простуда не пройдёт, пока как следует не подкрепишься, понимаете-ка?"),
    ("dialogs", "Could it be… you're dead set on making me eat?", "ひょっとして……。意地でも食べさせる気だったりします？", "Уж не хочешь ли ты во что бы то ни стало заставить меня поесть?"),
    ("dialogs", "Dead set, you say… How harsh. I put my heart into preparing this dish because I wanted you to eat it.", "意地でもだなんて、そんな……。ハルナさんに食べていただきたくて、心を込めてご用意した料理ですし。", "Во что бы то ни стало — да как жестоко. Я приготовила это блюдо с душой, потому что хотела, чтобы Харуна-сан поела."),
    ("dialogs", "If you were already well, you might not need to eat it… or so I was thinking…", "もし、病気が治ってるのでしたら、食べる必要はないかもしれないなーとか、思いますけど……。", "Если бы болезнь уже прошла, может, есть и не нужно… ну, так я подумала…"),
    ("dialogs", "...{#ch3.2_ha_010}", "……。", "…"),
    ("thoughs", "She's trying to get me to admit I'm not really sick…", "（この人、私が病気じゃないこと白状させようとしてるのね……）", "Она пытается вырвать у меня признание, что я не больна…"),
    ("thoughs", "She doesn't like that Hiraga-kun is nursing me, I'm sure… but I'm not about to back down either…", "（私が平賀くんに看病されてるのが気に入らないんでしょーけど、こっちだってそうはいかないんだから……）", "Ей не нравится, что за мной ухаживает Хирага-кун, я уверена… но и мне сдаваться не входит в планы…"),
    ("dialogs", "…I won't lose.", "……負けないんだから。", "…Я не сдамся."),
    ("dialogs", "Pardon? Did you say something?", "はい？今なにかおっしゃいましたかー？", "А? Вы что-то сказали?"),
    ("dialogs", "N-nope, nothing~.", "いーえ、なんにもー。", "Н-нет, ничего~."),
    ("dialogs", "Now, it's all ready.", "さー、用意ができました。", "Ну-с, всё готово."),
    ("dialogs", "My, it looks really hot… Like it's bubbling away.", "まあ、とっても熱そうな……。まるでグラグラと煮えてるみたい。", "Ой, выглядит очень горячим… Прямо кипит."),
    ("dialogs", "Even so, this might be too hot to eat…", "いくらなんでも、これじゃあ熱すぎて食べるのは無理かも……。", "Но всё же это, пожалуй, слишком горячо, чтобы есть…"),
    ("dialogs", "No, no. A sick person has to eat at least this much…", "いえいえ、病気の方はこれくらいは食べないと……。", "Нет-нет, больному нужно съесть хотя бы столько…"),
    ("dialogs", "Oh, right—I also prepared firewood, so I'll light the fireplace later.", "そうそう、薪も用意しましたから、後で暖炉も焚きますね。", "Ах да, я ещё заготовила дрова — позже разожгу камин."),
    ("dialogs", "Eh…!!", "え……！！", "Э…!!"),
    ("dialogs", "Ufu, ufufufu…", "ウフ、ウフフフフ……。", "Уфу, уфуфуфу…"),
    ("dialogs", "Fufu, fufufufu…", "フフ、フフフフフ……。", "Фуфу, фуфуфу…"),

    # ==== SCENE 164 ====
    ("dialogs", "Louise, where the heck did she go off to…", "ルイズのヤツ、いったい、どこに行っちまったんだろう……。", "Луиза-то куда ушла…"),
    ("dialogs", "Wh-wha—!? W-what the—!?", "う、うわっぷ！？な、なんだ、いったい！？", "У-ува-ах!? Ч-что это вообще!?"),
    ("dialogs", "This room's heat is unnatural—!?", "尋常じゃないぞ、この部屋の暑さはっ！？", "Эта жара ненормальна—!?"),
    ("dialogs", "Ufufu, ufufufu…", "ウフフ、ウフフフフ……。", "Уфуфу, уфуфуфу…"),
    ("dialogs", "Fufufu, fufufufu…", "フフフ、フフフフフ……。", "Фуфуфу, фуфуфу…"),
    ("dialogs", "W-what are you doing? Grinning at each other in this heat!", "な、なにやってんだ？こんな暑さの中、２人で微笑みあってるし。", "Ч-что вы делаете? Ещё и улыбаетесь друг другу в такой жаре!"),
    ("dialogs", "U-um…", "え～っと……。", "Н-ну…"),
    ("choises", "Are you okay, Haruna?{#ch3_m164a}", "大丈夫か、春奈？", "Ты в порядке, Харуна?"),
    ("choises", "Siesta, you okay?{#ch3_m164b}", "シエスタ、大丈夫？", "Сиеста, ты в порядке?"),
    ("choises", "...Louise!?{#ch3_m164c}", "……ルイズは！？", "…А Луиза?!"),

    # ==== SCENE 165 ====
    ("dialogs", "Are you okay, Haruna?", "大丈夫か、春奈？", "Ты в порядке, Харуна?"),
    ("dialogs", "Ah, Hiraga-kun… I'm fine…", "あっ、平賀くん……。私なら、大丈夫だよ……。", "А, Хирага-кун… Со мной всё в порядке…"),
    ("dialogs", "No, no, no—what are you saying? This doesn't look fine at all!", "いやいやいや、なに言ってんの？ちっとも大丈夫な状況には見えないって！", "Да нет, нет — что ты говоришь? Это совсем не «всё в порядке»!"),
    ("dialogs", "You're drenched in sweat—how many quilts do you have on you?", "こんなに汗かいちゃってるのに、何枚布団かけてんだよ？", "Ты вся в поту — сколько на тебе одеял?"),
    ("dialogs", "Th-that's…", "そ、それは……。", "Э-это…"),
    ("dialogs", "That's?", "それは？", "Это?"),
    ("dialogs", "It's nothing…", "なんでもない……。", "Ничего…"),
    ("dialogs", "That's the thing—'it's nothing' can't cover a situation like this, right?", "だからさ、こんな状況で、なんでもないってことはないだろ？", "Вот о чём я — в такой ситуации «ничего» не бывает, правильно?"),

    # ==== SCENE 166 ====
    ("dialogs", "Siesta, you okay?", "シエスタ、大丈夫？", "Сиеста, ты в порядке?"),
    ("dialogs", "Ah, Saito-san… Ufufufu…", "あ、サイトさんだぁ……。ウフフフフ……。", "А, Сайто-сан… Уфуфуфу…"),
    ("dialogs", "No, I don't mean 'Saito-san'—", "いや、サイトさんじゃなくてさ。", "Нет, я не про «Сайто-сан»—"),
    ("dialogs", "Yees. I'm fiiine.", "はいー。大丈夫ですよー。", "Да-а. Всё хоро-ошо."),
    ("dialogs", "You don't look fine at all… More importantly, what are you two doing?", "とても大丈夫そうには見えない……。それより、２人してなにやってんの？", "Совсем не выглядишь хорошо… Скажи лучше, что вы тут делаете вдвоём?"),
    ("dialogs", "W-well, you see… I was just warming up the room a little…", "あ、あのですね……。ちょっと部屋を暖めてたら……。", "А, ну, это… Я просто немного прогревала комнату…"),
    ("dialogs", "Warming it? Why?", "暖めるって、なんで？", "Прогревала? Зачем?"),
    ("dialogs", "Well, how should I put it…", "それはなんというか……。", "Это, как бы сказать…"),
    ("dialogs", "How should you put it?", "なんというか？", "Как бы сказать?"),
    ("dialogs", "Ufufufu…", "ウフフフフ……。", "Уфуфуфу…"),
    ("dialogs", "No, I don't mean 'ufufu'—", "いや、ウフフじゃなくてー。", "Нет, я не про «уфуфу»—"),

    # ==== SCENE 167 ====
    ("dialogs", "...Louise!?", "……ルイズは！？", "…А Луиза?!"),
    ("dialogs", "If you mean Miss Valiere, she isn't here.", "ミス・ヴァリエールでしたら、ここにはいません。", "Если вы о мадемуазель Вальер — её здесь нет."),
    ("dialogs", "Yes, it's just the two of us…", "うん、私達２人だけ……。", "Да, нас только двое…"),
    ("dialogs", "I see… So what are you two up to? Making the room this hot and all.", "そっか……。で、２人でなにしてんの？こんなに部屋を暑くしちゃってさ。", "Понятно… И что вы делаете вдвоём? Комната раскалена."),
    ("dialogs", "...{#ch3.2_si_025}", "……。", "…"),
    ("dialogs", "...{#ch3.2_ha_024}", "……。", "…"),
    ("dialogs", "Ufufu, ufufufu…{#ch3.2_si_026}", "ウフフ、ウフフフフ……。", "Уфуфу, уфуфуфу…"),
    ("dialogs", "Fufufu, fufufufu…{#ch3.2_ha_025}", "フフフ、フフフフフ……。", "Фуфуфу, фуфуфу…"),
    ("dialogs", "I have no idea what's going on…", "って、何がなんだか分からないし……。", "Я уже ничего не понимаю…"),

    # ==== SCENE 168 ====
    ("dialogs", "What on earth is going on?", "一体何がどうなってるんだ？", "Что вообще здесь происходит?"),
    ("dialogs", "Wow, it really did get hot~. Ah, Saito…", "うわぁ、さすがに暑くなってるわねぇ～。あっ、サイト……。", "Ух ты, в самом деле жарко~. А, Сайто…"),
    ("dialogs", "Hey, Louise. I just made a 'this is bad' face at you, didn't I?", "おい、ルイズ。いま俺の顔見て、まずいって顔したろ？", "Эй, Луиза. Ты же видела моё лицо — я посмотрел так, будто всё плохо, да?"),
    ("dialogs", "Eh? What do you mean?", "え？なんのこと？", "А? О чём ты?"),
    ("dialogs", "You don't seem that surprised by how hot this room is.", "この部屋の暑さをそんなに驚いちゃいないみたいだしな。", "Ты как-то не слишком удивлена, как тут жарко."),
    ("dialogs", "Th-that's just your imagination!", "そ、そんなの気のせいじゃない？", "Э-это тебе показалось!"),
    ("dialogs", "Besides, it's your own room in this state—you should be at least a little surprised…", "というか、自分の部屋がこんな有様になってんだから、少しは驚けよ……。", "И вообще, у тебя самой комната в таком состоянии — стоило бы хоть немного удивиться…"),
    ("dialogs", "…Waaah, Siesta, are you okay-? How did this happen-!", "……。わー、シエスタだいじょうぶー？どーしてこんなことにー！", "…Ва-а, Сиеста, ты в порядке-? Как так вышло-!"),
    ("thoughs", "She's laying it on thick…", "（わざとらしいなぁ……）", "Прям таки нарочно…"),
    ("dialogs", "M-Miss Valiere… I'm done for.", "ミ、ミス・ヴァリエール……。わたくし、もうダメです。", "М-мадемуазель Вальер… Я больше не могу."),
    ("dialogs", "W-wait, Siesta!?", "ちょ、ちょっとシエスタっ！？", "П-подожди, Сиеста!?"),
    ("dialogs", "I'll entrust the rest to your ha…n… ……hau!?", "あとはお任せいたし……ま……。……はうっ！？", "Доверяю остальное вашим ру……к…… Хау!?"),
    ("dialogs", "Waaah—Siesta!?", "わぁーっ、シエスターっ！？", "Ва-а—Сиеста!?"),
    ("dialogs", "Hey, pull yourself together, Siesta! Siestaa!?", "ちょっとしっかりして、シエスタっ！シエスタったらぁ！？", "Ну-ка приди в себя, Сиеста! Сиеста-а!?"),
    ("dialogs", "………………", "………。……。……。", "………………"),
    ("dialogs", "S-sorry. I actually passed out…", "……す、すみません。わたくし、本気で意識が飛んでしまって……。", "П-простите. Я правда потеряла сознание…"),
    ("dialogs", "Ah, you're okay. Thank goodness…", "あっ、大丈夫なのね。良かったぁ……。", "А, всё в порядке. Ну и слава богам…"),
    ("dialogs", "Louise…", "なあ、ルイズ……。", "Луиза…"),
    ("dialogs", "Wh-what…", "な、なによっ……。", "Ч-что…"),
    ("dialogs", "And you, Siesta…", "それから、シエスタ……。", "И ты, Сиеста…"),
    ("dialogs", "Y-yes!", "は、はいっ！", "Д-да!"),
    ("dialogs", "What exactly did you two do?", "２人とも、いったい何をしたんだ？", "Вы двое — что вы натворили?"),
    ("dialogs", "I didn't do anything…", "わたしは別に……。", "Я ничего не…"),
    ("dialogs", "You did plenty! Heating up the room like idiots with Siesta—what were you thinking!", "別にってことないだろ？シエスタと２人して、馬鹿みたいに部屋を暑くして、なに考えてんだ！", "Как это «ничего»! Сиеста с тобой нагрели комнату до безумия — о чём вы думали?!"),
    ("dialogs", "Haruna's sick! Even if she weren't, doing this to someone would break their body, you know?!", "春奈は病気なんだぞ？病気じゃなくたって、こんなことされれば、体がぶっ壊れちまうだろ？", "Харуна ведь больна! Даже если бы не она — от такого сломалось бы любое тело, понятно?!"),
    ("thoughs", "But who started this mess?", "（しかし、誰が騒ぎの原因なんだ？）", "Но кто тут устроил весь этот сыр-бор?"),
    ("choises", "It was Louise who started it, right?{#ch3_m168a}", "ルイズが言い出したことだろ？", "Это же Луиза затеяла?"),
    ("choises", "This isn't like the usual Siesta.{#ch3_m168b}", "いつものシエスタらしくないぞ", "Это не похоже на обычную Сиесту."),
    ("choises", "Do you dislike Haruna?{#ch3_m168c}", "春奈のこと、気に入らないのか？", "Тебе что, Харуна не нравится?"),
]

BUCKET_FILES = {
    "dialogs": "dialogs.rpy",
    "thoughs": "thoughs.rpy",
    "choises": "choises.rpy",
}

by_bucket = {"dialogs": [], "thoughs": [], "choises": []}
for bucket, old, ja, ru in ROWS:
    by_bucket[bucket].append((old, ja, ru))

total = 0
for bucket, pairs in by_bucket.items():
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

print("P4 TL pairs written:", total)
