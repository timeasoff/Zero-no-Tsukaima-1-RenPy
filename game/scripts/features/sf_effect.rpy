# ==== IMAGES ====
image black = "#000"
image white = "#fff"

image border = "gui/border.png"

transform border_left:
    zoom 0.85
    xalign 0.05
    yalign 0.5

    
transform border_right:
    zoom 0.85
    xzoom -1
    xalign 0.95
    yalign 0.5


# =============================================================================
#  ПОЗИЦИЯ ФОНА
# =============================================================================
transform bg_center:
    zoom 0.85
    xalign 0.5
    yalign 0.5

transform bg_default:
    zoom 1
    xalign 0.5
    yalign 0.5

transform bg_vignette:
    zoom 0.65
    xalign 0.5
    yalign 0.5

transform color_cover:
    zoom 2.0
    xalign 0.5
    yalign 0.5

transform fullscreen:
    xysize (config.screen_width, config.screen_height)

transform cover:
    xalign 0.5
    yalign 0.5
    fit "cover"

# =============================================================================
#  БАЗОВЫЕ ПЕРЕХОДЫ (используются в обычных scene ... with fade / with flash)
# =============================================================================

define flash = Fade(0.1, 0.5, 0.5, color="#fff")
define fade  = Fade(0.5, 0.0, 0.5)

# Имя последнего показанного через эффекты фона. Нужно, чтобы новый фон
# с ДРУГИМ тегом ("bg ..." -> "cg ...") надёжно заменял предыдущий, а не
# оставался лежать под ним. (см. фикс бага 2)
default _fx_bg_name = None

# =============================================================================
#  ГЕНЕРАТОР СЛУЧАЙНОЙ ТРЯСКИ (для blow)
#  Каждый кадр вычисляет новое случайное смещение — резкая, неравномерная
#  тряска (взрыв), а не плавное качание.
# =============================================================================
init python:
    import random as _fx_random

    def _make_blow_shaker(strength, duration):
        s = int(strength)
        dur = float(duration)
        def _shaker(trans, st, at):
            if st >= dur:
                trans.xoffset = 0
                trans.yoffset = 0
                return None
            # резкое случайное смещение на каждом кадре
            trans.xoffset = _fx_random.randint(-s, s)
            trans.yoffset = _fx_random.randint(-s, s)
            return 0   # перерисовать на следующем кадре
        return _shaker

# =============================================================================
#  ТРАНСФОРМЫ ТРЯСКИ (единственный источник истины)
#    hit_shake  — плавная, быстрая тряска (затухающие колебания)
#    blow_shake — резкие случайные рывки (взрыв)
# =============================================================================
transform hit_shake(duration=0.35, strength=25, *, old_widget=None, new_widget=None):
    delay duration
    new_widget
    events False
    linear (duration * 0.15) xoffset strength
    linear (duration * 0.20) xoffset -(strength * 0.7)
    linear (duration * 0.20) xoffset (strength * 0.45)
    linear (duration * 0.20) xoffset -(strength * 0.25)
    linear (duration * 0.25) xoffset 0
    events True

transform blow_shake(duration=0.7, strength=30, *, old_widget=None, new_widget=None):
    delay duration
    new_widget
    events False
    function _make_blow_shaker(strength, duration)
    xoffset 0
    yoffset 0
    events True

# =============================================================================
#  ЭФФЕКТЫ СЦЕНЫ
#
#  Публичные функции (первый аргумент — фон, без ключа):
#      fade_fx(bg=None, ...)   — обычное затухание в чёрный и проявление
#      flash_fx(bg=None, ...)  — мягкая матовая вспышка (полностью перекрывает)
#      hit_fx(bg=None, ...)    — плавная быстрая тряска
#      blow_fx(bg=None, ...)   — резкая случайная тряска (взрыв)
#
#  Комбинирование через scene_fx (порядок задаётся кортежем/строкой):
#      $ scene_fx(("flash", "blow"), "town_square_night")   # сначала вспышка, потом тряска
#      $ scene_fx("hit fade", "bg forest")                  # то же строкой

