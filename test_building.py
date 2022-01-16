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

@pytest.mark.parametrize("game_board, building_name,x_coord,y_coord",
                         [
                             ([
                                 [Building(), Shop(1,0), Building() , Building()],
                                 [Factory(0,1),Building(),House(2,1),Building()],
                                 [Building(),Beach(1,2),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]

                                 ],Shop,1,1)

                         ])
def test_get_top_building(game_board,building_name,x_coord,y_coord):
    """
        Test to retrieve the building object above the current building
    """
    test_building = Building()
    test_building.x_coord = x_coord
    test_building.y_coord = y_coord
    test_game = Game()
    test_game.board = game_board
    assert isinstance(test_building.get_top_building(test_game),building_name )


@pytest.mark.parametrize("game_board, building_name,x_coord,y_coord",
                         [
                             ([
                                 [Building(), Shop(1,0), Building() , Building()],
                                 [Factory(0,1),Building(),House(2,1),Building()],
                                 [Building(),Beach(1,2),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]

                                 ], Beach,1,1)

                         ])
def test_get_bot_building(game_board,building_name,x_coord,y_coord):
    """
        Test to retrieve the building object below the current building
    """
    test_building = Building()
    test_building.x_coord = x_coord
    test_building.y_coord = y_coord
    test_game = Game()
    test_game.board = game_board
    assert isinstance(test_building.get_bot_building(test_game),building_name )

@pytest.mark.parametrize("game_board, building_name,x_coord,y_coord",
                         [
                             ([
                                 [Building(), Shop(1,0), Building() , Building()],
                                 [Factory(0,1),Building(),House(2,1),Building()],
                                 [Building(),Beach(1,2),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]

                                 ],House,1,1)

                         ])
def test_get_right_building(game_board,building_name,x_coord,y_coord):
    """
        Test to retrieve the building object to the right of the current building
    """
    test_building = Building()
    test_building.x_coord = x_coord
    test_building.y_coord = y_coord
    test_game = Game()
    test_game.board = game_board
    assert isinstance(test_building.get_right_building(test_game),building_name )

@pytest.mark.parametrize("game_board, building_name,x_coord,y_coord",
                         [
                             ([
                                 [Building(), Shop(1,0), Building() , Building()],
                                 [Factory(0,1),Building(),House(2,1),Building()],
                                 [Building(),Beach(1,2),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]

                                 ],Factory,1,1)

                         ])
def test_get_left_building(game_board,building_name,x_coord,y_coord):
    """
        Test to retrieve the building object to the left of the current building
    """
    test_building = Building()
    test_building.x_coord = x_coord
    test_building.y_coord = y_coord
    test_game = Game()
    test_game.board = game_board
    assert isinstance(test_building.get_left_building(test_game),building_name )


@pytest.mark.parametrize("game_board, building_name,x_coord,y_coord",
                         [
                             ([
                                 [Building(), Shop(1,0), Building() , Building()],
                                 [Factory(0,1),Building(),House(2,1),Building()],
                                 [Building(),Beach(1,2),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]

                                 ],None,0,0)

                         ])
def test_get_top_building_out_of_bounds(game_board,building_name,x_coord,y_coord):
    """
        Test to retrieve the building object above the current building but out of bounds
    """
    test_building = Building()
    test_building.x_coord = x_coord
    test_building.y_coord = y_coord
    test_game = Game()
    test_game.board = game_board
    assert test_building.get_top_building(test_game) == building_name


@pytest.mark.parametrize("game_board, building_name,x_coord,y_coord",
                         [
                             ([
                                 [Building(), Shop(1,0), Building() , Building()],
                                 [Factory(0,1),Building(),House(2,1),Building()],
                                 [Building(),Beach(1,2),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]

                                 ],None,0,0)

                         ])
def test_get_left_building_out_of_bounds(game_board,building_name,x_coord,y_coord):
    """
        Test to retrieve the building object to the left of the current building but out of bounds
    """
    test_building = Building()
    test_building.x_coord = x_coord
    test_building.y_coord = y_coord
    test_game = Game()
    test_game.board = game_board
    assert test_building.get_left_building(test_game) == building_name


@pytest.mark.parametrize("game_board, building_name,x_coord,y_coord",
                         [
                             ([
                                 [Building(), Shop(1,0), Building() , Building()],
                                 [Factory(0,1),Building(),House(2,1),Building()],
                                 [Building(),Beach(1,2),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]

                                 ],None,3,3)

                         ])
def test_get_bot_building_out_of_bounds(game_board,building_name,x_coord,y_coord):
    """
        Test to retrieve the building object below the current building but out of bounds
    """
    test_building = Building()
    test_building.x_coord = x_coord
    test_building.y_coord = y_coord
    test_game = Game()
    test_game.board = game_board
    assert test_building.get_bot_building(test_game) == building_name

@pytest.mark.parametrize("game_board, building_name,x_coord,y_coord",
                         [
                             ([
                                 [Building(), Shop(1,0), Building() , Building()],
                                 [Factory(0,1),Building(),House(2,1),Building()],
                                 [Building(),Beach(1,2),Building(),Building()],
                                 [Building(),Building(),Building(),Building()]

                                 ],None,3,3)

                         ])
def test_get_right_building_out_of_bounds(game_board,building_name,x_coord,y_coord):
    """
        Test to retrieve the building object to the right of the current building but out of bounds
    """
    test_building = Building()
    test_building.x_coord = x_coord
    test_building.y_coord = y_coord
    test_game = Game()
    test_game.board = game_board
    assert test_building.get_right_building(test_game) == building_name

def test_calculate_score():
    test_building = Building()
    assert test_building.calculate_score() == None