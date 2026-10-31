# -*- coding: utf-8 -*-
"""S1, задание 3: сопоставление update_sympathy в game/chapters/1/*.rpy с
【好感度】 в ps2_source/chapters/chapter_02_ゼロのルイズ.txt (файл UTF-8;
CP932 — только ps2_source/scripts/SCENE_*.txt).

Метод (сопоставление «по позиции реплик вокруг»):
  1) якоря: ps2_source/_diagnostics/voice_scene_map.json (voice-имя -> psv-id)
     + [voice N] в chapter_02 дают строку источника для голосовой реплики порта;
  2) событие привязывается к диапазону между ближайшими известными голосовыми
     репликами до/после него; кандидат — 【好感度】 внутри диапазона
     (тот же персонаж приоритетен, короткий диапазон приоритетнее);
  3) классификация пар: SAME (==), X2 (ровно ×2), DIFF (прочее).

Ничего не правит — только читает и пишет UTF-8 отчёт _s1_context.txt.
Японский/русский в консоль не печатается.
"""
import re, os, glob, itertools

ROOT = '/workspace'
OUT = os.path.join(ROOT, 'reports/tasks/T20261031-033403-0df1/_s1_context.txt')

# персонаж источника -> char_key порта; собирается программно и проверяется
# полнотой ниже (исключает опечатку в катакане)
CHARMAP = {}
def _add(ja, key):
    CHARMAP[ja] = key
_add('ル' + 'イズ', 'louise')
_add('シ' + 'エスタ', 'siesta')
_add('タ' + 'バサ', 'tabitha')
_add('キュ' + 'ルケ', 'kirche')
_add('ハ' + 'ルナ', 'haruna')
_add('アン' + 'リエッタ', 'henrietta')

# ---------------- источник ----------------
src_path = os.path.join(ROOT, 'ps2_source/chapters/chapter_02_ゼロのルイズ.txt')
src_lines = open(src_path, encoding='utf-8').read().splitlines()
src_events = []  # (line_no, char, value)
unmapped = set()
for i, l in enumerate(src_lines, 1):
    m = re.search(r'【好感度】(\S+)\s+(-?\d+)', l)
    if m:
        ja = m.group(1)
        if ja not in CHARMAP:
            unmapped.add(ja)
            continue
        src_events.append((i, CHARMAP[ja], int(m.group(2))))
if unmapped:
    raise SystemExit('UNMAPPED CHARS: ' + repr(unmapped))

# ---------------- порт ----------------
HDR = re.compile(r'^(\s*)(menu:|if\b.*:|elif\b.*:|else\s*:|label\b.*:)')
UPD = re.compile(r'update_sympathy\(\s*(-?\d+)\s*(?:,\s*char_key\s*=\s*"([a-z]+)")?\s*\)')

files = sorted(glob.glob(os.path.join(ROOT, 'game/chapters/1/script-ch1_*.rpy')),
               key=lambda p: int(re.search(r'ch1_(\d+)', p).group(1)))
port_events = []  # (file, line, delta, char, context)
for path in files:
    fn = os.path.basename(path)
    lines = open(path, encoding='utf-8').read().splitlines()
    stack = []
    for i, l in enumerate(lines, 1):
        if not l.strip() or l.lstrip().startswith('#'):
            continue
        m = HDR.match(l)
        ind = len(l) - len(l.lstrip())
        if m:
            while stack and stack[-1][0] >= ind:
                stack.pop()
            stack.append((ind, i, l.strip()))
            continue
        while stack and stack[-1][0] >= ind:
            stack.pop()
        u = UPD.search(l)
        if u:
            port_events.append((fn, i, int(u.group(1)), u.group(2) or 'louise',
                                [(ln, t) for _, ln, t in stack]))

# ---------------- выравнивание ----------------
# Якоря: ps2_source/_diagnostics/voice_scene_map.json (voice-имя -> psv-id),
# источник: [voice N] в chapter_02. Событие привязывается к диапазону между
# ближайшими известными голосовыми репликами до/после него в ПОРТЕ; кандидат —
# 【好感度】 внутри диапазона (тот же персонаж приоритетен, короткий диапазон
# приоритетнее). Если диапазона нет — одиночный якорь ±40 строк.
import json
VSM = json.load(open(os.path.join(ROOT, 'ps2_source/_diagnostics/voice_scene_map.json'),
                     encoding='utf-8'))
