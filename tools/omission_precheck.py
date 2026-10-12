#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Omission Pre-check для pipeline ремастера (ZnT1).

Детерминированный технический слой (НЕ аудитор), который до запуска
аудиторских сессий A/B/C находит потенциально непокрытые JA-фрагменты и
кладёт их в evidence уровня CANDIDATE:

    reports/sma/<chapter_id>/<unit>/precheck/<run_id>.md

chapter_id: ch<N> для числовой главы, chextra для extra (как в agent_workflow).
unit:       report_unit части (ведущие цифры: 4b -> 4) либо "chapter"
            для охвата «вся глава» (совместимо с agent_workflow.sma_dir).

Принцип (строго детерминированный, без эвристик «на глазок»):

  1. Маркеры `# ==== SCENE N ====` / `# ==== CHOISE (scene N) ====` в EN-скрипте
     задают ОХВАТ части: множество сцен, реально присутствующих в переводе.
  2. JA-источник разбирается по сценам; отбираются реплики ТОЛЬКО сцен охвата
     (реплики других, ещё не портированных частей не считаются пропуском).
  3. Сопоставление — по voice-id: имя EN-реплики voice "..." -> id из
     references/voice_id_map.csv -> десятичный id JA-реплики [voice N].
     Порядок реплик и их длина НЕ используются (сравнение длин JA/RU
     запрещено как источник ложных срабатываний).
  4. JA-реплика охвата, для id которой нет EN-реплики, — кандидат FULL
     (выпавшая реплика).
  5. EN-реплика без непустого RU-перевода (tl/russian old -> new) — кандидат
     PARTIAL (строка есть, перевода нет).

Примеры запуска:
    python tools/omission_precheck.py --chapter 2_4b
    python tools/omission_precheck.py --chapter 3 --verbose
    python tools/omission_precheck.py --chapter extra

Инструмент ничего не правит: он только пишет evidence. Решение по каждому
кандидату выносит Analyzer (скилл semantic-analyzer), сверяя JA -> RU.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from output_util import ensure_safe_output, safe_print  # noqa: E402
from targets import resolve_target, TargetError  # noqa: E402


# ---------------------------------------------------------------- пути
ROOT = Path(__file__).parent.parent
GAME = ROOT / "game"
CHAPTERS_DIR = GAME / "chapters"
TL_RU_DIR = GAME / "tl" / "russian"
SRC_DIR = ROOT / "ps2_source" / "chapters"
MANIFEST = ROOT / "references" / "voice_id_map.csv"
VOICES_DIR = GAME / "audio" / "voices"
SMA_ROOT = ROOT / "reports" / "sma"

# ---------------------------------------------------------------- регэкспы
# JA-источник: `---- SCENE 0068 ----`, `[voice N]` (маркер в конце реплики),
# говорящий перед полноширинным двоеточием U+FF1A.
JA_SCENE_RE = re.compile(r"^----\s*SCENE\s+(\d+)\s*----")
JA_VOICE_RE = re.compile(r"\[voice\s+(\d+)\]")
JA_SPEAKER_RE = re.compile(r"^([^：\[\]]{1,24})：")

# EN-сценарий: `# ==== SCENE 68 ====`, `# ==== CHOISE (scene 137) ====`,
# `voice "..."`, реплика `char "..."`.
EN_SCENE_RE = re.compile(r"#\s*=+.*?scene\s*\(?\s*(\d+)", re.IGNORECASE)
EN_VOICE_RE = re.compile(r'^\s*voice\s+"([^"]+)"')
EN_SAY_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s+(.*)$")
EN_STR_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')

# Не-реплики Ren'Py: строка `word "..."` не должна приниматься за say-строку.
SAY_KEYWORDS = {
    "if", "elif", "else", "while", "for", "return", "jump", "call", "label",
    "menu", "python", "init", "define", "default", "scene", "show", "hide",
    "with", "play", "stop", "pause", "voice", "queue", "window", "nvl",
}

# tl/russian: `old "..."` / `new "..."`.
TL_OLD_RE = re.compile(r'^\s*old\s+"((?:[^"\\]|\\.)*)"')
TL_NEW_RE = re.compile(r'^\s*new\s+"((?:[^"\\]|\\.)*)"')

# манифест: `voice_name,voice_id`
MANIFEST_RE = re.compile(r"^([^,\s#]+)\s*,\s*(\d+)")


