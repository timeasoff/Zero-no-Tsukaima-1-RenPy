## sympathy.rpy - Система симпатии (Tsun/Dere)

# ============================================
# ШРИФТ ДЛЯ СИСТЕМЫ СИМПАТИИ
# ============================================
define sympathy_font = "fonts/KuroHanaMincho.ttf"

# Изображения для UI симпатии
image gui_sympathy_bar = "gui/system/sympathy/bar.webp"
image gui_sympathy_arrow = "gui/system/sympathy/arrow.webp"
image gui_sympathy_up = "gui/system/sympathy/up.webp"
image gui_sympathy_down = "gui/system/sympathy/down.webp"
image gui_sympathy_hud_icon = "gui/system/sympathy/hud_icon.webp"

# Иконки персонажей для отображения при изменении симпатии
image louise_icon = "gui/system/sympathy/louise_icon.webp"
image haruna_icon = "gui/system/sympathy/haruna_icon.webp"
image henrietta_icon = "gui/system/sympathy/henrietta_icon.webp"
image siesta_icon = "gui/system/sympathy/siesta_icon.webp"
image tabitha_icon = "gui/system/sympathy/tabitha_icon.webp"
image kirche_icon = "gui/system/sympathy/kirche_icon.webp"

# ============================================
# ПЕРЕМЕННЫЕ СИМПАТИИ (НЕ persistent - для корректного rollback)
# Диапазон: -100 (tsun) до +100 (dere), начало = 0 (нейтральный)
# ============================================
default louise_sympathy = 0
default haruna_sympathy = 0
default henrietta_sympathy = 0
default siesta_sympathy = 0
default tabitha_sympathy = 0
default kirche_sympathy = 0

# Маршрут главы 5 (route 1-6): вычисляется compute_zero_route() по макс. симпатии
default zero_route = 1

# Отслеживание "известных" персонажей (показываются в меню только после первого взаимодействия)
default known_characters = set()

# Видимость HUD иконки симпатии
default sympathy_hud_visible = False

# Словарь данных персонажей для системы симпатии
init python:
    sympathy_characters = {
        "louise": {
            "name": "Louise",
            "icon": "gui/system/sympathy/louise_icon.webp",
            "var": "louise_sympathy",
            "color": "#e9acb3",
            "has_tsun_dere": True  # Только у Louise есть tsun/dere
        },
        "haruna": {
            "name": "Haruna",
            "icon": "gui/system/sympathy/haruna_icon.webp",
            "var": "haruna_sympathy",
            "color": "#4b4d51",
            "has_tsun_dere": False
        },
        "henrietta": {
            "name": "Henrietta",
            "icon": "gui/system/sympathy/henrietta_icon.webp",
            "var": "henrietta_sympathy",
            "color": "#782163",
            "has_tsun_dere": False
        },
        "siesta": {
            "name": "Siesta",
            "icon": "gui/system/sympathy/siesta_icon.webp",
            "var": "siesta_sympathy",
            "color": "#535a6a",
            "has_tsun_dere": False
        },
        "tabitha": {
            "name": "Tabitha",
            "icon": "gui/system/sympathy/tabitha_icon.webp",
            "var": "tabitha_sympathy",
            "color": "#b4dfec",
            "has_tsun_dere": False
        },
        "kirche": {
            "name": "Kirche",
            "icon": "gui/system/sympathy/kirche_icon.webp",
            "var": "kirche_sympathy",
            "color": "#e36566",
            "has_tsun_dere": False
        }
    }

# ============================================
# ТРАНСФОРМАЦИИ ДЛЯ АНИМАЦИЙ
# ============================================

# Анимация блока уведомления (правый верхний угол)
transform sympathy_notification_anim:
    xpos 1.0
    ypos 0.0
    anchor (1.0, 0.0)
    xoffset -30
    yoffset 30
    alpha 0.0
    easein 0.3 alpha 1.0
    pause 2.0
    easeout 0.4 alpha 0.0

