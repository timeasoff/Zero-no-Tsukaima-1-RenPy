# S1 — аудит покрытия tndl (T20261031-154035-97bf)

Канон: `ps2_source/events_full/chapter_NN_*.txt`, строки `TNDL`.
Якорь: голос триггер-реплики → `voice_id_map` → строка `voice "..."`
(+ `update_sympathy` для like-смежных, сужение по сцене,
`label chN` для `tndl(null)`). ch1 — контроль, ch6 — чужой WIP.

| источник | порт | TNDL в JA | в порте | stale | план | NO-ANCHOR | непарные | статус |
| 01 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | OK-PLAN |
| 02 | 1 | 32 | 32 | 0 | 0 | 0 | 0 | PASS |
| 03 | 2 | 35 | 0 | 0 | 35 | 0 | 0 | OK-PLAN |
| 04 | 3 | 36 | 0 | 17 | 36 | 0 | 1 | REVIEW |
| 05 | 4 | 23 | 0 | 2 | 23 | 0 | 1 | REVIEW |
| 06 | 5 | 32 | 0 | 32 | 32 | 0 | 0 | OK-PLAN |
| 07 | 6 | 13 | 0 | 0 | 0 | 0 | 0 | FOREIGN-WIP |
|---|---|---|---|---|---|---|---|---|

## chapter_01 -> chapters/0

- TNDL в JA: 1 (1xnull); в порте вызовов: 0; stale-комментариев: 0
- план вставок: 1; NO-ANCHOR: 0; непарные stale: 0

| src | scene | value | kind | якорь (файл:строка) | тип | voice | stale-комментарий |
|---|---|---|---|---|---|---|---|
| 6 | 5 | null | null_start | script-ch0.rpy:1 | label | - |  |

## chapter_02 -> chapters/1 — КОНТРОЛЬ (уже портирована)

- вызовов в порте: 32 (JA: 32); распределение: порт 17x-30, 14x+30, 1xnull / JA 17x-30, 14x+30, 1xnull
- пары `update_sympathy` → `tndl`: порт 25 (значения -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, +30, +30, +30, +30, +30, +30, +30, +30, +30, +30, +30) / JA like-смежные 25 (-30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, -30, +30, +30, +30, +30, +30, +30, +30, +30, +30, +30, +30)
- standalone: порт 6 (значения -30, -30, -30, +30, +30, +30) / JA 6 (-30, -30, -30, +30, +30, +30); null: порт 1 / JA 1
- структурный вердикт: **PASS**
- примечание: `voice_id_map.csv` не содержит ch1-строк (голосовой якорь для ch1 недоступен; отдельное наблюдение).

## chapter_03 -> chapters/2

- TNDL в JA: 35 (18x-30, 16x+30, 1xnull); в порте вызовов: 0; stale-комментариев: 0
- план вставок: 35; NO-ANCHOR: 0; непарные stale: 0

