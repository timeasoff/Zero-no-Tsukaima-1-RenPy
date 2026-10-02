# ИНСТРУКЦИЯ АГЕНТУ ПЕРЕВОДА / ПОРТИРОВАНИЯ

Проект: **The Familiar Zero (小悪魔と春風の協奏曲) — Unofficial Remaster**, `D:\gameMake\ZnT-1\ZnT1`
Источник: расшифрованные скрипты PS2-версии, `D:\gameMake\ZnT-1\ZNT_TEST\output`

Твоя задача — **переносить диалоги и события из PS2-скриптов в существующий Ren'Py-проект**
и продолжать перевод. Ты **не настраиваешь структуру** (это другой агент, см.
`STRUCTURE_AGENT.md`, который лежит рядом). Существующие файлы не переписывай
архитектурно — только добавляй новые главы/строки и переводы.

---

## 0. Что читать обязательно перед работой

| Файл | Зачем |
|---|---|
| `game/chapters/0/script-ch0.rpy` | **Эталон №1** — пролог, самый короткий, показывает весь цикл целиком |
| `game/chapters/1/script-ch1_*.rpy` (10 файлов) | **Эталон №2** — первая глава, переведена вручную полностью |
| `game/PROMTS.md` | Правила перевода (3 варианта, сохранять «-сан», троеточие и т.д.) |
| `game/README.md` | Общее описание ремастера, 3 языка |
| `game/INSTRUCTION.md` | Разделение git-файлов и «динамических» медиа-папок |
| `game/definitions.rpy` | Объявления `image bg …` |
| `game/characters.rpy` | Короткие коды говорящих + реестр `char_data` |
| `game/scripts/features/*.rpy` | Сигнатуры всех `*_fx`, `show_sprites`, `update_sympathy`, `*_choice` |
| `output/_diagnostics/crosswalk.txt` | Как глава 1 соотносится с сценами PS2 (готовый ориентир) |

---

## 1. Карта источников (ZNT_TEST)

```
D:\gameMake\ZnT-1\ZNT_TEST\
  output\
    chapters\chapter_NN_<название>.txt      32 файла — ЧИТАЕМЫЙ вид: реплики + события,
                                            строго в порядке источника   ★ основной вход
    events_full\chapter_NN_<название>.txt   32 файла — ВСЕ вызовы с сырыми аргументами ★ точный вход
    scripts\SCENE_%04d.txt                  1920 шт., сырой CP932 (если нужен контекст if/for)
    all_dialogues.txt                       все 17 282 реплики по порядку глав
    chapter_map.txt / chapter_stats.json    таблица глав, диапазоны сцен, статистика
    README.txt                              полное описание формата (по-японски/англ.)
    _diagnostics\                           готовые отчёты (см. §10)
  PS2_GAME\OriginalFiles\
    Original\SCENE_ID.BIN|.HD               архив скриптов
    Original\VOICE_ID.BIN|.HD               архив голосов   (16192 записи, id 0..16191)
    Original\SOUND_ID.BIN|.HD               архив BGM/SE    (~99 записей)
    decoding\unpacked\
      SCENE_ID.BIN\*.BIN                    1920 сырых записей скриптов
      SCENEDAT.BIN\*.PNG                    1104 оригинальных картинки PS2 (фоны/CG)
      NORMAL.BIN\*.PNG                      335  оригинальных картинки PS2 (спрайты/прочее)
      VOICE_ID.BIN\VOICE_ID.BIN_<hex8>.STV  16192 голосовых дорожек
      SOUND_ID.BIN\                         BGM/SE + autoDecodeSTV.py (конвертер STV→wav)
```

> **Правило кодировки.** PowerShell здесь — cp1251. Никогда не печатай японский/русский
> в консоль. Пиши UTF-8 файлы, читай их инструментом `read`.
> `python -c "..."` с кавычками/переносами ломается — создавай `.py`-файл и запускай.

---

## 2. Грамматика `output/chapters/*.txt`

