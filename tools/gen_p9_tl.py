# -*- coding: utf-8 -*-
# Генератор TL-блоков для главы 3, части 9 (даты 1064–1083).
# old извлекается из script-ch3_9.rpy по порядку (авто-гарантия точности);
# ja_new — дословно из канона p9_canon.txt (переносы склеены, мысли в （ ）);
# ru_new — по JA. Теги в new не дублируются (конвенция ч. 3).
# Строки: 117 talks (114 голос + 3 без голоса) + 12 choises = 129.
# Запуск: python tools/gen_p9_tl.py           — dry-run (сверка + коллизии)
#         python tools/gen_p9_tl.py --apply   — запись в tl-файлы
import io
import re
import sys

BASE = r'D:/gameMake/ZnT-1/ZnT1'
SCRIPT = BASE + '/game/chapters/3/script-ch3_9.rpy'
CANON = r'C:/Users/user/AppData/Local/Temp/opencode/p9_canon.txt'
TL = {
    'ja': {'dialogs': BASE + '/game/tl/japanese/dialogs.rpy',
           'thoughs': BASE + '/game/tl/japanese/thoughs.rpy',
           'choises': BASE + '/game/tl/japanese/choises.rpy'},
    'ru': {'dialogs': BASE + '/game/tl/russian/dialogs.rpy',
           'thoughs': BASE + '/game/tl/russian/thoughs.rpy',
           'choises': BASE + '/game/tl/russian/choises.rpy'},
}
BUCKETS = ('dialogs', 'thoughs', 'choises')

