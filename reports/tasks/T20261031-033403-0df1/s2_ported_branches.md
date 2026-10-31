# Инвентарь развилок портированного кода (главы 0–6 + extra)

Дата: 2026-10-31. Задача S2 (промпт: `reports/tasks/prompts/T20261031-033403-0df1_S2.md`). Область: `game/chapters/0..6/*.rpy`, `game/chapters/extra/*.rpy`. Скрипты не изменялись — инвентаризация только чтением.

Метод: построчная экстракция событий (`menu`, `if/elif/else`, `jump`, `call`, `update_sympathy`, choice-экраны, `label`) в промежуточный TSV + чтение исходников для тел веток; таблицы собраны программно, счётчики и ключевые факты перепроверены отдельно.

Обозначения. **Типы**: `menu` — обычное меню; `date` — меню внутри лейблов с `date`; `if` — if/elif/else по store-переменным; `route` — диспетчеры маршрутов (`zero_route`, `louise_sympathy == 100`); `portrait_choice`/`sprite_choice` — экраны выбора; `extra` — точки вызова extra-сцен; `jump` — безусловный переход (в инвентаре — только выход пролога; остальные безусловные jump-переходы — в §Связность). **Текст**: `→ далее`/`продолжение` = fallthrough (поток идёт ниже выбора/условия); `+20@louise` = `update_sympathy(20, char_key=…)` (без `char_key` в исходнике — по умолчанию `louise`, `game/scripts/features/sympathy.rpy:418`); `-N` — отрицательная симпатия; тексты опций EN без скрытых тегов `{#…}`, обрезка на 40 символов; `(в опции меню)` / `(влож. if …)` / `внутри: …` — вложенность; `[gN]` — guard из колонки `условие`.

## Глава 0 (game/chapters/0)

| файл:строка | лейбл/блок | тип | условие | варианты → цели | симпатия на ветках | примечание |
|---|---|---|---|---|---|---|
| game/chapters/0/script-ch0.rpy:72 | ch0 > выход пролога | jump | нет | безусловный: → jump ch1 (game/chapters/1/script-ch1_1.rpy:24) | нет | 4× call overlay_screen + call intro — в §Связность |

### Связность

Цепочка частей (межфайловые jump внутри главы): —

Выходы из главы (чужие главы / внешние лейблы, в т.ч. `jump attention`):

- `game/chapters/0/script-ch0.rpy:72` (`ch0`) → **jump** `ch1` → `game/chapters/1/script-ch1_1.rpy:24`

Вызываемые чужие/helper-лейблы (`call`):

- `game/chapters/0/script-ch0.rpy:3` (`ch0`) → **call** `overlay_screen` → `game/scripts/overlay/overlay_screen.rpy:71` ×4
- `game/chapters/0/script-ch0.rpy:70` (`ch0`) → **call** `intro` → `game/script.rpy:1`

## Глава 1 (game/chapters/1)

| файл:строка | лейбл/блок | тип | условие | варианты → цели | симпатия на ветках | примечание |
|---|---|---|---|---|---|---|
| game/chapters/1/script-ch1_1.rpy:6 | forest_battle > if-цепочка | if | if _return == "start_battle"<br>elif _return == "cancel" | 1) → call screen battle_screen; → return (выход из звонка); (влож. if _return == "victory")<br>2) → продолжение после условия (fallthrough) | 1: нет<br>2: нет | WARNING Z3: лейбл недостижим (call закомментирован) |
| game/chapters/1/script-ch1_1.rpy:13 | forest_battle > if-цепочка | if | внутри: if _return == "start_battle"<br>if _return == "victory"<br>elif _return == "defeat" | 1) → return (выход из звонка)<br>2) → продолжение после условия (fallthrough) | 1: нет<br>2: нет | WARNING Z3: лейбл недостижим (call закомментирован) |
| game/chapters/1/script-ch1_1.rpy:124 | ch1 > menu | menu | нет | 1. I thoughts it's good! → далее (после меню)<br>2. I don't care. → далее (после меню)<br>3. It's terrible! → далее (после меню) | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/1/script-ch1_1.rpy:132 | ch1 > if-цепочка | if | if choise_result == "good"<br>elif choise_result == "neutral"<br>elif choise_result == "bad"<br>else | 1) → продолжение после условия (fallthrough)<br>2) → продолжение после условия (fallthrough)<br>3) → продолжение после условия (fallthrough)<br>4) → продолжение после условия (fallthrough) | 1: +20@louise<br>2: нет<br>3: -20@louise<br>4: нет | — |
| game/chapters/1/script-ch1_1.rpy:231 | ch1 > if-цепочка | if | if choise_result == "good"<br>else | 1) → продолжение после условия (fallthrough)<br>2) → продолжение после условия (fallthrough) | 1: нет<br>2: нет | — |
| game/chapters/1/script-ch1_1.rpy:372 | ch1 > menu | menu | нет | 1. Let me think for a moment. → далее (после меню)<br>2. Like hell I'd do that! → далее (после меню)<br>3. Alright... I'll hand her over. → далее (после меню) | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/1/script-ch1_1.rpy:380 | ch1 > if-цепочка | if | if choise_result == "good"<br>elif choise_result == "neutral"<br>elif choise_result == "bad" | 1) → продолжение после условия (fallthrough)<br>2) → продолжение после условия (fallthrough)<br>3) → продолжение после условия (fallthrough) | 1: +20@louise<br>2: нет<br>3: -20@louise | — |
| game/chapters/1/script-ch1_1.rpy:577 | ch1 > menu | menu | нет | 1. I don't recall. → далее (после меню)<br>2. I didn't do anything! → далее (после меню) | 1: нет<br>2: нет | скрытых условий у опций нет |
| game/chapters/1/script-ch1_1.rpy:583 | ch1 > if-цепочка | if | if choise_result == "bad" | 1) → продолжение после условия (fallthrough) | 1: -20@louise | — |
| game/chapters/1/script-ch1_1.rpy:628 | ch1 > if-цепочка | if | if choise_result == "good" | 1) → продолжение после условия (fallthrough) | 1: +20@louise | — |
| game/chapters/1/script-ch1_1.rpy:677 | ch1 > if-цепочка | if | if choise_result == "good" | 1) → продолжение после условия (fallthrough) | 1: нет | — |
| game/chapters/1/script-ch1_1.rpy:680 | ch1 > if-цепочка | if | if choise_result == "bad" | 1) → продолжение после условия (fallthrough) | 1: нет | — |
| game/chapters/1/script-ch1_2.rpy:85 | ch1_2 > menu | menu | нет | 1. Blame it on Louise → далее (после меню)<br>2. Try to cover it up yourself → далее (после меню)<br>3. Blame it on Siesta → далее (после меню) | 1: +20@louise<br>2: -20@louise<br>3: +20@siesta | скрытых условий у опций нет |
| game/chapters/1/script-ch1_3.rpy:10 | ch1_3 > sprite_choice | sprite_choice | нет | 1. Siesta's Room (siesta) → si_room_ch1_3<br>2. Louise's Room (louise) → l_room_ch1_3<br>3. Hallway (montmorency) → hallway_ch1_3 | si_room_ch1_3: +20@siesta, l_room_ch1_3: +20@louise; цели без симпатии: hallway_ch1_3 | инлайн-список dict{char,text,target}; цели достигаются renpy.call(target) (game/scripts/features/portrait_choises.rpy:218–220); условная симпатия целей — в строках их label/if |
| game/chapters/1/script-ch1_3.rpy:90 | si_room_ch1_3 > menu | menu | нет | 1. You might be right. → далее (после меню)<br>2. I doubt it's just a coincidence. → далее (после меню)<br>3. I don't really know. → далее (после меню) | 1: +20@siesta, -20@louise<br>2: нет<br>3: -20@siesta, +20@louise | скрытых условий у опций нет |
| game/chapters/1/script-ch1_3.rpy:239 | l_room_ch1_3 > menu | menu | нет | 1. Yeah, I want to go back. → далее (после меню)<br>2. I've already forgotten about my world. → далее (после меню)<br>3. I don't really know. → далее (после меню) | 1: нет<br>2: -20@louise<br>3: +20@louise | скрытых условий у опций нет |
| game/chapters/1/script-ch1_3.rpy:377 | hallway_ch1_3 > menu | menu | нет | 1. How did you know!? → далее (после меню)<br>2. Why do you think that? → далее (после меню)<br>3. Th-there's no way that's true, right? → далее (после меню) | 1: -20@louise<br>2: нет<br>3: +20@louise | скрытых условий у опций нет |
| game/chapters/1/script-ch1_5.rpy:89 | ch1_5 > menu | menu | нет | 1. Louise is just half-asleep! → далее (после меню)<br>2. We need a witness's testimony here! → далее (после меню)<br>3. I'll wake up Louise and let her explain… → далее (после меню) | 1: нет<br>2: +20@siesta, -20@louise<br>3: -20@siesta, +20@louise | скрытых условий у опций нет |
| game/chapters/1/script-ch1_5.rpy:234 | ch1_5 > if-цепочка | if | if result == "WAKE UP!"<br>else | 1) → продолжение после условия (fallthrough)<br>2) → продолжение после условия (fallthrough); (влож. if result == 'TESTIMONY!!!') | 1: нет<br>2: нет | — |
| game/chapters/1/script-ch1_5.rpy:258 | ch1_5 > if-цепочка | if | внутри: else (of result == "WAKE UP!")<br>if result == 'TESTIMONY!!!'<br>else | 1) → продолжение после условия (fallthrough)<br>2) → продолжение после условия (fallthrough) | 1: нет<br>2: нет | — |
| game/chapters/1/script-ch1_6.rpy:67 | ch1_6 > menu | menu | нет | 1. Ask Tabitha → далее (после меню)<br>2. Ask Siesta → далее (после меню)<br>3. Ask Louise → далее (после меню)<br>4. Ask Kirche → далее (после меню) | 1: -20@louise, +20@tabitha<br>2: -20@louise, +20@siesta<br>3: +20@louise<br>4: -20@louise, +20@kirche | скрытых условий у опций нет |
| game/chapters/1/script-ch1_6.rpy:433 | ch1_6 > menu | menu | нет | 1. Yeah. → далее (после меню)<br>2. Nope. → далее (после меню) | 1: +20@louise, -20@haruna, -20@siesta, -20@kirche<br>2: -20@louise, +20@haruna, +20@siesta, +20@kirche | скрытых условий у опций нет |
| game/chapters/1/script-ch1_7.rpy:123 | ch1_7 > menu | menu | нет | 1. Can't something be done, Headmaster? → далее (после меню)<br>2. What about Kirche's room? → далее (после меню)<br>3. You can come to my room. → далее (после меню) | 1: нет<br>2: -20@siesta<br>3: +20@siesta, -20@louise | скрытых условий у опций нет |
| game/chapters/1/script-ch1_8.rpy:115 | ch1_8 > sprite_choice | sprite_choice | нет | 1. Library (tabitha) → library_ch1_8<br>2. Kirche's Room (kirche) → k_room_ch1_8<br>3. Louise's Room (haruna) → l_room_ch1_8<br>4. Hallway → hallway_ch1_8 | library_ch1_8: +20@tabitha, k_room_ch1_8: +20@kirche, l_room_ch1_8: +20@haruna; цели без симпатии: hallway_ch1_8 | инлайн-список dict{char,text,target}; цели достигаются renpy.call(target) (game/scripts/features/portrait_choises.rpy:218–220); условная симпатия целей — в строках их label/if |
| game/chapters/1/script-ch1_8.rpy:168 | library_ch1_8 > menu | menu | нет | 1. See what's in the book → далее (после меню)<br>2. Snatch the book → далее (после меню)<br>3. Inquire about the book → далее (после меню) | 1: нет<br>2: -20@tabitha, +20@louise<br>3: +20@tabitha, -20@louise | скрытых условий у опций нет |
| game/chapters/1/script-ch1_8.rpy:347 | k_room_ch1_8 > menu | menu | нет | 1. Act like a gentleman and close my eyes. → далее (после меню)<br>2. Take this opportunity to get a good loo… → далее (после меню)<br>3. Scold her. → далее (после меню) | 1: нет<br>2: -20@louise, +20@kirche<br>3: +20@louise, -20@kirche | скрытых условий у опций нет |
| game/chapters/1/script-ch1_8.rpy:598 | l_room_ch1_8 > menu | menu | нет | 1. I thought I might clean the room a bit.… → далее (после меню)<br>2. Nothing special. → далее (после меню)<br>3. There's something I want to ask Haruna … → далее (после меню) | 1: +20@louise<br>2: -20@haruna<br>3: +20@haruna, -20@louise | скрытых условий у опций нет |
| game/chapters/1/script-ch1_9.rpy:83 | ch1_9 > menu | menu | нет | 1. Come on, can't something be done about … → далее (после меню)<br>2. Don't say such awful things! → далее (после меню) | 1: +20@louise<br>2: -20@louise | скрытых условий у опций нет |
| game/chapters/1/script-ch1_9.rpy:265 | ch1_9 > menu | menu | нет | 1. Isn't it possible that we overlooked so… → далее (после меню)<br>2. Was it by chance that she came to this … → далее (после меню) | 1: нет<br>2: нет | скрытых условий у опций нет |
| game/chapters/1/script-ch1_10.rpy:11 | ch1_10 > portrait_choice | portrait_choice | нет | 1. Go on a date with Louise (louise) → date_louise_1<br>2. Go on a date with Siesta (siesta) → date_siesta_1<br>3. Go on a date with Tabitha (tabitha) → date_tabitha_1<br>4. Go on a date with Kirche (kirche) → date_kirche_1<br>5. Go on a date with Haruna (haruna) → date_haruna_1 | нет | инлайн-список dict{char,text,target}; цели достигаются renpy.call(target) (game/scripts/features/portrait_choises.rpy:218–220); условная симпатия целей — в строках их label/if |
| game/chapters/1/script-ch1_10.rpy:25 | date_louise_1 > if-цепочка | route | if louise_sympathy == 100<br>else | 1) → call sp_l1<br>2) → call open_door; (влож. menu) | 1: нет<br>2: +20@louise, +20@louise (в опции меню), -20@louise (в опции меню) | — |
| game/chapters/1/script-ch1_10.rpy:77 | date_louise_1 > menu | date | внутри: else (of louise_sympathy == 100) | 1. You look really beautiful. → далее (после меню)<br>2. I don't really get it. → далее (после меню)<br>3. You don't seem like Louise. → далее (после меню) | 1: +20@louise<br>2: -20@louise<br>3: нет | скрытых условий у опций нет |
| game/chapters/1/script-ch1_10.rpy:174 | date_siesta_1 > if-цепочка | route | if louise_sympathy == 100<br>else | 1) → call sp_l1<br>2) → продолжение после условия (fallthrough); (влож. menu) | 1: нет<br>2: +20@siesta, +20@siesta (в опции меню), -20@siesta (в опции меню) | — |
| game/chapters/1/script-ch1_10.rpy:226 | date_siesta_1 > menu | date | внутри: else (of louise_sympathy == 100) | 1. You'll make an excellent wife. → далее (после меню)<br>2. Is that delicious? → далее (после меню)<br>3. So you're a thrifty person. → далее (после меню) | 1: +20@siesta<br>2: нет<br>3: -20@siesta | скрытых условий у опций нет |
| game/chapters/1/script-ch1_10.rpy:329 | date_tabitha_1 > if-цепочка | route | if louise_sympathy == 100<br>else | 1) → call sp_l1<br>2) → продолжение после условия (fallthrough); (влож. menu) | 1: нет<br>2: +20@tabitha, +20@tabitha (в опции меню), -20@tabitha (в опции меню) | — |
| game/chapters/1/script-ch1_10.rpy:381 | date_tabitha_1 > menu | date | внутри: else (of louise_sympathy == 100) | 1. Let me turn the pages for you. → далее (после меню)<br>2. Let me massage your shoulders. → далее (после меню)<br>3. Let me hold you. → далее (после меню) | 1: нет<br>2: +20@tabitha<br>3: -20@tabitha | скрытых условий у опций нет |
| game/chapters/1/script-ch1_10.rpy:567 | date_kirche_1 > if-цепочка | route | if louise_sympathy == 100<br>else | 1) → call sp_l1<br>2) → продолжение после условия (fallthrough); (влож. menu) | 1: нет<br>2: +20@kirche, +20@kirche (в опции меню), -20@kirche (в опции меню) | — |
| game/chapters/1/script-ch1_10.rpy:688 | date_kirche_1 > menu | date | внутри: else (of louise_sympathy == 100) | 1. What kind of men do you like? → далее (после меню)<br>2. What do you think of me? → далее (после меню)<br>3. Have you ever truly fallen in love with… → далее (после меню) | 1: нет<br>2: +20@kirche<br>3: -20@kirche | скрытых условий у опций нет |
| game/chapters/1/script-ch1_10.rpy:794 | date_haruna_1 > if-цепочка | route | if louise_sympathy == 100<br>else | 1) → call sp_l1<br>2) → продолжение после условия (fallthrough); (влож. menu) | 1: нет<br>2: +20@haruna, -20@haruna (в опции меню), +20@haruna (в опции меню) | — |
| game/chapters/1/script-ch1_10.rpy:862 | date_haruna_1 > menu | date | внутри: else (of louise_sympathy == 100) | 1. You were walking outside. → далее (после меню)<br>2. I don't know. → далее (после меню)<br>3. You were looking at the night sky. → далее (после меню) | 1: нет<br>2: -20@haruna<br>3: +20@haruna | скрытых условий у опций нет |

