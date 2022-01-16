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
                                 [Shop()]
                            
                                 ],0), 
                             ([
                                 [Shop(), Highway()]
                                 ],1), 
                             (
                                 [
                                     [House(), Shop(),Highway()]
                                 ],2),
                             (
                                 [
                                     [House(), Shop(),Highway()],
                                     [None,Beach(),None]
                                 ],3),
                             (
                                 [
                                     [None, Beach(),None],
                                     [House(),Shop(),Highway()],
                                     [None,Factory(),None]
                                 ],4),
                         
                         ])
def test_calculate_score(game_board, score):

    test_building = Shop()
    test_game = Game()
    test_game.board = game_board
    assert test_building.calculate_score(test_game.board) == score