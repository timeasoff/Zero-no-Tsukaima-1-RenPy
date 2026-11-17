#!/usr/bin/env python3
"""Write Analyzer Phase 2 decision reports for ch11 parts 3 and 4."""
import json

RUN = '20261117-221000-ch11'
P3 = [
    ('114', 'ch11_s_044', 'A,C', 'なにか変だな？', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'Что-то здесь не так.', 'Что-то здесь не так, правда?',
     'JA な？ — внутренний вопрос; RU была констатация. Оба аудитора сошлись.'),
    ('274', 'ch11_ha_033', 'A,F1', '懐かしい', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', '…будто прошла вечность…', '…уже накатывает какая-то ностальгия…',
     '懐かしい = ностальгия, а не ощущение долгого времени; подмена эмоции.'),
    ('281', 'ch11_w_009', 'C', 'ご苦労だったわね', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'Ты справилась с заданием.', 'Ты потрудилась на задании… спасибо.',
     'От перечня факта к акту признания труда (покровительственный тон).'),
    ('291', 'ch11_w_010', 'C', 'ようね', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'Значит, Акина ещё не проснулась.', 'Похоже, Акина ещё не проснулась.',
     'よう = осторожное «похоже», «Значит» делало вывод фактом.'),
    ('322', 'ch11_w_013', 'A', 'ふふふ', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'Хи-хи-хи.', 'Фу-фу-фу.',
     'ふふふ — сдержанный смех; «хи-хи» передаёт другой смех (ひひひ).'),
    ('373', 'ch11_w_021', 'C', 'のか', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'сила Акины просыпается!', 'неужели сила Акины начинает просыпаться?',
     'か = подозрение-вопрос; かけている = «начинает, в процессе».'),
    ('52', 'ch11_l_016', 'A', '態度', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'Что за тон!', 'Что за поведение!',
     '態度 — отношение/поведение в целом, не только манера говорить.'),
    ('31', 'ch11_l_015', 'A', '寂しい', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'без неё так пусто', 'без неё так одиноко',
     '寂しい — переживание одиночества, не описание пустого места.'),
    ('224', 'ch11_k_012', 'A,F1', '単純まっすぐ', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'всегда была прямолинейна', 'всегда была такой простой и прямолинейной',
     'Утрачен компонент 単純 (простодушие).'),
    ('486', 'ch11_w_025', 'A', '疲れきった', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'уставшее тело', 'измученное тело',
     'きる — полное изнеможение, важное для сцены гипноза.'),
    ('145', 'ch11_l_020', 'F1', 'ご主人様', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'Г-Господина своего', 'Г-Госпожу',
     'Луиза — женщина; dictionary.md: ご主人様 → «госпожа». Родовое рассогласование.'),
    ('537', 'ch11_s_054', 'F1', '元気がない', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'невесёлая', 'не в форме',
     '元気 — самочувствие/энергия, а не настроение.'),
    ('873', 'ch11_s_086', 'F1', '情けない', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'FALSE_POSITIVE', 'PRESERVED', 'Было бы обидно…', 'Было бы обидно…',
     'В контексте Сайто «обидно» передаёт его самоироничное сожаление; '
     'грамотная замена эмоционального регистра, смысл сохранён.'),
]
P4 = [
    ('32', 'ch11_s_098', 'A', 'さっきから / ずっと', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'С чего ты вдруг злишься?', 'С чего ты давно злишься?',
     'さっきから/ずっと — длительность, а не внезапность (влияние EN "all of a sudden").'),
    ('122', 'ch11_w_031', 'C', 'さあ？', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'Ну?', 'Ну, кто знает…',
     'Уклонение от ответа, а не побуждение собеседника продолжить.'),
    ('127', 'ch11_w_032', 'C', 'きっと … のよ', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'она, наверное, смущается', 'уверена, она просто смущается',
     'きっと … のよ — утвердительная окраска; «наверное» ослабляло её.'),
    ('235', 'ch11_s_110', 'A', 'そ、…お、', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'Когда она так прижимает, моё взрослое', 'Так, … моё… э-э… взрослое',
     'Запинки сохранены в соседних репликах; здесь утрачена комическая растерянность.'),
    ('249', 'ch11_l_046', 'F1', 'な、', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'О чём ты думаешь!', 'Ч-Что ты думаешь!',
     'な、 — запинка; EN сохранило "W-What", RU — нет.'),
    ('267', 'ch11_w_037', 'A,F1', '固いこと', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'такой строгой', 'такой сухой',
     '固い — официальность/скованность, не требовательность.'),
    ('329', 'ch11_w_039', 'C', 'かな', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'Хи-хи, она заметила?', 'Фу-фу, интересно, заметила ли она?',
     'かな — размышление вслух; прямой вопрос менял адресата. Смех сверен с ふふ.'),
    ('404', 'ch11_l_054', 'A,F1', 'おかしい', 'NOT_IN_SOURCE', 'NOT_IN_SOURCE',
     'CONFIRMED_ERROR', 'FIXED', 'Это подозрительно.', 'Это странно.',
     'おかしい мягче, чем 怪しい в предыдущей реплике; различие утрачено.'),
]

