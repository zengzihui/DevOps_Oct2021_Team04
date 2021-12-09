import sys
from unittest import mock
import pytest
from classes.menu import *
from testing_functions import *
from classes.game import Game
from classes.beach import *
from classes.factory import *
from classes.building import *
from classes.highway import *
from classes.house import *
from classes.shop import *


@pytest.mark.parametrize("testing_turn_number, expected",
                         [(2, 2), (16, 16), (3, 3), (10, 10)])
def test_print_turn_num(testing_turn_number, expected):
    """
    test if turn number is printed correctly
    """
    set_keyboard_input(None)

    # create testing game object
    test_game = Game()

    # set game turn number to testing turn number
    test_game.turn_num = testing_turn_number

    # call function to print turn number
    test_game.print_turn_num()

    # get output from print turn number
    out = get_display_output()

    # check if turn number is printed properly
    assert out[0] == "Turn {}".format(expected)


def test_print_board():
    """
    test if game board is printed correctly
    """
    set_keyboard_input(None)

    # create testing game object
    test_game = Game()
    test_game.print_board()

    # check if print_board() displays game board correctly
    out = get_display_output()
    assert out[0] == '    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+'


@pytest.mark.parametrize("option_list",
                         [(["0"])])
def test_game_menu_display(mocker, option_list):
    """
    test if game menu options are printed correctly
    """
    set_keyboard_input(None)

    # set input for menu options
    mocker.patch('builtins.input', side_effect=option_list)

    # create testing game object
    test_game = Game()

    test_game.game_menu()

    # check if game menu displays correct output
    out = get_display_output()

    assert out[0] == '1. Build a SHP\n2. Build a SHP\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu'


@pytest.mark.parametrize("option_list, expected",
                         [(["", "2"], 2), (["1"], 1), (["0"], 0), (["7", "4"], 4), (["a", "!", "0", "2"], 0)])
def test_game_menu_input(mocker, option_list, expected):
    """
    test if game menu is printed correctly and the option entered is returned
    """
    # set input for menu options
    mocker.patch('builtins.input', side_effect=option_list)

    # create testing game object
    test_game = Game()

    first_accepted_option = None

    selected = test_game.game_menu()
    for option in option_list:
        # if user chooses to exit, run the test with exit exception
        if option == "0" or option == "1" or option == "2" or option == "3" or option == "4" or option == "5":
            first_accepted_option = int(option)
            # check if selected option meets expected result
            assert int(selected) == expected
            break
    # check if first accepted option meets expected results
    assert first_accepted_option == expected


def test_start_new_turn():
    """
    test if game board, game menu and turn number will be displayed when turn starts
    """
    set_keyboard_input(["0"])

    # create testing game object
    test_game = Game()

    # check if game menu displays correct output
    test_game.start_new_turn()

    # check if output is expected
    out = get_display_output()
    assert out == ['', 'Turn 1', '    A     B     C     D  \n +-----+-----+-----+-----+\n1|     |     |     |     |\n +-----+-----+-----+-----+\n2|     |     |     |     |\n +-----+-----+-----+-----+\n3|     |     |     |     |\n +-----+-----+-----+-----+\n4|     |     |     |     |\n +-----+-----+-----+-----+',
                   '1. Build a SHP\n2. Build a SHP\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu', 'Your choice? ']


@pytest.mark.parametrize("option, expected",
                         [(["1"], True), (["2"], True), (["100", "2"], True)])
def test_start_new_turn_options(option, expected, mocker):
    """
    run start_new_turn input options
    """
    mocker.patch('classes.game.Game.add_building', return_value=True)
    test_game = Game()
    set_keyboard_input(option)
    assert test_game.start_new_turn() == expected


@pytest.mark.parametrize("building, expected",
                         [(Beach(), "BCH"), (Factory(), "FAC"), (Shop(), "SHP"), (Highway(), "HWY"), (House(), "HSE")])
