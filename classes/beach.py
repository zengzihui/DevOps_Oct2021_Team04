from .building import Building


class Beach(Building):
    """
    init function for Beach class

    Swah Jian Oon T01 9th December
    """

    def __init__(self, x_coord, y_coord):
        self.name = "BCH"
        self.x_coord = x_coord
        self.y_coord = y_coord

    def calculate_score(self, game):
        """
        This function calculates the score for a beach object on the game board

        Swah Jianoon T01 17th Janunary
        """
        if self.x_coord == 0 or self.x_coord == game.width - 1:
            return 3
        else:
            return 1
