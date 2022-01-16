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

@pytest.mark.parametrize("game_board,score,x_coord,y_coord",
                         [  
                             ([
                                 [Shop(0,0),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]
                            
                                 ],0,0,0), 

                             ([
                                 [Shop(0,0), Highway(), Building(), Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]

                                 ],1,0,0), 
                             (
                                 [
                                     [House(), Shop(1,0),Highway(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()]
                                 ],2 ,1,0),
                             (
                                 [
                                     [House(), Shop(1,0),Highway(),Building()],
                                     [Building(),Beach(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()]
                                 ],3, 1,0 ),
                             (
                                 [
                                     [Building(),Beach(),Building(),Building()],
                                     [House(),Shop(1,1),Highway(),Building()],
                                     [Building(),Factory(),Building(),Building()],
                                     [Building(),Building(),Building(),Building()]
                                 ],4, 1, 1),
                         
                         ])
def test_calculate_score(game_board, score, x_coord, y_coord):

    test_building = Shop(x_coord, y_coord)
    test_game = Game()
    test_game.board = game_board
    assert test_building.calculate_score(test_game) == score