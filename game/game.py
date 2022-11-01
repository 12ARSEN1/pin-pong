#game
from pygame import *

class GameSprint(sprite.Sprite):
    def __init__(self,pl_image,pl_x,pl_y,pl_s,weidth,height):
        super().__init__()
        self.image = transform.scale(image.load(pl_image),(weidth,height))
        self.speed = pl_s
        self.rect = self.image.get_rect()
        self.rect.x  = pl_x
        self.rect.y  = pl_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprint):
    def update_right(self):
        k= key.get_pressed()
        if k[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if k[K_DOWN] and self.rect.y<420:
            self.rect.y += self.speed
    def update_left(self):
        k= key.get_pressed()
        if k[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if k[K_s] and self.rect.y<420:
            self.rect.y += self.speed
win_width  =600
win_height = 500

window = display.set_mode((win_width,win_height))
BLUE = (200,255,255)
window.fill(BLUE)
racet_left =Player("cyborg.png",30,200,4,70,100)
racet_right =Player("cyborg.png",520,200,4,70,100)
ball = GameSprint("asteroid.png",200,200,4,50,50)
# прапорці, які відповідають за стан гри
game = True
finish = False

split_x = 3
split_y = 3
clock = time.Clock() # годинник 
FPS = 60 #кількість кадрів в секунду

# ігровий цикл
while game:
    for e in event.get():  # перевірка всіх подій
        if e.type == QUIT: # тип подій - закрити вікно
            game = False   # закінчуємо цикл while
    if finish != True:
        window.fill(BLUE)
        racet_left.update_left()
        racet_right.update_right()
        ball.rect.x+=split_x
        ball.rect.y+=split_y
        if ball.rect.y > win_height -50 or ball.rect.y < 0:
            split_y*=-1
        if ball.rect.x < 0:
            game = True
            finish = True
        if ball.rect.x > 600:
            game = True
            finish = True
        ball.reset()
        racet_left.reset()
        racet_right.reset()
    display.update()
    clock.tick(FPS)
