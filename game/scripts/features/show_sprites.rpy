# chara position
transform normal_center:
    zoom 0.55  
    xalign 0.5
    yalign 1.0

transform normal_right:
    zoom 0.55     
    xalign 1.2  
    yalign 1.0    

transform normal_left:
    zoom 0.55 
    xalign -0.2
    yalign 1.0        

transform close_center:
    zoom 0.70  
    xalign 0.5
    yalign 0.15

transform close_left_npc:
    zoom 0.60 
    xalign -0.3
    yalign 1.0        

transform close_right_npc:
    zoom 0.60 
    xalign 1.9
    yalign 0.95    


# slide
transform slide_left_out_generic:
    yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign -0.3 alpha 0

transform slide_right_out_generic:
    yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign 1.3 alpha 0

# === LEFT SLIDES ===
transform slide_left_in:
    xalign -0.3 yalign 1.0 zoom 0.55 alpha 0.1
    ease 0.4 xalign 0.05 alpha 1.0

transform slide_left_out:
    xalign 0.05 yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign -0.3 alpha 0

transform slide_left_to_center_in:
    xalign -0.3 yalign 1.0 zoom 0.55 alpha 0.1
    ease 0.4 xalign 0.5 alpha 1.0    

# === RIGHT SLIDES ===
transform slide_right_in:
    xalign 1.3 yalign 1.0 zoom 0.55 alpha 0.1
    ease 0.4 xalign 0.95 alpha 1.0

transform slide_right_out:
    xalign 0.95 yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign 1.3 alpha 0

transform slide_center_to_right_out:
    xalign 0.5 yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign 1.3 alpha 0  

# === CENTER TO SIDE SLIDES ===
transform slide_center_to_left:
    xalign 0.5 yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign -0.2 alpha 1.0

transform slide_center_to_right:
    xalign 0.5 yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign 1.2 alpha 1.0


