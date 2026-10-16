#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ch3_align — механическая построчная выверка главы 3 (EN-база + оба tl против JA-канона).

Источник канона: ps2_source/events_full/chapter_04*.txt (точные аргументы talk/
selectItem/dateItem, порядок сцен). Для каждой строки EN-скрипта части строится
трио: JA-канон / EN / RU (+ JA-tl сверяется с каноном дословно).

Кандидаты (flags) — НЕ вердикт, только сигнал к проверке (AGENTS.md §5):
  MISMATCH_JA   new в tl/japanese != JA-канон (дословно, '\\n' канона склеен)
  NO_JA / NO_RU в tl нет old для строки скрипта (дубль E4/E5, но локально)
  RU_EQ_EN      new в tl/russian дословно == EN-строке (подозрение копипаста)
  NO_CANON      строка скрипта не сопоставлена с каноном источника
  UNPORTED      канон охвата без строки скрипта (выпавшая реплика)
  DUP_EN        одинаковый EN при разных JA-канонах (один old не различит)
  CHOICE_TAG    расхождение текста пункта меню с selectItem (после снятия {#..})

Evidence (UTF-8): reports/sma/ch3/chapter/align_p{N}.md
Консоль — только ASCII (cp1251).

Пример:  python tools/ch3_align.py --part 1
         python tools/ch3_align.py --all
"""
from __future__ import annotations

import argparse
import csv
import datetime
import glob
import io
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from output_util import ensure_safe_output, safe_print  # noqa: E402

ROOT = Path(__file__).parent.parent
CH_DIR = ROOT / "game" / "chapters" / "3"
TL_DIRS = {"ja": ROOT / "game" / "tl" / "japanese",
           "ru": ROOT / "game" / "tl" / "russian"}
EVT_GLOB = str(ROOT / "ps2_source" / "events_full" / "chapter_04*.txt")
MANIFEST = ROOT / "references" / "voice_id_map.csv"
OUT_DIR = ROOT / "reports" / "sma" / "ch3" / "chapter"

PARTS = list(range(1, 10))

# ---------------------------------------------------------------- регэкспы
EVT_SCENE_RE = re.compile(r"^## SCENE (\d+)")
EVT_DLG_RE = re.compile(
    r'^DIALOGUE\s+talk\((?:"((?:[^"\\]|\\.)*)"|null),\s*'
    r'(?:"(?:[^"\\]|\\.)*"|null),\s*"((?:[^"\\]|\\.)*)",\s*(.+)\)\s*$')
EVT_CHOICE_RE = re.compile(r'^CHOICE\s+selectItem\("((?:[^"\\]|\\.)*)"')
EVT_MOVE_RE = re.compile(r'^MAPDEST\s+moveItem\("((?:[^"\\]|\\.)*)"')
EVT_DATE_RE = re.compile(r'^DATE\s+dateItem\("((?:[^"\\]|\\.)*)",\s*\(0x01000000 \+(\d+)\)\)')
EVT_VOICE_ID_RE = re.compile(r"\(0x04000000 \+(\d+)\)")

SC_SCRIPT_RE = re.compile(r"#\s*=+\s*SCENE\s+(\d+)")
SC_CHOICE_RE = re.compile(r"#\s*=+\s*(?:CHOISE|CHOICE)\s*\(scene\s*(\d+)\)")
SC_VOICE_RE = re.compile(r'^\s*voice\s+"((?:[^"\\]|\\.)*)"\s*$')
SC_SAY_RE = re.compile(r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s+("(?:[^"\\]|\\.)*")\s*$')
SC_ITEM_RE = re.compile(r'^\s*("(?:[^"\\]|\\.)*")\s*(?:if\b[^:]*)?:\s*$')
SC_OVERLAY_RE = re.compile(
    r'call\s+overlay_screen\(\s*"(?:[^"]*)"\s*,\s*("(?:[^"\\]|\\.)*")')
SC_DICT_RE = re.compile(r'"text":\s*("(?:[^"\\]|\\.)*")')
SC_MENU_RE = re.compile(r'^\s*menu:\s*$')

SAY_KEYWORDS = {
    "if", "elif", "else", "while", "for", "return", "jump", "call", "label",
    "menu", "python", "init", "define", "default", "scene", "show", "hide",
    "with", "play", "stop", "pause", "voice", "queue",
}

TAG_RE = re.compile(r"\{#[^}]*\}")


def _unquote(raw):
    """Снять внешние кавычки Ren'Py, раскрыть \\\" и \\\\ (но не \\n)."""
    s = raw[1:-1]
    return s.replace('\\"', '"').replace("\\\\", "\\")

# ---------------------------------------------------------------- TL-словари
def load_tl():
    """-> ({lang: {old: new}}, {lang: {old: [(file,line)]}}, dup-сообщения)"""
    maps = {"ja": {}, "ru": {}}
    spots = {"ja": {}, "ru": {}}
    dups = []
    for lang, d in TL_DIRS.items():
        for path in sorted(d.glob("*.rpy")):
            pending_old = None
            for i, line in enumerate(
                    io.open(path, encoding="utf-8").read().splitlines(), 1):
                m = re.match(r'^\s*old\s+("(?:[^"\\]|\\.)*")\s*$', line)
                if m:
                    pending_old = _unquote(m.group(1))
                    continue
                m = re.match(r'^\s*new\s+("(?:[^"\\]|\\.)*")\s*$', line)
                if m and pending_old is not None:
                    new = _unquote(m.group(1))
                    if pending_old in maps[lang]:
                        dups.append("%s DUP old in %s:%d (first %s:%d)" % (
                            lang, path.name, i,
                            spots[lang][pending_old][0][0],
                            spots[lang][pending_old][0][1]))
                    else:
                        maps[lang][pending_old] = new
                        spots[lang].setdefault(pending_old, []).append(
                            (path.name, i))
                    pending_old = None
    return maps, spots, dups


def load_voices():
    out = {}
    with io.open(MANIFEST, encoding="utf-8-sig", newline="") as f:
        for row in csv.reader(f):
            if not row or row[0].startswith("#") or row[0] == "voice_name":
                continue
            try:
                out[row[0]] = int(row[1])
            except (IndexError, ValueError):
                continue
    return out


# ---------------------------------------------------------------- канон JA
def load_canon():
    """-> (by_id: {int: (scene, speaker, text)}, by_scene: {scene: [item]})

    item: {'kind': 'dlg'|'choice'|'date', 'id': int|None, 'speaker': str,
           'text': str}
    text — канон со склеенными '\\n' (конвенция tl/japanese: new без '\\n').
    """
    path = Path(glob.glob(EVT_GLOB)[0])
    by_id, by_scene = {}, {}
    scene = None
    for line in io.open(path, encoding="utf-8").read().splitlines():
        m = EVT_SCENE_RE.match(line)
        if m:
            scene = int(m.group(1))
            by_scene.setdefault(scene, [])
            continue
        m = EVT_DLG_RE.match(line)
        if m:
            spk, text, last = m.group(1), m.group(2), m.group(3).strip()
            text = text.replace("\\n", "")
            vid = None
            vm = EVT_VOICE_ID_RE.search(last)
            if vm:
                vid = int(vm.group(1))
            item = {"kind": "dlg", "id": vid, "speaker": spk, "text": text}
            if scene is not None:
                by_scene[scene].append(item)
            if vid is not None:
                by_id[vid] = (scene, spk, text)
            continue
        m = EVT_CHOICE_RE.match(line)
        if m and scene is not None:
            by_scene[scene].append(
                {"kind": "choice", "id": None, "speaker": None,
                 "text": m.group(1).replace("\\n", "")})
            continue
        m = EVT_MOVE_RE.match(line)
        if m and scene is not None:
            # moveItem — пункты карты 【移動】: текст отображается как choice
            by_scene[scene].append(
                {"kind": "choice", "id": None, "speaker": None,
                 "text": m.group(1).replace("\\n", "")})
            continue
        m = EVT_DATE_RE.match(line)
        if m and scene is not None:
            by_scene[scene].append(
                {"kind": "date", "id": int(m.group(2)), "speaker": None,
                 "text": m.group(1)})
    return by_id, by_scene


# ---------------------------------------------------------------- скрипт
def parse_script(path):
    """-> (entries, scenes) — entries в порядке следования строк файла.

    entry: {'line','kind': 'voiced'|'novoice'|'choice'|'overlay',
            'speaker','text','voice','scene'}
    """
    entries = []
    scenes = set()
    cur_scene = None
    choice_scene = None
    menu_scene = None
    pending_voice = None
    for i, raw in enumerate(io.open(path, encoding="utf-8").read().splitlines(), 1):
        m = SC_CHOICE_RE.search(raw)
        if m:
            choice_scene = int(m.group(1))
            scenes.add(choice_scene)
            continue
        m = SC_SCRIPT_RE.search(raw)
        if m:
            cur_scene = int(m.group(1))
            scenes.add(cur_scene)
            continue
        if raw.lstrip().startswith("#"):
            continue
        m = SC_VOICE_RE.match(raw)
        if m:
            pending_voice = m.group(1)
            continue
        if SC_MENU_RE.match(raw):
            # сцена меню фиксируется здесь: пункты после ветвления не должны
            # наследовать SCENE-маркер внутренней ветки
            menu_scene = choice_scene if choice_scene is not None else cur_scene
            continue
        m = SC_OVERLAY_RE.search(raw)
        if m:
            entries.append({"line": i, "kind": "overlay", "speaker": None,
                            "text": _unquote(m.group(1)), "voice": None,
                            "scene": cur_scene})
            continue
        m = SC_SAY_RE.match(raw)
        if m:
            word, quoted = m.group(1), m.group(2)
            if word in SAY_KEYWORDS:
                continue
            text = _unquote(quoted)
            if pending_voice is not None:
                kind = "voiced"
            else:
                kind = "novoice"
            entries.append({"line": i, "kind": kind, "speaker": word,
                            "text": text, "voice": pending_voice,
                            "scene": cur_scene})
            pending_voice = None
            continue
        m = SC_ITEM_RE.match(raw)
        if m:
            text = _unquote(m.group(1))
            scene = menu_scene if menu_scene is not None else (
                choice_scene if choice_scene is not None else cur_scene)
            entries.append({"line": i, "kind": "choice", "speaker": None,
                            "text": text, "voice": None, "scene": scene})
            continue
        m = SC_DICT_RE.search(raw)
        if m and '"text":' in raw:
            # пункты portrait_choice / choices.append({...})
            entries.append({"line": i, "kind": "choice", "speaker": None,
                            "text": _unquote(m.group(1)), "voice": None,
                            "scene": cur_scene})
            continue
    return entries, scenes


# ---------------------------------------------------------------- сопоставление
def align(entries, scenes, by_id, by_scene, voices):
    """Помечает у каждого entry 'canon'; возвращает flags (кандидаты).

    Порядок: (1) voiced по id; (2) novoice по порядку среди null-voice dlg
    сцен охвата; (3) choice/date по порядку среди choice/date сцен охвата.
    """
    flags = []           # (code, entry_or_None, detail)
    used = set()
    canon_order = []
    for sc in sorted(scenes):
        for idx, it in enumerate(by_scene.get(sc, [])):
            canon_order.append((sc, idx, it))

    # (1) voiced по voice-id
    for e in entries:
        if e["kind"] != "voiced":
            continue
        vid = voices.get(e["voice"])
        if vid is None:
            flags.append(("NO_MANIFEST", e, str(e["voice"])))
            continue
        if vid not in by_id:
            flags.append(("NO_CANON", e, "id %d not in events" % vid))
            continue
        sc, spk, text = by_id[vid]
        e["canon"] = text
        e["canon_scene"] = sc
        used.add(("dlg", vid))

    # (2) novoice — по порядку среди null-voice dlg сцен охвата
    pools = {}
    for sc, idx, it in canon_order:
        if it["kind"] == "dlg" and it["id"] is None:
            pools.setdefault(sc, []).append((idx, it))
    cursors = {}
    for e in entries:
        if e["kind"] != "novoice":
            continue
        sc = e["scene"]
        pool = pools.get(sc, [])
        c = cursors.get(sc, 0)
        while c < len(pool) and ("dlgN", sc, pool[c][0]) in used:
            c += 1
        if c < len(pool):
            idx, it = pool[c]
            cursors[sc] = c + 1
            used.add(("dlgN", sc, idx))
            e["canon"] = it["text"]
            e["canon_scene"] = sc
        else:
            flags.append(("NO_CANON", e, "scene %s: novoice pool empty" % sc))

    # (3) choice/date по порядку в сцене
    for kind in ("choice", "date"):
        # пункт карты даты (portrait_choice) сопоставляется и с dateItem
        pool_kinds = ("choice", "date") if kind == "choice" else ("date",)
        cursors = {}
        for e in entries:
            if e["kind"] != kind:
                continue
            sc = e["scene"]
            pool = [(idx, it) for sc2, idx, it in canon_order
                    if sc2 == sc and it["kind"] in pool_kinds]
            c = cursors.get(sc, 0)
            while c < len(pool) and (kind, sc, pool[c][0]) in used:
                c += 1
            if c < len(pool):
                idx, it = pool[c]
                cursors[sc] = c + 1
                used.add((kind, sc, idx))
                e["canon"] = it["text"]
                e["canon_scene"] = sc
            else:
                flags.append(("NO_CANON", e,
                              "scene %s: %s pool empty" % (sc, kind)))

    # канон охвата без строки скрипта
    for sc, idx, it in canon_order:
        key = (("dlg", it["id"]) if (it["kind"] == "dlg" and it["id"] is not None)
               else ("dlgN", sc, idx) if it["kind"] == "dlg"
               else (it["kind"], sc, idx))
        # dateItem мог быть поглощён пунктом portrait_choice (kind=choice)
        if key not in used and ("choice", sc, idx) not in used:
            flags.append(("UNPORTED", None,
                          "scene %d [%s] %s" % (sc, it["kind"], it["text"][:70])))
    return flags


# ---------------------------------------------------------------- сборка
def build_part(part, maps, by_id, by_scene, voices):
    path = CH_DIR / ("script-ch3_%d.rpy" % part)
    entries, scenes = parse_script(path)
    flags = align(entries, scenes, by_id, by_scene, voices)

    en_index = {}
    for e in entries:
        old = e["text"]
        for lang in ("ja", "ru"):
            if old not in maps[lang]:
                flags.append(("NO_%s" % lang.upper(), e, ""))
        if old in maps["ru"] and maps["ru"][old] == old:
            flags.append(("RU_EQ_EN", e, old[:60]))
        if "canon" in e and e["kind"] != "overlay":
            ja_tl = maps["ja"].get(old)
            if ja_tl is not None and ja_tl != e["canon"]:
                flags.append(("MISMATCH_JA", e, "tl!=canon"))
        en_index.setdefault(old, []).append(e)

    for old, lst in en_index.items():
        canons = {e.get("canon") for e in lst if "canon" in e}
        if len(lst) > 1 and len(canons) > 1:
            flags.append(("DUP_EN", lst[0],
                          "x%d en, %d distinct canon" % (len(lst), len(canons))))
    return path, entries, scenes, flags


def render(part, path, entries, scenes, flags, maps):
    L = []
    L.append("# ch3 align — part %d (`%s`)" % (part, path.name))
    L.append("")
    L.append("Generated: %s. Canon: ps2_source/events_full chapter_04 "
             "(точные аргументы; '\\n' канона склеен)." %
             datetime.datetime.now().isoformat(timespec="seconds"))
    L.append("Scenes: %s." % ", ".join(str(s) for s in sorted(scenes)))
    counts = {}
    for e in entries:
        counts[e["kind"]] = counts.get(e["kind"], 0) + 1
    L.append("Entries: %d (%s)." % (
        len(entries), ", ".join("%s=%d" % kv for kv in sorted(counts.items()))))
    by_code = {}
    for code, e, det in flags:
        by_code.setdefault(code, []).append((e, det))
    L.append("Flags: %s." % (", ".join("%s=%d" % (c, len(v))
                                       for c, v in sorted(by_code.items())) or "none"))
    L.append("")
    if by_code:
        L.append("## FLAGS (кандидаты; classification — Analyzer)")
        L.append("")
        for code in sorted(by_code):
            for e, det in by_code[code]:
                loc = ("script line %d" % e["line"]) if e else "-"
                L.append("- [%s] %s: %s" % (code, loc, det))
        L.append("")
    L.append("## ENTRIES")
    L.append("")
    n = 0
    for e in entries:
        n += 1
        head = "#%d line %d scene %s kind=%s" % (
            n, e["line"], e["scene"], e["kind"])
        if e["voice"]:
            head += " voice=%s" % e["voice"]
        if e["speaker"]:
            head += " spk=%s" % e["speaker"]
        L.append("### " + head)
        L.append("- EN: %s" % e["text"])
        if "canon" in e and e["kind"] != "overlay":
            ja_tl = maps["ja"].get(e["text"])
            if ja_tl is None:
                state = "NO OLD IN TL/JA"
            elif ja_tl == e["canon"]:
                state = "OK"
            else:
                state = "DIFF tl=%s" % ja_tl
            L.append("- JA: %s" % e["canon"])
            L.append("- JAtl: %s" % state)
        elif "canon" in e:
            L.append("- JA: %s" % e["canon"])
            L.append("- JAtl: (overlay, skipped)")
        else:
            L.append("- JA: <no canon>")
        L.append("- RU: %s" % maps["ru"].get(e["text"], "<NO RU>"))
        L.append("")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------- main
def main():
    ensure_safe_output()
    ap = argparse.ArgumentParser(description="ch3 EN/JA/RU align evidence")
    ap.add_argument("--part", type=int, choices=PARTS)
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    parts = PARTS if args.all else ([args.part] if args.part else [])
    if not parts:
        safe_print("ERROR: specify --part N or --all")
        return 2

    maps, spots, dups = load_tl()
    voices = load_voices()
    by_id, by_scene = load_canon()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    total_flags = 0
    for part in parts:
        path, entries, scenes, flags = build_part(
            part, maps, by_id, by_scene, voices)
        text = render(part, path, entries, scenes, flags, maps)
        out = OUT_DIR / ("align_p%d.md" % part)
        io.open(out, "w", encoding="utf-8").write(text)
        codes = {}
        for code, e, det in flags:
            codes[code] = codes.get(code, 0) + 1
        total_flags += len(flags)
        safe_print("part %d: entries=%d flags=%d -> %s" % (
            part, len(entries), len(flags), out.name))
        if codes:
            safe_print("   " + " ".join("%s=%d" % kv for kv in sorted(codes.items())))
    if dups:
        safe_print("tl duplicates (all ch): %d" % len(dups))
    safe_print("TOTAL flags: %d" % total_flags)
    safe_print("RESULT: DONE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
