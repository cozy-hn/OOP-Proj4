# 게임을 하는 플레이어입니다.
# 컴퓨터 플레이어 클래스는 플레이어 클래스로부터 파생됩니다.
from .Money import Money
from .Hand import Hand

class Player:
    def __init__(self, id: int = 1, initial_bet: Money = Money(10000)) -> None:
        self.stakes: Money = initial_bet
        self.hands: [Hand] = []
        self.id: int = id
        
    def bet(self, money: Money) -> None:
        self.stakes.substitute(money)
    
    def fold(self) -> None:
        pass
    
    def game_in(self) -> None:
        pass
    
    def get_hands(self) -> []:
        return self.hands

    def set_hand(self, hands: [Hand]) -> None:
        self.hands.clear()
        self.hands.extend(hands)

    def get_id(self) -> int:
        return self.id
