# -*- coding: utf-8 -*-
# Генератор TL-блоков и манифеста голосов для главы 3, части 3 (сцены 1297–1321).
# old = точная строка EN-базы из script-ch3_3.rpy; ja_new — дословно из канона
# (переносы строк склеены, мысли в （ ）); ru_new — по JA.
# Дополнительно: добавляет 132 строки ch3.3_* в references/voice_id_map.csv.
# Запуск: python tools/gen_p3_tl.py
import io
import re
import sys

# (bucket, old, ja_new, ru_new)
ROWS = [
    # ==== SCENE 1297 (hallway) ====
    ("dialogs", "Even so, that Louise— she could've at least said something before leaving… Hm?",
     "それにしても、ルイズのヤツ、黙って出て行かなくたって……ん？",
     "Всё же, Луиза — могла бы хоть не уходить молча… А?"),
    ("dialogs", "Ah, there she is. Louise.",
     "あ、いたいた。ルイズだ。",
     "А, вот она. Луиза."),
    ("dialogs", "…Ah!?",
     "……あっ！？",
     "…А!?"),
    ("dialogs", "Hey, Louiise!",
     "おーい、ルイズーッ！",
     "Эй, Луиза-а!"),
    ("dialogs", "Why're you running!? Geez — don't make me chase you…",
     "なんで逃げるんだよっ！ったく、追いかけさせんなよ、もう……。",
     "Почему убегаешь!? Тьфу — не заставляй меня гнаться за тобой…"),
    ("dialogs", "Aaugh, honestly! Don't follow me on purpose!",
     "あー、もうっ！わざわざ追いかけて来ないでよっ！",
     "Ааа, блин! Не гоняйся за мной нарочно!"),
    ("dialogs", "If you run off the second you see me, naturally I'm going to get curious and chase you!",
     "人の顔見て逃げられたら、気になって追いかけるに決まってるだろ！",
     "Когда от меня убегают, как только увидят — я, само собой, полюбопытствую и побегу следом!"),
    ("dialogs", "I ran because I didn't want you to follow! You're my familiar, Saito — take a hint!!",
     "ついて来て欲しくないから、逃げたのっ！サイトはわたしの使い魔なんだから、それくらい察しなさいよっ！！",
     "Я убежала, потому что не хотела, чтобы ты шёл за мной! Ты мой фамильяр, Сайто — сообрази уже!!"),
    ("dialogs", "So that's why I— …Oh. Could it be…",
     "だから、なんでって……。あっ、ひょっとして……。",
     "Так почему же… А, может быть…"),
    # ==== CHOICE (scene 1297) ====
    ("choises", "Did I do something?{#ch3_m1297a}",
     "俺、なんかやらかした？",
     "Я что-то натворил?"),
    ("dialogs", "Did I do something? I don't think I've done anything to make Louise mad…",
     "俺、なんかやらかした？ルイズの機嫌を損ねるようなこと、した覚えは……ないような気がする。",
     "Я что-то натворил? Кажется, я не делал ничего, что могло бы расстроить Луизу…"),
    ("dialogs", "I don't care about that — I'm telling you not to follow me right now! Got it?",
     "なんでもいいから、今はわたしの後をついて来なくていいって言ってるのっ！分かった？",
     "Мне всё равно что — я говорю, чтобы ты сейчас не шёл за мной! Понял?"),
    ("dialogs", "I get it, I get it. Just don't be so mad…",
     "分かった、分かった。分かったから、そんなに怒るなよ……。",
     "Ладно, ладно. Я ж понял — не злись так…"),
    ("dialogs", "If you follow me… I'll really get mad at you, okay!!",
     "もし、ついて来たら……。サイトのこと、本気で怒っちゃうんだからねっ！！",
     "Если пойдёшь за мной… я правда рассержусь, ладно!!"),
    ("choises", "Am I in the way?{#ch3_m1297b}",
     "俺がいると邪魔？",
     "Я мешаюсь?"),
    ("dialogs", "Am I in the way?",
     "俺がいると邪魔？",
     "Я мешаюсь?"),
    ("dialogs", "I-I'm not saying you're in the way or anything…",
     "べ、別にサイトが邪魔だなんて思っちゃないわよ……。",
     "Я-я не то чтобы думаю, что ты мешаешь…"),
    ("dialogs", "Okay, okay. So where are you headed?",
     "分かった分かった。で、どこ行くつもりなんだよ？",
     "Хорошо, хорошо. И куда ты собираешься?"),
    ("dialogs", "You're not getting it at all! I told you not to come, so don't follow me!",
     "ちっとも分かってないっ！わたしが来るなって言ってるんだから、ついて来るなっ！",
     "Ты ничего не понимаешь! Я сказала не идти — так что не ходи за мной!"),
    ("choises", "Are you going to take a bath?{#ch3_m1297c}",
     "風呂に行くつもりとか？",
     "Ты собралась в ванну?"),
    ("dialogs", "Are you going to take a bath?",
     "お風呂に行くつもりとか？",
     "Собралась в ванну?"),
    ("dialogs", "Y-yes, I am… It's hot today, after all. …Wh-what's with that look?",
     "そ、そうよ……。今日は暑いしね。……って、な、なによ、その目は。",
     "Н-ну да… Сегодня ведь жарко. …Ч-что за взгляд?"),
    ("dialogs", "Really?{#ch3.3_s_012}",
     "本当？",
     "Правда?"),
    ("dialogs", "That doesn't matter! Just don't follow me for now! See you!",
     "そんなのどうだっていいじゃないっ！とにかく今はついて来ないで！じゃあね！",
     "Мне это не важно! В любом случае не ходи за мной! Пока!"),
    ("dialogs", "Well, shoot… Did I do something to Louise…",
     "なんだかなぁ……。俺、ルイズに何かしたかなぁ……。",
     "Эх… Не сделал ли я чего не то с Луизой…"),
    # ==== SCENE 1302 (siesta hallway) ====
    ("dialogs", "Where on earth did Louise run off to…",
     "いったい、どこ行っちまったのかなぁ、ルイズのヤツ……。",
     "Куда это Луиза удрала…"),
    ("dialogs", "…Hm? Isn't that Siesta? Looks like she's hauling a huge load…",
     "……ん？あれはシエスタじゃないか？なんだか大荷物を運んでるようだけど……。",
     "…А? Это же Сиеста? Похоже, тащит огромную ношу…"),
    ("dialogs", "Hey, Siestaaa!",
     "おーい、シエスター！",
     "Эй, Сиеста-а!"),
    ("dialogs", "…!? S-Saito-san!!",
     "……！？サ、サイトさんっ！！",
     "…!? С-Сайто-сан!!"),
    ("dialogs", "That load looks brutal to carry. Want a hand?",
     "その荷物、運ぶの大変だろ？手伝ってやろうか？",
     "Такую ношу тащить тяжело, да? Помочь?"),
    ("dialogs", "Um, well, you see…",
     "えっと、そのですね……。",
     "Ну, это, собственно…"),
    ("dialogs", "What's wrong? You don't have to hold back.",
     "どうしたの？遠慮なんてしなくっていいって。",
     "Что такое? Не нужно стесняться."),
    ("dialogs", "No, I'm fine…",
     "いいです……。",
     "Нет, лучше не надо…"),
    ("dialogs", "Huh? Why? Oh — could it be…",
     "えっ、なんで？あ、ひょっとして……。",
     "А? Почему? А, может быть…"),
    # ==== CHOICE (scene 1302) ====
    ("choises", "Luggage I'm not allowed to touch?{#ch3_m1302a}",
     "俺が触ったら困る荷物だとか？",
     "Багаж, которого мне трогать нельзя?"),
    ("dialogs", "Luggage I'm not allowed to touch?",
     "俺が触ったら困る荷物だとか？",
     "Багаж, которого мне трогать нельзя?"),
    ("dialogs", "N-no, that's not it at all~",
     "そ、そんなことはないですよー。",
     "Н-нет, ничего подобного~"),
    ("dialogs", "Then I'll…",
     "それじゃあ、俺が……。",
     "Тогда я…"),
    ("dialogs", "N-no! I said no — stooop!?",
     "ダ、ダメですっ！ダメですってば、いやぁーっ！？",
     "Н-нет! Нет же — не надоо!?"),
    ("dialogs", "W-wait, Siesta… W-what's wrong?",
     "ちょっ、ちょっとシエスタ……。ど、どうしたの？",
     "П-подожди, Сиеста… Ч-что такое?"),
    ("dialogs", "Please be quiet and trust me for now — I'd never do anything to hurt you, Saito-san.",
     "今は黙って、わたしを信じていてください。サイトさんにとって、けっして悪いようにはしませんから。",
     "Просто помолчи и поверь мне. Я ведь никогда не сделаю тебе ничего дурного, Сайто-сан."),
    ("choises", "Did I do something to offend you?{#ch3_m1302b}",
     "何か嫌われるようなことした？",
     "Я что-то сделал, чем тебя обидел?"),
    ("dialogs", "Did I do something to offend you?",
     "何か嫌われるようなことした？",
     "Я что-то сделал, чем тебя обидел?"),
    ("dialogs", "N-no, I haven't! Not at all!",
     "し、してませんっ！全然してませんからっ！",
     "Н-нет, не делала! Вообще нет!"),
    ("dialogs", "Then I'll carry the luggage…",
     "じゃあ、荷物は俺が運んで……。",
     "Тогда я понесу багаж…"),
    ("dialogs", "T-that's exactly why you can't! It's work I was asked to do…",
     "だ、だからダメです！わたしが頼まれた仕事ですから……。",
     "В-вот поэтому нельзя! Это же порученная мне работа…"),
    ("dialogs", "If they found out I let Saito-san help, I'd get scolded.",
     "サイトさんに手伝わせた、なんて知られたら、わたし、叱られてしまいます。",
     "Если узнают, что я попросила Сайто-сана помочь, меня отругают."),
    ("dialogs", "I-see…",
     "そ、そうなんだ……。",
     "Т-так вот как…"),
    ("choises", "Are you working out or something?{#ch3_m1302c}",
     "体を鍛えてるとか？",
     "Ты что, тренируешься?"),
    ("dialogs", "Are you working out or something?",
     "体を鍛えてるとか？",
     "Ты что, тренируешься?"),
    ("dialogs", "Well, in a way… A maid's job comes down to stamina, so this is how I keep in shape, day after day…",
     "ええ、まあ……。メイドのお仕事は体力勝負ですから、こうやって日々ですね……。",
     "Ну, можно сказать… Работа горничной — дело силовое, вот и тренируюсь так каждый день…"),
    ("dialogs", "You're kidding.",
     "嘘でしょ。",
     "Не может быть."),
    ("dialogs", "Yes.{#ch3.3_si_011}",
     "はい。",
     "Да."),
    ("dialogs", "I don't know what you're so shy about, but I'm going to help you.",
     "何を遠慮してるか分からないけど、手伝ってあげるよ。",
     "Не знаю, отчего ты так стесняешься, но я помогу."),
    ("dialogs", "Um, Saito-san — I really don't need any help…",
     "あのぉ、サイトさん。お手伝いは結構ですので……。",
     "Э-это, Сайто-сан. Помощь вовсе не обязательна…"),
    ("dialogs", "A-anyway! A load this size is nothing for me alone!",
     "と、とにかくっ！これくらいの荷物、わたし１人で大丈夫ですからっ！",
     "В-в любом случае! С такой ношей я и одна справлюсь!"),
    ("dialogs", "If Siesta insists that much, I won't do anything…",
     "シエスタがそこまで言うのなら、俺は何もしないけど……。",
     "Раз Сиеста так настаивает, я вмешиваться не буду…"),
    ("dialogs", "Well then, I'll be going, Saito-san.",
     "それでは失礼しますね、サイトさん。",
     "Ну что ж, я пойду. Сайто-сан."),
    ("dialogs", "Ah, right…",
     "あ、うん……。",
     "А, да…"),
    ("dialogs", "Whatever she says, she's still wobbling… I hope she's really okay…",
     "なんだかんだ言っても、足取りがふらついてるみたいだなぁ。……本当に、大丈夫なのかな？",
     "Как ни говори, а шаги у неё шатаются… Она ведь правда в порядке…"),
    # ==== SCENE 1307 (classroom) ====
    ("dialogs", "Now then, what should I do…{#ch3.3_s_032}",
     "さてと、どうしたもんかなぁ？",
     "Ну что ж, что теперь делать…"),
    ("dialogs", "My, Darling. All alone right now?",
     "あらダーリン。いま１人なの？",
     "Ох, Дорогой. Ты сейчас один?"),
    ("dialogs", "Ah, Kirche… Louise up and vanished the moment class ended…",
     "あ、キュルケ……。ルイズのヤツ、授業が終わったら、いなくなっちまってさ……。",
     "А, Кирхе… Луиза исчезла, как только кончился урок…"),
    ("dialogs", "I see, I see. …So that means my Darling's free right now, doesn't it?",
     "へー、そうなんだぁ。……ってことは、いまのダーリンはフリーってことよね？",
     "Понятно-понятно. …Значит, мой Дорогой сейчас свободен, да?"),
    ("dialogs", "Well, I guess so.",
     "まあ、そういうことになるのかなぁ。",
     "Ну, наверное, да."),
    ("dialogs", "Then here's a perfect chance — come with me… Mm?",
     "じゃあさ、いい機会だから、あたしと一緒に……んんっ？",
     "Раз уж такая возможность — пойдём со мной… Мм?"),
    ("dialogs", "What's wrong, Kirche? Staring at my face out of nowhere…",
     "どうしたんだ、キュルケ？急に俺の顔を見つめたりして……。",
     "Что такое, Кирхе? Вдруг уставилась мне в лицо…"),
    ("dialogs", "Wait. Would you let me read your fortune, Darling?",
     "ちょっと、待って。ダーリンのこと、少し占わせてもらっていい？",
     "Подожди. Разреши немного погадать, Дорогой?"),
    ("dialogs", "Ah, sure… I don't mind…",
     "あ、ああ……。それは構わないけど……。",
     "А, ага… Не против…"),
    ("dialogs", "…{#ch3.3_k_v01}",
     "………。",
     "…"),
    ("dialogs", "...I see it. ...Listen, Saito. You've got the look of someone who's going to have trouble with women.",
     "……見えた。……ねえ、サイト。あなた女難の相が出てるわよ。",
     "…Вижу. …Слушай, Сайто, у тебя на лице прямо написано: с женщинами одни неприятности."),
    ("dialogs", "Trouble with women? That can't happen to me... ...Actually, it can.",
     "女難の相だって？そんなこと俺にあるはず……。あるな……。",
     "Что, мне светят неприятности из-за женщин? Да не может такого со мной быть… Хотя… ещё как."),
    ("dialogs", "Hmm... Maybe your case is even worse than usual?",
     "うーん、いつもよりも、もっと重症かな？",
     "Хм… А у тебя, похоже, случай ещё тяжелее обычного."),
    ("dialogs", "Huh, seriously? Worse than usual — what's that mean?",
     "え、マジで？いつもよりも重症ってどういうこと？",
     "А, серьёзно? Тяжелее обычного — это как?"),
    ("dialogs", "I don't know the details either. But shouldn't you be careful around the girls here?",
     "あたしだって詳しいことは分からないわよ。でも、周りの女の子のこと気をつけなくっちゃ駄目なんじゃないかしら？",
     "Я же не знаю подробностей. Но разве не стоит беречься девушек вокруг?"),
    ("dialogs", "There must be one girl who's the cause. Any idea who, Darling?",
     "きっと原因になってる子がいるはずよ？ダーリンに思い当たる節はない？",
     "Наверняка есть девчонка, которая всему причина. Дорогой, нет ли у тебя подозрений?"),
    ("dialogs", "Someone I suspect, huh… Let me think…",
     "思い当たる節かぁ……。そうだなぁ……。",
     "Кого я подозреваю… Дай подумать…"),
    # ==== CHOICE (scene 1307) ====
    ("choises", "Louise, one way or another?{#ch3_m1307a}",
     "なんだかんだでルイズ？",
     "Так или иначе — Луиза?"),
    ("dialogs", "Louise, one way or another?",
     "なんだかんだでルイズ？",
     "Так или иначе — Луиза?"),
    ("dialogs", "My, so Darling thought so too.",
     "あら、ダーリンもそう思ってたのね。",
     "Ох, мой Дорогой тоже так думал."),
    ("dialogs", "Well, I'm always getting punished as the 'stupid dog' and all…",
     "だってさぁ、いつもバカ犬って、お仕置きされてるしさ……。",
     "Ну, меня же всегда наказывают как «глупую собаку»…"),
    ("dialogs", "I wonder what punishment would be worse than that…",
     "それよりもひどいって、どんなお仕置きだろ……。",
     "И какое наказание будет хуже…"),
    ("dialogs", "Brrr… I'm starting to get scared.",
     "ぶるぶるぶる。なんか、怖くなってきたぞ。",
     "Бр-р-р… Что-то я начинаю бояться."),
    ("choises", "Siesta directly?{#ch3_m1307b}",
     "直接的にはシエスタ？",
     "А непосредственно Сиеста?"),
    ("dialogs", "Siesta directly?",
     "直接的にはシエスタ？",
     "А непосредственно Сиеста?"),
    ("dialogs", "My, how unexpected… What about the maid?",
     "あら、意外ね……。メイドがどうしたの？",
     "Ой, неожиданно… А что с горничной?"),
    ("dialogs", "No, it's not like I think Siesta's done anything wrong or anything.",
     "いや、別にシエスタが悪いとかどうとかじゃないんだけどね。",
     "Нет, я не то чтобы считаю, что Сиеста виновата или ещё что."),
    ("dialogs", "It's just — when Louise and Siesta are in the same room, I don't know, I get all uneasy.",
     "たださ、ルイズとシエスタが同じ部屋にいると、なんだか俺が落ち着かないんだよ。",
     "Просто когда Луиза и Сиеста в одной комнате, мне почему-то не по себе."),
    ("dialogs", "Of course you'd be uneasy. In all sorts of ways…",
     "そりゃあ、落ち着かないでしょうねぇ。いろんな意味で……。",
     "Ну, не по себе же тебе. В самых разных смыслах…"),
    ("dialogs", "Hm? Did you say something?{#ch3.3_s_047}",
     "ん？いまなんか言った？",
     "А? Что-то сказала?"),
    ("dialogs", "Mm-mm, nothing at all.",
     "んーん、別になんにも。",
     "Мм-мм, ничего."),
    ("choises", "Kirche, by any chance?{#ch3_m1307c}",
     "もしかしてキュルケ？",
     "Может, Кирхе?"),
    ("dialogs", "Kirche, by any chance?",
     "もしかしてキュルケ？",
     "Может, Кирхе?"),
    ("dialogs", "Why would I be the cause? Darling or not, I'll get mad, you know?",
     "なんであたしが原因になるのよ？いくらダーリンでも、怒るわよ？",
     "Почему я должна быть причиной? Дорогой ты мой, но я всё равно рассержусь, ладно?"),
    ("dialogs", "Just kidding, just kidding.",
     "冗談だよ、冗談。",
     "Я шучу, шучу."),
    ("dialogs", "Say things like that and you'll bring on trouble with women that's no joke.",
     "そういうこと言ってると、冗談にならないような女難を起こしちゃうんだから。",
     "Такими словами ты накликаешь неприятности с женщинами — и совсем нешуточные."),
    ("dialogs", "No, that would be bad… Maybe.",
     "いや、それは困る……かも。",
     "Нет, это было бы плохо… Или может быть."),
    ("dialogs", "An-y-way! Whoever the cause is, you'd better watch out for trouble with women, okay?",
     "と・に・か・くっ！原因が誰であれ、女難には気をつけた方がいいわよ？",
     "В-лю-бом-слу-чае! Кто бы ни был причиной, берегись неприятностей с женщинами, ладно?"),
    ("dialogs", "Is that really so?",
     "そうなのかなぁ、やっぱり？",
     "И правда так?"),
    ("dialogs", "I can tell even without a proper reading — this could be pretty bad.",
     "あたしが本格的に占わなくても分かるくらいなんだから、もう相当やばいかもね。",
     "Раз даже без настоящего гадания это видно — так что, может, совсем уже плохо."),
    ("dialogs", "Yeah, I'll be careful…",
     "ああ、気をつけるよ……。",
     "Ага, поберегусь…"),
    ("thoughs", "But how am I supposed to be careful…",
     "（でも、どう気をつければいいんだろ）",
     "Только вот беречь-то как…"),
    # ==== SCENE 1312 (courtyard) ====
    ("dialogs", "I stepped out into the courtyard, but… No sign of Louise.",
     "中庭に出てみたものの……。ルイズの姿は見えないな。",
     "Вышел во двор… А Луизы нигде нет."),
    ("dialogs", "…Hm? Is that Tabitha over there?",
     "……ん？あそこにいるのはタバサか。",
     "…А? Это же Табита вон там?"),
    ("dialogs", "…{#ch3.3_t_v01}",
     "……。",
     "…"),
    ("dialogs", "H-hi…",
     "や、やあ……。",
     "П-привет…"),
    ("dialogs", "…{#ch3.3_t_v02}",
     "……。",
     "…"),
    ("thoughs", "No reaction, huh… — right, no time to chicken out.",
     "（反応ゼロか……。　って、ひるんでる場合じゃないよな）",
     "Реакции ноль… Верно, не время отступать."),
    ("dialogs", "If you know, I'd like to hear it… Have you seen Louise around here?",
     "もし知ってたら教えてほしいんだけど……。この辺でルイズを見かけなかった？",
     "Если знаешь — скажи… Не видела ли ты тут Луизу?"),
    ("dialogs", "…{#ch3.3_t_v03}",
     "……。",
     "…"),
    ("dialogs", "Um, Tabitha-san? Could it be…",
     "あのぉ、タバサさん？ひょっとして……。",
     "Э-это, Табита-сан? Может быть…"),
    # ==== CHOICE (scene 1312) ====
    ("choises", "Do you hate me?{#ch3_m1312a}",
     "ボクのこと嫌いですか？",
     "Ты меня не выносишь?"),
    ("dialogs", "Do you hate me?",
     "ボクのこと嫌いですか？",
     "Ты меня не выносишь?"),
    ("dialogs", "…{#ch3.3_t_v04}",
     "……。",
     "…"),
    ("choises", "Have you really not seen Louise?{#ch3_m1312b}",
     "本当にルイズ見かけてないの？",
     "Ты правда не видела Луизу?"),
    ("dialogs", "Have you really not seen Louise?",
     "本当にルイズ見かけてないの？",
     "Ты правда не видела Луизу?"),
    ("dialogs", "…Nope.",
     "……うん。",
     "…Не видела."),
    ("dialogs", "I-I see…",
     "そ、そうなんだぁ。",
     "А-а, понятно…"),
    ("choises", "Are you busy reading?{#ch3_m1312c}",
     "本読むのに忙しいですか？",
     "Тебе некогда читать?"),
    ("dialogs", "Are you busy reading?",
     "本読むのに忙しいですか？",
     "Тебе некогда читать?"),
    ("dialogs", "…Very.",
     "……とっても。",
     "…Очень."),
    ("dialogs", "I see. My apologies, then.",
     "なるほど、それは失礼いたしました。",
     "Понятно. Простите, что помешал."),
    ("dialogs", "Well then, I'd better not interrupt your reading — I'll be going.",
     "それじゃあ、本読んでるとこを邪魔しちゃ悪いから、俺行くわ。",
     "Ладно, не буду мешать тебе читать — я пойду."),
    ("dialogs", "…Louise isn't here.",
     "……ここにはルイズは来てない。",
     "…Луизы здесь нет."),
    ("dialogs", "R-right? Thanks for telling me.",
     "そ、そうか？教えてくれてサンキューな。",
     "О-о, так? Спасибо, что подсказала."),
    ("thoughs", "Tabitha seems kind of upset — did I say something to tick her off?",
     "（なんか、タバサの機嫌が悪いけど、　俺、なにかタバサの気に障ることを　したっけ？）",
     "Табита вроде недовольна… А я что-то такое сказал, чем её задел?"),
    # ==== SCENE 1317 (Louise's room) ====
    ("dialogs", "Back here again… She's not back, after all.",
     "ここに戻って……。きてないか、やっぱり。",
     "Вернулся сюда… И опять её нет."),
    ("dialogs", "Ah, Hiraga-kun!",
     "あっ、平賀くん！",
     "А, Хирага-кун!"),
    ("dialogs", "Sorry, Haruna. Seems I woke you while you were sleeping.",
     "ごめんな春奈。寝てたところ、起こしちまったみたいで。",
     "Прости, Харуна. Видно, разбудил тебя во сне."),
    ("dialogs", "No, it's fine. I was thinking I might be okay without sleeping soon anyway.",
     "ううん、そんなことないよ。そろそろ寝なくても大丈夫かなって思うし。",
     "Нет, ничего такого. Я как раз думала, что скоро можно будет и не спать."),
    ("dialogs", "No way. You have to sleep properly until you're better.",
     "ダメだぞ。治るまでちゃんと寝てなきゃ。",
     "Нельзя. Нужно нормально спать, пока не поправишься."),
    ("dialogs", "But…{#ch3.3_ha_003}",
     "でも……。",
     "Но…"),
    ("dialogs", "In this world, you can't just go to the hospital, take some medicine, and call it done.",
     "こっちの世界じゃ、病院行って、薬飲んでおしまいってわけにはいかないんだから。",
     "В этом мире нельзя просто пойти в больницу, выпить лекарства — и всё."),
    ("dialogs", "R-right…{#ch3.3_ha_004}",
     "う、うん……。",
     "Н-ну…"),
    ("dialogs", "I once got seriously hurt in a duel.",
     "前に決闘で、大怪我したことがあるんだよ。",
     "Когда-то я сильно поранился на дуэли."),
    ("dialogs", "Eh — Hiraga-kun is the type to fight duels… I'm a little… surprised…",
     "えっ、平賀くんって決闘なんてするタイプの人だったんだ……。ちょっと、びっくり……。",
     "Ой, Хирага-кун из тех, кто дрётся на дуэлях… Немного удивлена…"),
    ("dialogs", "Well, I'll keep my opponent's name a secret for their honor — but I won the duel, though I took a real beating.",
     "まぁ、相手は名誉のために伏せておくけど、決闘に勝つには勝ったんだけどさぁ、おもいっきりダメージもらっちゃってね。",
     "Ну, имя соперника я ради чести сохраню в тайне — дуэль выиграл, но досталось мне здорово."),
    ("dialogs", "Back then I had Louise buy me a secret potion for a healing spell — I caused her a ton of trouble.",
     "そのときルイズに、治癒の魔法をかけるための秘薬を買ってもらって、すっげぇ迷惑かけちまってるんだよ。",
     "Тогда я попросил Луизу купить тайное снадобье для исцеляющего заклинания — и доставил ей кучу хлопот."),
    ("dialogs", "And that secret potion turned out to be incredibly expensive…",
     "その秘薬ってのが、また、すっごく高い代物だったらしくて……。",
     "И это снадобье, как выяснилось, оказалось невероятно дорогим…"),
    ("dialogs", "…{#ch3.3_ha_v01}",
     "……。",
     "…"),
    ("dialogs", "Hm? What's wrong, Haruna?",
     "ん？どうしたんだ、春奈？",
     "А? Что такое, Харуна?"),
    ("dialogs", "…No, it's nothing. It's nothing, but…",
     "……ううん、なんでもないの。なんでもないんだけど……。",
     "…Нет, ничего. Просто ничего, но…"),
    ("dialogs", "Could it be… Is there something you want to say to me?",
     "ひょっとして……。俺になんか言いたいこととかあったりする？",
     "Может быть… Ты хочешь мне что-то сказать?"),
    ("dialogs", "…No.{#ch3.3_ha_007}",
     "……ないよ。",
     "…Нет."),
    ("thoughs", "She looks like she wants to say something — what should I do…",
     "（何か言いたげな様子なんだけど、　どうしたもんかなぁ？）",
     "Кажется, ей есть что сказать… Что теперь делать…"),
    ("dialogs", "Hey, Haruna…",
     "なぁ、春奈……。",
     "Слушай, Харуна…"),
    # ==== CHOICE (scene 1317) ====
    ("choises", "Don't hold back with me.{#ch3_m1317a}",
     "俺に遠慮とかすんなよな",
     "Не стесняйся меня."),
    ("dialogs", "Don't hold back with me.",
     "俺に遠慮とかすんなよな。",
     "Не стесняйся меня."),
    ("dialogs", "…{#ch3.3_ha_v02}",
     "……。",
     "…"),
    ("dialogs", "You and I are from the same world, you know.",
     "おまえと俺は、同じ世界の人間なんだし。",
     "Мы с тобой — люди одного мира."),
    ("dialogs", "…{#ch3.3_ha_v03}",
     "……。",
     "…"),
    ("choises", "You need to rest up now, okay?{#ch3_m1317b}",
     "今はゆっくり休まなきゃダメだぞ",
     "Сейчас надо спокойно отдыхать."),
    ("dialogs", "You need to rest up now, okay?",
     "今はゆっくり休まなきゃダメだぞ。",
     "Сейчас надо спокойно отдыхать."),
    ("dialogs", "…{#ch3.3_ha_v04}",
     "……。",
     "…"),
    ("dialogs", "This is a world where even curing one illness is a struggle. Your body's your greatest asset here.",
     "こんな病気ひとつ治すのもひと苦労な世界だ。ここじゃ、体が大事な財産なんだから。",
     "Мир, где даже одну болезнь вылечить — целая мука. Здесь тело — твоё главное богатство."),
    ("dialogs", "…{#ch3.3_ha_v05}",
     "……。",
     "…"),
    ("choises", "If you've got something to say, say it.{#ch3_m1317c}",
     "言いたいことがあるなら言えって",
     "Если есть что сказать — говори."),
    ("dialogs", "If you've got something to say, say it.",
     "言いたいことがあるなら言えって。",
     "Если есть что сказать — говори."),
    ("dialogs", "…{#ch3.3_ha_v06}",
     "……。",
     "…"),
    ("dialogs", "Keeping things you want to say all to yourself is stressful — bad for your health, you know?",
     "言いたいことを自分だけでかかえてるなんて、それだけでもストレスになって体によくないんだぜ？",
     "Всё держать в себе — это уже стресс, вредный для здоровья, понимаешь?"),
    ("dialogs", "…{#ch3.3_ha_v07}",
     "……。",
     "…"),
    ("dialogs", "I'm going to sleep…",
     "私、寝る……。",
     "Мне спать…"),
    ("dialogs", "…Ah, right? See you later, then.",
     "……あ、そっか？それじゃ、またあとでな。",
     "…А, точно? Ну, тогда до встречи."),
]

