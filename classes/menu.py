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

    options = {"1": "Start new game", "2": "Load saved game", "3": "Show high scores", "4": "Choose building pool", "5": "Choose city size", "": "", "0": "Exit"}

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


def start_new_game(building_pool):
    """
    intializes new game object and start the turn

    Zheng Jiongjie T01 9th December
    """
    current_game = Game(building_pool=building_pool)
    return current_game.start_new_turn()


def exit_game():
    """
    exits program

    Zheng Jiongjie T01 9th December
    """
    exit(1)

def building_display(buildings_list):
    """
    return chosen buildings displayed string

    Swah Jian Oon T01 19th December
    """
    temp_flag = False
    building_display = ""
    if len(buildings_list) != 0:
        for building in buildings_list:
            if temp_flag== False:
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
    building_list = ["BCH","FAC","HSE","HWY","MON","PRK","SHP"]
    display_list = ["Beach (BCH)","Factory (FAC)","House (HSE)","Highway (HWY)", "Monument (MON)","Park (PRK)","Shop (SHP)"]
    output_list ={}
    while(True):
        temp_count =1
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
                temp_count +=1
            print("")
            print("0. Exit to main menu")
            chosen = input("Enter input: ")
            try:
                chosen = int(chosen)-1
                if 0 <= chosen <= temp_count-2 :
                    output_list[building_list[chosen]] = 8
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
            