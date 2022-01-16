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
                                 [Factory(0,0), Factory(1,0), Factory(2,0) , Factory(3,0)],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]

                                 ],16,0,0), 
                             ([
                                 [Factory(0,0), Factory(1,0), Factory(2,0) , Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]
                                 ],9,0,0), 
                             (
                                 [
                                     [Factory(0,0), Factory(1,0),Building(), Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                 ],4,0,0),
                             (
                                 [
                                     [Factory(0,0), Building(),Building(), Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()]
                                 ],1,0,0),
                             (
                                 [
                                     [Factory(0,0), Factory(1,0), Factory(2,0) , Factory(3,0)],
                                     [Factory(0,1),Building(), Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()]
                                 ],17,0,0)
   
                         
                         ])
def test_calculate_score(game_board, total_score, x_coord, y_coord):

    test_building = House(x_coord, y_coord)
    test_game = Game()
    test_game.board = game_board
    assert test_building.calculate_score(test_game) == total_score