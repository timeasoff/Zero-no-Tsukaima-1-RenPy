# -*- coding: utf-8 -*-
"""Правки по итогам Фазы 2 анализатора для главы 7 (ch7_1/ch7_2/ch7_3).

Двойная инвариантность, как в предшественнике tools/apply_ch5_1_phase2_fixes.py:
1) правится ДАТА-ПАК генератора (tools/ch7_*_ru.py) — источники строк;
2) зеркально правится сгенерированный tl/russian (+ EN: script-ch7_2/ch7_3 и
   `old` в tl/{japanese,russian} для изменённых EN).

Правки вносимые (анализатор reports/sma/ch7/chapter/analysis/20261109-200742-7f02.md):
  C-105-01 ch7_c378      なんとなく: убрать «на всякий случай»
  C-208-01 ch7_h_002     やはり……そうですか: убрать «опасалась»
  C-239-01 ch7_h_005     でもね,ルイズ: убрать «Казалось бы»
  C-502-01 ch7_w_004     …しましょうか: восстановить предложение-вопрос
  C-588-01 ch7_s_032/c387 許すわけにはいかない: волевой акт вместо «оправдания»
  C-1016-01 ch7.2_h_008  あなたがた: 2-е лицо (EN + RU)
  C-1210-01 ch7.3_l_007  …はともかく: убрать гипотетическую рамку
  C-1294-01 ch7.3_h_005  籠絡する: переманить, а не «увлечь»
  C-1328-01 ch7.3_th_404a だろうな: RU «наверное», EN «must»

Каждая замена обязана найтись ровно один раз — иначе ошибка и ничего не пишется.
Запуск:  python tools/apply_ch7_phase2_fixes.py [--apply]
"""

import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def rpath(*parts):
    return os.path.join(ROOT, *parts)

