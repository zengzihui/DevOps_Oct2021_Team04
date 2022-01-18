from msilib.schema import Class
from tkinter.messagebox import NO
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

    Zheng Jiongjie T01 9th December
    """

    options = {"1": "Start new game", "2": "Load saved game", "3": "Show high scores",
               "4": "Choose building pool", "5": "Choose city size", "": "", "0": "Exit"}

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


def start_new_game(width, height):
    """
    intializes new game object and start the turn

    Zheng Jiongjie T01 9th December
    """
    current_game = Game(width=width, height=height)
    return current_game.start_new_turn()


def prompt_city_size(current_size):
    """
    displays current city size and promts user to enter new city size
    returns the x and y value in a list

    Zheng Jiongjie T01 18th January
    """
    print("")
    print("--------- CURRENT CITY SIZE ---------")
    print("x-axis: {}".format(current_size[0]))
    print("y-axis: {}".format(current_size[1]))
    print("-------------------------------------")

    temp_city_size = {"x-axis": None, "y-axis": None}
    print("")
    print("Choose your city size below. Please take note that the multiplication of x and y cannot be more than 40.")
    print("")

    city_size_to_be_updated = True

    # get new x and y values for city size
    for key in temp_city_size:
        temp_city_size[key] = input("enter value for {}: ".format(key))
        # check if input is int
        try:
            temp_city_size[key] = int(temp_city_size[key])

            if temp_city_size[key] <= 0:
                city_size_to_be_updated = False
                print("")
                print("Invalid input has been entered. Please enter an integer.")
                break
        except Exception as e:
            city_size_to_be_updated = False
            print("")
            print("Invalid input has been entered. Please enter an integer.")
            break

    # check if area of new city size is more than 40
    if city_size_to_be_updated is True and temp_city_size["x-axis"] * temp_city_size["y-axis"] > 40:
        city_size_to_be_updated = False
        # city size does not change
        print("")
        print("The multiplication of x and y exceeds the limit of 40. City Size remains the same.")

    if city_size_to_be_updated:
        # display new city size to updated
        print("")
        print("--------- CHOSEN CITY SIZE ---------")
        print("x-axis: {}".format(temp_city_size["x-axis"]))
        print("y-axis: {}".format(temp_city_size["y-axis"]))
        print("-------------------------------------")
        return [temp_city_size["x-axis"], temp_city_size["y-axis"]]

    else:
        # display old city size since new city size is invalid
        print("")
        print("--------- CURRENT CITY SIZE ---------")
        print("x-axis: {}".format(current_size[0]))
        print("y-axis: {}".format(current_size[1]))
        print("-------------------------------------")
        return current_size


def exit_game():
    """
    exits program

    Zheng Jiongjie T01 9th December
    """
    exit(1)