# Голоса: непрерывные диапазоны id (сверено с transcriptions_ja_ru.csv).
VOICES = (
    [("ch3.3_s_%03d" % (i + 1), 9631 + i) for i in range(82)] +
    [("ch3.3_l_%03d" % (i + 1), 4947 + i) for i in range(9)] +
    [("ch3.3_si_%03d" % (i + 1), 14416 + i) for i in range(14)] +
    [("ch3.3_k_%03d" % (i + 1), 2958 + i) for i in range(16)] +
    [("ch3.3_t_%03d" % (i + 1), 15442 + i) for i in range(3)] +
    [("ch3.3_ha_%03d" % (i + 1), 1882 + i) for i in range(8)]
)

BUCKET_FILES = {
    "dialogs": "dialogs.rpy",
    "thoughs": "thoughs.rpy",
    "choises": "choises.rpy",
}

SCRIPT_PATH = "game/chapters/3/script-ch3_3.rpy"
MANIFEST_PATH = "references/voice_id_map.csv"


def script_lines(script):
    """(bucket, old) для каждой say/menu-строки сценария в порядке следования."""
    out = []
    for ln in script.splitlines():
        m = re.match(r'^\s+(s|l|si|k|t|ha|th) "((?:[^"\\]|\\.)*)"\s*$', ln)
        m2 = re.match(r'^\s+"((?:[^"\\]|\\.)*)":\s*$', ln)
        if m:
            char, text = m.group(1), m.group(2)
            out.append(("thoughs" if char == "th" else "dialogs", text))
        elif m2:
            out.append(("choises", m2.group(1)))
    return out


