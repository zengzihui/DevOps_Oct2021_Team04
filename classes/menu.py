import json
from .game import Game
from .building import Building
from .shop import Shop
from .factory import Factory
from .highway import Highway
from .house import House
from .beach import Beach


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
    """
    intializes new game object and start the turn

    Zheng Jiongjie T01 9th December
    """
    current_game = Game()
    return current_game.start_new_turn()


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
    with open("game_save.json", "r") as save_file:
        save_data = json.load(save_file)
        try:
            loaded_game.building_pool = save_data["building_pool"]
            loaded_game.turn_num = save_data["turn_num"]
            loaded_game.width = save_data["width"]
            loaded_game.height = save_data["height"]
            loaded_game.randomized_building_history = save_data["randomized_history"]

            loaded_game.board = []
            for row in range(0, loaded_game.height + 1):
                loaded_game.board.append([])
                for col in range(0, loaded_game.width + 1):
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
                    else:
                        loaded_game.board[row].append(Building())
            return loaded_game
        except Exception as e:
            print("Failed to load game")
            return False
