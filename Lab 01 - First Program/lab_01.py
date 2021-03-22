from easygui import *

from random import *

#variable
name = enterbox("What is Your Name", "Name Please")
yoda_quit = 1
password_creator_quit = 1
random_island_quit = 1

prg = choicebox("What program do you want to run?", "Program Picker", choices=["Yoda The Prophet", "Password Creator", "Random Island", "Quit"])

while True:
    # Yoda Program
    if prg == "Yoda The Prophet":
        yoda_answers = ["Train yourself to let go of everything you fear to lose.", "You must unlearn what you have learned.", "Difficult to see. Always in motion is the future...", "Through the Force, things you will see. Other places. The Future...the past. Old friends long gone.", "Always pass what you have learned.", "Looking? Found someone you have, eh?", "Yes, a Jedi's strength flows from the Force. but beware of the dark side.", "You will find only what you bring in.", "PATIENCE YOU MUST HAVE my young padawan.", "Do or do not. There is no try."]
        while yoda_quit == 1:
            reply = choice(yoda_answers)
            enterbox("Question any you may ask young {}".format(name), "Yoda The Prophet")
            msgbox(reply, "Yoda The Prophet")
            yoda_quit = ynbox("Would You Like to ask yoda another question?", "Yoda The Prophet")

    # Password creator
    elif prg == "Password Creator":
        msgbox("Welcome {} to Password Creator".format(name), "Password Creator")
        noun = ["Cat", "Dog", "Jack", "Pony", "Fireball", "Car", "Fairy", "H"]
        adjective = ["Shiny", "Smelly", "Hot", "Cold", "W", "Dark", "Fluffy"]
        while password_creator_quit:
            number = [randrange(0, 99), "36", "85", "79", "54", "74", "85", "Y"]
            msgbox("Your New Password is:\n{}{}{}".format(choice(adjective), choice(noun), choice(number)), "Password Creator")
            password_creator_quit = ynbox("Would You Like A Different Password?")

    # Random Island Program
    elif prg == "Random Island":
        female = ["A Cat", "A Depressed Witch", "A drunken Princess", "A wild Nurse", "An Elven Archer"]
        male = ["a Dog", "Jerry", "a very Muscular Centaur", "a Lizardman", "a Goldfish"]
        place = ["At Home", "on Pluto", "On the Dinosaur", "In the Giant Ape", "At Work"]
        female_wore = ["a brown cape", "a red tophat", "a green tuxedo", "a dead lion(unskinned)", "a yellow beanie"]
        male_wore = ["a pink tutu dress", "a sparkly purple dress", "a bright yellow flamingo top hat", "a beautiful white wedding dress", "a purple skirt"]
        female_said = ["what am I", "what are you", "how does one fly", "do birds have baths?", "Yay"]
        male_said = ["love is life,life is love", "i love beans", "this macaroni is good", "kono dio da", "CHIPS PLEASE!!"]
        result = ["a JoJo's Reference", "Saten Attac 4", "Zombie Apocalypse", "Lies", "the government being overthrown", "CHIPS AND YAY"]
        planet_said = ["DIE DIE DIE", "NANI!!", "Oh noo, we ran out of milk", "oh look meteors", "im pretty sure the suns getting closer"]
        msgbox("Welcome {} to Random Island".format(name), "Random Island")
        while random_island_quit == 1:
            msgbox("{} met {} {}. She was wearing {} and he was wearing {}".format(choice(female), choice(male), choice(place), choice(female_wore), choice(male_wore)), "Random Island")
            msgbox("The female said {}, the man responded {}, the result was {}, and the planet said {}.".format( choice(female_said), choice(male_said), choice(result), choice(planet_said)), "Random Island")
            random_island_quit = ynbox("Would You Like Another Random Island?", "Random Island")

    # quit function
    elif prg == "Quit":
        break

    another_program = ynbox("Would you like to run another program?", "Program Picker")
    if another_program:
        prg = choicebox("What program do you want to run?", "Program Picker", choices=["Yoda The Prophet", "Password Creator", "Random Island", "Quit"])
    else:
        break
msgbox("Closing Program Now...", "Goodbye")
# program ends
# exit("Goodbye")
