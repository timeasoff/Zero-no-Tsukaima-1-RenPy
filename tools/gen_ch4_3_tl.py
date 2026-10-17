# -*- coding: utf-8 -*-
# Генератор TL-блоков для главы 4, части 3 (P4a: сцены 236–245 — дорога в
# Тристанию, Сиеста в мешке, сон в японской школе, пробуждение).
# old извлекается из script-ch4_3.rpy по порядку (авто-гарантия точности);
# ja_new — дословно из канона (ch4_canon_p4a.txt; переносы склеены, мысли в （ ）);
# ru_new — по JA. Теги в new не дублируются (конвенция ч. 3/ч. 4).
# Строки: 107 голосов (вкл. ？？？-реплику Сиесты из мешка, строку unk_si) +
# 1 молчаливая реплика Харуной (236, «……。») + 10 мыслей Сайто + 2 null-блока
# (245, «………………») + 6 пунктов меню = 126.
# Канон-экстракт (ch4_canon_p4a.txt) получается разбором
# ps2_source/chapters/chapter_05_トリスタニアの危機.txt (SCENE 236–245).
# Запуск: python tools/gen_ch4_3_tl.py           — dry-run (сверка + коллизии)
#         python tools/gen_ch4_3_tl.py --apply   — запись в tl-файлы
import io
import re
import sys

BASE = r'D:/gameMake/ZnT-1/ZnT1'
SCRIPT = BASE + '/game/chapters/4/script-ch4_3.rpy'
CANON = r'C:/Users/user/AppData/Local/Temp/opencode/ch4_canon_p4a.txt'
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
SCENE_ORDER = list(range(236, 246))

