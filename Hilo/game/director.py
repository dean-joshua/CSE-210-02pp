from game.dealer import Dealer

class Director:
    def __init__(self):
        '''A constructor method for the Director class.'''
        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()

    def start_game(self):
        ''' The start_game method for the Director class. Continues the game as long as the user can still play.'''
        while self.keep_playing:
            self.get_inputs()
            print("+---+---+---+---+")
            print(f"The current card is {self.dealer.current_card}")
            self.dealer.get_h_or_l()
            print(f"The next card is {self.dealer.next_card}")
            self.do_updates()           
            self.do_outputs()
            print("+---+---+---+---+")
            print("")

    def get_inputs(self):
        '''The get inputs method takes in all the necessary input for the game to start.'''
        self.dealer.get_current_card()
        self.dealer.get_next_card()       

    def do_updates(self):
        '''Updates the state of the game. This includes adding points when the user guesses correctly.'''
        points = self.dealer.get_points()
        if points  == 100:
            self.score += points 
        elif points  == 75:
            self.score -= points
        

    def do_outputs(self):
        '''Displays the score and choice to play again to the user.'''
        print(f"Your score is: {self.score}")
        if self.score > 0:
            choice = input("Play Again? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False
        