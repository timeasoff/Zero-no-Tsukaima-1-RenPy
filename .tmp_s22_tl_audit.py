#!/usr/bin/env python3
# S22 focused TL integrity audit for script-ch4_2.rpy (read-only, UTF-8 output).
import os, re, json

ROOT = "/workspace/.tmp/opencode/review-ch2-5"
SCRIPT = os.path.join(ROOT, "game/chapters/4/script-ch4_2.rpy")
OUT = os.path.join(ROOT, ".tmp_s22_tl_report.txt")

DIALOG_IDENTS = {"s","l","si","ha","d","c","o","t","k","g","m","th","unk","unk_ha","unk_k",
                 "soldier","commander","mage","unds"}

def unescape(s):
    # Ren'Py string literal: handle \" and \\ only (sufficient for comparison keys)
    return s.replace('\\"', '"').replace('\\\\', '\\')

def extract_script_strings():
    res = []  # (line, text, kind)
    with open(SCRIPT, encoding="utf-8") as f:
        for ln, raw in enumerate(f, 1):
            line = raw.rstrip("\n")
            st = line.strip()
            # skip comments
            if st.startswith("#"):
                continue
            # dialogue: ident "..."
            m = re.match(r'^([a-zA-Z_][a-zA-Z0-9_]*)\s+"(.*)"\s*$', st)
            if m and m.group(1) in DIALOG_IDENTS:
                res.append((ln, unescape(m.group(2)), "dialog"))
                continue
            # menu item: "text":
            m = re.match(r'^"(.*)":\s*$', st)
            if m:
                res.append((ln, unescape(m.group(1)), "menu"))
                continue
            # choice dict: "text": "..."
            m = re.match(r'^.*"text"\s*:\s*"(.*)"\s*[,}]?\s*$', st)
            if m:
                res.append((ln, unescape(m.group(1)), "choice"))
                continue
            # overlay title in call overlay_screen(..., "text", ...)
            if "overlay_screen(" in st:
                for mm in re.finditer(r'"(.*?)"', st):
                    res.append((ln, unescape(mm.group(1)), "overlay"))
    return res

def collect_old(lang):
    d = os.path.join(ROOT, "game/tl", lang)
    olds = {}  # old -> list of (file, line, new)
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".rpy"):
            continue
        path = os.path.join(d, fn)
        if fn == "common.rpy":
            continue
        cur_old = None
        with open(path, encoding="utf-8") as f:
            for ln, raw in enumerate(f, 1):
                st = raw.strip()
                m = re.match(r'^old\s+"(.*)"\s*$', st)
                if m:
                    cur_old = unescape(m.group(1))
                    olds.setdefault(cur_old, []).append((fn, ln, None))
                    continue
                m = re.match(r'^new\s+"(.*)"\s*$', st)
                if m and cur_old is not None:
                    fnl = olds[cur_old][-1]
                    olds[cur_old][-1] = (fnl[0], fnl[1], unescape(m.group(1)))
                    cur_old = None
    return olds

def main():
    strs = extract_script_strings()
    ja = collect_old("japanese")
    ru = collect_old("russian")
    lines = []
    lines.append("SCRIPT STRINGS: %d" % len(strs))
    missing_ja = [(ln, kind, t) for (ln, t, kind) in strs if t not in ja]
    missing_ru = [(ln, kind, t) for (ln, t, kind) in strs if t not in ru]
    lines.append("MISSING IN JA: %d" % len(missing_ja))
    for ln, kind, t in missing_ja:
        lines.append("  JA_MISS line=%d kind=%s text=%r" % (ln, kind, t[:90]))
    lines.append("MISSING IN RU: %d" % len(missing_ru))
    for ln, kind, t in missing_ru:
        lines.append("  RU_MISS line=%d kind=%s text=%r" % (ln, kind, t[:90]))
    # duplicates of old within a language for this part's strings
    dupja = [(t, ja[t]) for (ln, t, kind) in strs if len(ja.get(t, [])) > 1]
    dupru = [(t, ru[t]) for (ln, t, kind) in strs if len(ru.get(t, [])) > 1]
    lines.append("DUP OLD (JA among part strings): %d" % len(dupja))
    for t, occ in dupja:
        lines.append("  JA_DUP text=%r occ=%s" % (t[:80], occ))
    lines.append("DUP OLD (RU among part strings): %d" % len(dupru))
    for t, occ in dupru:
        lines.append("  RU_DUP text=%r occ=%s" % (t[:80], occ))
    # empty new for matched
    empty = []
    for (ln, t, kind) in strs:
        for lang, dd in (("ja", ja), ("ru", ru)):
            for fn, ol, nw in dd.get(t, []):
                if nw == "":
                    empty.append((lang, fn, ol, ln))
    lines.append("EMPTY NEW (matched): %d" % len(empty))
    for e in empty:
        lines.append("  EMPTY %s file=%s oldline=%d scriptline=%d" % e)
    # JA new vs RU new identical (suspicious: RU showing JA / EN)
    same = []
    for (ln, t, kind) in strs:
        jlist = ja.get(t, [])
        rlist = ru.get(t, [])
        if jlist and rlist and jlist[0][2] and jlist[0][2] == rlist[0][2]:
            same.append((ln, t))
    lines.append("JA_NEW == RU_NEW (suspicious): %d" % len(same))
    for ln, t in same:
        lines.append("  SAME line=%d text=%r" % (ln, t[:80]))
    # report translator-comment ids present
    tc = [t for (ln, t, kind) in strs if "{#" in t]
    lines.append("WITH TRANSLATOR COMMENT {#...}: %d" % len(tc))
    # show all strings compact for manual review
    lines.append("=== ALL STRINGS (line|kind|text) ===")
    for ln, t, kind in strs:
        lines.append("%d|%s|%s" % (ln, kind, t))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    # ASCII summary to console
    print("STRINGS=%d JA_MISS=%d RU_MISS=%d JA_DUP=%d RU_DUP=%d EMPTY=%d SAME_JA_RU=%d TC=%d" % (
        len(strs), len(missing_ja), len(missing_ru), len(dupja), len(dupru), len(empty), len(same), len(tc)))
    print("REPORT=" + OUT)

if __name__ == "__main__":
    main()
