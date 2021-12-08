
def main_menu():
    """
    prints main menu and requests user for input

    eg.
    Welcome, mayor of Simp City!
    ----------------------------
    1. Start new game
    2. Load saved game
    0. Exit
    Your choice?

    returns user's input option: string
    """

    options = {"1": "Start new game", "2": "Load saved game", "0": "Exit"}

    menu_string = ""

    menu_string += "Welcome, mayor of Simp City!\
        \n----------------------------\n"

    for key in options:
        menu_string += "{}. {}".format(key, options[key]) + "\n"

    print(menu_string)
    # print(repr(menu_string))
    chosen_option = input("Your choice? ")

    return chosen_option
