import sys
from unittest import mock
import pytest
from classes.menu import *
from test.testing_functions import *


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
    assert out[0] == 'Welcome, mayor of Simp City!\n----------------------------\n1. Start new game\n2. Load saved game\n4. Choose building pool\n\n0. Exit'


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
    assert out[0] == '\n1. Start new game\n2. Load saved game\n4. Choose building pool\n\n0. Exit'


@pytest.mark.parametrize("option_list, expected",
                         [(["2"], "2"), (["1"], "1"), (["0"], "0"),(["4"], "4")])
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
                         [(["", "2"], 2), (["a", "1"], 1), (["!", "0"], 0), (["7", "2", "0"], 2), (["a", "!", "0", "2"], 0)])
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
    building_pool = {"HSE":8, "FAC":8, "SHP": 8, "HWY":8, "BCH":8}
    assert start_new_game(building_pool) == "new turn started"


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
                             (["1", "1", "1", "1", "1"], {"BCH":8, "FAC":8, "HSE": 8, "HWY":8, "MON":8}),
                             
                         ])
def test_success_choose_building_pool(option_list,expected):
    """
    test choose building pool allows user to choose building pool

    Swah Jian Oon T01 19th January
    """
    set_keyboard_input(option_list)
    output_list =choose_building_pool()
    assert output_list == expected

@pytest.mark.parametrize("option_list, expected",
                         [
                             (["z","0"], "\nInvalid input has been entered.\nPlease enter integer for the option (e.g. 1) and it needs to be withing the range."),
                             (["z41231","0"], "\nInvalid input has been entered.\nPlease enter integer for the option (e.g. 1) and it needs to be withing the range."),
                             (["12","0"], "\nInvalid input has been entered.\nPlease enter integer for the option (e.g. 1) and it needs to be withing the range."),
                             
                         ])
def test_failure_choose_building_pool(option_list,expected):
    """
    test choose building pool display error message 

    Swah Jian Oon T01 19th January
    """
    set_keyboard_input(option_list)
    choose_building_pool()
    out = get_display_output()
    result = "\n" + out[18] + "\n" + out[19]
    assert result == expected

@pytest.mark.parametrize("option_list, expected",
                         [
                             (["0"], '''Configuring building pool is unsuccessful.
Building pool remains the same as the current building pool.'''),
                             
                         ])
def test_exit_choose_building_pool(option_list,expected):
    """
    test choose building pool allows user to print message before return to main menu

    Swah Jian Oon T01 19th January
    """
    set_keyboard_input(option_list)
    output_value =choose_building_pool()
    out = get_display_output()
    result = out[-2] + "\n" + out[-1]
    assert result == expected and output_value ==None

@pytest.mark.parametrize("building_list, expected",
                         [
                             (["BCH","FAC","HSE","HWY","MON"],'''
--------- CURRENT BUILDING POOL ---------
[BCH, FAC, HSE, HWY, MON]
-----------------------------------------''')
                             
                         ])
def test_print_building_display(building_list,expected):
    """
    test choose display current building pool

    Swah Jian Oon T01 19th January
    """
    combined_output =""
    set_keyboard_input(None)
    print_building_display(building_list)
    out = get_display_output()
    for result in out:
        combined_output+=result
        if result != out[-1]:
            combined_output += "\n"
    assert combined_output == expected

@pytest.mark.parametrize("option_list, expected",
                         [
                             (["0"], '''
--------- CURRENT BUILDING POOL ---------
[]
-----------------------------------------

Choose your new building pool below.

1.Beach (BCH)
2.Factory (FAC)
3.House (HSE)
4.Highway (HWY)
5.Monument (MON)
6.Park (PRK)
7.Shop (SHP)

0. Exit
'''),
                             
                         ])
def test_first_time_choose_building_pool_message(option_list,expected):
    """
    test to display first time choose building pool message
    """
    set_keyboard_input(option_list)
    choose_building_pool()
    out = get_display_output()
    output_len = len(out) - 1
    temp_count =0
    combined_output = ""
    for result in out:
        if temp_count <= (output_len - 4):
            combined_output += result
            if result!= out[-1]:
                combined_output += "\n"
        temp_count += 1

    assert combined_output == expected

@pytest.mark.parametrize("option_list, expected",
                         [
                             (["1","0"], '''
--------- CURRENT BUILDING POOL ---------
[BCH]
-----------------------------------------

1.Factory (FAC)
2.House (HSE)
3.Highway (HWY)
4.Monument (MON)
5.Park (PRK)
6.Shop (SHP)

0. Exit
'''),
                             
                         ])
def test_no_show_time_choose_building_pool_message(option_list,expected):
    """
    test to display first time choose building pool message
    """
    set_keyboard_input(option_list)
    choose_building_pool()
    out = get_display_output()
    output_len = len(out) - 1
    temp_count =0
    combined_output = ""
    for result in out:
        if 17 <= temp_count <= (output_len - 4):
            combined_output += result
            if result!= out[-1]:
                combined_output += "\n"
        temp_count += 1

    assert combined_output == expected
    