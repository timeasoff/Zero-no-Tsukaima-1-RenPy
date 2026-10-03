define s = Character(_("Saito"), color="#3874a3")
define l = Character(_("Louise"), color="#fd7589")
define k = Character(_("Kirche"), color="#e36566")
define t = Character(_("Tabitha"), color="#b4dfec")
define c = Character(_("Colbert"), color="#5e5b51")
define h = Character(_("Henrietta"), color="#782163")
define si = Character(_("Siesta"), color="#535a6a")
define ha = Character(_("Haruna"), color="#4b4d51")
define g = Character(_("Guiche"), color="#f3e69d")
define d = Character(_("Derflinger"), color="#9d996b")
define o = Character(_("Osmond"), color="#ddd7d4")
define m = Character(_("Montmorency"), color="#e2d79d")

define villager = Character(_("Villager"), color="#797979")

define commander = Character(_("Сommander"), color="#797979")
define soldier = Character(_("Soldier"), color="#797979")
define mage = Character(_("Mage"), color="#d82b2b")
define unds = Character(_("Underlings"), color="#d82b2b")

# --- Дополнительные NPC: зарегистрированы заранее (таблица §4.2 скилла
#     voice-workflow). Имена/коды PROVISIONAL — запись в reports/log.md;
#     при появлении первых реплик сверить с dictionary.md и указать персонажа
#     в отчёте части отдельным разделом (регистрация не отменяет отчётности).
define w         = Character(_("Weatherby"), color="#797979")
define ak        = Character(_("Akina"), color="#797979")
define merchant  = Character(_("Merchant"), color="#797979")
define informant = Character(_("Informant"), color="#797979")
define cat       = Character(_("Cat"), color="#797979")
define customer  = Character(_("Customer"), color="#797979")
define man_a     = Character(_("Man A"), color="#797979")
define man_b     = Character(_("Man B"), color="#797979")
define man_c     = Character(_("Man C"), color="#797979")
define innkeeper = Character(_("Innkeeper"), color="#797979")
define shopkeeper = Character(_("Shopkeeper"), color="#797979")


define unk = Character(_("???"), color="#000000") #protagonist
define unk_ha = Character(_("???"), color="#4b4d51") # haruna
define unk_k = Character(_("???"), color="#e36566") #kirche


define th = Character(None, 
    what_italic=True,
    what_color="#3874a3",
    #what_outlines=[(1, "#00000080", 0, 0)],
    window_style='thought_window'
)

