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

    def get_top_building(self, game):
        """
        Return name of top building if exist

        Swah Jianoon T01 17th Janunary
        """

        temp_y_lower = self.y_coord - 1
        if (0 <= temp_y_lower < game.height):
            return game.board[temp_y_lower][self.x_coord]
        else:
            return None

    def get_bot_building(self, game):
        """
        Return name of bottom building if exist

        Swah Jianoon T01 17th Janunary
        """

        temp_y_higher = self.y_coord + 1
        if (0 <= temp_y_higher < game.height):
            return game.board[temp_y_higher][self.x_coord]
        else:
            return None

    def get_left_building(self, game):
        """
        Return name of left building if exist

        Swah Jianoon T01 17th Janunary
        """

        temp_x_lower = self.x_coord - 1
        if (0 <= temp_x_lower < game.width):
            return game.board[self.y_coord][temp_x_lower]
        else:
            return None

    def get_right_building(self, game):
        """
        Return name of left building if exist

        Swah Jianoon T01 17th Janunary
        """

        temp_x_higher = self.x_coord + 1
        if (0 <= temp_x_higher < game.width):
            return game.board[self.y_coord][temp_x_higher]
        else:
            return None

    def calculate_score(self):
        """
        Return None when calculating score for default building

        Swah Jianoon T01 17th Janunary
        """
        return None