name2ids = {}
for e in VSM:
    nm, pv = e.get('voice'), e.get('psv')
    if nm and pv:
        name2ids.setdefault(nm, set()).add(int(pv))
id2lines = {}
for i, l in enumerate(src_lines, 1):
    for mm in re.finditer(r'\[voice (\d+)\]', l):
        id2lines.setdefault(int(mm.group(1)), []).append(i)

VOICERE = re.compile(r'voice "([A-Za-z0-9._]+)"')

# голосовые события порта по файлам (в порядке jump-цепочки)
port_voices = []  # (file, line, name, [ids])
for path in files:
    fn = os.path.basename(path)
    for i, l in enumerate(open(path, encoding='utf-8'), 1):
        mm = VOICERE.search(l)
        if mm:
            nm = mm.group(1)
            port_voices.append((fn, i, nm, sorted(name2ids.get(nm, ()))))

def anchor_lines(ev_idx, backward):
    """ближайшие известные voice-якоря (до/после события) -> строки источника"""
    fn, ln = port_events[ev_idx][0], port_events[ev_idx][1]
    fi = files.index(os.path.join(ROOT, 'game/chapters/1', fn))
    key = lambda v: files.index(os.path.join(ROOT, 'game/chapters/1', v[0]))
    if backward:
        cand = [v for v in port_voices
                if key(v) < fi or (key(v) == fi and v[1] < ln)]
        cand.sort(key=lambda v: (key(v), v[1]), reverse=True)
    else:
        cand = [v for v in port_voices
                if key(v) > fi or (key(v) == fi and v[1] > ln)]
        cand.sort(key=lambda v: (key(v), v[1]))
    res = []
    for v in cand:
        lines = []
        for pid in v[3]:
            lines.extend(id2lines.get(pid, ()))
        if lines:
            res.append(sorted(lines))
        if len(res) >= 3:
            break
    return res

MAX_WIDTH = 150   # окно уже 150 строк источника => якорь считается ложным

def find_pair(ev_idx, used_src):
    """-> (src_idx | None, все кандидаты в окне независимо от персонажа)"""
    pe = port_events[ev_idx]
    prevs, nexts = anchor_lines(ev_idx, True), anchor_lines(ev_idx, False)
    best = None
    allcands = set()
    combos = []
    if prevs and nexts:
        for pl in prevs:
            for nl in nexts:
                combos.append((pl, nl))
    elif prevs:
        combos = [(pl, None) for pl in prevs]
    elif nexts:
        combos = [(None, nl) for nl in nexts]
    for pl, nl in combos:
        cands = []
        if pl and nl:
            for a in pl:
                for b in nl:
                    lo, hi = min(a, b), max(a, b)
                    if lo == hi or hi - lo > MAX_WIDTH:
                        continue
                    for si, se in enumerate(src_events):
                        if lo < se[0] < hi:
                            cands.append((si, hi - lo))
        elif pl:
            for a in pl:
                for si, se in enumerate(src_events):
                    if abs(se[0] - a) <= 40:
                        cands.append((si, abs(se[0] - a)))
        elif nl:
            for b in nl:
                for si, se in enumerate(src_events):
                    if abs(se[0] - b) <= 40:
                        cands.append((si, abs(se[0] - b)))
        for si, width in cands:
            allcands.add(si)
            if si in used_src:
                continue          # событие источника уже привязано к другому вызову
            se = src_events[si]
            char_pen = 0 if se[1] == pe[3] else 50
            cost = char_pen + width
            if best is None or cost < best[0]:
                best = (cost, si)
    if best and best[0] < 50:
        return best[1], sorted(allcands)
    return None, sorted(allcands)

pairs = []
used_src = set()
diag = {}
# Ручная привязка (сверена семантически): текст menu-опции порта — перевод
# реплики-выбора источника, но голосовой строки в опции нет, поэтому якоря
# (предыдущая известная реплика) указывают на соседнюю ветку.
#   script-ch1_9.rpy:108 "Don't say such awful things!" (опция bad)
#     == source scene 55, строка 2543 "そんなひどいこと言うなよ！" [voice 10958],
#     【好感度】ルイズ -10 в строке 2546 (port -20 -> X2).
MANUAL = {('script-ch1_9.rpy', 108): 2546}
manual_src = {}
for (mf, ml), mline in MANUAL.items():
    for si, se in enumerate(src_events):
        if se[0] == mline:
            manual_src[(mf, ml)] = si
