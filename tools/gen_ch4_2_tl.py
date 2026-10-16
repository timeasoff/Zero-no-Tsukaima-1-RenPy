# -*- coding: utf-8 -*-
# Генератор TL-блоков для главы 4, части 2 (сцены 225–235 + дата 1342–1346).
# old извлекается из script-ch4_2.rpy по порядку (авто-гарантия точности);
# ja_new — дословно из канона ch4_canon_p2.txt (переносы склеены, мысли в （ ）);
# ru_new — по JA. Теги в new не дублируются (конвенция ч. 3/ч. 4).
# Строки: 125 голосов + 8 мыслей + 6 choises меню + 6 choises 【移動】-хаба = 145.
# Особенности: (1) хаб-пункты читаются из dict-литералов choices.append;
# (2) канон группируется по сценам и выдаётся в SCENE_ORDER (дата 1342–1346
# стоит в скрипте перед сценой 231, а в источнике — в конце); к 5 【移動】
# добавляется служебный Leave (JA «出発する», target moveInit = сцена 231).
# Запуск: python tools/gen_ch4_2_tl.py           — dry-run (сверка + коллизии)
#         python tools/gen_ch4_2_tl.py --apply   — запись в tl-файлы
import io
import re
import sys

BASE = r'D:/gameMake/ZnT-1/ZnT1'
SCRIPT = BASE + '/game/chapters/4/script-ch4_2.rpy'
CANON = r'C:/Users/user/AppData/Local/Temp/opencode/ch4_canon_p2.txt'
TL = {
    'ja': {'dialogs': BASE + '/game/tl/japanese/dialogs.rpy',
           'thoughs': BASE + '/game/tl/japanese/thoughs.rpy',
           'choises': BASE + '/game/tl/japanese/choises.rpy'},
    'ru': {'dialogs': BASE + '/game/tl/russian/dialogs.rpy',
           'thoughs': BASE + '/game/tl/russian/thoughs.rpy',
           'choises': BASE + '/game/tl/russian/choises.rpy'},
}
BUCKETS = ('dialogs', 'thoughs', 'choises')

# Порядок сцен в СКРИПТЕ (дата Луизы стоит перед сценой 231).
SCENE_ORDER = [225, 1342, 1343, 1344, 1345, 1346, 231, 232, 233, 234, 235]
LEAVE_JA = '出発する'  # служебный пункт хаба (leave-цель moveInit = сцена 231)

