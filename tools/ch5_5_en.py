# -*- coding: utf-8 -*-
"""EN-переводы для части ch5.5 (сцены 320–334).

Ключи — имена голосов сценария (ch5.5_<spk>_<NNN>) для реплик (в т.ч.
ch5.5_t_001 — голос-мысль （くいくい）), ch5_5_th_<NNN> для мыслей без
голоса, номер сцены-варианта (строкой) для пунктов меню.

Смысл и модальность — по JA (ps2_source/events_full/chapter_06_本当の想い.txt,
сцены 320–334; .tmp/ch5_5_source.txt). Многоточие — «…» (PROMTS.md §5);
конвенция окончаний — по данным частей 3–4 (проверено
tools/check_ellipsis_ja.py, расхождений 0):
  - целая строка JA «……。»         → EN/RU «…….»;
  - финал строки JA «……。»         → EN «…» (без точки), RU «….» (с точкой);
  - финал внутреннего переноса JA  → «…» в обоих языках (строка ещё
    продолжается);
  - финал JA «……» без «。»         → «…» (в вопросах «…?»).
Мысли — без скобок (PROMTS.md §8); цитаты в EN — одинарные '…'
(PROMTS.md §10). Реплика в сценарии — одна строка (в модуле — \\n).

Обращения: 平賀くん → Hiraga-kun, ルイズさん → Louise-san, ダーリン →
my darling (Кирхе → Сайто), ノエル → Noelle, キュルке → Kirche,
モンモン → Montmon (モンモранシー → Montmorency), 女王様 → the Queen.

Термины: 爆弾使い → 'bomb user' (первая встреча в tl, PROVISIONAL),
暫定 → provisional, ハッピーエンド/バッドエンド → happy ending / bad ending
(PROVISIONAL, первая встреча в tl), 上げ底 → padding, 芝居 → play,
立ち稽古 → proper rehearsals (PROVISIONAL), 配役 → casting,
王国万歳 → 'Long live the kingdom!'.

Пункты меню — отдельные строки источника (selectItem), не повторяют
первой реплики ветки — свои EN/RU.

??? (см. отчёт reports/ch5/5.md):
  - 15966 «敌の王族である王子との結婚は許さないとも主張してきたの» —
    дословный перевод; смысловой конфликт с 15967 (RECONCILE, JA не правится);
  - s_025 「ルイズの代わりに言っておくよ» → «I'll say it in Louise's place»;
  - t_001 くいくい → «Kui kui.» (PROVISIONAL, транслитерация).
"""

