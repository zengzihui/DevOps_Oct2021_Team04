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

@pytest.mark.parametrize("game_board,score",
                         [
                             ([
                                 [House()]
                            
                                 ],0), 
                            (
                                 [
                                    
                                 ]
                                 ,0),
                             ([
                                 [House(), Factory()]
                                 ],1), 
                             (
                                 [
                                     [House(), Shop()]
                                 ],1),
                             (
                                 [
                                     [House(), Beach()]
                                 ],2),
                             (
                                 [
                                     [None,Shop(),None],
                                     [Beach(),House(), House()],
                                 ],4),
                             (
                                 [
                                     [House(),House()]
                                 ], 2),
                            (
                                [
                                     [None,Shop(),None],
                                     [Beach(),House(), House()],
                                     [None,Factory(),None]
                                 ], 1)
   
                         
                         ])
def test_calculate_score(game_board, total_score):

    test_building = House()
    test_game = Game()
    test_game.board = game_board
    assert test_building.calculate_score(test_game.board) == total_score