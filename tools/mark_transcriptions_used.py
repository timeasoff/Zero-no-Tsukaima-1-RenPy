# -*- coding: utf-8 -*-
"""Mark used-but-queued transcription rows as consumed.

For every row in transcriptions_ja_ru.csv that (a) has a VOICE_ID.BIN_<hex>.wav
filename, (b) whose voice_id IS used by some game/chapters/*.rpy voice "..." call,
and (c) whose `status` field is NOT already a USE-mark (comment or chN... token),
set status to "USED <chapter-tag>".  This clears TRANSCRIPT_ROW_STILL_IN_QUEUE
warnings without deleting ASR rows, matching the discipline applied in chapter 5.

Usage:
    python tools/mark_transcriptions_used.py            # dry-run (print counts)
    python tools/mark_transcriptions_used.py --apply     # write transcriptions_ja_ru.csv
"""
import argparse
import csv
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RE_VOICE = re.compile(r"^VOICE_ID\.BIN_([0-9A-Fa-f]{8})\.wav$", re.IGNORECASE)
RE_MARK = re.compile(r"\bch\d[\w.]*_\w+_\d+")  # любой токен вида chX[_Y]_spk_NNN — уже помечено
RE_CH_FROM_NAME = re.compile(r"ch(\d+)")  # часть главы из voice_name, напр. ch3.5_c_001 -> ch3


def used_voice_ids() -> set:
    man_path = ROOT / "references" / "voice_id_map.csv"
    name_to_id = {}
    with open(man_path, encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            nm = (row.get("voice_name") or "").strip()
            vid = (row.get("voice_id") or "").strip()
            if nm and vid and not nm.startswith("#"):
                name_to_id[nm] = vid
    used = set()
    for p in (ROOT / "game" / "chapters").rglob("*.rpy"):
        for name in re.findall(r'voice "([^"]+)"', p.read_text(encoding="utf-8")):
            if name in name_to_id:
                used.add(name_to_id[name])
    return used, name_to_id


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ns = ap.parse_args()

    used, name_to_id = used_voice_ids()
    trans_path = ROOT / "transcriptions_ja_ru.csv"

    changed = 0
    kept = 0
    rows_out = []
    with open(trans_path, encoding="utf-8-sig", newline="") as fh:
        reader = csv.reader(fh)
        header = next(reader)
        for row in reader:
            if len(row) < 4:
                rows_out.append(row)
                continue
            fn = (row[0] or "").strip()
            m = RE_VOICE.match(fn)
            if not m:
                rows_out.append(row)
                kept += 1
                continue
            vid = str(int(m.group(1), 16))
            status = (row[3] or "").strip()
            if RE_MARK.search(status) or status.startswith("#"):
                rows_out.append(row)
                kept += 1
                continue
            # used in a script but row still queued -> mark it
            if vid in used:
                name = name_to_id.get(vid, "") if False else ""
                ch_tag = "USED"
                # try to derive chapter tag from a name that maps to this id
                for nm, iv in name_to_id.items():
                    if iv == vid:
                        mm = RE_CH_FROM_NAME.match(nm)
                        if mm:
                            ch_tag = "USED ch%s" % mm.group(1)
                        break
                row[3] = ch_tag
                changed += 1
                rows_out.append(row)
            else:
                rows_out.append(row)
                kept += 1

    sys.stdout.write("will_mark=%d keep=%d total=%d\n" % (changed, kept, changed + kept))
    if ns.apply:
        with open(trans_path, "w", encoding="utf-8-sig", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(header)
            w.writerows(rows_out)
        sys.stdout.write("written to %s\n" % trans_path.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
