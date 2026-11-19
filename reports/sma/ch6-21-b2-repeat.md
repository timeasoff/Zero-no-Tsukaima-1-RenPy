# Повторный независимый аудит B (контекст, актанты, логика) — главы 6–21

Ветка `review/ch6-21`, 2026-11-19. Новый проход B с новыми run_id `20261119-05*`, evidence в `reports/sma/ch<N>/chapter/b/`. A/C/Analyzer и прошлые B субагентами не читались. Skill B восстановлен из git-истории (удалён коммитом 8d7fee6). Проверен текст после повторного A.

## Итоги

26 находок (2 ERROR, 10 WARNING, 14 CANDIDATE). FIXED **17**: 13 EN (с синхронизацией `old` в JA/RU TL) и 4 RU — с JA/events_full-доказательствами. Оставшиеся CANDIDATE — PRESERVED/USER DECISION, без вкусовых замен. Один MISSING_TRANSLATION (выпавшая мысль в ch8) — USER DECISION: требует добавления новой реплики с голосом.

## Применённые правки

| тип | before → after | JA/основание |
|---|---|---|
| en | Perhaps even more kindly than I believe I deserve…{#ch7.3_h_ → Perhaps even more than I realize…{#ch7.3_h_013} | JA 思っている以上に = больше, чем осознаю |
| en | Did you raid your own village…? {#ch8_w_016} → Did you attack my village… my clan, and force them to tell y | JA 村を……一族を襲ってむりやり聞き出した |
| en | These days girls aren't like that. {#ch10_s_088} → These days girls are like that, aren't they? {#ch10_s_088} | JA あんな感じじゃないの = риторическое подтверждение |
| en | I came to ask whether you might allow us to scout you for ou → I came to ask whether you might allow us to scout her for ou | объект вербовки — Харуна (РА), не собеседник |
| en | it's a good story isn't it. {#ch10_m_005} → it's a good offer, isn't it. {#ch10_m_005} | JA いい話 = хорошее предложение |
| en | I also think it's a good story. {#ch10_choice_016} → I also think it's a good offer. {#ch10_choice_016} | JA いい話 = хорошее предложение |
| en | I also think it's a good story. {#ch10_s_108} → I also think it's a good offer. {#ch10_s_108} | JA いい話 = хорошее предложение |
| en | they say they come to Tristain often, so… {#ch11_ha_016} → Weatherly-san's troupe travels around, but they say they com | JA 旅回りだけど…よく来るらしい — уступка сохранена |
| en | …we could probably catch the enemy off guard… {#ch12_s_051} → …Indeed. Now that the existence of Void is barely known, we  | JA 確かに…虚無の存在が知られてない今なら — условие вывода |
| en | she runs out of magic power instantly. → she runs out of mental energy instantly. | JA 精神力 = психическая энергия, не магическая сила |
| en | Just because the master showed a little concern for his fami → Just because mistress showed a little concern for her famili | JA ご主人様 = Луиза-госпожа, 使い魔 = Сайто |
| en | …She probably has a reason, right? {#ch19_k_047} → With Louise? Well, if Tabitha says so, I guess it can't be h | JA ルイズと？…タバサがそうしろって言うなら — восстановлены звенья |
| en | Who said she's your lover? My familiar can do what she likes → Who said he's your lover? My familiar can do what he likes,  | речь о Сайто (муж. род) |
| ru | Не «что я здесь делаю»! → Не «что ты здесь делаешь»! | JA どうしてこんなところにじゃないよ — отрицание вопроса к собеседнику |
| ru | Здесь много военных. У вас было совещание? → Здесь много военных. Вы как раз в середине совещания? | JA 会議の最中だったんじゃ？ |
| ru | Меня просто попросил старик Осман позвать тебя и Луизу. → Мне просто велел старик Осман позвать тебя и Луизу. | JA 言いつかって = приказ/поручение |
| ru | Два шага. → Двое идут? | JA 足音は二つ = двое идущих |

## RECHECK

- `check_renpy_syntax.py` OK; `check_project.py` RESULT: OK errors=0; `check_typography.py --lang ru` по всем 16 главам — 0 ошибок; UTF-8 без U+FFFD; JA `new` не трогался.

## Состояние

- Ветка подтверждена: `review/ch6-21`; повторный проход B завершён по всему диапазону.
