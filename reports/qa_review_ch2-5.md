# QA-проверка глав 2–5 (ветка `qa/review-ch2-5`)

> Живой журнал проверки. Дополняется по ходу работы, чтобы другой агент мог продолжить с того же места.
> **ВЕТКА ИЗОЛИРОВАНА**: работа ведётся в worktree `hidden-forest`, ветка `qa/review-ch2-5`,
> база — коммит `f769e79` (снапшот `master` на момент старта). В `master` НИЧЕГО не сливается.
> Другой агент продолжает портирование в `D:/gameMake/ZnT-1/ZnT1` (ветка `master`) — его WIP
> в этой проверке не учитывается, проверяется закоммиченное состояние снапшота.

## Метаданные

| Поле | Значение |
|---|---|
| Дата старта | 2026-11-17 |
| Ветка | `qa/review-ch2-5` |
| База | `f769e79` |
| worktree | `C:/Users/user/.local/share/opencode/worktree/44cc87/hidden-forest` |
| Статус | 🔄 В РАБОТЕ |

## Задача

Проверить качество перевода, качество порта и ошибки (включая ошибки синтаксиса Ren'Py).
Отдельно проверить, не пропущено ли что-то случайно (покрытие JA-источника).
Порядок: глава 2 → глава 3 → глава 4 → глава 5. Каждый крупный шаг — коммит.

## Прогресс по главам

| Глава | Механические проверки | Покрытие / пропуски | Качество перевода (EN/RU) | Коммит | Статус |
|---|---|---|---|---|---|
| 2 | ✅ после исправлений | ✅ 11/11 частей, 0 пропусков | ✅ 6 ERROR исправлено, 3 CANDIDATE задокументированы | (этот коммит) | ✅ |
| 3 | ⬜ не начато | ⬜ | ⬜ | — | ⬜ |
| 4 | ⬜ не начато | ⬜ | ⬜ | — | ⬜ |
| 5 | ⬜ не начато | ⬜ | ⬜ | — | ⬜ |

## Инструменты и оговорки окружения

* Механический слой: `check_renpy_syntax.py`, `check_project.py`, `check_typography.py` (ru/en/ja),
  `check_placeholders.py`, `check_assets.py`, `check_voice_transcriptions.py`, `omission_precheck.py`.
* Контентный слой: три независимых **read-only** ревьюера (EN↔JA, RU↔JA, структура порта) с
  обязательной ссылкой на реальную JA-строку. Все их находки перепроверены вручную по исходнику
  перед классификацией (сканнер/ревьюер = evidence, а не вердикт).
* **Окружение:** в worktree изначально отсутствовали junction'ы `game/{audio,gui,images,video}`
  (они не версионируются). Из-за этого `check_assets` сначала дал 1281 ложный `VOICE_MISSING`.
  Junction'ы восстановлены на `D:\gameMake\ZnT-1\ZnT1_MEDIA\{audio,gui,images,video}` —
  после этого `check_assets` → OK. Это **FALSE POSITIVE окружения**, не дефект контента.
* **Системное расхождение (не исправлялось):** `check_typography --lang en` стабильно даёт
  426 `ELLIPSIS` в гл. 2 (`...` вместо `…`), хотя `PROMTS.md` п.5 требует `…`. Та же картина
  в эталоне гл. 1 (например `script-ch1_8.rpy`: 97 × `...`, 0 × `…`) и во всех портированных
  главах. Классификация: WARNING, disposition: PRESERVED — FUNCTIONAL / USER DECISION.
  Массовая замена — решение уровня всего проекта, а не одной главы; в этой ветке не делалась.

---

## Глава 2 — результат

### Механические проверки (после исправлений)

| Проверка | Результат |
|---|---|
| `check_renpy_syntax.py --chapter 2` | OK |
| `check_project.py --chapter 2` | errors=0, RESULT: OK (warnings=327 — глобальные stale UI/чужие главы) |
| `check_typography.py --chapter 2 --lang ru` | OK (1367 строк) |
| `check_typography.py --chapter 2 --lang ja` | OK (8027 строк; 345 `......` — канон JA) |
| `check_typography.py --chapter 2 --lang en` | 426 ELLIPSIS — системное, см. оговорку выше |
| `check_placeholders.py --chapter 2` | OK (165 ID без filename — ожидаемые заглушки) |
| `check_assets.py --chapter 2` | OK (1 warning: 103 строки CSV в очереди — это будущие части, не потеря) |
| `check_voice_transcriptions.py --chapter 2` | OK: 1281 voice в скриптах, 0 в очереди |
| `omission_precheck.py` | 11/11 частей (2_1…2_8), FULL-пропусков 0 |

Структура (проверено вторым ревьюером): 58 уникальных лейблов, цепочка
`ch2 → ch2_2 → … → ch2_8 → ch3` без дыр; `from _call_*` уникальны; 24 `menu:` ↔ 24 `selectItem`;
5 `dateItem` ↔ 5 `portrait_choice`; 1281 voice = 1281 `[voice N]` по порядку; 62 sympathy-вызова
после исправления = 62 канонических; BGM, спрайты, ID-заглушки — без расхождений.

### Находки (DETECT → INVESTIGATE → COMPARE → CLASSIFY → DECIDE → RECHECK → RECORD)

| ID | Место | JA (доказательство) | Было | Classification | Investigation / Disposition |
|---|---|---|---|---|---|
| E1 | `script-ch2_4c.rpy:323` | `ここが異常なしってのはよく分かった。` (строка 4591 источника) = «выяснил, что **отклонений нет**» | EN «…this place is **abnormal**»; RU «…тут не всё в порядке» | ERROR | Инверсия смысла. **FIXED**: EN «…there's nothing wrong with this place», RU «…здесь всё в порядке»; `old` обновлён в обоих `tl/`, JA `new` не тронут. |
| E2 | `script-ch2_4c.rpy:90` | `あら、素直じゃない。` (строка 4408) = «Ой, ты **не** откровенен» | EN «My, how **honest** of you.»; RU «Ох, как откровенно.» | ERROR | Инверсия отрицания. **FIXED**: EN «My, you're not being honest, are you?», RU «Ах, какой же ты неоткровенный.»; `old` обновлён в обоих `tl/`. |
| E3 | `script-ch2_4b.rpy:156` | `なんだ、そりゃ。` (строка 4136) = «Что это значит?» | EN «What, that's a **bad thing**?» | CANDIDATE | Добавлена оценка «плохо», которой нет в JA. **PRESERVED** (Leave-Unchanged Accuracy); рекомендованный вариант: «What's that supposed to mean?». Решение — за владельцем канона. |
| R1 | `dialogs.rpy:5714` (script-ch2_5.rpy:320) | `ダーリン` | RU «…замешан **Дарлинг**…» | ERROR | `dictionary.md:247`: «Дарлинг» не использовать, канон «Дорогой». **FIXED** → «Дорогой». |
| R2 | `dialogs.rpy:5726` (script-ch2_5.rpy:334) | `ダーリンやハルナ` | RU «перед **Дарлингом** и Харуной» | ERROR | Та же запись словаря. **FIXED** → «перед Дорогим и Харуной». |
| R3 | `dialogs.rpy:6535` (script-ch2_7.rpy:21) | `それがヴァリエール家の**生き様**よ！` (строка 3200) | RU «Таков **обычай** дома Вальер!» | CANDIDATE | `生き様` = «образ жизни», а не «обычай». EN ближе («how the House of Vallière lives»). **PRESERVED**, рекомендуется «Таков образ жизни дома Вальер!». |
| R4 | исходник строка 4983 | `ごめん、入るな。` («Извини, **не заходи**») | EN/RU «Извини, захожу» | CANDIDATE | Контекст: Табита уже открыла дверь; JA `入るな` — по всей видимости опечатка источника (`入るね`). **PRESERVED — JA / PRESERVED** для RU: перевод идёт по intended meaning, JA не редактируется (запрет §5). Записано в `reports/log.md`. |
| P1 | `script-ch2_2.rpy:287` | сцена 83: `like("シエスタ", -10)`, `like("ハルナ", 10)`; `sympathy_canon.csv` — только 2 строки | лишний `$ update_sympathy(-10, char_key="louise")` | ERROR | Третий вызов не имеет опоры в исходнике (62 → 61). **FIXED**: строка удалена. |
| P2 | `script-ch2_3.rpy:373` | сцена 95: `play=+25`→t24, `play=+27`→**t26**, `play=+18`→t17 | `new_music="t27"` | ERROR | `t27` соответствует `+28` сцены 94 (строка 1277); здесь нужен `t26`. **FIXED** → `t26`. |

Повторные проверки после исправлений: `check_project --chapter 2` → errors=0;
`check_renpy_syntax --chapter 2` → OK; `check_typography ru` → OK; `check_assets` → OK;
`omission_precheck 2_2 / 2_3 / 2_4c` → 0 кандидатов.

---

## where I stopped / точка передачи

- Текущая фаза: **глава 2 завершена и закоммичена**. Исправления живут только в ветке
  `qa/review-ch2-5` (в `master` не сливаются).
- Следующий шаг: **глава 3** — механические проверки (`check_renpy_syntax`, `check_project`,
  `check_typography` ru/en/ja, `check_placeholders`, `check_assets`, `check_voice_transcriptions`),
  затем `omission_precheck` по всем частям 3_1…3_9, затем независимый контент-ревью EN/RU/порт.
- Последний коммит: см. `git log -1` в этой ветке (коммит с сообщением `QA ch2: …`).
