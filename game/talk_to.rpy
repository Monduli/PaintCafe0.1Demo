    label talk_to_cafe:

    menu:
        "You look around at who is visiting. (Current Day: [date])"

        "Dane" if who_list[0] == 1:
            jump dane_dialog

        "Ellie" if who_list[1] == 1:
            jump ellie_dialog

        "Dane and Ellie" if who_list[4] == 1:
            jump dane_ellie_dialog

        "Westra" if who_list[2] == 1:
            jump westra_dialog

        "Ember" if who_list[3] == 1:
            jump ember_dialog

        "Back":
            jump back


###########################

    label talk_to_smith:

    menu:
        "You look around at who is visiting. (Current Day: [date])"

        "Dane" if who_list[0] == 2:
            jump dane_dialog

        "Ember" if who_list[3] == 2:
            jump ember_dialog

        "Back":
            jump back

###########################

    label talk_to_castle:

    menu:
        "You look around at who is visiting. (Current Day: [date])"

        "Ellie" if who_list[1] == 3:
            jump dane_dialog

        "Westra" if who_list[2] == 3:
            jump ember_dialog

        "Back":
            jump back