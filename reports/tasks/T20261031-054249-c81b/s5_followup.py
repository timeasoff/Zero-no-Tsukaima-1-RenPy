# -*- coding: utf-8 -*-
"""S5 (поправка 2026-10-31) — дочисления к s5_tundele_reach.py.

Запуск из корня проекта:
    python3 reports/tasks/T20261031-054249-c81b/s5_followup.py

Решает пункты поправки ведущего от 2026-10-31:

П.2 — расхождение «минимум 4 позитивных» vs «127 + 30*3 = 217 >= 211»:
  * почему 3 позитивных без негативных не проходят (структура решений главы);
  * кратчайший по позитивам путь >=211 — со строками events_full всех
    tndl(+30) на пути и итоговым счётом;
  * кратчайший по негативам путь <40 — там же для tndl(-30).

П.3 — уточнение формулы вероятности показа кормёжки при ПОВТОРНЫХ датах
  (ровно по коду getTunDeleScene / dateDone).

П.4 — пары (like Луизы на date(), zero_tundele на date()) на тех же путях,
  что и расчёт п.3 исходного отчёта; перекрёстная таблица like x tundele;
  попытка подобрать порог по like, эквивалентный >=211; итог — PROVISIONAL
  порог или ???

Только чтение ps2_source/ и game/; ничего не пишет кроме stdout.
"""

import collections
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
EVENTS = os.path.join(ROOT, 'ps2_source', 'events_full',
                      'chapter_02_ゼロのルイズ.txt')

START = 6
END = 68
DATE_SCENE = 62
DATE_LINE = 2679
START_VAL = 127

EXTRA_EDGES = {
    63: 1009, 64: 1014, 65: 1019, 66: 1024, 67: 1029,
    25: 1224, 26: 1229, 27: 1234,
    50: 1240, 51: 1245, 52: 1250, 53: 1255,
}

CLAMP_LO, CLAMP_HI = 0, 255


def clamp(v):
    return max(CLAMP_LO, min(CLAMP_HI, v))


def parse(path):
    """-> (edges, tndl_weights, like_weights Луизы, decisions: выборы по сценам)."""
    edges = collections.defaultdict(list)
    weights = collections.defaultdict(int)
    like_w = collections.defaultdict(int)
    tndl_events = []
    menu_options = collections.defaultdict(list)  # scene -> [(line, tgt)]
    cur = None
    with open(path, encoding='utf-8') as fh:
        for i, line in enumerate(fh, 1):
            s = line.strip()
            m = re.match(r'## SCENE (\d+)', s)
            if m:
                cur = int(m.group(1))
                continue
            if cur is None:
                continue
            m = re.match(r'TNDL\s+tndl\((-?\d+|null)\)', s)
            if m:
                if m.group(1) != 'null':
                    add = int(m.group(1))
                    weights[cur] += add
                    tndl_events.append((i, cur, add))
                continue
            if i < DATE_LINE:
                m = re.match(r'LIKE\s+like\("ルイズ",\s*(-?\d+)\)', s)
                if m:
                    like_w[cur] += int(m.group(1))
                    continue
            m = re.match(r'DATE\s+date\(\(0x01000000 \+(\d+)\)', s)
            if m:
                edges[cur].append(('dateprog', int(m.group(1)), None))
                continue
            m = re.match(r'GOTO\s+next\(\(0x01000000 \+(\d+)\),\s*true\)', s)
            if m:
                edges[cur].append(('next', int(m.group(1)), None))
                continue
            m = re.match(
                r'CHOICE\s+selectItem\("([^"]*)",\s*\(0x01000000 \+(\d+)\)', s)
            if m:
                tgt = int(m.group(2))
                edges[cur].append(('sel', tgt, m.group(1)))
                menu_options[cur].append((i, tgt))
                continue
            m = re.match(
                r'DATE\s+dateItem\("([^"]+)",\s*\(0x01000000 \+(\d+)\)\)', s)
            if m:
                edges[cur].append(('date', int(m.group(2)), m.group(1)))
                continue
            m = re.match(
                r'MAPDEST\s+moveItem\("([^"]+)",\s*[^,]+,'
                r'\s*\(0x01000000 \+(\d+)\)\)', s)
            if m:
                edges[cur].append(('move', int(m.group(2)), m.group(1)))
                continue
            m = re.match(r'MOVEINIT\s+moveInit\(\(0x01000000 \+(\d+)\)', s)
            if m:
                edges[cur].append(('moveInit', int(m.group(1)), None))
                continue
    for a, b in EXTRA_EDGES.items():
        edges.setdefault(a, []).append(('manual', b, None))
    return edges, weights, like_w, menu_options, tndl_events


