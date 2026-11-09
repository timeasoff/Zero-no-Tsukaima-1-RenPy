# -*- coding: utf-8 -*-
"""Пометить использованные строки transcriptions_ja_ru.csv для ch7_3.

Правило: строки CSV находятся по hex8-коду из имени wav (id -> %08X),
в начало строки добавляется префикс "# USED ch7_3 ". Повторная пометка —
ошибка. (Скилл voice-workflow: идти по id, а не по тексту.)

Список id берётся из манифеста references/voice_id_map.csv (строки с
voice_name, начинающиеся с "ch7.3_", — 95 штук), поэтому инструмент
самостоятельный и не зависит от генератора.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, "transcriptions_ja_ru.csv")
VOCAB = os.path.join(ROOT, "references", "voice_id_map.csv")


def main():
    rows = []
    for ln in io.open(VOCAB, encoding="utf-8").read().splitlines():
        if ln.startswith("ch7.3_"):
            parts = ln.split(",")
            if len(parts) < 3:
                raise SystemExit("плохая строка манифеста: %r" % ln)
            rows.append((parts[0], parts[1], parts[2]))
    if len(rows) != 95:
        raise SystemExit("в манифесте %d строк ch7.3_ — ожидалось 95" % len(rows))

    lines = io.open(PAGE, encoding="utf-8").read().splitlines()
    by_fname = {}
    for i, ln in enumerate(lines):
        m = re.match(r"^(# USED [^\s]+\s+)?(VOICE_ID\.BIN_([0-9A-Fa-f]{8})\.wav),", ln)
        if m:
            by_fname[m.group(2)] = (i, m.group(1), m.group(3).upper())
    used, bad = 0, []
    for name, vid, _wav in rows:
        hx = "%08X" % int(vid)
        fname = "VOICE_ID.BIN_%s.wav" % hx
        if fname not in by_fname:
            bad.append("%s (%s): строки нет в CSV" % (name, fname))
            continue
        i, mark, hx2 = by_fname[fname]
        if mark:
            raise SystemExit("%s (%s): строка уже помечена (%r)" % (name, fname, mark))
        if hx2 != hx:
            bad.append("%s (%s): метка id не совпала (%s)" % (name, fname, hx2))
            continue
        lines[i] = u"# USED ch7_3 " + lines[i]
        used += 1
    if bad:
        for b in bad:
            print("ERR:", b)
        raise SystemExit(1)
    io.open(PAGE, "w", encoding="utf-8", newline="\n").write(
        u"\n".join(lines) + u"\n")
    print("OK: marked %d rows" % used)


if __name__ == "__main__":
    main()
