# ============================================================================
#  portrait_choises.rpy
# ----------------------------------------------------------------------------
#  Два экрана выбора (screen), заменяющие обычный menu:
#
#    1) portrait_choice(...)  - ряд ПОРТРЕТОВ (как экран выбора девушки).
#       При наведении на портрет внизу меняется текст-подпись (caption).
#
#    2) sprite_choice(...)    - список ВАРИАНТОВ слева, а сбоку СПРАЙТ персонажа.
#       При наведении на вариант справа меняется спрайт того, к кому идём.
#       Вариант МОЖЕТ быть без спрайта (напр. "Hallway") - тогда при наведении
#       сбоку просто ничего не показывается.
#
#  Оба варианта:
#    - при показе проигрывают музыку (по умолчанию "t3", можно переопределить
#      аргументом music=..., music=None -> музыку не трогаем);
#    - используют СВОЙ захардкоженный фон (можно переопределить background=...);
#    - фон показывается ТОЙ ЖЕ трансформой, что и в диалогах
#      (bg_center/bg_default/bg_vignette из sf_effect.rpy), чтобы разрешение
#      и перспектива фона НЕ "скакали" при входе в меню выбора;
#    - при выборе жёстко уходим в ЧЁРНЫЙ кадр (спрайты убираются мгновенно),
#      затем CALL на target. Новую сцену проявляем уже внутри label через
#      fade_fx(...), который плавно выведет фон/спрайты из чёрного.
#    - target вызывается через renpy.call(), поэтому label выбора должен
#      заканчиваться на return: после него управление вернётся к statement'у,
#      идущему СРАЗУ ПОСЛЕ "$ sprite_choice(...)" / "$ portrait_choice(...)".
#
#  Словарь персонажей char_data лежит в отдельном файле char_data.rpy.
# ----------------------------------------------------------------------------
#  ПРИМЕРЫ ВЫЗОВА
# ----------------------------------------------------------------------------
#
#  # --- Кейс 2: выбор куда пойти (спрайт справа), музыка t3, фон коридора ---
#  #     У "Hallway" НЕТ ключа "char" -> при наведении справа спрайт не рисуется.
#  label ch1_3_choice:
#      $ sprite_choice([
#          {"char": "siesta", "text": "Siesta's Room", "target": "si_room_ch1_3"},
#          {"char": "louise", "text": "Louise's Room", "target": "l_room_ch1_3"},
#          {                  "text": "Hallway",       "target": "hallway_ch1_3"},
#      ])
#      # СЮДА ВЕРНЁМСЯ, когда выбранный label сделает return:
#      jump ch1_4
#      return
#
#  label hallway_ch1_3:
#      # мы пришли сюда с ЧЁРНОГО экрана без спрайтов -> проявляем сцену:
#      $ fade_fx("hallway_night", new_music="t6", sprites=("s 1"))
#      ...
#      return   # <- обязательно: вернёт управление к "jump ch1_4" выше
#
#  # --- Кейс 1: выбор с кем провести время (портреты + подпись снизу) ---
#  label date_choice:
#      $ portrait_choice([
#          {"char": "louise",   "text": "Провести время с Луизой.",     "target": "date_louise"},
#          {"char": "siesta",   "text": "Провести время с Сиестой.",    "target": "date_siesta"},
#          {"char": "tabitha",  "text": "Провести время с Табитой.",    "target": "date_tabitha"},
#          {"char": "kirche",   "text": "Провести время с Кирхе.",      "target": "date_kirche"},
#          {"char": "henrietta","text": "Провести время с Генриеттой.", "target": "date_henrietta"},
#      ])
#
#  # переопределение музыки/фона/позиции фона:
#  $ sprite_choice(choices, music="t7", background="images/bg/my_bg.webp")
#  $ portrait_choice(choices, music=None)                # music=None -> не менять музыку
#  $ sprite_choice(choices, bg_position="default")       # фон как bg_default (zoom 1)
#
#  Каждый пункт (choice) - это dict:
#     "char"   - ключ в словаре char_data (портрет/спрайт берём оттуда).
#                НЕОБЯЗАТЕЛЕН для sprite_choice: без него сбоку ничего не будет.
#     "text"   - текст пункта. В sprite_choice это надпись кнопки слева,
#                в portrait_choice это подпись снизу при наведении.
#     "target" - label, на который делаем jump при выборе этого пункта.
# ============================================================================

