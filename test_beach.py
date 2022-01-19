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

@pytest.mark.parametrize("game_board, total_score, x_coord, y_coord",
                         [
                             ([
                                 [Beach(0,0), Building(), Building() , Beach(3,0)],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Beach(1,2),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]

                                 ],3,0,0), 
                             ([
                                 [Beach(0,0), Building(), Building() , Beach(3,0)],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Beach(1,2),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]
                                 ],3,3,0), 
                             (
                                 [
                                    [Beach(0,0), Building(), Building() , Beach(3,0)],
                                    [Building(),Building(),Building(),Building()],
                                    [Building(),Beach(1,2),Building(),Building()],
                                    [Building(),Building(),Building(),Building()]
                                 ],1,1,2)
                         
                         ])
def test_calculate_score(game_board, total_score, x_coord, y_coord):
    """
    Test calculate score function of beach object
    
    Swah Jianoon T01 17th Janunary
    """
    test_building = Beach(x_coord, y_coord)
    test_game = Game()
    test_game.board = game_board
    assert test_building.calculate_score(test_game) == total_score