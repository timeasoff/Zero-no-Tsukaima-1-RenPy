# -*- coding: utf-8 -*-
"""EN-переводы для части ch5.4 (основная линия 315–319 + extra-сцены 1383–1407).

Ключи — имена голосов сценария (ch5.4_<spk>_<NNN>) для реплик,
ch5_4_th_<NNN> для мыслей, номер сцены-варианта (строкой) для пунктов меню.

Смысл и модальность — по JA (ps2_source/events_full/chapter_06_本当の想い.txt,
сцены 315–319 и 1383–1407). Многоточие — «…» (PROMTS.md §5); JA «…….» в
конце реплики → EN «….», JA «……」 внутри фразы → «…». Мысли — без скобок
(PROMTS.md §8). Реплика — одна строка в сценарии (переносы JA склеены).

Обращения: 平賀くん → Hiraga-kun, ダーリン → my darling (Кирхе → Сайто),
使い魔さん → Familiar-san, サイトさん → Saito-san, モンモン → Montmon.

Термины: 統率術 → command magic (PROVISIONAL, в проекте не встречался),
貴族のたしなみ → a noble accomplishment, 素人 → an amateur, 役者 → an actor,
劇団 → a troupe, 舞台 → the stage, 芝居 → the play.

Пункты меню повторяют первую реплику ветки (так в источнике) — совпадения
строк помечаются тегами генератора (E11), дубли не снимаются вручную.
"""

