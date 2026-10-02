# Как из PS2-бинарников были извлечены диалоги — методология

**Исходный образ:** `D:\gameMake\ZnT-1\ZNT_TEST\PS2_GAME\`
**Рабочая папка:** `D:\gameMake\ZnT-1\ZNT_TEST\`
**Результат:** `D:\gameMake\ZnT-1\ZNT_TEST\output\` → 17 282 реплики, 32 главы, 1920 сцен
**Куда это уходит:** инструкции `TRANSLATION_AGENT.md` и `STRUCTURE_AGENT.md` (лежат рядом)

> Игра — *ゼロのルイズ / Zero no Tsukaima: KOAKUMA to HARUKAZE no Concerto*,
> PS2, **SLPS_257.09**. Текст — **Shift-JIS (CP932)**, скрипты — **Squirrel**
> (диалект JavaScript-подобного языка). Перевода на этом этапе **не делалось** —
> только извлечение оригинального текста и потока событий.

---

## 0. Итог одной строкой

Из архива `SCENE_ID.BIN` восстановлены все 1920 сценарных скриптов (100% валидных по CP932),
разобраны на события, сгруппированы в 32 главы и выгружены в три параллельных вида
(читаемый / машинный / сырой), плюс сквозной список всех реплик. Валидация — `ALL CHECKS PASSED`.

---

## 1. Входные данные

```
PS2_GAME\OriginalFiles\Original\
  SCENE_ID.BIN   6 492 160 Б   архив сценарных скриптов (1920 записей)
  SCENE_ID.HD    7 684 Б       таблица размеров: 7684/4 = 1921 запись u32 LE
  VOICE_ID.BIN 981 067 776 Б   архив озвучки
  VOICE_ID.HD      64 768 Б    64768/4 = 16 192 голосовые дорожки (id 0..16191)
  SOUND_ID.BIN  150 704 128 Б  архив BGM/SE (≈99 записей)
  NORMAL.BIN / SCENEDAT.BIN    архивы изображений + .HD
  SLPS_257.09                  исполняемый файл
  SYSTEM.CNF, MOVIE, IOP, NORMAL.HD ...

PS2_GAME\OriginalFiles\decoding\
  quickbms\                    утилита/скрипты первичной распаковки
  unpacked\
    SCENE_ID.BIN\*.BIN         1920 «голых» записей  ★ вход для этапа 1
    SCENEDAT.BIN\*.PNG         1104 оригинальные картинки (фоны / CG)
    NORMAL.BIN\*.PNG           335  оригинальные картинки (спрайты / прочее)
    VOICE_ID.BIN\*.STV         16192 голосовых дорожек (0..16191)
    SOUND_ID.BIN\              BGM/SE + autoDecodeSTV.py (конвертер STV → wav)
```

Первичную распаковку по контейнеру (quickbms) считал уже готовой: в `unpacked/SCENE_ID.BIN`
лежат ровно 1920 файлов — это тела записей без заголовка. Всё дальнейшее делал сам.

---

## 2. Этап 1 — контейнер `HD` + `BIN` и правило интерливинга

**Скрипт:** `reconstruct_final.py` (→ `output/scripts/SCENE_%04d.txt`)

### 2.1 Формат

`SCENE_ID.HD` — массив `u32 LE`, по одному `SIZE` на запись (позиционно).
`SCENE_ID.BIN` — записи подряд с выравниванием **на 0x800**:

```
pos = 0
for idx in 0..ENTRIES:
    SIZE  = HD[idx]                          # размер записи целиком
    XSIZE, ZIP = u32, u32  по bin[pos:pos+8]  # заголовок
    data  = bin[pos+8 : pos+SIZE]            # тело
    pos  = align(pos + SIZE, 0x800)
```

* `ZIP == 1` — данные уже лежат «как есть», обычный текст.
* `ZIP >= 2` — данные являются **перемешиванием (interleave) `k = ZIP` потоков**.

### 2.2 Правило деинтерливинга (главная находка)

Куски вычисляются так, что **остаток достаётся ПОСЛЕДНЕМУ куску**, затем — склейка round-robin:

```python
def deinterleave(o, k):
    n = len(o)
    b = n // k
    sizes = [b] * (k - 1) + [n - b * (k - 1)]   # ← остаток в последний кусок
    chunks, p = [], 0
    for L in sizes:
        chunks.append(o[p:p+L]); p += L
    out = bytearray()
    for j in range(max(len(c) for c in chunks)):
        for c in chunks:
            if j < len(c):
                out.append(c[j])                 # ← round-robin по столбцам
    return bytes(out)
