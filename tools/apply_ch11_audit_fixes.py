#!/usr/bin/env python3
"""Analyzer Phase 2 decisions for chapter 11 (parts 3-4), applied to RU `new`.

Each key is the {#tag} of an EN string; value is the corrected RU string.
Only `new` lines change — `old` stays byte-identical, so JA/RU TL remain in sync.
Decisions and JA grounds are in reports/sma/ch11/{3,4}/analysis/*.phase2.md.
"""
import re

FIXES = {
    3: {
        'ch11_s_044': 'Что-то здесь не так, правда?',
        'ch11_ha_033': ('Мы только что вышли из театра, а уже накатывает какая-то '
                        'ностальгия… / Или это только мне так кажется?'),
        'ch11_w_009': 'Ты потрудилась на задании… спасибо.',
        'ch11_w_010': 'Понятно. Похоже, Акина ещё не проснулась.',
        'ch11_w_013': 'Фу-фу-фу. Впрочем, поверишь ты или нет — неважно.',
        'ch11_w_021': ('Чёрт, эта скорость! И это сопротивление… неужели сила Акины '
                       'начинает просыпаться?'),
        'ch11_l_016': 'Хм! Что за поведение!',
        'ch11_l_015': 'Мы знали её так недолго… / а теперь без неё так одиноко.',
        'ch11_k_012': 'Ну-ну, Луиза всегда была такой простой и прямолинейной…',
        'ch11_w_025': 'Ну же, спи. Отдохни своё измученное тело.',
        'ch11_l_020': 'Г-Госпожу игнорируете, между прочим! Глупый пёс!',
        'ch11_s_054': 'Луиза тоже какая-то не в форме по сравнению с обычным.',
    },
    4: {
        'ch11_s_098': 'С чего ты давно злишься? Ты всё время дуешься.',
        'ch11_w_031': 'Ну, кто знает…',
        'ch11_w_032': ('Мы встретились сразу после такого трогательного прощания, '
                       'так что, уверена, она просто смущается.'),
        'ch11_s_110': 'Так, когда она так прижимает, моё… э-э… взрослое обаяние…',
        'ch11_l_046': 'Ч-Что ты думаешь! Глупый пёс!',
        'ch11_w_037': 'Не обязательно быть такой сухой, правда?',
        'ch11_w_039': 'Фу-фу, интересно, заметила ли она?',
        'ch11_l_054': 'И вдобавок она стала нас выспрашивать… Это странно.',
    },
}


def main():
    for part, fixes in FIXES.items():
        path = 'game/tl/russian/ch11_%d_dialogs.rpy' % part
        lines = open(path, encoding='utf-8').read().split('\n')
        current_tag = None
        changed = 0
        for i, line in enumerate(lines):
            m = re.match(r'\s+old ".*\{#([^}]+)\}"\s*$', line)
            if m:
                current_tag = m.group(1)
                continue
            m = re.match(r'(\s+new ")(.*)(")\s*$', line)
            if m and current_tag in fixes:
                new = fixes[current_tag]
                assert '"' not in new, current_tag
                lines[i] = m.group(1) + new + m.group(3)
                changed += 1
                current_tag = None
        open(path, 'w', encoding='utf-8').write('\n'.join(lines))
        print('part %d: %d/%d fixes applied to %s' %
              (part, changed, len(fixes), path))
        assert changed == len(fixes), 'some tags not found'


if __name__ == '__main__':
    main()
