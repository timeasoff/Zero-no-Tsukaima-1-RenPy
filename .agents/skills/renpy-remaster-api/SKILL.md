---
name: renpy-remaster-api
description: Соответствие PS2 → Ren'Py для ремастера: references/ps2_to_renpy.csv, сигнатуры *_fx/show_sprites/update_sympathy/overlay_screen/portrait_choice/sprite_choice, именование лейблов и частей, уникальность from _call_overlay_screen_K, а также список того, что НЕ переносится. Применять при портировании событий в .rpy, написании и проверке игрового кода части.
---

# renpy-remaster-api — соответствие PS2 → Ren'Py

Скилл отвечает на вопрос «какой оператор Ren'Py соответствует этому событию PS2
и как его подписать». Эталоны — `game/chapters/0/script-ch0.rpy` и
`game/chapters/1/script-ch1_*.rpy`; **архитектурно они не переписываются**
(`AGENTS.md` §1, `project-constraints`).

## 1. Машиночитаемая таблица — `references/ps2_to_renpy.csv`

Колонки (шапка строки `# id,источник_chapters,источник_events_full,renpy,статус,примечание`):

```text
id,источник_chapters,источник_events_full,renpy,статус,примечание
20,"-> next scene N","next((0x01000000 +N),true)","jump <label>","OK","сильнейшая граница резки на части"
24,"[COFFEE]","coffee()","$ pause(1.0)","OK","сигнатуру не изобретать (решение: AGENTS.md §5)"
```

28 строк (id 1…28). **`статус`** — `OK` (переносится), `TOUCH` (точечно, см. скилл
`assets`), `DEFERRED` (не реализовано → пропуск с пометкой), `SKIP` (не переносится),
`CHECK` (сверить покрытие фичи перед главой). Читай CSV целиком перед портированием
новой главы; он — первичный справочник, скилл даёт только разъяснения и сигнатуры.

