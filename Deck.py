import random

from Card import Card
from DeckEmptyError import DeckEmptyError
from Mast import Mast
from Rang import Rang


class Deck:
    def __init__(self):
        self.__deck = []
        for rang in Rang.rangs.keys():
            for mast in Mast.symbols:
                self.__deck.append(Card(Rang(rang), Mast(mast)))
        self.__iter = None
        self.sort()
    
    def sort(self):
        for _ in range(100):
            first_card_index = random.randint(0, len(self.__deck) - 1)
            second_card_index = random.randint(0, len(self.__deck) - 1)
            self.__deck[first_card_index], self.__deck[second_card_index] \
                = (self.__deck[second_card_index], self.__deck[first_card_index])
        self.__iter = self.__deck.__iter__()
            
    def get_card(self):
        try:
            return next(self.__iter)
        except StopIteration:
            raise DeckEmptyError("Колода кончилась!")
    