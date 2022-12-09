# 게임을 하는 플레이어입니다.
# 컴퓨터 플레이어 클래스는 플레이어 클래스로부터 파생됩니다.
from .Hand import Hand
from enum import Enum
class Action(Enum):
    EXIT = 0
    DIE = 1
    CALL = 2
    HALF = 3
class Player:
    def __init__(self, player_id: int = 1, initial_bet: int = 10000) -> None:
        self.__stakes: int = initial_bet
        self.__hand: [str] = []
        self.__player_id: int = player_id
        self.__available_actions = [action for action in Action]


    def bet(self, money: int) -> None:
        self.__stakes-=money

    def take(self, money: int) -> None:
        self.__stakes+=money
        
    def actions(self, first_turn: int = 0) -> [Action]:
        # 단 첫턴인 경우에는 콜 못합니다.
        # 한번 콜하면 다시는 콜 못함
        if first_turn == self.__player_id:
            return self.__available_actions[:3]
        else:
            return self.__available_actions
    def fold(self) -> None:
        pass

    def get_id(self) -> int:
        return self.__player_id
    
    def game_in(self) -> None:
        pass

    def set_hand(self, hands: [Hand]) -> None:
        self.__hand.clear()
        self.__hand.extend(hands)

    def get_id(self) -> int:
        return self.__player_id

    def get_hands(self) -> list:
        return self.__hand
    
    def get_stakes(self)->int:
        return self.__stakes


