#!/usr/bin/env python3
"""Conservative style-candidate prefilter for RU TL strings in scope.

Evidence only: every hit must be manually classified with JA/EN context.
"""
import glob
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
PATTERNS = {
 'TAUTOLOGY': [r'вправду правда', r'действительно правда', r'главная суть',
               r'главная основная', r'свободная вакансия', r'памятный сувенир',
               r'совместное сотрудничество', r'предварительно планировать',
               r'полностью завершить', r'снова повторить', r'повторить ещё раз'],
 'REDUNDANCY': [r'вернуться обратно', r'спуститься вниз', r'подняться вверх',
                r'продолжать дальше', r'заранее предупредить', r'лично самому',
                r'ещё раз повторить', r'опять снова'],
 'AMPLIFIER': [r'совершенно абсолютно', r'действительно на самом деле',
               r'вполне полностью', r'окрайне сильно', r'абсолютно точно'],
 'CALQUE': [r'\bиметь возможность\b', r'\bпринять решение\b', r'\bдать ответ\b',
            r'\bоказать помощь\b', r'\bосуществить\b', r'\bпроизвести осмотр\b'],
}
SCOPE = [f for c in range(22, 29) for f in glob.glob(str(ROOT / 'game/tl/russian' / ('ch%d_*' % c)))]
SCOPE += glob.glob(str(ROOT / 'game/tl/russian/sp9*'))


def main():
    out = []
    for p in sorted(set(SCOPE)):
        old = None
        for i, line in enumerate(Path(p).read_text(encoding='utf-8').splitlines(), 1):
            mo = re.match(r'^\s*old "(.*)"', line)
            if mo:
                old = mo.group(1)
                continue
            mn = re.match(r'^\s*new "(.*)"', line)
            if mn and old is not None:
                s = mn.group(1)
                hits = []
                for cat, pats in PATTERNS.items():
                    for pat in pats:
                        if re.search(pat, s, re.I):
                            hits.append(cat + ':' + pat)
                if '  ' in s:
                    hits.append('DOUBLE_SPACE')
                if hits:
                    out.append((Path(p).name, i, old[:55], s[:90], hits))
                old = None
    print('candidates', len(out))
    for x in out[:60]:
        print('%s:%d | %s | %s | %s' % x)


if __name__ == '__main__':
    main()
