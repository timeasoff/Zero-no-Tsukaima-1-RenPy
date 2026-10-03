---
name: voice-workflow
description: Полный workflow голосов: [voice N] из источника → id → дорожка в wav_source/ → имя ch<N>_<spk>_<NNN> → строка voice "..." в сценарии + пара voice_name,voice_id в references/voice_id_map.csv → на финальном этапе части tools/media/audio_converter.py (check / convert --apply) создаёт .ogg в game/audio/voices/; scan сверяет сценарий с [voice N] по порядку. Работа с transcriptions_ja_ru.csv (правило «идти по id, а не по тексту», удаление/пометка использованной строки); таблица говорящих в game/characters.rpy и правило добавления нового говорящего. Применять при озвучке любой части и при вопросах про голосовые файлы, wav_source, манифест голосов или говорящих.
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
wav_source/                                        ВСЕ неиспользованные дорожки,
                                                   имя: "[<префикс> ]VOICE_ID.BIN_<hex8>.wav"
references/voice_id_map.csv                        манифест: voice_name → voice_id
transcriptions_ja_ru.csv                           ASR-расшифровки (очередь непортированного)
D:\gameMake\ZnT-1\ZNT_TEST\PS2_GAME\OriginalFiles\
  decoding\unpacked\VOICE_ID.BIN\VOICE_ID.BIN_<hex8>.STV    16 192 дорожек, id 0..16191
  decoding\unpacked\SOUND_ID.BIN\autoDecodeSTV.py            конвертер STV → wav
game\audio\voices\                                 сюда кладутся готовые .ogg (медиа, в git не идут)
tools\media\audio_converter.py                     check / convert / scan (см. §3.5)
game\characters.rpy                                таблица говорящих (define + char_data)
```

**`wav_source/` — основной источник дорожек:** 15 055 файлов, id покрывают все
нероптированные главы (`chapter_03`…`chapter_29`, `chapter_90` целиком). Не хватает
только уже сконвертированных дорожек (главы 0/1, `extra/sp_l1`) и двух id —
`4227` (chapter_18), `10373` (chapter_91): их нет ни в `wav_source`, ни как файлов —
это «**нет аудио**», отмечать в отчёте части. Неразобранный файл `yo-saito.wav`
(без id) инструментом пропускается и попадает в отчёт.

Формат CSV — `filename,original,translation,status`:

```text
filename,original,translation,status
VOICE_ID.BIN_00000001.wav,相変わらずバカズラを下げているわね,"Ты все еще ведешь себя глупо, как обычно.",Успешно
```

- `original` — японская ASR-расшифровка (см. §1);
- `translation` — русская расшифровка, **справочный** материал для переводчика,
  не готовый перевод;
- `status` — статус расшифровки (обычно `Успешно`);
- файл разбит неформальными закладками-секциями: `## ch_0`, `# ch_1 louise`,
  `##ch_1 derflinger`, `# ch_1 haruna`, `# ch_1 kirche`, `# ch1 saito`, `##ch_1 npc`, …
  — они ускоряют поиск блока главы/героя, но **не являются структурой**: поле
  `filename` — единственный надёжный ключ.

## 3. Шаги на каждую реплику

1. Найти `[voice N]` в `ps2_source/chapters/*.txt` (или `(0x04000000 +N)` в `events_full/`).
2. Перевести в hex: `VOICE_ID.BIN_%08X` (4283 → `VOICE_ID.BIN_000010BB`).
3. Найти строку в `transcriptions_ja_ru.csv` по `filename`.
   Если строки нет — голос уже портирован (или отсутствует): свериться с
   `_diagnostics/voice_csv_index.txt` и существующими `voice "…"` в `game/chapters/`.
4. Проверить дорожку: файл `wav_source/[<префикс> ]VOICE_ID.BIN_<hex8>.wav` существует?
   - **да** — переходим к шагу 5 ( дорожка переименовывается не вручную, а конвертером );
   - **нет** — свериться с `transcriptions_ja_ru.csv` и
     `_diagnostics/voice_csv_index.txt`; при необходимости декодировать `.STV`
     (`autoDecodeSTV.py`) и положить wav в `wav_source/` с именем по id;
   - и это невозможно — это «**нет аудио**»: строка в манифесте всё равно пишется,
     а случай обязательно перечисляется в отчёте части (см. §3.5, `missing_wav`).
5. Задать имя строки `voice`:
   - часть 1: `ch<N>_<spk>_<NNN>` → `ch1_s_001`;
   - части 2+: `ch<N>.<M>_<spk>_<NNN>` → `ch1.8_s_003`;
   - `<spk>` — код говорящего из `game/characters.rpy`;
   - `<NNN>` — **следующий свободный номер внутри этого файла для этого говорящего**,
     нумерация с `001`; не «следующий по всему проекту».
