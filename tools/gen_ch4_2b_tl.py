# -*- coding: utf-8 -*-
# Генератор TL-блоков для главы 4, части 2b (даты хаба 【移動】: сцены 1347–1366).
# old извлекается из script-ch4_2b.rpy по порядку (авто-гарантия точности);
# ja_new — дословно из канона (ch4_canon_p3.txt; переносы склеены, мысли в （ ）);
# ru_new — по JA. Теги в new не дублируются (конвенция ч. 3/ч. 4).
# Строки: 103 голоса + 9 мыслей Сайто + 2 молчаливые реплики Табиты (1361 ×2
# «……。» + мысль) + 12 пунктов меню (1347/1352/1357/1362 ×3) = 126.
# Канон-экстракт (ch4_canon_p3.txt) получается разбором
# ps2_source/chapters/chapter_05_トリスタニアの危機.txt (SCENE 1347–1366).
# Запуск: python tools/gen_ch4_2b_tl.py           — dry-run (сверка + коллизии)
#         python tools/gen_ch4_2b_tl.py --apply   — запись в tl-файлы
import io
import re
import sys

BASE = r'D:/gameMake/ZnT-1/ZnT1'
SCRIPT = BASE + '/game/chapters/4/script-ch4_2b.rpy'
CANON = r'C:/Users/user/AppData/Local/Temp/opencode/ch4_canon_p3.txt'
TL = {
    'ja': {'dialogs': BASE + '/game/tl/japanese/dialogs.rpy',
           'thoughs': BASE + '/game/tl/japanese/thoughs.rpy',
           'choises': BASE + '/game/tl/japanese/choises.rpy'},
    'ru': {'dialogs': BASE + '/game/tl/russian/dialogs.rpy',
           'thoughs': BASE + '/game/tl/russian/thoughs.rpy',
           'choises': BASE + '/game/tl/russian/choises.rpy'},
}
BUCKETS = ('dialogs', 'thoughs', 'choises')

# Порядок сцен в скрипте = порядок источника для этого блока.
SCENE_ORDER = list(range(1347, 1367))

