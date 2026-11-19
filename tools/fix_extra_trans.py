#!/usr/bin/env python3
"""Normalize extra-chapter trans_*.json RU (and EN) strings for typography.

- strip trailing engine tags that leaked into dialogue text from the PS2 source
- '...' -> '…'
- full-line (…) thought -> _…_ italics
- '…' single quotes -> «…» guillemets
- collapse double spaces, fix space before punctuation
"""
import json
import re

ENGINE = re.compile(r'\s*\[[A-Z][^\]]*\]\s*$')


def strip_engine(s):
    prev = None
    while prev != s:
        prev = s
        s = ENGINE.sub('', s)
    return s.rstrip()


def fix_ru(s):
    s = strip_engine(s)
    s = s.replace('...', '…')
    # thought fully wrapped in parentheses -> italics
    if s.startswith('(') and s.endswith(')') and s.count('(') == 1 and s.count(')') == 1:
        s = '_' + s[1:-1] + '_'
    # single-quoted -> guillemets
    s = re.sub(r"'([^']+)'", r'«\1»', s)
    s = re.sub(r' {2,}', ' ', s)
    s = re.sub(r'\s+([,.!?;:…])', r'\1', s)
    return s


def fix_en(s):
    s = strip_engine(s)
    s = s.replace('...', '…')
    s = re.sub(r' {2,}', ' ', s)
    return s


def main():
    for ch in ['90', '91']:
        p = f'reports/extra/trans_{ch}.json'
        d = json.load(open(p, encoding='utf-8'))
        n_engine = n_thought = n_quote = 0
        for k, v in d.items():
            if not isinstance(v, list) or len(v) != 2:
                continue
            en, ru = v[0], v[1]
            if not isinstance(en, str) or not isinstance(ru, str):
                continue
            if ENGINE.search(ru) or ENGINE.search(en):
                n_engine += 1
            if ru.startswith('(') and ru.endswith(')'):
                n_thought += 1
            if "'" in ru:
                n_quote += 1
            d[k] = [fix_en(en), fix_ru(ru)]
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(ch, 'engine', n_engine, 'thought', n_thought, 'singlequote', n_quote)


if __name__ == '__main__':
    main()
