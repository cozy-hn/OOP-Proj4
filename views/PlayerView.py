from WordView import *
from StakeView import StakeView

PLAYER = (34, 1)
COMPUTER = (1, 1)

class PlayerView:

    def __init__(self):
        self.wv = WordView()
        self.nv = NumberView()
        self.sv = StakeView()

    def display_player(self, player: int, stakes: int = 0) -> None:
        if player == 0:
            self.__display_player_state("PLAYER", PLAYER, stakes)

        else:
            self.__display_player_state("COM", COMPUTER, stakes)

    def __display_player_state(self, word: str, pos: tuple, stakes: int):
        self.wv.display_word(word, (pos[0], pos[1]))
        self.sv.display_stakes(stakes, (pos[0] + (WORD_HEIGHT + 7), 48))