# (bucket, ru_new) — 145 позиций в порядке строк скрипта (JA — из канона)
R = [
    # ==== SCENE 225 ====
    ('dialogs', 'Как-то тяжело на душе. Вдруг вызвали именно меня. Что бы это могло быть?'),
    ('dialogs', 'Если даже ректор не знает, может, она хочет обсудить что-то личное?'),
    ('dialogs', 'Не может быть. Её Высочество не стала бы вызывать меня ради чего-то личного.'),
    ('dialogs', 'Э-э… Господа, о чём вообще был тот разговор?'),
    ('dialogs', 'А, Луиза, можно рассказать Сиесте то, о чём мы говорили?'),
    ('dialogs', 'Почему бы и нет? Она всё равно скоро узнает.'),
    ('dialogs', 'Понимаешь, Её Высочество вызвала меня и Луизу. И мы отправляемся в Тристанию.'),
    ('dialogs', 'Что, к Её Величеству королеве!?'),
    ('dialogs', 'Э-эй, слишком громко. Слушай, это секрет, только между нами.'),
    ('dialogs', 'Да, поняла.'),
    ('dialogs', 'И ещё, ректор попросил представить Харуну Её Величеству, так что Харуна едет с нами.'),
    ('dialogs', 'Вот как…'),
    ('dialogs', 'Э-э… Луиза-сан.'),
    ('dialogs', 'Что такое, Харуна?'),
    ('dialogs', 'Луиза-сан, вы знакомы с Её Величеством королевой?'),
    ('dialogs', 'Да. В детстве я была у Её Высочества партнёром по играм.'),
    ('dialogs', 'То есть, иначе говоря, вы с Её Высочеством подруги детства?'),
    ('dialogs', 'Ну, выходит, что так. Но не болтай об этом попусту.'),
    ('dialogs', 'Её Высочество теперь королева, которая держит на себе целую страну.'),
    ('dialogs', 'Простому дворянину или простолюдину не позволено обращаться к ней так запросто.'),
    ('dialogs', 'Но настоящая проблема — зачем нас вызвали.'),
    ('dialogs', 'Думаешь, всё-таки из-за Харуны?'),
    ('dialogs', 'Ч-что, из-за меня…?'),
    ('dialogs', 'Хм, пока не знаю. Но, похоже, распоряжения ректора уладят это мирно…'),
    ('dialogs', '…'),
    ('dialogs', 'Всё будет хорошо, Харуна. Если что, я тебя защищу.'),
    ('dialogs', 'О-хо, как и ожидалось от моего напарника. Ну и крут же ты.'),
    ('dialogs', 'П-погоди. Нельзя устраивать беспорядок в королевском дворце.'),
    ('dialogs', 'Да говорю же, всё будет хорошо. Это был просто пример.'),
    ('dialogs', 'Ох уж…'),
    ('dialogs', 'Э-э… Госпожа Вальер.'),
    ('dialogs', 'Сиеста, что такое?'),
    ('dialogs', 'А что будет со мной?'),
    ('dialogs', 'Ах, об этом. Сиеста, я попрошу тебя остаться и присмотреть за комнатой.'),
    ('dialogs', 'Что!? Значит, мне нельзя поехать?'),
    ('dialogs', 'Нельзя. Те, кого вызвало Её Величество, — это я и Сайто. Харуна едет по делам ректора.'),
    ('dialogs', 'У тебя ведь нет там дел, Сиеста? Мы не можем раздувать свиту без причины.'),
    ('dialogs', 'Это…'),
    ('dialogs', 'Может, возьмём хотя бы Сиесту? Ну, чтобы за нами присматривала…'),
    ('dialogs', 'Нет.'),
    ('dialogs', 'Сайто-сан, спасибо. Но госпожа Вальер права. Тогда я останусь.'),
    ('dialogs', 'Сиеста…'),
    ('dialogs', 'Что ж, у меня ведь тоже есть работа. Позвольте откланяться.'),
    ('dialogs', 'Тогда давайте на этом разойдёмся. Собираемся у кареты.'),
    ('dialogs', 'Понял.'),
    ('dialogs', 'Да.'),
    ('thoughs', 'Ну что ж, чем бы мне заняться…'),
    # ---- 【移動】-хаб (сцена 225) ----
    ('choises', 'Комната Луизы'),
    ('choises', 'Кухня'),
    ('choises', 'Двор'),
    ('choises', 'Коридор'),
    ('choises', 'Комната Луизы'),
    ('choises', 'Отправиться'),
    # ==== SCENES 1342–1346 (дата Луизы) ====
    ('dialogs', 'Эй, чего ты всё разбросала? Пол в одежде.'),
    ('dialogs', 'Погоди, Сайто! Если у тебя есть время стоять и глазеть, помоги!'),
    ('dialogs', 'Луиза, чем ты только что занималась? Я свои сборы давно закончил.'),
    ('dialogs', 'Девушке нужно много всего, чтобы собраться.'),
    ('dialogs', 'К тому же в последнее время я всё оставляла на тебя, так что уже не знаю, где что лежит…'),
    ('thoughs', 'Вот что получается, когда всё на меня сваливают.'),
    ('choises', 'Помочь ей.'),
    ('choises', 'Не хочу помогать.'),
    ('choises', 'Помогу, но с одним условием.'),
    ('dialogs', 'Ладно, помогу.'),
    ('dialogs', 'Правда?'),
    ('dialogs', 'Так это никогда не закончится.'),
    ('dialogs', 'Раз уж у меня хорошее настроение, помогай молча!'),
    ('dialogs', 'А-а, значит, помогаю я.'),
    ('dialogs', 'Это приказ твоей госпожи. Без возражений.'),
    ('dialogs', 'Я не против помочь, но… у меня есть одно условие.'),
    ('dialogs', 'Условие? Ну-ка скажи, на всякий случай.'),
    ('dialogs', 'Хочу, чтобы к ужину добавили одно блюдо… вот так. Нельзя?'),
    ('dialogs', 'Отказано. Будешь молоть чепуху — вовсе оставлю без ужина!'),
    ('dialogs', 'Да-да, понял. Так что осталось?'),
    ('dialogs', 'Смена одежды…'),
    ('dialogs', 'Понятно. Раз ты никогда не убираешь, не знаешь, где что лежит.'),
    ('dialogs', 'У-у.'),
    ('dialogs', 'Э-э, на сколько дней тебе нужно?'),
    ('dialogs', '…Э-это. Дней на два-три, самое большее… хватит… наверное…'),
    ('dialogs', 'Да-да, дня на три. Кроме школьной формы, другая одежда нужна?'),
    ('dialogs', 'М-может, и нужна…'),
    ('dialogs', 'У тебя жар? Лицо ведь красное, знаешь?'),
    ('dialogs', 'Да помолчи! П-просто поскорее уложи!'),
    ('dialogs', 'Я и без указаний уложу как следует.'),
    ('dialogs', 'Хотя, странно говорить это парню, в последнее время я неплохо наловчился складывать одежду.'),
    ('dialogs', 'Смотри, Луиза. Вот так складываю, вот так разглаживаю.'),
    ('dialogs', 'Даже если бы я сказал, что это сделала девушка, сошло бы.'),
    ('dialogs', 'А эта белизна ткани. Можно сказать — шедевр ручной стирки.'),
    ('dialogs', 'Хватит уже! Я-я, ах, дальше я сама! Выйди из этой комнаты немедленно!'),
    ('dialogs', 'Что с тобой, Луиза? Я чем-то тебя обидел?'),
    ('dialogs', 'Н-ничем. Говорю же, я сама в конце концов сделаю.'),
    ('thoughs', 'Что же с ней такое творится?'),
    # ==== SCENE 231 ====
    ('dialogs', 'Итак, госпожа Вальер. Будьте осторожны в пути.'),
    ('dialogs', 'Да. Благодарю вас, мистер Кольбер.'),
    ('dialogs', 'Будьте внимательны в пути. Если что-то случится — сразу посылайте весть.'),
    ('dialogs', 'Поняла. Благодарю за то, что приготовили для нас такую прекрасную карету.'),
    ('dialogs', 'Хм, благодарности не нужны.'),
    ('dialogs', 'Ну же, Её Величество наверняка ждёт вас с нетерпением. Поезжайте и будьте осторожны.'),
    ('dialogs', 'Да, тогда мы отправимся.'),
    ('dialogs', 'Сайто-кун, прошу тебя позаботиться об этих двоих.'),
    ('dialogs', 'Да, постараюсь.'),
    ('dialogs', 'Харуна-кун, на месте следуйте указаниям госпожи Вальер и Сайто-куна.'),
    ('dialogs', 'Да, поняла.'),
    ('dialogs', 'Ну, давайте садиться в карету.'),
    ('thoughs', 'Так, об этой карете — сиденья там двухместные, друг напротив друга…'),
    ('thoughs', 'Луиза и Харуна сидят друг напротив друга. Так, с чьей стороны мне сесть…'),
    ('dialogs', 'Чего ты встал? Ну же, садись скорее рядом со мной!'),
    ('dialogs', 'Хирага-кун, рядом со мной тоже можно? Нехорошо, что Луиза-сан там теснится.'),
    ('dialogs', 'А, что же мне делать…'),
    ('choises', 'Сесть рядом с Луизой.'),
    ('choises', 'Сесть рядом с Харуной.'),
    ('choises', 'Мяться, не решаясь выбрать место.'),
    # ==== SCENE 232 ====
    ('dialogs', 'Ну что ж, тогда, пожалуй, сяду рядом с Луизой?'),
    ('dialogs', 'Т-то есть как!? Э-это… это же совершенно нормально, да.'),
    ('dialogs', 'Мм…'),
    ('thoughs', 'А-а… Харуна, почему ты так печально отводишь взгляд…'),
    # ==== SCENE 233 ====
    ('dialogs', 'Хорошо, тогда сяду рядом с Харуной.'),
    ('dialogs', 'Что-что! Всё равно… всё равно! Делай как хочешь, Сайто, вот и всё!'),
    ('dialogs', 'А? Чего ты злишься?'),
    ('dialogs', 'Тебя это не касается, Сайто.'),
    # ==== SCENE 234 ====
    ('thoughs', 'С чьей стороны сесть… Похоже, с кем бы я ни сел, кого-то задену.'),
    ('dialogs', 'Да определись уже наконец! Или тебя лучше погрузить вместе с остальным багажом?'),
    ('dialogs', 'Только не это, прошу.'),
    # ==== SCENE 235 ====
    ('dialogs', 'Кровопролитие.'),
    ('dialogs', 'А-а. Дорогой, скрываться вот так — как холодно с твоей стороны.'),
    ('dialogs', 'Кирхе, Табита.'),
    ('dialogs', 'Эй, про нас тоже не забывай.'),
    ('dialogs', 'Гиш, Монмон.'),
    ('dialogs', 'Говорю же, не Монмон. Ты ведь это назло?'),
    ('dialogs', 'Н-нет, прости. Но почему вы все здесь?'),
    ('dialogs', 'Пришли тебя проводить. Думаю, посмотрю на ваше отправление.'),
    ('dialogs', 'Вот как. Спасибо.'),
    ('dialogs', 'Дёрг-дёрг.'),
    ('dialogs', 'А? Что такое, Табита?'),
    ('dialogs', 'Ты, сюда.'),
    ('dialogs', '???'),
    ('dialogs', 'Ты и ты, сюда.'),
    ('dialogs', '???'),
    ('dialogs', 'Табита говорит, что Луизе и Харуне лучше сесть вместе, а ты, дорогой, напротив.'),
    ('dialogs', 'Так они будут на равных.'),
    ('dialogs', 'А, вот оно что. Спасибо, Табита. Надо же, всё оказалось просто.'),
    ('dialogs', '…'),
    ('dialogs', '…'),
    ('dialogs', 'Тогда, все, мы поехали.'),
    ('dialogs', 'Постарайтесь там.'),
    ('thoughs', 'И вот так мы наконец отправились из Академии магии.'),
]