```
========================================================================
CHAPTER 02 : ゼロのルイズ
core scenes : 0006-0067
========================================================================

---- SCENE 0006 ----
  [TITLE title("ゼロのルイズ")]                       ← заголовок главы/сцены
  [BG       stage    image=+85, level=200]            ← смена фона
  [EVENT_CG event    image=+148, level=80]            ← показ CG
  [SPRITE   lay5     image=+390, level=160, dir=1A]   ← показ спрайта в слоте
  [SPRITE   lay5     hide]                            ← скрыть слот
  [SPRITE   lay5     x=224, y=0]                      ← сдвиг слота
  [BGM      bgm      play=+19]                        ← включить музыку
  [BGM      bgm      stop=1000]                       ← fadeout 1000 мс
  [SE       se0      play=+63]                        ← эффект
  [SE       se1      stop=1]
  [TRANS    trans("crossfade", 1000)]                 ← переход, мс (всегда crossfade)
  [VIBRATE  vibrate(2)]                               ← тряска
  [LAYER    white   image=+2, level=0]  /  hide       ← вспышка
  [MOVIE    movie(0)]                                 ← видео
  [COFFEE]                                            ← пауза (в ремастере пока не реализована)
サイト：よろしく頼む。  [voice 15898]                    ← РЕПЛИКА: говорящий(10)＋：＋текст＋[voice N]
（ルイズが頬を膨らませた）  [voice 15901]                 ← мысли/нарратив, обёрнуто （ ）
    продолжение многострочной реплики  [voice N]       ← дочерние физические строки
  【選択肢】シエスタ → scene 1014                       ← выбор (selectItem)
  【デート】ルイズ → scene 1009                         ← свидание (dateItem)
  【デート進行】 → scene 1865                           ← продолжить свидание (date)
  【移動】表通り → scene 962  ((0x01000000 +1367))      ← переход по локации (moveItem)
  【好感度】ルイズ  10                                  ← симпатия (like) — бывает и «-10»
  → next scene 68                                      ← безусловный переход (next)
  extra scenes: 1009..1255  (56)                       ← служебная пометка (сцены других глав)
```

**Важно**
* `talk()` встречается в двух сигнатурах: `talk(голос, null, текст, голосовой_id)`
  (4 арг.) и `talk(голос, текст, голосовой_id)` (3 арг., сцены 63–67).
  Объявление движка `talk(name, disp, text, voice)` в сцене 3 — **пропускать**.
* Реплика может занимать несколько физических строк; тег `[voice N]` стоит на **последней**.
* `、` в CP932 = `0x81 0x5C` — наивный разбор «экранирования» ломается.
* Говорящие (частота): サイト 7269, ルイズ 3353, キュルケ 1221, ハルна 1081,
  シエスタ 997, タバサ 792, アンリエッタ 650, ウェザリー 358, アキナ 249,
  モンモランシー 244, コルベール 244, デルフリンガー 177, ギーシュ 171,
 奥斯マン 151, `null` 104 + NPC (味方Ａ, 将校, 魔導士, 商人, 兵士Ａ/Ｂ…).

### `output/events_full/*.txt` (точный вход)

Те же события, но сырые вызовы в порядке источника:

```
## SCENE 0006
SET        set("stage", {opacity = 100, y = 0, show = 1, level = 200,
                         x = 0, image = (0x02000000 +85)})
TRANS      trans("crossfade", 1000)
SET        set("bgm", {play = (0x03000000 +19)})
DIALOGUE   talk("サイト", null, "よろしく頼む。", (0x04000000 +15898))
CHOICE     selectItem("シエスタ", (0x01000000 +1014), null, true)
DATE       dateItem("ルイズ", (0x01000000 +1009))
GOTO       next((0x01000000 +68), true)
LIKE       like("ルイズ", 10)
TITLE      title("ゼロのルイズ")
WAIT       waitTime(1200, true)      MSGON/MSGOFF  MOVIE  VIBRATE  COFFEE  ITEM ...
```

Коды ссылок: `(0x01000000 +N)` сцена, `(0x02000000 +N)` картинка,
`(0x03000000 +N)` BGM/SE, `(0x04000000 +N)` голос.

