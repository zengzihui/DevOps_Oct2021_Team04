from cgi import test
from itertools import count
import sys
from unittest import mock
import pytest
from testing_functions import *
from classes.shop import *
from classes.highway import *
from classes.house import *
from classes.factory import *
from classes.beach import *
from classes.game import *

@pytest.mark.parametrize("game_board, total_score, x_coord, y_coord, counted_factory",
                         [
                             ([
                                 [Factory(0,0), Factory(1,0), Factory(2,0) , Factory(3,0)],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]

                                 ],4,0,0,0), 
                             ([
                                 [Factory(0,0), Factory(1,0), Factory(2,0) , Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]
                                 ],3,0,0,0), 
                             (
                                 [
                                     [Factory(0,0), Factory(1,0),Building(), Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                 ],2,0,0,0),
                             (
                                 [
                                     [Factory(0,0), Building(),Building(), Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()]
                                 ],1,0,0,0),
                             (
                                 [
                                     [Factory(0,0), Factory(1,0), Factory(2,0) , Factory(3,0)],
                                     [Factory(0,1),Building(), Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()]
                                 ],1,0,1,4),
                             (
                                 [
                                     [Factory(0,0), Factory(1,0), Factory(2,0) , Factory(3,0)],
                                     [Factory(0,1),Building(), Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()]
                                 ],4,0,0,0)
   
                         
                         ])
def test_calculate_score(game_board, total_score, x_coord, y_coord, counted_factory):
    """
    Test calculate score function of factory object

    Swah Jianoon T01 17th Janunary
    """
    test_building = Factory(x_coord, y_coord)
    test_game = Game()
    test_game.board = game_board

    # test score if there are >4 existing factory
    for h in range(0,test_game.height):
        for w in range(0,test_game.width):
            if test_game.board[h][w].name == "FAC" and counted_factory != 0:
                test_game.board[h][w].counted = True
                counted_factory -= 1

    assert test_building.calculate_score(test_game) == total_score