EN_DIALOGS = {
    # ===== SCENE 1383 (extra-блок A) =====
    "ch5.4_w_001": "Why are all the young people these days like this!\nThey have such fine talent,\nand it goes to waste.",
    "ch5.4_si_001": "Saito-san…\nI've been listening to everyone's complaints,\nin that same way, all this time…",
    "ch5.4_w_002": "I'm listening, you know!\nHonestly, the young people these days!",
    # ===== SCENE 1384 (вариант) =====
    "ch5.4_s_001": "That's not true!",
    "ch5.4_s_002": "They're the best of companions.\nI mean, sure, they're spoiled,\nand some of them are hard to stomach…",
    "ch5.4_s_003": "But they're not the sort of people who do things carelessly.",
    "ch5.4_si_002": "Saito-san…",
    "ch5.4_w_003": "It seems I insulted your friend.\nI'm sorry.",
    "ch5.4_s_004": "N-no, this time I do think their spoiledness is to blame too.",
    "ch5.4_s_005": "Well, I think they're overthinking all those complicated things,\nlike their family's standing and whatnot.",
    "ch5.4_w_004": "Well, nobles are like that, you know.",
    # ===== SCENE 1385 (вариант) =====
    "ch5.4_s_006": "Well, you're right.\nThey are spoiled, they don't listen to others,\nand they immediately start talking about commoners.",
    "ch5.4_s_007": "But they're not the sort of people to throw in the towel halfway.\nCan you believe me that much, at least?",
    "ch5.4_si_003": "Saito-san…",
    "ch5.4_w_005": "It seems I insulted your friend.\nI'm sorry.",
    # ===== SCENE 1386 (вариант) =====
    "ch5.4_s_008": "O-oh, it's no use telling me that.\nI'm the one who's always being run around by their spoiled ways!",
    "ch5.4_w_006": "Saito seems to be having a hard time too, doesn't he.",
    # ===== SCENE 1387 (после вариантов) =====
    "ch5.4_si_004": "By the way.\nWhat happened to the other actors?\nI don't see them much.",
    "ch5.4_w_007": "There wasn't an actor who fit the image this time.",
    "ch5.4_w_008": "You, for all you're amateurs, match the image of this play perfectly…\nso I invited you, hoping to make use of you.",
    "ch5.4_si_005": "S-so that's what it was!",
    # ===== SCENE 1388 (extra-блок B) =====
    # ===== SCENE 1389 (вариант) =====
    "ch5.4_t_001": "A book on command magic.",
    "ch5.4_s_009": "U-wha, wha!\nShe noticed!",
    # ===== SCENE 1390 (вариант) =====
    "ch5.4_t_002": "A book on command magic.",
    "ch5.4_s_010": "U-wha!\nShe noticed!",
    # ===== SCENE 1391 (вариант) =====
    "ch5.4_t_003": "A book on command magic.",
    "ch5.4_s_011": "U-woah!\nY-you scared me!",
    # ===== SCENE 1392 (после вариантов) =====
    "ch5.4_s_012": "A book on command magic?",
    "ch5.4_t_004": "The title is 'How to Become the Ideal Boss.'",
    "ch5.4_s_013": "S-so that's what it is.",
    "ch5.4_t_005": "Don't worry — you can do it.",
    "ch5.4_s_014": "Huh?",
    "ch5.4_t_006": "Believe in yourself.",
    "ch5.4_s_015": "A-ah, yes!\nI understand!",
    "ch5.4_s_016": "Thanks, Tabitha!\nI'll give it a try!",
    "ch5.4_t_007": "It really worked.",
    "ch5.4_s_017": "To think Tabitha is cheering me on like that…\nI have to do my best.",
    "ch5.4_d_001": "…Hey, partner.\nAren't you being a bit too simple?",
    # ===== SCENE 1393 (extra-блок C) =====
    "ch5.4_l_001": "Why on earth did you join\na troupe like this?!",
    "ch5.4_h_001": "Oh, but even I am interested in the troupe.",
    "ch5.4_l_002": "B-but that doesn't mean you have to go on stage!",
    "ch5.4_ha_001": "A-Hiraga-kun!",
    "ch5.4_s_018": "…H-how do you do.",
    "ch5.4_h_002": "Thank you for your hard work.\nFamiliar-san.",
    "ch5.4_s_019": "Are you really all right?\nDoing something like this.",
    "ch5.4_l_003": "O-of course I'm not!",
    "ch5.4_h_003": "It's fine…\nAs long as the commoners don't find out.",
    "ch5.4_l_004": "S-such a sloppy thing!",
    "ch5.4_ha_002": "A-but, well.\nEveryone is very good at dancing and acting, aren't they?",
    "ch5.4_l_005": "W-well, dancing is a noble accomplishment…",
    "ch5.4_ha_003": "I see… a noble accomplishment, huh…\nCompared to that, I'm…",
    "ch5.4_d_002": "Partner, say something…\nShe's really getting down on herself?",
    "ch5.4_s_020": "W-well, even if they say that.",
    # ===== SCENE 1394 (вариант) =====
    "ch5.4_s_021": "A girl's value isn't in dancing and stuff!",
    "ch5.4_ha_004": "Eh, really?",
    "ch5.4_s_022": "Just because she's a bit good at dancing\nwhat does that prove!\nHaruna has something Louise doesn't!",
    "ch5.4_l_006": "Saito, I'll ask for comparison.\nWhat does Haruna have that I don't?",
    "ch5.4_s_023": "W-well, that…\nwhat would it be, I wonder.",
    "ch5.4_ha_005": "Hiraga-kun…",
    # ===== SCENE 1395 (вариант) =====
    "ch5.4_s_024": "Why don't you ask Louise?\nAsking Louise about dancing and all that…",
    "ch5.4_ha_006": "Eh?",
    "ch5.4_s_025": "This is a good chance to study what they call a noble accomplishment!",
    "ch5.4_ha_007": "Y-yes, you're right.\nI should take it as a good opportunity.",
    # ===== SCENE 1396 (вариант) =====
    "ch5.4_s_026": "Haruna has her own good points, I tell you!",
    "ch5.4_ha_008": "…M-maybe?",
    "ch5.4_s_027": "M-maybe.",
    "ch5.4_ha_009": "Hehehe… thank you, Hiraga-kun.\nFor cheering me up.",
    # ===== SCENE 1397 (после вариантов) =====
    "ch5.4_l_007": "For now, Saito has to get better at dancing too.\nThe way things stand, he's completely hopeless.",
    "ch5.4_s_028": "G-gee!\nIt really is going to end up like that?",
    "ch5.4_ha_010": "Y-yes, that's right.\nHiraga-kun has to do his best too!",
    "ch5.4_h_004": "Then I'll help out as well.",
    "ch5.4_s_029": "H-help meee!",
    # ===== SCENE 1398 (extra-блок D) =====
    "ch5.4_s_030": "Yo, Kirche.",
    "ch5.4_k_001": "…Eek!\nOh my, what is it?\nMy darling?",
    "ch5.4_s_031": "Um, well, that is…",
    "ch5.4_k_002": "…You're not going back to rehearsal, are you?",
    "ch5.4_s_032": "U-um… no, well… …Yes.",
    "ch5.4_k_003": "Eeeh~.\nWell, it is a bother, you know…",
    # ===== SCENE 1399 (вариант) =====
    "ch5.4_s_033": "A-a bother, you say…? That's no way to talk!",
    "ch5.4_k_004": "Oh, come on.\nStop that…\nYou've just gotten bored of it.",
    "ch5.4_s_034": "You can say that, but!",
    "ch5.4_k_005": "Ufufufu…",
    # ===== SCENE 1400 (вариант) =====
    "ch5.4_s_035": "Hey, come back to rehearsal…",
    "ch5.4_k_006": "I wonder what I should do~?",
    "ch5.4_s_036": "It's obvious — it's only Kirche who shines on stage!",
    "ch5.4_k_007": "…Oh my, my darling thinks so too?",
    "ch5.4_s_037": "I do!\nI do!",
    # ===== SCENE 1401 (вариант) =====
    "ch5.4_s_038": "W-well, I want to slack off too, but…",
    "ch5.4_k_008": "Mmm, I'm not the one slacking off, you know.",
    "ch5.4_s_039": "…Eh?\nWhat do you mean?",
    "ch5.4_k_009": "A-ah!\nN-no, it's fine!\nDon't worry about it!",
    # ===== SCENE 1402 (после вариантов) =====
    "ch5.4_k_010": "Rest easy, my darling.\nThere's a good reason I won't come back.\nI'm just a little busy right now.",
    "ch5.4_s_040": "…Eh?\nWhat do you mean?",
    "ch5.4_k_011": "Yes, yes!\nWe'll continue this another time!",
    "ch5.4_s_041": "W-wait!\nKirche!",
    "ch5.4_k_012": "Bye-bye~.\nMy darling~.",
    "ch5.4_s_042": "O-oi!",
    "ch5.4_s_043": "Ahh, I feel like I've been caught in the smoke.",
    # ===== SCENE 1403 (extra-блок E) =====
    "ch5.4_s_044": "Hey, Montmon.",
    "ch5.4_m_001": "Oh, Saito.\nWhat a coincidence to meet here.",
    "ch5.4_g_001": "Hey, are you ignoring me?!",
    "ch5.4_s_045": "Ah, Guiche is here too…",
    "ch5.4_g_002": "What's with that blatant rudeness?!",
    # ===== SCENE 1404 (вариант) =====
    "ch5.4_s_046": "It's just your imagination.",
    "ch5.4_g_003": "Is that really so?",
    "ch5.4_g_004": "Surely you're not after my Montmorency as well?",
    "ch5.4_m_002": "Eh!",
    "ch5.4_g_005": "W-what are you blushing about?\nMontmorency?",
    "ch5.4_m_003": "S-such a thing…",
    "ch5.4_s_047": "W-well, more important than that!",
    # ===== SCENE 1405 (вариант) =====
    "ch5.4_s_048": "…Don't worry about it!",
    "ch5.4_g_006": "Deny it!",
    "ch5.4_m_004": "It does feel like a rather fitting way to treat me, though.",
    "ch5.4_g_007": "Montmorency!",
    "ch5.4_s_049": "W-well, that matters more!",
    # ===== SCENE 1406 (вариант) =====
    "ch5.4_s_050": "It's always like that, isn't it?",
    "ch5.4_g_008": "You didn't just say something outrageous, did you?",
    "ch5.4_s_051": "A-ah, no.\nI didn't say anything.",
    "ch5.4_g_009": "I see. A mishearing, then.\nHahaha, good.",
    "ch5.4_m_005": "More important than that.\nIt wasn't that you had some business, was it?",
    "ch5.4_s_052": "Yeah.",
    # ===== SCENE 1407 (после вариантов) =====
    "ch5.4_s_053": "Hey, aren't you going back to rehearse on the stage?",
    "ch5.4_m_006": "It's that, after all.\nI'm sorry.\nI can't for a while yet.",
    "ch5.4_s_054": "Well, I imagine being a noble makes a lot of things difficult…",
    "ch5.4_g_010": "A-ah, no!\nThat's a separate matter, it's all right.",
    "ch5.4_s_055": "W-well, then.\nWhy…!",
    "ch5.4_g_011": "N-no, it's, um.\nK-kirche was…",
    "ch5.4_s_056": "Huh?\nKirche?",
    "ch5.4_m_007": "Idiot!",
    "ch5.4_g_012": "Gah!",
    "ch5.4_m_008": "Honestly, you two!\nYou can't keep a secret!",
    "ch5.4_s_057": "M-montmorency!?",
    "ch5.4_m_009": "Once my own affairs are settled, I'll return to the theater,\nso please rest easy.",
    "ch5.4_s_058": "Y-yes…",
    "ch5.4_m_010": "Well then, we must be on our way.\nS-so, bye~.",
    "ch5.4_g_013": "D-don't pull me.\nMontmorency~~~.",
    "ch5.4_s_059": "Ahh!\nThey got away.",
}

