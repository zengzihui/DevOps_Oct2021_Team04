from pyexpat.errors import XML_ERROR_INCORRECT_ENCODING
from .building import Building


class House(Building):
    def __init__(self,x_coord,y_coord):
        """
        init function for House class

        Swah Jian Oon T01 9th December
        """
        self.name = "HSE"
        self.x_coord = x_coord
        self.y_coord = y_coord

    def calculate_score(self,game_board):
        """
        This function calculates the score for a house object on the game board
        """
        total_score = 0
        score_dict = {"HSE": 1, "FAC": 1, "SHP": 1, "BCH": 2}

        if self.get_top_building(game_board) != None:
            building = self.get_top_building(game_board)
            if building == "FAC":
                return score_dict[building]
            elif building in score_dict:
                total_score += score_dict[building]
        
        if self.get_bot_building(game_board) != None:
            building = self.get_bot_building(game_board)
            if building == "FAC":
                return score_dict[building]
            elif building in score_dict:
                total_score += score_dict[building]

        if self.get_left_building(game_board) != None:
            building = self.get_left_building(game_board)
            if building == "FAC":
                return score_dict[building]
            elif building in score_dict:
                total_score += score_dict[building]

        if self.get_right_building(game_board) != None:
            building = self.get_right_building(game_board)
            if building == "FAC":
                return score_dict[building]
            elif building in score_dict:
                total_score += score_dict[building]
        
        
        return total_score

    
