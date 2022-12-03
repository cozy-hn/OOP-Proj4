# 베팅 금액을 책임지는 클래스입니다.
class Money:
    def __init__(self, amount = None, currency = None):

        # 입력하지 않은 경우(필요없는 경우 제거 요망)
        if amount == None :
            self.amount = 0
        if currency == None : 
            self.currency = " "

        #맴버변수 초기화
        self.amount = amount
        self.currency = currency

    def setAmount(self : int):
        print("배팅할 금액을 얼마로 설정하시겠습니까? ")
        self.amount = input() 

    def setCurrency(self : str):
        print("화폐의 종류가 무엇인가요? ")
        self.currency = input() 

    def getAmount(self):
        return self.amount

    def getCurrency(self):
        return self.currency