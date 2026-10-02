# Скан манифеста голосов: ch1

Запуск: `2026-10-02 22:05`

| | значений |
|---|---:|
| voice-строк в сценарии | 1064 |
| [voice N] в источнике | 1067 |
| расхождение | -3 |

Источник: ps2_source/chapters/chapter_02_ゼロのルイズ.txt
Сценарии: game/chapters/1/script-ch1_1.rpy, game/chapters/1/script-ch1_2.rpy, game/chapters/1/script-ch1_3.rpy, game/chapters/1/script-ch1_4.rpy, game/chapters/1/script-ch1_5.rpy, game/chapters/1/script-ch1_6.rpy, game/chapters/1/script-ch1_7.rpy, game/chapters/1/script-ch1_8.rpy, game/chapters/1/script-ch1_9.rpy, game/chapters/1/script-ch1_10.rpy

## Результат: расхождение счётчиков — черновик НЕ записан

Причина может быть в пропущенной строке `voice "..."`, дополнительном `[voice N]` (extra scenes), несовпадении границ частей. Ни одна пара не считается доказанной: выровнять вручную и заполнить манифест вручную либо уточнить границы частей.

### Первые voice-строки сценария

- `ch1_s_001` game/chapters/1/script-ch1_1.rpy:34
- `ch1_l_001` game/chapters/1/script-ch1_1.rpy:37
- `ch1_s_002` game/chapters/1/script-ch1_1.rpy:40
- `ch1_l_002` game/chapters/1/script-ch1_1.rpy:45
- `ch1_s_003` game/chapters/1/script-ch1_1.rpy:48
- `ch1_s_004` game/chapters/1/script-ch1_1.rpy:51
- `ch1_l_003` game/chapters/1/script-ch1_1.rpy:56
- `ch1_s_005` game/chapters/1/script-ch1_1.rpy:61
- `ch1_l_004` game/chapters/1/script-ch1_1.rpy:64
- `ch1_l_005` game/chapters/1/script-ch1_1.rpy:67

### Первые [voice N] источника

- `5542` ps2_source/chapters/chapter_02_ゼロのルイズ.txt:32
- `10781` ps2_source/chapters/chapter_02_ゼロのルイズ.txt:33
- `5543` ps2_source/chapters/chapter_02_ゼロのルイズ.txt:34
- `10782` ps2_source/chapters/chapter_02_ゼロのルイズ.txt:35
- `5544` ps2_source/chapters/chapter_02_ゼロのルイズ.txt:37
- `10783` ps2_source/chapters/chapter_02_ゼロのルイズ.txt:40
- `10784` ps2_source/chapters/chapter_02_ゼロのルイズ.txt:42
- `5545` ps2_source/chapters/chapter_02_ゼロのルイズ.txt:44
- `10785` ps2_source/chapters/chapter_02_ゼロのルイズ.txt:48
- `5546` ps2_source/chapters/chapter_02_ゼロのルイズ.txt:51
