# -*- coding: utf-8 -*-
"""S2 — граф симпатий chapter_02 (JA) и достижимые min/max.

Запуск из корня проекта:
    python reports/tasks/T20261031-054249-c81b/s2_graph_maxmin.py

Строит граф главы источника `ps2_source/chapters/chapter_02_ゼロのルイズ.txt`
(читаемый вид) + точные вызовы `ps2_source/events_full/chapter_02_ゼロのルイズ.txt`
и считает достижимые значения симпатии по каждому персонажу двумя независимыми
способами:

  Способ A — перебор путей с мемоизацией (DFS от стартовой сцены, состояние =
             вектор из 5 симпатий; возвращает множество векторов на выходе).
  Способ B — топологическая DP по DAG (все сцены → множество векторов на входе).

Оба способа должны дать одинаковые числа (проверка в конце).

Порты с весами 20 (правило «модуль = 20» главы 1) тоже считаются обоими способами.

Граф строится из events_full (канон, точные вызовы), перекрёстно сверяется с
chapters (читаемый вид) — расхождение = ошибка парсинга.

Рёбра (все из events_full):
  GOTO       next((0x01000000 +N), true)          -> next
  CHOICE     selectItem("text", (0x01000000 +N))  -> sel
  DATE       dateItem("girl", (0x01000000 +N))    -> date
  DATE       date((0x01000000 +N), ...)           -> dateprog
  MAPDEST    moveItem("place", img, (0x01000000 +N)) -> move
  MOVEINIT   moveInit((0x01000000 +N), ...)       -> moveInit (главная линия после карты)

Сцены 25/26/27/50/51/52/53/63/64/65/66/67 определены, но в events_full на них
нет входящих рёбер (они — «невидимые» переходы внутри диалоговых окон движка;
внешних ссылок нет — это подтверждено grep по всем `0x01000000 +N`).
Они НЕ достижимы из стартовой сцены 6 и в расчёты не входят.

Сцены-возвраты дат (1013, 1018, 1023, 1028, 1033) ведут `GOTO next 68` —
сцена 68 — первый день главы 03 (за границей chapter_02, вес = 0,
терминальная для целей этой задачи).

Стартовая сцена: 6 (первая сцена файла, `CHAPTER 02 : ゼロのルイズ`).
Терминальные сцены (нет исходящих рёбер): 1228, 1233, 1238, 1244, 1249, 1254,
1255 + сцена 68 (граница главы, конец ветки даты).

Циклов нет (граф — DAG); это проверяется отдельным DFS.
"""

import collections
import functools
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
CHAPTERS = os.path.join(ROOT, 'ps2_source', 'chapters',
                        'chapter_02_ゼロのルイズ.txt')
EVENTS = os.path.join(ROOT, 'ps2_source', 'events_full',
                      'chapter_02_ゼロのルイズ.txt')

# вентили, добавленные вручную (внешних входящих рёбер в events_full нет,
# см. docstring); значение — цель. Обоснование: flow_trace.txt и глава 03.
EXTRA_EDGES = {
    63: 1009, 64: 1014, 65: 1019, 66: 1024, 67: 1029,
    25: 1224, 26: 1229, 27: 1234,
    50: 1240, 51: 1245, 52: 1250, 53: 1255,
}
START = 6
END = 68           # первая сцена chapter_03 (за границей главы)
DATE_MENU = 62     # сцена-владелец блока 【デート】

CHAR_KEY = {
    'ルイズ': 'louise', 'シエスタ': 'siesta', 'キュルケ': 'kirche',
    'タバサ': 'tabitha', 'ハルナ': 'haruna',
}


def parse_events(path):
    """-> (edges, weights, events, scenes)."""
    edges = collections.defaultdict(list)
    weights = collections.defaultdict(lambda: collections.defaultdict(int))
    events = []
    scenes = set()
    cur = None
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
            m = re.match(r'DATE\s+date\(\(0x01000000 \+(\d+)\)', s)
            if m:
                edges[cur].append(('dateprog', int(m.group(1)), None))
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
            m = re.match(r'LIKE\s+like\("([^"]+)",\s*(-?\d+)\)', s)
            if m:
                w = int(m.group(2))
                weights[cur][m.group(1)] += w
                events.append((cur, m.group(1), w, i))
                continue
    for a, b in EXTRA_EDGES.items():
        edges.setdefault(a, []).append(('manual', b, None))
    return edges, weights, events, scenes


def parse_chapters(path):
    """Читаемый вид: контроль числа 【好感度】 и сцен."""
    scenes = set()
    likes = []
    cur = None
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            s = line.strip()
            m = re.match(r'---- SCENE (\d+)', s)
            if m:
                cur = int(m.group(1))
                scenes.add(cur)
                continue
            m = re.search(r'【好感度】(\S+)\s+(-?\d+)', s)
            if m:
                likes.append((cur, m.group(1), int(m.group(2))))
    return scenes, likes


def build_full(edges, scenes):
    """Полный граф: все сцены + сцена END."""
    full = {s: list(v) for s, v in edges.items()}
    for s in scenes:
        full.setdefault(s, [])
    return full