```

Альтернативы (остаток в первый кусок / равномерное деление / деление наоборот) **провалились** —
проверялись брутфорсом `k_compare.py`, `kway.py`, `verify_k.py`, `test_interleave.py`, `cut_modes.py`,
`validate_recon.py`, `scan_window.py`, `scan_split.py`, `exact_rel.py`.

**Статистика по 1920 записям:** `{ZIP=1 (raw): 377, 2: 1533, 3: 6, 4: 1, 6: 2, 12: 1}`

Фолбэк: если после разбора `sjis_ratio < 0.999` — перебираются `k = 2..16` и берётся
лучший балл `sjis_ratio*100 + 1.5 * (count("set(") + count("talk(") + …)`.

**Результат: `bad = 0`**, все 1920 файлов имеют `sjis = 1.0000`.

---

## 3. Этап 2 — парсер скриптов (CP932-безопасный)

**Скрипт:** `extract_final.py` (18 974 Б, финальный)

Скрипты — исходник Squirrel, а не байткод, поэтому разбирал их напрямую по байтам.

### 3.1 Почему «наивный» разбор не годится

* Японская **канва «、» в CP932 = байты `0x81 0x5C`**, а `0x5C` — это `\`.
  Разделитель строк/экранирование наивным способом ломается на первой же запятой в тексте.
* **Байты 0x81–0x9F и 0xE0–0xFC — старшие байты двойных символов**, их нельзя считать
  одиночными: кавычка внутри японского текста может означать совершенно другое.

### 3.2 Решение — всё считается парами

```python
def _lead(c):
    return (0x81 <= c <= 0x9F) or (0xE0 <= c <= 0xFC)

def skip_string(d, i):          # d[i] == 0x22 → индекс за закрывающей кавычкой
    i += 1
    while i < n:
        c = d[i]
        if c == 0x5C: i += 2; continue      # экранирование
        if c == 0x22: return i + 1          # конец строки
        if _lead(c): i += 2; continue       # двойной SJIS-символ
        i += 1
    return n
```

Аргументы разбиваются `split_top()` по запятым **только на глубине 0**,
с защищёнными строками и учётом `()`, `{}`, `[]`.

### 3.3 Что вытаскивалось

* `talk(...)` — **реплики**. Встречается **две сигнатуры**:
  * `talk(голос, null, текст, голосовой_id)` — 4 аргумента;
  * `talk(голос, текст, голосовой_id)` — 3 аргумента (**сцены 63–67**);
  * объявление движка `talk(name, disp, text, voice)` в **сцене 3 — пропускается**.
* `set(layer, {…})` — смена фона/CG/спрайтов/музыки/звуков.
* `trans("crossfade", ms)`, `next(...)`, `selectItem(...)`, `selectInit(...)`,
  `title(...)`, `like(...)`, `dateItem/date(...)`, `moveItem(...)`, `waitTime(...)`, `reset()` и др.

---

## 4. Этап 3 — группировка по главам

**Авторитетный признак — 29 вызовов `title()`** + граф переходов `next()`.

| глава | сцены | как определялась |
|---|---|---|
| `00` Система (движок/меню/галерея) | 0–4, 1861–1869, 1915–1920 | **не портируется** |
| `01`…`29` основные | 5…1532 | индекс между маркерами `title()` |
| …из них сцены **1009–1532** | — | **back-trace** к ближайшему «своему» главе-предку (свидания/ветки, предложенные этой главой) |
| …из которых ушли вперёд | — | **forward-trace** к уже известной главе |
| `90` 特別イベント A | 1533–1696 | семья `dlEventId`, динамический диспетчинг |
| `91` 特別イベント B | 1697–1860 | семья `tnEventId`, динамический диспетчинг |

Результат: **`chapters = 32`, `dialogues = 17282`, `unassigned = 0`, `traced = 568`.**
То есть ни одна реплика не осталась «без главы».

Динамические спец-события (90/91) в PS2 вызываются **вычислением**
`(tun ? tnEventId : dlEventId) + 2 + no*3 + event[no]` из `getTunDeleScene()`,
поэтому статических ссылок на них нет — их пришлось клеить отдельными семьями id.

---

## 5. Этап 4 — что лежит в `output/`

```
output\
  chapters\chapter_NN_<яп.название>.txt   32  ★ ЧИТАЕМЫЙ вид (реплики + события, порядок источника)
  events_full\chapter_NN_<яп.название>.txt 32 ★ МАШИННЫЙ вид (все вызовы с сырыми аргументами)
  scripts\SCENE_%04d.txt                 1920  СЫРОЙ восстановленный CP932-исходник
  all_dialogues.txt                            все 17282 реплики подряд, по главам
  chapter_map.txt                              таблица глав: ядро сцен / talk / set / trans / choice
  chapter_stats.json                           то же в JSON (сумма talk = 17282)
  README.txt                                   описание форматов (яп + англ)
  _diagnostics\                                все отчёты (см. §8)
