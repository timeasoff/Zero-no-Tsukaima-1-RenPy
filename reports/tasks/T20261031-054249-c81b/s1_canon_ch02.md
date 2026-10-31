# S1 — канон-таблица симпатий `chapter_02` + построчная сверка с портом главы 1

Задача: `reports/tasks/prompts/T20261031-054249-c81b_S1.md`.
Дата: 2026-10-31. Ничего в `ps2_source/` и `game/` не изменялось (только чтение).

## 1. Источники и выход

* Канон (смысловый): `ps2_source/chapters/chapter_02_ゼロのルイズ.txt` — 54 события `【好感度】`.
* Канон (точные аргументы движка): `ps2_source/events_full/chapter_02_ゼロのルイズ.txt` — 54 вызова `LIKE like("…", N)`.
* Порт: `game/chapters/1/script-ch1_1..10.rpy` — 73 вызова `update_sympathy`.
* Выход: настоящий отчёт + `sympathy_canon_ch02.csv` (54 строки) + `sympathy_port_ch1_map.csv` (73 строки), UTF-8 без BOM.

**Сверка канон ↔ канон (точность парсера):** последовательности `(персонаж, значение)` в chapters и events_full совпадают полностью (`seq_ok=True`), сцены, вычисленные из заголовков `## SCENE` events_full, совпадают с `---- SCENE ----` chapters во всех 54 случаях (0 расхождений). Оба источника дают одни и те же 54 события.

## 2. Методика сопоставления (voice-id якоря) и её ограничения

Предписанная методика — окно из 2–3 голосовых id слева/справа от события.

**Мост `voice_name → voice_id`.** В `references/voice_id_map.csv` строк глав 0/1 НЕТ (манифест прямо говорит: «Уже созданные .ogg (главы 0/1, extra) строк не требуют») — проверено `grep -c "ch1"` = 0. Взял единственный существующий мост для главы 1: `ps2_source/_diagnostics/voice_scene_map.json` (`voice` → `psv` = `[voice N]` + `scene`). Это отклонение от буквы задания, но не по сути: `psv` там ровно те id, что стоят в `[voice N]` источника.

**Валидация моста (не на веру):** для каждой пары `(voice, psv)` из JSON найдена позиция `[voice psv]` в chapters-файле и вычислена её сцена:
* подтверждено совпадение сцены: **1000**;
* противоречий: **0**;
* неверифицируемых (в JSON `scene/psv = null`): 80.
Дубликаты голосовых имён в JSON: 176 — резолвились в пользу непустого `psv`.

**Алгоритм:**
1. для каждого события канона — окно: 3 `[voice N]` слева + 3 справа **внутри той же сцены** (psv уникальны в главе: 1067 id / 1067 вхождений — пересечение окон у разных событий возможно только при смежности внутри сцены);
2. для каждого вызова порта — окно: 3 `voice "…"` до + 3 после **внутри того же файла**, маппинг имён → psv через JSON;
3. score = размер пересечения множеств psv; пары формировались только при одинаковом `char_key` и score > 0, жадно по убыванию score (bipartite greedy);
4. tie на верхнем score → `AMBIGUOUS` (не «угадываем»);
5. страховочный якорь — «голосовые сцены» ( majority сцен оконных голосов ): **не понадобился ни разу** (0 вызовов без оконного совпадения).

**Ограничения методики (честно):**
* окно вызова порта может захватить голоса соседней опции `menu:` (голоса идут подряд в файле) — это занижает score, но не даёт ложной сцены, потому что `psv` канон-событий соседней сцены в исходном окне не встречаются (id уникальны);
* JSON устарел относительно 5 голосовых имён порта: `ch1.5_l_003-2`, `ch1.7_l_011`, `ch1.7_l_015`, `ch1.7_m_001`, `ch1.8_s_013-2` — плюс 12 прочих имён попадали в окна как `unmapped` (полный список в CSV); ни один из 5 отсутствующих не оказался рядом с `update_sympathy`, fallback не понадобился;
* в окнах порта встречаются split-имена вида `ch1.9_s_005-2` — если JSON отдаёт для них тот же `psv`, что и для базового имени, пересечение слегка «утепляется» симметрично обеим сторонам; на ранжирование это не влияло (все пары, кроме одной, имели строгое преимущество).

**Единственный AMBIGUOUS (и его разрешение).** `script-ch1_9.rpy:98` — окно дало tie: сцена 55 (score 2) = сцена 56 (score 2). Разрешено НЕ позицией, а содержательной сверкой текста:
* опция `«Come on, can't something be done about that?»` = канон `【選択肢】そこをなんとかならないか？` (сцена 54 → **56**) ⇒ `:98` (+20) ↔ сцена 56 (канон +10) → ratio **X2**;
* опция `«Don't say such awful things!»` = канон `【選択肢】そんなひどいこと言うなよ！` (сцена 54 → **55**) ⇒ `:108` (−20) ↔ сцена 55 (канон −10) → ratio **X2**.
Порядок опций в порте **обратен** канону — поэтому позиционное сопоставление здесь дало бы перевёрнутые знаки. Обе строки помечены в CSV флагом `AMBIGUOUS … RESOLVED …` (classification: AMBIGUOUS → disposition: RESOLVED-BY-TEXT, документировано).

## 3. Итог сверки

| метрика | значение |
|---|---|
| канон-событий chapter_02 | 54 |
| вызовов `update_sympathy` в порте | 73 |
| matched | **54** (все 54 канон-события найдены) |
| EXTRA (вызов порта без события канона) | **19** (все — Луиза) |
| MISSING (событие канона без вызова порта) | **0** |
| ratio SAME | 8 |
| ratio X2 (порт = 2× канон) | 39 |
| ratio DIFF | 7 |
| AMBIGUOUS | 1 (разрешён текстом, см. §2) |

Распределение DIFF (все 7 — **Табита**, знак совпадает, величина нет): канон ±15 → порт ±20 (`script-ch1_6.rpy:77`, `script-ch1_8.rpy:211`, `script-ch1_8.rpy:253`, `script-ch1_10.rpy:483`, `script-ch1_10.rpy:512`) и канон +30 → порт +20 (`script-ch1_8.rpy:139`, `script-ch1_10.rpy:341`).
SAME (8) — все «датовые» и «переходные» +20: сцены 1009, 1014, 1024, 1029, 1224, 1229, 1245, 1250.

## 4. Канон-таблица (54 события)

