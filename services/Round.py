# 한 라운드를 책임지는 클래스입니다.
from ..models.Player import Player, Action

class Round:
    def __init__(self, dealer, action_view) -> None:
        self.winner: Player = None
        self.bet_per_round: int = int(0)
        self.__action_view = action_view
        self.dealer = dealer
        self.default_bet = 1000
        self.total_bet = 0
    def add_winner(self, winner: Player) -> None:
        self.winner = winner
    def start_round(self, first_turn: int, players: list) -> int:
        # 라운드가 시작되면 턴을 돌아가면서 베팅을합니다.
        # 라운드가 끝나면 컴퓨터와 플레이어는 자신의 패를 공개하고
        # 가장 높은 밸류를 가진 패가 이깁니다.

        # 매 라운드에서
        # 첫턴이 나라면 내가 콜은 못하고 다이나 하프
        # 그리고 다음턴이 컴퓨터가 되고, 다이, 콜, 하프 가능
        # 그리고 내 턴이 되면 다이 콜 하프 가능
        # 그리고 콜 콜 하면 끝남
        # 라운드 내에서 베팅을 반복하는 것 필요
        # 베팅 금액을 정합니다.
        # 콜을 할 수 있는 돈이 없으면 게임이 끝남

        # 라운드가 시작하기 전에 패를 확인하고 죽을지 안죽을지를 결정합니다.
        # 컴퓨터의 행동
        # 다이 콜 하프 -> 랜덤(확률 조정 20% 확률로 다이)
        # 컴퓨가 콜 했을시 하프 못하게 해야함 -> 생각 조금만

        # 만약 한명이 다이 -> 다른 한명이 베팅 금액 다 가져가고 라운드 종료
        # 만약 콜 콜 -> 1. 베팅 금액이 같은 경우 2. 올인을 하는 경우
        # -> 승자 판별하고 승자에게 돈주고 라운드 종료

        computer_stakes: int = players[0].get_stakes()
        player_stakes: int = players[1].get_stakes()

        bets: [int] = [self.default_bet, self.default_bet]
        all_set: bool = False
        round_turn: int = 1
        turn = first_turn
        available_actions: [Action] = [action for action in Action]

        # 한 라운드를 시작하는 루프
        while not all_set:
            # 한 턴씩 진행합니다.
            # 둘 중에 하나가 죽으면 현재 라운드의 총 베팅 금액은 죽지않은쪽으로 갑니다.
            # 둘중에 하나라도 게임을 종료하면(exit) 바로 함수를 종료합니다.

            actions1: [Action] = players[turn].actions(first_turn)
            # 선택할 수 있는 액션만 보여줍니다.
            # 디스플레이 함수에서는 [str]로 넘겨줍니다
            self.__action_view.display(actions1)
            # 플레이어만 액션을 입력받습니다.
            action1: int = -1
            if players[turn].get_id() == 1:
                # 입력을 받는 뷰
                user_input = self.__action_view.display_input()
                action1 = available_actions[int(user_input)]
            else:
                action1 = players[turn].auto_action()
            turn = self.__take_action(action1, turn, players[turn], bets)

            actions2: Action = players[turn].actions(first_turn)
            # 선택할 수 있는 액션만 보여줍니다.
            self.__action_view.display(actions2)
            # 액션을 입력받습니다.
            actions2 = -1
            if players[turn].get_id() == 1:
                user_input = self.__action_view.display_input()
                action2 = available_actions[int(user_input)]
            else:
                action2 = players[turn].auto_action()
            turn = self.__take_action(action2, turn, players[turn], bets)

            if self.__is_round_end(action1, action2):
                all_set = True
            round_turn += 1
        self.total_bet = sum(bets)
        return self.total_bet

    def __is_round_end(self, action1: Action, action2: Action):
        is_round_end = False
        if action1 == Action.CALL and action2 == Action.CALL:
            is_round_end = True
        elif action1 == Action.DIE or action2 == Action.DIE:
            is_round_end = True
        return is_round_end

    def __take_action(self, action: Action, turn: int, player: Player, bets: [int]) -> int:
        if action == Action.EXIT:
            return int(0)
        elif action == Action.DIE:
            # player.die() ?
            pass
        elif action == Action.CALL:
            # player.call() ?
            if max(bets) > player.get_stakes():
                # 가진 돈보다 콜 해야하는 금액이 많으면 올인합니다.
                bets[turn] = player.get_stakes()
                player.bet(player.get_stakes())
            else:
                bets[turn] = max(bets)
                # 돈 빼기
        elif action == Action.HALF:
            # player.half() ?
            # 가진 돈보다 하프 해야하는 금액이 많으면 올인합니다.
            half_bet = max(bets) * 2 - player.get_stakes()
            if half_bet > player.get_stakes():
                # 가진 돈보다 하프 해야하는 금액이 많으면 올인합니다.
                bets[turn] = player.get_stakes()
                player.bet(player.get_stakes())
            else:
                bets[turn] = max(bets)
                bets[turn] += sum(bets) / 2

        turn += 1
        turn %= 2
        return turn