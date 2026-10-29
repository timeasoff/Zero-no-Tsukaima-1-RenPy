# -*- coding: utf-8 -*-
"""Generate chapter 5 part 7 from the PS2 event source.

Scope: scene 341 and route branches 1134-1138 and 1139-1143.
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "ps2_source", "events_full", "chapter_06_本当の想い.txt")
SCRIPT = os.path.join(ROOT, "game", "chapters", "5", "script-ch5_7.rpy")
ORDER = [341, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143]
SPK = {"サイト":"s", "ルイズ":"l", "ハルナ":"ha", "シエスタ":"si",
       "キュルケ":"k", "タバサ":"t", "ギーシュ":"g",
       "モンモランシー":"m", "ウェザリー":"w", "アンリエッタ":"h",
       "デルフリンガー":"d", "null":"th"}
IMG_RE = re.compile(r"image\s*=\s*\(0x02000000 \+(\d+)\)")
X_RE = re.compile(r"\bx\s*=\s*(-?\d+)")
ARG_RE = re.compile(r'"((?:[^"\\]|\\.)*)"|(\bnull\b)|\(0x0[46]000000 \+(\d+)\)')

SPRITES = {}
IMAGES = {}
for path, target in (("references/sprite_id_map.csv", SPRITES), ("references/image_id_map.csv", IMAGES)):
    with io.open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        for line in fh:
            p = line.rstrip("\n").split(",")
            if p and p[0].isdigit():
                target[int(p[0])] = p[1:]  # sprite: name; image: kind, filename

# Some PS2 sprite ids used by this scene are alternate frames in a known
# character block but are not yet listed in the project map. Keep these
# evidence-based provisional mappings local until the reference table is
# updated with the corresponding archive proof.
SPRITE_OVERRIDES = {
    314: "l 6", 501: "si 1", 688: "k 1", 633: "t 1", 864: "m 2",
    776: "h 3", 359: "l 6", 365: "l 6", 366: "l 6",
    363: "l 6", 361: "l 6",
    500: "si 1", 506: "si 1", 511: "si 1", 513: "si 1",
    516: "si 1", 517: "si 1", 519: "si 1", 520: "si 1",
}


def args(raw):
    vals, vid = [], None
    for m in ARG_RE.finditer(raw):
        if m.group(3): vid = int(m.group(3))
        elif m.group(2): vals.append("null")
        else: vals.append(m.group(1).replace('\\"', '"').replace('\\\\', '\\'))
    return (vals + ["null", "", ""])[:3] + [vid]


def parse():
    scenes, cur = {}, None
    with io.open(SRC, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            m = re.match(r"^## SCENE (\d+)", line)
            if m:
                cur = int(m.group(1)); scenes[cur] = []; continue
            if cur not in ORDER: continue
            if line.startswith("SET "):
                m = re.match(r'^SET\s+set\("(\w+)",\s*\{(.*)\}\)', line)
                if not m: continue
                layer, body = m.groups(); img = IMG_RE.search(body); x = X_RE.search(body)
                hide = "hide = 1" in body or "show = 0" in body
                if layer == "stage": scenes[cur].append(("bg_hide",) if hide else ("bg", int(img.group(1))) if img else ("noop",))
                elif layer == "event": scenes[cur].append(("cg_hide",) if hide else ("cg", int(img.group(1))) if img else ("noop",))
                elif layer == "bgm":
                    p = re.search(r"play\s*=\s*\(0x03000000 \+(\d+)\)", body)
                    scenes[cur].append(("bgm", int(p.group(1))) if p else ("stop",) if "stop" in body else ("noop",))
                elif layer == "white":
                    scenes[cur].append(("white_hide",) if hide else ("white",))
                elif layer.startswith("lay"):
                    scenes[cur].append(("sprite_hide", layer) if hide else ("sprite", layer, int(img.group(1)), int(x.group(1)) if x else None) if img else ("sprite_pos", layer, int(x.group(1))) if x else ("noop",))
            elif line.startswith("DIALOGUE"):
                parsed = args(line[line.index("(")+1:-1])
                scenes[cur].append(("talk",) + tuple(parsed))
            else:
                m = re.match(r'^CHOICE\s+selectItem\("((?:[^"\\]|\\.)*)",\s*\(0x01000000 \+(\d+)\)', line)
                if m: scenes[cur].append(("choice", m.group(1), int(m.group(2))))
                m = re.match(r'^GOTO\s+next\(\(0x01000000 \+(\d+)\)', line)
                if m: scenes[cur].append(("goto", int(m.group(1))))
    return scenes


def load_translations():
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import ch5_7_en as en_mod
    import ch5_7_ru as ru_mod
    EN_DIALOGS = getattr(en_mod, "EN_DIALOGS", {})
    EN_THOUGHTS = getattr(en_mod, "EN_THOUGHTS", {})
    EN_CHOICES = getattr(en_mod, "EN_CHOICES", {})
    RU_DIALOGS = getattr(ru_mod, "RU_DIALOGS", {})
    RU_THOUGHTS = getattr(ru_mod, "RU_THOUGHTS", {})
    RU_CHOICES = getattr(ru_mod, "RU_CHOICES", {})
    return EN_DIALOGS, EN_THOUGHTS, EN_CHOICES, RU_DIALOGS, RU_THOUGHTS, RU_CHOICES


def main():
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); ap.add_argument("--manifest", action="store_true")
    ns = ap.parse_args(); scenes = parse(); en, eth, choices, ru, rth, rchoices = load_translations()
    names, by_event, manifest = {}, {}, [] ; counts = {}; thought_no = 0; missing = []
    for sc in ORDER:
        for idx, ev in enumerate(scenes.get(sc, [])):
            if ev[0] != "talk": continue
            spk, _disp, text, vid = ev[1:]
            if vid is None: continue
            key = SPK.get(spk, "x"); counts[key] = counts.get(key, 0) + 1
            name = "ch5.7_%s_%03d" % (key, counts[key]); names[(sc, idx)] = name; manifest.append((name, vid, text))
    out = ["# Глава 5, часть 7: сцена 341 + route branches 1134/1139.", "# Generated from ps2_source/events_full/chapter_06_本当の想い.txt.", "", "label ch5_7:"]
    state = {"layers": {}}
    def emit(sc, indent="    "):
        nonlocal thought_no
        for idx, ev in enumerate(scenes.get(sc, [])):
            k = ev[0]
            if k == "bg":
                p = IMAGES.get(ev[1], []); fn = p[1] if len(p) > 1 and p[1] else "id(%d)" % ev[1]
                out.append('%s$ fade_fx("%s")  # BG +%d' % (indent, fn, ev[1]))
            elif k == "bg_hide": out.append('%s$ fade_fx("black")' % indent)
            elif k == "cg":
                p = IMAGES.get(ev[1], []); fn = p[1] if len(p) > 1 and p[1] else "id(%d)" % ev[1]
                out.append('%s$ fade_fx("%s", type="cg")' % (indent, fn))
            elif k == "cg_hide": out.append('%s$ fade_fx("black")' % indent)
            elif k == "bgm": out.append("%splay music t%d fadein 1.0" % (indent, ev[1]-1))
            elif k == "stop": out.append("%sstop music fadeout 1.0" % indent)
            elif k == "white": out.append('%s$ flash_fx("white")' % indent)
            elif k == "white_hide": out.append('%s$ flash_fx("white")' % indent)
            elif k == "sprite":
                layer, image = ev[1], ev[2]; state["layers"][layer] = image
                names_now = [SPRITES.get(v, [SPRITE_OVERRIDES.get(v, "id(%d)" % v)])[0] for v in state["layers"].values()]
                out.append('%s$ show_sprites((%s))  # %s +%d' % (indent, ", ".join('"%s"' % x for x in names_now), layer, image))
            elif k == "sprite_hide":
                state["layers"].pop(ev[1], None); names_now = [SPRITES.get(v, [SPRITE_OVERRIDES.get(v, "id(%d)" % v)])[0] for v in state["layers"].values()]
                out.append("%s$ show_sprites((%s))" % (indent, ", ".join('"%s"' % x for x in names_now)))
            elif k == "sprite_pos": pass
            elif k == "talk":
                spk, _disp, text, vid = ev[1:]; who = SPK.get(spk, "th")
                if vid is None:
                    thought_no += 1; tag = "ch5.7_th_%03d" % thought_no; val = eth.get(tag)
                    if val is None: missing.append((tag, text)); val = "@@MISSING_%s@@" % tag
                    if text.startswith("（") or spk == "null":
                        who = "th"
                    else:
                        who = SPK.get(spk, "th")
                    out.append('%s%s "%s{#%s}"' % (indent, who, val.replace("\n", " "), tag))
                else:
                    name = names[(sc, idx)]; val = en.get(name)
                    if val is None: missing.append((name, text)); val = "@@MISSING_%s@@" % name
                    out.extend(["%svoice \"%s\"" % (indent, name), '%s%s "%s{#ch5_7_v%s}"' % (indent, who, val.replace("\n", " "), vid)])
    emit(341)
    out += ["    $ zero_route = compute_zero_route()", "    if zero_route == 1:", "        jump ch5_7_r1_louise", "    elif zero_route == 2:", "        jump ch5_8_r2_kirche", "    elif zero_route == 3:", "        jump ch5_8_r3_tabitha", "    elif zero_route == 4:", "        jump ch5_7_r4_siesta", "    elif zero_route == 5:", "        jump ch5_9_r5_henrietta", "    else:", "        jump ch5_9_r6_haruna", ""]
    def branch(label, head, choices_sc, rejoin):
        out.append("label %s:" % label); emit(head); out.append("    menu:")
        for target in choices_sc:
            text = next((e[1] for e in scenes[head] if e[0] == "choice" and e[2] == target), "@@MISSING_CHOICE@@")
            choice_key = str(target)
            choice_text = choices.get(choice_key, text)
            out.append('        "%s{#ch5_7_c%s}":' % (choice_text, choice_key)); emit(target, "            "); out.append("            jump %s" % rejoin)
        out.append("label %s:" % rejoin); emit({"ch5_7_r1_rejoin":1138, "ch5_7_r4_rejoin":1143}[rejoin]); out.append("    jump ch5_10")
    branch("ch5_7_r1_louise", 1134, [1135,1136,1137], "ch5_7_r1_rejoin")
    branch("ch5_7_r4_siesta", 1139, [1140,1141,1142], "ch5_7_r4_rejoin")
    print("voices by speaker:", counts); print("total voices:", len(manifest)); print("missing translations:", len(missing))
    for key, text in missing: print("  %s: %s" % (key, text.replace("\n", " / ")[:100]))
    if missing and (ns.apply or ns.manifest):
        raise SystemExit("Refusing to write part 7: translations are incomplete")
    if ns.apply:
        with io.open(SCRIPT, "w", encoding="utf-8") as fh: fh.write("\n".join(out) + "\n")
    if ns.manifest:
        path = os.path.join(ROOT, "references/voice_id_map.csv")
        have = set()
        if os.path.exists(path):
            with io.open(path, encoding="utf-8") as fh:
                have = {line.split(",", 1)[0] for line in fh if line.strip() and not line.startswith("#")}
        with io.open(path, "a", encoding="utf-8") as fh:
            for name, vid, _ in manifest:
                if name not in have:
                    fh.write("%s,%d\n" % (name, vid))
    print("voice map:")
    for name, vid, text in manifest: print("  %s = %d | %s" % (name, vid, text.replace("\n", " / ")))

if __name__ == "__main__": main()
