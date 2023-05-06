from pygame import *

window = display.set_mode((600, 500))
display.set_caption('Пин-понг')
background = transform.scale(image.load('pin-pong.png'), (600, 500))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 2:
            self.rect.y -= 2
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += 2
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >2:
            self.rect.y -= 2
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += 2


class boll(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)











game = True

shar = boll('Group 1 (1).png',300,250,4)

p1 = Player('Rectangle 1 (1).png',3,250,2)
p2 = Player('Rectangle 1 (1).png',500,250,2)

while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    #игроки
    p1.update_left()
    p1.reset()

    p2.update_right()
    p2.reset()

    #шар
    shar.reset()

    FPS = 60
    display.update()



