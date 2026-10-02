---
name: voice-workflow
description: Полный workflow голосов: [voice N] из источника → id → .STV → .ogg в game/audio/voices/ → имя ch<N>_<spk>_<NNN> → строка voice "..." в сценарии; работа с transcriptions_ja_ru.csv (правило «идти по id, а не по тексту», удаление/пометка использованной строки); таблица говорящих в game/characters.rpy и правило добавления нового говорящего. Применять при озвучке любой части и при вопросах про голосовые файлы или говорящих.
---

# voice-workflow — голоса от `[voice N]` до строки `voice "…"`

## 1. Доказанное соответствие id

```text
[voice N] в ps2_source/chapters/*.txt   ==   (0x04000000 +N) в events_full
                                        ==   индекс строки в transcriptions_ja_ru.csv
                                        ==   имя файла VOICE_ID.BIN_%08X.wav / .STV
                                            (8 цифр hex, ВЕРХНИЙ регистр)
```

Пример: `[voice 4283]` → `4283 = 0x10BB` → `VOICE_ID.BIN_000010BB.STV` / `.wav`.

Доказательство (не гипотеза): число `voice "…"` в `.rpy` главы 1 = **1154** и число
«дырок» (удалённых использованных строк) в CSV = **1154**, причём первые дырки
`53, 54, 55, 56` — это реплики пролога (`ps2_source/_diagnostics/voice_csv_index.txt`).

⚠️ **Правило «по id, а не по тексту».** Колонка `original` в CSV — **ASR-расшифровка
аудио**, а не канонический текст: она часто отличается от JA («そうだね» против
«うん。そうだね。»). Искать голос по тексту реплики нельзя — только по `[voice N]`.

## 2. Где лежат файлы

```text
transcriptions_ja_ru.csv                     15 138 строк, UTF-8 с BOM — очередь непортированного
D:\gameMake\ZnT-1\ZNT_TEST\PS2_GAME\OriginalFiles\
  decoding\unpacked\VOICE_ID.BIN\VOICE_ID.BIN_<hex8>.STV    16 192 дорожки, id 0..16191
  decoding\unpacked\SOUND_ID.BIN\autoDecodeSTV.py            конвертер STV → wav
game\audio\voices\                           сюда кладутся готовые .ogg (медиа, в git не идут)
game\characters.rpy                          таблица говорящих (define + char_data)
```

Формат CSV — `filename,original,translation,status`:

```text
filename,original,translation,status
VOICE_ID.BIN_00000001.wav,相変わらずバカズラを下げているわね,"Ты все еще ведешь себя глупо, как обычно.",Успешно
```

* `original` — японская ASR-расшифровка (см. §1);
* `translation` — русская расшифровка, **справочный** материал для переводчика,
  не готовый перевод;
* `status` — статус расшифровки (обычно `Успешно`);
* файл разбит неформальными закладками-секциями: `## ch_0`, `# ch_1 louise`,
  `##ch_1 derflinger`, `# ch_1 haruna`, `# ch_1 kirche`, `# ch1 saito`, `##ch_1 npc`, …
  — они ускоряют поиск блока главы/героя, но **не являются структурой**: поле
  `filename` — единственный надёжный ключ.

## 3. Шаги на каждую реплику

1. Найти `[voice N]` в `ps2_source/chapters/*.txt` (или `(0x04000000 +N)` в `events_full/`).
2. Перевести в hex: `VOICE_ID.BIN_%08X` (4283 → `VOICE_ID.BIN_000010BB`).
3. Найти строку в `transcriptions_ja_ru.csv` по `filename`.
   Если строки нет — голос уже портирован (или отсутствует): свериться с
   `_diagnostics/voice_csv_index.txt` и существующими `voice "…"` в `game/chapters/`.
4. Оригинал: `...\VOICE_ID.BIN\VOICE_ID.BIN_<hex8>.STV` → конвертировать
   `autoDecodeSTV.py` (STV → wav).
5. Переименовать и положить в `game/audio/voices/`:
   * часть 1: `ch<N>_<spk>_<NNN>.ogg` → `ch1_s_001.ogg`;
   * части 2+: `ch<N>.<M>_<spk>_<NNN>.ogg` → `ch1.8_s_003.ogg`;
   * `<spk>` — код говорящего из `game/characters.rpy`;
   * `<NNN>` — **следующий свободный номер внутри этого файла для этого говорящего**,
     нумерация с `001`; не «следующий по всему проекту».
6. Вставить в `.rpy` строку `voice "ch<N>[.<M>]_<spk>_<NNN>"` **непосредственно перед
   репликой** (так сделано в эталонах `script-ch0.rpy` и `script-ch1_*.rpy`):

```renpy
    voice "ch1_s_001"
    s "…Hey, Louise-san, can you hear me?"
```

   Имя в строке `voice` без расширения `.ogg`.
7. **Удалить использованную строку из `transcriptions_ja_ru.csv`** — это принятая
   практика: CSV = очередь непортированного. Допустимая альтернатива — закомментировать
   строку (`#`) или поменять `status`; в файле уже есть такие пометки
   (напр. строка 5235: `# VOICE_ID.BIN_00001614.wav,…  ch1.6_l_016_2.wav`).
   Выбранный способ фиксируй в `reports/log.md`, если он отличается от «удалить».

### Проверка после работы

