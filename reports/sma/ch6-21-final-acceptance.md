# Финальная комплексная приёмка — проектные главы 6–21

Ветка `review/ch6-21` (изолированный worktree), дата 2026-11-19. Приёмка готовых частей после всех предыдущих циклов. Аудиты не запускались заново механически: проверены run_id, наличие evidence и входные данные; изменившийся текст проходил последующие слои (humanizer → grammar → style → structural). Статические проверки выполнены, **runtime-проверка игры НЕ проводилась** (медиа вынесены во внешний каталог, в контейнере недоступны).

## Результаты командных проверок

- `check_project.py` → **RESULT: OK, errors=0** (labels=902, overlayK=17, strings=13143, voices=11270); warnings=928 (главным образом W6 id-заглушки и W1 вне скоупа).
- `check_renpy_syntax.py` → OK (5 NO_RPY для пустых глав 24–28).
- `check_typography.py --chapter N --lang ru`, N=6..21 → 0 ошибок во всех главах.
- `check_placeholders.py --chapter N` → только предупреждения (123 уникальных `id(K)`, 452 с заполненным filename в `image_id_map.csv`).
- `check_assets.py --chapter N` → ERROR VOICE_MISSING на все `.ogg` (418+331+…): **ограничение среды** — `game/audio` junction на внешний `ZnT1_MEDIA`, в контейнере файлов нет; как проектную ошибку не классифицирую. BGM/SE по правилам `t{K-1}`/`se{ID}` из таблицы не перепроверялись (медиа недоступны).
- `check_voice_transcriptions.py --chapter N` → OK/WARN: warnings = TRANSCRIPT_ROW_STILL_IN_QUEUE (строки голосов остаются в очереди CSV); ядро voice ID ↔ manifest — 0 пропусков (11270 ID, все `voice "…"` гл. 6–21 имеют пару). Транскрипции не переписывались.
- `omission_precheck.py` → по 47 частям (прошлый цикл), кандидаты разобраны; новые запуски не требуются, вход текста менялся только локально и покрыт последующими слоями.
- `chapter_pipeline.py --chapter N --status` → все фазы `[ ]` (кэш pipeline не использовался; evidence лежит в `reports/sma/`, кэш НЕ сбрасывался).

## Статусы по частям

