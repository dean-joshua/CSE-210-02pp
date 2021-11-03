import random

class Dealer:
    def __init__(self):
        '''A constructor method for the Dealer class.'''
        self.current_card = 0
        self.next_card = 0
        self.h_or_l = ""
        pass

    def draw_card(self):
        ''''''
        list_of_cards = [1,2,3,4,5,6,7,8,9,10,11, 12, 13]
        return random.choice(list_of_cards)

    def get_current_card(self):
        self.current_card = self.draw_card()

    def get_next_card(self):
        self.next_card = self.draw_card()

  