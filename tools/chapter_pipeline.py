#!/usr/bin/env python3
"""
Пошаговый pipeline проверки главы для проекта ZnT1.

Отображает фазы проверки с галочками (как в agent_workflow.py):
- Механические проверки (синтаксис, типографика, заглушки, ассеты)
- Проверка английского перевода (EN)
- Проверка русского перевода (RU)
- Финальная сводка

Учитывает:
- Неполные главы (можно проверять на любом этапе)
- Повторные проверки (инкрементальность — показывает что изменилось)
- Кэширование результатов (не проверяет то, что уже проверено)

Запуск:
    python tools/chapter_pipeline.py [--chapter N] [--phase P] [--reset]
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
from typing import List, Optional, Dict, Tuple

sys.path.insert(0, str(Path(__file__).parent))
from output_util import ensure_safe_output  # noqa: E402


# ============================================================================
# КОНСТАНТЫ
# ============================================================================

ROOT = Path(__file__).parent.parent
PIPELINE_STATE_FILE = ROOT / "reports" / "pipeline_state.json"

# Фазы pipeline
PHASES = [
    ("syntax", "Синтаксис Ren'Py", "check_renpy_syntax.py"),
    ("typography_ru", "Типографика RU", "check_typography.py --lang ru"),
    ("typography_en", "Типографика EN", "check_typography.py --lang en"),
    ("placeholders", "Заглушки", "check_placeholders.py"),
    ("assets", "Ассеты", "check_assets.py"),
    ("voice", "Озвучка", "check_voice_transcriptions.py"),
    ("en_translation", "Перевод EN", "prompts/check_en_translation.md"),
    ("ru_translation", "Перевод RU", "prompts/check_ru_translation.md"),
    ("summary", "Финальная сводка", None),
]


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
    chapter: int
    phase_results: Dict[str, PhaseResult] = field(default_factory=dict)
    last_run: Optional[str] = None
    file_hashes: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "chapter": self.chapter,
            "phase_results": {k: v.to_dict() for k, v in self.phase_results.items()},
            "last_run": self.last_run,
            "file_hashes": self.file_hashes,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "PipelineState":
        state = cls(chapter=data["chapter"])
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
        print("\033[2J\033[H", end="")


def compute_file_hash(filepath: Path) -> str:
    """Вычислить хеш файла."""
    try:
        content = filepath.read_bytes()
        return hashlib.md5(content).hexdigest()
    except OSError:
        return ""


def get_chapter_files(chapter: int) -> List[Path]:
    """Получить список файлов главы."""
    chapter_dir = ROOT / "game" / "chapters" / str(chapter)
    if not chapter_dir.exists():
        return []
    return sorted(chapter_dir.glob("*.rpy"))


def get_tl_files(lang: str) -> List[Path]:
    """Получить список файлов переводов."""
    tl_dir = ROOT / "game" / "tl" / lang
    if not tl_dir.exists():
        return []
    return sorted(tl_dir.rglob("*.rpy"))


def load_state() -> Dict[int, PipelineState]:
    """Загрузить состояние pipeline."""
    if not PIPELINE_STATE_FILE.exists():
        return {}
    try:
        with open(PIPELINE_STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {int(k): PipelineState.from_dict(v) for k, v in data.items()}
    except (json.JSONDecodeError, KeyError):
        return {}


def save_state(states: Dict[int, PipelineState]) -> None:
    """Сохранить состояние pipeline."""
    PIPELINE_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PIPELINE_STATE_FILE, "w", encoding="utf-8") as f:
        json.dump({str(k): v.to_dict() for k, v in states.items()}, f, ensure_ascii=False, indent=2)


# ============================================================================
# ВЫПОЛНЕНИЕ ФАЗ
# ============================================================================

def run_mechanical_phase(phase_name: str, script: str, chapter: int) -> PhaseResult:
    """Запустить механическую фазу."""
    result = PhaseResult(name=phase_name, title=dict((p[0], p[1]) for p in PHASES)[phase_name])
    result.status = "running"
    result.timestamp = datetime.now().isoformat()

    # Формируем команду (скрипты пишут UTF-8 отчёты в reports/)
    cmd = [sys.executable, str(ROOT / "tools" / script.split()[0])]
    if "--lang" in script:
        cmd.extend(["--lang", script.split("--lang")[1].strip()])
    cmd.extend(["--chapter", str(chapter)])

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
        result.details["stdout"] = (process.stdout or "")[:8000]
        result.details["stderr"] = (process.stderr or "")[:2000]
        result.details["returncode"] = process.returncode

    except Exception as e:
        result.status = "error"
        result.message = str(e)

    return result


def run_translation_phase(phase_name: str, prompt_file: str, chapter: int) -> PhaseResult:
    """Фазу перевода выполняет агент (LLM) — здесь только отображение."""
    result = PhaseResult(name=phase_name, title=dict((p[0], p[1]) for p in PHASES)[phase_name])
    result.status = "pending"
    result.message = f"Требуется ручная проверка: {prompt_file}"
    return result


def run_summary_phase(chapter: int, state: PipelineState) -> PhaseResult:
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

def print_pipeline_header(chapter: int) -> None:
    print()
    separator("=")
    print(f"  Pipeline проверки главы {chapter}")
    separator("=")
    print()


def print_phase_status(state: PipelineState, current_phase: Optional[str] = None) -> None:
    """Вывести статус всех фаз."""
    print()
    for i, (name, title, _) in enumerate(PHASES, 1):
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

def run_pipeline(chapter: int, start_phase: Optional[str] = None, reset: bool = False) -> None:
    """Запустить pipeline."""
    states = load_state()
    state = states.get(chapter, PipelineState(chapter=chapter))

    if reset:
        state = PipelineState(chapter=chapter)

    # Проверяем изменение файлов
    chapter_files = get_chapter_files(chapter)
    current_hashes = {str(f): compute_file_hash(f) for f in chapter_files}
    files_changed = current_hashes != state.file_hashes

    if files_changed and not reset:
        print()
        print("  [!] Файлы главы изменились с момента последней проверки.")
        print("      Рекомендуется повторить механические проверки.")
        print()

    state.file_hashes = current_hashes

    # Определяем с какой фазы начать
    phase_names = [p[0] for p in PHASES]
    start_idx = 0
    if start_phase and start_phase in phase_names:
        start_idx = phase_names.index(start_phase)

    # Выводим статус
    print_pipeline_header(chapter)
    print_phase_status(state)

    # Выполняем фазы
    for i in range(start_idx, len(PHASES)):
        name, title, script = PHASES[i]

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

        if script is None:
            # Финальная сводка
            result = run_summary_phase(chapter, state)
        elif name in ("en_translation", "ru_translation"):
            # Фазы перевода — выполняет агент (LLM)/редактор по промпту
            result = run_translation_phase(name, script, chapter)
            print(f"  Требуется ручная проверка по промпту:")
            print(f"  {script}")
            print()
            interactive = False
            if sys.stdin.isatty():
                try:
                    input("  Нажмите Enter после выполнения проверки...")
                    interactive = True
                except (EOFError, KeyboardInterrupt):
                    interactive = False
            if interactive:
                result.status = "done"
                result.message = "Выполнено вручную"
            else:
                # Неинтерактивный запуск: фаза остаётся pending, не блокирует остальные
                result.status = "pending"
                result.message = f"Ожидает ручной проверки: {script}"
                print("  Неинтерактивный запуск — фаза осталась pending.")
                print("  Повторный запуск с терминала отметит её выполненной.")
                states[chapter] = state
                state.phase_results[name] = result
                save_state(states)
                continue
        else:
            # Механические фазы
            result = run_mechanical_phase(name, script, chapter)
            print_phase_details(result)

        state.phase_results[name] = result
        state.last_run = datetime.now().isoformat()

        # Сохраняем состояние
        states[chapter] = state
        save_state(states)

        # Обновляем отображение
        clear_screen()
        print_pipeline_header(chapter)
        print_phase_status(state, name)

    # Финальная сводка
    print()
    separator("=")
    print("  Pipeline завершён")
    separator("=")
    print()
    print_phase_status(state)
    print()


def main() -> int:
    ensure_safe_output()
    parser = argparse.ArgumentParser(description="Pipeline проверки главы")
    parser.add_argument("--chapter", "-c", type=int, required=True, help="Номер главы")
    parser.add_argument("--phase", "-p", choices=[p[0] for p in PHASES],
                        help="Начать с фазы")
    parser.add_argument("--reset", action="store_true", help="Сбросить состояние")
    parser.add_argument("--status", action="store_true", help="Только показать статус")
    args = parser.parse_args()

    if args.status:
        states = load_state()
        state = states.get(args.chapter, PipelineState(chapter=args.chapter))
        print_pipeline_header(args.chapter)
        print_phase_status(state)
        return 0

    run_pipeline(args.chapter, args.phase, args.reset)
    return 0


if __name__ == "__main__":
    sys.exit(main())
