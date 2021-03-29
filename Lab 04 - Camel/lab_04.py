import easygui
import random

# variables
player = 10
hunter = 0
thirst = 10
stamina = 30
escape = 100
game = 1


def introduction():
    easygui.msgbox("Welcome To Running Prey :D", "Running Prey")
    easygui.msgbox(
        "You are being chased by hunters, choose what to do wisely to make it through the forest\n\nYou have a 10km Head Start\n\nYou Need To Cross 100km",
        "Running Prey")
    easygui.msgbox("Happy Hunting", "Running Prey")

def quit():
    again = easygui.ynbox("Would You Like To Try Again?", "Running Prey")
    if again:
        player = 10
        hunter = 0
        thirst = 10
        stamina = 30
        escape = 100
        game = 0

    elif not again:
        exit("Goodbye")


def actions():
    global player, escape, stamina, thirst, hunter
    while game:

        worl()

        action = easygui.choicebox("What Is Your Action?", "Running Prey",
                                   choices=["Drink From River", "Walk", "Run", "Check Surroundings", "Take A Rest",
                                            "Quit"])

        if action == "Drink From River":
            thirst = thirst + 3
            stamina = stamina + 1

        elif action == "Walk":
            stamina = - 1
            move = random.randrange(2, 6)
            escape = escape - move
            player = player + move

        elif action == "Run":
            stamina = stamina - 3
            move = random.randrange(4, 13)
            escape = escape - move
            player = player + move

        elif action == "Check Surroundings":
            print(player - hunter)
            easygui.msgbox(
                "Distance to Escape: {} \nDistance From Hunters: {}\nThirst: {}\nStamina: {}".format(escape,
                                                                                                     (player - hunter),
                                                                                                     thirst, stamina),
                "Running Prey")

        elif action == "Take A Rest":
            easygui.msgbox("The Hunter Gain Ground", "Running Prey")
            stamina = stamina + 7

        elif action == "Quit":
            quit()

        hunter = hunter + random.randrange(4, 9)

def worl():
    if escape <= 10:
        easygui.msgbox("Congratulations you have Won!")
        quit()

def main():
    while True:
        introduction()
        actions()


main()