6. Вставить в `.rpy` строку `voice "ch<N>[.<M>]_<spk>_<NNN>"` **непосредственно перед
   репликой** (так сделано в эталонах `script-ch0.rpy` и `script-ch1_*.rpy`):

```renpy
    voice "ch1_s_001"
    s "…Hey, Louise-san, can you hear me?"
```

Имя в строке `voice` без расширения `.ogg`. 7. Добавить пару в манифест `references/voice_id_map.csv` — одна строка CSV:

```csv
ch1_s_001,5542,,
```

(`voice_name,voice_id` обязательны; `wav_file` — только если дорожка лежит в
`wav_source` под другим именем, `notes` — сомнения/источник). Без этой строки
`.ogg` не будет создан, а `check` покажет раздел «нет в манифесте». 8. **Удалить использованную строку из `transcriptions_ja_ru.csv`** — это принятая
практика: CSV = очередь непортированного. Допустимая альтернатива — закомментировать
строку (`#`) или поменять `status`; в файле уже есть такие пометки
(напр. строка 5235: `# VOICE_ID.BIN_00001614.wav,…  ch1.6_l_016_2.wav`).
Выбранный способ фиксируй в `reports/log.md`, если он отличается от «удалить».

### 3.5 Финальный этап части: конвертер

`.ogg` создаются **одним прогоном**, когда реплики части готовы и все пары
имя↔id проставлены в манифесте (не поштучно при портировании):

```text
python tools/media/audio_converter.py check            # сверка -> reports/voice_check.md
python tools/media/audio_converter.py convert --apply  # wav_source -> game/audio/voices/
                                                        # -> reports/voice_convert.md
```

- порядок: портирование → манифест → **`convert --apply`** → `tools/check_project.py`
  (иначе E3 «voice без ogg») → отчёт части;
- `check` возвращает `RESULT: ISSUES`, если есть строки без манифеста, без
  дорожки или манифест без `voice_id`, и печатает точные файлы и строки;
- **предупреждения** (говорящий без `define`, неразобранный файл `wav_source`,
  неиспользуемая строка манифеста) прогон не блокируют (`RESULT: OK`), но
  **обязательно переносятся в отчёт части** — это и есть сигнал «нет
  зарегистрированного персонажа/файла»;
- `convert` идемпотентен: созданные `.ogg` пропускаются; ограничение прогона —
  `--only ch3` (подстрока имени), `--chapter 3`, `--jobs 4`, `--limit N` (тест),
  `--out <dir>` (проверка в песочнице);
- `scan --chapter N` — вспомогательное сопоставление «строка `voice` ↔ `[voice N]`»
  строго по порядку: при равных счётчиках пишет черновик
  `reports/voice_map_draft_ch<N>.csv` (**проверить и перенести** в манифест —
  черновик не канон), при расхождении не пишет ничего и объясняет причину в
  `reports/voice_scan_ch<N>.md`;
- отчёты инструмента — **еvidence**, а не вердикт: решение по каждому разделу
  принимается по правилам §5 `AGENTS.md` (classification + disposition).

### Проверка после работы

- `voice "…"` не должны ссылаться на несуществующий `.ogg` — это **E3**
  в `tools/check_project.py` (в готовой главе 1 таких 0);
- `.ogg`, на которые никто не ссылается, — брак (в главе 1: 8 из 1162) — это **W2**;
- сверка без записи — `audio_converter.py check` → `reports/voice_check.md`;
- если `game/audio/voices/` пуст/не установлен — E3 пропускается с пометкой
  `voices: … ogg check SKIPPED (audio not installed)`; это не «проверка пройдена».

## 4. Таблица говорящих

### 4.1 Что уже есть в `game/characters.rpy`

```renpy
define s  = Character(_("Saito"), color="#3874a3")
define l  = Character(_("Louise"), color="#fd7589")
define k  = Character(_("Kirche"), color="#e36566")
define t  = Character(_("Tabitha"), color="#b4dfec")
define c  = Character(_("Colbert"), color="#5e5b51")
define h  = Character(_("Henrietta"), color="#782163")
define si = Character(_("Siesta"), color="#535a6a")
define ha = Character(_("Haruna"), color="#4b4d51")
define g  = Character(_("Guiche"), color="#f3e69d")
define d  = Character(_("Derflinger"), color="#9d996b")
define o  = Character(_("Osmond"), color="#ddd7d4")
define m  = Character(_("Montmorency"), color="#e2d79d")
define villager / commander / soldier / mage / unds      # NPC
define w / ak / merchant / informant / cat / customer    # NPC, добавлены заранее
define man_a / man_b / man_c / innkeeper / shopkeeper    #   (PROVISIONAL, см. журнал)
define unk / unk_ha / unk_k                              # «???» до узнавания
define th = Character(None, what_italic=True, …, window_style='thought_window')  # мысли
```

