# Инженерная целостность Ren'Py, ветвлений и TL — главы 6–21

Ветка `review/ch6-21`. Аудит по `renpy-remaster-api`, `ps2-source`, `tl-en-ru`, `project-checks`, `project-constraints`, справочникам `ps2_to_renpy.csv`, `routes.md`, `sympathy_canon.csv` и эталонам глав 0/1. Архитектура не переписывалась.

## Проверки (точный CLI)

- `python tools/check_project.py` → **RESULT: OK, errors=0** (labels=902, overlayK=17, strings=13143, voices=11270).
- `python tools/check_renpy_syntax.py` → OK (5 предсуществующих NO_RPY для пустых глав 24–28).
- `python tools/check_typography.py --chapter N --lang ru` по всем 16 главам → 0 ошибок.
- `python tools/check_placeholders.py --chapter N` (выборочно 6/10/13/18/21) → только предупреждения.

## FIXED — техническая целостность TL (146 правок)

- **136 файлов** `game/tl/{japanese,russian}/ch<N>_*.rpy` (гл. 10–21): закомментированный заголовок `translate … strings:` раскомментирован. До правки все пары `old/new` в этих файлах находились вне активного блока и **не применялись движком**; другой файл той же части с активным заголовком мог подменить перевод. После правки `check_project.py` и `check_renpy_syntax.py` — OK.
- `game/tl/russian/ch10_2_dialogs.rpy`: 10 строк с незакрытым курсивом `_(…` → `_(…)_`; ещё одна строка с голыми скобками → `_(…)_` (ранее), плюс `...` → `…`.

## Ручная сверка структур

- Labels: 517 в диапазоне, дублей 0; 10 «не найденных» jump-целей — это `call overlay_screen(...)`, переходы на `ch22` и `sp_l1` (вне диапазона/другие сущности), не битые цели.
- `call overlay_screen(...) from _call_overlay_screen_K`: K глобально уникальны (проверка `check_project.py`, overlayK=17).
- Сигнатуры `*_fx`, `show_sprites`, `update_sympathy`, `*_choice`, `overlay_screen` — по эталону; ошибок E-уровня нет. Непортированные `item/battle/movie/coffee` остаются в статусе SKIP/DEFERRED по таблице.
- Дубли `old` внутри языка/бакетов: 0 (кроме защищённого `options.rpy`, не входит в аудит).
- Покрытие: каждая не-multiline EN-строка гл. 6–21 имеет `old` в JA/RU; исключение — один испорченный файл (см. ???).

## FALSE POSITIVE / ??? (не исправлялось)

- W1 (8 предупреждений в ch8): `old`-строки мыслей вида `(…)`/scene dialogue корректно совпадают с EN `s (…)`; предфильтр `check_project.py` не распознаёт некавычечную форму → ложное срабатывание.
- W6 (452 в диапазоне + 170 вне диапазона): `id(N)`-заглушки фонов, для которых в `image_id_map.csv` уже есть filename. Для массовой замены есть `tools/replace_bg_placeholders.py --apply`, но это широкая реорганизация (включает гл. 5 и 22 вне скоупа) — USER DECISION, не применялось.
- ??? `game/tl/{japanese,russian}/ch8_3_thoughs.rpy:23`: в `old` записан японский текст вместо EN (остальные 6 пар того файла тоже имеют JA в `old`). Исправление потребовало бы менять JA-строки/создавать дубли `old` в соседнем корректном бакете `ch8_2_thoughs.rpy`; JA не редактируется — USER DECISION.
- USER DECISION (из предыдущих проходов): `jump ch14` в `script-ch13_3.rpy:19` и `script-ch13_4.rpy:330/403/459` делает сцены 568–577/1184–1188 недостижимыми; предложенные Analyzer'ом цели неоднозначны (риск зацикливания) — без решения владельца архитектуры не трогалось.

## Состояние

- Ветка подтверждена: `review/ch6-21`; технические правки внесены и повторно проверены; дальше цикл не запускался.
