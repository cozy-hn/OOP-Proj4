# 게임을 하는 플레이어입니다.
# 컴퓨터 플레이어 클래스는 플레이어 클래스로부터 파생됩니다.

from models.Action import Action

class Player:
    def __init__(self, initial_stakes: int = 10000) -> None:
        self.__stakes: int = initial_stakes
        self.__hand: [int] = []
        self.__player_id: int = 1
        self.__available_actions = [action for action in Action]
        self.__actions_did_call = [Action(0), Action(1),Action(2)]
        self.__actions_on_first_turn = self.__available_actions[:3]

    def get_id(self) -> int:
        return self.__player_id
    def get_stakes(self):
        return self.__stakes
    def bet(self, money: int) -> None:
        self.__stakes -= money
    def take(self, money: int) -> None:
        self.__stakes += money
    def actions(self, first_turn: int = 0, did_call: bool = False) -> [Action]:
        # 단 첫턴인 경우에는 콜 못합니다.
        # 한번 콜하면 콜 다이 밖에 못함
        if first_turn == self.__player_id:
            return self.__actions_on_first_turn
        elif did_call:
            return self.__actions_did_call
        else:
            return self.__available_actions

    def set_hand(self, hand: [int]) -> None:
        self.__hand = hand

    def get_hand(self) -> list:
        return self.__hand
