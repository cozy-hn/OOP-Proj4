# 게임을 하는 플레이어입니다.
# 컴퓨터 플레이어 클래스는 플레이어 클래스로부터 파생됩니다.
from Money import Money

class Player:
    def __init__(self, id: int, initial_bet: Money) -> None:
        self.stakes = initial_bet
        self.hands = []
        self.id = id
        
    def bet(self, money: Money) -> None:
        self.stakes.substitute(money)
    
    def fold() -> None:
        pass
    
    def game_in() -> None:
        pass
    
    def get_hands(self) -> list:
        return self.hands
    
    def get_id(self) -> int:
        return self.id
