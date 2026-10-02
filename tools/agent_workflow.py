#!/usr/bin/env python3
"""
Оркестратор рабочего процесса AI-агента проекта ZnT1
(The Familiar Zero - Unofficial Remaster: порт сценария PS2 в Ren'Py + перевод EN/RU).

Внутри два независимых раздела:
PROMPTS - LLM-промпты (PromptInfo): генерация готового задания агенту,
  копирование в буфер обмена и сохранение в agent_prompt.md (корень
  проекта; файл в .gitignore, перезаписывается при каждой генерации);
ACTIONS - детерминированные действия оркестратора (ActionInfo): запускают
  реальные инструменты проекта и НЕ создают LLM-промптов.

Единица работы - часть главы: game/chapters/<N>/script-ch<N>_<M>.rpy
(главы 0...28; глава extra со sp_*.rpy структуры "часть" не имеет и
оркестратором не ведётся).

Основные возможности:
- выбор режима через числовой ввод в консоли;
- выбор главы и части; навигация: следующая/предыдущая часть, следующая глава;
- централизованный контекст проекта (пути, иерархия JA > EN / JA > RU,
  обязательные документы, git, кодировка);
- режимы: первый запуск главы, продолжение, порт части, перевод/редактура,
  голоса, полный аудит, грамматика, стиль, humanizer, решения пользователя,
  прагматический аудит C, Analyzer (две фазы), проверка кодировки;
- SMA (независимый аудит): reports/sma/ch<N>/<part>/{a,b,c,precheck,analysis}/,
  результат - .md-файл с JSON-блоком, уникальный run_id на каждый запуск;
- копирование промпта в буфер (base64 -> PowerShell) и сохранение в файл;
- неинтерактивный режим: --list, --prompt <id> --chapter N --part M,
  --action <id> --chapter N --part M, --self-test-sma (dry-run).

КОНСОЛЬ: PowerShell здесь cp1251. Японский текст в print()/input() не попадает
(см. say()); тексты промптов выводятся только в файл и в буфер обмена.
Кириллица печатается нормально - её не избегают.

Запускать из корня проекта:
python tools/agent_workflow.py
"""
from __future__ import annotations

import base64
import glob as globlib
import json
import os
import re
import subprocess
import sys
import textwrap
import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Callable

# ============================================================================
# КОНСТАНТЫ
# ============================================================================
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TERMINAL_WIDTH = 78

# Готовый промпт-инструкция сохраняется в корне проекта под этим именем
# (строка добавлена в .gitignore, перезаписывается при каждой генерации).
PROMPT_FILE_NAME = "agent_prompt.md"
PROMPT_FILE = os.path.join(ROOT, PROMPT_FILE_NAME)

# Границы глав проекта (папки game/chapters/0 ... game/chapters/28).
PROJECT_CHAPTER_MIN = 0
PROJECT_CHAPTER_MAX = 28

# Плоские бакеты tl/ (AGENTS.md, раздел 6).
TL_LANGS = ("japanese", "russian")
TL_BUCKETS = ("dialogs", "thoughs", "choises", "common",
              "overlays", "characters", "options", "screens")

# Реальные инструменты проекта (tools/).
CHECK_TOOL = os.path.join("tools", "check_project.py")
IMAGE_MAP_TOOL = os.path.join("tools", "build_image_id_map.py")
BG_TOOL = os.path.join("tools", "replace_bg_placeholders.py")
IMAGE_MAP_CSV = os.path.join("references", "image_id_map.csv")
PS2_TO_RENPY_CSV = os.path.join("references", "ps2_to_renpy.csv")
STATS_FILE = os.path.join(ROOT, "ps2_source", "chapter_stats.json")

# ============================================================================
# УТИЛИТЫ ВЫВОДА
# ============================================================================
def say(text: str = "") -> None:
    """Печать одной строки без риска UnicodeEncodeError.

    Консоль PowerShell здесь cp1251: символы, которых нет в кодировке
    (японский и прочие), заменяются на '?' ТОЛЬКО в самом выводе - в файлы
    и в буфер обмена текст попадает нетронутым. Unicode-стрелка приводится
    к ASCII "->" ради читаемости консоли.
    """
    if not text:
        print()
        return
    text = text.replace("\u2192", "->")
    enc = getattr(sys.stdout, "encoding", None) or "utf-8"
    try:
        text.encode(enc)
    except (UnicodeEncodeError, LookupError):
        text = text.encode(enc, errors="replace").decode(enc, errors="replace")
    print(text)


def separator(char: str = "-", width: int = TERMINAL_WIDTH) -> None:
    """Вывести разделитель."""
    say(char * width)


def print_wrapped(
    text: str,
    width: int = TERMINAL_WIDTH,
    indent: str = "",
) -> None:
    """Вывести текст с автоматическим переносом строк."""
    if not text:
        say()
        return
    for line in text.splitlines():
        if not line.strip():
            say()
            continue
        wrapped = textwrap.wrap(
            line,
            width=max(20, width - len(indent)),
            break_long_words=False,
            break_on_hyphens=False,
        )
        if not wrapped:
            say()
            continue
        for part in wrapped:
            say(indent + part)


# ============================================================================
# МОДЕЛЬ: ГЛАВА + ЧАСТЬ
# ============================================================================
@dataclass
class Chapter:
    """Глава проекта (0...28) и её часть - единица работы оркестратора.

    Идентификаторы:
      chapter_id = ch<N>            (ch3)
      part_id    = ch<N> для части 1, ch<N>_<M> для части M > 1 (ch3, ch3_2)
    part_id совпадает с именем лейбла Ren'Py этой части и с именем каталога
    в reports/ и reports/sma/.
    """
    chapter: int
    part: int = 1

    # --- идентификаторы ---
    @property
    def chapter_id(self) -> str:
        return f"ch{self.chapter}"

    @property
    def part_id(self) -> str:
        return self.chapter_id if self.part == 1 else f"{self.chapter_id}_{self.part}"

    @property
    def label(self) -> str:
        """Лейбл Ren'Py этой части (ch<N>, ch<N>_2, ...)."""
        return self.part_id

    @property
    def source_chapter_number(self) -> int:
        """Номер главы в ps2_source: проектная N -> источник N+1."""
        return self.chapter + 1

    @property
    def stats_key(self) -> str:
        """Ключ проектной главы в ps2_source/chapter_stats.json."""
        return str(self.source_chapter_number)

    # --- файлы части ---
    @property
    def script_file_name(self) -> str:
        # Пролог (глава 0) - одна часть, файл без номера части.
        if self.chapter == 0:
            return "script-ch0.rpy"
        return f"script-ch{self.chapter}_{self.part}.rpy"

    @property
    def script_rel(self) -> str:
        return f"game/chapters/{self.chapter}/{self.script_file_name}"

    @property
    def script_path(self) -> str:
        return os.path.join(ROOT, "game", "chapters", str(self.chapter),
                            self.script_file_name)

    @property
    def script_exists(self) -> bool:
        return os.path.isfile(self.script_path)

    @property
    def exists_text(self) -> str:
        return "да" if self.script_exists else "нет"

    @property
    def report_rel(self) -> str:
        return f"reports/{self.chapter_id}/{self.part_id}.md"

    @property
    def report_path(self) -> str:
        return os.path.join(ROOT, "reports", self.chapter_id, f"{self.part_id}.md")

    @property
    def report_exists(self) -> bool:
        return os.path.isfile(self.report_path)

    @property
    def log_rel(self) -> str:
        return "reports/log.md"

    @property
    def log_path(self) -> str:
        return os.path.join(ROOT, "reports", "log.md")

    # --- источники JA (только глобы: японские имена в командные строки
    #     и в консоль не передаются) ---
    @property
    def source_chapter_glob(self) -> str:
        return (f"ps2_source/chapters/"
                f"chapter_{self.source_chapter_number:02d}_*.txt")

    @property
    def source_events_glob(self) -> str:
        return (f"ps2_source/events_full/"
                f"chapter_{self.source_chapter_number:02d}_*.txt")

    # --- переводные файлы (оба языка, плоские бакеты) ---
    @property
    def tl_paths(self) -> dict[str, dict[str, str]]:
        """lang -> bucket -> абсолютный путь (japanese и russian)."""
        return {
            lang: {b: os.path.join(ROOT, "game", "tl", lang, f"{b}.rpy")
                   for b in TL_BUCKETS}
            for lang in TL_LANGS
        }

    # --- каталоги SMA (независимый аудит) ---
    @property
    def sma_rel(self) -> str:
        return f"reports/sma/{self.chapter_id}/{self.part_id}"

    def sma_dir(self, kind: str) -> str:
        return os.path.join(ROOT, "reports", "sma", self.chapter_id,
                            self.part_id, kind)

    # --- служебное ---
    def describe(self) -> str:
        """Краткая строка состояния части для консоли (ASCII + кириллица)."""
        return (f"{self.part_id}  (глава {self.chapter}, часть {self.part}; "
                f"скрипт: {self.exists_text})")


def tl_display() -> str:
    """Краткое описание tl-путей для промптов (без длинного перечисления)."""
    return (f"game/tl/<lang>/<bucket>.rpy  (lang: {', '.join(TL_LANGS)}; "
            f"bucket: {', '.join(TL_BUCKETS)})")


# ============================================================================
# ВВОД И НАВИГАЦИЯ
# ============================================================================
def ask_int(prompt: str, minimum: int = 0, maximum: int | None = None) -> int:
    """Запросить целое число в допустимом диапазоне."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            say("  Введите целое число.")
            continue
        if value < minimum or (maximum is not None and value > maximum):
            limit = f"до {maximum}" if maximum is not None else "больше"
            say(f"  Число должно быть не меньше {minimum} и {limit}.")
            continue
        return value


def ask_chapter() -> Chapter:
    """Выбрать главу и часть."""
    say()
    say("Выбор части")
    separator()
    say()
    chapter = ask_int(f"  Номер главы ({PROJECT_CHAPTER_MIN}.."
                      f"{PROJECT_CHAPTER_MAX}): ",
                      PROJECT_CHAPTER_MIN, PROJECT_CHAPTER_MAX)
    part = ask_int("  Номер части (с 1): ", 1)
    ch = Chapter(chapter, part)
    say()
    say(f"  Текущая часть: {ch.describe()}")
    say(f"  Отчёт: {ch.report_rel} ({'есть' if ch.report_exists else 'нет'})")
    return ch


def navigate_next_part(ch: Chapter) -> Chapter:
    """Следующая часть той же главы."""
    return Chapter(ch.chapter, ch.part + 1)


def navigate_prev_part(ch: Chapter) -> Chapter | None:
    """Предыдущая часть той же главы (None - уже первая)."""
    if ch.part <= 1:
        return None
    return Chapter(ch.chapter, ch.part - 1)


def navigate_next_chapter(ch: Chapter) -> Chapter | None:
    """Первая часть следующей главы (None - последняя глава проекта)."""
    if ch.chapter >= PROJECT_CHAPTER_MAX:
        return None
    return Chapter(ch.chapter + 1, 1)


# ============================================================================
# ИНВЕНТАРЬ ЧАСТИ (подсчёт строк и реплик; вместо старого инвентаря блоков)
# ============================================================================
def part_inventory(ch: Chapter) -> dict:
    """Подсчёт строк/реплик части: скрипт (строки, voice, menu, jump, label).

    Ничего не пишет и не изменяет; используется в контексте промптов SMA,
    чтобы у аудитора/анализатора была численная картина части.
    """
    info = {
        "exists": ch.script_exists,
        "lines": 0,
        "nonempty": 0,
        "voice": 0,
        "menu": 0,
        "jump": 0,
        "labels": 0,
        "strings": 0,
    }
    if not ch.script_exists:
        return info
    try:
        with open(ch.script_path, encoding="utf-8", errors="replace") as fh:
            lines = fh.read().splitlines()
    except OSError:
        return info
    info["lines"] = len(lines)
    voice_re = re.compile(r'^\s*voice\s+"')
    str_re = re.compile(r'"(?:[^"\\]|\\.)*"')
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        info["nonempty"] += 1
        if voice_re.match(raw):
            info["voice"] += 1
        if line == "menu:" or (line.endswith(":") and line.startswith("menu")):
            info["menu"] += 1
        if line.startswith("jump "):
            info["jump"] += 1
        if line.startswith("label "):
            info["labels"] += 1
        if str_re.search(raw):
            info["strings"] += 1
    return info


def inventory_text(inv: dict) -> str:
    """Человекочитаемая строка инвентаря части (без японского)."""
    if not inv.get("exists"):
        return "файл части ещё не создан"
    return (f"строк: {inv['lines']} (непустых: {inv['nonempty']}), "
            f"строк со звуком: {inv['voice']}, строк с текстом: {inv['strings']}, "
            f"menu: {inv['menu']}, jump: {inv['jump']}, label: {inv['labels']}")


# ============================================================================
# КОНТЕКСТ ПРОЕКТА
# ============================================================================
def project_context(ch: Chapter) -> str:
    """Общий контекст, добавляемый в каждый промпт."""
    return f"""
