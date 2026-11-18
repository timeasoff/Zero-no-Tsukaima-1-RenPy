# Независимый смысловой аудит A (лексическая точность) — проектные главы 6–21

Запуск: 2026-11-18. Ветка: `review/ch6-21` (изолированный worktree `/workspace/.tmp/opencode/review-ch6-21`).
Специализация: A — лексическая точность и оттенки; проверены обе пары JA→EN и JA→RU независимо.
Все 16 проходов A работали изолированно (evidence-only); чужие evidence/отчёты/журналы до завершения диагностики не читались.

## Итоги по главам

| глава | evidence run_id | находок | FIXED | сохранено |
|---|---|---|---|---|
| 6 | `20261118-073608-a72d` | 7 | 4 | 3 |
| 7 | `20261118-073608-ac08` | 8 | 3 | 5 |
| 8 | `20261118-073609-7c86` | 14 | 11 | 3 |
| 9 | `20261118-073609-1830` | 8 | 4 | 4 |
| 10 | `20261118-073610-5f5e` | 9 | 6 | 3 |
| 11 | `20261118-073610-e8b5` | 11 | 3 | 8 |
| 12 | `20261118-073610-fcf8` | 10 | 6 | 4 |
| 13 | `20261118-073611-8bd5` | 8 | 7 | 1 |
| 14 | `20261118-073611-b434` | 6 | 3 | 3 |
| 15 | `20261118-073611-5a00` | 4 | 2 | 2 |
| 16 | `20261118-073611-eb65` | 5 | 3 | 2 |
| 17 | `20261118-073612-a0e8` | 8 | 2 | 6 |
| 18 | `20261118-073612-f34f` | 8 | 4 | 4 |
| 19 | `20261118-073612-2c29` | 5 | 3 | 2 |
| 20 | `20261118-073613-8e9e` | 5 | 2 | 3 |
| 21 | `20261118-073613-a325` | 5 | 5 | 0 |

**Итого:** 121 находок; FIXED 68; сохранено 53.

## Применённые исправления с JA-доказательствами

