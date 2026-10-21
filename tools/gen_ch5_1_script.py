# -*- coding: utf-8 -*-
"""Сборка game/chapters/5/script-ch5_1.rpy из events-источника.

Структура, порядок реплик, голоса, спрайты и события — строго из
ps2_source/events_full/chapter_06_本当の想い.txt (сцены 269–284).
Тексты EN подставляются из tools/ch5_1_en.py, RU — из tools/ch5_1_ru.py
(для tl). JA берётся из events (дословно).

Скрипт читает events_full напрямую (без промежуточных .tmp-файлов), поэтому
воспроизводим из репозитория.

Использование:
    python tools/gen_ch5_1_script.py            # dry-run: счётчики, пропуски
    python tools/gen_ch5_1_script.py --apply    # записать .rpy
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, 'game', 'chapters', '5', 'script-ch5_1.rpy')
SRC = os.path.join(ROOT, 'ps2_source', 'events_full',
                   'chapter_06_本当の想い.txt')

# ------------------------------------------------------------------ структура
SCENES = list(range(269, 285))
# (сцена, ветки меню, сцена-слияние) — порядок как в источнике
FLOW = [
    (269, None, None),
    (270, [271, 272, 273], 274),
    (275, [276, 277, 278], 279),
    (280, [281, 282, 283], 284),
]
# титульный монтаж сцены 269 (BG 2/1145/1132/1145/2) → overlay_screen
MONTAGE = {269: [2, 1145, 1132, 1145, 2]}

# ---------------------------------------------------------------- справочники
SPK = {'サイト': 's', 'ルイズ': 'l', 'ハルナ': 'ha', 'シエスタ': 'si',
       'デルフリンガー': 'd', 'キュルケ': 'k', 'タバサ': 't', 'ギーシュ': 'g',
       'モンモランシー': 'm', 'ウェザリー': 'w', 'null': 'th'}
# симпатия: ключ char_key (sympathy.rpy: louise/haruna/henrietta/siesta/
# tabitha/kirche; для остальных — имя переменной)
SYM_KEY = {'l': 'louise', 'ha': 'haruna', 'si': 'siesta', 'k': 'kirche',
            't': 'tabitha', 'h': 'henrietta', 's': 'saito', 'd': 'derflinger',
            'g': 'guiche', 'm': 'montmorency', 'w': 'weatherby'}
# «？？？» — персонаж назван, но в источнике имя скрыто
UNK = {'k': 'unk_k', 'w': 'unk_w'}

# спрайты: id -> имя (PROVISIONAL — пиксель-сверка невозможна, см. отчёт)
SPRITE_PROV = {
    504: 'si 2 angry',
    506: 'si 2 sad',
    654: 't 7',
    742: 'k 7',
    1061: 'w 1',
    1063: 'w 1 happy',
    1065: 'w 1 angry',
    1067: 'w 1 sad',
}
# слои персонажей, встречающиеся в сценах 269–284
LAYERS = ['lay0', 'lay1', 'lay2', 'lay3', 'lay4', 'lay5', 'lay6', 'lay7',
          'lay11', 'lay12', 'lay19', 'lay20']
SE_LAYERS = ('se0', 'se1', 'se2', 'se3')


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
for _k, _v in SPRITE_PROV.items():
    SPRITES.setdefault(_k, _v)


def esc(s):
    """экранирование строки для .rpy (переводы строк -> \\n, кавычки -> \\")."""
    return s.replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"')


def flat(s):
    """Склейка переносов строки в пробел (конвенция глав 0–4: одна реплика —
    одна строка в сценарии; JA в tl сохраняет переносы через '　')."""
    return s.replace('\n', ' ')


def load_tl_olds():
    """old из tl/{japanese,russian} — ЧУЖИЕ части (свои строки исключены)."""
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
    out = set(o for o in out if '#ch5_' not in o)
    try:
        from ch5_1_en import EN_DIALOGS, EN_THOUGHTS, EN_CHOICES
        for _d in (EN_DIALOGS, EN_THOUGHTS, EN_CHOICES):
            for _v in _d.values():
                out.discard(_v)
                out.discard(flat(_v))
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
RE_ITEM = re.compile(r'^ITEM\s+(item\(.*\))\s*$')
RE_IMG = re.compile(r'image\s*=\s*\(0x02000000 \+(\d+)\)')
RE_X = re.compile(r'(?<![\w])x\s*=\s*(-?\d+)')

SPLIT_ARGS = re.compile(r'"((?:[^"\\]|\\.)*)"|(\bnull\b)|\(0x0[46]000000 \+(\d+)\)')


def parse_args(args):
    """-> (spk, disp, text, voice_id) для talk(...)."""
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
    for ln in io.open(SRC, encoding='utf-8'):
        ln = ln.rstrip('\n')
        m = re.match(r'^## SCENE (\d+)', ln)
        if m:
            cur = int(m.group(1))
            scenes.setdefault(cur, [])
            continue
        if cur not in SCENES:
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
            elif layer == 'white':
                if hide:
                    ev.append(('white_hide',))
                elif img:
                    ev.append(('white_show', int(img.group(1))))
            elif layer in SE_LAYERS:
                ev.append(('se', ln))
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

        m = RE_ITEM.match(ln)
        if m:
            ev.append(('item', m.group(1)))
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
        elif ln.startswith('TNDL'):
            ev.append(('tndl', ln))
        elif ln.startswith('RESET'):
            ev.append(('reset', ln))
        elif ln.startswith('TITLE'):
            ev.append(('title', ln))
        elif ln.startswith('SYNC') or ln.startswith('CREATE'):
            continue
        elif ln.startswith('VIBRATE') or ln.startswith('vibrate'):
            ev.append(('se', ln))
        elif re.match(r'^(SE|se\d)\b', ln):
            ev.append(('se', ln))
        elif ln.startswith('wait') or ln.startswith('WAIT') or ln.startswith('msg') \
                or ln.startswith('MSG') or ln.startswith('back') \
                or ln.startswith('BACK') or ln.startswith('skip') or ln.startswith('SKIP'):
            # окно/ожидание/сброс — служебные, Ren'Py управляет окном сам
            continue
        elif ln.strip():
            ev.append(('misc', ln))
    return scenes


# ---------------------------------------------------------------- голоса
class Voices(object):
    def __init__(self):
        self.counts = {}

    def name(self, spk):
        key = SPK.get(spk, 'x')
        if key == 'th':
            return None
        self.counts[key] = self.counts.get(key, 0) + 1
        return 'ch5_%s_%03d' % (key, self.counts[key])


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--manifest', action='store_true',
                    help='дописать строки voice_name,voice_id в references/voice_id_map.csv')
    args = ap.parse_args()

    try:
        from ch5_1_en import EN_DIALOGS, EN_THOUGHTS, EN_CHOICES
    except ImportError:
        EN_DIALOGS, EN_THOUGHTS, EN_CHOICES = {}, {}, {}

    scenes = parse_events()
    V = Voices()
    missing = []
    collisions = []

    def scene_events(sc):
        return scenes.get(sc, [])

    # 1) нумерация голосов: порядок сцен как в сценарии
    vmap = {}
    vid_of = {}
    order = []
    for sc, branches, rejoin in FLOW:
        order.append(sc)
        if branches:
            order.extend(branches)
        if rejoin:
            order.append(rejoin)
    for sc in order:
        for i, e in enumerate(scene_events(sc)):
            if e[0] == 'talk' and e[4] is not None:
                vmap[(sc, i)] = V.name(e[1])
                vid_of[vmap[(sc, i)]] = e[4]

    # 2) подсчёт повторов EN (E11: одинаковый old нельзя повторять)
    en_counter = {}
    for sc in order:
        for i, e in enumerate(scene_events(sc)):
            if e[0] == 'talk' and e[4] is not None:
                en = EN_DIALOGS.get(vmap.get((sc, i)))
                if en is not None:
                    en = flat(en)
                    en_counter[en] = en_counter.get(en, 0) + 1
            elif e[0] == 'choice':
                en = EN_CHOICES.get(str(e[2]))
                if en is not None:
                    en = flat(en)
                    en_counter[en] = en_counter.get(en, 0) + 1

    def uniq_tag(en, tag):
        """тег нужен, только если строка повторяется внутри части; явный тег
        (уже в данных EN) сохраняется."""
        if '{#' in en:
            return en
        if en_counter.get(en, 0) <= 1:
            return en
        return '%s{#%s}' % (en, tag)

    # 3) генерация кода
    out = []
    state = {'layers': {}, 'bg': None, 'cg': None, 'bgm': None}
    thought_no = [0]

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
        names = []
        for it in items:
            nm = SPRITES.get(it[3], 'id(%d)' % it[3])
            if nm in names:
                # одинаковый тег спрайта в двух слоях (mage +1108/+1105 в
                # сценах 276–279) — в Ren'Py второй не выводится
                continue
            names.append(nm)
        return names

    def emit_sprites(force=False, indent='    '):
        vis = visible()
        key = tuple(vis)
        if key == state.get('_vis') and not force:
            return
        state['_vis'] = key
        if not vis:
            out.append('%s$ show_sprites()' % indent)
        else:
            out.append('%s$ show_sprites((%s))' % (indent, ', '.join('"%s"' % v for v in vis)))

    def cur_bgm_line():
        """индекс последней строки fade_fx без new_music"""
        for i in range(len(out) - 1, -1, -1):
            s = out[i].strip()
            if s.startswith('#'):
                continue
            if s.startswith('$ fade_fx(') and 'new_music' not in s:
                return i
            return None
        return None

    def emit_scene(sc, indent='    '):
        evs = scene_events(sc)
        montage = MONTAGE.get(sc, [])
        for i, e in enumerate(evs):
            k = e[0]
            if k == 'bg':
                if e[1] in montage:
                    out.append('%s# [BG +%d — титульный монтаж → overlay_screen]' % (indent, e[1]))
                    continue
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
                    state['cg'] = None
                    out.append('%s# [EVENT_CG hide] — поглощается переходом на фон' % indent)
                else:
                    out.append('%s# [EVENT_CG hide]' % indent)
                    out.append('%s$ fade_fx("black")' % indent)
                    state['cg'] = None
            elif k == 'white_show':
                out.append('%s# [LAYER white +%d] → flash_fx("white")' % (indent, e[1]))
                out.append('%s$ flash_fx("white")' % indent)
            elif k == 'white_hide':
                out.append('%s# [LAYER white hide] — вспышка гаснет (fade)' % indent)
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
                st = state['layers'].setdefault(lay, {'img': None, 'x': None, 'vis': False, 'level': 160})
                st['img'] = img
                st['vis'] = True
                if x is not None:
                    st['x'] = x
                nm = SPRITES.get(img, 'id(%d)' % img)
                out.append('%s# [%s +%d → %s]' % (indent, lay, img, nm))
                emit_sprites(indent=indent)
            elif k == 'sprite_hide':
                lay = e[1]
                st = state['layers'].setdefault(lay, {'img': None, 'x': None, 'vis': False, 'level': 160})
                st['vis'] = False
                out.append('%s# [%s hide]' % (indent, lay))
                emit_sprites(indent=indent)
            elif k == 'sprite_pos':
                lay, x = e[1], e[2]
                st = state['layers'].setdefault(lay, {'img': None, 'x': None, 'vis': False, 'level': 160})
                st['x'] = x
                out.append('%s# [%s x=%d]' % (indent, lay, x))
                emit_sprites(indent=indent)
            elif k == 'talk':
                spk, disp, text, vid = e[1], e[2], e[3], e[4]
                if vid is None:
                    thought_no[0] += 1
                    tag = 'ch5_th_%03d' % thought_no[0]
                    en = EN_THOUGHTS.get(tag)
                    if en is None:
                        missing.append(('thought', tag, text))
                        en = '@@MISSING_%s@@' % tag
                    en = flat(en)
                    out.append('%sth "%s{#%s}"' % (indent, esc(en), tag))
                    out.append('%s# JA: %s' % (indent, text.replace('\\n', ' / ')))
                else:
                    vn = vmap.get((sc, i))
                    key = SPK.get(spk, 'x')
                    if disp and disp != 'null' and '？？' in disp:
                        who = UNK.get(key, key)
                    else:
                        who = key
                    en = EN_DIALOGS.get(vn)
                    if en is None:
                        missing.append(('dialog', vn, text))
                        en = '@@MISSING_%s@@' % vn
                    else:
                        if flat(en) in TL_OLDS:
                            collisions.append((vn, flat(en)))
                    en = flat(en)
                    en = uniq_tag(en, 'ch5_v%s' % vid)
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
            elif k == 'item':
                out.append('%s# [ITEM %s] — система инвентаря не реализована, вызов не переносится' % (indent, e[1]))
            elif k == 'tndl':
                out.append('%s# [%s] — не переносится (система не реализована, AGENTS §6)' % (indent, e[1]))
            elif k == 'reset':
                out.append('%s# [%s] — сброс сцены: спрайты скрываются' % (indent, e[1]))
                state['layers'] = {}
                state['_vis'] = ()
                out.append('%s$ show_sprites()' % indent)
            elif k == 'title':
                out.append('%s# [%s] — титульная карточка → overlay_screen' % (indent, e[1]))
            elif k == 'se':
                out.append('%s# [%s] — SE не портируется' % (indent, e[1]))
            elif k == 'misc':
                out.append('%s# [%s] — не портируется' % (indent, e[1]))

    def emit_menu(sc, branches, rejoin):
        out.append('')
        out.append('    # ---- 【選択肢】 ----')
        out.append('    menu:')
        for target in branches:
            jt = ''
            for e in scene_events(sc):
                if e[0] == 'choice' and e[2] == target:
                    jt = e[1]
                    break
            en = EN_CHOICES.get(str(target))
            if en is None:
                missing.append(('choice', str(target), jt))
                en = '@@MISSING_choice_%s@@' % target
            else:
                if flat(en) in TL_OLDS:
                    collisions.append(('choice %s' % target, flat(en)))
            en = flat(en)
            en = uniq_tag(en, 'ch5_c%s' % target)
            out.append('        "%s":' % esc(en))
            out.append('            # JA: %s' % jt)
            out.append('            # ==== SCENE %d ====' % target)
            emit_scene(target, indent='            ')

    # --- сборка файла ---
    out.append(HEADER)
    out.append('')
    out.append('label ch5:')
    out.append('    # Титульный монтаж (BG 2/1145/1132/1145/2) → overlay_screen (образ «overlay»).')
    out.append('    call overlay_screen("overlay", "Chapter Five: \'True Feelings\'", isUseBlur=False, text_mode="black") from _call_overlay_screen_11')
    out.append('    pause(2)')

    for sc, branches, rejoin in FLOW:
        out.append('')
        out.append('    # ==== SCENE %d ====' % sc)
        emit_scene(sc)
        if branches:
            emit_menu(sc, branches, rejoin)
            out.append('')
            out.append('    # ==== SCENE %d (переход после вариантов) ====' % rejoin)
            emit_scene(rejoin)

    out.append('')
    out.append('    # [移動] → next(285): сцена 285 — часть 2 главы 5')
    out.append('    jump ch5_2')
    out.append('    return')

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

    if collisions:
        print('\nCOLLISIONS with existing tl (нужен явный тег): %d' % len(collisions))
        for key, en in collisions:
            print('  %-16s %s' % (key, en[:80]))

    if args.apply:
        d = os.path.dirname(SCRIPT)
        if not os.path.isdir(d):
            os.makedirs(d)
        with io.open(SCRIPT, 'w', encoding='utf-8') as fh:
            fh.write(text)
        print('\nwritten: %s (%d lines)' % (SCRIPT, text.count('\n')))

    if args.manifest:
        man = os.path.join(ROOT, 'references', 'voice_id_map.csv')
        have = set()
        with io.open(man, encoding='utf-8') as fh:
            for ln in fh:
                p = ln.rstrip('\n').split(',')
                if p and p[0] and not p[0].startswith('#'):
                    have.add(p[0])
        rows = [(n, vid_of[n]) for n in sorted(vid_of) if n not in have]
        with io.open(man, 'a', encoding='utf-8') as fh:
            for n, vid in rows:
                fh.write('%s,%d\n' % (n, vid))
        print('manifest: +%d строк (%d уже были)' % (len(rows), len(vid_of) - len(rows)))


