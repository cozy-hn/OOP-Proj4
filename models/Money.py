# 베팅 금액을 책임지는 클래스입니다.
class Money:
    def __init__(self, amount: int = 0, currency: str = "won"):
        #맴버변수 초기화
        self.amount = amount
        self.currency = currency

    def set_amount(self : int):
        print("배팅할 금액을 얼마로 설정하시겠습니까? ")
        self.amount = input() 

    def set_currency(self : str):
        # 화폐 종류는 원으로 통일합시다!
        print("화폐의 종류가 무엇인가요? ")
        self.currency = input() 

    def get_amount(self):
        return self.amount

    def get_currency(self):
        return self.currency