### Связность

Цепочка частей (межфайловые jump внутри главы): ch1_1 → ch1_2, ch1_2 → ch1_3, ch1_3 → ch1_4, ch1_4 → ch1_5, ch1_5 → ch1_6, ch1_6 → ch1_7, ch1_7 → ch1_8, ch1_8 → ch1_9, ch1_9 → ch1_10

Межфайловые переходы:

- `game/chapters/1/script-ch1_1.rpy:698` (`ch1`) → **jump** `ch1_2` → `game/chapters/1/script-ch1_2.rpy:2`
- `game/chapters/1/script-ch1_2.rpy:231` (`ch1_2`) → **jump** `ch1_3` → `game/chapters/1/script-ch1_3.rpy:2`
- `game/chapters/1/script-ch1_3.rpy:16` (`ch1_3`) → **jump** `ch1_4` → `game/chapters/1/script-ch1_4.rpy:2`
- `game/chapters/1/script-ch1_4.rpy:92` (`ch1_4`) → **jump** `ch1_5` → `game/chapters/1/script-ch1_5.rpy:2`
- `game/chapters/1/script-ch1_5.rpy:291` (`ch1_5`) → **jump** `ch1_6` → `game/chapters/1/script-ch1_6.rpy:2`
- `game/chapters/1/script-ch1_6.rpy:517` (`ch1_6`) → **jump** `ch1_7` → `game/chapters/1/script-ch1_7.rpy:2`
- `game/chapters/1/script-ch1_7.rpy:330` (`ch1_7`) → **jump** `ch1_8` → `game/chapters/1/script-ch1_8.rpy:2`
- `game/chapters/1/script-ch1_8.rpy:122` (`ch1_8`) → **jump** `ch1_9` → `game/chapters/1/script-ch1_9.rpy:2`
- `game/chapters/1/script-ch1_9.rpy:388` (`ch1_9`) → **jump** `ch1_10` → `game/chapters/1/script-ch1_10.rpy:2`

Выходы из главы (чужие главы / внешние лейблы, в т.ч. `jump attention`):

- `game/chapters/1/script-ch1_10.rpy:21` (`ch1_10`) → **jump** `ch2` → `game/chapters/2/script-ch2_1.rpy:3`

Вызываемые чужие/helper-лейблы (`call`):

- `game/chapters/1/script-ch1_1.rpy:25` (`ch1`) → **call** `overlay_screen` → `game/scripts/overlay/overlay_screen.rpy:71` ×3
- `game/chapters/1/script-ch1_10.rpy:26` (`date_louise_1`) → **call** `sp_l1` → `game/chapters/extra/sp_l1.rpy:2`
- `game/chapters/1/script-ch1_10.rpy:166` (`date_louise_1`) → **call** `open_door` → `game/scripts/features/helpers.rpy:6`
- `game/chapters/1/script-ch1_10.rpy:175` (`date_siesta_1`) → **call** `sp_l1` → `game/chapters/extra/sp_l1.rpy:2`
- `game/chapters/1/script-ch1_10.rpy:330` (`date_tabitha_1`) → **call** `sp_l1` → `game/chapters/extra/sp_l1.rpy:2`
- `game/chapters/1/script-ch1_10.rpy:568` (`date_kirche_1`) → **call** `sp_l1` → `game/chapters/extra/sp_l1.rpy:2`
- `game/chapters/1/script-ch1_10.rpy:795` (`date_haruna_1`) → **call** `sp_l1` → `game/chapters/extra/sp_l1.rpy:2`
- `game/chapters/1/script-ch1_2.rpy:3` (`ch1_2`) → **call** `overlay_screen` → `game/scripts/overlay/overlay_screen.rpy:71`
- `game/chapters/1/script-ch1_3.rpy:34` (`si_room_ch1_3`) → **call** `open_door` → `game/scripts/features/helpers.rpy:6` ×2
- `game/chapters/1/script-ch1_8.rpy:317` (`k_room_ch1_8`) → **call** `open_door` → `game/scripts/features/helpers.rpy:6` ×2

Динамические цели: экраны выбора (`ch1_3`, `ch1_8`, `ch1_10`) вызывают `renpy.call(target)` (`game/scripts/features/portrait_choises.rpy:218–220`) — целевые лейблы перечислены в колонке «варианты → цели» таблицы.

ВНИМАНИЕ: неразрешённые цели: game/chapters/1/script-ch1_1.rpy:4 call screen → battle_menu, game/chapters/1/script-ch1_1.rpy:11 call screen → battle_screen

## Глава 2 (game/chapters/2)

