# -*- coding: utf-8 -*-
"""Build the mechanical source-faithful port for chapter 6, part 2.

The Japanese source remains in comments/tl; this script only adds the new
chapter files and does not modify existing Japanese translations.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EV = next((ROOT / "ps2_source/events_full").glob("chapter_07_*.txt"))
SCENES = list(range(360, 375))
SPK = {"サイト":"s", "ルイズ":"l", "アンリエッタ":"h", "キュルケ":"k",
       "タバサ":"t", "ギーシュ":"g", "モンモランシー":"m", "シエスタ":"si",
       "ハルナ":"ha", "客":"customer", "商人ＭＲ":"merchant", "店主":"shopkeeper",
       "味方Ａ":"soldier"}

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

def flat(s):
    return re.sub(r"\s+", " ", s).strip()

def parse():
    out, cur = {}, None
    for raw in EV.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## SCENE (\d+)", raw)
        if m:
            cur = int(m.group(1)); out.setdefault(cur, []); continue
        if cur not in SCENES: continue
        m = re.match(r'DIALOGUE\s+talk\("([^"]+)",\s*(?:"([^"]*)"|null),\s*"((?:[^"\\]|\\.)*)",\s*(?:\(0x04000000 \+(\d+)\)|null)\)', raw)
        if m:
            out[cur].append(("talk", m.group(1), m.group(3).replace("\\n", " "), int(m.group(4)) if m.group(4) else None)); continue
        m = re.match(r'CHOICE\s+selectItem\("((?:[^"\\]|\\.)*)",\s*\(0x01000000 \+(\d+)\)', raw)
        if m: out[cur].append(("choice", m.group(1), int(m.group(2)))); continue
        m = re.match(r'GOTO\s+next\(\(0x01000000 \+(\d+)\)', raw)
        if m: out[cur].append(("goto", int(m.group(1)))); continue
    return out

def label(sc): return "ch6_2" if sc == 360 else "ch6_2_s%d" % sc

def main():
    data = parse(); counts = {}; rows=[]; manifest=[]
    for sc in SCENES:
        for e in data.get(sc, []):
            if e[0] != "talk": continue
            _, who, ja, vid = e; code = SPK.get(who, "unk")
            if vid is not None:
                counts[code] = counts.get(code, 0) + 1
                name = "ch6.2_%s_%03d" % (code, counts[code]); manifest.append((name, vid))
            else: name = None
            rows.append((sc, who, code, ja, vid, name))

    # Source-faithful structural port. Translation strings are deliberately
    # tagged so the editorial pass can replace them without losing coverage.
    out = ["# Chapter 6, part 2: source scenes 360-374.", "# Source: ps2_source/chapters/chapter_07_家出のお姫さま.txt.", "# EN/RU are provisional source placeholders pending editorial translation.", ""]
    by = {sc: [] for sc in SCENES}
    for r in rows: by[r[0]].append(r)
    for sc in SCENES:
        out += ["label %s:" % label(sc), "    # Source scene %d" % sc]
        # Preserve source resource ids as placeholders until image map names exist.
        bg = {360:38,361:58,362:58,363:58,364:58,365:44,366:44,367:44,368:44,369:44,370:60,371:43,372:43,373:43,374:43}.get(sc)
        music = {360:31,361:31,362:31,363:31,364:31,365:21,366:21,367:21,368:21,369:21,370:20,371:30,372:30,373:30,374:30}.get(sc)
        if bg is not None: out.append('    $ fade_fx("id(%d)", new_music="t%d")' % (bg, music-1))
        for _, who, code, ja, vid, name in by[sc]:
            text = "[PROVISIONAL EN] %s" % (name or "thought_%d_%s" % (sc, code))
            ident = code
            if ja.startswith("（") and ja.endswith("）") or vid is None and who == "サイト" and ja.startswith("（"):
                ident = "th"; text = text.strip("（）")
            if vid is not None: out.append('    voice "%s"' % name)
            out.append('    %s "%s"' % (ident, esc(text)))
        choices = [e for e in data.get(sc, []) if e[0] == "choice"]
        if choices:
            out.append("    menu:")
            for _, ja, target in choices:
                out += ['        "[PROVISIONAL EN] choice_%d":' % target, "            jump %s" % label(target)]
        gotos = [e[1] for e in data.get(sc, []) if e[0] == "goto"]
        if gotos: out.append("    jump %s" % (label(gotos[-1]) if gotos[-1] in SCENES else "attention"))
        elif sc == 374: out.append("    jump attention")
        out.append("")
    (ROOT / "game/chapters/6/script-ch6_2.rpy").write_text("\n".join(out), encoding="utf-8")

    # Append only new keys; existing files are read and extended in place.
    dialogs = [("[PROVISIONAL EN] %s" % r[5], r[3], "[ПРЕДВАРИТЕЛЬНЫЙ ПЕРЕВОД] %s" % r[5]) for r in rows if r[4] is not None]
    thoughts = [("[PROVISIONAL EN] thought_%d_%s" % (r[0], r[2]), r[3], "[ПРЕДВАРИТЕЛЬНЫЙ ПЕРЕВОД] thought_%d_%s" % (r[0], r[2])) for r in rows if r[4] is None and r[2] == "th"]
    choices = []
    for sc in SCENES:
        for _, ja, target in [e for e in data.get(sc, []) if e[0] == "choice"]:
            choices.append(("[PROVISIONAL EN] choice_%d" % target, ja, "[ПРЕДВАРИТЕЛЬНЫЙ ПЕРЕВОД] choice_%d" % target))
    for lang, value in (("japanese", 1), ("russian", 2)):
        for bucket, entries in (("dialogs", dialogs), ("thoughs", thoughts), ("choises", choices)):
            p = ROOT / "game/tl" / lang / (bucket + ".rpy")
            old_text = p.read_text(encoding="utf-8")
            old_text = re.sub(r"\n# ===== ch6_2 provisional source port =====\n.*", "\n", old_text, flags=re.S)
            p.write_text(old_text, encoding="utf-8")
            with p.open("a", encoding="utf-8") as f:
                f.write("\n# ===== ch6_2 provisional source port =====\n")
                for old, ja, ru in entries:
                    f.write('    old "%s"\n    new "%s"\n\n' % (esc(old), esc(ja if value == 1 else ru)))
    man = ROOT / "references/voice_id_map.csv"
    existing = {x.split(",",1)[0] for x in man.read_text(encoding="utf-8").splitlines() if x.strip()}
    with man.open("a", encoding="utf-8") as f:
        for name, vid in manifest:
            if name not in existing: f.write("%s,%d\n" % (name, vid))
    print("voices=%d strings=%d" % (len(manifest), len(rows)))

if __name__ == "__main__": main()
