import random

class Dealer:
    def __init__(self):
        '''A constructor method for the Dealer class.'''
        self.current_card = 0
        self.next_card = 0
        self.h_or_l = ""
        pass

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

    def get_h_or_l():
        pass

    def get_points():
        pass

  