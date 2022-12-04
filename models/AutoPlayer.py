# 컴퓨터 플레이어입니다. 플레이어로부터 파생됩니다. 
from .Player import Player
from .Money import Money

class AutoPlayer(Player):
    def __init__(self, id: int, initial_bet: Money) -> None:
        super().__init__(id, initial_bet)