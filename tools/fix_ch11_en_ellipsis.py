#!/usr/bin/env python3
"""PROMTS.md п.5: заменить '...' на '…' в EN-строках главы 11.

Меняет только содержимое кавычек в строках диалогов/меню сценария и в
`old "..."` файлов tl/{japanese,russian}/ch11_*.rpy — чтобы old оставался
дословным. Комментарии (JA-канон) не трогаются.
"""
import glob
import re

RE_DLG = re.compile(r'^(\s+[a-z_]+ )(".*")(\s*)$')
RE_MENU = re.compile(r'^(\s+)(".*")(:)$')
RE_OLD = re.compile(r'^(\s+old )(".*")(\s*)$')


def norm(s):
    return re.sub(r'\.{3,}', '…', s)


def fix(path):
    out = []
    changed = 0
    for line in open(path, encoding='utf-8').read().split('\n'):
        for rx in (RE_DLG, RE_MENU, RE_OLD):
            m = rx.match(line)
            if not m:
                continue
            body = m.group(2)
            newbody = norm(body)
            if newbody != body:
                changed += 1
                line = line[:m.start(2)] + newbody + line[m.end(2):]
            break
        out.append(line)
    if changed:
        open(path, 'w', encoding='utf-8').write('\n'.join(out))
    return changed


if __name__ == '__main__':
    total = 0
    paths = sorted(glob.glob('game/chapters/11/script-ch11_*.rpy'))
    paths += sorted(glob.glob('game/tl/japanese/ch11_*.rpy'))
    paths += sorted(glob.glob('game/tl/russian/ch11_*.rpy'))
    for p in paths:
        n = fix(p)
        if n:
            print('%3d  %s' % (n, p))
            total += n
    print('TOTAL', total)
