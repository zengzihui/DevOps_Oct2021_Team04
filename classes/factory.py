from .building import Building


class Factory(Building):
    """
    init function for Factory class

    Swah Jian Oon T01 9th December
    """
    def __init__(self, x_coord, y_coord):
        self.name = "FAC"
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.counted = False
    
    def calculate_score(self,game):
        """
        This function calculates the score for a factory object on the game board
                    
        Swah Jianoon T01 17th Janunary
        """
        similar_building = 0
        temp_list = []
        for h in range(0, game.height + 1):
            for w in range(0, game.width + 1):
                if game.board[h][w].name == self.name:
                    similar_building += 1
                    temp_list.append(game.board[h][w])
        
        if similar_building <= 4:
            self.counted = True
            return similar_building
        else: 
            counted = 0 
            for fac in temp_list:
                if fac.counted:
                    counted+= 1
            if counted >= 4: 
                self.counted = True
                return 1
            else: 
                self.counted = True
                return 4

        