# (bucket, ru_new) — 129 позиций в порядке строк скрипта (JA — из канона)
R = [
    # ==== SCENE 1064 ====
    ('dialogs', 'А, Сиеста — вот ты где.'),
    ('dialogs', 'Сайто! Как раз кстати!'),
    ('dialogs', 'У тебя ко мне дело?'),
    ('dialogs', 'Да! Есть кое-что, что я очень хочу тебе показать, Сайто!'),
    ('dialogs', 'А? И что же? Уже любопытно.'),
    ('dialogs', 'Пожалуйста, примите этот шарф!'),
    ('dialogs', 'Мне? Шарф ручной вязки… ты уверена? Хм… как-то даже очень приятно.'),
    ('dialogs', 'Я рада, что ты так сказал…'),
    ('dialogs', 'А? Ты же только что подарила мне шарф — так почему ты ещё вяжешь?'),
    ('dialogs', 'Тот, что на спицах, — второй.'),
    ('dialogs', 'Второй!? Только не говори — оба с одинаковым узором?'),
    ('dialogs', 'Да…'),
    ('thoughs', 'Хм-м… дай подумать…'),
    ('choises', 'Это парный лук, да?'),
    ('choises', 'Вот это мастерство.'),
    ('choises', 'Не лучше ли другой узор?'),
    # ==== SCENE 1065 ====
    ('dialogs', 'Это парный лук, да?'),
    ('dialogs', 'А что такое «парный лук»?'),
    ('dialogs', 'Когда двое носят одинаковую одежду — с одним узором, — и ходят вместе.'),
    ('dialogs', 'Как у всех учеников — форма одинаковая, правда?'),
    ('dialogs', 'Нет-нет. Когда все носят одно и то же — это не парный лук.'),
    ('dialogs', 'Смысл в том, что вы — только вдвоём.'),
    ('dialogs', 'Только вдвоём…'),
    # ==== SCENE 1066 ====
    ('dialogs', 'Это уже настоящее мастерство. Луиза тоже вяжет, но у неё так не выходило.'),
    ('dialogs', 'Однажды она подарила мне очень маленький свитер.'),
    ('dialogs', 'Я не проиграю…'),
    ('dialogs', 'А? Что такое, Сиеста?'),
    ('dialogs', 'Да нет, ничего. Совсем ничего~'),
    # ==== SCENE 1067 ====
    ('dialogs', 'А-а, может, другой узор? Ну, как-то неловко же…'),
    ('dialogs', 'Почему неловко?'),
    ('dialogs', 'С одинаковым узором — это, э-э… ну, неловко, но… мне нравится.'),
    ('dialogs', 'Раз тебе нравится — ладно. Только вот… годюсь ли я.'),
    ('dialogs', 'Это не так. …Это моё желание.'),
    # ==== SCENE 1068 ====
    ('dialogs', 'В общем, спасибо за шарф. Теперь зима обещает быть приятной.'),
    ('dialogs', 'Правда? Тогда я свяжу ещё кучу всего! Обязательно берите.'),
    ('dialogs', 'Ладно, договорились. Буду ждать.'),
    ('dialogs', 'Тогда я постараюсь изо всех сил!'),
    # ==== SCENE 1069 ====
    ('dialogs', 'Интересно, Табита тут…?'),
    ('dialogs', 'А, вот она. С фамильяром Сильфидой.'),
    ('dialogs', 'Выходит, Табита с удовольствием заботится о Сильфиде…'),
    ('dialogs', 'Значит, вот что называют идеальной связью между фамильяром и хозяином…'),
    ('thoughs', 'А уж моя госпожа Луиза…'),
    ('dialogs', '…Ты тут был?'),
    ('dialogs', 'А, Табита!? Прости-прости. Просто наблюдал немного.'),
    ('dialogs', 'Дурной вкус.'),
    ('dialogs', 'Табита да Сильфида так весело проводили время, что я поскупился поздороваться.'),
    ('dialogs', 'И ты понял?'),
    ('dialogs', 'Понял что — что вам было весело?'),
    ('dialogs', 'Угу.'),
    ('dialogs', 'Ну, да…'),
    ('choises', 'Я ведь тоже фамильяр!'),
    ('choises', 'Не смогу объяснить — просто понимаю.'),
    ('choises', 'Это видно по твоему лицу.'),
    # ==== SCENE 1070 ====
    ('dialogs', 'Я ведь тоже фамильяр — тут и понять не трудно.'),
    ('dialogs', 'Наобум.'),
    ('dialogs', 'Ага, раскусила…'),
    ('dialogs', 'Но то, что Табита и Сильфида ладят, — это видно любому.'),
    # ==== SCENE 1071 ====
    ('dialogs', 'Не смогу объяснить — просто понимаю.'),
    ('dialogs', 'Основания слабые.'),
    ('dialogs', 'Когда так указывают — я в замешательстве.'),
    ('dialogs', 'Но, глядя на Табиту с Сильфидой, я всё же чувствовал — вам весело.'),
    # ==== SCENE 1072 ====
    ('dialogs', 'Это видно по твоему лицу.'),
    ('dialogs', '…Врёшь.'),
    ('dialogs', 'Как будто я вру!'),
    ('dialogs', 'Я подумал — Сильфида, кажется, тот, рядом с кем Табита может расслабиться.'),
    # ==== SCENE 1073 ====
    ('dialogs', 'Но… подглядывать — дурно.'),
    ('dialogs', 'Прости-прости. Не буду мешать — можно ещё немного понаблюдать?'),
    ('dialogs', '…'),
    ('dialogs', 'Всё-таки нельзя? Вижу — Табите весело, и я сам настраиваюсь на хорошую волну.'),
    ('dialogs', '…Ладно.'),
    ('dialogs', 'Понял. Спасибо.'),
    # ==== SCENE 1074 ====
    ('dialogs', 'Кирхе, ты здесь?'),
    ('dialogs', 'А, Дорогой! Как раз кстати пришёл.'),
    ('dialogs', 'А, ты не в форме. Кирхе без формы — совсем другой вид.'),
    ('dialogs', 'Ну и ну, какие приятные слова. Хвалить платье — азбука общения с девушками.'),
    ('dialogs', 'Кстати — угадай, почему я так нарядилась?'),
    ('dialogs', 'Почему? Ну, это же…'),
    ('choises', 'Эксгибиционистка, что ли?'),
    ('choises', 'Чтобы снять стресс?'),
    ('choises', 'Желание быть кем-то другим?'),
    # ==== SCENE 1075 ====
    ('dialogs', 'Эксгибиционистка, что ли?'),
    ('dialogs', 'Эксгибиционистка — как невежливо. Но-но — раз Дорогой желает, я готова обнажаться хоть когда.'),
    ('dialogs', 'Н-нет, я в порядке.'),
    ('dialogs', 'Ну и неинтересный же ты~'),
    ('dialogs', 'Правильный ответ — снять стресс. Униформа всё-таки стесняет, правда? И стресс копится-копится…'),
    # ==== SCENE 1076 ====
    ('dialogs', 'Чтобы снять стресс?'),
    ('dialogs', 'Именно так, Дорогой! Академическая униформа так стесняет, что моё тело в неё не умещается…'),
    ('dialogs', '…Да, действительно стесняет.'),
    ('dialogs', 'А носить её нужно постоянно — и стресс копится и копится…'),
    # ==== SCENE 1077 ====
    ('dialogs', 'Желание быть кем-то другим?'),
    ('dialogs', 'Мм~ Не мимо, но и не в точку?'),
    ('dialogs', 'Ну, я сдаюсь.'),
    ('dialogs', 'Правильный ответ — снять стресс. Униформа всё-таки стесняет, правда? И стресс копится-копится…'),
    # ==== SCENE 1078 ====
    ('dialogs', 'Вот изредка я и надеваю что-то другое… А Луиза такого не делает?'),
    ('dialogs', 'Луиза? У неё в комнате одежды хватает.'),
    ('dialogs', 'В академии я вижу её почти всегда либо в форме, либо в пижаме.'),
    ('dialogs', 'Понятно. Тебе тоже нелегко, Сайто.'),
    ('dialogs', 'П-правда?'),
    ('dialogs', 'Как надоест Луиза — сразу ко мне. Я всегда жду!'),
    ('dialogs', 'Ха-ха-ха-ха…'),
    # ==== SCENE 1079 ====
    ('dialogs', 'Слушай, Харуна. Не выйти ли нам во двор?'),
    ('dialogs', 'Ладно, почему нет.'),
    ('dialogs', 'У меня есть кое-что, что я хотел тебе показать.'),
    ('dialogs', 'Ого, что же это? Уже не терпится~'),
    ('dialogs', 'Вот что я хотел тебе показать, Харуна.'),
    ('dialogs', 'Это самолёт? Похож на нулевой истребитель… Это же не настоящий, да?'),
    ('dialogs', 'Настоящий. Этот нулевой истребитель прибыл в этот мир из Японии.'),
    ('dialogs', 'Правда?! Из Японии — сюда?'),
    ('dialogs', 'Ага. Он принадлежит прадеду Сиесты — говорят, он на нём попал в этот мир.'),
    ('dialogs', 'Значит, мы не единственные, кто оказался в этом мире…'),
    ('dialogs', 'Но чтобы кто-то вернулся — такого я ещё не слышала…?'),
    ('dialogs', 'Это…'),
    ('choises', 'Тут ничего не сделаешь.'),
    ('choises', 'Может, мы просто не знаем.'),
    ('choises', 'Мы будем первыми, кто вернётся.'),
    # ==== SCENE 1080 ====
    ('dialogs', 'Тут ничего не сделаешь.'),
    ('dialogs', 'А почему это?'),
    ('dialogs', 'Если вернуться в родной мир, то, может, и не останется средств сообщить в этот мир об успехе? С этой точки зрения — ничего не сделаешь.'),
    ('dialogs', 'Разве это не слишком оптимистично?'),
    ('dialogs', 'Но всё равно гораздо лучше, чем просто сдаться, нет?'),
    # ==== SCENE 1081 ====
    ('dialogs', 'Может, мы просто этого не знаем?'),
    ('dialogs', 'Но ведь можно и не вернуться.'),
    ('dialogs', 'Поэтому, если уж представится случай — я хочу всё увидеть.'),
    # ==== SCENE 1082 ====
    ('dialogs', 'Надо только стать первыми вернувшимися.'),
    ('dialogs', 'Да. Здорово бы, если получится… только получится ли?'),
    ('dialogs', 'Судя по всему, в этот мир попадает кое-что из нашего мира.'),
    ('dialogs', 'Быть может, когда-нибудь мы найдём кое-что полезное для возвращения.'),
    # ==== SCENE 1083 ====
    ('dialogs', 'Верно. Шанс вернуться не равен нулю — так что пока не стоит сдаваться…'),
    ('dialogs', '…Ага. Именно.'),
]