# ---------------------------------------------------------------- утилиты
def rel(path) -> str:
    """Путь относительно корня проекта (posix-слэши)."""
    try:
        return Path(path).resolve().relative_to(ROOT.resolve()).as_posix()
    except (ValueError, OSError):
        return str(path).replace("\\", "/")


_ESCAPES = {"n": "\n", "t": "\t", '"': '"', "\\": "\\"}


def unescape(s: str) -> str:
    """Снять Ren'Py-экранирование внутри строкового литерала."""
    return re.sub(r"\\(.)", lambda m: _ESCAPES.get(m.group(1), m.group(1)), s)


def strip_text_tags(s: str) -> str:
    """Убрать Ren'Py-теги {…} (запасной ключ поиска в tl)."""
    return re.sub(r"\{[^}]*\}", "", s)


# ---------------------------------------------------------------- JA-источник
def parse_ja_file(path: Path) -> list[dict]:
    """Разобрать один файл JA-источника в список voiced-реплик по порядку.

    Многострочная реплика склеивается: `[voice N]` стоит в конце её последней
    физической строки, а говорящий — в начале первой.
    """
    entries: list[dict] = []
    scene: int | None = None
    pending: dict | None = None

    def flush(voice_id: int | None = None) -> None:
        nonlocal pending
        if pending is not None:
            text = " ".join(p for p in pending["parts"] if p).strip()
            if voice_id is not None and text:
                entries.append({
                    "voice_id": voice_id,
                    "speaker": pending["speaker"] or "",
                    "text": text,
                    "scene": scene,
                    "line": pending["line"],
                    "file": rel(path),
                })
            pending = None

    with open(path, encoding="utf-8", errors="replace") as fh:
        for idx, raw in enumerate(fh, 1):
            s = raw.rstrip("\r\n")

            sm = JA_SCENE_RE.match(s)
            if sm:
                flush()
                scene = int(sm.group(1))
                continue

            vm = JA_VOICE_RE.search(s)
            if vm:
                spk = JA_SPEAKER_RE.match(s) if not s.startswith("  ") else None
                if spk:
                    flush()
                    pending = {"speaker": spk.group(1).strip(), "parts": [],
                               "line": idx}
                    body = s[spk.end():]
                else:
                    if pending is None:
                        pending = {"speaker": None, "parts": [], "line": idx}
                    body = s
                pending["parts"].append(JA_VOICE_RE.sub("", body).strip())
                flush(int(vm.group(1)))
                continue

            if not s.startswith("  "):
                spk = JA_SPEAKER_RE.match(s)
                if spk:
                    flush()
                    pending = {"speaker": spk.group(1).strip(),
                               "parts": [s[spk.end():]], "line": idx}
                    continue

            st = s.strip()
            if (not st) or st.startswith("【") or st.startswith("→") \
                    or st.startswith("----") or st.startswith("===") \
                    or st.startswith("#") or (st.startswith("[") and st.endswith("]")):
                flush()
                continue

            if pending is None:
                pending = {"speaker": None, "parts": [], "line": idx}
            pending["parts"].append(st)

    flush()
    return entries


def parse_ja_all() -> tuple[dict[int, list[dict]], dict[int, dict]]:
    """Разобрать все JA-источники.

    Возвращает (scene_entries, id_index):
      scene_entries — сцена -> список voiced-реплик;
      id_index      — voice_id -> первая реплика с этим id (глобально).
    """
    scene_entries: dict[int, list[dict]] = {}
    id_index: dict[int, dict] = {}
    for path in sorted(SRC_DIR.glob("chapter_*.txt")):
        for e in parse_ja_file(path):
            scene_entries.setdefault(e["scene"], []).append(e)
            id_index.setdefault(e["voice_id"], e)
    return scene_entries, id_index


