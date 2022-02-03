from turtle import right
from .building import Building


class Highway(Building):
    def __init__(self, x_coord, y_coord):
        """
        init function for Highway class

        Swah Jian Oon T01 9th December
        """
        self.name = "HWY"
        self.x_coord = x_coord
        self.y_coord = y_coord

    def calculate_score(self, game):
        """
        This function calculates the score for a highway object on the game board

        Swah Jianoon T01 17th Janunary
        """
        left_count = 0
        left_count = self.check_left(game, left_count)
        right_count = 0
        right_count = self.check_right(game, right_count)
        total_score = right_count + left_count + 1
        return total_score

    def check_left(self, game, count):
        """
        recursively check if left side of board has highway

        Swah Jianoon T01 17th Janunary
        """
        if self.get_left_building(game) == None or self.get_left_building(game).name != self.name:
            return count
        else:
            building = self.get_left_building(game)
            count += 1
            return building.check_left(game, count)

    def check_right(self, game, count):
        """
        recursively check if right side of board has highway

        Swah Jianoon T01 17th Janunary
        """
        if self.get_right_building(game) == None or self.get_right_building(game).name != self.name:
            return count
        else:
            building = self.get_right_building(game)
            count += 1
            return building.check_right(game, count)
