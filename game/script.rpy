## TODO: Location sync
## TODO: If day advances, but character not spoken to, don't advance story (might already work)

    init python:
        import game as g
        renpy.music.register_channel("ambience", mixer="sound", loop=True)
        debug = 1
        class Quit(Action):

            def __init__(self, confirm=True, msg=layout.QUIT):
                self.confirm = confirm
                self.msg = msg

            def __call__(self):
                if self.confirm:
                    renpy.loadsave.force_autosave()
                    layout.yesno_screen(self.msg, Quit(False))
                else:
                    g.on_quit(gamedata)
                    renpy.quit()

    define d = Character("Dane")
    define n = Character("Cuppa")
    define e = Character("Ellie")
    define w = Character("Westra")
    define emb = Character("Ember")
    define r = Character("Rock")

    label main_menu:    # No main menu
        return          # get outta there, stop that
    label start:
    scene bg paint cafe

    python:
        _game_menu_screen = "preferences"
        flag = None                                     # Set placemarker flag to none
        gamedata = g.initialize()                       # Put data[""] into gamedata object
        add_day = g.find_day(gamedata)                  # Determine if it is the same day as it was when last opened
        try:
            if gamedata["playername"]:                  # If a name is already set
                playername = gamedata["playername"]     # then someone completed the tutorial
                flag = "continue"                       # and we should skip the tutorial and get to the selection menu.
        except KeyError:                    # (If there's no name)
            print("Name not found.")        # (Then they didn't do the tutorial yet)
    if flag == "continue":                              # If there is a name and a tutorial completed
        jump continue                                   # Continue the game
    else:
        jump new

    label continue:

    python:
        print("Days elapsed: " + str(gamedata["days"]))
        if add_day:
            print("It's a new day.")
            gamedata["dane_talked"] = False
            gamedata["ellie_talked"] = False
            gamedata["westra_talked"] = False
            gamedata["ember_talked"] = False
            gamedata["dane_ellie_talked"] = False
            patron_list = g.who_here(gamedata)
            who_list = g.check_who(patron_list)
        else:
            print("It's the same day.")
            patron_list = gamedata["in_cafe"]
            who_list = g.check_who(patron_list)
            dane_talked = gamedata["dane_talked"]

    label selection:

    python:
         date = gamedata["date"]
         gamedata["location"] = "Cafe"
         

    scene bg paint cafe
    stop music fadeout 1.0
    play ambience rain

    label back:

    python:
        location = gamedata["location"]

    menu:
        "What would you like to do? You are currently at the [location]."

        "Talk to someone.":
            python:
                if gamedata["location"] == "Cafe":
                    renpy.jump(label='talk_to_cafe')
                if gamedata["location"] == "Blacksmith":
                    renpy.jump(label='talk_to_smith')
                if gamedata["location"] == "Castle":
                    renpy.jump(label='talk_to_castle')

        "Move." if gamedata["days"] >= 3:
            jump move_menu

        "Debug" if debug == 1:
            jump debug

        "Save & Quit":
            python:
                g.on_quit(gamedata)
                renpy.quit()
        
    label debug:
    menu:
        "Debug options."

        "Add Day":
            "Advancing Day. Please hold on to your seats."
            python:
                gamedata["date"] += "69 lmao"
                g.on_quit(gamedata)
                renpy.quit()

        "Delete Save":
            menu:
                "Are you sure you want to delete your save data?"

                "Yes.":
                    n "Thanks for stopping by."
                    python:
                        g.delete_save()
                        renpy.quit()

                "No.":
                    jump debug

        "View Inventory":
            jump inventory

        "Console Output Gamedata":
            "Current Days Elapsed: [gamedata[days]]"
            jump debug

        "Back":
            jump back

    label inventory:
    menu:
        "In your current inventory, you have:"

        "Coffee" if "Coffee" in gamedata["inventory"]:
            "A steaming cup of coffee. From the first conversation with Dane and Ellie."
            jump inventory
        "Tea" if "Tea" in gamedata["inventory"]:
            "A steaming cup of tea. From the first conversation with Dane and Ellie."
            jump inventory
        "Water" if "Water" in gamedata["inventory"]:
            "A standard cup of water. From the first conversation with Dane and Ellie."
            jump inventory
        "Back":
            jump back

    label move_menu:
    menu:
        "Where would you like to move to?"

        "Outside." if gamedata["days"] >= 3 and gamedata["location"]=="Cafe":
            jump outside_menu

        "Blacksmith." if gamedata["c_ember"] >= 2 and gamedata["location"]!="Blacksmith":
            scene bg blacksmith
            python:
                gamedata["location"]="Blacksmith"
                renpy.jump("back")

        "Castle." if gamedata["c_dane"] >= 2 and gamedata["location"]!="Castle":
            scene bg castle
            play ambience outside
            python:
                gamedata["location"]="Castle"
                renpy.jump("back")

        "Cuppa's Cafe." if gamedata["location"] != "Cafe":
            jump selection

        "Back":
            jump back

    label outside_menu:
    scene bg outside
    "It is cold and rainy outside. The streets are empty and nobody is seen wandering around."
    jump selection