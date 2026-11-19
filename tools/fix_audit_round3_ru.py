#!/usr/bin/env python3
"""Round-3 RU fixes, all confirmed against authoritative JA `new` strings.

Each edit is keyed by the {#tag} so a single line cannot drift.
"""
from pathlib import Path
import glob, re

ROOT = Path(__file__).parent.parent

# tag -> (old RU new text, new RU new text)
RU_FIXES = {
 'ch26_s_063': ('Тогда я сам скажу Её Величеству напрямую…',
                'Тогда я сам скажу принцессе напрямую…'),
 'ch26_l_039': ('Если твоё «и» оскорбит принцессу, пострадаем мы!',
                'Если твоё «цуи» оскорбит принцессу, пострадаем мы!'),
 'ch26_l_062': ('Эй — этот театр… Он трясётся, да?',
                'Эй — этот театр… Кажется, он трясётся?'),
 'ch26_l_064': ('Право — вечно действуешь самовольно!',
                'Право — всё время, всё время, всё время действуешь самовольно!'),
 'ch26_s_108': ('Ах, я понимаю. Я чувствую столько злобы…',
                'Ах, я понимаю. Я чувствую такую кровожадность…'),
 'ch26_s_116': ('Из-за Харуны, да? Ах, не волнуйся. Я буду осторожен.',
                'Из-за Харуны, да? Ах, не волнуйся. Я не буду бить в полную силу.'),
 'ch26_d_003': ('Скоро увидишь. Моя интуиция будит. Если хочешь выжить, сражайся по-настоящему.',
                'Скоро увидишь. Моя интуиция гудит. Если хочешь выжить, сражайся по-настоящему.'),
 'ch26_s_122': ('Не Харуна…? Для тебя ты выглядишь точно как Харуна!',
                'Не Харуна…? Для меня ты выглядишь точно как Харуна!'),
 'ch26_ak_014': ('Она спит во мне. Пока я просыпаюсь, Харуна всегда спит.',
                 'Она спит во мне. Пока я не сплю, Харуна всегда спит.'),
 'ch26_s_214': ('Хм — то есть, проще говоря, тело сработало раньше, чем ты успела подумать?',
                'Хм — то есть, проще говоря, тело сработало раньше, чем ты успела успокоиться?'),
}

# tag -> (old EN text, new EN text) for EN base lines that also diverge from JA
EN_FIXES = {
 'ch26_s_063': ('Then I\'ll be blunt with Her Majesty myself…',
                'Then I\'ll be blunt with the princess myself…'),
 'ch26_l_039': ('If your \'just\' offends the princess, we\'re the ones in trouble!',
                'If your \'tsui\' offends the princess, we\'re the ones in trouble!'),
 'ch26_s_214': ('Hmm—so you mean your body moved before you could think, basically?',
                'Hmm—so you mean your body moved before you could calm down, basically?'),
}

def edit_file(path, pairs, field):
    text = path.read_text(encoding='utf-8')
    lines = text.split('\n')
    changed = 0
    for i, line in enumerate(lines):
        m = re.search(r'\{#(\w+)\}', line)
        if not m or m.group(1) not in pairs:
            continue
        old, new = pairs[m.group(1)]
        # the value line for tl is the following line; for scripts it is the same line
        if field == 'tl':
            if i + 1 < len(lines) and old in lines[i + 1]:
                lines[i + 1] = lines[i + 1].replace(old, new)
                changed += 1
        else:
            if old in line:
                lines[i] = line.replace(old, new)
                changed += 1
    if changed:
        path.write_text('\n'.join(lines), encoding='utf-8')
    return changed

for tag, (a, b) in RU_FIXES.items():
    for p in [Path(f) for f in glob.glob(str(ROOT / 'game/tl/russian/*.rpy'))]:
        n = edit_file(p, {tag: (a, b)}, 'tl')
        if n:
            print('RU', tag, '->', p.name)

for tag, (a, b) in EN_FIXES.items():
    for pattern, field in [('game/chapters/2[2-8]/*.rpy', 'script'),
                           ('game/tl/japanese/*.rpy', 'tl'),
                           ('game/tl/russian/*.rpy', 'tl')]:
        for p in [Path(f) for f in glob.glob(str(ROOT / pattern))]:
            n = edit_file(p, {tag: (a, b)}, field)
            if n:
                print('EN', tag, '->', p.name)