def build_full(edges, scenes):
    full = {s: list(v) for s, v in edges.items()}
    for s in scenes:
        full.setdefault(s, [])
    return full


def topo_order(full, start):
    vis, order = set(), []

    def dfs(u):
        if u in vis:
            return
        vis.add(u)
        for e in full.get(u, []):
            dfs(e[1])
        order.append(u)

    dfs(start)
    order.reverse()
    return order, vis


# --------------------------------------- П.2: структура решений и минимумы ---
def analyze_decisions(full, weights, menu_options):
    """Для каждого решения на путях до date(): опции, знаки tndl, число путей
    через каждую опцию (среди дошедших до date())."""
    # число путей от каждой вершины до date(): forward-DP в том же порядке,
    # что и расчёт путей в s5_tundele_reach.py (рёбра не «в обратную»)
    order, _ = topo_order(full, START)
    ways = collections.defaultdict(int)
    ways[START] = 1
    for s in order:
        if ways.get(s, 0) == 0:
            continue
        if s == DATE_SCENE:
            continue
        if s == END or not full.get(s):
            continue
        for e in full[s]:
            ways[e[1]] += ways[s]
    total = ways[DATE_SCENE]

    print('== П.2: структура решений на путях до date() ==')
    print('всего путей (контроль): %d' % total)
    # обратный счёт: путей ОТ вершины до date()
    rev = collections.defaultdict(list)
    for s in order:
        for e in full.get(s, []):
            rev[e[1]].append(s)
    frm = collections.defaultdict(int)
    frm[DATE_SCENE] = 1
    for s in reversed(order):
        if frm.get(s, 0) == 0:
            continue
        for p in rev[s]:
            frm[p] += frm[s]
    # решения = вершины с несколькими исходящими sel-рёбрами, лежащие на пути
    print('решения с tndl-опциями (знак каждой опции, число путей ЧЕРЕЗ опцию):')
    on_path = []
    off_path = []
    for s in sorted(menu_options):
        opts = menu_options[s]
        if len(opts) < 2:
            continue
        through = ways.get(s, 0) * frm.get(s, 0)
        (on_path if through == total else off_path).append(s)
        if through == 0:
            continue
        parts = []
        for ln, tgt in opts:
            w = weights.get(tgt, 0)
            sign = ('+' if w > 0 else '-' if w < 0 else '0')
            parts.append('%d(%s, line %d, %d путей)' % (
                tgt, sign, ln, ways.get(tgt, 0) * frm.get(tgt, 0)))
        # решения, где все опции одного знака, «обязательный» знак на решении
        signs = {('+' if weights.get(t, 0) > 0 else
                  '-' if weights.get(t, 0) < 0 else '0') for _, t in opts}
        forced = ('  [НЕТ НЕЙТРАЛЬНОЙ ОПЦИИ — знак обязателен]'
                  if '0' not in signs else '')
        print('  решение %d: %s%s' % (s, ' | '.join(parts), forced))
    print('решения на КАЖДОМ пути до date(): %s' % on_path)
    print('решения НЕ на путях до date() (нет путей в сцену 62): %s' % off_path)
    forced_sign = [s for s in on_path
                   if all(weights.get(t, 0) != 0 for _, t in menu_options[s])]
    print('из них БЕЗ нейтральной опции (все опции знаковые): %s' % forced_sign)
    return total, ways


def min_path_for(full, weights, ok, count_sign, tie='value'):
    """Путь к date() с ok(v); минимум числа tndl знака count_sign,
    при равенстве — минимум (или максимум) значения. -> (v, count, path)"""
    order, _ = topo_order(full, START)
    best = {(START, START_VAL): (0, None)}
    entries = {}
    for s in order:
        states = [(v, rec) for (sc, v), rec in best.items() if sc == s]
        if not states:
            continue
        if s == DATE_SCENE:
            for v, rec in states:
                entries[v] = rec
            continue
        add = weights.get(s, 0)
        here = 1 if (add > 0) == (count_sign > 0) and add != 0 else 0
        succ = [e[1] for e in full[s]] if s != END and full.get(s) else []
        for v, (cnt, _) in states:
            v2 = clamp(v + add)
            n2 = cnt + here
            for t in succ:
                key = (t, v2)
                cur = best.get(key)
                if cur is None or n2 < cur[0]:
                    best[key] = (n2, (s, v))
    cand = [(v, rec) for v, rec in entries.items() if ok(v)]
    if not cand:
        return None
    if tie == 'value':
        v_goal, rec = min(cand, key=lambda x: (x[1][0], x[0]))
    else:
        v_goal, rec = min(cand, key=lambda x: (x[1][0], -x[0]))
    path = [(DATE_SCENE, v_goal)]
    node = rec[1]
    while node is not None:
        path.append(node)
        node = best[node][1]
    path.reverse()
    return v_goal, entries[v_goal][0], path


