from ..models.Player import Player
from ..models.Dealer import Dealer
from ..models.AutoPlayer import AutoPlayer
from ..views.HandView import HandView
from ..views.BettingView import BettingView
from ..views.BackgroundView import Background
from ..views.NumberView import NumberView
from ..views.StakeView import StakeView
from ..views.WordView import WordView
from ..views.PlayerView import PlayerView

import Round

# 한 게임을 책임지는 클래스입니다.
class Game:
    def __init__(self):
        self.rounds: list = []
        self.winner: Player = None
        self.totalBet: int = None
        self.dealer: Dealer = None
        # 플레이어들 중 첫번째는 항상 컴퓨터입니다.
        self.computer_player = None
        self.player = None
        # 패를 보여줄 뷰를 가집니다.
        self.hand_view: HandView = None
        self.background_view: Background = None
        self.betting_view: BettingView = None
        self.number_view: NumberView = None
        self.player_view: PlayerView = None
        self.stake_view: StakeView = None
        self.word_view: WordView = None

    def start_game(self) -> None:
        self.hand_view: HandView = HandView()
        self.background_view: Background = Background()
        self.betting_view: BettingView = BettingView()
        self.player_view: PlayerView = PlayerView()
        self.stake_view: StakeView = StakeView()

        # 딜러를 초기화합니다.
        self.dealer = Dealer()
        # 판돈을 정합니다. -> 라운드마다 처음에 고정인데 -> 베팅을 하면 커진다
        # 예) 1000원 -> 플레이어당 천원씩 깔림
        # 플레이어와 컴퓨터 플레이어를 생성합니다.
        self.player = self.create_player(10000)
        self.computer_player = AutoPlayer(10000)

        # 게임이 끝나지 않았으면 게임을 계속합니다.
        # 매번 한 라운드를 생성합니다.
        # 종료조건: 기본 베팅 금액보다 돈이 적으면 게임 종료
        # 라운드마다 플레이어와 컴퓨터가 각자 베팅한 금액의 총합에 대한 정보가 어딘가 있어야한다.(라운드, 딜러)
        # -> 라운드로 합시다.
        # 첫 턴은 항상 플레이어입니다. game_turn이 True이면 플레이어 턴, False이면 컴퓨터 턴입니다.
        game_turn: bool = True
        while not self.dealer.check_game_ended(self.player, self.computer_player):
            game_round: Round = Round(self.dealer, self.background_view)
            # 라운드가 생성되면 딜러가 패를 분배합니다.
            self.dealer.distrubute_hands(self.player, self.computer_player)
            
            # 패가 분배되면 플레이어는 패를 확인합니다.
            # 패는 콘솔창에 출력합니다.
            self.hand_view.display_hand(self.player, self.player.get_hands(), front=True)

            # 라운드가 시작됩니다. 베팅이 반복됩니다.
            game_round.start_round(game_turn, self.player, self.computer_player)

            # 딜러가 승자를 판별합니다.
            round_winner: Player = self.dealer.announce_winner(self.player, self.computer_player)

            # 라운드에 승자를 추가합니다.
            # 라운드 승자와 얻은 금액을 입력합니다.
            game_round.add_winner(round_winner)
            # 라운드를 진행된 라운드에 추가하는 것은 라운드가 끝나고 마지막에 합니다.
            # game_round를 카피해서 넣어야할 듯?
            self.rounds.append(game_round)
            
        # 게임이 끝나면 승자와 최종 승리 금액을 출력합니다.
        winner: Player = self.player if self.player.get_stakes() > self.computer_player.get_stakes() else self.computer_player
        # 승자를 출력하는 뷰 만들어야할 듯
        # 패의 족보? 값? 이걸 보여주는 뷰가 필요
        # 같은 숫자의 패는 이미지 하나만
        
    def end_game(self) -> None:
        self.is_game_ended = True

    def create_player(self, bet_money: int) -> Player:
        return Player(bet_money)

    def show_opponent_hands(self) -> None:
        pass

    def display_player(self) -> None:
        pass

    def display_hand(self):
        pass