| файл:строка | лейбл/блок | тип | условие | варианты → цели | симпатия на ветках | примечание |
|---|---|---|---|---|---|---|
| game/chapters/2/script-ch2_1.rpy:87 | ch2 > menu | menu | нет | 1. Couldn't sleep because of an all-nighte… → далее (после меню)<br>2. Couldn't sleep because that female gues… → далее (после меню)<br>3. Couldn't sleep because she was keeping … → далее (после меню) | 1: нет<br>2: +10@louise<br>3: -10@louise | скрытых условий у опций нет |
| game/chapters/2/script-ch2_1.rpy:396 | ch2 > menu | menu | нет | 1. Shall we go catch him too? → jump ch2_2<br>2. I'd like to eat breakfast → jump ch2_2 | 1: -10@louise<br>2: нет | скрытых условий у опций нет |
| game/chapters/2/script-ch2_2.rpy:30 | ch2_2 > menu | menu | нет | 1. Going back to my room → jump hallway_ch2_2<br>2. Not going back to my room → jump hallway_ch2_2<br>3. What should I do... → jump hallway_ch2_2 | 1: -10@louise<br>2: +10@louise<br>3: нет | скрытых условий у опций нет |
| game/chapters/2/script-ch2_2.rpy:273 | l_room_ch2_2 > menu | menu | нет | 1. I was worried about Haruna → jump derf_ch2_2<br>2. I came to pick up something I forgot → jump derf_ch2_2 | 1: -10@siesta, -10@louise, +10@haruna<br>2: нет | скрытых условий у опций нет |
| game/chapters/2/script-ch2_2.rpy:433 | back_class_ch2_2 > menu | menu | нет | 1. I went to check on Haruna → jump ch2_3<br>2. I went to get Derflinger → jump ch2_3<br>3. I went to the toilet → jump ch2_3 | 1: -10@louise<br>2: +10@louise<br>3: нет | скрытых условий у опций нет |
| game/chapters/2/script-ch2_3.rpy:82 | ch2_3 > menu | menu | нет | 1. Stop it, Louise → jump ch2_3_battle<br>2. Stop it, Kirche → jump ch2_3_battle<br>3. Please stop them, Professor → jump ch2_3_battle | 1: +10@louise<br>2: +10@kirche<br>3: нет | скрытых условий у опций нет |
| game/chapters/2/script-ch2_3.rpy:444 | ch2_3_after > menu | menu | нет | 1. Louise, are you all right!? → jump ch2_4<br>2. Kirche, are you all right!? → jump ch2_4<br>3. Professor, are you all right!? → jump ch2_4 | 1: +10@louise<br>2: +10@kirche<br>3: -10@louise | скрытых условий у опций нет |
| game/chapters/2/script-ch2_4.rpy:132 | ch2_4_map > sprite_choice | sprite_choice | if "hallway" not in ch2_4_visited<br>if "kitchen" not in ch2_4_visited<br>if "yard" not in ch2_4_visited<br>if "classroom" not in ch2_4_visited<br>if "l_room" not in ch2_4_visited | 1. Hallway → hallway_ch2_4 [g1]<br>2. Kitchen → kitchen_ch2_4 [g2]<br>3. Courtyard → yard_ch2_4 [g3]<br>4. Classroom → classroom_ch2_4 [g4]<br>5. Louise's Room → l_room_ch2_4 [g5]<br>6. Leave → ch2_4_leave | hallway_ch2_4: +20@louise, kitchen_ch2_4: +20@siesta, yard_ch2_4: +20@kirche, classroom_ch2_4: +30@tabitha, l_room_ch2_4: +20@haruna; цели без симпатии: ch2_4_leave | [gN] → условие из этой же колонки (слиты if-цепочки антиповтора); хаб зациклен jump-ом; условная симпатия целей — в строках их label/if |
| game/chapters/2/script-ch2_4.rpy:213 | ch2_4_room > menu | menu | нет | 1. Did something happen, Louise? → jump ch2_4_dinner<br>2. Did something happen, Siesta? → jump ch2_4_dinner<br>3. How are you feeling, Haruna? → jump ch2_4_dinner | 1: +10@louise<br>2: -10@siesta<br>3: +10@haruna, -10@louise | скрытых условий у опций нет |
| game/chapters/2/script-ch2_4.rpy:455 | ch2_4_dinner > menu | menu | нет | 1. Do you want dinner too? → jump ch2_4_after<br>2. Do you want me to say 'ahh' for you too? → jump ch2_4_after<br>3. Do you want to be laid up in bed too? → jump ch2_4_after | 1: нет<br>2: +10@louise<br>3: -10@louise | скрытых условий у опций нет |
| game/chapters/2/script-ch2_4b.rpy:69 | hallway_ch2_4 > menu | menu | нет | 1. I know. → далее (после меню)<br>2. Don't worry about that. → далее (после меню)<br>3. Someday you'll be able to tell. → далее (после меню) | 1: +10@louise<br>2: -10@louise<br>3: нет | скрытых условий у опций нет |
| game/chapters/2/script-ch2_4b.rpy:229 | kitchen_ch2_4 > menu | menu | нет | 1. A suspicious person infiltrated. → далее (после меню)<br>2. That Louise did it again. → далее (после меню)<br>3. I don't know either. → далее (после меню) | 1: нет<br>2: +10@siesta<br>3: -10@siesta | скрытых условий у опций нет |
| game/chapters/2/script-ch2_4c.rpy:58 | yard_ch2_4 > menu | menu | нет | 1. I'd worry about anyone. → далее (после меню)<br>2. I'm worried because it's you, Kirche. → далее (после меню)<br>3. It's not like I'm worried about you. → далее (после меню) | 1: нет<br>2: +10@kirche<br>3: -10@kirche | скрытых условий у опций нет |
| game/chapters/2/script-ch2_4c.rpy:207 | classroom_ch2_4 > menu | menu | нет | 1. I was worried about Tabitha. → далее (после меню)<br>2. I was worried about everyone in the cla… → далее (после меню)<br>3. No particular reason. → далее (после меню) | 1: +15@tabitha<br>2: нет<br>3: -15@tabitha | скрытых условий у опций нет |
| game/chapters/2/script-ch2_4c.rpy:396 | l_room_ch2_4 > menu | menu | нет | 1. At least I'm glad you're safe, Haruna. → далее (после меню)<br>2. Make sure nobody else finds you. → далее (после меню)<br>3. Just stay put, okay? → далее (после меню) | 1: +10@haruna<br>2: нет<br>3: -10@haruna | скрытых условий у опций нет |
| game/chapters/2/script-ch2_5.rpy:66 | ch2_5 > menu | menu | нет | 1. Chase after Siesta → jump ch2_5_chase<br>2. Stay by Haruna's side → jump ch2_5_stay | 1: нет<br>2: нет | скрытых условий у опций нет |
| game/chapters/2/script-ch2_5.rpy:443 | ch2_5_map > sprite_choice | sprite_choice | if "l_room" not in ch2_5_visited<br>if "kirche_room" not in ch2_5_visited<br>if "tabitha_room" not in ch2_5_visited<br>if "corridor" not in ch2_5_visited | 1. Louise's Room → l_room_ch2_5 [g1]<br>2. Kirche's Room → kirche_room_ch2_5 [g2]<br>3. Tabitha's Room → tabitha_room_ch2_5 [g3]<br>4. Hallway → corridor_ch2_5 [g4]<br>5. Leave → ch2_5_leave | l_room_ch2_5: +20@haruna, kirche_room_ch2_5: +20@kirche, tabitha_room_ch2_5: +30@tabitha; цели без симпатии: corridor_ch2_5, ch2_5_leave | [gN] → условие из этой же колонки (слиты if-цепочки антиповтора); хаб зациклен jump-ом; условная симпатия целей — в строках их label/if |
| game/chapters/2/script-ch2_5b.rpy:46 | l_room_ch2_5 > menu | menu | нет | 1. Did I say something wrong? → далее (после меню)<br>2. Are you scared of being alone? → далее (после меню)<br>3. Does something hurt? → далее (после меню) | 1: -10@haruna<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/2/script-ch2_5b.rpy:195 | kirche_room_ch2_5 > menu | menu | нет | 1. I think I made her mad about Haruna. → далее (после меню)<br>2. It's Louise's usual tantrum. → далее (после меню)<br>3. I don't really know either. → далее (после меню) | 1: нет<br>2: нет<br>3: -10@kirche | скрытых условий у опций нет |
| game/chapters/2/script-ch2_5b.rpy:384 | tabitha_room_ch2_5 > menu | menu | нет | 1. What were you doing? → далее (после меню)<br>2. Why did you unlock the door? → далее (после меню)<br>3. Do you really not know where Louise is? → далее (после меню) | 1: +15@tabitha<br>2: нет<br>3: -15@tabitha | скрытых условий у опций нет |
| game/chapters/2/script-ch2_6.rpy:88 | ch2_6 > menu | menu | нет | 1. Did something happen to Louise? → jump ch2_6_night<br>2. What were you talking about earlier? → jump ch2_6_night<br>3. Could you take the dishes back? → jump ch2_6_night | 1: +10@siesta<br>2: -10@siesta<br>3: нет | скрытых условий у опций нет |
| game/chapters/2/script-ch2_6.rpy:221 | ch2_6_morning > portrait_choice | portrait_choice | нет | 1. Go on a date with Louise (louise) → date_louise_ch2_6<br>2. Go on a date with Siesta (siesta) → date_siesta_ch2_7<br>3. Go on a date with Tabitha (tabitha) → date_tabitha_ch2_7<br>4. Go on a date with Kirche (kirche) → date_kirche_ch2_8<br>5. Go on a date with Haruna (haruna) → date_haruna_ch2_8 | date_louise_ch2_6: +20@louise, date_siesta_ch2_7: +20@siesta, date_tabitha_ch2_7: +30@tabitha, date_kirche_ch2_8: +20@kirche, date_haruna_ch2_8: +20@haruna | инлайн-список dict{char,text,target}; цели достигаются renpy.call(target) (game/scripts/features/portrait_choises.rpy:218–220); условная симпатия целей — в строках их label/if |
| game/chapters/2/script-ch2_6.rpy:296 | date_louise_ch2_6 > menu | date | нет | 1. Bigger where, exactly? → jump date_louise_ch2_7<br>2. You don't have to push yourself. → jump date_louise_ch2_7<br>3. Give me some too. → jump date_louise_ch2_7 | 1: -10@louise<br>2: +10@louise<br>3: нет | скрытых условий у опций нет |
| game/chapters/2/script-ch2_7.rpy:58 | date_siesta_ch2_7 > menu | date | нет | 1. Nah, I'll pass. → jump ch2_7_siesta_refuse<br>2. Sounds like fun - let's do it. → jump ch2_7_siesta_join<br>3. I'll be in charge of tasting. → jump ch2_7_siesta_taste | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/2/script-ch2_7.rpy:302 | date_tabitha_ch2_7 > menu | date | нет | 1. Such days happen. → jump ch2_7_tabitha_1045<br>2. I'll buy you something. → jump ch2_7_tabitha_1046<br>3. Let's see more than just the bookstore. → jump ch2_8_tabitha_1047 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/2/script-ch2_8.rpy:111 | date_kirche_ch2_8 > menu | date | нет | 1. Fishing! → jump ch2_8_kirche_1050<br>2. Let's swim! → jump ch2_8_kirche_1051<br>3. An adventure in the shade! → jump ch2_8_kirche_1052 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/2/script-ch2_8.rpy:261 | date_haruna_ch2_8 > menu | date | нет | 1. A diary, of course. → jump ch2_8_haruna_1055<br>2. A student handbook. → jump ch2_8_haruna_1056<br>3. A letter from someone. → jump ch2_8_haruna_1057 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |

### Связность

Цепочка частей (межфайловые jump внутри главы): ch2_1 → ch2_2, ch2_2 → ch2_3, ch2_3 → ch2_4, ch2_4 → ch2_5, ch2_5 → ch2_6, ch2_6 → ch2_7, ch2_7 → ch2_8

Межфайловые переходы:

- `game/chapters/2/script-ch2_1.rpy:421` (`ch2`) → **jump** `ch2_2` → `game/chapters/2/script-ch2_2.rpy:5` ×2
- `game/chapters/2/script-ch2_2.rpy:484` (`back_class_ch2_2`) → **jump** `ch2_3` → `game/chapters/2/script-ch2_3.rpy:6` ×3
- `game/chapters/2/script-ch2_3.rpy:471` (`ch2_3_after`) → **jump** `ch2_4` → `game/chapters/2/script-ch2_4.rpy:9` ×3
- `game/chapters/2/script-ch2_4.rpy:611` (`ch2_4_after`) → **jump** `ch2_5` → `game/chapters/2/script-ch2_5.rpy:11`
- `game/chapters/2/script-ch2_5.rpy:448` (`ch2_5_leave`) → **jump** `ch2_6` → `game/chapters/2/script-ch2_6.rpy:10`
- `game/chapters/2/script-ch2_6.rpy:325` (`date_louise_ch2_6`) → **jump** `date_louise_ch2_7` → `game/chapters/2/script-ch2_7.rpy:8` ×3
- `game/chapters/2/script-ch2_7.rpy:308` (`date_tabitha_ch2_7`) → **jump** `ch2_8_tabitha_1047` → `game/chapters/2/script-ch2_8.rpy:10`
- `game/chapters/2/script-ch2_7.rpy:337` (`ch2_7_tabitha_1045`) → **jump** `ch2_8_tabitha_1048` → `game/chapters/2/script-ch2_8.rpy:35`
- `game/chapters/2/script-ch2_7.rpy:388` (`ch2_7_tabitha_1046`) → **jump** `ch2_8_tabitha_1048` → `game/chapters/2/script-ch2_8.rpy:35`

Выходы из главы (чужие главы / внешние лейблы, в т.ч. `jump attention`):

- `game/chapters/2/script-ch2_6.rpy:231` (`ch2_6_morning`) → **jump** `ch3` → `game/chapters/3/script-ch3_1.rpy:4`

Вызываемые чужие/helper-лейблы (`call`):

- `game/chapters/2/script-ch2_1.rpy:4` (`ch2`) → **call** `overlay_screen` → `game/scripts/overlay/overlay_screen.rpy:71`
- `game/chapters/2/script-ch2_1.rpy:328` (`ch2`) → **call** `open_door` → `game/scripts/features/helpers.rpy:6`
- `game/chapters/2/script-ch2_2.rpy:161` (`l_room_ch2_2`) → **call** `open_door` → `game/scripts/features/helpers.rpy:6`
- `game/chapters/2/script-ch2_2.rpy:402` (`derf_ch2_2`) → **call** `open_door` → `game/scripts/features/helpers.rpy:6`
- `game/chapters/2/script-ch2_4.rpy:155` (`ch2_4_room`) → **call** `open_door` → `game/scripts/features/helpers.rpy:6`
- `game/chapters/2/script-ch2_6.rpy:26` (`ch2_6`) → **call** `open_door` → `game/scripts/features/helpers.rpy:6`
- `game/chapters/2/script-ch2_8.rpy:73` (`date_kirche_ch2_8`) → **call** `open_door` → `game/scripts/features/helpers.rpy:6`

Динамические цели: экраны выбора (`ch2_4`, `ch2_5`, `ch2_6`) вызывают `renpy.call(target)` (`game/scripts/features/portrait_choises.rpy:218–220`) — целевые лейблы перечислены в колонке «варианты → цели» таблицы (локации карт-хабов лежат в отдельных частях, напр. `script-ch2_4b/c.rpy`).

