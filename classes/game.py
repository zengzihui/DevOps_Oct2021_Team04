class Game:

    def __init__(self):
        """
        init function for game class
        default turn number is 1
        """
        self.turn_num = 1

    def print_turn_num(self):
        """
        prints turn number based on self.turn_num in game class
        """
        print("Turn {}".format(self.turn_num))
