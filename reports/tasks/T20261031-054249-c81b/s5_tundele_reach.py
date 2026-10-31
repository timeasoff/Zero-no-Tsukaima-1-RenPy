# -*- coding: utf-8 -*-
"""S5 — достижимость zero_tundele к моменту date() в главе-источнике chapter_02.

Запуск из корня проекта:
    python reports/tasks/T20261031-054249-c81b/s5_tundele_reach.py

Механика (канон, ps2_source/scripts/SCENE_0003.txt):
    zero_tundele: старт 127 (tndl(null), :2711-2712), кламп [0..255] (:2717-2721);
    date(done, restrict, bgm) (:2551-2585): <40 -> getTunScene(),
    >=211 -> getDeleScene(), иначе — обычное дат-меню.

Граф главы строится из ps2_source/events_full/chapter_02_*.txt (канон, точные
вызовы); рёбра — те же, что в s2_graph_maxmin.py (см. его docstring), вес
вершины — сумма её вызовов tndl(±30) ДО сцены дат-меню.

Два независимых метода контроля (как в S2):
  A — DFS с мемоизацией: множество значений на входе дат-меню (кламп по пути);
  B — топологический DP по DAG: множество значений на выходе каждой сцены.
Оба должны дать одинаковое множество. Дополнительно считаются:
  * конкретные пути min/max (реконструкция),
  * минимальное число отрицательных tndl, дающих < 40 (forward DP + parent),
  * распределение числа путей по значениям на входе дат-меню.
"""

import collections
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
EVENTS = os.path.join(ROOT, 'ps2_source', 'events_full',
                      'chapter_02_ゼロのルイズ.txt')

START = 6            # первая сцена главы (там же tndl(null))
END = 68             # первая сцена chapter_03 (граница главы)
DATE_SCENE = 62      # сцена с dateItem(...) + date(...) — дат-меню
DATE_LINE = 2679     # строка events_full с вызовом date(...) (проверяется)

# вентили «невидимых» переходов (см. s2_graph_maxmin.py docstring)
EXTRA_EDGES = {
    63: 1009, 64: 1014, 65: 1019, 66: 1024, 67: 1029,
    25: 1224, 26: 1229, 27: 1234,
    50: 1240, 51: 1245, 52: 1250, 53: 1255,
}

CLAMP_LO, CLAMP_HI, START_VAL = 0, 255, 127


def clamp(v):
    return max(CLAMP_LO, min(CLAMP_HI, v))


def parse(path):
    """-> (edges, tndl_weights, tndl_events, date_scene, date_line)."""
    edges = collections.defaultdict(list)
    weights = collections.defaultdict(int)      # scene -> сумма tndl(±30)
    tndl_events = []                            # (line, scene, add)
    scenes = set()
    cur = None
    date_scene = date_line = None
    with open(path, encoding='utf-8') as fh:
        for i, line in enumerate(fh, 1):
            s = line.strip()
            m = re.match(r'## SCENE (\d+)', s)
            if m:
                cur = int(m.group(1))
                scenes.add(cur)
                continue
            if cur is None:
                continue
            m = re.match(r'TNDL\s+tndl\((-?\d+|null)\)', s)
            if m:
                arg = m.group(1)
                if arg == 'null':
                    tndl_events.append((i, cur, None))
                else:
                    add = int(arg)
                    weights[cur] += add
                    tndl_events.append((i, cur, add))
                continue
            m = re.match(r'DATE\s+date\(\(0x01000000 \+(\d+)\)', s)
            if m:
                date_scene, date_line = cur, i
                edges[cur].append(('dateprog', int(m.group(1)), None))
                continue
            m = re.match(r'GOTO\s+next\(\(0x01000000 \+(\d+)\),\s*true\)', s)
            if m:
                edges[cur].append(('next', int(m.group(1)), None))
                continue
            m = re.match(r'CHOICE\s+selectItem\("([^"]*)",\s*\(0x01000000 \+(\d+)\)',
                         s)
            if m:
                edges[cur].append(('sel', int(m.group(2)), m.group(1)))
                continue
            m = re.match(r'DATE\s+dateItem\("([^"]+)",\s*\(0x01000000 \+(\d+)\)\)',
                         s)
            if m:
                edges[cur].append(('date', int(m.group(2)), m.group(1)))
                continue
            m = re.match(
                r'MAPDEST\s+moveItem\("([^"]+)",\s*[^,]+,\s*\(0x01000000 \+(\d+)\)\)',
                s)
            if m:
                edges[cur].append(('move', int(m.group(2)), m.group(1)))
                continue
            m = re.match(r'MOVEINIT\s+moveInit\(\(0x01000000 \+(\d+)\)', s)
            if m:
                edges[cur].append(('moveInit', int(m.group(1)), None))
                continue
    for a, b in EXTRA_EDGES.items():
        edges.setdefault(a, []).append(('manual', b, None))
    return edges, weights, tndl_events, date_scene, date_line