def reachable(full, start):
    seen = set()
    stack = [start]
    while stack:
        x = stack.pop()
        if x in seen:
            continue
        seen.add(x)
        for e in full.get(x, []):
            if e[1] != END:
                stack.append(e[1])
    return seen


def has_cycles(full):
    color = {}

    def dfs(u):
        color[u] = 1
        for e in full.get(u, []):
            v = e[1]
            if v == END:
                continue
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


def terminals(full, scenes):
    out = []
    for s in sorted(scenes):
        if s == END:
            continue
        if not full.get(s):
            out.append(s)
    out.append(END)
    return out


# ---------------------------------------------------------------- способ A ---
def method_dfs(full, weights, chars, start, goal, map_weight=None):
    """A: DFS с мемоизацией.  goal='end' (сцена END/терминал) или 'date'
    (вход в сцену DATE_MENU).  map_weight: None (канон) или число (веса порта)."""
    ci = {c: i for i, c in enumerate(chars)}
    n = len(chars)
    memo = {}

    def apply(state, scene):
        w = weights.get(scene, {})
        t = list(state)
        for c, d in w.items():
            k = d if map_weight is None else (
                map_weight if d > 0 else -map_weight)
            t[ci[c]] += k
        return tuple(t)

    def dfs(scene, state):
        if goal == 'date':
            if scene == DATE_MENU:
                return frozenset([state])
            if scene == END or not full.get(scene):
                return frozenset()  # терминал мимо дат-меню — не результат
        else:
            if scene == END or not full.get(scene):
                return frozenset([state])
        key = (scene, state)
        if key in memo:
            return memo[key]
        st2 = apply(state, scene)
        res = set()
        for e in full[scene]:
            res |= dfs(e[1], st2)
        memo[key] = frozenset(res)
        return memo[key]

    return dfs(start, tuple([0] * n))


# ---------------------------------------------------------------- способ B ---
def method_dag(full, weights, chars, start, goal, map_weight=None):
    """B: топологический порядок, множество векторов на входе каждой сцены."""
    # Kahn по достижимому подграфу
    reach = reachable(full, start)
    reach.add(END)
    indeg = {s: 0 for s in reach}
    for s in reach:
        for e in full.get(s, []):
            if e[1] in reach:
                indeg[e[1]] += 1
    import collections as _c
    q = _c.deque([s for s in reach if indeg[s] == 0 and s != start]
                 if indeg[start] else [start])
    # старт может иметь indeg 0; просто кладём его
    q = _c.deque([start])
    topo = []
    seen = set()
    while q:
        u = q.popleft()
        if u in seen:
            continue
        seen.add(u)
        topo.append(u)
        for e in full.get(u, []):
            v = e[1]
            if v not in reach:
                continue
            if v not in seen:
                q.append(v)
    # т.к. граф DAG, рекурсивный обход надёжнее Kahn с повторами:
    topo = []
    vis = set()

    def dfs(u):
        if u in vis:
            return
        vis.add(u)
        for e in full.get(u, []):
            if e[1] in reach:
                dfs(e[1])
        topo.append(u)

    dfs(start)
    topo.reverse()

    ci = {c: i for i, c in enumerate(chars)}
    n = len(chars)
    entry = {s: set() for s in reach}
    entry[start] = {tuple([0] * n)}
    for s in topo:
        if not entry[s]:
            continue
        if goal == 'date' and s == DATE_MENU:
            continue
        w = weights.get(s, {})
        after = set()
        for st in entry[s]:
            t = list(st)
            for c, d in w.items():
                k = d if map_weight is None else (
                    map_weight if d > 0 else -map_weight)
                t[ci[c]] += k
            after.add(tuple(t))
        if s == END or not full.get(s):
            continue
        for e in full[s]:
            if e[1] in reach:
                entry[e[1]] |= after
    if goal == 'date':
        return frozenset(entry[DATE_MENU])
    # end: объединяем терминалы
    res = set()
    for s in topo:
        if s == END or not full.get(s):
            res |= entry[s] if entry[s] else set()
            # entry в терминал уже не включает вес терминала; вес применяем здесь
            w = weights.get(s, {})
            if w:
                fixed = set()
                for st in entry[s]:
                    t = list(st)
                    for c, d in w.items():
                        k = d if map_weight is None else (
                            map_weight if d > 0 else -map_weight)
                        t[ci[c]] += k
                    fixed.add(tuple(t))
                res -= entry[s]
                res |= fixed
    return frozenset(res)


def summarize(states, chars, label):
    lines = ['### %s' % label]
    for i, c in enumerate(chars):
        vals = sorted({st[i] for st in states})
        lines.append('  %s: min=%d max=%d шаг=%s набор=%s' % (
            CHAR_KEY[c], min(vals), max(vals),
            _step(vals), vals if len(vals) <= 20 else '(длинный)'))
    return '\n'.join(lines)


def _step(vals):
    if len(vals) < 2:
        return '—'
    ds = {vals[i + 1] - vals[i] for i in range(len(vals) - 1)}
    return str(min(ds)) if len(ds) == 1 else str(sorted(ds))


