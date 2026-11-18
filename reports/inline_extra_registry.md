# Реестр inline extra-сцен глав 23–28

Источник: `ps2_source/chapters/chapter_24`…`chapter_29`. По таблице глав,
`extra scenes:` есть только у проектных глав 25 (`chapter_26`, 25 сцен) и 26
(`chapter_27`, 5 сцен). Главы 23, 24, 27, 28 — `extras=0`.

Все 30 сцен портированы **внутри соответствующих частей** основной линии
(не вынесены в `game/chapters/extra/`) — по правилу AGENTS.md §6 и промпта 03.

## Глава 25 (`chapter_26`) — 25 сцен

| source scene | вызывающий label | целевой label | условие запуска | точка возврата | статус | коммит |
|---|---|---|---|---|---|---|
| 1214 | `ch25_3_scene_933` (dateItem Табасы) | `ch25_3_scene_1214` | выбор `【選択肢】旅の目印/占い/時刻` в 1214 | `ch25_3_scene_1218` → `jump ch26` (scene 934) | DONE | см. коммит ч.3 гл.25 |
| 1215 | `ch25_3_scene_1214` menu | `ch25_3_scene_1215` | выбор 1 | `ch25_3_scene_1218` | DONE | там же |
| 1216 | `ch25_3_scene_1214` menu | `ch25_3_scene_1216` | выбор 2 | `ch25_3_scene_1218` | DONE | там же |
| 1217 | `ch25_3_scene_1214` menu | `ch25_3_scene_1217` | выбор 3 | `ch25_3_scene_1218` | DONE | там же |
| 1218 | `ch25_3_scene_1215/16/17` | `ch25_3_scene_1218` | `→ next scene 1218` | `jump ch26` (934) | DONE | там же |
| 1513 | `ch25_2_scene_922` 【移動】劇場 | `ch25_4_scene_1513` | выбор/location | `jump ch25_2_scene_927` (moveInit 927 → 931) | DONE | см. коммит ч.4 гл.25 |
| 1514 | `ch25_4_scene_1513` menu | `ch25_4_scene_1514` | выбор 1 | `ch25_4_scene_1517` | DONE | там же |
| 1515 | `ch25_4_scene_1513` menu | `ch25_4_scene_1515` | выбор 2 | `ch25_4_scene_1517` | DONE | там же |
| 1516 | `ch25_4_scene_1513` menu | `ch25_4_scene_1516` | выбор 3 | `ch25_4_scene_1517` | DONE | там же |
| 1517 | `ch25_4_scene_1514/15/16` | `ch25_4_scene_1517` | `→ next scene 1517` | `jump ch25_2_scene_927` → 931 | DONE | там же |
| 1518 | `ch25_2_scene_922` 【移動】表通り | `ch25_4_scene_1518` | выбор/location | `jump ch25_2_scene_927` → 931 | DONE | там же |
| 1519 | `ch25_4_scene_1518` menu | `ch25_4_scene_1519` | выбор 1 | `ch25_4_scene_1522` | DONE | там же |
| 1520 | `ch25_4_scene_1518` menu | `ch25_4_scene_1520` | выбор 2 | `ch25_4_scene_1522` | DONE | там же |
| 1521 | `ch25_4_scene_1518` menu | `ch25_4_scene_1521` | выбор 3 | `ch25_4_scene_1522` | DONE | там же |
| 1522 | `ch25_4_scene_1519/20/21` | `ch25_4_scene_1522` | `→ next scene 1522` | `jump ch25_2_scene_927` → 931 | DONE | там же |
| 1523 | `ch25_2_scene_922` 【移動】裏通り | `ch25_4_scene_1523` | выбор/location | `jump ch25_2_scene_927` → 931 | DONE | там же |
| 1524 | `ch25_4_scene_1523` menu | `ch25_4_scene_1524` | выбор 1 | `ch25_4_scene_1527` | DONE | там же |
| 1525 | `ch25_4_scene_1523` menu | `ch25_4_scene_1525` | выбор 2 | `ch25_4_scene_1527` | DONE | там же |
| 1526 | `ch25_4_scene_1523` menu | `ch25_4_scene_1526` | выбор 3 | `ch25_4_scene_1527` | DONE | там же |
| 1527 | `ch25_4_scene_1524/25/26` | `ch25_4_scene_1527` | `→ next scene 1527` | `jump ch25_2_scene_927` → 931 | DONE | там же |
| 1528 | `ch25_2_scene_922` 【移動】街道 | `ch25_4_scene_1528` | выбор/location | `jump ch25_2_scene_927` → 931 | DONE | там же |
| 1529 | `ch25_4_scene_1528` menu | `ch25_4_scene_1529` | выбор 1 | `ch25_4_scene_1532` | DONE | там же |
| 1530 | `ch25_4_scene_1528` menu | `ch25_4_scene_1530` | выбор 2 | `ch25_4_scene_1532` | DONE | там же |
| 1531 | `ch25_4_scene_1528` menu | `ch25_4_scene_1531` | выбор 3 | `ch25_4_scene_1532` | DONE | там же |
| 1532 | `ch25_4_scene_1529/30/31` | `ch25_4_scene_1532` | `→ next scene 1532` | `jump ch26` (934) | DONE | там же |

Проверено: `events_full/chapter_26` содержит `DATE dateItem("タバサ", 0x01000000+1214)`
и `date(0x01000000+934, ...)` — переход из 933 и возврат в 934 сохранены.
Меню 1513/1518/1523/1528 созданы из `【移動】` сцены 922, итог — возврат в 931.

## Глава 26 (`chapter_27`) — 5 сцен

| source scene | вызывающий label | целевой label | условие запуска | точка возврата | статус | коммит |
|---|---|---|---|---|---|---|
| 1219 | `ch26_5` (dateItem Табасы, events_full +1219) | `ch26_5_scene_1219` | выбор `【選択肢】俺のこと/かばった/春奈のこと` | `ch26_5_scene_1223` → `jump ch27` (972) | DONE | коммит ч.5 гл.26 |
| 1220 | `ch26_5_scene_1219` menu | `ch26_5_scene_1220` | выбор 1 | `ch26_5_scene_1223` | DONE | там же |
| 1221 | `ch26_5_scene_1219` menu | `ch26_5_scene_1221` | выбор 2 | `ch26_5_scene_1223` | DONE | там же |
| 1222 | `ch26_5_scene_1219` menu | `ch26_5_scene_1222` | выбор 3 | `ch26_5_scene_1223` | DONE | там же |
| 1223 | `ch26_5_scene_1220/21/22` | `ch26_5_scene_1223` | `→ next scene 1223` | `jump ch27` (972) | DONE | там же |

## Проверки

- `check_project.py` → RESULT: OK (0 ошибок, E7 «нет метки» отсутствует).
- Все 30 лейблов найдены на диске; дублей нет; переходы из всех веток ведут к точкам возврата.
- `references/dictionary.md`, `addresses.md` не менялись.
- Таблица `dlEventId/tnEventId → label`: в проекте отдельного файла нет; соответствие
  задокументировано в этом реестре (дублирование в `references/` не создавал).

## Недостающие данные / ??? 

- Нет. Все 30 сцен имеют точные аргументы в `ps2_source/events_full/` и JM-текст в `ps2_source/chapters/`.