def build_full(edges, scenes):
    full = {s: list(v) for s, v in edges.items()}
    for s in scenes:
        full.setdefault(s, [])
    return full


# ---------------------------------------------------------------- метод A ---
def method_dfs(full, weights):
    """Множество значений zero_tundele на ВХОДЕ в DATE_SCENE (DFS + мемо)."""
    memo = {}

    def dfs(scene, val):
        if scene == DATE_SCENE:
            return frozenset([val])
        if scene == END or not full.get(scene):
            return frozenset()          # терминал мимо дат-меню — не результат
        key = (scene, val)
        if key in memo:
            return memo[key]
        v2 = clamp(val + weights.get(scene, 0))
        res = set()
        for e in full[scene]:
            res |= dfs(e[1], v2)
        memo[key] = frozenset(res)
        return memo[key]

    return dfs(START, START_VAL)


# ---------------------------------------------------------------- метод B ---
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


def method_dag(full, weights):
    order, vis = topo_order(full, START)
    entry = {START: {START_VAL}}
    for s in order:
        if s not in entry:
            continue
        if s == DATE_SCENE:
            continue                    # значения фиксируются на входе
        v2 = {clamp(v + weights.get(s, 0)) for v in entry[s]}
        if s == END or not full.get(s):
            continue
        for e in full[s]:
            entry.setdefault(e[1], set()).update(v2)
    return frozenset(entry.get(DATE_SCENE, set()))


# ------------------------------------------------------- распределение путей ---
def path_counts(full, weights):
    """Сколько путей приводит к каждому значению на входе DATE_SCENE."""
    order, _ = topo_order(full, START)
    cnt = {START: {START_VAL: 1}}
    dist = collections.Counter()
    for s in order:
        if s not in cnt:
            continue
        cur = cnt[s]
        if s == DATE_SCENE:
            for v, c in cur.items():
                dist[v] += c
            continue
        v2 = collections.Counter()
        add = weights.get(s, 0)
        for v, c in cur.items():
            v2[clamp(v + add)] += c
        if s == END or not full.get(s):
            continue
        for e in full[s]:
            tgt = cnt.setdefault(e[1], collections.Counter())
            for v, c in v2.items():
                tgt[v] += c
    return dist


# ------------------------------------------------------------- пути (цели) ---
def any_path(full, weights, pick):
    """DFS с выбором следующей ветки по pick(лучший из кандидатов).

    pick(best, cand) -> cand, если cand лучше best.  Кандидат — (val, path).
    goal: вход в DATE_SCENE.
    """
    memo = {}

    def dfs(scene, val):
        if scene == DATE_SCENE:
            return (val, [(scene, val)])
        if scene == END or not full.get(scene):
            return None
        key = (scene, val)
        if key in memo:
            return memo[key]
        v2 = clamp(val + weights.get(scene, 0))
        best = None
        for e in full[scene]:
            cand = dfs(e[1], v2)
            if cand is None:
                continue
            if best is None or pick(best, cand):
                best = cand
        memo[key] = None if best is None else (
            best[0], [(scene, val)] + best[1])
        return memo[key]

    return dfs(START, START_VAL)


