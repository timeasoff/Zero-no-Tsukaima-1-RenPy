#!/usr/bin/env python3
"""Final round-3 fixes: JA-confirmed omissions and modality shifts in ch27/ch28."""
from pathlib import Path
import glob, re

ROOT = Path(__file__).parent.parent

RU_NEW = {
 'ch27_s_140': ('Из-за отдельной личности Акины оказаться в таком положении…',
                'И всё же — как жаль Харуну. Из-за отдельной личности Акины она оказалась в таком положении…'),
 'ch28_k_002': ('Ноч за ночью тайно встречаться с Табитой — за моей спиной!',
                'Ночь за ночью устраивать с Табитой страстные свидания — за моей спиной!'),
 'ch28_s_027': ('Неужто — ты меня ненавидишь?',
                'Неужто я тебе не нравлюсь?'),
 'ch28_s_028': ('Она не отвечает… И у неё такой обеспокоенный вид…',
                'Она не отвечает… И у неё такой растерянный вид…'),
 'ch28_s_030': ('Всё ещё обеспокоена…',
                'Всё ещё растеряна…'),
}

EN_OLD = {
 'ch28_k_002': ('Going out on secret dates with Tabitha night after night—behind my back!',
                'Going out on intimate dates with Tabitha night after night—behind my back!'),
 'ch28_s_027': ('Could it be—you hate me?',
                'Could it be—you don\'t like me?'),
}

for tag, (a, b) in RU_NEW.items():
    for p in [Path(f) for f in glob.glob(str(ROOT / 'game/tl/russian/*.rpy'))]:
        lines = p.read_text(encoding='utf-8').split('\n')
        n = 0
        for i, line in enumerate(lines):
            m = re.search(r'\{#(\w+)\}', line)
            if m and m.group(1) == tag and i + 1 < len(lines) and a in lines[i + 1]:
                lines[i + 1] = lines[i + 1].replace(a, b)
                n += 1
        if n:
            p.write_text('\n'.join(lines), encoding='utf-8')
            print('RU', tag, '->', p.name)

for tag, (a, b) in EN_OLD.items():
    for pattern, field in [('game/chapters/2[2-8]/*.rpy', 'script'),
                           ('game/tl/japanese/*.rpy', 'old'),
                           ('game/tl/russian/*.rpy', 'old')]:
        for p in [Path(f) for f in glob.glob(str(ROOT / pattern))]:
            lines = p.read_text(encoding='utf-8').split('\n')
            n = 0
            for i, line in enumerate(lines):
                m = re.search(r'\{#(\w+)\}', line)
                if not m or m.group(1) != tag:
                    continue
                target = i if field in ('script', 'old') else i + 1
                if target < len(lines) and a in lines[target]:
                    lines[target] = lines[target].replace(a, b)
                    n += 1
            if n:
                p.write_text('\n'.join(lines), encoding='utf-8')
                print('EN', tag, '->', p.name)
