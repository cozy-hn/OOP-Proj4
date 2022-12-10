# 패를 나눠주는 딜러입니다.
from .Hand import Hand
from .Player import Player
from .Hand import Hand
from services.Round import Round
import itertools
import random
import Rule
import numpy as np 

class Dealer:
    def __init__(self, deck: [Hand], table):
        self.deck: [Hand] = deck
        self.table = table
    def announce_winner(self, player1: Player, player2: Player) -> Player:
        player1_value = Rule.calc_rules(player1.hands[0],Rule.jokbo)
        player2_value = Rule.calc_rules(player2.hands[0],Rule.jokbo)

        if player1_value < player2_value:
            return player1
        elif player1_value > player2_value:
            return player2
        # 두 플레이어의 패를 비교해서 밸류가 높은 쪽이 승리합니다.
        # 무승부는 존재하지 않습니다.
    def distribute_cards(self, player1: Player, player2: Player) -> None:
        # 플레이어에게 카드를 분배합니다.
        # 퍼블릭 메소드를 이용해서 플레이어 내부의 멤버변 수 hands에 새로운 패를 넣어줍니다.
        paeList = [i for i in range(1,29)]
        # Choose elements with different probabilities
        probabilities = [0.00526,0.00526,0.00526,0.00526,0.00526,0.00526,0.00526,0.00526,0.00526,0.00526,0.00526,0.00526,
                0.02105,0.02105,0.02105,0.02105,0.02105,0.02105,
                0.08421,0.08421, 0.08421, 0.08421,
                0.10,0.10526,0.0578,0.06316,0.07368,
                0.0738400000000002]
        
        cards= np.random.choice(paeList, 2, p=probabilities)

        player1.hands.clear()
        player2.hands.clear()
        player1.hands.extend(cards[0])
        player2.hands.extend(cards[1])


    def check_game_ended(self, player: Player, computer_player: Player) -> bool:
        is_game_ended = False
        if player.getStakes() == 0:
            is_game_ended = True
        elif computer_player.getStakes() == 0:
            is_game_ended = True
        return is_game_ended

#def calc_rules(self,paes):
#    jokbo = Rule.Jokbo.create_jokbo()
#    paes = sorted(paes, key=lambda x:x)
#    paes_str = str(paes[0]) + ',' + str(paes[1]#

#    b = jokbo.get(paes_str#

#    if b==None:
#        tmp_paes = paes[0] % 10
#        tmp_paes = paes[1] % 10
#        if tmp_paes == 0:
#            tmp_paes +=10
#        if tmp_paes == 0:
#            tmp_paes +=1#

#        #작은걸 앞으로 해준다. 해서 족보 다 일치시키기
#        if tmp_paes > tmp_paes:
#            temp = tmp_paes
#            tmp_paes = tmp_paes
#            tmp_paes = tem#

#        paes_str = str(tmp_paes) + ',' + str(tmp_paes) + ',#

#        jokbo_power = jokbo.get(paes_str#

#        if jokbo_power==None:
#            tmp_inp3 = tmp_paes + tmp_paes
#            tmp_inp3 %= 1#

#            inp3_str = str(tmp_inp3) + ',,'
#            jokbo_power = jokbo.get(inp3_str#

#    return jokbo_power


if __name__ == '__main__':
    player1 = Player()
    player2 = Player()

    Dealer.distribute_cards(player1,player2)
    print(player1.get_hands())
    print(player2.get_hands())


## test python 3. list_a = list(map(int, list_a))

