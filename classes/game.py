from random import randrange
import os

from classes.monument import Monument
from classes.park import Park

from .building import Building
from .shop import Shop
from .factory import Factory
from .highway import Highway
from .house import House
from .beach import Beach
from .json import *


class Game:

    def __init__(self, height=4, width=4, building_pool={}):
        """
        init function for game class
        default turn number is 1

        Zheng Jiongjie T01 9th December
        """
        self.building_pool = building_pool
        self.height = height
        self.width = width
        self.board = []
        self.turn_num = 1
        self.randomized_building_history = {}
        self.game_ended = False

        for row in range(0, self.height):
            self.board.append([])
            for col in range(0, self.width):
                self.board[row].append(Building())

    def print_turn_num(self):
        """
        prints turn number based on self.turn_num in game class

        Zheng Jiongjie T01 9th December
        """
        print("Turn {}".format(self.turn_num))

    def print_board(self, final_turn=False):
        """
        Print the map board with the building names
        Also print remaining buildings on the right of the game board

        Zheng Jiongjie T01 19th January
        """
        remaining_building_string_list = []
        if not final_turn:
            remaining_building_string_list = self.generate_remaining_building_string()

        column_names = "  "
        # add column names for map column
        for header in range(0, self.width):
            column_names += '   {:1s}  '.format(chr(header + 65))

        # add column names for remaning building section
        if remaining_building_string_list:
            column_names += "{:9}{}".format("",
                                            remaining_building_string_list.pop(0))

        print(column_names)

        row_seperation_string = "  +"
        for i in range(0, self.width):
            row_seperation_string += "-----+"

        for i in range(0, self.height):
            if remaining_building_string_list:
                print("{}{:8}{}".format(row_seperation_string,
                      "", remaining_building_string_list.pop(0)))
            else:
                print(row_seperation_string)
            row_string = "{:>2}".format(i + 1)
            for building in self.board[i]:
                row_string += "|"
                row_string += " {:3} ".format(building.name)
            row_string += "|"

            if remaining_building_string_list:
                row_string += "{:8}{}".format("",
                                              remaining_building_string_list.pop(0))

            print(row_string)
        if remaining_building_string_list:
            print("{}{:8}{}".format(row_seperation_string,
                  "", remaining_building_string_list.pop(0)))
        else:
            print(row_seperation_string)
        while(len(remaining_building_string_list) != 0):
            remaining_buildings_string = "{}{:8}{}".format(len(row_seperation_string)
                                                           * " ", "", remaining_building_string_list.pop(0))
            print(remaining_buildings_string)

    def generate_remaining_building_string(self):
        """
        generate the list of strings to print out for the remaining buildings

        Zheng Jiongjie T01 26th January
        """
        remaining_building_string = []
        remaining_building_string.append("Building   Remaining")
        remaining_building_string.append("--------------------")
        for key in self.building_pool:
            remaining_building_string.append(
                "{:9s}| {}".format(key, self.building_pool[key]))
        return remaining_building_string

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

        for key in options:
            if key != "":
                print("{}. {}".format(key, options[key]))
            else:
                print("")
        chosen_option = input("Your choice? ")

        while chosen_option not in options.keys() or chosen_option == "":
            print(
                "Invalid Input. Please enter a valid input (\"1\" / \"2\" / \"3\" / \"4\" / \"5\" / \"0\").")
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
        randomized_building_names = self.randomized_building_history[str(
            self.turn_num)]

        # check if game board is fully filled and end game if it is
        if self.turn_num > self.height * self.width and self.game_ended is False:
            self.game_ended = True
            self.end_of_game()
            self.update_high_score()

        # return back to main menu if game ends
        if self.game_ended:
            # break recursive start_new_turn
            return 0

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
            print("")
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
        self.randomized_building_history[str(self.turn_num)] = [
            random_building_one_name, random_building_two_name]

    def add_building(self, building_string):
        """
        Add building object to the board based on user input

        Swah Jianoon T01 9th December
        """
        building = Building()

        location_string = input("Build where? ")
        coords = self.input_to_coordinates(location_string)
        if coords is not None:
            x_coord, y_coord = coords
            if 0 <= x_coord < self.width and 0 <= y_coord < self.height:
                if self.check_building_exist(x_coord, y_coord):
                    print(
                        "You cannot build on a location that has already had a building")
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
                        elif building_string == "MON":
                            building = Monument(x_coord, y_coord)
                        elif building_string == "PRK":
                            building = Park(x_coord, y_coord)
                        self.board[y_coord][x_coord] = building
                        self.remove_building(building_string)
                        building.x_coord = x_coord
                        building.y_coord = y_coord
                        self.turn_num += 1
                    else:
                        print("You must build next to an existing building.")

            else:
                print(
                    "Your input is invalid, please follow 'letter' + 'digit' format to input for location.")
        else:
            print(
                "Your input is invalid, please follow 'letter' + 'digit' format to input for location.")
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
        if (0 <= temp_x_lower < self.width) and self.board[y_coord][temp_x_lower].name != "":
            return True
        elif (0 <= temp_x_higher < self.width) and self.board[y_coord][temp_x_higher].name != "":
            return True
        elif (0 <= temp_y_lower < self.height) and self.board[temp_y_lower][x_coord].name != "":
            return True
        elif (0 <= temp_y_higher < self.height) and self.board[temp_y_higher][x_coord].name != "":
            return True
        return False

    def display_building(self):
        """
        Display all buildings left in the building pool

        Swah Jianoon T01 9th December
        """
        spaces = " "
        output = "Building{0}Remaining\n--------{0}--------\n".format(
            spaces * 9, spaces * 9)
        for key in self.building_pool:
            output += "{0}{1}{2}\n".format(key,
                                           spaces * 14, self.building_pool[key])
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
        total_dict = {"": 0}
        display_dict = {"": ""}
        total_score = 0
        for key in self.building_pool:
            total_dict[key] = 0
            display_dict[key] = ""

        for h in range(0, self.height):
            for w in range(0, self.width):
                if self.board[h][w].name != "":
                    score = self.board[h][w].calculate_score(self)
                    total_score += score
                    total_dict[self.board[h][w].name] += int(score)
                    if display_dict[self.board[h][w].name] != "":
                        display_dict[self.board[h]
                                     [w].name] += " + {0}".format(str(score))
                    else:
                        display_dict[self.board[h][w].name] = str(score)

        for building in display_dict:
            if building != "":
                if total_dict[building] == 0:
                    print("{0}: 0".format(building))
                else:
                    print("{0}: {1} = {2}".format(
                        building, display_dict[building], str(total_dict[building])))
        print("Total score: {0}".format(total_score))
        self.start_new_turn()

    def calculate_total_score(self):
        """
        Calculate total score at any stage

        Swah Jianoon T01 27th January
        """
        total_score = 0
        for h in range(0, self.height):
            for w in range(0, self.width):
                if self.board[h][w].name != "":
                    score = self.board[h][w].calculate_score(self)
                    total_score += score
        return total_score

    def update_high_score(self):
        """
        Update high score with user's score

        Swah Jianoon T01 27th January
        """
        try:
            filename = "high_score_{0}.json".format((self.width)*(self.height))
            file_path = os.path.join(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))), filename)
            save_data = load_json(file_path)
            save_data["board_size"] = (self.width)*(self.height)
            high_score_list = save_data["high_scores"]
            position = 0
            total_score = self.calculate_total_score()
            if len(high_score_list) != 0:
                for high_score in high_score_list:
                    if not(total_score > high_score["score"]):
                        position += 1
            if position <= 9:
                print("Congratulations! You made the high score board at position {0}!".format(
                    position+1))
            while position <= 9:
                name = input("Please enter your name (max 20 chars): ")
                if len(name) > 20:
                    print("")
                    print("Invalid input for the name has been entered.")
                    print(
                        "Please remember only a max of 20 characters are allowed for the name.")
                    print("")
                else:
                    user_data = {'name': name, 'score': total_score}
                    high_score_list.insert(position, user_data)
                    save_data["high_scores"] = high_score_list
                    if len(save_data["high_scores"]) > 10:
                        save_data["high_scores"].pop()
                    update_json(file_path, save_data)
                    self.display_high_score()
                    return
                    
        except:
            filename = "high_score_{0}.json".format((self.width)*(self.height))
            file_path = os.path.join(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))), filename)
            print("")
            print(
                "The current high score file is corrupt and a new high score list will be generated.")
            print("")
            update_json(file_path, {'board_size': 0, 'high_scores': []})
            self.update_high_score()
            

        

    def display_high_score(self):
        """
        Display high score

        Swah Jianoon T01 27th January
        """
        try:
            filename = "high_score_{0}.json".format((self.width)*(self.height))
            file_path = os.path.join(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))), filename)
            save_data = load_json(file_path)
            high_score_list = save_data["high_scores"]
            print("")
            print("--------- HIGH SCORES ---------")
            print("Pos Player                Score")
            print("--- ------                -----")
            count = 1
            for high_score in high_score_list:
                print("{0:2d}. {1:<21} {2:5d}".format(int(count),
                    high_score["name"], int(high_score["score"])))
                count += 1
            print("-------------------------------")
        except:
            filename = "high_score_{0}.json".format((self.width)*(self.height))
            file_path = os.path.join(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))), filename)
            print("")
            print("The current file is corrupt and will therefore be deleted.")
            update_json(file_path, {'board_size': 0, 'high_scores': []})
            self.display_high_score()

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
                        save_data["board"][str(
                            building.x_coord) + "," + str(building.y_coord)] = building.name
            # save the game
            json.dump(save_data, save_file)

        print("")
        print("Game saved!")
        self.start_new_turn()

    def end_of_game(self):
        """
        Displays final game board and score

        Zheng Jiongjie T02 20th January
        """
        print("")
        print("Final layout of Simp City:")
        self.print_board(final_turn=True)
        self.display_all_scores()
