# -*- coding: utf-8 -*-
"""Пометка использованных строк transcriptions_ja_ru.csv для части ch4.5.

Берёт пары (voice_name, voice_id) из references/voice_id_map.csv для группы
`ch4.5_` и дописывает имя дорожки в статусную колонку строки очереди
(адресуется HEX-именем VOICE_ID.BIN_%08X.wav) — по образцу
tools/gen_ch4_4_voices.py (логика RE_STATUS_MARK).

Использование:
    python tools/mark_ch4_5_transcriptions.py           # dry-run
    python tools/mark_ch4_5_transcriptions.py --apply   # запись
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANS = os.path.join(BASE, 'transcriptions_ja_ru.csv')
MANIFEST = os.path.join(BASE, 'references', 'voice_id_map.csv')

RE_STATUS_MARK = re.compile(r'\bch\d[\w.]*_\w+_\d+')


def main():
    apply = '--apply' in sys.argv

    rows = []
    for ln in io.open(MANIFEST, encoding='utf-8-sig'):
        ln = ln.strip()
        if not ln or ln.startswith('#') or ln.startswith('voice_name'):
            continue
        parts = ln.split(',')
        if parts[0].startswith('ch4.5_') and len(parts) >= 2 and parts[1].strip().isdigit():
            rows.append((parts[0], int(parts[1])))
    print('manifest ch4.5 rows: %d' % len(rows))
    assert len(rows) == 109, 'expected 109 ch4.5 rows in manifest'

    raw = io.open(TRANS, encoding='utf-8-sig', newline='').read()
    bom = raw.startswith('\ufeff')
    text = raw[1:] if bom else raw
    lines = text.split('\n')
    idx = {}
    for i, ln in enumerate(lines):
        m = re.match(r'^VOICE_ID\.BIN_([0-9A-Fa-f]{8})\.(?:wav|WAV|STV),', ln)
        if m:
            idx[int(m.group(1), 16)] = i

    marks = 0
    already = 0
    missing = []
    for name, vid in rows:
        i = idx.get(vid)
        if i is None:
            missing.append((name, vid))
            continue
        if RE_STATUS_MARK.search(lines[i]):
            already += 1
            continue
        lines[i] = lines[i].rstrip('\r') + '   ' + name + '.wav'
        marks += 1
    print('transcriptions: mark=%d already=%d missing=%d'
          % (marks, already, len(missing)))
    for name, vid in missing[:10]:
        print('  MISSING ROW: %s id=%d (VOICE_ID.BIN_%08X.wav)' % (name, vid, vid))
    if missing:
        return 1

    if not apply:
        print('dry-run OK. Use --apply to write.')
        return 0

    out = ('\ufeff' if bom else '') + '\n'.join(lines)
    io.open(TRANS, 'w', encoding='utf-8', newline='').write(out)
    print('written: +%d marks in transcriptions_ja_ru.csv' % marks)
    return 0


if __name__ == '__main__':
    sys.exit(main())