def main():
    script = io.open(SCRIPT_PATH, encoding="utf-8").read()
    lines = script_lines(script)

    # 1. Каждый old реально есть в сценарии.
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

    # 2b. Двусторонняя сверка ROWS со строками сценария (порог = комплектность).
    row_olds = set(seen)
    script_olds = set(t for b, t in lines)
    only_script = script_olds - row_olds
    only_rows = row_olds - script_olds
    if only_script or only_rows:
        print("ERROR: ROWS/script mismatch.")
        for t in sorted(only_script):
            print("  - only in script: %s" % t)
        for t in sorted(only_rows):
            print("  - only in ROWS: %s" % t)
        raise SystemExit(1)
    print("script say/menu lines: %d | ROWS: %d" % (len(lines), len(ROWS)))

    # 2c. Бакеты: автопроверка (th→thoughs, меню→choises, остальное→dialogs).
    bucket_of = {t: b for b, t in lines}
    wrong = [(b, old) for b, old, ja, ru in ROWS if bucket_of.get(old) != b]
    if wrong:
        print("ERROR: bucket mismatch vs script:")
        for b, old in wrong:
            print("  - [%s] %s (script: %s)" % (b, old, bucket_of.get(old)))
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

    print("P3 TL pairs written:", total)
    if skipped:
        print("SKIPPED (old already present): %d" % len(skipped))
        for bucket, old in skipped:
            print("  - [%s] %s" % (bucket, old))

    # 5. Манифест голосов: добавить недостающие ch3.3_*.
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