HEADER = '''# Глава 5, часть 1 (сцены 269–284): переезд в городской дом, начало
# расследования бомбиста, погоня за похитителем сумки Харуны и встреча
# с Уэзерби у городской оперы.
# Источник: ps2_source/chapters/chapter_06_本当の想い.txt (SCENE 269–284).
# Точные аргументы: ps2_source/events_full/chapter_06_本当の想い.txt.
# Скелет собран генератором tools/gen_ch5_1_script.py (EN — tools/ch5_1_en.py,
#   RU — tools/ch5_1_ru.py), поэтому порядок реплик, голоса, спрайты и
#   события совпадают с источником дословно.
#
# Титульная карточка: K=11 (10 занят script-ch4_4.rpy). Вход — jump ch5
#   из главы 4; выход — jump ch5_2 (сцена 285) — E7 «forward debt»,
#   закроется частью 2.
#
# Голоса: ch5_<spk>_<NNN> — новая группа части 1, нумерация с 001 по
#   говорящему, порядок порта (269 → 270 → 271–273 → 274 → 275 → 276–278 →
#   279 → 280 → 281–283 → 284):
#   s ×32, l ×28, ha ×28, si ×6, w ×9, d ×3, k ×7, g ×2, t ×2, m ×1 —
#   всего 118. Мысли (th, без голоса) — 16, пункты меню — 9.
#
# Не портируются: battle() (система боя не подключена — прецедент ch2_3,
#   ch3_7, ch4_6), item() (инвентарь не реализован), TNDL, SE (se0 +67/+69,
#   se1 stop), waitAction/waitTime/waitSEStop, msgon/msgoff, back(), beginSkip.
#   COFFEE → pause(1.0).
# Фоны/CG: id(41), id(50), id(129), id(130) — имена пусты в image_id_map
#   (заглушки, требуют решения человека); sky, overlay, white, cafe,
#   town_square, cafe_entrance, l_si_sleep — имена заполнены.
# Спрайты: id → имя по references/sprite_id_map.csv; PROVISIONAL (пиксель-
#   сверка недоступна — архив PS2 не подключён): 504 = si 2 angry,
#   506 = si 2 sad, 654 = t 7, 742 = k 7, 1061 = w 1, 1063 = w 1 happy,
#   1065 = w 1 angry, 1067 = w 1 sad.
#
# Меню 【選択肢】: три развилки по три варианта (сцены 270, 275, 280) —
#   варианты развёрнуты внутрь пунктов меню, слияние — общая сцена
#   (274 / 279 / 284), как в script-ch1_10.rpy и script-ch4_6.rpy.
#
# Файл сгенерирован tools/gen_ch5_1_script.py — правки вносить в него
#   и в tools/ch5_1_en.py, затем перегенерировать.
'''

if __name__ == '__main__':
    main()
