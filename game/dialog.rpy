#####################################################
#####################################################
### INTRO ###
label new:

    "Welcome to my tavern."
    "What is your name?"

    # character name is set here
    define pov = Character("[povname]")

    python:
        povname = renpy.input("What is your name?")
        playername = povname.strip()
        gamedata["playername"] = playername
        if not playername:
             playername = "Dan"

    "Welcome, [playername]."
    n "My name is Cuppa. Thanks for choosing my establishment."
    n "People love to visit, and have they always have things to say."
    n "Why don't you stick around for a while and see who pops up?"

    python:
        gamedata['characters'] = [
        g.Char("Dane", 11),
        ]
        g.on_quit(gamedata);

    jump continue

##########################################################################################
##########################################################################################
##### DANE ###################
label dane_dialog:
    play music dane
    scene wall
    show tabled
    show dane behind tabled at truecenter
    if gamedata["dane_talked"]:
        "He sips his drink and nods at you."
        d "Always good to see you, [playername]."
        jump selection
    python:
        if gamedata["dane_talked"] == False:
            gamedata["c_dane"] += 1
            convo = "dane_" + str(gamedata["c_dane"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(d, "Error: End of dialog.")
                renpy.jump("selection")
        else:
            renpy.jump("selection")


##########################################################################################
##########################################################################################
##### ELLIE ###################

label ellie_dialog:
    play music ellie
    scene wall
    show tabled
    show ellie behind tabled at truecenter
    if gamedata["ellie_talked"]:
        if gamedata["c_ellie"] < 5:
            "She sips her drink and looks down at you."
            e "What do you want?"
        else:
            e "Hello, [playername]. Do you need something from me?"
        jump selection
    python:
        if gamedata["ellie_talked"] == False:
            gamedata["c_ellie"] += 1
            convo = "ellie_" + str(gamedata["c_ellie"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(e, "Error: No Ellie dialog.")
                renpy.jump("selection")
        else:
            renpy.jump("selection")



##########################################################################################
##########################################################################################
##### WESTRA ###################

label westra_dialog:
    play music westra
    scene wall
    show tabled
    show westra behind tabled at truecenter
    if gamedata["westra_talked"]:
        if gamedata["c_westra"] < 5:
            "She looks at you coldly."
            w "What?"
        else:
            w "Hello, [playername]."
        jump selection
    python:
        if gamedata["westra_talked"] == False:
            gamedata["c_westra"] += 1
            convo = "westra_" + str(gamedata["c_westra"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(w, "Error: No dialog.")
                renpy.jump("selection")
        else:
            renpy.jump("selection")



##########################################################################################
##########################################################################################
##### EMBER ###################

label ember_dialog:
    play music dane
    scene wall
    show tabled
    show ember behind tabled at truecenter
    if gamedata["ember_talked"]:
        if gamedata["c_ember"] < 5:
            "She turns to you and waves widely."
            emb "Hiiiiiiii [playername]!!!"
        else:
            emb "Good to see you, [playername]."
            "She smiles at you."
        jump selection
    python:
        if gamedata["ember_talked"] == False:
            gamedata["c_ember"] += 1
            convo = "ember_" + str(gamedata["c_ember"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(emb, "Error: No Ember dialog.")
                renpy.jump("selection")
        else:
            renpy.jump("selection")



##########################################################################################
##########################################################################################
##### DANE & ELLIE ###################

label dane_ellie_dialog:
    play music deli
    scene wall
    show tabled
    show dane behind tabled at right
    show ellie behind tabled at left
    if gamedata["dane_ellie_talked"]:
        "He sips his drink and nods at you."
        d "Always good to see you, [playername]."
        jump selection
    python:
        if gamedata["dane_ellie_talked"] == False:
            gamedata["c_dane_ellie"] += 1
            convo = "dane_ellie_" + str(gamedata["c_dane_ellie"])
            if renpy.has_label(convo) == True:
                renpy.jump(convo)
            else:
                renpy.say(d, "Dane has nothing left to say.")
                renpy.jump("selection")
        else:
            renpy.jump("selection")

##########################################################################################
##########################################################################################
## DANE DIALOG ##

label dane_1:
    python:
        print("Dane 1 playing.")
    d "Hello there!"
    menu:
        d "Have we met before?"

        "No, I don't think so.":
            d "Well, that's alright. There's a first time for everything!"
        "My name is [playername].":
            d "It's great to meet you, [playername]."
    d "My name is Silas Dane, if you were curious."
    d "I hope you'll come and talk to me again sometime!"
    jump dane_done

label dane_2:
    python:
        print("Dane 2 playing.")
    d "Hello again, [playername]!"
    d "Last we spoke, did I tell you what I do for a living?"
    d "I'm actually a royal bodyguard. I actually protect a princess when I'm not here."
    d "Maybe I'll bring her here sometime. She's a bit picky, but.. who knows?"
    d "Her name is Ellie. You should talk with her if you see her around."
    d "Well, maybe not, she.. doesn't exactly get us common folk."
    d "You should come visit us at the castle, actually. I'll mark it on your map so you can come take a look."
    d "It's busy sometimes and the common folk might struggle to get near it depending on what's going on..."
    d "But, it would be nice to see a friendly face over there if you get a chance."
    d "Anywho, have a good one, [playername]."
    jump dane_done

label dane_3:
    python:
        print("Dane 3 playing.")
    d "Oh, [playername]! I didn't expect you to take me up on my offer to see the castle."
    d "It's good to see you. Also, I'm not finished writing this part yet."
    d "Bye nerd lollllll"
    jump dane_done
    
label dane_done:
    python:
        gamedata["dane_talked"] = True

    jump selection

##########################################################################################
##########################################################################################
## ELLIE DIALOG ##

label ellie_1:
    python:
        print("Ellie 1 playing.")
    "A short irritated lady looks simultaneously confused and concerned as you approach."
    menu:
        e "What?"

        "I just wanted to --":
            e "You just wanted to get in my space."
        "My name is --":
            e "Is the name of a peasant important to me?"
    e "I'll have you know that you are speaking to royalty. I shouldn't even be in a place like this."
    e "My boneheaded bodyguard told me to come here and wait for him in a \"lovely, peaceful atmosphere\"."
    e "I can't fathom what in the world he could be talking about in regards to this.. hole."
    e "Now then, leave me alone to enjoy my tea. Far on the other side of the room, preferably."
    jump ellie_done

label ellie_2:
    python:
        print("Ellie 2 playing.")
    menu:
        e "You again. What do you want this time?"

        "Waiting for Dane again?":
            e "Yes, of course I am. I'm always waiting for him. Why else would I spend my time here?"
        "Just saying hello.":
            e "Well, I'm sure there are plenty of other people who would rather hear your greetings than I."
        "....":
            e "Don't just stand there. If you're going to stand somewhere, do it somewhere else."

    e "After all, I am royalty! And you will treat me as such!"
    e "I, Princess Elena Adelaide, deserve better than your company."
    e "... But, then again, I am waiting for him again, and I don't have much else to do..."
    menu:
        e "Fine. Tell me your name, commoner."

        "My name is [playername].":
            e "[playername]? The names the common people give their children these days, I swear."
        "I am Silas Dane, Royal Bodyguard!":
            e "Is that supposed to be a joke? I could see him saying that... but that is most assuredly not who you are."
            e "[playername] sounds like the name of a commoner. So I will call you that."

    e "You will visit with me again. I'm sure I'll be waiting here many more times for that.. oaf.. so I require the company."

    jump ellie_done

label ellie_done:
    python:
        gamedata["ellie_talked"] = True

    jump selection

##########################################################################################
##########################################################################################
## WESTRA DIALOG ##
label westra_1:
    python:
        print("Westra 1 playing.")
    "You decide to approach a lady at the bar."
    menu:
        "She sits atop a barstool reading a book. She doesn't notice you."

        "Excuse me.":
            w "Yes, excuse you."
        "Enjoying your book?":
            w "Enjoying pestering people who are trying to enjoy their book?"
    w "I just want my peace and quiet. Please leave me alone."
    "She goes back to reading her book. Perhaps now isn't the best time."
    jump westra_done

label westra_2:
    python:
        print("Westra 2 playing.")
    "You decide to approach the wizard again."
    menu:
        "The scholarly woman is still reading her book."

        "What are you reading?":
            w "None of your business."
        "Can I buy you a drink?":
            w "No."
        "...":
           "She still doesn't notice you standing there."

    "She continues reading her book without acknowledging you further."
    menu:

            "Why won't you talk to me?":
                w "Because I'm busy studying my spellbook. This is important royal work. Leave me alone."
            "Fine. I'll leave then.":
                w "Good. These spells won't study themselves."

    "You leave her to study her spells."

    jump westra_done

label westra_3:
    python:
        print("Westra 3 playing.")
    

label westra_done:
    python:
        gamedata["westra_talked"] = True

    jump selection

##########################################################################################
##########################################################################################
## EMBER DIALOG ##
label ember_1:
    python:
        print("Ember 1 playing.")
    "You see a red-headed lady at the bar."
    menu:
        "Atop her barstool, she spins around and shouts boisterously and unintelligibly at the other patrons."

        "Um.. hello there.":
            emb "Hiiiiii!"
        "Having fun?":
            emb "Yesssssssss!"
    emb "I'm Ember!! Whooooo are you?"
    menu:
        "Despite asking you this, she continues spinning uncontrollably."

        "I'm [playername]. Who are you?":
            emb "Hiiiiii [playername]!"
        "Could you stop spinning please?":
            emb "Noooooope! I'll never stop!"

    "She stands up proudly on her seat, holding her questionably marked bottle."
    emb "You need to try some of this stuff they're serving here!"
    "She hiccups audibly and falls down into her seat. She seems to have been quieted down by gravity."
    emb "We shoulddd talk sometimee. Ttalk more. Drink, MORE! We shouldd.. ddrink somettime.."
    "She falls asleep in her chair."
    "Perhaps you should leave her be."
    jump ember_done

label ember_2:
    python:
        print("Ember 2 playing.")
    "The boisterous woman is back at the bar again."
    menu:
        emb "Hiiiii [playername]!"

        "Hello again, Ember.":
            emb "You said hi to me yaaaaay."
        "Can I.. buy you a drink?":
            emb "I already have a drink but okay!"
        "...":
           "Hiiiiii quiet person!!"

    "She spins around in her chair. It's clear that she's excited to see you."
    menu:

        "What brings you here?":
            emb "Drinking! Drinking drinking and more drinking! BARTENDER!!"
        "Uh.. nice weather we're having.":
            emb "I wouldn't know, I've been inside too long!! Speaking of which..."

    "She slams on the table."
    n "I told you that you're being cut off. Please stop asking for more drinks."
    emb "Uuuuuugh. You're no funnnnnn! You should be more fun! And you should drink!!"
    "Cuppa walks away sighing."
    n "Good luck with this one, [playername]. She's a slippery one."
    emb "And your jokes suck!!"
    "She sits back in her chair and continues drinking her questionable liquid."
    emb "I'll buy you something next time! We can drink together!!"
    "She turns away from you and starts shouting for the bartender again."

    jump ember_done

label ember_done:
    python:
        gamedata["ember_talked"] = True

    jump selection

##########################################################################################
##########################################################################################
## DANE + ELLIE DIALOG ##
label dane_ellie_1:
    python:
        print("Dane+Ellie 1 playing.")
    d "Hello there!"
    e "Yes.. hello, [playername]."
    d "We were just about to order our drinks. Care to join us?"
    e "Do we have to order peasant drinks? I'm not so sure about this.. bean juice."
    d "But you like tea, which is leaf juice."
    e "It's different! Tea is tea. Coffee is a dark abyss of bean juice."
    "Ellie grumbles at Dane, but realizes that she's staring at him and starts to blush and turn away."
    e "But, but, if you.. like it.. then it's okay, I guess.."
    d "Backing down so quickly? Does this mean you've succumbed to my bean juice powers?"
    "She crosses her arms."
    e "I've succumbed to your ability to waste our guest's time! How could you do this to your princess??"
    menu:
        d "Ah, you're right. Would you like to order something?"

        "Just some good old fashioned bean juice.":
            d "Yeah, that's the spirit. Cuppa, some coffee for our friend here!"
            n "Sure, sure."
            "You receive a piping hot cup of joe."
            python:
                gamedata["inventory"].append("Coffee")
        "Is the tea here any good?":
            e "I mean, I wouldn't call it excellent, but..."
            n "Here you are."
            "You are handed a cup of tea. It's unclear which tea it is."
            python:
                gamedata["inventory"].append("Tea")
        "Water is fine.":
            e "You're boring. You should order something else."
            n "Water for the.. boring one. Ha ha."
            "Cuppa hands you a cuppa water."
            python:
                gamedata["inventory"].append("Water")

    d "Well, we'll be here enjoying our drinks if you need anything."
    e "Dane, how much longer do we have to stay here?"
    d "We don't have to stay here too much longer, but I would like to enjoy my coffee.."
    "You leave them to their bickering."
    jump dane_ellie_done

label dane_ellie_2:
    python:
        print("Dane+Ellie 2 playing.")
    d "Hello again, [playername]!"
    e "Back again? You can actually stand being around Dane?"
    d "Now, now. This is what it's like having friends, Ellie."
    e "I wouldn't know. I was locked up in that castle for so long with hardly anyone competent to talk to."
    e "Not that my current company is much of an improvement."
    "She glares at Dane, but there's something in her eyes that doesn't indicate anger."
    d "What's that supposed to mean? You know I was captain of the guard.."
    e "Yes, yes, this again. We all know you were a Guard Captain. It's really not that prestigious or anything."
    d "Well, I certainly think it is. What do you think, [playername]?"
    menu:
        d "Well, I certainly think it is. What do you think, [playername]?"

        "Captain of the Guard? Pretty impressive.":
            d "Exactly. I worked for a long time to get to where I am."
            "Dane smiles to himself."
        "Eh, I've seen better...":
            e "Yes, that's what I'm saying. It's nothing impressive."
            "Her tone of voice seems to indicate that she feels otherwise, but you decide not to pursue it."
    d "Well, in any event, I would like a cup of coffee before going back out into the field."
    e "Yes, today we're looking for some cultists. They're supposed to be holed up in a cave outside of town, actually."
    d "You'd better stay safe, [playername]. You never know what's going on outside these walls."
    "He smiles at you as you walk back to your table."

    jump dane_ellie_done

label dane_ellie_done:
    python:
        gamedata["dane_ellie_talked"] = True

    jump selection
