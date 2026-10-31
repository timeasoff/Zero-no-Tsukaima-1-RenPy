# -*- coding: utf-8 -*-
"""S3: генератор отчёта s3_source_branches.md из raw_s3.json.

Читает: raw_s3.json, ps2_source/_diagnostics/scene_graph.json,
game/chapters/6/*.rpy (для отметки портированных сцен ch07).
Пишет: s3_source_branches.md (UTF-8). ps2_source/ не изменяется.
"""
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", "..", ".."))
RAW = os.path.join(BASE, "raw_s3.json")
GRAPH = os.path.join(ROOT, "ps2_source", "_diagnostics", "scene_graph.json")
CH6_DIR = os.path.join(ROOT, "game", "chapters", "6")
OUT = os.path.join(BASE, "s3_source_branches.md")

# глава 7 источника = проектная глава 6
PROJECT_CH = {7: 6}

# к каким "чертогам" ведут foreign-цели (core-диапазоны глав источника)
CORE_RANGES = [
    (7, 344, 374), (8, 375, 404), (9, 405, 428), (10, 429, 430),
    (11, 431, 466), (12, 467, 509), (13, 510, 548), (14, 549, 577),
    (15, 578, 618), (16, 619, 659), (17, 660, 669),
]


def chapter_of(scene):
    for ch, a, b in CORE_RANGES:
        if a <= scene <= b:
            return ch
    return None


def cut40(s):
    return s if len(s) <= 40 else s[:39] + "…"


def load_graph():
    with open(GRAPH, encoding="utf-8") as f:
        g = json.load(f)
    graph = g["graph"]
    inc = {}
    for k, v in graph.items():
        for t in v:
            inc.setdefault(t, set()).add(int(k))
    return graph, inc


def ported_scenes_ch6():
    """Сцены, для которых есть label в game/chapters/6/*.rpy.

    label ch6   = сцена 344; label ch6_2 = сцена 360;
    label *_sNNN = сцена NNN (s-лейблы).
    """
    scenes = set()
    lab = re.compile(r"^label\s+(\w+)\s*:", re.M)
    base = {"ch6": 344, "ch6_2": 360}
    for name in sorted(os.listdir(CH6_DIR)):
        if not name.endswith(".rpy"):
            continue
        with open(os.path.join(CH6_DIR, name), encoding="utf-8") as f:
            for m in lab.finditer(f.read()):
                lbl = m.group(1)
                if lbl in base:
                    scenes.add(base[lbl])
                else:
                    s = re.search(r"s(\d+)$", lbl)
                    if s:
                        scenes.add(int(s.group(1)))
    return scenes


