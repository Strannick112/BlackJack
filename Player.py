from Hand import Hand


class Player:
    def __init__(self, name: str):
        self.hand = Hand()
        self.name = name

    def take_card(self, card):
        return self.hand.take_card(card)

    def discard(self):
        self.hand.discard()

    def get_points(self):
        return self.hand.get_points()

    def show_hand(self):
        for card in self.hand.cards:
            card.show()
        print(f"Кол-во очков: {self.get_points()}")
