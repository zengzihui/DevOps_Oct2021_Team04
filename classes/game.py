from .building import Building


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
            print("Invalid Input. Please enter a valid input (\"1\" / \"2\" / \"3\" / \"4\" / \"5\" / \"0\").")
            chosen_option = input("Your choice? ")

        return chosen_option

    def start_new_turn(self):
        """
        calls functions to print_turn_num(), print_board()
        and gets input from game_menu()
        """
        print("")
        self.print_turn_num()
        self.print_board()

        # calls game menu and gets back the entered option
        chosen_option = self.game_menu()