#      $ scene_fx(("hit", "fade"), "town_square_night", duration=(0.3, 2)) - удар с затемнением , у каждого своя длительность анимации
#
#  Общие параметры: duration, sprites, mode, side, center_front, sound,
#  hide, window_hide, new_music, music_fadein, stop_music, music_fadeout,
#  strength.
#
#  window_hide — скрывает диалоговое окно вместе с эффектом.
#      По умолчанию True для fade/flash, False для hit/blow/dissolve.
#      Обратно окно возвращать не нужно — следующая реплика покажет его сама.
# =============================================================================
init -1 python:

    _FX_COVERING = ("fade", "flash")            # прячут персонажей по умолчанию
    _FX_SCENE    = ("fade", "flash", "dissolve") # меняют сцену -> commit до эффекта
    _FX_KNOWN    = ("fade", "flash", "hit", "blow", "dissolve")
    _FX_DEFAULT_DUR = {"fade": 1.0, "flash": 1.0, "hit": 0.35, "blow": 0.7, "dissolve": 0.5}

    def _show_vignette():
        renpy.show(
            "border",
            at_list=[border_left],
            tag="_fx_border_left",
            layer="master",
            zorder=1000
        )

        renpy.show(
            "border",
            at_list=[border_right],
            tag="_fx_border_right",
            layer="master",
            zorder=1000
        )
    def _hide_vignette():
        renpy.hide("_fx_border_left", layer="master")
        renpy.hide("_fx_border_right", layer="master")

    # --- ФИКС БАГА 2 ---
    # Единый тег для ВСЕХ фонов/CG, которые показываются через эффекты.
    # Ren'Py заменяет изображение только в пределах одного тега. Раньше
    # "bg forest" имел тег "bg", а "cg ha_forest" — тег "cg", поэтому новый
    # CG показывался ПОВЕРХ (или под) старого фона, и визуально фон «не менялся».
    # Показывая любой фон под одним и тем же тегом, мы гарантируем, что новый
    # фон (bg ИЛИ cg) всегда полностью заменяет предыдущий.
    _FX_BG_TAG = "bg"

    def _parse_effects(effect):
        """Строку/кортеж эффектов -> упорядоченный список известных эффектов."""
        if not effect:
            return []
        if isinstance(effect, (tuple, list)):
            out = []
            for e in effect:
                out += _parse_effects(e)
            return out
        return [e for e in str(effect).lower().split() if e in _FX_KNOWN]

    def _dur_for(duration, index, default):
        """Длительность конкретного эффекта. duration может быть числом или
        кортежем/списком (своя длительность на каждый эффект)."""
        if isinstance(duration, (tuple, list)):
            if index < len(duration) and duration[index] is not None:
                return float(duration[index])
            return default
        if duration is None:
            return default
        return float(duration)

    def _fx_transition(effect, duration, strength):
        """Возвращает переход для одного эффекта (duration уже вычислен)."""
        if effect == "fade":
            # обычное затухание в чёрный (полностью перекрывает экран)
            return Fade(duration * 0.45, duration * 0.10, duration * 0.45, color="#000000")
        if effect == "flash":
            # мягкая матовая вспышка в белый (полностью перекрывает экран)
            return Fade(duration * 0.30, duration * 0.10, duration * 0.60, color="#ffffff")
        if effect == "dissolve":
            return Dissolve(duration)
        if effect == "hit":
            return hit_shake(duration=duration, strength=(25 if strength is None else strength))
        if effect == "blow":
            return blow_shake(duration=duration, strength=(30 if strength is None else strength))
        return None

    # -------------------------------------------------------------------------
    #  ФИКС БАГА 1: показ персонажей ВНУТРИ эффекта БЕЗ собственного
    #  renpy.with_statement.
    #
    #  Раньше _commit() звал show_sprites(..., anim=None). Но show_sprites
    #  внутри себя выполняет renpy.with_statement(None) — это НЕМЕДЛЕННО
    #  «фиксирует» текущее состояние экрана (гасит mage) ещё ДО того, как
    #  запустится переход flash/fade. Поэтому mage пропадал ДО вспышки.
    #
    #  Здесь мы только СТАВИМ картинки в очередь (renpy.show/renpy.hide) и
    #  обновляем состояние слотов, НО не вызываем with_statement. Тогда все
    #  изменения (гашение mage + показ новых) попадают в один переход
    #  flash/fade, который вызывается уже в scene_fx после _commit().
    # -------------------------------------------------------------------------
    def _stage_sprites_instant(chars, mode="normal", side=None, center_front=None):
        # [ЗАДАЧА 4] fade/dissolve сами управляют сценой — снимаем "ожидание
        # полной замены", выставленное предыдущим show_sprites(None).
        store._sprite_full_replace_pending = False
        if chars is None:
            return

        if isinstance(chars, str):
            chars = [chars]
        chars = list(chars)
        n = len(chars)

        if n == 1:
            layout = {(side or "center"): chars[0]}
        elif n == 2:
            layout = {"left": chars[0], "right": chars[1]}
        elif n == 3:
            layout = {"left": chars[0], "center": chars[1], "right": chars[2]}
        else:
            raise Exception("scene_fx: поддерживается от 1 до 3 персонажей")

        # уникализация тегов при коллизии (как в show_sprites)
        base_tags = {s: _tag_of(img) for s, img in layout.items()}
        tag_counts = {}
        for _bt in base_tags.values():
            tag_counts[_bt] = tag_counts.get(_bt, 0) + 1

        # порядок наложения центрального относительно боковых
        def _order_key(s):
            if s != "center":
                return 1
            if center_front is True:
                return 2
            if center_front is False:
                return 0
            return 1

        new_state = {}
        for s in sorted(layout.keys(), key=_order_key):
            img = layout[s]
            bt = base_tags[s]
            tag = bt if tag_counts[bt] == 1 else (bt + "__" + s)
            store._sprite_z += 1
            z, xa, ya = _geom(mode, s)
            renpy.show(img, at_list=[chara_at(z, xa, ya)],
                       tag=tag, zorder=store._sprite_z)
            new_state[s] = (tag, img, mode, store._sprite_z)
        store._sprite_slots = new_state

    def scene_fx(effect="fade", new_bg=None, duration=None, hide=None, window_hide=None, sprites=None, mode="normal", side=None, center_front=None, sound=None, hud=None, stop_music=False, music_fadeout=1.0, new_music=None, music_fadein=1.0, strength=None, bg_position="fullscreen", type="bg"):
        effects = _parse_effects(effect)
        has_cover = any(e in _FX_COVERING for e in effects)

        renpy.show(
            "black",
            at_list=[color_cover],
            tag="_fx_black",
            layer="master",
            zorder=-100
        )
        if type == "cg":
            bg_position = "vignette"

        # По умолчанию перекрывающие эффекты (fade/flash) убирают персонажей,
        # тряска (hit/blow) — оставляет.
        if hide is None:
            hide = has_cover

        # window hide (скрытие диалогового окна).
        # По умолчанию: для fade/flash — True, для остальных (hit/blow/dissolve) — False.
        # Окно не возвращаем обратно вручную: следующая реплика (window auto)
        # покажет его сама.
        if window_hide is None:
            window_hide = has_cover
        if window_hide:
            store._window = False

        # 1) Звук
        if sound is not None:
            renpy.sound.play(getattr(store.audio, sound, sound))

        # 2) Остановка музыки
        if stop_music or new_music is not None:
            renpy.music.stop(fadeout=music_fadeout)

        # 3) HUD / quick menu
        if hud is None:
            hud = hide
        if hud:
            store.quick_menu = False
            if hasattr(store, "sympathy_hud_visible"):
                store._fade_hud_was = store.sympathy_hud_visible
                store.sympathy_hud_visible = False

        # 4) Смена сцены (фон/персонажи) — применяется один раз.
        _state = {"done": False}
        def _commit():
            if _state["done"]:
                return
            _state["done"] = True
            # [ЗАДАЧА 4] смена сцены эффектом прерывает "ожидание замены"
            store._sprite_full_replace_pending = False
            if hide:
                for tag in _all_hide_tags():
                    renpy.hide(tag)
                store._sprite_slots = {}
                store._sprite_z = 0
            if new_bg is not None:
                _hide_vignette()

                # --- ФИКС БАГА 2 ---
                # На случай, если предыдущий фон был показан кем-то ещё под
                # СВОИМ естественным тегом ("cg ..." -> "cg"), отличным от
                # нашего единого _FX_BG_TAG, — гасим его явно.
                _prev = getattr(store, "_fx_bg_name", None)
                if _prev:
                    _ptag = _prev.split()[0]
                    if _ptag != _FX_BG_TAG:
                        renpy.hide(_ptag, layer="master")
                # Показываем ЛЮБОЙ фон (bg или cg) под одним фиксированным тегом,
                # поэтому новый фон всегда полностью заменяет предыдущий.
                if new_bg == "black" or new_bg == "white":
                    position = color_cover
                elif bg_position == "center":
                    position = bg_center
                elif bg_position == "default":
                    position = bg_default
                elif bg_position == "vignette":
                    _show_vignette()
                    position = bg_vignette
                elif bg_position == "fullscreen":
                    position = fullscreen
                elif bg_position == "cover":
                    position = cover

                renpy.hide(_FX_BG_TAG, layer="master")

                renpy.show(
                    new_bg,
                    at_list=[position],
                    tag=_FX_BG_TAG,
                    layer="master"
                )

                #renpy.show(new_bg, at_list=[position], tag=_FX_BG_TAG, layer="master")
                store._fx_bg_name = new_bg
            if sprites is not None:
                if hide:
                    # Состояние уже очищено выше -> ставим новых персонажей
                    # в очередь БЕЗ собственного with_statement, чтобы их
                    # появление/исчезновение старых попало в переход эффекта.
                    _stage_sprites_instant(sprites, mode, side, center_front)
                else:
                    # Персонажи остаются на экране (тряска и т.п.) — обычный путь.
                    show_sprites(sprites, mode=mode, anim=None, side=side, center_front=center_front)

        # Сцену меняем прямо перед первым «сценовым» эффектом (fade/flash/
        # dissolve), чтобы смена была скрыта переходом. Иначе — перед первым.
        commit_at = 0
        for i, e in enumerate(effects):
            if e in _FX_SCENE:
                commit_at = i
                break

        # 5) Применение эффектов по порядку (у каждого своя длительность)
        if not effects:
            _commit()
            renpy.with_statement(None)
        else:
            for i, e in enumerate(effects):
                if i == commit_at:
                    _commit()
                dur = _dur_for(duration, i, _FX_DEFAULT_DUR.get(e, 0.7))
                renpy.with_statement(_fx_transition(e, dur, strength))
        _commit()

        # 6) Новый трек
        if new_music is not None:
            renpy.music.play(getattr(store.audio, new_music, new_music), fadein=music_fadein)

    # -------------------------------------------------------------------------
    #  ПУБЛИЧНЫЕ ФУНКЦИИ (первый аргумент — фон, без ключа)
    # -------------------------------------------------------------------------
    def _run_fx(effect, bg, duration, kwargs):
        # поддержка и позиционного bg, и старого new_bg=...
        if bg is None:
            bg = kwargs.pop("new_bg", None)
        else:
            kwargs.pop("new_bg", None)
        scene_fx(effect, new_bg=bg, duration=duration, **kwargs)

    def fade_fx(bg=None, duration=1.0, window_hide=True, **kwargs):
        """Обычное затухание в чёрный и проявление нового фона/персонажей."""
        _run_fx("fade", bg, duration, kwargs)

    def flash_fx(bg=None, duration=2.0, window_hide=True, **kwargs):
        """Мягкая матовая вспышка, полностью перекрывающая изображение."""
        _run_fx("flash", bg, duration, kwargs)

    def hit_fx(bg=None, duration=0.35, **kwargs):
        """Плавная быстрая тряска (удар)."""
        kwargs.setdefault("sound", "punch")
        _run_fx("hit", bg, duration, kwargs)

    def blow_fx(bg=None, duration=0.7, **kwargs):
        """Резкая случайная тряска (взрыв)."""
        kwargs.setdefault("sound", "blow")
        _run_fx("blow", bg, duration, kwargs)

    def shake_fx(bg=None, duration=0.7, **kwargs):
        """Маленькая тряска """
        kwargs.setdefault("sound", None)
        kwargs.setdefault("strength", 5)
        _run_fx("blow", bg, duration, kwargs)

    def dissolve_fx(bg=None, duration=0.5, **kwargs):
        """Смена с прозрачностью"""
        _run_fx("dissolve", bg, duration, kwargs)