for ei in range(len(port_events)):
    pe = port_events[ei]
    si, cands = find_pair(ei, used_src)
    diag[ei] = cands
    if si is None and (pe[0], pe[1]) in manual_src:
        si = manual_src[(pe[0], pe[1])]
    if si is not None and si not in used_src:
        pairs.append((ei, si)); used_src.add(si)

n, m = len(port_events), len(src_events)

# ---------------- отчёт ----------------
same = x2 = other = 0
rows = []
for p, s in pairs:
    pe, se = port_events[p], src_events[s]
    pv, sv = pe[2], se[2]
    if pv == sv:
        tag = 'SAME'; same += 1
    elif pv == 2 * sv:
        tag = 'X2'; x2 += 1
    else:
        tag = 'DIFF'; other += 1
    rows.append(f'{tag:4}  {pe[0]}:{pe[1]} {pe[3]} {pv:+d}  <->  '
                f'chapter_02:{se[0]} {se[1]} {sv:+d}')

out = open(OUT, 'w', encoding='utf-8')
out.write('# S1.3 — события порта с контекстом веток + выравнивание с источником\n\n')
out.write('## A. События порта (game/chapters/1) с контекстом веток\n\n')
for fn, ln, delta, char, ctx in port_events:
    out.write(f'{fn}:{ln}  {char} {delta:+d}\n')
    for cln, t in ctx:
        out.write(f'      @ {fn}:{cln}: {t}\n')
out.write('\n## B. События источника (chapter_02, 【好感度】)\n\n')
for ln, ch, v in src_events:
    out.write(f'chapter_02:{ln}  {ch} {v:+d}\n')
out.write('\n## C. Выравнивание (якоря: диапазон между [voice]-репликами порта)\n\n')
out.write(f'порт: {n}, источник: {m}, пар: {len(pairs)}\n\n')
out.write('\n'.join(rows))
out.write('\n\n### Порт без пары:\n')
mp = {p for p, _ in pairs}
used_s = {s for _, s in pairs}
for idx, pe in enumerate(port_events):
    if idx not in mp:
        cands = diag.get(idx, [])
        note = ''
        if cands:
            items = [f'chapter_02:{src_events[c][0]} {src_events[c][1]} '
                     f'{src_events[c][2]:+d}' for c in cands]
            samec = [c for c in cands if src_events[c][1] == pe[3]]
            if samec:
                note = ' | кандидат(ы) того же персонажа уже заняты: ' + '; '.join(
                    f'chapter_02:{src_events[c][0]}' for c in samec)
            else:
                note = ' | в окне только КАНДИДАТЫ ДРУГОГО ПЕРСОНАЖА: ' + '; '.join(items)
        else:
            pv = anchor_lines(idx, True); nv = anchor_lines(idx, False)
            note = f' | окно пусто; якоря до={pv} после={nv}'
        out.write(f'NOPORTSRC  {pe[0]}:{pe[1]} {pe[3]} {pe[2]:+d}{note}\n')
out.write('\n### Источник без пары:\n')
ms = {s for _, s in pairs}
for idx, se in enumerate(src_events):
    if idx not in ms:
        out.write(f'SRCNOPORT  chapter_02:{se[0]} {se[1]} {se[2]:+d}\n')
# расхождения по персонажу: порт-события, у которых в окне только чужие персонажи
char_mm = [idx for idx in range(n) if idx not in mp
           and diag.get(idx)
           and all(src_events[c][1] != port_events[idx][3] for c in diag[idx])]
out.write(f'\n## D. Статистика: SAME={same}, X2={x2}, DIFF={other}, '
          f'порт-без-пары={n-len(pairs)}, источник-без-пары={m-len(pairs)}\n')
out.write(f'Расхождения по персонажу (в окне только кандидаты другого персонажа): '
          f'{len(char_mm)}\n')
for idx in char_mm:
    pe = port_events[idx]
    out.write(f'  CHARMM  {pe[0]}:{pe[1]} {pe[3]} {pe[2]:+d} -> окно: ' + '; '.join(
        f'chapter_02:{src_events[c][0]} {src_events[c][1]} {src_events[c][2]:+d}'
        for c in diag[idx]) + '\n')
out.close()
print('port', n, 'src', m, 'pairs', len(pairs),
      'same', same, 'x2', x2, 'diff', other)
