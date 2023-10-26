from Deck import Deck
from Player import Player


class Game:
    def __init__(self, players):
        self.players = tuple(Player(player) for player in players)
        self.__deck = Deck()

    def __start(self):
        for player in self.players:
            player.take_card(self.__deck.get_card())

    def __is_valid(self, player):
        return (player.get_points() != 0  \
            and input("Вы хотите взять карту? (Y/n)") in {"Y", "y", "yes"})

    def __move(self, player):
        print(f"Имя игрока: {player.name}")
        player.show_hand()
        while(self.__is_valid(player)):
            player.take_card(self.__deck.get_card())
            player.show_hand()

    def play(self):
        self.__start()
        for player in self.players:
            self.__move(player)

    def check_winner(self):
        winner_points = 0
        for player in self.players:
            if winner_points < player.get_points():
                winner_points = player.get_points()

        if winner_points == 0:
            return {"winner_points": 0, "winners": tuple()}
        else:
            return {
                "winner_points": winner_points,
                "winners": tuple(
                    player
                    for player in self.players
                    if winner_points == player.get_points()
                )
            }

