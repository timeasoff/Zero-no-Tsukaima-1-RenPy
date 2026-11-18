#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
renpy_gui_smoke.py — проверка игры через Ren'Py SDK: запуск, компиляция, скриншот.

Зачем: дать агенту/человеку быстрый способ проверить, что игра запускается с GUI,
и снять скриншот — без ручной возни с Xvfb и без вечных зависаний.

Подкоманды:
  precheck   Статический скан game/tl на дефекты, ломающие парсинг скрипта
             (без запуска движка). Это evidence, не вердикт.
  compile    Команда `compile` SDK: перекомпилирует скрипт и завершается
             (rc=0/1), печатает список ошибок парсинга.
             ВАЖНО: флаг `--compile` — не то же самое: он лишь форсирует
             перекомпиляцию перед обычным запуском (команда остаётся `run`),
             поэтому на чистом скрипте игра уходит в меню и ждёт ввод.
  shot       Запуск игры на Xvfb-дисплее + снятие кадра через ffmpeg x11grab
             -> PNG. Снимает то, что реально отрисовалось (меню / экран ошибки).

Окружение, которое выставляет инструмент (и headless-обёртка `renpy`):
  SDL_AUDIODRIVER=dummy, SDL_VIDEODRIVER=dummy — команде `compile` дисплей не нужен.
  DISPLAY=<Xvfb> — только для `shot`.
  RENPY_SIMPLE_EXCEPTIONS=1 — ошибка скрипта = быстрый выход rc=1 со списком
    `File "…", line N`, а не интерактивный экран, который под Xvfb ждёт ввод вечно.
  RENPY_EDIT_PY=tools/renpy_noop_editor.py — не пытаться открыть traceback
    в редакторе: в контейнере редактора и xdg-open нет.
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME_DIR = os.path.join(REPO, "game")
TL_DIR = os.path.join(GAME_DIR, "tl")
RENPY_SH = "/opt/renpy/renpy.sh"
NOOP_EDITOR = os.path.join(REPO, "tools", "renpy_noop_editor.py")
SHOT_DIR = os.path.join(REPO, ".tmp", "renpy_gui")
FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
XVFB = shutil.which("Xvfb") or "Xvfb"

PARSE_ERR_RE = re.compile(r'^File "([^"]+)", line (\d+): (.*)$', re.M)


# --------------------------------------------------------------------------- #
# precheck
# --------------------------------------------------------------------------- #

def scan_tl(tl_root):
    """Список дефектов (kind, relpath, lineno, snippet) в game/tl/**/*.rpy."""
    defects = []
    if not os.path.isdir(tl_root):
        return defects

    for dirpath, _dirs, files in os.walk(tl_root):
        for fn in sorted(files):
            if not fn.endswith(".rpy"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, GAME_DIR).replace(os.sep, "/")
            try:
                with open(full, encoding="utf-8") as f:
                    text = f.read()
            except UnicodeDecodeError as e:
                defects.append(("ENCODING", rel, 0, str(e)))
                continue

            lines = text.splitlines()
            has_directive = any(
                ln.lstrip().startswith("translate ") and ln.rstrip().endswith(":") for ln in lines
            )
            commented_only = (not has_directive) and any(
                ln.lstrip().startswith("# translate ") for ln in lines
            )

            # Обычная "-строка в old/new обязана закрыться в той же строке:
            # парсер вызывает compile(ll.rest(), "eval") — перенос строки
            # без \n ломает выражение -> "Could not parse string".
            # """...""" и \" допустимы.
            for i, ln in enumerate(lines, 1):
                s = ln.strip()
                m = re.match(r'(old|new)\s+"', s)
                if not m or s.startswith('"""') or s[m.end():].startswith('""'):
                    continue
                if not s[m.end():].rstrip().rstrip(",").endswith('"'):
                    defects.append(("UNTERMINATED_STRING", rel, i, s[:70]))

            # Блок old/new без рабочей директивы translate -> "Unexpected indentation".
            if not has_directive and any(ln.strip().startswith(("old ", "new ")) for ln in lines):
                kind = "MISSING_DIRECTIVE_COMMENTED" if commented_only else "MISSING_DIRECTIVE"
                first = next(
                    (j for j, ln in enumerate(lines, 1) if ln.strip().startswith(("old ", "new "))), 0
                )
                defects.append(
                    (kind, rel, first, lines[first - 1].strip()[:70] if first else "")
                )

    return defects


def cmd_precheck(tl_root):
    defects = scan_tl(tl_root)
    by_kind = {}
    for d in defects:
        by_kind.setdefault(d[0], []).append(d)

    print(f"=== precheck: дефектов загрузки скрипта: {len(defects)} ===")
    for kind in sorted(by_kind):
        items = by_kind[kind]
        files = sorted({it[1] for it in items})
        print(f"\n[{kind}] {len(items)} мест в {len(files)} файлах:")
        for it in items[:200]:
            print(f"  {it[1]}:{it[2]}  {it[3]}")
        if len(items) > 200:
            print(f"  ... ещё {len(items) - 200}")
    return 0 if not defects else 1


# --------------------------------------------------------------------------- #
# compile
# --------------------------------------------------------------------------- #

def sdk_env(extra=None):
    env = dict(os.environ)
    env["SDL_AUDIODRIVER"] = "dummy"
    env["SDL_VIDEODRIVER"] = "dummy"
    env["RENPY_SIMPLE_EXCEPTIONS"] = "1"
    env["RENPY_EDIT_PY"] = NOOP_EDITOR
    if extra:
        env.update(extra)
    return env