# (bucket, ru_new) — 126 позиций в порядке строк скрипта (JA — из канона)
R = [
    # ==== SCENE 1347 ====
    ('thoughs', 'Сиеста выглядела совсем подавленной. Всё ли с ней в порядке…'),
    ('thoughs', 'И правда — она столько с ней возилась, а тут вдруг велели остаться дома…'),
    ('thoughs', 'И ведь действительно сидит сгорбившись в кухне.'),
    ('dialogs', 'Только я остаюсь… Только я остаюсь… Только я остаюсь…'),
    ('dialogs', 'Напарник, у этой девицы совсем тяжёлый случай.'),
    ('thoughs', 'Хм. И как её только утешить…'),
    ('choises', 'Сказать, что задание опасное.'),
    ('choises', 'Сказать, что привезу сувенир.'),
    ('choises', 'Сказать, что это исключено.'),
    # ==== SCENE 1348 ====
    ('dialogs', 'Сиеста. Это опасное задание. Взять тебя с собой никак нельзя, понимаешь?'),
    ('dialogs', '…Опас…ное… задание.'),
    ('dialogs', 'Потому Луиза и не берёт тебя с собой, Сиеста. Войди и ты в её положение, ладно?'),
    ('dialogs', 'Нет!'),
    ('dialogs', 'Ой-ой…'),
    ('dialogs', 'Если задание опасное, тем более. Подвергнуть вас одного опасности — я такого… я такого не вынесу.'),
    ('dialogs', 'Сиеста…'),
    # ==== SCENE 1349 ====
    ('dialogs', 'Сиеста. Я обязательно привезу тебе сувенир, так что на этот раз смирись.'),
    ('dialogs', 'Сувенир… Не нужен он мне.'),
    ('dialogs', 'Хм. Даже сувенир не помог…'),
    ('dialogs', 'То… тогда… Сайто-сан, а когда вернётесь, вы сходите со мной на свидание?'),
    ('dialogs', 'На свидание?! П-почему?'),
    # ==== SCENE 1350 ====
    ('dialogs', 'Сиеста.'),
    ('dialogs', 'А… Сайто-сан…'),
    ('dialogs', 'Нельзя — значит нельзя. Ты уже взрослая, не стоит капризничать.'),
    # ==== SCENE 1351 ====
    ('dialogs', 'А-а!! И правда!'),
    ('dialogs', 'Сиеста, что с тобой?'),
    ('dialogs', 'Ну что это я, право. Простите, Сайто-сан. Спасибо, что вы за меня волновались.'),
    ('dialogs', 'Со мной уже всё хорошо, так что не волнуйтесь.'),
    ('dialogs', 'Ну, если так, то ладно…'),
    # ==== SCENE 1352 ====
    ('dialogs', 'Дорогой, вот ты где.'),
    ('dialogs', 'А, Кирхе.'),
    ('dialogs', 'Я слышала — ты собрался в Тристанию?'),
    ('dialogs', 'Ох. Вообще-то это должно было быть секретом. Откуда ты узнала?'),
    ('dialogs', 'М-м, секрет.'),
    ('dialogs', 'Пф.'),
    ('dialogs', 'Но причину я не слышала. Зачем ты вообще туда едешь?'),
    ('dialogs', 'Э-э…'),
    ('choises', 'Есть обстоятельства, о которых не скажешь.'),
    ('choises', 'Везу Харуну на прогулку.'),
    ('choises', 'Ректор попросил кое-что купить.'),
    # ==== SCENE 1353 ====
    ('dialogs', 'Это, э-э, обстоятельства, о которых не скажешь…'),
    ('dialogs', 'А-а. Скукотища.'),
    ('dialogs', 'Ну, скучно тебе или нет… Короче, это секрет.'),
    # ==== SCENE 1354 ====
    ('dialogs', 'Харуна всё-таки попала в другой мир, вот я и решил устроить ей небольшую экскурсию…'),
    ('dialogs', 'Правда?'),
    ('dialogs', 'Н-нет, правда. Честно-честно.'),
    # ==== SCENE 1355 ====
    ('dialogs', 'Ректор попросил меня сходить за покупками. Вот незадача.'),
    ('dialogs', 'Правда?'),
    ('dialogs', 'П-правда же. Ну, у него зрение испортилось, он новые очки заказал — и всё такое.'),
    # ==== SCENE 1356 ====
    ('dialogs', 'Хм…'),
    ('dialogs', 'Ну, вид у тебя такой, будто ты влип, пусть будет так.'),
    ('dialogs', 'Но-но. Как подумаю, что мы какое-то время не увидимся, так сразу одиноко.'),
    ('dialogs', 'Ну всё, сейчас как обниму покрепче.'),
    ('dialogs', 'Эй, Кирхе! Перестань, на нас же все смотрят!'),
    ('dialogs', 'Почему? Ничего страшного. Коплю на то время, пока мы не увидимся!'),
    ('dialogs', 'Давай-давай.'),
    ('dialogs', 'П-пощади…'),
    # ==== SCENE 1357 ====
    ('thoughs', 'Ой, Табита.'),
    ('dialogs', 'Искала.'),
    ('dialogs', 'Меня искала? Для тебя это редкость… Что-то случилось?'),
    ('dialogs', 'Это.'),
    ('dialogs', 'Эту книгу… мне?'),
    ('dialogs', 'Дам почитать.'),
    ('thoughs', 'Пролистав страницы, я увидел картинки из жизни знатного человека — с утра до ночи.'),
    ('thoughs', 'Там ещё что-то написано, но… что это за книга?'),
    ('choises', 'Книга о жизни знати?'),
    ('choises', 'Книга о семье Табиты?'),
    ('choises', 'Книга с какой-то историей?'),
    # ==== SCENE 1358 ====
    ('dialogs', 'Это, может, книга о жизни знати?'),
    ('dialogs', 'Думала, пригодится…'),
    ('dialogs', 'Хм, вот если бы ещё буквы читать…'),
    # ==== SCENE 1359 ====
    ('dialogs', 'Это, может, книга об обычаях семьи Табиты?'),
    ('dialogs', 'Совсем нет.'),
    ('dialogs', 'Эй, напарник. Это книга о том, как полагается вести себя знати.'),
    ('dialogs', 'Э, как вести себя знати? Но я же не читаю буквы, так что ничего не понятно.'),
    # ==== SCENE 1360 ====
    ('dialogs', 'Это, может, книга с какой-нибудь историей?'),
    ('dialogs', 'Нет.'),
    ('dialogs', 'Эй, напарник. Это книга о том, как полагается вести себя знати.'),
    ('dialogs', 'Э, как вести себя знати? Но я же не читаю буквы, так что ничего не понятно.'),
    # ==== SCENE 1361 ====
    ('dialogs', 'Жалко-то как. Напарник, пора бы тебе уже научиться читать.'),
    ('dialogs', 'Ничего не поделаешь. Я ведь не навсегда в этом мире.'),
    ('dialogs', '…'),
    ('dialogs', 'Читать — это я умею. Потом почитаю тебе вслух.'),
    ('dialogs', 'С-серьёзно?'),
    ('dialogs', 'Ну, когда говорят «манеры», я напрягаюсь, но знать всё-таки лучше.'),
    ('dialogs', 'Вот именно. Она специально выбрала книгу, где много картинок. Поблагодари вон ту девицу.'),
    ('dialogs', 'Э, для меня… И специально?'),
    ('dialogs', '…'),
    ('dialogs', 'Спасибо, Табита. Я у тебя в долгу.'),
    ('dialogs', 'Угу…'),
    ('thoughs', 'Хм, а когда это я успел рассказать Табите, что познакомлюсь со знатью?'),
    # ==== SCENE 1362 ====
    ('dialogs', 'А, Хирага-кун?'),
    ('dialogs', 'Э-э, вы кто?'),
    ('dialogs', 'Хирага-кун, ну ты и льстец. Это же я, я. Харуна.'),
    ('dialogs', 'А, так это Харуна? Я тебя сразу и не узнал. А что это за одежда?'),
    ('dialogs', 'Луиза-сан сказала, что всё время в одном и том же скучно, вот и дала мне это.'),
    ('dialogs', 'Ого, эта самая Луиза…'),
    ('dialogs', 'Хирага-кун, как тебе? Я так давно не носила ничего, кроме формы, что даже стесняюсь.'),
    ('thoughs', 'Ну-у…'),
    ('choises', 'Тебе очень идёт.'),
    ('choises', 'Я бы тоже хотел новую одежду.'),
    ('choises', 'Одежда красит человека, как говорится.'),
    # ==== SCENE 1363 ====
    ('dialogs', 'Тебе очень идёт, разве нет?'),
    ('dialogs', 'П-правда?'),
    ('dialogs', 'Я, кажется, уже говорила: в последнее время я всё время в форме, да?'),
    ('dialogs', 'В другой одежде и настроение становится радостнее. Одежда всё-таки важна.'),
    # ==== SCENE 1364 ====
    ('dialogs', 'Я бы тоже хотел новую одежду. С тех пор как я тут, я почти всё время в этом.'),
    ('dialogs', 'Были бы у меня деньги, я бы тебе купила…'),
    ('dialogs', 'Нет, мне и от одной мысли приятно. Вот бы у Луизы была хоть капелька этого…'),
    ('dialogs', 'Ой, Луиза-сан не такая ужасная, как ты думаешь.'),
    ('dialogs', 'Правда?'),
    # ==== SCENE 1365 ====
    ('dialogs', 'Одежда красит человека — верно говорят…'),
    ('dialogs', 'Хирага-кун, ну ты и жестокий.'),
    ('dialogs', 'Да нет, шучу, шучу. По-моему, тебе очень идёт.'),
    ('dialogs', 'П-правда? Спасибо, Хирага-кун.'),
    ('dialogs', 'Д-да нет, ничего.'),
    # ==== SCENE 1366 ====
    ('dialogs', 'Кстати, не в обиду будет сказано, а одежда Луизы не была маловата?'),
    ('dialogs', 'Ик.'),
    ('dialogs', 'Ну, Луиза же миниатюрная, да? Я и подумал, подойдёт ли тебе.'),
    ('dialogs', 'Вообще-то я и сама думала, что немного жмёт.'),
    ('dialogs', 'А, так и есть?'),
    ('dialogs', 'Ха-ха-ха-ха.'),
    ('dialogs', 'Ха-ха-ха-ха.'),
    ('dialogs', 'Хирага-кун, извращенец.'),
    ('dialogs', 'Будешь такое спрашивать у девушек — и я тебя накажу, хоть я и не Луиза-сан.'),
    ('dialogs', 'Н-нет, пощади…'),
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
        if m:
            items.append(('choises', m.group(1)))
            continue
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
    items = []
    for sc in SCENE_ORDER:
        items.extend(scenes.get(sc, []))
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
