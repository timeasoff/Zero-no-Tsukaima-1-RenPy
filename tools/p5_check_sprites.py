# -*- coding: utf-8 -*-
"""Сверка состояний спрайтов: канон chapter_04 (сцены части 5) vs script-ch3_5.rpy.

Канон: для каждой реплики/мысли считает множество имён спрайтов по событиям
[SPRITE layN image=+K]/hide и [LAYER lay0 ...] (позиционные x=/y=/vibrate=reset
игнорируются).
Скрипт: состояние после последнего show_sprites(...) перед строкой.
Сравнение по порядку следования строк (kind+spk+cдвоек).
"""
import io
import re
import sys
from collections import Counter

CANON = "ps2_source/chapters/chapter_04_\u5973\u306e\u6226\u3044.txt"
SCRIPT = "game/chapters/3/script-ch3_5.rpy"
SMAP = "references/sprite_id_map.csv"

SPK = {
    "\u30b5\u30a4\u30c8": "s",
    "\u30eb\u30a4\u30ba": "l",
    "\u30b7\u30a8\u30b9\u30bf": "si",
    "\u30cf\u30eb\u30ca": "ha",
    "\u30ad\u30e5\u30eb\u30b1": "k",
    "\u30bf\u30d0\u30b5": "t",
    "\u30b3\u30eb\u30d9\u30fc\u30eb": "c",
    "\u30e2\u30f3\u30e2\u30e9\u30f3\u30b7\u30fc": "m",
    "\u30ae\u30fc\u30b7\u30e5": "g",
}

# ручные override для id, отсутствующих в sprite_id_map
OVERRIDES = {931: "c 1 happy"}

SCENES = (
    list(range(169, 179)) + [179, 180, 181, 182] +
    list(range(1322, 1342))
)


def load_sprite_map():
    m = dict(OVERRIDES)
    for ln in io.open(SMAP, encoding="utf-8").read().splitlines():
        p = ln.split(",")
        if p[0].isdigit() and len(p) > 1 and p[1]:
            m.setdefault(int(p[0]), p[1])
    return m


def canon_items(smap):
    text = io.open(CANON, encoding="utf-8").read().splitlines()
    items = []
    scene = None
    cur = None
    state = set()
    active = False  # внутри текущей реплики
    for ln in text:
        m = re.match(r"---- SCENE (\d+) ----", ln)
        if m:
            scene = int(m.group(1))
            cur = None
            state = set()
            active = False
            continue
        if scene not in SCENES:
            continue
        # события спрайтов
        m = re.search(r"\[SPRITE\s+\S+\s+(.*)\]", ln)
        if m:
            args = m.group(1)
            im = re.search(r"image=\+(\d+)", args)
            if im:
                sid = int(im.group(1))
                name = smap.get(sid)
                if name is None:
                    state.add("?%d" % sid)
                else:
                    state.add(name)
            elif "hide" in args:
                pass  # полный набор сравнит итог к реплике; hide важен — снимаем всё?
                # hide конкретного слоя: нужен слой
                lay = re.match(r"\[SPRITE\s+(\S+)", ln).group(1)
                # слои участвуют через имена: убираем имя, стоявшее на слое ранее
                state.discard(LAYER_NAME.get(lay, ""))
            continue
        m = re.search(r"\[LAYER\s+(\S+)\s+(.*)\]", ln)
        if m:
            lay, args = m.group(1), m.group(2)
            im = re.search(r"image=\+(\d+)", args)
            if im:
                sid = int(im.group(1))
                name = smap.get(sid, "?%d" % sid)
                state.add(name)
                LAYER_NAME[lay] = name
            elif "hide" in args:
                state.discard(LAYER_NAME.get(lay, ""))
            continue
        if ln.startswith("["):
            continue
        if ln.startswith("  "):
            continue  # выборы/next/прочее события
        if not ln.strip():
            active = False
            continue
        m = re.match(r"\s*([^\s：:]+)：(.*)$", ln)
        if m and m.group(1) in SPK:
            cur = SPK[m.group(1)]
            textbuf = [m.group(2)]
            pending = True
            # начало новой реплики: фиксируем предыдущую
            if active:
                pass
            active = "utter"
            items.append(None)  # placeholder заполняем при завершении? проще: читаем сразу
            items.pop()
            cur_utt = {"spk": cur, "parts": [m.group(2)], "voice": None,
                       "scene": scene}
            v = re.search(r"\[voice (\d+)\]", ln)
            if v:
                cur_utt["voice"] = int(v.group(1))
            UTTS.append(cur_utt)
            active = cur_utt
            continue
        if active:
            v = re.search(r"\[voice (\d+)\]", ln)
            if v:
                active["voice"] = int(v.group(1))
            else:
                active["parts"].append(ln)
                # спрайтовые события уже обработаны выше; строка-продолжение
    # (спрайтовое состояние фиксируется в момент строки-реплики)
    return items


# глобальный буфер реплик канона
UTTS = []
LAYER_NAME = {}