Ключевые строки (id → Ren'Py):

| id | источник (`chapters`) | Ren'Py |
|---|---|---|
| 1 | `голос：текст  [voice N]` | строка `voice "chN[_.M]_spk_NNN"` + реплика `s "…"` |
| 2 | реплика в `（…）` / говорящий `null` | `th "текст"` |
| 3 | `[BG stage image=+K, level=200]` | `$ fade_fx("имя")` / `$ dissolve_fx("имя")` |
| 4 | `[EVENT_CG event image=+K, level=80]` | `$ fade_fx("имя", type="cg")` (и `dissolve_fx`, `flash_fx`) |
| 6 | `[SPRITE layN image=+K, level=160, dir=1A]` | `$ show_sprites(("l 1 angry", "s 3 sad"))` |
| 10 | `[BGM bgm play=+K]` | `new_music="t{K-1}"` внутри `*_fx` **или** `play music t{K-1}` |
| 15 | `[TITLE title("…")]` | `call overlay_screen("<bg>", "Chapter …") from _call_overlay_screen_K` |
| 16 | `【選択肢】label → scene N` | `menu:` (мелкий) или `$ sprite_choice([...])` (крупный) |
| 17 | `【デート】girl → scene N` | `$ portrait_choice([...])` → `label date_<girl>_1:` |
| 19 | `【移動】place → scene N` | `menu:` или `$ sprite_choice([...])` → `label <place>_ch1_<M>:` |
| 20 | `→ next scene N` | `jump <label>` |
| 21 | `【好感度】girl ±N` | `$ update_sympathy(N, char_key="…")` |
| 22 | `[WAIT waitTime(ms)]` | `pause(ms/1000)` |
| 23 | `[MOVIE movie(N)]` | **не реализовано** → пропустить, пометка в отчёте части |
| 24 | `[COFFEE]` | `$ pause(1.0)` |

## 2. Сигнатуры (по коду `game/scripts/features/`, проверено чтением)

```python
# sf_effect.rpy
scene_fx(effect="fade", new_bg=None, duration=None, hide=None, window_hide=None,
         sprites=None, mode="normal", side=None, center_front=None, sound=None,
         hud=None, stop_music=False, music_fadeout=1.0, new_music=None,
         music_fadein=1.0, strength=None, bg_position="fullscreen", type="bg")
fade_fx   (bg=None, duration=1.0, window_hide=True, **kwargs)
dissolve_fx(bg=None, duration=0.5, window_hide=True, **kwargs)
flash_fx  (bg=None, duration=2.0, window_hide=True, **kwargs)
hit_fx    (bg=None, duration=0.35, **kwargs)
blow_fx   (bg=None, duration=0.7, **kwargs)
shake_fx  (bg=None, duration=0.7, **kwargs)

# show_sprites.rpy
show_sprites(chars, mode="normal", anim_in=<default "slide">, anim_out=<default = anim_in>,
             side=None, center_front=None, hide_window=False, raise_z=True,
             anim=None, emote=<default>)

# sympathy.rpy
update_sympathy(value, char_key="louise", min_val=-100, max_val=100,
                up_sound="audio/sfx/sympathy_up.wav", down_sound="audio/sfx/sympathy_down.wav")

# overlay_screen.rpy (label, не def)
label overlay_screen(scene_name=None, title_text="", show_subtitle=False,
                     text_mode='beige', delay=2.0, isUseBlur=True, sound_path=None)

# portrait_choises.rpy (вызывается как $ …)
portrait_choice(choices, music=CHOICE_DEFAULT_MUSIC, background=PORTRAIT_CHOICE_BG,
                bg_position=PORTRAIT_CHOICE_BG_POS)
sprite_choice (choices, music=CHOICE_DEFAULT_MUSIC, background=SPRITE_CHOICE_BG,
               bg_position=SPRITE_CHOICE_BG_POS)
```

`value` в `update_sympathy` — **дельта** (не абсолют): `$ update_sympathy(20, char_key="louise")`
прибавляет 20 к текущему, зажато в `min_val…max_val`.

`portrait_choice`/`sprite_choice` делают `renpy.call(target)` (а **не** `jump`):
выбранный `label` обязан заканчиваться `return`, тогда выполнение вернётся на строку
после `$ …_choice(...)` (см. комментарии в `portrait_choises.rpy:196` и `:218`).

### Реальные вызовы из эталона

```renpy
$ fade_fx("town_square_night", sprites=("soldier 1", "soldier 1"))     # ch0
$ dissolve_fx("forest", new_music="t18")                               # ch1_1
$ dissolve_fx("l_s_forest", type="cg")                                 # ch1_1
$ show_sprites(("soldier 1 sad", "soldier 1 angry "), raise_z=False)   # ch0
$ show_sprites("s 1", mode="big")                                      # ch1_1
$ flash_fx("terrorist2", type="cg")                                    # ch0
$ shake_fx(...)                                                        # vibrate
$ update_sympathy(20, char_key="tabitha")                              # ch1_8
call overlay_screen("overlay", "Chapter One: \"Louise of Zero\"", isUseBlur=False,
                    text_mode="black") from _call_overlay_screen_4     # ch1_1
```

### CG и спрайты — первый CG через `fade_fx`

Если перед появлением CG на экране есть спрайты, **первый CG показывается через
`fade_fx`**, а не `dissolve_fx`: `fade` — покрывающий переход (`hide`/`hud` по умолчанию
`True`), поэтому спрайты исчезают сами. У `dissolve` `hide=False` — спрайты останутся
поверх картинки. Дальнейшие CG этой же серии можно показывать `dissolve_fx` (спрайтов на
экране уже нет). В источнике такие первые CG — fade, не crossfade.
Пример: `game/chapters/2/script-ch2_3.rpy` стр. 43 и 186.

### `from _call_overlay_screen_K` — уникальность

* Каждый `call overlay_screen(...)` в `.rpy` получает **собственный** суффикс `K`;
  дубликат падает при компиляции (проверяется как **E2** в `tools/check_project.py`).
* Заняты `1…6` (`_call_overlay_screen`, `_1`, `_2`, `_3` в `script-ch0.rpy`;
  `_4`, `_5` в `script-ch1_1.rpy`; `_6` в `script-ch1_2.rpy`) → **следующий свободный — 7**.
  Точный текущий максимум всегда смотри в отчёте `reports/check_project.md`
  (`overlay K: max=… next_free=…`).
* Есть старые вызовы вида `from _call_overlay_screen_battle_0` и `from _call_intro_1` —
  их regex E2 не ловит; **новые формы не плоди**, используй строго `_call_overlay_screen_<число>`.

### Условия и выборы — образцы

```renpy
# мелкий выбор (【選択肢】) — ch1_1
$ choise_result = None
menu:
    "I thoughts it's good!":
        $ choise_result = "good"
    "I don't care.":
        $ choise_result = "neutral"
    "It's terrible!":
        $ choise_result = "bad"
if choise_result == "good":
    ...
elif choise_result == "neutral":
    ## симпатия луизы не меняется
    ...
else:
    "ERR"

# крупный выбор локации (【移動】) — ch1_8
$ sprite_choice([
    {"char": "tabitha",      "text": "Library",     "target": "library_ch1_8"},
    {"char": "kirche",      "text": "Kirche's Room", "target": "k_room_ch1_8"},
    {"char": "haruna",      "text": "Louise's Room", "target": "l_room_ch1_8"},
    {"text": "Hallway",      "target": "hallway_ch1_8"},
])
jump ch1_9
```

`target` — имя `label`, оно должно существовать (проверяется **E7**).

## 3. Именование (принятый стандарт, не изобретать)

```text
файлы      game/chapters/<N>/script-ch<N>_1.rpy, script-ch<N>_2.rpy, …
           (пролог — script-ch0.rpy)
лейблы     ch<N> — часть 1; ch<N>_2, ch<N>_3, … — остальные
локации    <loc>_ch<N>_<M>   si_room_ch1_3, hallway_ch1_8, library_ch1_8,
           l_room_ch1_8, k_room_ch1_8
даты       date_<girl>_1     date_louise_1, date_siesta_1, date_tabitha_1, …
голоса     ch<N>_<spk>_<NNN>          (часть 1)
           ch<N>.<M>_<spk>_<NNN>      (части 2+; пример ch1.8_s_003)
связка     последний оператор части — jump ch<N>_<M+1>
           нижняя часть последней части главы — jump attention
```

`call overlay_screen(...) from _call_overlay_screen_K` — `K` уникален **во всём проекте**.

## 4. Что НЕ переносится и чем заменяется

| вызов PS2 | решение |
|---|---|
| `waitAction`, `waitSEStop`, `waitLoad`, `sync`, `create`, `setZoom`, `setRotate`, `setAffineOrigin`, `swapLayers`, `screenShow`, `msgon/msgoff`, `beginSkip/endSkip` | не переносятся; одна строка в отчёте части (чтобы не пересматриваться на каждой главе) |
| `movie(N)` (`[MOVIE movie(N)]`) | **не реализовано** → пропустить, пометка `MOVIE not ported` в отчёте части, если видеофайл не добавлен (есть только `renpy.movie_cutscene("video/intro.webm")` в `script.rpy`) |
| `coffee()` (`[COFFEE]`) | `$ pause(1.0)`; сигнатуру не изобретать |
| `item(...)` | `game/scripts/features/inventory.rpy` — сверить покрытие перед главой (статус `CHECK`) |
| `battle*`, `battleInit`, `battleEnemy` | `game/scripts/battle/*` — сверить покрытие перед главой (статус `CHECK`) |
| `[LAYER white …]` | вспышка → `flash_fx`; `[LAYER lay0 …]` (994 вызова) → `flash_fx`/переход по образцу эталона; точечные `x=/y=/setPos/setOpacity/setLevel` не копируются |
| `[TRANS trans("crossfade", N)]` | встроен в `*_fx(duration=N/1000)`; других переходов в игре нет |
| `[SE seN play=+K]` | `play sound <имя>` — точечно, см. скилл `assets` |
| `[VIBRATE vibrate(N)]` | `$ shake_fx(...)` |

`waitTime(ms)` → `pause(ms/1000)` переносится (строка 22 CSV).

## 5. `dir`, `level`, `x/y` — информативны, но не копируются

* `dir=1A/1B/1C/2A/2B/2C/3A/3B` — код входа спрайта в PS2; направление слайдов в
  ремастере считает сам `show_sprites` (`anim=`, `side=`). Смотрите эталон: там
  `anim="dissolve"` / `anim="slide"`.
* `level`: 200 = фон, 80 = CG, 160 = спрайты, 0 = слой `white`. Порядок слоёв в
  Ren'Py задаёт `show_sprites` сам.
* Точечные `[SPRITE lay5 x=224, y=0]` → `show_sprites(..., side="left"/"right")`;
  сдвиг обычно опускается.

## 6. Словари

**Симпатия** `like(девушка, N)` → `update_sympathy(N, char_key=…)`; `char_key` только
из набора шести героинь (`sympathy_characters`): `louise` (по умолчанию), `haruna`,
`siesta`, `kirche`, `tabitha`, `henrietta`; диапазон −100…+100.

**Говорящие → код символа** (`game/characters.rpy`): サイト→`s`, ルイズ→`l`, キュルケ→`k`,
タバサ→`t`, コルベール→`c`, アンリエッタ→`h`, シエスタ→`si`, ハルナ→`ha`, ギーシュ→`g`,
デルフリンガー→`d`, オスマン→`o`, モンモランシー→`m`, мысли/`null`/`（…）`→`th`,
???-до-узнавания→`unk`, `unk_ha`, `unk_k`; NPC: 兵士Ａ/Ｂ→`soldier`, 将校→`commander`,
魔導士→`mage`, 部下→`unds`. Говорящего без кода заводи по правилу скилла `voice-workflow`
(таблица говорящих).

## 7. Порядок действий при портировании события

1. Найти событие в `ps2_source/chapters/`, уточнить аргументы в `events_full/`.
2. Свериться со строкой `references/ps2_to_renpy.csv` (статус → можно/точечно/нельзя).
3. Взять сигнатуру из §2 этого скилла, имя ассета — из `references/image_id_map.csv`
   (`python tools/build_image_id_map.py` обновляет справочник), BGM — только `t{K-1}`.
   Если у id ещё нет заполненного `filename` — пиши **заглушку самим id**:
   `$ fade_fx("id(1145)")`, `$ dissolve_fx("id(148)", type="cg")`. Имя «на глазок»
   запрещено; замена после заполнения справочника —
   `python tools/replace_bg_placeholders.py --apply` (ловят E10/W6).
4. Написать оператор в порядке: `*_fx` → `voice` → реплика → `menu`/`*_choice` → `jump`.
5. Прогнать `python tools/check_project.py` (E1/E2/E7/E10 ловят ошибки кода).