# =============================================================================
#  ГЕОМЕТРИЯ, УТИЛИТЫ, ДИНАМИЧЕСКАЯ ДЛИТЕЛЬНОСТЬ
# =============================================================================
init -1 python:
    import math  # [FIX] вынесен в начало, а не внутрь _slide_dur

    CHARA_GEOM = {
        ("normal", "left"):   (0.55, -0.20, 1.00),
        ("normal", "center"): (0.55,  0.50, 1.00),
        ("normal", "right"):  (0.55,  1.20, 1.00),

        ("big",    "left"):   (0.70, -0.30, 1.00),
        ("big",    "center"): (0.70,  0.50, 0.15),
        ("big",    "right"):  (0.70,  1.40, 0.95),
    }

    def _geom(mode, side):
        return CHARA_GEOM.get((mode, side), CHARA_GEOM[("normal", "center")])

    def _off(side, direction):
        if side == "left":
            return -0.60
        if side == "right":
            return 1.70
        return 1.70 if direction == "out" else -0.60

    _ANIM_UNSET = object()

    def _entry_x(slot, slide_dir):
        if slide_dir == "right":
            return -0.60
        if slide_dir == "left":
            return 1.70
        return _off(slot, "in")

    def _exit_x(slot, slide_dir):
        if slide_dir == "left":
            return -0.60
        if slide_dir == "right":
            return 1.70
        return _off(slot, "out")

    def _slide_dur(x0, x1):
        # [FIX] math уже импортирован на уровне init-блока
        if not SLIDE_DYNAMIC:
            return _SLIDE_DUR / max(SLIDE_SPEED, 0.01)
        dist = abs(float(x1) - float(x0))
        ref  = max(_SLIDE_REF_DIST, 0.001)
        dur  = _SLIDE_DUR * math.sqrt(max(dist, 0.0) / ref)
        dur  = dur / max(SLIDE_SPEED, 0.01)
        return max(_SLIDE_DUR_MIN, min(_SLIDE_DUR_MAX, dur))

    # -------------------------------------------------------------------------
    #  [ЗАДАЧА 1] БЫСТРЫЙ "КОРОТКИЙ" СЛАЙД
    #
    #  Вместо того чтобы гнать спрайт через весь экран из-за края (эффект
    #  "карусели"), он появляется совсем рядом со своим финальным местом,
    #  проходит короткую траекторию из alpha 0 в alpha 1 и резко встаёт на
    #  место. Насколько близко к цели он появляется — задаёт SLIDE_SHORT_DIST,
    #  длительность рывка — SLIDE_SHORT_DUR.
    #
    #  Полностью совместимо с mode="big": стартовая точка считается от
    #  РЕАЛЬНОЙ финальной координаты слота (target_xa), которая уже учитывает
    #  режим (normal/big).
    # -------------------------------------------------------------------------
    def _entry_x_short(slot, slide_dir, target_xa):
        # откуда ВЪЕЗЖАЕТ новый спрайт (рядом с целью)
        if slide_dir == "right":
            return target_xa - SLIDE_SHORT_DIST   # въезд слева-направо
        if slide_dir == "left":
            return target_xa + SLIDE_SHORT_DIST   # въезд справа-налево
        # nearest — из ближней стороны
        if slot == "right":
            return target_xa + SLIDE_SHORT_DIST
        return target_xa - SLIDE_SHORT_DIST

    def _exit_x_short(slot, slide_dir, target_xa):
        # куда УЕЗЖАЕТ уходящий спрайт (рядом с местом, откуда стоял)
        if slide_dir == "left":
            return target_xa - SLIDE_SHORT_DIST
        if slide_dir == "right":
            return target_xa + SLIDE_SHORT_DIST
        # nearest — в ближнюю сторону
        if slot == "left":
            return target_xa - SLIDE_SHORT_DIST
        return target_xa + SLIDE_SHORT_DIST

    def _slide_in_geom(slot, slide_dir, target_xa):
        """(start_x, duration) для въезжающего спрайта."""
        if SLIDE_SHORT:
            return _entry_x_short(slot, slide_dir, target_xa), SLIDE_SHORT_DUR
        sx = _entry_x(slot, slide_dir)
        return sx, _slide_dur(sx, target_xa)

    def _slide_out_geom(slot, slide_dir, target_xa):
        """(exit_x, duration) для уезжающего спрайта."""
        if SLIDE_SHORT:
            return _exit_x_short(slot, slide_dir, target_xa), SLIDE_SHORT_DUR
        ex = _exit_x(slot, slide_dir)
        return ex, _slide_dur(target_xa, ex)

    def _zorder(side, center_front):
        if side == "center":
            if center_front is True:
                return 50
            if center_front is False:
                return 5
            return 15
        return 20

    def _tag_of(image_name):
        return image_name.split()[0]

    def _all_hide_tags():
        tags = list(CHARA_TAGS)
        for _s, _rec in store._sprite_slots.items():
            _t = _rec[0]
            if _t not in tags:
                tags.append(_t)
        return tags


# =============================================================================
#  СОСТОЯНИЕ
# =============================================================================
default _sprite_slots = {}
default _sprite_z = 0

# [ЗАДАЧА 4] Выставляется, когда show_sprites(None) снял всех без явной
# анимации. Следующий show_sprites(...) трактует это как полную замену:
# все новые въезжают слева, как будто старые только что уехали вправо.
default _sprite_full_replace_pending = False

define CHARA_TAGS = [
    "l", "s", "k", "t", "c", "h", "si", "ha", "g", "d", "o", "m",
    "npc_left", "npc_right", "mage",
]

define _SLIDE_DUR      = 0.4
define SLIDE_DYNAMIC   = True
define SLIDE_SPEED     = 1.3
define _SLIDE_REF_DIST = 0.5
define _SLIDE_DUR_MIN  = 0.3
define _SLIDE_DUR_MAX  = 0.9

# =============================================================================
#  [ЗАДАЧА 1] НАСТРОЙКИ БЫСТРОГО КОРОТКОГО СЛАЙДА
# =============================================================================
# True  -> новый быстрый режим: спрайт появляется у самого своего места и
#          делает короткий резкий слайд (alpha 0 -> 1). Быстро, без "карусели".
# False -> прежнее поведение: длинный слайд из-за края экрана
#          (по старым правилам _slide_dur / _entry_x / _exit_x).
define SLIDE_SHORT      = True

