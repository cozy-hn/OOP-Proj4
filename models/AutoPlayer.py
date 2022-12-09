# 컴퓨터 플레이어입니다. 플레이어로부터 파생됩니다. 
from .Player import Player
from .Money import Money
from random import randrange

# 컴퓨터 플레이어가 자동으로 폴드, 벳을하게 해야하는데 이 로직을 정해야합니다.
class AutoPlayer(Player):
    def __init__(self, player_id: int = 0, initial_bet: Money = Money(10000)) -> None:
        super().__init__(player_id, initial_bet)

    def auto_bet(self) -> Money:
        # 랜덤하게 혹은 특정 로직에 의해 컴퓨터는 자동으로 베팅합니다.
        # 랜덤으로 확률적으로
        bet: Money = self.__decide_bet()
        self.bet(bet)
        return bet

    def __decide_bet(self) -> Money:
        # 특정 로직에 의해 컴퓨터 플레이어가 베팅할 금액을 정합니다.
        return Money(100)
    def fold(self) -> None:
        pass

    def play(self):
        rannum=randrange(1,100)
        # hand 무엇을 받을지 확인 후 다시 수정예정
        # {1: '삼팔광땡', 2: '광땡', 3:'장땡', 4:'구땡', 5:'팔땡',
        #           6: '칠땡', 7: '육땡', 8:'오땡', 9:'사땡', 10:'삼땡',
        #           11: '이땡', 12: '일땡', 13:'알리', 14:'독사', 15:'구삥',
        #           16: '장삥', 17: '장사', 18:'세륙', 19:'아홉끗', 20:'여덟끗',
        #           21: '일곱끗', 22: '여섯끗', 23: '다섯끗', 24: '사끗', 25: '삼끗',
        #           26: '두끗', 27: '한끗', 28: '망통'}
        if self.hand in [1]:#삼팔 광땡
            if rannum in [i for i in range(1,2)]:
                self.die()
            elif rannum in [i for i in range(2,4)]:
                self.call()
            else:
                self.half()
        elif self.hand in [2,3]:#다른 광땡
            if rannum in [i for i in range(1,4)]:
                self.die()
            elif rannum in [i for i in range(4,7)]:
                self.call()
            else:
                self.half()
        elif self.hand in [3,4,5,6,7]:
            if rannum in [i for i in range(1,8)]:
                self.die()
            elif rannum in [i for i in range(8,18)]:
                self.call()
            else:
                self.half()
        elif self.hand in [8,9,10,11,12]:
            if rannum in [i for i in range(1,11)]:
                self.die()
            elif rannum in [i for i in range(11,23)]:
                self.call()
            else:
                self.half()
        elif self.hand in [13,14,15,16,17,18]:
            if rannum in [i for i in range(1,16)]:
                self.die()
            elif rannum in [i for i in range(16,36)]:
                self.call()
            else:
                self.half()
        elif self.hand in [19,20,21,22,23]:
            if rannum in [i for i in range(1,36)]:
                self.die()
            elif rannum in [i for i in range(36,76)]:
                self.call()
            else:
                self.half()
        elif self.hand in [24,25,26,27]:
            if rannum in [i for i in range(1,51)]:
                self.die()
            elif rannum in [i for i in range(51,86)]:
                self.call()
            else:
                self.half()
        else: #망통
            if rannum in [i for i in range(1,71)]:
                self.die()
            elif rannum in [i for i in range(71,96)]:
                self.call()
            else:
                self.half()