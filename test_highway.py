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
                                 [Highway(0,0), Building(), Building() , Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]

                                 ],1,0,0), 
                             ([
                                 [Highway(0,0), Highway(1,0),Building(), Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]
                                 ],2,0,0), 
                             (
                                 [
                                     [Highway(0,0), Highway(1,0),Highway(2,0), Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                 ],3,0,0),
                             (
                                 [
                                     [Highway(0,0), Highway(1,0),Highway(2,0), Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()]
                                 ],3,1,0),
                             (
                                 [
                                     [Highway(0,0), Highway(1,0),Highway(2,0),Building()],
                                     [Building(),Building(), Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()]
                                 ],3,2,0)
   
                         
                         ])
def test_calculate_score(game_board, total_score, x_coord, y_coord):

    test_building = Highway(x_coord, y_coord)
    test_game = Game()
    test_game.board = game_board
    assert test_building.calculate_score(test_game) == total_score