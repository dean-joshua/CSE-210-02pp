import random

class Dealer:
    def __init__(self):
        '''A constructor method for the Dealer class.'''
        self.current_card = 0
        self.next_card = 0
        self.h_or_l = ""


    def draw_card(self):
        '''A draw card method that pulls a new card'''
        list_of_cards = [1,2,3,4,5,6,7,8,9,10,11, 12, 13]
        return random.choice(list_of_cards)

    def get_current_card(self):
        '''A current card method that. The dealer draws a current card'''
        self.current_card = self.draw_card()

    def get_next_card(self):
        '''A next card method. The dealer draws the next card'''
        self.next_card = self.draw_card()

    def get_h_or_l(self):
        '''Asks the user for their guess as h or l.'''
        guessing = True
        while guessing:
            try:
                self.h_or_l = input("Higher or Lower? [h/l]: ")
                if self.h_or_l.lower() == 'h' or self.h_or_l.lower() == 'l':
                    guessing = False
                else:
                    print("Needs to be h or l.")
            except ValueError:
                print("Needs to be a string or int")
        assert self.h_or_l in ["h","l"], "Should be h or l"

    def get_points(self):
        '''Add points to local points value depending on guess. (to be added to director points)'''
        if self.next_card > self.current_card:
            if self.h_or_l == "h":
                return 100
            else:
                return 75
        elif self.current_card > self.next_card:
            if self.h_or_l == "l":
                return 100
            else:
                return 75

  