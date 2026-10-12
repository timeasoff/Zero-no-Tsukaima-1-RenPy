#!/usr/bin/env python3
"""
Пошаговый pipeline проверки главы/части/файла для проекта ZnT1.

Отображает фазы проверки с галочками (как в agent_workflow.py):
- Механические проверки (синтаксис, типографика, заглушки, ассеты, голоса)
- Детерминированный Omission Pre-check (evidence для аудиторов)
- Слои агента (задания tools/agent_workflow.py): перевод/редактура,
  независимый аудит A/B/C, Analyzer (2 фазы), humanizer, грамматика, стиль
- Финальная сводка

Цель (--chapter) — гибкая, см. tools/targets.py:
    2                          — вся глава (папка game/chapters/2/)
    extra                      — вся папка extra (sp_l1.rpy)
    0                          — пролог (script-ch0.rpy)
    2_4b                       — часть 4b главы 2 (script-ch2_4b.rpy)
    2_4                        — часть 4 главы 2 (script-ch2_4.rpy)
    2_5*                       — все части с префиксом 5
    script-ch2_5b.rpy          — полное имя файла (по всем папкам глав)
    sp_l1 / sp_l1.rpy          — файл в extra
    game/chapters/2/script-ch2_4b.rpy — путь от корня проекта

Учитывает:
- Неполные главы (можно проверять на любом этапе)
- Повторные проверки (инкрементальность — показывает что изменилось)
- Кэширование результатов (не проверяет то, что уже проверено)
- Состояние ключится по разрешённой цели (key), файлы — по MD5 цели

Запуск:
    python tools/chapter_pipeline.py --chapter 2
    python tools/chapter_pipeline.py --chapter 2_4b
    python tools/chapter_pipeline.py --chapter script-ch2_5b.rpy
    python tools/chapter_pipeline.py --chapter sp_l1
    python tools/chapter_pipeline.py --chapter extra
    python tools/chapter_pipeline.py --chapter 2 [--phase P] [--reset] [--status]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

sys.path.insert(0, str(Path(__file__).parent))
from output_util import ensure_safe_output, safe_print  # noqa: E402
from targets import resolve_target, TargetError, ResolvedTarget  # noqa: E402


# ============================================================================
# КОНСТАНТЫ
# ============================================================================

ROOT = Path(__file__).parent.parent
PIPELINE_STATE_FILE = ROOT / "reports" / "pipeline_state.json"

# Фазы pipeline: (имя, заголовок, источник, стиль охвата)
#   источник: "<tool>.py [args]"  — механический инструмент проекта;
#             "agent:<prompt_id>" — задание слоя агента (tools/agent_workflow.py);
#             None                — только финальная сводка.
#   стиль:    "target"  — инструменту передаётся --chapter <исходная цель>
#                         (инструменты на tools/targets.py);
#             "chapter" — инструменту передаётся --chapter <номер главы>;
#             "project" — без --chapter (инструмент работает по всему проекту).
PHASES = [
    # 1. Механические проверки
    ("syntax", "Синтаксис Ren'Py", "check_renpy_syntax.py", "target"),
    ("typography_ru", "Типографика RU", "check_typography.py --lang ru", "target"),
    ("typography_en", "Типографика EN", "check_typography.py --lang en", "target"),
    ("placeholders", "Заглушки", "check_placeholders.py", "target"),
    ("assets", "Ассеты", "check_assets.py", "target"),
    ("voice", "Озвучка", "check_voice_transcriptions.py", "target"),
    ("check_project", "Проверка проекта", "check_project.py", "chapter"),
    ("audio", "Озвучка: сверка", "media/audio_converter.py check", "project"),
    # 2. Детерминированное evidence (технический слой, НЕ аудитор)
    ("precheck", "Omission Pre-check", "omission_precheck.py", "target"),
    # 3. Слои агента (задания tools/agent_workflow.py; pipeline только ведёт)
    ("translation", "Перевод / редактура", "agent:translate-edit", None),
    ("semantic_audit_a", "Семантический аудит A", "agent:semantic-audit-a", None),
    ("pragmatic_c", "Прагматический аудит C", "agent:pragmatic-c", None),
    ("analyzer_phase1", "Analyzer: Фаза 1 (blind)", "agent:analyzer-phase1", None),
    ("analyzer_phase2", "Analyzer: Фаза 2 (evidence)", "agent:analyzer-phase2", None),
    ("humanizer", "Humanizer", "agent:humanizer", None),
    ("grammar", "Грамматический контроль", "agent:grammar-audit", None),
    ("style", "Стилевой аудит", "agent:style-audit", None),
    # 4. Итог
    ("summary", "Финальная сводка", None, None),
]

PHASE_TITLES = {p[0]: p[1] for p in PHASES}


@dataclass
class PhaseResult:
    name: str
    title: str
    status: str = "pending"  # pending / running / done / error / skipped
    message: str = ""
    timestamp: Optional[str] = None
    duration: Optional[float] = None
    details: Dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "title": self.title,
            "status": self.status,
            "message": self.message,
            "timestamp": self.timestamp,
            "duration": self.duration,
            "details": self.details,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "PhaseResult":
        return cls(**data)


@dataclass
class PipelineState:
    target: str = ""
    phase_results: Dict[str, PhaseResult] = field(default_factory=dict)
    last_run: Optional[str] = None
    file_hashes: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "target": self.target,
            "phase_results": {k: v.to_dict() for k, v in self.phase_results.items()},
            "last_run": self.last_run,
            "file_hashes": self.file_hashes,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "PipelineState":
        # Поле называлось chapter до перехода на строковые цели — принимаем оба.
        tgt = data.get("target")
        if tgt is None:
            tgt = str(data.get("chapter") or "")
        state = cls(target=tgt)
        state.phase_results = {
            k: PhaseResult.from_dict(v) for k, v in data.get("phase_results", {}).items()
        }
        state.last_run = data.get("last_run")
        state.file_hashes = data.get("file_hashes", {})
        return state


# ============================================================================
# УТИЛИТЫ
# ============================================================================

def separator(char: str = "-", width: int = 60) -> None:
    print(char * width)


def clear_screen() -> None:
    if not sys.stdout.isatty():
        return
    if sys.platform == "win32":
        os.system("cls")
    else:
        print("\033[2J\033[1;1H", end="")


def compute_file_hash(filepath: Path) -> str:
    """Вычислить хеш файла."""
    try:
        content = filepath.read_bytes()
        return hashlib.md5(content).hexdigest()
    except OSError:
        return ""


def load_state() -> Dict[str, PipelineState]:
    """Загрузить состояние pipeline (ключи — строковые цели)."""
    if not PIPELINE_STATE_FILE.exists():
        return {}
    try:
        with open(PIPELINE_STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {str(k): PipelineState.from_dict(v) for k, v in data.items()}
    except (json.JSONDecodeError, KeyError, TypeError):
        return {}


def save_state(states: Dict[str, PipelineState]) -> None:
    """Сохранить состояние pipeline."""
    PIPELINE_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PIPELINE_STATE_FILE, "w", encoding="utf-8") as f:
        json.dump({str(k): v.to_dict() for k, v in states.items()},
                  f, ensure_ascii=False, indent=2)


def file_list_line(target: ResolvedTarget) -> str:
    """Строка со списком файлов цели (ASCII)."""
    files = [f.relative_to(ROOT).as_posix() for f in target.files]
    if not files:
        return "(no .rpy files)"
    shown = ", ".join(files[:8])
    if len(files) > 8:
        shown += f", ... ({len(files)} total)"
    return shown


# ============================================================================
# ВЫПОЛНЕНИЕ ФАЗ
# ============================================================================

def run_mechanical_phase(phase_name: str, source: str, style: str,
                         target_raw: str, target: ResolvedTarget) -> PhaseResult:
    """Запустить механическую фазу.

    source — "<tool>.py [args]"; --chapter передаётся по style:
      "target"  — исходная цель пользователя (инструменты на tools/targets.py);
      "chapter" — номер главы (check_project: принимает только int);
      "project" — без --chapter.
    """
    result = PhaseResult(name=phase_name, title=PHASE_TITLES[phase_name])
    result.status = "running"
    result.timestamp = datetime.now().isoformat()

    parts = source.split()
    cmd = [sys.executable, str(ROOT / "tools" / parts[0])] + parts[1:]

    if style == "target":
        cmd += ["--chapter", target_raw]
    elif style == "chapter":
        name = target.chapter_dir.name
        if name.isdigit():
            cmd += ["--chapter", name]
        else:
            result.status = "skipped"
            result.message = (
                "check_project принимает только номер главы — "
                "для extra/prologue фаза пропущена")
            return result
    # style == "project": без --chapter

    try:
        process = subprocess.run(
            cmd,
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        result.duration = None  # Можно добавить замер времени

        if process.returncode == 0:
            result.status = "done"
            result.message = "OK"
        else:
            result.status = "error"
            result.message = process.stdout[:500] if process.stdout else "Ошибка"

        # Сохраняем детали (обрезаем, чтобы state не разрастался)
        result.details["cmd"] = " ".join(cmd)
        result.details["stdout"] = (process.stdout or "")[:8000]
        result.details["stderr"] = (process.stderr or "")[:2000]
        result.details["returncode"] = process.returncode

    except Exception as e:
        result.status = "error"
        result.message = str(e)

    return result


def run_agent_phase(phase_name: str, prompt_id: str) -> PhaseResult:
    """Фаза слоя агента: pipeline только ведёт её (задание — agent_workflow.py)."""
    result = PhaseResult(name=phase_name, title=PHASE_TITLES[phase_name])
    result.status = "pending"
    result.details["workflow_prompt"] = prompt_id
    result.message = (
        "Задание агента: python tools/agent_workflow.py (промпт: %s)" % prompt_id)
    return result


def run_summary_phase(state: PipelineState) -> PhaseResult:
    """Финальная сводка."""
    result = PhaseResult(name="summary", title="Финальная сводка")
    result.status = "done"

    total = len(PHASES) - 1  # Без самой сводки
    done = sum(1 for p in state.phase_results.values() if p.status == "done")
    errors = sum(1 for p in state.phase_results.values() if p.status == "error")

    result.message = f"Выполнено {done}/{total} фаз, ошибок: {errors}"
    result.details["total"] = total
    result.details["done"] = done
    result.details["errors"] = errors

    return result


# ============================================================================
# ОТОБРАЖЕНИЕ
# ============================================================================

def print_pipeline_header(target: ResolvedTarget) -> None:
    print()
    separator("=")
    print(f"  Pipeline проверки: {target.label}")
    print(f"  Файлы ({len(target.files)}): {file_list_line(target)}")
    separator("=")
    print()


def print_phase_status(state: PipelineState, current_phase: Optional[str] = None) -> None:
    """Вывести статус всех фаз."""
    print()
    for i, (name, title, _src, _style) in enumerate(PHASES, 1):
        result = state.phase_results.get(name)
        if result:
            if result.status == "done":
                marker = "[x]"
            elif result.status == "error":
                marker = "[!]"
            elif result.status == "running":
                marker = "[>]"
            else:
                marker = "[ ]"
            status = result.message[:40] if result.message else ""
        else:
            marker = "[ ]"
            status = ""

        current = " ->" if name == current_phase else "   "
        print(f"  {current} {i:2d}. {marker} {title}")
        if status:
            print(f"           {status}")
    print()


def print_phase_details(result: PhaseResult) -> None:
    """Вывести детали фазы."""
    print()
    separator("=")
    print(f"  Фаза: {result.title}")
    separator("=")
    print()

    if result.details.get("stdout"):
        print(result.details["stdout"])

    if result.details.get("stderr"):
        print("STDERR:")
        print(result.details["stderr"])

    print()
    print(f"  Статус: {result.status}")
    print(f"  Сообщение: {result.message}")
    print()


# ============================================================================
# ОСНОВНОЙ ЦИКЛ
# ============================================================================

def run_pipeline(target_raw: str, start_phase: Optional[str] = None,
                 reset: bool = False) -> int:
    """Запустить pipeline по цели. Возвращает код выхода."""
    try:
        target = resolve_target(ROOT, target_raw)
    except TargetError as e:
        safe_print(f"ERROR: {e}")
        return 1

    key = target.key
    states = load_state()
    state = states.get(key, PipelineState(target=key))

    if reset:
        state = PipelineState(target=key)

    # Проверяем изменение файлов ЦЕЛИ (часть/файл/глава)
    current_hashes = {str(f): compute_file_hash(f) for f in target.files}
    files_changed = current_hashes != state.file_hashes

    if files_changed and not reset:
        print()
        print("  [!] Файлы цели изменились с момента последней проверки.")
        print("      Рекомендуется повторить механические проверки.")
        print()

    state.file_hashes = current_hashes

    # Определяем с какой фазы начать
    phase_names = [p[0] for p in PHASES]
    start_idx = 0
    if start_phase and start_phase in phase_names:
        start_idx = phase_names.index(start_phase)

    # Выводим статус
    print_pipeline_header(target)
    print_phase_status(state)

    # Выполняем фазы
    for i in range(start_idx, len(PHASES)):
        name, title, source, style = PHASES[i]

        # Пропускаем уже выполненные фазы (если файлы не менялись)
        if not files_changed and not reset:
            existing = state.phase_results.get(name)
            if existing and existing.status == "done":
                print(f"  Пропуск: {title} (уже выполнено)")
                continue

        print()
        separator()
        print(f"  Выполнение: {title}")
        separator()
        print()

        if name == "summary":
            # Финальная сводка
            result = run_summary_phase(state)
        elif source and source.startswith("agent:"):
            # Слой агента: pipeline только ведёт фазу, задание — agent_workflow.py
            prompt_id = source[len("agent:"):]
            result = run_agent_phase(name, prompt_id)
            run_hint = f"python tools/agent_workflow.py (промпт: {prompt_id})"
            print(f"  Задание агента: {run_hint}")
            print()
            interactive = False
            if sys.stdin.isatty():
                try:
                    input("  Нажмите Enter после выполнения...")
                    interactive = True
                except (EOFError, KeyboardInterrupt):
                    interactive = False
            if interactive:
                result.status = "done"
                result.message = "Выполнено вручную"
            else:
                # Неинтерактивный запуск: фаза остаётся pending, не блокирует остальные
                result.status = "pending"
                result.message = f"Ожидает ручного выполнения: {run_hint}"
                print("  Неинтерактивный запуск — фаза осталась pending.")
                print("  Повторный запуск с терминала отметит её выполненной.")
                states[key] = state
                state.phase_results[name] = result
                save_state(states)
                continue
        else:
            # Механическая фаза: --chapter передаётся по style (target/chapter/project)
            result = run_mechanical_phase(name, source, style, target_raw, target)
            print_phase_details(result)

        state.phase_results[name] = result
        state.last_run = datetime.now().isoformat()

        # Сохраняем состояние
        states[key] = state
        save_state(states)

        # Обновляем отображение
        clear_screen()
        print_pipeline_header(target)
        print_phase_status(state, name)

    # Финальная сводка
    print()
    separator("=")
    print("  Pipeline завершён")
    separator("=")
    print()
    print_phase_status(state)
    print()
    return 0


def main() -> int:
    ensure_safe_output()
    parser = argparse.ArgumentParser(description="Pipeline проверки главы/части/файла")
    parser.add_argument("--chapter", "-c", required=True,
                        help="Цель: 2 | extra | 0 | 2_4b | 2_5* | "
                             "script-ch2_5b.rpy | sp_l1 | путь от корня")
    parser.add_argument("--phase", "-p", choices=[p[0] for p in PHASES],
                        help="Начать с фазы")
    parser.add_argument("--reset", action="store_true", help="Сбросить состояние")
    parser.add_argument("--status", action="store_true", help="Только показать статус")
    args = parser.parse_args()

    if args.status:
        try:
            target = resolve_target(ROOT, args.chapter)
        except TargetError as e:
            safe_print(f"ERROR: {e}")
            return 1
        states = load_state()
        state = states.get(target.key, PipelineState(target=target.key))
        print_pipeline_header(target)
        print_phase_status(state)
        return 0

    return run_pipeline(args.chapter, args.phase, args.reset)


if __name__ == "__main__":
    sys.exit(main())