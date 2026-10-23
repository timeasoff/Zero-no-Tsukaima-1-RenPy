# -*- coding: utf-8 -*-
"""Полная пересборка game/ch5_6/script-ch5_6.rpy.

Структура части 6 (глубинный-first, как в эталоне ch1_10):
  сцена 335 core (4 мысли Сайта — пауза перед объявлением ролей)
  -> меню выбора локации (5 веток)
      каждая ветка = head + мини-меню выбора + rejoin-сцена (кроме Уэзерби)
  -> jump ch5_7 (сцена 341 core — часть 7).

Голоса = depth-first порядок по веткам:
  [1408,1409,1410,1411,1412], [1413,1414,1415,1416,1417],
  [1418,1419,1420,1421,1422], [1423,1424,1425,1426,1427], [1428]
Нумерация: ch5.6_<spk>_<NNN>, NNN — порядковый по говорящему в этом потоке.
Всего: 127 голосовых + 17 мыслей.

EN → инструменты/ch5_6_en.py, RU → tools/ch5_6_ru.py, JA → events-источник.
old/new пары → tl/japanese, tl/russian (tools/gen_ch5_6_tl.py).
Голоса → references/voice_id_map.csv (tools/apply --manifest).

Использование:
    python tools/gen_ch5_6_script2.py            # dry-run: счётчики, пропуски
    python tools/gen_ch5_6_script2.py --apply    # записать .rpy
    python tools/gen_ch5_6_script2.py --manifest # дописать voice_id_map.csv
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, 'game', 'chapters', '5', 'script-ch5_6.rpy')
SRC = os.path.join(ROOT, 'ps2_source', 'events_full',
                   'chapter_06_本当の想い.txt')

# ------------------------------------------------------- структура (depth-first)
# CHAINS = порядок обхода = порядок нумерации голосов (register6.py)
CHAINS = [
    [1408, 1409, 1410, 1411, 1412],  # ветка "舞台": Курке/Харуна
    [1413, 1414, 1415, 1416, 1417],  # ветка "劇場": Луиза/ギーシュ
    [1418, 1419, 1420, 1421, 1422],  # ветка "表通り(1)": Сиеста/Монмон
    [1423, 1424, 1425, 1426, 1427],  # ветка "宿": タバサ/アンリエッタ
    [1428],                          # ветка "表通り(2)": ウェザリー
]
# дерево для сборки: (сцена-заголовок, ветки, rejoin)
FLOW = [
    (335, [1408, 1413, 1418, 1423, 1428], None),  # core: меню выбора локации
    (1408, [1409, 1410, 1411], 1412),
    (1413, [1414, 1415, 1416], 1417),
    (1418, [1419, 1420, 1421], 1422),
    (1423, [1424, 1425, 1426], 1427),
    (1428, [], None),
]
MONTAGE = {}

# -------------------------------------------------------------- справочники
SPK = {'サイト': 's', 'ルイズ': 'l', 'ハルナ': 'ha', 'シエスタ': 'si',
       'デルフリンガー': 'd', 'キュルケ': 'k', 'タバサ': 't', 'ギーシュ': 'g',
       'モンモランシー': 'm', 'ウェザリー': 'w', 'アンリエッタ': 'h',
       'null': 'th'}
SYM_KEY = {'l': 'louise', 'ha': 'haruna', 'si': 'siesta', 'k': 'kirche',
           't': 'tabitha', 'h': 'henrietta', 's': 'saito', 'd': 'derflinger',
           'g': 'guiche', 'm': 'montmorency', 'w': 'weatherby'}

SPRITES = {}
IMAGES = {}
with io.open(os.path.join(ROOT, 'references', 'sprite_id_map.csv'),
             encoding='utf-8') as fh:
    for ln in fh:
        p = ln.rstrip('\n').split(',')
        if p and p[0].isdigit():
            SPRITES[int(p[0])] = p[1] if len(p) > 1 else ''
with io.open(os.path.join(ROOT, 'references', 'image_id_map.csv'),
             encoding='utf-8') as fh:
    for ln in fh:
        p = ln.rstrip('\n').split(',')
        if p and p[0].isdigit():
            IMAGES[int(p[0])] = (p[1], p[2] if len(p) > 2 else '')


def flat(s):
    return s.replace('\n', ' ')


def bg_name(i):
    kind, fn = IMAGES.get(i, ('bg', ''))
    if not fn:
        return 'id(%d)' % i, kind == 'cg'
    return fn, kind == 'cg'


# ---------------------------------------------------------- разбор events
RE_SET = re.compile(r'^SET\s+set\("(\w+)",\s*\{(.*)\}\)\s*$')
RE_TALK = re.compile(r'^DIALOGUE\s+talk\((.*)\)\s*$')
RE_LIKE = re.compile(r'^LIKE\s+like\("([^"]*)",\s*(-?\d+)\)\s*$')
RE_CHOICE = re.compile(r'^CHOICE\s+selectItem\("((?:[^"\\]|\\.)*)",\s*\(0x01000000 \+(\d+)\).*$')
RE_GOTO = re.compile(r'^GOTO\s+next\(\(0x01000000 \+(\d+)\).*$')
RE_MAPDEST = re.compile(r'^MAPDEST\s+moveItem\("([^"]*)",\s*\(0x02000000 \+\d+\),\s*\(0x01000000 \+(\d+)\)\)')
RE_IMG = re.compile(r'image\s*=\s*\(0x02000000 \+(\d+)\)')
RE_X = re.compile(r'(?<![\w])x\s*=\s*(-?\d+)')
SPLIT_ARGS = re.compile(r'"((?:[^"\\]|\\.)*)"|(\bnull\b)|\(0x0[46]000000 \+(\d+)\)')


def parse_args(args):
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
    included = {s for ch in CHAINS for s in ch} | {335}
    for ln in io.open(SRC, encoding='utf-8'):
        ln = ln.rstrip('\n')
        m = re.match(r'^## SCENE (\d+)', ln)
        if m:
            cur = int(m.group(1))
            scenes.setdefault(cur, [])
            continue
        if cur not in included:
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
            elif layer in ('se0', 'se1', 'se2', 'se3'):
                ev.append(('se', ln))
            elif layer in ('lay0', 'lay1', 'lay2', 'lay3', 'lay4', 'lay5',
                           'lay6', 'lay7', 'lay8', 'lay20'):
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

        if ln.startswith('MENUINIT') or ln.startswith('MENU '):
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
                or ln.startswith('BACK') or ln.startswith('skip') or ln.startswith('SKIP') \
                or ln.startswith('MOVE') or ln.startswith('MOVEINIT') \
                or ln.startswith('MAPDEST') or ln.startswith('checkRoute'):
            continue
        elif ln.strip():
            ev.append(('misc', ln))
    return scenes


# ----------------------------------------------------------- голосовая карта
class VoiceRegistry(object):
    """Генерация имен голосов depth-first по CHAINS (register6.py)."""
    def __init__(self):
        self.names = []
        self.counts = {}

    def name(self, spk):
        key = SPK.get(spk, 'x')
        self.counts[key] = self.counts.get(key, 0) + 1
        n = 'ch5.6_%s_%03d' % (key, self.counts[key])
        self.names.append(n)
        return n


def load_mappings():
    sys.path.insert(0, ROOT)
    sys.path.insert(0, os.path.join(ROOT, '.tmp'))
    import mapping6
    from ch5_6_en import EN_DIALOGS, EN_THOUGHTS, EN_CHOICES
    from ch5_6_ru import RU_DIALOGS, RU_THOUGHTS, RU_CHOICES
    return (mapping6.VOICE_MAP, mapping6.THOUGHT_MAP, mapping6.CHOICE_MAP,
            mapping6.FRESH_IN_PIN, EN_DIALOGS, EN_THOUGHTS, EN_CHOICES,
            RU_DIALOGS, RU_THOUGHTS, RU_CHOICES)


def resolve_dlg(vn, EN_DIALOGS, VOICE_MAP, FRESH_IN_PIN):
    """EN-перевод для нового голоса vn: старая запись, merge или fresh."""
    rec = VOICE_MAP.get(vn, ('old', vn))
    if rec[0] == 'old':
        return EN_DIALOGS.get(rec[1])
    if rec[0] == 'merge':
        parts = []
        for k in rec[1]:
            e = EN_DIALOGS.get(k)
            if e:
                parts.append(flat(e))
        return ' '.join(parts) if parts else None
    if rec[0] == 'fresh':
        return rec[1][0]
    return EN_DIALOGS.get(vn)


def resolve_th(tag, EN_THOUGHTS, THOUGHT_MAP):
    rec = THOUGHT_MAP.get(tag, ('old', tag))
    if rec[0] == 'old':
        return EN_THOUGHTS.get(rec[1])
    return EN_THOUGHTS.get(tag)


def resolve_choice(target, EN_CHOICES, CHOICE_MAP):
    rec = CHOICE_MAP.get(str(target), ('old', str(target)))
    if rec[0] == 'old':
        return EN_CHOICES.get(rec[1])
    return EN_CHOICES.get(str(target))


def build_loc_ja(scenes):
    """Карта target-scene -> JA-название локации из SCENE 335 MAPDEST."""
    locs = {}
    for ln in io.open(SRC, encoding='utf-8'):
        m = RE_MAPDEST.match(ln.rstrip('\n'))
        if m:
            locs[int(m.group(2))] = m.group(1)
    return locs


# --------------------------------------------------------------- сборка .rpy
def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--manifest', action='store_true')
    args = ap.parse_args()

    (VOICE_MAP, THOUGHT_MAP, CHOICE_MAP, FRESH_IN_PIN,
     EN_DIALOGS, EN_THOUGHTS, EN_CHOICES,
     RU_DIALOGS, RU_THOUGHTS, RU_CHOICES) = load_mappings()

    scenes = parse_events()
    loc_ja = build_loc_ja(scenes)  # target -> JA location name
    V = VoiceRegistry()
    missing = []
    collisions = []

    # порядок обхода = порядок генерации имен (CHAINS)
    order = [s for ch in CHAINS for s in ch]

    vmap = {}      # (sc, i) -> voice name
    vid_of = {}    # voice name -> vid
    for sc in order:
        for i, e in enumerate(scenes.get(sc, [])):
            if e[0] == 'talk' and e[4] is not None:
                vmap[(sc, i)] = V.name(e[1])
                vid_of[vmap[(sc, i)]] = e[4]

    # подсчёт повторов для авто-тегов
    en_counter = {}
    for sc in order:
        for i, e in enumerate(scenes.get(sc, [])):
            if e[0] == 'talk' and e[4] is not None:
                vn = vmap.get((sc, i))
                en = resolve_dlg(vn, EN_DIALOGS, VOICE_MAP, FRESH_IN_PIN)
                if en is not None:
                    en_counter[flat(en)] = en_counter.get(flat(en), 0) + 1
            elif e[0] == 'choice':
                en = resolve_choice(e[2], EN_CHOICES, CHOICE_MAP)
                if en is not None:
                    en_counter[flat(en)] = en_counter.get(flat(en), 0) + 1

    def uniq_tag(en, tag):
        if '{#' in en:
            return en
        if en_counter.get(en, 0) <= 1:
            return en
        return '%s{#%s}' % (en, tag)

    out = []
    state = {'layers': {}, 'bg': None, 'cg': None, 'bgm': None,
             '_vis': None}
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
                continue
            names.append(nm)
        return names

    def emit_sprites(indent='    '):
        vis = visible()
        key = tuple(vis)
        if key == state.get('_vis') and not vis:
            return
        state['_vis'] = key
        if not vis:
            out.append('%s$ show_sprites()' % indent)
        else:
            out.append('%s$ show_sprites((%s))' % (
                indent, ', '.join('"%s"' % v for v in vis)))

    def cur_bgm_line():
        for i in range(len(out) - 1, -1, -1):
            s = out[i].strip()
            if s.startswith('#'):
                continue
            if s.startswith('$ fade_fx(') and 'new_music' not in s:
                return i
            return None
        return None

    def emit_scene(sc, indent='    '):
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
                    state['cg'] = None
                    out.append('%s# [EVENT_CG hide] — поглощается переходом на CG' % indent)
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
                st = state['layers'].setdefault(lay,
                                                {'img': None, 'x': None,
                                                 'vis': False, 'level': 160})
                st['img'] = img
                st['vis'] = True
                if x is not None:
                    st['x'] = x
                nm = SPRITES.get(img, 'id(%d)' % img)
                out.append('%s# [%s +%d → %s]' % (indent, lay, img, nm))
                emit_sprites(indent=indent)
            elif k == 'sprite_hide':
                lay = e[1]
                st = state['layers'].setdefault(lay,
                                                {'img': None, 'x': None,
                                                 'vis': False, 'level': 160})
                st['vis'] = False
                out.append('%s# [%s hide]' % (indent, lay))
                emit_sprites(indent=indent)
            elif k == 'sprite_pos':
                lay, x = e[1], e[2]
                st = state['layers'].setdefault(lay,
                                                {'img': None, 'x': None,
                                                 'vis': False, 'level': 160})
                st['x'] = x
                out.append('%s# [%s x=%d]' % (indent, lay, x))
                emit_sprites(indent=indent)
            elif k == 'talk':
                spk, disp, text, vid = e[1], e[2], e[3], e[4]
                if vid is None:
                    thought_no[0] += 1
                    tag = 'ch5.6_th_%03d' % thought_no[0]
                    en = resolve_th(tag, EN_THOUGHTS, THOUGHT_MAP)
                    if en is None:
                        missing.append(('thought', tag, text))
                        en = '@@MISSING_%s@@' % tag
                    en = flat(en)
                    out.append('%sth "%s{#%s}"' % (indent, en, tag))
                    out.append('%s# JA: %s' % (indent, text.replace('\\n', ' / ')))
                else:
                    vn = vmap.get((sc, i))
                    key = SPK.get(spk, 'x')
                    en = resolve_dlg(vn, EN_DIALOGS, VOICE_MAP, FRESH_IN_PIN)
                    if en is None:
                        missing.append(('dialog', vn, text))
                        en = '@@MISSING_%s@@' % vn
                    en = flat(en)
                    tag = 'ch5_6_v%s' % vid
                    out.append('%svoice "%s"' % (indent, vn))
                    who = key
                    out.append('%s%s "%s{#%s}"' % (indent, who, en, tag))
                    out.append('%s# JA[%s]: %s' % (indent, vid,
                                                   text.replace('\\n', ' / ')))
            elif k == 'like':
                key_sym = SPK.get(e[1], 'x')
                out.append('%s$ update_sympathy(%d, char_key="%s")' % (
                    indent, e[2], SYM_KEY.get(key_sym, key_sym)))
            elif k == 'choice':
                pass
            elif k == 'trans':
                out.append('%s# [%s] — переход выполняется fade_fx' % (
                    indent, e[1].replace('  ', ' ')))
            elif k == 'coffee':
                out.append('%s# [COFFEE] → pause(1.0)' % indent)
                out.append('%s$ pause(1.0)' % indent)
            elif k == 'battle':
                out.append('%s# [BATTLE %s] — система боя не реализована, вызов не переносится'
                           % (indent, e[1]))
            elif k == 'item':
                out.append('%s# [ITEM %s] — система инвентаря не реализована, вызов не переносится'
                           % (indent, e[1]))
            elif k == 'tndl':
                out.append('%s# [%s] — не переносится (система не реализована, AGENTS §6)'
                           % (indent, e[1]))
            elif k == 'reset':
                out.append('%s# [%s] — сброс сцены: спрайты скрываются' % (indent, e[1]))
                state['layers'] = {}
                state['_vis'] = None
                out.append('%s$ show_sprites()' % indent)
            elif k == 'title':
                out.append('%s# [%s] — титульная карточка → overlay_screen' % (
                    indent, e[1]))
            elif k == 'se':
                out.append('%s# [%s] — SE не портируется' % (indent, e[1]))
            elif k == 'misc':
                out.append('%s# [%s] — не портируется' % (indent, e[1]))

    def emit_menu(sc, branches, rejoin, indent='    '):
        out.append('')
        out.append('%s# ---- 【選択肢】 — выбор локации (【移動】) ----' % indent)
        out.append('%smenu:' % indent)
        for target in branches:
            jt = ''
            for e in scenes.get(sc, []):
                if e[0] == 'choice' and e[2] == target:
                    jt = e[1]
                    break
            en = resolve_choice(target, EN_CHOICES, CHOICE_MAP)
            if en is None:
                missing.append(('choice', str(target), jt))
                en = '@@MISSING_choice_%s@@' % target
            en = uniq_tag(en, 'ch5_6_c%s' % target)
            out.append('%s    "%s":' % (indent, en))
            out.append('%s        # JA: %s' % (indent, jt))
            out.append('%s        # ==== SCENE %d (переход после вариантов) ====' % (
                indent, target))
            emit_scene(target, indent=indent + '    ')
            if target == rejoin:
                out.append('%s        # ==== SCENE %d (rejoin, после мини-меню) ===='
                           % (indent, rejoin))
                emit_scene(rejoin, indent=indent + '    ')

    def emit_main_flow():
        """Сцена 335 -> главное меню выбора локации (5 веток),
        каждая ветка = head + мини-меню + rejoin -> jump."""
        emitted.add(335)
        out.append('')
        out.append('    # ==== SCENE 335 (core: пауза перед объявлением ролей) ====')
        emit_scene(335)
        out.append('')
        out.append('    # ---- 【選択肢】 — выбор локации (【移動】) ----')
        out.append('    menu:')
        for target in [1408, 1413, 1418, 1423, 1428]:
            tree = next(t for t in FLOW if t[0] == target)
            sc, branches, rejoin = tree
            # главная ветка — head сцена
            jt = loc_ja.get(target, '')
            en = resolve_choice(target, EN_CHOICES, CHOICE_MAP)
            if en is None:
                missing.append(('choice', str(target), jt))
                en = '@@MISSING_choice_%s@@' % target
            en = flat(en)
            out.append('        "%s{#ch5_6_c%s}":' % (en, target))
            out.append('            # JA: %s' % jt)
            out.append('            # ==== SCENE %d (ветка: head) ====' % sc)
            emit_once(sc, indent='            ')
            # внутри ветки — мини-меню выбора внутри-сцены
            if branches:
                out.append('            # ---- 【選択肢】 — выбор места в локации ----')
                out.append('            menu:')
                for br in branches:
                    jt2 = ''
                    for e in scenes.get(sc, []):
                        if e[0] == 'choice' and e[2] == br:
                            jt2 = e[1]
                            break
                    en2 = resolve_choice(br, EN_CHOICES, CHOICE_MAP)
                    if en2 is None:
                        missing.append(('choice', str(br), jt2))
                        en2 = '@@MISSING_choice_%s@@' % br
                    en2 = flat(en2)
                    out.append('                "%s{#ch5_6_c%s}":' % (en2, br))
                    out.append('                    # JA: %s' % jt2)
                    out.append('                    # ==== SCENE %d ====' % br)
                    emit_once(br, indent='                    ')
                if rejoin:
                    out.append('            # ==== SCENE %d (rejoin, после мини-меню) ===='
                               % rejoin)
                    emit_once(rejoin, indent='            ')

    # ------------------------------------------------------------------- тело
    out.append(HEADER)
    out.append('')
    out.append('label ch5_6:')
    out.append('    # Часть 6: сцена 335 — пауза перед объявлением ролей + меню')
    out.append('    # выбора локации; extra-блок 1408–1428 — 5 веток (Курке/Харуна,')
    out.append('    # Луиза/ギーシュ, Сиеста/Монモン, タバサ/アンリエッタ, ウェザリー).')
    out.append('    # Сцены 341–343 (core) не входят — ведут в extra-цепочки')
    out.append('    # (1104–1163 состав, 1870–1875 меню дат), портируются отдельно.')
    out.append('')

    # регистр излучённых сцен (чтобы не дублировать в ветках)
    emitted = set()

    def emit_once(sc, indent='        '):
        if sc in emitted:
            return
        emitted.add(sc)
        emit_scene(sc, indent=indent)

    emit_main_flow()

    # Выход из части: сцена 1428 заканчивается MOVE (не переносится).
    # Сцена 341 (core, объявление ролей) — первая сцена части 7.
    out.append('')
    out.append('    # [移動] → next(341): сцена 341 (core) — часть 7 главы 5')
    out.append('    jump ch5_7')

    text = '\n'.join(out) + '\n'

    print('voices by speaker:', V.counts)
    print('total voices:', sum(V.counts.values()))
    print('thoughts:', thought_no[0])
    print('unique voice names:', len(set(V.names)), 'total names:', len(V.names))
    if missing:
        print('\nMISSING translations: %d' % len(missing))
        for kind, key, ja in missing[:60]:
            print('  %-8s %-16s %s' % (kind, key, ja.replace('\n', ' / ')[:70]))
    else:
        print('\nall translations present')

    if collisions:
        print('\nCOLLISIONS with existing tl (auto-tag): %d' % len(collisions))
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


HEADER = '''# Глава 5, часть 6 (сцена 335 core + extra-блок 1408–1428): пауза перед
# объявлением ролей, меню выбора локации; 5 веток — Курке/ハルナ, ルイズ/ギーシュ,
# シエスタ/モンモランシー, タバサ/アンリエッタ, ウェザリー.
# Источник: ps2_source/chapters/chapter_06_本当の想い.txt (SCENE 335; extra
#   1408–1428). Точные аргументы: ps2_source/events_full/chapter_06_本当の想い.txt.
#
# Структура пересобрана (tools/gen_ch5_6_script2.py): сцена 335 -> главное меню
#   5 веток -> каждая ветка = head + мини-меню выбора + rejoin. Порядок реплик,
#   голоса, спрайты и события строго из источника (depth-first обход).
# EN — tools/ch5_6_en.py, RU — tools/ch5_6_ru.py, JA — events-источник.
# old/new пары переводов — tools/gen_ch5_6_tl.py (tl/japanese, tl/russian).
# Голоса — references/voice_id_map.csv (tools/gen_ch5_6_script2.py --manifest).
#
# Вход — jump ch5_6 из script-ch5_5.rpy (сцена 335). Выход — jump ch5_7
#   (сцена 341, core, объявление ролей); сцена 341 ведет в extra-ветки состава
#   (1104–1163), которые портируются отдельно (sp-файл).
#
# Голоса: ch5.6_<spk>_<NNN> — новая группа части 6, нумерация с 001 по
#   говорящему, порядок порта: 1408->1409/1410/1411->1412,
#   1413->1414/1415/1416->1417, 1418->1419/1420/1421->1422,
#   1423->1424/1425/1426->1427, 1428. Всего 127 голосов (+17 мыслей).
#
# mapping old->new (из tools/.tmp/mapping6.py): k — пропуск 3000; ha —
#   merge(1949), split(1951); h — split(473+474); s — merge(9937); t — пропуски;
#   w — сдвиг +8; l/g/m/si — сдвиг +2; fresh: k_002=「あら、ダーリン！」,
#   ha_002=「ひ、平賀くん！」.
#
# Не портируются:
#   - сцена 341 (core): ведет в extra-ветки состава (1104–1163), портируются
#     отдельно (sp-файл);
#   - сцена 342 (core): ведет в меню дат 1870–1875, портируется отдельно;
#   - сцена 343 (core): пустой переход (E7 forward debt, закроется частью 7+);
#   - MOVEINIT/MAPDEST/MOVE, waitAction, msgon/msgoff — перенос карты переходов
#     PS2 не реализован;
#   - SE (se1) — не переносится.
#
# Фоны: bg 58 = stage (stub, id(58)), bg 54 = stage2 (stub id(54)),
#   bg 53/57/55/50/38/41/90 — имена пусты в image_id_map.csv (заглушки id(K));
#   имена заполняет человек через tools/build_image_id_map.py +
#   tools/replace_bg_placeholders.py --apply.
#
# Спрайты: lay20 (ウェザリー 1061/1063/1067), lay5 (サイト 390/392/429/…);
#   id спрайтов без строки в sprite_id_map.csv → заглушки id(K).
'''

if __name__ == '__main__':
    main()
