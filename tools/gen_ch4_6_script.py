# -*- coding: utf-8 -*-
"""Сборка game/chapters/4/script-ch4_6.rpy из events-источника.

Структура, порядок реплик, голоса, спрайты и события — строго из
ps2_source/events_full/chapter_05_トリスタニアの危機.txt (сцены 261–268,
1084–1103). Тексты EN подставляются из tools/ch4_6_en.py, RU — из
tools/ch4_6_ru.py (для tl). JA берётся из events (дословно).

Использование:
    python tools/gen_ch4_6_script.py            # dry-run: счётчики, пропуски
    python tools/gen_ch4_6_script.py --apply    # записать .rpy
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, 'game', 'chapters', '4', 'script-ch4_6.rpy')
EVENTS = [
    os.path.join(ROOT, '.tmp', 'events_261_268.txt'),
    os.path.join(ROOT, '.tmp', 'events_1085_1103.txt'),
]

# ---------------------------------------------------------------- справочники
SPK = {'サイト': 's', 'ルイズ': 'l', 'アンリエッタ': 'h', 'シエスタ': 'si',
       'ハルナ': 'ha', 'デルフリンガー': 'd', 'アキナ': 'ak', 'null': 'th'}
SYM = {'サイト': 'サイト', 'ルイズ': 'ルイズ', 'アンリエッタ': 'アンリエッタ',
       'シエスタ': 'シエスタ', 'ハルナ': 'ハルナ', 'デルフリンガー': 'デルフリンガー',
       'アキナ': 'アキナ', 'null': 'null'}
# симпатия: ключ char_key
# симпатия: ключ char_key (по префиксу говорящего; допустимые ключи —
# sympathy.rpy: louise / haruna / henrietta / siesta / tabitha / kirche)
SYM_KEY = {'l': 'louise', 'h': 'henrietta', 'si': 'siesta', 'ha': 'haruna',
           's': 'saito', 'd': 'derflinger'}

# спрайты: id -> имя (PROVISIONAL — см. отчёт части 6)
SPRITE_PROV = {
    420: 's 5 shy',
    471: 's 8 angry',
    552: 'si 6 shy',
    764: 'h 1',
    766: 'h 1 happy',
    770: 'h 1 sad',
    786: 'h 2',
    788: 'h 2 happy',
    792: 'h 2 sad',
}
# слои персонажей
LAYERS = ['lay1', 'lay2', 'lay5', 'lay6', 'lay7', 'lay8', 'lay19', 'lay21']


def load_csv(path, id_col=0):
    out = {}
    with io.open(path, encoding='utf-8') as fh:
        for ln in fh:
            p = ln.rstrip('\n').split(',')
            if p and p[id_col].isdigit():
                out[int(p[id_col])] = p[id_col + 1]
    return out


def load_images(path):
    """image_id_map.csv: id, kind, filename, … -> (kind, filename)."""
    out = {}
    with io.open(path, encoding='utf-8') as fh:
        for ln in fh:
            p = ln.rstrip('\n').split(',')
            if p and p[0].isdigit():
                out[int(p[0])] = (p[1], p[2] if len(p) > 2 else '')
    return out


SPRITES = load_csv(os.path.join(ROOT, 'references', 'sprite_id_map.csv'))
IMAGES = load_images(os.path.join(ROOT, 'references', 'image_id_map.csv'))
for k, v in SPRITE_PROV.items():
    SPRITES.setdefault(k, v)

# спрайты Акины: файлов в медиа нет — не показываются (прецедент Kolber)
AKINA_SPRITES = {1028, 1032}


def esc(s):
    """экранирование строки для .rpy (переводы строк -> \n, кавычки -> \")."""
    return s.replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"')


def load_tl_olds():
    """old из tl/{japanese,russian} — ЧУЖИЕ части (свои строки исключены,
    иначе решение о тегах зависело бы от состояния tl и менялось от прогона
    к прогону)."""
    out = set()
    base = os.path.join(ROOT, 'game', 'tl')
    for lang in ('japanese', 'russian'):
        d = os.path.join(base, lang)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith('.rpy'):
                continue
            for ln in io.open(os.path.join(d, fn), encoding='utf-8'):
                m = re.match(r'^\s*old\s+"(.*)"\s*$', ln)
                if m:
                    out.add(m.group(1))
    # исключаем блоки самой части 6 (по тегу) и её строки без тега
    out = set(o for o in out if '#ch4.6_' not in o)
    try:
        from ch4_6_en import EN_DIALOGS, EN_THOUGHTS, EN_CHOICES
        for k, v in EN_DIALOGS.items():
            out.discard(v)
        for k, v in EN_THOUGHTS.items():
            out.discard(v)
            out.discard('%s{#%s}' % (v, k))
        for k, v in EN_CHOICES.items():
            out.discard(v)
    except ImportError:
        pass
    return out


TL_OLDS = load_tl_olds()


def bg_name(i):
    """(имя, is_cg) по image_id_map; пустое имя → заглушка id(K)."""
    kind, fn = IMAGES.get(i, ('bg', ''))
    if not fn:
        return 'id(%d)' % i, kind == 'cg'
    return fn, kind == 'cg'


# ---------------------------------------------------------------- разбор events
RE_SET = re.compile(r'^SET\s+set\("(\w+)",\s*\{(.*)\}\)\s*$')
RE_TALK = re.compile(r'^DIALOGUE\s+talk\((.*)\)\s*$')
RE_LIKE = re.compile(r'^LIKE\s+like\("([^"]*)",\s*(-?\d+)\)\s*$')
RE_CHOICE = re.compile(r'^CHOICE\s+selectItem\("((?:[^"\\]|\\.)*)",\s*\(0x01000000 \+(\d+)\).*$')
RE_GOTO = re.compile(r'^GOTO\s+next\(\(0x01000000 \+(\d+)\).*$')
RE_IMG = re.compile(r'image\s*=\s*\(0x02000000 \+(\d+)\)')
RE_X = re.compile(r'(?<![\w])x\s*=\s*(-?\d+)')

SPLIT_ARGS = re.compile(r'"((?:[^"\\]|\\.)*)"|(\bnull\b)|\(0x0[46]000000 \+(\d+)\)')


def parse_args(args):
    """-> (spk, disp, text, voice_id) для talk(...).

    Позиционный разбор: talk(spk, disp, text, voice). Аргументы — либо
    строка в кавычках, либо литерал null, либо id голоса.
    """
    toks = []
    vid = None
    for m in SPLIT_ARGS.finditer(args):
        if m.group(3):
            vid = int(m.group(3))
        elif m.group(2):
            toks.append('null')
        else:
            toks.append(m.group(1))
    spk = toks[0] if len(toks) > 0 else 'null'
    disp = toks[1] if len(toks) > 1 else 'null'
    text = toks[2] if len(toks) > 2 else ''
    return spk, disp, text, vid


def parse_events():
    scenes = {}
    cur = None
    for fn in EVENTS:
        for ln in io.open(fn, encoding='utf-8'):
            ln = ln.rstrip('\n')
            m = re.match(r'^## SCENE (\d+)', ln)
            if m:
                cur = int(m.group(1))
                scenes.setdefault(cur, [])
                continue
            if cur is None:
                continue
            ev = scenes[cur]

            m = RE_SET.match(ln)
            if m:
                layer, body = m.group(1), m.group(2)
                img = RE_IMG.search(body)
                x = RE_X.search(body)
                hide = ('hide = 1' in body) or ('show = 0' in body)
                if layer == 'stage':
                    if hide:
                        ev.append(('bg_hide',))
                    elif img:
                        ev.append(('bg', int(img.group(1))))
                elif layer == 'event':
                    if hide:
                        ev.append(('cg_hide',))
                    elif img:
                        ev.append(('cg', int(img.group(1))))
                elif layer == 'bgm':
                    mplay = re.search(r'play\s*=\s*\(0x03000000 \+(\d+)\)', body)
                    if mplay:
                        ev.append(('bgm_play', int(mplay.group(1))))
                    elif 'stop' in body:
                        ev.append(('bgm_stop',))
                elif layer in LAYERS:
                    if img:
                        ev.append(('sprite', layer, int(img.group(1)),
                                   int(x.group(1)) if x else None))
                    elif hide:
                        ev.append(('sprite_hide', layer))
                    elif x:
                        ev.append(('sprite_pos', layer, int(x.group(1))))
                continue

            m = RE_TALK.match(ln)
            if m:
                spk, disp, text, vid = parse_args(m.group(1))
                ev.append(('talk', spk, disp, text or '', vid))
                continue

            m = RE_LIKE.match(ln)
            if m:
                ev.append(('like', m.group(1), int(m.group(2))))
                continue

            m = RE_CHOICE.match(ln)
            if m:
                ev.append(('choice', m.group(1), int(m.group(2))))
                continue

            m = RE_GOTO.match(ln)
            if m:
                ev.append(('goto', int(m.group(1))))
                continue

            if ln.startswith('MENUINIT'):
                ev.append(('menu_init',))
            elif ln.startswith('MENU '):
                ev.append(('menu',))
            elif ln.startswith('TRANS'):
                ev.append(('trans', ln))
            elif ln.startswith('COFFEE'):
                ev.append(('coffee',))
            elif ln.startswith('BATTLE') or ln.startswith('battle'):
                ev.append(('battle', ln))
            elif ln.startswith('SET') or ln.startswith('SYNC') or ln.startswith('CREATE'):
                continue
            elif ln.startswith('VIBRATE') or ln.startswith('SET') or ln.startswith('se'):
                ev.append(('se', ln))
            elif re.match(r'^(SE|se0|se1)\b', ln):
                ev.append(('se', ln))
            elif ln.startswith('wait') or ln.startswith('msg') or ln.startswith('vibrate'):
                ev.append(('misc', ln))
            elif ln.strip():
                ev.append(('misc', ln))
    return scenes


# ---------------------------------------------------------------- голоса
class Voices:
    def __init__(self):
        self.counts = {}
        self.by_scene = {}
        self.seq = []

    def name(self, spk, scene):
        key = SPK.get(spk, 'x')
        if key == 'th':
            return None
        self.counts[key] = self.counts.get(key, 0) + 1
        return 'ch4.6_%s_%03d' % (key, self.counts[key])


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    try:
        from ch4_6_en import EN_DIALOGS, EN_THOUGHTS, EN_CHOICES
    except ImportError:
        EN_DIALOGS, EN_THOUGHTS, EN_CHOICES = {}, {}, {}

    scenes = parse_events()
    V = Voices()
    missing = []

    # имя голоса для каждой реплики (в порядке сцен: main, затем маршруты)
    ORDER = [261, 262, 263, 264]
    ROUTES = [
        ('louise', 'date_louise_ch4_6', 265, 1084, [1085, 1086, 1087], 1088),
        ('siesta', 'date_siesta_ch4_6', 266, 1089, [1090, 1091, 1092], 1093),
        ('haruna', 'date_haruna_ch4_6', 267, 1094, [1095, 1096, 1097], 1098),
        ('henrietta', 'date_henrietta_ch4_6', 268, 1099, [1100, 1101, 1102], 1103),
    ]

    # Сцены мостов 265–268 (по одной мысли) идут в начале маршрутов
    ROUTE_SCENES = []
    for key, label, bridge, head, branches, rejoin in ROUTES:
        ROUTE_SCENES.append((key, label, bridge, head, branches, rejoin))

    def scene_voices(sc):
        """проставить имена голосов для всех talk в сцене (в порядке событий)"""
        out = []
        for e in scenes.get(sc, []):
            if e[0] == 'talk':
                out.append(V.name(e[1], sc))
            else:
                out.append(None)
        return out

    # 1) нумерация: сначала main (261-264), потом маршруты в порядке
    vmap = {}   # (scene, index) -> voice name
    for sc in ORDER:
        for i, e in enumerate(scenes[sc]):
            if e[0] == 'talk' and e[4] is not None:
                vmap[(sc, i)] = V.name(e[1], sc)
    for key, label, bridge, head, branches, rejoin in ROUTE_SCENES:
        for sc in [bridge, head] + branches + [rejoin]:
            for i, e in enumerate(scenes.get(sc, [])):
                if e[0] == 'talk' and e[4] is not None:
                    vmap[(sc, i)] = V.name(e[1], sc)

    # 2) генерация кода
    out = []
    state = {'layers': {}, 'bg': None, 'cg': None, 'bgm': None}
    thought_no = [0]

    # --- подсчёт повторов EN (E11: одинаковый old нельзя повторять) ---
    en_counter = {}
    for sc in ORDER + [s for r in ROUTE_SCENES for s in [r[2], r[3]] + r[4] + [r[5]]]:
        for i, e in enumerate(scenes.get(sc, [])):
            if e[0] == 'talk' and e[4] is not None:
                vn = vmap.get((sc, i))
                en = EN_DIALOGS.get(vn)
                if en is not None:
                    en_counter[en] = en_counter.get(en, 0) + 1
            elif e[0] == 'choice':
                en = EN_CHOICES.get(str(e[2]))
                if en is not None:
                    en_counter[en] = en_counter.get(en, 0) + 1

    def uniq_tag(en, tag):
        """тег нужен, только если строка повторяется внутри части; явный тег
        (уже в данных EN) сохраняется. Решение детерминировано: не зависит от
        текущего состояния tl."""
        if '{#' in en:
            return en
        if en_counter.get(en, 0) <= 1:
            return en
        return '%s{#%s}' % (en, tag)

    def visible():
        items = []
        for lay, st in state['layers'].items():
            if not st.get('vis') or st.get('img') is None:
                continue
            x = st.get('x')
            if x is None:
                rank = 1
            elif x < -20:
                rank = 0
            elif x < 150:
                rank = 1
            else:
                rank = 2
            items.append((rank, st.get('level', 160), lay, st['img']))
        items.sort(key=lambda t: (t[0], t[1], t[2]))
        return [SPRITES.get(i[3], 'id(%d)' % i[3]) for i in items]

    def emit_sprites(force=False):
        vis = visible()
        key = tuple(vis)
        if key == state.get('_vis') and not force:
            return
        state['_vis'] = key
        if not vis:
            out.append('    $ show_sprites()')
        else:
            out.append('    $ show_sprites((%s))' % ', '.join('"%s"' % v for v in vis))

    def cur_bgm_line():
        """индекс последней строки fade_fx без new_music (комментарии пропускаем)"""
        for i in range(len(out) - 1, -1, -1):
            s = out[i].strip()
            if s.startswith('#'):
                continue
            if s.startswith('$ fade_fx(') and 'new_music' not in s:
                return i
            return None
        return None

    def emit_scene(sc, indent='    ', voice_of=None, in_menu=False):
        """выдаёт код сцены; menu-выборы обрабатываются вызывающим."""
        evs = scenes.get(sc, [])
        for i, e in enumerate(evs):
            k = e[0]
            if k == 'bg':
                name, is_cg = bg_name(e[1])
                out.append('%s# [BG +%d → %s]' % (indent, e[1], name))
                out.append('%s$ fade_fx("%s")' % (indent, name))
                state['bg'] = e[1]
                state['cg'] = None
            elif k == 'bg_hide':
                nxt = evs[i + 1][0] if i + 1 < len(evs) else None
                if nxt == 'cg':
                    state['bg'] = None
                    out.append('%s# [BG hide] — поглощается переходом на CG' % indent)
                else:
                    out.append('%s# [BG hide]' % indent)
                    out.append('%s$ fade_fx("black")' % indent)
                    state['bg'] = None
            elif k == 'cg':
                name, _ = bg_name(e[1])
                out.append('%s# [EVENT_CG +%d → %s]' % (indent, e[1], name))
                out.append('%s$ fade_fx("%s", type="cg")' % (indent, name))
                state['cg'] = e[1]
            elif k == 'cg_hide':
                nxt = evs[i + 1][0] if i + 1 < len(evs) else None
                if nxt == 'bg':
                    out.append('%s# [EVENT_CG hide] — поглощается переходом на фон' % indent)
                    state['cg'] = None
                else:
                    out.append('%s# [EVENT_CG hide]' % indent)
                    out.append('%s$ fade_fx("black")' % indent)
                    state['cg'] = None
            elif k == 'bgm_play':
                t = e[1] - 1
                idx = cur_bgm_line()
                if idx is not None:
                    ln = out[idx]
                    out[idx] = ln[:-1] + ', new_music="t%d")' % t
                else:
                    out.append('%splay music t%d fadein 1.0' % (indent, t))
                state['bgm'] = e[1]
            elif k == 'bgm_stop':
                out.append('%sstop music fadeout 1.0' % indent)
                state['bgm'] = None
            elif k == 'sprite':
                lay, img, x = e[1], e[2], e[3]
                if img in AKINA_SPRITES:
                    out.append('%s# [%s +%d] — спрайт Акины: файла в медиа нет, не показывается' % (indent, lay, img))
                    continue
                st = state['layers'].setdefault(lay, {'img': None, 'x': None, 'vis': False, 'level': 160})
                st['img'] = img
                st['vis'] = True
                if x is not None:
                    st['x'] = x
                nm = SPRITES.get(img, 'id(%d)' % img)
                out.append('%s# [%s +%d → %s]' % (indent, lay, img, nm))
                emit_sprites()
            elif k == 'sprite_hide':
                lay = e[1]
                st = state['layers'].setdefault(lay, {'img': None, 'x': None, 'vis': False, 'level': 160})
                st['vis'] = False
                out.append('%s# [%s hide]' % (indent, lay))
                emit_sprites()
            elif k == 'sprite_pos':
                lay, x = e[1], e[2]
                st = state['layers'].setdefault(lay, {'img': None, 'x': None, 'vis': False, 'level': 160})
                st['x'] = x
                out.append('%s# [%s x=%d]' % (indent, lay, x))
                emit_sprites()
            elif k == 'talk':
                spk, disp, text, vid = e[1], e[2], e[3], e[4]
                if vid is None:
                    # мысль (без голоса) — th
                    thought_no[0] += 1
                    tag = 'ch4.6_th_%03d' % thought_no[0]
                    en = EN_THOUGHTS.get(tag)
                    if en is None:
                        missing.append(('thought', tag, text))
                        en = '@@MISSING_%s@@' % tag
                    out.append('%sth "%s{#%s}"' % (indent, esc(en), tag))
                    out.append('%s# JA: %s' % (indent, text.replace('\\n', ' / ')))
                else:
                    vn = vmap.get((sc, i))
                    key = SPK.get(spk, 'x')
                    if disp and disp != 'null' and '？？' in disp:
                        who = 'unk_ak' if key == 'ak' else 'unk_h'
                    else:
                        who = key
                    en = EN_DIALOGS.get(vn)
                    if en is None:
                        missing.append(('dialog', vn, text))
                        en = '@@MISSING_%s@@' % vn
                    en = uniq_tag(en, 'ch4.6_v%s' % vid)
                    out.append('%svoice "%s"' % (indent, vn))
                    out.append('%s%s "%s"' % (indent, who, esc(en)))
                    out.append('%s# JA[%s]: %s' % (indent, vid, text.replace('\\n', ' / ')))
            elif k == 'like':
                key_sym = SPK.get(e[1], 'x')
                out.append('%s$ update_sympathy(%d, char_key="%s")' % (
                    indent, e[2], SYM_KEY.get(key_sym, key_sym)))
            elif k == 'choice':
                pass
            elif k == 'trans':
                out.append('%s# [%s] — переход выполняется fade_fx' % (indent, e[1].replace('  ', ' ')))
            elif k == 'coffee':
                out.append('%s# [COFFEE] → pause(1.0)' % indent)
                out.append('%s$ pause(1.0)' % indent)
            elif k == 'battle':
                out.append('%s# [BATTLE %s] — система боя не реализована, вызов не переносится' % (indent, e[1]))
            elif k == 'se':
                out.append('%s# [%s] — SE не портируется' % (indent, e[1]))
            elif k == 'misc':
                out.append('%s# [%s] — не портируется' % (indent, e[1]))

    def emit_route(key, label, bridge, head, branches, rejoin):
        out.append('')
        out.append('label %s:' % label)
        out.append('    # ==== SCENE %d (мост): в PS2 не проигрывается (dateDone → next(%d) прямо)' % (bridge, head))
        out.append('    # текст мысли канонически сохранён здесь (ACCEPTABLE ADAPTATION)')
        # мысль моста
        for i, e in enumerate(scenes.get(bridge, [])):
            if e[0] == 'talk':
                thought_no[0] += 1
                tag = 'ch4.6_th_%03d' % thought_no[0]
                en = EN_THOUGHTS.get(tag)
                if en is None:
                    missing.append(('thought', tag, e[3]))
                    en = '@@MISSING_%s@@' % tag
                out.append('    th "%s{#%s}"' % (esc(en), tag))
                out.append('    # JA: %s' % e[3].replace('\\n', ' / '))
        out.append('')
        out.append('    # ==== SCENE %d ====' % head)
        emit_scene(head)
        # меню
        choices = [(e[1], e[2]) for e in scenes.get(head, []) if e[0] == 'choice']
        if choices:
            out.append('')
            out.append('    # ---- 【選択肢】 ----')
            out.append('    menu:')
            for jt, target in choices:
                en = EN_CHOICES.get(str(target))
                if en is None:
                    missing.append(('choice', str(target), jt))
                    en = '@@MISSING_choice_%s@@' % target
                en = uniq_tag(en, 'ch4.6_c%s' % target)
                out.append('        "%s":' % esc(en))
                out.append('            # JA: %s' % jt)
                out.append('            # ==== SCENE %d ====' % target)
                emit_scene(target, indent='            ')
            out.append('')
            out.append('    # ==== SCENE %d (переход после вариантов) ====' % rejoin)
            emit_scene(rejoin)
        out.append('')
        out.append('    # [移動] → next(269): сцена 269 — глава 5, НЕ портируется')
        out.append('    return')

    # --- сборка файла ---
    out.append(HEADER)
    out.append('')
    out.append('label ch4_6:')
    for sc in ORDER:
        out.append('')
        out.append('    # ==== SCENE %d ====' % sc)
        emit_scene(sc)
        if sc == 264:
            out.append('')
            out.append('    # ---- 【デート】 меню выбора даты ----')
            out.append('    $ portrait_choice([')
            out.append('        {"char": "louise",    "text": "Go on a date with Louise",     "target": "date_louise_ch4_6"},')
            out.append('        {"char": "siesta",    "text": "Go on a date with Siesta",     "target": "date_siesta_ch4_6"},')
            out.append('        {"char": "haruna",    "text": "Go on a date with Haruna",     "target": "date_haruna_ch4_6"},')
            out.append('        {"char": "henrietta", "text": "Go on a date with Henrietta",  "target": "date_henrietta_ch4_6"},')
            out.append('    ])')
            out.append('')
            out.append('    $ fade_fx("black")')
            out.append('    stop music fadeout 1.0')
            out.append('    jump attention')
            out.append('    return')

    for r in ROUTE_SCENES:
        emit_route(*r)

    text = '\n'.join(out) + '\n'

    print('voices by speaker:', V.counts)
    print('total voices:', sum(V.counts.values()))
    print('thoughts:', thought_no[0])
    if missing:
        print('\nMISSING translations: %d' % len(missing))
        for kind, key, ja in missing[:40]:
            print('  %-8s %-16s %s' % (kind, key, ja.replace('\n', ' / ')[:70]))
    else:
        print('\nall translations present')

    if args.apply:
        with io.open(SCRIPT, 'w', encoding='utf-8') as fh:
            fh.write(text)
        print('\nwritten: %s (%d lines)' % (SCRIPT, text.count('\n')))


HEADER = '''# Глава 4, часть 6 (сцены 261–268 + даты 1084–1103): финал основной линии
# (бой с Акиной, разговор с Анриеттой) и четыре маршрута дат.
# Источник: ps2_source/chapters/chapter_05_トリスタニアの危機.txt
#   (SCENE 261–268, 1084–1103). Точные аргументы:
#   ps2_source/events_full/chapter_05_トリスタニアの危機.txt.
# Скелет собран генератором tools/gen_ch4_6_script.py (EN — tools/ch4_6_en.py,
#   RU — tools/ch4_6_ru.py), поэтому порядок реплик, голоса, спрайты и
#   события совпадают с источником дословно.
#
# Сцены 265–268 — «мосты» с мыслями Саито перед каждой датой. В PS2 система
#   дат прыгает прямо в 1084/1089/1094/1099 (dateDone → next(info.next)),
#   поэтому 265–268 не проигрываются: их текст перенесён в th в начале
#   соответствующей даты (ACCEPTABLE ADAPTATION — см. reports/ch4/6.md).
#   Сцена 1063 (CG+199) — мёртвая, не портируется.
#   Сцена 269 (конец дат) — принадлежит главе 5, не портируется.
#
# Голоса: ch4.6_<spk>_<NNN> — новая группа части 6, нумерация с 001 по
#   говорящему, порядок порта (261 → 262 → 263 → 264 → 1084 → 1085–1088 →
#   1089–1093 → 1094–1098 → 1099–1103):
#   s ×112, l ×49, h ×34, si ×29, ha ×28, d ×14, ak ×4 — всего 270.
#   Мысли (th, без голоса) — 19, пункты меню — 12.
#
# Не портируются: battle() (система боя не реализована), SE (se0 +63/+65/+72,
#   se1 stop), vibrate, msgon/msgoff, waitAction, sync, point x=/y=,
#   CREATE. COFFEE → pause(1.0).
# Фоны/CG: id(37), id(64), id(70) — имена пусты в image_id_map (заглушки);
#   id(102), id(201), id(202), id(203) — CG без имён (заглушки id(K)).
#   town_square_evening, library_night, sky_night, white — имена заполнены.
# Спрайты: id → имя по references/sprite_id_map.csv; PROVISIONAL:
#   420 = s 5 shy, 471 = s 8 angry, 552 = si 6 shy, 764 = h 1, 766 = h 1 happy,
#   770 = h 1 sad, 786 = h 2, 788 = h 2 happy, 792 = h 2 sad.
#   [471 в ch4_5 показан как "s 4 angry" — не соответствует биекции блоков
#    спрайтов (434 = единственный s 4); см. отчёт части 6 и журнал.]
#   [770 = h 1 sad по унифицированной пиксель-сетке (pos 6 = sad);
#    комментарий ch4_5 ("h 1 angry") без пиксель-сверки — расхождение
#    зафиксировано (RECONCILE) в отчёте и журнале.]
#   Спрайты Акины (lay21 +1028/+1032) в игре отсутствуют — не показываются.
#
# Меню дат: три опции (Луиза/Сиеста/Харуна) повторяют EN главы 1
#   ("Go on a date with ..."), их переводы уже есть в tl (повтор old запрещён —
#   E11); добавлена только Henrietta.
#
# Файл сгенерирован tools/gen_ch4_6_script.py — правки вносить в него
#   и в tools/ch4_6_en.py, затем перегенерировать.
'''

if __name__ == '__main__':
    main()