def score_path(weights, tndl_events, path):
    """-> (позитивы, негативы, [события со строками events_full])"""
    pos = neg = 0
    detail = []
    lines_by_scene = collections.defaultdict(list)
    for ln, sc, add in tndl_events:
        lines_by_scene[sc].append((ln, add))
    for sc, _v in path:
        if sc == DATE_SCENE:
            continue
        for ln, add in lines_by_scene.get(sc, []):
            if add > 0:
                pos += 1
            else:
                neg += 1
            detail.append('сцена %d: tndl(%+d) events_full:%d' % (sc, add, ln))
    return pos, neg, detail


# ------------------------------------------- П.4: пары (like, tundele) ---
def joint_paths(full, weights, like_w):
    """Перебор всех путей до date(): множество пар (louise_like, tundele).

    Вес сцены применяется при входе в неё (как в s5_tundele_reach.py),
    фиксируется на входе DATE_SCENE.
    """
    order, _ = topo_order(full, START)
    states = {START: {(START_VAL, 0)}}   # scene -> set((tundele, like))
    for s in order:
        if s not in states:
            continue
        if s == DATE_SCENE:
            break
        out = set()
        add_t = weights.get(s, 0)
        add_l = like_w.get(s, 0)
        for (t, lk) in states[s]:
            out.add((clamp(t + add_t), lk + add_l))
        if s == END or not full.get(s):
            continue
        for e in full[s]:
            states.setdefault(e[1], set()).update(out)
    return states.get(DATE_SCENE, set())


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    edges, weights, like_w, menu_options, tndl_events = parse(EVENTS)
    scenes = set(edges) | {v[1] for lst in edges.values() for v in lst}
    full = build_full(edges, scenes)

    # ---------- П.2 ----------
    total, ways = analyze_decisions(full, weights, menu_options)

    print()
    print('== П.2: кратчайший путь >=211 (минимум позитивных tndl(+30)) ==')
    pp = min_path_for(full, weights, lambda v: v >= 211, +1, tie='value')
    v, cnt, path = pp
    pos, neg, detail = score_path(weights, tndl_events, path)
    print('значение %d, позитивных по DP: %d; пересчёт по событиям: '
          'позитивных %d, негативных %d' % (v, cnt, pos, neg))
    print('события на пути:')
    for d in detail:
        print('   ' + d)
    print('счёт: 127 + 30*(%d) - 30*(%d) = %d (кламп %d)' % (
        pos, neg, START_VAL + 30 * pos - 30 * neg, clamp(
            START_VAL + 30 * pos - 30 * neg)))
    print('путь: %s' % ' -> '.join('%d(@%d)%s' % (
        sc, vv, ' tndl%+d->%d' % (weights[sc], clamp(vv + weights[sc]))
        if weights.get(sc) else '') for sc, vv in path))

    print()
    print('== П.2: путь >=211 с МИНИМУМОМ негативных (0 негативных) ==')
    pp2 = min_path_for(full, weights, lambda v: v >= 211, -1, tie='value')
    v, cnt, path = pp2
    pos, neg, detail = score_path(weights, tndl_events, path)
    print('значение %d, негативных по DP: %d; пересчёт: позитивных %d, '
          'негативных %d' % (v, cnt, pos, neg))
    for d in detail:
        print('   ' + d)
    print('счёт: 127 + 30*(%d) - 30*(%d) = %d (кламп %d)' % (
        pos, neg, START_VAL + 30 * pos - 30 * neg,
        clamp(START_VAL + 30 * pos - 30 * neg)))

    print()
    print('== П.2: кратчайший путь <40 (минимум негативных tndl(-30)) ==')
    pn = min_path_for(full, weights, lambda v: v < 40, -1, tie='value')
    v, cnt, path = pn
    pos, neg, detail = score_path(weights, tndl_events, path)
    print('значение %d, негативных по DP: %d; пересчёт по событиям: '
          'позитивных %d, негативных %d' % (v, cnt, pos, neg))
    print('события на пути:')
    for d in detail:
        print('   ' + d)
    print('счёт: 127 + 30*(%d) - 30*(%d) = %d (кламп %d)' % (
        pos, neg, START_VAL + 30 * pos - 30 * neg, clamp(
            START_VAL + 30 * pos - 30 * neg)))
    print('путь: %s' % ' -> '.join('%d(@%d)%s' % (
        sc, vv, ' tndl%+d->%d' % (weights[sc], clamp(vv + weights[sc]))
        if weights.get(sc) else '') for sc, vv in path))

    # ---------- П.2: пары (npos, nneg), достижимые к date() ----------
    print()
    print('== П.2: достижимые пары (число tndl(+30), число tndl(-30)) к date() ==')
    order, _ = topo_order(full, START)
    st = {START: {(0, 0)}}
    for s in order:
        if s not in st:
            continue
        if s == DATE_SCENE:
            break
        add = weights.get(s, 0)
        out = set()
        for (p, n) in st[s]:
            if add > 0:
                out.add((p + 1, n))
            elif add < 0:
                out.add((p, n + 1))
            else:
                out.add((p, n))
        if s == END or not full.get(s):
            continue
        for e in full[s]:
            st.setdefault(e[1], set()).update(out)
    pairs_ne = st.get(DATE_SCENE, set())
    print('пар: %d; npos min=%d max=%d; nneg min=%d max=%d' % (
        len(pairs_ne), min(p for p, n in pairs_ne), max(p for p, n in pairs_ne),
        min(n for p, n in pairs_ne), max(n for p, n in pairs_ne)))
    print('(3 pos, 0 neg) достижима: %s; (0 pos, 3 neg) достижима: %s' % (
        (3, 0) in pairs_ne, (0, 3) in pairs_ne))
    print('все пары: %s' % sorted(pairs_ne))
    print('минимум позитивных среди путей >=211: %s' % sorted(
        {p for (p, n) in pairs_ne}))
    # сколько негативов нужно минимум, чтобы остаться >=211
    need = sorted({n for (p, n) in pairs_ne
                   if START_VAL + 30 * p - 30 * n >= 211})
    print('минимальное nneg среди путей с npos>=4 (счёт >=211): %s' % need)

    # ---------- П.4 ----------
    print()
    print('== П.4: пары (like Луизы, zero_tundele) на входе date() ==')
    pairs = joint_paths(full, weights, like_w)
    print('пар достижимо: %d' % len(pairs))
    print('like: min=%d max=%d' % (min(p[1] for p in pairs),
                                    max(p[1] for p in pairs)))
    by_like = collections.defaultdict(set)
    by_t = collections.defaultdict(set)
    for t, lk in pairs:
        by_like[lk].add(t)
        by_t[t].add(lk)
    print('перекрёстная таблица (строки = like, значения = tundele):')
    for lk in sorted(by_like):
        print('  like %+4d -> tundele %s' % (lk, sorted(by_like[lk])))
    print()
    # сколько ПУТЕЙ в каждой ячейке
    cnt_cell = collections.Counter()
    order, _ = topo_order(full, START)
    st = {START: collections.Counter({(START_VAL, 0): 1})}
    for s in order:
        if s not in st:
            continue
        if s == DATE_SCENE:
            for (t, lk), c in st[s].items():
                cnt_cell[(lk, t)] += c
            break
        out = collections.Counter()
        add_t = weights.get(s, 0)
        add_l = like_w.get(s, 0)
        for (t, lk), c in st[s].items():
            out[(clamp(t + add_t), lk + add_l)] += c
        if s == END or not full.get(s):
            continue
        for e in full[s]:
            st.setdefault(e[1], collections.Counter()).update(out)
    total2 = sum(cnt_cell.values())
    print('всего путей (контроль): %d' % total2)
    assert total2 == total, 'число путей разошлось с анализом решений'

    hi = [(lk, t) for (lk, t), c in cnt_cell.items() if t >= 211]
    hi_paths = sum(c for (lk, t), c in cnt_cell.items() if t >= 211)
    print('путей >=211: %d (%.4f%%), like на них: %s' % (
        hi_paths, 100.0 * hi_paths / total,
        sorted({lk for (lk, t) in hi})))
    lo = [(lk, t) for (lk, t), c in cnt_cell.items() if t < 40]
    lo_paths = sum(c for (lk, t), c in cnt_cell.items() if t < 40)
    print('путей <40: %d (%.4f%%), like на них: %s' % (
        lo_paths, 100.0 * lo_paths / total,
        sorted({lk for (lk, t) in lo})))

    # распределение ПУТЕЙ по like внутри каждого класса
    def dist(pred):
        d = collections.Counter()
        for (lk, t), c in cnt_cell.items():
            if pred(t):
                d[lk] += c
        return d
    d_hi = dist(lambda t: t >= 211)
    d_lo = dist(lambda t: t < 40)
    print('распределение путей >=211 по like: %s' % sorted(d_hi.items()))
    print('распределение путей <40 по like: %s' % sorted(d_lo.items()))

    # Попытка подобрать порог по like, ближайший к >=211
    print()
    print('порог по like: доля путей с like >= T среди всех путей,')
    print('и пересечение с путями tundele >= 211 (доля Жаккара):')
    like_values = sorted({lk for (lk, _t) in cnt_cell})
    set_hi = {(lk, t) for (lk, t), c in cnt_cell.items() if t >= 211}
    best = None
    for T in like_values:
        set_T = {(lk, t) for (lk, t) in cnt_cell if lk >= T}
        c_T = sum(c for (lk, t), c in cnt_cell.items() if lk >= T)
        inter = set_T & set_hi
        c_int = sum(c for (lk, t), c in cnt_cell.items()
                    if (lk, t) in inter)
        union = set_T | set_hi
        c_un = sum(c for (lk, t), c in cnt_cell.items()
                   if (lk, t) in union)
        jac = c_int / c_un if c_un else 0.0
        # наивная «точность/полнота» по путям
        prec = c_int / c_T if c_T else 0.0
        rec = c_int / hi_paths if hi_paths else 0.0
        print('  like >= %+3d: путей %5d (%5.2f%%), пересечение %4d, '
              'Жаккар %.3f, precision %.3f, recall %.3f' % (
                  T, c_T, 100.0 * c_T / total, c_int, jac, prec, rec))
        if best is None or jac > best[0]:
            best = (jac, T, c_T, prec, rec)
    print('лучший порог по Жаккару: like >= %+d (Жаккар %.3f, '
          'precision %.3f, recall %.3f)' % (best[1], best[0], best[3],
                                             best[4]))

    # и порог по like, дающий ту же ДОЛЮ путей, что и >=211 (9.56%)
    target = 100.0 * hi_paths / total
    print()
    print('порог по like с долей путей, ближайшей к %.4f%% (>=211):' % target)
    for T in like_values:
        c_T = sum(c for (lk, t), c in cnt_cell.items() if lk >= T)
        print('  like >= %+3d: %5.2f%%' % (T, 100.0 * c_T / total))

    # обратное направление: порог like <= T против путей <40 (тун-ветка)
    print()
    print('обратное направление (тун-ветка <40): доля Жаккара для like <= T:')
    set_lo = {(lk, t) for (lk, t), c in cnt_cell.items() if t < 40}
    lo_paths2 = sum(c for (lk, t), c in cnt_cell.items() if t < 40)
    best_lo = None
    for T in like_values:
        c_T = sum(c for (lk, t), c in cnt_cell.items() if lk <= T)
        inter = sum(c for (lk, t), c in cnt_cell.items()
                    if lk <= T and t < 40)
        union = sum(c for (lk, t), c in cnt_cell.items()
                    if lk <= T or t < 40)
        jac = inter / union if union else 0.0
        prec = inter / c_T if c_T else 0.0
        rec = inter / lo_paths2 if lo_paths2 else 0.0
        print('  like <= %+3d: путей %5d (%5.2f%%), пересечение %4d, '
              'Жаккар %.3f, precision %.3f, recall %.3f' % (
                  T, c_T, 100.0 * c_T / total, inter, jac, prec, rec))
        if best_lo is None or jac > best_lo[0]:
            best_lo = (jac, T, prec, rec)
    print('лучший порог для <40 по Жаккару: like <= %+d (Жаккар %.3f, '
          'precision %.3f, recall %.3f)' % (best_lo[1], best_lo[0],
                                            best_lo[2], best_lo[3]))


if __name__ == '__main__':
    main()