# Анимация полоски симпатии (только для Louise, по центру сверху)
transform sympathy_bar_anim:
    xpos 0.5
    ypos 0.0
    anchor (0.5, 0.0)
    yoffset 15
    alpha 0.0
    zoom 0.8
    linear 0.3 alpha 1.0
    pause 2.0
    linear 0.4 alpha 0.0

# Анимация стрелки/указателя на полоске
# Прогресс-бар идёт от -100 до +100, где 0 = середина
transform sympathy_arrow_anim(start_val, end_val, bar_width_px):
    xpos 0.5
    ypos 0.0
    zoom 0.8
    anchor (0.5, 0.0)
    yoffset 85
    # Позиция: при 0 стрелка по центру, при -100 слева, при +100 справа
    xoffset int(float(start_val) / 100.0 * (bar_width_px / 2.0))
    alpha 0.0
    linear 0.3 alpha 1.0
    # Плавное движение к новой позиции
    linear 1.0 xoffset int(float(end_val) / 100.0 * (bar_width_px / 2.0))
    pause 1.0
    linear 0.4 alpha 0.0

# Анимация второго блока для Louise (tsun/dere + up)
transform sympathy_louise_second_anim:
    xpos 1.0
    ypos 0.0
    anchor (1.0, 0.0)
    xoffset -30
    yoffset 30
    alpha 0.0
    easein 0.3 alpha 1.0
    pause 2.0
    easeout 0.4 alpha 0.0

# ============================================
# HUD ИКОНКА ДЛЯ ОТКРЫТИЯ МЕНЮ СИМПАТИИ (отдельный экран)
# ============================================

transform icon_hover:
    zoom 1.0
    on hover:
        ease 0.1 zoom 1.1
    on idle:
        ease 0.1 zoom 1.0

screen sympathy_hud_icon():
    zorder 100
    
    if sympathy_hud_visible:
        imagebutton:
            xpos 0.1
            ypos 0.1
            anchor (1.0, 0.5)
            xoffset -20
            idle "gui_sympathy_hud_icon"
            hover "gui_sympathy_hud_icon"
            at icon_hover
            action ShowMenu("sympathy_status")

# ============================================
# ЭКРАН УВЕДОМЛЕНИЯ О ИЗМЕНЕНИИ СИМПАТИИ (КЕЙС 1 - ДЛЯ ВСЕХ ПЕРСОНАЖЕЙ)
# ============================================

screen sympathy_notification(char_key, change_value):
    zorder 150
    modal False
    
    $ char_data = sympathy_characters.get(char_key, {"name": "???", "icon": None, "color": "#ffffff"})
    $ char_icon = char_data.get("icon", None)
    
    # Блок в правом верхнем углу: [Уровень симпатии] [Иконка персонажа] [UP/DOWN]
    frame at sympathy_notification_anim:
        xpos 1.0
        ypos 0.0
        anchor (1.0, 0.0)
        xoffset -30
        yoffset 30
        background None
        padding (0, 0)
        
        hbox:
            spacing 15
            yalign 0.5
            
            # 1. Текст "Уровень симпатии" (кастомный шрифт)
            text "Sympathy level":
                font sympathy_font
                size 32
                color "#ffffff"
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            
            # 2. Иконка персонажа (умеренный размер)
            if char_icon and renpy.loadable(char_icon):
                add char_icon:
                    zoom 0.5
                    yalign 0.5
            
            # 3. Иконка UP или DOWN (маленький размер)
            if change_value > 0:
                add "gui_sympathy_up":
                    zoom 0.35
                    yalign 0.5
            elif change_value < 0:
                add "gui_sympathy_down":
                    zoom 0.35
                    yalign 0.5

# ============================================
# ЭКРАН УВЕДОМЛЕНИЯ ДЛЯ LOUISE - ВТОРОЙ БЛОК (TSUN/DERE + ПРОГРЕСС-БАР)
# ============================================

