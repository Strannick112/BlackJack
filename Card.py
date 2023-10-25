from Mast import Mast
from Rang import Rang


class Card:
    def __init__(self, rang: Rang, mast: Mast):
        self.rang = rang
        self.mast = mast

    def get_points(self):
        return self.rang.points

    def show(self):
        print(
f"""
-----------
|{self.rang.symbol}{self.mast.symbol}       |
|         |
|         |
|         |
|         |
|       {self.rang.symbol}{self.mast.symbol}|
""")