**Полный список тегов `events_full`** (префикс + вызов):
`DIALOGUE SET TRANS GOTO CHOICE DATE TITLE WAIT MSGON MSGOFF BACK RESET LIKE ITEM
MOVIE VIBRATE CREATE SYNC MENU MENUINIT TNDL MAPDEST MOVE MOVEINIT COFFEE SKIP
RESETSEL DECL`.

---

## 3. Соответствие глав: источник → проект

**Правило: проектная папка/лейбл `N` = источник `chapter_{N+1}`**
(пролог = источник `chapter_01` = папка `0`, первая глава = источник `chapter_02` = папка `1`).

| проект | источник | ядро сцен | реплик | статус |
|---|---|---|---|---|
| `chapters/0/script-ch0.rpy` | `chapter_01_プロローグ` | 0005 | 15 | ✅ готово |
| `chapters/1/script-ch1_1..10.rpy` | `chapter_02_ゼロのルイズ` | 0006–0067 (+1009–1033, 1224–1255) | 1244 | ✅ готово |
| `chapters/2/` (пусто) | `chapter_03_黒髪の来訪者` | 0068–0136 | 1382 | ⬜ |
| `chapters/3/` | `chapter_04_女の戦い` | 0137–0218 | 1078 | ⬜ |
| `chapters/4/` | `chapter_05_トリスタニアの危機` | 0219–0268 | 1072 | ⬜ |
| `chapters/5/` | `chapter_06_本当の想い` | 0269–0343 | 1470 | ⬜ |
| `chapters/6/` | `chapter_07_家出のお姫さま` | 0344–0374 | 431 | ⬜ |
| `chapters/7/` | `chapter_08_失望のお姫さま` | 0375–0404 | 336 | ⬜ |
| `chapters/8/` | `chapter_09_決意のお姫さま` | 0405–0428 | 378 | ⬜ |
| *(новые папки 9…28)* | `chapter_10 … chapter_29` | см. `chapter_map.txt` | 10 022 | ⬜ |
| `chapters/extra/sp_l1.rpy` | `chapter_90/91` (события тундэре/дэре) | 1533–1860 | 2189 | ⬜ частично |

⚠️ Папки `2…8` в репозитории **уже созданы, но пусты** — это нормально, клади в них файлы.
⚠️ Папки `9…28` придётся создавать (это решение агента структуры — уточни у него, прежде чем плодить).

**Именование** (уже принятый в проекте стандарт):
* файлы: `script-ch<N>_1.rpy`, `script-ch<N>_2.rpy`, … (`script-ch0.rpy` для пролога)
* лейблы: `ch<N>` для первой части, `ch<N>_2`, `ch<N>_3`, … для остальных;
  внутри части — лейблы локаций: `si_room_ch1_3`, `hallway_ch1_8`, `library_ch1_8`
* соединение: последний оператор части — `jump ch<N>_<M+1>`; последняя часть — `jump attention`
* голоса: `ch<N>_<spk>_<NNN>.ogg` (часть 1) и `ch<N>.<M>_<spk>_<NNN>.ogg` (части 2+),
  нумерация внутри файла по говорящему с `001`

**Как резать главу на части.** Ориентир — глава 1: 10 частей на 1244 реплики (≈115 голосовых
на часть). Режь по естественным границам: смена локации (`[BG stage image=…]` перед новым
блоком), `→ next scene`, начало ветки `【移уд】`/`【選択肢】`. Служебные строки
`extra scenes: …` — не код, а пометка о том, что эти сцены пришли из другой главы; реплики
из них всё равно идут **своим лейблом внутри той же части** (см. `date_*_1` в `ch1_10`).

---

## 4. Таблица соответствия PS2 → Ren'Py (ядро работы)