| src | scene | value | kind | якорь (файл:строка) | тип | voice | stale-комментарий |
|---|---|---|---|---|---|---|---|
| 6 | 68 | null | null_start | script-ch2_1.rpy:3 | label | - |  |
| 129 | 70 | +30 | like | script-ch2_1.rpy:132 | syn | ch2_l_007 |  |
| 166 | 71 | -30 | like | script-ch2_1.rpy:180 | syn | ch2_l_011 |  |
| 374 | 74 | -30 | like | script-ch2_1.rpy:407 | syn | ch2_l_025 |  |
| 397 | 75 | +30 | standalone | script-ch2_1.rpy:431 | dialogue | ch2_l_027 |  |
| 459 | 78 | -30 | like | script-ch2_2.rpy:47 | syn | ch2.2_l_002 |  |
| 480 | 79 | +30 | like | script-ch2_2.rpy:69 | syn | ch2.2_s_004 |  |
| 682 | 83 | -30 | like | script-ch2_2.rpy:283 | syn | ch2.2_si_005 |  |
| 834 | 87 | -30 | like | script-ch2_2.rpy:444 | syn | ch2.2_l_012 |  |
| 904 | 88 | +30 | like | script-ch2_2.rpy:518 | syn | ch2.2_l_021 |  |
| 1020 | 91 | +30 | like | script-ch2_3.rpy:105 | syn | ch2.3_l_009 |  |
| 1050 | 92 | -30 | like | script-ch2_3.rpy:149 | syn | ch2.3_k_013 |  |
| 1447 | 96 | +30 | like | script-ch2_3.rpy:455 | syn | ch2.3_l_031 |  |
| 1469 | 97 | -30 | like | script-ch2_3.rpy:483 | syn | ch2.3_k_032 |  |
| 1852 | 107 | +30 | like | script-ch2_4.rpy:238 | syn | ch2.4_l_016 |  |
| 1900 | 109 | -30 | like | script-ch2_4.rpy:287 | syn | ch2.4_l_018 |  |
| 2113 | 112 | +30 | like | script-ch2_4.rpy:508 | syn | ch2.4_l_035 |  |
| 2135 | 113 | -30 | like | script-ch2_4.rpy:536 | syn | ch2.4_l_038 |  |
| 2320 | 116 | +30 | standalone | script-ch2_5.rpy:82 | dialogue | ch2.5_s_183 |  |
| 2338 | 117 | -30 | like | script-ch2_5.rpy:101 | syn | ch2.5_ha_037 |  |
| 2774 | 126 | -30 | like | script-ch2_6.rpy:102 | syn | ch2.6_si_007 |  |
| 4051 | 1257 | +30 | like | script-ch2_4b.rpy:79 | syn | ch2.5_l_008 |  |
| 4072 | 1258 | -30 | like | script-ch2_4b.rpy:105 | syn | ch2.5_l_011 |  |
| 4206 | 1263 | -30 | standalone | script-ch2_4b.rpy:277 | dialogue | ch2.5_si_013 |  |
| 4240 | 1264 | +30 | like | script-ch2_4b.rpy:328 | syn | ch2.5_si_019 |  |
| 4346 | 1268 | -30 | standalone | script-ch2_4c.rpy:90 | dialogue | ch2.5_k_008 |  |
| 4370 | 1269 | +30 | like | script-ch2_4c.rpy:120 | syn | ch2.5_k_011 |  |
| 4446 | 1272 | -30 | like | script-ch2_4c.rpy:217 | syn | ch2.5_t_005 |  |
| 4492 | 1274 | +30 | like | script-ch2_4c.rpy:281 | syn | ch2.5_t_009 |  |
| 4580 | 1277 | -30 | like | script-ch2_4c.rpy:406 | syn | ch2.5_ha_008 |  |
| 4685 | 1282 | +30 | like | script-ch2_5b.rpy:55 | syn | ch2.5_ha_024 |  |
| 4821 | 1288 | -30 | standalone | script-ch2_5b.rpy:239 | dialogue | ch2.5_k_027 |  |
| 4843 | 1289 | +30 | standalone | script-ch2_5b.rpy:270 | dialogue | ch2.5_s_143 |  |
| 4959 | 1292 | -30 | like | script-ch2_5b.rpy:431 | syn | ch2.5_s_162 |  |
| 4996 | 1294 | +30 | like | script-ch2_5b.rpy:481 | syn | ch2.5_t_023 |  |

## chapter_04 -> chapters/3

- TNDL в JA: 36 (24x-30, 11x+30, 1xnull); в порте вызовов: 0; stale-комментариев: 17
- план вставок: 36; NO-ANCHOR: 0; непарные stale: 1