def main():
    with open(RAW, encoding="utf-8") as f:
        raw = json.load(f)
    graph, inc = load_graph()
    ported = ported_scenes_ch6() if os.path.isdir(CH6_DIR) else set()

    lines = []
    out = lines.append

    out("# S3 — Инвентарь развилок источника: главы 07–17 (+ экстра-блоки)")
    out("")
    out("Источник: `ps2_source/chapters/chapter_07_*.txt` … `chapter_17_*.txt` (канон JA, "
        "только чтение); точные вызовы — `ps2_source/events_full/`. "
        "Счётчики рёбер графа (корни/висячие сцены) — из "
        "`ps2_source/_diagnostics/scene_graph.json` (рёбра GOTO+CHOICE; "
        "**рёбра `dateItem`/`date()`/`moveInit` в граф не входят** — это учтено в "
        "пояснениях). Соответствие проектных папок: source `chapter_{N+1}` = "
        "`game/chapters/N` (chapter_07 = проектная глава 6).")
    out("")
    out("Типы строк таблицы: `選択肢` (одно меню = одна строка), `移動`, `デート` (dateItem), "
        "`デート進行` (вызов `date()`), `next` (агрегировано по сцене-владельцу), "
        "`tndl`, `route`. Тексты выборов обрезаны до ~40 знаков.")
    out("")

    for ch in [str(n) for n in range(7, 18)]:
        x = raw[ch]
        ev = x["ev"]
        sl = set(x["scene_list"])

        out("## Глава %02d (ps2_source/chapters/chapter_%02d_*.txt)" % (int(ch), int(ch)))
        for h in x["header"]:
            out("")
            out("* %s" % h)

        # --- счётчики ---
        menus = sorted({c[0] for c in ev["choices"]})
        n_choices = len(ev["choices"])
        n_dates = len(ev["dates"])
        n_dateprog = len(x["dateprog"])
        n_moves_ch = len(x["moves"])
        n_moves_ev = len(ev["moves"])
        n_next = len(x["nexts"])
        n_tndl = len(ev["tndls"])
        n_like = len(ev["likes"]) + len(x["likes_ch"])
        n_route = len(ev["routes"])
        n_checkroute = sum(1 for _s, c in ev["routes"] if c == "checkRoute")
        n_checkkiss = sum(1 for _s, c in ev["routes"] if c == "checkKiss")
        out("")
        out("Сводка: выборов %d (меню %d), дат %d (+%d `date()`), смен локаций %d, "
            "tndl %d, like() %d, checkRoute %d, checkKiss %d; "
            "`next`-переходов %d."
            % (n_choices, len(menus), n_dates, n_dateprog, n_moves_ch, n_tndl,
               n_like, n_checkroute, n_checkkiss, n_next))
        if n_moves_ev != n_moves_ch:
            out("В `events_full` смен локаций %d (расхождение со `chapters` — см. "
                "`Замечания`)." % n_moves_ev)

        out("")
        out("| сцена-владелец | тип | варианты (текст → сцена) | условие/примечание |")
        out("|---|---|---|---|")

        rows = []  # (scene, order, type, variants, note)

        # 選択肢: одно меню = одна строка
        by_owner = {}
        for owner, text, target, _e, _f in ev["choices"]:
            by_owner.setdefault(owner, []).append((text, target))
        cond_by_menu = {}
        for owner, text, target, e, flag in ev["choices"]:
            if (e, flag) != ("null", "true"):
                cond_by_menu.setdefault(owner, []).append(
                    "eval=%s flag=%s" % (e, flag))
        for owner, items in by_owner.items():
            variants = "; ".join("%s → %d" % (cut40(t), tg) for t, tg in items)
            rows.append((owner, 1, "選択肢", variants,
                         "; ".join(cond_by_menu.get(owner, [])) or
                         "%d вариантов" % len(items)))

        # 移動 (chapters-вид; дополнения events — отдельной пометкой)
        mv_by_owner = {}
        for owner, name, image, dest in x["moves"]:
            mv_by_owner.setdefault(owner, []).append((name, dest))
        for owner, items in mv_by_owner.items():
            variants = "; ".join("%s → %d" % (n, d) for n, d in items)
            rows.append((owner, 2, "移動", variants,
                         "moveInit+move(); пунктов: %d" % len(items)))
        # пункты только в events_full (image=0)
        seen = {(o, d) for o, n, i, d in x["moves"]}
        ev_only = [(o, n.strip('"'), d) for o, n, i, d in ev["moves"]
                   if (o, d) not in seen]
        if ev_only:
            by_o = {}
            for o, n, d in ev_only:
                by_o.setdefault(o, []).append((n, d))
            for owner, items in sorted(by_o.items()):
                variants = "; ".join("%s → %d" % (n, d) for n, d in items)
                rows.append((owner, 3, "移動 (только events)",
                             variants,
                             "moveItem с image=0 — не отображается в chapters"))

        # デート (dateItem) и デート進行 (date())
        for owner, name, target in ev["dates"]:
            note = "dateItem-блок"
            tg = chapter_of(target)
            if tg and tg != int(ch):
                note += "; экстра-блок вне core (гл. %02d)" % tg
            rows.append((owner, 4, "デート", "%s → %d" % (name.strip('"'), target), note))
        for owner, target in x["dateprog"]:
            tg = chapter_of(target)
            note = "вызов `date()` — сцена после свидания"
            if tg and tg != int(ch):
                note += "; вход в гл. %02d" % tg
            rows.append((owner, 5, "デート進行", "date() → %d" % target, note))

        # next: агрегация по сцене-владельцу
        nxt_by_owner = {}
        for owner, target in x["nexts"]:
            nxt_by_owner.setdefault(owner, []).append(target)
        cond_by_owner = {}
        for o, t, c in ev["cond_gotos"]:
            cond_by_owner.setdefault(o, []).append("%d: %s" % (t, c))
        for owner, targets in nxt_by_owner.items():
            variants = ", ".join("→ %d" % t for t in targets)
            notes = []
            if owner in cond_by_owner:
                notes.append("условный переход, условие — " +
                             "; ".join(cond_by_owner[owner]))
            foreign = [t for t in targets if t not in sl]
            for t in foreign:
                tg = chapter_of(t)
                if tg and tg != int(ch):
                    notes.append("→ %d = вход в гл. %02d" % (t, tg))
            out_of_range = [t for t in targets if chapter_of(t) is None
                            and t not in sl]
            for t in out_of_range:
                notes.append("цель %d вне core/extra глав 07–17 ???" % t)
            notes.append("переходов: %d" % len(targets))
            rows.append((owner, 6, "next", variants, "; ".join(notes)))

        # tndl
        for scene, val in ev["tndls"]:
            note = "сброс в 127" if val == "null" else "значение %s" % val
            rows.append((scene, 7, "tndl", "tndl(%s)" % val, note))

        # route
        for scene, call in ev["routes"]:
            rows.append((scene, 8, "route", "%s()" % call,
                         "см. подраздел «Маршрут»"))

        rows.sort(key=lambda r: (r[0], r[1]))
        for owner, _o, typ, variants, note in rows:
            out("| %d | %s | %s | %s |" % (owner, typ, variants, note or "—"))

        # --- События тундэре-метра ---
        out("")
        out("### События тундэре-метра")
        if ev["tndls"]:
            out("")
            for scene, val in ev["tndls"]:
                out("* %d → `tndl(%s)`%s" % (scene, val,
                                             " — сброс в 127" if val == "null" else ""))
        else:
            out("")
            out("* событий `tndl()` в главе нет.")

        # --- Маршрут ---
        out("")
        out("### Маршрут")
        out("")
        route_lines = []
        for scene, call in ev["routes"]:
            route_lines.append("* %d → `%s()`" % (scene, call))
        for o, t, c in ev["cond_gotos"]:
            route_lines.append("* условный переход: %d → %d при `%s`" % (o, t, c))
        # входы в главу
        entries = sorted(t for t in sl
                         if any(s not in sl for s in inc.get(t, ())))
        for t in entries:
            src = sorted(s for s in inc.get(t, ()) if s not in sl)
            route_lines.append("* вход в главу: %d ← сц. %s (извне)"
                               % (t, ", ".join(str(s) for s in src)))
        # корни без входящих рёбер
        roots = sorted(n for n in sl if n not in inc)
        if roots:
            route_lines.append("* корни без входящих рёбер (GOTO/CHOICE): %s"
                               % ", ".join(str(r) for r in roots))
        # выходы
        exit_owners = {}
        for o, t in x["nexts"]:
            if t not in sl and chapter_of(t) is not None:
                exit_owners.setdefault(t, set()).add(o)
        for o, t in x["dateprog"]:
            if t not in sl and chapter_of(t) is not None:
                exit_owners.setdefault(t, set()).add(o)
        for t in sorted(exit_owners):
            tg = chapter_of(t)
            route_lines.append("* выход из главы: сц. %s → гл. %02d, сцена %d"
                               % (", ".join(str(s) for s in
                                            sorted(exit_owners[t])), tg, t))
        # сцены без исходящих рёбер
        no_out = sorted(n for n in sl if not graph.get(str(n)))
        if no_out:
            route_lines.append("* сцены без исходящих рёбер графа: %s"
                               % ", ".join(str(n) for n in no_out))
        if not route_lines:
            route_lines.append("* route-веток нет.")
        for l in route_lines:
            out(l)

        # --- портированные сцены ch07 ---
        if int(ch) in PROJECT_CH:
            core_a = int(re.search(r"(\d+) \.\.", x["header"][0]).group(1))
            mine = sorted(p for p in ported if sl and p in sl)
            not_mine = sorted(sl - set(mine))
            out("")
            out("### Портированные сцены (`game/chapters/%d/`)" % PROJECT_CH[int(ch)])
            out("")
            out("* Есть labels для %d сцен из %d: %s"
                % (len(mine), len(sl), ", ".join(str(s) for s in mine)))
            out("* Нет в `.rpy`: %s"
                % ", ".join(str(s) for s in not_mine))
            out("* Файлы: `script-ch6_1.rpy` (label `ch6` = сц. %d + s-лейблы), "
                "`script-ch6_2.rpy` (label `ch6_2` = сц. 360)." % core_a)
        out("")

    # ---------------- Замечания ----------------
    out("## Замечания (???)")
    out("")
    out("1. **ch10 (проектная 9): сцена 429 — корень без входящих рёбер и без "
        "исходящих.** Сцена 428 (гл. 09) ведёт напрямую в 430 (`→ next scene 430`), "
        "минуя 429; при этом 429 содержит TITLE «魅惑のお姫さま» + основной текст и "
        "заканчивается `syssave()` без `setClear()`, а 430 — `setClear(); syssave()`. "
        "Как движок попадает в 429 — из текстовых рёбер не следует "
        "(возможно, карточка-заголовок вызывается иначе). Classification: WARNING. "
        "Disposition: ??? (требуется решение человека при порте гл. 9).")
    out("2. **ch17 (проектная 16): сцена 660 — корень без входящих рёбер.** "
        "Сцена 659 (гл. 16) ведёт напрямую в 665, минуя блок 660–664. Блок 660–664: "
        "660 (TITLE + текст, конец — выбор 661/662/663), 661/662/663 → 664, "
        "664 — висячая сцена без исходящих рёбер. "
        "Classification: WARNING. Disposition: ??? (сценарная логика перехода "
        "659 → 665 требует проверки человеком).")
    out("3. **SCENE_0664 — NUL-стаб.** `ps2_source/scripts/SCENE_0664.txt`: 26 байт, "
        "содержимое `if (isJump()){re\\0…` (9 NUL) — тело утеряно. "
        "Признак «петля `if(isJump())` → переход» сохранился, сам переход не читается. "
        "В `chapters/chapter_17` сцена 664 пуста. Classification: ERROR (источник "
        "повреждён). Disposition: ??? (восстановление возможно только по JA-канону/"
        "человеку; не править автоматически).")
    out("4. **ch12: расхождение chapters ↔ events_full по 移動.** В chapters смен "
        "локаций 4 (сцена 471), в events_full 8 (471 + 483). Причина: сцена 483 "
        "содержит 4 вызова `moveItem(name, 0, dest)` с image=0 "
        "(表通り→1895, 裏通り→1900, 街道→1905, 劇場→1910) — такие пункты не "
        "отображаются в читаемом chapters-виде. Classification: WARNING. "
        "Disposition: ACCEPTABLE ADAPTATION (объяснено), но при порте учитывать "
        "оба набора пунктов меню карты для сцен 471 и 483.")
    out("5. **ch15: расхождение chapters (7) ↔ events_full (8) по 移動.** Сцена 599: "
        "4-й пункт `moveItem(\"城前\", 0, 1492)` с image=0 отсутствует в chapters "
        "(пункты 1489/1490/1491 отображаются, 1492 — нет). "
        "Classification: WARNING. Disposition: ACCEPTABLE ADAPTATION; при порте "
        "сцены 599 нужен 4-й пункт 城前→1492.")
    out("6. **Корни без входящих рёбер, требующие пояснения:** "
        "ch07: 356–359 и 360; ch11: 440, 447–451; ch12: 472, 484, 494, 499, 509, "
        "1876, 1881, 1886, 1890, 1895, 1900, 1905, 1910; ch13: 514, 539; "
        "ch14: 564–568; ch15: 589–593, 600–604; плюс date-экстры 1164/1169/1174/"
        "1179/1184/1189 (входят рёбрами `dateItem`, которых нет в graph). "
        "Частично объяснимо: первым аргументом `moveInit(...)` являются сцены-"
        "«возврат с карты» 360, 451, 472, 484, 568, 593, 604 (движок переходит туда "
        "при закрытии карты — рёбра в graph отсутствуют); стабы вида "
        "`if(isJump()) → next(локация)` (356–359, 447–450, 564–567, 589–592, "
        "600–603) ведут в те же локации, что и moveItem. "
        "Classification: CANDIDATE. Disposition: PROVISIONAL — объяснение "
        "не доказано рёбрами источника, при порте сверять с движком карты. "
        "Сцены 440, 494, 499, 514, 539 (с содержанием, корни) — "
        "Disposition: ??? (путь входа не найден).")
    out("7. **like()/【好感度】: 0 вызовов во всех главах 07–17** — сверено по "
        "chapters и events_full (проверка пройдена, не ошибка).")
    out("8. **checkRoute(): 0 вызовов в главах 07–17** (он в главе 6 источника, "
        "сцена 341). Условные развилки здесь — только `checkKiss()` "
        "(ch09 сц. 416, ch13 сц. 518, ch16 сц. 646), условие — флаг `zero_kiss`.")
    out("9. **`if` кроме `if(isJump())`: не найдено** (other_if = 0 во всех главах); "
        "все прочие условия в events — второй аргумент `GOTO next(..., cond)`: "
        "только `zero_kiss`/`!zero_kiss`.")
    out("10. **Сцены без исходящих рёбер, завершающие главу:** "
        "ch13: 543 (`syssave()`), 548 (`setClear(); syssave()`); "
        "ch10: 429/430 (см. п. 1); ch17: 664 (битый стаб, п. 3), 669 "
        "(`setClear(); syssave()`). Остальные «висячие» сцены (1433/1438/1443/1448, "
        "1453/1458/1463/1468, 1469/1474/1479/1484, 1485–1492 и т.п.) — это "
        "локации карты, заканчивающиеся вызовом `MOVE move()` (возврат к карте), "
        "плюс date-блоки, заканчивающиеся `date()` — это норма, не ошибка.")
    out("11. **ch12: четыре идентичных блока デート/デート進行 (506–509).** "
        "Сцены 506, 507, 508, 509 — четыре одинаковых входа в dateItem-блок "
        "(ハルナ → 1179) с одинаковым `date() → 510`; выбор, какой из четырёх "
        "срабатывает, задаётся сценой-предшественником. "
        "Classification: PASS (дубликаты функциональны). Disposition: PRESERVED — "
        "FUNCTIONAL; при порте достаточно одного механизма, но все четыре входа "
        "нужно сохранить как варианты.")
    out("12. **Терминалы с `setClear(); syssave()`:** 430 (ch10), 548 (ch13), "
        "669 (ch17) — «концы ветвей»; в `chapters` без исходящих рёбер, в игре — "
        "завершение фрагмента. Disposition: PRESERVED — FUNCTIONAL.")
    out("13. **Ветки в несуществующие сцены: не найдено** (bad_targets = 0 во всех "
        "главах 07–17).")
    out("14. **ch12: сцены 1904, 1909, 1914 — стабы без читаемого продолжения.** "
        "Вход из 1901/1902/1903, 1906/1907/1908, 1911/1912/1913 соответственно; "
        "исходящих рёбер нет ни в chapters, ни в events_full (там только строка "
        "`if(isJump())`). Сырые `SCENE_1904/1909/1914.txt` повреждены: 34 байта, "
        "EMBEDDED-NUL (`if (isJump()){re\\0e\\0(\\0;\\0}\\0m\\0v\\0(\\0;\\0` — "
        "фрагмент напоминает `…reset();}mv(;`, т.е. вероятный возврат к карте, "
        "как у соседних сцен 1880/1885/1889/1894/1899 с `MOVE move()`). "
        "Classification: ERROR (тело сцены в источнике повреждено). "
        "Disposition: ??? — прочтение `mv(…` гипотетическое, при порте гл. 11 "
        "решение принимает человек (класс NUL-стабов AGENTS: «потери текста нет» "
        "относится к talk()-строкам, но продолжение ветки здесь нечитаемо).")

    text = "\n".join(lines) + "\n"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print("OK wrote %s (%d lines, %d bytes)" %
          (OUT, text.count("\n"), len(text.encode("utf-8"))))


if __name__ == "__main__":
    main()