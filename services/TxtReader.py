# 테스트 파일을 읽어오는 클래스입니다.

class TxtReader:
    def __init__(self) -> None:
        self.hands = dict()

    def read_hands(self) -> dict:

        for i in range(21):
            self.hands[str(i)] = []
            f = open(f"../src/img/{i}.txt", encoding="UTF8")
            k = 0
            while True:
                line = f.readline()
                if not line:
                    break
                self.hands[str(i)].append(line)
                k += 1

        return self.hands
