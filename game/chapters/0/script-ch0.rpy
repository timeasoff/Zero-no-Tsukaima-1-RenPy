label ch0:
    stop music fadeout 2.0
    call overlay_screen("town_square_night", "Tristania") from _call_overlay_screen
    $ blow_fx(new_music="t23", music_fadein=2)
    #$ scene_fx(effect="blow", duration=1, sound="blow", new_music="t23", music_fadein=2)
    pause(0.5)

    $ show_sprites(("soldier 1 angry"), mode="tall", anim="dissolve")
    voice "ch0_soldier_001"
    commander "Where did the explosion happen?"

    $ show_sprites(("soldier 1 angry", "soldier 1 angry"), mode="tall")

    voice "ch0_soldier_002"
    soldier "Sir—on the street facing the main avenue, multiple explosions involving explosive materials have been confirmed."

    voice "ch0_soldier_003"
    commander "Hurry up and dispatch the fire response team. Do not let the damage escalate."

    voice "ch0_soldier_004"
    soldier "Yes, Sir!"

    call overlay_screen(None,  "My name is Louise Françoise Le\u00A0Blanc\u00A0de\u00A0La\u00A0Vallière", text_mode="white", delay=5.5, sound_path="ch0_l_001") from _call_overlay_screen_1
    $ fade_fx("town_square_night", sprites=("soldier 1", "soldier 1"), mode="tall")

    voice "ch0_un_001"
    unk "Hahahaha. You're always working hard."

    $ show_sprites(("soldier 1 sad", "soldier 1"), mode="tall", raise_z=False)

    voice "ch0_soldier_005"
    commander "Where is he?"

    $ show_sprites(("soldier 1 sad", "soldier 1 angry "), mode="tall")
    voice "ch0_soldier_006"
    soldier "Sir, he's on top of that mansion."

    call overlay_screen(None, "The Pentagon that governs the five powers", text_mode="white", delay=3.5, sound_path="ch0_l_002") from _call_overlay_screen_2
    $ fade_fx("terrorist", type="cg")

    voice "ch0_un_002"
    unk "Let's call it a day. Hurry up and put out the fire."

    voice "ch0_soldier_007"
    commander "You—what's your objective?"

    voice "ch0_un_003"
    unk "Objective? To dismantle every rule this country stands on."

    voice "ch0_soldier_008"
    soldier "Huh?"

    voice "ch0_un_004"
    unk "Until then, you'll just have to cherish your mundane lives, won't you?"

    $ flash_fx("terrorist2", type="cg")

    voice "ch0_soldier_009"
    soldier "He… did he just vanish?"

    voice "ch0_soldier_010"
    commander "Hey! Apprehend him immediately!"

    voice "ch0_soldier_011"
    soldier "Yes, Sir!"

    call overlay_screen(None, "Bestow blessings upon this one, and make them my familiar", delay=4.5, text_mode="white", sound_path="ch0_l_003") from _call_overlay_screen_3
    stop music fadeout 1.0
    pause(1)
    call intro from _call_intro_1

    jump ch1