def canon_flow(smap):
    """Один проход: возвращает [(kind, spk, state_frozenset, text)]."""
    UTTS.clear()
    LAYER_NAME.clear()
    text = io.open(CANON, encoding="utf-8").read().splitlines()
    out = []
    scene = None
    cur = None
    state = set()
    utt = None
    for ln in text:
        m = re.match(r"---- SCENE (\d+) ----", ln)
        if m:
            scene = int(m.group(1))
            cur = None
            state = set()
            LAYER_NAME.clear()
            utt = None
            continue
        if scene not in SCENES:
            continue
        st = ln.strip()
        if st.startswith("["):
            m = re.search(r"\[SPRITE\s+(\S+)\s+(.*)\]", st)
            if m:
                lay, args = m.group(1), m.group(2)
                im = re.search(r"image=\+(\d+)", args)
                if im:
                    sid = int(im.group(1))
                    name = smap.get(sid, "?%d" % sid)
                    old = LAYER_NAME.get(lay)
                    if old:
                        state.discard(old)
                    state.add(name)
                    LAYER_NAME[lay] = name
                elif re.search(r"\bhide\b", args):
                    nm = LAYER_NAME.pop(lay, None)
                    if nm:
                        state.discard(nm)
                continue
            m = re.search(r"\[LAYER\s+(\S+)\s+(.*)\]", st)
            if m:
                lay, args = m.group(1), m.group(2)
                im = re.search(r"image=\+(\d+)", args)
                if im:
                    sid = int(im.group(1))
                    name = smap.get(sid, "?%d" % sid)
                    old = LAYER_NAME.get(lay)
                    if old:
                        state.discard(old)
                    state.add(name)
                    LAYER_NAME[lay] = name
                elif re.search(r"\bhide\b", args):
                    nm = LAYER_NAME.pop(lay, None)
                    if nm:
                        state.discard(nm)
                continue
            continue
        if ln.startswith("  \u3010"):  # 【選択肢】/【移動】/【好感度】
            if "\u9078\u629e\u80a2" in ln or "\u79fb\u52d5" in ln:
                out.append(("menu", None, frozenset(state), ln.strip()))
            continue
        if ln.startswith("  "):
            continue
        if not ln.strip():
            utt = None
            continue
        m = re.match(r"\s*([^\s：:]+)：(.*)$", ln)
        if m and m.group(1) in SPK:
            body = m.group(2)
            spk0 = "th" if body.startswith("\uff08") else SPK[m.group(1)]
            v = re.search(r"\[voice (\d+)\]", body)
            utt = {
                "spk": spk0,
                "parts": [re.sub(r"\s*\[voice \d+\]", "", body)],
                "voice": int(v.group(1)) if v else None,
                "state": frozenset(state),
            }
            out.append(("item", utt["spk"], utt["state"], utt))
            continue
        # continuation
        if utt is not None:
            v = re.search(r"\[voice (\d+)\]", ln)
            if v:
                utt["voice"] = int(v.group(1))
                utt["parts"].append(re.sub(r"\s*\[voice \d+\]", "", ln))
            else:
                utt["parts"].append(ln)
            utt["state"] = utt["state"]  # state фиксирован на начале
        # если утт None — это строки не-реплик (маловероятно)
    return out


def canon_items_flat(smap):
    flow = canon_flow(smap)
    items = []
    for kind, spk, state, payload in flow:
        if kind == "menu":
            continue
        items.append((spk, state, payload))
    return items


def script_items():
    lines = io.open(SCRIPT, encoding="utf-8").read().splitlines()
    items = []
    state = set()
    for ln in lines:
        m = re.search(r"\$ show_sprites\((.*)\)\s*$", ln)
        if m:
            inner = m.group(1)
            if inner.strip() == "None":
                state = set()
            else:
                state = set(re.findall(r'"([^"]+)"', inner))
            continue
        m = re.match(r'\s*(s|l|si|ha|k|t|c|m|g|th) "(.*)"$', ln)
        if m:
            spk = m.group(1)
            items.append((spk, frozenset(state), m.group(2)))
    return items


def main():
    smap = load_sprite_map()
    c = canon_items_flat(smap)
    s = script_items()
    print("canon items: %d" % len(c))
    print("script items: %d" % len(s))
    errors = []
    if len(c) != len(s):
        errors.append("COUNT: canon=%d script=%d" % (len(c), len(s)))
    for i, (cc, ss) in enumerate(zip(c, s)):
        if cc[0] != ss[0]:
            errors.append("#%d spk: canon=%s script=%s" % (i, cc[0], ss[0]))
            continue
        if cc[1] != ss[1]:
            missing = sorted(cc[1] - ss[1])
            extra = sorted(ss[1] - cc[1])
            errors.append("#%d [%s] canon=%s script=%s | miss=%s extra=%s | %r"
                          % (i, ss[0], sorted(cc[1]), sorted(ss[1]),
                             missing, extra, ss[2][:60]))
    if errors:
        print("RESULT: FAIL (%d)" % len(errors))
        for e in errors[:60]:
            print("  " + e)
        return 1
    print("RESULT: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
