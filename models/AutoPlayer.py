# 컴퓨터 플레이어입니다. 플레이어로부터 파생됩니다. 
from .Player import Player
from random import randrange
from Player import Action
# 컴퓨터 플레이어가 자동으로 폴드, 벳을하게 해야하는데 이 로직을 정해야합니다.
class AutoPlayer(Player):
    def __init__(self, player_id: int = 0, initial_bet: int = int(10000)) -> None:
        super().__init__(player_id, initial_bet)

    def __decide_bet(self) -> int:
        # 특정 로직에 의해 컴퓨터 플레이어가 베팅할 금액을 정합니다.
        return int(100)

    def auto_action(self) -> Action:
        rannum=randrange(1,100)
        if self.hand in [1]:#삼팔 광땡
            if rannum in [i for i in range(1,2)]:
                return Action.DIE
            elif rannum in [i for i in range(2,4)]:
                return Action.CALL
            else:
                return Action.HALF
        elif self.hand in [2,3]:#다른 광땡
            if rannum in [i for i in range(1,4)]:
                return Action.DIE
            elif rannum in [i for i in range(4,7)]:
                return Action.CALL
            else:
                return Action.HALF
        elif self.hand in [3,4,5,6,7]:
            if rannum in [i for i in range(1,8)]:
                return Action.DIE
            elif rannum in [i for i in range(8,18)]:
                return Action.CALL
            else:
                return Action.HALF
        elif self.hand in [8,9,10,11,12]:
            if rannum in [i for i in range(1,11)]:
                return Action.DIE
            elif rannum in [i for i in range(11,23)]:
                return Action.CALL
            else:
                return Action.HALF
        elif self.hand in [13,14,15,16,17,18]:
            if rannum in [i for i in range(1,16)]:
                return Action.DIE
            elif rannum in [i for i in range(16,36)]:
                return Action.CALL
            else:
                return Action.HALF
        elif self.hand in [19,20,21,22,23]:
            if rannum in [i for i in range(1,36)]:
                return Action.DIE
            elif rannum in [i for i in range(36,76)]:
                return Action.CALL
            else:
                return Action.HALF
        elif self.hand in [24,25,26,27]:
            if rannum in [i for i in range(1,51)]:
                return Action.DIE
            elif rannum in [i for i in range(51,86)]:
                return Action.CALL
            else:
                return Action.HALF
        else: #망통
            if rannum in [i for i in range(1,71)]:
                return Action.DIE
            elif rannum in [i for i in range(71,96)]:
                return Action.CALL
            else:
                return Action.HALF