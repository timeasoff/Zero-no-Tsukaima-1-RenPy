# Финальная приёмка порта — port/ch22-to-end (промпт 12)

Дата: 2026-11-18. Ветка `port/ch22-to-end`, worktree `/workspace/.tmp/opencode/port-final`. План: `reports/port_plan_ch22_to_end.md` (база `c0130ec`). Коммитов в ветке: **45**.

## 1. Сводка по целевым единицам

| единица | исход | частей | реплик (EN-строк) | голосов JA → порт | выборов | проверки | статус |
|---|---|---:|---:|---:|---:|---|---|
| гл.22 ч.5 | chapter_23, 1209–1213 | 1 (в папке 5) | 60 | 58 → 58 | 3/3 | ✅ | DONE |
| гл.23 | chapter_24, 849–893 | 3 | 354 | 343 → 343 | 24/24 | ✅ | DONE |
| гл.24 | chapter_25, 894–902 | 1 | 133 | 126 → 126 | 3/3 | ✅ | DONE |
| гл.25 | chapter_26, 903–933 + extra | 4 | 511 | 451 → 451 | 30/30 | ✅ | DONE |
| гл.26 | chapter_27, 934–971 + extra | 6 (вкл. 4b) | 612 | 550 → 550 | 24/24 | ✅ | DONE |
| гл.27 | chapter_28, 972–998 | 3 | 346 | 311 → 311 | 15/15 | ✅ | DONE |
| гл.28 | chapter_29, 999–1008 | 2 | 206 | 182 → 182 | 6/6 | ✅ | DONE |
| chapter_90 | 1533–1696 | sp90 | 1040 | 966 → 966 | 108/108 | ✅ | DONE |
| chapter_91 | 1697–1860 | sp91 + sp_d1 | 1149 | 956 → 879¹ | 108/108 | ✅ | DONE (с отклонением) |

¹ 77 голосов не имеют исходного `.wav`; реплики сохранены, строки `voice` удалены (`reports/extra/no_audio_ch91.md`).

**Итого:** 3943 голоса источника → 3866 в порту (3943 − 77), 5208 EN-строк, 321 choice-пункт (105 в основной линии + 216 в extra), 30 inline extra-сцен, 328 сцен chapter_90/91.

Coverage-evidence: `reports/coverage/*.md` (A–F); все проверки PASS, кроме документированного расхождения A в ch.91.

## 2. Архитектура и граф

- `tools/flow_audit.py`: 592 label, 754 jump, 7 call, 115 menu, 28 return; **битых целей 0**, **циклов из входов 0**.
- Цепочка: `ch22 → ch23 → ch24 → ch25 → ch26 → ch27 → ch28 → attention`; в гл.26 восстановлена пропущенная ветвь `ch26_4 → ch26_4b → ch26_5 → ch27`.
- Overlay K=20…25 (6 титульных карточек гл.23–28), дублей E2 = 0, `next_free=26`.
- Симпатии: 0 событий `【好感度】` в исходнике целевой области и 0 вызовов `update_sympathy` в порту — расхождений нет. `checkKiss()`-ветки: выбрана ветка `zero_kiss` по образцу гл.12; вторая зафиксирована как OPEN.
- 103 недостижимых лейбла: ~95 альтернативных корней extra (dispatch OPEN, чужая зона), невыбранные `!zero_kiss`-ветки, сцены-проводники `【移動】` — уникального контента не теряют.

## 3. Синхронность локализаций

- `tools/tl_consistency_audit.py`: 0 EN-строк без точного `old` в JA и RU, 0 дублей `old`, 0 пустых `new`, 0 `...`, 0 незакрытых `{i}`.
- JA `new` не редактировались ни разу (прямой запрет); расхождения (`MISMATCH_JA`) зафиксированы как evidence.
- RU проверен смысловыми/прагматическими аудитами и литературной вычиткой; 248 замен канонических имён приведены к `dictionary.md`.

## 4. Голоса и ресурсы

