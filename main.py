from pygame import *

window = display.set_mode((600, 500))
display.set_caption('Пин-понг')
background = transform.scale(image.load('123.png'), (600, 500))
font.init()

speed_x = 3
speed_y = 3



font1 = font.Font(None, 35)
font2 = font.Font(None, 35)

lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0 , 0))
lose2 = font2.render('PLAYER 2 LOSE!', True, (0, 180 ,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 150))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.image = transform.scale(image.load(player_image), (25, 100))
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


class ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.image = transform.scale(image.load(player_image), (65, 65))












game = True
finish = False

shar = ball('Group 1 (1).png',255,250,4)

p1 = Player('pin-pong.png',10,250,2)
p2 = Player('pin-pong.png',560,250,2)

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

    if finish != True:
        shar.rect.x += speed_x
        shar.rect.y += speed_y

    if shar.rect.y > 500-50 or shar.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(p1, shar) or sprite.collide_rect(p2, shar):
        speed_x *= -1

    if shar.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 250))

    if shar.rect.x > 600:
        finish = True
        window.blit(lose2, (200, 250))




    FPS = 60
    display.update()