## Глава 3 (game/chapters/3)

| файл:строка | лейбл/блок | тип | условие | варианты → цели | симпатия на ветках | примечание |
|---|---|---|---|---|---|---|
| game/chapters/3/script-ch3_1.rpy:96 | ch3 > menu | menu | нет | 1. I didn't think it was a bother. → jump ch3_141<br>2. Now that you mention it, it might be cr… → jump ch3_141<br>3. How about the four of us sleep together? → jump ch3_141 | 1: нет<br>2: нет<br>3: -10@louise, -10@siesta, -10@haruna | скрытых условий у опций нет |
| game/chapters/3/script-ch3_1.rpy:371 | ch3_141 > menu | menu | нет | 1. Probably Louise. → jump ch3_146<br>2. Maybe Siesta? → jump ch3_146<br>3. Maybe Haruna? → jump ch3_146 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_2.rpy:102 | ch3_2 > menu | menu | нет | 1. Are you feeling under the weather? → jump ch3_151<br>2. Are you sleepy? → jump ch3_151<br>3. Are you hungry? → jump ch3_151 | 1: +10@louise<br>2: -10@louise<br>3: -20@louise | скрытых условий у опций нет |
| game/chapters/3/script-ch3_2.rpy:383 | ch3_153 > menu | menu | нет | 1. Well, she's probably fine, right? → jump ch3_157<br>2. I'm a little worried, I guess. → jump ch3_157<br>3. Yeah, it does bug me. → jump ch3_157 | 1: +10@louise<br>2: -10@louise<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_2.rpy:541 | ch3_2_map > sprite_choice | sprite_choice | if "hallway" not in ch3_2_visited<br>if "siesta_hallway" not in ch3_2_visited<br>if "classroom" not in ch3_2_visited<br>if "courtyard" not in ch3_2_visited<br>if "l_room" not in ch3_2_visited | 1. Hallway → hallway_ch3_3 [g1]<br>2. Hallway → siesta_hallway_ch3_3 [g2]<br>3. Classroom → classroom_ch3_3 [g3]<br>4. Courtyard → courtyard_ch3_3 [g4]<br>5. Louise's Room → l_room_ch3_3 [g5]<br>6. Leave → ch3_2_leave | hallway_ch3_3: +20@louise, siesta_hallway_ch3_3: +20@siesta, classroom_ch3_3: +20@kirche, courtyard_ch3_3: +30@tabitha, l_room_ch3_3: +20@haruna; цели без симпатии: ch3_2_leave | [gN] → условие из этой же колонки (слиты if-цепочки антиповтора); хаб зациклен jump-ом; условная симпатия целей — в строках их label/if |
| game/chapters/3/script-ch3_3.rpy:69 | hallway_ch3_3 > menu | menu | нет | 1. Did I do something? → jump ch3_1301<br>2. Am I in the way? → jump ch3_1301<br>3. Are you going to take a bath? → jump ch3_1301 | 1: -10@louise<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_3.rpy:216 | siesta_hallway_ch3_3 > menu | menu | нет | 1. Luggage I'm not allowed to touch? → jump ch3_1306<br>2. Did I do something to offend you? → jump ch3_1306<br>3. Are you working out or something? → jump ch3_1306 | 1: -10@siesta<br>2: +10@siesta<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_3.rpy:433 | classroom_ch3_3 > menu | menu | нет | 1. Louise, one way or another? → jump ch3_1311<br>2. Siesta directly? → jump ch3_1311<br>3. Kirche, by any chance? → jump ch3_1311 | 1: +10@kirche<br>2: нет<br>3: -10@kirche | скрытых условий у опций нет |
| game/chapters/3/script-ch3_3.rpy:641 | courtyard_ch3_3 > menu | menu | нет | 1. Do you hate me? → jump ch3_1316<br>2. Have you really not seen Louise? → jump ch3_1316<br>3. Are you busy reading? → jump ch3_1316 | 1: +15@tabitha<br>2: -15@tabitha<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_3.rpy:842 | l_room_ch3_3 > menu | menu | нет | 1. Don't hold back with me. → jump ch3_1321<br>2. You need to rest up now, okay? → jump ch3_1321<br>3. If you've got something to say, say it. → jump ch3_1321 | 1: +10@haruna<br>2: нет<br>3: -10@haruna | скрытых условий у опций нет |
| game/chapters/3/script-ch3_4.rpy:185 | ch3_4 > menu | menu | нет | 1. Are you okay, Haruna? → jump ch3_4_168<br>2. Siesta, you okay? → jump ch3_4_168<br>3. ...Louise!? → jump ch3_4_168 | 1: +10@haruna<br>2: +10@siesta<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_4.rpy:460 | ch3_4_168 > menu | menu | нет | 1. It was Louise who started it, right? → jump ch3_5_169<br>2. This isn't like the usual Siesta. → jump ch3_5_170<br>3. Do you dislike Haruna? → jump ch3_5_171 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_5.rpy:233 | ch3_5_173 > menu | menu | нет | 1. Is it wrong of me to look after Haruna? → jump ch3_5_174<br>2. You didn't need to worry about her. → jump ch3_5_175<br>3. I'm just saying something objective. → jump ch3_5_176 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_5.rpy:494 | ch3_5_178 > menu | menu | нет | 1. Louise's room → jump ch3_5_1322<br>2. Kirche's room → jump ch3_5_1327<br>3. Tabitha's room → jump ch3_5_1332<br>4. The kitchen → jump ch3_5_1337 | 1: нет<br>2: нет<br>3: нет<br>4: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_5.rpy:561 | ch3_5_1322 > menu | menu | нет | 1. Was it because Haruna took over your ro… → jump ch3_5_1323<br>2. Actually, maybe it was Louise and Siest… → jump ch3_5_1324<br>3. Hmm, I have no idea. → jump ch3_5_1325 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_5.rpy:727 | ch3_5_1327 > menu | menu | нет | 1. Yes, I'd love to. → jump ch3_5_1328<br>2. Once things calm down, sure. → jump ch3_5_1329<br>3. I'll make time to visit. → jump ch3_5_1330 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_5.rpy:857 | ch3_5_1332 > menu | menu | нет | 1. It's not like I need her for anything. → jump ch3_5_1333<br>2. I wanted to ask her about Haruna. → jump ch3_5_1334<br>3. Sorry. I can't tell you, Monmon. → jump ch3_5_1335 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_5.rpy:1015 | ch3_5_1337 > menu | menu | нет | 1. I wanted to consult you about Haruna. → jump ch3_5_1338<br>2. No, never mind. → jump ch3_5_1339<br>3. Yeah, I just need her for something. → jump ch3_5_1340 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_6.rpy:92 | ch3_6 > menu | menu | нет | 1. Do you need Louise for something? → jump ch3_6_187<br>2. Or did you come to see Haruna? → jump ch3_6_187<br>3. Don't tell me you came to see me? → jump ch3_6_187 | 1: нет<br>2: нет<br>3: +10@kirche | скрытых условий у опций нет |
| game/chapters/3/script-ch3_6.rpy:275 | ch3_6_187 > menu | menu | нет | 1. I'd never think that! → jump ch3_6_191<br>2. It's not about breasts or not… → jump ch3_6_191<br>3. I don't judge people by their breasts. → jump ch3_6_191 | 1: -10@louise<br>2: +10@kirche, -10@louise, -10@siesta, -10@haruna<br>3: +10@kirche | скрытых условий у опций нет |
| game/chapters/3/script-ch3_6.rpy:477 | ch3_6_192 > menu | menu | нет | 1. They won't listen to me anyway. → jump ch3_7_193<br>2. Girls shouldn't be dueling. → jump ch3_7_194<br>3. Why not let them go until both are sati… → jump ch3_7_195 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_7.rpy:371 | ch3_7_197 > menu | menu | нет | 1. Sorry — that's a bit of a shock… → jump ch3_7_201<br>2. I'm just glad you weren't really sick → jump ch3_7_201<br>3. You don't have to worry about me → jump ch3_7_201 | 1: -10@haruna<br>2: +10@haruna<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_7.rpy:560 | ch3_7_202 > menu | menu | нет | 1. Why not just apologize honestly? → jump ch3_7_206<br>2. You don't have to apologize → jump ch3_7_206<br>3. How about treating them to sweets somet… → jump ch3_7_206 | 1: +10@haruna<br>2: -10@haruna<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_8.rpy:106 | ch3_8 > menu | menu | нет | 1. …I just want to protect her. → jump ch3_8_208<br>2. …I want to believe her unconditionally. → jump ch3_8_209<br>3. …it kind of sends a chill down my spine. → jump ch3_8_210 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_8.rpy:410 | ch3_8_213 > portrait_choice | portrait_choice | нет | 1. Go on a date with Louise (louise) → date_louise_ch3_8<br>2. Go on a date with Siesta (siesta) → date_siesta_ch3_9<br>3. Go on a date with Tabitha (tabitha) → date_tabitha_ch3_9<br>4. Go on a date with Kirche (kirche) → date_kirche_ch3_9<br>5. Go on a date with Haruna (haruna) → date_haruna_ch3_9 | date_louise_ch3_8: +20@louise, date_siesta_ch3_9: +20@siesta, date_tabitha_ch3_9: +30@tabitha, date_kirche_ch3_9: +20@kirche, date_haruna_ch3_9: +20@haruna | инлайн-список dict{char,text,target}; цели достигаются renpy.call(target) (game/scripts/features/portrait_choises.rpy:218–220); условная симпатия целей — в строках их label/if |
| game/chapters/3/script-ch3_8.rpy:514 | date_louise_ch3_8 > menu | date | нет | 1. Peel an apple for her. → jump ch3_8_l_1060<br>2. Wipe her down. → jump ch3_8_l_1061<br>3. Tell her a story. → jump ch3_8_l_1062 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_9.rpy:87 | date_siesta_ch3_9 > menu | date | нет | 1. Is that a pair look? → jump ch3_9_si_1065<br>2. Some skill, huh. → jump ch3_9_si_1066<br>3. Wouldn't a different pattern be better? → jump ch3_9_si_1067 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_9.rpy:257 | date_tabitha_ch3_9 > menu | date | нет | 1. I'm a familiar too, y'know! → jump ch3_9_t_1070<br>2. I can't explain it — I just know. → jump ch3_9_t_1071<br>3. It's written on your face. → jump ch3_9_t_1072 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_9.rpy:419 | date_kirche_ch3_9 > menu | date | нет | 1. Because you're an exhibitionist? → jump ch3_9_k_1075<br>2. To let off steam? → jump ch3_9_k_1076<br>3. Some wish to become someone else? → jump ch3_9_k_1077 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/3/script-ch3_9.rpy:635 | date_haruna_ch3_9 > menu | date | нет | 1. That can't be helped. → jump ch3_9_ha_1080<br>2. Maybe we just don't know. → jump ch3_9_ha_1081<br>3. We'll be the first to return. → jump ch3_9_ha_1082 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |

### Связность

Цепочка частей (межфайловые jump внутри главы): ch3_1 → ch3_2, ch3_2 → ch3_4, ch3_4 → ch3_5, ch3_5 → ch3_6, ch3_6 → ch3_7, ch3_7 → ch3_8

Межфайловые переходы:

