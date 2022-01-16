class Building:
    def __init__(self):
        """
        init function for building class

        Zheng Jiongjie T01 9th December
        """
        self.name = ""
        self.x_coord = None
        self.y_coord = None
        return

    def get_top_building(self,game_board):
        """
        Return name of top building if exist
        """

        temp_y_lower =  self.y_coord - 1
        if (0 <= temp_y_lower <= game_board.height):
            pass
        else:
            return None
            
        return game_board.board[temp_y_lower][self.x_coord].name

    def get_bot_building(self,game_board):
        """
        Return name of bottom building if exist
        """

        temp_y_higher = self.y_coord + 1
        if (0 <= temp_y_higher <= game_board.width):
            pass
        else:
            return None
            
        return game_board.board[temp_y_higher][self.x_coord].name
    
    def get_left_building(self,game_board):
        """
        Return name of left building if exist
        """

        temp_x_lower = self.x_coord - 1
        if (0 <= temp_x_lower <= game_board.width):
            pass
        else:
            return None
            
        return game_board.board[self.y_coord][temp_x_lower].name

    def get_right_building(self,game_board):
        """
        Return name of left building if exist
        """

        temp_x_higher = self.x_coord + 1
        if (0 <= temp_x_higher <= game_board.width):
            pass
        else:
            return None
            
        return game_board.board[self.y_coord][temp_x_higher].name

   