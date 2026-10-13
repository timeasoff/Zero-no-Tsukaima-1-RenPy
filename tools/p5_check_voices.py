# -*- coding: utf-8 -*-
"""Сверка голосов script-ch3_5.rpy с каноном chapter_04.

1) извлекает voice "ch3.5_<spk>_NNN" в порядке следования;
2) извлекает [voice N] из канонных сцен 169-178 и 1322-1341 (с учётом
   говорящего и порядка);
3) сравнивает: порядок, говорящий, сквозную нумерацию по говорящему;
4) печатает отчёт (только ASCII).
"""
import io
import re
import sys
from collections import Counter

CANON = "ps2_source/chapters/chapter_04_\u5973\u306e\u6226\u3044.txt"
SCRIPT = "game/chapters/3/script-ch3_5.rpy"

SPK = {
    "\u30b5\u30a4\u30c8": "s",      # サイト
    "\u30eb\u30a4\u30ba": "l",      # ルイズ
    "\u30b7\u30a8\u30b9\u30bf": "si",  # シエスタ
    "\u30cf\u30eb\u30ca": "ha",     # ハルナ
    "\u30ad\u30e5\u30eb\u30b1": "k",  # キュルケ
    "\u30bf\u30d0\u30b5": "t",      # タバサ
    "\u30b3\u30eb\u30d9\u30fc\u30eb": "c",  # コルベール
    "\u30e2\u30f3\u30e2\u30e9\u30f3\u30b7\u30fc": "m",  # モンモランシー
    "\u30ae\u30fc\u30b7\u30e5": "g",  # ギーシュ
}

# сцены части 5 в порядке источника
SCENES = (
    list(range(169, 179)) + [179, 180, 181, 182] +
    list(range(1322, 1342))
)


def canon_voice_lines():
    text = io.open(CANON, encoding="utf-8").read().splitlines()
    out = []  # (scene, spk, voice_id)
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
            out.append((scene, cur, int(v.group(1))))
    return out


def script_voice_lines():
    text = io.open(SCRIPT, encoding="utf-8").read()
    out = []  # (spk, num) in order
    for m in re.finditer(r'voice "ch3\.5_([a-z]+)_(\d+)"', text):
        out.append((m.group(1), int(m.group(2))))
    return out


def main():
    canon = canon_voice_lines()
    script = script_voice_lines()
    print("canon voice lines: %d" % len(canon))
    print("script voice lines: %d" % len(script))

    errors = []

    # 1) количество
    if len(canon) != len(script):
        errors.append("COUNT mismatch: canon=%d script=%d"
                      % (len(canon), len(script)))

    # 2) говорящий и порядок
    for i, (c, s) in enumerate(zip(canon, script)):
        if c[1] != s[0]:
            errors.append("SPK mismatch at #%d: canon scene=%d spk=%s, script=%s"
                          % (i, c[0], c[1], s[0]))

    # 3) сквозная нумерация по говорящему
    counters = Counter()
    for i, (c, s) in enumerate(zip(canon, script)):
        counters[c[1]] += 1
        if s[1] != counters[c[1]]:
            errors.append("NUM mismatch at #%d (scene %d): spk=%s expect %03d got %03d"
                          % (i, c[0], c[1], counters[c[1]], s[1]))

    # 4) дубли ключей
    keys = ["%s_%03d" % (s[0], s[1]) for s in script]
    for k, n in Counter(keys).items():
        if n > 1:
            errors.append("DUPLICATE key: %s x%d" % (k, n))

    # 5) итоговые диапазоны
    ranges = {}
    for spk, num in script:
        ranges.setdefault(spk, []).append(num)
    for spk in sorted(ranges):
        nums = ranges[spk]
        print("range %s: %03d..%03d (%d lines)"
              % (spk, min(nums), max(nums), len(nums)))

    if errors:
        print("RESULT: FAIL (%d errors)" % len(errors))
        for e in errors[:50]:
            print("  " + e)
        return 1
    print("RESULT: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
