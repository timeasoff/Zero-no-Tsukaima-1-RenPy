# -*- coding: utf-8 -*-
"""Добавляет в references/voice_id_map.csv пары ch3.5_* (часть 5 главы 3).

Пары получены сверкой порядка script-ch3_5.rpy с каноном (tools/p5_check_voices.py).
wav_file/notes остаются пустыми — конвертация на финальном этапе части.
"""
import csv
import io
import re
import sys

CANON = "ps2_source/chapters/chapter_04_\u5973\u306e\u6226\u3044.txt"
SCRIPT = "game/chapters/3/script-ch3_5.rpy"
MANIFEST = "references/voice_id_map.csv"

SPK = {
    "\u30b5\u30a4\u30c8": "s",
    "\u30eb\u30a4\u30ba": "l",
    "\u30b7\u30a8\u30b9\u30bf": "si",
    "\u30cf\u30eb\u30ca": "ha",
    "\u30ad\u30e5\u30eb\u30b1": "k",
    "\u30bf\u30d0\u30b5": "t",
    "\u30b3\u30eb\u30d9\u30fc\u30eb": "c",
    "\u30e2\u30f3\u30e2\u30e9\u30f3\u30b7\u30fc": "m",
    "\u30ae\u30fc\u30b7\u30e5": "g",
}

SCENES = (
    list(range(169, 179)) + [179, 180, 181, 182] +
    list(range(1322, 1342))
)


def canon_voice_lines():
    text = io.open(CANON, encoding="utf-8").read().splitlines()
    out = []
    scene = None
    cur = None
    for ln in text:
        m = re.match(r"---- SCENE (\d+) ----", ln)
        if m:
            scene = int(m.group(1))
            cur = None
            continue
        if scene not in SCENES:
            continue
        m = re.match(r"\s*([^\s：:]+)：", ln)
        if m and m.group(1) in SPK:
            cur = SPK[m.group(1)]
        v = re.search(r"\[voice (\d+)\]", ln)
        if v and cur is not None:
            out.append((cur, int(v.group(1))))
    return out


def main():
    canon = canon_voice_lines()
    text = io.open(SCRIPT, encoding="utf-8").read()
    script = [(m.group(1), int(m.group(2)))
              for m in re.finditer(r'voice "ch3\.5_([a-z]+)_(\d+)"', text)]
    assert len(canon) == len(script), (len(canon), len(script))

    new_rows = []
    for (c_spk, vid), (s_spk, s_num) in zip(canon, script):
        assert c_spk == s_spk, (c_spk, s_spk, vid)
        name = "ch3.5_%s_%03d" % (s_spk, s_num)
        new_rows.append([name, str(vid)])

    rows = list(csv.reader(io.open(MANIFEST, encoding="utf-8")))
    have = {r[0] for r in rows if r}
    dup = [r[0] for r in new_rows if r[0] in have]
    if dup:
        print("already present: %d (%s...)" % (len(dup), dup[0]))
        return 1

    with io.open(MANIFEST, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        for r in new_rows:
            w.writerow(r)
    print("appended: %d rows (total now %d)" % (len(new_rows), len(rows) + len(new_rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