# ----------------------------------------------------------------------------
#  ФОНЫ ПО УМОЛЧАНИЮ (захардкожены, но переопределяются аргументом background=)
# ----------------------------------------------------------------------------
define PORTRAIT_CHOICE_BG = "images/bg/choice_portrait.webp"   # экран выбора девушки
define SPRITE_CHOICE_BG   = "images/bg/hallway_night.webp"     # экран "куда пойти"

# Позиция/масштаб фона - имя трансформы из sf_effect.rpy:
# "center" -> bg_center (zoom 0.85) | "default" -> bg_default (zoom 1) | "vignette" -> bg_vignette (zoom 0.65).
# Так фон на экране выбора выглядит ИДЕНТИЧНО фону в предыдущей сцене и не "скачет".
define PORTRAIT_CHOICE_BG_POS = "vignette"
define SPRITE_CHOICE_BG_POS   = "fullscreen"

# Музыка по умолчанию для обоих экранов
define CHOICE_DEFAULT_MUSIC = "t3"

# Чёрный кадр, в который уходим после выбора (как $ fade_fx("black", ...)).
define CHOICE_BLACK_IMAGE = "black"

# ----------------------------------------------------------------------------
#  НАСТРОЙКИ ВНЕШНЕГО ВИДА (константы - меняй под свою игру)
# ----------------------------------------------------------------------------
# Картинки-подложки кнопок как в обычном menu (стандартный Ren'Py GUI).
# Если у тебя свои плашки для выбора - поставь сюда их пути.
define CHOICE_BTN_IDLE_IMG  = "gui/button/choice_idle_background.png"
define CHOICE_BTN_HOVER_IMG = "gui/button/choice_hover_background.png"

# --- ПОРТРЕТЫ (portrait_choice) ---
# Размер карточки портрета. Портрет вписывается в этот бокс (fit "cover"),
# поэтому НЕ растягивается на весь экран и не вылезает за подпись снизу.
define PORTRAIT_W = 210
define PORTRAIT_H = 520
# Насколько увеличивается портрет при наведении (маленькое значение, чтобы
# он не вылезал за пределы своей ячейки).
define PORTRAIT_HOVER_ZOOM = 1.04
# Скорость анимации наведения (чем больше - тем медленнее/плавнее).
define PORTRAIT_ANIM_TIME = 0.25
# Затемнение НЕ выбранных портретов (0.0 - без затемнения, отрицательное - темнее).
# Было -0.18 (слишком темно) -> делаем светлее.
define PORTRAIT_DIM = -0.06
# Вертикальное положение ряда портретов (0.0 - верх экрана, 1.0 - низ).
# Меньше значение -> портреты выше и НЕ наезжают на нижний бар с подписью.
define PORTRAIT_ROW_YALIGN = 0.30

# --- СПРАЙТ СБОКУ (sprite_choice) ---
# Спрайт показывается ровно так же, как в игре (zoom как у обычных персонажей),
# чтобы не был огромным. Значения совпадают с normal_right из show_sprites.rpy.
define SPRITE_CHOICE_ZOOM   = 0.55
define SPRITE_CHOICE_XALIGN = 1.0
define SPRITE_CHOICE_YALIGN = 1.0
# Длительность плавной смены спрайта при наведении
define SPRITE_CHOICE_FADE = 0.20

