from console.screen import sc
import os
from HandView import HandView
from WordView import NumberView, WordView, NUM_HEIGHT, NUM_WIDTH

WIDTH = 192
HEIGHT = 56

class Background:
    def __init__(self):
        os.system(f"mode {WIDTH},{HEIGHT}")
        os.system("color 0f")
        os.system("cls")

        # Draw Player Box
        for i in range(23):
            with sc.location(i-1, 63):
                print("|")

            with sc.location(HEIGHT - (i+1), 63):
                print("|")

        for i in range(63):
            with sc.location(22, i):
                print("-")

            with sc.location(HEIGHT - 24, i):
                print("_")

        # Draw Input Menu Box
        for i in range(35):
            with sc.location(HEIGHT - (i + 2), 128):
                print("|")

        for i in range(63):
            with sc.location(HEIGHT - 36, 128 + i):
                print("-")

        for i, word in enumerate(["EXIT", "CALL", "HALF", "DIE"]):
            NumberView().display_number(i, (HEIGHT - 35 + (i * (NUM_HEIGHT+2)), 130))
            WordView().display_word(word, (HEIGHT - 35 + (i * (NUM_HEIGHT+2)), 130 + (2 * NUM_WIDTH)))

#test
screen = Background()
HandView().display_hand(0, (3, 7))
HandView().display_hand(1, front=False)

# with sc.location(HEIGHT-2,129):
#     print(123)

while True:
    with sc.location(HEIGHT - 37, 128):
        a = input("CHOICE : ")
        if a:
            break