| ч/часть | строка | пара | JA-основание | было → стало |
|---|---|---|---|---|
| 8/1 | 487 | EN/RU | 良くないしらせ bad news (EN polarity) | Sounds like there's some bad news…{#ch8_l_008} |
| 8/1 | 454 | EN/RU | ついててもらう have Siesta attend | Right. / Let's have Siesta stay with the Princess.{#ch8_l_007} |
| 8/3 | 247 | EN/RU | ご武運を wish luck in battle | Yes! Good luck in battle, Saito-san…! {#ch8_si_013} |
| 8/3 | 647 | EN/RU | 未熟 inexperienced; subject I, not you | I never imagined I'd be defeated by a queen I looked down on as inexperienced!{#ch8_w_024} |
| 10/2 | 458 | EN/RU | Nunca -> Никогда | Я собиралась немного изучить кулинарию, хотя? / Никогда не думала, что научусь именно так, / даже не предполагала. |
| 11/4 | 136 | EN/RU | duplicate of previous RU line | В прошлый раз из-за подготовки к представлению почти не было возможности поговорить с тобой по-настоящему. |
| 12/3 | 506 | EN/RU | あなたがわたしに subject inversion | In other words, you're saying 'I love you' to me!{#ch12_ak_064} |
| 13/2 | 131 | EN/RU | こんばんわ。お１人？ dropped | Людям, видно, тоже непросто собраться… О, добрый вечер. Вы один? |
| 14/3 | 705 | EN/RU | おにいちゃんを object, not me | O-Onii-chan. Don't be mean to him…{#ch14_k_084} |
| 15/1 | 352 | EN/RU | まったく、なんで俺がこんな目に | Чёрт, почему именно мне всё это выпадает… |
| 16/1 | 903 | EN/RU | うふふ！ replaced by previous line text | Уф-фу! |
| 17/1 | 905 | EN/RU | 現在の位置 + 二日と少々 | Judging from their current position, the fleet will enter Tristain's airspace in a little over two days.{#ch17_soldier_007} |
| 21/4 | 721 | EN/RU | ご主人様の作る料理 cook is mistress | What! Simply being able to eat the food your mistress makes should be thanks enough!{#ch21_l_075} |
| 6/1 | 19 | EN/RU | 足が棒になる stiffness | Фух, ноги прямо деревянные… |
| 6/1 | 365 | EN/RU | 何もできません categorical | Эм-м, я-я ничего не могу, но если чем-то помогу…! |
| 6/2 | 96 | EN/RU | 結構 moderate degree | Именно. Люди, знаете ли, довольно безответственное говорят. В интернете то же самое. |
| 6/2 | 175 | EN/RU | そう言えばそうでしたね confirmation only | А, точно. Ты и правда права. |
| 7/2 | 400 | EN/RU | きゃあっ shriek of fright | Ах! |
| 7/1 | 321 | EN/RU | ちょっと annoyed, not apology | Ну! «Просто так» — что это вообще значит, «просто так»? |
| 7/3 | 204 | EN/RU | でれでれ顔 lovelorn | Просто бесит его глупое жалкое влюблённо-томное лицо! |
| 8/3 | 316 | EN/RU | はっ military yes-sir | Есть! С утра у восточной батареи идут мелкие сражения. |
| 8/3 | 607 | EN/RU | 無念 chagrin; 牙と爪 fangs/claws | Come then! All I have left are the fangs and claws of my resentment and rage! Take this!! {#ch8_w_021} |
| 8/3 | 655 | EN/RU | 生き恥をさらす + とどめを刺しなさい plea | Then at this point, no mercy for the defeated! I won't live in shame — finish me off with one blow! {#ch8_w_025} |
| 9/1 | 50 | EN/RU | 根に持つ hold a grudge | Фу-у… / Прошло уже немало времени, / а Луиза всё ещё таит на меня зло. |
| 9/1 | 54 | EN/RU | 不可抗力 irresistible, not chance | Я же говорю: поцелуй принцессы — я не мог ничего поделать… |
| 9/1 | 189 | EN/RU | 人目を忍んで unseen | Простите, я думал, вы мне помогаете, / но, пожалуйста, будьте осторожнее — чтобы никто не заметил. |
| 9/1 | 606 | EN/RU | 心苦しい heartache, not awkward | Тогда мне будет горько. |
| 10/2 | 669 | EN/RU | 慣れない unfamiliar, not habitual | Чем непривычная работа горничной, / желаемая работа лучше… |
| 10/2 | 322 | EN/RU | はあ sigh, next line ため息 | Хаа… |
| 10/1 | 239 | EN/RU | 優等生 model student | Ты и в самом деле отличница. |
| 10/1 | 828 | EN/RU | と、とっても stutter position | О-очень красиво почищена, / это потрясающе. |
| 10/2 | 583 | EN/RU | こちらにいる is here | Well, I heard that Miss Haruna, who played the heroine in that performance, is here. {#ch10_w_003} |
| 11/1 | 43 | EN/RU | 起きる時間 time to rise | Ugh, what? It's not time to get up yet.{#ch11_s_001} |
| 11/3 | 569 | EN/RU | いらないんじゃない？ no toss action | We don't need it, do we?{#ch11_3_c_485_3} |
| 12/3 | 824 | EN/RU | 女の戦い women's fight | My my, it seems the fight between the women has only just begun.{#ch12_h_015} |
| 12/4 | 115 | EN/RU | あなたにも使っていた she used on you too | Заклинание, что смущает чужие сердца, которым она пользовалась и на тебе тоже, в этой стране запрещено… |
| 12/1 | 901 | EN/RU | 何度でも no fixed number | If I said it was a lie, would this reality change? Then I'd say it again and again. I am Akina.{#ch12_ak_007} |
| 12/1 | 122 | EN/RU | いわれても refusal to hear | T-Don't say that to me!{#ch12_1_c_510_3} |
| 13/1 | 246 | EN/RU | わたしが使う use everyone else | Т-Тогда взамен! Я использую всех остальных! |
| 13/1 | 864 | EN/RU | 不潔 filthy, not shameless | H-How filthy!{#ch13_l_032} |
| 13/2 | 57 | EN/RU | むっ、胸が、でありますかっ！ dropped | Хм, сердце!? Должно быть, это очень тревожно! |
| 13/2 | 74 | EN/RU | 鼻の下のばし leaching look | (Oh boy. That soldier is drooling over Kirche…){#ch13_s_053} |
| 13/2 | 719 | EN/RU | 照れちまう embarrassment, not shame | Как-то неловко мне… |
| 13/3 | 249 | EN/RU | 名に賭けて oath | As a mage of the 'fire' attribute… I stake my name — Kirche of the Slight Fever — on it…{#ch13_k_102} |
| 14/2 | 34 | EN/RU | 見張り keeping watch | Думаешь? Замок наверняка входит в конечную цель. Возможно, она пришла наблюдать за замком. |
| 14/4 | 571 | EN/RU | ちょっと待て、おまえら dropped | Подождите, вы двое. Вы меня за кого принимаете?! |
| 15/3 | 477 | EN/RU | ち、ちょっと hey, not touche | H-Hey, Louise! That's too much!{#ch15_m_013} |
| 16/1 | 770 | EN/RU | たまらなかった can't resist | Хотя тот дисбаланс был просто неотразим… |
| 16/1 | 112 | EN/RU | のよ……？ question modality | Listen, Valliere. The bigger the obstacle, the more my flame of love burns…?{#ch16_k_007} |
| 17/1 | 693 | EN/RU | ひどく intensifier | What, Louise. You look really depressed… Maybe I'm wrong?{#ch17_s_038} |
| 18/4 | 133 | EN/RU | ばか野郎 rough insult | Идиотка! |
| 18/4 | 911 | EN/RU | やっつける beat up | Всё хорошо! Я точно разделаюсь с тем кораблём! |
| 18/2 | 1148 | EN/RU | 時間稼ぎ役 playing for time | Мы с Табасой продержимся довольно долго. Только роль того, кто выигрывает время, обидна… |
| 18/1 | 212 | EN/RU | 暴れてる no 'слегка' | Харуна буйствует. |
| 19/2 | 202 | EN/RU | バチは当たらない no sin | W-What… It's not as if worrying about your own familiar is a sin, is it?{#ch19_l_231} |
| 19/1 | 810 | EN/RU | 心強い reinforced by ally | Да. С Табасой я чувствую себя увереннее — она надёжная опора. |
| 20/1 | 542 | EN/RU | 気に入って liked me | Нет. Кто-то из другой труппы, кто смотрел тот спектакль, я им понравилась — и меня завербовали. |
| 20/1 | 500 | EN/RU | どうかな wondering, not certain | Yeah. I can't stay at this academy forever… I've been wondering whether it's right to keep relying on Louise and the others.{#ch20_ha_001} |
| 21/1 | 304 | EN/RU | 興ざめ mood spoiled | Hmph, our tea time is ruined. I've completely lost the mood for it. Let's go, Montmorency.{#ch21_g_004} |
| 21/3 | 1029 | EN/RU | 腕一本で何とかしやがれ sarcastic challenge | Hah… Just one village girl — handle her with that one arm of yours, I'm telling you. Figure it out yourself.{#ch21_d_018} |
| 21/2 | 609 | EN/RU | 死んでも emphasis | Who said she's your lover? My familiar can do what she likes, but I absolutely refuse to hand her over to you, even if it kills me!{#ch21_l_040} |
| 21/2 | 965 | EN/RU | 淡々と calmly, not seriously | No, would you all stop calmly steamrolling ahead with this!{#ch21_s_084} |

## Не применённые находки (classification / disposition)

Каждая CANDIDATE — локальная неоднозначность оттенка без прямого JA-опровержения текущего варианта: `PRESERVED — ???`. WARNING без правки — различие не доказано однозначно: `PRESERVED — FUNCTIONAL`. Список (ч/часть:строка, severity, причина):

- 6/1:696 [CANDIDATE] JA->RU — Сдвиг мимического оттенка: «лицо расползлось/разгладилось» → «довольное лицо» → PRESERVED — ???
- 6/2:213 [CANDIDATE] JA->RU — Модальный сдвиг: утверждение с вопросительной концовкой → предположение с «наверное» → PRESERVED — ???
- 6/3:195 [CANDIDATE] JA->RU — Интонационно-эмоциональный сдвиг смеха: тихий застенчивый смех → громкий «Ха-ха» → PRESERVED — ???
- 7/1:326 [CANDIDATE] JA->RU — 解決 (разрешить/уладить) заменено на «объяснить» → PRESERVED — ???
- 7/2:754 [CANDIDATE] JA->RU — Презрительное обращение 貴様ら сведено к нейтральному «вы» → PRESERVED — ???
- 7/2:651 [CANDIDATE] JA->RU — 驚く (удивиться) усилено до «перепугаться» → PRESERVED — ???
- 7/2:146 [CANDIDATE] JA->RU — 慌てて (поспешно/в суматохе) мотивировано страхом → PRESERVED — ???
- 7/3:199 [CANDIDATE] JA->RU — 心細い (одиноко/беспомощно) окрашено как «страшно» → PRESERVED — ???
- 8/3:473 [CANDIDATE] JA->RU — Emphatic 必ず (without fail) replaced by a wish for safety → PRESERVED — ???
- 8/3:78 [CANDIDATE] JA->EN — Trembling/rattling onomatopoeia rendered as a complaint sound → PRESERVED — ???
- 8/3:271 [CANDIDATE] JA->RU — First-person resolve 頑張ります ('I'll do my best') -> 'Удачи' ('good luck' to others) → PRESERVED — ???
- 9/1:612 [CANDIDATE] JA->RU — Потеря модально-смыслового компонента «褒美» (вознаграждение) → PRESERVED — ???
- 9/1:500 [CANDIDATE] JA->RU — Лексический сдвиг: «повод/зацепка/шанс» → «способ» → PRESERVED — ???
- 9/1:378 [CANDIDATE] JA->RU — Двойной сдвиг: 楽しい (наслаждение) → «забавно» (комизм); いいのかなって (сомнение) → «правда?» → PRESERVED — ???
- 9/1:496 [CANDIDATE] JA->RU — Оттенок предвкушения ослаблен до констатации радости → PRESERVED — ???
- 10/1:1114 [CANDIDATE] JA->RU — Усиление степени: «生活力» (бытовая компетентность) → «навыки выживания» → PRESERVED — ???
- 10/2:614 [CANDIDATE] JA->RU — Неверное значение «話»: «предложение/дело» переведено как «история» → PRESERVED — ???
- 10/2:591 [CANDIDATE] JA->EN — Подмена объекта: «собрать [её] в нашу труппу» → «scout the theater troupe» (вербовать саму труппу) → PRESERVED — ???
- 11/1:155 [CANDIDATE] JA->RU — Потеря наречия степени «ずいぶん» → PRESERVED — ???
- 11/1:155 [CANDIDATE] JA->EN — Потеря наречия степени «ずいぶん» → PRESERVED — ???
- 11/2:81 [CANDIDATE] JA->RU — «大騒ぎ» (переполох/суматоха) → «паника» → PRESERVED — ???
- 11/2:246 [CANDIDATE] JA->RU — Утверждение → побуждение → PRESERVED — ???
- 11/2:275 [CANDIDATE] JA->RU — «難しい顔» (серьёзное/озабоченное лицо) → «мрачный вид» → PRESERVED — ???
- 11/3:174 [CANDIDATE] JA->RU — Согласие → вероятность → PRESERVED — ???
- 11/3:553 [CANDIDATE] JA->RU — Удивлённое «あれ？」 → оклик «Эй?» → PRESERVED — ???
- 11/4:235 [CANDIDATE] JA->RU — Переносное давление → физическое прижатие → PRESERVED — ???
- 12/1:88 [CANDIDATE] JA->EN — Сдвиг оттенка: 生返事 (вялый/рассеянный ответ) → «answered too slowly» → PRESERVED — ???
- 12/1:334 [CANDIDATE] JA->RU — Ослаблена степень кашля: ゲホゲホ → лёгкое «кхм» → PRESERVED — ???
- 12/2:165 [CANDIDATE] JA->RU — 優等生ぶり (образ примерной ученицы) сужено до «прилежание» → PRESERVED — ???
- 12/3:527 [CANDIDATE] JA->EN — 鈍感 (тупость к намёкам) заменено общим «Idiot» → PRESERVED — ???
- 13/4:252 [CANDIDATE] JA->EN — Пропущено восклицание «しまった» (внезапная тревога) → PRESERVED — ???
- 14/1:306 [CANDIDATE] JA->RU — 警戒 (being wary / on guard) → «беспокоит» (worries / concerns) → PRESERVED — ???
- 14/4:88 [CANDIDATE] JA->RU — Потеря каузативного оттенка «довести Кирке до такого состояния» → PRESERVED — ???
- 14/4:490 [CANDIDATE] JA->RU — もやもや (смутное, неясное, тягостное чувство) сведено к нейтральному «чувство» → PRESERVED — ???
- 15/4:31 [CANDIDATE] JA->RU — Пропущено обращение 相棒 («напарник») → PRESERVED — ???
- 15/4:178 [CANDIDATE] JA->RU — Усиление эмоциональной окраски: 年増 → «старухи» → PRESERVED — ???
- 16/1:793 [CANDIDATE] JA->RU — Потеря оттенка «絶妙» → PRESERVED — ???
- 16/1:505 [CANDIDATE] JA->RU — Лексический оттенок «スカウト» → PRESERVED — ???
- 17/1:904 [ERROR] JA->EN — Подмена смысла: «current position» → «current speed» → PRESERVED — FUNCTIONAL
- 17/1:904 [ERROR] JA->EN — Инверсия количества: «чуть больше двух дней» → «чуть меньше двух дней» → PRESERVED — FUNCTIONAL
- 17/2:245 [CANDIDATE] JA->EN — Конкретное действие заменено общим: 洗濯 (стирка) → «clean» → PRESERVED — ???
- 17/2:245 [CANDIDATE] JA->RU — Конкретное действие заменено общим: 洗濯 (стирка) → «убирать» → PRESERVED — ???
- 17/2:249 [CANDIDATE] JA->EN — Завышение степени: 一人前 (компетентна/полноценная) → «prodigy» → PRESERVED — ???
- 17/2:249 [CANDIDATE] JA->RU — Завышение степени: 一人前 (компетентна/полноценная) → «настоящий мастер» → PRESERVED — ???
- 18/2:700 [CANDIDATE] JA->RU — Потеря конкретной эмоции «угрызения/вины» → PRESERVED — ???
- 18/2:594 [CANDIDATE] JA->RU — «怒って» (злость) заменено на «дулась» (обида) → PRESERVED — ???
- 18/2:700 [CANDIDATE] JA->EN — Потеря конкретной эмоции «угрызения/вины» → PRESERVED — ???
- 18/2:594 [CANDIDATE] JA->EN — «怒って» (злость) заменено на «sulked» → PRESERVED — ???
- 19/1:104 [CANDIDATE] JA->EN — Потеря самоуничижительного оттенка はしくれ → PRESERVED — ???
- 19/1:104 [CANDIDATE] JA->RU — Потеря самоуничижительного оттенка はしくれ → PRESERVED — ???
- 20/1:105 [CANDIDATE] JA->EN — Добавлена оценичная деталь «like an idiot», которой нет в JA в явном виде → PRESERVED — ???
- 20/1:647 [CANDIDATE] JA->RU — «フラフラしてる» (шляется/слоняется) заменено на «отлыниваешь» (сачкуешь/уклоняешься) → PRESERVED — ???
- 20/1:666 [CANDIDATE] JA->RU — Обобщённое «拘束具» (средства удержания) сужено до конкретного «наручники» → PRESERVED — ???

## Проверки после правок

- `python tools/check_renpy_syntax.py` → OK (5 предсуществующих NO_RPY-предупреждений для пустых глав 24–28).
- `python tools/check_project.py` → RESULT: OK, errors=0 (warnings=928 — предсуществующие).
- `check_typography.py` — EN/RU по ч6–21: ошибки только предсуществующие (`...` в ч6_2/ч10_2, скобочные мысли в ч9_1); на исправленных строках новых ошибок нет.
- UTF-8: 346 файлов `.rpy` проверены строгим декодированием, U+FFFD = 0.
- Японский `new` в `game/tl/japanese/` не изменялся (только `old` синхронизирован с новой EN-строкой).

## Критическое наблюдение (НЕ исправлялось — вне зоны аудита A)

У 50 из 54 TL-файлов, затронутых правками, заголовок `translate japanese/russian strings:` закомментирован (`# translate … strings:`). Следствие: RU-правки и синхронизированные `old` в этих файлах **не применяются движком**, пока заголовок не будет раскомментирован владельцем этой области. EN-правки в `game/chapters/**/*.rpy` активны независимо. Проблема предсуществующая, ранее зафиксирована в `reports/log.md` (2026-11-18) как отложенная; аудит A её не исправлял — это не лексическая ошибка, а состояние архитектуры TL. Затронуты файлы глав 10–21 (JA и RU); файлы глав 8–9 активны. Перед приёмкой результатов аудита владелец области должен раскомментировать заголовки и прогнать компиляцию Ren'Py SDK.

## Состояние задачи

- Ветка подтверждена: `review/ch6-21`, изолированный worktree.
- evidence: `reports/sma/ch<N>/chapter/a/<run_id>.md` (по одному на главу), отчёты частей дополнены.
- Главы 20 (один файл `script-ch20.rpy`) и все остальные проверены полностью; пустых/неготовых частей в диапазоне нет.