* `voice "…"` не должны ссылаться на несуществующий `.ogg` — это **E3**
  в `tools/check_project.py` (в готовой главе 1 таких 0);
* `.ogg`, на которые никто не ссылается, — брак (в главе 1: 8 из 1162) — это **W2**;
* если `game/audio/voices/` пуст/не установлен — E3 пропускается с пометкой
  `voices: … ogg check SKIPPED (audio not installed)`; это не «проверка пройдена».

## 4. Таблица говорящих

### 4.1 Что уже есть в `game/characters.rpy`

```renpy
define s  = Character(_("Saito"), color="#3874a3")
define l  = Character(_("Louise"), color="#fd7589")
define k  = Character(_("Kirche"), color="#e36566")
define t  = Character(_("Tabitha"), color="#b4dfec")
define c  = Character(_("Kolbert"), color="#5e5b51")
define h  = Character(_("Henrietta"), color="#782163")
define si = Character(_("Siesta"), color="#535a6a")
define ha = Character(_("Haruna"), color="#4b4d51")
define g  = Character(_("Guiche"), color="#f3e69d")
define d  = Character(_("Derflinger"), color="#9d996b")
define o  = Character(_("Osmond"), color="#ddd7d4")
define m  = Character(_("Montmorency"), color="#e2d79d")
define villager / commander / soldier / mage / unds      # NPC
define unk / unk_ha / unk_k                              # «???» до узнавания
define th = Character(None, what_italic=True, …, window_style='thought_window')  # мысли
```

### 4.2 PS2-имя → код (частоты — `_diagnostics/chapter_line_grammar.txt`)

| PS2 | код | реплик | PS2 | код | реплик |
|---|---|---|---|---|---|
| サイト | `s` | 7269 | ウェザリー | ⚠️ нет | 358 |
| ルイズ | `l` | 3353 | アキナ | ⚠️ нет | 249 |
| キュルケ | `k` | 1221 | モンモランシー | `m` | 244 |
| ハルナ | `ha` | 1081 | コルベール | `c` | 244 |
| シエスタ | `si` | 997 | デルフリンガー | `d` | 177 |
| タバサ | `t` | 792 | ギーシュ | `g` | 171 |
| アンリエッタ | `h` | 650 | オスマン | `o` | 151 |
| `null` / `（…）` | `th` | 104 | 味方Ａ/将校/魔導士 | `soldier`/`commander`/`mage` | 62/61/28 |
| 商人ＭＲ/商人 | ⚠️ нет | 13/11 | 兵士Ａ/兵士Ｂ | `soldier` | 6/5 |
| 情報屋/部下/猫/客 | ⚠️ нет | 5/4/4/3 | 男Ａ/男Ｂ/男Ｃ, 敵兵士ＥＳ, 宿の主人, 店主, 敵ＥＡ, どぶねずみ | ⚠️ нет | по 1–2 |

⚠️ = говорящий встречается в PS2, но кода в `characters.rpy` пока нет
(ウェザリー — 358 реплик, Акина — 249; в прологе Акина озвучена как `unk`).

### 4.3 Правило добавления нового говорящего

1. Выбрать короткий свободный код (проверить `grep -n "^define " game/characters.rpy`,
   чтобы не занять существующий и не совпасть с локальной переменной).
2. Добавить `define <code> = Character(_("Display Name"), color="#hex")` в
   `game/characters.rpy` — **до** того, как писать реплики этим говорящим:
   иначе `tools/check_project.py` даст **W4** `unknown speaker '…' (no define)`.
3. `_("…")` делает имя переводимым → добавить `old/new` в
   `game/tl/japanese/characters.rpy` **и** `game/tl/russian/characters.rpy`.
4. Если персонаж участвует в выборах (`portrait_choice`/`sprite_choice`) — завести
   запись в реестр `char_data`: `name`, опционально `color`, `description`,
   `portrait_choise` (путь к портрету), `sprite_choise` (тег image, напр. `"si 1"`).
5. «???» до узнавания персонажа → отдельный `unk_*` с цветом персонажа (образец
   `unk_ha`, `unk_k`).
6. Записать решение в `reports/log.md`, если код/имя выбирался наугад (статус
   `PROVISIONAL`, пока не подтверждён владельцем).

## 5. Порядок работы с голосом внутри части

```text
[voice N] из источника  →  id → hex → .STV → wav → .ogg (имя — §3, шаг 5)
                        →  строка voice "…" перед репликой
                        →  строка CSV удалена/помечена
                        →  python tools/check_project.py  (E3/W2)
```

Очередность в порции коммита: `script-ch<N>_<M>.rpy` + `tl/japanese/*` + `tl/russian/*`
+ `transcriptions_ja_ru.csv` + `reports/*` — одним коммитом (по явному подтверждению
пользователя; см. `project-constraints`).

## 6. Чего не делать

* Не подбирать голос по тексту реплики и не «сверяться по смыслу» — только id.
* Не переиспользовать `.ogg` под другой `[voice N]`: у каждой реплики свой id.
* Не оставлять `voice "…"` без файла и файл без `voice "…"` (E3 / W2).
* Не коммитить `.ogg` в git — `game/audio` входит в «динамические» папки
  (см. `game/INSTRUCTION.md` и скилл `assets`).
* Не менять `original` в CSV: это аудио-расшифровка, её правка искажает источник.
