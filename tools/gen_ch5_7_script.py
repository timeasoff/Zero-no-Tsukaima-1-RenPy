# -*- coding: utf-8 -*-
"""Полная пересборка game/chapters/5/script-ch5_7.rpy.

Структура части 7:
  сцена 336-340 (техпереходы, нет диалогов)
  сцена 341 (преамбула оперы - диалоги)
  сцена 342 (реакция)
  сцена 343 (выбор дат - меню)
  -> extra 1104-1114 (первые даты)

Голоса = depth-first по веткам дат:
  [1104,1105,1106,1107,1108], [1109,1110,1111], [1112,1113,1114,1115,1116]
  ...(остатки в будущих частях)

Нумерация: ch5.7_<spk>_<NNN>, NNN — порядковый по говорящему в этом потоке.
Всего: ~80 голосовых + мысли.

EN → tools/ch5_7_en.py, RU → tools/ch5_7_ru.py, JA → events-источник.
old/new пары → tl/japanese, tl/russian (tools/gen_ch5_7_tl.py).
Голоса → references/voice_id_map.csv (tools/apply --manifest).

Использование:
    python tools/gen_ch5_7_script.py            # dry-run: счётчики, пропуски
    python tools/gen_ch5_7_script.py --apply    # записать .rpy
    python tools/gen_ch5_7_script.py --manifest # дописать voice_id_map.csv
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, 'game', 'chapters', '5', 'script-ch5_7.rpy')
SRC = os.path.join(ROOT, 'ps2_source', 'events_full',
                   'chapter_06_本当の想い.txt')

# ------------------------------------------------------- структура (depth-first)
# CHAINS = порядок обхода = порядок нумерации голосов
# Границы: 341-342 (core), затем даты 1104-1114
CHAINS = [
    # core: сцены 341-342
    # затем даты
]

# Меню выбора дат из сцены 343
# → next scene 1104, 1110, 1114, 1118, 1122, 1126, 1130, 1134, 1139, 1144, 1149, 1154, 1159
DATE_CHOICES = [
    (1104, "舞台"),  # Stage
    (1110, "劇場"),  # Theater
    (1114, "表通り"),  # Main Street
    (1118, "宿"),    # Inn
    (1122, "表通り"),  # Main Street
    (1126, "宿"),    # Inn
    (1130, "表通り"),  # Main Street
    (1134, "舞台"),  # Stage
    (1139, "表通り"),  # Main Street
    (1144, "劇場"),  # Theater
    (1149, "舞台"),  # Stage
    (1154, "宿"),    # Inn
    (1159, "表通り"),  # Main Street
]

# -------------------------------------------------------------- справочники
SPK = {'サイト': 's', 'ルイズ': 'l', 'ハルナ': 'ha', 'シエスタ': 'si',
       'デルフリンガー': 'd', 'キュルケ': 'k', 'タバサ': 't', 'ギーシュ': 'g',
       'モンモランシー': 'm', 'ウェザリー': 'w', 'アンリエッタ': 'a',
       'ハルナ': 'ha', 'null': 'th'}

SYM_KEY = {'l': 'louise', 'ha': 'haruna', 'si': 'siesta', 'k': 'kirche',
           't': 'tabitha', 'h': 'henrietta', 's': 'saito', 'd': 'derflinger',
           'g': 'guiche', 'm': 'montmorency', 'w': 'weatherby', 'a': 'anreitta'}

SPRITES = {}
IMAGES = {}
with io.open(os.path.join(ROOT, 'references', 'sprite_id_map.csv'),
             encoding='utf-8') as fh:
    for ln in fh:
        p = ln.rstrip('\n').split(',')
        if p and p[0].isdigit():
            SPRITES[int(p[0])] = p[1] if len(p) > 1 else ''
with io.open(os.path.join(ROOT, 'references', 'image_id_map.csv'),
             encoding='utf-8') as fh:
    for ln in fh:
        p = ln.rstrip('\n').split(',')
        if p and p[0].isdigit():
            IMAGES[int(p[0])] = (p[1], p[2] if len(p) > 2 else '')


def flat(s):
    return s.replace('\n', ' ')


def bg_name(i):
    kind, fn = IMAGES.get(i, ('bg', ''))
    if not fn:
        return 'id(%d)' % i, kind == 'cg'
    return fn, kind == 'cg'


# ---------------------------------------------------------- разбор events
RE_SET = re.compile(r'^SET\s+set\("(\w+)",\s*\{(.*)\}\)\s*$')
RE_TALK = re.compile(r'^DIALOGUE\s+talk\((.*)\)\s*$')
RE_LIKE = re.compile(r'^LIKE\s+like\("([^"]*)",\s*(-?\d+)\)\s*$')
RE_CHOICE = re.compile(r'^CHOICE\s+selectItem\("((?:[^"\\]|\\.)*)",\s*\(0x01000000 \+(\d+)\).*$')
RE_GOTO = re.compile(r'^GOTO\s+next\(\(0x01000000 \+(\d+)\).*$')
RE_MAPDEST = re.compile(r'^MAPDEST\s+moveItem\("([^"]*)",\s*\(0x02000000 \+\d+\),\s*\(0x01000000 \+(\d+)\)\)')
RE_IMG = re.compile(r'image\s*=\s*\(0x02000000 \+(\d+)\)')

def parse_events():
    """Разбор events-файла в структурированный формат."""
    with io.open(SRC, encoding='utf-8') as f:
        content = f.read()
    
    events = []
    current_scenario = []
    
    for line in content.split('\n'):
        if RE_SET.match(line):
            current_scenario.append(('set', RE_SET.match(line).groups()))
        elif RE_TALK.match(line):
            current_scenario.append(('talk', RE_TALK.match(line).groups()))
        elif RE_CHOICE.match(line):
            current_scenario.append(('choice', RE_CHOICE.match(line).groups()))
        elif RE_GOTO.match(line):
            current_scenario.append(('goto', RE_GOTO.match(line).groups()))
        elif RE_LIKE.match(line):
            current_scenario.append(('like', RE_LIKE.match(line).groups()))
        elif RE_MAPDEST.match(line):
            current_scenario.append(('mapdest', RE_MAPDEST.match(line).groups()))
        elif line.startswith('---- SCENE'):
            if current_scenario:
                events.append(current_scenario)
            current_scenario = []
    
    if current_scenario:
        events.append(current_scenario)
    
    return events

# ---------------------------------------------------------- генерация скрипта
def generate_script():
    """Генерация script-ch5_7.rpy."""
    events = parse_events()
    
    # Здесь будет логика генерации
    # Пока просто выводим структуру
    print(f"Найдено {len(events)} сцен")
    return events

if __name__ == '__main__':
    events = generate_script()
    
    if '--apply' in sys.argv:
        # Записать скрипт
        with io.open(SCRIPT, 'w', encoding='utf-8') as f:
            f.write("# Generated script\n")
        print(f"Script written to {SCRIPT}")
    
    if '--manifest' in sys.argv:
        print("Manifest mode not implemented")