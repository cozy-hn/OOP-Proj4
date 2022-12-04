# 패를 나눠주는 딜러입니다.
from .Hand import Hand
from .Money import Money
from .Player import Player

class Dealer:
    def __init__(self, deck: [Hand], table):
        self.deck: [Hand] = deck
        self.table = table
    def announce_winner(self, players_in: [Player]) -> Player:
        top_value: int = 0
        top_player: Player = players_in[0]
        for player in players_in:
            value: int = self.table.getValue(player.hands)
            if value > top_value:
                top_value = value
                top_player = player

        return top_player
    def distribute_cards(self, player1: Player, player2: Player) -> None:
        return

    def check_game_ended(self, players: [Player]) -> bool:
        is_game_ended = False
        looser_count: int = 0
        for i in range(len(players)):
            if players[i].getStakes() == Money(0):
                looser_count += 1
        if looser_count == len(players)-1:
            is_game_ended = True
        return is_game_ended
    
    def start_new_round(self):
        return 0
