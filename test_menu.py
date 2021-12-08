import sys
from unittest import mock
import pytest
from classes.menu import main_menu
from testing_functions import *


@pytest.mark.parametrize("option_list",
                         [(["0"])])
def test_main_menu_display(mocker, option_list):
    """
    test if main menu options are printed correctly
    """
    set_keyboard_input(None)

    # set input for menu options
    mocker.patch('builtins.input', side_effect=option_list)

    # run main menu function
    selected = main_menu()

    # check if main_menu function displays correct output
    out = get_display_output()
    assert out[0] == 'Welcome, mayor of Simp City!        \n----------------------------\n1. Start new game\n2. Load saved game\n0. Exit\n'
