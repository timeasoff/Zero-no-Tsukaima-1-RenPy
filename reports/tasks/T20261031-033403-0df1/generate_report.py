#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка отчёта s5_source_branches.md из raw_branches.json.

Только чтение ps2_source/; выход — UTF-8 markdown рядом со скриптом.
"""
import json
import os
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw_branches.json")
OUT = os.path.join(HERE, "s5_source_branches.md")

TYPE_ORDER = ["選択肢", "移動", "デート", "デート進行", "next", "tndl", "route"]


def cut(s, n=40):
    s = " ".join(s.split())
    return s if len(s) <= n else s[:n - 1] + "…"


def group(items, key=lambda x: x[0]):
    d = OrderedDict()
    for it in items:
        d.setdefault(key(it), []).append(it)
    return d


def chapter_rows(d):
    """Строки таблицы одной главы: (owner, type, variants, note)."""
    e = d["ev"]
    rows = []

    for owner, items in group(d["choices"]).items():
        var = "; ".join("%s → %d" % (t, g) for _, t, g in items)
        evals = {x[3] for x in e["choices"] if x[0] == owner and x[3] not in ("null", "")}
        note = ("eval: " + "; ".join(sorted(evals))) if evals else ""
        rows.append((owner, "選択肢", var, note))

    for owner, items in group(d["moves"]).items():
        var = "; ".join("%s → %d" % (n, r if r else t) for _, n, t, r, _ in items)
        note = "карта: число после → scene = id картинки; реальная цель из ((0x01000000 +N)) / moveItem"
        rows.append((owner, "移動", var, note))

    for owner, items in group(d["dates"]).items():
        var = "; ".join("%s → %d" % (n, g) for _, n, g in items)
        rows.append((owner, "デート", var, "dateItem(); сцены-слайды, в конце next обратно к цели date()"))

    for owner, tgt in d["dateprog"]:
        note = "date(done=%d, restrict=false, bgm=+4); при экстремальном тундэре-метре меню свидания заменяется событием 90/91" % tgt
        rows.append((owner, "デート進行", "→ %d" % tgt, note))

    cond = {(o, g): c for o, g, c in e["cond_gotos"]}
    for owner, items in group(d["nexts"]).items():
        parts = []
        notes = []
        for _, g in items:
            c = cond.get((owner, g))
            parts.append("→ %d%s" % (g, (" [%s]" % c) if c else ""))
            if c:
                notes.append("%d — условный переход (%s)" % (g, c))
        rows.append((owner, "next", "; ".join(parts), "; ".join(notes)))

    for owner, items in group(e["tndls"]).items():
        var = "; ".join("tndl(%s)" % v for _, v in items)
        vals = [v for _, v in items]
        if all(v == "null" for v in vals):
            note = "null = сброс метра в 127 (старт)"
        else:
            note = "дельта метра zero_tundele (0…255)"
        rows.append((owner, "tndl", var, note))

    for owner, items in group(e["routes"]).items():
        var = "; ".join(k for _, k in items)
        if var == "checkKiss":
            note = "zero_kiss = (zero_tundele_count >= 4 ? 0 : 1); далее условные next zero_kiss / !zero_kiss"
        else:
            note = "checkRoute(): определяет zero_route по zero_tundele_count и max zero_likes"
        rows.append((owner, "route", var, note))

    rows.sort(key=lambda r: (r[0], TYPE_ORDER.index(r[1])))
    return rows


def render_table(rows):
    out = ["| сцена-владелец | тип | варианты (текст → сцена) | условие/примечание |",
           "|---|---|---|---|"]
    for o, t, v, n in rows:
        out.append("| %d | %s | %s | %s |" % (o, t, v.replace("|", "\\|"),
                                               n.replace("|", "\\|")))
    return "\n".join(out)


def summary_line(ch, d):
    e = d["ev"]
    menus = len({x[0] for x in d["choices"]})
    return (
        "Сводка: сцен %d, меню выбора %d (вариантов %d), дат %d, дат-продолжений %d, "
        "смен локации %d, `next` %d, tndl %d, like() %d, checkRoute/checkKiss %d, "
        "внешних условий (кроме `if(isJump())`) %d."
        % (d["scenes"], menus, len(d["choices"]), len(d["dates"]), len(d["dateprog"]),
           len(d["moves"]), len(d["nexts"]), len(e["tndls"]), len(e["likes"]),
           len(e["routes"]), len(e["other_if"]))
    )


def main():
    raw = json.load(open(RAW, encoding="utf-8"))
    L = []
    w = L.append

    # ---------- шапка ----------
    w("# S5 — Инвентарь развилок источника: главы 18…29 + экстра 90/91")
    w("")
    w("Задание: `reports/tasks/prompts/T20261031-033403-0df1_S5.md`. Отчёт самодостаточен: "
      "все числа и тексты взяты напрямую из `ps2_source/` (только чтение, ничего не правилось).")
    w("")
    w("**Область:** `ps2_source/chapters/chapter_18_*.txt` … `chapter_29_*.txt`, "
      "`chapter_90_*.txt`, `chapter_91_*.txt` (читаемый вид) + `ps2_source/events_full/` "
      "те же файлы (точные `tndl/selectItem/dateItem/moveItem/next/if`) + "
      "`ps2_source/scripts/*.txt` (CP932) для `tnEventId`/`dlEventId`/`getTunDeleScene`/`date`.")
    w("")
    w("**Метод:** `extract_branches.py` (парсит оба входа в `raw_branches.json`), "
      "`scan_tnde.py`/`decode_scene3.py` (поиск присвоений в CP932-скриптах), "
      "`scene_tails.py`, `entry_samples.py`, `entry_speakers.py`, `sample_routes.py`, "
      "`engine_tables.py` — все скрипты лежат рядом с отчётом. CP932 декодируется python'ом, "
      "японский в консоль не выводится.")
    w("")
    w("**Проектные папки (проверено listing'ом):** `game/chapters/17` … `game/chapters/28` — "
      "**пусты** (0 файлов: источники `chapter_18`…`chapter_29` = проектные главы 17…28, "
      "не портированы); `game/chapters/extra/` — только `sp_l1.rpy`. То есть для всех глав "
      "18…29 работа по порту ещё не начиналась, а для 90/91 портирован лишь файл `sp_l1.rpy`.")
    w("")

    # ---------- сводная таблица ----------
    w("## 0. Сводная таблица счётчиков")
    w("")
    w("| глава | сцен | меню выбора (вариантов) | дат | дат-продолж. | смен локации | `next` | tndl | like() | checkRoute/checkKiss | внешних `if` |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for ch in [str(c) for c in list(range(18, 30)) + [90, 91]]:
        d = raw[ch]
        e = d["ev"]
        menus = len({x[0] for x in d["choices"]})
        w("| %s | %d | %d (%d) | %d | %d | %d | %d | %d | 0 | %d | %d |"
          % (ch, d["scenes"], menus, len(d["choices"]), len(d["dates"]),
             len(d["dateprog"]), len(d["moves"]), len(d["nexts"]), len(e["tndls"]),
             len(e["routes"]), len(e["other_if"])))
    w("")
    w("**like() (`【好感度】` / `like(...)`) во всех 14 главах = 0 — вызовов нет ни в "
      "`chapters/`, ни в `events_full/` (проверено обоими входами).**")
    w("")
    w("**Внешние условия:** во всех `events_full` этих глав ровно 602 строки `if`, и все — "
      "рутинное `if(isJump())`. Других `if(...)` нет. Единственное внешнее условие, влияющее "
      "на переходы, — флаг `zero_kiss` в `GOTO next(..., zero_kiss)` (см. раздел «Маршрут»).")
    w("")

    # ---------- главы 18..29 ----------
    w("## 1. Главы 18…29 — таблицы развилок")
    w("")
    w("Типы: `選択肢` (меню выбора), `移動` (смена локации), `デート` (список партнёров "
      "`dateItem`), `デート進行` (`date()` — запуск свидания), `next` (безусловный/условный "
      "`next()`), `tndl` (сдвиг тундэре-метра), `route` (`checkRoute`/`checkKiss`). "
      "Сцены-владельцы и номера сцен — строго из файлов.")
    w("")

    for ch in [str(c) for c in range(18, 30)]:
        d = raw[ch]
        w("### Глава %s (`ps2_source/chapters/%s`)" % (ch, d["file"]))
        w("")
        for hline in d["header"]:
            w("")
            w("`%s`" % hline.strip())
        w("")
        w(summary_line(ch, d))
        w("")
        rows = chapter_rows(d)
        if rows:
            w(render_table(rows))
        else:
            w("Развилок нет — глава линейная (см. примечание ниже).")
        w("")

        # подразделы
        e = d["ev"]
        w("* События тундэре-метра: %s."
          % ("нет вызовов `tndl`" if not e["tndls"] else
             "%d вызов(ов) `tndl` — в таблице строками типа `tndl` (сброс `null` на первой "
             "сцене главы, далее дельты ±30/±40)" % len(e["tndls"])))
        if e["routes"]:
            w("* Маршрут: %s." % "; ".join(
                "`%s()` в сцене %d" % (k, o) for o, k in e["routes"]))
            if e["cond_gotos"]:
                w("  Условные переходы: " + "; ".join(
                    "%d → %d [%s]" % (o, g, c) for o, g, c in e["cond_gotos"]) + ".")
        else:
            w("* Маршрут: `checkRoute()`/`checkKiss()` в главе нет.")
        w("")

    # ---------- тундэре-метр: механизм ----------
    w("## 2. События тундэре-метра — механизм (из кода движка)")
    w("")
    w("Всё ниже — из `ps2_source/scripts/SCENE_0003.txt` (CP932, расшифрован "
      "`decode_scene3.py` → `SCENE_0003_decoded.txt`):")
    w("")
    w("```")
    w("zero_tundele      0…255, старт 127;  tndl(null) -> 127;  tndl(add) -> +/- add (кламп)")
    w("date(done, restrict, bgm):")
    w("    if (zero_tundele < 40)   -> getTunScene()  = getTunDeleScene(true,  zero_tun_event,  restrict)")
    w("    else if (zero_tundele >= 211) -> getDeleScene() = getTunDeleScene(false, zero_dele_event, restrict)")
    w("    zero_tndl_done = done;  resetSelect2(zero_tndl_scene)  // меню свидания -> вычисленная сцена")
    w("    ::DateClear(zero_tndl_flag != 0)")
    w("getTunDeleScene(tun, event, restrict):")
    w("    for (i = 0; i < 6; i++) ... switch (event[i]) { case 0: level1; case 1: level1 x4; case 2: level2 }")
    w("    return (tun ? tnEventId : dlEventId) + 2 + (zero_tndl_no * 3) + event[zero_tndl_no];")
    w("tndlStart() -> next(zero_tndl_scene, true)   // прыжок в событие")
    w("tndlEnd()   -> next(zero_tndl_done, true)    // возврат к цели date()")
    w("dateDone()  -> zero_tun_event[zero_tndl_no]++ / zero_dele_event[...]++; zero_tundele_count++")
    w("```")
    w("")
    w("Практические следствия для порта глав 18…29:")
    w("")
    w("* `【デート進行】 → scene N` = вызов `date(N, false, +4)`: сцена `N` — это "
      "«отложенная» цель свидания; при экстремальном метре (<40 или ≥211) меню свидания "
      "заменяется событием главы 90/91, а после него `tndlEnd()` ведёт ровно в ту же `N` "
      "(пример главы 18: `date(696, …)` — событие вместо свидания, финиш всё равно в 696).")
    w("* `event[no]` может быть только 0/1/2 (в `switch` нет ветки для 3+), поэтому на слот "
      "приходится максимум 3 показа, дальше слот выпадает из пула → всего 6×3 = 18 входных "
      "сцен на блок.")
    w("* `zero_tundele_count` (число фактических изменений метра) — вход для `checkRoute()`/`checkKiss()` "
      "и для определения «пути» (см. раздел 4).")
    w("* В самих главах 18…29 `tndl` вызывается только внутри реплик-веток "
      "(`null`/±30/±40); в главах 90/91 вызовов `tndl` **нет вообще** — события метр не двигают.")
    w("")

    # ---------- маршрут ----------
    w("## 3. Маршрут — `checkRoute()` / `checkKiss()`")
    w("")
    w("Определения (тот же `SCENE_0003.txt`):")
    w("")
    w("```")
    w("checkRoute(): zero_route = 1 (ルイズ), если zero_tundele_count >= 4;")
    w("              иначе — по максимуму zero_likes: isMax(5)->6 ハルナ, isMax(3)->4 シエスタ,")
    w("              isMax(4)->5 アンリエッタ, isMax(2)->3 タバサ, isMax(1)->2 キュルке, иначе 1 ルイズ")
    w("checkKiss():  zero_kiss = (zero_tundele_count >= 4) ? 0 : 1")
    w("likeNameMap:  ルイズ=0, キュルケ=1, タバサ=2, シエスタ=3, アンリエッタ=4, ハルナ=5")
    w("```")
    w("")
    w("Где вызываются (все главы проекта, для контекста): `checkRoute()` — **один раз**, "
      "сцена 0341 (глава 6, `ps2_source/events_full/chapter_06_…`); `checkKiss()` — сцены "
      "0416 (гл. 9), 0518 (гл. 13), 0646 (гл. 16), **0755 (гл. 20), 0863 (гл. 24), 0990 (гл. 28)**.")
    w("")
    w("В охватываемых главах 18…29:")
    w("")
    w("| глава | сцена с `checkKiss()` | условные переходы |")
    w("|---|---|---|")
    for ch in ["20", "24", "28"]:
        d = raw[ch]
        rk = [o for o, k in d["ev"]["routes"] if k == "checkKiss"]
        cg = "; ".join("%d → %d [%s]" % (o, g, c) for o, g, c in d["ev"]["cond_gotos"])
        w("| %s | %s | %s |" % (ch, ", ".join(str(x) for x in rk) or "—", cg or "—"))
    w("")
    w("* глава 25: `checkKiss()` **нет**, но условные переходы `899 → 900 [zero_kiss]` / "
      "`899 → 901 [!zero_kiss]` есть — флаг переиспользуется (считан ранее, см. главу 24); "
      "при порте это тоже ветка.")
    w("* главы 18, 19, 21, 22, 23, 26, 27, 29: ни `checkRoute`, ни `checkKiss`, ни условных "
      "`next` — только безусловные `→ next scene N`.")
    w("")
    w("Внимание: в `chapters/*.txt` условие у `next` **не видно** (там просто "
      "`→ next scene 756` и `→ next scene 757` подряд) — условие читается только из "
      "`events_full` (`GOTO next((0x01000000 +N), zero_kiss)` / `!zero_kiss`).")
    w("")

    # ---------- главы 90/91 ----------
    w("## 4. Главы 90 и 91 — спецсобытия тундэре/дэре")
    w("")
    w("### 4.1 Сводка и состав сцен")
    w("")
    w("| | глава 90 | глава 91 |")
    w("|---|---|---|")
    a, b = raw["90"], raw["91"]
    w("| источник | `chapter_90_特別イベントA（トゥンデレ／デレ）` | `chapter_91_特別イベントB（トゥンデレ／デレ）` |")
    w("| диапазон сцен | `extra scenes: 1533..1696 (164)` | `extra scenes: 1697..1860 (164)` |")
    w("| сцен в файле | %d | %d |" % (a["scenes"], b["scenes"]))
    w("| `【選択肢】` | %d (36 меню × 3) | %d (36 меню × 3) |" % (len(a["choices"]), len(b["choices"])))
    w("| `→ next scene` | %d | %d |" % (len(a["nexts"]), len(b["nexts"])))
    w("| `【好感度】` / `like()` | 0 | 0 |")
    w("| `tndl` в `events_full` | 0 | 0 |")
    w("| `checkRoute`/`checkKiss` | 0 | 0 |")
    w("| `【移動】`/`【デート】`/`【デート進行】` | 0 | 0 |")
    w("| входные сцены (по формуле) | 1535…1552 (18) | 1699…1716 (18) |")
    w("| стартовые стабы | 1533, 1534 (NUL-порча) | 1697, 1698 (NUL-порча) |")
    w("")
    w("**Структура обеих глав одинакова** (проверено по `chapters/` и `events_full/`):")
    w("")
    w("```")
    w("входная сцена E (18 шт.)            — реплики + меню из 3 вариантов")
    w("  ├─ вариант 1 → G+0 ─┐")
    w("  ├─ вариант 2 → G+1 ─┼─ каждый: → next G+3")
    w("  └─ вариант 3 → G+2 ─┘")
    w("  G+3 = второе меню (3 варианта) → G+4, G+5, G+6 — каждый: → next G+7")
    w("  G+7 = финал маршрута: [COFFEE] + tndlEnd()  -> next(zero_tndl_done)")
    w("где G = 1553 + 8*k (гл.90) / 1717 + 8*k (гл.91), k = 0…17")
    w("```")
    w("")
    w("Итог на главу: 18 входных сцен + 18 групп × 8 сцен = 162 + 2 стаба = 164 сцены "
      "(сверено с шапкой файлов). `next` = 18 групп × 6 = 108 ✓, меню = 18 входных + "
      "18 групповых = 36 ✓.")
    w("")

    for ch, base, gbase in (("90", 1533, 1553), ("91", 1697, 1717)):
        d = raw[ch]
        w("### 4.%s Глава %s — меню (входные сцены и вторые меню групп)" % (2 if ch == "90" else 3, ch))
        w("")
        w(summary_line(ch, d))
        w("")
        menus = group(d["choices"])
        rows = []
        for owner, items in sorted(menus.items()):
            var = "; ".join("%s → %d" % (t, g) for _, t, g in items)
            if owner < (base + 2 + 18):
                note = "входная сцена (по формуле base+2+no*3+event[no]); группа G = %d" % (
                    gbase + 8 * (owner - (base + 2)))
            else:
                note = "второе меню группы G = %d" % (gbase + 8 * ((owner - 3 - gbase) // 8))
            rows.append((owner, "選択肢", var, note))
        rows.sort(key=lambda r: r[0])
        w(render_table(rows))
        w("")
        w("Все остальные переходы главы подчинены регулярной схеме из 4.1 (108 шт.): "
          "`G+0/G+1/G+2 → next (G+3)`, `G+4/G+5/G+6 → next (G+7)`, "
          "финалы G+7 = %s%s."
          % ("tndlEnd() (кроме группы k=13 главы 90 — см. «Замечания», п. 2)" if ch == "91"
             else "tndlEnd() в 17 из 18 групп; в финале 1664 — только COFFEE (см. «Замечания», п. 2)",
             "" if ch == "91" else ""))
        w("")

    # ---------- тундэре/дэре-варианты ----------
    w("### 4.4 Какие сцены несут тундэре- и дэре-варианты")
    w("")
    w("Теги `【…】` в главах 90/91 — только `【選択肢】` (216 шт. суммарно), никаких "
      "`【好感度】`/`【デート】`/`【移動】` нет. Маркировки «тун»/«дэре» на уровне сцен "
      "**нет** — разделяются только два блока-поддиапазона, а именно:")
    w("")
    w("* **блок 1533…1696 (гл. 90)** — во всех 18 входных сценах реплики `ルイズ`/`サイト` "
      "с агрессивно-наказывающим контекстом («この、バカ犬っ！」, ошейник, お仕置き, отпор), "
      "BGM во всех сценах группы — `play=+30` (в основном потоке этот же BGM идёт со "
      "сценами ссор), CG-вспышки `image=+161` с `vibrate`;");
    w("* **блок 1697…1860 (гл. 91)** — тот же состав говорящих, но контент приглашений/ухода "
      "за героем («す・い・て・る・わ・よ・ね？」, купание, купальник, совместный чай), "
      "BGM — `play=+4` (спокойная тема), вибраций нет.")
    w("")
    w("Пример градации внутри одного меню (глава 91, сцена 1699): "
      "`うん！ 空いてる空いてる！！ → 1717` / `なんか、空いてる気がしてきた → 1718` / "
      "`断固空いてない → 1719` — это три разных ответа `サイト` (согласие / нейтраль / отказ); "
      "механически все три ведут в параллельные сцены одной группы и заканчиваются "
      "одинаково (`tndlEnd()` → возврат к `zero_tndl_done`), счётчики не меняются.")
    w("")
    w("Какая из глав — тундэре-блок, а какая — дэре-блок, источником **не доказано** — "
      "см. «Замечания», пункт 1 (расхождение `README.txt` и контента).")
    w("")

    # ---------- формула id ----------
    w("### 4.5 Как вычисляется id экстра-сцены")
    w("")
    w("Все вхождения `tnEventId`/`dlEventId` в `ps2_source/scripts/*.txt` — **только в "
      "`SCENE_0003.txt`** (7 вхождений `tn`, 6 `dl`, найдено `scan_tnde.py`):")
    w("")
    w("1. объявление (строки 54–56): `dlEventId <- null;` / `tnEventId <- null;` — "
      "комментарии `// デレイベントID` и `// ツンイベントID`;")
    w("2. формула в `getTunDeleScene(tun, event, restrict)`: "
      "`return (tun ? tnEventId : dlEventId) + 2 + (zero_tndl_no * 3) + event[zero_tndl_no];`")
    w("3. закомментированные строки в `date()`: `//resetSelect(tnEventId, tnEventId + 1);` / "
      "`//resetSelect(dlEventId, dlEventId + 1);` (заменены на `resetSelect2(zero_tndl_scene)`);")
    w("4. отладочный `tndlTest(level)`: "
      "`zero_tndl_scene = (tdtest_td == 0 ? tnEventId : dlEventId) + 2 + (tdtest_type * 3) + level;` "
      "и `next(tdtest_td == 0 ? tnEventId : dlEventId, true)`.")
    w("")
    w("**Присвоений `tnEventId <- N` / `dlEventId <- N` (N ≠ null) в "
      "`ps2_source/scripts/*.txt` НЕТ** — ни в `SCENE_0000…0004`, ни в сценах глав "
      "(проверен весь каталог, 1920 файлов, поиск байтов с `rg -a` + python-скан; "
      "в `_diagnostics/eventid_refs.txt` раздел «scenes containing arrays/tables with "
      "1533..1860 literals» пуст — тот же результат).")
    w("")
    w("Отсюда:")
    w("")
    w("* **в самом `ps2_source/` числовые значения не доказуемы**; единственный текстовый "
      "источник — `ps2_source/README.txt` (п. «CH90/91 …»): "
      "«`dlEventId 側 = 1533 系（18 ルート×8シーン）、` `tnEventId 側 = 1697 系（同上）`», "
      "т.е. README утверждает: **гл. 90 = дэре-блок, гл. 91 = тун-блок**;")
    w("* структурно утверждение README согласуется с кодом: обе базы имеют ровно по две "
      "стартовые сцены под `resetSelect(base, base+1)`, а `base+2 … base+19` дают ровно 18 "
      "входных сцен (1535…1552 и 1699…1716) — это совпадает с формулой;");
    w("* стартовые стабы восстановлены из байтов (NUL-порча): `SCENE_1533/1697` = "
      "`reset(); tndlStart(); talk(null, null, \" \", null);` (точная сверка длины: "
      "9+13+29 = 51 байт ✓), `SCENE_1534/1698` = `reset(); tndlStart();` "
      "(9+13 = 22 байта ✓). То есть базовые сцены — обёртки, вызывающие `tndlStart()` "
      "-> `next(zero_tndl_scene)`;");
    w("* входящих рёбер в 1533/1534/1697/1698 нет (`scene_graph.json`: все четыре — "
      "`roots`), а активный код `date()` ведёт `resetSelect2` **напрямую** на вычисленную "
      "сцену — обёртки в финальной версии, по-видимому, недостижимы (см. «Замечания», п. 4).")
    w("")
    w("**Где искать присвоения:** (а) скомпилированный Squirrel движка во внешнем архиве "
      "`D:\\gameMake\\ZnT-1\\ZNT_TEST\\PS2_GAME\\` (не в контейнере) — искать байты "
      "`tnEventId`/`dlEventId` рядом с литералами 1533/1697; (б) файлы движка, не "
      "попавшие в извлечение (в `ps2_source/scripts/` только сцены 0…1919); "
      "(в) воспроизводимый тест: отладочное меню `chapter_00`, сцена 1865 "
      "(`【選択肢】ツン → zero_tundele=0` / `デレ → zero_tundele=255`, затем "
      "`【選択肢】ツン/デレ → tdtest_td=0/1`, `tndlTest(level)`) — выбор «ツン» и показ "
      "блок сразу даст ответ, какой блок тундэре.")
    w("")

    # ---------- замечания ----------
    w("## 5. Замечания (???)")
    w("")
    w("1. **`???` — какой блок тундэре, какой дэре.** `README.txt` утверждает "
      "`dlEventId → 1533 系` (гл. 90 = дэре) и `tnEventId → 1697 系` (гл. 91 = тун); "
      "контент глав говорит наоборот: гл. 90 — наказания/агрессия + BGM +30 (низкий метр), "
      "гл. 91 — нежность/уход + BGM +4 (высокий метр). Присвоений в коде нет, выбрать "
      "истину по источнику нельзя. Решение за человеком; до решения в "
      "`references/routes.md` помечать оба варианта как неподтверждённые.")
    w("")
    w("2. **`???` — сцена 1664 (финал группы k=13 главы 90) не вызывает `tndlEnd()`.** "
      "`SCENE_1664.txt` = `… waitTime(1000, true); coffee(); tndl` + 7 NUL-байтов "
      "(оригинал `tndlEnd();` уничтожен порчей). Все остальные 17 финалов главы 90 и все 18 "
      "главы 91 содержат `tndlEnd()`. Следствие: при попадании в эту ветку событие, видимо, "
      "не возвращается в `zero_tndl_done` (в оригинале, вероятно, возвращался — порча данных). "
      "При порте: восстанавливать по образцу соседних финалов + отметить в отчёте части.")
    w("3. **`???` — глава 21 (`chapter_21`, сцены 769–770) не имеет ни одной развилки и "
      "входящих рёбер.** Сцена 768 (глава 20) ведёт `next(770)`, в 769 и 770 нет ни `next()`, "
      "ни `selectItem` (обе — терминальные, заканчиваются `syssave()`), в `scene_graph.json` "
      "769 и 770 (как и 429/430) — `roots` без входящих рёбер. При этом 769 содержит "
      "`title(\"小悪魔のおしおки\")` **и основной текст главы** (Uniform/ванная сюжетная линия), "
      "а 770 — следующий эпизод (разговор с `ハルナ`). Это расходится с формулировкой "
      "`AGENTS.md`/скилла `ps2-source` («429/769 — только карточки, основной текст в 430/770»): "
      "по файлам карточка и текст **в одной сцене**. Как 769 достигается в игре — из источника "
      "не следует (динамический переход/продолжение после сохранения?), при порте главы 21 "
      "нужно решение человека.")
    w("4. **`???` — назначение шести слотов `zero_tun_event[0..5]`.** По структуре слот = "
      "группе из трёх сцен (0..5 × event 0/1/2 = 18 входов), но контент всех 18 входов "
      "обеих глав — про `ルイズ`×`사이트` (с инцидентными `キュルке`/`ギーシュ`/`モンモранシー` "
      "в сценах 1545 и 1549), то есть слоты — не «девушки». "
      "Отладочное меню главы 00 подписывает слоты цифрами `２…７` "
      "(`selectItem(\"２\", …, \"tdtest_type=0\")` … `\"７\" → tdtest_type=5`), что не "
      "сводится ни к `likeNameMap` (0…5), ни к `nameMap` (ルイズ=1 … アンリエッта=7), "
      "ни к `zero_route` (1…6). Смысл подписи не определён.")
    w("5. **`???` — глава 25.** Нет `checkKiss()`, но условные переходы по `zero_kiss` "
      "есть (899 → 900/901): флаг считан в предыдущей главе (24). При разнесении глав по "
      "частям это состояние надо переносить вместе с ними.")
    w("6. **Примечание (не `???`, поведение источника).** `【移動】` в главах 22 и 26: "
      "число после `→ scene` — это id картинки карты, реальная цель записана в "
      "двойных скобках `((0x01000000 +N))` и подтверждена `moveItem(..., image, dest)` "
      "в `events_full` (например, сцена 795: `タバサの部屋 → 588 ((0x01000000 +1493))`, "
      "`MAPDEST moveItem(\"タバサの部屋\", …, (0x01000000 +1493))`). В таблицах указаны "
      "**реальные** цели 1493/1498/1503/1508 (гл. 22) и 1513/1518/1523/1528 (гл. 26).")
    w("")

    # ---------- воспроизводимость ----------
    w("## 6. Воспроизводимость")
    w("")
    w("| скрипт | что делает | выход |")
    w("|---|---|---|")
    w("| `extract_branches.py` | парсит `chapters/` + `events_full/` для 14 глав | `raw_branches.json` |")
    w("| `scan_tnde.py` | ищет `tnEventId`/`dlEventId`/`getTunDeleScene`/`date(` в CP932-скриптах | `tnde_scan_out.txt` |")
    w("| `decode_scene3.py` | расшифровка `SCENE_0003.txt` в UTF-8 | `SCENE_0003_decoded.txt` |")
    w("| `scene_tails.py` | шапка/хвост сцен 428/429/430/768/769/770/771 | `scene_tails.md` |")
    w("| `entry_samples.py`, `entry_speakers.py` | сэмплы и состав говорящих входных сцен 90/91 | `entry_samples.md`, `entry_speakers.md` |")
    w("| `sample_routes.py` | сэмплы веток/финалов 90/91 + BGM/CG | `route_samples.md` |")
    w("| `engine_tables.py` | поиск таблиц глав/сцен в движковых сценах | `engine_tables.md` |")
    w("| `generate_report.py` | сборка этого отчёта | `s5_source_branches.md` |")
    w("")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print("-> %s (%d lines)" % (OUT, len(L)))


if __name__ == "__main__":
    main()
