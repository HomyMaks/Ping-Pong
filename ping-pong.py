# Импорты
from pygame import *
from random import randint

# Константы
WIDTH = 600
HEIGHT = 500
FPS = 60
WIN_SCORE = 10
RESTART_TIME = 1000

BACKGROUND = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Экран
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Ping-Pong')
clock = time.Clock()

# Классы и спрайты
class GameSprite():
    def __init__(self, img: str, x: int, y: int, w: int, h: int):
        super().__init__()
        self.image = trasform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset():
        window.blit(self.image, (self.rect.x, self.rect.y))
        

# Игровой цикл
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        window.fill(BACKGROUND)
    
    display.update()
    clock.tick(FPS)