| # | Источник (`chapters/*.txt`) | Источник (`events_full`) | Ren'Py |
|---|---|---|---|
| 1 | `голос：текст  [voice N]` | `DIALOGUE talk(...)` | `voice "chX_…_NNN"` **строкой выше** + `s "English text"` |
| 2 | реплика в `（…）` или говорящий `null` | там же | `th "text"` (курсив, своё окно) |
| 3 | `[BG stage image=+K, level=200]` | `set("stage",{image=…})` | `$ fade_fx("имя")` или `$ dissolve_fx("имя")` |
| 4 | `[EVENT_CG event image=+K, level=80]` | `set("event",{image=…})` | `$ fade_fx("имя", type="cg")` / `dissolve_fx(…, type="cg")` / `flash_fx(…, type="cg")` |
| 5 | `[BG stage hide]`, `[EVENT_CG event hide]` | `set(…,{show=0})` | обычно поглощается следующим `*__fx`; иначе `$ fade_fx("black")` |
| 6 | `[SPRITE layN image=+K, level=160, dir=1A]` | `set("layN",{image=…})` | `$ show_sprites(("l 1 angry", "s 3 sad"))` |
| 7 | `[SPRITE layN hide]` | `set("layN",{show=0})` | `$ show_sprites(("l 1",))` без убранного персонажа / `$ show_sprites(())` |
| 8 | `[SPRITE layN x=…, y=…]` | `set("layN",{x=,y=})` | `$ show_sprites(..., side="left"/"right")`; точечные сдвиги обычно опускаются |
| 9 | `[LAYER lay0 …]`, `[LAYER white …]` | `set("lay0"/"white",…)` | слой-оверлей → `flash_fx` / переход; `white` = вспышка |
| 10 | `[BGM bgm play=+K]` | `set("bgm",{play=(0x03000000+K)})` | `new_music="t{K-1}"` **внутри** `*_fx` или `play music t<K-1>` |
| 11 | `[BGM bgm stop=1000]` | `set("bgm",{stop=1000})` | `stop music fadeout 1.0` / `stop_music=True` в `*_fx` |
| 12 | `[SE se0 play=+K]` | `set("se0",{play=…})` | `play sound <имя>` — **портировано точечно, см. §7** |
| 13 | `[TRANS trans("crossfade", N)]` | `trans("crossfade", N)` | *встроен* в `*_fx(duration=N/1000)`; других переходов в игре нет |
| 14 | `[VIBRATE vibrate(N)]` | `vibrate(N)` | `$ shake_fx(...)` |
| 15 | `[TITLE title("…")]` | `title("…")` | `call overlay_screen("<bg>", "Chapter …") from _call_overlay_screen_K` |
| 16 | `【選択肢】label → scene N` | `selectItem("label",(0x01000000+N),cond,true)` | `menu:` (мелкий) или `$ sprite_choice([{char,text,target}])` (крупный) |
| 17 | `【デート】girl → scene N` | `dateItem("girl",(0x01000000+N))` | `$ portrait_choice([{char,text,target}])` → `label date_<girl>_1:` |
| 18 | `【デート進行】 → scene N` | `date(N,false,bgm)` | `jump`/`return` на продолжение основной линии |
| 19 | `【移動】place → scene N` | `moveItem("place",(0x01000000+N))` | `menu:` или `$ sprite_choice([...])` → `label <place>_ch1_<M>:` |
| 20 | `→ next scene N` | `next((0x01000000+N),true)` | `jump <label>` |
| 21 | `【好感度】girl ±N` | `like("girl", N)` | `$ update_sympathy(N, char_key="…")` |
| 22 | `[WAIT waitTime(ms)]` | `waitTime(ms,true)` | `pause(ms/1000)` |
| 23 | `[MOVIE movie(N)]` | `movie(N)` | ⚠️ **не реализовано** (см. `STRUCTURE_AGENT.md`) |
| 24 | `[COFFEE]` | `coffee()` | ⚠️ **не реализовано** — до появления реализации ставь `pause(...)` |
| 25 | — | `msgon/msgoff`, `beginSkip/endSkip` | не переносятся (окно текста управляется автоматически) |
| 26 | — | `item(...)` | `game/scripts/features/inventory.rpy` |
| 27 | — | `battle*`, `battleInit`, `battleEnemy` | `game/scripts/battle/*` |