```

Формат `chapters/*.txt`:

```
---- SCENE 0006 ----
  [TITLE title("ゼロのルイズ")]
  [BG       stage    image=+85, level=200]
  [EVENT_CG event    image=+148, level=80]
  [SPRITE   lay5     image=+390, level=160, dir=1A]
  [BGM      bgm      play=+19]
  [SE       se0      play=+63]
  [TRANS    trans("crossfade", 1000)]
サイト：よろしく頼む。  [voice 15898]
（ルイズが頬を膨らませた）  [voice 15901]
  【選択肢】シエスタ → scene 1014
  【デート】ルイズ → scene 1009
  【好感度】ルイズ  10
  → next scene 68
```

Коды ресурсов: `(0x01000000 +N)` сцена, `(0x02000000 +N)` картинка,
`(0x03000000 +N)` BGM/SE, `(0x04000000 +N)` голос.

Формат `events_full/*.txt`: префикс события + точный вызов, `## SCENE NNNN` как разделитель.
**Список видов:** `DIALOGUE SET TRANS GOTO CHOICE DATE TITLE WAIT MSGON MSGOFF BACK RESET
LIKE ITEM MOVIE VIBRATE CREATE SYNC MENU MENUINIT TNDL MAPDEST MOVE MOVEINIT COFFEE SKIP
RESETSEL DECL`.

---

## 6. Этап 5 — верификация

**Скрипт:** `verify_final.py` → печатает `verify ok=True`, отчёт в `_diagnostics/final_verify.txt`

```
[OK ] chapters/ has 32 files (got 32)
[OK ] chapters/ and events_full/ file names match
[OK ] events_full DIALOGUE lines = 17282 (got 17282)
[OK ] all_dialogues.txt lines = 17282 (got 17282)
[OK ] dialogue counts agree (17282 vs 17282)
[OK ] all 1920 reconstructed scenes covered (got 1920)
[OK ] scene sets identical
[OK ] no empty chapter files []
[OK ] no replacement chars in chapter files []
[OK ] chapter_01 contains Japanese characters (233)
[OK ] DIALOGUE kind = 17282
[OK ] SET kind = 28400 (got 28400)
[OK ] TRANS kind = 1293 (got 1293)
[OK ] chapter_stats.json talk sum = 17282 (got 17282)

RESULT: ALL CHECKS PASSED
```

Контрольные числа: `DIALOGUE 17282`, `SET 28400`, `WAIT 2258`, `MSGOFF 2078`, `RESET 1903`,
`GOTO 1416`, `BACK 1299`, `TRANS 1293`, `CHOICE 1092`, `MSGON 879`, `SYNC 484`,
`MENUINIT 390`, `MENU 364`, `TNDL 332`, `LIKE 273`, `VIBRATE 221`, `CREATE 202`,
`MOVE 97`, `MAPDEST 81`, `COFFEE 77`, `DATE 70`, `ITEM 70`, `SKIP 40`, `TITLE 30`,
`MOVEINIT 20`, `MOVIE 14`, `RESETSEL 3`, `DECL 1`.

---

## 7. Как повторить (три команды)

```powershell
cd D:\gameMake\ZnT-1\ZNT_TEST
python reconstruct_final.py    # HD+BIN → output\scripts\SCENE_%04d.txt   (ожидается: files=1920 bad=0)
python extract_final.py        # scripts → output\chapters, events_full, all_dialogues, chapter_map
python verify_final.py         # ожидается: verify ok=True
```

Все скрипты — обычный Python 3 без внешних зависимостей (`os`, `re`, `struct`, `json`).

---

## 8. Что лежит в `ZNT_TEST` — инвентаризация

≈160 скриптов, это **хронологический журнал** исследования. Кучу промежуточных можно не читать;
вот каркас по эпохам:

| эпоха | скрипты | зачем |
|---|---|---|
| определение кодировки | `analyze*.py`, `extract_japanese.py`, `extract_dialogues{,_sjis,_utf8,_utf16}.py`, `try_encodings.py` | UTF-8 дал мусор, UTF-16 дал 0 байт, **CP932 подтвердился** |
| попытка компилятора | `extract_all_functions.py`, `extract_structured.py`, `dump_compiled.py`, `check_plain.py`, `classify_all.py`, `find_bc_mgf*.py`, `analyze_structure.py` | проверка, байткод это или исходник → **исходник** |
| реверс контейнера | `check_hd.py`, `find_in_bin.py`, `cmp_slices.py`, `parse_records.py`, `dump_rec.py`, `zip_check.py`, `test_interleave.py` | нашёл `HD→SIZE`, выравнивание 0x800, `ZIP` |
| **поиск правила интерливинга** | `test_hyp.py`, `validate_recon.py`, `reconstruct_all{,2}.py`, `k_compare.py`, `kway.py`, `verify_k.py`, `cut_modes.py`, `scan_window.py`, `scan_split.py`, `exact_rel.py`, `diag_low.py` | главный тупик, закрыт правилом «остаток → последний кусок» |
| закрепление | **`reconstruct_final.py`**, `structure_check.py`, `balance_check.py`, `check813.py`, `search1918.py` | финальная реконструкция, `bad=0` |
| парсинг и граф | `nul_scan.py`, `encoding_cmp.py`, `scene_graph.py`, `reachability.py`, `flow_trace.py`, `edge_inspect.py`, `talk_bytes.py`, `sample_view.py` | граф сцен, доезды веток |
| главы и выборки | `inspect_unassigned.py`, `block_vs_main.py`, `block_refs.py`, `text_overlap.py`, `menu_scenes.py`, `eventid_{refs,all}.py`, `tndl_funcs.py`, `branch_peek.py`, `talk_odd.py`, `prune_stale.py`, `nul_detail.py`, **`extract_final.py`**, **`verify_final.py`** | финальные продукты |
| **сопоставление с ремастером** | `voice_probe.py`, `correspondence.py`, **`crosswalk.py`**, `bgm_check.py`, `resource_probe{,2}.py`, `voice_se_check.py`, `voice_csv_check.py`, `voice_csv_index.py`, `line_grammar.py`, `img_probe.py` | как это склеивается с `ZnT1` |

Отчёты — `output\_diagnostics\` (≈90 файлов). Ключевые для ремастера:

| отчёт | содержание |
|---|---|
| `crosswalk.txt` / `.json` | `.rpy` ↔ сцены PS2, `jump/call`, инвентарь `*_fx`, структура PS2 внутри сцен |
| `voice_scene_map.json` | `voice` → сцена → PS2-id → японский текст |
| `chapter_line_grammar.txt` | все формы строк `chapters/*.txt` + словарь говорящих |
| `bgm_check.txt` | доказательство правила BGM |
| `voice_csv_index.txt` | сверка `transcriptions_ja_ru.csv` с PS2-голосами |
| `resource_map.txt`, `resource_map2.txt` | диапазоны id картинок/BGM/SE, слои, `level`, `dir` |
| `scene_label_crosswalk.txt`, `correspondence.txt` | первые (менее удачные) версии кроссворда |
| `final_verify.txt`, `reconstruct_final.txt` | протоколы валидации |

---

## 9. Что из этого пригодилось ремастеру

Извлечённые данные позволили **доказать три вещи**, без которых порт невозможен:

1. **BGM.** PS2 `[BGM bgm play=+K]` → файл `audio/bgm/t{K-1}.ogg`.
   Проверено `bgm_check.py`: правило `t(K-1)` набирает **32 совпадения** из 32 однозначных,
   гипотезы `tK` и `t(K+1)` — лишь 14 и 11. Пример: `[BGM play=+24]` → `new_music="t23"`.

2. **Голоса.** `[voice N]` из PS2 = индекс строки в `transcriptions_ja_ru.csv`
   = имя файла `VOICE_ID.BIN_%08X.wav`.
   Решающее доказательство: **«дырок» в CSV ровно 1154 и голосовых ссылок в `.rpy` ровно 1154**,
   при этом первые дырки `53, 54, 55, 56` — это как раз реплики пролога
   (доказательство — `voice_csv_index.txt`). Отсюда следует, что CSV — это **очередь
   непортированного**, а `original` внутри — **ASR-расшифровка аудио, не канонический текст**
   (поэтому искать голос нужно **по id, а не по тексту**).

3. **Кроссворд сцен.** `crosswalk.py` резолвит **1218 из 1339 (91%)** реплик проекта
   на конкретные сцены PS2 и **1082** на PS2-id голоса — то есть глава 1 можно сверить
   со источником строка в строку.

Отдельно оказалось, что **`(0x02000000 +K)` — единое id-пространство** для фонов, CG и спрайтов:
`stage` → 117 id в 1..1173, `event` → 197 id в 1..1176, `layN` → 322 id в **302..1125**,
пересечений «спрайты ↔ фоны/CG» = **0**. Но id **не совпадает** с номером записи в распакованных
PNG (в `SCENEDAT.BIN` нет записей 5..15, хотя фоновые id их содержат; в `NORMAL.BIN` нет 1..6,
хотя фоновые id их содержат) — значит где-то есть транслирующая таблица. Это **открытая задача №1**,
она описана в `STRUCTURE_AGENT.md` §4.1.

---

## 10. Известные аномалии (не баги, это свойства источника)

* **Индекс 1239 отсутствует** в архиве — 1920 записей, не 1921 (в HD 1921 слот, один нулевой).
* **12 файлов содержат NUL** — 1533, 1534, 1664, 1697, 1698, 1904, 1909, 1914, 1918, 1919,
  1920, 664. Все это стабы 26–293 байт **без единого `talk()`** — потери текста нет.
* **Title-карточки 429 и 769 изолированы** («魅惑のお姫さま», 「小悪魔のおしおき」),
  основной текст этих глав идёт в сценах **430** и **770**.
* `output/chapters/chapter_00_システム…` (сцены 0–4, 1861–1869, 1915–1920) — это меню и
  библиотека движка, **не портируется**; там же `selectItem(..., (zero_route=N))`.
* Сцены `0–3` — движковая библиотека (`sceneMain`, `Layer`, `ScreenLayer`, объявление `talk(...)`).
* `chapter_02` содержит 118 сцен, хотя ядро — 0006–0067: остальные (1009–1033, 1224–1255)
  приклеены back-trace'ом как свидания/ветки первой главы.

---

## 11. Подводные камни окружения (чтобы не повторять)

1. **PowerShell здесь — cp1251.** Японский/русский в консоль печатать **нельзя**
   (получится `????` или мусор). Результаты — в UTF-8 файлы, читать их инструментом `read`.
   Даже `Get-Content -Encoding UTF8` отдаёт кракозябру в этом шелле.
2. **`python -c "..."` ломается** из-за кавычек и переводов строк в PowerShell.
   Правило: писать `.py`-файл через `write` и запускать `python <файл>`.
3. **Кодировка выходных файлов — всегда UTF-8 явно**, `encoding="utf-8"` в каждом `open`.
4. **`errors="replace"` на входе** допустим только для чернового анализа; в финальном
   `extract_final.py` текст декодируется по байтам, чтобы не потерять символы.
5. Мусорные `.py` из первых итераций (`analyze.py`…`analyze8.py`, `extract_dialogues*.py`)
   **оставлены намеренно** как журнал — удалять их не нужно, но и не опираться на них:
   финальная цепочка только три скрипта (§7).

---

## Связанные документы

| файл | что описывает |
|---|---|
| `TRANSLATION_AGENT.md` | грамматика `output/*`, таблица глав, соответствие PS2 → Ren'Py, workflow голосов и переводов |
| `STRUCTURE_AGENT.md` | состояние проекта `ZnT1`, целевая раскладка, открытые проблемы, требования к скиллам |
| `EXTRACTION_METHOD.md` | **этот файл** — как данные были получены |
| `output/README.txt` | форматы выходных файлов (по-японски / по-английски) |
| `ZNT_TEST/output/_diagnostics/*` | все отчёты, упомянутые выше |