Источник: `chapter_02_ゼロのルイズ` → проектная глава 1. Колонки как в задании; `source_line` = строка в chapters, `events_full_line` = строка в events_full.

| chapter_source | proj_ch | scene | char_ja | char_key | value | branch_kind | menu_owner_scene | choice_text | src_line | ef_line | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| chapter_02_ゼロのルイズ | 1 | 7 | ルイズ | louise | 10 | choice | 6 | いいと思うぜ | 131 | 154 | — |
| chapter_02_ゼロのルイズ | 1 | 8 | ルイズ | louise | -10 | choice | 6 | 悪い！ | 145 | 171 | — |
| chapter_02_ゼロのルイズ | 1 | 12 | ルイズ | louise | 10 | choice | 11 | そんなことできるか | 371 | 360 | — |
| chapter_02_ゼロのルイズ | 1 | 13 | ルイズ | louise | -10 | choice | 11 | 分かった、渡そう | 385 | 375 | — |
| chapter_02_ゼロのルイズ | 1 | 17 | ルイズ | louise | 10 | choice | 16 | なにもしていない！ | 613 | 597 | — |
| chapter_02_ゼロのルイズ | 1 | 18 | ルイズ | louise | -10 | choice | 16 | 記憶にありません | 646 | 623 | — |
| chapter_02_ゼロのルイズ | 1 | 21 | ルイズ | louise | 10 | choice | 20 | ルイズに振る | 829 | 795 | — |
| chapter_02_ゼロのルイズ | 1 | 22 | シエスタ | siesta | 10 | choice | 20 | シエスタに振る | 853 | 816 | — |
| chapter_02_ゼロのルイズ | 1 | 31 | シエスタ | siesta | -10 | choice | 29 | ルイズを起こして説明させよう | 1208 | 1175 | — |
| chapter_02_ゼロのルイズ | 1 | 32 | シエスタ | siesta | 10 | choice | 29 | ここは第三者の証言を！ | 1282 | 1244 | — |
| chapter_02_ゼロのルイズ | 1 | 35 | キュルケ | kirche | 10 | choice | 34 | キュルケに訊ねる | 1452 | 1384 | — |
| chapter_02_ゼロのルイズ | 1 | 36 | タバサ | tabitha | 15 | choice | 34 | タバサに訊ねる | 1486 | 1414 | — |
| chapter_02_ゼロのルイズ | 1 | 37 | シエスタ | siesta | 10 | choice | 34 | シエスタに訊ねる | 1506 | 1436 | — |
| chapter_02_ゼロのルイズ | 1 | 38 | ルイズ | louise | 10 | choice | 34 | ルイズに訊ねる | 1552 | 1475 | — |
| chapter_02_ゼロのルイズ | 1 | 41 | ハルナ | haruna | -10 | choice | 40 | はい | 1867 | 1765 | — |
| chapter_02_ゼロのルイズ | 1 | 41 | シエスタ | siesta | -10 | choice | 40 | はい | 1888 | 1788 | — |
| chapter_02_ゼロのルイズ | 1 | 41 | キュルケ | kirche | -10 | choice | 40 | はい | 1911 | 1811 | — |
| chapter_02_ゼロのルイズ | 1 | 42 | ハルナ | haruna | 10 | choice | 40 | いいえ | 1937 | 1840 | — |
| chapter_02_ゼロのルイズ | 1 | 42 | シエスタ | siesta | 10 | choice | 40 | いいえ | 1939 | 1842 | — |
| chapter_02_ゼロのルイズ | 1 | 42 | キュルケ | kirche | 10 | choice | 40 | いいえ | 1943 | 1844 | — |
| chapter_02_ゼロのルイズ | 1 | 45 | シエスタ | siesta | 10 | choice | 44 | 俺の部屋に来るといいよ | 2133 | 2030 | — |
| chapter_02_ゼロのルイズ | 1 | 46 | シエスタ | siesta | -10 | choice | 44 | キュルケの部屋はどうだ | 2179 | 2069 | — |
| chapter_02_ゼロのルイズ | 1 | 55 | ルイズ | louise | -10 | choice | 54 | そんなひどいこと言うなよ！ | 2546 | 2419 | — |
| chapter_02_ゼロのルイズ | 1 | 56 | ルイズ | louise | 10 | choice | 54 | そこをなんとかならないか？ | 2565 | 2438 | — |
| chapter_02_ゼロのルイズ | 1 | 1009 | ルイズ | louise | 20 | date | 62 | ルイズ | 2926 | 2833 | дата-блок ルイズ: сцены 1009-1013 |
| chapter_02_ゼロのルイズ | 1 | 1010 | ルイズ | louise | 10 | choice | 1009 | すっごくきれいだ | 2968 | 2868 | внутри дата-блока ルイズ (1009-1013), меню даты — сцена 62 |
| chapter_02_ゼロのルイズ | 1 | 1012 | ルイズ | louise | -10 | choice | 1009 | よく分かんねえ | 3016 | 2907 | внутри дата-блока ルイズ (1009-1013), меню даты — сцена 62 |
| chapter_02_ゼロのルイズ | 1 | 1014 | シエスタ | siesta | 20 | date | 62 | シエスタ | 3065 | 2961 | дата-блок シエスタ: сцены 1014-1018 |
| chapter_02_ゼロのルイズ | 1 | 1015 | シエスタ | siesta | 10 | choice | 1014 | いいお嫁さんになれるよ | 3118 | 2998 | внутри дата-блока シエスタ (1014-1018), меню даты — сцена 62 |
| chapter_02_ゼロのルイズ | 1 | 1016 | シエスタ | siesta | -10 | choice | 1014 | 節約家なんだね | 3154 | 3024 | внутри дата-блока シエスタ (1014-1018), меню даты — сцена 62 |
| chapter_02_ゼロのルイズ | 1 | 1019 | タバサ | tabitha | 30 | date | 62 | タバサ | 3223 | 3094 | дата-блок タバサ: сцены 1019-1023 |
| chapter_02_ゼロのルイズ | 1 | 1021 | タバサ | tabitha | -15 | choice | 1019 | 抱っこしてあげよう | 3292 | 3164 | внутри дата-блока タバサ (1019-1023), меню даты — сцена 62 |
| chapter_02_ゼロのルイズ | 1 | 1022 | タバサ | tabitha | 15 | choice | 1019 | 肩を揉んであげよう | 3358 | 3244 | внутри дата-блока タバサ (1019-1023), меню даты — сцена 62 |
| chapter_02_ゼロのルイズ | 1 | 1024 | キュルケ | kirche | 20 | date | 62 | キュルケ | 3403 | 3298 | дата-блок キュルケ: сцены 1024-1028 |
| chapter_02_ゼロのルイズ | 1 | 1026 | キュルケ | kirche | -10 | choice | 1024 | 本気で人を好きになったことは？ | 3535 | 3418 | внутри дата-блока キュルケ (1024-1028), меню даты — сцена 62 |
| chapter_02_ゼロのルイズ | 1 | 1027 | キュルケ | kirche | 10 | choice | 1024 | 俺のこと、どう思ってる？ | 3560 | 3440 | внутри дата-блока キュルケ (1024-1028), меню даты — сцена 62 |
| chapter_02_ゼロのルイズ | 1 | 1029 | ハルナ | haruna | 20 | date | 62 | ハルナ | 3638 | 3522 | дата-блок ハルナ: сцены 1029-1033 |
| chapter_02_ゼロのルイズ | 1 | 1031 | ハルナ | haruna | 10 | choice | 1029 | 夜空を見てた | 3676 | 3561 | внутри дата-блока ハルナ (1029-1033), меню даты — сцена 62 |
| chapter_02_ゼロのルイズ | 1 | 1032 | ハルナ | haruna | -10 | choice | 1029 | 分からない | 3690 | 3576 | внутри дата-блока ハルナ (1029-1033), меню даты — сцена 62 |
| chapter_02_ゼロのルイズ | 1 | 1224 | シエスタ | siesta | 20 | move | 24 | シエスタの部屋 | 3770 | 3664 | корень ветки перемещения |
| chapter_02_ゼロのルイズ | 1 | 1225 | シエスタ | siesta | 10 | choice | 1224 | たぶん、そうかもしれない | 3815 | 3695 | ветка перемещения «シエスタの部屋» (корень сцены 1224, меню — сцена 24) |
| chapter_02_ゼロのルイズ | 1 | 1226 | シエスタ | siesta | -10 | choice | 1224 | よく分からない | 3833 | 3713 | ветка перемещения «シエスタの部屋» (корень сцены 1224, меню — сцена 24) |
| chapter_02_ゼロのルイズ | 1 | 1229 | ルイズ | louise | 20 | move | 24 | ルイズの部屋 | 3901 | 3780 | корень ветки перемещения |
| chapter_02_ゼロのルイズ | 1 | 1231 | ルイズ | louise | 10 | choice | 1229 | よく分からない | 3973 | 3841 | ветка перемещения «ルイズの部屋» (корень сцены 1229, меню — сцена 24) |
| chapter_02_ゼロのルイズ | 1 | 1232 | ルイズ | louise | -10 | choice | 1229 | 元の世界なんて忘れたよ | 3986 | 3856 | ветка перемещения «ルイズの部屋» (корень сцены 1229, меню — сцена 24) |
| chapter_02_ゼロのルイズ | 1 | 1240 | タバサ | tabitha | 30 | move | 49 | 図書館 | 4174 | 4036 | корень ветки перемещения |
| chapter_02_ゼロのルイズ | 1 | 1242 | タバサ | tabitha | -15 | choice | 1240 | 本を取り上げる | 4229 | 4095 | ветка перемещения «図書館» (корень сцены 1240, меню — сцена 49) |
| chapter_02_ゼロのルイズ | 1 | 1243 | タバサ | tabitha | 15 | choice | 1240 | 本の内容を訊ねる | 4263 | 4125 | ветка перемещения «図書館» (корень сцены 1240, меню — сцена 49) |
| chapter_02_ゼロのルイズ | 1 | 1245 | キュルケ | kirche | 20 | move | 49 | キュルケの部屋 | 4327 | 4191 | корень ветки перемещения |
| chapter_02_ゼロのルイズ | 1 | 1247 | キュルケ | kirche | 10 | choice | 1245 | この際じっくりと観察する | 4401 | 4257 | ветка перемещения «キュルケの部屋» (корень сцены 1245, меню — сцена 49) |
| chapter_02_ゼロのルイズ | 1 | 1248 | キュルケ | kirche | -10 | choice | 1245 | お説教する | 4436 | 4290 | ветка перемещения «キュルケの部屋» (корень сцены 1245, меню — сцена 49) |
| chapter_02_ゼロのルイズ | 1 | 1250 | ハルナ | haruna | 20 | move | 49 | ルイズの部屋 | 4482 | 4346 | корень ветки перемещения |
| chapter_02_ゼロのルイズ | 1 | 1252 | ハルナ | haruna | 10 | choice | 1250 | 春奈に一刻も早く聞きたいことが | 4594 | 4443 | ветка перемещения «ルイズの部屋» (корень сцены 1250, меню — сцена 49) |
| chapter_02_ゼロのルイズ | 1 | 1253 | ハルナ | haruna | -10 | choice | 1250 | なんとなく | 4648 | 4501 | ветка перемещения «ルイズの部屋» (корень сцены 1250, меню — сцена 49) |

