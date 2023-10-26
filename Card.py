from Mast import Mast
from Rang import Rang


class Card:
    def __init__(self, rang: Rang, mast: Mast):
        self.__rang = rang
        self.__mast = mast

    def get_points(self):
        return self.__rang.points

    def get_rang(self):
        return self.__rang.symbol

    def get_mast(self):
        return self.__mast.symbol

    def show(self):
        print(
f"""-----------
|{self.__rang.symbol}{self.__mast.symbol}       |
|         |
|         |
|         |
|       {self.__rang.symbol}{self.__mast.symbol}|
-----------
""")
