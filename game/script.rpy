label intro:
    $ renpy.movie_cutscene("video/intro.webm")
    return

label splashscreen:
    scene black
    pause (0.5)
    scene disclaimer with fade
    pause(2)
    scene black with fade
    pause(1)
    call intro from _call_intro
    return       


label start:
    jump ch0
    jump attention
    return
