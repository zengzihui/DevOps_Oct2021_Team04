import copy
from .building import Building


class Park(Building):
    def __init__(self,x_coord,y_coord):
        """
        init function for Park class

        Swah Jian Oon T01 18th January
        """
        self.name = "PRK"
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.counted = False
    
    def calculate_score(self, game):
        """
        calculate score for the Park object

        Swah Jian Oon T01 18th January
        """
        temp_park = []
        temp_count = 0
        for h in range(0,game.height):
            for w in range(0,game.width):
                all_park = []
                if game.board[h][w].name == "PRK":
                    all_park = game.board[h][w].check_left(game,all_park)
                    all_park = game.board[h][w].check_right(game,all_park)
                    all_park = game.board[h][w].check_top(game, all_park)
                    all_park = game.board[h][w].check_bottom(game, all_park)
                    all_park.append(game.board[h][w])
                if len(all_park) > temp_count:
                    temp_count = len(all_park)
                    temp_park = copy.deepcopy(all_park)
        
        total_count = 0
        for park in temp_park:
            if park.counted == True:
                total_count += 1

        if total_count == 0:
            self.counted = True
            return 1
        elif total_count == 1:
            self.counted = True
            return 2
        elif total_count == 2:
            self.counted = True
            return 5
        elif total_count == 3:
            self.counted = True
            return 8
        elif total_count == 4:
            self.counted = True
            return 6
        else:
            self.counted = True
            return 1
            
    def check_left(self,game,list):
        """
        recursively check if left side of board has park

        Swah Jianoon T01 18th Janunary
        """
        if self.get_left_building(game) == None or self.get_left_building(game).name != self.name:
            return list
        else:
            building = self.get_left_building(game)
            list.append(building)
            return building.check_left(game,list)

    def check_right(self,game,list):
        """
        recursively check if right side of board has park
                          
        Swah Jianoon T01 18th Janunary
        """
        if self.get_right_building(game) == None or self.get_right_building(game).name != self.name:
            return list
        else:
            building = self.get_right_building(game)
            list.append(building)
            return building.check_right(game,list) 
    
    def check_top(self,game,list):
        """
        recursively check if top side of board has park
        Swah Jianoon T01 18th Janunary
        """
        if self.get_top_building(game) == None or self.get_top_building(game).name != self.name:
            return list
        else:
            building = self.get_top_building(game)
            list.append(building)
            return building.check_top(game,list)

    def check_bottom(self,game,list):
        """
        recursively check if bottom side of board has park
                          
        Swah Jianoon T01 18th Janunary
        """
        if self.get_bot_building(game) == None or self.get_bot_building(game).name != self.name:
            return list
        else:
            building = self.get_bot_building(game)
            list.append(building)
            return building.check_bottom(game,list) 