### Словари

**Симпатия** — `like(девушка, N)` → `update_sympathy(N, char_key=…)`:

| PS2 | `char_key` | диапазон |
|---|---|---|
| ルイズ | `louise` (по умолчанию) | −100…+100 |
| ハルナ | `haruna` | там же |
| シエスタ | `siesta` | там же |
| キュルケ | `kirche` | там же |
| タバサ | `tabitha` | там же |
| アンリエッタ | `henrietta` | там же |

**Говорящие** → код символа (`game/characters.rpy`):

| PS2 | код |  | PS2 | код |
|---|---|---|---|---|
| サイト | `s` | | ギーシュ | `g` |
| ルイズ | `l` | | デルフリンガー | `d` |
| キュルケ | `k` | | オスマン | `o` |
| タバサ | `t` | | モンモランシー | `m` |
| シエスタ | `si` | | アンリエッタ | `h` |
| ハルナ | `ha` | | コルベール | `c` |
| мысли / `null` / `（…）` | `th` | | 「???」 до узнавания | `unk`, `unk_ha`, `unk_k` |
| 兵士Ａ/Ｂ, 将校 | `soldier` / `commander` | | 魔導士, 味方Ａ, 部下 | `mage` / `soldier` / `unds` |
| прочие NPC, 商人, 宿の主人, 猫… | ⚠️ *нет кода* → см. `STRUCTURE_AGENT.md` §6 | | | |

**dir=1A/1B/1C/2A/2B/2C/3A/3B** — код входа спрайта в PS2. В ремастере направление
слайдов считает сам `show_sprites` (`anim=`, `side=`), поэтому `dir` **информативен, но не
копируется буквально**. Смотрите эталон: там `anim="dissolve"` / `anim="slide"`.

**level** — 200 = фон, 80 = CG, 160 = спрайты, 0 = слой `white`. В Ren'Py порядок слоёв
задаёт `show_sprites` сам.

---

## 5. Голоса (voice) — полный workflow

Проверенный факт: **число `[voice N]` в `.rpy` (1154) ровно совпадает с числом «дырок»
в `transcriptions_ja_ru.csv` (1154)**, и первые «дырки» — 53,54,55,56 — это как раз
реплики пролога. То есть **`[voice N]` из PS2 = индекс строки в CSV = имя файла
`VOICE_ID.BIN_%08X.wav` (8 цифр, верхний регистр hex)**.

### Шаги на каждую реплику

1. Найди `[voice N]` в `chapters/*.txt` (или `(0x04000000 +N)` в `events_full`).
2. Посчитай hex: `VOICE_ID.BIN_%08X.wav` (например 4283 → `VOICE_ID.BIN_000010BB.wav`).
3. Найди строку в `D:\gameMake\ZnT-1\ZnT1\transcriptions_ja_ru.csv`:
   `filename,original,translation,status`
   * `original` — японская **расшифровка аудио (ASR)**, не канонический текст!
     Часто отличается от канона («そうだね» против «うん。そうだね。»).
     Поэтому **искать голос надо по ID, а не по тексту**.
   * `translation` — русская расшифровка (ссылка для переводчика).
   * CSV разбит секциями-закладками `## ch_0`, `# ch_1 louise`, `ch_1 kirche` — они помогают
     быстро найти блок нужной главы/героя.
4. Оригинал трека: `...\decoding\unpacked\VOICE_ID.BIN\VOICE_ID.BIN_%08X.STV`.
   Конвертер — `...\unpacked\SOUND_ID.BIN\autoDecodeSTV.py` (STV → wav).
5. Переименуй в `ch<N>[.<M>]_<spk>_<NNN>.ogg` и положи в `game/audio/voices/`.
   `<NNN>` — следующий свободный номер **внутри этого файла** для этого говорящего.
