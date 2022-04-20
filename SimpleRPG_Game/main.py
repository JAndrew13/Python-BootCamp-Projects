

# function to ask play again or not
def play_again():
    print("\nDo you want to play again? (y or n)")

    # convert the player's input to lower_case
    answer = input(">").lower()

    if "y" in answer:
        # if player typed "yes" or "y" start the game from the beginning
        start()
    else:
        # if user types anything besides "yes" or "y", exit() the program
        exit()

    # game_over function accepts an argument called "reason"
def game_over(reason):
    # print the "reason" in a new line ()
    print("\n" + reason)
    print("Game Over!")
    # ask player to play again or not by activating play_again() function
    play_again()

# diamond room
def diamond_room():
    # give some prompts
    # \n is to print the text on a new line
    print("\nYou enter a room with glittering gemstones growing all around you!")
    print("One particular crystal is has a glowing blue light, below it appears to be a tunnel!")
    print("What would you like to do? (1 or 2)")
    print("1). Carefully extract the glowing crystal, and make you way through the tunnel.")
    print("2). Ignore the glittering room, its obviously a trap! Make your way down the dim tunnel")

    # take input()
    answer = input(">")

    if answer == "1":
        # the player is dead!
        game_over("You were cursed by the crystal, your skin begins to glow, and you are quickly engulfed with fire.")
    elif answer == "2":
        # the player won the game
        print("\nYou flee this shitty cave, and make your way through the tunnel. Congrats! You have Won!")
        play_again()
    else:
        # else call game_over() function with the reason argument
        game_over("You typed the wong input.. The dungeon hears your typo an the crystals collapsed all around you!")

# goblin room

def goblin_room():
    # give some prompts
    # \n is to print the text on a new line
    print("\nThere is an strange looking green man here.")
    print("Behind him you see another door")
    print("You see the pointy eared man sharpening a rusty shank, eek!")
    print("What would you like to do? (1 or 2)")
    print("1). Stay in the shadows, and try to slip past the goblin quietly.")
    print("2). Shout at the man, HEY - WHO LET YOU IN HERE?!")

    # take input()
    answer = input(">")

    if answer == "1":
        # the player is dead!
        game_over("You were quickly shanked by the tiny goblin, R.I.P, He also looted your corpse.")
    elif answer == "2":
        # lead player to the diamond_room()
        print("\nThe goblin is terrified by your presence, he apologizes profusely and shows himself out!")
        diamond_room()
    else:
        # else call game_over() function with the reason argument
        game_over("Dont you know how to type a number? The goblin has shanked you!")

# boar room
def boar_room():
    # give some prompts
    # \n is to print the text on a new line
    print("\nThere is an Angry Boar here.")
    print("Behind the boar you see another door")
    print("You see the boar rooting around a bin of.. carrots?")
    print("What would you like to do? (1 or 2)")
    print("1). Quickly nab a tasty carrot.")
    print("2). Scare the boar.")

    # take input()
    answer = input(">")

    if answer == "1":
        # the player is dead!
        game_over("You were brutally impaled by the boar, R.I.P")
    elif answer == "2":
        # lead player to the diamond_room()
        print("\nThe boar is terrified by your sneak attack, he flees the room in terror!")
        diamond_room()
    else:
        # else call game_over() function with the reason argument
        game_over("Dont you know how to type a number? The boar has impaled you!")

def start():
    # Give some prompts
    print("\nYou are standing in a dark room, the air is damp..")
    print("\nYou hear a strange snarl echo into the room! Oh dear!")
    print("\nThere is a door to your LEFT and RIGHT, which way would you ike to go?")

    # Convert players input() into lower case
    answer = input(">").lower()

    if "l" in answer:
        # if player typed Left or L, Lead player to boar_room()
        boar_room()
    elif "r" in answer:
        #else if player typed Right or R, Lead player to goblin_room()
        goblin_room()
    else:
        # else call game_over() function with the "reason" argument
        game_over("You must enter R or L to proceed.")

# start the game
start()

