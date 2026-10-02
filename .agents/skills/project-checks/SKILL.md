---
name: project-checks
description: Автопроверки проекта: все проверки tools/check_project.py (E1…E10, W1…W6, I1 — формулировки по коду скрипта), исключения read-only (game/tl/*/common.rpy), как запускать и как читать reports/check_project.md, плюс ручной чек-лист приёмки части и первичный чек-лист запуска. Применять после каждой записи файлов части, перед отчётом reports/ch<N>/<part>.md и перед финальным завершением главы.
---

# project-checks — автопроверки и чек-листы приёмки

## 1. Запуск

```powershell
python tools/check_project.py                 # полный прогон + отчёт
python tools/check_project.py --chapter 2     # проверить только главу 2 (I1)
python tools/check_project.py --no-report     # без записи отчёта
```

* Консоль выводит **только ASCII** (PowerShell здесь cp1251) — детали и тексты строк
  всегда в `reports/check_project.md` (UTF-8, перезаписывается при каждом запуске).
* Код возврата: `0` при `RESULT: OK`, `1` при `RESULT: ERRORS`.
* В консоль печатается сводка:
  `labels=N overlayK=N strings=N voices=N` / `errors=N warnings=N info=N` /
  `report: reports/check_project.md` / `RESULT: OK|ERRORS`.

Опции нет фильтра по кодам: чтобы локализовать проблему, открой отчёт и найди
строку `E4 …`/`W1 …` — в ней есть файл и номер строки.

## 2. Отчёт `reports/check_project.md`

Три секции: `## ERROR (n)`, `## WARNING (n)`, `## INFO (n)`; каждый пункт — строка
вида `E7 jump 'ch1_11' at game/chapters/1/script-ch1_10.rpy:999 has no label`.

Полезные INFO-строки:

```text
speakers defined: N                      # сколько define … = Character( найдено
overlay K: max=6 used=6 next_free=7       # следующий свободный K для overlay_screen
voices: refs=N ogg=N missing=N            # либо … ogg check SKIPPED (audio not installed)
I1 ch2: strings=… source_talk=1382        # прогресс против chapter_stats.json
labels=… rpy=… strings(strict=…) tl_old=japanese:N,russian:M
```

⚠️ `ogg check SKIPPED` — проверка голосов **не выполнялась** (нет `game/audio/voices/`),
это не «пройдено».

**Область строгих проверок (ERROR):** только строки в `game/chapters/`; остальной
игре — предупреждения (W5); `game/remark/` исключён целиком (у него свои файлы на
каждый язык); исключены также `/saves/`, `/cache/`.

**Исключение read-only:** `game/tl/japanese/common.rpy` и `game/tl/russian/common.rpy`
взяты из документации Ren'Py — файлы помечены атрибутом `+R`, **не редактируются и не
проверяются**: их ключи участвуют в покрытии E4/E5, но E6/E8/W1 для них не выдаются
(см. `TL_READONLY_SUFFIXES` в коде).

## 3. Проверки (по коду `tools/check_project.py`)

### ERROR

| код | формулировка по коду скрипта | как чинить |
|---|---|---|
| **E1** | duplicate label names across `game/**/*.rpy` | переименовать дубликат (в сообщении: имя и `файл:строка` для каждого вхождения) |
| **E2** | duplicate `from _call_overlay_screen_K` suffixes | дать вызову новый свободный `K` (см. INFO `next_free=`) |
| **E3** | `voice "..."` referencing a missing `.ogg` (skipped if audio not installed) | положить `.ogg` с точно таким именем либо исправить строку `voice` |
| **E4** | translatable string in `game/chapters/` without an entry in `tl/japanese` | добавить `old/new` в нужный бакет `game/tl/japanese/` |
| **E5** | translatable string in `game/chapters/` without an entry in `tl/russian` | то же в `game/tl/russian/` |
| **E6** | empty `new ""` in `tl` | заполнить перевод (пустой `new` запрещён) |
| **E7** | `jump` / `call` to a label that does not exist | создать лейбл или поправить цель; `call screen` не считается |
| **E8** | tl file declares a different language than its folder | в `tl/japanese/` должен быть `translate japanese strings:`, в `tl/russian/` — `translate russian strings:` |
| **E9** | invalid / duplicate rows in `references/image_id_map.csv` (битый `image_id`, дубль строки, нет файла при используемых заглушках) | `python tools/build_image_id_map.py` пересоберёт файл, сохранив заполненные `filename`/`notes`; дубли строк — убрать руками |
| **E10** | placeholder `id(K)` in a script that is not in `image_id_map.csv` | id выдуман/опечатан → сверить с `[BG … image=+K]` в `ps2_source/` и добавить строку генератором |

Как скрипт находит строки (важно для диагностики): кандидатами считаются
`<ident> "текст"` (диалог, если `ident` объявлен через `define … = Character(`),
`"текст":` в `menu:`, голая строка `"текст"` (нарратив), `"text": "…"` (пункт
`*_choice`), второй аргумент `call overlay_screen(…, "текст"…)`, `_("текст")`.
Кавычки внутри строк считаются по `\"`, поэтому **многострочная реплика без
экранирования даёт W3**.

### WARNING

| код | формулировка по коду скрипта | что делать |
|---|---|---|
| **W1** | `old` keys in tl with no matching script string (stale / mismatched `old`) | обычно опечатка в `old` или строка сценария уже изменена → сверить дословно |
| **W2** | `.ogg` files referenced by nobody | брак: удалить/переименовать либо добавить строку `voice` |
| **W3** | unbalanced quote on a script line (possible multi-line dialogue) | реплика должна быть в одной строке (переносы JA склеиваются в `tl`) |
| **W4** | unknown speaker identifier in `game/chapters/` (character has no `define`) | завести `define <code> = Character(…)` (скилл `voice-workflow` §4.3) |
| **W5** | translatable string OUTSIDE `game/chapters/` without tl entry (UI/screens) | добавить `old/new`, если строка действительно должна переводиться |
| **W6** | placeholder `id(K)` whose id IS mapped (replacement is pending) | имя уже заполнено в справочнике → `python tools/replace_bg_placeholders.py --apply` |

### INFO

| код | формулировка по коду скрипта |
|---|---|
| **I1** | chapter string counts vs talk counts in `ps2_source/chapter_stats.json` |

Логика I1: для папки `game/chapters/<N>/` берётся число переводимых строк, а
источник — `talk` главы источника **`N+1`** (`chapter_stats.json`).

* `strings > talk` → **WARNING** `I1 chN: X script strings > Y source talk`
  (строк больше, чем реплик в каноне — почти всегда лишнее);
* `strings == talk` → INFO без пометки;
* `strings < talk` → INFO `(gap expected)` — норма в процессе работы;
* глава не начата (`strings = 0`) → INFO `not started (source talk=…)`.

Дополнительно печатается строка без кода — сводка по справочнику картинок:

```text
image map: ids=312 named=0 open=312 | placeholders=0 in 0 file(s)
```

`named` — сколько id уже сопоставлено (колонка `filename`), `open` — сколько ждёт
заполнения человеком, `placeholders` — сколько заглушек `id(K)` сейчас в `.rpy`.

## 4. Ручной чек-лист приёмки части

Закрытым считается part, по которому выполнены **все** пункты и написан отчёт
`reports/ch<N>/<part>.md`.

- [ ] Каждая реплика из `ps2_source/chapters/chapter_NN_*.txt` есть в `.rpy`
      **в том же порядке** (I1: счётчик строк совпадает с `talk` для главы).
- [ ] Каждый `[BG stage …]` / `[EVENT_CG …]` / блок `[SPRITE …]` порождает
      `*_fx`/`show_sprites`.
- [ ] Каждый `[BGM play=+K]` → `t{K-1}`; ни один `t*` не взят «на глазок».
- [ ] Каждый `→ next scene` / `【…】` → конкретный `jump`/`menu`/`*_choice`; дыр в графе нет.
- [ ] Каждый `【好感度】X N` → `update_sympathy(N, char_key="…")`.
- [ ] `voice "…"` → существующий `.ogg` в `game/audio/voices/`; использованные строки
      `transcriptions_ja_ru.csv` удалены/помечены; лишних ссылок нет (E3/W2).
- [ ] У каждой новой EN-строки есть `old/new` **и** в `tl/japanese`, **и** в
      `tl/russian` (в правильном бакете), `old` дословно совпадает со строкой сценария.
- [ ] JA-`new` дословно из источника, переносы строк склеены, мысли в `（ ）`.
- [ ] Все `K` в `from _call_overlay_screen_K` уникальны; все `label` уникальны.
- [ ] Нижняя часть последней части главы — `jump attention`.
- [ ] `python tools/check_project.py` → `RESULT: OK`.
- [ ] Проект компилируется/запускается; в японском и русском режимах текст не
      «улетает» в EN.
- [ ] Отчёт `reports/ch<N>/<part>.md` написан; PROVISIONAL/??? — в `reports/log.md`.

## 5. Первичный чек-лист запуска (перед началом работы над главой)

- [ ] `AGENTS.md` и скиллы по `AGENTS.md` §7 прочитаны.
- [ ] `dictionary.md`, `addresses.md` перечитаны перед главой.
- [ ] Источник главы прочитан целиком (`ps2_source/chapters/`), точные аргументы —
      `ps2_source/events_full/`.
- [ ] Часть определена алгоритмом резки (скилл `ps2-source` §7); имена файлов/лейблов
      детерминированы.
- [ ] Справочники под рукой: `references/ps2_to_renpy.csv`, `references/image_id_map.csv`.
- [ ] `python tools/check_project.py` прогнан до начала работы (базовое состояние
      зафиксировано в `reports/check_project.md`).
- [ ] Журнал `reports/log.md` открыт для записи PROVISIONAL/???.

## 6. Рекомендуемый ритм

```text
запись части  →  python tools/check_project.py  →  разбор ERROR/WARNING
             →  отчёт reports/ch<N>/<part>.md   →  запись решений в reports/log.md
перед финалом главы → прогон ещё раз → RESULT: OK + I1-счётчик сходится с talk
```

Ошибки сканера — только **evidence**: каждая находка проходит полный жизненный цикл
сигнала (`DETECT → … → RECORD`) с classification/disposition — см. `project-constraints`.