def parse_script():
    txt = io.open(SCRIPT, encoding='utf-8').read()
    items = []
    for line in txt.splitlines():
        m = re.match(r'^\s+(s|l|ha|k|si|t|th) "([^"]*)"$', line)
        if m:
            kind = 'thoughs' if m.group(1) == 'th' else 'dialogs'
            items.append((kind, m.group(2)))
            continue
        m = re.match(r'^\s+"([^"]*)":$', line)
        if m and not m.group(1).startswith('{"char"'):
            items.append(('choises', m.group(1)))
    return items


def load_canon():
    items = []
    for line in io.open(CANON, encoding='utf-8'):
        line = line.rstrip('\n')
        m = re.match(r'^  TALK (\S+) \| v=(\S+) \| (.*)$', line)
        if m:
            # мысли сайта — без голоса (канон: サイト, v=NONE); остальное — реплики
            kind = 'thoughs' if (m.group(1) == 'サイト' and m.group(2) == 'NONE') \
                else 'dialogs'
            items.append((kind, m.group(3)))
            continue
        m = re.match(r'^  KICK 【選択肢】(.+?) → scene \d+$', line)
        if m:
            items.append(('choises', m.group(1)))
    return items


def fmt_pair(old, new):
    return '\n    old "%s"\n    new "%s"\n' % (old, new)


