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

# прапорці, які відповідають за стан гри
game = True
finish = False

clock = time.Clock() # годинник 
FPS = 60 #кількість кадрів в секунду

# ігровий цикл
while game:
    for e in event.get():  # перевірка всіх подій
        if e.type == QUIT: # тип подій - закрити вікно
            game = False   # закінчуємо цикл while
    if finish != True:
        window.fill(fon)
    display.update()
    clock.tick(FPS)
