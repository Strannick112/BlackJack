from Card import Card


class Hand:
    def __init__(self):
        self.cards = []
        self.__points = 0

    def take_card(self, card: Card):
        self.cards.append(card)
        self.__points += card.get_points()

    def discard(self):
        self.cards = []
        self.__points = 0

    def get_points(self):
        return 0 if self.__points > 21 else self.__points

    # def get_points(self):
    #     sum = 0
    #     for card in self.cards:
    #         sum += card.get_points()
    #     return 0 if sum > 21 else sum