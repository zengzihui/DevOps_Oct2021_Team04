import sys
from unittest import mock
import pytest
from classes.menu import *
from testing_functions import *
from classes.game import Game


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

    # fix output of randomize building to only show shops
    mocker.patch('classes.game.Game.randomize_buildings', return_value=["SHP", "SHP"])

    test_game.game_menu(test_game.randomize_buildings())

    # check if game menu displays correct output
    out = get_display_output()

    assert out[0] == '1. Build a SHP\n2. Build a SHP\n3. See remaining buildings\n4. See current score\n\n5. Save game\n0. Exit to main menu\n'


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

    # fix output of randomize building to only show shops
    mocker.patch('classes.game.Game.randomize_buildings', return_value=["SHP", "SHP"])

    first_accepted_option = None

    selected = test_game.game_menu(test_game.randomize_buildings())
    for option in option_list:
        # if user chooses to exit, run the test with exit exception
        if option == "0" or option == "1" or option == "2" or option == "3" or option == "4" or option == "5":
            first_accepted_option = int(option)
            # check if selected option meets expected result
            assert int(selected) == expected
            break
    # check if first accepted option meets expected results
    assert first_accepted_option == expected
