import sys
from unittest import mock
import pytest
from test.testing_functions import *
from classes.shop import *
from classes.highway import *
from classes.house import *
from classes.factory import *
from classes.beach import *
from classes.game import *


@pytest.mark.parametrize("game_board, total_score, x_coord, y_coord",
                         [
                             ([
                                 [House(0, 0), Building(), Building(), Building()],
                                 [Building(), Building(), Building(), Building()],
                                 [Building(), Building(), Building(), Building()],
                                 [Building(), Building(), Building(), Building()]

                             ], 0, 0, 0),
                             ([
                                 [House(0, 0), Factory(1, 0), Building(), Building()],
                                 [Building(), Building(), Building(), Building()],
                                 [Building(), Building(), Building(), Building()],
                                 [Building(), Building(), Building(), Building()]
                             ], 1, 0, 0),
                             (
                                 [
                                     [House(0, 0), Shop(1, 0), Building(), Building()],
                                     [Building(), Building(), Building(), Building()],
                                     [Building(), Building(), Building(), Building()],
                                     [Building(), Building(), Building(), Building()],
                                 ], 1, 0, 0),
                             (
                                 [
                                     [House(0, 0), Beach(1, 0), Building(), Building()],
                                     [Building(), Building(), Building(), Building()],
                                     [Building(), Building(), Building(), Building()],
                                     [Building(), Building(), Building(), Building()]
                                 ], 2, 0, 0),
                             (
                                 [
                                     [Building(), Shop(1, 0), Building(), Building()],
                                     [Beach(0, 1), House(1, 1), House(2, 1), Building()],
                                     [Building(), Building(), Building(), Building()],
                                     [Building(), Building(), Building(), Building()]
                                 ], 4, 1, 1),
                             (
                                 [
                                     [House(0, 0), House(1, 0), Building(), Building()],
                                     [Building(), Building(), Building(), Building()],
                                     [Building(), Building(), Building(), Building()],
                                     [Building(), Building(), Building(), Building()]
                                 ], 1, 0, 0),
                             (
                                 [
                                     [Building(), Shop(1, 0), Building(), Building()],
                                     [Beach(0, 1), House(1, 1), House(2, 1), Building()],
                                     [Building(), Factory(1, 2), Building(), Building()],
                                     [Building(), Building(), Building(), Building()]
                                 ], 1, 1, 1),

                             (
                                 [
                                     [Building(), Factory(1, 0), Building(), Building()],
                                     [Beach(0, 1), House(1, 1), Shop(2, 1), Building()],
                                     [Building(), House(1, 2), Building(), Building()],
                                     [Building(), Building(), Building(), Building()]
                                 ], 1, 1, 1),

                             (
                                 [
                                     [Building(), House(1, 0), Building(), Building()],
                                     [Factory(0, 1), House(1, 1), Shop(2, 1), Building()],
                                     [Building(), House(1, 2), Building(), Building()],
                                     [Building(), Building(), Building(), Building()]
                                 ], 1, 1, 1),



                         ])
def test_calculate_score(game_board, total_score, x_coord, y_coord):
    """
    Test calculate score function of house object

    Swah Jianoon T01 17th Janunary
    """
    test_building = House(x_coord, y_coord)
    test_game = Game()
    test_game.board = game_board
    assert test_building.calculate_score(test_game) == total_score
