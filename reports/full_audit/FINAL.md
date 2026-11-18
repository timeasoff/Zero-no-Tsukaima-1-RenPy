# Итоговый отчёт: полный аудит глав 22–28

Ветка `port/ch22-to-end`.Scope: game/chapters/22…28, их JA/RU TL, источники chapter_23…29, связанные справочники.

## Соответствие глав (подтверждено по ps2_source/chapter_map.txt)
22↔chapter_23, 23↔24, 24↔25, 25↔26, 26↔27, 27↔28, 28↔29. Все 7 глав поддерживаются `tools/targets.py`.

## По главам

| глава | частей |EN-строк|голосов|A/B/C находок|исправлено|FIXED|OPEN|статус|
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 22 | 5 | 60 (ч.5) | 58 | 3 | 2 | 2 | 0 | DONE |
| 23 | 3 | 354 | 343 | 3 | 3 | 3 | 0 | DONE |
| 24 | 1 | 133 | 126 | 0 | 0 | 0 | 0 | DONE |
| 25 | 4 | 511 | 451 | 2+3 | 5 | 5 | 0 | DONE |
| 26 | 6 | 612 | 550 | 2+1 | 0 | 0 | 1 | DONE (OPEN F15) |
| 27 | 3 | 346 | 311 | 3+3+3 | 6 | 6 | 0 | DONE |
| 28 | 2 | 206 | 182 | 2+1 | 3 | 3 | 0 | DONE |

Итого: 24 части, 5208 EN-строк, 2364 голоса (scope без extra), 25 находок A/B/C + 3 компиляционных.

## Критические ошибки
1. **CHOICE scene 986 (гл.27)** — JA `やっぱり、ルイズかな` / `やっぱり、タバサかな` / `ごめん、キュルケが先に決めて` подменены EN/RU на «Leave it to Tabitha / Worried about after / Worried about everyone» — FIXED (ERROR, HIGH).
2. **Компиляция Ren'Py** (SDK доступен):
   - 16 TL-файлов гл.22 с `# translate ... strings:` → «Unexpected indentation» — FIXED;
   - 2 пустых TL-блока `ch26_4_choises` → FIXED (инертные пары);
   - 24 JA `new` с неэкранированным `trans("crossfade", ...)` → «Could not parse string» — FIXED техническим экранированием (смысл JA сохранён; MISMATCH_JA/OPEN на будущую очистку tag'ов из JA new).
   Повторная компиляция: **0 ошибок в зоне 22–28** (146 ошибок вне scope — главы 0–21/common, не трогались).

## Исправления локализации (15)
Список в `reports/sma/analysis/20261118-204000-phase2.md`: 相棒→Партнёр, やばい→Ой нехорошо, 騒ぎ→переполох, 嫌がる→сторонятся, 絶対→точно, ポジティブに考えた方がいいよな→Надо бы… да?, いっそのこと→раз уже так, どちらかというと/圧倒的に→скорее/подавляюще, イライラ→злит, ひどくご立腹→очень рассержена, 私のことを気に入って→проникся симпатией.

## Технические проверки (свежий прогон)
- `check_project.py` → OK (0 errors).
- `check_renpy_syntax.py` → OK.
- typography RU/EN 22–28 → OK 7/7; JA → OK 8/8.
- `check_placeholders.py`, `check_assets.py`, `check_voice_transcriptions.py` → OK с ожидаемыми предупреждениями (W6/CSV).
- `omission_precheck.py` 7/7 → 0 кандидатов.
- `audio_converter.py check` → OK (ogg на месте).
- TL-аудит: 0 ошибок old/new, дублей, пустых.
- Компиляция Ren'Py: 0 ошибок в зоне.

## Ограничения и OPEN
- B-аудитор: отдельного скилла/промпта в проекте нет — B-промпты сгенерированы вручную (`tools/gen_b_prompts.py`), это отмечено.
- `semantic-audit-a` доступен; C через `pragmatic-c`; Analyzer фазы 1/2 выполнены (3 blind + Phase2).
- F15 (`大丈夫でしょ` → «Конечно, в порядке») — OPEN, связано с OPEN zero_kiss/dispatch.
- MISMATCH_JA: ENGINE-теги в JA `new` ch90/91 оставлены (канон не редактируется); технически экранированы кавычки для компиляции.
- 146 компиляционных ошибок вне scope (гл.0–21) — не трогались по требованию.
- Runtime-прохождение маршрутов не выполнялось: только статическая проверка графа + компиляция.

## Изменённые файлы
EN: `game/chapters/27/script-ch27_2.rpy`.
JA TL: `game/tl/japanese/ch26_4_choises.rpy`, `ch27_2_choises.rpy`, `sp90_dialogs.rpy`, `sp91_dialogs.rpy`, 16 файлов гл.22 (header).
RU TL: `ch22_5_dialogs.rpy`, `ch23_1_dialogs.rpy`, `ch25_2_dialogs.rpy`, `ch26_4_choises.rpy`, `ch26_4_dialogs.rpy`, `ch27_2_choises.rpy`, `ch27_2_dialogs.rpy`, `ch28_2_dialogs.rpy`, 16 файлов гл.22 (header).
Инструменты: `tools/gen_b_prompts.py`, `tools/fix_full_audit.py`.
Отчёты: `reports/full_audit/`, `reports/sma/`, `reports/log.md`.

## Второй проход (дополнение)

- A/B/C расширены на все 24 части; 15 JA-подтверждённых исправлений (включая SUBJECT_MISMATCH ch23_3 c101 и choice-лейблы ch27_1); Analyzer Фаза 2 `reports/sma/analysis/20261118-220000-phase2-full.md`. Compile в зоне 0 ошибок.