def test_sub_classes(building, expected):
    """
    test if the different buildings can be initialized
    """
    assert building.name == expected


@pytest.mark.parametrize("location,x,y",
                         [("a1", 0, 0), ("a2", 0, 1)])
def test_add_building(location, x, y, mocker):
    """
    success cases for adding_building function
    """
    mocker.patch('classes.game.Game.start_new_turn', return_value=True)
    test_shop = "SHP"
    test_game = Game()
    set_keyboard_input([location])
    test_game.add_building(test_shop)
    assert isinstance(test_game.board[y][x], Shop)


@pytest.mark.parametrize("location",
                         [("a6"), ("z2")])
def test_add_building_failure_random_input(location,mocker):
    """
    failing cases for adding_building function for random input
    """
    mocker.patch('classes.game.Game.start_new_turn', return_value=True)
    test_game = Game()
    set_keyboard_input([location])
    test_game.add_building("SHP")
    output = get_display_output()
    assert output[1] == "Your input is invalid, please follow 'letter' + 'digit' format to input for location."


@pytest.mark.parametrize("location",
                         [("b1")])
def test_add_building_failure_existing_building(location,mocker):
    """
    failing cases for adding_building function for placing a building on an existing one
    """
    mocker.patch('classes.game.Game.start_new_turn', return_value=True) 
    test_game = Game()
    test_game.board[0][1] = Shop()
    set_keyboard_input([location])
    test_game.add_building("SHP")
    output = get_display_output()
    assert output[1] == "You cannot build on a location that has already had a building"


@pytest.mark.parametrize("location",
                         [("a4")])
def test_add_building_failure_adjacent_building(location,mocker):
    """
    failing cases for adding_building function for placing a building on an existing one
    """
    mocker.patch('classes.game.Game.start_new_turn', return_value=True) 
    test_game = Game()
    test_game.turn_num = 2
    test_game.board[0][1] = Shop()
    set_keyboard_input([location])
    test_game.add_building("SHP")
    output = get_display_output()
    assert output[1] == "You must build next to an existing building."


@pytest.mark.parametrize("location,expected_x,expected_y", [("a1", 0, 0), ("a5", 0, 4), ("b6", 1, 5)])
def test_input_to_coordinates(location, expected_x, expected_y):
    """
    test function to convert input to coordinates
    """
    test_game = Game()
    x, y = test_game.input_to_coordinates(location)
    assert x == expected_x
    assert y == expected_y

@pytest.mark.parametrize("test_pass, x_coord, y_coord",
                         [(True, 1, 0), (True, 0, 1), (True, 1, 2), (True, 2, 1), (False, 3, 3), (False, 0, 3)])
def test_check_surrounding_buildings_exist(test_pass,x_coord, y_coord):
    """
    test if surroundings buildings exist function works
    """
    test_game = Game()
    test_game.board[1][1] = Shop()
    assert test_game.check_surrounding_buildings_exist(x_coord, y_coord) == test_pass

@pytest.mark.parametrize("test_pass, x_coord, y_coord",
                         [(True, 1, 0), (False, 0, 1)])
def test_check_building_exist(test_pass,x_coord,y_coord):
    """
    test if check building exist
    """
    test_game = Game()
    test_game.board[0][1] = Shop()
    
    assert test_game.check_building_exist(x_coord,y_coord) == test_pass 

@pytest.mark.parametrize("building_name",
                         [("FAC"),("SHP"),("BCH"),("HWY"),("HSE")])
def test_remove_building(building_name):
    """
    test if building can be removed from the building pool
    """
    test_game = Game()
    test_game.remove_building(building_name)
    assert test_game[building_name] == 7

def test_display_buildings(building_name):
    """
    test if display buildings pool works
    """
    test_game = Game()
    for key in test_game.building_pool:
        output = "Building         Remaining\n--------         ---------\n" + key + "              " + test_game.building_pool[key] + "\n"
    assert test_game.display_buildings() == output