6. Вставь в `.rpy` строку `voice "ch<N>[.<M>]_<spk>_<NNN>"` непосредственно перед репликой.
7. **Удали использованную строку из CSV** — это принятая в репозитории практика
   (коммиты `preserve original csv transcription` → `remove used voices from transcription`,
   CSV — это очередь непортированного). *Запасной вариант:* вместо удаления поменяй
   `status` — согласуй с владельцем репозитория.

### Проверка после работы

* `voice "…"` в новых `.rpy` **не должны** ссылаться на несуществующий `.ogg`
  (в готовой главе 1 таких 0).
* `.ogg`, на которые никто не ссылается, — это брак; в главе 1 их 8 шт. из 1162.
* Реестр готовых соответствий: `output/_diagnostics/voice_scene_map.json`
  (`voice` → `scene` → `psv` → `ja`) — пересоздаётся `python crosswalk.py`.

---

## 6. Текст и переводы — куда писать

Английский — **базовый язык ремастера, он пишется прямо в сценарий**.
Японский и русский — через стандартную систему переводов Ren'Py.

```
game/chapters/<N>/script-ch<N>_<M>.rpy     ← EN-текст, voice, *_fx, menu, jump   (база)
game/tl/japanese/<bucket>.rpy              ← translate japanese strings:  old "EN" / new "JA"
game/tl/russian/<bucket>.rpy               ← translate russian strings:   old "EN" / new "RU"
```

**Бакеты `tl/<язык>/` (все лежат плоско):**

| файл | что туда идёт |
|---|---|
| `dialogs.rpy` | обычные реплики (`s "…"`, `l "…"`) — основной объём |
| `thoughs.rpy` | мысли (`th "…"`) |
| `choises.rpy` | тексты пунктов `menu:` / `*_choice` |
| `overlays.rpy` | тексты `call overlay_screen(...)` (заголовки глав/локаций) |
| `common.rpy` | строки экранов, кнопок, общего UI |
| `characters.rpy` | отображаемые имена персонажей |
| `options.rpy`, `screens.rpy` | прочее UI |

**Ключ `old` обязан дословно совпадать со строкой в сценарии** — иначе перевод молча
не применяется и в игре остаётся английский. Известные расхождения уже есть
(в `thoughs.rpy` часть `old` записана с дефисом вместо `—` и без акцентов:
`Francoise` против `Françoise`). **Если в японском режиме строка осталась английской —
чини `old` в `tl`, а не сценарий.**

**Правила японского (канон, `new` в `tl/japanese`):**
* брать дословно из `output/chapters/*.txt`;
* **склеивать** переносы строк реплики в одну строку;
* мысли остаются в полных скобках `（…）`; для EN/RU скобки не ставить
  (правило 8 из `PROMTS.md` — их рисует окно `th`);
* в `old` (EN) троеточие `......` → `...`, «-сан» и прочие обращения сохраняются.

**Проверка перед коммитом:** `renpy` перевод должен давать `new` для каждой новой
EN-строки **в обоих** языках; пропущенный `old` в `tl/russian` = реплика без перевода.

---

## 7. Ресурсы: как находить имена

### BGM — правило готово ✅
PS2 `[BGM bgm play=+K]` → файл `game/audio/bgm/t{K-1}.ogg`.
Доказательство и пофайловая сверка: `output/_diagnostics/bgm_check.txt`
(32 точных совпадения из 32 однозначных; гипотезы `tK` и `tK-1` набирают лишь 14 и 11).
Пример: `[BGM bgm play=+24]` → `new_music="t23"`.
`t1`,`t2` практически не используются (PS2 начинается с id 3), `t32` — музыка экрана
«конец главы», добавленного ремастером.

### SE — правила нет, портируется точечно ⚠️
PS2: `[SE seN play=+K]`, K ∈ 36..95, всего 35 разных id. В ремастере **только 9 файлов**
`game/audio/sfx/{blow,blow_2,close_door,door,knock_door,open_door,punch,read,take_sword}.ogg`
и всего 4 используются в главах: `take_sword` (ch1_1), `knock_door` (ch1_3/5/8),
`read` (ch1_8/10), `blow_2` (ch1_6). Большинство PS2-SE — щелчки UI/атмосфера,
их **не переносят**. Переноси только осмысленные (дверь, оружие, листание) и смотри,
как сделано в эталоне.

