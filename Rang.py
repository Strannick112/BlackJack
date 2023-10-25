from RangSymbolException import RangSymbolException


class Rang:
    rangs = {
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "X": 10,
        "J": 1,
        "Q": 2,
        "K": 3,
        "A": 11
    }

    def __init__(self, symbol):
        if symbol in Rang.rangs.keys():
            self.symbol = symbol
            self.points = Rang.rangs[symbol]
        else:
            raise RangSymbolException("Ранга с указанным символом не существует!!!")

