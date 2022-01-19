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

    Zheng Jiongjie T01 9th December
    """
    set_keyboard_input([None, None])

    # set input for menu options
    mocker.patch('builtins.input', side_effect=option_list)

    # run main menu function
    main_menu()

    # check if main_menu function displays correct output
    out = get_display_output()
    assert (out[0] == 'Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n3. Show high scores\n\
4. Choose building pool\n5. Choose city size\n\n0. Exit')


@ pytest.mark.parametrize("option_list",
                          [(["0"])])
def test_main_menu_display_without_welcome(mocker, option_list):
    """
    test if main menu options are printed correctly

    Zheng Jiongjie T01 9th December
    """
    set_keyboard_input([None, None])

    # set input for menu options
    mocker.patch('builtins.input', side_effect=option_list)

    # run main menu function
    main_menu(True)

    # check if main_menu function displays correct output
    out = get_display_output()
    assert (out[0] == '\n1. Start new game\n2. Load saved game\n3. Show high scores\n\
4. Choose building pool\n5. Choose city size\n\n0. Exit')


@ pytest.mark.parametrize("option_list, expected",
                          [(["2"], "2"), (["1"], "1"), (["0"], "0")])
def test_main_menu_input_success(mocker, option_list, expected):
    """
    test if main_menu() returns the value entered by user

    Zheng Jiongjie T01 9th December
    """
    # set input for menu options
    mocker.patch('builtins.input', side_effect=option_list)

    # gets value returned from main_menu()
    selected = main_menu()

    # checks if input to main menu is returned back to function call
    assert selected == expected


@ pytest.mark.parametrize("option_list, expected",
                          [(["", "2"], 2), (["a", "1"], 1), (["!", "0"], 0), (["7", "4", "2", "0"], 4), (["a", "!", "0", "2"], 0)])
def test_main_menu_input_invalid_inputs(mocker, option_list, expected):
    """
    test if main menu accepts another input after invalid input is entered
    test if accepted option is returned from main_menu()

    Zheng Jiongjie T01 9th December
    """
    # set input for menu options
    mocker.patch('builtins.input', side_effect=option_list)

    first_accepted_option = None

    menu_options = {"1": "Start new game", "2": "Load saved game", "3": "Show high scores",
                    "4": "Choose building pool", "5": "Choose city size", "": "", "0": "Exit"}

    selected = main_menu()
    for option in option_list:
        # if user chooses to exit, run the test with exit exception
        if option in menu_options:
            try:
                first_accepted_option = int(option)
            except Exception as e:
                first_accepted_option = ""
                continue
            assert int(selected) == expected
            break
    assert first_accepted_option == expected


def test_start_new_game(mocker):
    """
    test if Game.start_new_turn() is called when start_new_game() is called

    Zheng Jiongjie T01 9th December
    """
    mocker.patch('classes.game.Game.start_new_turn', return_value="new turn started")
    assert start_new_game(4, 4) == "new turn started"


def test_main_menu_exit_program():
    """
    test if program closes when exit() function is called

    Zheng Jiongjie T01 9th December
    """
    with pytest.raises(SystemExit) as e:
        exit_game()
    assert e.type == SystemExit
    assert e.value.code == 1


@pytest.mark.parametrize("option_list, expected",
                         [(["5", "5"], [5, 5]), (["5", "6"], [5, 6]), (["5", "5"], [5, 5]),
                          (["1", "40"], [1, 40]), (["2", "24", "26", "1"], [26, 1]), (["40", "26", "1"], [26, 1]),
                          (["40", "40", "6", "6"], [6, 6]), (["a", "b", "6", "6"], [6, 6]),
                          (["a", "3", "3"], [3, 3]), (["a", "3", "0"], [4, 4]), (["0"], [4, 4]),
                          (["-1", "5", "5"], [5, 5]), (["", "5", "5"], [5, 5])])
def test_choose_city_size(mocker, option_list, expected):
    """
    test if prompt_city_size() returns back valid city sizes

    Zheng Jiongjie T01 18th January
    """
    # set input for menu options
    mocker.patch('builtins.input', side_effect=option_list)

    # default city size (if user enters invalid input, this should be the city size returned)
    default_city_size = [4, 4]

    new_city_size = prompt_city_size(default_city_size)

    assert new_city_size == expected
