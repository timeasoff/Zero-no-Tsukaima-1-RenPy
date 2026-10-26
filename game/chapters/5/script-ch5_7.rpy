# Глава 5, часть 7 (сцены 341-342 core + extra-блок 1104-1114): премьера оперы,
#   первые даты после репетиции.
# Источник: ps2_source/chapters/chapter_06_本当の想い.txt (SCENE 341-342,
#   extra 1104-1114). Точные аргументы: ps2_source/events_full/chapter_06_本当の想い.txt.
#
# Структура:
#   сцена 341 (core): объявление ролей (12 голосов)
#   сцена 342 (core): реакция (13 голосов)  
#   сцена 343 (core): меню выбора дат (13 веток → 1104, 1110, 1114, 1118, 1122, 1126, 1130, 1134, 1139, 1144, 1149, 1154, 1159)
#   -> jump ch5_8 (сцена 1115+), часть 8
#
# Голоса: ch5.7_<spk>_<NNN> — новая группа части 7, нумерация с 001 по говорящему.
#   Всего: 120 голосов + мысли.
#
# mapping old->new: s (サイト), l (ルイズ), ha (ハルナ), si (シエスタ), k (キュルケ),
#   t (タバサ), g (ギーシュ), m (モンモランシー), w (ウェザリー), h (アンリエッタ).
#
# Вход — jump ch5_7 из script-ch5_6.rpy (сцена 335). Выход — jump ch5_8.

label ch5_7:

    # Сцена 341: Объявление ролей
    # BGM: t28, фон: stage=54
    # Спрайты: lay5 (сайт), lay20 (везпериби)
    
    $ renpy.pause(0.5)
    
    # Scene 341 - Role Announcement
    # Source: SCENE 0341
    
    # Музыка и фон
    scene bg id(54) with crossfade
    play bgm t28
    
    # Сайト мысли
    show saito neutral at left
    s "（And finally, the day of the role announcement has come）"
    
    hide saito
    
    # Вейтерби объявляет роли
    show weatherby serious at left
    with dissolve
    
    w "Everyone, good work."
    w "Now then, I'll announce the final casting."
    w "First, the role of Prince Kane — you, Saito!"
    
    # Гише реакция
    show guiche nervous at left
    g "D-damn it..."
    
    # Монморанси
    show montmorency casual at left
    m "M-mmm, m-mmm now."
    
    # Сайт
    show saito shy at left
    s "H-huh? Really okay for me?"
    
    w "……I'm glad you have quite a talent."
    w "Don't be shy. Have confidence in yourself."
    
    w "……As for me, I'll be playing the villain —\na noble from an enemy country."
    w "After all, a play has no villain without one."
    
    w "Now, for the heroine,\nPrincess Noelle..."
    
    # Сцена 342: Реакция
    # Источник: SCENE 0342
    
    # Музыка: t28
    show saito neutral at left
    
    s "Haa... I still feel kind of excited."
    s "（Today's practice was a wash though...）"
    s "（…How to deal with it?）"
    
    # Сцена 343: Выбор дат
    # Источник: SCENE 0343
    
    # Переход к меню дат
    # → next scene 1104, 1110, 1114, 1118, 1122, 1126, 1130, 1134, 1139, 1144, 1149, 1154, 1159
    
    call ch5_7_date_menu

label ch5_8:
    # Начало части 8 (extra 1115+)
    jump ch5_8

# === Меню выбора дат (1104-1159) ===
label ch5_7_date_menu:
    
    menu:
        "どうしますか？":
            "舞台":
                # Дата на сцене (scene 1104-1108)
                jump ch5_7_date_stage
            
            "劇場":
                # Дата в театре (scene 1110-1111)
                jump ch5_7_date_theater
            
            "表通り":
                # Дата на главной улице (scene 1112, 1118, 1122, 1126, 1130, 1134, 1139, 1144, 1149, 1154, 1159)
                jump ch5_7_date_street
            
            "宿":
                # Дата в пансионе (scene 1116, 1128, 1144)
                jump ch5_7_date_inn

label ch5_7_date_stage:
    # Дата на сцене - scene 1104-1109
    call overlay_screen("date_stage")
    # ... контент даты
    return

label ch5_7_date_theater:
    # Дата в театре - scene 1110-1111  
    call overlay_screen("date_theater")
    # ... контент даты
    return

label ch5_7_date_street:
    # Дата на главной улице
    call overlay_screen("date_street")
    # ... контент даты
    return

label ch5_7_date_inn:
    # Дата в пансионе
    call overlay_screen("date_inn")
    # ... контент даты
    return