# Насколько ДАЛЕКО от финальной точки начинается слайд (в единицах xalign).
# Это тот самый "момент, на котором появляется слайд":
#   меньше значение -> спрайт возникает ещё ближе к месту (короче путь);
#   больше значение -> путь длиннее (ближе к старому виду).
define SLIDE_SHORT_DIST = 0.22

# Длительность короткого слайда в секундах (резкий и быстрый рывок).
define SLIDE_SHORT_DUR  = 0.22

# =============================================================================
#  [ЗАДАЧА 2] АНИМАЦИЯ ПОЛНОЙ ЗАМЕНЫ ВСЕХ СПРАЙТОВ
# =============================================================================
# Что делать по умолчанию, когда на экране ВСЕ спрайты заменяются другими
# персонажами (именно персонажи, а не смена эмоции у тех же). Тогда больше не
# нужно каждый раз писать anim_in="slide_right", anim_out="slide_right".
# Срабатывает ТОЛЬКО если вызывающий не указал анимацию явно.
#   "slide_right" -> все уезжают вправо, новые въезжают слева-направо
#   "slide_left"  -> то же, но влево
#   "slide"       -> прежняя логика "в ближайшую сторону"
#   None          -> ничего не навязывать (полностью старое поведение)
#
# [ЗАДАЧА 4] Сюда же относится и полное снятие всех: show_sprites(None) без
# явной анимации по умолчанию уводит ВСЕХ вправо (а не в ближайшую сторону),
# и следующий show_sprites(...) въезжает слева. Так пара
#   $ show_sprites(None)
#   $ show_sprites("l 4 angry")
# читается как полная замена, без ручного anim_in/anim_out в каждом вызове.
define FULL_REPLACE_ANIM = "slide_right"

# =============================================================================
#  [ЗАДАЧА 3] АНИМАЦИЯ СМЕНЫ ЭМОЦИИ
# =============================================================================
# Эффект, когда у того же персонажа в том же режиме меняется только картинка
# (например "k 1" -> "k 1 happy"). Перекрывается аргументом emote=... в вызове.
#   "dissolve" -> плавное растворение (по умолчанию)
#   None       -> без анимации (мгновенно)
define EMOTION_ANIM = "dissolve"


# =============================================================================
#  ПАРАМЕТРИЧЕСКИЕ ТРАНСФОРМЫ
# =============================================================================

transform chara_at(z, xa, ya):
    zoom z
    xalign xa
    yalign ya
    alpha 1.0

transform chara_slide_in(z, xa, ya, sx, dur=0.4):
    zoom z
    yalign ya
    xalign sx
    alpha 0.0
    easein dur xalign xa alpha 1.0

transform chara_slide_out(z, xa, ya, ex, dur=0.4):
    zoom z
    yalign ya
    xalign xa
    alpha 1.0
    easeout dur xalign ex alpha 0.0

transform chara_move(z0, xa0, ya0, z1, xa1, ya1, dur=0.4):
    zoom z0
    xalign xa0
    yalign ya0
    alpha 1.0
    ease dur zoom z1 xalign xa1 yalign ya1


# =============================================================================
#  СКРЫТЬ ВСЕХ
# =============================================================================
init -1 python:

    def _hide_all(anim="dissolve"):
        slots = store._sprite_slots

        if not slots:
            store._sprite_slots = {}
            store._sprite_z = 0
            if anim == "dissolve":
                renpy.with_statement(dissolve)
            return

        if renpy.is_skipping() or renpy.in_rollback():
            for tag in _all_hide_tags():
                renpy.hide(tag)
            store._sprite_slots = {}
            store._sprite_z = 0
            renpy.with_statement(None)
            return

        if anim is None or anim == "dissolve":
            for tag in _all_hide_tags():
                renpy.hide(tag)
            store._sprite_slots = {}
            store._sprite_z = 0
            renpy.with_statement(dissolve if anim == "dissolve" else None)
            return

        if anim == "slide_left":
            dir_of = lambda s: "left"
        elif anim == "slide_right":
            dir_of = lambda s: "right"
        elif anim == "slide":
            dir_of = lambda s: "left" if s == "left" else "right"
        else:
            for tag in _all_hide_tags():
                renpy.hide(tag)
            store._sprite_slots = {}
            store._sprite_z = 0
            renpy.with_statement(None)
            return

        _max_dur = 0.0
        for s, (tag, img, m, z) in slots.items():
            zoom_, xa, ya = _geom(m, s)
            ex, d = _slide_out_geom(s, dir_of(s), xa)   # [ЗАДАЧА 1]
            _max_dur = max(_max_dur, d)
            renpy.show(img, at_list=[chara_slide_out(zoom_, xa, ya, ex, d)],
                       tag=tag, zorder=z)
        renpy.with_statement(None)
        renpy.pause(_max_dur)

        # [FIX] один цикл hide в конце, без лишнего with_statement между ними
        for tag in _all_hide_tags():
            renpy.hide(tag)
        store._sprite_slots = {}
        store._sprite_z = 0
        renpy.with_statement(None)


