#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S1 — достижимость порогов louise_sympathy (+100 / -100) к входу в label ch1_10.

Модель главы 1 (порта) по факту кода:
  цепочка jump: ch1 -> ch1_2 -> ch1_3 -> ch1_4 -> ch1_5 -> ch1_6 -> ch1_7
                 -> ch1_8 -> ch1_9 -> ch1_10   (все безусловные)
  * ch1_3 и ch1_8 — sprite_choice: игрок выбирает ОДНУ локацию из N,
    внутри локации одно меню => ветки этих частей взаимоисключающие;
  * остальные меню внутри части идут последовательно (все обязательны);
  * update_sympathy(v) => value = clamp(value + v, -100, +100)
    (game/scripts/features/sympathy.rpy:418, 442-443);
  * между ch1_9 и проверками в ch1_10 симпатия не меняется:
    ch1_10:11 portrait_choice -> jump в date_<girl>_1 -> первая же строка
    "if louise_sympathy == 100" (ch1_10:25/174/329/567/794), поэтому ВСЕ
    5 проверок видят одно и то же значение — значение на входе в ch1_10.

Два независимых способа расчёта (оба печатаются, сверяются):
  СПОСОБ 1 — DP по множествам достижимых значений после каждой группы;
  СПОСОБ 2 — полный перебор всех комбинаций вариантов (itertools.product)
             + арифметическая проверка min = sum(min по группам),
                                          max = sum(max по группам).

