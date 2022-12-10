from views.PlayerView import PlayerView
from views.WordView import WordView

POS_WINNER = (25, 1)

class WinnerView(PlayerView):

    def __init__(self):
        WordView.__init__(self)

    def display_winner(self, winner: int):
        if winner == 0:
            self.display_word("WIN", POS_WINNER)
        else:
            self.display_word("LOSE", POS_WINNER)