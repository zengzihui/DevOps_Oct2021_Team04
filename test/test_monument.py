import pytest
from classes.shop import *
from classes.highway import *
from classes.house import *
from classes.factory import *
from classes.beach import *
from classes.game import *
from classes.monument import *
from classes.park import *
@pytest.mark.parametrize("game_board, total_score, x_coord, y_coord",
                         [
                             ([
                                 [Monument(0,0), Building(), Building() , Monument(3,0)],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Monument(0,3),Building(),Building(),Monument(3,3)]
                                 ],4,0,0), 
                             ([
                                 [Monument(0,0), Building(), Building() , Monument(3,0)],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Monument(3,3)]
                                 ],4,0,0), 
                             (
                                 [
                                    [Monument(0,0), Building(), Building() , Building()],
                                    [Building(),Building(),Building(),Building()],
                                    [Building(),Building(),Building(),Building()],
                                    [Building(),Building(),Building(),Building()]
                                 ],2,0,0), 
                             (
                                 [
                                    [Building(), Building(), Building() , Building()],
                                    [Monument(0,1),Building(),Building(),Building()],
                                    [Building(),Building(),Building(),Building()],
                                    [Building(),Building(),Building(),Building()]
                                 ],1,0,1), 
                             (
                                 [
                                    [Monument(0,0), Building(), Building() , Monument(3,0)],
                                    [Monument(0,1),Building(),Building(),Building()],
                                    [Building(),Building(),Building(),Building()],
                                    [Monument(0,3),Building(),Building(),Monument(3,3)]
                                    ],4,0,1)
                         
                         ])
def test_calculate_score(game_board, total_score, x_coord, y_coord):
    """
    Test calculate score function of Monument object
    
    Swah Jianoon T01 18th Janunary
    """
    test_building = Monument(x_coord, y_coord)
    test_game = Game()
    test_game.board = game_board
    assert test_building.calculate_score(test_game) == total_score 