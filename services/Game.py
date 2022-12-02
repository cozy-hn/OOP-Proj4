from models import Player, Dealer
import Round


# 한 게임을 책임지는 클래스입니다.
class Game:
    def __init__(self):
        self.rounds = []
        self.winner = None
        self.totalBet = None
        self.dealer = None
        self.players = []

    def start_game(self):
        self.dealer = Dealer()

        for i in range(4):
            self.players.append(self.create_player())

        while True:
            if self.dealer.check_game_ended(self.players):
                self.end_game()

            round = Round()
            self.rounds.append(round)

            round.start_round()

    def end_game(self):
        pass

    def create_player(self):
        return Player()

    def show_opponent_hands(self):
        pass

    def display_player(self):
        pass

    def display_hand(self):
        pass