def best_path(full, weights, start, goal, char):
    """Любой путь, дающий min/max по одному персонажу (для отчёта).

    goal='end'  — путь до терминала (END или сцены без исходящих).
    goal='date' — путь, заканчивающийся входом в DATE_MENU (иначе None).
    """
    memo_max, memo_min = {}, {}

    def is_terminal(scene):
        return scene == END or not full.get(scene)

    def go_max(scene, val):
        v = val + weights.get(scene, {}).get(char, 0)
        if goal == 'date':
            if scene == DATE_MENU:
                return (val, [(scene, val)])
            if is_terminal(scene):
                return None
        else:
            if is_terminal(scene):
                return (v, [(scene, v)])
        key = (scene, val)
        if key in memo_max:
            return memo_max[key]
        best = None
        for e in full[scene]:
            cand = go_max(e[1], v)
            if cand is not None and (best is None or cand[0] > best[0]):
                best = cand
        memo_max[key] = None if best is None else (
            best[0], [(scene, val)] + best[1])
        return memo_max[key]

    def go_min(scene, val):
        v = val + weights.get(scene, {}).get(char, 0)
        if goal == 'date':
            if scene == DATE_MENU:
                return (val, [(scene, val)])
            if is_terminal(scene):
                return None
        else:
            if is_terminal(scene):
                return (v, [(scene, v)])
        key = (scene, val)
        if key in memo_min:
            return memo_min[key]
        best = None
        for e in full[scene]:
            cand = go_min(e[1], v)
            if cand is not None and (best is None or cand[0] < best[0]):
                best = cand
        memo_min[key] = None if best is None else (
            best[0], [(scene, val)] + best[1])
        return memo_min[key]

    return go_max(start, 0), go_min(start, 0)


def main():
    edges, weights, events, scenes_ev = parse_events(EVENTS)
    scenes_ch, likes = parse_chapters(CHAPTERS)

    print('== Контроль парсинга ==')
    print('сцен events_full: %d, chapters: %d, совпадение: %s' % (
        len(scenes_ev), len(scenes_ch), scenes_ev == scenes_ch))
    print('LIKE events: %d, 【好感度】 lines: %d, совпадение: %s' % (
        len(events), len(likes), len(events) == len(likes)))
    # сверка событий 1:1
    ev_sorted = sorted((s, c, w) for s, c, w, _ in events)
    ch_sorted = sorted(likes)
    print('события совпадают 1:1: %s' % (ev_sorted == ch_sorted))

    full = build_full(edges, scenes_ev | scenes_ev)
    # сцены без рёбер (25..67) уже есть через EXTRA_EDGES
    print('узлов графа: %d' % len(full))

    cyc = has_cycles(full)
    print('циклы: %s' % cyc)

    reach = reachable(full, START)
    print('достижимо из %d: %d сцен; недостижимы: %s' % (
        START, len(reach), sorted((scenes_ev | {END}) - reach - {END})))

    terms = terminals(full, scenes_ev)
    print('терминальные сцены: %s' % terms)

    chars = sorted({c for w in weights.values() for c in w})
    print('персонажи: %s' % chars)

    for goal in ('date', 'end'):
        for mw, tag in ((None, 'канон JA'), (20, 'веса порта (модуль=20)')):
            a = method_dfs(full, weights, chars, START, goal, mw)
            b = method_dag(full, weights, chars, START, goal, mw)
            same = (set(a) == set(b))
            print()
            print(summarize(a, chars, 'цель=%s, веса=%s, способ A (DFS)' % (
                goal, tag)))
            print('  совпадение A и B: %s (|A|=%d |B|=%d)' % (
                same, len(a), len(b)))

    # лучший путь по Луизе к концу главы (канон)
    print()
    mx, mn = best_path(full, weights, START, 'end', 'ルイズ')
    print('Луиза: max к концу = %d, путь: %s' % (
        mx[0], ' -> '.join(str(s) for s, _ in mx[1])))
    print('Луиза: min к концу = %d, путь: %s' % (
        mn[0], ' -> '.join(str(s) for s, _ in mn[1])))
    mx2, mn2 = best_path(full, weights, START, 'date', 'ルイズ')
    print('Луиза: max к дат-меню = %d, путь: %s' % (
        mx2[0], ' -> '.join(str(s) for s, _ in mx2[1])))
    print('Луиза: min к дат-меню = %d, путь: %s' % (
        mn2[0], ' -> '.join(str(s) for s, _ in mn2[1])))

    # JSON-снимок для отчёта
    out = {
        'scenes': sorted(scenes_ev),
        'start': START, 'end': END, 'date_menu': DATE_MENU,
        'terminals': terms,
        'edges': {str(k): [[e[0], e[1], e[2]] for e in v]
                  for k, v in edges.items()},
        'weights': {str(k): dict(v) for k, v in weights.items()},
        'events': [(s, c, w, ln) for s, c, w, ln in events],
        'reachable': sorted(reach),
        'cycles': cyc,
    }
    snap = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        's2_graph_snapshot.json')
    with open(snap, 'w', encoding='utf-8') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print('\nснимок графа: %s' % os.path.relpath(snap, ROOT))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()