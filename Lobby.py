from Game import Game


class Lobby:
    def __init__(self):
        self.game = Game(self.__input_player_names())

    def __input_player_names(self):
        count = int(input("Введите количество игроков"))
        return tuple(input(f"Введите имя игрока {index}") for index in range(count))

    def play(self):
        return self.game.play()