### Фоны / CG / спрайты — таблицы ещё нет ❌
`(0x02000000 +K)` — **единый** id-пространствo (доказано: спрайты занимают 302..1125,
фоны 1..1173, CG 1..1176, пересечений между «спрайты» и «фоны/CG» = 0), но **напрямую
на имя файла id не переводится** — индексы PNG в `unpacked/{SCENEDAT,NORMAL}.BIN`
не совпадают с id (нет ни 10..15 в SCENEDAT, ни 1..6 в NORMAL).

Что делать **до** того, как портировать новую главу:
1. Проверь, не появился ли справочник `image_id_map` (создаёт агент структуры,
   см. `STRUCTURE_AGENT.md` §5).
2. Если нет — определяй визуально: `stage` → один из `game/images/bg/*.webp` (65 шт.),
   `event` → `game/images/cg/*.webp` (41 шт.), `layN` → `game/images/chara/*.webp`
   (289 шт.), сверяясь с оригиналами `unpacked/SCENEDAT.BIN/*.PNG` (1104) и
   `unpacked/NORMAL.BIN/*.PNG` (335). Имена, уже задекларированные в `definitions.rpy`
   (179 `image`-инструкций) — первый источник.
3. Каждую новую пару **id → имя сразу записывай** в общий справочник, чтобы глава 2+
   не искала одно и то же заново.

### Что показывает эталон главы 1 (ориентируйся на это)
`$ fade_fx("forest", new_music="t18")` — фон + музыка разом;
`$ dissolve_fx("l_s_forest", type="cg")` — CG;
`$ show_sprites(("l 3 angry", "d 1"))` — спрайты;
`$ show_sprites("d 1", mode="big")` — крупный план;
`$ show_sprites(..., anim="slide")`, `center_front=True`, `raise_z=False`;
`$ hit_fx()`, `$ flash_fx(...)`, `$ shake_fx(...)`, `$ blow_fx(...)`, `$ fade_clear()`;
`$ update_sympathy(20, char_key="louise")`;
`call overlay_screen(bg, "Title", text_mode="black") from _call_overlay_screen_K`;
`play sound take_sword`; `pause(0.5)`; `jump ch1_2`.

Полные сигнатуры — `game/scripts/features/sf_effect.rpy`:
```
scene_fx(effect="fade", new_bg=None, duration=None, hide=None, window_hide=None,
         sprites=None, mode="normal", side=None, center_front=None, sound=None,
         hud=None, stop_music=False, music_fadeout=1.0, new_music=None,
         music_fadein=1.0, strength=None, bg_position="fullscreen", type="bg")
fade_fx(bg=None, duration=1.0, window_hide=True, **kwargs)     # alias effect="fade"
dissolve_fx(bg=None, duration=0.5, ...)                        # alias effect="dissolve"
flash_fx / hit_fx / blow_fx / shake_fx                         # аналогично
show_sprites(chars, mode="normal", anim_in, anim_out, side=None,
             center_front=None, hide_window=False, raise_z=True, anim=None, emote=None)
update_sympathy(value, char_key="louise", min_val=-100, max_val=100, up_sound=…, down_sound=…)
label overlay_screen(scene_name=None, title_text="", show_subtitle=False,
                     text_mode='beige', delay=2.0, isUseBlur=True, sound_path=None)
```
⚠️ У `call overlay_screen(...) from _call_overlay_screen_K` — **уникальный суффикс `K`**.
Каждый новый вызов должен получить новый номер, иначе Ren'Py упадёт на дубликате.

---

## 8. Порядок работы над одной главой

1. **Прочитай весь** `output/chapters/chapter_NN_*.txt` от начала до конца (это границы главы).
2. **Прочитай `events_full`** той же главы — там точные аргументы `set/next/selectItem/dateItem`.
3. Определи **структуру**: локации, `→ next`, ветки `【選択肢】`/`【デート】`/`【移動】`,
   ветки, уводящие в `extra scenes:` (эти сцены — из другой главы, но живут здесь же).
