label attention:

    $ fade_fx("black", new_music="t32")

    centered "{size=+14}Congratulations!!!{/size}"
    centered "{size=+14}You've reached the end of the available content!{/size}"
    centered "{size=+14}The translation is not yet complete.{/size}"
    centered "{size=+14}You can actively participate in the translation!{/size}"
    centered "{size=+14}You can find the contact information in the \"About the Game\" section.{/size}"

    menu:
        "Return to the main menu":
            return

        "An interactive story about the remaster ⬅️⬅️⬅️":
            call remark from _call_remark
    return