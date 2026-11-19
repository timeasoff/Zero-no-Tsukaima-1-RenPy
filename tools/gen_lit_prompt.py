#!/usr/bin/env python3
"""Generate independent Russian literary-review prompts for sampled parts."""
from pathlib import Path
import sys

ROOT = Path(__file__).parent.parent
UNITS = [
 ('ch23_3', 23, 'script-ch23_3.rpy', 'ch23_3', 'chapter_24_沈黙の応援.txt'),
 ('ch25_1', 25, 'script-ch25.rpy', 'ch25', 'chapter_26_手紙の秘密.txt'),
 ('ch26_2', 26, 'script-ch26_2.rpy', 'ch26_2', 'chapter_27_タバサの秘密.txt'),
 ('ch27_2', 27, 'script-ch27_2.rpy', 'ch27_2', 'chapter_28_ハルナの秘密.txt'),
 ('sp90', 'extra', 'sp90.rpy', 'sp90', 'chapter_90_特別イベントA（トゥンデレ／デレ）.txt'),
 ('sp91', 'extra', 'sp91.rpy', 'sp91', 'chapter_91_特別イベントB（トゥンデレ／デレ）.txt'),
]

TEMPLATE = """ЗАДАЧА: независимая русская литературная вычитка (промпт 10), часть {unit}.

РАБОТАЙ АВТОНОМНО. Не читай чужие аудиты, отчёты частей и журнал. Используй только перечисленные файлы и свои скиллы.

ВХОДЫ:
- RU (предмет проверки): game/tl/russian/{ru_glob}*.rpy
- JA-пары (справочно, НЕ редактировать): game/tl/japanese/{ru_glob}*.rpy
- EN-база: game/chapters/{chdir}/{script}
- JA-источник: ps2_source/chapters/{src}

ОБЯЗАТЕЛЬНЫЕ СКИЛЛЫ (прочитай перед работой):
- .agents/skills/russian-humanizer/SKILL.md
- .agents/skills/russian-prose-rules/SKILL.md
- .agents/skills/russian-grammar-control/SKILL.md (+ references/grammar-traps.md)
- .agents/skills/russian-style-audit/SKILL.md
- .agents/skills/terminology-dictionary/SKILL.md
- .agents/skills/forms-of-address/SKILL.md
- dictionary.md и addresses.md

ЧТО ПРОВЕРЯТЬ (по чек-листам скиллов):
1. Кальки, переводной синтаксис, неестественный порядок слов.
2. Грамматика: управление, согласование, актанты, залог (RGC-1: возвратный глагол там, где JA/EN пассив), местоимения.
3. Естественность диалогов, различимость голосов персонажей, регистр.
4. Повторы, тавтология, семантическая избыточность, сочетаемость.
5. Прямая речь, мысли, курсив, кавычки, тире, многоточия.
6. Единообразие терминов и установленных обращений (по dictionary.md / addresses.md).

ЖЁСТКИЕ ПРАВИЛА:
- Не переписывай корректную формулировку по субъективному предпочтению. Если текст грамматически корректен, сохраняет смысл JA, термины и оформление — оставь (PRESERVED).
- Не убирай намеренные повторы, просторечие, эмоциональную тавтологию и голос персонажа (PRESERVED — FUNCTIONAL / CHARACTER VOICE).
- Каждую смысловую правку сверь с JA; в находке приведи точную JA-цитату.
- Никаких правок файлов. Только отчёт.

ФОРМАТ: один .md-файл {out}. Внутри:
- шапка (unit, дата, объём проверенных new-строк);
- сводка по категориям (тавтология/повторы/избыточность/коллокации/кальки/номинализации/порядок слов/прочее);
- для каждого кандидата: точная RU-цитата, JA-доказательство, категория, classification (ERROR/WARNING/CANDIDATE), предлагаемая минимальная правка, disposition-рекомендация;
- если проблем нет — явно «CANDIDATES: 0».

Проверь ВСЕ new-строки части, а не только подозрительные.
"""

for unit, ch, script, prefix, src in UNITS:
    chdir = 'extra' if ch == 'extra' else str(ch)
    if ch == 'extra':
        ch_for_src = src.split('_')[1]  # 90 / 91
        ru_glob = prefix
    else:
        ru_glob = prefix
    out = 'reports/lit09/%s.md' % unit
    text = TEMPLATE.format(unit=unit, ru_glob=ru_glob, chdir=chdir,
                           script=script, src=src, out=out)
    p = ROOT / 'reports/lit09' / ('prompt_%s.txt' % unit)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8')
    print(p.relative_to(ROOT))