| src | scene | value | kind | якорь (файл:строка) | тип | voice | stale-комментарий |
|---|---|---|---|---|---|---|---|
| 6 | 137 | null | null_start | script-ch3_1.rpy:4 | label | - |  |
| 188 | 140 | -30 | like | script-ch3_1.rpy:157 | syn | ch3_l_004 |  |
| 358 | 143 | +30 | standalone | script-ch3_1.rpy:380 | dialogue | ch3_g_013 |  |
| 393 | 145 | -30 | standalone | script-ch3_1.rpy:419 | dialogue | ch3_s_028 |  |
| 505 | 148 | +30 | like | script-ch3_2.rpy:133 | syn | ch3.2_l_007 |  |
| 524 | 149 | -30 | like | script-ch3_2.rpy:159 | syn | ch3.2_l_009 |  |
| 541 | 150 | -30 | like | script-ch3_2.rpy:180 | syn | ch3.2_l_010 |  |
| 676 | 154 | +30 | like | script-ch3_2.rpy:396 | syn | ch3.2_l_027 |  |
| 709 | 155 | -30 | like | script-ch3_2.rpy:458 | syn | ch3.2_l_032 |  |
| 1019 | 165 | -30 | like | script-ch3_4.rpy:197 | syn | ch3.4_ha_020 |  |
| 1047 | 166 | -30 | like | script-ch3_4.rpy:242 | syn | ch3.4_si_019 |  |
| 1075 | 167 | +30 | standalone | script-ch3_4.rpy:292 | dialogue | ch3.4_s_017 |  |
| 1212 | 169 | -30 | like | script-ch3_5.rpy:35 | syn | ch3.5_l_002 |  |
| 1373 | 174 | -30 | like | script-ch3_5.rpy:255 | syn | ch3.5_l_011 |  |
| 1391 | 175 | +30 | like | script-ch3_5.rpy:279 | syn | ch3.5_l_013 |  |
| 1740 | 186 | -30 | like | script-ch3_6.rpy:152 | syn | ch3.6_k_006 | script-ch3_6.rpy:151 val=-30 OK |
| 1855 | 188 | -30 | like | script-ch3_6.rpy:285 | syn | ch3.6_l_008 | script-ch3_6.rpy:284 val=-30 OK |
| 1872 | 189 | -30 | like | script-ch3_6.rpy:316 | syn | ch3.6_l_010 | script-ch3_6.rpy:315 val=-30 OK |
| 2008 | 193 | -30 | like | script-ch3_7.rpy:71 | syn | ch3.7_l_003 | script-ch3_7.rpy:70 val=-30 OK |
| 2039 | 194 | -30 | like | script-ch3_7.rpy:127 | syn | ch3.7_l_004 | script-ch3_7.rpy:126 val=-30 OK |
| 2186 | 198 | +30 | like | script-ch3_7.rpy:394 | syn | ch3.7_ha_012 | script-ch3_7.rpy:393 val=+30 OK |
| 2206 | 199 | -30 | like | script-ch3_7.rpy:424 | syn | ch3.7_ha_014 | script-ch3_7.rpy:423 val=-30 OK |
| 2516 | 209 | -30 | like | script-ch3_8.rpy:156 | syn | ch3.8_l_006 | script-ch3_8.rpy:155 val=-30 OK |
| 2535 | 210 | -30 | like | script-ch3_8.rpy:185 | syn | ch3.8_l_008 | script-ch3_8.rpy:184 val=-30 OK |
| 3480 | 1298 | -30 | like | script-ch3_3.rpy:80 | syn | ch3.3_l_004 | script-ch3_3.rpy:79 val=-30 OK |
| 3717 | 1308 | -30 | like | script-ch3_3.rpy:450 | syn | ch3.3_k_009 | script-ch3_3.rpy:449 val=-30 OK |
| 3761 | 1310 | +30 | like | script-ch3_3.rpy:535 | syn | ch3.3_k_013 | script-ch3_3.rpy:534 val=+30 OK |
| 3836 | 1313 | -30 | like | script-ch3_3.rpy:654 | syn | ch3.3_s_058 | script-ch3_3.rpy:653 val=-30 OK |
| 3851 | 1314 | +30 | like | script-ch3_3.rpy:674 | syn | ch3.3_t_001 | script-ch3_3.rpy:673 val=+30 OK |
| 3955 | 1318 | -30 | like | script-ch3_3.rpy:857 | syn | ch3.3_s_076 | script-ch3_3.rpy:856 val=-30 OK |
| 3988 | 1320 | +30 | like | script-ch3_3.rpy:897 | syn | ch3.3_s_080 | script-ch3_3.rpy:896 val=+30 OK |
| 4208 | 1330 | -30 | standalone | script-ch3_5.rpy:796 | dialogue | ch3.5_s_054 |  |
| 4280 | 1334 | -30 | standalone | script-ch3_5.rpy:889 | dialogue | ch3.5_s_061 |  |
| 4312 | 1335 | +30 | standalone | script-ch3_5.rpy:948 | dialogue | ch3.5_s_067 |  |
| 4374 | 1338 | -30 | standalone | script-ch3_5.rpy:1030 | dialogue | ch3.5_s_072 |  |
| 4415 | 1340 | +30 | standalone | script-ch3_5.rpy:1086 | dialogue | ch3.5_s_076 |  |

