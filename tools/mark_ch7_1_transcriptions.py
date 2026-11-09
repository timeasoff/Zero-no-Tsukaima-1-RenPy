# -*- coding: utf-8 -*-
"""Пометить использованные строки transcriptions_ja_ru.csv для ch7_1.

Правило: строки CSV находятся по hex8-коду из имени wav (id -> %08X),
в начало строки добавляется префикс "# USED ch7_1 ". Повторная пометка —
ошибка. (Скилл voice-workflow: идти по id, а не по тексту.)
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_ch7_1_common as CC

PAGE = CC.rel("transcriptions_ja_ru.csv")


def main():
    data = CC.full_check()
    rows = data["voice_rows"]
    lines = io.open(PAGE, encoding="utf-8").read().splitlines()
    by_fname = {}
    for i, ln in enumerate(lines):
        m = re.match(r"^(# USED [^\s]+\s+)?(VOICE_ID\.BIN_([0-9A-Fa-f]{8})\.wav),", ln)
        if m:
            by_fname[m.group(2)] = (i, m.group(1), m.group(3).upper())
    used, bad = 0, []
    for name, vid, wav in rows:
        hx = "%08X" % int(vid)
        fname = "VOICE_ID.BIN_%s.wav" % hx
        if hx not in by_fname and fname not in by_fname:
            bad.append("%s (%s): строки нет в CSV" % (name, fname))
            continue
        key = fname if fname in by_fname else hx
        i, mark, hx2 = by_fname[key]
        if mark:
            # уже помечена; id уникальны в пределах главы — тут это будет
            # повторная попытка пометки (второй прогон) — фиксируем и ругаемся
            raise CC.Fail("%s (%s): строка уже помечена (%r)" % (name, fname, mark))
        if hx2 != hx:
            bad.append("%s (%s): метка id не совпала (%s)" % (name, fname, hx2))
            continue
        lines[i] = u"# USED ch7_1 " + lines[i]
        used += 1
    if bad:
        for b in bad:
            print("ERR:", b)
        raise SystemExit(1)
    io.open(PAGE, "w", encoding="utf-8", newline="\n").write(u"\n".join(lines) + u"\n")
    print("OK: помечено %d строк, всего строк теперь %d" % (used, len(lines)))


if __name__ == "__main__":
    main()
