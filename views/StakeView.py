from WordView import *

class StakeView:

    def __init__(self):
        self.nv = NumberView()
        self.wv = WordView()

    def display_stakes(self, stakes: int, pos: tuple) -> None:
        _stakes = reversed([int(i) for i in str(stakes)])
        for i, num in enumerate(_stakes):
            self.nv.display_number(num, (pos[0], pos[1] - ((i + 1) * NUM_WIDTH)))

        self.wv.display_word("WON", (pos[0], pos[1]))