def parse_script():
    txt = io.open(SCRIPT, encoding='utf-8').read()
    items = []
    for line in txt.splitlines():
        m = re.match(r'^\s+(s|l|ha|k|si|t|th|c|o|g|m|d) "([^"]*)"$', line)
        if m:
            kind = 'thoughs' if m.group(1) == 'th' else 'dialogs'
            items.append((kind, m.group(2)))
            continue
        m = re.match(r'^\s+"([^"]*)":$', line)
        if m and not m.group(1).startswith('{"char"'):
            items.append(('choises', m.group(1)))
            continue
        m = re.search(r'\{\s*(?:"char":\s*"[^"]*",\s*)?"text":\s*"([^"]*)"',
                      line)
        if m and line.lstrip().startswith('$ choices.append'):
            items.append(('choises', m.group(1)))
    return items


def load_canon():
    scenes = {}
    cur = None
    for line in io.open(CANON, encoding='utf-8'):
        line = line.rstrip('\n')
        m = re.match(r'^SCENE (\d+) \(line (\d+)\)$', line)
        if m:
            cur = int(m.group(1))
            scenes.setdefault(cur, [])
            continue
        if cur is None:
            continue
        m = re.match(r'^  TALK (\S+) \| v=(\S+) \| (.*)$', line)
        if m:
            kind = 'thoughs' if (m.group(2) == 'NONE'
                                 and m.group(1) in ('サイト', 'null')) \
                else 'dialogs'
            scenes[cur].append((kind, m.group(3)))
            continue
        m = re.match(r'^  KICK 【選択肢】(.+?) → scene', line)
        if m:
            scenes[cur].append(('choises', m.group(1)))
            continue
        m = re.match(r'^  KICK 【移動】(.+?) → scene', line)
        if m:
            scenes[cur].append(('choises_move', m.group(1)))
            continue
    items = []
    for sc in SCENE_ORDER:
        block = scenes.get(sc, [])
        res = []
        for i, it in enumerate(block):
            res.append(('choises', it[1]) if it[0] == 'choises_move' else it)
            if it[0] == 'choises_move' and \
                    (i + 1 == len(block) or block[i + 1][0] != 'choises_move'):
                res.append(('choises', LEAVE_JA))
        items.extend(res)
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
    olds = [p[1] for p in pairs]
    dup = sorted({o for o in olds if olds.count(o) > 1})
    if dup:
        print('DUP IN SET:')
        for d in dup:
            print(' ', repr(d))
        return 1
    coll = []
    for lang in ('ja', 'ru'):
        content = {b: io.open(TL[lang][b], encoding='utf-8').read()
                   for b in BUCKETS}
        for b, old, _ja, _ru in pairs:
            if re.search(r'^\s*old "%s"\s*$' % re.escape(old), content[b], re.M):
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