- `game/chapters/3/script-ch3_1.rpy:473` (`ch3_146`) → **jump** `ch3_2` → `game/chapters/3/script-ch3_2.rpy:14`
- `game/chapters/3/script-ch3_2.rpy:546` (`ch3_2_leave`) → **jump** `ch3_4` → `game/chapters/3/script-ch3_4.rpy:7`
- `game/chapters/3/script-ch3_4.rpy:462` (`ch3_4_168`) → **jump** `ch3_5_169` → `game/chapters/3/script-ch3_5.rpy:13`
- `game/chapters/3/script-ch3_4.rpy:465` (`ch3_4_168`) → **jump** `ch3_5_170` → `game/chapters/3/script-ch3_5.rpy:50`
- `game/chapters/3/script-ch3_4.rpy:468` (`ch3_4_168`) → **jump** `ch3_5_171` → `game/chapters/3/script-ch3_5.rpy:88`
- `game/chapters/3/script-ch3_5.rpy:692` (`ch3_5_1326`) → **jump** `ch3_6` → `game/chapters/3/script-ch3_6.rpy:17`
- `game/chapters/3/script-ch3_5.rpy:818` (`ch3_5_1331`) → **jump** `ch3_6` → `game/chapters/3/script-ch3_6.rpy:17`
- `game/chapters/3/script-ch3_5.rpy:972` (`ch3_5_1336`) → **jump** `ch3_6` → `game/chapters/3/script-ch3_6.rpy:17`
- `game/chapters/3/script-ch3_5.rpy:1146` (`ch3_5_1341`) → **jump** `ch3_6` → `game/chapters/3/script-ch3_6.rpy:17`
- `game/chapters/3/script-ch3_6.rpy:479` (`ch3_6_192`) → **jump** `ch3_7_193` → `game/chapters/3/script-ch3_7.rpy:17`
- `game/chapters/3/script-ch3_6.rpy:482` (`ch3_6_192`) → **jump** `ch3_7_194` → `game/chapters/3/script-ch3_7.rpy:97`
- `game/chapters/3/script-ch3_6.rpy:485` (`ch3_6_192`) → **jump** `ch3_7_195` → `game/chapters/3/script-ch3_7.rpy:150`
- `game/chapters/3/script-ch3_7.rpy:748` (`ch3_7_206`) → **jump** `ch3_8` → `game/chapters/3/script-ch3_8.rpy:21`

Выходы из главы (чужие главы / внешние лейблы, в т.ч. `jump attention`):

- `game/chapters/3/script-ch3_8.rpy:420` (`ch3_8_213`) → **jump** `ch4` → `game/chapters/4/script-ch4_1.rpy:16`

Вызываемые чужие/helper-лейблы (`call`):

- `game/chapters/3/script-ch3_1.rpy:5` (`ch3`) → **call** `overlay_screen` → `game/scripts/overlay/overlay_screen.rpy:71`

Динамические цели: экраны выбора (`ch3_2`, `ch3_8`) вызывают `renpy.call(target)` (`game/scripts/features/portrait_choises.rpy:218–220`) — целевые лейблы перечислены в колонке «варианты → цели» таблицы (локации карт-хабов лежат в отдельных частях, напр. `script-ch2_4b/c.rpy`).

## Глава 4 (game/chapters/4)

| файл:строка | лейбл/блок | тип | условие | варианты → цели | симпатия на ветках | примечание |
|---|---|---|---|---|---|---|
| game/chapters/4/script-ch4_1.rpy:321 | ch4 > menu | menu | нет | 1. It was an accident. → jump ch4_1_220<br>2. Louise was the one who… → jump ch4_1_221<br>3. Actually, it was me… → jump ch4_1_222 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_2.rpy:311 | ch4_2_map > sprite_choice | sprite_choice | if "louise_room" not in ch4_2_visited<br>if "kitchen" not in ch4_2_visited<br>if "yard" not in ch4_2_visited<br>if "hallway" not in ch4_2_visited<br>if "h_room" not in ch4_2_visited | 1. Louise's Room → date_louise_ch4_2 [g1]<br>2. Kitchen → date_siesta_ch4_2 [g2]<br>3. Courtyard → date_kirche_ch4_2 [g3]<br>4. Hallway → date_tabitha_ch4_2 [g4]<br>5. Louise's Room → date_haruna_ch4_2 [g5]<br>6. Leave → ch4_2_leave | date_louise_ch4_2: +20@louise, date_siesta_ch4_2: +20@siesta, date_kirche_ch4_2: +20@kirche, date_tabitha_ch4_2: +30@tabitha, date_haruna_ch4_2: +20@haruna; цели без симпатии: ch4_2_leave | [gN] → условие из этой же колонки (слиты if-цепочки антиповтора); хаб зациклен jump-ом; условная симпатия целей — в строках их label/if |
| game/chapters/4/script-ch4_2.rpy:359 | date_louise_ch4_2 > menu | date | нет | 1. Give her a hand. → jump ch4_2_l_1343<br>2. I don't want to help. → jump ch4_2_l_1344<br>3. Offer to help, on one condition. → jump ch4_2_l_1345 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_2.rpy:660 | ch4_2_231 > menu | menu | нет | 1. Sit next to Louise. → jump ch4_2_232<br>2. Sit next to Haruna. → jump ch4_2_233<br>3. Waver over which seat. → jump ch4_2_234 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_2b.rpy:53 | date_siesta_ch4_2 > menu | date | нет | 1. Tell her it's a dangerous mission. → jump ch4_2b_siesta_1348<br>2. Tell her I'll bring back a souvenir. → jump ch4_2b_siesta_1349<br>3. Tell her it's absolutely out of the que… → jump ch4_2b_siesta_1350 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_2b.rpy:261 | date_kirche_ch4_2 > menu | date | нет | 1. There are reasons I can't tell you. → jump ch4_2b_kirche_1353<br>2. I'm taking Haruna sightseeing. → jump ch4_2b_kirche_1354<br>3. The headmaster asked me to run an erran… → jump ch4_2b_kirche_1355 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_2b.rpy:429 | date_tabitha_ch4_2 > menu | date | нет | 1. A book about noble life? → jump ch4_2b_tabitha_1358<br>2. A book about Tabitha's family? → jump ch4_2b_tabitha_1359<br>3. A book with some kind of story? → jump ch4_2b_tabitha_1360 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_2b.rpy:661 | date_haruna_ch4_2 > menu | date | нет | 1. It really suits you. → jump ch4_2b_haruna_1363<br>2. I'd like some new clothes too. → jump ch4_2b_haruna_1364<br>3. Clothes make the man, as they say. → jump ch4_2b_haruna_1365 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_3.rpy:256 | ch4_3 > menu | menu | нет | 1. Say she's my little sister. → jump ch4_3_237<br>2. Say she's Louise's maid. → jump ch4_3_238<br>3. I think we should just tell the truth. → jump ch4_3_239 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_3.rpy:503 | ch4_3_241 > menu | menu | нет | 1. Ask her to handle the class journal too. → jump ch4_3_242<br>2. Say you feel unwell and go to the infir… → jump ch4_3_243<br>3. What day of the week was it again? → jump ch4_3_244 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_4.rpy:146 | ch4_4_247 > menu | menu | нет | 1. We're right here with you. → jump ch4_4_248<br>2. Louise will track down the way back. → jump ch4_4_249<br>3. Someday, somehow, it'll all work out. → jump ch4_4_250 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_4.rpy:351 | ch4_4_map > sprite_choice | sprite_choice | if "store" not in ch4_4_visited<br>if "apothecary" not in ch4_4_visited<br>if "stroll" not in ch4_4_visited<br>if "street" not in ch4_4_visited | 1. Main Street → date_haruna_ch4_4 [g1]<br>2. Main Street → date_louise_ch4_4 [g2]<br>3. Main Street → date_siesta_ch4_4 [g3]<br>4. Main Street → date_street_ch4_4 [g4]<br>5. Leave → ch4_4_leave | date_haruna_ch4_4: +20@haruna, date_louise_ch4_4: +20@louise, date_siesta_ch4_4: +20@siesta; цели без симпатии: date_street_ch4_4, ch4_4_leave | [gN] → условие из этой же колонки (слиты if-цепочки антиповтора); хаб зациклен jump-ом; условная симпатия целей — в строках их label/if |
| game/chapters/4/script-ch4_4.rpy:475 | date_haruna_ch4_4 > menu | date | нет | 1. The red fruit that looks like a tomato. → jump ch4_4_haruna_1368<br>2. The green fruit that looks like a cucum… → jump ch4_4_haruna_1369<br>3. The yellow fruit that looks like a lemo… → jump ch4_4_haruna_1370 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_4.rpy:689 | date_louise_ch4_4 > menu | date | нет | 1. A love potion? → jump ch4_4_louise_1373<br>2. A cold medicine? → jump ch4_4_louise_1374<br>3. A cough medicine? → jump ch4_4_louise_1375 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_4.rpy:974 | date_siesta_ch4_4 > menu | date | нет | 1. It's a big city. → jump ch4_4_siesta_1378<br>2. It's smaller than I expected. → jump ch4_4_siesta_1379<br>3. What do you think, Siesta? → jump ch4_4_siesta_1380 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_5.rpy:437 | ch4_5 > menu | menu | нет | 1. The Bomb User isn't Louise. → jump ch4_5_257<br>2. The Bomb User is Louise. → jump ch4_5_258<br>3. Is there other information? → jump ch4_5_259 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_6.rpy:659 | ch4_6 > portrait_choice | portrait_choice | нет | 1. Go on a date with Louise (louise) → date_louise_ch4_6<br>2. Go on a date with Siesta (siesta) → date_siesta_ch4_6<br>3. Go on a date with Haruna (haruna) → date_haruna_ch4_6<br>4. Go on a date with Henrietta (henrietta) → date_henrietta_ch4_6 | date_louise_ch4_6: +20@louise, date_siesta_ch4_6: +20@siesta, +10@siesta, -10@siesta, date_haruna_ch4_6: +20@haruna, +10@haruna, -10@haruna, date_henrietta_ch4_6: +50@henrietta, +30@henrietta, -30@henrietta | инлайн-список dict{char,text,target}; цели достигаются renpy.call(target) (game/scripts/features/portrait_choises.rpy:218–220); условная симпатия целей — в строках их label/if |
| game/chapters/4/script-ch4_6.rpy:746 | date_louise_ch4_6 > menu | date | нет | 1. She really is hardworking, isn't she? → далее (после меню)<br>2. Why not try doing it without relying on… → далее (после меню)<br>3. Why not ask Tabitha about it? → далее (после меню) | 1: +10@louise<br>2: нет<br>3: -10@louise | скрытых условий у опций нет |
| game/chapters/4/script-ch4_6.rpy:1021 | date_siesta_ch4_6 > menu | date | нет | 1. That's not true at all. → далее (после меню) | 1: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_6.rpy:1300 | date_haruna_ch4_6 > menu | date | нет | 1. Japanese songs, I guess. → далее (после меню) | 1: нет | скрытых условий у опций нет |
| game/chapters/4/script-ch4_6.rpy:1659 | date_henrietta_ch4_6 > menu | date | нет | 1. I'm on the princess's side. → далее (после меню) | 1: нет | скрытых условий у опций нет |

### Связность

Цепочка частей (межфайловые jump внутри главы): ch4_1 → ch4_2, ch4_2 → ch4_3, ch4_3 → ch4_4, ch4_4 → ch4_5, ch4_5 → ch4_6

Межфайловые переходы:

- `game/chapters/4/script-ch4_1.rpy:742` (`ch4_1_224`) → **jump** `ch4_2` → `game/chapters/4/script-ch4_2.rpy:22`
- `game/chapters/4/script-ch4_2.rpy:897` (`ch4_2_235`) → **jump** `ch4_3` → `game/chapters/4/script-ch4_3.rpy:33`
- `game/chapters/4/script-ch4_3.rpy:690` (`ch4_3_245`) → **jump** `ch4_4` → `game/chapters/4/script-ch4_4.rpy:47`
- `game/chapters/4/script-ch4_4.rpy:358` (`ch4_4_leave`) → **jump** `ch4_5` → `game/chapters/4/script-ch4_5.rpy:32`
- `game/chapters/4/script-ch4_5.rpy:661` (`ch4_5_260`) → **jump** `ch4_6` → `game/chapters/4/script-ch4_6.rpy:47`

Выходы из главы (чужие главы / внешние лейблы, в т.ч. `jump attention`):

- `game/chapters/4/script-ch4_6.rpy:671` (`ch4_6`) → **jump** `ch5` → `game/chapters/5/script-ch5_1.rpy:40`

Вызываемые чужие/helper-лейблы (`call`):

- `game/chapters/4/script-ch4_1.rpy:17` (`ch4`) → **call** `overlay_screen` → `game/scripts/overlay/overlay_screen.rpy:71`
- `game/chapters/4/script-ch4_4.rpy:94` (`ch4_4_247`) → **call** `overlay_screen` → `game/scripts/overlay/overlay_screen.rpy:71`

Динамические цели: экраны выбора (`ch4_2`, `ch4_4`, `ch4_6`) вызывают `renpy.call(target)` (`game/scripts/features/portrait_choises.rpy:218–220`) — целевые лейблы перечислены в колонке «варианты → цели» таблицы (локации карт-хабов лежат в отдельных частях, напр. `script-ch2_4b/c.rpy`).

## Глава 5 (game/chapters/5)

