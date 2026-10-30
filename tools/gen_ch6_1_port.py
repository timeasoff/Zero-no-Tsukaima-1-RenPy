# -*- coding: utf-8 -*-
"""Generate the structural first port of chapter 6, part 1.

The source text is authoritative.  EN/RU strings are deliberately marked as
provisional until the editorial translation pass; no source dialogue is lost.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = next((ROOT / "ps2_source/chapters").glob("chapter_07_*.txt"))
EV = next((ROOT / "ps2_source/events_full").glob("chapter_07_*.txt"))
OUT = ROOT / "game/chapters/6/script-ch6_1.rpy"

SCENES = list(range(344, 356)) + list(range(1429, 1449))
SPK = {"サイト": "s", "ルイズ": "l", "シエスタ": "si", "キュルケ": "k",
       "タバサ": "t", "ギーシュ": "g", "モンモランシー": "m",
       "アンリエッタ": "h", "ハルナ": "ha", "客": "customer",
       "商人ＭＲ": "merchant", "店主": "shopkeeper"}

def flat(s):
    return re.sub(r"\s+", " ", s.replace("\n", " ")).strip()

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

def parse_events():
    scenes, cur = {}, None
    for raw in EV.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## SCENE (\d+)", raw)
        if m:
            cur = int(m.group(1)); scenes.setdefault(cur, []); continue
        if cur not in SCENES:
            continue
        m = re.match(r'DIALOGUE\s+talk\("([^"]+)",\s*(?:"([^"]*)"|null),\s*"((?:[^"\\]|\\.)*)",\s*(?:\(0x04000000 \+(\d+)\)|null)\)', raw)
        if m:
            text = m.group(3).replace('\\n', '\n')
            scenes[cur].append(("talk", m.group(1), text, int(m.group(4)) if m.group(4) else None)); continue
        m = re.match(r'CHOICE\s+selectItem\("((?:[^"\\]|\\.)*)",\s*\(0x01000000 \+(\d+)\)', raw)
        if m:
            scenes[cur].append(("choice", m.group(1), int(m.group(2)))); continue
        m = re.match(r'GOTO\s+next\(\(0x01000000 \+(\d+)\)', raw)
        if m:
            scenes[cur].append(("goto", int(m.group(1)))); continue
        m = re.search(r'\[移動\].*?→ scene 808.*?\+(\d+)', raw)
        if m:
            scenes[cur].append(("goto", int(m.group(1)))); continue
    return scenes

def main():
    ev = parse_events()
    counts = {}
    rows = []
    for sc in SCENES:
        rows.append((sc, []))
        for event in ev.get(sc, []):
            if event[0] != "talk":
                continue
            _, spk, text, vid = event
            if vid is None:
                continue
            key = SPK.get(spk, "unk")
            counts[key] = counts.get(key, 0) + 1
            name = "ch6_%s_%03d" % (key, counts[key])
            en = "[PROVISIONAL EN] %s" % name
            ru = "[ПРЕДВАРИТЕЛЬНЫЙ ПЕРЕВОД] %s" % name
            rows[-1][1].append((spk, text, vid, name, en, ru))

    out = ["# Chapter 6, part 1: scenes 344–355 and route extras 1429–1448.",
           "# Source: ps2_source/chapters/chapter_07_家出のお姫さま.txt.",
           "# EN/RU strings are PROVISIONAL placeholders pending editorial translation.",
           "# Scene 360 is intentionally outside this part.", ""]
    labels = {sc: ("ch6" if sc == 344 else "ch6_s%d" % sc) for sc in SCENES}
    for sc in SCENES:
        out += ["label %s:" % labels[sc], "    # Source scene %d" % sc]
        for spk, ja, vid, name, en, ru in dict(rows)[sc]:
            who = SPK.get(spk, "unk")
            out += ['    voice "%s"' % name, '    %s "%s"' % (who, esc(en)),
                    '    # JA[%d]: %s' % (vid, flat(ja))]
        choices = [x for x in ev.get(sc, []) if x[0] == "choice"]
        if choices:
            out.append("    menu:")
            for _, text, target in choices:
                target_label = labels.get(target, "ch6_s%d" % target)
                out += ['        "[PROVISIONAL EN] choice_%d":' % target,
                        '            jump %s' % target_label,
                        '            # JA: %s' % text]
        if sc == 355:
            out.append("    menu:")
            for text, target in (("城前", 1429), ("裏通り", 1434), ("街道", 1439), ("表通り", 1444)):
                out += ['        "[PROVISIONAL EN] route_%d":' % target,
                        '            jump %s' % labels[target],
                        '            # JA: %s' % text]
        gotos = [x[1] for x in ev.get(sc, []) if x[0] == "goto"]
        if gotos:
            target = gotos[-1]
            if target in labels:
                out.append("    jump %s" % labels[target])
            elif target == 360:
                out.append("    jump ch6_2  # scene 360 belongs to the next part")
            else:
                out.append("    jump ch6_2  # next source scene %d" % target)
        elif sc == 1448:
            out.append("    jump ch6_2  # return to the continuation after route extras")
        out.append("")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out), encoding="utf-8")

    tl = {"dialogs": [], "choises": []}
    for sc in SCENES:
        for spk, ja, vid, name, en, ru in dict(rows)[sc]:
            tl["dialogs"].append((en, ja, ru))
        for _, text, target in [x for x in ev.get(sc, []) if x[0] == "choice"]:
            en = "[PROVISIONAL EN] choice_%d" % target
            tl["choises"].append((en, text, "[ПРЕДВАРИТЕЛЬНЫЙ ПЕРЕВОД] choice_%d" % target))
        if sc == 355:
            for text, target in (("城前", 1429), ("裏通り", 1434), ("街道", 1439), ("表通り", 1444)):
                tl["choises"].append(("[PROVISIONAL EN] route_%d" % target, text,
                                       "[ПРЕДВАРИТЕЛЬНЫЙ ПЕРЕВОД] route_%d" % target))
    for lang, col in (("japanese", 1), ("russian", 2)):
        for bucket, entries in tl.items():
            path = ROOT / "game/tl" / lang / ("choises.rpy" if bucket == "choises" else "dialogs.rpy")
            old = path.read_text(encoding="utf-8")
            old = re.sub(r"\n# ===== ch6_1 provisional port =====\n.*?# ===== end ch6_1 =====\n?", "\n", old, flags=re.S)
            path.write_text(old, encoding="utf-8")
            with path.open("a", encoding="utf-8") as fh:
                fh.write("\n# ===== ch6_1 provisional port =====\n")
                for en, ja, ru in entries:
                    fh.write('    old "%s"\n    new "%s"\n\n' % (esc(en), esc(ja if col == 1 else ru)))
                fh.write("# ===== end ch6_1 =====\n")
    man = ROOT / "references/voice_id_map.csv"
    existing = set(x.split(",", 1)[0] for x in man.read_text(encoding="utf-8").splitlines() if x.strip())
    with man.open("a", encoding="utf-8") as fh:
        for sc in SCENES:
            for _, _, vid, name, _, _ in dict(rows)[sc]:
                if name not in existing:
                    fh.write("%s,%d\n" % (name, vid)); existing.add(name)
    print("scenes=%d voices=%d" % (len(SCENES), sum(counts.values())))

if __name__ == "__main__":
    main()