4. Разрежь на части (`script-ch<N>_M.rpy`), назови лейблы, свяжи `jump`.
5. Пиши по порядку: `*_fx` → `voice` → реплика → `menu`/`*_choice` → `jump`.
6. Параллельно добавляй EN в сценарий и `old/new` в оба `tl/`.
7. Портируй голоса (§5).
8. Прогони чек-лист §9.

**Очередность по репозиторию** (из истории git) — один коммит = одна порция работы:
`script-chN_M.rpy` + `tl/japanese/*` + `tl/russian/*` + `transcriptions_ja_ru.csv`
(удаление использованных строк). Голоса в git не попадают — они лежат в облачном
архиве (см. `game/INSTRUCTION.md`: `audio`, `gui`, `images`, `video` — «динамические» папки).

---

## 9. Чек-лист приёмки главы

- [ ] Каждая реплика из `output/chapters/chapter_NN_*.txt` есть в `.rpy` **в том же порядке**
      (сверка по количеству: глава N должна дать столько же строк, сколько `talk` в `chapter_map.txt`).
- [ ] Каждый `[BG stage …]` / `[EVENT_CG …]` / блок `[SPRITE …]` порождает `*_fx`/`show_sprites`.
- [ ] Каждый `[BGM play=+K]` → `t{K-1}`; ни один `t*` не взят «на глазок».
- [ ] Каждый `→ next scene` / `【…】` → конкретный `jump`/`menu`/`*_choice`; дыр в графе нет.
- [ ] Каждый `【好感度】X N` → `update_sympathy(N, char_key="…")`.
- [ ] `voice "…"` → существующий `.ogg` в `game/audio/voices/`; лишних ссылок нет.
- [ ] Каждая новая EN-строка имеет `old/new` **и** в `tl/japanese`, **и** в `tl/russian`
      (в правильном бакете §6).
- [ ] `old` дословно совпадает со строкой сценария.
- [ ] `call overlay_screen(...) from _call_overlay_screen_K` — все `K` уникальны.
- [ ] Все `label` уникальны в проекте (проверь `grep -r "^label "` по `game/chapters`).
- [ ] Нижняя часть последнего файла — `jump attention` (как в главе 1), если глава замыкает линию.
- [ ] Японский `new` — дословно из источника, переносы строк склеены, мысли в `（ ）`.
- [ ] Проект компилируется/запускается, текст в японском и русском режимах не «улетает» в EN.

---

## 10. Готовые инструменты и отчёты (`ZNT_TEST`)

Скрипты (запуск: `python <имя>` из `D:\gameMake\ZnT-1\ZNT_TEST`):

| скрипт | что даёт |
|---|---|
| `crosswalk.py` | **главный**: `.rpy` ↔ сцены PS2, `jump/call`, инвентарь `*_fx`, структура PS2 внутри сцен, `voice` → scene → PS2 id → JA |
| `resource_probe.py` | id BGM/SE/картинок, имена `tN` и `play sound` по файлам, раскладка `game/images` |
| `resource_probe2.py` | `level`, слои `set()`, значения `dir`, `trans()` |
| `bgm_check.py` | доказательство правила `t{K-1}` |
| `voice_csv_index.py` | сверка CSV с PS2-голосами («дырки» = портированные) |
| `line_grammar.py` | все формы строк `chapters/*.txt` + словарь говорящих |

Отчёты (`output/_diagnostics/`): `crosswalk.txt|json`, `voice_scene_map.json`,
`chapter_line_grammar.txt`, `resource_map.txt`, `resource_map2.txt`, `bgm_check.txt`,
`voice_csv_index.txt`, `voice_csv_status.txt`, `scene_label_crosswalk.txt`,
`correspondence.txt`.

Пересоздание всего: `python crosswalk.py && python resource_probe.py && python bgm_check.py`.

Базовая валидация самой выборки (не порта): `python verify_final.py` → `verify ok=True`.
