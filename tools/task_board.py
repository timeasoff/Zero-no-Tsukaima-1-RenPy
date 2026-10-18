#!/usr/bin/env python3
"""
Доска задач оркестратора ZnT1 (The Familiar Zero - Unofficial Remaster).

Персистентный журнал свободных задач ведущего агента: пользователь дал
задачу свободной форме («проверь главу 3», «проверь чанки 3_2 и 3_5»,
«продолжи перевод главы 4») - ведущий агент декомпозирует её на подзадачи
и ведёт их НЕ в памяти сессии, а на диске. Это переживает и компактизацию
контекста ведущего агента, и обрыв связи со субагентом.

Файлы:
  reports/task_board.json  - машиночитаемое состояние (в git);
  reports/task_board.md    - человекочитаемая сводка (генерируется sync);
  reports/tasks/<task>/<sub>.result.md  - result-маркер субагента
      (субагент пишет его по завершении; наличие маркера, а не возврат
      субагента, означает готовность подзадачи);
  reports/tasks/prompts/<task>_<sub>.md - сгенерированные промпты
      (в .gitignore; пересоздаются командой agent_workflow --out).

Жизненный цикл подзадачи:
  pending  -> running (start, со sessionID субагента) -> done | fail
  done/fail/skip - терминальные; у running обрыв читается через check.

Жизненный цикл задачи:
  open -> closed (close; только когда все подзадачи done/skipped).

ГЛАВНОЕ ПРАВИЛО ОБРЫВА: готовность подзадачи определяется НА ДИСКЕ
(result-маркер + артефакты), а не словесным отчётом субагента. Если
маркер PARTIAL или отсутствует - подзадача докрывается продолжением той
же сессии субагента (sessionID хранится в доске) либо перезапуском.

Консоль здесь cp1251: японский в вывод не попадает никогда, кириллица -
через output_util.safe_print. Все пути в сообщениях - прямые слэши.

Запускать из корня проекта:
  python tools/task_board.py status
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import uuid
from datetime import datetime
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import targets  # tools/targets.py: разрешение цели (2 | 2_4b | файл | extra)
from output_util import ensure_safe_output, safe_print

ROOT = Path(__file__).resolve().parent.parent
BOARD_PATH = ROOT / "reports" / "task_board.json"
MD_PATH = ROOT / "reports" / "task_board.md"
TASKS_DIR = ROOT / "reports" / "tasks"
PROMPTS_DIR = TASKS_DIR / "prompts"

BOARD_VERSION = 1

# Статусы подзадач и задач.
SUB_PENDING = "pending"
SUB_RUNNING = "running"
SUB_DONE = "done"
SUB_FAILED = "failed"
SUB_SKIPPED = "skipped"
SUB_TERMINAL = (SUB_DONE, SUB_FAILED, SUB_SKIPPED)

TASK_OPEN = "open"
TASK_CLOSED = "closed"

# Служба: сколько минут mtime артефакта может «отстать» от started
# (субагент мог стартовать чуть раньше фиксации start - допуск).
MTIME_SLACK_MIN = 5


# ============================================================================
# УТИЛИТЫ
# ============================================================================
def now_iso() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def new_task_id() -> str:
    return f"T{datetime.now():%Y%m%d-%H%M%S}-{uuid.uuid4().hex[:4]}"


def rel(path: Path | str) -> str:
    """Путь относительно корня проекта, прямые слэши (для сообщений)."""
    p = Path(path)
    try:
        return p.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return p.as_posix()


def marker_rel(task_id: str, sub_id: str) -> str:
    return f"reports/tasks/{task_id}/{sub_id}.result.md"


def marker_path(task_id: str, sub_id: str) -> Path:
    return TASKS_DIR / task_id / f"{sub_id}.result.md"


def prompt_rel(task_id: str, sub_id: str) -> str:
    return f"reports/tasks/prompts/{task_id}_{sub_id}.md"


# ============================================================================
# ДОСКА: ЗАГРУЗКА / СОХРАНЕНИЕ
# ============================================================================
def load_board() -> dict:
    if not BOARD_PATH.is_file():
        return {"version": BOARD_VERSION, "tasks": []}
    try:
        with open(BOARD_PATH, encoding="utf-8") as fh:
            board = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"ERROR: cannot read board {rel(BOARD_PATH)}: {exc}")
    board.setdefault("version", BOARD_VERSION)
    board.setdefault("tasks", [])
    return board


def save_board(board: dict) -> None:
    """Атомарное сохранение (tmp + replace), UTF-8, LF."""
    BOARD_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = BOARD_PATH.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(board, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    os.replace(tmp, BOARD_PATH)


def find_task(board: dict, task_id: str | None) -> dict:
    """Найти задачу по id; без id - ровно одна открытая, иначе ошибка."""
    tasks = board["tasks"]
    if task_id:
        for t in tasks:
            if t["id"] == task_id:
                return t
        ids = ", ".join(t["id"] for t in tasks) or "(none)"
        raise SystemExit(f"ERROR: task '{task_id}' not found. Existing: {ids}")
    open_tasks = [t for t in tasks if t["status"] == TASK_OPEN]
    if len(open_tasks) == 1:
        return open_tasks[0]
    if not open_tasks:
        raise SystemExit(
            "ERROR: no open task. Create one: "
            "python tools/task_board.py new --request \"...\" [--target N]")
    ids = ", ".join(t["id"] for t in open_tasks)
    raise SystemExit(f"ERROR: several open tasks ({ids}) - specify task id.")


def find_sub(task: dict, sub_id: str) -> dict:
    for s in task["subtasks"]:
        if s["id"] == sub_id:
            return s
    ids = ", ".join(s["id"] for s in task["subtasks"]) or "(none)"
    raise SystemExit(
        f"ERROR: subtask '{sub_id}' not found in {task['id']}. "
        f"Existing: {ids}")


def next_sub_id(task: dict) -> str:
    n = len(task["subtasks"]) + 1
    while f"S{n}" in {s["id"] for s in task["subtasks"]}:
        n += 1
    return f"S{n}"


# ============================================================================
# РАЗБОР ЦЕЛИ (best-effort, не роняет при несуществующем файле)
# ============================================================================
def target_parts(target: str, scope: str) -> dict:
    """Извлечь chapter_id/unit из цели best-effort.

    Часть может быть ещё не создана (port-part новой части) - поэтому
    targets.resolve_target используется только как удача, а не как обязанность.
    Возвращает {"chapter_id": "ch4", "unit": "6"|"chapter"|<файл>,
    "ok": bool, "script": rel|None, "report": rel|None}.
    """
    info = {"chapter_id": None, "unit": None, "ok": False,
            "script": None, "report": None}
    raw = (target or "").strip()

    # 1. Попытка точного резолва (существующий файл/папка).
    chapter_dir = None
    file_name = None
    try:
        t = targets.resolve_target(ROOT, raw)
        chapter_dir = t.chapter_dir.name
        if t.files:
            file_name = t.files[0].name
    except targets.TargetError:
        pass

    # 2. Фолбэк по синтаксису цели.
    if chapter_dir is None:
        m = re.fullmatch(r"(\d+)[_/](\w+)", raw)
        if m:
            chapter_dir, part = m.group(1), m.group(2)
            file_name = f"script-ch{chapter_dir}_{part}.rpy"
        elif re.fullmatch(r"\d+", raw):
            chapter_dir = raw
        elif re.fullmatch(r"sp_\w+", raw):
            chapter_dir, file_name = "extra", f"{raw}.rpy"
        elif re.fullmatch(r"script-ch(\d+)(?:_(\w+))?\.rpy", raw):
            m2 = re.fullmatch(r"script-ch(\d+)(?:_(\w+))?\.rpy", raw)
            chapter_dir = m2.group(1)
            file_name = raw
        elif raw in ("extra",):
            chapter_dir = "extra"
    if chapter_dir is None:
        return info

    info["chapter_id"] = "chextra" if chapter_dir == "extra" else f"ch{chapter_dir}"

    # 3. Единица отчёта/SMA и пути.
    if scope == "chapter":
        info["unit"] = "chapter"
        script = None
        folder = ROOT / "game" / "chapters" / chapter_dir
        if folder.is_dir():
            cands = sorted(p.name for p in folder.glob("script-*.rpy"))
            script = f"game/chapters/{chapter_dir}/{cands[0]}" if cands else None
        info["script"] = script
    else:
        if file_name is None:
            folder = ROOT / "game" / "chapters" / chapter_dir
            cands = sorted(p.name for p in folder.glob("script-*.rpy")) \
                if folder.is_dir() else []
            if len(cands) == 1:
                file_name = cands[0]
        if file_name:
            info["script"] = f"game/chapters/{chapter_dir}/{file_name}"
            m3 = re.match(r"script-ch\d+_(.+)\.rpy", file_name)
            if chapter_dir == "0" or (file_name == "script-ch0.rpy"):
                info["unit"] = "0"
            elif m3:
                mm = re.match(r"(\d+)", m3.group(1))
                info["unit"] = mm.group(1) if mm else m3.group(1)
            elif file_name.startswith("script-"):
                info["unit"] = file_name[len("script-"):-len(".rpy")]
            else:
                info["unit"] = file_name[:-len(".rpy")]
        else:
            m4 = re.fullmatch(r"(\d+)", chapter_dir)
            info["unit"] = "1" if m4 else None
    if info["chapter_id"] and info["unit"]:
        info["report"] = f"reports/{info['chapter_id']}/{info['unit']}.md"
        info["ok"] = True
    return info


# ============================================================================
# КОНТРАКТ СУБАГЕНТА (текст, который ведущий агент ДОЛЖЕН приложить)
# ============================================================================
def work_contract(task_id: str, sub_id: str) -> str:
    """Обязательная приписка к промпту каждого субагента.

    Возвращает готовый текст: субагент получает маркер-путь и правила,
    при которых обрыв связи не теряет результат.
    """
    marker = marker_rel(task_id, sub_id)
    return f"""
