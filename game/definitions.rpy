init python:
    import os
    
    def get_localized_path(path):
        base, ext = os.path.splitext(path)

        if _preferences.language == "japanese": 
            localized = f"{base}_jp{ext}"
        elif _preferences.language == "russian":
            localized = f"{base}_ru{ext}"
            
        if renpy.loadable(localized):
            return localized
        return path


# ==== IMAGES ====
image bg overlay = "bg/overlay.webp"

# forest
image bg forest = "bg/forest.webp"
image bg forest_evening = "bg/forest_evening.webp"
image bg forest_night = "bg/forest_night.webp"
image bg forest_blurred = "bg/forest_blurred.webp"

# sky
image bg sky = "bg/sky.webp"
image bg sky_night = "bg/sky_night.webp"
image bg sky_evening = "bg/sky_evening.webp"

# TOWN

# town_square
image bg town_square = "bg/town_square.webp"
image bg town_square_evening = "bg/town_square_evening.webp"
image bg town_square_night = "bg/town_square_night.webp"
image bg town_square_ruined = "bg/town_square_ruined.webp"
image bg town_square_night_blurred = "bg/town_square_night_blurred.webp"

# town
image bg town = "bg/town.webp"
image bg town_evening = "bg/town_evening.webp"
image bg town_night = "bg/town_night.webp"

# cafe
image bg cafe = "bg/cafe.webp"
image bg cafe_evening = "bg/cafe_evening.webp"
image bg cafe_night = "bg/cafe_night.webp"

# cafe_entrance
image bg cafe_entrance = "bg/cafe_entrance.webp"
image bg cafe_entrance_evening = "bg/cafe_entrance_evening.webp"
image bg cafe_entrance_night = "bg/cafe_entrance_night.webp"

# ACADEMY

# yard
image bg yard = "bg/yard.webp"
image bg yard_evening = "bg/yard_evening.webp"
image bg yard_night = "bg/yard_night.webp"
image bg yard_night_blurred = "bg/yard_night_blurred.webp"
image bg yard_ruined = "bg/yard_ruined.webp"
image bg yard_ruined_evening = "bg/yard_ruined_evening.webp"
image bg yard_ruined_night = "bg/yard_ruined_night.webp"

# classroom
image bg classroom = "bg/classroom.webp"
image bg classroom_evening = "bg/classroom_evening.webp"
image bg classroom_night = "bg/classroom_night.webp"

# kitchen
image bg kitchen = "bg/kitchen.webp"
image bg kitchen_evening = "bg/kitchen_evening.webp"
image bg kitchen_night = "bg/kitchen_night.webp"

# osman cabinet
image bg osman_cabinet = "bg/osman_cabinet.webp"
image bg osman_cabinet_evening = "bg/osman_cabinet_evening.webp"
image bg osman_cabinet_night = "bg/osman_cabinet_night.webp"

# library
image bg library = "bg/library.webp"
image bg library_evening = "bg/library_evening.webp"
image bg library_night = "bg/library_night.webp"

# library_table
image bg library_table = "bg/library_table.webp"
image bg library_table_evening = "bg/library_table_evening.webp"
image bg library_table_night = "bg/library_table_night.webp"

# siesta room
image bg si_room = "bg/si_room.webp"
image bg si_room_evening = "bg/si_room_evening.webp"
image bg si_room_night = "bg/si_room_night.webp"

#hallway
image bg hallway = "bg/hallway.webp"
image bg hallway_evening = "bg/hallway_evening.webp"
image bg hallway_night = "bg/hallway_night.webp"
#hallway_down
image bg hallway_down = "bg/hallway_down.webp"
image bg hallway_down_evening = "bg/hallway_down_evening.webp"
image bg hallway_down_night = "bg/hallway_down_night.webp"

#louise_room
image bg louise_room = "bg/louise_room.webp"
image bg louise_room_evening = "bg/louise_room_evening.webp"
image bg louise_room_night = "bg/louise_room_night.webp"

image bg room = "bg/room.webp"
image bg room_evening = "bg/room_evening.webp"
image bg room_night = "bg/room_night.webp"

#kirche_room
image bg kirche_room = "bg room"
image bg kirche_room_evening = "bg room_evening"
image bg kirche_room_night = "bg room_night"

#tabitha_room
image bg tabitha_room = "bg room"
image bg tabitha_room_evening = "bg room_evening"
image bg tabitha_room_night = "bg room_night"

#dining_hall
image bg dining_hall = "bg/dining_hall.webp"
image bg dining_hall_evening = "bg/dining_hall_evening.webp"
image bg dining_hall_night = "bg/dining_hall_night.webp"

# ==== CG ==== 

image cg terrorist = "cg/terrorist.webp"
image cg terrorist2 = "cg/terrorist2.webp"
image cg terrorist3 = "cg/terrorist3.webp"

image cg l_s_forest_l_speak = "cg/l_s_forest_l_speak.webp"
image cg l_s_forest_l_s_speak = "cg/l_s_forest_l_s_speak.webp"
image cg l_s_forest = "cg/l_s_forest.webp"
image cg l_forest = "cg/l_forest.webp"
image cg l_s_forest_s_speak = "cg/l_s_forest_s_speak.webp"

