# -*- coding: utf-8 -*-
"""Генератор script-ch7_1.rpy — часть 1 главы 7 (сцены 375-388, chapter_08).

Архитектура как у tools/gen_ch5_1_script.py:
  структура и порядок — из reports/_tmp_manifest.txt (авторитетный поток
  событий), тексты JA — из ps2_source/chapters/chapter_08_*.txt,
  EN из tools/ch7_1_en.py, RU из tools/ch7_1_ru.py.

Кросс-проверки (жёсткие, без совпадения.generator падает):
  порядок и идентификаторы голосов, тексты JA (поток против глав),
  пункты меню, TNDL-якоря, итоги по говорящим, наличие всех переводов,
  резолв всех спрайтов по references/sprite_id_map.csv
  и фонов/CG по references/image_id_map.csv.

Правки текстов — в ch7_1_en.py / ch7_1_ru.py, затем перегенерация.
Запуск: python tools/gen_ch7_1_script.py
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_ch7_1_common as CC

SPR_ID = re.compile(r"image = \(0x02000000 \+(\d+)\)")
SPK_ORDER = ["l", "s", "k", "si", "t", "g", "m", "ha", "h", "w"]
MONTAGE_IDS = {2, 1145, 1167}
BG_K = {"5": "t4", "19": "t18", "20": "t19", "28": "t27"}
OVERLAY_K = 12
OUT_PATH = CC.rel("game", "chapters", "7", "script-ch7_1.rpy")

HEADER = """# Глава 7, часть 1 (сцены 375-388): «失望のお姫さま» —_title,
# интрига с бомбистом (Кирхе ведёт расследование театра), ночная вылазка
# к театру и столкновение с Уэзерби; три развилки (-choice) — части
# сливаются в общие сцены 379/384; третья развилка подводит к части 2.
# Источник: ps2_source/chapters/chapter_08_失望のお姫さま.txt (SCENE 375-388).
# Точные аргументы: ps2_source/events_full/chapter_08_失望のお姫さま.txt.
# Скелет собран генератором tools/gen_ch7_1_script.py (EN — tools/ch7_1_en.py,
#   RU — tools/ch7_1_ru.py), порядок реплик, голоса, спрайты и события
#   совпадают с источником; структура — из reports/_tmp_manifest.txt.
#
# Титульная карточка: K=12 (11 занято script-ch5_1.rpy). Вход — jump ch7
#   из главы 6; выход — jump ch7_2 (сцена 389) — E7 «forward debt»,
#   закроется частью 2.
#
# Голоса: ch7_<spk>_<NNN> — нумерация с 001 по говорящему, порядок порта
#   (375 → ветки 376/377/378 → 379 → 380 → ветки 381/382/383 → 384 → 385 →
#   ветки 386/387/388):
#   l ×37, s ×33, h ×22, k ×17, w ×18, t ×4, g ×3, si ×3, m ×2, ha ×1 —
#   всего 140. Мысли (th, без голоса) — 2, пункты меню — 9.
#
# Не портируются: ITEM ×3 (バナナ/ハート型チョコ/青汁 — инвентарь не реализован),
#   SE (se1 stop), MSGON/MSGOFF, beginSkip/endSkip, back(), waitTime/waitAction,
#   TRANS (переход выполняется fade_fx), BGU, TNDL — переносится (as tndl).
#
# Фоны/CG: id(41), id(53), id(54), id(264) — имена пусты в image_id_map
#   (заглушки id(K), требуют решения человека); 2/1145/1167 = титульный
#   монтаж (white/overlay/overlay, только в комментариях).
# Спрайты: id → имя по references/sprite_id_map.csv; PROVISIONAL (пиксель-
#   сверка недоступна — архив PS2 не подключён): 572 = g 2 sad, 621 = t 4,
#   1061 = w 1, 1063 = w 1 happy, 1065 = w 1 angry.
#
# Меню 【選択肢】: три развилки по три варианта (сцены 375, 380, 385) —
#   варианты разворачиваются внутрь пунктов меню, слияние — общая сцена
#   (379 / 384), как в script-ch5_1.rpy; третья развилка (сцена 385) уводит
#   в часть 2 (каждый вариант завершается jump ch7_2).
#
# Файл сгенерирован tools/gen_ch7_1_script.py — правки вносить в него
#   и в tools/ch7_1_en.py, затем перегенерировать.
"""


class SMap:
    """id спрайта -> имя ('l 1 angry'), из references/sprite_id_map.csv."""

    def __init__(self):
        self.m = {}
        self.prov = []
        path = CC.rel("references", "sprite_id_map.csv")
        for ln in io.open(path, encoding="utf-8-sig").read().splitlines():
            if not ln or ln.startswith("#"):
                continue
            parts = ln.split(",")
            if not re.match(r"^\d+$", parts[0].strip()):
                continue
            sid = int(parts[0])
            self.m[sid] = parts[1].strip()
            if "PROVISIONAL" in ln:
                self.prov.append(sid)

    def get(self, sid):
        if sid not in self.m:
            raise CC.Fail("спрайт id %d отсутствует в references/sprite_id_map.csv" % sid)
        return self.m[sid]


class ImMap:
    """id фона/CG -> имя; пустое filename → заглушка id(K)."""

    def __init__(self):
        self.m = {}
        path = CC.rel("references", "image_id_map.csv")
        for ln in io.open(path, encoding="utf-8-sig").read().splitlines():
            if not ln or ln.startswith("#"):
                continue
            parts = ln.split(",")
            if not re.match(r"^\d+$", parts[0].strip()):
                continue
            sid = int(parts[0])
            fname = parts[2].strip()
            self.m[sid] = fname if fname else "id(%d)" % sid

    def get(self, sid):
        if sid not in self.m:
            raise CC.Fail("фон/CG id %d отсутствует в references/image_id_map.csv" % sid)
        return self.m[sid]


class Emitter:
    def __init__(self, smap, imap, dmap, ths, chmap):
        self.L = []
        self.smap = smap
        self.imap = imap
        self.dmap = dmap
        self.ths = ths
        self.chmap = chmap
        self.vis = dict()
        self.used_th = set()
        self.used_choices = set()
        self.used_dialogs = set()

    def w(self, ind, line):
        self.L.append(("    " * ind + line) if line else "")

    def key(self, name):
        return SPK_ORDER.index(name.split(" ")[0])

    def emit_sprites(self, ind):
        names = sorted(self.vis.values(), key=self.key)
        if not names:
            self.w(ind, "$ show_sprites()")
        else:
            self.w(ind, "$ show_sprites((%s))" % ", ".join('"%s"' % n for n in names))

    # ------------------------------------------------- одиночные события
    def do_same(self, ind, ev):
        k = ev["kind"]
        if k == "RESET":
            self.w(ind, "# [RESET      reset()] — сброс сцены: спрайты скрываются")
            self.vis = {}
            self.emit_sprites(ind)
        elif k == "TITLE":
            self.w(ind, '# [TITLE      title("失望のお姫さま")] — титульная карточка → overlay_screen')
        elif k == "SKIP":
            self.w(ind, "# [SKIP       beginSkip()] — не портируется")
        elif k == "UNK3":
            self.w(ind, "# [endSkip    endSkip()] — не портируется")
        elif k == "MSGOFF":
            self.w(ind, "# [MSGOFF     msgoff()] — не портируется")
        elif k == "MSGON":
            self.w(ind, "# [MSGON      msgon()] — не портируется")
        elif k == "BACK":
            self.w(ind, "# [BACK       back()] — не портируется")
        elif k == "WAIT":
            self.w(ind, "# [WAIT       %s] — не портируется" % ev["value"])
        elif k == "ITEM":
            self.w(ind, "# [ITEM      %s] — система инвентаря не реализована, вызов не переносится" % ev["value"])
        elif k == "if":
            self.w(ind, "# [if         if(isJump())] — не портируется")
        elif k == "BGU":
            self.w(ind, "# [BGU        %s] — не портируется" % ev["value"])
        else:
            raise CC.Fail("do_same: не умеет событие %r" % ev["kind"])

    def sprite_set(self, ind, ev):
        layer, args = ev["layer"], ev["args"]
        m = SPR_ID.search(args)
        if m:
            sid = int(m.group(1))
            name = self.smap.get(sid)
            old = self.vis.get(layer)
            self.vis[layer] = name
            same = (old == name)
            self.w(ind, "# [%s +%d → %s]" % (layer, sid, name))
            if not same:
                self.emit_sprites(ind)
            return
        if ("hide = 1" in args) or ("show = 0" in args):
            self.w(ind, "# [%s hide]" % layer)
            if layer in self.vis:
                del self.vis[layer]
                self.emit_sprites(ind)
            return
        mov = []
        for tok in args.split(","):
            t = tok.strip()
            if t.startswith("x "):
                mov.append("x=%s" % t.split("=", 1)[1].strip())
            elif t.startswith("y "):
                mov.append("y=%s" % t.split("=", 1)[1].strip())
        self.w(ind, "# [%s %s]" % (layer, ",".join(mov) if mov else "dr/anim"))

    def bg(self, ind, ev, fold=None):
        v = ev["value"]
        if v == "hide":
            self.w(ind, "# [BG hide]")
            self.w(ind, '$ fade_fx("black")')
            return
        sid = int(v[1:])
        name = self.imap.get(sid)
        self.w(ind, "# [BG +%d → %s]" % (sid, name))
        if fold:
            self.w(ind, '$ fade_fx("%s", new_music="%s")' % (name, fold))
        else:
            self.w(ind, '$ fade_fx("%s")' % name)

    def event_cg(self, ind, ev, fold=None):
        args = ev["args"]
        m = SPR_ID.search(args)
        if m:
            sid = int(m.group(1))
            name = self.imap.get(sid)
            self.w(ind, "# [EVENT_CG +%d → %s]" % (sid, name))
            if fold:
                self.w(ind, '$ fade_fx("%s", type="cg", new_music="%s")' % (name, fold))
            else:
                self.w(ind, '$ fade_fx("%s", type="cg")' % name)
        else:
            self.w(ind, "# [EVENT_CG hide] — гаснет (без перехода)")

    def bgm_stop(self, ind, ev):
        self.w(ind, "# [BGM stop] — стоп музыки")
        self.w(ind, "stop music fadeout 1.0")

    def dialog(self, ind, ev):
        d = self.dmap[ev["name"]]
        self.w(ind, 'voice "%s"' % d["name"])
        self.w(ind, '%s "%s{#%s}"' % (d["spk"], d["en"], d["name"]))
        self.w(ind, "# JA[%s]: %s" % (d["vid"], " / ".join(d["ja_lines"])))
        self.used_dialogs.add(d["name"])

    def th(self, ind):
        i = len(self.used_th)
        t = self.ths[i]
        tag = "ch7_th_375%s" % ("ab"[i])
        self.w(ind, 'th "%s%s"' % (t["en"], "{#" + tag + "}"))
        self.w(ind, "# JA: %s" % " / ".join(t["ja_lines"]))
        self.used_th.add(tag)

    # ----------------------------------------------------- блок события
    def fold_check(self, evs, i):
        """BG/EVENT_CG + TRANS + BGM play → имя музыки или None."""
        if (i + 2 < len(evs)
                and evs[i + 1]["kind"] == "TRANS"
                and evs[i + 2]["kind"] == "BGM"):
            m = re.match(r"play=(\d+)$", evs[i + 2]["value"] or "")
            if m:
                return BG_K[m.group(1)]
        return None

    def emit_block(self, ind, scene, evs, menu_branch=False):
        """evs — события блока сцены (без SCENE-маркера).
        menu_branch=True — внутри пункта меню (после GOTO комментария
        ветка просто заканчивается; слияние даёт сам fall-through)."""
        n = len(evs)
        skip_next = 0
        for i, ev in enumerate(evs):
            if skip_next:
                skip_next -= 1
                continue
            k = ev["kind"]
            if k == "SCENE":
                continue
            if k in ("MENUINIT", "CHOICE", "MENU"):
                # меню обрабатывается планом (не в блоке)
                continue
            if k == "GOTO":
                self.w(ind, "# [移動] → next(%d)" % ev["target"])
                continue
            if k == "TNDL":
                val = "None" if ev["value"] == "null" else ev["value"]
                self.w(ind, "$ tndl(%s)" % val)
                continue
            if k == "TRANS":
                self.w(ind, "# [TRANS   %s] — переход выполняется fade_fx" % ev["value"])
                continue
            if k == "BG":
                fold = self.fold_check(evs, i)
                self.bg(ind, ev, fold=fold)
                if fold:
                    skip_next = 2
                continue
            if k == "EVENT_CG":
                fold = self.fold_check(evs, i)
                self.event_cg(ind, ev, fold=fold)
                if fold:
                    skip_next = 2
                continue
            if k == "BGM":
                m = re.match(r"play=(\d+)$", ev["value"] or "")
                if m:
                    if (i + 1 < n and evs[i + 1]["kind"] == "BG"
                            and evs[i + 1]["value"] != "hide"):
                        mus = BG_K[m.group(1)]
                        self.w(ind, "# [BGM play=+%s → %s] — музыка раньше фона"
                               % (m.group(1), mus))
                        self.w(ind, "play music %s fadein 1.0" % mus)
                        continue
                    raise CC.Fail("BGM play=+%s не свернут и не стоит перед BG" % m.group(1))
                self.bgm_stop(ind, ev)
                continue
            if k == "SET":
                if ev["layer"].startswith("se"):
                    self.w(ind, '# [SET       set("%s", {%s})] — SE не портируется'
                           % (ev["layer"], ev["args"].replace(u"｜", u"|")))
                    continue
                self.sprite_set(ind, ev)
                continue
            if k == "D":
                self.dialog(ind, ev)
                continue
            if k == "TH":
                self.th(ind)
                continue
            self.do_same(ind, ev)

    def emit_menu(self, ind, chs, block_get, common):
        self.w(ind, "")
        self.w(ind, "# ---- 【選択肢】 ----")
        self.w(ind, "menu:")
        for t in chs:
            c = self.chmap[t]
            self.w(ind + 1, '"%s{#ch7_c%d}":' % (c["en"], t))
            self.w(ind + 2, "# JA: %s" % c["ja"])
            self.used_choices.add("ch7_c%d" % t)
            blk = block_get(t)
            self.emit_block(ind + 2, t, blk, menu_branch=True)
            if common is None:
                self.w(ind + 2, "# Часть 1 заканчивается: сцена 389 → глава 7, часть 2.")
                self.w(ind + 2, "jump ch7_2")
            self.w(ind + 1, "")


def build():
    data = CC.full_check()
    smap, imap = SMap(), ImMap()
    dmap = {d["name"]: d for d in data["dialogs"]}
    chmap = {c["target"]: c for c in data["choices"]}

    voice_rows, events, totals = data["voice_rows"], data["events"], data["totals"]

    # разбить события на блоки-сцены
    blocks = []          # [(scene, [events])]
    cur = None
    for ev in events:
        if ev["kind"] == "SCENE":
            cur = (int(ev["scene"]), [])
            blocks.append(cur)
            continue
        if cur is None:
            raise CC.Fail("событие до первой сцены: %r" % ev["kind"])
        cur[1].append(ev)
    bmap = dict(blocks)
    scenes_seen = [s for s, _ in blocks]
    if scenes_seen != [375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385,
                       386, 387, 388]:
        raise CC.Fail("порядок сцен неожиданный: %r" % scenes_seen)

    # меню из потока
    menus, idx = [], 0
    while idx < len(events):
        if events[idx]["kind"] != "MENUINIT":
            idx += 1
            continue
        chs = []
        j = idx + 1
        while events[j]["kind"] != "MENU":
            if events[j]["kind"] == "CHOICE":
                chs.append(events[j]["target"])
            j += 1
        k = j + 1
        common = None
        while k < len(events):
            if events[k]["kind"] == "GOTO":
                common = events[k]["target"]
                break
            k += 1
        if common is None:
            raise CC.Fail("меню без GOTO-цели")
        menus.append((chs, common))
        idx = k
    if len(menus) != 3:
        raise CC.Fail("меню %d вместо 3: %r" % (len(menus), menus))
    if menus != [([376, 377, 378], 379), ([381, 382, 383], 384),
                 ([386, 387, 388], 389)]:
        raise CC.Fail("карта меню не совпала: %r" % (menus,))

    em = Emitter(smap, imap, dmap, data["ths"], chmap)
    em.used_th = set()

    # ---- шапка метка и титульная карточка
    em.L = []
    head = header_lines(smap.prov)
    em.L = head + em.L
    em.w(0, "")
    em.w(0, "label ch7:")
    em.w(1, "$ tndl(None)")
    em.w(1, "# Титульный монтаж (BG 2/1145/1167/1145/2) → overlay_screen (образ «overlay»).")
    em.w(1, 'call overlay_screen("overlay", "Chapter Seven: \'The Disappointed Princess\'{#ch7_title}", isUseBlur=False, text_mode="black") from _call_overlay_screen_%d' % OVERLAY_K)
    em.w(1, "pause(2)")
    em.w(0, "")

    # ---- сцена 375 (вход в часть)
    em.w(1, "")
    em.w(1, "# ==== SCENE 375 ====")
    evs375 = bmap[375]
    # монтаж: события до endSkip (BG/TRANS/WAIT и прочее — комментарием)
    title_montage = []
    body = []
    ended = False
    hmm = 0
    for ev in evs375:
        if not ended:
            if ev["kind"] == "UNK3":
                ended = True
                title_montage.append(ev)
                continue
            title_montage.append(ev)
        else:
            body.append(ev)
    if not ended:
        raise CC.Fail("до endSkip не дошли")
    for ev in title_montage:
        if ev["kind"] in ("MENUINIT", "CHOICE", "MENU"):
            raise CC.Fail("меню внутри титульного монтажа")
        if ev["kind"] == "TNDL":
            if ev["value"] != "null":
                raise CC.Fail("TNDL %r внутри монтажа" % ev["value"])
            continue   # tndl(None) уже выдан на метке
        if ev["kind"] == "BG":
            sid = int(ev["value"][1:])
            if sid not in MONTAGE_IDS:
                raise CC.Fail("BG %d вне монтажа" % sid)
            em.w(1, "# [BG +%d — титульный монтаж → overlay_screen]" % sid)
        elif ev["kind"] == "TRANS":
            em.w(1, "# [TRANS   %s] — переход выполняется fade_fx" % ev["value"])
        elif ev["kind"] in ("RESET", "TITLE", "SKIP", "UNK3"):
            em.do_same(1, ev)
        else:
            em.do_same(1, ev)
    em.emit_block(1, 375, body)

    # ---- развилка 1
    em.emit_menu(1, [376, 377, 378], lambda t: bmap[t], 379)
    # ---- общая сцена 379
    em.w(1, "")
    em.w(1, "# ==== SCENE 379 (переход после вариантов) ====")
    em.emit_block(1, 379, bmap[379])

    # ---- сцена 380
    em.w(1, "")
    em.w(1, "# ==== SCENE 380 ====")
    em.emit_block(1, 380, bmap[380])

    # ---- развилка 2
    em.emit_menu(1, [381, 382, 383], lambda t: bmap[t], 384)
    em.w(1, "")
    em.w(1, "# ==== SCENE 384 (переход после вариантов) ====")
    em.emit_block(1, 384, bmap[384])

    # ---- сцена 385
    em.w(1, "")
    em.w(1, "# ==== SCENE 385 ====")
    em.emit_block(1, 385, bmap[385])

    # ---- развилка 3 (ветки уходят в часть 2)
    em.emit_menu(1, [386, 387, 388], lambda t: bmap[t], None)
    em.w(1, "")
    em.w(1, "# конец части 1: сцена 389 — в script-ch7_2.rpy (jump внутри веток)")

    # ---- контроль покрытия
    names_all = {d["name"] for d in data["dialogs"]}
    if em.used_dialogs != names_all:
        raise CC.Fail("не все реплики выдали: %r" % sorted(names_all - em.used_dialogs))
    if em.used_th != {"ch7_th_375a", "ch7_th_375b"}:
        raise CC.Fail("мысли не все: %r" % em.used_th)
    want_ch = {"ch7_c%d" % t for t in (376, 377, 378, 381, 382, 383, 386, 387, 388)}
    if em.used_choices != want_ch:
        raise CC.Fail("пункты меню не все: %r" % (want_ch ^ em.used_choices))

    io.open(OUT_PATH, "w", encoding="utf-8", newline="\n").write(
        "\n".join(em.L).rstrip("\n") + "\n")
    print("OK: написано %s, строк %d" % (OUT_PATH, len(em.L)))


def header_lines(prov):
    prov_txt = ", ".join(str(p) for p in prov) if prov else "(нет)"
    h = HEADER.replace("—_title,", "— титульная карточка-overlay K=12,")
    h = h.replace("—-choice)", "— меню 【選択肢】")
    h = h.replace("(нет)", prov_txt)
    out = []
    for ln in h.splitlines():
        out.append(ln)
    return out


if __name__ == "__main__":
    build()
    print("OK script")
