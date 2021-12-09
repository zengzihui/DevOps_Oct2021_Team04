from .game import Game


def main_menu(from_game_menu=None):
    """
    prints main menu and requests user for input

    eg.
    Welcome, mayor of Simp City!
    ----------------------------
    1. Start new game
    2. Load saved game
    0. Exit
    Your choice?

    Returns option selected by user: string
    """

    options = {"1": "Start new game", "2": "Load saved game", "": "", "0": "Exit"}

    menu_string = ""
    if not from_game_menu:
        menu_string += "Welcome, mayor of Simp City!\n----------------------------\n"
    else:
        menu_string += "\n"

    for key in options:
        if key == "":
            menu_string += "\n"
        else:
            menu_string += "{}. {}".format(key, options[key]) + "\n"
    menu_string = menu_string.rstrip()
    print(menu_string)
    # print(repr(menu_string))
    chosen_option = input("Your choice? ")

    while chosen_option not in options.keys() or chosen_option == "":
        print("Invalid input, please try again")
        chosen_option = input("Your choice? ")

    return chosen_option


def start_new_game():
    current_game = Game()
    return current_game.start_new_turn()


def exit_game():
    """
    exits program
    """
    exit(1)