def cmd_compile(game, timeout):
    cmd = [RENPY_SH, game, "compile"]
    t0 = time.time()
    rc = None
    out = ""
    try:
        proc = subprocess.run(
            cmd,
            env=sdk_env(),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
        )
        rc = proc.returncode
        out = proc.stdout.decode("utf-8", "replace")
    except subprocess.TimeoutExpired as e:
        out = (e.stdout or b"").decode("utf-8", "replace") + "\n[TIMEOUT]"

    errs = PARSE_ERR_RE.findall(out)
    print(f"[compile] rc={rc} elapsed={time.time() - t0:.1f}s parse_errors={len(errs)}")
    for fn, ln, msg in errs[:40]:
        print(f"  {fn}:{ln}: {msg}")
    if len(errs) > 40:
        print(f"  ... ещё {len(errs) - 40}")

    if rc is None:
        return 3
    if errs:
        return 1
    return 0 if rc == 0 else 1


# --------------------------------------------------------------------------- #
# shot
# --------------------------------------------------------------------------- #

def find_free_display():
    for n in range(99, 60, -1):
        if not os.path.exists(f"/tmp/.X11-unix/X{n}") and not os.path.exists(f"/tmp/.X{n}-lock"):
            return n
    raise RuntimeError("нет свободного X-дисплея (:99..:61)")


def frame_stats(path):
    try:
        from PIL import Image

        im = Image.open(path)
        im.load()
        lo, hi = im.convert("L").getextrema()
        return im.size, (lo, hi)
    except Exception as e:  # noqa: BLE001 - диагностика, не критично
        return None, str(e)


def cmd_shot(game, out, wait, size):
    w, h = (int(x) for x in size.lower().split("x"))
    os.makedirs(SHOT_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)

    disp = find_free_display()
    run_log = os.path.join(SHOT_DIR, "run.log")

    xvfb = subprocess.Popen(
        [XVFB, f":{disp}", "-screen", "0", f"{w}x{h}x24", "-nolisten", "tcp"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    game_p = None
    logf = None
    try:
        for _ in range(100):
            if os.path.exists(f"/tmp/.X11-unix/X{disp}"):
                break
            time.sleep(0.1)

        # Намеренно без RENPY_SIMPLE_EXCEPTIONS: снимаем то, что реально
        # отрисовалось (меню или экран ошибки), а не получаем через секунду выход.
        env = sdk_env({"DISPLAY": f":{disp}"})
        env.pop("RENPY_SIMPLE_EXCEPTIONS", None)
        env.pop("SDL_VIDEODRIVER", None)

        logf = open(run_log, "ab")
        game_p = subprocess.Popen(
            [RENPY_SH, game],
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=logf,
            stderr=logf,
        )

        time.sleep(wait)

        ff = subprocess.run(
            [
                FFMPEG, "-y", "-loglevel", "error",
                "-f", "x11grab", "-video_size", f"{w}x{h}",
                "-i", f":{disp}", "-frames:v", "1", out,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    finally:
        if logf is not None:
            logf.close()
        for p in (game_p, xvfb):
            if p is None:
                continue
            try:
                p.terminate()
            except Exception:  # noqa: BLE001
                pass
        time.sleep(0.5)
        for p in (game_p, xvfb):
            if p is None:
                continue
            try:
                if p.poll() is None:
                    p.kill()
            except Exception:  # noqa: BLE001
                pass

    size_bytes = os.path.getsize(out) if os.path.exists(out) else 0
    dims, extrema = frame_stats(out) if size_bytes else (None, None)
    print(
        f"[shot] display=:{disp} game_rc={game_p.poll() if game_p else None} "
        f"ffmpeg_rc={ff.returncode} png={out} bytes={size_bytes} dims={dims} extrema={extrema}"
    )
    if ff.returncode != 0:
        print(ff.stdout.decode("utf-8", "replace")[:500])
    if not size_bytes:
        return 1
    if isinstance(extrema, tuple) and extrema[1] < 5:
        print("[shot] ВНИМАНИЕ: кадр почти чёрный — игра, возможно, не отрисовалась.")
    return 0


# --------------------------------------------------------------------------- #

def main():
    ap = argparse.ArgumentParser(description="Проверка игры через Ren'Py SDK (запуск/компиляция/скриншот).")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("precheck", help="статический скан game/tl (без движка)")
    p.add_argument("--tl", default=TL_DIR)

    p = sub.add_parser("compile", help="команда `compile` SDK: перекомпиляция + выход")
    p.add_argument("--game", default=GAME_DIR)
    p.add_argument("--timeout", type=int, default=300)

    p = sub.add_parser("shot", help="Xvfb + запуск игры + скриншот (ffmpeg x11grab)")
    p.add_argument("--game", default=GAME_DIR)
    p.add_argument("--out", default=os.path.join(SHOT_DIR, "screenshot.png"))
    p.add_argument("--wait", type=float, default=12.0, help="секунд ожидания перед снимком")
    p.add_argument("--size", default="1280x720", help="размер Xvfb-экрана, WxH")

    args = ap.parse_args()

    if args.cmd == "precheck":
        sys.exit(cmd_precheck(args.tl))
    if args.cmd == "compile":
        sys.exit(cmd_compile(args.game, args.timeout))
    if args.cmd == "shot":
        sys.exit(cmd_shot(args.game, args.out, args.wait, args.size))


if __name__ == "__main__":
    main()