screen sympathy_louise_second(change_value, old_value, new_value):
    zorder 150
    modal False
    
    # Определяем текст: dere если повышаем симпатию, tsun если понижаем
    $ display_text = "Dere" if change_value > 0 else "Tsun"
    $ text_color = "#ff69b4" if change_value > 0 else "#ff6b6b"
    
    # Прогресс бар по центру сверху (300 пикселей ширина)
    add "gui_sympathy_bar" at sympathy_bar_anim
    add "gui_sympathy_arrow" at sympathy_arrow_anim(old_value, new_value, 300)
    
    # Блок в правом верхнем углу: [tsun/dere] [UP]
    frame at sympathy_louise_second_anim:
        xpos 1.0
        ypos 0.0
        anchor (1.0, 0.0)
        xoffset -30
        yoffset 30
        background None
        padding (0, 0)
        
        hbox:
            spacing 15
            yalign 0.5
            
            # 1. Текст tsun/dere (кастомный шрифт)
            text display_text:
                font sympathy_font
                size 32
                color text_color
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            
            # 2. Иконка UP (всегда, маленький размер)
            add "gui_sympathy_up":
                zoom 0.35
                yalign 0.5

# ============================================
# ЭКРАН ПРОСМОТРА СИМПАТИИ (меню)
# ============================================

screen sympathy_status():
    tag menu
    modal True
    zorder 200
    
    # Затемнённый фон
    add Solid("#00000099")
    
    $ _frame_bg = Frame("gui/frame_wood.webp", 20, 20, 20, 20) if renpy.loadable("gui/frame_wood.webp") else Solid("#e8d5b8")
    
    # Основной контейнер
    frame:
        xpos 0.5
        ypos 0.5
        anchor (0.5, 0.5)
        xsize 800
        ysize 600
        background _frame_bg
        padding (30, 30)
        
        vbox:
            xfill True
            spacing 20
            
            # Заголовок
            text "Sympathy level":
                xalign 0.5
                font sympathy_font
                size 40
                color "#5c3d2e"
                outlines [(2, "#d4a574", 0, 0)]
            
            null height 20
            
            # Список ТОЛЬКО известных персонажей
            for char_key in sympathy_characters:
                if char_key in known_characters:
                    $ char_data = sympathy_characters[char_key]
                    $ var_name = char_data["var"]
                    $ current_val = getattr(renpy.store, var_name, 0)
                    $ char_name = char_data["name"]
                    $ char_color = char_data["color"]
                    $ char_icon = char_data["icon"]
                    $ has_tsun_dere = char_data.get("has_tsun_dere", False)
                    # Для бара: преобразуем -100..+100 в 0..200 для отображения
                    $ bar_value = current_val + 100
                    
                    frame:
                        xfill True
                        ysize 80
                        background Solid("#f5ead8")
                        padding (15, 10)
                        
                        hbox:
                            spacing 20
                            yalign 0.5
                            
                            # Иконка персонажа
                            if char_icon and renpy.loadable(char_icon):
                                add char_icon:
                                    zoom 0.4
                                    yalign 0.5
                            else:
                                null width 60
                            
                            # Имя персонажа
                            text char_name:
                                font sympathy_font
                                size 28
                                color "#5c3d2e"
                                yalign 0.5
                                min_width 120
                            
                            # Полоска симпатии (от -100 до +100, центр = 0)
                            vbox:
                                yalign 0.5
                                spacing 5
                                xsize 350
                                
                                # Бар (0..200 диапазон, где 100 = нейтраль)
                                bar:
                                    value bar_value
                                    range 200
                                    xsize 350
                                    ysize 20
                                    left_bar Solid(char_color)
                                    right_bar Solid("#3a3a3a")
                                
                                # Подписи Tsun / Dere - ТОЛЬКО для Louise
                                if has_tsun_dere:
                                    hbox:
                                        xfill True
                                        text "Tsun":
                                            font sympathy_font
                                            size 16
                                            color "#8b4513"
                                        text "Dere":
                                            font sympathy_font
                                            size 16
                                            color "#ff69b4"
                                            xalign 1.0
                            
                            # Числовое значение
                            text "[current_val]":
                                font sympathy_font
                                size 28
                                color char_color
                                yalign 0.5
            
            # Если нет известных персонажей
            if not known_characters:
                text "No characters unlocked yet":
                    xalign 0.5
                    font sympathy_font
                    size 24
                    color "#888888"
            
            null height 20
            
            # Кнопка закрыть
            textbutton "Close":
                xalign 0.5
                action Return()
                text_font sympathy_font
                text_size 28
                text_color "#5c3d2e"
                text_hover_color "#8b5a2b"