Выход: отчёт-файл _reachability.txt (UTF-8) + короткая ASCII-сводка в консоль.
"""

import itertools
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "_reachability.txt")

MINV, MAXV = -100, 100


def clamp(v):
    return max(MINV, min(MAXV, v))


# ---------------------------------------------------------------------------
# ГРУППЫ ВЕТОК ПОРТА (в порядке исполнения). Каждая группа = одно решение
# игрока (меню ИЛИ выбор локации через sprite_choice).
# Элементы: (дельта louise, "описание с file:line").
# ---------------------------------------------------------------------------
GROUPS = [
    ("G1  ch1_1 меню@124", [
        (+20, "opt good -> script-ch1_1.rpy:142"),
        (0,   "opt neutral -> script-ch1_1.rpy:128 (без вызова)"),
        (-20, "opt bad -> script-ch1_1.rpy:161"),
    ]),
    ("G2  ch1_1 меню@372", [
        (+20, "opt good -> script-ch1_1.rpy:390"),
        (0,   "opt neutral -> script-ch1_1.rpy:374 (без вызова)"),
        (-20, "opt bad -> script-ch1_1.rpy:419"),
    ]),
    ("G3  ch1_1 меню@577", [
        (-20, "opt bad -> script-ch1_1.rpy:590"),
        (+20, "opt good -> script-ch1_1.rpy:653"),
    ]),
    ("G4  ch1_2 меню@85", [
        (+20, "Blame it on Louise -> script-ch1_2.rpy:95"),
        (-20, "cover it up yourself -> script-ch1_2.rpy:112"),
        (0,   "Blame it on Siesta -> script-ch1_2.rpy:136 (только siesta)"),
    ]),
    ("G5  ch1_3 sprite_choice (одна локация)", [
        (-20, "si_room меню@90 opt1 -> script-ch1_3.rpy:99"),
        (0,   "si_room меню@90 opt2 -> script-ch1_3.rpy:111 (без вызова)"),
        (+20, "si_room меню@90 opt3 -> script-ch1_3.rpy:127"),
        (+20, "l_room безусл. -> script-ch1_3.rpy:185 + меню@239 opt1 (0)"),
        (0,   "l_room +20(185) + меню@239 opt2 -20(264)"),
        (+40, "l_room +20(185) + меню@239 opt3 +20(305)"),
        (-20, "hallway меню@377 opt1 -> script-ch1_3.rpy:385"),
        (0,   "hallway меню@377 opt2 -> script-ch1_3.rpy:399 (без вызова)"),
        (+20, "hallway меню@377 opt3 -> script-ch1_3.rpy:427"),
    ]),
    # ch1_4 (script-ch1_4.rpy) — меню и update_sympathy нет -> группа не нужна
    ("G7  ch1_5 меню@89", [
        (0,   "opt1 half-asleep -> script-ch1_5.rpy:90 (без вызова louise)"),
        (-20, "opt2 witness -> script-ch1_5.rpy:137"),
        (+20, "opt3 wake up Louise -> script-ch1_5.rpy:212"),
    ]),
    ("G8  ch1_6 меню@67", [
        (-20, "Ask Tabitha -> script-ch1_6.rpy:76"),
        (-20, "Ask Siesta -> script-ch1_6.rpy:96"),
        (+20, "Ask Louise -> script-ch1_6.rpy:142"),
        (-20, "Ask Kirche -> script-ch1_6.rpy:178"),
    ]),
    ("G9  ch1_6 меню@433", [
        (+20, "Yeah -> script-ch1_6.rpy:437"),
        (-20, "Nope -> script-ch1_6.rpy:470"),
    ]),
    ("G10 ch1_7 меню@123", [
        (0,   "opt1 Headmaster -> script-ch1_7.rpy:124 (без вызова louise)"),
        (0,   "opt2 Kirche's room -> script-ch1_7.rpy:169 (только siesta)"),
        (-20, "opt3 my room -> script-ch1_7.rpy:271"),
    ]),
    ("G11 ch1_8 sprite_choice (одна локация)", [
        (0,   "library меню@168 opt1 -> script-ch1_8.rpy:169 (без вызова)"),
        (+20, "library меню@168 opt2 -> script-ch1_8.rpy:212"),
        (-20, "library меню@168 opt3 -> script-ch1_8.rpy:254"),
        (0,   "k_room меню@347 opt1 -> script-ch1_8.rpy:348 (без вызова)"),
        (-20, "k_room меню@347 opt2 -> script-ch1_8.rpy:406"),
        (+20, "k_room меню@347 opt3 -> script-ch1_8.rpy:453"),
        (+20, "l_room меню@598 opt1 -> script-ch1_8.rpy:611"),
        (0,   "l_room меню@598 opt2 -> script-ch1_8.rpy:659 (только haruna)"),
        (-20, "l_room меню@598 opt3 -> script-ch1_8.rpy:696"),
        (0,   "hallway: меню нет (script-ch1_8.rpy:743-754)"),
    ]),
    ("G12 ch1_9 меню@83 + меню@265", [
        (+20, "меню@83 opt1 -> script-ch1_9.rpy:98 (меню@265: без вызова)"),
        (-20, "меню@83 opt2 -> script-ch1_9.rpy:108 (меню@265: без вызова)"),
    ]),
]

# ---------------------------------------------------------------------------
# ОДНОШАГОВЫЕ СЦЕНАРИИ
# ---------------------------------------------------------------------------


def dp(groups, apply_clamp=True):
    """СПОСОБ 1: множество достижимых значений после каждой группы."""
    states = {0}
    trail = []
    for name, opts in groups:
        vals = set()
        for s in states:
            for d, _ in opts:
                v = s + d
                if apply_clamp:
                    v = clamp(v)
                vals.add(v)
        states = vals
        trail.append((name, min(states), max(states), len(states),
                      100 in states, -100 in states))
    return states, trail


def enumerate_all(groups, apply_clamp=True):
    """СПОСОБ 2: полный перебор всех комбинаций вариантов."""
    names = [g[0] for g in groups]
    optlists = [[d for d, _ in g[1]] for g in groups]
    finals = set()
    combos_100 = 0
    combos_m100 = 0
    best_pos_100 = None      # min число «хороших» (+) выборов среди путей в 100
    best_neg_100 = None      # max число «плохих» (-) выборов среди путей в 100
    best_pos_m100 = None
    best_neg_m100 = None
    stats = {100: [None, None, None, None],      # [min_pos, max_pos, min_neg, max_neg]
             -100: [None, None, None, None]}
    wit100 = witm100 = None
    total = 0
    for combo in itertools.product(*optlists):
        total += 1
        v = 0
        for d in combo:
            v = v + d
            if apply_clamp:
                v = clamp(v)
        finals.add(v)
        pos = sum(1 for d in combo if d > 0)
        neg = sum(1 for d in combo if d < 0)
        if v in stats:
            s = stats[v]
            cands = (pos, pos, neg, neg)
            for i, val in enumerate(cands):
                if s[i] is None or (val < s[i] if i % 2 == 0 else val > s[i]):
                    s[i] = val
        if v == 100:
            combos_100 += 1
            if best_pos_100 is None or pos < best_pos_100:
                best_pos_100 = pos
                wit100 = combo
            if best_neg_100 is None or neg > best_neg_100:
                best_neg_100 = neg
        if v == -100:
            combos_m100 += 1
            if best_pos_m100 is None or pos < best_pos_m100:
                best_pos_m100 = pos
                witm100 = combo
            if best_neg_m100 is None or neg > best_neg_m100:
                best_neg_m100 = neg
    return {
        "finals": finals, "total": total, "names": names, "stats": stats,
        "combos_100": combos_100, "combos_m100": combos_m100,
        "best_pos_100": best_pos_100, "best_neg_100": best_neg_100,
        "best_pos_m100": best_pos_m100, "best_neg_m100": best_neg_m100,
        "wit100": wit100, "witm100": witm100,
    }


def arith(groups):
    """СПОСОБ 2б: арифметика — min/max сырой (без клампа) суммы."""
    lo = sum(min(d for d, _ in opts) for _, opts in groups)
    hi = sum(max(d for d, _ in opts) for _, opts in groups)
    return lo, hi


def scale_groups(groups, den):
    """Уменьшить все дельты в den раз (целочисленно; все дельты кратны 20)."""
    return [(name, [(d // den, desc) for d, desc in opts])
            for name, opts in groups]


def render_set(s, cap=400):
    vals = sorted(s)
    if len(vals) > cap:
        return "[-%d..%d], n=%d" % (abs(vals[0]), vals[-1], len(vals))
    return "[" + ", ".join(str(v) for v in vals) + "]"


def main():
    L = []
    A = L.append

    A("S1 — достижимость louise_sympathy: модель главы 1 (порт) и два способа")
    A("расчёта. Шкала: -100..+100, clamp на КАЖДОМ вызове")
    A("(game/scripts/features/sympathy.rpy:418 signature, :442-443 clamp).")
    A("")
    A("Проверяемые точки: 5 условий 'if louise_sympathy == 100' в")
    A("game/chapters/1/script-ch1_10.rpy:25, 174, 329, 567, 794 (-> call sp_l1).")
    A("Все 5 видят одно значение = значение на входе в ch1_10 (portrait_choice")
    A("ch1_10:11 выполняется раньше любых update_sympathy этой части).")
    A("")

    A("=== ГРУППЫ ВЕТОК (порядок исполнения, файл:строка) ===")
    for name, opts in GROUPS:
        uniq = sorted(set(d for d, _ in opts))
        A("%-38s варианты louise: %s" % (name, uniq))
        for d, desc in opts:
            A("        %+4d  %s" % (d, desc))
    A("")

    # ---------------- СЦЕНАРИЙ A: порт, с клампом ----------------
    A("=== СЦЕНАРИЙ A: ПОРТ, с клампом ±100 (фактическое поведение игры) ===")
    set1, trail1 = dp(GROUPS, True)
    res2 = enumerate_all(GROUPS, True)
    lo_ar, hi_ar = arith(GROUPS)
    A("СПОСОБ 1 (DP):          множество на входе ch1_10: %s" % render_set(set1))
    A("                       min=%d  max=%d  n=%d  100 in set: %s  -100 in set: %s"
      % (min(set1), max(set1), len(set1), 100 in set1, -100 in set1))
    A("СПОСОБ 2 (перебор):     множество на входе ch1_10: %s" % render_set(res2["finals"]))
    A("                       min=%d  max=%d  n=%d  комбинаций всего: %d"
      % (min(res2["finals"]), max(res2["finals"]), len(res2["finals"]), res2["total"]))
    A("                       путей ровно в +100: %d ; ровно в -100: %d"
      % (res2["combos_100"], res2["combos_m100"]))
    A("СВЕРКА множеств: %s" % ("OK — идентичны" if set1 == res2["finals"] else "MISMATCH!"))
    A("Прогресс DP (после группы: min/max/n/есть100/есть-100):")
    for name, mn, mx, n, h100, hm100 in trail1:
        A("   %-38s %4d .. %4d  n=%3d  100:%s  -100:%s"
          % (name, mn, mx, n, "yes" if h100 else "no", "yes" if hm100 else "no"))
    A("")

    # ---------------- СЦЕНАРИЙ B: порт, без клампа ----------------
    A("=== СЦЕНАРИЙ B: ПОРТ, БЕЗ клампа (сырая сумма) ===")
    set1r, _ = dp(GROUPS, False)
    res2r = enumerate_all(GROUPS, False)
    A("СПОСОБ 1 (DP):      %s" % render_set(set1r))
    A("                       min=%d max=%d n=%d" % (min(set1r), max(set1r), len(set1r)))
    A("СПОСОБ 2 (перебор): %s" % render_set(res2r["finals"]))
    A("                       min=%d max=%d n=%d" % (min(res2r["finals"]),
                                                    max(res2r["finals"]),
                                                    len(res2r["finals"])))
    A("СПОСОБ 2б (арифметика min/max по таблице веток): min=%d  max=%d" % (lo_ar, hi_ar))
    A("путей ровно в +100 (без клампа): %d ; ровно в -100: %d ; всего: %d"
      % (res2r["combos_100"], res2r["combos_m100"], res2r["total"]))
    A("СВЕРКА: множества %s ; арифметика min %s ; арифметика max %s"
      % ("OK" if set1r == res2r["finals"] else "MISMATCH",
         "OK" if lo_ar == min(set1r) else "MISMATCH",
         "OK" if hi_ar == max(set1r) else "MISMATCH"))
    A("")

    # ---------------- СВИДЕТЕЛИ ----------------
    A("=== СВИДЕТЕЛИ (сценарий A, с клампом) ===")
    def show_wit(combo, groups, target):
        if combo is None:
            A("  путь в %+d не найден" % target)
            return
        pos = sum(1 for d in combo if d > 0)
        neg = sum(1 for d in combo if d < 0)
        z = sum(1 for d in combo if d == 0)
        A("  %+d: хороших=%d, плохих=%d, нейтральных=%d" % (target, pos, neg, z))
        run = 0
        for (name, opts), d in zip(groups, combo):
            run = clamp(run + d)
            A("      %-38s %+4d -> %4d" % (name, d, run))
    A("минимум «хороших» выборов для +100:")
    show_wit(res2["wit100"], GROUPS, 100)
    A("минимум «хороших» / максимум «плохих» для -100:")
    show_wit(res2["witm100"], GROUPS, -100)
    st = res2["stats"]
    A("  статистика путей (min/max «хороших» и min/max «плохих»):")
    A("    к +100: %d комбинаций; хороших min/max = %s/%s; плохих min/max = %s/%s"
      % (res2["combos_100"], st[100][0], st[100][1], st[100][2], st[100][3]))
    A("    к -100: %d комбинаций; хороших min/max = %s/%s; плохих min/max = %s/%s"
      % (res2["combos_m100"], st[-100][0], st[-100][1], st[-100][2], st[-100][3]))
    A("")

    # ---------------- СЦЕНАРИЙ C: шаг ±10 ----------------
    A("=== СЦЕНАРИЙ C: шаг приведён к источнику — все дельты ±10 (структура та же) ===")
    G10 = scale_groups(GROUPS, 2)
    setA, _ = dp(G10, False)
    setB, _ = dp(G10, True)
    resC = enumerate_all(G10, True)
    resCraw = enumerate_all(G10, False)
    loC, hiC = arith(G10)
    A("без клампа: min=%d max=%d n=%d ; 100 in set: %s ; -100 in set: %s"
      % (min(setA), max(setA), len(setA), 100 in setA, -100 in setA))
    A("с клампом:  min=%d max=%d n=%d ; 100 in set: %s ; -100 in set: %s"
      % (min(setB), max(setB), len(setB), 100 in setB, -100 in setB))
    A("перебор(с клампом): min=%d max=%d ; совпадение с DP: %s"
      % (min(resC["finals"]), max(resC["finals"]),
         "OK" if resC["finals"] == setB else "MISMATCH"))
    A("арифметика min/max (сырой): %d / %d" % (loC, hiC))
    A("путей в +100: %d ; в -100: %d (с клампом); всего комбинаций: %d"
      % (resC["combos_100"], resC["combos_m100"], resC["total"]))
    A("без клампа — путей ровно в +100: %d ; ровно в -100: %d (из %d)"
      % (resCraw["combos_100"], resCraw["combos_m100"], resCraw["total"]))
    A("")

    # ---------------- СЦЕНАРИЙ D: канон PS2 (оценка) ----------------
    A("=== СЦЕНАРИЙ D: КАНОН PS2, глава 1 (ОЦЕНКА, PROVISIONAL) ===")
    A("Правило построения: из портованной группы исключены те louise-вызовы,")
    A("которые не имеют пары в ps2_source/chapters/chapter_02 (19 шт., см.")
    A("_s1_context.txt, раздел 'Порт без пары'), а значения оставшихся 16")
    A("заменены на значения источника (±10, +20). Структура веток взята от")
    A("порта — предположение, НЕ доказанный факт; число носит оценочный характер.")
    G_CANON = [
        ("G1  ch1_1 меню@124", [(10, "src chapter_02:131"), (0, ""), (-10, "src 145")]),
        ("G2  ch1_1 меню@372", [(10, "src 371"), (0, ""), (-10, "src 385")]),
        ("G3  ch1_1 меню@577", [(-10, "src 646"), (10, "src 613")]),
        ("G4  ch1_2 меню@85", [(10, "src 829"), (0, "порт 112 — без пары в источнике"), (0, "")]),
        ("G5  ch1_3 sprite_choice", [
            (0, "si_room: оба louise-вызова порта без пары"),
            (20, "l_room безусл. src 3901 (+20) + меню@239 opt1"),
            (10, "l_room +20 + меню@239 opt2 (src 3986: -10)"),
            (30, "l_room +20 + меню@239 opt3 (src 3973: +10)"),
            (0, "hallway: оба louise-вызова порта без пары"),
        ]),
        ("G7  ch1_5 меню@89", [(0, "оба louise-вызова порта без пары (журнал, USER DECISION)")]),
        ("G8  ch1_6 меню@67", [(0, ""), (0, ""), (10, "src 1552"), (0, "")]),
        ("G9  ch1_6 меню@433", [(0, "оба без пары"), (0, "оба без пары")]),
        ("G10 ch1_7 меню@123", [(0, ""), (0, ""), (0, "вызов 271 без пары")]),
        ("G11 ch1_8 sprite_choice", [(0, "все 6 louise-вызовов без пары")]),
        ("G12 ch1_9 меню@83", [(10, "src 2565"), (-10, "src 2546")]),
    ]
    setC, _ = dp(G_CANON, False)
    resD = enumerate_all(G_CANON, False)
    loD, hiD = arith(G_CANON)
    A("без клампа (в PS2 клампа нет): min=%d max=%d n=%d ; множество %s"
      % (min(setC), max(setC), len(setC), render_set(setC)))
    A("перебор: min=%d max=%d ; совпадение с DP: %s"
      % (min(resD["finals"]), max(resD["finals"]),
         "OK" if resD["finals"] == setC else "MISMATCH"))
    A("арифметика min/max: %d / %d" % (loD, hiD))
    A("=> по этой оценке в главе 1 канонический максимум louise = %+d, т.е. 100"
      % max(setC))
    A("   НЕ набирается в главе 1 (и -100 тоже). PROVISIONAL — см. оговорку выше.")
    A("")

    # ---------------- ИТОГ ----------------
    A("=== ИТОГОВЫЕ ЧИСЛА ===")
    A("A) порт + кламп:  min=%d  max=%d  n=%d  100=%s  -100=%s"
      % (min(set1), max(set1), len(set1), 100 in set1, -100 in set1))
    A("   (Способ 1 и Способ 2 дали %s)"
      % ("одинаковые множества" if set1 == res2["finals"] else "РАЗНЫЕ множества"))
    A("B) порт без клампа: min=%d  max=%d  n=%d (кратно 20)"
      % (min(set1r), max(set1r), len(set1r)))
    A("   арифметика min/max: %d / %d — %s"
      % (lo_ar, hi_ar, "совпало" if (lo_ar == min(set1r) and hi_ar == max(set1r))
         else "не совпало"))
    A("C) шаг ±10: сырой разброс %+d..%d ; 100 достижимо: %s (без клампа) / %s (с клампом)"
      % (min(setA), max(setA), 100 in setA, 100 in setB))
    A("D) канон PS2 (оценка): %+d..%d ; 100 достижимо: %s"
      % (min(setC), max(setC), 100 in setC))

    text = "\n".join(L) + "\n"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)

    # ASCII-сводка в консоль (без кириллицы)
    print("A(port+clamp)  min=%d max=%d n=%d has100=%s has-100=%s"
          % (min(set1), max(set1), len(set1), 100 in set1, -100 in set1))
    print("  method1==method2: %s" % (set1 == res2["finals"]))
    print("B(port raw)    min=%d max=%d n=%d arith=(%d,%d)"
          % (min(set1r), max(set1r), len(set1r), lo_ar, hi_ar))
    print("C(step 10)     raw=(%d,%d) has100(raw)=%s has100(clamp)=%s"
          % (min(setA), max(setA), 100 in setA, 100 in setB))
    print("D(canon est)   raw=(%d,%d) has100=%s"
          % (min(setC), max(setC), 100 in setC))
    print("combos: total=%d in100=%d in-100=%d" %
          (res2["total"], res2["combos_100"], res2["combos_m100"]))
    print("written: %s" % OUT)


if __name__ == "__main__":
    main()
