import sys
from unittest import mock
import pytest
from classes.menu import *
from classes.monument import Monument
from classes.park import Park
from test.testing_functions import *
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

    Zheng Jiongjie T01 9th December
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

    Zheng Jiongjie T01 9th December
    """
    set_keyboard_input(None)

    # create testing game object
    test_game = Game(building_pool={"HSE": 8, "FAC": 8, "SHP": 8, "HWY": 8, "BCH": 8})
    test_game.print_board()

    # check if print_board() displays game board correctly
    out = get_display_output()
    assert out == [
        "     A     B     C     D           Building   Remaining",
        "  +-----+-----+-----+-----+        --------------------",
        " 1|     |     |     |     |        HSE      | 8",
        "  +-----+-----+-----+-----+        FAC      | 8",
        " 2|     |     |     |     |        SHP      | 8",
        "  +-----+-----+-----+-----+        HWY      | 8",
        " 3|     |     |     |     |        BCH      | 8",
        "  +-----+-----+-----+-----+",
        " 4|     |     |     |     |",
        "  +-----+-----+-----+-----+"]


def test_print_board_for_small_board():
    """
    test if game board is printed correctly

    Zheng Jiongjie T01 9th December
    """
    set_keyboard_input(None)
    # create testing game object
    test_game = Game(height=1, width=1, building_pool={"HSE": 8, "FAC": 8, "SHP": 8, "HWY": 8, "BCH": 8})

    test_game.print_board()
    # check if print_board() displays game board correctly
    out = get_display_output()
    assert out == [
        '     A           Building   Remaining',
        '  +-----+        --------------------',
        ' 1|     |        HSE      | 8',
        '  +-----+        FAC      | 8',
        '                 SHP      | 8',
        '                 HWY      | 8',
        '                 BCH      | 8']


def test_game_menu_display():
    """
    test if game menu options are printed correctly

    Zheng Jiongjie T01 9th December
    """

    # set input for menu options
    set_keyboard_input(["0", "0", "0"])
    # create testing game object
    test_game = Game()

    test_game.game_menu()

    # check if game menu displays correct output
    out = get_display_output()

    assert out == ['1. Build a SHP', '2. Build a SHP', '3. See remaining buildings',
                   '4. See current score', '', '5. Save game', '0. Exit to main menu', 'Your choice? ']


@pytest.mark.parametrize("option_list, expected",
                         [(["", "2"], 2), (["1"], 1), (["0"], 0), (["7", "4"], 4), (["a", "!", "0", "2"], 0)])
def test_game_menu_input(mocker, option_list, expected):
    """
    test if game menu is printed correctly and the option entered is returned

    Zheng Jiongjie T01 9th December
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

    Zheng Jiongjie T01 9th December
    """
    set_keyboard_input(["0"])

    # create testing game object
    test_game = Game(building_pool={"HSE": 8, "FAC": 8, "SHP": 8, "HWY": 8, "BCH": 8})

    # fill game object with fake randomized building history
    test_game.randomized_building_history = {"1": ["SHP", "SHP"]}

    # check if game menu displays correct output
    test_game.start_new_turn()

    # check if output is expected
    out = get_display_output()
    assert out == [
        "",
        "Turn 1",
        "     A     B     C     D           Building   Remaining",
        "  +-----+-----+-----+-----+        --------------------",
        " 1|     |     |     |     |        HSE      | 8",
        "  +-----+-----+-----+-----+        FAC      | 8",
        " 2|     |     |     |     |        SHP      | 8",
        "  +-----+-----+-----+-----+        HWY      | 8",
        " 3|     |     |     |     |        BCH      | 8",
        "  +-----+-----+-----+-----+",
        " 4|     |     |     |     |",
        "  +-----+-----+-----+-----+",
        "1. Build a SHP",
        "2. Build a SHP",
        "3. See remaining buildings",
        "4. See current score",
        "",
        "5. Save game",
        "0. Exit to main menu",
        'Your choice? ']


@pytest.mark.parametrize("option, expected",
                         [(["1"], 1), (["2"], 1), (["100", "2"], 1), (["3"], 2), (["4"], 3)])
def test_start_new_turn_options(option, expected, mocker):
    """
    run start_new_turn input options

    Zheng Jiongjie T01 9th December
    """
    set_keyboard_input(option)
    mocker.patch('classes.game.Game.add_building', return_value=1)
    mocker.patch('classes.game.Game.display_building', return_value=2)
    mocker.patch('classes.game.Game.display_all_scores', return_value=3)
    test_game = Game()
    assert test_game.start_new_turn() == expected


@pytest.mark.parametrize("building, expected",
                         [(Beach(0, 0), "BCH"), (Factory(0, 0), "FAC"), (Shop(0, 0), "SHP"), (Highway(0, 0), "HWY"), (House(0, 0), "HSE")])
def test_sub_classes(building, expected):
    """
    test if the different buildings can be initialized

    Swah Jianoon T01 9th December
    """
    assert building.name == expected


@pytest.mark.parametrize("location,x,y,building_name,building_type",
                         [("a1", 0, 0, "SHP", Shop), ("a2", 0, 1, "FAC", Factory), ("a1", 0, 0, "BCH", Beach), ("a1", 0, 0, "HSE", House), ("a1", 0, 0, "HWY", Highway), ("a1", 0, 0, "MON", Monument), ("a1", 0, 0, "PRK", Park)])
def test_add_building(location, x, y, building_name, building_type, mocker):
    """
    success cases for adding_building function

    Swah Jianoon T01 9th December
    """
    mocker.patch('classes.game.Game.start_new_turn', return_value=True)
    test_game = Game()
    set_keyboard_input([location])
    test_game.building_pool = {"HSE": 8, "FAC": 8, "SHP": 8, "HWY": 8, "BCH": 8, "MON": 8, "PRK": 8}
    test_game.add_building(building_name)
    assert isinstance(test_game.board[y][x], building_type)


@pytest.mark.parametrize("location",
                         [("a6"), ("z2"), ("2"), ("z"), ("")])
def test_add_building_failure_random_input(location, mocker):
    """
    failing cases for adding_building function for random input

    Swah Jianoon T01 9th December
    """
    mocker.patch('classes.game.Game.start_new_turn', return_value=True)
    test_game = Game()
    set_keyboard_input([location])
    test_game.add_building("SHP")
    output = get_display_output()
    assert output[1] == "Your input is invalid, please follow 'letter' + 'digit' format to input for location."


@pytest.mark.parametrize("location",
                         [("b1")])
def test_add_building_failure_existing_building(location, mocker):
    """
    failing cases for adding_building function for placing a building on an existing one

    Swah Jianoon T01 9th December
    """
    mocker.patch('classes.game.Game.start_new_turn', return_value=True)
    test_game = Game()
    test_game.board[0][1] = Shop(0, 1)
    set_keyboard_input([location])
    test_game.add_building("SHP")
    output = get_display_output()
    assert output[1] == "You cannot build on a location that has already had a building"


@pytest.mark.parametrize("location",
                         [("a4")])
def test_add_building_failure_adjacent_building(location, mocker):
    """
    failing cases for adding_building function for placing a building on an existing one

    Swah Jianoon T01 9th December
    """
    mocker.patch('classes.game.Game.start_new_turn', return_value=True)
    test_game = Game()
    test_game.turn_num = 2
    test_game.board[0][1] = Shop(0, 1)
    set_keyboard_input([location])
    test_game.add_building("SHP")
    output = get_display_output()
    assert output[1] == "You must build next to an existing building."


@pytest.mark.parametrize("location,expected_x,expected_y", [("a1", 0, 0), ("a5", 0, 4), ("b6", 1, 5)])
def test_input_to_coordinates(location, expected_x, expected_y):
    """
    test function to convert input to coordinates

    Swah Jianoon T01 9th December
    """
    test_game = Game()
    x, y = test_game.input_to_coordinates(location)
    assert x == expected_x
    assert y == expected_y


@pytest.mark.parametrize("test_pass, x_coord, y_coord",
                         [(True, 1, 0), (True, 0, 1), (True, 1, 2), (True, 2, 1), (False, 3, 3), (False, 0, 3)])
def test_check_surrounding_buildings_exist(test_pass, x_coord, y_coord):
    """
    test if surroundings buildings exist function works

    Swah Jianoon T01 9th December
    """
    test_game = Game()
    test_game.board[1][1] = Shop(1, 1)
    assert test_game.check_surrounding_buildings_exist(x_coord, y_coord) == test_pass


@pytest.mark.parametrize("test_pass, x_coord, y_coord",
                         [(True, 1, 0), (False, 0, 1)])
def test_check_building_exist(test_pass, x_coord, y_coord):
    """
    test if check building exist

    Swah Jianoon T01 9th December
    """
    test_game = Game()
    test_game.board[0][1] = Shop(0, 1)

    assert test_game.check_building_exist(x_coord, y_coord) == test_pass


@pytest.mark.parametrize("building_name",
                         [("FAC"), ("SHP"), ("BCH"), ("HWY"), ("HSE")])
def test_remove_building(building_name):
    """
    test if building can be removed from the building pool

    Swah Jianoon T01 9th December
    """
    test_game = Game()
    test_game.building_pool = {"HSE": 8, "FAC": 8, "SHP": 8, "HWY": 8, "BCH": 8, "MON": 8, "PRK": 8}
    test_game.remove_building(building_name)
    assert test_game.building_pool[building_name] == 7


def test_display_building(mocker):
    """
    test if display buildings pool works

    Swah Jianoon T01 9th December
    """
    mocker.patch('classes.game.Game.start_new_turn', return_value=True)
    set_keyboard_input(None)
    test_game = Game()
    test_game.building_pool = {"HSE": 8, "FAC": 8, "SHP": 8, "HWY": 8, "BCH": 8}
    match = '''Building         Remaining
--------         --------
HSE              8
FAC              8
SHP              8
HWY              8
BCH              8\n'''

    test_game.display_building()
    output = get_display_output()
    assert match == output[0]


@pytest.mark.parametrize("game_board, match",
                         [
                             ([
                                 [Shop(0, 0), Shop(1, 0), House(2, 0), Factory(3, 0)],
                                 [Beach(0, 1), House(1, 1), House(2, 1), Beach(3, 1)],
                                 [Beach(0, 2), Shop(1, 2), House(2, 2), House(3, 2)],
                                 [Highway(0, 3), Highway(1, 3), Highway(2, 3), Highway(3, 3)]

                             ],
                                 '''HSE: 1 + 5 + 5 + 3 + 3 = 17
FAC: 1 = 1
SHP: 2 + 2 + 3 = 7
HWY: 4 + 4 + 4 + 4 = 16
BCH: 3 + 3 + 3 = 9
Total score: 50'''
                             ),
                             ([
                                 [Shop(0, 0), Shop(1, 0), House(2, 0), Factory(3, 0)],
                                 [Beach(0, 1), House(1, 1), House(2, 1), Beach(3, 1)],
                                 [Beach(0, 2), Shop(1, 2), House(2, 2), House(3, 2)],
                                 [Highway(0, 3), Highway(1, 3), Highway(2, 3), Building()]

                             ],
                                 '''HSE: 1 + 5 + 5 + 3 + 3 = 17
FAC: 1 = 1
SHP: 2 + 2 + 3 = 7
HWY: 3 + 3 + 3 = 9
BCH: 3 + 3 + 3 = 9
Total score: 43'''
                             ),
                             ([
                                 [Building(), Building(), Building(), Building()],
                                 [Building(), Building(), Building(), Building()],
                                 [Building(), Building(), Building(), Building()],
                                 [Building(), Building(), Building(), Building()]

                             ],
                                 '''HSE: 0
FAC: 0
SHP: 0
HWY: 0
BCH: 0
Total score: 0'''
                             )

                         ])
def test_display_all_scores(game_board, match, mocker):
    """
    test if all scores are displayed

    Swah Jianoon T01 17th Janunary
    """
    mocker.patch('classes.game.Game.start_new_turn', return_value=0)
    test_string = ""
    set_keyboard_input(None)
    test_game = Game()
    test_game.building_pool = {"HSE": 8, "FAC": 8, "SHP": 8, "HWY": 8, "BCH": 8}
    test_game.board = game_board

    test_game.display_all_scores()
    output = get_display_output()
    for out in output:
        test_string += out
        if out != output[-1]:
            test_string += "\n"
    assert test_string == match


def test_randomize_two_buildings_from_pool_random():
    """
    tests get_two_buildings_from_pool() function if the results are properly randomized

    Zheng Jiongjie T01 16th January
    """
    # run randomze buildings for 10 turns 10 times
    for i in range(0, 10):
        test_game = Game()
        test_game.building_pool = {"HSE": 8, "FAC": 8, "SHP": 8, "HWY": 8, "BCH": 8}

        # generate randomized buildings for turn 1
        test_game.get_two_buildings_from_pool(test_game.building_pool)

        # generate randomized buildings for turn 2
        test_game.turn_num = 2
        test_game.get_two_buildings_from_pool(test_game.building_pool)

        # generate randomized buildings for turn 3
        test_game.turn_num = 3
        test_game.get_two_buildings_from_pool(test_game.building_pool)

        # generate randomized buildings for turn 4
        test_game.turn_num = 4
        test_game.get_two_buildings_from_pool(test_game.building_pool)

        # generate randomized buildings for turn 5
        test_game.turn_num = 5
        test_game.get_two_buildings_from_pool(test_game.building_pool)

        # generate randomized buildings for turn 6
        test_game.turn_num = 6
        test_game.get_two_buildings_from_pool(test_game.building_pool)

        # generate randomized buildings for turn 7
        test_game.turn_num = 7
        test_game.get_two_buildings_from_pool(test_game.building_pool)

        # generate randomized buildings for turn 8
        test_game.turn_num = 8
        test_game.get_two_buildings_from_pool(test_game.building_pool)

        # generate randomized buildings for turn 9
        test_game.turn_num = 9
        test_game.get_two_buildings_from_pool(test_game.building_pool)

        # generate randomized buildings for turn 10
        test_game.turn_num = 10
        test_game.get_two_buildings_from_pool(test_game.building_pool)

        # assert randomly generated buildings across all 10 turns are not the same
        assert not (test_game.randomized_building_history["1"] == test_game.randomized_building_history["2"] ==
                    test_game.randomized_building_history["3"] == test_game.randomized_building_history["4"] ==
                    test_game.randomized_building_history["5"] == test_game.randomized_building_history["6"] ==
                    test_game.randomized_building_history["7"] == test_game.randomized_building_history["8"] ==
                    test_game.randomized_building_history["9"] == test_game.randomized_building_history["10"])


def test_randomize_two_buildings_from_pool_when_no_building_for_type():
    """
    tests get_two_buildings_from_pool() function if the it returns buildings with 0 buildings left in pool

    Zheng Jiongjie T01 16th January
    """
    test_game = Game()

    # remove all beaches from building pool
    test_game.building_pool = {"HSE": 8, "FAC": 8, "SHP": 8, "HWY": 8, "BCH": 0}

    # loop through 10 times, BCH must never be the value returned from get_two_buildings_from_pool()
    for i in range(0, 10):
        # get randomized building
        test_game.get_two_buildings_from_pool(test_game.building_pool)
        # check each item in randomized building
        for item in test_game.randomized_building_history[str(test_game.turn_num)]:
            # BCH must never appear from randomized building, since there is 0 of it left in the pool
            assert item != "BCH"


def test_randomize_two_buildings_from_pool_when_no_building():
    """
    tests get_two_buildings_from_pool() function if building pool is empty

    Zheng Jiongjie T01 16th January
    """
    test_game = Game()

    # remove all beaches from building pool
    test_game.building_pool = {"HSE": 0, "FAC": 0, "SHP": 0, "HWY": 0, "BCH": 0}

    # get randomized building
    test_game.get_two_buildings_from_pool(test_game.building_pool)
    # check each item in randomized building
    for item in test_game.randomized_building_history[str(test_game.turn_num)]:
        # nothing must never appear from randomized building, since there is no building in pool
        assert item == ""


@pytest.mark.parametrize("game_board, match",
                         [
                             ([
                                 [Shop(0, 0), Shop(1, 0), House(2, 0), Factory(3, 0)],
                                 [Beach(0, 1), House(1, 1), House(2, 1), Beach(3, 1)],
                                 [Beach(0, 2), Shop(1, 2), House(2, 2), House(3, 2)],
                                 [Highway(0, 3), Highway(1, 3), Highway(2, 3), Building()]
                             ],
                                 [
                                 '',
                                 'Turn 16',
                                 '     A     B     C     D           Building   Remaining',
                                 '  +-----+-----+-----+-----+        --------------------',
                                 ' 1| SHP | SHP | HSE | FAC |        HSE      | 20',
                                 '  +-----+-----+-----+-----+        FAC      | 0',
                                 ' 2| BCH | HSE | HSE | BCH |        SHP      | 0',
                                 '  +-----+-----+-----+-----+        HWY      | 2',
                                 ' 3| BCH | SHP | HSE | HSE |        BCH      | 0',
                                 '  +-----+-----+-----+-----+',
                                 ' 4| HWY | HWY | HWY |     |',
                                 '  +-----+-----+-----+-----+',
                                 '1. Build a HWY',
                                 '2. Build a HWY',
                                 '3. See remaining buildings',
                                 '4. See current score',
                                 '',
                                 '5. Save game',
                                 '0. Exit to main menu',
                                 'Your choice? ',
                                 'Build where? ',
                                 '',
                                 'Final layout of Simp City:',
                                 '     A     B     C     D  ',
                                 '  +-----+-----+-----+-----+',
                                 ' 1| SHP | SHP | HSE | FAC |',
                                 '  +-----+-----+-----+-----+',
                                 ' 2| BCH | HSE | HSE | BCH |',
                                 '  +-----+-----+-----+-----+',
                                 ' 3| BCH | SHP | HSE | HSE |',
                                 '  +-----+-----+-----+-----+',
                                 ' 4| HWY | HWY | HWY | HWY |',
                                 '  +-----+-----+-----+-----+',
                                 'HSE: 1 + 5 + 5 + 3 + 3 = 17',
                                 'FAC: 1 = 1',
                                 'SHP: 2 + 2 + 3 = 7',
                                 'HWY: 4 + 4 + 4 + 4 = 16',
                                 'BCH: 3 + 3 + 3 = 9',
                                 'Total score: 50'])])
def test_end_of_game_display(game_board, match):
    """
    check if game ends when all spaces on the board is filled

    Zheng Jiongjie T01 20th January
    """

    test_game = Game()

    # set dummy game board at final turn
    test_game.board = game_board
    test_game.turn_num = 16
    test_game.randomized_building_history = {"16": ["HWY", "HWY"]}
    test_game.building_pool = {"HSE": 20, "FAC": 0, "SHP": 0, "HWY": 2, "BCH": 0}

    # build final highway building at d4
    set_keyboard_input(["1", "d4"])

    test_game.start_new_turn()

    output = get_display_output()

    assert output == match
