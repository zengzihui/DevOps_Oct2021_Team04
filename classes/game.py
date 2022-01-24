from random import randrange
import json

from .building import Building
from .shop import Shop
from .factory import Factory
from .highway import Highway
from .house import House
from .beach import Beach


class Game:

    def __init__(self, height=3, width=3):
        """
        init function for game class
        default turn number is 1

        Zheng Jiongjie T01 9th December
        """

        self.building_pool = {"HSE": 8, "FAC": 8, "SHP": 8, "HWY": 8, "BCH": 8}
        self.height = height
        self.width = width
        self.board = []
        self.turn_num = 1
        self.randomized_building_history = {}

        width_counter = 0
        while (width_counter <= width):
            height_counter = 0
            self.board.append([])

            while (height_counter <= height):
                self.board[width_counter].append(Building())
                height_counter += 1

            width_counter += 1

    def print_turn_num(self):
        """
        prints turn number based on self.turn_num in game class

        Zheng Jiongjie T01 9th December
        """
        print("Turn {}".format(self.turn_num))

    def print_board(self):
        """
        Print the map board with the building names

        Zheng Jiongjie T01 9th December
        """
        game_board_string = " "
        row_count = 0
        for header in range(0, self.width + 1):
            game_board_string += '   {:1s}  '.format(chr(header + 65))
        game_board_string += "\n"
        for row in self.board:
            game_board_string += "{:26s}".format(" +-----+-----+-----+-----+") + "\n"
            game_board_string += str(row_count + 1)
            for building in row:
                building_short = ""
                if building:
                    building_short = building.name
                game_board_string += '|'
                game_board_string += ' {:3s} '.format(building_short)
            game_board_string += "|\n"
            row_count += 1
        game_board_string += "{:26s}".format(" +-----+-----+-----+-----+")
        print(game_board_string)

    def game_menu(self, randomized_building_name=["SHP", "SHP"]):
        """
        Print game menu

        eg.
        1. Build a HSE
        2. Build a BCH
        3. See remaining buildings
        4. See current score

        5. Save game
        0. Exit to main menu

        where HSE and BCH are randomized

        "randomized_building_name" in method signature will be generated from randomize_buildings() function which will be implemented
        at a later date.

        Zheng Jiongjie T01 9th December
        """
        options = {"1": "Build a {}".format(randomized_building_name[0]), "2": "Build a {}"
                   .format(randomized_building_name[1]), "3": "See remaining buildings",
                   "4": "See current score", "": "", "5": "Save game",
                   "0": "Exit to main menu"}

        game_menu_string = ""
        for key in options:
            if key != "":
                game_menu_string += "{}. {}".format(key, options[key]) + "\n"
            else:
                game_menu_string += "\n"
        game_menu_string = game_menu_string.rstrip()
        print(game_menu_string)
        chosen_option = input("Your choice? ")

        while chosen_option not in options.keys() or chosen_option == "":
            print("Invalid Input. Please enter a valid input (\"1\" / \"2\" / \"3\" / \"4\" / \"5\" / \"0\").")
            chosen_option = input("Your choice? ")

        return chosen_option

    def start_new_turn(self):
        """
        calls functions to print_turn_num(), print_board()
        and gets input from game_menu()

        "randomized_building_name" list will be replaced with a function to randomized the different buildings in the future. For now we will use only SHP

        Zheng Jiongjie T01 9th December
        """

        # generate random buildings for turn if buildings for the turn has yet to be generated
        if str(self.turn_num) not in self.randomized_building_history:
            self.get_two_buildings_from_pool(self.building_pool)
        # retrieve 2 random genrated buildings from randomized building history
        randomized_building_names = self.randomized_building_history[str(self.turn_num)]

        print("")
        self.print_turn_num()
        self.print_board()

        # calls game menu and gets back the entered option
        chosen_option = self.game_menu(randomized_building_names)
        if chosen_option == "1":
            return self.add_building(randomized_building_names[0])
        elif chosen_option == "2":
            return self.add_building(randomized_building_names[1])
        elif chosen_option == "3":
            return self.display_building()
        elif chosen_option == "4":
            return self.display_all_scores()
        elif chosen_option == "5":
            return self.save_game()
        elif chosen_option == "0":
            return 0

    def get_two_buildings_from_pool(self, building_pool):
        """
        Get 2 random building names from pool of buildings

        Zheng Jiongjie T01 16th January
        """
        # create temporary list to store all buildings
        temp_building_list = []

        # populate list with the number of buildings left in the pool
        for building_type in building_pool:
            for i in range(0, building_pool[building_type]):
                temp_building_list.append(building_type)

        try:
            # generate a random index for building 1
            random_building_one_index = randrange(len(temp_building_list))
            # get randomized building 1's string
            random_building_one_name = temp_building_list[random_building_one_index]
            # remove the first randomized building from temporary pool
            temp_building_list.pop(random_building_one_index)
        except Exception as ex:
            # if no more buildings
            random_building_one_name = ""

        try:
            # generate a random index for building 2
            random_building_two_index = randrange(len(temp_building_list))
            # get randomized building 2's string
            random_building_two_name = temp_building_list[random_building_two_index]
        except Exception as ex:
            # if only 1 building left
            random_building_two_name = random_building_one_name

        # updates randomized building history with the list of 2 randomized buildings
        self.randomized_building_history[str(self.turn_num)] = [random_building_one_name, random_building_two_name]

    def add_building(self, building_string):
        """
        Add building object to the board based on user input

        Swah Jianoon T01 9th December
        """
        building = Building()

        location_string = input("Build where? ")
        coords = self.input_to_coordinates(location_string)
        if coords != None:
            x_coord, y_coord = coords
            if 0 <= x_coord < 4 and 0 <= y_coord < 4:
                if self.check_building_exist(x_coord, y_coord):
                    print("You cannot build on a location that has already had a building")
                else:
                    if self.check_surrounding_buildings_exist(x_coord, y_coord) or self.turn_num == 1:
                        if building_string == "SHP":
                            building = Shop(x_coord, y_coord)
                        elif building_string == "HSE":
                            building = House(x_coord, y_coord)
                        elif building_string == "FAC":
                            building = Factory(x_coord, y_coord)
                        elif building_string == "HWY":
                            building = Highway(x_coord, y_coord)
                        elif building_string == "BCH":
                            building = Beach(x_coord, y_coord)
                        self.board[y_coord][x_coord] = building
                        self.remove_building(building_string)
                        building.x_coord = x_coord
                        building.y_coord = y_coord
                        self.turn_num += 1
                    else:
                        print("You must build next to an existing building.")

            else:
                print("Your input is invalid, please follow 'letter' + 'digit' format to input for location.")
        else:
            print("Your input is invalid, please follow 'letter' + 'digit' format to input for location.")
        self.start_new_turn()

    def input_to_coordinates(self, location_string):
        """
        Converts user input location into coordinates

        Swah Jianoon T01 9th December
        """
        ASCII_string_value = 97
        ASCII_int_value = 49
        if len(location_string) >= 2:
            x = ord(location_string[0]) - ASCII_string_value
            y = ord(location_string[1]) - ASCII_int_value
            return (x, y)
        return None

    def check_building_exist(self, x_coord, y_coord):
        """
        check if building exists at the coordinate

        Swah Jianoon T01 9th December
        """
        if self.board[y_coord][x_coord].name == "":
            return False
        else:
            return True

    def check_surrounding_buildings_exist(self, x_coord, y_coord):
        """
        check if there are adjacent buildings

        Swah Jianoon T01 9th December
        """
        temp_x_lower = x_coord - 1
        temp_x_higher = x_coord + 1
        temp_y_lower = y_coord - 1
        temp_y_higher = y_coord + 1
        if (0 <= temp_x_lower < 4) and self.board[y_coord][temp_x_lower].name != "":
            return True
        elif (0 <= temp_x_higher < 4) and self.board[y_coord][temp_x_higher].name != "":
            return True
        elif (0 <= temp_y_lower < 4) and self.board[temp_y_lower][x_coord].name != "":
            return True
        elif (0 <= temp_y_higher < 4) and self.board[temp_y_higher][x_coord].name != "":
            return True
        return False

    def display_building(self):
        """
        Display all buildings left in the building pool

        Swah Jianoon T01 9th December
        """
        spaces = " "
        output = "Building{0}Remaining\n--------{0}--------\n".format(spaces * 9, spaces * 9)
        for key in self.building_pool:
            output += "{0}{1}{2}\n".format(key, spaces * 14, self.building_pool[key])
        print(output)
        self.start_new_turn()

    def remove_building(self, building_name):
        """
        Remove a building from the building pool

        Swah Jianoon T01 9th December
        """
        self.building_pool[building_name] -= 1

    def display_all_scores(self):
        """
        Display the current score of the game

        Eg .

        HSE: 1 + 5 + 5 + 3 + 3 = 17
        FAC: 1 = 1
        SHP: 2 + 2 + 3 = 7
        HWY: 4 + 4 + 4 + 4 = 16
        BCH: 3 + 3 + 3 = 9
        Total score: 50

        Swah Jianoon T01 17th Janunary
        """
        print("")
        total_dict = {"": 0}
        display_dict = {"": ""}
        total_score = 0
        for key in self.building_pool:
            total_dict[key] = 0
            display_dict[key] = ""

        for h in range(0, self.height + 1):
            for w in range(0, self.width + 1):
                if self.board[h][w].name != "":
                    score = self.board[h][w].calculate_score(self)
                    total_score += score
                    total_dict[self.board[h][w].name] += int(score)
                    if display_dict[self.board[h][w].name] != "":
                        display_dict[self.board[h][w].name] += " + {0}".format(str(score))
                    else:
                        display_dict[self.board[h][w].name] = str(score)

        for building in display_dict:
            if building != "":
                if total_dict[building] == 0:
                    print("{0}: 0".format(building))
                else:
                    print("{0}: {1} = {2}".format(building, display_dict[building], str(total_dict[building])))
        print("Total score: {0}".format(total_score))
        self.start_new_turn()

    def save_game(self):
        """
        save game details to json file

        Zheng Jiongjie T01 21st January
        """
        with open("game_save.json", "w+") as save_file:
            # generate save file based on current game
            save_data = {"board": {}, "turn_num": self.turn_num, "width": self.width,
                         "height": self.height, "randomized_history": self.randomized_building_history,
                         "building_pool": self.building_pool}
            # add buildings in current game to save file
            for row in self.board:
                for building in row:
                    if building.x_coord is not None and building.y_coord is not None:
                        save_data["board"][str(building.x_coord) + "," + str(building.y_coord)] = building.name
            # save the game
            json.dump(save_data, save_file)

        print("")
        print("Game saved!")
        self.start_new_turn()