# ----------------------------------------------------------------------------
#  ОБЩИЙ СЛОВАРЬ СУЩНОСТЕЙ ПЕРСОНАЖЕЙ
#  Здесь хранятся портреты (для экрана с портретами) и спрайты (для экрана
#  со спрайтом сбоку). Один общий реестр на всю игру - добавляй персонажей сюда.
#
#    "name"     - отображаемое имя (можно использовать в подписях/подсказках)
#    "portrait" - путь к портрету (карточка лица) для portrait_choice
#    "sprite"   - спрайт для sprite_choice. Это может быть либо тег
#                 существующего image ("si 1", "l 1" ...), либо путь к файлу
#                 ("images/sprites/siesta.webp"). Оба варианта работают в add.
# ----------------------------------------------------------------------------
define char_data = {
    "saito":       {
        "name": "Saito",  
        "color": "#3874a3",
        'description': "A Japanese boy who was summoned to this world by Louise.\nHe is treated as a familiar by Louise.", 

        "portrait_choise": "gui/system/portraits/choises/s_full.webp",  
        "sprite_choise": "s 1",

        # battle: {
        #     "is_mage": False, "is_enemy": False,
        #     "skills": ["slash", "d_slash", "wind_moon_slash"],
        #     "hp": 255, "max_hp": 255, "mp": 100, "max_mp": 100,
        #     "attack": 45, "defense": 30, "agility": 35, "accuracy": 95,
        #     "battle_normal": "gui/system/battle/s.webp",
        #     "battle_happy": "gui/system/battle/s_happy.webp",
        #     "battle_sad": "gui/system/battle/s_sad.webp",
        #     "battle_cast_1": "video/cast/s_cast_1.webm", 
        #     "battle_cast_2": "video/cast/s_cast_2.webm", 
        #     "lines": { ## реплики
        #         "attack": [],
        #         "cast": [],
        #         "hurt": [],
        #         "defend": [],
        #         "defeat": [],
        #         "win": [],
        #     },
        # }
        
    },
    "louise":      {
        "name": "Louise",      
        "color": "#fd7589",
        "description": "The magician who summoned Saito.\nAlthough she can use Void magic,\nits true nature remains unknown.",

        #CHOISES
        "portrait_choise": "gui/system/portraits/choises/l_full.webp",  
        "sprite_choise": "l 1",

        # battle: {
        #     "is_mage": True, "is_enemy": False,
        #     "skills": ["arrow", "heroism", "meteor", "dispel", "heal"],
        #     "hp": 200, "max_hp": 200, "mp": 150, "max_mp": 150,
        #     "attack": 25, "defense": 20, "agility": 30, "accuracy": 85,
        #     "battle_normal": "gui/system/battle/l.webp",
        #     "battle_happy": "gui/system/battle/l_happy.webp",
        #     "battle_sad": "gui/system/battle/l_sad.webp",
        #     "battle_cast_1": "video/cast/l_cast_1.webm", 
        #     "battle_cast_2": "video/cast/l_cast_2.webm", 
        #     "lines": { ## реплики
        #         "attack": [],
        #         "cast": [],
        #         "hurt": [],
        #         "defend": [],
        #         "defeat": [],
        #         "win": [],
        #     },
        # }

    },
    "siesta":      {
        "name": "Siesta",      
        'description': "A maid working at Tristain Academy of Magic.\nSince she is a commoner, she cannot use magic.\nShe has feelings for Saito.",

        #CHOISES
        "portrait_choise": "gui/system/portraits/choises/si_full.webp", 
        "sprite_choise": "si 1",
    },
    "tabitha":     {
        "name": "Tabitha", 
        "color": "#b4dfec",
        'description': "Louise's classmate.\nSpecializes in wind magic.\mHer nickname is \"Tabitha of the Snow Wind\".", 

        #CHOISES
        "portrait_choise": "gui/system/portraits/choises/t_full.webp",  
        "sprite_choise": "t 1",

        # battle: {
        #     "is_mage": True, "is_enemy": False,
        #     "skills": ["wing", "air_needle", "wind_break", "air_force", "heal"],
        #     "hp": 180, "max_hp": 180, "mp": 180, "max_mp": 180,
        #     "attack": 20, "defense": 18, "agility": 40, "accuracy": 90,
        #     "battle_normal": "gui/system/battle/t.webp",
        #     "battle_happy": "gui/system/battle/t_happy.webp",
        #     "battle_sad": "gui/system/battle/t_sad.webp",
        #     "battle_cast_1": "video/cast/t_cast_1.webm", 
        #     "battle_cast_2": "video/cast/t_cast_2.webm", 
        #     "lines": { ## реплики
        #         "attack": [],
        #         "cast": [],
        #         "hurt": [],
        #         "defend": [],
        #         "defeat": [],
        #         "win": [],
        #     },
        # }
    },
    "kirche":      {
        "name": "Kirche",      
        "color": "#e36566",
        'description': "Louise's classmate.\nSpecializes in fire magic.\nHer nickname is \"Kirche of the Mild Fever\".",

        #CHOISES
        "portrait_choise": "gui/system/portraits/choises/k_full.webp", 
        "sprite_choise": "k 1",

        # battle: {
        #     "is_mage": True, "is_enemy": False,
        #     "skills": ["fire", "fire_needle", "fire_arrow", "fire_shield", "heal"],
        #     "hp": 190, "max_hp": 190, "mp": 170, "max_mp": 170,
        #     "attack": 22, "defense": 22, "agility": 28, "accuracy": 88,
        #     "battle_normal": "gui/system/battle/k.webp",
        #     "battle_happy": "gui/system/battle/k_happy.webp",
        #     "battle_sad": "gui/system/battle/k_sad.webp",
        #     "battle_cast_1": "video/cast/k_cast_1.webm", 
        #     "battle_cast_2": "video/cast/k_cast_2.webm", 
        #     "lines": { ## реплики
        #         "attack": [],
        #         "cast": [],
        #         "hurt": [],
        #         "defend": [],
        #         "defeat": [],
        #         "win": [],
        #     },
        # }
        
    },
    "henrietta":   {
        "name": "Henrietta",   
        "color": "#782163",
        'description': "Princess of the Tristain Kingdom.\nChildhood friend of Louise.\nSpecializes in water magic.",

        #CHOISES
        "portrait_choise": "gui/system/portraits/choises/h_full.webp", 
        "sprite_choise": "h 1",

        # battle: {
        #     "is_mage": True, "is_enemy": False,
        #     "skills": ["water", "water_needle", "water_hazard", "water_blade", "heal"],
        #     "hp": 185, "max_hp": 185, "mp": 175, "max_mp": 175,
        #     "attack": 23, "defense": 25, "agility": 32, "accuracy": 87,
        #     "battle_normal": "gui/system/battle/h.webp",
        #     "battle_happy": "gui/system/battle/h_happy.webp",
        #     "battle_sad": "gui/system/battle/h_sad.webp",
        #     "battle_cast_1": "video/cast/h_cast_1.webm", 
        #     "battle_cast_2": "video/cast/h_cast_2.webm", 
        #     "lines": { ## реплики
        #         "attack": [],
        #         "cast": [],
        #         "hurt": [],
        #         "defend": [],
        #         "defeat": [],
        #         "win": [],
        #     },
        # }
    },
    "montmorency": {
        "name": "Montmorency", 

        #CHOISES
        "portrait_choise": "gui/system/portraits/choises/m_full.webp",  
        "sprite_choise": "m 1"
    },
    "haruna": {
        "name": "Haruna", 

        #CHOISES
        "portrait_choise": "gui/system/portraits/choises/ha_full.webp",  
        "sprite_choise": "ha 1"
    },

    "mage": {
        "name": "Mage", 
        "color": "#d82b2b",

        # battle: {
        #     "sprite_attack": "mage attack",
        #     "sprite_idle": "mage",
        #     "is_mage": True, "is_enemy": True,
        #     "skills": ["dark_bolt", "dark_nova"],
        #     "hp": 90, "max_hp": 90, "mp": 120, "max_mp": 120,
        #     "attack": 35, "defense": 12, "agility": 25, "accuracy": 85,
        #     "battle_cast_1": "video/cast/m_cast_1.webm", 
        #     "battle_cast_2": "video/cast/m_cast_2.webm", 
        #     "lines": {
        #         "attack": [],
        #         "cast": [],
        #         "hurt": [],
        #         "defeat": [],
        #     },
        # }
    },
}






# define tiffania = Character(_("Тиффания"), color="#fec979")
# define agnes = Character(_("Агнес"), color="#ede2ba")