# =============================================================================
#  ДИНАМИЧЕСКИЙ ПОКАЗ 1-3 ПЕРСОНАЖЕЙ
# =============================================================================
init -1 python:

    def _parse_show_anim(anim, slots_order):
        dir_by_slot = {}

        if isinstance(anim, (tuple, list)):
            for i, a in enumerate(anim):
                if i >= len(slots_order):
                    break
                s = slots_order[i]
                if a == "slide_left":
                    dir_by_slot[s] = "left"
                elif a == "slide_right":
                    dir_by_slot[s] = "right"
                else:
                    dir_by_slot[s] = "nearest"
            for s in slots_order:
                dir_by_slot.setdefault(s, "nearest")
            return "slide", dir_by_slot

        if anim == "slide_left":
            for s in slots_order:
                dir_by_slot[s] = "left"
            return "slide", dir_by_slot
        if anim == "slide_right":
            for s in slots_order:
                dir_by_slot[s] = "right"
            return "slide", dir_by_slot
        if anim == "slide":
            for s in slots_order:
                dir_by_slot[s] = "nearest"
            return "slide", dir_by_slot
        if anim is None:
            return None, dir_by_slot
        return "dissolve", dir_by_slot


    def show_sprites(chars, mode="normal", anim_in=_ANIM_UNSET, anim_out=_ANIM_UNSET,
                     side=None, center_front=None, hide_window=False,
                     raise_z=True, anim=_ANIM_UNSET, emote=_ANIM_UNSET):
        # --- [ЗАДАЧА 2] запоминаем, задал ли ВЫЗЫВАЮЩИЙ анимацию явно ---
        # Нужно, чтобы автоподстановка FULL_REPLACE_ANIM не перезатирала то,
        # что явно прописано в существующих вызовах (обратная совместимость).
        in_explicit  = (anim is not _ANIM_UNSET) or (anim_in is not _ANIM_UNSET)
        out_explicit = (anim is not _ANIM_UNSET) or (anim_out is not _ANIM_UNSET)

        # общий anim= (как раньше) перекрывает anim_in
        if anim is not _ANIM_UNSET:
            anim_in = anim

        # значения по умолчанию (прежнее поведение: базово slide)
        if anim_in is _ANIM_UNSET:
            anim_in = "slide"
        if anim_out is _ANIM_UNSET:
            anim_out = anim_in

        # --- [ЗАДАЧА 3] эффект смены эмоции: аргумент перекрывает константу ---
        if emote is _ANIM_UNSET:
            emote = EMOTION_ANIM

        if chars is None:
            # [ЗАДАЧА 4] Полное снятие всех спрайтов — это тоже "полная замена".
            # Если анимация не задана явно, уводим ВСЕХ вправо (а не каждого в
            # ближайшую сторону) и помечаем, что следующий показ — замена.
            # in_explicit/out_explicit сняты ДО подстановки значений по
            # умолчанию, поэтому отражают именно явные аргументы вызывающего.
            fully_default = (not in_explicit) and (not out_explicit)
            if fully_default and FULL_REPLACE_ANIM is not None:
                anim_out = FULL_REPLACE_ANIM
            _hide_all(anim_out)
            store._sprite_full_replace_pending = fully_default \
                and (FULL_REPLACE_ANIM is not None)
            return

        if isinstance(chars, str):
            chars = [chars]
        chars = list(chars)
        n = len(chars)

        if n == 1:
            slots_order = [side or "center"]
        elif n == 2:
            slots_order = ["left", "right"]
        elif n == 3:
            slots_order = ["left", "center", "right"]
        else:
            raise Exception("show_sprites: поддерживается от 1 до 3 персонажей")

        layout = {slots_order[i]: chars[i] for i in range(n)}

        # --- [ЗАДАЧА 2] определяем ПОЛНУЮ замену всех спрайтов ---
        # Полная замена = на экране кто-то был И ни один старый ПЕРСОНАЖ
        # (сравниваем теги персонажей, а не эмоции) не остаётся среди новых.
        # Смена эмоции ("k 1" -> "k 1 happy") сюда не попадает, т.к. тег "k"
        # остаётся -> множества пересекаются.
        _old_char_tags = set(_tag_of(oimg)
                             for _s, (_t, oimg, _m, _z) in store._sprite_slots.items())
        _new_char_tags = set(_tag_of(img) for img in layout.values())
        _full_replace = bool(_old_char_tags) and bool(_new_char_tags) \
                        and _old_char_tags.isdisjoint(_new_char_tags)

        # [ЗАДАЧА 4] Замена через show_sprites(None): состояние уже очищено,
        # поэтому _full_replace её не видит — берём флаг с прошлого вызова.
        _pending = getattr(store, "_sprite_full_replace_pending", False)
        store._sprite_full_replace_pending = False

        if (_full_replace or _pending) and FULL_REPLACE_ANIM is not None:
            if not in_explicit:
                anim_in = FULL_REPLACE_ANIM
            if not out_explicit:
                anim_out = FULL_REPLACE_ANIM

        anim_family_in, dir_in = _parse_show_anim(anim_in, slots_order)
        anim_family_out, dir_out = _parse_show_anim(anim_out, ["left", "center", "right"])

        _apply_layout(layout, mode, anim_family_in, anim_family_out,
                      center_front, hide_window, raise_z, dir_in, dir_out, emote)


    def _apply_layout(layout, mode, anim_in, anim_out, center_front,
                      hide_window=False, raise_z=True, dir_in=None, dir_out=None,
                      emote_anim="dissolve"):
        slots = store._sprite_slots
        if dir_in is None:
            dir_in = {}
        if dir_out is None:
            dir_out = {}

        _instant = renpy.is_skipping() or renpy.in_rollback()

        slide_in   = (anim_in == "slide")
        noanim_in  = (anim_in is None)
        slide_out  = (anim_out == "slide")
        noanim_out = (anim_out is None)

        if hide_window:
            _window_hide(None)
        else:
            _window_show(None)

        base_tags = {s: _tag_of(img) for s, img in layout.items()}
        tag_counts = {}
        for _bt in base_tags.values():
            tag_counts[_bt] = tag_counts.get(_bt, 0) + 1

        new = {}
        for s, img in layout.items():
            bt = base_tags[s]
            tag = bt if tag_counts[bt] == 1 else (bt + "__" + s)
            new[s] = (tag, img)

        old_by_tag = {tag: (s, oimg, om, oz)
                      for s, (tag, oimg, om, oz) in slots.items()}
        new_by_tag = {tag: (s, nimg) for s, (tag, nimg) in new.items()}

        # ---- МГНОВЕННЫЙ РЕЖИМ (скип / откат) ----
        if _instant:
            new_tags = set(new_by_tag.keys())
            for tag, (os_, oimg, om, oz) in old_by_tag.items():
                if tag not in new_tags:
                    renpy.hide(tag)

            def _order_key_fast(item):
                s = item[0]
                if s != "center":
                    return 1
                if center_front is True:
                    return 2
                if center_front is False:
                    return 0
                return 1

            old_z_by_slot_fast = {s: oz for s, (tag, oimg, om, oz) in slots.items()}
            slot_z = {}
            for s, (tag, nimg) in sorted(new.items(), key=_order_key_fast):
                if not raise_z and s in old_z_by_slot_fast:
                    slot_z[s] = old_z_by_slot_fast[s]
                else:
                    store._sprite_z += 1
                    slot_z[s] = store._sprite_z
                z, xa, ya = _geom(mode, s)
                renpy.show(nimg, at_list=[chara_at(z, xa, ya)],
                           tag=tag, zorder=slot_z[s])
            renpy.with_statement(None)

            new_state = {}
            for s, (tag, nimg) in new.items():
                new_state[s] = (tag, nimg, mode, slot_z[s])
            store._sprite_slots = new_state
            return

        new_tags_set = set(t for (t, _img) in new.values())

        old_groups = {}
        for _s, (_otag, _oimg, _om, _oz) in slots.items():
            _b = _tag_of(_oimg)
            old_groups.setdefault(_b, []).append((_s, _otag, _oimg, _om, _oz))

        new_groups = {}
        for _s, (_ntag, _nimg) in new.items():
            _b = _tag_of(_nimg)
            new_groups.setdefault(_b, []).append((_s, _ntag, _nimg))

        leavers  = []
        movers   = []
        resizes  = []
        emotions = []
        entrants = []

        for _b in (set(old_groups) | set(new_groups)):
            olds = old_groups.get(_b, [])
            news = new_groups.get(_b, [])
            used_old = set()
            used_new = set()

            for ni, (ns_, ntag, nimg) in enumerate(news):
                for oi, (os_, otag, oimg, om, oz) in enumerate(olds):
                    if oi in used_old:
                        continue
                    if os_ == ns_:
                        used_old.add(oi)
                        used_new.add(ni)
                        if om != mode:
                            resizes.append((ns_, otag, ntag, nimg, om))
                        elif oimg != nimg:
                            emotions.append((ns_, otag, ntag, nimg))
                        break

            rem_old = [olds[i] for i in range(len(olds)) if i not in used_old]
            rem_new = [news[i] for i in range(len(news)) if i not in used_new]

            k = min(len(rem_old), len(rem_new))
            for i in range(k):
                os_, otag, oimg, om, oz = rem_old[i]
                ns_, ntag, nimg = rem_new[i]
                movers.append((os_, ns_, otag, ntag, nimg, om))

            for i in range(k, len(rem_old)):
                os_, otag, oimg, om, oz = rem_old[i]
                leavers.append((os_, otag, oimg, om))
            for i in range(k, len(rem_new)):
                ns_, ntag, nimg = rem_new[i]
                entrants.append((ns_, ntag, nimg))

        # ---- ZORDER ----
        shown_slots = [m[1] for m in movers] + [r[0] for r in resizes] \
                      + [e[0] for e in emotions] + [e[0] for e in entrants]

        def _order_key(s):
            if s != "center":
                return 1
            if center_front is True:
                return 2
            if center_front is False:
                return 0
            return 1

        old_z_by_slot = {s: oz for s, (tag, oimg, om, oz) in slots.items()}

        slot_z = {}
        for s in sorted(shown_slots, key=_order_key):
            if not raise_z and s in old_z_by_slot:
                slot_z[s] = old_z_by_slot[s]
            else:
                store._sprite_z += 1
                slot_z[s] = store._sprite_z

        # ---- 1) УХОДЯЩИЕ ----
        if leavers:
            if slide_out:
                _max_dur = 0.0
                for s, tag, oimg, om in leavers:
                    z, xa, ya = _geom(om, s)
                    ex, d = _slide_out_geom(s, dir_out.get(s), xa)   # [ЗАДАЧА 1]
                    _max_dur = max(_max_dur, d)
                    renpy.show(oimg, at_list=[chara_slide_out(z, xa, ya, ex, d)],
                               tag=tag, zorder=old_z_by_slot.get(s, 20))
                renpy.with_statement(None)
                renpy.pause(_max_dur)
                # [FIX] hide после pause — без лишнего with_statement между ними
                for s, tag, oimg, om in leavers:
                    renpy.hide(tag)
            else:
                for s, tag, oimg, om in leavers:
                    renpy.hide(tag)
                renpy.with_statement(None if noanim_out else dissolve)

        # ---- 2) ПЕРЕЕЗЖАЮЩИЕ ----
        if movers:
            for os_, ns_, otag, ntag, nimg, om in movers:
                z1, xa1, ya1 = _geom(mode, ns_)
                if noanim_in:
                    renpy.show(nimg, at_list=[chara_at(z1, xa1, ya1)],
                               tag=ntag, zorder=slot_z[ns_])
                else:
                    z0, xa0, ya0 = _geom(om, os_)
                    d = _slide_dur(xa0, xa1)
                    renpy.show(nimg, at_list=[chara_move(z0, xa0, ya0, z1, xa1, ya1, d)],
                               tag=ntag, zorder=slot_z[ns_])
                if otag != ntag and otag not in new_tags_set:
                    renpy.hide(otag)
            renpy.with_statement(None)

        # ---- 3a) СМЕНА РАЗМЕРА ----
        if resizes:
            for s, otag, ntag, nimg, om in resizes:
                z1, xa1, ya1 = _geom(mode, s)
                if noanim_in:
                    renpy.show(nimg, at_list=[chara_at(z1, xa1, ya1)],
                               tag=ntag, zorder=slot_z[s])
                else:
                    z0, xa0, ya0 = _geom(om, s)
                    d = _SLIDE_DUR / max(SLIDE_SPEED, 0.01)
                    renpy.show(nimg, at_list=[chara_move(z0, xa0, ya0, z1, xa1, ya1, d)],
                               tag=ntag, zorder=slot_z[s])
                if otag != ntag and otag not in new_tags_set:
                    renpy.hide(otag)
            renpy.with_statement(None)

        # ---- 3b) СМЕНА ЭМОЦИИ ----  [ЗАДАЧА 3]
        if emotions:
            for s, otag, ntag, nimg in emotions:
                z, xa, ya = _geom(mode, s)
                renpy.show(nimg, at_list=[chara_at(z, xa, ya)],
                           tag=ntag, zorder=slot_z[s])
                if otag != ntag and otag not in new_tags_set:
                    renpy.hide(otag)
            # Эффект смены эмоции задаётся аргументом emote / константой
            # EMOTION_ANIM. Если весь показ идёт без анимации (anim=None),
            # эмоция тоже мгновенная — сохраняем прежнее поведение.
            if noanim_in:
                _emote_trans = None
            elif emote_anim == "dissolve":
                _emote_trans = dissolve
            else:
                _emote_trans = None
            renpy.with_statement(_emote_trans)

        # задержка перед появлением новых
        # [ЗАДАЧА 1] в быстром режиме зазор меньше, чтобы замена ощущалась резкой
        if (leavers or movers) and entrants and not noanim_in:
            renpy.pause(0.05 if SLIDE_SHORT else 0.2)

        # ---- 4) НОВЫЕ ПЕРСОНАЖИ ----
        if entrants:
            if slide_in:
                _max_dur = 0.0
                for s, tag, nimg in entrants:
                    z, xa, ya = _geom(mode, s)
                    sx, d = _slide_in_geom(s, dir_in.get(s), xa)   # [ЗАДАЧА 1]
                    _max_dur = max(_max_dur, d)
                    renpy.show(nimg, at_list=[chara_slide_in(z, xa, ya, sx, d)],
                               tag=tag, zorder=slot_z[s])
                renpy.with_statement(None)
                renpy.pause(_max_dur)
                # [FIX] УБРАН второй цикл renpy.show(chara_at) после pause.
                # Трансформ chara_slide_in уже заканчивается в точке покоя
                # (xalign xa, alpha 1.0). Повторный show вызывал микро-фриз
                # из-за пересоздания дисплея на лету.
            else:
                for s, tag, nimg in entrants:
                    z, xa, ya = _geom(mode, s)
                    renpy.show(nimg, at_list=[chara_at(z, xa, ya)],
                               tag=tag, zorder=slot_z[s])
                renpy.with_statement(None if noanim_in else dissolve)

        # ---- ПЕРЕСТРОИТЬ СОСТОЯНИЕ ----
        new_state = {}
        for s, (tag, nimg) in new.items():
            z = slot_z.get(s, old_z_by_slot.get(s, 0))
            new_state[s] = (tag, nimg, mode, z)
        store._sprite_slots = new_state
