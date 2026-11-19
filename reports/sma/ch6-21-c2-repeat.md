# Повторный независимый прагматический аудит C — главы 6–21

Ветка `review/ch6-21`, 2026-11-19. Новый проход с run_id `20261119-05*`, evidence в `reports/sma/ch<N>/chapter/c/`. A/B/Analyzer, прошлые C, отчёты и журнал субагентами не читались. Проверен текст после повторных A и B.

## Итоги

27 находок (0 ERROR, 8 WARNING, 19 CANDIDATE). FIXED **15** — 9 EN (с синхронизацией `old` в JA/RU) и 6 RU с JA-доказательствами прагматического сдвига. Оставшиеся CANDIDATE — PRESERVED, без вкусовых замен.

## Применённые правки

| тип | before → after | JA/основание |
|---|---|---|
| ru | Для случайности это слишком точно. Несомненно, всё было сд → Для случайности это слишком точно. Похоже, всё-таки это бы | JA でしょう = хеджированное умозаключение |
| en | You must take better care of yourself.{#ch7.3_s_020} → Please take better care of yourself.{#ch7.3_s_020} | JA 〜てください = вежливая просьба, не приказ |
| en | Understood. I'll make sure I'm not an obstacle. Do your be → Understood. I'll make sure I'm not an obstacle. I'll do my | JA 頑張ります = самообязательство, не директива |
| en | Fine then. If you won't stop, then we'll defeat you. {#ch8 → Sorry to disappoint you. If you won't stop, then we'll def | JA おあいにくさま = иронично-вежливый отпор |
| ru | Хорошо. Если не остановитесь — победим вас мы. → Жаль вас огорчать. Если не остановитесь — победим вас мы. | JA おあいにくさま = иронично-вежливый отпор |
| en | (Even the Princess, who laughed at first, has lately been  → (Even the Princess, who laughed at first, is said to be cl | JA らしい = эвиденциальность/слух |
| ru | Даже принцесса, что сначала смеялась, в последнее время де → Даже принцесса, что сначала смеялась, по слухам, в последн | JA らしい = слух, не факт |
| en | …It was a rough night.{#ch15_m_001} → …You've had a rough time.{#ch15_m_001} | JA おつかれさま = признание усилий собеседника |
| ru | …Тяжёлая была ночь, да? → …Ты натерпелся. | JA おつかれさま = утешение/признание, не констатация |
| en | …So that's the mistress's decision. I refuse!{#ch18_s_142} → …So that's the mistress's decision, is it? I refuse!{#ch18 | JA そうかい…か = обиженный риторический вопрос |
| en | I know. I know it, but…{#ch19_s_272} → I know. I should know it, but…{#ch19_s_272} | JA 分かってるはず = должен знать |
| en | I keep thinking there must have been another way…{#ch21_si → I keep thinking there might have been another way…{#ch21_s | JA んじゃないかって = осторожное раздумье |
| ru | Это не шутка!! Об этом не может быть и речи! → Да вы что!! Ни в коем случае!! | JA 冗談じゃないわ = негодующее возражение |
| en | I'm not angry!{#ch11_l_037} → I'm not angry or anything!{#ch11_l_037} | JA なんか + わよ = защитно-капризное отрицание |
| ru | Я не злюсь! → Я вовсе не злюсь, ничего такого! | JA 怒ってなんかないわよ |

## RECHECK

- `check_renpy_syntax.py` OK; `check_project.py` RESULT: OK errors=0; `check_typography.py --lang ru` по всем 16 главам — 0 ошибок; UTF-8 без U+FFFD; JA `new` не трогался.

## Состояние

- Ветка подтверждена: `review/ch6-21`; повторный проход C завершён по всему диапазону.
