from .building import Building


class Monument(Building):
    def __init__(self,x_coord,y_coord):
        """
        init function for Park class

        Swah Jian Oon T01 18th January
        """
        self.name = "MON"
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.counted = False
    
    def calculate_score(self, game):
        """
        calculate score for the Monument object

        Swah Jian Oon T01 18th January
        """        
        temp_list = []
        corner_count = 0
        similar_building = 0
        corner = False
        for h in range(0, game.height + 1):
            for w in range(0, game.width + 1):
                if game.board[h][w].name == self.name:
                    similar_building += 1
                    temp_list.append(game.board[h][w])

        for monument in temp_list:
            for height in [0, game.height]:
                for width in [0, game.width]:
                    if monument.x_coord == width and monument.y_coord == height:
                        corner_count +=1 
                    if self.x_coord == width and self.y_coord == height:
                        corner = True
        
        if corner_count >= 3:
            return 4
        else:
            if corner == True:
                return 2
            else:
                return 1
