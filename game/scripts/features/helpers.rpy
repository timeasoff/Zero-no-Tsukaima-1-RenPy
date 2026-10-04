# open_door — стандартный дверной переход персонажа.
#   ИСПОЛЬЗОВАТЬ всегда, когда персонаж входит/выходит через дверь: спрайты уходят
#   со сдвигом (slide_left/right), играются звуки open_door/close_door, затем fade в
#   new_bg (или в black при new_bg=None). quit_side — сторона, куда уходит вошедший.
#   НЕ подменять дверной переход обычным fade_fx / show_sprites(None): пропадёт звук.
label open_door(quit_side="left", new_bg=None, stop_music=False):
    window hide
    if quit_side == "left":
        $ show_sprites(None, anim="slide_left")
    else:
        $ show_sprites(None, anim="slide_right")

    # трюк  ̶с̶ ̶ж̶̶̶о̶̶̶п̶̶̶о̶̶̶й̶̶̶   с black сделан, чтобы звук закрытия двери был с анимацией затухания
    pause(0.5)
    play sound open_door
    if stop_music is True:
        stop music fadeout 1.0
    pause(1.0)

    if new_bg is None:
        $ fade_fx("black", bg_position="default")
    else:
        $ fade_fx(new_bg)
    play sound close_door
    pause (1.0)
    return