| файл:строка | лейбл/блок | тип | условие | варианты → цели | симпатия на ветках | примечание |
|---|---|---|---|---|---|---|
| game/chapters/5/script-ch5_1.rpy:170 | ch5 > menu | menu | нет | 1. It's nothing, nothing at all. → далее (после меню)<br>2. Let me tell you something, though. → далее (после меню)<br>3. I'm not making a sour face at all. → далее (после меню) | 1: -10@louise<br>2: нет<br>3: -10@louise | скрытых условий у опций нет |
| game/chapters/5/script-ch5_1.rpy:493 | ch5 > menu | menu | нет | 1. Is Haruna all right? → далее (после меню)<br>2. Is Louise all right? → далее (после меню)<br>3. Is Siesta all right? → далее (после меню) | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_1.rpy:842 | ch5 > menu | menu | нет | 1. Watch over her. → далее (после меню)<br>2. Offer to help. → далее (после меню)<br>3. Tell Haruna to give up. → далее (после меню) | 1: нет<br>2: нет<br>3: -10@haruna | скрытых условий у опций нет |
| game/chapters/5/script-ch5_2.rpy:182 | ch5_2 > menu | menu | нет | 1. I'm coming along too. → далее (после меню)<br>2. Take care of yourself. → далее (после меню)<br>3. What if Siesta came along? → далее (после меню) | 1: +10@haruna<br>2: -10@haruna<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_2.rpy:399 | ch5_2 > menu | menu | нет | 1. Ask Kirche. → далее (после меню)<br>2. Give it up. → далее (после меню)<br>3. Break the door down. → далее (после меню) | 1: +10@kirche<br>2: -10@haruna<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_2.rpy:693 | ch5_2 > menu | menu | нет | 1. We came to talk about it again. → далее (после меню)<br>2. W-we came looking for something we lost. → далее (после меню)<br>3. S-stay silent. → далее (после меню) | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_3.rpy:144 | ch5_3 > menu | menu | нет | 1. Persuade Siesta → далее (после меню)<br>2. Persuade Louise → далее (после меню)<br>3. Persuade Kirche → далее (после меню) | 1: -10@siesta<br>2: -10@louise<br>3: -10@kirche | скрытых условий у опций нет |
| game/chapters/5/script-ch5_3.rpy:612 | ch5_3 > menu | menu | нет | 1. S-so, exactly → далее (после меню)<br>2. That's just how it is… → далее (после меню)<br>3. Are you sure it's all right? → далее (после меню) | 1: нет<br>2: +30@henrietta<br>3: +30@henrietta | скрытых условий у опций нет |
| game/chapters/5/script-ch5_3.rpy:819 | ch5_3 > menu | menu | нет | 1. Stop Kirche → далее (после меню)<br>2. Stop Montmorency → далее (после меню)<br>3. Don't chase after those who leave → далее (после меню) | 1: +15@tabitha<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_4.rpy:163 | ch5_4_a > menu | menu | нет | 1. That's not true! → далее (после меню)<br>2. Well, you're right. → далее (после меню)<br>3. It's no use telling me that. → далее (после меню) | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_4.rpy:358 | ch5_4_b > menu | menu | нет | 1. I wonder what book she's reading? → далее (после меню)<br>2. It'd be rude to disturb her → далее (после меню)<br>3. Let me play a prank → далее (после меню) | 1: нет<br>2: +15@tabitha<br>3: -15@tabitha | скрытых условий у опций нет |
| game/chapters/5/script-ch5_4.rpy:625 | ch5_4_c > menu | menu | нет | 1. A girl's value isn't in her dancing! → далее (после меню)<br>2. Why don't you ask Louise? → далее (после меню)<br>3. Haruna has her own good points! → далее (после меню) | 1: -10@louise<br>2: нет<br>3: +10@haruna | скрытых условий у опций нет |
| game/chapters/5/script-ch5_4.rpy:837 | ch5_4_d > menu | menu | нет | 1. A-a bother, you say… → далее (после меню)<br>2. Hey, come back to rehearsal → далее (после меню)<br>3. I want to slack off too, but… → далее (после меню) | 1: нет<br>2: +10@kirche<br>3: -10@kirche | скрытых условий у опций нет |
| game/chapters/5/script-ch5_4.rpy:1037 | ch5_4_e > menu | menu | нет | 1. It's just your imagination → далее (после меню)<br>2. Don't worry about it! → далее (после меню)<br>3. It's always like that, isn't it? → далее (после меню) | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_5.rpy:270 | ch5_5 > menu | menu | нет | 1. What a horrible story → далее (после меню)<br>2. It's a good story → далее (после меню)<br>3. I don't get it → далее (после меню) | 1: -10@louise, -10@siesta<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_5.rpy:512 | ch5_5 > menu | menu | нет | 1. I'm glad! → далее (после меню)<br>2. Don't underestimate us! → далее (после меню)<br>3. Could my role be swapped too? → далее (после меню) | 1: +10@kirche, -10@louise<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_5.rpy:728 | ch5_5 > menu | menu | нет | 1. Looking for the bomb user? → далее (после меню)<br>2. Kirche's birthday? → далее (после меню)<br>3. My dance footwork? → далее (после меню) | 1: +10@kirche<br>2: -10@kirche<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_6.rpy:86 | ch5_6 > menu | menu | нет | 1. To the theater (stage) → далее (после меню) | 1: +20@kirche, +10@kirche, -10@kirche, -10@haruna | скрытых условий у опций нет |
| game/chapters/5/script-ch5_6.rpy:144 | ch5_6 > menu | menu | внутри: menu; opt "To the theater (stage)" | 1. I was worried about Kirche. → далее (после меню)<br>2. I wasn't worried at all. → далее (после меню)<br>3. Was that so? → далее (после меню) | 1: нет<br>2: +10@kirche<br>3: -10@kirche, -10@haruna | скрытых условий у опций нет |
| game/chapters/5/script-ch5_6.rpy:332 | ch5_6 > menu | menu | внутри: menu; opt "To the auditorium" | 1. Confront Guiche → далее (после меню)<br>2. Confront Louise → далее (после меню)<br>3. Throw a rock → далее (после меню) | 1: +10@louise<br>2: нет<br>3: -10@louise | скрытых условий у опций нет |
| game/chapters/5/script-ch5_6.rpy:613 | ch5_6 > menu | menu | внутри: menu; opt "To the main street" | 1. I'd love to try Montmon's cooking → далее (после меню)<br>2. What's your specialty? → далее (после меню)<br>3. Can you actually make something edible? → далее (после меню) | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_6.rpy:892 | ch5_6 > menu | menu | внутри: menu; opt "To the inn" | 1. Topic: the weather → далее (после меню)<br>2. Topic: the familiar → далее (после меню)<br>3. Topic: books → далее (после меню) | 1: нет<br>2: нет<br>3: +15@tabitha, +30@henrietta | скрытых условий у опций нет |
| game/chapters/5/script-ch5_7.rpy:64 | ch5_7 > if-цепочка | route | if zero_route == 1<br>elif zero_route == 2<br>elif zero_route == 3<br>elif zero_route == 4<br>elif zero_route == 5<br>else | 1) → jump ch5_7_r1_louise<br>2) → jump ch5_8_r2_kirche<br>3) → jump ch5_8_r3_tabitha<br>4) → jump ch5_7_r4_siesta<br>5) → jump ch5_9_r5_henrietta<br>6) → jump ch5_9_r6_haruna | 1: нет<br>2: нет<br>3: нет<br>4: нет<br>5: нет<br>6: нет | — |
| game/chapters/5/script-ch5_7.rpy:204 | ch5_7_r1_louise > menu | menu | нет | 1. I meant it... → jump ch5_7_r1_rejoin<br>2. It was only a play! → jump ch5_7_r1_rejoin<br>3. Change the subject → jump ch5_7_r1_rejoin | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_7.rpy:380 | ch5_7_r4_siesta > menu | menu | нет | 1. Maybe I was serious? → jump ch5_7_r4_rejoin<br>2. It was only acting! → jump ch5_7_r4_rejoin<br>3. Laugh it off → jump ch5_7_r4_rejoin | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_8.rpy:108 | ch5_8_kirche_play > menu | menu | нет | 1. Maybe I really meant it… → далее (после меню)<br>2. It was only a play! → далее (после меню)<br>3. Laugh it off → далее (после меню) | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_8.rpy:242 | ch5_8_tabitha_play > menu | menu | нет | 1. Maybe I really meant it → далее (после меню)<br>2. It was only a play! → далее (после меню)<br>3. Laugh it off → далее (после меню) | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_9.rpy:5 | ch5_9 > if-цепочка | route | if zero_route == 5<br>else | 1) → jump ch5_9_r5_henrietta<br>2) → jump ch5_9_r6_haruna | 1: нет<br>2: нет | — |
| game/chapters/5/script-ch5_9.rpy:97 | ch5_9_r6_haruna > menu | menu | нет | 1. I really meant it. → jump ch5_9_r6_haruna_1155<br>2. It was only a play! → jump ch5_9_r6_haruna_1156<br>3. Laugh it off → jump ch5_9_r6_haruna_1157 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_9.rpy:245 | ch5_9_r5_henrietta > menu | menu | нет | 1. I really meant it. → jump ch5_9_r5_henrietta_1160<br>2. I am sorry. → jump ch5_9_r5_henrietta_1161<br>3. Laugh it off → jump ch5_9_r5_henrietta_1162 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_10.rpy:50 | ch5_10_date_menu > if-цепочка | route | if zero_route == 1<br>elif zero_route == 2<br>elif zero_route == 3<br>elif zero_route == 4<br>elif zero_route == 5<br>else | 1) → jump ch5_10_date_louise<br>2) → jump ch5_10_date_kirche<br>3) → jump ch5_11_date_tabitha<br>4) → jump ch5_10_date_siesta<br>5) → jump ch5_11_date_henrietta<br>6) → jump ch5_11_date_haruna | 1: нет<br>2: нет<br>3: нет<br>4: нет<br>5: нет<br>6: нет | — |
| game/chapters/5/script-ch5_10.rpy:102 | ch5_10_date_louise > menu | date | нет | 1. You look prettier than usual. → jump ch5_11_date_louise_1105<br>2. You look the same as always. → jump ch5_11_date_louise_1106<br>3. Does the dress fit you? → jump ch5_11_date_louise_1107 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_10.rpy:165 | ch5_10_date_siesta > menu | date | нет | 1. I want to go home… → jump ch5_11_date_siesta_1110<br>2. I want to eat hamburgers… → jump ch5_11_date_siesta_1111<br>3. Do you have any other food stories? → jump ch5_11_date_siesta_1112 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_10.rpy:234 | ch5_10_date_kirche > menu | date | нет | 1. Resist. → jump ch5_11_date_kirche_1115<br>2. Yes. → jump ch5_11_date_kirche_1116<br>3. No. → jump ch5_11_date_kirche_1117 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_11.rpy:80 | ch5_11_date_tabitha > menu | date | нет | 1. I do not know. → jump ch5_11_date_tabitha_1120<br>2. I meant all of it! → jump ch5_11_date_tabitha_1121<br>3. What about you, Tabitha? → jump ch5_11_date_tabitha_1122 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_11.rpy:192 | ch5_11_date_haruna > menu | date | нет | 1. A picture of a pet? → jump ch5_11_date_haruna_1125<br>2. A picture of her boyfriend? → jump ch5_11_date_haruna_1126<br>3. A picture of me? → jump ch5_11_date_haruna_1127 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_11.rpy:293 | ch5_11_date_henrietta > menu | date | нет | 1. I meant it. → jump ch5_11_date_henrietta_1130<br>2. It was not just acting. → jump ch5_11_date_henrietta_1131<br>3. I do not know. → jump ch5_11_date_henrietta_1132 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/5/script-ch5_11.rpy:363 | ch5_11_scene_343 > if-цепочка | route | if zero_route == 1<br>elif zero_route == 2<br>elif zero_route == 3<br>elif zero_route == 4<br>elif zero_route == 5<br>else | 1) → jump attention<br>2) → jump attention<br>3) → jump attention<br>4) → jump attention<br>5) → jump attention<br>6) → jump attention | 1: нет<br>2: нет<br>3: нет<br>4: нет<br>5: нет<br>6: нет | WARNING Z2: все ветки ведут в attention |

### Связность

Цепочка частей (межфайловые jump внутри главы): ch5_1 → ch5_2, ch5_2 → ch5_3, ch5_3 → ch5_4, ch5_4 → ch5_5, ch5_5 → ch5_6, ch5_6 → ch5_7, ch5_7 → ch5_8, ch5_7 → ch5_9, ch5_7 → ch5_10, ch5_8 → ch5_9, ch5_9 → ch5_10, ch5_10 → ch5_11

