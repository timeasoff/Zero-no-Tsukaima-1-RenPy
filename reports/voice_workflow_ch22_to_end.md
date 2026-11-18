# Голосовая часть: гл.22 ч.5, гл.23–28, chapter_90/91

Дата: 2026-11-18. Ветка `port/ch22-to-end`. Скилл `voice-workflow`.
**Правило: ID только из `[voice N]` (сверено с `events_full/`), NEVER по тексту ASR.**

## 1. Метод

- Источник ID: `ps2_source/chapters/*.txt` → `[voice N]`; соответствие `(0x04000000+N)` в `events_full/` и имени `VOICE_ID.BIN_%08X.wav` проверено скиллом.
- Имя: для глав `ch<N>_<spk>_<NNN>`, для extra `sp90/sp91_s<scene>_<item>` (принятая схема этих порций), для восстановленной части 4b — `ch26_4b_<spk>_<NNN>`.
- Speaker: сверен с `game/characters.rpy` (все коды определены), ASR-колонка `original` не менялась.
- Порядок: `tools/voice_audit.py` (создан в этом проходе) сравнивает последовательность `[voice N]` источника с последовательностью имён `.rpy`, решённых через манифест; для `chapter_91` файлы `sp91.rpy` и `sp_d1.rpy` интерливлятся по номеру сцены (1700 → 1701…).

## 2. Счётчики по единицам

| единица | `[voice N]` в источнике | `voice "..."` в порту | порядок | без wav | CSV помечено | пропущено ID |Speaking без define | дублей имён |
|---|---:|---:|---|---:|---:|---:|---|---:|
| ch22_5 | 58 | 58 | OK | 0 | 58 | 0 | 0 | 0 |
| ch23 | 343 | 343 | OK | 0 | 343 | 0 | 0 | 0 |
| ch24 | 126 | 126 | OK | 0 | 126 | 0 | 0 | 0 |
| ch25 | 451 | 451 | OK | 0 | 451 | 0 | 0 | 0 |
| ch26 (вкл. 4b) | 550 | 550 | OK | 0 | 550 | 0 | 0 | 0 |
| ch27 | 311 | 311 | OK | 0 | 311 | 0 | 0 | 0 |
| ch28 | 182 | 182 | OK | 0 | 182 | 0 | 0 | 0 |
| chapter_90 | 966 | 966 | OK | 0 | 966 | 0 | 0 | 0 |
| chapter_91 (+sp_d1) | 956 | 879¹ | OK | 0 | 879 | 77² | 0 | 0 |
| **ИТОГО** | **3943** | **3866** | **9/9 OK** | **0** | **3866** | **77** | **0** | **0** |

¹ 956 − 77 = 879. ² См. §4.

Evidence: `reports/voice_audit.md`.

## 3. Обработка `transcriptions_ja_ru.csv`

- **Было:** все 3866 используемых ID оставались активными строками очереди (свидетельство `check_voice_transcriptions.py`: `TRANSCRIPT_ROW_STILL_IN_QUEUE`).
- **Сделано:** `tools/mark_target_transcriptions.py` (создан в проходе) пометил status 3851 строку тегом `USED ch<unit>`; 15 строк уже были помечены ранее. Колонка `original` **не изменялась**, строки не удалялись (обратимая пометка по правилу skill §3.8).
- Выбор `USED chN` вместо комментирования filename: формат распознаётся и `check_voice_transcriptions.py` (`RE_STATUS_MARK`), и `audio_converter.py`.
- После правки: `check_voice_transcriptions.py --chapter 23…28` → `OK — проблем не найдено`; `--chapter 22` → OK с предупреждениями **только по частям 1–4** (не входят в scope этого прохода, 415 шт), глобально `TRANSCRIPT_ROW_STILL_IN_QUEUE = 0`.

## 4. Missing IDs / NO AUDIO

77 ID `chapter_91` не имеют дорожки в `wav_files/` (проверено по `VOICE_ID.BIN_%08X.wav`, а также через STV-архив при первом порте): 5035, 10333, 5036, 10334, 10335, 10336, 5037, 10337, 5038, 10338, … Полный список — `reports/extra/no_audio_ch91.md`.

