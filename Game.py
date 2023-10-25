from Deck import Deck
from Player import Player


class Game:
    def __init__(self, players):
        self.players = tuple(Player(player) for player in players)
        self.deck = Deck()

    def start(self):
        for player in self.players:
            player.take_card(self.deck.get_card())

    def __is_valid(self, player):
        return (player.get_points() != 0  \
            and input("Вы хотите взять карту? (Y/n)") in {"Y", "y", "yes"})

    def move(self, player):
        player.show_hand()
        while(self.__is_valid(player)):
            player.take_card(self.deck.get_card())
            player.show_hand()

    def play(self):
        self.start()
        for player in self.players:
            self.move(player)
        self.check_winner()

    def check_winner(self):
        winner_points = 0
        for player in self.players:
            if winner_points < player.get_points():
                winner_points = player.get_points()

        if winner_points == 0:
            print("Все игроки проиграли")
        for player in self.players:
            if winner_points == player.get_points():
                print(f"Игрок {player.name} победил с счётом {winner_points}")