Межфайловые переходы:

- `game/chapters/5/script-ch5_1.rpy:996` (`ch5`) → **jump** `ch5_2` → `game/chapters/5/script-ch5_2.rpy:28`
- `game/chapters/5/script-ch5_10.rpy:55` (`ch5_10_date_menu`) → **jump** `ch5_11_date_tabitha` → `game/chapters/5/script-ch5_11.rpy:5`
- `game/chapters/5/script-ch5_10.rpy:59` (`ch5_10_date_menu`) → **jump** `ch5_11_date_henrietta` → `game/chapters/5/script-ch5_11.rpy:256`
- `game/chapters/5/script-ch5_10.rpy:61` (`ch5_10_date_menu`) → **jump** `ch5_11_date_haruna` → `game/chapters/5/script-ch5_11.rpy:149`
- `game/chapters/5/script-ch5_10.rpy:104` (`ch5_10_date_louise`) → **jump** `ch5_11_date_louise_1105` → `game/chapters/5/script-ch5_11.rpy:376`
- `game/chapters/5/script-ch5_10.rpy:106` (`ch5_10_date_louise`) → **jump** `ch5_11_date_louise_1106` → `game/chapters/5/script-ch5_11.rpy:386`
- `game/chapters/5/script-ch5_10.rpy:108` (`ch5_10_date_louise`) → **jump** `ch5_11_date_louise_1107` → `game/chapters/5/script-ch5_11.rpy:396`
- `game/chapters/5/script-ch5_10.rpy:167` (`ch5_10_date_siesta`) → **jump** `ch5_11_date_siesta_1110` → `game/chapters/5/script-ch5_11.rpy:424`
- `game/chapters/5/script-ch5_10.rpy:169` (`ch5_10_date_siesta`) → **jump** `ch5_11_date_siesta_1111` → `game/chapters/5/script-ch5_11.rpy:438`
- `game/chapters/5/script-ch5_10.rpy:171` (`ch5_10_date_siesta`) → **jump** `ch5_11_date_siesta_1112` → `game/chapters/5/script-ch5_11.rpy:454`
- `game/chapters/5/script-ch5_10.rpy:236` (`ch5_10_date_kirche`) → **jump** `ch5_11_date_kirche_1115` → `game/chapters/5/script-ch5_11.rpy:475`
- `game/chapters/5/script-ch5_10.rpy:238` (`ch5_10_date_kirche`) → **jump** `ch5_11_date_kirche_1116` → `game/chapters/5/script-ch5_11.rpy:489`
- `game/chapters/5/script-ch5_10.rpy:240` (`ch5_10_date_kirche`) → **jump** `ch5_11_date_kirche_1117` → `game/chapters/5/script-ch5_11.rpy:501`
- `game/chapters/5/script-ch5_2.rpy:1023` (`ch5_2`) → **jump** `ch5_3` → `game/chapters/5/script-ch5_3.rpy:28`
- `game/chapters/5/script-ch5_3.rpy:988` (`ch5_3`) → **jump** `ch5_4` → `game/chapters/5/script-ch5_4.rpy:36`
- `game/chapters/5/script-ch5_3.rpy:1010` (`ch5_3_sc309`) → **jump** `ch5_4` → `game/chapters/5/script-ch5_4.rpy:36`
- `game/chapters/5/script-ch5_4.rpy:117` (`ch5_4`) → **jump** `ch5_5` → `game/chapters/5/script-ch5_5.rpy:30`
- `game/chapters/5/script-ch5_5.rpy:899` (`ch5_5`) → **jump** `ch5_6` → `game/chapters/5/script-ch5_6.rpy:50`
- `game/chapters/5/script-ch5_6.rpy:1189` (`ch5_6`) → **jump** `ch5_7` → `game/chapters/5/script-ch5_7.rpy:4`
- `game/chapters/5/script-ch5_7.rpy:67` (`ch5_7`) → **jump** `ch5_8_r2_kirche` → `game/chapters/5/script-ch5_8.rpy:4`
- `game/chapters/5/script-ch5_7.rpy:69` (`ch5_7`) → **jump** `ch5_8_r3_tabitha` → `game/chapters/5/script-ch5_8.rpy:136`
- `game/chapters/5/script-ch5_7.rpy:73` (`ch5_7`) → **jump** `ch5_9_r5_henrietta` → `game/chapters/5/script-ch5_9.rpy:142`
- `game/chapters/5/script-ch5_7.rpy:75` (`ch5_7`) → **jump** `ch5_9_r6_haruna` → `game/chapters/5/script-ch5_9.rpy:10`
- `game/chapters/5/script-ch5_7.rpy:251` (`ch5_7_r1_rejoin`) → **jump** `ch5_10` → `game/chapters/5/script-ch5_10.rpy:6`
- `game/chapters/5/script-ch5_7.rpy:431` (`ch5_7_r4_rejoin`) → **jump** `ch5_10` → `game/chapters/5/script-ch5_10.rpy:6`
- `game/chapters/5/script-ch5_8.rpy:134` (`ch5_8_r2_end`) → **jump** `ch5_9` → `game/chapters/5/script-ch5_9.rpy:4`
- `game/chapters/5/script-ch5_8.rpy:275` (`ch5_8_r3_end`) → **jump** `ch5_9` → `game/chapters/5/script-ch5_9.rpy:4`
- `game/chapters/5/script-ch5_9.rpy:141` (`ch5_9_r6_haruna_1158`) → **jump** `ch5_10` → `game/chapters/5/script-ch5_10.rpy:6`
- `game/chapters/5/script-ch5_9.rpy:291` (`ch5_9_r5_henrietta_1163`) → **jump** `ch5_10` → `game/chapters/5/script-ch5_10.rpy:6`

Выходы из главы (чужие главы / внешние лейблы, в т.ч. `jump attention`):

- `game/chapters/5/script-ch5_11.rpy:364` (`ch5_11_scene_343`) → **jump** `attention` → `game/chapters/attention.rpy:1` ×6

Вызываемые чужие/helper-лейблы (`call`):

- `game/chapters/5/script-ch5_1.rpy:42` (`ch5`) → **call** `overlay_screen` → `game/scripts/overlay/overlay_screen.rpy:71`

## Глава 6 (game/chapters/6)

| файл:строка | лейбл/блок | тип | условие | варианты → цели | симпатия на ветках | примечание |
|---|---|---|---|---|---|---|
| game/chapters/6/script-ch6_1.rpy:101 | ch6 > menu | menu | нет | 1. The princess!? → jump ch6_s345<br>2. The innkeeper's voice changed!? → jump ch6_s346<br>3. Who is Miss ‘It-is-I’!? → jump ch6_s347 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/6/script-ch6_1.rpy:259 | ch6_s349 > menu | menu | нет | 1. The culprit was a craftsman who went on… → jump ch6_s350<br>2. The bombings were meant to lure enemy a… → jump ch6_s351<br>3. Just a bombing fanatic → jump ch6_s352 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/6/script-ch6_1.rpy:477 | ch6_s355 > menu | menu | нет | 1. In front of the castle → jump ch6_s1429<br>2. Down a back street → jump ch6_s1434<br>3. Along the highway → jump ch6_s1439<br>4. On the main street → jump ch6_s1444 | 1: нет<br>2: нет<br>3: нет<br>4: нет | скрытых условий у опций нет |
| game/chapters/6/script-ch6_1.rpy:519 | ch6_s1429 > menu | menu | нет | 1. What about my cousin? → jump ch6_s1430<br>2. What about my sister-in-law? → jump ch6_s1431<br>3. What about my fiancée? → jump ch6_s1432 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/6/script-ch6_1.rpy:625 | ch6_s1434 > menu | menu | нет | 1. A girl like Kirche → jump ch6_s1435<br>2. Someone like me → jump ch6_s1436<br>3. No girl should come here → jump ch6_s1437 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/6/script-ch6_1.rpy:731 | ch6_s1439 > menu | menu | нет | 1. Someday, you will be able to go whereve… → jump ch6_s1440<br>2. You must not run away → jump ch6_s1441<br>3. It is dangerous to lose your way → jump ch6_s1442 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/6/script-ch6_1.rpy:834 | ch6_s1444 > menu | menu | нет | 1. Even if it was coincidence, isn't it en… → jump ch6_s1445<br>2. Our efforts were not a coincidence → jump ch6_s1446<br>3. It will be all right next time → jump ch6_s1447 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/6/script-ch6_2.rpy:59 | ch6_2 > menu | menu | нет | 1. Don't let it get to you → jump ch6_2_s361<br>2. What matters is what you do from here on → jump ch6_2_s362<br>3. There are all kinds of people → jump ch6_2_s363 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/6/script-ch6_2.rpy:185 | ch6_2_s365 > menu | menu | нет | 1. A world without kings → jump ch6_2_s366<br>2. A world without magic → jump ch6_2_s367<br>3. A world without night → jump ch6_2_s368 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/6/script-ch6_2.rpy:310 | ch6_2_s370 > menu | menu | нет | 1. It wasn't my fault! → jump ch6_2_s371<br>2. I have no regrets about my date with th… → jump ch6_2_s372<br>3. I went to see how things were in town... → jump ch6_2_s373 | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |

### Связность

Цепочка частей (межфайловые jump внутри главы): ch6_1 → ch6_2

Межфайловые переходы:

- `game/chapters/6/script-ch6_1.rpy:916` (`ch6_s1448`) → **jump** `ch6_2` → `game/chapters/6/script-ch6_2.rpy:5`

Выходы из главы (чужие главы / внешние лейблы, в т.ч. `jump attention`):

- `game/chapters/6/script-ch6_2.rpy:366` (`ch6_2_s374`) → **jump** `attention` → `game/chapters/attention.rpy:1`

## Extra (game/chapters/extra)

### Точки вызова sp_l1 (все способы вызова)

В проекте `sp_l1` вызывается только через `call sp_l1 from _call_sp_l1_N`; `jump sp_l1` и ссылок из других мест нет (проверено по всем `game/**/*.rpy` и `references/`). Все 5 точек — в `game/chapters/1/script-ch1_10.rpy`, каждая — в ветке `if louise_sympathy == 100`:

| файл:строка | лейбл/блок | тип | условие | варианты → цели | симпатия на ветках | примечание |
|---|---|---|---|---|---|---|
| game/chapters/1/script-ch1_10.rpy:26 | date_louise_1 > if louise_sympathy == 100 | extra | if louise_sympathy == 100 | if-ветка → call `sp_l1` (`game/chapters/extra/sp_l1.rpy:2`); другая ветка: → call open_door; (влож. menu) | if-ветка: нет (до вызова); другая ветка: +20@louise, +20@louise (в опции меню), -20@louise (в опции меню) | условие из цепочки `game/chapters/1/script-ch1_10.rpy:25`; раскладка другой ветки — строка route той же главы |
| game/chapters/1/script-ch1_10.rpy:175 | date_siesta_1 > if louise_sympathy == 100 | extra | if louise_sympathy == 100 | if-ветка → call `sp_l1` (`game/chapters/extra/sp_l1.rpy:2`); другая ветка: → продолжение после условия (fallthrough); (влож. menu) | if-ветка: нет (до вызова); другая ветка: +20@siesta, +20@siesta (в опции меню), -20@siesta (в опции меню) | условие из цепочки `game/chapters/1/script-ch1_10.rpy:174`; раскладка другой ветки — строка route той же главы |
| game/chapters/1/script-ch1_10.rpy:330 | date_tabitha_1 > if louise_sympathy == 100 | extra | if louise_sympathy == 100 | if-ветка → call `sp_l1` (`game/chapters/extra/sp_l1.rpy:2`); другая ветка: → продолжение после условия (fallthrough); (влож. menu) | if-ветка: нет (до вызова); другая ветка: +20@tabitha, +20@tabitha (в опции меню), -20@tabitha (в опции меню) | условие из цепочки `game/chapters/1/script-ch1_10.rpy:329`; раскладка другой ветки — строка route той же главы |
| game/chapters/1/script-ch1_10.rpy:568 | date_kirche_1 > if louise_sympathy == 100 | extra | if louise_sympathy == 100 | if-ветка → call `sp_l1` (`game/chapters/extra/sp_l1.rpy:2`); другая ветка: → продолжение после условия (fallthrough); (влож. menu) | if-ветка: нет (до вызова); другая ветка: +20@kirche, +20@kirche (в опции меню), -20@kirche (в опции меню) | условие из цепочки `game/chapters/1/script-ch1_10.rpy:567`; раскладка другой ветки — строка route той же главы |
| game/chapters/1/script-ch1_10.rpy:795 | date_haruna_1 > if louise_sympathy == 100 | extra | if louise_sympathy == 100 | if-ветка → call `sp_l1` (`game/chapters/extra/sp_l1.rpy:2`); другая ветка: → продолжение после условия (fallthrough); (влож. menu) | if-ветка: нет (до вызова); другая ветка: +20@haruna, -20@haruna (в опции меню), +20@haruna (в опции меню) | условие из цепочки `game/chapters/1/script-ch1_10.rpy:794`; раскладка другой ветки — строка route той же главы |

