import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from services.TxtReader import TxtReader
from console.screen import sc

NUM_WIDTH = 8
NUM_HEIGHT = 7

WORD_HEIGHT = 7

class NumberView:

    def __init__(self):
        self.numbers = TxtReader().read_numbers()

    def display_number(self, num: int, pos: tuple) -> None:
        for i in range(NUM_HEIGHT):
            with sc.location(pos[0]+i, pos[1]):
                print(self.numbers[str(num)][i], end="")
        return

class WordView:

    def __init__(self):
        self.words = TxtReader().read_words()

    def display_word(self, word: str, pos: tuple) -> None:
        for i in range(WORD_HEIGHT):
            with sc.location(pos[0]+i, pos[1]):
                print(self.words[word][i], end="")
        return