# ----------------------------------------------------------------------------
#  ХЕЛПЕРЫ (python)
# ----------------------------------------------------------------------------
init python:

    def _choice_resolve_audio(name):
        # Позволяет передавать как имя из namespace audio (define audio.t3 = ...),
        # так и прямой путь к файлу. None -> музыку не трогаем.
        if name is None:
            return None
        return getattr(store.audio, name, name)

    def _choice_play_music(music):
        track = _choice_resolve_audio(music)
        if track is not None:
            renpy.music.play(track, channel="music", fadeout=1.0, fadein=1.0)

    def _choice_bg_transform(pos):
        # Возвращает ту же трансформу фона, что используется в диалогах
        # (sf_effect.rpy). Благодаря этому фон на экране выбора выглядит
        # идентично фону в предыдущей сцене и не "скачет" по разрешению.
        return {
            "center":   bg_center,
            "default":  bg_default,
            "vignette": bg_vignette,
            "fullscreen": fullscreen,
        }.get(pos, bg_center)

    def _choice_sprite_of(ch):
        # Спрайт варианта (или None, если у пункта нет "char" или у персонажа
        # не задан "sprite"). Именно это даёт "вариант без спрайта".
        key = ch.get("char")
        if not key:
            return None
        return char_data.get(key, {}).get("sprite_choise")

    def _choice_cut_to_black():
        # Жёстко (без плавного затухания) убираем ВСЁ с экрана и показываем
        # чёрный кадр. Фон/спрайты выбора исчезают мгновенно, чтобы на ветке
        # выбора мы стартовали именно с чёрного, а fade_fx() уже плавно
        # проявил новую сцену "из чёрного".
        renpy.scene()                     # очищает master-слой (фон + спрайты)
        renpy.show(CHOICE_BLACK_IMAGE)    # мгновенный чёрный кадр
        # Гасим автоматическое управление окном (config.window == "auto"),
        # иначе на стыке statement'ов Ren'Py рисует ПУСТОЕ окно диалога прямо
        # на чёрном фоне (то самое "окно то появляется, то пропадает").
        # False -> окно останется скрытым, пока не начнётся реальная реплика.
        store._window = False
        # ВАЖНО: restart_interaction() НЕ отрисовывает кадр, поэтому последним
        # "показанным" кадром оставался экран выбора со старым спрайтом, и
        # следующий fade_fx() дизолвил именно из него (старый спрайт "всплывал").
        # with_statement(None) мгновенно фиксирует чёрный кадр как показанный,
        # так что fade_fx() на ветке выбора проявляет сцену уже из чёрного.
        renpy.with_statement(None)

    def portrait_choice(choices, music=CHOICE_DEFAULT_MUSIC,
                         background=PORTRAIT_CHOICE_BG, bg_position=PORTRAIT_CHOICE_BG_POS):
        """
        Экран выбора с портретами. При наведении на портрет снизу меняется подпись.
        При выборе -> уходим в чёрный (спрайты убираются) и CALL на target.
        """

        _choice_play_music(music)
        target = renpy.call_screen(
            "portrait_choice_screen",
            choices=choices,
            background=background,
            bg_position=bg_position,
        )
        _choice_cut_to_black()
        # call (а НЕ jump): выбранный label заканчивается на return и должен
        # вернуть управление сюда -> выполнение продолжится со statement'а,
        # следующего за "$ portrait_choice(...)" (например "jump ch1_4").
        renpy.call(target)

    def sprite_choice(choices, music=CHOICE_DEFAULT_MUSIC,
                      background=SPRITE_CHOICE_BG, bg_position=SPRITE_CHOICE_BG_POS):
        """
        Экран выбора со списком вариантов слева и спрайтом персонажа справа.
        При наведении на вариант справа меняется спрайт (или пропадает, если
        у пункта нет спрайта). При выборе -> уходим в чёрный и CALL на target.
        """
        _choice_play_music(music)
        default_sprite = _choice_sprite_of(choices[0]) if choices else None
        target = renpy.call_screen(
            "sprite_choice_screen",
            choices=choices,
            background=background,
            bg_position=bg_position,
            default_sprite=default_sprite,
        )
        _choice_cut_to_black()
        # call (а НЕ jump): выбранный label заканчивается на return и вернёт нас
        # сюда -> продолжим со statement'а после "$ sprite_choice(...)".
        renpy.call(target)


# ----------------------------------------------------------------------------
#  ТРАНСФОРМЫ / АНИМАЦИИ
# ----------------------------------------------------------------------------

