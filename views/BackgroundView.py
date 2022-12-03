from console.utils import cls, set_title
from console.screen import sc
import os

WIDTH = 192
HEIGHT = 55

class Background:

     def __init__(self):
         os.system(f"mode {WIDTH},{HEIGHT}")
         os.system("color 0f")
         cls()

screen = Background()

