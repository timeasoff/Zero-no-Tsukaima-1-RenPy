#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S1 / T20261031-154035-97bf: аудит покрытия tndl по реализованным частям (v2).

Источник канона: ps2_source/events_full/chapter_NN_*.txt (строки TNDL).
Порт: game/chapters/{0..6}/script-*.rpy.

Якорь события (v2):
  * null_start   -> label chN первого файла главы;
  * like-смежное -> голос триггер-реплики -> voice-строка -> ближайший после
    неё update_sympathy(значениеLike) (окно до следующей voice, <=40 строк);
    если голос не резолвится -> кандидаты update_sympathy(значение, персонаж),
    сужение по сцене (# ==== SCENE N ====) -> по соседству stale-комментария;
  * standalone   -> голос -> строка диалога после voice (предпочтительно),
    иначе первое утверждение в окне.

Строки 1-based по всему файлу; окно поиска — индексы строк после voice.

ch1 — контроль (уже портирована в 7a8585c): без вставок, проверка
распределения + дистанции вызова от якоря для резолвляемых событий.
ch6 — чужой WIP: только инвентарь.

Выход: s1_tndl_audit.md + s1_insert_plan.csv.
"""
import csv
import re
from pathlib import Path

TASK_DIR = Path(__file__).resolve().parent
ROOT = TASK_DIR.parents[2]

SRC2DIR = {1: "0", 2: "1", 3: "2", 4: "3", 5: "4", 6: "5", 7: "6"}

JA2KEY = {
    "ルイズ": "louise",
    "シエスタ": "siesta",
    "タバサ": "tabitha",
    "キュルケ": "kirche",
    "ハルナ": "haruna",
    "アンリエッタ": "anrietta",
}

STALE_RE = re.compile(r"не переносится|не портируется|система не реализована")
TNDL_IN_LINE_RE = re.compile(r"tndl\(([+-]?\d+|null)\)")
VOICE_RE = re.compile(r'^\s*voice "([^"]+)"')
SYN_RE = re.compile(r'^\s*\$ ?update_sympathy\((-?\d+)(?:,\s*char_key="(\w+)")?\)')
CALL_RE = re.compile(r'^\s*\$ ?tndl\((None|-?\d+)\)')
DIALOGUE_RE = re.compile(r'^\s*[A-Za-z_][\w.]* "')
SCENE_RE = re.compile(r"^\s*# ==== SCENE (\d+)")


def part_key(path):
    name = path if isinstance(path, str) else path.name
    m = re.match(r"script-ch(\d+)_(\d+)([a-z]*)", name)
    if m:
        return (int(m.group(1)), int(m.group(2)), m.group(3))
    m = re.match(r"script-ch(\d+)", name)
    return (int(m.group(1)) if m else 0, 0, "")


def parse_source(path):
    events = []
    scene = None
    last_talk = None   # (char, voice_id|None, line) — ближайшая talk
    last_voiced = None  # (char, voice_id, line) — ближайшая talk с голосом
    gap = 0             # безголосых talk после last_voiced
    last_like = None    # (char, value, line)
    for i, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        m = re.match(r"^## SCENE (\d+)", raw)
        if m:
            scene = int(m.group(1))
            continue
        m = re.match(r'^DIALOGUE\s+talk\("([^"]+)"', raw)
        if m:
            mv = re.search(r"\(0x04000000 \+(\d+)\)\s*\)\s*$", raw)
            vid = int(mv.group(1)) if mv else None
            last_talk = (m.group(1), vid, i)
            if vid is not None:
                last_voiced = (m.group(1), vid, i)
                gap = 0
            else:
                gap += 1
            continue
        m = re.match(r'^LIKE\s+like\("([^"]+)",\s*(-?\d+)\)', raw)
        if m:
            last_like = (m.group(1), int(m.group(2)), i)
            continue
        m = re.match(r"^TNDL\s+tndl\(([+-]?\d+|null)\)\s*$", raw)
        if m:
            tok = m.group(1)
            value = None if tok == "null" else int(tok)
            like_adj = last_like is not None and last_like[2] == i - 1
            if value is None:
                kind = "null_start"
            elif like_adj:
                kind = "like"
            else:
                kind = "standalone"
            events.append({
                "src_line": i,
                "scene": scene,
                "value": value,
                "like": (last_like[0], last_like[1], last_like[2]) if like_adj else None,
                "talk": last_talk,
                "voiced": last_voiced,
                "gap": gap,
                "kind": kind,
            })
    return events


def load_voice_map(path):
    id2names = {}
    with path.open(encoding="utf-8") as fh:
        for row in csv.reader(fh):
            if not row or row[0].startswith("#") or row[0] == "voice_name":
                continue
            if len(row) > 1 and row[1].isdigit():
                id2names.setdefault(int(row[1]), []).append(row[0])
    return id2names


def scan_port(chapter_dir, ch_num):
    port = {"files": {}, "voices": {}, "syns": [], "stale": [], "calls": [],
            "labels": {}, "scenes": {}, "syn_by_key": {}, "scene_marks": {}}
    for f in sorted(chapter_dir.glob("*.rpy"), key=part_key):
        lines = f.read_text(encoding="utf-8").splitlines()
        port["files"][f.name] = lines
        for n, ln in enumerate(lines, 1):
            m = VOICE_RE.match(ln)
            if m:
                port["voices"].setdefault(m.group(1), (f.name, n))
            m = SYN_RE.match(ln)
            if m:
                entry = (f.name, n, int(m.group(1)), m.group(2))
                port["syns"].append(entry)
                port["syn_by_key"].setdefault((m.group(2), int(m.group(1))), []).append(entry)
            m = CALL_RE.match(ln)
            if m:
                port["calls"].append((f.name, n,
                                      None if m.group(1) == "None" else int(m.group(1))))
            m = re.match(r"^label (ch\d+):", ln)
            if m:
                port["labels"][m.group(1)] = (f.name, n)
            m = SCENE_RE.match(ln)
            if m:
                sc = int(m.group(1))
                port["scenes"].setdefault(sc, set()).add(f.name)
                port["scene_marks"].setdefault(f.name, []).append((n, sc))
            if "tndl(" in ln and ln.lstrip().startswith("#") and STALE_RE.search(ln):
                mv = TNDL_IN_LINE_RE.search(ln)
                claimed = None
                if mv:
                    claimed = None if mv.group(1) == "null" else int(mv.group(1))
                port["stale"].append((f.name, n, claimed, ln.strip()))
    port["ch_num"] = ch_num
    return port


def indent_of(line):
    return line[: len(line) - len(line.lstrip())]


def window_bounds(lines, start_1based, cap):
    """Индексы строк (0-based) после voice-строки: до следующей voice <= cap."""
    lo = start_1based          # 0-based индекс первой строки после voice
    hi = min(len(lines), lo + cap)
    for j in range(lo, hi):
        if VOICE_RE.match(lines[j]):
            hi = j
            break
    return lo, hi


def resolve_voice(talk, port, id2names):
    if not talk or talk[1] is None:
        return None, None, None
    for nm in id2names.get(talk[1], []):
        if nm in port["voices"]:
            f, l = port["voices"][nm]
            return f, l, nm
    return None, None, None


def segment_scene(port, fname, line):
    """Сцена сегмента файла, в который попадает строка line (последний
    маркер # ==== SCENE N ==== не далее line)."""
    cur = None
    for n, sc in port["scene_marks"].get(fname, []):
        if n <= line:
            cur = sc
        else:
            break
    return cur


def dialogue_anchor(lines, lo, hi, gap):
    """Строка (1-based) диалога-якоря (вставка ПОСЛЕ неё): пропускаем gap
    безголосых диалогов, якорь — следующий. Если диалогов нет вовсе — fb
    (первое утверждение) только при gap == 0."""
    seen = 0
    fb = None
    for j in range(lo, hi):
        ln = lines[j]
        if not ln.strip() or ln.lstrip().startswith("#"):
            continue
        if VOICE_RE.match(ln) or CALL_RE.match(ln):
            break
        if DIALOGUE_RE.match(ln):
            if seen == gap:
                return j + 1  # 1-based строка диалога
            seen += 1
            continue
        if fb is None:
            fb = (j + 1, indent_of(ln))
    if gap == 0 and fb:
        return fb[0]
    return None


def resolve(ev, port, id2names, stale_lines):
    files = port["files"]
    if ev["kind"] == "null_start":
        lab = port["labels"].get("ch%d" % port["ch_num"])
        if not lab:
            return None
        fl, ln = lab
        return dict(anchor_file=fl, anchor_line=ln, anchor_type="label",
                    indent="    ", voice_name=None)

    gap = ev.get("gap") or 0
    vf, vl, vname = resolve_voice(ev.get("voiced"), port, id2names)

    # --- like-смежное, голос резолвился: ближайший update_sympathy(значение)
    if ev["like"] and vf:
        lines = files[vf]
        val = ev["like"][1]
        lo, hi = window_bounds(lines, vl, 40)
        syn_at = None
        for j in range(lo, hi):
            m = SYN_RE.match(lines[j])
            if m and int(m.group(1)) == val:
                syn_at = j + 1
                break
        if syn_at:
            return dict(anchor_file=vf, anchor_line=syn_at, anchor_type="syn",
                        indent=indent_of(lines[syn_at - 1]), voice_name=vname)
        # синхронии в окне нет — якорь диалог (+8 строк на syn)
        d = dialogue_anchor(lines, lo, hi, gap)
        if d:
            for j in range(d, min(d + 8, hi)):
                m = SYN_RE.match(lines[j])
                if m and int(m.group(1)) == val:
                    return dict(anchor_file=vf, anchor_line=j + 1,
                                anchor_type="syn_after_dlg",
                                indent=indent_of(lines[j]), voice_name=vname)
            return dict(anchor_file=vf, anchor_line=d, anchor_type="dialogue",
                        indent=indent_of(lines[d - 1]), voice_name=vname)

    # --- standalone / голос есть: диалог после voice
    if vf:
        lines = files[vf]
        lo, hi = window_bounds(lines, vl, 40)
        d = dialogue_anchor(lines, lo, hi, gap)
        if d:
            return dict(anchor_file=vf, anchor_line=d, anchor_type="dialogue",
                        indent=indent_of(lines[d - 1]), voice_name=vname)

    # --- фолбэки без голоса ---
    if ev["like"]:
        char, val, _ = ev["like"]
        key = JA2KEY.get(char)
        cands = list(port["syn_by_key"].get((key, val), []))
        # 1) сужение по СЕГМЕНТУ сцены (маркер файла)
        seg = [c for c in cands
               if segment_scene(port, c[0], c[1]) == ev["scene"]]
        if seg:
            cands = seg
        else:
            # 2) сужение по файлам, содержащим сцену
            if ev["scene"] in port["scenes"]:
                sf = port["scenes"][ev["scene"]]
                narrowed = [c for c in cands if c[0] in sf]
                if narrowed:
                    cands = narrowed
        if len(cands) == 1:
            fl, ln, _, _ = cands[0]
            return dict(anchor_file=fl, anchor_line=ln, anchor_type="syn_fallback",
                        indent=None, voice_name=None)
        if len(cands) > 1:
            # 3) соседство со stale-комментарием
            for fl, ln, _, _ in cands:
                for sfl, sln, _, _ in stale_lines:
                    if sfl == fl and abs(sln - ln) <= 3:
                        return dict(anchor_file=fl, anchor_line=ln,
                                    anchor_type="syn_via_stale", indent=None,
                                    voice_name=None)
            return dict(anchor_file=None, anchor_line=None,
                        anchor_type="syn_cands", cands=cands)
        return dict(anchor_file=None, anchor_line=None, anchor_type="no_syn")

    # standalone без голоса — вручную
    return dict(anchor_file=None, anchor_line=None, anchor_type="no_voice")


def pair_stale(inserts, stale):
    used = set()
    # pass 1: <= 12 строк (предпочтение совпадению значения)
    for ins in inserts:
        best, best_key = None, None
        for idx, st in enumerate(stale):
            if idx in used or st[0] != ins["insert_file"]:
                continue
            dist = abs(st[1] - ins["insert_after"])
            if dist > 12:
                continue
            key = (0 if st[2] == ins["value"] else 1, dist)
            if best_key is None or key < best_key:
                best, best_key = idx, key
        if best is not None:
            used.add(best)
            ins["stale_file"], ins["stale_line"], ins["stale_claimed"], ins["stale_text"] = stale[best]
            ins["stale_match"] = (stale[best][2] == ins["value"])
    # pass 2: непарный комментарий -> ближайшая НЕзанятая вставка того же
    # значения в том же файле (<= 30 строк; «применён выше» и т.п.)
    for idx, st in enumerate(stale):
        if idx in used:
            continue
        best, bestd = None, None
        for ins in inserts:
            if ins.get("stale_file") or ins["insert_file"] != st[0]:
                continue
            if ins["value"] != st[2]:
                continue
            dist = abs(st[1] - ins["insert_after"])
            if dist > 30:
                continue
            if bestd is None or dist < bestd:
                best, bestd = ins, dist
        if best is not None:
            used.add(idx)
            best["stale_file"], best["stale_line"], best["stale_claimed"], best["stale_text"] = st
            best["stale_match"] = (st[2] == best["value"])
    return [st for idx, st in enumerate(stale) if idx not in used]


def fmt_val(v):
    return "null" if v is None else "%+d" % v


def main():
    id2names = load_voice_map(ROOT / "references" / "voice_id_map.csv")
    rows = []
    md = ["# S1 — аудит покрытия tndl (T20261031-154035-97bf)", "",
          "Канон: `ps2_source/events_full/chapter_NN_*.txt`, строки `TNDL`.",
          "Якорь: голос триггер-реплики → `voice_id_map` → строка `voice \"...\"`",
          "(+ `update_sympathy` для like-смежных, сужение по сцене,",
          "`label chN` для `tndl(null)`). ch1 — контроль, ch6 — чужой WIP.", "",
          "| источник | порт | TNDL в JA | в порте | stale | план | NO-ANCHOR | непарные | статус |",
          "|---|---|---|---|---|---|---|---|---|"]
    summary = []

    for nn, d in sorted(SRC2DIR.items()):
        src = next((ROOT / "ps2_source" / "events_full").glob("chapter_%02d_*.txt" % nn), None)
        events = parse_source(src)
        cdir = ROOT / "game" / "chapters" / d
        port = scan_port(cdir, int(d))
        control = (d == "1")
        foreign = (d == "6")

        md.append("")
        md.append("## chapter_%02d -> chapters/%s%s" % (
            nn, d, " — КОНТРОЛЬ (уже портирована)" if control else
            " — инвентарь, БЕЗ правок (чужой WIP)" if foreign else ""))
        md.append("")

        if foreign:
            md.append("| src_line | scene | value | триггер |")
            md.append("|---|---|---|---|")
            for e in events:
                t = e["talk"] or ("?", None, 0)
                md.append("| %d | %s | %s | %s (voice id %s) |" % (
                    e["src_line"], e["scene"], fmt_val(e["value"]), t[0], t[1]))
            summary.append((nn, d, len(events), len(port["calls"]), len(port["stale"]),
                            0, 0, 0, "FOREIGN-WIP"))
            continue

        src_vals = [e["value"] for e in events]
        dist = ", ".join("%sx%s" % (src_vals.count(v), fmt_val(v))
                         for v in sorted(set(src_vals), key=lambda x: (x is None, x)))

        if control:
            # Структурная проверка (манифест не содержит ch1-строк — якорная
            # сверка по голосу недоступна, размещение подтверждено отчётом
            # reports/ch1_sympathy_fix.md §3): пары like->tndl, standalone, null.
            src_like = sorted(e["value"] for e in events if e["kind"] == "like")
            src_solo = sorted(e["value"] for e in events if e["kind"] == "standalone")
            src_null = sum(1 for e in events if e["kind"] == "null_start")
            pairs, solo, nones = [], [], 0
            for fname in sorted(port["files"], key=part_key):
                lines = port["files"][fname]
                for n, ln in enumerate(lines, 1):
                    m = CALL_RE.match(ln)
                    if not m:
                        continue
                    val = None if m.group(1) == "None" else int(m.group(1))
                    if val is None:
                        nones += 1
                        continue
                    near_syn = False
                    k = n - 2
                    while k >= 0:
                        s = lines[k]
                        if not s.strip() or s.lstrip().startswith("#"):
                            k -= 1
                            continue
                        if SYN_RE.match(s):
                            near_syn = True
                        break
                    (pairs if near_syn else solo).append(val)
            pairs.sort()
            solo.sort()
            struct_ok = (pairs == src_like and solo == src_solo and nones == src_null)
            md.append("- вызовов в порте: %d (JA: %d); распределение: порт %s / JA %s"
                      % (len(port["calls"]), len(events), dist, dist))
            md.append("- пары `update_sympathy` → `tndl`: порт %d (значения %s) / JA like-смежные %d (%s)"
                      % (len(pairs), ", ".join(fmt_val(v) for v in pairs),
                         len(src_like), ", ".join(fmt_val(v) for v in src_like)))
            md.append("- standalone: порт %d (значения %s) / JA %d (%s); null: порт %d / JA %d"
                      % (len(solo), ", ".join(fmt_val(v) for v in solo),
                         len(src_solo), ", ".join(fmt_val(v) for v in src_solo),
                         nones, src_null))
            md.append("- структурный вердикт: **%s**" % ("PASS" if struct_ok else "REVIEW"))
            md.append("- примечание: `voice_id_map.csv` не содержит ch1-строк "
                      "(голосовой якорь для ch1 недоступен; отдельное наблюдение).")
            rows.append(dict(chapter=d, kind="control", status="CONTROL",
                             verdict="structural PASS" if struct_ok
                                     else "structural REVIEW"))
            summary.append((nn, d, len(events), len(port["calls"]), len(port["stale"]),
                            0, 0, 0, "PASS" if struct_ok else "REVIEW"))
            continue

        # --- обычные главы: план вставок ---
        inserts, noanchor = [], []
        stale_lines = port["stale"]
        for ev in events:
            res = resolve(ev, port, id2names, stale_lines)
            row = dict(chapter=d, source_line=ev["src_line"], scene=ev["scene"],
                       value=ev["value"], kind=ev["kind"])
            if ev["talk"]:
                row["talk_char"], row["voice_id"] = ev["talk"][0], ev["talk"][1]
            if res is None or not res.get("anchor_file"):
                at = res.get("anchor_type") if res else "resolve_none"
                if res and res.get("cands"):
                    row["cands"] = ";".join("%s:%d" % (c[0], c[1]) for c in res["cands"])
                row["status"] = "NO-ANCHOR(%s)" % at
                noanchor.append(row)
                rows.append(row)
                continue
            row.update({k: v for k, v in res.items()})
            row["insert_file"] = res["anchor_file"]
            row["insert_after"] = res["anchor_line"]
            row["status"] = "PLAN"
            inserts.append(row)
            rows.append(row)

        unpaired = pair_stale(inserts, stale_lines)

        summary.append((nn, d, len(events), len(port["calls"]), len(port["stale"]),
                        len(inserts), len(noanchor), len(unpaired),
                        "OK-PLAN" if not noanchor and not unpaired else "REVIEW"))

        md.append("- TNDL в JA: %d (%s); в порте вызовов: %d; stale-комментариев: %d"
                  % (len(events), dist, len(port["calls"]), len(port["stale"])))
        md.append("- план вставок: %d; NO-ANCHOR: %d; непарные stale: %d"
                  % (len(inserts), len(noanchor), len(unpaired)))
        md.append("")
        md.append("| src | scene | value | kind | якорь (файл:строка) | тип | voice | stale-комментарий |")
        md.append("|---|---|---|---|---|---|---|---|")
        for ins in sorted(inserts, key=lambda r: r["source_line"]):
            stale_txt = ""
            if ins.get("stale_file"):
                flag = "OK" if ins.get("stale_match") else "**MISMATCH**"
                stale_txt = "%s:%d val=%s %s" % (ins["stale_file"], ins["stale_line"],
                                                 fmt_val(ins["stale_claimed"]), flag)
            md.append("| %d | %s | %s | %s | %s:%s | %s | %s | %s |" % (
                ins["source_line"], ins["scene"], fmt_val(ins["value"]), ins["kind"],
                ins.get("anchor_file"), ins.get("anchor_line"), ins.get("anchor_type"),
                ins.get("voice_name") or "-", stale_txt))
        if noanchor:
            md.append("")
            md.append("**NO-ANCHOR (вручную):**")
            for r in noanchor:
                md.append("- src %d scene %s value=%s kind=%s talk=%s vid=%s type=%s %s" % (
                    r["source_line"], r["scene"], fmt_val(r["value"]), r["kind"],
                    r.get("talk_char"), r.get("voice_id"),
                    r["status"], r.get("cands", "")))
        if unpaired:
            md.append("")
            md.append("**Непарные stale-комментарии (вручную):**")
            for st in unpaired:
                md.append("- %s:%d val=%s :: %s" % (st[0], st[1], fmt_val(st[2]), st[3]))

    for i, s in enumerate(summary):
        md.insert(8 + i, "| %02d | %s | %d | %d | %d | %d | %d | %d | %s |" % s)

    (TASK_DIR / "s1_tndl_audit.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    cols = ["chapter", "source_line", "scene", "value", "kind", "talk_char",
            "voice_id", "voice_name", "anchor_file", "anchor_line", "anchor_type",
            "insert_file", "insert_after", "indent", "stale_file", "stale_line",
            "stale_claimed", "stale_match", "status", "cands", "verdict"]
    with (TASK_DIR / "s1_insert_plan.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)

    print("SUMMARY (src_ch, dir, JA, ported, stale, plan, noanchor, unpaired, status)")
    for s in summary:
        print(s)
    print("wrote s1_tndl_audit.md, s1_insert_plan.csv")


if __name__ == "__main__":
    main()