ПРОТОКОЛ ЗАВЕРШЕНИЯ (обязателен, перекрывает всё остальное):
1. Работай только файлами проекта; доску задач reports/task_board.json
   НЕ читай и НЕ изменяй - её ведёт ведущий агент.
2. По завершении (успех ИЛИ частичный результат ИЛИ невозможность
   закончить) ОБЯЗАТЕЛЬНО запиши result-маркер:
   {marker}
   Структура (UTF-8):
     STATUS: DONE | PARTIAL
     СДЕЛАНО: <что сделано, коротко>
     ФАЙЛЫ: <изменённые файлы через запятую, rel-пути>
     ПРОВЕРКИ: <какие проверки прогнаны и их итог>
     ОСТАЛОСЬ: <что не сделано и почему; пусто при DONE>
     ВОПРОСЫ: <сомнения/??? для человека; пусто если нет>
   Маркер - ЕДИНСТВЕННОЕ доказательство завершения: без него ведущий
   агент считает подзадачу оборванной и продолжит (возможно, той же
   сессией). Не пропускай шаг записи маркера даже при успехе.
3. Не выполняй git commit; не удаляй файлы молча.
""".strip()


# ============================================================================
# ПРОВЕРКИ НА ДИСКЕ (check / verify)
# ============================================================================
SMA_KIND_BY_PROMPT = {
    "semantic-audit-a": "a",
    "pragmatic-c": "c",
    "analyzer-phase1": "analysis",
    "analyzer-phase2": "analysis",
}
REPORT_UNIT_PROMPTS = ("translate-edit", "full-audit", "grammar-audit",
                       "style-audit", "humanizer", "encoding-check")
PORT_PROMPTS = ("port-part", "continue", "first-launch")


def _mtime(path: Path) -> float | None:
    try:
        return path.stat().st_mtime
    except OSError:
        return None


def _newer_than(path: Path, started_iso: str | None,
                slack_min: int = MTIME_SLACK_MIN) -> bool | None:
    """True/False; None - нет timestamp для сравнения (started не задан)."""
    mt = _mtime(path)
    if mt is None:
        return False
    if not started_iso:
        return None
    try:
        started = datetime.strptime(started_iso, "%Y-%m-%d %H:%M:%S").timestamp()
    except ValueError:
        return None
    return mt >= started - slack_min * 60


def read_marker(task_id: str, sub_id: str) -> dict | None:
    """Прочитать result-маркер подзадачи; None - маркера нет."""
    path = marker_path(task_id, sub_id)
    if not path.is_file():
        return None
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    status = "DONE"
    m = re.search(r"^\s*STATUS:\s*(\w+)", text, re.MULTILINE | re.IGNORECASE)
    if m:
        status = m.group(1).upper()
    head = [ln for ln in text.splitlines() if ln.strip()][:12]
    return {"path": rel(path), "status": status, "mtime": _mtime(path),
            "head": head}


def expected_artifacts(sub: dict) -> list[tuple[str, str]]:
    """Ожидаемые артефакты подзадачи: [(kind, rel-путь-или-каталог)].

    kind: file | dir | sma | sma-phase1 | script+report.
    Best-effort: при несуществующей цели возвращает пусто - проверка
    сводится к перечню evidence подзадачи.
    """
    if sub["kind"] != "prompt":
        return []
    pid = sub.get("prompt") or ""
    info = target_parts(sub.get("target") or "", sub.get("scope") or "part")
    out: list[tuple[str, str]] = []
    if pid in SMA_KIND_BY_PROMPT:
        kind_dir = SMA_KIND_BY_PROMPT[pid]
        if info["chapter_id"] and info["unit"]:
            base = f"reports/sma/{info['chapter_id']}/{info['unit']}/{kind_dir}"
            if pid == "analyzer-phase1":
                out.append(("sma-phase1", base))
            elif pid == "analyzer-phase2":
                out.append(("sma-phase2", base))
            else:
                out.append(("dir", base))
        return out
    if pid in PORT_PROMPTS:
        if info["script"]:
            out.append(("file", info["script"]))
        if info["report"]:
            out.append(("file", info["report"]))
        return out
    if pid in REPORT_UNIT_PROMPTS:
        if info["report"]:
            out.append(("file", info["report"]))
        return out
    if pid == "voice-work":
        out.append(("file", "reports/voice_check.md"))
        if info["script"]:
            out.append(("file", info["script"]))
        return out
    if pid == "check-project" or sub["kind"] == "action":
        out.append(("file", "reports/check_project.md"))
        return out
    return out


def verify_sub(sub: dict, task_id: str) -> list[str]:
    """Проверка одной подзадачи. Возвращает список проблем (пусто - OK)."""
    problems: list[str] = []
    started = sub.get("started")
    for kind, rpath in expected_artifacts(sub):
        p = ROOT / rpath
        if kind == "dir":
            if not p.is_dir() or not any(p.glob("*.md")):
                problems.append(f"нет evidence-каталога {rpath}/*.md")
        elif kind == "sma-phase1":
            if not p.is_dir() or not any(p.glob("*.phase1.md")):
                problems.append(f"нет слепого вывода {rpath}/*.phase1.md")
        elif kind == "sma-phase2":
            hits = [f for f in p.glob("*.md")
                    if not f.name.endswith(".phase1.md")] if p.is_dir() else []
            if not hits:
                problems.append(f"нет решения {rpath}/*.md (без .phase1)")
        else:  # file
            if not p.is_file():
                problems.append(f"нет файла {rpath}")
            elif _newer_than(p, started) is False and started:
                problems.append(
                    f"{rpath} не обновлялся после старта подзадачи ({started})")
    for ev in sub.get("evidence") or []:
        if not (ROOT / ev).exists():
            problems.append(f"нет заявленного evidence: {ev}")
    marker = read_marker(task_id, sub["id"])
    if marker and marker["status"] != "DONE" and sub["status"] == SUB_DONE:
        problems.append(f"маркер {marker['path']} имеет STATUS != DONE")
    return problems


# ============================================================================
# КОМАНДЫ
# ============================================================================
def cmd_new(args) -> int:
    board = load_board()
    task = {
        "id": new_task_id(),
        "created": now_iso(),
        "request": args.request,
        "target": args.target or "",
        "status": TASK_OPEN,
        "subtasks": [],
    }
    board["tasks"].append(task)
    save_board(board)
    safe_print(f"CREATED: {task['id']}")
    safe_print(f"  request: {task['request']}")
    if task["target"]:
        safe_print(f"  target:  {task['target']}")
    safe_print("Следующий шаг - декомпозиция:")
    safe_print(f"  python tools/task_board.py sub-add {task['id']} "
               f"--prompt <prompt-id> --target <цель> [--scope chapter] "
               f"[--title \"...\"]")
    safe_print(f"  python tools/task_board.py sub-add {task['id']} "
               f"--manual \"<описание>\" [--target <цель>]")
    return 0


def cmd_sub_add(args) -> int:
    board = load_board()
    task = find_task(board, args.task)
    if bool(args.prompt) == bool(args.manual):
        safe_print("ERROR: укажите РОВНО ОДНО из: --prompt <id> | --manual \"текст\"")
        return 2
    sub = {
        "id": next_sub_id(task),
        "kind": "prompt" if args.prompt else "manual",
        "prompt": args.prompt or "",
        "target": args.target or task.get("target") or "",
        "scope": args.scope or "part",
        "title": args.title or (args.prompt or args.manual or ""),
        "status": SUB_PENDING,
        "created": now_iso(),
        "started": None,
        "finished": None,
        "session": None,
        "note": "",
        "evidence": [],
        "manual": args.manual or "",
    }
    if sub["kind"] == "prompt" and not args.target and not task.get("target"):
        safe_print("ERROR: --prompt требует --target (или --target у задачи).")
        return 2
    task["subtasks"].append(sub)
    save_board(board)
    safe_print(f"ADDED: {task['id']}/{sub['id']}  [{sub['kind']}] "
               f"{sub['target'] or '-'}  {sub['title']}")
    return 0


def _status_mark(s: dict) -> str:
    marks = {SUB_PENDING: " ", SUB_RUNNING: "~", SUB_DONE: "x",
             SUB_FAILED: "!", SUB_SKIPPED: "-"}
    return marks.get(s["status"], "?")


def cmd_status(args) -> int:
    board = load_board()
    tasks = board["tasks"]
    if args.task:
        tasks = [find_task(board, args.task)]
    open_tasks = [t for t in board["tasks"] if t["status"] == TASK_OPEN]
    safe_print(f"BOARD: {rel(BOARD_PATH)}  (задач всего: {len(tasks)}, "
               f"открытых: {len(open_tasks)})")
    if not tasks:
        safe_print("  Задач нет. Создай: python tools/task_board.py new "
                   "--request \"...\"")
        return 0
    for t in tasks:
        safe_print()
        safe_print(f"{t['id']}  [{t['status']}]  target={t.get('target') or '-'}")
        safe_print(f"  request: {t['request']}")
        if not t["subtasks"]:
            safe_print("  (подзадач нет - нужна декомпозиция)")
            continue
        done = sum(1 for s in t["subtasks"] if s["status"] in (SUB_DONE, SUB_SKIPPED))
        safe_print(f"  подзадач: {len(t['subtasks'])}, закрыто: {done}")
        for s in t["subtasks"]:
            marker = "маркер+" if read_marker(t["id"], s["id"]) else "маркер-"
            sess = f" ses={s['session']}" if s.get("session") else ""
            target = f" {s['target']}" if s.get("target") else ""
            prompt = f" {s['prompt']}" if s.get("prompt") else ""
            safe_print(f"   [{_status_mark(s)}] {s['id']:<4} "
                       f"{s['status']:<8}{prompt}{target}  {marker}{sess}")
            safe_print(f"         {s['title']}")
            if s.get("note"):
                safe_print(f"         note: {s['note']}")
    safe_print()
    safe_print("Легенда: [ ] pending  [~] running  [x] done  [!] failed  "
               "[-] skipped")
    safe_print("Обрыв/восстановление: python tools/task_board.py check "
               "<task>")
    return 0


def _subcommands_block(task: dict, s: dict) -> list[str]:
    """Точные команды исполнения одной подзадачи (для next)."""
    lines: list[str] = []
    if s["kind"] == "prompt":
        out = prompt_rel(task["id"], s["id"])
        cmd = (f"python tools/agent_workflow.py --prompt {s['prompt']} "
               f"--chapter {s['target']}")
        if s["scope"] == "chapter":
            cmd += " --scope chapter"
        cmd += f" --out {out}"
        lines.append(cmd)
        lines.append(f"(затем: задание субагенту = текст из {out} + "
                     f"ПРОТОКОЛ ЗАВЕРШЕНИЯ: "
                     f"python tools/task_board.py contract {task['id']} {s['id']}; "
                     f"после запуска записать сессию: "
                     f"python tools/task_board.py start {task['id']} {s['id']} "
                     f"--session <sessionID>)")
    else:
        lines.append(f"manual: {s.get('manual') or s['title']}")
        lines.append(f"(записать старт: python tools/task_board.py start "
                     f"{task['id']} {s['id']})")
    return lines


def cmd_next(args) -> int:
    board = load_board()
    task = find_task(board, args.task)
    # 1. Сначала - running: возможно, это оборванные подзадачи.
    running = [s for s in task["subtasks"] if s["status"] == SUB_RUNNING]
    if running:
        safe_print("ВНИМАНИЕ: есть RUNNING-подзадачи - сначала проверь обрыв:")
        safe_print(f"  python tools/task_board.py check {task['id']}")
        safe_print()
    pending = [s for s in task["subtasks"] if s["status"] == SUB_PENDING]
    if not pending:
        if running:
            safe_print("Pending нет; running-подзадачи ждут решения по check.")
            return 0
        safe_print(f"Все подзадачи {task['id']} закрыты. Задачу можно закрыть:")
        safe_print(f"  python tools/task_board.py close {task['id']}")
        return 0
    s = pending[0]
    safe_print(f"СЛЕДУЮЩАЯ ПОДЗАДАЧА: {task['id']}/{s['id']}  [{s['kind']}]")
    safe_print(f"  title:  {s['title']}")
    if s.get("target"):
        safe_print(f"  target: {s['target']} (scope: {s['scope']})")
    safe_print("Команды:")
    for line in _subcommands_block(task, s):
        safe_print(f"  {line}")
    if len(pending) > 1:
        safe_print(f"Дальше в очереди: "
                   f"{', '.join(x['id'] for x in pending[1:])}")
    return 0


def cmd_start(args) -> int:
    board = load_board()
    task = find_task(board, args.task)
    s = find_sub(task, args.sub)
    if s["status"] in SUB_TERMINAL:
        safe_print(f"ERROR: {s['id']} уже в терминальном статусе {s['status']}")
        return 2
    s["status"] = SUB_RUNNING
    s["started"] = now_iso()
    s["finished"] = None
    if args.session:
        s["session"] = args.session
    save_board(board)
    sess = f", session={s['session']}" if s.get("session") else ""
    safe_print(f"STARTED: {task['id']}/{s['id']} at {s['started']}{sess}")
    if s["kind"] == "prompt":
        safe_print(f"  маркер субагента (пишет он): "
                   f"{marker_rel(task['id'], s['id'])}")
    return 0


def cmd_done(args) -> int:
    board = load_board()
    task = find_task(board, args.task)
    s = find_sub(task, args.sub)
    s["status"] = SUB_DONE
    s["finished"] = now_iso()
    if args.note:
        s["note"] = args.note
    for ev in args.evidence or []:
        if ev not in s["evidence"]:
            s["evidence"].append(ev)
    save_board(board)
    safe_print(f"DONE: {task['id']}/{s['id']} at {s['finished']}")
    marker = read_marker(task["id"], s["id"])
    safe_print(f"  маркер: {marker['path'] if marker else 'НЕТ'}")
    if not marker:
        safe_print("  WARNING: маркер субагента отсутствует - готовность "
                   "подтверждена только твоей проверкой.")
    return 0


def cmd_fail(args) -> int:
    board = load_board()
    task = find_task(board, args.task)
    s = find_sub(task, args.sub)
    s["status"] = SUB_FAILED
    s["finished"] = now_iso()
    s["note"] = args.note or "failed"
    save_board(board)
    safe_print(f"FAILED: {task['id']}/{s['id']}: {s['note']}")
    safe_print("Можно добавить замену: python tools/task_board.py sub-add "
               f"{task['id']} --prompt <id> --target <цель>")
    return 0


def cmd_skip(args) -> int:
    board = load_board()
    task = find_task(board, args.task)
    s = find_sub(task, args.sub)
    s["status"] = SUB_SKIPPED
    s["finished"] = now_iso()
    s["note"] = args.note or "skipped"
    save_board(board)
    safe_print(f"SKIPPED: {task['id']}/{s['id']}: {s['note']}")
    return 0


def cmd_check(args) -> int:
    """Главная команда восстановления после обрыва/компактизации.

    Для каждой незакрытой подзадачи определяет по диску:
      READY      - result-маркер STATUS: DONE -> можно done;
      PARTIAL    - маркер STATUS: PARTIAL -> продолжить субагента;
      ORPHANED   - started есть, маркера нет -> обрыв: продолжить сессией
                   (если session записан) либо перезапустить;
      PENDING    - ещё не запускалась -> запускать по next.
    Ничего не изменяет - только диагностика и точные команды.
    """
    board = load_board()
    task = find_task(board, args.task)
    safe_print(f"CHECK: {task['id']}  [{task['status']}]")
    verdicts = {"READY": [], "PARTIAL": [], "ORPHANED": [], "PENDING": []}
    for s in task["subtasks"]:
        if s["status"] in SUB_TERMINAL:
            continue
        marker = read_marker(task["id"], s["id"])
        if marker and marker["status"] == "DONE":
            verdict = "READY"
        elif marker:
            verdict = "PARTIAL"
        elif s.get("started"):
            verdict = "ORPHANED"
        else:
            verdict = "PENDING"
        verdicts[verdict].append(s)
        safe_print()
        safe_print(f"  {s['id']:<4} {verdict:<9} [{s['status']}] {s['title']}")
        if s.get("target"):
            safe_print(f"       target: {s['target']} (scope: {s['scope']})")
        if marker:
            safe_print(f"       маркер: {marker['path']} "
                       f"(STATUS: {marker['status']})")
            for line in marker["head"][:6]:
                safe_print(f"         | {line}")
        if verdict == "READY":
            safe_print(f"       -> готово на диске. Закрыть: "
                       f"python tools/task_board.py done {task['id']} {s['id']}")
        elif verdict == "PARTIAL":
            if s.get("session"):
                safe_print(f"       -> продолжи СУБАГЕНТА сессии "
                           f"{s['session']} (инструмент продолжения субагента, "
                           f"sessionID={s['session']}): приказ - «Продолжай "
                           f"задачу {s['id']}; дочитай маркер {marker['path']} "
                           f"и закрой ОСТАЛОСЬ».")
            else:
                safe_print("       -> session не записан: перезапусти по "
                           "промпту (см. next) с приказом «доделай по "
                           f"маркеру {marker['path']}».")
        elif verdict == "ORPHANED":
            if s.get("session"):
                safe_print(f"       -> обрыв без маркера. Продолжи субагента "
                           f"сессии {s['session']} (sessionID={s['session']}) "
                           f"приказом: «Продолжай задачу {s['id']}; если "
                           f"работа утеряна - перечитай задание и выполни, "
                           f"маркер обязательно запиши».")
            else:
                safe_print("       -> обрыв без маркера и session: перезапусти "
                           "по промпту (см. next) с ПРОТОКОЛОМ ЗАВЕРШЕНИЯ.")
        else:
            safe_print("       -> ещё не запускалась: см. next.")
    safe_print()
    total_ready = len(verdicts["READY"])
    safe_print(f"ИТОГ: READY {total_ready}, PARTIAL {len(verdicts['PARTIAL'])}, "
               f"ORPHANED {len(verdicts['ORPHANED'])}, "
               f"PENDING {len(verdicts['PENDING'])}")
    if total_ready:
        safe_print(f"Закрыть готовые: python tools/task_board.py done "
                   f"{task['id']} <sub>")
    if verdicts["PARTIAL"] or verdicts["ORPHANED"]:
        safe_print("Продолжение/перезапуск обязателен до перехода к новым "
                   "подзадачам (task-orchestrator, раздел обрыва).")
    return 0


def cmd_verify(args) -> int:
    """Проверка заявленного результата закрытых подзадач по артефактам."""
    board = load_board()
    task = find_task(board, args.task)
    bad = 0
    checked = 0
    for s in task["subtasks"]:
        if s["status"] not in (SUB_DONE, SUB_RUNNING):
            continue
        checked += 1
        problems = verify_sub(s, task["id"])
        if problems:
            bad += 1
            safe_print(f"  {s['id']:<4} FAIL  [{s['status']}] {s['title']}")
            for p in problems:
                safe_print(f"       - {p}")
        else:
            safe_print(f"  {s['id']:<4} OK    [{s['status']}] {s['title']}")
    safe_print()
    safe_print(f"VERIFY {task['id']}: проверено {checked}, с проблемами {bad}")
    if bad:
        safe_print("Проблемы verify - повод НЕ считать подзадачу готовой: "
                   "перепроверь или верни в running.")
        return 1
    return 0


def cmd_close(args) -> int:
    board = load_board()
    task = find_task(board, args.task)
    open_subs = [s for s in task["subtasks"]
                 if s["status"] not in (SUB_DONE, SUB_SKIPPED)]
    if open_subs and not args.force:
        ids = ", ".join(f"{s['id']}({s['status']})" for s in open_subs)
        safe_print(f"ERROR: незакрытые подзадачи: {ids}")
        safe_print("Сначала check -> done/fail/skip; закрыть принудительно "
                   "можно флагом --force.")
        return 2
    task["status"] = TASK_CLOSED
    task["closed"] = now_iso()
    save_board(board)
    safe_print(f"CLOSED: {task['id']} at {task['closed']}")
    safe_print("Не забудь: обнови reports/translation_plan.md и сделай запись "
               "в reports/log.md; коммит - по правилам AGENTS.md.")
    return 0


def cmd_contract(args) -> int:
    """Печать готового ПРОТОКОЛА ЗАВЕРШЕНИЯ для задания субагента.

    Ведущий агент генерирует промпт, запускает субагента и прикладывает
    к заданию дословный вывод этой команды (маркер уже привязан к
    конкретной подзадаче доски).
    """
    board = load_board()
    task = find_task(board, args.task)
    s = find_sub(task, args.sub)
    safe_print(work_contract(task["id"], s["id"]))
    return 0


def cmd_subtasks(args) -> int:
    """Добавить декомпозицию списком из stdin (по одной команде sub-add)."""
    safe_print("Используй sub-add по одной подзадаче - доска маленькая, "
               "а поштучная запись не теряется при обрыве.")
    return 2


# ============================================================================
# СВОДКА task_board.md
# ============================================================================
def cmd_sync(args) -> int:
    board = load_board()
    lines = [
        "# Доска задач оркестратора (генерируется: "
        "python tools/task_board.py sync)",
        "",
        "Состояние ведётся в `reports/task_board.json`; эта сводка — "
        "зеркало для человека.",
        "",
    ]
    for t in board["tasks"]:
        done = sum(1 for s in t["subtasks"] if s["status"] in (SUB_DONE, SUB_SKIPPED))
        lines.append(f"## {t['id']} — [{t['status']}] "
                     f"(закрыто {done} из {len(t['subtasks'])})")
        lines.append("")
        lines.append(f"* Запрос: {t['request']}")
        if t.get("target"):
            lines.append(f"* Цель: `{t['target']}`")
        lines.append(f"* Создана: {t['created']}")
        if t.get("closed"):
            lines.append(f"* Закрыта: {t['closed']}")
        lines.append("")
        if t["subtasks"]:
            lines.append("| # | статус | режим | цель | заголовок |")
            lines.append("|---|---|---|---|---|")
            for s in t["subtasks"]:
                box = {SUB_PENDING: "[ ]", SUB_RUNNING: "[~]",
                       SUB_DONE: "[x]", SUB_FAILED: "[!]",
                       SUB_SKIPPED: "[-]"}.get(s["status"], "[?]")
                lines.append(
                    f"| {s['id']} | {box} {s['status']} | "
                    f"`{s.get('prompt') or 'manual'}` | "
                    f"`{s.get('target') or '-'}` | {s['title']} |")
            lines.append("")
    MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    safe_print(f"SYNC: {rel(MD_PATH)} (задач: {len(board['tasks'])})")
    return 0


# ============================================================================
# CLI
# ============================================================================
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="task_board.py",
        description="Доска задач оркестратора ZnT1 (reports/task_board.json).")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("new", help="создать задачу свободной формы")
    sp.add_argument("--request", required=True,
                    help="текст запроса пользователя (кириллица допустима)")
    sp.add_argument("--target", default=None,
                    help="цель по форме targets: 4 | 4_6 | script-ch4_6.rpy | extra")
    sp.set_defaults(func=cmd_new)

    sp = sub.add_parser("sub-add", help="добавить подзадачу")
    sp.add_argument("task", help="id задачи (T...); можно единственную открытую")
    sp.add_argument("--prompt", default=None,
                    help="id промпта agent_workflow.py (port-part, full-audit, ...)")
    sp.add_argument("--manual", default=None,
                    help="текстовая подзадача без промпта")
    sp.add_argument("--target", default=None,
                    help="цель подзадачи (по умолчанию - цель задачи)")
    sp.add_argument("--scope", choices=("part", "chapter"), default="part",
                    help="охват: part (по умолчанию) | chapter (вся глава)")
    sp.add_argument("--title", default=None,
                    help="короткий заголовок для status/next")
    sp.set_defaults(func=cmd_sub_add)

    sp = sub.add_parser("status", help="показать состояние доски")
    sp.add_argument("task", nargs="?", default=None)
    sp.set_defaults(func=cmd_status)

    sp = sub.add_parser("next", help="следующая подзадача с точными командами")
    sp.add_argument("task", nargs="?", default=None)
    sp.set_defaults(func=cmd_next)

    sp = sub.add_parser("start", help="пометить подзадачу запущенной")
    sp.add_argument("task")
    sp.add_argument("sub")
    sp.add_argument("--session", default=None,
                    help="sessionID субагента (для продолжения после обрыва)")
    sp.set_defaults(func=cmd_start)

    sp = sub.add_parser("done", help="закрыть подзадачу как выполненную")
    sp.add_argument("task")
    sp.add_argument("sub")
    sp.add_argument("--note", default=None)
    sp.add_argument("--evidence", nargs="*", default=None,
                    help="rel-пути артефактов-доказательств")
    sp.set_defaults(func=cmd_done)

    sp = sub.add_parser("fail", help="закрыть подзадачу как проваленную")
    sp.add_argument("task")
    sp.add_argument("sub")
    sp.add_argument("--note", default="")
    sp.set_defaults(func=cmd_fail)

    sp = sub.add_parser("skip", help="пропустить подзадачу")
    sp.add_argument("task")
    sp.add_argument("sub")
    sp.add_argument("--note", default="")
    sp.set_defaults(func=cmd_skip)

    sp = sub.add_parser(
        "check",
        help="ДИАГНОСТИКА обрыва: READY / PARTIAL / ORPHANED / PENDING")
    sp.add_argument("task", nargs="?", default=None)
    sp.set_defaults(func=cmd_check)

    sp = sub.add_parser(
        "verify",
        help="сверить done/running-подзадачи с артефактами на диске")
    sp.add_argument("task", nargs="?", default=None)
    sp.set_defaults(func=cmd_verify)

    sp = sub.add_parser("close", help="закрыть задачу")
    sp.add_argument("task", nargs="?", default=None)
    sp.add_argument("--force", action="store_true",
                    help="закрыть, несмотря на незакрытые подзадачи")
    sp.set_defaults(func=cmd_close)

    sp = sub.add_parser(
        "contract",
        help="печать ПРОТОКОЛА ЗАВЕРШЕНИЯ (приписка к заданию субагента)")
    sp.add_argument("task")
    sp.add_argument("sub")
    sp.set_defaults(func=cmd_contract)

    sp = sub.add_parser("sync", help="перегенерировать reports/task_board.md")
    sp.set_defaults(func=cmd_sync)
    return p


def main(argv: list[str] | None = None) -> int:
    ensure_safe_output()
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