### 4.1 Сводка канона по персонажам

| персонаж | всего | распределение значений | сцены |
|---|---|---|---|
| Луиза (ルイズ) | 16 | -10×6, +10×8, +20×2 | 7, 8, 12, 13, 17, 18, 21, 38, 55, 56, 1009, 1010, 1012, 1229, 1231, 1232 |
| Сиеста (シエスタ) | 14 | -10×5, +10×7, +20×2 | 22, 31, 32, 37, 41, 42, 45, 46, 1014, 1015, 1016, 1224, 1225, 1226 |
| Кирче (キュルケ) | 9 | -10×3, +10×4, +20×2 | 35, 41, 42, 1024, 1026, 1027, 1245, 1247, 1248 |
| Табита (タバサ) | 7 | -15×2, +15×3, +30×2 | 36, 1019, 1021, 1022, 1240, 1242, 1243 |
| Харуна (ハルナ) | 8 | -10×3, +10×3, +20×2 | 41, 42, 1029, 1031, 1032, 1250, 1252, 1253 |

Ни одно канон-событие не является «чисто линейным»: все 54 лежат в ветках
(`choice` — цель `【選択肢】`, `date` — вход в блок `【デート】`, `move` — цель `【移動】`).

### 4.2 Дата-блоки и 【デート進行】