# ---------------------------------------------------------------- EN-сценарий
def parse_en_file(path: Path) -> tuple[list[dict], list[int]]:
    """Разобрать EN-скрипт: voiced-реплики и маркеры сцен.

    Для каждой `voice "..."` ищется следующая say-строка (текст реплики),
    пропуская пустые строки, комментарии и `$ ...`-строки.
    """
    with open(path, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().splitlines()

    entries: list[dict] = []
    scenes: list[int] = []
    scene: int | None = None

    for idx, s in enumerate(lines, 1):
        sm = EN_SCENE_RE.search(s)
        if sm:
            scene = int(sm.group(1))
            scenes.append(scene)

        vm = EN_VOICE_RE.match(s)
        if not vm:
            continue

        name = vm.group(1)
        text: str | None = None
        text_line: int | None = None
        for j in range(idx, len(lines)):
            nxt = lines[j]
            if EN_VOICE_RE.match(nxt) or EN_SCENE_RE.search(nxt):
                break
            if nxt.lstrip().startswith("#") or not nxt.strip():
                continue
            if nxt.lstrip().startswith("$"):
                continue
            dm = EN_SAY_RE.match(nxt)
            if dm and dm.group(1) not in SAY_KEYWORDS and dm.group(2).lstrip().startswith('"'):
                sm2 = EN_STR_RE.search(dm.group(2))
                if sm2:
                    text = unescape(sm2.group(1))
                    text_line = j + 1
                break

        entries.append({
            "voice_name": name,
            "text": text,
            "scene": scene,
            "line": idx,
            "text_line": text_line,
            "file": rel(path),
        })

    return entries, scenes


# ---------------------------------------------------------------- манифест / RU
def load_manifest() -> dict[str, int]:
    """voice_id_map.csv -> {voice_name: voice_id} (строки с # пропускаются)."""
    manifest: dict[str, int] = {}
    if not MANIFEST.is_file():
        return manifest
    with open(MANIFEST, encoding="utf-8-sig", errors="replace") as fh:
        for raw in fh:
            m = MANIFEST_RE.match(raw.strip())
            if m:
                manifest[m.group(1)] = int(m.group(2))
    return manifest


def load_ogg_stems() -> set[str]:
    """Имена уже существующих .ogg (game/audio/voices) — как в check_project."""
    stems: set[str] = set()
    if VOICES_DIR.is_dir():
        for n in os.listdir(VOICES_DIR):
            if n.lower().endswith(".ogg"):
                stems.add(os.path.splitext(n)[0])
    return stems


def load_ru_translations() -> dict[str, str]:
    """tl/russian/*.rpy -> {old: new} (пустой new не затирает непустой)."""
    tr: dict[str, str] = {}
    if not TL_RU_DIR.is_dir():
        return tr
    for path in sorted(TL_RU_DIR.glob("*.rpy")):
        old: str | None = None
        with open(path, encoding="utf-8", errors="replace") as fh:
            for raw in fh:
                s = raw.rstrip("\r\n")
                mo = TL_OLD_RE.match(s)
                if mo:
                    old = unescape(mo.group(1))
                    continue
                mn = TL_NEW_RE.match(s)
                if mn and old is not None:
                    new = unescape(mn.group(1))
                    if new.strip() or old not in tr:
                        tr[old] = new
                    old = None
    return tr


# ---------------------------------------------------------------- охват / путь
def sma_location(target) -> tuple[str, str]:
    """(chapter_id, unit) для каталога evidence — по конвенции agent_workflow."""
    name = target.chapter_dir.name
    chapter_id = "chextra" if name == "extra" else f"ch{name}"

    if target.is_folder or len(target.files) != 1:
        return chapter_id, "chapter"

    stem = target.files[0].stem
    prefix = f"script-ch{name}_"
    if stem.startswith(prefix):
        part = stem[len(prefix):]
    elif name.isdigit():
        part = "1"
    else:
        part = stem
    m = re.match(r"(\d+)", part)
    return chapter_id, (m.group(1) if m else part)


# ---------------------------------------------------------------- анализ
def analyze(target, verbose: bool = False) -> dict:
    """Собрать evidence pre-check для цели (часть/файл/глава)."""
    manifest = load_manifest()
    scene_entries, id_index = parse_ja_all()

    en_entries: list[dict] = []
    en_scenes: set[int] = set()
    for f in target.files:
        entries, scenes = parse_en_file(f)
        en_entries.extend(entries)
        en_scenes.update(scenes)

    notes: list[str] = []

    # voice_name -> id; отдельно — голоса без строки в манифесте (ch0/extra
    # используют уже существующие .ogg и строк в voice_id_map.csv не требуют).
    ogg = load_ogg_stems()
    en_unknown = [e for e in en_entries if e["voice_name"] not in manifest]
    en_unresolved = [e for e in en_unknown if e["voice_name"] not in ogg]
    en_ogg_ok = [e for e in en_unknown if e["voice_name"] in ogg]
    for e in en_entries:
        e["voice_id"] = manifest.get(e["voice_name"])

    if en_unknown:
        notes.append(
            "Голоса без строки в voice_id_map.csv: %d; из них с уже "
            "существующим .ogg: %d, без .ogg и без id: %d. Для голосов без "
            "id детерминированное сопоставление JA<->EN по voice-id невозможно."
            % (len(en_unknown), len(en_ogg_ok), len(en_unresolved))
        )

    # Охват: сцены из EN-маркеров; если их нет — вывести по voice-id.
    scope_scenes = set(en_scenes)
    if not scope_scenes:
        inferred: set[int] = set()
        for e in en_entries:
            ja = id_index.get(e["voice_id"]) if e["voice_id"] is not None else None
            if ja and ja["scene"] is not None:
                inferred.add(ja["scene"])
        scope_scenes = inferred
        if scope_scenes:
            notes.append(
                "В сценарии цели нет маркеров `# ==== SCENE N ====`: охват "
                "определён по voice-id найденных реплик (границы усечены)."
            )
        else:
            notes.append(
                "Охват JA определить не удалось: маркеров сцен нет, voice-id "
                "не сопоставились. Поиск пропусков по сценам невозможен."
            )

    # JA-реплики охвата
    scope_ja: list[dict] = []
    for sc in sorted(scope_scenes):
        scope_ja.extend(scene_entries.get(sc, []))

    ja_by_id: dict[int, list[dict]] = {}
    for e in scope_ja:
        ja_by_id.setdefault(e["voice_id"], []).append(e)

    en_ids = Counter(e["voice_id"] for e in en_entries
                     if e["voice_id"] is not None)
    ja_ids = Counter(e["voice_id"] for e in scope_ja)
    missing = ja_ids - en_ids        # JA-id, не покрытые EN-репликами
    en_not_in_source = [e for e in en_entries
                        if e["voice_id"] is not None
                        and e["voice_id"] not in id_index]

    # сцены с незарегистрированными EN-голосами -> понижение confidence
    scenes_with_unknown = {e["scene"] for e in en_unknown}

    findings: list[dict] = []

    # FULL: выпавшая voiced-реплика JA
    for vid in sorted(missing):
        for ja in ja_by_id.get(vid, [])[:missing[vid]]:
            low = ja["scene"] in scenes_with_unknown
            findings.append({
                "candidate_id": "PC-JA-%d-%d" % (ja["line"], vid),
                "issue_type": "MISSING_TRANSLATION",
                "omission_scope": "DIALOGUE_FRAGMENT",
                "omission_kind": "FULL",
                "line": ja["line"],
                "scene": ja["scene"],
                "voice_id": vid,
                "speaker": ja["speaker"],
                "source": ja["text"],
                "ja_span": ja["text"],
                "ru_before": "",
                "ru_after": "",
                "missing_content": ja["text"],
                "not_compression_reason": (
                    "JA-реплике [voice %d] (%s) не соответствует ни одна "
                    "EN-реплика с этим voice-id в охвате части — реплика "
                    "выпала целиком, а не сжата." % (vid, ja["speaker"] or "?")
                ),
                "severity": "ERROR",
                "confidence": "LOW" if low else "HIGH",
                "evidence": "JA %s:%d (scene %s)" % (
                    ja["file"], ja["line"], ja["scene"]),
            })

    # PARTIAL: EN-реплика без непустого RU-перевода
    ru = load_ru_translations()
    ru_missing: list[dict] = []
    for e in en_entries:
        if not e["text"]:
            continue
        val = ru.get(e["text"])
        if val is None:
            val = ru.get(strip_text_tags(e["text"]))
        if val is None or not val.strip():
            ru_missing.append(e)

    for e in ru_missing:
        ja = id_index.get(e["voice_id"]) if e["voice_id"] is not None else None
        findings.append({
            "candidate_id": "PC-EN-%d" % e["line"],
            "issue_type": "MISSING_TRANSLATION",
            "omission_scope": "SENTENCE",
            "omission_kind": "PARTIAL",
            "line": e["line"],
            "scene": e["scene"],
            "voice_id": e["voice_id"],
            "voice_name": e["voice_name"],
            "source": e["text"],
            "ja_span": (ja["text"] if ja else ""),
            "ru_before": "",
            "ru_after": "",
            "missing_content": e["text"],
            "not_compression_reason": (
                "EN-строка %s существует, но RU-перевода для неё нет в "
                "tl/russian (текст отсутствует целиком, это не сжатие)."
                % e["voice_name"]
            ),
            "severity": "ERROR",
            "confidence": "HIGH",
            "evidence": "%s:%d" % (e["file"], e["text_line"] or e["line"]),
        })

    findings.sort(key=lambda c: (c["line"], c["candidate_id"]))

    stats = {
        "scope_scenes": sorted(scope_scenes),
        "ja_in_scope": len(scope_ja),
        "en_voices": len(en_entries),
        "covered": len(scope_ja) - sum(missing.values()),
        "full_omissions": sum(missing.values()),
        "ru_missing": len(ru_missing),
        "voices_without_manifest": len(en_unknown),
        "voices_ogg_ok": len(en_ogg_ok),
        "voices_unresolved": len(en_unresolved),
        "en_not_in_source": len(en_not_in_source),
        "candidates": len(findings),
    }

    result = {
        "target": target.key,
        "label": target.label,
        "chapter_id": sma_location(target)[0],
        "unit": sma_location(target)[1],
        "files": [rel(f) for f in target.files],
        "notes": notes,
        "stats": stats,
        "candidates": findings,
        "voices_without_manifest": [
            {"voice_name": e["voice_name"], "ogg_exists": e["voice_name"] in ogg,
             "file": e["file"], "line": e["line"]}
            for e in en_unknown
        ],
        "en_not_in_source": [
            {"voice_name": e["voice_name"], "voice_id": e["voice_id"],
             "file": e["file"], "line": e["line"]}
            for e in en_not_in_source
        ],
    }

    if verbose:
        safe_print("Omission Pre-check: %s (%s/%s)" % (
            target.label, result["chapter_id"], result["unit"]))
        safe_print("  JA in scope: %d (scenes: %d)" % (
            stats["ja_in_scope"], len(stats["scope_scenes"])))
        safe_print("  EN voices:   %d" % stats["en_voices"])
        safe_print("  covered:     %d" % stats["covered"])
        safe_print("  FULL:        %d" % stats["full_omissions"])
        safe_print("  RU missing:  %d" % stats["ru_missing"])
        safe_print("  voices w/o manifest id: %d (ogg ok %d, unresolved %d)" % (
            stats["voices_without_manifest"], stats["voices_ogg_ok"],
            stats["voices_unresolved"]))
        safe_print("  EN id not in JA source: %d" % stats["en_not_in_source"])
        safe_print("  candidates:  %d" % stats["candidates"])

    return result


# ---------------------------------------------------------------- evidence
def save_evidence(result: dict, target) -> Path:
    """Записать evidence в reports/sma/<chapter_id>/<unit>/precheck/."""
    now = datetime.datetime.now()
    base = now.strftime("%Y%m%d-%H%M%S") + "-p0a1"
    out_dir = SMA_ROOT / result["chapter_id"] / result["unit"] / "precheck"
    out_dir.mkdir(parents=True, exist_ok=True)

    run_id = base
    n = 2
    while (out_dir / (run_id + ".md")).exists():
        run_id = "%s-%d" % (base, n)
        n += 1
    out_path = out_dir / (run_id + ".md")

    stats = result["stats"]
    lines = [
        "# Omission Pre-check evidence",
        "",
        "- run_id: `%s`" % run_id,
        "- время: %s" % now.strftime("%Y-%m-%d %H:%M"),
        "- цель: `%s` (%s)" % (result["target"], result["label"]),
        "- каталог: `%s/%s`" % (result["chapter_id"], result["unit"]),
        "- файлы: %s" % ", ".join("`%s`" % f for f in result["files"]),
        "- статус: детерминированный слой (НЕ аудитор, НЕ голос)",
        "",
        "## Охват",
        "",
        "- сцены: %s" % (
            ", ".join(str(s) for s in stats["scope_scenes"]) or "(нет)"),
        "- JA-реплик в охвате: %d" % stats["ja_in_scope"],
        "- EN voiced-реплик: %d" % stats["en_voices"],
        "- покрыто: %d" % stats["covered"],
        "",
        "## Статистика",
        "",
        "| Показатель | Значение |",
        "|---|---|",
        "| FULL (выпавшая JA-реплика) | %d |" % stats["full_omissions"],
        "| RU missing (EN без перевода) | %d |" % stats["ru_missing"],
        "| Голос без id в манифесте | %d (из них .ogg есть: %d; не разрешён: %d) |"
        % (stats["voices_without_manifest"], stats["voices_ogg_ok"],
           stats["voices_unresolved"]),
        "| EN id не найден в JA | %d |" % stats["en_not_in_source"],
        "| Кандидатов всего | %d |" % stats["candidates"],
        "",
    ]

    if result["notes"]:
        lines.append("## Примечания")
        lines.append("")
        for note in result["notes"]:
            lines.append("- %s" % note)
        lines.append("")

    lines.append("## Кандидаты")
    lines.append("")
    if result["candidates"]:
        for i, c in enumerate(result["candidates"], 1):
            lines.append("### MISSING_TRANSLATION — %d (%s)" % (
                c["line"], c["omission_kind"]))
            lines.append("")
            lines.append("- Scope: %s" % c["omission_scope"])
            lines.append("- Kind: %s" % c["omission_kind"])
            lines.append("- Severity: %s (confidence %s)" % (
                c["severity"], c["confidence"]))
            if c.get("scene") is not None:
                lines.append("- Scene: %s" % c["scene"])
            lines.append("- Evidence: %s" % c.get("evidence", ""))
            lines.append("- JA: %s" % c["ja_span"])
            lines.append("- RU (before): %s" % (c["ru_before"] or "—"))
            lines.append("- RU (after): %s" % (c["ru_after"] or "—"))
            lines.append("- Missing: %s" % c["missing_content"])
            lines.append("- Reason (почему не компрессия): %s"
                         % c["not_compression_reason"])
            lines.append("")
    else:
        lines.append("_Кандидатов не найдено._")
        lines.append("")

    if result["voices_without_manifest"]:
        lines.append("## Голоса без пары имя<->id в voice_id_map.csv")
        lines.append("")
        lines.append("Строка манифеста нужна только для сопоставления JA -> EN "
                     "по voice-id. Если .ogg уже существует (главы 0/1/extra), "
                     "строка не требуется (см. шапку манифеста).")
        lines.append("")
        for u in result["voices_without_manifest"]:
            mark = "ogg OK" if u["ogg_exists"] else "NO ogg"
            lines.append("- `%s` [%s] — %s:%d" % (
                u["voice_name"], mark, u["file"], u["line"]))
        lines.append("")

    if result["en_not_in_source"]:
        lines.append("## EN voice-id не найден в JA-источнике")
        lines.append("")
        for u in result["en_not_in_source"]:
            lines.append("- `%s` (id %s) — %s:%d" % (
                u["voice_name"], u["voice_id"], u["file"], u["line"]))
        lines.append("")

    lines.append("## JSON")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps({
        "run_id": run_id,
        "timestamp": now.isoformat(),
        "chapter_id": result["chapter_id"],
        "unit": result["unit"],
        "target": result["target"],
        "stats": stats,
        "candidates": result["candidates"],
        "voices_without_manifest": result["voices_without_manifest"],
        "en_not_in_source": result["en_not_in_source"],
    }, ensure_ascii=False, indent=2))
    lines.append("```")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


# ---------------------------------------------------------------- main
def main() -> int:
    ensure_safe_output()
    parser = argparse.ArgumentParser(
        description="Omission Pre-check: JA-покрытие по voice-id в охвате части")
    parser.add_argument("--chapter", "-c", required=True,
                        help="Цель: 2 | 2_4b | 2_5* | script-ch2_5b.rpy | "
                             "extra | sp_l1 (см. tools/targets.py)")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--no-report", action="store_true",
                        help="Не писать evidence-файл")
    args = parser.parse_args()

    try:
        target = resolve_target(ROOT, args.chapter)
    except TargetError as e:
        safe_print("ERROR: %s" % e)
        return 2

    result = analyze(target, args.verbose)

    if not args.no_report:
        out_path = save_evidence(result, target)
        safe_print("Evidence: %s" % rel(out_path))

    n = result["stats"]["candidates"]
    if n == 0:
        safe_print("OK - кандидатов не найдено.")
    else:
        safe_print("Candidates: %d" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