def min_count_path(full, weights, ok, count_sign):
    """Путь к DATE_SCENE с value, проходящим ok(v), при минимальном числе
    tndl со знаком count_sign (+1 — считаем позитивные, −1 — негативные).

    При равенстве счётчиков выбирается минимальное значение.
    Forward DP по (scene, value): best[(s,v)] = (счётчик, parent).
    """
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
    v_goal, rec = min(cand, key=lambda x: (x[1][0], x[0]))
    path = [(DATE_SCENE, v_goal)]
    node = rec[1]
    while node is not None:
        path.append(node)
        node = best[node][1]
    path.reverse()
    return v_goal, entries[v_goal][0], path


def fmt_path(full, weights, path):
    out = []
    for i, (sc, v) in enumerate(path):
        add = weights.get(sc, 0)
        tag = ''
        if add:
            tag = ' tndl%+d->%d' % (add, clamp(v + add))
        out.append('%d(@%d)%s' % (sc, v, tag))
    return ' -> '.join(out)


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    edges, weights, tndl_events, date_scene, date_line = parse(EVENTS)
    scenes = set(edges) | {v[1] for lst in edges.values() for v in lst}

    print('== Контроль исходных данных ==')
    print('сцена date(): %s (ожидалось 62), строка events_full: %s '
          '(ожидалось %s)' % (date_scene, date_line, DATE_LINE))
    assert date_scene == DATE_SCENE, 'дат-меню не там, где ожидалось'
    assert date_line == DATE_LINE, 'строка date() сместилась'
    print('tndl(null) в сцене %s: %s' % (
        START, any(e[1] == START and e[2] is None for e in tndl_events)))
    before = [e for e in tndl_events if e[0] < date_line and e[2] is not None]
    after = [e for e in tndl_events if e[0] > date_line and e[2] is not None]
    pos = [e for e in before if e[2] > 0]
    neg = [e for e in before if e[2] < 0]
    print('tndl(±) ДО date(): %d = %d×(+30) + %d×(−30)' % (
        len(before), len(pos), len(neg)))
    print('tndl(±) ПОСЛЕ date(): %d (в ветках дат — в расчёт не входят)'
          % len(after))
    print('только ±30? %s' % sorted({e[2] for e in tndl_events
                                     if e[2] is not None}))
    print('вес сцены дат-меню %d: %d' % (DATE_SCENE,
                                         weights.get(DATE_SCENE, 0)))
    assert weights.get(DATE_SCENE, 0) == 0
    print('сцен-источников tndl до даты: %s' % sorted(
        {e[1] for e in before}))
    for ln, sc, add in before:
        print('   events_full:%d  scene %d  tndl(%+d)' % (ln, sc, add))

    full = build_full(edges, scenes)
    cyc = []

    def has_cycles():
        color = {}

        def dfs(u):
            color[u] = 1
            for e in full.get(u, []):
                v = e[1]
                if color.get(v, 0) == 1:
                    return True
                if color.get(v, 0) == 0 and dfs(v):
                    return True
            color[u] = 2
            return False

        for s in sorted(full):
            if color.get(s, 0) == 0 and dfs(s):
                return True
        return False

    cyc = has_cycles()
    print('\n== Граф ==')
    print('узлов: %d, циклов: %s' % (len(full), cyc))

    a = method_dfs(full, weights)
    b = method_dag(full, weights)
    print('\n== Достижимые значения на входе date() ==')
    print('метод A (DFS):  min=%d max=%d |A|=%d' % (min(a), max(a), len(a)))
    print('метод B (DAG):  min=%d max=%d |B|=%d' % (min(b), max(b), len(b)))
    print('совпадение A и B: %s' % (set(a) == set(b)))
    assert set(a) == set(b), 'методы разошлись'
    vals = sorted(a)
    print('значения: %s' % vals)

    print('\n== Пороги date() ==')
    print('<40 (тун-событие):  достижимо: %s; значений: %s' % (
        any(v < 40 for v in vals), [v for v in vals if v < 40]))
    print('>=211 (дэре-событие): достижимо: %s; значений: %s' % (
        any(v >= 211 for v in vals), [v for v in vals if v >= 211]))
    print('обычное дат-меню (40..210): значений: %d' % len(
        [v for v in vals if 40 <= v <= 210]))

    print('\n== Пути ==')
    p_max = any_path(full, weights, lambda best, cand: cand[0] > best[0])
    p_min = any_path(full, weights, lambda best, cand: cand[0] < best[0])
    print('MAX %d: %s' % (p_max[0], fmt_path(full, weights, p_max[1])))
    print('MIN %d: %s' % (p_min[0], fmt_path(full, weights, p_min[1])))
    pn = min_count_path(full, weights, lambda v: v < 40, -1)
    if pn:
        v, negs, path = pn
        print('MIN-NEG <40: значение %d, отрицательных tndl: %d' % (v, negs))
        print('  путь: %s' % fmt_path(full, weights, path))
    else:
        print('MIN-NEG <40: пути нет')
    pp = min_count_path(full, weights, lambda v: v >= 211, +1)
    if pp:
        v, poss, path = pp
        print('MIN-POS >=211: значение %d, позитивных tndl: %d' % (v, poss))
        print('  путь: %s' % fmt_path(full, weights, path))
    else:
        print('MIN-POS >=211: пути нет')
    pn2 = min_count_path(full, weights, lambda v: v >= 211, -1)
    if pn2:
        print('MIN-NEG >=211: значение %d, отрицательных tndl: %d' % (
            pn2[0], pn2[1]))

    dist = path_counts(full, weights)
    total = sum(dist.values())
    print('\n== Распределение путей по значениям на входе date() ==')
    print('всего путей: %d' % total)
    lo = sum(c for v, c in dist.items() if v < 40)
    hi_c = sum(c for v, c in dist.items() if v >= 211)
    print('путей с <40: %d (%.4f%%)' % (lo, 100.0 * lo / total))
    print('путей с >=211: %d (%.4f%%)' % (hi_c, 100.0 * hi_c / total))
    print('значений с путями: %s' % sorted(dist))

    # Число РЕШАЮЩИХ рёбер (меню выбора) на пути: если оно одинаково у всех
    # путей, доли путей выше можно читать как вероятности при случайном выборе.
    order2, _ = topo_order(full, START)
    # forward-DP по (scene) с min/max числа решений
    mn = {START: 0}
    mx = {START: 0}
    for s in order2:
        if s not in mn:
            continue
        if s == END or not full.get(s):
            continue
        for e in full[s]:
            wgt = 1 if e[0] in ('sel', 'date', 'move', 'moveInit') else 0
            for store, pick in ((mn, min), (mx, max)):
                cur = store.get(e[1])
                val = store[s] + wgt
                store[e[1]] = val if cur is None else pick(cur, val)
    print('решений на пути до date(): min=%s max=%s' % (
        mn.get(DATE_SCENE), mx.get(DATE_SCENE)))

    # Точная вероятность значений при равной вероятности вариантов меню:
    # решение -> 1/k по вариантам, безусловный next -> 1 по цели.
    # Вероятность считается по состоянию (scene, value).
    dec_kinds = ('sel', 'date', 'move', 'moveInit')
    prob2 = {(START, START_VAL): 1.0}
    dist_p = collections.defaultdict(float)
    for s in order2:
        states = [(v, p) for (sc, v), p in prob2.items() if sc == s]
        if not states:
            continue
        if s == DATE_SCENE:
            for v, p in states:
                dist_p[v] += p
            continue
        outs = full.get(s) or []
        if not outs:
            continue
        dec = [e for e in outs if e[0] in dec_kinds]
        targets = dec if dec else outs
        add = weights.get(s, 0)
        for v, p in states:
            v2 = clamp(v + add)
            share = p / len(targets)
            for e in targets:
                prob2[(e[1], v2)] = prob2.get((e[1], v2), 0.0) + share
    pr_lo = sum(p for v, p in dist_p.items() if v < 40)
    pr_hi = sum(p for v, p in dist_p.items() if v >= 211)
    print('P(<40) при равных вариантах меню:  %.4f' % pr_lo)
    print('P(>=211) при равных вариантах меню: %.4f' % pr_hi)
    print('сумма вероятностей: %.6f' % sum(dist_p.values()))

    print('\n== Статика порта (game/) ==')
    hit = []
    for dirpath, _dirs, files in os.walk(os.path.join(ROOT, 'game')):
        if 'tl' in dirpath.split(os.sep):
            continue
        for fn in files:
            if not fn.endswith('.rpy'):
                continue
            p = os.path.join(dirpath, fn)
            try:
                data = open(p, encoding='utf-8').read()
            except (UnicodeDecodeError, OSError):
                continue
            for i, line in enumerate(data.splitlines(), 1):
                if 'zero_tundele' in line or re.search(r'\btndl\(', line):
                    hit.append('%s:%d: %s' % (
                        os.path.relpath(p, ROOT), i, line.strip()))
    print('упоминаний zero_tundele/tndl( в game/**/*.rpy: %d' % len(hit))
    for h in hit:
        print('   ', h)

    # --------------------------------------- 6. утечка вероятностной массы ---
    print('\n== 6. Утечка вероятностной массы и общий выход из даты ==')
    order3, _ = topo_order(full, START)
    # доля путей (при равных вариантах меню), доходящих до каждой сцены
    prob_sc = {START: 1.0}
    for s in order3:
        p_s = prob_sc.get(s, 0.0)
        if not p_s:
            continue
        outs = full.get(s) or []
        if not outs:
            print('  терминал S%s: доля путей %.4f (мимо дат-меню)' % (
                s, p_s))
            continue
        if s == DATE_SCENE:
            print('  S62 (date): накоплено %.4f' % p_s)
            continue
        dec = [e for e in outs if e[0] in dec_kinds]
        targets = dec if dec else outs
        for e in targets:
            prob_sc[e[1]] = prob_sc.get(e[1], 0.0) + p_s / len(targets)
    print('  сумма доль на терминалах + дата = %.4f' % sum(
        prob_sc.get(s, 0.0) for s in order3 if not full.get(s)
        or s == DATE_SCENE))

    print('\n  рёбра EXTRA_EDGES и их роль:')
    for st, nxt in sorted(EXTRA_EDGES.items()):
        role = ('выход из даты в dateprog %d' % nxt) if nxt == DATE_SCENE else (
            'локация/карта, возврат по moveDone' if nxt in (1224, 1229, 1234,
                                                            1240, 1245, 1250,
                                                            1255) else
            'нетерминальная сцена')
        print('    S%d -> S%d : %s (доля путей через источник %.4f)' % (
            st, nxt, role, prob_sc.get(st, 0.0)))

    print('\n  выбор комнаты на карте/локации СЛЕПОЙ: ::MoveAdd(info.room,')
    print('  info.pose) и moveDone(param) -> next(info.next) (SCENE_0003);')
    print('  moveInit count=1 у сцен 24/49 и count=3 у сцены 100 —')
    print('  число заходов ограничено, затем move() -> выход из даты.')
    print('  Исходящих GOTO из 1224..1255 в events_full НЕТ (рёбер нет).')


if __name__ == '__main__':
    main()
