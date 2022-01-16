from .building import Building


class Shop(Building):
    """
    init function for Shop class

    Swah Jian Oon T01 9th December
    """
    def __init__(self,x_coord,y_coord):
        self.name = "SHP"
        self.x_coord = x_coord
        self.y_coord = y_coord

    def calculate_score(self,game_board):
        """
        This function calculates the score for a shop object on the game board
        """
        total_score = 0
        score_dict = {"":0,self.name:0}
        # fill up score_dict dictionary with 4 different types of building with 1 count
        for key in game_board.building_pool:
            if key != "SHP":
                score_dict[key] = 1
                continue
        
        temp_x_lower = self.x_coord - 1
        if (0 <= temp_x_lower < game_board.width):
            pass
        else:
            temp_x_lower = 0

        temp_x_higher = self.x_coord + 1
        if (0 <= temp_x_higher < game_board.width):
            pass
        else:
            temp_x_higher = game_board.width

        temp_y_lower = self.y_coord - 1
        if (0 <= temp_y_lower < game_board.height):
            pass
        else:
            temp_x_lower = 0
        
        temp_y_higher = self.y_coord + 1
        if (0 <= temp_y_higher < game_board.height):
            pass
        else:
            temp_x_higher = game_board.height
        
        if score_dict[game_board.board[self.y_coord][temp_x_lower].name] == 1:
            score_dict[game_board.board[self.y_coord][temp_x_lower].name] = 0
            total_score += 1
        
        if score_dict[game_board.board[self.y_coord][temp_x_higher].name] == 1:
            score_dict[game_board.board[self.y_coord][temp_x_higher].name] = 0
            total_score += 1

        if score_dict[game_board.board[temp_y_lower][self.x_coord].name] == 1:
            score_dict[game_board.board[temp_y_lower][self.x_coord].name] = 0
            total_score += 1
        
        if score_dict[game_board.board[temp_y_higher][self.x_coord].name] == 1:
            score_dict[game_board.board[temp_y_higher][self.x_coord].name] = 0
            total_score += 1

        return total_score
