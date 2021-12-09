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
        """
        self.height = height
        self.width = width
        self.board = []
        self.turn_num = 1

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
        """
        print("Turn {}".format(self.turn_num))

    def print_board(self):
        """
        Print the map board with the building names
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
            print("Invalid input, please try again")
            chosen_option = input("Your choice? ")

        return chosen_option

    def start_new_turn(self):
        """
        calls functions to print_turn_num(), print_board()
        and gets input from game_menu()

        "randomized_building_name" list will be replaced with a function to randomized the different buildings in the future. For now we will use only SHP
        """
        randomized_building_name=["SHP", "SHP"]
        print("")
        self.print_turn_num()
        self.print_board()

        # calls game menu and gets back the entered option
        chosen_option = self.game_menu()
        if chosen_option == "1":
            return self.add_building(randomized_building_name[0])
        elif chosen_option =="2":
            return self.add_building(randomized_building_name[1])

    def add_building(self, building_string):
        """
        Add building object to the board based on user input
        """
        building = Building()
        if building_string == "SHP":
            building = Shop()

        location_string = input("Build where? ")
        x_coord, y_coord = self.input_to_coordinates(location_string)
        self.board[y_coord][x_coord] = building
        building.x_coord = x_coord
        building.y_coord = y_coord
        self.start_new_turn()
    def input_to_coordinates(self,location_string):
        """
        Converts user input location into coordinates
        """
        ASCII_string_value = 97
        ASCII_int_value = 49
        x = ord(location_string[0]) - ASCII_string_value
        y = ord(location_string[1]) - ASCII_int_value

        return x, y