# ---- Формы замен: (файл, старое_точное, новое_точное, описание) ----
FIXES = [
    # ---- data-packs (источники строк) ----
    (rpath("tools", "ch7_1_ru.py"),
     'RU["ch7_h_002"] = "Как я и опасалась… значит, всё-таки так…"',
     'RU["ch7_h_002"] = "Как я и думала… значит, всё-таки так…"',
     "C-208-01"),
    (rpath("tools", "ch7_1_ru.py"),
     'RU["ch7_h_005"] = "Казалось бы, Луиза. Однако немало тех, кто сомневается, чего одна королева может добиться."',
     'RU["ch7_h_005"] = "Но знаете, Луиза. Немало есть тех, кто сомневается, чего одна королева может добиться."',
     "C-239-01"),
    (rpath("tools", "ch7_1_ru.py"),
     'RU["ch7_c378"] = "Просто так… на всякий случай."',
     'RU["ch7_c378"] = "Просто так…"',
     "C-105-01"),
    (rpath("tools", "ch7_1_ru.py"),
     'RU["ch7_c387"] = "Но даже так — преступление не оправдание."',
     'RU["ch7_c387"] = "Но даже так — нельзя позволить преступлению сойти с рук."',
     "C-588-01"),
    (rpath("tools", "ch7_1_ru.py"),
     'RU["ch7_s_032"] = "Но даже так — преступлений это не оправдывает!"',
     'RU["ch7_s_032"] = "Но даже так — нельзя позволить, чтобы преступление сошло с рук!"',
     "C-588-01"),
    (rpath("tools", "ch7_1_ru.py"),
     'RU["ch7_w_004"] = "А сперва я расскажу вам кое-что любопытное."',
     'RU["ch7_w_004"] = "А сперва позвольте рассказать вам кое-что любопытное."',
     "C-502-01"),
    (rpath("tools", "ch7_2_ru.py"),
     '"ch7.2_h_008": u"Те, кто стоит у них за спиной, — Реконкиста, не так ли.",',
     '"ch7.2_h_008": u"Те, кто стоит у вас за спиной, — Реконкиста, не так ли.",',
     "C-1016-01"),
    (rpath("tools", "ch7_3_ru.py"),
     '"ch7.3_l_007": u"Но даже если бы мы сумели их придержать — и как же конкретично мы будем спасать Харуну?",',
     '"ch7.3_l_007": u"Остановить их — это одно. Но вот как конкретно мы спасём Харуну?",',
     "C-1210-01"),
    (rpath("tools", "ch7_3_ru.py"),
     '"ch7.3_h_005": u"Из-за этого я и дала им шанс увлечь дворян нашей страны.",',
     '"ch7.3_h_005": u"Из-за этого я и дала им шанс переманить дворян нашей страны на свою сторону.",',
     "C-1294-01"),
    (rpath("tools", "ch7_3_ru.py"),
     '"ch7.3_th_404a": u"Принцесса… для той, что всё воспринимает всерьёз, такие минуты наверняка проходят вдвойне тяжело…",',
     '"ch7.3_th_404a": u"Принцесса… для той, что всё воспринимает всерьёз, такие минуты, наверное, проходят тем тяжелее…",',
     "C-1328-01"),

    # ---- сгенерированный tl/russian (зеркало data-packs) ----
    (rpath("game", "tl", "russian", "dialogs.rpy"),
     'new "Как я и опасалась… значит, всё-таки так…"',
     'new "Как я и думала… значит, всё-таки так…"',
     "C-208-01 (tl)"),
    (rpath("game", "tl", "russian", "dialogs.rpy"),
     'new "Казалось бы, Луиза. Однако немало тех, кто сомневается, чего одна королева может добиться."',
     'new "Но знаете, Луиза. Немало есть тех, кто сомневается, чего одна королева может добиться."',
     "C-239-01 (tl)"),
    (rpath("game", "tl", "russian", "dialogs.rpy"),
     'new "Но даже так — преступлений это не оправдывает!"',
     'new "Но даже так — нельзя позволить, чтобы преступление сошло с рук!"',
     "C-588-01 (tl)"),
    (rpath("game", "tl", "russian", "dialogs.rpy"),
     'new "А сперва я расскажу вам кое-что любопытное."',
     'new "А сперва позвольте рассказать вам кое-что любопытное."',
     "C-502-01 (tl)"),
    (rpath("game", "tl", "russian", "dialogs.rpy"),
     'new "Те, кто стоит у них за спиной, — Реконкиста, не так ли."',
     'new "Те, кто стоит у вас за спиной, — Реконкиста, не так ли."',
     "C-1016-01 (tl)"),
    (rpath("game", "tl", "russian", "dialogs.rpy"),
     'new "Но даже если бы мы сумели их придержать — и как же конкретично мы будем спасать Харуну?"',
     'new "Остановить их — это одно. Но вот как конкретно мы спасём Харуну?"',
     "C-1210-01 (tl)"),    (rpath("game", "tl", "russian", "dialogs.rpy"),
     'new "Из-за этого я и дала им шанс увлечь дворян нашей страны."',
     'new "Из-за этого я и дала им шанс переманить дворян нашей страны на свою сторону."',
     "C-1294-01 (tl)"),
    (rpath("game", "tl", "russian", "choises.rpy"),
     'new "Просто так… на всякий случай."',
     'new "Просто так…"',
     "C-105-01 (tl)"),
    (rpath("game", "tl", "russian", "choises.rpy"),
     'new "Но даже так — преступление не оправдание."',
     'new "Но даже так — нельзя позволить преступлению сойти с рук."',
     "C-588-01b (tl)"),
    (rpath("game", "tl", "russian", "thoughs.rpy"),
     'new "Принцесса… для той, что всё воспринимает всерьёз, такие минуты наверняка проходят вдвойне тяжело…"',
     'new "Принцесса… для той, что всё воспринимает всерьёз, такие минуты, наверное, проходят тем тяжелее…"',
     "C-1328-01 (tl)"),

    # ---- EN-база сценария + синхронные old в tl/{japanese,russian} ----
    (rpath("game", "chapters", "7", "script-ch7_2.rpy"),
     'h "The ones standing behind them are Reconquista, are they not.{#ch7.2_h_008}"',
     'h "The ones standing behind you are Reconquista, are they not.{#ch7.2_h_008}"',
     "C-1016-01 (EN)"),
    (rpath("game", "chapters", "7", "script-ch7_3.rpy"),
     'th "Princess… she\'s so serious about everything that moments like this weigh on her all the heavier…{#ch7.3_th_404a}"',
     'th "Princess… she\'s so serious about everything that moments like this must weigh on her all the heavier…{#ch7.3_th_404a}"',
     "C-1328-01 (EN)"),
    (rpath("game", "tl", "japanese", "dialogs.rpy"),
     'old "The ones standing behind them are Reconquista, are they not.{#ch7.2_h_008}"',
     'old "The ones standing behind you are Reconquista, are they not.{#ch7.2_h_008}"',
     "C-1016-01 (old-ja)"),
    (rpath("game", "tl", "russian", "dialogs.rpy"),
     'old "The ones standing behind them are Reconquista, are they not.{#ch7.2_h_008}"',
     'old "The ones standing behind you are Reconquista, are they not.{#ch7.2_h_008}"',
     "C-1016-01 (old-ru)"),
    (rpath("game", "tl", "japanese", "thoughs.rpy"),
     'old "Princess… she\'s so serious about everything that moments like this weigh on her all the heavier…{#ch7.3_th_404a}"',
     'old "Princess… she\'s so serious about everything that moments like this must weigh on her all the heavier…{#ch7.3_th_404a}"',
     "C-1328-01 (old-ja)"),
    (rpath("game", "tl", "russian", "thoughs.rpy"),
     'old "Princess… she\'s so serious about everything that moments like this weigh on her all the heavier…{#ch7.3_th_404a}"',
     'old "Princess… she\'s so serious about everything that moments like this must weigh on her all the heavier…{#ch7.3_th_404a}"',
     "C-1328-01 (old-ru)"),
]


def main():
    apply = "--apply" in sys.argv
    # Фаза 0: проверяем, что каждая замена найдётся РОВНО один раз.
    errors = []
    cache = {}
    for path, old, new, tag in FIXES:
        if path in cache:
            txt = cache[path]
        else:
            txt = io.open(path, encoding="utf-8").read()
            cache[path] = txt
        n = txt.count(old)
        if n != 1:
            errors.append("%s (%s): found %d occurrences of needle" % (path, tag, n))
        if new in txt:
            errors.append("%s (%s): новая строка уже присутствует" % (path, tag))
    if errors:
        print("ERRORS (ничего не записано):")
        for e in errors:
            print("  " + e)
        return 1
    if not apply:
        print("dry-run: %d замен, все находки уникальны. Запуск с --apply запишет." % len(FIXES))
        return 0
    # Фаза 1: применяем (порядок внутри одного файла не конфликтует: замены различны).
    changed = {}
    for path, old, new, tag in FIXES:
        txt = changed.get(path) if path in changed else cache[path]
        txt = txt.replace(old, new, 1)
        changed[path] = txt
        print("ok: %s (%s)" % (os.path.relpath(path, ROOT), tag))
    for path, txt in sorted(changed.items()):
        io.open(path, "w", encoding="utf-8", newline="\n").write(txt)
        print("written: %s" % os.path.relpath(path, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