Вход в даты — сцена **62** (меню `【デート】`): →1009 Луиза, →1014 Сиеста, →1019 Табита, →1024 Кирче, →1029 Харуна.
Блоки: Луиза 1009–1013, Сиеста 1014–1018, Табита 1019–1023, Кирче 1024–1028, Харуна 1029–1033.
Датовые переходные сцены 63–67 ведут `→ next` в блок соответствующей девушки.

**`【デート進行】` в chapter_02 — ровно ОДИН** (строка chapters 2849: `【デート進行】 → scene 68`; events_full 2679: `DATE date((0x01000000 +68),false,(0x03000000 +4))`, сцена-владелец — 62). Это генеральный переход «продолжить уже начатую дату»: сцена 68 вне диапазона главы (core 6..67), в неё входит тот дата-блок, что был начат ранее; **событий `【好感度】` ни на этом переходе, ни внутри него нет**. Расхождение с формулировкой задания («двух сцен с 【デート進行】») вынесено в §8/QUESTIONS — второго маркера в chapter_02 нет; в `chapter_06` их пять, в `chapter_03/04/05` — по одному (проверено grep'ом по `ps2_source/chapters/`).

## 5. Построчная сверка «порт ↔ канон» (73 вызова)

`matched_scene` — сцена канона или `EMPTY`; ratio: SAME / X2 / DIFF / EXTRA.

> **О колонке `opt` (эвристика контекста, не якорь):** это ближайшая строка-опция `menu:` выше вызова.
> В `script-ch1_1.rpy` ветки реализованы через `menu → $ choise_result → if/elif`, поэтому там `opt`
> показывает последнюю опцию меню, а не фактическую ветку ( строки `script-ch1_1.rpy:142/161/390/419/590/653` ).
> На сопоставление это не влияло — оно построено только на voice-id окнах; в остальных файлах вызовы
> стоят непосредственно внутри блока опции (проверено по отступу), `opt` там достоверен.

| file:line | char_key | value | matched_scene | value_canon | ratio | comment |
|---|---|---|---|---|---|---|
| script-ch1_1.rpy:142 | louise | 20 | 7 | 10 | X2 | anchor=window; окно-сцены 7:3,9:2; label `ch1`; опция «It's terrible!» |
| script-ch1_1.rpy:161 | louise | -20 | 8 | -10 | X2 | anchor=window; окно-сцены 10:3,9:2; label `ch1`; опция «It's terrible!» |
| script-ch1_1.rpy:390 | louise | 20 | 12 | 10 | X2 | anchor=window; окно-сцены 11:2,12:2; label `ch1`; опция «Alright... I'll hand her over.» |
| script-ch1_1.rpy:419 | louise | -20 | 13 | -10 | X2 | anchor=window; окно-сцены 13:4,11:1; label `ch1`; опция «Alright... I'll hand her over.» |
| script-ch1_1.rpy:590 | louise | -20 | 18 | -10 | X2 | anchor=window; окно-сцены 18:5,16:1; label `ch1`; опция «I didn't do anything!» |
| script-ch1_1.rpy:653 | louise | 20 | 17 | 10 | X2 | anchor=window; окно-сцены 17:4; label `ch1`; опция «I didn't do anything!» |
| script-ch1_2.rpy:95 | louise | 20 | 21 | 10 | X2 | anchor=window; окно-сцены 21:4,20:1; label `ch1_2`; опция «Blame it on Louise» |
| script-ch1_2.rpy:112 | louise | -20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 23:4,21:2; label `ch1_2`; опция «Try to cover it up yourself» |
| script-ch1_2.rpy:136 | siesta | 20 | 22 | 10 | X2 | anchor=window; окно-сцены 22:4,23:1; label `ch1_2`; опция «Blame it on Siesta» |
| script-ch1_3.rpy:51 | siesta | 20 | 1224 | 20 | SAME | anchor=window; окно-сцены 1224:6; label `si_room_ch1_3` |
| script-ch1_3.rpy:98 | siesta | 20 | 1225 | 10 | X2 | anchor=window; окно-сцены 1225:5,1029:1; label `si_room_ch1_3`; опция «You might be right.» |
| script-ch1_3.rpy:99 | louise | -20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 1225:5,1029:1; label `si_room_ch1_3`; опция «You might be right.» |
| script-ch1_3.rpy:126 | siesta | -20 | 1226 | -10 | X2 | anchor=window; окно-сцены 1226:4,1225:1; label `si_room_ch1_3`; опция «I don't really know.{#var2}» |
| script-ch1_3.rpy:127 | louise | 20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 1226:4,1225:1; label `si_room_ch1_3`; опция «I don't really know.{#var2}» |
| script-ch1_3.rpy:185 | louise | 20 | 1229 | 20 | SAME | anchor=window; окно-сцены 1229:4,1228:2; label `l_room_ch1_3` |
| script-ch1_3.rpy:264 | louise | -20 | 1232 | -10 | X2 | anchor=window; окно-сцены 1232:5,1230:1; label `l_room_ch1_3`; опция «I've already forgotten about my world.» |
| script-ch1_3.rpy:305 | louise | 20 | 1231 | 10 | X2 | anchor=window; окно-сцены 1233:3,1231:2; label `l_room_ch1_3`; опция «I don't really know.» |
| script-ch1_3.rpy:385 | louise | -20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 1237:5; label `hallway_ch1_3`; опция «How did you know!?{#var1}» |
| script-ch1_3.rpy:427 | louise | 20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 1235:5,1236:1; label `hallway_ch1_3`; опция «Th-there's no way that's true, right?» |
| script-ch1_5.rpy:136 | siesta | 20 | 32 | 10 | X2 | anchor=window; окно-сцены 32:6; label `ch1_5`; опция «We need a witness's testimony here!» |
| script-ch1_5.rpy:137 | louise | -20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 32:6; label `ch1_5`; опция «We need a witness's testimony here!» |
| script-ch1_5.rpy:211 | siesta | -20 | 31 | -10 | X2 | anchor=window; окно-сцены 31:4,30:1; label `ch1_5`; опция «I'll wake up Louise and let her explain it herself.» |
| script-ch1_5.rpy:212 | louise | 20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 31:4,30:1; label `ch1_5`; опция «I'll wake up Louise and let her explain it herself.» |
| script-ch1_6.rpy:76 | louise | -20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 36:5,34:1; label `ch1_6`; опция «Ask Tabitha» |
| script-ch1_6.rpy:77 | tabitha | 20 | 36 | 15 | DIFF | anchor=window; окно-сцены 36:5,34:1; label `ch1_6`; опция «Ask Tabitha» |
| script-ch1_6.rpy:96 | louise | -20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 37:5,36:1; label `ch1_6`; опция «Ask Siesta» |
| script-ch1_6.rpy:97 | siesta | 20 | 37 | 10 | X2 | anchor=window; окно-сцены 37:5,36:1; label `ch1_6`; опция «Ask Siesta» |
| script-ch1_6.rpy:142 | louise | 20 | 38 | 10 | X2 | anchor=window; окно-сцены 38:4,37:1; label `ch1_6`; опция «Ask Louise» |
| script-ch1_6.rpy:178 | louise | -20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 35:5,38:1; label `ch1_6`; опция «Ask Kirche» |
| script-ch1_6.rpy:179 | kirche | 20 | 35 | 10 | X2 | anchor=window; окно-сцены 35:5,38:1; label `ch1_6`; опция «Ask Kirche» |
| script-ch1_6.rpy:437 | louise | 20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 41:4,40:2; label `ch1_6`; опция «Yeah.{#v2}» |
| script-ch1_6.rpy:443 | haruna | -20 | 41 | -10 | X2 | anchor=window; окно-сцены 41:5,40:1; label `ch1_6`; опция «Yeah.{#v2}» |
| script-ch1_6.rpy:449 | siesta | -20 | 41 | -10 | X2 | anchor=window; окно-сцены 41:6; label `ch1_6`; опция «Yeah.{#v2}» |
| script-ch1_6.rpy:455 | kirche | -20 | 41 | -10 | X2 | anchor=window; окно-сцены 41:5,42:1; label `ch1_6`; опция «Yeah.{#v2}» |
| script-ch1_6.rpy:470 | louise | -20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 42:4,41:1; label `ch1_6`; опция «Nope.» |
| script-ch1_6.rpy:477 | haruna | 20 | 42 | 10 | X2 | anchor=window; окно-сцены 42:5,40:1; label `ch1_6`; опция «Nope.» |
| script-ch1_6.rpy:481 | siesta | 20 | 42 | 10 | X2 | anchor=window; окно-сцены 42:6; label `ch1_6`; опция «Nope.» |
| script-ch1_6.rpy:485 | kirche | 20 | 42 | 10 | X2 | anchor=window; окно-сцены 42:5,43:1; label `ch1_6`; опция «Nope.» |
| script-ch1_7.rpy:169 | siesta | -20 | 46 | -10 | X2 | anchor=window; окно-сцены 46:4,45:2; label `ch1_7`; опция «What about Kirche's room?» |
| script-ch1_7.rpy:270 | siesta | 20 | 45 | 10 | X2 | anchor=window; окно-сцены 45:5,46:1; label `ch1_7`; опция «You can come to my room.» |
| script-ch1_7.rpy:271 | louise | -20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 45:5,46:1; label `ch1_7`; опция «You can come to my room.» |
| script-ch1_8.rpy:139 | tabitha | 20 | 1240 | 30 | DIFF | anchor=window; окно-сцены 1240:5,1019:1; label `library_ch1_8` |
| script-ch1_8.rpy:211 | tabitha | -20 | 1242 | -15 | DIFF | anchor=window; окно-сцены 1241:4,1242:1; label `library_ch1_8`; опция «Snatch the book» |
| script-ch1_8.rpy:212 | louise | 20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 1241:4,1242:1; label `library_ch1_8`; опция «Snatch the book» |
| script-ch1_8.rpy:253 | tabitha | 20 | 1243 | 15 | DIFF | anchor=window; окно-сцены 1243:5,1242:1; label `library_ch1_8`; опция «Inquire about the book» |
| script-ch1_8.rpy:254 | louise | -20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 1243:5,1242:1; label `library_ch1_8`; опция «Inquire about the book» |
| script-ch1_8.rpy:324 | kirche | 20 | 1245 | 20 | SAME | anchor=window; окно-сцены 1245:6; label `k_room_ch1_8` |
| script-ch1_8.rpy:406 | louise | -20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 1247:4,1246:2; label `k_room_ch1_8`; опция «Take this opportunity to get a good look.» |
| script-ch1_8.rpy:407 | kirche | 20 | 1247 | 10 | X2 | anchor=window; окно-сцены 1247:4,1246:2; label `k_room_ch1_8`; опция «Take this opportunity to get a good look.» |
| script-ch1_8.rpy:453 | louise | 20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 1248:5,1024:1; label `k_room_ch1_8`; опция «Scold her.» |
| script-ch1_8.rpy:454 | kirche | -20 | 1248 | -10 | X2 | anchor=window; окно-сцены 1248:5,1024:1; label `k_room_ch1_8`; опция «Scold her.» |
| script-ch1_8.rpy:500 | haruna | 20 | 1250 | 20 | SAME | anchor=window; окно-сцены 1250:3,1249:2; label `l_room_ch1_8` |
| script-ch1_8.rpy:611 | louise | 20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 1251:5,10:1; label `l_room_ch1_8`; опция «I thought I might clean the room a bit...» |
| script-ch1_8.rpy:659 | haruna | -20 | 1253 | -10 | X2 | anchor=window; окно-сцены 1253:4,1252:1; label `l_room_ch1_8`; опция «Nothing special.» |
| script-ch1_8.rpy:695 | haruna | 20 | 1252 | 10 | X2 | anchor=window; окно-сцены 1252:5,29:1; label `l_room_ch1_8`; опция «There's something I want to ask Haruna right away...» |
| script-ch1_8.rpy:696 | louise | -20 | EMPTY | — | EXTRA | EXTRA: нет события в каноне chapter_02; окно-сцены 1252:5,29:1; label `l_room_ch1_8`; опция «There's something I want to ask Haruna right away...» |
| script-ch1_9.rpy:98 | louise | 20 | 56 | 10 | X2 | AMBIGUOUS: tie scene55(score2),scene56(score2); AMBIGUOUS по окну voice-id (tie scene55=2/scene56=2) -> RESOLVED по тексту опции меню: "Come on, can't something be done about that?" = 【選択肢】そこをなんとかならないか？ -> сцена 56; anchor=window+text; окно-сцены 56:2,55:2; label `ch1_9`; опция «Come on, can't something be done about that?» |
| script-ch1_9.rpy:108 | louise | -20 | 55 | -10 | X2 | AMBIGUOUS по окну voice-id -> RESOLVED по тексту опции меню: "Don't say such awful things!" = 【選択肢】そんなひどいこと言うなよ！ -> сцена 55; anchor=window+text; окно-сцены 55:2,57:2; label `ch1_9`; опция «Don't say such awful things!» |
| script-ch1_10.rpy:37 | louise | 20 | 1009 | 20 | SAME | anchor=window; окно-сцены 1009:5; label `date_louise_1` |
| script-ch1_10.rpy:87 | louise | 20 | 1010 | 10 | X2 | anchor=window; окно-сцены 1010:5,1009:1; label `date_louise_1`; опция «You look really beautiful.» |
| script-ch1_10.rpy:111 | louise | -20 | 1012 | -10 | X2 | anchor=window; окно-сцены 1012:3,1010:1; label `date_louise_1`; опция «I don't really get it.» |
| script-ch1_10.rpy:181 | siesta | 20 | 1014 | 20 | SAME | anchor=window; окно-сцены 1014:3,1013:2; label `date_siesta_1` |
| script-ch1_10.rpy:236 | siesta | 20 | 1015 | 10 | X2 | anchor=window; окно-сцены 1015:4,29:1; label `date_siesta_1`; опция «You'll make an excellent wife.» |
| script-ch1_10.rpy:297 | siesta | -20 | 1016 | -10 | X2 | anchor=window; окно-сцены 1016:5,1017:1; label `date_siesta_1`; опция «So you're a thrifty person.» |
| script-ch1_10.rpy:341 | tabitha | 20 | 1019 | 30 | DIFF | anchor=window; окно-сцены 1019:5,1018:1; label `date_tabitha_1` |
| script-ch1_10.rpy:483 | tabitha | 20 | 1022 | 15 | DIFF | anchor=window; окно-сцены 1022:5; label `date_tabitha_1`; опция «Let me massage your shoulders.» |
| script-ch1_10.rpy:512 | tabitha | -20 | 1021 | -15 | DIFF | anchor=window; окно-сцены 1021:3,1020:2; label `date_tabitha_1`; опция «Let me hold you.» |
| script-ch1_10.rpy:578 | kirche | 20 | 1024 | 20 | SAME | anchor=window; окно-сцены 1024:5,29:1; label `date_kirche_1` |
| script-ch1_10.rpy:730 | kirche | 20 | 1027 | 10 | X2 | anchor=window; окно-сцены 1027:5,60:1; label `date_kirche_1`; опция «What do you think of me?» |
| script-ch1_10.rpy:757 | kirche | -20 | 1026 | -10 | X2 | anchor=window; окно-сцены 1026:5,1027:1; label `date_kirche_1`; опция «Have you ever truly fallen in love with someone?» |
| script-ch1_10.rpy:841 | haruna | 20 | 1029 | 20 | SAME | anchor=window; окно-сцены 1029:6; label `date_haruna_1` |
| script-ch1_10.rpy:888 | haruna | -20 | 1032 | -10 | X2 | anchor=window; окно-сцены 1032:3,1030:1; label `date_haruna_1`; опция «I don't know.» |
| script-ch1_10.rpy:909 | haruna | 20 | 1031 | 10 | X2 | anchor=window; окно-сцены 1031:4,1032:1; label `date_haruna_1`; опция «You were looking at the night sky.» |

## 6. Обратная сторона: каждое канон-событие → строка порта

| scene | char_ja | value_canon | порт (file:line = value) | ratio |
|---|---|---|---|---|
| 7 | ルイズ | 10 | script-ch1_1.rpy:142 = 20 | X2 |
| 8 | ルイズ | -10 | script-ch1_1.rpy:161 = -20 | X2 |
| 12 | ルイズ | 10 | script-ch1_1.rpy:390 = 20 | X2 |
| 13 | ルイズ | -10 | script-ch1_1.rpy:419 = -20 | X2 |
| 17 | ルイズ | 10 | script-ch1_1.rpy:653 = 20 | X2 |
| 18 | ルイズ | -10 | script-ch1_1.rpy:590 = -20 | X2 |
| 21 | ルイズ | 10 | script-ch1_2.rpy:95 = 20 | X2 |
| 22 | シエスタ | 10 | script-ch1_2.rpy:136 = 20 | X2 |
| 31 | シエスタ | -10 | script-ch1_5.rpy:211 = -20 | X2 |
| 32 | シエスタ | 10 | script-ch1_5.rpy:136 = 20 | X2 |
| 35 | キュルケ | 10 | script-ch1_6.rpy:179 = 20 | X2 |
| 36 | タバサ | 15 | script-ch1_6.rpy:77 = 20 | DIFF |
| 37 | シエスタ | 10 | script-ch1_6.rpy:97 = 20 | X2 |
| 38 | ルイズ | 10 | script-ch1_6.rpy:142 = 20 | X2 |
| 41 | ハルナ | -10 | script-ch1_6.rpy:443 = -20 | X2 |
| 41 | シエスタ | -10 | script-ch1_6.rpy:449 = -20 | X2 |
| 41 | キュルケ | -10 | script-ch1_6.rpy:455 = -20 | X2 |
| 42 | ハルナ | 10 | script-ch1_6.rpy:477 = 20 | X2 |
| 42 | シエスタ | 10 | script-ch1_6.rpy:481 = 20 | X2 |
| 42 | キュルケ | 10 | script-ch1_6.rpy:485 = 20 | X2 |
| 45 | シエスタ | 10 | script-ch1_7.rpy:270 = 20 | X2 |
| 46 | シエスタ | -10 | script-ch1_7.rpy:169 = -20 | X2 |
| 55 | ルイズ | -10 | script-ch1_9.rpy:108 = -20 | X2 |
| 56 | ルイズ | 10 | script-ch1_9.rpy:98 = 20 | X2 |
| 1009 | ルイズ | 20 | script-ch1_10.rpy:37 = 20 | SAME |
| 1010 | ルイズ | 10 | script-ch1_10.rpy:87 = 20 | X2 |
| 1012 | ルイズ | -10 | script-ch1_10.rpy:111 = -20 | X2 |
| 1014 | シエスタ | 20 | script-ch1_10.rpy:181 = 20 | SAME |
| 1015 | シエスタ | 10 | script-ch1_10.rpy:236 = 20 | X2 |
| 1016 | シエスタ | -10 | script-ch1_10.rpy:297 = -20 | X2 |
| 1019 | タバサ | 30 | script-ch1_10.rpy:341 = 20 | DIFF |
| 1021 | タバサ | -15 | script-ch1_10.rpy:512 = -20 | DIFF |
| 1022 | タバサ | 15 | script-ch1_10.rpy:483 = 20 | DIFF |
| 1024 | キュルケ | 20 | script-ch1_10.rpy:578 = 20 | SAME |
| 1026 | キュルケ | -10 | script-ch1_10.rpy:757 = -20 | X2 |
| 1027 | キュルケ | 10 | script-ch1_10.rpy:730 = 20 | X2 |
| 1029 | ハルナ | 20 | script-ch1_10.rpy:841 = 20 | SAME |
| 1031 | ハルナ | 10 | script-ch1_10.rpy:909 = 20 | X2 |
| 1032 | ハルナ | -10 | script-ch1_10.rpy:888 = -20 | X2 |
| 1224 | シエスタ | 20 | script-ch1_3.rpy:51 = 20 | SAME |
| 1225 | シエスタ | 10 | script-ch1_3.rpy:98 = 20 | X2 |
| 1226 | シエスタ | -10 | script-ch1_3.rpy:126 = -20 | X2 |
| 1229 | ルイズ | 20 | script-ch1_3.rpy:185 = 20 | SAME |
| 1231 | ルイズ | 10 | script-ch1_3.rpy:305 = 20 | X2 |
| 1232 | ルイズ | -10 | script-ch1_3.rpy:264 = -20 | X2 |
| 1240 | タバサ | 30 | script-ch1_8.rpy:139 = 20 | DIFF |
| 1242 | タバサ | -15 | script-ch1_8.rpy:211 = -20 | DIFF |
| 1243 | タバサ | 15 | script-ch1_8.rpy:253 = 20 | DIFF |
| 1245 | キュルケ | 20 | script-ch1_8.rpy:324 = 20 | SAME |
| 1247 | キュルケ | 10 | script-ch1_8.rpy:407 = 20 | X2 |
| 1248 | キュルケ | -10 | script-ch1_8.rpy:454 = -20 | X2 |
| 1250 | ハルナ | 20 | script-ch1_8.rpy:500 = 20 | SAME |
| 1252 | ハルナ | 10 | script-ch1_8.rpy:695 = 20 | X2 |
| 1253 | ハルナ | -10 | script-ch1_8.rpy:659 = -20 | X2 |

**MISSING: 0** — все 54 события канона отражены в порте ровно одним вызовом (bijection 54↔54).

## 7. Ответы на вопросы пользователя

### 7.1 Есть ли в chapter_02 логика «Луиза теряет при выборе другой героини»?

**В КАНОНЕ chapter_02 — НЕТ. 0 сцен.** Доказательство (полный перечень многоперсонажных сцен канона — других нет):
* сцена **41**: Харуна −10, Сиеста −10, Кирче −10 (одновременно, без Луизы);
* сцена **42**: Харуна +10, Сиеста +10, Кирче +10 (одновременно, без Луизы).
Все остальные 48 событий — по одному персонажу на сцену. Сцена, где Луиза меняется вместе с кем-то ещё, в chapter_02 отсутствует (проверено программно: `mixed louise+other scenes: []`).

**Контрпример из chapter_03, сцена 109 — ПОДТВЕРЖДЁН** (такая логика в главе 3 есть):

| строка chapters | содержимое |
|---|---|
| 1897 | サイト：春奈、具合はどう？  [voice 11136] |
| 1904 | 朝に比べたら、だいぶ良くなったと思う。  [voice 2110] |
| 1905 | 【好感度】ハルナ  10 |
| 1906 | サイト：そりゃ一安心だな。  [voice 11137] |
| 1907 | ルイズ：……ふん。  [voice 5829] |
| 1908 | 【好感度】ルイズ  -10 |
| 1910 | でも、もう大丈夫、かな。  [voice 2111] |
| 1912 | 体調が完全に戻るまでは、ちゃんと休んでろよ。  [voice 11138] |
| 1914 | ハルナ：ありがとう、平賀くん。  [voice 2112] |

То есть в сцене 109 chapter_03: `【好感度】ハルナ +10` (стр. 1905) и `【好感度】ルイズ -10` (стр. 1908) — Харуна получает при выборе, обращённом к ней, а Луиза теряет **в той же сцене**. Это штатная механика канона начиная с главы 3, но в главе 1 (chapter_02) её нет.

**Для главы 1 (проект, порт): логика «Луиза теряет» в ПОРТЕ ЕСТЬ — и это ровно те 19 EXTRA-вызовов, которых нет в каноне.** Из 19 — **13 стоят смежно (через 1 строку) с вызовом другого персонажа**, то есть образуют «парные» блоки «другая героиня ±20 / Луиза ∓20», внесённые в порт «на глаз»:

| файл | строка | первый вызов | второй файл:строка | второй вызов |
|---|---|---|---|---|
| script-ch1_3.rpy | 98 | siesta 20 | script-ch1_3.rpy:99 | louise -20 |
| script-ch1_3.rpy | 126 | siesta -20 | script-ch1_3.rpy:127 | louise 20 |
| script-ch1_5.rpy | 136 | siesta 20 | script-ch1_5.rpy:137 | louise -20 |
| script-ch1_5.rpy | 211 | siesta -20 | script-ch1_5.rpy:212 | louise 20 |
| script-ch1_6.rpy | 76 | louise -20 | script-ch1_6.rpy:77 | tabitha 20 |
| script-ch1_6.rpy | 96 | louise -20 | script-ch1_6.rpy:97 | siesta 20 |
| script-ch1_6.rpy | 178 | louise -20 | script-ch1_6.rpy:179 | kirche 20 |
| script-ch1_7.rpy | 270 | siesta 20 | script-ch1_7.rpy:271 | louise -20 |
| script-ch1_8.rpy | 211 | tabitha -20 | script-ch1_8.rpy:212 | louise 20 |
| script-ch1_8.rpy | 253 | tabitha 20 | script-ch1_8.rpy:254 | louise -20 |
| script-ch1_8.rpy | 406 | louise -20 | script-ch1_8.rpy:407 | kirche 20 |
| script-ch1_8.rpy | 453 | louise 20 | script-ch1_8.rpy:454 | kirche -20 |
| script-ch1_8.rpy | 695 | haruna 20 | script-ch1_8.rpy:696 | louise -20 |

Оставшиеся 6 EXTRA-вызовов Луизы (`:112` в ch1_2, `:385`/`:427` в ch1_3, `:437`/`:470` в ch1_6, `:611` в ch1_8) стоят вне смежных пар — не вплотную к вызову другого персонажа, — но тоже в ветках, где канон Луизу не двигает (сцены 23, 1235/1237, 41/42, 1251 — без события Луизы). Итого: **канон chapter_02 не содержит потерь Луизы за другой персонаж; потери Луизы в главе 1 существуют только как дополнения порта.**

### 7.2 Какие именно вызовы порта не имеют пары в каноне (19 EXTRA, все Луиза)

`окно-сцены` — сцена по большинству голосовых id в окне вызова (само по себе не доказательство, приведено для навигации; канон-события этих сцен либо отсутствуют, либо принадлежат только другому персонажу). Колонки `label`/`опция` — реальная ветка меню (все 19 EXTRA находятся вне `script-ch1_1.rpy`, то есть вне if/elif-паттерна, см. примечание в §5):

| file:line | char | value | окно-сцены | label | опция меню / ветка | флаги |
|---|---|---|---|---|---|---|
| script-ch1_2.rpy:112 | louise | -20 | 23 | `ch1_2` | «Try to cover it up yourself» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_3.rpy:99 | louise | -20 | 1225 | `si_room_ch1_3` | «You might be right.» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_3.rpy:127 | louise | 20 | 1226 | `si_room_ch1_3` | «I don't really know.{#var2}» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_3.rpy:385 | louise | -20 | 1237 | `hallway_ch1_3` | «How did you know!?{#var1}» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_3.rpy:427 | louise | 20 | 1235 | `hallway_ch1_3` | «Th-there's no way that's true, right?» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_5.rpy:137 | louise | -20 | 32 | `ch1_5` | «We need a witness's testimony here!» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_5.rpy:212 | louise | 20 | 31 | `ch1_5` | «I'll wake up Louise and let her explain it herself.» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_6.rpy:76 | louise | -20 | 36 | `ch1_6` | «Ask Tabitha» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_6.rpy:96 | louise | -20 | 37 | `ch1_6` | «Ask Siesta» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_6.rpy:178 | louise | -20 | 35 | `ch1_6` | «Ask Kirche» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_6.rpy:437 | louise | 20 | 41 | `ch1_6` | «Yeah.{#v2}» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_6.rpy:470 | louise | -20 | 42 | `ch1_6` | «Nope.» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_7.rpy:271 | louise | -20 | 45 | `ch1_7` | «You can come to my room.» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_8.rpy:212 | louise | 20 | 1241 | `library_ch1_8` | «Snatch the book» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_8.rpy:254 | louise | -20 | 1243 | `library_ch1_8` | «Inquire about the book» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_8.rpy:406 | louise | -20 | 1247 | `k_room_ch1_8` | «Take this opportunity to get a good look.» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_8.rpy:453 | louise | 20 | 1248 | `k_room_ch1_8` | «Scold her.» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_8.rpy:611 | louise | 20 | 1251 | `l_room_ch1_8` | «I thought I might clean the room a bit...» | EXTRA: нет события в каноне chapter_02 |
| script-ch1_8.rpy:696 | louise | -20 | 1252 | `l_room_ch1_8` | «There's something I want to ask Haruna right away...» | EXTRA: нет события в каноне chapter_02 |

Пояснения по веткам: `si_room_ch1_3` — ночная визитная ветка «Сиеста» (сцены 1224–1226); `hallway_ch1_3` — ветка «Коридор» (1235–1237); `ch1_5` — выбор «кто объяснит» (31/32); `ch1_6` — выбор «кому задать вопрос» (35–38) и «はい/いいえ» (41/42); `ch1_7` — ветка «моя комната» (45/46); `library_ch1_8` — «Библиотека» (1240–1243); `k_room_ch1_8` — «Комната Кирче» (1245–1248); `l_room_ch1_8` — «Комната Луизы» (1250–1253); `ch1_2` — сцена 23 («сам отшутился», в каноне без события).

## 8. PROVISIONAL / ??? / методические пометки

1. **`voice_id_map.csv` не покрывает главу 1** (0 строк `ch1`), якорь построен через `ps2_source/_diagnostics/voice_scene_map.json` — PROVISIONAL-решение методики; при правке кода (следующая подзадача) мост нужен будет снова. Кандидат: после приёмки таблицы завести строки `ch1*` в `voice_id_map.csv` (не делал — вне объёма S1 и это запись в `references/`).
2. JSON устарел для 5 голосовых имён (§2) и содержит 80 неверифицируемых/null-записей и 176 дубликатов имён — на результат не повлияло (fallback 0).
3. «Две сцены с 【デート進行】» из задания: в chapter_02 найдена **одна** — см. §4.2. Возможная причина расхождения: второй маркер посчитан в events_full (это тот же переход) либо имелась в виду сцена-житель `chapter_00` (`【デート進行】 → scene 1865`). Требуется уточнение ведущего → **???/QUESTION**.
4. 7 DIFF — не ошибка метода, а расхождение величин Табиты (канон ±15/±30 vs порт ±20): это уже содержательная находка для правки кода, не для S1.
5. Итоговый биекшен 54↔54 означает, что человек при порте **не потерял ни одного** канон-события — добавил только 19.

## 9. Проверки

* CSV: UTF-8 без BOM (первые байты `63 68 61` / `66 69 6c` — заголовки, не `EF BB BF`), заголовок, разделитель `,`, кавычки `"`, перевод строки LF; строк данных 54 и 73 (+заголовок).
* Чтение доски `reports/task_board.json` не выполнялось (protocol S1).
* `ps2_source/` — без единой правки; `game/` — S1 только читал. В `git status` есть незакоммиченные правки `game/chapters/6/script-ch6_1.rpy`, `game/chapters/6/script-ch6_2.rpy`, `game/tl/russian/thoughs.rpy` — они из других сессий, не от этой подзадачи (S1 их не создавал и не трогал); выход S1 — только новые файлы в `reports/tasks/T20261031-054249-c81b/`. Git-коммит не выполнялся.
* Ожидания задания выполнены: EXTRA = 19, все `louise`; MISSING = 0; контрпример chapter_03 с.109 приведён.
