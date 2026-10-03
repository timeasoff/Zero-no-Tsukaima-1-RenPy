#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZnT1 remaster - project checks (skill: project-checks).

Run:  python tools/check_project.py [--chapter N] [--no-report]

Checks
  E1  duplicate label names across game/**/*.rpy
  E2  duplicate `from _call_overlay_screen_K` suffixes
  E3  `voice "..."` referencing a missing .ogg (skipped if audio not installed)
  E4  translatable string in game/chapters/ without an entry in tl/japanese
  E5  translatable string in game/chapters/ without an entry in tl/russian
  E6  empty `new ""` in tl
  E7  `jump` / `call` to a label that does not exist
  E8  tl file declares a different language than its folder
  E11 duplicate `old` inside one tl language (Ren'Py 8.5 StringTranslator.add
      raises "A translation for ... already exists at file:line" on startup;
      identical base strings are disambiguated in the script with an inline
      {#tag} comment instead of being translated twice)
  W1  `old` keys in tl with no matching script string (stale / mismatched `old`)
  W2  .ogg files referenced by nobody
  W3  unbalanced quote on a script line (possible multi-line dialogue)
  W4  unknown speaker identifier in game/chapters/ (character has no `define`)
  W5  translatable string OUTSIDE game/chapters/ without tl entry (UI/screens)
  I1  chapter string counts vs talk counts in ps2_source/chapter_stats.json

   E9  invalid / duplicate rows in references/image_id_map.csv
   E10 placeholder id(K) in a script that is not in image_id_map.csv
   W6  placeholder id(K) whose id IS mapped (replacement is pending)

Exceptions (read-only, never reported, never edited):
   game/tl/<lang>/common.rpy  -- taken from the Ren'Py documentation; its keys
   still count for E4/E5 coverage, but stale keys / empty new / wrong-language
   declarations inside these files are ignored.

Scope: strict (ERROR) only for game/chapters/; the rest of the game is W5,
game/remark/ is excluded (it carries its own per-language files).

Console output is ASCII-only (PowerShell here is cp1251); details go to
reports/check_project.md as UTF-8.
"""

import argparse
import csv
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME = os.path.join(ROOT, "game")
TL_DIR = os.path.join(GAME, "tl")
CHAPTERS = os.path.join(GAME, "chapters")
VOICES_DIR = os.path.join(GAME, "audio", "voices")
CHAPTER_STATS = os.path.join(ROOT, "ps2_source", "chapter_stats.json")
IMAGE_MAP = os.path.join(ROOT, "references", "image_id_map.csv")
REPORT = os.path.join(ROOT, "reports", "check_project.md")

# Заглушка фонового/CG id в скриптах: id(1145) — пока filename в
# references/image_id_map.csv не заполнен (см. tools/replace_bg_placeholders.py)
PH_RE = re.compile(r"\bid\((\d+)\)")

STR = r'"(?:[^"\\]|\\.)*"'
DIALOGUE_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s+(" + STR + r")\s*$")
BARE_RE = re.compile(r"^\s*(" + STR + r")\s*$")
MENU_RE = re.compile(r"^\s*(" + STR + r")\s*:\s*$")
TEXT_KEY_RE = re.compile(r'"text"\s*:\s*(' + STR + r")")
GETTEXT_RE = re.compile(r"_\(\s*(" + STR + r")\s*\)")
OVERLAY_RE = re.compile(r"call\s+overlay_screen\(\s*" + STR + r"\s*,\s*(" + STR + r")")
LABEL_RE = re.compile(r"^\s*label\s+([A-Za-z_][A-Za-z0-9_]+)\s*(?:\(|:)")
SPEAKER_DEF_RE = re.compile(r"^\s*define\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*Character\s*\(")
OVERLAY_K_RE = re.compile(r"_call_overlay_screen_(\d+)")
VOICE_RE = re.compile(r'^\s*voice\s+(' + STR + r")\s*$")
JUMP_RE = re.compile(r"^\s*jump\s+([A-Za-z_][A-Za-z0-9_]*)\s*$")
CALL_RE = re.compile(r"^\s*call\s+([A-Za-z_][A-Za-z0-9_]*)\s*(?:\(|$)")
TL_LANG_RE = re.compile(r"^\s*translate\s+([a-z_]+)\s+strings\s*:")
TL_OLD_RE = re.compile(r"^\s*old\s+(" + STR + r")\s*$")
TL_NEW_RE = re.compile(r"^\s*new\s+(" + STR + r")\s*$")

EXCLUDE_PARTS = ("/remark/", "/saves/", "/cache/")

# tl/common.rpy взят из документации Ren'Py: файл read-only (атрибут +R),
# не редактируется и не проверяется; его ключи участвуют в покрытии E4/E5.
TL_READONLY_SUFFIXES = ("/tl/japanese/common.rpy", "/tl/russian/common.rpy")


def is_tl_readonly(relpath):
    return any(relpath.endswith(sfx) for sfx in TL_READONLY_SUFFIXES)


def read_lines(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return fh.read().splitlines()
    except OSError as exc:
        return ["# unreadable: %s" % exc]


def walk_rpy(base):
    out = []
    for dirpath, _dirs, filenames in os.walk(base):
        for name in sorted(filenames):
            if name.endswith(".rpy"):
                out.append(os.path.join(dirpath, name))
    return sorted(out)


def rel(path):
    return os.path.relpath(path, ROOT).replace("\\", "/")


def excluded(path):
    r = "/" + rel(path)
    return any(part in r for part in EXCLUDE_PARTS)


def unescape(raw):
    body = raw[1:-1]
    return body.replace('\\"', '"').replace("\\\\", "\\")


def collect_strings(path, speakers):
    """-> (candidates[(text, kind, lineno)], unknown_speakers[(name, lineno)], unbalanced)"""
    found, unknown, bad = [], [], []
    for i, line in enumerate(read_lines(path), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        m = TEXT_KEY_RE.search(line)
        if m:
            found.append((unescape(m.group(1)), "choice", i))
            continue
        m = OVERLAY_RE.search(line)
        if m:
            found.append((unescape(m.group(1)), "overlay", i))
            continue
        m = GETTEXT_RE.search(line)
        if m:
            found.append((unescape(m.group(1)), "gettext", i))
            continue
        m = DIALOGUE_RE.match(line)
        if m:
            name, raw = m.group(1), m.group(2)
            if name in speakers:
                if raw.count('"') % 2:
                    bad.append(i)
                else:
                    found.append((unescape(raw), "dialogue", i))
            elif line.lstrip().startswith(name) and line[:1] not in (" ", "\t"):
                unknown.append((name, i))  # top-level `ident "..."` = likely speaker
            continue
        m = MENU_RE.match(line)
        if m:
            raw = m.group(1)
            if raw.count('"') % 2:
                bad.append(i)
            else:
                found.append((unescape(raw), "menu", i))
            continue
        m = BARE_RE.match(line)
        if m:
            raw = m.group(1)
            if raw.count('"') % 2:
                bad.append(i)
            else:
                found.append((unescape(raw), "narration", i))
    return found, unknown, bad


def parse_tl(folder):
    """-> (keys[text]->list(new,file,line), wrong_lang, empty_new)"""
    keys, wrong_lang, empty_new = {}, [], []
    lang = os.path.basename(folder)
    for path in walk_rpy(folder):
        cur_key = None
        cur_line = 0
        for i, line in enumerate(read_lines(path), 1):
            m = TL_LANG_RE.match(line)
            if m and m.group(1) != lang:
                wrong_lang.append((rel(path), i, m.group(1)))
            m = TL_OLD_RE.match(line)
            if m:
                cur_key = unescape(m.group(1))
                cur_line = i
                keys.setdefault(cur_key, []).append(("", rel(path), i))
                continue
            m = TL_NEW_RE.match(line)
            if m and cur_key is not None:
                keys[cur_key][-1] = (unescape(m.group(1)), rel(path), cur_line)
                if unescape(m.group(1)).strip() == "":
                    empty_new.append((rel(path), cur_line))
    return keys, wrong_lang, empty_new


def chapter_map_talks():
    """project chapter N -> talk count of source chapter N+1 (chapter_stats.json)."""
    talks = {}
    if not os.path.isfile(CHAPTER_STATS):
        return talks
    try:
        with open(CHAPTER_STATS, encoding="utf-8") as fh:
            stats = json.load(fh)
    except Exception:
        return talks
    for key, val in stats.items():
        if key.isdigit() and isinstance(val, dict) and "talk" in val:
            talks[int(key)] = int(val["talk"])
    return talks


def load_image_map():
    """references/image_id_map.csv -> (ids:set, named:set, problems:list[str])."""
    ids, named, problems = set(), set(), []
    if not os.path.isfile(IMAGE_MAP):
        return ids, named, problems
    seen = {}
    with open(IMAGE_MAP, encoding="utf-8", errors="replace") as fh:
        for i, line in enumerate(fh, 1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if i and line.startswith("image_id,"):
                continue
            parts = next(csv.reader([line]))
            if not parts or parts[0].strip() == "image_id":
                continue
            if len(parts) < 3:
                problems.append("image_id_map.csv line %d: %d columns" % (i, len(parts)))
                continue
            raw = parts[0].strip()
            if not raw.isdigit():
                problems.append("image_id_map.csv line %d: bad image_id %r" % (i, raw[:20]))
                continue
            num = int(raw)
            if num in seen:
                problems.append("image_id_map.csv line %d: duplicate image_id %d "
                                "(first at line %d)" % (i, num, seen[num]))
            seen.setdefault(num, i)
            ids.add(num)
            if parts[2].strip():
                named.add(num)
    return ids, named, problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", type=int, default=None)
    ap.add_argument("--no-report", action="store_true")
    args = ap.parse_args()

    errors, warnings, info = [], [], []

    rpy_all = [p for p in walk_rpy(GAME) if not excluded(p)]
    rpy_scripts = [p for p in rpy_all if os.sep + "tl" + os.sep not in p]

    speakers = set()
    for path in rpy_all:
        for line in read_lines(path):
            m = SPEAKER_DEF_RE.match(line)
            if m:
                speakers.add(m.group(1))
    info.append("speakers defined: %d" % len(speakers))

    # E1 labels
    labels = {}
    for path in rpy_all:
        for i, line in enumerate(read_lines(path), 1):
            m = LABEL_RE.match(line)
            if m:
                labels.setdefault(m.group(1), []).append((rel(path), i))
    for name, hits in sorted(labels.items()):
        if len(hits) > 1:
            errors.append("E1 duplicate label '%s': %s"
                          % (name, ", ".join("%s:%d" % h for h in hits)))

    # E2 overlay K
    ks = []
    for path in rpy_scripts:
        for i, line in enumerate(read_lines(path), 1):
            for m in OVERLAY_K_RE.finditer(line):
                ks.append((int(m.group(1)), rel(path), i))
    seen_k = {}
    for k, f, i in ks:
        seen_k.setdefault(k, []).append((f, i))
    for k, hits in sorted(seen_k.items()):
        if len(hits) > 1:
            errors.append("E2 overlay K=%d used %d times: %s"
                          % (k, len(hits), ", ".join("%s:%d" % h for h in hits)))
    max_k = max(seen_k) if seen_k else 0
    info.append("overlay K: max=%d used=%d next_free=%d" % (max_k, len(ks), max_k + 1))

    # E7 jump/call targets
    known = set(labels)
    for path in rpy_scripts:
        for i, line in enumerate(read_lines(path), 1):
            m = JUMP_RE.match(line)
            if m and m.group(1) not in known:
                errors.append("E7 jump '%s' at %s:%d has no label"
                              % (m.group(1), rel(path), i))
                continue
            m = CALL_RE.match(line)
            if m and m.group(1) != "screen" and m.group(1) not in known:
                errors.append("E7 call '%s' at %s:%d has no label"
                              % (m.group(1), rel(path), i))

    # candidates
    candidates, per_file = [], {}
    for path in rpy_scripts:
        in_chapters = rel(path).startswith("game/chapters/")
        found, unknown, bad = collect_strings(path, speakers)
        per_file[rel(path)] = len(found)
        for text, kind, i in found:
            candidates.append((text, kind, rel(path), i, in_chapters))
        for i in bad:
            warnings.append("W3 unbalanced quote at %s:%d" % (rel(path), i))
        if in_chapters:
            for name, i in sorted(set(unknown)):
                warnings.append("W4 unknown speaker '%s' at %s:%d (no define)"
                                % (name, rel(path), i))

    cand_strict = set(t for t, _k, _f, _i, strict in candidates if strict)
    cand_all = set(t for t, _k, _f, _i, _s in candidates)
    strict_at = {}
    for text, kind, f, i, strict in candidates:
        if strict:
            strict_at.setdefault(text, (kind, f, i))

    # E4/E5/E6/E8/W1/W5
    tl_keys = {}
    for lang in ("japanese", "russian"):
        folder = os.path.join(TL_DIR, lang)
        if not os.path.isdir(folder):
            errors.append("E4/E5 tl folder missing: %s" % rel(folder))
            continue
        keys, wrong_lang, empty_new = parse_tl(folder)
        tl_keys[lang] = keys
        code = 4 if lang == "japanese" else 5
        for f, i, got in wrong_lang:
            if is_tl_readonly(f):
                continue
            errors.append("E8 tl/%s declares 'translate %s' at %s:%d"
                          % (lang, got, f, i))
        for f, i in empty_new:
            if is_tl_readonly(f):
                continue
            errors.append("E6 empty new at %s:%d" % (f, i))
        for k in sorted(keys):
            hits = keys[k]
            if len(hits) > 1:
                errors.append("E11 duplicate old in tl/%s: %s (%d times) at %s"
                              % (lang, k[:70], len(hits),
                                 ", ".join("%s:%d" % (h[1], h[2]) for h in hits)))
        missing_strict = cand_strict - set(keys)
        missing_soft = cand_all - cand_strict - set(keys)
        for k in sorted(missing_strict):
            kind, f, i = strict_at[k]
            errors.append("E%d missing in tl/%s: %s (%s) at %s:%d"
                          % (code, lang, kind, k[:70], f, i))
        if missing_soft:
            warnings.append("W5 %d string(s) outside game/chapters/ missing in "
                            "tl/%s (UI/screens)" % (len(missing_soft), lang))
        for k in sorted(set(keys) - cand_all):
            f, i = keys[k][0][1], keys[k][0][2]
            if is_tl_readonly(f):
                continue
            warnings.append("W1 stale old in tl/%s at %s:%d: %s" % (lang, f, i, k[:70]))

    # E3 voices / W2
    voice_refs = []
    for path in rpy_scripts:
        for i, line in enumerate(read_lines(path), 1):
            m = VOICE_RE.match(line)
            if m:
                voice_refs.append((unescape(m.group(1)), rel(path), i))
    if os.path.isdir(VOICES_DIR) and os.listdir(VOICES_DIR):
        have = {os.path.splitext(n)[0] for n in os.listdir(VOICES_DIR)
                if n.lower().endswith(".ogg")}
        for name, f, i in voice_refs:
            if name not in have:
                errors.append("E3 voice without ogg: %s at %s:%d" % (name, f, i))
        used = {n for n, _f, _i in voice_refs}
        warnings.append("W2 %d ogg not referenced by any script" % len(have - used))
        info.append("voices: refs=%d ogg=%d missing=%d"
                    % (len(voice_refs), len(have), len(have & used) - len(have & used)
                       + len([1 for n, _f, _i in voice_refs if n not in have])))
    else:
        info.append("voices: refs=%d ogg check SKIPPED (audio not installed)"
                    % len(voice_refs))

    # I1 chapter counts
    talks = chapter_map_talks()
    for name in sorted(os.listdir(CHAPTERS), key=lambda s: (len(s), s)):
        full = os.path.join(CHAPTERS, name)
        if not os.path.isdir(full) or not name.isdigit():
            continue
        n = int(name)
        if args.chapter is not None and n != args.chapter:
            continue
        dlg = sum(per_file.get(rel(p), 0) for p in walk_rpy(full))
        src = talks.get(n + 1)
        if src is None or dlg == 0:
            if src is not None:
                info.append("I1 ch%d: not started (source talk=%d)" % (n, src))
            continue
        if dlg > src:
            warnings.append("I1 ch%d: %d script strings > %d source talk" % (n, dlg, src))
        else:
            info.append("I1 ch%d: strings=%d source_talk=%d%s"
                        % (n, dlg, src, "" if dlg == src else " (gap expected)"))

    # E9/E10/W6/I2 - image id map (references/image_id_map.csv) + placeholders
    map_ids, map_named, map_problems = load_image_map()
    for msg in map_problems:
        errors.append("E9 %s" % msg)
    ph_hits = []
    for path in rpy_all:
        for i, line in enumerate(read_lines(path), 1):
            nums = [int(m) for m in PH_RE.findall(line)]
            if nums:
                ph_hits.append((rel(path), i, nums))
    ph_total = sum(len(_n) for _f, _i, _n in ph_hits)
    if not os.path.isfile(IMAGE_MAP) and ph_total:
        errors.append("E9 references/image_id_map.csv missing but %d "
                      "placeholder(s) id(K) in use" % ph_total)
    for f, i, nums in ph_hits:
        for num in nums:
            if map_ids and num not in map_ids:
                errors.append("E10 placeholder id(%d) unknown to image_id_map.csv "
                              "at %s:%d" % (num, f, i))
            elif num in map_named:
                warnings.append("W6 placeholder id(%d) has a name in "
                                "image_id_map.csv at %s:%d (run "
                                "tools/replace_bg_placeholders.py --apply)"
                                % (num, f, i))
    info.append("image map: ids=%d named=%d open=%d | placeholders=%d in %d file(s)"
                % (len(map_ids), len(map_named), len(map_ids - map_named),
                   ph_total, len({f for f, _i, _n in ph_hits})))

    info.append("labels=%d rpy=%d strings(strict=%d) tl_old=%s"
                % (len(labels), len(rpy_scripts), len(cand_strict),
                   ",".join("%s:%d" % (k, len(tl_keys.get(k, [])))
                            for k in ("japanese", "russian"))))

    if not args.no_report:
        os.makedirs(os.path.dirname(REPORT), exist_ok=True)
        with open(REPORT, "w", encoding="utf-8") as fh:
            fh.write("# check_project — отчёт автопроверок\n\n")
            fh.write("Команда: `python tools/check_project.py` "
                     "(опция `--chapter N` ограничивает проверку одной главей).\n\n")
            fh.write("Строго (ERROR) проверяются строки в `game/chapters/`; "
                     "остальной игре — предупреждения; `game/remark/` исключён "
                     "(у него свои файлы на каждый язык).\n\n")
            for title, items in (("ERROR", errors), ("WARNING", warnings),
                                 ("INFO", info)):
                fh.write("## %s (%d)\n\n" % (title, len(items)))
                if items:
                    for it in items:
                        fh.write("- %s\n" % it)
                else:
                    fh.write("- нет\n")
                fh.write("\n")

    print("labels=%d overlayK=%d strings=%d voices=%d"
          % (len(labels), len(ks), len(candidates), len(voice_refs)))
    print("errors=%d warnings=%d info=%d" % (len(errors), len(warnings), len(info)))
    if not args.no_report:
        print("report: %s" % rel(REPORT))
    print("RESULT: %s" % ("ERRORS" if errors else "OK"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
