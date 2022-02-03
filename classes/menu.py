import json
from .game import Game
from .json import *
import os
from .building import Building
from .shop import Shop
from .factory import Factory
from .highway import Highway
from .house import House
from .beach import Beach
import os.path


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


def start_new_game(width, height, building_pool):
    """
    intializes new game object and start the turn

    Zheng Jiongjie T01 9th December
    """
    current_game = Game(width=width, height=height, building_pool=building_pool)
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
                        print("Invalid input has been entered. Please enter a number.")
                        print("")
                        continue
                    if key == "width" and temp_city_size[key] > 26:
                        print("")
                        print("Invalid input has been entered. Please enter a number.")
                        print("")
                        continue
                    break
                except Exception as e:
                    print("")
                    print("Invalid input has been entered. Please enter a number.")
                    print("")
                    continue

        # check if area of new city size is more than 40
        if city_size_to_be_updated is True and temp_city_size["width"] * temp_city_size["height"] > 40:
            # city size does not change
            print("")
            print("The multiplication of width and height exceeds the limit of 40. Please re-enter your input.")
            print("")
        else:
            break

    if city_size_to_be_updated:
        # display new city size to updated
        print("")
        print("--------- CHOSEN CITY SIZE ---------")
        print("Width: {}".format(temp_city_size["width"]))
        print("Height: {}".format(temp_city_size["height"]))
        print("------------------------------------")
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


def load_game():
    """
    load game from save file

    Zheng Jiongjie T01 25th January
    """
    loaded_game = Game()
    if os.path.isfile("game_save.json") is False:
        print("")
        print("No save game found!")
        return False
    with open("game_save.json", "r") as save_file:
        save_data = json.load(save_file)
        try:
            loaded_game.building_pool = save_data["building_pool"]
            loaded_game.turn_num = save_data["turn_num"]
            loaded_game.width = save_data["width"]
            loaded_game.height = save_data["height"]
            loaded_game.randomized_building_history = save_data["randomized_history"]

            loaded_game.board = []
            for row in range(0, loaded_game.height):
                loaded_game.board.append([])
                for col in range(0, loaded_game.width):
                    if str(col) + "," + str(row) in save_data["board"]:
                        building_str = save_data["board"][str(col) + "," + str(row)]

                        if building_str == "SHP":
                            loaded_game.board[row].append(Shop(col, row))
                        elif building_str == "HSE":
                            loaded_game.board[row].append(House(col, row))
                        elif building_str == "FAC":
                            loaded_game.board[row].append(Factory(col, row))
                        elif building_str == "HWY":
                            loaded_game.board[row].append(Highway(col, row))
                        elif building_str == "BCH":
                            loaded_game.board[row].append(Beach(col, row))
                    else:
                        loaded_game.board[row].append(Building())
            return loaded_game
        except Exception as e:
            print("")
            print("Failed to load game!")
            return False


def building_display(buildings_list):
    """
    return chosen buildings displayed string

    Swah Jian Oon T01 19th December
    """
    temp_flag = False
    building_display = ""
    if len(buildings_list) != 0:
        for building in buildings_list:
            if temp_flag == False:
                building_display = "{0}".format(building)
                temp_flag = True
            else:
                building_display += ", {0}".format(building)
    return building_display


def print_building_display(buildings_list):
    buildings = building_display(buildings_list)
    print("")
    print("--------- CURRENT BUILDING POOL ---------")
    print("[{0}]".format(buildings))
    print("-----------------------------------------")


def print_chosen_display(buidling_list):
    buildings = building_display(buidling_list)
    print("")
    print("--------- CHOSEN BUILDING POOL ---------")
    print("[{0}]".format(buildings))
    print("----------------------------------------")


def choose_building_pool(building_pool):
    """
    intiate choose building pool menu 

    Swah Jian Oon T01 19th December
    """
    print_building_display(building_pool)
    print("")
    first_time = True
    display_current_building = True
    building_list = ["BCH", "FAC", "HSE", "HWY", "MON", "PRK", "SHP"]
    display_list = ["Beach (BCH)", "Factory (FAC)", "House (HSE)", "Highway (HWY)",
                    "Monument (MON)", "Park (PRK)", "Shop (SHP)"]
    output_list = []
    while(True):
        temp_count = 1
        if len(output_list) <= 4:
            if first_time:
                print("Choose your new building pool below.")
                print("")
                first_time = False
            else:
                if display_current_building == True:
                    print_building_display(output_list)
                    print("")
            for display in display_list:
                print("{0}. {1}".format(temp_count, display))
                temp_count += 1
            print("")
            print("0. Exit to main menu")
            chosen = input("Enter input: ")
            try:
                chosen = int(chosen) - 1
                if 0 <= chosen <= temp_count - 2:
                    output_list.append(building_list[chosen])
                    del building_list[chosen]
                    del display_list[chosen]
                    display_current_building = True
                elif chosen == -1:
                    print("")
                    print("Configuring building pool is unsuccessful.")
                    print("Building pool remains the same as the current building pool.")
                    return None
                else:
                    print("")
                    print("Invalid input has been entered.")
                    print("Please enter number for the option (e.g. 1) and it needs to be within the range.")
                    print("")
                    display_current_building = False
            except:
                print("")
                print("Invalid input has been entered.")
                print("Please enter number for the option (e.g. 1) and it needs to be within the range.")
                print("")
                display_current_building = False
        else:
            print_chosen_display(output_list)
            return output_list