EN_THOUGHTS = {
    "ch5_4_th_001": "Oh — Siesta and Weatherby are here.",
    "ch5_4_th_002": "…R-really?",
    "ch5_4_th_003": "By the way…",
    "ch5_4_th_004": "Is that really true?",
    "ch5_4_th_005": "Weatherby-san doesn't seem like someone who would consider it all right\nto hand the leading role to an amateur,\nsomeone who'd be fine with such a bold thing…",
    "ch5_4_th_006": "Well, fine, I guess.",
    "ch5_4_th_007": "Oh — Tabitha's here.",
    "ch5_4_th_008": "…….",
    "ch5_4_th_009": "She's even reading a book at a time like this…",
    "ch5_4_th_010": "What book could she be reading?\nL-let me just peek…",
    "ch5_4_th_011": "It'd be rude to interrupt her reading…\nMaybe I should back off?",
    "ch5_4_th_012": "She's reading it with such dedication…",
    "ch5_4_th_013": "Tabitha, quietly reading a book like this…\nshe's like a princess from some country,\nlike a doll…",
    "ch5_4_th_014": "…I-I want to poke her cheek…\nIt looks soft…",
    "ch5_4_th_015": "Swallowed.\nS-slowly…",
    "ch5_4_th_016": "I see — she's thinking about it in her own way, Tabitha-style.",
    "ch5_4_th_017": "A-am I being encouraged?",
    "ch5_4_th_018": "Oh — Louise, the princess,\nand Haruna are here too.",
    "ch5_4_th_019": "It's gotten hard to walk away, somehow.\nMaybe I should retreat…",
    "ch5_4_th_020": "Oh — Kirche is here.",
    "ch5_4_th_021": "Guiche and Montmorency are here.",
    "ch5_4_th_022": "…W-what on earth is going on?",
}

EN_CHOICES = {
    "1384": "That's not true!",
    "1385": "Well, you're right.",
    "1386": "It's no use telling me that.",
    "1389": "I wonder what book she's reading?",
    "1390": "It'd be rude to disturb her",
    "1391": "Let me play a prank",
    "1394": "A girl's value isn't in her dancing!",
    "1395": "Why don't you ask Louise?",
    "1396": "Haruna has her own good points!",
    "1399": "A-a bother, you say…",
    "1400": "Hey, come back to rehearsal",
    "1401": "I want to slack off too, but…",
    "1404": "It's just your imagination",
    "1405": "Don't worry about it!",
    "1406": "It's always like that, isn't it?",
}