image cg ha_forest = "cg/ha_forest.webp"
image cg ha_forest_open = "cg/ha_forest_open.webp"

image cg ha_sick = "cg/ha_sick.webp"
image cg ha_sick_2 = "cg/ha_sick_2.webp"
image cg ha_sick_3 = "cg/ha_sick_3.webp"
image cg ha_sick_4 = "cg/ha_sick_4.webp"
image cg ha_sick_5 = "cg/ha_sick_5.webp"

image cg si_wakeup = "cg/si_wakeup.webp"
image cg si_wakeup_2 = "cg/si_wakeup_2.webp"

image cg ha_hug= "cg/ha_hug.webp"
image cg ha_hug_2 = "cg/ha_hug_2.webp"
image cg ha_hug_3 = "cg/ha_hug_3.webp"

image cg k_hug= "cg/k_hug.webp"
image cg k_hug_2 = "cg/k_hug_2.webp"
image cg k_hug_3 = "cg/k_hug_3.webp"

image cg butterbrot = "cg/butterbrot.webp"

image cg ready_to_blow = "cg/ready_to_blow.webp"
image cg ready_to_blow_2 = "cg/ready_to_blow_2.webp"

image l_feed = "cg/l_feed.webp"
image l_feed_2 = "cg/l_feed_2.webp"
image l_feed_3 = "cg/l_feed_3.webp"

image t_library_read = "cg/t_library_read.webp"
image t_library_read_2 = "cg/t_library_read_2.webp"
image t_library_read_3 = "cg/t_library_read_3.webp"
image t_library_read_4 = "cg/t_library_read_4.webp"

image cg t_massage = "cg/t_massage.webp"
image cg t_massage_2 = "cg/t_massage_2.webp"
image cg t_massage_3 = "cg/t_massage_3.webp"
image cg ha_moon = "cg/ha_moon.webp"

# chapter 3 (project ch2): Louise/Kirche clash; Akina's first appearance
image cg l_k_fight = "cg/l_k_fight.webp"
image cg l_k_fight_2 = "cg/l_k_fight_2.webp"
image cg l_k_fight_3 = "cg/l_k_fight_3.webp"
image cg l_k_fight_4 = "cg/l_k_fight_4.webp"
image cg ak_appear = "cg/ak_appear.webp"
image cg ak_sky = "cg/ak_sky.webp"


# ==== MUSIC ====
define audio.t1 = "audio/bgm/t1.ogg"
define audio.t2 = "audio/bgm/t2.ogg"
define audio.t3 = "audio/bgm/t3.ogg"
define audio.t4 = "audio/bgm/t4.ogg"
define audio.t5 = "audio/bgm/t5.ogg"
define audio.t6 = "audio/bgm/t6.ogg"
define audio.t7 = "audio/bgm/t7.ogg"
define audio.t8 = "audio/bgm/t8.ogg"
define audio.t9 = "audio/bgm/t9.ogg"
define audio.t10 = "audio/bgm/t10.ogg"
define audio.t11 = "audio/bgm/t11.ogg"
define audio.t12 = "audio/bgm/t12.ogg"
define audio.t13 = "audio/bgm/t13.ogg"
define audio.t14 = "audio/bgm/t14.ogg"
define audio.t15 = "audio/bgm/t15.ogg"
define audio.t16 = "audio/bgm/t16.ogg"
define audio.t17 = "audio/bgm/t17.ogg"
define audio.t18 = "audio/bgm/t18.ogg"
define audio.t19 = "audio/bgm/t19.ogg"
define audio.t20 = "audio/bgm/t20.ogg"
define audio.t21 = "audio/bgm/t21.ogg"
define audio.t22 = "audio/bgm/t22.ogg"
define audio.t23 = "audio/bgm/t23.ogg"
define audio.t24 = "audio/bgm/t24.ogg"
define audio.t25 = "audio/bgm/t25.ogg"
define audio.t26 = "audio/bgm/t26.ogg"
define audio.t27 = "audio/bgm/t27.ogg"
define audio.t28 = "audio/bgm/t28.ogg"
define audio.t29 = "audio/bgm/t29.ogg"
define audio.t30 = "audio/bgm/t30.ogg"
define audio.t31 = "audio/bgm/t31.ogg"
define audio.t32 = "audio/bgm/t32.ogg"

# ==== SOUNDS ====
define audio.blow = "audio/sfx/blow.ogg"
define audio.blow_2 = "audio/sfx/blow_2.ogg"
define audio.punch = "audio/sfx/punch.ogg"
define audio.take_sword = "audio/sfx/take_sword.ogg"
define audio.door = "audio/sfx/door.ogg"
define audio.knock_door = "audio/sfx/knock_door.ogg"
define audio.close_door = "audio/sfx/close_door.ogg"
define audio.open_door = "audio/sfx/open_door.ogg"
define audio.read = "audio/sfx/read.ogg"

