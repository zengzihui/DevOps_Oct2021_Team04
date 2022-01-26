import pytest
from classes.shop import *
from classes.highway import *
from classes.house import *
from classes.factory import *
from classes.beach import *
from classes.game import *
from classes.monument import *
from classes.park import *
@pytest.mark.parametrize("game_board, total_score, x_coord, y_coord, counted",
                         [
                             ([
                                 [Park(0,0), Park(1,0), Park(2,0) , Park(3,0),Park(4,0)],
                                 [Park(0,1),Building(),Building(),Building(),Building()],
                                 [Park(0,2),Building(),Building(),Building(),Building()],
                                 [Park(0,3),Building(),Building(),Building(),Building()]
                                 ],1,0,3,7),
                            ([
                                 [Park(0,0), Park(1,0), Park(2,0) , Park(3,0),Park(4,0)],
                                 [Park(0,1),Building(),Building(),Building(),Building()],
                                 [Park(0,2),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()]
                                 ],1,0,2,6),
                            ([
                                 [Park(0,0), Park(1,0), Park(2,0) , Park(3,0),Park(4,0)],
                                 [Park(0,1),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()]
                                 ],1,0,1,5),
                            ([
                                 [Park(0,0), Park(1,0), Park(2,0) , Park(3,0),Park(4,0)],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()]
                                 ],6,4,0,4),
                            ([
                                 [Park(0,0), Park(1,0), Park(2,0) , Park(3,0),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()]
                                 ],8,3,0,3),
                            ([
                                 [Park(0,0), Park(1,0),Park(2,0), Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()]
                                 ],5,2,0,2),
                            ([
                                 [Park(0,0), Park(1,0), Building() , Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()]
                                 ],2,1,0,1),
                            ([
                                 [Park(0,0), Building(), Building() , Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()],
                                 [Building(),Building(),Building(),Building(),Building()]
                                 ],1,0,0,0)
                         ])
def test_calculate_score(game_board, total_score, x_coord, y_coord, counted):
    """
    Test calculate score function of park object
    
    Swah Jianoon T01 18th Janunary
    """
    test_building = Park(x_coord, y_coord)
    test_game = Game(3,4)
    test_game.board = game_board

    for h in range(0,test_game.height + 1):
        for w in range(0,test_game.width + 1):
            if test_game.board[h][w].name == "PRK" and counted != 0:
                test_game.board[h][w].counted = True
                counted -= 1

    assert test_building.calculate_score(test_game) == total_score 