# Лёгкое приближение портрета при наведении (медленнее, чем было, и без
# выхода за пределы карточки - zoom очень маленький, масштаб от центра).
transform _pc_portrait_focus:
    anchor (0.5, 0.5) pos (0.5, 0.5)
    on idle:
        linear PORTRAIT_ANIM_TIME zoom 1.0 matrixcolor BrightnessMatrix(PORTRAIT_DIM)
    on hover:
        linear PORTRAIT_ANIM_TIME zoom PORTRAIT_HOVER_ZOOM matrixcolor BrightnessMatrix(0.0)

# Плавная смена спрайта справа. Позиция/зум спрайта = как у обычных персонажей.
transform _pc_sprite_swap(zoom_=SPRITE_CHOICE_ZOOM, xa=SPRITE_CHOICE_XALIGN, ya=SPRITE_CHOICE_YALIGN):
    zoom zoom_
    xalign xa
    yalign ya
    on show:
        alpha 0.0
        linear SPRITE_CHOICE_FADE alpha 1.0
    on replace:
        alpha 0.0
        linear SPRITE_CHOICE_FADE alpha 1.0


# ============================================================================
#  ЭКРАН 1: ВЫБОР ПО ПОРТРЕТАМ (подпись снизу меняется при наведении)
# ============================================================================
screen portrait_choice_screen(choices, background, bg_position="center"):
    modal True
    zorder 100

    # начальная подпись - текст первого пункта, чтобы бар снизу не был пустым
    default caption = (choices[0]["text"] if choices else "")

    # Фон показываем ТОЙ ЖЕ трансформой, что и в диалогах (bg_center и т.п.) -
    # разрешение/перспектива совпадают с предыдущей сценой, без "скачка".
    add background at _choice_bg_transform(bg_position)

    if bg_position == "vignette":
        add "border" at border_left
        add "border" at border_right

    # Ряд портретов - карточками фиксированного размера (не на весь экран).
    # Чуть выше центра (PORTRAIT_ROW_YALIGN), чтобы не наезжали на нижний бар.
    hbox:
        xalign 0.5
        yalign PORTRAIT_ROW_YALIGN
        spacing 14

        for ch in choices:
            $ data = char_data.get(ch["char"], {})
            button:
                xysize (PORTRAIT_W, PORTRAIT_H)
                background None
                action Return(ch["target"])
                hovered SetScreenVariable("caption", ch["text"])
                # на unhover оставляем последнюю подпись (не сбрасываем)

                at _pc_portrait_focus

                # Портрет вписан в карточку - не растягивается на весь экран
                add data.get("portrait_choise", "gui/system/portraits/choises/placeholder.webp"):
                    fit "cover"
                    xysize (PORTRAIT_W, PORTRAIT_H)

    # Нижний бар с подписью - подложка как у кнопки обычного menu (картинка)
    frame:
        align (0.5, 0.9)
        xsize 1100
        padding (40, 26)
        background Frame(CHOICE_BTN_IDLE_IMG, 30, 12)

        text caption:
            align (0.5, 0.5)
            size 40
            color "#f4e9d2"
            outlines [(2, "#00000088", 0, 0)]
            text_align 0.5


# ============================================================================
#  ЭКРАН 2: ВЫБОР СПИСКОМ + СПРАЙТ СБОКУ (меняется при наведении)
# ============================================================================
screen sprite_choice_screen(choices, background, default_sprite, bg_position="center"):
    modal True
    zorder 100

    # текущий показываемый спрайт (обновляется при наведении на пункт).
    # Может быть None -> сбоку ничего не показываем (вариант "без спрайта").
    default current_sprite = default_sprite

    # Фон показываем ТОЙ ЖЕ трансформой, что и в диалогах - без "скачка".
    add background at _choice_bg_transform(bg_position)

    # Спрайт персонажа справа (в том же масштабе, что и обычные персонажи).
    # Показываем ТОЛЬКО если у наведённого варианта есть спрайт.
    if current_sprite:
        add current_sprite at _pc_sprite_swap

    # Список вариантов слева - кнопки-плашки как в обычном menu (style choice_button)
    vbox:
        align (0.06, 0.5)
        spacing 10

        for ch in choices:
            textbutton ch["text"]:
                style "choice_button"
                xsize 800
                action Return(ch["target"])
                hovered SetScreenVariable("current_sprite", _choice_sprite_of(ch))
