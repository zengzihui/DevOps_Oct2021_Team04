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
    assert out[0] == 'Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n\n0. Exit'


@pytest.mark.parametrize("option_list",
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
    assert out[0] == '\n1. Start new game\n2. Load saved game\n\n0. Exit'


@pytest.mark.parametrize("option_list, expected",
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


@pytest.mark.parametrize("option_list, expected",
                         [(["", "2"], 2), (["a", "1"], 1), (["!", "0"], 0), (["7", "4", "2", "0"], 2), (["a", "!", "0", "2"], 0)])
def test_main_menu_input_invalid_inputs(mocker, option_list, expected):
    """
    test if main menu accepts another input after invalid input is entered
    test if accepted option is returned from main_menu()

    Zheng Jiongjie T01 9th December
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

    Zheng Jiongjie T01 9th December
    """
    mocker.patch('classes.game.Game.start_new_turn', return_value="new turn started")
    assert start_new_game() == "new turn started"


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
                         [
                             (["4", "1"], "--------- CURRENT BUILDING POOL ---------\n[BCH]"),
                             (["4", "2"], "--------- CURRENT BUILDING POOL ---------\n[FAC]"),
                             (["4", "3"], "--------- CURRENT BUILDING POOL ---------\n[HSE]"),
                             (["4", "4"], "--------- CURRENT BUILDING POOL ---------\n[HWY]"),
                             (["4", "5"], "--------- CURRENT BUILDING POOL ---------\n[MON]"),
                             (["4", "6"], "--------- CURRENT BUILDING POOL ---------\n[PRK]"),
                             (["4", "7"], "--------- CURRENT BUILDING POOL ---------\n[SHP]"),
                             (["4", "1", "2", "3", "4", "5", "6", "7"], 
                             "--------- CURRENT BUILDING POOL ---------\n[BCH, FAC, HSE, HWY, MON, PRK, SHP]"),
                         ])
def test_choose_building_pool(option_list,expected):
    """
    test choose building pool allows user to choose building pool

    Swah Jian Oon T01 19th January
    """
    choose_building_pool()
    set_keyboard_input(option_list)
    out = get_display_output()
    assert out[-1] == expected


