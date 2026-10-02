---
name: assets
description: Ассеты ремастера: BGM по правилу t{K-1} из [BGM play=+K] (никогда «на глазок»), политика точечного переноса SE, справочник references/image_id_map.csv (формат и как расширять), где лежат оригиналы PS2 PNG/STV/wav и как конвертировать STV (autoDecodeSTV.py), что коммитится в git, а что нет (game/INSTRUCTION.md). Применять при подборе фонов/CG/спрайтов/музыки/звуков для части и при добавлении новых медиа.
---

# assets — BGM, SE, картинки, оригиналы, git vs медиа

## 1. BGM — правило `t{K-1}` (доказано, не «на глазок»)

```text
PS2:  [BGM bgm play=+K]   ==   events_full: set("bgm", {play = (0x03000000 +K)})
Ren'Py:  файл game/audio/bgm/t{K-1}.ogg
```

Пример: `[BGM bgm play=+24]` → `new_music="t23"`; `[BGM play=+19]` → `t18`.

* Доказательство: `ps2_source/_diagnostics/bgm_check.txt` — правило `t(K-1)` даёт
  **32 совпадения из 32** однозначных случаев; гипотезы `tK` и `t(K+1)` набирают
  лишь 14 и 11.
* Файлов 32: `game/audio/bgm/t1.ogg` … `t32.ogg`. `t1`,`t2` практически не
  используются (PS2 начинается с id 3), `t32` — музыка экрана «конец главы»,
  добавленного ремастером.
* В коде музыка задаётся **внутри** `*_fx`: `$ dissolve_fx("forest", new_music="t18")`,
  либо отдельно `play music t18` / `stop music fadeout 1.0`
  (стоп: `[BGM bgm stop=1000]` → `stop music fadeout 1.0` или `stop_music=True`).
* Ни один `t*` не берётся «похожий»/«по настроению» — только по формуле.

## 2. SE — правила нет, портируется точечно

* PS2: `[SE seN play=+K]`, `K ∈ 36..95`, всего 35 разных id
  (`[SE se0 play=+63]`, `[SE se1 stop=1]`).
* В ремастере всего **9 файлов** `game/audio/sfx/`:
  `blow, blow_2, close_door, door, knock_door, open_door, punch, read, take_sword`.
* Из них в главах используются 4: `take_sword` (ch1_1), `knock_door` (ch1_3/5/8),
  `read` (ch1_8/10), `blow_2` (ch1_6).
* Большинство PS2-SE — щелчки UI и атмосфера, **их не переносят**. Переноси только
  осмысленные (дверь, оружие, листание) и смотри, как сделано в эталоне:
  `play sound take_sword`.
* Имя звука в `play sound` — без пути и расширения, файл должен лежать в `game/audio/sfx/`.

## 3. Картинки: `references/image_id_map.csv`

**Справочник обязателен перед новой главой.** Файл **генерируется из источника**, а не
пишется с нуля:

```powershell
python tools/build_image_id_map.py                 # все id фонов и CG
python tools/build_image_id_map.py --include-chara # + id спрайтов
python tools/build_image_id_map.py --dry-run       # только статистика
```

Формат (колонки, UTF-8, с `#`-комментариями в шапке как в `ps2_to_renpy.csv`):

```text
image_id,kind,filename,source,notes,uses,chapters
28,bg,forest,chapter_02 [BG stage image=+28],,12,02;03;05
390,chara,l 1 angry,chapter_02 [SPRITE lay5 image=+390],,4,02
148,cg,l_s_forest,chapter_02 [EVENT_CG event image=+148],,7,02;03
```

* `image_id` — **K из `(0x02000000 +K)`** в источнике;
* `kind` ∈ `bg | cg | chara` (составные виды через `|`, если id встречается и как фон,
  и как CG);
* `filename` — имя в проекте: для `bg`/`cg` имя файла без расширения
  (`fade_fx("forest")`, `dissolve_fx("l_s_forest", type="cg")`), для `chara` — тег
  image вида `"l 1 angry"`, `"s 3 sad"`. **Заполняет человек**; пусто = не сопоставлено;
* `source`, `uses`, `chapters` — генерируются (первая находка, число использований,
  главы источника через `;`); пересборка их перезаписывает, `filename`/`notes` — **нет**;
* `notes` — сомнения и `PROVISIONAL` (заполняет человек).

### 3.0 Заглушки `id(K)` и их замена

Пока `filename` пуст, при порте фон пишется **заглушкой** — самим id:

```renpy
$ fade_fx("id(1145)")                 # фон без сопоставления
$ dissolve_fx("id(148)", type="cg")   # CG без сопоставления
```

После того как человек заполнил `filename`, заглушки подставляются автоматически:

```powershell
python tools/replace_bg_placeholders.py           # dry-run: что найдено
python tools/replace_bg_placeholders.py --apply   # внести замены
```

Отчёт — `reports/bg_placeholders.md` (готово к замене / остаются заглушками /
заглушки внутри `game/tl` — их `old` синхронизировать вручную). Правило проверяется
`tools/check_project.py`: **E10** — заглушка `id(K)` отсутствует в справочнике;
**W6** — заглушка осталась, хотя имя уже заполнено; **E9** — битые/дублирующиеся
строки CSV. Заглушка «на глазок» вместо `id(K)` — нарушение (см. AGENTS.md §9).

### 3.1 Свойства id-пространства (проверенные факты)

* `(0x02000000 +K)` — **единое** пространство для фонов, CG и спрайтов:
  `stage` → 117 id в 1..1173; `event` → 197 id в 1..1176; `layN` → 322 id в
  **302..1125**; пересечений «спрайты ↔ фоны/CG» = **0**. Всего 634 разных id из 1..1176.
