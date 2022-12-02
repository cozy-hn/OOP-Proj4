# 패를 나눠주는 딜러입니다.
from Rule import rule 

class Dealer:
    def __init__(self):
        pass
    def announce_winner():
        return 0
    def distribute_cards():
        return 0
    def check_game_ended(self, players: list) -> bool:
        is_game_ended = False
        looser_count: int = 0
        for i in range(len(players)):
            if players[i].getStakes() == Money(0):
                looser_count += 1
        if looser_count == len(players)-1:
            is_game_ended = True
        return is_game_ended
    
    def start_new_round():
        return 0
