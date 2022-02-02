from .building import Building


class Shop(Building):
    """
    init function for Shop class

    Swah Jian Oon T01 9th December
    """

    def __init__(self, x_coord, y_coord):
        self.name = "SHP"
        self.x_coord = x_coord
        self.y_coord = y_coord

    def calculate_score(self, game):
        """
        This function calculates the score for a shop object on the game board
        """
        total_score = 0
        score_dict = {"": 0, self.name: 0}
        # fill up score_dict dictionary with 4 different types of building with 1 count
        for key in game.building_pool:
            score_dict[key] = 1

        if self.get_top_building(game) != None:
            building = self.get_top_building(game).name
            if score_dict[building] == 1:
                score_dict[building] = 0
                total_score += 1

        if self.get_bot_building(game) != None:
            building = self.get_bot_building(game).name
            if score_dict[building] == 1:
                score_dict[building] = 0
                total_score += 1

        if self.get_left_building(game) != None:
            building = self.get_left_building(game).name
            if score_dict[building] == 1:
                score_dict[building] = 0
                total_score += 1

        if self.get_right_building(game) != None:
            building = self.get_right_building(game).name
            if score_dict[building] == 1:
                score_dict[building] = 0
                total_score += 1

        return total_score
