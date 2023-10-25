from MastException import MastException


class Mast:
    symbols = "♦♣♠♥"
    def __init__(self, symbol):
        if symbol in Mast.symbols:
            self.symbol = symbol
        else:
            raise MastException("Указанный символ масти недоступим!")
