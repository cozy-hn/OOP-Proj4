# The computer player class is derived from the player class.
from models.Player import Player
from random import randrange
from models.Action import Action


class AutoPlayer(Player):
    def __init__(self, initial_stakes: int = 10000) -> None:
        Player.__init__(self, initial_stakes)
        self.__player_id = 0

    def __decide_bet(self) -> int:
        return int(100)

    def auto_action(self) -> Action:
        # The specific logic determines which batting method
        #Create a random number from 1 to 100, which determines HALF, CALL, and DIE.
        rannum=randrange(1,100)
        if self.__hand in [1]:
            if rannum in [i for i in range(1,2)]:
                return Action.DIE
            elif rannum in [i for i in range(2,4)]:
                return Action.CALL
            else:
                return Action.HALF
        elif self.__hand in [2,3]:
            if rannum in [i for i in range(1,4)]:
                return Action.DIE
            elif rannum in [i for i in range(4,7)]:
                return Action.CALL
            else:
                return Action.HALF
        elif self.__hand in [3,4,5,6,7]:
            if rannum in [i for i in range(1,8)]:
                return Action.DIE
            elif rannum in [i for i in range(8,18)]:
                return Action.CALL
            else:
                return Action.HALF
        elif self.__hand in [8,9,10,11,12]:
            if rannum in [i for i in range(1,11)]:
                return Action.DIE
            elif rannum in [i for i in range(11,23)]:
                return Action.CALL
            else:
                return Action.HALF
        elif self.__hand in [13,14,15,16,17,18]:
            if rannum in [i for i in range(1,16)]:
                return Action.DIE
            elif rannum in [i for i in range(16,36)]:
                return Action.CALL
            else:
                return Action.HALF
        elif self.__hand in [19,20,21,22,23]:
            if rannum in [i for i in range(1,36)]:
                return Action.DIE
            elif rannum in [i for i in range(36,76)]:
                return Action.CALL
            else:
                return Action.HALF
        elif self.__hand in [24,25,26,27]:
            if rannum in [i for i in range(1,51)]:
                return Action.DIE
            elif rannum in [i for i in range(51,86)]:
                return Action.CALL
            else:
                return Action.HALF
        else:
            if rannum in [i for i in range(1,71)]:
                return Action.DIE
            elif rannum in [i for i in range(71,96)]:
                return Action.CALL
            else:
                return Action.HALF
