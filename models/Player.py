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
        self.__player_id: int = id
        self.__available_actions = [action for action in Action]
        self.alive: bool = True
        self.callfee: int = 0  # 콜비용
        self.betsum: int = 0  # 배팅한 돈의 총액
        self.betfee: int = 0  # 자신의 턴에 배팅 할 돈

    def bet(self, money: int) -> None:
        self.__stakes.substitute(money)

    def actions(self, first_turn: int = 0) -> [Action]:
        # 단 첫턴인 경우에는 콜 못합니다.
        # 한번 콜하면 다시는 콜 못함
        if first_turn == self.__player_id:
            return self.__available_actions[:3]
        else:
            return self.__available_actions

    def take(self, money: int) -> None:
        self.__stakes.add(money)

    def fold(self) -> None:
        pass

    def get_id(self) -> int:
        return self.__player_id
    
    def game_in(self) -> None:
        pass

    def getbetsum(self)->int:
        return self.betsum

    def set_hand(self, hands: [Hand]) -> None:
        self.hands.clear()
        self.hands.extend(hands)

    def get_id(self) -> int:
        return self.id

    def getbetfee(self) -> int:
        return self.betfee

    def get_hands(self) -> list:
        return self.hands

    def showcallbetfee(self, otherplayerbetsum: int) -> int:
        return abs(self.betsum - otherplayerbetsum)

    def showhalfbetfee(self, otherplayerbet: int, moneyonthegame: int) -> int:
        return abs(self.betsum - otherplayerbet) + (abs(self.betsum - otherplayerbet) + moneyonthegame) // 2

    def bet(self, money):
        self.money.minus(money)
        self.betsum += money

    def setturn(self, turn: int) -> None:
        self.turn: int = turn

    def getturn(self) -> int:
        return self.turn

    def survive(self) -> bool:  # getalive()
        return self.alive  # 이걸 여기서 처리할까요?

    def getbetsum(self) -> int:
        return self.betsum

    def getbetfee(self) -> int:
        return self.betfee

    def get_hands(self) -> list:
        return self.hands

    def showcallbetfee(self, otherplayerbetsum: int) -> int:
        return abs(self.betsum - otherplayerbetsum)

    def showhalfbetfee(self, otherplayerbet: int, moneyonthegame: int) -> int:
        return abs(self.betsum - otherplayerbet) + (abs(self.betsum - otherplayerbet) + moneyonthegame) // 2
    # def die(self):
    #     self.alive=False

    def call(self, otherplayerbetsum: int) -> None:
        self.callfee = abs(self.betsum - otherplayerbetsum)
        self.betfee = self.callfee
        if self.betfee > self.money.getmoney():
            self.alive = False
        self.betsum += self.betfee
        self.money.minus(self.betfee)

    def half(self, otherplayerbet: int, moneyonthegame: int) -> None:
        self.callfee = abs(self.betsum - otherplayerbet)
        self.betfee = self.callfee + (self.callfee + moneyonthegame) // 2
        if self.betfee > self.money.getmoney():
            self.alive = False
        self.betsum += self.betfee
        self.money.minus(self.betfee)

    # def quarter(self,otherplayerbet,moneyonthegame):
    #     self.callfee=abs(self.betsum-otherplayerbet)
    #     self.betfee=self.callfee+(self.callfee+moneyonthegame)/4
    #     if self.betfee>self.money:
    #         self.alive=False
    #     self.betsum+=self.betfee
    #     self.money-=self.betfee

    # def ddadang(self,otherplayerbet,otherplayercallfee):
    #     self.callfee=abs(self.betsum-otherplayerbet)
    #     self.betfee=self.callfee+otherplayercallfee
    #     if self.betfee>self.money:
    #         self.alive=False
    #     self.betsum+=self.betfee
    #     self.money-=self.betfee