- `tools/voice_audit.py`: 9/9 единиц — порядок `[voice N]` совпадает с порядком `voice "..."`; 3866 пар имя↔id, 0 дублей, 0 speaker без `define`.
- `audio_converter.py check` → **RESULT: OK** (ogg-проверка реально выполнялась, не SKIPPED); `convert --apply` idempotent.
- `transcriptions_ja_ru.csv`: 3851 строка помечена `USED ch<unit>` строго по ID.
- BGM: 20/20 треков по формуле `t{K-1}`, missing/extra = 0; image id: 109/109 в `image_id_map.csv`, E10 = 0; FX-сигнатуры валидны; MOVIE ×2 — `MOVIE not ported`.
- W6 (35 заглушек с заполненным именем в зоне) — OPEN: замена потребовала бы правки чужих глав 0–21.

## 5. Результаты проверок (свежий прогон)

| проверка | результат |
|---|---|
| `check_project.py` | **RESULT: OK** (errors 0, warnings 1213 — глобальные/вне scope) |
| `check_renpy_syntax.py` | OK — проблем не найдено |
| `check_typography.py --lang ru` (22–28) | OK 7/7; extra: 5 ошибок в `choises.rpy`/`thoughs.rpy` — зона глав 0–21 |
| `check_typography.py --lang en` (22–28) | OK 7/7; extra: 30 ошибок в `sp_l1.rpy` — зона глав 0–21 |
| `check_placeholders.py` | OK с предупреждениями (2034 — глобальные W6) |
| `check_assets.py` | OK с 1 предупреждением (CSV-очередь глав 0–21) |
| `check_voice_transcriptions.py` | OK с предупреждениями (6034 — глобальная очередь) |
| `omission_precheck.py` (22–28, extra) | 8/8 целей → 0 кандидатов |
| `audio_converter.py check` | RESULT: OK |
| `task_board.py verify` | 4/4 подзадачи OK, проблем 0 |
| `chapter_pipeline.py --status` | состояние не заполнялось для этих частей (проверки запускались напрямую); кэш не сбрасывался |

## 6. Открытые вопросы и ограничения

1. **77 NO AUDIO (ch.91)** — нет дорожек в архиве; реплики сохранены без `voice`. PRESERVED — NO AUDIO.
2. **Dispatch `zero_tundele`** — call-site в главах 0–21 (чужая зона); sp90/sp91 существуют как entry points, но не подключены. OPEN.
3. **W6 / замена заглушек** — OPEN: нет scope-замены, `replace_bg_placeholders.py` затронул бы чужие главы.
4. **`zero_kiss` / ветвление по датам** — не реализовано в ремастере; выбрана ветка `zero_kiss`, альтернативная зафиксирована. OPEN/PROVISIONAL.
5. **Регистр «мисс» / обращения** — USER DECISION (расхождение с `addresses.md` при последовательном использовании в арке).
6. **MOVIE ×2** — SKIP по проектной таблице.
7. **Среда**: Ren'Py SDK отсутствует (синтаксис проверен `check_renpy_syntax.py`, не реальным движком); внешний PS2-архив и медиа-junctions из этой среды недоступны — бинарные ресурсы не проверялись визуально; `semantic-audit-a` и `tl-en-ru` недоступны, `semantic-audit-b` отсутствует на диске — их роли выполнены ручной сверкой и доступными аудиторами; `style_scan.py` отсутствует — создан консервативный предфильтр.

## 7. Итог

Все плановые части гл.22 ч.5, гл.23–28 и отдельные `chapter_90/91` имеют отчёты, прошли обязательные проверки и закоммичены. Статус целевой области: **DONE** с документированными отклонениями (п.6). Главы 0–21, другие ветки/worktree, JA-оригинал и бинарные медиа не трогались.

### Ключевые отчёты
`reports/port_plan_ch22_to_end.md`, `reports/FINAL_ACCEPTANCE.md`, `reports/coverage/README.md`, `reports/flow_sympathy_ch22_to_end.md`, `reports/en_ru_tl_consistency.md`, `reports/voice_workflow_ch22_to_end.md`, `reports/semantic_pragmatic_review.md`, `reports/ru_literary_review.md`, `reports/assets_media_fx.md`, `reports/inline_extra_registry.md`, `reports/log.md`, `reports/translation_plan.md`.
