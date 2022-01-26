from ast import While
from .game import Game
from .json import *
import os


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
    print("Width: {}".format(current_size[0]))
    print("Height: {}".format(current_size[1]))
    print("-------------------------------------")

    temp_city_size = {"width": None, "height": None}
    print("")
    print("Choose your city size below. Please take note that the multiplication of width and height cannot be more than 40.")
    print("Enter 0 to exit this configuration.")
    print("")

    city_size_to_be_updated = True
    while True:
        # flag
        exit_loop = False

        # get new height and width values for city size
        for key in temp_city_size:
            # exit function if user enter 0 when prompted for new city size
            if exit_loop:
                break

            while True:
                temp_city_size[key] = input("Enter value for {}: ".format(key.lower()))

                # exit and dont update values if user enters 0
                if temp_city_size[key] == "0":
                    print("")
                    print("City size will not be updated.")
                    city_size_to_be_updated = False
                    exit_loop = True
                    break

                # check if input is int
                try:
                    temp_city_size[key] = int(temp_city_size[key])
                    # check if int is 1 or more
                    if temp_city_size[key] <= 0:
                        print("")
                        print("Invalid input has been entered. Please enter an integer.")
                        print("")
                        continue
                    if key == "width" and temp_city_size[key] > 26:
                        print("")
                        print("Invalid input has been entered. Please enter an integer.")
                        print("")
                        continue
                    break
                except Exception as e:
                    print("")
                    print("Invalid input has been entered. Please enter an integer.")
                    print("")
                    continue

        # check if area of new city size is more than 40
        if city_size_to_be_updated is True and temp_city_size["width"] * temp_city_size["height"] > 40:
            # city size does not change
            print("")
            print("The multiplication of x and y exceeds the limit of 40. Please re-enter your input.")
            print("")
        else:
            break

    if city_size_to_be_updated:
        # display new city size to updated
        print("")
        print("--------- CHOSEN CITY SIZE ---------")
        print("Width: {}".format(temp_city_size["width"]))
        print("Height: {}".format(temp_city_size["height"]))
        print("-------------------------------------")
        return [temp_city_size["width"], temp_city_size["height"]]

    else:
        # display old city size since new city size is invalid
        print("")
        print("--------- CURRENT CITY SIZE ---------")
        print("Width: {}".format(current_size[0]))
        print("Height: {}".format(current_size[1]))
        print("-------------------------------------")
        return current_size


def exit_game():
    """
    exits program

    Zheng Jiongjie T01 9th December
    """
    exit(1)
