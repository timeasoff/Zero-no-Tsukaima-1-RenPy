#!/usr/bin/env python3
"""Mark transcription rows consumed by the port/ch22-to-end scope ONLY.

Scope: ch22_5, ch23-28, chapter_90/91 (see tools/voice_audit.py UNITS).
ID is taken from `[voice N]` via voice_name -> voice_id manifest.  The ASR column
`original` is never touched.  Rows already marked (commented filename or a USED
status) are left unchanged.

Usage: python tools/mark_target_transcriptions.py [--apply]
"""
import argparse
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import voice_audit as va

ROOT = Path(__file__).parent.parent
CSV = ROOT / 'transcriptions_ja_ru.csv'
RE_ROW = re.compile(r'^(#+\s*)?VOICE_ID\.BIN_([0-9A-Fa-f]{8})\.(wav|WAV|STV)$')
RE_MARK = re.compile(r'\bch\d[\w.]*_\w+_\d+|#?\s*USED\s+ch\d', re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ns = ap.parse_args()
    man = va.load_manifest()
    id_to_tag = {}
    for unit, src, globs, keep in va.UNITS:
        names, _, _ = va.port_voices(globs, man)
        tag = 'USED ch' + (unit[2:] if unit.startswith('ch') else unit[2:5])
        for n in names:
            if n in man:
                id_to_tag[str(man[n])] = tag
    with open(CSV, encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.reader(fh))
    changed = 0
    for row in rows[1:]:
        if len(row) < 4:
            continue
        m = RE_ROW.match((row[0] or '').strip())
        if not m or m.group(1):
            continue
        vid = str(int(m.group(2), 16))
        status = (row[3] or '').strip()
        if RE_MARK.search(status) or status.startswith('#'):
            continue
        if vid in id_to_tag:
            row[3] = id_to_tag[vid]
            changed += 1
    print('scope_ids=%d will_mark=%d total_rows=%d' % (len(id_to_tag), changed, len(rows) - 1))
    if ns.apply:
        with open(CSV, 'w', encoding='utf-8-sig', newline='') as fh:
            csv.writer(fh).writerows(rows)
        print('written', CSV.name)


if __name__ == '__main__':
    main()
