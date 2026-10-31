#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S2 / T20261031-015233-a0c8: дозакрытие ch6 WIP.

1) E4/E5: синхронизация 8 old в tl/japanese/thoughs.rpy и tl/russian/thoughs.rpy
   (WIP снял `_`-префиксы и `(...)`-скобки в скрипте ch6_1/ch6_2, old не синхронизированы).
2) RU-нормализация: снять `_..._` с 3 new (ch6_344_th_001..003) — конвенция
   tl/russian/thoughs: мысли без маркеров (прецедент WIP для ch6_2 + чистые строки ch5_5).
3) E11: tag-dedup 11 коротких ch6_2 строк — hidden-теги {#ch6_2_dNNN} в скрипте
   и в tl old (ja + ru), new-строки не трогать.
4) tndl: 13 событий по инвентарю reports/tndl_port_fix.md §6 (канон events_full/chapter_07):
   tndl(None) после label ch6; вставки после anchor-реплики (voice-имена из voice_id_map).

JA-new не редактируются (правило AGENTS §5). Mismatch （） в 4 ch6_2 thought-JA-new —
по флагам в log.md, сюда не входит.
"""
import re
from pathlib import Path

ROOT = Path("/workspace")
OK = []

def fix_file(rel, pairs, expect=None):
    p = ROOT / rel
    txt = p.read_text(encoding="utf-8")
    n = 0
    for old_s, new_s in pairs:
        c = txt.count(old_s)
        if c != 1:
            raise SystemExit(f"FAIL {rel}: {c!r} occurrences of {old_s[:60]!r} (expect 1)")
        txt = txt.replace(old_s, new_s)
        n += 1
    if expect is not None and n != expect:
        raise SystemExit(f"FAIL {rel}: applied {n}, expect {expect}")
    p.write_text(txt, encoding="utf-8")
    OK.append(f"{rel}: {n} правок")

# ---------- 1) E4/E5: old-синхронизация в tl/thoughs ----------
TH4_CH6_1 = [
    ('old "_It has been several days since the play ended. We still haven\'t found any clues about the bomber.{#ch6_344_th_001}"',
     'old "It has been several days since the play ended. We still haven\'t found any clues about the bomber.{#ch6_344_th_001}"'),
    ('old "_We\'ve kept investigating, but we haven\'t found any promising information. Louise is getting grumpier, too…{#ch6_344_th_002}"',
     'old "We\'ve kept investigating, but we haven\'t found any promising information. Louise is getting grumpier, too…{#ch6_344_th_002}"'),
    ('old "_How long is this going to go on…?{#ch6_344_th_003}"',
     'old "How long is this going to go on…?{#ch6_344_th_003}"'),
    ('old "_Oh no, we\'re too late!{#ch6_1429_th_001}"',
     'old "Oh no, we\'re too late!{#ch6_1429_th_001}"'),
]
TH4_CH6_2 = [
    ('old "(She\'s truly a queen. She sees all that just by looking at the market.)"',
     'old "She\'s truly a queen. She sees all that just by looking at the market."'),
    ('old "(It seems to have cheered her up. Whether the food had anything to do with it, I have no idea.)"',
     'old "It seems to have cheered her up. Whether the food had anything to do with it, I have no idea."'),
    ('old "(What am I going to do...? If I confess that I took the princess out without permission and wandered around town with her all day, Louise will punish me for sure.)"',
     'old "What am I going to do...? If I confess that I took the princess out without permission and wandered around town with her all day, Louise will punish me for sure."'),
    ('old "(But if I go back now, Louise will beat me to death for making her act on her honest feelings.)"',
     'old "But if I go back now, Louise will beat me to death for making her act on her honest feelings."'),
]
for lang in ("japanese", "russian"):
    fix_file(f"game/tl/{lang}/thoughs.rpy", TH4_CH6_1 + TH4_CH6_2, expect=8)
print("E4/E5: old-синк 8×2 выполнен")

# ---------- 2) RU-new нормализация (чтения ch6_344) ----------
RU_NEW_FIX = [
    ('new "_С спектакля прошло уже несколько дней. Но мы так и не нашли никаких следов бомбиста._"',
     'new "С спектакля прошло уже несколько дней. Но мы так и не нашли никаких следов бомбиста."'),
    ('new "_Мы продолжаем расследование, но ничего стоящего узнать не удаётся. Луиза тоже становится всё раздражительнее…_"',
     'new "Мы продолжаем расследование, но ничего стоящего узнать не удаётся. Луиза тоже становится всё раздражительнее…"'),
    ('new "_Интересно, долго это ещё будет продолжаться…?_"',
     'new "Интересно, долго это ещё будет продолжаться…?"'),
]
fix_file("game/tl/russian/thoughs.rpy", RU_NEW_FIX, expect=3)
print("RU-new: 3 маркера сняты")

# ---------- 3) E11: tag-dedup ----------
# (tag, speaker, text) — по порядку появления в скрипте ch6_2
E11 = [
    ("d001", "h", "I'm glad."),
    ("d002", "s", "Hm?"),
    ("d003", "s", "Huh?"),
    ("d004", "h", "..."),
    ("d005", "h", "Hm?"),
    ("d006", "s", "Yes?"),
    ("d007", "h", "I see..."),
    ("d008", "s", "Huh?"),
    ("d009", "s", "You think so?"),
    ("d010", "l", "Oh, is that so?"),
    ("d011", "l", "..."),
]
# скрипт: теги построчно (порядок появления в файле = порядок списка)
p = ROOT / "game/chapters/6/script-ch6_2.rpy"
lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
i, ok = 0, 0
for tag, spk, text in E11:
    target = f'{spk} "{text}"'
    tagged = f'{spk} "{text}{{#ch6_2_{tag}}}"'
    found = None
    for j in range(i, len(lines)):
        if lines[j].strip() == target:
            found = j
            break
    if found is None:
        raise SystemExit(f"FAIL ch6_2: строка {target!r} не найдена с позиции {i}")
    lines[found] = lines[found].replace(target, tagged, 1)
    i = found + 1
    ok += 1
p.write_text("".join(lines), encoding="utf-8")
OK.append(f"ch6_2 скрипт: {ok} тегов")

# tl old: теги в блоках ch6_2 (ja + ru), порядок = порядок E11
for lang in ("japanese", "russian"):
    p = ROOT / f"game/tl/{lang}/dialogs.rpy"
    lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
    start = next(k for k, l in enumerate(lines) if "ch6_2 provisional source port" in l)
    i, ok = start, 0
    for tag, spk, text in E11:
        target = f'    old "{text}"'
        tagged = f'    old "{text}{{#ch6_2_{tag}}}"'
        found = None
        for j in range(i, len(lines)):
            if lines[j].rstrip("\n") == target:
                found = j
                break
        if found is None:
            raise SystemExit(f"FAIL {lang} dialogs: old {text!r} не найдено с позиции {i}")
        lines[found] = lines[found].replace(target, tagged, 1)
        i = found + 1
        ok += 1
    p.write_text("".join(lines), encoding="utf-8")
    OK.append(f"{lang} dialogs: {ok} тегов old")
print("E11: tag-dedup 11×(скрипт + 2 tl) выполнен")

# ---------- 4) tndl ----------
def find_voice_block(lines, voice_name):
    """Блок реплики: строка `voice name` + реплика +JA-комментарии (# JA[...]) подряд.
    Возвращает индекс последней строки блока (point of insertion = +1)."""
    idx = [k for k, l in enumerate(lines) if l.strip() == f'voice "{voice_name}"']
    if len(idx) != 1:
        raise SystemExit(f"FAIL: voice {voice_name!r} найдено {len(idx)} раз")
    k = idx[0]
    j = k + 1
    if j >= len(lines) or not re.match(r'\s*[a-z_.]+ "', lines[j]):
        raise SystemExit(f"FAIL: после voice {voice_name!r} нет реплики")
    j += 1
    while j < len(lines) and lines[j].lstrip().startswith("# JA["):
        j += 1
    return j - 1

# (voice_name, value, src_line, scene) — канон events_full/chapter_07
CH6_1_TNDL = [
    ("ch6_l_011", -30, 161, 346),
    ("ch6_l_013", -30, 184, 347),
    ("ch6_h_015", 40, 353, 351),
    ("ch6_l_022", -30, 372, 352),
    ("ch6_unk_007", -30, 1379, 1432),
    ("ch6_h_042", 40, 1486, 1437),
    ("ch6_s_073", -30, 1553, 1440),
    ("ch6_s_086", -30, 1665, 1445),
    ("ch6_s_089", 40, 1688, 1446),
]
CH6_2_TNDL = [
    ("ch6.2_h_016", -30, 761, 362),
    ("ch6.2_l_008", -30, 1043, 372),
    ("ch6.2_l_010", 40, 1061, 373),
]

p = ROOT / "game/chapters/6/script-ch6_1.rpy"
lines = p.read_text(encoding="utf-8").splitlines(keepends=True)

# tndl(None) после `label ch6:` (events_full src L6, null)
k = next(i for i, l in enumerate(lines) if l.strip() == "label ch6:")
lines.insert(k + 1, "    $ tndl(None)  # TNDL events_full L6 (null, старт главы)\n")
OK.append("ch6_1: tndl(None) после label ch6")

inserts = []
for vn, val, srcline, scene in CH6_1_TNDL:
    end = find_voice_block(lines, vn)
    inserts.append((end, f"    $ tndl({val})  # TNDL events_full L{srcline} (sc {scene}, {vn})\n"))
for pos, text in sorted(inserts, key=lambda t: t[0], reverse=True):
    lines.insert(pos + 1, text)
OK.append(f"ch6_1: {len(inserts)} вставок tndl")
p.write_text("".join(lines), encoding="utf-8")

p = ROOT / "game/chapters/6/script-ch6_2.rpy"
lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
inserts = []
for vn, val, srcline, scene in CH6_2_TNDL:
    end = find_voice_block(lines, vn)
    inserts.append((end, f"    $ tndl({val})  # TNDL events_full L{srcline} (sc {scene}, {vn})\n"))
for pos, text in sorted(inserts, key=lambda t: t[0], reverse=True):
    lines.insert(pos + 1, text)
OK.append(f"ch6_2: {len(inserts)} вставок tndl")
p.write_text("".join(lines), encoding="utf-8")

print("OK:")
for o in OK:
    print("  " + o)