**Непарные stale-комментарии (вручную):**
- script-ch3_8.rpy:199 val=-30 :: # [好感度] タバサ -15 (TNDL только для ルイズ: tndl(-30) не портируется; ルイズ -10 применён выше)

## chapter_05 -> chapters/4

- TNDL в JA: 23 (13x-30, 9x+30, 1xnull); в порте вызовов: 0; stale-комментариев: 2
- план вставок: 23; NO-ANCHOR: 0; непарные stale: 1

| src | scene | value | kind | якорь (файл:строка) | тип | voice | stale-комментарий |
|---|---|---|---|---|---|---|---|
| 6 | 219 | null | null_start | script-ch4_1.rpy:16 | label | - |  |
| 188 | 220 | +30 | like | script-ch4_1.rpy:348 | syn | ch4_l_006 |  |
| 223 | 222 | -30 | like | script-ch4_1.rpy:398 | syn | ch4_l_009 |  |
| 734 | 232 | +30 | like | script-ch4_2.rpy:687 | syn | ch4.2_l_040 |  |
| 758 | 233 | -30 | like | script-ch4_2.rpy:726 | syn | ch4.2_l_041 |  |
| 1036 | 237 | -30 | like | script-ch4_3.rpy:284 | syn | ch4.3_l_012 | script-ch4_3.rpy:283 val=-30 OK |
| 1439 | 248 | -30 | like | script-ch4_4.rpy:185 | syn | ch4.4_ha_006 |  |
| 1883 | 257 | +30 | like | script-ch4_5.rpy:459 | syn | ch4.5_s_012 |  |
| 1933 | 258 | -30 | like | script-ch4_5.rpy:506 | syn | ch4.5_l_023 |  |
| 3249 | 1343 | +30 | like | script-ch4_2.rpy:387 | syn | ch4.2_l_023 |  |
| 3286 | 1345 | -30 | like | script-ch4_2.rpy:451 | syn | ch4.2_l_027 |  |
| 3386 | 1348 | +30 | like | script-ch4_2b.rpy:101 | syn | ch4.2_si_014 |  |
| 3409 | 1349 | -30 | like | script-ch4_2b.rpy:136 | syn | ch4.2_si_016 |  |
| 3518 | 1354 | +30 | like | script-ch4_2b.rpy:311 | syn | ch4.2_k_008 |  |
| 3535 | 1355 | +30 | like | script-ch4_2b.rpy:337 | syn | ch4.2_k_009 |  |
| 3616 | 1358 | -30 | like | script-ch4_2b.rpy:456 | syn | ch4.2_t_009 |  |
| 3636 | 1359 | +30 | like | script-ch4_2b.rpy:485 | syn | ch4.2_t_010 |  |
| 3773 | 1363 | -30 | like | script-ch4_2b.rpy:688 | syn | ch4.2_ha_014 |  |
| 3915 | 1368 | -30 | standalone | script-ch4_4.rpy:493 | dialogue | ch4.4_s_017 |  |
| 3937 | 1369 | -30 | standalone | script-ch4_4.rpy:530 | dialogue | ch4.4_s_019 |  |
| 3959 | 1370 | -30 | standalone | script-ch4_4.rpy:567 | dialogue | ch4.4_s_021 |  |
| 4205 | 1378 | -30 | like | script-ch4_4.rpy:1016 | syn | ch4.4_si_017 |  |
| 4224 | 1379 | +30 | like | script-ch4_4.rpy:1046 | syn | ch4.4_si_019 |  |