EN_DIALOGS = {
    # ===== SCENE 320 =====
    "ch5.5_l_001": "Hah… practice again today.\nPractice again tomorrow…\nEven so, something still feels unresolved.",
    "ch5.5_l_002": "…Oh?\nHaruna, you were here?",
    "ch5.5_ha_001": "A-Ah!",
    "ch5.5_l_003": "W-What!\nIt's me!\nMe!",
    "ch5.5_l_004": "…Hold on!\nEh?\nWhy don't you have a chest?",
    "ch5.5_ha_002": "N-no!\nDon't look!",
    "ch5.5_l_005": "…Wh-what is that!\nHaruna, was your chest padded?",
    "ch5.5_ha_003": "S-sorry!",
    "ch5.5_l_006": "Sorry doesn't cut it!",
    "ch5.5_l_007": "B-because of that stuffing,\ndo you know how much my small chest ached —\nor rather, how self-conscious I felt!",
    "ch5.5_ha_004": "Please!\nKeep it a secret from everyone!",
    "ch5.5_l_008": "…….",
    "ch5.5_ha_005": "…….",
    "ch5.5_l_009": "…Honestly, what am I to do with you.\nAll right, I get it.\nI'll keep your secret.",
    "ch5.5_ha_006": "…Th-thank you…",
    "ch5.5_ha_007": "…Once, for the sake of appearances…\none pad, then another —\nbefore I knew it there was no going back…\nand finally…",
    "ch5.5_l_010": "…O-oh.\nSo this is what a pad is?",
    "ch5.5_ha_008": "…Y-yes.\nYou put them on like this…\nI suppose you'd call it padding…",
    "ch5.5_ha_009": "…It's a girl's secret tool,\nfound in our world.",
    "ch5.5_l_011": "…H-hm.\nOdd shape.",
    "ch5.5_l_012": "…….",
    "ch5.5_l_013": "…B-but.\nIt's wonderful.",
    "ch5.5_l_014": "It's just now, for the first time,\nI felt interest and respect for the world Saito was in.",
    "ch5.5_ha_010": "I thought I didn't need them anymore,\nbut Hiraga-kun seems to like girls\nwith big chests, so…",
    "ch5.5_l_015": "Right.\nHe pretends not to be interested,\nbut it's obvious.",
    "ch5.5_ha_011": "Louise-san, I'm sorry.",
    "ch5.5_l_016": "No, it's all right, Haruna.\nIt's all that stupid dog's fault.\nHe doesn't understand girls' feelings.",
    "ch5.5_ha_012": "That's right.",
    "ch5.5_l_017": "…Pfft, heh heh heh.",
    "ch5.5_ha_013": "Ah ha, ah ha ha ha…",
    "ch5.5_s_001": "They sure seem to be enjoying themselves, huh?\n…What were those two talking about?",
    "ch5.5_d_001": "Partner.\nWell — better not to ask, as they say.",
    "ch5.5_s_002": "What's that supposed to mean?",
    # ===== SCENE 321 =====
    "ch5.5_w_001": "Everyone, attention!",
    "ch5.5_w_002": "The script is done, and you've come a long way\nwith the basics, so I'd like to move on\nto proper rehearsals.",
    "ch5.5_ha_014": "E-at last…?",
    "ch5.5_si_001": "We did it, everyone.",
    "ch5.5_w_003": "…Well, since those who aren't here\ncan't be helped —\nhere are the main roles as I picture them now.",
    "ch5.5_si_002": "So — what happens then?",
    "ch5.5_w_004": "Oh — but first, the plot of the second half…",
    "ch5.5_w_005": "By the time their love had advanced as far as\nthe prince's proposal, an epidemic breaks out in the girl's homeland —\nthe enemy kingdom — and the royal family all perish.",
    "ch5.5_w_006": "The panicked enemy country looks for an heir\nand finally finds Noelle.\nIt immediately pressures the girl to return home at once.",
    "ch5.5_w_007": "It also insisted that her marriage\nto the prince of the enemy royal family\nwould not be permitted.",
    "ch5.5_w_008": "The kingdom and Prince Kane keep refusing the demands,\nbut the angry enemy country finally uses its army\nto take Noelle back.",
    "ch5.5_w_009": "The overwhelming enemy army.\nAt last, the royal castle falls…",
    "ch5.5_w_010": "Holding back the enemy soldiers pouring in,\nthe knights cry 'Long live the kingdom!'\nand die, one after another.",
    "ch5.5_w_011": "Prince Kane, wounded in battle,\ntakes Noelle up the tower to make his final confession…\nAnd at the same time, he tells her to leave the castle.",
    "ch5.5_w_012": "But the girl shakes her head.\nEven giving up her throne and life,\nshe answered the prince's confession.",
    "ch5.5_w_013": "Then, surrounded by enemy soldiers,\nthe two leap from the tower and end their own lives.",
    "ch5.5_w_014": "From where the two fell, beautiful white flowers\nbegan to bloom.\n…That's the story.",
    "ch5.5_s_003": "Th-that's it?\nA bad ending?",
    "ch5.5_w_015": "Got some complaint?",
    # ===== SCENE 322 =====
    "ch5.5_s_004": "What a horrible story.",
    "ch5.5_l_018": "What do you mean? It's a good story!",
    "ch5.5_si_003": "That's right, Saito-san!",
    "ch5.5_s_005": "But it's a tragedy!\nNothing beats a happy ending!",
    "ch5.5_l_019": "A happy ending without any reason —\nisn't it just a comedy?!",
    "ch5.5_w_016": "I understand that Saito\nlikes those comedy-style happy endings, though.",
    "ch5.5_w_017": "But I'd like to save that for another performance.\nThis play is a 'tragedy.'",
    # ===== SCENE 323 =====
    "ch5.5_s_006": "No, I think it's a good story.",
    "ch5.5_l_020": "My?\nSaito, can you tell a good story from a bad one?",
    "ch5.5_s_007": "I read quite a lot, you know.\nW-well, so I like to think\nmy eye is reasonably sharp!",
    "ch5.5_w_018": "Is that so.",
    # ===== SCENE 324 =====
    "ch5.5_s_008": "No, I don't really get it.",
    "ch5.5_w_019": "Now, now.\nSaito, that's a problem.",
    "ch5.5_w_020": "Well, next time I'll just have to make you\nread books until you're sick of them, won't I?",
    "ch5.5_s_009": "N-no…\nAnd, well…",
    # ===== SCENE 325 =====
    "ch5.5_w_021": "Now, about the casting…",
    "ch5.5_w_022": "First, our own Prince Kane — you, Saito!",
    "ch5.5_s_010": "…Whaaat!?\nM-me?",
    "ch5.5_w_023": "The heroine, the girl Noelle — you, Louise!",
    "ch5.5_l_021": "…Ufufu, of course!",
    "ch5.5_w_024": "However — provisional!",
    "ch5.5_l_022": "…Eh?\nW-wait!\nWhat do you mean, provisional?!",
    "ch5.5_w_025": "Everyone's still rough, but they've got the right stuff.\nDepending on how the other candidates turn out,\nI may swap you out.",
    "ch5.5_w_026": "I need a little more time before the final decision.",
    "ch5.5_k_001": "Oh my?\nThen I might still have a shot at the lead?",
    "ch5.5_l_023": "Kirche!",
    "ch5.5_m_001": "Louise as the lead\nover me — that's impossible.",
    "ch5.5_g_001": "Y-you, the lead…\nU-unforgivable!",
    "ch5.5_s_011": "Everyone!",
    "ch5.5_w_027": "…Never mind.\nEverything is decided on merit alone.\nYou all truly have a chance.",
    "ch5.5_k_002": "What a generous decision.",
    # ===== SCENE 326 =====
    "ch5.5_s_012": "I'm glad for you.\nKirche, Montmon!",
    "ch5.5_k_003": "Oh, thank you.\nMy darling.",
    "ch5.5_m_002": "Well, it'll be work making up the lost ground, though.",
    "ch5.5_l_024": "…Saito, one moment.\nDoes that mean you're dissatisfied\nwith me as the heroine?",
    "ch5.5_s_013": "N-no, that's not what I mean at all…",
    # ===== SCENE 327 =====
    "ch5.5_s_014": "Don't underestimate us —\nyou had us do nothing but grueling basics!",
    "ch5.5_k_004": "Oh my, quite the confidence.\nMy darling.",
    # ===== SCENE 328 =====
    "ch5.5_s_015": "U-um.\nIs there a chance my role could be swapped too?",
    "ch5.5_w_028": "Of course there is.\nLike I said just now.\nIt's provisional through and through.",
    "ch5.5_w_029": "Besides, sometimes a woman plays the part.\nDon't get complacent.",
    # ===== SCENE 329 =====
    "ch5.5_w_030": "…The final roles, including the rest of the cast,\nwill be announced another day.",
    "ch5.5_w_031": "Now, work hard at rehearsal.\nDismissed!",
    # ===== SCENE 330 =====
    "ch5.5_k_005": "Well then — good work, everyone!",
    "ch5.5_l_025": "…What's with you, Kirche.\nYou were complaining the whole time,\nbut lately you've gone completely zealous?",
    "ch5.5_k_006": "…Oh my, I've never been one\nto mind this sort of thing, to begin with.",
    "ch5.5_l_026": "Easy for you to say.\nEven though you ran away halfway…",
    "ch5.5_k_007": "That's…!",
    "ch5.5_t_001": "Kui kui.",
    "ch5.5_k_008": "That's true.",
    "ch5.5_k_009": "…By the way.\nSay, my darling.",
    "ch5.5_s_016": "What is it, Kirche?",
    "ch5.5_k_010": "Haven't you forgotten something?\nSomething very important.",
    "ch5.5_s_017": "Eh?\nSomething I forgot?",
    # ===== SCENE 331 =====
    "ch5.5_s_018": "Do you mean looking for\n'the bomb user' the Queen asked me about?",
    "ch5.5_k_011": "Correct.",
    # ===== SCENE 332 =====
    "ch5.5_s_019": "Do you mean that today\nis Kirche's birthday?",
    "ch5.5_k_012": "I'm sorry.\nToday isn't that day.",
    "ch5.5_k_013": "The answer is: what happened to\nfinding 'the bomb user'?",
    # ===== SCENE 333 =====
    "ch5.5_s_020": "Could it be that my footwork\nin the dance wasn't good today?",
    "ch5.5_k_014": "Hmm.\nNo, that's not it.",
    "ch5.5_k_015": "The answer is: what happened to\nfinding 'the bomb user'?",
    # ===== SCENE 334 =====
    "ch5.5_s_021": "Crap.\nI've been so busy with practice lately\nI haven't been able to look around at all.",
    "ch5.5_s_022": "I-I have to tell Louise\nabout this…",
    "ch5.5_t_002": "…It's fine.",
    "ch5.5_s_023": "…Eh?",
    "ch5.5_k_016": "…Aah, you didn't have to give me away so soon.\nI wanted to watch my darling squirm\na little longer…",
    "ch5.5_s_024": "Kirche.\nYou could have just told me so.",
    "ch5.5_k_017": "Well, you know Louise —\nwhen she gets going, she goes straight ahead, doesn't she?",
    "ch5.5_k_018": "Besides, that girl isn't good\nat asking others for favors,\nso we just kept quiet.",
    "ch5.5_t_003": "Just covering your embarrassment.",
    "ch5.5_k_019": "Th-that's not it!",
    "ch5.5_s_025": "Kirche, thanks.\nI'll say it in Louise's place.",
    "ch5.5_k_020": "Honestly, my darling.",
}

EN_THOUGHTS = {
    "ch5_5_th_001": "Even after that, the days of practice continued.",
    "ch5_5_th_002": "The little princess's behavior on her daily visits is mystery enough,\nbut it's just as mysterious that Kirche, Montmorency,\nand Guiche haven't come back.",
    "ch5_5_th_003": "Who knows how this will turn out…",
    "ch5_5_th_004": "They're comics, though.",
    "ch5_5_th_005": "…….",
    "ch5_5_th_006": "And then the days of preparing and rehearsing for the show\nflew by in a blink.",
    "ch5_5_th_007": "According to Tabitha, Kirche, Montmorency,\nand Guiche had looked into\nthe bomb user for me.",
}

EN_CHOICES = {
    "322": "What a horrible story",
    "323": "It's a good story",
    "324": "I don't get it",
    "326": "I'm glad!",
    "327": "Don't underestimate us!",
    "328": "Could my role be swapped too?",
    "331": "Looking for the bomb user?",
    "332": "Kirche's birthday?",
    "333": "My dance footwork?",
}