# (bucket, ru_new) — 126 позиций в порядке строк скрипта (JA — из канона)
R = [
    # ==== SCENE 236 ====
    ('thoughs', 'Сколько же мы уже трясёмся в карете с тех пор, как выехали из академии?'),
    ('thoughs', 'Небо ещё светлое. Пожалуй, прибудем к вечеру?'),
    ('dialogs', '…Суу… суу…'),
    ('dialogs', '…Мм… мм…'),
    ('thoughs', 'А они вдвоём прижались друг к другу и сладко спят.'),
    ('thoughs', 'Ну да, с самого утра всё сидим в карете. Ладно, неудивительно… Может, и мне вздремнуть?'),
    ('dialogs', 'Угх… что ж это за дорога такая паршивая!!'),
    ('dialogs', 'И тут поклажа, что была навалена, валилась на меня… Ох…'),
    ('dialogs', 'Гахах… тяжело же… Да он неподъёмно тяжёлый… Что вообще тут навалено-то?'),
    ('dialogs', 'Что с тобой, напарник? И чего ты там так стонал?'),
    ('dialogs', 'Как карету качнуло, так эта наваленная поклажа свалилась прямо на меня.'),
    ('dialogs', '…Ммх…'),
    ('dialogs', 'Ува-ва-ва! П-поклажа заговорила!!'),
    ('dialogs', 'Поклажа разговаривает? Ты со сна рехнулся уже, напарник?'),
    ('dialogs', 'Эй, вот уж от кого-кого, а от тебя это слышать… Или это мир, где разговаривает вообще всё?'),
    ('dialogs', '…Ну и шумишь. Мне даже поспать нельзя.'),
    ('dialogs', 'Наваленная поклажа посыпалась на меня. Потом она заговорила. И ещё какая-то мягкая…'),
    ('dialogs', 'Сайто, что ты вообще такое говоришь?'),
    ('dialogs', 'К-как бы там ни было, откроем и посмотрим, что внутри.'),
    ('dialogs', 'Аха, а я к вам тоже забралась!'),
    ('dialogs', '……。'),
    ('dialogs', '……。'),
    ('dialogs', '……。'),
    ('dialogs', '……。'),
    ('dialogs', '…Тэ-хэ.'),
    ('dialogs', 'П-почему тут Сиеста, которая должна была остаться дома?'),
    ('dialogs', 'Сейчас же затяни мешок с поклажей!'),
    ('dialogs', 'Э-э!?'),
    ('dialogs', 'Ну зачем же так!?'),
    ('dialogs', 'Выбросим. Если повезёт, её подберут бродячие артисты.'),
    ('thoughs', '…Да постой, Луиза!! Ты же всерьёз затягиваешь мешок!!'),
    ('dialogs', 'П-простите, мадемуазель Вальер!! Простите меня, пожалуйста… Уааааа!?'),
    ('dialogs', 'Эй, ты всерьёз!? Успокойся, Луиза!!'),
    ('dialogs', 'В-ведь я всем пригожусь! Буду стараться изо всех сил, так что п-пожалуйста, возьмите меня с собой!!'),
    ('dialogs', 'Я же велела Сиесте остаться дома! Неужели это ты всё подстроил, Сайто…!'),
    ('dialogs', 'Н-ну, погоди-ка. Разве я мог такое провернуть?'),
    ('dialogs', 'Простите, мадемуазель Вальер. Сайто-сан совершенно не виноват. Всё это было моим собственным решением.'),
    ('dialogs', 'Сиеста…'),
    ('dialogs', 'Я волновалась за Харуну-сан и Сайто-сана, и вот, не удержавшись, увязалась тайком, как безбилетница.'),
    ('dialogs', 'Что ж, немного обидно, что меня не позвали… Но Сайто, что ты собираешься с этим делать?'),
    ('dialogs', 'А что тут скажешь… Но и возвращаться в академию теперь нельзя, разве нет?'),
    ('dialogs', 'Как есть, поедем во дворец! Без причины же её с собой не возьмёшь, разве нет?'),
    ('dialogs', '……。'),
    ('dialogs', 'Сайто. И как ты собираешься объяснить, кто такая Сиеста?'),
    ('dialogs', 'Насчёт Сиесты-то…'),
    ('choises', 'Сказать, что она моя сестра.'),
    ('choises', 'Сказать, что она служанка Луизы.'),
    ('choises', 'Думаю, стоит сказать как есть.'),
    # ==== SCENE 237 ====
    ('dialogs', 'Что, сказать, будто она моя родная сестра?'),
    ('dialogs', '…Что-о!?'),
    ('dialogs', 'Э-э!?'),
    ('dialogs', 'Ну а Сиеста — у неё чёрные волосы и чёрные глаза, так? Думаю, сойдёт, если позвать её моей сестрой.'),
    ('dialogs', 'Э-э… И как мне вас звать? Братиком? Или солиднее — братец?'),
    ('dialogs', 'А-ах, что выбрать! Я никак не решусь…'),
    ('dialogs', 'Что тут размышлять! Есть варианты получше?'),
    ('dialogs', 'Тогда как насчёт сказать, что она служанка Луизы?'),
    ('dialogs', 'Н-ну… Похоже, разумная идея. Пусть будет так.'),
    # ==== SCENE 238 ====
    ('dialogs', 'Ну а вариант со служанкой Луизы как?'),
    ('dialogs', 'Н-ну… Похоже, разумная идея. Пусть будет так.'),
    ('dialogs', 'Есть! Вместо Сайто-сана возьму на себя все заботы о вашем быте.'),
    ('dialogs', 'Что-то в твоих словах настораживает… Но и ладно, пусть так.'),
    # ==== SCENE 239 ====
    ('dialogs', 'Так и сказать как есть. Принцесса ведь — она поймёт.'),
    ('dialogs', '…Я прекрасно знаю, что пути нет… А врать всё равно бессмысленно…'),
    ('dialogs', 'Верно… Ну и славно, Сиеста.'),
    ('dialogs', 'Но нет.'),
    ('dialogs', 'Э-э!?'),
    ('dialogs', 'Пусть пока считается, что она моя служанка. А то больших проблем не оберёмся…'),
    ('dialogs', 'Есть, всё поняла!'),
    # ==== SCENE 240 ====
    ('thoughs', 'Ну, таково дело… В итоге во дворец поехали мы втроём: с Луизой, Харуной и Сиестой.'),
    # ==== SCENE 241 ====
    ('dialogs', '……。'),
    ('dialogs', '…Хирага-кун.'),
    ('dialogs', 'Ммх…?'),
    ('dialogs', 'Хирага-кун, ты чего.'),
    ('dialogs', 'Ах, извини… Так мы доехали до Тристании?'),
    ('dialogs', 'Вот безобразие… Чего расселся? Уже пора домой!'),
    ('dialogs', '…!?'),
    ('dialogs', 'А…? Подожди, это же школа, разве нет?'),
    ('thoughs', 'Окидываю взглядом окрестности — и нахожу кое-кого из знакомых одноклассников.'),
    ('dialogs', 'После уроков ты продолжал дремать, Хирага-кун. Неужели спал на всех занятиях подряд?'),
    ('dialogs', 'Что, правда все? Вот попал.'),
    ('dialogs', 'И помни, Хирага-кун: сегодня ты дежурный. Поскорее пиши классный журнал.'),
    ('dialogs', 'А, точно?'),
    ('dialogs', '«Точно», говоришь?! Сегодня же мы оба были дежурными! И почти всю работу делала я, между прочим!'),
    ('dialogs', 'Да, верно… извиняюсь. Просто самочувствие плохое.'),
    ('dialogs', 'Вот же балбес... Я тут посмотрю за тобой.'),
    ('dialogs', 'Вот только классный журнал придётся написать как следует, понял?'),
    ('dialogs', 'Угх…'),
    ('dialogs', 'Ну-у же, не витай в облаках. Пиши скорей, Хирага-кун. Ведь домой нам идти вместе, не так ли?'),
    ('choises', 'Попросить её написать и классный журнал.'),
    ('choises', 'Сослаться на недомогание и идти в медпункт.'),
    ('choises', 'А какой сегодня день недели?'),
    # ==== SCENE 242 ====
    ('dialogs', 'Слушай, уж с таким рвением и классный журнал за меня напишешь!'),
    ('dialogs', 'Ну уж нет! Это нечестно — почему одна я всё тянуть должна!?'),
    # ==== SCENE 243 ====
    ('dialogs', 'Я, тут сказать, не в полном порядке… В медпункт отпустите?'),
    ('dialogs', 'Хм-м, но во сне ты бормотал довольно бодро. К тому же, вроде, тебе снились девчонки вокруг.'),
    ('dialogs', 'С-серьёзно?!'),
    ('dialogs', 'Угу, так что… Просьба отклонена.'),
    # ==== SCENE 244 ====
    ('dialogs', 'Кстати, какой нынче день? Вроде бы пятница?'),
    ('dialogs', 'Понедельник, конечно же. Неужели всё так плохо, Хирага-кун?'),
    # ==== SCENE 245 ====
    ('thoughs', '………………'),
    ('dialogs', 'Ну вот, так ведь можно?'),
    ('dialogs', 'Ну, посмотрим… Хм, так сойдёт? Хотя в журнале у тебя всё враньё.'),
    ('dialogs', 'Так то оно так — весь день-то проспал.'),
    ('dialogs', 'А завтра будь поосторожнее. Учитель и так постоянно тебя предупреждает.'),
    ('dialogs', 'Так точно.'),
    ('dialogs', 'А вот такого Хираги-куна ждёт наказание!'),
    ('dialogs', 'Н-наказание!? …Стоп, а это что?'),
    ('dialogs', 'Ну разве самому не нравится? Наказание.'),
    ('dialogs', 'Так ведь Луиза-сан говорила: от наказаний ты, мол, в восторге.'),
    ('dialogs', 'Луиза-сан? Кто это?'),
    ('dialogs', 'А, кто бы это мог быть?'),
    ('dialogs', 'Т-т-так это что за сфера из света?!'),
    ('dialogs', 'Ну-у… магия?'),
    ('dialogs', 'М-магия?! Погоди, Харуна!! Прекрати!!!'),
    ('dialogs', 'Оговорки не принимаются!'),
    ('dialogs', 'Уааааааа.'),
    ('dialogs', 'Сайто? Что случилось? Дремала себе, а тут вдруг как закричишь.'),
    ('dialogs', 'Где это я?'),
    ('dialogs', 'Мы ещё на тракте. А что за дело?'),
    ('dialogs', 'Сайто-сан, вы попрели! Какой же вам снился кошмар?'),
    ('dialogs', 'Н-ни-ничего не случилось…'),
    ('thoughs', 'И чего ж мне снилось такое? А Харуна — маг? Да такого быть не может…'),
    ('thoughs', 'Наверное, это всё просто спуталось в башке с привычными наказаниями Луизы.'),
    ('dialogs', '…?'),
    ('thoughs', 'Ладно, посплю ещё разок…'),
    ('thoughs', '………………'),
]


def parse_script():
    txt = io.open(SCRIPT, encoding='utf-8').read()
    items = []
    for line in txt.splitlines():
        m = re.match(r'^\s+(unk_si|s|l|ha|k|si|t|th|c|o|g|m|d) "([^"]*)"$', line)
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
        for i, (a, b) in enumerate(zip(items, canon)):
            if a != b:
                print(' first item mismatch at #%d: script=%r canon=%r'
                      % (i + 1, a, b))
                break
        print(' tail: script=%r' % (items[len(canon):len(canon) + 3],)
              if len(items) > len(canon) else ' tail: canon=%r'
              % (canon[len(items):len(items) + 3],))
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
