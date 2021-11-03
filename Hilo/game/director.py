from game.dealer import Dealer

class Director:
    def __init__(self):
        '''A constructor method for the Director class.'''
        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()

    def start_game(self):
        ''' The start_game method for the Director class. Continues the game as long as the user is able to'''
        while self.keep_playing:
            self.get_inputs
            self.do_updates
            self.do_outputs

    def get_inputs(self):
        # Example comment 
        # Example comment 2
        #Example comment 3
        pass

    def do_updates(self):
        pass

    def do_outputs(self):
        pass