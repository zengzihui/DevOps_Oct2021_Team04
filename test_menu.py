import sys
from unittest import mock
import pytest
from classes.menu import *
from testing_functions import *


@pytest.mark.parametrize("option_list",
                         [(["0"])])
def test_main_menu_display(mocker, option_list):
    """
    test if main menu options are printed correctly
    """
    set_keyboard_input([None, None])

    # set input for menu options
    mocker.patch('builtins.input', side_effect=option_list)

    # run main menu function
    main_menu()

    # check if main_menu function displays correct output
    out = get_display_output()
    assert out[0] == 'Welcome, mayor of Simp City!        \n----------------------------\n1. Start new game\n2. Load saved game\n0. Exit\n'


@pytest.mark.parametrize("option_list, expected",
                         [(["2"], "2"), (["1"], "1"), (["0"], "0")])
def test_main_menu_input_success(mocker, option_list, expected):
    """
    test if main_menu() returns the value entered by user
    """
    # set input for menu options
    mocker.patch('builtins.input', side_effect=option_list)

    # gets value returned from main_menu()
    selected = main_menu()

    # checks if input to main menu is returned back to function call
    assert selected == expected


@pytest.mark.parametrize("option_list, expected",
                         [(["", "2"], 2), (["a", "1"], 1), (["!", "0"], 0), (["7", "4", "2", "0"], 2), (["a", "!", "0", "2"], 0)])
def test_main_menu_input_invalid_inputs(mocker, option_list, expected):
    """
    test if main menu accepts another input after invalid input is entered
    test if accepted option is returned from main_menu()
    """
    # set input for menu options
    mocker.patch('builtins.input', side_effect=option_list)

    first_accepted_option = None

    selected = main_menu()
    for option in option_list:
        # if user chooses to exit, run the test with exit exception
        if option == "0" or option == "1" or option == "2":
            first_accepted_option = int(option)
            assert int(selected) == expected
            break
    assert first_accepted_option == expected


def test_start_new_game(mocker):
    """
    test if Game.start_new_turn() is called when start_new_game() is called
    """
    mocker.patch('classes.game.Game.start_new_turn', return_value="new turn started")
    assert start_new_game() == "new turn started"

def test_main_menu_exit_program():
    """
    test if program closes when exit() function is called
    """
    with pytest.raises(SystemExit) as e:
        exit_game()
    assert e.type == SystemExit
    assert e.value.code == 1
