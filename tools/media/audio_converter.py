#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Конвертер голосов для pipeline ремастера (ZnT1).

Что делает (в отличие от старой версии, которая брала файлы из текущей папки):

  check    — сверка сценария, манифеста и wav_source: у каждой строки voice
             найден ли .ogg, есть ли пара имя↔id в references/voice_id_map.csv,
             найден ли сам .wav, зарегистрирован ли говорящий в characters.rpy;
  convert  — конвертация wav_source/*.wav -> game/audio/voices/<voice_name>.ogg
             по манифесту (сухой прогон по умолчанию, запись — --apply);
  scan     — предложение строк манифеста: сопоставляет voice "..." в сценарии
             и [voice N] в ps2_source строго по порядку, при расхождении
             счётчиков НИЧЕГО не пишет, а печатает отчёт о расхождении.

Используется агентом НА ФИНАЛЬНОМ ЭТАПЕ части: когда реплики портированы
и сопоставлены с аудио (строки манифеста добавлены), т.е. перед
python tools/check_project.py (иначе E3 «voice без ogg»).

Примеры:

  python tools/media/audio_converter.py check
  python tools/media/audio_converter.py check --only ch3
  python tools/media/audio_converter.py scan --chapter 3
  python tools/media/audio_converter.py convert --apply --chapter 3 --jobs 4

Отчёты: reports/voice_check.md (check), reports/voice_convert.md (convert),
reports/voice_scan_<ch>.md + reports/voice_map_draft_<ch>.csv (scan)
Манифест: references/voice_id_map.csv   (колонки voice_name,voice_id,wav_file,notes)
"""

import argparse
import csv
import datetime
import os
import re
import subprocess
import sys
from collections import OrderedDict, defaultdict
from concurrent.futures import ThreadPoolExecutor

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# ---------------------------------------------------------------- пути
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WAV_DIR = os.path.join(ROOT, "wav_source")
OUT_DIR = os.path.join(ROOT, "game", "audio", "voices")
MANIFEST = os.path.join(ROOT, "references", "voice_id_map.csv")
CHAPTERS_DIR = os.path.join(ROOT, "game", "chapters")
CHARACTERS = os.path.join(ROOT, "game", "characters.rpy")
SRC_DIR = os.path.join(ROOT, "ps2_source", "chapters")
REPORT = os.path.join(ROOT, "reports", "voice_convert.md")
CHECK_REPORT = os.path.join(ROOT, "reports", "voice_check.md")

OUTPUT_FORMAT = "ogg"

MANIFEST_HEADER = ["voice_name", "voice_id", "wav_file", "notes"]

WAV_ID_RE = re.compile(r"VOICE_ID\.BIN_([0-9A-Fa-f]{8})\.wav$", re.I)
VOICE_LINE_RE = re.compile(r'^\s*voice\s+"([^"]+)"')
SRC_VOICE_RE = re.compile(r"\[voice\s+(\d+)\]")
DEFINE_RE = re.compile(r"^\s*define\s+([A-Za-z_]\w*)\s*=\s*Character")
# ch3_s_001 / ch3.2_s_001 / sp_l1_s_003-2 -> говорящий s
SPEAKER_RE = re.compile(r"^(?:ch\d+(?:\.\d+)?|sp(?:_l\d+)?)_(.+?)_\d+")


def rel(path):
    try:
        return os.path.relpath(path, ROOT).replace(os.sep, "/")
    except ValueError:
        return path.replace(os.sep, "/")


# ---------------------------------------------------------------- данные
def wav_index():
    """id (dec) -> имя файла в wav_source/; плюс список неразобранных имён."""
    index = {}
    unparsed = []
    if not os.path.isdir(WAV_DIR):
        return index, unparsed
    for name in sorted(os.listdir(WAV_DIR)):
        full = os.path.join(WAV_DIR, name)
        if not os.path.isfile(full):
            continue
        m = WAV_ID_RE.search(name)
        if not m:
            unparsed.append(name)
            continue
        index.setdefault(int(m.group(1), 16), name)
    return index, unparsed


def script_voices(only=None):
    """voice_name -> [(file, line), ...] по всем сценариям глав."""
    result = OrderedDict()
    if not os.path.isdir(CHAPTERS_DIR):
        return result
    for dirpath, _dirs, files in os.walk(CHAPTERS_DIR):
        for fn in sorted(files):
            if not fn.endswith(".rpy"):
                continue
            full = os.path.join(dirpath, fn)
            try:
                with open(full, encoding="utf-8", errors="replace") as fh:
                    for i, line in enumerate(fh, 1):
                        m = VOICE_LINE_RE.match(line)
                        if not m:
                            continue
                        name = m.group(1)
                        if only and only not in name:
                            continue
                        result.setdefault(name, []).append((rel(full), i))
            except OSError as exc:
                print("не читается %s: %s" % (rel(full), exc))
    return result


def load_manifest():
    """voice_name -> {voice_id, wav_file, notes} (строки, начинающиеся с #, пропускаются)."""
    rows = OrderedDict()
    if not os.path.isfile(MANIFEST):
        return rows
    with open(MANIFEST, encoding="utf-8-sig", errors="replace", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            name = (row.get("voice_name") or "").strip()
            if not name or name.startswith("#"):
                continue
            vid = (row.get("voice_id") or "").strip()
            rows[name] = {
                "voice_id": int(vid) if vid.isdigit() else None,
                "wav_file": (row.get("wav_file") or "").strip(),
                "notes": (row.get("notes") or "").strip(),
            }
    return rows


def speaker_codes():
    codes = set()
    for dirpath, _dirs, files in os.walk(os.path.join(ROOT, "game")):
        if os.sep + "tl" + os.sep in dirpath + os.sep:
            continue
        for fn in files:
            if not fn.endswith(".rpy"):
                continue
            full = os.path.join(dirpath, fn)
            with open(full, encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    m = DEFINE_RE.match(line)
                    if m:
                        codes.add(m.group(1))
    return codes


def ogg_names():
    if not os.path.isdir(OUT_DIR):
        return set()
    return {os.path.splitext(n)[0] for n in os.listdir(OUT_DIR)
            if n.lower().endswith(".ogg")}


def speaker_of(name):
    m = SPEAKER_RE.match(name)
    return m.group(1) if m else None


def classify(names, manifest, wavs, have_ogg, defines):
    """Классификация каждой voice-строки сценария."""
    state = OrderedDict()
    for name in names:
        wav = None
        if name in have_ogg:
            kind = "ok_ogg"
        elif name in manifest:
            vid = manifest[name]["voice_id"]
            wav = manifest[name]["wav_file"] or (
                wavs.get(vid) if vid is not None else None)
            if vid is None and not manifest[name]["wav_file"]:
                kind = "manifest_no_id"
            elif wav is None:
                kind = "missing_wav"
            elif not os.path.isfile(os.path.join(WAV_DIR, wav)):
                kind = "missing_wav"
            else:
                kind = "pending"
        else:
            kind = "unmapped"
        spk = speaker_of(name)
        state[name] = {
            "kind": kind,
            "wav": wav,
            "speaker": spk,
            "speaker_known": (spk in defines) if spk else None,
            "where": [],
        }
    return state


def render(where, limit=20):
    if not where:
        return ""
    bits = ["%s:%d" % (f, i) for f, i in where[:limit]]
    extra = len(where) - limit
    return " (" + ", ".join(bits) + (" +%d" % extra if extra > 0 else "") + ")"


def write_report(path, lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines).rstrip() + "\n")
    return path


# ---------------------------------------------------------------- check
def cmd_check(args):
    wavs, unparsed = wav_index()
    manifest = load_manifest()
    have_ogg = ogg_names()
    defines = speaker_codes()
    voices = script_voices(args.only)

    state = classify(voices.keys(), manifest, wavs, have_ogg, defines)
    for name, info in state.items():
        info["where"] = voices[name]

    groups = defaultdict(list)
    for name, info in state.items():
        groups[info["kind"]].append(name)

    orphan = [n for n in manifest if n not in state]
    unknown_speakers = sorted({i["speaker"] for i in state.values()
                               if i["speaker"] and not i["speaker_known"]})
    no_format = [n for n in state if state[n]["speaker"] is None]

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    L = ["# Голоса: сверка (check)", "",
         "Запуск: `%s`" % now,
         "Команда: `python tools/media/audio_converter.py check%s`" %
         ((" --only %s" % args.only) if args.only else ""), "",
         "## Итоги", "",
         "| показатель | значений |",
         "|---|---:|",
         "| voice-строк в сценарии | %d |" % len(state),
         "| уже есть .ogg | %d |" % len(groups["ok_ogg"]),
         "| ждут конвертации (есть wav) | %d |" % len(groups["pending"]),
         "| **нет аудио (нет wav)** | **%d** |" % len(groups["missing_wav"]),
         "| **нет в манифесте (нет пары имя↔id)** | **%d** |" %
         len(groups["unmapped"]),
         "| манифест без voice_id | %d |" % len(groups["manifest_no_id"]),
         "| манифест: строк всего | %d |" % len(manifest),
         "| манифест: не используются сценарием | %d |" % len(orphan),
         "| wav в wav_source | %d |" % len(wavs),
         ""]

    def section(title, kind, hint):
        L.append("## %s" % title)
        L.append("")
        if not groups[kind]:
            L.append("_нет_")
            L.append("")
            return
        L.append("| voice_name | где встречается |")
        L.append("|---|---|")
        for n in sorted(groups[kind]):
            L.append("| `%s` | %s |" % (n, ", ".join(
                "%s:%d" % (f, i) for f, i in state[n]["where"][:3])))
        L.append("")
        L.append(hint)
        L.append("")

    section("Нет аудио: wav в wav_source не найден (voice_id из манифеста есть, "
              "файла нет)", "missing_wav",
            "→ отсутствует дорожка: проверить id в `transcriptions_ja_ru.csv` и "
            "`ps2_source/_diagnostics/voice_csv_index.txt`, при необходимости "
            "декодировать `.STV` (см. скилл `voice-workflow` §2). "
            "Обязательно указать в отчёте части.")
    section("Нет в манифесте: имя voice не сопоставлено с id (строка присутствует "
            "в сценарии, но .ogg не создан)", "unmapped",
            "→ добавить строку `voice_name,voice_id` в "
            "`references/voice_id_map.csv` (id из `[voice N]` источника) и "
            "повторить запуск; если .ogg уже существует — раздел неактуален.")
    section("Манифест без voice_id", "manifest_no_id",
            "→ заполнить колонку `voice_id` десятичным `[voice N]` из источника.")

    if unknown_speakers:
        L.append("## Говорящие без `define` в characters.rpy (нет имени → нет файлов)")
        L.append("")
        L.append(", ".join("`%s`" % s for s in unknown_speakers))
        L.append("")
        L.append("→ см. скилл `voice-workflow` §4.3 (регистрация + tl) и обязательно "
                 "отметить в отчёте части.")
        L.append("")
    if no_format:
        L.append("## Имена voice нестандартного формата (говорящий не определён)")
        L.append("")
        L.append(", ".join("`%s`" % n for n in sorted(no_format)))
        L.append("")
    if orphan:
        L.append("## Строки манифеста, которых нет в сценарии")
        L.append("")
        for n in sorted(orphan):
            L.append("- `%s` (voice_id=%s)" % (n, manifest[n]["voice_id"]))
        L.append("")
    if unparsed:
        L.append("## Неразобранные файлы в wav_source")
        L.append("")
        for n in unparsed:
            L.append("- `%s`" % n)
        L.append("")

    warnings = len(unknown_speakers) + len(unparsed) + len(orphan)
    problems = (len(groups["missing_wav"]) + len(groups["unmapped"]) +
                len(groups["manifest_no_id"]))
    L.append("## Итог")
    L.append("")
    L.append("**%s** (проблем: %d; предупреждений: %d; ждут конвертации: %d)" %
             ("OK" if problems == 0 else "ISSUES", problems, warnings,
              len(groups["pending"])))
    L.append("")
    if warnings:
        L.append("Предупреждения не блокируют конвертацию, но **обязательно "
                 "переносятся в отчёт части** (незарегистрированные говорящие, "
                 "неразобранные файлы, неиспользуемые строки манифеста).")
        L.append("")

    path = write_report(args.report, L)
    print("check: строк=%d ogg=%d pending=%d нет_аудио=%d нет_в_манифесте=%d "
          "предупреждений=%d" %
          (len(state), len(groups["ok_ogg"]), len(groups["pending"]),
           len(groups["missing_wav"]), len(groups["unmapped"]), warnings))
    print("отчёт: %s" % rel(path))
    print("RESULT: %s" % ("OK" if problems == 0 else "ISSUES"))
    return 0 if problems == 0 else 1


# ---------------------------------------------------------------- convert
def convert_one(wav_path, out_path):
    codec = {"ogg": ["-c:a", "libvorbis", "-q:a", "5"],
             "opus": ["-c:a", "libopus", "-b:a", "128k"],
             "mp3": ["-c:a", "libmp3lame", "-q:a", "2"],
             "flac": ["-c:a", "flac"],
             "wav": ["-c:a", "pcm_s16le"]}.get(OUTPUT_FORMAT, [])
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error",
           "-i", wav_path, *codec, "-y", out_path]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except FileNotFoundError:
        print("ffmpeg не найден. Установите FFmpeg "
              "(https://ffmpeg.org/download.html).")
        sys.exit(2)
    except subprocess.CalledProcessError as exc:
        return (out_path, (exc.stderr or "").strip()[:300])
    if not os.path.isfile(out_path) or os.path.getsize(out_path) == 0:
        return (out_path, "пустой выходной файл")
    return (out_path, None)


def cmd_convert(args):
    wavs, unparsed = wav_index()
    manifest = load_manifest()
    have_ogg = ogg_names()
    defines = speaker_codes()
    voices = script_voices(args.only)
    state = classify(voices.keys(), manifest, wavs, have_ogg, defines)
    for name, info in state.items():
        info["where"] = voices[name]

    pending = [n for n, i in state.items() if i["kind"] == "pending"]
    if args.chapter is not None:
        pending = [n for n in pending if n.startswith("ch%d" % args.chapter)
                   or n.startswith("ch%d." % args.chapter)]
    pending = sorted(pending)[:args.limit] if args.limit else sorted(pending)

    print("к конвертации: %d (сухой прогон, запись: --apply)" % len(pending))

    done, failed = [], []
    if pending and args.apply:
        os.makedirs(args.out, exist_ok=True)
        jobs = []
        for name in pending:
            wav_name = state[name]["wav"]
            wav_path = os.path.join(WAV_DIR, wav_name)
            out_path = os.path.join(args.out, name + "." + OUTPUT_FORMAT)
            jobs.append((name, wav_path, out_path))
        with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
            futures = [pool.submit(convert_one, w, o) for _n, w, o in jobs]
            for (name, _w, _o), fut in zip(jobs, futures):
                _out, err = fut.result()
                if err:
                    failed.append((name, err))
                    print("  ОШИБКА %s: %s" % (name, err))
                else:
                    done.append(name)
        print("сконвертировано: %d, ошибок: %d" % (len(done), len(failed)))

    # отчёт: полная картина (как в check) + результат конвертации
    groups = defaultdict(list)
    for name, info in state.items():
        groups[info["kind"]].append(name)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    L = ["# Голоса: конвертация", "",
         "Запуск: `%s`" % now,
         "Команда: `python tools/media/audio_converter.py convert%s%s`" %
         ((" --only %s" % args.only) if args.only else "",
          " --apply" if args.apply else " (сухой прогон)"),
         "Куда: `%s`" % rel(args.out), "",
         "## Итоги", "",
         "| показатель | значений |",
         "|---|---:|",
         "| voice-строк в сценарии | %d |" % len(state),
         "| уже есть .ogg | %d |" % len(groups["ok_ogg"]),
         "| к конвертации | %d |" % len(pending),
         "| сконвертировано сейчас | %d |" % len(done),
         "| ошибок конвертации | %d |" % len(failed),
         "| **нет аудио (нет wav)** | **%d** |" % len(groups["missing_wav"]),
         "| **нет в манифесте** | **%d** |" % len(groups["unmapped"]),
         "| wav в wav_source | %d |" % len(wavs),
         ""]
    if done:
        L += ["## Сконвертировано", ""]
        for n in done:
            L.append("- `%s.ogg`" % n)
        L.append("")
    if failed:
        L += ["## Ошибки конвертации", ""]
        for n, err in failed:
            L.append("- `%s`: %s" % (n, err.replace("\n", " ")))
        L.append("")
    if groups["missing_wav"]:
        L += ["## Нет аудио (wav не найден) — указать в отчёте части", ""]
        for n in sorted(groups["missing_wav"]):
            L.append("- `%s` (voice_id=%s)" %
                     (n, manifest.get(n, {}).get("voice_id")))
        L.append("")
    if groups["unmapped"]:
        L += ["## Нет в манифесте (нет пары имя↔id) — добавить строки "
              "и повторить", ""]
        for n in sorted(groups["unmapped"]):
            L.append("- `%s`%s" % (n, render(state[n]["where"], 3)))
        L.append("")
    unknown = sorted({i["speaker"] for i in state.values()
                      if i["speaker"] and not i["speaker_known"]})
    if unknown:
        L += ["## Говорящие без `define` — зарегистрировать и указать в отчёте", "",
              ", ".join("`%s`" % s for s in unknown), ""]
    if unparsed:
        L += ["## Неразобранные файлы wav_source", ""]
        L += ["- `%s`" % n for n in unparsed]
        L.append("")

    path = write_report(args.report, L)
    print("отчёт: %s" % rel(path))
    print("RESULT: %s" % ("OK" if not (failed or groups["missing_wav"]
                                       or groups["unmapped"]) else "ISSUES"))
    return 0 if not (failed or groups["missing_wav"] or groups["unmapped"]) else 1


# ---------------------------------------------------------------- scan
def source_path_for(chapter):
    prefix = "chapter_%02d_" % chapter
    for fn in sorted(os.listdir(SRC_DIR)):
        if fn.startswith(prefix) and fn.endswith(".txt"):
            return os.path.join(SRC_DIR, fn)
    return None


def script_files_for(chapter):
    folder = os.path.join(CHAPTERS_DIR, str(chapter))
    if not os.path.isdir(folder):
        return []
    out = []
    for fn in os.listdir(folder):
        if not fn.endswith(".rpy"):
            continue
        m = re.search(r"_(\d+)\.rpy$", fn)
        out.append((int(m.group(1)) if m else 0, fn))
    return [os.path.join(folder, fn) for _n, fn in sorted(out)]


def cmd_scan(args):
    if args.source and args.script:
        src_files = [args.source]
        script_files = list(args.script)
        tag = os.path.splitext(os.path.basename(args.source))[0]
    elif args.chapter is not None:
        src = source_path_for(args.chapter + 1)
        if not src:
            print("источник для главы %d не найден в %s" %
                  (args.chapter + 1, rel(SRC_DIR)))
            return 2
        script_files = script_files_for(args.chapter)
        if not script_files:
            print("нет сценариев в %s" % rel(os.path.join(CHAPTERS_DIR,
                                                         str(args.chapter))))
            return 2
        src_files = [src]
        tag = "ch%d" % args.chapter
    else:
        print("нужен --chapter N либо --source + --script")
        return 2

    names = []           # (name, file, line)
    for full in script_files:
        with open(full, encoding="utf-8", errors="replace") as fh:
            for i, line in enumerate(fh, 1):
                m = VOICE_LINE_RE.match(line)
                if m:
                    names.append((m.group(1), rel(full), i))

    ids = []             # (id, file, line)
    for full in src_files:
        with open(full, encoding="utf-8", errors="replace") as fh:
            for i, line in enumerate(fh, 1):
                for m in SRC_VOICE_RE.finditer(line):
                    ids.append((int(m.group(1)), rel(full), i))

    draft_path = os.path.join(ROOT, "reports",
                              "voice_map_draft_%s.csv" % tag)
    ok = len(names) == len(ids)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    L = ["# Скан манифеста голосов: %s" % tag, "",
         "Запуск: `%s`" % now, "",
         "| | значений |",
         "|---|---:|",
         "| voice-строк в сценарии | %d |" % len(names),
         "| [voice N] в источнике | %d |" % len(ids),
         "| расхождение | %d |" % (len(names) - len(ids)), "",
         "Источник: %s" % ", ".join(rel(f) for f in src_files),
         "Сценарии: %s" % ", ".join(rel(f) for f in script_files), ""]

    if ok:
        with open(draft_path, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(MANIFEST_HEADER)
            for (name, _f, _i), (vid, _sf, _sl) in zip(names, ids):
                w.writerow([name, vid, "",
                            "scan %s; проверить и перенести в %s"
                            % (now, rel(MANIFEST))])
        L += ["## Результат: счётчики совпали — черновик записан", "",
              "`%s`" % rel(draft_path), "",
              "Строки **предложены**, а не приняты: сверить, перенести в "
              "`references/voice_id_map.csv` (без колонки `notes` со служебной "
              "пометкой — по желанию), затем запустить `convert --apply`.", ""]
        print("scan %s: строк=%d, id=%d -> черновик %s"
              % (tag, len(names), len(ids), rel(draft_path)))
        print("RESULT: DRAFT")
    else:
        L += ["## Результат: расхождение счётчиков — черновик НЕ записан", "",
              "Причина может быть в пропущенной строке `voice \"...\"`, "
              "дополнительном `[voice N]` (extra scenes), несовпадении границ "
              "частей. Ни одна пара не считается доказанной: выровнять вручную "
              "и заполнить манифест вручную либо уточнить границы частей.", "",
              "### Первые voice-строки сценария", ""]
        for name, f, i in names[:10]:
            L.append("- `%s` %s:%d" % (name, f, i))
        L += ["", "### Первые [voice N] источника", ""]
        for vid, f, i in ids[:10]:
            L.append("- `%d` %s:%d" % (vid, f, i))
        L.append("")
        print("scan %s: РАСХОЖДЕНИЕ строк=%d id=%d (черновик не записан)"
              % (tag, len(names), len(ids)))
        print("RESULT: MISMATCH")

    path = write_report(os.path.join(ROOT, "reports",
                                     "voice_scan_%s.md" % tag), L)
    print("отчёт: %s" % rel(path))
    return 0 if ok else 1


# ---------------------------------------------------------------- CLI
def main():
    ap = argparse.ArgumentParser(
        description="Голоса ZnT1: check / convert / scan (wav_source -> "
                    "game/audio/voices)")
    sub = ap.add_subparsers(dest="cmd")

    p = sub.add_parser("check", help="сверка сценария, манифеста и wav_source")
    p.add_argument("--only", default=None, help="подстрока фильтра имён voice")
    p.add_argument("--report", default=CHECK_REPORT)
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("convert", help="wav_source -> game/audio/voices/<name>.ogg")
    p.add_argument("--apply", action="store_true",
                   help="записывать .ogg (без флага — только список)")
    p.add_argument("--only", default=None, help="подстрока фильтра имён voice")
    p.add_argument("--chapter", type=int, default=None,
                   help="только глава N (chN_ / chN.)")
    p.add_argument("--jobs", type=int, default=1, help="потоки ffmpeg (по умолчанию 1)")
    p.add_argument("--limit", type=int, default=0, help="не больше N файлов (тест)")
    p.add_argument("--out", default=OUT_DIR,
                   help="куда писать .ogg (по умолчанию game/audio/voices)")
    p.add_argument("--report", default=REPORT)
    p.set_defaults(func=cmd_convert)

    p = sub.add_parser("scan", help="предложить строки манифеста для главы")
    p.add_argument("--chapter", type=int, default=None,
                   help="проектная глава N (источник chapter_{N+1})")
    p.add_argument("--source", default=None, help="путь к txt источника")
    p.add_argument("--script", action="append", default=None,
                   help="путь к .rpy (можно несколько)")
    p.set_defaults(func=cmd_scan)

    args = ap.parse_args()
    if not getattr(args, "func", None):
        ap.print_help()
        return 0
    return args.func(args) or 0


if __name__ == "__main__":
    sys.exit(main())