- По правилу AGENTS.md реплики **сохранены**, строки `voice` удалены; повторной попытки переиспользовать чужую дорожку не было.
- Classification: **CANDIDATE → PRESERVED — NO AUDIO**. В `voice_check.md` эти ID попадают в раздел «Манифест, не используемый сценарием» (ложное срабатывание для проверки `W2`-логики).
- Дополнительно: `ch17_soldier_002` (4227) и `ch9_l_001/002` (4601/4602) — неunused-manifest записи из чужих глав 0–21, не трогались.

## 5. Говорящие и формат имён

- Все фактические speaker-коды (`s/l/k/t/si/h/ha/m/d/g/c/o/th/ak/…`) определены в `game/characters.rpy` → `voice_audit` даёт 0 undefined.
- `audio_converter.py check` печатает `4b_k/4b_s/4b_t`, `a`, `d1_d`, `e`, `mer`, `un` как «говорящие без define» и ~1800 имён `sp90_*/sp91_*` как «нестандартный формат» — это **артефакты парсера имён** (`SPEAKER_RE` извлекает сегмент `4b_s` из `ch26_4b_s_001` и не понимает префикс `sp90_`), а не реальные пропуски `define`.
  - Classification: **CANDIDATE → FALSE POSITIVE** (speaker-код подтверждён по коду реплики и `characters.rpy`).
  - Решение: имена не переименовывались — переименование создало бы осиротевшие `.ogg`, а удаление файлов запрещено промптом.
- Дублирований имени `voice` внутри файлов нет; повтор ID в источнике (13789 в гл.90, 5320 в гл.91) — легитимное PS2-переиспользование одной дорожки, разные `voice_name`.

## 6. Конвертация и ссылки

Порядок по скиллу: `audio_converter.py check` → `convert --apply` → `check` → `check_project.py`.

- `check`: `строк=15134 ogg=15134 pending=0 нет_аудио=0 нет_в_манифесте=0 предупреждений=90` → **RESULT: OK**.
- `convert --apply`: `к конвертации: 0` (идемпотентно, все `.ogg` созданы на предыдущих этапах) → **RESULT: OK**.
- Post-`check`: те же цифры → **RESULT: OK**. `ogg check SKIPPED` — нет, проверка реально выполнена.
- `check_project.py` → `RESULT: OK` (E3=0, т.е. каждая строка `voice` имеет `.ogg`; W2 не содержит новых бракованных ссылок).
- `.ogg` в git не добавлялись (динамические медиа, `game/INSTRUCTION.md`).

## 7. Изменения и коммит

- `transcriptions_ja_ru.csv` — 3851 статусная пометка (только scope этого прохода).
- `tools/voice_audit.py`, `tools/mark_target_transcriptions.py` — новые аудитор и scope-маркер.
- `reports/voice_audit.md`, `reports/voice_check.md`, `reports/voice_convert.md`, `reports/log.md` — отчёты.
- Ни один `.rpy`, JA/RU `tl`, `voice_id_map.csv` в этом проходе не менялись (все пары имя↔id были внесены на этапах порта).

## 8. Чек-лист

- [x] `task_board.py status` выполнен первым;
- [x] ID брались только из `[voice N]`, не по тексту;
- [x] дорожки найдены для всех 3866 используемых ID; 77 NO AUDIO документированы;
- [x] speaker сверены с `characters.rpy`, новых `define` не потребовалось;
- [x] каждая строка `voice` ↔ пара в манифесте ↔ `.ogg`;
- [x] порядок voice совпадает с источником во всех 9 единицах;
- [x] `transcriptions_ja_ru.csv` промаркирован строго по ID;
- [x] `audio_converter.py check` → convert → check: RESULT OK; `check_project.py` OK;
- [x] отчёт написан; PROVISIONAL/NO AUDIO/FALSE POSITIVE зафиксированы в `reports/log.md`.
