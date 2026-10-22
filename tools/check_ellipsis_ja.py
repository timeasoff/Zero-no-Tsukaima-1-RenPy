# -*- coding: utf-8 -*-
"""Конвенция многоточия: JA (# JA / # JA[id] комментарий) vs EN (сценарий) и RU (tl).

Правило (конвенция проекта; «….»-примечания более ранних частей она
перекрывает — см. резолюцию; в вопросах оба языка — '…?'):
  JA строка целиком '……。'  -> EN/RU '…….' (U+2026 U+2026 '.')
  JA финал  '……。'/'…….'     -> EN '…' (без точки); RU '….'
  JA финал  '……' (без '。')  -> EN/RU '…'
Печатает расхождения и итоговые счётчики.
"""
import io, os, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_tl(lang):
    out = {}
    for bucket in ('dialogs', 'thoughs', 'choises'):
        p = os.path.join(ROOT, 'game', 'tl', lang, bucket + '.rpy')
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8').read()
        for m in re.finditer(r'old "(.*?)"\n\s*new "(.*?)"', txt, re.S):
            out[m.group(1)] = m.group(2)
    return out

def cls(t):
    if t is None:
        return None
    if '…….' in t: return 'SIL'
    if '….' in t:  return 'FIN'
    if t.rstrip().endswith('…?'): return 'Q'
    if '…' in t:   return 'MID'
    return '-'

# ожидаемые классы по языку: EN — '…' без точки в конце строки,
# RU — '….'; вопросы в обоих — '…?' (класс Q).
EXP = {
    'en': {'SIL': {'SIL'}, 'FIN': {'MID', 'Q'}, 'MID': {'MID', 'Q'}},
    'ru': {'SIL': {'SIL'}, 'FIN': {'FIN', 'Q'}, 'MID': {'MID', 'Q'}},
}

def ja_cls(j):
    b = j.strip()
    if b.startswith('（') and b.endswith('）'):
        b = b[1:-1].strip()
    seg = b.split('/')[-1].replace('　', ' ').strip()
    if seg.endswith('……。'):
        return 'SIL' if seg == '……。' else 'FIN'
    if seg.endswith('……') or seg.endswith('…'):
        return 'MID'
    return None

ru = load_tl('russian')
ja_map = load_tl('japanese')

for part in ('3', '4', '5'):
    p = os.path.join(ROOT, 'game', 'chapters', '5', 'script-ch5_%s.rpy' % part)
    if not os.path.exists(p):
        continue
    lines = io.open(p, encoding='utf-8').read().split('\n')
    print('==== part %s ====' % part)
    ok = bad = noru = 0
    for i, ln in enumerate(lines):
        m = re.match(r'\s*\w+ "(.*)"\s*$', ln)
        if not m:
            continue
        en_full = re.sub(r'\{#[^}]+\}$', '', m.group(1))
        if '…' not in en_full:
            continue
        # JA-комментарий идёт ПОСЛЕ своей строки ('# JA:' / '# JA[1234]:')
        ja = None
        for j in (i + 1, i + 2, i - 1, i):
            if 0 <= j < len(lines):
                mm = re.match(r'# JA(?:\[\d+\])?:\s*(.*)$', lines[j].strip())
                if mm:
                    ja = mm.group(1)
                    break
        if ja is None:
            continue
        cj = ja_cls(ja)
        if cj is None:
            continue
        ce = cls(en_full.split('\n')[-1])
        exp = EXP['en'][cj]
        if ce in exp:
            ok += 1
        else:
            bad += 1
            print('  EN BAD JA=%s EN=%s | %s | %s' % (
                cj, ce, ja.split('/')[-1].strip()[-16:], en_full.split('\n')[-1][-36:]))
        # RU
        old = m.group(1)  # старая строка с тегом (как в tl)
        r = ru.get(old) or ru.get(en_full)
        if r is None:
            noru += 1
        else:
            cr = cls(r.split('\n')[-1])
            if cr not in EXP['ru'][cj]:
                print('  RU BAD JA=%s RU=%s | %s | %s' % (
                    cj, cr, ja.split('/')[-1].strip()[-16:], r.split('\n')[-1][-36:]))
    print('  EN ok=%d bad=%d | RU not-found=%d (см. BAD-строки выше)' % (ok, bad, noru))
