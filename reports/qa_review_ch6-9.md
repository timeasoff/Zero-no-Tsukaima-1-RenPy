# QA-проверка глав 6–9 (ветка `qa/review-ch2-5`)

> Продолжение аудита глав 2–5 (отчёт `reports/qa_review_ch2-5.md`).
> ВЕТКА ИЗОЛИРОВАНА: `qa/review-ch2-5`, база `f769e79`; в `master` ничего не сливается.
> Другой агент работает в `D:/gameMake/ZnT-1/ZnT1` (master) — его WIP здесь не учитывается.

## Метаданные

| Поле | Значение |
|---|---|
| Дата старта | 2026-11-17 |
| Ветка | `qa/review-ch2-5` |
| Статус | 🔄 В РАБОТЕ |

## Прогресс

| Глава | Механика | Покрытие JA | EN/RU | Порт | Коммит | Статус |
|---|---|---|---|---|---|---|
| 6 | ✅ | ✅ 3/3 части | ✅ 2 ERROR исправлено | ✅ critical `$ jump` исправлен | (этот коммит) | ✅ |
| 7 | ✅ | ✅ 3/3 | ✅ RU: 2 ERROR | ✅ | (этот коммит) | ✅ |
| 8 | ✅ | ⚠️ 2 FULL (no media) | ✅ EN ~12, RU ~12 | ✅ 6 ERROR | (этот коммит) | ✅ |
| 9 | ✅ | ⚠️ 2 FULL (no media) | ✅ EN/RU | ✅ | (этот коммит) | ✅ |

## Находки

| ID | Глава | Место | Описание | Classification | Disposition |
|---|---|---|---|---|---|
| — | — | — | пока нет | — | — |

## Глава 6

**Механика:** `check_project` errors=0; `check_renpy_syntax` OK; `check_typography ru` OK; `omission_precheck 6_1/6_2/6_3` → 0; сканеры отступов → 0. `check_assets` OK, но 417 голосов ещё в очереди транскрипций (WIP окружения/другого агента, не потеря). W6-заглушки: `id(38/40/44/58/60)` в `ch6_2/ch6_3` — ожидаемые до заполнения имён.

**Находки (все исправлены):**

| ID | Место | Доказательство | Classification / Disposition |
|---|---|---|---|
| P3 | `script-ch6_3.rpy:32` | `$ jump ch6_3_s1164` — невалидный Python; это единственный `$ jump` в проекте, ломал компиляцию всей игры | ERROR → **FIXED**: `jump ch6_3_s1164` |
| R1 | `script-ch6_1.rpy:221` + TL | JA «トリスタニアの地図» = Tristania (`dictionary.md:201` → Тристания), а не Tristain/Тристейн | ERROR → **FIXED** EN + `old` + RU: «This is a map of Tristania…» / «карта Тристании» |
| R2 | `dialogs.rpy:16107` | JA «サイトさん» у Сиесты; `addresses.md` требует «Сайто-сан» | ERROR → **FIXED**: «мадемуазель Вальер, Сайто-сан» |
| R3 | `dialogs.rpy:16107/16554/16557` | канон «Вальер», «герцог де Ла Вальер» | CANDIDATE → **FIXED** как безопасная каноническая замена |
| P1 | `script-ch6_1.rpy:6` | нет `call overlay_screen("Chapter Six…")`, хотя карточка есть в `overlays.rpy` и у всех др. глав есть | CANDIDATE → REMAINING (нужен уникальный K=15, решение по структуре) |
| P3b | `script-ch6_3.rpy:181–183` | source `play=+16` → t15, но music остановлен и не возобновлён | CANDIDATE → REMAINING |
| P1b | `script-ch6_1.rpy` (целиком) | 4 BGM-сигнала источника не портированы | CANDIDATE → REMAINING |
| R4/R5 | `dialogs.rpy:16494`, `thoughs.rpy:1343` | инверсия субъекта 俺が; сломанный порядок слов «благодаря ли этому еда» | CANDIDATE → REMAINING |

EN-ревью:~1500 строк / ~490 реплик — замечаний нет. Структура: 53 лейбла без дублей, 11 меню ↔ source, 13 tndl-вызовов точны, 418 voices на месте, гейт `sp_l1` корректен.

## Главы 7–9 — результат

**Механика:** `check_project` errors=0/warnings=318; `check_renpy_syntax` OK; RU-типографика OK; валидатор отступов 0; omission precheck 7_1…7_3 → 0, 8_1/8_2 → 0, 8_3/9_1 → по 2 FULL-пропуска (голоса без манифеста/ogg в этой среде — зафиксированы как ???).

**Исправлено:**

| Категория | Примеры |
|---|---|
| Синтаксис | `ch8_2:39/520` — unquoted `s (...)` → `th "(...)"`; `ch8_3:310` — тег вне строки → внутрь; теги `{#ch8_l_60}`/`{#ch8_s_94}` → 3-значные; `ch8_2:116` — `id(213)` → `ready_to_blow` |
| EN-смысл | «good news»→«bad news» (良くない); «tell Princess about Siesta»→«have Siesta stay with the Princess»; «give me your support»→«Good luck out there» (ご武運を); «split up / Site»→«split into two / Saito»; инверсия проигрыша королеве; «finish me» вместо «This is the finishing blow»; заклинание Пустоты «you who are not here… as though you were here»; tangible→incorporeal; Weatherly→Weatherby (3) |
| RU-смысл | «своюBomb»→«свою бомбу»; «применить»→«применю»; «осязаемые»→«бесплотные»; «Гав»→«Так точно!»; «Тристейнии»→«Тристании»; «Сайт»→«Сайто»; «Хэруна»→«Харуна»; «……っ！»→«…!»; «Кюрке/Табаса/Гюш/Сьеста»→канон; инверсия проигрыша; «у Харуну»→«у Харуны»; «доверия нет»→«мне нельзя доверять»; Везерли→Уэзерби |
| Мусор в коде | удалены рассуждения агента и дубль `voice "ch8_h_075"` в `ch8_3.rpy:518–525`; скобки мыслей заменены на курсив в RU `ch9_1_thoughs` и `ch8_2_thoughs` |

Осталось как ??? (нет медиа в среде): 4 выпавших реплики с голосами 4601/4602 (ch9), 13655/930 (ch8) — нет записей в манифесте и `.ogg`, восстановить невозможно без исходного STV-архива.

## where I stopped

- Текущая фаза: **глава 6 завершена**; висячие вопросы глав 2–5 закрыты по указанию пользователя. Далее — **глава 7**.
- Инструменты: `check_renpy_syntax`, `check_project`, `check_typography`, `check_placeholders`, `check_assets`, `check_voice_transcriptions`, `omission_precheck`; сканер отступов `C:/Users/user/AppData/Local/Temp/opencode/qa_indent_all.py`; валидатор `qa_pyindent2.py`.
- Важно: `check_renpy_syntax.py` не ловит отступы внутри `menu:` — всегда запускать оба сканера.