* id **не совпадает** с номером записи в распакованных PNG: в `SCENEDAT.BIN` нет
  записей 5..15, хотя фоновые id их содержат; в `NORMAL.BIN` нет 1..6, хотя
  фоновые id их содержат → **напрямую id → имя файла не переводится**, нужна
  транслирующая таблица (это и есть `image_id_map.csv`).

### 3.2 Как расширять справочник

1. Сначала прогнать генератор — он добавит недостающие id и **сохранит** уже
   заполненные `filename`/`notes`: `python tools/build_image_id_map.py`
   (сейчас в файле: 312 строк — 117 фонов + 197 CG, две пары id общие).
2. Заполнение `filename` — **работа человека**: сопоставить id с существующими
   картинками проекта. Агент НЕ придумывает пары: пока `filename` пуст, в скриптах
   остаётся заглушка `id(K)` (§3.0). Кандидатов для сверки подсказывают колонки
   `uses`/`chapters` (в каких главах id встречается) и первая находка `source`.
3. Остальное — визуально: оригинал
   `D:\gameMake\ZnT-1\ZNT_TEST\PS2_GAME\OriginalFiles\decoding\unpacked\SCENEDAT.BIN\*.PNG`
   (1104 фон/CG) или `…\NORMAL.BIN\*.PNG` (335 спрайт/прочее) против
   `game/images/bg` (65), `game/images/cg` (41), `game/images/chara` (289).
4. **Каждую новую пару записывать в справочник сразу** — иначе глава N+1 ищет одно
   и то же заново.
5. Имена, уже объявленные в `game/definitions.rpy` (~179 инструкций `image …`) —
   первый источник имён:

```renpy
image bg forest = "bg/forest.webp"
image bg town_square_night = "bg/town_square_night.webp"
image bg overlay = "bg/overlay.webp"
```

`overlay_screen` строит фон как `"bg " + scene_name (+ "_blurred")`, поэтому
`scene_name` в `call overlay_screen("forest", …)` — это имя **без** префикса `bg `.

### 3.3 Гигиена папок картинок

Фактическая раскладка на момент инвентаризации:
`bg 65`, `cg 41`, `chara 289`, `orig 1038`, `renamed 395`,
плюс дубли `chara - копия` (289) и `renamed` (PNG-копии тех же ассетов).
**Не создавай новых дублей**; расхождение имён фиксируй в `reports/log.md`.

## 4. Оригиналы PS2 и конвертация

```text
D:\gameMake\ZnT-1\ZNT_TEST\PS2_GAME\OriginalFiles\
  Original\SCENE_ID.BIN|.HD        архив скриптов
  Original\VOICE_ID.BIN|.HD        архив озвучки (16 192 дорожки, id 0..16191)
  Original\SOUND_ID.BIN|.HD        архив BGM/SE (~99 записей)
  decoding\unpacked\SCENEDAT.BIN\*.PNG   1104 оригинальные картинки (фоны/CG)
  decoding\unpacked\NORMAL.BIN\*.PNG     335  оригинальные картинки (спрайты/прочее)
  decoding\unpacked\VOICE_ID.BIN\VOICE_ID.BIN_<hex8>.STV   16 192 голоса
  decoding\unpacked\SOUND_ID.BIN\                            BGM/SE + autoDecodeSTV.py
```

* **STV → wav**: `decoding\unpacked\SOUND_ID.BIN\autoDecodeSTV.py`
  (подробности голосов — скилл `voice-workflow`).
* Конвертация картинок: из PNG проект использует **`.webp`**
  (`game/images/bg/*.webp`, `cg/*.webp`); если ассета нет — сначала искать в
  `game/images/orig` (1038 PNG) и `game/images/renamed`.
* Медиа-оригиналы **не в git** (внешний архив `ZNT_TEST`, вне репозитория).

## 5. Git vs медиа (`game/INSTRUCTION.md`)

В git идут **скрипты**: `.rpy`, `tl/`, `references/`, `reports/`, `tools/`,
`ps2_source/`, `dictionary.md`, `addresses.md`, `transcriptions_ja_ru.csv`.

**Не коммитятся** — «динамические» папки: **`audio`, `gui`, `images`, `video`**
(и все `*.ogg`, `*.png`, `*.webp`, `*.wav`, `*.webm` — `.gitignore` это уже покрывает).
Медиа хранятся отдельным архивом в облаке.

Полное обновление игры = `git pull` + скачать архив медиа из облака и положить в
`game/` (**старые папки предварительно удалить**).

Новые голоса живут в `game/audio/voices/` локально и в облачном архиве:
порция коммита `script + tl + transcriptions_ja_ru.csv + reports` — без `.ogg`.

## 6. Чек-лист по ассетам перед закрытием части

- [ ] Каждый `[BGM play=+K]` превращён в `t{K-1}`; ни один `t*` не взят «на глазок».
- [ ] Каждый `image_id` из части есть в `image_id_map.csv` (нет прогонов с недостающими
      строками — `build_image_id_map.py` дописал, E9 чист); каждый фон/CG — либо
      заполненный `filename`, либо заглушка `id(K)` (E10 чист, W6 отсутствует).
- [ ] Перенесённые SE названы именами из `game/audio/sfx/` (или добавлены туда).
- [ ] Медиа не попали в git (`git status` — без `audio/`, `images/`, `gui/`, `video/`).
- [ ] Нет новых дублей папок/файлов в `game/images/`.
