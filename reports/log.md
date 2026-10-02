# Журнал решений (reports/log.md)

Общий журнал проекта. **Дополняется, не переписывается.** Сюда попадают:
PROVISIONAL-решения (термины, обращения, формы), `RECONCILE` (расхождения EN ↔ RU при
обоих допустимых по JA вариантах), `OPEN`/`DEFERRED` (отложенные вопросы), `???`
(нужно решение человека), отклонения от источника, заметки по гигиене репозитория.

Формат записи:

```markdown
## YYYY-MM-DD — <короткий заголовок>
- статус: PROVISIONAL | RECONCILE | OPEN | DEFERRED | USER DECISION | INFO
- место: `<файл>` / глава N, часть M
- вопрос: ...
- решение/вариант: ...
- где использовано: ...
```

---

## 2026-10-02 — настройка среды под агентов

- статус: INFO
- место: корень проекта
- Решения:
  - единая инструкция — `AGENTS.md`; разовые брифы структуры/порта удалены, их
    содержание перенесено в `AGENTS.md` и скиллы `.agents/skills/`;
  - расшифрованные скрипты PS2 перенесены из `D:\gameMake\ZnT-1\ZNT_TEST\output`
    в `D:\gameMake\ZnT-1\ZnT1\ps2_source` (2097 файлов, 17,4 МБ);
  - отчёты агента — `reports/` в корне (не внутри `game/`);
  - справочники — `references/` (`ps2_to_renpy.csv`, `image_id_map.csv`);
  - автопроверки — `tools/check_project.py`;
  - созданы папки глав `game/chapters/9` … `28`;
  - бакеты `tl/` остаются плоскими; см. `AGENTS.md` §6.
- Открытые вопросы: см. записи ниже.

## 2026-10-02 — инструменты среды и чистка документов

- статус: INFO
- место: корень проекта, `tools/`, `references/`, `game/tl/`
- Решения:
  - `tools/agent_workflow.py` (был из новелльного проекта) переписан под ZnT1:
    модель «глава + часть», пути `game/chapters/<N>/script-ch<N>_<M>.rpy`,
    `ps2_source/`, `reports/`; режимы PROMPTS — first-launch, continue, port-part,
    translate-edit, voice-work, full-audit, grammar-audit, style-audit, humanizer,
    resolve-decisions, pragmatic-c, analyzer-phase1/phase2, encoding-check;
    ACTIONS — check-project, chapter-state, source-stats, image-id-map,
    bg-placeholders; есть `--list`. Промпт сохраняется в `agent_prompt.md`
    (в `.gitignore`); в консоль не выводится. Старый контур (translates/merged/
    output/_audit/*_scan.py/блоки) удалён.
  - `game/tl/japanese/common.rpy` и `game/tl/russian/common.rpy` взяты из
    документации Ren'Py: атрибут `+R` (read-only), из проверок исключены
    (`TL_READONLY_SUFFIXES` в `tools/check_project.py`) — ключи участвуют в
    покрытии E4/E5, но E6/E8/W1 по ним не выдаются. Предупреждений стало 812 → 277.
  - `references/image_id_map.csv` **сгенерирован из источника**
    (`python tools/build_image_id_map.py`): 312 строк = 117 фонов (`bg`) + 197 CG
    (`cg`), 2 id встречаются и так, и так; колонки `filename`/`notes` заполняет
    человек — сейчас пусты (0 из 312).
  - Правило заглушек: пока `filename` пуст, фон пишется как `fade_fx("id(K)")`
    (`id(1145)`), CG — `dissolve_fx("id(K)", type="cg")`; имя «на глазок»
    запрещено. После заполнения справочника —
    `python tools/replace_bg_placeholders.py --apply` (по умолчанию dry-run,
    отчёт `reports/bg_placeholders.md`; заглушки внутри `game/tl/` не трогаются —
    их `old` синхронизировать вручную).
  - Новые автопроверки: **E9** — битые/дублирующиеся строки `image_id_map.csv`;
    **E10** — заглушка `id(K)` отсутствует в справочнике; **W6** — заглушка
    осталась, хотя имя уже заполнено. Текущий прогон: `RESULT: OK`
    (`labels=33 overlayK=6 strings=1549 voices=1156`, errors=0, warnings=277).
  - `dictionary.md` и `addresses.md`: добавлены шапки о происхождении пометок —
    «т. N / Том vNN / гл. N / chNN / бN» относятся к источнику-ранобэ и старой
    структуре работы, к `game/chapters/<N>` отношения не имеют; заголовки разделов
    помечены `[ранобэ]`, инлайновые «т.NN» → «т. NN ранобэ».
  - Смысловые правки при этой чистке (не касаются канона лексики):
    Генриетта — «до восшествия на престол — принцесса; после — королева»
    (было «до т.5 / с т.5»); Виконт — «позднее — Вард, имя названо в т. 2 ранобэ»;
    в `addresses.md` ссылка на журнал `output/_log/` → `reports/log.md`.
  - Удалены `STRUCTURE_AGENT.md`, `TRANSLATION_AGENT.md`,
    `NOVELL_AGENTS_INSTRUCTION.md`; исправлены ссылки на них в
    `EXTRACTION_METHOD.md` (открытая задача → `references/image_id_map.csv`) и
    `references/ps2_to_renpy.csv` (источник грамматики → AGENTS.md §2–§3 + скиллы).
  - `.gitkeep` добавлен в 27 пустых папок `game/chapters/2` … `28`.
  - Отключённые системой скиллы `translation-audit`, `semantic-audit-a`,
    `semantic-audit-b` убраны из таблицы `AGENTS.md` §7: задания по ним не
    генерировать; файлы на диске не трогались.
- ???: в `addresses.md` осталась пометка «Пример (т.14, ch04)» — `ch04` могло
  означать главу ранобэ либо старую нумерацию работы; требует уточнения.

## 2026-10-02 — расхождение симпатии с источником (ch1, часть 5)

- статус: ???
- место: `game/chapters/1/script-ch1_5.rpy:211-212` ↔
  `ps2_source/events_full/chapter_02_ゼロのルイズ.txt:1175`
- вопрос: в источнике точный вызов `LIKE like("シエста", -10)` (читаемый вид —
  `【好感度】シエスタ -10`, `chapters/*.txt:1208`) и в этом фрагменте события
  `like()` по Луизе **нет**; в скрипте стоит
  `update_sympathy(-20, char_key="siesta")` и `update_sympathy(20, char_key="louise")`.
  Похоже на удвоение значения: `chapters/*.txt:853` `【好感度】シエスタ 10` ↔
  `script-ch1_5.rpy:136` `update_sympathy(20, char_key="siesta")`
  (парность здесь проверена не так строго, как первый случай).
- решение: **не править** — нужно решение пользователя (масштаб шкалы ремастера
  -100…+100 в `game/scripts/features/sympathy.rpy:415` не даёт оснований
  умножать; PS2-код `like()` недоступен). Если масштаб не предполагает ×2,
  привести к источнику и проверить остальные `update_sympathy` главы 1.