**Непарные stale-комментарии (вручную):**
- script-ch4_3.rpy:20 val=-30 :: # TNDL tndl(-30) в 237 — не переносится (система не реализована, AGENTS §6).

## chapter_06 -> chapters/5

- TNDL в JA: 32 (21x-30, 10x+30, 1xnull); в порте вызовов: 0; stale-комментариев: 32
- план вставок: 32; NO-ANCHOR: 0; непарные stale: 0

| src | scene | value | kind | якорь (файл:строка) | тип | voice | stale-комментарий |
|---|---|---|---|---|---|---|---|
| 6 | 269 | null | null_start | script-ch5_1.rpy:40 | label | - | script-ch5_1.rpy:49 val=null OK |
| 119 | 271 | -30 | like | script-ch5_1.rpy:193 | syn | ch5_l_006 | script-ch5_1.rpy:194 val=-30 OK |
| 148 | 273 | -30 | like | script-ch5_1.rpy:244 | syn | ch5_l_007 | script-ch5_1.rpy:245 val=-30 OK |
| 518 | 281 | -30 | standalone | script-ch5_1.rpy:865 | dialogue | ch5_l_028 | script-ch5_1.rpy:867 val=-30 OK |
| 559 | 283 | +30 | like | script-ch5_1.rpy:941 | syn | ch5_ha_027 | script-ch5_1.rpy:942 val=+30 OK |
| 680 | 286 | -30 | like | script-ch5_2.rpy:206 | syn | ch5.2_ha_006 | script-ch5_2.rpy:207 val=-30 OK |
| 802 | 291 | -30 | like | script-ch5_2.rpy:423 | syn | ch5.2_k_008 | script-ch5_2.rpy:424 val=-30 OK |
| 830 | 292 | +30 | like | script-ch5_2.rpy:478 | syn | ch5.2_ha_010 | script-ch5_2.rpy:479 val=+30 OK |
| 1213 | 302 | -30 | like | script-ch5_3.rpy:212 | syn | ch5.3_l_005 | script-ch5_3.rpy:213 val=-30 OK |
| 1237 | 303 | +30 | like | script-ch5_3.rpy:259 | syn | ch5.3_k_004 | script-ch5_3.rpy:260 val=+30 OK |
| 1454 | 307 | -30 | like | script-ch5_3.rpy:659 | syn | ch5.3_h_007 | script-ch5_3.rpy:660 val=-30 OK |
| 1476 | 308 | -30 | like | script-ch5_3.rpy:689 | syn | ch5.3_h_009 | script-ch5_3.rpy:690 val=-30 OK |
| 1905 | 322 | -30 | like | script-ch5_5.rpy:296 | syn | ch5.5_l_018 | script-ch5_5.rpy:297 val=-30 OK |
| 1935 | 323 | +30 | standalone | script-ch5_5.rpy:356 | dialogue | ch5.5_s_007 | script-ch5_5.rpy:358 val=+30 OK |
| 2035 | 326 | -30 | like | script-ch5_5.rpy:553 | syn | ch5.5_l_024 | script-ch5_5.rpy:554 val=-30 OK |
| 2054 | 327 | +30 | standalone | script-ch5_5.rpy:586 | dialogue | ch5.5_s_014 | script-ch5_5.rpy:588 val=+30 OK |
| 2155 | 331 | -30 | like | script-ch5_5.rpy:752 | syn | ch5.5_k_011 | script-ch5_5.rpy:753 val=-30 OK |
| 4491 | 1384 | +30 | standalone | script-ch5_4.rpy:195 | dialogue | ch5.4_si_002 | script-ch5_4.rpy:197 val=+30 OK |
| 4530 | 1386 | -30 | standalone | script-ch5_4.rpy:271 | dialogue | ch5.4_s_008 | script-ch5_4.rpy:273 val=-30 OK |
| 4610 | 1390 | -30 | like | script-ch5_4.rpy:397 | syn | ch5.4_t_002 | script-ch5_4.rpy:398 val=-30 OK |
| 4628 | 1391 | +30 | like | script-ch5_4.rpy:427 | syn | ch5.4_t_003 | script-ch5_4.rpy:428 val=+30 OK |
| 4755 | 1394 | -30 | like | script-ch5_4.rpy:659 | syn | ch5.4_l_006 | script-ch5_4.rpy:660 val=-30 OK |
| 4795 | 1396 | -30 | like | script-ch5_4.rpy:735 | syn | ch5.4_ha_009 | script-ch5_4.rpy:736 val=-30 OK |
| 4890 | 1400 | -30 | like | script-ch5_4.rpy:899 | syn | ch5.4_k_007 | script-ch5_4.rpy:900 val=-30 OK |
| 4907 | 1401 | +30 | like | script-ch5_4.rpy:928 | syn | ch5.4_k_008 | script-ch5_4.rpy:929 val=+30 OK |
| 4986 | 1404 | -30 | standalone | script-ch5_4.rpy:1071 | dialogue | ch5.4_m_002 | script-ch5_4.rpy:1073 val=-30 OK |
| 5174 | 1410 | -30 | like | script-ch5_6.rpy:210 | syn | ch5.6_k_006 | script-ch5_6.rpy:211 val=-30 OK |
| 5193 | 1411 | +30 | like | script-ch5_6.rpy:243 | syn | ch5.6_ha_004 | script-ch5_6.rpy:244 val=+30 OK |
| 5266 | 1414 | +30 | like | script-ch5_6.rpy:364 | syn | ch5.6_l_001 | script-ch5_6.rpy:365 val=+30 OK |
| 5331 | 1416 | -30 | like | script-ch5_6.rpy:468 | syn | ch5.6_l_004 | script-ch5_6.rpy:469 val=-30 OK |
| 5422 | 1419 | -30 | standalone | script-ch5_6.rpy:632 | dialogue | ch5.6_s_023 | script-ch5_6.rpy:634 val=-30 OK |
| 5636 | 1426 | -30 | like | script-ch5_6.rpy:1027 | syn | ch5.6_t_010 | script-ch5_6.rpy:1028 val=-30 OK |

## chapter_07 -> chapters/6 — инвентарь, БЕЗ правок (чужой WIP)

| src_line | scene | value | триггер |
|---|---|---|---|
| 6 | 344 | null | ? (voice id None) |
| 161 | 346 | -30 | ルイズ (voice id 7307) |
| 184 | 347 | -30 | ルイズ (voice id 7309) |
| 353 | 351 | +40 | アンリエッタ (voice id 748) |
| 372 | 352 | -30 | ルイズ (voice id 7318) |
| 761 | 362 | -30 | アンリエッタ (voice id 778) |
| 1043 | 372 | -30 | ルイズ (voice id 7336) |
| 1061 | 373 | +40 | ルイズ (voice id 7338) |
| 1379 | 1432 | -30 | 味方Ａ (voice id 4224) |
| 1486 | 1437 | +40 | アンリエッタ (voice id 487) |
| 1553 | 1440 | -30 | サイト (voice id 10298) |
| 1665 | 1445 | -30 | サイト (voice id 10312) |
| 1688 | 1446 | +40 | サイト (voice id 10315) |