### Связность

Вход: только 5 `call sp_l1` из главы 1 (таблица выше). Выход из extra-сцены: явного `return` в файле нет — см. Замечания Z7.

Внешние вызовы из extra:

- `game/chapters/extra/sp_l1.rpy:3` (`sp_l1`) → **call** `overlay_screen` → `game/scripts/overlay/overlay_screen.rpy:71`

### Файлы extra

| файл:строка | лейбл/блок | тип | условие | варианты → цели | симпатия на ветках | примечание |
|---|---|---|---|---|---|---|
| game/chapters/extra/sp_l1.rpy:17 | sp_l1 > menu | menu | нет | 1. Looks like I'm actually getting hungry.… → далее (после меню)<br>2. Yep! Starving, totally starving!! → далее (после меню)<br>3. Not hungry one bit. → далее (после меню) | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |
| game/chapters/extra/sp_l1.rpy:160 | sp_l1 > menu | menu | нет | 1. Is this some kind of punishment game? → далее (после меню)<br>2. Ahh... → далее (после меню)<br>3. Does this have poison in it or somethin… → далее (после меню) | 1: нет<br>2: нет<br>3: нет | скрытых условий у опций нет |

`sp_l1.rpy`: 283 строк, `label sp_l1` на строке 2; возвратов `return`: **нет**. Прочие конструкции (voice/реплики/эффекты) ветвлением не являются.

## Замечания

Метка: `???` — вопрос человеку; `WARNING` — требует внимания. Classification — природа места после расследования, disposition — судьба находки. Правки в скриптах не выполнялись (объём S2 — инвентаризация).

| # | метка | место | расследование (факты) | classification | disposition |
|---|---|---|---|---|---|
| Z1 | ??? | `game/chapters/6/script-ch6_1.rpy:6` (`label ch6`) | `jump ch6` / `call ch6` в `game/**` отсутствуют (скан регуляркой `^(jump|call)\s+ch6\s*$` по всем *.rpy — 0 совпадений): вход в главу 6 не написан. `reports/translation_plan.md:333` — «Вход: jump ch6 из главы 5» — незакрытый пункт. Глава 5 заканчивается `jump attention` (Z2), поэтому глава 6 из сюжетной линии недостижима. | WARNING | ??? |
| Z2 | WARNING | `game/chapters/5/script-ch5_11.rpy:363–374` (`label ch5_11_scene_343`) | Диспетчер `zero_route`: 5 условий `zero_route == 1..5` + `else` = 6 веток, и **все** ведут `jump attention` (программная сверка: да). Финиш главы 5 не переходит в главу 6 — связано с Z1. | WARNING | ??? |
| Z3 | WARNING | `game/chapters/1/script-ch1_1.rpy:3` (`label forest_battle`), if-цепочки :6, :13, вызов :467 | Лейбл недостижим: `call forest_battle` закомментирован. Внутри — `call screen battle_menu` и `battle_screen`, но эти экраны нигде не определены (в `game/scripts/battle/battle_screens.rpy` есть только `battle_prep:55` и `battle_hud:175`) — при включении ветки была бы ошибка. Боевая система не реализована (AGENTS.md §6); ветка сохранена как мёртвый код. | WARNING | ACCEPTABLE ADAPTATION |
| Z4 | WARNING | `game/chapters/5/script-ch5_3.rpy:990` (`label ch5_3_sc309`) | Недостижима в потоке сцен, но это задокументировано комментарием самого лейбла: сцена 309 — «переход» движка PS2, ветки 306–308 ведут сразу в 310, текста нет. | PASS | ACCEPTABLE ADAPTATION |
| Z5 | WARNING | `game/chapters/5/script-ch5_6.rpy:18` (комментарий «ЗАДОЛЖЕННОСТЬ (E7)») | Комментарий утверждает, что `jump ch5_7` ведёт в «не портированную» часть 7 — устарел: `script-ch5_7.rpy` существует, `jump ch5_7` разрешается, проверка синтаксиса главы 5 проходит. Правка комментария в S2 не выполнялась (scripts не редактируются). | WARNING | USER DECISION |
| Z6 | PASS | `game/chapters/5/script-ch5_4.rpy:54, :69, :84, :99, :114` | Пять безусловных `call ch5_4_a…e` подряд — расследовано: это extra-блоки `【移動】`, каждый завершается `return`, последовательность повторяет поток сцен 315–319; решение зафиксировано в `reports/log.md:3614-3615`. PS2-вызов `if(isJump())` не портируется (отмечено комментарием в коде). | PASS | ACCEPTABLE ADAPTATION |
| Z7 | ??? | `game/chapters/extra/sp_l1.rpy` (283 строк) | В файле **нет ни одного `return`** (программный скан: 0). Последняя выполняемая строка — `$ show_sprites(None, anim_out="slide_right")`. Все 5 точек входа — через `call sp_l1`, то есть после сцены исполнение доходит до конца файла внутри звонка; поведение Ren'Py в этом случае (возврат по завершении программы или выход из игры) нужно проверить рантаймом. | WARNING | ??? |
| Z8 | WARNING | Leave-цели пяти карт-хабов: `ch2_4_leave:136` → `game/chapters/2/script-ch2_4.rpy:137 jump ch2_4_room`; `ch2_5_leave:447` → `game/chapters/2/script-ch2_5.rpy:448 jump ch2_6`; `ch3_2_leave:545` → `game/chapters/3/script-ch3_2.rpy:546 jump ch3_4`; `ch4_2_leave:316` → `game/chapters/4/script-ch4_2.rpy:317 jump ch4_2_231`; `ch4_4_leave:356` → `game/chapters/4/script-ch4_4.rpy:358 jump ch4_5` | Экран выполняет `renpy.call(target)` (`portrait_choises.rpy:218–220`), но leave-лейблы завершаются `jump`, а не `return` — фрейм звонка не закрывается; за прохождение копится до 5 висячих фреймов (по одному на хаб). Локации напротив возвращаются `return`, цикл хаба работает. Нужна проверка рантаймом (глубина стека звонков). | WARNING | ??? |
| Z9 | PASS | `game/chapters/1/script-ch1_1.rpy:162–163` | `else:` → строка-заглушка `"ERR"` в цепочке `choise_result` (меню :124–130 задаёт good/neutral/bad, все покрыты) — фактически недостижима, оставлена как отладочная заглушка. | PASS | PRESERVED — FUNCTIONAL |
| Z10 | PASS | `game/chapters/1/script-ch1_2.rpy:84` (`$ result = None`) | Запись без чтения в этом файле: чтения `result ==` только в `game/chapters/1/script-ch1_5.rpy:234`, `game/chapters/1/script-ch1_5.rpy:258`; присвоения `result`: сама эта строка и `game/chapters/1/script-ch1_5.rpy:88`, `game/chapters/1/script-ch1_5.rpy:116`, `game/chapters/1/script-ch1_5.rpy:191`. Безвредная инициализация перед menu; не трогаем («не переписывать без нужды»). | PASS | PRESERVED — FUNCTIONAL |
| Z11 | WARNING | недостижимые `return` после безусловного `jump` (23 мест) | Программный скан всех файлов 0–6+extra: game/chapters/1/script-ch1_1.rpy:700 (после `jump ch1_2`); game/chapters/1/script-ch1_2.rpy:232 (после `jump ch1_3`); game/chapters/1/script-ch1_3.rpy:17 (после `jump ch1_4`); game/chapters/1/script-ch1_4.rpy:94 (после `jump ch1_5`); game/chapters/1/script-ch1_5.rpy:292 (после `jump ch1_6`); game/chapters/1/script-ch1_6.rpy:518 (после `jump ch1_7`); game/chapters/1/script-ch1_7.rpy:331 (после `jump ch1_8`); game/chapters/1/script-ch1_8.rpy:123 (после `jump ch1_9`); game/chapters/1/script-ch1_9.rpy:389 (после `jump ch1_10`); game/chapters/1/script-ch1_10.rpy:22 (после `jump ch2`); game/chapters/2/script-ch2_1.rpy:457 (после `jump ch2_2`); game/chapters/2/script-ch2_2.rpy:574 (после `jump ch2_3`); game/chapters/2/script-ch2_4.rpy:117 (после `jump ch2_4_map`); game/chapters/2/script-ch2_4.rpy:134 (после `jump ch2_4_map`); game/chapters/2/script-ch2_5.rpy:445 (после `jump ch2_5_map`); game/chapters/3/script-ch3_2.rpy:543 (после `jump ch3_2_map`); game/chapters/4/script-ch4_2.rpy:313 (после `jump ch4_2_map`); game/chapters/4/script-ch4_4.rpy:353 (после `jump ch4_4_map`); game/chapters/4/script-ch4_6.rpy:672 (после `jump ch5`); game/chapters/5/script-ch5_1.rpy:997 (после `jump ch5_2`); game/chapters/5/script-ch5_2.rpy:1024 (после `jump ch5_3`); game/chapters/5/script-ch5_3.rpy:1011 (после `jump ch5_4`); game/chapters/5/script-ch5_4.rpy:118 (после `jump ch5_5`) — хвосты-защитники: `jump` безусловный, `return` после него никогда не выполнится. Распространённый паттерн концов частей и карт-хабов. | PASS | PRESERVED — FUNCTIONAL |

## Проверки

1. **Синтаксис Ren'Py**: прогнан `python tools/check_renpy_syntax.py --chapter N` для N = 0, 1, 2, 3, 4, 5, 6 — все 7 запусков → код возврата 0; `reports/check_renpy_syntax.md` (2026-10-31 04:32): «OK — проблем не найдено.»
2. **Факт по заданию — `if louise_sympathy == 100`**: ровно **5** (программный подсчёт): `game/chapters/1/script-ch1_10.rpy:25`, `game/chapters/1/script-ch1_10.rpy:174`, `game/chapters/1/script-ch1_10.rpy:329`, `game/chapters/1/script-ch1_10.rpy:567`, `game/chapters/1/script-ch1_10.rpy:794`. Все — `route`-строки в `script-ch1_10.rpy`, каждая с веткой `call sp_l1` + `else`.
3. **Факт по заданию — диспетчеры `zero_route`** (ветвей по факту, программный подсчёт):

| файл:строка | лейбл | условий `zero_route ==` | веток (условия + else) |
|---|---|---|---|
| `game/chapters/5/script-ch5_7.rpy:64` | `ch5_7` | 5 | **6** |
| `game/chapters/5/script-ch5_10.rpy:50` | `ch5_10_date_menu` | 5 | **6** |
| `game/chapters/5/script-ch5_11.rpy:363` | `ch5_11_scene_343` | 5 | **6** |
| `game/chapters/5/script-ch5_9.rpy:5` | `ch5_9` | 1 | **2** |

   Итог: `ch5_7`, `ch5_10_date_menu`, `ch5_11_scene_343` — по **6** веток (5 условий + `else`), как требует задание; `ch5_9` — 2 ветки (справочно, в списке задания не значился).
4. **Объём инвентаря** (программный подсчёт по извлечению): menu — 137; choice-экранов — 11 (`sprite_choice` 7 + `portrait_choice` 4); событий if/elif/else — 74 в 43 if-цепочках, из них 23 цепочек-гардов (`not in *_visited`) слиты в строки хабов, if/route-строк в таблицах — 20; jump — 482; call — 38; update_sympathy — 292; label — 375; межфайловых рёбер связности — 118; неразрешённых целей — 2.
5. **Строки таблиц по типам** (фактически в отчёте): date — 33, extra — 5, if — 11, jump — 1, menu — 104, portrait_choice — 4, route — 9, sprite_choice — 7.
6. **Скрипты не изменялись**: отчёт собран только чтением `*.rpy`; git-коммит не выполняется (протокол S2, маркер — `S2.result.md`).
7. Границы объёма: сверка симпатий с JA-источником (`ps2_source/`) и полнота переноса PS2-веток — другие подзадачи (S1/S3); здесь только инвентаризация портированного кода.