### 4.2 PS2-имя → код (частоты — `_diagnostics/chapter_line_grammar.txt`)

| PS2                              | код                       | реплик | PS2                | код                          | реплик   |
| -------------------------------- | ------------------------- | ------ | ------------------ | ---------------------------- | -------- |
| サイト                           | `s`                       | 7269   | ウェザリー         | `w` ⚠                        | 358      |
| ルイズ                           | `l`                       | 3353   | アキナ             | `ak` ⚠                       | 249      |
| キュルケ                         | `k`                       | 1221   | モンモランシー     | `m`                          | 244      |
| ハルナ                           | `ha`                      | 1081   | コルベール         | `c`                          | 244      |
| シエスタ                         | `si`                      | 997    | デルフリンガー     | `d`                          | 177      |
| タバサ                           | `t`                       | 792    | ギーシュ           | `g`                          | 171      |
| アンリエッタ                     | `h`                       | 650    | オスマン           | `o`                          | 151      |
| `null` / `（…）`                 | `th`                      | 104    | 味方Ａ/将校/魔導士 | `soldier`/`commander`/`mage` | 62/61/28 |
| 商人ＭＲ/商人                    | `merchant` ⚠              | 13/11  | 兵士Ａ/兵士Ｂ      | `soldier`                    | 6/5      |
| 情報屋                           | `informant` ⚠             | 5      | 部下               | `unds`                       | 4        |
| 猫                               | `cat` ⚠                   | 4      | 客                 | `customer` ⚠                 | 3        |
| 男Ａ/男Ｂ/男Ｃ                   | `man_a`/`man_b`/`man_c` ⚠ | по 1–2 | 宿の主人 / 店主    | `innkeeper`/`shopkeeper` ⚠   | по 1–2   |
| 敵兵士ＥＳ / 敵ＥＡ / どぶねずみ | ⚠️ **нет**                | по 1–2 |                    |                              |          |

⚠ = код есть, но имя/код **PROVISIONAL** (выбраны по роли в JA-строке, в
`dictionary.md` нет) — сверить при первых репликах и указать персонажа в отчёте
части даже после регистрации. `敵兵士ＥＳ`/`敵ＥＡ`/`どぶねずみ` не регистрировались —
завести по §4.3 при встрече. В прологе Акина озвучена как `unk`.
⚠️ = кода нет: `tools/check_project.py` даст **W4**, зарегистрировать по §4.3
**до** первой реплики этим говорящим.

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
[voice N] из источника → id → дорожка в wav_source/ (или .STV → wav → wav_source)
                       → имя voice "ch<N>[.<M>]_<spk>_<NNN>" перед репликой
                       → строка voice_name,voice_id в references/voice_id_map.csv
                       → строка CSV удалена/помечена
                       === финальный этап части (§3.5) ===
                       → audio_converter.py convert --apply  (.ogg в game/audio/voices/)
                       → audio_converter.py check            (reports/voice_check.md)
                       → python tools/check_project.py       (E3/W2)
                       → в отчёт части: нет аудио / нет пары / незарегистрированные
```

Очередность в порции коммита: `script-ch<N>_<M>.rpy` + `tl/japanese/*` + `tl/russian/*`

- `transcriptions_ja_ru.csv` + `references/voice_id_map.csv` + `reports/*` — одним
  коммитом (по явному подтверждению пользователя; см. `project-constraints`).

## 6. Чего не делать

- Не подбирать голос по тексту реплики и не «сверяться по смыслу» — только id.
- Не переиспользовать `.ogg` под другой `[voice N]`: у каждой реплики свой id;
  дубль имени voice в сценарии — признак ошибки (так был пойман `ch1.8_s_013-3`).
- Не оставлять `voice "…"` без файла и файл без `voice "…"` (E3 / W2).
- Не создавать `.ogg` вручную (конвертацией в обход манифеста): пара
  `voice_name,voice_id` → `references/voice_id_map.csv`, конвертация — общим
  прогоном `audio_converter.py convert --apply` на финальном этапе.
- Не объявлять часть готовой без `audio_converter.py check` → `RESULT: OK` и без
  перенесения его предупреждений в отчёт части.
- Не коммитить `.ogg` в git — `game/audio` входит в «динамические» папки
  (см. `game/INSTRUCTION.md` и скилл `assets`).
- Не менять `original` в CSV: это аудио-расшифровка, её правка искажает источник.
