# -*- coding: utf-8 -*-
"""Глава 4, часть 3 (P4a): пары voice_name <-> voice_id + пометка очереди транскрипций.

Часть 3 — новая группа голосов `ch4.3_` (нумерация с 001 по говорящему: s 43,
l 21, si 16 (вкл. ？？？-реплику из мешка — пара остаётся si), ha 24, d 3;
итого 107). Пары получены позиционной сверкой порядка script-ch4_3.rpy
с каноном (ch4_canon_p4a.txt, сцены 236–245 идут в порядке источника).
voice_id — ДЕСЯТИЧНЫЙ (как [voice N] источника и как в references/voice_id_map.csv);
строка очереди transcriptions_ja_ru.csv адресуется HEX-именем VOICE_ID.BIN_%08X.wav.

Запуск: python tools/gen_ch4_3_voices.py           — dry-run
        python tools/gen_ch4_3_voices.py --apply   — запись
"""
import io
import re
import sys

BASE = r'D:/gameMake/ZnT-1/ZnT1'
CANON = r'C:/Users/user/AppData/Local/Temp/opencode/ch4_canon_p4a.txt'
SCRIPT = BASE + '/game/chapters/4/script-ch4_3.rpy'
MANIFEST = BASE + '/references/voice_id_map.csv'
TRANS = BASE + '/transcriptions_ja_ru.csv'
SCENE_ORDER = list(range(236, 246))

SPK = {
    'サイト': 's', 'ルイズ': 'l', 'シエスタ': 'si', 'ハルナ': 'ha',
    'キュルケ': 'k', 'タバサ': 't', 'コルベール': 'c', 'オスマン': 'o',
    'モンモランシー': 'm', 'ギーシュ': 'g', 'デルフリンガー': 'd',
}
RE_STATUS_MARK = re.compile(r'\bch\d[\w.]*_\w+_\d+')


def canon_voices():
    scenes = {}
    cur = None
    for line in io.open(CANON, encoding='utf-8'):
        line = line.rstrip('\n')
        m = re.match(r'^SCENE (\d+) \(line \d+\)$', line)
        if m:
            cur = int(m.group(1))
            scenes.setdefault(cur, [])
            continue
        if cur is None:
            continue
        m = re.match(r'^  TALK (\S+) \| v=(\d+) \|', line)
        if m:
            scenes[cur].append((m.group(1), int(m.group(2))))
    out = []
    for sc in SCENE_ORDER:
        out.extend(scenes.get(sc, []))
    return out


def script_voices():
    txt = io.open(SCRIPT, encoding='utf-8').read()
    return [(m.group(1), m.group(2))
            for m in re.finditer(r'voice "ch4\.3_([a-z]+)_(\d+)"', txt)]


def main():
    apply = '--apply' in sys.argv
    canon = canon_voices()
    script = script_voices()
    print('canon voices: %d  script voices: %d' % (len(canon), len(script)))
    if len(canon) != len(script):
        print('COUNT MISMATCH')
        return 1

    rows = []
    for (ja, vid), (spk, num) in zip(canon, script):
        code = SPK.get(ja)
        if code is None:
            print('UNKNOWN SPEAKER: %r' % ja)
            return 1
        if code != spk:
            print('SPEAKER MISMATCH: canon=%s(%s) script=%s_%s'
                  % (ja, code, spk, num))
            return 1
        rows.append(('ch4.3_%s_%s' % (spk, num), vid))

    have = set()
    for line in io.open(MANIFEST, encoding='utf-8-sig'):
        if line.startswith('#'):
            continue
        name = line.split(',', 1)[0].strip()
        if name:
            have.add(name)
    dup = [n for n, _ in rows if n in have]
    if dup:
        print('ALREADY IN MANIFEST: %d (%s)' % (len(dup), dup[0]))
        return 1

    # --- очередь транскрипций: строка по HEX-имени ---
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
        print('  MISSING ROW: %s id=%d (VOICE_ID.BIN_%08X.wav)'
              % (name, vid, vid))
    if missing:
        return 1

    if not apply:
        print('dry-run OK. Use --apply to write.')
        return 0

    with io.open(MANIFEST, 'a', encoding='utf-8', newline='') as f:
        for name, vid in rows:
            f.write('%s,%d\n' % (name, vid))
    out = ('\ufeff' if bom else '') + '\n'.join(lines)
    io.open(TRANS, 'w', encoding='utf-8', newline='').write(out)
    print('written: manifest +%d rows, transcriptions +%d marks'
          % (len(rows), marks))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