def main():
    apply = '--apply' in sys.argv
    items = parse_script()
    canon = load_canon()
    print('script items:', len(items), ' canon items:', len(canon),
          ' translations:', len(R))
    if not (len(items) == len(canon) == len(R)):
        print('COUNT MISMATCH')
        return 1
    pairs = []
    for i, ((skind, sold), (ckind, cja), (rbucket, rru)) in enumerate(
            zip(items, canon, R), 1):
        if skind != ckind:
            print('KIND MISMATCH #%d: script=%s canon=%s (%r)'
                  % (i, skind, ckind, sold))
            return 1
        if skind != rbucket:
            print('BUCKET MISMATCH #%d: script=%s ru=%s (%r)'
                  % (i, skind, rbucket, sold))
            return 1
        pairs.append((rbucket, sold, cja, rru))
    # уникальность olds внутри набора
    olds = [p[1] for p in pairs]
    dup = sorted({o for o in olds if olds.count(o) > 1})
    if dup:
        print('DUP IN SET:')
        for d in dup:
            print(' ', repr(d))
        return 1
    # коллизии с уже существующими парами (все 3 бакета, оба языка)
    coll = []
    for lang in ('ja', 'ru'):
        content = {b: io.open(TL[lang][b], encoding='utf-8').read()
                   for b in BUCKETS}
        for b, old, _ja, _ru in pairs:
            if '    old "%s"\n' % old in content[b]:
                coll.append((lang, b, old))
    if coll:
        print('COLLISIONS WITH EXISTING:')
        for c in coll:
            print(' ', c[0], c[1], repr(c[2]))
        return 1
    if not apply:
        print('dry-run OK (no write). Use --apply to write.')
        return 0
    counts = {}
    for lang in ('ja', 'ru'):
        for b, old, ja, ru in pairs:
            new = ja if lang == 'ja' else ru
            with io.open(TL[lang][b], 'a', encoding='utf-8', newline='\n') as f:
                f.write(fmt_pair(old, new))
            counts[(lang, b)] = counts.get((lang, b), 0) + 1
    print('written:', dict(counts))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
