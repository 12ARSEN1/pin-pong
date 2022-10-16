#game
from pygame import *

class GameSprint(sprint.Sprint):
    def __init__(self):
        pass
    def reset(self):
        pass
class Player(GameSprint):
    def update_right(self):
        pass
    def update_left(self):
        pass
win_width  =600
win_height = 500

window = display.set_mode((win_height,win_width))
BLUE = (200,255,255)
window.fill(BLUE)

