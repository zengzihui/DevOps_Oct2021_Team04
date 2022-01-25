import sys
from unittest import mock
import pytest
from classes.menu import *
from testing_functions import *
import json
from classes.game import Game
from classes.beach import *
from classes.factory import *
from classes.building import *
from classes.highway import *
from classes.house import *
from classes.shop import *


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


def test_load_game_success():
    """
    check if loaded game matches the game save file

    Zheng Jiongjie T01 25th January
    """

    # saves dummy save file
    with open("game_save.json", "w+") as save_file:
        dummy_data = {"board": {"0,0": "SHP", "1,0": "SHP", "2,0": "HSE", "3,0": "FAC",
                                "0,1": "BCH", "1,1": "HSE", "2,1": "HSE", "3,1": "BCH",
                                "0,2": "BCH", "1,2": "SHP", "2,2": "HSE", "3,2": "HSE",
                                "0,3": "HWY", "1,3": "HWY", "2,3": "HWY", "3,3": "HWY"},
                      "turn_num": 1, "width": 3, "height": 3,
                      "randomized_history": {},
                      "building_pool": {"HSE": 0, "FAC": 0, "SHP": 0, "HWY": 0, "BCH": 0}}
        json.dump(dummy_data, save_file)

    loaded_game = load_game()

    # check if all game data is loaded correctly
    assert type(loaded_game.board[0][0]) is Shop
    assert type(loaded_game.board[0][1]) is Shop
    assert type(loaded_game.board[0][2]) is House
    assert type(loaded_game.board[0][3]) is Factory
    assert type(loaded_game.board[1][0]) is Beach
    assert type(loaded_game.board[1][1]) is House
    assert type(loaded_game.board[1][2]) is House
    assert type(loaded_game.board[1][3]) is Beach
    assert type(loaded_game.board[2][0]) is Beach
    assert type(loaded_game.board[2][1]) is Shop
    assert type(loaded_game.board[2][2]) is House
    assert type(loaded_game.board[2][3]) is House
    assert type(loaded_game.board[3][0]) is Highway
    assert type(loaded_game.board[3][1]) is Highway
    assert type(loaded_game.board[3][2]) is Highway
    assert type(loaded_game.board[3][3]) is Highway
    assert loaded_game.height == 3
    assert loaded_game.width == 3
    assert loaded_game.turn_num == 1
    assert loaded_game.building_pool == {"HSE": 0, "FAC": 0, "SHP": 0, "HWY": 0, "BCH": 0}
    assert loaded_game.randomized_building_history == {}


def test_load_game_fail():
    """
    check if game loads on corrupted save file

    Zheng Jiongjie T01 25th January
    """

    # saves wrong save file (randomized_history is randoized_history)
    with open("game_save.json", "w+") as save_file:
        dummy_data = {"board": {"0,0": "SHP", "1,0": "SHP", "2,0": "HSE", "3,0": "FAC",
                                "0,1": "BCH", "1,1": "HSE", "2,1": "HSE", "3,1": "BCH",
                                "0,2": "BCH", "1,2": "SHP", "2,2": "HSE", "3,2": "HSE",
                                "0,3": "HWY", "1,3": "HWY", "2,3": "HWY", "3,3": "HWY"},
                      "turn_num": 1, "width": 3, "height": 3,
                      "randoized_history": {},
                      "building_pool": {"HSE": 0, "FAC": 0, "SHP": 0, "HWY": 0, "BCH": 0}}
        json.dump(dummy_data, save_file)

    loaded_game = load_game()

    assert loaded_game is False