FIELDS = ('line', 'tag', 'inputs', 'ja', 'classification', 'disposition',
          'status', 'action', 'before', 'after', 'reason')


def report(part, rows, phase1, audits):
    findings = [dict(zip(FIELDS, r)) for r in rows]
    obj = {
        'analysis_id': RUN + '-p%d' % part,
        'part': 'ch11_%d' % part,
        'phase': 2,
        'inputs': {'phase1': phase1, 'a_runs': audits['a'], 'c_runs': audits['c'],
                   'precheck': 'reports/sma/ch11/%d/precheck/' % part},
        'findings': findings,
    }
    fixed = sum(1 for r in rows if r[7] == 'FIXED')
    preserved = sum(1 for r in rows if r[7] == 'PRESERVED')
    text = [
        '# Analyzer — Фаза 2 (evidence review), ch11_%d' % part,
        '',
        '- analysis_id: `%s`' % obj['analysis_id'],
        '- Дата: 2026-11-17',
        '- Вход: Фаза 1 `%s`; A `%s`; C `%s`; precheck каталог.' % (
            phase1, ', '.join(audits['a']), ', '.join(audits['c'])),
        '- Каждый кандидат проверен по JA напрямую. Итог: %d CONFIRMED_ERROR → FIXED, '
        '%d FALSE_POSITIVE → PRESERVED.' % (fixed, preserved),
        '',
        '## Решения',
        '',
        '| Строка | Тег | JA | Статус |_disposition|',
        '|---|---|---|---|---|',
    ]
    for r in rows:
        text.append('| %s | %s | %s | %s | %s |' %
                    (r[0], r[1], r[3], r[6], r[7]))
    text += ['', '## Детали', '']
    for r in rows:
        text.append('- **%s / %s** (%s): JA `%s`. %s → %s. %s' %
                    (r[0], r[1], r[2], r[3], r[6], r[7], r[10]))
    text += ['', '## JSON', '', '```json',
             json.dumps(obj, ensure_ascii=False, indent=2), '```', '']
    path = 'reports/sma/ch11/%d/analysis/%s-p%d.md' % (part, RUN, part)
    open(path, 'w', encoding='utf-8').write('\n'.join(text))
    print('wrote', path, 'findings', len(rows))


if __name__ == '__main__':
    report(3, P3, 'reports/sma/ch11/3/analysis/20261117-220211-8996.phase1.md',
           {'a': ['reports/sma/ch11/3/a/20261117-220052-14cc.md'],
            'c': ['reports/sma/ch11/3/c/20261117-220035-53e2.md']})
    report(4, P4, 'reports/sma/ch11/4/analysis/20261117-220245-13a1.phase1.md',
           {'a': ['reports/sma/ch11/4/a/20261117-220052-c730.md'],
            'c': ['reports/sma/ch11/4/c/20261117-220053-5669.md']})