| глава/часть | файл | статус | открытые вопросы |
|---|---|---|---|
| 6/1 | `script-ch6_1.rpy` | PASS | — |
| 6/2 | `script-ch6_2.rpy` | PASS | — |
| 6/3 | `script-ch6_3.rpy` | PASS | — |
| 7/1 | `script-ch7_1.rpy` | PASS | — |
| 7/2 | `script-ch7_2.rpy` | PASS | — |
| 7/3 | `script-ch7_3.rpy` | PASS | — |
| 8/1 | `script-ch8_1.rpy` | PASS | — |
| 8/2 | `script-ch8_2.rpy` | PASS | — |
| 8/3 | `script-ch8_3.rpy` | PASS | — |
| 9/1 | `script-ch9_1.rpy` | PASS | — |
| 10/1 | `script-ch10_1.rpy` | PASS | — |
| 10/2 | `script-ch10_2.rpy` | PASS | — |
| 11/1 | `script-ch11_1.rpy` | PASS | — |
| 11/2 | `script-ch11_2.rpy` | PASS | — |
| 11/3 | `script-ch11_3.rpy` | PASS | — |
| 11/4 | `script-ch11_4.rpy` | PASS | — |
| 12/1 | `script-ch12_1.rpy` | PASS | — |
| 12/2 | `script-ch12_2.rpy` | PASS | — |
| 12/3 | `script-ch12_3.rpy` | PASS | — |
| 12/4 | `script-ch12_4.rpy` | PASS | — |
| 13/1 | `script-ch13_1.rpy` | PASS | — |
| 13/2 | `script-ch13_2.rpy` | PASS | — |
| 13/3 | `script-ch13_3.rpy` | PASS | — |
| 13/4 | `script-ch13_4.rpy` | PASS | — |
| 14/1 | `script-ch14_1.rpy` | PASS | — |
| 14/2 | `script-ch14_2.rpy` | PASS | — |
| 14/3 | `script-ch14_3.rpy` | PASS | — |
| 14/4 | `script-ch14_4.rpy` | PASS | — |
| 15/1 | `script-ch15_1.rpy` | PASS | — |
| 15/2 | `script-ch15_2.rpy` | PASS | — |
| 15/3 | `script-ch15_3.rpy` | PASS | — |
| 15/4 | `script-ch15_4.rpy` | PASS | — |
| 16/1 | `script-ch16_1.rpy` | PASS | — |
| 17/1 | `script-ch17_1.rpy` | PASS | — |
| 17/2 | `script-ch17_2.rpy` | PASS | — |
| 18/1 | `script-ch18_1.rpy` | PASS | — |
| 18/2 | `script-ch18_2.rpy` | PASS | — |
| 18/3 | `script-ch18_3.rpy` | PASS | — |
| 18/4 | `script-ch18_4.rpy` | PASS | — |
| 19/1 | `script-ch19_1.rpy` | PASS | — |
| 19/2 | `script-ch19_2.rpy` | PASS | — |
| 19/3 | `script-ch19_3.rpy` | PASS | — |
| 20/1 | `script-ch20.rpy` | PASS | — |
| 21/1 | `script-ch21_1.rpy` | PASS | — |
| 21/2 | `script-ch21_2.rpy` | PASS | — |
| 21/3 | `script-ch21_3.rpy` | PASS | — |
| 21/4 | `script-ch21_4.rpy` | PASS | — |

## Свод по слоям

1. **Канон/полнота:**.order реплик сверен; пропуски — только документированные defer (ch8/ch9/ch14/ch17/ch18) и USER DECISION (ch13 jump). Смысловые исправления A/B/C+Analyzer применены с JA-доказательствами.
2. **Смысл/русский:** A (121 finding/62 FIXED), B (76/43), C (76/31), полный цикл (580/55), humanizer (28), grammar (27+11), style (20) — все правки прошли RECHECK.
3. **Терминология:** несоответствия исправлены (Тристания, Уэзерби/Везерли, Вальер, Мотсогнир, Старый Осман, Ч-что, Ваше Высочество); dictionary.md/addresses.md не редактировались.
4. **Ren'Py/TL:** 136 TL-заголовков раскомментированы, 10 курсивов закрыты, дублей old/label нет, K уникальны, битых jump-целей нет.

## Открытые вопросы (не маскируются)

- USER DECISION: W6 — массовая замена `id(K)` на имена из image_id_map.csv (затронет гл. 5/22); недостижимые сцены ch13; defer extra-ветвей и TNDL в ch10–13; omission voice 4601/4602 (ch9), 13655 (ch8), 681–683 (ch17).
- ???: `ch8_3_thoughs.rpy` — JA-текст в `old` (JA не редактируется; исправление создало бы дубли); voice-id mismatch в манифесте (929/930, 11840/11841, 3324/3327).
- PROVISIONAL: `モートソグニル` → Мотсогнир (dictionary) против «Мортогнир» в log.md; другие PROVISIONAL-записи словаря не пересматривались.
- RECONCILE: все предыдущие разрешены правкой только неверной формы; оставшиеся расхождения зафиксированы в аудите C/full-cycle.

## Итог

**Статус диапазона: PASS WITH OPEN QUESTIONS.** Все 47 частей проверены статически и имеют ясный статус; ни одна не объявлена полностью готовой к runtime без внешних медиа. Голосовые/медиа-связи не перепроверены физически (junction недоступен). Игра не запускалась, lint/compile SDK не выполнялся — это не заявляется как сделанное.
