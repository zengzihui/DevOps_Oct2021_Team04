import pytest
from testing_functions import *
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
                                 [Park(), Park(), Park() , Park(),Park()],
                                 [Park(),Building(),Building(),Building(),Building()],
                                 [Park(),Building(),Building(),Building(),Building()],
                                 [Park(),Building(),Building(),Building(),Building()]
                                 ],25,0,0),
                            ([
                                 [Park(), Park(), Park() , Park(),Building()],
                                 [Park(),Building(),Building(),Building(),Building()],
                                 [Park(),Building(),Building(),Building(),Building()],
                                 [Park(),Building(),Building(),Building(),Building()]
                                 ],24,0,0),
                            ([
                                 [Park(), Park(), Park() , Park(),Building()],
                                 [Park(),Building(),Building(),Building(),Building()],
                                 [Park(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()]
                                 ],23,0,0),
                            ([
                                 [Park(), Park(), Park() , Park(),Building()],
                                 [Park(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()]
                                 ],22,0,0),
                            ([
                                 [Park(), Park(), Park() , Park(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()]
                                 ],16,0,0),
                            ([
                                 [Park(), Park(), Park() , Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()]
                                 ],8,0,0),
                            ([
                                 [Park(), Park(), Building() , Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()]
                                 ],3,0,0),
                            ([
                                 [Park(), Building(), Building() , Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()]
                                 ],1,0,0)
                         ])
def test_calculate_score(game_board, total_score, x_coord, y_coord):
    """
    Test calculate score function of park object
    
    Swah Jianoon T01 18th Janunary
    """
    test_building = Park(x_coord, y_coord)
    test_game = Game()
    test_game.board = game_board
    assert test_building.calculate_score(test_game) == total_score 