# ============================================
# ФУНКЦИИ PYTHON
# ============================================

init python:
    def show_sympathy_hud():
        """Show HUD icon of Sympathy menu"""
        renpy.store.sympathy_hud_visible = True
        renpy.show_screen("sympathy_hud_icon")
    
    def hide_sympathy_hud():
        """Hide HUD icon of Sympathy menu"""
        renpy.store.sympathy_hud_visible = False
        renpy.hide_screen("sympathy_hud_icon")
    
    def toggle_sympathy_hud():
        """Toggle HUD icon visibility"""
        if renpy.store.sympathy_hud_visible:
            hide_sympathy_hud()
        else:
            show_sympathy_hud()

    def update_sympathy(value, char_key="louise", min_val=-100, max_val=100,
                        up_sound="audio/sfx/sympathy_up.wav", 
                        down_sound="audio/sfx/sympathy_down.wav"):
        """
        Update character sympathy with animation
        
        Диапазон: -100 (tsun) до +100 (dere), начало = 0 (нейтральный)
        
        Логика:
        - Для всех персонажей: показываем блок [Уровень симпатии] [Иконка] [UP/DOWN]
        - Для Louise: дополнительно показываем прогресс-бар + блок [tsun/dere] [UP]
        """
        
        # Получаем данные персонажа
        char_data = sympathy_characters.get(char_key, None)
        if char_data is None:
            var_name = char_key + "_sympathy"
        else:
            var_name = char_data["var"]
        
        # Получаем текущее значение (из store, не persistent - для rollback)
        old_value = getattr(renpy.store, var_name, 0)
        
        # Вычисляем новое значение с ограничением
        new_value = old_value + value
        new_value = max(min_val, min(max_val, new_value))
        
        # Сохраняем новое значение в store (поддерживает rollback)
        setattr(renpy.store, var_name, new_value)
        
        # Добавляем персонажа в "известные"
        renpy.store.known_characters.add(char_key)
        
        # Проигрываем звук
        #if value > 0 and renpy.loadable(up_sound):
            #renpy.sound.play(up_sound, channel="sound")
        #elif value < 0 and renpy.loadable(down_sound):
            #renpy.sound.play(down_sound, channel="sound")
        
        # ============================================
        # КЕЙС 1: Все персонажи (включая Louise)
        # Показываем блок: [Уровень симпатии] [Иконка персонажа] [UP/DOWN]
        # ============================================
        #renpy.show_screen("sympathy_notification", 
                         # char_key=char_key,
                          #change_value=value)
        
        # Ждём завершения анимации первого блока
        #renpy.pause(2.8, hard=False)
        
        # Скрываем первый экран
        #renpy.hide_screen("sympathy_notification")
        
        # ============================================
        # КЕЙС 2: Только для Louise - дополнительный блок с прогресс-баром
        # После задержки показываем прогресс-бар + [tsun/dere] [UP]
        # ============================================
       # if char_key == "louise":
            # Небольшая задержка перед вторым блоком
            #renpy.pause(0.3, hard=False)
            
            # Показываем второй экран для Louise (прогресс-бар + tsun/dere)
           # renpy.show_screen("sympathy_louise_second", 
                            #  change_value=value,
                            ##  new_value=new_value)
            
            # Ждём завершения анимации
           # renpy.pause(2.8, hard=False)
            
            # Скрываем экран
           # renpy.hide_screen("sympathy_louise_second")
        
        return new_value
    
    def get_sympathy(char_key="louise"):
        """Получить текущее значение симпатии персонажа"""
        char_data = sympathy_characters.get(char_key, None)
        if char_data:
            var_name = char_data["var"]
        else:
            var_name = char_key + "_sympathy"
        
        return getattr(renpy.store, var_name, 0)
    
    def set_sympathy(char_key, value, min_val=-100, max_val=100):
        """Установить значение симпатии напрямую (без анимации)"""
        char_data = sympathy_characters.get(char_key, None)
        if char_data:
            var_name = char_data["var"]
        else:
            var_name = char_key + "_sympathy"
        
        value = max(min_val, min(max_val, value))
        setattr(renpy.store, var_name, value)
        
        # Добавляем в известные
        renpy.store.known_characters.add(char_key)
        
        return value
    
    def is_character_known(char_key):
        """Проверить, известен ли персонаж"""
        return char_key in renpy.store.known_characters

    def compute_zero_route():
        """Маршрут (route) главы 5 — аналог PS2 checkRoute() (SCENE_0003.txt).

        JA-канон (ps2_source/scripts/SCENE_0003.txt, function checkRoute):
        маршрут = девушка с МАКСИМАЛЬНОЙ симпатией; при равенстве побеждает
        более ранняя проверка в порядке PS2. Числовой route:
            1 = Луиза, 2 = Кюрке, 3 = Табаса, 4 = Сиеста,
            5 = Анриетта, 6 = Харуна.
        PS2 дополнительно принудительно ставит route=1 (Луиза) при
        zero_tundele_count >= 4; счётчик тундэре-теста в ремастере не ведётся,
        поэтому эта оговорка опущена (зафиксировано в reports/log.md).

        Порядок проверок полностью повторяет checkRoute() из SCENE_0003:
        Haruna (6), Siesta (4), Henrietta (5), Tabitha (3), Kirche (2).
        Louise (1) — fallback, если ни одна из этих проверок не сработала.
        Поэтому при равенстве всех шести значений, включая стартовые нули,
        выбирается route 6: isMax(5) истинно.
        """
        order = [("haruna", 6), ("siesta", 4), ("henrietta", 5),
                 ("tabitha", 3), ("kirche", 2), ("louise", 1)]
        vals = [(name, route, get_sympathy(name)) for name, route in order]
        best = max(v for _, _, v in vals)
        for _, route, v in vals[:-1]:
            if v == best:
                return route
        return 1

# ============================================
# ПРИМЕР ИСПОЛЬЗОВАНИЯ
# ============================================
# 
# В скрипте игры:
#
# # Показать HUD иконку меню симпатии
# $ show_sympathy_hud()
#
# # Скрыть HUD иконку
# $ hide_sympathy_hud()
#
# # Переключить видимость
# $ toggle_sympathy_hud()
#
# # Повысить симпатию Луизы на 10 (покажет оба блока + прогресс-бар)
# $ update_sympathy(10, "louise")
#
# # Понизить симпатию Луизы на 5 (покажет оба блока + прогресс-бар)
# $ update_sympathy(-5, "louise")
#
# # Повысить симпатию Haruna на 15 (покажет только первый блок, без прогресс-бара)
# $ update_sympathy(15, "haruna")
#
# # Получить текущую симпатию (диапазон -100 до +100)
# $ current = get_sympathy("louise")
#
# # Проверить, известен ли персонаж
# if is_character_known("haruna"):
#     "Haruna уже известна!"
#
# # Показать экран просмотра симпатии (видны только известные персонажи)
# call screen sympathy_status
# ============================================