КОНТЕКСТ ПРОЕКТА ZnT1
Проект: The Familiar Zero - Unofficial Remaster (PS2 -> Ren'Py + перевод EN/RU)
Корень проекта:
{ROOT}

ЕДИНИЦА РАБОТЫ - часть главы (итерация; три файла пишутся синхронно):
  {ch.script_rel}
  game/tl/japanese/<bucket>.rpy
  game/tl/russian/<bucket>.rpy
Лейблы части: {ch.label}
Файл существует: {ch.exists_text}
Отчёт части: {ch.report_rel}
Журнал решений: {ch.log_rel}
Бакеты tl (плоские): {', '.join(TL_BUCKETS)}

ИСТОЧНИК JA (КАНОН), проектная глава {ch.chapter} = источник {ch.source_chapter_number}:
  {ch.source_chapter_glob}            (реплики и события в порядке источника)
  {ch.source_events_glob}             (точные аргументы set/next/selectItem/dateItem)
  ps2_source/chapter_stats.json       (ключ "{ch.stats_key}")
Глобы даны без японских имён: в командные строки и в вывод консоли передавай
только глобы, никогда - полные японские имена файлов.

ПРОВЕРКИ, СПРАВОЧНИКИ И ГЛАВНЫЕ ФАЙЛЫ:
  python tools/check_project.py       -> reports/check_project.md (E1-E8, W1-W5, I1)
  {PS2_TO_RENPY_CSV}   (карта событий PS2 -> Ren'Py)
  {IMAGE_MAP_CSV}  (справочник image id; заполняется пользователем)
  dictionary.md      (канон имён, названий, терминов, заклинаний)
  addresses.md       (формы обращений к персонажам)
  game/PROMTS.md     (правила перевода: 3 варианта, "-сан", троеточие, кавычки)
  transcriptions_ja_ru.csv, game/audio/voices/, game/characters.rpy  (голоса)

ОБЯЗАТЕЛЬНЫЕ ДОКУМЕНТЫ (читай перед работой и применяй при любых решениях):
  AGENTS.md - раздел 3 (единица работы и резка), 4 (порядок работы),
    5 (правила, жизненный цикл сигнала, неопределённость), 6 (инфраструктура),
    7 (скиллы и порядок слоёв), 8 (отчёты), 9 (чек-лист приёмки части).
  dictionary.md, addresses.md, game/PROMTS.md.
  Скиллы: .agents/skills/<name>/SKILL.md (названия - в AGENTS.md, раздел 7).

ИЕРАРХИЯ ИСТОЧНИКОВ
JA - канон (authoritative source of truth): ps2_source/chapters/*.txt.
EN - база сценария; готового эталонного EN НЕТ, EN пишем мы из JA прямо
     в .rpy. RU - перевод из JA в game/tl/russian.
JA > EN и JA > RU при любом конфликте. Ни EN, ни RU не являются
доказательством исходного смысла, даже если написаны этой же сессией.
Совпадение RU с EN само по себе доказательством не является.
Расхождение EN <-> RU не решается молча: обе формы сверяются по JA; неверна
одна из форм - правится эта форма; сомнение - флаг и запись в журнал.

GIT
git commit ЗАПРЕЩЁН без явного подтверждения пользователя на конкретный набор
изменений. Успешные проверки, "сохранить прогресс" и это задание подтверждением
не являются. Можно только предложить коммит (сообщение + перечень изменений).

КОДИРОВКА И КАНАЛ ТЕКСТА
Консоль PowerShell здесь cp1251. Японский текст НИКОГДА не передавай в аргументы
командной строк и не пиши в print()/input() - это UnicodeEncodeError. Пути с
японскими именами передавай глобом (см. выше). Длинный или японский текст сначала
пиши в UTF-8 файл инструментом записи, а команде передавай только путь.
Кириллица печатается нормально - её не избегай.

ЗАПРЕТЫ
Промежуточных каталогов и служебных файлов-копий текста не создавай: единица
записи - файлы проекта (script-*.rpy, оба tl/, reports/*, журнал).
Существующее не переписывай без нужды; работа идёт добавлением.
Модальность реплики неприкосновенна. Обнаружение сигнала - не вердикт:
каждый кандидат получает classification и disposition (AGENTS.md, раздел 5).
UNCERTAINTY != STOP: локальные и средние неопределённости решай сам
(PROVISIONAL + запись в {ch.log_rel} + продолжение); блокирующая - останови
минимальный участок и задай ровно один вопрос.
""".strip()


# ============================================================================
# SMA (НЕЗАВИСИМЫЙ АУДИТ): ID, ПУТИ, КОНТЕКСТ
# ============================================================================
# Архитектура: изолированные аудиторские сессии кладут evidence в
#   reports/sma/ch<N>/<part>/{a,b,c,precheck}/,
# а двухфазный Analyzer читает всё evidence и пишет свой результат в
#   reports/sma/ch<N>/<part>/analysis/.
# Скиллы независимых аудиторов A и B, а также скилл сквозной переводческой
# сверки отключены системой: задания для них здесь НЕ генерируются (их evidence
# появляется от внешних изолированных сессий). Оркестратор ведёт только
# прагматический аудит C и Analyzer.
SMA_REL_ROOT = "reports/sma"
SMA_KINDS = ("a", "b", "c", "analysis")   # каталоги результатов внутри части
SMA_PRECHECK_KIND = "precheck"            # детерминированное evidence (не аудитор)
SMA_EXT = "md"                            # формат: .md c JSON-блоком
_SMA_ISSUED_IDS: set[str] = set()         # гарантия уникальности в процессе

# Формулировки изоляции (используются и в промптах, и в self-test).
SMA_AUTONOMY_NOTE = (
    "РАБОТАЙ АВТОНОМНО. Все данные для аудита приведены в этом задании. "
    "Не перечисляй содержимое каталогов и не открывай никакие файлы, кроме "
    "перечисленных в задании; единственное исключение - OWN SKILL, если он "
    "явно указан в задании (это инструкции самого аудитора, а не чужие "
    "результаты)."
)
SMA_OWN_FILE_NOTE = (
    "Единственный файл, который ты создаёшь, - результат этого запуска "
    "(см. OUTPUT FILE). Любые другие файлы в каталоге части в задание не "
    "входят: не читай их, не сравнивай с ними свой результат и не делай "
    "выводов из их наличия или отсутствия."
)
SMA_FORBIDDEN_INPUTS_NOTE = (
    "ЗАПРЕЩЁННЫЕ ВХОДЫ (не читай и не используй, даже если попадутся): "
    "чужие evidence-каталоги этой части (a/, b/, c/, precheck/, analysis/), "
    "отчёты частей, reports/log.md, результаты и findings других запусков. "
    "Если такой материал оказался в задании - не используй его и сообщи "
    "об ошибке генерации."
)

# Иерархия источников для промптов C и Analyzer ОБЕИХ фаз.
SMA_SOURCE_HIERARCHY_NOTE = (
    "ИЕРАРХИЯ ИСТОЧНИКОВ (SOURCE PRIORITY)\n"
    "JA - authoritative source of truth (авторитетный источник истины):\n"
    "     ps2_source/chapters/*.txt; точные аргументы событий - ps2_source/events_full/*.txt.\n"
    "RU - text under review (проверяемый перевод): game/tl/russian/<bucket>.rpy.\n"
    "EN - reference only (справочная база сценария, НЕ источник смысла):\n"
    "     game/chapters/<N>/script-*.rpy - наш собственный текст, готового\n"
    "     эталонного EN нет.\n"
    "Основная проверка - JA -> RU. Не EN -> RU и не JA -> EN -> RU: EN не\n"
    "является промежуточным эталоном перевода.\n"
    "JA has priority over EN (JA > EN) и JA > RU при любом конфликте:\n"
    "конфликтующую с JA интерпретацию EN игнорируй.\n"
    "EN must not be treated as authority.\n"
    "Совпадение RU с EN само по себе не является доказательством правильности\n"
    "перевода. Конфликтный случай JA = X, EN = Y, RU = Y: вывод «RU корректен,\n"
    "потому что совпадает с EN» запрещён - оценивай соответствие RU японскому\n"
    "оригиналу (JA -> RU)."
)


def sma_chapter_rel(ch: Chapter) -> str:
    """Каталог части SMA относительно корня проекта (прямые слэши)."""
    return f"{SMA_REL_ROOT}/{ch.chapter_id}/{ch.part_id}"


def sma_chapter_dir(ch: Chapter, kind: str) -> str:
    """Абсолютный путь каталога одного типа результатов этой части."""
    return ch.sma_dir(kind)


def sma_result_rel_path(ch: Chapter, kind: str, run_id: str) -> str:
    """Путь результата относительно корня проекта (прямые слэши)."""
    return f"{sma_chapter_rel(ch)}/{kind}/{run_id}.{SMA_EXT}"


def sma_result_abs_path(ch: Chapter, kind: str, run_id: str) -> str:
    """Абсолютный путь файла результата (kind: a / b / c / analysis)."""
    return os.path.join(sma_chapter_dir(ch, kind), f"{run_id}.{SMA_EXT}")


def _sma_run_id_taken(ch: Chapter, run_id: str) -> bool:
    """True, если идентификатор запуска уже занят файлом результата."""
    for kind in SMA_KINDS:
        folder = sma_chapter_dir(ch, kind)
        if os.path.exists(os.path.join(folder, f"{run_id}.{SMA_EXT}")):
            return True
        if os.path.exists(os.path.join(folder, f"{run_id}.phase1.{SMA_EXT}")):
            return True
    return False


def new_audit_run_id(ch: Chapter | None = None) -> str:
    """Уникальный идентификатор запуска: YYYYMMDD-HHMMSS-xxxx.

    Генерируется при создании промпта, поэтому повторные запуски не
    перезаписывают предыдущие результаты: каждый запуск пишет свой файл.
    Номер вручную увеличивать не нужно.
    """
    while True:
        run_id = f"{datetime.now():%Y%m%d-%H%M%S}-{uuid.uuid4().hex[:4]}"
        if run_id in _SMA_ISSUED_IDS:
            continue
        if ch is not None and _sma_run_id_taken(ch, run_id):
            continue
        _SMA_ISSUED_IDS.add(run_id)
        return run_id


def sma_existing_runs(ch: Chapter, kind: str) -> list[str]:
    """Существующие run_id результатов одного типа (без слепых Фазы 1).

    Используется Analyzer'ом: он учитывает ВСЕ существующие запуски (механизма
    ручного выбора отдельных run_id нет). Ничего не создаёт и не изменяет.
    """
    folder = sma_chapter_dir(ch, kind)
    if not os.path.isdir(folder):
        return []
    ids = [os.path.splitext(name)[0] for name in os.listdir(folder)
           if name.lower().endswith(f".{SMA_EXT}")
           and not name.lower().endswith(f".phase1.{SMA_EXT}")]
    return sorted(ids)


def sma_existing_phase1_runs(ch: Chapter) -> list[str]:
    """Существующие слепые выводы Фазы 1 (analysis/<id>.phase1.md)."""
    folder = sma_chapter_dir(ch, "analysis")
    if not os.path.isdir(folder):
        return []
    return sorted(os.path.splitext(os.path.splitext(name)[0])[0]
                  for name in os.listdir(folder)
                  if name.lower().endswith(f".phase1.{SMA_EXT}"))


def sma_existing_precheck(ch: Chapter) -> list[str]:
    """Существующие evidence детерминированного pre-check (precheck/*.md)."""
    folder = sma_chapter_dir(ch, SMA_PRECHECK_KIND)
    if not os.path.isdir(folder):
        return []
    return sorted(os.path.splitext(name)[0] for name in os.listdir(folder)
                  if name.lower().endswith(f".{SMA_EXT}"))


def sma_phase1_rel_path(ch: Chapter, phase1_id: str) -> str:
    """Путь слепого вывода Фазы 1 (её собственный результат, не evidence)."""
    return f"{sma_chapter_rel(ch)}/analysis/{phase1_id}.phase1.{SMA_EXT}"


def sma_phase1_abs_path(ch: Chapter, phase1_id: str) -> str:
    return os.path.join(sma_chapter_dir(ch, "analysis"),
                        f"{phase1_id}.phase1.{SMA_EXT}")


def semantic_audit_context(ch: Chapter) -> str:
    """Минимальный контекст для прагматического аудита C и Analyzer.

    В отличие от project_context не раскрываются журнал, чек-листы и
    прочие пути: аудитору нужны только источник JA, EN-строки сценария,
    RU-бакеты, соседний контекст и численная картина части.
    """
    inv = part_inventory(ch)
    return f"""КОНТЕКСТ АУДИТА ЧАСТИ
Проект: ZnT1. Часть: {ch.part_id} (глава {ch.chapter}, часть {ch.part}).
Сценарий (EN-база, соседние реплики, номера строк): {ch.script_rel}
Японский источник (JA - канон): {ch.source_chapter_glob}
Точные аргументы событий: {ch.source_events_glob}
Русский перевод (RU - предмет проверки): {tl_display()}
Японские пары к EN-строкам: game/tl/japanese/<bucket>.rpy
Соседние реплики этой же части - ТОЛЬКО как контекст.
Численная картина части: {inventory_text(inv)}.
Единица проверки - реплика/строка части в порядке сценария. Находка
относится только к той реплике, в которой найдена. Соседние реплики нужны
исключительно для понимания контекста.
Материал задания ограничен перечисленным выше; никакие другие материалы,
каталоги и прошлые результаты в задание не входят."""

# ============================================================================
# ПРОМПТЫ: ТИПЫ ДАННЫХ
# ============================================================================
@dataclass
class PromptInfo:
    """Один режим LLM-промпта (id - стабильный ключ для --prompt)."""
    id: str
    title: str
    description: str
    guide: str
    generator: Callable[[Chapter], str] | None = None


@dataclass
class ActionInfo:
    """Техническое действие оркестратора (НЕ LLM-промпт).

    В отличие от PromptInfo действие не генерирует задание для агента, а
    выполняет детерминированный шаг проекта: ``execute`` получает текущую
    часть и возвращает код завершения процесса (0 - успех).

    ActionInfo НЕ наследуется от PromptInfo и НЕ входит в PROMPTS.
    """
    id: str
    name: str
    description: str
    execute: Callable[[Chapter], int]


# ============================================================================
# ПРОМПТЫ: РАБОЧИЕ РЕЖИМЫ ПОРТА
# ============================================================================
def prompt_first_launch(ch: Chapter) -> str:
    return f"""
{project_context(ch)}
РЕЖИМ: ПЕРВЫЙ ЗАПУСК ГЛАВЫ {ch.chapter_id}
Подготовь среду для главы {ch.chapter_id} и сразу начни работу над её
первой частью. Пользователь уже поручил обработать эту главу - это разрешение
на выполнение; отдельного подтверждения «начинать ли?» не требуется.
ПОДГОТОВИТЕЛЬНЫЙ ЭТАП (выполни в ЭТОМ же запуске, без остановки):
1. Прочитай AGENTS.md целиком (разделы 3, 4, 5, 7, 8, 9).
2. Прочитай скиллы ps2-source, project-constraints, renpy-remaster-api,
   project-checks; перечитай dictionary.md, addresses.md, game/PROMTS.md.
3. Прочитай ВСЮ главу источника: {ch.source_chapter_glob} целиком, затем
   {ch.source_events_glob} (точные set/next/selectItem/dateItem);
   статистика - ps2_source/chapter_stats.json (ключ "{ch.stats_key}").
4. Определи структуру главы: локации, переходы "next scene", ветки
   (перемещение/выбор/свидания), сцены, уводящие в extra scenes.
5. Разрежь главу на части по AGENTS.md, раздел 3: целевой размер
   115 +/- 25 голосовых на часть, резать только на СИЛЬНОЙ границе,
   окно 90...140, не раньше 90; имена файлов и лейблов детерминированы
   (script-ch<N>_<M>.rpy; лейблы ch<N>, ch<N>_2, ...), концы частей связать
   jump, последняя часть главы заканчивается jump attention.
6. Прогони python tools/check_project.py и зафиксируй базовое состояние
   (в отчёте первой части укажи, что проверка прогнана до начала работы).
7. Для первой части определи границы, события, реплики, [voice N], BGM и фоны.
И СРАЗУ ПЕРЕХОДИ К ИСПОЛНЕНИЮ: портируй первую часть по режиму
«Порт части» (события -> voice -> реплика EN -> menu/choice -> jump,
параллельно old/new в оба tl), затем python tools/check_project.py
и отчёт {f'reports/{ch.chapter_id}/{ch.chapter_id}.md'}.
После успешной подготовки НЕ останавливайся и НЕ проси разрешения начать:
ANALYSIS -> CLASSIFICATION -> PROVISIONAL RESOLUTION -> EXECUTION.
Неопределённости: UNCERTAINTY != STOP; локальные и средние решай сам:
обоснованная форма + пометка PROVISIONAL + запись в {ch.log_rel} + продолжение
(PROVISIONAL != CANONICAL, PROVISIONAL != WAIT); новый PROVISIONAL-термин
обязательно укажи в отчёте части. Действительно блокирующая неопределённость -
останови минимальный участок и задай ровно один вопрос.
Запрещено в этом режиме: спрашивать «начинать ли / продолжать ли»,
возвращать только план, завершаться после подготовки, ждать следующего
сообщения пользователя.
""".strip()


def prompt_continue(ch: Chapter) -> str:
    return f"""
{project_context(ch)}
РЕЖИМ: ПРОДОЛЖЕНИЕ РАБОТЫ НАД ЧАСТЬЮ {ch.part_id}
Продолжи работу над частью {ch.part_id} с её текущего состояния.
Сначала проверь (без переспрашивания):
- AGENTS.md (разделы 4, 5, 9) и скиллы ps2-source, renpy-remaster-api,
  tl-en-ru, project-checks;
- сам файл части {ch.script_rel} (что уже портировано, где обрыв);
- оба tl-бакета: какие строки уже получили old/new;
- отчёт части {ch.report_rel}, если он есть;
- журнал {ch.log_rel} и отчёт автопроверки reports/check_project.md;
- состояние источника {ch.source_chapter_glob} (сколько части осталось).
Определи следующий незакрытый этап обычного порядка (события *_fx -> voice ->
реплика EN -> menu/choice -> jump + параллельные old/new в оба tl) и выполни
его до конца в этом запуске: не повторяй уже сделанное, не переписывай
работающее без нужды, но и не останавливайся на «плане».
После записи файлов - самопроверка (self-review), python tools/check_project.py,
дописка отчёта части и журнальных записей по необходимости.
Ничего не удаляй молча; расхождения JA <-> EN <-> RU фиксируй в журнале.
""".strip()


def prompt_port_part(ch: Chapter) -> str:
    return f"""
{project_context(ch)}
РЕЖИМ: ПОРТ ЧАСТИ {ch.part_id}
Цель: превратить границы части в готовый скрипт и обе переводные пары.
0. Перечитай AGENTS.md, раздел 4 (порядок работы), и скиллы ps2-source,
   renpy-remaster-api, tl-en-ru, voice-workflow, assets, project-checks.
1. Границы и содержимое части бери ТОЛЬКО из источника:
   {ch.source_chapter_glob} (порядок реплик и событий) и
   {ch.source_events_glob} (точные аргументы). Ни один вызов не переносится
   «на глазок».
2. Портируй по порядку:
   a) события -> игровые вызовы: [BG]/[EVENT_CG] -> фон/CG-событие,
      [SPRITE] -> show_sprites, [BGM play=+K] -> t{{K-1}} (никогда по
      названию!), [SE] -> точечный перенос по assets, [LAYER] -> flash_fx
      или переход по образцу глав 0/1; соответствие - references/ps2_to_renpy.csv
      и скилл renpy-remaster-api; образцы - game/chapters/0 и game/chapters/1;
   b) title-карточки -> call overlay_screen(...) с новым уникальным K;
   c) voice: [voice N] -> id -> .STV -> .ogg -> имя -> строка voice "..."
      (скилл voice-workflow; имя - по номеру части: часть 1 - ch<N>_<spk>_<NNN>.ogg,
      части 2+ - ch<N>.<M>_<spk>_<NNN>.ogg);
   d) реплика EN: пишется из JA прямо в .rpy (готового EN нет); правила -
      game/PROMTS.md и скилл tl-en-ru; мысли остаются мыслями, реплики -
      репликами;
   e) menu / *_choice (portrait_choice, sprite_choice), симпатия -
      update_sympathy(N, char_key="...");
   f) jump: конец части -> jump ch<N>_<M+1>; конец главы -> jump attention.
   Нереализуемые вызовы (movie, coffee, waitAction, waitSEStop, waitLoad, sync,
   create, setZoom, msgon/msgoff, beginSkip/endSkip и прочие из AGENTS.md,
   раздел 6) НЕ переносятся - одна строка в отчёте части, без повторного
   разбора на каждой главе.
3. Параллельно с каждой новой EN-строкой добавляй old/new в ОБА tl:
   game/tl/japanese/<bucket>.rpy и game/tl/russian/<bucket>.rpy.
   old - дословная строка сценария (переносы склеены); new - перевод;
   бакет - по типу строки; JA-мысли в японских скобках.
4. Перед записью каждой строки - self-review (галлюцинации, пропуски,
   искажение смысла); термины сверяй с dictionary.md, обращения - с addresses.md.
5. Запись - только файлами проекта (скилл save-progress): порция части целиком
   (script + оба tl), без промежуточных каталогов.
6. После записи - python tools/check_project.py: ошибки E1-E8/W1-W5/I1 по
   своей части исправляй, не откладывая; итог - reports/check_project.md.
7. Отчёт части: {ch.report_rel} по шаблону AGENTS.md, раздел 8
   (источники и границы -> соответствие сцен -> неперенесённые вызовы ->
   голоса -> перевод EN/RU -> PROVISIONAL/??? -> чек-лист раздела 9).
Запреты контекста (git, кодировка, промежуточные каталоги) действуют полностью.
""".strip()


def prompt_translate_edit(ch: Chapter) -> str:
    return f"""
{project_context(ch)}
РЕЖИМ: ПЕРЕВОД / РЕДАКТУРА EN <-> RU ЧАСТИ {ch.part_id}
Вход: {ch.script_rel} (EN-база, написанная нами из JA) + оба tl; готового
эталонного EN в проекте нет.
1. Определи объём: строки сценария без пары old/new в каждом языке
   (python tools/check_project.py; E4 - нет в japanese, E5 - нет в russian;
   отчёт - reports/check_project.md).
2. Перевод по скиллу tl-en-ru и game/PROMTS.md: old дословно равен строке
   сценария, new - перевод по правилам (варианты, "-сан", троеточие, кавычки,
   мысли), бакеты плоские, оба языка обязательны.
3. Сверка смысла JA -> EN и JA -> RU построчно (JA - арбитр): пропуски,
   добавления, смысловые сдвиги, модальность, местоимения и пол, отрицания,
   время и аспект, эмоциональные оттенки, действия персонажей, соответствие
   обращений addresses.md и терминов dictionary.md.
   Каждый кандидат получает classification (ERROR / WARNING / CANDIDATE / PASS)
   и disposition (FIXED / FALSE POSITIVE / PRESERVED - ... / USER DECISION / ???);
   обнаружение сигнала - повод для проверки, а не разрешение на правку.
4. Правка EN-базы возможна только если по JA неверна именно она; правка RU -
   если по JA неверна RU; расхождение, где обе формы допустимы по JA, - флаг
   RECONCILE в журнал, не молчаливая правка.
5. Оформление русского - russian-prose-rules; после каждой правки строки
   в game/tl/russian - russian-grammar-control; перед каждой записью -
   self-review.
6. Запись - порция части (save-progress); после неё - python
   tools/check_project.py; итог и изменения - в отчёте части и {ch.log_rel}.
Существующее не переписывай без нужды; ноль правок - допустимый итог.
Предпочтение редактора не доказательство ошибки.
""".strip()


def prompt_voice_work(ch: Chapter) -> str:
    return f"""
{project_context(ch)}
РЕЖИМ: ПОРТИРОВАНИЕ ГОЛОСОВ ЧАСТИ {ch.part_id}
Обязательный порядок - скилл voice-workflow (.agents/skills/voice-workflow/SKILL.md).
1. Выпиши все [voice N] этой части из {ch.source_chapter_glob}
   в порядке источника; точные привязки сцен - {ch.source_events_glob}.
2. Для каждого id: файл .STV из архива -> .ogg в game/audio/voices/ ->
   имя по правилу части -> строка voice "имя" в {ch.script_rel}.
   Именование: часть 1 - ch<N>_<spk>_<NNN>.ogg, части 2+ -
   ch<N>.<M>_<spk>_<NNN>.ogg; нумерация по говорящему с 001.
3. Иди по ID, а НЕ по тексту: не подбирай голос «по похожести» и не угадывай
   id по реплике. Использованную строку transcriptions_ja_ru.csv удали или
   пометь как использованную.
4. Говорящие: game/characters.rpy (define + char_data). Нового говорящего
   добавляй только по правилу скилла; идентификатор реплики должен быть
   определён (иначе W4 в проверке).
5. Проверка: python tools/check_project.py - E3 (строка voice без .ogg),
   W2 (.ogg, на которые никто не ссылается), W4 (неизвестный говорящий).
Конвертация STV -> wav выполняется утилитой из архива источника (см. скилл
assets); голоса кладутся сразу в game/audio/voices/, временных папок не создаётся.
Ни один голос не переносится «на глазок»: без подтверждённого id не двигай.
""".strip()


def prompt_full_audit(ch: Chapter) -> str:
    return f"""
{project_context(ch)}
РЕЖИМ: ПОЛНЫЙ АУДИТ ЧАСТИ {ch.part_id}
Проведи полный аудит части по слоям (порядок обязателен):
0. Перечитай AGENTS.md, раздел 5 (жизненный цикл сигнала, неопределённость),
   раздел 8 (отчёт) и раздел 9 (чек-лист); dictionary.md, addresses.md,
   game/PROMTS.md; скилл project-checks.
1. СМЫСЛОВАЯ СВЕРКА JA -> EN и JA -> RU: построчно по {ch.script_rel}
   и русским бакетам против {ch.source_chapter_glob} (аргументы событий -
   {ch.source_events_glob}). Ищи пропуски, добавления, смысловые сдвиги,
   смену субъекта/роли, модальность, время/аспект, отрицания, обращения,
   эмоциональные оттенки. Обратный перевод - диагностический инструмент,
   не арбитр над JA.
2. russian-prose-rules: прямая/косвенная речь, мысли, курсив, тире, кавычки,
   числа, отбивка реплик от наррации.
3. russian-humanizer: канцелярит, кальки с английского, шаблоны, AI-штампы;
   защита от переисправления - references/false-positives.md этого скилла;
   голос персонажей и модальность не «улучшаются».
4. russian-grammar-control: морфология, согласование, управление, падежи,
   актанты и залог - после humanizer и после КАЖДОЙ правки строки в
   game/tl/russian.
5. russian-style-audit: тавтология, повторы, семантическая избыточность,
   неудачные словосочетания, кальки, номинализации, монотонность эпитетов.
6. Перед каждой записью - self-review; запись - порция части (save-progress).
7. python tools/check_project.py -> RESULT: OK (E1-E8, W1-W5, I1), отчёт
   reports/check_project.md; ручные пункты приёмки - скилл project-checks.
8. Итоговый отчёт: {ch.report_rel} по шаблону AGENTS.md, раздел 8; по
   каждому кандидату - classification + disposition; PROVISIONAL/??? - в
   {ch.log_rel}.
Правило правок: обнаружение сигнала не разрешает правку; исправляй только
подтверждённые ошибки; грамматически допустимую форму не меняй ради
«более естественного» варианта; ноль правок - допустимый итог аудита.
git commit запрещён (см. контекст).
""".strip()


def prompt_grammar_audit(ch: Chapter) -> str:
    return f"""
{project_context(ch)}
РЕЖИМ: ГРАММАТИЧЕСКИЙ АУДИТ ЧАСТИ {ch.part_id}
Используй скилл russian-grammar-control (.agents/skills/russian-grammar-control/SKILL.md).
Область: строки game/tl/russian/<bucket>.rpy этой части и соответствующие
EN-строки {ch.script_rel} (для сверки структуры с JA).
Порядок:
1. python tools/check_project.py - механическая рамка (E6 пустой new,
   W1 устаревший old, E4/E5 пропущенные пары).
2. Разбор по предложениям: схема «кто -> что делает -> кого/чего», голос,
   управление, согласование, референция.
3. Проверь: залог и актанты (пассив в JA/EN - сигнал проверки, не ошибка;
   сначала установи синтаксическую структуру), возвратные глаголы, управление
   глаголов, согласование, падежи, местоименные связи, пунктуацию,
   связанную с грамматикой.
Каждый кандидат обязан получить вердикт: ИСПРАВЛЕНО (disposition FIXED,
правка в файл), ОТКЛОНЕНО (FALSE POSITIVE) с обоснованием, PRESERVED - ...
или ??? (решение пользователя). «Звучит по-русски» - не аргумент: разбор
схемы и падежей обязателен.
После каждой правки - повторный грамматический контроль изменённой строки и
python tools/check_project.py; перед записью - self-review.
Не переписывай художественный текст без необходимости; авторский стиль и
смысл сохраняй; ноль исправлений - допустимый итог.
Итог - раздел в отчёте части {ch.report_rel}; спорное - в {ch.log_rel}.
""".strip()


def prompt_style_audit(ch: Chapter) -> str:
    return f"""
{project_context(ch)}
РЕЖИМ: СТИЛЕВОЙ АУДИТ ЧАСТИ {ch.part_id}
Используй скилл russian-style-audit (.agents/skills/russian-style-audit/SKILL.md).
Проверь: тавтологию; повторы и повтор однокоренных слов; семантическую
избыточность; неудачные словосочетания; кальки; избыточные номинализации;
неестественный порядок слов; монотонность эпитетов (один описательный эпитет
слишком часто без синонимов - chapter-level кандидат).
Не дублируй другие слои: смысл JA -> EN/RU - шаг 1 полного аудита; залог и
актанты - russian-grammar-control; оформление речи и мыслей -
russian-prose-rules; канцелярит и AI-штампы - russian-humanizer.
Не убирай нормальную авторскую повторность, если она выполняет
художественную функцию; не превращай текст в стерильный пересказ.
Предпочтение редактора не является доказательством ошибки: нельзя менять
корректный текст ради варианта «красивее / естественнее / без повтора»
(AGENTS.md, раздел 5, жизненный цикл сигнала).
Каждый кандидат получает classification (ERROR / WARNING / CANDIDATE) и
disposition (FIXED / FALSE POSITIVE / PRESERVED - FUNCTIONAL / PRESERVED - JA /
PRESERVED - CHARACTER VOICE / ACCEPTABLE ADAPTATION / USER DECISION / ???);
формулировка «все кандидаты разобраны» без судьбы каждого - нарушение.
Правки - с self-review и python tools/check_project.py после записи;
ноль правок - допустимый итог. Итог - раздел отчёта {ch.report_rel}.
""".strip()


def prompt_humanizer(ch: Chapter) -> str:
    return f"""
{project_context(ch)}
РЕЖИМ: HUMANIZER / MACHINE-LIKE ДЛЯ ЧАСТИ {ch.part_id}
Используй скилл russian-humanizer (.agents/skills/russian-humanizer/SKILL.md,
каталог references/ внутри скилла: patterns, translationese,
kantselyarit-dict, false-positives, style-rules, automation-policy).
Ищи: кальки с английского (главный источник машинности), канцелярит,
шаблонные конструкции, чрезмерно книжные связки, неестественный порядок слов,
повторяющиеся синтаксические схемы, формально правильные, но неживые формулы.
Ограничения этого проекта (перекрывают каталог скилла):
- курсив - разметка по russian-prose-rules, а не «следы Markdown»;
- реплики персонажей - голос персонажа: характер речи не «улучшается»;
- модальные слова и оттенки уверенности правятся только после сверки с JA;
- маркеры риска - сигнал, а не разрешение: автоматически - только
  однозначный низкорисковый мусор (опечатки, технические артефакты,
  нарушение обязательного формата); рискованное - предложить, не навязывать.
После каждой внесённой правки - повторный контроль: self-review, сверка с JA,
терминология (dictionary.md), грамматика (russian-grammar-control),
оформление (russian-prose-rules), затем python tools/check_project.py.
Не делай текст просто «красивее», не меняй смысл, не удаляй намеренную
стилистику, не чини нормальную разговорную речь. Ноль правок - допустимый
итог: humanizer не создаёт stylistic churn.
Итог - раздел отчёта {ch.report_rel}; спорные предложения - в {ch.log_rel}.
""".strip()


def prompt_resolve_decisions(ch: Chapter) -> str:
    return f"""
{project_context(ch)}
РЕЖИМ: РЕШЕНИЯ ПОЛЬЗОВАТЕЛЯ - OPEN / DEFERRED И PROVISIONAL
Пользователь даёт решения по ранее отложенным вопросам (статусы OPEN/DEFERRED
в {ch.log_rel} и в отчётах частей) и/или по временным значениям словаря
(записи PROVISIONAL в dictionary.md и addresses.md). Задача - применить
решение, а не пересказать вопрос: в одном проходе найти ВСЕ места, где
встречается затронутое сомнение или форма, и привести их в соответствие.
Основания: AGENTS.md, раздел 5 - «Жизненный цикл любого сигнала»,
«Неопределённость», PROVISIONAL != CANONICAL
(PROVISIONAL -> USER CONFIRMED -> CANONICAL;
 PROVISIONAL -> REJECTED -> заменить ВСЕ места использования).
1. РАЗОБРАТЬ РЕШЕНИЯ: выпиши каждый пункт отдельно (что разрешено, что
   запрещено, к чему относится: одна часть / вся глава / правило проекта /
   термин словаря). Формулировка двояка - задай ровно один конкретный вопрос
   и до ответа текст не меняй.
2. СОСТАВИТЬ ПОЛНЫЙ СПИСОК ЗАТРОНУТЫХ МЕСТ (решение почти всегда шире одной
   части): script-файлы главы game/chapters/{ch.chapter}/*.rpy, оба tl-языка
   (все бакеты), dictionary.md, addresses.md, отчёты частей
   reports/{ch.chapter_id}/*.md и журнал {ch.log_rel}. Перечисли найденные
   файлы и строки ДО правки.
3. ПРИМЕНИТЬ: единая новая форма во всех найденных местах (REPLACE ALL),
   без «пилотных» частичных правок; правки только файлами проекта, перед
   каждой записью - self-review; если решение подтверждает текущий текст -
   не менять ничего.
4. ОБНОВИТЬ СТАТУСЫ: OPEN/DEFERRED -> RESOLVED (правка внесена) либо CLOSED
   (оставлено как есть, решение явное); dictionary.md: PROVISIONAL ->
   подтверждена (снять пометку, указать «решение пользователя») либо
   отклонена (заменить во всех местах); в {ch.log_rel} - отдельная запись на
   каждый пункт: решение, затронутые файлы, что именно изменено.
5. ПОВТОРНЫЙ КОНТРОЛЬ: после изменений - self-review, сверка с JA,
   russian-grammar-control по изменённым русским строкам, python
   tools/check_project.py; убедись, что незатронутый текст не пострадал и
   что ни одно место с той же формой не пропущено.
Запрещено: закрывать OPEN/DEFERRED без явного решения пользователя; менять
текст «заодно» или по своей инициативе; применять решение только к текущей
части, если оно относится ко всем файлам; записывать неподтверждённую форму
как канон; считать вопрос закрытым без записи в журнале.
""".strip()


def prompt_encoding_check(ch: Chapter) -> str:
    return f"""
{project_context(ch)}
РЕЖИМ: ПРОВЕРКА КОДИРОВКИ И ЦЕЛОСТНОСТИ ФАЙЛОВ ЧАСТИ {ch.part_id}
Проверяемые файлы: {ch.script_rel}, все бакеты game/tl/japanese/*.rpy и
game/tl/russian/*.rpy (участвующие в этой части), при необходимости
{ch.report_rel} и {ch.log_rel}.
Проверь:
- кодировку UTF-8 (без BOM-сюрпризов, без смешения кодировок);
- NUL-байты, управляющие и невидимые символы;
- mojibake и подмену букв на '?' внутри файлов (в консоли '?' - допустимая
  замена, в файлах - повреждение);
- кавычки, тире, многоточия, многоточия внутри реплик;
- парность old/new: каждая строка сценария имеет ровно одну пару на язык,
  new не пуст (E6), старые old без строки в сценарии (W1);
- незакрытый курсив и слитые реплики (W3 - незакрытая кавычка).
Не меняй содержимое без подтверждённой ошибки: находка сначала классифицируется
(ERROR / WARNING / CANDIDATE / PASS), потом решается (disposition), правка -
только после решения, с записью в {ch.log_rel}.
Порядок действий при исправлении: правка файлом -> self-review -> python
tools/check_project.py -> запись в журнал.
Скрипты запускай только с путями без японских имён (глобы из контекста).
""".strip()


# ============================================================================
# ПРОМПТЫ: НЕЗАВИСИМЫЙ АУДИТ (C) И ANALYZER (ДВЕ ФАЗЫ)
# ============================================================================
# Задания для независимых аудиторов A и B здесь НЕ генерируются: их скиллы
# отключены системой (их evidence появляется от внешних изолированных сессий).
# Оркестратор ведёт прагматический аудит C и Analyzer, который читает всё
# evidence из reports/sma/ch<N>/<part>/{a,b,c,precheck}/.
def prompt_pragmatic_c(ch: Chapter) -> str:
    """Prompt ТОЛЬКО для Pragmatic Auditor C (прагматика, речевые акты).

    C - НЕ третий универсальный смысловой аудитор: он закрывает отдельный
    слой смысла - коммуникативный смысл высказывания - и не дублирует ни
    микро-, ни макро-семантику.

    Полностью изолирован: в тексте нет ссылок на других аудиторов, на их
    результаты, на Analyzer и на прошлые отчёты. Аудитор получает свой
    уникальный run_id и единственный выходной файл внутри
    reports/sma/ch<N>/<part>/c/.
    """
    run_id = new_audit_run_id(ch)
    out_rel = sma_result_rel_path(ch, "c", run_id)
    out_abs = sma_result_abs_path(ch, "c", run_id)
    return f"""ЗАДАЧА: независимый прагматический аудит перевода JA -> RU. Ты - Pragmatic Auditor C.

{SMA_AUTONOMY_NOTE}

OWN SKILL (единственный разрешённый файл за пределами задания):
.agents/skills/pragmatic-audit/SKILL.md
{SMA_FORBIDDEN_INPUTS_NOTE}

{semantic_audit_context(ch)}

{SMA_SOURCE_HIERARCHY_NOTE}

ФОКУС AUDITOR C - коммуникативный смысл (прагматика) высказывания:
- что говорящий фактически делает своей репликой (речевой акт): сообщает,
  спрашивает, просит, требует, обещает, предупреждает, разрешает, приказывает,
  отказывает, уклоняется от ответа;
- сохранился ли намёк и сохранилась ли недосказанность: подразумеваемое не
  должно стать прямо сказанным (и наоборот);
- степень уверенности: предположение vs утверждение, сомнение vs уверенность,
  вероятность vs факт;
- форма и сила реплики: просьба vs требование, мягкий vs прямой отказ,
  уклонение vs прямой ответ, разрешение vs приказ, обещание vs намерение;
- установка говорящего: удивление, недоверие, сомнение, ирония, сарказм,
  скрытое отношение;
- смягчение / усиление, изменение коммуникативной силы и категоричности;
- потеря implied meaning или появление подразумеваемого, которого в JA нет.

ОСОБОЕ ВНИМАНИЕ - японским прагматическим конструкциям, частицам и формам,
где словарное содержание передано верно, но меняется ФУНКЦИЯ высказывания
(полный перечень - в разделе «Японские прагматические маркеры» своего SKILL).
Но не своди аудит к списку частиц: важен эффект конструкции на коммуникативный
смысл в конкретном контексте - кто говорит, кому, зачем, после чего и с какой
интонацией.

ГЛАВНЫЙ ВОПРОС ПРОВЕРКИ:
«Сохранился ли в переводе тот же коммуникативный акт и тот же подтекст,
который был в японском?»
Приоритетные кандидаты: намёк -> прямое утверждение; сомнение -> уверенность;
мягкая просьба -> требование; уклонение -> прямой ответ; ирония ->
буквальность; скрытое недовольство -> нейтральная реплика; смягчённый отказ
-> категоричный отказ.

НАПРАВЛЕНИЕ ПРОВЕРКИ: JA -> RU. Сначала установи, что говорящий делает своей
репликой в японском оригинале (и чего он сознательно не договаривает), затем
сверь, сохраняет ли перевод тот же речевой акт, ту же степень уверенности,
ту же силу реплики и тот же подтекст.

ЕДИНИЦА АУДИТА: одна реплика/строка части (TARGET). Соседние реплики
(PREVIOUS, NEXT) даны ТОЛЬКО как контекст; находки относятся только к TARGET.
Если проблема в соседней реплике - не фиксируй её.

ЧТО НЕ ВХОДИТ В ЗАДАЧУ (не проверяй и не фиксируй):
- точность выбора слова, оттенки значения, эмоции, мимика, жесты, интонация -
  микро-семантика;
- субъект/объект, причинно-следственные и временные связи, местоименные
  связи, логика событий, намерение персонажа, идиомы, метафоры -
  макро-семантика и логика;
- грамматика - russian-grammar-control; стиль - russian-style-audit;
  оформление - russian-prose-rules;
- орфография и «можно сказать красивее» - вообще не находка;
- систематический поиск пропусков - это детерминированный слой pre-check
  (evidence в precheck/); если отсутствие реплики непосредственно проявилось
  в твоей обычной проверке - сообщи как issue_type MISSING_TRANSLATION;
- автоматические исправления: ты НИЧЕГО не исправляешь и ничего не пишешь
  в файлы сценария и переводов.

ЖИЗНЕННЫЙ ЦИКЛ СИГНАЛА: ты выполняешь DETECT -> INVESTIGATE -> COMPARE ->
CLASSIFY. DISPOSITION (FIXED / FALSE POSITIVE / PRESERVED - ... / USER DECISION
/ ???) ставит рассматриватель кандидата (Analyzer/редактор), а не ты.
Обнаружение - только «здесь требуется проверка», не разрешение на правку.

ПРОЦЕДУРА:
1. Прочитай свой SKILL (.agents/skills/pragmatic-audit/SKILL.md).
2. Пройди по репликам части в порядке сценария: установи речевой акт JA,
   уверенность, силу и подтекст; свери с переводом.
3. Для каждого расхождения создай находку: aspect + reason + pragmatic_reason
   + confidence + classification.

ФОРМАТ РЕЗУЛЬТАТА: один .md-файл - шапка (роль, часть {ch.part_id}, run_id,
дата, входные строки), краткая сводка и JSON-блок в ```json:
{{
  "audit_id": "sma-c",
  "audit_type": "pragmatic-audit",
  "part": "{ch.part_id}",
  "run_id": "{run_id}",
  "pair": "JA->RU",
  "findings": [
    {{
      "line": 42,
      "source": "точная JA-цитата",
      "current": "точная цитата перевода",
      "pair": "JA->RU",
      "aspect": "Уверенность -> категоричное утверждение",
      "problem": "Изменена коммуникативная сила",
      "reason": "Объяснение расхождения JA -> перевод",
      "pragmatic_reason": "Почему это ИМЕННО прагматическая проблема",
      "issue_type": "PRAGMATIC_SHIFT",
      "confidence": "HIGH",
      "suggestion": "Предложенный вариант",
      "classification": "WARNING"
    }}
  ]
}}

ПРАВИЛА:
- classification: только ERROR / WARNING / CANDIDATE (по реплике без проблем -
  PASS в сводке); confidence: HIGH / MEDIUM / LOW (LOW - только при CANDIDATE).
- line - номер реплики/строки в части (целое, порядок сценария).
- reason объясняет расхождение, pragmatic_reason доказывает, что изменён
  коммуникативный смысл, а не вкусовщина; без pragmatic_reason находка
  недействительна.
- Если проблем нет - "findings": [] и явная сводка «findings: 0».
- source и current - точные цитаты, без пересказа.
- Литературное предпочтение - не ошибка.
- Не выдумывай: нет уверенности - не включай находку.

{SMA_OWN_FILE_NOTE}

OUTPUT FILE (единственный файл этого запуска):
{out_rel}
(абсолютный путь: {out_abs})
Запиши результат строго в описанном формате .md с JSON-блоком. Ничего больше
не создавай и не изменяй."""


def prompt_analyzer_phase1(ch: Chapter) -> str:
    """ФАЗА Analyzer 1 - ПОЛНОСТЬЮ BLIND (только JA + EN + RU + контекст).

    В этот промпт физически НЕ передаются: findings аудиторов, evidence
    pre-check, происхождение (sources), списки запусков и результаты прежних
    анализов. Фаза 1 выносит только предварительное заключение, никаких
    финальных статусов.
    """
    phase1_id = new_audit_run_id(ch)
    out_rel = sma_phase1_rel_path(ch, phase1_id)
    out_abs = sma_phase1_abs_path(ch, phase1_id)
    inv = part_inventory(ch)
    return f"""ЗАДАЧА: смысловой анализатор (Analyzer), ФАЗА 1 - СЛЕПАЯ ПРОВЕРКА.
Часть: {ch.part_id}. Запуск фазы: {phase1_id}.

РОЛЬ
Ты - СМЫСЛОВОЙ АНАЛИЗАТОР, но в Фазе 1 работаешь как чистая независимая
сверка перевода с японским оригиналом. Ты ещё не видел ничьих находок и
ничьих выводов - и не должен их видеть. Фаза 1 обязана быть настоящей
независимой оценкой, а не повтором чужого мнения.

ВХОДНЫЕ ДАННЫЕ ЭТОЙ ФАЗЫ (и БОЛЬШЕ НИЧЕГО)
JA - authoritative source of truth: {ch.source_chapter_glob}
EN - reference only (база сценария): {ch.script_rel}
RU - text under review: {tl_display()}
Контекст соседних реплик: те же файлы части
Численная картина части: {inventory_text(inv)}.
Куда записать свой вывод Фазы 1: {out_rel}

{SMA_SOURCE_HIERARCHY_NOTE}

{SMA_AUTONOMY_NOTE}

ОГРАНИЧЕНИЕ ФАЗЫ 1
Это задание содержит только перечисленные выше данные. Никакие другие
каталоги, evidence, списки запусков и прошлые выводы в него не входят и
открываться не должны. Если тебе передали что-то сверх списка - не
используй это и сообщи об ошибке генерации задания.

После Фазы 1 будет отдельное задание Фазы 2, куда тебе передадут результаты
независимых проверок для сопоставления с твоим первоначальным выводом. Сейчас
об этом не думай: сделай самостоятельную оценку.

ПОРЯДОК РАБОТЫ ФАЗЫ 1 (слепо, по каждой реплике/строке части)
  1) прочитай JA-фрагмент из источника;
  2) прочитай текущую EN-строку сценария и её RU-пару;
  3) прочитай соседние реплики только для контекста;
  4) самостоятельно установи смысл JA;
  5) самостоятельно установи смысл перевода;
  6) ответь по существу:
     - есть ли semantic mismatch и в чём именно;
     - есть ли OMISSION - содержательный фрагмент JA, которому в переводе нет
       никакого соответствия (полный обрыв, частичный обрыв, выпавшая реплика
       или событие);
     - есть ли ДОБАВЛЕННЫЙ смысл - в переводе есть то, чего в JA нет;
     - есть ли другие существенные ошибки.

О МЕТОДЕ ПРОВЕРКИ ПОЛНОТЫ
Отдельный алгоритм поиска пропусков в Фазе 1 НЕ запускается: ты просто
самостоятельно сравниваешь JA и перевод как перевод в целом. Если русский
текст заканчивается раньше японского, последовательность реплик или событий
не покрыта либо фрагмент явно отсутствует - зафиксируй кандидата omission.
«JA длиннее перевода» само по себе пропуском НЕ является: сжатие, слияние
реплик и убранный повтор - норма, если содержание сохранено.

ЗАПРЕЩЕНО В ФАЗЕ 1
- ссылаться на находки, оценки, статусы или вердикты других этапов;
- подбирать заключение под чужие мнения;
- править текст (правки - только в Фазе 2 после сверки с evidence);
- выносить финальные статусы (CONFIRMED_ERROR / DISPUTED / ...);
- останавливаться и спрашивать разрешения: нулевое число находок -
  допустимый итог Фазы 1.

ФОРМАТ ВЫВОДА ФАЗЫ 1: один .md-файл - шапка (часть, run_id, дата) + сводка +
JSON-блок в ```json:
{{
  "analysis_id": "{phase1_id}.phase1",
  "part": "{ch.part_id}",
  "phase": 1,
  "scope": "blind",
  "results": [
    {{
      "line": 15,
      "finding": "MISSING_TRANSLATION",
      "note": "Кратко: что именно отсутствует и почему это не компрессия",
      "confidence": "HIGH"
    }}
  ]
}}

Значения finding: MISTRANSLATION / NUANCE_SHIFT / LEXICAL_MISMATCH /
PRAGMATIC_SHIFT / ADDED_CONTENT / AMBIGUITY / MISSING_TRANSLATION / OTHER / NONE.
- NONE - реплика проверена, существенных ошибок нет.
- confidence: HIGH / MEDIUM / LOW.
- Это ПРЕДВАРИТЕЛЬНОЕ заключение слепой проверки, а не финальный вердикт.
- Пустой results = «существенных ошибок не найдено»; это допустимый итог.
Ничего, кроме этого файла, не создавай и не изменяй.

OUTPUT FILE (единственный файл этого запуска):
{out_rel}
(абсолютный путь: {out_abs})"""


def prompt_analyzer_phase2(ch: Chapter,
                           runs: dict[str, list[str]] | None = None) -> str:
    """ФАЗА Analyzer 2 - EVIDENCE REVIEW (после слепой Фазы 1).

    Analyzer - единственный агент, которому разрешено читать результаты
    независимых аудиторов (все существующие запуски ЭТОЙ части; механизма
    ручного выбора run_id нет). Он сам сверяет candidates с источником,
    исправляет только CONFIRMED_ERROR и пишет спорное в analysis/.

    Два режима одного и того же анализа:
    - A + B - если запусков C ещё нет;
    - A + B + C - если запуски C существуют.
    Наличие C и pre-check не обязательно; majority vote запрещён в обоих
    режимах.

    ``runs`` - только для self-test (симуляция содержимого каталогов);
    в рабочем режиме список запусков читается с диска.
    """
    analysis_id = new_audit_run_id(ch)
    run_map = (runs if runs is not None
               else {k: sma_existing_runs(ch, k) for k in ("a", "b", "c")})
    phase1_list = sma_existing_phase1_runs(ch)
    precheck_list = sma_existing_precheck(ch)
    a_runs = run_map.get("a", [])
    b_runs = run_map.get("b", [])
    c_runs = run_map.get("c", [])
    a_list = ", ".join(a_runs) if a_runs else "(пока нет ни одного запуска A)"
    b_list = ", ".join(b_runs) if b_runs else "(пока нет ни одного запуска B)"
    c_list = ", ".join(c_runs) if c_runs else "(пока нет ни одного запуска C)"
    mode = "A + B + C" if c_runs else "A + B"
    p1_list = (", ".join(f"{r}.phase1" for r in phase1_list)
               if phase1_list else "(нет слепых выводов Фазы 1)")
    pc_list = (", ".join(precheck_list) if precheck_list
               else "(pre-check не запускался - это норма)")
    pc_input = (f'"{sma_chapter_rel(ch)}/{SMA_PRECHECK_KIND}/{precheck_list[0]}.{SMA_EXT}"'
                if precheck_list else "null")
    if not (a_runs or b_runs or c_runs or precheck_list):
        evidence_note = (
            "EVIDENCE ОТСУТСТВУЕТ: ни одного запуска аудиторов и ни одного "
            "файла pre-check для этой части нет. Ограничься отчётом по своему "
            "слепому выводу Фазы 1, правки НЕ вноси и явно сообщи, что "
            "evidence для Фазы 2 отсутствует.")
    else:
        evidence_note = "НАБОР EVIDENCE (inputs этой части)"
    return f"""ЗАДАЧА: смысловой анализатор (Analyzer) независимых аудиторских сессий и прагматического аудита C.
Часть: {ch.part_id}. Запуск анализа: {analysis_id}.

РОЛЬ
Ты НЕ независимый аудитор: ты получаешь результаты уже выполненных
независимых аудиторских сессий и выносишь итоговое решение по каждому
кандидату. Доступ к evidence - сознательное исключение именно для Analyzer.

ВХОДНЫЕ ДАННЫЕ ЭТОЙ ЧАСТИ
JA - authoritative source of truth: {ch.source_chapter_glob}
EN - reference only (база сценария): {ch.script_rel}
RU - text under review: {tl_display()}
Контекст соседних реплик: те же файлы части
Численная картина части: {inventory_text(part_inventory(ch))}.
Слепой вывод Фазы 1 (твоё собственное ПЕРВОНАЧАЛЬНОЕ заключение, сделано
БЕЗ evidence): {sma_chapter_rel(ch)}/analysis/*.phase1.md
Результаты независимых аудиторов A (читай ТОЛЬКО этот каталог):
  {sma_chapter_rel(ch)}/a/
Результаты независимых аудиторов B (читай ТОЛЬКО этот каталог):
  {sma_chapter_rel(ch)}/b/
Результаты Pragmatic Auditor C (читай ТОЛЬКО этот каталог):
  {sma_chapter_rel(ch)}/c/
Evidence детерминированного pre-check (не аудитор, не голос):
  {sma_chapter_rel(ch)}/{SMA_PRECHECK_KIND}/
Каталог результатов Analyzer (куда писать):
  {sma_chapter_rel(ch)}/analysis/

{SMA_SOURCE_HIERARCHY_NOTE}

НАБОР EVIDENCE (inputs этой части)
a_runs: {a_list}
b_runs: {b_list}
c_runs: {c_list}
precheck: {pc_list}
Фаза 1: {p1_list}
{evidence_note}

РЕЖИМ ЭТОГО ЗАПУСКА: {mode}
- Режим A + B - если в c/ нет ни одного файла результата: работай только с
  findings A и B. Отсутствие запусков C - норма, это не повод останавливаться.
- Режим A + B + C - если запуски C существуют: подключи их findings наравне
  с findings A и B (тот же порядок, тот же статус, тот же разбор).
Наличие C НЕ обязательно; наличие pre-check НЕ обязательно: если его файлов
нет - работай без него и не останавливайся.

ПРАВИЛА EVIDENCE:
- Учитывай ВСЕ существующие запуски этой части, а не только последний;
  ручного выбора отдельных run_id нет.
- Результаты ДРУГИХ частей и глав не используй.
- findings аудиторов - исторические: не редактируй, не удаляй и не
  переписывай файлы в a/, b/ и c/.

ШАГ 0 - УБЕДИСЬ, ЧТО ФАЗА 1 УЖЕ ВЫПОЛНЕНА (слепо, без evidence)
Фаза 1 выполнялась ОТДЕЛЬНЫМ заданием, куда не передавалось НИКАКОГО evidence.
Её вывод лежит в analysis/<id>.phase1.md.
- Если такого файла нет - STOP: Фазу 1 выполнять в этом задании НЕЛЬЗЯ
  (blindness утрачен). НЕ пытайся выполнить Фазу 1 внутри Фазы 2: сначала
  отдельное задание «Смысловой анализатор - Фаза 1 (blind)», и только после
  его завершения - Фаза 2.
- Вывод Фазы 1 - входные данные, а НЕ evidence и не чужое мнение: он не
  голосует и не является основанием для правки.

ШАГ 1 - СБОР EVIDENCE (Фаза 2 начинается здесь)
Собери ВСЕ findings из всех существующих запусков A, B и C этой части плюс
evidence pre-check. Логически совпадающие candidates сгруппируй и сохрани
происхождение (sources.a / sources.b / sources.c / sources.precheck).

ФАЗА 2 - EVIDENCE REVIEW (ТОЛЬКО после завершённой Фазы 1)
  1) воспроизведи своё заключение Фазы 1 - каким оно было ДО evidence;
  2) посмотри findings A; 3) findings B; 4) findings C; 5) evidence pre-check;
  6) сопоставь всё со своим первоначальным выводом;
  7) реши по каждому candidate: подтвердить, отвергнуть или создать нового;
  8) реши, достаточно ли оснований для правки.

ДОПУСТИМЫЕ ИСХОДЫ (все - норма, не ошибка процесса)
- pre-check нашёл пропуск, Фаза 1 его не заметила -> после сверки JA -> RU
  можно CONFIRMED_ERROR (и FIXED, если правка разрешена).
- Фаза 1 считает перевод корректным, pre-check подозревает пропуск -> после
  проверки DISPUTED (границы/допустимость неясны) либо FALSE_POSITIVE
  (компрессия допустима).
- pre-check и аудиторы молчат, а Фаза 1 нашла ошибку -> candidate создаёшь ты.
- pre-check отсутствует -> работай с имеющимся evidence в прежнем объёме.
- Фаза 1 сама не заметила то, что подтвердилось в Фазе 2 - это не порок
  слепой проверки: именно поэтому фазы разделены.

ЗАПРЕЩЕНО:
- majority vote; «A + B + C -> ошибка»; «BOTH_FOUND -> ERROR автоматически»;
- считать согласие всех аудиторов подтверждением ошибки, а находку только
  одного (в том числе только C) - автоматически ложным positive;
- считать количество обнаружений доказательством: это только evidence;
- принимать решение вместо проверки JA -> RU;
- считать EN источником истины или опираться на совпадение перевода с EN:
  если evidence аудитора или EN противоречит JA, ориентируйся на JA (JA > EN).

ПРОИСХОЖДЕНИЕ (sources) НЕ ГОЛОСУЕТ
- sources.a / sources.b / sources.c / sources.precheck - отметка о том, кто
  заметил место, а не голос за статус.
- Finding C не имеет приоритета над A/B и не отменяется отсутствием находок
  в A/B (и наоборот): каждый candidate рассматривается сам по себе.
- Режим A+B и режим A+B+C обрабатываются одинаково: меняется только набор
  evidence, но не порядок работы и не статусы.

СТАТУСЫ (каждому candidate обязателен один)
- CONFIRMED_ERROR - ясная смысловая ошибка: JA однозначен, перевод передаёт
  другой смысл, исправление формулируется однозначно -> МОЖНО исправлять.
- DISPUTED - расхождение мнений аудиторов или неоднозначность JA -> НЕ
  исправлять.
- FALSE_POSITIVE - finding не подтверждается -> НЕ исправлять.
- OPTIONAL - допустимое улучшение, текущий перевод правилен -> НЕ исправлять.
WARNING / CANDIDATE сами по себе правку не разрешают. Диспозиция кандидата
(FIXED / FALSE POSITIVE / PRESERVED - ... / USER DECISION / ???) фиксируется
по жизненному циклу сигнала (AGENTS.md, раздел 5): обнаружение != решение.

ПРАВКА (только строки этой части, только для CONFIRMED_ERROR)
- Перед правкой зафиксируй исходное состояние: сохрани «before» и подготовь
  «after».
- Правь САМИМИ ФАЙЛАМИ ПРОЕКТА: game/tl/russian/<bucket>.rpy (и
  {ch.script_rel}, если по JA неверна EN-база). Промежуточных копий не создаёт.
- Перед записью - self-review (скилл self-review); после записи - сверка с JA,
  russian-grammar-control по изменённым русским строкам и python
  tools/check_project.py.
- В {ch.log_rel} - запись ПРАВКА: что изменено и почему; before/after - в
  analysis-отчёте.
- Ничего не меняй «заодно»; соседние реплики без необходимости не трогай.
- После исправления одних строк следующие candidates проверяй по АКТУАЛЬНОМУ
  переводу (findings аудиторов остаются историческими).
- НЕ запускай цикл аудиторы -> Analyzer -> правка -> аудиторы -> ...: после
  Analyzer цикл заканчивается; повторный аудит - отдельный ручной запуск.

ФОРМАТ РЕЗУЛЬТАТА: один .md-файл - человекочитаемый отчёт (таблица по каждому
candidate + отдельные сводки по DISPUTED и OPTIONAL) с JSON-блоком в ```json:
{{
  "analysis_id": "{analysis_id}",
  "part": "{ch.part_id}",
  "inputs": {{
    "a_runs": [{json_list(a_runs)}],
    "b_runs": [{json_list(b_runs)}],
    "c_runs": [{json_list(c_runs)}],
    "precheck": {pc_input}
  }},
  "results": [
    {{
      "line": 11,
      "candidate_id": "C-11-01",
      "sources": {{ "a": ["<run_id>"], "b": ["<run_id>"], "c": ["<run_id>"], "precheck": false }},
      "source": "JA fragment",
      "current": "RU fragment",
      "status": "CONFIRMED_ERROR",
      "reason": "Обоснование Analyzer",
      "suggestion": "Исправленный вариант",
      "action": "FIXED",
      "before": "строка до правки (обязательно для FIXED)",
      "after": "строка после правки (обязательно для FIXED)"
    }}
  ]
}}

Разрешённые status: CONFIRMED_ERROR / DISPUTED / FALSE_POSITIVE / OPTIONAL.
Разрешённые action: FIXED / REPORT_ONLY / PRESERVED.
- FIXED - только для CONFIRMED_ERROR (правка внесена в файлы проекта).
- REPORT_ONLY - DISPUTED / OPTIONAL (в отчёт, перевод не менять).
- PRESERVED - FALSE_POSITIVE (оставлено как есть).
- line - номер реплики/строки в части; candidate_id стабилен: C-<line>-<NN>.
- inputs.a_runs / b_runs / c_runs - все существующие запуски этой части на
  момент анализа; в режиме A+B поле c_runs пустое.
- inputs.precheck - путь к evidence pre-check либо null, если его нет.
- Для omission-кандидата (issue_type MISSING_TRANSLATION) обязательны поля:
  omission_scope, omission_kind, ja_span, ru_before, ru_after,
  missing_content, not_compression_reason - и отдельная явная секция в MD-части
  отчёта (Scope / Kind / Severity / JA / RU before / RU after / Missing /
  Reason), а не общая фраза. «Пропуск != компрессия»: сжатие, слияние реплик и
  убранный повтор при сохранённом содержании пропуском не являются.

OUTPUT FILES (этой части, запуск {analysis_id})
MD: {sma_result_rel_path(ch, "analysis", analysis_id)}
(абсолютный путь: {sma_result_abs_path(ch, "analysis", analysis_id)})
Пиши ТОЛЬКО в каталог analysis/ этой части; другие файлы не создавай и не
изменяй. Итоги рассмотренных кандидатов (classification + disposition)
отражаются также в отчёте части {ch.report_rel}; журнальные записи - дозаписью
в {ch.log_rel}."""


def json_list(items: list[str]) -> str:
    """Список строк как JSON-массив без внешних скобок (для вставки в шаблон)."""
    return ", ".join(f'"{item}"' for item in items)


# ============================================================================
# СПИСОК ПРОМПТОВ
# ============================================================================
# Скиллы независимых аудиторов A и B, а также скилл сквозной переводческой
# сверки отключены системой: задания для них здесь НЕ генерируются. Их evidence
# появляется от внешних изолированных сессий в reports/sma/ch<N>/<part>/{a,b}/
# и читается режимами «Прагматический аудит C» и «Смысловой анализатор».
PROMPTS: list[PromptInfo] = [
    PromptInfo(
        "first-launch",
        "Первый запуск главы",
        "Анализ источника, резка на части и сразу начало первой части",
        """
        Читает всю главу источника (реплики и точные аргументы событий),
        определяет структуру и режет главу на части по алгоритму AGENTS.md
        (115 +/- 25 голосовых, сильные границы, окно 90...140), назначает
        имена файлов и лейблов, связывает jump, прогоняет базовую
        автопроверку - и в ТОМ ЖЕ запуске начинает портировать первую часть.
        Спрашивать «начинать ли?» и возвращать один план запрещено.
        Локальные неопределённости решаются как PROVISIONAL и не блокируют.
        Использовать при начале работы над новой главой.
        """.strip(),
        prompt_first_launch,
    ),
    PromptInfo(
        "continue",
        "Продолжение работы над частью",
        "Определить текущее состояние части и продолжить с него",
        """
        Проверяет файл части, оба tl, отчёт, журнал и автопроверку,
        определяет следующий незакрытый этап обычного порядка порта и
        выполняет его до конца. Существующая работа не повторяется и без
        нужды не переписывается. Использовать для обычного продолжения
        незавершённой части.
        """.strip(),
        prompt_continue,
    ),
    PromptInfo(
        "port-part",
        "Порт части",
        "События -> voice -> реплика EN -> menu/choice -> jump + оба tl",
        """
        Основной режим портирования: события PS2 переносятся в игровые
        вызовы по справочнику соответствий и образцу глав 0/1, голоса
        идут по id, EN-база пишется из JA прямо в скрипт, параллельно
        добавляются old/new в оба языка, в конце - jump, автопроверка и
        отчёт части. Аргументы событий берутся только из источника.
        Использовать для переноса очередной (или первой) части главы.
        """.strip(),
        prompt_port_part,
    ),
    PromptInfo(
        "translate-edit",
        "Перевод / редактура EN <-> RU",
        "Сверка и доработка переводных строк существующей части",
        """
        Находит строки без пары old/new, переводит и редактирует по JA
        (JA - арбитр, EN - только наша база сценария), сверяет смысл,
        термины и обращения, применяет правила оформления и грамматики,
        записывает изменения в файлы проекта с самопроверкой и
        автопроверкой. Использовать, когда база части есть, а перевод
        требует доработки.
        """.strip(),
        prompt_translate_edit,
    ),
    PromptInfo(
        "voice-work",
        "Портирование голосов",
        "id -> STV -> ogg -> имя -> строка voice (скилл voice-workflow)",
        """
        Ведёт работу со звуком строго по идентификаторам: собирает все
        [voice N] части, конвертирует и размещает .ogg с правильными
        именами, проставляет строки voice, обновляет таблицу говорящих
        и transcriptions_ja_ru.csv, проверяет результат автопроверкой.
        Подбор голоса «по похожести» запрещён.
        """.strip(),
        prompt_voice_work,
    ),
    PromptInfo(
        "full-audit",
        "Полный аудит части",
        "Смысл -> проза -> humanizer -> грамматика -> стиль -> чек-лист -> отчёт",
        """
        Последовательная проверка готовой или почти готовой части по всем
        слоям: смысловая сверка с японским оригиналом, оформление русской
        прозы, снятие машинности, грамматический контроль, стилевой аудит,
        самопроверка перед записью, автопроверка проекта и итоговый отчёт
        части с classification/disposition каждого кандидата. Ноль правок -
        допустимый итог. Использовать перед закрытием части.
        """.strip(),
        prompt_full_audit,
    ),
    PromptInfo(
        "grammar-audit",
        "Грамматический аудит",
        "Морфология, согласование, управление, падежи, актанты и залог",
        """
        Отдельная проверка русского текста по скиллу russian-grammar-control:
        разбор по предложениям, залог и актанты, управление, согласование,
        падежи, местоименные связи. Каждый кандидат получает вердикт с
        обоснованием; правки сопровождаются повторным контролем и
        автопроверкой. Использовать, когда смысл устраивает, а нужен
        чисто языковой контроль.
        """.strip(),
        prompt_grammar_audit,
    ),
    PromptInfo(
        "style-audit",
        "Стилевой аудит",
        "Тавтология, повторы, избыточность, кальки, неудачные словосочетания",
        """
        Проверка текста по скиллу russian-style-audit: повторы, тавтология,
        семантическая избыточность, кальки, номинализации, монотонность
        эпитетов. Не дублирует смысловой, грамматический и оформительский
        слои; намеренная повторность и голос персонажей не считаются
        ошибками; предпочтение редактора не равно ошибке.
        Использовать после смысловой и грамматической проверок.
        """.strip(),
        prompt_style_audit,
    ),
    PromptInfo(
        "humanizer",
        "Humanizer / machine-like",
        "Кальки, канцелярит, шаблоны и другие признаки машинного текста",
        """
        Ищет места, формально правильные, но неживые: кальки с английского,
        канцелярит, шаблонные конструкции, книжные связки, повторяющиеся
        схемы. Работает с защитой от переисправления: голос персонажей,
        модальность и оформленная разметка не «улучшаются»; рискованные
        правки предлагаются, а не вносятся молча. Использовать, когда
        перевод смыслово корректен, но отдельные фразы звучат как перевод.
        """.strip(),
        prompt_humanizer,
    ),
    PromptInfo(
        "resolve-decisions",
        "Решения пользователя (OPEN / PROVISIONAL)",
        "Применить решения по отложенным вопросам и временным значениям",
        """
        Применяет решения пользователя по статусам OPEN/DEFERRED и по
        записям PROVISIONAL одним проходом: находит все места использования
        (скрипт, оба языка, словари, отчёты, журнал), приводит их к единой
        форме, обновляет статусы и записи словаря, фиксирует всё в журнале
        и прогоняет повторный контроль. Закрытие вопроса без явного
        решения запрещено. Использовать после получения решений.
        """.strip(),
        prompt_resolve_decisions,
    ),
    PromptInfo(
        "pragmatic-c",
        "Прагматический аудит C",
        "Изолированный аудит: речевой акт, подтекст, сила реплики",
        """
        Генерирует изолированное задание для прагматического аудитора C:
        коммуникативный акт реплики, намёк и недосказанность, степень
        уверенности, сила и категоричность, скрытое отношение, японские
        прагматические конструкции. Уникальный run_id на каждый запуск,
        единственный выходной файл - .md с JSON-блоком в
        reports/sma/ch<N>/<part>/c/. Ничего не правит: только evidence.
        """.strip(),
        prompt_pragmatic_c,
    ),
    PromptInfo(
        "analyzer-phase1",
        "Смысловой анализатор - Фаза 1 (blind)",
        "Слепая самостоятельная сверка JA -> RU, БЕЗ какого-либо evidence",
        """
        Первая из двух независимых фаз. Задание содержит только JA,
        EN-базу, RU-перевод и контекст части; физически не передаются
        findings аудиторов, evidence pre-check, происхождение, списки
        запусков и результаты прежних анализов. Никаких финальных статусов
        Фаза 1 не выносит - только предварительное заключение в
        analysis/<id>.phase1.md. Запускать ПЕРЕД Фазой 2.
        """.strip(),
        prompt_analyzer_phase1,
    ),
    PromptInfo(
        "analyzer-phase2",
        "Смысловой анализатор - Фаза 2 (evidence review)",
        "Сверка слепого вывода Фазы 1 со всем evidence и решение по кандидатам",
        """
        Вторая фаза: сюда сознательно передаётся всё evidence - findings
        независимых аудиторских сессий, C и pre-check - и собственное
        слепое заключение Фазы 1. Analyzer группирует кандидатов, сам
        сверяет их с источником, исправляет только CONFIRMED_ERROR (записью
        в файлы проекта) и пишет спорное в отчёт. Majority vote запрещён;
        режимы A+B и A+B+C; результат - .md с JSON-блоком в analysis/.
        Запускать ПОСЛЕ Фазы 1.
        """.strip(),
        prompt_analyzer_phase2,
    ),
    PromptInfo(
        "encoding-check",
        "Проверка кодировки и целостности",
        "UTF-8, повреждённые символы, пары old/new, управляющие символы",
        """
        Техническая проверка файлов части: кодировка, mojibake, подмена
        букв, управляющие символы, парность и непустота переводных пар,
        незакрытая разметка. Содержимое без подтверждённой ошибки не
        меняется; каждая находка проходит классификацию и решение.
        Использовать после переноса файлов, работы разных редакторов
        или при подозрении на повреждение.
        """.strip(),
        prompt_encoding_check,
    ),
]


# ============================================================================
# ACTIONS (детерминированные действия; НЕ LLM-промпты)
# ============================================================================
def _run_tool(script_rel: str, args: list[str]) -> int:
    """Запустить инструмент проекта, показать вывод и код завершения.

    Путь к скрипту берётся от ROOT; аргументы - только ASCII (японские
    имена в командные строки не передаются). Вывод печатается через say():
    нестандартные символы заменяются на '?' только в консоли.
    """
    command = [sys.executable, script_rel] + list(args)
    shown = " ".join([script_rel] + list(args))
    say(f"  Команда: python {shown}")
    say()
    try:
        process = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except OSError as exc:
        say(f"  Не удалось запустить {script_rel}: {exc}")
        return 1
    say("  --- stdout ---")
    for line in (process.stdout or "").splitlines():
        say("  " + line)
    if process.stderr:
        say("  --- stderr ---")
        for line in process.stderr.splitlines():
            say("  " + line)
    say()
    say(f"  Код завершения: {process.returncode}")
    return process.returncode


def _tool_missing(script_rel: str) -> bool:
    """True, если скрипта в проекте ещё нет (сначала сообщить, не падать)."""
    if os.path.isfile(os.path.join(ROOT, script_rel)):
        return False
    say()
    say(f"  Скрипт не найден: {script_rel}")
    say("  Действие станет доступно после его добавления в tools/.")
    return True


def action_check_project(ch: Chapter) -> int:
    """Прогнать автопроверку проекта и показать результат."""
    say()
    separator("=")
    say()
    say("  Действие: автопроверка проекта")
    say(f"  Часть: {ch.part_id}")
    say()
    say("  Назначение: все проверки E1-E8, W1-W5, I1 (скилл project-checks).")
    say("  Отчёт пишется в reports/check_project.md (UTF-8).")
    say("  Код 0 = RESULT: OK, код 1 = RESULT: ERRORS.")
    say()
    separator("=")
    say()
    return _run_tool(CHECK_TOOL, [])


def load_chapter_stats() -> dict:
    """chapter_stats.json целиком (значения содержат японские имена глав:
    в консоль они НЕ выводятся - используются только числовые поля)."""
    try:
        with open(STATS_FILE, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def numeric_stats_text(entry: dict) -> str:
    """Числовые поля статистики одной главы источника (без поля name)."""
    order = ("scenes", "core_min", "core_max", "extras", "talk",
             "set", "trans", "choice", "date")
    parts = []
    for key in order:
        if key in entry:
            parts.append(f"{key}={entry[key]}")
    return ", ".join(parts) if parts else "(числовых полей нет)"


def _iter_chapter_parts(chapter: int) -> list[tuple[int, str]]:
    """[(номер части, имя файла)] по фактическим файлам главы."""
    folder = os.path.join(ROOT, "game", "chapters", str(chapter))
    if not os.path.isdir(folder):
        return []
    found: list[tuple[int, str]] = []
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".rpy"):
            continue
        if chapter == 0 and name == "script-ch0.rpy":
            found.append((1, name))
            continue
        match = re.match(rf"^script-ch{chapter}_(\d+)\.rpy$", name)
        if match:
            found.append((int(match.group(1)), name))
    return sorted(found)


def action_chapter_state(ch: Chapter) -> int:
    """Показать состояние главы: какие части есть, счётчики, отчёты."""
    say()
    separator("=")
    say()
    say(f"  Действие: состояние главы {ch.chapter_id} (проектная глава {ch.chapter})")
    say(f"  Каталог: game/chapters/{ch.chapter}/")
    say()
    parts = _iter_chapter_parts(ch.chapter)
    stats = load_chapter_stats()
    entry = stats.get(str(ch.chapter + 1))
    if isinstance(entry, dict) and "talk" in entry:
        say(f"  Источник (chapter_stats.json, ключ \"{ch.chapter + 1}\"): "
            f"{numeric_stats_text(entry)}")
    else:
        say("  Источник: chapter_stats.json - запись для этой главы не найдена")
    say(f"  Глоб реплик: {ch.source_chapter_glob}")
    say()
    if not parts:
        say("  Файлы частей не найдены (глава ещё не начата).")
        say(f"  Первая часть будет: {Chapter(chapter=ch.chapter, part=1).script_rel}")
    for part_no, file_name in parts:
        part_ch = Chapter(chapter=ch.chapter, part=part_no)
        inv = part_inventory(part_ch)
        say(f"  часть {part_no} ({part_ch.part_id})  файл: {file_name}")
        say(f"      {inventory_text(inv)}")
        say(f"      отчёт: {part_ch.report_rel} "
            f"({'есть' if part_ch.report_exists else 'нет'})")
    if parts:
        next_part = parts[-1][0] + 1
        nxt = Chapter(chapter=ch.chapter, part=next_part)
        say()
        say(f"  Следующая к созданию: часть {next_part} ({nxt.script_rel})")
    else:
        say()
        say("  Следующая к созданию: часть 1")
    say()
    say(f"  Общий ход: прогони python {CHECK_TOOL} - там I1 по этой главе.")
    say()
    separator("=")
    say()
    return 0


def action_source_stats(ch: Chapter) -> int:
    """Показать сводку по источнику главы (глобы + chapter_stats.json)."""
    chapter_glob = os.path.join(ROOT, "ps2_source", "chapters",
                                f"chapter_{ch.chapter + 1:02d}_*.txt")
    events_glob = os.path.join(ROOT, "ps2_source", "events_full",
                               f"chapter_{ch.chapter + 1:02d}_*.txt")
    chapter_hits = sorted(globlib.glob(chapter_glob))
    events_hits = sorted(globlib.glob(events_glob))
    stats = load_chapter_stats()
    entry = stats.get(str(ch.chapter + 1))
    say()
    separator("=")
    say()
    say(f"  Действие: сводка по источнику главы {ch.chapter_id}")
    say()
    say(f"  Реплики и события: {ch.source_chapter_glob}")
    say(f"    совпадений: {len(chapter_hits)}  "
        "(имена содержат японский - в консоль не выводятся)")
    say(f"  Точные аргументы: {ch.source_events_glob}")
    say(f"    совпадений: {len(events_hits)}")
    say()
    if isinstance(entry, dict):
        say(f"  chapter_stats.json, ключ \"{ch.chapter + 1}\":")
        say(f"    {numeric_stats_text(entry)}")
        talk = entry.get("talk")
        if isinstance(talk, int):
            say(f"    ориентир для I1: talk={talk} "
                "(полный охват части достигается суммой строк её файлов)")
    else:
        say("  chapter_stats.json: записи для этой главы нет")
    say()
    say("  Замечание: поле name главы в JSON - японское, поэтому не печатается.")
    say()
    separator("=")
    say()
    return 0


def action_image_id_map(ch: Chapter) -> int:
    """Обновить справочник image id (tools/build_image_id_map.py)."""
    say()
    separator("=")
    say()
    say("  Действие: обновление справочника image id")
    say(f"  Часть: {ch.part_id}")
    say()
    say(f"  Справочник: {IMAGE_MAP_CSV}")
    say("  Назначение: сопоставление id картинок PS2 с именами ремастера.")
    say("  Вывод скрипта не должен содержать японских строк в консоли -")
    say("  печать идёт через защитный вывод.")
    say()
    separator("=")
    say()
    if _tool_missing(IMAGE_MAP_TOOL):
        say(f"  Справочник {IMAGE_MAP_CSV} заполняется пользователем")
        say("  (формат и порядок расширения - скилл assets).")
        return 1
    return _run_tool(IMAGE_MAP_TOOL, [])


def action_bg_placeholders(ch: Chapter) -> int:
    """Замена заглушек id(K) на имена (по умолчанию dry-run)."""
    say()
    separator("=")
    say()
    say("  Действие: замена заглушек id(K) на имена из справочника")
    say(f"  Часть: {ch.part_id}")
    say()
    say("  Режим по умолчанию: dry-run (только список замен, без записи).")
    say("  Применение: python tools/replace_bg_placeholders.py --apply")
    say()
    separator("=")
    say()
    if _tool_missing(BG_TOOL):
        say("  Заглушки id(K) пока правятся вручную по references/*.csv.")
        return 1
    args = ["--apply"] if CLI_APPLY else []
    code = _run_tool(BG_TOOL, args)
    say()
    if CLI_APPLY:
        say("  Режим --apply: изменения могли быть внесены в файлы.")
    else:
        say("  Это был dry-run. Изменения НЕ вносились.")
        say(f"  Для применения: python {BG_TOOL} --apply")
    return code


ACTIONS: list[ActionInfo] = [
    ActionInfo(
        "check-project",
        "Автопроверка проекта",
        "Прогнать python tools/check_project.py и показать результат",
        action_check_project,
    ),
    ActionInfo(
        "chapter-state",
        "Состояние главы и частей",
        "Какие script-файлы есть, счётчики строк/голосов, отчёты",
        action_chapter_state,
    ),
    ActionInfo(
        "source-stats",
        "Сводка по источнику главы",
        "Глобы источника и числовые поля chapter_stats.json",
        action_source_stats,
    ),
    ActionInfo(
        "image-id-map",
        "Обновить справочник image id",
        "python tools/build_image_id_map.py (если скрипт добавлен)",
        action_image_id_map,
    ),
    ActionInfo(
        "bg-placeholders",
        "Замена заглушек id(K)",
        "python tools/replace_bg_placeholders.py - dry-run, --apply для записи",
        action_bg_placeholders,
    ),
]

# Режим применения для замены заглушек: False = dry-run (по умолчанию),
# True = --apply (задаётся только через CLI, в интерактиве - dry-run).
CLI_APPLY = False


# ============================================================================
# ГЕНЕРАЦИЯ ПРОМПТА, ФАЙЛ, БУФЕР ОБМЕНА
# ============================================================================
def generate_prompt(info: PromptInfo, ch: Chapter) -> str:
    """Сгенерировать текст промпта; пустая строка - режим без генератора."""
    if info.generator is None:
        return ""
    text = info.generator(ch)
    return text.strip() if isinstance(text, str) else ""


def save_prompt_to_file(text: str) -> str:
    """Сохранить промпт в agent_prompt.md (UTF-8) и вернуть путь.

    Файл в корне проекта, в .gitignore; перезаписывается при каждой генерации.
    В консоль текст промпта НЕ выводится - только путь.
    """
    with open(PROMPT_FILE, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
        if not text.endswith("\n"):
            fh.write("\n")
    return PROMPT_FILE


def copy_to_clipboard(text: str) -> bool:
    """Скопировать текст в системный буфер обмена (PowerShell + base64).

    base64 передаётся в stdin: командная строка остаётся короткой (нет лимита
    длины), а консоль cp1251 текст не искажает - искажения могли бы попасть
    и в буфер.
    """
    data = base64.b64encode(text.encode("utf-8")).decode("ascii")
    command = (
        "Set-Clipboard -Value "
        "([System.Text.Encoding]::UTF8.GetString("
        "[Convert]::FromBase64String([Console]::In.ReadToEnd())))"
    )
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command", command],
            input=data + "\n",
            capture_output=True,
            text=True,
            encoding="ascii",
            errors="replace",
        )
    except OSError:
        return False
    if result.returncode != 0:
        err = (result.stderr or "").strip()
        if err:
            say(f"  Буфер обмена: {err.splitlines()[-1]}")
        return False
    return True


def ask_confirmation(question: str) -> bool:
    """Да/нет одним числом (консоль здесь cp1251: только ASCII-цифры)."""
    return ask_int(question, 0, 1) == 1


# ============================================================================
# ИНТЕРАКТИВНЫЕ ЭКРАНЫ
# ============================================================================
def print_banner() -> None:
    say()
    say("=" * TERMINAL_WIDTH)
    say("  ZnT1 - оркестратор рабочего процесса (промпты и действия)")
    say("  Единица работы: часть главы game/chapters/<N>/script-<...>.rpy")
    say("=" * TERMINAL_WIDTH)


def show_prompt_info(info: PromptInfo, ch: Chapter) -> None:
    """Показать карточку режима: id, описание, что делает (без текста промпта)."""
    say()
    say("=" * TERMINAL_WIDTH)
    say(f"  {info.title}   [id: {info.id}]")
    say("=" * TERMINAL_WIDTH)
    print_wrapped(info.description, indent="  ")
    say()
    say("  Что делает:")
    print_wrapped(textwrap.dedent(info.guide), indent="    ")
    say()
    say(f"  Целевая часть: {ch.describe()}")
    say(f"  Отчёт части: {ch.report_rel} ({'есть' if ch.report_exists else 'нет'})")
    say()
    say("=" * TERMINAL_WIDTH)


def prompts_menu(ch: Chapter) -> None:
    """Подменю режимов (промптов) с генерацией по подтверждению."""
    while True:
        say()
        say("  РЕЖИМЫ (PROMPTS)")
        separator()
        for index, info in enumerate(PROMPTS, 1):
            say(f"    {index:>2}. {info.title}   [{info.id}]")
        say("     0. Назад в главное меню")
        say()
        choice = ask_int("  Ваш выбор: ", 0, len(PROMPTS))
        if choice == 0:
            return
        info = PROMPTS[choice - 1]
        show_prompt_info(info, ch)
        if not ask_confirmation(
                f"  Сгенерировать промпт для {ch.part_id}? (1 - да, 0 - отмена): "):
            say("  Отменено.")
            continue
        text = generate_prompt(info, ch)
        if not text:
            say("  У режима нет генератора - промпт не создан.")
            continue
        path = save_prompt_to_file(text)
        say()
        say(f"  Готово: {len(text)} символов.")
        say(f"  Промпт сохранён: {path}")
        say("  Текст в консоль не выводится (кодировка консоли cp1251).")
        say("  Его можно открыть в редакторе или скопировать в буфер.")
        if ask_confirmation("  Скопировать в буфер обмена? (1 - да, 0 - нет): "):
            if copy_to_clipboard(text):
                say("  Скопировано в буфер обмена.")
            else:
                say("  Не удалось скопировать (буфер недоступен).")
        say()
        if not ask_confirmation("  Сгенерировать ещё один промпт? (1 - да, 0 - нет): "):
            return


def actions_menu(ch: Chapter) -> None:
    """Подменю детерминированных действий (промпт не создаётся)."""
    while True:
        say()
        say("  ДЕЙСТВИЯ (ACTIONS) - без генерации промпта")
        separator()
        for index, info in enumerate(ACTIONS, 1):
            say(f"    {index:>2}. {info.name}   [{info.id}]")
        say("     0. Назад в главное меню")
        say()
        choice = ask_int("  Ваш выбор: ", 0, len(ACTIONS))
        if choice == 0:
            return
        info = ACTIONS[choice - 1]
        say()
        say("=" * TERMINAL_WIDTH)
        say(f"  {info.name}   [id: {info.id}]")
        say("=" * TERMINAL_WIDTH)
        print_wrapped(info.description, indent="  ")
        say()
        say(f"  Целевая часть: {ch.describe()}")
        say()
        if not ask_confirmation("  Выполнить? (1 - да, 0 - отмена): "):
            say("  Отменено.")
            continue
        code = info.execute(ch)
        say(f"  Действие завершено: {info.id} (код {code}).")
        if not ask_confirmation("  Выполнить ещё одно действие? (1 - да, 0 - нет): "):
            return


def navigation_menu(ch: Chapter) -> Chapter:
    """Навигация по частям; возвращает (возможно, новую) текущую часть."""
    while True:
        prev_part = navigate_prev_part(ch)
        next_part = navigate_next_part(ch)
        next_chapter = navigate_next_chapter(ch)
        say()
        say(f"  Текущая часть: {ch.describe()}")
        say()
        say("  НАВИГАЦИЯ")
        say(f"    1. Следующая часть: {next_part.part_id}")
        if prev_part is None:
            say("    2. Предыдущая часть: недоступно (это первая часть)")
        else:
            say(f"    2. Предыдущая часть: {prev_part.part_id}")
        if next_chapter is None:
            say("    3. Следующая глава: недоступно (это последняя глава)")
        else:
            say(f"    3. Следующая глава: {next_chapter.part_id} "
                f"(глоб {next_chapter.source_chapter_glob})")
        say("     0. Назад в главное меню")
        say()
        choice = ask_int("  Ваш выбор: ", 0, 3)
        if choice == 1:
            ch = next_part
        elif choice == 2:
            if prev_part is None:
                say("  Это первая часть главы.")
            else:
                ch = prev_part
        elif choice == 3:
            if next_chapter is None:
                say("  Это последняя глава проекта.")
            else:
                ch = next_chapter
        else:
            return ch
        say(f"  Текущая часть: {ch.describe()}")


def main_menu(ch: Chapter) -> str:
    """Главное меню; возвращает команду: prompts/actions/change/nav/quit."""
    say()
    say(f"  Текущая часть: {ch.describe()}")
    say(f"  Скрипт: {ch.script_rel} ({ch.exists_text})")
    say(f"  Отчёт: {ch.report_rel} ({'есть' if ch.report_exists else 'нет'})")
    say()
    say("  ГЛАВНОЕ МЕНЮ")
    say("    1. Режимы работы (промпты)")
    say("    2. Действия (без генерации промпта)")
    say("    3. Сменить часть вручную")
    say("    4. Навигация")
    say("    0. Выход")
    say()
    choice = ask_int("  Ваш выбор: ", 0, 4)
    return {1: "prompts", 2: "actions", 3: "change", 4: "nav", 0: "quit"}[choice]


def interactive_loop() -> int:
    """Интерактивный режим: выбор части -> меню -> работа -> выход."""
    print_banner()
    ch = ask_chapter()
    while True:
        command = main_menu(ch)
        if command == "quit":
            say()
            say("  Выход.")
            return 0
        if command == "prompts":
            prompts_menu(ch)
        elif command == "actions":
            actions_menu(ch)
        elif command == "change":
            ch = ask_chapter()
        elif command == "nav":
            ch = navigation_menu(ch)


# ============================================================================
# SELF-TEST (dry-run: файлы проекта не читаются и не изменяются)
# ============================================================================
def self_test_sma() -> int:
    """Самопроверка оркестратора: структура режимов, изоляция фаз, run_id.

    Ничего не пишет: только генерирует промпты в памяти и сверяет их
    properties. Возвращает 0 - все проверки пройдены, 1 - есть провалы.
    """
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, ok: bool, detail: str = "") -> None:
        checks.append((name, bool(ok), detail))

    expected_prompt_ids = [
        "first-launch", "continue", "port-part", "translate-edit", "voice-work",
        "full-audit", "grammar-audit", "style-audit", "humanizer",
        "resolve-decisions", "pragmatic-c", "analyzer-phase1",
        "analyzer-phase2", "encoding-check",
    ]
    expected_action_ids = [
        "check-project", "chapter-state", "source-stats", "image-id-map",
        "bg-placeholders",
    ]

    prompt_ids = [p.id for p in PROMPTS]
    action_ids = [a.id for a in ACTIONS]
    check("PROMPTS: состав id соответствует ожидаемому",
          prompt_ids == expected_prompt_ids,
          f"получено: {', '.join(prompt_ids)}")
    check("ACTIONS: состав id соответствует ожидаемому",
          action_ids == expected_action_ids,
          f"получено: {', '.join(action_ids)}")
    check("PROMPTS: id уникальны", len(set(prompt_ids)) == len(prompt_ids))
    check("ACTIONS: id уникальны", len(set(action_ids)) == len(action_ids))
    check("PROMPTS и ACTIONS не пересекаются",
          not (set(prompt_ids) & set(action_ids)))
    check("PROMPTS: у каждого есть генератор",
          all(callable(p.generator) for p in PROMPTS))
    check("ACTIONS: у каждого есть исполняемая функция",
          all(callable(a.execute) for a in ACTIONS))
    check("TL-бакеты уникальны", len(set(TL_BUCKETS)) == len(TL_BUCKETS))
    check("Границы глав осмыслены",
          PROJECT_CHAPTER_MIN == 0 and PROJECT_CHAPTER_MAX >= 28)

    ch = Chapter(chapter=3, part=2)
    check("Часть: скрипт по шаблону game/chapters/<N>/script-ch<N>_<M>.rpy",
          ch.script_rel == "game/chapters/3/script-ch3_2.rpy",
          ch.script_rel)
    check("Часть: источник = глава проекта + 1",
          ch.source_chapter_glob.startswith("ps2_source/chapters/chapter_04_"),
          ch.source_chapter_glob)
    check("Пути SMA начинаются с reports/sma/ и используют прямые слэши",
          ch.sma_rel == "reports/sma/ch3/ch3_2" and "\\" not in ch.sma_rel,
          ch.sma_rel)

    run_a = new_audit_run_id(ch)
    run_b = new_audit_run_id(ch)
    pattern = re.compile(r"^\d{8}-\d{6}-[0-9a-f]{4}$")
    check("run_id имеет вид YYYYMMDD-HHMMSS-xxxx",
          bool(pattern.match(run_a)) and bool(pattern.match(run_b)),
          f"{run_a}, {run_b}")
    check("run_id уникальны в пределах процесса", run_a != run_b)

    texts = {p.id: generate_prompt(p, ch) for p in PROMPTS}
    check("Все промпты непусты",
          all(len(text) > 200 for text in texts.values()))
    check("Все промпты содержат идентификатор части",
          all(ch.part_id in text for text in texts.values()))
    check("В промптах нет японских иероглифов (риск cp1251 исключён)",
          all(not any("\u3000" <= c <= "\u9fff" or "\uff00" <= c <= "\uffef"
                      for c in text)
              for text in texts.values()))
    check("В промптах есть ссылка на JA как канон",
          all("JA" in text for text in texts.values()))
    check("В контексте промптов есть запрет git commit без подтверждения",
          "git commit" in texts["port-part"])
    check("В контексте промптов есть правило кодировки консоли",
          "cp1251" in texts["port-part"])

    phase1 = texts["analyzer-phase1"]
    check("Фаза 1: слепая (blind)", "blind" in phase1.lower())
    check("Фаза 1: не содержит перечней evidence (a_runs/b_runs/c_runs)",
          all(marker not in phase1
              for marker in ("a_runs", "b_runs", "c_runs", "precheck:")))
    check("Фаза 1: финальные статусы только под запретом, не в JSON",
          '"CONFIRMED_ERROR"' not in phase1
          and '"status"' not in phase1
          and "выносить финальные статусы" in phase1)

    phase2 = texts["analyzer-phase2"]
    check("Фаза 2: содержит inputs a_runs/b_runs/c_runs/precheck",
          all(marker in phase2
              for marker in ('"a_runs"', '"b_runs"', '"c_runs"', "precheck")))
    check("Фаза 2: все четыре статуса кандидата",
          all(marker in phase2 for marker in
              ("CONFIRMED_ERROR", "DISPUTED", "FALSE_POSITIVE", "OPTIONAL")))
    check("Фаза 2: запрет majority vote", "majority" in phase2)
    check("Фаза 2: оба режима (A + B и A + B + C)",
          "A + B" in phase2 and "A + B + C" in phase2)
    check("Фаза 2: путь результата в analysis/ этой части",
          phase2.count(f"{ch.sma_rel}/analysis/") >= 1)

    c_text = texts["pragmatic-c"]
    check("Аудит C: своя роль и свой каталог результата",
          "Pragmatic Auditor C" in c_text and f"{ch.sma_rel}/c/" in c_text)
    check("Аудит C: не ссылается на результаты других аудиторов/Analyzer",
          f"{ch.sma_rel}/a/" not in c_text
          and f"{ch.sma_rel}/b/" not in c_text
          and f"{ch.sma_rel}/analysis/" not in c_text)

    say()
    say("  SELF-TEST (dry-run, файлы не изменялись)")
    separator()
    failed = 0
    for name, ok, detail in checks:
        status = "OK  " if ok else "FAIL"
        say(f"  [{status}] {name}")
        if not ok and detail:
            say(f"         {detail}")
        if not ok:
            failed += 1
    say()
    say(f"  ИТОГ: {len(checks) - failed}/{len(checks)} проверок пройдено.")
    say()
    return 1 if failed else 0


# ============================================================================
# CLI
# ============================================================================
USAGE = """\
Использование (запускать из корня проекта):

  python tools/agent_workflow.py
      Интерактивный режим: выбор части, режимы (промпты), действия, навигация.

  python tools/agent_workflow.py --list
      Печатает id и названия всех PROMPTS и ACTIONS.

  python tools/agent_workflow.py --prompt <id> [--chapter N] [--part M]
      Генерирует промпт и сохраняет его в agent_prompt.md (корень проекта).
      В консоль выводится ТОЛЬКО путь к файлу, текст промпта не печатается.

  python tools/agent_workflow.py --action <id> [--chapter N] [--part M] [--apply]
      Выполняет действие (промпт не создаётся). --apply относится к замене
      заглушек (по умолчанию dry-run).

  python tools/agent_workflow.py --self-test-sma
      Самопроверка оркестратора без изменения файлов.

  python tools/agent_workflow.py --help
      Эта справка.

Примеры:
  python tools/agent_workflow.py --prompt port-part --chapter 3 --part 2
  python tools/agent_workflow.py --action chapter-state --chapter 5
"""


def parse_cli(argv: list[str]) -> dict | int:
    """Разобрать аргументы CLI. Возвращает словарь опций либо 2 - ошибка."""
    options: dict = {
        "prompt": None, "action": None, "chapter": None, "part": None,
        "apply": False, "list": False, "self_test": False,
    }
    index = 0
    while index < len(argv):
        arg = argv[index]
        index += 1
        if arg in ("-h", "--help"):
            print_wrapped(USAGE)
            return 1
        if arg == "--list":
            options["list"] = True
            continue
        if arg == "--self-test-sma":
            options["self_test"] = True
            continue
        if arg == "--apply":
            options["apply"] = True
            continue
        if arg in ("--prompt", "--action", "--chapter", "--part"):
            if index >= len(argv):
                say(f"  После {arg} ожидается значение.")
                return 2
            value = argv[index]
            index += 1
            if arg == "--chapter" or arg == "--part":
                try:
                    value = int(value)
                except ValueError:
                    say(f"  {arg} ожидает целое число, получено: {value}")
                    return 2
            options[arg[2:]] = value
            continue
        say(f"  Неизвестный аргумент: {arg}")
        print_wrapped(USAGE)
        return 2
    if options["prompt"] and options["action"]:
        say("  --prompt и --action одновременно не задаются.")
        return 2
    return options


def cli_list() -> int:
    """Печать списка режимов и действий (id + название)."""
    say()
    say("PROMPTS (режимы; текст промпта печатается только в файл):")
    for info in PROMPTS:
        say(f"  {info.id:<18} {info.title}")
    say()
    say("ACTIONS (детерминированные действия):")
    for info in ACTIONS:
        say(f"  {info.id:<18} {info.name}")
    say()
    return 0


def cli_resolve_chapter(options: dict) -> Chapter:
    """Собрать Chapter из --chapter/--part (по умолчанию - глава 0, часть 1)."""
    chapter = options.get("chapter")
    part = options.get("part")
    return Chapter(
        chapter=PROJECT_CHAPTER_MIN if chapter is None else int(chapter),
        part=1 if part is None else int(part),
    )


def cli_prompt(prompt_id: str, ch: Chapter) -> int:
    """Сгенерировать промпт и напечатать ТОЛЬКО путь файла."""
    info = next((p for p in PROMPTS if p.id == prompt_id), None)
    if info is None:
        say(f"  Неизвестный id промпта: {prompt_id}")
        say(f"  Доступные: {', '.join(p.id for p in PROMPTS)}")
        return 2
    text = generate_prompt(info, ch)
    if not text:
        say("  Генератор не задан - промпт не создан.")
        return 1
    say(save_prompt_to_file(text))
    return 0


def cli_action(action_id: str, ch: Chapter, apply: bool = False) -> int:
    """Выполнить действие; --apply передаётся замене заглушек."""
    global CLI_APPLY
    info = next((a for a in ACTIONS if a.id == action_id), None)
    if info is None:
        say(f"  Неизвестный id действия: {action_id}")
        say(f"  Доступные: {', '.join(a.id for a in ACTIONS)}")
        return 2
    CLI_APPLY = bool(apply)
    return info.execute(ch)


def main(argv: list[str] | None = None) -> int:
    """Точка входа: CLI-режим при наличии аргументов, иначе интерактив."""
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        return interactive_loop()
    options = parse_cli(args)
    if isinstance(options, int):
        return options
    if options["self_test"]:
        return self_test_sma()
    if options["list"]:
        return cli_list()
    if options["prompt"]:
        return cli_prompt(str(options["prompt"]), cli_resolve_chapter(options))
    if options["action"]:
        return cli_action(str(options["action"]),
                          cli_resolve_chapter(options),
                          bool(options["apply"]))
    print_wrapped(USAGE)
    return 2


if __name__ == "__main__":
    sys.exit(main())


